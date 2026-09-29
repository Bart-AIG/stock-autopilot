# Process audit — 2026-09-29

**Goal (Ryan):** grow the Agentic account as much as possible; the benchmark is SPY and QQQ.
**Scope:** all three books (equity swing, options, day track), plus capital policy, measurement and operations.
**Evidence:** the broker's full trade record (`get_pnl_trade_history span=all`, `get_realized_pnl`), live account state on 2026-09-29, SPY/QQQ weekly bars, the repo's code and rules, and published research.
**Honest limit:** this environment cannot reach outside market data (Yahoo/Stooq are blocked; FMP is reachable only from GitHub Actions). None of the recommendations below is backtested yet. Section 8 lays out how to test them before switching anything.

---

## 1. Scorecard: where the account stands against the benchmark

| | Start (first close 2026-06-05) | Now (2026-09-29) | Change |
|---|---|---|---|
| Agentic account | ~$3,845 (implied: now + realized losses, assuming no deposits or withdrawals) | $3,340 | **≈ −13%** |
| SPY | ~755 (week of 06-01) | ~765 | ≈ +1% |
| QQQ | ~737 (week of 06-01) | ~739 | ≈ 0% |

The benchmark was roughly flat over this stretch, and the account lost about 13 points against it.

**Where the loss came from (broker realized P&L, June → today, 92 closes):**

| Book | Closes | Wins | Realized |
|---|---|---|---|
| Options | 21 | 9 | **−$572** |
| Equities | ~71 | ~48 | **+$78** |
| **Total** | 92 | | **−$494** |

- **The options book accounts for the whole shortfall.** The equity book is roughly breakeven: a +2% gain on ~$3k over four months, close to the benchmark.
- **Neither book has beaten the benchmark.** Equities about matched it and options lost to it badly.
- The equity figures are my classification of the trade list (option closes are the rows priced per contract). The totals reconcile to the broker's −$494.03.

---

## 2. The most important finding: the system does not measure what you care about

- **You measure excess return; the system does not.** Your goal is to beat SPY and QQQ. The system's scoreboard (`calibrate.py`, the Friday review) measures **win rate over the breakeven win rate**. That is a health check on a trading rule, not on the account. A book can post a +22-point margin over breakeven and still trail QQQ by 20% a year. The 72%-win-rate equity book did roughly that: it won often, made little, and missed the rally.
- **There is no benchmark tracking at all.** No run computes the account's return against SPY/QQQ over the same window, so nobody can say whether the system is working.

**Fix (small, no strategy change):**
- Add a daily `benchmark.json`: account total value (time-weighted, net of any deposits) vs SPY and QQQ total return since a fixed start date.
- Print the gap at the top of every daily report.
- Make **"excess return vs QQQ, rolling 3 months"** the primary metric the weekly calibration and the Friday review answer to. Keep margin-over-breakeven as a secondary health check per rule.

---

## 3. Capital: about 25% of the account is structurally idle

The capital policy always keeps **25% of the account out of the market**:
- 20% is reserved for options, and it has held no position most days (today: $668 reserved, $0 used).
- 5% is the operational reserve.

On top of that, cash waits between trades whenever no A-grade setup triggers. Today, after the TGT buy, about $836 of the $3,340 (25%) is cash.

**Why it matters for the benchmark:**
- A fully invested QQQ holder has 100% exposure. This account has 60–75%.
- In a rising market that alone guarantees underperformance, before any trade is taken.
- It is the single easiest thing to fix.

**Fix: make QQQ the default holding instead of cash.** This is the standard **core-satellite** structure used by active managers who are measured against an index.
- Anything not assigned to a live A/A+ position sits in **QQQ**, the benchmark itself.
- Keep a real **2% cash** buffer for fees. 5% is more than the account needs at this size, and nothing has ever needed it.
- A new swing entry is funded by selling that amount of QQQ. An exit's proceeds go back into QQQ at the next run.
- **Consequence:** "doing nothing" now **matches the benchmark** instead of lagging it. The trading book only has to add value *on top of* QQQ, instead of first earning back 25% of idle exposure.
- **Trade-off:** it adds turnover (QQQ trades in and out), and on a taxable account those are short-term gains. QQQ's spread is about $0.01, so the dollar cost is trivial.

---

## 4. Equity book: the entry and exit rules come from opposite strategies

| | What it is | Where it comes from |
|---|---|---|
| **Entry (since 09-25)** | Quality grade A/A+: 52-week high proximity, relative strength, 12-1 momentum, MA stack, then buy the pullback | **Momentum / trend-following.** The edge is that leaders keep leading (Jegadeesh & Titman 1993; George & Hwang 2004; the O'Neil / Minervini practitioner canon) |
| **Main exit** | RSI(2) ≥ 70 take-profit, no magnitude test | **Short-term mean reversion** (Connors). The edge is a quick snap-back from oversold |
| **Loss rule** | No price stop ever (HARD RULE 5) | Also from Connors, whose research shows stops *hurt* RSI(2) mean reversion |

**Why the mismatch costs money:**
- Momentum returns are made by a minority of big winners, the right tail. Momentum research consistently finds the return is concentrated in the names that keep trending for months.
- An exit that fires on the first 2–3 day bounce sells every leader before it can become one of those winners.
- The book's own record shows it:
  - MRK was sold today for +1.0% while still A+ #8.
  - TGT was sold 09-28 at $160.18 and bought back today at $157.03.
  - The old measurement ("the RSI2 exit sits a mean 0.84% from entry", 72% win rate, payoff 1.02) is exactly what capping the right tail looks like: many small wins and no big ones.
- The no-stop rule has the opposite problem. It was right for mean-reversion dips. For a momentum book, the discipline is the reverse: **cut losers fast, let winners run.** The ABNB (−$112) and UNP (−$41) time-stop sales on 09-24 are what a leader book with no loss control looks like.

**Recommended rules for the leader book (needs Ryan's approval: it amends HARD RULE 5 for this book):**

| Rule | Proposal | Rationale |
|---|---|---|
| Entry | Keep the grade + pullback trigger as is | The entry is sound |
| Initial loss cut | Close below the 50-day SMA, **or** −8% from entry, whichever comes first | The standard momentum discipline; −7 to −8% is the O'Neil/Minervini norm |
| Winner exit | Grade exit (rank leaves the top 25%) **or** a trailing stop (15% below the high, or a close below the 10-week MA) | Lets a leader run as long as it stays a leader |
| RSI2 ≥ 70 take-profit | **Drop it** for A/A+ holdings | It truncates the right tail |
| Rebalance | Monthly re-rank. Rotate the weakest holding if a clearly higher-ranked A+ name is available | Momentum portfolios are rebalanced monthly in the research |
| Share count | Prefer whole shares so the 15% trail can rest at the broker. Where fractional (DE 0.93 sh), the report tracks the trail level and the agent sells when it is breached | Fractional positions cannot carry native trails |

- **Stops are agent-monitored, not resting.** A resting stop would put an agent-placed stop on a swing position, which HARD RULE 5 forbids today. The rule change would allow either.
- **What this will look like:** a lower win rate (probably 40–50% instead of 72%) with a much higher payoff ratio. That is normal and expected for momentum. **This is exactly why the scoreboard must move to excess return (section 2):** under the current win-rate metric a better strategy would look worse.

---

## 5. Options book: pause it

**The evidence:**
- **−$572 on 21 closes (9 winners).** This is the whole account's underperformance.
- **The research is blunt.** Bryzgalova, Pavlova & Sikorskaya (*Journal of Finance* 2023) find retail options traders lose money on average, and mostly **from the cost of trading itself** (average bid-ask spread 12.6%), not from bad direction calls. This book's own chains quote 10–38% of mid on the graded names (ABBV 24%, DE 31.5% today).
- **The 20% bucket ($668) holds at most one position.** That makes each trade a single bet with no diversification.
- **The gate and the candidate list are mismatched:**
  - The re-grade prices illiquid pullback names instead of liquid A+ names (NVDA, AMD, MSFT).
  - The 20% payoff-at-target test uses equity mean-reversion targets (TGT: +4.7%) that an at-the-money call cannot meet.
  - The system has spent most of the past month *not* trading options, while paying the idle-capital cost in section 3.

**Recommendation:**
1. **Pause new speculative options entries.** Return the 20% bucket to the core (section 3). That adds about 20% more market exposure, worth more to the benchmark race than the options book has ever delivered.
2. **Keep hedging as a live-session decision with Ryan** (e.g. an index put before a known risk), not an autonomous sleeve.
3. **If options are revived later:**
   - Limit them to SPY, QQQ and ≤3%-spread mega-caps.
   - Use a target suited to options (the implied move, not the equity swing target).
   - Require the trade to beat simply holding the stock with the same dollars, over the same horizon, in a written comparison.
   - Revive only after the equity book has shown excess return over at least 20 closes.

---

## 6. Day track: do not go live Monday

The track is a copy of Zarattini & Aziz's 5-minute QQQ opening-range breakout ("Can Day Trading Really Be Profitable?", SSRN 4416622), with three material differences:

| | Paper | Our day track |
|---|---|---|
| Profit side | Target 10R, else **hold to the close** | Stop to breakeven at +1R, ATR trail from +2R, **close at 12:00 ET if under 0.5R** |
| Hit rate / edge | 24% hit rate, **+0.13R per trade**. The edge is entirely the rare big winner | Same signal, but the exit rules cut off most of those winners |
| Sizing | 1% risk, **up to 4× leverage** | Cash-bound: R ≈ $4 at this account size |
| Costs | Commission only. **No spread, no slippage, no out-of-sample test**. An independent replication on five indices this month found the gross result reproduces but is **~zero net of costs** | — |

**Our paper record matches the paper's shape:** 8 signals, total +6.47R, but **one trade (+6.48R on 09-21) is the entire result**; the other 7 net −0.01R. `graduate()` checks only total expectancy, so it will likely pass Monday on what is, statistically, one lucky trade.

**Even at its best the dollars cannot move the account.** At +0.13R per trade and R ≈ $4, the expected gain is about **$0.50 per trading day**. Meanwhile it takes first claim on deployable cash each morning and is the most complex piece of the system.

**Recommendation:** retire the day track, or at minimum keep it in paper, match the paper's exits exactly (no chop rule, no early breakeven) and require ≥50 signals **with the best trade removed** before any live vote. Phase 2 (TQQQ/SQQQ) is the only version that could matter in dollars, and it is also the version where a 0.13R edge that nets to zero after costs becomes a real loss.

---

## 7. Operations: rule churn and file bloat are now risks in themselves

- **Rule churn:**
  - Prompts v12 → v15 went live in one day (2026-09-29).
  - The rules changed three times this week.
  - The calibration counts only trades made under the current parameters. **Every change resets the evidence to zero**, so the system cannot learn anything.
  - In-regime closes since 09-25: **4**. Twenty is needed before any tuning.
- **File bloat:**
  - `CLAUDE.md` is **289 KB**, `holdings.json` **1.9 MB**, `trade_journal.json` **8.7 MB**.
  - Every run (up to ~26/day) re-reads them.
  - Most of `CLAUDE.md` is incident history; the rules that actually bind would fit in ~25 KB.
  - The file documents the errors this causes itself (stale-clone overwrites of master, miscounted throttles, runs obeying a stale prompt description).
- **Run cadence:** a 15-minute cadence made sense for options exits. With options paused and a monthly-rebalanced momentum book, **2–3 runs per day** suffice (open +45 min, midday, 30 min before the close). That is fewer tokens and fewer chances for a sibling-run collision.

**Recommendation:**
1. **Freeze the equity rules for ~20 closes** (roughly 6–8 weeks) once the section 4 decision is made.
2. **Rewrite `CLAUDE.md` to the rules in force** (target ≤30 KB) and move the history to `docs/history/`.
3. **Rotate the journal monthly.**
4. **Cut the cadence.**

---

## 8. How to validate before switching

The data lives where the scheduled report runs: GitHub Actions has the FMP key. I propose `backtest.py` plus a manual `workflow_dispatch` workflow that:

1. Rebuilds the 12-trait grade historically over the 236-name universe, 2019 → today, point-in-time. Survivorship bias is unavoidable with today's universe; that caveat must be stated.
2. Uses the same grade + pullback entries, with four exit variants:
   - (a) today's RSI2 ≥ 70 take-profit + grade exit;
   - (b) grade exit + 15% trail + −8%/50-day loss cut;
   - (c) (b) without the loss cut;
   - (d) monthly top-4 rotation, no pullback trigger.
3. For each variant, reports CAGR, max drawdown, turnover and **excess return vs SPY and QQQ**, with and without the QQQ core.
4. Also reruns the day track on 1-minute QQQ with the paper's exact rules vs ours, net of a 1¢ spread.

**Decision rule:**
- Adopt (b) or (d) only if it beats (a) **and** QQQ net of costs in the backtest.
- Then run it live, frozen, for 20 closes, judged on excess return.

---

## 9. Priority order and expected effect

| # | Change | Effort | Needs Ryan? | Expected effect vs benchmark |
|---|---|---|---|---|
| 1 | Benchmark tracking + excess-return scoreboard | small | no (measurement only) | Makes every later decision visible; no P&L effect by itself |
| 2 | QQQ as the default holding (core-satellite); reserve 5% → 2% | small | **yes** (capital policy) | Removes the ~25% idle drag. Likely the largest single gain |
| 3 | Pause speculative options; return the bucket to the core | small | **yes** | Stops the book that produced the whole shortfall |
| 4 | Don't graduate the day track Monday; retire it or re-spec it | small | **yes** | Avoids a live bet on one lucky trade; removes complexity |
| 5 | Backtest harness (section 8) | medium | no (read-only analysis) | Decides the exit question on evidence |
| 6 | Leader-book exits (drop RSI2 TP, add loss cut + trail) | medium | **yes** (HARD RULE 5) | Lets winners run; this is where excess return would come from |
| 7 | Freeze rules for 20 closes; slim `CLAUDE.md`; cut cadence | medium | yes for the freeze | Fewer errors, lower cost, a learnable system |

**What not to do:** add more gates. Every past fix added a rule, and the TACTICAL options track died of that. The changes above remove more than they add.

**A candid note on expectations:** most active strategies, professional ones included, do not beat QQQ over time (SPIVA scorecards; Barber & Odean on retail turnover). The structure above is designed so that *doing nothing* matches QQQ, and the strategy is only allowed to add risk where it has shown, in data, that it adds return. The only reliable way to *exceed* the index without skill is leverage (e.g. a trend-filtered TQQQ sleeve). It is not recommended here, because a leveraged ETF can lose 70–80% in a bear market (TQQQ in 2022). It is a legitimate option to discuss if you want more aggression than the stock-selection edge can deliver.

---

### Sources
- Bryzgalova, Pavlova & Sikorskaya, *Retail Trading in Options and the Rise of the Big Three Wholesalers*, Journal of Finance 78 (2023) — https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13285
- Zarattini & Aziz, *Can Day Trading Really Be Profitable?* (SSRN 4416622) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622
- Independent five-index replication of the ORB paper (gross reproduced, net ≈ zero), 2026-09-25 — https://www.mql5.com/en/blogs/post/776235
- Jegadeesh & Titman (1993) momentum; George & Hwang (2004) 52-week high (cited in CLAUDE.md's quality-grade section)
- Broker data: `get_pnl_trade_history(span=all)` and `get_realized_pnl(span=year)` on account 718757339, read 2026-09-29 ~19:30Z
