# Strategy report - INTRADAY  (2026-10-14 19:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | A+ | 11/12 | #19 | RSI2 dip | AI-software |  |  |  | 249.35 | 9.1 | 249.35 | 230.87 | 277.07 | -7.4% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 4/12), LRCX (C 3/12), ARM (C 6/12), SMCI (C 7/12), NBIS (C 4/12), MU (C 7/12), DELL (B 9/12), QQQI (C 4/12), QQQ (B 10/12), VIAV (C 7/12), LITE (B 8/12), SPY (C 7/12), AFRM (C 5/12), ETN (C 5/12), MRVL (B 10/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +254.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +54.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +50.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +44.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | COP | A+ | 12/12 | +23.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +22.1% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | XOM | A+ | 12/12 | +19.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | CVX | A+ | 12/12 | +18.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WBD | A+ | 12/12 | +16.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | DVN | A+ | 12/12 | +13.9% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | OXY | A+ | 12/12 | +12.4% | -7.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | ABBV | A+ | 12/12 | +9.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | EOG | A+ | 12/12 | +9.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | PM | A+ | 12/12 | +5.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | ADI | A+ | 12/12 | +4.0% | -9.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | AAPL | A+ | 12/12 | +0.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +47.0% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +30.7% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | CRWD | A+ | 11/12 | +20.2% | -10.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | PFE | A+ | 11/12 | +14.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | MRK | A+ | 11/12 | +13.2% | -5.8% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | EMR | A+ | 11/12 | +13.0% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | AMGN | A+ | 11/12 | +12.7% | -3.8% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | AMD | B | 11/12 | +11.4% | -12.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | KO | B | 11/12 | +5.8% | -0.3% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 523.9 | 68.9 | T |
| 2 **TOP** | MU | 487.7 | 37.0 | T |
| 3 **TOP** | LITE | 412.2 | 42.6 | T |
| 4 **TOP** | WDC | 337.2 | 32.1 | F |
| 5 **TOP** | DELL | 327.3 | 41.2 | T |
| 6 **TOP** | INTC | 303.6 | 37.9 | T |
| 7 **TOP** | AAOI | 253.7 | 37.3 | F |
| 8 **TOP** | MRVL | 224.9 | 46.2 | T |
| 9 **TOP** | AMD | 211.2 | 46.1 | T |
| 10 **TOP** | VIAV | 181.1 | 43.3 | T |
| 11 **TOP** | COHR | 158.8 | 39.1 | F |
| 12 **TOP** | AMAT | 152.8 | 36.6 | T |
| 13 **TOP** | VLO | 144.4 | 76.4 | T |
| 14 **TOP** | NBIS | 134.7 | 34.8 | T |
| 15 **TOP** | LRCX | 133.8 | 37.2 | T |
| 16 **TOP** | FCEL | 122.4 | 38.4 | F |
| 17 **TOP** | MPC | 119.9 | 79.1 | T |
| 18 **TOP** | CRWD | 115.9 | 49.0 | T |
| 19 **TOP** | UMAC | 115.8 | 31.7 | F |
| 20 **TOP** | PSX | 96.6 | 78.4 | T |
| 21 **TOP** | PANW | 90.5 | 46.4 | T |
| 22 **TOP** | CAT | 81.7 | 33.4 | F |
| 23  | MTSI | 81.7 | 47.2 | T |
| 24  | NUE | 80.1 | 55.4 | T |
| 25  | SCCO | 79.5 | 46.7 | T |
| 26  | TGT | 76.4 | 47.2 | T |
| 27  | KLAC | 75.4 | 39.2 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 922.13 | 37.0 | 2.1 | -11.5% | -6.2% | 487.7 | EXPENSIVE -50% (LOW) | 472.12 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | QQQI | Other | 54.83 | 43.0 | 2.7 | -1.5% | -0.4% | 0.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | QQQ | Index-ETF | 727.48 | 43.8 | 2.9 | -2.0% | +0.1% | 20.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | NVDA | Semis | 220.16 | 42.9 | 10.3 | -3.7% | -1.4% | 18.6 | FAIR -1% (MED) | 223.03 | +45% | DISRUPTOR | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year |
| 🟡 dip | AMZN | Other | 253.03 | 48.3 | 14.8 | -0.1% | -1.9% | 11.1 | DEEP VALUE +100% (LOW) | 514.02 | +26% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | GOOGL | Other | 347.02 | 50.6 | 15.6 | +0.1% | +0.5% | 45.1 | RICH -24% (LOW) | 268.15 | +20% | DISRUPTOR | growth: business changed (margin 73% vs 33% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other | disruption: revenue +13%/yr over 3 yrs; analysts see revenue +24% next year |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NBIS | Other | 184.15 | 34.8 | 1.6 | -19.2% | -17.7% | 134.7 | EXPENSIVE -50% (LOW) | 93.15 | +76% | DISRUPTOR | growth: business changed (margin 74% vs 23% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +240%/yr over 3 yrs; analysts see revenue +531% next year |
| 🟢 oversold | ARM | Semis | 238.06 | 35.9 | 0.6 | -17.9% | -11.7% | 58.7 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | AMAT | Semis | 447.83 | 36.6 | 0.3 | -8.9% | -8.0% | 152.8 | EXPENSIVE -50% (LOW) | 227.72 | +42% | INNOVATING [research: neutral] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year; research 2026-10-13: Broadest equipment maker, gains from AI chip demand, but Mizuho expects it to lag the WFE market as Chinese rivals (AMEC, Naura) win domestic share in core tools; date of that note is unclear, so evidence is thin. |
| 🟢 oversold | LRCX | Semis | 286.7 | 37.2 | 0.3 | -9.0% | -7.7% | 133.8 | EXPENSIVE -50% (LOW) | 146.66 | +24% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +51% next year; gross margin up 4 pts (50%); research 2026-10-13: Etch/deposition leader benefiting from AI and memory tightness (RBC, Apr 2026); China exposure falling as global spend rises. Chinese etch makers (AMEC, Naura) are a share risk inside China, not yet visible in results. |
| 🟢 oversold | VIAV | Photonics | 38.41 | 43.3 | 4.6 | -7.0% | -2.6% | 181.1 | EXPENSIVE -50% (LOW) | 20.56 | +52% | INNOVATING | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟢 oversold | NET | AI-software | 324.5 | 44.9 | 8.1 | -6.7% | +1.7% | 49.3 | EXPENSIVE -50% (LOW) | 162.15 | +8% | DISRUPTOR | preprofit: far from its own history: the market has re-rated it, find out why | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year |
| 🟢 oversold | PANW | AI-software | 375.88 | 46.4 | 8.7 | -4.2% | +0.6% | 90.5 | EXPENSIVE -50% (LOW) | 188.03 | +10% | INNOVATING | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year |
| 🟢 oversold | SPY | Index-ETF | 767.46 | 47.6 | 6.1 | -0.4% | -0.1% | 15.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | BHP | Other | 82.89 | 37.5 | 7.5 | -3.2% | -6.7% | 56.7 | EXPENSIVE -25% (HIGH) | 62.0 | +15% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | ETN | Other | 406.74 | 40.6 | 6.6 | -5.7% | -4.5% | 7.5 | EXPENSIVE -34% (MED) | 275.86 | +20% | INNOVATING | steady: analysts disagree | disruption: analysts see revenue +20% next year; gross margin up 4 pts (38%) |

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

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 437.7 | 68.9 |  |
| COP | 59.1 | 71.0 |  |
| TMO | 22.3 | 60.9 |  |
| CVX | 43.3 | 71.1 |  |
| DVN | 54.6 | 60.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| WULF | 3.5 | 28.0 | SPEC |
| OKLO | -79.0 | 28.4 | SPEC |
| DKNG | -26.6 | 34.3 |  |
| SMR | -81.3 | 25.5 | SPEC |
| POET | -14.5 | 27.9 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._