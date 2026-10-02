# Strategy report - INTRADAY  (2026-10-02 18:17 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #9 | 21 EMA pullback | Other |  |  | 2026-10-21 | 654.09 | 15.0 | 654.09 | 628.91 | 679.61 | -3.8% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JNJ (C 7/12), KO (C 7/12), PFE (B 10/12), GILD (B 9/12), VRTX (C 7/12), LLY (C 4/12), MRK (B 11/12), BMY (C 6/12), PM (C 8/12), ROST (C 7/12), WDC (C 3/12)

## Quality ranking — top 25 of 239 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +128.2% | -7.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +55.0% | -0.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +49.0% | -1.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LITE | A+ | 12/12 | +46.1% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | NET | A+ | 12/12 | +39.6% | -2.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +34.7% | -4.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +32.5% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.4% | -4.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +23.9% | -3.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | NVDA | A+ | 12/12 | +17.6% | -0.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMD | A+ | 12/12 | +11.9% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EMR | A+ | 12/12 | +11.6% | -1.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PANW | A+ | 12/12 | +10.1% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | DE | A+ | 12/12 | +5.0% | -3.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | AAPL | A+ | 12/12 | +4.1% | -2.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | QQQ | A+ | 12/12 | +1.2% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AEHR | A+ | 11/12 | +44.2% | -27.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PLTR | A+ | 11/12 | +40.6% | -8.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | HPQ | A+ | 11/12 | +40.5% | -9.0% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | RBRK | A+ | 11/12 | +32.9% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MSFT | A+ | 11/12 | +30.8% | -5.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | XOM | A+ | 11/12 | +18.0% | -4.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | WBD | A+ | 11/12 | +16.1% | -0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | MRK | B | 11/12 | +10.9% | -8.2% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | DDOG | B | 11/12 | +6.4% | -3.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 23 of 231)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 707.0 | 59.6 | T |
| 2 **TOP** | LITE | 556.7 | 66.7 | T |
| 3 **TOP** | MRNA | 523.4 | 65.6 | T |
| 4 **TOP** | WDC | 448.0 | 39.3 | T |
| 5 **TOP** | AAOI | 341.7 | 57.1 | T |
| 6 **TOP** | BE | 323.1 | 58.9 | T |
| 7 **TOP** | DELL | 306.9 | 58.6 | T |
| 8 **TOP** | INTC | 272.0 | 61.5 | T |
| 9 **TOP** | FCEL | 258.2 | 52.9 | T |
| 10 **TOP** | TSEM | 240.7 | 58.1 | T |
| 11 **TOP** | AEHR | 222.5 | 58.7 | T |
| 12 **TOP** | MRVL | 219.6 | 65.0 | T |
| 13 **TOP** | NBIS | 210.5 | 56.9 | T |
| 14 **TOP** | COHR | 206.0 | 60.1 | T |
| 15 **TOP** | VIAV | 200.3 | 72.9 | T |
| 16 **TOP** | LRCX | 197.1 | 68.2 | T |
| 17 **TOP** | AMD | 181.6 | 69.6 | T |
| 18 **TOP** | AMAT | 178.3 | 69.1 | T |
| 19 **TOP** | WBD | 144.3 | 75.4 | T |
| 20 **TOP** | VLO | 137.3 | 67.4 | T |
| 21 **TOP** | NOK | 132.6 | 52.7 | T |
| 22 **TOP** | ILMN | 118.0 | 68.4 | T |
| 23 **TOP** | MPC | 114.8 | 69.2 | T |
| 24  | GLW | 110.5 | 56.3 | T |
| 25  | KLAC | 103.5 | 67.2 | T |
| 26  | CRWD | 96.8 | 68.3 | T |
| 27  | MTSI | 96.5 | 68.3 | T |
| 28  | PSX | 91.3 | 64.4 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | REGN | Other | 737.17 | 35.7 | 23.2 | -5.8% | -6.1% | 47.4 | 17.6 | 21.6 | 56.6 | ⚠️ rich |
| 🟡 dip | UNH | Other | 369.77 | 38.0 | 59.1 | -2.4% | -6.1% | 29.4 | 23.8 | 14.2 | -0.7 | ✅ value |
| 🟡 dip | V | Other | 360.85 | 41.5 | 41.9 | -1.8% | -2.1% | 8.1 | 30.6 | 32.1 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 88.57 | 47.2 | 85.8 | -1.0% | -2.3% | 39.5 | 35.0 | 9.7 | 1.1 | ✅ value |
| 🟡 dip | AMZN | Other | 250.84 | 47.7 | 81.8 | -0.3% | -2.2% | 13.2 | 19.9 | -231.9 | 0.2 | ✅ value |
| 🟡 dip | GOOGL | Other | 343.71 | 50.1 | 65.7 | +0.3% | -0.2% | 59.5 | 16.9 | 77.5 | 0.2 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 17.85 | 52.9 | 90.1 | +7.4% | -3.7% | 258.2 | -5.3 | -13.6 | -0.1 | — |
| 🟡 dip | TKR | Other | 122.85 | 57.1 | 96.5 | +4.0% | -1.6% | 57.2 | 33.1 | 22.2 | -2.0 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | JNJ | Other | 255.65 | 31.9 | 1.2 | -4.5% | -3.9% | 54.6 | 29.5 | 32.9 | -3.7 | — |
| 🟢 oversold | JPM | Other | 331.25 | 33.6 | 26.9 | -4.1% | -6.0% | 18.9 | 14.2 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | BMY | Other | 60.77 | 36.5 | 7.2 | -3.7% | -5.8% | 42.7 | 13.4 | 10.8 | 0.2 | ✅ value |
| 🟢 oversold | KO | Other | 85.58 | 37.2 | 1.9 | -2.4% | -2.7% | 27.8 | 25.7 | 25.7 | 1.5 | ✅ value |
| 🟡 dip | C | Other | 128.18 | 38.4 | 40.6 | -4.1% | -4.3% | 41.7 | 13.6 | -9.0 | 0.4 | ✅ value |
| 🟡 dip | DIA | Index-ETF | 510.72 | 38.5 | 60.4 | -1.5% | -3.0% | 17.0 | — | — | — |  |
| 🟢 oversold | VRTX | Other | 504.72 | 39.0 | 3.0 | -2.7% | -2.6% | 38.8 | 29.1 | 33.8 | 1.3 | ✅ value |
| 🟡 dip | IWM | Index-ETF | 281.54 | 39.6 | 84.4 | -1.2% | -3.8% | 25.7 | — | — | — |  |
| 🟡 dip | NEM | Other | 114.95 | 40.3 | 26.9 | -6.1% | -2.4% | 65.0 | 14.5 | 9.5 | 0.3 | ✅ value |
| 🟡 dip | NUE | Other | 239.81 | 41.4 | 72.7 | -4.0% | -6.2% | 80.3 | 19.1 | 34.5 | 0.2 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 446.4 | 65.6 |  |
| MPC | 101.2 | 69.2 |  |
| VLO | 118.3 | 67.4 |  |
| LITE | 407.9 | 66.7 |  |
| NET | 25.7 | 61.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -83.3 | 29.2 |  |
| RCAT | -20.5 | 31.3 | SPEC |
| JOBY | -58.0 | 33.5 | SPEC |
| BWXT | -16.8 | 30.1 | SPEC |
| OKLO | -65.9 | 40.7 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._