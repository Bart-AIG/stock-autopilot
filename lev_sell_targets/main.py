"""Sell-target model for leveraged ETF positions.

Re-runnable weekly:  python main.py            (fetches fresh data)
                     python main.py --cache    (re-uses cache/*.json)

Outputs (in ./output): sell_targets.xlsx, summary.md, <TICKER>_fan.png
All model output is a description of past behaviour and of a resampled
past. It is not a forecast.
"""
import argparse
import datetime as dt
import json
import math
import os
import sys
import time
import urllib.request

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# CONFIG: edit here. Add a pair by adding a dict to POSITIONS.
# Shares / cost basis: joint account, read from the broker 2026-11-12.
# ---------------------------------------------------------------------------
POSITIONS = [
    {"etf": "SOXL", "underlying": "SOXX", "leverage": 3, "shares": 105, "cost": 53.90,
     "real_history": True,      # use the real fund for the historical study
     "index_change": "2021-07-01",  # calibrate drag after the index change
     "note": "SOXX is a proxy for the NYSE/ICE Semiconductor Index SOXL tracks. "
             "Both funds changed index in 2021, so pre-2021 history mixes two indexes."},
    {"etf": "COHX", "underlying": "COHR", "leverage": 2, "shares": 500, "cost": 7.40,
     "real_history": False, "index_change": None,
     "note": "COHR history before 2022 is II-VI Inc (it bought Coherent and took the ticker)."},
    {"etf": "AAOX", "underlying": "AAOI", "leverage": 2, "shares": 2300, "cost": 1.79,
     "real_history": False, "index_change": None,
     "note": "AAOI history starts 2013-09-26 (IPO)."},
]

SETTINGS = {
    "mc_paths": 10_000,
    "mc_years": 2,
    "block": 20,
    "seed": 7,
    "min_rung_prob": 0.20,        # a rung needs >= this 2y touch probability (worse of both runs)
    "stress_T": [0.25, 0.5, 1.0, 2.0],
    "checkpoint_T": [0.25, 0.5, 1.0],
    # Underlying target levels. ("way", f) = f of the way from now to the ATH;
    # ("ath", m) = ATH x (1+m). The 10% rung is extra, used only when fewer
    # than 3 of the required levels have a meaningful hit probability.
    "levels": [("way", 0.10, "10% to ATH (extra)"), ("way", 0.25, "25% to ATH"),
               ("way", 0.50, "50% to ATH"), ("way", 0.75, "75% to ATH"),
               ("way", 1.00, "ATH"), ("ath", 0.10, "ATH +10%"), ("ath", 0.25, "ATH +25%")],
    "rung_pcts": {4: [0.25, 0.25, 0.25, 0.25], 3: [0.34, 0.33, 0.33], 2: [0.5, 0.5], 1: [1.0]},
}
# Risk notes from issuer / news research. Update by hand when you re-run.
# Researched 2026-11-12 from third-party data sites; issuer pages were not reachable, so unverified.
RISK_NOTES = [
    "SOXL (Direxion): about $19B net assets (Jul 2026), 0.75% net expense ratio. No closure or reverse-split "
    "notice found. Index moved from PHLX SOX to the ICE (now NYSE) Semiconductor Index on 2021-08-25.",
    "COHX (Tradr, launched 2026-02-18, 1.49% expense ratio): AUM fell from about $94M (Sep 1) to about $58M "
    "(Oct 15). No closure notice found, but Tradr has closed about 20 single-stock funds in 2026 (Jan, Mar, "
    "May, Oct). LIQUIDATION RISK: moderate and rising.",
    "AAOX (Tradr, launched 2026-03-24, 1.49% expense ratio): about $200-280M AUM, larger than COHX. No "
    "closure notice found. Same issuer closure pattern applies. A liquidation pays out NAV in cash, which "
    "realizes the gain or loss on Tradr's date, not yours.",
    "Earnings: COHR reported 2026-11-04 and AAOI 2026-11-05. Next dates are not announced; expect about "
    "early Feb 2027 (COHR) and late Feb 2027 (AAOI). Both fall before rung 1's time stop on COHX and AAOX.",
]

BUCKETS = [("<3m", 0, 63), ("3-6m", 63, 126), ("6-12m", 126, 252), ("1-2y", 252, 504),
           ("2y+", 504, 10**9), ("all", 0, 10**9)]
TD = 252
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
OUT = os.path.join(HERE, "output")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
LOG = []


def log(msg):
    LOG.append(msg)
    print(msg)


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
def fetch(ticker, use_cache):
    path = os.path.join(CACHE, f"{ticker}.json")
    if not (use_cache and os.path.exists(path)):
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
               f"?period1=1262304000&period2={int(time.time())}&interval=1d&events=split,div")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            raw = urllib.request.urlopen(req, timeout=30).read()
            js = json.loads(raw)
            if not js.get("chart", {}).get("result"):
                raise ValueError(js.get("chart", {}).get("error"))
        except Exception as e:  # stop, never fall back to made-up prices
            sys.exit(f"DATA PULL FAILED for {ticker}: {e}. Stopping (no fallback prices).")
        os.makedirs(CACHE, exist_ok=True)
        with open(path, "wb") as f:
            f.write(raw)
    js = json.load(open(path))
    res = js["chart"]["result"][0]
    meta = res["meta"]
    off = meta.get("gmtoffset", 0)
    dates = [dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date() for t in res["timestamp"]]
    q = res["indicators"]["quote"][0]
    df = pd.DataFrame({"adj": res["indicators"]["adjclose"][0]["adjclose"],
                       "close": q["close"], "high": q["high"]},
                      index=pd.to_datetime(dates)).dropna(subset=["adj", "close"])
    df = df[~df.index.duplicated(keep="last")]
    splits = []
    for s in res.get("events", {}).get("splits", {}).values():
        d = pd.Timestamp(dt.datetime.fromtimestamp(s["date"] + off, dt.timezone.utc).date())
        i = df.index.searchsorted(d)
        if 0 < i < len(df):
            adj_r = df["adj"].iloc[i] / df["adj"].iloc[i - 1] - 1
            raw_r = df["close"].iloc[i] / df["close"].iloc[i - 1] - 1
            ok = abs(adj_r) < 0.25
            splits.append(f"{s['splitRatio']} on {d.date()}: adjusted return that day "
                          f"{adj_r:+.1%} ({'continuous' if ok else 'BREAK - check'})")
    # Intraday flag
    now = time.time()
    per = meta.get("currentTradingPeriod", {}).get("regular", {})
    last_date = df.index[-1].date()
    today = dt.datetime.fromtimestamp(now + off, dt.timezone.utc).date()
    intraday = bool(last_date == today and per and per["start"] <= now < per["end"])
    for s in splits:
        log(f"  {ticker} split {s}")
    return {"df": df, "splits": splits, "intraday": intraday, "last": float(df["adj"].iloc[-1]),
            "last_date": last_date, "fetched": dt.datetime.fromtimestamp(os.path.getmtime(path))}


# ---------------------------------------------------------------------------
# Model pieces
# ---------------------------------------------------------------------------
def calibrate(etf, und, k, since=None):
    j = pd.concat([etf["adj"].rename("L"), und["adj"].rename("S")], axis=1, sort=True).dropna()
    if since:
        j = j[j.index >= since]
    r = j.pct_change().dropna()
    beta = float(np.cov(r.L, r.S)[0, 1] / np.var(r.S, ddof=1))
    corr = float(r.L.corr(r.S))
    diff = r.L - k * r.S
    drag = float(-diff.mean() * TD)   # positive = cost (fees + financing)
    se = float(diff.std() * TD / math.sqrt(len(diff)))
    return {"start": r.index[0].date(), "end": r.index[-1].date(), "n": len(r),
            "beta": beta, "corr": corr, "drag": drag, "drag_se": se}


def vols(und):
    r = und["adj"].pct_change().dropna()
    return {"3m": float(r.iloc[-63:].std() * math.sqrt(TD)),
            "1y": float(r.iloc[-252:].std() * math.sqrt(TD)),
            "lr": float(r[r.index >= "2016-01-01"].std() * math.sqrt(TD))}


def synthetic(und, k, drag):
    r = und["adj"].pct_change().fillna(0.0).values
    f = np.clip(1 + k * r - drag / TD, 0.0, None)
    return pd.Series(np.cumprod(f), index=und.index)


def track_err(etf, syn):
    j = pd.concat([etf["adj"].rename("L"), syn.rename("Y")], axis=1, sort=True).dropna()
    r = j.pct_change().dropna()
    te = float((r.L - r.Y).std() * math.sqrt(TD))
    cum_real = j.L.iloc[-1] / j.L.iloc[0] - 1
    cum_syn = j.Y.iloc[-1] / j.Y.iloc[0] - 1
    return te, float(cum_real), float(cum_syn)


def level_prices(S_now, ath):
    out = []
    for kind, v, label in SETTINGS["levels"]:
        s = S_now + v * (ath - S_now) if kind == "way" else ath * (1 + v)
        out.append({"kind": kind, "val": v, "label": label, "S": s, "gap": s / S_now - 1})
    return out


def historical(S, L, gap, L_now):
    """For every start date, first day S rose by `gap`; record L multiple and days."""
    S = np.asarray(S, float)
    L = np.asarray(L, float)
    n = len(S)
    days, mult = [], []
    for t in range(n - 1):
        if L[t] <= 0:
            continue
        w = S[t + 1:] >= S[t] * (1 + gap)
        j = int(w.argmax())
        if w[j]:
            days.append(j + 1)
            mult.append(L[t + 1 + j] / L[t])
    days, mult = np.array(days), np.array(mult)
    rows = []
    for name, lo, hi in BUCKETS:
        m = (days >= lo) & (days < hi) if len(days) else np.array([], bool)
        if m.sum() == 0:
            rows.append({"bucket": name, "n": 0})
            continue
        px = L_now * mult[m]
        p = np.percentile(px, [10, 25, 50, 75, 90])
        rows.append({"bucket": name, "n": int(m.sum()), "med_days": float(np.median(days[m])),
                     "p10": p[0], "p25": p[1], "p50": p[2], "p75": p[3], "p90": p[4]})
    return {"starts": n - 1, "hits": len(days), "rows": rows}


def first_day(cum, thr, up=True):
    hit = cum >= thr if up else cum <= thr
    d = hit.argmax(axis=1).astype(float)
    d[~hit[:, -1]] = np.inf
    return d


def monte_carlo(rets, k, drag, rng):
    N, H, B = SETTINGS["mc_paths"], SETTINGS["mc_years"] * TD, SETTINGS["block"]
    nb = math.ceil(H / B)
    starts = rng.integers(0, len(rets) - B, size=(N, nb))
    idx = (starts[:, :, None] + np.arange(B)).reshape(N, -1)[:, :H]
    r = rets[idx]
    S = np.cumprod(1 + r, axis=1)
    L = np.cumprod(np.clip(1 + k * r - drag / TD, 0.0, None), axis=1)
    return {"S": S, "L": L, "cmS": np.maximum.accumulate(S, axis=1),
            "cmL": np.maximum.accumulate(L, axis=1), "cnL": np.minimum.accumulate(L, axis=1)}


def mc_level_stats(mc, gap, L_now, ceiling):
    hd = first_day(mc["cmS"], 1 + gap)
    hit = np.isfinite(hd)
    p = {h: float((hd < d).mean()) for h, d in (("3m", 63), ("6m", 126), ("1y", 252), ("2y", 504))}
    if hit.sum():
        Lh = mc["L"][np.where(hit)[0], hd[hit].astype(int)] * L_now
        med_L = float(np.median(Lh))
        q = np.percentile(hd[hit], [25, 50, 75])
    else:
        med_L, q = float("nan"), [np.nan] * 3
    p_ceiling = float(np.isfinite(first_day(mc["cmL"], ceiling / L_now)).mean())
    return {"p": p, "med_L": med_L, "hd_q": q, "p_ceiling": p_ceiling, "hd": hd}


def mc_touch(mc, price, L_now):
    up = price >= L_now
    d = first_day(mc["cmL"] if up else mc["cnL"], price / L_now, up=up)
    return d


# ---------------------------------------------------------------------------
# Run one pair
# ---------------------------------------------------------------------------
def run_pair(cfg, data, rng):
    etf, und, k = data[cfg["etf"]], data[cfg["underlying"]], cfg["leverage"]
    E, U = etf["df"], und["df"]
    out = {"cfg": cfg, "intraday": etf["intraday"] or und["intraday"],
           "splits": {cfg["etf"]: etf["splits"], cfg["underlying"]: und["splits"]}}
    out["L_now"], out["S_now"] = etf["last"], und["last"]
    out["asof"] = max(etf["last_date"], und["last_date"])
    ath_i = U["close"].idxmax()
    out["ath"], out["ath_date"] = float(U.loc[ath_i, "close"]), ath_i.date()
    # adj and close can differ by dividends; put S_now on the same (close) basis as the ATH
    out["S_now"] = float(U["close"].iloc[-1])
    out["L_now"] = float(E["close"].iloc[-1])

    cal_full = calibrate(E, U, k)
    cal = calibrate(E, U, k, cfg["index_change"]) if cfg["index_change"] else cal_full
    out["cal_full"], out["cal"] = cal_full, cal
    drag = cal["drag"]
    out["drag"] = drag
    out["vol"] = vols(U)

    syn = synthetic(U, k, drag)
    out["te"] = track_err(E, syn)
    if cfg["real_history"]:
        j = pd.concat([E["adj"].rename("L"), U["adj"].rename("S")], axis=1, sort=True).dropna()
        S_hist, L_hist = j.S.values, j.L.values
        out["hist_src"] = f"real {cfg['etf']} vs {cfg['underlying']}, {j.index[0].date()} on"
    else:
        S_hist, L_hist = U["adj"].values, syn.values
        out["hist_src"] = f"synthetic {k}x {cfg['underlying']} less {drag:.1%}/yr drag, {U.index[0].date()} on"

    r = U["adj"].pct_change().dropna()
    out["wipe_days"] = [(d.date(), float(x)) for d, x in r[r <= -1 / k].items()]
    out["big_days"] = [(d.date(), float(x)) for d, x in r[r <= -0.5 / k].items()]

    levels = level_prices(out["S_now"], out["ath"])
    sig = max(out["vol"]["lr"], out["vol"]["1y"])
    for lv in levels:
        lv["ceiling"] = out["L_now"] * (lv["S"] / out["S_now"]) ** k
        lv["hist"] = historical(S_hist, L_hist, lv["gap"], out["L_now"])
    out["levels"] = levels

    rets_full = r.values
    rets_2y = r.values[-2 * TD:]
    out["mc"] = {}
    for name, rr in (("full", rets_full), ("2y", rets_2y)):
        mc = monte_carlo(rr, k, drag, rng)
        stats = [mc_level_stats(mc, lv["gap"], out["L_now"], lv["ceiling"]) for lv in levels]
        out["mc"][name] = {"mc": mc, "stats": stats}

    # ---- Sell plan ------------------------------------------------------
    cand = []
    for i, lv in enumerate(levels):
        p2 = min(out["mc"][n]["stats"][i]["p"]["2y"] for n in ("full", "2y"))
        mc_med = min(out["mc"][n]["stats"][i]["med_L"] for n in ("full", "2y"))
        # Rung price = stress price (long-run vol) at the median time the underlying
        # takes to reach the level (full-history run). Time stop = that date.
        T_med = out["mc"]["full"]["stats"][i]["hd_q"][1] / TD
        decay_lr = k * (k - 1) / 2 * out["vol"]["lr"] ** 2 + drag
        price = lv["ceiling"] * math.exp(-decay_lr * T_med) if np.isfinite(T_med) else float("nan")
        lv["p2_min"], lv["rung_price"], lv["mc_med"], lv["T_med"] = p2, price, mc_med, T_med
        if p2 >= SETTINGS["min_rung_prob"] and price > max(out["L_now"], cfg["cost"]):
            cand.append(i)
    req = [i for i in cand if SETTINGS["levels"][i][2].find("extra") < 0]
    chosen = req[:4] if len(req) >= 3 else sorted(set(cand[:1] + req))[:4]
    if not chosen:  # nothing meaningful: fall back to the single most likely level
        chosen = [max(range(len(levels)), key=lambda i: levels[i]["p2_min"])]
    out["thin_ladder"] = len(chosen) < 3
    pcts = SETTINGS["rung_pcts"][len(chosen)]
    rungs = []
    for n, (i, pct) in enumerate(zip(chosen, pcts)):
        lv = levels[i]
        price = lv["rung_price"]
        touch = {}
        for name in ("full", "2y"):
            d = mc_touch(out["mc"][name]["mc"], price, out["L_now"])
            touch[name] = d
        dfull = touch["full"][np.isfinite(touch["full"])]
        win = np.percentile(dfull, [25, 75]) if len(dfull) else [np.nan, np.nan]
        T = lv["T_med"]
        rungs.append({"level_idx": i, "pct": pct, "price": price,
                      "p_full": float(np.isfinite(touch["full"]).mean()),
                      "p_2y": float(np.isfinite(touch["2y"]).mean()),
                      "win_days": win, "T_stop": T, "touch": touch})
    out["rungs"] = rungs

    # Downside before the first rung is touched; cost-basis touch; L vs S at 1y
    out["down"] = {}
    for name in ("full", "2y"):
        mc = out["mc"][name]["mc"]
        first = rungs[0]["touch"][name]
        dd = {}
        for x in (0.5, 0.75, 0.9):
            d = first_day(mc["cnL"], 1 - x, up=False)
            dd[x] = float((d < first).mean())
        cb = mc_touch(mc, cfg["cost"], out["L_now"])
        L1, S1 = mc["L"][:, TD - 1], mc["S"][:, TD - 1]
        out["down"][name] = {"dd": dd, "p_cost": float(np.isfinite(cb).mean()),
                             "p_L_beats_S_1y": float((L1 > S1).mean()),
                             "med_L1": float(np.median(L1)), "med_S1": float(np.median(S1)),
                             "mean_L1": float(np.mean(L1)), "mean_S1": float(np.mean(S1))}
    out["sig"] = sig
    out["hurdle"] = (k + 1) / 2 * sig ** 2 + drag / (k - 1)
    return out


# ---------------------------------------------------------------------------
# Chart
# ---------------------------------------------------------------------------
def chart(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cfg = res["cfg"]
    L0 = res["L_now"]
    fig, ax = plt.subplots(figsize=(11, 6), dpi=110)
    x = pd.bdate_range(pd.Timestamp(res["asof"]) + pd.Timedelta(days=1), periods=SETTINGS["mc_years"] * TD)
    P = np.percentile(res["mc"]["full"]["mc"]["L"] * L0, [5, 25, 50, 75, 95], axis=0)
    ax.fill_between(x, P[0], P[4], color="#9ecae1", alpha=0.45, label="5-95% (full history)")
    ax.fill_between(x, P[1], P[3], color="#4292c6", alpha=0.5, label="25-75% (full history)")
    ax.plot(x, P[2], color="#08306b", lw=2, label="median (full history)")
    P2 = np.percentile(res["mc"]["2y"]["mc"]["L"] * L0, [25, 50, 75], axis=0)
    ax.plot(x, P2[1], color="#d94801", lw=1.8, ls="--", label="median (last-2y returns)")
    ax.plot(x, P2[0], color="#d94801", lw=0.8, ls=":")
    ax.plot(x, P2[2], color="#d94801", lw=0.8, ls=":", label="25/75% (last-2y returns)")
    for n, rg in enumerate(res["rungs"], 1):
        ax.axhline(rg["price"], color="#238b45", lw=1.2)
        ax.text(x[-230], rg["price"], f" Rung {n}: ${rg['price']:.2f} ({rg['p_full']:.0%}/{rg['p_2y']:.0%})",
                va="bottom", color="#238b45", fontsize=9)
    ax.axhline(cfg["cost"], color="#a50f15", lw=1.2, ls="--")
    ax.text(x[-160], cfg["cost"], f" cost basis ${cfg['cost']:.2f}", va="bottom", color="#a50f15", fontsize=9)
    ax.axhline(L0, color="grey", lw=0.8)
    ax.set_yscale("log")
    ax.set_title(f"{cfg['etf']} ({cfg['leverage']}x {cfg['underlying']}): simulated price fan, "
                 f"10,000 block-bootstrap paths, from ${L0:.2f} on {res['asof']}")
    ax.set_ylabel(f"{cfg['etf']} price (log scale)")
    ax.legend(loc="lower left", fontsize=8)
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    p = os.path.join(OUT, f"{cfg['etf']}_fan.png")
    fig.savefig(p)
    plt.close(fig)
    return p


# ---------------------------------------------------------------------------
# Workbook
# ---------------------------------------------------------------------------
def workbook(results, path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter as CL

    F = "Arial"
    BLUE = Font(name=F, color="0000FF")
    BLACK = Font(name=F)
    GREEN = Font(name=F, color="008000")
    BOLD = Font(name=F, bold=True)
    TITLE = Font(name=F, bold=True, size=14)
    YEL = PatternFill("solid", fgColor="FFF9C4")
    HDR = PatternFill("solid", fgColor="D9E1F2")
    GREY = PatternFill("solid", fgColor="EDEDED")
    thin = Border(bottom=Side(style="thin", color="999999"))
    USD = '$#,##0.00;($#,##0.00);"-"'
    USD0 = '$#,##0;($#,##0);"-"'
    PCT = '0.0%;(0.0%);"-"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Inputs"

    def put(sh, ref, v, font=BLACK, fmt=None, fill=None):
        c = sh[ref]
        c.value = v
        c.font = font
        if fmt:
            c.number_format = fmt
        if fill:
            c.fill = fill
        return c

    def inp(sh, ref, v, fmt=None):
        return put(sh, ref, v, BLUE, fmt, YEL)

    def header(sh, row, labels, col=1):
        for i, h in enumerate(labels):
            c = sh.cell(row=row, column=col + i, value=h)
            c.font = BOLD
            c.fill = HDR
            c.alignment = Alignment(wrap_text=True, vertical="center")
            c.border = thin

    # ---------------- Inputs ----------------
    put(ws, "A1", "Leveraged ETF sell-target model: inputs", TITLE)
    put(ws, "A2", "Legend:", BOLD)
    inp(ws, "B2", "Blue on yellow = hard-coded input (edit these)")
    put(ws, "C2", "Black = formula", BLACK)
    put(ws, "D2", "Green = link to another sheet", GREEN)
    put(ws, "E2", "Grey fill = raw simulation / history result (re-run main.py to refresh)", BLACK, fill=GREY)
    gen = [("As-of date", results[0]["asof"], "yyyy-mm-dd"), ("MC horizon (years)", SETTINGS["mc_years"], "0"),
           ("MC paths", SETTINGS["mc_paths"], "#,##0"), ("Bootstrap block (trading days)", SETTINGS["block"], "0"),
           ("Min 2y touch probability for a rung", SETTINGS["min_rung_prob"], PCT),
           ("Trading days per year", TD, "0")]
    for i, (lab, v, fmt) in enumerate(gen):
        put(ws, f"A{4 + i}", lab)
        inp(ws, f"B{4 + i}", v, fmt)
    G = {"asof": "Inputs!$B$4"}
    fields = [("Underlying", "underlying", None), ("Target leverage (k)", "k", "0"),
              ("Shares held", "shares", "#,##0"), ("Cost basis / share", "cost", USD),
              ("Leveraged ETF price now", "L_now", USD), ("Underlying price now", "S_now", USD),
              ("Underlying all-time high (close)", "ath", USD),
              ("Drag (fees + financing, /yr)", "drag", PCT),
              ("Underlying vol, since 2016", "vol_lr", PCT), ("Underlying vol, 1y", "vol_1y", PCT),
              ("Underlying vol, 3m", "vol_3m", PCT),
              ("Rung 1 % of shares", "pct1", PCT), ("Rung 2 % of shares", "pct2", PCT),
              ("Rung 3 % of shares", "pct3", PCT), ("Rung 4 % of shares", "pct4", PCT)]
    header(ws, 11, ["Field"] + [r["cfg"]["etf"] for r in results] + ["Source / note"])
    IN = {}
    for j, res in enumerate(results):
        col = CL(2 + j)
        IN[res["cfg"]["etf"]] = {}
        vals = {"underlying": res["cfg"]["underlying"], "k": res["cfg"]["leverage"],
                "shares": res["cfg"]["shares"], "cost": res["cfg"]["cost"], "L_now": res["L_now"],
                "S_now": res["S_now"], "ath": res["ath"], "drag": res["drag"],
                "vol_lr": res["vol"]["lr"], "vol_1y": res["vol"]["1y"], "vol_3m": res["vol"]["3m"]}
        for n in range(4):
            vals[f"pct{n + 1}"] = res["rungs"][n]["pct"] if n < len(res["rungs"]) else 0
        for i, (lab, key, fmt) in enumerate(fields):
            row = 12 + i
            put(ws, f"A{row}", lab)
            inp(ws, f"{col}{row}", vals[key], fmt)
            IN[res["cfg"]["etf"]][key] = f"Inputs!${col}${row}"
    srcn = CL(2 + len(results))
    notes = {12: "Config", 13: "Fund prospectus", 14: "Broker, joint account, 2026-11-12",
             15: "Broker, joint account, 2026-11-12", 16: "Yahoo Finance last close (may be intraday)",
             17: "Yahoo Finance last close (may be intraday)", 18: "Max split-adjusted close, Yahoo Finance",
             19: "Measured: mean(ETF r - k x underlying r) x 252 over the overlap (SOXL: since 2021-07-01)",
             20: "Yahoo adjclose daily returns", 21: "Last 252 sessions", 22: "Last 63 sessions",
             23: "Model pick; edit to re-weight", 24: "", 25: "", 26: ""}
    for row, t in notes.items():
        put(ws, f"{srcn}{row}", t)
    LV0 = 30
    header(ws, LV0 - 1, ["Underlying level", "Kind (way/ath)", "Value"])
    for i, (kind, v, lab) in enumerate(SETTINGS["levels"]):
        put(ws, f"A{LV0 + i}", lab)
        inp(ws, f"B{LV0 + i}", kind)
        inp(ws, f"C{LV0 + i}", v, PCT)
    put(ws, f"D{LV0}", "way = fraction of the way from today to the ATH; ath = ATH x (1 + value)")
    ST = LV0 + len(SETTINGS["levels"]) + 1
    put(ws, f"A{ST}", "Stress-case horizons T (years)", BOLD)
    for i, T in enumerate(SETTINGS["stress_T"]):
        inp(ws, f"{CL(2 + i)}{ST}", T, "0.00")
    put(ws, f"A{ST + 1}", "Rotation checkpoints T (years)", BOLD)
    for i, T in enumerate(SETTINGS["checkpoint_T"]):
        inp(ws, f"{CL(2 + i)}{ST + 1}", T, "0.00")
    put(ws, f"A{ST + 3}", "Example: to test a 30% first trim, change 'Rung 1 % of shares' to 30.0% and "
        "lower another rung so the rungs sum to 100%.")
    ws.column_dimensions["A"].width = 38
    for c in "BCDE":
        ws.column_dimensions[c].width = 14
    ws.column_dimensions[srcn].width = 70

    # ---------------- Ticker sheets ----------------
    SUM_ROWS = []
    for res in results:
        cfg = res["cfg"]
        t = cfg["etf"]
        I = IN[t]
        sh = wb.create_sheet(t)
        put(sh, "A1", f"{t}: {cfg['leverage']}x {cfg['underlying']}", TITLE)
        put(sh, "A2", ("PRICES ARE INTRADAY (market open when fetched). " if res["intraday"] else "")
            + cfg["note"])
        # Calibration (raw results)
        header(sh, 4, ["Calibration (raw results)", "Value"])
        cf, c = res["cal_full"], res["cal"]
        te, cr, cs = res["te"]
        cal_rows = [
            ("Overlap used for drag", f"{c['start']} to {c['end']} ({c['n']} days)", None),
            ("Beta of ETF on underlying", c["beta"], "0.000"), ("Correlation", c["corr"], "0.000"),
            ("Measured drag /yr", c["drag"], PCT), ("Drag standard error /yr", c["drag_se"], PCT),
            ("Full-overlap beta / drag", f"{cf['beta']:.3f} / {cf['drag']:.1%} ({cf['start']} on)", None),
            ("Synthetic vs real tracking error /yr", te, PCT),
            ("Real ETF return over overlap", cr, PCT), ("Synthetic return over overlap", cs, PCT),
            ("Underlying ATH date", str(res["ath_date"]), None),
            ("Splits found", "; ".join(sum(res["splits"].values(), [])) or "none", None),
            (f"Days underlying fell >= {1 / cfg['leverage']:.0%} (fund wipe-out)",
             ", ".join(f"{d} {x:.0%}" for d, x in res["wipe_days"]) or "none", None),
            (f"Days underlying fell >= {0.5 / cfg['leverage']:.0%} (fund -50%+)",
             ", ".join(f"{d} {x:.0%}" for d, x in res["big_days"]) or "none", None),
        ]
        for i, (lab, v, fmt) in enumerate(cal_rows):
            put(sh, f"A{5 + i}", lab)
            put(sh, f"B{5 + i}", v, BLACK, fmt, GREY)
        # Level mapping
        R0 = 20
        header(sh, R0, ["Level", "Kind", "Value", "Underlying target", "Gap from now", "Ceiling (no decay)"]
               + [f"Stress, LR vol, T={T}y" for T in SETTINGS["stress_T"]]
               + [f"Stress, 1y vol, T={T}y" for T in SETTINGS["stress_T"]])
        put(sh, f"A{R0 - 1}", "Level mapping. Ceiling = L_now x (S_target/S_now)^k. "
            "Stress = Ceiling x exp(-(k(k-1)/2 x vol^2 + drag) x T)", BOLD)
        LROW = {}
        for i in range(len(SETTINGS["levels"])):
            r_ = R0 + 1 + i
            LROW[i] = r_
            put(sh, f"A{r_}", f"=Inputs!$A${LV0 + i}", GREEN)
            put(sh, f"B{r_}", f"=Inputs!$B${LV0 + i}", GREEN)
            put(sh, f"C{r_}", f"=Inputs!$C${LV0 + i}", GREEN, PCT)
            put(sh, f"D{r_}", f'=IF(B{r_}="way",{I["S_now"]}+C{r_}*({I["ath"]}-{I["S_now"]}),{I["ath"]}*(1+C{r_}))',
                BLACK, USD)
            put(sh, f"E{r_}", f"=D{r_}/{I['S_now']}-1", BLACK, PCT)
            put(sh, f"F{r_}", f"={I['L_now']}*(D{r_}/{I['S_now']})^{I['k']}", BLACK, USD)
            for q, vk in enumerate(("vol_lr", "vol_1y")):
                for m in range(4):
                    col = CL(7 + q * 4 + m)
                    Tref = f"Inputs!${CL(2 + m)}${ST}"
                    put(sh, f"{col}{r_}",
                        f"=F{r_}*EXP(-({I['k']}*({I['k']}-1)/2*{I[vk]}^2+{I['drag']})*{Tref})", BLACK, USD)
        # Historical conditional
        H0 = R0 + len(SETTINGS["levels"]) + 4
        put(sh, f"A{H0 - 1}", f"Historical conditional distribution of {t} price when the underlying first "
            f"reaches each level ({res['hist_src']}). Start dates overlap heavily: "
            "treat as one history, not independent samples.", BOLD)
        header(sh, H0, ["Level", "Time to reach", "Episodes", "Median days", "P10", "P25", "P50 (median)",
                        "P75", "P90", "Start dates tested", "Share that ever reached"])
        rr = H0 + 1
        for i, lv in enumerate(res["levels"]):
            h = lv["hist"]
            for b in h["rows"]:
                put(sh, f"A{rr}", f"=A{LROW[i]}", BLACK)
                put(sh, f"B{rr}", b["bucket"], BLACK, None, GREY)
                put(sh, f"C{rr}", b["n"], BLACK, "#,##0", GREY)
                if b["n"]:
                    put(sh, f"D{rr}", b["med_days"], BLACK, "#,##0", GREY)
                    for q, key in enumerate(("p10", "p25", "p50", "p75", "p90")):
                        put(sh, f"{CL(5 + q)}{rr}", b[key], BLACK, USD, GREY)
                if b["bucket"] == "all":
                    put(sh, f"J{rr}", h["starts"], BLACK, "#,##0", GREY)
                    put(sh, f"K{rr}", f"=IF(J{rr}>0,C{rr}/J{rr},0)", BLACK, PCT)
                    lv["hist_all_row"] = rr
                rr += 1
        # Monte Carlo
        M0 = rr + 3
        put(sh, f"A{M0 - 1}", "Monte Carlo: 20-day block bootstrap of underlying daily returns, 10,000 paths, "
            "2 years, leveraged return = k x r - drag/252 each day (raw results).", BOLD)
        header(sh, M0, ["Run", "Level", "Underlying target", "P(hit) 3m", "P(hit) 6m", "P(hit) 1y", "P(hit) 2y",
                        "Median ETF price on hit day", "Hit day P25 (sessions)", "Hit day median", "Hit day P75",
                        "P(ETF touches ceiling) 2y"])
        MROW = {}
        rr = M0 + 1
        for name, lab in (("full", "Full history"), ("2y", "Last 2y only")):
            for i, st in enumerate(res["mc"][name]["stats"]):
                MROW[(name, i)] = rr
                put(sh, f"A{rr}", lab)
                put(sh, f"B{rr}", f"=A{LROW[i]}")
                put(sh, f"C{rr}", f"=D{LROW[i]}", BLACK, USD)
                for q, hk in enumerate(("3m", "6m", "1y", "2y")):
                    put(sh, f"{CL(4 + q)}{rr}", st["p"][hk], BLACK, PCT, GREY)
                if not math.isnan(st["med_L"]):
                    put(sh, f"H{rr}", st["med_L"], BLACK, USD, GREY)
                    for q in range(3):
                        put(sh, f"{CL(9 + q)}{rr}", float(st["hd_q"][q]), BLACK, "#,##0", GREY)
                put(sh, f"L{rr}", st["p_ceiling"], BLACK, PCT, GREY)
                rr += 1
        D0 = rr + 2
        header(sh, D0, ["Run", "P(-50% before rung 1)", "P(-75% before rung 1)", "P(-90% before rung 1)",
                        "P(touch cost basis) 2y", "P(ETF beats underlying) 1y", "Median ETF 1y multiple",
                        "Median underlying 1y multiple", "Mean ETF 1y multiple", "Mean underlying 1y multiple"])
        DROW = {}
        rr = D0 + 1
        for name, lab in (("full", "Full history"), ("2y", "Last 2y only")):
            d = res["down"][name]
            DROW[name] = rr
            put(sh, f"A{rr}", lab)
            for q, v in enumerate([d["dd"][0.5], d["dd"][0.75], d["dd"][0.9], d["p_cost"], d["p_L_beats_S_1y"]]):
                put(sh, f"{CL(2 + q)}{rr}", v, BLACK, PCT, GREY)
            for q, v in enumerate([d["med_L1"], d["med_S1"], d["mean_L1"], d["mean_S1"]]):
                put(sh, f"{CL(7 + q)}{rr}", v, BLACK, "0.00x", GREY)
            rr += 1
        # Sell ladder
        S0 = rr + 3
        put(sh, f"A{S0 - 1}", "Sell ladder. Sell price = stress-case price (long-run vol) at the median time "
            "the underlying takes to reach the level in the full-history run. Time stop = the date the stress "
            "price falls below the sell price (= that median time). Column P shows the simulated median ETF "
            "price on the hit day for comparison.", BOLD)
        header(sh, S0, ["Rung", "Underlying level", "Underlying target", "Sell price (ETF)", "% of shares",
                        "Shares", "Proceeds", "P&L vs cost", "P(touch) 2y, worse run", "P(touch) full run",
                        "P(touch) 2y run", "Expected window (P25-P75 touch date)", "Time stop (years)",
                        "Time stop date", "If not hit by the time stop", "MC median ETF price on hit (worse run)"])
        k = cfg["leverage"]
        rr = S0 + 1
        rung_rows = []
        for n, rg in enumerate(res["rungs"]):
            i = rg["level_idx"]
            put(sh, f"A{rr}", n + 1)
            put(sh, f"B{rr}", f"=A{LROW[i]}")
            put(sh, f"C{rr}", f"=D{LROW[i]}", BLACK, USD)
            put(sh, f"D{rr}", f"=F{LROW[i]}*EXP(-({I['k']}*({I['k']}-1)/2*{I['vol_lr']}^2+{I['drag']})"
                f"*J{MROW[('full', i)]}/Inputs!$B$9)", BLACK, USD)
            put(sh, f"P{rr}", f"=MIN(H{MROW[('full', i)]},H{MROW[('2y', i)]})", BLACK, USD)
            put(sh, f"E{rr}", f"={I['pct' + str(n + 1)]}", GREEN, PCT)
            put(sh, f"F{rr}", f"=ROUNDDOWN({I['shares']}*E{rr},0)", BLACK, "#,##0")
            put(sh, f"G{rr}", f"=F{rr}*D{rr}", BLACK, USD0)
            put(sh, f"H{rr}", f"=(D{rr}-{I['cost']})*F{rr}", BLACK, USD0)
            put(sh, f"I{rr}", f"=MIN(J{rr},K{rr})", BLACK, PCT)
            put(sh, f"J{rr}", rg["p_full"], BLACK, PCT, GREY)
            put(sh, f"K{rr}", rg["p_2y"], BLACK, PCT, GREY)
            w = rg["win_days"]
            if not np.isnan(w[0]):
                a = np.busday_offset(np.datetime64(res["asof"]), int(w[0]), roll="forward")
                b = np.busday_offset(np.datetime64(res["asof"]), int(w[1]), roll="forward")
                put(sh, f"L{rr}", f"{a} to {b}", BLACK, None, GREY)
            put(sh, f"M{rr}", f"=LN(F{LROW[i]}/D{rr})/({I['k']}*({I['k']}-1)/2*{I['vol_lr']}^2"
                f"+{I['drag']})", BLACK, "0.00")
            put(sh, f"N{rr}", f"=INT({G['asof']}+M{rr}*365)", BLACK, "yyyy-mm-dd")
            nxt = "rotate the rung's shares into the underlying" if n == len(res["rungs"]) - 1 else \
                f"move these shares to rung {n + 2}'s plan or rotate to the underlying"
            put(sh, f"O{rr}", f"Lower this rung to the stress price at that date, or {nxt}")
            rung_rows.append(rr)
            rr += 1
        tot = rr
        put(sh, f"A{tot}", "Total sold on ladder", BOLD)
        put(sh, f"F{tot}", f"=SUM(F{rung_rows[0]}:F{rung_rows[-1]})", BOLD, "#,##0")
        put(sh, f"G{tot}", f"=SUM(G{rung_rows[0]}:G{rung_rows[-1]})", BOLD, USD0)
        put(sh, f"H{tot}", f"=SUM(H{rung_rows[0]}:H{rung_rows[-1]})", BOLD, USD0)
        put(sh, f"A{tot + 1}", "Unallocated shares (rounding runner), valued at today's price")
        put(sh, f"F{tot + 1}", f"={I['shares']}-F{tot}", BLACK, "#,##0")
        put(sh, f"G{tot + 1}", f"=F{tot + 1}*{I['L_now']}", BLACK, USD0)
        put(sh, f"A{tot + 2}", "Position value today")
        put(sh, f"G{tot + 2}", f"={I['shares']}*{I['L_now']}", BLACK, USD0)
        put(sh, f"H{tot + 2}", f"=({I['L_now']}-{I['cost']})*{I['shares']}", BLACK, USD0)
        # Rotation
        Q0 = tot + 5
        put(sh, f"A{Q0}", "Rotation trigger (median outcome, not mean)", BOLD)
        put(sh, f"A{Q0 + 1}", "Vol used (higher of since-2016 and 1y)")
        put(sh, f"B{Q0 + 1}", f"=MAX({I['vol_lr']},{I['vol_1y']})", BLACK, PCT)
        put(sh, f"A{Q0 + 2}", "Hurdle: underlying arithmetic return/yr the ETF needs to beat the underlying "
            "= (k+1)/2 x vol^2 + drag/(k-1)")
        put(sh, f"B{Q0 + 2}", f"=({I['k']}+1)/2*B{Q0 + 1}^2+{I['drag']}/({I['k']}-1)", BLACK, PCT)
        header(sh, Q0 + 3, ["Checkpoint", "Date", "Underlying must be at or above", "Gap from now"])
        for m in range(len(SETTINGS["checkpoint_T"])):
            r_ = Q0 + 4 + m
            Tref = f"Inputs!${CL(2 + m)}${ST + 1}"
            put(sh, f"A{r_}", f"={Tref}", GREEN, "0.00")
            put(sh, f"B{r_}", f"={G['asof']}+A{r_}*365", BLACK, "yyyy-mm-dd")
            put(sh, f"C{r_}", f"={I['S_now']}*EXP((B{Q0 + 2}-B{Q0 + 1}^2/2)*A{r_})", BLACK, USD)
            put(sh, f"D{r_}", f"=C{r_}/{I['S_now']}-1", BLACK, PCT)
        put(sh, f"A{Q0 + 4 + len(SETTINGS['checkpoint_T'])}",
            "Below the checkpoint on that date = the underlying is compounding under the hurdle; the median "
            "outcome now favours holding the underlying. Rotate.")
        # Breakeven
        B0 = Q0 + 7 + len(SETTINGS["checkpoint_T"])
        put(sh, f"A{B0}", "Cost-basis line", BOLD)
        put(sh, f"A{B0 + 1}", "ETF cost basis")
        put(sh, f"B{B0 + 1}", f"={I['cost']}", GREEN, USD)
        put(sh, f"A{B0 + 2}", "ETF move to breakeven")
        put(sh, f"B{B0 + 2}", f"={I['cost']}/{I['L_now']}-1", BLACK, PCT)
        put(sh, f"A{B0 + 3}", "Underlying level at breakeven, no decay = S_now x (cost/L_now)^(1/k)")
        put(sh, f"B{B0 + 3}", f"={I['S_now']}*({I['cost']}/{I['L_now']})^(1/{I['k']})", BLACK, USD)
        put(sh, f"A{B0 + 4}", "Same, after 1y of stress decay")
        put(sh, f"B{B0 + 4}", f"=B{B0 + 3}*EXP(({I['k']}-1)/2*MAX({I['vol_lr']},{I['vol_1y']})^2+{I['drag']}/{I['k']})",
            BLACK, USD)
        put(sh, f"A{B0 + 5}", "P(ETF touches cost basis within 2y): full run / last-2y run")
        put(sh, f"B{B0 + 5}", f"=E{DROW['full']}", BLACK, PCT)
        put(sh, f"C{B0 + 5}", f"=E{DROW['2y']}", BLACK, PCT)
        sh.column_dimensions["A"].width = 44
        for col in range(2, 16):
            sh.column_dimensions[CL(col)].width = 15
        sh.column_dimensions["B"].width = 26
        sh.column_dimensions["L"].width = 24
        sh.column_dimensions["O"].width = 60
        sh.freeze_panes = "B4"
        SUM_ROWS.append((t, rung_rows, tot))

    # ---------------- Summary ----------------
    sm = wb.create_sheet("Summary", 1)
    put(sm, "A1", "Sell ladder summary (all positions)", TITLE)
    put(sm, "A2", "Every number links to the ticker sheets. Probabilities are from resampled history, "
        "not forecasts.")
    header(sm, 4, ["ETF", "Rung", "Underlying level", "Underlying target", "Sell price (ETF)", "Shares",
                   "Proceeds", "P&L vs cost", "P(touch) 2y, worse run", "Time stop date"])
    rr = 5
    tot_rows = []
    for t, rows, tot in SUM_ROWS:
        first = rr
        for n, src in enumerate(rows):
            put(sm, f"A{rr}", t)
            put(sm, f"B{rr}", f"='{t}'!A{src}", GREEN)
            put(sm, f"C{rr}", f"='{t}'!B{src}", GREEN)
            put(sm, f"D{rr}", f"='{t}'!C{src}", GREEN, USD)
            put(sm, f"E{rr}", f"='{t}'!D{src}", GREEN, USD)
            put(sm, f"F{rr}", f"='{t}'!F{src}", GREEN, "#,##0")
            put(sm, f"G{rr}", f"='{t}'!G{src}", GREEN, USD0)
            put(sm, f"H{rr}", f"='{t}'!H{src}", GREEN, USD0)
            put(sm, f"I{rr}", f"='{t}'!I{src}", GREEN, PCT)
            put(sm, f"J{rr}", f"='{t}'!N{src}", GREEN, "yyyy-mm-dd")
            rr += 1
        put(sm, f"A{rr}", f"{t} total", BOLD)
        for col, fmt in (("F", "#,##0"), ("G", USD0), ("H", USD0)):
            put(sm, f"{col}{rr}", f"=SUM({col}{first}:{col}{rr - 1})", BOLD, fmt)
        tot_rows.append(rr)
        rr += 2
    put(sm, f"A{rr}", "Grand total", BOLD)
    for col, fmt in (("G", USD0), ("H", USD0)):
        put(sm, f"{col}{rr}", "=" + "+".join(f"{col}{x}" for x in tot_rows), BOLD, fmt)
    put(sm, f"A{rr + 1}", "Value of all three positions today")
    put(sm, f"G{rr + 1}", "=" + "+".join(f"{IN[t]['shares']}*{IN[t]['L_now']}" for t, _, _ in SUM_ROWS),
        BLACK, USD0)
    sm.column_dimensions["A"].width = 16
    for col in "BCDEFGHIJ":
        sm.column_dimensions[col].width = 17
    for s in wb.worksheets:
        for row in s.iter_rows():
            for c in row:
                if c.font and c.font.name != F:
                    c.font = Font(name=F, bold=c.font.bold, color=c.font.color, size=c.font.size)
    wb.save(path)


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------
def bday(asof, n):
    return str(np.busday_offset(np.datetime64(asof), int(n), roll="forward"))


def summary_md(results, path, flags):
    L = []
    asof = results[0]["asof"]
    intr = any(r["intraday"] for r in results)
    L.append(f"# Leveraged ETF sell targets ({asof}{', INTRADAY prices' if intr else ''})\n")
    L.append("Model output describes resampled history. It is not a forecast.\n")
    L.append("## Recommendation\n")
    L.append("Place the ladder below as GTC limit sells on the leveraged ETF, re-run weekly, and rotate to "
             "the underlying when a checkpoint fails. Ranked by how much the leverage is costing you:\n")
    L.append("| ETF | Vol drag + fees /yr (long-run vol) | Hurdle: underlying return/yr to beat holding it | "
             "P(ETF beats underlying over 1y), worse run | Verdict |")
    L.append("|---|---|---|---|---|")
    for r in sorted(results, key=lambda r: -r["hurdle"]):
        k = r["cfg"]["leverage"]
        dec = k * (k - 1) / 2 * r["vol"]["lr"] ** 2 + r["drag"]
        pb = min(r["down"]["full"]["p_L_beats_S_1y"], r["down"]["2y"]["p_L_beats_S_1y"])
        v = ("Leverage is a losing bet on the median path; trim early or rotate now" if pb < 0.25 else
             "Leverage needs a fast move; sell into strength" if pb < 0.45 else "Ladder is reasonable")
        L.append(f"| {r['cfg']['etf']} | {dec:.0%} | {r['hurdle']:.0%} | {pb:.0%} | {v} |")
    L.append("")
    L.append("## Action items\n")
    n = 1
    for r in results:
        g = r["rungs"][0]
        sh = math.floor(r["cfg"]["shares"] * g["pct"])
        prices = ", ".join(f"${x['price']:.2f}" for x in r["rungs"])
        L.append(f"{n}. **{r['cfg']['etf']}**: place {len(r['rungs'])} GTC limit sells "
                 f"({prices}), first rung {sh:,} shares. "
                 f"If the underlying is below ${r['S_now'] * math.exp((r['hurdle'] - r['sig'] ** 2 / 2) * 0.25):.2f} on "
                 f"{(dt.date.fromisoformat(str(r['asof'])) + dt.timedelta(days=91)).isoformat()}, rotate to {r['cfg']['underlying']}.")
        n += 1
    L.append(f"{n}. Re-run `python main.py` each week (and after any 10%+ move); rungs and time stops move with "
             "price, vol and drag.")
    L.append(f"{n + 1}. Decide on COHX and AAOX before the Feb 2027 earnings prints: a gap through earnings is "
             "the main way a 2x fund loses half its value in a day.")
    L.append("")
    L.append("## Sell ladder\n")
    L.append("| ETF | Rung | Underlying level | Underlying target | Sell price | Shares | Proceeds | "
             "P(touch) 2y | Time stop |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    grand = 0.0
    for r in results:
        k = r["cfg"]["leverage"]
        tot = 0.0
        for n, rg in enumerate(r["rungs"], 1):
            lv = r["levels"][rg["level_idx"]]
            sh = math.floor(r["cfg"]["shares"] * rg["pct"])
            proc = sh * rg["price"]
            tot += proc
            stop = (dt.date.fromisoformat(str(asof)) + dt.timedelta(days=rg["T_stop"] * 365)).isoformat()
            L.append(f"| {r['cfg']['etf']} | {n} | {lv['label']} | ${lv['S']:.2f} | **${rg['price']:.2f}** | "
                     f"{sh:,} | ${proc:,.0f} | {min(rg['p_full'], rg['p_2y']):.0%} | {stop} |")
        grand += tot
        L.append(f"| **{r['cfg']['etf']} total** | | | | | | **${tot:,.0f}** | | |")
    L.append(f"| **All three** | | | | | | **${grand:,.0f}** | | |\n")
    L.append("P(touch) is the worse of the full-history and last-2-year Monte Carlo runs. Time stop is the "
             "date the stress-case price falls below the rung if the underlying has not got there yet.\n")
    L.append("## Calibration\n")
    L.append("| ETF | Beta | Corr | Drag /yr (SE) | Synthetic TE /yr | Vol 3m / 1y / since 2016 | ETF now | "
             "Underlying now | ATH |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for r in results:
        c, v = r["cal"], r["vol"]
        L.append(f"| {r['cfg']['etf']} | {c['beta']:.2f} | {c['corr']:.3f} | {c['drag']:.1%} "
                 f"(+/-{c['drag_se']:.1%}) | {r['te'][0]:.1%} | {v['3m']:.0%} / {v['1y']:.0%} / {v['lr']:.0%} | "
                 f"${r['L_now']:.2f} | ${r['S_now']:.2f} | ${r['ath']:.2f} ({r['ath_date']}) |")
    L.append("\n## Level mapping (ceiling vs history vs simulation)\n")
    for r in results:
        L.append(f"### {r['cfg']['etf']}\n")
        L.append("| Level | Underlying | Ceiling | Hist median | Hist P10-P90 | MC P(hit 1y) | MC P(hit 2y) "
                 "full / 2y | MC median price on hit |")
        L.append("|---|---|---|---|---|---|---|---|")
        for i, lv in enumerate(r["levels"]):
            a = lv["hist"]["rows"][-1]
            hm = f"${a['p50']:.2f}" if a["n"] else "n/a"
            hr = f"${a['p10']:.2f}-${a['p90']:.2f}" if a["n"] else "n/a"
            sf, s2 = r["mc"]["full"]["stats"][i], r["mc"]["2y"]["stats"][i]
            L.append(f"| {lv['label']} | ${lv['S']:.2f} | ${lv['ceiling']:.2f} | {hm} | {hr} | "
                     f"{sf['p']['1y']:.0%} | {sf['p']['2y']:.0%} / {s2['p']['2y']:.0%} | "
                     f"${min(sf['med_L'], s2['med_L']):.2f} |")
        L.append("")
    L.append("## Rotation and downside\n")
    L.append("| ETF | Hurdle (underlying return/yr needed) | Underlying needed at 3m / 6m / 1y | "
             "P(ETF beats underlying, 1y) full / 2y | P(-50% before rung 1) | P(-75%) | Cost basis touch 2y |")
    L.append("|---|---|---|---|---|---|---|")
    for r in results:
        sig, h, S0 = r["sig"], r["hurdle"], r["S_now"]
        cps = " / ".join(f"${S0 * math.exp((h - sig ** 2 / 2) * T):.2f}" for T in SETTINGS["checkpoint_T"])
        df, d2 = r["down"]["full"], r["down"]["2y"]
        L.append(f"| {r['cfg']['etf']} | {h:.0%} | {cps} | {df['p_L_beats_S_1y']:.0%} / {d2['p_L_beats_S_1y']:.0%} | "
                 f"{max(df['dd'][0.5], d2['dd'][0.5]):.0%} | {max(df['dd'][0.75], d2['dd'][0.75]):.0%} | "
                 f"{max(df['p_cost'], d2['p_cost']):.0%} |")
    L.append("\nDownside columns show the worse of the two runs.\n")
    L.append("## Fund and event risk\n")
    for i, f in enumerate(RISK_NOTES, 1):
        L.append(f"{i}. {f}")
    L.append("")
    L.append("## Flags\n")
    for i, f in enumerate(flags, 1):
        L.append(f"{i}. {f}")
    L.append("\n## Data log\n")
    for m in LOG:
        L.append(f"- {m.strip()}")
    open(path, "w").write("\n".join(L) + "\n")


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", action="store_true", help="re-use cache/*.json instead of fetching")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    rng = np.random.default_rng(SETTINGS["seed"])
    tickers = sorted({p[k] for p in POSITIONS for k in ("etf", "underlying")})
    data = {}
    for t in tickers:
        data[t] = fetch(t, a.cache)
        d = data[t]
        log(f"{t}: {len(d['df'])} bars {d['df'].index[0].date()} to {d['last_date']}, last ${d['last']:.2f}"
            f"{' (INTRADAY)' if d['intraday'] else ''}")
    results = []
    for cfg in POSITIONS:
        log(f"Running {cfg['etf']} ...")
        results.append(run_pair(cfg, data, rng))
    flags = []
    for r in results:
        t = r["cfg"]["etf"]
        if r["intraday"]:
            flags.append(f"{t}: prices are intraday ({r['asof']}); re-run after the close for settled numbers.")
        if r["wipe_days"]:
            flags.append(f"{t}: the underlying had {len(r['wipe_days'])} day(s) that would have wiped out a "
                         f"{r['cfg']['leverage']}x fund: {r['wipe_days']}")
        if r["thin_ladder"]:
            flags.append(f"{t}: fewer than 3 levels have a >= {SETTINGS['min_rung_prob']:.0%} two-year hit "
                         "probability, so the ladder is thin.")
        if r["cal"]["drag_se"] > abs(r["cal"]["drag"]) / 2:
            flags.append(f"{t}: drag {r['cal']['drag']:.1%} has a standard error of "
                         f"{r['cal']['drag_se']:.1%} (short overlap); treat it as rough.")
    for r in results:
        r["fan"] = chart(r)
    workbook(results, os.path.join(OUT, "sell_targets.xlsx"))
    summary_md(results, os.path.join(OUT, "summary.md"), flags)
    json.dump({r["cfg"]["etf"]: {"L_now": r["L_now"], "S_now": r["S_now"], "ath": r["ath"],
                                 "drag": r["drag"], "rungs": [{"price": g["price"], "p_full": g["p_full"],
                                                               "p_2y": g["p_2y"], "T_stop": g["T_stop"],
                                                               "level": r["levels"][g["level_idx"]]["label"]}
                                                              for g in r["rungs"]]}
               for r in results}, open(os.path.join(OUT, "run.json"), "w"), indent=1, default=str)
    log("Done: output/sell_targets.xlsx, output/summary.md, output/*_fan.png")


if __name__ == "__main__":
    main()
