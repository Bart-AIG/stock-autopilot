# Strategy report - INTRADAY  (2026-06-17 19:02 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.37 | 38.37 | 36.61 | price 36.37 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.37 | 1.0 | 36.37 | 34.51 | 39.82 | -5.1% |
| SLB | Energy |  |  | 51.13 | 2.3 | 51.13 | 48.25 | 55.75 | -5.6% |
| PSX | Energy |  |  | 168.78 | 4.4 | 168.78 | 161.61 | 179.53 | -4.2% |
| UNP | Other |  |  | 257.21 | 6.2 | 257.21 | 244.56 | 276.18 | -4.9% |
| CVX | Energy |  |  | 178.03 | 6.4 | 178.03 | 171.02 | 188.55 | -3.9% |
| WMT | Other |  |  | 117.58 | 6.5 | 117.58 | 111.4 | 126.85 | -5.3% |
| MPC | Energy |  |  | 246.95 | 7.1 | 246.95 | 233.07 | 267.21 | -5.6% |
| VLO | Energy |  |  | 241.61 | 7.1 | 241.61 | 228.21 | 261.45 | -5.5% |
| KO | Other |  | HELD | 79.68 | 7.9 | 79.68 | 76.61 | 83.59 | -3.9% |
| VZ | Other |  |  | 45.31 | 9.3 | 45.31 | 43.51 | 48.02 | -4.0% |
| F | Other |  |  | 14.24 | 9.8 | 14.24 | 12.99 | 16.11 | -8.8% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL, KO. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 6/11 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 48.2 | T |
| 2 **TOP** | ONDS | 942.9 | 43.7 | T |
| 3 **TOP** | AAOI | 827.0 | 49.7 | T |
| 4 **TOP** | MU | 595.4 | 63.4 | T |
| 5 **TOP** | IREN | 500.0 | 53.8 | T |
| 6 **TOP** | TE | 493.2 | 57.0 | T |
| 7 **TOP** | APLD | 473.1 | 57.8 | T |
| 8 **TOP** | LASR | 459.0 | 42.9 | T |
| 9 **TOP** | WULF | 443.4 | 63.9 | T |
| 10 **TOP** | VIAV | 432.7 | 49.9 | T |
| 11 **TOP** | RKLB | 412.9 | 48.7 | T |
| 12 **TOP** | INTC | 399.4 | 58.6 | T |
| 13 **TOP** | COHR | 361.6 | 52.8 | T |
| 14 **TOP** | FCEL | 330.6 | 57.2 | T |
| 15 **TOP** | UUUU | 298.2 | 43.2 | F |
| 16 **TOP** | AMD | 259.3 | 59.1 | T |
| 17 **TOP** | LRCX | 229.2 | 67.3 | T |
| 18 **TOP** | ASTS | 225.7 | 46.8 | T |
| 19 **TOP** | POET | 201.7 | 50.4 | T |
| 20 **TOP** | WBD | 195.9 | 41.0 | T |
| 21 **TOP** | MTSI | 188.6 | 54.8 | T |
| 22  | MRVL | 164.9 | 62.9 | T |
| 23  | INOD | 157.9 | 57.1 | T |
| 24  | AMAT | 149.8 | 74.8 | T |
| 25  | UEC | 149.5 | 44.2 | F |
| 26  | CAT | 144.3 | 63.5 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 48.2 |  |
| ONDS | 942.9 | 43.7 | SPEC |
| AAOI | 827.0 | 49.7 | SPEC |
| MU | 595.4 | 63.4 |  |
| IREN | 500.0 | 53.8 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 34.3 |  |
| SMR | -56.6 | 48.0 | SPEC |
| ACHR | -55.5 | 43.3 | SPEC |
| WDAY | -52.8 | 41.3 |  |
| NOW | -50.3 | 43.4 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._