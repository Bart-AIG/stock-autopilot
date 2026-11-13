"""
LEVX stage 7: NIGHT and DAY legs on the same capital, from real 5-minute bars (2018 -> today).

NIGHT  buy at 15:50 if the index is above its 200-day SMA (today's 15:50 price counted in),
       sell at the next open.
DAY    noise-area breakout, long only (Zarattini, Aziz & Barbon 2024): at each check, buy if
       the fund is above max(open, prior close) x (1 + its average move for that time of day
       over the last `lookback` sessions); sell when it falls back below max(that band, VWAP);
       flat at the close unless NIGHT keeps it.
`lag=1` fills every DAY order one 5-minute bar after the signal bar (the routine fires one
minute after the bar closes; the true fill sits between lag 0 and lag 1).
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

import levx_data as D
import levx_intraday as I
import levx_lab as L

P1, P2 = ("2018-01-01", "2022-12-31"), ("2023-01-01", "2026-12-31")


def trend_flag(und: str, days: pd.DatetimeIndex, n: int = 200) -> np.ndarray:
    """Index above its n-day SMA using the price at 15:50 on the day (5-minute bars)."""
    u = D.daily(und, drop_today_if_open=False)
    Xu = I.sessions(und)
    p1550 = pd.Series(Xu["C"][:, I.B1550], index=Xu["days"])
    prior = u["raw"].rolling(n - 1).sum().shift(1)
    sma = (prior + p1550.reindex(u.index).fillna(u["raw"])) / n
    px = p1550.reindex(u.index).fillna(u["raw"])
    return (px > sma).reindex(days).fillna(False).to_numpy(bool)


def day_leg(X, lookback=14, step=6, lag=0, first=5, last=71, gate=None, rule="band"):
    """Returns per-day gross return, round trips, and whether the leg is still long at 15:50.
    rule "band" (live): long while the check's close is above the band.
    rule "published": long while it is above max(band, session VWAP) (Zarattini et al.).
    rule "as_first_run": exit below max(band, VWAP) but re-enter above the band in the same
    check, i.e. the band rule plus round trips that never changed the position. This is how
    the first tests were coded; kept so they can be reproduced."""
    O, C, H, Lo, V = X["O"], X["C"], X["H"], X["L"], X["V"]
    n = len(O)
    mv = np.abs(C / O[:, :1] - 1)
    sig = pd.DataFrame(mv).rolling(lookback, min_periods=max(5, int(lookback * 0.7))).mean().shift(1).to_numpy()
    tp = (H + Lo + C) / 3
    cv = np.cumsum(V, axis=1)
    vw = np.where(cv > 0, np.cumsum(tp * V, axis=1) / np.maximum(cv, 1e-9), C)
    checks = list(range(first, last + 1, step))
    ret, tr, open_at_close = np.zeros(n), np.zeros(n), np.zeros(n, bool)
    exit_px = np.full(n, np.nan)
    for d in range(n):
        if not np.isfinite(sig[d, checks[0]]) or (gate is not None and not gate[d]):
            continue
        ref = max(O[d, 0], X["pc"][d])
        pos, entry, acc, k = False, 0.0, 1.0, 0
        for b in checks:
            U, c = ref * (1 + sig[d, b]), C[d, b]
            fill = C[d, min(b + lag, 77)]
            if rule == "as_first_run":
                if pos and c < max(U, vw[d, b]):
                    acc *= fill / entry
                    pos = False
                if not pos and c > U:
                    pos, entry, k = True, fill, k + 1
                continue
            want = c > U if rule == "band" else c > max(U, vw[d, b])
            if pos and not want:
                acc *= fill / entry
                pos = False
            elif not pos and want:
                pos, entry, k = True, fill, k + 1
        if pos:
            acc *= C[d, -1] / entry
            open_at_close[d] = True
        ret[d], tr[d] = acc - 1, k
    return ret, tr, open_at_close


def night_leg(X, up, day_open=None, bar=I.B1550):
    """Gross overnight return booked on the buy day; entry at 15:50, or at the close with no
    entry cost when the DAY leg is already long (day_open)."""
    nxt = np.r_[X["O"][1:, 0], np.nan]
    near = np.r_[np.diff(X["days"].to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
    entry = X["C"][:, bar].copy()
    sides = np.full(len(entry), 2.0)
    if day_open is not None:
        entry = np.where(day_open, X["C"][:, -1], entry)
        sides = np.where(day_open, 0.0, 2.0)       # the DAY exit and NIGHT entry cancel: 2 sides saved
    take = up & near & np.isfinite(nxt)
    return np.where(take, nxt / entry - 1, 0.0), np.where(take, sides, 0.0), take


def stats_line(label, r, days):
    cells = []
    for a, b in (P1, P2):
        m = (days >= a) & (days <= b)
        st = L.stats(r[m])
        cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
    print(f"| {label} | " + " | ".join(cells) + " |")


def run(fund, und, cost_bp):
    X = I.sessions(fund)
    days = X["days"]
    up = trend_flag(und, days)
    c = cost_bp / 1e4
    print(f"\n### {fund}: {len(days)} sessions, {cost_bp:g} bp/side")
    print("| Leg | 2018-22 CAGR / DD / Sharpe | 2023-26 CAGR / DD / Sharpe |")
    print("|---|---|---|")
    out = {}
    nr, ns, _ = night_leg(X, up)
    night = nr - ns * c
    stats_line("NIGHT (15:50 -> open, index > 200d)", night, days)
    for lab, kw in (("DAY base (14d, 30-min checks, no lag)", {}), ("DAY, fill one bar late", {"lag": 1}),
                    ("DAY, 15-min checks", {"step": 3, "first": 5}), ("DAY, 60-min checks", {"step": 12, "first": 5}),
                    ("DAY, 10-day lookback", {"lookback": 10}), ("DAY, 20-day lookback", {"lookback": 20}),
                    ("DAY, only when index > 200d", {"gate": up_prev(up)}), ("DAY, only when index < 200d", {"gate": ~up_prev(up)}),
                    ("DAY, fill one bar late, 2x cost", {"lag": 1, "_c": 2})):
        cc = c * kw.pop("_c", 1)
        dr, dt, dop = day_leg(X, **kw)
        stats_line(lab, dr - 2 * cc * dt, days)
        if lab.startswith("DAY, fill one bar late") and "2x" not in lab:
            out["day"], out["dop"], out["dt"] = dr - 2 * c * dt, dop, dt
    dr, dt, dop = day_leg(X, lag=1)
    nr2, ns2, _ = night_leg(X, up, dop)
    # combined: DAY exit cost is waived when NIGHT keeps the position (already netted in ns2 = 0 sides)
    saved = np.where(dop & (ns2 == 0) & up, c, 0.0)       # the DAY leg charged its exit side; give it back
    comb = (1 + dr - 2 * c * dt + saved) * (1 + nr2 - ns2 * c) - 1
    stats_line("NIGHT + DAY on the same capital (DAY one bar late)", comb, days)
    j = pd.DataFrame({"n": night, "d": out["day"]}, index=days)
    print(f"\ncorrelation NIGHT vs DAY (same-day): {j.corr().iloc[0,1]:.2f}; DAY trades/yr {out['dt'].sum()/ (len(days)/252):.0f}; "
          f"DAY in market at some point on {np.mean(out['dt']>0)*100:.0f}% of days; NIGHT held {np.mean(up)*100:.0f}% of nights")
    s = pd.Series(comb, index=days)
    print("year by year, NIGHT + DAY:", " ".join(f"{y}:{((1+g).prod()-1)*100:+.0f}%" for y, g in s.groupby(s.index.year)))
    s2 = pd.Series(night, index=days)
    print("year by year, NIGHT only :", " ".join(f"{y}:{((1+g).prod()-1)*100:+.0f}%" for y, g in s2.groupby(s2.index.year)))
    s3 = pd.Series(out["day"], index=days)
    print("year by year, DAY only   :", " ".join(f"{y}:{((1+g).prod()-1)*100:+.0f}%" for y, g in s3.groupby(s3.index.year)))
    return {"night": s2, "day": s3, "comb": s}


def up_prev(up):
    return np.r_[False, up[:-1]]


if __name__ == "__main__":
    res = {}
    res["SOXL"] = run("SOXL", "SOXX", 2.0)
    res["TQQQ"] = run("TQQQ", "QQQ", 1.5)
    pd.to_pickle(res, D.CACHE / "daynight.pkl")
