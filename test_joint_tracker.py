"""Tests for build_joint_tracker: the data join and that the workbook builds."""
import json
import os
import tempfile

import build_joint_tracker as b

DATA = {
    "asof": "2026-10-29",
    "holdings": {"AAA": {"shares": 10, "avg_cost": 50.0}, "LEV": {"shares": 5, "avg_cost": 20.0},
                 "ZZZ^": {"shares": 3, "avg_cost": 0.0}},
    "market": {
        "AAA": {"name": "A Co", "type": "Stock", "price": 60.0, "sma50": 58, "sma200": 55, "low60": 52,
                "high60": 66, "high52": 70, "analyst_mean": 80, "earnings": "2026-11-02"},
        "LEV": {"name": "Lev", "type": "3x Lev ETF", "price": 25.0, "sma50": 30, "sma200": 28, "low60": 18,
                "high60": 35, "high52": 40},
        "ZZZ^": {"name": "none", "price": None},
        "BBB": {"name": "B Co", "price": 100.0, "sma50": 98, "sma200": 99, "analyst_mean": 130},
        "CCC": {"name": "C Co", "price": 40.0, "sma50": 41, "sma200": 39},
    },
    "quality": [{"sym": "CCC", "grade": "A", "rank": 2}, {"sym": "BBB", "grade": "A+", "rank": 1}],
    "new_industry": {"AAA": {"grade": "A", "industry": "Test"}},
    "notes": {"AAA": "note"},
}
TARGETS = {"rows": {"AAA": {"methods": {"robinhood": 79, "analysts": 81}, "final": 80, "agreement": "MED"}}}
SETUPS = {"rows": {"CCC": {"pre": 57, "pre_label": "PULLING BACK"}, "BBB": {"pre": 14, "pre_label": "EXTENDED"}}}


def test_holdings_rows_targets_and_skips():
    rows, skipped = b.holdings_rows(DATA, TARGETS, {})
    assert skipped == ["ZZZ^"]
    by = {r[0]: r for r in rows}
    assert by["AAA"][16] == 80 and by["AAA"][17] == "MED"
    assert by["LEV"][16] == 30 and by["LEV"][17] == "TECH (50-day)"  # leveraged ETF -> 50-day
    assert rows[0][0] == "AAA"  # biggest position first


def test_watch_rows_order_and_locks():
    rows = b.watch_rows(dict(DATA, _vals={}), SETUPS, {"names": {}},
                        {"lockouts": {"BBB": {"clear": "2026-11-22"}}})
    syms = [r[0] for r in rows]
    assert syms[:2] == ["CCC", "BBB"]  # most coiled first, not business rank
    assert rows[1][17].isoformat() == "2026-11-22"
    assert rows[2][2] == "New industry" and rows[2][3] == "HELD"


def test_build_writes_workbook():
    d = tempfile.mkdtemp()
    data_path = os.path.join(d, "data.json")
    json.dump(DATA, open(data_path, "w"))
    out = os.path.join(d, "t.xlsx")
    assert b.build(out, data_path) == out and os.path.getsize(out) > 0
