# Strategy report - INTRADAY  (2026-06-17 16:01 UTC)

## >>> ACTION <<<

## SELL / EXIT signals (your holdings)
Positions whose exit rule fired. Confirm with a live quote and approve each sell in-session.

| Ticker | Sleeve | Price | Entry | Stop | Why exit |
|---|---|---|---|---|---|
| HAL | swing | 36.58 | 38.37 | 36.61 | price 36.58 <= stop 36.61 |

- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — LITE, ONDS, AAOI, MU, IREN, TE, APLD, LASR. If buying power is tight, fund a new entry by exiting the weakest above.

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| HAL | Energy |  | HELD | 36.58 | 1.1 | 36.58 | 34.73 | 39.83 | -5.1% |
| SLB | Energy |  |  | 51.62 | 2.8 | 51.62 | 48.78 | 55.88 | -5.5% |
| PSX | Energy |  |  | 168.5 | 4.2 | 168.5 | 161.31 | 179.28 | -4.3% |
| VLO | Energy |  |  | 238.43 | 5.0 | 238.43 | 224.99 | 258.6 | -5.6% |
| MPC | Energy |  |  | 245.81 | 6.2 | 245.81 | 231.92 | 266.65 | -5.7% |
| CVX | Energy |  |  | 179.19 | 8.6 | 179.19 | 172.16 | 189.73 | -3.9% |
| UNP | Other |  |  | 261.11 | 9.0 | 261.11 | 248.99 | 279.29 | -4.6% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** HAL. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🟡 **Cluster:** 6/7 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 21 of 214)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 1035.3 | 48.0 | T |
| 2 **TOP** | ONDS | 942.9 | 43.5 | T |
| 3 **TOP** | AAOI | 827.0 | 48.7 | T |
| 4 **TOP** | MU | 595.4 | 62.6 | T |
| 5 **TOP** | IREN | 500.0 | 51.3 | T |
| 6 **TOP** | TE | 493.2 | 56.2 | T |
| 7 **TOP** | APLD | 473.1 | 56.0 | T |
| 8 **TOP** | LASR | 459.0 | 43.6 | T |
| 9 **TOP** | WULF | 443.4 | 61.0 | T |
| 10 **TOP** | VIAV | 432.7 | 50.4 | T |
| 11 **TOP** | RKLB | 412.9 | 46.8 | T |
| 12 **TOP** | INTC | 399.4 | 57.4 | T |
| 13 **TOP** | COHR | 361.6 | 52.6 | T |
| 14 **TOP** | FCEL | 330.6 | 58.4 | T |
| 15 **TOP** | UUUU | 298.2 | 43.0 | F |
| 16 **TOP** | AMD | 259.3 | 59.4 | T |
| 17 **TOP** | LRCX | 229.2 | 68.5 | T |
| 18 **TOP** | ASTS | 225.7 | 44.8 | T |
| 19 **TOP** | POET | 201.7 | 49.8 | T |
| 20 **TOP** | WBD | 195.9 | 42.5 | T |
| 21 **TOP** | MTSI | 188.6 | 54.1 | T |
| 22  | MRVL | 164.9 | 61.8 | T |
| 23  | INOD | 157.9 | 58.3 | T |
| 24  | AMAT | 149.8 | 75.6 | T |
| 25  | UEC | 149.5 | 44.8 | F |
| 26  | CAT | 144.3 | 62.9 | T |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LITE | 1035.3 | 48.0 |  |
| ONDS | 942.9 | 43.5 | SPEC |
| AAOI | 827.0 | 48.7 | SPEC |
| MU | 595.4 | 62.6 |  |
| IREN | 500.0 | 51.3 | SPEC |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LULU | -62.6 | 38.4 |  |
| SMR | -56.6 | 46.5 | SPEC |
| ACHR | -55.5 | 45.1 | SPEC |
| WDAY | -52.8 | 42.8 |  |
| NOW | -50.3 | 45.2 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._