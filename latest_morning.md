# Strategy report - MORNING  (2026-11-19 15:12 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V | A+ | 12/12 | #4 | RSI2 dip | Other |  |  |  | 407.93 | 4.3 | 407.93 | 390.7 | 433.77 | -4.2% |
| LLY | A+ | 12/12 | #5 | RSI2 dip | Other |  |  |  | 1369.51 | 4.0 | 1369.51 | 1290.85 | 1443.5 | -5.7% |
| ABBV | A+ | 12/12 | #7 | RSI2 dip | Other |  |  |  | 282.84 | 1.1 | 282.84 | 273.68 | 295.03 | -3.2% |
| BLK | A+ | 12/12 | #8 | 21 EMA pullback | Other |  |  |  | 1181.79 | 49.5 | 1181.79 | 1120.29 | 1226.31 | -5.2% |
| WMT | A+ | 11/12 | #9 | RSI2 dip | Other |  |  | ⚠️ 2026-11-19 | 125.53 | 7.8 | 125.53 | 120.73 | 129.17 | -3.8% |
| CME | A+ | 11/12 | #13 | RSI2 dip | Other |  |  |  | 308.28 | 9.3 | 308.28 | 296.44 | 319.37 | -3.8% |
| MO | A+ | 11/12 | #14 | RSI2 dip | Other |  |  |  | 73.95 | 3.4 | 73.95 | 70.7 | 78.82 | -4.4% |
| REGN | A+ | 11/12 | #15 | RSI2 dip | Other |  |  |  | 930.9 | 9.9 | 930.9 | 849.25 | 973.36 | -8.8% |
| MA | A+ | 11/12 | #17 | RSI2 dip | Other |  |  |  | 634.62 | 4.6 | 634.62 | 605.16 | 672.68 | -4.6% |
| LIN | A+ | 11/12 | #20 | 21 EMA pullback | Other |  |  |  | 514.12 | 36.2 | 514.12 | 499.97 | 526.55 | -2.8% |
| KO | A+ | 11/12 | #22 | RSI2 dip | Other |  |  |  | 95.06 | 4.3 | 95.06 | 91.91 | 99.48 | -3.3% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** WMT (2026-11-19). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMGN (B 11/12), PFE (B 8/12), MRK (C 3/12), MRNA (B 8/12), DE (C 4/12), PM (C 5/12), JNJ (C 7/12), MPC (C 7/12), MDLZ (B 9/12), SHOP (C 6/12), WDAY (C 3/12), XOM (C 7/12), VLO (C 5/12), MMM (B 10/12), CL (B 9/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +22.3% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +21.1% | -2.7% | EXPENSIVE -30% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COST | A+ | 12/12 | +18.9% | -2.1% | EXPENSIVE -27% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | V | A+ | 12/12 | +13.8% | -6.6% | FAIR -9% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LLY | A+ | 12/12 | +12.9% | -5.1% | RICH -13% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DLTR | A+ | 12/12 | +11.1% | -4.0% | DEEP VALUE +34% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | ABBV | A+ | 12/12 | +10.6% | -4.1% | EXPENSIVE -40% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | BLK | A+ | 12/12 | +6.0% | -3.6% | RICH -21% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | WMT | A+ | 11/12 | +24.9% | -6.5% | EXPENSIVE -44% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PG | A+ | 11/12 | +19.6% | -3.2% | FAIR -3% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | DIS | A+ | 11/12 | +16.6% | -0.7% | UNDERVALUED +13% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | TXN | A+ | 11/12 | +16.4% | -10.5% | EXPENSIVE -33% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | CME | A+ | 11/12 | +16.0% | -5.6% | FAIR +6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | MO | A+ | 11/12 | +15.7% | -6.3% | RICH -12% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | REGN | A+ | 11/12 | +15.5% | -4.4% | FAIR -9% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 16 | TMO | A+ | 11/12 | +14.4% | -3.6% | RICH -19% (HIGH) | AT RISK | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MA | A+ | 11/12 | +13.1% | -5.7% | FAIR +5% (HIGH) | INNOVATING (quant STABLE) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 18 | MDT | A+ | 11/12 | +12.0% | -4.2% | FAIR +7% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | ASND | A+ | 11/12 | +10.2% | -2.8% | N/A | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | LIN | A+ | 11/12 | +9.3% | -5.9% | RICH -23% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | AMZN | A+ | 11/12 | +8.9% | -4.3% | DEEP VALUE +100% (LOW) | DISRUPTOR (quant INNOVATING) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | KO | A+ | 11/12 | +8.2% | -4.4% | FAIR -3% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | EMR | A+ | 11/12 | +6.8% | -5.2% | RICH -23% (HIGH) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | TGT | B | 11/12 | +5.0% | -1.5% | FAIR -7% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | AMGN | B | 11/12 | +3.8% | -8.2% | EXPENSIVE -25% (HIGH) | INNOVATING | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 822.3 | 33.9 | F |
| 2 **TOP** | MRNA | 788.7 | 41.2 | T |
| 3 **TOP** | LITE | 410.9 | 38.6 | F |
| 4 **TOP** | MU | 333.4 | 42.2 | F |
| 5 **TOP** | DELL | 212.1 | 37.4 | F |
| 6 **TOP** | MRVL | 180.1 | 36.6 | F |
| 7 **TOP** | VLO | 170.6 | 35.7 | T |
| 8 **TOP** | VIAV | 163.9 | 48.0 | F |
| 9 **TOP** | MPC | 155.0 | 34.9 | T |
| 10 **TOP** | INTC | 140.7 | 35.3 | F |
| 11 **TOP** | SOXL | 130.9 | 38.2 | F |
| 12 **TOP** | AAOI | 124.8 | 31.8 | F |
| 13 **TOP** | PSX | 123.3 | 37.5 | T |
| 14 **TOP** | AMD | 122.3 | 52.2 | T |
| 15 **TOP** | COHR | 92.8 | 51.7 | F |
| 16 **TOP** | NUE | 91.4 | 46.3 | T |
| 17 **TOP** | MTSI | 87.4 | 46.7 | F |
| 18 **TOP** | LRCX | 82.9 | 42.0 | F |
| 19 **TOP** | CRWD | 80.6 | 57.5 | T |
| 20 **TOP** | AMAT | 77.5 | 42.3 | F |
| 21 **TOP** | MRK | 71.8 | 34.1 | T |
| 22  | WBD | 68.9 | 75.2 | T |
| 23  | TGT | 68.3 | 61.7 | T |
| 24  | COP | 67.6 | 42.1 | T |
| 25  | DDOG | 64.1 | 36.2 | F |
| 26  | ROKU | 63.7 | 61.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SHOP | Other | 139.11 | 37.1 | 5.3 | -8.8% | -9.4% | 5.3 | UNDERVALUED +18% (MED) | 164.47 | +29% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +30% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟢 oversold | MRK | Other | 135.01 | 34.1 | 1.0 | -6.9% | -7.2% | 71.8 | EXPENSIVE -38% (LOW) | 83.94 | +22% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟢 oversold | XOM | Energy | 160.21 | 35.5 | 6.0 | -7.1% | -5.5% | 57.8 | RICH -24% (HIGH) | 122.03 | +11% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Long-run threat from EV adoption (IEA: ~5.4 mb/d displaced by 2030, demand peak ~2029), but demand still grows this decade and the IEA cut its US EV forecast; not visible in XOM's volumes yet. |
| 🟢 oversold | PM | Other | 186.8 | 35.0 | 2.5 | -6.6% | -5.1% | 26.5 | EXPENSIVE -25% (HIGH) | 139.32 | +16% | INNOVATING (quant STABLE) [research: innovating] | steady | disruption: research 2026-11-09: Smoke-free (IQOS heated tobacco, ZYN pouches) was ~42-43% of net revenue in 2026 (41.5% FY2025) and IQOS overtook Marlboro; PMI is the one shifting the market, though US ZYN shipments fell 23.5% in Q1 2026. |
| 🟢 oversold | DE | Other | 636.72 | 39.4 | 1.1 | -3.9% | -4.3% | 36.7 | EXPENSIVE -42% (HIGH) | 368.13 | +17% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%); research 2026-11-16: Deere is the one driving ag automation (See & Spray Gen 2 consolidated and expanded to ~2x crops for MY2027, autonomy-ready tillage, goal of an autonomy kit on every large tractor, full autonomy for corn/soy by 2030); tech options support margins while base equipment volume is cyclical-down. No rival shown taking share. |
| 🟢 oversold | AMGN | Other | 439.05 | 42.9 | 0.5 | -4.3% | +2.3% | 44.7 | EXPENSIVE -25% (HIGH) | 329.27 | -2% | INNOVATING | steady: analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin slipping 4 pts (71%) |
| 🟢 oversold | JNJ | Other | 266.96 | 44.5 | 2.6 | -2.8% | -0.1% | 33.9 | EXPENSIVE -38% (HIGH) | 163.85 | +6% | STABLE [research: neutral] | steady | disruption: R&D 16% of revenue; research 2026-10-14: Stelara is eroding ~55-60% to biosimilars, but Tremfya (+71%) and the oncology franchise offset it; 2026 sales guide $100.3-101.3B. A patent cliff, not a technology making the business obsolete. |
| 🟢 oversold | ABBV | Other | 282.84 | 44.7 | 1.1 | -2.6% | +1.6% | 24.6 | EXPENSIVE -40% (HIGH) | 169.55 | +13% | STABLE | steady | disruption: revenue flat (+2%/yr over 3 yrs); analysts see revenue +11% next year |
| 🟢 oversold | PFE | Other | 27.61 | 33.9 | 0.8 | -6.2% | -4.2% | 22.0 | RICH -25% (MED) | 20.71 | +11% | AT RISK [research: neutral] | steady: its multiples disagree with each other | disruption: revenue shrinking -15%/yr over 3 yrs; gross margin up 8 pts (74%); research 2026-11-10: Revenue pressure is a patent cliff, not a technology making it obsolete: loss of exclusivity ~$1.5B headwind in 2026, ~$4.5B in 2027 (Eliquis key patent expires Nov 2026); the bet is the $10B Metsera obesity buy (Phase III, MET097 launch targeted 2028), unproven so far. |
| 🟢 oversold | MO | Other | 73.95 | 44.2 | 3.4 | -3.2% | +1.5% | 15.9 | RICH -12% (HIGH) | 64.85 | +13% | AT RISK | steady | disruption: revenue shrinking -1%/yr over 3 yrs; gross margin up 3 pts (72%) |

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

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #213 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #234 | N/A | INNOVATING |
| Drones | UMAC | C 1/12 #178 | N/A | N/A |
| Drones | UAVS | C 0/12 #233 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #220 | DEEP VALUE +100% (LOW) | DISRUPTOR |
| Drones | DPRO | C 0/12 #219 | DEEP VALUE +52% (LOW) | BEING DISRUPTED |
| Drones | KTOS | C 0/12 #214 | FAIR -1% (MED) | INNOVATING |
| Drones | AVAV | C 0/12 #200 | DEEP VALUE +73% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #235 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #162 | FAIR +7% (HIGH) | STABLE |
| Raw materials | SCCO | C 1/12 #165 | EXPENSIVE -27% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #160 | FAIR -10% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #161 | RICH -15% (LOW) | STABLE |
| Raw materials | FCX | C 1/12 #166 | RICH -18% (MED) | STABLE |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 42.8 | 59.2 |  |
| COST | 11.5 | 66.3 |  |
| V | 27.0 | 47.5 |  |
| LLY | 23.4 | 53.4 |  |
| DLTR | 23.5 | 58.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| UUUU | -45.5 | 26.3 | SPEC |
| IREN | -43.0 | 31.3 | SPEC |
| QBTS | -47.2 | 31.3 | SPEC |
| ASTS | -29.7 | 33.3 | SPEC |
| UEC | -31.0 | 31.2 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._