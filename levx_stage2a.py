"""
LEVX stage 2a: anatomy of a dip trade. DISCOVERY DATA ONLY (entries 2011-2022) unless --val.

Every RSI2 / IBS entry on every underlying becomes one row: features known at the entry close,
and the trade's 1x return to the house exit (close > 5-day SMA for RSI2; IBS > 0.8 or 5
sessions for IBS). Buckets show which conditions carry the edge. No leverage, no costs here:
this is about the signal, not the vehicle.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L


def trades_for(sym, df, spy_up, vix, kind):
    c, h, l = (df[k].to_numpy() for k in ("c", "h", "l"))
    n = len(c)
    if n < 300:
        return []
    s200, s50, s5 = L.sma(c, 200), L.sma(c, 50), L.sma(c, 5)
    r2 = L.rsi(c, 2)
    rng = h - l
    ibs = np.where(rng > 0, (c - l) / np.where(rng > 0, rng, 1), 0.5)
    ret = np.r_[0, c[1:] / c[:-1] - 1]
    vol20 = pd.Series(ret).rolling(20).std().to_numpy() * np.sqrt(252)
    su = spy_up.reindex(df.index).ffill().to_numpy()
    vx = vix.reindex(df.index).ffill().to_numpy()
    out = []
    for leg in ("RSI2", "IBS"):
        on, age, e = False, 0, None
        for i in range(260, n):
            if on:
                age += 1
                done = (c[i] > s5[i]) if leg == "RSI2" else (ibs[i] > 0.8 or age >= 5)
                if done:
                    out.append({**e, "exit": df.index[i], "ret": c[i] / e["px"] - 1, "days": age,
                                "mae": min(c[e["i"] + 1:i + 1].min() / e["px"] - 1, 0.0)})
                    on = False
            else:
                trig = (r2[i] < 10) if leg == "RSI2" else (ibs[i] < 0.2)
                if trig and np.isfinite(s200[i]):
                    on, age = True, 0
                    e = {"sym": sym, "kind": kind, "leg": leg, "entry": df.index[i], "i": i, "px": c[i],
                         "above200": bool(c[i] > s200[i]), "above50": bool(c[i] > s50[i]),
                         "d200": c[i] / s200[i] - 1, "mom12": c[i] / c[i - 252] - 1, "mom6": c[i] / c[i - 126] - 1,
                         "mom1": c[i] / c[i - 21] - 1, "r5": c[i] / c[i - 5] - 1, "r1": ret[i], "vol20": vol20[i],
                         "rsi2": r2[i], "ibs": ibs[i], "spy_up": bool(su[i]), "vix": vx[i],
                         "gap": df["o"].to_numpy()[i] / c[i - 1] - 1}
    return out


def bucket(t, col, bins, labels=None):
    g = t.groupby(pd.cut(t[col], bins, labels=labels), observed=True)["ret"]
    return pd.DataFrame({"n": g.size(), "mean%": g.mean() * 100, "med%": g.median() * 100, "win%": g.apply(lambda x: (x > 0).mean() * 100),
                         "t": g.apply(lambda x: x.mean() / (x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 5 and x.std() > 0 else np.nan)}).round(2)


def main(val=False):
    spy = D.daily("SPY")
    spy_up = pd.Series(spy["c"].to_numpy() > L.sma(spy["c"].to_numpy(), 200), index=spy.index)
    vix = D.daily("^VIX", drop_today_if_open=False)["raw"]
    rows = []
    uni = L.universe()
    idx_und = sorted({r["und"] for r in uni if r["kind"] == "index" and r["first"] <= "2016-01-01"})
    for s in idx_und:
        df = D.daily(s)
        if df is not None:
            rows += trades_for(s, df, spy_up, vix, "index")
    for s in L.pit_pool():
        df = D.daily(s)
        if df is not None:
            rows += trades_for(s, df, spy_up, vix, "pool")
    t = pd.DataFrame(rows)
    # cross-sectional momentum rank inside the pool at each entry date (PIT)
    lo, hi = ("2023-01-01", "2099-01-01") if val else ("2011-01-01", "2022-12-31")
    t = t[(t["entry"] >= lo) & (t["entry"] <= hi)].copy()
    t.to_pickle(D.CACHE / ("dips_val.pkl" if val else "dips_disc.pkl"))
    pd.set_option("display.width", 200)
    for kind in ("index", "pool"):
        for leg in ("RSI2", "IBS"):
            x = t[(t.kind == kind) & (t.leg == leg)]
            print(f"\n===== {kind} / {leg}: {len(x)} trades, mean {x.ret.mean()*100:.2f}%, win {(x.ret>0).mean()*100:.0f}%, avg days {x.days.mean():.1f}, worst {x.ret.min()*100:.0f}%")
            print("-- above 200d:"); print(x.groupby("above200")["ret"].agg(["size", "mean", "median"]).assign(mean=lambda d: d["mean"] * 100, median=lambda d: d["median"] * 100).round(2))
            print("-- SPY above 200d:"); print(x.groupby("spy_up")["ret"].agg(["size", "mean"]).assign(mean=lambda d: d["mean"] * 100).round(2))
            print("-- 12m momentum:"); print(bucket(x, "mom12", [-9, -0.2, 0, 0.2, 0.5, 1.0, 99]))
            print("-- 1m momentum:"); print(bucket(x, "mom1", [-9, -0.2, -0.1, -0.05, 0, 0.05, 99]))
            print("-- 5d return:"); print(bucket(x, "r5", [-9, -0.15, -0.10, -0.06, -0.03, 0, 99]))
            print("-- entry-day return:"); print(bucket(x, "r1", [-9, -0.08, -0.05, -0.03, -0.015, 0, 99]))
            print("-- vol20:"); print(bucket(x, "vol20", [0, 0.15, 0.25, 0.35, 0.5, 0.8, 99]))
            print("-- VIX:"); print(bucket(x, "vix", [0, 14, 18, 22, 28, 40, 999]))
            print("-- dist to 200d:"); print(bucket(x, "d200", [-9, -0.2, -0.1, 0, 0.1, 0.2, 0.4, 99]))


if __name__ == "__main__":
    main("--val" in sys.argv)
