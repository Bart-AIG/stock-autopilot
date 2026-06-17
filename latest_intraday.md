# Strategy report - INTRADAY  (2026-06-17 18:02 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.27 | 38.37 | 36.61 | price 36.27 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.27 | 0.9 | 36.27 | 34.41 | 39.82 | -5.1% |
| SLB | Energy |  |  | 50.69 | 2.0 | 50.69 | 47.75 | 55.73 | -5.8% |
| PSX | Energy |  |  | 169.14 | 4.7 | 169.14 | 161.99 | 179.86 | -4.2% |
| CVX | Energy |  |  | 178.03 | 6.4 | 178.03 | 171.02 | 188.55 | -3.9% |
| WMT | Other |  |  | 118.04 | 7.3 | 118.04 | 111.89 | 127.26 | -5.2% |
| VLO | Energy |  |  | 241.93 | 7.4 | 241.93 | 228.52 | 261.45 | -5.5% |
| UNP | Other |  |  | 259.34 | 7.4 | 259.34 | 247.01 | 277.83 | -4.8% |
| MPC | Energy |  |  | 247.72 | 7.9 | 247.72 | 233.85 | 267.21 | -5.6% |
| CSCO | Other |  |  | 118.03 | 8.7 | 118.03 | 110.56 | 129.24 | -6.3% |
| VZ | Other |  |  | 45.33 | 9.4 | 45.33 | 43.53 | 48.02 | -4.0% |
| F | Other |  |  | 14.22 | 9.4 | 14.22 | 12.97 | 16.09 | -8.8% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 6/11 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 47.9 | T |
| 2 **TOP** | ONDS | 942.9 | 44.3 | T |
| 3 **TOP** | AAOI | 827.0 | 49.2 | T |
| 4 **TOP** | MU | 595.4 | 62.7 | T |
| 5 **TOP** | IREN | 500.0 | 53.6 | T |
| 6 **TOP** | TE | 493.2 | 57.0 | T |
| 7 **TOP** | APLD | 473.1 | 57.8 | T |
| 8 **TOP** | LASR | 459.0 | 43.9 | T |
| 9 **TOP** | WULF | 443.4 | 63.0 | T |
| 10 **TOP** | VIAV | 432.7 | 49.6 | T |
| 11 **TOP** | RKLB | 412.9 | 48.2 | T |
| 12 **TOP** | INTC | 399.4 | 57.9 | T |
| 13 **TOP** | COHR | 361.6 | 52.7 | T |
| 14 **TOP** | FCEL | 330.6 | 57.2 | T |
| 15 **TOP** | UUUU | 298.2 | 43.2 | F |
| 16 **TOP** | AMD | 259.3 | 59.0 | T |
| 17 **TOP** | LRCX | 229.2 | 67.5 | T |
| 18 **TOP** | ASTS | 225.7 | 46.9 | T |
| 19 **TOP** | POET | 201.7 | 50.3 | T |
| 20 **TOP** | WBD | 195.9 | 41.4 | T |
| 21 **TOP** | MTSI | 188.6 | 54.4 | T |
| 22  | MRVL | 164.9 | 62.2 | T |
| 23  | INOD | 157.9 | 58.8 | T |
| 24  | AMAT | 149.8 | 75.1 | T |
| 25  | UEC | 149.5 | 44.7 | F |
| 26  | CAT | 144.3 | 63.1 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 47.9 |  |
| ONDS | 942.9 | 44.3 | SPEC |
| AAOI | 827.0 | 49.2 | SPEC |
| MU | 595.4 | 62.7 |  |
| IREN | 500.0 | 53.6 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 35.7 |  |
| SMR | -56.6 | 46.6 | SPEC |
| ACHR | -55.5 | 45.0 | SPEC |
| WDAY | -52.8 | 43.1 |  |
| NOW | -50.3 | 44.8 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._