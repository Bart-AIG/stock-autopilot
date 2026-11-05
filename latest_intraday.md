# Strategy report - INTRADAY  (2026-11-05 17:06 UTC)

## >>> ACTION <<<

## Portfolio review — every position (take-profit / trail / hold)
_No holdings ledger yet. The trading session writes `holdings.json` on each fill (buy → add, sell → remove); once populated, every position is judged here._

## Leader pullback setups — quality grade picks WHAT, the pullback picks WHEN
Top 10% of the universe by quality grade (>= 9/12 traits, beating SPY over 3 months), pulling back: RSI2<10 or a touch of the 21-day EMA. Entry/stop/target are ESTIMATES.

| Ticker | Grade | Q | Rank | Trigger | Theme | Spec | Held | Earnings | Price | RSI2 | Entry | Stop | Target | Stop% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TMO | A+ | 12/12 | #7 | 21 EMA pullback | Other |  |  |  | 691.23 | 32.1 | 691.23 | 663.58 | 709.18 | -4.0% |
| XOM | A+ | 12/12 | #10 | 21 EMA pullback | Energy |  |  |  | 169.69 | 11.8 | 169.69 | 161.41 | 182.11 | -4.9% |
| EMR | A+ | 12/12 | #15 | 21 EMA pullback | Other |  |  |  | 163.91 | 26.0 | 163.91 | 156.98 | 170.74 | -4.2% |
| COP | A+ | 11/12 | #19 | 21 EMA pullback | Energy |  |  | ⚠️ 2026-11-05 | 137.52 | 14.5 | 137.52 | 129.72 | 149.23 | -5.7% |

### How to read this (concentration & sizing)
- ⚠️ **Reports earnings inside the hold window:** COP (2026-11-05). A 1-3 week swing straddles the print, and the suggested stop cannot protect an overnight gap — a name can beat and still gap down (TPR beat EPS on 2026-08-13 and fell 16% the same day). Treat these as NO-ENTRY unless the earnings move IS the thesis.
- ✅ **Discipline:** take the highest-ranked, least-correlated names. Per-name cap 30% of account value; target 3-4 concurrent positions, minimum entry ~$600. Equity capital excludes the 20% options bucket and the 5% reserve. The agent places NO stop (HARD RULE 5): exits are the RSI2>=70 take-profit on a green position, the GRADE EXIT (rank leaves the top 25%), and Ryan's native trail once green enough.

**Excluded — RSI2 dips on names that are NOT leaders** (the old screen would have bought these; the grade filters them out): PLTR (C 3/12), PANW (C 4/12), ZS (B 8/12), CRWD (C 8/12), OXY (C 8/12), MPC (B 8/12), NUE (B 9/12), PSX (C 6/12), ADI (C 7/12), SNOW (C 4/12), AMD (C 5/12), TEM (C 6/12)

## Quality ranking — top 25 of 236 (A = buyable, B = holdable)
Value = valuation grade vs the name's own 10-yr multiples; Disruption = is the business being disrupted or doing the disrupting (legends under the joint section). Display only: neither changes the grade.

| # | Ticker | Grade | Q | RS vs SPY 3M | Off 52W hi | Value | Disruption | Traits firing |
|---|---|---|---|---|---|---|---|---|
| 1 | MRNA | A+ | 12/12 | +315.4% | -5.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 2 | ABBV | A+ | 12/12 | +23.8% | -0.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 3 | WBD | A+ | 12/12 | +22.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 4 | MAR | A+ | 12/12 | +22.5% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 5 | LLY | A+ | 12/12 | +21.9% | -1.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 6 | REGN | A+ | 12/12 | +21.2% | -5.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 7 | TMO | A+ | 12/12 | +20.5% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 8 | PFE | A+ | 12/12 | +18.3% | -0.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 9 | AMGN | A+ | 12/12 | +18.3% | -2.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 10 | XOM | A+ | 12/12 | +15.0% | -9.3% | EXPENSIVE -30% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 11 | KO | A+ | 12/12 | +14.6% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 12 | AAPL | A+ | 12/12 | +14.3% | -1.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 13 | VRTX | A+ | 12/12 | +14.1% | -2.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 14 | PM | A+ | 12/12 | +12.8% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 15 | EMR | A+ | 12/12 | +7.7% | -4.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 16 | SPOT | A+ | 11/12 | +30.7% | -4.6% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 17 | V | A+ | 11/12 | +22.4% | -1.8% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 18 | MA | A+ | 11/12 | +21.9% | -1.4% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 19 | COP | A+ | 11/12 | +21.1% | -10.7% | RICH -10% (HIGH) | STABLE | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 20 | CME | A+ | 11/12 | +20.7% | -5.9% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 21 | PG | A+ | 11/12 | +19.0% | 0.0% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 22 | MSFT | A+ | 11/12 | +12.5% | -2.5% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 23 | DE | A+ | 11/12 | +12.3% | -5.4% | EXPENSIVE -44% (HIGH) | STABLE | 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 24 | BLK | B | 11/12 | +7.9% | -3.7% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, RS 3M, RS 6M, U/D VOL, OBV UP, HH/HL |
| 25 | UNP | B | 11/12 | +6.7% | -3.2% | — | — | MA STACK, 21 EMA UP, > 50 SMA, 200 UP, 52W HI, W.EMA, 12-1 MOM, RS 3M, RS 6M, U/D VOL, OBV UP |

## 12-1 momentum ranking (top decile = 22 of 221)
Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.

| # | Ticker | mom12-1% | RSI14 | >200MA |
|---|---|---|---|---|
| 1 **TOP** | SNDK | 1270.4 | 25.4 | F |
| 2 **TOP** | LITE | 605.7 | 27.4 | F |
| 3 **TOP** | MRNA | 580.7 | 61.2 | T |
| 4 **TOP** | MU | 447.5 | 28.8 | F |
| 5 **TOP** | DELL | 293.8 | 27.0 | F |
| 6 **TOP** | SOXL | 293.8 | 27.4 | F |
| 7 **TOP** | AAOI | 285.2 | 27.6 | F |
| 8 **TOP** | VIAV | 276.7 | 31.0 | F |
| 9 **TOP** | MRVL | 222.8 | 23.4 | F |
| 10 **TOP** | AMD | 218.8 | 31.0 | T |
| 11 **TOP** | INTC | 207.5 | 21.6 | F |
| 12 **TOP** | COHR | 194.8 | 28.3 | F |
| 13 **TOP** | MTSI | 166.2 | 31.6 | F |
| 14 **TOP** | VLO | 156.5 | 33.9 | T |
| 15 **TOP** | AMAT | 136.8 | 27.1 | F |
| 16 **TOP** | CRWD | 124.9 | 36.8 | T |
| 17 **TOP** | LRCX | 123.9 | 24.0 | F |
| 18 **TOP** | MPC | 123.4 | 32.9 | T |
| 19 **TOP** | PSX | 103.0 | 36.8 | T |
| 20 **TOP** | NBIS | 100.0 | 29.3 | F |
| 21 **TOP** | PANW | 97.5 | 34.4 | T |
| 22 **TOP** | FCEL | 94.8 | 29.1 | F |
| 23  | ARM | 93.7 | 27.6 | F |
| 24  | NUE | 85.2 | 43.7 | T |
| 25  | FCX | 80.0 | 26.4 | F |
| 26  | DDOG | 76.8 | 26.6 | F |
| 27  | CAT | 74.3 | 20.4 | F |

## Joint long-term port — accumulate signals (oversold within an uptrend)
Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD ideas ONLY (no exit alerts, not part of the ACTION trigger). **Primary signal is TECHNICAL:** a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI + moving averages), ranked most-oversold first. **Signal:** 🟢 oversold (RSI14 ≤ 35 or RSI2 < 10) / 🟡 dip. **Value** = the valuation grade: how far the price sits from what the name's own 10-year multiples imply (positive = undervalued by that much), with the multiples chosen for its industry. Within each signal tier, cheaper names rank first.


**New long-term ideas you don't hold (oversold uptrends):**
| Signal | Ticker | Theme | Price | RSI14 | RSI2 | vs 20d | vs 50d | mom12-1% | Value | Fair | Analysts | Disruption | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢 oversold | OXY | Energy | 57.26 | 35.7 | 3.2 | -7.3% | -4.8% | 28.5 | UNDERVALUED +13% (HIGH) | 66.11 | +22% | STABLE | cyclical: analysts agree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | PLTR | AI-software | 155.25 | 25.5 | 0.1 | -19.4% | -16.7% | 7.0 | EXPENSIVE -50% (LOW) | 79.19 | +48% | DISRUPTOR [research: disruptor] | preprofit: far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +33%/yr over 3 yrs; analysts see revenue +89% next year; research 2026-11-02: AIP is opening a largely new enterprise market for operational AI (US commercial revenue +149% y/y to $764M in Q2 2026; FY26 guide ~$8.15B, +82%); Microsoft Fabric and frontier-model vendors (Anthropic) are named threats but have not dented reported growth. |
| 🟢 oversold | AMD | Semis | 418.63 | 31.0 | 8.2 | -21.9% | -23.6% | 218.8 | EXPENSIVE -28% (LOW) | 307.61 | +52% | DISRUPTOR [research: innovating] | cyclical: PEAK-CYCLE margins (25% vs 18% normal): earnings multiples ignored; its multiples disagree with each other; analysts disagree | disruption: revenue +29%/yr over 5 yrs; analysts see revenue +48% next year; research 2026-10-26: Gains from the AI-compute shift: OpenAI 6 GW MI450 deal (first 1 GW from 2H26) plus Meta as a customer, Helios rack-scale systems, and continued CPU share gains from Intel. Still a distant No. 2 to Nvidia in accelerators. |
| 🟢 oversold | SNOW | AI-software | 275.93 | 31.8 | 5.4 | -14.6% | -16.2% | 38.5 | UNDERVALUED +24% (LOW) | 341.34 | +58% | INNOVATING (quant DISRUPTOR) [research: threatened] | preprofit: analysts agree | disruption: revenue +31%/yr over 3 yrs; analysts see revenue +35% next year; research 2026-10-21: Databricks is pulling ahead in the AI data-platform race (~$6.9B ARR +80% vs Snowflake ~$5.3B +34%, mid-2026, Tunguz), with ~25% of Databricks ARR from AI; Snowflake product revenue still +31% (Q2 FY27) and its AI layer (Cortex, Snowflake Intelligence) is small. Share loss, not yet shrinking. |
| 🟢 oversold | PANW | AI-software | 321.65 | 34.4 | 0.6 | -12.8% | -13.5% | 97.5 | EXPENSIVE -50% (LOW) | 162.02 | +28% | DISRUPTOR (quant INNOVATING) [research: innovating] | growth: business changed (margin 13% vs 4% 10-yr median): its own history is a weak yardstick; far from its own history: the market has re-rated it, find out why; analysts disagree | disruption: revenue +19%/yr over 3 yrs; analysts see revenue +23% next year; research 2026-10-14: Platformization plus AI security products (AI Access, AI Runtime Security, AI-SPM) position it to gain from vendor consolidation; AI-native rivals (CrowdStrike, Zscaler, Wiz) are pushing into the same space, so margin pressure is the risk, not obsolescence. |
| 🟢 oversold | CRWD | AI-software | 221.17 | 36.8 | 3.2 | -10.9% | -9.4% | 124.9 | EXPENSIVE -38% (LOW) | 136.22 | +10% | DISRUPTOR [research: innovating] | preprofit | disruption: revenue +29%/yr over 3 yrs; analysts see revenue +25% next year; research 2026-10-21: Endpoint security leader adding AI-agent security; Microsoft Defender/Security Copilot bundling is the standing competitive threat (CEO: 'Microsoft is always going to be a competitor'), not obsolescence. Evidence on new-market creation is thin. |
| 🟢 oversold | MPC | Energy | 385.86 | 32.9 | 3.2 | -14.5% | -8.5% | 123.4 | EXPENSIVE -36% (MED) | 252.52 | +15% | STABLE | cyclical: PEAK-CYCLE margins (14% vs 8% normal): earnings multiples ignored | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | PSX | Energy | 253.84 | 36.8 | 4.9 | -9.7% | -5.3% | 103.0 | EXPENSIVE -30% (MED) | 184.07 | +11% | STABLE | cyclical: PEAK-CYCLE margins (11% vs 6% normal): earnings multiples ignored | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |
| 🟢 oversold | ADI | Semis | 376.64 | 39.1 | 5.3 | -7.4% | -3.7% | 73.4 | EXPENSIVE -44% (HIGH) | 218.02 | +19% | INNOVATING | cyclical | disruption: revenue +14%/yr over 5 yrs; analysts see revenue +37% next year |
| 🟢 oversold | NUE | Other | 253.84 | 43.7 | 3.5 | -3.3% | -0.6% | 85.2 | EXPENSIVE -31% (MED) | 173.43 | +20% | STABLE | cyclical: analysts disagree | disruption: commodity producer: revenue and margins follow the commodity price, not competitors |

_The technical screen is the SIGNAL (oversold within an uptrend); the valuation grade says whether the price is cheap for that business, and the disruption grade says whether the business itself is under threat. Confirm each with the news/thesis (HARD RULE 7) before buying: a name can sit below its own history because its future really is worse._

_Valuation grade: DEEP VALUE >= +25% below fair | UNDERVALUED +10 to +25% | FAIR within 10% | RICH 10-25% above | EXPENSIVE > 25% above. Fair = the price at the stock's own 10-year median multiples, using the multiples that suit its industry: banks/insurers on book value, REITs on cash flow, cyclicals (energy, materials, miners, semis, autos, homebuilders) on sales and book with earnings multiples dropped at a peak or trough, growth on sales/EBITDA/FCF, everyone else on earnings/EBITDA/FCF. Confidence (HIGH/MED/LOW) drops when the margin cycle is extreme, the business has changed shape, the multiples disagree, or analysts' median target points the other way. Analysts = median 12-month target vs price. Relative to its OWN past only: when the whole market is above its history, most names read RICH._

_Disruption grade: is a changing trend or new technology making this business obsolete (AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market (DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant layer is an early warning. Quant layer: 10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades >= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; banks, insurers and REITs are judged on revenue only. A dated research note (competitors, emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history but AT RISK or BEING DISRUPTED._

## SWING_M picks — grade context (display only, never a filter)
This month's top-10 by 12-month return, traded mechanically by the sleeve. The valuation and disruption grades are shown for context only: the tested rules have no such filter and the standing ban forbids adding one without a live Ryan turn (see grades_filter_results.md for the backtest of using them as a filter).

| Ticker | Held now | Value | Disruption | Why |
|---|---|---|---|---|
| MRNA | no | EXPENSIVE -50% (LOW) | AT RISK | revenue -53%/yr, unwinding a one-time boom (peak 10x today's); gross margin down 16 pts vs 5-yr median (55%) |
| LITE | no | EXPENSIVE -50% (LOW) | DISRUPTOR (quant INNOVATING) [research: disruptor] | revenue +19%/yr over 3 yrs; analysts see revenue +117% next year; research 2026-10-29: Lumentum's lasers and optical circuit switches are building the optical layer of AI data centers; OCS backlog >$400M (Google a key customer) and co-packaged optics moving from evaluation to booked orders into 2027. Demand exceeds supply. |
| MU | no | EXPENSIVE -50% (LOW) | DISRUPTOR [research: innovating] | revenue +37%/yr over 5 yrs; analysts see revenue +109% next year; research 2026-10-12: HBM/server memory for AI lifted Micron to ~23% of DRAM revenue (TrendForce Q2 2026), near SK hynix; the gain is from the AI shift, not a new market it created. |
| DELL | no | EXPENSIVE -48% (MED) | INNOVATING (quant STABLE) [research: innovating] | analysts see revenue +71% next year; gross margin slipping 2 pts (20%); research 2026-10-26: AI server builder: record AI backlog ($43B at FY26 end, reported ~$51B later), demand ahead of supply; PC side flat to down. Gains from the AI build-out but on lower-margin pass-through hardware. |
| WDC | no | EXPENSIVE -45% (LOW) | DISRUPTOR [research: innovating] | revenue +27%/yr over 3 yrs; analysts see revenue +64% next year; research 2026-10-06: AI data-lake build-out made nearline HDDs scarce: sold out for 2026, LTAs into 2027-28, 26TB CMR/32TB UltraSMR ramp, HAMR in hyperscale qualification for 2027; flash substitution is a long-run risk but SSDs cost ~16x per TB. |
| ILMN | no | DEEP VALUE +52% (MED) | BEING DISRUPTED | revenue shrinking -2%/yr over 3 yrs; R&D 22% of revenue |
| VLO | no | EXPENSIVE -46% (LOW) | AT RISK (quant STABLE) [research: threatened] | commodity producer: revenue and margins follow the commodity price, not competitors; research 2026-10-28: Refining margins very strong in 2026 (Q2 refining op income $4.5B vs $1.3B; $23.62/bbl), and Diamond Green Diesel renewable diesel/SAF swung to $717M profit. Long-run EV adoption erodes gasoline demand; not visible in current numbers. Oil sector is de-emphasized for new entries per Ryan's steer. |
| MPC | no | EXPENSIVE -36% (MED) | STABLE | commodity producer: revenue and margins follow the commodity price, not competitors |
| MRVL | no | EXPENSIVE -45% (LOW) | DISRUPTOR [research: innovating] | revenue +23%/yr over 5 yrs; analysts see revenue +47% next year; research 2026-10-19: Rides the AI data-center shift through optical interconnect (1.6T optics in volume production, guided +50% for FY2027) and 18 custom-chip programs; risk is losing custom-chip sockets (most Amazon Trainium 3 went to Alchip). Gains from the shift; not creating a new market. |
| VIAV | no | EXPENSIVE -35% (MED) | INNOVATING | revenue +11%/yr over 3 yrs; analysts see revenue +24% next year |

## Options candidates (sleeve: options — single-leg LONG)
Underlyings only, drawn from the quality grade: CALLS on top-graded leaders, PUTS on bottom-graded laggards. **Options bucket = 20% of account value, no per-trade cap; paused if the bucket loses 40%** (see CLAUDE.md HARD RULE 8). Pick the contract off the live chain (21-45 DTE, ~0.35 delta) and grade it with options_grade.grade_contract() on current quotes; only a combined A/A+ may enter.

**Calls (bullish — strong uptrend > 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| MRNA | 727.3 | 61.2 |  |
| ABBV | 25.7 | 65.0 |  |
| MAR | 31.0 | 71.8 |  |
| LLY | 31.1 | 70.6 |  |
| REGN | 18.2 | 66.6 |  |

**Puts (bearish — downtrend < 200MA):**
| Ticker | mom12-1% | RSI14 | Spec |
|---|---|---|---|
| ASTS | -13.4 | 25.4 | SPEC |
| IREN | -41.9 | 27.2 | SPEC |
| LEU | -55.0 | 27.6 | SPEC |
| CRWV | -23.6 | 28.3 | SPEC |
| APLD | -23.3 | 30.9 | SPEC |

---
_Read-only. No positions checked, no trades placed. Bring this into a session to act with live quotes and per-order approval._