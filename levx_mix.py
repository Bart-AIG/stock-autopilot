"""
LEVX stage 8: the sleeve as a whole, and how it mixes with the live sleeves.

Sleeve series (daily, net of costs):
  SWING_Q   QQQ swing union in QLD (house rule, this engine reproduces robust_backtest.swing)
  SWING_M   monthly top-10 momentum names, swing union, 1x (house rule)
  BBW       the live bbw.py rules on NVDA 2x (synthetic to 2022, real NVDL from 2023)
  LEVX      TQQQ night + TQQQ day + SOXL night, from real 5-minute bars
Mixes are rebalanced monthly (as in mix_optimizer.py). 2019-22 picks a mix; 2023-26 scores it.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import pandas as pd

import bbw
import levx_book as B
import levx_data as D
import levx_daynight as DN
import levx_intraday as I
import levx_lab as L
from levx_bbw_long import candles15
from levx_stage2b import top_n_monthly

START = "2019-01-02"


def swing_q():
    P = B.Panel([{"und": "QQQ", "lev": 2.0, "kind": "index", "fund": "QLD"}], start="2006-06-01")
    st = B.run_book(P, P.signal(L.sig_swing, trend=200), K=1, fresh_only=False, size=1.0, start="2007-06-01")
    return pd.Series(st["r"], index=st["idx"])


def swing_m():
    pool = [{"und": s, "lev": 1.0, "kind": "spot", "fund": None} for s in L.pit_pool()]
    P = B.Panel(pool, start="2017-06-01", syn_cost=1e-4)
    top = top_n_monthly(P, P.feature("mom12"), 10)
    st = B.run_book(P, top & P.signal(L.sig_swing, trend=200), K=10, fresh_only=False, start="2018-06-01")
    return pd.Series(st["r"], index=st["idx"])


def bbw_series(cost=0.0003):
    out = {}
    for sym, lev, a, b in (("NVDA", 2.0, "2018-01-01", "2022-12-31"), ("NVDL", None, "2023-01-01", "2099-01-01")):
        X = I.sessions(sym, (sym, lev)) if lev else I.sessions(sym)
        r = bbw.backtest(candles15(X))
        for t in r["list"]:
            d = pd.Timestamp(t["out"][:10])
            if a <= str(d.date()) <= b:
                out[d] = (1 + out.get(d, 0.0)) * (1 + t["ret"] - 2 * cost) - 1
    return pd.Series(out).sort_index()


def levx_legs(target=None):
    """Night legs booked on the day the position is SOLD (so they line up with close-to-close
    sleeves); day leg booked on its own day. target = annualised overnight vol target per fund."""
    legs = {}
    for fund, und, cost_bp in (("TQQQ", "QQQ", 1.5), ("SOXL", "SOXX", 2.0)):
        X = I.sessions(fund)
        days = X["days"]
        up = DN.trend_flag(und, days)
        c = cost_bp / 1e4
        dr, dt, dop = DN.day_leg(X, lag=1)
        nr, ns, take = DN.night_leg(X, up, dop if fund == "TQQQ" else None)
        w = np.ones(len(days))
        if target:
            raw_n = np.r_[np.nan, (X["O"][1:, 0] / X["C"][:-1, -1] - 1)]       # last night's move, known today
            vol = pd.Series(raw_n).rolling(20, min_periods=10).std().to_numpy() * np.sqrt(252)
            w = np.nan_to_num(np.minimum(1.0, target / np.where(vol > 0, vol, np.nan)), nan=0.0)
        night = w * (nr - ns * c)
        legs[f"{fund}_night"] = pd.Series(np.r_[0.0, night[:-1]], index=days)
        saved = np.where(dop & (ns == 0) & up, c, 0.0) if fund == "TQQQ" else 0.0
        legs[f"{fund}_day"] = pd.Series(dr - 2 * c * dt + saved, index=days)
    return legs


def levx(legs, w_t_night=0.5, w_s_night=0.5, w_t_day=1.0, soxl_day=0.0):
    """Sleeve return: night capital split TQQQ/SOXL; the DAY leg runs on w_t_day of the sleeve."""
    j = pd.DataFrame(legs).fillna(0.0)
    night = w_t_night * j["TQQQ_night"] + w_s_night * j["SOXL_night"]
    day = w_t_day * j["TQQQ_day"] + soxl_day * j["SOXL_day"]
    return (1 + night) * (1 + day) - 1


def combine(weights, sleeves: pd.DataFrame) -> pd.Series:
    """Monthly rebalance to the weights (mix_optimizer.combine)."""
    bal, month, out = np.array(weights, float), None, []
    w = np.array(weights, float)
    for d, row in zip(sleeves.index, sleeves.to_numpy()):
        m = (d.year, d.month)
        if m != month:
            bal, month = w * bal.sum() if month else w.copy(), m
        tot = bal.sum()
        bal = bal * (1 + row)
        out.append(bal.sum() / tot - 1)
    return pd.Series(out, index=sleeves.index)


def st_line(label, s, periods):
    cells = []
    for a, b in periods:
        x = s[(s.index >= a) & (s.index <= b)]
        st = L.stats(x.to_numpy())
        cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
    return f"| {label} | " + " | ".join(cells) + " |"


def swing_q_1550():
    """SWING_Q decided and traded at 15:50 on the live price (the house's pessimistic version,
    mix_optimizer.py): robust_backtest.swing with the 15:45 bar's close as the execution price.
    2x synthetic, as in the house test."""
    from robust_backtest import swing
    q = D.daily("QQQ", drop_today_if_open=False)
    Xq = I.sessions("QQQ")
    ds = [d.strftime("%Y-%m-%d") for d in q.index]
    C, H, Lw = q["c"].tolist(), q["h"].tolist(), q["l"].tolist()
    X, XH, XL = list(C), list(H), list(Lw)
    f = (q["c"] / q["raw"]).to_dict()
    pos = {d: i for i, d in enumerate(q.index)}
    for k, d in enumerate(Xq["days"]):
        i = pos.get(d)
        if i is None:
            continue
        X[i] = Xq["C"][k, 74] * f[d]
        XH[i] = Xq["H"][k, :75].max() * f[d]
        XL[i] = Xq["L"][k, :75].min() * f[d]
    cash = L.cash_returns()
    br = {d.strftime("%Y-%m-%d"): float(v) for d, v in cash.items()}
    out = swing(ds, C, H, Lw, None, X=X, XH=XH, XL=XL, lev=2, cash=br)
    s = pd.Series(out)
    s.index = pd.to_datetime(s.index)
    return s


if __name__ == "__main__":
    import levx_final as F
    per = (("2019-01-02", "2022-12-31"), ("2023-01-01", "2026-12-31"), ("2019-01-02", "2026-12-31"))
    cash = L.cash_returns()
    sq, sm, bw = swing_q(), swing_m(), bbw_series()
    lx = F.sleeve(F.run())
    lx2 = F.sleeve(F.run(cost_mult=2))
    S = pd.DataFrame({"SWING_Q": sq, "SWING_M": sm}).dropna()
    S = S[S.index >= START]
    S["BBW"] = bw.reindex(S.index).fillna(0.0)
    S["LEVX"] = lx.reindex(S.index).fillna(0.0)
    c = cash.reindex(S.index).fillna(0.0)
    Pz = pd.DataFrame({"SWING_Q": swing_q_1550().reindex(S.index).fillna(0.0), "SWING_M": c + 0.75 * (S["SWING_M"] - c),
                       "BBW": S["BBW"], "LEVX": lx2.reindex(S.index).fillna(0.0)})
    S.to_pickle(D.CACHE / "mix_series.pkl")
    Pz.to_pickle(D.CACHE / "mix_series_pess.pkl")
    q = D.daily("QQQ")["c"].pct_change().reindex(S.index).fillna(0.0)
    print("### Sleeves alone (CAGR / max drawdown / Sharpe)")
    print("| Sleeve | 2019-22 | 2023-26 | 2019-26 | 2019-26 pessimistic |\n|---|---|---|---|---|")
    for k in ("SWING_Q", "SWING_M", "BBW", "LEVX"):
        print(st_line(k, S[k], per)[:-1] + st_line("", Pz[k], per[2:]).split("|", 2)[2])
    print(st_line("QQQ buy & hold", q, per) + " |")
    print("\n### Daily correlation, 2019-26")
    print(S.corr().round(2).to_string())
    xx = pd.concat([S["LEVX"], q.rename("QQQ")], axis=1)
    beta = np.cov(xx["LEVX"], xx["QQQ"])[0, 1] / xx["QQQ"].var()
    alpha = (xx["LEVX"].mean() - beta * xx["QQQ"].mean()) * 252
    print(f"\nLEVX vs QQQ (daily, 2019-26): beta {beta:.2f}, alpha {alpha*100:.0f}%/yr, correlation {xx.corr().iloc[0,1]:.2f}")
    cols = ["SWING_Q", "SWING_M", "BBW", "LEVX"]
    print("\n### Account mixes, monthly rebalance. Split = SWING_Q / SWING_M / BBW / LEVX")
    print("| Split | 2019-22 | 2023-26 | 2019-26 | 2019-26 pessimistic | Worst day | $2,372 becomes (pessimistic, 2019-26) |")
    print("|---|---|---|---|---|---|---|")
    mixes = ((50, 30, 20, 0), (40, 30, 20, 10), (30, 30, 20, 20), (40, 30, 10, 20), (50, 30, 0, 20), (50, 20, 10, 20),
             (20, 30, 20, 30), (30, 30, 10, 30), (40, 30, 0, 30), (30, 30, 0, 40), (20, 30, 0, 50), (0, 30, 0, 70), (0, 0, 0, 100))
    for w in mixes:
        a = combine(np.array(w) / 100, S[cols])
        b = combine(np.array(w) / 100, Pz[cols])
        end = 2372 * float((1 + b).prod())
        print(st_line(" / ".join(str(x) for x in w), a, per)[:-1] + st_line("", b, per[2:]).split("|", 2)[2]
              + f" {a.min()*100:.1f}% | ${end:,.0f} |")
    print("\n### Walk-forward: pick the split on 2019-22 only, score it on 2023-26 (10% steps, as tested)")
    grid = [w for w in itertools.product(range(0, 101, 10), repeat=4) if sum(w) == 100]
    a0, b0 = per[0]
    res = []
    for w in grid:
        s_ = combine(np.array(w) / 100, S[cols])
        st = L.stats(s_[(s_.index >= a0) & (s_.index <= b0)].to_numpy())
        res.append((w, st["cagr"], st["mdd"], st["sharpe"], s_))
    for lim in (-0.20, -0.25, -0.30, -0.99):
        ok = [r for r in res if r[2] >= lim]
        if not ok:
            continue
        best = max(ok, key=lambda r: r[1])
        st = L.stats(best[4][best[4].index >= per[1][0]].to_numpy())
        print(f"- drawdown limit {lim:.0%}: picks {best[0]} ({best[1]:.1%} / {best[2]:.0%} in 2019-22); unseen 2023-26: {st['cagr']:.1%} / {st['mdd']:.0%} / {st['sharpe']:.2f}")
    bs = max(res, key=lambda r: r[3])
    st = L.stats(bs[4][bs[4].index >= per[1][0]].to_numpy())
    print(f"- best Sharpe in 2019-22: {bs[0]} ({bs[3]:.2f}); unseen 2023-26: {st['cagr']:.1%} / {st['mdd']:.0%} / {st['sharpe']:.2f}")
    live = [r for r in res if r[0] == (50, 30, 20, 0)][0]
    st = L.stats(live[4][live[4].index >= per[1][0]].to_numpy())
    print(f"- live split (50, 30, 20, 0) for reference: {live[1]:.1%} / {live[2]:.0%} in 2019-22; 2023-26: {st['cagr']:.1%} / {st['mdd']:.0%} / {st['sharpe']:.2f}")
