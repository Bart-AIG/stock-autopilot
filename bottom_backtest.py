"""Backtest for bottom_watch.py. Run: python3 bottom_backtest.py

Reads data/bottom/*.csv (daily QQQ, SPY, VIX, HYG, IEF, RSP since 1999-2007; source:
Robinhood history pulled 2026-11-20). For every day inside every QQQ / SPY selloff it asks
"has the lowest close of this selloff already printed?", ranks 44 candidate variables by how
well each separates yes from no, fits a small logistic model, and checks it on selloffs it
was not fitted on (every selloff that peaked in the same calendar year is held out together).

Writes bottom_model.json (what the live job loads) and bottom_results.md (the evidence).
Needs numpy. The live job does not.
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
}
CLIP = {"vix_off": (-0.75, 0.0), "dist200": (-0.40, 0.15), "rsi14": (0.0, 100.0)}
FEATS = ["vix_off", "dist200", "rsi14"]
FALLBACK = ["dist200", "rsi14"]            # when no VIX reading is available
VARIANTS = {
    "VIX off its peak only": ["vix_off"],
    "+ close vs the 200-day": ["vix_off", "dist200"],
    "+ RSI(14)  [chosen]": ["vix_off", "dist200", "rsi14"],
    "+ share of the drop retraced": ["vix_off", "dist200", "rsi14", "retr"],
    "+ failed rebounds so far": ["vix_off", "dist200", "rsi14", "legs"],
    "+ direction of the 200-day": ["vix_off", "dist200", "rsi14", "slope200"],
    "+ junk bonds vs Treasuries": ["vix_off", "dist200", "rsi14", "hy20"],
    "11 variables": ["vix_off", "dist200", "rsi14", "retr", "legs", "reb_atr", "giveback", "days", "speed", "ddclose", "dist50"],
    "No VIX: 200-day + RSI(14)": ["dist200", "rsi14"],
}


def load(sym):
    R = list(csv.DictReader(open(DATA / f"{sym}.csv")))
    return {"d": [r["date"] for r in R], "o": [float(r["open"]) for r in R], "h": [float(r["high"]) for r in R],
            "l": [float(r["low"]) for r in R], "c": [float(r["close"]) for r in R],
            "v": [float(r["volume"]) if r.get("volume") else None for r in R]}


def closes(sym):
    return {r["date"]: float(r["close"]) for r in csv.DictReader(open(DATA / f"{sym}.csv"))}


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


def design(feats, rows):
    rows = [r for r in rows if all(r.get(f) is not None for f in feats)]
    X = np.array([[val(f, r) for f in feats] for r in rows])
    y = np.array([r["y"] for r in rows], float)
    cnt = Counter((r["sym"], r["ep"]) for r in rows)
    w = np.array([1 / math.sqrt(cnt[(r["sym"], r["ep"])]) for r in rows])     # a 700-day bear must not outvote 40 corrections
    return rows, X, y, w / w.mean()


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
    """Weighted pool-adjacent-violators. Returns knots [[raw, calibrated], ...]."""
    order = np.argsort(pred)
    blocks = [[float(pred[i]), float(y[i]) * float(w[i]), float(w[i]), float(pred[i]) * float(w[i])] for i in order]
    out = []
    for b in blocks:                       # block = [max raw, sum(y*w), sum(w), sum(raw*w)]
        out.append(b)
        while len(out) > 1 and out[-2][1] / out[-2][2] > out[-1][1] / out[-1][2]:
            a = out.pop()
            out[-1] = [a[0], out[-1][1] + a[1], out[-1][2] + a[2], out[-1][3] + a[3]]
    xs = np.array([b[3] / b[2] for b in out])
    ys = np.array([b[1] / b[2] for b in out])
    grid = [0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98]
    knots = [[g, float(np.clip(np.interp(g, xs, ys), 0.03, 0.95))] for g in grid]
    for i in range(1, len(knots)):
        knots[i][1] = max(knots[i][1], knots[i - 1][1])
    return [[k[0], round(k[1], 3)] for k in knots]


def calibrate(p, knots):
    return float(np.interp(p, [k[0] for k in knots], [k[1] for k in knots]))


def main():
    vix, hyg, ief, rsp, spyc = closes("VIX"), closes("HYG"), closes("IEF"), closes("RSP"), closes("SPY")
    ALL, EPS = [], {}
    for s in ("QQQ", "SPY"):
        B = load(s)
        rows, eps = bw.scan(s, B, vix, hyg, ief, rsp, spyc)
        EPS[s] = (B, eps)
        ALL += [r for r in rows if r["y"] is not None]
    VIXROWS = [r for r in ALL if r.get("vix_off") is not None]
    n_eps = len({(r["sym"], r["ep"]) for r in ALL})
    L = ["# Bottom watch: which variables say the low is in", "",
         f"Built {ALL and max(r['date'] for r in ALL)} data. Re-run with `python3 bottom_backtest.py`.", "",
         f"- **Sample:** {len(ALL):,} days inside {n_eps} QQQ and SPY selloffs, 1999-09 to 2026 (closing prices). "
         f"VIX history starts 2002-05, so models that use it are fitted on {len(VIXROWS):,} days.",
         "- **Question on each day:** has the lowest close of this selloff already printed?",
         "- **Score:** 0.50 means the variable is useless; 1.00 means it separates the two perfectly "
         "(AUC, direction-adjusted). \"On the low day\" is the same score using only days that made a new closing low.", ""]
    # ---- single-variable ranking
    feats = [k for k in NAMES if any(r.get(k) is not None for r in ALL)]
    rank = []
    for f in feats:
        sub = [r for r in ALL if r.get(f) is not None]
        a = auc([r[f] for r in sub], [r["y"] for r in sub])
        d0 = [r for r in sub if r["days"] == 0]
        a0 = auc([r[f] for r in d0], [r["y"] for r in d0]) if len(d0) > 50 else float("nan")
        rank.append((f, a, a0, len(sub)))
    rank.sort(key=lambda t: -abs(t[1] - 0.5))
    L += ["## Each variable on its own", "", "| Variable | Score | Low more likely in when it is | On the low day | Days |", "|---|---|---|---|---|"]
    for f, a, a0, n in rank:
        L.append(f"| {NAMES[f]} | {max(a, 1 - a):.2f} | {'higher' if a >= 0.5 else 'lower'} | "
                 f"{'n/a' if a0 != a0 else f'{max(a0, 1 - a0):.2f}'} | {n:,} |")
    base0 = np.mean([r["y"] for r in ALL if r["days"] == 0])
    L += ["", f"A day that makes a new closing low turns out to be the final low {base0 * 100:.0f}% of the time. "
          "Volume on the low day, a close off the low, follow-through days and the equal-weight index all score near 0.50: "
          "they did not separate final lows from the rest.", ""]
    # ---- model comparison
    L += ["## Combining them (tested on selloffs the model had not seen)", "",
          "| Model | Score | Improvement over always guessing the base rate |", "|---|---|---|"]
    for name, fs in VARIANTS.items():
        base_rows = [r for r in VIXROWS if all(r.get(f) is not None for f in fs)]
        _, _, _, _, m = oos(fs, base_rows)
        L.append(f"| {name} | {m['auc']:.3f} | {m['skill'] * 100:.1f}% |")
    L += ["", "Adding a fourth variable made the out-of-sample result worse every time, so the model stops at three.", ""]
    # ---- final model
    rows, pred, y, w, m = oos(FEATS, VIXROWS)
    knots = isotonic(pred, y, w)
    cal = np.array([calibrate(p, knots) for p in pred])
    _, X, yy, ww = design(FEATS, VIXROWS)
    mu, sd = X.mean(0), X.std(0)
    b = fit((X - mu) / sd, yy, ww)
    rows_f, Xf, yf, wf = design(FALLBACK, ALL)
    muf, sdf = Xf.mean(0), Xf.std(0)
    bf = fit((Xf - muf) / sdf, yf, wf)
    _, predf, yf2, wf2, mf = oos(FALLBACK, ALL)
    knots_f = isotonic(predf, yf2, wf2)
    bands = [(0, .25), (.25, .5), (.5, .7), (.7, .85), (.85, 1.01)]
    rel = []
    for a, c in bands:
        k = (cal >= a) & (cal < c)
        rel.append({"lo": a, "hi": min(c, 1.0), "n": int(k.sum()), "actual": round(float(y[k].mean()), 3) if k.sum() else None})
    L += ["## The model", "", "Chance the low is in = a logistic blend of three readings, then adjusted so that the "
          "stated chance matches how often it was right out of sample.", "",
          "| Reading | Average in past selloffs | Weight (per standard deviation) |", "|---|---|---|"]
    for f, mm, ss, bb in zip(FEATS, mu, sd, b[1:]):
        L.append(f"| {NAMES[f]} | {mm:.3f} | {bb:+.2f} |")
    L += ["", f"Out of sample: score {m['auc']:.3f}; {m['skill'] * 100:.1f}% better than the base rate.", "",
          "| Stated chance | Days | Low really was in |", "|---|---|---|"]
    for r_ in rel:
        L.append(f"| {r_['lo'] * 100:.0f}% to {r_['hi'] * 100:.0f}% | {r_['n']:,} | {r_['actual'] * 100:.0f}% |" if r_["n"] else
                 f"| {r_['lo'] * 100:.0f}% to {r_['hi'] * 100:.0f}% | 0 | n/a |")
    # ---- lead time and false alarms
    by = defaultdict(list)
    for r, p in zip(rows, cal):
        by[(r["sym"], r["ep"])].append((r["i"], r["days"], r["y"], p, r["reb"], r["date"], r["ddlow"], r["peak_date"]))
    tab, lead = [], {0.5: [], 0.7: []}
    false = {0.5: 0, 0.7: 0}
    deep_false = {0.5: 0, 0.7: 0}
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
            if post[0][6] < -0.25:
                deep_false[th] += fa
            if hit:
                lead[th].append((hit[1], hit[4]))
            row += [hit[1] if hit else None, hit[4] if hit else None, fa]
        tab.append(row)
    L += ["", "## How fast it calls a low, and how often it is fooled", "",
          f"- **Speed:** across {len(tab)} selloffs the reading reached 50% a median of {st.median(x[0] for x in lead[0.5]):.0f} "
          f"sessions after the final low (price {st.median(x[1] for x in lead[0.5]) * 100:.1f}% off the low by then) and 70% after "
          f"{st.median(x[0] for x in lead[0.7]):.0f} sessions ({st.median(x[1] for x in lead[0.7]) * 100:.1f}% off the low).",
          f"- **False alarms:** before the final low the reading crossed 50% {false[0.5]} times and 70% {false[0.7]} times. "
          f"{deep_false[0.5]} and {deep_false[0.7]} of those were inside the selloffs that fell more than 25% "
          "(2000-02, 2008, 2020, 2022): bear-market rallies look like bottoms to this model.", "",
          "| Index | High | Final low | Depth | Sessions to 50% | Off the low then | False 50% crossings | Sessions to 70% | Off the low then | False 70% crossings |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for t in tab:
        f = lambda v, pct=False: "n/a" if v is None else (f"{v * 100:.1f}%" if pct else f"{v}")
        L.append(f"| {t[0]} | {t[1]} | {t[2]} | {t[3] * 100:.1f}% | {f(t[4])} | {f(t[5], True)} | {t[6]} | {f(t[7])} | {f(t[8], True)} | {t[9]} |")
    L += ["", "## Limits", "",
          "- About 50 selloffs, and QQQ and SPY mostly fall together, so the independent sample is nearer 25.",
          "- Only three of them were long bear markets. The model cannot tell a bear-market rally from a final low early on.",
          "- Everything is on closing prices. An intraday reading uses the live price as if it were the close.",
          "- VIX readings before 2002-05 were not available, so the 2000-01 part of the dot-com bust is not in the VIX model.", ""]
    (HERE / "bottom_results.md").write_text("\n".join(L))
    model = {
        "_comment": "Written by bottom_backtest.py. Do not edit by hand; changing the model needs a live Ryan turn and a re-run.",
        "built_from_data_through": max(r["date"] for r in ALL),
        "features": FEATS, "clip": {k: list(v) for k, v in CLIP.items()},
        "mean": [round(float(x), 6) for x in mu], "sd": [round(float(x), 6) for x in sd],
        "intercept": round(float(b[0]), 6), "beta": [round(float(x), 6) for x in b[1:]], "calibration": knots,
        "fallback": {"features": FALLBACK, "mean": [round(float(x), 6) for x in muf], "sd": [round(float(x), 6) for x in sdf],
                     "intercept": round(float(bf[0]), 6), "beta": [round(float(x), 6) for x in bf[1:]], "calibration": knots_f,
                     "auc": round(mf["auc"], 3)},
        "oos": {"auc": round(m["auc"], 3), "skill": round(m["skill"], 3), "days": m["n"], "selloffs": len(tab), "reliability": rel,
                "median_sessions_to_50": st.median(x[0] for x in lead[0.5]), "median_sessions_to_70": st.median(x[0] for x in lead[0.7]),
                "false_50": false[0.5], "false_70": false[0.7]},
    }
    (HERE / "bottom_model.json").write_text(json.dumps(model, indent=2) + "\n")
    print(f"days {len(ALL)} selloffs {n_eps} | chosen model: score {m['auc']:.3f}, skill {m['skill'] * 100:.1f}%")
    print("calibration knots", knots)
    print("reliability", [(r_['lo'], r_['hi'], r_['n'], r_['actual']) for r_ in rel])
    print("wrote bottom_model.json and bottom_results.md")


if __name__ == "__main__":
    main()
