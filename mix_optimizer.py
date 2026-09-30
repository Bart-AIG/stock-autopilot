"""
Mix optimizer — which ratio of the strongest sleeves gives the best annual return with low
drawdowns?  (Ryan, 2026-09-30: "maybe there is a ratio that give the best annual return and
low drops".)

Runs on GitHub Actions (FMP key). Pure standard library.

Candidate sleeves (each as tested before, 2019 -> today):
  CORE     vol-targeted QQQ (25% / 20d realised vol, <=2x) above the 200-day SMA, else T-bills
  SWING_M  RSI2 + IBS + turn-of-month on the monthly top-10 12-month-momentum names, 1x
  SWING_Q  the same rules on QQQ at 2x (QLD)
  DAY      noise-area breakout on QQQ, 5-minute bars, 3x
  ODTE     SPX-style 0DTE credit spread at 2x the expected move, 10% of sleeve at risk,
           ASSUMED 3% credit (no option prices exist to test the credit)

Method:
  * Every split in 10% steps across the five sleeves (1,001 portfolios), monthly rebalance.
  * Frontier: best CAGR for each max-drawdown limit.
  * Walk-forward (the honest check): pick the best split using 2019-2022 ONLY, then score it
    on 2023-2026, which the pick never saw.
  * Pessimistic re-run of the winners with the realistic sleeve versions:
      DAY on 30-minute bars (how it would actually trade), 0DTE at a 2% credit,
      SWING_Q traded at 15:50, SWING_M with a 25% haircut on its excess return over cash
      (the QQQ swing lost ~25% trading at 15:50; single-name 15:50 data would take hours).
Limits: ~7.7 years; one path; the optimum of 1,001 tries is flattered by construction - the
walk-forward and pessimistic rows are the ones to believe.
"""

from __future__ import annotations

import itertools
import math
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

from backtest import NDX100_2018, SP100_2018
from combo_backtest import curve_stats, noise_series
from intraday_backtest import fetch_5min, fetch_unadjusted
from momentum_sleeves_backtest import adj, bars30, noise30
from options_income_backtest import zero_dte
from robust_backtest import arrays, combine, full_ohlc, swing

HERE = Path(__file__).resolve().parent
NAMES = ["CORE", "SWING_M", "SWING_Q", "DAY", "ODTE"]


def prev_closes(days, raw):
    rd, prev, j = sorted(raw), {}, 0
    for s in sorted(days):
        while j < len(rd) and rd[j] < s:
            j += 1
        if j:
            prev[s] = raw[rd[j - 1]]
    return prev


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "BIL"]):
        a = adj(s, key)
        if a:
            A[s] = a
        if n % 40 == 0:
            print(f"daily {n}", flush=True)
        time.sleep(0.08)
    qd = sorted(d for d in A["QQQ"] if d in A["BIL"])
    Q = [A["QQQ"][d] for d in qd]
    qr = {qd[i]: Q[i] / Q[i - 1] - 1 for i in range(1, len(qd))}
    br = {qd[i]: A["BIL"][qd[i]] / A["BIL"][qd[i - 1]] - 1 for i in range(1, len(qd))}
    rv = [None] * len(qd)
    for i in range(21, len(qd)):
        rv[i] = statistics.pstdev([Q[j] / Q[j - 1] - 1 for j in range(i - 19, i + 1)]) * math.sqrt(252)

    # CORE
    core = {}
    for i in range(203, len(qd)):
        if Q[i - 2] > sum(Q[i - 201:i - 1]) / 200:
            lv = min(2.0, 0.25 / (rv[i - 1] or 1e-9))
            core[qd[i]] = lv * qr[qd[i]] - 0.00475 * lv / 252 - max(0.0, lv - 1) * br.get(qd[i], 0.0)
        else:
            core[qd[i]] = br.get(qd[i], 0.0)

    # SWING_M
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}
    for m in me:
        k = qd.index(m)
        sc = sorted(((A[s][m] / A[s][qd[k - 252]] - 1, s) for s in pool
                     if s in A and m in A[s] and qd[k - 252] in A[s]), reverse=True)
        picks[m] = [s for _, s in sc[:10]]
    ever = sorted({s for v in picks.values() for s in v})
    sw = {}
    for s in ever:
        o = full_ohlc(s, key, "2016-06-01")
        if o and s in A:
            ds, C, H, L = arrays(o, A[s])
            if len(ds) > 260:
                sw[s] = swing(ds, C, H, L, None, lev=1, cash=br)
        time.sleep(0.05)
    tdates = [d for d in qd if d > me[0]]
    swing_m = {}
    for d in tdates:
        b = picks[[m for m in me if m < d][-1]]
        rs = [sw[s].get(d, 0.0) for s in b if s in sw]
        swing_m[d] = sum(rs) / len(rs) if rs else 0.0
    swing_m_pess = {d: br.get(d, 0.0) + 0.75 * (r - br.get(d, 0.0)) for d, r in swing_m.items()}

    # SWING_Q (close and 15:50)
    q_ohlc = full_ohlc("QQQ", key, "2016-06-01")
    ds, C, H, L = arrays(q_ohlc, A["QQQ"])
    swing_q = swing(ds, C, H, L, None, lev=2, cash=br)
    q5 = fetch_5min("QQQ", key, log)
    raw_q = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    X, XH, XL = list(C), list(H), list(L)
    for i, d in enumerate(ds):
        bars = q5.get(d)
        if bars and d in raw_q:
            upto = [b for b in bars if b["t"] <= "15:45"]
            if len(upto) >= 60:
                f = C[i] / raw_q[d]
                X[i], XH[i], XL[i] = upto[-1]["c"] * f, max(b["h"] for b in upto) * f, min(b["l"] for b in upto) * f
    swing_q_1550 = swing(ds, C, H, L, None, X=X, XH=XH, XL=XL, lev=2, cash=br)

    # DAY (5-min and 30-min)
    day5 = noise_series(q5, prev_closes(q5, raw_q), 14, 30, 3, 3e-4)
    q30 = bars30("QQQ", key, log)
    d30 = noise30(q30, prev_closes(q30, raw_q), long_only=False)
    day30 = {d: 3 * r for d, r in d30.items()}

    # ODTE (3% and 2% credit)
    s5 = fetch_5min("SPY", key, log)
    sc_ = {s: s5[s][-1]["c"] for s in s5}
    odte3 = {d: (0.10 * v / 0.97 if v is not None else 0.0) for d, v in zero_dte(s5, sc_, 2.0, 0.03).items()}
    odte2 = {d: (0.10 * v / 0.98 if v is not None else 0.0) for d, v in zero_dte(s5, sc_, 2.0, 0.02).items()}

    start = max(min(core), min(swing_m), min(day5), min(odte3), "2019-01-02")
    pd = [d for d in tdates if d >= start and d in core]
    opt = {"CORE": core, "SWING_M": swing_m, "SWING_Q": swing_q, "DAY": day5, "ODTE": odte3}
    pess = {"CORE": core, "SWING_M": swing_m_pess, "SWING_Q": swing_q_1550, "DAY": day30, "ODTE": odte2}

    def evaluate(w, sleeves, dates):
        pr = combine([x / 10 for x in w], [sleeves[n] for n in NAMES], dates)
        st, y, end = curve_stats(pr, dates)
        return st, y, end

    grid = [w for w in itertools.product(range(11), repeat=5) if sum(w) == 10]
    train = [d for d in pd if d <= "2022-12-31"]
    test = [d for d in pd if d >= "2023-01-01"]
    res = []
    for w in grid:
        st, y, end = evaluate(w, opt, pd)
        tr, _, _ = evaluate(w, opt, train)
        te, _, _ = evaluate(w, opt, test)
        res.append({"w": w, "st": st, "y": y, "end": end, "tr": tr, "te": te})

    fmt = lambda w: " / ".join(f"{x * 10}" for x in w)
    out = [f"# Mix optimizer — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Period {pd[0]} → {pd[-1]}. Weights are CORE / SWING_M / SWING_Q / DAY / ODTE (%). "
           "1,001 splits in 10% steps, monthly rebalance. QQQ over the same days is the benchmark.\n"]
    qs, qy, qe = curve_stats([qr[d] for d in pd], pd)
    qtr, _, _ = curve_stats([qr[d] for d in train], train)
    qte, _, _ = curve_stats([qr[d] for d in test], test)
    out.append(f"**QQQ:** {qs['cagr']:.1%}/yr, max DD {qs['mdd']:.1%}, worst year {min(qy.values()):.1%}, "
               f"$3,340 → ${3340 * qe:,.0f}. 2019–22: {qtr['cagr']:.1%}; 2023–26: {qte['cagr']:.1%}.\n")

    # sleeves alone + correlations
    out.append("## Each sleeve alone (optimistic version / pessimistic version)\n")
    out.append("| Sleeve | CAGR / max DD (as tested) | CAGR / max DD (pessimistic) |\n|---|---|---|")
    for n in NAMES:
        a, _, _ = curve_stats([opt[n].get(d, 0.0) for d in pd], pd)
        b, _, _ = curve_stats([pess[n].get(d, 0.0) for d in pd], pd)
        out.append(f"| {n} | {a['cagr']:.1%} / {a['mdd']:.0%} | {b['cagr']:.1%} / {b['mdd']:.0%} |")
    out.append("\n**Daily correlations (as tested):**\n")
    out.append("| | " + " | ".join(NAMES) + " |\n|---|" + "---|" * len(NAMES))
    for a in NAMES:
        xa = [opt[a].get(d, 0.0) for d in pd]
        out.append(f"| {a} | " + " | ".join(f"{statistics.correlation(xa, [opt[b].get(d, 0.0) for d in pd]):+.2f}" for b in NAMES) + " |")

    def show(r, note=""):
        p_st, p_y, p_end = evaluate(r["w"], pess, pd)
        return (f"| {fmt(r['w'])} | {r['st']['cagr']:.1%} | {r['st']['mdd']:.1%} | {min(r['y'].values()):.1%} | "
                f"{r['st']['sharpe']:.2f} | {r['tr']['cagr']:.1%} | {r['te']['cagr']:.1%} | "
                f"**{p_st['cagr']:.1%} / {p_st['mdd']:.0%}** | ${3340 * r['end']:,.0f} |{note}")

    hdr = ("| CORE / SWING_M / SWING_Q / DAY / ODTE | CAGR | Max DD | Worst yr | Sharpe | 2019–22 | 2023–26 | "
           "Pessimistic CAGR / DD | $3,340 → |\n|---|---|---|---|---|---|---|---|---|")
    constraint_sets = [
        ("A. Without 0DTE (everything here is backtestable)", lambda w: w[4] == 0),
        ("B. 0DTE capped at 20% (its credit is an assumption)", lambda w: w[4] <= 2),
        ("C. Unconstrained (0DTE's assumed 3% credit dominates - do not trust)", lambda w: True),
    ]
    for title, allowed in constraint_sets:
        sub = [r for r in res if allowed(r["w"])]
        out.append(f"\n## {title}\n")
        out.append("**Frontier - best CAGR at each drawdown limit (full period, flattered by selection):**\n")
        out.append(hdr)
        seen = set()
        for cap in (-0.10, -0.12, -0.15, -0.18, -0.20, -0.25, -0.30):
            ok = [r for r in sub if r["st"]["mdd"] >= cap]
            if ok:
                best = max(ok, key=lambda r: r["st"]["cagr"])
                if best["w"] in seen:
                    continue
                seen.add(best["w"])
                out.append(show(best, f" DD ≤ {-cap:.0%}"))
        out.append("\n**Top 5 by Sharpe:**\n")
        out.append(hdr)
        for r in sorted(sub, key=lambda r: -r["st"]["sharpe"])[:5]:
            out.append(show(r))
        out.append("\n**Walk-forward - choose on 2019-2022 only, score on 2023-2026:**\n")
        out.append("| Rule used to choose (2019-22 only) | Chosen split | 2019-22 CAGR / DD | 2023-26 CAGR / DD (unseen) | "
                   "Pessimistic full-period CAGR / DD | QQQ 2023-26 |\n|---|---|---|---|---|---|")
        picks_wf = []
        for cap in (-0.15, -0.20, -0.25):
            ok = [r for r in sub if r["tr"]["mdd"] >= cap]
            if ok:
                picks_wf.append((f"Best CAGR, 2019-22 DD <= {-cap:.0%}", max(ok, key=lambda r: r["tr"]["cagr"])))
        picks_wf.append(("Best Sharpe on 2019-22", max(sub, key=lambda r: r["tr"]["sharpe"])))
        for lab, b in picks_wf:
            p_st, _, _ = evaluate(b["w"], pess, pd)
            out.append(f"| {lab} | {fmt(b['w'])} | {b['tr']['cagr']:.1%} / {b['tr']['mdd']:.0%} | "
                       f"{b['te']['cagr']:.1%} / {b['te']['mdd']:.0%} | {p_st['cagr']:.1%} / {p_st['mdd']:.0%} | "
                       f"{qte['cagr']:.1%} / {qte['mdd']:.0%} |")

    out.append("\n## Reference splits\n")
    out.append(hdr)
    for w in ((5, 5, 0, 0, 0), (4, 0, 3, 3, 0), (4, 4, 0, 0, 2), (3, 3, 2, 0, 2), (4, 3, 0, 1, 2), (3, 4, 1, 0, 2), (10, 0, 0, 0, 0), (0, 10, 0, 0, 0)):
        r = next(x for x in res if x["w"] == w)
        out.append(show(r))
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "mix_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
