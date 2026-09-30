"""
Factor horse race — which stock-ranking signal best predicts next month's winners inside
SPY and QQQ?  (Ryan, 2026-09-29: "is there a better correlation to use when trying to
pick stock in spy and qqq to run this test with".)

Runs on GitHub Actions (FMP key). Pure standard library.

Universe (no hindsight): S&P 100 and Nasdaq-100 as of end-2018, ranked monthly from
end-2018 to today; also the two pooled. Each month-end every name is scored on each
signal; we then measure
  IC        Spearman rank correlation between the score and the NEXT month's return,
            averaged over months, with a t-stat (mean / std * sqrt(n)) and % months > 0.
            |t| > 2 is the usual bar for "not luck".
  TOP10     equal-weight the 10 best-scored names for the next month (5 bp x turnover).
  SPREAD    top-decile minus bottom-decile next-month return, annualised.

Signals (published; parameters are the papers' defaults, not tuned):
  MOM12        trailing 12-month return
  MOM12_1      12-month return skipping the last month (Jegadeesh & Titman 1993)
  MOM6_1       6-month return skipping the last month
  RISKADJ_MOM  MOM12_1 / 12-month daily volatility
  RESID_MOM    12-1 residual return vs the index ETF, scaled by residual volatility
               (Blitz, Huij & Martens 2011)
  SMOOTH_MOM   MOM12_1 with the "frog-in-the-pan" smoothness filter: top 30 by MOM12_1,
               then prefer the smallest information discreteness (Da, Gurun & Warachka 2014)
  HIGH52       price / 52-week high (George & Hwang 2004)
  REV1         minus last month's return (short-term reversal)
  LOWVOL       minus 12-month daily volatility (low-volatility anomaly)
  TREND_MOM    MOM12_1, only names above their 200-day SMA
  COMPOSITE    average rank of MOM12_1, HIGH52 and RESID_MOM
  GROSS_PROF   gross profit / total assets (Novy-Marx 2013) - if FMP serves statements
  EARN_SURP    latest quarterly EPS surprise within 90 days (post-earnings drift) - if served

Limits: ~93 months per pool; testing many signals means the best one is partly luck,
so read the t-stats, not only the top line. Fundamentals are lagged 90 days after the
fiscal period end to avoid look-ahead. Taxes ignored.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from backtest import BASE, NDX100_2018, SP100_2018, _get, stats

HERE = Path(__file__).resolve().parent
COST = 5e-4
START = "2016-06-01"


def adj(sym, key):
    data = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    if not isinstance(data, list) or not data:
        return None
    rows = sorted(((r["date"][:10], float(r.get("adjClose") or r.get("close") or 0)) for r in data))
    return [(d, p) for d, p in rows if p > 0]


def fundamentals(sym, key, log):
    """[(available_date, gross_profit/total_assets)] or None."""
    inc = _get(f"{BASE}/income-statement?symbol={sym}&period=annual&limit=15&apikey={key}")
    bal = _get(f"{BASE}/balance-sheet-statement?symbol={sym}&period=annual&limit=15&apikey={key}")
    if not isinstance(inc, list) or not isinstance(bal, list) or not inc or not bal:
        return None
    ta = {r["date"][:10]: r.get("totalAssets") for r in bal if r.get("date")}
    out = []
    for r in inc:
        d = (r.get("date") or "")[:10]
        gp, a = r.get("grossProfit"), ta.get(d)
        if d and gp is not None and a:
            avail = (date.fromisoformat(d) + timedelta(days=90)).isoformat()
            out.append((avail, gp / a))
    return sorted(out) or None


def earnings(sym, key):
    e = _get(f"{BASE}/earnings?symbol={sym}&limit=60&apikey={key}")
    if not isinstance(e, list) or not e:
        return None
    out = []
    for r in e:
        a, est = r.get("epsActual"), r.get("epsEstimated")
        if a is not None and est not in (None, 0):
            out.append((r["date"][:10], (a - est) / abs(est)))
    return sorted(out) or None


def spearman(x, y):
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for k, i in enumerate(o):
            r[i] = k
        return r
    return statistics.correlation(rk(x), rk(y)) if len(x) >= 10 else None


def scores_at(sym_ser, idx_of, t_date, etf_ret):
    """All price-based signals for one name at month-end t_date."""
    dates, px = sym_ser
    j = idx_of.get(t_date)
    if j is None or j < 260:
        return None
    p = px
    r = [p[k] / p[k - 1] - 1 for k in range(j - 251, j + 1)]
    vol = statistics.pstdev(r) * math.sqrt(252) or 1e-9
    m12 = p[j] / p[j - 252] - 1
    m12_1 = p[j - 21] / p[j - 252] - 1
    m6_1 = p[j - 21] / p[j - 126] - 1
    win = r[:-21]
    pos = sum(1 for x in win if x > 0) / len(win)
    neg = sum(1 for x in win if x < 0) / len(win)
    idisc = (1 if m12_1 > 0 else -1) * (neg - pos)
    mk = [etf_ret.get(dates[k]) for k in range(j - 251, j - 20)]
    pairs = [(a, b) for a, b in zip(win, mk) if b is not None]
    resid_score = None
    if len(pairs) > 150:
        xs, ys = [b for _, b in pairs], [a for a, _ in pairs]
        mx, my = statistics.mean(xs), statistics.mean(ys)
        vx = sum((x - mx) ** 2 for x in xs)
        beta = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / vx if vx else 1.0
        res = [y - beta * x for x, y in zip(xs, ys)]
        sd = statistics.pstdev(res) or 1e-9
        resid_score = sum(res) / (sd * math.sqrt(len(res)))
    return {
        "MOM12": m12, "MOM12_1": m12_1, "MOM6_1": m6_1, "RISKADJ_MOM": m12_1 / vol,
        "RESID_MOM": resid_score, "HIGH52": p[j] / max(p[j - 251:j + 1]),
        "REV1": -(p[j] / p[j - 21] - 1), "LOWVOL": -vol,
        "TREND_MOM": m12_1 if p[j] > sum(p[j - 199:j + 1]) / 200 else None,
        "_idisc": idisc,
    }


SIGNALS = ["MOM12", "MOM12_1", "MOM6_1", "RISKADJ_MOM", "RESID_MOM", "SMOOTH_MOM", "HIGH52",
           "REV1", "LOWVOL", "TREND_MOM", "COMPOSITE", "GROSS_PROF", "EARN_SURP"]


def latest_before(series, d, max_age_days=None):
    v = None
    for a, x in series:
        if a <= d:
            v = (a, x)
        else:
            break
    if v and max_age_days is not None and (date.fromisoformat(d) - date.fromisoformat(v[0])).days > max_age_days:
        return None
    return v[1] if v else None


def run_pool(label, names, etf, data, fund, earn, out):
    etf_dates, etf_px = data[etf]
    etf_ret = {etf_dates[k]: etf_px[k] / etf_px[k - 1] - 1 for k in range(1, len(etf_dates))}
    month_ends = []
    for k in range(len(etf_dates)):
        if k == len(etf_dates) - 1 or etf_dates[k][:7] != etf_dates[k + 1][:7]:
            month_ends.append(etf_dates[k])
    month_ends = [m for m in month_ends if m >= "2018-12-01"]
    idx = {s: {d: i for i, d in enumerate(data[s][0])} for s in names if s in data}
    ic = {s: [] for s in SIGNALS}
    port = {s: [] for s in SIGNALS}
    spread = {s: [] for s in SIGNALS}
    held = {s: [] for s in SIGNALS}
    etf_m, used = [], []
    for mi in range(len(month_ends) - 1):
        t, t1 = month_ends[mi], month_ends[mi + 1]
        rows = {}
        for s in idx:
            sc = scores_at(data[s], idx[s], t, etf_ret)
            if not sc:
                continue
            j1 = idx[s].get(t1)
            if j1 is None:
                continue
            sc["_next"] = data[s][1][j1] / data[s][1][idx[s][t]] - 1
            if s in fund:
                sc["GROSS_PROF"] = latest_before(fund[s], t)
            if s in earn:
                sc["EARN_SURP"] = latest_before(earn[s], t, 90)
            rows[s] = sc
        if len(rows) < 30:
            continue
        # derived signals
        by = sorted(rows, key=lambda s: rows[s]["MOM12_1"], reverse=True)[:30]
        for s in rows:
            rows[s]["SMOOTH_MOM"] = -rows[s]["_idisc"] if s in by else None
        for sig in ("MOM12_1", "HIGH52", "RESID_MOM"):
            vals = sorted((rows[s][sig], s) for s in rows if rows[s].get(sig) is not None)
            for k, (_, s) in enumerate(vals):
                rows[s].setdefault("_rk", []).append(k / max(1, len(vals) - 1))
        for s in rows:
            rk = rows[s].get("_rk", [])
            rows[s]["COMPOSITE"] = sum(rk) / len(rk) if len(rk) == 3 else None
        etf_m.append(data[etf][1][idx_etf(data, etf, t1)] / data[etf][1][idx_etf(data, etf, t)] - 1)
        used.append(t1)
        for sig in SIGNALS:
            have = [(rows[s][sig], rows[s]["_next"], s) for s in rows if rows[s].get(sig) is not None]
            if len(have) < 10:
                port[sig].append(None)
                continue
            c = spearman([h[0] for h in have], [h[1] for h in have])
            if c is not None and sig != "SMOOTH_MOM":
                ic[sig].append(c)
            have.sort(key=lambda h: h[0], reverse=True)
            top = [h[2] for h in have[:10]]
            r = sum(rows[s]["_next"] for s in top) / len(top)
            turn = len(set(top) - set(held[sig])) / 10 if held[sig] else 1.0
            port[sig].append(r - 2 * COST * turn)
            held[sig] = top
            if len(have) >= 30 and sig != "SMOOTH_MOM":
                d = len(have) // 10
                spread[sig].append(sum(h[1] for h in have[:d]) / d - sum(h[1] for h in have[-d:]) / d)
    n_m = len(etf_m)
    dates = used
    eq, ec = [1.0], [1.0]
    for r in etf_m:
        ec.append(ec[-1] * (1 + r))
    se = stats(ec[1:], dates)
    out.append(f"## {label} — {len(idx)} names, benchmark {etf}, {dates[0][:7]} → {dates[-1][:7]} ({n_m} months)\n")
    out.append(f"{etf} buy & hold over the same months: CAGR {se['cagr']:.1%}, max DD {se['mdd']:.0%}.\n")
    out.append("| Signal | Mean IC | IC t-stat | IC > 0 | Top-10 CAGR | vs " + etf + " | Top-10 max DD | Top-minus-bottom decile / yr | Months |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    table = []
    for sig in SIGNALS:
        rs = [x for x in port[sig] if x is not None]
        if len(rs) < 24:
            table.append((sig, None))
            continue
        cur = [1.0]
        for x in port[sig]:
            cur.append(cur[-1] * (1 + (x or 0.0)))
        st = stats(cur[1:], dates[:len(cur) - 1])
        icv = ic[sig]
        m_ic = statistics.mean(icv) if icv else float("nan")
        t_ic = (m_ic / statistics.stdev(icv) * math.sqrt(len(icv))) if len(icv) > 2 and statistics.stdev(icv) else float("nan")
        pos = sum(1 for x in icv if x > 0) / len(icv) if icv else float("nan")
        spr = statistics.mean(spread[sig]) * 12 if spread[sig] else float("nan")
        table.append((sig, (m_ic, t_ic, pos, st, spr, len(rs))))
    for sig, v in sorted(table, key=lambda x: -(x[1][3]["cagr"] if x[1] else -9)):
        if not v:
            out.append(f"| {sig} | n/a (data not served) | | | | | | | |")
            continue
        m_ic, t_ic, pos, st, spr, n = v
        ic_txt = "—" if sig == "SMOOTH_MOM" else f"{m_ic:+.3f}"
        t_txt = "—" if sig == "SMOOTH_MOM" else f"{t_ic:+.1f}"
        p_txt = "—" if sig == "SMOOTH_MOM" else f"{pos:.0%}"
        s_txt = "—" if sig == "SMOOTH_MOM" or math.isnan(spr) else f"{spr:+.1%}"
        out.append(f"| {sig} | {ic_txt} | {t_txt} | {p_txt} | {st['cagr']:.1%} | {st['cagr'] - se['cagr']:+.1%} | "
                   f"{st['mdd']:.0%} | {s_txt} | {n} |")
    out.append("")


_ETF_IDX = {}


def idx_etf(data, etf, d):
    if etf not in _ETF_IDX:
        _ETF_IDX[etf] = {x: i for i, x in enumerate(data[etf][0])}
    return _ETF_IDX[etf][d]


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    names = sorted(set(SP100_2018) | set(NDX100_2018))
    data, fund, earn = {}, {}, {}
    fund_ok = earn_ok = True
    for n, s in enumerate(names + ["SPY", "QQQ"]):
        ser = adj(s, key)
        if ser:
            data[s] = ([d for d, _ in ser], [p for _, p in ser])
        if s not in ("SPY", "QQQ"):
            if fund_ok:
                f = fundamentals(s, key, log)
                if f:
                    fund[s] = f
                elif n == 0:
                    fund_ok = False
                    log.append("financial statements not served on this FMP tier: GROSS_PROF skipped")
            if earn_ok:
                e = earnings(s, key)
                if e:
                    earn[s] = e
                elif n == 0:
                    earn_ok = False
                    log.append("earnings history not served on this FMP tier: EARN_SURP skipped")
        if n % 40 == 0:
            print(f"fetched {n}/{len(names) + 2}", flush=True)
        time.sleep(0.1)
    log.append(f"prices {len(data)}, fundamentals {len(fund)}, earnings {len(earn)}")
    out = [f"# Factor horse race — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           "Which ranking signal best predicts next month's winners inside the S&P 100 / Nasdaq-100 "
           "(end-2018 lists, no hindsight)? Sorted by top-10 portfolio CAGR; judge by the IC t-stat "
           "(|t| > 2 is the usual bar for a real signal).\n"]
    run_pool("S&P 100 (end-2018)", [s for s in SP100_2018 if s in data], "SPY", data, fund, earn, out)
    run_pool("Nasdaq-100 (end-2018)", [s for s in NDX100_2018 if s in data], "QQQ", data, fund, earn, out)
    run_pool("Both pooled", [s for s in names if s in data], "QQQ", data, fund, earn, out)
    out.append("## Data log\n")
    out.extend(f"- {x}" for x in log)
    (HERE / "factors_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
