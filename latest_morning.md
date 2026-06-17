# Strategy report - MORNING  (2026-06-17 16:42 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.48 | 38.37 | 36.61 | price 36.48 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.48 | 1.1 | 36.48 | 34.63 | 39.83 | -5.1% |
| SLB | Energy |  |  | 51.41 | 2.6 | 51.41 | 48.55 | 55.76 | -5.6% |
| PSX | Energy |  |  | 169.34 | 4.8 | 169.34 | 162.2 | 180.04 | -4.2% |
| VLO | Energy |  |  | 241.75 | 7.2 | 241.75 | 228.35 | 261.45 | -5.5% |
| MPC | Energy |  |  | 247.54 | 7.7 | 247.54 | 233.66 | 267.21 | -5.6% |
| CVX | Energy |  |  | 178.86 | 7.8 | 178.86 | 171.84 | 189.38 | -3.9% |
| UNP | Other |  |  | 260.66 | 8.5 | 260.66 | 248.49 | 278.91 | -4.7% |
| WMT | Other |  |  | 118.79 | 9.5 | 118.79 | 112.67 | 127.96 | -5.1% |
| VZ | Other |  |  | 45.4 | 9.7 | 45.4 | 43.61 | 48.08 | -3.9% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 6/9 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 48.0 | T |
| 2 **TOP** | ONDS | 942.9 | 44.3 | T |
| 3 **TOP** | AAOI | 827.0 | 49.0 | T |
| 4 **TOP** | MU | 595.4 | 62.7 | T |
| 5 **TOP** | IREN | 500.0 | 52.3 | T |
| 6 **TOP** | TE | 493.2 | 56.8 | T |
| 7 **TOP** | APLD | 473.1 | 56.7 | T |
| 8 **TOP** | LASR | 459.0 | 44.3 | T |
| 9 **TOP** | WULF | 443.4 | 62.1 | T |
| 10 **TOP** | VIAV | 432.7 | 50.9 | T |
| 11 **TOP** | RKLB | 412.9 | 48.1 | T |
| 12 **TOP** | INTC | 399.4 | 57.8 | T |
| 13 **TOP** | COHR | 361.6 | 52.6 | T |
| 14 **TOP** | FCEL | 330.6 | 58.1 | T |
| 15 **TOP** | UUUU | 298.2 | 43.0 | F |
| 16 **TOP** | AMD | 259.3 | 59.1 | T |
| 17 **TOP** | LRCX | 229.2 | 67.8 | T |
| 18 **TOP** | ASTS | 225.7 | 45.7 | T |
| 19 **TOP** | POET | 201.7 | 50.3 | T |
| 20 **TOP** | WBD | 195.9 | 42.5 | T |
| 21 **TOP** | MTSI | 188.6 | 54.4 | T |
| 22  | MRVL | 164.9 | 62.1 | T |
| 23  | INOD | 157.9 | 59.4 | T |
| 24  | AMAT | 149.8 | 75.1 | T |
| 25  | UEC | 149.5 | 44.2 | F |
| 26  | CAT | 144.3 | 63.3 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 48.0 |  |
| ONDS | 942.9 | 44.3 | SPEC |
| AAOI | 827.0 | 49.0 | SPEC |
| MU | 595.4 | 62.7 |  |
| IREN | 500.0 | 52.3 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 37.0 |  |
| SMR | -56.6 | 46.2 | SPEC |
| ACHR | -55.5 | 45.9 | SPEC |
| WDAY | -52.8 | 43.4 |  |
| NOW | -50.3 | 45.4 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._