"""
Process backtest — does the live decision process beat SPY / QQQ, and would a
different one do better?  (Ryan, 2026-09-29: "test the actual process/methods we
are using to decide if there is a better strategy ... beating SPY and QQQ returns
is the benchmark.")

Runs on GitHub Actions (the only place with the FMP key). Pure standard library.

PART A — equity swing process. Daily replay, 2019 -> today, over the live scan
universe (analyze.UNIVERSE + the joint watch-list), graded every session with the
LIVE grade.py (same traits, same top-10% / 9-of-12 / RS-3M bar, same top-25% hold
bar) and the LIVE RSI (analyze.compute_rsi). Each strategy below is one process;
they differ only in entry, exits and capital structure, so the comparison
isolates the method.

PART B — day track. QQQ 5-minute opening-range breakout from 1-minute bars: the
Zarattini & Aziz paper rules vs. the rules in docs/day-track-spec.md, in R per
trade gross and net of a 1-cent spread per side.

Honest limits, printed in the output too:
  * SURVIVORSHIP: the universe is TODAY's list, so it contains the names that
    survived and grew. Absolute returns are flattered for EVERY strategy; the
    comparison between strategies on the same universe is the useful output.
  * No earnings calendar history, so the [ERN] no-entry bar is not modelled.
  * Fills at the signal session's close +/- 5 bp (a lag-1 variant fills at the
    next close). No commissions (Robinhood).
  * FMP daily data may be split-unadjusted on this tier; the loader repairs
    clean split ratios and prints every repair.
  * Options cannot be tested: no historical options data on this FMP tier.

Usage:
  python backtest.py                 # fetch from FMP (needs FMP_API_KEY), run all
  python backtest.py --synthetic     # offline logic check on random-walk data
  python backtest.py --skip-daytrack
"""

from __future__ import annotations

import argparse
import gzip
import json
import math
import os
import random
import statistics
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import grade as quality
from analyze import UNIVERSE, compute_rsi

HERE = Path(__file__).resolve().parent
BASE = "https://financialmodelingprep.com/stable"
FETCH_FROM = "2017-06-01"
TRADE_FROM = "2019-01-02"
COST_BP = 5            # slippage/spread per side, basis points
GRADE_WINDOW = 400     # rows handed to grade.score_one (it needs >= 260)
RSI_WINDOW = 60


# ----------------------------------------------------------------------------- data

def _get(url: str):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3 + attempt * 3)
                continue
            return {"_http_error": e.code}
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                return {"_error": str(e)}
            time.sleep(2)
    return None


SPLIT_RATIOS = [2, 3, 4, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50]


def repair_splits(sym: str, rows: list[dict], log: list[str]) -> list[dict]:
    """rows chronological. Detect a one-day jump that matches a clean split ratio and
    rescale everything before it. Prints each repair so it can be checked."""
    for i in range(1, len(rows)):
        a, b = rows[i - 1]["price"], rows[i]["price"]
        if not a or not b:
            continue
        for ratio, kind in ((a / b, "split"), (b / a, "reverse")):
            for k in SPLIT_RATIOS:
                if abs(ratio / k - 1) < 0.06:
                    f = (1 / k) if kind == "split" else k
                    for r in rows[:i]:
                        r["price"] *= f
                        r["volume"] = r["volume"] / f if f else r["volume"]
                    log.append(f"{sym} {rows[i]['date']}: {kind} 1:{k} repaired")
                    break
            else:
                continue
            break
    return rows


def fetch_daily(sym: str, key: str, log: list[str]) -> tuple[list[dict] | None, str]:
    to_d = date.today().isoformat()
    for ep, pfield in (("historical-price-eod/dividend-adjusted", "adjClose"),
                       ("historical-price-eod/full", "close"),
                       ("historical-price-eod/light", "price")):
        data = _get(f"{BASE}/{ep}?symbol={sym}&from={FETCH_FROM}&to={to_d}&apikey={key}")
        if isinstance(data, list) and data:
            rows = []
            for r in data:
                p = r.get(pfield) or r.get("close") or r.get("price") or r.get("adjClose")
                if p:
                    rows.append({"date": r["date"][:10], "price": float(p),
                                 "volume": float(r.get("volume") or 0)})
            rows.sort(key=lambda r: r["date"])
            if pfield != "adjClose":
                rows = repair_splits(sym, rows, log)
            return rows, ep
    return None, "none"


def synthetic_daily(symbols: list[str]) -> dict[str, list[dict]]:
    rnd = random.Random(7)
    d0 = date(2017, 6, 1)
    days = []
    d = d0
    while d < date.today():
        if d.weekday() < 5:
            days.append(d.isoformat())
        d += timedelta(days=1)
    out = {}
    for s in symbols:
        drift = rnd.uniform(-0.0002, 0.0012)
        vol = rnd.uniform(0.01, 0.03)
        p, rows = 50.0, []
        for dd in days:
            p *= math.exp(drift + vol * rnd.gauss(0, 1))
            rows.append({"date": dd, "price": p, "volume": rnd.uniform(1e5, 1e6)})
        out[s] = rows
    return out


# ----------------------------------------------------------------------------- engine

class Pos:
    __slots__ = ("sym", "shares", "entry", "entry_i", "high")

    def __init__(self, sym, shares, entry, entry_i):
        self.sym, self.shares, self.entry, self.entry_i, self.high = sym, shares, entry, entry_i, entry


def run_strategy(cfg: dict, dates: list[str], px: dict[str, list[float | None]],
                 grades: list[dict], rsi2: dict[str, list[float | None]],
                 sma50: dict[str, list[float | None]]) -> dict:
    """Replay one process. px[sym][i] = close on dates[i] (None if not trading)."""
    cost = cfg.get("cost_bp", COST_BP) / 1e4
    lag = cfg.get("lag", 0)
    slots = cfg.get("slots", 4)
    reserve = cfg.get("reserve", 0.02)
    core = cfg.get("core")                      # None or "QQQ"
    cash, core_sh = 100_000.0, 0.0
    pos: dict[str, Pos] = {}
    trades, curve, exposure = [], [], []
    pending: list[tuple] = []                   # (kind, sym, reason) to fill at next close (lag=1)
    start = next(i for i, d in enumerate(dates) if d >= TRADE_FROM)

    def price(sym, i):
        return px[sym][i]

    def equity(i):
        e = cash + sum(p.shares * (price(p.sym, i) or p.entry) for p in pos.values())
        if core_sh:
            e += core_sh * price(core, i)
        return e

    def sell(sym, i, reason):
        nonlocal cash
        p = pos.pop(sym)
        fill = price(sym, i) or p.entry
        fill *= (1 - cost)
        cash += p.shares * fill
        trades.append({"sym": sym, "ret": fill / p.entry - 1, "days": i - p.entry_i, "reason": reason,
                       "pnl": p.shares * (fill - p.entry), "date": dates[i]})

    def core_sell(i, amount):
        nonlocal cash, core_sh
        if not core or amount <= 0 or core_sh <= 0:
            return
        q = price(core, i)
        n = min(core_sh, amount / (q * (1 - cost)))
        core_sh -= n
        cash += n * q * (1 - cost)

    def buy(sym, i, dollars):
        nonlocal cash
        q = price(sym, i)
        if not q:
            return
        if cash < dollars:
            core_sell(i, dollars - cash + 1)
        dollars = min(dollars, cash)
        if dollars <= 0:
            return
        fill = q * (1 + cost)
        pos[sym] = Pos(sym, dollars / fill, fill, i)
        cash -= dollars

    last_month = None
    for i in range(start, len(dates)):
        g = grades[i]
        # 0. execute yesterday's decisions (lag=1)
        if lag and pending:
            for kind, sym, reason in pending:
                if kind == "sell" and sym in pos and price(sym, i):
                    sell(sym, i, reason)
            eq = equity(i)
            for kind, sym, reason in pending:
                if kind == "buy" and sym not in pos and len(pos) < slots and price(sym, i):
                    target = eq * (1 - reserve) / slots
                    if cash + (core_sh * price(core, i) if core else 0) >= 0.9 * target:
                        buy(sym, i, target)
            pending = []

        for p in pos.values():
            q = price(p.sym, i)
            if q:
                p.high = max(p.high, q)

        # 1. exits
        exits = []
        for sym, p in list(pos.items()):
            q = price(sym, i)
            if not q:
                continue
            gs = g.get(sym)
            r2 = rsi2[sym][i]
            reason = None
            if cfg.get("rsi2_tp") and r2 is not None and r2 >= 70 and q > p.entry:
                reason = "rsi2_tp"
            elif cfg.get("grade_exit") and (gs is None or gs["pct"] > quality.HOLD_PCT):
                if not cfg.get("monthly") or dates[i][:7] != last_month:
                    reason = "grade_exit"
            if not reason and cfg.get("trail") and q <= p.high * (1 - cfg["trail"]):
                reason = "trail"
            if not reason and cfg.get("loss_cut"):
                s50 = sma50[sym][i]
                if q <= p.entry * (1 - cfg["loss_cut"]) or (s50 and q < s50 and q < p.entry):
                    reason = "loss_cut"
            if not reason and cfg.get("time_stop") and i - p.entry_i >= cfg["time_stop"]:
                reason = "time_stop"
            if reason:
                exits.append((sym, reason))
        for sym, reason in exits:
            if lag:
                pending.append(("sell", sym, reason))
            else:
                sell(sym, i, reason)

        # 2. entries
        month = dates[i][:7]
        rebalance_day = month != last_month
        free = slots - len(pos) + (len(exits) if lag else 0)
        if free > 0 and (not cfg.get("monthly") or rebalance_day):
            cands = []
            for sym, gs in g.items():
                if sym in pos or sym in ("SPY", "QQQ") or not gs.get("eligible"):
                    continue
                q = price(sym, i)
                if not q:
                    continue
                if cfg["entry"] == "pullback":
                    if quality.pullback_trigger(gs, q, rsi2[sym][i]) is None:
                        continue
                cands.append((gs["rank"], sym))
            if cfg["entry"] == "connors":           # the pre-grade screen, for reference
                cands = []
                for sym in px:
                    if sym in pos or sym in ("SPY", "QQQ"):
                        continue
                    gs, q, r2 = g.get(sym), price(sym, i), rsi2[sym][i]
                    if gs and q and r2 is not None and r2 < 10 and gs["traits"]["ma200_up"]:
                        cands.append((r2, sym))
            cands.sort()
            eq = equity(i)
            target = eq * (1 - reserve) / slots
            for _, sym in cands[: min(free, cfg.get("max_entries_day", 3))]:
                if lag:
                    pending.append(("buy", sym, "entry"))
                else:
                    avail = cash + (core_sh * price(core, i) * (1 - cost) if core else 0)
                    if avail >= 0.9 * target and len(pos) < slots:
                        buy(sym, i, target)
        last_month = month

        # 3. park idle cash in the core
        if core and price(core, i):
            eq = equity(i)
            spare = cash - reserve * eq
            if spare > 0.01 * eq:
                q = price(core, i) * (1 + cost)
                core_sh += spare / q
                cash -= spare

        eq = equity(i)
        curve.append(eq)
        exposure.append(1 - cash / eq if eq else 0)

    return {"curve": curve, "trades": trades, "exposure": statistics.mean(exposure)}


# ----------------------------------------------------------------------------- stats

def stats(curve: list[float], dates: list[str]) -> dict:
    yrs = max((datetime.fromisoformat(dates[-1]) - datetime.fromisoformat(dates[0])).days / 365.25, 1e-9)
    total = curve[-1] / curve[0]
    rets = [curve[i] / curve[i - 1] - 1 for i in range(1, len(curve))]
    vol = statistics.pstdev(rets) * math.sqrt(252) if len(rets) > 2 else 0
    peak, mdd = curve[0], 0.0
    for v in curve:
        peak = max(peak, v)
        mdd = min(mdd, v / peak - 1)
    cagr = total ** (1 / yrs) - 1
    return {"cagr": cagr, "total": total - 1, "vol": vol, "mdd": mdd,
            "sharpe": (statistics.mean(rets) * 252 / vol) if vol else 0}


def yearly(curve, dates):
    out, first = {}, {}
    for v, d in zip(curve, dates):
        y = d[:4]
        first.setdefault(y, v)
        out[y] = v / first[y] - 1
    # chain from the prior year's close so each year is a true calendar return
    ys = sorted(out)
    last = {}
    for v, d in zip(curve, dates):
        last[d[:4]] = v
    res, prev = {}, curve[0]
    for y in ys:
        res[y] = last[y] / prev - 1
        prev = last[y]
    return res


def trade_stats(tr):
    if not tr:
        return {"n": 0}
    w = [t["ret"] for t in tr if t["ret"] > 0]
    l = [t["ret"] for t in tr if t["ret"] <= 0]
    aw = statistics.mean(w) if w else 0
    al = abs(statistics.mean(l)) if l else 0
    reasons = {}
    for t in tr:
        reasons[t["reason"]] = reasons.get(t["reason"], 0) + 1
    return {"n": len(tr), "win": len(w) / len(tr), "avg_win": aw, "avg_loss": al,
            "payoff": aw / al if al else float("inf"), "exp": statistics.mean(t["ret"] for t in tr),
            "hold": statistics.mean(t["days"] for t in tr), "reasons": reasons}


# ----------------------------------------------------------------------------- part A

STRATEGIES = [
    # name, description, config
    ("CURRENT", "Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve)",
     {"entry": "pullback", "rsi2_tp": True, "grade_exit": True, "reserve": 0.25}),
    ("CURRENT_2pct", "Same exits, only a 2% cash reserve (options bucket returned to stocks)",
     {"entry": "pullback", "rsi2_tp": True, "grade_exit": True, "reserve": 0.02}),
    ("CURRENT_QQQcore", "Same exits, idle cash parked in QQQ",
     {"entry": "pullback", "rsi2_tp": True, "grade_exit": True, "reserve": 0.02, "core": "QQQ"}),
    ("LEADER", "Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit",
     {"entry": "pullback", "grade_exit": True, "trail": 0.15, "loss_cut": 0.08, "reserve": 0.02}),
    ("LEADER_QQQcore", "LEADER with idle cash in QQQ",
     {"entry": "pullback", "grade_exit": True, "trail": 0.15, "loss_cut": 0.08, "reserve": 0.02, "core": "QQQ"}),
    ("LEADER_nocut", "Grade exit + 15% trail, no loss cut",
     {"entry": "pullback", "grade_exit": True, "trail": 0.15, "reserve": 0.02}),
    ("GRADE_HOLD", "Pullback entry; only exit = grade exit (hold while top 25%)",
     {"entry": "pullback", "grade_exit": True, "reserve": 0.02}),
    ("GRADE_HOLD_any", "No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit",
     {"entry": "grade", "grade_exit": True, "reserve": 0.02}),
    ("ROTATE_MONTHLY", "Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start",
     {"entry": "grade", "grade_exit": True, "monthly": True, "reserve": 0.02}),
    ("ROTATE_MONTHLY_QQQcore", "ROTATE_MONTHLY with idle cash in QQQ",
     {"entry": "grade", "grade_exit": True, "monthly": True, "reserve": 0.02, "core": "QQQ"}),
    ("ROTATE_MONTHLY_8", "ROTATE_MONTHLY with 8 slots",
     {"entry": "grade", "grade_exit": True, "monthly": True, "reserve": 0.02, "slots": 8}),
    ("OLD_CONNORS", "Pre-2026-09-25 screen for reference: RSI2<10 above a rising 200SMA; RSI2>=70 TP; 14-day time stop",
     {"entry": "connors", "rsi2_tp": True, "time_stop": 14, "reserve": 0.02}),
]



SP100_2018 = [  # S&P 100 constituents at end-2018 (tickers as they trade today where renamed).
    # Chosen BEFORE the test period, so it carries no hindsight about 2019-2026 winners.
    # Names acquired/delisted since (AGN, CELG, DWDP, UTX->RTX merger, WBA) drop out if FMP
    # lacks their history -- a small residual survivorship bias, stated in the output.
    "AAPL", "ABBV", "ABT", "ACN", "ADBE", "AIG", "ALL", "AMGN", "AMZN", "AXP", "BA", "BAC",
    "BIIB", "BK", "BKNG", "BLK", "BMY", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP",
    "COST", "CSCO", "CVS", "CVX", "DHR", "DIS", "DUK", "EMR", "EXC", "F", "FDX", "GD", "GE",
    "GILD", "GM", "GOOGL", "GS", "HD", "HON", "IBM", "INTC", "JNJ", "JPM", "KHC", "KMI", "KO",
    "LLY", "LMT", "LOW", "MA", "MCD", "MDLZ", "MDT", "MET", "MMM", "MO", "MRK", "MS", "MSFT",
    "NEE", "NFLX", "NKE", "NVDA", "ORCL", "OXY", "PEP", "PFE", "PG", "PM", "PYPL", "QCOM",
    "RTX", "SBUX", "SLB", "SO", "SPG", "T", "TGT", "TXN", "UNH", "UNP", "UPS", "USB", "V",
    "VZ", "WBA", "WFC", "WMT", "XOM", "META", "BRK-B", "GOOG",
]

NDX100_2018 = [  # Nasdaq-100 constituents at end-2018 (renamed tickers mapped). QQQ's own pool,
    # chosen before the test period -- the fairest "can the grade beat QQQ from inside QQQ" test.
    "AAL", "AAPL", "ADBE", "ADI", "ADP", "ADSK", "ALGN", "AMAT", "AMGN", "AMZN", "ASML", "AVGO",
    "BIDU", "BIIB", "BKNG", "BMRN", "CDNS", "CHKP", "CHTR", "CMCSA", "COST", "CSCO", "CSX",
    "CTAS", "TCOM", "CTSH", "DLTR", "EA", "EBAY", "EXPE", "FAST", "META", "FISV", "FOXA",
    "GILD", "GOOGL", "HAS", "HOLX", "HSIC", "IDXX", "ILMN", "INCY", "INTC", "INTU", "ISRG",
    "JBHT", "JD", "KHC", "KLAC", "LBTYA", "LRCX", "MAR", "MCHP", "MDLZ", "MELI", "MNST", "MSFT",
    "MU", "NFLX", "NTAP", "NTES", "NVDA", "NXPI", "ORLY", "PAYX", "PCAR", "PEP", "PYPL", "QCOM",
    "REGN", "ROST", "SBUX", "SIRI", "SNPS", "SWKS", "TMUS", "TSLA", "TTWO", "TXN", "UAL", "ULTA",
    "VRSK", "VRTX", "WBA", "WDAY", "WDC", "WYNN", "XEL",
]
EXTRA = ["QLD", "TQQQ", "BIL"]

CORE_SET = ["CURRENT", "CURRENT_2pct", "CURRENT_QQQcore", "LEADER", "LEADER_QQQcore", "GRADE_HOLD",
            "GRADE_HOLD_any", "ROTATE_MONTHLY", "ROTATE_MONTHLY_8", "ROTATE_MONTHLY_QQQcore"]
LAG_SET = ("CURRENT", "LEADER", "GRADE_HOLD", "GRADE_HOLD_any", "ROTATE_MONTHLY", "ROTATE_MONTHLY_QQQcore")


def build(hist, syms):
    dates = [r["date"] for r in hist["SPY"]]
    idx = {d: i for i, d in enumerate(dates)}
    px = {s: [None] * len(dates) for s in syms}
    vol = {s: [0.0] * len(dates) for s in syms}
    for s in syms:
        for r in hist[s]:
            i = idx.get(r["date"])
            if i is not None:
                px[s][i], vol[s][i] = r["price"], r["volume"]
    t0 = time.time()
    grades, rsi2, sma50 = [], {s: [None] * len(dates) for s in syms}, {s: [None] * len(dates) for s in syms}
    start = next(i for i, d in enumerate(dates) if d >= TRADE_FROM)
    for i in range(len(dates)):
        if i < start - 1:
            grades.append({})
            continue
        h = {}
        for s in syms:
            col = px[s]
            if col[i] is None:
                continue
            lo = max(0, i - GRADE_WINDOW + 1)
            rows = [{"price": col[j], "volume": vol[s][j]} for j in range(i, lo - 1, -1) if col[j]]
            if len(rows) >= 260:
                h[s] = rows
                closes = [col[j] for j in range(max(0, i - RSI_WINDOW + 1), i + 1) if col[j]]
                rsi2[s][i] = compute_rsi(closes, 2)
                sma50[s][i] = sum(r["price"] for r in rows[:50]) / 50
        grades.append(quality.grade_universe(h) if "SPY" in h else {})
        if i % 500 == 0:
            print(f"  graded {dates[i]} ({len(h)} names) {time.time() - t0:.0f}s", flush=True)
    return dates, px, grades, rsi2, sma50, start


def period_cagr(curve, tdates, a, b):
    ix = [k for k, d in enumerate(tdates) if a <= d <= b]
    if len(ix) < 20:
        return None
    return stats([curve[k] for k in ix], [tdates[k] for k in ix])["cagr"]


def contributors(trades, n=5):
    by = {}
    for t in trades:
        by[t["sym"]] = by.get(t["sym"], 0) + t["pnl"]
    total = sum(by.values())
    top = sorted(by.items(), key=lambda kv: -kv[1])[:n]
    share = sum(v for _, v in top) / total if total > 0 else float("nan")
    return top, share, len(by)


def part_a(hist, out, label, syms, names, detail):
    t0 = time.time()
    dates, px, grades, rsi2, sma50, start = build(hist, syms)
    tdates = dates[start:]
    split = "2022-12-31"
    bench = {}
    for b in ("SPY", "QQQ"):
        c = [px[b][i] for i in range(start, len(dates))]
        bench[b] = (stats(c, tdates), yearly(c, tdates), period_cagr(c, tdates, tdates[0], split),
                    period_cagr(c, tdates, "2023-01-01", tdates[-1]))
    results = []
    for name, desc, cfg in STRATEGIES:
        if name not in names:
            continue
        variants = [(name, dict(cfg))]
        if name in LAG_SET:
            variants.append((name + "_lag1", dict(cfg, lag=1)))
        if name in ("GRADE_HOLD_any", "ROTATE_MONTHLY") and detail:
            variants.append((name + "_cost25bp", dict(cfg, cost_bp=25)))
        for vname, c2 in variants:
            r = run_strategy(c2, dates, px, grades, rsi2, sma50)
            s = stats(r["curve"], tdates)
            results.append({"name": vname, "desc": desc, "s": s, "yr": yearly(r["curve"], tdates),
                            "t": trade_stats(r["trades"]), "ex": r["exposure"],
                            "p1": period_cagr(r["curve"], tdates, tdates[0], split),
                            "p2": period_cagr(r["curve"], tdates, "2023-01-01", tdates[-1]),
                            "top": contributors(r["trades"])})
            print(f"  [{label}] {vname}: CAGR {s['cagr']:.1%} mdd {s['mdd']:.1%}", flush=True)

    f = lambda x: "n/a" if x is None else f"{x:.1%}"
    out.append(f"## Part A — {label}: {len(syms) - 2} names, {tdates[0]} → {tdates[-1]}\n")
    out.append("| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for b in ("SPY", "QQQ"):
        s = bench[b][0]
        out.append(f"| **{b} buy & hold** | {s['cagr']:.1%} | | | {f(bench[b][2])} | {f(bench[b][3])} | {s['mdd']:.1%} | {s['sharpe']:.2f} | 100% | | | | | |")
    for r in sorted(results, key=lambda r: -r["s"]["cagr"]):
        s, t = r["s"], r["t"]
        out.append(f"| {r['name']} | {s['cagr']:.1%} | {s['cagr'] - bench['SPY'][0]['cagr']:+.1%} | "
                   f"{s['cagr'] - bench['QQQ'][0]['cagr']:+.1%} | {f(r['p1'])} | {f(r['p2'])} | {s['mdd']:.1%} | "
                   f"{s['sharpe']:.2f} | {r['ex']:.0%} | {t.get('n', 0)} | {t.get('win', 0):.0%} | "
                   f"{t.get('payoff', 0):.2f} | {t.get('hold', 0):.0f} | {r['top'][1]:.0%} of {r['top'][2]} names |")
    out.append("\n**Biggest contributors (realized P&L by name, per $100k start):**\n")
    for r in results:
        if r["name"].endswith(("_lag1", "_cost25bp")):
            continue
        out.append(f"- {r['name']}: " + ", ".join(f"{k} ${v:,.0f}" for k, v in r["top"][0]))
    if detail:
        yrs = sorted(bench["SPY"][1])
        out.append("\n**Calendar-year returns:**\n")
        out.append("| Strategy | " + " | ".join(yrs) + " |")
        out.append("|---|" + "---|" * len(yrs))
        for b in ("SPY", "QQQ"):
            out.append(f"| **{b}** | " + " | ".join(f"{bench[b][1].get(y, 0):.1%}" for y in yrs) + " |")
        for r in results:
            out.append(f"| {r['name']} | " + " | ".join(f"{r['yr'].get(y, 0):.1%}" for y in yrs) + " |")
        out.append("\n**Definitions and exit mix:**\n")
        for r in results:
            out.append(f"- **{r['name']}** — {r['desc']}. Exits: {r['t'].get('reasons', {})}")
    out.append(f"\n_{label} compute: {time.time() - t0:.0f}s._\n")



# ----------------------------------------------------------------------------- part C

def part_c(hist, out):
    """Index-based ways to beat QQQ, from real ETF closes (fees and leverage decay included).
    Trend filter: hold the fund while QQQ closes above its 200-day SMA, else BIL (T-bills);
    the switch fills at the NEXT close (no look-ahead)."""
    need = ["QQQ", "QLD", "TQQQ", "BIL", "SPY"]
    if any(n not in hist for n in need):
        out.append("## Part C — skipped (missing " + ", ".join(n for n in need if n not in hist) + ")\n")
        return
    maps = {n: {r["date"]: r["price"] for r in hist[n]} for n in need}
    dates = [d for d in (r["date"] for r in hist["QQQ"]) if all(d in maps[n] for n in need)]
    q = [maps["QQQ"][d] for d in dates]
    start = next(i for i, d in enumerate(dates) if d >= TRADE_FROM)
    sig = [None] * len(dates)
    for i in range(200, len(dates)):
        sig[i] = q[i] > sum(q[i - 199:i + 1]) / 200
    tdates = dates[start:]
    rows = []
    for fund in ("QQQ", "QLD", "TQQQ"):
        f = [maps[fund][d] for d in dates]
        b = [maps["BIL"][d] for d in dates]
        bh = [f[i] / f[start] for i in range(start, len(dates))]
        eq, cur, curve, switches, inv = 1.0, "fund", [], 0, 0
        for i in range(start, len(dates)):
            if i > start:
                r = f[i] / f[i - 1] if cur == "fund" else b[i] / b[i - 1]
                eq *= r
            want = "fund" if sig[i] else "bil"
            if want != cur:
                eq *= 1 - COST_BP / 1e4
                cur, switches = want, switches + 1
            inv += cur == "fund"
            curve.append(eq)
        rows.append((f"{fund} buy & hold", stats(bh, tdates), yearly(bh, tdates), 1.0, 0))
        rows.append((f"{fund} + 200d trend filter", stats(curve, tdates), yearly(curve, tdates),
                     inv / len(curve), switches))
    out.append(f"## Part C — index-based alternatives, {tdates[0]} → {tdates[-1]}\n")
    out.append("Real ETF closes (expense ratios and daily-reset decay included). Trend filter: in the fund while "
               "QQQ > its 200-day SMA, else T-bills (BIL); switches fill at the next close.\n")
    out.append("| Strategy | CAGR | Max DD | Sharpe | Vol | Time invested | Switches |")
    out.append("|---|---|---|---|---|---|---|")
    for n, s_, _, inv, sw in rows:
        out.append(f"| {n} | {s_['cagr']:.1%} | {s_['mdd']:.1%} | {s_['sharpe']:.2f} | {s_['vol']:.0%} | {inv:.0%} | {sw} |")
    yrs = sorted(rows[0][2])
    out.append("\n| Strategy | " + " | ".join(yrs) + " |")
    out.append("|---|" + "---|" * len(yrs))
    for n, _, yr, _, _ in rows:
        out.append(f"| {n} | " + " | ".join(f"{yr.get(y, 0):.1%}" for y in yrs) + " |")
    out.append("")


# ----------------------------------------------------------------------------- part D

def part_d(key, hist, out, log):
    """Long-history stress test for leverage: simulate 1x/2x/3x daily-reset QQQ from 1999, so
    the 2000-02 (-83%) and 2008 crashes are included. Daily r_L = L*r - fee - (L-1)*financing.
    Validated against the real QLD/TQQQ over their live overlap."""
    data = None
    if key:
        data = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol=QQQ&from=1999-03-10&to={date.today()}&apikey={key}")
    if not isinstance(data, list) or not data:
        out.append(f"## Part D — skipped (no long QQQ history: {str(data)[:120]})\n")
        return
    rows = sorted(({"date": r["date"][:10], "p": float(r.get("adjClose") or r["close"])} for r in data),
                  key=lambda r: r["date"])
    dates, q = [r["date"] for r in rows], [r["p"] for r in rows]
    FEE, FIN = {1: 0.0020, 2: 0.0095, 3: 0.0086}, 0.025
    def sim(L, filt):
        eq, cur, curve = 1.0, True, []
        for i in range(len(q)):
            if i:
                if cur:
                    r = q[i] / q[i - 1] - 1
                    eq *= 1 + L * r - FEE[L] / 252 - (L - 1) * FIN / 252
                else:
                    eq *= 1 + FIN / 252
            if filt and i >= 200:
                want = q[i] > sum(q[i - 199:i + 1]) / 200
                if want != cur:
                    eq *= 1 - COST_BP / 1e4
                    cur = want
            curve.append(eq)
        return curve
    first = next(i for i in range(len(dates)) if i >= 200)
    periods = [("1999-2026 (all)", dates[first], dates[-1]), ("2000-2002 crash", "2000-03-01", "2002-12-31"),
               ("2007-2009 crisis", "2007-10-01", "2009-06-30"), ("2010-2018", "2010-01-01", "2018-12-31"),
               ("2019-2026", "2019-01-01", dates[-1])]
    out.append(f"## Part D — leverage stress test: simulated daily-reset QQQ, {dates[first]} → {dates[-1]}\n")
    out.append(f"(Earliest QQQ row FMP returned: {dates[0]}; periods before {dates[first]} show 'no data'.)\n")
    out.append(f"Fees 0.20%/0.95%/0.86% a year for 1x/2x/3x; financing {FIN:.1%} a year on the borrowed part; "
               "trend filter = hold while QQQ > 200-day SMA, else T-bills at the same rate. CAGR per period, max drawdown in brackets.\n")
    out.append("| Strategy | " + " | ".join(p[0] for p in periods) + " |")
    out.append("|---|" + "---|" * len(periods))
    for L in (1, 2, 3):
        for filt in (False, True):
            c = sim(L, filt)
            cells = []
            for _, a, b in periods:
                ix = [k for k in range(first, len(dates)) if a <= dates[k] <= b]
                if len(ix) < 20:
                    cells.append("no data")
                    continue
                st = stats([c[k] for k in ix], [dates[k] for k in ix])
                cells.append(f"{st['cagr']:.1%} ({st['mdd']:.0%})")
            out.append(f"| {L}x QQQ{' + 200d filter' if filt else ''} | " + " | ".join(cells) + " |")
    # validation against real funds
    for fund, L in (("QLD", 2), ("TQQQ", 3)):
        if fund in hist:
            real = {r["date"]: r["price"] for r in hist[fund]}
            c = sim(L, False)
            ix = [k for k in range(len(dates)) if dates[k] >= "2019-01-02" and dates[k] in real]
            if len(ix) > 20:
                sim_c = stats([c[k] for k in ix], [dates[k] for k in ix])["cagr"]
                real_c = stats([real[dates[k]] for k in ix], [dates[k] for k in ix])["cagr"]
                out.append(f"\nValidation 2019→: simulated {L}x CAGR {sim_c:.1%} vs real {fund} {real_c:.1%}.")
    out.append("")


# ----------------------------------------------------------------------------- part B

def fetch_minutes(key: str, log: list[str], interval: str = "1min") -> dict[str, list[dict]]:
    """QQQ intraday bars by ET session date. FMP returns local exchange time."""
    days: dict[str, list[dict]] = {}
    end = date.today()
    d = end - timedelta(days=730)
    while d < end:
        e = min(d + timedelta(days=4), end)
        data = _get(f"{BASE}/historical-chart/{interval}?symbol=QQQ&from={d}&to={e}&apikey={key}")
        if not isinstance(data, list):
            log.append(f"{interval} fetch {d}..{e} failed: {data}")
            if not days:
                return {}
        else:
            for r in data:
                ts = r["date"]
                days.setdefault(ts[:10], []).append(
                    {"t": ts[11:16], "o": r["open"], "h": r["high"], "l": r["low"], "c": r["close"]})
        d = e + timedelta(days=1)
        time.sleep(0.25)
    for k in days:
        days[k].sort(key=lambda b: b["t"])
    return days


def orb_day(bars: list[dict], rules: str, atr_d: float | None, step: int = 1) -> float | None:
    """One session. Returns R multiple, or None (no trade). step = bar size in minutes."""
    rth = [b for b in bars if "09:30" <= b["t"] <= "15:59"]
    orb = [b for b in rth if b["t"] < "09:35"]
    rest = [b for b in rth if b["t"] >= "09:35"]
    if len(orb) < 5 // step or len(rest) < 30 // step:
        return None
    hi, lo = max(b["h"] for b in orb), min(b["l"] for b in orb)
    op, cl = orb[0]["o"], orb[-1]["c"]
    rng = hi - lo
    if rng <= 0 or cl == op:
        return None
    long = cl > op
    entry = rest[0]["o"]
    if rules == "ours":
        if abs(cl - op) < 0.10 * rng:
            return None
        edge = hi if long else lo
        if (entry - edge if long else edge - entry) > 0.5 * rng:
            return None
    stop = lo if long else hi
    if atr_d and rules == "ours":
        min_d = 0.1 * atr_d
        if abs(entry - stop) < min_d:
            stop = entry - min_d if long else entry + min_d
    risk = abs(entry - stop)
    if risk <= 0:
        return None
    sgn = 1 if long else -1
    target = entry + sgn * 10 * risk
    best = entry
    five = []
    for b in rest:
        five.append(b)
        # stop / target first (conservative: stop wins a tie)
        if (b["l"] <= stop) if long else (b["h"] >= stop):
            return sgn * (stop - entry) / risk
        if rules == "paper" and ((b["h"] >= target) if long else (b["l"] <= target)):
            return 10.0
        best = max(best, b["h"]) if long else min(best, b["l"])
        r_now = sgn * (b["c"] - entry) / risk
        if rules == "ours":
            if r_now >= 1 and ((stop < entry) if long else (stop > entry)):
                stop = entry
            if r_now >= 2:
                k = 5 // step
                agg = [five[j:j + k] for j in range(0, len(five), k)]
                trs = [max(x["h"] for x in a) - min(x["l"] for x in a) for a in agg[-14:] if a]
                atr5 = statistics.mean(trs) if trs else risk
                new = best - sgn * 1.5 * atr5
                stop = max(stop, new) if long else min(stop, new)
            if b["t"] >= "12:00" and abs(r_now) < 0.5:
                return r_now
            if b["t"] >= "15:30":
                return r_now
    return sgn * (rest[-1]["c"] - entry) / risk


def part_b(key: str | None, daily_qqq: list[dict], out: list[str], log: list[str]) -> None:
    out.append("## Part B — day track (QQQ 5-min opening-range breakout)\n")
    if not key:
        out.append("_Skipped: no API key (synthetic run)._\n")
        return
    step, days = 1, fetch_minutes(key, log)
    if not days:
        step, days = 5, fetch_minutes(key, log, "5min")
    if not days:
        out.append("_1-minute QQQ history is not available on this FMP tier — Part B could not run. "
                   "See the fetch log below._\n")
        return
    closes = {r["date"]: r["price"] for r in daily_qqq}
    dl = sorted(closes)
    res = {"paper": [], "ours": []}
    risk_pts = []
    for d in sorted(days):
        prior = [closes[x] for x in dl if x < d][-15:]
        atr_d = statistics.mean(abs(prior[j] - prior[j - 1]) for j in range(1, len(prior))) if len(prior) > 2 else None
        for rules in res:
            r = orb_day(days[d], rules, atr_d, step)
            if r is not None:
                res[rules].append((d, r))
        rth = [b for b in days[d] if "09:30" <= b["t"] < "09:35"]
        if len(rth) == 5 // step:
            risk_pts.append(max(b["h"] for b in rth) - min(b["l"] for b in rth))
    spread_R = (0.02 / statistics.mean(risk_pts)) if risk_pts else 0
    out.append(f"Bar size: {step}-minute (1-minute is paywalled on this FMP tier; the paper itself uses the first 5-minute bar). "
               f"Sessions: {len(days)} ({min(days)} → {max(days)}). "
               f"Cost model: 1¢ per side = {spread_R:.3f}R per round trip at the average OR range "
               f"({statistics.mean(risk_pts):.2f} pts).\n")
    out.append("| Rules | Trades | Win % | Gross R/trade | Net R/trade | Total net R | Net R excl. best trade | Best trade R |")
    out.append("|---|---|---|---|---|---|---|---|")
    for rules, rs in res.items():
        if not rs:
            continue
        r = [x for _, x in rs]
        net = [x - spread_R for x in r]
        best = max(net)
        out.append(f"| {rules} | {len(r)} | {sum(1 for x in r if x > 0) / len(r):.0%} | {statistics.mean(r):+.3f} | "
                   f"{statistics.mean(net):+.3f} | {sum(net):+.1f} | {sum(net) - best:+.1f} | {best:+.1f} |")
    out.append("\n`paper` = Zarattini & Aziz: stop at the opposite OR extreme, 10R target, else exit at the close. "
               "`ours` = docs/day-track-spec.md: body filter, late-entry gate, breakeven at +1R, 1.5×ATR(5-min) "
               "trail from +2R, 12:00 chop exit, 15:30 flat.\n")
    out.append("Dollar scale at this account: a cash-bound QQQ position of ~$2,500 on a typical OR range "
               f"risks about ${2500 / 740 * statistics.mean(risk_pts):.2f} per R.\n")


# ----------------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--synthetic", action="store_true")
    ap.add_argument("--skip-daytrack", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    joint = []
    jp = HERE / "watchlist_joint.json"
    if jp.exists():
        joint = json.loads(jp.read_text()).get("symbols", [])
    scan = list(dict.fromkeys(UNIVERSE + joint + ["SPY", "QQQ"]))
    if a.limit:
        scan = scan[: a.limit] + ["SPY", "QQQ"]
    syms = list(dict.fromkeys(scan + ([] if a.limit else SP100_2018 + NDX100_2018 + EXTRA)))
    log: list[str] = []
    key = None
    if a.synthetic:
        hist = synthetic_daily(syms)
        src = {"synthetic": len(hist)}
    else:
        key = os.environ.get("FMP_API_KEY", "").strip()
        if not key:
            sys.exit("FMP_API_KEY not set")
        hist, src = {}, {}
        for n, s in enumerate(syms):
            rows, ep = fetch_daily(s, key, log)
            src[ep] = src.get(ep, 0) + 1
            if rows:
                hist[s] = rows
            if n % 25 == 0:
                print(f"fetched {n}/{len(syms)}", flush=True)
            time.sleep(0.2)
        if "SPY" not in hist or "QQQ" not in hist:
            sys.exit("no SPY/QQQ history")
        with gzip.open(HERE / "backtest_data.json.gz", "wt") as f:
            json.dump(hist, f)

    out = [f"# Process backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Data sources (daily): {src}. Names with history: {len(hist)}.\n"]
    from analyze import SPECULATIVE
    everything = [s for s in scan if hist.get(s)]
    part_a(hist, out, "A1 FULL scan universe (today's list: survivorship-biased)",
           everything, [n for n, _, _ in STRATEGIES], True)
    ex_spec = [s for s in everything if s not in SPECULATIVE]
    part_a(hist, out, "A2 scan universe minus the 41 SPECULATIVE names", ex_spec, CORE_SET, False)
    sp = [s for s in SP100_2018 if s in hist] + ["SPY", "QQQ"]
    part_a(hist, out, "A3 S&P 100 as of end-2018 (no hindsight in the universe)", sp, CORE_SET, True)
    nd = [s for s in NDX100_2018 if s in hist] + ["SPY", "QQQ"]
    part_a(hist, out, "A4 Nasdaq-100 as of end-2018 (QQQ's own pool, no hindsight)", nd, CORE_SET, True)
    part_c(hist, out)
    part_d(key, hist, out, log)
    if not a.skip_daytrack:
        part_b(key, hist.get("QQQ", []), out, log)
    out.append("## Data log\n")
    out.extend(f"- {x}" for x in (log or ["(no split repairs or fetch errors)"]))
    name = "backtest_results_synthetic.md" if a.synthetic else "backtest_results.md"
    (HERE / name).write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
