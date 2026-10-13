# Strategy report - INTRADAY  (2026-10-13 19:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | A+ | 12/12 | #12 | 21 EMA pullback | Semis |  | HELD | 2026-11-03 | 597.34 | 22.1 | 597.34 | 550.28 | 649.42 | -7.9% |
| NVDA | A+ | 12/12 | #16 | 21 EMA pullback | Semis |  |  |  | 227.4 | 30.4 | 227.4 | 219.67 | 238.99 | -3.4% |
| QQQ | A+ | 12/12 | #18 | 21 EMA pullback | Index-ETF |  |  |  | 742.47 | 13.8 | 742.47 | 725.16 | 759.66 | -2.3% |
| LITE | A+ | 11/12 | #21 | 21 EMA pullback | Photonics |  |  |  | 974.89 | 15.8 | 974.89 | 865.76 | 1133.4 | -11.2% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🔴 **Correlated cluster:** 3/4 setups are in the AI/tech complex (semis, AI-infra, quantum, photonics). They move together — buying several is **ONE leveraged AI bet, not diversification.** Pick 1-2, not the cluster.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 5/12), LRCX (C 3/12), KLAC (C 4/12), ARM (C 6/12), MU (C 7/12), SMCI (B 10/12), VRTX (C 5/12), CRDO (C 3/12)

## Quality ranking — top 25 of 224 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +215.7% | -3.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +55.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +52.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +45.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | DELL | A+ | 12/12 | +35.6% | -2.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | CRWD | A+ | 12/12 | +23.7% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | COP | A+ | 12/12 | +23.2% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | TMO | A+ | 12/12 | +21.0% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | XOM | A+ | 12/12 | +17.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | CVX | A+ | 12/12 | +17.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | WBD | A+ | 12/12 | +15.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AMD | A+ | 12/12 | +9.7% | -8.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +9.2% | -2.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | PM | A+ | 12/12 | +8.1% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +8.1% | -0.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | NVDA | A+ | 12/12 | +4.0% | -4.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AAPL | A+ | 12/12 | +1.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | QQQ | A+ | 12/12 | +0.4% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PLTR | A+ | 11/12 | +52.8% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +34.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | LITE | A+ | 11/12 | +26.9% | -13.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | EMR | A+ | 11/12 | +16.7% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | DVN | B | 11/12 | +13.4% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | OXY | B | 11/12 | +11.7% | -6.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | PFE | B | 11/12 | +11.1% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 217)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 520.3 | 38.7 | T |
| 2 **TOP** | MRNA | 512.4 | 66.7 | T |
| 3 **TOP** | LITE | 468.7 | 49.2 | T |
| 4 **TOP** | WDC | 357.9 | 34.4 | F |
| 5 **TOP** | DELL | 353.7 | 57.3 | T |
| 6 **TOP** | INTC | 327.5 | 41.3 | T |
| 7 **TOP** | AAOI | 289.2 | 42.1 | F |
| 8 **TOP** | MRVL | 250.6 | 55.3 | T |
| 9 **TOP** | AMD | 225.5 | 53.6 | T |
| 10 **TOP** | VIAV | 222.1 | 49.0 | T |
| 11 **TOP** | COHR | 196.5 | 44.5 | F |
| 12 **TOP** | AMAT | 172.0 | 38.6 | T |
| 13 **TOP** | LRCX | 155.0 | 40.9 | T |
| 14 **TOP** | VLO | 149.1 | 75.3 | T |
| 15 **TOP** | FCEL | 131.3 | 41.8 | T |
| 16 **TOP** | MPC | 119.6 | 77.8 | T |
| 17 **TOP** | MTSI | 108.5 | 52.8 | T |
| 18 **TOP** | PSX | 98.4 | 76.5 | T |
| 19 **TOP** | CAT | 89.7 | 37.0 | F |
| 20 **TOP** | CRWD | 89.6 | 56.3 | T |
| 21 **TOP** | KLAC | 87.4 | 42.1 | T |
| 22  | NUE | 83.5 | 54.5 | T |
| 23  | ARM | 75.8 | 40.4 | T |
| 24  | MRK | 73.8 | 43.9 | T |
| 25  | TGT | 73.2 | 43.2 | T |
| 26  | FDX | 68.8 | 41.2 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 937 | 38.7 | 3.3 | -10.1% | -4.5% | 520.3 | EXPENSIVE -50% (LOW) | 473.0 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | CRDO | Other | 195.8 | 47.0 | 9.6 | -1.4% | -6.4% | 0.6 | EXPENSIVE -40% (MED) | 113.59 | +45% | DISRUPTOR [research: disruptor] | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year; research 2026-10-12: Invented the active electrical cable (AEC) market for AI data centers and holds ~88% of it (650 Group); Jefferies sees AEC units 8.6M in 2026 to 12.3M in 2027. |
| 🟡 dip | AMZN | Other | 259.12 | 55.1 | 49.0 | +2.5% | +0.3% | 12.5 | DEEP VALUE +100% (LOW) | 522.95 | +24% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | VRTX | Other | 488 | 32.9 | 8.2 | -4.7% | -6.4% | 30.6 | FAIR -2% (HIGH) | 486.0 | +21% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟢 oversold | AMAT | Semis | 455.78 | 38.6 | 0.4 | -6.9% | -6.7% | 172.0 | EXPENSIVE -50% (LOW) | 238.0 | +36% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year |
| 🟢 oversold | ARM | Semis | 254.55 | 40.4 | 1.2 | -12.3% | -5.9% | 75.8 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | LRCX | Semis | 296.33 | 40.9 | 0.6 | -5.6% | -4.7% | 155.0 | EXPENSIVE -50% (LOW) | 151.0 | +21% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +50% next year; gross margin up 4 pts (50%) |
| 🟢 oversold | JNJ | Other | 248.2 | 34.1 | 14.2 | -5.8% | -6.5% | 49.2 | RICH -25% (HIGH) | 188.16 | +13% | STABLE | steady | disruption: R&D 16% of revenue |
| 🟢 oversold | KLAC | Semis | 182.3 | 42.1 | 0.7 | -4.1% | -3.1% | 87.4 | EXPENSIVE -50% (MED) | 93.03 | +18% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why | disruption: revenue +14%/yr over 5 yrs; analysts see revenue +34% next year |
| 🟡 dip | ROST | Other | 225.31 | 42.3 | 55.9 | -1.9% | -3.9% | 56.0 | FAIR -9% (HIGH) | 204.92 | +26% | STABLE [research: neutral] | steady | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |
| 🟡 dip | REGN | Other | 754.32 | 45.8 | 53.7 | -1.3% | -4.5% | 39.6 | FAIR +4% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +22% next year; R&D 41% of revenue |
| 🟡 dip | LLY | Other | 1158.73 | 47.8 | 20.4 | -0.5% | -1.4% | 47.7 | FAIR +2% (LOW) | 1195.82 | +17% | DISRUPTOR | steady: business changed (margin 54% vs 29% 10-yr median): its own history is a weak yardstick | disruption: revenue +32%/yr over 3 yrs; analysts see revenue +36% next year |
| 🟡 dip | DIA | Index-ETF | 516.52 | 48.6 | 57.6 | +0.4% | -1.7% | 14.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -36% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +9% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 446.7 | 66.7 |  |
| DELL | 254.8 | 57.3 |  |
| CRWD | 90.7 | 56.3 |  |
| COP | 55.9 | 69.4 |  |
| TMO | 16.9 | 56.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| OKLO | -75.4 | 33.3 | SPEC |
| ASTS | -26.9 | 32.4 | SPEC |
| QBTS | -49.0 | 27.5 | SPEC |
| UUUU | -39.3 | 25.7 | SPEC |
| APLD | -27.7 | 36.8 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._