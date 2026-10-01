"""
The sleeve process (routine prompt v16, Ryan's live turn 2026-09-30: "Lets move forward with
implementing the new strategy on our Stock autopilot routine").

Tested in docs/process-audit-2026-09-29.md (sections 11, 12, 14, 16). Two live sleeves, both
running the same rules, SWING_UNION:
  SWING_Q  QQQ's signals, held as QLD (2x QQQ).                 70% of the investable base
  SWING_M  each of the month's top-10 names by 12-month return, 1x.  30% (3% per name)
  GROWTH   Claude-researched high-growth names: PAPER ONLY until Ryan makes it live, then
           10% taken from SWING_Q (-> 60%). Tracked in growth_paper.json, not here.
Investable base = 95% of total account value (the 5% operational reserve stays).

SWING_UNION (per symbol, decided near the close, held close to close; "in" if ANY leg is on):
  RSI2 leg  enter: RSI(2) < 10 and price > 200-day SMA.  exit: price > 5-day SMA.
  IBS leg   enter: (price - low) / (high - low) < 0.2 and price > 200-day SMA.
            exit: IBS > 0.8, or 5 sessions held.
  TOM leg   in over the last trading day of a month and the first three of the next.
No stops, no targets: the tested rules have none.

Two commands:
  python sleeves.py build            (GitHub Actions, FMP key) -> sleeves_state.json:
                                     the month's picks and each symbol's leg state as of
                                     the last completed session.
  python sleeves.py decide LIVE.json [--tv TOTAL_VALUE]
                                     (the routine, no network) LIVE.json =
                                     {"asof_utc": "...", "SYM": {"px":.., "hi":.., "lo":..}, ...}
                                     with today's live price and session high/low so far.
                                     Prints the target book as JSON.
The replay in build() and the one-step decision in step() are the same function the
backtests used (robust_backtest.swing), checked by test_sleeves.py.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from analyze import SPECULATIVE, UNIVERSE, compute_rsi

HERE = Path(__file__).resolve().parent
STATE = HERE / "sleeves_state.json"

INVEST_FRAC = 0.95                      # 5% operational reserve
W_SWING_Q = 0.70                        # 0.60 once GROWTH is live
W_SWING_M = 0.30
N_PICKS = 10
Q_SIGNAL, Q_VEHICLE = "QQQ", "QLD"
RSI_IN, IBS_IN, IBS_OUT, IBS_MAX = 10, 0.2, 0.8, 5
ETFS = {"SPY", "QQQ", "IWM", "DIA"}

# NYSE full-day holidays (early closes are ordinary sessions for these rules).
HOLIDAYS = {
    "2025-01-01", "2025-01-09", "2025-01-20", "2025-02-17", "2025-04-18", "2025-05-26",
    "2025-06-19", "2025-07-04", "2025-09-01", "2025-11-27", "2025-12-25",
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19",
    "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
    "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-18",
    "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24",
}


# ----------------------------------------------------------------------------- calendar

def is_session(d: date) -> bool:
    return d.weekday() < 5 and d.isoformat() not in HOLIDAYS


def sessions_in_month(y: int, m: int) -> list[str]:
    d, out = date(y, m, 1), []
    while d.month == m:
        if is_session(d):
            out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def next_session(d: date) -> date:
    d += timedelta(days=1)
    while not is_session(d):
        d += timedelta(days=1)
    return d


def is_tom(day: str) -> bool:
    """Last trading day of its month or one of the first three."""
    d = date.fromisoformat(day)
    s = sessions_in_month(d.year, d.month)
    return day in s[:3] or day == s[-1]


def pool() -> list[str]:
    try:
        from backtest import NDX100_2018, SP100_2018
        extra = set(SP100_2018) | set(NDX100_2018)
    except Exception:  # noqa: BLE001
        extra = set()
    return sorted((set(UNIVERSE) - SPECULATIVE - ETFS) | extra)


# ----------------------------------------------------------------------------- rules

def fresh_legs() -> dict:
    return {"RSI2": False, "IBS": False, "TOM": False, "ibs_age": 0}


def step(legs: dict, prior: list[float], px: float, hi: float, lo: float, next_day_tom: bool) -> tuple[dict, dict]:
    """One decision. prior = closes of completed sessions (oldest first, >= 199), px = the
    price the decision is taken at, hi/lo = today's range up to now. Returns (new legs,
    detail). Mirrors robust_backtest.swing exactly."""
    sma200 = (sum(prior[-199:]) + px) / 200
    up = px > sma200
    r2 = compute_rsi(prior[-59:] + [px], 2)
    sma5 = (sum(prior[-4:]) + px) / 5
    rng = hi - lo
    ibs = (px - lo) / rng if rng > 0 else 0.5
    new = dict(legs)
    if legs["RSI2"]:
        new["RSI2"] = not (px > sma5)
    else:
        new["RSI2"] = r2 is not None and r2 < RSI_IN and up
    if legs["IBS"]:
        age = legs["ibs_age"] + 1
        new["IBS"] = not (ibs > IBS_OUT or age >= IBS_MAX)
        new["ibs_age"] = age
    else:
        new["IBS"] = ibs < IBS_IN and up
        new["ibs_age"] = 0
    new["TOM"] = bool(next_day_tom)
    detail = {"px": round(px, 4), "sma200": round(sma200, 4), "above_200": up, "rsi2": r2,
              "sma5": round(sma5, 4), "ibs": round(ibs, 3), "next_session_tom": bool(next_day_tom)}
    return new, detail


def is_in(legs: dict) -> bool:
    return bool(legs["RSI2"] or legs["IBS"] or legs["TOM"])


def replay(dates: list[str], C: list[float], H: list[float], L: list[float]) -> dict:
    """Leg state after the last completed session in the arrays (what is held going into
    the next session). TOM from the exchange calendar."""
    legs = fresh_legs()
    for i in range(201, len(dates)):
        nxt = dates[i + 1] if i + 1 < len(dates) else next_session(date.fromisoformat(dates[i])).isoformat()
        legs, _ = step(legs, C[:i], C[i], H[i], L[i], is_tom(nxt))
    return legs


# ----------------------------------------------------------------------------- build (Actions)

def _fmp(url: str):
    import urllib.error
    import urllib.request
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3 + 3 * attempt)
                continue
            return None
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return None


def fetch_ohlc(sym: str, key: str, days: int = 460):
    base = "https://financialmodelingprep.com/stable"
    frm = (date.today() - timedelta(days=days)).isoformat()
    data = _fmp(f"{base}/historical-price-eod/full?symbol={sym}&from={frm}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return None
    rows = sorted((r for r in data if r.get("close") and r.get("high") and r.get("low")), key=lambda r: r["date"])
    return ([r["date"][:10] for r in rows], [float(r["close"]) for r in rows],
            [float(r["high"]) for r in rows], [float(r["low"]) for r in rows])


def completed_only(o, now_utc: datetime):
    """Drop a bar for a session that has not closed yet (FMP can serve today's partial bar)."""
    dates, C, H, L = o
    et_now = now_utc - timedelta(hours=4)          # EDT; a 1h error at DST edges only affects 15:00-16:00 ET
    today = et_now.date().isoformat()
    if dates and dates[-1] == today and (et_now.hour, et_now.minute) < (16, 5):
        return dates[:-1], C[:-1], H[:-1], L[:-1]
    return o


def build(key: str) -> dict:
    now = datetime.now(timezone.utc)
    names = pool()
    q = completed_only(fetch_ohlc(Q_SIGNAL, key), now)
    if not q or len(q[0]) < 260:
        raise SystemExit("QQQ history missing")
    qd = q[0]
    as_of = qd[-1]
    cur_month = next_session(date.fromisoformat(as_of)).isoformat()[:7]
    month_end = [d for d in qd if d[:7] < cur_month][-1]
    k = qd.index(month_end)
    base_day = qd[k - 252]

    def usable(o) -> bool:
        # A name ranks only with both anchor bars (month-end and the 12-month base); else a bad fetch.
        return bool(o) and len(o[0]) > 260 and month_end in o[0] and base_day in o[0]

    closes: dict[str, tuple] = {}
    missing = list(names)
    # 2026-10-01: a rebuild silently lost MRNA and MRVL (top-10 names) to bad fetches and swapped
    # the month's picks. Retry every name whose data is unusable before ranking anything.
    for attempt in range(3):
        retry = []
        for i, s in enumerate(missing):
            o = fetch_ohlc(s, key)
            o = completed_only(o, now) if o else None
            if usable(o):
                closes[s] = o
            else:
                retry.append(s)
            if i % 40 == 0:
                print(f"  pass {attempt + 1}: {i}/{len(missing)}", flush=True)
            time.sleep(0.12 if attempt == 0 else 1.0)
        missing = retry
        if not missing:
            break
    if missing:
        print(f"  no usable data after retries: {missing}", flush=True)
    ranked = []
    for s, (ds, C, _, _) in closes.items():
        ix = {d: j for j, d in enumerate(ds)}
        if C[ix[month_end]] >= 5:
            ranked.append((C[ix[month_end]] / C[ix[base_day]] - 1, s))
    ranked.sort(reverse=True)
    picks = [s for _, s in ranked[:N_PICKS]]
    # The month's picks are fixed once (tested design). A later build in the same month keeps the
    # picks already published; if one of them has no usable data now, fail rather than swap it.
    try:
        prev = json.loads(STATE.read_text())
    except Exception:  # noqa: BLE001
        prev = {}
    if prev.get("month_end_ranked") == month_end and prev.get("picks"):
        locked = [p["symbol"] for p in prev["picks"]]
        lost = [s for s in locked if s not in closes]
        if lost:
            raise SystemExit(f"locked picks {lost} have no usable data; keeping the published state")
        if locked != picks:
            print(f"  picks locked for {cur_month}: {locked} (fresh ranking was {picks})", flush=True)
        rmap = {s: r for r, s in ranked}
        ranked = [(rmap[s], s) for s in locked] + [(r, s) for r, s in ranked if s not in locked]
        picks = locked
    today = next_session(date.fromisoformat(as_of)).isoformat()
    syms = {}
    for s in [Q_SIGNAL] + picks:
        ds, C, H, L = q if s == Q_SIGNAL else closes[s]
        if ds[-1] != as_of:
            syms[s] = {"error": f"last bar {ds[-1]} != {as_of}"}
            continue
        legs = replay(ds, C, H, L)
        syms[s] = {"last_date": ds[-1], "last_close": C[-1], "prior_closes": [round(x, 4) for x in C[-200:]],
                   "legs": legs, "in_after_last_close": is_in(legs)}
    return {"built_utc": now.strftime("%Y-%m-%dT%H:%MZ"), "as_of_close": as_of, "decision_session": today,
            "month_end_ranked": month_end, "base_day_12m": base_day,
            "picks": [{"symbol": s, "ret_12m": round(r, 4)} for r, s in ranked[:N_PICKS]],
            "runners_up": [{"symbol": s, "ret_12m": round(r, 4)} for r, s in ranked[N_PICKS:N_PICKS + 5]],
            "pool_size": len(closes), "weights": {"invest_frac": INVEST_FRAC, "SWING_Q": W_SWING_Q,
                                                  "SWING_M": W_SWING_M, "per_pick": W_SWING_M / N_PICKS},
            "vehicle": {Q_SIGNAL: Q_VEHICLE}, "symbols": syms}


# ----------------------------------------------------------------------------- decide (routine)

def decide(state: dict, live: dict, tv: float | None, today: str | None = None) -> dict:
    today = today or datetime.now(timezone.utc).date().isoformat()
    out = {"decision_session": today, "state_as_of": state["as_of_close"], "errors": [], "targets": []}
    if state.get("decision_session") != today:
        out["errors"].append(f"STALE STATE: built for {state.get('decision_session')}, today is {today}. "
                             "No sleeve entries this run; hold what is held.")
        return out
    nxt_tom = is_tom(next_session(date.fromisoformat(today)).isoformat())
    base = (tv or 0) * INVEST_FRAC
    for s, info in state["symbols"].items():
        if "error" in info:
            out["errors"].append(f"{s}: {info['error']}")
            continue
        lv = live.get(s)
        if not lv or not all(k in lv for k in ("px", "hi", "lo")):
            out["errors"].append(f"{s}: no live price/high/low")
            continue
        hi, lo = max(lv["hi"], lv["px"]), min(lv["lo"], lv["px"])
        legs, det = step(info["legs"], info["prior_closes"], lv["px"], hi, lo, nxt_tom)
        sleeve = "swing_q" if s == Q_SIGNAL else "swing_m"
        w = W_SWING_Q if sleeve == "swing_q" else W_SWING_M / N_PICKS
        on = is_in(legs)
        out["targets"].append({
            "sleeve": sleeve, "signal_symbol": s, "trade_symbol": state.get("vehicle", {}).get(s, s),
            "hold_through_close": on, "legs_on": [k for k in ("RSI2", "IBS", "TOM") if legs[k]],
            "was_in_after_last_close": info["in_after_last_close"],
            "target_usd": round(base * w, 2) if (tv and on) else 0.0, "weight": w, **det})
    return out


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "build":
        key = os.environ.get("FMP_API_KEY", "").strip()
        if not key:
            sys.exit("FMP_API_KEY not set")
        st = build(key)
        STATE.write_text(json.dumps(st, indent=1) + "\n")
        print(f"sleeves_state.json: as of {st['as_of_close']}, picks {[p['symbol'] for p in st['picks']]}")
        return
    if len(sys.argv) >= 3 and sys.argv[1] == "decide":
        live = json.loads(Path(sys.argv[2]).read_text())
        tv = float(sys.argv[sys.argv.index("--tv") + 1]) if "--tv" in sys.argv else None
        today = sys.argv[sys.argv.index("--today") + 1] if "--today" in sys.argv else None
        print(json.dumps(decide(json.loads(STATE.read_text()), live, tv, today), indent=1))
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
