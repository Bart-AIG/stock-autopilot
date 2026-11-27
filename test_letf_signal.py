"""Tests for letf_signal.py (the joint leveraged-ETF rule) and its push decisions.

Run: python3 test_letf_signal.py   (or pytest test_letf_signal.py)
The parity tests compare against letf_joint_backtest.py, the code the backtest ran; they need
pandas and are skipped where it is missing (the GitHub runner runs the rest).
"""
import csv
from datetime import date, timedelta
from pathlib import Path

import letf_signal as ls

HERE = Path(__file__).parent


def _csv(sym, col="close"):
    R = list(csv.DictReader(open(HERE / "data" / "letf" / f"{sym}.csv")))
    return [r["date"] for r in R], [float(r[col]) for r in R]


def _have_pandas():
    try:
        import pandas  # noqa: F401
        return True
    except ImportError:
        return False


def test_band_matches_the_backtest_rule():
    if not _have_pandas():
        print("  skipped: pandas not installed")
        return
    import letf_joint_backtest as B
    for sym in ("SPY", "QQQ", "SOXX"):
        u = B.load(sym)
        want = (B.rules(u, 3)["sma200_band2"][0] / 3).astype(int).tolist()
        got = ls.band_states(u["c"].tolist())
        assert got == want, sym


def test_size_matches_the_recommended_rule_on_fridays():
    if not _have_pandas():
        print("  skipped: pandas not installed")
        return
    import letf_joint_backtest as B
    u = B.load("SPY")
    expo, _ = B.rules(u, 3)["recommended"]
    fri = B.period_end(u.index, "W")
    c = u["c"].tolist()
    checked = 0
    for i in range(len(c) - 1, 300, -1):
        if fri.iloc[i] and expo.iloc[i] > 0:
            assert abs(ls.size_pct(ls.vol20(c[: i + 1])) - expo.iloc[i] / 3 * 100) < 0.06, u.index[i]
            checked += 1
            if checked >= 40:
                break
    assert checked == 40


def test_five_years_of_history_reach_the_full_history_state():
    for sym in ("SPY", "QQQ", "SOXX"):
        d, c = _csv(sym)
        full = ls.band_states(c)
        n = 1250                      # what the job fetches: about 5 years of sessions
        for end in range(len(c) - 250, len(c) + 1, 10):
            assert ls.band_states(c[end - n:end])[-1] == full[end - 1], (sym, d[end - 1])


def test_band_and_size_on_a_made_up_series():
    c = [100.0] * 200
    assert ls.band_states(c)[-1] == 0
    assert ls.band_states(c + [102.5])[-1] == 1          # 2.5% above a 200-day near 100 turns ON
    assert ls.band_states(c + [102.5, 101.0])[-1] == 1   # inside the band: no change
    assert ls.band_states(c + [102.5, 101.0, 97.0])[-1] == 0
    assert ls.size_pct(0.10) == 100.0 and ls.size_pct(0.25) == 66.7 and ls.size_pct(None) is None


def test_mutations_are_caught():
    d, c = _csv("SPY")
    base = ls.band_states(c)
    assert ls.band_states(c, band=0.01) != base
    assert ls.band_states(c, n=150) != base
    assert ls.size_pct(0.3, target=0.4) != ls.size_pct(0.3)


# ------------------------------------------------------------------ push decisions

def _r(sym, state, close, size=50.0, sma=100.0, since="2026-11-02", d="2026-11-25"):
    return {"sym": sym, "fund": ls.FUNDS[sym][0], "role": "", "date": d, "close": close, "sma200": sma,
            "on_line": sma * 1.02, "off_line": sma * 0.98, "vs_sma_pct": (close / sma - 1) * 100,
            "state": state, "since": since, "vol20_pct": 30.0, "size_pct": size}


FRI, MON, TUE = "2026-12-04", "2026-12-07", "2026-12-08"


def test_first_reading_pushes_once():
    conf = {"SPY": _r("SPY", "OFF", 97)}
    new, why, imp, kind = ls.decide(conf, None, {}, TUE, True, False)
    assert why == ["First reading of the joint leveraged-ETF signal"] and not imp
    new2, why2, *_ = ls.decide(conf, None, new, "2026-12-09", True, False)
    assert why2 == []


def test_a_confirmed_flip_pushes_with_the_flip_date():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-12-04"}
    new, why, imp, _ = ls.decide({"SPY": _r("SPY", "ON", 103, since=TUE, d=TUE)}, None, st, TUE, True, False)
    assert imp and why[0].startswith(f"SPY turned ON on the {TUE} close: BUY UPRO")
    assert new["confirmed"]["SPY"]["state"] == "ON"


def test_a_provisional_flip_does_not_change_the_stored_state():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-12-04"}
    new, why, *_ = ls.decide({"SPY": _r("SPY", "ON", 103)}, None, st, TUE, False, False)
    assert new["confirmed"]["SPY"]["state"] == "OFF" and not any("turned" in w for w in why)


def test_heads_up_once_per_index_per_session():
    st = {"confirmed": {"SPY": {"state": "ON"}}, "weekly_session": "2026-12-04"}
    conf = {"SPY": _r("SPY", "ON", 101)}
    live = {"SPY": _r("SPY", "OFF", 97.5)}
    new, why, imp, _ = ls.decide(conf, live, st, TUE, False, False)
    assert imp and "below the OFF line" in why[0] and "sell all UPRO" in why[0]
    _, why2, *_ = ls.decide(conf, live, new, TUE, False, False)
    assert why2 == []
    _, why3, *_ = ls.decide(conf, {"SPY": _r("SPY", "ON", 99)}, st, TUE, False, False)
    assert why3 == []                                   # inside the band: no heads-up


def test_friday_preview_then_a_quiet_close_when_nothing_changed():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-11-27"}
    conf = {"SPY": _r("SPY", "OFF", 97, d="2026-12-03")}
    live = {"SPY": _r("SPY", "OFF", 97.5, d=FRI)}
    new, why, imp, kind = ls.decide(conf, live, st, FRI, False, True)
    assert kind == "friday_preview" and why == ["Friday update, live prices, before the close"] and not imp
    _, why2, *_ = ls.decide(conf, live, new, FRI, False, True)
    assert why2 == []                                   # the preview goes out once
    new3, why3, *_ = ls.decide({"SPY": _r("SPY", "OFF", 97.4, d=FRI)}, None, new, FRI, True, False)
    assert why3 == [] and new3["weekly_session"] == FRI


def test_friday_close_pushes_when_it_changes_the_preview():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-11-27",
          "preview_session": FRI, "preview": {"SPY": {"state": "OFF", "size_pct": 50.0}}}
    _, why, imp, kind = ls.decide({"SPY": _r("SPY", "ON", 103, since=FRI, d=FRI)}, None, st, FRI, True, False)
    assert imp and kind == "friday_close" and any("changed the Friday update for SPY" in w for w in why)
    _, why2, imp2, _ = ls.decide({"SPY": _r("SPY", "OFF", 97, size=80.0, d=FRI)}, None,
                                 dict(st, confirmed={"SPY": {"state": "OFF"}}), FRI, True, False)
    assert imp2 and any("changed the Friday update" in w for w in why2)   # size moved 30 points


def test_missed_friday_is_caught_up_on_the_close_and_not_twice():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-11-27"}
    new, why, *_ = ls.decide({"SPY": _r("SPY", "OFF", 97, d=MON)}, None, st, MON, True, False)
    assert why == ["Catch-up: no weekly update since 2026-11-27"]
    _, why2, *_ = ls.decide({"SPY": _r("SPY", "OFF", 97, d=TUE)}, None, new, TUE, True, False)
    assert why2 == []


def test_friday_close_with_no_preview_sends_the_update():
    st = {"confirmed": {"SPY": {"state": "OFF"}}, "weekly_session": "2026-11-27"}
    _, why, imp, kind = ls.decide({"SPY": _r("SPY", "OFF", 97, d=FRI)}, None, st, FRI, True, False)
    assert why == ["Friday update, on the close"] and kind == "friday_close" and not imp


def test_live_action_is_conditional():
    r = _r("SPY", "ON", 103)
    assert ls.action_live(r, "OFF").startswith("if it closes here: BUY UPRO")
    assert ls.action_live(r, "ON").startswith("hold UPRO")


def test_dates_are_weekdays_as_expected():
    assert ls.weekday(FRI) == 4 and ls.weekday(MON) == 0
    assert date.fromisoformat(MON) - date.fromisoformat(FRI) == timedelta(days=3)


if __name__ == "__main__":
    tests = [(k, v) for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for name, fn in tests:
        fn()
        print("ok", name)
    print(f"{len(tests)} tests passed")
