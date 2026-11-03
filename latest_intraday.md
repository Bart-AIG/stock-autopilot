# Strategy report - INTRADAY  (2026-11-03 17:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COP | A+ | 12/12 | #3 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 144.5 | 17.0 | 144.5 | 137.22 | 154.03 | -5.0% |
| CVX | A+ | 12/12 | #5 | 21 EMA pullback | Energy |  |  |  | 226.01 | 19.7 | 226.01 | 217.03 | 235.52 | -4.0% |
| XOM | A+ | 12/12 | #9 | 21 EMA pullback | Energy |  |  |  | 177.96 | 19.2 | 177.96 | 170.36 | 187.25 | -4.3% |
| EOG | A+ | 12/12 | #11 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 156.22 | 15.7 | 156.22 | 149.15 | 165.54 | -4.5% |
| RBRK | A+ | 11/12 | #22 | 21 EMA pullback | AI-infra | SPEC |  |  | 117.94 | 32.1 | 117.94 | 106.44 | 135.19 | -9.8% |
| CRWD | A+ | 11/12 | #23 | 21 EMA pullback | AI-software |  |  |  | 247.02 | 42.1 | 247.02 | 224.12 | 275.04 | -9.3% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** COP (2026-11-05), EOG (2026-11-05). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 4/6 setups are 'Energy' — correlated, don't buy them all.
- ⚠️ **1/6 are speculative** (high-vol). Size tiny; keep TOTAL speculative exposure ≤ ~20-25% of the account.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): PLTR (C 7/12), SHOP (C 5/12), HPQ (C 5/12), AAPL (B 9/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +315.2% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | REGN | A+ | 12/12 | +27.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COP | A+ | 12/12 | +27.8% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LLY | A+ | 12/12 | +23.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CVX | A+ | 12/12 | +23.4% | -3.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +23.0% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | WBD | A+ | 12/12 | +20.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | PFE | A+ | 12/12 | +19.8% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | XOM | A+ | 12/12 | +19.5% | -4.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | ABBV | A+ | 12/12 | +19.1% | -2.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | EOG | A+ | 12/12 | +18.6% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | MAR | A+ | 12/12 | +17.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMGN | A+ | 12/12 | +15.7% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | ADI | A+ | 12/12 | +15.6% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | TXN | A+ | 12/12 | +15.3% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | VRTX | A+ | 12/12 | +12.2% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PM | A+ | 12/12 | +12.0% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | KO | A+ | 12/12 | +11.2% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | EMR | A+ | 12/12 | +4.2% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | NUE | A+ | 12/12 | +1.9% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | TEM | A+ | 11/12 | +74.8% | -9.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | RBRK | A+ | 11/12 | +41.0% | -13.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | CRWD | A+ | 11/12 | +19.6% | -11.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | CME | B | 11/12 | +17.2% | -6.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | V | B | 11/12 | +16.3% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1239.5 | 33.7 | F |
| 2 **TOP** | MRNA | 566.9 | 61.0 | T |
| 3 **TOP** | LITE | 562.6 | 34.0 | F |
| 4 **TOP** | MU | 472.3 | 40.4 | T |
| 5 **TOP** | SOXL | 328.2 | 35.4 | F |
| 6 **TOP** | AAOI | 313.9 | 34.3 | F |
| 7 **TOP** | DELL | 299.7 | 35.4 | T |
| 8 **TOP** | AMD | 285.0 | 39.8 | T |
| 9 **TOP** | VIAV | 270.3 | 38.5 | F |
| 10 **TOP** | INTC | 224.0 | 24.0 | F |
| 11 **TOP** | MRVL | 215.8 | 28.2 | F |
| 12 **TOP** | COHR | 196.7 | 36.3 | F |
| 13 **TOP** | VLO | 153.3 | 43.1 | T |
| 14 **TOP** | MTSI | 152.4 | 41.4 | F |
| 15 **TOP** | AMAT | 148.3 | 35.8 | F |
| 16 **TOP** | LRCX | 138.3 | 33.4 | F |
| 17 **TOP** | CRWD | 120.5 | 48.5 | T |
| 18 **TOP** | MPC | 118.7 | 45.0 | T |
| 19 **TOP** | ARM | 101.4 | 35.5 | F |
| 20 **TOP** | PSX | 98.9 | 52.3 | T |
| 21 **TOP** | PANW | 94.6 | 43.9 | T |
| 22 **TOP** | NBIS | 89.7 | 36.8 | F |
| 23  | KLAC | 87.8 | 40.2 | F |
| 24  | DDOG | 82.6 | 35.4 | T |
| 25  | FCX | 81.6 | 29.6 | F |
| 26  | FCEL | 80.9 | 36.3 | F |
| 27  | TGT | 75.2 | 50.3 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | QQQ | Index-ETF | 686.55 | 35.3 | 33.4 | -4.7% | -5.2% | 24.3 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | AMZN | Other | 248.17 | 46.4 | 70.4 | -2.2% | -2.2% | 14.6 | DEEP VALUE +100% (LOW) | 493.96 | +33% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | PLTR | AI-software | 173.12 | 34.4 | 0.6 | -11.6% | -7.3% | 9.1 | EXPENSIVE -50% (LOW) | 84.7 | +38% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +86% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | AAPL | Other | 331.28 | 41.2 | 6.2 | -3.2% | -0.8% | 29.3 | EXPENSIVE -26% (HIGH) | 245.0 | +6% | STABLE | growth | disruption: gross margin up 5 pts (49%) |
| 🟢 oversold | HPQ | Other | 28.17 | 35.4 | 1.3 | -9.7% | -11.1% | 20.6 | UNDERVALUED +18% (MED) | 33.07 | -9% | AT RISK [research: threatened] | **VALUE TRAP?** growth: analysts disagree | disruption: revenue shrinking -4%/yr over 3 yrs; research 2026-10-30: Printing (its high-margin profit pool) is in structural decline (supplies and hardware volumes falling); the AI-PC refresh helps the PC side but memory costs have roughly doubled in the bill of materials. Not yet collapsing: tank printers +42%. |
| 🟡 dip | NVDA | Semis | 208.47 | 41.2 | 62.3 | -4.4% | -5.9% | 24.7 | FAIR +7% (MED) | 223.06 | +56% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | USB | Other | 60.08 | 54.8 | 47.6 | +2.5% | +0.5% | 19.6 | FAIR +2% (HIGH) | 61.64 | +13% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | SLB | Energy | 52.62 | 54.9 | 33.3 | +3.6% | +0.4% | 42.3 | FAIR -9% (HIGH) | 47.47 | +22% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-26: Core oilfield services shrinking (Q2 rev -4.5% YoY, Middle East disruption) while Data Center Solutions grew 63% in 1H26 (Meta 1GW Canada project, ~$3.4B Kelvion cooling deal) and digital ARR >$1B. Diversifying, but still mostly an oil-cycle business. |
| 🟡 dip | PNC | Other | 229.88 | 56.4 | 47.2 | +3.1% | +0.1% | 11.4 | FAIR -0% (HIGH) | 229.55 | +19% | STABLE [research: neutral] | bank | disruption: research 2026-10-29: No visible technology disruption: PNC is consolidating (FirstBank closed Jan 2026, +$850-900M NII) to compete at national scale; fintech and deposit competition are background pressures, not showing in results. |
| 🟡 dip | DELL | Other | 407.96 | 35.4 | 34.4 | -16.7% | -20.4% | 299.7 | EXPENSIVE -50% (LOW) | 205.75 | +38% | INNOVATING (quant STABLE) [research: innovating] | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| 🟡 dip | DDOG | AI-software | 219.94 | 35.4 | 20.2 | -16.8% | -12.3% | 82.6 | FAIR -10% (LOW) | 197.59 | +37% | DISRUPTOR [research: innovating] | growth: business changed (margin 8% vs 2% 10-yr median): its own history is a weak yardstick | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +31% next year; research 2026-10-30: Gains from AI workloads: LLM Observability spans up ~10x and Bits AI SRE GA with 1,000+ paying customers; FY26 revenue guide raised to ~$4.3B (+25-27%). Risk: hyperscaler native monitoring and Dynatrace/Cisco-Splunk competition. |
| 🟡 dip | NET | AI-software | 276.35 | 37.0 | 40.4 | -12.5% | -13.7% | 61.1 | EXPENSIVE -43% (LOW) | 155.67 | +28% | DISRUPTOR [research: innovating] | growth: analysts disagree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year; research 2026-10-21: Moving from CDN/security into infrastructure for AI agents (agent runtime, Agent Memory, AI Search, Workers AI inference at the edge); revenue ~+34% YoY. Competes with AWS, Google, Akamai, Fastly, Vercel on this; gains from the shift. Sources are thin secondary coverage. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +114% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -50% (LOW) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +34% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -47% (MED) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -42% (MED) | STABLE | commodity producer: revenue and margins follow the commodity price, not competitors |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 648.2 | 61.0 |  |
| COP | 44.5 | 54.3 |  |
| CVX | 30.9 | 56.7 |  |
| TMO | 19.3 | 58.5 |  |
| PFE | 11.2 | 64.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| QBTS | -57.8 | 27.2 | SPEC |
| LEU | -61.5 | 30.7 | SPEC |
| ASTS | -27.2 | 33.6 | SPEC |
| SMR | -82.9 | 32.1 | SPEC |
| CRWV | -34.6 | 33.4 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._