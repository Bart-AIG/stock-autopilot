"""Tests for disruption.py and its use in quality_watch.py. No network.
Run: python test_disruption.py"""
import json
import tempfile
from datetime import date
from pathlib import Path

import disruption as d
import quality_watch as qw


def inc(revs, gms=None, rd=0.0):
    """Annual income rows oldest -> newest, fiscal years 2016..."""
    gms = gms or [0.6] * len(revs)
    return [{"fiscalYear": str(2016 + i), "date": f"{2016 + i}-12-31", "revenue": r,
             "grossProfit": r * g, "researchAndDevelopmentExpenses": r * rd}
            for i, (r, g) in enumerate(zip(revs, gms))]


def est(year, rev):
    return [{"date": f"{year}-12-31", "revenueAvg": rev}]


def test_shrinking_revenue_and_margin_erosion_is_being_disrupted():
    revs = [100, 105, 110, 112, 110, 104, 98, 92, 88, 85]
    gms = [0.60, 0.60, 0.61, 0.60, 0.60, 0.60, 0.56, 0.53, 0.50, 0.48]
    out = d.score(inc(revs, gms), est(2026, 80), "steady")
    assert out["label"] == "BEING DISRUPTED"
    assert any("shrinking" in e for e in out["evidence"])
    assert any("gross margin down" in e for e in out["evidence"])


def test_fast_growth_margin_expansion_and_rd_is_disruptor():
    revs = [10, 12, 15, 19, 24, 30, 40, 55, 75, 100]
    gms = [0.55, 0.56, 0.57, 0.58, 0.60, 0.61, 0.62, 0.64, 0.67, 0.70]
    out = d.score(inc(revs, gms, rd=0.2), est(2026, 130), "growth")
    assert out["label"] == "DISRUPTOR" and out["threat"] == 0


def test_market_fear_flags_a_healthy_looking_business():
    # ADBE shape: +10%/yr, flat 89% margin, priced at half its own history.
    revs = [6, 7, 9, 11, 13, 16, 17.6, 19.4, 21.5, 23.8]
    out = d.score(inc(revs, [0.89] * 10, rd=0.18), est(2026, 26.6), "growth",
                  {"gap_pct": 100.0, "flags": []})
    assert out["label"] == "AT RISK"
    assert any("market fear" in e for e in out["evidence"])
    # A big gap caused by a changed business is NOT market fear.
    out2 = d.score(inc(revs, [0.89] * 10, rd=0.18), est(2026, 26.6), "growth",
                   {"gap_pct": 100.0, "flags": ["business changed (margin ...)"]})
    assert not any("market fear" in e for e in out2["evidence"])


def test_commodity_producer_swings_are_ignored():
    revs = [50, 40, 45, 60, 80, 70, 55, 65, 90, 120]
    gms = [0.2, 0.1, 0.15, 0.25, 0.35, 0.3, 0.2, 0.25, 0.3, 0.4]
    out = d.score(inc(revs, gms), est(2026, 150), "cyclical", {"sector": "Basic Materials"})
    assert out["label"] == "STABLE" and out["confidence"] == "LOW"


def test_bank_ignores_forward_estimates_and_rate_driven_growth():
    revs = [50, 52, 55, 54, 56, 60, 70, 90, 110, 120]
    out = d.score(inc(revs, [0] * 10), est(2026, 80), "bank")
    assert out["label"] == "STABLE"
    assert out["metrics"]["fwd_growth_pct"] is None


def test_boom_unwind_counts_once():
    # MRNA shape: tiny, then a 300x spike, then most of it gone.
    revs = [0.2, 0.1, 0.06, 0.8, 18.5, 19.3, 6.8, 3.2, 2.1, 2.0]
    gms = [0.5, 0.5, 0.5, 0.7, 0.85, 0.82, 0.6, 0.55, 0.5, 0.5]
    out = d.score(inc(revs, gms), [], "steady")
    assert any("one-time boom" in e for e in out["evidence"])
    assert out["label"] != "BEING DISRUPTED" and out["confidence"] == "LOW"


def test_notes_move_label_one_step_and_expire():
    q = {"label": "STABLE", "evidence": [], "confidence": "HIGH"}
    today = date(2026, 10, 2)
    threatened = d.combine(q, {"date": "2026-09-30", "verdict": "threatened", "summary": "x"}, today)
    assert threatened["final"] == "AT RISK"
    stale = d.combine(q, {"date": "2026-05-01", "verdict": "threatened"}, today)
    assert stale["final"] == "STABLE" and stale["note"] is None
    q2 = {"label": "INNOVATING", "evidence": [], "confidence": "HIGH"}
    assert d.combine(q2, {"date": "2026-10-01", "verdict": "disruptor"}, today)["final"] == "DISRUPTOR"
    # One step only: a "disrupted" note cannot take DISRUPTOR straight to BEING DISRUPTED.
    q3 = {"label": "DISRUPTOR", "evidence": [], "confidence": "HIGH"}
    assert d.combine(q3, {"date": "2026-10-01", "verdict": "disrupted"}, today)["final"] == "INNOVATING"


def test_value_trap_flag():
    assert d.value_trap({"grade": "DEEP VALUE"}, {"final": "AT RISK"})
    assert not d.value_trap({"grade": "DEEP VALUE"}, {"final": "STABLE"})
    assert not d.value_trap({"grade": "RICH"}, {"final": "BEING DISRUPTED"})


def test_save_note_round_trip():
    with tempfile.TemporaryDirectory() as t:
        p = Path(t) / "notes.json"
        d.save_note("ABC", "threatened", "AI rivals", ["XYZ"], [], ["https://x"], "test",
                    on="2026-10-02", path=p)
        assert d.load_notes(p)["ABC"]["verdict"] == "threatened"
        try:
            d.save_note("ABC", "doomed", "x", path=p)
            raise AssertionError("bad verdict accepted")
        except ValueError:
            pass


def _scan_row(sym, dist=0.0):
    return {"symbol": sym, "name": sym, "price": 100.0, "sma200": 100.0 / (1 + dist), "dist": dist,
            "sma200_rising": True, "group": None, "sector": None,
            "fundamental.quarterlyRevenueGrowth": 0.25, "fundamental.netProfitMargin": 0.30,
            "fundamental.operatingMargin": 0.30, "fundamental.grossMargin": 0.6,
            "fundamental.returnOnEquity": 0.3, "fundamental.cashFlowFreePerShare": 5}


def test_quality_watch_puts_threatened_cheap_names_after_healthy_ones():
    rows = [_scan_row("TRAP", 0.0), _scan_row("OK", 0.02)]
    vals = {"TRAP": {"symbol": "TRAP", "grade": "DEEP VALUE", "confidence": "HIGH", "gap_pct": 40,
                     "disruption": {"label": "AT RISK", "evidence": ["market fear"], "confidence": "HIGH"}},
            "OK": {"symbol": "OK", "grade": "FAIR", "confidence": "HIGH", "gap_pct": 0,
                   "disruption": {"label": "STABLE", "evidence": [], "confidence": "HIGH"}}}
    cands = qw.candidates(rows, vals=vals, notes={})
    assert [c["symbol"] for c in cands] == ["OK", "TRAP"]
    text = qw.report(cands, {"create": [], "delete": [], "keep": []}, "now", set())
    assert "VALUE TRAP?" in text and "Disruption grade" in text


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
