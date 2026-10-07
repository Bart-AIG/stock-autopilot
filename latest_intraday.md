# Strategy report - INTRADAY  (2026-10-07 18:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SNOW | A+ | 12/12 | #11 | 21 EMA pullback | AI-software |  |  |  | 336.58 | 33.5 | 336.58 | 324.01 | 341.99 | -3.7% |
| XOM | A+ | 11/12 | #18 | 21 EMA pullback | Energy |  |  |  | 163.74 | 33.8 | 163.74 | 158.12 | 169.32 | -3.4% |
| CVX | A+ | 11/12 | #20 | 21 EMA pullback | Energy |  |  |  | 205.4 | 24.5 | 205.4 | 198.82 | 215.27 | -3.2% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): JPM (C 6/12), QCOM (C 6/12), INOD (C 6/12), C (C 4/12), DE (B 8/12)

## Quality ranking — top 25 of 227 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +147.1% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +51.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +46.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +39.4% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LITE | A+ | 12/12 | +38.1% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | RBRK | A+ | 12/12 | +37.1% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +31.5% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | DELL | A+ | 12/12 | +25.9% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +22.8% | -2.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | NET | A+ | 12/12 | +22.6% | -3.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | SNOW | A+ | 12/12 | +22.4% | -5.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PANW | A+ | 12/12 | +17.3% | -2.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMD | A+ | 12/12 | +14.4% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | NVDA | A+ | 12/12 | +13.4% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | QQQ | A+ | 12/12 | +1.2% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PLTR | A+ | 11/12 | +46.4% | -6.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MSFT | A+ | 11/12 | +34.4% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | XOM | A+ | 11/12 | +15.7% | -4.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 19 | WBD | A+ | 11/12 | +15.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 20 | CVX | A+ | 11/12 | +14.6% | -5.7% | RICH -20% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | META | A+ | 11/12 | +11.2% | -6.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | ABBV | A+ | 11/12 | +5.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | ETN | B | 11/12 | +2.6% | -6.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | SMCI | B | 10/12 | +54.8% | -23.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | ILMN | B | 10/12 | +36.9% | -7.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 221)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 673.8 | 59.2 | T |
| 2 **TOP** | LITE | 489.6 | 66.7 | T |
| 3 **TOP** | MRNA | 479.0 | 62.1 | T |
| 4 **TOP** | WDC | 407.9 | 39.2 | T |
| 5 **TOP** | AAOI | 339.9 | 59.2 | T |
| 6 **TOP** | DELL | 319.9 | 61.3 | T |
| 7 **TOP** | INTC | 291.2 | 52.2 | T |
| 8 **TOP** | FCEL | 269.1 | 50.9 | T |
| 9 **TOP** | MRVL | 253.0 | 65.7 | T |
| 10 **TOP** | AMD | 216.0 | 70.0 | T |
| 11 **TOP** | VIAV | 199.0 | 67.3 | T |
| 12 **TOP** | LRCX | 198.8 | 55.1 | T |
| 13 **TOP** | COHR | 188.1 | 59.7 | T |
| 14 **TOP** | AMAT | 179.4 | 59.9 | T |
| 15 **TOP** | VLO | 136.5 | 71.1 | T |
| 16 **TOP** | WBD | 133.3 | 75.2 | T |
| 17 **TOP** | ILMN | 120.6 | 61.8 | T |
| 18 **TOP** | MPC | 115.7 | 73.9 | T |
| 19 **TOP** | MTSI | 107.1 | 67.9 | T |
| 20 **TOP** | KLAC | 105.1 | 55.3 | T |
| 21 **TOP** | CRWD | 104.1 | 62.9 | T |
| 22 **TOP** | PSX | 93.9 | 68.0 | T |
| 23  | CAT | 92.4 | 47.2 | T |
| 24  | APLD | 89.8 | 41.9 | F |
| 25  | ARM | 82.4 | 54.5 | T |
| 26  | WULF | 80.8 | 39.2 | F |
| 27  | MRK | 77.5 | 45.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | AUR | Other | 5.67 | 41.8 | 32.7 | -6.1% | -9.0% | 10.6 | N/A | — | — | INNOVATING | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year |
| 🟡 dip | GOOGL | Other | 348.46 | 54.1 | 87.4 | +1.2% | +0.8% | 44.0 | RICH -23% (LOW) | 264.67 | +23% | DISRUPTOR | growth: business changed (margin 73% vs 33% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: revenue +13%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟡 dip | AMZN | Other | 258.77 | 57.3 | 97.8 | +2.9% | +0.3% | 11.3 | DEEP VALUE +100% (LOW) | 509.88 | +28% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QCOM | Semis | 175.91 | 44.9 | 8.0 | -5.6% | +2.2% | 5.6 | FAIR -2% (HIGH) | 173.3 | +8% | INNOVATING | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year |
| 🟢 oversold | JPM | Other | 328.95 | 31.4 | 5.2 | -3.7% | -6.2% | 21.8 | EXPENSIVE -30% (HIGH) | 228.96 | +13% | STABLE | bank |
| 🟢 oversold | C | Other | 126.46 | 35.2 | 8.7 | -4.3% | -5.4% | 44.4 | EXPENSIVE -29% (HIGH) | 90.03 | +19% | STABLE | bank |
| 🟢 oversold | DE | Other | 660.62 | 44.8 | 9.9 | -3.3% | +1.4% | 46.5 | EXPENSIVE -45% (HIGH) | 372.18 | +10% | STABLE | cyclical | disruption: analysts expect revenue -7% next year; gross margin up 5 pts (36%) |
| 🟡 dip | OXY | Energy | 57.86 | 48.5 | 35.0 | -0.9% | -1.2% | 30.8 | UNDERVALUED +10% (HIGH) | 64.33 | +21% | STABLE | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟡 dip | REGN | Other | 745.31 | 41.0 | 76.5 | -3.3% | -5.5% | 44.4 | FAIR +5% (HIGH) | 780.09 | +14% | INNOVATING | steady | disruption: analysts see revenue +20% next year; R&D 41% of revenue |
| 🟡 dip | KO | Other | 86.14 | 41.9 | 43.0 | -1.5% | -2.1% | 29.6 | FAIR +4% (HIGH) | 90.21 | +10% | STABLE | steady |
| 🟡 dip | VRTX | Other | 507.14 | 42.2 | 67.9 | -1.5% | -2.4% | 37.9 | FAIR -5% (HIGH) | 484.37 | +18% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | ROST | Other | 227.25 | 43.3 | 56.4 | -1.4% | -4.0% | 52.8 | FAIR -8% (HIGH) | 207.27 | +25% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟡 dip | GM | Other | 81.16 | 46.7 | 57.9 | -1.7% | -4.6% | 50.6 | FAIR -6% (MED) | 76.59 | +24% | STABLE | cyclical: TROUGH-CYCLE margins (7% vs 13% normal): earnings multiples ignored | disruption: cyclical: judged on 5-yr trends |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +107% next year |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | yes | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +48% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -38% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | yes | UNDERVALUED +12% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 409.5 | 62.1 |  |
| MPC | 105.5 | 73.9 |  |
| VLO | 134.3 | 71.1 |  |
| PSX | 95.0 | 68.0 |  |
| LITE | 509.3 | 66.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| APP | -46.8 | 34.8 |  |
| RCAT | -40.3 | 28.5 | SPEC |
| JOBY | -65.0 | 28.3 | SPEC |
| QBTS | -49.5 | 35.6 | SPEC |
| DKNG | -31.8 | 33.6 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._