"""
Swing sleeve backtest — overnight and multi-day index swings, alone and combined with
the CORE (QLD + 200-day switch) and DAY (3x noise-area breakout) sleeves.
(Ryan, 2026-09-29: "lets add one more strategy that is geared towards overnight and
weekly swings".)

Runs on GitHub Actions (FMP key). Pure standard library.

Candidate SWING rules on QQQ (published/standard, parameters not tuned):
  OVERNIGHT      Buy at the close, sell at the next open (the "overnight drift"; most of
                 QQQ's return accrues outside the session). Variant: only while QQQ is
                 above its 200-day SMA.
  RSI2           Connors & Alvarez: buy at the close when RSI(2) < 10 and QQQ > 200-day
                 SMA; sell at the close when QQQ closes above its 5-day SMA. ~2-5 day holds.
  IBS            Internal bar strength = (close-low)/(high-low). Buy at the close when
                 IBS < 0.2 and QQQ > 200-day SMA; sell at the close when IBS > 0.8 or
                 after 5 sessions.
  TOM            Turn of the month (Lakonishok & Smidt 1988; McConnell & Xu 2008): hold
                 for the last trading day of the month and the first 3 of the next.
  SWING_UNION    In the market whenever RSI2, IBS or TOM is active (one position).
Each at 1x (QQQ), 2x (QLD-style) and 3x (TQQQ-style): L x QQQ's move for the holding
window, costs 1 bp per side per 1x of exposure. Idle cash earns T-bills (BIL).

Limits: leveraged sleeves are modelled as exactly L x QQQ over the holding window (a
daily-reset fund matches that for close->close and close->open holds). Unadjusted
opens are used for overnight returns (dividend gaps included, ~0.6%/yr drag).
One historical path; taxes ignored.
"""

from __future__ import annotations

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
START_CAPITAL = 3340.0
FEE = 1e-4          # per side per 1x of exposure


def full_ohlc(sym, key, start="2006-06-01"):
    data = _get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={start}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return {}
    return {r["date"][:10]: (float(r["open"]), float(r["high"]), float(r["low"]), float(r["close"]))
            for r in data if r.get("open") and r.get("close")}


def swing_series(ohlc, adj, bil_ret, L):
    """Daily net return on capital for each SWING rule, keyed by date (return from the
    prior close to this close; OVERNIGHT books close->open and sits in cash intraday)."""
    dates = [d for d in sorted(ohlc) if d in adj]
    closes = [ohlc[d][3] for d in dates]
    out = {k: {} for k in ("OVERNIGHT", "OVERNIGHT >200d", "RSI2", "IBS", "TOM", "SWING_UNION")}
    month_idx = {}
    for i, d in enumerate(dates):
        month_idx.setdefault(d[:7], []).append(i)
    last_of_month = {m: ix[-1] for m, ix in month_idx.items()}
    first3 = {i for ix in month_idx.values() for i in ix[:3]}
    tom_days = first3 | set(last_of_month.values())
    pos = {"RSI2": 0, "IBS": 0}
    held = {"RSI2": False, "IBS": False, "TOM": False, "SWING_UNION": False}
    age_ibs = 0
    for i in range(201, len(dates)):
        d, p = dates[i], dates[i - 1]
        r_cc = adj[d] / adj[p] - 1
        r_on = ohlc[d][0] / ohlc[p][3] - 1
        cash = bil_ret.get(d, 0.0)
        sma200_p = sum(closes[i - 200:i]) / 200
        up_p = closes[i - 1] > sma200_p
        # overnight: decided at the prior close
        out["OVERNIGHT"][d] = L * r_on - 2 * FEE * L
        out["OVERNIGHT >200d"][d] = (L * r_on - 2 * FEE * L) if up_p else cash
        # positions held over day d were set at the close of day p (flags in `held`)
        for k in ("RSI2", "IBS", "TOM", "SWING_UNION"):
            out[k][d] = L * r_cc if held[k] else cash
        # ---- decide at the close of d for tomorrow
        c = closes[i]
        o, h, l, _ = ohlc[d]
        sma200 = sum(closes[i - 199:i + 1]) / 200
        sma5 = sum(closes[i - 4:i + 1]) / 5
        r2 = compute_rsi(closes[i - 59:i + 1], 2)
        new = {}
        if held["RSI2"]:
            new["RSI2"] = not (c > sma5)
        else:
            new["RSI2"] = r2 is not None and r2 < 10 and c > sma200
        ibs = (c - l) / (h - l) if h > l else 0.5
        if held["IBS"]:
            age_ibs += 1
            new["IBS"] = not (ibs > 0.8 or age_ibs >= 5)
        else:
            new["IBS"] = ibs < 0.2 and c > sma200
            age_ibs = 0
        new["TOM"] = (i + 1) in tom_days
        new["SWING_UNION"] = new["RSI2"] or new["IBS"] or new["TOM"]
        for k in new:
            if new[k] != held[k]:
                for kk in (k,):
                    # charge the switch on the day it happens
                    out[kk][d] -= FEE * L
            held[k] = new[k]
    return dates[201:], out


def combine(weights, sleeves, dates):
    """weights: list of floats summing to 1; sleeves: list of dict date->ret. Monthly rebalance."""
    bal, month, pr = list(weights), None, []
    for d in dates:
        if d[:7] != month:
            tot = sum(bal) if month else 1.0
            bal, month = [w * tot for w in weights], d[:7]
        tot = sum(bal)
        bal = [b * (1 + s.get(d, 0.0)) for b, s in zip(bal, sleeves)]
        pr.append(sum(bal) / tot - 1)
    return pr


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    ohlc = full_ohlc("QQQ", key)
    adj = adj_daily("QQQ", key, "2006-06-01")
    qld = adj_daily("QLD", key, "2006-06-01")
    bil = adj_daily("BIL", key, "2006-06-01")
    if not (ohlc and adj and qld and bil):
        sys.exit("missing daily data")
    bd = sorted(bil)
    bil_ret = {bd[i]: bil[bd[i]] / bil[bd[i - 1]] - 1 for i in range(1, len(bd))}
    qd = sorted(d for d in adj if d in qld and d in bil)
    qqq_ret = {qd[i]: adj[qd[i]] / adj[qd[i - 1]] - 1 for i in range(1, len(qd))}

    out = [f"# Swing sleeve backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           __doc__.split("Candidate SWING rules on QQQ (published/standard, parameters not tuned):")[1]
           .split("Limits:")[0].strip() + "\n"]

    # ---------- swing rules alone, long history
    series = {}
    for L in (1, 2, 3):
        sd, ser = swing_series(ohlc, adj, bil_ret, L)
        series[L] = (sd, ser)
    sd = series[1][0]
    periods = [("2007–2026", sd[0], sd[-1]), ("2008 crisis (2007-10 → 2009-06)", "2007-10-01", "2009-06-30"),
               ("2018–2026", "2018-01-01", sd[-1]), ("2022", "2022-01-01", "2022-12-31")]
    out.append(f"## Swing rules alone, {sd[0]} → {sd[-1]} (CAGR / max drawdown)\n")
    out.append("| Rule | Lev | " + " | ".join(p[0] for p in periods) + " | Time in market |")
    out.append("|---|---|" + "---|" * len(periods) + "---|")
    bh = {d: qqq_ret.get(d, 0.0) for d in sd}
    for name, ser in [("QQQ buy & hold", {1: bh})] + [(k, None) for k in series[1][1]]:
        for L in ((1,) if ser else (1, 2, 3)):
            s = ser[1] if ser else series[L][1][name]
            cells = []
            for _, a, b in periods:
                dd = [d for d in sd if a <= d <= b]
                st, _, _ = curve_stats([s.get(d, 0.0) for d in dd], dd)
                cells.append(f"{st['cagr']:.1%} / {st['mdd']:.0%}")
            if ser:
                tim = "100%"
            elif name.startswith("OVERNIGHT"):
                tim = f"{sum(1 for d in sd if s[d] != bil_ret.get(d, 0.0)) / len(sd):.0%} of nights"
            else:
                tim = f"{sum(1 for d in sd if abs(s[d] - bil_ret.get(d, 0.0)) > 1e-12) / len(sd):.0%}"
            out.append(f"| {name} | {L}x | " + " | ".join(cells) + f" | {tim} |")

    # ---------- the three-sleeve portfolio (needs the intraday data: 2018+)
    raw = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    days = fetch_5min("QQQ", key, log)
    rd, prev, j = sorted(raw), {}, 0
    for s in sorted(days):
        while j < len(rd) and rd[j] < s:
            j += 1
        if j:
            prev[s] = raw[rd[j - 1]]
    sig = {}
    for i in range(200, len(qd)):
        sig[qd[i]] = adj[qd[i]] > sum(adj[qd[k]] for k in range(i - 199, i + 1)) / 200
    core, state = {}, None
    for i in range(202, len(qd)):
        d, p = qd[i], qd[i - 1]
        want = sig[qd[i - 2]]
        cost = 5e-4 if state is not None and want != state else 0.0
        state = want
        core[d] = ((qld[d] / qld[p] - 1) if state else (bil[d] / bil[p] - 1)) - cost
    day = noise_series(days, prev, 14, 30, 3, 3e-4)
    cd = [d for d in sorted(days) if d in core and d in series[1][1]["RSI2"]]

    swing_opts = {"SWING_UNION 3x": series[3][1]["SWING_UNION"], "SWING_UNION 2x": series[2][1]["SWING_UNION"],
                  "OVERNIGHT >200d 3x": series[3][1]["OVERNIGHT >200d"]}
    corr_rows = []
    for nm, s in swing_opts.items():
        x = [s.get(d, 0.0) for d in cd]
        corr_rows.append(f"{nm}: vs CORE {statistics.correlation(x, [core[d] for d in cd]):+.2f}, "
                         f"vs DAY {statistics.correlation(x, [day.get(d, 0.0) for d in cd]):+.2f}")
    out.append(f"\n## Three-sleeve portfolios, {cd[0]} → {cd[-1]} (monthly rebalance)\n")
    out.append("CORE = QLD while QQQ > 200-day SMA else T-bills. DAY = 3x noise-area breakout (14-day, 30-min). "
               "SWING = the rule named in the section header.\n")
    out.append("Daily correlations — " + "; ".join(corr_rows) + ".\n")
    splits = [(100, 0, 0), (50, 50, 0), (60, 40, 0), (50, 25, 25), (40, 30, 30), (40, 40, 20),
              (34, 33, 33), (30, 40, 30), (60, 20, 20), (50, 0, 50), (0, 50, 50), (0, 0, 100)]
    q_st, q_y, q_end = curve_stats([qqq_ret[d] for d in cd], cd)
    for nm, sw in swing_opts.items():
        out.append(f"### SWING = {nm}\n")
        out.append("| CORE / DAY / SWING | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |")
        out.append("|---|---|---|---|---|---|")
        out.append(f"| QQQ buy & hold | {q_st['cagr']:.1%} | {q_st['mdd']:.1%} | {q_st['sharpe']:.2f} | "
                   f"{min(q_y.values()):.1%} | ${START_CAPITAL * q_end:,.0f} |")
        yr_rows = [("QQQ buy & hold", q_y)]
        for c, dy, s in splits:
            pr = combine([c / 100, dy / 100, s / 100], [core, day, sw], cd)
            st, y, end = curve_stats(pr, cd)
            lab = f"{c} / {dy} / {s}"
            out.append(f"| {lab} | {st['cagr']:.1%} | {st['mdd']:.1%} | {st['sharpe']:.2f} | "
                       f"{min(y.values()):.1%} | ${START_CAPITAL * end:,.0f} |")
            if (c, dy, s) in ((50, 50, 0), (40, 30, 30), (34, 33, 33), (0, 0, 100)):
                yr_rows.append((lab, y))
        yrs = sorted(q_y)
        out.append("\n| Split | " + " | ".join(yrs) + " |")
        out.append("|---|" + "---|" * len(yrs))
        for lab, y in yr_rows:
            out.append(f"| {lab} | " + " | ".join(f"{y.get(k, 0):.1%}" for k in yrs) + " |")
        out.append("")
    out.append("## Data log\n")
    out.extend(f"- {x}" for x in (log[:20] or ["(clean)"]))
    (HERE / "swing_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
