"""
LEVX side check: the live BBW rules (bbw.py, unchanged) on 8.8 years of 15-minute candles.
The BBW sleeve was adopted on 8 months of Robinhood bars (2026-02-23 -> 10-30). FMP serves
5-minute bars back to 2018, so the same code can be run year by year.
A synthetic 2x fund is built from the underlying's 5-minute bars (daily reset, with drag).
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import bbw
import levx_data as D
import levx_intraday as I


def candles15(X) -> list[list]:
    """15-minute candles [iso, o, h, l, c] from a sessions() dict (78 five-minute slots)."""
    out = []
    O, H, Lo, C = X["O"], X["H"], X["L"], X["C"]
    for d, day in enumerate(X["days"]):
        for k in range(0, 78, 3):
            t = (day + pd.Timedelta(hours=9, minutes=30 + 5 * k)).isoformat()
            out.append([t, float(O[d, k]), float(H[d, k:k + 3].max()), float(Lo[d, k:k + 3].min()), float(C[d, k + 2])])
    return out


def by_year(B, label, cost=0.0):
    T = [x[0] for x in B]
    years = sorted({t[:4] for t in T})
    cells, tot = [], 1.0
    n_tr = 0
    for y in years:
        idx = [i for i, t in enumerate(T) if t[:4] == y]
        r = bbw.backtest(B, None, start=idx[0], end=idx[-1] + 1)
        rets = [t["ret"] - 2 * cost for t in r["list"]]
        tot_y = float(np.prod([1 + x for x in rets]) - 1) if rets else 0.0
        cells.append(f"{y}: {tot_y*100:+.0f}% ({len(rets)} tr, B&H {r['bh']*100:+.0f}%)")
        tot *= 1 + tot_y
        n_tr += len(rets)
    print(f"- **{label}**: " + "; ".join(cells) + f". Compounded {(tot-1)*100:+.0f}% over {len(years)} years, {n_tr} trades.")


if __name__ == "__main__":
    for sym, lev, cost in (("NVDA", 2.0, 0.0003), ("NVDL", None, 0.0003), ("NVDA", None, 0.0001), ("SOXL", None, 0.0002),
                           ("TQQQ", None, 0.00015), ("QQQ", None, 0.0001), ("TSLA", 2.0, 0.0005), ("AMD", 2.0, 0.0010), ("MU", 2.0, 0.0006)):
        X = I.sessions(sym, (sym, lev)) if lev else I.sessions(sym)
        if X is None:
            print(sym, "no data")
            continue
        by_year(candles15(X), f"{sym}{' synthetic 2x' if lev else ''}, {cost*1e4:.1f} bp/side", cost)
