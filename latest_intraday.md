# Strategy report - INTRADAY  (2026-11-20 18:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAR | A+ | 12/12 | #4 | RSI2 dip | Other |  |  |  | 409.28 | 8.2 | 409.28 | 393.35 | 429.18 | -3.9% |
| MO | A+ | 12/12 | #6 | 21 EMA pullback | Other |  |  |  | 75.48 | 40.3 | 75.48 | 72.42 | 78.9 | -4.1% |
| LLY | A+ | 12/12 | #8 | 21 EMA pullback | Other |  |  |  | 1353.61 | 10.7 | 1353.61 | 1276.95 | 1443.5 | -5.7% |
| V | A+ | 11/12 | #15 | 21 EMA pullback | Other |  |  |  | 405.86 | 32.0 | 405.86 | 387.96 | 432.71 | -4.4% |
| MA | A+ | 11/12 | #16 | 21 EMA pullback | Other |  |  |  | 630.81 | 29.4 | 630.81 | 600.88 | 672.68 | -4.7% |
| LIN | A+ | 11/12 | #17 | RSI2 dip | Other |  |  |  | 508.55 | 3.5 | 508.55 | 494.54 | 526.55 | -2.8% |
| ASND | A+ | 11/12 | #18 | RSI2 dip | Other |  |  |  | 252.92 | 3.7 | 252.92 | 240.74 | 271.19 | -4.8% |
| AMGN | A+ | 11/12 | #19 | RSI2 dip | Other |  |  |  | 439.09 | 4.3 | 439.09 | 421.57 | 465.38 | -4.0% |
| AAPL | A | 10/12 | #22 | RSI2 dip | Other |  |  |  | 345.88 | 4.6 | 345.88 | 331.18 | 356.27 | -4.3% |
| SPOT | A | 10/12 | #23 | 21 EMA pullback | Other |  |  |  | 589.79 | 37.2 | 589.79 | 551.65 | 627.66 | -6.5% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): BLK (B 9/12), PYPL (C 5/12), NUE (C 5/12), TXN (B 7/12), PM (C 5/12), MSFT (C 4/12), ABNB (B 9/12), PFE (B 8/12), PSX (C 5/12), EMR (B 8/12), UPS (B 7/12), AMD (C 5/12), LMT (B 8/12), SNOW (C 3/12), TMO (B 10/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +26.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | PG | A+ | 12/12 | +24.3% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COST | A+ | 12/12 | +23.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MAR | A+ | 12/12 | +22.0% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CME | A+ | 12/12 | +19.7% | -4.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | MO | A+ | 12/12 | +18.5% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | ABBV | A+ | 12/12 | +17.3% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | LLY | A+ | 12/12 | +16.8% | -6.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | DLTR | A+ | 12/12 | +10.0% | -5.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WMT | A+ | 11/12 | +30.2% | -3.3% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | REGN | A+ | 11/12 | +20.2% | -4.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 12 | MDT | A+ | 11/12 | +16.9% | -4.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | DIS | A+ | 11/12 | +15.6% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | KO | A+ | 11/12 | +14.4% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 15 | V | A+ | 11/12 | +14.4% | -7.0% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MA | A+ | 11/12 | +13.4% | -6.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 17 | LIN | A+ | 11/12 | +12.1% | -7.0% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | ASND | A+ | 11/12 | +8.9% | -8.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 19 | AMGN | A+ | 11/12 | +7.3% | -8.2% | EXPENSIVE -26% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | TGT | A+ | 11/12 | +6.5% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 21 | GILD | A | 10/12 | +23.1% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 22 | AAPL | A | 10/12 | +19.8% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 23 | SPOT | A | 10/12 | +17.9% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | TMO | B | 10/12 | +15.6% | -6.5% | RICH -18% (HIGH) | AT RISK | MA STACK, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | ROKU | B | 10/12 | +14.7% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 218)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 823.3 | 25.7 | F |
| 2 **TOP** | MRNA | 794.2 | 41.3 | T |
| 3 **TOP** | LITE | 422.1 | 30.6 | F |
| 4 **TOP** | MU | 351.7 | 29.8 | F |
| 5 **TOP** | DELL | 225.2 | 28.7 | F |
| 6 **TOP** | MRVL | 190.5 | 28.3 | F |
| 7 **TOP** | VLO | 177.0 | 35.1 | T |
| 8 **TOP** | VIAV | 165.5 | 36.4 | F |
| 9 **TOP** | MPC | 155.9 | 35.5 | T |
| 10 **TOP** | SOXL | 148.7 | 29.1 | F |
| 11 **TOP** | INTC | 143.9 | 29.0 | F |
| 12 **TOP** | AMD | 132.2 | 39.3 | T |
| 13 **TOP** | AAOI | 131.5 | 26.3 | F |
| 14 **TOP** | PSX | 125.6 | 36.4 | T |
| 15 **TOP** | COHR | 96.6 | 38.2 | F |
| 16 **TOP** | MTSI | 95.9 | 37.5 | F |
| 17 **TOP** | CRWD | 90.0 | 47.6 | T |
| 18 **TOP** | NUE | 88.3 | 36.2 | T |
| 19 **TOP** | AMAT | 80.9 | 31.4 | F |
| 20 **TOP** | LRCX | 79.8 | 30.8 | F |
| 21 **TOP** | DDOG | 74.8 | 26.7 | F |
| 22  | MRK | 71.1 | 35.4 | T |
| 23  | COP | 68.6 | 46.2 | T |
| 24  | FCX | 66.8 | 20.8 | F |
| 25  | ADI | 64.8 | 34.9 | F |
| 26  | NBIS | 64.5 | 29.1 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AMZN | Other | 250.38 | 44.3 | 16.4 | -2.8% | -1.9% | 18.2 | DEEP VALUE +100% (LOW) | 513.53 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SNOW | AI-software | 258.35 | 32.8 | 9.1 | -12.5% | -19.0% | 30.4 | DEEP VALUE +27% (LOW) | 341.03 | +64% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | MSFT | Other | 489.29 | 36.2 | 3.6 | -6.5% | -5.9% | 3.0 | RICH -12% (LOW) | 443.92 | +26% | INNOVATING (quant STABLE) [research: innovating] | growth: its multiples disagree with each other; analysts disagree | disruption: revenue +16%/yr over 3 yrs; research 2026-11-17: AI is a demand driver, not a substitute: Azure +43% in FY26 Q4 and past $100B/yr, M365 Copilot at 30M paid seats; the risk is value shifting from per-seat Copilot to consumption and rival agent tools (Salesforce Agentforce, ServiceNow), plus margin pressure from >$50B capex. |
| 🟢 oversold | PSX | Energy | 243.26 | 36.4 | 7.0 | -6.9% | -9.2% | 125.6 | EXPENSIVE -25% (LOW) | 182.77 | +23% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | AMD | Semis | 434.25 | 39.3 | 9.0 | -14.8% | -21.5% | 132.2 | EXPENSIVE -30% (LOW) | 326.66 | +38% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (25% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +51% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| 🟢 oversold | EMR | Other | 152.42 | 36.2 | 8.4 | -7.3% | -4.9% | 23.4 | RICH -20% (HIGH) | 125.85 | +11% | STABLE | cyclical | disruption: gross margin up 4 pts (53%); cyclical: judged on 5-yr trends |
| 🟢 oversold | BLK | Other | 1112.12 | 40.2 | 0.8 | -5.5% | -0.8% | 1.7 | RICH -18% (MED) | 933.28 | +18% | INNOVATING | steady: its multiples disagree with each other | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +22% next year |
| 🟢 oversold | PM | Other | 186.15 | 34.4 | 2.3 | -6.6% | -5.4% | 29.9 | EXPENSIVE -26% (HIGH) | 139.34 | +14% | INNOVATING (quant STABLE) [research: innovating] | steady | disruption: research 2026-11-09: Smoke-free (IQOS heated tobacco, ZYN pouches) was ~42-43% of net revenue in 2026 (41.5% FY2025) and IQOS overtook Marlboro; PMI is the one shifting the market, though US ZYN shipments fell 23.5% in Q1 2026. |
| 🟢 oversold | NUE | Other | 239.67 | 36.2 | 1.3 | -7.5% | -5.7% | 88.3 | EXPENSIVE -28% (MED) | 174.55 | +24% | STABLE | cyclical: analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | TXN | Semis | 268.55 | 37.8 | 1.7 | -10.1% | -6.3% | 57.4 | EXPENSIVE -29% (HIGH) | 200.66 | +19% | STABLE [research: neutral] | cyclical | disruption: analysts see revenue +27% next year; cyclical: judged on 5-yr trends; research 2026-11-06: Analog leader with a 300mm-fab cost edge; main risk is subsidized Chinese mature-node analog makers (e.g. Will Semi, 3Peak) pressuring price in cost-sensitive segments, plus fab under-utilization. Share loss not clearly visible yet; sources disagree on China exposure. |
| 🟢 oversold | AMGN | Other | 439.45 | 43.3 | 4.3 | -4.2% | +2.1% | 45.6 | EXPENSIVE -26% (HIGH) | 329.16 | -3% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin slipping 4 pts (71%); research 2026-11-19: Biosimilars are eroding Prolia (Q2 2026 -32%) and pricing hits Enbrel (-22% net price), a patent/pricing cliff rather than a technology making it obsolete; six growth drivers grew 26% (~70% of product sales), its own biosimilar portfolio grew 37% to $3B, and MariTide (GIPR/GLP-1) is in six Phase III studies, not yet a product. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +19% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +119% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -45% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -36% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +61% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -41% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -32% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -42% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -29% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| PG | 12.7 | 62.0 |  |
| COST | 14.3 | 71.9 |  |
| MAR | 39.6 | 52.1 |  |
| CME | 12.3 | 58.6 |  |
| MO | 29.8 | 49.9 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -44.3 | 25.3 | SPEC |
| ASTS | -33.2 | 27.7 | SPEC |
| APLD | -17.3 | 30.1 | SPEC |
| UEC | -37.6 | 27.5 | SPEC |
| RGTI | -54.9 | 28.2 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._