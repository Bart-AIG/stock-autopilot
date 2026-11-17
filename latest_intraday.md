# Strategy report - INTRADAY  (2026-11-17 16:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V | A+ | 12/12 | #4 | 21 EMA pullback | Other |  |  |  | 419.09 | 19.3 | 419.09 | 401.9 | 436.57 | -4.1% |
| TMO | A+ | 12/12 | #6 | RSI2 dip | Other |  |  |  | 690.88 | 9.6 | 690.88 | 657.28 | 721.63 | -4.9% |
| AMGN | A+ | 12/12 | #11 | RSI2 dip | Other |  |  |  | 458.01 | 4.3 | 458.01 | 440.53 | 478.48 | -3.8% |
| VRTX | A+ | 12/12 | #12 | RSI2 dip | Other |  |  |  | 531.28 | 1.6 | 531.28 | 506.92 | 558.88 | -4.6% |
| MA | A+ | 11/12 | #15 | 21 EMA pullback | Other |  |  |  | 646.68 | 14.5 | 646.68 | 616.81 | 672.68 | -4.6% |
| BLK | A+ | 11/12 | #20 | RSI2 dip | Other |  |  |  | 1183.9 | 9.2 | 1183.9 | 1121.82 | 1226.31 | -5.2% |
| UNP | A+ | 11/12 | #22 | 21 EMA pullback | Other |  |  |  | 297.25 | 14.9 | 297.25 | 284.67 | 308.53 | -4.2% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ZS (C 6/12), TEM (C 6/12), MRNA (B 10/12), RBRK (C 7/12), EMR (B 10/12), MSFT (C 6/12), SNOW (C 3/12), DE (B 7/12), PLTR (C 4/12), DIA (C 5/12), PANW (C 3/12), AMZN (C 7/12), PFE (B 9/12), CRWD (C 5/12), NET (C 5/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MO | A+ | 12/12 | +24.1% | -0.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | WBD | A+ | 12/12 | +23.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | MAR | A+ | 12/12 | +23.2% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | V | A+ | 12/12 | +19.5% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | REGN | A+ | 12/12 | +18.5% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +17.4% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | LLY | A+ | 12/12 | +15.7% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | ABBV | A+ | 12/12 | +14.9% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | DLTR | A+ | 12/12 | +10.2% | -5.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | EOG | A+ | 12/12 | +9.3% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMGN | A+ | 12/12 | +8.4% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | VRTX | A+ | 12/12 | +1.1% | -4.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PG | A+ | 11/12 | +24.6% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | CME | A+ | 11/12 | +22.7% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | MA | A+ | 11/12 | +17.6% | -3.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 16 | DIS | A+ | 11/12 | +16.6% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | KO | A+ | 11/12 | +14.8% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 18 | LIN | A+ | 11/12 | +13.4% | -4.4% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PM | A+ | 11/12 | +9.6% | -5.8% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | BLK | A+ | 11/12 | +6.7% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | ASND | A+ | 11/12 | +6.1% | -5.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | UNP | A+ | 11/12 | +3.2% | -4.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | ABNB | A+ | 11/12 | +2.8% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | MRNA | B | 10/12 | +25.4% | -21.9% | — | — | MA STACK, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | COST | B | 10/12 | +21.6% | 0.0% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 827.0 | 30.1 | F |
| 2 **TOP** | MRNA | 738.2 | 45.5 | T |
| 3 **TOP** | LITE | 400.2 | 35.2 | F |
| 4 **TOP** | MU | 334.3 | 35.8 | F |
| 5 **TOP** | DELL | 202.0 | 32.4 | F |
| 6 **TOP** | VLO | 181.9 | 42.6 | T |
| 7 **TOP** | ILMN | 175.0 | 32.6 | T |
| 8 **TOP** | MPC | 159.2 | 43.6 | T |
| 9 **TOP** | MRVL | 159.0 | 32.4 | F |
| 10 **TOP** | VIAV | 156.0 | 41.0 | F |
| 11 **TOP** | INTC | 142.8 | 28.9 | F |
| 12 **TOP** | AAOI | 136.7 | 31.6 | F |
| 13 **TOP** | SOXL | 132.5 | 33.5 | F |
| 14 **TOP** | AMD | 126.9 | 45.4 | T |
| 15 **TOP** | PSX | 126.8 | 43.9 | T |
| 16 **TOP** | COHR | 100.2 | 43.5 | F |
| 17 **TOP** | NUE | 94.5 | 48.2 | T |
| 18 **TOP** | MTSI | 91.7 | 42.6 | F |
| 19 **TOP** | CRWD | 87.7 | 38.7 | T |
| 20 **TOP** | LRCX | 86.5 | 36.4 | F |
| 21 **TOP** | AMAT | 81.9 | 37.9 | F |
| 22 **TOP** | MRK | 72.1 | 46.0 | T |
| 23  | WBD | 70.1 | 75.2 | T |
| 24  | TGT | 69.8 | 49.3 | T |
| 25  | COP | 69.4 | 52.7 | T |
| 26  | FCX | 68.9 | 32.0 | F |
| 27  | PANW | 64.5 | 34.9 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | AMZN | Other | 256.27 | 48.4 | 5.9 | -0.2% | +0.6% | 17.3 | DEEP VALUE +100% (LOW) | 519.22 | +27% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | USB | Other | 59.21 | 46.4 | 9.7 | -1.5% | -0.3% | 28.5 | FAIR +4% (HIGH) | 61.64 | +15% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟢 oversold | PLTR | AI-software | 156.89 | 33.0 | 4.5 | -12.3% | -14.8% | 4.4 | EXPENSIVE -50% (LOW) | 79.7 | +55% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +90% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | SNOW | AI-software | 267.04 | 34.1 | 3.8 | -11.9% | -17.2% | 27.5 | DEEP VALUE +26% (LOW) | 340.45 | +61% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | PANW | AI-software | 308.59 | 34.9 | 5.0 | -11.2% | -15.8% | 64.5 | EXPENSIVE -50% (LOW) | 153.15 | +36% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | RBRK | AI-infra | 100.3 | 35.7 | 3.1 | -14.7% | -12.1% | 45.6 | RICH -17% (LOW) | 85.63 | +6% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +30%/yr over 3 yrs; analysts see revenue +28% next year; research 2026-10-23: Cyber-resilience leader extending into AI-agent governance and recovery (Rubrik Agent Cloud, Bedrock/Copilot/Gemini integrations); cloud ARR +57%; rivals CrowdStrike and Palo Alto compete in AI security. |
| 🟢 oversold | CRWD | AI-software | 219.62 | 38.7 | 6.4 | -8.2% | -10.5% | 87.7 | EXPENSIVE -38% (LOW) | 136.34 | +14% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +29%/yr over 3 yrs; analysts see revenue +25% next year; research 2026-10-21: Endpoint security leader adding AI-agent security; Microsoft Defender/Security Copilot bundling is the standing competitive threat (CEO: 'Microsoft is always going to be a competitor'), not obsolescence. Evidence on new-market creation is thin. |
| 🟢 oversold | MSFT | Other | 500.52 | 40.0 | 3.6 | -5.0% | -3.7% | 3.0 | RICH -13% (LOW) | 444.23 | +23% | STABLE | growth: its multiples disagree with each other; analysts disagree | disruption: revenue +16%/yr over 3 yrs |
| 🟢 oversold | DIA | Index-ETF | 508.59 | 40.6 | 4.7 | -2.4% | -1.9% | 12.4 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | NET | AI-software | 282.08 | 43.6 | 9.1 | -5.0% | -11.9% | 41.1 | EXPENSIVE -41% (LOW) | 167.42 | +23% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +37% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟢 oversold | EMR | Other | 160.19 | 44.3 | 3.4 | -3.0% | +0.2% | 24.9 | RICH -22% (HIGH) | 125.85 | +7% | STABLE | cyclical | disruption: gross margin up 4 pts (53%); cyclical: judged on 5-yr trends |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +18% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +118% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -47% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -37% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +61% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -44% (MED) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -36% (MED) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -32% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MO | 27.3 | 65.7 |  |
| MAR | 36.7 | 69.6 |  |
| V | 22.1 | 56.5 |  |
| REGN | 12.8 | 67.9 |  |
| TMO | 17.4 | 50.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -40.2 | 29.5 | SPEC |
| UUUU | -47.5 | 26.3 | SPEC |
| ASTS | -31.8 | 31.7 | SPEC |
| QBTS | -49.9 | 29.4 | SPEC |
| RGTI | -54.2 | 32.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._