#!/usr/bin/env python3
"""
options_backtest.py: monthly SPY put selling on REAL option prices, 2018-2026. Research only:
no routine imports this and nothing here places an order.

Why it exists (Ryan, live turn 2026-11-13): "Why did we retire the options tracks? Did we never
determine a good way to implement options trading. ... Can we figure that out?"
Findings: docs/options-research-2026-11-13.md.

WHAT IS NEW: real historical option prices. Robinhood keeps daily bars for expired contracts
back to at least November 2017:
    get_option_instruments(chain_symbol="SPY", expiration_dates=..., type="put",
                           state="expired", strike_price="264.0000")   -> the contract id
    get_option_historicals(instrument_ids=[...], start_time=..., end_time=..., interval="day")
Before June 2020 a bar's open equals its close (one price a day, and it is the close: checked
against SPY's intrinsic value on 2020-03-12, 03-13 and 03-20). The high and low fields are
noisy and are not used. Bars flagged "interpolated" carry no trade and are treated as missing.
The earlier work on file (docs/strategy-shortlist.md) had no option prices and said so.

THE TEST
  Entry   the close of the first trading day after each monthly expiration, into the next
          monthly expiration (25 to 35 days out). 106 cycles, 2017-12-18 to 2026-10-16.
  Strikes spot x (1 - z x VIX x sqrt(days/365)) for z = 0, 0.5, 1, 1.5, 2. On 2026-11-13 the
          z = 0.5 strike was a 27-delta put and z = 1.0 a 16-delta put.
  Exit    expiration, at SPY's close.
  Costs   half a bid/ask spread per leg at entry (max of 1 cent and 0.4% of the leg's price;
          measured 2026-11-13: 1.5 to 2 cents on $3.50 to $8 legs), $0.04 a contract in
          regulatory fees, and a second crossing when the short strike ends within 1% of the
          money or in it (the broker closes those near the bell).
  Fixed-width spreads take the long leg's price from implied volatility interpolated between
  the pulled strikes. Check on the live chain of 2026-11-13: within half a cent on 6 strikes.

USAGE
  python3 options_backtest.py            the tables at the modelled cost
  python3 options_backtest.py --cost 2   the same at twice the cost
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "options" / "spy_put_cycles.json"
ZS = (0, 0.5, 1.0, 1.5, 2.0)


def N(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs_put(S: float, K: float, T: float, v: float) -> float:
    if v <= 0 or T <= 0:
        return max(K - S, 0.0)
    d1 = (math.log(S / K) + 0.5 * v * v * T) / (v * math.sqrt(T))
    return K * N(-(d1 - v * math.sqrt(T))) - S * N(-d1)


def iv_put(S: float, K: float, T: float, p: float) -> float:
    lo, hi = 1e-4, 5.0
    if p <= max(K - S, 0) + 1e-9:
        return lo
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if bs_put(S, K, T, mid) > p:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def load(path: Path = DATA) -> pd.DataFrame:
    rows = []
    for c in json.loads(path.read_text())["cycles"]:
        S0, T = c["spot"], c["dte"] / 365
        ks = [l["strike"] for l in c["legs"]]
        ivs = [iv_put(S0, l["strike"], T, l["px"]) for l in c["legs"]]
        r = {"n": c["n"], "entry": c["entry"], "exp": c["exp"], "dte": c["dte"], "S0": S0, "ST": c["exp_close"],
             "vix": c["vix"], "spy_ret": c["spy_total_return"], "above200": c["above_200d"], "ret5": c["ret_5d"]}
        for l in c["legs"]:
            r[f"K{l['z']}"], r[f"P{l['z']}"] = l["strike"], l["px"]
        for z in (0.5, 1.0):
            for w in (5, 10):
                k = r[f"K{z}"] - w
                r[f"Pw{z}_{w}"] = bs_put(S0, k, T, float(np.interp(k, ks[::-1], ivs[::-1])))
        rows.append(r)
    return pd.DataFrame(rows)


class Costs:
    def __init__(self, mult: float = 1.0):
        self.mult = mult
        self.fee = 0.0004 * mult                       # $0.04 a contract, per share

    def half(self, px):
        return self.mult * np.maximum(0.01, 0.004 * np.asarray(px, dtype=float))


def payoff(K, ST):
    return np.maximum(np.asarray(K, dtype=float) - ST, 0.0)


def spread(Ks, Ps, Kl, Pl, ST, cost: Costs):
    """Short put Ks, long put Kl below it. Per share: (net credit, max loss, net P/L)."""
    credit = Ps - Pl - cost.half(Ps) - cost.half(Pl) - 2 * cost.fee
    loss = payoff(Ks, ST) - payoff(Kl, ST)
    near = ST < Ks * 1.01
    exit_cost = np.where(near, cost.half(np.maximum(payoff(Ks, ST), 0.05))
                         + cost.half(np.maximum(payoff(Kl, ST), 0.05)) + 2 * cost.fee, 0.0)
    return credit, (Ks - Kl) - credit, credit - loss - exit_cost


def cash_secured(K, P, ST, cost: Costs):
    credit = P - cost.half(P) - cost.fee
    near = ST < K * 1.01
    exit_cost = np.where(near, cost.half(np.maximum(payoff(K, ST), 0.05)) + cost.fee, 0.0)
    return credit, K - credit, credit - payoff(K, ST) - exit_cost


def years(df: pd.DataFrame) -> float:
    return (pd.Timestamp(df.exp.iloc[-1]) - pd.Timestamp(df.entry.iloc[0])).days / 365.25


def growth(R, f: float, yrs: float) -> tuple[float, float]:
    """Capital path when a fraction f of capital is at maximum risk every cycle: (CAGR %, max DD %)."""
    eq = np.cumprod(1 + f * np.asarray(R, dtype=float))
    if eq.min() <= 0:
        return float("nan"), -100.0
    return 100 * (eq[-1] ** (1 / yrs) - 1), 100 * (eq / np.maximum.accumulate(eq) - 1).min()


def stats(label: str, credit, risk, pnl, yrs: float | None = None) -> dict:
    R = pnl / risk
    n = len(R)
    out = {"structure": label, "n": n, "win %": round(100 * (pnl > 0).mean(), 1),
           "credit $": round(100 * credit.mean(), 1), "max risk $": round(100 * risk.mean()),
           "avg P/L $": round(100 * pnl.mean(), 2), "worst $": round(100 * pnl.min()),
           "total $": round(100 * pnl.sum()), "P/L per $100 risk": round(100 * R.mean(), 2),
           "t": round(R.mean() / (R.std(ddof=1) / math.sqrt(n)), 2) if n > 2 else float("nan")}
    if yrs:
        for f in (0.1, 0.2, 0.5):
            g, dd = growth(R, f, yrs)
            out[f"{int(f * 100)}% at risk: CAGR/maxDD"] = f"{g:.1f}% / {dd:.0f}%"
    return out


def tables(df: pd.DataFrame, cost: Costs) -> dict:
    ST, yrs = df.ST.values, years(df)
    main = [stats(f"cash-secured put, z={z}", *cash_secured(df[f"K{z}"].values, df[f"P{z}"].values, ST, cost), yrs)
            for z in (0, 0.5, 1.0)]
    for z in (0.5, 1.0):
        for w in (5, 10):
            main.append(stats(f"put spread, short z={z}, ${w} wide",
                              *spread(df[f"K{z}"].values, df[f"P{z}"].values, df[f"K{z}"].values - w,
                                      df[f"Pw{z}_{w}"].values, ST, cost), yrs))
    for a, b in ((0, 1.0), (0.5, 1.0), (0.5, 2.0), (1.0, 2.0)):
        main.append(stats(f"put spread, short z={a} / long z={b}",
                          *spread(df[f"K{a}"].values, df[f"P{a}"].values, df[f"K{b}"].values,
                                  df[f"P{b}"].values, ST, cost), yrs))
    c5, r5, p5 = spread(df["K0.5"].values, df["P0.5"].values, df["K0.5"].values - 5, df["Pw0.5_5"].values, ST, cost)
    year = df.exp.str[:4]
    by_year = pd.DataFrame({"year": year, "pnl": 100 * p5}).groupby("year").pnl.agg(["count", "sum", "min"]).round(0)
    splits = []
    for lab, m in (("SPY above its 200-day at entry", df.above200.values), ("SPY below its 200-day at entry", ~df.above200.values),
                   ("VIX 20 or higher at entry", df.vix.values >= 20), ("VIX under 20 at entry", df.vix.values < 20),
                   ("VIX under 14 at entry", df.vix.values < 14),
                   ("SPY down over the prior 5 days", df.ret5.values < 0), ("SPY up over the prior 5 days", df.ret5.values >= 0),
                   ("expiring 2018-2021", (year <= "2021").values), ("expiring 2022-2026", (year >= "2022").values)):
        splits.append(stats(lab, c5[m], r5[m], p5[m]))
    R5 = p5 / r5
    rng = np.random.default_rng(7)
    boot = np.array([rng.choice(R5, len(R5)).mean() for _ in range(20000)])
    bh = np.cumprod(1 + df.spy_ret.values)
    pw = cash_secured(df["K0"].values, df["P0"].values, ST, cost)
    head = {
        "cycles": len(df), "first entry": df.entry.iloc[0], "last expiration": df.exp.iloc[-1], "years": round(yrs, 2),
        "cost multiple": cost.mult, "average days to expiration": round(float(df.dte.mean()), 1),
        "SPY held over the same cycles, CAGR %": round(100 * (bh[-1] ** (1 / yrs) - 1), 1),
        "SPY max drawdown at cycle ends %": round(100 * (bh / np.maximum.accumulate(bh) - 1).min(), 1),
        "cash-secured at-the-money put, CAGR % (no interest on the cash)": round(growth(pw[2] / df["K0"].values, 1.0, yrs)[0], 1),
        "5-wide spread, short z=0.5": {
            "losing cycles": int((p5 < 0).sum()), "average loss $": round(float(100 * p5[p5 < 0].mean())),
            "average win $": round(float(100 * p5[p5 > 0].mean())),
            "mean P/L per $100 of risk, per cycle": round(float(100 * R5.mean()), 2),
            "90% interval (bootstrap)": [round(float(x), 2) for x in 100 * np.percentile(boot, [5, 95])],
            "chance the true mean is zero or less": round(float((boot <= 0).mean()), 3),
            "best capital fraction at risk -> CAGR / maxDD": {f"{int(f * 100)}%": "{:.1f}% / {:.0f}%".format(*growth(R5, f, yrs))
                                                              for f in (0.05, 0.10, 0.15, 0.20, 0.30)},
        },
    }
    return {"head": head, "main": pd.DataFrame(main), "by_year": by_year, "splits": pd.DataFrame(splits)}


def main(argv: list[str]) -> int:
    mult = float(argv[argv.index("--cost") + 1]) if "--cost" in argv else 1.0
    t = tables(load(), Costs(mult))
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    print(json.dumps(t["head"], indent=1))
    print("\nPer one contract or one spread, every month:")
    print(t["main"].to_string(index=False))
    print("\n5-wide spread, short z=0.5, by expiration year ($ per one spread):")
    print(t["by_year"].T.to_string())
    print("\n5-wide spread, short z=0.5, split by the conditions at entry:")
    print(t["splits"].to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
