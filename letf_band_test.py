"""Test of a published 'fixed-dollar SOXL band' strategy (shared by Ryan 2026-11-26) against
the joint-account trend rule (letf_joint_backtest.py).

The article's rules, as written:
  start: $5,000 in SOXL, $5,000 cash. Target stays $5,000 forever.
  after each close: position value <= $4,500 -> schedule a buy back to $5,000 at the next open
  (only with cash on hand); value >= $5,500 -> schedule a trim to $5,000 at the next open;
  in a strong trend (SOXX close > 20-day SMA > 100-day SMA) the trim trigger is $7,500.
  Orders are sized at the next open. 0.10% cost on every trade after the first. Cash earns 0.

Variants added here:
  gate_buys  : no dip buys while SOXX is OFF under the 2%-band 200-day rule
  gate_full  : while OFF hold no SOXL (sell at the next open), back to the $5,000 target when ON
Read-only research. Output printed; summary in letf_joint_results.md section 10.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

import letf_joint_backtest as B


def soxl_prices(real: bool) -> pd.DataFrame:
    """Real SOXL (2010-03 on) or a synthetic 3x SOXX fund (2001-07 on), calibrated spread 0.75%."""
    if real:
        return B.load("SOXL")
    u = B.load("SOXX")
    f = B.synth(u, B.tbill(u.index), 3, B.SPREAD["SOXX"])
    c = (1 + f["cc"]).cumprod() * 100
    o = c.shift(1) * (1 + f["co"])
    o.iloc[0] = c.iloc[0]
    return pd.DataFrame({"o": o, "c": c})


def trend_inputs():
    s = B.load("SOXX")["c"]
    strong = (s > s.rolling(20).mean()) & (s.rolling(20).mean() > s.rolling(100).mean())
    band_on = B.rules(B.load("SOXX"), 3)["sma200_band2"][0] > 0
    return strong, band_on


def band_strategy(px, strong, band_on, start, end=None, variant="article", target=5000.0, cash=5000.0,
                  lo=0.9, hi=1.1, hi_strong=1.5, cost=0.001, rf=None, start_at_open=True):
    idx = px.index[(px.index >= pd.Timestamp(start)) & (px.index <= pd.Timestamp(end or px.index[-1]))]
    o, c = px["o"].reindex(idx), px["c"].reindex(idx)
    st, on = strong.reindex(idx).fillna(False), band_on.reindex(idx).fillna(False)
    shares = 0.0
    if variant != "gate_full" or on.iloc[0]:
        shares = target / (o.iloc[0] if start_at_open else c.iloc[0])   # first purchase, no cost
    else:
        cash += target
    pending = None
    eq, trims, buys, short_cash = [], 0, 0, 0
    for i, d in enumerate(idx):
        if i > 0:
            if rf is not None:
                cash *= 1 + rf.loc[d] / 252
            if pending is not None:
                v = shares * o.iloc[i]
                want = 0.0 if pending == "exit" else target
                delta = want - v
                if pending in ("buy", "enter") and delta > 0:
                    amt = min(delta, cash / (1 + cost))
                    if amt < delta - 1e-6:
                        short_cash += 1
                    if amt > 0:
                        shares += amt / o.iloc[i]
                        cash -= amt * (1 + cost)
                        buys += 1
                elif pending in ("trim", "exit") and delta < 0:
                    amt = -delta
                    shares -= amt / o.iloc[i]
                    cash += amt * (1 - cost)
                    trims += 1
                pending = None
        v = shares * c.iloc[i]
        if variant == "gate_full":
            if not on.iloc[i]:
                pending = "exit" if shares > 0 else None
            elif shares == 0:
                pending = "enter"
        if pending is None and (variant != "gate_full" or on.iloc[i]):
            trim_at = target * (hi_strong if st.iloc[i] else hi)
            if shares > 0 and v >= trim_at:
                pending = "trim"
            elif v <= target * lo and (variant == "article" or on.iloc[i]):
                pending = "buy"
        eq.append(cash + v)
    eq = pd.Series(eq, index=idx)
    return {"eq": eq, "trims": trims, "buys": buys, "short_cash": short_cash, "cash": cash, "soxl": shares * c.iloc[-1]}


def summary(eq):
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    return {"final": eq.iloc[-1], "cagr": (eq.iloc[-1] / eq.iloc[0]) ** (1 / yrs) - 1 if yrs > 0.5 else np.nan,
            "mdd": (eq / eq.cummax() - 1).min()}


def hold_half(px, start, end=None, amt=5000.0, cash=5000.0):
    m = (px.index >= pd.Timestamp(start)) & (px.index <= pd.Timestamp(end or px.index[-1]))
    c = px["c"][m]
    return cash + amt * c / px["o"][m].iloc[0]


def trend_rule(start, end=None, equity=10000.0):
    """The joint process's recommended rule on synthetic SOXL, $10,000 sleeve, at the close."""
    u = B.load("SOXX")
    rf = B.tbill(u.index)
    e, a = B.rules(u, 3)["recommended"]
    B.START_EQUITY = equity
    r = B.simulate(u, rf, 3, B.SPREAD["SOXX"], e, a, execution="close", taxed=False, start=pd.Timestamp(start),
                   end=pd.Timestamp(end) if end else None)
    return r["eq"]


def spy_hold(start, end=None, equity=10000.0):
    s = B.load("SPY")["c"]
    s = s[(s.index >= pd.Timestamp(start)) & (s.index <= pd.Timestamp(end or s.index[-1]))]
    return equity * s / s.iloc[0]


def band_fast(o, c, st, on, variant="article", target=5000.0, cash=5000.0, frac=None, lo=0.9, hi=1.1,
              hi_strong=1.5, cost=0.001, rf=None):
    """numpy version of band_strategy (same rules; start purchase at the first open). frac: target as a
    share of the account instead of fixed dollars. Returns the daily account value and counts."""
    n = len(c)
    eq = np.empty(n)
    shares = 0.0
    if variant != "gate_full" or on[0]:
        t0 = frac * (cash + target) if frac else target
        shares = t0 / o[0]
        cash = cash + target - t0
    else:
        cash += target
    pend = 0           # 1 buy/enter, -1 trim/exit-to-target, -2 exit all
    trims = buys = short = 0
    for i in range(n):
        if i > 0:
            if rf is not None:
                cash *= 1 + rf[i] / 252
            if pend:
                v = shares * o[i]
                tgt = frac * (cash + v) if frac else target
                want = 0.0 if pend == -2 else tgt
                d = want - v
                if pend == 1 and d > 0:
                    amt = min(d, cash / (1 + cost))
                    short += amt < d - 1e-6
                    if amt > 0:
                        shares += amt / o[i]; cash -= amt * (1 + cost); buys += 1
                elif pend < 0 and d < 0:
                    shares += d / o[i]; cash += -d * (1 - cost); trims += 1
                pend = 0
        v = shares * c[i]
        tgt = frac * (cash + v) if frac else target
        if variant == "gate_full":
            if not on[i]:
                pend = -2 if shares > 0 else 0
            elif shares == 0:
                pend = 1
        if pend == 0 and (variant != "gate_full" or on[i]):
            if shares > 0 and v >= tgt * (hi_strong if st[i] else hi):
                pend = -1
            elif v <= tgt * lo and (variant == "article" or on[i]):
                pend = 1
        eq[i] = cash + v
    return eq, trims, buys, short


def stats_arr(eq, days):
    yrs = days / 365.25
    return (eq[-1] / eq[0]) ** (1 / yrs) - 1, (eq / np.maximum.accumulate(eq) - 1).min()
