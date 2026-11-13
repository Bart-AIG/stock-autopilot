"""
LEVX stage 2b: slot-limited books. Which DESIGN makes the most, and does it survive the years
it was not designed on?

Universes
  IDX    leveraged index/sector funds (real prices from launch, synthetic before)   2007 ->
  IDX+POOL  the same plus a synthetic 2x fund on every end-2018 S&P 100 / Nasdaq-100 name
            (what today's single-stock fund menu would have looked like, without hindsight)
  REAL   every real leveraged fund, single-stock funds included, from its launch, only while
         its 20-day median dollar volume >= $2M                                      2022-08 ->
Discovery = 2007-2022. Validation = 2023 -> today.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import pandas as pd

import levx_book as B
import levx_data as D
import levx_lab as L

DISC = ("2007-06-01", "2022-12-31")
VAL = ("2023-01-01", "2026-12-31")


def segments(pos: np.ndarray):
    """(start, end) index pairs of each run of True in a 1-D bool array."""
    d = np.diff(np.r_[0, pos.astype(int), 0])
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def keep_trades(want: np.ndarray, entry_ok: np.ndarray) -> np.ndarray:
    """Keep only the trades (runs) whose first day passes entry_ok."""
    out = np.zeros_like(want)
    for j in range(want.shape[1]):
        for a, b in segments(want[:, j]):
            if entry_ok[a, j]:
                out[a:b, j] = True
    return out


def top_n_monthly(panel: B.Panel, score: np.ndarray, n: int, gate: np.ndarray | None = None) -> np.ndarray:
    """Membership flag: at each month-end rank eligible names by score, flag the top n for the
    following month."""
    cal = panel.cal
    out = np.zeros(score.shape, bool)
    me = np.flatnonzero(np.r_[cal.month[1:] != cal.month[:-1], True])
    cur = np.zeros(score.shape[1], bool)
    k = 0
    for t in range(len(cal)):
        out[t] = cur
        if k < len(me) and t == me[k]:
            s = np.where(panel.elig[t] & np.isfinite(score[t]), score[t], -np.inf)
            if gate is not None:
                s = np.where(gate[t], s, -np.inf)
            order = np.argsort(-s)
            cur = np.zeros(score.shape[1], bool)
            cur[[j for j in order[:n] if np.isfinite(s[j])]] = True
            k += 1
    return out


def designs(P: B.Panel, vix: np.ndarray):
    sw200 = P.signal(L.sig_swing, trend=200)
    sw0 = P.signal(L.sig_swing, trend=None)
    dip200 = P.signal(L.sig_swing, trend=200, parts=("RSI2", "IBS"))
    dip0 = P.signal(L.sig_swing, trend=None, parts=("RSI2", "IBS"))
    rsi200 = P.signal(L.sig_swing, trend=200, parts=("RSI2",))
    rsi0 = P.signal(L.sig_swing, trend=None, parts=("RSI2",))
    ibs0 = P.signal(L.sig_swing, trend=None, parts=("IBS",))
    don20 = P.signal(L.sig_donchian, n_in=20, n_out=10)
    t200 = P.signal(L.sig_trend, n=200)
    t50 = P.signal(L.sig_trend, n=50)
    vol = P.feature("vol20")
    mom = P.feature("mom12")
    hot = np.repeat((vix >= 22)[:, None], P.n, 1)
    panic = np.repeat((vix >= 28)[:, None], P.n, 1)
    regime = dip200 | keep_trades(dip0, hot)
    out = {
        "SWING200 (house union)": dict(want=sw200, rank=vol),
        "SWING0 (union, no trend filter)": dict(want=sw0, rank=vol),
        "DIP200 (RSI2+IBS, >200d)": dict(want=dip200, rank=vol),
        "DIP0 (RSI2+IBS, any trend)": dict(want=dip0, rank=vol),
        "RSI200 (RSI2 leg, >200d)": dict(want=rsi200, rank=vol),
        "RSI0 (RSI2 leg, any trend)": dict(want=rsi0, rank=vol),
        "REGIME (DIP200, plus any-trend dips when VIX>=22)": dict(want=regime, rank=vol),
        "HOT (dips only when VIX>=22)": dict(want=keep_trades(dip0, hot), rank=vol),
        "PANIC (dips only when VIX>=28)": dict(want=keep_trades(dip0, panic), rank=vol),
        "CALM (DIP200 only when VIX<22)": dict(want=keep_trades(dip200, ~hot), rank=vol),
        "DON20 breakout, rank momentum": dict(want=don20, rank=mom),
        "MOM top-4 monthly, >200d": dict(want=top_n_monthly(P, mom, 4, t200 & P.elig) & t200, fresh_only=False),
        "MOM top-4 monthly, >50d": dict(want=top_n_monthly(P, mom, 4, t50 & P.elig) & t50, fresh_only=False),
        "MOM top-10 x SWING200 (SWING_M at 2x)": dict(want=top_n_monthly(P, mom, 10) & sw200, fresh_only=False, K=10),
        "MOM top-10 x SWING0": dict(want=top_n_monthly(P, mom, 10) & sw0, fresh_only=False, K=10),
        "BUY & HOLD equal weight": dict(want=np.ones_like(sw200), fresh_only=False, K=P.n),
    }
    return out


def report(label, P, vix, K=4, periods=(("disc", DISC), ("val", VAL)), ref=None, only=None):
    print(f"\n### {label}: {P.n} names, {K} slots")
    print("| Design | " + " | ".join(f"{p} CAGR / DD / Sharpe" for p, _ in periods) + " | Invested | Trades | Win | Avg trade | Worst | Corr SWING_Q |")
    print("|---|" + "---|" * (len(periods) + 6))
    res = {}
    for name, d in designs(P, vix).items():
        if only and not any(o in name for o in only):
            continue
        cells, last = [], None
        for pl, (a, b) in periods:
            st = B.run_book(P, d["want"], K=d.get("K", K), rank=d.get("rank"), fresh_only=d.get("fresh_only", True), start=a, end=b)
            cells.append(f"{L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'], 0)} / {st['sharpe']:.2f}")
            res[(name, pl)] = st
            last = st
        full = B.run_book(P, d["want"], K=d.get("K", K), rank=d.get("rank"), fresh_only=d.get("fresh_only", True), start=periods[0][1][0], end=periods[-1][1][1])
        corr = float("nan")
        if ref is not None:
            x = pd.Series(full["r"], index=full["idx"])
            j = pd.concat([x, ref], axis=1, sort=True).dropna()
            corr = float(j.corr().iloc[0, 1])
        res[(name, "full")] = full
        print(f"| {name} | " + " | ".join(cells) + f" | {full['expo']*100:.0f}% | {full['trades']} | {L.fmt_pct(full['win'],0)} | {L.fmt_pct(full['avg_trade'],2)} | {L.fmt_pct(full['worst_trade'],0)} | {corr:.2f} |")
    return res


def members_index():
    uni = L.universe()
    idx_rows = [r for r in uni if r["kind"] == "index"]
    bi = L.best_fund_per_underlying(idx_rows, "history")
    for r in idx_rows:
        cur = bi[r["und"]]
        if r["lev"] > cur["lev"] and r["first"] <= "2011-06-30":
            bi[r["und"]] = r
    return [{"und": u, "lev": r["lev"], "kind": "index", "fund": r["fund"]} for u, r in sorted(bi.items()) if r["first"] <= "2016-01-01"]


def members_real(min_dv=2e6):
    uni = L.universe(min_dv)
    best = L.best_fund_per_underlying(uni, "history")
    return [{"und": u, "lev": r["lev"], "kind": r["kind"], "fund": r["fund"]} for u, r in sorted(best.items())]


def swing_q_ref():
    P = B.Panel([{"und": "QQQ", "lev": 2.0, "kind": "index", "fund": "QLD"}], start="2006-06-01")
    st = B.run_book(P, P.signal(L.sig_swing, trend=200), K=1, fresh_only=False, size=1.0, start="2007-06-01")
    return pd.Series(st["r"], index=st["idx"]), st


if __name__ == "__main__":
    vix_s = D.daily("^VIX", drop_today_if_open=False)["raw"]
    ref, ref_st = swing_q_ref()
    for pl, (a, b) in (("disc", DISC), ("val", VAL)):
        x = ref[(ref.index >= a) & (ref.index <= b)]
        st = L.stats(x.to_numpy())
        print(f"SWING_Q reference (QQQ signals in QLD) {pl}: {L.fmt_pct(st['cagr'])} / {L.fmt_pct(st['mdd'],0)} / {st['sharpe']:.2f}")
    which = sys.argv[1:] or ["IDX", "POOL", "IDX+POOL", "REAL"]
    idx = members_index()
    pool = [{"und": s, "lev": 2.0, "kind": "stock", "fund": None} for s in L.pit_pool()]
    if "IDX" in which:
        P = B.Panel(idx, start="2006-06-01")
        report("IDX: leveraged index/sector funds", P, vix_s.reindex(P.cal).ffill().to_numpy(), ref=ref)
    if "POOL" in which:
        P = B.Panel(pool, start="2006-06-01")
        report("POOL: synthetic 2x on the end-2018 S&P 100 + Nasdaq-100 names", P, vix_s.reindex(P.cal).ffill().to_numpy(), ref=ref)
    if "IDX+POOL" in which:
        P = B.Panel(idx + pool, start="2006-06-01")
        report("IDX+POOL", P, vix_s.reindex(P.cal).ffill().to_numpy(), ref=ref)
    if "REAL" in which:
        P = B.Panel(members_real(), start="2021-06-01", veh_mode="real")
        report("REAL: every real leveraged fund from launch, >= $2M/day", P, vix_s.reindex(P.cal).ffill().to_numpy(),
               periods=(("2022-08 to 2024", ("2022-08-01", "2024-12-31")), ("2025 to now", ("2025-01-01", "2026-12-31"))), ref=ref)
