# Strategy report - MORNING  (2026-11-03 15:12 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COP | A+ | 12/12 | #3 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 144.71 | 17.5 | 144.71 | 137.45 | 154.03 | -5.0% |
| CVX | A+ | 12/12 | #5 | 21 EMA pullback | Energy |  |  |  | 225.72 | 18.9 | 225.72 | 216.72 | 235.52 | -4.0% |
| XOM | A+ | 12/12 | #9 | 21 EMA pullback | Energy |  |  |  | 178.34 | 20.3 | 178.34 | 170.76 | 187.25 | -4.2% |
| EOG | A+ | 12/12 | #11 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 156.03 | 15.3 | 156.03 | 148.95 | 165.54 | -4.5% |
| RBRK | A+ | 11/12 | #22 | 21 EMA pullback | AI-infra | SPEC |  |  | 117.58 | 29.8 | 117.58 | 106.14 | 134.72 | -9.7% |
| CRWD | A+ | 11/12 | #23 | 21 EMA pullback | AI-software |  |  |  | 248 | 46.0 | 248 | 224.91 | 275.04 | -9.3% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** COP (2026-11-05), EOG (2026-11-05). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 🟡 **Cluster:** 4/6 setups are 'Energy' — correlated, don't buy them all.
- ⚠️ **1/6 are speculative** (high-vol). Size tiny; keep TOTAL speculative exposure ≤ ~20-25% of the account.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): PLTR (C 7/12), SHOP (C 5/12), HPQ (C 5/12), ZS (B 10/12), SNOW (C 4/12), AAPL (B 10/12), UNH (C 8/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +312.7% | -6.0% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | REGN | A+ | 12/12 | +28.1% | 0.0% | RICH -14% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COP | A+ | 12/12 | +27.9% | -6.1% | RICH -20% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LLY | A+ | 12/12 | +24.4% | 0.0% | RICH -15% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CVX | A+ | 12/12 | +23.2% | -4.2% | RICH -20% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +22.5% | -2.0% | RICH -19% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | PFE | A+ | 12/12 | +21.7% | 0.0% | EXPENSIVE -36% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +20.6% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | XOM | A+ | 12/12 | +19.7% | -4.8% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | ABBV | A+ | 12/12 | +19.6% | -1.9% | EXPENSIVE -42% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | EOG | A+ | 12/12 | +18.4% | -5.7% | FAIR -4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | MAR | A+ | 12/12 | +17.5% | 0.0% | EXPENSIVE -31% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMGN | A+ | 12/12 | +16.4% | 0.0% | EXPENSIVE -31% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | ADI | A+ | 12/12 | +14.5% | -4.7% | EXPENSIVE -47% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | VRTX | A+ | 12/12 | +14.1% | -2.8% | RICH -20% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | TXN | A+ | 12/12 | +12.5% | -7.8% | EXPENSIVE -35% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PM | A+ | 12/12 | +12.2% | -0.4% | EXPENSIVE -33% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | KO | A+ | 12/12 | +10.9% | -1.4% | FAIR -2% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | EMR | A+ | 12/12 | +4.4% | -2.7% | EXPENSIVE -32% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | NUE | A+ | 12/12 | +2.7% | -0.5% | EXPENSIVE -37% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | TEM | A+ | 11/12 | +76.1% | -8.4% | DEEP VALUE +75% (LOW) | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | RBRK | A+ | 11/12 | +40.8% | -13.5% | EXPENSIVE -27% (LOW) | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | CRWD | A+ | 11/12 | +20.3% | -11.1% | EXPENSIVE -45% (LOW) | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | V | B | 11/12 | +16.3% | -1.1% | RICH -12% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | CME | B | 11/12 | +16.2% | -7.5% | FAIR +8% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1239.5 | 33.9 | F |
| 2 **TOP** | MRNA | 566.9 | 60.5 | T |
| 3 **TOP** | LITE | 562.6 | 35.4 | F |
| 4 **TOP** | MU | 472.3 | 41.2 | T |
| 5 **TOP** | SOXL | 328.2 | 34.7 | F |
| 6 **TOP** | AAOI | 313.9 | 35.5 | F |
| 7 **TOP** | DELL | 299.7 | 36.2 | T |
| 8 **TOP** | AMD | 285.0 | 39.2 | T |
| 9 **TOP** | VIAV | 270.3 | 37.1 | F |
| 10 **TOP** | INTC | 224.0 | 25.5 | F |
| 11 **TOP** | MRVL | 215.8 | 28.8 | F |
| 12 **TOP** | COHR | 196.7 | 36.6 | F |
| 13 **TOP** | VLO | 153.3 | 39.3 | T |
| 14 **TOP** | MTSI | 152.4 | 41.0 | F |
| 15 **TOP** | AMAT | 148.3 | 36.6 | F |
| 16 **TOP** | LRCX | 138.3 | 33.3 | F |
| 17 **TOP** | CRWD | 120.5 | 49.0 | T |
| 18 **TOP** | MPC | 118.7 | 43.0 | T |
| 19 **TOP** | ARM | 101.4 | 36.0 | F |
| 20 **TOP** | PSX | 98.9 | 47.4 | T |
| 21 **TOP** | PANW | 94.6 | 44.1 | T |
| 22 **TOP** | NBIS | 89.7 | 36.4 | F |
| 23  | KLAC | 87.8 | 39.0 | F |
| 24  | DDOG | 82.6 | 34.6 | T |
| 25  | FCX | 81.6 | 30.6 | F |
| 26  | FCEL | 80.9 | 38.0 | F |
| 27  | TGT | 75.2 | 54.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QQQ | Index-ETF | 684.62 | 34.2 | 25.6 | -5.0% | -5.4% | 24.3 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | AMZN | Other | 247.03 | 45.3 | 65.3 | -2.6% | -2.6% | 14.6 | DEEP VALUE +100% (LOW) | 493.96 | +33% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | PLTR | AI-software | 170.06 | 32.7 | 0.4 | -13.1% | -8.9% | 9.1 | EXPENSIVE -50% (LOW) | 84.7 | +38% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +86% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | DDOG | AI-software | 218.11 | 34.6 | 10.9 | -17.4% | -13.0% | 82.6 | FAIR -10% (LOW) | 197.59 | +37% | DISRUPTOR [research: innovating] | growth: business changed (margin 8% vs 2% 10-yr median): its own history is a weak yardstick | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +31% next year; research 2026-10-30: Gains from AI workloads: LLM Observability spans up ~10x and Bits AI SRE GA with 1,000+ paying customers; FY26 revenue guide raised to ~$4.3B (+25-27%). Risk: hyperscaler native monitoring and Dynatrace/Cisco-Splunk competition. |
| 🟢 oversold | SNOW | AI-software | 290.53 | 34.9 | 3.1 | -11.5% | -12.1% | 45.1 | UNDERVALUED +17% (LOW) | 341.13 | +50% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | AAPL | Other | 331.3 | 41.2 | 6.2 | -3.2% | -0.8% | 29.3 | EXPENSIVE -26% (HIGH) | 245.0 | +6% | STABLE | growth | disruption: gross margin up 5 pts (49%) |
| 🟢 oversold | HPQ | Other | 28.21 | 35.5 | 1.3 | -9.6% | -11.0% | 20.6 | UNDERVALUED +18% (MED) | 33.07 | -9% | AT RISK [research: threatened] | **VALUE TRAP?** growth: analysts disagree | disruption: revenue shrinking -4%/yr over 3 yrs; research 2026-10-30: Printing (its high-margin profit pool) is in structural decline (supplies and hardware volumes falling); the AI-PC refresh helps the PC side but memory costs have roughly doubled in the bill of materials. Not yet collapsing: tank printers +42%. |
| 🟡 dip | NVDA | Semis | 207.77 | 40.4 | 59.6 | -4.7% | -6.2% | 24.7 | FAIR +7% (MED) | 223.06 | +56% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | OXY | Energy | 60.47 | 46.2 | 13.0 | -2.4% | +0.5% | 29.5 | FAIR +9% (HIGH) | 66.11 | +17% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟡 dip | SLB | Energy | 52.38 | 53.9 | 15.5 | +3.1% | -0.1% | 42.3 | FAIR -9% (HIGH) | 47.47 | +22% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-26: Core oilfield services shrinking (Q2 rev -4.5% YoY, Middle East disruption) while Data Center Solutions grew 63% in 1H26 (Meta 1GW Canada project, ~$3.4B Kelvion cooling deal) and digital ARR >$1B. Diversifying, but still mostly an oil-cycle business. |
| 🟡 dip | USB | Other | 60.38 | 56.8 | 61.3 | +3.0% | +1.0% | 19.6 | FAIR +2% (HIGH) | 61.64 | +13% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | PNC | Other | 230.22 | 57.0 | 50.5 | +3.3% | +0.3% | 11.4 | FAIR -0% (HIGH) | 229.55 | +19% | STABLE [research: neutral] | bank | disruption: research 2026-10-29: No visible technology disruption: PNC is consolidating (FirstBank closed Jan 2026, +$850-900M NII) to compete at national scale; fintech and deposit competition are background pressures, not showing in results. |

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

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #211 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #235 | N/A | INNOVATING |
| Drones | UMAC | C 2/12 #154 | N/A | N/A |
| Drones | UAVS | C 0/12 #229 | N/A | AT RISK |
| Drones | ONDS | C 1/12 #178 | DEEP VALUE +81% (LOW) | DISRUPTOR |
| Drones | DPRO | C 2/12 #153 | FAIR +6% (LOW) | AT RISK |
| Drones | KTOS | C 0/12 #206 | RICH -25% (LOW) | INNOVATING |
| Drones | AVAV | C 0/12 #204 | DEEP VALUE +40% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #232 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #169 | FAIR +0% (HIGH) | STABLE |
| Raw materials | SCCO | C 2/12 #145 | EXPENSIVE -36% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #163 | RICH -20% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #175 | EXPENSIVE -37% (LOW) | STABLE |
| Raw materials | FCX | C 2/12 #146 | EXPENSIVE -31% (MED) | STABLE |
| Growth opportunities | NBIS | C 1/12 #177 | EXPENSIVE -50% (LOW) | DISRUPTOR [research: disruptor] |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 648.2 | 60.5 |  |
| COP | 44.5 | 54.1 |  |
| CVX | 30.9 | 55.6 |  |
| TMO | 19.3 | 57.2 |  |
| PFE | 11.2 | 69.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| QBTS | -57.8 | 27.9 | SPEC |
| LEU | -61.5 | 34.1 | SPEC |
| ASTS | -27.2 | 34.3 | SPEC |
| OKLO | -72.9 | 27.3 | SPEC |
| APLD | -28.7 | 37.4 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._