"""Chart-setup score: how bullish is the daily chart right now (set 2026-10-14).

Ryan, live turn 2026-10-14, after a TrendSpider "falling wedges everywhere" post: *"rank
the names selected in the quality stock watch routine by most bullish chart setups"*.

score() reads one name's daily closes + volume and returns a 0-100 setup score, a
label, the best pattern found, its trigger price and the confirmations behind it.
Pure functions, no network. report.py builds setups.json each morning for the Quality
@ 200-day list (build()), and quality_watch.py ranks and prints from that cache.

What it looks for (closes only: FMP's light history has no high/low):
  PATTERNS (the best one counts):
    falling wedge  - two falling trendlines through swing highs and swing lows that
                     converge (the upper one falls faster). Trigger = upper line.
    double bottom  - two swing lows within 3%, >= 10 sessions apart, a >= 5% bounce
                     between them. Trigger = the bounce high (neckline).
    bull flag      - a >= 10% run in <= 20 sessions, then a pullback that gives back
                     <= half of it. Trigger = the run's high.
  A pattern is worth more once price closes ABOVE its trigger (breakout) than while
  it is still forming, and more when the breakout came on above-average volume.
  CONFIRMATIONS: higher low, RSI(14) bullish divergence, MACD cross up, close above a
  rising 20-day EMA, up-day volume > down-day volume, 50-day reclaimed.
  PENALTIES: a fresh 60-day closing low (falling knife); below a falling 50-day.

HONEST LIMIT: no backtest. Pattern studies (Bulkowski, Encyclopedia of Chart Patterns)
report these break upward more often than not, but this scorer's exact rules are
unproven. It ranks a watch list for Ryan's eyes; it is NOT a gate or filter on the
sleeves (the standing ban on unattended filters applies) and it never trades.
"""
from __future__ import annotations

import json
from pathlib import Path

CACHE = Path(__file__).resolve().parent / "setups.json"

PIVOT_K = 3                 # a swing high/low is the extreme of +/- 3 sessions
WEDGE_LOOKBACKS = (40, 60, 90, 120)
FRESH_BREAKOUT = 5          # a breakout within the last 5 sessions is "fresh"
NEAR_TRIGGER = 0.03         # within 3% under the trigger = "near"

BANDS = ((60, "STRONG"), (35, "CONSTRUCTIVE"), (15, "NEUTRAL"), (0, "WEAK"))


# ---------------------------------------------------------------- helpers
def _ema(xs: list[float], span: int) -> list[float]:
    k, out = 2 / (span + 1), []
    for x in xs:
        out.append(x if not out else x * k + out[-1] * (1 - k))
    return out


def _sma(xs: list[float], n: int, end: int | None = None) -> float | None:
    end = len(xs) if end is None else end
    return sum(xs[end - n:end]) / n if end >= n else None


def _rsi_series(xs: list[float], n: int = 14) -> list[float | None]:
    out: list[float | None] = [None] * len(xs)
    if len(xs) <= n:
        return out
    g = sum(max(xs[i] - xs[i - 1], 0) for i in range(1, n + 1)) / n
    l = sum(max(xs[i - 1] - xs[i], 0) for i in range(1, n + 1)) / n
    out[n] = 100 - 100 / (1 + g / l) if l else 100.0
    for i in range(n + 1, len(xs)):
        d = xs[i] - xs[i - 1]
        g = (g * (n - 1) + max(d, 0)) / n
        l = (l * (n - 1) + max(-d, 0)) / n
        out[i] = 100 - 100 / (1 + g / l) if l else 100.0
    return out


def pivots(xs: list[float], k: int = PIVOT_K) -> tuple[list[int], list[int]]:
    """Indexes of swing highs and swing lows (strict extreme of the +/- k window)."""
    hi, lo = [], []
    for i in range(k, len(xs) - k):
        w = xs[i - k:i + k + 1]
        if xs[i] == max(w) and w.count(xs[i]) == 1:
            hi.append(i)
        if xs[i] == min(w) and w.count(xs[i]) == 1:
            lo.append(i)
    return hi, lo


def _fit(points: list[tuple[int, float]]) -> tuple[float, float]:
    """Least-squares slope and intercept."""
    n = len(points)
    mx = sum(p[0] for p in points) / n
    my = sum(p[1] for p in points) / n
    sxx = sum((p[0] - mx) ** 2 for p in points)
    slope = sum((p[0] - mx) * (p[1] - my) for p in points) / sxx if sxx else 0.0
    return slope, my - slope * mx


def _chrono(rows_desc: list[dict]) -> tuple[list[float], list[float]]:
    """FMP rows (newest first, 'price'/'close' + 'volume') -> oldest-first lists."""
    closes, vols = [], []
    for r in reversed(rows_desc or []):
        p = r.get("price", r.get("close"))
        if p is None:
            continue
        closes.append(float(p))
        vols.append(float(r.get("volume") or 0))
    return closes, vols


def _breakout_age(xs: list[float], line) -> int | None:
    """Sessions since the close first crossed above line(i) and stayed above; None if
    the latest close is not above it or the cross is older than FRESH_BREAKOUT * 2."""
    last = len(xs) - 1
    if xs[last] <= line(last):
        return None
    for age in range(0, FRESH_BREAKOUT * 2):
        i = last - age - 1
        if i < 0:
            return None
        if xs[i] <= line(i):
            return age
    return None


def _vol_confirmed(vols: list[float], age: int) -> bool:
    """Any of the breakout sessions traded above its 20-day average volume."""
    last = len(vols) - 1
    for i in range(last - age, last + 1):
        avg = _sma(vols, 20, i)
        if avg and vols[i] > 1.2 * avg:
            return True
    return False


# ---------------------------------------------------------------- patterns
TOUCH_TOL = 0.015           # a swing point within 1.5% of a line "touches" it


def _edge(xs: list[float], idx: list[int], lo: int, hi: int, above: bool):
    """Best trendline through two of the swing points idx (all inside [lo, hi]) that
    no close in [lo, hi] crosses by more than 1%: resistance when above=True, support
    otherwise. Best = most touches, then the longest span. Returns (slope, intercept,
    touches) or None."""
    best = None
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            i, j = idx[a], idx[b]
            if j - i < 5:
                continue
            m = (xs[j] - xs[i]) / (j - i)
            c = xs[i] - m * i
            if above and any(xs[k] > (m * k + c) * 1.01 for k in range(lo, hi + 1)):
                continue
            if not above and any(xs[k] < (m * k + c) * 0.99 for k in range(lo, hi + 1)):
                continue
            t = sum(1 for k in idx if abs(xs[k] / (m * k + c) - 1) <= TOUCH_TOL)
            key = (t, j - i)
            if best is None or key > best[0]:
                best = (key, m, c, t)
    return None if best is None else best[1:]


def falling_wedge(xs: list[float], vols: list[float]) -> dict | None:
    """Resistance drawn down from the lookback's highest close, support under the lows
    since, both falling and converging (the upper line falls faster)."""
    best = None
    last = len(xs) - 1
    hi_all, lo_all = pivots(xs)
    for L in WEDGE_LOOKBACKS:
        if len(xs) < L + PIVOT_K + 1:
            continue
        window = range(last - L, last + 1)
        start = max(window, key=lambda i: xs[i])            # the anchor high
        if last - start < 20:
            continue
        body_end = last - 1      # the latest close may already be breaking out
        hp = [i for i in hi_all if start <= i <= body_end] or []
        if start not in hp:
            hp = [start] + hp
        lp = [i for i in lo_all if start < i <= body_end]
        if len(hp) < 2 or len(lp) < 2:
            continue
        # resistance: no close between the anchor and the breakout window above it
        up = _edge(xs, hp, start, last - FRESH_BREAKOUT * 2, above=True)
        dn = _edge(xs, lp, lp[0], body_end, above=False)
        if not up or not dn:
            continue
        su, bu, tu = up
        sl, bl, tl = dn
        upper = lambda i, s=su, b=bu: s * i + b
        lower = lambda i, s=sl, b=bl: s * i + b
        w0, w1 = upper(lp[0]) - lower(lp[0]), upper(last) - lower(last)
        if not (su < 0 and sl < 0 and su < sl and w0 > 0 and 0 < w1 < 0.75 * w0):
            continue
        if tu < 2 or tl < 2 or tu + tl < 5:
            continue
        mid = (start + last) // 2
        cand = {"pattern": "falling wedge", "touches": tu + tl, "trigger": upper(last),
                "support": lower(last), "lookback": L, "age": _breakout_age(xs, upper),
                "vol_contract": _mean(vols[mid:]) < _mean(vols[start:mid])}
        if best is None or (cand["touches"], L) > (best["touches"], best["lookback"]):
            best = cand
    return best


def double_bottom(xs: list[float]) -> dict | None:
    last = len(xs) - 1
    start = max(0, last - 90)
    _, lo = pivots(xs[start:])
    lo = [start + i for i in lo]
    for j in range(len(lo) - 1, 0, -1):          # most recent pair first
        b, a = lo[j], lo[j - 1]
        if b - a < 10 or abs(xs[b] / xs[a] - 1) > 0.03:
            continue
        neck = max(xs[a:b + 1])
        if neck < 1.05 * max(xs[a], xs[b]):
            continue
        if min(xs[b:]) < min(xs[a], xs[b]) * 0.98:   # undercut since = pattern failed
            continue
        return {"pattern": "double bottom", "trigger": neck, "support": min(xs[a], xs[b]),
                "age": _breakout_age(xs, lambda i, n=neck: n)}
    return None


def bull_flag(xs: list[float]) -> dict | None:
    last = len(xs) - 1
    for top in range(last - 5, max(last - 26, 20), -1):     # flag 5..25 sessions old
        base = min(xs[top - 20:top])
        if xs[top] < 1.10 * base or xs[top] != max(xs[top - 20:last + 1]):
            continue
        give_back = (xs[top] - min(xs[top:])) / (xs[top] - base)
        if give_back > 0.5:
            return None
        return {"pattern": "bull flag", "trigger": xs[top], "support": min(xs[top:]),
                "age": _breakout_age(xs, lambda i, t=xs[top]: t)}
    return None


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


# ---------------------------------------------------------------- score
PATTERN_POINTS = {"fresh_breakout": 45, "breakout": 30, "near": 25, "forming": 15}


def score(rows_desc: list[dict]) -> dict | None:
    """0-100 bullish-setup score for one name; None with < 130 sessions of data."""
    xs, vols = _chrono(rows_desc)
    if len(xs) < 130:
        return None
    last = len(xs) - 1
    price = xs[last]
    pts, why = 0, []

    found = [p for p in (falling_wedge(xs, vols), double_bottom(xs), bull_flag(xs)) if p]
    best = None
    for p in found:
        age = p["age"]
        if age is not None:
            state = "fresh_breakout" if age < FRESH_BREAKOUT else "breakout"
        elif price > p["trigger"]:
            state = "breakout"            # broke out > 10 sessions ago and held
        elif price >= p["trigger"] * (1 - NEAR_TRIGGER):
            state = "near"
        else:
            state = "forming"
        p["state"] = state
        p["points"] = PATTERN_POINTS[state]
        if age is not None and _vol_confirmed(vols, age):
            p["points"] += 5
            p["vol_breakout"] = True
        if p.get("vol_contract"):
            p["points"] += 5
        if best is None or p["points"] > best["points"]:
            best = p
    if best:
        pts += best["points"]
        label = {"fresh_breakout": "BROKE OUT", "breakout": "broke out",
                 "near": "near trigger", "forming": "forming"}[best["state"]]
        why.append(f"{best['pattern']} {label}"
                   + (" on volume" if best.get("vol_breakout") else ""))

    hi, lo = pivots(xs)
    rsi = _rsi_series(xs)
    if len(lo) >= 2:
        a, b = lo[-2], lo[-1]
        if xs[b] > xs[a]:
            pts += 10
            why.append("higher low")
        elif rsi[a] is not None and rsi[b] is not None and rsi[b] > rsi[a] + 2:
            pts += 10
            why.append("RSI bullish divergence")
    macd = [f - s for f, s in zip(_ema(xs, 12), _ema(xs, 26))]
    sig = _ema(macd, 9)
    if any(macd[i] > sig[i] and macd[i - 1] <= sig[i - 1] for i in range(last - 4, last + 1)):
        pts += 10
        why.append("MACD crossed up")
    elif macd[last] > sig[last]:
        pts += 5
        why.append("MACD above signal")
    e20 = _ema(xs, 20)
    if price > e20[last] and e20[last] > e20[last - 5]:
        pts += 10
        why.append("above a rising 20-day")
    up = sum(v for i, v in enumerate(vols[-20:], len(xs) - 20) if xs[i] > xs[i - 1])
    dn = sum(v for i, v in enumerate(vols[-20:], len(xs) - 20) if xs[i] < xs[i - 1])
    if up > dn:
        pts += 5
        why.append("up-volume > down-volume")
    s50, s50_prev = _sma(xs, 50), _sma(xs, 50, last - 9)
    if price > s50 and any(xs[i] <= _sma(xs, 50, i + 1) for i in range(last - 10, last)):
        pts += 10
        why.append("reclaimed the 50-day")
    if min(xs[-3:]) <= min(xs[-60:]):
        pts -= 15
        why.append("PENALTY: fresh 60-day low")
    if price < s50 and s50 < s50_prev:
        pts -= 10
        why.append("PENALTY: below a falling 50-day")

    pts = max(0, min(100, pts))
    out = {"score": pts, "label": label_for(pts), "why": why, "price": round(price, 2)}
    if best:
        out["pattern"] = {"name": best["pattern"], "state": best["state"],
                          "trigger": round(best["trigger"], 2),
                          "support": round(best["support"], 2)}
    return out


def label_for(pts: int) -> str:
    return next(lbl for cut, lbl in BANDS if pts >= cut)


# ---------------------------------------------------------------- cache + display
def build(histories: dict[str, list[dict]], asof: str) -> dict:
    rows = {}
    for sym, h in histories.items():
        s = score(h)
        if s:
            rows[sym] = s
    return {"asof_utc": asof, "rows": rows}


def save_cache(blob: dict) -> None:
    CACHE.write_text(json.dumps(blob, indent=1) + "\n", encoding="utf-8")


def load_cache() -> dict[str, dict]:
    try:
        return json.loads(CACHE.read_text(encoding="utf-8")).get("rows", {})
    except (OSError, ValueError, AttributeError):
        return {}


def live_state(s: dict | None, price: float | None) -> str | None:
    """Re-read the cached pattern against a live price: a name that crossed its
    trigger since the morning close shows as breaking out now."""
    p = (s or {}).get("pattern")
    if not p or price is None:
        return None
    if p["state"] in ("near", "forming") and price > p["trigger"]:
        return "BREAKING OUT NOW"
    if price < p["support"]:
        return "BROKE SUPPORT"
    return None


def cell(s: dict | None, price: float | None = None) -> str:
    if not s:
        return "—"
    return f"{s['score']} {s['label']}"


def pattern_cell(s: dict | None, price: float | None = None) -> str:
    p = (s or {}).get("pattern")
    if not p:
        return "no pattern"
    live = live_state(s, price)
    state = {"fresh_breakout": "broke out", "breakout": "broke out (older)",
             "near": "near trigger", "forming": "forming"}[p["state"]]
    txt = f"{p['name']}, {state}"
    if price is not None and p["state"] in ("near", "forming"):
        txt += f" ({p['trigger'] / price - 1:+.1%} to {p['trigger']})"
    return txt + (f" **{live}**" if live else "")


LEGEND = ("_Setup = how bullish the daily chart is, 0-100: STRONG >= 60, CONSTRUCTIVE 35-59, "
          "NEUTRAL 15-34, WEAK < 15. Patterns: falling wedge (converging falling trendlines), "
          "double bottom, bull flag; a close above the trigger (breakout) scores more than a "
          "pattern still forming, more again on volume. Plus higher low / RSI divergence, MACD "
          "cross, a rising 20-day, up-volume, a 50-day reclaim; minus a fresh 60-day low or a "
          "falling 50-day. Built from the morning's closes; the trigger is re-checked against "
          "the live price. No backtest: a ranking aid, not a buy signal._")
