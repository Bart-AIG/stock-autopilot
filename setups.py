"""Chart-setup scores (set 2026-10-14). PRE-BREAKOUT (prebreakout(), the ranking in use)
and the original bullish-chart score (score, kept as a description; it backtested
INVERSELY).

Ryan, live turn 2026-10-14, after a TrendSpider "falling wedges everywhere" post: *"rank
the names selected in the quality stock watch routine by most bullish chart setups"*.

score() reads one name's daily closes + volume and returns a 0-100 setup score, a
label, the best pattern found, its trigger price and the confirmations behind it.
Pure functions, no network. report.py builds setups.json each morning for the Quality
@ 200-day list (build()), and quality_watch.py ranks and prints from that cache.

What it looks for (daily open/high/low/close/volume; trendlines run through the
swing HIGHS and LOWS like a hand-drawn chart, breakouts are judged on the CLOSE):
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

BACKTEST (setups_backtest.py -> setups_results.md, run 2026-10-14): on S&P 100 +
Nasdaq-100 names within -8%/+5% of their 200-day, 2019-2026, the score was NEGATIVELY
related to the next 63 sessions' excess return (non-overlapping rank IC -0.111, t -3.1;
top-3 names lagged the average by 3.5%), in both 2019-22 and 2023-26. Breakouts, a rising
20-day and up-volume lagged; fresh 60-day lows, RSI divergence and still-forming
patterns led: short-term mean reversion, the same effect the RSI(2) sleeves trade. So
the score DESCRIBES a chart; it does not rank expected return. It ranks a watch list for Ryan's eyes; it is NOT a gate or filter on the
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


def _chrono(rows_desc: list[dict]):
    """FMP rows (newest first) -> oldest-first closes, highs, lows, volumes. The light
    history has only 'price'; then highs and lows fall back to the close."""
    C, H, L, V = [], [], [], []
    for r in reversed(rows_desc or []):
        p = r.get("close", r.get("price"))
        if p is None:
            continue
        p = float(p)
        C.append(p)
        H.append(float(r.get("high") or p))
        L.append(float(r.get("low") or p))
        V.append(float(r.get("volume") or 0))
    return C, H, L, V


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
    """Any of the breakout sessions traded above 1.2x its 20-day average volume."""
    last = len(vols) - 1
    for i in range(last - age, last + 1):
        avg = _sma(vols, 20, i)
        if avg and vols[i] > 1.2 * avg:
            return True
    return False


# ---------------------------------------------------------------- patterns
TOUCH_TOL = 0.015           # a swing point within 1.5% of a line "touches" it
CLOSE_TOL = 0.005           # a close may poke 0.5% through a line (intraday wicks: 2%)
WICK_TOL = 0.02


def _edge(P: list[float], C: list[float], idx: list[int], lo: int, hi: int, above: bool):
    """Best trendline through two of the swing points idx of series P (highs for
    resistance, lows for support) that no close in [lo, hi] crosses by more than 0.5%
    and no high/low (P itself) by more than 2%. Best = most touches, then the longest
    span. Returns (slope, intercept, touches) or None."""
    best = None
    rng = range(lo, hi + 1)
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            i, j = idx[a], idx[b]
            if j - i < 5:
                continue
            m = (P[j] - P[i]) / (j - i)
            c = P[i] - m * i
            if above:
                if any(C[k] > (m * k + c) * (1 + CLOSE_TOL) or P[k] > (m * k + c) * (1 + WICK_TOL)
                       for k in rng):
                    continue
            elif any(C[k] < (m * k + c) * (1 - CLOSE_TOL) or P[k] < (m * k + c) * (1 - WICK_TOL)
                     for k in rng):
                continue
            t = sum(1 for k in idx if abs(P[k] / (m * k + c) - 1) <= TOUCH_TOL)
            key = (t, j - i)
            if best is None or key > best[0]:
                best = (key, m, c, t)
    return None if best is None else best[1:]


def falling_wedge(C, H, L, V, piv=None) -> dict | None:
    """Resistance drawn down from the lookback's highest high through later swing
    highs, support under the swing lows since; both falling and converging (the upper
    line falls faster). Trigger = the resistance line today; breakout = a close above."""
    best = None
    last = len(C) - 1
    hi_all, lo_all = piv or (pivots(H)[0], pivots(L)[1])
    for LB in WEDGE_LOOKBACKS:
        if len(C) < LB + PIVOT_K + 1:
            continue
        start = max(range(last - LB, last + 1), key=lambda i: H[i])     # anchor high
        if last - start < 20:
            continue
        body_end = last - 1      # the latest close may already be breaking out
        hp = [i for i in hi_all if start <= i <= body_end]
        if start not in hp:
            hp = [start] + hp
        lp = [i for i in lo_all if start < i <= body_end]
        if len(hp) < 2 or len(lp) < 2:
            continue
        up = _edge(H, C, hp, start, last - FRESH_BREAKOUT * 2, above=True)
        if not up or up[0] >= 0:
            continue
        dn = _edge(L, C, lp, lp[0], body_end, above=False)
        if not dn:
            continue
        su, bu, tu = up
        sl, bl, tl = dn
        upper = lambda i, s=su, b=bu: s * i + b
        lower = lambda i, s=sl, b=bl: s * i + b
        w0, w1 = upper(lp[0]) - lower(lp[0]), upper(last) - lower(last)
        if not (sl < 0 and su < sl and w0 > 0 and 0 < w1 < 0.75 * w0):
            continue
        if tu < 2 or tl < 2 or tu + tl < 5:
            continue
        mid = (start + last) // 2
        cand = {"pattern": "falling wedge", "touches": tu + tl, "trigger": upper(last),
                "support": lower(last), "lookback": LB, "age": _breakout_age(C, upper),
                "vol_contract": _mean(V[mid:]) < _mean(V[start:mid])}
        if best is None or (cand["touches"], LB) > (best["touches"], best["lookback"]):
            best = cand
    return best


def double_bottom(C, H, L, piv=None) -> dict | None:
    """Two swing lows within 3%, >= 10 sessions apart, a >= 5% bounce between them, not
    undercut since. Trigger = the highest high between the lows (neckline)."""
    last = len(C) - 1
    start = max(0, last - 90)
    lo = [i for i in (piv[1] if piv else pivots(L)[1]) if i >= start]
    for j in range(len(lo) - 1, 0, -1):          # most recent pair first
        b, a = lo[j], lo[j - 1]
        if b - a < 10 or abs(L[b] / L[a] - 1) > 0.03:
            continue
        neck = max(H[a:b + 1])
        if neck < 1.05 * max(L[a], L[b]):
            continue
        floor = min(L[a], L[b])
        if min(L[b:]) < floor * 0.98:            # undercut since = pattern failed
            continue
        return {"pattern": "double bottom", "trigger": neck, "support": floor,
                "age": _breakout_age(C, lambda i, n=neck: n)}
    return None


def bull_flag(C, H, L) -> dict | None:
    """A >= 10% run in <= 20 sessions to a high 5-25 sessions ago, then a pullback that
    gives back <= half of it. Trigger = the run's high."""
    last = len(C) - 1
    for top in range(last - 5, max(last - 26, 20), -1):
        base = min(L[top - 20:top])
        if H[top] < 1.10 * base or H[top] != max(H[top - 20:last + 1]):
            continue
        give_back = (H[top] - min(L[top:])) / (H[top] - base)
        if give_back > 0.5:
            return None
        return {"pattern": "bull flag", "trigger": H[top], "support": min(L[top:]),
                "age": _breakout_age(C, lambda i, t=H[top]: t)}
    return None


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


# ---------------------------------------------------------------- score
PATTERN_POINTS = {"fresh_breakout": 45, "breakout": 30, "near": 25, "forming": 15}
STATE_WORDS = {"fresh_breakout": "BROKE OUT", "breakout": "broke out",
               "near": "near trigger", "forming": "forming"}
MIN_BARS = 130


def score(rows_desc: list[dict]) -> dict | None:
    """0-100 bullish-setup score for one name; None with < 130 sessions of data."""
    return score_arrays(*_chrono(rows_desc))


def score_arrays(C, H, L, V) -> dict | None:
    """score() on oldest-first arrays (the backtest calls this directly). 'flags' lists
    the machine keys of every component that fired, for setups_backtest.py."""
    if len(C) < MIN_BARS:
        return None
    last = len(C) - 1
    price = C[last]
    pts, why, flags = 0, [], []
    hp, lp = pivots(H)[0], pivots(L)[1]

    found = [p for p in (falling_wedge(C, H, L, V, (hp, lp)), double_bottom(C, H, L, (hp, lp)),
                         bull_flag(C, H, L)) if p]
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
        if age is not None and _vol_confirmed(V, age):
            p["points"] += 5
            p["vol_breakout"] = True
        if p.get("vol_contract"):
            p["points"] += 5
        if best is None or p["points"] > best["points"]:
            best = p
    if best:
        pts += best["points"]
        why.append(f"{best['pattern']} {STATE_WORDS[best['state']]}"
                   + (" on volume" if best.get("vol_breakout") else ""))
        flags.append(f"{best['pattern'].replace(' ', '_')}:{best['state']}")

    rsi = _rsi_series(C)
    if len(lp) >= 2:
        a, b = lp[-2], lp[-1]
        if L[b] > L[a]:
            pts += 10
            why.append("higher low")
            flags.append("higher_low")
        elif rsi[a] is not None and rsi[b] is not None and rsi[b] > rsi[a] + 2:
            pts += 10
            why.append("RSI bullish divergence")
            flags.append("rsi_divergence")
    macd = [f - s for f, s in zip(_ema(C, 12), _ema(C, 26))]
    sig = _ema(macd, 9)
    if any(macd[i] > sig[i] and macd[i - 1] <= sig[i - 1] for i in range(last - 4, last + 1)):
        pts += 10
        why.append("MACD crossed up")
        flags.append("macd_cross")
    elif macd[last] > sig[last]:
        pts += 5
        why.append("MACD above signal")
        flags.append("macd_above")
    e20 = _ema(C, 20)
    if price > e20[last] and e20[last] > e20[last - 5]:
        pts += 10
        why.append("above a rising 20-day")
        flags.append("rising_20d")
    up = sum(V[i] for i in range(last - 19, last + 1) if C[i] > C[i - 1])
    dn = sum(V[i] for i in range(last - 19, last + 1) if C[i] < C[i - 1])
    if up > dn:
        pts += 5
        why.append("up-volume > down-volume")
        flags.append("up_volume")
    s50, s50_prev = _sma(C, 50), _sma(C, 50, last - 9)
    if price > s50 and any(C[i] <= _sma(C, 50, i + 1) for i in range(last - 10, last)):
        pts += 10
        why.append("reclaimed the 50-day")
        flags.append("reclaim_50d")
    if min(C[-3:]) <= min(C[-60:]):
        pts -= 15
        why.append("PENALTY: fresh 60-day low")
        flags.append("pen_60d_low")
    if price < s50 and s50 < s50_prev:
        pts -= 10
        why.append("PENALTY: below a falling 50-day")
        flags.append("pen_falling_50d")

    pts = max(0, min(100, pts))
    states = {p["state"] for p in found}
    forming = [p for p in found if p["state"] in ("near", "forming")]
    feat = {
        "pattern_forming": bool(forming),
        "pattern_broke_out": bool(states & {"fresh_breakout", "breakout"}),
        "rsi_divergence": "rsi_divergence" in flags,
        "fresh_60d_low": "pen_60d_low" in flags,
        "rsi14_below_40": rsi[last] is not None and rsi[last] < 40,
        "below_20d": price < e20[last],
        "pullback_8pct": price / max(C[-60:]) - 1 <= -0.08,
        "volume_drying": _mean(V[-10:]) < 0.85 * _mean(V[-50:]),
        "higher_low": "higher_low" in flags,
        "macd_cross": "macd_cross" in flags,
        "macd_above": "macd_above" in flags,
        "rising_20d": "rising_20d" in flags,
        "up_volume": "up_volume" in flags,
        "reclaim_50d": "reclaim_50d" in flags,
        "below_falling_50d": "pen_falling_50d" in flags,
    }
    pre = prebreakout(feat)
    out = {"score": pts, "label": label_for(pts), "why": why, "flags": flags,
           "feat": feat, "pre": pre, "pre_label": pre_label(pre),
           "price": round(price, 2)}
    if best:
        out["pattern"] = {"name": best["pattern"], "state": best["state"],
                          "trigger": round(best["trigger"], 2),
                          "support": round(best["support"], 2)}
    return out


# PRE-BREAKOUT score (Ryan, live turn 2026-10-14: "thats what we should be looking for,
# ones before the breakout"). The 2026-10-14 backtest showed the bullish-LOOKING chart
# (breakouts, rising 20-day, up-volume) lagged and the pulled-back chart led. These are
# the "before the breakout" traits, written down BEFORE the out-of-sample check
# (setups_backtest.py fits nothing on 2023-26; see setups_results.md). Each is worth
# one point; a broken-out pattern costs one (the move it promised has happened).
PRE_WEIGHTS = {
    "pattern_forming": 1, "rsi_divergence": 1, "fresh_60d_low": 1, "rsi14_below_40": 1,
    "below_20d": 1, "pullback_8pct": 1, "volume_drying": 1, "pattern_broke_out": -1,
}
PRE_MAX = sum(w for w in PRE_WEIGHTS.values() if w > 0)


def prebreakout(feat: dict, weights: dict | None = None) -> int:
    """0-100: how far the chart sits in the 'pulled back, not yet broken out' state."""
    w = weights or PRE_WEIGHTS
    pos = sum(v for v in w.values() if v > 0) or 1
    raw = sum(v for k, v in w.items() if feat.get(k))
    return max(0, round(100 * raw / pos))


def pre_label(pre: int) -> str:
    return "COILED" if pre >= 60 else "PULLING BACK" if pre >= 35 else "MIXED" if pre >= 15 else "EXTENDED"


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


PRE_WORDS = {"pattern_forming": "pattern forming", "rsi_divergence": "RSI divergence",
             "fresh_60d_low": "fresh 60-day low", "rsi14_below_40": "RSI(14) < 40",
             "below_20d": "below 20-day", "pullback_8pct": ">= 8% off 60-day high",
             "volume_drying": "volume drying up", "pattern_broke_out": "already broke out (-1)"}


def pre_cell(s: dict | None) -> str:
    if not s or s.get("pre") is None:
        return "—"
    return f"{s['pre']} {s.get('pre_label') or pre_label(s['pre'])}"


def pre_why(s: dict | None) -> str:
    feat = (s or {}).get("feat") or {}
    words = [PRE_WORDS[k] for k in PRE_WEIGHTS if feat.get(k)]
    return ", ".join(words) or "—"


LEGEND = ("_Pre-breakout = how far the chart sits in the 'pulled back, not yet broken out' state, "
          "0-100: COILED >= 60, PULLING BACK 35-59, MIXED 15-34, EXTENDED < 15. One point each for "
          "a pattern forming (falling wedge, double bottom, bull flag below its trigger), RSI "
          "divergence, a fresh 60-day low, RSI(14) < 40, below the 20-day, >= 8% off the 60-day high, "
          "volume drying up; minus one for a pattern that already broke out. Backtested 2026-10-14 "
          "(setups_results.md): rank IC +0.093 (t 2.6) over 2019-2026, +0.097 (t 2.0) on 2023-26 data "
          "it was not built from; the most-coiled fifth beat the least by ~2.8% vs SPY over 3 months. "
          "The pattern itself adds little; most of the edge is the pullback (short-term mean "
          "reversion). Built from the morning's daily bars; the pattern trigger is re-checked "
          "against the live price._")
