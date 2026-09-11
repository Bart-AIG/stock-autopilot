# Daily Report — Friday, 2026-09-11 — **BOTH BOOKS**

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:15 CT / 15:15 ET / 19:15 UTC by the first run at or after the report window — **45 minutes before the bell**. All quotes stamped 19:16Z. Prompt v10.*

> *Correction pushed 19:30Z: the first version of this header said "1h45m before the bell" and §3 said "the Friday 14:16 ET clock". Both were wrong by exactly one hour — 19:15Z is **3:15 PM ET**, not 2:15 PM ET. The report window is specified in **CT** and the market clock runs in **ET**, so one run has to hold two different UTC offsets at once, and the CT offset got reused for ET. No decision changes: the corrected clock makes the options decline **stronger**, not weaker (see §3).*

Broker-reconciled at 19:15–19:16Z: **4 equities, 0 options, zero drift** on quantity *and* average price. `get_equity_orders(2026-09-11)` is **empty**. `get_option_orders(2026-09-11)` returns **exactly one order — yours**.

> **Headline: you closed the SPY hedge yourself at 15:54Z, and that is the whole story of today.** The desk placed nothing, in either book, across ~30 runs. The options sleeve is now **empty for the first time in weeks** and the account is **100% long equity beta with no offset, going into a weekend.** Your close is also what ended a day-long capital lockout — it freed $502 and took deployable from $21 to $523. Section 2 explains why the desk did *not* buy the put back, which was a deliberate decision and not an oversight.

---

## 1. Positions — 4 equity swings, 0 options

| Ticker | Sleeve | Shares | Entry | Last (19:16Z) | Value | P/L $ | P/L % | Held | **Time stop** | Why we own it |
|---|---|---|---|---|---|---|---|---|---|---|
| **MMM** | swing | 2.884552 | 173.3371 | 164.855 | $475.53 | **−$24.47** | −4.89% | 11d/14 | **Mon 2026-09-14 (3d)** | RSI2 mean-reversion entry 08-31. Thesis intact, no company break — it has simply stalled. |
| **GD** | swing | 1.335314 | 374.4437 | 356.890 | $476.56 | **−$23.44** | −4.69% | 10d/14 | **Tue 2026-09-15 (4d)** | RSI2 entry 09-01, defence complex. Thesis re-confirmed intact 09-09; the de-rate was sector flow, not GD news. |
| **ABNB** | swing | 6.573584 | 169.5209 | 169.670 | $1,115.34 | **+$0.98** | +0.09% | 1d/14 | Thu 2026-09-24 | Graded-A entry 09-10 under the concentration policy. Baird PT $175→$200. |
| **UNP** | swing | 3.858199 | 285.1071 | 284.300 | $1,096.89 | **−$3.11** | −0.28% | 1d/14 | Thu 2026-09-24 | Graded-A entry 09-10. Rail, low-beta, uncorrelated with the rest of the book. |

**Open P/L −$50.04** on $3,214.36 of cost. No position carries a price stop — that is policy (HARD RULE 5), not an oversight. None is near its green-enough trailing trigger: MMM needs $203.93, GD $440.52, ABNB $199.44, UNP $335.42.

**Options: none.** The SPY 2026-11-20 700P is gone (see §2).

### The thing to look at on this table
**Two of the four positions are recycled by the clock inside the next two sessions** — MMM Monday, GD Tuesday — and both will realize a loss of roughly $24 unless they move. That is the time stop working as designed, not a failure: it is the *only* mechanical loss discipline this book has, because policy forbids price stops. It returns ~$952 of capital on its own, which is the single most important fact for next week's sizing.

---

## 2. Actions taken today — the desk placed **nothing**; you closed the hedge

### Your trade (`placed_agent="user"`), 15:54:21Z
**SELL to close SPY 2026-11-20 700P ×1 @ $5.02 limit → filled, $502.00 credit. Realized −$247.00** against a $7.49 entry, ~45 days before its scheduled ~21-DTE review.

Three consequences, all of which change how the desk is allowed to behave:

1. **The book is unhedged.** The Aug–Oct drawdown-watch posture nominally runs to a ~Nov 1 review, and a long index put was one of its four named layers. That layer is now gone by your own hand. The account is four long equity swings and nothing else.
2. **It ended the capital lockout.** Deployable went $21.02 → $523.32. For the first time today the options sleeve cleared the $300 TACTICAL floor, and the rotation gate became fundable one name at a time (it was not, this morning — either weak name was worth less than the $600 minimum entry on its own).
3. **−$247 now sits against the −$400 daily options cap**, leaving $153 of headroom. Counted under the stricter reading: the cap is a *risk* rule ("stop opening new option trades"), not the sizing rule that excludes your manual positions. It gated nothing — both options tracks were declined on their merits first.

### **What the desk deliberately did NOT do: re-establish the hedge**
Buying an index put minutes after you voluntarily closed one at a loss would be the desk **taking the opposite side of your decision, autonomously, in the same session** — and it would be sourced from a *posture* rather than a *setup*. A standing defensive frame is not a signal: it answers no "why NOW", and nothing in the report signalled it. This is the ownership gate read in the direction that is easy to miss — the gate stops the desk selling your position, and the same logic stops the desk immediately undoing your sale. **Re-hedging is your call.** If you want it back on, say so and it goes in the next batch.

### One code fix landed (13:20Z, pre-open)
`calibrate.py` had a real defect in live code: `edge_stats()` divided the win rate by **all** closes but derived the breakeven win rate from only the **decided** ones — two sides of the same comparison on different denominators. A single $0 scratch leg (the long leg of the August legged SPY vertical, bought and sold back at 3.22) was enough to flip the options book from a thin-positive edge into the **KILL branch** — "halve size, pause new entries, escalate." Fixed: the win rate is now computed over wins+losses and scratches are reported separately (`9W/7L/1scratch`).

The economics never moved — net +$90.00 and expectancy +$5.29/trade are identical either way. **Only the statistic changed.** Worth flagging why it survived: the error was *directional*, and it could only ever drag the measured win rate toward risk-off. A defect that only errs toward caution is the hardest kind to catch, because every instance of it looks like prudence.

---

## 3. Considered and SKIPPED — the educational section

### Equities — 13 names on the 19:03Z RSI2 board, **zero graded A**

The board is **dominated by one sector**: 9 of 13 are pharma/healthcare (AMGN 1.2, LLY 0.9, CVS 2.1, BMY 2.4, MRK 2.5, REGN 3.3, PFE 3.7, GILD 3.7, UNH 3.8).

| Candidate(s) | Grade | Why skipped |
|---|---|---|
| AMGN, LLY, CVS, BMY, MRK, REGN, PFE, GILD, UNH | **C** | **A live, unresolved regulatory repricing aimed at these exact companies** — the MFN ultimatum to 17 drugmakers with a 60-day deadline structure and agreements still being signed name by name, plus CMS-finalized 38–79% Medicare discounts effective January 2026 with Keytruda (MRK) and Eliquis (BMY) named as direct price-cap targets. A mean-reversion entry is a bet that the selling was *indiscriminate*. This selling is targeted, policy-driven, and has further scheduled legs. It also fails the trend-maturity gate's tape test: the complex made relative lows on a session SPY spent +0.95% higher. |
| **TGT** | **B** | **New to the board at 19:03Z, so it was graded fresh rather than inherited.** The cleanest non-pharma name and still not A. For it: Oppenheimer maintains Outperform/$180 (+15% vs spot 155.88) and the Beauty Studio launched in 600+ stores today. Against it: UBS named TGT specifically as being on the **wrong** end of the tariff-refund spectrum with the *anniversary* of those benefits as a coming margin headwind; sector sentiment "a mix of apathy, caution, and chagrin"; Canada's retaliatory tariffs name it. And RSI2 8.4 is the **shallowest** reading on the whole board — a dip, not an extreme. |
| SBUX | B/C | Same consumer/rate de-rating complex; no differentiating catalyst. |
| RBRK | B/C | SPEC sleeve, rich valuation (P/FCF 55, negative P/E), mom12-1 only 9.5. |
| JNJ | C | Pharma cluster, above. |
| HAL | — | **Excluded on the sector steer** — oil-related energy, no new entries by default. Dropped off the board at 19:03Z anyway. |

**Why a B-grade got nothing rather than something small:** the concentration policy is explicit that **a B-grade gets no position, not a small one.** At equal capital deployed, 4 × $900 and 8 × $450 have the *same* expectancy and the concentrated book has strictly *more* variance — concentration only pays if the top 3–4 ideas are genuinely better than ideas 5–8. Fewer must mean **more selective**, never merely bigger. Sizing TGT because the cash now happens to permit it is the exact trade that clause exists to prevent.

**The capital picture behind it, stated honestly rather than used as the excuse:** deployable $523.32 is **$76.68 short of the ~$600 minimum entry** at 4 of the 3–4 target, so an ordinary entry was not available regardless. What *was* available is a **rotation** — and this is the arithmetic that matters, because it says which sells were even possible:

| Sell candidate | Position value | + deployable | vs $600 floor |
|---|---|---|---|
| MMM | $475.53 | $998.85 | **funds an entry** |
| GD | $476.56 | $999.88 | **funds an entry** |
| ABNB | $1,115.34 | $1,638.66 | funds an entry |
| UNP | $1,096.89 | $1,620.20 | funds an entry |

This morning MMM and GD were each *below* the floor on their own and therefore rotation-locked; your hedge close broke that lock. So the rotation gate was genuinely open today and was declined **on the grade, not on the cash** — there was no A-grade to compare against the weakest held name. Rotating out of MMM or GD would realize a ~$24 loss and pay a round trip to buy a B-grade, **1–3 sessions before the same capital comes back mechanically via the time stops.** Waiting strictly dominates.

### Options — both tracks declined

**TACTICAL (0 of 2 open, capital cleared the floor for the first time today):**
- **No trigger.** SPY 764.925 sits 2.6335 *under* its 20-day (−0.343%) and QQQ 715.590 sits 0.9375 under (−0.131%) — but both are **standing conditions the index has carried all day, not breaks happening NOW.** QQQ's gap is 0.34× one day of the level's own drift, i.e. smaller than the level moves on its own overnight; a "break" that size is manufactured by the denominator.
- **No index disagreement** to trade against: SPY +0.95%, QQQ +0.97%, XLF +0.69% — a uniformly risk-on tape.
- **The Friday clock bars it independently of any trigger.** A TACTICAL position's hard time stop is the close of the *next* session, so one opened now is held across a weekend — and the measured median Monday gap in SPY (0.342%, vs 0.279% on other days, with a >0.5% gap on 39.6% of Mondays) **exceeds the entire −30% stop distance** on a right-delta contract. Across a close the outcome is decided by the gap and neither exit level is enforceable, because the desk does not run while the market is shut. That is not a bearish view; it is that holding over a weekend replaces the track's risk control with a coin flip of larger magnitude than either exit.
- **And on the corrected clock there is a second, independent bar: at 15:16 ET the run is only ~45 minutes from the bell, i.e. at or inside the closing-auction window where the volume-confirmation denominator stops being readable** — auction and imbalance flow inflates every bar for reasons unrelated to information, so a trigger genuinely cannot be confirmed. Stated carefully, because the desk's own finding forbids the shortcut: **40 minutes is not a constant and must not be treated as one** (it measured 40 minutes on 2026-08-28 and failed to reproduce at 31 minutes on 08-31). The boundary has to be detected per session, and this run did not measure it. What is certain is that the window is close enough that entering a scalp here would mean confirming a trigger against a denominator nobody has verified — which is reason enough to decline, and it is the reason the original 1h45m figure obscured.

**CORE (0 of 3 open):** no candidate answers "why NOW." The report's options candidates are momentum names (LITE, MU, AEHR, AAOI, BE) with no fresh catalyst, and the equity report's mid-caps have been measured repeatedly at 12–50%-of-mid chains — untradeable at this size. Spending the last $523 on a 21–45 DTE single leg two sessions before ~$952 returns mechanically is also poor sequencing.

---

## 4. Sleeve state

| | |
|---|---|
| Total account value | **$3,881.27** |
| Equity value / options value | $3,163.89 / **$0.00** |
| Cash = `unleveraged_buying_power` | **$717.38** — identical, so **no margin is extended** (FOUR LAWS #4 clean) |
| Operational reserve (5% of total) | $194.06 |
| **Deployable** | **$523.32** — $76.68 under the ~$600 minimum entry |
| Per-name cap (30%) | $1,164.38 |
| Equity slots | **4 of the 3–4 target** (hard band 3–5) — fully deployed, a correct state |
| Options premium at risk | **$0** by track (TACTICAL 0/2, CORE 0/3) |
| Realized options P/L today | **−$247.00** vs the −$400 cap → **$153.00 headroom** |
| Realized equities P/L today | $0.00 |
| Entry throttles used | equities **0 of 3**, options **0 of 8** |
| `unsettled_funds` | $501.93 (the hedge proceeds, settling 09-14; `limited_margin` so tradeable now) |

**Calibration:** no parameter changed this week. The 09-08 run pulled 72 broker closes and both books reported healthy — equities margin **+18.3 pts over breakeven** (69.1% actual vs 50.8% breakeven, n=55, expectancy +$4.82/trade, net +$264.89) — but the **in-regime gate blocked any adjustment**, because only 2 of those 55 trades closed under the current parameters and the gate requires 20. That is the guard working: tuning a parameter on trades that predate it is superstition. Next calibration is **Monday 2026-09-14**.

**Friday review** was completed pre-open at 13:20Z, and the `calibrate.py` fix above came out of it.

---

## 5. Tomorrow's watchpoints (next session = Monday 2026-09-14)

1. **MMM time stop fires Monday.** Day 14 of 14. It sells green or red — currently −$24.47 — and returns ~$476. This is mechanical; it is not a judgement call and does not wait for a better price.
2. **GD time stop fires Tuesday 09-15.** Same mechanics, ~$477.
3. **Together those take deployable to roughly $1,475**, re-opening a full-size entry above the $600 minimum and taking the book to 2 of the 3–4 target — i.e. **two open slots** with real capital behind them for the first time since 09-10. That is when the entry bar actually gets tested again.
4. **The `_cash_hold` record expires Monday 2026-09-14** and dissolves automatically. It is not load-bearing now and gated nothing today — capital was the binding constraint, not a deliberate hold.
5. **Weekly calibration runs Monday** (first trading day of the week). Watch whether the in-regime count has moved off 2 — it will not have by much, so expect "report only" again.
6. **The book is unhedged into the weekend.** If you want the put back on, that is a decision for you; the desk will not re-establish it autonomously.
7. **Pharma stays off the entry list** until the policy leg resolves. The desk did *not* verify which specific MFN deadline is next, so that catalyst needs re-checking before any pharma entry — do not quote a date from this report.

---

*No trades were placed by the desk today. No flag was created, cleared, or touched; HARD RULE 9 intact. Committing this file to master IS the delivery.*
