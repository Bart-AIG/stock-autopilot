"""Does the chart-setup score predict returns? (Ryan, live turn 2026-10-14: "do all three",
the third being a backtest of setups.py before anyone trusts its ranking.)

Universe: S&P 100 + Nasdaq-100 constituents as of end-2018 (backtest.py's lists), so the
names carry no hindsight about 2019-2026 winners. Every SAMPLE_STEP sessions from 2019 on,
each name is scored by the PRODUCTION function setups.score_arrays() on the 300 sessions
up to and including that day (full daily OHLC + volume from FMP; nothing after the day is
visible). Forward returns are measured from that day's close over 21 / 63 / 126 sessions,
both raw and in EXCESS of SPY over the same window.

The question that matters is the one the Quality @ 200-day list asks, so the headline
sample is IN THE BAND: price between -8% and +5% of its 200-day SMA (quality_watch's band).
The business-quality screen itself can't be applied point in time (the scanner's
fundamentals have no history), so this tests the CHART score on large caps near their
200-day, not the exact quality list.

Measured:
  1. Return by label (WEAK / NEUTRAL / CONSTRUCTIVE / STRONG) and by score quintile.
  2. Each component on its own: excess return with vs without it.
  3. RANKING, which is what Ryan asked for: on each date, the in-band names ranked by
     score; rank correlation (Spearman IC) with the next 63-session excess return, and
     the top-3 names' excess over the average in-band name.
  4. Stability: the same tables for 2019-2022 and 2023-2026.

Honest limits, printed with the results: samples overlap (a 63-session return sampled
every few days counts the same move many times), so the non-overlapping IC is the one to
trust; a few 2018 names were acquired since and drop out if FMP lacks their history.

Network: FMP (key in FMP_API_KEY). Writes setups_results.md.
"""
from __future__ import annotations

import json
import math
import os
import statistics
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path

import setups
from backtest import BASE, NDX100_2018, SP100_2018, _get

HERE = Path(__file__).resolve().parent
OUT = HERE / "setups_results.md"
CACHE = HERE / "logs" / "setups_ohlc_cache.json"
START = "2018-01-01"
FIRST_SAMPLE = "2019-01-01"
SAMPLE_STEP = 2
WINDOW = 300
HORIZONS = (21, 63, 126)
BAND = (-0.08, 0.05)
LABELS = ("WEAK", "NEUTRAL", "CONSTRUCTIVE", "STRONG")


def fetch(sym: str, key: str):
    data = _get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={START}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return None
    rows = sorted((r for r in data if r.get("close") and r.get("high") and r.get("low")),
                  key=lambda r: r["date"])
    return [(r["date"][:10], float(r["high"]), float(r["low"]), float(r["close"]),
             float(r.get("volume") or 0)) for r in rows]


def load_data(key: str, log: list[str]) -> dict:
    if CACHE.exists():
        try:
            blob = json.loads(CACHE.read_text())
            if blob.get("date") == str(date.today()):
                return blob["data"]
        except ValueError:
            pass
    syms = list(dict.fromkeys(SP100_2018 + NDX100_2018 + ["SPY"]))
    data = {}
    for i, s in enumerate(syms, 1):
        rows = fetch(s, key)
        if rows and len(rows) > WINDOW + 130:
            data[s] = rows
        else:
            log.append(f"{s}: no usable history ({'none' if not rows else len(rows)} rows), dropped")
        time.sleep(0.15)
        if i % 25 == 0:
            print(f"  fetched {i}/{len(syms)}", flush=True)
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps({"date": str(date.today()), "data": data}))
    return data


def spearman(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 5:
        return None

    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx = math.sqrt(sum((a - mx) ** 2 for a in rx))
    syy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return sxy / (sxx * syy) if sxx and syy else None


def samples(data: dict) -> list[dict]:
    spy = {d: c for d, _, _, c, _ in data["SPY"]}
    out = []
    for n_sym, (sym, rows) in enumerate(sorted(data.items()), 1):
        if sym == "SPY":
            continue
        D = [r[0] for r in rows]
        H = [r[1] for r in rows]
        L = [r[2] for r in rows]
        C = [r[3] for r in rows]
        V = [r[4] for r in rows]
        for t in range(WINDOW - 1, len(rows), SAMPLE_STEP):
            if D[t] < FIRST_SAMPLE or D[t] not in spy:
                continue
            sma200 = sum(C[t - 199:t + 1]) / 200
            dist = C[t] / sma200 - 1
            a = t - WINDOW + 1
            s = setups.score_arrays(C[a:t + 1], H[a:t + 1], L[a:t + 1], V[a:t + 1])
            if not s:
                continue
            row = {"sym": sym, "date": D[t], "score": s["score"], "label": s["label"],
                   "pre": s["pre"], "feat": [k for k, v in s["feat"].items() if v],
                   "flags": s["flags"], "dist": dist, "in_band": BAND[0] <= dist <= BAND[1]}
            for h in HORIZONS:
                if t + h < len(rows) and D[t + h] in spy:
                    r = C[t + h] / C[t] - 1
                    row[f"r{h}"] = r
                    row[f"x{h}"] = r - (spy[D[t + h]] / spy[D[t]] - 1)
            out.append(row)
        if n_sym % 20 == 0:
            print(f"  scored {n_sym}/{len(data) - 1} names ({len(out)} samples)", flush=True)
    return out


def pct(v):
    return "—" if v is None else f"{v * 100:+.2f}%"


def summarize(rows: list[dict], h: int) -> dict:
    xs = [r[f"x{h}"] for r in rows if f"x{h}" in r]
    if not xs:
        return {"n": 0}
    return {"n": len(xs), "mean": statistics.mean(xs), "median": statistics.median(xs),
            "win": sum(1 for x in xs if x > 0) / len(xs)}


def bucket_table(rows: list[dict], key, buckets, title: str) -> list[str]:
    lines = [f"### {title}", "",
             "| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |",
             "|---|---|---|---|---|---|---|"]
    for b in buckets:
        sub = [r for r in rows if key(r) == b]
        s21, s63, s126 = (summarize(sub, h) for h in HORIZONS)
        if not s63["n"]:
            lines.append(f"| {b} | 0 | — | — | — | — | — |")
            continue
        lines.append(f"| {b} | {s63['n']} | {pct(s21.get('mean'))} | {pct(s63['mean'])} | "
                     f"{pct(s63['median'])} | {s63['win']:.1%} | {pct(s126.get('mean'))} |")
    s63 = summarize(rows, 63)
    if s63["n"]:
        lines.append(f"| **All** | {s63['n']} | {pct(summarize(rows, 21).get('mean'))} | "
                     f"{pct(s63['mean'])} | {pct(s63['median'])} | {s63['win']:.1%} | "
                     f"{pct(summarize(rows, 126).get('mean'))} |")
    return lines + [""]


def ranking(rows: list[dict], h: int = 63, key: str = "score") -> dict:
    by_date = defaultdict(list)
    for r in rows:
        if f"x{h}" in r:
            by_date[r["date"]].append(r)
    dates = sorted(d for d, v in by_date.items() if len(v) >= 6)
    ics, spreads = [], []
    for d in dates:
        v = by_date[d]
        ic = spearman([r[key] for r in v], [r[f"x{h}"] for r in v])
        if ic is not None:
            ics.append((d, ic))
        top = sorted(v, key=lambda r: -r[key])[:3]
        spreads.append((d, statistics.mean(r[f"x{h}"] for r in top)
                        - statistics.mean(r[f"x{h}"] for r in v)))
    # non-overlapping: dates at least h sessions apart (sampled every SAMPLE_STEP sessions)
    gap = math.ceil(h / SAMPLE_STEP)
    non_ic = [ic for i, (_, ic) in enumerate(ics) if i % gap == 0]
    non_sp = [sp for i, (_, sp) in enumerate(spreads) if i % gap == 0]

    def tstat(v):
        if len(v) < 3:
            return None
        sd = statistics.stdev(v)
        return statistics.mean(v) / (sd / math.sqrt(len(v))) if sd else None
    return {"dates": len(dates), "ic_mean": statistics.mean(i for _, i in ics) if ics else None,
            "ic_pos": sum(1 for _, i in ics if i > 0) / len(ics) if ics else None,
            "non_n": len(non_ic), "non_ic": statistics.mean(non_ic) if non_ic else None,
            "non_ic_t": tstat(non_ic),
            "top3": statistics.mean(s for _, s in spreads) if spreads else None,
            "top3_win": sum(1 for _, s in spreads if s > 0) / len(spreads) if spreads else None,
            "non_top3": statistics.mean(non_sp) if non_sp else None, "non_top3_t": tstat(non_sp)}


def rank_lines(name: str, rk: dict) -> str:
    f = lambda v: "—" if v is None else f"{v:+.3f}"
    t = lambda v: "—" if v is None else f"{v:.1f}"
    share = lambda v: "—" if v is None else f"{v:.0%}"
    return (f"| {name} | {rk['dates']} | {f(rk['ic_mean'])} | "
            f"{share(rk['ic_pos'])} | {rk['non_n']} | "
            f"{f(rk['non_ic'])} | {t(rk['non_ic_t'])} | {pct(rk['top3'])} | "
            f"{share(rk['top3_win'])} | "
            f"{pct(rk['non_top3'])} | {t(rk['non_top3_t'])} |")


def quintile(rows: list[dict], key: str = "score"):
    sc = sorted(r[key] for r in rows)
    cuts = [sc[int(len(sc) * q / 5)] for q in range(1, 5)] if sc else []

    def q(r):
        return f"Q{1 + sum(1 for c in cuts if r[key] > c)}"
    return q


def main() -> None:
    key = os.environ.get("FMP_API_KEY")
    if not key:
        sys.exit("FMP_API_KEY not set")
    log: list[str] = []
    t0 = time.time()
    data = load_data(key, log)
    if "SPY" not in data:
        sys.exit("no SPY history; cannot measure excess returns")
    print(f"{len(data)} symbols loaded; scoring...", flush=True)
    rows = samples(data)
    band = [r for r in rows if r["in_band"]]
    print(f"{len(rows)} samples, {len(band)} in the 200-day band ({time.time() - t0:.0f}s)")

    L = ["# Chart-setup score backtest (setups.py)", "",
         f"Run {time.strftime('%Y-%m-%d %H:%MZ', time.gmtime())}. {len(data) - 1} large caps "
         f"(S&P 100 + Nasdaq-100 as of end-2018), scored every {SAMPLE_STEP} sessions from "
         f"{FIRST_SAMPLE}, by the production scorer on daily OHLC + volume. Returns are in EXCESS "
         "of SPY over the same window. **In band** = price -8% to +5% vs its 200-day SMA, the "
         "Quality @ 200-day list's band.", "",
         f"Samples: {len(rows)} total, {len(band)} in band.", ""]

    L += ["## 1. Does ranking by score pick better names? (the question asked)", "",
          "On each date the in-band names are ranked by setup score. **IC** = rank correlation of "
          "score with the next 63-session excess return (0 = no information; +0.05 is a useful "
          "ranking signal in practice). **Top 3** = the 3 highest-scored names' excess over the "
          "average in-band name that day. Non-overlapping = dates 63+ sessions apart, so each "
          "move counts once: trust that column, and its t-stat (|t| >= 2 is the usual bar).", "",
          "| Sample | Dates | IC mean | IC > 0 | Non-overlap dates | IC (non-overlap) | t | "
          "Top 3 vs avg | Top 3 wins | Top 3 (non-overlap) | t |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    early = [r for r in band if r["date"] < "2023-01-01"]
    late = [r for r in band if r["date"] >= "2023-01-01"]
    for name, sub in (("In band, 2019-2026", band), ("In band, 2019-2022", early),
                      ("In band, 2023-2026", late), ("All samples (any distance)", rows)):
        L.append(rank_lines(name, ranking(sub)))
    L.append("")

    L += ["## 2. Return by label and by score quintile", ""]
    L += bucket_table(band, lambda r: r["label"], LABELS, "In band: by label")
    L += bucket_table(band, quintile(band), ["Q1", "Q2", "Q3", "Q4", "Q5"],
                      "In band: by score quintile (Q5 = highest scores)")
    L += bucket_table(early, lambda r: r["label"], LABELS, "In band, 2019-2022: by label")
    L += bucket_table(late, lambda r: r["label"], LABELS, "In band, 2023-2026: by label")
    L += bucket_table(rows, lambda r: r["label"], LABELS, "All samples: by label")

    L += ["## 3. Each component on its own (in band, 63-session excess)", "",
          "| Component | n with | Excess with | n without | Excess without | Difference | "
          "Beat SPY with |", "|---|---|---|---|---|---|---|"]
    flags = sorted({f for r in band for f in r["flags"]})
    for fl in flags:
        w = [r["x63"] for r in band if "x63" in r and fl in r["flags"]]
        wo = [r["x63"] for r in band if "x63" in r and fl not in r["flags"]]
        if len(w) < 20 or not wo:
            continue
        mw, mo = statistics.mean(w), statistics.mean(wo)
        L.append(f"| {fl} | {len(w)} | {pct(mw)} | {len(wo)} | {pct(mo)} | {pct(mw - mo)} | "
                 f"{sum(1 for x in w if x > 0) / len(w):.1%} |")
    L.append("")

    # ---------------- PRE-BREAKOUT score: train 2019-2022, untouched test 2023-2026
    def feat_table(sub, title):
        out = [f"### {title}", "", "| Trait | n with | 63d excess with | without | Difference | Beat SPY with |",
               "|---|---|---|---|---|---|"]
        diffs = {}
        for fl in sorted(setups.PRE_WEIGHTS.keys() | {f for r in sub for f in r["feat"]}):
            w = [r["x63"] for r in sub if "x63" in r and fl in r["feat"]]
            wo = [r["x63"] for r in sub if "x63" in r and fl not in r["feat"]]
            if len(w) < 20 or not wo:
                continue
            d = statistics.mean(w) - statistics.mean(wo)
            diffs[fl] = d
            out.append(f"| {fl} | {len(w)} | {pct(statistics.mean(w))} | {pct(statistics.mean(wo))} | "
                       f"{pct(d)} | {sum(1 for x in w if x > 0) / len(w):.1%} |")
        return out + [""], diffs

    ft_train, train_diffs = feat_table(early, "Train 2019-2022 (in band)")
    ft_test, _ = feat_table(late, "Test 2023-2026 (in band, never used to build anything)")
    fitted = {k: (1 if d > 0.005 else -1) for k, d in train_diffs.items() if abs(d) > 0.005}
    for r in rows:
        r["pre_fit"] = setups.prebreakout(dict.fromkeys(r["feat"], True), fitted) if fitted else 0
    L += ["## 4. PRE-BREAKOUT score (Ryan, 2026-10-14: rank the names BEFORE the breakout)", "",
          "Two versions, both judged on 2023-2026, which neither was built from:",
          "- **PRE (written in advance):** +1 each for pattern forming, RSI divergence, fresh 60-day "
          "low, RSI(14) < 40, below the 20-day, >= 8% off the 60-day high, volume drying up; -1 for "
          "a pattern already broken out (setups.PRE_WEIGHTS).",
          "- **FIT (2019-2022 only):** +1 for every trait that beat by > 0.5% in 2019-2022, -1 for "
          f"every trait that lagged by > 0.5%. Chosen weights: `{fitted}`.", "",
          "| Score | Sample | Dates | IC mean | IC > 0 | Non-overlap dates | IC (non-overlap) | t | "
          "Top 3 vs avg | Top 3 wins | Top 3 (non-overlap) | t |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for key, nm in (("pre", "PRE"), ("pre_fit", "FIT"), ("score", "Old setup score")):
        for pname, sub in (("Train 2019-22", early), ("**Test 2023-26**", late), ("All in band", band)):
            L.append(rank_lines(f"{nm} | {pname}", ranking(sub, key=key)).replace("| ", "| ", 1))
    L.append("")
    L += bucket_table(late, quintile(late, "pre"), ["Q1", "Q2", "Q3", "Q4", "Q5"],
                      "PRE score, TEST 2023-26 in band, by quintile (Q5 = most pulled back / coiled)")
    L += bucket_table(early, quintile(early, "pre"), ["Q1", "Q2", "Q3", "Q4", "Q5"],
                      "PRE score, TRAIN 2019-22 in band, by quintile")
    L += ["### Each trait, by period", ""] + ft_train + ft_test

    L += ["## Honest limits", "",
          "- Samples overlap: a 63-session return sampled every "
          f"{SAMPLE_STEP} sessions counts the same move ~{63 // SAMPLE_STEP} times. The "
          "non-overlapping IC and top-3 columns, with their t-stats, are the evidence; the rest "
          "is description.",
          "- The business-quality screen (margins, growth, ROE) can't be applied point in time, "
          "so this is the chart score on large caps near their 200-day, not the exact list.",
          "- Constituents are as of end-2018 (no hindsight), but names acquired since drop out "
          "if FMP lacks their history: a small survivorship bias toward names that lasted.",
          "- No costs: these are signal tests, not a strategy."]
    if log:
        L += ["", "## Data notes", ""] + [f"- {x}" for x in log]
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {OUT} in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
