# Strategy report - INTRADAY  (2026-10-01 18:46 UTC)

## >>> ACTION <<<

## 📅 MONTHLY REBALANCE DUE (first trading day of the month)
Run the monthly portfolio review alongside today's signals:
- **Momentum rotate:** re-rank the 12-1 top decile (below); exit held momentum names that dropped out of the decile or broke the 200-day MA; weigh the better-play list.
- **Concentration check:** trim any position over the per-name cap (30% of account value) or the speculative sleeve over ~25%; confirm the operational reserve.
- **Cull the laggards:** this is the moment to sell underwater names whose thesis has weakened — they carry no price stop, so the monthly review is their exit gate.
- **Quarterly deep review:** re-confirm the thesis on every long-held position and re-sleeve (swing/momentum) anything that has drifted.

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #9 | RSI2 dip | Other |  |  | 2026-10-21 | 658.71 | 6.3 | 658.71 | 634.54 | 679.61 | -3.7% |
| MRK | A+ | 12/12 | #13 | RSI2 dip | Other |  |  |  | 143.66 | 5.7 | 143.66 | 139.5 | 149.9 | -2.9% |
| AAPL | A+ | 12/12 | #14 | 21 EMA pullback | Other |  |  |  | 329.85 | 27.0 | 329.85 | 318.13 | 341.07 | -3.6% |
| PFE | A+ | 11/12 | #23 | RSI2 dip | Other |  |  |  | 28.14 | 6.9 | 28.14 | 27.56 | 28.81 | -2.0% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): KO (C 6/12), DE (B 11/12), FCX (C 5/12), JNJ (C 7/12), C (C 4/12), ROKU (C 7/12), VRTX (B 8/12), UNH (C 3/12), MA (C 3/12), LLY (C 5/12), UNP (C 3/12), ABBV (B 11/12), DIA (C 3/12), GILD (B 11/12), PM (B 9/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +138.9% | -5.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +53.8% | -1.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +49.0% | -1.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | NET | A+ | 12/12 | +42.2% | -2.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LITE | A+ | 12/12 | +40.1% | -1.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +35.0% | -7.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +34.8% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.9% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +23.2% | -3.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +16.7% | -2.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +16.4% | -1.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PANW | A+ | 12/12 | +10.0% | -1.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | MRK | A+ | 12/12 | +8.4% | -8.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +4.2% | -3.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +1.6% | -0.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | HPQ | A+ | 11/12 | +44.8% | -8.9% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +44.4% | -8.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | AEHR | A+ | 11/12 | +41.5% | -30.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MSFT | A+ | 11/12 | +29.6% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | TGT | A+ | 11/12 | +18.3% | -7.3% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | XOM | A+ | 11/12 | +16.7% | -4.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | WBD | A+ | 11/12 | +14.2% | -0.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | PFE | A+ | 11/12 | +13.2% | -2.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | EMR | B | 11/12 | +11.0% | -3.9% | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | GILD | B | 11/12 | +10.0% | -5.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 229)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 684.3 | 61.9 | T |
| 2 **TOP** | LITE | 554.3 | 63.2 | T |
| 3 **TOP** | MRNA | 540.4 | 68.4 | T |
| 4 **TOP** | AAOI | 327.2 | 51.1 | F |
| 5 **TOP** | FCEL | 306.7 | 46.9 | T |
| 6 **TOP** | BE | 303.5 | 54.5 | T |
| 7 **TOP** | INTC | 265.4 | 62.3 | T |
| 8 **TOP** | DELL | 247.9 | 54.2 | T |
| 9 **TOP** | TSEM | 238.4 | 59.0 | T |
| 10 **TOP** | MRVL | 234.6 | 63.4 | T |
| 11 **TOP** | VIAV | 208.6 | 68.7 | T |
| 12 **TOP** | AEHR | 207.0 | 54.8 | T |
| 13 **TOP** | COHR | 200.7 | 56.0 | T |
| 14 **TOP** | NBIS | 192.1 | 53.5 | T |
| 15 **TOP** | LRCX | 189.8 | 64.8 | T |
| 16 **TOP** | AMD | 182.6 | 67.3 | T |
| 17 **TOP** | AMAT | 174.9 | 67.0 | T |
| 18 **TOP** | WBD | 143.3 | 75.0 | T |
| 19 **TOP** | VLO | 138.1 | 66.2 | T |
| 20 **TOP** | NOK | 130.9 | 49.6 | T |
| 21 **TOP** | GLW | 117.2 | 53.6 | T |
| 22 **TOP** | MPC | 113.1 | 66.9 | T |
| 23  | MTSI | 104.5 | 61.0 | T |
| 24  | CRWD | 103.0 | 67.4 | T |
| 25  | KLAC | 96.0 | 63.5 | T |
| 26  | PANW | 90.1 | 58.5 | T |
| 27  | PSX | 88.7 | 61.9 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNH | Other | 364.36 | 31.5 | 4.4 | -4.2% | -7.7% | 27.9 | 23.4 | 14.0 | -0.7 | ✅ value |
| 🟡 dip | REGN | Other | 741.65 | 36.2 | 14.3 | -5.9% | -5.3% | 41.9 | 17.7 | 21.7 | 56.8 | ⚠️ rich |
| 🟡 dip | V | Other | 359.8 | 39.9 | 13.0 | -2.3% | -2.4% | 5.9 | 30.6 | 32.0 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 85.91 | 40.0 | 34.2 | -4.2% | -5.3% | 45.2 | 34.0 | 9.4 | 1.1 | ✅ value |
| 🟡 dip | TKR | Other | 118.23 | 45.3 | 82.0 | +0.2% | -5.5% | 54.2 | 31.9 | 21.3 | -1.9 | ✅ value |
| 🟡 dip | AMZN | Other | 249.52 | 45.7 | 76.2 | -1.0% | -2.6% | 11.3 | 19.8 | -230.7 | 0.2 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 16.68 | 46.9 | 58.9 | +1.3% | -10.6% | 306.7 | -4.9 | -12.5 | -0.0 | — |
| 🟡 dip | CRDO | Other | 207.52 | 55.9 | 86.4 | +16.3% | -0.4% | 67.9 | 70.3 | 88.2 | 0.2 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNP | Other | 271.03 | 30.6 | 6.0 | -3.1% | -6.9% | 30.0 | 22.0 | 24.8 | 3.1 | ⚠️ rich |
| 🟢 oversold | JPM | Other | 331.97 | 33.4 | 30.0 | -4.3% | -5.8% | 17.8 | 14.3 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | IWM | Index-ETF | 279.32 | 33.7 | 56.1 | -2.2% | -4.6% | 23.6 | — | — | — |  |
| 🟢 oversold | C | Other | 126.67 | 34.3 | 3.6 | -5.5% | -5.5% | 37.2 | 13.4 | -8.9 | 0.4 | ✅ value |
| 🟢 oversold | DIA | Index-ETF | 508.43 | 35.0 | 8.7 | -2.1% | -3.5% | 15.7 | — | — | — |  |
| 🟡 dip | NUE | Other | 234.69 | 35.5 | 18.3 | -6.5% | -8.2% | 69.4 | 18.7 | 33.7 | 0.1 | ✅ value |
| 🟢 oversold | JNJ | Other | 259.64 | 36.3 | 2.2 | -3.4% | -2.4% | 53.1 | 30.0 | 33.4 | -3.7 | — |
| 🟢 oversold | ROKU | Other | 150.63 | 38.1 | 3.8 | -2.3% | -1.5% | 61.1 | 62.8 | 27.1 | 0.0 | — |
| 🟢 oversold | KO | Other | 85.95 | 38.9 | 1.6 | -2.2% | -2.2% | 27.6 | 25.8 | 25.8 | 1.5 | ✅ value |
| 🟡 dip | BMY | Other | 61.66 | 39.9 | 14.6 | -2.9% | -4.4% | 41.8 | 13.6 | 11.0 | 0.2 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 497.3 | 68.4 |  |
| MPC | 98.7 | 66.9 |  |
| VLO | 112.6 | 66.2 |  |
| NET | 33.0 | 61.4 |  |
| LITE | 434.0 | 63.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -78.0 | 29.1 |  |
| RCAT | -20.3 | 30.6 | SPEC |
| OKLO | -65.5 | 40.4 | SPEC |
| JOBY | -58.6 | 34.4 | SPEC |
| BWXT | -12.4 | 32.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._