"""Tests for earnings.py, the VIX reading in risk_watch.grade(), and the new scan columns."""
import earnings as e
import quality_watch as qw
import risk_watch as rw

AMZN = [  # trimmed get_earnings_results rows, 2026-10-23
    {"eps": {"actual": "5.75"}, "report": {"date": "2026-07-30", "timing": "pm", "verified": True}},
    {"eps": {"actual": None}, "report": {"date": "2026-10-29", "timing": "pm", "verified": True}},
    {"eps": {"actual": None}, "report": {"date": "2027-02-04", "timing": "pm", "verified": False}},
]


def test_next_report_and_cell():
    n = e.next_report(AMZN, "2026-10-23")
    assert n == {"date": "2026-10-29", "timing": "pm", "verified": True, "days": 6}
    assert e.soon(n) and e.cell(n) == "**Oct 29 pm (6d)**"
    assert e.next_report([], "2026-10-23") is None and e.cell(None) == "—"


def test_scanner_ymd():
    assert e.from_ymd("2.0261028e+07") == "2026-10-28"
    assert e.from_ymd("") is None and e.from_ymd("2.0261399e+07") is None
    s = e.from_scan("2.0270127e+07", "2026-10-23")
    assert s["days"] == 96 and not s["verified"] and e.cell(s) == "Jan 27? (96d)"
    assert e.from_scan("2.0261001e+07", "2026-10-23") is None   # already past


def test_vix_scoring_shares_one_slot_with_vixy():
    vixy = [{"alert_id": "v", "symbol": "VIXY", "condition_type": "price_above", "enabled": True,
             "condition": {"target_price": "21.15"}}]
    assert rw.vix_points(20.25) == 0 and rw.vix_points(22) == 1 and rw.vix_points(27) == 2 and rw.vix_points(40) == 3
    calm = rw.grade(vixy, {"VIXY": 17.5}, ignore_ids=set(), vix=20.25)
    assert calm["score"] == 0 and any(r["symbol"] == "VIX" and not r["triggered"] for r in calm["readings"])
    # VIX 27 (2 pts) with VIXY under its alert: the VIX counts
    assert rw.grade(vixy, {"VIXY": 17.5}, ignore_ids=set(), vix=27)["score"] == 2
    # VIXY fired (2 pts) and VIX 23 (1 pt): one slot, the larger (2), not 3
    assert rw.grade(vixy, {"VIXY": 22.0}, ignore_ids=set(), vix=23)["score"] == 2
    # no vix passed: unchanged behaviour
    assert rw.grade(vixy, {"VIXY": 22.0}, ignore_ids=set())["score"] == 2


def test_scan_display_columns_pass_through():
    r = qw.from_scan({"ticker": "CDNS", "columns": {"Forward P/E": "32.36", "Earnings date": "2.0261026e+07",
                                                    "Beta": "1.25", "Last": "315", "200d SMA": "327"}})
    assert r["fundamental.forwardPeRatio"] == "32.36" and r["fundamental.earningsYmd"] == "2.0261026e+07"
    assert qw._pe(32.36) == "32.4" and qw._pe(None) == "—" and qw._pe(-3) == "—"
