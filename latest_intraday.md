# Strategy report - INTRADAY  (2026-08-18 19:03 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | Semis |  |  | 2026-09-02 | 379.21 | 1.6 | 379.21 | 353.74 | 417.42 | -6.7% |
| DE | Other |  |  | ⚠️ 2026-08-20 | 591.62 | 3.0 | 591.62 | 563.17 | 634.3 | -4.8% |
| ALAB | Other |  |  |  | 298.84 | 4.4 | 298.84 | 244.88 | 361.67 | -18.1% ⚠ |
| ARM | Semis |  |  |  | 253.2 | 5.7 | 253.2 | 216.45 | 286.68 | -14.5% |
| BA | Other |  |  |  | 223.67 | 6.6 | 223.67 | 208.95 | 240.19 | -6.6% |
| HON | Other |  |  |  | 227.91 | 7.7 | 227.91 | 215.18 | 247.0 | -5.6% |
| GM | Other |  |  |  | 84.09 | 8.2 | 84.09 | 79.58 | 90.3 | -5.4% |
| BE | Other |  |  |  | 207.46 | 9.5 | 207.46 | 163.33 | 237.16 | -21.3% ⚠ |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** DE (2026-08-20). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ⚠️ **2 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 22 of 229)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | BE | 760.2 | 44.3 | T |
| 2 **TOP** | MU | 642.2 | 51.6 | T |
| 3 **TOP** | LITE | 616.9 | 53.0 | T |
| 4 **TOP** | AEHR | 437.8 | 58.5 | T |
| 5 **TOP** | TSEM | 382.3 | 49.1 | T |
| 6 **TOP** | INTC | 311.4 | 44.7 | T |
| 7 **TOP** | VIAV | 274.1 | 49.7 | T |
| 8 **TOP** | AAOI | 257.7 | 52.4 | T |
| 9 **TOP** | WULF | 254.0 | 37.8 | F |
| 10 **TOP** | FCEL | 248.4 | 49.7 | T |
| 11 **TOP** | LASR | 246.9 | 38.3 | F |
| 12 **TOP** | NBIS | 236.6 | 56.2 | T |
| 13 **TOP** | AMD | 215.8 | 46.8 | T |
| 14 **TOP** | LRCX | 211.2 | 51.1 | T |
| 15 **TOP** | DELL | 202.0 | 55.9 | T |
| 16 **TOP** | ALAB | 197.3 | 43.5 | T |
| 17 **TOP** | ONDS | 192.8 | 53.7 | F |
| 18 **TOP** | GLW | 186.3 | 48.3 | T |
| 19 **TOP** | COHR | 178.7 | 47.9 | T |
| 20 **TOP** | AMAT | 178.1 | 45.6 | T |
| 21 **TOP** | MRVL | 152.8 | 49.4 | T |
| 22 **TOP** | KLAC | 128.5 | 43.7 | T |
| 23  | CRDO | 116.8 | 51.3 | T |
| 24  | APLD | 116.2 | 43.6 | F |
| 25  | NOK | 113.1 | 49.6 | T |
| 26  | CAT | 112.8 | 43.3 | T |
| 27  | VLO | 111.9 | 75.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | CVS | Other | 94.75 | 37.0 | 45.5 | -6.2% | -7.3% | 73.5 | 24.7 | 10.3 | 3.9 | ⚠️ rich |
| 🟡 dip | UNH | Other | 395.75 | 39.0 | 21.6 | -3.9% | -4.7% | 50.7 | 25.5 | 15.2 | -0.8 | ✅ value |
| 🟡 dip | TKR | Other | 129.23 | 42.9 | 17.9 | -3.8% | -5.8% | 74.1 | 34.8 | 23.3 | -2.1 | ✅ value |
| 🟢 oversold | ALAB | Other | 298.62 | 43.5 | 4.4 | -4.2% | -15.6% | 197.3 | 137.7 | 185.2 | 0.5 | ✅ value |
| 🟢 oversold | BE | Other | 207.09 | 44.3 | 9.5 | -2.5% | -15.4% | 760.2 | 248.0 | 97.2 | -0.0 | ⚠️ rich |
| 🟡 dip | GOOGL | Other | 342.81 | 45.4 | 13.5 | -0.9% | -2.8% | 87.4 | 17.0 | 77.9 | 0.2 | ✅ value |
| 🟡 dip | AMD | Semis | 480.22 | 46.8 | 22.0 | -2.2% | -5.9% | 215.8 | 121.9 | 93.2 | 1.0 | ✅ value |
| 🟡 dip | COHR | Photonics | 308.5 | 47.9 | 24.1 | +0.6% | -7.8% | 178.7 | 71.0 | -1.0 | 0.0 | — |
| 🟡 dip | GLW | Other | 159.35 | 48.3 | 28.8 | +4.5% | -9.3% | 186.3 | 72.1 | 57.3 | 0.5 | ✅ value |
| 🟡 dip | DDOG | AI-software | 248.73 | 48.3 | 44.6 | -2.5% | -0.2% | 78.4 | 499.6 | 76.6 | 12.8 | ⚠️ rich |
| 🟡 dip | TSEM | Semis | 238.94 | 49.1 | 13.3 | +0.9% | -2.3% | 382.3 | 96.2 | 90.6 | 2.1 | — |
| 🟡 dip | MRVL | Semis | 213.46 | 49.4 | 25.7 | +4.3% | -9.3% | 152.8 | 72.7 | 112.5 | 0.0 | ⚠️ rich |
| 🟡 dip | NOK | Comm | 10.35 | 49.6 | 26.1 | +7.3% | -10.4% | 113.1 | 70.2 | 92.7 | -2.5 | ⚠️ rich |
| 🟡 dip | FCEL | Battery/H2 | 21.2 | 49.7 | 32.7 | -0.0% | -2.5% | 248.4 | -3.2 | -13.8 | 0.0 | — |
| 🟡 dip | IBKR | Financials | 90.63 | 49.7 | 28.1 | +0.5% | -1.0% | 41.3 | 35.8 | 9.9 | 1.1 | ✅ value |
| 🟡 dip | MU | Semis | 934.57 | 51.6 | 30.1 | +4.4% | -2.9% | 642.2 | — | — | — |  |
| 🟡 dip | AAOI | Photonics | 133.25 | 52.4 | 25.5 | +12.3% | +0.9% | 257.7 | — | — | — |  |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | LIN | Other | 479.9 | 38.7 | 56.9 | -2.6% | -5.8% | 10.4 | 30.8 | 44.6 | 3.0 | — |
| 🟡 dip | ON | Semis | 78.52 | 40.0 | 14.8 | -5.1% | -17.5% | 43.9 | 49.8 | 17.3 | 1.1 | ✅ value |
| 🟢 oversold | AVGO | Semis | 378.64 | 40.7 | 1.6 | -5.3% | -2.9% | 30.9 | 61.3 | 55.1 | 0.5 | ✅ value |
| 🟢 oversold | ARM | Semis | 252.55 | 41.7 | 5.7 | -4.7% | -17.7% | 70.5 | 261.1 | 183.5 | 5.6 | ⚠️ rich |
| 🟡 dip | TXN | Semis | 270.75 | 42.4 | 20.8 | -3.0% | -7.1% | 31.1 | 41.0 | 46.2 | 2.1 | — |
| 🟡 dip | CSCO | Other | 111.89 | 42.5 | 23.2 | -3.9% | -4.3% | 64.5 | 33.3 | 32.4 | 1.1 | ✅ value |
| 🟢 oversold | DE | Other | 591.67 | 43.2 | 3.0 | -3.3% | -1.8% | 19.5 | 33.4 | 42.4 | -2.3 | — |
| 🟡 dip | CAT | Other | 836.94 | 43.3 | 23.8 | -1.7% | -8.0% | 112.8 | 35.9 | 31.0 | 2.0 | — |
| 🟡 dip | KLAC | Semis | 192.73 | 43.7 | 12.0 | -2.3% | -13.0% | 128.5 | 52.4 | 66.9 | 2.6 | — |
| 🟡 dip | ADI | Semis | 372.15 | 44.6 | 12.8 | -1.3% | -4.6% | 55.2 | 55.1 | 39.7 | 0.7 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BE | 760.2 | 44.3 |  |
| MU | 642.2 | 51.6 |  |
| LITE | 616.9 | 53.0 |  |
| AEHR | 437.8 | 58.5 |  |
| TSEM | 382.3 | 49.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| SMR | -84.6 | 44.5 | SPEC |
| BYND | -83.1 | 33.5 |  |
| COIN | -62.6 | 43.4 |  |
| QUBT | -60.0 | 47.5 | SPEC |
| QS | -60.0 | 44.1 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._