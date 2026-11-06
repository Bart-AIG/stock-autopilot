# Strategy report - INTRADAY  (2026-11-06 17:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PFE | A+ | 12/12 | #11 | 21 EMA pullback | Other |  |  |  | 29.32 | 17.4 | 29.32 | 28.12 | 30.79 | -4.1% |
| PM | A+ | 12/12 | #12 | 21 EMA pullback | Other |  |  |  | 199.54 | 11.8 | 199.54 | 189.99 | 211.28 | -4.8% |
| EMR | A+ | 12/12 | #14 | 21 EMA pullback | Other |  |  |  | 163.55 | 34.5 | 163.55 | 156.39 | 170.74 | -4.4% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ZS (C 7/12), MPC (B 8/12), TXN (B 8/12), VLO (C 7/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +350.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +24.7% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | WBD | A+ | 12/12 | +22.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | V | A+ | 12/12 | +21.5% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | ABBV | A+ | 12/12 | +21.2% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +20.0% | -2.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | REGN | A+ | 12/12 | +16.4% | -6.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | LLY | A+ | 12/12 | +15.3% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | AMGN | A+ | 12/12 | +15.0% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | KO | A+ | 12/12 | +14.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | PFE | A+ | 12/12 | +12.8% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PM | A+ | 12/12 | +11.5% | -5.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | VRTX | A+ | 12/12 | +8.8% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EMR | A+ | 12/12 | +7.3% | -4.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | SPOT | A+ | 11/12 | +23.3% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MA | A+ | 11/12 | +21.3% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | CME | A+ | 11/12 | +20.6% | -6.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PG | A+ | 11/12 | +17.6% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | DE | A+ | 11/12 | +14.7% | -5.1% | EXPENSIVE -44% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | BLK | A+ | 11/12 | +9.5% | -2.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | ABNB | A+ | 11/12 | +7.0% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | ASND | A+ | 11/12 | +4.2% | -7.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | ACN | A | 10/12 | +50.3% | -9.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | GILD | B | 10/12 | +30.5% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 25 | MO | B | 10/12 | +20.9% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1299.3 | 26.7 | F |
| 2 **TOP** | MRNA | 618.7 | 66.5 | T |
| 3 **TOP** | LITE | 607.0 | 28.7 | F |
| 4 **TOP** | MU | 485.9 | 32.0 | F |
| 5 **TOP** | SOXL | 309.2 | 29.3 | F |
| 6 **TOP** | AAOI | 291.0 | 30.0 | F |
| 7 **TOP** | DELL | 283.7 | 30.1 | F |
| 8 **TOP** | VIAV | 265.8 | 38.4 | F |
| 9 **TOP** | MRVL | 227.3 | 25.0 | F |
| 10 **TOP** | AMD | 205.4 | 37.6 | T |
| 11 **TOP** | INTC | 204.3 | 25.1 | F |
| 12 **TOP** | COHR | 194.6 | 36.4 | F |
| 13 **TOP** | MTSI | 162.5 | 36.8 | F |
| 14 **TOP** | VLO | 159.9 | 32.1 | T |
| 15 **TOP** | AMAT | 146.1 | 31.5 | F |
| 16 **TOP** | LRCX | 134.8 | 31.4 | F |
| 17 **TOP** | MPC | 130.9 | 30.3 | T |
| 18 **TOP** | CRWD | 119.1 | 37.4 | T |
| 19 **TOP** | PSX | 105.2 | 35.4 | T |
| 20 **TOP** | NBIS | 101.5 | 34.0 | F |
| 21 **TOP** | PANW | 92.2 | 34.4 | T |
| 22 **TOP** | ARM | 84.7 | 30.5 | F |
| 23  | KLAC | 81.5 | 35.0 | F |
| 24  | NUE | 81.5 | 43.8 | T |
| 25  | FCEL | 80.2 | 35.0 | F |
| 26  | FCX | 76.6 | 34.5 | F |
| 27  | DDOG | 75.6 | 27.7 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MPC | Energy | 373.36 | 30.3 | 2.0 | -16.4% | -11.5% | 130.9 | EXPENSIVE -34% (LOW) | 247.66 | +22% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| 🟢 oversold | PLTR | AI-software | 161.54 | 32.3 | 38.6 | -15.1% | -13.1% | 6.6 | EXPENSIVE -50% (LOW) | 80.81 | +45% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +89% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | SNOW | AI-software | 275.43 | 33.4 | 32.4 | -13.4% | -16.1% | 41.8 | DEEP VALUE +26% (LOW) | 341.12 | +61% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | PANW | AI-software | 318.09 | 34.4 | 15.6 | -12.5% | -14.1% | 92.2 | EXPENSIVE -50% (LOW) | 161.74 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | TXN | Semis | 275.69 | 41.8 | 6.9 | -5.2% | -1.2% | 63.2 | EXPENSIVE -28% (HIGH) | 200.73 | +19% | STABLE | cyclical | disruption: analysts see revenue +27% next year; cyclical: judged on 5-yr trends |
| 🟢 oversold | VLO | Energy | 349.96 | 32.1 | 7.6 | -14.8% | -12.4% | 159.9 | EXPENSIVE -44% (LOW) | 195.36 | +27% | AT RISK (quant STABLE) [research: threatened] | cyclical: PEAK-CYCLE margins (14% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| 🟡 dip | OXY | Energy | 56.89 | 36.0 | 27.3 | -7.5% | -5.3% | 28.4 | UNDERVALUED +17% (HIGH) | 66.11 | +26% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Core is oil and gas (2026 capex cut 8%, ~1% production growth); Stratos direct-air-capture plant could open a carbon-removal market but has slipped to late 2026 and its economics are unproven without subsidies. |
| 🟡 dip | EOG | Energy | 147.94 | 42.4 | 44.6 | -5.5% | -0.9% | 30.6 | UNDERVALUED +12% (HIGH) | 165.97 | +7% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟡 dip | SHOP | Other | 150.7 | 44.2 | 58.7 | -8.8% | -1.2% | 2.9 | UNDERVALUED +12% (MED) | 164.58 | +23% | INNOVATING | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +33% next year |
| 🟡 dip | COP | Energy | 137.57 | 44.7 | 40.2 | -5.0% | +0.5% | 36.3 | FAIR -9% (HIGH) | 124.95 | +15% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +117% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -48% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -43% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +50% (HIGH) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -44% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -34% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -45% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -29% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 736.2 | 66.5 |  |
| MAR | 27.6 | 71.3 |  |
| V | 10.3 | 63.7 |  |
| ABBV | 25.7 | 58.6 |  |
| TMO | 14.9 | 54.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| ASTS | -19.1 | 30.2 | SPEC |
| QBTS | -52.9 | 35.2 | SPEC |
| CRWV | -28.7 | 31.5 | SPEC |
| OKLO | -71.5 | 36.4 | SPEC |
| APLD | -27.9 | 36.5 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._