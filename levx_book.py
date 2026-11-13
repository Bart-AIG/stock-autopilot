"""
LEVX book simulator: a slot-limited portfolio of leveraged funds driven by per-name signals.

  panel = Panel(members, start)     aligns every member to one calendar and precomputes the
                                    vehicle returns, costs, eligibility and common features
  run_book(panel, want, K, ...)     daily loop: mark to market, exit, enter, with costs

`want[t, j]` is the per-name desired state at the close of day t (True = hold into t+1).
Research only; the live routine never imports this.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

import levx_data as D
import levx_lab as L

TD = 252


def cost_side(px: np.ndarray, dv20: np.ndarray, vol20: np.ndarray) -> np.ndarray:
    """Half-spread + 1 bp slippage per side, from the fund's price, 20-day median dollar
    volume and 20-day daily volatility. Calibrated to Robinhood quotes sampled 2026-11-13
    (data/levx_cache/spreads_rh.jsonl): SOXL 3.6 bp full spread, NVDL 6, TSLL 10, AMDL 22,
    LITX 41-51, AAOX 61 (one tick), COHX 70-110."""
    base = np.select([dv20 >= 1e9, dv20 >= 2e8, dv20 >= 5e7, dv20 >= 2e7, dv20 >= 5e6],
                     [1.5e-4, 3e-4, 10e-4, 20e-4, 30e-4], 50e-4)
    scale = np.clip(np.nan_to_num(vol20, nan=0.06) / 0.06, 0.5, 3.0)
    tick = 0.005 / np.maximum(px, 0.01)
    return np.maximum(tick, base * scale) + 1e-4


class Panel:
    """Everything the book needs, as (days x members) matrices on one calendar."""

    def __init__(self, members: list[dict], start: str = "2007-01-01", veh_mode: str = "hybrid",
                 syn_cost: float = 0.0008, min_dv: float = 2e6, extra_drag: float = 0.0):
        cal = D.daily("SPY").index
        self.cal = cal[cal >= start]
        self.members = []
        cols = {k: [] for k in ("rc", "ro", "ri", "elig", "cost", "uc", "uo", "uh", "ul", "real")}
        for m in members:
            u = D.daily(m["und"])
            if u is None or len(u) < 60:
                continue
            v = L.vehicle(m["und"], m["lev"], m["kind"], m.get("fund"), mode=veh_mode, extra_drag=extra_drag)
            if v is None:
                continue
            v = v.reindex(self.cal)
            u2 = u.reindex(self.cal)
            real = v["real"].fillna(False).to_numpy(bool)
            ok = v["rc"].notna().to_numpy()
            if "dv" in v:
                dv20 = v["dv"].rolling(20, min_periods=10).median().shift(1).to_numpy()
                vol20 = v["rc"].rolling(20, min_periods=10).std().shift(1).to_numpy()
                c_real = cost_side(np.nan_to_num(v["px"].to_numpy(), nan=10.0), np.nan_to_num(dv20), vol20)
                liquid = np.nan_to_num(dv20) >= min_dv
            else:
                c_real, liquid = np.full(len(self.cal), syn_cost), np.zeros(len(self.cal), bool)
            cost = np.where(real, c_real, syn_cost)
            elig = ok & np.where(real, liquid, veh_mode != "real")
            self.members.append(m)
            cols["rc"].append(np.nan_to_num(v["rc"].to_numpy()))
            cols["ro"].append(np.nan_to_num(v["ro"].to_numpy()))
            cols["ri"].append(np.nan_to_num(v["ri"].to_numpy()))
            cols["elig"].append(elig)
            cols["cost"].append(cost)
            cols["real"].append(real)
            for a, b in (("uc", "c"), ("uo", "o"), ("uh", "h"), ("ul", "l")):
                cols[a].append(u2[b].to_numpy())
        for k, v in cols.items():
            setattr(self, k, np.column_stack(v))
        self.n = len(self.members)
        self.cash = L.cash_returns().reindex(self.cal).fillna(0.0).to_numpy()
        self._sig_cache: dict = {}

    # ---- per-name signals, computed on each underlying's own history then aligned
    def signal(self, fn, **kw) -> np.ndarray:
        key = (fn.__name__, tuple(sorted((k, str(v)) for k, v in kw.items())))
        if key in self._sig_cache:
            return self._sig_cache[key]
        out = np.zeros((len(self.cal), self.n), bool)
        for j, m in enumerate(self.members):
            u = D.daily(m["und"])
            p = pd.Series(fn(u, **kw), index=u.index).reindex(self.cal).fillna(False).to_numpy(bool)
            out[:, j] = p
        self._sig_cache[key] = out
        return out

    def feature(self, name: str) -> np.ndarray:
        """mom12 / mom6 / vol20 / above200 of the underlying, aligned (NaN where unknown)."""
        key = ("feat", name)
        if key in self._sig_cache:
            return self._sig_cache[key]
        out = np.full((len(self.cal), self.n), np.nan)
        for j, m in enumerate(self.members):
            u = D.daily(m["und"])
            c = u["c"]
            if name == "mom12":
                s = c / c.shift(252) - 1
            elif name == "mom6":
                s = c / c.shift(126) - 1
            elif name == "mom3":
                s = c / c.shift(63) - 1
            elif name == "mom1":
                s = c / c.shift(21) - 1
            elif name == "vol20":
                s = c.pct_change().rolling(20).std() * math.sqrt(TD)
            elif name == "vol60":
                s = c.pct_change().rolling(60).std() * math.sqrt(TD)
            elif name == "above200":
                s = (c > c.rolling(200).mean()).astype(float).where(c.rolling(200).mean().notna())
            elif name == "d200":
                s = c / c.rolling(200).mean() - 1
            elif name == "rsi2":
                s = pd.Series(L.rsi(c.to_numpy(), 2), index=c.index)
            else:
                raise KeyError(name)
            out[:, j] = s.reindex(self.cal).to_numpy()
        self._sig_cache[key] = out
        return out


def run_book(panel: Panel, want: np.ndarray, K: int = 4, rank: np.ndarray | None = None,
             fresh_only: bool = True, weight: np.ndarray | None = None, start: str | None = None,
             end: str | None = None, cost_mult: float = 1.0, lev_cap: float = 1.0,
             size: float | None = None) -> dict:
    """Slot book. Each entry takes `size` of equity (default 1/K), at most K names, never
    more than `lev_cap` of equity invested. want = desired state per name at each close.
    rank = higher is taken first when signals exceed free slots. fresh_only = only enter on
    the day the signal turns on (a trade already under way is not joined late).
    weight = optional (days x names) multiplier on the slot size (e.g. regime scaling)."""
    cal = panel.cal
    i0 = int(np.searchsorted(cal, pd.Timestamp(start))) if start else 0
    i1 = int(np.searchsorted(cal, pd.Timestamp(end), side="right")) if end else len(cal)
    n = panel.n
    size = size if size is not None else 1.0 / K
    w = np.zeros(n)                       # position value as a fraction of equity (marked daily)
    held = np.zeros(n, bool)
    since = np.ones(n)                    # price-only growth of each open position since entry
    rets, expo, ntr, log = [], [], 0, []
    prev_want = want[i0 - 1] if i0 > 0 else np.zeros(n, bool)
    for t in range(i0, i1):
        # 1. mark to market: positions held from the previous close earn today's return
        day = float((w * panel.rc[t]).sum()) + (1.0 - w.sum()) * panel.cash[t]
        since = np.where(held, since * (1 + panel.rc[t]), 1.0)
        w = w * (1 + panel.rc[t]) / (1.0 + day)
        fee = 0.0
        # 2. exits at today's close
        out_now = held & ~want[t]
        for j in np.flatnonzero(out_now):
            c = panel.cost[t, j] * cost_mult
            fee += w[j] * c
            log.append(since[j] * (1 - c) - 1)
        w[out_now] = 0.0
        held[out_now] = False
        # 3. entries at today's close
        cand = want[t] & ~held & panel.elig[t]
        if fresh_only:
            cand &= ~prev_want
        free = K - int(held.sum())
        if free > 0 and cand.any():
            idx = np.flatnonzero(cand)
            if rank is not None:
                r = np.nan_to_num(rank[t, idx], nan=-1e9)
                idx = idx[np.argsort(-r, kind="stable")]
            for j in idx[:free]:
                s = size * (weight[t, j] if weight is not None else 1.0)
                s = min(s, lev_cap - w.sum())
                if s <= 1e-6:
                    continue
                c = panel.cost[t, j] * cost_mult
                w[j] = s
                held[j] = True
                since[j] = 1 - c
                fee += s * c
                ntr += 1
        day = (1 + day) * (1 - fee) - 1
        if fee:
            w = w / (1 - fee)
        rets.append(day)
        expo.append(float(w.sum()))
        prev_want = want[t]
    r = np.array(rets)
    st = L.stats(r)
    tl = np.array(log)
    st.update(trades=ntr, expo=float(np.mean(expo)), r=r, idx=cal[i0:i1], tlog=tl,
              win=float((tl > 0).mean()) if len(tl) else float("nan"),
              avg_trade=float(tl.mean()) if len(tl) else float("nan"),
              worst_trade=float(tl.min()) if len(tl) else float("nan"))
    return st


def yearly(r: np.ndarray, idx: pd.DatetimeIndex) -> dict:
    s = pd.Series(r, index=idx)
    return {int(y): float((1 + g).prod() - 1) for y, g in s.groupby(s.index.year)}


def line(label: str, st: dict) -> str:
    return (f"| {label} | {L.fmt_pct(st['cagr'])} | {L.fmt_pct(st['mdd'], 0)} | {st['sharpe']:.2f} | "
            f"{L.fmt_pct(st['vol'], 0)} | {st.get('expo', float('nan')) * 100:.0f}% | {st.get('trades', '')} |")
