# Strategy report - MORNING  (2026-10-05 14:11 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XOM | A+ | 11/12 | #21 | 21 EMA pullback | Energy |  |  |  | 163.22 | 40.8 | 163.22 | 157.26 | 169.32 | -3.7% |
| DE | A+ | 11/12 | #22 | 21 EMA pullback | Other |  |  |  | 678.95 | 47.4 | 678.95 | 654.48 | 709.48 | -3.6% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JNJ (C 6/12), KO (C 6/12), PFE (B 10/12), TGT (B 8/12), VRTX (C 6/12), BMY (C 5/12), GILD (B 10/12), ROST (C 3/12), PM (C 5/12), MRK (B 9/12)

## Quality ranking — top 25 of 238 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +135.7% | -6.4% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +58.4% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | LITE | A+ | 12/12 | +52.2% | -0.1% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | VLO | A+ | 12/12 | +51.9% | -0.2% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CRWD | A+ | 12/12 | +36.7% | 0.0% | EXPENSIVE -49% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +30.2% | -5.5% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | NET | A+ | 12/12 | +29.4% | -0.8% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | SNOW | A+ | 12/12 | +26.6% | -4.5% | FAIR +2% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +24.7% | -2.9% | RICH -17% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +18.8% | -0.8% | EXPENSIVE -37% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +17.4% | 0.0% | FAIR -6% (MED) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PANW | A+ | 12/12 | +17.4% | 0.0% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | EMR | A+ | 12/12 | +14.2% | -1.7% | EXPENSIVE -31% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +4.4% | -2.2% | EXPENSIVE -34% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +2.9% | 0.0% | N/A | N/A | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | AEHR | A+ | 11/12 | +51.9% | -28.8% | EXPENSIVE -50% (LOW) | BEING DISRUPTED | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | RBRK | A+ | 11/12 | +37.8% | 0.0% | EXPENSIVE -29% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PLTR | A+ | 11/12 | +37.4% | -8.9% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MSFT | A+ | 11/12 | +32.6% | -2.7% | RICH -16% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | WBD | A+ | 11/12 | +15.4% | 0.0% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | XOM | A+ | 11/12 | +12.2% | -4.8% | EXPENSIVE -31% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | DE | A+ | 11/12 | +9.4% | -4.3% | EXPENSIVE -45% (HIGH) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | QLD | A+ | 11/12 | +7.0% | -1.8% | N/A | N/A | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | DDOG | B | 11/12 | +6.6% | -2.3% | EXPENSIVE -28% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | ETN | B | 11/12 | +6.6% | -5.7% | EXPENSIVE -36% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 23 of 231)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 673.8 | 56.3 | T |
| 2 **TOP** | LITE | 489.6 | 66.6 | T |
| 3 **TOP** | MRNA | 479.0 | 66.4 | T |
| 4 **TOP** | WDC | 407.9 | 46.6 | T |
| 5 **TOP** | BE | 343.1 | 57.3 | T |
| 6 **TOP** | AAOI | 339.9 | 56.6 | T |
| 7 **TOP** | DELL | 319.9 | 56.5 | T |
| 8 **TOP** | INTC | 291.2 | 56.4 | T |
| 9 **TOP** | FCEL | 269.1 | 49.9 | T |
| 10 **TOP** | MRVL | 253.0 | 63.0 | T |
| 11 **TOP** | TSEM | 251.7 | 59.8 | T |
| 12 **TOP** | NBIS | 245.8 | 54.2 | T |
| 13 **TOP** | AEHR | 237.5 | 56.0 | T |
| 14 **TOP** | AMD | 216.0 | 68.1 | T |
| 15 **TOP** | VIAV | 199.0 | 72.7 | T |
| 16 **TOP** | LRCX | 198.8 | 65.6 | T |
| 17 **TOP** | COHR | 188.1 | 58.4 | T |
| 18 **TOP** | AMAT | 179.4 | 68.0 | T |
| 19 **TOP** | VLO | 136.5 | 67.9 | T |
| 20 **TOP** | WBD | 133.3 | 75.2 | T |
| 21 **TOP** | ILMN | 120.6 | 72.4 | T |
| 22 **TOP** | NOK | 120.4 | 48.1 | T |
| 23 **TOP** | GLW | 116.7 | 53.4 | T |
| 24  | MPC | 115.7 | 71.5 | T |
| 25  | MTSI | 107.1 | 66.8 | T |
| 26  | KLAC | 105.1 | 60.1 | T |
| 27  | CRWD | 104.1 | 69.5 | T |
| 28  | PSX | 93.9 | 64.9 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | V | Other | 362.81 | 44.5 | 74.1 | -1.1% | -1.6% | 9.3 | FAIR -0% (HIGH) | 363.29 | +15% | STABLE | steady | disruption: revenue +11%/yr over 3 yrs |
| 🟡 dip | IBKR | Financials | 88.34 | 46.7 | 85.0 | -1.0% | -2.5% | 54.0 | EXPENSIVE -33% (LOW) | 59.24 | +23% | INNOVATING | steady: its multiples disagree with each other; analysts disagree | disruption: revenue +35%/yr over 3 yrs; analysts expect revenue -27% next year |
| 🟡 dip | AMZN | Other | 251.81 | 48.9 | 86.1 | +0.2% | -2.0% | 11.3 | DEEP VALUE +100% (LOW) | 503.28 | +29% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |
| 🟡 dip | CRSP | Gene-edit | 54.99 | 49.1 | 21.2 | +0.2% | +0.8% | 1.7 | N/A | — | — | DISRUPTOR | preprofit: not enough history for this industry's multiples | disruption: revenue +100%/yr over 3 yrs; analysts see revenue +945% next year |
| 🟡 dip | GOOGL | Other | 344.88 | 51.1 | 72.8 | +0.6% | +0.0% | 44.0 | RICH -23% (LOW) | 264.76 | +23% | DISRUPTOR | growth: business changed (margin 73% vs 33% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: revenue +13%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟡 dip | TKR | Other | 120.4 | 50.9 | 52.2 | +2.1% | -3.2% | 58.3 | EXPENSIVE -44% (HIGH) | 67.35 | +16% | STABLE | steady | disruption: revenue flat (+1%/yr over 3 yrs) |
| 🟡 dip | CRDO | Other | 209.43 | 55.3 | 46.9 | +14.3% | +0.7% | 21.1 | EXPENSIVE -44% (MED) | 117.48 | +31% | DISRUPTOR | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year |
| 🟡 dip | UNH | Other | 370.43 | 39.3 | 52.5 | -1.9% | -5.7% | 25.9 | FAIR +6% (HIGH) | 393.15 | +32% | AT RISK | steady | disruption: revenue +11%/yr over 3 yrs; analysts expect revenue -0% next year |
| 🟡 dip | FCEL | Battery/H2 | 17.3 | 49.9 | 45.3 | +3.2% | -6.3% | 269.1 | DEEP VALUE +100% (LOW) | 35.02 | +26% | AT RISK | **VALUE TRAP?** preprofit: far from its own history: the market has re-rated it, find out why; analysts agree | disruption: analysts expect revenue -7% next year; R&D 22% of revenue |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | KO | Other | 85.31 | 35.8 | 1.1 | -2.6% | -3.1% | 29.6 | FAIR +6% (HIGH) | 90.19 | +11% | STABLE | steady |
| 🟢 oversold | VRTX | Other | 502.38 | 37.8 | 2.1 | -2.8% | -3.1% | 37.9 | FAIR -4% (HIGH) | 484.31 | +20% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟢 oversold | ROST | Other | 227.17 | 41.3 | 5.2 | -1.5% | -4.4% | 52.8 | FAIR -9% (HIGH) | 207.27 | +24% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟢 oversold | MRK | Other | 141.33 | 40.5 | 7.2 | -3.5% | -0.8% | 77.5 | EXPENSIVE -37% (LOW) | 88.79 | +21% | STABLE | steady: its multiples disagree with each other; analysts disagree | disruption: R&D 19% of revenue |
| 🟢 oversold | GILD | Other | 144.38 | 43.1 | 2.5 | -2.7% | +0.6% | 31.2 | RICH -23% (LOW) | 110.6 | +4% | STABLE | steady: business changed (margin 2% vs 40% 10-yr median): its own history is a weak yardstick | disruption: revenue flat (+3%/yr over 3 yrs); R&D 20% of revenue |
| 🟢 oversold | AMGN | Other | 402.1 | 47.2 | 8.4 | +1.2% | -1.9% | 54.1 | RICH -22% (HIGH) | 314.81 | -0% | INNOVATING | steady: analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin slipping 4 pts (71%) |
| 🟢 oversold | JNJ | Other | 254.75 | 31.0 | 0.9 | -4.5% | -4.2% | 54.3 | EXPENSIVE -26% (HIGH) | 188.16 | +11% | STABLE | steady | disruption: R&D 16% of revenue |
| 🟢 oversold | JPM | Other | 330.94 | 33.3 | 19.9 | -3.8% | -5.9% | 21.8 | EXPENSIVE -31% (HIGH) | 228.96 | +12% | STABLE | bank |
| 🟢 oversold | PM | Other | 187.12 | 44.4 | 6.6 | -1.6% | -1.4% | 13.0 | EXPENSIVE -28% (HIGH) | 134.93 | +14% | STABLE | steady |
| 🟢 oversold | BMY | Other | 59.44 | 31.8 | 2.5 | -5.3% | -7.8% | 41.7 | DEEP VALUE +44% (MED) | 84.54 | +11% | AT RISK | **VALUE TRAP?** steady: analysts disagree | disruption: revenue flat (+1%/yr over 3 yrs); gross margin up 14 pts (71%) |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +107% next year |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +108% next year |
| DELL | yes | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +27%/yr over 3 yrs; analysts see revenue +48% next year |
| AMD | yes | EXPENSIVE -37% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +19% next year |
| VIAV | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | yes | FAIR +6% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 424.7 | 66.4 |  |
| MPC | 101.7 | 71.5 |  |
| LITE | 399.2 | 66.6 |  |
| VLO | 125.1 | 67.9 |  |
| CRWD | 73.1 | 69.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| BYND | -83.9 | 29.3 |  |
| RCAT | -25.9 | 32.1 | SPEC |
| DKNG | -30.7 | 31.3 |  |
| JOBY | -61.4 | 30.6 | SPEC |
| QBTS | -42.4 | 36.6 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._