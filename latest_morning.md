# Strategy report - MORNING  (2026-06-17 14:01 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.28 | 38.37 | 36.61 | price 36.28 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.28 | 1.0 | 36.28 | 34.42 | 39.82 | -5.1% |
| SLB | Energy |  |  | 51.25 | 2.4 | 51.25 | 48.38 | 55.76 | -5.6% |
| PSX | Energy |  |  | 168.57 | 4.2 | 168.57 | 161.39 | 179.34 | -4.3% |
| VLO | Energy |  |  | 241.04 | 6.6 | 241.04 | 227.65 | 261.13 | -5.6% |
| KO | Other |  | HELD | 79.48 | 7.0 | 79.48 | 76.41 | 83.59 | -3.9% |
| CVX | Energy |  |  | 178.56 | 7.3 | 178.56 | 171.55 | 189.08 | -3.9% |
| MPC | Energy |  |  | 247.68 | 7.8 | 247.68 | 233.81 | 267.21 | -5.6% |
| CSCO | Other |  |  | 118.25 | 9.5 | 118.25 | 110.78 | 129.46 | -6.3% |
| EOG | Energy |  |  | 131.93 | 9.5 | 131.93 | 125.98 | 140.86 | -4.5% |
| UNP | Other |  |  | 261.88 | 9.8 | 261.88 | 249.82 | 279.39 | -4.6% |
| MRK | Other |  | HELD | 114.13 | 9.9 | 114.13 | 107.84 | 122.41 | -5.5% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL, KO, MRK. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 7/11 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 46.5 | T |
| 2 **TOP** | ONDS | 942.9 | 42.2 | F |
| 3 **TOP** | AAOI | 827.0 | 48.4 | T |
| 4 **TOP** | MU | 595.4 | 60.6 | T |
| 5 **TOP** | IREN | 500.0 | 51.2 | T |
| 6 **TOP** | TE | 493.2 | 54.1 | T |
| 7 **TOP** | APLD | 473.1 | 57.3 | T |
| 8 **TOP** | LASR | 459.0 | 43.4 | T |
| 9 **TOP** | WULF | 443.4 | 60.0 | T |
| 10 **TOP** | VIAV | 432.7 | 49.7 | T |
| 11 **TOP** | RKLB | 412.9 | 47.1 | T |
| 12 **TOP** | INTC | 399.4 | 55.6 | T |
| 13 **TOP** | COHR | 361.6 | 50.9 | T |
| 14 **TOP** | FCEL | 330.6 | 54.8 | T |
| 15 **TOP** | UUUU | 298.2 | 42.4 | F |
| 16 **TOP** | AMD | 259.3 | 57.3 | T |
| 17 **TOP** | LRCX | 229.2 | 68.1 | T |
| 18 **TOP** | ASTS | 225.7 | 45.0 | T |
| 19 **TOP** | POET | 201.7 | 49.8 | T |
| 20 **TOP** | WBD | 195.9 | 41.4 | T |
| 21 **TOP** | MTSI | 188.6 | 54.0 | T |
| 22  | MRVL | 164.9 | 60.3 | T |
| 23  | INOD | 157.9 | 59.0 | T |
| 24  | AMAT | 149.8 | 75.4 | T |
| 25  | UEC | 149.5 | 44.7 | F |
| 26  | CAT | 144.3 | 62.4 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 46.5 |  |
| AAOI | 827.0 | 48.4 | SPEC |
| MU | 595.4 | 60.6 |  |
| IREN | 500.0 | 51.2 | SPEC |
| TE | 493.2 | 54.1 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 39.6 |  |
| SMR | -56.6 | 44.0 | SPEC |
| ACHR | -55.5 | 40.9 | SPEC |
| WDAY | -52.8 | 45.2 |  |
| NOW | -50.3 | 47.0 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._