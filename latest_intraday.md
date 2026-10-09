# Strategy report - INTRADAY  (2026-10-09 17:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | A+ | 12/12 | #11 | RSI2 dip | Semis |  |  |  | 229.37 | 9.1 | 229.37 | 220.5 | 239.24 | -3.9% |
| AAPL | A+ | 12/12 | #14 | 21 EMA pullback | Other |  |  |  | 335.08 | 34.4 | 335.08 | 326.4 | 341.07 | -2.6% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): DE (C 4/12), QCOM (C 5/12), ARM (C 7/12), INTC (C 7/12)

## Quality ranking — top 25 of 226 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +223.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +52.1% | -0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +46.1% | -0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LITE | A+ | 12/12 | +41.9% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CRWD | A+ | 12/12 | +41.3% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | PSX | A+ | 12/12 | +39.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | DELL | A+ | 12/12 | +32.5% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | PANW | A+ | 12/12 | +22.1% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +20.8% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +10.3% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +8.8% | -4.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | ABBV | A+ | 12/12 | +7.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PM | A+ | 12/12 | +7.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +1.7% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +1.6% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PLTR | A+ | 11/12 | +54.1% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | RBRK | A+ | 11/12 | +42.1% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +32.9% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | COP | A+ | 11/12 | +15.5% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 20 | WBD | A+ | 11/12 | +14.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | MRK | A+ | 11/12 | +13.7% | -6.8% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | XOM | A+ | 11/12 | +13.5% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | AMGN | B | 11/12 | +11.4% | -6.4% | RICH -21% (HIGH) | INNOVATING | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | DDOG | B | 11/12 | +8.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | DVN | B | 11/12 | +7.3% | -6.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 660.0 | 50.2 | T |
| 2 **TOP** | LITE | 551.8 | 63.8 | T |
| 3 **TOP** | MRNA | 454.2 | 70.8 | T |
| 4 **TOP** | WDC | 410.1 | 37.7 | F |
| 5 **TOP** | AAOI | 355.0 | 51.3 | T |
| 6 **TOP** | DELL | 341.3 | 61.0 | T |
| 7 **TOP** | INTC | 334.7 | 44.1 | T |
| 8 **TOP** | MRVL | 251.6 | 59.3 | T |
| 9 **TOP** | VIAV | 235.2 | 61.7 | T |
| 10 **TOP** | AMD | 234.4 | 57.9 | T |
| 11 **TOP** | FCEL | 219.9 | 48.5 | T |
| 12 **TOP** | COHR | 205.9 | 51.0 | T |
| 13 **TOP** | LRCX | 199.2 | 51.4 | T |
| 14 **TOP** | AMAT | 186.8 | 55.3 | T |
| 15 **TOP** | VLO | 140.3 | 77.0 | T |
| 16 **TOP** | WBD | 127.7 | 75.2 | T |
| 17 **TOP** | MTSI | 120.4 | 61.7 | T |
| 18 **TOP** | MPC | 118.1 | 79.4 | T |
| 19 **TOP** | KLAC | 99.3 | 54.7 | T |
| 20 **TOP** | PSX | 97.1 | 75.7 | T |
| 21 **TOP** | CRWD | 96.3 | 64.0 | T |
| 22 **TOP** | CAT | 95.1 | 44.8 | F |
| 23  | ARM | 87.7 | 43.9 | T |
| 24  | NUE | 82.9 | 52.3 | T |
| 25  | APLD | 78.6 | 40.1 | F |
| 26  | MRK | 74.4 | 52.0 | T |
| 27  | FCX | 73.7 | 55.7 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AUR | Other | 5.75 | 43.9 | 78.6 | -3.8% | -7.6% | 14.0 | N/A | — | — | INNOVATING | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year |
| 🟡 dip | AMZN | Other | 260.98 | 57.8 | 74.3 | +3.6% | +0.7% | 5.9 | DEEP VALUE +100% (LOW) | 517.46 | +26% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QCOM | Semis | 172.9 | 42.3 | 2.5 | -6.9% | -0.1% | 11.2 | FAIR -1% (HIGH) | 173.41 | +9% | INNOVATING | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year |
| 🟢 oversold | ARM | Semis | 266.41 | 43.9 | 2.6 | -7.8% | -1.3% | 87.7 | N/A | — | — | DISRUPTOR | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year |
| 🟢 oversold | DE | Other | 629.54 | 35.3 | 2.2 | -7.3% | -3.6% | 42.4 | EXPENSIVE -43% (HIGH) | 372.37 | +13% | STABLE | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%) |
| 🟡 dip | ROST | Other | 223.45 | 37.4 | 11.6 | -2.8% | -5.1% | 51.1 | FAIR -7% (HIGH) | 204.92 | +28% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟡 dip | REGN | Other | 746.07 | 41.9 | 79.7 | -2.7% | -5.5% | 45.1 | FAIR +4% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +21% next year; R&D 41% of revenue |
| 🟡 dip | VRTX | Other | 509.52 | 45.1 | 80.1 | -0.8% | -2.1% | 31.4 | FAIR -6% (HIGH) | 486.0 | +17% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | KO | Other | 88.21 | 55.0 | 90.6 | +0.9% | +0.3% | 29.0 | FAIR +3% (HIGH) | 90.21 | +8% | STABLE | steady |
| 🟡 dip | IWM | Index-ETF | 278.95 | 38.5 | 56.1 | -1.1% | -4.3% | 22.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | DIA | Index-ETF | 515.61 | 47.4 | 83.5 | +0.1% | -2.0% | 14.4 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | GM | Other | 82.38 | 49.7 | 78.1 | +0.2% | -2.9% | 44.4 | RICH -20% (LOW) | 65.59 | +23% | STABLE | cyclical: its multiples disagree with each other; analysts disagree | disruption: cyclical: judged on 5-yr trends |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +107% next year |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +48% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -37% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +8% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 389.3 | 70.8 |  |
| LITE | 473.7 | 63.8 |  |
| CRWD | 63.8 | 64.0 |  |
| DELL | 207.9 | 61.0 |  |
| PANW | 55.4 | 62.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| APP | -50.1 | 35.5 |  |
| ASTS | -26.2 | 33.5 | SPEC |
| OKLO | -70.4 | 38.2 | SPEC |
| UUUU | -24.3 | 30.3 | SPEC |
| QBTS | -51.4 | 31.8 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._