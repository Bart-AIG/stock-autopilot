# Strategy report - MORNING  (2026-10-14 14:13 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DELL | A+ | 12/12 | #5 | RSI2 dip | Other |  |  |  | 531.2 | 4.2 | 531.2 | 490.09 | 588.4 | -7.7% |
| CRWD | A+ | 12/12 | #7 | 21 EMA pullback | AI-software |  |  |  | 253.94 | 12.3 | 253.94 | 235.87 | 278.86 | -7.1% |
| AMD | A+ | 12/12 | #12 | 21 EMA pullback | Semis |  | HELD | 2026-11-03 | 586.47 | 18.9 | 586.47 | 538.43 | 649.42 | -8.2% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 4/12), LRCX (C 3/12), KLAC (C 3/12), ARM (C 6/12), SMCI (C 7/12), NBIS (C 4/12), MU (C 7/12), CRDO (C 3/12), QQQI (C 6/12), QQQ (B 10/12), FCEL (C 3/12), LITE (B 10/12), BHP (C 5/12), VIAV (B 9/12), PANW (B 9/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +233.0% | -5.7% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +53.1% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +48.6% | -0.3% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +42.6% | 0.0% | EXPENSIVE -46% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | DELL | A+ | 12/12 | +32.7% | -9.7% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | COP | A+ | 12/12 | +22.5% | 0.0% | RICH -19% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +21.6% | -8.9% | EXPENSIVE -46% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | TMO | A+ | 12/12 | +21.3% | -0.7% | RICH -17% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | XOM | A+ | 12/12 | +17.0% | 0.0% | EXPENSIVE -38% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | CVX | A+ | 12/12 | +16.6% | 0.0% | EXPENSIVE -26% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | WBD | A+ | 12/12 | +15.5% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AMD | A+ | 12/12 | +14.0% | -9.7% | EXPENSIVE -36% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | DVN | A+ | 12/12 | +13.5% | -3.7% | RICH -17% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | OXY | A+ | 12/12 | +12.2% | -6.7% | FAIR +7% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +7.8% | -0.1% | FAIR -4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | ABBV | A+ | 12/12 | +7.5% | -0.0% | EXPENSIVE -46% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | ADI | A+ | 12/12 | +3.8% | -8.7% | EXPENSIVE -46% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PM | A+ | 12/12 | +3.3% | -0.1% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | AAPL | A+ | 12/12 | +0.7% | 0.0% | EXPENSIVE -36% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | PLTR | A+ | 11/12 | +51.3% | -0.8% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MSFT | A+ | 11/12 | +32.1% | -0.3% | RICH -17% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | EMR | A+ | 11/12 | +13.9% | -1.1% | EXPENSIVE -31% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | PFE | A+ | 11/12 | +13.1% | 0.0% | EXPENSIVE -30% (MED) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | AMGN | B | 11/12 | +10.9% | -4.7% | RICH -24% (HIGH) | INNOVATING | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | MRK | B | 11/12 | +10.4% | -7.5% | EXPENSIVE -38% (MED) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 224)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 523.9 | 64.0 | T |
| 2 **TOP** | MU | 487.7 | 38.7 | T |
| 3 **TOP** | LITE | 412.2 | 45.5 | T |
| 4 **TOP** | WDC | 337.2 | 34.6 | F |
| 5 **TOP** | DELL | 327.3 | 46.4 | T |
| 6 **TOP** | INTC | 303.6 | 40.0 | T |
| 7 **TOP** | AAOI | 253.7 | 40.0 | F |
| 8 **TOP** | MRVL | 224.9 | 50.2 | T |
| 9 **TOP** | AMD | 211.2 | 50.3 | T |
| 10 **TOP** | VIAV | 181.1 | 47.7 | T |
| 11 **TOP** | COHR | 158.8 | 42.0 | F |
| 12 **TOP** | AMAT | 152.8 | 37.6 | T |
| 13 **TOP** | VLO | 144.4 | 74.9 | T |
| 14 **TOP** | NBIS | 134.7 | 35.4 | T |
| 15 **TOP** | LRCX | 133.8 | 38.9 | T |
| 16 **TOP** | FCEL | 122.4 | 40.6 | T |
| 17 **TOP** | MPC | 119.9 | 78.6 | T |
| 18 **TOP** | CRWD | 115.9 | 51.4 | T |
| 19 **TOP** | UMAC | 115.8 | 33.5 | F |
| 20 **TOP** | PSX | 96.6 | 77.4 | T |
| 21 **TOP** | PANW | 90.5 | 46.6 | T |
| 22 **TOP** | CAT | 81.7 | 36.3 | F |
| 23  | MTSI | 81.7 | 50.4 | T |
| 24  | NUE | 80.1 | 54.8 | T |
| 25  | SCCO | 79.5 | 51.8 | T |
| 26  | TGT | 76.4 | 43.0 | T |
| 27  | KLAC | 75.4 | 41.4 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 938.87 | 38.7 | 2.9 | -10.0% | -4.5% | 487.7 | EXPENSIVE -50% (LOW) | 472.12 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | QQQI | Other | 55.42 | 48.9 | 5.3 | -0.5% | +0.7% | 0.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | NVDA | Semis | 224.58 | 47.3 | 17.9 | -1.9% | +0.6% | 18.6 | FAIR -1% (MED) | 223.03 | +45% | DISRUPTOR | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year |
| 🟡 dip | AMZN | Other | 257.92 | 53.6 | 36.0 | +1.8% | -0.0% | 11.1 | DEEP VALUE +100% (LOW) | 514.02 | +26% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NBIS | Other | 186.34 | 35.4 | 1.8 | -18.3% | -16.8% | 134.7 | EXPENSIVE -50% (LOW) | 93.15 | +76% | DISRUPTOR | growth: business changed (margin 74% vs 23% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +240%/yr over 3 yrs; analysts see revenue +531% next year |
| 🟢 oversold | ARM | Semis | 242.51 | 37.0 | 0.8 | -16.5% | -10.1% | 58.7 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | AMAT | Semis | 452.25 | 37.6 | 0.3 | -8.0% | -7.1% | 152.8 | EXPENSIVE -50% (LOW) | 227.72 | +42% | INNOVATING [research: neutral] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year; research 2026-10-13: Broadest equipment maker, gains from AI chip demand, but Mizuho expects it to lag the WFE market as Chinese rivals (AMEC, Naura) win domestic share in core tools; date of that note is unclear, so evidence is thin. |
| 🟢 oversold | LRCX | Semis | 291.31 | 38.9 | 0.4 | -7.6% | -6.2% | 133.8 | EXPENSIVE -50% (LOW) | 146.66 | +24% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +51% next year; gross margin up 4 pts (50%); research 2026-10-13: Etch/deposition leader benefiting from AI and memory tightness (RBC, Apr 2026); China exposure falling as global spend rises. Chinese etch makers (AMEC, Naura) are a share risk inside China, not yet visible in results. |
| 🟢 oversold | KLAC | Semis | 181.56 | 41.4 | 0.6 | -4.9% | -3.4% | 75.4 | EXPENSIVE -50% (LOW) | 91.25 | +20% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +14%/yr over 5 yrs; analysts see revenue +34% next year; research 2026-10-13: Process-control leader riding AI and advanced-packaging demand (June-quarter revenue ~$3.66B, +15% y/y; guide ~$4.0B). Gains from the shift; no new untapped market of its own. |
| 🟢 oversold | PANW | AI-software | 376.62 | 46.6 | 9.0 | -4.0% | +0.8% | 90.5 | EXPENSIVE -50% (LOW) | 188.03 | +10% | INNOVATING | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year |
| 🟢 oversold | JNJ | Other | 249.05 | 35.0 | 18.7 | -5.2% | -6.1% | 49.6 | EXPENSIVE -34% (HIGH) | 166.49 | +11% | STABLE | steady | disruption: R&D 16% of revenue |
| 🟢 oversold | BHP | Other | 83.07 | 38.0 | 8.2 | -3.0% | -6.5% | 56.7 | EXPENSIVE -25% (HIGH) | 62.0 | +15% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | FCEL | Battery/H2 | 14.79 | 40.6 | 7.9 | -14.3% | -17.6% | 122.4 | DEEP VALUE +100% (LOW) | 29.61 | +49% | AT RISK | **VALUE TRAP?** preprofit: far from its own history: the market has re-rated it, find out why; analysts agree | disruption: analysts expect revenue -7% next year; R&D 22% of revenue |
| 🟡 dip | VRTX | Other | 490.34 | 36.1 | 33.8 | -4.0% | -6.0% | 31.7 | FAIR -2% (HIGH) | 486.0 | +22% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -47% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -36% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +8% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #231 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 2/12 #141 | N/A | INNOVATING |
| Drones | UMAC | C 3/12 #109 | N/A | N/A |
| Drones | UAVS | C 3/12 #112 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #176 | DEEP VALUE +70% (LOW) | DISRUPTOR |
| Drones | DPRO | C 3/12 #121 | FAIR -2% (LOW) | AT RISK |
| Drones | KTOS | C 0/12 #196 | RICH -24% (LOW) | INNOVATING |
| Drones | AVAV | C 0/12 #210 | DEEP VALUE +42% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #236 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 2/12 #130 | FAIR -9% (HIGH) | STABLE |
| Raw materials | SCCO | B 9/12 #44 | EXPENSIVE -46% (HIGH) | STABLE |
| Raw materials | BHP | C 5/12 #92 | EXPENSIVE -25% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #168 | EXPENSIVE -37% (LOW) | STABLE |
| Raw materials | FCX | C 5/12 #89 | EXPENSIVE -41% (HIGH) | STABLE |
| Growth opportunities | NBIS | C 4/12 #100 | EXPENSIVE -50% (LOW) | DISRUPTOR |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 437.7 | 64.0 |  |
| VLO | 146.0 | 74.9 |  |
| DELL | 254.3 | 46.4 |  |
| COP | 59.1 | 70.5 |  |
| CRWD | 90.7 | 51.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| WULF | 3.5 | 29.7 | SPEC |
| OKLO | -79.0 | 30.3 | SPEC |
| APLD | -31.6 | 31.8 | SPEC |
| DKNG | -26.6 | 37.6 |  |
| POET | -14.5 | 29.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._