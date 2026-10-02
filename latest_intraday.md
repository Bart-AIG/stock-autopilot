# Strategy report - INTRADAY  (2026-10-02 15:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #9 | 21 EMA pullback | Other |  |  | 2026-10-21 | 653.37 | 10.7 | 653.37 | 628.22 | 679.61 | -3.8% |
| MRK | A+ | 11/12 | #23 | RSI2 dip | Other |  |  |  | 142.74 | 3.8 | 142.74 | 138.64 | 148.88 | -2.9% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JNJ (C 7/12), KO (C 7/12), VRTX (C 7/12), PFE (B 10/12), GILD (B 9/12), ABBV (B 10/12), BMY (C 6/12)

## Quality ranking — top 25 of 239 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +122.8% | -9.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +50.8% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +44.2% | -4.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LITE | A+ | 12/12 | +43.4% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | NET | A+ | 12/12 | +38.8% | -2.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | CRWD | A+ | 12/12 | +33.7% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | DELL | A+ | 12/12 | +33.7% | -4.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.5% | -4.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +23.5% | -3.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | NVDA | A+ | 12/12 | +18.4% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMD | A+ | 12/12 | +13.2% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EMR | A+ | 12/12 | +12.1% | -1.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PANW | A+ | 12/12 | +11.5% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +3.9% | -2.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +1.4% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | AEHR | A+ | 11/12 | +47.2% | -25.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +43.5% | -6.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | HPQ | A+ | 11/12 | +40.0% | -9.2% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | RBRK | A+ | 11/12 | +31.8% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +30.8% | -4.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | XOM | A+ | 11/12 | +17.1% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | WBD | A+ | 11/12 | +15.8% | -0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | MRK | A+ | 11/12 | +10.1% | -8.7% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | DDOG | B | 11/12 | +6.9% | -2.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | ADI | B | 11/12 | +5.2% | -5.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 23 of 231)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 707.0 | 60.7 | T |
| 2 **TOP** | LITE | 556.7 | 65.4 | T |
| 3 **TOP** | MRNA | 523.4 | 62.7 | T |
| 4 **TOP** | WDC | 448.0 | 36.3 | F |
| 5 **TOP** | AAOI | 341.7 | 57.6 | T |
| 6 **TOP** | BE | 323.1 | 59.6 | T |
| 7 **TOP** | DELL | 306.9 | 58.0 | T |
| 8 **TOP** | INTC | 272.0 | 64.4 | T |
| 9 **TOP** | FCEL | 258.2 | 52.2 | T |
| 10 **TOP** | TSEM | 240.7 | 59.4 | T |
| 11 **TOP** | AEHR | 222.5 | 60.3 | T |
| 12 **TOP** | MRVL | 219.6 | 65.9 | T |
| 13 **TOP** | NBIS | 210.5 | 58.3 | T |
| 14 **TOP** | COHR | 206.0 | 60.4 | T |
| 15 **TOP** | VIAV | 200.3 | 73.0 | T |
| 16 **TOP** | LRCX | 197.1 | 68.0 | T |
| 17 **TOP** | AMD | 181.6 | 70.9 | T |
| 18 **TOP** | AMAT | 178.3 | 69.2 | T |
| 19 **TOP** | WBD | 144.3 | 75.3 | T |
| 20 **TOP** | VLO | 137.3 | 59.4 | T |
| 21 **TOP** | NOK | 132.6 | 53.7 | T |
| 22 **TOP** | ILMN | 118.0 | 69.3 | T |
| 23 **TOP** | MPC | 114.8 | 62.9 | T |
| 24  | GLW | 110.5 | 56.8 | T |
| 25  | KLAC | 103.5 | 67.3 | T |
| 26  | CRWD | 96.8 | 69.4 | T |
| 27  | MTSI | 96.5 | 68.6 | T |
| 28  | PSX | 91.3 | 58.5 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNH | Other | 367.08 | 34.6 | 38.5 | -3.0% | -6.7% | 29.4 | 23.6 | 14.1 | -0.7 | ✅ value |
| 🟡 dip | V | Other | 359.46 | 39.6 | 14.5 | -2.2% | -2.5% | 8.1 | 30.5 | 31.9 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 88.78 | 47.7 | 86.6 | -0.7% | -2.1% | 39.5 | 34.9 | 9.6 | 1.1 | ✅ value |
| 🟡 dip | AMZN | Other | 251.42 | 48.4 | 84.1 | -0.1% | -2.0% | 13.2 | 19.9 | -232.5 | 0.2 | ✅ value |
| 🟡 dip | GOOGL | Other | 344.55 | 50.8 | 68.4 | +0.5% | +0.0% | 59.5 | 16.9 | 77.6 | 0.2 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 17.7 | 52.2 | 89.1 | +6.6% | -4.5% | 258.2 | -5.1 | -13.1 | -0.1 | — |
| 🟡 dip | TKR | Other | 121.94 | 55.2 | 95.8 | +3.3% | -2.3% | 57.2 | 32.8 | 21.9 | -2.0 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | USB | Other | 57.71 | 33.1 | 47.3 | -4.1% | -7.1% | 29.4 | 11.5 | 7.2 | 0.6 | ✅ value |
| 🟢 oversold | JNJ | Other | 257.08 | 33.4 | 1.4 | -4.0% | -3.4% | 54.6 | 29.7 | 33.1 | -3.7 | — |
| 🟢 oversold | JPM | Other | 332.08 | 34.2 | 32.2 | -3.8% | -5.7% | 18.9 | 14.2 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | KO | Other | 85.3 | 35.9 | 1.6 | -2.7% | -3.0% | 27.8 | 25.6 | 25.7 | 1.5 | ✅ value |
| 🟢 oversold | BMY | Other | 60.86 | 36.8 | 7.2 | -3.6% | -5.6% | 42.7 | 13.4 | 10.8 | 0.2 | ✅ value |
| 🟡 dip | C | Other | 128.01 | 37.9 | 37.2 | -4.2% | -4.4% | 41.7 | 13.6 | -8.9 | 0.4 | ✅ value |
| 🟢 oversold | VRTX | Other | 503.07 | 38.2 | 2.5 | -3.0% | -2.9% | 38.8 | 29.0 | 33.6 | 1.3 | ✅ value |
| 🟡 dip | DIA | Index-ETF | 511.36 | 39.4 | 66.1 | -1.3% | -2.9% | 17.0 | — | — | — |  |
| 🟡 dip | NEM | Other | 115.08 | 40.5 | 32.5 | -6.0% | -2.3% | 65.0 | 14.4 | 9.5 | 0.3 | ✅ value |
| 🟡 dip | UNP | Other | 277.32 | 42.6 | 90.1 | -0.6% | -4.6% | 30.5 | 22.4 | 25.3 | 3.1 | ⚠️ rich |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 446.4 | 62.7 |  |
| MPC | 101.2 | 62.9 |  |
| VLO | 118.3 | 59.4 |  |
| LITE | 407.9 | 65.4 |  |
| NET | 25.7 | 60.8 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -83.3 | 29.7 |  |
| RCAT | -20.5 | 34.1 | SPEC |
| JOBY | -58.0 | 35.1 | SPEC |
| BWXT | -16.8 | 30.3 | SPEC |
| OKLO | -65.9 | 41.5 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._