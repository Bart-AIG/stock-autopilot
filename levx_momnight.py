"""
LEVX stage 5: momentum names at night. The monthly top-N 12-month-momentum names from the
end-2018 S&P 100 + Nasdaq-100 pool (the SWING_M pick list), held three ways:
  NIGHT   close -> next open only        DAY   open -> close only        CC   close to close
with 1x shares or a synthetic 2x fund, net of a per-side cost. 2019+ is the honest window (the
pool was fixed at end-2018); earlier years reuse that list and are shown for the split only.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx_book as B
import levx_data as D
import levx_lab as L
from levx_stage2b import top_n_monthly

PERIODS = (("2007-18*", "2007-06-01", "2018-12-31"), ("2019-22", "2019-01-01", "2022-12-31"), ("2023-26", "2023-01-01", "2026-12-31"))


def series(P, flag, mode, cost):
    held = np.vstack([np.zeros((1, P.n), bool), flag[:-1]])
    r = {"ovn": P.ro, "intra": P.ri, "cc": P.rc}[mode]
    n = held.sum(axis=1)
    gross = np.where(n > 0, (r * held).sum(axis=1) / np.maximum(n, 1), 0.0)
    if mode == "cc":
        # cost only on changes of membership
        chg = (flag != np.vstack([np.zeros((1, P.n), bool), flag[:-1]])).sum(axis=1)
        fee = np.r_[0, chg[:-1]] * cost / np.maximum(n, 1)
    else:
        fee = np.where(n > 0, 2 * cost, 0.0)
    return pd.Series(gross - fee, index=P.cal)


def row(label, s):
    cells = []
    for _, a, b in PERIODS:
        x = s[(s.index >= a) & (s.index <= b)]
        st = L.stats(x.to_numpy())
        cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
    print(f"| {label} | " + " | ".join(cells) + " |")


def main():
    names = L.pit_pool()
    out = {}
    for lev, kind, costs in ((1.0, "spot", (0.0001, 0.0002)), (2.0, "stock", (0.0003, 0.0006, 0.0012))):
        P = B.Panel([{"und": s, "lev": lev, "kind": kind, "fund": None} for s in names], start="2006-06-01")
        mom = P.feature("mom12")
        up = np.nan_to_num(P.feature("above200")) > 0.5
        sw = P.signal(L.sig_swing, trend=200)
        print(f"\n### {lev:g}x, pool of {P.n} names")
        print("| Book | " + " | ".join(f"{p} CAGR / DD / Sharpe" for p, _, _ in PERIODS) + " |")
        print("|---|" + "---|" * len(PERIODS))
        for n in (5, 10, 20):
            top = top_n_monthly(P, mom, n)
            for c in costs:
                s = series(P, top, "ovn", c)
                out[(lev, n, "night", c)] = s
                row(f"top-{n} NIGHT, {c*1e4:.0f} bp/side", s)
            row(f"top-{n} NIGHT only above 200d, {costs[0]*1e4:.0f} bp/side", series(P, top & up, "ovn", costs[0]))
            row(f"top-{n} DAY (open->close), {costs[0]*1e4:.0f} bp/side", series(P, top, "intra", costs[0]))
            row(f"top-{n} held close-to-close", series(P, top, "cc", costs[0]))
            row(f"top-{n} x house swing, close-to-close (SWING_M at {lev:g}x)", series(P, top & sw, "cc", costs[0]))
            row(f"top-{n} x house swing, NIGHTS only, {costs[0]*1e4:.0f} bp/side", series(P, top & sw, "ovn", costs[0]))
        allp = P.elig
        row(f"ALL names NIGHT, {costs[0]*1e4:.0f} bp/side", series(P, allp, "ovn", costs[0]))
        volr = P.feature("vol60")
        row(f"top-10 by 60d volatility NIGHT, {costs[0]*1e4:.0f} bp/side", series(P, top_n_monthly(P, volr, 10), "ovn", costs[0]))
        row(f"top-10 by 60d volatility DAY", series(P, top_n_monthly(P, volr, 10), "intra", costs[0]))
        row(f"bottom-10 momentum NIGHT, {costs[0]*1e4:.0f} bp/side", series(P, top_n_monthly(P, -mom, 10), "ovn", costs[0]))
    pd.to_pickle(out, D.CACHE / "momnight.pkl")


if __name__ == "__main__":
    main()
