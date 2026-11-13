"""
LEVX final backtest: the live rules (levx.py) replayed on real 5-minute bars, 2018 -> today.
levx.simulate is the source of truth; an independent vectorised implementation
(levx_daynight) is run beside it as a cross-check.   python levx_final.py
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx
import levx_data as D
import levx_daynight as DN
import levx_intraday as I
import levx_lab as L

COST = {"TQQQ": 0.00015, "SOXL": 0.0002}


def dataset(fund: str):
    X = I.sessions(fund)
    cfg = levx.FUNDS[fund]
    days = X["days"]
    u = D.daily(cfg["index"], drop_today_if_open=False)
    Xu = I.sessions(cfg["index"])
    px = pd.Series(Xu["C"][:, 75], index=Xu["days"]).reindex(days)
    px = px.fillna(u["raw"].reindex(days))
    prior = u["raw"].rolling(levx.SMA_N - 1).sum().shift(1).reindex(days)
    f = {"days": list(days), "pc": X["pc"].tolist(), **{k: X[k].tolist() for k in "OHLCV"}}
    return X, f, [None if not np.isfinite(v) else float(v) for v in prior], [None if not np.isfinite(v) else float(v) for v in px]


_DATA: dict = {}


def run(cost_mult: float = 1.0, lag: int = 1, exit_open: bool = False, extra_cost: float = 0.0, b_exit: int = 0):
    out = {}
    for fund, cfg in levx.FUNDS.items():
        if fund not in _DATA:
            _DATA[fund] = dataset(fund)
        X, f, prior, px = _DATA[fund]
        rows = levx.simulate(f, prior, px, cfg["day"], COST[fund] * cost_mult + extra_cost, lag=lag,
                             exit_open=exit_open, b_exit=b_exit)
        out[fund] = pd.DataFrame(rows).set_index("day")
    return out


def sleeve(res: dict) -> pd.Series:
    j = pd.concat({f: r for f, r in res.items()}, axis=1, sort=True).fillna(0.0)
    night = sum(levx.FUNDS[f]["night_share"] * j[(f, "night_ret")] for f in levx.FUNDS)
    day = sum(j[(f, "day_ret")] for f in levx.FUNDS)
    return (1 + night) * (1 + day) - 1


def cross_check(res):
    """Independent vectorised version of the same spec."""
    print("cross-check against the vectorised implementation (max abs daily difference):")
    for fund, cfg in levx.FUNDS.items():
        X = I.sessions(fund)
        days = X["days"]
        c = COST[fund]
        up_sma = DN.trend_flag(cfg["index"], days)
        ov = np.r_[np.nan, X["O"][1:, 0] / X["C"][:-1, -1] - 1]
        vol = pd.Series(ov).rolling(20, min_periods=10).std().shift(1).to_numpy() * np.sqrt(252)
        w = np.nan_to_num(np.minimum(1.0, 0.40 / np.where(vol > 0, vol, np.nan)), nan=0.0) * up_sma
        near = np.r_[np.diff(days.to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
        nxt = np.r_[X["C"][1:, 0], np.nan]
        n_ret = np.where(near & (w > 0), w * (nxt / X["C"][:, 75] - 1 - 2 * c), 0.0)
        n_ret = np.r_[0.0, n_ret[:-1]]
        mine = res[fund]["night_ret"].to_numpy()
        print(f"  {fund} night: {np.nanmax(np.abs(mine - np.nan_to_num(n_ret))):.2e}  (nights held {int((mine != 0).sum())} vs {int((n_ret != 0).sum())})")
        if cfg["day"]:
            dr, dt, dop = DN.day_leg(X, lag=1)
            adj = np.where(dop, (1 + dr) * X["C"][:, 75] / X["C"][:, -1] - 1, dr)     # flatten at 15:50, not the close
            d_ret = adj - 2 * c * dt
            mine = res[fund]["day_ret"].to_numpy()
            k = 20
            print(f"  {fund} day: {np.max(np.abs(mine[k:] - d_ret[k:])):.2e}  (trades {int(res[fund]['day_trades'].sum())} vs {int(dt.sum())})")


if __name__ == "__main__":
    res = run()
    cross_check(res)
    s = sleeve(res)
    s.to_pickle(D.CACHE / "levx_final.pkl")
    per = (("2018-22", "2018-01-01", "2022-12-31"), ("2023-26", "2023-01-01", "2026-12-31"), ("2018-26", "2018-01-01", "2026-12-31"))
    print("\n| LEVX (live rules, real 5-minute bars) | " + " | ".join(p for p, _, _ in per) + " |\n|---|---|---|---|")

    def line(label, x):
        cells = []
        for _, a, b in per:
            st = L.stats(x[(x.index >= a) & (x.index <= b)].to_numpy())
            cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
        print(f"| {label} | " + " | ".join(cells) + " |")

    line("Base: TQQQ night + day, SOXL night", s)
    j = pd.concat(res, axis=1, sort=True).fillna(0.0)
    line("NIGHT legs only", 0.5 * j[("TQQQ", "night_ret")] + 0.5 * j[("SOXL", "night_ret")])
    line("TQQQ night only (its half)", 0.5 * j[("TQQQ", "night_ret")])
    line("SOXL night only (its half)", 0.5 * j[("SOXL", "night_ret")])
    line("DAY leg only", j[("TQQQ", "day_ret")])
    for m in (2, 3):
        line(f"Base at {m}x costs", sleeve(run(cost_mult=m)))
    print("\nyear by year: " + " ".join(f"{y}:{((1+g).prod()-1)*100:+.0f}%" for y, g in s.groupby(s.index.year)))
    nights = (j[("TQQQ", "night_w")] > 0).mean(), (j[("SOXL", "night_w")] > 0).mean()
    print(f"nights held: TQQQ {nights[0]*100:.0f}%, SOXL {nights[1]*100:.0f}%; average night weight when held: "
          f"TQQQ {j[('TQQQ','night_w')][j[('TQQQ','night_w')]>0].mean():.2f}, SOXL {j[('SOXL','night_w')][j[('SOXL','night_w')]>0].mean():.2f}; "
          f"DAY round trips per year {j[('TQQQ','day_trades')].sum() / (len(j)/252):.0f}")
