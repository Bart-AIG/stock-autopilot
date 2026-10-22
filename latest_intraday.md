# Strategy report - INTRADAY  (2026-10-22 17:55 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPC | A+ | 12/12 | #1 | RSI2 dip | Energy |  |  | ⚠️ 2026-11-03 | 458.92 | 5.1 | 458.92 | 433.87 | 484.92 | -5.5% |
| VLO | A+ | 12/12 | #2 | 21 EMA pullback | Energy |  |  |  | 423.46 | 11.5 | 423.46 | 398.11 | 459.78 | -6.0% |
| PSX | A+ | 12/12 | #3 | RSI2 dip | Energy |  |  |  | 281.78 | 5.6 | 281.78 | 268.87 | 297.29 | -4.6% |
| MRNA | A+ | 11/12 | #18 | 21 EMA pullback | Other |  |  | 2026-11-06 | 184.75 | 10.5 | 184.75 | 149.11 | 238.22 | -19.3% ⚠ |
| MSFT | A+ | 11/12 | #20 | 21 EMA pullback | Other |  |  |  | 523.98 | 11.7 | 523.98 | 505.72 | 543.45 | -3.5% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MPC (2026-11-03). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 3/5 setups are 'Energy' — correlated, don't buy them all.
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): META (C 6/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MPC | A+ | 12/12 | +45.0% | -5.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | VLO | A+ | 12/12 | +36.4% | -8.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | PSX | A+ | 12/12 | +32.8% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PFE | A+ | 12/12 | +19.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | COP | A+ | 12/12 | +18.3% | -0.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +16.5% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | AMGN | A+ | 12/12 | +16.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +15.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | CVX | A+ | 12/12 | +12.9% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | KO | A+ | 12/12 | +12.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | XOM | A+ | 12/12 | +9.7% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | LLY | A+ | 12/12 | +6.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +6.5% | -1.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | OXY | A+ | 12/12 | +5.9% | -5.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +4.6% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PM | A+ | 12/12 | +1.2% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AAPL | A+ | 12/12 | +0.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MRNA | A+ | 11/12 | +235.6% | -25.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PLTR | A+ | 11/12 | +57.6% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +34.0% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MA | A+ | 11/12 | +13.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | V | A+ | 11/12 | +13.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | VRTX | A+ | 11/12 | +8.8% | -4.1% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | DVN | B | 11/12 | +6.4% | -5.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | MAR | B | 11/12 | +3.1% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 587.3 | 45.6 | T |
| 2 **TOP** | MU | 565.9 | 35.4 | T |
| 3 **TOP** | LITE | 474.1 | 34.6 | F |
| 4 **TOP** | INTC | 330.7 | 31.1 | T |
| 5 **TOP** | DELL | 304.5 | 36.9 | T |
| 6 **TOP** | AMD | 290.4 | 37.0 | T |
| 7 **TOP** | AAOI | 250.4 | 30.3 | F |
| 8 **TOP** | MRVL | 247.4 | 38.3 | T |
| 9 **TOP** | VIAV | 194.0 | 32.1 | F |
| 10 **TOP** | COHR | 170.8 | 29.5 | F |
| 11 **TOP** | AMAT | 135.6 | 26.0 | F |
| 12 **TOP** | LRCX | 135.2 | 24.9 | F |
| 13 **TOP** | ARM | 130.6 | 31.7 | F |
| 14 **TOP** | VLO | 126.6 | 53.0 | T |
| 15 **TOP** | NBIS | 121.5 | 29.7 | F |
| 16 **TOP** | MTSI | 116.0 | 34.7 | F |
| 17 **TOP** | MPC | 108.1 | 60.4 | T |
| 18 **TOP** | CRWD | 102.8 | 45.9 | T |
| 19 **TOP** | PSX | 98.2 | 56.5 | T |
| 20 **TOP** | MRK | 87.7 | 53.9 | T |
| 21 **TOP** | SCCO | 87.2 | 32.9 | F |
| 22 **TOP** | FCEL | 86.0 | 34.4 | F |
| 23  | TGT | 83.7 | 48.5 | T |
| 24  | NUE | 82.4 | 55.3 | T |
| 25  | PANW | 79.9 | 43.5 | T |
| 26  | DDOG | 78.9 | 49.7 | T |
| 27  | KLAC | 75.8 | 24.5 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | NVDA | Semis | 212.73 | 39.4 | 24.2 | -6.0% | -4.5% | 24.7 | FAIR +3% (MED) | 223.05 | +50% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | MU | Semis | 864.98 | 35.4 | 18.7 | -13.3% | -12.1% | 565.9 | EXPENSIVE -50% (LOW) | 450.29 | +67% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | QQQ | Index-ETF | 705.58 | 36.9 | 18.6 | -4.3% | -2.9% | 24.1 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MRVL | Semis | 223.46 | 38.3 | 15.3 | -13.5% | -8.0% | 247.4 | EXPENSIVE -50% (LOW) | 116.84 | +48% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | AMZN | Other | 250.62 | 45.3 | 11.8 | -1.5% | -2.1% | 12.0 | DEEP VALUE +100% (LOW) | 507.0 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | ASND | Other | 242.07 | 58.4 | 98.1 | +5.8% | -0.2% | 21.0 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +98% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | INTC | Semis | 86.39 | 31.1 | 11.1 | -18.4% | -15.7% | 330.7 | EXPENSIVE -50% (LOW) | 44.33 | +24% | BEING DISRUPTED | cyclical: TROUGH-CYCLE margins (6% vs 41% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| 🟡 dip | QCOM | Semis | 173.45 | 45.0 | 29.1 | -3.4% | -1.4% | 16.8 | FAIR -4% (HIGH) | 171.16 | +10% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | USB | Other | 59.93 | 57.0 | 90.1 | +3.6% | -0.8% | 20.1 | FAIR +3% (HIGH) | 61.64 | +14% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | DELL | Other | 452.21 | 36.9 | 27.6 | -14.6% | -12.0% | 304.5 | EXPENSIVE -50% (LOW) | 234.85 | +21% | STABLE | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| 🟡 dip | AMD | Semis | 511.31 | 37.0 | 18.5 | -13.8% | -5.6% | 290.4 | EXPENSIVE -33% (LOW) | 349.77 | +22% | DISRUPTOR | cyclical: PEAK-CYCLE margins (26% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| 🟡 dip | SNOW | AI-software | 311.83 | 41.1 | 22.6 | -6.9% | -6.0% | 46.6 | FAIR +9% (LOW) | 341.13 | +39% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | NET | AI-software | 306.28 | 42.1 | 64.7 | -8.6% | -4.1% | 54.6 | EXPENSIVE -50% (LOW) | 156.02 | +12% | DISRUPTOR [research: innovating] | preprofit: far from its own history: the market has re-rated it, find out why | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟡 dip | PANW | AI-software | 355.29 | 43.5 | 75.0 | -7.5% | -4.1% | 79.9 | EXPENSIVE -50% (LOW) | 179.6 | +16% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟡 dip | SPY | Index-ETF | 762.9 | 44.4 | 22.8 | -1.0% | -0.7% | 16.0 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | DIA | Index-ETF | 526.86 | 60.8 | 76.0 | +2.0% | +0.7% | 11.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

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

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MPC | 112.4 | 60.4 |  |
| VLO | 138.3 | 53.0 |  |
| PSX | 99.4 | 56.5 |  |
| PFE | 13.4 | 70.6 |  |
| COP | 48.2 | 71.8 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -59.9 | 27.3 | SPEC |
| OKLO | -72.2 | 27.6 | SPEC |
| SMR | -77.4 | 25.6 | SPEC |
| ASTS | -23.7 | 27.9 | SPEC |
| APLD | -16.3 | 35.1 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._