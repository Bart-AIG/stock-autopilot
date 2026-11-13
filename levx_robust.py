"""
LEVX stage 9: try to break it.
  A  Does the night rule work on leveraged index funds it was not built on?
  B  LEVX with worse costs, later exits, without its best nights, and year by year.
  C  Block-bootstrap ranges for the sleeve and for the account mix.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import levx_data as D
import levx_daynight as DN
import levx_intraday as I
import levx_lab as L
import levx_mix as M
import levx_sleeve as SL

PER = (("2007-17", "2007-06-01", "2017-12-31"), ("2018-22", "2018-01-01", "2022-12-31"), ("2023-26", "2023-01-01", "2026-12-31"))


def part_a():
    print("### A. Night rule (index above 200-day SMA, close -> open) on other leveraged index funds")
    print("| Fund | Index | Cost bp/side | 2007-17 | 2018-22 | 2023-26 | Night avg bp (t) 2018-26 |")
    print("|---|---|---|---|---|---|---|")
    funds = [("TQQQ", "QQQ", 3, 1.5), ("SOXL", "SOXX", 3, 2.0), ("QLD", "QQQ", 2, 1.5), ("UPRO", "SPY", 3, 2.0), ("SPXL", "SPY", 3, 2.0),
             ("SSO", "SPY", 2, 1.5), ("UDOW", "DIA", 3, 3.0), ("TNA", "IWM", 3, 2.5), ("TECL", "XLK", 3, 4.0), ("FAS", "XLF", 3, 4.0),
             ("LABU", "XBI", 3, 5.0), ("USD", "SOXX", 2, 5.0), ("NAIL", "ITB", 3, 8.0), ("DPST", "KRE", 3, 8.0), ("YINN", "FXI", 3, 5.0)]
    for f, u, k, c in funds:
        SL.LEGS[f] = (u, float(k), c)
        s = SL.night(f, 200)
        cells = []
        for _, a, b in PER:
            x = s[(s.index >= a) & (s.index <= b)]
            st = L.stats(x.to_numpy())
            cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
        x = s[s.index >= "2018-01-01"]
        g = x[x != 0] + 2 * c / 1e4
        t = g.mean() / (g.std(ddof=1) / np.sqrt(len(g)))
        print(f"| {f} | {u} | {c:g} | " + " | ".join(cells) + f" | {g.mean()*1e4:+.1f} ({t:+.1f}) |")


def build(cost_mult=1.0, exit_bar=None, entry_bar=I.B1550, lag=1, target=0.40, drop_best=0):
    """LEVX-E rebuilt from 5-minute bars with the stress knobs. Returns the daily sleeve series."""
    legs = {}
    for fund, und, cost_bp in (("TQQQ", "QQQ", 1.5), ("SOXL", "SOXX", 2.0)):
        X = I.sessions(fund)
        days = X["days"]
        up = DN.trend_flag(und, days)
        c = cost_bp / 1e4 * cost_mult
        dr, dt, dop = DN.day_leg(X, lag=lag)
        if exit_bar is None:
            nr, ns, take = DN.night_leg(X, up, dop if fund == "TQQQ" else None, bar=entry_bar)
        else:
            nxt = np.r_[X["C"][1:, exit_bar], np.nan]
            near = np.r_[np.diff(days.to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
            take = up & near & np.isfinite(nxt)
            nr, ns = np.where(take, nxt / X["C"][:, entry_bar] - 1, 0.0), np.where(take, 2.0, 0.0)
        raw_n = np.r_[np.nan, (X["O"][1:, 0] / X["C"][:-1, -1] - 1)]
        vol = pd.Series(raw_n).rolling(20, min_periods=10).std().to_numpy() * np.sqrt(252)
        w = np.nan_to_num(np.minimum(1.0, target / np.where(vol > 0, vol, np.nan)), nan=0.0) if target else np.ones(len(days))
        night = w * (nr - ns * c)
        if drop_best:
            idx = np.argsort(night)[-drop_best:]
            night = night.copy()
            night[idx] = 0.0
        legs[f"{fund}_night"] = pd.Series(np.r_[0.0, night[:-1]], index=days)
        legs[f"{fund}_day"] = pd.Series(dr - 2 * c * dt, index=days)
    return M.levx(legs)


def part_b():
    print("\n### B. LEVX (TQQQ night + day, SOXL night, 40% vol target) under stress, 2018-22 | 2023-26 | 2018-26")
    print("| Variant | 2018-22 | 2023-26 | 2018-26 |\n|---|---|---|---|")
    per = (("2018-01-01", "2022-12-31"), ("2023-01-01", "2026-12-31"), ("2018-01-01", "2026-12-31"))
    base = build()
    rows = {"Base": base, "Costs x2": build(cost_mult=2), "Costs x3": build(cost_mult=3), "Costs x5": build(cost_mult=5),
            "Sell at 09:35 instead of the open": build(exit_bar=0), "Sell at 09:45": build(exit_bar=2), "Sell at 10:00": build(exit_bar=5),
            "Buy at 15:30": build(entry_bar=I.B1530), "Buy at the close (15:55 bar)": build(entry_bar=77),
            "Without the 10 best nights per fund": build(drop_best=10), "Without the 25 best nights per fund": build(drop_best=25),
            "No vol target": build(target=None), "Vol target 30%": build(target=0.30), "Vol target 60%": build(target=0.60),
            "Day leg filled at the signal bar (no lag)": build(lag=0), "Day leg two bars late": build(lag=2)}
    for k, s in rows.items():
        print(M.st_line(k, s, per))
    print("\nBase, year by year: " + " ".join(f"{y}:{((1+g).prod()-1)*100:+.0f}%" for y, g in base.groupby(base.index.year)))
    w = (1 + base).cumprod()
    dd = w / w.cummax() - 1
    worst = dd.idxmin()
    start = w[:worst].idxmax()
    print(f"Deepest drawdown {dd.min()*100:.0f}%: {start.date()} -> {worst.date()}. Worst day {base.min()*100:.1f}% on {base.idxmin().date()}. "
          f"Days worse than -5%: {(base < -0.05).sum()}. Months negative: {(base.groupby([base.index.year, base.index.month]).apply(lambda g: (1+g).prod()-1) < 0).mean()*100:.0f}%")
    return base


def boot(s: pd.Series, n=2000, block=20, seed=11):
    rng = np.random.default_rng(seed)
    x = s.to_numpy()
    T = len(x)
    nb = int(np.ceil(T / block))
    out = []
    for _ in range(n):
        st = rng.integers(0, T - block, nb)
        y = np.concatenate([x[a:a + block] for a in st])[:T]
        eq = np.cumprod(1 + y)
        out.append((eq[-1] ** (252 / T) - 1, (eq / np.maximum.accumulate(eq) - 1).min(), y.mean() / y.std() * np.sqrt(252)))
    return np.array(out)


def part_c(base):
    print("\n### C. Block bootstrap (20-day blocks, 2,000 resamples of the 2019-26 daily returns)")
    print("| Series | CAGR 5th / median / 95th | Max DD 5th / median / 95th | Sharpe 5th / median / 95th | P(CAGR < 0) | P(DD worse than -50%) |")
    print("|---|---|---|---|---|---|")
    S = pd.read_pickle(D.CACHE / "mix_series.pkl")
    S["LEVX"] = base.reindex(S.index).fillna(0.0)
    mixes = {"LEVX alone": S["LEVX"], "SWING_Q alone": S["SWING_Q"],
             "Live mix 50/30/20/0": M.combine(np.array([.5, .3, .2, 0]), S[["SWING_Q", "SWING_M", "BBW", "LEVX"]]),
             "30/30/20/20 (20% LEVX from SWING_Q)": M.combine(np.array([.3, .3, .2, .2]), S[["SWING_Q", "SWING_M", "BBW", "LEVX"]]),
             "40/30/10/20": M.combine(np.array([.4, .3, .1, .2]), S[["SWING_Q", "SWING_M", "BBW", "LEVX"]]),
             "50/30/0/20 (20% LEVX replaces BBW)": M.combine(np.array([.5, .3, 0, .2]), S[["SWING_Q", "SWING_M", "BBW", "LEVX"]]),
             "30/30/0/40": M.combine(np.array([.3, .3, 0, .4]), S[["SWING_Q", "SWING_M", "BBW", "LEVX"]])}
    for k, s in mixes.items():
        b = boot(s)
        q = lambda j: np.percentile(b[:, j], [5, 50, 95])
        c, d, sh = q(0), q(1), q(2)
        print(f"| {k} | {c[0]*100:.0f}% / {c[1]*100:.0f}% / {c[2]*100:.0f}% | {d[0]*100:.0f}% / {d[1]*100:.0f}% / {d[2]*100:.0f}% | "
              f"{sh[0]:.2f} / {sh[1]:.2f} / {sh[2]:.2f} | {(b[:,0]<0).mean()*100:.1f}% | {(b[:,1]<-0.5).mean()*100:.1f}% |")


if __name__ == "__main__":
    part_a()
    base = part_b()
    part_c(base)
    base.to_pickle(D.CACHE / "levx_base.pkl")
