# Strategy report - INTRADAY  (2026-10-02 16:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #9 | 21 EMA pullback | Other |  |  | 2026-10-21 | 653.71 | 12.8 | 653.71 | 628.55 | 679.61 | -3.8% |
| TGT | A+ | 11/12 | #21 | 21 EMA pullback | Other |  |  |  | 155.9 | 14.3 | 155.9 | 150.31 | 164.28 | -3.6% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JNJ (C 7/12), KO (C 7/12), PFE (B 10/12), VRTX (C 7/12), GILD (B 9/12), LLY (C 4/12), MRK (B 11/12), BMY (C 6/12), PM (B 8/12), WDC (C 3/12), ROST (C 7/12), NEM (C 7/12)

## Quality ranking — top 25 of 239 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +130.0% | -6.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +53.8% | -1.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +46.9% | -2.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LITE | A+ | 12/12 | +46.7% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | NET | A+ | 12/12 | +39.7% | -2.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +34.2% | -4.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +32.4% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.1% | -4.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +24.0% | -3.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | NVDA | A+ | 12/12 | +18.1% | -0.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMD | A+ | 12/12 | +12.5% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EMR | A+ | 12/12 | +12.0% | -1.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PANW | A+ | 12/12 | +9.9% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +3.9% | -2.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +1.4% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | AEHR | A+ | 11/12 | +47.6% | -25.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +40.5% | -8.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | HPQ | A+ | 11/12 | +40.5% | -9.0% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | RBRK | A+ | 11/12 | +31.7% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +30.6% | -5.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | TGT | A+ | 11/12 | +21.2% | -8.3% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | XOM | A+ | 11/12 | +17.7% | -4.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | WBD | A+ | 11/12 | +16.1% | -0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | MRK | B | 11/12 | +10.8% | -8.2% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | DDOG | B | 11/12 | +7.3% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 23 of 231)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 707.0 | 60.3 | T |
| 2 **TOP** | LITE | 556.7 | 67.0 | T |
| 3 **TOP** | MRNA | 523.4 | 66.3 | T |
| 4 **TOP** | WDC | 448.0 | 37.8 | T |
| 5 **TOP** | AAOI | 341.7 | 57.0 | T |
| 6 **TOP** | BE | 323.1 | 59.5 | T |
| 7 **TOP** | DELL | 306.9 | 58.2 | T |
| 8 **TOP** | INTC | 272.0 | 63.7 | T |
| 9 **TOP** | FCEL | 258.2 | 51.2 | T |
| 10 **TOP** | TSEM | 240.7 | 58.6 | T |
| 11 **TOP** | AEHR | 222.5 | 60.4 | T |
| 12 **TOP** | MRVL | 219.6 | 66.1 | T |
| 13 **TOP** | NBIS | 210.5 | 58.0 | T |
| 14 **TOP** | COHR | 206.0 | 60.3 | T |
| 15 **TOP** | VIAV | 200.3 | 74.1 | T |
| 16 **TOP** | LRCX | 197.1 | 68.7 | T |
| 17 **TOP** | AMD | 181.6 | 70.1 | T |
| 18 **TOP** | AMAT | 178.3 | 70.0 | T |
| 19 **TOP** | WBD | 144.3 | 75.3 | T |
| 20 **TOP** | VLO | 137.3 | 63.6 | T |
| 21 **TOP** | NOK | 132.6 | 52.4 | T |
| 22 **TOP** | ILMN | 118.0 | 69.1 | T |
| 23 **TOP** | MPC | 114.8 | 68.2 | T |
| 24  | GLW | 110.5 | 56.4 | T |
| 25  | KLAC | 103.5 | 68.2 | T |
| 26  | CRWD | 96.8 | 68.3 | T |
| 27  | MTSI | 96.5 | 68.8 | T |
| 28  | PSX | 91.3 | 62.7 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | UNH | Other | 367.53 | 35.2 | 43.3 | -2.9% | -6.6% | 29.4 | 23.6 | 14.1 | -0.7 | ✅ value |
| 🟡 dip | V | Other | 359.52 | 39.7 | 15.4 | -2.2% | -2.5% | 8.1 | 30.6 | 32.0 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 88.17 | 46.3 | 83.9 | -1.4% | -2.7% | 39.5 | 34.8 | 9.6 | 1.1 | ✅ value |
| 🟡 dip | AMZN | Other | 250.42 | 47.2 | 79.7 | -0.5% | -2.4% | 13.2 | 19.9 | -232.3 | 0.2 | ✅ value |
| 🟡 dip | CRSP | Gene-edit | 54.47 | 47.6 | 18.9 | -0.7% | +0.2% | 8.1 | -11.4 | -10.9 | -2.5 | — |
| 🟡 dip | GOOGL | Other | 342.71 | 49.3 | 61.8 | +0.0% | -0.5% | 59.5 | 16.9 | 77.5 | 0.2 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 17.49 | 51.2 | 87.2 | +5.4% | -5.6% | 258.2 | -5.1 | -13.1 | -0.1 | — |
| 🟡 dip | TKR | Other | 122.67 | 56.8 | 96.4 | +3.9% | -1.7% | 57.2 | 32.9 | 22.0 | -2.0 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | JNJ | Other | 256.8 | 33.1 | 1.4 | -4.1% | -3.5% | 54.6 | 29.7 | 33.1 | -3.7 | — |
| 🟢 oversold | JPM | Other | 331.15 | 33.5 | 26.3 | -4.1% | -6.0% | 18.9 | 14.2 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | KO | Other | 85.38 | 36.2 | 1.7 | -2.6% | -2.9% | 27.8 | 25.7 | 25.7 | 1.5 | ✅ value |
| 🟢 oversold | BMY | Other | 60.73 | 36.3 | 6.8 | -3.8% | -5.8% | 42.7 | 13.4 | 10.8 | 0.2 | ✅ value |
| 🟡 dip | C | Other | 127.63 | 36.8 | 27.8 | -4.4% | -4.7% | 41.7 | 13.5 | -8.9 | 0.4 | ✅ value |
| 🟢 oversold | VRTX | Other | 502.34 | 37.8 | 2.4 | -3.2% | -3.1% | 38.8 | 29.0 | 33.6 | 1.3 | ✅ value |
| 🟡 dip | DIA | Index-ETF | 510.32 | 37.9 | 55.7 | -1.5% | -3.1% | 17.0 | — | — | — |  |
| 🟢 oversold | NEM | Other | 114.15 | 39.0 | 8.6 | -6.7% | -3.1% | 65.0 | 14.4 | 9.4 | 0.3 | ✅ value |
| 🟡 dip | IWM | Index-ETF | 281.83 | 40.3 | 85.5 | -1.1% | -3.7% | 25.7 | — | — | — |  |
| 🟡 dip | NUE | Other | 240.58 | 42.2 | 75.4 | -3.8% | -6.0% | 80.3 | 19.2 | 34.6 | 0.2 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 446.4 | 66.3 |  |
| MPC | 101.2 | 68.2 |  |
| VLO | 118.3 | 63.6 |  |
| LITE | 407.9 | 67.0 |  |
| NET | 25.7 | 61.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -83.3 | 29.3 |  |
| RCAT | -20.5 | 31.1 | SPEC |
| JOBY | -58.0 | 32.9 | SPEC |
| BWXT | -16.8 | 29.0 | SPEC |
| OKLO | -65.9 | 41.1 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._