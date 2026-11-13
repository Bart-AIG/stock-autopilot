"""
LEVX stage 6: the NIGHT sleeve on daily open/close data (real SOXL and TQQQ from 2010,
synthetic 3x before), and how it mixes with the live sleeves.

Rule: at the close, hold the fund overnight if its index closed above its N-day SMA; sell at
the next open. Optional volatility target: weight = min(1, target / realised overnight vol).
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L

PERIODS = (("2007-17", "2007-06-01", "2017-12-31"), ("2018-22", "2018-01-01", "2022-12-31"), ("2023-26", "2023-01-01", "2026-12-31"))
LEGS = {"SOXL": ("SOXX", 3.0, 2.0), "TQQQ": ("QQQ", 3.0, 1.5), "QLD": ("QQQ", 2.0, 1.5), "SPXL": ("SPY", 3.0, 2.0)}


def night(fund: str, sma_n: int = 200, target: float | None = None, cost_bp: float | None = None,
          gate: str = "sma") -> pd.Series:
    """Daily net return of the night-only rule for one fund (return booked on the day the
    position is sold)."""
    und, k, c0 = LEGS[fund]
    cost = (c0 if cost_bp is None else cost_bp) / 1e4
    u = D.daily(und)
    veh = L.vehicle(und, k, "index", fund)
    ro = veh["ro"].to_numpy()
    if gate == "sma":
        pos = L.sig_trend(u, sma_n)
    elif gate == "none":
        pos = np.ones(len(u), bool)
    else:
        raise KeyError(gate)
    w = pos.astype(float)
    if target:
        vol = pd.Series(ro).rolling(20, min_periods=10).std().to_numpy() * np.sqrt(252)   # includes today's open: known
        w = w * np.minimum(1.0, target / np.where(vol > 0, vol, np.nan))
        w = np.nan_to_num(w)
    held = np.r_[0.0, w[:-1]]
    r = held * (np.nan_to_num(ro) - 2 * cost)
    return pd.Series(r, index=u.index)


def table(rows: dict[str, pd.Series], periods=PERIODS, extra=None):
    print("| | " + " | ".join(f"{p} CAGR / DD / Sharpe" for p, _, _ in periods) + " | Worst night | Avg weight |")
    print("|---|" + "---|" * (len(periods) + 2))
    for name, s in rows.items():
        cells = []
        for _, a, b in periods:
            x = s[(s.index >= a) & (s.index <= b)]
            st = L.stats(x.to_numpy())
            cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
        x = s[s.index >= periods[0][1]]
        print(f"| {name} | " + " | ".join(cells) + f" | {x.min()*100:.1f}% | {extra.get(name, '') if extra else ''} |")


def yearly(s: pd.Series) -> str:
    y = s.groupby(s.index.year).apply(lambda g: (1 + g).prod() - 1)
    return " ".join(f"{int(k)}:{v*100:+.0f}%" for k, v in y.items())


if __name__ == "__main__":
    rows = {}
    for f in ("SOXL", "TQQQ"):
        rows[f"{f} every night"] = night(f, gate="none")
        for n in (100, 150, 200, 250):
            rows[f"{f} > {n}d"] = night(f, n)
        for t in (0.6, 0.4, 0.3):
            rows[f"{f} > 200d, vol target {t:.0%}"] = night(f, 200, t)
        rows[f"{f} > 200d at 2x cost"] = night(f, 200, cost_bp=LEGS[f][2] * 2)
        rows[f"{f} > 200d at 4x cost"] = night(f, 200, cost_bp=LEGS[f][2] * 4)
    j = pd.concat([night("SOXL"), night("TQQQ")], axis=1, sort=True).fillna(0.0)
    rows["50/50 SOXL + TQQQ > 200d"] = j.mean(axis=1)
    j4 = pd.concat([night("SOXL", 200, 0.4), night("TQQQ", 200, 0.4)], axis=1, sort=True).fillna(0.0)
    rows["50/50, vol target 40% each"] = j4.mean(axis=1)
    table(rows)
    print("\nYear by year:")
    for k in ("SOXL > 200d", "TQQQ > 200d", "50/50 SOXL + TQQQ > 200d", "50/50, vol target 40% each"):
        print(f"- {k}: {yearly(rows[k][rows[k].index >= '2007-06-01'])}")
    s = rows["SOXL > 200d"]; s = s[s.index >= "2010-03-12"]
    print("\nSOXL > 200d, 10 worst nights:", [(str(d.date()), round(v * 100, 1)) for d, v in s.nsmallest(10).items()])
    print("corr SOXL/TQQQ night returns:", round(float(pd.concat([night('SOXL'), night('TQQQ')], axis=1).dropna().corr().iloc[0, 1]), 2))
    pd.to_pickle(rows, D.CACHE / "sleeve_rows.pkl")
