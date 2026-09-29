# Process audit — 2026-09-29 (backtest-based)

**Goal (Ryan):** grow the account as much as possible; the benchmark is SPY and QQQ.

**Scope (Ryan's correction):** test the **methods**, not the account's past. The account's earlier losses were mostly Ryan's own hedges, so account history is not used here.

**Evidence:** `backtest.py`, run on GitHub Actions with FMP's split- and dividend-adjusted daily data. Full numbers are in `backtest_results.md`. The code reuses the live `grade.py` and the live RSI function, grades every session, and replays each process day by day from 2019 to today. Fills are at the signal close ±5 bp; a `_lag1` variant fills at the next close.

---

## 1. Verdict in one table

| Question | Answer | Confidence |
|---|---|---|
| Does today's live equity process beat SPY/QQQ? | **No. It ranked last or near last in all four universes tested** (5–19%/yr vs QQQ 23.1%) | High |
| Why? | **The RSI2 ≥ 70 take-profit.** It wins ~70% of trades but its average win is ~0.5–0.6× its average loss, with a 4-day hold. It sells leaders at the first bounce | High |
| Does the quality grade pick winners? | **Somewhat, and only when leaders are held for weeks** (monthly rotation). It beat QQQ inside QQQ's own end-2018 pool by +3 to +6.5 pts/yr, but lost to SPY inside the S&P 100 pool, and 2 names made most of the profit | Low–moderate |
| Does idle cash hurt? | Yes. A 25% idle reserve cost 1–8 pts/yr; holding QQQ with the spare cash always helped | High |
| What reliably beats QQQ? | **2× Nasdaq (QLD) held only while QQQ is above its 200-day average**, T-bills otherwise. It beat QQQ over 2007–2026 (including 2008) **with a smaller worst drawdown than QQQ itself** | Moderate |
| Day track? | The edge is real and positive net of costs over 2 years (paper rules +0.158R/trade). **Our added rules cut it by two-thirds.** At this account size it's worth about $250/yr | Moderate |
| Options? | Not testable (no historical options data). Leverage is cheaper through QLD than through single-leg calls | — |

---

## 2. Equity process results

Annual growth rate 2019-01-02 → 2026-09-29. QQQ = 23.1% (max drawdown −35%), SPY = 17.2% (−34%).

| Universe | Why it matters | CURRENT (live) | Best variant | Best variant vs QQQ |
|---|---|---|---|---|
| A1 today's scan list (236) | Built recently, so it contains this cycle's winners: **hindsight** | 18.8% | Top-ranked A/A+ held until they leave the top 25%: 81.8% | +59 (not credible) |
| A2 same list minus 41 speculative names | Still hand-picked recently | 13.9% | Same: 59.6% | +37 (not credible) |
| A3 **S&P 100 as of end-2018** | Fixed before the test period, **no hindsight** | 5.0% | Monthly top-4 rotation, spare cash in QQQ: 15.4% | **−7.7** |
| A4 **Nasdaq-100 as of end-2018** | QQQ's own pool, **no hindsight** | 5.9% | Monthly top-4 rotation: 26.3% (29.6% lag-1, 24.5% at 25 bp costs) | **+3.2 (+1.4 to +6.5)** |

- **What to take from it:** the huge A1/A2 numbers are what a hand-picked, hindsight watchlist produces. They say little about the method.
- **Inside the unbiased pools:**
  - The **CURRENT process loses to both benchmarks by 11–18 pts a year.**
  - Holding leaders for about 2 months (monthly rotation) is consistently the best way to use the grade.
  - Even that beats QQQ only inside QQQ's own pool, mostly from WDC and NVDA.
  - Its 2023–26 edge in that pool is about zero.

---

## 3. Index alternatives (real ETF prices, then a simulation back to 2007)

Real funds, 2019 → today (fees and leverage decay included):

| | Annual return | Worst drop |
|---|---|---|
| QQQ | 23.1% | −35% |
| QQQ + 200-day filter | 19.5% | −22% |
| QLD (2×) | 37.0% | −64% |
| **QLD + 200-day filter** | **33.6%** | **−40%** |
| TQQQ (3×) + 200-day filter | 46.3% | −55% |

Simulated daily-reset leverage, 2007-08 → today. This includes the 2008 crisis. FMP's QQQ history starts 2006-11, so the 2000–02 crash is **not** covered. The simulation runs 1–3 pts/yr optimistic compared with the real QLD/TQQQ:

| | 2007–2026 | 2007–09 crisis | 2010–2018 | 2019–2026 |
|---|---|---|---|---|
| 1× QQQ | 16.1% (−54%) | −18.3% | 15.3% | 22.9% |
| **2× + 200-day filter** | **20.2% (−47%)** | **−19.0%** | **11.5%** | 34.6% |
| 2× buy & hold | 24.2% (**−83%**) | −43.1% | 25.0% | 38.3% |
| 3× + 200-day filter | 26.1% (−63%) | −29.6% | 13.4% | 48.0% |

**What the 2× + filter row means:**
- **Upside:** over 19 years it beat QQQ by about 4 pts a year (about 3 after the simulation's optimism), and its worst drop (−47%) was smaller than holding QQQ itself (−54%).
- **Weak spot:** it **lagged QQQ for most of 2010–2018** (11.5% vs 15.3%). Choppy markets whipsaw the 200-day switch. Expect multi-year stretches of trailing QQQ. That is the price of this approach, not a malfunction.
- **Unleveraged or unfiltered versions:** filtered 1× never beats QQQ. Unfiltered 2×/3× beats it but carries −83% / −95% drawdowns.
- **Prior work:** this is the published "leverage + trend filter" approach (Gayed & Bilello, *Leverage for the Long Run*, 2016; the 200-day rule follows Faber 2007).

---

## 4. Day track

2 years, 500 sessions, 5-minute bars (1-minute data is paywalled on this data plan), 1¢/side cost:

| Rules | Trades | Win % | Net R/trade | Total net R | Excl. best trade |
|---|---|---|---|---|---|
| Paper (stop at opposite OR edge, 10R target, else hold to close) | 499 | 28% | **+0.158** | +78.8 | +68.8 |
| **Ours** (breakeven at +1R, trail from +2R, 12:00 chop exit, 15:30 flat) | 462 | 29% | **+0.053** | +24.3 | +17.3 |

- **Our exit rules cut the right tail the strategy lives on.** Revert to the paper's rules if the track is kept.
- **Dollars:** at about $6.41 per R (a ~$2,500 cash-bound QQQ position), the paper's rules made about $250/yr. That is about 10%/yr on the cash it ties up during the day, **less than the same cash would expect in the core.** It only adds value on top of a core that can't use that cash.

---

## 5. Recommended setup (needs Ryan's approval: it replaces the swing, options and day-track mandates)

| Sleeve | Weight | Rule | Why |
|---|---|---|---|
| **Core** | **~75%** | **QLD while QQQ closes above its 200-day SMA; otherwise SGOV/BIL (T-bills).** Checked once a day after 15:30 ET; switch at that close or the next | The only tested approach that beat QQQ across 2007–2026 with a smaller worst drawdown. Mechanical, ~4 switches a year |
| **Satellite** | **~25%** | Monthly: hold the top-4 grade A/A+ names from a **liquid large-cap pool** (Nasdaq-100 + S&P 100, not the hand-picked speculative list). Sell only if a name leaves the top 25% at the monthly check. Spare cash → QQQ | The grade's best, most honest use. Keeps a measurable stock-picking track record against QQQ |
| Cash | ~2% | Fees and plumbing | 25% idle cost 1–8 pts/yr |
| **Retire** | — | The RSI2 swing process, autonomous options, the day track (or paper-only with the paper's rules) | Last in every test / not testable / worth less than the core |

**Blended expectation:** 2019–26 about 32%/yr vs QQQ 23%, with a 2008-type drawdown of about −40 to −45%. **These are historical, not promised returns.**

**Things Ryan must accept or reject:**
1. **This is leverage.** QLD is 2× daily and can fall ~50% in a crash even with the filter. It uses no margin (the fund holds the leverage, and your account borrows nothing), but it moves twice as hard as QQQ. That is within the letter of the no-margin rule but is a real change in risk.
2. **It can trail QQQ for years** (2010–2018 did), and a sharp one-day crash can land before the filter reacts.
3. **Taxes:** in a taxable account every switch realizes gains, mostly short-term.
4. **HARD RULE 5 is unaffected.** No stops are needed; the 200-day switch is the risk control.

**Simpler operations:** 1–3 runs a day instead of ~26. `CLAUDE.md` can shrink from 289 KB to the rules above. The scoreboard becomes **account return vs QQQ**, reported daily. Freeze the rules for 6 months, then re-run `backtest.py` and review.

---

## 7. Day-trading strategies and the core/day split (added 2026-09-29, `intraday_results.md`, `combo_results.md`)

**Intraday strategies, QQQ 5-minute bars, 2018 → today (2,179 sessions), after costs:**
- **Opening-range breakout: lost money** on QQQ and SPY in every variant, including the paper's own risk sizing at up to 4×. **Retire the current day track.**
- **Intraday momentum and the gap strategies:** no edge.
- **Noise-area breakout (Zarattini, Aziz & Barbon 2024):** +8.7%/yr at 1×, and +25.3%/yr with a −30% max drawdown through a 3× fund. Positive in 8 of 9 years, including +43% (3×) in 2022. It was weak on SPY, though (+1.4%/yr at 1×).

**Robustness of the noise-area sleeve (3×):**
- Checking every **30 or 60 minutes works** across 10/14/20-day lookbacks (22–29%/yr). Checking every **15 minutes does not** (~7%/yr); the extra trades eat the edge.
- **The edge is cost-sensitive:** doubling costs to 6 bp per side cuts it to 9%/yr.
- **It is weaker in the second half** of the sample (about 15–21%/yr vs 29–40% in the first half).

**Core (QLD + 200-day switch) / day (3× noise-area) splits, monthly rebalance, 2018 → today.** QQQ buy & hold: 20.0%/yr, −35% max drawdown, −32% worst year.

| Split | CAGR | Max DD | Worst year | $3,340 → |
|---|---|---|---|---|
| 100 / 0 | 26.8% | −44% | −36% | $27.6k |
| 70 / 30 | 28.8% | −34% | −16% | $31.2k |
| **60 / 40** | **28.9%** | **−31%** | **−9%** | $31.5k |
| **50 / 50** | **28.9%** | **−29%** | **−1.5%** | $31.2k |
| 0 / 100 | 25.3% | −30% | −4% | $24.0k |
| 100 core + overlay (day trade the core's idle cash when it is in T-bills) | 38.3% | −57% | −14% | $59.0k |

- **The two sleeves are slightly negatively correlated** (−0.14 daily). Blending them keeps the return and roughly halves the bad years: every split from 70/30 to 40/60 beats QQQ by ~9 pts a year with a smaller worst drawdown than QQQ.
- **The overlay earns the most but carries the deepest drawdown.** It runs the 3× day strategy in exactly the markets where the core has stepped aside.

**Recommendation:** 50/50 or 60/40 core/day, rebalanced monthly. The day sleeve checks every 30–60 minutes; 60 minutes means fewer trades and less cost. **Paper-trade the day sleeve first.** The whole edge depends on real fills costing ≤ ~3 bp of capital per side. The agent must act within a few minutes of each :00/:30 bar close, through TQQQ/SQQQ. Limits: 8.7 years, no 2008 in the intraday data, the 3× fund modelled as exactly 3× QQQ, and taxes ignored.

---

## 8. Swing sleeve (overnight / multi-day) and three-sleeve splits (added 2026-09-29, `swing_results.md`)

**Swing rules alone on QQQ, 2007-08 → today (includes 2008), CAGR / max drawdown.** QQQ buy & hold: 16.2% / −53%.

| Rule | 1× | 2× | 3× | Time in market |
|---|---|---|---|---|
| Overnight (close→open), only above the 200-day | 6.9% / −19% | 13.0% / −36% | 18.4% / −50% | 80% of nights |
| RSI(2) < 10 pullback, exit above the 5-day SMA | 5.5% / −13% | 9.4% / −25% | 12.6% / −37% | 16% |
| IBS < 0.2 reversion | 8.0% / −16% | 14.4% / −30% | 20.1% / −44% | 32% |
| Turn of the month | 4.5% / −24% | 7.0% / −46% | 8.5% / −62% | 24% |
| **Union of RSI2 + IBS + turn-of-month** | **13.5% / −26%** | **25.5% / −49%** | **36.1% / −65%** | 52% |

- **At 1×, the union made 13.5%/yr while in the market half the time,** with half of QQQ's drawdown. It lost only 1.6% through the 2008 crisis, when QQQ lost 18%.
- **Leverage scales it up** but brings back 2008-sized drawdowns: −49% at 2×, −65% at 3×.

**Three-sleeve portfolios, 2018 → today, monthly rebalance.** QQQ buy & hold: 20.0%/yr, −35% max drawdown, −32% worst year. The swing sleeve correlates +0.67 with the CORE and −0.06 with the DAY sleeve.

| CORE / DAY / SWING | Swing via | CAGR | Max DD | Worst year | $3,340 → |
|---|---|---|---|---|---|
| 50 / 50 / 0 | — | 28.9% | −29% | −1.5% | $31.2k |
| **40 / 30 / 30** | **2× (QLD)** | **31.7%** | **−24%** | **−9.8%** | **$38.0k** |
| 34 / 33 / 33 | 2× | 31.9% | −22% | −6.9% | $38.5k |
| 30 / 40 / 30 | 2× | 31.6% | −20% | −2.2% | $37.6k |
| **34 / 33 / 33** | **3× (TQQQ)** | **37.8%** | **−24%** | **−10.3%** | **$56.6k** |
| 30 / 40 / 30 | 3× | 37.0% | −22% | −5.5% | $53.6k |
| 0 / 50 / 50 | 3× | 41.5% | −20% | +4.2% | $71.4k |

- **The union swing sleeve adds about 3–9 pts/yr on top of the two-sleeve mix at a similar or smaller drawdown.** The overnight-only version added nothing on top of the core, because it overlaps the core too much.
- **Why keep the core** even though 0/50/50 scored best in this window: it is the only sleeve with a 19-year record that includes 2008. The day sleeve has 8.7 years of data and weakened in its second half, and the 3× swing sleeve drew down −65% in 2008.

**Implementation notes:**
- **Timing:** the swing rules decide on the day's close. Live, the agent would check at about 15:50 ET with the live price and send a market order before the close. The small timing difference is not yet tested.
- **Gaps in testing:** the swing rules have not been checked on SPY, and each rule's settings have not been varied (e.g. RSI 5 vs 10, IBS 0.15 vs 0.25).
- **Taxes:** every sleeve trades often, so gains are mostly short-term.

---

## 9. Do last year's biggest winners keep winning? (added 2026-09-29, `winners_results.md`)

**Universe:** the S&P 100 and Nasdaq-100 as of end-2018, years 2019–2026. FMP's point-in-time constituent history is paywalled (HTTP 402), so the end-2018 lists are used; they carry no hindsight for 2019 onward.

| | S&P 100 pool | Nasdaq-100 pool |
|---|---|---|
| Rank correlation, last year's return vs this year's (7-year average) | **+0.06** (−0.49 to +0.38) | **−0.04** (−0.50 to +0.37) |
| Last year's top 10: average next-year return | +25.7% vs SPY +18.4% | +22.6% vs QQQ +26.2% |
| Top-10 hit rate vs the ETF | 51% | 39% |
| Buy last year's top 10 each January (CAGR) | **24.4%** vs SPY 17.2% | **19.3%** vs QQQ 22.6% |
| Buy last year's top 5 each January (CAGR) | 30.9% (worst year −4.7%) | 22.1% (worst year −35.5%) |
| **Monthly: hold the 10 best trailing-12-month names** | **23.1% / −14% max DD** vs SPY 17.2% / −24% | **28.1% / −25%** vs QQQ 23.1% / −33% |

- **Calendar-year winners are a coin flip for the next year.** The correlation averages about zero and swings wildly. Winners crashed in 2022 (the Nasdaq top 5 lost 35%), and in 2023 the prior year's *losers* led (+76% / +94% for the bottom decile).
- **The standard monthly version works in both pools.** Refreshing the list every month means momentum reversals get sold within weeks instead of held for a year. It beat SPY and QQQ by about 5–6 pts a year with smaller drawdowns.
- **This simple rule matched the 12-trait grade's monthly rotation** (28.1% vs 26.3% in the same Nasdaq-100 pool). The extra traits added nothing measurable.
- **Limits:** 7 years, one fallback list per index, no 2008, and profits concentrated in a few names (NVDA, MU, LRCX, WDC).

---

## 10. Factor horse race: which ranking signal picks winners inside SPY/QQQ? (added 2026-09-29, `factors_results.md`)

**Setup:** 13 published signals, scored monthly 2019–2026 (93 months) in the end-2018 S&P 100 and Nasdaq-100 pools. Two measures: the IC (rank correlation with next month's return, t > 2 = real) and a monthly top-10 portfolio.

| Signal | IC t-stat (S&P / NDX / pooled) | Top-10 vs ETF (S&P / NDX / pooled) |
|---|---|---|
| **12-month momentum** | +0.5 / +0.3 / +0.3 | **+5.8 / +4.1 / +7.7 pts/yr** |
| 12-1 momentum | +0.2 / +0.2 / +0.1 | +3.8 / +1.4 / +4.1 |
| Residual momentum | −0.0 / −0.0 / +0.1 | −2.5 / +1.0 / +4.4 |
| Risk-adjusted momentum | +0.3 / +0.5 / +0.3 | +0.3 / −0.2 / +0.5 |
| Earnings surprise | +1.0 / +1.0 / +1.1 | +0.6 / −0.2 / −4.2 |
| Gross profitability | −0.2 / **+2.8** / +0.8 | −3.9 / −3.9 / −3.8 |
| 52-week-high proximity | −0.0 / +0.1 / −0.1 | **−7.6 / −12.9 / −16.1** |
| Low volatility | −1.1 / −1.0 / −1.1 | **−7.7 / −13.7 / −13.0** |

- **No signal predicts the whole ranking reliably.** Every IC is near zero (−0.03 to +0.04), and only one of 39 t-stats clears 2. That one is profitability in the Nasdaq pool, and its top-10 portfolio still lost to QQQ. With 39 tries, one hit is about what luck produces.
- **Plain 12-month momentum is still the most useful stock picker.** Its top 10 beat SPY and QQQ in all three pools by 4–8 pts/yr. But its IC is ~0, so the edge comes from catching a few big right-tail winners each year, not from a reliable correlation. Expect long flat stretches.
- **The more sophisticated momentum versions added nothing** over the plain one (residual, smooth, risk-adjusted, composite).
- **52-week-high proximity and low volatility were the worst signals.** The 52-week-high trait is part of the current 12-trait grade, which fits the grade adding nothing measurable (section 9).

---

## 11. Robustness batch (added 2026-09-29, `robust_results.md`)

**Swing sleeve:**
- **Settings.** It holds across one-at-a-time parameter changes: 12.8–14.2%/yr at 1× over 2007–2026 for every variant, against a 13.8% baseline. All three parts matter; removing IBS or TOM costs 4–5 pts.
- **SPY.** The rules work on SPY too: 8.6%/yr at 1× with a −19% max drawdown, vs SPY buy & hold at 11.0% / −55%, and 15.7% at 2×.
- **Execution timing is the real cost.** Deciding and trading at 15:50 ET on the live price, instead of the exact close, cuts the 2018–26 CAGR from 19.2% to 14.6% at 1× and from 37.1% to 26.8% at 2×. Most of the gap is in 2018–21. **The 15:50 numbers are the realistic ones.**

**2000–02 crash:** ^NDX index history is not served on this FMP tier (and QQQ history starts 2006-11), so **the leveraged core has not been tested against 2000–02**. It remains the largest untested risk.

**Core variants, real ETFs, 2007–2026 (CAGR / max DD):**

| Core | 2007–26 | 2022 |
|---|---|---|
| QLD + 200d → T-bills (baseline) | 21.4% / −46% | −37% |
| → TLT when out | 19.4% / −60% | −56% (bonds fell with stocks) |
| → GLD when out | 24.0% / −47% | −40% |
| → dual momentum (TLT/GLD/BIL) | 21.8% / −48% | −43% |
| **Vol-target 25% (≤ 2×) + 200d → T-bills** | **18.0% / −42%** | **−20%** |
| Vol-target 30% (≤ 2×) + 200d → T-bills | 19.9% / −44% | −24% |
| QQQ buy & hold | 17.5% / −49% | −34% |

**40 / 30 / 30 portfolio, 2018–2026** (QQQ: 20.0%/yr, −35% max DD, −32% worst year):

| Core in the mix | Swing executed | CAGR | Max DD | Worst year |
|---|---|---|---|---|
| QLD + 200d → T-bills | close | 31.7% | −24% | −9.8% |
| QLD + 200d → T-bills | 15:50 | 28.6% | −28% | −9.5% |
| **Vol-target 25% + 200d → T-bills** | close | **29.2%** | **−16%** | **−1.7%** |
| Vol-target 25% + 200d → dual momentum | 15:50 | 26.7% | −21% | −4.7% |

**What the batch changes:**
- **Make the core volatility-targeted.** Exposure = 25% ÷ QQQ's 20-day realized volatility, capped at 2×, still switched off below the 200-day SMA. It is held as a QQQ/QLD mix: e.g. 1.4× = 60% QLD + 40% QQQ. That gives up ~2 pts of return and **cuts the portfolio's max drawdown by about a third**.
- **Keep T-bills as the "off" asset.** Bonds fell with stocks in 2022; gold and dual momentum added nothing reliable.
- **Plan on the 15:50 swing numbers.**
- **Realistic 2018–26 expectation for the plan:** about 26–29%/yr vs QQQ's 20%, with a max drawdown of about −16% to −21% vs −35%. Historical, not a promise.

---

## 6. Limits of this evidence
- **Survivorship bias:** the end-2018 pools still lose any names FMP no longer carries (small effect). The A1/A2 universes are heavily hindsight-biased and should not be used for decisions.
- **One market history:** 2007–2026 is one path, mostly a strong Nasdaq era; 2000–02 is untested. Leveraged Nasdaq in a 2000–02-style decline with repeated whipsaws would be worse than anything shown here.
- **Missing inputs:** no earnings calendar history, and fills are at closing prices. The day-track sample is only 2 years.
- **Nothing here is a guarantee.** Re-run `backtest.py` whenever the rules change.

### Sources
- Backtest: `backtest.py`, results in `backtest_results.md` (Actions runs 2026-09-29).
- Zarattini & Aziz, *Can Day Trading Really Be Profitable?* (SSRN 4416622).
- Gayed & Bilello, *Leverage for the Long Run* (2016).
- Faber, *A Quantitative Approach to Tactical Asset Allocation* (2007).
- Bryzgalova, Pavlova & Sikorskaya, *Journal of Finance* 78 (2023) — retail options costs.
