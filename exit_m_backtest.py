"""
Exit backtest, part 2 — the SWING_M profit exit on REAL intraday prices.
(Ryan, live turn 2026-10-05: "agreed with 1. then lets test recommendation 2".)

Part 1 (exit_backtest.py / exit_results.md) found the multi-variable PROFIT exit ("exhaustion
score", K points of 7) worth a follow-up on SWING_M only: on daily bars it cut the sleeve's
max drawdown from -21% to -13/-16% for ~3 points of return. Daily bars cannot say WHEN in the
day the trigger is crossed, so this re-runs it on 5-minute bars:

  * every run is simulated at 09:35, 10:00, 10:30 ... 15:00 ET at that moment's price; a sell
    fires at the first check whose price is at or above the day's trigger, filled at that
    price less 0.05%;
  * the close decision (the current RSI2 / IBS / turn-of-month rules) is taken at 15:50 on
    the 15:45 bar, as live - for BASE and every variant alike, so the comparison is fair;
  * 5-minute bars are fetched only for the months each name was one of the ten picks; days
    without bars fall back to the daily-bar proxy and are counted in the data log.

Formulas, thresholds and K values are UNCHANGED from part 1 (no re-tuning on this data).
The variant is chosen on 2019-2022 and scored on 2023-2026, and the portfolio rows combine
it with SWING_Q at 70% (current rules, true intraday, as tested in part 1).
"""

from __future__ import annotations

import os
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from backtest import BASE, NDX100_2018, SP100_2018, _get
from combo_backtest import curve_stats
from exit_backtest import CHECKS, START, Series, cell, label, simulate, tstats
from robust_backtest import combine

HERE = Path(__file__).resolve().parent


def load(sym, key):
    """Series on the dividend-adjusted scale plus {date: adj/raw factor}."""
    data = _get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    adjd = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    if not isinstance(data, list) or not isinstance(adjd, list):
        return None
    a = {r["date"][:10]: float(r.get("adjClose") or r.get("close") or 0) for r in adjd}
    rows = {}
    for r in data:
        d = r["date"][:10]
        if d in a and a[d] and r.get("close") and r.get("high") and r.get("low") and r.get("open"):
            f = a[d] / float(r["close"])
            rows[d] = (float(r["open"]) * f, float(r["high"]) * f, float(r["low"]) * f, a[d], f)
    ds = sorted(rows)
    if len(ds) < 300:
        return None
    s = Series(ds, [rows[d][0] for d in ds], [rows[d][1] for d in ds], [rows[d][2] for d in ds],
               [rows[d][3] for d in ds])
    s.fac = {d: rows[d][4] for d in ds}
    return s


def bars5(sym, key, a, b, log):
    """{date: [5-minute bars 09:30-15:55]} between dates a and b (inclusive), full sessions only."""
    days = {}
    d, end = date.fromisoformat(a), date.fromisoformat(b)
    while d <= end:
        e = min(d + timedelta(days=6), end)
        data = _get(f"{BASE}/historical-chart/5min?symbol={sym}&from={d}&to={e}&apikey={key}")
        if isinstance(data, list):
            for r in data:
                ts = r["date"]
                days.setdefault(ts[:10], []).append(
                    {"t": ts[11:16], "h": float(r["high"]), "l": float(r["low"]), "c": float(r["close"])})
        else:
            log.append(f"{sym} 5min {d}: {str(data)[:60]}")
        d = e + timedelta(days=1)
        time.sleep(0.12)
    out = {}
    for k, v in days.items():
        seen, uniq = set(), []
        for x in sorted((x for x in v if "09:30" <= x["t"] <= "15:55"), key=lambda x: x["t"]):
            if x["t"] not in seen:
                seen.add(x["t"]), uniq.append(x)
        if len(uniq) >= 70:
            out[k] = uniq
    return out


def intraday_arrays(s, b5):
    """X/XH/XL at 15:45 (15:50 decision) and the check prices, on the adjusted scale."""
    X, XH, XL, intra = list(s.C), list(s.H), list(s.L), {}
    for i, d in enumerate(s.dates):
        bars = b5.get(d)
        if not bars:
            continue
        f = s.fac[d]
        upto = [x for x in bars if x["t"] <= "15:45"]
        if len(upto) >= 60:
            X[i], XH[i], XL[i] = upto[-1]["c"] * f, max(x["h"] for x in upto) * f, min(x["l"] for x in upto) * f
        bt = {x["t"]: x["c"] * f for x in bars}
        pts = [bt[t] for t in CHECKS if t in bt]
        if len(pts) >= 8:
            intra[d] = pts
    return X, XH, XL, intra


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    S = {}
    for n, sym in enumerate(pool + ["QQQ", "BIL"]):
        s = load(sym, key)
        if s:
            S[sym] = s
        if n % 40 == 0:
            print(f"daily {n}/{len(pool) + 2}", flush=True)
        time.sleep(0.08)
    Q, B = S["QQQ"], S["BIL"]
    qd = [d for d in Q.dates if d in B.ix]
    br = {d: B.C[B.ix[d]] / B.C[B.ix[d] - 1] - 1 for d in qd if B.ix[d] > 0}
    qr = {d: Q.C[Q.ix[d]] / Q.C[Q.ix[d] - 1] - 1 for d in qd if Q.ix[d] > 0}
    mkt_below = {Q.dates[i] for i in range(201, len(Q.dates)) if Q.C[i - 1] < sum(Q.C[i - 200:i]) / 200}

    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}
    for m in me:
        b = qd[qd.index(m) - 252]
        sc = [(S[x].C[S[x].ix[m]] / S[x].C[S[x].ix[b]] - 1, x) for x in pool
              if x in S and m in S[x].ix and b in S[x].ix]
        picks[m] = [x for _, x in sorted(sc, reverse=True)[:10]]
    tdates = [d for d in qd if d > me[0]]
    pick_of = {d: picks[[m for m in me if m < d][-1]] for d in tdates}

    # pick windows: for each symbol, the trading days it is a pick (+5 sessions after, for exits)
    windows = {}
    for j, m in enumerate(me[:-1]):
        a = qd[qd.index(m) + 1]
        b = me[j + 1] if j + 1 < len(me) else qd[-1]
        for x in picks[m]:
            windows.setdefault(x, []).append((a, b))
    for j, m in enumerate(me):
        if m == me[-1]:
            a = qd[min(qd.index(m) + 1, len(qd) - 1)]
            for x in picks[m]:
                windows.setdefault(x, []).append((a, qd[-1]))

    sims = {}
    variants = [None, 2, 3, 4, 5]
    covered = total = 0
    for n, x in enumerate(sorted(windows)):
        if x not in S:
            log.append(f"{x}: no daily data")
            continue
        s = S[x]
        b5 = {}
        merged = []
        for a, b in sorted(windows[x]):
            if merged and a <= (date.fromisoformat(merged[-1][1]) + timedelta(days=5)).isoformat():
                merged[-1] = (merged[-1][0], max(merged[-1][1], b))
            else:
                merged.append((a, b))
        for a, b in merged:
            b5.update(bars5(x, key, a, b, log))
        X, XH, XL, intra = intraday_arrays(s, b5)
        pick_days = [d for d in tdates if x in pick_of[d]]
        total += len(pick_days)
        covered += sum(1 for d in pick_days if d in intra)
        for kp in variants:
            r_true, t_true = simulate(s, kp, None, lev=1, cash=br, mkt_below=mkt_below, X=X, XH=XH, XL=XL, intraday=intra)
            r_prox, t_prox = simulate(s, kp, None, lev=1, cash=br, mkt_below=mkt_below)
            keep = lambda t: [z for z in t if z["in"] in pick_of and x in pick_of[z["in"]]]
            sims[(x, kp)] = (r_true, keep(t_true), r_prox, keep(t_prox))
        print(f"intraday {n + 1}/{len(windows)} {x}: {len(b5)} sessions", flush=True)
    log.insert(0, f"pick-days with 5-minute bars: {covered}/{total} ({covered / max(total, 1):.0%}); the rest use the daily-bar proxy")

    # SWING_Q at 70%: current rules, true intraday, as part 1
    from intraday_backtest import fetch_5min, fetch_unadjusted
    q5 = fetch_5min("QQQ", key, log)
    raw_q = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    QX, QXH, QXL = list(Q.C), list(Q.H), list(Q.L)
    for i, d in enumerate(Q.dates):
        bars = q5.get(d)
        if bars and d in raw_q:
            f = Q.C[i] / raw_q[d]
            upto = [y for y in bars if y["t"] <= "15:45"]
            if len(upto) >= 60:
                QX[i], QXH[i], QXL[i] = upto[-1]["c"] * f, max(y["h"] for y in upto) * f, min(y["l"] for y in upto) * f
    swing_q, _ = simulate(Q, None, None, lev=2, cash=br, X=QX, XH=QXH, XL=QXL)

    res = {}
    for kp in variants:
        for mode, ix in (("true", 0), ("proxy", 2)):
            sm, tr = {}, []
            for d in tdates:
                rs = [sims[(x, kp)][ix].get(d, 0.0) for x in pick_of[d] if (x, kp) in sims]
                sm[d] = sum(rs) / len(rs) if rs else 0.0
            for x in windows:
                if (x, kp) in sims:
                    tr += sims[(x, kp)][ix + 1]
            res[(kp, mode)] = (sm, tr)

    start = "2019-01-02"
    pd = [d for d in tdates if d >= start]
    train = [d for d in pd if d <= "2022-12-31"]
    test = [d for d in pd if d >= "2023-01-01"]
    port = {k: dict(zip(pd, combine([0.7, 0.3], [swing_q, v[0]], pd))) for k, v in res.items()}

    def mar(ser, ds):
        st, _, _ = curve_stats([ser.get(d, 0.0) for d in ds], ds)
        return st["cagr"] / abs(st["mdd"]) if st["mdd"] else 0

    out = [f"# Exit backtest part 2 — SWING_M profit exit on real intraday prices — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Period {pd[0]} → {pd[-1]}. Cells are CAGR / max drawdown. Formula and K values unchanged from part 1 "
           "(exit_results.md). 'True intraday' = checks at 09:35 … 15:00 on 5-minute bars and the close decision at "
           "15:50 for every variant; 'daily proxy' = part 1's method.\n",
           f"**QQQ:** full {cell(qr, pd)} · 2019–22 {cell(qr, train)} · 2023–26 {cell(qr, test)}\n",
           "## SWING_M alone\n",
           "| Variant | Full (true intraday) | 2019–22 | 2023–26 | Full (daily proxy) | Trades (true intraday, 1x) |",
           "|---|---|---|---|---|---|"]
    for kp in variants:
        sm, tr = res[(kp, "true")]
        out.append(f"| {label(kp, None)} | {cell(sm, pd)} | {cell(sm, train)} | {cell(sm, test)} | "
                   f"{cell(res[(kp, 'proxy')][0], pd)} | {tstats([t for t in tr if t['in'] >= pd[0]])} |")
    out.append("\n## Portfolio: 70% SWING_Q (current rules) + 30% SWING_M (variant), true intraday\n")
    out.append("| SWING_M variant | Full | 2019–22 | 2023–26 |\n|---|---|---|---|")
    for kp in variants:
        p = port[(kp, "true")]
        out.append(f"| {label(kp, None)} | {cell(p, pd)} | {cell(p, train)} | {cell(p, test)} |")
    out.append("\n## Walk-forward — chosen on 2019–22, scored on 2023–26 (SWING_M, true intraday)\n")
    out.append("| Choice rule | Variant | 2019–22 | 2023–26 (unseen) | BASE 2023–26 |\n|---|---|---|---|---|")
    base = res[(None, "true")][0]
    for lab, f in (("Best return / drawdown (MAR)", lambda kp: mar(res[(kp, "true")][0], train)),
                   ("Best CAGR", lambda kp: curve_stats([res[(kp, "true")][0].get(d, 0.0) for d in train], train)[0]["cagr"])):
        kp = max(variants, key=f)
        sm = res[(kp, "true")][0]
        out.append(f"| {lab} | {label(kp, None)} | {cell(sm, train)} | {cell(sm, test)} | {cell(base, test)} |")
    out.append("\n## Yearly, SWING_M (true intraday)\n")
    yrs = sorted({d[:4] for d in pd})
    out.append("| Variant | " + " | ".join(yrs) + " |\n|---|" + "---|" * len(yrs))
    for kp in variants:
        sm = res[(kp, "true")][0]
        cells = []
        for y in yrs:
            ds = [d for d in pd if d[:4] == y]
            eq = 1.0
            for d in ds:
                eq *= 1 + sm.get(d, 0.0)
            cells.append(f"{eq - 1:+.1%}")
        out.append(f"| {label(kp, None)} | " + " | ".join(cells) + " |")
    out.append("\n## Data log\n")
    out.extend(f"- {z}" for z in (log[:30] or ["(clean)"]))
    (HERE / "exit_m_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
