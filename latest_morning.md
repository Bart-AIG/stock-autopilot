# Strategy report - MORNING  (2026-11-27 15:14 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ABBV | A+ | 12/12 | #5 | 21 EMA pullback | Other |  |  |  | 290.69 | 33.1 | 290.69 | 278.77 | 300.28 | -4.1% |
| MO | A+ | 11/12 | #15 | 21 EMA pullback | Other |  |  |  | 75.44 | 48.7 | 75.44 | 73.03 | 78.9 | -3.2% |
| MRNA | A | 10/12 | #20 | 21 EMA pullback | Other |  |  |  | 216.44 | 42.3 | 216.44 | 186.93 | 260.71 | -13.6% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MAR | A+ | 12/12 | +25.0% | -3.0% | EXPENSIVE -30% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | WBD | A+ | 12/12 | +24.9% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | LLY | A+ | 12/12 | +24.5% | -3.9% | RICH -14% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | DLTR | A+ | 12/12 | +22.9% | -3.4% | DEEP VALUE +34% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | ABBV | A+ | 12/12 | +20.2% | -3.2% | EXPENSIVE -41% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | V | A+ | 12/12 | +18.7% | -1.8% | RICH -14% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | MA | A+ | 12/12 | +18.0% | -1.2% | FAIR +0% (HIGH) | INNOVATING (quant STABLE) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | AMGN | A+ | 12/12 | +14.9% | -1.9% | EXPENSIVE -30% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | LIN | A+ | 12/12 | +14.5% | -3.2% | EXPENSIVE -25% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WMT | A+ | 11/12 | +34.4% | -1.7% | EXPENSIVE -46% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | PG | A+ | 11/12 | +26.3% | -0.4% | FAIR -6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | DIS | A+ | 11/12 | +23.7% | 0.0% | FAIR +9% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | COST | A+ | 11/12 | +22.2% | -1.7% | EXPENSIVE -27% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | ASND | A+ | 11/12 | +17.9% | -0.3% | N/A | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 15 | MO | A+ | 11/12 | +16.3% | -4.4% | RICH -15% (HIGH) | AT RISK [research: threatened] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | CME | A+ | 11/12 | +15.3% | -4.6% | FAIR +4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | KO | A+ | 11/12 | +14.9% | -2.2% | FAIR -6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 18 | EOG | A+ | 11/12 | +11.5% | -9.0% | UNDERVALUED +11% (HIGH) | STABLE [research: neutral] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | BLK | A+ | 11/12 | +6.3% | -5.1% | RICH -20% (MED) | INNOVATING | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MRNA | A | 10/12 | +63.2% | -19.5% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | REGN | A | 10/12 | +29.6% | -0.9% | RICH -14% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | GILD | A | 10/12 | +26.3% | -2.0% | EXPENSIVE -34% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 23 | SPOT | A | 10/12 | +19.7% | -1.2% | UNDERVALUED +10% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | DG | B | 10/12 | +19.3% | -11.2% | UNDERVALUED +22% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | AAPL | B | 10/12 | +17.8% | -0.0% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 744.9 | 49.5 | T |
| 2 **TOP** | SNDK | 700.4 | 30.7 | F |
| 3 **TOP** | LITE | 360.7 | 37.2 | F |
| 4 **TOP** | MU | 343.1 | 36.8 | F |
| 5 **TOP** | DELL | 199.5 | 39.3 | F |
| 6 **TOP** | ILMN | 195.3 | 39.0 | T |
| 7 **TOP** | MRVL | 184.5 | 36.8 | F |
| 8 **TOP** | VIAV | 146.1 | 41.5 | F |
| 9 **TOP** | INTC | 130.0 | 36.5 | F |
| 10 **TOP** | VLO | 129.4 | 34.4 | T |
| 11 **TOP** | MPC | 129.3 | 35.8 | T |
| 12 **TOP** | SOXL | 128.6 | 33.3 | F |
| 13 **TOP** | AMD | 124.2 | 37.5 | F |
| 14 **TOP** | AAOI | 123.0 | 33.5 | F |
| 15 **TOP** | PSX | 104.8 | 39.7 | T |
| 16 **TOP** | CRWD | 95.0 | 39.4 | T |
| 17 **TOP** | TXN | 85.6 | 44.6 | T |
| 18 **TOP** | AMAT | 82.7 | 37.2 | F |
| 19 **TOP** | ADI | 78.9 | 39.7 | F |
| 20 **TOP** | NUE | 78.8 | 52.8 | T |
| 21 **TOP** | RBRK | 78.7 | 47.2 | T |
| 22  | COHR | 78.5 | 47.6 | F |
| 23  | PANW | 78.2 | 50.4 | T |
| 24  | DDOG | 77.0 | 33.0 | F |
| 25  | MTSI | 76.4 | 41.6 | F |
| 26  | COP | 71.7 | 50.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AMZN | Other | 249.42 | 45.6 | 52.1 | -3.1% | -2.2% | 11.1 | DEEP VALUE +100% (LOW) | 501.47 | +31% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | EOG | Energy | 150.66 | 48.6 | 86.2 | -0.7% | +0.1% | 52.0 | UNDERVALUED +11% (HIGH) | 167.77 | +9% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟡 dip | COP | Energy | 138.28 | 50.2 | 87.7 | -0.2% | +0.7% | 71.7 | FAIR -8% (HIGH) | 126.45 | +12% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |
| 🟡 dip | USB | Other | 59.36 | 51.5 | 91.3 | -0.1% | +0.9% | 26.1 | FAIR +4% (HIGH) | 61.63 | +15% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | QCOM | Semis | 173.04 | 52.6 | 89.1 | +3.7% | -1.6% | 1.1 | FAIR -4% (HIGH) | 166.94 | +6% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: R&D 24% of revenue; cyclical: judged on 5-yr trends; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | PSX | Energy | 242.87 | 39.7 | 84.1 | -4.2% | -8.6% | 104.8 | RICH -24% (LOW) | 182.78 | +24% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟡 dip | SNOW | AI-software | 269.35 | 39.9 | 55.4 | -4.5% | -14.2% | 27.3 | DEEP VALUE +27% (LOW) | 341.13 | +64% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | NET | AI-software | 285.8 | 46.2 | 49.9 | -0.5% | -9.5% | 42.3 | EXPENSIVE -42% (LOW) | 166.27 | +22% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +37% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟡 dip | MRK | Other | 140.93 | 47.1 | 73.0 | -2.0% | -2.7% | 61.9 | EXPENSIVE -39% (LOW) | 86.52 | +17% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟡 dip | RBRK | AI-infra | 109.32 | 47.2 | 48.7 | -1.3% | -5.8% | 78.7 | RICH -22% (LOW) | 85.38 | +6% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +30%/yr over 3 yrs; analysts see revenue +28% next year; research 2026-10-23: Cyber-resilience leader extending into AI-agent governance and recovery (Rubrik Agent Cloud, Bedrock/Copilot/Gemini integrations); cloud ARR +57%; rivals CrowdStrike and Palo Alto compete in AI security. |
| 🟡 dip | PLTR | AI-software | 167.62 | 48.3 | 90.6 | +1.7% | -8.1% | 3.8 | EXPENSIVE -50% (LOW) | 84.2 | +46% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +91% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +19% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +120% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -42% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +77% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -37% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +65% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +60% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | yes | EXPENSIVE -40% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | yes | EXPENSIVE -31% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -43% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -29% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #206 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #233 | N/A | INNOVATING |
| Drones | UMAC | C 1/12 #175 | N/A | N/A |
| Drones | UAVS | C 0/12 #234 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #220 | DEEP VALUE +100% (LOW) | DISRUPTOR |
| Drones | DPRO | C 0/12 #219 | DEEP VALUE +53% (LOW) | BEING DISRUPTED |
| Drones | KTOS | C 0/12 #208 | FAIR +2% (MED) | INNOVATING |
| Drones | AVAV | C 0/12 #201 | DEEP VALUE +83% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #236 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #152 | FAIR +8% (HIGH) | STABLE |
| Raw materials | SCCO | C 1/12 #154 | EXPENSIVE -26% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #148 | RICH -14% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #161 | RICH -11% (LOW) | STABLE |
| Raw materials | FCX | C 1/12 #164 | RICH -15% (MED) | STABLE |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 29.7 | 56.4 |  |
| LLY | 16.1 | 55.1 |  |
| DLTR | 20.4 | 61.8 |  |
| ABBV | 23.4 | 52.4 |  |
| V | 19.8 | 61.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -39.2 | 30.9 | SPEC |
| UUUU | -42.1 | 31.4 | SPEC |
| QBTS | -47.9 | 33.8 | SPEC |
| ASTS | -23.8 | 35.0 | SPEC |
| UEC | -31.1 | 37.7 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._