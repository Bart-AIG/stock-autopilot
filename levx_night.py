"""
LEVX stage 4: the night effect in liquid leveraged index funds.

Close-to-close return = overnight (close -> next open) + intraday (open -> close). This
script measures where each rule's return is earned, and tests night-only versions:
  N-ALL     hold every night
  N-UP      hold every night the underlying closed above its 200-day SMA
  N-SWING   hold only the nights the house SWING_UNION is "in" (dip or turn-of-month state)
  N-DIP     hold only the nights after an oversold close (RSI2<10 or IBS<0.2) above the 200-day
  SWING cc  the house rule as it runs today (close to close), for comparison
  SWING day only the intraday half of the house rule's held days
Real fund open/close from Yahoo daily bars (synthetic before launch). Cost per side in bp.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L

PERIODS = (("2007-17", "2007-06-01", "2017-12-31"), ("2018-22", "2018-01-01", "2022-12-31"), ("2023-26", "2023-01-01", "2026-12-31"))


def study(und, fund, k, cost_bp, kind="index"):
    u = D.daily(und)
    veh = L.vehicle(und, k, kind, fund)
    cash = L.cash_returns().reindex(u.index).fillna(0.0).to_numpy()
    c, h, l = (u[x].to_numpy() for x in "chl")
    up = L.sig_trend(u, 200)
    sw = L.sig_swing(u, trend=200)
    r2 = L.rsi(c, 2)
    rng = h - l
    ibs = np.where(rng > 0, (c - l) / np.where(rng > 0, rng, 1), 0.5)
    dip = ((r2 < 10) | (ibs < 0.2)) & up
    cost = cost_bp / 1e4
    ones = np.ones(len(u), bool)
    rules = {
        "Buy & hold": ("cc", ones), "N-ALL (every night)": ("ovn", ones), "N-UP (nights above 200d)": ("ovn", up),
        "N-SWING (nights the house rule is in)": ("ovn", sw), "N-DIP (nights after an oversold close, >200d)": ("ovn", dip),
        "N-UP minus strong closes (IBS<=0.8)": ("ovn", up & (ibs <= 0.8)),
        "SWING close-to-close (house rule)": ("cc", sw), "SWING intraday half only": ("intra", sw),
        "DAY-ALL (every session, open->close)": ("intra", ones), "DAY below 200d": ("intra", ~up),
    }
    print(f"\n### {fund} ({k:g}x {und}), {cost_bp:g} bp per side")
    print("| Rule | " + " | ".join(f"{p} CAGR / DD / Sharpe" for p, _, _ in PERIODS) + " | Nights or days held | Avg per held bp |")
    print("|---|" + "---|" * (len(PERIODS) + 2))
    out = {}
    for name, (mode, pos) in rules.items():
        r = L.simulate(pos, veh, cost, mode, cash)
        s = pd.Series(r, index=u.index)
        out[name] = s
        cells = []
        for _, a, b in PERIODS:
            x = s[(s.index >= a) & (s.index <= b)]
            st = L.stats(x.to_numpy())
            cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
        held = np.r_[False, pos[:-1]]
        m = (u.index >= PERIODS[0][1])
        base = veh["rc" if mode == "cc" else "ro" if mode == "ovn" else "ri"].to_numpy()
        hb = np.nanmean(base[m & held]) * 1e4 if (m & held).any() else float("nan")
        print(f"| {name} | " + " | ".join(cells) + f" | {(m & held).sum() / m.sum() * 100:.0f}% | {hb:+.1f} |")
    return out


if __name__ == "__main__":
    res = {}
    res["QLD"] = study("QQQ", "QLD", 2.0, 1.5)
    res["TQQQ"] = study("QQQ", "TQQQ", 3.0, 1.5)
    res["SOXL"] = study("SOXX", "SOXL", 3.0, 2.0)
    res["SPXL"] = study("SPY", "SPXL", 3.0, 2.0)
    res["TECL"] = study("XLK", "TECL", 3.0, 4.0)
    pd.to_pickle(res, D.CACHE / "night.pkl")
