"""Checks for bbw.py. Run: python test_bbw.py

1. The backtest reproduces the NVDL result measured 2026-11-01 (23 trades, +92.9%), which
   matched TrendSpider's published curve over the same window.
2. The LIVE decision path (decide_one, one candle at a time, as the routine runs it) makes
   exactly the same trades as the backtest. This is the test that matters: the live code
   must execute the tested rules, nothing more.
3. 5-minute -> 15-minute aggregation drops incomplete and interpolated bars.
4. The review pauses on a drawdown breach and only PROPOSES retire/rotate/add.
"""

import json
from datetime import datetime, timedelta, timezone

import bbw

B = json.load(open("data/intraday15/NVDL.json"))


def test_backtest_reproduces():
    r = bbw.backtest(B)
    assert r["trades"] == 23, r["trades"]
    assert abs(r["ret"] - 0.9293) < 0.002, r["ret"]
    assert abs(r["win"] - 0.3913) < 0.01, r["win"]


def test_live_path_matches_backtest():
    bt = bbw.backtest(B)["list"]
    strat = {"id": "t", "symbol": "NVDL", "weight": 0.2, "status": "live", "params": {}}
    pos, last, live = None, None, []
    pending = None  # an order decided on candle i fills at candle i+1's open
    for i in range(1, len(B)):
        if pending:
            kind, _ = pending
            if kind == "buy":
                pos = {"entry_candle": B[i][0], "entry_price": B[i][1], "peak_close": B[i][1]}
            else:
                live.append(round(B[i][1] / pos["entry_price"] - 1, 6))
                pos = None
            pending = None
        view = B[:i + 1]
        if pos:
            pos["last_candle"] = last
        d = bbw.decide_one({**strat, "last_candle": last}, pos, view)
        last = view[-1][0]
        if d["action"] == "buy":
            pending = ("buy", i)
        elif d["action"] == "sell":
            pending = ("sell", i)
        elif d["action"] == "hold":
            pos["peak_close"] = d["peak_close"]
    assert [round(t["ret"], 6) for t in bt] == live, (len(bt), len(live))


def test_aggregation():
    t0 = datetime(2026, 10, 30, 19, 30, tzinfo=timezone.utc)
    bars = []
    for k in range(6):
        t = t0 + timedelta(minutes=5 * k)
        bars.append({"begins_at": t.isoformat().replace("+00:00", "Z"), "open_price": 10 + k,
                     "high_price": 11 + k, "low_price": 9 + k, "close_price": 10.5 + k})
    bars.append({"begins_at": "2026-10-30T20:00:00Z", "open_price": 1, "high_price": 1, "low_price": 1,
                 "close_price": 1, "interpolated": True})
    out = bbw.aggregate_15m(bars, now_utc=t0 + timedelta(minutes=29))
    assert len(out) == 1, out  # the 19:45 candle is incomplete at 19:59
    assert out[0][1:] == [10, 13, 9, 12.5], out


def test_review():
    state = {"strategies": [{"id": "a", "symbol": "AAA", "status": "live", "weight": 0.2}],
             "trade_log": [{"strategy": "a", "ret": -0.12}, {"strategy": "a", "ret": -0.11}]}
    v = bbw.review(state, {})
    assert v[0]["verdict"] == "PAUSE", v
    state["trade_log"] = [{"strategy": "a", "ret": r} for r in [-0.01] * 6 + [0.004] * 4]
    v = bbw.review(state, {})
    assert v[0]["verdict"] == "PROPOSE RETIRE", v
    good = {"pass": True, "score": 0.5, "variant": "template",
            "out_of_sample": {"ret": 0.4, "bh": -0.1}}
    v = bbw.review({"strategies": [], "trade_log": []}, {"BBB": good})
    assert v[0]["verdict"] == "PROPOSE ADD", v


def main():
    test_backtest_reproduces()
    test_live_path_matches_backtest()
    test_aggregation()
    test_review()
    print("ok")


if __name__ == "__main__":
    main()
