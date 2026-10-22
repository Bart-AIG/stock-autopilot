# Strategy report - MORNING  (2026-10-22 14:10 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPC | A+ | 12/12 | #2 | RSI2 dip | Energy |  |  | ⚠️ 2026-11-03 | 461.92 | 6.5 | 461.92 | 437.12 | 484.92 | -5.4% |
| VLO | A+ | 12/12 | #3 | 21 EMA pullback | Energy |  |  |  | 426.31 | 13.8 | 426.31 | 401.27 | 459.78 | -5.9% |
| MSFT | A+ | 11/12 | #17 | 21 EMA pullback | Other |  |  |  | 526.0 | 14.2 | 526.0 | 508.0 | 543.45 | -3.4% |
| DVN | A+ | 11/12 | #21 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 49.55 | 15.0 | 49.55 | 47.53 | 50.92 | -4.1% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MPC (2026-11-03), DVN (2026-11-05). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 3/4 setups are 'Energy' — correlated, don't buy them all.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): FCX (C 3/12), SCCO (C 3/12), META (C 6/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +336.9% | -3.1% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +45.6% | -4.7% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +37.1% | -7.3% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +36.3% | -2.6% | EXPENSIVE -45% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | PFE | A+ | 12/12 | +19.4% | 0.0% | EXPENSIVE -31% (MED) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +17.3% | -1.2% | RICH -18% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | COP | A+ | 12/12 | +17.0% | -0.9% | RICH -20% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | AMGN | A+ | 12/12 | +14.8% | 0.0% | EXPENSIVE -28% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WBD | A+ | 12/12 | +14.7% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | CVX | A+ | 12/12 | +12.1% | -0.5% | EXPENSIVE -27% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | KO | A+ | 12/12 | +10.5% | 0.0% | FAIR -4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | XOM | A+ | 12/12 | +9.1% | -1.0% | EXPENSIVE -38% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +5.5% | -1.9% | EXPENSIVE -46% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | LLY | A+ | 12/12 | +5.0% | 0.0% | FAIR -8% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +3.8% | -0.3% | FAIR -5% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PLTR | A+ | 11/12 | +59.5% | -4.0% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MSFT | A+ | 11/12 | +34.0% | -3.2% | RICH -15% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MA | A+ | 11/12 | +12.3% | 0.0% | FAIR +4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | V | A+ | 11/12 | +11.6% | 0.0% | RICH -12% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | VRTX | A+ | 11/12 | +7.0% | -5.2% | FAIR -8% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | DVN | A+ | 11/12 | +6.2% | -4.8% | RICH -16% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | OXY | A+ | 11/12 | +5.4% | -5.6% | FAIR +6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | MAR | A+ | 11/12 | +3.6% | -0.5% | EXPENSIVE -30% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | AAPL | B | 11/12 | -0.1% | 0.0% | EXPENSIVE -36% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | PM | B | 11/12 | -0.7% | -3.2% | EXPENSIVE -31% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 587.3 | 65.1 | T |
| 2 **TOP** | MU | 565.9 | 39.2 | T |
| 3 **TOP** | LITE | 474.1 | 37.2 | T |
| 4 **TOP** | INTC | 330.7 | 32.7 | T |
| 5 **TOP** | DELL | 304.5 | 39.3 | T |
| 6 **TOP** | AMD | 290.4 | 39.8 | T |
| 7 **TOP** | AAOI | 250.4 | 32.4 | F |
| 8 **TOP** | MRVL | 247.4 | 42.4 | T |
| 9 **TOP** | VIAV | 194.0 | 35.4 | F |
| 10 **TOP** | COHR | 170.8 | 31.5 | F |
| 11 **TOP** | AMAT | 135.6 | 27.4 | F |
| 12 **TOP** | LRCX | 135.2 | 26.7 | F |
| 13 **TOP** | ARM | 130.6 | 33.0 | F |
| 14 **TOP** | VLO | 126.6 | 54.9 | T |
| 15 **TOP** | NBIS | 121.5 | 31.2 | F |
| 16 **TOP** | MTSI | 116.0 | 38.6 | F |
| 17 **TOP** | MPC | 108.1 | 62.6 | T |
| 18 **TOP** | CRWD | 102.8 | 45.7 | T |
| 19 **TOP** | PSX | 98.2 | 66.1 | T |
| 20 **TOP** | MRK | 87.7 | 61.8 | T |
| 21 **TOP** | SCCO | 87.2 | 36.4 | T |
| 22 **TOP** | FCEL | 86.0 | 37.0 | F |
| 23  | TGT | 83.7 | 44.6 | T |
| 24  | NUE | 82.4 | 51.8 | T |
| 25  | PANW | 79.9 | 43.9 | T |
| 26  | DDOG | 78.9 | 50.4 | T |
| 27  | KLAC | 75.8 | 26.7 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | NVDA | Semis | 216.69 | 42.7 | 34.7 | -4.3% | -2.8% | 24.7 | FAIR +3% (MED) | 223.05 | +50% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | MU | Semis | 903.17 | 39.2 | 42.5 | -9.6% | -8.3% | 565.9 | EXPENSIVE -50% (LOW) | 450.29 | +67% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | QQQ | Index-ETF | 714.35 | 40.5 | 28.0 | -3.2% | -1.7% | 24.1 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MRVL | Semis | 234.84 | 42.4 | 27.0 | -9.3% | -3.4% | 247.4 | EXPENSIVE -50% (LOW) | 116.84 | +48% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | AMZN | Other | 253.39 | 47.6 | 14.7 | -0.5% | -1.0% | 12.0 | DEEP VALUE +100% (LOW) | 507.0 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | ASND | Other | 240.63 | 57.2 | 97.6 | +5.2% | -0.8% | 21.0 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +98% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | FCX | Other | 66.3 | 34.8 | 2.0 | -6.4% | -7.9% | 64.6 | EXPENSIVE -38% (HIGH) | 41.2 | +14% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | SCCO | Other | 188.59 | 36.4 | 2.9 | -6.7% | -6.3% | 87.2 | EXPENSIVE -40% (HIGH) | 112.91 | -10% | STABLE | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | INTC | Semis | 88.62 | 32.7 | 15.7 | -16.4% | -13.6% | 330.7 | EXPENSIVE -50% (LOW) | 44.33 | +24% | BEING DISRUPTED | cyclical: TROUGH-CYCLE margins (6% vs 41% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| 🟡 dip | QCOM | Semis | 176.86 | 48.4 | 56.6 | -1.6% | +0.5% | 16.8 | FAIR -4% (HIGH) | 171.16 | +10% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | USB | Other | 59.81 | 56.4 | 89.2 | +3.5% | -1.0% | 20.1 | FAIR +3% (HIGH) | 61.64 | +14% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | DELL | Other | 467.9 | 39.3 | 39.8 | -11.8% | -9.0% | 304.5 | EXPENSIVE -50% (LOW) | 234.85 | +21% | STABLE | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| 🟡 dip | AMD | Semis | 527.64 | 39.8 | 26.2 | -11.2% | -2.6% | 290.4 | EXPENSIVE -33% (LOW) | 349.77 | +22% | DISRUPTOR | cyclical: PEAK-CYCLE margins (26% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| 🟡 dip | SNOW | AI-software | 311.43 | 40.9 | 21.8 | -7.1% | -6.2% | 46.6 | FAIR +9% (LOW) | 341.13 | +39% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | NET | AI-software | 307.31 | 42.5 | 70.2 | -8.3% | -3.8% | 54.6 | EXPENSIVE -50% (LOW) | 156.02 | +12% | DISRUPTOR [research: innovating] | preprofit: far from its own history: the market has re-rated it, find out why | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟡 dip | NEM | Other | 114.01 | 43.2 | 12.1 | -1.9% | -6.4% | 52.0 | EXPENSIVE -32% (LOW) | 76.97 | +23% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (65% vs 33% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-12: Largest gold producer; results follow the gold price, no technology shift threatens or expands its market. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (LOW) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | no | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +50% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -33% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| INTC | no | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -49% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| ILMN | no | FAIR +7% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | AVAV | C 0/12 #217 | DEEP VALUE +49% (LOW) | AT RISK |
| Drones | DPRO | C 2/12 #151 | FAIR +0% (LOW) | AT RISK |
| Drones | EH | C 0/12 #226 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | KTOS | C 0/12 #209 | RICH -20% (LOW) | INNOVATING |
| Drones | ONDS | C 0/12 #215 | DEEP VALUE +76% (LOW) | DISRUPTOR |
| Drones | RCAT | C 0/12 #235 | DEEP VALUE +100% (LOW) | AT RISK |
| Drones | UAVS | C 2/12 #148 | N/A | AT RISK |
| Drones | UMAC | C 1/12 #171 | N/A | N/A |
| Drones | ZENA | C 0/12 #224 | N/A | INNOVATING |
| Raw materials | BHP | C 1/12 #161 | RICH -21% (MED) | STABLE |
| Raw materials | CENX | C 1/12 #181 | EXPENSIVE -35% (LOW) | STABLE |
| Raw materials | FCX | C 3/12 #119 | EXPENSIVE -38% (HIGH) | STABLE |
| Raw materials | RIO | C 1/12 #162 | FAIR -2% (HIGH) | STABLE |
| Raw materials | SCCO | C 3/12 #118 | EXPENSIVE -40% (HIGH) | STABLE |
| Growth opportunities | NBIS | C 1/12 #167 | EXPENSIVE -50% (LOW) | DISRUPTOR [research: disruptor] |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 562.5 | 65.1 |  |
| MPC | 112.4 | 62.6 |  |
| VLO | 138.3 | 54.9 |  |
| PSX | 99.4 | 66.1 |  |
| PFE | 13.4 | 70.8 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -59.9 | 28.5 | SPEC |
| SMR | -77.4 | 25.9 | SPEC |
| OKLO | -72.2 | 28.2 | SPEC |
| IREN | -14.8 | 25.7 | SPEC |
| ASTS | -23.7 | 29.2 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._