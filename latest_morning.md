# Strategy report - MORNING  (2026-08-19 14:02 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Connors RSI(2) swing setups (1-3 week holds)
Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.

| Ticker | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|
| ALAB | Other |  |  |  | 288.47 | 2.1 | 288.47 | 236.59 | 361.67 | -18.0% ⚠ |
| CRWD | AI-software |  |  | ⚠️ 2026-08-26 | 200.83 | 2.4 | 200.83 | 185.85 | 223.3 | -7.5% |
| ARM | Semis |  |  |  | 248.23 | 4.0 | 248.23 | 212.23 | 286.68 | -14.5% |
| HON | Other |  |  |  | 225.51 | 4.0 | 225.51 | 213.0 | 244.29 | -5.6% |
| BA | Other |  |  |  | 221.85 | 4.4 | 221.85 | 207.27 | 240.19 | -6.6% |
| DELL | Other |  |  | 2026-09-03 | 439.83 | 5.3 | 439.83 | 383.85 | 494.51 | -12.7% |
| ETN | Other |  |  |  | 422.29 | 5.4 | 422.29 | 385.54 | 459.96 | -8.7% |
| BE | Other |  |  |  | 203.33 | 7.1 | 203.33 | 160.36 | 237.16 | -21.1% ⚠ |
| INTC | Semis |  |  |  | 92.79 | 7.2 | 92.79 | 81.4 | 104.56 | -12.3% |
| KLAC | Semis |  |  |  | 188.98 | 7.5 | 188.98 | 169.03 | 218.73 | -10.6% |
| TSEM | Semis |  |  |  | 229.31 | 7.9 | 229.31 | 188.91 | 265.48 | -17.6% ⚠ |
| NET | AI-software |  |  |  | 291.06 | 8.0 | 291.06 | 266.65 | 327.68 | -8.4% |
| GOOGL | Other |  |  |  | 342.14 | 9.8 | 342.14 | 317.32 | 377.65 | -7.3% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** CRWD (2026-08-26). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 4/13 setups are 'Semis' — correlated, don't buy them all.
- ⚠️ **3 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap ~15-20%, and set the stop on every entry.

## 12-1 momentum ranking (top decile = 22 of 229)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | BE | 688.6 | 43.2 | T |
| 2 **TOP** | MU | 656.6 | 50.9 | T |
| 3 **TOP** | LITE | 648.9 | 50.4 | T |
| 4 **TOP** | AEHR | 413.3 | 52.4 | T |
| 5 **TOP** | TSEM | 368.1 | 46.3 | T |
| 6 **TOP** | INTC | 320.2 | 42.0 | T |
| 7 **TOP** | VIAV | 286.6 | 48.0 | T |
| 8 **TOP** | FCEL | 273.6 | 46.8 | T |
| 9 **TOP** | WULF | 267.6 | 36.7 | F |
| 10 **TOP** | AAOI | 259.8 | 50.4 | T |
| 11 **TOP** | NBIS | 245.9 | 49.6 | T |
| 12 **TOP** | LASR | 242.2 | 36.7 | F |
| 13 **TOP** | AMD | 220.8 | 44.5 | T |
| 14 **TOP** | ONDS | 208.1 | 51.6 | F |
| 15 **TOP** | LRCX | 204.7 | 48.9 | T |
| 16 **TOP** | ALAB | 202.6 | 41.3 | T |
| 17 **TOP** | DELL | 191.0 | 49.5 | T |
| 18 **TOP** | COHR | 186.5 | 45.7 | T |
| 19 **TOP** | GLW | 183.5 | 45.5 | T |
| 20 **TOP** | AMAT | 176.0 | 43.7 | T |
| 21 **TOP** | MRVL | 161.1 | 55.8 | T |
| 22 **TOP** | APLD | 133.4 | 40.6 | F |
| 23  | CRDO | 126.9 | 49.0 | T |
| 24  | IREN | 124.1 | 47.6 | F |
| 25  | KLAC | 123.0 | 42.0 | T |
| 26  | VLO | 114.4 | 72.1 | T |
| 27  | NOK | 112.2 | 49.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | UNH | Other | 394.86 | 38.8 | 32.5 | -3.6% | -4.8% | 49.1 | 25.4 | 15.2 | -0.8 | ✅ value |
| 🟡 dip | CVS | Other | 95.53 | 39.4 | 62.6 | -4.9% | -6.5% | 73.7 | 25.0 | 10.4 | 3.9 | ⚠️ rich |
| 🟢 oversold | ALAB | Other | 288.47 | 41.3 | 2.1 | -6.8% | -18.2% | 202.6 | 132.5 | 178.1 | 0.5 | ✅ value |
| 🟡 dip | TKR | Other | 128.16 | 41.6 | 13.6 | -4.2% | -6.5% | 69.8 | 34.5 | 23.1 | -2.1 | ✅ value |
| 🟢 oversold | BE | Other | 203.33 | 43.2 | 7.1 | -3.9% | -16.7% | 688.6 | 241.2 | 94.5 | -0.0 | ⚠️ rich |
| 🟡 dip | AMD | Semis | 468.34 | 44.5 | 12.9 | -3.9% | -8.2% | 220.8 | 118.6 | 90.7 | 1.0 | ✅ value |
| 🟡 dip | DDOG | AI-software | 238.7 | 44.5 | 11.4 | -6.2% | -4.2% | 81.5 | 478.2 | 73.3 | 12.3 | ⚠️ rich |
| 🟢 oversold | GOOGL | Other | 342.14 | 44.9 | 9.8 | -1.1% | -2.9% | 90.2 | 17.0 | 77.7 | 0.2 | ✅ value |
| 🟡 dip | GLW | Other | 152.79 | 45.5 | 17.5 | +0.2% | -12.7% | 183.5 | 69.1 | 54.9 | 0.5 | ✅ value |
| 🟡 dip | COHR | Photonics | 295.34 | 45.7 | 17.2 | -3.4% | -11.1% | 186.5 | 67.3 | -56.0 | 0.0 | — |
| 🟢 oversold | TSEM | Semis | 229.31 | 46.3 | 7.9 | -2.8% | -6.1% | 368.1 | 92.0 | 86.6 | 2.0 | — |
| 🟡 dip | FCEL | Battery/H2 | 20.02 | 46.8 | 13.6 | -5.2% | -8.3% | 273.6 | -3.0 | -12.9 | 0.0 | — |
| 🟡 dip | IBKR | Financials | 89.65 | 47.8 | 20.6 | -0.4% | -2.1% | 43.1 | 35.4 | 9.8 | 1.1 | ✅ value |
| 🟡 dip | CRDO | Other | 235.47 | 49.0 | 18.1 | +1.4% | -2.6% | 126.9 | 89.2 | 107.0 | 0.1 | ✅ value |
| 🟡 dip | NOK | Comm | 10.31 | 49.2 | 21.9 | +6.8% | -10.1% | 112.2 | 69.6 | 91.9 | -2.5 | ⚠️ rich |
| 🟡 dip | NBIS | Other | 218.42 | 49.6 | 10.6 | +3.2% | -2.0% | 245.9 | 832.3 | -8.8 | -10.8 | — |
| 🟡 dip | AAOI | Photonics | 127.99 | 50.4 | 19.8 | +7.1% | -2.1% | 259.8 | -162.6 | -24.6 | -3.2 | — |
| 🟡 dip | MU | Semis | 927.9 | 50.9 | 25.5 | +3.8% | -3.6% | 656.6 | 20.7 | 40.0 | 0.0 | — |
| 🟡 dip | MRVL | Semis | 231.73 | 55.8 | 67.6 | +12.5% | -1.1% | 161.1 | — | — | — |  |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | CAT | Other | 813.58 | 39.4 | 12.8 | -4.1% | -10.4% | 108.9 | 34.9 | 30.2 | 1.9 | — |
| 🟡 dip | ON | Semis | 78.38 | 39.8 | 11.8 | -4.5% | -16.9% | 42.8 | 49.5 | 17.2 | 1.1 | ✅ value |
| 🟢 oversold | ARM | Semis | 248.23 | 40.5 | 4.0 | -5.7% | -18.6% | 72.0 | 252.6 | 177.5 | 5.4 | ⚠️ rich |
| 🟡 dip | LIN | Other | 482.04 | 40.6 | 70.5 | -1.9% | -5.3% | 10.1 | 31.0 | 44.8 | 3.0 | — |
| 🟡 dip | CSCO | Other | 111.13 | 41.5 | 17.4 | -4.5% | -4.7% | 62.7 | 33.0 | 32.2 | 1.1 | ✅ value |
| 🟢 oversold | INTC | Semis | 92.79 | 42.0 | 7.2 | -3.6% | -14.7% | 320.2 | -43.7 | 164.3 | 0.0 | ⚠️ rich |
| 🟢 oversold | KLAC | Semis | 188.98 | 42.0 | 7.5 | -3.7% | -14.6% | 123.0 | 51.3 | 65.5 | 2.5 | — |
| 🟡 dip | TXN | Semis | 270.11 | 42.0 | 17.4 | -2.8% | -7.2% | 31.1 | 40.8 | 46.0 | 2.1 | — |
| 🟡 dip | DE | Other | 591.02 | 43.3 | 22.3 | -3.3% | -2.0% | 17.2 | 33.5 | 42.4 | -2.3 | — |
| 🟡 dip | AMAT | Semis | 495.59 | 43.7 | 18.9 | -4.6% | -11.6% | 176.0 | 42.4 | 63.0 | 1.1 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only. In-session: pick the contract off the live Robinhood chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, ≤$150/trade & ≤15% total. See docs/options-strategy.md.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BE | 688.6 | 43.2 |  |
| MU | 656.6 | 50.9 |  |
| LITE | 648.9 | 50.4 |  |
| AEHR | 413.3 | 52.4 |  |
| TSEM | 368.1 | 46.3 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| SMR | -84.2 | 45.3 | SPEC |
| BYND | -83.0 | 37.4 |  |
| COIN | -61.8 | 48.2 |  |
| QS | -59.8 | 43.5 | SPEC |
| QUBT | -59.4 | 43.7 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._