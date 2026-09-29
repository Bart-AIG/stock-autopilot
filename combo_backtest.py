"""
Combination backtest — how should the account be split between the trend-filtered
leveraged core and the intraday noise-area sleeve?  (Ryan, 2026-09-29: "lets test it
with combinations different ratios of account balance".)

Runs on GitHub Actions (FMP key). Pure standard library.

Sleeves (both tested separately in backtest_results.md / intraday_results.md):
  CORE  QLD while QQQ's close is above its 200-day SMA, else T-bills (BIL). The switch
        is decided at the close and filled at the NEXT close (no look-ahead), 5 bp cost.
  DAY   Noise-area breakout on QQQ (Zarattini, Aziz & Barbon 2024) traded through a 3x
        fund (TQQQ long / SQQQ short), flat every night. 3 bp per side on capital.

Portfolios: fixed CORE/DAY splits from 100/0 to 0/100, rebalanced on the first session
of each month (two separate cash pools in between). Plus an OVERLAY variant: when the
CORE is in T-bills, that cash also runs the DAY strategy intraday (it is idle anyway).

Also: a robustness grid for the DAY sleeve (lookback days, check interval, costs, and
the first vs second half of the sample), because it was the least-proven piece.

Limits: one historical path (2018 -> today, ~8.7 years; 2008 and 2000-02 not in the
intraday data); 5-minute bars; the 3x sleeve is modelled as 3x QQQ's intraday move
(no fund tracking error); taxes ignored.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import date, datetime
from pathlib import Path

from backtest import BASE, _get, stats
from intraday_backtest import fetch_5min, fetch_unadjusted

HERE = Path(__file__).resolve().parent
START_CAPITAL = 3340.0


def adj_daily(sym, key, start="2016-06-01"):
    data = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol={sym}&from={start}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return {}
    return {r["date"][:10]: float(r.get("adjClose") or r["close"]) for r in data}


def noise_day(bars, prev_close, sigma, check=30):
    op = bars[0]["o"]
    up_ref, dn_ref = max(op, prev_close), min(op, prev_close)
    pos, entry, ret, trades = 0, 0.0, 0.0, 0
    pv = vv = 0.0
    for b in bars:
        tp = (b["h"] + b["l"] + b["c"]) / 3
        pv += tp * b["v"]
        vv += b["v"]
        vwap = pv / vv if vv else b["c"]
        end_min = int(b["t"][:2]) * 60 + int(b["t"][3:]) + 5
        if (end_min - 570) % check != 0 or b["t"] == bars[-1]["t"]:
            continue
        s = sigma.get(b["t"])
        if s is None:
            continue
        U, L, c = up_ref * (1 + s), dn_ref * (1 - s), b["c"]
        if pos == 1 and c < max(U, vwap):
            ret += c / entry - 1
            pos = 0
        elif pos == -1 and c > min(L, vwap):
            ret += 1 - c / entry
            pos = 0
        if pos == 0:
            if c > U:
                pos, entry, trades = 1, c, trades + 1
            elif c < L:
                pos, entry, trades = -1, c, trades + 1
    if pos:
        x = bars[-1]["c"]
        ret += (x / entry - 1) if pos == 1 else (1 - x / entry)
    return ret, trades


def noise_series(days, prev, lookback=14, check=30, lev=3, cost=3e-4):
    """Daily net return on capital of the DAY sleeve, keyed by session date."""
    sessions = sorted(days)
    moves = {s: {b["t"]: abs(b["c"] / days[s][0]["o"] - 1) for b in days[s]} for s in sessions}
    out = {}
    for i, s in enumerate(sessions):
        p = prev.get(s)
        if p is None or i < lookback:
            out[s] = 0.0
            continue
        hist = sessions[i - lookback:i]
        sig = {}
        for b in days[s]:
            vals = [moves[h][b["t"]] for h in hist if b["t"] in moves[h]]
            if len(vals) >= int(lookback * 0.7):
                sig[b["t"]] = sum(vals) / len(vals)
        r, n = noise_day(days[s], p, sig, check)
        out[s] = lev * r - 2 * cost * n
    return out


def curve_stats(rets, dates):
    eq, curve = 1.0, []
    for r in rets:
        eq *= 1 + r
        curve.append(eq)
    st = stats(curve, dates)
    yrs, last, prev_end = {}, {}, 1.0
    for v, d in zip(curve, dates):
        last[d[:4]] = v
    for y in sorted(last):
        yrs[y] = last[y] / prev_end - 1
        prev_end = last[y]
    return st, yrs, curve[-1]


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    qqq_adj, qld, bil = adj_daily("QQQ", key), adj_daily("QLD", key), adj_daily("BIL", key)
    raw = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    days = fetch_5min("QQQ", key, log)
    if not (qqq_adj and qld and bil and raw and days):
        sys.exit("missing data")

    # prior unadjusted close per session (matches the unadjusted intraday bars)
    rd = sorted(raw)
    prev = {}
    j = 0
    for s in sorted(days):
        while j < len(rd) and rd[j] < s:
            j += 1
        if j:
            prev[s] = raw[rd[j - 1]]

    # CORE: signal at close d -> position held from close d to close d+1, switch at close (lag 1)
    qd = sorted(d for d in qqq_adj if d in qld and d in bil)
    sig = {}
    for i in range(200, len(qd)):
        w = [qqq_adj[qd[k]] for k in range(i - 199, i + 1)]
        sig[qd[i]] = qqq_adj[qd[i]] > sum(w) / 200
    core_ret, core_on = {}, {}
    state = None
    for i in range(201, len(qd)):
        d, p = qd[i], qd[i - 1]
        want = sig[qd[i - 2]] if i >= 202 else sig[p]      # decided at close i-2, filled at close i-1
        cost = 0.0
        if state is not None and want != state:
            cost = 5e-4
        state = want
        r = (qld[d] / qld[p] - 1) if state else (bil[d] / bil[p] - 1)
        core_ret[d], core_on[d] = r - cost, state

    dates = [d for d in sorted(days) if d in core_ret]
    day3 = noise_series(days, prev)
    qqq_ret = {qd[i]: qqq_adj[qd[i]] / qqq_adj[qd[i - 1]] - 1 for i in range(1, len(qd))}
    bil_ret = {qd[i]: bil[qd[i]] / bil[qd[i - 1]] - 1 for i in range(1, len(qd))}

    out = [f"# Combination backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Sessions: {len(dates)} ({dates[0]} → {dates[-1]}). Starting value in the $ column: ${START_CAPITAL:,.0f} "
           "(today's account). CORE = QLD while QQQ > 200-day SMA else T-bills. DAY = noise-area breakout on QQQ "
           "through a 3x fund. Monthly rebalance.\n"]

    c = [core_ret[d] for d in dates]
    dy = [day3.get(d, 0.0) for d in dates]
    corr = statistics.correlation(c, dy) if len(c) > 10 else float("nan")
    out.append(f"Daily correlation CORE vs DAY: **{corr:+.2f}**. DAY sleeve active on "
               f"{sum(1 for x in dy if x) / len(dy):.0%} of sessions.\n")

    rows = []
    q_st, q_y, q_end = curve_stats([qqq_ret[d] for d in dates], dates)
    rows.append(("QQQ buy & hold (benchmark)", q_st, q_y, q_end))
    for wc in (100, 90, 80, 70, 60, 50, 40, 30, 20, 0):
        wd = 100 - wc
        a, b = wc / 100, wd / 100
        pr, month = [], None
        for d in dates:
            if d[:7] != month:
                a, b, month = wc / 100, wd / 100, d[:7]
            tot = a + b
            a2, b2 = a * (1 + core_ret[d]), b * (1 + day3.get(d, 0.0))
            pr.append((a2 + b2) / tot - 1)
            a, b = a2, b2
        st, y, end = curve_stats(pr, dates)
        rows.append((f"{wc}% CORE / {wd}% DAY", st, y, end))
    # overlay: core cash runs DAY when the core is in T-bills
    for wc in (100, 70):
        wd = 100 - wc
        a, b, pr, month = wc / 100, wd / 100, [], None
        for d in dates:
            if d[:7] != month:
                a, b, month = wc / 100, wd / 100, d[:7]
            tot = a + b
            cr = core_ret[d] + (day3.get(d, 0.0) if not core_on[d] else 0.0)
            a2, b2 = a * (1 + cr), b * (1 + day3.get(d, 0.0))
            pr.append((a2 + b2) / tot - 1)
            a, b = a2, b2
        st, y, end = curve_stats(pr, dates)
        rows.append((f"{wc}% CORE + OVERLAY / {wd}% DAY", st, y, end))

    out.append("| Mix | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |")
    out.append("|---|---|---|---|---|---|")
    for name, st, y, end in rows:
        out.append(f"| {name} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | "
                   f"{min(y.values()):.1%} | ${START_CAPITAL * end:,.0f} |")
    yrs = sorted(rows[0][2])
    out.append("\n**Calendar-year returns:**\n")
    out.append("| Mix | " + " | ".join(yrs) + " |")
    out.append("|---|" + "---|" * len(yrs))
    for name, _, y, _ in rows:
        out.append(f"| {name} | " + " | ".join(f"{y.get(k, 0):.1%}" for k in yrs) + " |")

    # robustness of the DAY sleeve
    out.append("\n## DAY sleeve robustness (3x, CAGR / max DD)\n")
    half = dates[len(dates) // 2]
    out.append(f"Halves split at {half}.\n")
    out.append("| Lookback | Check every | Cost/side | Full period | First half | Second half |")
    out.append("|---|---|---|---|---|---|")
    for lb in (10, 14, 20):
        for ck in (15, 30, 60):
            for cost in (3e-4, 6e-4):
                if cost == 6e-4 and not (lb == 14 and ck == 30):
                    continue
                ser = noise_series(days, prev, lb, ck, 3, cost)
                cells = []
                for a_, b_ in ((dates[0], dates[-1]), (dates[0], half), (half, dates[-1])):
                    dd = [d for d in dates if a_ <= d <= b_]
                    st, _, _ = curve_stats([ser.get(d, 0.0) for d in dd], dd)
                    cells.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
                out.append(f"| {lb}d | {ck} min | {cost * 1e4:.0f} bp | " + " | ".join(cells) + " |")
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "combo_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
