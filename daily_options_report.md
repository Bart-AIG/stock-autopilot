# Daily Report — Monday, 2026-09-14 — **BOTH BOOKS**

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:15 CT / 15:15 ET / 19:15 UTC by the first run at or after the report window — **45 minutes before the bell**. Quotes stamped 19:16Z. Prompt v10.*

Broker-reconciled at 19:16Z: **2 equities, 0 options, zero drift** on quantity *and* average price. `get_equity_orders(2026-09-14)` returns **exactly two orders — both this automation's own exits**, already on master. `get_option_orders` is empty for the day.

> **Headline: the book shrank from four positions to two, both by exits, and the desk placed nothing new across ~30 runs.** MMM hit its 14-day time stop at the open and was sold red on purpose; GD was sold into an overbought bounce one day short of its own time stop. Together they realized **−$52.78**. That is not a bad day — it is the exit machinery doing exactly what it was rewritten to do on 09-02. The harder question, and the one Section 3 is about, is that **the equity book is now BELOW its 3-4 target band with $1,470 of deployable cash and nothing on the board graded above B+.** Ten consecutive runs found the capital and declined on grade alone.

---

## 1. Positions — 2 equity swings, 0 options

| Ticker | Sleeve | Shares | Entry | Last (19:16Z) | Value | P/L $ | P/L % | Held | **Time stop** | Why we own it |
|---|---|---|---|---|---|---|---|---|---|---|
| **ABNB** | swing | 6.573584 | 169.5209 | 169.900 | $1,116.85 | **+$2.49** | +0.22% | 4d/14 | Thu 2026-09-24 | Graded-A RSI2 entry 09-10 inside a rising 200-day. The decisive evidence was analysts marking estimates **up** through the week price fell ~7.7% (consensus PT $179.75 → $183.24, Raymond James upgrade, Baird $175→$200) — a repricing of the market, not the company. |
| **UNP** | swing | 3.858199 | 285.1071 | 284.900 | $1,099.20 | **−$0.80** | −0.07% | 4d/14 | Thu 2026-09-24 | Graded-A entry 09-10. Rail, low-beta, deliberately uncorrelated with the rest of the book. |

**Live RSI(2), Wilder-computed from own daily bars including the 19:16Z print — not taken from the report:** ABNB **39.82**, UNP **37.41**. The mechanical take-profit fires at **≥70**, so neither is close. ABNB is green, so its profit-banking authority is *open* but untriggered; UNP is red, so under the 2026-08-26 correction that authority is structurally unavailable to it regardless of what RSI2 does. Neither is near its target (ABNB $183.08, UNP $298.32). **No exit fired. Both HOLD.**

Options: **empty**, and the book has been **unhedged since you closed the SPY 2026-11-20 700P yourself on 09-11.** Re-establishing a hedge is your call, not the desk's — it was your position.

---

## 2. Actions taken today — two exits, both equity, both autonomous

### 2a. MMM — **TIME STOP**, sold 13:35:45Z at $162.605, realized **−$30.96 (−6.19%)**

Entered 2026-08-31 at $173.3371. `(2026-09-14 − 2026-08-31).days = 14 ≥ SWING_TIME_STOP_DAYS`. It fired **green or red, and went out red** — which is the mechanism working, not failing.

Why this matters more than the dollar figure: HARD RULE 5 forbids price stops entirely, so **the time stop is the only mechanical loss discipline this book has.** Every other exit is gated on being profitable. MMM was underwater on all fourteen of its days, so the RSI2≥70 banking authority was never once available to it. Without the time stop this position would have drifted to the monthly cull.

It was **not** a thesis sell and the report should be honest about that: none of the three written invalidation conditions was met — no guidance cut, no legal charge, analyst targets still above spot, and price still above its 200-day (though the cushion had narrowed from ~6.0% at entry to ~1.1%). **The trade failed, not the company.** A Connors mean-reversion swing that in fourteen days neither reached its $180.83 target nor printed its bounce — it fell 6.2% instead — had its chance. $469 recycled is worth more than $469 parked.

*Process note:* two concurrent runs independently reached this trigger. The second one's broker precheck found the fill already in place and stood down. **One order exists.** That is the 2026-08-28 "broker is the arbiter" rule earning its keep.

### 2b. GD — **discretionary exit-into-strength**, sold 14:17:31Z at $358.0976, realized **−$21.82 (−4.36%)**

Entered 2026-09-01 at $374.4437, held 13 days — **one day short** of its time stop. So, precisely: this was **not** the mechanical time stop, and **not** a take-profit (the position was ~4.4% underwater, so that authority was unavailable). It was the optional exit-into-strength the 14:02Z report flagged: *RSI2 80.9 overbought while underwater, 1 day to the time stop, this bounce is likely the better exit price.*

**You should know that two runs split on this one.** The 14:00Z run evaluated the identical signal, ran the HARD RULE 7 check to a thesis-**intact** verdict, and **declined** — writing down that the report's "this bounce is likely the better exit price" claim is unmeasured. A sibling run took the opposite view seventeen minutes later and sold. Neither broke a rule: HARD RULE 5 makes this exit explicitly **optional**, so both hold and sell were permissible, and the acting run wins by default because a fill is irreversible.

Worth marking the outcome without over-reading it: **GD is $357.005 right now, $1.09 below the exit.** Selling into the bounce was, so far, marginally the better price — and n=1 proves nothing about whether the rule is right.

### The exit taxonomy, because it is a designed feedback loop and not bookkeeping

Since the 09-02 Connors-pure policy went live: **time stop 2** (LLY 09-10, MMM today) · **discretionary exit-into-strength inside the warn window 2** (MDLZ 09-09, GD today) · **RSI2≥70 mechanical take-profit 0** · **thesis sells 0.**

The zero is the number to watch, and it is not coincidence: that authority is gated on `price > entry`, and essentially every position in this cohort has been red, so it has been **structurally unavailable** rather than merely untriggered. Prompt v10 says plainly that a book where the time stop closes nearly everything is not mean-reverting and the entry trigger needs review. **Four of four closes are now time-stop-family.** It is too small a sample to act on — but it is the exact pattern the rule was written to catch, and if it holds through this week's closes it becomes the main thing for Friday's review.

---

## 3. Candidates screened and **skipped** — the whole board, and why

The 19:03Z intraday report (fresh, header clean, no `DATA ERROR`) lists **eleven** RSI(2) setups. All eleven are accounted for — checked against the enumeration rather than assumed, per the 09-10 lesson where a "0 of 26" verdict turned out to be built from a 23-name sample and the remainder held the best setup of the day.

| Name | RSI2 | Grade | Why not |
|---|---|---|---|
| **SLB** | 1.4 | — | **Excluded, oil steer.** Never graded. |
| **WMB** | 7.6 | — | **Excluded, oil steer.** Never graded. |
| **MU** | 8.6 | — | **Excluded, `[ERN 2026-09-30]` inside the hold window.** An **absolute** bar under the concentration policy — at 30% sizing with no price stop, one overnight gap through a print is a 4-5% account hit. |
| **NVDA** | 2.5 | **B+** | Best name on the board and the deepest oversold print. Held under a bounded reopening condition set at 17:35Z after a full HARD RULE 7 check. Re-tested this run: both triggers **negative**. |
| **LRCX** | 5.4 | B− | Same trade as NVDA. −6.7% today. |
| **AMAT** | 8.6 | B | Same trade. −5.9% today. |
| **LITE** | 7.7 | C | Highest beta to the same narrative, −9.0% today. |
| **NBIS** | 9.9 | C | AI-adjacent, extended. Re-appeared on the board after being retired at 18:02Z — a name returning is not a new signal. |
| **BAC** | 3.0 | C | Declined earlier today on an uncalendared IB-fee guidance cut, then on the FOMC sitting inside the hold window for the most rate-exposed sector on the board. |
| **RTX** | 4.1 | B | Printing fresh session lows against a flat index through the afternoon. |
| **FCX** | 7.9 | B | Declines on grade. Its old numeric gate was audited at 18:45Z and found to be drawn around session bars rather than any structural level — so the decline rests on the grade, not on that gate. |

**Six of eleven are one trade.** NVDA/LRCX/AMAT/MU plus AI-adjacent LITE/NBIS are a single semiconductor export-policy de-rating: **SMH −4.18% on the session**, a complex-wide move whose driving catalyst is unresolved and open-ended. That fails the trend-maturity gate on all three legs — the move has run, the catalyst is *not* priced because it is *not settled*, and the tape is not confirming a turn.

The NVDA reopening condition was **re-derived this run, not inherited**: the DATE trigger is the first committed report of **09-15** (tomorrow, not today), and the PRICE trigger is an SMH close below **537.730** (today's session low — a structural level, so a well-formed gate) against **SMH 544.77**, still 7.04 above it. **Neither fires.**

**The one thing to be clear about: nothing was declined for lack of money.** Deployable was $1,470.57 all afternoon, $735/slot to fill the book back to four, every figure comfortably above the $600 minimum. Ten consecutive runs found a fundable, genuinely open slot and declined anyway — because the concentration policy says a **B-grade gets no position, not a small one**, and that fewer positions must mean *more selective*, never merely bigger. Being under-deployed raises the value of a good entry; it does not lower the bar for a bad one.

### Options — no entry, either track

**TACTICAL:** no trigger. The measurable version: SPY spent 18:00–19:16Z inside a **1.22-point range (761.61–762.83, 0.16%)** and QQQ inside 1.75 points, drifting rather than breaking. An empty book is not a trigger. Two things compound it — (a) a scalp opened now carries its hard time stop **overnight into FOMC eve**, and both of its exits sit inside one median overnight gap; (b) the confirmation denominator is already contaminated: SPY's three most recent 5-minute buckets average **120,678 against an 84,558 prevailing rate — 1.43×**, with the step at 19:00Z, a full hour before the bell. All three buckets reconciled **exactly** against their 1-minute sums first, so that is clean data, not a feed hole. *Honest bound: n=3 buckets and the 18:00Z bucket alone exceeds every one of them, so this is a provisional read on today's closing-flow boundary, not a new constant — and it decided nothing, because the absence of a price trigger declines the track on its own.*

**CORE:** no full-stack thesis, and the **FOMC on Wednesday 09-16 sits inside every 21-45 DTE window**. Note the asymmetry deliberately: the FOMC is cited against CORE and **not** against TACTICAL, because a scalp opened today is flat by the 09-15 close and the event falls outside that track's window. Each track screens its own window; borrowing the other track's objection is a category error this desk has made before.

---

## 4. Sleeve state

| | |
|---|---|
| Total account value | **$3,880.65** |
| Cash = buying power = **unleveraged** buying power | **$1,664.60** *(identical — no margin extended, FOUR LAWS #4 unambiguous)* |
| Equity value / options value | $2,216.05 / **$0** |
| Operational reserve (5% of total, recomputed) | $194.03 |
| **Deployable** | **$1,470.57** |
| Open equity slots | **2 of the 3-4 target — below the band floor** |
| Per-name cap (30%) / minimum entry | $1,164.20 / ~$600 |
| Premium at risk — TACTICAL / CORE | $0 / $0 |
| Realized today — equities | **−$52.78** over 2 closing trades (broker-confirmed) |
| Realized today — options | **$0.00** against the −$400 cap — full headroom, gates nothing |
| Throttles used | **0 of 3** equity entries · **0 of 8** options entries |

Exits do not consume entry throttle, which is why two orders were placed today and both throttles read zero.

**Weekly calibration — ran pre-open at 07:35Z (Monday is the week's first trading day). Verdict on both books: NO CHANGE.** Nothing applied, nothing escalated. Equities measure **+18.73 points over breakeven** (n=51, 66.7% hit rate, payoff 1.086, expectancy +$5.01/trade) — a healthy book — but only **4 of 51** closes happened under the current parameters, so the in-regime gate correctly returns REPORT ONLY. MMM's close today makes it 5; the gate needs 20 and stays shut for roughly another month. That is the system refusing to tune a parameter on data that predates it, which is the whole point of the guard.

One fix worth flagging because it was live code gating the risk-off branch: the calibration's blended pull was found to defeat **both** of its own guards — blending equities with options *raises* n and makes the sample-size floor easier to clear, and a single defensive-hedge close (your SPY 700P, −$247) was enough to flip a +18.7-point equity book into a three-parameter tightening. A hedge losing money is the hedge working. Fixed in `calibrate.py`; the books are now scored separately, as v10 requires.

---

## 5. Tomorrow's watchpoints

- **FOMC decision Wednesday 09-16.** Inside every CORE options window and inside a 14-day equity hold. It is the reason the four large-cap financials were declined today and it does not decay until it resolves.
- **Semis reopening condition, DATE leg fires tomorrow** — the first committed report of 09-15 re-opens NVDA/LRCX/AMAT/LITE for a fresh grade. The PRICE leg (SMH close < 537.730) can fire sooner. NVDA at B+ is the closest thing to an entry this book has.
- **ABNB and UNP both time-stop Thursday 2026-09-24.** Ten days out; nothing due before then unless RSI2 crosses 70 on ABNB while it is green, which would be a genuine mechanical exit and the one thing that would justify rewriting this report today.
- **The book is unhedged and 100% long equity beta into an FOMC week.** The desk will not re-establish the SPY put on its own — that was your position and closing it was your call.
- **Exit taxonomy stands at 4 closes, 4 of them time-stop-family, 0 mechanical take-profits.** If Friday's review still reads that way, the entry trigger — not the exit engine — is what needs the look.

---

*No trade was placed in either book this run. Positions verified against the broker, not the ledger; RSI(2) recomputed from own bars, not read from the report; the semis and FCX gates re-derived from this run's own quotes rather than inherited. HARD RULE 9: no flag touched, none claimed, and no approval from you is asserted anywhere in this document.*
