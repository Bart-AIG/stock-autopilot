"""
Intraday strategy backtest — which day-trading methods, if any, earn more than the
capital would earn elsewhere?  (Ryan, 2026-09-29: "Are there other day trading
strategies that we can test?")

Runs on GitHub Actions (FMP key). 5-minute bars (1-minute is paywalled on this tier)
for QQQ and SPY, as far back as FMP serves them. Every strategy is flat at the close,
so it only uses capital intraday; the hurdle it must clear is what that capital would
earn in the core (QQQ ~16-23%/yr in the tests, QLD+200d ~20-34%).

Strategies (all published or standard; parameters are the published ones, not tuned):
  ORB-k      Opening-range breakout, range = first k minutes (5/15/30). Direction =
             range close vs open; enter next bar's open; stop at the opposite range
             extreme; 10R target; else exit at the close (Zarattini & Aziz 2023).
  ORB-k long-only / trend   Only longs; or longs above / shorts below the 200-day SMA.
  IMOM       Intraday momentum (Gao, Han, Li & Zhou, JFE 2018): the return from the
             prior close to 10:00 predicts the last half hour; trade 15:30 -> close.
  NOISE      Noise-area breakout (Zarattini, Aziz & Barbon 2024, "Beat the Market"):
             band = open (or prior close) +/- the 14-day average absolute move from the
             open at that time of day; checked every 30 min; enter on a close outside
             the band; exit when price closes back through max(band, VWAP) or at the close.
  GAP_FADE / GAP_GO   Gap > 0.3% vs prior close: fade it toward the prior close
             (target = prior close), or go with it; enter 09:35, exit at the close.
  OVERNIGHT / INTRADAY   Close -> next open vs open -> close (reference: where the
             index's return actually accrues).

Costs: 1 bp per side at 1x (QQQ/SPY spread is ~0.15 bp; the rest is slippage);
a 3x row scales returns by 3 and charges 3 bp per side (TQQQ/UPRO-style vehicle,
intraday only, so no overnight decay).

Honest limits (also printed): single path of history; 5-minute bars mean stops fill at
the stop price with no gap-through inside a bar; no borrow/short constraints beyond
using an inverse ETF; results are gross of taxes.
"""

from __future__ import annotations

import json
import math
import os
import statistics
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from backtest import BASE, _get, fetch_daily, stats, yearly

HERE = Path(__file__).resolve().parent
START = "2018-01-01"
COST = {1: 1e-4, 3: 3e-4}


def fetch_unadjusted(sym: str, key: str) -> list[dict]:
    """Raw (unadjusted) daily closes, to match the unadjusted intraday bars. Using the
    dividend-adjusted series here manufactures a fake overnight gap every day."""
    data = _get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return []
    return sorted(({"date": r["date"][:10], "price": float(r["close"])} for r in data if r.get("close")),
                  key=lambda r: r["date"])


def fetch_5min(sym: str, key: str, log: list[str]) -> dict[str, list[dict]]:
    days: dict[str, list[dict]] = {}
    d, end = date.fromisoformat(START), date.today()
    empty_run = 0
    while d < end:
        e = min(d + timedelta(days=6), end)
        data = _get(f"{BASE}/historical-chart/5min?symbol={sym}&from={d}&to={e}&apikey={key}")
        if isinstance(data, list) and data:
            empty_run = 0
            for r in data:
                ts = r["date"]
                days.setdefault(ts[:10], []).append(
                    {"t": ts[11:16], "o": float(r["open"]), "h": float(r["high"]),
                     "l": float(r["low"]), "c": float(r["close"]), "v": float(r.get("volume") or 0)})
        else:
            empty_run += 1
            if not isinstance(data, list):
                log.append(f"{sym} 5min {d}..{e}: {str(data)[:80]}")
        d = e + timedelta(days=1)
        time.sleep(0.15)
    for k in list(days):
        bars = sorted((b for b in days[k] if "09:30" <= b["t"] <= "15:55"), key=lambda b: b["t"])
        # dedupe identical timestamps
        seen, uniq = set(), []
        for b in bars:
            if b["t"] not in seen:
                seen.add(b["t"]), uniq.append(b)
        if len(uniq) >= 70:          # a full session is 78 bars; drop half days / holes
            days[k] = uniq
        else:
            del days[k]
    return days


# ----------------------------------------------------------------------------- strategies
# each returns (gross return on capital for the day at 1x, number of round trips) or (0, 0)

def orb(bars, k, prev_close, mode="both", trend_up=None, risk_cap=None):
    """risk_cap=None -> 1x notional. Otherwise the paper's sizing: notional = 1% of
    capital / stop distance, capped at risk_cap x capital. Returns (r, n, weight)."""
    n = k // 5
    rng_b, rest = bars[:n], bars[n:]
    hi, lo = max(b["h"] for b in rng_b), min(b["l"] for b in rng_b)
    op, cl = rng_b[0]["o"], rng_b[-1]["c"]
    if cl == op or hi <= lo:
        return 0.0, 0, 0
    long = cl > op
    if mode == "long" and not long:
        return 0.0, 0, 0
    if mode == "trend" and trend_up is not None and long != trend_up:
        return 0.0, 0, 0
    entry = rest[0]["o"]
    stop = lo if long else hi
    risk = abs(entry - stop)
    if risk <= 0:
        return 0.0, 0, 0
    w = 1.0 if risk_cap is None else min(risk_cap, 0.01 / (risk / entry))
    tgt = entry + (10 * risk if long else -10 * risk)
    for b in rest:
        if (b["l"] <= stop) if long else (b["h"] >= stop):
            x = stop
            break
        if (b["h"] >= tgt) if long else (b["l"] <= tgt):
            x = tgt
            break
    else:
        x = rest[-1]["c"]
    return ((x / entry - 1) if long else (1 - x / entry)), 1, w


def imom(bars, prev_close):
    t = {b["t"]: b for b in bars}
    if "09:55" not in t or "15:30" not in t or not prev_close:
        return 0.0, 0
    r1 = t["09:55"]["c"] / prev_close - 1
    if r1 == 0:
        return 0.0, 0
    entry, x = t["15:30"]["o"], bars[-1]["c"]
    return ((x / entry - 1) if r1 > 0 else (1 - x / entry)), 1


def noise(bars, prev_close, sigma):
    """sigma: dict time -> avg |close_t/open - 1| over the prior 14 sessions."""
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
        if end_min % 30 != 0 or b["t"] == bars[-1]["t"]:
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


def gap(bars, prev_close, fade=True, th=0.003):
    if not prev_close:
        return 0.0, 0
    g = bars[0]["o"] / prev_close - 1
    if abs(g) < th:
        return 0.0, 0
    short = (g > 0) == fade
    entry = bars[1]["o"]
    x = bars[-1]["c"]
    if fade and ((prev_close < entry) if short else (prev_close > entry)):
        for b in bars[1:]:
            if (b["l"] <= prev_close) if short else (b["h"] >= prev_close):
                x = prev_close
                break
    return ((1 - x / entry) if short else (x / entry - 1)), 1


# ----------------------------------------------------------------------------- runner

def evaluate(sym, days, daily):
    closes = {r["date"]: r["price"] for r in daily}
    dl = sorted(closes)
    sessions = sorted(days)
    # prior close, 200d trend and noise sigma per session
    prev, trend = {}, {}
    for s in sessions:
        before = [d for d in dl if d < s]
        if before:
            prev[s] = closes[before[-1]]
            w = [closes[d] for d in before[-200:]]
            trend[s] = (closes[before[-1]] > sum(w) / len(w)) if len(w) == 200 else None
    moves = {}
    for s in sessions:
        op = days[s][0]["o"]
        moves[s] = {b["t"]: abs(b["c"] / op - 1) for b in days[s]}
    strat = {
        "ORB-5": lambda s, b: orb(b, 5, prev.get(s)),
        "ORB-15": lambda s, b: orb(b, 15, prev.get(s)),
        "ORB-30": lambda s, b: orb(b, 30, prev.get(s)),
        "ORB-5 long-only": lambda s, b: orb(b, 5, prev.get(s), "long"),
        "ORB-5 with 200d trend": lambda s, b: orb(b, 5, prev.get(s), "trend", trend.get(s)),
        "ORB-5 risk-sized, cap 1x (cash)": lambda s, b: orb(b, 5, prev.get(s), risk_cap=1.0),
        "ORB-5 risk-sized, cap 3x (via 3x ETF)": lambda s, b: orb(b, 5, prev.get(s), risk_cap=3.0),
        "ORB-5 risk-sized, cap 4x (paper)": lambda s, b: orb(b, 5, prev.get(s), risk_cap=4.0),
        "IMOM (15:30→close)": lambda s, b: imom(b, prev.get(s)),
        "NOISE-area breakout": None,
        "GAP_FADE >0.3%": lambda s, b: gap(b, prev.get(s), True),
        "GAP_GO >0.3%": lambda s, b: gap(b, prev.get(s), False),
    }
    res = {k: [] for k in strat}
    res["OVERNIGHT (close→open)"] = []
    res["INTRADAY (open→close)"] = []
    res[f"{sym} buy & hold"] = []
    for i, s in enumerate(sessions):
        b = days[s]
        p = prev.get(s)
        if p is None:
            continue
        for k, f in strat.items():
            if k == "NOISE-area breakout":
                hist_s = sessions[max(0, i - 14):i]
                if len(hist_s) < 14:
                    res[k].append((s, 0.0, 0, 1.0))
                    continue
                sig = {}
                for bar in b:
                    vals = [moves[h].get(bar["t"]) for h in hist_s if bar["t"] in moves[h]]
                    if len(vals) >= 10:
                        sig[bar["t"]] = sum(vals) / len(vals)
                r, n = noise(b, p, sig)
            else:
                o = f(s, b)
                r, n = o[0], o[1]
                if len(o) == 3:
                    res[k].append((s, r, n, o[2]))
                    continue
            res[k].append((s, r, n, 1.0))
        res["OVERNIGHT (close→open)"].append((s, b[0]["o"] / p - 1, 1, 1.0))
        res["INTRADAY (open→close)"].append((s, b[-1]["c"] / b[0]["o"] - 1, 1, 1.0))
        res[f"{sym} buy & hold"].append((s, b[-1]["c"] / p - 1, 0, 1.0))
    return res


def summarize(rows, lev):
    eq, curve, dates = 1.0, [], []
    traded = [r for _, r, n, _ in rows if n]
    for d, r, n, w in rows:
        net = lev * w * r - 2 * COST[lev] * n * w
        eq *= 1 + net
        curve.append(eq)
        dates.append(d)
    st = stats(curve, dates)
    wins = [r for r in traded if r > 0]
    return st, yearly(curve, dates), {
        "days": sum(1 for _, _, n, _ in rows if n), "trades": sum(n for _, _, n, _ in rows),
        "win": len(wins) / len(traded) if traded else 0,
        "avg_bp": statistics.mean(traded) * 1e4 if traded else 0}


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log, out = [], [f"# Intraday strategy backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n"]
    out.append(__doc__.split("Strategies")[0].strip().split("\n\n", 1)[1] + "\n")
    for sym in ("QQQ", "SPY"):
        daily = fetch_unadjusted(sym, key)
        days = fetch_5min(sym, key, log)
        if not days or not daily:
            out.append(f"## {sym}: no 5-minute data\n")
            continue
        sess = sorted(days)
        res = evaluate(sym, days, daily)
        out.append(f"## {sym} — {len(sess)} full sessions, {sess[0]} → {sess[-1]}\n")
        out.append("| Strategy | CAGR 1x | Max DD 1x | Sharpe 1x | CAGR 3x | Max DD 3x | Days traded | Trades | Win % | Avg trade (bp, gross) |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        yr_rows = []
        for k, rows in res.items():
            s1, y1, m = summarize(rows, 1)
            if k.endswith("buy & hold"):
                out.append(f"| **{k}** | {s1['cagr']:.1%} | {s1['mdd']:.1%} | {s1['sharpe']:.2f} | | | 100% | | | |")
                yr_rows.append((k, y1))
                continue
            if "risk-sized" in k:
                out.append(f"| {k} | {s1['cagr']:.1%} | {s1['mdd']:.1%} | {s1['sharpe']:.2f} | (sized) | | "
                           f"{m['days'] / len(rows):.0%} | {m['trades']} | {m['win']:.0%} | {m['avg_bp']:+.1f} |")
                yr_rows.append((k, y1))
                continue
            s3, _, _ = summarize(rows, 3)
            out.append(f"| {k} | {s1['cagr']:.1%} | {s1['mdd']:.1%} | {s1['sharpe']:.2f} | {s3['cagr']:.1%} | "
                       f"{s3['mdd']:.1%} | {m['days'] / len(rows):.0%} | {m['trades']} | {m['win']:.0%} | {m['avg_bp']:+.1f} |")
            yr_rows.append((k, y1))
        yrs = sorted(yr_rows[0][1])
        out.append("\n**Calendar-year returns (1x, net of costs):**\n")
        out.append("| Strategy | " + " | ".join(yrs) + " |")
        out.append("|---|" + "---|" * len(yrs))
        for k, y in yr_rows:
            out.append(f"| {k} | " + " | ".join(f"{y.get(x, 0):.1%}" for x in yrs) + " |")
        out.append("")
    out.append("**Reading it:** a day strategy only uses capital during the session, so compare its CAGR to what "
               "the same capital earns in the core (the buy & hold row, or QLD+200d at ~20-34%/yr in backtest_results.md). "
               "The 3x column is the same trades through a 3x ETF (TQQQ/SQQQ, UPRO/SPXU), intraday only.\n")
    out.append("## Data log\n")
    out.extend(f"- {x}" for x in (log[:40] or ["(clean)"]))
    (HERE / "intraday_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
