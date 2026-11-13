"""
LEVX stage 3: intraday (5-minute) tests. Is there a DAY-TRADE or a 15-minute swing edge in the
leveraged funds?   python levx_intraday.py [SYMBOL ...]

Data: FMP 5-minute bars, 2018 -> today, regular session, split-adjusted here. A session is a
78-slot row (09:30 ... 15:55 bar starts); half days and sessions with holes are dropped.
Every rule is published or already used by the house, run with its published parameters:
  ORB-5/15/30   opening-range breakout, long only, stop at the range low, exit at the close
  GAP-GO / GAP-FADE   open -> close after a gap up / gap down of more than 1 x the fund's
                      average absolute gap
  FH-MOM        first half hour up (prior close -> 10:00) -> long 10:00 -> close
  LATE-MOM      day up at 15:30 -> long 15:30 -> close
  NOISE         noise-area breakout (Zarattini, Aziz & Barbon 2024), long only, 30-min checks
  VWAP          long while above session VWAP, 30-minute checks from 10:00
  DIP->CLOSE    down more than 1 x average range by 14:00 -> long to the close
  DIP->OPEN     same entry at 15:50, exit at the next open
  OVN           15:50 -> next open, every night; OVN-UP only when above the 200-day SMA
  OPEN->CLOSE   the whole session, every day (reference)
A synthetic 2x fund is 2 x the underlying's move from the prior close, exact for intraday.
"""
from __future__ import annotations

import math
import sys
from datetime import time as dtime

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L

SLOTS = pd.date_range("09:30", "15:55", freq="5min").time
S = {t: i for i, t in enumerate(SLOTS)}
B1000, B1400, B1530, B1550 = S[dtime(9, 55)], S[dtime(13, 55)], S[dtime(15, 25)], S[dtime(15, 45)]  # bar whose CLOSE is that time
DISC, VAL = ("2018-01-01", "2022-12-31"), ("2023-01-01", "2026-12-31")


def sessions(sym: str, lev_from: tuple[str, float] | None = None):
    """Returns dict(days, O, H, L, C, V, pc) with (days x 78) arrays of split-adjusted prices
    and pc = prior session close. lev_from=(underlying, k) builds a synthetic k-times fund."""
    src = lev_from[0] if lev_from else sym
    df = D.fmp_5min(src)
    if df is None or len(df) < 1000:
        return None
    dly = D.daily(src, drop_today_if_open=False)
    day = df.index.normalize()
    # FMP's 5-minute bars are already split-adjusted, but not always consistently: scale any
    # session whose last bar is more than 3% away from the daily (split-adjusted) close.
    last = df.groupby(day)["c"].last()
    ratio = (dly["raw"].reindex(last.index) / last).fillna(1.0)
    ratio = ratio.where((ratio - 1).abs() > 0.03, 1.0)
    fac = ratio.reindex(day).to_numpy()
    df = df.assign(o=df.o * fac, h=df.h * fac, l=df.l * fac, c=df.c * fac, d=day, s=[S.get(t, -1) for t in df.index.time])
    df = df[df.s >= 0]
    cnt = df.groupby("d").size()
    good = cnt[cnt >= 74].index
    df = df[df.d.isin(good)]
    days = pd.DatetimeIndex(sorted(good))
    di = {d: i for i, d in enumerate(days)}
    n = len(days)
    M = {k: np.full((n, 78), np.nan) for k in "ohlcv"}
    r = df.d.map(di).to_numpy()
    for k in "ohlcv":
        M[k][r, df.s.to_numpy()] = df[k].to_numpy()
    # fill holes: carry the last close forward, zero volume
    c = pd.DataFrame(M["c"]).ffill(axis=1).bfill(axis=1).to_numpy()
    for k in "ohl":
        M[k] = np.where(np.isnan(M[k]), c, M[k])
    M["c"], M["v"] = c, np.nan_to_num(M["v"])
    pc = (dly["raw"] * 1.0).shift(1).reindex(days).to_numpy()   # Yahoo close is split-adjusted
    ok = np.isfinite(pc) & (np.abs(M["o"][:, 0] / pc - 1) < 0.6)
    out = {"days": days[ok], "pc": pc[ok], **{k.upper(): v[ok] for k, v in M.items()}}
    c200 = dly["c"].rolling(200).mean()
    out["up200"] = (dly["c"] > c200).shift(1).reindex(out["days"]).fillna(False).to_numpy(bool)
    if lev_from:
        # Synthetic daily-reset fund. Each session is anchored on the synthetic fund's own prior
        # close (built from daily data with drag), so overnight returns are continuous.
        k = lev_from[1]
        syn = L.synthetic(D.daily(src, drop_today_if_open=False), abs(k), "stock")["c"] if k > 0 else None
        anchor = syn.shift(1).reindex(out["days"]).to_numpy() if syn is not None else out["pc"].copy()
        und_pc = out["pc"]
        for a in "OHLC":
            out[a] = anchor[:, None] * np.clip(1 + k * (out[a] / und_pc[:, None] - 1), 0.01, None)
        if k < 0:
            out["H"], out["L"] = np.maximum(out["H"], out["L"]), np.minimum(out["H"], out["L"])
        out["pc"] = anchor
        out["syn_k"] = k
    return out


# ----------------------------------------------------------------------------- rules
# each returns (gross return per day, round trips per day) as arrays over days

def r_orb(X, k):
    O, H, Lo, C = X["O"], X["H"], X["L"], X["C"]
    n = len(O)
    ret, tr = np.zeros(n), np.zeros(n)
    for d in range(n):
        if not C[d, k - 1] > O[d, 0]:
            continue
        stop = Lo[d, :k].min()
        entry = O[d, k]
        if entry <= stop:
            continue
        x = C[d, -1]
        for b in range(k, 78):
            if Lo[d, b] <= stop:
                x = min(stop, O[d, b])
                break
        ret[d], tr[d] = x / entry - 1, 1
    return ret, tr


def r_gap(X, go=True):
    g = X["O"][:, 0] / X["pc"] - 1
    th = pd.Series(np.abs(g)).rolling(60, min_periods=20).mean().shift(1).to_numpy()
    take = (g > th) if go else (g < -th)
    take &= np.isfinite(th)
    r = X["C"][:, -1] / X["O"][:, 1] - 1          # enter at 09:35, as the house test did
    return np.where(take, r, 0.0), take.astype(float)


def r_from(X, bar, cond):
    r = X["C"][:, -1] / X["C"][:, bar] - 1
    return np.where(cond, r, 0.0), cond.astype(float)


def r_noise(X, lookback=14, step=6):
    O, C, H, Lo, V = X["O"], X["C"], X["H"], X["L"], X["V"]
    n = len(O)
    mv = np.abs(C / O[:, :1] - 1)
    sig = pd.DataFrame(mv).rolling(lookback, min_periods=10).mean().shift(1).to_numpy()
    tp = (H + Lo + C) / 3
    vw = np.cumsum(tp * V, axis=1) / np.maximum(np.cumsum(V, axis=1), 1e-9)
    vw = np.where(np.cumsum(V, axis=1) > 0, vw, C)
    ret, tr = np.zeros(n), np.zeros(n)
    checks = [b for b in range(step - 1, 77, step)]            # closes at :00 / :30
    for d in range(n):
        if not np.isfinite(sig[d, checks[0]]):
            continue
        ref = max(O[d, 0], X["pc"][d])
        pos, entry, acc, k = False, 0.0, 1.0, 0
        for b in checks:
            U, c = ref * (1 + sig[d, b]), C[d, b]
            if pos and c < max(U, vw[d, b]):
                acc *= c / entry
                pos = False
            if not pos and c > U:
                pos, entry, k = True, c, k + 1
        if pos:
            acc *= C[d, -1] / entry
        ret[d], tr[d] = acc - 1, k
    return ret, tr


def r_vwap(X, step=6):
    C, H, Lo, V = X["C"], X["H"], X["L"], X["V"]
    tp = (H + Lo + C) / 3
    cv = np.cumsum(V, axis=1)
    vw = np.where(cv > 0, np.cumsum(tp * V, axis=1) / np.maximum(cv, 1e-9), C)
    n = len(C)
    ret, tr = np.zeros(n), np.zeros(n)
    checks = [b for b in range(step - 1, 77, step)]
    for d in range(n):
        pos, entry, acc, k = False, 0.0, 1.0, 0
        for b in checks:
            c = C[d, b]
            if pos and c < vw[d, b]:
                acc *= c / entry
                pos = False
            elif not pos and c > vw[d, b]:
                pos, entry, k = True, c, k + 1
        if pos:
            acc *= C[d, -1] / entry
        ret[d], tr[d] = acc - 1, k
    return ret, tr


def r_dip(X, bar, to_open=False):
    """Down more than 1 x the 60-day average absolute open->`bar` move by `bar`: buy there."""
    mv = X["C"][:, bar] / X["O"][:, 0] - 1
    th = pd.Series(np.abs(mv)).rolling(60, min_periods=20).mean().shift(1).to_numpy()
    take = (mv < -th) & np.isfinite(th)
    if to_open:
        nxt = np.r_[X["O"][1:, 0], np.nan]
        gapdays = np.r_[np.diff(X["days"].to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
        r = nxt / X["C"][:, bar] - 1
        take &= np.isfinite(r) & gapdays
        return np.where(take, r, 0.0), take.astype(float)
    return np.where(take, X["C"][:, -1] / X["C"][:, bar] - 1, 0.0), take.astype(float)


def r_overnight(X, cond=None, bar=B1550):
    nxt = np.r_[X["O"][1:, 0], np.nan]
    near = np.r_[np.diff(X["days"].to_numpy()).astype("timedelta64[D]").astype(int) <= 5, False]
    r = nxt / X["C"][:, bar] - 1
    take = np.isfinite(r) & near
    if cond is not None:
        take &= cond
    return np.where(take, r, 0.0), take.astype(float)


def battery(X):
    up = X["C"][:, B1000] / X["pc"] - 1 > 0
    late = X["C"][:, B1530] / X["pc"] - 1 > 0
    return {
        "ORB-5 long": r_orb(X, 1), "ORB-15 long": r_orb(X, 3), "ORB-30 long": r_orb(X, 6),
        "GAP-GO": r_gap(X, True), "GAP-FADE": r_gap(X, False),
        "FH-MOM (10:00 -> close)": r_from(X, B1000, up),
        "LATE-MOM (15:30 -> close)": r_from(X, B1530, late),
        "NOISE breakout long": r_noise(X),
        "VWAP trend long": r_vwap(X),
        "DIP 14:00 -> close": r_dip(X, B1400),
        "DIP 15:50 -> next open": r_dip(X, B1550, True),
        "OVN every night (15:50 -> open)": r_overnight(X),
        "OVN above 200d": r_overnight(X, X["up200"]),
        "OVN below 200d": r_overnight(X, ~X["up200"]),
        "OPEN -> CLOSE every day": (X["C"][:, -1] / X["O"][:, 0] - 1, np.ones(len(X["O"]))),
    }


def summarize(name, ret, tr, days, cost):
    net = ret - 2 * cost * tr
    out = {}
    for pl, (a, b) in (("disc", DISC), ("val", VAL)):
        m = (days >= a) & (days <= b)
        st = L.stats(net[m])
        t = tr[m] > 0
        g = ret[m][t]
        st.update(trades=int(tr[m].sum()), avg_bp=float(g.mean() * 1e4) if len(g) else float("nan"),
                  win=float((g > 0).mean()) if len(g) else float("nan"),
                  tstat=float(g.mean() / (g.std(ddof=1) / math.sqrt(len(g)))) if len(g) > 20 and g.std() > 0 else float("nan"))
        out[pl] = st
    return out


def run(label, X, cost):
    print(f"\n### {label}: {len(X['days'])} sessions {X['days'][0].date()} -> {X['days'][-1].date()}, cost {cost*1e4:.0f} bp/side")
    print("| Rule | 2018-22 CAGR / DD / Sharpe | trades | avg trade bp (t) | win | 2023-26 CAGR / DD / Sharpe | trades | avg trade bp (t) | win |")
    print("|---|---|---|---|---|---|---|---|---|")
    res = {}
    for name, (ret, tr) in battery(X).items():
        s = summarize(name, ret, tr, X["days"], cost)
        res[name] = s
        d, v = s["disc"], s["val"]
        print(f"| {name} | {L.fmt_pct(d['cagr'])} / {L.fmt_pct(d['mdd'],0)} / {d['sharpe']:.2f} | {d['trades']} | {d['avg_bp']:+.0f} ({d['tstat']:+.1f}) | {L.fmt_pct(d['win'],0)} | "
              f"{L.fmt_pct(v['cagr'])} / {L.fmt_pct(v['mdd'],0)} / {v['sharpe']:.2f} | {v['trades']} | {v['avg_bp']:+.0f} ({v['tstat']:+.1f}) | {L.fmt_pct(v['win'],0)} |")
    return res


if __name__ == "__main__":
    args = sys.argv[1:] or ["SOXL"]
    for a in args:
        if ":" in a:                      # e.g. AAOI:2:0.003  -> synthetic 2x of AAOI at 30 bp/side
            und, k, c = a.split(":")
            X = sessions(und, (und, float(k)))
            if X is not None:
                run(f"synthetic {k}x {und}", X, float(c))
        else:
            X = sessions(a)
            if X is not None:
                run(a, X, 0.0002)
