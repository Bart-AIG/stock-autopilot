"""Tests for bottom_watch.py and bottom_watch_run.py.

Run: python3 test_bottom_watch.py   (or pytest test_bottom_watch.py)
"""
import json
import random
from datetime import date, datetime, timedelta
from pathlib import Path

import bottom_watch as bw
import bottom_watch_run as run

HERE = Path(__file__).parent
MODEL = json.loads((HERE / "bottom_model.json").read_text())
PLAN = {"set": None, "vix_spike": 36,          # "set" is filled in below: the first session after the flat stretch
        "steps": [{"name": "Buy step 1", "QQQ": 590, "SPY": 675, "amount": "1/3 of cash"}],
        "turn": {"QQQ": 648, "SPY": 716, "vix_below": 26}, "trend": {"vix_below": 22}}


def _days(n, start=date(2020, 1, 1)):
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def _bars(closes, lows=None, highs=None):
    n = len(closes)
    return {"d": _days(n), "o": list(closes), "h": list(highs or [c * 1.002 for c in closes]),
            "l": list(lows or [c * 0.998 for c in closes]), "c": list(closes), "v": [1e6] * n}


PLAN["set"] = _days(301)[300]


def _path(*legs, flat=300, level=100.0):
    """Flat at `level`, then straight-line legs [(target, sessions), ...]."""
    c = [level] * flat
    for target, n in legs:
        a = c[-1]
        c += [a + (target - a) * (i + 1) / n for i in range(n)]
    return c


def _real():
    return run.offline({}, None)


# ---------------------------------------------------------------- the engine

def test_known_final_lows():
    bars, V = _real()
    vix = dict(zip(V["d"], V["c"]))
    want = {"QQQ": {"2021-11-19": "2022-12-28", "2025-02-19": "2025-04-08"},
            "SPY": {"2022-01-03": "2022-10-12", "2025-02-19": "2025-04-08"}}
    for s in ("QQQ", "SPY"):
        rows, eps = bw.scan(s, bars[s], vix)
        got = {bars[s]["d"][e["peak_i"]]: bars[s]["d"][e["low_i"]] for e in eps}
        for pk, low in want[s].items():
            assert got.get(pk) == low, (s, pk, got.get(pk))
        done = [r for r in rows if r["y"] is not None]
        assert len(done) > 2000 and 0.3 < sum(r["y"] for r in done) / len(done) < 0.7


def test_nothing_from_the_future():
    """A day's variables must be the same whether or not later bars exist."""
    bars, V = _real()
    vix = dict(zip(V["d"], V["c"]))
    B = bars["QQQ"]
    full = {r["i"]: r for r in bw.scan("QQQ", B, vix)[0]}
    random.seed(7)
    for j in random.sample(sorted(full), 12):
        cut = {k: v[:j + 1] for k, v in B.items()}
        last = bw.scan("QQQ", cut, vix)[0][-1]
        assert last["i"] == j
        for k, v in last.items():
            if k == "y":
                continue
            w = full[j][k]
            assert (v == w) or (isinstance(v, float) and abs(v - w) < 1e-9), (j, k, v, w)


def test_probability_direction_and_bounds():
    f = {"dist200": -0.08, "retr": 0.15}
    p0, basis = bw.probability(MODEL, f)
    assert basis == "full" and 0.03 <= p0 <= 0.95
    assert bw.probability(MODEL, {**f, "dist200": 0.03})[0] > p0       # back above the 200-day
    assert bw.probability(MODEL, {**f, "retr": 0.6})[0] > p0           # more of the drop retraced
    lo = bw.probability(MODEL, {"dist200": -0.9, "retr": 0.0})[0]
    hi = bw.probability(MODEL, {"dist200": 0.9, "retr": 1.0})[0]
    assert 0.03 <= lo < 0.25 and 0.85 <= hi <= 0.95                    # never certain either way
    assert bw.probability(MODEL, {"dist200": None, "retr": 0.2}) == (None, "missing")


def test_price_that_would_move_the_reading():
    f = {"runlow": 600.0, "peak": 760.0}
    p50, p70 = bw.price_for(MODEL, f, 683.0, 0.5), bw.price_for(MODEL, f, 683.0, 0.7)
    assert 600 < p50 < p70 < 760
    at = lambda c: bw.probability(MODEL, {"dist200": c / 683.0 - 1, "retr": (c - 600) / 160})[0]
    assert abs(at(p50) - 0.5) < 0.01 and abs(at(p70) - 0.7) < 0.01 and at(p50 - 5) < 0.5
    assert bw.price_for({**MODEL, "features": ["dist200", "retr", "rsi14"]}, f, 683.0, 0.5) is None   # only for the price-only model
    assert bw.price_for(MODEL, f, 683.0, 0.99) is None                                              # the model never says 99%


def test_model_file():
    n = len(MODEL["features"])
    assert n == len(MODEL["mean"]) == len(MODEL["sd"]) == len(MODEL["beta"])
    ys = [k[1] for k in MODEL["calibration"]]
    assert ys == sorted(ys) and all(0.03 <= y <= 0.95 for y in ys)
    assert MODEL["features"] == ["dist200", "retr"] and all(b > 0 for b in MODEL["beta"])
    assert MODEL["oos"]["auc"] > 0.75 and MODEL["oos"]["skill"] > 0.25
    assert len(MODEL["checkpoints"]) >= 6 and all(0.5 < c["hit"] < 1 and c["hit"] > c["miss"] for c in MODEL["checkpoints"])


def test_stages():
    def stage(c):
        return bw.reading("QQQ", _bars(c), None, MODEL)
    r = stage(_path((85, 10)))
    assert r["stage"] == "NEW LOW" and r["open"] and r["days"] == 0 and r["basis"] == "full" and r["vix"] is None
    r = stage(_path((85, 10), (92, 5)))
    assert r["stage"] == "REBOUND" and abs(r["reb"] - (92 / 85 - 1)) < 1e-9 and r["days"] == 5
    r = stage(_path((85, 10), (92, 5), (86, 4)))
    assert r["stage"] == "RETEST" and r["legs"] == 0
    r = stage(_path((85, 10), (92, 5), (84, 4)))
    assert r["stage"] == "FAILED REBOUND" and r["legs"] == 1
    r = stage(_path((85, 10), (92, 5), (84, 4), (83, 1)))
    assert r["stage"] == "NEW LOW" and r["legs"] == 1          # the day after a failed rebound is just a new low
    r = stage(_path((85, 10), (97.5, 12)))
    assert r["stage"] == "RECOVERED" and not r["open"]
    r = stage(_path((85, 10), (97.5, 12), (98, 1)))
    assert r["stage"] == "NO SELLOFF"
    r = stage(_path((95, 5)))
    assert r["stage"] == "NO SELLOFF" and abs(r["starts_at"] - 90) < 1e-9


def test_spy_starts_at_eight_percent():
    assert bw.reading("SPY", _bars(_path((91.5, 5))), None, MODEL)["stage"] == "NEW LOW"
    assert bw.reading("QQQ", _bars(_path((91.5, 5))), None, MODEL)["stage"] == "NO SELLOFF"


# ---------------------------------------------------------------- buy-back levels

def _plan_case(qqq_tail, vix_tail, provisional=False):
    """300 flat sessions at 700 then the given (low, high, close) bars; VIX highs alongside."""
    n = 300 + len(qqq_tail)
    c = [700.0] * 300 + [x[2] for x in qqq_tail]
    B = _bars(c, lows=[699.0] * 300 + [x[0] for x in qqq_tail], highs=[701.0] * 300 + [x[1] for x in qqq_tail])
    S = _bars([800.0] * n)
    V = {"d": B["d"], "h": [15.0] * 300 + list(vix_tail), "c": [15.0] * 300 + [v - 1 for v in vix_tail]}
    return bw.plan_status(PLAN, {"QQQ": B, "SPY": S}, V, B["d"][290], provisional)


def test_buy_step_needs_level_vix_spike_and_an_up_close():
    it = _plan_case([(640, 660, 650)], [30])[0]
    assert it["state"] == "not_reached"
    it = _plan_case([(585, 620, 586)], [30])[0]                     # level hit, no VIX spike
    assert it["state"] == "reached" and "VIX has not spiked" in it["gap"]
    it = _plan_case([(585, 620, 586)], [38])[0]                     # level hit, VIX spiked, closed at its low
    assert it["state"] == "reached" and "top half" in it["gap"]
    it = _plan_case([(585, 620, 586), (580, 600, 598)], [38, 33])[0]   # the first up-close after it
    assert it["state"] == "met" and it["sym"] == "QQQ"
    it = _plan_case([(585, 620, 586), (580, 600, 598)], [38, 33], provisional=True)[0]
    assert it["state"] == "met_provisional"                         # today's bar is a live price, not a close
    it = _plan_case([(585, 620, 586), (580, 600, 598), (600, 615, 610)], [38, 33, 30], provisional=True)[0]
    assert it["state"] == "met"                                     # met on an earlier, finished session


def test_turn_and_trend_triggers():
    turn = _plan_case([(640, 655, 650)], [30])[1]
    assert turn["name"] == "Turn trigger" and turn["state"] == "not_reached"       # above 648 but VIX closed 29
    turn = _plan_case([(640, 655, 650)], [26.5])[1]
    assert turn["state"] == "met"
    trend = _plan_case([(640, 655, 650)], [22.5])[2]
    assert trend["name"] == "Trend repaired" and trend["state"] == "not_reached"   # QQQ under its 200-day, SPY at it
    trend = _plan_case([(700, 712, 710)], [22.5])[2]
    assert trend["state"] == "met"


# ---------------------------------------------------------------- when to push

def _reading(**kw):
    r = {"sym": "QQQ", "stage": "REBOUND", "prob": 0.40, "band": 1, "peak_date": "2026-10-06", "ddclose": -0.15,
         "close": 640.0, "low": 615.0, "low_date": "2026-11-20", "reb": 0.04, "maxreb": 0.05}
    r.update(kw)
    return {"QQQ": r}


def test_push_rules():
    why, note, imp = bw.decide({}, _reading(), [], "2026-11-23", False, False)
    assert len(why) == 1 and "is in a selloff" in why[0] and imp
    prev = {"notified": note, "pushed": {"QQQ": {"prob": 0.40, "band": 1, "stage": "REBOUND", "episode": "2026-10-06"}}}
    assert bw.decide(prev, _reading(), [], "2026-11-23", False, False)[0] == []          # nothing changed: silent
    assert bw.decide(prev, _reading(prob=0.52, band=2), [], "2026-11-23", False, False)[0] != []
    assert bw.decide(prev, _reading(prob=0.51, band=2, stage="REBOUND"), [], "2026-11-23", False, False)[0] != []
    near = {**prev, "pushed": {"QQQ": {"prob": 0.49, "band": 1, "stage": "REBOUND", "episode": "2026-10-06"}}}
    assert bw.decide(near, _reading(prob=0.51, band=2), [], "2026-11-23", False, False)[0] == []   # 2 points is not news
    why = bw.decide(prev, _reading(stage="NEW LOW", prob=0.2, band=0), [], "2026-11-23", False, False)[0]
    assert any("trading under its lowest close" in w for w in why)
    why = bw.decide(prev, _reading(stage="NEW LOW", prob=0.2, band=0), [], "2026-11-23", True, False)[0]
    assert any("new closing low" in w for w in why) and any("Daily summary" in w for w in why)
    why, note2, imp = bw.decide(prev, _reading(), [], "2026-11-23", True, False)
    assert why == ["Daily summary after the close"] and not imp
    assert bw.decide({**prev, "notified": note2}, _reading(), [], "2026-11-23", True, False)[0] == []   # one summary a day
    assert bw.decide(prev, {"QQQ": {"sym": "QQQ", "stage": "NO SELLOFF"}}, [], "2026-11-23", True, False)[0] == []


def test_plan_pushes_once():
    item = {"key": "2026-11-20:Buy step 1", "name": "Buy step 1", "text": "QQQ $590 or SPY $675", "state": "reached",
            "date": "2026-11-23", "gap": "waiting for a close in the top half of the day's range"}
    prev = {"pushed": {"QQQ": {"prob": 0.40, "band": 1, "stage": "REBOUND", "episode": "2026-10-06"}}}
    why, note, _ = bw.decide(prev, _reading(), [item], "2026-11-23", False, False)
    assert len(why) == 1 and "level reached" in why[0]
    prev["notified"] = note
    assert bw.decide(prev, _reading(), [item], "2026-11-23", False, False)[0] == []
    live = {**item, "state": "met_provisional"}
    assert bw.decide(prev, _reading(), [live], "2026-11-23", False, False)[0] == []      # too early in the day to act on
    why, note, _ = bw.decide(prev, _reading(), [live], "2026-11-23", False, True)
    assert len(why) == 1 and "so far today" in why[0]
    prev["notified"] = note
    why, _, _ = bw.decide(prev, _reading(), [{**item, "state": "met"}], "2026-11-23", True, False)
    assert any("conditions met at the Nov 23 close" in w for w in why)


# ---------------------------------------------------------------- the job

def test_merge_live_quote():
    B = _bars([100.0] * 5)
    last = B["d"][-1]
    nxt = (datetime.fromisoformat(last) + timedelta(days=1)).replace(hour=15, tzinfo=run.ET)
    q = {"price": 98.0, "open": 100.5, "dayHigh": 101.0, "dayLow": 97.5, "volume": 5e6, "timestamp": nxt.timestamp()}
    run.merge_live(B, q)
    assert len(B["c"]) == 6 and B["c"][-1] == 98.0 and B["l"][-1] == 97.5 and B["d"][-1] == nxt.date().isoformat()
    run.merge_live(B, {**q, "price": 97.0, "dayLow": 96.0})          # same session: replace, do not append
    assert len(B["c"]) == 6 and B["c"][-1] == 97.0 and B["l"][-1] == 96.0
    old = (datetime.fromisoformat(last) - timedelta(days=3)).replace(hour=15, tzinfo=run.ET)
    run.merge_live(B, {**q, "price": 50.0, "timestamp": old.timestamp()})   # a stale quote changes nothing
    assert len(B["c"]) == 6 and B["c"][-1] == 97.0


def test_compute_end_to_end_and_quiet_second_run():
    bars, V = run.offline({"QQQ": 615.03, "SPY": 695.46}, 35.43)
    plan = json.loads((HERE / "bottom_watch_plan.json").read_text())
    session = bars["QQQ"]["d"][-1]
    st1, report, push, title, why, imp = run.compute(bars, V, {}, MODEL, plan, session, False, False, "2:00 pm CT Fri Nov 20")
    assert title.startswith("Bottom watch: chance the low is in, QQQ ") and imp and len(why) == 2
    r = st1["readings"]["QQQ"]
    assert r["stage"] == "NEW LOW" and r["peak_date"] == "2026-10-06" and 0.05 < r["prob"] < 0.35
    assert "Chance the low is in" in report and "Your buy-back levels" in report and "Buy step 1" in push
    for text in (report, push, title):
        assert "—" not in text and "–" not in text          # no em or en dashes, ever
    assert len(push.encode()) < 3800                                 # fits one ntfy message
    json.dumps(st1)
    st2, _, _, _, why2, _ = run.compute(bars, V, st1, MODEL, plan, session, False, False, "2:15 pm CT Fri Nov 20")
    assert why2 == [] and st2["pushed"] == st1["pushed"]             # same inputs, no second push
    st3, _, _, _, why3, imp3 = run.compute(bars, V, st2, MODEL, plan, session, True, False, "3:20 pm CT Fri Nov 20")
    assert why3 == ["Daily summary after the close"] and not imp3 and st3["final_session"] == session


def test_state_file_on_disk_is_valid_and_a_bad_one_does_not_stop_the_job(tmp_path=None):
    import tempfile
    assert isinstance(json.loads((HERE / "bottom_watch.json").read_text()), dict) if (HERE / "bottom_watch.json").exists() else True
    d = Path(tempfile.mkdtemp())
    assert run.load_state(d / "missing.json") == {}
    (d / "bad.json").write_text('{"pushed": {}}\\n')              # the hand-edit that broke the 2026-11-20 test run
    assert run.load_state(d / "bad.json") == {}
    (d / "list.json").write_text("[1, 2]")
    assert run.load_state(d / "list.json") == {}
    (d / "ok.json").write_text('{"pushed": {"QQQ": {"prob": 0.2}}}')
    assert run.load_state(d / "ok.json")["pushed"]["QQQ"]["prob"] == 0.2


def test_push_priority_is_quieter_at_night():
    at = lambda h: datetime(2026, 11, 20, h, 30, tzinfo=run.ET)
    assert run.push_priority(True, at(11)) == "high" and run.push_priority(False, at(16)) == "default"
    assert run.push_priority(True, at(23)) == "default" and run.push_priority(False, at(23)) == "low"
    assert run.push_priority(False, at(2)) == "low" and run.push_priority(False, at(7)) == "default"


def test_the_watch_is_chained_to_the_report_not_only_to_github_cron():
    """GitHub's own cron runs hours late in this repo, so the intraday trigger is the Stock Report."""
    wf = (HERE / ".github" / "workflows" / "bottom-watch.yml").read_text()
    report = (HERE / ".github" / "workflows" / "stock-report.yml").read_text()
    name = next(ln.split(":", 1)[1].strip() for ln in report.splitlines() if ln.startswith("name:"))
    assert "workflow_run:" in wf and f'workflows: ["{name}"]' in wf and "branches: [master]" in wf
    assert "workflow_dispatch:" in wf                                # the cron-job.org entry point


def test_a_refit_is_not_a_market_move():
    """After the model changes, the next run must not push 'the chance rose' off the old model's number."""
    bars, V = run.offline({"QQQ": 615.03, "SPY": 695.46}, 35.43)
    plan = json.loads((HERE / "bottom_watch_plan.json").read_text())
    session = bars["QQQ"]["d"][-1]
    st1 = run.compute(bars, V, {}, MODEL, plan, session, False, False, "t")[0]
    other = {**MODEL, "intercept": MODEL["intercept"] + 2.5}          # a re-fit that moves every reading up a band or more
    assert bw.probability(other, {"dist200": -0.1, "retr": 0.0})[0] - bw.probability(MODEL, {"dist200": -0.1, "retr": 0.0})[0] > 0.2
    st2, _, _, _, why, _ = run.compute(bars, V, st1, other, plan, session, False, False, "t")
    assert why == [] and st2["model_id"] != st1["model_id"]
    assert st2["pushed"]["QQQ"]["prob"] == st2["readings"]["QQQ"]["prob"] != st1["pushed"]["QQQ"]["prob"]


def test_reading_matches_the_backtest_row():
    bars, V = _real()
    vix = dict(zip(V["d"], V["c"]))
    r = bw.reading("QQQ", bars["QQQ"], vix, MODEL)
    row = bw.scan("QQQ", bars["QQQ"], vix)[0][-1]
    assert r["prob"] == bw.probability(MODEL, row)[0] and r["low"] == row["runlow"]
    assert [c["label"] for c in r["checks"]] == [c["label"] for c in MODEL["checkpoints"]]


if __name__ == "__main__":
    tests = [(k, v) for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for name, fn in tests:
        fn()
        print("ok", name)
    print(f"{len(tests)} tests passed")
