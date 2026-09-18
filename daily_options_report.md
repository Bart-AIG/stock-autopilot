# Daily report — trading day 2026-09-18 (Friday, quad-witching)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-17 report, so this run owned the duty and took it. Quotes stamped 19:16–19:17Z, well past the opening auction.*

**One line:** **The desk placed exactly one trade today — the IBKR take-profit at 14:17Z, +$18.88 — and that sale is the whole story of the session, because it changed the constraint the book has been operating under all week.** Before it, deployable cash was **$369** against a **$600** minimum entry and both live books were shut on capital alone. After it, deployable is **$1,095.92** and a compliant entry existed at $600–$1,034 for the rest of the day. **Nothing was bought, and for the first time this week the reason is merit rather than money.** Twelve RSI(2) names were cut down to one full workup (MA), which was declined on a standing veto. The DAY TRACK stayed paused. The options book is empty and stayed empty.

---

## 1. DAY TRACK — PAUSED, no signal evaluated

| | |
|---|---|
| **Phase** | PAPER (paper day 3 of 10 complete; nothing has ever been placed) |
| **Status today** | **PAUSED** — `track_status(3445.95, [-1,-1,-1], [-1,-1,-1])` → `paused: True, "3 consecutive losing days — rest of week"` |
| **Graduation** | `graduate(3, [-1,-1,-1])` → `go_live: False — "paper 3d / 3 trades; need 10d and 8 trades"` |
| **Pause expires** | first run of **Monday 2026-09-22** |

Both figures were **re-verified by running the code against this run's own equity**, not inherited from the ledger. No opening range was taken and no signal was evaluated, which is correct: the pause is a bar on *taking* a signal, and the spec forbids an unattended run promoting or un-pausing the phase mid-week.

**Nothing has changed since yesterday's report** on either the pause or the structural problem it flagged — at this account size a long QQQ share costs ~$719, so the long side remains unbuyable and the eventual ten-day graduation sample will be shorts-only. That defect is recorded and is for the Monday calibration to weigh, not for a scheduled run to patch.

---

## 2. Positions — 2 of the 3–4 target slots

| Name | Entry | Now (19:16Z) | P/L | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|
| **ABNB** 6.5736 sh | 169.5209 (09-10) | 166.900 | **−$17.23 / −1.55%** | 8d of 14 | **09-24** | RSI(2) mean-reversion entry inside a rising 200-day uptrend. Thesis intact — the September softness has a named, non-structural driver, not a thesis break. |
| **UNP** 3.8582 sh | 285.1071 (09-10) | 280.000 | **−$19.70 / −1.79%** | 8d of 14 | **09-24** | Same RSI(2) setup, low-beta rail. Nothing has happened to the thesis; it is simply not working yet. |

**No exit fired on either, on any of the three mechanisms, and each was checked against a live bid rather than an inherited number:**

- **Take-profit (RSI2≥70 while GREEN):** unreachable by construction. Both names are underwater, and the trigger gates on `price > entry`. This is the 2026-08-26 correction doing its job — an RSI2≥70 print on an underwater position is an *optional* exit-into-strength routed to thesis, never a mechanical loss-realization.
- **Time stop (14 days):** day 8 of 14 for both, firing **2026-09-24**. The 3-day warn window opens **Monday**, not today.
- **Trailing stop:** not applicable. Green-enough triggers are ABNB $199.44 and UNP $335.42, both far away. The desk places no stop on a swing position (HARD RULE 5).

So the time stop is currently the only reachable exit on this book, which is the intended state for two sound-but-stalled theses.

---

## 3. Actions taken today — one, and it is the week's only trade

### IBKR — mechanical TAKE-PROFIT, +$18.88 (+2.67%) in 2 days

| | |
|---|---|
| Order | `6aad4800-7cdb-464f-bce8-8500fe86890b`, sell 8.109516 sh, market, regular hours, `placed_agent: agentic` |
| Filled | **2026-09-18T14:17:36.796Z** at **$89.6301** |
| Basis / proceeds | $707.96 → $726.86 gross, $0.02 fees |
| Broker realized | **+$18.90 gross / +$18.88 net** |
| Rule that fired it | RSI(2) ≥ 70 cross while GREEN — the Connors-pure take-profit |

**Why it was taken with no magnitude test, stated plainly because it looks small:** the 2026-09-02 rewrite VOIDED the "magnitude floor" heuristic. Measured across this whole book, the RSI2≥70 trigger sits a mean **0.84%** from the entry price, so the exit banks ~0–1% of position value *by construction* and no target-relative floor can ever be satisfied. The broker's own record says these small round trips are the edge, not noise: trades under ±$10 are 58% of all closes and net **+$90.48**. A +2.67% two-day close is comfortably above that band.

**The interesting part is what happened at the open, and it is already written up as a durable finding.** This same take-profit **fired and un-fired inside the opening auction**: at the 13:32Z auction print IBKR showed RSI2 **70.70** and green, and on the mandatory settled re-quote four minutes later it read **60.30**. The 13:33Z run did *not* take it — correctly, per the standing "never price a decision off the opening auction print" rule — and the trigger then re-formed properly later in the morning on a bid the desk could actually transact at. Two of today's durable findings come out of that sequence: `_THE_AUTONOMOUS_EQUITY_TAKE_PROFIT_FIRES_AND_UNFIRES_INSIDE_THE_OPENING_AUCTION_2026-09-18` and `_THE_BID_CLEARING_STANDARD_WITHHELD_A_FIRE_AND_THEN_PERMITTED_A_BETTER_ONE_SAME_SESSION_2026-09-18`. The discipline cost nothing and bought a better fill.

**What the sale did to capital, which is why it matters more than $18.88:** it converted a shut book into an open one mid-session. That is the first time this week capital was not the binding constraint.

---

## 4. Actions considered and SKIPPED — the educational section

Twelve names appeared on the RSI(2) board across the day's four report refreshes (13:3xZ, 15:08Z, 16:06Z, 19:06Z). **Every one is dispositioned; the 19:06Z board added zero ungraded names.** How the board was cut:

| Bucket | Names | Reason |
|---|---|---|
| **Held** | ABNB | Already owned — a buy is an ADD, not a fresh idea. |
| **Sector steer** | SLB | Oil energy. Excluded by Ryan's standing steer; no workup performed. |
| **Bank cohort veto** | C, PNC, WFC | `_FOUR_BANKS_ENTERED_THE_RSI2_BOARD_IN_ONE_REFRESH_AND_ONE_UNCALENDARED_GUIDANCE_EVENT_MADE_ALL_FOUR` — BAC's intra-quarter guidance to Q3 IB fees down ≥10% industry-wide, a driver no earnings calendar carries. Four banks moving as one fact is not four setups. |
| **Pharma/healthcare veto** | BMY, CVS, UNH | `_PHARMA_RSI2_CLUSTER_IS_A_POLICY_DE-RATING_NOT_A_MEAN_REVERSION_SETUP` — a policy de-rating does not mean-revert on a 2-period RSI. |
| **Trend-maturity clause (c)** | MDLZ, CRM, VZ, DASH, ROKU | All still making relative lows against SPY — the dip is in progress, not relieved. Declined **at the screen**; these did not each get a full HARD RULE 7 news check, and saying so is more honest than implying they did. MDLZ additionally carries a re-entry flag (exited from this book 2026-09-09). |
| **Full workup** | **MA** | The only name whose tape confirmed (+0.10% vs SPY −0.21%). |

### MA — declined, grade B+

Structure passed cleanly: 20 > 50 > 200, sitting on the 50-day, 200-day rising +0.108/day with ~321 sessions of cushion, an August golden cross, `[ERN]` verified clear against a 55-event calendar, and an analyst mean PT of $671.64 (+18.6%).

It was declined on a **standing durable disqualifier**, `_A_DIFFUSE_STRUCTURAL_NARRATIVE_IS_NOT_A_CATALYST`, written 2026-09-08 when V was declined on the identical driver — the 09-01 twenty-one-bank stablecoin consortium, BankChain, and the agentic-unbundling thesis that knocked V/MA/AXP/DASH together. **The release condition is the headline stream stopping, and it has instead added legs** (UK domestic payments rail, renewed card-fee crackdown). MA's own RSI2 trigger had also independently decayed 9.61 → 27.64 by the time it was worked up. Full record: `_MA_DECLINED_2026-09-18_STANDING_PAYMENTS_COMPLEX_VETO`.

Worth noting as process: the run cited the existing key rather than re-deriving a weaker objection, which is the failure `_A_DURABLE_REJECT_KEY_EXISTED_AND_THREE_RUNS_RE_DERIVED_A_WEAKER_OBJECTION_INSTEAD` names. It also discarded a search-aggregator claim that MA is "−25% over the past year" as incompatible with the measured rising 200-day and August golden cross — measured drawdown is −5.60% from the 08-24 high.

### Options — nothing graded, and the reason is the vol tape

The options book is **empty** and no CORE candidate reached a thesis. Index premium is genuinely expensive on our own measurements: **SPY IV/RV 1.4575 raw / 1.6869 ex-gap, 96.3rd percentile of its own history (n=27); QQQ 1.3088 / 1.5062, also 96.3rd.** Buying long index premium here is paying the richest relative level this file has on record.

The divergence is the notable part and is written up as `_INDEX_VOL_IS_AT_ITS_96TH_PERCENTILE_WHILE_NVDA_SITS_AT_ITS_18TH__THE_BID_IS_FOR_MACRO_PROTECTION_NOT_FOR_STOCKS_2026-09-18`: **NVDA sits at 0.7715 raw / 1.0495 ex-gap, its 18.5th percentile.** The vol bid is for macro protection, not for single stocks. That is context, not a thesis — cheap vol supplies no reason to own anything, and no CORE name cleared the entry stack.

**No `_cash_hold` was minted, deliberately.** There is no named opportunity being waited for; the book simply found nothing that grades A. Minting a hold here would be the void cash floor returning through the side door, which THE CAPITAL POLICY forbids.

---

## 5. Sleeve state (19:16Z)

| | |
|---|---|
| **Total account value** | **$3,445.95** |
| Equity value / options value | $2,177.73 / **$0** |
| Cash = buying power = **unleveraged** buying power | **$1,268.22** — identical, so **no margin is being extended** (FOUR LAWS #4 unambiguous) |
| Operational reserve (5% of total) | **$172.30** |
| **Deployable** | **$1,095.92** |
| Per-name cap (30% of account) | **$1,033.79** |
| Minimum entry | $600 — **clear**, a compliant entry exists |
| Equity slots | **2 of the 3–4 target** filled; 1–2 open |
| Options premium at risk | **$0.00**, CORE 0 of 3 open |
| Realized options P/L today | **$0.00** vs the −$400 cap (0 closes; measured against the broker, not defaulted) |
| Realized equities today | **+$18.88** (the IBKR take-profit) |
| Throttles used | equities **0 of 3** entries, options **0 of 3** — the IBKR sale was an EXIT, and exits are never throttled |
| Unsettled funds | $726.84 — the IBKR proceeds. On `limited_margin` these are spendable and are **already inside** the $1,268.22, not additive. |

Account re-confirmed **718757339, `limited_margin`, `option_level_3`, agentic_allowed**. Reconciliation against the broker at 19:16–19:17Z: **ZERO DRIFT in both books** — ABNB 6.573584 and UNP 3.858199 fully sellable and matching the ledger, 0 option contracts against 0 ledger rows, and `get_equity_orders` showing exactly **one** order all day (the 14:17Z IBKR sale, agentic, already ledgered) — so no sibling run landed anything.

---

## 6. Friday review — final broker re-source

The weekly review was written at 13:40Z and **amended at 14:50Z** after the IBKR close falsified three of its figures. This run performed the final re-source against the broker (`get_pnl_trade_history` span=week, read 19:17Z) and **the amended figures stand — no trade has printed since 14:17:36Z.**

**The week, broker-sourced (2026-09-14 → 09-18):**

| Book | Closes | Net |
|---|---|---|
| **Equities** | 3 — MMM −$30.96 (time stop), GD −$21.83 (warn-window exit-into-strength), IBKR **+$18.88** (take-profit) | **−$33.91** |
| **Options** | 3 — VLO 390P ×2 −$360, SPY 731P lapsed −$28, SPY 770C lapsed −$27 | **−$415.00**, and **all three are `placed_agent: "user"`** — Ryan's own. The desk opened, sized, managed and closed none of them. |

**Edge statistic, in-regime (post-2026-09-02 Connors-pure rewrite), n=7:** 2W/5L, win rate 28.6%, payoff ratio 0.58, breakeven 63.3%, **margin −34.71 pts**, expectancy −$9.50/trade.

**`recommend()` returns REPORT ONLY — n=7 < 20. No parameter moves in either direction, and the KILL branch is not reachable** (it is exempt from the in-regime gate, *not* from the sample-size floor ahead of it). So nothing was tuned.

**The honest reading of that margin, because a −34.71 looks alarming:** one $19 trade moved it **+42.19 points** and the payoff ratio **8.4×**. At n=7 the headline statistic has that sensitivity to a single small close. `MIN_TRADES_FOR_ACTION = 20` is not conservatism — it is the measured sensitivity of this statistic at this sample size. **Never quote a margin figure from a single-digit n without the n beside it.**

**Watch item carried to Monday:** **five of the seven in-regime closes are the time stop or its warn window; two are the actual mean-reversion take-profit.** Elapsed time still closes more of this book than mean reversion does. If the take-profit share is still ~2-in-7 at n=20, it is the **ENTRY trigger** that needs review, not the exits.

**Drift check: zero overrides logged this week.** The one action taken — the IBKR take-profit — is a gate being *obeyed*, not overridden. Stated honestly: the week was near-inactive, so a clean drift check reflects **inactivity as much as discipline**, and structure drift is untestable on an empty options book.

---

## 7. Tomorrow's watchpoints

- **Monday 2026-09-22 is a big run.** It carries the **weekly calibration** (broker-sourced, both books split, in-regime gate applied), the **DAY TRACK pause expiry** and its `graduate()` re-evaluation, and the **monthly-cadence momentum items**.
- **ABNB and UNP enter the time-stop warn window on Monday** (day 11 of 14), firing **2026-09-24**. Both are underwater, so the warn-window rule matters: a position about to be recycled anyway is better sold *into* a bounce than out of one.
- **Capital is no longer the binding constraint.** $1,095.92 deployable, one to two open slots, 30% per-name cap at $1,033.79. The next A-grade setup is fundable at full size — which raises the cost of a bad entry rather than lowering the bar for one.
- **Index premium at the 96th percentile** argues against opening long index vol; NVDA at its 18th is the divergence worth watching if a single-name CORE thesis appears.
- **Quad-witching today** — treat today's closing prints and volumes as unrepresentative when Monday's run computes baselines off them.
