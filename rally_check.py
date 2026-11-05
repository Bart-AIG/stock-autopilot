"""Rally quality check for SPY and QQQ: is a rally to new highs FRAGILE?

Ryan, live turn 2026-11-05: "understanding when we have a large increase in qqq and spy
if it is on low liquidity and volume because if it is then we know the gains are very
fragile". Tested in rally_backtest.py / rally_results.md (2007-2026, FMP daily bars):

- A single big up day on light volume is NOT a warning (it did no worse than a normal one).
- Light volume during a multi-week rally is a weak warning on its own.
- Light volume PLUS narrow leadership (the cap-weighted ETF beating its equal-weight twin,
  i.e. a few mega caps carrying the index) is the fragile combination. For QQQ, 5%+
  20-day rallies into a 52-week high that were both: 57% fell 7%+ within 60 sessions
  (n=7) vs ~19% for broad rallies. The rule fired on QQQ from 2026-09-21 through the
  2026-10-06 peak.

Pure functions, no network. Bars are oldest-first dicts with 'date', 'close', 'volume'.
A FLAG, not a trade signal: the sample is small (n=5-9 per cell).
"""
from __future__ import annotations

import statistics

PAIRS = {"SPY": "RSP", "QQQ": "QQQE"}   # cap-weighted ETF -> its equal-weight twin

RALLY_GAIN = 0.03        # 20-session gain that counts as a rally
NEAR_HIGH = 0.98         # close within 2% of the 252-session high
LOW_VOLUME = 0.85        # 20-session avg volume / prior 100-session avg below this
NARROW_GAP = 0.02        # beat the equal-weight twin by >= 2 points over 20 sessions
WINDOW, BASE, YEAR = 20, 100, 252


def check(bars: list[dict], ew_bars: list[dict]) -> dict:
    """State of one index: FRAGILE (rally + light volume + narrow), THIN (rally + light
    volume), NARROW (rally + narrow), HEALTHY (rally, neither), NO RALLY, or NO DATA."""
    need = YEAR
    if len(bars) < need or len(ew_bars) < WINDOW + 1:
        return {"state": "NO DATA", "why": f"need {need} daily bars, have {len(bars)}"}
    c = [float(b["close"]) for b in bars]
    v = [float(b["volume"]) for b in bars]
    ew = {b["date"]: float(b["close"]) for b in ew_bars}
    d_now, d_then = bars[-1]["date"], bars[-1 - WINDOW]["date"]
    gain = c[-1] / c[-1 - WINDOW] - 1
    high = max(c[-YEAR:])
    vol_ratio = statistics.mean(v[-WINDOW:]) / statistics.mean(v[-WINDOW - BASE:-WINDOW])
    ew_gain = (ew[d_now] / ew[d_then] - 1) if d_now in ew and d_then in ew else None
    gap = gain - ew_gain if ew_gain is not None else None
    rally = gain >= RALLY_GAIN and c[-1] >= NEAR_HIGH * high
    thin = vol_ratio < LOW_VOLUME
    narrow = gap is not None and gap >= NARROW_GAP
    if not rally:
        state = "NO RALLY"
    elif thin and narrow:
        state = "FRAGILE"
    elif thin:
        state = "THIN"
    elif narrow:
        state = "NARROW"
    else:
        state = "HEALTHY"
    return {
        "state": state,
        "date": d_now,
        "close": round(c[-1], 2),
        "gain_20d_pct": round(100 * gain, 2),
        "off_high_pct": round(100 * (c[-1] / high - 1), 2),
        "volume_ratio": round(vol_ratio, 2),
        "vs_equal_weight_pts": None if gap is None else round(100 * gap, 2),
    }


def summary(results: dict[str, dict], prior: dict | None = None) -> dict:
    """Combine per-index checks into one flag. FRAGILE if either index is FRAGILE.
    Keeps the date the current state began, from the prior file."""
    states = {s: r.get("state") for s, r in results.items()}
    flag = "FRAGILE" if "FRAGILE" in states.values() else (
        "WATCH" if {"THIN", "NARROW"} & set(states.values()) else "OK")
    prior = prior or {}
    as_of = max((r.get("date") or "" for r in results.values()), default="")
    since = prior.get("since") if prior.get("flag") == flag else as_of
    note = {
        "FRAGILE": "Rally to highs on light volume, carried by a few mega caps. Historically "
                   "the most likely to give back 7%+ within ~3 months. Do not add margin or "
                   "leveraged ETFs into it; trim leverage into strength.",
        "WATCH": "Rally is either light on volume or narrow, not both. Weak warning on its own.",
        "OK": "No fragile rally.",
    }[flag]
    return {"flag": flag, "since": since, "as_of": as_of, "note": note, "indexes": results}
