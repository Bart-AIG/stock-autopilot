"""Checks for levx.py. Run: python test_levx.py

1. The backtest (levx.simulate) reproduces, on real 5-minute bars, the returns an independent
   vectorised implementation of the same rules produced (stored in data/levx_fixture.json).
2. The LIVE decision path (levx.decide, called the way the routine calls it at 09:31,
   10:01 ... 15:31 and 15:46 ET) reaches the same positions as the backtest. This is the
   test that matters: the live code must execute the tested rules, nothing more.
3. Phases, the stale-inputs guard, the fresh-entry rule, the missing-bars guard, the
   scorecard and pause rule, and the sizing formulas.
"""

import json
import math
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import levx

FX = json.load(open("data/levx_fixture.json"))["funds"]
ET = ZoneInfo("America/New_York")
SLOTS = [f"{(570 + 5 * i) // 60:02d}:{(570 + 5 * i) % 60:02d}" for i in range(78)]


def _fund(name):
    r = FX[name]
    days = [datetime.fromisoformat(d) for d in r["days"]]
    return r, {"days": days, "pc": r["pc"], "O": r["O"], "H": r["H"], "L": r["L"], "C": r["C"], "V": r["V"]}


def test_backtest_reproduces():
    for name, cfg in levx.FUNDS.items():
        r, f = _fund(name)
        rows = levx.simulate(f, r["index_prior_sum"], r["index_px"], cfg["day"], r["cost"], lag=1)
        w0 = r["warm"]
        for d in range(w0, len(rows)):
            assert abs(rows[d]["night_ret"] - r["expect_night_ret"][d]) < 1e-7, (name, r["days"][d], rows[d]["night_ret"], r["expect_night_ret"][d])
            if cfg["day"]:
                exp = r["expect_day_gross"][d] - 2 * r["cost"] * r["expect_day_trades"][d]
                assert rows[d]["day_trades"] == r["expect_day_trades"][d], (name, r["days"][d])
                assert abs(rows[d]["day_ret"] - exp) < 2e-4, (name, r["days"][d], rows[d]["day_ret"], exp)
        held = sum(1 for d in range(w0, len(rows)) if rows[d]["night_ret"] != 0)
        assert held >= 3, (name, "fixture holds too few nights to be a test", held)


def _rh_bars(day: str, rec: dict, d: int, upto_slot: int) -> list[dict]:
    """Fixture bars for one day as the Robinhood connector returns them."""
    out = []
    for i in range(upto_slot + 1):
        hh, mm = int(SLOTS[i][:2]), int(SLOTS[i][3:])
        t = datetime.fromisoformat(day).replace(hour=hh, minute=mm, tzinfo=ET)
        out.append({"begins_at": t.astimezone(ZoneInfo("UTC")).isoformat().replace("+00:00", "Z"),
                    "open_price": str(rec["O"][d][i]), "high_price": str(rec["H"][d][i]),
                    "low_price": str(rec["L"][d][i]), "close_price": str(rec["C"][d][i]),
                    "volume": rec["V"][d][i], "interpolated": False})
    return out


def test_live_path_matches_backtest():
    """Walk the routine's clock through every fixture day and compare with simulate()."""
    recs = {n: _fund(n) for n in levx.FUNDS}
    sims = {n: levx.simulate(recs[n][1], recs[n][0]["index_prior_sum"], recs[n][0]["index_px"], levx.FUNDS[n]["day"],
                             recs[n][0]["cost"], lag=1) for n in levx.FUNDS}
    T = FX["TQQQ"]
    n_days = len(T["days"])
    checked_night = checked_day = 0
    for d in range(T["warm"], n_days - 1):
        day = T["days"][d]
        if day in levx.EARLY_CLOSE:
            continue
        # the morning inputs the Action would have built before this session
        inputs = {"for_session": day, "funds": {}}
        for n, cfg in levx.FUNDS.items():
            r = FX[n]
            overnight = [r["O"][k][0] / r["C"][k - 1][77] - 1 for k in range(1, d)]
            fi = {"index": cfg["index"], "index_prior_sum": r["index_prior_sum"][d], "prev_close": r["pc"][d],
                  "overnight": overnight[-levx.VOL_N:]}
            if cfg["day"]:
                hist = [{"open": r["O"][k][0], "closes": {t: r["C"][k][SLOTS.index(t) - 1] for t in levx.CHECKS}}
                        for k in range(max(0, d - levx.SIGMA_N), d)]
                fi["sigma"] = levx.sigma_profile(hist)
            inputs["funds"][n] = fi
        # 09:31: sell-only
        now = datetime.fromisoformat(day).replace(hour=9, minute=31, tzinfo=ET)
        out = levx.decide(inputs, {"quotes": {}, "bars5": {}}, now)
        assert out["phase"] == "morning" and all(t["frac"] == 0 for t in out["targets"].values())
        # DAY checks: the run fires one minute after each :00/:30 bar closes
        st_full = levx.day_replay([(SLOTS[i], T["O"][d][i], T["H"][d][i], T["L"][d][i], T["C"][d][i], T["V"][d][i])
                                   for i in range(78)], T["pc"][d], inputs["funds"]["TQQQ"]["sigma"])
        want = {}
        for t, what, _ in st_full["log"]:
            want[t] = what
        state = False
        for t in levx.CHECKS:
            hh, mm = int(t[:2]), int(t[3:])
            now = datetime.fromisoformat(day).replace(hour=hh, minute=mm, tzinfo=ET) + timedelta(minutes=1)
            bars = _rh_bars(day, T, d, SLOTS.index(t) - 1)
            out = levx.decide(inputs, {"quotes": {}, "bars5": {"TQQQ": bars}}, now)
            assert out["phase"] == "day"
            tg = out["targets"]["TQQQ"]
            if tg["frac"] > 0 and not state:
                assert want.get(t) == "buy" and tg["buy_ok"], (day, t, tg, want)
                state = True
            elif tg["frac"] == 0 and state:
                assert want.get(t) in ("sell", None) and any(w == "sell" for tt, w in want.items() if tt <= t), (day, t)
                state = False
            assert out["targets"]["SOXL"]["frac"] == 0
            checked_day += 1
        assert state == st_full["in"], (day, state, st_full["in"])
        # 15:46: the NIGHT decision, with the index price the backtest used
        now = datetime.fromisoformat(day).replace(hour=15, minute=46, tzinfo=ET)
        quotes = {levx.FUNDS[n]["index"]: FX[n]["index_px"][d] for n in levx.FUNDS}
        out = levx.decide(inputs, {"quotes": quotes, "bars5": {}}, now)
        assert out["phase"] == "night"
        for n, cfg in levx.FUNDS.items():
            w_live = out["targets"][n]["frac"] / cfg["night_share"]
            w_bt = sims[n][d + 1]["night_w"]            # the weight simulate carried into the next morning
            assert abs(w_live - w_bt) < 1e-3, (day, n, w_live, w_bt)
            assert abs(w_live - FX[n]["expect_night_w"][d]) < 1e-3, (day, n, w_live, FX[n]["expect_night_w"][d])
            checked_night += 1
    assert checked_night > 20 and checked_day > 200


def test_phases_and_guards():
    def at(day, hm):
        return datetime.fromisoformat(day).replace(hour=int(hm[:2]), minute=int(hm[3:]), tzinfo=ET)
    assert levx.phase_of(at("2026-11-12", "09:29")) == "closed"
    assert levx.phase_of(at("2026-11-12", "09:31")) == "morning"
    assert levx.phase_of(at("2026-11-12", "10:01")) == "day"
    assert levx.phase_of(at("2026-11-12", "15:31")) == "day"
    assert levx.phase_of(at("2026-11-12", "15:46")) == "night"
    assert levx.phase_of(at("2026-11-12", "16:01")) == "closed"
    assert levx.phase_of(at("2026-11-14", "10:01")) == "closed"          # Saturday
    assert levx.phase_of(at("2026-11-27", "10:01")) == "morning"         # early close: sell-only
    assert levx.phase_of(at("2026-11-27", "13:05")) == "closed"
    # stale inputs: no entries
    inputs = {"for_session": "2026-11-11", "funds": {}}
    out = levx.decide(inputs, {"quotes": {"QQQ": 700, "SOXX": 200}}, at("2026-11-12", "15:46"))
    assert out["stale_inputs"] and all(t["frac"] == 0 and not t["buy_ok"] for t in out["targets"].values())


def test_fresh_entry_rule():
    """A DAY entry is only taken within FRESH_MIN minutes of its signal bar; a run that arrives
    late keeps the state but may not open."""
    T = FX["TQQQ"]
    for d in range(T["warm"], len(T["days"]) - 1):
        hist = [{"open": T["O"][k][0], "closes": {t: T["C"][k][SLOTS.index(t) - 1] for t in levx.CHECKS}}
                for k in range(d - levx.SIGMA_N, d)]
        sig = levx.sigma_profile(hist)
        st = levx.day_replay([(SLOTS[i], T["O"][d][i], T["H"][d][i], T["L"][d][i], T["C"][d][i], T["V"][d][i])
                              for i in range(78)], T["pc"][d], sig)
        buys = [t for t, w, _ in st["log"] if w == "buy"]
        if not buys or T["days"][d] in levx.EARLY_CLOSE:
            continue
        t = buys[0]
        inputs = {"for_session": T["days"][d], "funds": {"TQQQ": {"prev_close": T["pc"][d], "sigma": sig},
                                                           "SOXL": {"prev_close": 1.0}}}
        base = datetime.fromisoformat(T["days"][d]).replace(hour=int(t[:2]), minute=int(t[3:]), tzinfo=ET)
        bars = _rh_bars(T["days"][d], T, d, SLOTS.index(t) - 1)
        on_time = levx.decide(inputs, {"bars5": {"TQQQ": bars}}, base + timedelta(minutes=2))
        late = levx.decide(inputs, {"bars5": {"TQQQ": bars}}, base + timedelta(minutes=20))
        assert on_time["targets"]["TQQQ"] == {"frac": levx.DAY_SHARE, "buy_ok": True}
        assert late["targets"]["TQQQ"]["frac"] == levx.DAY_SHARE and late["targets"]["TQQQ"]["buy_ok"] is False
        return
    raise AssertionError("no DAY entry in the fixture")


def test_missing_bars_hold():
    """A hole in the 5-minute feed is not a signal: the target is None (leave the position
    alone) and nothing may be opened."""
    T = FX["TQQQ"]
    d = T["warm"] + 1
    day = T["days"][d]
    while day in levx.EARLY_CLOSE:
        d += 1
        day = T["days"][d]
    hist = [{"open": T["O"][k][0], "closes": {t: T["C"][k][SLOTS.index(t) - 1] for t in levx.CHECKS}}
            for k in range(d - levx.SIGMA_N, d)]
    inputs = {"for_session": day, "funds": {"TQQQ": {"prev_close": T["pc"][d], "sigma": levx.sigma_profile(hist)},
                                            "SOXL": {"prev_close": 1.0}}}
    now = datetime.fromisoformat(day).replace(hour=11, minute=1, tzinfo=ET)
    full = _rh_bars(day, T, d, SLOTS.index("11:00") - 1)
    ok = levx.decide(inputs, {"bars5": {"TQQQ": full}}, now)
    assert ok["targets"]["TQQQ"]["frac"] is not None
    for bad in ([], full[1:], full[:-1], [dict(b, interpolated=True) for b in full]):
        out = levx.decide(inputs, {"bars5": {"TQQQ": bad}}, now)
        assert out["targets"]["TQQQ"] == {"frac": None, "buy_ok": False}, bad[:1]
        assert "error" in out["detail"]["TQQQ"]


def test_scorecard_and_pause():
    def row(day, leg, w, ret, **kw):
        return {"fund": "TQQQ", "leg": leg, "out": f"{day}T14:35:00Z", "weight": w, "ret": ret, **kw}
    st = {"trade_log": [row("2026-11-16", "night", 0.5, 0.02, slip_in_bp=1.0, slip_out_bp=2.0, paper=False),
                        row("2026-11-16", "day", 1.0, -0.01, paper=False),
                        row("2026-11-17", "night", 0.25, -0.04, late=True, paper=True)]}
    sc = levx.scorecard(st)
    want = (1 + 0.5 * 0.02) * (1 - 0.01) * (1 + 0.25 * -0.04) - 1
    assert abs(sc["return"] - want) < 1e-5 and sc["days"] == 2
    assert sc["legs"]["night"]["trades"] == 2 and sc["legs"]["night"]["wins"] == 1 and sc["legs"]["night"]["late"] == 1
    assert sc["legs"]["day"]["avg_ret_bp"] == -100.0
    assert sc["round_trip_cost_bp"] == {"TQQQ": {"n": 1, "avg": 3.0, "backtest": 3.0, "check": "too_few"}}
    for avg, want_chk in ((5.9, "ok"), (6.1, "notify"), (12.1, "propose_pause")):
        log = [row(f"2026-11-{2 + i:02d}", "night", 0.5, 0.0, slip_in_bp=avg / 2, slip_out_bp=avg / 2) for i in range(20)]
        assert levx.scorecard({"trade_log": log})["round_trip_cost_bp"]["TQQQ"]["check"] == want_chk, (avg, want_chk)
        assert levx.scorecard({"trade_log": log[:19]})["round_trip_cost_bp"]["TQQQ"]["check"] == "too_few"
    assert sc["check"] == "ok"
    assert levx.scorecard(st, paper=True)["days"] == 1 and levx.scorecard(st, paper=False)["days"] == 1
    assert levx.scorecard({"trade_log": []})["return"] == 0.0
    # drawdown from the sleeve's own high: notify at -30%, pause at -40%
    up = [row("2026-11-02", "day", 1.0, 0.10)]
    assert levx.scorecard({"trade_log": up + [row("2026-11-03", "day", 1.0, -0.29)]})["check"] == "ok"
    assert levx.scorecard({"trade_log": up + [row("2026-11-03", "day", 1.0, -0.31)]})["check"] == "notify"
    assert levx.scorecard({"trade_log": up + [row("2026-11-03", "day", 1.0, -0.41)]})["check"] == "pause"
    assert levx.mode_of({"status": "paused"}) == "paused"
    assert levx.mode_of({"status": "active"}) == ("live" if levx.W_LEVX > 0 else "paper")


def test_exit_at_open_option():
    """exit_open sells the night position at the session's first print (the queued sell)."""
    r, f = _fund("SOXL")
    a = levx.simulate(f, r["index_prior_sum"], r["index_px"], False, r["cost"])
    b = levx.simulate(f, r["index_prior_sum"], r["index_px"], False, r["cost"], exit_open=True)
    n = 0
    for d in range(r["warm"], len(a)):
        w = a[d]["night_w"]
        assert b[d]["night_w"] == w
        if w > 0:
            entry = f["C"][d - 1][75]
            assert abs(b[d]["night_ret"] - w * (f["O"][d][0] / entry - 1 - 2 * r["cost"])) < 1e-12
            assert abs(a[d]["night_ret"] - w * (f["C"][d][0] / entry - 1 - 2 * r["cost"])) < 1e-12
            n += 1
    assert n >= 3


def test_sizing():
    o = [0.01, -0.01] * 10                          # daily sd ~1.03% -> ~16% a year
    nw = levx.night_weight(101.0, 100.0 * 199, o)
    assert nw["gate"] and nw["weight"] == 1.0
    nw = levx.night_weight(99.0, 100.0 * 199, o)
    assert not nw["gate"] and nw["weight"] == 0.0
    big = [0.05, -0.05] * 10                        # ~81% a year -> weight ~0.49
    nw = levx.night_weight(101.0, 100.0 * 199, big)
    assert abs(nw["weight"] - levx.VOL_TARGET / nw["vol"]) < 1e-12 and 0.45 < nw["weight"] < 0.55
    assert levx.night_weight(101.0, 100.0 * 199, [0.01] * 5)["weight"] == 0.0      # too little history: no position
    assert levx.W_LEVX == 0.0 or 0 < levx.W_LEVX <= 0.5
    assert abs(levx.sleeve_usd(1000.0) - 1000.0 * 0.95 * levx.W_LEVX) < 1e-9
    assert math.isclose(sum(c["night_share"] for c in levx.FUNDS.values()), 1.0)


def test_weights_fit_the_base():
    """LEVX is funded by shrinking another sleeve in the same commit. If the live weights sum
    past 100% of the base the sleeves would fight over cash, so this must fail first."""
    import sleeves
    bw = json.load(open("bbw_state.json"))
    bbw_w = sum(float(s.get("weight", 0)) for s in bw.get("strategies", []) if s.get("status") in ("live", "paused"))
    total = sleeves.W_SWING_Q + sleeves.W_SWING_M + bbw_w + levx.W_LEVX
    assert total <= 1.0 + 1e-9, f"sleeve weights sum to {total:.2f} of the base"


def main():
    test_weights_fit_the_base()
    test_backtest_reproduces()
    test_live_path_matches_backtest()
    test_phases_and_guards()
    test_fresh_entry_rule()
    test_missing_bars_hold()
    test_scorecard_and_pause()
    test_exit_at_open_option()
    test_sizing()
    print("ok")


if __name__ == "__main__":
    main()
