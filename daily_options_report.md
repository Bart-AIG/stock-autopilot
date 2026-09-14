# Daily Report — Monday, 2026-09-14 — **BOTH BOOKS**

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written by the 19:15Z run — the first at or after the 14:15 CT report window. 14:15 CT = **15:15 ET**, so this lands ~40 minutes before the bell. All quotes venue-stamped 19:19–19:20Z, settled, far past the opening auction. Prompt v10.*

Broker-reconciled at 19:19–19:20Z: **2 equities, 0 options, zero drift** on quantity *and* average price. `get_equity_orders(2026-09-14)` returns exactly two orders — both this desk's own exits, already on master. `get_option_orders(2026-09-14)` is **empty**.

> **Headline: the book halved today, and both closures were exits rather than decisions to raise cash.** MMM hit its 14-day time stop and was sold mechanically at 13:35Z. GD was sold at 14:17Z on an optional exit-into-strength — a call a concurrent run had *declined* seventeen minutes earlier, which is worth reading in §2 because it is the first time two scheduled runs have split on a discretionary exit. Realized **−$52.78** across the two. The desk then declined every one of the day's 15 RSI2 candidates on **grade**, with $1,470 fundable and the book **below its target band**. That combination — capital available, a genuine open slot, and still no trade — is the whole story of the afternoon, and §3 is where it is argued.

---

## 1. Positions — 2 equity swings, 0 options

| Ticker | Sleeve | Shares | Entry | Last (19:19Z) | Value | P/L $ | P/L % | Held | **Time stop** | Why we own it |
|---|---|---|---|---|---|---|---|---|---|---|
| **ABNB** | swing | 6.573584 | 169.5209 | 169.860 | $1,116.59 | **+$2.23** | +0.20% | 4d/14 | Thu **2026-09-24** | Graded-A RSI2 entry 09-10 inside a monotonically rising 200-day (+20.7% above it). Baird PT $175→$200. |
| **UNP** | swing | 3.858199 | 285.1071 | 285.015 | $1,099.55 | **−$0.36** | −0.03% | 4d/14 | Thu **2026-09-24** | Graded-A entry 09-10. Rail — low-beta and genuinely uncorrelated with the rest of the book, which is why it survived a day that hit semis for −4%. |

**Open P/L +$1.87** on $2,214.60 of cost. Broker `equity_value` $2,216.92.

**No position carries a price stop. That is policy (HARD RULE 5), not an oversight.** The three exits this book has are the RSI2≥70 cross while green, the 14-day time stop, and Ryan's native 15% trail once a name is green enough. Neither name is close to a trail trigger: ABNB needs **$199.44**, UNP needs **$335.42**.

**Mechanical exits checked independently of the report, not taken on trust.** Wilder RSI2 computed from own daily bars including the live print: **ABNB 39.35**, **UNP 40.70** — both nowhere near the 70 cross. (ABNB's settled 09-11 reading was 43.68, UNP's 17.51; UNP's jump to 40.70 is today's +0.22% bounce off a 2-period base, not a signal.) Neither time stop fires for another ten days.

**Options: none.** The sleeve has been empty since you closed the SPY 2026-11-20 700P yourself on 09-11. **The account remains 100% long equity beta with no offset going into the FOMC decision on Wednesday** — stated plainly because it is the single largest uncovered risk in the book, and §5 explains why the desk did not buy a hedge back today.

---

## 2. Actions taken today — two exits, no entries

### 2a. MMM — SELL / TIME STOP (stalled), 13:35:45Z, 2.884552 sh @ $162.605, realized **−$30.96 (−6.19%)**

Entered 2026-08-31 at $173.3371. `(2026-09-14 − 2026-08-31).days = 14 ≥ SWING_TIME_STOP_DAYS`. **It fired on the calendar, not on the price, and it went out red — which is the mechanism working, not failing.** Because HARD RULE 5 forbids price stops, the time stop is the *only* mechanical loss discipline this book has, and it is deliberately the one exit that cannot collapse onto the entry price the way both price-based exits do. MMM had neither hit its target nor printed its bounce in 14 days; that is the definition of stalled.

This is the **third** time-stop firing since the policy went live 09-02 (PNC 09-03, LLY 09-10, MMM today). No thesis break was alleged and none was needed — a time stop does not ask whether the company is fine, it asks whether the *trade* is working.

Priced honestly, not favourably: the 13:31Z quotes carried venue timestamps *inside* the opening auction window, so the exit was priced off a re-quote whose venue stamp was at/after 13:35Z.

### 2b. GD — SELL / EXIT-INTO-STRENGTH (underwater, **optional**), 14:17:31Z, 1.335314 sh @ $358.0976, realized **−$21.82 (−4.36%)**

Entered 2026-09-01 at $374.4437. Held 13 days — **one day short of the time stop**, which was due Tuesday 09-15. So this was *not* the mechanical time stop, and it was *not* the RSI2 take-profit either: that authority is gated on `price > entry`, and GD was ~4.4% underwater, so the profit-banking power was structurally unavailable. It was the report's optional `EXIT-INTO-STRENGTH` line, taken into the strongest RSI2 print of the whole 13-day hold (report 80.9; independently computed 75.28 at the fill price).

**The part you should know about, because it is a first for this system:** a concurrent run had evaluated the *same* signal seventeen minutes earlier and **declined** it, on a HARD RULE 7 thesis verdict of **INTACT — and strongly so**: FactSet mean PT $424.50 against a $357 spot, mean rating Overweight, **four consecutive upward PT revisions with not one cut**, plus $184.3M and $194.1M of fresh contract awards and the 08-31 multiyear DoD framework to triple PAC-3 and quadruple THAAD capacity.

Two scheduled runs, opposite conclusions, 17 minutes apart, and the position is gone.

**Neither run broke a rule, and I am not going to pretend otherwise.** HARD RULE 5 makes an underwater RSI2 bounce an *optional* exit routed to thesis — optional means both hold and sell were inside policy. The selling run took the same class of exit this book took on MDLZ on 09-09. The declining run's argument was the better-evidenced one. What the day exposed is structural: the existing collision rule covers two runs that **agree** and both act (the duplicate-entry hazard). It has nothing to say about two runs that **disagree**, where the one that acts simply wins, because acting is irreversible and declining is not. Recorded in `holdings.json._CONCURRENT_RUNS_SPLIT_ON_A_DISCRETIONARY_EXIT_AND_THE_ACTING_RUN_WINS_BY_DEFAULT_2026-09-14`.

**Net for the day: −$52.78 realized over 2 closing trades, broker-confirmed** (`get_realized_pnl` equity, 09-14..09-14). Both were exits. **Zero entries in either book.**

---

## 3. Candidates screened and SKIPPED — 15 names, zero A-grades

This is the section worth reading, because the honest summary of today is *"capital was available, the book was under-target, and nothing was good enough."*

**The screen was not 15 opportunities. It was about four.** The 19:03Z board carries 11 RSI2 setups; earlier boards carried 15 distinct names across the session. Six of them are **one trade** (the AI/semis complex), four more are **one trade** (the bank cohort), and two are excluded outright by your sector steer. A screen that fills with one de-rating is *measuring the de-rating*, not finding N independent setups.

### The AI/semis cluster — NVDA, LRCX, AMAT, LITE, NBIS, MU

| Name | Grade | The specific reason |
|---|---|---|
| **NVDA** | **B+** | Deepest oversold on the board (RSI2 2.5) and BofA's PO $350 vs $212 spot. Against it: it is the *least* dislocated name in the complex (−2.7% vs LRCX −7.6%), so there is the least reversion to capture — and it is the most-owned semi in America (82% of active managers), i.e. the most exposed if the sentiment unwind has legs. Close to A. Not A. |
| **AMAT** | **B** | Weakest oversold print of the group. UBS Buy PT $695 vs $428. No name-specific negative found — but BofA's note today explicitly buckets chip-equipment as names that "could recover **later**", i.e. the bull case itself does not say buy it now. |
| **LRCX** | **B−** | Biggest dislocation and the best PT support on paper (Berenberg $420). Outweighed by **three insider sales totalling ~$30.0M in the two weeks before the drop** — CEO Archer $9.58M and Director Mayer $3.01M on 09-09, SVP Varadarajan $17.41M on 09-02 (SEC Form 4s). |
| **LITE / NBIS** | **C** | Highest beta to the narrative (LITE −9.0% today). No verified analyst support. |
| **MU** | **EXCLUDED** | `[ERN 2026-09-30]` inside the hold window. Under the concentration policy that flag is an **absolute bar** — at 30% sizing with no price stop, one overnight gap through a print is a ~4–5% account hit. Verified against the earnings calendar, not taken from the report's column. |

**A correction the desk made about itself today, which changed no decision but cleaned up the reasoning.** Four consecutive runs had declined this cluster on two stated grounds — *"the chip-export/memory catalyst is unresolved"* and *"the de-rating is still deepening."* Both were checked today and **both are wrong**. The driver is not export policy at all: it is an **AI-governance sentiment shock** (a weekend essay from Anthropic's CEO urging the industry to slow frontier capability gains, backed publicly by OpenAI's Altman, DeepMind's Hassabis and Musk), and the tell is that the bid rotated straight into **cybersecurity** — CRWD/PANW/NOW all ~+5%. That is a sentiment rotation signature, not an export-control one. And the names were *basing* through the afternoon, not deepening.

Withdrawing two false objections does not create a thesis. The cluster is still declined — but now on **grade**, which is an honest reason, rather than on two facts that weren't true.

### The bank cohort — BAC, C, MS, GS: all **C**

**Four banks entered the RSI2 board in a single one-hour report refresh**, and one event made all four: BAC's CEO publicly guided Q3 investment-banking fees to $1.6–1.8B, **down at least 10% year over year**, and characterised the *industry* as ~10% lower. That is an intra-quarter guidance disclosure — **no earnings calendar carries it**, so the screen is structurally blind to it and simply reported four fresh oversold prints. Four names arriving together is not four opportunities; it is one unexplained fact, and once explained it is a fundamental downgrade rather than a technical dip. The FOMC decision Wednesday is an independent second bar on the most rate-sensitive cluster on the board.

### The rest

- **SLB, WMB — EXCLUDED on your standing sector steer** (oilfield services; WMB gas midstream, treated as de-emphasized-adjacent). Not graded, per the steer.
- **RTX — B.** Broke the very session low its earlier B-grade was reasoned from.
- **FCX — B**, and its reopening gate was retired today as badly constructed: the 68.535 level was the **midpoint of a range the desk drew around its own session bars** — 6.90% below the 20-day SMA and 1.70% above the 50-day, so a proxy for nothing. The standing rule against exactly this object had been written for options triggers and never carried across to the equity book. It has been now.

**The verdict, stated as a policy question rather than a mood:** the concentration policy says a **B-grade gets no position, not a small one**, and that *fewer must mean more selective, never merely bigger*. Being below the target band raises the **value** of a good entry; it does not lower the **bar** for a bad one. Capital was fundable twice over — $1,470.52 deployable, $735/slot to reach four, a $1,164 per-name cap, everything clearing the $600 minimum. **Declined on grade.** 0 of 3 equity entries used.

**Spread specs handed to you today: none.** No CORE options thesis cleared, so there was nothing to spec.

---

## 4. Sleeve state

| | |
|---|---|
| **Total account value** | $3,881.52 |
| **Cash = buying power = unleveraged BP** | **$1,664.60** — identical, so no margin is being extended and FOUR LAWS #4 is unambiguous |
| Equity value / options value | $2,216.92 / **$0** |
| Operational reserve (5% of total, recomputed) | $194.08 |
| **Deployable** | **$1,470.52** |
| Options premium at risk — TACTICAL / CORE / hedge | **$0 / $0 / $0** |
| Realized today — options | **$0.00** against the −$400 cap; full headroom, gates nothing |
| Realized today — equities | **−$52.78** over 2 closing trades (MMM −$30.96, GD −$21.82) |
| Entry throttles | Options **0 of 8**; equities **0 of 3**. Today's two orders were *exits*, and exits are never throttled |
| Open equity slots | **2 of the 3–4 target — below the hard band floor of 3**, so the open slot is a genuine hole, not an optional fourth |
| Options positions | 0 of 5 (0 TACTICAL / 0 CORE) |

**The `_cash_hold` on the books is properly formed and I am going to be honest about how much work it is doing.** It names a real dated catalyst (**FOMC decision Wed 2026-09-16, 14:00 ET**, an SEP/dot-plot meeting with CME FedWatch pricing a 25bp **hike** at ~85.6%), a checkable trigger, and an expiry of **2026-09-17**. That satisfies the capital policy's three requirements. But the entries were declined on **grade** independently — so the hold is not what kept the money in cash today, and it should not be credited with a discipline that grade actually supplied. Its original justification text was refuted by this same session three hours after it was written and was repaired in place at 19:00Z rather than left standing.

**No options hedge was re-opened, and that was a decision rather than an omission.** Buying index puts into an 85%-priced hike, two days ahead of the event, is paying event premium for the leg the market has already discounted — the asymmetric surprise Wednesday is a *hold* or the dot plot, neither of which a put is well-positioned for. The honest cost of that choice is stated at the top of §1: the book is unhedged long beta into a binary.

---

## 5. Weekly calibration — ran this morning, **NO CHANGE to either book**

Pulled from the **broker** (`get_pnl_trade_history`, span 3month, 69 closes), never from the journal, and split per book because blending hides which one is working.

| Book | n | Hit rate | Payoff | Breakeven WR | **Margin** | Expectancy | Verdict |
|---|---|---|---|---|---|---|---|
| **Equities** | 51 | 66.67% | 1.086 | 47.94% | **+18.73 pts** | +$5.01/trade | **Report only** |
| **Options** (directional, hedge stripped) | 17 | 56.25% | 0.877 | 53.29% | **+2.96 pts** | +$5.29/trade | **Report only** |
| Options (as bucketed, hedge included) | 18 | 52.94% | 0.743 | 57.38% | −4.44 pts | −$8.72/trade | Report only |

Both books are blocked from adjustment, for **different** reasons, and the difference matters:

- **Equities** are healthy on the headline (+18.7 pts of margin over breakeven) but only **4 of 51 closes happened under the current parameters** — the Connors-pure exits and concentration sizing only went live 09-02. The **in-regime gate** blocked any tuning, exactly as designed. Tuning a parameter on trades that predate it is superstition, and it is indistinguishable from real calibration unless you count. The in-regime sample is rebuilding: 4 today, 6 by week's end with MMM and GD now closed. It needs 20. **Roughly another month before that gate opens.**
- **Options** are blocked on sample size alone — n=17 < 20.

**The demonstration this week stopped being rhetorical.** The blended 69-trade sample reads +1.90 pts, which crosses out of STABLE into **DEGRADED** and would have **changed three equity parameters** — on a book whose own per-book reading is +18.7 and thriving. Last week the same blend read +6.6 and merely "looked healthy." A defensive guard was added to `calibrate.py` at the call site; every per-book verdict is byte-identical.

---

## 6. Tomorrow's watchpoints

- **FOMC, Wed 09-16 14:00 ET** — SEP/dot-plot meeting. 25bp hike ~85.6% priced; **the asymmetric surprise is a hold or the dots, not the hike**. Both open equity swings have time stops on 09-24, so **both span it squarely**. Any new equity entry spans it too. A TACTICAL option scalp would not — don't let that objection get borrowed across tracks.
- **The AI/semis deferral EXPIRES at the first committed report of the 09-15 session.** Re-grade NVDA / LRCX / AMAT / LITE / NBIS **from scratch on post-shock numbers** — do not carry today's grade forward and do not reuse the pre-shock one. Hard price gate attached: **if SMH closes below today's session low of 537.730** the de-rating has resumed and the cluster stays excluded regardless of RSI2 (SMH closed the day around 544.65, above it). If it holds, they compete on grade like anything else. **This is not a queue — they re-enter the funnel, not the book.**
- **No time stop is due tomorrow.** GD's 09-15 stop was pre-empted by today's exit; ABNB and UNP are both 09-24.
- **No earnings for any held name** through its time stop, verified against the 6-day high-market-cap calendar — which returned rows rather than degrading, so the absence is corroborated rather than assumed.
- **The book is 2 of 3–4 and unhedged.** Both are real, both are stated, and neither is a reason to lower the entry bar.

---

*Broker is the ledger of record for every P&L figure here. Reasoning lives in `trade_journal.json`; the durable findings behind §2 and §3 are named in `holdings.json` rather than re-argued.*
