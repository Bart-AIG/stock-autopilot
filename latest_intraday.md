# Strategy report - INTRADAY  (2026-10-16 15:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLTR | A+ | 11/12 | #19 | RSI2 dip | AI-software |  |  | 2026-11-02 | 191.43 | 3.6 | 191.43 | 180.86 | 207.29 | -5.5% |

### How to read this (concentration & sizing)
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): SMCI (C 7/12), QQQI (C 3/12), QLD (C 6/12), DELL (B 8/12), QQQ (C 6/12), CRWD (B 8/12), NET (C 6/12), PANW (C 5/12), LITE (C 7/12), MRVL (C 7/12), INTC (C 4/12), DDOG (C 8/12), SNOW (C 7/12), ETN (C 1/12), CSCO (C 5/12)

## Quality ranking — top 25 of 237 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +260.8% | -8.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +47.3% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +37.9% | -3.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PSX | A+ | 12/12 | +35.7% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | TMO | A+ | 12/12 | +27.3% | -0.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | COP | A+ | 12/12 | +20.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | XOM | A+ | 12/12 | +14.8% | -0.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +14.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | GILD | A+ | 12/12 | +13.7% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | CVX | A+ | 12/12 | +13.0% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | KO | A+ | 12/12 | +9.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | DVN | A+ | 12/12 | +9.8% | -4.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +8.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | OXY | A+ | 12/12 | +7.3% | -7.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +6.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | ADI | A+ | 12/12 | +5.8% | -8.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | PM | A+ | 12/12 | +2.2% | -0.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | AAPL | A+ | 12/12 | +1.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PLTR | A+ | 11/12 | +40.3% | -7.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +28.9% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | ABNB | A+ | 11/12 | +17.2% | -7.8% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | AMGN | A+ | 11/12 | +16.2% | -1.5% | — | — | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | PFE | A+ | 11/12 | +15.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 24 | EMR | B | 11/12 | +15.5% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 25 | V | B | 11/12 | +7.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 225)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 486.2 | 61.2 | T |
| 2 **TOP** | MU | 483.4 | 36.3 | T |
| 3 **TOP** | LITE | 438.0 | 38.6 | T |
| 4 **TOP** | DELL | 341.2 | 35.0 | T |
| 5 **TOP** | WDC | 304.5 | 28.6 | F |
| 6 **TOP** | INTC | 299.9 | 33.4 | T |
| 7 **TOP** | AAOI | 234.4 | 34.6 | F |
| 8 **TOP** | MRVL | 233.6 | 40.7 | T |
| 9 **TOP** | AMD | 219.4 | 40.7 | T |
| 10 **TOP** | VIAV | 183.2 | 37.1 | F |
| 11 **TOP** | COHR | 177.5 | 34.4 | F |
| 12 **TOP** | VLO | 148.0 | 66.3 | T |
| 13 **TOP** | AMAT | 139.4 | 31.4 | F |
| 14 **TOP** | NBIS | 134.1 | 32.7 | T |
| 15 **TOP** | FCEL | 128.3 | 37.2 | F |
| 16 **TOP** | MPC | 126.2 | 74.2 | T |
| 17 **TOP** | LRCX | 123.5 | 31.9 | F |
| 18 **TOP** | CRWD | 117.0 | 40.6 | T |
| 19 **TOP** | PSX | 98.9 | 69.9 | T |
| 20 **TOP** | MTSI | 91.9 | 40.5 | F |
| 21 **TOP** | UMAC | 89.1 | 32.0 | F |
| 22 **TOP** | PANW | 86.6 | 39.3 | T |
| 23  | NUE | 82.4 | 61.8 | T |
| 24  | MRK | 78.7 | 52.8 | T |
| 25  | CAT | 77.6 | 32.8 | F |
| 26  | SCCO | 77.2 | 55.0 | T |
| 27  | TGT | 72.4 | 52.0 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NVDA | Semis | 217.56 | 40.6 | 6.1 | -4.7% | -2.5% | 22.3 | FAIR +3% (MED) | 223.06 | +50% | DISRUPTOR | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year |
| 🟢 oversold | QQQ | Index-ETF | 720.98 | 40.1 | 1.1 | -3.0% | -0.8% | 19.2 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟢 oversold | MRVL | Semis | 236.31 | 40.7 | 2.7 | -10.3% | -2.0% | 233.6 | EXPENSIVE -50% (LOW) | 116.75 | +48% | DISRUPTOR | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| 🟡 dip | MU | Semis | 903.33 | 36.3 | 14.4 | -12.6% | -8.2% | 483.4 | EXPENSIVE -50% (LOW) | 449.08 | +67% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | GOOGL | Other | 344.8 | 48.2 | 15.1 | -0.5% | +0.0% | 36.5 | RICH -23% (LOW) | 263.99 | +24% | DISRUPTOR | growth: business changed (margin 73% vs 33% 10-yr median): its own history is a weak yardstick; its multiples disagree with each other; analysts disagree | disruption: revenue +13%/yr over 3 yrs; analysts see revenue +24% next year |
| 🟡 dip | AMZN | Other | 254.61 | 49.9 | 28.1 | +0.5% | -1.0% | 5.1 | DEEP VALUE +100% (LOW) | 506.32 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | NET | AI-software | 298.6 | 36.5 | 1.9 | -13.6% | -6.7% | 48.1 | EXPENSIVE -48% (LOW) | 155.68 | +18% | DISRUPTOR | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +32% next year |
| 🟢 oversold | PANW | AI-software | 351.83 | 39.3 | 2.3 | -10.1% | -5.8% | 86.6 | EXPENSIVE -50% (LOW) | 177.54 | +17% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | SNOW | AI-software | 315.43 | 40.1 | 3.1 | -7.0% | -5.4% | 53.3 | FAIR +8% (LOW) | 341.13 | +38% | DISRUPTOR | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year |
| 🟢 oversold | CRWD | AI-software | 231.68 | 40.6 | 1.9 | -10.9% | -0.7% | 117.0 | EXPENSIVE -42% (LOW) | 136.42 | +2% | DISRUPTOR | preprofit | disruption: revenue +29%/yr over 3 yrs; analysts see revenue +25% next year |
| 🟢 oversold | DDOG | AI-software | 252.69 | 44.3 | 2.9 | -6.1% | +2.2% | 71.5 | RICH -21% (LOW) | 197.89 | +19% | DISRUPTOR | growth: business changed (margin 8% vs 2% 10-yr median): its own history is a weak yardstick | disruption: revenue +27%/yr over 3 yrs; analysts see revenue +31% next year |
| 🟢 oversold | ETN | Other | 399.51 | 37.7 | 3.1 | -7.0% | -5.7% | 7.2 | EXPENSIVE -31% (MED) | 275.81 | +25% | INNOVATING | steady: analysts disagree | disruption: analysts see revenue +20% next year; gross margin up 4 pts (38%) |
| 🟢 oversold | CSCO | Other | 108.51 | 43.0 | 3.2 | -2.4% | -2.8% | 61.0 | EXPENSIVE -44% (MED) | 60.4 | +25% | INNOVATING | growth: analysts disagree | disruption: analysts see revenue +15% next year; R&D 15% of revenue |
| 🟡 dip | QCOM | Semis | 176.85 | 47.3 | 53.8 | -3.8% | +1.0% | 12.6 | FAIR -2% (HIGH) | 171.17 | +9% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | VRTX | Other | 508.94 | 48.5 | 74.9 | -0.3% | -2.6% | 31.1 | FAIR -5% (HIGH) | 486.44 | +18% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟡 dip | USB | Other | 58.74 | 50.6 | 89.3 | +1.5% | -3.4% | 23.4 | FAIR +5% (HIGH) | 61.64 | +16% | STABLE | bank |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +108% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +109% next year |
| DELL | yes | EXPENSIVE -50% (LOW) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | yes | EXPENSIVE -47% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +49% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -34% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| INTC | yes | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year |
| ILMN | no | UNDERVALUED +13% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 470.2 | 61.2 |  |
| MPC | 129.5 | 74.2 |  |
| VLO | 156.3 | 66.3 |  |
| PSX | 111.6 | 69.9 |  |
| TMO | 24.7 | 64.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| WULF | 6.5 | 34.8 | SPEC |
| MOD | 5.0 | 33.8 |  |
| APLD | -30.1 | 28.3 | SPEC |
| OKLO | -76.9 | 30.9 | SPEC |
| QBTS | -60.5 | 27.9 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._