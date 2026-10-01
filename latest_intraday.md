# Strategy report - INTRADAY  (2026-10-01 19:07 UTC)

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
| TMO | A+ | 12/12 | #9 | RSI2 dip | Other |  |  | 2026-10-21 | 658.79 | 6.3 | 658.79 | 634.64 | 679.61 | -3.7% |
| MRK | A+ | 12/12 | #13 | RSI2 dip | Other |  |  |  | 143.77 | 5.8 | 143.77 | 139.61 | 150.0 | -2.9% |
| TGT | A+ | 11/12 | #19 | 21 EMA pullback | Other |  |  |  | 156.56 | 33.9 | 156.56 | 150.93 | 164.44 | -3.6% |
| PFE | A+ | 11/12 | #22 | RSI2 dip | Other |  |  |  | 28.14 | 7.0 | 28.14 | 27.57 | 28.81 | -2.0% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): DE (B 11/12), JNJ (C 7/12), FCX (C 5/12), VRTX (C 7/12), C (C 4/12), ROKU (C 7/12), UNH (C 3/12), MA (C 3/12), UNP (C 3/12), KO (C 6/12), ABBV (B 11/12), DIA (C 3/12), GILD (B 11/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +137.9% | -5.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +54.2% | -1.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +49.0% | -1.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | NET | A+ | 12/12 | +41.7% | -2.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LITE | A+ | 12/12 | +41.1% | -0.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +34.7% | -8.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +34.5% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.9% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +23.1% | -3.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +16.7% | -1.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +16.5% | -1.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PANW | A+ | 12/12 | +9.9% | -1.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | MRK | A+ | 12/12 | +8.3% | -8.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | QQQ | A+ | 12/12 | +1.7% | -0.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | PLTR | A+ | 11/12 | +44.4% | -8.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | HPQ | A+ | 11/12 | +44.3% | -9.2% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AEHR | A+ | 11/12 | +43.0% | -30.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +29.4% | -4.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | TGT | A+ | 11/12 | +17.5% | -7.8% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | XOM | A+ | 11/12 | +16.7% | -4.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | WBD | A+ | 11/12 | +14.2% | -0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | PFE | A+ | 11/12 | +13.1% | -2.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | EMR | A+ | 11/12 | +11.2% | -3.7% | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | GILD | B | 11/12 | +10.0% | -5.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | ETN | B | 11/12 | +7.3% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 229)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 684.3 | 62.8 | T |
| 2 **TOP** | LITE | 554.3 | 63.8 | T |
| 3 **TOP** | MRNA | 540.4 | 67.9 | T |
| 4 **TOP** | AAOI | 327.2 | 51.9 | F |
| 5 **TOP** | FCEL | 306.7 | 46.9 | T |
| 6 **TOP** | BE | 303.5 | 54.8 | T |
| 7 **TOP** | INTC | 265.4 | 62.3 | T |
| 8 **TOP** | DELL | 247.9 | 54.0 | T |
| 9 **TOP** | TSEM | 238.4 | 59.2 | T |
| 10 **TOP** | MRVL | 234.6 | 63.7 | T |
| 11 **TOP** | VIAV | 208.6 | 69.1 | T |
| 12 **TOP** | AEHR | 207.0 | 55.6 | T |
| 13 **TOP** | COHR | 200.7 | 56.6 | T |
| 14 **TOP** | NBIS | 192.1 | 53.8 | T |
| 15 **TOP** | LRCX | 189.8 | 65.3 | T |
| 16 **TOP** | AMD | 182.6 | 67.4 | T |
| 17 **TOP** | AMAT | 174.9 | 67.5 | T |
| 18 **TOP** | WBD | 143.3 | 75.2 | T |
| 19 **TOP** | VLO | 138.1 | 66.3 | T |
| 20 **TOP** | NOK | 130.9 | 50.4 | T |
| 21 **TOP** | GLW | 117.2 | 54.4 | T |
| 22 **TOP** | MPC | 113.1 | 67.4 | T |
| 23  | MTSI | 104.5 | 61.3 | T |
| 24  | CRWD | 103.0 | 67.3 | T |
| 25  | KLAC | 96.0 | 63.7 | T |
| 26  | PANW | 90.1 | 58.4 | T |
| 27  | PSX | 88.7 | 62.1 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNH | Other | 363.7 | 31.1 | 4.6 | -4.3% | -7.9% | 27.9 | 23.4 | 14.0 | -0.7 | ✅ value |
| 🟡 dip | REGN | Other | 741.21 | 36.1 | 15.2 | -6.0% | -5.4% | 41.9 | 17.7 | 21.7 | 56.9 | ⚠️ rich |
| 🟡 dip | V | Other | 359.87 | 40.0 | 16.9 | -2.3% | -2.3% | 5.9 | 30.6 | 32.0 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 86.06 | 40.4 | 40.2 | -4.0% | -5.1% | 45.2 | 34.0 | 9.4 | 1.1 | ✅ value |
| 🟡 dip | AMZN | Other | 249.45 | 45.6 | 75.5 | -1.0% | -2.6% | 11.3 | 19.8 | -230.5 | 0.2 | ✅ value |
| 🟡 dip | TKR | Other | 118.38 | 45.8 | 83.2 | +0.3% | -5.4% | 54.2 | 31.9 | 21.3 | -1.9 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 16.68 | 46.9 | 58.9 | +1.3% | -10.6% | 306.7 | -4.8 | -12.4 | -0.0 | — |
| 🟡 dip | CRDO | Other | 207.07 | 55.7 | 86.1 | +16.1% | -0.6% | 67.9 | 69.9 | 87.7 | 0.2 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNP | Other | 271.47 | 31.0 | 6.1 | -2.9% | -6.7% | 30.0 | 22.0 | 24.8 | 3.1 | ⚠️ rich |
| 🟢 oversold | JPM | Other | 332.02 | 33.4 | 30.6 | -4.2% | -5.8% | 17.8 | 14.3 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | IWM | Index-ETF | 279.33 | 33.7 | 56.2 | -2.2% | -4.6% | 23.6 | — | — | — |  |
| 🟢 oversold | C | Other | 126.66 | 34.2 | 3.9 | -5.5% | -5.5% | 37.2 | 13.5 | -8.9 | 0.4 | ✅ value |
| 🟢 oversold | DIA | Index-ETF | 508.38 | 34.9 | 8.8 | -2.1% | -3.5% | 15.7 | — | — | — |  |
| 🟡 dip | NUE | Other | 234.74 | 35.5 | 22.7 | -6.5% | -8.2% | 69.4 | 18.7 | 33.8 | 0.1 | ✅ value |
| 🟢 oversold | JNJ | Other | 259.55 | 36.2 | 2.2 | -3.4% | -2.5% | 53.1 | 30.0 | 33.4 | -3.7 | — |
| 🟢 oversold | ROKU | Other | 150.68 | 38.3 | 4.0 | -2.3% | -1.5% | 61.1 | 62.8 | 27.1 | 0.0 | — |
| 🟢 oversold | KO | Other | 86.11 | 39.8 | 6.9 | -2.0% | -2.0% | 27.6 | 25.9 | 25.9 | 1.5 | ✅ value |
| 🟡 dip | BMY | Other | 61.69 | 40.0 | 14.7 | -2.8% | -4.4% | 41.8 | 13.6 | 11.0 | 0.2 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 497.3 | 67.9 |  |
| MPC | 98.7 | 67.4 |  |
| VLO | 112.6 | 66.3 |  |
| NET | 33.0 | 61.1 |  |
| LITE | 434.0 | 63.8 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -78.0 | 29.2 |  |
| RCAT | -20.3 | 30.8 | SPEC |
| OKLO | -65.5 | 40.4 | SPEC |
| JOBY | -58.6 | 34.2 | SPEC |
| BWXT | -12.4 | 32.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._