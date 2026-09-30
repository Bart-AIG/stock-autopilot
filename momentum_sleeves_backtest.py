"""
Momentum-picked sleeves — run the CORE, DAY and SWING rules on the monthly momentum picks
instead of on QQQ.  (Ryan, 2026-09-29: "what if we used the momentum pick method and ran
the core, day and swing sleeve on those names with monthly balance".)

Runs on GitHub Actions (FMP key). Pure standard library.

PICKS: at each month-end, the 10 names with the best trailing 12-month return from the
pooled S&P 100 + Nasdaq-100 lists as of end-2018 (no hindsight), equal weight, held for
the next month (the best signal in factors_results.md).

Constraint that shapes the design: there are no 2x/3x funds for most single stocks and the
account uses no margin and cannot short, so the stock sleeves run at 1x and the DAY sleeve
long-only. To separate "better names" from "more leverage", the QQQ sleeves are also shown
at 1x.

Sleeves:
  CORE-M   the 10 picks while QQQ > 200-day SMA (switch decided at a close, filled at the
           next), else T-bills. 5 bp x monthly turnover.
  DAY-M    noise-area breakout (Zarattini, Aziz & Barbon 2024) on each pick with 30-minute
           bars (the strategy checks every 30 min), 10% of the sleeve per name; long-only
           (realistic) and long/short (reference). 3 bp per side.
  SWING-M  RSI(2) + IBS + turn-of-month union on each pick, daily, 10% per name, idle cash
           in T-bills; trades at the close (the QQQ test showed ~25% of return lost when
           trading at 15:50 instead - apply the same haircut mentally).
  QQQ sleeves for comparison, same code: CORE (1x, and vol-targeted <=2x), DAY on QQQ
  30-minute bars (1x and 3x), SWING (1x and 2x).
Portfolios: 40/30/30 CORE/DAY/SWING, monthly rebalance, 2019-01 -> today.

Limits: one fallback universe; 7.7 years; single-stock intraday split days are skipped;
the 30-minute DAY sleeve on QQQ is shown so it can be compared with the 5-minute result.
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
from combo_backtest import curve_stats
from robust_backtest import arrays, combine, full_ohlc, swing

HERE = Path(__file__).resolve().parent
START = "2016-06-01"


def adj(sym, key):
    data = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    if not isinstance(data, list) or not data:
        return {}
    return {r["date"][:10]: float(r.get("adjClose") or r.get("close") or 0) for r in data
            if (r.get("adjClose") or r.get("close"))}


def bars30(sym, key, log):
    days = {}
    d, end = date(2018, 1, 1), date.today()
    while d < end:
        e = min(d + timedelta(days=24), end)
        data = _get(f"{BASE}/historical-chart/30min?symbol={sym}&from={d}&to={e}&apikey={key}")
        if isinstance(data, list):
            for r in data:
                ts = r["date"]
                days.setdefault(ts[:10], []).append(
                    {"t": ts[11:16], "o": float(r["open"]), "h": float(r["high"]), "l": float(r["low"]),
                     "c": float(r["close"]), "v": float(r.get("volume") or 0)})
        elif not days:
            log.append(f"{sym} 30min {d}: {str(data)[:60]}")
        d = e + timedelta(days=1)
        time.sleep(0.1)
    out = {}
    for k, v in days.items():
        b = sorted((x for x in v if "09:30" <= x["t"] <= "15:30"), key=lambda x: x["t"])
        uniq, seen = [], set()
        for x in b:
            if x["t"] not in seen:
                seen.add(x["t"]), uniq.append(x)
        if len(uniq) == 13:
            out[k] = uniq
    return out


def noise30(days, prev, lookback=14, long_only=True, cost=3e-4):
    """{date: net 1x return} for the noise-area breakout on 30-minute bars."""
    sess = sorted(days)
    moves = {s: {b["t"]: abs(b["c"] / days[s][0]["o"] - 1) for b in days[s]} for s in sess}
    out = {}
    for i, s in enumerate(sess):
        p = prev.get(s)
        bars = days[s]
        if p is None or i < lookback or abs(bars[0]["o"] / p - 1) > 0.3:   # skip split days
            out[s] = 0.0
            continue
        hist = sess[i - lookback:i]
        sig = {}
        for b in bars:
            vals = [moves[h][b["t"]] for h in hist if b["t"] in moves[h]]
            if len(vals) >= 10:
                sig[b["t"]] = sum(vals) / len(vals)
        op = bars[0]["o"]
        up_ref, dn_ref = max(op, p), min(op, p)
        pos, entry, ret, n = 0, 0.0, 0.0, 0
        pv = vv = 0.0
        for b in bars[:-1]:                               # last bar closes at 16:00 -> exit
            tp = (b["h"] + b["l"] + b["c"]) / 3
            pv += tp * b["v"]
            vv += b["v"]
            vwap = pv / vv if vv else b["c"]
            sgm = sig.get(b["t"])
            if sgm is None:
                continue
            U, L, c = up_ref * (1 + sgm), dn_ref * (1 - sgm), b["c"]
            if pos == 1 and c < max(U, vwap):
                ret += c / entry - 1
                pos = 0
            elif pos == -1 and c > min(L, vwap):
                ret += 1 - c / entry
                pos = 0
            if pos == 0:
                if c > U:
                    pos, entry, n = 1, c, n + 1
                elif c < L and not long_only:
                    pos, entry, n = -1, c, n + 1
        if pos:
            x = bars[-1]["c"]
            ret += (x / entry - 1) if pos == 1 else (1 - x / entry)
        out[s] = ret - 2 * cost * n
    return out


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "QLD", "BIL"]):
        a = adj(s, key)
        if a:
            A[s] = a
        if n % 40 == 0:
            print(f"daily {n}/{len(pool) + 3}", flush=True)
        time.sleep(0.08)
    qd = sorted(d for d in A["QQQ"] if d in A["BIL"] and d in A["QLD"])
    bil_r = {qd[i]: A["BIL"][qd[i]] / A["BIL"][qd[i - 1]] - 1 for i in range(1, len(qd))}
    qqq_r = {qd[i]: A["QQQ"][qd[i]] / A["QQQ"][qd[i - 1]] - 1 for i in range(1, len(qd))}

    # ---- monthly momentum picks (top 10 by trailing 252-session return)
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}                                   # month-end -> list held for the next month
    for m in me:
        k = qd.index(m)
        if k < 252:
            continue
        m0 = qd[k - 252]
        sc = [(A[s][m] / A[s][m0] - 1, s) for s in pool if s in A and m in A[s] and m0 in A[s]]
        sc.sort(reverse=True)
        picks[m] = [s for _, s in sc[:10]]
    ever = sorted({s for v in picks.values() for s in v})
    log.append(f"{len(ever)} distinct names were ever in the top 10: {', '.join(ever)}")

    def basket_on(d):
        """Picks in force on date d (chosen at the last month-end strictly before d)."""
        prior = [m for m in me if m < d and m in picks]
        return picks[prior[-1]] if prior else None

    tdates = [d for d in qd if d > me[0] and basket_on(d)]
    basket_by_day = {d: basket_on(d) for d in tdates}

    # ---- 200-day switch on QQQ (decided at close i-2, filled at close i-1)
    qidx = {d: i for i, d in enumerate(qd)}
    sig = {}
    for i in range(200, len(qd)):
        sig[qd[i]] = A["QQQ"][qd[i]] > sum(A["QQQ"][qd[j]] for j in range(i - 199, i + 1)) / 200
    on = {qd[i]: sig[qd[i - 2]] for i in range(202, len(qd))}

    # ---- CORE-M and QQQ cores
    core_m, prev_b = {}, None
    for d in tdates:
        b = basket_by_day[d]
        i = qidx[d]
        p = qd[i - 1]
        if on.get(d):
            rs = [A[s][d] / A[s][p] - 1 for s in b if d in A[s] and p in A[s]]
            r = sum(rs) / len(rs) if rs else 0.0
        else:
            r = bil_r.get(d, 0.0)
        if prev_b is not None and b != prev_b:
            r -= 2 * 5e-4 * len(set(b) - set(prev_b)) / 10
        prev_b = b
        core_m[d] = r
    core_q1 = {d: (qqq_r[d] if on.get(d) else bil_r.get(d, 0.0)) for d in tdates}
    core_qvt = {}
    for d in tdates:
        i = qidx[d]
        if on.get(d):
            rv = statistics.pstdev([qqq_r[qd[j]] for j in range(i - 21, i - 1)]) * math.sqrt(252) or 1e-9
            lv = min(2.0, 0.25 / rv)
            core_qvt[d] = lv * qqq_r[d] - 0.00475 * lv / 252 - max(0.0, lv - 1) * bil_r.get(d, 0.0)
        else:
            core_qvt[d] = bil_r.get(d, 0.0)

    # ---- per-name daily OHLC (swing) and 30-min bars (day)
    ohlc, b30, prevc = {}, {}, {}
    for n, s in enumerate(ever + ["QQQ"]):
        ohlc[s] = full_ohlc(s, key, START)
        b30[s] = bars30(s, key, log)
        rd = sorted(ohlc[s])
        prevc[s] = {rd[i]: ohlc[s][rd[i - 1]][3] for i in range(1, len(rd))}
        print(f"intraday {n + 1}/{len(ever) + 1} {s}: {len(b30[s])} sessions", flush=True)

    swing_name, day_name_lo, day_name_ls = {}, {}, {}
    for s in ever + ["QQQ"]:
        if s not in A or not ohlc.get(s):
            continue
        ds, C, H, L = arrays(ohlc[s], A[s])
        if len(ds) > 260:
            swing_name[s] = swing(ds, C, H, L, None, lev=1, cash=bil_r)
        day_name_lo[s] = noise30(b30[s], prevc[s], long_only=True)
        day_name_ls[s] = noise30(b30[s], prevc[s], long_only=False)

    def sleeve_from(per_name):
        out = {}
        for d in tdates:
            b = basket_by_day[d]
            rs = [per_name[s].get(d, 0.0) for s in b if s in per_name]
            out[d] = sum(rs) / len(rs) if rs else 0.0
        return out

    swing_m = sleeve_from(swing_name)
    day_m_lo, day_m_ls = sleeve_from(day_name_lo), sleeve_from(day_name_ls)
    swing_q1 = {d: swing_name.get("QQQ", {}).get(d, 0.0) for d in tdates}
    ds, C, H, L = arrays(ohlc["QQQ"], A["QQQ"])
    swing_q2 = swing(ds, C, H, L, None, lev=2, cash=bil_r)
    day_q1 = {d: day_name_ls["QQQ"].get(d, 0.0) for d in tdates}
    day_q3 = {d: 3 * day_name_ls["QQQ"].get(d, 0.0) for d in tdates}   # cost scales with exposure too
    day_q1_lo = {d: day_name_lo["QQQ"].get(d, 0.0) for d in tdates}

    out = [f"# Momentum-picked sleeves — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Picks: monthly top 10 by 12-month return from the pooled end-2018 S&P 100 + Nasdaq-100 lists. "
           f"Period {tdates[0]} → {tdates[-1]}. {len(ever)} different names were picked at some point.\n"]
    per = [("2019–2026", tdates[0], tdates[-1]), ("2019–2021", tdates[0], "2021-12-31"),
           ("2022", "2022-01-01", "2022-12-31"), ("2023–2026", "2023-01-01", tdates[-1])]

    def line(label, ser):
        cells = []
        for _, a, b in per:
            dd = [d for d in tdates if a <= d <= b]
            st, _, _ = curve_stats([ser.get(d, 0.0) for d in dd], dd)
            cells.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
        return f"| {label} | " + " | ".join(cells) + " |"

    out.append("## Each sleeve alone (CAGR / max DD)\n")
    out.append("| Sleeve | " + " | ".join(p[0] for p in per) + " |\n|---|" + "---|" * len(per))
    rows = [("QQQ buy & hold", {d: qqq_r[d] for d in tdates}),
            ("Momentum top 10, always held (1x)", {d: statistics.mean(
                [A[s][d] / A[s][qd[qidx[d] - 1]] - 1 for s in basket_by_day[d] if d in A[s] and qd[qidx[d] - 1] in A[s]] or [0])
                for d in tdates}),
            ("CORE-M: top 10 + 200d switch (1x)", core_m), ("CORE QQQ + 200d (1x)", core_q1),
            ("CORE QQQ vol-target 25% ≤2x (current plan)", core_qvt),
            ("DAY-M: noise on the picks, long-only (1x)", day_m_lo),
            ("DAY-M: noise on the picks, long/short (1x, reference)", day_m_ls),
            ("DAY QQQ noise 30-min, long/short (1x)", day_q1), ("DAY QQQ noise 30-min, long-only (1x)", day_q1_lo),
            ("DAY QQQ noise 30-min, 3x (current plan)", day_q3),
            ("SWING-M: union on the picks (1x)", swing_m), ("SWING QQQ union (1x)", swing_q1),
            ("SWING QQQ union 2x (current plan)", {d: swing_q2.get(d, 0.0) for d in tdates})]
    for lab, ser in rows:
        out.append(line(lab, ser))

    out.append("\n## 40 / 30 / 30 CORE / DAY / SWING portfolios, monthly rebalance\n")
    out.append("| Portfolio | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |")
    out.append("|---|---|---|---|---|---|")
    port = [
        ("A. Current plan (QQQ: vol-target core, day 3x, swing 2x)", [core_qvt, day_q3, swing_q2]),
        ("B. QQQ plan at 1x (core 1x, day 1x, swing 1x)", [core_q1, day_q1, swing_q1]),
        ("C. Momentum plan at 1x (CORE-M, DAY-M long-only, SWING-M)", [core_m, day_m_lo, swing_m]),
        ("D. Hybrid: CORE-M + QQQ day 3x + QQQ swing 2x", [core_m, day_q3, swing_q2]),
        ("E. Hybrid: QQQ vol-target core + DAY-M + SWING-M", [core_qvt, day_m_lo, swing_m]),
        ("F. Hybrid: half/half core (QQQ vol-target + CORE-M) + QQQ day 3x + QQQ swing 2x",
         [{d: 0.5 * core_qvt.get(d, 0) + 0.5 * core_m.get(d, 0) for d in tdates}, day_q3, swing_q2]),
    ]
    q_st, q_y, q_end = curve_stats([qqq_r[d] for d in tdates], tdates)
    out.append(f"| QQQ buy & hold | {q_st['cagr']:.1%} | {q_st['mdd']:.1%} | {q_st['sharpe']:.2f} | "
               f"{min(q_y.values()):.1%} | ${3340 * q_end:,.0f} |")
    yr_rows = [("QQQ", q_y)]
    for lab, sl in port:
        pr = combine([0.4, 0.3, 0.3], sl, tdates)
        st, y, end = curve_stats(pr, tdates)
        out.append(f"| {lab} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | {min(y.values()):.1%} | ${3340 * end:,.0f} |")
        yr_rows.append((lab[:2], y))
    yrs = sorted(q_y)
    out.append("\n| Portfolio | " + " | ".join(yrs) + " |\n|---|" + "---|" * len(yrs))
    for lab, y in yr_rows:
        out.append(f"| {lab} | " + " | ".join(f"{y.get(k, 0):.1%}" for k in yrs) + " |")
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in log[:30])
    (HERE / "momentum_sleeves_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
