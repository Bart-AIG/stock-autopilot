"""
Where should a 10-15% "Claude researches high-growth names" sleeve be funded from?
(Ryan, 2026-09-30: "pick the best overall split then add a 10-15% 'Claude researches
high-growth names' sleeve to the split. Figure out where its ratio should be taken from".)

Runs on GitHub Actions (FMP key). Pure standard library.

Base split = the live no-0DTE split: CORE 0 / SWING_M 30 / SWING_Q 70 / ODTE 0 (first run used 0/20/60/20).
(DAY is 0 everywhere since audit §15). The sleeves are rebuilt exactly as in mix_optimizer.py,
optimistic and pessimistic versions.

The research sleeve cannot be backtested (its picks do not exist yet), so it is bracketed by
three stand-ins that cover the plausible range:
  ARKK   a real, research-driven disruptive-growth fund: huge 2020, -75% 2021-22. The honest
         "high-growth picking done by a research team" record, good years and bad.
  MOM5   buy-and-hold of the 5 strongest names (12-month return) from the end-2018 large-cap
         pool, re-picked monthly: what "find the fastest growers" looks like when it works.
  CASH   T-bills: the research adds nothing and just sits idle.
For each stand-in, the sleeve is funded five ways (from SWING_M, from SWING_Q, from ODTE,
half SWING_M/half SWING_Q, pro-rata from all three) at 10% and 15%, monthly rebalance.
The donor to prefer is the one whose result is best ACROSS the three stand-ins, since we do
not know in advance which one the real sleeve will resemble.
Limits: 2019 -> today, one path; the stand-ins are proxies, not the sleeve itself.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

from backtest import NDX100_2018, SP100_2018
from combo_backtest import curve_stats
from intraday_backtest import fetch_5min, fetch_unadjusted
from momentum_sleeves_backtest import adj
from options_income_backtest import zero_dte
from robust_backtest import arrays, combine, full_ohlc, swing

HERE = Path(__file__).resolve().parent
SLEEVES = ["CORE", "SWING_M", "SWING_Q", "ODTE", "GROWTH"]
# Re-run 2026-09-30 on the split actually going live (0DTE removed: not executable). The first
# run (base 0/20/60/20 with ODTE) is in git history and audit section 16.
BASE = {"CORE": 0.0, "SWING_M": 0.30, "SWING_Q": 0.70, "ODTE": 0.0}


def donors(size):
    out = []
    for lab, take in (("from SWING_M", {"SWING_M": 1.0}), ("from SWING_Q", {"SWING_Q": 1.0}),
                      ("from ODTE", {"ODTE": 1.0}), ("half SWING_M / half SWING_Q", {"SWING_M": .5, "SWING_Q": .5}),
                      ("pro-rata from all", {k: v for k, v in BASE.items() if v})):
        if any(BASE[k] < size * v / sum(take.values()) - 1e-9 for k, v in take.items()):
            continue
        tot = sum(take.values())
        w = dict(BASE)
        for k, v in take.items():
            w[k] -= size * v / tot
        w["GROWTH"] = size
        out.append((lab, w))
    return out


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "BIL", "ARKK"]):
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

    core = {}
    for i in range(203, len(qd)):
        if Q[i - 2] > sum(Q[i - 201:i - 1]) / 200:
            lv = min(2.0, 0.25 / (rv[i - 1] or 1e-9))
            core[qd[i]] = lv * qr[qd[i]] - 0.00475 * lv / 252 - max(0.0, lv - 1) * br.get(qd[i], 0.0)
        else:
            core[qd[i]] = br.get(qd[i], 0.0)

    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    ranked = {}
    for m in me:
        k = qd.index(m)
        ranked[m] = [s for _, s in sorted(((A[s][m] / A[s][qd[k - 252]] - 1, s) for s in pool
                                           if s in A and m in A[s] and qd[k - 252] in A[s]), reverse=True)]
    ever = sorted({s for v in ranked.values() for s in v[:10]})
    sw = {}
    for s in ever:
        o = full_ohlc(s, key, "2016-06-01")
        if o and s in A:
            ds, C, H, L = arrays(o, A[s])
            if len(ds) > 260:
                sw[s] = swing(ds, C, H, L, None, lev=1, cash=br)
        time.sleep(0.05)
    tdates = [d for d in qd if d > me[0]]
    swing_m, mom5 = {}, {}
    for i, d in enumerate(qd):
        if d <= me[0]:
            continue
        r = ranked[[m for m in me if m < d][-1]]
        rs = [sw[s].get(d, 0.0) for s in r[:10] if s in sw]
        swing_m[d] = sum(rs) / len(rs) if rs else 0.0
        hs = [A[s][d] / A[s][qd[i - 1]] - 1 for s in r[:5] if d in A[s] and qd[i - 1] in A[s]]
        mom5[d] = sum(hs) / len(hs) if hs else 0.0
    swing_m_pess = {d: br.get(d, 0.0) + 0.75 * (r - br.get(d, 0.0)) for d, r in swing_m.items()}

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

    s5 = fetch_5min("SPY", key, log)
    sc_ = {s: s5[s][-1]["c"] for s in s5}
    odte3 = {d: (0.10 * v / 0.97 if v is not None else 0.0) for d, v in zero_dte(s5, sc_, 2.0, 0.03).items()}
    odte2 = {d: (0.10 * v / 0.98 if v is not None else 0.0) for d, v in zero_dte(s5, sc_, 2.0, 0.02).items()}

    ak = A.get("ARKK", {})
    arkk = {qd[i]: ak[qd[i]] / ak[qd[i - 1]] - 1 for i in range(1, len(qd)) if qd[i] in ak and qd[i - 1] in ak}
    proxies = {"ARKK": arkk, "MOM5": mom5, "CASH": br}

    start = max(min(core), min(swing_m), min(odte3), "2019-01-02")
    pd = [d for d in tdates if d >= start and d in core]
    train = [d for d in pd if d <= "2022-12-31"]
    test = [d for d in pd if d >= "2023-01-01"]
    opt = {"CORE": core, "SWING_M": swing_m, "SWING_Q": swing_q, "ODTE": odte3}
    pess = {"CORE": core, "SWING_M": swing_m_pess, "SWING_Q": swing_q_1550, "ODTE": odte2}

    def ev(w, sleeves, g, dates):
        pr = combine([w.get(n, 0.0) for n in SLEEVES], [sleeves.get(n, g) if n != "GROWTH" else g for n in SLEEVES], dates)
        return curve_stats(pr, dates)

    out = [f"# High-growth research sleeve — where to fund it — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Period {pd[0]} → {pd[-1]}. Base split CORE 0 / SWING_M 30 / SWING_Q 70 / ODTE 0 (no 0DTE), monthly rebalance.\n"]
    qs, qy, _ = curve_stats([qr[d] for d in pd], pd)
    out.append(f"**QQQ:** {qs['cagr']:.1%}/yr, max DD {qs['mdd']:.1%}, worst year {min(qy.values()):.1%}.\n")

    out.append("## The stand-ins alone\n")
    out.append("| Stand-in | CAGR | Max DD | Worst yr | 2019–22 | 2023–26 | Corr SWING_M | Corr SWING_Q | Corr ODTE |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    for n, g in proxies.items():
        st, y, _ = curve_stats([g.get(d, 0.0) for d in pd], pd)
        a, _, _ = curve_stats([g.get(d, 0.0) for d in train], train)
        b, _, _ = curve_stats([g.get(d, 0.0) for d in test], test)
        xg = [g.get(d, 0.0) for d in pd]
        cs = []
        for s in ("SWING_M", "SWING_Q", "ODTE"):
            try:
                cs.append(f"{statistics.correlation(xg, [opt[s].get(d, 0.0) for d in pd]):+.2f}")
            except statistics.StatisticsError:
                cs.append("n/a")
        out.append(f"| {n} | {st['cagr']:.1%} | {st['mdd']:.0%} | {min(y.values()):.1%} | {a['cagr']:.1%} | {b['cagr']:.1%} | "
                   + " | ".join(cs) + " |")

    base_o, by_o, _ = ev(BASE, opt, {}, pd)
    base_p, _, _ = ev(BASE, pess, {}, pd)
    out.append(f"\n**Base split without the sleeve:** as tested {base_o['cagr']:.1%} / {base_o['mdd']:.1%} "
               f"(worst yr {min(by_o.values()):.1%}); pessimistic {base_p['cagr']:.1%} / {base_p['mdd']:.1%}.\n")

    score = {}
    for size in (0.10, 0.15):
        out.append(f"## Sleeve at {size:.0%}\n")
        out.append("| Funded | Split CORE/SW_M/SW_Q/ODTE/GROWTH | Stand-in | As tested CAGR / DD / worst yr | 2019–22 | 2023–26 | Pessimistic CAGR / DD |")
        out.append("|---|---|---|---|---|---|---|")
        for lab, w in donors(size):
            wtxt = " / ".join(f"{w.get(n, 0) * 100:.1f}".rstrip("0").rstrip(".") for n in SLEEVES)
            for pn, g in proxies.items():
                st, y, _ = ev(w, opt, g, pd)
                a, _, _ = ev(w, opt, g, train)
                b, _, _ = ev(w, opt, g, test)
                p, _, _ = ev(w, pess, g, pd)
                out.append(f"| {lab} | {wtxt} | {pn} | {st['cagr']:.1%} / {st['mdd']:.1%} / {min(y.values()):.1%} | "
                           f"{a['cagr']:.1%} | {b['cagr']:.1%} | {p['cagr']:.1%} / {p['mdd']:.1%} |")
                sc = score.setdefault((size, lab), [])
                sc.append((p["cagr"], p["mdd"], st["cagr"], st["mdd"]))
        out.append("")

    out.append("## Ranking of funding sources (averaged over the three stand-ins)\n")
    out.append("| Size | Funded | Avg pessimistic CAGR | Worst pessimistic DD | Avg as-tested CAGR | Worst as-tested DD | Return / |DD| (pess.) |")
    out.append("|---|---|---|---|---|---|---|")
    rows = []
    for (size, lab), v in score.items():
        pc = statistics.mean(x[0] for x in v)
        pdd = min(x[1] for x in v)
        oc = statistics.mean(x[2] for x in v)
        odd = min(x[3] for x in v)
        rows.append((size, -(pc / abs(pdd)), lab, pc, pdd, oc, odd))
    for size, neg, lab, pc, pdd, oc, odd in sorted(rows):
        out.append(f"| {size:.0%} | {lab} | {pc:.1%} | {pdd:.1%} | {oc:.1%} | {odd:.1%} | {-neg:.2f} |")
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "growth_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
