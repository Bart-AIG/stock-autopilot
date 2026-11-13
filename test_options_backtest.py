#!/usr/bin/env python3
"""Pins the headline numbers of options_backtest.py to the committed dataset. Run: python3 test_options_backtest.py"""

import options_backtest as O


def test_dataset():
    df = O.load()
    assert len(df) == 106 and df.entry.iloc[0] == "2017-12-18" and df.exp.iloc[-1] == "2026-10-16"
    for z in O.ZS:
        assert (df[f"P{z}"] > 0).all()
    # put prices fall as the strike falls, in every cycle
    for a, b in zip(O.ZS, O.ZS[1:]):
        assert (df[f"K{a}"] > df[f"K{b}"]).all() and (df[f"P{a}"] >= df[f"P{b}"]).all()


def test_headline_numbers():
    df = O.load()
    t = O.tables(df, O.Costs(1.0))
    m = t["main"].set_index("structure")
    s = m.loc["put spread, short z=0.5, $5 wide"]
    assert s["n"] == 106 and s["win %"] == 84.9 and abs(s["avg P/L $"] - 14.99) < 0.02 and s["total $"] == 1588
    assert s["t"] == 0.9 and s["worst $"] == -465
    h = t["head"]["5-wide spread, short z=0.5"]
    assert h["losing cycles"] == 16 and h["average loss $"] == -385 and h["average win $"] == 86
    assert h["90% interval (bootstrap)"][0] < 0 < h["90% interval (bootstrap)"][1]
    assert t["head"]["SPY held over the same cycles, CAGR %"] == 14.2
    assert t["head"]["cash-secured at-the-money put, CAGR % (no interest on the cash)"] == 4.5
    sp = t["splits"].set_index("structure")
    assert sp.loc["expiring 2018-2021", "avg P/L $"] > sp.loc["expiring 2022-2026", "avg P/L $"] > 0
    assert sp.loc["VIX under 14 at entry", "avg P/L $"] < 0


def test_costs_and_interpolation():
    df = O.load()
    m1 = O.tables(df, O.Costs(1.0))["main"].set_index("structure")
    m2 = O.tables(df, O.Costs(2.0))["main"].set_index("structure")
    k = "put spread, short z=0.5, $5 wide"
    assert abs(m2.loc[k, "avg P/L $"] - 9.73) < 0.02 and m2.loc[k, "avg P/L $"] < m1.loc[k, "avg P/L $"]
    # the interpolation used for fixed-width spreads, checked on the live chain of 2026-11-13
    import numpy as np
    S, T = 753.29, 35 / 365
    knots = {735: 8.21, 720: 5.61, 700: 3.535}
    actual = {730: 7.21, 725: 6.35, 718: 5.345, 717: 5.215, 715: 4.975, 710: 4.425}
    ks = sorted(knots, reverse=True)
    ivs = [O.iv_put(S, k, T, knots[k]) for k in ks]
    for k, a in actual.items():
        p = O.bs_put(S, k, T, float(np.interp(k, ks[::-1], ivs[::-1])))
        assert abs(p - a) < 0.006, (k, p, a)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("ok")
