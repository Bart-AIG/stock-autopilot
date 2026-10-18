"""
Hourly mean-reversion screen: does the TrendSpider Sidekick META idea work, and on
which other names? (Ryan, 2026-10-18, sharing a TrendSpider screenshot: "Build me a
reversion strategy for trading $META" -> 5 long-only entries on 1-hour bars, each with
a plain fixed 12-candle exit.)

Runs on GitHub Actions (FMP key). 1-hour regular-session bars from 2021-01-01.

Entries (long only, signal on a bar's close, filled at the NEXT bar's open, exit at the
close of the 12th bar after entry, one position per symbol at a time):
  E1 RSI2_UPTREND   RSI(2) < 10 and close > SMA(200)            (Connors, hourly)
  E2 BB_VOLUME      close < lower Bollinger(20, 2) and volume > 1.5x its 20-bar mean
  E3 SHARP_5BAR     5-bar return < -2.5 x (100-bar stdev of 1-bar returns) x sqrt(5)
  E4 STRETCH_EMA20  (EMA20 - close) / ATR(14) > 2
  E5 STOCH_HOOK     Stochastic(14,3): %K crosses above %D with both < 20

Baseline ("random entry"): the mean 12-bar forward return from EVERY bar's next open.
Edge = mean trade return - baseline. An entry only "works" on a name if the edge is
positive in BOTH halves (2021-23 and 2024-26) and the full-period t-stat > 2.

Costs: 2 bp per side (liquid large caps). Honest limits: one path of history; 5 entries
x ~45 names = ~225 tests, so a handful will pass by chance (expect ~5% false positives
at t > 2 before the two-halves check); fills at the next bar's open, no gap-through.
"""

from __future__ import annotations

import json
import math
import os
import statistics
import time
from datetime import date, timedelta
from pathlib import Path

from backtest import BASE, _get

HERE = Path(__file__).resolve().parent
START = "2021-01-01"
SPLIT = "2024-01-01"
HOLD = 12
COST = 2e-4  # per side

UNIVERSE = [
    "META", "AAPL", "MSFT", "AMZN", "GOOGL", "NVDA", "TSLA", "AMD", "AVGO", "NFLX",
    "CRM", "ADBE", "ORCL", "NOW", "INTU", "QCOM", "TXN", "MU", "AMAT", "PANW",
    "UBER", "SHOP", "PLTR", "ISRG", "COST", "WMT", "HD", "MCD", "PG", "KO", "PEP",
    "JPM", "V", "MA", "UNH", "LLY", "XOM", "CAT", "GE", "BA",
    "SPY", "QQQ", "IWM", "SMH", "XLF",
]
ENTRIES = ["RSI2_UPTREND", "BB_VOLUME", "SHARP_5BAR", "STRETCH_EMA20", "STOCH_HOOK"]


# ----------------------------------------------------------------------------- data

def fetch_hourly(sym: str, key: str, log: list[str]) -> list[dict]:
    rows: dict[str, dict] = {}
    d, end = date.fromisoformat(START), date.today()
    while d < end:
        e = min(d + timedelta(days=45), end)
        data = _get(f"{BASE}/historical-chart/1hour?symbol={sym}&from={d}&to={e}&apikey={key}")
        if isinstance(data, list):
            for r in data:
                t = r["date"]
                if "09:30" <= t[11:16] <= "15:59":
                    rows[t] = {"t": t, "o": float(r["open"]), "h": float(r["high"]),
                               "l": float(r["low"]), "c": float(r["close"]),
                               "v": float(r.get("volume") or 0)}
        else:
            log.append(f"{sym} {d}..{e}: {str(data)[:80]}")
        d = e + timedelta(days=1)
        time.sleep(0.12)
    return [rows[k] for k in sorted(rows)]


# ----------------------------------------------------------------------------- indicators

def sma(x, n):
    out, s = [None] * len(x), 0.0
    for i, v in enumerate(x):
        s += v
        if i >= n:
            s -= x[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def ema(x, n):
    out, k, e = [None] * len(x), 2 / (n + 1), None
    for i, v in enumerate(x):
        e = v if e is None else e + k * (v - e)
        out[i] = e if i >= n - 1 else None
    return out


def rsi(c, n):
    out = [None] * len(c)
    ag = al = None
    for i in range(1, len(c)):
        ch = c[i] - c[i - 1]
        g, l = max(ch, 0.0), max(-ch, 0.0)
        if i <= n:
            ag = (ag or 0) + g / n
            al = (al or 0) + l / n
            if i < n:
                continue
        else:
            ag = (ag * (n - 1) + g) / n
            al = (al * (n - 1) + l) / n
        out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def rolling_std(x, n):
    out = [None] * len(x)
    for i in range(n - 1, len(x)):
        w = x[i - n + 1:i + 1]
        if None in w:
            continue
        out[i] = statistics.pstdev(w)
    return out


def atr(b, n):
    tr = [b[0]["h"] - b[0]["l"]] + [
        max(b[i]["h"] - b[i]["l"], abs(b[i]["h"] - b[i - 1]["c"]), abs(b[i]["l"] - b[i - 1]["c"]))
        for i in range(1, len(b))]
    out, a = [None] * len(b), None
    for i, t in enumerate(tr):
        a = t if a is None else (a * (n - 1) + t) / n
        out[i] = a if i >= n else None
    return out


def signals(b: list[dict]) -> dict[str, list[bool]]:
    c = [x["c"] for x in b]
    v = [x["v"] for x in b]
    N = len(b)
    r2, s200 = rsi(c, 2), sma(c, 200)
    m20, sd20 = sma(c, 20), rolling_std(c, 20)
    vm20 = sma(v, 20)
    r1 = [None] + [c[i] / c[i - 1] - 1 for i in range(1, N)]
    sd100 = rolling_std(r1, 100)
    e20, a14 = ema(c, 20), atr(b, 14)
    # stochastic 14,3
    k_raw = [None] * N
    for i in range(13, N):
        hh = max(x["h"] for x in b[i - 13:i + 1])
        ll = min(x["l"] for x in b[i - 13:i + 1])
        k_raw[i] = 50.0 if hh == ll else 100 * (c[i] - ll) / (hh - ll)
    k = [None] * N
    for i in range(15, N):
        k[i] = sum(k_raw[i - 2:i + 1]) / 3
    d = [None] * N
    for i in range(17, N):
        d[i] = sum(k[i - 2:i + 1]) / 3

    out = {e: [False] * N for e in ENTRIES}
    for i in range(1, N):
        if r2[i] is not None and s200[i] is not None:
            out["RSI2_UPTREND"][i] = r2[i] < 10 and c[i] > s200[i]
        if m20[i] is not None and sd20[i] is not None and vm20[i]:
            out["BB_VOLUME"][i] = c[i] < m20[i] - 2 * sd20[i] and v[i] > 1.5 * vm20[i]
        if i >= 5 and sd100[i]:
            out["SHARP_5BAR"][i] = (c[i] / c[i - 5] - 1) < -2.5 * sd100[i] * math.sqrt(5)
        if e20[i] is not None and a14[i]:
            out["STRETCH_EMA20"][i] = (e20[i] - c[i]) / a14[i] > 2
        if None not in (k[i], d[i], k[i - 1], d[i - 1]):
            out["STOCH_HOOK"][i] = k[i - 1] <= d[i - 1] and k[i] > d[i] and k[i] < 20 and d[i] < 20
    return out


# ----------------------------------------------------------------------------- backtest

def fwd(b, i):
    """Return from bar i+1's open to bar i+HOLD's close (net of costs), or None."""
    if i + HOLD >= len(b):
        return None
    return b[i + HOLD]["c"] / b[i + 1]["o"] - 1 - 2 * COST


def trades(b, sig):
    out, i = [], 0
    while i < len(b):
        if sig[i]:
            r = fwd(b, i)
            if r is None:
                break
            out.append((b[i]["t"], r))
            i += HOLD + 1
        else:
            i += 1
    return out


def summarize(tr, base):
    if not tr:
        return None
    rs = [r for _, r in tr]
    n = len(rs)
    m = statistics.mean(rs)
    sd = statistics.pstdev(rs) if n > 1 else 0
    wins = [r for r in rs if r > 0]
    losses = [-r for r in rs if r <= 0]
    pf = (sum(wins) / sum(losses)) if losses and sum(losses) > 0 else float("inf")
    t = (m - base) / (sd / math.sqrt(n)) if sd > 0 and n > 1 else 0
    return {"n": n, "mean": m, "edge": m - base, "win": len(wins) / n, "pf": pf, "t": t,
            "total": math.prod(1 + r for r in rs) - 1}


def baseline(b, lo=None, hi=None):
    rs = [fwd(b, i) for i in range(len(b))
          if (lo is None or b[i]["t"] >= lo) and (hi is None or b[i]["t"] < hi)]
    rs = [r for r in rs if r is not None]
    return statistics.mean(rs) + 2 * COST if rs else 0.0  # baseline is gross: buy-and-hold pays no round trip per bar


def analyze(sym, b):
    sig = signals(b)
    base = baseline(b)
    b1, b2 = baseline(b, hi=SPLIT), baseline(b, lo=SPLIT)
    res = {"bars": len(b), "base": base, "entries": {}}
    for e in ENTRIES:
        tr = trades(b, sig[e])
        s = summarize(tr, base)
        h1 = summarize([x for x in tr if x[0] < SPLIT], b1)
        h2 = summarize([x for x in tr if x[0] >= SPLIT], b2)
        works = bool(s and h1 and h2 and s["t"] > 2 and h1["edge"] > 0 and h2["edge"] > 0)
        res["entries"][e] = {"all": s, "h1": h1, "h2": h2, "works": works}
    return res


# ----------------------------------------------------------------------------- report

def pct(x, d=2):
    return "-" if x is None else f"{x * 100:+.{d}f}%"


def write_report(results, log):
    L = ["# Hourly mean-reversion screen (TrendSpider META idea, tested)", "",
         f"Generated {date.today()} by `hourly_reversion_backtest.py`. 1-hour regular-session bars, "
         f"{START} to today. Long only, signal on a bar's close, fill at the next bar's open, exit at the "
         f"close of the {HOLD}th bar (~2 sessions, so every trade holds overnight). One position per symbol. "
         f"Costs {COST * 1e4:.0f} bp per side.", "",
         "**Edge** = mean trade return minus the mean 12-bar return from ANY bar (the 'random entry' baseline). "
         "**Works** = t-stat > 2 over the full period AND positive edge in both 2021-23 and 2024-26.", "",
         "Read with the multiple-testing caveat: ~225 tests, so ~10 can pass t > 2 by luck before the halves check.", ""]

    # META detail
    if "META" in results:
        r = results["META"]
        L += ["## META detail", "", f"{r['bars']} bars. Baseline 12-bar return {pct(r['base'], 3)}.", "",
              "| Entry | Trades | Avg trade | Edge vs random | Win % | Profit factor | t | Edge 21-23 | Edge 24-26 | Works |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for e in ENTRIES:
            x = r["entries"][e]
            s = x["all"]
            if not s:
                L.append(f"| {e} | 0 | | | | | | | | |")
                continue
            L.append(f"| {e} | {s['n']} | {pct(s['mean'], 3)} | {pct(s['edge'], 3)} | {s['win'] * 100:.0f}% | "
                     f"{s['pf']:.2f} | {s['t']:.2f} | {pct((x['h1'] or {}).get('edge'), 3)} | "
                     f"{pct((x['h2'] or {}).get('edge'), 3)} | {'YES' if x['works'] else 'no'} |")
        L.append("")

    # Entry-level pooled view
    L += ["## Each entry across all names", "",
          "| Entry | Names where it works | Avg edge (all names) | Names with positive edge | Pooled trades |",
          "|---|---|---|---|---|"]
    for e in ENTRIES:
        rows = [(s, r["entries"][e]) for s, r in results.items() if r["entries"][e]["all"]]
        works = [s for s, x in rows if x["works"]]
        edges = [x["all"]["edge"] for _, x in rows]
        pos = sum(1 for v in edges if v > 0)
        n = sum(x["all"]["n"] for _, x in rows)
        L.append(f"| {e} | {len(works)}/{len(rows)}: {', '.join(works) or '-'} | "
                 f"{pct(statistics.mean(edges) if edges else None, 3)} | {pos}/{len(rows)} | {n} |")
    L.append("")

    # Name ranking
    L += ["## Names ranked by best robust entry", "",
          "| Symbol | Entries that work | Best entry | Trades | Edge | Win % | PF | t | Edge 21-23 | Edge 24-26 |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    ranked = []
    for s, r in results.items():
        cands = [(e, x) for e, x in r["entries"].items() if x["all"]]
        if not cands:
            continue
        best = max(cands, key=lambda ex: (ex[1]["works"], ex[1]["all"]["t"]))
        nw = sum(1 for _, x in cands if x["works"])
        ranked.append((nw, best[1]["all"]["t"], s, best))
    for nw, _, s, (e, x) in sorted(ranked, reverse=True):
        a = x["all"]
        L.append(f"| {s} | {nw} | {e} | {a['n']} | {pct(a['edge'], 3)} | {a['win'] * 100:.0f}% | {a['pf']:.2f} | "
                 f"{a['t']:.2f} | {pct((x['h1'] or {}).get('edge'), 3)} | {pct((x['h2'] or {}).get('edge'), 3)} |")
    L.append("")
    if log:
        L += ["## Fetch log", ""] + [f"- {x}" for x in log[:40]]
    (HERE / "hourly_reversion_results.md").write_text("\n".join(L) + "\n")


def main():
    key = os.environ.get("FMP_API_KEY", "")
    if not key:
        raise SystemExit("FMP_API_KEY not set")
    log, results, raw = [], {}, {}
    for sym in UNIVERSE:
        b = fetch_hourly(sym, key, log)
        if len(b) < 1000:
            log.append(f"{sym}: only {len(b)} bars, skipped")
            continue
        raw[sym] = b
        results[sym] = analyze(sym, b)
        print(sym, len(b), "bars", flush=True)
    (HERE / "hourly_reversion_results.json").write_text(json.dumps(results, indent=1))
    write_report(results, log)


if __name__ == "__main__":
    main()
