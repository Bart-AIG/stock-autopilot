"""Backtest for bottom_watch.py. Run: python3 bottom_backtest.py

Reads data/bottom/*.csv (daily QQQ, SPY, VIX, HYG, IEF, RSP; Robinhood history pulled
2026-11-20) and data/bottom/macro/*.csv (monthly series). For every day inside every QQQ / SPY
selloff since 1999 it asks "has the lowest close of this selloff already printed?", ranks each
candidate variable by how well it separates yes from no, fits a small logistic model, and
checks it on selloffs it was not fitted on (every selloff that peaked in the same calendar
year is held out together).

Writes bottom_model.json (what the scheduled job loads) and bottom_results.md (the evidence).
Needs numpy. The scheduled job does not.

Monthly series, each used only once it would have been published:
  CAPE.csv          Shiller P/E on the first of each month (multpl.com)
  M2.csv            M2 money supply, monthly (Federal Reserve), used with a 2-month lag
  MARGIN_DEBT.csv   FINRA margin debt, monthly, used with a 2-month lag
"""
from __future__ import annotations

import csv
import json
import math
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

import bottom_watch as bw

HERE = Path(__file__).parent
DATA = HERE / "data" / "bottom"
MACRO = DATA / "macro"

NAMES = {
    "vix_off": "VIX below its peak of the selloff", "dist200": "Close vs the 200-day average",
    "retr": "Share of the drop retraced", "dist50": "Close vs the 50-day average", "rsi14": "RSI(14)",
    "reb_atr": "Rebound off the low, in daily ranges", "dist20": "Close vs the 20-day average",
    "above200": "Above the 200-day", "above50": "Above the 50-day", "vix_peak_age": "Sessions since the VIX peak",
    "reb": "Rebound off the low, %", "hy20": "Junk bonds vs Treasuries, 20 days", "above20": "Above the 20-day",
    "vix_vs20": "VIX vs its 20-day average", "updn10": "Up-day vs down-day volume, 10 days",
    "ddclose": "Drawdown from the high", "days": "Sessions since the low", "rsi2": "RSI(2)", "vix": "VIX level",
    "hy5": "Junk bonds vs Treasuries, 5 days", "legs": "Failed rebounds so far", "sess_pk_low": "Sessions from the high to the low",
    "ddlow": "Depth of the low", "speed": "Speed of the decline", "giveback": "Rebound given back",
    "lowday_volr": "Volume on the low day", "climax5": "Peak volume into the low", "lowday_loc": "Close position on the low day",
    "ftd": "Follow-through day", "ew_rel20": "Average stock vs the index, 20 days", "rsi_div": "RSI divergence at the low",
    "vix_div": "VIX divergence at the low", "slope200": "Direction of the 200-day", "climax_age": "Sessions since peak volume",
    "vol_div": "Low-day volume vs peak volume", "maxreb": "Best rebound so far", "vix_peak": "VIX peak of the selloff",
    "vix_low": "VIX on the low day", "rsi_low": "RSI on the low day", "climax_ep": "Peak volume of the selloff",
    "vix_prevleg": "VIX vs the previous leg's low", "sess_pk": "Sessions since the high", "above5": "Above the 5-day",
    "above10": "Above the 10-day",
    "bb_z": "Bollinger: position inside the bands", "bb_z_low": "Bollinger: position on the low day",
    "bb_width": "Bollinger: band width", "bb_width_off": "Bollinger: bands narrower than their widest",
    "bb_out_age": "Bollinger: sessions since a close under the lower band",
    "bb_reentry": "Bollinger: back inside after a close under the lower band",
    "bb_w_bottom": "Bollinger: new low that held inside the band (W bottom)", "bb_zmax": "Bollinger: highest position since the low",
    "cape": "Shiller P/E", "cape_peak": "Shiller P/E at the high", "cape_rel10": "Shiller P/E vs its 10-year average",
    "m2_yoy": "M2 growth, 12 months", "m2_6m": "M2 growth, 6 months annualized", "spx_m2_rel": "S&P 500 / M2 vs its 5-year average",
    "md_yoy": "Margin debt, 12-month change", "md_3m": "Margin debt, 3-month change",
    "md_dd": "Margin debt below its 3-year high", "md_spx_rel": "Margin debt / S&P 500 vs its 5-year average",
}
ASKED = {   # Ryan, live turn 2026-11-20: Shiller index, money supply, total debt in the market, Bollinger lines
    "Bollinger bands": ["bb_z", "bb_width", "bb_width_off", "bb_out_age", "bb_reentry", "bb_w_bottom", "bb_z_low", "bb_zmax"],
    "Shiller P/E": ["cape", "cape_peak", "cape_rel10"],
    "M2 money supply": ["m2_yoy", "m2_6m", "spx_m2_rel"],
    "Margin debt": ["md_yoy", "md_3m", "md_dd", "md_spx_rel"],
}
SLOW = ("cape", "m2_yoy", "spx_m2_rel", "md_yoy", "md_dd", "md_spx_rel")     # tested against how deep each selloff went
CLIP = {"vix_off": (-0.75, 0.0), "dist200": (-0.40, 0.15), "rsi14": (0.0, 100.0), "bb_z": (-3.5, 3.5), "bb_zmax": (-3.5, 3.5),
        "bb_z_low": (-3.5, 3.5), "bb_width_off": (-0.9, 0.0), "cape": (10, 50), "cape_peak": (10, 50), "cape_rel10": (-0.6, 0.8),
        "m2_yoy": (-0.06, 0.28), "m2_6m": (-0.08, 0.40), "spx_m2_rel": (-0.5, 0.6), "md_yoy": (-0.5, 0.8), "md_3m": (-0.3, 0.3),
        "md_dd": (-0.5, 0.0), "md_spx_rel": (-0.5, 0.6)}
FEATS = ["vix_off", "dist200", "rsi14"]
FALLBACK = ["dist200", "rsi14"]            # when no VIX reading is available
VARIANTS = {
    "VIX off its peak only": ["vix_off"],
    "+ close vs the 200-day": ["vix_off", "dist200"],
    "+ RSI(14)  [chosen]": FEATS,
    "+ share of the drop retraced": FEATS + ["retr"],
    "+ failed rebounds so far": FEATS + ["legs"],
    "+ direction of the 200-day": FEATS + ["slope200"],
    "+ junk bonds vs Treasuries": FEATS + ["hy20"],
    "11 variables": FEATS + ["retr", "legs", "reb_atr", "giveback", "days", "speed", "ddclose", "dist50"],
    "No VIX: 200-day + RSI(14)": FALLBACK,
}
CHECKS = [("VIX 20% under its peak close", "vix_off", "<=", -0.20), ("VIX 40% under its peak close", "vix_off", "<=", -0.40),
          ("Close above the 20-day average", "above20", ">=", 1), ("Close above the 50-day average", "above50", ">=", 1),
          ("RSI(14) at 50 or more", "rsi14", ">=", 50), ("Half of the drop retraced", "retr", ">=", 0.5),
          ("Close above the 200-day average", "above200", ">=", 1), ("10 sessions without a new closing low", "days", ">=", 10)]


def load(sym):
    R = list(csv.DictReader(open(DATA / f"{sym}.csv")))
    return {"d": [r["date"] for r in R], "o": [float(r["open"]) for r in R], "h": [float(r["high"]) for r in R],
            "l": [float(r["low"]) for r in R], "c": [float(r["close"]) for r in R],
            "v": [float(r["volume"]) if r.get("volume") else None for r in R]}


def closes(sym):
    return {r["date"]: float(r["close"]) for r in csv.DictReader(open(DATA / f"{sym}.csv"))}


def monthly(name):
    """{'YYYY-MM': value} from data/bottom/macro/<name>, or None when the file is not there."""
    p = MACRO / name
    if not p.exists():
        return None
    return {r["date"][:7]: float(r["value"]) for r in csv.DictReader(open(p))}


def ym(m, k):
    t = int(m[:4]) * 12 + int(m[5:7]) - 1 + k
    return f"{t // 12}-{t % 12 + 1:02d}"


def add_macro(rows, spy):
    """Slow variables, each from the latest month that had been published on that day."""
    cape, m2, md = monthly("CAPE.csv"), monthly("M2.csv"), monthly("MARGIN_DEBT.csv")
    first = {}
    for d in sorted(spy):
        first.setdefault(d[:7], spy[d])           # SPY close on the first session of each month

    def rel(series, m, now):                      # (SPY / series) now against its average over the prior 60 months
        hist = [first[x] / series[x] for x in (ym(m, -k) for k in range(1, 61)) if x in first and x in series]
        return (now / (sum(hist) / len(hist)) - 1) if len(hist) >= 48 else None

    def at(d):
        m, f = d[:7], {}
        if cape and m in cape and m in first and d in spy:
            f["cape"] = cape[m] * spy[d] / first[m]
            past = [cape[x] for x in (ym(m, -k) for k in range(1, 121)) if x in cape]
            f["cape_rel10"] = f["cape"] / (sum(past) / len(past)) - 1 if len(past) == 120 else None
        if m2:
            a, b, c6 = m2.get(ym(m, -2)), m2.get(ym(m, -14)), m2.get(ym(m, -8))
            if a and b and c6 and d in spy:
                f["m2_yoy"], f["m2_6m"] = a / b - 1, (a / c6) ** 2 - 1
                f["spx_m2_rel"] = rel(m2, ym(m, -2), spy[d] / a)
        if md:
            a, b, c3 = md.get(ym(m, -2)), md.get(ym(m, -14)), md.get(ym(m, -5))
            hi = [md[x] for x in (ym(m, -k) for k in range(2, 39)) if x in md]
            if a and b and c3 and len(hi) >= 24 and d in spy:
                f["md_yoy"], f["md_3m"], f["md_dd"] = a / b - 1, a / c3 - 1, a / max(hi) - 1
                hist = [md[x] / first[x] for x in (ym(m, -2 - k) for k in range(1, 61)) if x in md and x in first]
                f["md_spx_rel"] = ((a / spy[d]) / (sum(hist) / len(hist)) - 1) if len(hist) >= 48 else None
        return f

    for r in rows:
        r.update(at(r["date"]))
        r["cape_peak"] = at(r["peak_date"]).get("cape")
    return {"cape": bool(cape), "m2": bool(m2), "md": bool(md), "at": at}


def auc(x, y):
    x, y = np.asarray(x, float), np.asarray(y, int)
    if y.sum() in (0, len(y)):
        return float("nan")
    order = x.argsort(kind="mergesort")
    r = np.empty(len(x))
    r[order] = np.arange(1, len(x) + 1)
    xs, i = x[order], 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[j + 1] == xs[i]:
            j += 1
        if j > i:
            r[order[i:j + 1]] = (i + j + 2) / 2
        i = j + 1
    n1 = y.sum()
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * (len(y) - n1)))


def val(f, r):
    x = r[f]
    if f in CLIP:
        x = max(CLIP[f][0], min(CLIP[f][1], x))
    return float(x)


def fit(X, y, w, l2=1.0):
    n, k = X.shape
    A = np.hstack([np.ones((n, 1)), X])
    b = np.zeros(k + 1)
    R = np.eye(k + 1) * l2
    R[0, 0] = 0
    for _ in range(80):
        p = 1 / (1 + np.exp(-(A @ b)))
        step = np.linalg.solve((A * (w * p * (1 - p) + 1e-9)[:, None]).T @ A + R, A.T @ (w * (y - p)) - R @ b)
        b += step
        if np.abs(step).max() < 1e-9:
            break
    return b


def weights(rows):
    cnt = Counter((r["sym"], r["ep"]) for r in rows)
    w = np.array([1 / math.sqrt(cnt[(r["sym"], r["ep"])]) for r in rows])     # a 700-day bear must not outvote 40 corrections
    return w / w.mean()


def design(feats, rows):
    rows = [r for r in rows if all(r.get(f) is not None for f in feats)]
    X = np.array([[val(f, r) for f in feats] for r in rows])
    return rows, X, np.array([r["y"] for r in rows], float), weights(rows)


def oos(feats, rows):
    """Out-of-sample predictions: hold out every selloff that peaked in the same year."""
    rows, X, y, w = design(feats, rows)
    grp = np.array([r["peak_date"][:4] for r in rows])
    pred = np.zeros(len(rows))
    for g in sorted(set(grp)):
        te = grp == g
        mu, sd = X[~te].mean(0), X[~te].std(0) + 1e-9
        b = fit((X[~te] - mu) / sd, y[~te], w[~te])
        pred[te] = 1 / (1 + np.exp(-(b[0] + ((X[te] - mu) / sd) @ b[1:])))
    base = np.average(y, weights=w)
    skill = 1 - np.average((pred - y) ** 2, weights=w) / np.average((base - y) ** 2, weights=w)
    return rows, pred, y, w, {"n": len(rows), "auc": auc(pred, y), "skill": float(skill)}


def isotonic(pred, y, w):
    """Weighted pool-adjacent-violators, read off on a fixed grid. Returns [[raw, calibrated], ...]."""
    order = np.argsort(pred)
    out = []
    for i in order:                        # block = [sum(y*w), sum(w), sum(raw*w)]
        out.append([float(y[i]) * float(w[i]), float(w[i]), float(pred[i]) * float(w[i])])
        while len(out) > 1 and out[-2][0] / out[-2][1] > out[-1][0] / out[-1][1]:
            a = out.pop()
            out[-1] = [out[-1][0] + a[0], out[-1][1] + a[1], out[-1][2] + a[2]]
    xs, ys = np.array([b[2] / b[1] for b in out]), np.array([b[0] / b[1] for b in out])
    grid = [0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98]
    knots = [[g, float(np.clip(np.interp(g, xs, ys), 0.03, 0.95))] for g in grid]
    for i in range(1, len(knots)):
        knots[i][1] = max(knots[i][1], knots[i - 1][1])
    return [[k[0], round(k[1], 3)] for k in knots]


def calibrate(p, knots):
    return float(np.interp(p, [k[0] for k in knots], [k[1] for k in knots]))


def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def score(f, rows):
    sub = [r for r in rows if r.get(f) is not None]
    if len(sub) < 200:
        return None
    a = auc([r[f] for r in sub], [r["y"] for r in sub])
    d0 = [r for r in sub if r["days"] == 0]
    a0 = auc([r[f] for r in d0], [r["y"] for r in d0]) if len(d0) > 50 else float("nan")
    return a, a0, len(sub)


def main():
    vix, hyg, ief, rsp, spyc = closes("VIX"), closes("HYG"), closes("IEF"), closes("RSP"), closes("SPY")
    ALL, OPEN, EPS, last_bar = [], {}, [], ""
    for s in ("QQQ", "SPY"):
        B = load(s)
        last_bar = max(last_bar, B["d"][-1])
        rows, eps = bw.scan(s, B, vix, hyg, ief, rsp, spyc)
        ALL += [r for r in rows if r["y"] is not None]
        if eps and eps[-1]["end_i"] is None:
            OPEN[s] = [r for r in rows if r["ep"] == eps[-1]["k"]]
        EPS += [{"sym": s, "peak_date": B["d"][e["peak_i"]], "depth": e["runlow"] / e["peak"] - 1,
                 "sess": e["low_i"] - e["peak_i"]} for e in eps if e["end_i"] is not None]
    have = add_macro(ALL, spyc)
    OPEN_PEAK = min((R[0]["peak_date"] for R in OPEN.values()), default=None)
    for e in EPS:
        e.update(have["at"](e["peak_date"]))
    VIXROWS = [r for r in ALL if r.get("vix_off") is not None]
    n_eps = len({(r["sym"], r["ep"]) for r in ALL})
    W = dict(zip(map(id, ALL), weights(ALL)))
    L = ["# Bottom watch: which variables say the low is in", "",
         f"Data through {last_bar}. Re-run with `python3 bottom_backtest.py`.", "",
         f"- **Sample:** {len(ALL):,} days inside {n_eps} finished QQQ and SPY selloffs, 1999-09 to 2026, on closing prices. "
         "A selloff starts when the close is 10% (QQQ) or 8% (SPY) under its 1-year closing high and ends when the close is back within 3% of it. "
         f"VIX history starts 2002-05, so models that use it are fitted on {len(VIXROWS):,} days.",
         "- **Question on each day:** has the lowest close of this selloff already printed?",
         "- **Score:** 0.50 means the variable is useless and 1.00 means it separates the two perfectly "
         "(area under the ROC curve). \"On the low day\" is the same score using only days that made a new closing low, "
         "which is the hardest moment to call.", ""]

    # ---- every variable on its own
    rank = [(f,) + sc for f in NAMES for sc in [score(f, ALL)] if sc]
    rank.sort(key=lambda t: -abs(t[1] - 0.5))
    L += ["## Each variable on its own", "", "| Variable | Score | Low more likely in when it is | On the low day | Days |", "|---|---|---|---|---|"]
    for f, a, a0, n in rank:
        L.append(f"| {NAMES[f]} | {max(a, 1 - a):.2f} | {'higher' if a >= 0.5 else 'lower'} | "
                 f"{'n/a' if a0 != a0 else f'{max(a0, 1 - a0):.2f}'} | {n:,} |")
    d0 = [r for r in ALL if r["days"] == 0]
    w0 = np.array([W[id(r)] for r in d0])
    L += ["", f"A day that makes a new closing low was the final low on {np.mean([r['y'] for r in d0]) * 100:.0f}% of such days, or "
          f"{np.average([r['y'] for r in d0], weights=w0) * 100:.0f}% when every selloff counts equally (long bear markets have many new-low days). "
          "Volume on the low day, a close off the low, follow-through days and the equal-weight index all score near 0.50: "
          "they did not separate final lows from the rest.", ""]

    # ---- combinations
    res = {name: oos(fs, [r for r in VIXROWS if all(r.get(f) is not None for f in fs)])[4] for name, fs in VARIANTS.items()}
    chosen = res["+ RSI(14)  [chosen]"]
    L += ["## Combining them (tested on selloffs the model had not seen)", "",
          "| Model | Score | Better than always quoting the average |", "|---|---|---|"]
    for name, m in res.items():
        L.append(f"| {name} | {m['auc']:.3f} | {m['skill'] * 100:.1f}% |")
    better = [n for n, m in res.items() if n.startswith("+ ") and len(VARIANTS[n]) > len(FEATS) and m["skill"] > chosen["skill"] + 0.005]
    L += ["", ("Adding a fourth variable did not improve the out-of-sample result, so the model stops at three."
               if not better else "These four-variable versions beat the chosen model by more than half a point: " + ", ".join(better) + "."), ""]

    # ---- the model
    rows, pred, y, w, m = oos(FEATS, VIXROWS)
    knots = isotonic(pred, y, w)
    cal = np.array([calibrate(p, knots) for p in pred])
    _, X, yy, ww = design(FEATS, VIXROWS)
    mu, sd = X.mean(0), X.std(0)
    b = fit((X - mu) / sd, yy, ww)
    _, Xf, yf, wf = design(FALLBACK, ALL)
    muf, sdf = Xf.mean(0), Xf.std(0)
    bf = fit((Xf - muf) / sdf, yf, wf)
    _, predf, yf2, wf2, mf = oos(FALLBACK, ALL)
    knots_f = isotonic(predf, yf2, wf2)
    rel = []
    for a, c in [(0, .25), (.25, .5), (.5, .7), (.7, .85), (.85, 1.01)]:
        k = (cal >= a) & (cal < c)
        rel.append({"lo": a, "hi": min(c, 1.0), "n": int(k.sum()), "actual": round(float(np.average(y[k], weights=w[k])), 3) if k.sum() else None})
    L += ["## The model", "", "Chance the low is in = a logistic blend of three readings, then adjusted so that the "
          "stated chance matches how often it was right out of sample.", "",
          "| Reading | Average in past selloffs | Weight (per standard deviation) |", "|---|---|---|"]
    for f, mm, bb_ in zip(FEATS, mu, b[1:]):
        L.append(f"| {NAMES[f]} | {mm:.3f} | {bb_:+.2f} |")
    L += ["", f"Out of sample: score {m['auc']:.3f}; {m['skill'] * 100:.1f}% better than always quoting the average.", "",
          "| Stated chance | Days | Low really was in |", "|---|---|---|"]
    for r_ in rel:
        L.append(f"| {r_['lo'] * 100:.0f}% to {r_['hi'] * 100:.0f}% | {r_['n']:,} | " + (f"{r_['actual'] * 100:.0f}% |" if r_["n"] else "n/a |"))
    L += ["", "The adjustment was fitted on these same out-of-sample predictions, so this table is slightly flattering.", ""]

    # ---- rebound checkpoints
    checks = []
    L += ["## Rebound checkpoints", "", "How often the low was already in on days when each checkpoint was met, and when it was not "
          "(every selloff counted equally). These are shown in the report; the chance above is the estimate.", "",
          "| Checkpoint | Low in when met | Low in when not met | Share of days met |", "|---|---|---|---|"]
    for label, f, op, x in CHECKS:
        sub = [r for r in ALL if r.get(f) is not None]
        ws, ys = np.array([W[id(r)] for r in sub]), np.array([r["y"] for r in sub])
        met = np.array([(r[f] >= x) if op == ">=" else (r[f] <= x) for r in sub])
        hit, miss = float(np.average(ys[met], weights=ws[met])), float(np.average(ys[~met], weights=ws[~met]))
        checks.append({"label": label, "f": f, "op": op, "x": x, "hit": round(hit, 3), "miss": round(miss, 3)})
        L.append(f"| {label} | {hit * 100:.0f}% | {miss * 100:.0f}% | {met.mean() * 100:.0f}% |")

    # ---- lead time and false alarms
    by = defaultdict(list)
    for r, p in zip(rows, cal):
        by[(r["sym"], r["ep"])].append((r["i"], r["days"], r["y"], p, r["reb"], r["date"], r["ddlow"], r["peak_date"]))
    tab, lead, false, deep = [], {0.5: [], 0.7: []}, {0.5: 0, 0.7: 0}, {0.5: 0, 0.7: 0}
    for k, R in sorted(by.items(), key=lambda t: t[1][0][7]):
        R.sort()
        pre, post = [x for x in R if x[2] == 0], [x for x in R if x[2] == 1]
        if not post:
            continue
        row = [k[0], R[0][7], post[0][5], post[0][6]]
        for th in (0.5, 0.7):
            hit = next((x for x in post if x[3] >= th), None)
            fa = sum(1 for i, x in enumerate(pre) if x[3] >= th and (i == 0 or pre[i - 1][3] < th))
            false[th] += fa
            deep[th] += fa if post[0][6] < -0.25 else 0
            if hit:
                lead[th].append((hit[1], hit[4]))
            row += [hit[1] if hit else None, hit[4] if hit else None, fa]
        tab.append(row)
    L += ["", "## How fast it calls a low, and how often it is fooled", "",
          f"- **Speed:** across {len(tab)} selloffs the reading reached 50% a median of {st.median(x[0] for x in lead[0.5]):.0f} "
          f"sessions after the final low (price {st.median(x[1] for x in lead[0.5]) * 100:.1f}% off the low by then) and 70% after "
          f"{st.median(x[0] for x in lead[0.7]):.0f} sessions ({st.median(x[1] for x in lead[0.7]) * 100:.1f}% off the low).",
          f"- **False alarms:** before the final low the reading crossed 50% {false[0.5]} times and 70% {false[0.7]} times. "
          f"{deep[0.5]} and {deep[0.7]} of those were inside the selloffs that fell more than 25% "
          "(2000-02, 2008, 2020, 2022): bear-market rallies look like bottoms to this model.", "",
          "| Index | High | Final low | Depth | Sessions to 50% | Off the low then | False 50% crossings | Sessions to 70% | Off the low then | False 70% crossings |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    g = lambda v, pct=False: "n/a" if v is None else (f"{v * 100:.1f}%" if pct else f"{v}")
    for t in tab:
        L.append(f"| {t[0]} | {t[1]} | {t[2]} | {t[3] * 100:.1f}% | {g(t[4])} | {g(t[5], True)} | {t[6]} | {g(t[7])} | {g(t[8], True)} | {t[9]} |")

    # ---- the four variables Ryan asked about
    L += ["", "## Bollinger bands, Shiller P/E, M2 and margin debt", "",
          "Ryan asked on 2026-11-20 whether these had been tested. They had not; this section is the test. "
          "\"Added to the model\" is the out-of-sample result with the variable as a fourth input "
          f"(the three-variable model scores {chosen['skill'] * 100:.1f}%). The last column asks a different question of the slow series: "
          "does the reading at the high say how deep the selloff goes (rank correlation with depth, QQQ / SPY; "
          "+1 would mean a higher reading always came with a deeper selloff, and anything inside about 0.4 either way is indistinguishable from none on this sample).", "",
          "| Group | Variable | Score alone | Added to the model | Reading at the high vs depth |", "|---|---|---|---|---|"]
    verdict = {}
    for grp, fs in ASKED.items():
        best = None
        for f in fs:
            sc = score(f, ALL)
            if not sc:
                continue
            sub = [r for r in VIXROWS if r.get(f) is not None]
            base_m = oos(FEATS, sub)[4]["skill"]
            mm = oos(FEATS + [f], sub)[4]["skill"]
            gain = (mm - base_m) * 100
            best = gain if best is None else max(best, gain)
            cell = "n/a"
            if f in SLOW:
                parts = []
                for s in ("QQQ", "SPY"):
                    E = [e for e in EPS if e["sym"] == s and e.get(f) is not None]
                    parts.append(f"{spearman([e[f] for e in E], [-e['depth'] for e in E]):+.2f} (n={len(E)})" if len(E) >= 8 else "n/a")
                cell = " / ".join(parts)
            L.append(f"| {grp} | {NAMES[f]} | {max(sc[0], 1 - sc[0]):.2f} | {gain:+.1f} points | {cell} |")
        verdict[grp] = best
        if best is None:
            L.append(f"| {grp} | not tested: the history could not be downloaded | n/a | n/a | n/a |")
    L += [""]
    for grp, best in verdict.items():
        if best is None:
            L.append(f"- **{grp}:** no data, so no verdict.")
        elif best > 1.0:
            L.append(f"- **{grp}:** the best version added {best:.1f} points out of sample. Worth a closer look before adding it.")
        elif best <= 0.05:
            L.append(f"- **{grp}:** every version left the out-of-sample result the same or worse. Not added to the model.")
        else:
            L.append(f"- **{grp}:** the best version added {best:.1f} points out of sample, inside the noise. Not added to the model.")
    L += ["", "Shiller P/E, M2 and margin debt are monthly and published weeks late, so within one selloff they barely move: "
          "they can describe the backdrop but cannot mark a day. Bollinger position is the 20-day average and RSI restated.", ""]
    if OPEN_PEAK:
        now_at = have["at"](OPEN_PEAK)
        L += [f"**The backdrop at this selloff's high ({OPEN_PEAK})** against the highs of the {sum(1 for e in EPS if e['sym'] == 'QQQ')} "
              "finished QQQ selloffs. A high rank says the backdrop was stretched; the correlations above say that has not reliably meant a deeper selloff.", "",
              "| Reading | At this high | Rank among past highs | Median of past highs |", "|---|---|---|---|"]
        for f in SLOW:
            xs = sorted(e[f] for e in EPS if e["sym"] == "QQQ" and e.get(f) is not None)
            v = now_at.get(f)
            if v is None or len(xs) < 8:
                continue
            fmt = (lambda x: f"{x:.1f}") if f == "cape" else (lambda x: f"{x * 100:+.1f}%")
            L.append(f"| {NAMES[f]} | {fmt(v)} | {sum(x <= v for x in xs)} of {len(xs)} (1 = lowest) | {fmt(xs[len(xs) // 2])} |")
        L.append("")

    # ---- the selloff open now
    if OPEN:
        L += ["## The selloff open now, day by day", "", "What the model would have said at each close (not yet scored: the selloff is still open).", ""]
        for s, R in OPEN.items():
            L += [f"**{s}**, high close ${R[0]['peak']:,.2f} on {R[0]['peak_date']}:", "", "| Date | Close | From the high | VIX vs its peak | Chance the low is in |", "|---|---|---|---|---|"]
            model_now = {"features": FEATS, "clip": {k: list(v) for k, v in CLIP.items()}, "mean": list(mu), "sd": list(sd),
                         "intercept": float(b[0]), "beta": list(b[1:]), "calibration": knots,
                         "fallback": {"features": FALLBACK, "mean": list(muf), "sd": list(sdf), "intercept": float(bf[0]), "beta": list(bf[1:]), "calibration": knots_f}}
            for r in R:
                p = bw.probability(model_now, r)[0]
                L.append(f"| {r['date']} | ${r['close']:,.2f} | {r['ddclose'] * 100:.1f}% | "
                         + ("n/a" if r.get("vix_off") is None else f"{r['vix_off'] * 100:.0f}%") + f" | {p * 100:.0f}% |")
            L.append("")

    L += ["## Limits", "",
          f"- {n_eps} selloffs, and QQQ and SPY mostly fall together, so the independent sample is nearer 25.",
          "- Only three of them were long bear markets. The model cannot tell a bear-market rally from a final low early on.",
          "- Everything is on closing prices. An intraday reading uses the live price as if it were the close.",
          "- VIX readings before 2002-05 were not available, so the 2000-01 part of the dot-com bust is not in the VIX model.", ""]
    (HERE / "bottom_results.md").write_text("\n".join(L))
    model = {
        "_comment": "Written by bottom_backtest.py. Do not edit by hand; changing the model needs a live Ryan turn and a re-run.",
        "built_from_data_through": last_bar,
        "features": FEATS, "clip": {k: list(CLIP[k]) for k in FEATS},
        "mean": [round(float(x), 6) for x in mu], "sd": [round(float(x), 6) for x in sd],
        "intercept": round(float(b[0]), 6), "beta": [round(float(x), 6) for x in b[1:]], "calibration": knots,
        "fallback": {"features": FALLBACK, "mean": [round(float(x), 6) for x in muf], "sd": [round(float(x), 6) for x in sdf],
                     "intercept": round(float(bf[0]), 6), "beta": [round(float(x), 6) for x in bf[1:]], "calibration": knots_f,
                     "auc": round(mf["auc"], 3)},
        "checkpoints": checks,
        "oos": {"auc": round(m["auc"], 3), "skill": round(m["skill"], 3), "days": m["n"], "selloffs": len(tab), "reliability": rel,
                "median_sessions_to_50": st.median(x[0] for x in lead[0.5]), "median_sessions_to_70": st.median(x[0] for x in lead[0.7]),
                "false_50": false[0.5], "false_70": false[0.7]},
    }
    (HERE / "bottom_model.json").write_text(json.dumps(model, indent=2) + "\n")
    print(f"days {len(ALL)} selloffs {n_eps} | chosen model: score {m['auc']:.3f}, skill {m['skill'] * 100:.1f}% | macro files: "
          + ", ".join(k for k in ("cape", "m2", "md") if have[k]))
    print("wrote bottom_model.json and bottom_results.md")


if __name__ == "__main__":
    main()
