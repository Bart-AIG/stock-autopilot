"""
Options-income sleeves added to what already works (Ryan, 2026-09-30: "what if we added one
of these strategies as a sleeve ratio'd to what we already figured out works" - and, on QQQI:
"just run the same strategy that the qqqi etf managers run for ourselves").

Runs on GitHub Actions (FMP key). Pure standard library.

WHAT ALREADY WORKS (from the earlier tests; the day sleeve is dropped):
  CORE    QQQ exposure = 25% / 20-day realised vol (capped at 2x) while QQQ > 200-day SMA,
          else T-bills.
  SWING-M RSI(2) + IBS + turn-of-month swing rules run on the monthly top-10 12-month-momentum
          names from the pooled end-2018 S&P 100 + Nasdaq-100 lists, 1x.

NEW SLEEVE 1 - "DIY QQQI" (covered call on the Nasdaq-100, run by us):
  Hold QQQ (total return); at each month-end sell a ~1-month call on 100% of it, near or
  slightly out of the money, and optionally buy a further-OTM call so some upside is kept
  (a call spread). Rolled monthly, held to the roll.
  No historical option prices are available on this data tier, so options are priced with
  Black-Scholes using implied vol = QQQ 20-day realised vol x 1.10 (the QQQ IV/RV ratio this
  desk measured in iv_history.json is ~1.0-1.2); 3% of premium lost to the bid/ask.
  Validated against the real funds: QQQI (2024+) and QYLD (at-the-money covered call, 2014+).
  Practical note: one QQQ contract covers 100 shares (~$74k) and one XND contract ~$25k, so
  this cannot be run at the current ~$3.3k account size; the test tells whether it is worth
  running later.

NEW SLEEVE 2 - QuantGlide-style SPX 0DTE credit spread (structural test only):
  On SPY 5-minute bars: 09:30-10:30 opening range; entry at 10:35; direction from price vs the
  range midpoint (below -> bear call, above -> bull put; the reverse is also tested); skip if
  the range is wider than 0.8x the expected daily move; short strike z x the expected move for
  the rest of the day away, 15-point-equivalent width (0.2% of price); held to the close.
  Without option prices the CREDIT is an assumption, so the output is (a) how often the
  spread is breached and how badly, and (b) the credit needed to break even - compared with
  the $0.45 on 15 points (3% of width) in QuantGlide's own example. Costs 0.5% of width.
  Governance: this conflicts with the playbook (0-1 DTE is banned; the agentic API cannot
  place multi-leg orders), so it could only be traded after a rule change.

Portfolios: CORE / SWING-M / DIY-QQQI / 0DTE splits, monthly rebalance, 2019 -> today.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import date, datetime
from pathlib import Path

from backtest import NDX100_2018, SP100_2018, stats
from combo_backtest import curve_stats
from intraday_backtest import fetch_5min
from momentum_sleeves_backtest import adj
from robust_backtest import arrays, combine, full_ohlc, swing

HERE = Path(__file__).resolve().parent


def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs_call(S, K, T, r, v):
    if T <= 0 or v <= 0:
        return max(S - K, 0.0)
    d1 = (math.log(S / K) + (r + v * v / 2) * T) / (v * math.sqrt(T))
    return S * ncdf(d1) - K * math.exp(-r * T) * ncdf(d1 - v * math.sqrt(T))


def covered_call(dates, P, rv, r_ann, otm, kicker=None, cover=1.0, ivk=1.10, slip=0.03):
    """Daily return series of a monthly-rolled covered call on price series P (total return).
    otm: short strike as % above spot (0 = at the money); kicker: long call % above spot."""
    out, i = {}, 0
    month_end = [k for k in range(len(dates)) if k == len(dates) - 1 or dates[k][:7] != dates[k + 1][:7]]
    rolls = [k for k in month_end if k >= 21]
    for a, b in zip(rolls, rolls[1:]):
        S0 = P[a]
        vol = max(0.08, rv[a] * ivk)
        n = b - a
        K = S0 * (1 + otm)
        K2 = S0 * (1 + kicker) if kicker else None
        r = r_ann.get(dates[a], 0.03)
        prem = bs_call(S0, K, n / 252, r, vol) * (1 - slip)
        kcost = bs_call(S0, K2, n / 252, r, vol) * (1 + slip) if K2 else 0.0

        def value(k):
            S = P[k]
            T = (b - k) / 252
            v = S - cover * bs_call(S, K, T, r, vol)
            if K2:
                v += cover * bs_call(S, K2, T, r, vol)
            return v

        prev = S0 - cover * prem + (cover * kcost if K2 else 0.0)
        # the net credit is cash we hold: add it back so the sleeve's equity starts at S0
        cash = cover * prem - (cover * kcost if K2 else 0.0)
        prev_eq = prev + cash
        for k in range(a + 1, b + 1):
            eq = value(k) + cash
            out[dates[k]] = eq / prev_eq - 1
            prev_eq = eq
    return out


def zero_dte(days, daily_close, z=2.0, credit=0.03, reverse=False, gate=0.8, cost=0.005):
    """Per-session P&L in units of spread width, or None when no trade."""
    dl = sorted(daily_close)
    res = {}
    for s in sorted(days):
        prior = [daily_close[d] for d in dl if d < s][-21:]
        if len(prior) < 21:
            continue
        rets = [prior[i] / prior[i - 1] - 1 for i in range(1, len(prior))]
        sd = statistics.pstdev(rets)
        bars = days[s]
        orb = [b for b in bars if b["t"] < "10:30"]
        ent = [b for b in bars if b["t"] == "10:30"]
        if len(orb) < 10 or not ent:
            continue
        hi, lo = max(b["h"] for b in orb), min(b["l"] for b in orb)
        E, X = ent[0]["c"], bars[-1]["c"]
        if (hi - lo) / E > gate * sd:
            res[s] = None
            continue
        bear = (E < (hi + lo) / 2) != reverse
        D = z * sd * math.sqrt(325 / 390) * E
        W = 0.002 * E
        x = (X - (E + D)) if bear else ((E - D) - X)
        res[s] = credit - min(max(x, 0.0), W) / W - cost
    return res


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "BIL", "SPY", "QQQI", "QYLD"]):
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
    r_ann = {}
    for i in range(22, len(qd)):   # trailing 21-day T-bill yield, capped at 0-10%
        r_ann[qd[i]] = min(0.10, max(0.0, statistics.mean(br.get(qd[j], 0.0) for j in range(i - 20, i + 1)) * 252))
    rv = [None] * len(qd)
    for i in range(21, len(qd)):
        rv[i] = statistics.pstdev([Q[j] / Q[j - 1] - 1 for j in range(i - 19, i + 1)]) * math.sqrt(252)

    # ---------- CORE (vol-target 25%, <=2x, 200d switch decided at close i-2)
    core = {}
    for i in range(203, len(qd)):
        on = Q[i - 2] > sum(Q[i - 201:i - 1]) / 200
        if on:
            lv = min(2.0, 0.25 / (rv[i - 1] or 1e-9))
            core[qd[i]] = lv * qr[qd[i]] - 0.00475 * lv / 252 - max(0.0, lv - 1) * br.get(qd[i], 0.0)
        else:
            core[qd[i]] = br.get(qd[i], 0.0)

    # ---------- SWING-M
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}
    for m in me:
        k = qd.index(m)
        m0 = qd[k - 252]
        sc = sorted(((A[s][m] / A[s][m0] - 1, s) for s in pool if s in A and m in A[s] and m0 in A[s]), reverse=True)
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
        prior = [m for m in me if m < d]
        b = picks[prior[-1]]
        rs = [sw[s].get(d, 0.0) for s in b if s in sw]
        swing_m[d] = sum(rs) / len(rs) if rs else 0.0

    # ---------- DIY QQQI (covered call) variants
    cc_variants = {
        "ATM, 100% covered (QYLD-style)": dict(otm=0.0),
        "2% OTM, 100% covered": dict(otm=0.02),
        "2% OTM + buy 6% OTM call (QQQI-style call spread)": dict(otm=0.02, kicker=0.06),
        "1% OTM + buy 5% OTM call": dict(otm=0.01, kicker=0.05),
        "2% OTM, 50% covered": dict(otm=0.02, cover=0.5),
    }
    cc = {k: covered_call(qd, Q, rv, r_ann, **v) for k, v in cc_variants.items()}
    out = [f"# Options-income sleeves — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n"]

    def cells(ser, periods, dl):
        c = []
        for _, a, b in periods:
            dd = [d for d in dl if a <= d <= b and d in ser]
            if len(dd) < 40:
                c.append("n/a")
                continue
            st, _, _ = curve_stats([ser[d] for d in dd], dd)
            c.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
        return " | ".join(c)

    # validation vs real funds
    out.append("## 1. DIY covered call (\"run the QQQI strategy ourselves\") — model vs the real funds\n")
    val = []
    for fund, model in (("QYLD", "ATM, 100% covered (QYLD-style)"), ("QQQI", "2% OTM + buy 6% OTM call (QQQI-style call spread)")):
        if fund in A:
            fd = sorted(d for d in A[fund] if d in cc[model])
            fr = {fd[i]: A[fund][fd[i]] / A[fund][fd[i - 1]] - 1 for i in range(1, len(fd))}
            dd = fd[1:]
            if len(dd) > 60:
                s_f, _, _ = curve_stats([fr[d] for d in dd], dd)
                s_m, _, _ = curve_stats([cc[model][d] for d in dd], dd)
                s_q, _, _ = curve_stats([qr.get(d, 0.0) for d in dd], dd)
                val.append(f"| {fund} (real) vs model \"{model}\", {dd[0]} → {dd[-1]} | {s_f['cagr']:.1%} / {s_f['mdd']:.0%} | "
                           f"{s_m['cagr']:.1%} / {s_m['mdd']:.0%} | {s_q['cagr']:.1%} / {s_q['mdd']:.0%} |")
    out.append("| Check | Real fund (CAGR / max DD) | Our model | QQQ same period |\n|---|---|---|---|")
    out.extend(val or ["| (fund history not served) | | | |"])
    per = [("2007–2026", "2007-01-01", qd[-1]), ("2008 crisis", "2007-10-01", "2009-06-30"),
           ("2019–2026", "2019-01-01", qd[-1]), ("2022", "2022-01-01", "2022-12-31"), ("2023–2026", "2023-01-01", qd[-1])]
    out.append("\n| Covered-call variant (CAGR / max DD) | " + " | ".join(p[0] for p in per) + " |\n|---|" + "---|" * len(per))
    out.append("| QQQ buy & hold | " + cells(qr, per, qd) + " |")
    for k, ser in cc.items():
        out.append(f"| {k} | " + cells(ser, per, qd) + " |")

    # ---------- 0DTE
    days = fetch_5min("SPY", key, log)
    spy_close = {}
    for s in sorted(days):
        spy_close[s] = days[s][-1]["c"]
    out.append(f"\n## 2. QuantGlide-style 0DTE credit spread — structural test on SPY ({len(days)} sessions)\n")
    out.append("P&L in units of spread width; the credit is an assumption because no option prices are available. "
               "QuantGlide's own example: $0.45 credit on a 15-point spread = 3% of width.\n")
    out.append("| Short strike distance | Direction | Trades / yr | Win rate | Avg loss when breached (x width) | "
               "Max-loss days | Breakeven credit (% of width) |")
    out.append("|---|---|---|---|---|---|---|")
    yrs = max(1e-9, len(days) / 252)
    for z in (1.5, 2.0, 2.5):
        for rev in (False, True):
            r0 = zero_dte(days, spy_close, z=z, credit=0.0, reverse=rev, cost=0.0)
            trades = [v for v in r0.values() if v is not None]
            if not trades:
                continue
            losses = [-v for v in trades if v < 0]
            be = (sum(losses) / len(trades) + 0.005) / (1 - 0.0)
            out.append(f"| {z}× expected move | {'fade (reverse)' if rev else 'with morning direction'} | {len(trades) / yrs:.0f} | "
                       f"{1 - len(losses) / len(trades):.1%} | {statistics.mean(losses) if losses else 0:.2f} | "
                       f"{sum(1 for x in losses if x >= 0.999)} | {be:.1%} |")
    out.append("\n**Sleeve returns (CAGR / max DD) at 10% and 30% of the sleeve at risk per trade:**\n")
    out.append("| Distance | Credit | 10% at risk | 30% at risk (QuantGlide sizing) |\n|---|---|---|---|")
    zd = sorted(days)
    sleeve_0dte = None
    for z in (1.5, 2.0, 2.5):
        for c in (0.02, 0.03, 0.05):
            r = zero_dte(days, spy_close, z=z, credit=c)
            row = []
            for f in (0.10, 0.30):
                ser = {d: (f * v / (1 - c) if v is not None else 0.0) for d, v in r.items()}
                dd = [d for d in zd if d in ser]
                st, _, _ = curve_stats([ser[d] for d in dd], dd)
                row.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
                if z == 2.0 and c == 0.03 and f == 0.10:
                    sleeve_0dte = ser
            out.append(f"| {z}× | {c:.0%} | " + " | ".join(row) + " |")

    # ---------- portfolios
    first0 = min(sleeve_0dte)
    pd = [d for d in tdates if d in core and d in swing_m and d >= first0]
    ccs = cc["2% OTM + buy 6% OTM call (QQQI-style call spread)"]
    out.append(f"\n## 3. Portfolios, {pd[0]} → {pd[-1]}, monthly rebalance\n")
    out.append("CORE = vol-targeted QQQ core; SWING-M = swing rules on the momentum picks (trading at the close; "
               "the earlier test lost ~25% of swing return trading at 15:50); CC = DIY QQQI (2% OTM + 6% OTM call bought); "
               "0DTE = 2.0× distance, 3% credit, 10% at risk per trade.\n")
    out.append("| CORE / SWING-M / CC / 0DTE | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |")
    out.append("|---|---|---|---|---|---|")
    st, y, e = curve_stats([qr[d] for d in pd], pd)
    out.append(f"| QQQ buy & hold | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | {min(y.values()):.1%} | ${3340 * e:,.0f} |")
    for w in ((50, 50, 0, 0), (40, 40, 20, 0), (35, 35, 30, 0), (30, 30, 40, 0), (45, 45, 0, 10), (40, 40, 0, 20),
              (35, 35, 20, 10), (0, 0, 100, 0), (0, 0, 0, 100)):
        pr = combine([x / 100 for x in w], [core, swing_m, ccs, sleeve_0dte], pd)
        st, y, e = curve_stats(pr, pd)
        out.append(f"| {' / '.join(map(str, w))} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | "
                   f"{min(y.values()):.1%} | ${3340 * e:,.0f} |")
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "options_income_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
