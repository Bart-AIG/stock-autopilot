# Strategy report - INTRADAY  (2026-10-26 19:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MRNA | A+ | 11/12 | #18 | 21 EMA pullback | Other |  |  | ⚠️ 2026-11-06 | 196.82 | 10.5 | 196.82 | 164.16 | 245.81 | -16.6% ⚠ |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MRNA (2026-11-06). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): META (C 6/12), MRK (C 5/12)

## Quality ranking — top 25 of 234 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | RBRK | A+ | 12/12 | +84.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | MPC | A+ | 12/12 | +50.6% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | VLO | A+ | 12/12 | +39.5% | -7.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | COP | A+ | 12/12 | +29.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CVX | A+ | 12/12 | +20.7% | -0.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | DVN | A+ | 12/12 | +17.8% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | XOM | A+ | 12/12 | +17.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | HPQ | A+ | 12/12 | +16.8% | -4.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | OXY | A+ | 12/12 | +15.7% | -3.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WBD | A+ | 12/12 | +15.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | TMO | A+ | 12/12 | +14.8% | -2.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | PFE | A+ | 12/12 | +14.6% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | EOG | A+ | 12/12 | +13.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | AMGN | A+ | 12/12 | +9.0% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | ABBV | A+ | 12/12 | +5.1% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | KO | A+ | 12/12 | +1.6% | -2.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | LLY | A+ | 12/12 | +1.5% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MRNA | A+ | 11/12 | +249.5% | -19.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PLTR | A+ | 11/12 | +58.1% | -4.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | CRWD | A+ | 11/12 | +41.1% | -5.9% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | MSFT | A+ | 11/12 | +32.0% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | SHOP | A+ | 11/12 | +25.9% | -6.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | DDOG | A+ | 11/12 | +9.3% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | V | B | 11/12 | +6.9% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | MA | B | 11/12 | +5.9% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 222)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 712.1 | 49.1 | T |
| 2 **TOP** | MU | 588.2 | 43.3 | T |
| 3 **TOP** | LITE | 485.8 | 42.9 | T |
| 4 **TOP** | DELL | 330.5 | 41.8 | T |
| 5 **TOP** | AMD | 295.5 | 43.1 | T |
| 6 **TOP** | AAOI | 293.5 | 36.7 | F |
| 7 **TOP** | INTC | 246.5 | 39.6 | T |
| 8 **TOP** | VIAV | 233.2 | 38.6 | F |
| 9 **TOP** | MRVL | 214.9 | 45.3 | T |
| 10 **TOP** | COHR | 176.5 | 36.0 | F |
| 11 **TOP** | LRCX | 145.6 | 30.2 | F |
| 12 **TOP** | AMAT | 137.8 | 31.9 | F |
| 13 **TOP** | ARM | 122.3 | 38.7 | F |
| 14 **TOP** | MTSI | 120.7 | 39.1 | F |
| 15 **TOP** | VLO | 120.5 | 54.6 | T |
| 16 **TOP** | NBIS | 120.4 | 30.6 | F |
| 17 **TOP** | CRWD | 109.5 | 58.0 | T |
| 18 **TOP** | FCEL | 108.7 | 34.9 | F |
| 19 **TOP** | FCX | 102.3 | 33.8 | T |
| 20 **TOP** | MPC | 98.1 | 65.0 | T |
| 21 **TOP** | DDOG | 92.8 | 58.0 | T |
| 22 **TOP** | MRK | 89.4 | 42.7 | T |
| 23  | UMAC | 86.3 | 34.8 | F |
| 24  | PANW | 85.2 | 55.5 | T |
| 25  | PSX | 83.4 | 62.7 | T |
| 26  | TGT | 79.2 | 39.4 | T |
| 27  | NUE | 79.0 | 57.5 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | META | Other | 632.86 | 34.0 | 1.8 | -11.3% | -4.8% | 1.1 | RICH -14% (LOW) | 540.6 | +37% | DISRUPTOR (quant INNOVATING) [research: disruptor] | growth: its multiples disagree with each other; analysts disagree | disruption: revenue +20%/yr over 3 yrs; analysts see revenue +28% next year; research 2026-10-22: AI glasses are a new device category Meta dominates (~76% of 2025 smart-glasses shipments per IDC); the core ad business is growing (+26%), and the open question is the return on its capex. |
| 🟡 dip | NVDA | Semis | 216.26 | 44.4 | 65.4 | -3.8% | -2.7% | 26.3 | FAIR +4% (MED) | 223.06 | +52% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | QQQ | Index-ETF | 712.76 | 42.1 | 63.0 | -2.9% | -1.7% | 24.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MU | Semis | 910.66 | 43.3 | 74.3 | -7.0% | -7.2% | 588.2 | EXPENSIVE -50% (LOW) | 442.61 | +69% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | AMZN | Other | 248.27 | 43.5 | 18.5 | -2.5% | -2.8% | 13.6 | DEEP VALUE +100% (LOW) | 498.14 | +30% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | TEM | AI-health | 66.03 | 45.3 | 45.1 | -7.0% | -4.7% | 8.3 | DEEP VALUE +100% (LOW) | 128.61 | +13% | DISRUPTOR | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +58%/yr over 3 yrs; analysts see revenue +25% next year |
| 🟡 dip | MRVL | Semis | 236.63 | 45.3 | 67.4 | -7.6% | -2.7% | 214.9 | EXPENSIVE -50% (LOW) | 112.1 | +54% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | ASND | Other | 244.82 | 60.7 | 99.0 | +6.2% | +0.9% | 17.5 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +97% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | FCX | Other | 65.19 | 33.8 | 21.0 | -7.0% | -9.3% | 102.3 | EXPENSIVE -36% (HIGH) | 41.2 | +16% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | MRK | Other | 140.77 | 42.7 | 7.7 | -2.8% | -4.1% | 89.4 | EXPENSIVE -37% (MED) | 90.38 | +16% | STABLE | steady: its multiples disagree with each other | disruption: R&D 19% of revenue |
| 🟡 dip | VRTX | Other | 512.28 | 49.3 | 22.6 | +0.5% | -2.0% | 36.4 | FAIR -6% (HIGH) | 486.44 | +16% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟡 dip | USB | Other | 59.82 | 55.8 | 69.7 | +3.3% | -0.6% | 20.0 | FAIR +2% (HIGH) | 61.64 | +13% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | RTX | Other | 196.95 | 58.4 | 76.5 | +4.8% | +0.2% | 15.9 | FAIR -8% (HIGH) | 179.21 | +20% | STABLE | steady |
| 🟡 dip | SLB | Energy | 52.81 | 59.0 | 75.2 | +6.5% | +0.7% | 45.1 | FAIR +0% (HIGH) | 52.08 | +22% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟡 dip | DELL | Other | 471.55 | 41.8 | 69.1 | -9.4% | -8.0% | 330.5 | EXPENSIVE -50% (LOW) | 226.07 | +26% | STABLE | growth: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| 🟡 dip | LITE | Photonics | 830.05 | 42.9 | 74.9 | -12.6% | -10.1% | 485.8 | EXPENSIVE -50% (LOW) | 390.65 | +46% | INNOVATING | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +110% next year |
| 🟡 dip | AMD | Semis | 532.05 | 43.1 | 64.7 | -8.8% | -1.9% | 295.5 | EXPENSIVE -33% (LOW) | 345.74 | +24% | DISRUPTOR | cyclical: PEAK-CYCLE margins (26% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| 🟡 dip | SPY | Index-ETF | 765.04 | 47.0 | 56.8 | -0.7% | -0.3% | 16.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | no | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +110% next year |
| DELL | no | EXPENSIVE -50% (LOW) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | no | EXPENSIVE -49% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +63% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -33% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| INTC | no | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| ILMN | no | FAIR +10% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| RBRK | 42.5 | 68.9 | SPEC |
| MPC | 100.8 | 65.0 |  |
| VLO | 123.6 | 54.6 |  |
| DVN | 40.7 | 62.4 |  |
| HPQ | 12.5 | 62.8 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -57.3 | 25.5 | SPEC |
| SMR | -77.6 | 25.0 | SPEC |
| OKLO | -69.5 | 26.5 | SPEC |
| QBTS | -43.9 | 28.1 | SPEC |
| APLD | -21.4 | 33.3 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._