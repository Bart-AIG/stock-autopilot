"""Tests for price_targets.py and valuation.forward_target (set 2026-10-09). No network.
Run: python test_price_targets.py"""
import json
import tempfile
from datetime import date

import price_targets as pt
import risk_watch
import valuation

TODAY = date(2026, 10, 9)


def test_combine_median_of_three():
    c = pt.combine(100, {"value": 120}, {"value": 150}, {"value": 130})
    assert c["final"] == 130 and c["agreement"] == "MED" and c["upside_pct"] == 30.0
    assert c["status"] == "BELOW TARGET"


def test_combine_two_and_one():
    two = pt.combine(100, None, {"value": 120}, {"value": 130})
    assert two["final"] == 125 and two["agreement"] == "MED"   # analyst-only agreement capped
    assert pt.combine(100, {"value": 120}, {"value": 125}, None)["agreement"] == "HIGH"
    one = pt.combine(100, None, {"value": 120}, None)
    assert one["final"] == 120 and one["agreement"] == "LOW"
    assert pt.combine(130, {"value": 120}, None, None)["status"] == "AT/ABOVE TARGET"
    assert pt.combine(100, None, None, None)["final"] is None


def test_median_resists_one_outlier():
    # MU-style: a $3,000 street-high drags a mean, never the median of the three methods
    assert pt.combine(1000, {"value": 1300}, {"value": 1600}, {"value": 1550})["final"] == 1550


def test_fundamental_prefers_forward_and_drops_low():
    row = {"fair": 90, "confidence": "HIGH", "fwd": {"target": 140, "confidence": "MED", "basis": "x"}}
    assert pt.fundamental(row)["value"] == 140
    row["fwd"]["confidence"] = "LOW"
    assert pt.fundamental(row)["value"] == 90          # falls back to the history fair value
    row["confidence"] = "LOW"
    assert pt.fundamental(row) is None


def test_robinhood_needs_ratings():
    r = {"num_buy_ratings": 2, "num_hold_ratings": 1, "num_sell_ratings": 0, "mean_price_target": "50"}
    assert pt.robinhood(r)["value"] == 50
    r["num_hold_ratings"] = 0
    assert pt.robinhood(r) is None
    assert pt.robinhood(None) is None


def test_analysts_uses_fresh_dated_targets_only():
    note = {"date": "2026-10-09", "targets": [
        {"firm": "A", "target": 100, "date": "2026-10-01"},
        {"firm": "B", "target": 120, "date": "2026-09-15"},
        {"firm": "C", "target": 999, "date": "2026-01-01"},     # too old
        {"firm": "D", "target": 80, "date": "unclear"}]}        # undated
    a = pt.analysts(note, TODAY)
    assert a["value"] == 110 and a["n"] == 2
    note["targets"] = note["targets"][:1]
    assert pt.analysts(note, TODAY) is None


def test_research_due_oldest_first():
    notes = {"A": {"date": "2026-09-01"}, "B": {"date": "2026-10-01"}, "C": {"date": "2026-08-01"}}
    assert pt.research_due(notes, ["A", "B", "C", "D"], TODAY) == ["D", "C", "A"]


def test_plan_alerts():
    rows = {"UP": {"price": 100, "final": 130}, "HIT": {"price": 140, "final": 130},
            "MOVE": {"price": 100, "final": 150}, "SAME": {"price": 100, "final": 121},
            "FIRED": {"price": 100, "final": 131}, "RAISED": {"price": 100, "final": 150}}
    managed = {"HIT": {"alert_id": "h", "level": 130}, "MOVE": {"alert_id": "m", "level": 130},
               "SAME": {"alert_id": "s", "level": 120}, "FIRED": {"alert_id": "f", "level": 130},
               "RAISED": {"alert_id": "r", "level": 130}, "SOLD": {"alert_id": "x", "level": 50}}
    plan = pt.plan_alerts(rows, managed, live_ids={"h", "m", "s", "x"})
    assert {"symbol": "UP", "level": 130} in plan["create"]
    assert {"symbol": "RAISED", "level": 150} in plan["create"]          # target raised past the hit
    assert not any(c["symbol"] == "FIRED" for c in plan["create"])      # not re-armed at ~same level
    assert plan["update"] == [{"symbol": "MOVE", "alert_id": "m", "level": 150}]
    assert {"symbol": "HIT", "alert_id": "h"} in plan["delete"]          # price already above target
    assert {"symbol": "SOLD", "alert_id": "x"} in plan["delete"]
    assert {"symbol": "FIRED", "level": 130} in plan["fired"]
    assert not any(f["symbol"] == "SOLD" for f in plan["fired"])


def test_risk_watch_skips_price_target_alerts():
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"managed_alerts": {"MU": {"alert_id": "p1", "level": 1500}}}, f)
    assert risk_watch.price_target_alert_ids(f.name) == {"p1"}


def test_forward_target_steady():
    annual = [{"fiscalYear": str(y), "priceToEarningsRatio": 20, "evToEBITDA": 15} for y in range(2021, 2026)]
    inp = {"price": 100, "mcap": 100_000, "ev": 110_000, "annual": annual,
           "estimates": [{"date": "2026-12-31", "epsAvg": 5, "ebitdaAvg": 8000, "numAnalystsEps": 20},
                         {"date": "2027-12-31", "epsAvg": 6, "ebitdaAvg": 9000, "numAnalystsEps": 20}]}
    v = {"profile": "steady", "flags": []}
    f = valuation.forward_target(inp, v, "2026-10-09")
    # FY2027 (first year ending >= 6 months out): P/E 20 x $6 = $120; EV/EBITDA 15 x 9,000
    # = 135,000 EV - 10,000 net debt = 125,000 / 1,000 shares = $125; geometric mean ~ $122.47
    assert f["fiscal_year_end"] == "2027-12-31"
    assert abs(f["target"] - 122.47) < 0.05 and f["confidence"] == "HIGH"


def test_forward_target_cyclical_skips_pe_and_handles_missing():
    annual = [{"fiscalYear": str(y), "priceToEarningsRatio": 8, "evToSales": 4} for y in range(2021, 2026)]
    inp = {"price": 100, "mcap": 100_000, "ev": 100_000, "annual": annual,
           "estimates": [{"date": "2027-08-31", "epsAvg": 50, "revenueAvg": 30_000}]}
    f = valuation.forward_target(inp, {"profile": "cyclical", "flags": []}, "2026-10-09")
    assert [l["metric"] for l in f["legs"]] == ["EV/Sales"] and f["target"] == 120.0
    assert valuation.forward_target({**inp, "estimates": []}, {"profile": "cyclical"}, "2026-10-09") is None


def test_report_renders():
    md = pt.report({"MU": {"price": 1000, "final": 1550, "upside_pct": 55.0, "agreement": "HIGH",
                           "methods": {"robinhood": 1600}, "alert": "set"}}, "2026-10-09")
    assert "MU" in md and "$1,550.00" in md and "+55.0%" in md


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
