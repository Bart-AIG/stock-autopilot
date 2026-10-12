# Strategy report - MORNING  (2026-10-12 14:14 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #9 | 21 EMA pullback | Other |  |  | ⚠️ 2026-10-21 | 656.85 | 46.3 | 656.85 | 627.23 | 679.61 | -4.5% |
| AMD | A+ | 12/12 | #13 | RSI2 dip | Semis |  | HELD |  | 597.07 | 5.6 | 597.07 | 550.2 | 649.42 | -7.8% |
| NVDA | A+ | 12/12 | #15 | RSI2 dip | Semis |  |  |  | 227.13 | 5.1 | 227.13 | 219.52 | 238.54 | -3.4% |
| QQQ | A+ | 12/12 | #16 | 21 EMA pullback | Index-ETF |  |  |  | 747.84 | 28.0 | 747.84 | 730.45 | 759.66 | -2.3% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** TMO (2026-10-21). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ARM (C 6/12), INTC (C 6/12), QCOM (C 5/12), HPQ (C 6/12), MU (C 8/12), SMCI (B 10/12)

## Quality ranking — top 25 of 224 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +228.7% | -0.4% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +49.9% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +44.0% | 0.0% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | SNOW | A+ | 12/12 | +28.2% | -1.4% | FAIR -4% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | DELL | A+ | 12/12 | +23.9% | -0.9% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | CRWD | A+ | 12/12 | +23.8% | -3.8% | EXPENSIVE -49% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | LITE | A+ | 12/12 | +23.6% | -8.6% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | NET | A+ | 12/12 | +21.4% | -2.5% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | TMO | A+ | 12/12 | +19.4% | -3.3% | RICH -15% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | PANW | A+ | 12/12 | +13.1% | -2.0% | EXPENSIVE -50% (LOW) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | PM | A+ | 12/12 | +11.4% | 0.0% | EXPENSIVE -32% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | ABBV | A+ | 12/12 | +10.3% | 0.0% | EXPENSIVE -45% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMD | A+ | 12/12 | +5.4% | -8.1% | EXPENSIVE -36% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AAPL | A+ | 12/12 | +5.0% | 0.0% | EXPENSIVE -36% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | NVDA | A+ | 12/12 | +3.7% | -5.1% | FAIR -1% (MED) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | QQQ | A+ | 12/12 | +0.4% | -1.6% | N/A | N/A | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PLTR | A+ | 11/12 | +52.4% | -0.2% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | RBRK | A+ | 11/12 | +37.9% | -1.0% | EXPENSIVE -31% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MSFT | A+ | 11/12 | +36.6% | -0.5% | RICH -17% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | COP | A+ | 11/12 | +18.9% | -3.0% | RICH -16% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | MRK | A+ | 11/12 | +17.2% | -6.8% | EXPENSIVE -38% (MED) | STABLE | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | FCX | A+ | 11/12 | +15.5% | -7.7% | EXPENSIVE -44% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | XOM | B | 11/12 | +15.2% | 0.0% | EXPENSIVE -36% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | WBD | B | 11/12 | +14.9% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | AMGN | B | 11/12 | +13.3% | -6.5% | RICH -22% (HIGH) | INNOVATING | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 21 of 219)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MU | 520.3 | 44.3 | T |
| 2 **TOP** | MRNA | 512.4 | 71.5 | T |
| 3 **TOP** | LITE | 468.7 | 54.7 | T |
| 4 **TOP** | WDC | 357.9 | 36.5 | F |
| 5 **TOP** | DELL | 353.7 | 60.7 | T |
| 6 **TOP** | INTC | 327.5 | 40.7 | T |
| 7 **TOP** | AAOI | 289.2 | 46.0 | F |
| 8 **TOP** | MRVL | 250.6 | 59.7 | T |
| 9 **TOP** | AMD | 225.5 | 53.8 | T |
| 10 **TOP** | VIAV | 222.1 | 57.1 | T |
| 11 **TOP** | COHR | 196.5 | 48.1 | T |
| 12 **TOP** | AMAT | 172.0 | 51.1 | T |
| 13 **TOP** | LRCX | 155.0 | 48.3 | T |
| 14 **TOP** | VLO | 149.1 | 72.8 | T |
| 15 **TOP** | FCEL | 131.3 | 47.3 | T |
| 16 **TOP** | MPC | 119.6 | 76.0 | T |
| 17 **TOP** | MTSI | 108.5 | 58.8 | T |
| 18 **TOP** | PSX | 98.4 | 73.0 | T |
| 19 **TOP** | CAT | 89.7 | 47.2 | T |
| 20 **TOP** | CRWD | 89.6 | 60.1 | T |
| 21 **TOP** | KLAC | 87.4 | 51.2 | T |
| 22  | NUE | 83.5 | 52.9 | T |
| 23  | ARM | 75.8 | 41.6 | T |
| 24  | MRK | 73.8 | 52.1 | T |
| 25  | TGT | 73.2 | 40.5 | T |
| 26  | FDX | 68.8 | 42.0 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 986.47 | 44.3 | 8.4 | -5.3% | +0.7% | 520.3 | EXPENSIVE -50% (LOW) | 490.58 | +53% | DISRUPTOR | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year |
| 🟡 dip | AUR | Other | 5.76 | 44.5 | 43.6 | -3.2% | -7.2% | 13.4 | N/A | — | — | INNOVATING | preprofit: not enough history for this industry's multiples | disruption: revenue -47%/yr, unwinding a one-time boom (peak 27x today's); analysts see revenue +392% next year |
| 🟡 dip | AMZN | Other | 261.18 | 57.5 | 64.7 | +3.5% | +0.9% | 12.5 | DEEP VALUE +100% (LOW) | 520.91 | +25% | INNOVATING | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%) |
| 🟡 dip | CRDO | Other | 206.7 | 51.9 | 20.5 | +5.1% | -1.5% | 0.6 | EXPENSIVE -42% (MED) | 116.44 | +35% | DISRUPTOR | cyclical: analysts disagree | disruption: revenue +87%/yr over 5 yrs; analysts see revenue +87% next year |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | QCOM | Semis | 172.87 | 42.1 | 1.6 | -6.8% | -0.4% | 12.4 | FAIR +0% (HIGH) | 173.33 | +10% | INNOVATING | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year |
| 🟢 oversold | ARM | Semis | 258.68 | 41.6 | 1.5 | -10.8% | -4.3% | 75.8 | N/A | — | — | DISRUPTOR | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year |
| 🟢 oversold | LRCX | Semis | 313.32 | 48.3 | 2.4 | +0.2% | +0.7% | 155.0 | EXPENSIVE -50% (MED) | 154.85 | +18% | INNOVATING | cyclical: far from its own history: the market has re-rated it, find out why | disruption: analysts see revenue +50% next year; gross margin up 4 pts (50%) |
| 🟢 oversold | HPQ | Other | 29.23 | 39.0 | 6.2 | -8.7% | -5.9% | 26.9 | UNDERVALUED +10% (MED) | 32.61 | -14% | AT RISK | **VALUE TRAP?** growth: analysts disagree | disruption: revenue shrinking -4%/yr over 3 yrs |
| 🟡 dip | ROST | Other | 222.79 | 37.0 | 23.7 | -2.9% | -5.2% | 56.0 | FAIR -8% (HIGH) | 204.91 | +27% | STABLE | steady | disruption: analysts see revenue +13% next year |
| 🟡 dip | REGN | Other | 759 | 47.4 | 93.8 | -0.7% | -3.9% | 39.6 | FAIR +2% (HIGH) | 780.09 | +12% | INNOVATING | steady | disruption: analysts see revenue +21% next year; R&D 41% of revenue |
| 🟡 dip | VRTX | Other | 513.78 | 48.7 | 89.5 | +0.1% | -1.4% | 30.6 | FAIR -5% (HIGH) | 486.0 | +17% | INNOVATING | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%) |
| 🟡 dip | KO | Other | 88.76 | 57.9 | 94.7 | +1.6% | +0.9% | 31.8 | FAIR +1% (HIGH) | 90.21 | +7% | STABLE | steady |
| 🟡 dip | IWM | Index-ETF | 278.42 | 37.6 | 40.9 | -1.1% | -4.4% | 21.2 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | COHR | Photonics | 300.17 | 48.1 | 22.1 | -2.1% | -1.5% | 196.5 | EXPENSIVE -50% (LOW) | 147.21 | +43% | INNOVATING | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +49% next year |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
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
| MRNA | 423.0 | 71.5 |  |
| VLO | 141.0 | 72.8 |  |
| SNOW | 31.2 | 65.1 |  |
| DELL | 263.8 | 60.7 |  |
| CRWD | 62.4 | 60.1 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| OKLO | -73.8 | 35.7 | SPEC |
| UUUU | -34.3 | 27.9 | SPEC |
| QBTS | -52.1 | 29.9 | SPEC |
| ASTS | -31.0 | 39.5 | SPEC |
| SOUN | -66.3 | 26.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._