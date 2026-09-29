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
