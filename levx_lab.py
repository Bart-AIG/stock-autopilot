"""
Research library for the leveraged-ETF sleeve (LEVX): signals, vehicles, simulation, stats.
Used by levx_stage*.py. Research only; the live routine never imports this.

Conventions
  * Signals come from the UNDERLYING's adjusted daily bars (long history).
  * pos[i] = True means "hold the vehicle from close i to close i+1" (decided at close i).
  * The vehicle is the real leveraged fund where it exists, else a synthetic daily-reset fund:
    k x underlying return - drag/252, drag = fee + (k-1) x (T-bill + spread).
  * Costs are charged per side at each change of position.
"""

from __future__ import annotations

import json
import math

import numpy as np
import pandas as pd

import levx_data as D

TD = 252


# ----------------------------------------------------------------------------- indicators

def rsi(c: np.ndarray, n: int = 2) -> np.ndarray:
    """Wilder RSI, rounded to 0.1 like analyze.compute_rsi (the live function)."""
    out = np.full(len(c), np.nan)
    if len(c) <= n:
        return out
    d = np.diff(c)
    g, l = np.maximum(d, 0), np.maximum(-d, 0)
    ag, al = g[:n].mean(), l[:n].mean()
    out[n] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    for i in range(n, len(d)):
        ag = (ag * (n - 1) + g[i]) / n
        al = (al * (n - 1) + l[i]) / n
        out[i + 1] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return np.round(out, 1)


def sma(x: np.ndarray, n: int) -> np.ndarray:
    return pd.Series(x).rolling(n).mean().to_numpy()


def tom_flags(idx: pd.DatetimeIndex, first: int = 3, last: int = 1) -> np.ndarray:
    """True on the last `last` and first `first` sessions of each month."""
    ym = idx.year * 12 + idx.month
    s = pd.Series(np.arange(len(idx)), index=idx)
    rank_fwd = s.groupby(ym).cumcount().to_numpy()
    rank_back = s.iloc[::-1].groupby(ym[::-1]).cumcount().iloc[::-1].to_numpy()
    return (rank_fwd < first) | (rank_back < last)


def atr(h, l, c, n=14):
    pc = np.r_[c[0], c[:-1]]
    tr = np.maximum(h - l, np.maximum(abs(h - pc), abs(l - pc)))
    return pd.Series(tr).rolling(n).mean().to_numpy()


# ----------------------------------------------------------------------------- signals
# every function takes the underlying's DataFrame (o h l c) and returns pos (bool array)

def sig_bh(df, **_):
    return np.ones(len(df), bool)


def sig_trend(df, n=200, **_):
    c = df["c"].to_numpy()
    m = sma(c, n)
    return np.nan_to_num(c > m, nan=0).astype(bool) & ~np.isnan(m)


def sig_swing(df, trend=200, parts=("RSI2", "IBS", "TOM"), rsi_in=10, ibs_in=0.2, ibs_out=0.8,
              ibs_max=5, rsi_exit="sma5", **_):
    """The house SWING_UNION (robust_backtest.swing / sleeves.step). trend=None drops the
    trend filter; trend=50 uses the 50-day SMA."""
    c, h, l = (df[k].to_numpy() for k in ("c", "h", "l"))
    n = len(c)
    up = np.ones(n, bool) if not trend else np.nan_to_num(c > sma(c, trend), nan=0).astype(bool)
    start = max(trend or 0, 60) + 1
    r2 = rsi(c, 2)
    s5 = sma(c, 5)
    rng = h - l
    ibs = np.where(rng > 0, (c - l) / np.where(rng > 0, rng, 1), 0.5)
    tom = tom_flags(df.index)
    pos = np.zeros(n, bool)
    hr = hi = False
    age = 0
    for i in range(start, n):
        if "RSI2" in parts:
            if hr:
                hr = not (c[i] > s5[i]) if rsi_exit == "sma5" else not (r2[i] > 70)
            else:
                hr = bool(r2[i] < rsi_in and up[i])
        if "IBS" in parts:
            if hi:
                age += 1
                hi = not (ibs[i] > ibs_out or age >= ibs_max)
            else:
                hi = bool(ibs[i] < ibs_in and up[i])
                age = 0
        ht = "TOM" in parts and i + 1 < n and bool(tom[i + 1])
        pos[i] = hr or hi or ht
    return pos


def sig_donchian(df, n_in=20, n_out=10, **_):
    c, h, l = (df[k].to_numpy() for k in ("c", "h", "l"))
    hh = pd.Series(h).rolling(n_in).max().shift(1).to_numpy()
    ll = pd.Series(l).rolling(n_out).min().shift(1).to_numpy()
    pos = np.zeros(len(c), bool)
    on = False
    for i in range(n_in + 1, len(c)):
        if on:
            on = not (c[i] < ll[i])
        else:
            on = bool(c[i] > hh[i])
        pos[i] = on
    return pos


def sig_upcont(df, trend=None, **_):
    """Strong close continuation: up day closing in the top 20% of its range -> hold 1 day."""
    c, h, l = (df[k].to_numpy() for k in ("c", "h", "l"))
    rng = h - l
    ibs = np.where(rng > 0, (c - l) / np.where(rng > 0, rng, 1), 0.5)
    up = np.r_[False, c[1:] > c[:-1]]
    pos = up & (ibs > 0.8)
    if trend:
        pos &= sig_trend(df, trend)
    return pos


def sig_dnrev(df, trend=None, **_):
    """Weak close reversal: down day closing in the bottom 20% of its range -> hold 1 day."""
    c, h, l = (df[k].to_numpy() for k in ("c", "h", "l"))
    rng = h - l
    ibs = np.where(rng > 0, (c - l) / np.where(rng > 0, rng, 1), 0.5)
    dn = np.r_[False, c[1:] < c[:-1]]
    pos = dn & (ibs < 0.2)
    if trend:
        pos &= sig_trend(df, trend)
    return pos


def sig_washout(df, look=10, drop=-0.25, max_hold=10, **_):
    """Capitulation bounce: `look`-day return below `drop` -> hold until close > 5-day SMA
    or max_hold sessions. No trend filter."""
    c = df["c"].to_numpy()
    s5 = sma(c, 5)
    pos = np.zeros(len(c), bool)
    on, age = False, 0
    for i in range(look + 5, len(c)):
        if on:
            age += 1
            on = not (c[i] > s5[i] or age >= max_hold)
        else:
            on = bool(c[i] / c[i - look] - 1 < drop)
            age = 0
        pos[i] = on
    return pos


def sig_mom_gate(df, fast=20, slow=100, **_):
    """Trend stack: close > fast SMA and fast SMA > slow SMA."""
    c = df["c"].to_numpy()
    f, s = sma(c, fast), sma(c, slow)
    return np.nan_to_num((c > f) & (f > s), nan=0).astype(bool) & ~np.isnan(s)


# ----------------------------------------------------------------------------- vehicles

_CASH = None


def cash_returns() -> pd.Series:
    """Daily T-bill return (BIL since 2007; ^IRX yield before that)."""
    global _CASH
    if _CASH is None:
        bil = D.daily("BIL")["c"].pct_change()
        irx = D.daily("^IRX")
        if irx is not None:
            y = (irx["raw"] / 100 / TD).reindex(bil.index.union(irx.index)).ffill()
            bil = bil.reindex(y.index).fillna(y)
        _CASH = bil.fillna(0.0)
    return _CASH


def rf_annual(idx: pd.DatetimeIndex) -> np.ndarray:
    """Annualised T-bill rate per day (20-day mean of the cash return)."""
    c = cash_returns().reindex(idx).fillna(0.0)
    return (c.rolling(20, min_periods=1).mean() * TD).to_numpy()


def synthetic(und: pd.DataFrame, k: float, kind: str = "stock", extra_drag: float = 0.0) -> pd.DataFrame:
    """Daily-reset k-times fund built from the underlying. drag = fee + (k-1) x (rf + spread).
    Index funds: fee 0.95%, spread 0.5%. Single-stock funds: fee 1.3%, spread 1.5%."""
    fee, spr = (0.0095, 0.005) if kind == "index" else (0.0, 0.0) if kind == "spot" else (0.013, 0.015)
    r = und["c"].pct_change().fillna(0.0).to_numpy()
    drag = (fee + (k - 1) * (rf_annual(und.index) + spr) + extra_drag) / TD
    cc = np.clip(k * r - drag, -0.999, None)
    c = np.cumprod(1 + cc)
    # split the day into overnight and intraday with the same leverage; drag sits overnight
    ro = (und["o"] / und["c"].shift(1) - 1).fillna(0.0).to_numpy()
    o = np.r_[1.0, c[:-1]] * np.clip(1 + k * ro - drag, 0.001, None)
    return pd.DataFrame({"o": o, "c": c}, index=und.index)


def vehicle(und_sym: str, k: float, kind: str, fund_sym: str | None = None, mode: str = "hybrid",
            extra_drag: float = 0.0) -> pd.DataFrame | None:
    """o/c of the tradable leveraged fund on the underlying's calendar, plus `real` flags.
    mode: 'syn' (always synthetic), 'real' (only the real fund, NaN before launch),
    'hybrid' (real from launch, synthetic before)."""
    u = D.daily(und_sym)
    if u is None:
        return None
    s = synthetic(u, k, kind, extra_drag)
    rs = pd.DataFrame({"ro": (s["o"] / s["c"].shift(1) - 1), "rc": s["c"].pct_change(), "real": False}, index=u.index)
    rs["ri"] = s["c"] / s["o"] - 1
    if mode == "syn" or not fund_sym:
        return rs
    f = D.daily(fund_sym)
    if f is None:
        return rs if mode == "hybrid" else None
    f = f.reindex(u.index)
    rr = pd.DataFrame({"ro": f["o"] / f["c"].shift(1) - 1, "rc": f["c"].pct_change(), "ri": f["c"] / f["o"] - 1}, index=u.index)
    ok = rr["rc"].notna() & f["c"].shift(1).notna()
    if mode == "real":
        rs[["ro", "rc", "ri"]] = np.nan
    for k_ in ("ro", "rc", "ri"):
        rs.loc[ok, k_] = rr.loc[ok, k_]
    rs.loc[ok, "real"] = True
    rs["dv"] = f["dv"]
    rs["px"] = f["px"]
    return rs


# ----------------------------------------------------------------------------- simulation

def simulate(pos: np.ndarray, veh: pd.DataFrame, cost: float | np.ndarray = 0.0, mode: str = "cc",
             cash: np.ndarray | None = None) -> np.ndarray:
    """Daily net return of the timed vehicle. mode 'cc' = close to close; 'ovn' = close to next
    open (2 sides every held night); 'intra' = open to close of the NEXT day (2 sides)."""
    n = len(pos)
    out = np.zeros(n)
    cash = np.zeros(n) if cash is None else cash
    cost = np.full(n, cost) if np.isscalar(cost) else cost
    held = np.r_[False, pos[:-1]]                 # position carried into day i
    if mode == "cc":
        r = np.nan_to_num(veh["rc"].to_numpy())
        out = np.where(held, r, cash)
        flips = pos != held
        out = out - np.where(flips, cost, 0.0)
        return out
    r = np.nan_to_num(veh["ro" if mode == "ovn" else "ri"].to_numpy())
    out = np.where(held, r - 2 * cost, cash)
    return out


def stats(r: np.ndarray, idx: pd.DatetimeIndex | None = None) -> dict:
    r = np.asarray(r, float)
    if len(r) < 20:
        return {"cagr": float("nan"), "mdd": float("nan"), "sharpe": float("nan"), "vol": float("nan"), "n": len(r)}
    eq = np.cumprod(1 + r)
    yrs = len(r) / TD
    cagr = eq[-1] ** (1 / yrs) - 1 if eq[-1] > 0 else -1.0
    dd = eq / np.maximum.accumulate(eq) - 1
    sd = r.std()
    return {"cagr": float(cagr), "mdd": float(dd.min()), "sharpe": float(r.mean() / sd * math.sqrt(TD)) if sd > 0 else 0.0,
            "vol": float(sd * math.sqrt(TD)), "n": len(r), "total": float(eq[-1] - 1)}


def trades(pos: np.ndarray, r: np.ndarray, cost: float | np.ndarray = 0.0) -> np.ndarray:
    """Net compounded return of each completed trade (entry at close i, exit at close j)."""
    cost = np.full(len(pos), cost) if np.isscalar(cost) else cost
    held = np.r_[False, pos[:-1]]
    out, acc, on = [], 1.0, False
    for i in range(len(pos)):
        if held[i]:
            acc *= 1 + r[i]
        if on and not pos[i]:
            out.append(acc * (1 - cost[i]) - 1)
            on = False
        if pos[i] and not on:
            on, acc = True, 1.0 - cost[i]
    return np.array(out)


def timing_edge(pos: np.ndarray, r: np.ndarray, valid: np.ndarray | None = None) -> dict:
    """Does the signal pick better days than average? Mean next-day return when held minus the
    mean over all valid days, in bp, with a simple t-stat."""
    held = np.r_[False, pos[:-1]]
    v = np.isfinite(r) if valid is None else (valid & np.isfinite(r))
    a, b = r[v & held], r[v]
    if len(a) < 20:
        return {"n": int(len(a)), "edge_bp": float("nan"), "t": float("nan"), "tim": float("nan")}
    edge = a.mean() - b.mean()
    se = a.std(ddof=1) / math.sqrt(len(a))
    return {"n": int(len(a)), "edge_bp": float(edge * 1e4), "t": float(edge / se) if se > 0 else 0.0,
            "held_bp": float(a.mean() * 1e4), "all_bp": float(b.mean() * 1e4), "tim": float(len(a) / max(1, len(b)))}


def fmt_pct(x, d=1):
    return "n/a" if x is None or (isinstance(x, float) and not math.isfinite(x)) else f"{x * 100:.{d}f}%"


# ----------------------------------------------------------------------------- universes

def universe(min_dv: float = 0.0) -> list[dict]:
    u = json.loads((D.CACHE / "universe.json").read_text())
    return [r for r in u if r.get("ok") and r.get("dv60", 0) >= min_dv]


def best_fund_per_underlying(rows: list[dict], prefer: str = "history") -> dict[str, dict]:
    """One vehicle per underlying. 'history' = the longest-lived fund (more real prices in the
    test); 'liquidity' = the one with the highest dollar volume today (what would be traded)."""
    out: dict[str, dict] = {}
    for r in rows:
        k = r["und"]
        cur = out.get(k)
        if cur is None:
            out[k] = r
        elif prefer == "history":
            if (r["first"], -r["dv60"]) < (cur["first"], -cur["dv60"]):
                out[k] = r
        elif r["dv60"] > cur["dv60"]:
            out[k] = r
    return out


def pit_pool() -> list[str]:
    from backtest import NDX100_2018, SP100_2018
    return sorted(set(SP100_2018) | set(NDX100_2018))
