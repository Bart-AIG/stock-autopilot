# Strategy report - INTRADAY  (2026-06-17 17:01 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.51 | 38.37 | 36.61 | price 36.51 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.51 | 1.1 | 36.51 | 34.66 | 39.83 | -5.1% |
| SLB | Energy |  |  | 51.26 | 2.4 | 51.26 | 48.39 | 55.76 | -5.6% |
| PSX | Energy |  |  | 169.44 | 4.9 | 169.44 | 162.31 | 180.14 | -4.2% |
| CVX | Energy |  |  | 178.41 | 7.0 | 178.41 | 171.4 | 188.93 | -3.9% |
| VLO | Energy |  |  | 242.17 | 7.6 | 242.17 | 228.75 | 261.45 | -5.5% |
| MPC | Energy |  |  | 247.69 | 7.8 | 247.69 | 233.81 | 267.21 | -5.6% |
| UNP | Other |  |  | 260.45 | 8.3 | 260.45 | 248.26 | 278.73 | -4.7% |
| WMT | Other |  |  | 118.69 | 9.1 | 118.69 | 112.57 | 127.87 | -5.2% |
| VZ | Other |  |  | 45.38 | 9.7 | 45.38 | 43.59 | 48.07 | -3.9% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 6/9 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 47.9 | T |
| 2 **TOP** | ONDS | 942.9 | 44.5 | T |
| 3 **TOP** | AAOI | 827.0 | 49.1 | T |
| 4 **TOP** | MU | 595.4 | 62.5 | T |
| 5 **TOP** | IREN | 500.0 | 52.7 | T |
| 6 **TOP** | TE | 493.2 | 56.5 | T |
| 7 **TOP** | APLD | 473.1 | 57.4 | T |
| 8 **TOP** | LASR | 459.0 | 44.5 | T |
| 9 **TOP** | WULF | 443.4 | 62.0 | T |
| 10 **TOP** | VIAV | 432.7 | 51.1 | T |
| 11 **TOP** | RKLB | 412.9 | 48.0 | T |
| 12 **TOP** | INTC | 399.4 | 57.9 | T |
| 13 **TOP** | COHR | 361.6 | 52.3 | T |
| 14 **TOP** | FCEL | 330.6 | 57.9 | T |
| 15 **TOP** | UUUU | 298.2 | 43.6 | F |
| 16 **TOP** | AMD | 259.3 | 59.0 | T |
| 17 **TOP** | LRCX | 229.2 | 67.7 | T |
| 18 **TOP** | ASTS | 225.7 | 45.7 | T |
| 19 **TOP** | POET | 201.7 | 50.2 | T |
| 20 **TOP** | WBD | 195.9 | 42.4 | T |
| 21 **TOP** | MTSI | 188.6 | 54.6 | T |
| 22  | MRVL | 164.9 | 61.9 | T |
| 23  | INOD | 157.9 | 59.2 | T |
| 24  | AMAT | 149.8 | 75.0 | T |
| 25  | UEC | 149.5 | 45.0 | F |
| 26  | CAT | 144.3 | 62.9 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 47.9 |  |
| ONDS | 942.9 | 44.5 | SPEC |
| AAOI | 827.0 | 49.1 | SPEC |
| MU | 595.4 | 62.5 |  |
| IREN | 500.0 | 52.7 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 36.4 |  |
| SMR | -56.6 | 46.7 | SPEC |
| ACHR | -55.5 | 45.7 | SPEC |
| WDAY | -52.8 | 43.0 |  |
| NOW | -50.3 | 44.9 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._