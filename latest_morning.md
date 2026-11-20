# Strategy report - MORNING  (2026-11-20 15:14 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAR | A+ | 12/12 | #3 | 21 EMA pullback | Other |  |  |  | 413.3 | 12.3 | 413.3 | 397.52 | 429.18 | -3.8% |
| MO | A+ | 12/12 | #6 | 21 EMA pullback | Other |  |  |  | 75.15 | 29.3 | 75.15 | 72.12 | 78.9 | -4.0% |
| LLY | A+ | 12/12 | #7 | 21 EMA pullback | Other |  |  |  | 1362.93 | 31.8 | 1362.93 | 1285.66 | 1443.5 | -5.7% |
| TMO | A+ | 11/12 | #14 | 21 EMA pullback | Other |  |  |  | 687.8 | 26.6 | 687.8 | 655.74 | 721.63 | -4.7% |
| V | A+ | 11/12 | #15 | 21 EMA pullback | Other |  |  |  | 407.0 | 37.9 | 407.0 | 388.96 | 434.04 | -4.4% |
| MA | A+ | 11/12 | #16 | 21 EMA pullback | Other |  |  |  | 635.35 | 45.2 | 635.35 | 604.92 | 672.68 | -4.8% |
| ASND | A+ | 11/12 | #19 | RSI2 dip | Other |  |  |  | 255.19 | 4.7 | 255.19 | 243.05 | 273.41 | -4.8% |
| AMGN | A+ | 11/12 | #20 | 21 EMA pullback | Other |  |  |  | 443.48 | 40.6 | 443.48 | 425.6 | 470.29 | -4.0% |
| AAPL | A | 10/12 | #23 | 21 EMA pullback | Other |  |  |  | 350.57 | 45.0 | 350.57 | 335.77 | 356.27 | -4.2% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): DE (C 4/12), PYPL (C 5/12), BLK (B 10/12), TEM (C 5/12), NUE (C 5/12), MPC (B 7/12), TXN (B 7/12), GM (C 4/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +24.4% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | PG | A+ | 12/12 | +22.4% | -1.4% | FAIR -5% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | MAR | A+ | 12/12 | +20.7% | -3.7% | EXPENSIVE -29% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | COST | A+ | 12/12 | +19.9% | -0.6% | EXPENSIVE -28% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CME | A+ | 12/12 | +17.3% | -4.7% | FAIR +5% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | MO | A+ | 12/12 | +15.7% | -4.8% | RICH -14% (HIGH) | AT RISK [research: threatened] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | LLY | A+ | 12/12 | +15.2% | -5.6% | RICH -13% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | ABBV | A+ | 12/12 | +14.7% | -2.5% | EXPENSIVE -41% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | DLTR | A+ | 12/12 | +9.1% | -4.0% | DEEP VALUE +33% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WMT | A+ | 11/12 | +27.3% | -3.7% | EXPENSIVE -45% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | REGN | A+ | 11/12 | +19.3% | -3.5% | FAIR -10% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 12 | MDT | A+ | 11/12 | +16.2% | -2.8% | FAIR +6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | DIS | A+ | 11/12 | +15.4% | -1.1% | UNDERVALUED +14% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | TMO | A+ | 11/12 | +15.3% | -4.7% | RICH -18% (HIGH) | AT RISK | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | V | A+ | 11/12 | +12.4% | -6.8% | FAIR -9% (HIGH) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MA | A+ | 11/12 | +11.8% | -5.5% | FAIR +5% (HIGH) | INNOVATING (quant STABLE) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 17 | KO | A+ | 11/12 | +11.4% | -2.5% | FAIR -5% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 18 | LIN | A+ | 11/12 | +10.9% | -5.9% | RICH -23% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | ASND | A+ | 11/12 | +7.2% | -7.9% | N/A | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | AMGN | A+ | 11/12 | +5.8% | -7.3% | EXPENSIVE -26% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | TGT | A+ | 11/12 | +5.6% | -0.3% | FAIR -8% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | GILD | A | 10/12 | +21.2% | -3.1% | EXPENSIVE -32% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 23 | AAPL | A | 10/12 | +18.9% | -1.6% | EXPENSIVE -31% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 24 | SPOT | B | 10/12 | +16.6% | -5.2% | UNDERVALUED +16% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | ROKU | B | 10/12 | +12.3% | -1.4% | DEEP VALUE +100% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 218)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 823.3 | 27.8 | F |
| 2 **TOP** | MRNA | 794.2 | 45.8 | T |
| 3 **TOP** | LITE | 422.1 | 32.9 | F |
| 4 **TOP** | MU | 351.7 | 33.4 | F |
| 5 **TOP** | DELL | 225.2 | 30.9 | F |
| 6 **TOP** | MRVL | 190.5 | 30.4 | F |
| 7 **TOP** | VLO | 177.0 | 35.6 | T |
| 8 **TOP** | VIAV | 165.5 | 40.6 | F |
| 9 **TOP** | MPC | 155.9 | 33.3 | T |
| 10 **TOP** | SOXL | 148.7 | 31.9 | F |
| 11 **TOP** | INTC | 143.9 | 32.1 | F |
| 12 **TOP** | AMD | 132.2 | 43.4 | T |
| 13 **TOP** | AAOI | 131.5 | 28.3 | F |
| 14 **TOP** | PSX | 125.6 | 36.9 | T |
| 15 **TOP** | COHR | 96.6 | 44.1 | F |
| 16 **TOP** | MTSI | 95.9 | 40.8 | F |
| 17 **TOP** | CRWD | 90.0 | 48.2 | T |
| 18 **TOP** | NUE | 88.3 | 38.7 | T |
| 19 **TOP** | AMAT | 80.9 | 34.6 | F |
| 20 **TOP** | LRCX | 79.8 | 33.7 | F |
| 21 **TOP** | DDOG | 74.8 | 27.0 | F |
| 22  | MRK | 71.1 | 38.7 | T |
| 23  | COP | 68.6 | 45.8 | T |
| 24  | FCX | 66.8 | 23.0 | F |
| 25  | ADI | 64.8 | 40.7 | F |
| 26  | NBIS | 64.5 | 31.1 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SHOP | Other | 133.5 | 34.5 | 23.9 | -11.2% | -13.0% | 7.2 | UNDERVALUED +24% (MED) | 164.49 | +35% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +29% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟢 oversold | GM | Other | 81.7 | 43.6 | 5.8 | -4.5% | -1.8% | 14.2 | FAIR +4% (MED) | 84.74 | +21% | STABLE | cyclical: TROUGH-CYCLE margins (8% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |
| 🟢 oversold | MPC | Energy | 364.63 | 33.3 | 2.6 | -10.4% | -13.7% | 155.9 | EXPENSIVE -32% (LOW) | 251.25 | +24% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| 🟢 oversold | SNOW | AI-software | 265.63 | 34.9 | 14.6 | -10.2% | -16.7% | 30.4 | DEEP VALUE +27% (LOW) | 341.03 | +64% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | BLK | Other | 1135.72 | 44.2 | 1.5 | -3.6% | +1.3% | 1.7 | RICH -18% (MED) | 933.28 | +18% | INNOVATING | steady: its multiples disagree with each other | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +22% next year |
| 🟢 oversold | DE | Other | 618.62 | 34.3 | 0.4 | -6.4% | -6.9% | 38.4 | EXPENSIVE -40% (HIGH) | 368.13 | +20% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%); research 2026-11-16: Deere is the one driving ag automation (See & Spray Gen 2 consolidated and expanded to ~2x crops for MY2027, autonomy-ready tillage, goal of an autonomy kit on every large tractor, full autonomy for corn/soy by 2030); tech options support margins while base equipment volume is cyclical-down. No rival shown taking share. |
| 🟢 oversold | NUE | Other | 243.56 | 38.7 | 2.1 | -6.0% | -4.2% | 88.3 | EXPENSIVE -28% (MED) | 174.55 | +24% | STABLE | cyclical: analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | TXN | Semis | 281.83 | 43.3 | 4.0 | -5.8% | -1.7% | 57.4 | EXPENSIVE -29% (HIGH) | 200.66 | +19% | STABLE [research: neutral] | cyclical | disruption: analysts see revenue +27% next year; cyclical: judged on 5-yr trends; research 2026-11-06: Analog leader with a 300mm-fab cost edge; main risk is subsidized Chinese mature-node analog makers (e.g. Will Semi, 3Peak) pressuring price in cost-sensitive segments, plus fab under-utilization. Share loss not clearly visible yet; sources disagree on China exposure. |
| 🟡 dip | EOG | Energy | 151.49 | 47.7 | 56.5 | -2.1% | +0.6% | 48.9 | UNDERVALUED +11% (HIGH) | 167.77 | +9% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟡 dip | COP | Energy | 136.78 | 45.8 | 59.3 | -3.3% | -0.5% | 68.6 | FAIR -7% (HIGH) | 126.45 | +14% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |

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

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #214 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #233 | N/A | INNOVATING |
| Drones | UMAC | C 1/12 #171 | N/A | N/A |
| Drones | UAVS | C 0/12 #234 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #218 | DEEP VALUE +100% (LOW) | DISRUPTOR |
| Drones | DPRO | C 0/12 #225 | N/A | AT RISK |
| Drones | KTOS | C 0/12 #210 | FAIR +8% (MED) | INNOVATING |
| Drones | AVAV | C 0/12 #199 | DEEP VALUE +88% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #235 | N/A | AT RISK |
| Raw materials | RIO | C 1/12 #152 | FAIR +10% (HIGH) | STABLE |
| Raw materials | SCCO | C 1/12 #160 | RICH -23% (MED) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #151 | FAIR -8% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #155 | FAIR -8% (MED) | STABLE |
| Raw materials | FCX | C 1/12 #163 | RICH -11% (MED) | STABLE |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| PG | 12.7 | 62.9 |  |
| MAR | 39.6 | 55.2 |  |
| COST | 14.3 | 70.5 |  |
| CME | 12.3 | 58.6 |  |
| MO | 29.8 | 48.6 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -44.3 | 26.7 | SPEC |
| QBTS | -50.4 | 26.5 | SPEC |
| ASTS | -33.2 | 30.6 | SPEC |
| UEC | -37.6 | 29.8 | SPEC |
| APLD | -17.3 | 33.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._