# Daily report — trading day 2026-09-22 (Tuesday)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-21 report, so this run owned the duty and took it. Quotes stamped 19:15:4x–19:15:5xZ venue time, well past the opening auction.*

**One line:** **Nothing traded in any of the three books today, and only one of those three stand-downs was a judgement.** The DAY TRACK printed its most decisive opening range yet — a 99.6%-body long signal — and **could not afford one share of QQQ**, the track's first capital-blocked signal. The options book stayed empty because $99.62 of deployable cash is a fifth of the CORE low end. The equity book held three underwater swings with no exit condition met and no fundable entry. The thing to watch is **Thursday**: ABNB and UNP hit their 14-day time stops, which is the event that unfreezes ~$2,100 of capital.

---

## 1. DAY TRACK — paper day 5, FIRST CAPITAL-BLOCKED SIGNAL

| | |
|---|---|
| **Phase** | PAPER (day **5 of 10**; **4 signals of 8** — today did not add a signal). Nothing has ever been placed. |
| **Status** | ACTIVE — the 3-consecutive-loss pause expired at the week boundary and Monday's +6.4774R broke the streak. |
| **Today** | **SKIP — `plan_entry` → `action='skip'`, "cannot afford one whole share inside the caps"** |

**The signal was not marginal — it was the cleanest the track has produced:**

| | |
|---|---|
| Opening range | **740.97 – 743.45** (open 740.98, close 743.45) from five clean 1-minute bars, 13:30–13:34:59Z |
| Body | **2.47 of 2.48 points = 99.6% of range.** The doji gate (body < 10%) is nowhere near in play. |
| Direction | **LONG**, unambiguous |
| Late-entry gate | **PASSED** — ceiling 744.69 (OR high + 0.5 × range), spot 743.87 sat 0.82 under it. This skip is capital, not chasing. |
| Stop that would have been | 740.97 (opposite OR edge), 0.3898% |
| ATR14 daily | 9.5586 |
| Size | **0 shares**, `bound_by='cash'` |

**Why it skipped:** deployable was **$96.59** at 13:37Z against a **~$743.87** minimum ticket for one whole QQQ share — short by a factor of **7.7**. No judgement was applied and none was permitted; the spec forbids an unattended run adding or relaxing a gate.

**The finding this produced — `_DAY_TRACK_THE_LONG_SIDE_COSTS_30X_THE_SHORT_SIDE_SO_CAPITAL_FILTERS_THE_PAPER_SAMPLE_BY_DIRECTION_2026-09-22`:**

The long vehicle (QQQ, ~$744) costs **~30×** the short vehicle (PSQ, ~$24.91), and the spec requires **whole shares**. So the minimum ticket is ~$744 to go long and ~$25 to go short. Whenever deployable cash sits between those two numbers, **the track is fundable on one side only — and which side is decided by the swing book's deployment, which has nothing to do with the day-track signal.** A SHORT on today's identical tape would have funded ~3 PSQ and traded.

This is **structural, not bad luck.** The whole-share requirement is load-bearing: a fractional position cannot carry a resting broker stop, and that resting stop is the track's entire risk control while the agent is absent 14 of every 15 minutes. The minimum ticket cannot be lowered without destroying the thing that makes the track safe.

**What it does to the graduation sample:** today incremented **days (5)** but not **signals (4)**. The two-part gate — 10 days AND 8 trades — is now doing exactly the work it exists for: the day count will reach 10 while the signal count lags, which is the honest representation of a track being *prevented* from trading rather than *choosing* not to. Escalated to Ryan; **not fixed by this run**, because the fix is a spec change and only an interactive session with a real Ryan turn may make one.

---

## 2. Positions — equity book (3 swings, all underwater)

Marks at 19:15:4x–19:15:5xZ venue time.

| Name | Shares | Entry | Last | Value | P/L | Held | Time stop |
|---|---|---|---|---|---|---|---|
| **ABNB** | 6.573584 | 169.5209 | 161.170 | $1,059.46 | **−$54.90 (−4.93%)** | 12d | **Thu 2026-09-24** |
| **UNP** | 3.858199 | 285.1071 | 274.160 | $1,057.76 | **−$42.24 (−3.84%)** | 12d | **Thu 2026-09-24** |
| **V** | 2.716801 | 368.0799 | 363.165 | $986.65 | **−$13.35 (−1.34%)** | 1d | Mon 2026-10-05 |
| | | | | **$3,103.88** | **−$110.48 (−3.44%)** | | |

**Why we own each, and where its exit is:**

- **ABNB** — Connors RSI(2) mean-reversion entry, 2026-09-10. Still oversold (RSI2 6.5) and still inside a rising 200-day uptrend; it re-appears on today's own setup board marked HELD. Target 183.08 is **13.6% away**; green-enough (Ryan's native trail trigger) is 199.44. **The live exit is the time stop on Thursday, green or red.**
- **UNP** — same entry date, same signal class. Target 298.32 is **8.8% away**, green-enough 335.42. **Time stop Thursday.**
- **V** — entered yesterday 14:23Z for $1,000.00, the first autonomous equity entry since 09-14. One day old. Target 383.06 (**5.5% away**), green-enough 433.04, time stop 10-05.

**No exit fired today, and the reason is mechanical rather than discretionary.** All three are underwater, so the RSI2≥70 take-profit is **structurally unavailable** — it is gated on `price > entry`, because it is a *profit-banking* authority and may never realize a loss on a technical bounce. No target was hit. No green-enough crossing, so no SET TRAILING STOP alert for Ryan. No thesis flag is open on any of the three. That leaves the 14-day time stop as the only live exit, and it is 2 days out for two of the three.

**Options book: EMPTY.** 0 positions, $0 options value, 0 ledger rows, and `get_option_orders(created_at_gte=2026-09-21)` returns nothing.

---

## 3. Actions taken today

**None, in any book.** No order was placed, filled, or cancelled. `get_equity_orders(created_at_gte=2026-09-22)` is **empty** at every reconciliation this run performed, so no sibling run landed a fill either.

---

## 4. Candidates considered and SKIPPED

Board: the **19:08Z intraday report** (7 minutes old at write time, no `DATA ERROR`). Twelve RSI(2) setups. Membership is **unchanged** from the 18:07Z board the 18:15Z run graded at **zero A-grades**; only the intra-list ranking moved.

| Candidate | RSI2 | Why it was not taken |
|---|---|---|
| CVS | 0.9 | **Capital.** Deepest oversold print on the board, but see the gate below. |
| VZ | 1.1 | Capital. |
| CRM | 3.1 | Capital — and a **−13.5% stop distance**, roughly 4× the rest of the board. |
| KHC | 3.6 | Capital. |
| PNC | 7.1 | Capital. |
| BAC | 8.1 | Capital. |
| **OXY, CVX, COP, EOG, DVN** | 3.4–6.8 | **Excluded on the sector steer** — de-emphasized oil energy, no new entries by default. Reply to override. Note these are **5 of 12** setups, a correlated cluster the report itself flags. |
| **ABNB** | 6.5 | **Already HELD.** A buy here ADDS to an existing position; not an add candidate two days from its own time stop. |

**The actual gate, stated precisely, because "no capital" is the lazy version of it:** deployable is **$99.62** — that is **17% of the $600 minimum entry**. Under the CAPITAL POLICY, when deployable sits below one normal position size the gate is no longer "is this A-grade" but **ROTATION: a new idea must grade BETTER THAN THE WEAKEST POSITION HELD.** Nothing on this board clears that. More to the point, the two weakest-looking positions (ABNB, UNP) **self-liquidate on Thursday** via their time stops, and "weakest" means weakest on the *entry stack*, never simply the biggest loser — **rotating a sound underwater thesis out two days ahead of its own mechanical exit is churn**, and it would pay a spread and a round trip to do it.

**Options: no CORE candidate was worked to a thesis.** $99.62 deployable is **20%** of the $500 CORE low end, so the book is declined **on capital, not on merit** — say it that way round. The IV sweep ran anyway and is complete, 8 of 8.

**IV readings logged today** (`iv_history.json`, one row per name, raw IV/RV ratio):

| SPY | QQQ | NVDA | AMD | TSM | AVGO | MSFT | TSLA |
|---|---|---|---|---|---|---|---|
| 1.2011 | 1.1381 | 0.7657 | 0.9452 | 1.1875 | 0.9767 | 1.1432 | 0.9295 |

---

## 5. Sleeve state

| | |
|---|---|
| **Total account value** | **$3,372.02** |
| Equity value | $3,103.80 |
| Options value | $0.00 |
| Cash | $268.22 |
| `buying_power` | $268.22 |
| **`unleveraged_buying_power`** | **$268.22** — identical, so **no margin is being extended** (FOUR LAWS #4 unambiguous) |
| Operational reserve (5% of total) | **$168.60** |
| **DEPLOYABLE** | **$99.62** |
| Premium at risk (options) | **$0.00** |
| Realized options P/L today | **$0.00** vs the **−$400** cap → full headroom |
| Options entries used | **0 of 3** |
| Equity entries used | **0 of 3** |
| Open equity slots | **3 of the 3–4 target** — the book is at target and ~92% invested |
| Calibration change this week | **None applied.** Monday 09-21's calibration ran; its options KILL branch was **reversed** the same day after the attribution bug was found. No parameter moved today, and today is not a Monday. |

**The book is ~92% invested and that is a correct state, not a breach** — there is no cash floor; it was removed 2026-08-29. Cash is the residual of quality.

---

## 6. Tomorrow's watchpoints

1. **THURSDAY 2026-09-24 is the real event: ABNB and UNP hit day 14 and the TIME STOP fires on both, green or red.** That is ~$2,117 returning to deployable — the first time since 09-11 the book will be able to fund a normal entry, and it will unblock the DAY TRACK's long side at the same time. Wednesday is day 13 for both; no action is due tomorrow.
2. **No price stop exists on any equity position and none will be placed** (HARD RULE 5). The time stop is the book's only mechanical loss discipline.
3. **DAY TRACK**: paper day 6 tomorrow. If the OR prints SHORT it is fundable (~$25/share PSQ) and will trade; if it prints LONG it will skip again on capital until Thursday. That directional filtering is the finding above and it is being recorded, not corrected.
4. **Graduation** is not near: 5 days of 10, 4 signals of 8. Next review is the Monday **2026-09-28** calibration via `day_track.graduate()`. No run promotes the phase mid-week.
5. **Green-enough trail triggers**, none close: ABNB 199.44, UNP 335.42, V 433.04.
6. **Escalated and open for Ryan**: the 30× long/short vehicle asymmetry in the DAY TRACK. It needs a spec decision, which only an interactive session can make.
