# Strategy report - MORNING  (2026-10-27 14:09 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPC | A+ | 12/12 | #3 | 21 EMA pullback | Energy |  |  |  | 452.51 | 25.1 | 452.51 | 424.88 | 484.92 | -6.1% |
| MRNA | A+ | 11/12 | #17 | RSI2 dip | Other |  |  | ⚠️ 2026-11-06 | 185.32 | 4.3 | 185.32 | 153.98 | 232.33 | -16.9% ⚠ |
| SHOP | A+ | 11/12 | #20 | RSI2 dip | Other |  |  |  | 165.29 | 4.3 | 165.29 | 154.58 | 179.22 | -6.5% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MRNA (2026-11-06). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): ABNB (B 8/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | RBRK | A+ | 12/12 | +85.7% | 0.0% | EXPENSIVE -37% (LOW) | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | CRWD | A+ | 12/12 | +44.2% | -4.0% | EXPENSIVE -48% (LOW) | DISRUPTOR [research: innovating] | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | MPC | A+ | 12/12 | +41.5% | -6.7% | EXPENSIVE -50% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | COP | A+ | 12/12 | +22.5% | -0.5% | RICH -23% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | CVX | A+ | 12/12 | +15.4% | -0.9% | EXPENSIVE -29% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +14.5% | -1.1% | RICH -18% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | ADI | A+ | 12/12 | +13.4% | -6.1% | EXPENSIVE -46% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +13.4% | 0.0% | EXPENSIVE -50% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | PFE | A+ | 12/12 | +13.2% | -2.3% | EXPENSIVE -30% (MED) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | HPQ | A+ | 12/12 | +12.1% | -6.2% | FAIR -1% (HIGH) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | XOM | A+ | 12/12 | +12.0% | -0.6% | EXPENSIVE -40% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AMGN | A+ | 12/12 | +9.7% | -0.6% | EXPENSIVE -27% (HIGH) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | OXY | A+ | 12/12 | +8.6% | -3.8% | FAIR +4% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | EOG | A+ | 12/12 | +6.2% | -0.8% | FAIR -8% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | ABBV | A+ | 12/12 | +3.8% | -0.9% | EXPENSIVE -46% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | LLY | A+ | 12/12 | +1.9% | -1.0% | FAIR -7% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MRNA | A+ | 11/12 | +235.1% | -24.6% | EXPENSIVE -50% (LOW) | AT RISK | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PLTR | A+ | 11/12 | +56.2% | -5.1% | EXPENSIVE -50% (LOW) | DISRUPTOR | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | MSFT | A+ | 11/12 | +30.5% | -2.6% | RICH -15% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | SHOP | A+ | 11/12 | +22.9% | -7.8% | FAIR -5% (MED) | INNOVATING | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | DVN | A+ | 11/12 | +10.1% | -1.7% | RICH -19% (LOW) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, U/D VOL, OBV UP, HH/HL |
| 22 | TXN | A+ | 11/12 | +6.6% | -8.8% | EXPENSIVE -33% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 23 | EMR | A+ | 11/12 | +6.5% | -1.1% | EXPENSIVE -31% (MED) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |
| 24 | V | B | 11/12 | +3.8% | -3.2% | FAIR -10% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | MA | B | 11/12 | +2.8% | -4.1% | FAIR +7% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 712.1 | 45.2 | T |
| 2 **TOP** | MU | 588.2 | 44.7 | T |
| 3 **TOP** | LITE | 485.8 | 43.7 | T |
| 4 **TOP** | DELL | 330.5 | 46.2 | T |
| 5 **TOP** | AMD | 295.5 | 47.3 | T |
| 6 **TOP** | AAOI | 293.5 | 36.3 | F |
| 7 **TOP** | INTC | 246.5 | 41.7 | T |
| 8 **TOP** | VIAV | 233.2 | 38.5 | F |
| 9 **TOP** | MRVL | 214.9 | 46.5 | T |
| 10 **TOP** | ILMN | 194.5 | 58.2 | T |
| 11 **TOP** | COHR | 176.5 | 37.7 | F |
| 12 **TOP** | LRCX | 145.6 | 29.7 | F |
| 13 **TOP** | AMAT | 137.8 | 31.0 | F |
| 14 **TOP** | ARM | 122.3 | 38.2 | F |
| 15 **TOP** | MTSI | 120.7 | 42.5 | F |
| 16 **TOP** | VLO | 120.5 | 44.8 | T |
| 17 **TOP** | NBIS | 120.4 | 37.1 | F |
| 18 **TOP** | CRWD | 109.5 | 60.2 | T |
| 19 **TOP** | FCEL | 108.7 | 35.9 | F |
| 20 **TOP** | FCX | 102.3 | 32.6 | F |
| 21 **TOP** | MPC | 98.1 | 54.5 | T |
| 22 **TOP** | DDOG | 92.8 | 55.6 | T |
| 23  | MRK | 89.4 | 43.1 | T |
| 24  | UMAC | 86.3 | 37.6 | F |
| 25  | PANW | 85.2 | 56.6 | T |
| 26  | PSX | 83.4 | 51.9 | T |
| 27  | TGT | 79.2 | 39.2 | T |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟡 dip | NVDA | Semis | 216.05 | 44.2 | 64.8 | -3.7% | -2.7% | 26.3 | FAIR +3% (MED) | 223.06 | +50% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | QQQ | Index-ETF | 715.45 | 43.8 | 73.4 | -2.4% | -1.3% | 24.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MU | Semis | 919 | 44.7 | 81.5 | -5.4% | -6.2% | 588.2 | EXPENSIVE -50% (LOW) | 458.9 | +63% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | AMZN | Other | 249.44 | 44.8 | 33.9 | -2.1% | -2.2% | 13.6 | DEEP VALUE +100% (LOW) | 498.92 | +30% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | MRVL | Semis | 238.93 | 46.5 | 77.1 | -6.2% | -1.8% | 214.9 | EXPENSIVE -50% (LOW) | 119.3 | +45% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | TEM | AI-health | 67.32 | 46.9 | 61.9 | -4.3% | -3.3% | 8.3 | DEEP VALUE +96% (LOW) | 132.63 | +7% | DISRUPTOR [research: innovating] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +58%/yr over 3 yrs; analysts see revenue +25% next year; research 2026-10-26: AI precision-oncology platform; testing builds a proprietary multimodal data moat that grows more valuable as AI and biomarker-driven therapy spread; ~25% revenue growth guided for 2026. Not yet profitable; rivals (Guardant, Foundation Medicine, Caris) not quantified. |
| 🟡 dip | ASND | Other | 244.21 | 59.7 | 67.5 | +5.6% | +0.7% | 17.5 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +97% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | ABNB | Other | 167.59 | 48.2 | 6.7 | -0.1% | -2.3% | 27.3 | FAIR -1% (LOW) | 165.45 | +12% | AT RISK | steady: business changed (margin 23% vs 5% 10-yr median): its own history is a weak yardstick | disruption: revenue +14%/yr over 3 yrs; gross margin down 10 pts vs 5-yr median (72%) |
| 🟡 dip | VRTX | Other | 512.35 | 49.2 | 17.8 | +0.6% | -2.0% | 36.4 | FAIR -5% (HIGH) | 486.52 | +17% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟡 dip | USB | Other | 59.34 | 52.8 | 32.5 | +2.4% | -1.2% | 20.0 | FAIR +4% (HIGH) | 61.64 | +14% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | RTX | Other | 197.43 | 58.9 | 77.0 | +4.8% | +0.7% | 15.9 | FAIR -9% (HIGH) | 179.21 | +19% | STABLE | steady |
| 🟡 dip | LITE | Photonics | 836.1 | 43.7 | 79.5 | -11.2% | -9.2% | 485.8 | EXPENSIVE -50% (LOW) | 418.95 | +36% | INNOVATING | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +110% next year |
| 🟡 dip | VLO | Energy | 405.55 | 44.8 | 14.0 | -5.3% | +2.6% | 120.5 | EXPENSIVE -50% (LOW) | 203.26 | +9% | STABLE | cyclical: PEAK-CYCLE margins (14% vs 6% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟡 dip | AMD | Semis | 548.82 | 47.3 | 82.3 | -5.5% | +1.0% | 295.5 | EXPENSIVE -34% (LOW) | 360.84 | +18% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (26% vs 18% normal): earnings multiples ignored; its multiples disagree with each other | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| 🟡 dip | SPY | Index-ETF | 766.24 | 48.1 | 64.1 | -0.5% | -0.2% | 16.5 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | DIA | Index-ETF | 522.22 | 53.1 | 33.8 | +0.9% | -0.0% | 11.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | ROST | Other | 229.75 | 47.2 | 30.2 | -0.4% | -0.7% | 55.8 | RICH -11% (MED) | 204.92 | +23% | STABLE [research: neutral] | steady: analysts disagree | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |

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

## Theme watchlists — your picks, graded (display only)
Names on your Robinhood theme lists. Quality is grade.py's letter (A/A+ buyable, B holdable, C neither); value and disruption as above. Context, not signals.

| List | Ticker | Quality | Value | Disruption |
|---|---|---|---|---|
| Drones | EH | C 0/12 #229 | DEEP VALUE +100% (LOW) | INNOVATING |
| Drones | ZENA | C 0/12 #230 | N/A | INNOVATING |
| Drones | UMAC | C 2/12 #134 | N/A | N/A |
| Drones | UAVS | C 0/12 #209 | N/A | AT RISK |
| Drones | ONDS | C 0/12 #188 | DEEP VALUE +69% (LOW) | DISRUPTOR |
| Drones | DPRO | C 2/12 #144 | FAIR +4% (LOW) | AT RISK |
| Drones | KTOS | C 0/12 #193 | RICH -23% (LOW) | INNOVATING |
| Drones | AVAV | C 0/12 #198 | DEEP VALUE +42% (LOW) | AT RISK |
| Drones | RCAT | C 0/12 #234 | DEEP VALUE +100% (LOW) | AT RISK |
| Raw materials | RIO | C 1/12 #171 | FAIR -3% (HIGH) | STABLE |
| Raw materials | SCCO | C 4/12 #103 | EXPENSIVE -40% (HIGH) | INNOVATING (quant STABLE) [research: innovating] |
| Raw materials | BHP | C 1/12 #157 | RICH -23% (HIGH) | STABLE |
| Raw materials | CENX | C 1/12 #181 | EXPENSIVE -35% (LOW) | STABLE |
| Raw materials | FCX | C 3/12 #113 | EXPENSIVE -40% (MED) | STABLE |
| Growth opportunities | NBIS | C 3/12 #112 | EXPENSIVE -50% (LOW) | DISRUPTOR [research: disruptor] |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| RBRK | 46.9 | 70.8 | SPEC |
| CRWD | 96.7 | 60.2 |  |
| MPC | 98.5 | 54.5 |  |
| COP | 43.2 | 74.8 |  |
| CVX | 32.7 | 72.0 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -63.3 | 32.3 | SPEC |
| SMR | -79.0 | 29.8 | SPEC |
| OKLO | -72.7 | 30.2 | SPEC |
| QBTS | -48.6 | 30.0 | SPEC |
| UUUU | -48.4 | 25.9 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._