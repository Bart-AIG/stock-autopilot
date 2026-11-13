"""Builds data/levx_fixture.json for test_levx.py: the last N sessions of TQQQ and SOXL
5-minute bars with the 200-day inputs, and the returns an INDEPENDENT vectorised
implementation (levx_daynight) gets for the same rules.   python levx_fixture.py [N]"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

import levx
import levx_daynight as DN
import levx_final as F
import levx_intraday as I

N = int(sys.argv[1]) if len(sys.argv) > 1 else 45
out = {"note": "see levx_fixture.py", "funds": {}}
for fund, cfg in levx.FUNDS.items():
    X, f, prior, px = F.dataset(fund)
    days = X["days"]
    c = F.COST[fund]
    # independent implementation over the FULL history, then cut to the last N sessions
    up = DN.trend_flag(cfg["index"], days)
    ov = np.r_[np.nan, X["O"][1:, 0] / X["C"][:-1, -1] - 1]
    vol = pd.Series(ov).rolling(20, min_periods=10).std().shift(1).to_numpy() * np.sqrt(252)
    w = np.nan_to_num(np.minimum(1.0, levx.VOL_TARGET / np.where(vol > 0, vol, np.nan)), nan=0.0) * up
    near = np.r_[np.diff(days.to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
    nxt = np.r_[X["C"][1:, 0], np.nan]
    n_ret = np.r_[0.0, np.where(near & (w > 0), w * (nxt / X["C"][:, 75] - 1 - 2 * c), 0.0)[:-1]]
    rec = {"cost": c, "warm": 25,
           "days": [d.strftime("%Y-%m-%d") for d in days[-N:]], "pc": [round(float(v), 4) for v in X["pc"][-N:]],
           "index_prior_sum": [round(v, 4) for v in prior[-N:]], "index_px": [round(v, 4) for v in px[-N:]],
           "expect_night_w": [round(float(v), 6) for v in w[-N:]],
           "expect_night_ret": [round(float(v), 8) for v in n_ret[-N:]]}
    for k in "OHLC":
        rec[k] = [[round(float(v), 4) for v in row] for row in X[k][-N:]]
    rec["V"] = [[int(v) for v in row] for row in X["V"][-N:]]
    if cfg["day"]:
        dr, dt, dop = DN.day_leg(X, lag=1)
        adj = np.where(dop, (1 + dr) * X["C"][:, 75] / X["C"][:, -1] - 1, dr)
        rec["expect_day_gross"] = [round(float(v), 8) for v in adj[-N:]]
        rec["expect_day_trades"] = [int(v) for v in dt[-N:]]
    out["funds"][fund] = rec
json.dump(out, open("data/levx_fixture.json", "w"), separators=(",", ":"))
print("wrote data/levx_fixture.json", {f: len(r["days"]) for f, r in out["funds"].items()})
