"""
Exit backtest — can a multi-variable SELL formula, checked on every run through the day,
beat the swing sleeves' close-only exits?  (Ryan, live turn 2026-10-05: "we should have a
formula that identifies the sell that can be taken at runs through out the day ... a rule
like sell at x% is too simple ... maybe more than one depending on if its a sell for profit
or sell to limit losses".)

Runs on GitHub Actions (FMP key). Pure standard library. Read-only research.

THE TWO FORMULAS (each indicator is one point; sell when the points reach K):

PROFIT EXIT ("exhaustion score") - only while the position is GREEN (price > entry):
  P1 daily RSI(2)  >= 90               (short-term overbought)
  P2 daily RSI(14) >= 70               (medium-term overbought)
  P3 price >= upper Bollinger band (20-day, 2 sd)
  P4 today's move >= 1.0 x ATR(14)     (an unusually big up day)
  P5 gain since entry >= 1.5 x ATR(14) (the trade has paid well for its volatility)
  P6 weekly RSI(14)  >= 70             (overextended on the week)
  P7 monthly RSI(14) >= 70             (overextended on the month)
  Sell when points >= K_P.

LOSS EXIT ("damage score") - only while the position is RED (price < entry):
  L1 loss since entry >= 2.0 x ATR(14)
  L2 price below the 200-day SMA       (the setup's own precondition is gone)
  L3 price below the lowest low of the prior 20 sessions (a breakdown)
  L4 today's drop >= 1.5 x ATR(14)     (a shock day)
  L5 the market (QQQ) closed below its 200-day SMA yesterday
  L6 held >= 5 sessions without recovering
  Sell when points >= K_L.

Every indicator uses the live price as "today's" value, so each point turns on at a price
level computable before the open; the score therefore reduces to ONE trigger price per day,
which a run can compare against the live quote. That is also how the test runs on daily bars:
  * daily-bar proxy: the exit fires if the day's high (profit) / low (loss) reaches the
    trigger; fill at the trigger, or at the open if it gapped through; loss fills take a
    further 0.10% slip; profit fills 0.05%. If both trigger the same day, the loss is assumed
    first (pessimistic).
  * TRUE INTRADAY (SWING_Q only, 5-minute QQQ bars from 2018): the run is checked at 09:35,
    10:00, 10:30 ... 15:00 ET at that moment's price, and the close decision is taken at 15:50
    as live. This validates the daily-bar proxy.
After an intraday exit the symbol needs a FRESH entry signal: legs reset, no same-day
re-entry, and the turn-of-month leg stays off until the next turn-of-month window.

Variants: base, profit-only K_P=2..5, loss-only K_L=2..4, and every combination.
Honest check: the variant is CHOSEN on 2019-2022 only and SCORED on 2023-2026.

Limits: one historical path; daily-bar proxy for single names; the SWING_M pick pool is the
2018 S&P 100 + Nasdaq-100 (as in every earlier sleeve test); taxes ignored.
"""

from __future__ import annotations

import math
import os
import statistics
import sys
import time
from datetime import date, datetime
from pathlib import Path

from analyze import compute_rsi
from backtest import NDX100_2018, SP100_2018
from combo_backtest import curve_stats
from robust_backtest import FEE, combine, swing

HERE = Path(__file__).resolve().parent
START = "2015-01-01"
CHECKS = ["09:35", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
          "14:00", "14:30", "15:00"]
PROFIT_SLIP, LOSS_SLIP = 0.0005, 0.0010
INF = float("inf")


# ----------------------------------------------------------------------------- indicators

def solve_up(cond, lo, hi, it=24):
    """Smallest price p in [lo, hi] with cond(p) true, cond monotone non-decreasing in p.
    Returns lo if already true at lo, INF if never true."""
    if cond(lo):
        return lo
    if not cond(hi):
        return INF
    for _ in range(it):
        mid = (lo + hi) / 2
        if cond(mid):
            hi = mid
        else:
            lo = mid
    return hi


def period_closes(dates, C, key):
    """For each day i: (closes of COMPLETED periods before day i's period, last 40)."""
    out, done, cur, last = [], [], None, None
    for i, d in enumerate(dates):
        k = key(d)
        if k != cur:
            if last is not None:
                done.append(last)
            cur = k
        out.append(done[-40:])
        last = C[i]
    return out


def week_key(d):
    y, w, _ = date.fromisoformat(d).isocalendar()
    return (y, w)


class Series:
    """One symbol's adjusted OHLC with cached per-day indicator thresholds."""

    def __init__(self, dates, O, H, L, C):
        self.dates, self.O, self.H, self.L, self.C = dates, O, H, L, C
        n = len(dates)
        self.atr = [None] * n
        for i in range(15, n):
            trs = [max(H[j] - L[j], abs(H[j] - C[j - 1]), abs(L[j] - C[j - 1])) for j in range(i - 14, i)]
            self.atr[i] = sum(trs) / 14
        self.wk = period_closes(dates, C, week_key)
        self.mo = period_closes(dates, C, lambda d: d[:7])
        self._p, self._l = {}, {}
        self.ix = {d: i for i, d in enumerate(dates)}

    def profit_fixed(self, i):
        """Entry-independent profit thresholds for day i (price at/above which each point is on)."""
        if i in self._p:
            return self._p[i]
        C, pc = self.C, self.C[i - 1]
        lo, hi = pc * 0.6, pc * 1.6
        c30, c60, c20 = C[i - 30:i], C[i - 60:i], C[i - 19:i]

        def bb(p):
            xs = c20 + [p]
            m = sum(xs) / 20
            return p >= m + 2 * statistics.pstdev(xs)

        th = [solve_up(lambda p: (compute_rsi(c30 + [p], 2) or 0) >= 90, lo, hi),
              solve_up(lambda p: (compute_rsi(c60 + [p], 14) or 0) >= 70, lo, hi),
              solve_up(bb, lo, hi),
              pc + 1.0 * self.atr[i]]
        for hist in (self.wk[i], self.mo[i]):
            th.append(solve_up(lambda p: (compute_rsi(hist + [p], 14) or 0) >= 70, lo, hi)
                      if len(hist) >= 15 else INF)
        self._p[i] = th
        return th

    def loss_fixed(self, i):
        """Entry-independent loss thresholds (price at/below which each point is on)."""
        if i in self._l:
            return self._l[i]
        C = self.C
        th = [sum(C[i - 199:i]) / 199 * (1 - 1e-9),        # p < SMA200 incl. p  <=>  p < S/199
              min(self.L[i - 20:i]) * (1 - 1e-9),
              C[i - 1] - 1.5 * self.atr[i]]
        self._l[i] = th
        return th

    def profit_level(self, i, entry, k):
        th = sorted(self.profit_fixed(i) + [entry + 1.5 * self.atr[i]])
        lvl = th[k - 1] if k <= len(th) else INF
        return max(lvl, entry * (1 + 1e-6)) if lvl < INF else INF

    def loss_level(self, i, entry, k, held_days, mkt_below):
        const = int(held_days >= 5) + int(mkt_below)
        need = k - const
        if need <= 0:
            return entry * (1 - 1e-6)
        th = sorted(self.loss_fixed(i) + [entry - 2.0 * self.atr[i]], reverse=True)
        lvl = th[need - 1] if need <= len(th) else -INF
        return min(lvl, entry * (1 - 1e-6))


# ----------------------------------------------------------------------------- engine

def simulate(s: Series, kp=None, kl=None, lev=1, cash=None, mkt_below=frozenset(), X=None, XH=None,
             XL=None, intraday=None, start_i=201):
    """Union swing sleeve (RSI2 + IBS + TOM, exactly robust_backtest.swing) plus optional
    intraday exits. Returns ({date: net return on capital}, [trade dicts])."""
    dates, C, H, L, O = s.dates, s.C, s.H, s.L, s.O
    X = X or C
    XH, XL = XH or H, XL or L
    n = len(dates)
    month_ix = {}
    for i, d in enumerate(dates):
        month_ix.setdefault(d[:7], []).append(i)
    tom_days = set()
    for ix in month_ix.values():
        tom_days |= set(ix[:3]) | {ix[-1]}
    held = {"RSI2": False, "IBS": False, "TOM": False}
    age, out, pos, trades = 0, {}, False, []
    entry = entry_i = None
    tom_block = False
    for i in range(start_i, n):
        d = dates[i]
        c0 = (cash or {}).get(d, 0.0)
        exited = None
        if pos and (kp or kl) and s.atr[i]:
            pl = s.profit_level(i, entry, kp) if kp else INF
            ll = s.loss_level(i, entry, kl, i - entry_i, d in mkt_below) if kl else -INF
            day = intraday.get(d) if intraday else None
            if day:
                for px in day:
                    if px <= ll:
                        exited = (px * (1 - LOSS_SLIP), "loss")
                        break
                    if px >= pl:
                        exited = (px * (1 - PROFIT_SLIP), "profit")
                        break
            else:
                if O[i] <= ll:
                    exited = (O[i] * (1 - LOSS_SLIP), "loss")
                elif O[i] >= pl:
                    exited = (O[i] * (1 - PROFIT_SLIP), "profit")
                elif L[i] <= ll:
                    exited = (ll * (1 - LOSS_SLIP), "loss")
                elif H[i] >= pl:
                    exited = (pl * (1 - PROFIT_SLIP), "profit")
        if exited:
            px, kind = exited
            out[d] = lev * (px / X[i - 1] - 1) - FEE * lev
            trades.append({"in": dates[entry_i], "out": d, "ret": px / entry - 1, "days": i - entry_i, "kind": kind})
            pos, held, age, tom_block = False, {"RSI2": False, "IBS": False, "TOM": False}, 0, True
            continue
        r = X[i] / X[i - 1] - 1
        out[d] = lev * r if pos else c0
        hist = C[i - 199:i] + [X[i]]
        px = X[i]
        up = px > sum(hist) / 200
        r2 = compute_rsi(C[i - 59:i] + [px], 2)
        new = dict(held)
        if held["RSI2"]:
            new["RSI2"] = not (px > sum(C[i - 4:i] + [px]) / 5)
        else:
            new["RSI2"] = r2 is not None and r2 < 10 and up
        rng = XH[i] - XL[i]
        ibs = (X[i] - XL[i]) / rng if rng > 0 else 0.5
        if held["IBS"]:
            age += 1
            new["IBS"] = not (ibs > 0.8 or age >= 5)
        else:
            new["IBS"] = ibs < 0.2 and up
            age = 0
        nxt_tom = (i + 1) in tom_days
        if not nxt_tom:
            tom_block = False
        new["TOM"] = nxt_tom and not tom_block
        now = any(new.values())
        if now != pos:
            out[d] -= FEE * lev
            if now:
                entry, entry_i = px, i
            else:
                trades.append({"in": dates[entry_i], "out": d, "ret": px / entry - 1, "days": i - entry_i, "kind": "rule"})
        pos = now
        held = new
    return out, trades


# ----------------------------------------------------------------------------- data

def _get(url):
    from backtest import _get as g
    return g(url)


def ohlc_adj(sym, key):
    from backtest import BASE
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
            rows[d] = (float(r["open"]) * f, float(r["high"]) * f, float(r["low"]) * f, a[d])
    ds = sorted(rows)
    if len(ds) < 300:
        return None
    return Series(ds, [rows[d][0] for d in ds], [rows[d][1] for d in ds], [rows[d][2] for d in ds],
                  [rows[d][3] for d in ds])


# ----------------------------------------------------------------------------- report helpers

def tstats(trades):
    if not trades:
        return "0 trades"
    w = [t["ret"] for t in trades if t["ret"] > 0]
    lo = [t["ret"] for t in trades if t["ret"] <= 0]
    aw = statistics.mean(w) if w else 0
    al = statistics.mean(lo) if lo else 0
    kinds = {k: sum(1 for t in trades if t["kind"] == k) for k in ("rule", "profit", "loss")}
    return (f"{len(trades)} trades, win {len(w) / len(trades):.0%}, avg {statistics.mean(t['ret'] for t in trades):+.2%}, "
            f"avg win {aw:+.2%} / loss {al:+.2%}, hold {statistics.mean(t['days'] for t in trades):.1f}d, "
            f"exits rule/profit/loss {kinds['rule']}/{kinds['profit']}/{kinds['loss']}")


def cell(ser, dates):
    if len(dates) < 20:
        return "n/a"
    st, _, _ = curve_stats([ser.get(d, 0.0) for d in dates], dates)
    return f"{st['cagr']:.1%} / {st['mdd']:.1%}"


def label(kp, kl):
    if not kp and not kl:
        return "BASE (current rules)"
    return " + ".join(x for x in (f"profit K={kp}" if kp else "", f"loss K={kl}" if kl else "") if x)


# ----------------------------------------------------------------------------- main

def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    from intraday_backtest import fetch_5min, fetch_unadjusted
    log = []
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    S = {}
    for n, sym in enumerate(pool + ["QQQ", "BIL"]):
        s = ohlc_adj(sym, key)
        if s:
            S[sym] = s
        else:
            log.append(f"{sym}: no data")
        if n % 40 == 0:
            print(f"daily {n}/{len(pool) + 2}", flush=True)
        time.sleep(0.08)
    Q, B = S["QQQ"], S["BIL"]
    qd = [d for d in Q.dates if d in set(B.dates)]
    qi = {d: i for i, d in enumerate(Q.dates)}
    bi = {d: i for i, d in enumerate(B.dates)}
    br = {d: B.C[bi[d]] / B.C[bi[d] - 1] - 1 for d in qd if bi[d] > 0}
    qr = {d: Q.C[qi[d]] / Q.C[qi[d] - 1] - 1 for d in qd if qi[d] > 0}
    mkt_below = set()
    for i in range(201, len(Q.dates)):
        if Q.C[i - 1] < sum(Q.C[i - 200:i]) / 200:
            mkt_below.add(Q.dates[i])

    # monthly picks (same as mix_optimizer): top 10 by 12-month return at each month end
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}
    for m in me:
        k = qd.index(m)
        b = qd[k - 252]
        sc = []
        for sym in pool:
            s = S.get(sym)
            if s and m in s.ix and b in s.ix:
                sc.append((s.C[s.ix[m]] / s.C[s.ix[b]] - 1, sym))
        picks[m] = [x for _, x in sorted(sc, reverse=True)[:10]]
    ever = sorted({x for v in picks.values() for x in v})
    tdates = [d for d in qd if d > me[0]]
    pick_of = {}
    for d in tdates:
        pick_of[d] = picks[[m for m in me if m < d][-1]]

    # QQQ intraday (5-minute bars) for the true-intraday SWING_Q run and the 15:50 decision
    q5 = fetch_5min("QQQ", key, log)
    raw_q = {r["date"]: r["price"] for r in fetch_unadjusted("QQQ", key)}
    X, XH, XL = list(Q.C), list(Q.H), list(Q.L)
    intra = {}
    for i, d in enumerate(Q.dates):
        bars = q5.get(d)
        if bars and d in raw_q:
            f = Q.C[i] / raw_q[d]
            upto = [b for b in bars if b["t"] <= "15:45"]
            if len(upto) >= 60:
                X[i], XH[i], XL[i] = upto[-1]["c"] * f, max(b["h"] for b in upto) * f, min(b["l"] for b in upto) * f
            bt = {b["t"]: b["c"] * f for b in bars}
            pts = [bt[t] for t in CHECKS if t in bt]
            if len(pts) >= 8:
                intra[d] = pts

    variants = [(None, None)] + [(k, None) for k in (2, 3, 4, 5)] + [(None, k) for k in (2, 3, 4)] + \
               [(a, b) for a in (2, 3, 4, 5) for b in (2, 3, 4)]

    # sanity: engine BASE == robust_backtest.swing
    base_q, _ = simulate(Q, lev=2, cash=br)
    ref_q = swing(Q.dates, Q.C, Q.H, Q.L, None, lev=2, cash=br)
    diff = max(abs(base_q.get(d, 0) - ref_q.get(d, 0)) for d in ref_q)
    log.append(f"engine check vs robust_backtest.swing (SWING_Q, close): max daily diff {diff:.2e}")

    res = {}
    for kp, kl in variants:
        sq, tq = simulate(Q, kp, kl, lev=2, cash=br, mkt_below=mkt_below)
        sqi, tqi = simulate(Q, kp, kl, lev=2, cash=br, mkt_below=mkt_below, X=X, XH=XH, XL=XL, intraday=intra)
        per, tm = {}, []
        for sym in ever:
            if sym in S:
                r, t = simulate(S[sym], kp, kl, lev=1, cash=br, mkt_below=mkt_below)
                per[sym] = r
                tm += [x for x in t if x["in"] in pick_of and sym in pick_of[x["in"]]]
        sm = {}
        for d in tdates:
            rs = [per[x].get(d, 0.0) for x in pick_of[d] if x in per]
            sm[d] = sum(rs) / len(rs) if rs else 0.0
        res[(kp, kl)] = {"q": sq, "qi": sqi, "m": sm, "tq": tq, "tqi": tqi, "tm": tm}
        print(f"variant {label(kp, kl)} done", flush=True)

    start = max("2019-01-02", min(res[(None, None)]["m"]))
    pd = [d for d in tdates if d >= start]
    train = [d for d in pd if d <= "2022-12-31"]
    test = [d for d in pd if d >= "2023-01-01"]
    for v in res.values():
        v["port"] = dict(zip(pd, combine([0.7, 0.3], [v["qi"], v["m"]], pd)))
        v["port_proxy"] = dict(zip(pd, combine([0.7, 0.3], [v["q"], v["m"]], pd)))

    def mar(ser, ds):
        st, _, _ = curve_stats([ser.get(d, 0.0) for d in ds], ds)
        return st["cagr"] / abs(st["mdd"]) if st["mdd"] else 0, st

    out = [f"# Exit backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Period {pd[0]} → {pd[-1]}. Portfolio = 70% SWING_Q (QLD, 2x, true intraday checks on 5-minute QQQ "
           "bars, close decision at 15:50) + 30% SWING_M (top-10 momentum names, daily-bar proxy for intraday "
           "checks), monthly rebalance. Cells are CAGR / max drawdown. Formulas are in the file header.\n",
           f"**QQQ:** full {cell(qr, pd)} · 2019–22 {cell(qr, train)} · 2023–26 {cell(qr, test)}\n",
           "## Portfolio (70/30) by variant\n",
           "| Variant | Full period | 2019–22 (choose) | 2023–26 (unseen) | Full, SWING_Q on daily proxy |",
           "|---|---|---|---|---|"]
    for kv in variants:
        v = res[kv]
        out.append(f"| {label(*kv)} | {cell(v['port'], pd)} | {cell(v['port'], train)} | {cell(v['port'], test)} | "
                   f"{cell(v['port_proxy'], pd)} |")

    out.append("\n## Walk-forward — chosen on 2019–22 only, scored on 2023–26\n")
    out.append("| Choice rule (2019–22) | Variant | 2019–22 | 2023–26 (unseen) | BASE 2023–26 |\n|---|---|---|---|---|")
    base = res[(None, None)]["port"]
    rules = [
        ("Best return / drawdown (MAR)", lambda kv: mar(res[kv]["port"], train)[0]),
        ("Best CAGR", lambda kv: mar(res[kv]["port"], train)[1]["cagr"]),
        ("Best CAGR with DD no worse than BASE", lambda kv: mar(res[kv]["port"], train)[1]["cagr"]
         if mar(res[kv]["port"], train)[1]["mdd"] >= mar(base, train)[1]["mdd"] - 1e-9 else -9),
        ("Best profit-only (MAR)", lambda kv: mar(res[kv]["port"], train)[0] if kv[1] is None and kv[0] else -9),
        ("Best loss-only (MAR)", lambda kv: mar(res[kv]["port"], train)[0] if kv[0] is None and kv[1] else -9),
    ]
    for lab, f in rules:
        kv = max(variants, key=f)
        v = res[kv]
        out.append(f"| {lab} | {label(*kv)} | {cell(v['port'], train)} | {cell(v['port'], test)} | {cell(base, test)} |")

    for name, sk, tk in (("SWING_Q (QLD 2x), true intraday", "qi", "tqi"), ("SWING_Q (QLD 2x), daily-bar proxy", "q", "tq"),
                         ("SWING_M (10 names 1x), daily-bar proxy", "m", "tm")):
        out.append(f"\n## {name}\n")
        out.append("| Variant | Full | 2019–22 | 2023–26 | Trades (1x, full period) |\n|---|---|---|---|---|")
        for kv in variants:
            v = res[kv]
            tr = [t for t in v[tk] if t["in"] >= pd[0]]
            out.append(f"| {label(*kv)} | {cell(v[sk], pd)} | {cell(v[sk], train)} | {cell(v[sk], test)} | {tstats(tr)} |")

    out.append("\n## Data log\n")
    out.extend(f"- {x}" for x in (log[:25] or ["(clean)"]))
    (HERE / "exit_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
