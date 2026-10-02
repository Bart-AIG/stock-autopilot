"""Tests for valuation.py and its use in quality_watch.py. No network.
Run: python -m pytest test_valuation.py -q   (or python test_valuation.py)"""
import quality_watch as qw
import valuation as v


def annual(n=10, **fields):
    return [dict(fields) for _ in range(n)]


def base(sector, industry, ttm, ann, price=100.0, mcap=1000.0, ev=1000.0, tgt=None, sym="X"):
    return {"symbol": sym, "sector": sector, "industry": industry, "price": price, "mcap": mcap,
            "ev": ev, "ttm": ttm, "annual": ann, "target_median": tgt}


def test_classify_by_industry():
    assert v.classify("Financial Services", "Banks - Regional") == "bank"
    assert v.classify("Financial Services", "Insurance - Property & Casualty") == "insurer"
    assert v.classify("Real Estate", "REIT - Retail") == "reit"
    assert v.classify("Basic Materials", "Gold") == "cyclical"
    assert v.classify("Energy", "Oil & Gas Integrated") == "cyclical"
    assert v.classify("Technology", "Semiconductors") == "cyclical"
    assert v.classify("Consumer Cyclical", "Residential Construction") == "cyclical"
    assert v.classify("Utilities", "Regulated Electric") == "utility"
    assert v.classify("Technology", "Software - Application") == "growth"
    assert v.classify("Consumer Defensive", "Beverages - Non-Alcoholic") == "steady"
    assert v.classify("Healthcare", "Biotechnology", {"ebitda_margin": -0.3}) == "preprofit"
    # Financial-services data/payments are steady earners, not lenders.
    assert v.classify("Financial Services", "Financial - Credit Services") == "steady"


def test_steady_cheap_vs_own_history():
    # P/E 15 vs median 20, P/FCF 15 vs 20, EV/EBITDA 10 vs 10 (no net debt).
    inp = base("Consumer Defensive", "Packaged Foods",
               {"pe": 15, "pfcf": 15, "ev_ebitda": 10, "ebitda_margin": 0.2},
               annual(priceToEarningsRatio=20, priceToFreeCashFlowRatio=20, evToEBITDA=10,
                      ebitdaMargin=0.2), tgt=120)
    out = v.value(inp)
    assert out["profile"] == "steady"
    assert 18 < out["gap_pct"] < 23          # geometric mean of 1.333, 1.333, 1.0
    assert out["grade"] == "UNDERVALUED"
    assert out["confidence"] == "HIGH"
    assert "analysts agree" in out["flags"]


def test_bank_ignores_fcf_and_uses_book():
    inp = base("Financial Services", "Banks - Diversified",
               {"pb": 1.0, "pe": 10, "pfcf": 1.0, "roe": 0.12},
               annual(priceToBookRatio=1.5, priceToEarningsRatio=10, priceToFreeCashFlowRatio=50,
                      returnOnEquity=0.12))
    out = v.value(inp)
    assert {m["metric"] for m in out["metrics"]} == {"P/B", "P/E"}
    assert out["grade"] in ("UNDERVALUED", "DEEP VALUE")


def test_cyclical_peak_drops_ebitda_and_never_uses_pe():
    # At the peak EV/EBITDA looks half-price (5 vs 10) and P/E looks cheap too; both must
    # be ignored. Sales and book say fairly priced.
    inp = base("Basic Materials", "Steel",
               {"ev_sales": 1.0, "pb": 2.0, "ev_ebitda": 5, "pe": 5, "ebitda_margin": 0.30},
               annual(evToSales=1.0, priceToBookRatio=2.0, evToEBITDA=10, priceToEarningsRatio=15,
                      ebitdaMargin=0.15))
    out = v.value(inp)
    names = {m["metric"] for m in out["metrics"]}
    assert "EV/EBITDA" not in names and "P/E" not in names
    assert out["grade"] == "FAIR"
    assert any("PEAK-CYCLE" in f for f in out["flags"])
    assert out["confidence"] == "MED"


def test_ev_multiple_respects_net_debt():
    # EV 1500 = mcap 1000 + 500 net debt. EV/Sales falling back from 3 to 2 cuts EV to
    # 1000, i.e. equity 500: the price halves, not falls by a third.
    r = v.implied_ratio("ev", 3.0, 2.0, ev=1500, mcap=1000)
    assert abs(r - 0.5) < 1e-9
    assert v.implied_ratio("ev", 3.0, 1.0, ev=1500, mcap=1000) is None   # equity wiped


def test_business_changed_is_low_confidence_and_ranks_neutral():
    inp = base("Consumer Cyclical", "Specialty Retail",
               {"pe": 20, "ev_ebitda": 10, "ebitda_margin": 0.33},
               annual(priceToEarningsRatio=60, evToEBITDA=25, ebitdaMargin=0.13))
    out = v.value(inp)
    assert out["confidence"] == "LOW"
    assert v.rank_tier(out) == v.TIER["N/A"]


def test_cheap_but_analysts_flat_lowers_confidence():
    inp = base("Financial Services", "Asset Management",
               {"pe": 10, "pfcf": 10, "ev_ebitda": 7, "ebitda_margin": 0.4},
               annual(priceToEarningsRatio=14, priceToFreeCashFlowRatio=17, evToEBITDA=9,
                      ebitdaMargin=0.4), tgt=104)
    out = v.value(inp)
    assert out["grade"] == "DEEP VALUE" and out["confidence"] == "MED"
    assert "analysts disagree" in out["flags"]


def test_not_enough_history_is_na():
    inp = base("Consumer Defensive", "Beverages", {"pe": 20}, annual(n=3, priceToEarningsRatio=25))
    out = v.value(inp)
    assert out["grade"] == "N/A" and out["gap_pct"] is None
    assert v.short(out) == "N/A" and v.short(None) == "—"


def test_labels():
    assert v.grade_label(0.30) == "DEEP VALUE"
    assert v.grade_label(0.10) == "UNDERVALUED"
    assert v.grade_label(0.0) == "FAIR"
    assert v.grade_label(-0.15) == "RICH"
    assert v.grade_label(-0.40) == "EXPENSIVE"


def _scan_row(sym, dist=0.0):
    return {"symbol": sym, "name": sym, "price": 100.0, "sma200": 100.0 / (1 + dist), "dist": dist,
            "sma200_rising": True, "group": None, "sector": None,
            "fundamental.quarterlyRevenueGrowth": 0.25, "fundamental.netProfitMargin": 0.30,
            "fundamental.operatingMargin": 0.30, "fundamental.grossMargin": 0.6,
            "fundamental.returnOnEquity": 0.3, "fundamental.cashFlowFreePerShare": 5}


def test_quality_watch_ranks_cheaper_first_within_grade():
    rows = [_scan_row("RICHCO", 0.0), _scan_row("CHEAPCO", 0.04), _scan_row("NOVAL", 0.01)]
    vals = {"RICHCO": {"grade": "EXPENSIVE", "confidence": "HIGH", "gap_pct": -30},
            "CHEAPCO": {"grade": "UNDERVALUED", "confidence": "MED", "gap_pct": 15}}
    order = [c["symbol"] for c in qw.candidates(rows, vals=vals)]
    assert order == ["CHEAPCO", "NOVAL", "RICHCO"]
    text = qw.report(qw.candidates(rows, vals=vals), {"create": [], "delete": [], "keep": []},
                     "now", set())
    assert "UNDERVALUED +15% (MED)" in text and "Valuation grade" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
