"""Do the valuation and disruption grades improve SWING_M? (Ryan, live turn 2026-10-02:
"lets test C to see if we learn anything interesting".)

SWING_M = each month's top-10 names by 12-month return (S&P 100 + Nasdaq 100 as of 2018,
159 names, so no hindsight in the universe), each traded on the SWING_UNION rules at 1x,
exactly as mix_optimizer.py builds it. This script re-runs it with filters that skip a name
and take the next-ranked one instead, so every variant holds 10 names:

  BASE          no filter (the live rule)
  NO_DISRUPTED  skip names graded BEING DISRUPTED
  NO_AT_RISK    skip AT RISK and BEING DISRUPTED
  NO_EXPENSIVE  skip valuation EXPENSIVE (> 25% above its own history), HIGH/MED confidence
  NO_RICH       skip RICH and EXPENSIVE, HIGH/MED confidence
  PREFER_CHEAP  among the top 20, take the 10 with the best valuation tier (momentum breaks ties)

POINT IN TIME: at each month-end the grades are computed by the PRODUCTION functions
(valuation.value, disruption.score) from annual statements whose filing date is on or before
that month-end, priced at that day's close. What is NOT point in time and is therefore left
out: analysts' revenue forecasts and price targets (no history), the research notes. The
latest filed ANNUAL statement stands in for trailing-12-month numbers, so fundamentals lag
by up to a year. The sector/industry label is today's.

Also measures, for every month's top-20 candidates, the next month's buy-and-hold return
by grade bucket: does the grade predict anything at all, filter or no filter?

Network: FMP (key in FMP_API_KEY). Writes grades_filter_results.md.
"""
from __future__ import annotations

import json
import os
import statistics
import sys
import time
from collections import defaultdict
from pathlib import Path

import disruption
import valuation
from backtest import NDX100_2018, SP100_2018
from combo_backtest import curve_stats
from momentum_sleeves_backtest import adj
from robust_backtest import arrays, full_ohlc, swing

HERE = Path(__file__).resolve().parent
OUT = HERE / "grades_filter_results.md"
CACHE = HERE / "logs" / "grades_fund_cache.json"
TOP_N, POOL_N = 10, 20


def fetch_fundamentals(sym, key):
    g = valuation._get
    prof = g(f"profile?symbol={sym}", key) or []
    out = {"profile": prof[0] if isinstance(prof, list) and prof else {}}
    for name, path in (("inc", "income-statement"), ("bal", "balance-sheet-statement"),
                       ("cf", "cash-flow-statement"), ("rat", "ratios"), ("km", "key-metrics")):
        d = g(f"{path}?symbol={sym}&period=annual&limit=20", key)
        out[name] = d if isinstance(d, list) else []
        time.sleep(0.12)
    return out


def point_in_time(f, asof, raw_close):
    """valuation.value() + disruption.score() inputs as of `asof`, or None."""
    filed = {}
    for r in f["inc"]:
        fd = (r.get("filingDate") or r.get("acceptedDate") or "")[:10]
        if fd and fd <= asof:
            filed[str(r.get("fiscalYear"))] = r
    if len(filed) < 5:
        return None
    years = sorted(filed)[-10:]
    inc = [filed[y] for y in years]
    last = inc[-1]
    fy = str(last.get("fiscalYear"))
    bal = next((r for r in f["bal"] if str(r.get("fiscalYear")) == fy), {})
    cf = next((r for r in f["cf"] if str(r.get("fiscalYear")) == fy), {})
    shares = last.get("weightedAverageShsOutDil") or last.get("weightedAverageShsOut")
    rev, ni = last.get("revenue") or 0, last.get("netIncome")
    if not (shares and rev and raw_close):
        return None
    mcap = raw_close * shares
    debt = (bal.get("totalDebt") or 0)
    cashv = (bal.get("cashAndCashEquivalents") or 0)
    ev = mcap + debt - cashv
    eq = bal.get("totalStockholdersEquity")
    ebitda = last.get("ebitda")
    fcf, ocf = cf.get("freeCashFlow"), cf.get("operatingCashFlow")

    def div(a, b):
        return a / b if a and b and b > 0 else None
    ttm = {"pe": div(mcap, ni), "pb": div(mcap, eq), "pfcf": div(mcap, fcf), "pocf": div(mcap, ocf),
           "ev_sales": div(ev, rev), "ev_ebitda": div(ev, ebitda),
           "ebitda_margin": (ebitda / rev) if ebitda is not None and rev else None,
           "roe": (ni / eq) if ni is not None and eq else None}
    hist = {}
    for r in f["rat"] + f["km"]:
        y = str(r.get("fiscalYear"))
        if y in years:
            hist.setdefault(y, {}).update(r)
    p = f["profile"]
    v_in = {"symbol": None, "sector": p.get("sector"), "industry": p.get("industry"),
            "price": raw_close, "mcap": mcap, "ev": ev, "ttm": ttm,
            "annual": [hist[y] for y in years if y in hist], "target_median": None}
    return v_in, inc


def grade(sym, f, asof, raw_close):
    pit = point_in_time(f, asof, raw_close)
    if not pit:
        return None
    v_in, inc = pit
    v_in["symbol"] = sym
    v = valuation.value(v_in)
    d = disruption.score(inc, [], v["profile"], v)
    return {"val": v["grade"], "val_conf": v["confidence"], "gap": v["gap_pct"], "dis": d["label"]}


def keep(variant, g):
    if g is None:
        return True                      # ungradable: never filtered out
    if variant == "NO_DISRUPTED":
        return g["dis"] != "BEING DISRUPTED"
    if variant == "NO_AT_RISK":
        return g["dis"] not in ("AT RISK", "BEING DISRUPTED")
    if variant == "NO_EXPENSIVE":
        return not (g["val"] == "EXPENSIVE" and g["val_conf"] != "LOW")
    if variant == "NO_RICH":
        return not (g["val"] in ("RICH", "EXPENSIVE") and g["val_conf"] != "LOW")
    return True


VARIANTS = ["BASE", "NO_DISRUPTED", "NO_AT_RISK", "NO_EXPENSIVE", "NO_RICH", "PREFER_CHEAP"]


def main():
    key = os.environ.get("FMP_API_KEY", "").strip() or sys.exit("FMP_API_KEY not set")
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "BIL"]):
        a = adj(s, key)
        if a:
            A[s] = a
        time.sleep(0.08)
        if n % 40 == 0:
            print("prices", n, flush=True)
    qd = sorted(d for d in A["QQQ"] if d in A["BIL"])
    br = {qd[i]: A["BIL"][qd[i]] / A["BIL"][qd[i - 1]] - 1 for i in range(1, len(qd))}
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    ranked = {}
    for m in me:
        k = qd.index(m)
        sc = sorted(((A[s][m] / A[s][qd[k - 252]] - 1, s) for s in pool
                     if s in A and m in A[s] and qd[k - 252] in A[s]), reverse=True)
        ranked[m] = [s for _, s in sc[:POOL_N]]
    cand = sorted({s for v in ranked.values() for s in v})
    print(len(cand), "candidate names", flush=True)

    CACHE.parent.mkdir(exist_ok=True)
    fund = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    ohlc, sw = {}, {}
    for n, s in enumerate(cand):
        if s not in fund:
            fund[s] = fetch_fundamentals(s, key)
        o = full_ohlc(s, key, "2016-06-01")
        if o and s in A:
            ohlc[s] = o
            ds, C, H, L = arrays(o, A[s])
            if len(ds) > 260:
                sw[s] = swing(ds, C, H, L, None, lev=1, cash=br)
        if n % 10 == 0:
            print("names", n, flush=True)
            CACHE.write_text(json.dumps(fund))
        time.sleep(0.05)
    CACHE.write_text(json.dumps(fund))

    grades = {}
    for m in me:
        for s in ranked[m]:
            o = ohlc.get(s, {})
            raw = o.get(m, [None] * 4)[3] if m in o else None
            grades[(m, s)] = grade(s, fund.get(s, {"inc": [], "bal": [], "cf": [], "rat": [], "km": [],
                                                   "profile": {}}), m, raw) if raw else None

    picks = {v: {} for v in VARIANTS}
    for m in me:
        r = ranked[m]
        for v in VARIANTS:
            if v == "PREFER_CHEAP":
                order = sorted(range(len(r)), key=lambda i: (valuation.rank_tier(
                    {"grade": grades[(m, r[i])]["val"], "confidence": grades[(m, r[i])]["val_conf"]}
                    if grades[(m, r[i])] else None), i))
                picks[v][m] = [r[i] for i in order[:TOP_N]]
            else:
                picks[v][m] = [s for s in r if keep(v, grades[(m, s)])][:TOP_N]

    tdates = [d for d in qd if d > me[0]]
    series = {}
    for v in VARIANTS:
        out = {}
        for d in tdates:
            b = picks[v][[m for m in me if m < d][-1]]
            rs = [sw[s].get(d, 0.0) for s in b if s in sw]
            out[d] = sum(rs) / len(rs) if rs else 0.0
        series[v] = out

    start = "2019-01-02"
    pdates = [d for d in tdates if d >= start]

    def stats(v, dates):
        st, yrs, end = curve_stats([series[v][d] for d in dates], dates)
        return st, yrs

    # Forward 1-month buy-and-hold return of each top-20 candidate, by grade bucket.
    fwd = defaultdict(list)
    for i, m in enumerate(me[:-1]):
        nxt = me[i + 1]
        for s in ranked[m]:
            if s in A and m in A[s] and nxt in A[s]:
                ret = A[s][nxt] / A[s][m] - 1
                g = grades[(m, s)]
                fwd[("dis", g["dis"] if g else "N/A")].append(ret)
                vb = (g["val"] if g and g["val_conf"] != "LOW" else "N/A or LOW")
                fwd[("val", vb)].append(ret)
                fwd[("all", "all")].append(ret)

    lines = ["# Do the valuation and disruption grades improve SWING_M?", "",
             f"Run {time.strftime('%Y-%m-%d %H:%MZ', time.gmtime())}. Universe: S&P 100 + Nasdaq 100 as "
             f"of 2018 ({len(pool)} names). Period {pdates[0]} to {pdates[-1]}. Grades computed point in time "
             "by the production valuation.py / disruption.py from annual statements filed by each month-end; "
             "no analyst forecasts, targets or research notes (no history exists). A filtered name is "
             "replaced by the next-ranked one, so every variant holds 10.", "",
             "## SWING_M with each filter (1x, close-to-close, as in mix_optimizer.py)", "",
             "| Variant | CAGR | Max DD | Sharpe | 2019-22 CAGR | 2023-26 CAGR | Months a pick changed |",
             "|---|---|---|---|---|---|---|"]
    tr = [d for d in pdates if d <= "2022-12-31"]
    te = [d for d in pdates if d >= "2023-01-01"]
    for v in VARIANTS:
        st, _ = stats(v, pdates)
        st_tr, _ = stats(v, tr)
        st_te, _ = stats(v, te)
        changed = sum(1 for m in me if set(picks[v][m]) != set(picks["BASE"][m]))
        lines.append(f"| {v} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st.get('sharpe', 0):.2f} | "
                     f"{st_tr['cagr']:.1%} | {st_te['cagr']:.1%} | {changed} of {len(me)} |")
    lines += ["", "## Next-month buy-and-hold return of the top-20 momentum names, by grade", "",
              "| Grade | n | Mean | Median | Share positive |", "|---|---|---|---|---|"]
    for k in sorted(fwd):
        xs = fwd[k]
        lines.append(f"| {k[0]}: {k[1]} | {len(xs)} | {statistics.mean(xs):+.2%} | "
                     f"{statistics.median(xs):+.2%} | {sum(x > 0 for x in xs) / len(xs):.0%} |")
    lines += ["", "## How often each grade appeared among BASE picks", ""]
    cnt = defaultdict(int)
    for m in me:
        for s in picks["BASE"][m]:
            g = grades[(m, s)]
            cnt[("dis", g["dis"] if g else "N/A")] += 1
            cnt[("val", g["val"] if g else "N/A")] += 1
    lines.append(", ".join(f"{k[0]} {k[1]}: {n}" for k, n in sorted(cnt.items())))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
