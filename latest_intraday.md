# Strategy report - INTRADAY  (2026-11-18 19:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MO | A+ | 12/12 | #4 | 21 EMA pullback | Other |  |  |  | 76.33 | 11.0 | 76.33 | 72.99 | 78.9 | -4.4% |
| V | A+ | 12/12 | #5 | 21 EMA pullback | Other |  |  |  | 416.44 | 14.9 | 416.44 | 398.99 | 436.57 | -4.2% |
| LLY | A+ | 12/12 | #7 | RSI2 dip | Other |  |  |  | 1389.62 | 7.3 | 1389.62 | 1309.08 | 1443.5 | -5.8% |
| ABBV | A+ | 12/12 | #9 | RSI2 dip | Other |  |  |  | 286.93 | 2.2 | 286.93 | 278.0 | 295.03 | -3.1% |
| BLK | A+ | 12/12 | #10 | RSI2 dip | Other |  |  |  | 1173.01 | 5.7 | 1173.01 | 1111.94 | 1226.31 | -5.2% |
| AMGN | A+ | 12/12 | #11 | RSI2 dip | Other |  |  |  | 443.76 | 0.8 | 443.76 | 425.02 | 471.88 | -4.2% |
| EOG | A+ | 12/12 | #13 | RSI2 dip | Energy |  |  |  | 150.24 | 9.4 | 150.24 | 141.95 | 162.66 | -5.5% |
| MA | A+ | 11/12 | #18 | 21 EMA pullback | Other |  |  |  | 643.58 | 11.3 | 643.58 | 613.63 | 672.68 | -4.7% |
| TMO | A+ | 11/12 | #19 | 21 EMA pullback | Other |  |  |  | 691.95 | 49.1 | 691.95 | 658.28 | 721.63 | -4.9% |
| LIN | A+ | 11/12 | #21 | RSI2 dip | Other |  |  |  | 511.5 | 7.2 | 511.5 | 496.41 | 526.55 | -2.9% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): MRNA (B 8/12), MRK (C 3/12), PFE (B 9/12), DE (C 5/12), MPC (B 7/12), PSX (C 5/12), USB (C 5/12), VLO (C 5/12), NXPI (B 9/12), CVX (C 6/12), WDAY (C 3/12), XOM (B 8/12), JNJ (B 9/12), SHOP (C 7/12), CI (C 6/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MAR | A+ | 12/12 | +23.3% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | WBD | A+ | 12/12 | +22.4% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | REGN | A+ | 12/12 | +18.6% | -2.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MO | A+ | 12/12 | +17.8% | -3.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | V | A+ | 12/12 | +17.8% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | AAPL | A+ | 12/12 | +17.5% | -0.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | LLY | A+ | 12/12 | +15.9% | -3.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | DLTR | A+ | 12/12 | +15.2% | -2.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | ABBV | A+ | 12/12 | +13.6% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | BLK | A+ | 12/12 | +7.3% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | AMGN | A+ | 12/12 | +6.6% | -7.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | VRTX | A+ | 12/12 | +3.6% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | EOG | A+ | 12/12 | +2.9% | -9.0% | UNDERVALUED +10% (HIGH) | STABLE [research: neutral] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | PG | A+ | 11/12 | +23.4% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | COST | A+ | 11/12 | +22.9% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | CME | A+ | 11/12 | +18.2% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | DIS | A+ | 11/12 | +18.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MA | A+ | 11/12 | +16.1% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 19 | TMO | A+ | 11/12 | +14.2% | -4.1% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | KO | A+ | 11/12 | +12.1% | -1.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 21 | LIN | A+ | 11/12 | +10.2% | -6.4% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | EMR | A+ | 11/12 | +9.0% | -4.7% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | AMZN | A+ | 11/12 | +6.6% | -5.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | UNP | B | 11/12 | +2.9% | -3.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | ABNB | B | 11/12 | +2.5% | -4.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 878.3 | 30.1 | F |
| 2 **TOP** | MRNA | 772.3 | 42.4 | T |
| 3 **TOP** | LITE | 406.5 | 35.6 | F |
| 4 **TOP** | MU | 347.1 | 36.7 | F |
| 5 **TOP** | DELL | 204.5 | 32.7 | F |
| 6 **TOP** | ILMN | 175.2 | 39.5 | T |
| 7 **TOP** | VLO | 174.6 | 35.7 | T |
| 8 **TOP** | MRVL | 169.6 | 33.2 | F |
| 9 **TOP** | VIAV | 168.3 | 43.3 | F |
| 10 **TOP** | MPC | 156.8 | 35.4 | T |
| 11 **TOP** | INTC | 148.7 | 29.2 | F |
| 12 **TOP** | AAOI | 145.0 | 29.8 | F |
| 13 **TOP** | SOXL | 144.8 | 34.3 | F |
| 14 **TOP** | AMD | 130.8 | 49.3 | T |
| 15 **TOP** | PSX | 124.8 | 36.9 | T |
| 16 **TOP** | COHR | 99.4 | 45.0 | F |
| 17 **TOP** | NUE | 97.9 | 45.0 | T |
| 18 **TOP** | MTSI | 94.3 | 43.1 | F |
| 19 **TOP** | LRCX | 92.4 | 37.2 | F |
| 20 **TOP** | CRWD | 88.3 | 51.3 | T |
| 21 **TOP** | AMAT | 83.6 | 38.7 | F |
| 22 **TOP** | DDOG | 70.3 | 29.3 | F |
| 23  | WBD | 70.1 | 75.2 | T |
| 24  | MRK | 69.4 | 37.8 | T |
| 25  | FCX | 69.4 | 26.3 | F |
| 26  | TGT | 68.7 | 65.0 | T |
| 27  | COP | 67.9 | 43.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | SHOP | Other | 141.53 | 38.8 | 7.5 | -8.1% | -7.7% | 8.4 | UNDERVALUED +16% (MED) | 164.51 | +27% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: analysts agree | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +30% next year; research 2026-11-06: Commerce platform positioned for AI agentic shopping: Q3 2026 saw the first delegated purchases by personal AI agents on its stack (shop.dev); AI-driven orders tripled YoY in Q2; agentic orders carry the same economics as online-store orders. Growth ~low 30s%. |
| 🟢 oversold | EOG | Energy | 150.69 | 45.9 | 9.4 | -3.2% | +0.1% | 48.4 | UNDERVALUED +10% (HIGH) | 167.77 | +8% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟢 oversold | COP | Energy | 135.63 | 43.0 | 8.3 | -5.0% | -1.4% | 67.9 | FAIR -8% (HIGH) | 126.43 | +13% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |
| 🟢 oversold | USB | Other | 58.55 | 43.1 | 5.1 | -2.5% | -1.2% | 26.6 | FAIR +5% (HIGH) | 61.65 | +16% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟢 oversold | PLTR | AI-software | 157.88 | 34.3 | 25.9 | -10.6% | -14.2% | 9.0 | EXPENSIVE -50% (LOW) | 78.54 | +57% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +91% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | MPC | Energy | 373.4 | 35.4 | 4.3 | -10.2% | -11.9% | 156.8 | EXPENSIVE -34% (LOW) | 253.76 | +20% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| 🟢 oversold | PSX | Energy | 244.76 | 36.9 | 4.8 | -7.7% | -8.9% | 124.8 | EXPENSIVE -27% (LOW) | 182.77 | +20% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | MRK | Other | 138.27 | 37.8 | 1.8 | -5.1% | -5.1% | 69.4 | EXPENSIVE -39% (LOW) | 86.68 | +17% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |
| 🟢 oversold | CVX | Energy | 206.71 | 37.1 | 6.1 | -6.5% | -4.1% | 46.6 | RICH -12% (HIGH) | 183.52 | +11% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Same oil-demand-peak risk as the majors (IEA peak ~2029, EVs displacing ~5.4 mb/d by 2030); slower US EV adoption pushes it out. A risk, not yet showing in demand or pricing. |
| 🟢 oversold | XOM | Energy | 161.29 | 36.6 | 6.8 | -7.0% | -4.9% | 58.8 | EXPENSIVE -26% (HIGH) | 122.01 | +8% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Long-run threat from EV adoption (IEA: ~5.4 mb/d displaced by 2030, demand peak ~2029), but demand still grows this decade and the IEA cut its US EV forecast; not visible in XOM's volumes yet. |

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

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 40.4 | 67.9 |  |
| REGN | 14.6 | 65.1 |  |
| MO | 28.4 | 52.8 |  |
| V | 24.8 | 54.3 |  |
| AAPL | 26.9 | 57.5 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| IREN | -43.9 | 29.0 | SPEC |
| ASTS | -27.3 | 30.0 | SPEC |
| UUUU | -45.1 | 25.5 | SPEC |
| QBTS | -48.4 | 28.4 | SPEC |
| APLD | -15.7 | 37.4 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._