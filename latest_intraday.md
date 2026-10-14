# Strategy report - INTRADAY  (2026-10-14 17:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRWD | A+ | 12/12 | #7 | 21 EMA pullback | AI-software |  |  |  | 251.35 | 10.3 | 251.35 | 233.08 | 278.76 | -7.3% |
| AMD | A+ | 11/12 | #23 | 21 EMA pullback | Semis |  | HELD | 2026-11-03 | 573.36 | 13.4 | 573.36 | 524.13 | 647.21 | -8.6% |

### How to read this (concentration & sizing)
- 📌 **Already held (marked HELD):** AMD. A new buy ADDS to the existing position — skip unless you mean to add, and re-check the per-name cap on the combined size.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): AMAT (C 4/12), LRCX (C 3/12), ARM (C 6/12), SMCI (C 7/12), NBIS (C 4/12), MU (C 7/12), DELL (B 10/12), QQQI (C 6/12), CRDO (C 2/12), QQQ (B 10/12), VIAV (C 7/12), AFRM (C 5/12), LITE (B 9/12), GEV (C 6/12), ROKU (C 7/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +250.8% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +54.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +50.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +44.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | COP | A+ | 12/12 | +23.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +21.3% | -1.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CRWD | A+ | 12/12 | +21.1% | -9.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | XOM | A+ | 12/12 | +18.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | CVX | A+ | 12/12 | +18.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WBD | A+ | 12/12 | +15.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | DVN | A+ | 12/12 | +14.2% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | OXY | A+ | 12/12 | +12.6% | -6.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +9.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EOG | A+ | 12/12 | +8.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | ADI | A+ | 12/12 | +4.2% | -8.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | PM | A+ | 12/12 | +4.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | AAPL | A+ | 12/12 | +0.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PLTR | A+ | 11/12 | +48.4% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MSFT | A+ | 11/12 | +31.0% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | PFE | A+ | 11/12 | +13.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 21 | EMR | A+ | 11/12 | +12.9% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 22 | MRK | A+ | 11/12 | +12.8% | -5.9% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | AMD | A+ | 11/12 | +12.0% | -11.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | AMGN | B | 11/12 | +11.7% | -4.4% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | KO | B | 11/12 | +5.3% | -0.4% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 523.9 | 68.3 | T |
| 2 **TOP** | MU | 487.7 | 38.0 | T |
| 3 **TOP** | LITE | 412.2 | 43.9 | T |
| 4 **TOP** | WDC | 337.2 | 32.9 | F |
| 5 **TOP** | DELL | 327.3 | 42.2 | T |
| 6 **TOP** | INTC | 303.6 | 39.1 | T |
| 7 **TOP** | AAOI | 253.7 | 38.2 | F |
| 8 **TOP** | MRVL | 224.9 | 48.1 | T |
| 9 **TOP** | AMD | 211.2 | 47.2 | T |
| 10 **TOP** | VIAV | 181.1 | 44.9 | T |
| 11 **TOP** | COHR | 158.8 | 40.2 | F |
| 12 **TOP** | AMAT | 152.8 | 37.1 | T |
| 13 **TOP** | VLO | 144.4 | 76.2 | T |
| 14 **TOP** | NBIS | 134.7 | 35.5 | T |
| 15 **TOP** | LRCX | 133.8 | 37.6 | T |
| 16 **TOP** | FCEL | 122.4 | 39.6 | F |
| 17 **TOP** | MPC | 119.9 | 79.1 | T |
| 18 **TOP** | CRWD | 115.9 | 50.4 | T |
| 19 **TOP** | UMAC | 115.8 | 32.5 | F |
| 20 **TOP** | PSX | 96.6 | 78.3 | T |
| 21 **TOP** | PANW | 90.5 | 47.0 | T |
| 22 **TOP** | CAT | 81.7 | 34.0 | F |
| 23  | MTSI | 81.7 | 48.9 | T |
| 24  | NUE | 80.1 | 55.9 | T |
| 25  | SCCO | 79.5 | 49.4 | T |
| 26  | TGT | 76.4 | 45.4 | T |
| 27  | KLAC | 75.4 | 39.8 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | MU | Semis | 932.01 | 38.0 | 2.3 | -10.6% | -5.2% | 487.7 | EXPENSIVE -50% (LOW) | 472.12 | +59% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟢 oversold | QQQI | Other | 55.12 | 45.7 | 3.3 | -1.0% | +0.1% | 0.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | QQQ | Index-ETF | 731.59 | 46.2 | 3.6 | -1.5% | +0.7% | 20.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | NVDA | Semis | 222.59 | 45.2 | 13.2 | -2.7% | -0.3% | 18.6 | FAIR -1% (MED) | 223.03 | +45% | DISRUPTOR | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year |
| 🟡 dip | AMZN | Other | 254.45 | 49.7 | 17.4 | +0.5% | -1.3% | 11.1 | DEEP VALUE +100% (LOW) | 514.02 | +26% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NBIS | Other | 186.74 | 35.5 | 1.8 | -18.1% | -16.6% | 134.7 | EXPENSIVE -50% (LOW) | 93.15 | +76% | DISRUPTOR | growth: business changed (margin 74% vs 23% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +240%/yr over 3 yrs; analysts see revenue +531% next year |
| 🟢 oversold | ARM | Semis | 242.85 | 37.1 | 0.8 | -16.3% | -10.0% | 58.7 | N/A | — | — | DISRUPTOR [research: disruptor] | preprofit: not enough history for this industry's multiples | disruption: revenue +22%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-12: Arm-based hyperscaler CPUs are displacing x86 servers (data-center royalties reportedly more than doubled in FY2026) and Arm now sells its own data-center CPU; RISC-V is a long-term threat, strongest in low-cost embedded chips. |
| 🟢 oversold | AMAT | Semis | 449.8 | 37.1 | 0.3 | -8.5% | -7.6% | 152.8 | EXPENSIVE -50% (LOW) | 227.72 | +42% | INNOVATING [research: neutral] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 5 yrs; analysts see revenue +21% next year; research 2026-10-13: Broadest equipment maker, gains from AI chip demand, but Mizuho expects it to lag the WFE market as Chinese rivals (AMEC, Naura) win domestic share in core tools; date of that note is unclear, so evidence is thin. |
| 🟢 oversold | LRCX | Semis | 287.63 | 37.6 | 0.3 | -8.7% | -7.4% | 133.8 | EXPENSIVE -50% (LOW) | 146.66 | +24% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +51% next year; gross margin up 4 pts (50%); research 2026-10-13: Etch/deposition leader benefiting from AI and memory tightness (RBC, Apr 2026); China exposure falling as global spend rises. Chinese etch makers (AMEC, Naura) are a share risk inside China, not yet visible in results. |
| 🟢 oversold | GEV | Nuclear | 938.43 | 43.0 | 6.8 | -3.4% | -3.0% | 39.8 | N/A | — | — | STABLE | cyclical: PEAK-CYCLE margins (22% vs 3% normal): earnings multiples ignored; not enough history for this industry's multiples | disruption: analysts see revenue +22% next year; cyclical: judged on 3-yr trends |
| 🟢 oversold | VIAV | Photonics | 39.22 | 44.9 | 5.6 | -5.1% | -0.6% | 181.1 | EXPENSIVE -50% (LOW) | 20.56 | +52% | INNOVATING | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟢 oversold | SPY | Index-ETF | 770.25 | 50.2 | 7.2 | -0.0% | +0.2% | 15.7 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | BHP | Other | 83.36 | 38.7 | 8.9 | -2.6% | -6.2% | 56.7 | EXPENSIVE -25% (HIGH) | 62.0 | +15% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | DELL | Other | 509.3 | 42.2 | 2.9 | -8.9% | -0.7% | 327.3 | EXPENSIVE -50% (MED) | 265.69 | +7% | STABLE | growth: far from its own history: the market has re-rated it, find out why | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| 🟢 oversold | ETN | Other | 412.63 | 42.9 | 8.1 | -4.3% | -3.1% | 7.5 | EXPENSIVE -34% (MED) | 275.86 | +20% | INNOVATING | steady: analysts disagree | disruption: analysts see revenue +20% next year; gross margin up 4 pts (38%) |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | yes | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | no | EXPENSIVE -50% (MED) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -47% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -36% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +47% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | FAIR +8% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 437.7 | 68.3 |  |
| COP | 59.1 | 71.3 |  |
| TMO | 22.3 | 60.2 |  |
| CRWD | 90.7 | 50.4 |  |
| XOM | 50.9 | 74.9 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| WULF | 3.5 | 28.9 | SPEC |
| OKLO | -79.0 | 29.3 | SPEC |
| DKNG | -26.6 | 33.5 |  |
| POET | -14.5 | 28.5 | SPEC |
| APLD | -31.6 | 31.1 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._