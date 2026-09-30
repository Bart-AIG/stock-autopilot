"""
"Stocks in play" day-trading sleeve with trade plans fixed at entry and monitored on the
routine's cadence.  (Ryan, 2026-09-30: "each time it buys it should predetermine when to take
profit and loss based on the evaluated variables at purchase, then evaluate the purchase every
time the routine fires to make sure it is monitored well".)

Runs on GitHub Actions (FMP key). Pure standard library. ~2 years of 5-minute bars.

Universe: the pooled S&P 100 + Nasdaq-100 lists as of end-2018 (liquid large caps; chosen
before the test window, so no hindsight about which names ran).

Each session, at 09:35 ET:
  RVOL   first-5-minute volume / its own 14-session average at 09:30. Keep RVOL >= 1 (or a
         stricter cut), daily ATR(14) >= $0.50; rank by RVOL; take the top N ("in play").
  DIR    first 5-minute candle up -> long, down -> short (long-only is the realistic version:
         the account cannot short).
  ENTRY  a buy-stop resting at the opening-range high (sell-stop at the low for shorts); fills
         only if the breakout happens, before 15:00.
Trade plan fixed at entry from the variables measured then (DYNAMIC versions):
  STOP   D = ATR14 x s, with s = 0.15, +0.05 when RVOL > 4 (the most active names swing more).
  TARGET entry + D x m, m = 2, +1 if the trade is with the stock's daily trend (prior close vs
         its 20-day SMA), +1 if it is with QQQ's first 5-minute candle.
Monitoring every time the routine fires (every 15 minutes; 30 in one variant):
  * +1R -> stop to breakeven; +2R -> trail the stop 1D below the price.
  * price at or through the target -> take profit.
  * open >= 30 minutes and price on the wrong side of VWAP -> exit.
  * QQQ on the wrong side of its VWAP while the trade is not yet +1R -> exit.
  * 15:50 -> flat.
Execution realism: the protective stop rests at the broker only from the first routine fire
after the fill (the gap in between is unprotected, as live); resting stops fill at the stop
price, or at the bar open if the bar gaps through it. Each position is 1/N of the sleeve, 1x,
cash only. Costs 4 bp per round trip.
Reference: the published version (top 20, long/short, stop 10% of ATR active immediately, exit
at the close) with idealised fills.

Limits: ~2 years; one universe; 5-minute bars (no tick path inside a bar: when a bar touches
both the stop and the target, the stop is assumed first).
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from backtest import BASE, NDX100_2018, SP100_2018, _get
from combo_backtest import curve_stats
from robust_backtest import full_ohlc

HERE = Path(__file__).resolve().parent
START = (date.today() - timedelta(days=730)).isoformat()
COST = 4e-4
CHECK_EVERY = 15


def fetch5(sym, key, log):
    """5-minute bars keyed by session; adaptive chunking in case FMP truncates long ranges."""
    days = {}

    def grab(a, b):
        data = _get(f"{BASE}/historical-chart/5min?symbol={sym}&from={a}&to={b}&apikey={key}")
        return data if isinstance(data, list) else None

    d, end = date.fromisoformat(START), date.today()
    while d < end:
        e = min(d + timedelta(days=29), end)
        data = grab(d, e)
        if data:
            earliest = min(r["date"][:10] for r in data)
            if earliest > (d + timedelta(days=4)).isoformat():       # truncated -> weekly chunks
                data = []
                w = d
                while w <= e:
                    x = grab(w, min(w + timedelta(days=6), e)) or []
                    data += x
                    w += timedelta(days=7)
            for r in data:
                ts = r["date"]
                days.setdefault(ts[:10], []).append(
                    {"t": ts[11:16], "o": float(r["open"]), "h": float(r["high"]), "l": float(r["low"]),
                     "c": float(r["close"]), "v": float(r.get("volume") or 0)})
        elif not days:
            log.append(f"{sym}: 5min not served")
            return {}
        d = e + timedelta(days=1)
        time.sleep(0.1)
    out = {}
    for k, v in days.items():
        b = sorted((x for x in v if "09:30" <= x["t"] <= "15:55"), key=lambda x: x["t"])
        uniq, seen = [], set()
        for x in b:
            if x["t"] not in seen:
                seen.add(x["t"]), uniq.append(x)
        if len(uniq) >= 70 and uniq[0]["t"] == "09:30":
            out[k] = uniq
    return out


def minutes(t):
    return int(t[:2]) * 60 + int(t[3:])


def is_check(bar_t, every):
    """True if a routine fires at the END of this 5-minute bar."""
    end = minutes(bar_t) + 5
    return (end - 570) % every == 0


def vwap_series(bars):
    out, pv, vv = [], 0.0, 0.0
    for b in bars:
        tp = (b["h"] + b["l"] + b["c"]) / 3
        pv += tp * b["v"]
        vv += b["v"]
        out.append(pv / vv if vv else b["c"])
    return out


def simulate(cfg, sess, intr, daily, qqq):
    """Returns list of (session, trade_return, R, exit_reason) and per-session sleeve returns."""
    N, every = cfg["N"], cfg.get("every", CHECK_EVERY)
    trades, day_ret = [], {}
    names = [s for s in intr if s != "QQQ"]
    for di, s in enumerate(sess):
        if di < 15:
            continue
        hist = sess[di - 14:di]
        q = qqq.get(s)
        q_dir = (1 if q[0]["c"] > q[0]["o"] else -1) if q else 0
        q_vwap = vwap_series(q) if q else None
        cands = []
        for sym in names:
            b = intr[sym].get(s)
            dv = daily.get(sym)
            if not b or not dv or s not in dv["idx"]:
                continue
            i = dv["idx"][s]
            if i < 21:
                continue
            v0s = [intr[sym][h][0]["v"] for h in hist if h in intr[sym]]
            if len(v0s) < 10 or not sum(v0s):
                continue
            rvol = b[0]["v"] / (sum(v0s) / len(v0s))
            o, hi, lo, cl = dv["o"], dv["h"], dv["l"], dv["c"]
            trs = [max(hi[k] - lo[k], abs(hi[k] - cl[k - 1]), abs(lo[k] - cl[k - 1])) for k in range(i - 14, i)]
            atr = sum(trs) / 14
            prev = cl[i - 1]
            if abs(b[0]["o"] / prev - 1) > 0.3 or atr < 0.5 or b[0]["c"] < 5:
                continue
            if rvol < cfg.get("rvol_min", 1.0):
                continue
            sma20 = sum(cl[i - 20:i]) / 20
            cands.append((rvol, sym, atr, prev > sma20))
        cands.sort(reverse=True)
        rets = []
        for rvol, sym, atr, up_trend in cands[:N]:
            b = intr[sym][s]
            first = b[0]
            if first["c"] == first["o"]:
                continue
            d = 1 if first["c"] > first["o"] else -1
            if cfg.get("long_only") and d < 0:
                continue
            level = first["h"] if d > 0 else first["l"]
            vw = vwap_series(b)
            # entry: resting stop order at the range edge, until 15:00
            fill_k, entry = None, None
            for k in range(1, len(b)):
                if b[k]["t"] >= "15:00":
                    break
                if (b[k]["h"] >= level) if d > 0 else (b[k]["l"] <= level):
                    entry = max(level, b[k]["o"]) if d > 0 else min(level, b[k]["o"])
                    fill_k = k
                    break
            if fill_k is None:
                continue
            if cfg.get("dynamic"):
                s_mult = 0.15 + (0.05 if rvol > 4 else 0.0)
                D = atr * s_mult
                m = 2.0 + (1.0 if (up_trend == (d > 0)) else 0.0) + (1.0 if q_dir == d else 0.0)
                target = entry + d * D * m
            else:
                D = atr * cfg.get("stop_atr", 0.10)
                target = None
            stop = entry - d * D
            stop_live = cfg.get("ideal", False)
            exit_px, reason = None, None
            for k in range(fill_k, len(b)):
                bar = b[k]
                # resting stop (intrabar), only once it has been placed
                if stop_live and k > fill_k:
                    hit = (bar["l"] <= stop) if d > 0 else (bar["h"] >= stop)
                    if hit:
                        gap_through = (bar["o"] < stop) if d > 0 else (bar["o"] > stop)
                        exit_px, reason = (bar["o"] if gap_through else stop), "stop"
                        break
                if bar["t"] >= "15:50" or k == len(b) - 1:
                    exit_px, reason = bar["c"], "time"
                    break
                if not is_check(bar["t"], every) or cfg.get("ideal"):
                    continue
                # ---- the routine fires at the end of this bar
                px = bar["c"]
                if not stop_live:
                    stop_live = True
                    if (px <= stop) if d > 0 else (px >= stop):      # breached before protection
                        exit_px, reason = px, "stop (before protected)"
                        break
                if not cfg.get("dynamic"):
                    continue
                r_now = (px - entry) * d / D
                if target is not None and ((px >= target) if d > 0 else (px <= target)):
                    exit_px, reason = px, "target"
                    break
                if r_now >= 2:
                    stop = max(stop, px - D) if d > 0 else min(stop, px + D)
                elif r_now >= 1:
                    stop = max(stop, entry) if d > 0 else min(stop, entry)
                open_min = minutes(bar["t"]) + 5 - (minutes(b[fill_k]["t"]) + 5)
                if cfg.get("vwap_rule", True) and open_min >= 30 and ((px < vw[k]) if d > 0 else (px > vw[k])):
                    exit_px, reason = px, "lost VWAP"
                    break
                if cfg.get("mkt_rule", True) and q and r_now < 1:
                    qk = next((j for j, x in enumerate(q) if x["t"] == bar["t"]), None)
                    if qk is not None and ((q[qk]["c"] < q_vwap[qk]) if d > 0 else (q[qk]["c"] > q_vwap[qk])):
                        exit_px, reason = px, "market turned"
                        break
            r = (exit_px / entry - 1) * d - COST
            trades.append((s, r, (exit_px - entry) * d / D, reason))
            rets.append(r)
        day_ret[s] = sum(rets) / N
    return trades, day_ret


VARIANTS = [
    ("Published (top 20, long/short, 0.1 ATR stop active at once, exit at close, ideal fills)",
     {"N": 20, "ideal": True, "stop_atr": 0.10}),
    ("Published rules, long-only, ideal fills", {"N": 20, "ideal": True, "stop_atr": 0.10, "long_only": True}),
    ("Realistic plain: top 10, long-only, 0.1 ATR stop from next fire, exit 15:50", {"N": 10, "long_only": True, "stop_atr": 0.10}),
    ("DYNAMIC: top 10, long-only, plan set at entry + 15-min monitoring", {"N": 10, "long_only": True, "dynamic": True}),
    ("DYNAMIC, long/short (reference - cannot short)", {"N": 10, "dynamic": True}),
    ("DYNAMIC, top 5", {"N": 5, "long_only": True, "dynamic": True}),
    ("DYNAMIC, RVOL >= 2", {"N": 10, "long_only": True, "dynamic": True, "rvol_min": 2.0}),
    ("DYNAMIC, RVOL >= 3", {"N": 10, "long_only": True, "dynamic": True, "rvol_min": 3.0}),
    ("DYNAMIC without the VWAP exit", {"N": 10, "long_only": True, "dynamic": True, "vwap_rule": False}),
    ("DYNAMIC without the market (QQQ) exit", {"N": 10, "long_only": True, "dynamic": True, "mkt_rule": False}),
    ("DYNAMIC, routine every 30 min", {"N": 10, "long_only": True, "dynamic": True, "every": 30}),
]


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    names = sorted(set(SP100_2018) | set(NDX100_2018))
    intr, daily = {}, {}
    for n, sym in enumerate(names + ["QQQ"]):
        b = fetch5(sym, key, log)
        o = full_ohlc(sym, key, (date.today() - timedelta(days=800)).isoformat())
        if b and o:
            intr[sym] = b
            ds = sorted(o)
            daily[sym] = {"idx": {d: i for i, d in enumerate(ds)}, "o": [o[d][0] for d in ds],
                          "h": [o[d][1] for d in ds], "l": [o[d][2] for d in ds], "c": [o[d][3] for d in ds]}
        print(f"{n + 1}/{len(names) + 1} {sym}: {len(b) if b else 0} sessions", flush=True)
    qqq = intr.get("QQQ", {})
    sess = sorted(qqq)
    out = [f"# Stocks-in-play day-trading test — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"{len(intr) - 1} names with 5-minute data, {len(sess)} sessions ({sess[0]} → {sess[-1]}). "
           "Returns are for the day-trading sleeve itself (1x, cash, flat every night).\n"]
    q_rets = {}
    for i in range(1, len(sess)):
        q_rets[sess[i]] = qqq[sess[i]][-1]["c"] / qqq[sess[i - 1]][-1]["c"] - 1
    dd = sess[15:]
    half = dd[len(dd) // 2]
    qs, _, _ = curve_stats([q_rets.get(d, 0.0) for d in dd], dd)
    out.append(f"QQQ buy & hold over the same sessions: {qs['cagr']:.1%}/yr, max DD {qs['mdd']:.0%}.\n")
    out.append("| Version | CAGR | Max DD | Sharpe | 1st year | 2nd year | Trades/day | Win % | Avg R | Avg trade | Exit mix |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for label, cfg in VARIANTS:
        trades, dr = simulate(cfg, sess, intr, daily, qqq)
        st, _, _ = curve_stats([dr.get(d, 0.0) for d in dd], dd)
        a = [d for d in dd if d < half]
        b = [d for d in dd if d >= half]
        s1, _, _ = curve_stats([dr.get(d, 0.0) for d in a], a)
        s2, _, _ = curve_stats([dr.get(d, 0.0) for d in b], b)
        n = len(trades)
        mix = {}
        for t in trades:
            mix[t[3]] = mix.get(t[3], 0) + 1
        mix_s = ", ".join(f"{k} {v / n:.0%}" for k, v in sorted(mix.items(), key=lambda x: -x[1])) if n else ""
        out.append(f"| {label} | {st['cagr']:.1%} | {st['mdd']:.0%} | {st['sharpe']:.2f} | {s1['cagr']:.1%} | {s2['cagr']:.1%} | "
                   f"{n / len(dd):.1f} | {sum(1 for t in trades if t[1] > 0) / n:.0%} | "
                   f"{statistics.mean(t[2] for t in trades):+.2f} | {statistics.mean(t[1] for t in trades) * 1e4:+.1f} bp | {mix_s} |"
                   if n else f"| {label} | no trades | | | | | | | | | |")
        print(label, f"{st['cagr']:.1%}", flush=True)
    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:30] or ["(clean)"]))
    (HERE / "sip_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
