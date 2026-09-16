# Daily report — trading day 2026-09-16 (Wednesday, FOMC)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-15 report, so this run owned the duty and took it rather than deferring. Quotes stamped 19:16–19:19Z — well past the opening auction, and ~45 minutes after the Powell press conference began.*

**One line:** The desk made **one** trade today — an autonomous IBKR swing entry at 16:24Z, taken ~95 minutes before the Fed decision — and the day's story since then is that the presser handed the whole tape back and then some. **SPY went from +0.34% at 18:19Z to −0.83% now, a −1.16% leg inside one hour.** All three swing positions are red; nothing fires an exit, by design. The DAY TRACK took paper signal #2 and stopped out at −1.00R for the second day running, both times with the *direction* right. And the RSI(2) board **doubled from 9 names to 19** during the selloff — which this run investigated and declined, for two different reasons that are worth separating.

---

## 1. DAY TRACK — paper day 2 of 10

**Phase: PAPER.** Nothing was placed. Read the gate carefully, because it is easy to misread right now:

- **Lock (a) — prompt v11 stop authority: OPEN (discharged).** Confirmed live 2026-09-15T16:18Z and this run is likewise invoked with v11. Stop reporting this as a blocker.
- **Lock (b) — `day_track.graduate()`: STILL CLOSED, and it has nothing to do with the prompt.** It needs ≥10 paper days and ≥8 signals with positive expectancy. We are at **2 days, 2 signals**. `graduate(2, [−1.0, −1.0])` → `go_live: false — "paper 2d / 2 trades; need 10d and 8 trades"`. Earliest arithmetically possible go-live is a Monday on or after **2026-09-28**, and only the Monday calibration may flip it. **A live prompt stamp is not a graduation.**

### Today's signal

| Field | Value |
|---|---|
| Opening range (QQQ, 09:30–09:35 ET, 1-minute bars) | direction **LONG** (OR close above OR open) |
| Vehicle | QQQ |
| Paper entry | **708.43** |
| Stop (opposite OR edge) | **707.86** — 0.0805% away |
| Size | **1 share** (long-side quantization: a $708 share price against ~$711 deployable rounds to exactly one) |
| R | **$0.57** |
| Exit | **stop reached 13:36Z** — the first full minute after entry printed a low of **707.650**, breaching by 0.21 |
| Result | **−1.00R = −$0.57** |

### Three things today's paper trade taught, and they matter more than the −$0.57

1. **Both paper signals so far were directionally RIGHT and both were stopped out inside two minutes.** Day 1 was short and reversed up; day 2 was long and QQQ traded 710.01 by 14:01Z — roughly +2.8R had the stop not been taken first. That is a **stop-placement** observation, not a strategy verdict at n=2, and the honest read is that the opening-range edge may be too tight to survive the first two minutes of noise. **Do not "fix" this by widening the stop mid-paper** — that is precisely what the 10-day/8-signal sample exists to decide, with numbers, at a Monday calibration.
2. **A concurrent run managed the same paper position and ratcheted a stop that had already been hit**, concluding it was an open +2.44R winner. Every step of that pass was individually correct; its conclusion was wrong because the position was already dead. Root cause is now a durable finding: in paper, `manage()` must be fed **the adverse extreme since the last pass**, never the current price.
3. **A derived-field repair fixed one member of a set and left the other stale**, leaving the row reading with a stop *above* the entry of a long — arithmetically impossible. Repaired 17:20Z. Same shape as the lot-count rule: when a change invalidates a derived set, repair the **whole set** in one pass.

**Running paper tally: 2 signals, 2 losses, −2.00R.**

---

## 2. Positions — all three books

### Equity swing book (3 of the 3–4 target slots filled)

| Name | Entry | Bid now | P/L | Held | Time stop | Target | Trail arms at | Why we own it |
|---|---|---|---|---|---|---|---|---|
| **ABNB** | 169.5209 (09-10) | 166.82 | **−1.59%** / −$17.75 | 6d of 14 | **2026-09-24** | 183.08 | 199.44 | RSI(2) mean-reversion entry inside a rising 200-day uptrend. Thesis intact. |
| **UNP** | 285.1071 (09-10) | 280.65 | **−1.56%** / −$17.20 | 6d of 14 | **2026-09-24** | 298.32 | 335.42 | Same setup; rail with a durable franchise. Thesis intact. |
| **IBKR** | 87.2999 (09-16) | 85.37 | **−2.21%** / −$15.65 | 0d of 14 | **2026-09-30** | 96.14 | 102.71 | Entered today — see §3. Sharp pullback inside an intact intermediate uptrend (20-day above 50-day), analyst mean PT ~$109, August operating metrics strong on every measure. |

**Nothing fires an exit, and that is the policy working, not a gap in it.** All three are **red at the bid**, so the RSI2≥70 take-profit's GREEN precondition is shut — under HARD RULE 5 an RSI2 print on an underwater name is an *optional* exit-into-strength routed to thesis, never a mechanical loss-realization. No target and no trail trigger is within reach. No time stop is due. And **a macro repricing is not a thesis break**: a cross-sectional percentage move, however many names agree with it, cannot license a sale — that is the discretionary price stop HARD RULE 5 exists to forbid.

One genuinely encouraging datapoint, which only shows up if you measure against the *sector* rather than the index: **ABNB is the only name in today's entire screen universe trading at or better than its own sector** (−0.844% vs XLY −0.893%, a ratio of 0.94x). UNP is −0.364pp under XLI. IBKR is the one taking real cohort damage at −1.674pp under XLF.

### Options book — 0 agentic positions

Nothing open on the desk's own account. **0 of 3 CORE slots, 0 of 3 daily entries used, $0.00 realized against the −$400 cap.** TACTICAL is retired.

### Ryan's own positions — ownership gate engaged, no action taken

| Contract | Cost | Mark | DTE | Status |
|---|---|---|---|---|
| SPY 2026-09-17 **731P** | $28.00 | ~$0.09–0.10 | **1** | Ryan's, `placed_agent="user"` |
| SPY 2026-09-17 **770C** | $27.00 | ~$0.12 | **1** | Ryan's; his own sell-to-close limit at 0.50 is working (order `6aaace42`, 0 filled) |

The two legs of the strangle Ryan opened himself on 09-15, 55 seconds apart. **With SPY at 751.14 both wings are ~20 points out of the money with one day left**, and the combined mark is ~$24 against $55 paid. The desk never closes, trims or re-prices these; his 17:13Z limit order is direct evidence he is managing them himself. Notify-once was discharged 09-15 — re-paging him on a position he is actively working would be noise. **Recorded, not actioned.**

---

## 3. Actions taken today, with the reasoning

### The one trade: IBKR, $707.96 → 8.109516 sh @ $87.2999, filled 16:24:37.62Z

Autonomous equity entry under HARD RULE 6, signal-sourced from the 16:07Z committed report. The gate stack, in the order it was cleared:

- **Signal:** RSI2 8.6 on the live print (17.3 on the settled 09-15 close), inside the report's rising-200-day gate.
- **The discriminator that separated it from four financials declined earlier the same day:** USB and RTX failed because their **20-day sits below their 50-day** — the 200-day gate can certify a name that is already rolling over. IBKR's 20-day is **above** its 50-day (92.47 vs 91.92, +0.60%) with spot 5–5.6% under both. That is a sharp pullback inside an intact intermediate uptrend, which is the Connors setup; the others were downtrends wearing an oversold badge.
- **200-day rising, verified monotonically:** 75.26 → 79.72 across 22 sessions, zero down-ticks, spot +9.46% above it.
- **HARD RULE 7 thesis — INTACT-TO-STRENGTHENING:** FactSet average Overweight, mean PT $108.72–109.42 (+24.6% over the fill), Goldman Buy $113, BofA Buy $114. August metrics: DARTs 4.276M +23% YoY, client equity $962.8B +35%, accounts 5.46M +35%. The −7% session on 09-01 was a **UBS downgrade**, i.e. priced sentiment, not broken fundamentals.
- **`[ERN]` clean and *verified*, not assumed:** `get_earnings_calendar(+21d, high_market_cap)` returned 64 events — so not degraded-empty — and IBKR does not appear. Q3 prints mid-October, outside the hold window whose time stop is 09-30.
- **Sizing:** $707.96 = **18.3% of account value**, deliberately under the 30% cap, above the $600 minimum. Review gate returned `order_checks {}` on a $0.02 spread.

**The disagreement, reported rather than smoothed over.** A **concurrent 16:20Z run graded the same name off the same report and DEFERRED it** — not declined, deferred — on the ground that sizing into a binary event 95 minutes before the dot plot was imprudent. The two runs agree on every measured leg and differ only on whether v11's "macro is a sizing input, not a bar" permits a reduced-size entry ahead of the decision. One run judged yes and sized at 18.3%; the other judged no. **The broker-first sibling check cannot see a sibling's *decision*, only its *fills*** — so both runs were correctly following procedure. Preserved in full as `_TWO_CONCURRENT_RUNS_REACHED_OPPOSITE_VERDICTS_ON_ONE_NAME_...` and flagged for Ryan.

**Honest mark: IBKR is −2.21% eight hours later**, and the deferring run's concern is the one the tape has so far validated. That is a *timing* observation on a 14-day hold, not a verdict on the entry — but it should not be buried, and this is the kind of split that deserves Ryan's eye on the policy question, not just the trade.

### The cash hold was dissolved (18:00Z)

The `_cash_hold` placed 09-14 named a checkable trigger (a post-FOMC re-grade). The trigger fired, the re-grade was performed, and the answer was **still no A-grade** — so the hold **dissolved** rather than being renewed. That is the capital policy working exactly as written: a hold that cannot expire is the cash floor sneaking back in. Capital is now in ordinary full deployment, and **nothing today was declined for want of money.**

### No options entry, no spread spec handed to Ryan

No CORE thesis cleared the full stack. Nothing to spec.

---

## 4. Candidates screened and declined — the educational section

This run inherited a board that had **doubled in one hour: 9 names at 18:07Z → 19 names at 19:07Z**, as SPY fell −1.16%. That is a real change in the ungraded delta and it got a full workup rather than a restated decline.

**My first hypothesis was that the board was measuring beta** — that a −1% index leg mechanically admits a crowd of names to an RSI2<10 gate, so 19 "ideas" are really one trade (long the index) wearing 19 tickers. **The desk's own detector refuted it**, and the refutation is the useful part. The prescribed test is to measure a screen name against **its sector ETF**, not the index, because index-relative weakness is what the screen already encodes. Measured at 19:16–19:19Z:

Benchmarks: SPY −0.825% · QQQ −0.430% · **XLF −2.155%** · SMH −0.111% · XLB −1.478% · XLI −0.657% · XLY −0.893% · XLV −0.095%

| New arrival | Day % | vs sector | Verdict |
|---|---|---|---|
| **LRCX** | −1.683% | **−1.573pp** vs SMH (15.2x) | Name-specific de-rating against a *flat* semis complex. Worse than a dip. |
| **C** | −3.485% | −1.330pp vs XLF (1.62x) | Bank cohort de-rating, compounding. |
| **SCHW** | −3.303% | −1.148pp vs XLF (1.53x) | Same. |
| **AMZN** | −1.389% | −0.496pp vs XLY (1.56x) | Underperforming its own sector. |
| **TKR** | −1.124% | −0.467pp vs XLI (1.71x) | Same, and thin. |
| **MS** | −2.463% | −0.308pp vs XLF (1.14x) | Essentially *tracking* a badly-hit sector. |
| **FCX** | −1.658% | **−0.179pp** vs XLB (1.12x) | Tracking its sector — so the oversold print is a materials-sector move, not a name setup. |
| **IWM / DIA** | −1.094% / −1.448% | *(index vehicles)* | No idiosyncratic thesis exists to check. |
| **EPD** | — | — | Excluded: oil-energy steer. |
| **UNP** | −1.021% | −0.364pp vs XLI | Already held. |

**Not one arrival is trading at or above its sector.** So the decline is unanimous — but for **two different reasons**, and citing the wrong one for the wrong name would be exactly the "check that passes for the wrong reason" this desk keeps catching:

- **Sector-divergent de-ratings** (LRCX, C, SCHW, AMZN, TKR): these are *not* beta. They are names being marked down harder than their complex, which under the desk's own detector makes them **worse** candidates, not cheaper ones. My beta hypothesis is refuted here.
- **Sector-trackers and index vehicles** (FCX, MS, IWM, DIA): these *are* beta. There is no name-specific edge to buy — the oversold print belongs to the sector or the index, and this book already carries that exposure.

**The carried-over names got worse, not better:** PNC −4.940% (2.29x XLF), USB −4.878% (2.26x), BAC −3.637% (1.69x), FDX −2.626% (**3.99x** XLI), CVS −2.799% (**29.3x** a flat XLV), AMAT −2.075% (18.8x SMH). The bank/broker de-rating three earlier runs graded down is intact and deepening.

**Two further reasons no entry was taken, stated so they are not mistaken for the primary one:**

1. **Correlation.** IBKR is already held and is the single worst sector-relative name in the book (−1.674pp vs XLF). A second financial at ~$700 would put ~37% of a 4-name account on one macro factor — the factor that repriced violently today. With a 3–4 name target and a 30% per-name cap, correlation is the dominant risk, not selection.
2. **Clock.** It is 15:16 ET. Any entry carries overnight **with no price stop** (HARD RULE 5) into a tape still moving as it was quoted.

**Capital declined nothing.** Deployable **$711.56** clears the $600 minimum, the 4th slot is open, and the equity throttle stood at 1 of 3. **THE BAR declined it** — and a B-grade gets no position, not a small one.

---

## 5. Sleeve state

| | |
|---|---|
| Account value | **$3,799.92** |
| Cash = buying power = **unleveraged** buying power | **$901.56** — identical, so no margin is being extended (FOUR LAWS #4 unambiguous) |
| Equity value / options value | $2,874.36 / $24.00 |
| Operational reserve (5% of total, recomputed) | **$190.00** |
| **Deployable** | **$711.56** |
| Per-name cap (30%) | $1,139.97 |
| Options premium at risk — **agentic** | **$0.00** (0 of 3 CORE slots) |
| Options premium at risk — Ryan's own | $55.00 cost, ~$24.00 mark |
| Realized options P/L today | **$0.00** vs the −$400 cap |
| Entry throttles used | **equities 1 of 3** · options 0 of 3 · day track 1 of 1 (spent) |
| Equity slots | **3 of the 3–4 target** |
| Reconciliation | **ZERO DRIFT, both books, verified at the broker 19:16Z.** 3 equity positions and 2 option legs match the ledger one-for-one. Sibling check clean: the only equity order today is the ledgered IBKR fill; the only option order is Ryan's own. |

**Weekly calibration (week of 2026-09-14):** run and complete, pre-open Monday, broker-sourced. **Verdict both books: NO CHANGE.** No parameter altered, nothing escalated as a band breach. No calibration change was applied this week, so nothing in today's behaviour traces to one.

---

## 6. Tomorrow's watchpoints (Thursday 2026-09-17)

1. **Ryan's SPY strangle expires.** Both wings ~20 points OTM with a combined ~$24 mark against $55 paid. Absent a very large overnight move both expire worthless; his 0.50 sell limit on the 770C is moving *away* from the market, not toward it. **His call entirely** — the desk will not touch it. Expiry is a ledger event to reconcile, not a decision to make.
2. **Whether today's presser leg extends or reverts.** This matters to the desk not as a market call but because the swing book carries **no price stops** by design — a continued leg down is absorbed, not stopped. That is the accepted cost of a policy that refuses to turn normal pullbacks into realized losses.
3. **ABNB and UNP cross day 7 of 14.** Time stop **2026-09-24** for both. Inside 3 days of that date the report begins annotating them, and an RSI2 bounce on a name about to be recycled is better sold *into* than out of.
4. **Whether the bank/broker cohort stabilises.** Seven financials sit on the RSI2 board and the desk holds one of them. A cohort that stops underperforming XLF converts those names from de-ratings into candidates; one that keeps underperforming is a reason to stay at one.
5. **DAY TRACK paper day 3.** New opening range, one trade, PAPER only. Watch whether the "direction right, stopped in two minutes" pattern makes it three for three — that is the observation the Monday calibration will need, and it must be *collected*, not acted on.

---

*Reconciled against the broker, not the ledger. All P/L figures above are broker-sourced or computed from live quotes stamped 19:16–19:19Z. No position was opened, closed or modified by this run.*
