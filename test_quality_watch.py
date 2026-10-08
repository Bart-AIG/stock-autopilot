"""Tests for the re-buy watch in quality_watch.py (set 2026-10-08). No network.
Run: python test_quality_watch.py"""
import json
import tempfile

import quality_watch as qw
import risk_watch


def test_stages():
    assert qw.rebuy_status(79.2, 82.5, 86.1, False)["stage"] == "WAIT"
    assert qw.rebuy_status(79.2, 82.5, 86.1, True)["stage"] == "TURNING"
    assert qw.rebuy_status(84.0, 82.5, 86.1, False)["stage"] == "EARLY"
    assert qw.rebuy_status(87.0, 82.5, 86.1, True)["stage"] == "BUY"


def test_wash_sale():
    assert qw.wash_clear("2026-10-08") == "2026-11-08"
    s = qw.rebuy_status(87, 82, 86, True, today="2026-10-20", clear_date="2026-11-08")
    assert s["wash_sale_open"]
    s = qw.rebuy_status(87, 82, 86, True, today="2026-11-08", clear_date="2026-11-08")
    assert not s["wash_sale_open"]


def test_wanted_and_plan():
    assert qw.rebuy_wanted(79, 82, 86, False) == {"reclaim_50d", "reclaim_200d", "macd_turn"}
    assert qw.rebuy_wanted(84, 82, 86, True) == {"reclaim_200d"}
    entry = {"alerts": {"reclaim_50d": {"alert_id": "a"}, "reclaim_200d": {"alert_id": "b"},
                        "macd_turn": {"alert_id": "c"}}}
    # 50-day reclaimed (alert a fired and is gone); MACD turned up, c still live
    plan = qw.rebuy_plan(entry, {"reclaim_200d"}, live_ids={"b", "c"})
    assert plan["keep"] == ["reclaim_200d"]
    assert {"key": "macd_turn", "alert_id": "c"} in plan["delete"]
    assert {"key": "reclaim_50d", "alert_id": None} in plan["delete"]
    assert plan["create"] == []
    # price fell back under the 50-day: the fired reclaim alert is re-created
    plan = qw.rebuy_plan({"alerts": {}}, {"reclaim_50d"}, live_ids=set())
    assert plan["create"][0]["key"] == "reclaim_50d"
    assert plan["create"][0]["indicator"]["period"] == 50


def test_risk_watch_skips_rebuy_alerts():
    watch = {"names": {"CRCL": {"alerts": {"macd_turn": {"alert_id": "r1"}}}}}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(watch, f)
    assert risk_watch.rebuy_watch_alert_ids(f.name) == {"r1"}
    assert qw.rebuy_alert_ids(watch["names"]) == {"r1"}


def test_live_state_ids_are_skipped():
    ids = risk_watch.rebuy_watch_alert_ids()
    assert "e260f480-fc1c-48e0-950b-479e2ea1b0fa" in ids   # CRCL macd_turn


def test_report_section():
    rows = [{"symbol": "CRCL", "price": 79.2, "prev_stage": "WAIT", "sold_price": 79.2,
             "status": qw.rebuy_status(84, 82.5, 86.1, False, clear_date="2026-11-08",
                                       today="2026-10-20")}]
    md = "\n".join(qw.rebuy_report(rows))
    assert "EARLY" in md and "⬆" in md and "defers the loss" in md


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
