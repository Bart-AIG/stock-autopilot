# Strategy report - INTRADAY  (2026-10-15 16:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADI | A+ | 12/12 | #15 | 21 EMA pullback | Semis |  |  |  | 400.35 | 19.4 | 400.35 | 383.04 | 420.55 | -4.3% |
| CRWD | A+ | 11/12 | #20 | RSI2 dip | AI-software |  |  |  | 243.62 | 5.6 | 243.62 | 225.41 | 270.93 | -7.5% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): SMCI (B 7/12), NBIS (C 2/12), DELL (B 8/12), QQQI (C 3/12), QLD (C 7/12), QQQ (C 7/12), LITE (C 7/12), MRVL (C 7/12), ETN (C 1/12), NET (C 6/12), CSCO (C 5/12), MU (C 7/12), INTC (C 4/12), BHP (C 5/12), PANW (C 7/12)

## Quality ranking — top 25 of 237 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +281.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +48.3% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +40.3% | -3.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +37.7% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | TMO | A+ | 12/12 | +26.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | COP | A+ | 12/12 | +20.2% | -0.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | XOM | A+ | 12/12 | +14.9% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +14.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | GILD | A+ | 12/12 | +14.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | MRK | A+ | 12/12 | +14.1% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | CVX | A+ | 12/12 | +14.1% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | KO | A+ | 12/12 | +9.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +9.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EOG | A+ | 12/12 | +5.9% | -0.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | ADI | A+ | 12/12 | +3.2% | -10.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PM | A+ | 12/12 | +1.1% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +46.5% | -4.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +33.0% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | AMGN | A+ | 11/12 | +16.1% | -1.3% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | CRWD | A+ | 11/12 | +15.9% | -13.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | PFE | A+ | 11/12 | +14.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | ABNB | A+ | 11/12 | +14.4% | -9.5% | FAIR -2% (LOW) | AT RISK | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | EMR | A+ | 11/12 | +11.2% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | DVN | B | 11/12 | +9.0% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | V | B | 11/12 | +7.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 225)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 502.1 | 72.1 | T |
| 2 **TOP** | MU | 487.9 | 36.7 | T |
| 3 **TOP** | LITE | 397.1 | 39.5 | T |
| 4 **TOP** | DELL | 328.6 | 35.7 | T |
| 5 **TOP** | WDC | 302.3 | 29.4 | F |
| 6 **TOP** | INTC | 292.2 | 35.1 | T |
| 7 **TOP** | MRVL | 228.8 | 41.3 | T |
| 8 **TOP** | AAOI | 222.4 | 35.7 | F |
| 9 **TOP** | AMD | 212.9 | 42.0 | T |
| 10 **TOP** | VIAV | 178.5 | 38.8 | F |
| 11 **TOP** | COHR | 155.0 | 35.9 | F |
| 12 **TOP** | VLO | 152.0 | 67.2 | T |
| 13 **TOP** | AMAT | 146.4 | 32.8 | F |
| 14 **TOP** | FCEL | 131.4 | 37.5 | F |
| 15 **TOP** | MPC | 128.3 | 73.2 | T |
| 16 **TOP** | NBIS | 128.0 | 32.8 | T |
| 17 **TOP** | LRCX | 127.2 | 33.4 | F |
| 18 **TOP** | CRWD | 118.1 | 45.6 | T |
| 19 **TOP** | UMAC | 110.3 | 30.2 | F |
| 20 **TOP** | PSX | 102.0 | 72.3 | T |
| 21 **TOP** | PANW | 86.4 | 44.1 | T |
| 22 **TOP** | NUE | 82.8 | 53.5 | T |
| 23  | MTSI | 82.6 | 41.7 | F |
| 24  | CAT | 79.7 | 30.7 | F |
| 25  | MRK | 77.5 | 58.8 | T |
| 26  | TGT | 74.3 | 52.8 | T |
| 27  | SCCO | 74.3 | 48.5 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NVDA | Semis | 217.68 | 40.6 | 6.8 | -4.8% | -2.5% | 19.4 | FAIR +4% (MED) | 223.06 | +51% | DISRUPTOR | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year |
| 🟢 oversold | MU | Semis | 916.56 | 36.7 | 4.8 | -11.8% | -6.7% | 487.9 | EXPENSIVE -50% (LOW) | 439.48 | +71% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | MRVL | Semis | 237.71 | 41.3 | 4.1 | -9.9% | -1.2% | 228.8 | EXPENSIVE -50% (LOW) | 115.73 | +49% | DISRUPTOR | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| 🟢 oversold | QQQ | Index-ETF | 724.94 | 42.4 | 2.2 | -2.4% | -0.3% | 19.1 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | AMZN | Other | 253.8 | 49.0 | 15.7 | +0.2% | -1.4% | 7.3 | DEEP VALUE +100% (LOW) | 504.0 | +29% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NBIS | Other | 176.4 | 32.8 | 1.1 | -22.0% | -20.9% | 128.0 | EXPENSIVE -50% (LOW) | 83.77 | +96% | DISRUPTOR [research: disruptor] | growth: business changed (margin 74% vs 23% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +240%/yr over 3 yrs; analysts see revenue +531% next year; research 2026-10-14: GPU neocloud building a new AI-compute market: Q2 2026 revenue $582M (+454% y/y), ~$27B Meta contract, 2026 guide $3.0-3.4B; risks are hyperscaler competition, commoditization and $20-25B capex/leverage. |
| 🟢 oversold | ARM | Semis | 239.66 | 36.6 | 9.3 | -17.0% | -10.9% | 57.2 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | NET | AI-software | 311.12 | 40.3 | 4.3 | -10.3% | -2.6% | 44.8 | EXPENSIVE -50% (LOW) | 155.68 | +13% | DISRUPTOR | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year |
| 🟢 oversold | PANW | AI-software | 368.62 | 44.1 | 6.1 | -6.0% | -1.3% | 86.4 | EXPENSIVE -50% (LOW) | 184.65 | +12% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | SNOW | AI-software | 327.7 | 45.2 | 8.7 | -3.6% | -1.6% | 43.0 | FAIR +6% (LOW) | 341.13 | +36% | DISRUPTOR | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year |
| 🟢 oversold | BHP | Other | 82.63 | 36.8 | 5.9 | -3.3% | -6.9% | 54.7 | RICH -21% (HIGH) | 63.69 | +17% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | ETN | Other | 400.08 | 38.0 | 4.2 | -7.1% | -5.8% | 4.5 | EXPENSIVE -30% (MED) | 275.92 | +27% | INNOVATING | steady: analysts disagree | disruption: analysts see revenue +20% next year; gross margin up 4 pts (38%) |
| 🟢 oversold | FCX | Other | 69.48 | 43.1 | 7.8 | -3.2% | -3.5% | 52.0 | EXPENSIVE -38% (HIGH) | 41.2 | +12% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | CSCO | Other | 109.06 | 44.0 | 4.4 | -1.9% | -2.5% | 64.2 | EXPENSIVE -45% (MED) | 60.54 | +22% | INNOVATING | growth: analysts disagree | disruption: analysts see revenue +15% next year; R&D 15% of revenue |
| 🟡 dip | QCOM | Semis | 176.18 | 46.5 | 63.5 | -4.2% | +0.8% | 16.5 | FAIR -2% (HIGH) | 171.17 | +9% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | yes | EXPENSIVE -50% (LOW) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -47% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -34% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | UNDERVALUED +11% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 454.7 | 72.1 |  |
| MPC | 126.0 | 73.2 |  |
| VLO | 148.6 | 67.2 |  |
| PSX | 102.3 | 72.3 |  |
| TMO | 23.3 | 66.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| WULF | -0.5 | 26.8 | SPEC |
| MOD | 8.6 | 33.1 |  |
| OKLO | -79.5 | 28.7 | SPEC |
| QBTS | -62.2 | 25.7 | SPEC |
| APLD | -30.4 | 28.6 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._