# Strategy report - MORNING  (2026-11-16 15:10 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #6 | 21 EMA pullback | Other |  |  |  | 696.95 | 15.8 | 696.95 | 663.15 | 721.63 | -4.8% |
| EMR | A+ | 12/12 | #14 | RSI2 dip | Other |  |  |  | 162.84 | 5.6 | 162.84 | 154.55 | 170.74 | -5.1% |
| MRNA | A+ | 11/12 | #16 | RSI2 dip | Other |  |  |  | 216.59 | 4.6 | 216.59 | 182.17 | 268.23 | -15.9% ⚠ |
| COP | A+ | 11/12 | #23 | 21 EMA pullback | Energy |  |  |  | 139.67 | 42.7 | 139.67 | 132.18 | 150.9 | -5.4% |

### How to read this (concentration & sizing)
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ZS (C 7/12), ILMN (C 5/12), TEM (B 8/12), ROST (C 5/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MO | A+ | 12/12 | +24.3% | 0.0% | RICH -18% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +22.4% | -0.5% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | LLY | A+ | 12/12 | +22.4% | 0.0% | RICH -19% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | REGN | A+ | 12/12 | +21.4% | -1.3% | RICH -11% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | WBD | A+ | 12/12 | +21.3% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +21.2% | -3.4% | RICH -19% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | V | A+ | 12/12 | +20.6% | -1.8% | RICH -14% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | ABBV | A+ | 12/12 | +17.9% | 0.0% | EXPENSIVE -42% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | AAPL | A+ | 12/12 | +16.9% | -0.7% | EXPENSIVE -31% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | KO | A+ | 12/12 | +15.5% | 0.0% | FAIR -8% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMGN | A+ | 12/12 | +13.2% | -1.9% | EXPENSIVE -30% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EOG | A+ | 12/12 | +8.0% | -5.5% | FAIR +7% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | DLTR | A+ | 12/12 | +7.5% | -7.1% | DEEP VALUE +38% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EMR | A+ | 12/12 | +6.0% | -4.6% | RICH -22% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | VRTX | A+ | 12/12 | +5.8% | -2.7% | RICH -23% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MRNA | A+ | 11/12 | +246.8% | -19.5% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PG | A+ | 11/12 | +23.0% | 0.0% | FAIR -6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | CME | A+ | 11/12 | +20.2% | -2.4% | FAIR +2% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MA | A+ | 11/12 | +18.7% | -1.0% | FAIR -0% (HIGH) | INNOVATING (quant STABLE) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | DIS | A+ | 11/12 | +17.2% | -0.7% | FAIR +3% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | LIN | A+ | 11/12 | +13.1% | -3.4% | EXPENSIVE -25% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | MDLZ | A+ | 11/12 | +11.7% | 0.0% | UNDERVALUED +16% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | COP | A+ | 11/12 | +10.5% | -9.3% | FAIR -10% (HIGH) | STABLE [research: neutral] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | PFE | B | 11/12 | +9.7% | -5.4% | EXPENSIVE -28% (MED) | AT RISK [research: neutral] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | BLK | B | 11/12 | +8.0% | -1.0% | RICH -23% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 827.0 | 31.8 | F |
| 2 **TOP** | MRNA | 738.2 | 47.5 | T |
| 3 **TOP** | LITE | 400.2 | 34.7 | F |
| 4 **TOP** | MU | 334.3 | 38.6 | F |
| 5 **TOP** | DELL | 202.0 | 33.5 | F |
| 6 **TOP** | VLO | 181.9 | 43.4 | T |
| 7 **TOP** | ILMN | 175.0 | 33.3 | T |
| 8 **TOP** | MPC | 159.2 | 44.4 | T |
| 9 **TOP** | MRVL | 159.0 | 32.5 | F |
| 10 **TOP** | VIAV | 156.0 | 40.4 | F |
| 11 **TOP** | INTC | 142.8 | 30.1 | F |
| 12 **TOP** | AAOI | 136.7 | 32.7 | F |
| 13 **TOP** | SOXL | 132.5 | 34.4 | F |
| 14 **TOP** | AMD | 126.9 | 47.7 | T |
| 15 **TOP** | PSX | 126.8 | 45.4 | T |
| 16 **TOP** | COHR | 100.2 | 41.8 | F |
| 17 **TOP** | NUE | 94.5 | 49.7 | T |
| 18 **TOP** | MTSI | 91.7 | 42.3 | F |
| 19 **TOP** | CRWD | 87.7 | 39.6 | T |
| 20 **TOP** | LRCX | 86.5 | 38.1 | F |
| 21 **TOP** | AMAT | 81.9 | 39.0 | F |
| 22 **TOP** | MRK | 72.1 | 54.0 | T |
| 23  | WBD | 70.1 | 75.2 | T |
| 24  | TGT | 69.8 | 53.7 | T |
| 25  | COP | 69.4 | 49.2 | T |
| 26  | FCX | 68.9 | 33.5 | F |
| 27  | PANW | 64.5 | 36.6 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | ROST | Other | 227.13 | 44.1 | 7.2 | -2.9% | -1.9% | 51.6 | FAIR -10% (HIGH) | 204.92 | +24% | STABLE [research: neutral] | steady | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |
| 🟢 oversold | DE | Other | 666.67 | 50.2 | 9.1 | +0.6% | -0.2% | 40.0 | EXPENSIVE -44% (HIGH) | 375.53 | +11% | STABLE | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%) |
| 🟡 dip | CVS | Other | 90.13 | 52.6 | 82.4 | +0.8% | +0.7% | 11.9 | DEEP VALUE +30% (HIGH) | 117.1 | +22% | STABLE [research: neutral] | steady: analysts agree | disruption: gross margin slipping 3 pts (14%); research 2026-10-28: Turnaround led by Aetna margin recovery (MLR 87.4% vs 89.9%); 2026 EPS guide raised twice to $7.90-8.10. PBM business-model transition flagged as a 2027 headwind; no clear tech obsolescence found in this check. |
| 🟡 dip | SHOP | Other | 144.53 | 40.8 | 16.3 | -8.0% | -5.4% | 7.5 | UNDERVALUED +15% (MED) | 164.5 | +26% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +30% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟡 dip | OXY | Energy | 57.62 | 42.4 | 33.1 | -4.3% | -3.5% | 52.5 | UNDERVALUED +21% (HIGH) | 69.7 | +22% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Core is oil and gas (2026 capex cut 8%, ~1% production growth); Stratos direct-air-capture plant could open a carbon-removal market but has slipped to late 2026 and its economics are unproven without subsidies. |
| 🟡 dip | QCOM | Semis | 171.24 | 47.9 | 21.5 | -1.1% | -4.2% | 5.3 | FAIR -2% (HIGH) | 166.99 | +9% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: R&D 24% of revenue; cyclical: judged on 5-yr trends; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | PANW | AI-software | 315.02 | 36.6 | 12.4 | -9.8% | -14.2% | 64.5 | EXPENSIVE -50% (LOW) | 157.37 | +32% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟡 dip | PLTR | AI-software | 163.5 | 36.6 | 10.8 | -9.6% | -11.4% | 4.4 | EXPENSIVE -50% (LOW) | 81.28 | +52% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +90% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟡 dip | SNOW | AI-software | 283.57 | 39.1 | 11.4 | -7.2% | -12.4% | 27.5 | UNDERVALUED +21% (LOW) | 341.13 | +54% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | CRWD | AI-software | 221.47 | 39.6 | 12.1 | -7.6% | -9.6% | 87.7 | EXPENSIVE -38% (LOW) | 136.42 | +14% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +29%/yr over 3 yrs; analysts see revenue +25% next year; research 2026-10-21: Endpoint security leader adding AI-agent security; Microsoft Defender/Security Copilot bundling is the standing competitive threat (CEO: 'Microsoft is always going to be a competitor'), not obsolescence. Evidence on new-market creation is thin. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +18% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +118% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -47% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -44% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +59% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -44% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -36% (MED) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -30% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #211 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #236 | N/A | INNOVATING |
| Drones | UMAC | C 1/12 #182 | N/A | N/A |
| Drones | UAVS | C 0/12 #232 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #223 | DEEP VALUE +100% (LOW) | DISRUPTOR |
| Drones | DPRO | C 0/12 #206 | UNDERVALUED +24% (LOW) | AT RISK |
| Drones | KTOS | C 0/12 #221 | FAIR -7% (MED) | INNOVATING |
| Drones | AVAV | C 0/12 #204 | DEEP VALUE +55% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #234 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #157 | FAIR +0% (HIGH) | STABLE |
| Raw materials | SCCO | C 1/12 #154 | EXPENSIVE -32% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #151 | RICH -18% (HIGH) | STABLE |
| Raw materials | CENX | C 2/12 #141 | RICH -21% (LOW) | STABLE |
| Raw materials | FCX | C 1/12 #152 | RICH -24% (MED) | STABLE |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MO | 29.9 | 67.3 |  |
| MAR | 35.0 | 70.2 |  |
| LLY | 22.9 | 72.0 |  |
| REGN | 13.8 | 69.1 |  |
| TMO | 18.9 | 52.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -44.5 | 30.2 | SPEC |
| UUUU | -45.3 | 29.3 | SPEC |
| QBTS | -49.6 | 33.1 | SPEC |
| ASTS | -33.8 | 35.5 | SPEC |
| APLD | -21.7 | 37.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._