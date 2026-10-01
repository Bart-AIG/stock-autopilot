# Strategy report - INTRADAY  (2026-10-01 17:10 UTC)

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
| TMO | A+ | 12/12 | #8 | RSI2 dip | Other |  |  |  | 660.33 | 6.9 | 660.33 | 636.47 | 679.61 | -3.6% |
| MRK | A+ | 12/12 | #10 | RSI2 dip | Other |  |  |  | 143.88 | 6.0 | 143.88 | 139.73 | 150.1 | -2.9% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JNJ (C 7/12), FCX (C 5/12), KO (C 7/12), VRTX (C 7/12), UNH (C 3/12), UNP (C 3/12), LLY (C 5/12), ABBV (B 11/12), DIA (C 3/12), GILD (B 11/12), PM (B 9/12)

## Quality ranking — top 25 of 144 (A = buyable, B = holdable)
| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Traits firing |
|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +137.6% | -6.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +52.7% | -2.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | NET | A+ | 12/12 | +41.6% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LITE | A+ | 12/12 | +41.0% | -0.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | DELL | A+ | 12/12 | +34.4% | -8.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | CRWD | A+ | 12/12 | +33.8% | -0.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | SNOW | A+ | 12/12 | +27.9% | -5.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | TMO | A+ | 12/12 | +23.9% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | PANW | A+ | 12/12 | +9.7% | -1.9% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | MRK | A+ | 12/12 | +8.8% | -8.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | HPQ | A+ | 11/12 | +44.1% | -9.5% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PLTR | A+ | 11/12 | +43.5% | -9.0% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AEHR | A+ | 11/12 | +42.3% | -30.5% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | TGT | A+ | 11/12 | +18.5% | -7.4% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | XOM | B | 11/12 | +16.9% | -4.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 16 | WBD | B | 11/12 | +14.5% | -0.1% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 17 | PFE | B | 11/12 | +13.7% | -2.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 18 | EMR | B | 11/12 | +11.0% | -4.1% | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | GILD | B | 11/12 | +10.2% | -5.3% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 20 | ETN | B | 11/12 | +6.5% | -5.8% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | DDOG | B | 11/12 | +2.7% | -5.2% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | ABBV | B | 11/12 | -2.9% | -2.6% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | SMCI | B | 10/12 | +49.2% | -29.7% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | PSX | B | 10/12 | +46.4% | -4.4% | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 25 | CVX | B | 10/12 | +19.6% | -5.3% | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 14 of 140)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | LITE | 554.3 | 63.6 | T |
| 2 **TOP** | MRNA | 540.4 | 67.5 | T |
| 3 **TOP** | AAOI | 327.2 | 49.4 | F |
| 4 **TOP** | FCEL | 306.7 | 46.6 | T |
| 5 **TOP** | BE | 303.5 | 55.0 | T |
| 6 **TOP** | DELL | 247.9 | 53.5 | T |
| 7 **TOP** | TSEM | 238.4 | 58.3 | T |
| 8 **TOP** | MRVL | 234.6 | 62.3 | T |
| 9 **TOP** | VIAV | 208.6 | 67.6 | T |
| 10 **TOP** | AEHR | 207.0 | 55.1 | T |
| 11 **TOP** | COHR | 200.7 | 55.9 | T |
| 12 **TOP** | NBIS | 192.1 | 52.4 | T |
| 13 **TOP** | WBD | 143.3 | 74.9 | T |
| 14 **TOP** | NOK | 130.9 | 48.5 | T |
| 15  | GLW | 117.2 | 52.4 | T |
| 16  | MPC | 113.1 | 65.4 | T |
| 17  | MTSI | 104.5 | 60.5 | T |
| 18  | CRWD | 103.0 | 66.2 | T |
| 19  | PANW | 90.1 | 57.5 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. The P/E, P/FCF, PEG columns are **secondary value context** — not the headline read (Val: ✅ cheap-for-growth / ⚠️ rich / — / blank = no data).

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNH | Other | 363.55 | 31.0 | 4.4 | -4.4% | -7.9% | 27.9 | — | — | — |  |
| 🟡 dip | IBKR | Financials | 86.5 | 41.6 | 52.7 | -3.6% | -4.7% | 45.2 | — | — | — |  |
| 🟡 dip | TKR | Other | 118.17 | 45.1 | 81.5 | +0.2% | -5.6% | 54.2 | — | — | — |  |
| 🟡 dip | FCEL | Battery/H2 | 16.62 | 46.6 | 55.8 | +1.0% | -10.9% | 306.7 | — | — | — |  |
| 🟡 dip | CRDO | Other | 207.71 | 56.0 | 86.6 | +16.4% | -0.3% | 67.9 | — | — | — |  |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | P/E | P/FCF | PEG | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | UNP | Other | 270.94 | 30.5 | 4.4 | -3.1% | -6.9% | 30.0 | — | — | — |  |
| 🟢 oversold | IWM | Index-ETF | 278.86 | 32.5 | 46.7 | -2.4% | -4.8% | 23.6 | — | — | — |  |
| 🟢 oversold | DIA | Index-ETF | 507.42 | 34.1 | 7.2 | -2.3% | -3.7% | 15.7 | — | — | — |  |
| 🟢 oversold | NUE | Other | 234.18 | 34.9 | 12.0 | -6.7% | -8.4% | 69.4 | — | — | — |  |
| 🟢 oversold | JNJ | Other | 259.24 | 35.8 | 2.1 | -3.6% | -2.6% | 53.1 | — | — | — |  |
| 🟡 dip | BMY | Other | 61.28 | 38.4 | 12.1 | -3.5% | -5.0% | 41.8 | — | — | — |  |
| 🟢 oversold | KO | Other | 86.09 | 39.6 | 3.8 | -2.0% | -2.0% | 27.6 | — | — | — |  |
| 🟡 dip | NEM | Other | 114.76 | 39.8 | 11.9 | -6.9% | -2.3% | 64.8 | — | — | — |  |
| 🟢 oversold | VRTX | Other | 507.71 | 40.6 | 3.8 | -2.7% | -1.9% | 40.1 | — | — | — |  |
| 🟢 oversold | FCX | Other | 69.11 | 42.7 | 2.2 | -3.8% | -1.8% | 63.2 | — | — | — |  |

_The technical screen is the SIGNAL (oversold within an uptrend); the value columns are context. Confirm each with the news/thesis (HARD RULE 7) and a real valuation before buying — an oversold name can keep falling if the thesis is broken._

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 497.3 | 67.5 |  |
| MPC | 98.7 | 65.4 |  |
| NET | 33.0 | 60.7 |  |
| LITE | 434.0 | 63.6 |  |
| DELL | 199.8 | 53.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -78.0 | 28.7 |  |
| OKLO | -65.5 | 41.1 | SPEC |
| BWXT | -12.4 | 32.2 | SPEC |
| DKNG | -37.3 | 27.3 |  |
| BKSY | 6.5 | 41.4 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._