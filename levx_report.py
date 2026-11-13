"""LEVX: the closing numbers for levx_results.md, all from the live rules (levx.simulate).
   python levx_report.py"""
from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

import levx
import levx_data as D
import levx_final as F
import levx_lab as L
import levx_mix as M
from levx_robust import boot

warnings.filterwarnings("ignore")
PER = (("2018-01-01", "2022-12-31"), ("2023-01-01", "2026-12-31"), ("2018-01-01", "2026-12-31"))


def line(label, s):
    return M.st_line(label, s, PER)


if __name__ == "__main__":
    res = F.run()
    base = F.sleeve(res)
    j = pd.concat(res, axis=1, sort=True).fillna(0.0)
    print("### Stress (2018-22 | 2023-26 | 2018-26)\n| Variant | 2018-22 | 2023-26 | 2018-26 |\n|---|---|---|---|")
    print(line("Base", base))
    for m in (2, 3, 4):
        print(line(f"Costs x{m}", F.sleeve(F.run(cost_mult=m))))
    for lag in (0, 2):
        print(line(f"DAY fills {lag} bars after the signal", F.sleeve(F.run(lag=lag))))
    for b, lab in ((1, "09:40"), (2, "09:45"), (3, "09:50"), (5, "10:00")):
        print(line(f"Night sold at {lab} instead of 09:35", F.sleeve(F.run(b_exit=b))))
    print(line("Night sold at the open (queued sell), same costs", F.sleeve(F.run(exit_open=True))))
    print(line("Night sold at the open, costs x2", F.sleeve(F.run(exit_open=True, cost_mult=2))))
    print(line("Night sold at the open, +2 bp a side on every order", F.sleeve(F.run(exit_open=True, extra_cost=0.0002))))
    for k in (10, 25):
        r2 = {f: r.copy() for f, r in res.items()}
        for f in r2:
            idx = r2[f]["night_ret"].nlargest(k).index
            r2[f].loc[idx, "night_ret"] = 0.0
        print(line(f"Without each fund's {k} best nights", F.sleeve(r2)))
    r3 = {f: r.copy() for f, r in res.items()}
    idx = r3["TQQQ"]["day_ret"].nlargest(10).index
    r3["TQQQ"].loc[idx, "day_ret"] = 0.0
    print(line("Without the 10 best DAY sessions", F.sleeve(r3)))
    w = (1 + base).cumprod()
    dd = w / w.cummax() - 1
    t1 = dd.idxmin()
    t0 = w[:t1].idxmax()
    mo = base.groupby([base.index.year, base.index.month]).apply(lambda g: (1 + g).prod() - 1)
    print(f"\nDeepest drawdown {dd.min()*100:.0f}% ({t0.date()} to {t1.date()}); worst day {base.min()*100:.1f}% ({base.idxmin().date()}); "
          f"days worse than -5%: {(base < -0.05).sum()} of {len(base)}; losing months {(mo < 0).mean()*100:.0f}%; worst month {mo.min()*100:.0f}%; best month {mo.max()*100:.0f}%")
    last = base[base.index >= "2026-10-01"]
    print(f"2026-10-01 to {base.index[-1].date()}: LEVX {((1+last).prod()-1)*100:+.1f}%")
    print("\n### Bootstrap, 2019-26 daily returns, 20-day blocks, 2,000 resamples")
    print("| Series | CAGR 5th / median / 95th | Max drawdown 5th / median / 95th | P(drawdown beyond -25%) | P(beyond -40%) |\n|---|---|---|---|---|")
    S = pd.read_pickle(D.CACHE / "mix_series.pkl")
    cols = ["SWING_Q", "SWING_M", "BBW", "LEVX"]
    for lab, w_ in (("LEVX alone", (0, 0, 0, 100)), ("Live split 50/30/20/0", (50, 30, 20, 0)), ("30/30/20/20", (30, 30, 20, 20)),
                    ("20/30/20/30", (20, 30, 20, 30)), ("30/30/0/40", (30, 30, 0, 40))):
        b = boot(M.combine(np.array(w_) / 100, S[cols]))
        c, d = np.percentile(b[:, 0], [5, 50, 95]), np.percentile(b[:, 1], [5, 50, 95])
        print(f"| {lab} | {c[0]*100:.0f}% / {c[1]*100:.0f}% / {c[2]*100:.0f}% | {d[0]*100:.0f}% / {d[1]*100:.0f}% / {d[2]*100:.0f}% | "
              f"{(b[:,1] < -0.25).mean()*100:.0f}% | {(b[:,1] < -0.40).mean()*100:.0f}% |")
    n_orders = (j[("TQQQ", "night_w")] > 0).sum() * 2 + (j[("SOXL", "night_w")] > 0).sum() * 2 + j[("TQQQ", "day_trades")].sum() * 2
    print(f"\norders per year: about {n_orders / (len(j) / 252):.0f}")
    import levx_daynight as DN
    import levx_intraday as I
    X = I.sessions("TQQQ")
    print("\n### DAY rule readings on TQQQ (1.5 bp a side, fills one bar late, flat at 15:50)")
    print("| Reading | 2018-22 | 2023-26 | 2018-26 | Round trips a year |\n|---|---|---|---|---|")
    for rule, lab in (("band", "Band only (live)"), ("published", "Band and VWAP (published)"), ("as_first_run", "As first coded")):
        dr, dt, dop = DN.day_leg(X, lag=1, rule=rule)
        adj = np.where(dop, (1 + dr) * X["C"][:, 75] / X["C"][:, -1] - 1, dr) - 2 * 0.00015 * dt
        print(line(lab, pd.Series(adj, index=X["days"])) + f" {dt.sum() / (len(dt) / 252):.0f} |")
    held = res["TQQQ"]["day_held_to_night"].fillna(False).astype(bool)
    print(f"DAY position still on at the NIGHT decision: {held.mean()*100:.0f}% of sessions; "
          f"sessions with a DAY entry: {(res['TQQQ']['day_trades'] > 0).mean()*100:.0f}%")
