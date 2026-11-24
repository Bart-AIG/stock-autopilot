# Strategy report - INTRADAY  (2026-11-24 20:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAR | A+ | 12/12 | #4 | 21 EMA pullback | Other |  |  |  | 413.94 | 48.0 | 413.94 | 397.2 | 429.18 | -4.0% |
| MO | A+ | 11/12 | #16 | 21 EMA pullback | Other |  |  |  | 74.48 | 46.5 | 74.48 | 71.43 | 78.9 | -4.1% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): MPC (C 5/12), VLO (C 4/12), PSX (C 5/12), MDT (B 10/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | LLY | A+ | 12/12 | +25.4% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | WBD | A+ | 12/12 | +25.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | DLTR | A+ | 12/12 | +22.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MAR | A+ | 12/12 | +21.9% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | ABBV | A+ | 12/12 | +20.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | COST | A+ | 12/12 | +20.4% | -2.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CME | A+ | 12/12 | +17.2% | -4.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | TGT | A+ | 12/12 | +13.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WMT | A+ | 11/12 | +32.7% | -1.9% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PG | A+ | 11/12 | +25.2% | -0.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | DIS | A+ | 11/12 | +17.8% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | TMO | A+ | 11/12 | +16.5% | -3.5% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ASND | A+ | 11/12 | +15.3% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 14 | KO | A+ | 11/12 | +15.0% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 15 | V | A+ | 11/12 | +14.7% | -4.9% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MO | A+ | 11/12 | +14.3% | -5.6% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AMGN | A+ | 11/12 | +13.7% | -1.4% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | VRTX | A+ | 11/12 | +9.0% | 0.0% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | BLK | A+ | 11/12 | +3.7% | -7.0% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MRNA | A | 10/12 | +57.9% | -15.8% | — | — | MA STACK, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | GILD | A | 10/12 | +27.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 22 | REGN | A | 10/12 | +26.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | AAPL | A | 10/12 | +18.8% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 24 | SPOT | B | 10/12 | +16.0% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | MA | B | 10/12 | +14.4% | -4.0% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 648.3 | 53.3 | T |
| 2 **TOP** | SNDK | 565.0 | 28.1 | F |
| 3 **TOP** | LITE | 321.7 | 35.8 | F |
| 4 **TOP** | MU | 300.7 | 37.2 | F |
| 5 **TOP** | DELL | 187.7 | 36.4 | F |
| 6 **TOP** | MRVL | 171.6 | 35.4 | F |
| 7 **TOP** | ILMN | 169.1 | 40.7 | T |
| 8 **TOP** | VLO | 145.1 | 31.2 | T |
| 9 **TOP** | MPC | 133.0 | 30.7 | T |
| 10 **TOP** | INTC | 127.2 | 36.3 | F |
| 11 **TOP** | VIAV | 121.5 | 40.2 | F |
| 12 **TOP** | PSX | 109.8 | 33.1 | T |
| 13 **TOP** | AMD | 104.3 | 38.6 | F |
| 14 **TOP** | AAOI | 98.5 | 32.7 | F |
| 15 **TOP** | CRWD | 95.4 | 38.3 | T |
| 16 **TOP** | SOXL | 93.7 | 33.1 | F |
| 17 **TOP** | NUE | 86.1 | 42.8 | T |
| 18 **TOP** | PANW | 75.3 | 50.4 | T |
| 19 **TOP** | DDOG | 72.3 | 32.3 | F |
| 20 **TOP** | COP | 71.3 | 44.8 | T |
| 21 **TOP** | TXN | 68.3 | 39.9 | F |
| 22  | MTSI | 67.7 | 41.6 | F |
| 23  | RBRK | 67.2 | 47.7 | T |
| 24  | MRK | 66.0 | 48.1 | T |
| 25  | AMAT | 64.9 | 39.1 | F |
| 26  | ROKU | 64.7 | 61.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AMZN | Other | 251.25 | 45.9 | 37.4 | -2.5% | -1.5% | 10.6 | DEEP VALUE +100% (LOW) | 510.78 | +29% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MDT | Other | 96.14 | 43.0 | 9.4 | -4.5% | +1.4% | 1.9 | DEEP VALUE +30% (MED) | 128.9 | -0% | STABLE | steady: analysts disagree |
| 🟢 oversold | PSX | Energy | 237.02 | 33.1 | 1.5 | -7.7% | -11.2% | 109.8 | RICH -23% (LOW) | 182.77 | +26% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟡 dip | EOG | Energy | 147.79 | 43.4 | 52.3 | -3.4% | -1.7% | 53.3 | UNDERVALUED +15% (HIGH) | 167.77 | +14% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟡 dip | MSFT | Other | 493.19 | 39.4 | 48.2 | -5.0% | -5.1% | 0.2 | FAIR -10% (MED) | 444.23 | +28% | INNOVATING (quant STABLE) [research: innovating] | growth: its multiples disagree with each other | disruption: revenue +16%/yr over 3 yrs; research 2026-11-17: AI is a demand driver, not a substitute: Azure +43% in FY26 Q4 and past $100B/yr, M365 Copilot at 30M paid seats; the risk is value shifting from per-seat Copilot to consumption and rival agent tools (Salesforce Agentforce, ServiceNow), plus margin pressure from >$50B capex. |
| 🟡 dip | COP | Energy | 135.25 | 44.8 | 59.5 | -3.3% | -1.4% | 71.3 | FAIR -4% (HIGH) | 126.45 | +17% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |
| 🟡 dip | GM | Other | 81.73 | 45.5 | 61.6 | -4.7% | -1.5% | 9.0 | FAIR +4% (MED) | 84.74 | +21% | STABLE [research: neutral] | cyclical: TROUGH-CYCLE margins (8% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends; research 2026-11-23: Software/autonomy race is the risk: Tesla's software lead and Chinese automakers' 2-3 year development cycles; GM's 2026-10-21 'GM Forward' plan (central computer, eyes-off highway driving from the 2028 Escalade IQ, AI to halve development time) is a catch-up, not a new market. No lost share in its core US trucks/SUVs visible yet; Chinese rivals are largely kept out of the US by tariffs. |
| 🟡 dip | SNOW | AI-software | 272.6 | 40.9 | 65.4 | -5.6% | -13.9% | 26.2 | DEEP VALUE +26% (LOW) | 341.13 | +62% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | PLTR | AI-software | 161.03 | 43.1 | 75.1 | -4.1% | -11.9% | 6.6 | EXPENSIVE -50% (LOW) | 79.68 | +55% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +91% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟡 dip | NET | AI-software | 287.88 | 46.6 | 46.3 | -0.8% | -9.4% | 49.5 | EXPENSIVE -43% (LOW) | 166.27 | +20% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +37% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟡 dip | RBRK | AI-infra | 110.23 | 47.7 | 45.1 | -2.8% | -4.9% | 67.2 | RICH -25% (LOW) | 85.58 | +0% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +30%/yr over 3 yrs; analysts see revenue +28% next year; research 2026-10-23: Cyber-resilience leader extending into AI-agent governance and recovery (Rubrik Agent Cloud, Bedrock/Copilot/Gemini integrations); cloud ARR +57%; rivals CrowdStrike and Palo Alto compete in AI security. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +19% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +120% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -46% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -36% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +65% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +55% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | yes | EXPENSIVE -40% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | yes | EXPENSIVE -31% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -43% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -28% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LLY | 20.7 | 60.0 |  |
| DLTR | 22.7 | 68.0 |  |
| MAR | 33.4 | 54.7 |  |
| ABBV | 21.4 | 63.9 |  |
| COST | 11.8 | 63.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -39.8 | 31.0 | SPEC |
| QBTS | -43.5 | 29.2 | SPEC |
| ASTS | -23.2 | 31.1 | SPEC |
| UEC | -31.7 | 33.5 | SPEC |
| LEU | -59.3 | 35.5 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._