# Strategy report - INTRADAY  (2026-10-08 19:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NET | A+ | 12/12 | #9 | 21 EMA pullback | AI-software |  |  | 2026-10-29 | 337.79 | 10.3 | 337.79 | 311.49 | 359.49 | -7.8% |
| TMO | A+ | 12/12 | #10 | 21 EMA pullback | Other |  |  | ⚠️ 2026-10-21 | 649.3 | 23.4 | 649.3 | 619.65 | 679.61 | -4.6% |
| NVDA | A+ | 12/12 | #14 | 21 EMA pullback | Semis |  |  |  | 230.38 | 11.2 | 230.38 | 221.49 | 239.24 | -3.9% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** TMO (2026-10-21). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ARM (C 8/12), INTC (C 8/12), QCOM (C 6/12), DE (C 5/12), COHR (C 8/12)

## Quality ranking — top 25 of 227 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +184.3% | -3.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +61.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +55.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +46.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | RBRK | A+ | 12/12 | +40.7% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | CRWD | A+ | 12/12 | +38.9% | -5.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | DELL | A+ | 12/12 | +30.1% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | LITE | A+ | 12/12 | +28.1% | -7.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | NET | A+ | 12/12 | +24.3% | -5.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | TMO | A+ | 12/12 | +20.6% | -4.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | PANW | A+ | 12/12 | +20.4% | -4.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PM | A+ | 12/12 | +8.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMD | A+ | 12/12 | +8.1% | -5.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | NVDA | A+ | 12/12 | +6.7% | -3.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | AAPL | A+ | 12/12 | +5.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | QQQ | A+ | 12/12 | +0.5% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +53.2% | -4.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MSFT | A+ | 11/12 | +33.2% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | COP | A+ | 11/12 | +20.7% | -5.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 20 | XOM | A+ | 11/12 | +19.1% | -1.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | CVX | A+ | 11/12 | +17.7% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | WBD | A+ | 11/12 | +16.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | DVN | B | 11/12 | +13.7% | -5.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | ABBV | B | 11/12 | +7.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | META | B | 11/12 | +5.0% | -7.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 221)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 660.9 | 51.6 | T |
| 2 **TOP** | LITE | 555.0 | 57.8 | T |
| 3 **TOP** | MRNA | 465.2 | 63.2 | T |
| 4 **TOP** | WDC | 411.6 | 37.4 | F |
| 5 **TOP** | AAOI | 372.1 | 47.9 | F |
| 6 **TOP** | DELL | 334.0 | 59.9 | T |
| 7 **TOP** | INTC | 326.8 | 45.1 | T |
| 8 **TOP** | FCEL | 320.9 | 48.5 | T |
| 9 **TOP** | MRVL | 241.5 | 60.6 | T |
| 10 **TOP** | AMD | 234.0 | 59.9 | T |
| 11 **TOP** | VIAV | 233.8 | 57.1 | T |
| 12 **TOP** | COHR | 205.9 | 49.5 | T |
| 13 **TOP** | LRCX | 205.0 | 51.3 | T |
| 14 **TOP** | AMAT | 191.8 | 54.7 | T |
| 15 **TOP** | VLO | 143.3 | 77.2 | T |
| 16 **TOP** | WBD | 127.7 | 75.2 | T |
| 17 **TOP** | MPC | 119.5 | 79.9 | T |
| 18 **TOP** | ILMN | 115.0 | 56.9 | T |
| 19 **TOP** | MTSI | 111.0 | 61.3 | T |
| 20 **TOP** | KLAC | 107.9 | 55.1 | T |
| 21 **TOP** | APLD | 103.5 | 39.7 | F |
| 22 **TOP** | PSX | 99.0 | 74.4 | T |
| 23  | CRWD | 96.2 | 60.5 | T |
| 24  | CAT | 94.5 | 43.0 | F |
| 25  | WULF | 94.1 | 36.5 | F |
| 26  | ARM | 88.0 | 45.9 | T |
| 27  | IREN | 79.2 | 34.8 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AUR | Other | 5.68 | 42.1 | 29.5 | -5.5% | -8.8% | 13.0 | N/A | — | — | INNOVATING | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year |
| 🟡 dip | AMZN | Other | 254.52 | 51.3 | 37.6 | +1.1% | -1.6% | 9.0 | DEEP VALUE +100% (LOW) | 516.93 | +26% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |
| 🟡 dip | GOOGL | Other | 347.95 | 53.1 | 47.2 | +0.8% | +0.6% | 44.6 | RICH -24% (LOW) | 266.32 | +22% | DISRUPTOR | growth: business changed (margin 73% vs 33% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: revenue +13%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟡 dip | CRDO | Other | 209.97 | 54.1 | 22.1 | +9.9% | +0.2% | 13.7 | EXPENSIVE -44% (MED) | 117.82 | +30% | DISRUPTOR | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QCOM | Semis | 174.29 | 43.5 | 4.8 | -6.4% | +1.0% | 8.6 | FAIR -1% (HIGH) | 173.34 | +9% | INNOVATING | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year |
| 🟢 oversold | COHR | Photonics | 305.24 | 49.5 | 9.4 | +0.2% | +0.8% | 205.9 | EXPENSIVE -50% (LOW) | 152.21 | +38% | INNOVATING | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +49% next year |
| 🟢 oversold | DE | Other | 649.53 | 41.1 | 6.7 | -4.7% | -0.4% | 41.4 | EXPENSIVE -44% (HIGH) | 365.56 | +13% | STABLE | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%) |
| 🟡 dip | REGN | Other | 736.52 | 38.1 | 39.3 | -4.1% | -6.7% | 45.1 | FAIR +6% (HIGH) | 780.09 | +15% | INNOVATING | steady | disruption: analysts see revenue +20% next year; R&D 41% of revenue |
| 🟡 dip | VRTX | Other | 505.87 | 41.1 | 62.5 | -1.6% | -2.7% | 33.8 | FAIR -4% (HIGH) | 484.31 | +20% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | ROST | Other | 226.52 | 42.2 | 58.4 | -1.7% | -4.1% | 51.3 | FAIR -9% (HIGH) | 204.94 | +26% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟡 dip | GM | Other | 82.16 | 49.1 | 75.1 | -0.2% | -3.3% | 47.4 | FAIR -6% (MED) | 76.59 | +25% | STABLE | cyclical: TROUGH-CYCLE margins (7% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |
| 🟡 dip | KO | Other | 87.82 | 53.0 | 87.3 | +0.5% | -0.2% | 31.0 | FAIR +4% (HIGH) | 90.2 | +10% | STABLE | steady |
| 🟡 dip | DIA | Index-ETF | 510.96 | 40.3 | 32.0 | -0.9% | -2.9% | 15.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | NEM | Other | 115.21 | 42.5 | 56.0 | -4.0% | -3.7% | 67.8 | EXPENSIVE -33% (LOW) | 76.96 | +20% | STABLE | cyclical: PEAK-CYCLE margins (65% vs 33% normal): earnings multiples ignored; analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +107% next year |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +48% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -38% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | yes | UNDERVALUED +16% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 396.0 | 63.2 |  |
| PSX | 97.0 | 74.4 |  |
| RBRK | 11.7 | 64.1 | SPEC |
| CRWD | 71.5 | 60.5 |  |
| DELL | 254.8 | 59.9 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| APP | -51.7 | 35.9 |  |
| RCAT | -45.0 | 26.1 | SPEC |
| OKLO | -68.3 | 38.1 | SPEC |
| QBTS | -52.1 | 31.9 | SPEC |
| UUUU | -17.3 | 28.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._