# Strategy report - INTRADAY  (2026-10-23 19:07 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MPC | A+ | 12/12 | #1 | RSI2 dip | Energy |  |  |  | 457.21 | 4.0 | 457.21 | 432.11 | 484.92 | -5.5% |
| VLO | A+ | 12/12 | #2 | RSI2 dip | Energy |  |  |  | 420.4 | 7.6 | 420.4 | 395.35 | 457.98 | -6.0% |
| TMO | A+ | 12/12 | #6 | 21 EMA pullback | Other |  |  |  | 671.59 | 17.7 | 671.59 | 641.73 | 696.49 | -4.4% |
| MRNA | A+ | 11/12 | #17 | 21 EMA pullback | Other |  |  | ⚠️ 2026-11-06 | 199.31 | 12.6 | 199.31 | 166.26 | 245.81 | -16.6% ⚠ |
| PLTR | A+ | 11/12 | #18 | 21 EMA pullback | AI-software |  |  |  | 195.43 | 39.8 | 195.43 | 181.83 | 209.05 | -7.0% |
| MSFT | A+ | 11/12 | #20 | 21 EMA pullback | Other |  |  |  | 524.1 | 36.1 | 524.1 | 508.28 | 543.45 | -3.0% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** MRNA (2026-11-06). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ⚠️ **1 have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the dollar-risk-to-stop is small, not the dollar position.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): META (C 6/12), AMZN (C 4/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MPC | A+ | 12/12 | +43.5% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | VLO | A+ | 12/12 | +34.9% | -8.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | COP | A+ | 12/12 | +27.9% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | CVX | A+ | 12/12 | +19.8% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | PFE | A+ | 12/12 | +19.0% | -1.1% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | TMO | A+ | 12/12 | +17.1% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | DVN | A+ | 12/12 | +16.0% | -1.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | WBD | A+ | 12/12 | +15.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | XOM | A+ | 12/12 | +15.2% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | AMGN | A+ | 12/12 | +14.1% | -1.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | OXY | A+ | 12/12 | +14.1% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | EOG | A+ | 12/12 | +13.7% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | ABBV | A+ | 12/12 | +8.1% | -1.3% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | KO | A+ | 12/12 | +7.6% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | LLY | A+ | 12/12 | +2.9% | -3.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | AAPL | A+ | 12/12 | +0.0% | -0.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | MRNA | A+ | 11/12 | +255.1% | -19.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | PLTR | A+ | 11/12 | +45.7% | -6.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | CRWD | A+ | 11/12 | +38.6% | -8.6% | — | — | MA STACK, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | MSFT | A+ | 11/12 | +31.8% | -3.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | V | A+ | 11/12 | +10.0% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | MA | A+ | 11/12 | +9.9% | -1.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | VRTX | A+ | 11/12 | +6.8% | -5.8% | FAIR -8% (HIGH) | DISRUPTOR (quant INNOVATING) [research: innovating] | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | PM | B | 11/12 | -0.7% | -2.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | RBRK | B | 10/12 | +69.5% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, HH/HL |

## 12-1 momentum ranking (top decile = 22 of 223)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | MRNA | 606.1 | 49.9 | T |
| 2 **TOP** | MU | 544.1 | 38.4 | T |
| 3 **TOP** | LITE | 471.4 | 35.6 | F |
| 4 **TOP** | INTC | 317.9 | 32.5 | T |
| 5 **TOP** | DELL | 309.3 | 38.4 | T |
| 6 **TOP** | AMD | 282.0 | 39.1 | T |
| 7 **TOP** | AAOI | 260.2 | 30.8 | F |
| 8 **TOP** | MRVL | 249.6 | 41.4 | T |
| 9 **TOP** | VIAV | 193.6 | 34.1 | F |
| 10 **TOP** | COHR | 175.0 | 30.4 | F |
| 11 **TOP** | AMAT | 136.2 | 27.0 | F |
| 12 **TOP** | ARM | 135.9 | 31.9 | F |
| 13 **TOP** | LRCX | 132.9 | 24.6 | F |
| 14 **TOP** | VLO | 120.6 | 51.6 | T |
| 15 **TOP** | CRWD | 116.9 | 54.8 | T |
| 16 **TOP** | MTSI | 114.2 | 36.2 | F |
| 17 **TOP** | NBIS | 110.2 | 31.2 | F |
| 18 **TOP** | MPC | 103.5 | 59.8 | T |
| 19 **TOP** | PSX | 93.9 | 58.0 | T |
| 20 **TOP** | PANW | 93.5 | 52.0 | T |
| 21 **TOP** | FCEL | 89.2 | 32.9 | F |
| 22 **TOP** | SCCO | 85.4 | 35.3 | F |
| 23  | MRK | 85.2 | 49.1 | T |
| 24  | DDOG | 82.9 | 54.1 | T |
| 25  | NUE | 82.6 | 57.9 | T |
| 26  | TGT | 79.5 | 45.1 | T |
| 27  | KLAC | 75.4 | 23.3 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.

**Held in the joint port — ADD / average-in candidates (oversold within their uptrend):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | AMZN | Other | 248.31 | 43.4 | 9.1 | -2.4% | -2.9% | 12.9 | DEEP VALUE +100% (LOW) | 497.54 | +31% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady: business changed (margin 33% vs 13% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts agree | disruption: revenue +12%/yr over 3 yrs; gross margin up 6 pts (50%); research 2026-10-12: AWS grew 28% last quarter and Trainium is reported at a ~$20B annual pace with large Anthropic/OpenAI commitments; Amazon gains from the AI-compute shift rather than being displaced by it. |
| 🟡 dip | NVDA | Semis | 211.65 | 38.6 | 21.4 | -6.2% | -4.9% | 26.4 | FAIR +5% (MED) | 223.07 | +53% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (77% vs 36% normal): earnings multiples ignored | disruption: revenue +67%/yr over 5 yrs; analysts see revenue +90% next year; research 2026-10-19: Still the dominant AI accelerator supplier; hyperscaler custom ASICs (Broadcom, Marvell, Google TPU) are the named threat and growing fastest, but estimates put ASICs at only ~13% of accelerator sales by 2027. Gains from the AI shift; share-erosion risk, not obsolescence. |
| 🟡 dip | QQQ | Index-ETF | 704.98 | 36.9 | 19.9 | -4.1% | -2.9% | 23.9 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | MU | Semis | 878.9 | 38.4 | 44.6 | -10.9% | -10.6% | 544.1 | EXPENSIVE -50% (LOW) | 441.16 | +70% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (82% vs 49% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| 🟡 dip | MRVL | Semis | 229.2 | 41.4 | 40.0 | -10.8% | -5.7% | 249.6 | EXPENSIVE -50% (LOW) | 113.5 | +52% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (50% vs 18% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| 🟡 dip | ASND | Other | 242.3 | 58.3 | 84.2 | +5.5% | -0.1% | 15.0 | N/A | — | — | DISRUPTOR [research: innovating] | steady: not enough history for this industry's multiples | disruption: revenue +138%/yr over 3 yrs; analysts see revenue +98% next year; research 2026-10-05: Yorvipath (hypoparathyroidism) revenue ~EUR252M in Q2 2026, 6,300+ US patient enrollments, launches in 35+ countries; TransCon pipeline extends it. Single-product concentration is the risk. |

**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | INTC | Semis | 86.74 | 32.5 | 29.7 | -16.7% | -15.0% | 317.9 | EXPENSIVE -50% (LOW) | 43.1 | +28% | BEING DISRUPTED | cyclical: TROUGH-CYCLE margins (6% vs 41% normal): earnings multiples ignored; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| 🟡 dip | QCOM | Semis | 176.21 | 48.3 | 61.1 | -1.1% | +0.1% | 16.3 | FAIR -2% (HIGH) | 171.17 | +12% | DISRUPTOR (quant INNOVATING) [research: innovating] | cyclical | disruption: revenue +13%/yr over 5 yrs; analysts expect revenue -3% next year; research 2026-10-12: Losing Apple's modem business (~$5.7B+/yr at risk by 2027) but replacing it with data-center AI chips (Amazon deal of up to $60B, target $15B DC revenue by FY2029) and record automotive; the core handset business is being substituted, not made obsolete. |
| 🟡 dip | USB | Other | 59.62 | 54.8 | 59.7 | +3.1% | -1.1% | 18.5 | FAIR +4% (HIGH) | 61.64 | +15% | STABLE [research: neutral] | bank | disruption: research 2026-10-21: Large regional bank; fintech competition in payments is a noted risk, and it is responding with a USBDC stablecoin pilot on Stellar (first live cross-border transfer Sept 2026) and stablecoin-reserve custody for Anchorage. No visible obsolescence; not creating a new market. |
| 🟡 dip | VRTX | Other | 525.6 | 55.9 | 49.6 | +2.9% | +0.5% | 36.0 | FAIR -8% (HIGH) | 486.44 | +14% | DISRUPTOR (quant INNOVATING) [research: innovating] | steady | disruption: revenue +11%/yr over 3 yrs; gross margin slipping 3 pts (85%); research 2026-10-13: Cystic fibrosis franchise plus newer markets (non-opioid pain, gene editing); a 2025 phase-2 pain-drug failure cut the pain upside, so it gains from new therapies but has not yet proven a large new market. |
| 🟡 dip | SPY | Index-ETF | 760.62 | 42.6 | 15.9 | -1.2% | -0.9% | 15.8 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | SNOW | AI-software | 322.68 | 46.3 | 65.9 | -3.5% | -2.7% | 49.8 | FAIR +8% (LOW) | 341.13 | +38% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟡 dip | DIA | Index-ETF | 522.0 | 53.1 | 22.1 | +1.1% | -0.2% | 11.1 | N/A | — | — | N/A | steady: not enough history for this industry's multiples | disruption: fewer than 4 years of revenue history |
| 🟡 dip | ROST | Other | 228.7 | 45.6 | 15.0 | -1.0% | -1.3% | 60.6 | RICH -11% (MED) | 204.92 | +22% | STABLE [research: neutral] | steady: analysts disagree | disruption: analysts see revenue +13% next year; research 2026-10-12: Off-price store chain gaining share from value-seeking shoppers (Deutsche Bank sees +210 bp off-price share in 2026); no sign online retail is eroding the treasure-hunt model, and no new market either. |
| 🟡 dip | FCX | Other | 65.54 | 35.2 | 29.8 | -6.9% | -8.8% | 60.0 | EXPENSIVE -36% (HIGH) | 41.2 | +16% | STABLE | cyclical | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟡 dip | CSCO | Other | 106.12 | 40.8 | 50.0 | -4.2% | -3.7% | 57.6 | EXPENSIVE -43% (MED) | 60.4 | +28% | INNOVATING | growth: analysts disagree | disruption: analysts see revenue +15% next year; R&D 15% of revenue |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| MU | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| LITE | yes | EXPENSIVE -50% (LOW) | INNOVATING | revenue +19%/yr over 3 yrs; analysts see revenue +110% next year |
| DELL | yes | EXPENSIVE -50% (LOW) | STABLE | analysts see revenue +71% next year; gross margin slipping 2 pts (20%) |
| WDC | no | EXPENSIVE -46% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +54% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| AMD | yes | EXPENSIVE -33% (LOW) | DISRUPTOR | revenue +29%/yr over 5 yrs; analysts see revenue +48% next year |
| INTC | no | EXPENSIVE -50% (LOW) | BEING DISRUPTED | revenue shrinking -7%/yr over 5 yrs; analysts see revenue +20% next year |
| VIAV | no | EXPENSIVE -48% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |
| MRVL | yes | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| ILMN | no | UNDERVALUED +10% (MED) | AT RISK | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MPC | 107.4 | 59.8 |  |
| VLO | 136.5 | 51.6 |  |
| PFE | 14.9 | 66.4 |  |
| TMO | 19.6 | 52.9 |  |
| DVN | 50.9 | 61.2 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| LEU | -53.2 | 27.5 | SPEC |
| QBTS | -35.9 | 28.5 | SPEC |
| SMR | -75.6 | 27.0 | SPEC |
| OKLO | -68.1 | 27.8 | SPEC |
| ASTS | -14.4 | 31.2 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._