"""Valuation grade: is a stock cheap or expensive, and by how much (set 2026-10-02).

Ryan, live turn 2026-10-02: he asked whether any automated grade measures undervaluation
and by how much (none did), chose "the stock's own history + analyst targets as a
cross-check", and added: "make sure the industry is understood because some have variable
and cyclical things that others don't. I want this added to grades we are already doing
and worked into our process."

METHOD
1. Classify the company by FMP sector + industry into a PROFILE. The profile decides
   which multiples are honest for that kind of business (see PROFILES):
     bank / insurer  -> price-to-book first, P/E second. Free cash flow is meaningless
                        for a lender (loans flow through operating cash).
     REIT            -> price-to-operating-cash-flow (an FFO proxy) + EV/EBITDA. Never
                        P/E: depreciation on real estate makes REIT earnings misleading.
     cyclical        -> EV/sales + price-to-book (+ EV/EBITDA only when margins are
                        normal). Never P/E: earnings swing with the cycle, so a P/E looks
                        cheapest exactly at the peak (the classic value trap).
     growth          -> EV/sales, EV/EBITDA, price-to-FCF.
     utility         -> P/E, EV/EBITDA, price-to-book.
     pre-profit      -> EV/sales only, LOW confidence; no grade if sales are negligible.
     steady (default)-> P/E, EV/EBITDA, price-to-FCF.
2. For each multiple: today's (TTM) value vs the MEDIAN of the company's own last 10
   fiscal years (needs >= 5 valid years). The ratio says what the price would be if the
   stock traded at its usual multiple. EV multiples are converted to a price through net
   debt, so leverage is handled correctly.
3. Combine the multiples (weighted geometric mean) -> FAIR VALUE and GAP %:
   gap = fair / price - 1. Positive = undervalued by that much.
4. Cycle / business-change check: the profile's margin (EBITDA margin, or ROE for
   lenders) today vs its 10-year median. For a cyclical, a margin far above normal is
   PEAK-CYCLE and far below is TROUGH: EV/EBITDA is dropped (it would look falsely cheap
   at a peak, falsely expensive at a trough) and confidence falls. For anyone else a big
   margin shift means the business changed, so its own history is a weaker yardstick.
5. Analyst cross-check: median 12-month price target vs price. It never moves the gap;
   it lowers confidence when it points the other way.

GRADES (by gap %):  DEEP VALUE >= +25 | UNDERVALUED +10..+25 | FAIR -10..+10 |
                    RICH -25..-10 | EXPENSIVE < -25 | N/A (not enough history / data)

HONEST LIMITS: history is not destiny. A stock can sit below its own 10-year multiple
because its future is genuinely worse (a broken thesis), and a name whose business has
improved deserves a higher multiple than its past. That is what the confidence and the
flags are for. No backtest. This grade is CONTEXT for the joint/long-term account and the
Quality @ 200-day watch. It is never a gate on the mechanical sleeves (CLAUDE.md bans
unattended additions to them).

Pure functions + one fetch helper (fetch_inputs) that needs FMP. report.py builds
valuation.json each morning; quality_watch.py reads it.
"""
from __future__ import annotations

import json
import math
import statistics
import time
import urllib.error
import urllib.request
from pathlib import Path

import disruption

HERE = Path(__file__).resolve().parent
CACHE_FILE = HERE / "valuation.json"
BASE = "https://financialmodelingprep.com/stable"

MIN_YEARS = 5            # a multiple needs this many valid fiscal years to count
CLIP = (0.5, 2.0)        # one multiple can't imply more than 2x / less than half the price
RERATED = 0.5            # |gap| >= 50%: the market has re-rated the name; history is suspect
CYCLE_HIGH = 1.4         # margin >= 1.4x its 10-yr median = peak-cycle (cyclicals) / changed business
CYCLE_LOW = 0.6          # margin <= 0.6x its median = trough (cyclicals) / changed business
DISPERSION_MAX = 1.6     # metrics disagreeing by more than this (max/min fair) lowers confidence

# Multiple key -> (TTM field, annual field, kind, sane upper bound). kind "price" =
# price / per-share quantity; kind "ev" = enterprise value / quantity.
METRICS = {
    "pe":      ("priceToEarningsRatioTTM", "priceToEarningsRatio", "price", 150),
    "pb":      ("priceToBookRatioTTM", "priceToBookRatio", "price", 60),
    "pfcf":    ("priceToFreeCashFlowRatioTTM", "priceToFreeCashFlowRatio", "price", 200),
    "pocf":    ("priceToOperatingCashFlowRatioTTM", "priceToOperatingCashFlowRatio", "price", 150),
    "ev_sales": ("evToSalesTTM", "evToSales", "ev", 80),
    "ev_ebitda": ("evToEBITDATTM", "evToEBITDA", "ev", 120),
}
LABELS = {"pe": "P/E", "pb": "P/B", "pfcf": "P/FCF", "pocf": "P/CashFlow",
          "ev_sales": "EV/Sales", "ev_ebitda": "EV/EBITDA"}

# Profile -> {multiple: weight}, the margin used for the cycle check, and a one-line why.
PROFILES = {
    "bank":      ({"pb": 2, "pe": 1}, "roe",
                  "lender: valued on book value; FCF is meaningless for a bank"),
    "insurer":   ({"pb": 1, "pe": 1}, "roe",
                  "insurer: valued on book value and earnings"),
    "reit":      ({"pocf": 2, "ev_ebitda": 1}, "ebitda_margin",
                  "REIT: valued on cash flow (FFO proxy); P/E is distorted by depreciation"),
    "cyclical":  ({"ev_sales": 2, "pb": 1, "ev_ebitda": 1}, "ebitda_margin",
                  "cyclical: valued on sales and book; P/E looks cheapest at the peak"),
    "utility":   ({"pe": 1, "ev_ebitda": 1, "pb": 1}, "ebitda_margin",
                  "utility: regulated returns, valued on earnings and book"),
    "growth":    ({"ev_sales": 1, "ev_ebitda": 1, "pfcf": 1}, "ebitda_margin",
                  "growth: valued on sales, EBITDA and free cash flow"),
    "preprofit": ({"ev_sales": 1}, None,
                  "not yet profitable: sales multiple only, low confidence"),
    "steady":    ({"pe": 1, "ev_ebitda": 1, "pfcf": 1}, "ebitda_margin",
                  "steady earner: valued on earnings, EBITDA and free cash flow"),
}

# Industries whose earnings swing with a commodity or the economic cycle. Sector-wide
# for Energy and Basic Materials (steel, gold, copper, chemicals, aluminum, fertilizer).
CYCLICAL_SECTORS = {"Energy", "Basic Materials"}
CYCLICAL_INDUSTRY_WORDS = (
    "semiconductor", "auto -", "auto parts", "residential construction", "airline",
    "marine shipping", "trucking", "agricultural - machinery", "industrial - machinery",
    "steel", "gold", "silver", "copper", "aluminum", "coal", "oil & gas", "chemicals",
    "paper", "lumber", "building materials", "construction materials", "homebuilding",
    "travel lodging", "cruise", "recreational vehicles", "rental & leasing",
)
GROWTH_INDUSTRY_WORDS = (
    "software", "internet content", "information technology services", "internet retail",
    "electronic gaming", "communication equipment", "computer hardware", "cybersecurity",
    "consumer electronics",
)


def _f(x) -> float | None:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def classify(sector: str | None, industry: str | None, ttm: dict | None = None) -> str:
    """FMP sector + industry (+ TTM numbers for the pre-profit test) -> a PROFILES key."""
    s, i = (sector or "").strip(), (industry or "").strip().lower()
    t = ttm or {}
    ebitda_m, ev_sales = _f(t.get("ebitda_margin")), _f(t.get("ev_sales"))
    if i.startswith("banks") or i in ("financial - mortgages",):
        return "bank"
    if i.startswith("insurance"):
        return "insurer"
    if s == "Real Estate" and i.startswith("reit"):
        return "reit"
    # Losing money at the EBITDA line (or a sales multiple only a story can justify):
    # earnings-based multiples are undefined, so value on sales with low confidence.
    if ebitda_m is not None and ebitda_m <= 0:
        return "preprofit"
    if ev_sales is not None and ev_sales > 40 and s in ("Healthcare", "Technology"):
        return "preprofit"
    if s in CYCLICAL_SECTORS or any(w in i for w in CYCLICAL_INDUSTRY_WORDS):
        return "cyclical"
    if s == "Utilities" or i.startswith("regulated") or i.startswith("utilities"):
        return "utility"
    if s == "Technology" or any(w in i for w in GROWTH_INDUSTRY_WORDS):
        return "growth"
    return "steady"


def _hist_median(annual: list[dict], field: str, cap: float) -> tuple[float | None, int]:
    vals = [v for v in (_f(r.get(field)) for r in annual) if v is not None and 0 < v <= cap]
    return (statistics.median(vals), len(vals)) if len(vals) >= MIN_YEARS else (None, len(vals))


def implied_ratio(kind: str, cur: float, med: float, ev: float | None, mcap: float | None) -> float | None:
    """Fair price / current price if the multiple went back to its median.
    Price multiples scale linearly. EV multiples move enterprise value; net debt stays,
    so the equity (and price) moves by (fair EV - net debt) / market cap."""
    if not (cur and med and cur > 0 and med > 0):
        return None
    if kind == "price":
        return med / cur
    if not (ev and mcap and mcap > 0):
        return None
    fair_mcap = ev * med / cur - (ev - mcap)
    return fair_mcap / mcap if fair_mcap > 0 else None


def grade_label(gap: float | None) -> str:
    if gap is None:
        return "N/A"
    if gap >= 0.25:
        return "DEEP VALUE"
    if gap >= 0.10:
        return "UNDERVALUED"
    if gap > -0.10:
        return "FAIR"
    if gap > -0.25:
        return "RICH"
    return "EXPENSIVE"


# Sort order for ranking (lower = cheaper first); N/A sits in the middle, never rewarded.
TIER = {"DEEP VALUE": 0, "UNDERVALUED": 1, "FAIR": 2, "N/A": 3, "RICH": 4, "EXPENSIVE": 5}


def rank_tier(v: dict | None) -> int:
    """Tier used to RANK names. A LOW-confidence grade ranks as N/A: it is shown, never
    allowed to promote or demote a name."""
    if not v or v.get("confidence") == "LOW":
        return TIER["N/A"]
    return TIER.get(v.get("grade"), TIER["N/A"])


def value(inp: dict) -> dict:
    """inp = {symbol, sector, industry, price, mcap, ev, ttm: {metric keys + ebitda_margin,
    roe}, annual: [{annual fields + ebitdaMargin, returnOnEquity}], target_median}.
    Returns the grade dict (see module docstring). Never raises on missing data."""
    sym, price = inp.get("symbol"), _f(inp.get("price"))
    ttm, annual = inp.get("ttm") or {}, inp.get("annual") or []
    profile = classify(inp.get("sector"), inp.get("industry"), ttm)
    weights, margin_key, why = PROFILES[profile]
    weights = dict(weights)
    flags, conf = [], 3

    # Cycle / business-change check on the profile's margin.
    cycle = None
    if margin_key:
        annual_field = {"ebitda_margin": "ebitdaMargin", "roe": "returnOnEquity"}[margin_key]
        cur_m = _f(ttm.get(margin_key))
        hist = [v for v in (_f(r.get(annual_field)) for r in annual) if v is not None]
        med_m = statistics.median(hist) if len(hist) >= MIN_YEARS else None
        if cur_m is not None and med_m and med_m > 0:
            rel = cur_m / med_m
            if rel >= CYCLE_HIGH:
                cycle = "peak"
            elif rel <= CYCLE_LOW:
                cycle = "trough"
            if cycle and profile == "cyclical":
                weights.pop("ev_ebitda", None)
                flags.append(f"{'PEAK' if cycle == 'peak' else 'TROUGH'}-CYCLE margins "
                             f"({cur_m:.0%} vs {med_m:.0%} normal): earnings multiples ignored")
                conf -= 1
            elif cycle and profile in ("bank", "insurer"):
                flags.append(f"ROE {cur_m:.0%} vs {med_m:.0%} normal: credit/underwriting cycle "
                             f"{'high' if cycle == 'peak' else 'low'}")
                conf -= 1
            elif cycle:
                # Measured 2026-10-02: AMZN's EBITDA margin is ~2.5x its 10-yr median, so
                # its old P/E (thin margins) read +162% "cheap". A business that changed
                # shape is not comparable to its own past: confidence drops to LOW.
                flags.append(f"business changed (margin {cur_m:.0%} vs {med_m:.0%} 10-yr median): "
                             "its own history is a weak yardstick")
                conf -= 2

    parts, used = [], []
    for key, w in weights.items():
        ttm_f, ann_f, kind, cap = METRICS[key]
        cur = _f(ttm.get(key))
        if cur is None or cur <= 0 or cur > cap:
            continue
        med, n = _hist_median(annual, ann_f, cap)
        if med is None:
            continue
        r = implied_ratio(kind, cur, med, _f(inp.get("ev")), _f(inp.get("mcap")))
        if r is None:
            continue
        r = min(max(r, CLIP[0]), CLIP[1])
        parts.append((r, w))
        used.append({"metric": LABELS[key], "now": round(cur, 2), "median_10y": round(med, 2),
                     "years": n, "implied_gap_pct": round((r - 1) * 100, 1)})

    out = {"symbol": sym, "profile": profile, "basis": why, "sector": inp.get("sector"),
           "industry": inp.get("industry"), "price": price, "metrics": used, "flags": flags}
    if not parts or not price:
        out.update(fair=None, gap_pct=None, grade="N/A", confidence="LOW",
                   analyst_target=_f(inp.get("target_median")), analyst_upside_pct=None)
        out["flags"] = flags + ["not enough history for this industry's multiples"]
        return out

    wsum = sum(w for _, w in parts)
    ratio = math.exp(sum(w * math.log(r) for r, w in parts) / wsum)
    gap = ratio - 1
    if len(parts) == 1:
        conf -= 1
    rs = [r for r, _ in parts]
    if len(rs) > 1 and max(rs) / min(rs) > DISPERSION_MAX:
        conf -= 1
        flags.append("its multiples disagree with each other")
    if profile == "preprofit":
        conf = min(conf, 1)
    # Measured 2026-10-02: ADBE read +200% at HIGH (P/E ~17 vs a 10-yr median ~45) and
    # DELL -67%. A gap that large means the market re-priced the business itself (AI
    # disruption fear, a new growth story), so its own history is a weak anchor.
    if abs(gap) >= RERATED:
        conf -= 1
        flags.append("far from its own history: the market has re-rated it, find out why")

    tgt = _f(inp.get("target_median"))
    upside = tgt / price - 1 if tgt and price else None
    if upside is not None:
        # "Cheap" with analysts seeing < +5% (TROW 2026-10-02: +42% vs history, +4% to
        # target) usually means the market expects the business to shrink.
        # Scaled to the gap: ADBE +100% "cheap" with analysts at +9% is a disagreement.
        if (gap >= 0.10 and upside < max(0.05, gap / 4)) or (gap <= -0.10 and upside > 0.20):
            conf -= 1
            flags.append("analysts disagree")
        elif (gap >= 0.10 and upside >= 0.10) or (gap <= -0.10 and upside <= 0):
            flags.append("analysts agree")

    out.update(fair=round(price * ratio, 2), gap_pct=round(gap * 100, 1), grade=grade_label(gap),
               confidence={3: "HIGH", 2: "MED"}.get(conf, "LOW"),
               analyst_target=tgt, analyst_upside_pct=round(upside * 100, 1) if upside is not None else None)
    return out


# ---------------------------------------------------------------------------
# Forward price target, the way a sell-side analyst builds one (set 2026-10-09)
# ---------------------------------------------------------------------------
# Ryan, live turn 2026-10-09: "look at financials and basically do exactly what a financial
# analyst would do to determine what you think the price target is." A 12-month target is
# a FORWARD estimate times a JUSTIFIED multiple: next fiscal year's consensus EPS / EBITDA /
# revenue, times the multiple the stock has earned over its last 5 fiscal years (the recent
# regime, not 10 years: AI-era re-ratings make a 10-year median stale). EV multiples go
# through net debt to a per-share price. value() above answers "cheap vs its own past
# today"; this answers "where should it trade on next year's numbers".

FWD_YEARS = 5           # justified multiple = median of the last 5 fiscal years
FWD_MIN_YEARS = 3       # needs at least this many valid years
FWD_MIN_DAYS = 180      # use the first fiscal year ending at least ~6 months out
FWD_CLIP = (0.4, 3.0)   # one leg can't imply less than 0.4x or more than 3x today's price
FWD_LEGS = {            # profile -> {multiple: weight}; same industry logic as PROFILES
    "steady":    {"pe": 1, "ev_ebitda": 1},
    "utility":   {"pe": 1, "ev_ebitda": 1},
    "bank":      {"pe": 1},
    "insurer":   {"pe": 1},
    "reit":      {"ev_ebitda": 1},
    "growth":    {"pe": 1, "ev_ebitda": 1, "ev_sales": 1},
    "cyclical":  {"ev_sales": 2, "ev_ebitda": 1},   # never P/E: cheapest-looking at the peak
    "preprofit": {"ev_sales": 1},
}
FWD_EST = {"pe": ("epsAvg", "estimatedEpsAvg"),
           "ev_ebitda": ("ebitdaAvg", "estimatedEbitdaAvg"),
           "ev_sales": ("revenueAvg", "estimatedRevenueAvg")}


def _est(row: dict, key: str) -> float | None:
    for f in FWD_EST[key]:
        v = _f(row.get(f))
        if v is not None:
            return v
    return None


def forward_target(inp: dict, v: dict, today: str | None = None) -> dict | None:
    """Analyst-style 12-month target from next fiscal year's consensus estimates times the
    stock's 5-year median multiples. inp = fetch_inputs() dict, v = value(inp).
    Returns {target, upside_pct, fiscal_year_end, legs, confidence, basis} or None."""
    from datetime import date, timedelta
    price, mcap, ev = _f(inp.get("price")), _f(inp.get("mcap")), _f(inp.get("ev"))
    if not (price and mcap and price > 0 and mcap > 0):
        return None
    shares, net_debt = mcap / price, (ev - mcap) if ev else 0.0
    day0 = date.fromisoformat(today) if today else date.today()
    cutoff = (day0 + timedelta(days=FWD_MIN_DAYS)).isoformat()
    ests = sorted((e for e in inp.get("estimates") or [] if str(e.get("date"))[:10] >= cutoff),
                  key=lambda e: str(e.get("date")))
    if not ests:
        return None
    est = ests[0]
    annual = sorted(inp.get("annual") or [], key=lambda r: str(r.get("fiscalYear")), reverse=True)[:FWD_YEARS]
    legs_w = dict(FWD_LEGS.get(v.get("profile"), FWD_LEGS["steady"]))
    if any(f.startswith(("PEAK", "TROUGH")) for f in v.get("flags", [])):
        legs_w.pop("ev_ebitda", None)   # same rule as value(): no EBITDA multiple at a cycle extreme
    parts, legs = [], []
    for key, w in legs_w.items():
        _, ann_f, _, cap = METRICS[key]
        hist = [x for x in (_f(r.get(ann_f)) for r in annual) if x is not None and 0 < x <= cap]
        if len(hist) < FWD_MIN_YEARS:
            continue
        mult, fwd = statistics.median(hist), _est(est, key)
        if not fwd or fwd <= 0:
            continue
        tgt = mult * fwd if key == "pe" else (mult * fwd - net_debt) / shares
        if tgt <= 0:
            continue
        r = min(max(tgt / price, FWD_CLIP[0]), FWD_CLIP[1])
        parts.append((r, w))
        legs.append({"metric": LABELS[key], "multiple_5y": round(mult, 2), "estimate": fwd,
                     "implied": round(price * r, 2)})
    if not parts:
        return None
    ratio = math.exp(sum(w * math.log(r) for r, w in parts) / sum(w for _, w in parts))
    conf = 3 - (len(parts) == 1)
    rs = [r for r, _ in parts]
    if len(rs) > 1 and max(rs) / min(rs) > DISPERSION_MAX:
        conf -= 1
    n = _f(est.get("numAnalystsEps") or est.get("numAnalystsRevenue"))
    if n is not None and n < 3:
        conf -= 1
    if v.get("profile") == "preprofit" or any(r in (FWD_CLIP[0], FWD_CLIP[1]) for r in rs):
        conf = min(conf, 1)
    return {"target": round(price * ratio, 2), "upside_pct": round((ratio - 1) * 100, 1),
            "fiscal_year_end": str(est.get("date"))[:10], "legs": legs,
            "confidence": {3: "HIGH", 2: "MED"}.get(conf, "LOW"),
            "basis": f"FY ending {str(est.get('date'))[:10]} consensus x 5-yr median "
                     + " / ".join(l["metric"] for l in legs)}


LEGEND = ("_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within "
          "10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own "
          "10-year median multiples, using the multiples that suit its industry: banks/insurers on "
          "book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, "
          "homebuilders) on sales and book with earnings multiples dropped at a peak or trough, "
          "growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence "
          "(HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, "
          "the multiples disagree, or analysts' median target points the other way. Analysts = "
          "median 12-month target vs price. Relative to its OWN past only: when the whole market "
          "is above its history, most names read RICH._")


def short(v: dict | None) -> str:
    """Compact cell for a report table: 'UNDERVALUED +18% (MED)', or '—' when absent."""
    if not v:
        return "—"
    if v.get("gap_pct") is None:
        return "N/A"
    return f"{v['grade']} {v['gap_pct']:+.0f}% ({v['confidence']})"


def analyst_cell(v: dict | None) -> str:
    u = (v or {}).get("analyst_upside_pct")
    return f"{u:+.0f}%" if u is not None else "—"


# ---------------------------------------------------------------------------
# Data (FMP /stable, Starter plan: annual history only, ~10 years)
# ---------------------------------------------------------------------------

def _get(path: str, key: str):
    url = f"{BASE}/{path}{'&' if '?' in path else '?'}apikey={key}"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError, TimeoutError):
        return None


def fetch_inputs(sym: str, key: str, pause: float = 0.2) -> dict | None:
    """Six FMP calls -> the value() input dict. None if the profile is missing."""
    def first(x):
        return x[0] if isinstance(x, list) and x and isinstance(x[0], dict) else {}
    prof = first(_get(f"profile?symbol={sym}", key)); time.sleep(pause)
    if not prof:
        return None
    rt = first(_get(f"ratios-ttm?symbol={sym}", key)); time.sleep(pause)
    kt = first(_get(f"key-metrics-ttm?symbol={sym}", key)); time.sleep(pause)
    ra = _get(f"ratios?symbol={sym}&period=annual&limit=10", key) or []; time.sleep(pause)
    ka = _get(f"key-metrics?symbol={sym}&period=annual&limit=10", key) or []; time.sleep(pause)
    pt = first(_get(f"price-target-consensus?symbol={sym}", key)); time.sleep(pause)
    # For the disruption grade (disruption.py): 10 yrs of revenue / gross margin / R&D
    # and analysts' forward revenue.
    inc = _get(f"income-statement?symbol={sym}&period=annual&limit=10", key) or []; time.sleep(pause)
    est = _get(f"analyst-estimates?symbol={sym}&period=annual&limit=10", key) or []; time.sleep(pause)
    by_year = {}
    for r in (ra if isinstance(ra, list) else []) + (ka if isinstance(ka, list) else []):
        if isinstance(r, dict) and r.get("fiscalYear"):
            by_year.setdefault(r["fiscalYear"], {}).update(r)
    ttm = {k: rt.get(f) if f in rt else kt.get(f) for k, (f, _, _, _) in METRICS.items()}
    ttm["ebitda_margin"] = rt.get("ebitdaMarginTTM")
    ttm["roe"] = kt.get("returnOnEquityTTM")
    return {"symbol": sym, "sector": prof.get("sector"), "industry": prof.get("industry"),
            "price": prof.get("price"), "mcap": kt.get("marketCap") or prof.get("marketCap"),
            "ev": kt.get("enterpriseValueTTM"), "ttm": ttm, "annual": list(by_year.values()),
            "target_median": pt.get("targetMedian") or pt.get("targetConsensus"),
            "income": inc if isinstance(inc, list) else [],
            "estimates": est if isinstance(est, list) else []}


def build(symbols, key: str, cache: dict | None = None, today: str | None = None) -> dict:
    """Value each symbol (and attach its quant disruption grade under "disruption"),
    reusing today's cached rows. Returns {sym: value dict}."""
    cache = cache or {}
    out = {}
    for sym in dict.fromkeys(s for s in symbols if s):
        row = cache.get(sym)
        if row and today and row.get("asof") == today and "disruption" in row and "fwd" in row:
            out[sym] = row
            continue
        inp = fetch_inputs(sym, key)
        if inp is None:
            continue
        v = value(inp)
        v["disruption"] = disruption.score(inp["income"], inp["estimates"], v["profile"], v)
        v["fwd"] = forward_target(inp, v, today)
        v["asof"] = today
        out[sym] = v
    return out


def load_cache(path: Path = CACHE_FILE) -> dict:
    """{sym: value dict} from valuation.json; {} if missing or unreadable."""
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("rows", {})
    except (OSError, ValueError, AttributeError):
        return {}


def save_cache(rows: dict, asof_utc: str, path: Path = CACHE_FILE) -> None:
    path.write_text(json.dumps({"asof_utc": asof_utc, "method": "valuation.py",
                                "rows": dict(sorted(rows.items()))}, indent=1) + "\n",
                    encoding="utf-8")


if __name__ == "__main__":   # python valuation.py NUE GOOGL JPM ... (needs FMP_API_KEY)
    import os
    import sys
    k = os.environ.get("FMP_API_KEY")
    for s in sys.argv[1:]:
        i = fetch_inputs(s, k)
        v = value(i) if i else None
        if not v:
            print(s, "no data")
            continue
        d = disruption.score(i["income"], i["estimates"], v["profile"], v)
        print(f"{s:6} {d['label']:16} T{d['threat']} I{d['innovator']} {'; '.join(d['evidence'])}")
        print(f"{'':6} {v['profile']:9} {short(v):28} fair {v['fair']} vs {v['price']} | "
              f"analysts {analyst_cell(v)} | " + "; ".join(
                  f"{m['metric']} {m['now']} vs {m['median_10y']}" for m in v["metrics"])
              + (" | " + "; ".join(v["flags"]) if v["flags"] else ""))
