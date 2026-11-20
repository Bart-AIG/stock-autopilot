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
                e["leg_i"] = j
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
                      "bb_out_i": None, "bb_out_before": False, "bbw_max": None, "zmax": None, "leg_i": None}
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


# ------------------------------------------------------------------ the live reading

BANDS = ((0.25, "Low not in"), (0.50, "Low unlikely in"), (0.70, "Toss-up"),
         (0.85, "Low probably in"), (9.9, "Low very likely in"))
STAGE_TEXT = {"NEW LOW": "New closing low", "FAILED REBOUND": "Rebound failed, new closing low",
              "REBOUND": "Rebounding", "RETEST": "Retesting the low", "RECOVERED": "Recovered",
              "NO SELLOFF": "No selloff open"}
LIVE_TEXT = {"NEW LOW": "Trading under the lowest close so far",
             "FAILED REBOUND": "Rebound failing, trading under the lowest close so far"}
RETEST_MIN, RETEST_KEEP = 0.04, 0.35     # a rebound of 4%+ that has given back 65% of itself is a retest
BAND_MOVE = 0.05                         # a band change is pushed only after a 5-point move since the last push
_MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def band(p):
    return next(i for i, (hi, _) in enumerate(BANDS) if p < hi)


def _interp(x, xs, ys):
    if x <= xs[0]:
        return ys[0]
    for i in range(1, len(xs)):
        if x <= xs[i]:
            return ys[i - 1] + (x - xs[i - 1]) / (xs[i] - xs[i - 1]) * (ys[i] - ys[i - 1])
    return ys[-1]


def probability(model, f):
    """(chance 0-1 that the lowest close of the selloff is already in, basis).

    f is one row from scan(). basis is "full", or "no_vix" when there is no VIX reading and
    the two-variable fallback was used. The raw logistic output is mapped through the
    calibration knots, so a stated 70% was right about 70% of the time out of sample.
    """
    use, basis = model, "full"
    if f.get("vix_off") is None:
        use, basis = model["fallback"], "no_vix"
    z = use["intercept"]
    for name, mu, sd, beta in zip(use["features"], use["mean"], use["sd"], use["beta"]):
        x = f.get(name)
        if x is None:
            return None, "missing_" + name
        lo, hi = model["clip"].get(name, (-1e18, 1e18))
        z += beta * (min(hi, max(lo, x)) - mu) / sd
    raw = 1 / (1 + math.exp(-z))
    return _interp(raw, [k[0] for k in use["calibration"]], [k[1] for k in use["calibration"]]), basis


def _need(cp, f, r):
    """What has to happen for an unmet checkpoint, in plain words."""
    k, x = cp["f"], cp["x"]
    if k == "vix_off" and f.get("vix_peak"):
        return f"VIX at or under {f['vix_peak'] * (1 + x):.1f}"
    if k in ("above20", "above50", "above200"):
        m = r.get("sma" + k[5:])
        return f"close above ${m:,.2f}" if m else ""
    if k == "retr":
        return f"close at or above ${f['runlow'] + x * (f['peak'] - f['runlow']):,.2f}"
    if k == "reb":
        return f"close at or above ${f['runlow'] * (1 + x):,.2f}"
    if k == "rsi14":
        return f"RSI(14) at {x:.0f} or more (now {f['rsi14']:.0f})"
    if k == "days":
        return f"{x:.0f} sessions without a new closing low (now {f['days']})"
    return ""


def reading(sym, B, vix, model):
    """Today's reading for one index. The last bar of B is the bar judged; during the session
    the live price stands in as its close, so an intraday reading is provisional."""
    rows, eps = scan(sym, B, vix)
    d, c = B["d"], B["c"]
    last = len(c) - 1
    hi = max(c[max(0, last - YEAR + 1):last + 1])
    sma = lambda k: (sum(c[last - k + 1:last + 1]) / k) if last + 1 >= k else None
    r = {"sym": sym, "date": d[last], "close": c[last], "high252": hi, "from_high": c[last] / hi - 1,
         "starts_at": hi * (1 - TH_START[sym]), "sma20": sma(20), "sma50": sma(50), "sma200": sma(200),
         "stage": "NO SELLOFF", "open": False}
    e = eps[-1] if eps else None
    if e is None or (e["end_i"] is not None and e["end_i"] != last):
        return r
    f = rows[-1]
    p, basis = probability(model, f)
    if e["end_i"] == last:
        stage = "RECOVERED"
    elif f["days"] == 0:
        stage = "FAILED REBOUND" if e.get("leg_i") == last else "NEW LOW"
    elif f["maxreb"] >= RETEST_MIN and f["reb"] <= f["maxreb"] * RETEST_KEEP:
        stage = "RETEST"
    else:
        stage = "REBOUND"
    checks = []
    for cp in model.get("checkpoints", []):
        x = f.get(cp["f"])
        met = None if x is None else (x >= cp["x"] if cp["op"] == ">=" else x <= cp["x"])
        checks.append({"label": cp["label"], "hit": cp["hit"], "met": met, "need": "" if met else _need(cp, f, r)})
    trend = [(q["date"], probability(model, q)[0]) for q in [q for q in rows if q["ep"] == e["k"]][-8:]]
    r.update({"open": e["end_i"] is None, "stage": stage, "prob": p, "basis": basis,
              "band": band(p) if p is not None else None,
              "peak": f["peak"], "peak_date": f["peak_date"], "low": f["runlow"], "low_date": f["low_date"],
              "days": f["days"], "reb": f["reb"], "maxreb": f["maxreb"], "giveback": f["giveback"],
              "retr": f["retr"], "legs": f["legs"], "ddlow": f["ddlow"], "ddclose": f["ddclose"],
              "sess_pk": f["sess_pk"], "rsi14": f["rsi14"], "dist200": f["dist200"],
              "vix": f.get("vix"), "vix_peak": f.get("vix_peak"),
              "vix_peak_date": d[e["vixpk_i"]] if e.get("vixpk_i") is not None else None,
              "vix_off": f.get("vix_off"), "checks": checks, "trend": trend})
    return r


# ------------------------------------------------------------------ Ryan's buy-back levels

def plan_status(plan, bars, vix, since, provisional):
    """Where the buy-back levels stand (bottom_watch_plan.json). Advisory: Ryan places every order.

    bars: {"QQQ": B, "SPY": B}. vix: {"d", "h", "c"} oldest first. since: first date the VIX spike
    may count from (the high of the selloff). provisional: the last bar is a live price, so "closes
    in the top half of the day's range" and "closes above" are not final for that bar.
    Each item: name, text (the level in words), state (not_reached / reached / met / met_provisional),
    date, and gap (how far away, as text).
    """
    out = []
    vd = [(dd, (hh if hh is not None else cc)) for dd, hh, cc in zip(vix["d"], vix["h"], vix["c"]) if dd >= since and cc is not None]

    def vmax(day):
        return max((x for dd, x in vd if dd <= day), default=0.0)

    vclose = dict(zip(vix["d"], vix["c"]))
    last_day = max(B["d"][-1] for B in bars.values())
    for st in plan.get("steps", []):
        reached = met = None
        for sym, B in bars.items():
            if sym not in st:
                continue
            ri = next((i for i in range(len(B["d"])) if B["d"][i] >= plan["set"] and B["l"][i] <= st[sym]), None)
            if ri is None:
                continue
            if reached is None or B["d"][ri] < reached[0]:
                reached = (B["d"][ri], sym)
            mi = next((i for i in range(ri, len(B["d"])) if B["c"][i] >= (B["h"][i] + B["l"][i]) / 2
                       and vmax(B["d"][i]) >= plan["vix_spike"]), None)
            if mi is not None and (met is None or B["d"][mi] < met[0]):
                met = (B["d"][mi], sym)
        levels = " or ".join(f"{s} ${st[s]:,.0f}" for s in bars if s in st)
        item = {"key": f"{plan['set']}:{st['name']}", "name": st["name"], "text": levels, "amount": st.get("amount", ""), "date": None}
        if met:
            item["state"] = "met_provisional" if (provisional and met[0] == last_day) else "met"
            item["date"], item["sym"] = met
        elif reached:
            item["state"] = "reached"
            item["date"], item["sym"] = reached
            spike = vmax(last_day)
            item["gap"] = (f"VIX has not spiked above {plan['vix_spike']} (high so far {spike:.1f})" if spike < plan["vix_spike"]
                           else "waiting for a close in the top half of the day's range")
        else:
            item["state"] = "not_reached"
            item["gap"] = ", ".join(f"{s} is {bars[s]['c'][-1] / st[s] - 1:.1%} above its level" for s in bars if s in st)
        out.append(item)

    def first(cond):
        days = sorted({dd for B in bars.values() for dd in B["d"] if dd >= plan["set"]})
        return next((dd for dd in days if cond(dd)), None)

    def close_on(sym, day):
        B = bars[sym]
        i = next((i for i in range(len(B["d"]) - 1, -1, -1) if B["d"][i] <= day), None)
        return None if i is None else (i, B["c"][i])

    def above(sym, day, level=None):
        x = close_on(sym, day)
        if x is None:
            return False
        i, cl = x
        if level is None:                                   # its own 200-day average on that day
            if i < 199:
                return False
            level = sum(bars[sym]["c"][i - 199:i + 1]) / 200
        return cl > level

    for key, name in (("turn", "Turn trigger"), ("trend", "Trend repaired")):
        cfg = plan.get(key)
        if not cfg:
            continue
        if key == "turn":
            cond = lambda day: (vclose.get(day) is not None and vclose[day] < cfg["vix_below"]
                                and any(above(s, day, cfg[s]) for s in bars if s in cfg))
            text = " or ".join(f"{s} closes above ${cfg[s]:,.0f}" for s in bars if s in cfg) + f", with VIX closing under {cfg['vix_below']}"
        else:
            cond = lambda day: (vclose.get(day) is not None and vclose[day] < cfg["vix_below"]
                                and any(above(s, day) for s in bars))
            m = {s: sum(bars[s]["c"][-200:]) / 200 for s in bars if len(bars[s]["c"]) >= 200}
            text = (" or ".join(f"{s} closes above its 200-day (${m[s]:,.0f})" for s in m)
                    + f", with VIX closing under {cfg['vix_below']}")
        day = first(cond)
        item = {"key": f"{plan['set']}:{key}", "name": name, "text": text, "amount": cfg.get("amount", ""), "date": day}
        if day:
            item["state"] = "met_provisional" if (provisional and day == last_day) else "met"
        else:
            item["state"] = "not_reached"
            v = vclose.get(last_day)
            item["gap"] = f"VIX {v:.1f}" if v is not None else ""
        out.append(item)
    return out


# ------------------------------------------------------------------ what is worth a push

def decide(prev, readings, plan_items, session, final, late_day):
    """Compare this run with what was last pushed. Returns (reasons, notified, important).

    prev is the state file ({} on the first run). A push goes out for: a selloff opening, a new
    closing low after a rebound, a failed rebound, a retest, a recovery, the chance moving into a
    different band (and at least 5 points since the last push), a buy-back level being reached or
    met, and one summary after each close while a selloff is open. Nothing else pushes, so four
    runs a day stay quiet unless something changed.
    """
    note = dict(prev.get("notified") or {})
    pushed = prev.get("pushed") or {}
    why, important = [], False

    def once(key, text, imp=True):
        nonlocal important
        if key not in note:
            note[key] = session
            why.append(text)
            important = important or imp

    for sym, r in readings.items():
        was = pushed.get(sym) or {}
        if r["stage"] == "NO SELLOFF":
            continue
        ep = r["peak_date"]
        if was.get("episode") != ep:
            once(f"open:{sym}:{ep}", f"{sym} is in a selloff, {-r['ddclose']:.1%} under its {_day(ep)} high close")
            continue
        if r["stage"] == "RECOVERED":
            once(f"recovered:{sym}:{ep}", f"{sym} is back within 3% of its high: the selloff is over")
            continue
        if r["stage"] == "FAILED REBOUND":
            once(f"failed:{sym}:{session}", (f"{sym} rebound failed: new closing low at ${r['close']:,.2f}" if final else
                                             f"{sym} rebound is failing: ${r['close']:,.2f} is under its lowest close of the selloff"))
        elif r["stage"] == "NEW LOW" and was.get("stage") in ("REBOUND", "RETEST"):
            once(f"newlow:{sym}:{session}", (f"{sym} made a new closing low at ${r['close']:,.2f}" if final else
                                             f"{sym} is trading under its lowest close of the selloff (${r['close']:,.2f} now)"))
        elif r["stage"] == "RETEST" and was.get("stage") == "REBOUND":
            once(f"retest:{sym}:{r['low_date']}", f"{sym} is retesting its low: {r['reb']:.1%} above it after a {r['maxreb']:.1%} rebound")
        if (r.get("prob") is not None and was.get("prob") is not None and r["band"] != was.get("band")
                and abs(r["prob"] - was["prob"]) >= BAND_MOVE):
            word = "rose" if r["prob"] > was["prob"] else "fell"
            once(f"band:{sym}:{session}:{r['band']}", f"{sym} chance the low is in {word} to {r['prob']:.0%} from {was['prob']:.0%}")
    for it in plan_items:
        if it["state"] == "reached":
            once(f"plan:{it['key']}:reached", f"{it['name']} level reached ({it['text']}): {it.get('gap', '')}")
        elif it["state"] == "met":
            once(f"plan:{it['key']}:met", f"{it['name']} conditions met at the {_day(it['date'])} close")
        elif it["state"] == "met_provisional" and late_day:
            once(f"plan:{it['key']}:late:{session}", f"{it['name']} conditions are met so far today (not final until the close)")
    if final and any(r["stage"] != "NO SELLOFF" for r in readings.values()):
        once(f"daily:{session}", "Daily summary after the close", imp=False)
    return why, note, important


# ------------------------------------------------------------------ the report

def _day(s):
    return f"{_MON[int(s[5:7]) - 1]} {int(s[8:10])}"


def stage_text(stage, final):
    return STAGE_TEXT[stage] if final else LIVE_TEXT.get(stage, STAGE_TEXT[stage])


def headline(readings):
    live = [f"{s} {r['prob']:.0%}" for s, r in readings.items() if r["stage"] != "NO SELLOFF" and r.get("prob") is not None]
    if not live:
        return "Bottom watch: no selloff open"
    return "Bottom watch: chance the low is in, " + ", ".join(live)


def _index_lines(r, was, final=True):
    s = r["sym"]
    if r["stage"] == "NO SELLOFF":
        return [f"{s} ${r['close']:,.2f}: no selloff open. {-r['from_high']:.1%} under its 1-year high close; "
                f"a reading starts at ${r['starts_at']:,.2f}."]
    prev = f" ({was['prob']:.0%} at the last push)" if was and was.get("prob") is not None and abs(was["prob"] - r["prob"]) >= 0.005 else ""
    what = "this is the final low" if r["stage"] in ("NEW LOW", "FAILED REBOUND") else "the low is in"
    out = [f"{s} ${r['close']:,.2f}: {r['prob']:.0%} chance {what}{prev}. {BANDS[r['band']][1]}."]
    base = f"{-r['ddclose']:.1%} under the {_day(r['peak_date'])} high close of ${r['peak']:,.2f}, session {r['sess_pk']} of the selloff"
    if r["stage"] in ("NEW LOW", "FAILED REBOUND"):
        out.append(f"  {stage_text(r['stage'], final)}. {base}.")
    elif r["stage"] == "RECOVERED":
        out.append(f"  Recovered: back within 3% of the high. The low close was ${r['low']:,.2f} on {_day(r['low_date'])}.")
    else:
        out.append(f"  {stage_text(r['stage'], final)}: up {r['reb']:.1%} from the ${r['low']:,.2f} low close of {_day(r['low_date'])} "
                   f"({r['days']} session{'s' if r['days'] != 1 else ''} ago), best {r['maxreb']:.1%}. {base[0].upper() + base[1:]}.")
    if r["legs"]:
        out.append(f"  Failed rebounds so far: {r['legs']}.")
    return out


def _vix_line(readings):
    r = next((x for x in readings.values() if x.get("vix") is not None), None)
    if not r:
        return "VIX: no reading this run, so the estimate uses the 200-day and RSI only."
    if r["vix_off"] > -0.005:
        return f"VIX {r['vix']:.1f}, its highest close of the selloff."
    return f"VIX {r['vix']:.1f}, {-r['vix_off']:.0%} under its peak close of {r['vix_peak']:.1f} on {_day(r['vix_peak_date'])}."


def _plan_lines(items):
    out = []
    for it in items:
        if it["state"] == "not_reached":
            tail = "not reached" + (f" ({it['gap']})" if it.get("gap") else "")
        elif it["state"] == "reached":
            tail = f"level reached {_day(it['date'])}; {it.get('gap', '')}"
        elif it["state"] == "met_provisional":
            tail = "conditions met so far today (not final until the close)"
        else:
            tail = f"conditions met at the {_day(it['date'])} close"
        out.append(f"- {it['name']} ({it['text']}): {tail}.")
    return out


def push_text(readings, plan_items, why, when, final, pushed):
    """Short plain text for the phone push."""
    L = [f"{when}, {'after the close' if final else 'intraday, provisional'}."]
    if why:
        L.append("Why this push: " + "; ".join(why) + ".")
    L.append("")
    for s, r in readings.items():
        L += _index_lines(r, (pushed or {}).get(s), final)
    live = [r for r in readings.values() if r["stage"] not in ("NO SELLOFF", "RECOVERED")]
    if live:
        L += [_vix_line(readings), ""]
        todo = []
        for r in live:
            for ck in r["checks"]:
                if ck["met"] is False and ck["need"]:
                    todo.append((ck["hit"], f"- {r['sym'] + ': ' if 'VIX' not in ck['need'] else ''}{ck['need']} "
                                            f"(low was in {ck['hit']:.0%} of the time once met)"))
        seen, lines = set(), []
        for _, t in sorted(todo):
            if t not in seen:
                seen.add(t)
                lines.append(t)
        if lines:
            L += ["What would raise the odds:"] + lines[:4] + [""]
    if plan_items:
        L += ["Your buy-back levels:"] + _plan_lines(plan_items)
    return "\n".join(L).strip() + "\n"


def report(readings, plan_items, why, when, final, pushed, model):
    """The full report committed to the repo (markdown)."""
    L = [headline(readings), "", f"**{when}, {'after the close' if final else 'intraday (provisional: the after-close run confirms it)'}.**"]
    if why:
        L.append("What changed: " + "; ".join(why) + ".")
    L.append("")
    for s, r in readings.items():
        L += _index_lines(r, (pushed or {}).get(s), final)
    live = [r for r in readings.values() if r["stage"] != "NO SELLOFF"]
    if live:
        L += [_vix_line(readings), "", "| | " + " | ".join(r["sym"] for r in live) + " |", "|---|" + "---|" * len(live)]
        row = lambda name, fn: L.append(f"| {name} | " + " | ".join(fn(r) for r in live) + " |")
        row("Chance the low is in", lambda r: f"**{r['prob']:.0%}**")
        row("Stage", lambda r: stage_text(r["stage"], final))
        row("Price", lambda r: f"${r['close']:,.2f}")
        row("High close", lambda r: f"${r['peak']:,.2f} ({_day(r['peak_date'])})")
        row("From the high", lambda r: f"{r['ddclose']:.1%}")
        row("Lowest close", lambda r: f"${r['low']:,.2f} ({_day(r['low_date'])})")
        row("Up from the low", lambda r: f"{r['reb']:.1%} in {r['days']} sessions")
        row("Best rebound, failed rebounds", lambda r: f"{r['maxreb']:.1%}, {r['legs']}")
        row("Close vs the 200-day", lambda r: f"{r['dist200']:.1%} (${r['sma200']:,.2f})")
        row("RSI(14)", lambda r: f"{r['rsi14']:.0f}")
        row("VIX vs its peak close", lambda r: "n/a" if r.get("vix_off") is None else f"{r['vix_off']:.0%} ({r['vix']:.1f} vs {r['vix_peak']:.1f})")
        L += ["", "**Rebound checkpoints.** \"Past odds\" is how often the low was already in on days when the checkpoint was met.", "",
              "| Checkpoint | Past odds | " + " | ".join(r["sym"] for r in live) + " |", "|---|---|" + "---|" * len(live)]
        for i, ck in enumerate(live[0]["checks"]):
            cells = []
            for r in live:
                c2 = r["checks"][i]
                cells.append("n/a" if c2["met"] is None else ("yes" if c2["met"] else f"no: {c2['need']}"))
            L.append(f"| {ck['label']} | {ck['hit']:.0%} | " + " | ".join(cells) + " |")
        L += ["", "**Chance by day (closing readings, today's is live until the close):**"]
        for r in live:
            L.append(f"- {r['sym']}: " + ", ".join(f"{_day(dd)} {p:.0%}" for dd, p in r["trend"] if p is not None))
    if plan_items:
        L += ["", "**Your buy-back levels** (advisory; you place the orders):"] + _plan_lines(plan_items)
    rel = model.get("oos", {}).get("reliability", [])
    if rel:
        L += ["", "**How to read the chance.** On past selloffs the model had not seen, the low really was in: " +
              "; ".join(f"{x['actual']:.0%} of the time at a reading of {x['lo']:.0%} to {x['hi']:.0%}" for x in rel if x.get("actual") is not None) +
              ". Inside long bear markets those figures ran 4 to 10 points lower, because a bear-market rally looks like a final low early on. "
              "Evidence: bottom_results.md."]
    return "\n".join(L).strip() + "\n"
