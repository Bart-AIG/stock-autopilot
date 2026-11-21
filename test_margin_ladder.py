"""Tests for margin_ladder.py (pure; synthetic bars). Run: python3 test_margin_ladder.py"""
import json
from datetime import date, timedelta
from pathlib import Path

import margin_ladder as ml

PLAN = json.loads((Path(__file__).parent / "margin_ladder_plan.json").read_text())


def days(end, n):
    out, d = [], date.fromisoformat(end)
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d -= timedelta(days=1)
    return out[::-1]


def bars_from(closes, end, rng=0.004):
    d = days(end, len(closes))
    return {"d": d, "o": list(closes), "h": [c * (1 + rng) for c in closes], "l": [c * (1 - rng) for c in closes],
            "c": list(closes), "v": [0.0] * len(closes)}


def market(end, qqq_last, spy_last, vix_last, vix_hist=25.0, n=300, q_base=700.0, s_base=740.0, tail=None):
    """Flat-ish history with chosen last closes. tail: list of (qqq, spy) for the final sessions."""
    q = [q_base] * n
    s = [s_base] * n
    if tail:
        for i, (a, b) in enumerate(tail):
            q[n - len(tail) + i], s[n - len(tail) + i] = a, b
    q[-1], s[-1] = qqq_last, spy_last
    v = [vix_hist] * n
    v[-1] = vix_last
    B = {"QQQ": bars_from(q, end), "SPY": bars_from(s, end)}
    V = {"d": B["QQQ"]["d"], "h": list(v), "c": list(v)}
    return B, V


def test_waits_for_not_before_and_notifies_once():
    B, V = market("2026-12-10", 650, 720, 24)          # stage 1 confirmation met on 12-10
    st, status, push = ml.run(PLAN, B, V, {}, "2026-12-10", True)
    assert st["stage"] == 0
    assert any("waits for 2026-12-21" in x for x in push)
    st2, _, push2 = ml.run(PLAN, B, V, st, "2026-12-10", True)
    assert not any("waits" in x for x in push2)


def test_unlocks_stage1_one_per_session():
    B, V = market("2026-12-22", 690, 740, 15)          # stage 1 and 2 confirmations both hold
    st, status, push = ml.run(PLAN, B, V, {}, "2026-12-22", True)
    assert st["stage"] == 1, st
    assert any(x.startswith("STAGE 1 UNLOCKED") for x in push)
    assert any("$10,000" in x for x in push)
    st2, _, push2 = ml.run(PLAN, B, V, st, "2026-12-22", True)
    assert st2["stage"] == 1 and not push2               # same session: no second stage


def test_provisional_never_moves():
    B, V = market("2026-12-22", 690, 740, 15)
    st, status, push = ml.run(PLAN, B, V, {}, "2026-12-22", False)
    assert st["stage"] == 0 and not any("UNLOCKED" in x for x in push)
    assert status["stages"][0]["confirm_ok"]


def test_dip_trigger_needs_vix_spike_and_top_half_close():
    tail = [(700, 740)] * 5 + [(588, 670)]
    B, V = market("2026-12-22", 588, 670, 34, vix_hist=30, tail=tail)
    assert ml.dip_date(PLAN, PLAN["stages"][0], B, V) is None          # no VIX spike above 36
    V["h"][-1] = 37.0
    assert ml.dip_date(PLAN, PLAN["stages"][0], B, V) == "2026-12-22"
    B["QQQ"]["c"][-1] = B["QQQ"]["l"][-1]                               # close at the low: not top half
    B["SPY"]["c"][-1] = B["SPY"]["l"][-1]
    assert ml.dip_date(PLAN, PLAN["stages"][0], B, V) is None


def test_delever_drops_stage_and_cools_down():
    B, V = market("2026-12-29", 660, 720, 24)          # QQQ under its 200-day (~700)
    prev = {"set": PLAN["set"], "stage": 3, "history": [], "notified": {}}
    st, status, push = ml.run(PLAN, B, V, prev, "2026-12-29", True)
    assert st["stage"] == 2, st
    assert any(x.startswith("DE-LEVER") for x in push)
    # next session the stage 3 confirmation would need >50-day anyway; check cooldown blocks a stage-2 -> 3 move
    B2, V2 = market("2026-12-30", 760, 800, 15)
    st2, status2, push2 = ml.run(PLAN, B2, V2, st, "2026-12-30", True)
    assert status2["cooling"] and st2["stage"] == 2


def test_new_selloff_rule_is_most_severe():
    B, V = market("2026-12-29", 600, 690, 31, q_base=700)
    prev = {"set": PLAN["set"], "stage": 4, "history": [], "notified": {}}
    st, _, push = ml.run(PLAN, B, V, prev, "2026-12-29", True)
    assert st["stage"] == 1, st


def test_no_delever_below_from_stage():
    B, V = market("2026-12-29", 600, 690, 31)
    prev = {"set": PLAN["set"], "stage": 2, "history": [], "notified": {}}
    st, _, push = ml.run(PLAN, B, V, prev, "2026-12-29", True)
    assert st["stage"] == 2 and not any("DE-LEVER" in x for x in push)


def test_trim_notice_once():
    B, V = market("2026-11-23", 610, 690, 34)
    st, _, push = ml.run(PLAN, B, V, {}, "2026-11-23", True)
    assert any("MPWR" in x for x in push)
    _, _, push2 = ml.run(PLAN, B, V, st, "2026-11-23", True)
    assert not any("MPWR" in x for x in push2)


def test_plan_adds_up():
    assert max(s["limit"] for s in PLAN["stages"]) == 60000
    for s in PLAN["stages"]:
        assert abs(sum(s["buys"].values()) - s["spend"]) <= 600, s["n"]
    tot = {}
    for s in PLAN["stages"]:
        for k, v in s["buys"].items():
            tot[k] = tot.get(k, 0) + v
    held = {"RBRK": 854}
    for k, v in tot.items():
        assert abs(v + held.get(k, 0) - PLAN["targets"][k]) <= 5, (k, v, PLAN["targets"][k])


def test_report_renders():
    B, V = market("2026-12-22", 690, 740, 15)
    st, status, _ = ml.run(PLAN, B, V, {}, "2026-12-22", True)
    md = ml.report(PLAN, status, "3:30 pm CT")
    assert "stage 1 of 4" in md and "| 2 |" in md


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
    print(f"ok: {n} margin ladder tests passed")
