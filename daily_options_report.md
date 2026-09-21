# Daily report — trading day 2026-09-21 (Monday)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-18 report, so this run owned the duty and took it. Quotes stamped 19:15–19:16Z, well past the opening auction.*

**One line:** **Three things happened today and each one changed a state the book had been stuck in for a week.** The desk bought **V for $1,000** — the first autonomous equity entry since 09-14, taken on merit with capital finally available. The **DAY TRACK printed its first winner in paper, +6.4774R (+$9.31)**, against −1R on each of its first three days. And the morning calibration's **options KILL branch was reversed** after Ryan challenged the attribution and the desk found two of its own measurement bugs. The book is now three swings deep, ~92% invested, and deployable cash is **$97.51** — below the $600 minimum entry, so the next trade waits on Thursday's time stops.

---

## 1. DAY TRACK — paper day 4, FIRST WINNER: +6.4774R

| | |
|---|---|
| **Phase** | PAPER (day **4 of 10**; **4 signals of 8**). Nothing has ever been placed. |
| **Status** | **ACTIVE** — `track_status(3410.93, [-1,-1,6.4774], [6.4774])` → `paused: False`. The 3-consecutive-loss pause expired at the week boundary and today's win broke the streak. |
| **Graduation** | `graduate(4, [-1,-1,-1,6.4774])` → **`go_live: False`** — *"paper 4d / 4 trades; need 10d and 8 trades"*. Next review **Monday 2026-09-28**. |

**Today's trade, end to end:**

| | |
|---|---|
| Opening range (1-min bars, 09:30–09:35) | high **728.84** / low **727.82**, range 1.02 pts, body **69.1%** of range → clean **LONG** signal |
| Entry | QQQ **729.2575**, 1 share (cash-bound), 13:37Z |
| Stop | OR low **727.82** → stop distance 1.4375 pts = **$1.44 per R** |
| Exit | **738.5688** at 17:05Z — the ATR trail, breached by the 16:52Z one-minute bar (low 738.500) and again at 16:53Z |
| Result | **+6.4774R = +$9.31**, banking **91.9% of peak** |

**The trail was not mis-set, and that is worth saying because it looked like it might have been.** Twelve ratchets moved the stop from breakeven to 738.5688 across four hours. The 16:47Z run flagged "thinnest room of the session" — correct, but it was a *symptom* of price sitting 0.63 under the session high, not a defect in the trail. Give-back tolerance at the close was 1.5 × atr5 = 0.8212 pts; the pullback that actually closed the trade ran **0.890 pts = 1.63 × atr5**. The trail did exactly what it is for: it let a 4-hour trend run and then took it out on a move genuinely larger than the prevailing noise.

**Running paper tally: 4 days, 4 signals, −1R / −1R / −1R / +6.4774R = +3.4774R cumulative.** Win rate 25% against a payoff-implied breakeven of ~13.4% — positive, and **n=4 is far too small to mean anything**. It is recorded as a fact, not as evidence. Graduation needs six more paper days and four more signals, and only a Monday calibration can flip the phase.

**The structural defect flagged last week has not gone away:** at this account size a long QQQ share costs ~$729 and only one is affordable, so long-side R is quantized brutally and the short side (PSQ) sizes into a different instrument entirely. Today's long happened to fit. That is for the 09-28 calibration to weigh, not for a scheduled run to patch.

---

## 2. Positions — 3 of the 3–4 target slots, all swing, all `placed_agent: agentic`

| Name | Entry | Now (19:15Z) | P/L | % of acct | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|---|
| **ABNB** 6.5736 sh | 169.5209 (09-10) | 167.770 | **−$11.51 / −1.03%** | 32.3% | 11d of 14 | **09-24** | RSI(2) mean-reversion inside a rising 200-day uptrend. Thesis **INTACT**, re-researched today. |
| **UNP** 3.8582 sh | 285.1071 (09-10) | 269.430 | **−$60.49 / −5.50%** | 30.4% | 11d of 14 | **09-24** | Same setup, low-beta rail. Thesis **INTACT and now explained** — the weakness is sector, not name. |
| **V** 2.7168 sh | 368.0799 (09-21) | 369.420 | **+$3.64 / +0.36%** | 29.4% | 0d of 14 | **10-05** | Today's entry. Only non-energy name clearing both the RSI2 and the rising-200-day gates with real margin. |

**No exit fired on any of the three mechanisms, and each was checked against a live quote:**

- **Take-profit (RSI2 ≥ 70 while GREEN):** ABNB printed **RSI2 71.6** on the 18:35Z report — the first ≥70 print this book has seen in a week — and it did **not** fire, because ABNB is **underwater (−1.03%)** and the gate is `price > entry`. Under the 2026-08-26 correction that is an *optional exit-into-strength routed to thesis*, never a mechanical loss-realization. Researched to **INTACT** and held (§3). V is the one green name and sits at RSI2 ~44, nowhere near the trigger.
- **Time stop (14 days):** day **11 of 14** for ABNB and UNP, firing **Thursday 2026-09-24**. Both are inside the 3-day warn window. They will be sold **green or red** — this is the book's only mechanical loss discipline and it does not negotiate.
- **Trailing stop:** not applicable anywhere. Green-enough triggers are ABNB **$199.44**, UNP **$335.42**, V **$433.04** — all far away. The desk places no stop on a swing position (HARD RULE 5).

**Concentration, stated plainly: ABNB at 32.3% and UNP at 30.4% are both over the 30% per-name cap — entirely on the denominator.** Neither position grew; the account value fell. The ruling is the same as 09-17: **STOP ADDING, NOT SELL.** The cap is a sizing gate, not a continuous constraint forcing liquidation, and HARD RULE 5 permits a sale only on a target hit, a green RSI2 bounce, or a thesis break. Thursday's time stops resolve it without paying a round trip.

---

## 3. Actions taken today — one entry, one research verdict, one reversal

### 3a. BOUGHT: V — 2.716801 sh @ $368.0799 = $1,000.00 (order `6ab13deb`, filled 14:23:39Z)

The day's **one of three** autonomous equity entries, taken by the 14:20Z run on the report that landed at 14:07Z — deliberately deferred past the opening window so the decision used *today's* report rather than Friday's.

**Grade A−, and the weak leg is stated rather than dressed up.** The full gate stack:

- **Technical:** RSI2 **8.6** — oversold, but shallowly so, and that is the weakest leg of the trade. The compensating strength is the trend: spot sits above a 200-day that is genuinely **rising**, with the 20-day above the 50-day, which is what a pullback inside an intact uptrend looks like.
- **HARD RULE 7 thesis:** INTACT. Payments network, no adverse company news, analyst posture constructive.
- **Earnings:** clean — nothing inside the 14-day hold window (verified against the calendar, not inferred from a blank column).
- **Sector steer:** non-energy. Five of the twelve setups on the board were excluded on the oil steer before grading.
- **Sizing:** $1,000 = **29.29% of account value at entry**, inside the 30% cap and above the $600 minimum. Deployable was $1,097.49; size = deployable ÷ remaining slots with one slot fundable.
- **Broker-first check:** `get_equity_orders(2026-09-21)` returned **zero** orders immediately before placing, then `origin/master` was re-fetched and `holdings.json` re-read. No sibling had landed an entry. Review gate `order_checks {}`.
- **Exit plan, written before the order:** thesis + **time stop 2026-10-05**. No price stop.

**Why only one entry, and it is arithmetic rather than judgement:** after the $1,000 fill the residual was **$97.49**, far below the $600 minimum. Under the concentration policy a sub-$600 entry is a *skipped* opportunity, not a small one — so no second name could have been funded at any grade.

### 3b. UNP — thesis researched to INTACT, and the unexplained part is now explained

UNP was down **−2.24%** on a **+0.88%** SPY tape, which the prior run had logged as "intact but unexplained". It is explained: **the move is sector, not name.** CSX −1.89% and NSC −1.41% on the same tape, driven by the **J.B. Hunt profit warning of 09-16** (JBHT −13%, its worst day since March 2020) on diesel at $6.31/gal, +70.5% y/y, which de-rated freight broadly.

The newest **UNP-specific** news is 09-16 and it is **bullish**: UBS upgraded Neutral → **Buy**, PT $310 → **$339**, citing 3.5% 2027 volume growth, intermodal +6–7%, and an explicit pricing tailwind *versus the truckload market* — i.e. the same diesel shock selling the rails is a relative **positive** for rail economics. Consensus mean PT **$334.04** against $269.43 spot = **+24%**. Verdict **INTACT**; holds to Thursday's time stop.

### 3c. ABNB — exit-into-strength flagged, researched, declined

The 18:35Z report was the first to flag ABNB **EXIT-INTO-STRENGTH (underwater — optional)** at RSI2 71.6 with the 3-day time-stop annotation. Genuinely new information, so it got a full HARD RULE 7 workup rather than a re-notice:

- Consensus **Overweight**, mean PT **$183.24** = ~+9.5% upside, and targets are being **raised**: RBC Outperform **$195** (today), Gordon Haskett $146 → $180 (09-11), Truist $134 → $161 (09-10).
- RBC today: the hotel push could add ~1M rooms to TAM by year-end.
- **Bear evidence weighed honestly:** RBC flags AI-agent competition as a real risk to digital travel marketplaces (judging ABNB "somewhat better protected than many"); two insider Form 4 sales on 09-14/09-15, both routine and both leaving large residual stakes.

**Verdict INTACT — hold.** CLAUDE.md does say a name about to be recycled is better sold *into* a bounce than out of one, and that was considered explicitly. It is advisory colour on a decision the ruleset routes through **thesis**, and it does not convert a technical print into a licence to realize a loss. Thursday's time stop remains the exit.

### 3d. GOVERNANCE: the options KILL branch was reversed, and the errors were the desk's

The 13:40Z Monday calibration fired the **KILL branch** on the options book (n=21, margin −13.41 pts, expectancy −$27.24/trade), halved position size and paused new agentic options entries. Ryan challenged it in a live turn — *"Don't kill options most of the negative plays were actually made by me"* — and he was **substantially right on the facts**. The desk verified that independently before acting, rather than deferring to the instruction alone, and found **two of its own measurement bugs**:

1. **Attributed by the CLOSING order.** The ownership gate is defined on the **open**. Every position one party opened and the other closed was filed to the wrong side.
2. **The hedge was never stripped.** The SPY 2026-11-20 700P at **−$247** is the largest single loss in the sample and is **insurance expected to decay** — exempt from every premium backstop by policy, and not an edge measurement at all. It alone is **43%** of the −$572 that triggered the KILL.

Corrected by opening order with the hedge stripped, **no bucket reaches the n=20 action threshold**: pure-agentic n=10 / −$141, pure-user n=6 / −$40, mixed n=4 / −$144. `recommend()` returns **REPORT ONLY** on every cut. **The KILL fired on a sample artifact and is withdrawn.** Options entries are **not** paused; size multiplier back to 1.0; every other gate unchanged.

**What this does NOT establish, and the distinction matters:** the corrected pure-agentic slice is **still negative** — −$141 over 10 closes, margin −17.44 pts, expectancy −$14.10. The reversal establishes the KILL was *unsupported*, not that the desk's options book is *healthy*. At n=10 it is **unmeasured**. No run should read this as a clean bill of health or as a reason to size up.

---

## 4. Considered and SKIPPED — the whole board, and why each one lost

Twelve RSI(2) setups on the 14:07Z report. **Capital was not the binding constraint when the board was graded** ($1,097.63 deployable, one fundable slot) — the bar was.

| Name | Grade | Why it was declined |
|---|---|---|
| **CVS** | **B** | The strongest-*looking* candidate on the board and declined on **measurement**. Deepest print (RSI2 1.0), best analyst file (27 buy / 3 hold / 0 sell, mean PT $114.58 = **+30.9%**), and **no adverse company news** across a −10% three-week slide. Killed by the **trend gate**: own-measured SMA200 **87.2432** vs spot 87.53 — a **0.33% buffer** on an average rising **$0.0594/day**, so the 200-day *crosses the entry price inside the 14-day hold*. At 30% size with no price stop, that is the one leg that cannot be marginal. |
| **DASH** | **C** | RSI2 3.9, +36% to consensus — and it **fails the trend gate outright on slope**: SMA200 188.627 → 188.608 → 188.545 across 09-16/17/18, i.e. **falling**. "Above a rising 200-day" is two tests and this passes only the first. Also the most correlated name on the board with the held ABNB. |
| **VZ** | **C** | RSI2 4.0 but the weakest conviction on the list — 10 buy vs **18 hold**, mean PT $50.64 = **+5.3%** upside — and it was **+0.02% on the day**, so there was no actual dip to buy. |
| **PM** | **C** | RSI2 7.2, +11.9% to a mean PT whose coverage last updated **2026-07-26** — two months stale, so the analyst leg is unverifiable at decision time. |
| **MDLZ** | **C** | RSI2 4.4 and +13.8% to PT, but the book **exited MDLZ on 09-09, twelve days ago**, and the report flags it as a re-entry. No articulable reason why this entry differs from the hold that just failed — and inventing one to justify a re-buy is exactly the churn the flag exists to catch. |
| **SLB, OXY, CVX, COP, XOM** | — | **Excluded before grading** on the standing de-emphasized-energy sector steer. Five of twelve; the report flagged the cluster itself. |
| **UNP** | — | Excluded as **HELD** — an add to a losing position needs Ryan's approval (FOUR LAWS #3). |

**The transferable half, and it is today's most useful lesson: the two best names on the board failed the *same* test, and it is the test the Connors setup is actually built on.** CVS and DASH both had excellent oversold prints and good analyst files, and both lack a genuine uptrend underneath the dip — DASH because its 200-day has stopped rising, CVS because its 200-day is about to *overtake the entry price during the hold*. A mean-reversion trade with no trend to revert *to* is not the setup; it is a falling knife with good statistics. Recorded in `_THE_RISING_200DAY_CAN_EXPIRE_THE_SETUP_DURING_THE_HOLD_SO_MEASURE_ITS_SLOPE_NOT_ONLY_ITS_SIDE_2026-09-21`.

**Options: no CORE candidate graded out, and IV is not what stopped it.** The book is empty, the pause is lifted, and nothing presented a thesis. The equity report's RSI2 names are now measured for a third time at near-zero options tradeability. The IV sweep independently rules out the reflexive trade — buying index or AMD premium on a strong-tape morning — without being a thesis either way: on the 2026-10-16 monthly (25 DTE, quoted 14:20Z outside the opening-window inflation), **long premium sits at the rich end of this file's own record on exactly the names a CORE entry would use — SPY 89.3rd percentile, QQQ 92.9th, MSFT 96.4th, AMD 100.0th.** The only sub-1.0 raw ratios (NVDA 0.7708, AVGO 0.9520) are single-gap artifacts reading 1.0414 / 1.1323 ex-gap.

---

## 5. Sleeve state

| | |
|---|---|
| **Account value** | **$3,414.23** (equity $3,146.01 + cash $268.22; options $0) |
| **Cash / buying power** | $268.22 — `buying_power` **==** `unleveraged_buying_power`, so **no margin is extended** and FOUR LAWS #4 is unambiguous |
| **Operational reserve** (5% of total, recomputed) | **$170.71** |
| **DEPLOYABLE** | **$97.51** — below the **$600** minimum entry, so **no entry is fundable in either book** until a position closes |
| **Options premium at risk** | **$0.00** — book empty, 0 open of max 3 CORE |
| **Realized options P/L today** | **$0.00** vs the −$400 cap (full headroom); 0 closing trades |
| **Realized equity P/L today** | **$0.00** — no closes. Last realized trade: IBKR take-profit 09-18, **+$18.90** |
| **Entry throttles** | Equities **1 of 3** used (V); options **0 of 3**; day track **1 of 1** (paper) |
| **Equity slots** | **3 filled of the 3–4 target** — at band, and the 4th is unfundable regardless |
| **Calibration applied this week** | **NONE.** Equity book HEALTHY (+12.99 pts margin over a 52.3% breakeven, expectancy +$3.73, n=49) but **only 7 of 49 closes are in-regime** against `MIN_TRADES_FOR_ACTION=20` → **report only, no parameter changed.** Options KILL fired and was reversed (§3d). Day track `graduate()` → `go_live: False`. |

**On the equity calibration, because a healthy reading that changes nothing looks like a wasted measurement and is not:** 42 of those 49 closes predate the parameters a calibration would move, so the sample carries **no evidence about them**. Tuning on it would be superstition — the in-regime gate working exactly as designed. Evidence rebuilds at roughly one close per week; 20 in-regime closes is a Q4 date, not an October one. And even then the asymmetry holds: a healthy reading may only lengthen the time stop, never loosen the entry trigger.

---

## 6. Tomorrow's watchpoints

1. **🔴 THE TIME STOPS ARE THURSDAY 09-24 — ABNB and UNP both fire, green or red.** Tomorrow they are 12 of 14 days, two days out. This is the single most consequential scheduled event on the book: it is the **only** mechanical loss discipline the swing sleeve has, and it is also **the funding event** — those two positions are ~$2,142, and until one closes, deployable cash stays at $97.51 and nothing can be bought at any grade.
2. **ABNB RSI2 is in the 70s while the position is 1.03% underwater.** If it prints ≥70 with price **above $169.5209** (+1.05% from here), the gate flips from *optional exit-into-strength* to a **mechanical take-profit** and it executes autonomously, with no magnitude test. Worth watching on any strength tomorrow — that is a materially better exit than Thursday's unconditional one.
3. **DAY TRACK paper day 5 of 10**, 4 signals of 8. Pause conditions clear on both counts. Next graduation review **Monday 2026-09-28** — six more days and four more signals minimum, so no promotion is possible before then regardless of results.
4. **AMD's IV ratio will read artificially cheap tomorrow.** Today's +8.96% gap is not yet inside the trailing realized window; once it closes, AMD's raw ratio drops from **1.1131 to ~1.0122** on *unchanged* implied vol. **Read the ex-gap ratio, not the raw one** — the raw number is an artifact, flagged a day early so the next run inherits the warning rather than the surprise. (IV is the leg held fixed in that projection, so the actual print most likely lands lower.)
5. **Options entries are unpaused but the book stays empty on capital, not on policy.** $97.51 funds no CORE vehicle at any DTE.
6. **Standing, for Ryan, no action needed:** the desk's own options record is **−$141 over 10 closes** after the corrections — below the threshold to act on, i.e. genuinely *unmeasured* rather than *fine*. If it reaches n=20 still negative, the KILL branch fires again and will be correct that time.

---

*Delivery: committing this file to master IS the delivery — `eod-report-notify.yml` fires on any master push touching it. Exactly one run per trading day writes this file; a later run rewrites it only on a MATERIAL event (a fill, an exit, a new flag, a trigger firing), never to refresh closing marks.*
