"""
Quality grade: a 12-trait trend/strength score for every name in the universe.

Set 2026-09-25 (Ryan, live turn: "Design approved... Let's just update the live
process"). Motivation, measured from the broker's own record: the RSI(2) screen's
only quality gate was "above a rising 200-day MA", so it kept buying slow,
defensive names that were oversold because nobody wanted them (ROST, MDLZ, MMM,
GD, LLY, UNP, ABNB, PNC — 9 closes since 2026-08-26, 2 wins, -$219). The grade
now decides WHICH names may be bought; the RSI(2) / 21-EMA pullback decides WHEN.

Every trait is computable from the FMP 'light' feed (daily close + volume only —
no high/low), so there is no ATR/NR7/close-in-range trait. Pure functions, no
network: report.py feeds it the history cache.
"""

from __future__ import annotations

import statistics

# --- Policy constants (the numbers Ryan approved; change only via a live turn) ---
ELIGIBLE_PCT = 0.10        # top 10% of the universe by grade may be BOUGHT
MIN_ELIGIBLE_SCORE = 9     # ...and must pass at least 9 of the 12 traits
HOLD_PCT = 0.25            # a held name that falls out of the top 25% is SOLD (grade exit)
EMA21_TOUCH_BAND = 0.01    # 21-EMA pullback trigger: close within +1% of the 21 EMA
N_TRAITS = 12

TRAITS = [
    # key,         short label,  what it tests
    ("ma_stack",   "MA STACK",   "21 EMA > 50 SMA > 200 SMA"),
    ("ema21_up",   "21 EMA UP",  "21-day EMA rising over the last 5 sessions"),
    ("above_50",   "> 50 SMA",   "close above the 50-day SMA"),
    ("ma200_up",   "200 UP",     "close above a RISING 200-day SMA"),
    ("near_high",  "52W HI",     "within 10% of the 252-day closing high"),
    ("weekly",     "W.EMA",      "weekly close > weekly EMA10 > weekly EMA30"),
    ("mom_12_1",   "12-1 MOM",   "12-1 month return > +10%"),
    ("rs_3m",      "RS 3M",      "3-month return beats SPY"),
    ("rs_6m",      "RS 6M",      "6-month return beats SPY"),
    ("ud_vol",     "U/D VOL",    "up-day volume > down-day volume over 50 sessions"),
    ("obv_up",     "OBV UP",     "on-balance volume higher than 50 sessions ago"),
    ("hh_hl",      "HH/HL",      "higher high AND higher low, last 40 vs prior 40 sessions"),
]


def _ema(values_chrono: list[float], span: int) -> list[float]:
    """EMA series, oldest-first in, oldest-first out."""
    if not values_chrono:
        return []
    k = 2 / (span + 1)
    out = [values_chrono[0]]
    for v in values_chrono[1:]:
        out.append(v * k + out[-1] * (1 - k))
    return out


def _ret(closes_desc: list[float], n: int) -> float | None:
    if len(closes_desc) <= n or not closes_desc[n]:
        return None
    return closes_desc[0] / closes_desc[n] - 1


def score_one(rows_desc: list[dict], spy_closes_desc: list[float] | None) -> dict | None:
    """Score one name. rows_desc = FMP rows newest-first ({'price','volume',...}).
    Returns None if there is not enough history (<260 sessions) to grade honestly."""
    closes = [r["price"] for r in rows_desc if r.get("price")]
    vols = [r.get("volume") or 0 for r in rows_desc if r.get("price")]
    if len(closes) < 260:
        return None
    chrono = list(reversed(closes))
    price = closes[0]

    ema21 = _ema(chrono, 21)
    sma50 = sum(closes[:50]) / 50
    sma200 = sum(closes[:200]) / 200
    sma200_prev = sum(closes[20:220]) / 200
    hi252 = max(closes[:252])

    # Weekly series: every 5th session, newest-anchored (approximates Friday closes).
    weekly = list(reversed(closes[::5]))
    w10, w30 = _ema(weekly, 10), _ema(weekly, 30)

    # 12-1 momentum: return from ~252 to ~21 sessions ago.
    mom = closes[21] / closes[252] - 1 if closes[252] else None
    r63, r126 = _ret(closes, 63), _ret(closes, 126)
    s63 = _ret(spy_closes_desc, 63) if spy_closes_desc else None
    s126 = _ret(spy_closes_desc, 126) if spy_closes_desc else None

    up_v = sum(vols[i] for i in range(50) if closes[i] > closes[i + 1])
    dn_v = sum(vols[i] for i in range(50) if closes[i] < closes[i + 1])
    # OBV change over the last 50 sessions = signed volume sum.
    obv_delta = up_v - dn_v

    t = {
        "ma_stack": ema21[-1] > sma50 > sma200,
        "ema21_up": ema21[-1] > ema21[-6],
        "above_50": price > sma50,
        "ma200_up": price > sma200 and sma200 >= sma200_prev,
        "near_high": price >= 0.90 * hi252,
        "weekly": weekly[-1] > w10[-1] > w30[-1],
        "mom_12_1": mom is not None and mom > 0.10,
        "rs_3m": r63 is not None and s63 is not None and r63 > s63,
        "rs_6m": r126 is not None and s126 is not None and r126 > s126,
        "ud_vol": up_v > dn_v,
        "obv_up": obv_delta > 0,
        "hh_hl": max(closes[:40]) > max(closes[40:80]) and min(closes[:40]) > min(closes[40:80]),
    }
    score = sum(1 for v in t.values() if v)
    return {
        "score": score,
        "traits": t,
        "price": round(price, 2),
        "ema21": round(ema21[-1], 2),
        "sma50": round(sma50, 2),
        "sma200": round(sma200, 2),
        "off_high_pct": round((price / hi252 - 1) * 100, 1),
        "rs_3m_pct": round((r63 - s63) * 100, 1) if r63 is not None and s63 is not None else None,
        "mom_12_1_pct": round(mom * 100, 1) if mom is not None else None,
        "sigma_pct": round(statistics.pstdev(
            [closes[i] / closes[i + 1] - 1 for i in range(20)]) * 100, 2),
    }


def grade_universe(histories: dict[str, list[dict]], spy_sym: str = "SPY") -> dict[str, dict]:
    """Score every name, then rank. Rank key = (score, relative strength vs SPY),
    so ties on the integer score are broken by the continuous RS measure.
    Adds rank, n, pct (rank/n, 0 = best), eligible (buyable), keep (holdable)."""
    spy_rows = histories.get(spy_sym) or []
    spy = [r["price"] for r in spy_rows if r.get("price")] or None
    graded = {}
    for sym, rows in histories.items():
        if not rows:
            continue
        g = score_one(rows, spy)
        if g:
            graded[sym] = g
    order = sorted(graded, key=lambda s: (graded[s]["score"],
                                          graded[s]["rs_3m_pct"] if graded[s]["rs_3m_pct"] is not None else -999),
                   reverse=True)
    n = len(order)
    for i, sym in enumerate(order, 1):
        g = graded[sym]
        g["rank"], g["n"], g["pct"] = i, n, i / n
        g["eligible"] = (g["pct"] <= ELIGIBLE_PCT and g["score"] >= MIN_ELIGIBLE_SCORE
                         and g["traits"]["rs_3m"])
        g["keep"] = g["pct"] <= HOLD_PCT
        g["grade"] = letter(g)
    return graded


def letter(g: dict) -> str:
    """A+ / A = buyable leaders; B = holdable (top 25%); C = neither."""
    if g.get("eligible"):
        return "A+" if g["score"] >= 11 else "A"
    if g.get("keep"):
        return "B"
    return "C"


def pullback_trigger(g: dict, price: float, rsi2: float | None) -> str | None:
    """WHEN to buy a leader. Returns the trigger name or None.
      RSI2 DIP:  RSI(2) < 10 (the Connors oversold print, now only on leaders)
      21 EMA:    price has pulled back to within +1% of the 21-day EMA, still above
                 the 50-day SMA, with RSI(2) < 50 so it is a real pullback, not a
                 stock riding the EMA up."""
    if rsi2 is not None and rsi2 < 10:
        return "RSI2 dip"
    if (g["ema21"] and price <= g["ema21"] * (1 + EMA21_TOUCH_BAND)
            and price > g["sma50"] and rsi2 is not None and rsi2 < 50):
        return "21 EMA pullback"
    return None


def trait_string(g: dict) -> str:
    """Compact list of the traits firing, e.g. 'MA STACK, 21 EMA UP, ...'."""
    labels = dict((k, lab) for k, lab, _ in TRAITS)
    return ", ".join(labels[k] for k, _, _ in TRAITS if g["traits"].get(k))
