# Strategy report - INTRADAY  (2026-10-01 18:06 UTC)

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
| TMO | A+ | 12/12 | #9 | RSI2 dip | Other |  |  | 2026-10-21 | 654.75 | 5.3 | 654.75 | 629.73 | 679.61 | -3.8% |
| MRK | A+ | 12/12 | #13 | RSI2 dip | Other |  |  |  | 143.33 | 5.2 | 143.33 | 139.14 | 149.61 | -2.9% |
| AAPL | A+ | 12/12 | #14 | 21 EMA pullback | Other |  |  |  | 328.96 | 24.3 | 328.96 | 317.18 | 341.07 | -3.6% |
| PFE | A+ | 11/12 | #22 | RSI2 dip | Other |  |  |  | 28.11 | 6.5 | 28.11 | 27.53 | 28.81 | -2.1% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): DE (B 11/12), KO (C 6/12), FCX (C 5/12), JNJ (C 7/12), UNP (C 3/12), C (C 4/12), VRTX (C 7/12), ROKU (C 7/12), MA (C 3/12), LLY (C 5/12), UNH (C 3/12), V (C 4/12), DIA (C 3/12), ABBV (B 11/12), GILD (B 11/12)

## Quality ranking — top 25 of 234 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +138.0% | -5.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +53.8% | -2.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +48.9% | -1.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | NET | A+ | 12/12 | +42.6% | -1.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LITE | A+ | 12/12 | +40.7% | -1.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +35.2% | -7.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +34.5% | 0.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +27.9% | -4.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +22.8% | -3.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +16.6% | -2.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +15.8% | -2.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PANW | A+ | 12/12 | +10.2% | -1.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | MRK | A+ | 12/12 | +8.4% | -8.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +4.0% | -3.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | HPQ | A+ | 11/12 | +44.1% | -9.4% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PLTR | A+ | 11/12 | +44.0% | -8.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AEHR | A+ | 11/12 | +43.2% | -30.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +29.4% | -5.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | TGT | A+ | 11/12 | +18.3% | -7.4% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | XOM | A+ | 11/12 | +16.9% | -4.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | WBD | A+ | 11/12 | +14.3% | -0.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | PFE | A+ | 11/12 | +13.5% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | EMR | A+ | 11/12 | +10.5% | -4.4% | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | GILD | B | 11/12 | +10.1% | -5.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | ETN | B | 11/12 | +7.1% | -5.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 228)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 684.3 | 62.6 | T |
| 2 **TOP** | LITE | 554.3 | 63.5 | T |
| 3 **TOP** | MRNA | 540.4 | 67.8 | T |
| 4 **TOP** | AAOI | 327.2 | 51.9 | F |
| 5 **TOP** | FCEL | 306.7 | 47.7 | T |
| 6 **TOP** | BE | 303.5 | 55.4 | T |
| 7 **TOP** | INTC | 265.4 | 62.6 | T |
| 8 **TOP** | DELL | 247.9 | 54.3 | T |
| 9 **TOP** | TSEM | 238.4 | 58.5 | T |
| 10 **TOP** | MRVL | 234.6 | 63.2 | T |
| 11 **TOP** | VIAV | 208.6 | 68.4 | T |
| 12 **TOP** | AEHR | 207.0 | 55.7 | T |
| 13 **TOP** | COHR | 200.7 | 56.4 | T |
| 14 **TOP** | NBIS | 192.1 | 54.2 | T |
| 15 **TOP** | LRCX | 189.8 | 64.4 | T |
| 16 **TOP** | AMD | 182.6 | 67.1 | T |
| 17 **TOP** | AMAT | 174.9 | 66.5 | T |
| 18 **TOP** | WBD | 143.3 | 75.0 | T |
| 19 **TOP** | VLO | 138.1 | 66.1 | T |
| 20 **TOP** | NOK | 130.9 | 49.4 | T |
| 21 **TOP** | GLW | 117.2 | 53.1 | T |
| 22 **TOP** | MPC | 113.1 | 66.8 | T |
| 23  | MTSI | 104.5 | 60.9 | T |
| 24  | CRWD | 103.0 | 67.1 | T |
| 25  | KLAC | 96.0 | 63.2 | T |
| 26  | PANW | 90.1 | 58.6 | T |
| 27  | PSX | 88.7 | 61.9 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNH | Other | 364.65 | 31.7 | 4.8 | -4.1% | -7.6% | 27.9 | 23.4 | 14.0 | -0.7 | ✅ value |
| 🟡 dip | REGN | Other | 741.63 | 36.2 | 14.0 | -5.9% | -5.3% | 41.9 | 17.7 | 21.7 | 56.8 | ⚠️ rich |
| 🟢 oversold | V | Other | 359.04 | 38.9 | 5.7 | -2.5% | -2.6% | 5.9 | 30.5 | 31.9 | 2.1 | — |
| 🟡 dip | IBKR | Financials | 86.53 | 41.7 | 53.4 | -3.5% | -4.6% | 45.2 | 34.1 | 9.4 | 1.1 | ✅ value |
| 🟡 dip | TKR | Other | 117.81 | 44.0 | 77.3 | -0.1% | -5.9% | 54.2 | 31.7 | 21.2 | -1.9 | ✅ value |
| 🟡 dip | AMZN | Other | 248.92 | 44.9 | 64.3 | -1.2% | -2.8% | 11.3 | 19.8 | -230.3 | 0.2 | ✅ value |
| 🟡 dip | GOOGL | Other | 339.25 | 46.1 | 24.9 | -1.0% | -1.3% | 57.4 | 16.7 | 76.5 | 0.1 | ✅ value |
| 🟡 dip | FCEL | Battery/H2 | 16.84 | 47.7 | 65.9 | +2.2% | -9.8% | 306.7 | -4.9 | -12.6 | -0.0 | — |
| 🟡 dip | CRDO | Other | 208.5 | 56.3 | 87.1 | +16.8% | +0.1% | 67.9 | 69.9 | 87.7 | 0.2 | ✅ value |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNP | Other | 270.6 | 30.1 | 3.5 | -3.2% | -7.0% | 30.0 | 21.8 | 24.7 | 3.0 | — |
| 🟢 oversold | IWM | Index-ETF | 279.12 | 33.2 | 52.4 | -2.3% | -4.7% | 23.6 | — | — | — |  |
| 🟢 oversold | JPM | Other | 332.15 | 33.6 | 32.5 | -4.2% | -5.8% | 17.8 | 14.3 | -5.5 | 0.7 | ✅ value |
| 🟢 oversold | DIA | Index-ETF | 507.99 | 34.6 | 7.3 | -2.2% | -3.6% | 15.7 | — | — | — |  |
| 🟢 oversold | C | Other | 126.99 | 34.8 | 3.6 | -5.3% | -5.2% | 37.2 | 13.4 | -8.9 | 0.4 | ✅ value |
| 🟡 dip | NUE | Other | 234.85 | 35.7 | 14.4 | -6.4% | -8.2% | 69.4 | 18.7 | 33.7 | 0.1 | ✅ value |
| 🟢 oversold | JNJ | Other | 259.26 | 35.9 | 2.0 | -3.5% | -2.6% | 53.1 | 29.9 | 33.3 | -3.7 | — |
| 🟢 oversold | ROKU | Other | 150.71 | 38.3 | 3.9 | -2.3% | -1.5% | 61.1 | 62.8 | 27.1 | 0.0 | — |
| 🟢 oversold | KO | Other | 85.87 | 38.5 | 1.6 | -2.2% | -2.2% | 27.6 | 25.8 | 25.8 | 1.5 | ✅ value |
| 🟡 dip | BMY | Other | 61.62 | 39.7 | 13.4 | -2.9% | -4.5% | 41.8 | 13.5 | 11.0 | 0.2 | ✅ value |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 497.3 | 67.8 |  |
| MPC | 98.7 | 66.8 |  |
| VLO | 112.6 | 66.1 |  |
| NET | 33.0 | 61.7 |  |
| LITE | 434.0 | 63.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -78.0 | 29.1 |  |
| RCAT | -20.3 | 31.0 | SPEC |
| OKLO | -65.5 | 41.0 | SPEC |
| JOBY | -58.6 | 34.6 | SPEC |
| BWXT | -12.4 | 32.2 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._