# Strategy report - INTRADAY  (2026-11-23 18:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LLY | A+ | 12/12 | #4 | 21 EMA pullback | Other |  |  |  | 1360.82 | 47.6 | 1360.82 | 1283.45 | 1443.5 | -5.7% |
| CME | A+ | 12/12 | #5 | 21 EMA pullback | Other |  |  |  | 302.87 | 10.5 | 302.87 | 290.86 | 319.37 | -4.0% |
| MO | A+ | 11/12 | #10 | RSI2 dip | Other |  |  |  | 74.02 | 7.7 | 74.02 | 71.03 | 78.51 | -4.0% |
| KO | A+ | 11/12 | #14 | 21 EMA pullback | Other |  |  |  | 95.86 | 21.8 | 95.86 | 93.25 | 99.48 | -2.7% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): MPC (C 5/12), EOG (B 8/12), PSX (C 5/12), VLO (C 5/12)

## Quality ranking — top 25 of 235 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | WBD | A+ | 12/12 | +24.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MAR | A+ | 12/12 | +22.0% | -3.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COST | A+ | 12/12 | +19.9% | -1.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | LLY | A+ | 12/12 | +16.0% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CME | A+ | 12/12 | +14.9% | -7.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DLTR | A+ | 12/12 | +9.0% | -5.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | WMT | A+ | 11/12 | +28.0% | -4.0% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | PG | A+ | 11/12 | +22.7% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 11/12 | +15.2% | -4.7% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | MO | A+ | 11/12 | +14.3% | -6.3% | RICH -11% (HIGH) | AT RISK [research: threatened] | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | ABBV | A+ | 11/12 | +13.7% | -2.7% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | DIS | A+ | 11/12 | +13.2% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | V | A+ | 11/12 | +12.4% | -6.1% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | KO | A+ | 11/12 | +10.3% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 15 | AMGN | A+ | 11/12 | +7.4% | -6.0% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | BLK | A+ | 11/12 | +3.5% | -6.2% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MRNA | A | 10/12 | +37.8% | -22.0% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | GILD | A | 10/12 | +19.8% | -2.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 19 | AAPL | A | 10/12 | +18.2% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 20 | REGN | A | 10/12 | +17.8% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 21 | MDT | A | 10/12 | +16.3% | -4.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | ROKU | A | 10/12 | +12.1% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |
| 23 | MA | A | 10/12 | +11.9% | -5.4% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | LIN | B | 10/12 | +11.2% | -6.0% | — | — | > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | SPOT | B | 10/12 | +10.4% | -7.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 21 of 218)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 648.3 | 47.3 | T |
| 2 **TOP** | SNDK | 565.0 | 32.8 | F |
| 3 **TOP** | LITE | 321.7 | 39.4 | F |
| 4 **TOP** | MU | 300.7 | 42.3 | F |
| 5 **TOP** | DELL | 187.7 | 42.2 | F |
| 6 **TOP** | MRVL | 171.6 | 38.5 | F |
| 7 **TOP** | VLO | 145.1 | 33.5 | T |
| 8 **TOP** | MPC | 133.0 | 32.5 | T |
| 9 **TOP** | INTC | 127.2 | 38.2 | F |
| 10 **TOP** | VIAV | 121.5 | 46.2 | F |
| 11 **TOP** | PSX | 109.8 | 33.9 | T |
| 12 **TOP** | AMD | 104.3 | 43.2 | T |
| 13 **TOP** | AAOI | 98.5 | 32.9 | F |
| 14 **TOP** | CRWD | 95.4 | 37.2 | T |
| 15 **TOP** | SOXL | 93.7 | 36.6 | F |
| 16 **TOP** | NUE | 86.1 | 43.5 | T |
| 17 **TOP** | PANW | 75.3 | 52.1 | T |
| 18 **TOP** | DDOG | 72.3 | 33.2 | F |
| 19 **TOP** | COP | 71.3 | 40.1 | T |
| 20 **TOP** | TXN | 68.3 | 49.6 | T |
| 21 **TOP** | MTSI | 67.7 | 47.3 | F |
| 22  | RBRK | 67.2 | 51.6 | T |
| 23  | MRK | 66.0 | 36.2 | T |
| 24  | AMAT | 64.9 | 42.6 | F |
| 25  | ROKU | 64.7 | 61.0 | T |
| 26  | ADI | 64.3 | 46.1 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | EOG | Energy | 146.24 | 40.0 | 2.1 | -4.9% | -2.8% | 53.3 | UNDERVALUED +13% (HIGH) | 167.63 | +11% | STABLE [research: neutral] | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Low-cost shale producer; gas demand from LNG and data-center power is a tailwind (management sees 3-5%/yr US gas demand growth), but it is a commodity producer riding a trend, not creating a market. |
| 🟢 oversold | MPC | Energy | 362.01 | 32.5 | 1.7 | -9.9% | -14.2% | 133.0 | EXPENSIVE -31% (LOW) | 249.38 | +27% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| 🟢 oversold | PSX | Energy | 238.67 | 33.9 | 2.3 | -7.7% | -10.8% | 109.8 | RICH -24% (LOW) | 182.77 | +25% | STABLE [research: neutral] | cyclical: PEAK-CYCLE margins (12% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-06: Refiner + midstream; refining margins held up by tight supply (96% utilization Q2 2026) and midstream EBITDA targeted at $4.5B run rate by 2027. EV-driven gasoline decline is a long-run risk not yet visible in demand or results. |
| 🟢 oversold | XOM | Energy | 157.58 | 33.7 | 14.9 | -7.2% | -6.9% | 58.8 | RICH -23% (HIGH) | 122.05 | +12% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Long-run threat from EV adoption (IEA: ~5.4 mb/d displaced by 2030, demand peak ~2029), but demand still grows this decade and the IEA cut its US EV forecast; not visible in XOM's volumes yet. |
| 🟢 oversold | VLO | Energy | 333.85 | 33.5 | 5.3 | -8.6% | -15.6% | 145.1 | EXPENSIVE -41% (LOW) | 198.77 | +32% | AT RISK (quant STABLE) [research: threatened] | cyclical: PEAK-CYCLE margins (14% vs 6% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| 🟢 oversold | PFE | Other | 27.43 | 33.0 | 24.5 | -6.1% | -4.8% | 21.3 | RICH -25% (MED) | 20.72 | +11% | AT RISK [research: neutral] | steady: its multiples disagree with each other | disruption: revenue shrinking -15%/yr over 3 yrs; gross margin up 8 pts (74%); research 2026-11-10: Revenue pressure is a patent cliff, not a technology making it obsolete: loss of exclusivity ~$1.5B headwind in 2026, ~$4.5B in 2027 (Eliquis key patent expires Nov 2026); the bet is the $10B Metsera obesity buy (Phase III, MET097 launch targeted 2028), unproven so far. |
| 🟢 oversold | MO | Other | 73.94 | 43.9 | 7.7 | -3.3% | +1.2% | 14.9 | RICH -11% (HIGH) | 64.85 | +13% | AT RISK [research: threatened] | steady | disruption: revenue shrinking -1%/yr over 3 yrs; gross margin up 3 pts (72%); research 2026-11-19: Smoke-free products are displacing cigarettes: Q3 2026 domestic cigarette volume -2.9% (~-4% adjusted; industry -5%), discount brands up 2 pts to 34%, while pouches are now >60% of oral nicotine and Altria's on! share is 8.3% (down 0.3 pts sequentially) behind PMI's ZYN; NJOY Ace was blocked by an ITC ruling. Pricing still holds revenue, so the shift is a threat to the core, not yet a revenue collapse. |
| 🟡 dip | COP | Energy | 132.91 | 40.1 | 17.4 | -5.4% | -3.2% | 71.3 | FAIR -6% (HIGH) | 126.45 | +14% | STABLE [research: neutral] | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-09: Pure upstream producer, most exposed to a post-2030 oil demand peak (IEA ~2029); demand still rising this decade, so the EV threat is not visible in its volumes yet. |
| 🟡 dip | GM | Other | 81.84 | 45.7 | 61.8 | -4.5% | -1.5% | 9.0 | FAIR +5% (MED) | 84.74 | +22% | STABLE | cyclical: TROUGH-CYCLE margins (8% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |
| 🟡 dip | MRK | Other | 134.9 | 36.2 | 43.8 | -6.4% | -7.0% | 66.0 | EXPENSIVE -38% (LOW) | 84.12 | +22% | STABLE [research: neutral] | steady: business changed (margin 18% vs 35% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: R&D 19% of revenue; research 2026-11-17: Main risk is a patent cliff, not a new technology: Keytruda (~$31.7B, about half of sales) loses exclusivity 2028-29; Merck is moving patients to subcutaneous Keytruda Qlex and building Winrevair (PAH, ~2x y/y) and Capvaxive as offsets. No product creating a large untapped market yet. |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); analysts see revenue +19% next year |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +120% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -48% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -40% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +65% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +56% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -41% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -31% (LOW) | STABLE [research: neutral] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-11-05: Refiner in an 'enhanced mid-cycle' through 2027 (R&M EBITDA $6.7B in Q2 2026); EV adoption is a long-run fuel-demand risk not yet visible; renewable diesel depends on credits. |
| MRVL | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -35% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +34% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MAR | 38.4 | 56.3 |  |
| COST | 12.3 | 66.6 |  |
| LLY | 22.1 | 52.0 |  |
| CME | 11.1 | 49.8 |  |
| DLTR | 27.1 | 55.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| UUUU | -43.1 | 27.9 | SPEC |
| IREN | -42.7 | 34.2 | SPEC |
| QBTS | -43.1 | 32.1 | SPEC |
| ASTS | -21.5 | 33.6 | SPEC |
| UEC | -33.5 | 34.9 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._