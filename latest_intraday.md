# Strategy report - INTRADAY  (2026-11-19 16:08 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V | A+ | 12/12 | #4 | RSI2 dip | Other |  |  |  | 403.51 | 3.1 | 403.51 | 385.78 | 430.1 | -4.4% |
| LLY | A+ | 12/12 | #5 | RSI2 dip | Other |  |  |  | 1349.99 | 2.6 | 1349.99 | 1270.52 | 1443.5 | -5.9% |
| ABBV | A+ | 12/12 | #7 | RSI2 dip | Other |  |  |  | 280.44 | 0.8 | 280.44 | 271.04 | 294.56 | -3.4% |
| BLK | A+ | 12/12 | #8 | RSI2 dip | Other |  |  |  | 1161.98 | 3.3 | 1161.98 | 1101.58 | 1226.31 | -5.2% |
| WMT | A+ | 11/12 | #9 | RSI2 dip | Other |  |  | ⚠️ 2026-11-19 | 125.55 | 7.8 | 125.55 | 120.75 | 129.17 | -3.8% |
| CME | A+ | 11/12 | #12 | RSI2 dip | Other |  |  |  | 307.52 | 8.1 | 307.52 | 295.66 | 319.37 | -3.9% |
| MO | A+ | 11/12 | #13 | RSI2 dip | Other |  |  |  | 73.76 | 3.2 | 73.76 | 70.48 | 78.67 | -4.4% |
| REGN | A+ | 11/12 | #14 | RSI2 dip | Other |  |  |  | 928.87 | 9.1 | 928.87 | 847.24 | 973.36 | -8.8% |
| MA | A+ | 11/12 | #16 | RSI2 dip | Other |  |  |  | 630.0 | 3.5 | 630.0 | 600.24 | 672.68 | -4.7% |
| LIN | A+ | 11/12 | #17 | 21 EMA pullback | Other |  |  |  | 512.47 | 13.8 | 512.47 | 498.4 | 526.55 | -2.7% |
| KO | A+ | 11/12 | #19 | RSI2 dip | Other |  |  |  | 95.5 | 4.9 | 95.5 | 92.45 | 99.48 | -3.2% |
| EMR | A+ | 11/12 | #21 | 21 EMA pullback | Other |  |  |  | 161.12 | 41.6 | 161.12 | 152.62 | 170.74 | -5.3% |
| GILD | A | 10/12 | #23 | 21 EMA pullback | Other |  |  |  | 165.5 | 14.2 | 165.5 | 157.45 | 174.48 | -4.9% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** WMT (2026-11-19). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMGN (B 10/12), DE (C 4/12), PFE (B 8/12), MRK (C 3/12), PM (C 6/12), JNJ (C 7/12), SHOP (C 6/12), MDLZ (B 9/12), MMM (B 10/12), MPC (B 7/12), PSX (C 5/12), WDAY (C 3/12), TEM (C 5/12), PYPL (B 9/12), GM (C 4/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +23.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +21.6% | -3.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COST | A+ | 12/12 | +19.4% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | V | A+ | 12/12 | +14.1% | -7.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LLY | A+ | 12/12 | +12.3% | -6.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DLTR | A+ | 12/12 | +11.5% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | ABBV | A+ | 12/12 | +10.6% | -5.0% | EXPENSIVE -40% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | BLK | A+ | 12/12 | +5.6% | -5.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WMT | A+ | 11/12 | +26.0% | -6.4% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PG | A+ | 11/12 | +21.2% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | DIS | A+ | 11/12 | +18.1% | -0.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | CME | A+ | 11/12 | +16.7% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | MO | A+ | 11/12 | +16.3% | -6.6% | RICH -12% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | REGN | A+ | 11/12 | +15.9% | -4.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 15 | TMO | A+ | 11/12 | +15.1% | -3.8% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MA | A+ | 11/12 | +13.7% | -6.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 17 | LIN | A+ | 11/12 | +9.9% | -6.3% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | ASND | A+ | 11/12 | +9.7% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 19 | KO | A+ | 11/12 | +9.5% | -4.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | AMZN | A+ | 11/12 | +8.7% | -5.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 21 | EMR | A+ | 11/12 | +7.3% | -5.6% | RICH -23% (HIGH) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | TGT | A+ | 11/12 | +5.6% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | GILD | A | 10/12 | +18.1% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 24 | AAPL | B | 10/12 | +17.9% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 25 | SPOT | B | 10/12 | +16.0% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 822.3 | 32.3 | F |
| 2 **TOP** | MRNA | 788.7 | 41.3 | T |
| 3 **TOP** | LITE | 410.9 | 36.8 | F |
| 4 **TOP** | MU | 333.4 | 39.5 | F |
| 5 **TOP** | DELL | 212.1 | 35.0 | F |
| 6 **TOP** | MRVL | 180.1 | 34.7 | F |
| 7 **TOP** | VLO | 170.6 | 35.5 | T |
| 8 **TOP** | VIAV | 163.9 | 46.5 | F |
| 9 **TOP** | MPC | 155.0 | 35.1 | T |
| 10 **TOP** | INTC | 140.7 | 33.5 | F |
| 11 **TOP** | SOXL | 130.9 | 35.5 | F |
| 12 **TOP** | AAOI | 124.8 | 30.9 | F |
| 13 **TOP** | PSX | 123.3 | 36.5 | T |
| 14 **TOP** | AMD | 122.3 | 45.0 | T |
| 15 **TOP** | COHR | 92.8 | 49.7 | F |
| 16 **TOP** | NUE | 91.4 | 43.3 | T |
| 17 **TOP** | MTSI | 87.4 | 45.9 | F |
| 18 **TOP** | LRCX | 82.9 | 39.9 | F |
| 19 **TOP** | CRWD | 80.6 | 57.0 | T |
| 20 **TOP** | AMAT | 77.5 | 40.9 | F |
| 21 **TOP** | MRK | 71.8 | 32.9 | T |
| 22  | WBD | 68.9 | 75.2 | T |
| 23  | TGT | 68.3 | 61.1 | T |
| 24  | COP | 67.6 | 41.5 | T |
| 25  | DDOG | 64.1 | 33.0 | F |
| 26  | ROKU | 63.7 | 61.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SHOP | Other | 136.96 | 35.6 | 3.1 | -10.1% | -10.8% | 5.3 | UNDERVALUED +18% (MED) | 164.47 | +29% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +30% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟢 oversold | EOG | Energy | 149.39 | 44.2 | 7.9 | -3.8% | -0.8% | 48.4 | UNDERVALUED +12% (HIGH) | 167.77 | +10% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟢 oversold | COP | Energy | 134.44 | 41.5 | 7.2 | -5.4% | -2.2% | 67.6 | FAIR -6% (HIGH) | 126.45 | +15% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |
| 🟢 oversold | GM | Other | 81.77 | 43.8 | 5.2 | -4.1% | -1.8% | 32.9 | FAIR +3% (MED) | 84.73 | +20% | STABLE | cyclical: TROUGH-CYCLE margins (8% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |
| 🟢 oversold | MRK | Other | 133.91 | 32.9 | 0.8 | -7.6% | -8.0% | 71.8 | EXPENSIVE -38% (LOW) | 83.94 | +22% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟢 oversold | PSX | Energy | 244.05 | 36.5 | 4.4 | -7.3% | -9.1% | 123.3 | EXPENSIVE -25% (LOW) | 182.77 | +23% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | XOM | Energy | 159.8 | 35.1 | 5.3 | -7.3% | -5.7% | 57.8 | RICH -24% (HIGH) | 122.03 | +11% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Long-run threat from EV adoption (IEA: ~5.4 mb/d displaced by 2030, demand peak ~2029), but demand still grows this decade and the IEA cut its US EV forecast; not visible in XOM's volumes yet. |
| 🟢 oversold | VRTX | Other | 523.33 | 44.6 | 7.2 | -2.8% | +0.1% | 22.8 | RICH -20% (HIGH) | 418.69 | +16% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +10%/yr over 3 yrs; R&D 33% of revenue; research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟢 oversold | PM | Other | 185.2 | 33.6 | 2.2 | -7.4% | -5.9% | 26.5 | EXPENSIVE -25% (HIGH) | 139.32 | +16% | INNOVATING (quant STABLE) [research: innovating] | steady | disruption: research 2026-11-09: Smoke-free (IQOS heated tobacco, ZYN pouches) was ~42-43% of net revenue in 2026 (41.5% FY2025) and IQOS overtook Marlboro; PMI is the one shifting the market, though US ZYN shipments fell 23.5% in Q1 2026. |
| 🟢 oversold | DE | Other | 625.65 | 36.2 | 0.6 | -5.5% | -6.0% | 36.7 | EXPENSIVE -42% (HIGH) | 368.13 | +17% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%); research 2026-11-16: Deere is the one driving ag automation (See & Spray Gen 2 consolidated and expanded to ~2x crops for MY2027, autonomy-ready tillage, goal of an autonomy kit on every large tractor, full autonomy for corn/soy by 2030); tech options support margins while base equipment volume is cyclical-down. No rival shown taking share. |

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
| ILMN | no | DEEP VALUE +48% (HIGH) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | yes | EXPENSIVE -42% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | yes | EXPENSIVE -32% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -39% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 42.8 | 57.6 |  |
| COST | 11.5 | 64.4 |  |
| V | 27.0 | 45.7 |  |
| LLY | 23.4 | 50.0 |  |
| DLTR | 23.5 | 57.6 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -43.0 | 28.9 | SPEC |
| UUUU | -45.5 | 25.6 | SPEC |
| QBTS | -47.2 | 29.3 | SPEC |
| ASTS | -29.7 | 32.1 | SPEC |
| UEC | -31.0 | 31.6 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._