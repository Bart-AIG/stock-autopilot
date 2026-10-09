# Strategy report - MORNING  (2026-10-09 14:10 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NVDA | A+ | 12/12 | #11 | 21 EMA pullback | Semis |  |  |  | 230.79 | 17.1 | 230.79 | 221.92 | 239.24 | -3.8% |
| AAPL | A+ | 12/12 | #15 | 21 EMA pullback | Other |  |  |  | 332.25 | 25.7 | 332.25 | 323.0 | 341.07 | -2.8% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): QCOM (C 6/12), ARM (C 8/12), INTC (C 7/12), DE (C 7/12), ROST (C 2/12)

## Quality ranking — top 25 of 226 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +216.8% | 0.0% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +53.4% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +46.8% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +39.9% | 0.0% | EXPENSIVE -45% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CRWD | A+ | 12/12 | +38.4% | -4.3% | EXPENSIVE -48% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | LITE | A+ | 12/12 | +37.7% | -4.3% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | DELL | A+ | 12/12 | +31.7% | -1.8% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | TMO | A+ | 12/12 | +21.0% | -3.1% | RICH -15% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | PANW | A+ | 12/12 | +20.0% | -2.8% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMD | A+ | 12/12 | +11.4% | -5.4% | EXPENSIVE -37% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | NVDA | A+ | 12/12 | +9.8% | -3.5% | FAIR -4% (MED) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PM | A+ | 12/12 | +7.8% | 0.0% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +7.4% | 0.0% | EXPENSIVE -45% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | QQQ | A+ | 12/12 | +1.7% | -1.4% | N/A | N/A | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | AAPL | A+ | 12/12 | +1.1% | -2.6% | EXPENSIVE -34% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PLTR | A+ | 11/12 | +50.7% | -3.2% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | RBRK | A+ | 11/12 | +40.7% | -3.9% | EXPENSIVE -30% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +31.4% | -2.6% | RICH -16% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | COP | A+ | 11/12 | +16.4% | -4.1% | RICH -15% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 20 | WBD | A+ | 11/12 | +14.9% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | XOM | A+ | 11/12 | +13.9% | -1.0% | EXPENSIVE -35% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | MRK | A+ | 11/12 | +12.8% | -7.8% | EXPENSIVE -37% (MED) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | DVN | B | 11/12 | +8.6% | -5.8% | RICH -15% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | DDOG | B | 11/12 | +4.0% | -2.8% | EXPENSIVE -28% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | ADI | B | 11/12 | +1.0% | -9.3% | EXPENSIVE -46% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 22 of 220)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 660.0 | 51.8 | T |
| 2 **TOP** | LITE | 551.8 | 61.2 | T |
| 3 **TOP** | MRNA | 454.2 | 69.5 | T |
| 4 **TOP** | WDC | 410.1 | 36.4 | F |
| 5 **TOP** | AAOI | 355.0 | 49.7 | F |
| 6 **TOP** | DELL | 341.3 | 60.1 | T |
| 7 **TOP** | INTC | 334.7 | 44.8 | T |
| 8 **TOP** | MRVL | 251.6 | 58.9 | T |
| 9 **TOP** | VIAV | 235.2 | 60.0 | T |
| 10 **TOP** | AMD | 234.4 | 59.2 | T |
| 11 **TOP** | FCEL | 219.9 | 48.6 | T |
| 12 **TOP** | COHR | 205.9 | 49.7 | T |
| 13 **TOP** | LRCX | 199.2 | 52.0 | T |
| 14 **TOP** | AMAT | 186.8 | 55.7 | T |
| 15 **TOP** | VLO | 140.3 | 77.4 | T |
| 16 **TOP** | WBD | 127.7 | 75.2 | T |
| 17 **TOP** | MTSI | 120.4 | 60.5 | T |
| 18 **TOP** | MPC | 118.1 | 80.1 | T |
| 19 **TOP** | KLAC | 99.3 | 57.0 | T |
| 20 **TOP** | PSX | 97.1 | 76.2 | T |
| 21 **TOP** | CRWD | 96.3 | 61.4 | T |
| 22 **TOP** | CAT | 95.1 | 44.0 | F |
| 23  | ARM | 87.7 | 45.4 | T |
| 24  | NUE | 82.9 | 53.4 | T |
| 25  | APLD | 78.6 | 40.4 | F |
| 26  | MRK | 74.4 | 49.0 | T |
| 27  | FCX | 73.7 | 56.1 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AUR | Other | 5.8 | 45.6 | 90.6 | -3.0% | -6.8% | 14.0 | N/A | — | — | INNOVATING | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year |
| 🟡 dip | AMZN | Other | 258.39 | 55.4 | 66.8 | +2.6% | -0.2% | 5.9 | DEEP VALUE +100% (LOW) | 517.46 | +26% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | ROST | Other | 220.71 | 34.3 | 6.2 | -4.0% | -6.3% | 51.1 | FAIR -7% (HIGH) | 204.92 | +28% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟢 oversold | QCOM | Semis | 173.22 | 42.5 | 2.6 | -6.8% | +0.1% | 11.2 | FAIR -1% (HIGH) | 173.41 | +9% | INNOVATING | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year |
| 🟢 oversold | ARM | Semis | 271.5 | 45.4 | 3.4 | -6.1% | +0.6% | 87.7 | N/A | — | — | DISRUPTOR | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year |
| 🟢 oversold | DE | Other | 650.12 | 41.2 | 5.7 | -4.4% | -0.5% | 42.4 | EXPENSIVE -43% (HIGH) | 372.37 | +13% | STABLE | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%) |
| 🟢 oversold | BMY | Other | 59.55 | 35.0 | 32.4 | -3.7% | -7.1% | 36.4 | DEEP VALUE +42% (MED) | 84.83 | +9% | BEING DISRUPTED | **VALUE TRAP?** steady: analysts disagree | disruption: revenue flat (+1%/yr over 3 yrs); gross margin down 5 pts vs 5-yr median (71%) |
| 🟡 dip | REGN | Other | 746.77 | 42.2 | 80.9 | -2.6% | -5.4% | 45.1 | FAIR +4% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +21% next year; R&D 41% of revenue |
| 🟡 dip | VRTX | Other | 512.63 | 47.7 | 85.3 | -0.3% | -1.5% | 31.4 | FAIR -6% (HIGH) | 486.0 | +17% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | KO | Other | 87.92 | 53.6 | 88.5 | +0.6% | -0.1% | 29.0 | FAIR +3% (HIGH) | 90.21 | +8% | STABLE | steady |
| 🟡 dip | IWM | Index-ETF | 278.66 | 37.8 | 51.1 | -1.2% | -4.4% | 22.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | DIA | Index-ETF | 513.3 | 44.0 | 72.2 | -0.3% | -2.4% | 14.4 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +107% next year |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +48% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -37% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +8% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 389.3 | 69.5 |  |
| CRWD | 63.8 | 61.4 |  |
| LITE | 473.7 | 61.2 |  |
| DELL | 207.9 | 60.1 |  |
| TMO | 12.5 | 54.6 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| APP | -50.1 | 36.3 |  |
| RCAT | -43.7 | 25.0 | SPEC |
| OKLO | -70.4 | 38.9 | SPEC |
| UUUU | -24.3 | 29.1 | SPEC |
| LULU | -44.6 | 33.2 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._