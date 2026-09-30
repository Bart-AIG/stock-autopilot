"""
Robustness batch for the three-sleeve plan (Ryan, 2026-09-29: "lets test it").

Runs on GitHub Actions (FMP key). Pure standard library.

1. SWING robustness
   a. Execution realism: decide AND trade at 15:50 ET on the live price (the 15:45-15:50
      5-minute bar), instead of on the exact close. 2018 -> today (intraday data window).
   b. Same rules on SPY (2007 -> today).
   c. One-at-a-time parameter changes: RSI(2) entry 5/10/15; RSI exit SMA5 / SMA3 /
      RSI2>70; IBS entry 0.15/0.20/0.25; turn-of-month window.
2. 2000-02 crash test on the Nasdaq-100 INDEX (^NDX, price only) as far back as FMP serves
   it: 1x/2x/3x daily-reset, with and without the 200-day switch, plus the SWING rules.
   Cash / financing rate = 3-month T-bill from FMP treasury rates if served, else 3%/yr.
3. CORE upgrades (real ETFs, 2007 -> today): volatility-targeted leverage (target 20/25/30%
   annualised, capped at 2x) and a better "off" asset (TLT, GLD, or dual momentum = the
   best 3-month performer of TLT/GLD/BIL). Then each core variant inside the 40/30/30
   CORE/DAY/SWING portfolio (2018 -> today).

Limits: ^NDX is a price index (no dividends, ~0.5-1%/yr understated); synthetic leverage
ignores fund tracking error; one historical path; taxes ignored.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
from datetime import date, datetime
from pathlib import Path

from analyze import compute_rsi
from backtest import BASE, _get, stats
from combo_backtest import adj_daily, curve_stats, noise_series
from intraday_backtest import fetch_5min, fetch_unadjusted

HERE = Path(__file__).resolve().parent
FEE = 1e-4


def full_ohlc(sym, key, start):
    data = _get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={start}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return {}
    return {r["date"][:10]: (float(r["open"]), float(r["high"]), float(r["low"]), float(r["close"]))
            for r in data if r.get("close") and r.get("high") and r.get("low") and r.get("open")}


def tbill_rates(key, log):
    """{date: annual 3-month rate as a fraction}, or {} (callers fall back to 3%)."""
    out = {}
    for y in range(1985, date.today().year + 1):
        d = _get(f"{BASE}/treasury-rates?from={y}-01-01&to={y}-12-31&apikey={key}")
        if not isinstance(d, list):
            log.append(f"treasury rates not served ({str(d)[:60]}); using 3%/yr")
            return {}
        for r in d:
            v = r.get("month3")
            if v is not None:
                out[r["date"][:10]] = float(v) / 100
    return out


def rate_on(rates, d, default=0.03):
    return rates.get(d, default) if rates else default


# ----------------------------------------------------------------------------- swing rules

def swing(dates, C, H, L, O_unused, X=None, XH=None, XL=None, lev=1, cash=None, rsi_in=10,
          rsi_exit="sma5", ibs_in=0.2, ibs_out=0.8, ibs_max=5, tom=(1, 3), parts=("RSI2", "IBS", "TOM")):
    """Union swing sleeve. C = adjusted closes (signals + returns). X = execution/signal price
    for 'today' (defaults to C: trade at the close). H/L (or XH/XL up to the execution time)
    and the matching unadjusted price feed IBS via the ratio (C-L)/(H-L) computed on the
    same scale. Returns {date: net return on capital} for holding from exec d-1 to exec d."""
    X = X or C
    XH, XL = XH or H, XL or L
    n = len(dates)
    month_ix = {}
    for i, d in enumerate(dates):
        month_ix.setdefault(d[:7], []).append(i)
    tom_days = set()
    for ix in month_ix.values():
        tom_days |= set(ix[:tom[1]]) | set(ix[-tom[0]:] if tom[0] else [])
    held = {"RSI2": False, "IBS": False, "TOM": False}
    age, out, pos = 0, {}, False
    for i in range(201, n):
        d = dates[i]
        r = X[i] / X[i - 1] - 1
        c0 = (cash or {}).get(d, 0.0)
        out[d] = lev * r if pos else c0
        hist = C[i - 199:i] + [X[i]]
        sma200 = sum(hist) / 200
        px = X[i]
        up = px > sma200
        r2 = compute_rsi(C[i - 59:i] + [px], 2)
        new = dict(held)
        if "RSI2" in parts:
            if held["RSI2"]:
                if rsi_exit == "sma5":
                    new["RSI2"] = not (px > sum(C[i - 4:i] + [px]) / 5)
                elif rsi_exit == "sma3":
                    new["RSI2"] = not (px > sum(C[i - 2:i] + [px]) / 3)
                else:
                    new["RSI2"] = not (r2 is not None and r2 > 70)
            else:
                new["RSI2"] = r2 is not None and r2 < rsi_in and up
        if "IBS" in parts:
            rng = XH[i] - XL[i]
            ibs = (X[i] - XL[i]) / rng if rng > 0 else 0.5
            if held["IBS"]:
                age += 1
                new["IBS"] = not (ibs > ibs_out or age >= ibs_max)
            else:
                new["IBS"] = ibs < ibs_in and up
                age = 0
        if "TOM" in parts:
            new["TOM"] = (i + 1) in tom_days
        now = any(new[k] for k in parts)
        if now != pos:
            out[d] -= FEE * lev
        pos = now
        held = new
    return out


def arrays(ohlc, adj):
    dates = [d for d in sorted(ohlc) if d in adj]
    C = [adj[d] for d in dates]
    # H/L on the adjusted scale so IBS uses consistent prices
    H = [ohlc[d][1] * adj[d] / ohlc[d][3] for d in dates]
    L = [ohlc[d][2] * adj[d] / ohlc[d][3] for d in dates]
    return dates, C, H, L


def row(label, ser, dates, periods):
    cells = []
    for _, a, b in periods:
        dd = [d for d in dates if a <= d <= b and d in ser]
        if len(dd) < 20:
            cells.append("no data")
            continue
        st, _, _ = curve_stats([ser[d] for d in dd], dd)
        cells.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
    return f"| {label} | " + " | ".join(cells) + " |"


def combine(weights, sleeves, dates):
    bal, month, pr = list(weights), None, []
    for d in dates:
        if d[:7] != month:
            tot = sum(bal) if month else 1.0
            bal, month = [w * tot for w in weights], d[:7]
        tot = sum(bal)
        bal = [b * (1 + s.get(d, 0.0)) for b, s in zip(bal, sleeves)]
        pr.append(sum(bal) / tot - 1)
    return pr


# ----------------------------------------------------------------------------- main

def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log, out = [], [f"# Robustness batch — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n"]
    adjd = {s: adj_daily(s, key, "2006-01-01") for s in ("QQQ", "QLD", "BIL", "TLT", "GLD", "SPY")}
    bd = sorted(adjd["BIL"])
    bil_ret = {bd[i]: adjd["BIL"][bd[i]] / adjd["BIL"][bd[i - 1]] - 1 for i in range(1, len(bd))}
    q_ohlc = full_ohlc("QQQ", key, "2006-01-01")
    s_ohlc = full_ohlc("SPY", key, "2006-01-01")

    # ---------------- 1. SWING robustness
    qd, qC, qH, qL = arrays(q_ohlc, adjd["QQQ"])
    per = [("2007–2026", qd[201], qd[-1]), ("2008 crisis", "2007-10-01", "2009-06-30"),
           ("2018–2026", "2018-01-01", qd[-1]), ("2022", "2022-01-01", "2022-12-31")]
    hdr = "| Variant | " + " | ".join(p[0] for p in per) + " |\n|---|" + "---|" * len(per)
    out.append("## 1. SWING sleeve robustness (union of RSI2 + IBS + turn-of-month; CAGR / max DD)\n")
    out.append("### 1c. Parameter changes, one at a time, QQQ at 1x\n")
    out.append(hdr)
    variants = [("Baseline (RSI<10, exit >SMA5, IBS<0.2, TOM last 1 + first 3)", {}),
                ("RSI entry < 5", {"rsi_in": 5}), ("RSI entry < 15", {"rsi_in": 15}),
                ("RSI exit > SMA3", {"rsi_exit": "sma3"}), ("RSI exit RSI2 > 70", {"rsi_exit": "rsi70"}),
                ("IBS entry < 0.15", {"ibs_in": 0.15}), ("IBS entry < 0.25", {"ibs_in": 0.25}),
                ("TOM last 2 + first 2", {"tom": (2, 2)}), ("TOM last 1 + first 4", {"tom": (1, 4)}),
                ("Without TOM", {"parts": ("RSI2", "IBS")}), ("Without IBS", {"parts": ("RSI2", "TOM")}),
                ("Without RSI2", {"parts": ("IBS", "TOM")})]
    for lab, kw in variants:
        out.append(row(lab, swing(qd, qC, qH, qL, None, cash=bil_ret, **kw), qd, per))
    out.append("\n### 1b. Same rules on SPY vs QQQ (1x / 2x)\n")
    out.append(hdr)
    sd, sC, sH, sL = arrays(s_ohlc, adjd["SPY"])
    for lev in (1, 2):
        out.append(row(f"QQQ union {lev}x", swing(qd, qC, qH, qL, None, lev=lev, cash=bil_ret), qd, per))
        out.append(row(f"SPY union {lev}x", swing(sd, sC, sH, sL, None, lev=lev, cash=bil_ret), sd, per))
    b_q = {qd[i]: qC[i] / qC[i - 1] - 1 for i in range(1, len(qd))}
    b_s = {sd[i]: sC[i] / sC[i - 1] - 1 for i in range(1, len(sd))}
    out.append(row("QQQ buy & hold", b_q, qd, per))
    out.append(row("SPY buy & hold", b_s, sd, per))

    # 1a. 15:50 execution
    days = fetch_5min("QQQ", key, log)
    raw = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    X, XH, XL, n_sub = list(qC), list(qH), list(qL), 0
    for i, d in enumerate(qd):
        bars = days.get(d)
        if not bars or d not in raw:
            continue
        upto = [b for b in bars if b["t"] <= "15:45"]
        if len(upto) < 60:
            continue
        f = qC[i] / raw[d]                      # unadjusted -> adjusted scale for that day
        X[i] = upto[-1]["c"] * f
        XH[i] = max(b["h"] for b in upto) * f
        XL[i] = min(b["l"] for b in upto) * f
        n_sub += 1
    per18 = [("2018–2026", "2018-01-01", qd[-1]), ("2018–2021", "2018-01-01", "2021-12-31"),
             ("2022–2026", "2022-01-01", qd[-1]), ("2022", "2022-01-01", "2022-12-31")]
    out.append(f"\n### 1a. Execution: trade at the close vs decide-and-trade at 15:50 ET ({n_sub} sessions with 15:50 prices)\n")
    out.append("| Variant | " + " | ".join(p[0] for p in per18) + " |\n|---|" + "---|" * len(per18))
    for lev in (1, 2, 3):
        out.append(row(f"At the close, {lev}x", swing(qd, qC, qH, qL, None, lev=lev, cash=bil_ret), qd, per18))
        s1550 = swing(qd, qC, qH, qL, None, X=X, XH=XH, XL=XL, lev=lev, cash=bil_ret)
        out.append(row(f"At 15:50, {lev}x", s1550, qd, per18))
        if lev == 2:
            swing_1550_2x = s1550
    swing_close_2x = swing(qd, qC, qH, qL, None, lev=2, cash=bil_ret)

    # ---------------- 2. 2000-02 on ^NDX
    nd = full_ohlc("%5ENDX", key, "1985-01-01")
    rates = tbill_rates(key, log)
    out.append("\n## 2. Long history on the Nasdaq-100 index (^NDX, price only)\n")
    if not nd:
        out.append("_^NDX history not served on this FMP tier — skipped._\n")
    else:
        dd = sorted(nd)
        C = [nd[d][3] for d in dd]
        H = [nd[d][1] for d in dd]
        Lw = [nd[d][2] for d in dd]
        out.append(f"Index data: {dd[0]} → {dd[-1]}. Cash/financing: "
                   f"{'3-month T-bill (FMP)' if rates else 'flat 3%/yr (T-bill history not served)'}.\n")
        cash = {d: rate_on(rates, d) / 252 for d in dd}
        per_l = [("Full", dd[201], dd[-1]), ("1987 crash yr", "1987-01-01", "1987-12-31"),
                 ("2000–02 bust", "2000-03-01", "2002-12-31"), ("2007–09", "2007-10-01", "2009-06-30"),
                 ("2010–18", "2010-01-01", "2018-12-31"), ("2019–26", "2019-01-01", dd[-1])]
        out.append("| Strategy | " + " | ".join(p[0] for p in per_l) + " |\n|---|" + "---|" * len(per_l))
        fee = {1: 0.002, 2: 0.0095, 3: 0.0095}
        for lv in (1, 2, 3):
            for filt in (False, True):
                ser, on = {}, True
                for i in range(1, len(dd)):
                    d = dd[i]
                    r = C[i] / C[i - 1] - 1
                    if on:
                        ser[d] = lv * r - fee[lv] / 252 - (lv - 1) * rate_on(rates, d) / 252
                    else:
                        ser[d] = cash[d]
                    if filt and i >= 200:
                        want = C[i] > sum(C[i - 199:i + 1]) / 200
                        if want != on:
                            ser[d] -= 5e-4
                            on = want
                out.append(row(f"{lv}x NDX{' + 200d' if filt else ''}", ser, dd, per_l))
        for lv in (1, 2):
            s_nd = swing(dd, C, H, Lw, None, lev=lv, cash=cash)
            out.append(row(f"SWING union {lv}x (on ^NDX)", s_nd, dd, per_l))

    # ---------------- 3. CORE upgrades on real ETFs
    names = ("QQQ", "QLD", "BIL", "TLT", "GLD")
    cd = sorted(set.intersection(*(set(adjd[n]) for n in names)))
    P = {n: [adjd[n][d] for d in cd] for n in names}
    R = {n: [0.0] + [P[n][i] / P[n][i - 1] - 1 for i in range(1, len(cd))] for n in names}
    sig = [None] * len(cd)
    for i in range(200, len(cd)):
        sig[i] = P["QQQ"][i] > sum(P["QQQ"][i - 199:i + 1]) / 200

    def core(offmode="BIL", vt=None):
        ser, state = {}, None
        for i in range(202, len(cd)):
            d = cd[i]
            want = sig[i - 2]                      # decided at close i-2, filled at close i-1
            cost = 5e-4 if state is not None and want != state else 0.0
            state = want
            if want:
                if vt:
                    rv = statistics.pstdev(R["QQQ"][i - 21:i - 1]) * math.sqrt(252) or 1e-9
                    lv = min(2.0, vt / rv)
                    r = lv * R["QQQ"][i] - 0.00475 * lv / 252 - max(0.0, lv - 1) * R["BIL"][i]
                else:
                    r = R["QLD"][i]
            else:
                off = offmode
                if offmode == "DUAL":
                    best, bv = "BIL", P["BIL"][i - 1] / P["BIL"][i - 64] - 1
                    for a in ("TLT", "GLD"):
                        v = P[a][i - 1] / P[a][i - 64] - 1
                        if v > bv:
                            best, bv = a, v
                    off = best
                r = R[off][i]
            ser[d] = r - cost
        return ser

    cores = {"QLD + 200d → T-bills (baseline)": core(),
             "QLD + 200d → TLT": core("TLT"), "QLD + 200d → GLD": core("GLD"),
             "QLD + 200d → dual momentum (TLT/GLD/BIL)": core("DUAL"),
             "Vol-target 20% (≤2x) + 200d → T-bills": core(vt=0.20),
             "Vol-target 25% (≤2x) + 200d → T-bills": core(vt=0.25),
             "Vol-target 30% (≤2x) + 200d → T-bills": core(vt=0.30),
             "Vol-target 25% (≤2x) + 200d → dual momentum": core("DUAL", vt=0.25)}
    per_c = [("2007–2026", cd[202], cd[-1]), ("2008 crisis", "2007-10-01", "2009-06-30"),
             ("2018–2026", "2018-01-01", cd[-1]), ("2022", "2022-01-01", "2022-12-31")]
    out.append("\n## 3. CORE variants on real ETFs (CAGR / max DD)\n")
    out.append("| Core | " + " | ".join(p[0] for p in per_c) + " |\n|---|" + "---|" * len(per_c))
    for k, v in cores.items():
        out.append(row(k, v, cd, per_c))
    qqq_bh = {cd[i]: R["QQQ"][i] for i in range(1, len(cd))}
    out.append(row("QQQ buy & hold", qqq_bh, cd, per_c))

    # 40/30/30 with each core, day sleeve, swing (close and 15:50)
    rd, prev, j = sorted(raw), {}, 0
    for s in sorted(days):
        while j < len(rd) and rd[j] < s:
            j += 1
        if j:
            prev[s] = raw[rd[j - 1]]
    day = noise_series(days, prev, 14, 30, 3, 3e-4)
    pd = [d for d in sorted(days) if d in cores["QLD + 200d → T-bills (baseline)"] and d in swing_close_2x]
    out.append(f"\n## 3b. 40 / 30 / 30 CORE / DAY / SWING (2x), {pd[0]} → {pd[-1]}, monthly rebalance\n")
    out.append("| Core variant | Swing executed | CAGR | Max DD | Sharpe | Worst year |")
    out.append("|---|---|---|---|---|---|")
    q_st, q_y, _ = curve_stats([qqq_bh.get(d, 0.0) for d in pd], pd)
    out.append(f"| QQQ buy & hold | — | {q_st['cagr']:.1%} | {q_st['mdd']:.1%} | {q_st['sharpe']:.2f} | {min(q_y.values()):.1%} |")
    for k, cs in cores.items():
        for lab, sw in (("close", swing_close_2x), ("15:50", swing_1550_2x)):
            if lab == "15:50" and "baseline" not in k and "dual momentum" not in k:
                continue
            pr = combine([0.4, 0.3, 0.3], [cs, day, sw], pd)
            st, y, _ = curve_stats(pr, pd)
            out.append(f"| {k} | {lab} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | {min(y.values()):.1%} |")
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "robust_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
