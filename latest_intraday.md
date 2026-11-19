# Strategy report - INTRADAY  (2026-11-19 21:16 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAR | A+ | 12/12 | #2 | 21 EMA pullback | Other |  |  |  | 414.04 | 13.5 | 414.04 | 397.72 | 429.18 | -3.9% |
| MO | A+ | 12/12 | #4 | RSI2 dip | Other |  |  |  | 74.68 | 4.3 | 74.68 | 71.53 | 78.9 | -4.2% |
| V | A+ | 12/12 | #5 | RSI2 dip | Other |  |  |  | 402.25 | 2.9 | 402.25 | 384.33 | 429.12 | -4.5% |
| LLY | A+ | 12/12 | #6 | RSI2 dip | Other |  |  |  | 1351.24 | 2.7 | 1351.24 | 1271.86 | 1443.5 | -5.9% |
| ABBV | A+ | 12/12 | #7 | RSI2 dip | Other |  |  |  | 283.49 | 1.2 | 283.49 | 274.37 | 295.03 | -3.2% |
| CME | A+ | 11/12 | #12 | RSI2 dip | Other |  |  |  | 306.31 | 6.7 | 306.31 | 294.39 | 319.37 | -3.9% |
| REGN | A+ | 11/12 | #13 | RSI2 dip | Other |  |  |  | 923.34 | 7.5 | 923.34 | 841.67 | 973.36 | -8.8% |
| TMO | A+ | 11/12 | #14 | 21 EMA pullback | Other |  |  |  | 688.87 | 32.0 | 688.87 | 656.72 | 721.63 | -4.7% |
| MA | A+ | 11/12 | #15 | RSI2 dip | Other |  |  |  | 626.5 | 3.0 | 626.5 | 596.38 | 671.68 | -4.8% |
| KO | A+ | 11/12 | #16 | RSI2 dip | Other |  |  |  | 96.09 | 6.0 | 96.09 | 93.16 | 99.48 | -3.0% |
| LIN | A+ | 11/12 | #17 | RSI2 dip | Other |  |  |  | 510.21 | 5.3 | 510.21 | 496.16 | 526.55 | -2.8% |
| ASND | A+ | 11/12 | #19 | RSI2 dip | Other |  |  |  | 255.96 | 5.1 | 255.96 | 243.81 | 274.19 | -4.7% |
| AMGN | A+ | 11/12 | #20 | RSI2 dip | Other |  |  |  | 438.82 | 0.5 | 438.82 | 420.79 | 465.87 | -4.1% |
| BLK | A+ | 11/12 | #21 | RSI2 dip | Other |  |  |  | 1135.81 | 1.5 | 1135.81 | 1074.07 | 1226.31 | -5.4% |
| GILD | A | 10/12 | #22 | 21 EMA pullback | Other |  |  |  | 166.53 | 17.9 | 166.53 | 158.56 | 174.48 | -4.8% |
| AAPL | A | 10/12 | #23 | 21 EMA pullback | Other |  |  |  | 349.21 | 11.4 | 349.21 | 334.48 | 356.27 | -4.2% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): DE (C 4/12), MRK (C 3/12), PFE (B 8/12), SHOP (C 6/12), PM (C 6/12), TEM (C 5/12), JNJ (B 7/12), MPC (B 7/12), MMM (B 10/12), WDAY (C 3/12), PYPL (B 7/12), ABNB (B 10/12), PSX (C 5/12), XOM (B 7/12), VLO (C 5/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +25.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +22.7% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COST | A+ | 12/12 | +21.9% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MO | A+ | 12/12 | +19.5% | -5.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | V | A+ | 12/12 | +15.0% | -7.8% | FAIR -9% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | LLY | A+ | 12/12 | +14.1% | -6.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | ABBV | A+ | 12/12 | +13.5% | -3.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | DLTR | A+ | 12/12 | +13.2% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WMT | A+ | 11/12 | +28.1% | -6.1% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PG | A+ | 11/12 | +22.6% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | DIS | A+ | 11/12 | +18.1% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | CME | A+ | 11/12 | +17.9% | -6.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | REGN | A+ | 11/12 | +17.2% | -5.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 14 | TMO | A+ | 11/12 | +16.0% | -4.5% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | MA | A+ | 11/12 | +14.5% | -6.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 16 | KO | A+ | 11/12 | +12.0% | -3.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 17 | LIN | A+ | 11/12 | +11.2% | -6.7% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | TGT | A+ | 11/12 | +7.8% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 19 | ASND | A+ | 11/12 | +7.6% | -7.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | AMGN | A+ | 11/12 | +6.4% | -8.3% | EXPENSIVE -25% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | BLK | A+ | 11/12 | +4.8% | -7.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | GILD | A | 10/12 | +20.5% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 23 | AAPL | A | 10/12 | +19.4% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 24 | SPOT | B | 10/12 | +15.9% | -7.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | MDT | B | 10/12 | +14.3% | -4.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 822.3 | 29.4 | F |
| 2 **TOP** | MRNA | 788.7 | 42.5 | T |
| 3 **TOP** | LITE | 410.9 | 34.4 | F |
| 4 **TOP** | MU | 333.4 | 35.9 | F |
| 5 **TOP** | DELL | 212.1 | 32.5 | F |
| 6 **TOP** | MRVL | 180.1 | 31.6 | F |
| 7 **TOP** | VLO | 170.6 | 34.7 | T |
| 8 **TOP** | ILMN | 169.3 | 36.1 | T |
| 9 **TOP** | VIAV | 163.9 | 42.7 | F |
| 10 **TOP** | MPC | 155.0 | 34.1 | T |
| 11 **TOP** | INTC | 140.7 | 31.0 | F |
| 12 **TOP** | SOXL | 130.9 | 33.1 | F |
| 13 **TOP** | AAOI | 124.8 | 29.2 | F |
| 14 **TOP** | PSX | 123.3 | 35.9 | T |
| 15 **TOP** | AMD | 122.3 | 45.2 | T |
| 16 **TOP** | COHR | 92.8 | 45.8 | F |
| 17 **TOP** | NUE | 91.4 | 41.6 | T |
| 18 **TOP** | MTSI | 87.4 | 42.3 | F |
| 19 **TOP** | LRCX | 82.9 | 35.7 | F |
| 20 **TOP** | CRWD | 80.6 | 53.4 | T |
| 21 **TOP** | AMAT | 77.5 | 36.9 | F |
| 22  | MRK | 71.8 | 31.9 | T |
| 23  | WBD | 68.9 | 75.2 | T |
| 24  | TGT | 68.3 | 61.9 | T |
| 25  | COP | 67.6 | 42.5 | T |
| 26  | DDOG | 64.1 | 27.7 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AMZN | Other | 257.37 | 49.0 | 30.4 | -0.0% | +0.8% | 21.3 | DEEP VALUE +100% (LOW) | 542.78 | +21% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 32% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SHOP | Other | 131.97 | 32.6 | 1.7 | -13.3% | -13.9% | 5.3 | UNDERVALUED +18% (MED) | 164.47 | +29% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +30% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟢 oversold | EOG | Energy | 149.53 | 44.4 | 8.2 | -3.7% | -0.7% | 48.4 | UNDERVALUED +12% (HIGH) | 167.77 | +10% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟢 oversold | GM | Other | 81.75 | 43.7 | 6.2 | -4.1% | -1.9% | 32.9 | FAIR +3% (MED) | 84.73 | +20% | STABLE | cyclical: TROUGH-CYCLE margins (8% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |
| 🟢 oversold | V | Other | 402.48 | 43.9 | 2.9 | -3.5% | +2.1% | 18.0 | FAIR -9% (HIGH) | 370.59 | +9% | STABLE | steady | disruption: revenue +12%/yr over 3 yrs |
| 🟢 oversold | MRK | Other | 132.74 | 31.9 | 0.7 | -8.4% | -8.8% | 71.8 | EXPENSIVE -38% (LOW) | 83.94 | +22% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟢 oversold | PSX | Energy | 242.73 | 35.9 | 4.1 | -7.8% | -9.5% | 123.3 | EXPENSIVE -25% (LOW) | 182.77 | +23% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | MSFT | Other | 498.3 | 39.2 | 8.0 | -5.1% | -4.2% | 2.9 | RICH -15% (LOW) | 444.23 | +20% | INNOVATING (quant STABLE) [research: innovating] | growth: its multiples disagree with each other; analysts disagree | disruption: revenue +16%/yr over 3 yrs; research 2026-11-17: AI is a demand driver, not a substitute: Azure +43% in FY26 Q4 and past $100B/yr, M365 Copilot at 30M paid seats; the risk is value shifting from per-seat Copilot to consumption and rival agent tools (Salesforce Agentforce, ServiceNow), plus margin pressure from >$50B capex. |
| 🟢 oversold | XOM | Energy | 158.97 | 34.2 | 4.7 | -7.8% | -6.2% | 57.8 | RICH -24% (HIGH) | 122.03 | +11% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Long-run threat from EV adoption (IEA: ~5.4 mb/d displaced by 2030, demand peak ~2029), but demand still grows this decade and the IEA cut its US EV forecast; not visible in XOM's volumes yet. |
| 🟢 oversold | VRTX | Other | 520.66 | 43.4 | 6.3 | -3.3% | -0.4% | 22.8 | RICH -20% (HIGH) | 418.69 | +16% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +10%/yr over 3 yrs; R&D 33% of revenue; research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟢 oversold | PM | Other | 186.43 | 34.6 | 2.4 | -6.8% | -5.3% | 26.5 | EXPENSIVE -25% (HIGH) | 139.32 | +16% | INNOVATING (quant STABLE) [research: innovating] | steady | disruption: research 2026-11-09: Smoke-free (IQOS heated tobacco, ZYN pouches) was ~42-43% of net revenue in 2026 (41.5% FY2025) and IQOS overtook Marlboro; PMI is the one shifting the market, though US ZYN shipments fell 23.5% in Q1 2026. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +19% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +118% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -48% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -41% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +48% (HIGH) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | yes | EXPENSIVE -42% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | yes | EXPENSIVE -32% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -39% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 42.8 | 55.9 |  |
| COST | 11.5 | 67.8 |  |
| MO | 25.3 | 46.7 |  |
| V | 27.0 | 43.9 |  |
| LLY | 23.4 | 50.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -43.0 | 27.7 | SPEC |
| QBTS | -47.2 | 26.6 | SPEC |
| ASTS | -29.7 | 29.8 | SPEC |
| RGTI | -53.1 | 30.7 | SPEC |
| UEC | -31.0 | 29.6 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._