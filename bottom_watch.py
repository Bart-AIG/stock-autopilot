"""Bottom watch: is the low of a QQQ / SPY selloff in, and is the rebound holding?

Ryan, live turns 2026-11-20: "set up a scheduled task that can run a few times a day to
evaluate if the bottom is in by probability check the variables that the highest
correlations. it should monitor the bottom and the rebound".

Pure functions, no network. Bars are oldest-first dicts of lists: d (YYYY-MM-DD), o, h, l,
c, v. The backtest (bottom_backtest.py -> bottom_results.md) and the scheduled job
(bottom_watch_run.py) both call scan() below, so the live reading is computed by the code
that was tested.

Everything is on CLOSING prices (a bad intraday print or a flash crash cannot move it, and
the live job and the backtest use different data vendors). A selloff ("episode") starts when
the close is 10% (QQQ) or 8% (SPY) under the 252-session closing high. It ends when the close
is back within 3% of that high or makes a new 252-session closing high. The question on every
day inside one: has the lowest close of the episode already printed?
"""
from __future__ import annotations

import math

YEAR = 252
TH_START = {"QQQ": 0.10, "SPY": 0.08}   # a close this far under the 252-session closing high starts an episode
RECOVER = 0.03           # close within 3% of the old high ends it
BOUNCE = {"SPY": 0.05, "QQQ": 0.07}      # a rebound this big that then fails = one more leg down
FTD_MIN = {"SPY": 0.0125, "QQQ": 0.015}  # follow-through day: this gain on rising volume, day 4+


def _rsi(c, n):
    out = [None] * len(c)
    if len(c) <= n:
        return out
    g = l = 0.0
    for i in range(1, n + 1):
        ch = c[i] - c[i - 1]
        g += max(ch, 0.0)
        l += max(-ch, 0.0)
    g /= n
    l /= n
    out[n] = 100.0 if l == 0 else 100 - 100 / (1 + g / l)
    for i in range(n + 1, len(c)):
        ch = c[i] - c[i - 1]
        g = (g * (n - 1) + max(ch, 0.0)) / n
        l = (l * (n - 1) + max(-ch, 0.0)) / n
        out[i] = 100.0 if l == 0 else 100 - 100 / (1 + g / l)
    return out


def _aligned(dates, series):
    """series: {date: value}. Forward-filled list aligned to dates (None before the first)."""
    out, last = [], None
    for d in dates:
        if series and d in series and series[d] is not None:
            last = series[d]
        out.append(last)
    return out


def scan(sym, B, vix=None, hyg=None, ief=None, rsp=None, spy=None):
    """Walk the bars once. Returns (rows, episodes).

    rows: one dict per day inside an episode, with every candidate variable measured at that
    day's close (nothing from the future). episodes: dicts with peak, start, end and the final
    low; an episode still open at the last bar has end_i None and its rows have y None.
    """
    d, o, h, l, c, v = B["d"], B["o"], B["h"], B["l"], B["c"], B["v"]
    n = len(c)
    cs = [0.0]
    for x in c:
        cs.append(cs[-1] + x)
    sma = lambda k, i: (cs[i + 1] - cs[i + 1 - k]) / k if i + 1 >= k else None
    rsi14, rsi2 = _rsi(c, 14), _rsi(c, 2)
    vs = [0.0]
    for x in v:
        vs.append(vs[-1] + (x or 0.0))
    volr = [None] * n
    for i in range(50, n):
        base = (vs[i] - vs[i - 50]) / 50
        volr[i] = (v[i] / base) if base and v[i] is not None else None
    tr = [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, n)]
    ts = [0.0]
    for x in tr:
        ts.append(ts[-1] + x)
    atrp = [((ts[i + 1] - ts[i - 19]) / 20) / c[i] if i >= 19 else None for i in range(n)]
    c2 = [0.0]
    for x in c:
        c2.append(c2[-1] + x * x)
    bbz, bbw = [None] * n, [None] * n          # Bollinger (20, 2): position in sd from the middle band; band width
    for i in range(19, n):
        m = (cs[i + 1] - cs[i - 19]) / 20
        sd = math.sqrt(max(0.0, (c2[i + 1] - c2[i - 19]) / 20 - m * m))
        if sd > 0:
            bbz[i], bbw[i] = (c[i] - m) / sd, 4 * sd / m
    vx = _aligned(d, vix)
    ratio = None
    if hyg and ief:
        hy, ie = _aligned(d, hyg), _aligned(d, ief)
        ratio = [(a / b) if a and b else None for a, b in zip(hy, ie)]
    rs, sp = (_aligned(d, rsp), _aligned(d, spy)) if rsp and spy else (None, None)

    rows, eps, ep = [], [], None

    def update(e, j):
        if e["runlow"] is None or c[j] < e["runlow"]:
            if e["runlow"] is not None and e["maxc"] >= e["runlow"] * (1 + BOUNCE[sym]):
                e["legs"] += 1
                e["prev"] = {"rsi": rsi14[e["low_i"]], "vix": vx[e["low_i"]], "low": e["runlow"],
                             "volr": volr[e["low_i"]], "i": e["low_i"]}
            if e["low_i"] is not None and bbz[e["low_i"]] is not None and bbz[e["low_i"]] <= -2:
                e["bb_out_before"] = True          # an earlier low closed under the lower band
            e["runlow"], e["low_i"], e["maxc"], e["ftd"], e["zmax"] = c[j], j, c[j], 0, bbz[j]
        else:
            e["maxc"] = max(e["maxc"], c[j])
            if bbz[j] is not None and (e["zmax"] is None or bbz[j] > e["zmax"]):
                e["zmax"] = bbz[j]
            if (j - e["low_i"] >= 3 and c[j] / c[j - 1] - 1 >= FTD_MIN[sym]
                    and v[j] is not None and v[j - 1] is not None and v[j] > v[j - 1]):
                e["ftd"] = 1
        if vx[j] is not None and (e["vixpk"] is None or vx[j] >= e["vixpk"]):
            e["vixpk"], e["vixpk_i"] = vx[j], j
        if volr[j] is not None and (e["climax"] is None or volr[j] >= e["climax"]):
            e["climax"], e["climax_i"] = volr[j], j
        if bbz[j] is not None and bbz[j] <= -2:
            e["bb_out_i"] = j
        if bbw[j] is not None and (e["bbw_max"] is None or bbw[j] >= e["bbw_max"]):
            e["bbw_max"] = bbw[j]

    def feats(e, j):
        low, li, pk = e["runlow"], e["low_i"], e["peak"]
        f = {"sym": sym, "date": d[j], "i": j, "ep": e["k"], "y": None,
             "close": c[j], "runlow": low, "low_date": d[li], "peak": pk, "peak_date": d[e["peak_i"]]}
        f["reb"] = c[j] / low - 1
        f["days"] = j - li
        f["retr"] = (c[j] - low) / (pk - low) if pk > low else 0.0
        f["ddlow"] = low / pk - 1
        f["ddclose"] = c[j] / pk - 1
        f["legs"] = e["legs"]
        f["sess_pk_low"] = li - e["peak_i"]
        f["speed"] = -f["ddlow"] / max(1, f["sess_pk_low"]) * 100          # % lost per session to the low
        f["maxreb"] = e["maxc"] / low - 1
        f["giveback"] = c[j] / e["maxc"] - 1
        a = atrp[li] or atrp[j]
        f["reb_atr"] = f["reb"] / a if a else None
        for k in (5, 10, 20, 50, 200):
            m = sma(k, j)
            f[f"above{k}"] = None if m is None else int(c[j] > m)
            f[f"dist{k}"] = None if m is None else c[j] / m - 1
        m200, m200b = sma(200, j), sma(200, j - 20)
        f["slope200"] = (m200 / m200b - 1) if m200 and m200b else None      # 200-day average vs 20 sessions ago
        f["sess_pk"] = j - e["peak_i"]
        f["rsi14"], f["rsi2"], f["rsi_low"] = rsi14[j], rsi2[j], rsi14[li]
        pv = e["prev"]
        f["rsi_div"] = (rsi14[li] - pv["rsi"]) if pv and pv["rsi"] is not None and rsi14[li] is not None else 0.0
        rng = h[li] - l[li]
        f["lowday_loc"] = min(1.0, max(0.0, (c[li] - l[li]) / rng)) if rng > 0 else 0.5
        f["lowday_volr"] = volr[li]
        w = [x for x in volr[max(0, li - 4):li + 1] if x is not None]
        f["climax5"] = max(w) if w else None
        f["climax_ep"] = e["climax"]
        f["vol_div"] = (volr[li] / e["climax"]) if volr[li] and e["climax"] else None
        f["climax_age"] = (j - e["climax_i"]) if e["climax"] is not None else None
        up = sum(v[q] for q in range(j - 9, j + 1) if c[q] > c[q - 1] and v[q])
        dn = sum(v[q] for q in range(j - 9, j + 1) if c[q] < c[q - 1] and v[q])
        f["updn10"] = math.log((up + 1) / (dn + 1))
        f["ftd"] = e["ftd"]
        f["bb_z"], f["bb_z_low"], f["bb_width"], f["bb_zmax"] = bbz[j], bbz[li], bbw[j], e["zmax"]
        f["bb_width_off"] = (bbw[j] / e["bbw_max"] - 1) if bbw[j] and e["bbw_max"] else None
        f["bb_out_age"] = (j - e["bb_out_i"]) if e["bb_out_i"] is not None else None
        f["bb_reentry"] = int(e["bb_out_i"] is not None and bbz[j] is not None and bbz[j] > -2)
        f["bb_w_bottom"] = int(e["bb_out_before"] and bbz[li] is not None and bbz[li] > -2)
        if vx[j] is not None and e["vixpk"]:
            f["vix"] = vx[j]
            f["vix_peak"] = e["vixpk"]
            f["vix_off"] = vx[j] / e["vixpk"] - 1
            f["vix_low"] = vx[li]
            f["vix_div"] = (vx[li] / e["vixpk"] - 1) if vx[li] else None
            f["vix_peak_age"] = j - e["vixpk_i"]
            w = [x for x in vx[j - 19:j + 1] if x is not None]
            f["vix_vs20"] = vx[j] / (sum(w) / len(w)) - 1 if w else None
            f["vix_prevleg"] = (vx[li] - pv["vix"]) if pv and pv["vix"] and vx[li] else 0.0
        else:
            for k in ("vix", "vix_peak", "vix_off", "vix_low", "vix_div", "vix_peak_age", "vix_vs20", "vix_prevleg"):
                f[k] = None
        if ratio and ratio[j] and ratio[j - 5] and ratio[j - 20]:
            f["hy5"], f["hy20"] = ratio[j] / ratio[j - 5] - 1, ratio[j] / ratio[j - 20] - 1
        else:
            f["hy5"] = f["hy20"] = None
        if rs and rs[j] and rs[j - 20] and sp[j] and sp[j - 20]:
            f["ew_rel20"] = (rs[j] / rs[j - 20]) - (sp[j] / sp[j - 20])
        else:
            f["ew_rel20"] = None
        return f

    for i in range(YEAR, n):
        if ep is None:
            w0 = i - YEAR + 1
            hi = max(c[w0:i + 1])
            if c[i] / hi - 1 <= -TH_START[sym]:
                pk_i = max(range(w0, i + 1), key=lambda q: (c[q], q))
                ep = {"sym": sym, "k": len(eps), "peak_i": pk_i, "peak": c[pk_i], "start_i": i,
                      "runlow": None, "low_i": None, "maxc": None, "ftd": 0, "legs": 0, "prev": None,
                      "vixpk": None, "vixpk_i": None, "climax": None, "climax_i": None, "end_i": None,
                      "bb_out_i": None, "bb_out_before": False, "bbw_max": None, "zmax": None}
                for j in range(pk_i + 1, i):
                    update(ep, j)
            else:
                continue
        update(ep, i)
        rows.append(feats(ep, i))
        if c[i] >= ep["peak"] * (1 - RECOVER) or c[i] >= max(c[i - YEAR:i]):
            ep["end_i"] = i
            for r in reversed(rows):
                if r["ep"] != ep["k"] or r["sym"] != sym:
                    break
                r["y"] = int(r["i"] >= ep["low_i"])
            eps.append(ep)
            ep = None
    if ep is not None:
        eps.append(ep)
    return rows, eps
