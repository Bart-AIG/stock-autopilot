# Strategy report - INTRADAY  (2026-10-13 17:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | A+ | 12/12 | #13 | 21 EMA pullback | Semis |  | HELD | 2026-11-03 | 597.64 | 23.4 | 597.64 | 550.57 | 649.42 | -7.9% |
| NVDA | A+ | 12/12 | #17 | 21 EMA pullback | Semis |  |  |  | 227.01 | 22.8 | 227.01 | 219.3 | 238.58 | -3.4% |
| QQQ | A+ | 12/12 | #19 | 21 EMA pullback | Index-ETF |  |  |  | 742.29 | 13.5 | 742.29 | 724.96 | 759.66 | -2.3% |
| LITE | A+ | 11/12 | #22 | 21 EMA pullback | Photonics |  |  |  | 972.5 | 15.5 | 972.5 | 863.44 | 1133.4 | -11.2% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- 🔴 **Correlated cluster:** 3/4 setups are in the AI/tech complex (semis, AI-infra, quantum, photonics). They move together — buying several is **ONE leveraged AI bet, not diversification.** Pick 1-2, not the cluster.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 5/12), LRCX (C 3/12), KLAC (C 4/12), MU (C 7/12), SMCI (B 10/12), CRDO (C 3/12), VRTX (C 5/12)

## Quality ranking — top 25 of 224 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +212.5% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +54.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +51.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | RBRK | A+ | 12/12 | +45.1% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | PSX | A+ | 12/12 | +44.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +35.7% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +24.0% | -5.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | COP | A+ | 12/12 | +22.8% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +21.0% | -2.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | XOM | A+ | 12/12 | +17.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | CVX | A+ | 12/12 | +17.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | WBD | A+ | 12/12 | +15.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMD | A+ | 12/12 | +10.3% | -7.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | ABBV | A+ | 12/12 | +10.2% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | PM | A+ | 12/12 | +7.9% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | EOG | A+ | 12/12 | +7.9% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | NVDA | A+ | 12/12 | +3.8% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | AAPL | A+ | 12/12 | +1.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | QQQ | A+ | 12/12 | +0.5% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | PLTR | A+ | 11/12 | +51.4% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MSFT | A+ | 11/12 | +34.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | LITE | A+ | 11/12 | +26.4% | -14.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | EMR | B | 11/12 | +16.1% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | DVN | B | 11/12 | +13.1% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | AMGN | B | 11/12 | +12.8% | -6.6% | RICH -22% (HIGH) | INNOVATING | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 218)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 520.3 | 38.7 | T |
| 2 **TOP** | MRNA | 512.4 | 66.1 | T |
| 3 **TOP** | LITE | 468.7 | 48.8 | T |
| 4 **TOP** | WDC | 357.9 | 34.6 | F |
| 5 **TOP** | DELL | 353.7 | 57.4 | T |
| 6 **TOP** | INTC | 327.5 | 41.3 | T |
| 7 **TOP** | AAOI | 289.2 | 42.4 | F |
| 8 **TOP** | MRVL | 250.6 | 55.5 | T |
| 9 **TOP** | AMD | 225.5 | 54.4 | T |
| 10 **TOP** | VIAV | 222.1 | 48.4 | T |
| 11 **TOP** | COHR | 196.5 | 44.1 | F |
| 12 **TOP** | AMAT | 172.0 | 40.2 | T |
| 13 **TOP** | LRCX | 155.0 | 41.5 | T |
| 14 **TOP** | VLO | 149.1 | 74.8 | T |
| 15 **TOP** | FCEL | 131.3 | 41.8 | T |
| 16 **TOP** | MPC | 119.6 | 77.4 | T |
| 17 **TOP** | MTSI | 108.5 | 51.5 | T |
| 18 **TOP** | PSX | 98.4 | 75.9 | T |
| 19 **TOP** | CAT | 89.7 | 35.9 | F |
| 20 **TOP** | CRWD | 89.6 | 56.5 | T |
| 21 **TOP** | KLAC | 87.4 | 42.5 | T |
| 22  | NUE | 83.5 | 53.8 | T |
| 23  | ARM | 75.8 | 41.7 | T |
| 24  | MRK | 73.8 | 46.3 | T |
| 25  | TGT | 73.2 | 43.5 | T |
| 26  | FDX | 68.8 | 39.4 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 937.16 | 38.7 | 3.3 | -10.1% | -4.5% | 520.3 | EXPENSIVE -50% (LOW) | 473.0 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | CRDO | Other | 193.35 | 46.0 | 8.7 | -2.6% | -7.6% | 0.6 | EXPENSIVE -40% (MED) | 113.59 | +45% | DISRUPTOR [research: disruptor] | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year; research 2026-10-12: Invented the active electrical cable (AEC) market for AI data centers and holds ~88% of it (650 Group); Jefferies sees AEC units 8.6M in 2026 to 12.3M in 2027. |
| 🟡 dip | AMZN | Other | 260.24 | 56.3 | 59.4 | +2.9% | +0.7% | 12.5 | DEEP VALUE +100% (LOW) | 522.95 | +24% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | VRTX | Other | 490.6 | 34.0 | 9.2 | -4.2% | -5.9% | 30.6 | FAIR -2% (HIGH) | 486.0 | +21% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟢 oversold | AMAT | Semis | 462.8 | 40.2 | 0.5 | -5.5% | -5.3% | 172.0 | EXPENSIVE -50% (LOW) | 238.0 | +36% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year |
| 🟢 oversold | LRCX | Semis | 297.93 | 41.5 | 0.6 | -5.1% | -4.2% | 155.0 | EXPENSIVE -50% (LOW) | 151.0 | +21% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +50% next year; gross margin up 4 pts (50%) |
| 🟢 oversold | JNJ | Other | 245.63 | 32.4 | 12.9 | -6.8% | -7.4% | 49.2 | RICH -25% (HIGH) | 188.16 | +13% | STABLE | steady | disruption: R&D 16% of revenue |
| 🟢 oversold | KLAC | Semis | 182.86 | 42.5 | 0.7 | -3.8% | -2.8% | 87.4 | EXPENSIVE -50% (MED) | 93.03 | +18% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why | disruption: revenue +14%/yr over 5 yrs; analysts see revenue +34% next year |
| 🟡 dip | ROST | Other | 224.67 | 41.4 | 46.7 | -2.1% | -4.2% | 56.0 | FAIR -9% (HIGH) | 204.92 | +26% | STABLE [research: neutral] | steady | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |
| 🟡 dip | REGN | Other | 752.41 | 45.2 | 48.9 | -1.5% | -4.7% | 39.6 | FAIR +4% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +22% next year; R&D 41% of revenue |
| 🟡 dip | CL | Other | 89.78 | 60.4 | 83.6 | +3.4% | +0.7% | 4.2 | FAIR -8% (HIGH) | 82.19 | +12% | STABLE | steady |
| 🟡 dip | ARM | Semis | 257.91 | 41.7 | 21.8 | -11.2% | -4.7% | 75.8 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟡 dip | DIA | Index-ETF | 515.78 | 47.6 | 48.3 | +0.3% | -1.8% | 14.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

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
| MRNA | 446.7 | 66.1 |  |
| VLO | 142.3 | 74.8 |  |
| RBRK | 21.7 | 58.7 | SPEC |
| DELL | 254.8 | 57.4 |  |
| CRWD | 90.7 | 56.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| OKLO | -75.4 | 33.3 | SPEC |
| ASTS | -26.9 | 32.4 | SPEC |
| UUUU | -39.3 | 25.4 | SPEC |
| QBTS | -49.0 | 27.8 | SPEC |
| APLD | -27.7 | 37.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._