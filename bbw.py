"""BBW sleeves: 15-minute Bollinger-squeeze pullback strategies, plus the weekly search
for new ones and the monthly review that retires or rotates them.

Authority: Ryan, REAL live turns 2026-11-01:
  "add this as a sleeve to the auto options routine, we also need to always search for
   similar strategys on other names including leveraged variations or others to see if
   there is another that tests well and we should add it"
  "We need a way to remove bad strats or rotate less effective ones for new ones if one
   starts to not perform well. Maybe monthly"
  Sizing: 20% of the sleeve base, taken from SWING_Q (70 -> 50). New finds are PROPOSED
  to Ryan and added only on his approval.

The rules are TrendSpider's published "NVDL BBW Strategy" (15-minute bars):
  ENTRY (all, on a completed candle's close; fill at the next candle's open):
    - the upper Bollinger band (20, 2) crosses ABOVE the close. Read literally, as
      TrendSpider wrote it: price was above the upper band and closes back inside it.
      (The other reading, close crossing above the band, made 32% vs TrendSpider's ~95%
      over the same window; the literal reading made 93%. See docs/bbw-sleeve.md.)
    - MACD(19, 39) line > 0
    - close > close 10 candles ago
    - a "squeeze" in the last 5 candles: Bollinger width at or below each of the
      prior 14 candles' widths.
  EXITS (checked on each candle close, filled at the next open):
    - stop: close <= entry x (1 - 2.5%)
    - trailing: close <= highest close since entry x (1 - 6%)
    - 50 candles held, any P/L
    - 10 candles held while P/L < 0

Pure functions, no network. The routine supplies 5-minute bars from the Robinhood
connector (it has no 15-minute interval) and this module builds 15-minute candles.

CLI:
  python3 bbw.py decide <bars5.json> --now <ISO-UTC>      # live decision for every live strategy
  python3 bbw.py backtest <bars15.json> [--variant <name>]
  python3 bbw.py discover                                   # weekly search over data/intraday15/
  python3 bbw.py review --today YYYY-MM-DD                  # monthly review
"""
from __future__ import annotations

import json
import math
import os
import statistics as st
import sys
from datetime import datetime, timedelta, timezone

STATE_FILE = "bbw_state.json"
CACHE_DIR = os.path.join("data", "intraday15")

DEFAULT = {
    "bb_len": 20, "bb_k": 2.0,
    "macd_fast": 19, "macd_slow": 39,
    "mom_lookback": 10,
    "squeeze_lookback": 14, "squeeze_within": 5,
    "stop": 0.025, "trail": 0.06,
    "max_bars": 50, "loss_bars": 10,
}

# The search's variant family. Kept SMALL on purpose: every extra variant tested is one more
# chance to find something that looked good by luck. A variant must pass both the in-sample
# and the later, unseen out-of-sample stretch.
VARIANTS = {
    "template": {},
    "hold30": {"max_bars": 30},
    "hold80": {"max_bars": 80},
    "macd12_26": {"macd_fast": 12, "macd_slow": 26},
    "squeeze20": {"squeeze_lookback": 20},
}

# Acceptance rules for a candidate (symbol x variant). All required.
QUALIFY = {
    "min_trades_total": 15,
    "min_trades_oos": 6,
    "oos_frac": 0.4,          # last 40% of the candles are never used to pick the variant
    "max_dd": -0.15,
    "min_months": 4,
}

# Leveraged fund -> the stock or index it tracks. A proposal on a symbol whose underlying is
# already live says so, because it adds to the same bet rather than diversifying.
UNDERLYING = {
    "NVDL": "NVDA", "NVDU": "NVDA", "AMDL": "AMD", "TSLL": "TSLA", "AAPU": "AAPL", "AMZU": "AMZN",
    "GGLL": "GOOGL", "METU": "META", "MSFU": "MSFT", "AVL": "AVGO", "PLTU": "PLTR", "MUU": "MU",
    "QLD": "QQQ", "TQQQ": "QQQ", "SPXL": "SPY", "SSO": "SPY", "SOXL": "SOXX", "USD": "SOXX", "TECL": "XLK",
}


def underlying(sym: str) -> str:
    return UNDERLYING.get(sym, sym)


# Monthly review thresholds.
REVIEW = {
    "min_live_trades": 10,        # below this, live results are too few to judge
    "pause_dd": -0.20,            # strategy equity down 20% from its own high: AUTO-PAUSE entries
    "rotate_margin": 0.10,        # a candidate must beat the weakest live strategy's score by 10 pts
    "recent_months": 4,           # re-backtest window for the review
}


# ---------------------------------------------------------------- candles
def aggregate_15m(bars5: list[dict], now_utc: datetime | None = None) -> list[list]:
    """5-minute Robinhood bars -> 15-minute candles [iso, o, h, l, c].

    Interpolated bars are dropped. A candle is kept only if it is complete: its end time is
    at or before now_utc (when given). Buckets align to :00/:15/:30/:45, which matches the
    9:30 ET open."""
    agg: dict[datetime, list] = {}
    for b in sorted(bars5, key=lambda x: x["begins_at"]):
        if b.get("interpolated"):
            continue
        t = datetime.fromisoformat(b["begins_at"].replace("Z", "+00:00"))
        k = t.replace(minute=(t.minute // 15) * 15, second=0, microsecond=0)
        o, h, l, c = (float(b[x]) for x in ("open_price", "high_price", "low_price", "close_price"))
        if k not in agg:
            agg[k] = [o, h, l, c]
        else:
            a = agg[k]
            a[1] = max(a[1], h)
            a[2] = min(a[2], l)
            a[3] = c
    out = []
    for k in sorted(agg):
        if now_utc is not None and k + timedelta(minutes=15) > now_utc:
            continue
        out.append([k.isoformat()] + agg[k])
    return out


# ---------------------------------------------------------------- indicators
def _ema(a: list[float], p: int) -> list[float | None]:
    out: list[float | None] = [None] * len(a)
    if len(a) < p:
        return out
    k = 2 / (p + 1)
    s = sum(a[:p]) / p
    out[p - 1] = s
    for i in range(p, len(a)):
        s = a[i] * k + s * (1 - k)
        out[i] = s
    return out


def indicators(C: list[float], p: dict) -> dict:
    n = len(C)
    L, K = p["bb_len"], p["bb_k"]
    up: list[float | None] = [None] * n
    wd: list[float | None] = [None] * n
    for i in range(L - 1, n):
        w = C[i - L + 1:i + 1]
        m = sum(w) / L
        sd = math.sqrt(sum((x - m) ** 2 for x in w) / L)   # population std (TA-Lib)
        up[i] = m + K * sd
        wd[i] = 2 * K * sd / m
    ef, es = _ema(C, p["macd_fast"]), _ema(C, p["macd_slow"])
    macd = [(ef[i] - es[i]) if (ef[i] is not None and es[i] is not None) else None for i in range(n)]
    lb = p["squeeze_lookback"]
    sq = [False] * n
    for j in range(L - 1 + lb, n):
        sq[j] = all(wd[j] <= wd[j - k] for k in range(1, lb + 1))
    return {"up": up, "wd": wd, "macd": macd, "sq": sq}


def warmup(p: dict) -> int:
    return max(p["bb_len"] + p["squeeze_lookback"] + p["squeeze_within"], p["macd_slow"], p["mom_lookback"] + 1) + 1


def entry_signal(C: list[float], ind: dict, i: int, p: dict) -> bool:
    if i < warmup(p) or ind["macd"][i] is None:
        return False
    up = ind["up"]
    cross = up[i] > C[i] and up[i - 1] <= C[i - 1]
    if not cross:
        return False
    if not ind["macd"][i] > 0:
        return False
    if not C[i] > C[i - p["mom_lookback"]]:
        return False
    w = p["squeeze_within"]
    return any(ind["sq"][j] for j in range(i - w + 1, i + 1))


def exit_reason(entry: float, peak: float, close: float, held: int, p: dict) -> str | None:
    r = close / entry - 1
    if r <= -p["stop"]:
        return "stop"
    if close <= peak * (1 - p["trail"]):
        return "trail"
    if held >= p["max_bars"]:
        return "time"
    if held >= p["loss_bars"] and r < 0:
        return "loss_time"
    return None


# ---------------------------------------------------------------- backtest
def backtest(B: list[list], p: dict | None = None, start: int = 0, end: int | None = None) -> dict:
    """Long-only, one position, 100% of the sleeve per trade, fills at the next candle's open.
    Indicators use all bars before `start` as warm-up; trades are only opened in [start, end)."""
    p = {**DEFAULT, **(p or {})}
    T = [x[0] for x in B]
    O = [x[1] for x in B]
    C = [x[4] for x in B]
    n = len(C) if end is None else end
    ind = indicators(C[:n], p)
    eq, hwm, mdd = 1.0, 1.0, 0.0
    trades = []
    pos = None
    i = max(start, warmup(p))
    while i < n - 1:
        if pos is None:
            if entry_signal(C, ind, i, p):
                pos = {"e": O[i + 1], "ei": i + 1, "pk": O[i + 1]}
                i = i + 1
            else:
                i += 1
                continue
        pos["pk"] = max(pos["pk"], C[i])
        held = i - pos["ei"] + 1
        why = exit_reason(pos["e"], pos["pk"], C[i], held, p)
        if why:
            xp = O[i + 1]
            ret = xp / pos["e"] - 1
            eq *= 1 + ret
            hwm = max(hwm, eq)
            mdd = min(mdd, eq / hwm - 1)
            trades.append({"in": T[pos["ei"]], "out": T[i + 1], "ret": ret, "why": why})
            pos = None
        i += 1
    s0 = max(start, warmup(p))
    bh = (C[n - 1] / O[s0] - 1) if n - 1 > s0 else 0.0
    return summarize(trades, eq - 1, mdd, bh)


def summarize(trades: list[dict], total: float, mdd: float, bh: float) -> dict:
    rets = [t["ret"] for t in trades]
    wins = [r for r in rets if r > 0]
    losses = [r for r in rets if r <= 0]
    top = sorted(rets, reverse=True)
    ex_top3 = math.prod(1 + r for r in top[3:]) - 1 if len(top) > 3 else -1.0
    return {
        "ret": total, "bh": bh, "trades": len(rets),
        "win": len(wins) / len(rets) if rets else 0.0,
        "avg": st.mean(rets) if rets else 0.0,
        "payoff": (st.mean(wins) / abs(st.mean(losses))) if wins and losses else None,
        "max_dd": mdd, "ex_top3": ex_top3, "list": trades,
    }


# ---------------------------------------------------------------- search (weekly)
def months_covered(B: list[list]) -> float:
    if len(B) < 2:
        return 0.0
    a = datetime.fromisoformat(B[0][0])
    b = datetime.fromisoformat(B[-1][0])
    return (b - a).days / 30.4


def qualify(B: list[list], variants: dict | None = None) -> dict:
    """Pick the best variant on the first (1 - oos_frac) of the data, then test it on the
    rest, which the pick never saw. Returns the verdict and every number behind it."""
    variants = variants or VARIANTS
    q = QUALIFY
    if months_covered(B) < q["min_months"]:
        return {"pass": False, "why": f"only {months_covered(B):.1f} months of 15-min data", "variant": None}
    cut = int(len(B) * (1 - q["oos_frac"]))
    best, best_ins = None, None
    for name, over in variants.items():
        r = backtest(B, over, 0, cut)
        if best_ins is None or r["ret"] - r["bh"] > best_ins["ret"] - best_ins["bh"]:
            best, best_ins = name, r
    p = variants[best]
    oos = backtest(B, p, cut)
    full = backtest(B, p)
    fails = []
    if full["trades"] < q["min_trades_total"]:
        fails.append(f"{full['trades']} trades < {q['min_trades_total']}")
    if oos["trades"] < q["min_trades_oos"]:
        fails.append(f"{oos['trades']} out-of-sample trades < {q['min_trades_oos']}")
    for label, r in (("in-sample", best_ins), ("out-of-sample", oos)):
        if r["ret"] <= 0:
            fails.append(f"{label} return {r['ret']*100:.1f}% <= 0")
        if r["ret"] <= r["bh"]:
            fails.append(f"{label} {r['ret']*100:.1f}% does not beat buy-and-hold {r['bh']*100:.1f}%")
    if full["ex_top3"] <= 0:
        fails.append(f"without its 3 best trades it makes {full['ex_top3']*100:.1f}%")
    if full["max_dd"] < q["max_dd"]:
        fails.append(f"drawdown {full['max_dd']*100:.1f}% worse than {q['max_dd']*100:.0f}%")
    score = oos["ret"] - oos["bh"]
    return {"pass": not fails, "why": "; ".join(fails) or "passes every rule", "variant": best,
            "score": score, "in_sample": _brief(best_ins), "out_of_sample": _brief(oos), "full": _brief(full),
            "variants_tested": len(variants), "months": round(months_covered(B), 1)}


def _brief(r: dict) -> dict:
    return {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k != "list"}


def discover(state: dict, cache_dir: str = CACHE_DIR) -> list[dict]:
    """Run qualify() on every cached symbol. Live strategies are scored too (for the review)."""
    out = []
    for sym in state.get("universe", []):
        f = os.path.join(cache_dir, f"{sym}.json")
        if not os.path.exists(f):
            out.append({"symbol": sym, "pass": False, "why": "no cached 15-min data yet"})
            continue
        B = json.load(open(f))
        r = qualify(B)
        r["symbol"] = sym
        out.append(r)
    return sorted(out, key=lambda r: -(r.get("score") or -9))


def merge_cache(old: list[list], new: list[list]) -> list[list]:
    d = {x[0]: x for x in old}
    d.update({x[0]: x for x in new})
    return [d[k] for k in sorted(d)]


# ---------------------------------------------------------------- live decision (every 15 min)
def live_strategies(state: dict) -> list[dict]:
    return [s for s in state.get("strategies", []) if s.get("status") in ("live", "paused")]


def fill_index(T: list[str], entry_time: str) -> int | None:
    """Index of the candle the entry filled in: the first candle starting at or after the
    15-minute bucket of entry_time. Works for an ISO fill time or a candle start; an order
    filled at the next session's open maps to that session's first candle."""
    t = datetime.fromisoformat(entry_time.replace("Z", "+00:00"))
    t = t.replace(minute=(t.minute // 15) * 15, second=0, microsecond=0)
    for i, x in enumerate(T):
        if datetime.fromisoformat(x) >= t:
            return i
    return None


def decide_one(strat: dict, pos: dict | None, B: list[list]) -> dict:
    """Decide on the newest completed candle. With a position, every candle since the last
    one evaluated is checked in order, so a missed run still exits (late, and says so). A
    new entry is only ever taken on the NEWEST candle: a stale signal is not chased."""
    p = {**DEFAULT, **strat.get("params", {})}
    T = [x[0] for x in B]
    C = [x[4] for x in B]
    if len(B) < warmup(p) + 2:
        return {"action": "none", "why": f"only {len(B)} candles, need {warmup(p) + 2}"}
    last = len(B) - 1
    if pos:
        start = fill_index(T, pos["entry_candle"])
        if start is None:
            return {"action": "hold", "why": "fill candle not in the bars yet; fetch more history", "candle": T[last]}
        peak = pos.get("peak_close", pos["entry_price"])
        done = pos.get("last_candle")
        for i in range(start, last + 1):
            peak = max(peak, C[i])
            held = i - start + 1
            if done and T[i] <= done:
                continue
            why = exit_reason(pos["entry_price"], peak, C[i], held, p)
            if why:
                late = i < last
                return {"action": "sell", "why": why, "candle": T[i], "late": late, "held": held,
                        "close": C[i], "peak_close": peak,
                        "pnl_pct": round((C[i] / pos["entry_price"] - 1) * 100, 2)}
        return {"action": "hold", "candle": T[last], "held": last - start + 1, "peak_close": peak,
                "pnl_pct": round((C[last] / pos["entry_price"] - 1) * 100, 2)}
    if strat.get("status") == "paused":
        return {"action": "none", "why": "strategy paused (drawdown rule); waiting for Ryan", "candle": T[last]}
    if strat.get("last_candle") == T[last]:
        return {"action": "none", "why": "newest candle already evaluated", "candle": T[last]}
    ind = indicators(C, p)
    if entry_signal(C, ind, last, p):
        return {"action": "buy", "why": "entry signal", "candle": T[last], "close": C[last]}
    return {"action": "none", "why": "no signal", "candle": T[last]}


def target_usd(strat: dict, total_value: float, invest_frac: float = 0.95) -> float:
    return round(total_value * invest_frac * strat["weight"], 2)


# ---------------------------------------------------------------- monthly review
def strategy_equity(trades: list[dict]) -> tuple[float, float]:
    """Compounded return of a strategy's closed live trades, and its drawdown from its own high."""
    eq, hwm = 1.0, 1.0
    for t in trades:
        eq *= 1 + t["ret"]
        hwm = max(hwm, eq)
    return eq - 1, eq / hwm - 1


def review(state: dict, scores: dict[str, dict]) -> list[dict]:
    """Monthly: verdict per live strategy plus rotation proposals. Only PAUSE is automatic
    (a drawdown breach); retiring, rotating and adding all wait for a live Ryan turn."""
    R = REVIEW
    out = []
    live = [s for s in state.get("strategies", []) if s.get("status") in ("live", "paused")]
    for s in live:
        trades = [t for t in state.get("trade_log", []) if t.get("strategy") == s["id"]]
        tot, dd = strategy_equity(trades)
        sc = scores.get(s["symbol"], {})
        v = {"id": s["id"], "symbol": s["symbol"], "live_trades": len(trades),
             "live_return": round(tot, 4), "live_dd": round(dd, 4),
             "recent_test": sc.get("why"), "recent_score": sc.get("score")}
        if dd <= R["pause_dd"]:
            v["verdict"] = "PAUSE"
            v["reason"] = f"live drawdown {dd*100:.1f}% breached {R['pause_dd']*100:.0f}%: new entries stop until Ryan resumes or retires it"
        elif len(trades) >= R["min_live_trades"] and (st.mean([t["ret"] for t in trades]) <= 0):
            v["verdict"] = "PROPOSE RETIRE"
            v["reason"] = f"average live trade {st.mean([t['ret'] for t in trades])*100:.2f}% over {len(trades)} trades"
        elif sc and not sc.get("pass"):
            v["verdict"] = "WATCH"
            v["reason"] = f"no longer passes on recent data: {sc.get('why')}"
        else:
            v["verdict"] = "KEEP"
            v["reason"] = "live and recent tests acceptable" if trades else "no live trades yet"
        out.append(v)
    live_syms = {s["symbol"] for s in live}
    live_under = {underlying(s["symbol"]): s["symbol"] for s in live}
    weakest = min((v for v in out if v.get("recent_score") is not None), key=lambda v: v["recent_score"], default=None)
    for sym, sc in scores.items():
        if sym in live_syms or not sc.get("pass"):
            continue
        if weakest and weakest["verdict"] in ("WATCH", "PROPOSE RETIRE", "PAUSE") and \
                sc["score"] >= (weakest["recent_score"] or 0) + R["rotate_margin"]:
            out.append({"id": None, "symbol": sym, "verdict": "PROPOSE ROTATE",
                        "reason": f"replace {weakest['symbol']} (score {weakest['recent_score']}) with {sym} {sc['variant']} (score {round(sc['score'],3)})"})
        else:
            same = live_under.get(underlying(sym))
            note = f"; SAME UNDERLYING as live {same}, so it adds to that bet" if same else ""
            out.append({"id": None, "symbol": sym, "verdict": "PROPOSE ADD",
                        "reason": f"{sc['variant']} passes: out-of-sample {sc['out_of_sample']['ret']*100:.1f}% vs buy-and-hold {sc['out_of_sample']['bh']*100:.1f}%{note}"})
    return out


# ---------------------------------------------------------------- CLI
def _load_state() -> dict:
    return json.load(open(STATE_FILE))


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    if cmd == "backtest":
        B = json.load(open(argv[2]))
        var = argv[argv.index("--variant") + 1] if "--variant" in argv else "template"
        r = backtest(B, VARIANTS[var])
        print(json.dumps(_brief(r), indent=1))
        for t in r["list"]:
            print(f"  {t['in'][:16]} -> {t['out'][:16]} {t['ret']*100:+6.2f}% {t['why']}")
        return 0
    if cmd == "decide":
        raw = json.load(open(argv[2]))
        now = datetime.fromisoformat(argv[argv.index("--now") + 1].replace("Z", "+00:00"))
        state = _load_state()
        res = []
        for s in live_strategies(state):
            bars5 = raw.get(s["symbol"], [])
            B = aggregate_15m(bars5, now)
            d = decide_one(s, state.get("positions", {}).get(s["id"]), B)
            d.update({"id": s["id"], "symbol": s["symbol"], "weight": s["weight"]})
            res.append(d)
        print(json.dumps(res, indent=1))
        return 0
    if cmd == "discover":
        state = _load_state()
        for r in discover(state):
            print(json.dumps({k: r.get(k) for k in ("symbol", "pass", "variant", "score", "why", "months")}))
        return 0
    if cmd == "review":
        state = _load_state()
        scores = {r["symbol"]: r for r in discover(state)}
        print(json.dumps(review(state, scores), indent=1))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
