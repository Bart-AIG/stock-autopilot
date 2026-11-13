"""
LEVX stage 1: which DAILY-bar rule has a real edge on leveraged-fund underlyings?

Every rule is pre-specified (published or already used by the house) and run unchanged on
five universes. Two measures per rule:
  timing edge   mean next-day return of the UNDERLYING on held days minus its mean on all
                days (bp/day), averaged across names by date, with a t-stat. This is free of
                the universe's own drift, so a hindsight-picked list cannot fake it.
  sleeve        equal-weight book of the leveraged vehicles (cash when a name is out),
                net of costs: CAGR / max drawdown / Sharpe.
Discovery = 2011-2022, validation = 2023 -> today (never used to choose anything).

  python levx_stage1.py   -> data/levx_cache/stage1.json, prints tables
"""
from __future__ import annotations

import json
import math
import sys

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L

DISC = ("2011-01-01", "2022-12-31")
VAL = ("2023-01-01", "2099-01-01")
COST = {"index": 0.0005, "stock": 0.0020}

RULES = {
    "BH":        (L.sig_bh, {}, "cc"),
    "T200":      (L.sig_trend, {"n": 200}, "cc"),
    "T50":       (L.sig_trend, {"n": 50}, "cc"),
    "T20":       (L.sig_trend, {"n": 20}, "cc"),
    "STACK":     (L.sig_mom_gate, {}, "cc"),
    "SWING":     (L.sig_swing, {"trend": 200}, "cc"),
    "SWING50":   (L.sig_swing, {"trend": 50}, "cc"),
    "SWING0":    (L.sig_swing, {"trend": None}, "cc"),
    "RSI2":      (L.sig_swing, {"trend": 200, "parts": ("RSI2",)}, "cc"),
    "IBS":       (L.sig_swing, {"trend": 200, "parts": ("IBS",)}, "cc"),
    "TOM":       (L.sig_swing, {"trend": None, "parts": ("TOM",)}, "cc"),
    "DIP0":      (L.sig_swing, {"trend": None, "parts": ("RSI2", "IBS")}, "cc"),
    "DIPBELOW":  (None, {}, "cc"),          # dips only BELOW the 200-day (what a knife-catcher buys)
    "DON20":     (L.sig_donchian, {"n_in": 20, "n_out": 10}, "cc"),
    "DON55":     (L.sig_donchian, {"n_in": 55, "n_out": 20}, "cc"),
    "UPCONT":    (L.sig_upcont, {}, "cc"),
    "DNREV":     (L.sig_dnrev, {}, "cc"),
    "WASH":      (L.sig_washout, {}, "cc"),
    "OVN":       (L.sig_bh, {}, "ovn"),
    "OVN200":    (L.sig_trend, {"n": 200}, "ovn"),
    "INTRA":     (L.sig_bh, {}, "intra"),
}


def positions(name, df):
    if name == "DIPBELOW":
        a = L.sig_swing(df, trend=None, parts=("RSI2", "IBS"))
        b = L.sig_swing(df, trend=200, parts=("RSI2", "IBS"))
        return a & ~b
    fn, kw, _ = RULES[name]
    return fn(df, **kw)


def run_universe(label, members, start="2011-01-01", veh_mode="hybrid", elig=None):
    """members: list of dict(und, lev, kind, fund). Returns per-rule dict of period stats."""
    cash = L.cash_returns()
    cal = D.daily("SPY").index
    cal = cal[cal >= start]
    per_rule_ret = {r: [] for r in RULES}
    per_rule_edge = {r: [] for r in RULES}
    per_rule_trades = {r: [] for r in RULES}
    und_ret_all = []
    used = 0
    for m in members:
        u = D.daily(m["und"])
        if u is None or len(u) < 260:
            continue
        veh = L.vehicle(m["und"], m["lev"], m["kind"], m.get("fund"), mode=veh_mode)
        if veh is None:
            continue
        used += 1
        c = cash.reindex(u.index).fillna(0.0).to_numpy()
        ur = u["c"].pct_change().to_numpy()
        ok = veh["rc"].notna().to_numpy()
        if elig is not None:
            ok &= elig(m, u, veh)
        und_ret_all.append(pd.Series(np.where(ok, ur, np.nan), index=u.index).reindex(cal))
        cost = COST[m["kind"]]
        for name, (_, _, mode) in RULES.items():
            pos = positions(name, u)
            r = L.simulate(pos, veh, cost, mode, c)
            r = np.where(ok, r, np.nan)
            per_rule_ret[name].append(pd.Series(r, index=u.index).reindex(cal))
            held = np.r_[False, pos[:-1]]
            if mode == "ovn":
                base = (u["o"] / u["c"].shift(1) - 1).to_numpy()
            elif mode == "intra":
                base = (u["c"] / u["o"] - 1).to_numpy()
            else:
                base = ur
            per_rule_edge[name].append(pd.Series(np.where(held & ok, base, np.nan), index=u.index).reindex(cal))
            if mode == "cc":
                tr = L.trades(pos[u.index >= start], np.nan_to_num(veh["rc"].to_numpy())[u.index >= start], cost)
                per_rule_trades[name].append(tr)
    und = pd.concat(und_ret_all, axis=1)
    out = {"_n": used}
    for name in RULES:
        R = pd.concat(per_rule_ret[name], axis=1)
        port = R.mean(axis=1, skipna=True).fillna(0.0)
        E = pd.concat(per_rule_edge[name], axis=1)
        res = {}
        for pl, (a, b) in (("disc", DISC), ("val", VAL), ("all", (start, "2099"))):
            sl = (port.index >= a) & (port.index <= b)
            st = L.stats(port[sl].to_numpy())
            # timing edge by date: mean held-return across names minus mean all-return across names
            he, al = E[sl].mean(axis=1, skipna=True), und[sl].mean(axis=1, skipna=True)
            d = (he - al).dropna()
            t = float(d.mean() / (d.std(ddof=1) / math.sqrt(len(d)))) if len(d) > 30 and d.std() > 0 else float("nan")
            tim = float(E[sl].notna().sum().sum() / max(1, und[sl].notna().sum().sum()))
            st.update(edge_bp=float(d.mean() * 1e4) if len(d) else float("nan"), t=t, tim=tim,
                      held_bp=float(np.nanmean(E[sl].to_numpy()) * 1e4) if E[sl].notna().any().any() else float("nan"))
            res[pl] = st
        if per_rule_trades[name]:
            tr = np.concatenate(per_rule_trades[name]) if len(per_rule_trades[name]) else np.array([])
            if len(tr):
                res["trades"] = {"n": int(len(tr)), "win": float((tr > 0).mean()), "avg": float(tr.mean()),
                                 "med": float(np.median(tr)), "worst": float(tr.min())}
        out[name] = res
    return out


def table(label, res):
    print(f"\n### {label} ({res['_n']} names)")
    print("| Rule | Time in | Edge bp/day (t) disc | Edge (t) val | Sleeve disc CAGR / DD / Sh | Sleeve val CAGR / DD / Sh | Trades | Win | Avg trade |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name in RULES:
        r = res[name]
        d, v = r["disc"], r["val"]
        tr = r.get("trades", {})
        print(f"| {name} | {d['tim']*100:.0f}% | {d['edge_bp']:+.1f} ({d['t']:+.1f}) | {v['edge_bp']:+.1f} ({v['t']:+.1f}) | "
              f"{L.fmt_pct(d['cagr'])} / {L.fmt_pct(d['mdd'],0)} / {d['sharpe']:.2f} | "
              f"{L.fmt_pct(v['cagr'])} / {L.fmt_pct(v['mdd'],0)} / {v['sharpe']:.2f} | "
              f"{tr.get('n','')} | {L.fmt_pct(tr.get('win'),0) if tr else ''} | {L.fmt_pct(tr.get('avg'),2) if tr else ''} |")


def main():
    uni = L.universe()
    idx_rows = [r for r in uni if r["kind"] == "index"]
    stk_rows = [r for r in uni if r["kind"] == "stock"]
    bi = L.best_fund_per_underlying(idx_rows, "history")
    # index funds: prefer 3x where the same underlying has both, they are "like SOXL"
    for r in idx_rows:
        cur = bi[r["und"]]
        if r["lev"] > cur["lev"] and r["first"] <= "2011-06-30":
            bi[r["und"]] = r
    index_members = [{"und": u, "lev": r["lev"], "kind": "index", "fund": r["fund"]} for u, r in sorted(bi.items())
                     if r["first"] <= "2016-01-01"]
    bs = L.best_fund_per_underlying([r for r in stk_rows if r["dv60"] >= 2e6], "history")
    stock_members = [{"und": u, "lev": 2.0, "kind": "stock", "fund": r["fund"]} for u, r in sorted(bs.items())]
    pool_members = [{"und": s, "lev": 2.0, "kind": "stock", "fund": None} for s in L.pit_pool()]
    named = [{"und": "SOXX", "lev": 3.0, "kind": "index", "fund": "SOXL"},
             {"und": "AAOI", "lev": 2.0, "kind": "stock", "fund": "AAOX"},
             {"und": "COHR", "lev": 2.0, "kind": "stock", "fund": "COHX"},
             {"und": "LITE", "lev": 2.0, "kind": "stock", "fund": "LITX"}]
    out = {}
    out["QQQ->QLD (SWING_Q reference)"] = run_universe("q", [{"und": "QQQ", "lev": 2.0, "kind": "index", "fund": "QLD"}])
    out["SOXX->SOXL (3x, real fund)"] = run_universe("s", named[:1])
    out["Named single stocks: AAOI, COHR, LITE (2x)"] = run_universe("n", named[1:])
    out["INDEX/SECTOR leveraged funds"] = run_universe("i", index_members)
    out["STOCKS with a 2x fund today (hindsight list)"] = run_universe("st", stock_members)
    out["PIT POOL: end-2018 S&P 100 + Nasdaq-100 (2x synthetic)"] = run_universe("p", pool_members)
    (D.CACHE / "stage1.json").write_text(json.dumps(out, indent=1, default=float))
    print("index members:", [(m["und"], m["fund"], m["lev"]) for m in index_members])
    print("stock members:", len(stock_members))
    for k, v in out.items():
        table(k, v)


if __name__ == "__main__":
    main()
