# Strategy report - INTRADAY  (2026-11-02 20:06 UTC)

## >>> ACTION <<<

## 📅 MONTHLY REBALANCE DUE (first trading day of the month)
Run the monthly portfolio review alongside today's signals:
- **Momentum rotate:** re-rank the 12-1 top decile (below); exit held momentum names that dropped out of the decile or broke the 200-day MA; weigh the better-play list.
- **Concentration check:** trim any position over the per-name cap (30% of account value) or the speculative sleeve over ~25%; confirm the operational reserve.
- **Cull the laggards:** this is the moment to sell underwater names whose thesis has weakened — they carry no price stop, so the monthly review is their exit gate.

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #7 | 21 EMA pullback | Other |  |  |  | 685.87 | 16.9 | 685.87 | 658.18 | 709.18 | -4.0% |
| AAPL | A+ | 12/12 | #18 | 21 EMA pullback | Other |  |  |  | 338.63 | 14.9 | 338.63 | 330.3 | 348.91 | -2.5% |
| RBRK | A+ | 11/12 | #22 | RSI2 dip | AI-infra | SPEC |  |  | 116.31 | 3.5 | 116.31 | 105.34 | 132.77 | -9.4% |

### How to read this (concentration & sizing)
- ⚠️ **1/3 are speculative** (high-vol). Size tiny; keep TOTAL speculative exposure ≤ ~20-25% of the account.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): PLTR (C 7/12), HPQ (C 5/12), DDOG (C 7/12), NET (C 4/12), MSFT (B 10/12), ZS (B 10/12), SNOW (C 4/12), CSCO (C 3/12), DELL (C 6/12), SHOP (B 9/12), CRWD (B 11/12), PANW (C 6/12), QQQ (C 4/12), AMD (C 7/12), CVS (C 3/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +293.6% | -9.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | LLY | A+ | 12/12 | +29.1% | -0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | GILD | A+ | 12/12 | +28.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | REGN | A+ | 12/12 | +28.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | COP | A+ | 12/12 | +27.4% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | PFE | A+ | 12/12 | +23.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | TMO | A+ | 12/12 | +23.5% | -3.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | CVX | A+ | 12/12 | +22.2% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | AMGN | A+ | 12/12 | +22.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WBD | A+ | 12/12 | +20.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | ABBV | A+ | 12/12 | +20.6% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | XOM | A+ | 12/12 | +19.6% | -3.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | VRTX | A+ | 12/12 | +17.6% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | MO | A+ | 12/12 | +15.7% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | PM | A+ | 12/12 | +13.7% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | KO | A+ | 12/12 | +13.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | EOG | A+ | 12/12 | +12.4% | -4.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | AAPL | A+ | 12/12 | +11.2% | -3.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | TXN | A+ | 12/12 | +9.9% | -8.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | EMR | A+ | 12/12 | +7.0% | -2.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | NUE | A+ | 12/12 | +3.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | RBRK | A+ | 11/12 | +45.3% | -14.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | MAR | A+ | 11/12 | +22.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | CME | B | 11/12 | +18.4% | -6.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | MA | B | 11/12 | +17.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 221)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1239.5 | 30.3 | F |
| 2 **TOP** | MRNA | 566.9 | 57.8 | T |
| 3 **TOP** | LITE | 562.6 | 35.2 | F |
| 4 **TOP** | MU | 472.3 | 37.7 | T |
| 5 **TOP** | SOXL | 328.2 | 32.1 | F |
| 6 **TOP** | AAOI | 313.9 | 33.6 | F |
| 7 **TOP** | DELL | 299.7 | 32.7 | T |
| 8 **TOP** | AMD | 285.0 | 35.4 | T |
| 9 **TOP** | VIAV | 270.3 | 33.3 | F |
| 10 **TOP** | INTC | 224.0 | 23.1 | F |
| 11 **TOP** | MRVL | 215.8 | 28.7 | F |
| 12 **TOP** | COHR | 196.7 | 33.0 | F |
| 13 **TOP** | VLO | 153.3 | 41.0 | T |
| 14 **TOP** | MTSI | 152.4 | 35.6 | F |
| 15 **TOP** | AMAT | 148.3 | 33.9 | F |
| 16 **TOP** | LRCX | 138.3 | 30.5 | F |
| 17 **TOP** | CRWD | 120.5 | 46.1 | T |
| 18 **TOP** | MPC | 118.7 | 47.6 | T |
| 19 **TOP** | ARM | 101.4 | 33.3 | F |
| 20 **TOP** | PSX | 98.9 | 51.2 | T |
| 21 **TOP** | PANW | 94.6 | 43.0 | T |
| 22 **TOP** | NBIS | 89.7 | 32.8 | F |
| 23  | KLAC | 87.8 | 38.1 | F |
| 24  | DDOG | 82.6 | 34.5 | T |
| 25  | FCX | 81.6 | 33.3 | F |
| 26  | FCEL | 80.9 | 33.1 | F |
| 27  | TGT | 75.2 | 57.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QQQ | Index-ETF | 685.63 | 33.4 | 6.5 | -5.4% | -5.4% | 24.3 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | AMZN | Other | 248.49 | 46.5 | 65.4 | -2.3% | -2.2% | 14.6 | DEEP VALUE +100% (LOW) | 500.36 | +32% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | DELL | Other | 401.2 | 32.7 | 4.6 | -19.5% | -21.8% | 299.7 | EXPENSIVE -50% (LOW) | 206.79 | +38% | INNOVATING (quant STABLE) [research: innovating] | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| 🟢 oversold | NET | AI-software | 268.6 | 32.8 | 2.0 | -16.1% | -16.1% | 61.1 | EXPENSIVE -41% (LOW) | 155.49 | +32% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |
| 🟢 oversold | DDOG | AI-software | 219.9 | 34.5 | 1.8 | -17.8% | -12.4% | 82.6 | RICH -11% (LOW) | 197.95 | +34% | DISRUPTOR [research: innovating] | growth: business changed (margin 8% vs 2% 10-yr median): its own history is a weak yardstick; analysts disagree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +31% next year; research 2026-10-30: Gains from AI workloads: LLM Observability spans up ~10x and Bits AI SRE GA with 1,000+ paying customers; FY26 revenue guide raised to ~$4.3B (+25-27%). Risk: hyperscaler native monitoring and Dynatrace/Cisco-Splunk competition. |
| 🟢 oversold | SNOW | AI-software | 291.16 | 35.1 | 3.3 | -12.0% | -12.1% | 45.1 | UNDERVALUED +14% (LOW) | 341.13 | +46% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | AMD | Semis | 473.81 | 35.4 | 6.9 | -15.8% | -13.6% | 285.0 | EXPENSIVE -32% (LOW) | 340.93 | +29% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (26% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| 🟢 oversold | PLTR | AI-software | 181.19 | 39.7 | 1.3 | -8.0% | -3.1% | 9.1 | EXPENSIVE -50% (LOW) | 91.96 | +25% | DISRUPTOR | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +84% next year |
| 🟢 oversold | SPY | Index-ETF | 755.2 | 39.9 | 9.0 | -1.9% | -1.6% | 15.0 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | PANW | AI-software | 354.67 | 43.0 | 6.1 | -6.5% | -4.7% | 94.6 | EXPENSIVE -50% (LOW) | 177.92 | +17% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | CVS | Other | 88.97 | 43.4 | 7.2 | -1.8% | -2.4% | 11.6 | EXPENSIVE -26% (LOW) | 65.6 | +26% | STABLE [research: neutral] | steady: business changed (margin 3% vs 6% 10-yr median): its own history is a weak yardstick; analysts disagree | disruption: gross margin slipping 3 pts (14%); research 2026-10-28: Turnaround led by Aetna margin recovery (MLR 87.4% vs 89.9%); 2026 EPS guide raised twice to $7.90-8.10. PBM business-model transition flagged as a 2027 headwind; no clear tech obsolescence found in this check. |
| 🟢 oversold | CRWD | AI-software | 242.92 | 46.1 | 6.0 | -4.2% | +0.7% | 120.5 | EXPENSIVE -44% (LOW) | 136.42 | -0% | DISRUPTOR [research: innovating] | preprofit: analysts agree | disruption: revenue +29%/yr over 3 yrs; analysts see revenue +25% next year; research 2026-10-21: Endpoint security leader adding AI-agent security; Microsoft Defender/Security Copilot bundling is the standing competitive threat (CEO: 'Microsoft is always going to be a competitor'), not obsolescence. Evidence on new-market creation is thin. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +110% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -50% (LOW) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +38% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -48% (MED) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -50% (MED) | STABLE | commodity producer: revenue and margins follow the commodity price, not competitors |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 575.2 | 57.8 |  |
| GILD | 22.2 | 74.6 |  |
| COP | 43.8 | 59.6 |  |
| PFE | 14.5 | 69.6 |  |
| TMO | 17.7 | 54.0 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| QBTS | -56.3 | 25.1 | SPEC |
| LEU | -63.7 | 30.9 | SPEC |
| APLD | -25.2 | 33.3 | SPEC |
| ASTS | -23.8 | 31.0 | SPEC |
| IREN | -28.3 | 28.0 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._