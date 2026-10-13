# Strategy report - MORNING  (2026-10-13 14:09 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AMD | A+ | 12/12 | #15 | RSI2 dip | Semis |  | HELD | 2026-11-03 | 588.66 | 3.6 | 588.66 | 541.92 | 649.42 | -7.9% |
| NVDA | A+ | 12/12 | #18 | RSI2 dip | Semis |  |  |  | 225.4 | 3.3 | 225.4 | 217.69 | 236.97 | -3.4% |
| QQQ | A+ | 12/12 | #20 | 21 EMA pullback | Index-ETF |  |  |  | 743.6 | 15.8 | 743.6 | 726.35 | 759.66 | -2.3% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 5/12), LRCX (C 3/12), ARM (C 6/12), INTC (C 6/12), KLAC (C 4/12), MU (C 7/12), SMCI (B 10/12), MRVL (B 10/12), CRDO (C 5/12)

## Quality ranking — top 25 of 224 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +208.7% | -5.4% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +54.1% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +50.3% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | RBRK | A+ | 12/12 | +47.9% | -3.5% | EXPENSIVE -30% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | PSX | A+ | 12/12 | +43.5% | 0.0% | EXPENSIVE -45% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DELL | A+ | 12/12 | +35.7% | -2.7% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +25.5% | -4.7% | EXPENSIVE -48% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | COP | A+ | 12/12 | +22.0% | -1.3% | RICH -18% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +20.6% | -2.6% | RICH -15% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | XOM | A+ | 12/12 | +17.4% | 0.0% | EXPENSIVE -37% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | CVX | A+ | 12/12 | +16.4% | -0.4% | RICH -25% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | WBD | A+ | 12/12 | +15.4% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | PANW | A+ | 12/12 | +11.2% | -3.6% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | ABBV | A+ | 12/12 | +10.9% | -1.0% | EXPENSIVE -45% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | AMD | A+ | 12/12 | +8.2% | -9.4% | EXPENSIVE -36% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PM | A+ | 12/12 | +8.1% | -0.5% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | EOG | A+ | 12/12 | +7.3% | -1.3% | FAIR -2% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | NVDA | A+ | 12/12 | +3.0% | -5.8% | FAIR -1% (MED) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | AAPL | A+ | 12/12 | +2.4% | 0.0% | EXPENSIVE -36% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | QQQ | A+ | 12/12 | +0.5% | -2.1% | N/A | N/A | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | PLTR | A+ | 11/12 | +54.4% | 0.0% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | MSFT | A+ | 11/12 | +35.9% | 0.0% | RICH -19% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | LITE | B | 11/12 | +27.1% | -13.6% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | EMR | B | 11/12 | +16.4% | -1.0% | EXPENSIVE -31% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | AMGN | B | 11/12 | +12.9% | -6.4% | RICH -22% (HIGH) | INNOVATING | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 218)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 520.3 | 39.2 | T |
| 2 **TOP** | MRNA | 512.4 | 65.1 | T |
| 3 **TOP** | LITE | 468.7 | 49.4 | T |
| 4 **TOP** | WDC | 357.9 | 32.3 | F |
| 5 **TOP** | DELL | 353.7 | 57.5 | T |
| 6 **TOP** | INTC | 327.5 | 39.3 | T |
| 7 **TOP** | AAOI | 289.2 | 42.9 | F |
| 8 **TOP** | MRVL | 250.6 | 52.3 | T |
| 9 **TOP** | AMD | 225.5 | 51.3 | T |
| 10 **TOP** | VIAV | 222.1 | 48.4 | T |
| 11 **TOP** | COHR | 196.5 | 43.6 | F |
| 12 **TOP** | AMAT | 172.0 | 43.8 | T |
| 13 **TOP** | LRCX | 155.0 | 42.8 | T |
| 14 **TOP** | VLO | 149.1 | 74.0 | T |
| 15 **TOP** | FCEL | 131.3 | 43.1 | T |
| 16 **TOP** | MPC | 119.6 | 77.1 | T |
| 17 **TOP** | MTSI | 108.5 | 51.9 | T |
| 18 **TOP** | PSX | 98.4 | 75.0 | T |
| 19 **TOP** | CAT | 89.7 | 38.7 | F |
| 20 **TOP** | CRWD | 89.6 | 58.1 | T |
| 21 **TOP** | KLAC | 87.4 | 45.0 | T |
| 22  | NUE | 83.5 | 54.0 | T |
| 23  | ARM | 75.8 | 38.8 | T |
| 24  | MRK | 73.8 | 48.1 | T |
| 25  | TGT | 73.2 | 44.9 | T |
| 26  | FDX | 68.8 | 41.4 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 942.59 | 39.2 | 3.6 | -9.6% | -4.0% | 520.3 | EXPENSIVE -50% (LOW) | 473.0 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | CRDO | Other | 189.69 | 44.6 | 7.2 | -4.4% | -9.3% | 0.6 | EXPENSIVE -40% (MED) | 113.59 | +45% | DISRUPTOR [research: disruptor] | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year; research 2026-10-12: Invented the active electrical cable (AEC) market for AI data centers and holds ~88% of it (650 Group); Jefferies sees AEC units 8.6M in 2026 to 12.3M in 2027. |
| 🟡 dip | AUR | Other | 5.63 | 41.5 | 20.6 | -4.6% | -8.9% | 13.4 | N/A | — | — | DISRUPTOR (quant INNOVATING) [research: innovating] | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year; research 2026-10-12: Driverless trucking on Sun Belt lanes (~440k driverless miles, target >200 trucks by end-2026), but still pre-revenue scale with 2025 losses of $816M; a builder of a new market, not yet proven economics. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | ARM | Semis | 248.71 | 38.8 | 0.8 | -14.3% | -8.0% | 75.8 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | LRCX | Semis | 301.14 | 42.8 | 0.8 | -4.1% | -3.2% | 155.0 | EXPENSIVE -50% (LOW) | 151.0 | +21% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +50% next year; gross margin up 4 pts (50%) |
| 🟢 oversold | AMAT | Semis | 476.45 | 43.8 | 0.8 | -2.9% | -2.5% | 172.0 | EXPENSIVE -50% (LOW) | 238.0 | +36% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year |
| 🟢 oversold | KLAC | Semis | 185.98 | 45.0 | 1.1 | -2.3% | -1.2% | 87.4 | EXPENSIVE -50% (MED) | 93.03 | +18% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why | disruption: revenue +14%/yr over 5 yrs; analysts see revenue +34% next year |
| 🟡 dip | VRTX | Other | 496.18 | 36.7 | 13.0 | -3.1% | -4.9% | 30.6 | FAIR -2% (HIGH) | 486.0 | +21% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | ROST | Other | 225.59 | 42.7 | 61.2 | -1.8% | -3.8% | 56.0 | FAIR -9% (HIGH) | 204.92 | +26% | STABLE [research: neutral] | steady | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |
| 🟡 dip | REGN | Other | 747.73 | 43.7 | 40.1 | -2.1% | -5.3% | 39.6 | FAIR +4% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +22% next year; R&D 41% of revenue |
| 🟡 dip | CL | Other | 89.62 | 59.5 | 74.3 | +3.2% | +0.5% | 4.2 | FAIR -8% (HIGH) | 82.19 | +12% | STABLE | steady |
| 🟡 dip | GM | Other | 82.64 | 50.3 | 71.4 | +1.0% | -2.3% | 46.4 | RICH -20% (LOW) | 65.63 | +24% | STABLE | cyclical: its multiples disagree with each other; analysts disagree | disruption: cyclical: judged on 5-yr trends |
| 🟡 dip | DIA | Index-ETF | 518.12 | 50.8 | 91.2 | +0.7% | -1.4% | 14.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -36% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +9% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 446.7 | 65.1 |  |
| VLO | 142.3 | 74.0 |  |
| RBRK | 21.7 | 61.4 | SPEC |
| DELL | 254.8 | 57.5 |  |
| CRWD | 90.7 | 58.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| OKLO | -75.4 | 32.8 | SPEC |
| ASTS | -26.9 | 31.9 | SPEC |
| UUUU | -39.3 | 25.5 | SPEC |
| QBTS | -49.0 | 27.5 | SPEC |
| APLD | -27.7 | 34.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._