# Strategy report - INTRADAY  (2026-10-30 15:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RBRK | A+ | 12/12 | #2 | RSI2 dip | AI-infra | SPEC |  |  | 124.06 | 8.2 | 124.06 | 112.95 | 136 | -9.0% |
| CRWD | A+ | 12/12 | #5 | 21 EMA pullback | AI-software |  |  |  | 251.86 | 12.3 | 251.86 | 228.96 | 278.86 | -9.1% |
| PLTR | A+ | 11/12 | #20 | RSI2 dip | AI-software |  |  |  | 187.1 | 2.3 | 187.1 | 173.23 | 207.9 | -7.4% |
| MPC | A+ | 11/12 | #21 | 21 EMA pullback | Energy |  |  |  | 439.07 | 49.6 | 439.07 | 410.47 | 481.96 | -6.5% |

### How to read this (concentration & sizing)
- 🔴 **Correlated cluster:** 3/4 setups are in the AI/tech complex (semis, AI-infra, quantum, photonics). They move together — buying several is **ONE leveraged AI bet, not diversification.** Pick 1-2, not the cluster.
- ⚠️ **1/4 are speculative** (high-vol). Size tiny; keep TOTAL speculative exposure ≤ ~20-25% of the account.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): HPQ (C 7/12), NET (C 4/12), DDOG (C 8/12), SHOP (B 10/12), SNOW (C 4/12), NVDA (C 5/12), MSFT (B 11/12), CSCO (C 3/12), DELL (C 7/12), QLD (C 5/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +304.9% | -9.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | RBRK | A+ | 12/12 | +67.8% | -7.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | GILD | A+ | 12/12 | +31.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LLY | A+ | 12/12 | +27.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CRWD | A+ | 12/12 | +25.0% | -9.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | AMGN | A+ | 12/12 | +23.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | TMO | A+ | 12/12 | +21.6% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | PFE | A+ | 12/12 | +20.8% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | ABBV | A+ | 12/12 | +20.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | XOM | A+ | 12/12 | +18.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | WBD | A+ | 12/12 | +18.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AAPL | A+ | 12/12 | +14.6% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | OXY | A+ | 12/12 | +14.1% | -4.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EOG | A+ | 12/12 | +12.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | TXN | A+ | 12/12 | +12.2% | -8.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PM | A+ | 12/12 | +11.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | KO | A+ | 12/12 | +8.4% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | EMR | A+ | 12/12 | +8.0% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | NUE | A+ | 12/12 | +4.4% | -0.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | PLTR | A+ | 11/12 | +49.4% | -10.0% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MPC | A+ | 11/12 | +42.7% | -9.5% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | VRTX | A+ | 11/12 | +18.4% | 0.0% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | MAR | A+ | 11/12 | +15.2% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | ADI | B | 11/12 | +14.9% | -6.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | V | B | 11/12 | +13.0% | -0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1450.7 | 34.7 | F |
| 2 **TOP** | MRNA | 645.5 | 58.0 | T |
| 3 **TOP** | MU | 536.6 | 42.9 | T |
| 4 **TOP** | LITE | 496.9 | 43.5 | T |
| 5 **TOP** | SOXL | 324.4 | 35.0 | F |
| 6 **TOP** | AAOI | 282.8 | 36.4 | F |
| 7 **TOP** | DELL | 279.5 | 36.9 | T |
| 8 **TOP** | AMD | 278.1 | 41.1 | T |
| 9 **TOP** | INTC | 258.4 | 25.3 | F |
| 10 **TOP** | VIAV | 230.3 | 36.5 | F |
| 11 **TOP** | MRVL | 214.3 | 35.5 | T |
| 12 **TOP** | COHR | 167.2 | 34.7 | F |
| 13 **TOP** | AMAT | 149.8 | 37.3 | F |
| 14 **TOP** | LRCX | 145.3 | 34.1 | F |
| 15 **TOP** | MTSI | 128.8 | 38.1 | F |
| 16 **TOP** | VLO | 127.7 | 41.4 | T |
| 17 **TOP** | CRWD | 115.9 | 51.6 | T |
| 18 **TOP** | FCEL | 110.5 | 34.5 | F |
| 19 **TOP** | NBIS | 110.1 | 37.0 | F |
| 20 **TOP** | MPC | 105.2 | 49.1 | T |
| 21 **TOP** | ARM | 104.7 | 34.7 | F |
| 22 **TOP** | PANW | 95.1 | 48.6 | T |
| 23  | DDOG | 92.3 | 39.7 | T |
| 24  | PSX | 87.7 | 53.4 | T |
| 25  | KLAC | 80.7 | 42.5 | F |
| 26  | FCX | 78.5 | 31.8 | F |
| 27  | TGT | 74.7 | 49.1 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | QQQ | Index-ETF | 696.94 | 36.9 | 10.0 | -4.3% | -3.9% | 23.2 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NVDA | Semis | 206.91 | 36.6 | 6.2 | -6.6% | -6.7% | 22.4 | FAIR +7% (MED) | 223.03 | +56% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟢 oversold | NET | AI-software | 280.51 | 35.6 | 2.9 | -13.5% | -12.5% | 61.8 | EXPENSIVE -46% (LOW) | 155.68 | +20% | DISRUPTOR [research: innovating] | preprofit: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟢 oversold | DELL | Other | 433.85 | 36.9 | 8.8 | -14.3% | -15.6% | 279.5 | EXPENSIVE -50% (LOW) | 218.37 | +30% | INNOVATING (quant STABLE) [research: innovating] | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| 🟢 oversold | SNOW | AI-software | 304.29 | 39.1 | 5.7 | -8.6% | -8.3% | 50.5 | UNDERVALUED +11% (LOW) | 341.13 | +42% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | DDOG | AI-software | 238.7 | 39.7 | 3.3 | -11.7% | -5.0% | 92.3 | RICH -20% (LOW) | 197.79 | +22% | DISRUPTOR | growth: business changed (margin 8% vs 2% 10-yr median): its own history is a weak yardstick; analysts disagree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +31% next year |
| 🟢 oversold | PLTR | AI-software | 188.15 | 45.1 | 2.3 | -4.7% | +0.6% | 2.5 | EXPENSIVE -50% (LOW) | 94.32 | +22% | DISRUPTOR | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +84% next year |
| 🟢 oversold | CSCO | Other | 105.28 | 40.7 | 8.7 | -5.2% | -4.3% | 57.3 | EXPENSIVE -43% (MED) | 60.4 | +28% | INNOVATING | growth: analysts disagree | disruption: analysts see revenue +15% next year; R&D 15% of revenue |
| 🟢 oversold | HPQ | Other | 29.41 | 39.4 | 2.1 | -6.8% | -7.3% | 14.9 | UNDERVALUED +14% (MED) | 33.07 | -12% | AT RISK | **VALUE TRAP?** growth: analysts disagree | disruption: revenue shrinking -4%/yr over 3 yrs |
| 🟡 dip | USB | Other | 59.89 | 54.8 | 40.9 | +2.7% | +0.0% | 19.5 | FAIR +3% (HIGH) | 61.64 | +14% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | MRVL | Semis | 202.72 | 35.5 | 10.0 | -18.3% | -16.5% | 214.3 | EXPENSIVE -50% (LOW) | 101.94 | +69% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +110% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| DELL | no | EXPENSIVE -50% (LOW) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -33% (LOW) | DISRUPTOR [research: innovating] | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| INTC | no | EXPENSIVE -50% (LOW) | BEING DISRUPTED [research: threatened] | revenue shrinking -6%/yr over 3 yrs; analysts see revenue +19% next year; research 2026-10-26: AMD has taken PC and server CPU share (server ~30%) and Arm designs keep gaining; offset is 18A foundry (yields ~85% per KeyBanc, outside customers reported, break-even pulled forward). Core x86 franchise still losing ground. |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| ILMN | no | DEEP VALUE +27% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 664.9 | 58.0 |  |
| RBRK | 60.5 | 55.6 | SPEC |
| CRWD | 95.1 | 51.6 |  |
| AMGN | 39.6 | 72.8 |  |
| TMO | 16.9 | 60.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| QBTS | -51.7 | 27.3 | SPEC |
| LEU | -64.4 | 34.4 | SPEC |
| APLD | -29.8 | 36.7 | SPEC |
| OKLO | -74.8 | 28.8 | SPEC |
| IREN | -32.7 | 31.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._