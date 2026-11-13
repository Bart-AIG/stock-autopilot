#!/usr/bin/env python3
"""Tests for capital.py (sleeve money and the real-money drawdown). Run: python3 test_capital.py"""

import contextlib
import io
import json
import tempfile
from pathlib import Path

import capital as C


def approx(a, b, tol=1e-9):
    return abs(a - b) <= tol


NOW = "2026-11-13T19:31Z"


def read(st, **kw):
    """One reading with defaults that keep every other input still."""
    base = dict(total_value=2000.0, user_value=0.0, unrealized=0.0, realized=0.0, now=NOW)
    base.update(kw)
    return C.update(st, **base)


def test_sleeve_money():
    m = C.money(2493.54, 684.00, 1729.87)
    assert m["sleeve_money"] == 1809.54
    assert m["base"] == round(0.95 * 1809.54, 2)
    assert m["reserve"] == round(0.05 * 1809.54, 2)
    assert m["deployable"] == round(1729.87 - 0.05 * 1809.54, 2)
    assert C.money(100, 0, 2.0)["deployable"] == 0.0            # never negative
    # the four sleeve targets fit inside the money that exists
    import levx
    import sleeves
    w = sleeves.W_SWING_Q + 0.30 + 0.20 + levx.W_LEVX
    assert approx(w, 1.0), w
    assert w * m["base"] <= m["sleeve_money"] - m["reserve"] + 0.01
    for bad in ((None, 0), (float("nan"), 0), (-1, 0), (100, -5), (100, 150), (True, 0)):
        try:
            C.sleeve_money(*bad)
        except ValueError:
            continue
        raise AssertionError(f"accepted {bad}")


def test_index_follows_pnl_on_real_money():
    st = C.new_state()
    st, r = read(st, total_value=2000, unrealized=0, realized=0)        # first reading
    assert r["index"] == 1.0 and r["status"] == "ok" and r["action"] == "none"
    st, r = read(st, total_value=1900, unrealized=-100)                 # lost $100 of $2,000
    assert approx(st["index"], 0.95) and r["drawdown_pct"] == -5.0
    st, r = read(st, total_value=1995, unrealized=-5)                   # made $95 on $1,900
    assert approx(st["index"], 0.95 * (1 + 95 / 1900))
    assert approx(st["hwm_index"], 1.0)
    st, r = read(st, total_value=2100, unrealized=0, realized=100)      # +$105 on $1,995: above the old high
    assert st["index"] > 1.0 and approx(st["hwm_index"], 1.0)           # ...but a high needs two readings
    st, r = read(st, total_value=2100, unrealized=0, realized=100)
    assert approx(st["hwm_index"], st["index"]) and r["drawdown_pct"] == 0.0
    # one bad input cannot ratchet the high-water mark
    bad, _ = read(st, total_value=2300, unrealized=200, realized=100)   # a wrong +$200
    good, r = read(bad, total_value=2100, unrealized=0, realized=100)   # corrected on the next reading
    assert approx(good["hwm_index"], st["hwm_index"]) and approx(good["index"], st["index"], 1e-9)
    assert r["drawdown_pct"] == 0.0


def test_ryans_trades_and_deposits_never_move_the_index():
    st = C.new_state()
    st, _ = read(st, total_value=2500, user_value=500, unrealized=-10, realized=30)
    i0 = st["index"]
    # his option loses $400: total value and user value fall together
    st, r = read(st, total_value=2100, user_value=100, unrealized=-10, realized=30)
    assert approx(st["index"], i0) and r["sleeve_money"] if "sleeve_money" in r else True
    # he buys $1,500 more options with sleeve cash: user value up, total unchanged
    st, _ = read(st, total_value=2100, user_value=1600, unrealized=-10, realized=30)
    assert approx(st["index"], i0) and st["last"]["sleeve_money"] == 500.0
    # he deposits $5,000
    st, _ = read(st, total_value=7100, user_value=1600, unrealized=-10, realized=30)
    assert approx(st["index"], i0) and st["last"]["sleeve_money"] == 5500.0
    # the old add-back measure would have halted on the option loss alone; this one reads 0%
    assert st["status"] == "ok" and st["drawdown_pct"] == 0.0
    # and a sleeve loss is measured on the money that carried it ($5,500), not on total value
    st, r = read(st, total_value=6825, user_value=1600, unrealized=-285, realized=30)
    assert approx(st["index"], i0 * (1 - 275 / 5500)) and r["drawdown_pct"] == -5.0


def test_thresholds_notice_once_and_sticky_halt():
    st = C.new_state()
    st, _ = read(st, total_value=1000)
    st, r = read(st, total_value=810, unrealized=-190)                  # -19%
    assert r["status"] == "ok" and r["action"] == "none" and r["new_sleeve_buys_allowed"]
    st, r = read(st, total_value=795, unrealized=-205)                  # -20.5%
    assert r["status"] == "notify" and r["action"] == "notify" and r["new_sleeve_buys_allowed"]
    st, r = read(st, total_value=790, unrealized=-210)                  # still past -20%: no second notice
    assert r["status"] == "notify" and r["action"] == "none"
    st, r = read(st, total_value=830, unrealized=-170)                  # -17%: ok, notice still spent
    assert r["status"] == "ok" and st["notice_utc"]
    st, r = read(st, total_value=860, unrealized=-140)                  # above -15%: re-armed
    assert st["notice_utc"] is None
    st, r = read(st, total_value=795, unrealized=-205)
    assert r["action"] == "notify"
    st, r = read(st, total_value=745, unrealized=-255, now="2026-11-13T20:01Z")
    assert r["status"] == "halt" and r["action"] == "halt_notify" and not r["new_sleeve_buys_allowed"]
    assert st["halt"]["status"] == "ACTIVE" and st["halt"]["set_utc"] == "2026-11-13T20:01Z"
    st, r = read(st, total_value=820, unrealized=-180)
    st, r = read(st, total_value=900, unrealized=-100)                  # recovered to -10%: still halted
    assert approx(st["index"], 0.90) and r["drawdown_pct"] == -10.0
    assert r["status"] == "halt" and r["action"] == "halted" and not r["new_sleeve_buys_allowed"]
    # only a lift clears it, and it moves the high-water mark to the current index
    lifted = C.lift(st, now="lift-time", by="Ryan, live turn: 'lift it'")
    assert lifted["halt"] is None and lifted["status"] == "ok" and approx(lifted["hwm_index"], lifted["index"])
    assert lifted["lifts"][-1]["halt_was"]["status"] == "ACTIVE"
    lifted, r = read(lifted, total_value=900, unrealized=-100)
    assert r["status"] == "ok" and r["drawdown_pct"] == 0.0 and r["new_sleeve_buys_allowed"]
    assert approx(lifted["hwm_index"], 0.90)
    try:
        C.lift(st, now="x", by="  ")
    except ValueError:
        pass
    else:
        raise AssertionError("lift without a quote was accepted")


def test_suspect_reading_is_not_applied():
    st = C.new_state()
    st, _ = read(st, total_value=60, unrealized=0)                      # sleeves nearly empty
    before = json.dumps(st, sort_keys=True)
    # a deposit and a trade landed between two readings: -$50 on a $60 base is not a real -83%
    st2, r = read(st, total_value=5010, unrealized=-50)
    assert r["status"] == "suspect" and r["action"] == "suspect" and not r["new_sleeve_buys_allowed"]
    assert "Not applied" in r["notes"][-1] and "once" in r["notes"][-1]
    marker = st2.pop("suspect")
    st2["suspect"] = None
    assert json.dumps(st2, sort_keys=True) == before                    # index, high and last reading untouched
    assert marker["count"] == 1 and marker["step_pct"] == -83.3
    # the next run sees the same thing: still no buys, but no second notice
    st2["suspect"] = marker
    st3, r = read(st2, total_value=5010, unrealized=-50)
    assert r["action"] == "suspect_repeat" and not r["new_sleeve_buys_allowed"] and st3["suspect"]["count"] == 2
    assert approx(st3["index"], st["index"]) and st3["last"] == st["last"]
    # an interactive session checks the numbers and moves the starting point; the index does not move
    fixed = C.rebase(st3, total_value=5010, user_value=0, unrealized=-50, realized=0, now=NOW, by="checked by hand")
    assert fixed["suspect"] is None and approx(fixed["index"], st["index"]) and fixed["last"]["sleeve_money"] == 5010.0
    fixed, r = read(fixed, total_value=4960, unrealized=-100)
    assert r["status"] == "ok" and approx(fixed["index"], st["index"] * (1 - 50 / 5010))
    # a wrong input that is right on the next run clears itself
    st4, r = read(st2, total_value=60, unrealized=-1)
    assert r["status"] == "ok" and st4["suspect"] is None
    # with no sleeve money at the last reading there is no base at all: P/L change is skipped
    st0 = C.new_state()
    st0, _ = read(st0, total_value=500, user_value=500)
    st0, r = read(st0, total_value=2000, user_value=500, unrealized=-3)
    assert approx(st0["index"], 1.0) and r["status"] == "ok" and "no base" in r["notes"][0]


def test_inputs_are_checked_and_a_sale_does_not_move_the_index():
    st = C.new_state()
    for bad in (None, float("nan"), True):
        try:
            C.update(st, total_value=1000, user_value=0, unrealized=0, realized=bad, now=NOW)
        except ValueError:
            continue
        raise AssertionError(f"realized={bad!r} was accepted")
    with contextlib.redirect_stdout(io.StringIO()):
        assert C.main(["drawdown", "--tv", "1000", "--user-value", "0", "--unrealized", "0", "--now", NOW]) == 2
    # selling a position moves its P/L from unrealized to realized: the index does not move
    st, _ = read(st, total_value=1000, realized=32.64, unrealized=-35.0)
    st2, _ = read(st, total_value=1000, realized=-2.36, unrealized=0.0)
    assert approx(st2["index"], st["index"])
    # a different but consistent realized basis gives the same index: only changes count
    a = C.new_state(); b = C.new_state()
    a, _ = read(a, realized=0, unrealized=0); a, _ = read(a, realized=-20, unrealized=5)
    b, _ = read(b, realized=500, unrealized=0); b, _ = read(b, realized=480, unrealized=5)
    assert approx(a["index"], b["index"])


def test_result_lines_and_dollars_to_each_line():
    st = C.new_state(index=0.909, hwm_index=1.022, hwm_utc="2026-10-09")
    st, r = read(st, total_value=2493.54, user_value=684.0, realized=32.64, unrealized=-3.26)
    assert r["drawdown_pct"] == round(100 * (0.909 / 1.022 - 1), 2)
    assert r["notify_at_index"] == round(1.022 * 0.80, 6) and r["halt_at_index"] == round(1.022 * 0.75, 6)
    # losing usd_to_halt from here lands exactly on the halt line
    st2, r2 = read(st, total_value=2493.54 - r["usd_to_halt"], user_value=684.0, realized=32.64,
                   unrealized=-3.26 - r["usd_to_halt"])
    assert abs(st2["index"] - r["halt_at_index"]) < 2e-5                # to the cent
    st2, r2 = read(st, total_value=2493.54 - r["usd_to_halt"] - 0.02, user_value=684.0, realized=32.64,
                   unrealized=-3.26 - r["usd_to_halt"] - 0.02)
    assert r2["status"] == "halt"
    st3, r3 = read(st, total_value=2493.54 - r["usd_to_notify"] + 1, user_value=684.0, realized=32.64,
                   unrealized=-3.26 - r["usd_to_notify"] + 1)
    assert r3["status"] == "ok"


def test_today_and_month_marks():
    assert C.et_date("2026-11-13T19:31Z") == "2026-11-13"
    assert C.et_date("2026-11-14T00:45Z") == "2026-11-13"                # evening ET is still the same trading day
    assert C.et_date("2026-11-13T21:19:07Z") == "2026-11-13"
    st = C.new_state()
    st, r = read(st, total_value=1000, now="2026-11-12T20:31Z")
    assert r["today_pct"] == 0.0 and r["month_to_date_pct"] == 0.0
    st, r = read(st, total_value=990, unrealized=-10, now="2026-11-12T20:46Z")
    assert r["today_pct"] == -1.0
    # the overnight gap belongs to the new day
    st, r = read(st, total_value=970.2, unrealized=-29.8, now="2026-11-13T14:31Z")
    assert r["today_pct"] == -2.0 and r["month_to_date_pct"] == round(100 * (0.99 * 0.98 - 1), 2)
    st, r = read(st, total_value=970.2, unrealized=-29.8, now="2026-12-01T14:31Z")
    assert r["today_pct"] == 0.0 and r["month_to_date_pct"] == 0.0 and st["marks"]["month"] == "2026-12"
    assert r["since_start_pct"] == round(100 * (0.99 * 0.98 - 1), 2)


def test_ledger_write_keeps_the_file_format():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "holdings.json"
        ledger = {"updated_utc": "x", "note": "em dash — stays escaped",
                  "_SLEEVE_PROCESS": {"start_utc": "2026-09-30T20:14Z", "drawdown_real": C.new_state()},
                  "positions": [{"symbol": "ILMN", "shares": 0.384363}]}
        p.write_text(json.dumps(ledger, indent=2))
        before = p.read_text()
        with contextlib.redirect_stdout(io.StringIO()):
            rc = C.main(["drawdown", "--tv", "2000", "--user-value", "500", "--unrealized", "-3", "--realized",
                         "10", "--now", "2026-11-13T21:30Z", "--write", "--ledger", str(p)])
        assert rc == 0
        after = p.read_text()
        assert "\\u2014" in after and after.count("\n") > before.count("\n")
        h = json.loads(after)
        assert h["positions"] == ledger["positions"] and h["note"] == ledger["note"]
        assert h["_SLEEVE_PROCESS"]["drawdown_real"]["last"]["sleeve_money"] == 1500.0
        assert json.dumps(h, indent=2) == after                         # still round-trips
        # a file in another format is refused, not reformatted
        p.write_text(json.dumps(ledger, indent=1))
        try:
            C.write_state(C.new_state(), p)
        except SystemExit as e:
            assert "round-trip" in str(e)
        else:
            raise AssertionError("reformatted a ledger that was not indent=2")
        assert p.read_text() == json.dumps(ledger, indent=1)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("ok")
