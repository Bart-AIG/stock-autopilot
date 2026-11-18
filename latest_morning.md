# Strategy report - MORNING  (2026-11-18 15:13 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MO | A+ | 12/12 | #4 | 21 EMA pullback | Other |  |  |  | 76.89 | 15.1 | 76.89 | 73.58 | 78.9 | -4.3% |
| V | A+ | 12/12 | #6 | 21 EMA pullback | Other |  |  |  | 414.34 | 11.3 | 414.34 | 396.91 | 436.57 | -4.2% |
| ABBV | A+ | 12/12 | #8 | RSI2 dip | Other |  |  |  | 290.39 | 4.2 | 290.39 | 281.89 | 295.03 | -2.9% |
| AMGN | A+ | 12/12 | #10 | RSI2 dip | Other |  |  |  | 450.42 | 1.3 | 450.42 | 432.64 | 477.1 | -3.9% |
| BLK | A+ | 12/12 | #11 | 21 EMA pullback | Other |  |  |  | 1181.09 | 10.5 | 1181.09 | 1119.82 | 1226.31 | -5.2% |
| EOG | A+ | 12/12 | #12 | 21 EMA pullback | Energy |  |  |  | 152.88 | 16.3 | 152.88 | 144.75 | 165.07 | -5.3% |
| CME | A+ | 11/12 | #15 | 21 EMA pullback | Other |  |  |  | 306.95 | 10.0 | 306.95 | 293.67 | 319.37 | -4.3% |
| MA | A+ | 11/12 | #16 | RSI2 dip | Other |  |  |  | 641.36 | 9.6 | 641.36 | 611.41 | 672.68 | -4.7% |
| TMO | A+ | 11/12 | #18 | RSI2 dip | Other |  |  |  | 685.9 | 5.6 | 685.9 | 652.65 | 721.63 | -4.8% |
| LIN | A+ | 11/12 | #20 | RSI2 dip | Other |  |  |  | 511.92 | 7.5 | 511.92 | 496.85 | 526.55 | -2.9% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): MMM (B 10/12), MRNA (B 8/12), DE (C 5/12), PFE (B 9/12), MRK (C 4/12), MSFT (C 6/12), USB (C 5/12), UNH (C 4/12), PSX (C 5/12), MPC (B 7/12), JPM (C 6/12), BMY (C 5/12), CVX (C 6/12), WDAY (C 3/12), VLO (C 5/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MAR | A+ | 12/12 | +23.6% | -0.3% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | WBD | A+ | 12/12 | +22.1% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | REGN | A+ | 12/12 | +20.0% | -1.2% | RICH -12% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MO | A+ | 12/12 | +18.5% | -2.5% | RICH -16% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | AAPL | A+ | 12/12 | +17.9% | -0.1% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | V | A+ | 12/12 | +16.9% | -5.1% | RICH -10% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | LLY | A+ | 12/12 | +16.7% | -2.5% | RICH -15% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | ABBV | A+ | 12/12 | +14.5% | -1.6% | EXPENSIVE -41% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | DLTR | A+ | 12/12 | +11.7% | -5.6% | DEEP VALUE +36% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMGN | A+ | 12/12 | +7.5% | -5.9% | EXPENSIVE -27% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | BLK | A+ | 12/12 | +7.3% | -3.7% | RICH -20% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EOG | A+ | 12/12 | +4.1% | -7.6% | UNDERVALUED +10% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PG | A+ | 11/12 | +22.9% | -1.4% | FAIR -4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | COST | A+ | 11/12 | +22.2% | -0.6% | EXPENSIVE -28% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | CME | A+ | 11/12 | +17.0% | -6.0% | FAIR +7% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | MA | A+ | 11/12 | +15.4% | -4.7% | FAIR +4% (HIGH) | INNOVATING (quant STABLE) [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 17 | DIS | A+ | 11/12 | +14.9% | -0.2% | UNDERVALUED +14% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | TMO | A+ | 11/12 | +12.9% | -5.0% | RICH -18% (HIGH) | AT RISK | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | KO | A+ | 11/12 | +11.7% | -1.6% | FAIR -6% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 20 | LIN | A+ | 11/12 | +10.0% | -6.4% | RICH -22% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | UNP | A+ | 11/12 | +2.7% | -3.0% | RICH -11% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | ABNB | A+ | 11/12 | +1.6% | -4.9% | FAIR -5% (LOW) | AT RISK [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | WMT | A | 10/12 | +25.5% | -5.7% | EXPENSIVE -43% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | GILD | B | 10/12 | +21.6% | -3.0% | EXPENSIVE -32% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 25 | SPOT | B | 10/12 | +17.7% | -4.5% | UNDERVALUED +14% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 878.3 | 30.4 | F |
| 2 **TOP** | MRNA | 772.3 | 43.9 | T |
| 3 **TOP** | LITE | 406.5 | 36.2 | F |
| 4 **TOP** | MU | 347.1 | 37.4 | F |
| 5 **TOP** | DELL | 204.5 | 34.3 | F |
| 6 **TOP** | ILMN | 175.2 | 35.6 | T |
| 7 **TOP** | VLO | 174.6 | 37.8 | T |
| 8 **TOP** | MRVL | 169.6 | 34.0 | F |
| 9 **TOP** | VIAV | 168.3 | 44.6 | F |
| 10 **TOP** | MPC | 156.8 | 38.0 | T |
| 11 **TOP** | INTC | 148.7 | 29.8 | F |
| 12 **TOP** | AAOI | 145.0 | 29.7 | F |
| 13 **TOP** | SOXL | 144.8 | 35.1 | F |
| 14 **TOP** | AMD | 130.8 | 48.7 | T |
| 15 **TOP** | PSX | 124.8 | 38.5 | T |
| 16 **TOP** | COHR | 99.4 | 45.7 | F |
| 17 **TOP** | NUE | 97.9 | 47.1 | T |
| 18 **TOP** | MTSI | 94.3 | 45.1 | F |
| 19 **TOP** | LRCX | 92.4 | 38.9 | F |
| 20 **TOP** | CRWD | 88.3 | 43.5 | T |
| 21 **TOP** | AMAT | 83.6 | 40.0 | F |
| 22 **TOP** | DDOG | 70.3 | 27.3 | F |
| 23  | WBD | 70.1 | 75.2 | T |
| 24  | MRK | 69.4 | 41.6 | T |
| 25  | FCX | 69.4 | 26.1 | F |
| 26  | TGT | 68.7 | 62.4 | T |
| 27  | COP | 67.9 | 45.6 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | USB | Other | 58.76 | 44.1 | 6.1 | -2.2% | -0.9% | 26.6 | FAIR +5% (HIGH) | 61.65 | +16% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟢 oversold | PLTR | AI-software | 157.53 | 33.9 | 21.2 | -10.8% | -14.4% | 9.0 | EXPENSIVE -50% (LOW) | 78.54 | +57% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +91% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | MPC | Energy | 383.64 | 38.0 | 7.1 | -7.9% | -9.5% | 156.8 | EXPENSIVE -34% (LOW) | 253.76 | +20% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| 🟢 oversold | PSX | Energy | 248.12 | 38.5 | 6.5 | -6.6% | -7.7% | 124.8 | EXPENSIVE -27% (LOW) | 182.77 | +20% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | MRK | Other | 141.22 | 41.6 | 3.3 | -3.2% | -3.1% | 69.4 | EXPENSIVE -39% (LOW) | 86.68 | +17% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟢 oversold | MSFT | Other | 505.79 | 41.7 | 4.3 | -3.8% | -2.7% | 3.9 | RICH -12% (LOW) | 444.3 | +23% | INNOVATING (quant STABLE) [research: innovating] | growth: its multiples disagree with each other; analysts disagree | disruption: revenue +16%/yr over 3 yrs; research 2026-11-17: AI is a demand driver, not a substitute: Azure +43% in FY26 Q4 and past $100B/yr, M365 Copilot at 30M paid seats; the risk is value shifting from per-seat Copilot to consumption and rival agent tools (Salesforce Agentforce, ServiceNow), plus margin pressure from >$50B capex. |
| 🟢 oversold | CVX | Energy | 209.37 | 39.4 | 8.1 | -5.4% | -2.9% | 46.6 | RICH -12% (HIGH) | 183.52 | +11% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Same oil-demand-peak risk as the majors (IEA peak ~2029, EVs displacing ~5.4 mb/d by 2030); slower US EV adoption pushes it out. A risk, not yet showing in demand or pricing. |
| 🟢 oversold | JPM | Other | 329.24 | 41.4 | 7.2 | -2.8% | -2.9% | 12.1 | EXPENSIVE -28% (HIGH) | 236.32 | +14% | STABLE | bank |
| 🟢 oversold | DE | Other | 643.71 | 41.8 | 2.2 | -2.9% | -3.4% | 36.8 | EXPENSIVE -43% (HIGH) | 368.63 | +15% | INNOVATING (quant STABLE) [research: innovating] | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%); research 2026-11-16: Deere is the one driving ag automation (See & Spray Gen 2 consolidated and expanded to ~2x crops for MY2027, autonomy-ready tillage, goal of an autonomy kit on every large tractor, full autonomy for corn/soy by 2030); tech options support margins while base equipment volume is cyclical-down. No rival shown taking share. |
| 🟢 oversold | UNH | Other | 375.52 | 36.4 | 6.3 | -7.2% | -4.0% | 14.1 | UNDERVALUED +12% (HIGH) | 416.12 | +34% | AT RISK | **VALUE TRAP?** steady: analysts agree | disruption: revenue +11%/yr over 3 yrs; gross margin down 6 pts vs 5-yr median (19%) |

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
| DELL | no | EXPENSIVE -47% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -37% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | yes | DEEP VALUE +55% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -42% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -34% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -34% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #208 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #235 | N/A | INNOVATING |
| Drones | UMAC | C 1/12 #177 | N/A | N/A |
| Drones | UAVS | C 0/12 #233 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #221 | DEEP VALUE +100% (LOW) | DISRUPTOR |
| Drones | DPRO | C 0/12 #210 | DEEP VALUE +35% (LOW) | AT RISK |
| Drones | KTOS | C 0/12 #219 | FAIR -0% (MED) | INNOVATING |
| Drones | AVAV | C 0/12 #202 | DEEP VALUE +69% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #236 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #156 | FAIR +8% (HIGH) | STABLE |
| Raw materials | SCCO | C 1/12 #159 | EXPENSIVE -26% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #155 | RICH -14% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #158 | RICH -13% (LOW) | STABLE |
| Raw materials | FCX | C 1/12 #161 | RICH -17% (MED) | STABLE |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 40.4 | 68.9 |  |
| REGN | 14.6 | 68.8 |  |
| MO | 28.4 | 55.8 |  |
| AAPL | 26.9 | 59.2 |  |
| V | 24.8 | 52.4 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -43.9 | 29.4 | SPEC |
| ASTS | -27.3 | 32.1 | SPEC |
| QBTS | -48.4 | 31.2 | SPEC |
| UUUU | -45.1 | 30.6 | SPEC |
| APLD | -15.7 | 36.7 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._