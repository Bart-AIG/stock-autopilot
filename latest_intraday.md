# Strategy report - INTRADAY  (2026-11-04 16:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CVX | A+ | 12/12 | #11 | RSI2 dip | Energy |  |  |  | 218.57 | 6.6 | 218.57 | 209.09 | 232.8 | -4.3% |
| XOM | A+ | 12/12 | #15 | RSI2 dip | Energy |  |  |  | 171.56 | 7.0 | 171.56 | 163.42 | 183.77 | -4.7% |
| COP | A+ | 11/12 | #19 | RSI2 dip | Energy |  |  | ⚠️ 2026-11-05 | 138.73 | 6.6 | 138.73 | 130.95 | 150.41 | -5.6% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** COP (2026-11-05). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 3/3 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): PLTR (C 7/12), OXY (C 8/12), MPC (B 8/12), PANW (C 4/12), EOG (B 11/12), PSX (C 6/12), ZS (B 10/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +359.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | REGN | A+ | 12/12 | +24.0% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | TMO | A+ | 12/12 | +20.3% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LLY | A+ | 12/12 | +19.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | WBD | A+ | 12/12 | +18.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | ABBV | A+ | 12/12 | +17.4% | -3.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | AMGN | A+ | 12/12 | +17.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | MAR | A+ | 12/12 | +17.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | V | A+ | 12/12 | +16.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PFE | A+ | 12/12 | +16.5% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | CVX | A+ | 12/12 | +15.4% | -7.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AAPL | A+ | 12/12 | +13.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PM | A+ | 12/12 | +13.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | VRTX | A+ | 12/12 | +12.0% | -3.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | XOM | A+ | 12/12 | +10.9% | -8.6% | EXPENSIVE -29% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | KO | A+ | 12/12 | +10.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | TXN | A+ | 12/12 | +10.6% | -7.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | EMR | A+ | 12/12 | +8.4% | -0.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | COP | A+ | 11/12 | +18.9% | -10.1% | RICH -18% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MA | A+ | 11/12 | +16.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | CME | A+ | 11/12 | +16.0% | -6.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | PG | A+ | 11/12 | +14.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | MSFT | A+ | 11/12 | +10.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | EOG | B | 11/12 | +10.0% | -9.8% | FAIR -1% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | ADI | B | 11/12 | +6.7% | -9.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 222)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1227.1 | 30.5 | F |
| 2 **TOP** | MRNA | 613.3 | 65.4 | T |
| 3 **TOP** | LITE | 566.4 | 30.5 | F |
| 4 **TOP** | MU | 466.4 | 35.8 | T |
| 5 **TOP** | AAOI | 335.3 | 31.8 | F |
| 6 **TOP** | SOXL | 329.7 | 32.1 | F |
| 7 **TOP** | DELL | 292.4 | 31.4 | T |
| 8 **TOP** | AMD | 283.6 | 38.3 | T |
| 9 **TOP** | VIAV | 268.8 | 36.0 | F |
| 10 **TOP** | INTC | 215.5 | 22.4 | F |
| 11 **TOP** | MRVL | 214.6 | 26.3 | F |
| 12 **TOP** | COHR | 193.7 | 32.2 | F |
| 13 **TOP** | VLO | 161.4 | 34.9 | T |
| 14 **TOP** | MTSI | 157.7 | 35.3 | F |
| 15 **TOP** | AMAT | 149.3 | 33.5 | F |
| 16 **TOP** | LRCX | 137.2 | 31.1 | F |
| 17 **TOP** | MPC | 124.4 | 34.1 | T |
| 18 **TOP** | CRWD | 122.6 | 45.4 | T |
| 19 **TOP** | PSX | 102.8 | 38.9 | T |
| 20 **TOP** | ARM | 98.4 | 33.2 | F |
| 21 **TOP** | PANW | 96.3 | 41.7 | T |
| 22 **TOP** | KLAC | 87.8 | 37.0 | F |
| 23  | FCX | 83.0 | 31.7 | F |
| 24  | DDOG | 82.1 | 29.0 | F |
| 25  | NUE | 82.1 | 51.8 | T |
| 26  | NBIS | 81.7 | 34.8 | F |
| 27  | FCEL | 77.0 | 34.4 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | META | Other | 634.67 | 41.6 | 84.7 | -5.9% | -5.8% | 4.4 | FAIR -3% (MED) | 617.76 | +36% | DISRUPTOR (quant INNOVATING) [research: disruptor] | growth: its multiples disagree with each other | disruption: revenue +20%/yr over 3 yrs; analysts see revenue +28% next year; research 2026-10-22: AI glasses are a new device category Meta dominates (~76% of 2025 smart-glasses shipments per IDC); the core ad business is growing (+26%), and the open question is the return on its capex. |
| 🟡 dip | QQQ | Index-ETF | 693.36 | 39.3 | 63.1 | -3.4% | -4.2% | 25.4 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | OXY | Energy | 57.82 | 37.2 | 4.0 | -6.6% | -3.9% | 30.0 | UNDERVALUED +13% (HIGH) | 66.11 | +21% | STABLE | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | EOG | Energy | 149.39 | 42.3 | 5.8 | -4.7% | +0.1% | 30.0 | FAIR -1% (HIGH) | 149.37 | +6% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | DELL | Other | 373.93 | 31.4 | 13.7 | -22.0% | -26.8% | 292.4 | EXPENSIVE -50% (LOW) | 192.36 | +48% | INNOVATING (quant STABLE) [research: innovating] | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| 🟢 oversold | NET | AI-software | 261.66 | 33.0 | 17.3 | -16.0% | -18.2% | 65.9 | EXPENSIVE -41% (LOW) | 155.68 | +32% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟢 oversold | SNOW | AI-software | 286.29 | 34.6 | 12.7 | -12.2% | -13.2% | 44.2 | UNDERVALUED +17% (LOW) | 341.13 | +49% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | PLTR | AI-software | 174.07 | 34.9 | 0.5 | -10.7% | -6.9% | 9.4 | EXPENSIVE -50% (LOW) | 87.6 | +34% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +89% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | PANW | AI-software | 349.73 | 41.7 | 4.4 | -6.2% | -6.0% | 96.3 | EXPENSIVE -50% (LOW) | 177.25 | +17% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | COP | Energy | 138.47 | 44.8 | 6.6 | -4.3% | +1.3% | 36.4 | RICH -18% (HIGH) | 115.56 | +12% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | MPC | Energy | 390.77 | 34.1 | 4.1 | -14.1% | -7.2% | 124.4 | EXPENSIVE -37% (MED) | 253.7 | +13% | STABLE | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | PSX | Energy | 257.79 | 38.9 | 7.4 | -8.7% | -3.8% | 102.8 | EXPENSIVE -30% (MED) | 184.07 | +11% | STABLE | cyclical: PEAK-CYCLE margins (11% vs 6% normal): earnings multiples ignored | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +117% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -50% (LOW) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -49% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +37% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -46% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -37% (MED) | STABLE | commodity producer: revenue and margins follow the commodity price, not competitors |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 652.5 | 65.4 |  |
| TMO | 16.2 | 57.0 |  |
| ABBV | 25.8 | 57.1 |  |
| AMGN | 35.9 | 72.1 |  |
| V | 10.0 | 74.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -55.1 | 28.4 | SPEC |
| QBTS | -52.3 | 27.5 | SPEC |
| ASTS | -11.3 | 30.7 | SPEC |
| SMR | -80.4 | 30.1 | SPEC |
| IREN | -39.1 | 30.8 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._