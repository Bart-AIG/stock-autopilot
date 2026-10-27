# Strategy report - INTRADAY  (2026-10-27 18:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPC | A+ | 12/12 | #3 | 21 EMA pullback | Energy |  |  |  | 439.75 | 17.1 | 439.75 | 409.52 | 484.92 | -6.9% |
| MRNA | A+ | 11/12 | #18 | 21 EMA pullback | Other |  |  | ⚠️ 2026-11-06 | 198.98 | 13.4 | 198.98 | 166.18 | 245.81 | -16.5% ⚠ |
| SHOP | A+ | 11/12 | #21 | RSI2 dip | Other |  |  |  | 165.99 | 5.2 | 165.99 | 155.31 | 179.22 | -6.4% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MRNA (2026-11-06). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): VLO (B 9/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | RBRK | A+ | 12/12 | +84.3% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | CRWD | A+ | 12/12 | +44.1% | -3.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | MPC | A+ | 12/12 | +36.8% | -9.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | PANW | A+ | 12/12 | +22.8% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | COP | A+ | 12/12 | +19.9% | -2.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +15.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | CVX | A+ | 12/12 | +13.8% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | ADI | A+ | 12/12 | +13.5% | -5.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | HPQ | A+ | 12/12 | +13.4% | -4.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | WBD | A+ | 12/12 | +13.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | PFE | A+ | 12/12 | +12.4% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | XOM | A+ | 12/12 | +10.0% | -1.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | AMGN | A+ | 12/12 | +9.8% | -0.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EMR | A+ | 12/12 | +8.1% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EOG | A+ | 12/12 | +5.4% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | ABBV | A+ | 12/12 | +3.4% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | LLY | A+ | 12/12 | +0.2% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MRNA | A+ | 11/12 | +260.4% | -18.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | PLTR | A+ | 11/12 | +56.6% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +30.6% | -2.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | SHOP | A+ | 11/12 | +22.8% | -7.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | DVN | A+ | 11/12 | +9.1% | -2.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 23 | TXN | A+ | 11/12 | +7.7% | -7.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | OXY | B | 11/12 | +6.8% | -5.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 25 | V | B | 11/12 | +2.9% | -3.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 225)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 712.1 | 50.0 | T |
| 2 **TOP** | MU | 588.2 | 46.3 | T |
| 3 **TOP** | LITE | 485.8 | 46.5 | T |
| 4 **TOP** | DELL | 330.5 | 49.2 | T |
| 5 **TOP** | AMD | 295.5 | 49.5 | T |
| 6 **TOP** | AAOI | 293.5 | 39.1 | F |
| 7 **TOP** | INTC | 246.5 | 42.4 | T |
| 8 **TOP** | VIAV | 233.2 | 41.4 | F |
| 9 **TOP** | MRVL | 214.9 | 48.2 | T |
| 10 **TOP** | ILMN | 194.5 | 60.4 | T |
| 11 **TOP** | COHR | 176.5 | 40.4 | F |
| 12 **TOP** | LRCX | 145.6 | 30.6 | F |
| 13 **TOP** | AMAT | 137.8 | 33.8 | F |
| 14 **TOP** | ARM | 122.3 | 39.5 | F |
| 15 **TOP** | MTSI | 120.7 | 43.4 | F |
| 16 **TOP** | VLO | 120.5 | 40.2 | T |
| 17 **TOP** | NBIS | 120.4 | 38.5 | F |
| 18 **TOP** | CRWD | 109.5 | 60.5 | T |
| 19 **TOP** | FCEL | 108.7 | 38.6 | F |
| 20 **TOP** | FCX | 102.3 | 38.5 | T |
| 21 **TOP** | MPC | 98.1 | 48.8 | T |
| 22 **TOP** | DDOG | 92.8 | 56.7 | T |
| 23  | MRK | 89.4 | 45.1 | T |
| 24  | UMAC | 86.3 | 39.6 | F |
| 25  | PANW | 85.2 | 58.7 | T |
| 26  | PSX | 83.4 | 46.3 | T |
| 27  | TGT | 79.2 | 40.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | NVDA | Semis | 218 | 46.4 | 75.3 | -2.9% | -1.9% | 26.3 | FAIR +3% (MED) | 223.06 | +50% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | MU | Semis | 930.82 | 46.3 | 85.7 | -4.3% | -5.0% | 588.2 | EXPENSIVE -50% (LOW) | 458.9 | +63% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | QQQ | Index-ETF | 720.64 | 46.8 | 82.2 | -1.7% | -0.6% | 24.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MRVL | Semis | 242.56 | 48.2 | 82.3 | -4.8% | -0.3% | 214.9 | EXPENSIVE -50% (LOW) | 119.3 | +45% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | AMZN | Other | 253.95 | 49.4 | 72.2 | -0.4% | -0.5% | 13.6 | DEEP VALUE +100% (LOW) | 498.92 | +30% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | ASND | Other | 243.71 | 59.1 | 57.9 | +5.4% | +0.5% | 17.5 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +97% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | VLO | Energy | 392.16 | 40.2 | 9.5 | -8.3% | -0.7% | 120.5 | EXPENSIVE -50% (LOW) | 203.26 | +9% | STABLE | cyclical: PEAK-CYCLE margins (14% vs 6% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | CVS | Other | 91.35 | 50.7 | 9.1 | +1.7% | -0.1% | 17.6 | EXPENSIVE -29% (LOW) | 65.6 | +22% | STABLE | steady: business changed (margin 3% vs 6% 10-yr median): its own history is a weak yardstick; analysts disagree | disruption: gross margin slipping 3 pts (14%) |
| 🟢 oversold | ABNB | Other | 168.48 | 49.4 | 8.0 | +0.4% | -1.8% | 27.3 | FAIR -1% (LOW) | 165.45 | +12% | AT RISK | steady: business changed (margin 23% vs 5% 10-yr median): its own history is a weak yardstick | disruption: revenue +14%/yr over 3 yrs; gross margin down 10 pts vs 5-yr median (72%) |
| 🟡 dip | VRTX | Other | 516.45 | 51.2 | 25.5 | +1.3% | -1.2% | 36.4 | FAIR -5% (HIGH) | 486.52 | +17% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟡 dip | USB | Other | 59.74 | 55.5 | 68.6 | +3.1% | -0.5% | 20.0 | FAIR +4% (HIGH) | 61.64 | +14% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | RTX | Other | 195.74 | 56.0 | 57.0 | +3.9% | -0.2% | 15.9 | FAIR -9% (HIGH) | 179.21 | +19% | STABLE | steady |
| 🟡 dip | LITE | Photonics | 864.2 | 46.5 | 85.7 | -8.4% | -6.2% | 485.8 | EXPENSIVE -50% (LOW) | 418.95 | +36% | INNOVATING | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +110% next year |
| 🟡 dip | IWM | Index-ETF | 279.68 | 50.9 | 92.7 | +0.9% | -2.0% | 16.8 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | SPY | Index-ETF | 769.6 | 51.1 | 76.7 | -0.1% | +0.3% | 16.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | DIA | Index-ETF | 523.04 | 54.3 | 44.0 | +1.1% | +0.1% | 11.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |

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
| DELL | no | EXPENSIVE -50% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +63% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | no | EXPENSIVE -34% (LOW) | DISRUPTOR [research: innovating] | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| INTC | no | EXPENSIVE -50% (LOW) | BEING DISRUPTED [research: threatened] | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year; research 2026-10-26: AMD has taken PC and server CPU share (server ~30%) and Arm designs keep gaining; offset is 18A foundry (yields ~85% per KeyBanc, outside customers reported, break-even pulled forward). Core x86 franchise still losing ground. |
| VIAV | no | EXPENSIVE -50% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| ILMN | yes | FAIR +7% (HIGH) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| RBRK | 46.9 | 70.4 | SPEC |
| CRWD | 96.7 | 60.5 |  |
| MPC | 98.5 | 48.8 |  |
| PANW | 80.6 | 58.7 |  |
| COP | 43.2 | 67.7 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -63.3 | 35.3 | SPEC |
| OKLO | -72.7 | 31.8 | SPEC |
| SMR | -79.0 | 32.6 | SPEC |
| QBTS | -48.6 | 33.3 | SPEC |
| BKNG | -20.4 | 33.1 |  |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._