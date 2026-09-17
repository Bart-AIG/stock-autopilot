# Daily report — trading day 2026-09-17 (Thursday, day after FOMC)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-16 report, so this run owned the duty and took it rather than deferring. Quotes stamped 19:15–19:17Z, well past the opening auction.*

**One line:** **The desk placed nothing today, in any of the three books, and for once the reason is almost entirely capital rather than judgment.** Deployable cash is **$369.12** against a **$600** minimum equity entry and a **$500** low-end options size — both live books were shut before any setup was graded. The day's three real events all came from outside the desk's authority or from its own paper track: **Ryan closed his VLO puts himself for −$360**, his **SPY 731P/770C strangle expires worthless at tonight's bell**, and the **DAY TRACK stopped out for the third straight paper day and has paused itself for the rest of the week.** Fifteen RSI(2) candidates were graded across the session; every one was declined on merit as well as on capital.

---

## 1. DAY TRACK — paper day 3 of 10, now PAUSED

| | |
|---|---|
| **Phase** | PAPER (nothing placed, ever, this week) |
| **QQQ opening range 09:30–09:35 ET** | high **716.43** / low **714.06**, open 715.98, close 714.115 |
| **Direction** | **SHORT** — body 78.7% of range, well clear of the 10% doji filter |
| **Vehicle / size** | PSQ, **7 shares** @ 25.965 — cash-bound, $181.75 of a then-$187.47 deployable |
| **Stop** | 25.8905 (the opposite OR edge, translated into PSQ) → **R = $0.52** |
| **Result** | **STOPPED OUT at −1.00R (−$0.52)**, closed 14:27Z |
| **Week** | −1.00R, −1.00R, −1.00R = **−3.00R** |

**The track has paused itself, by its own rule, and it tripped BOTH pause conditions at once** — three consecutive losing days *and* a week at −3.00R. `day_track.track_status()` returns `paused` and the pause expires at the first run of the next trading week, **Monday 2026-09-22**. No run promotes or un-pauses the phase mid-week; `day_track.graduate()` returns `go_live: false — "paper 3d / 3 trades; need 10d and 8 trades"`. **This was escalated to you by push notification earlier today** and is repeated here because the report is the durable copy.

**What three losses actually tell us, stated honestly:** almost nothing about the edge. n=3 is noise, and the more interesting pattern is that **all three signals had the direction RIGHT and were stopped out anyway** — twice inside two minutes of entry. That points at the *stop*, not the *signal*: the opening-range edge on a 0.1–0.3%-wide range is so tight that ordinary first-minute chop reaches it. That is a hypothesis for the Monday calibration to test with numbers, not something for an unattended run to "fix" by adding a filter — and the spec explicitly forbids a mid-week rule change.

**One structural problem worth your attention:** at $369 of deployable cash, **a long QQQ share costs $716, so the long side is literally unbuyable.** All three paper signals so far happen to have been shorts, and the direction was genuinely short on the bars each time — but the paper sample *cannot* contain a long at this account size, which means the ten-day graduation sample will be a shorts-only sample. That is a real defect in the evidence the graduation gate will read. Recorded in `holdings.json._DAY_TRACK_THE_LONG_SIDE_IS_NOW_UNAFFORDABLE_SO_THE_PAPER_SAMPLE_WILL_SELECT_SHORTS_2026-09-17`.

---

## 2. Positions

### Equity swings — 3 of the 3–4 target slots

| Name | Entry | Now (19:16Z) | P/L | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|
| **ABNB** 6.5736 sh | 169.5209 (09-10) | 165.795 | **−$24.48 / −2.20%** | 7d of 14 | **09-24** | RSI(2) mean-reversion entry inside a rising 200-day uptrend. Thesis intact — the early-September softness has a named, non-structural driver (see 09-15 finding), not a thesis break. |
| **UNP** 3.8582 sh | 285.1071 (09-10) | 282.58 | **−$9.75 / −0.89%** | 7d of 14 | **09-24** | Same RSI(2) setup, low-beta rail. Essentially flat; nothing has happened to the thesis. |
| **IBKR** 8.1095 sh | 87.2999 (09-16) | 88.93 | **+$13.22 / +1.87%** | 1d of 14 | **09-30** | Yesterday's autonomous entry, taken ~95 min before the Fed decision on a two-channel thesis. The de-rating channel is the one that paid: IBKR is **+2.53% today** and the only green name in the book. |

**No exit fired on any of the three, on any of the three mechanisms** — and I checked each against a live bid rather than an inherited number:

- **RSI2 ≥ 70 take-profit:** the trigger is a fixed *price* for the session, re-solved this morning. **IBKR needs bid ≥ 90.45** (live 88.93, short by $1.52 / 1.71%); **ABNB needs ≥ 170.08** (live 165.77, short $4.31); **UNP needs ≥ 285.38** (live 282.51, short $2.87). All determinate — spreads are $0.02–$0.13, nowhere near the thresholds.
- **Time stop (14 days):** due 09-24 / 09-24 / 09-30. None due, none inside the 3-day warning window.
- **Green-enough trail:** needs 199.44 / 335.42 / 102.71. Nothing close, so no `SET TRAILING STOP` alert for you today.

### Options — 2 contracts, both yours, both expiring tonight

| Contract | Qty | Basis | Now | Status |
|---|---|---|---|---|
| SPY 2026-09-17 **731P** | 1 | $0.28 | ~$0.00 | Expires worthless tonight — SPY 762.82, the put is **31.82 OTM** |
| SPY 2026-09-17 **770C** | 1 | $0.27 | ~$0.03 | Expires worthless tonight — SPY 762.82, the call is **7.18 OTM** |

Both are `placed_agent: "user"` — your FOMC strangle from 09-15. **The ownership gate means the desk does not close, roll or touch them**, and there is nothing to do operationally: total options book value is **$3**, and assignment would require SPY to rally 0.94% in the last ~40 minutes. The $55 of basis is a realized loss on your side of the book when they lapse.

**Agentic options book: 0 of 3 CORE slots, 0 of 3 entries used.**

---

## 3. Actions taken today

**By the desk: NONE.** No order was sent in any book — no equity entry, no equity exit, no option entry, no option exit, no day-track order (the track is in PAPER and additionally paused).

**By you, in-app — two things, both recorded and reconciled:**

1. **VLO 2026-09-18 390P ×2 CLOSED at 14:55:36Z for $0.75 (credit $150) against a $510 basis → −$360.00 realized.** You cancelled your own $1.30 ask-side limit at 14:44Z and crossed to the bid eleven minutes later. Broker-confirmed twice (`get_option_orders` order `6aabff68`, and `get_realized_pnl` = −$360.00 / 1 closing trade). The ledger row was removed at 15:01Z and the close is in `_closed_positions`.
2. The strangle above decaying from ~$15 to $3 into tonight's expiry.

**Why that matters to the desk even though it was your trade:** those two moves cut **total account value from $4,080.11 at the open to $3,445.25 now, −15.66% in one session, with the equity book flat.** That has a governance consequence you should know about, covered in §5.

**One ledger repair, no trade:** the DAY TRACK's five stored paper rows were missing their canonical flat fields (`r_multiple`, `exit_reason`, `pnl_usd`, `entry`), which meant the pause and graduation gates were only readable by hand — and a machine read of them *un-paused* the track. Repaired additively across both stores and verified to reproduce the identical verdicts. `holdings.json._THE_DAY_TRACKS_TWO_SAFETY_GATES_ARE_FED_BY_HAND_AND_THE_MACHINE_PATH_IS_BROKEN_OR_UNSAFE_2026-09-17`.

---

## 4. Candidates considered and SKIPPED — 15 graded, 0 taken

The RSI(2) board churned all day (6 names at 14:06Z → 9 → 8 → 7 at 19:07Z). Every non-held name that appeared on any board today was graded. **The most important thing to say plainly: these were declined on MERIT first, with capital as a redundant second reason — not the other way round.**

**The financials/consumer cluster (14:20Z, 6 names): BAC, C, MS, CVS, SCHW, DASH — all declined.**
- **50-day discriminator: 0 of 6 passed.** Every one traded below *both* its 20- and its 50-day (BAC −6.89%, MS −6.33%, CVS −8.15%, DASH −4.62%, C −2.67%, SCHW −2.57% under the 50-day). A mean-reversion entry needs a mean to revert *toward*; below both averages the setup is a downtrend, not a dip.
- **Cohort test: all 6 red (mean −0.715%) while SPY was +0.971%** — a 1.69-point gap against a rising tape, with no green exception to work. XLF at −0.34% marks it as **one financials move**, so the six were a single candidate, not six.

**Later additions, each graded when it first appeared:** **PNC** (14:50Z, same financials cohort), **LRCX** grade **C** and **VZ** grade **B** (15:20Z), **BMY** grade **B** (17:20Z). None reached A-grade; under the concentration policy **a B-grade gets no position, not a small one.**

**The rotation gate never needed adjudicating.** Under the capital policy, when deployable cash is below one position size a new idea must grade *better than the weakest position held*. A candidate that fails the entry stack outright cannot clear that bar, so no weakest-name ranking was required on any of the fifteen.

**Options:** no CORE candidate was armed. Even setting thesis aside, **$369 of deployable cash cannot fund the $500–1,000 CORE band** — the book is capital-blocked, not thesis-blocked. **No spread specs handed to you today.**

---

## 5. Sleeve state

| | |
|---|---|
| Total account value | **$3,445.25** (was $4,080.11 at the 13:33Z open — **−15.66%**, ~all of it your options book) |
| Cash = buying power = **unleveraged** buying power | **$541.38** — identical, so **no margin is extended** and FOUR LAWS #4 is unambiguous |
| Equity value / options value | $2,900.87 / **$3.00** |
| Operational reserve (5% of total, recomputed) | **$172.26** |
| **Deployable** | **$369.12** — below the **$600** minimum equity entry AND the **$500** options low end |
| Premium at risk, agentic | **$0.00** (both open contracts are yours) |
| Realized options P/L today vs the −$400 cap | **−$360.00**, **+$40.00 of headroom remaining** — 90% spent, **not hit**, so it gates nothing |
| Realized equity P/L today | $0.00 (no equity order placed all day) |
| Throttles | options **0 of 3**, equities **0 of 3**, day track 1 of 1 (paper, spent) |
| Equity slots | **3 of the 3–4 target** |

**Two governance items you should see, neither of which triggers an action:**

**(a) The −$400 options loss cap has been applied to YOUR loss, strictly, and that is a judgment call the documents do not settle.** The VLO round trip was yours end to end. Whether a user-placed position's realized loss counts against the *desk's* daily cap has never been tested. The tie-breaker is "where either is stricter, the stricter rule applies", so the desk counted it — leaving $40 of headroom instead of the full $400. **This is a question for you, not for an unattended run to resolve the permissive way.** (`_USER_LOSS_AGAINST_THE_DESK_OPTIONS_CAP`.) Worth noting the cap was also carried with its headroom *sign inverted* for 18 minutes this afternoon before being caught and corrected at 16:47Z — wrong in sign, therefore wrong in consequence; fixed, with the mechanism written up.

**(b) Two of three swings are now over the 30% per-name cap, and not one share moved.** ABNB **31.63%**, UNP **31.65%**, IBKR 20.94%. Against this morning's $4,080 denominator the identical positions read 26.69% / 26.66% / 17.61% — comfortably inside. **The crossing is entirely denominator:** the cap is a percentage of *total* account value, which includes the options book, so your VLO loss and the decaying strangle pushed the equity book over a gate it never moved toward. The ruling is **STOP ADDING, NOT SELL** — the cap is a sizing gate, and HARD RULE 5 permits an equity sale only on a fired exit. Today that changes nothing, because the book was already shut on capital. **The sharp edge is worth remembering: the part of that denominator that moves is the part the desk is forbidden to touch.** (`_THE_PER_NAME_CAP_IS_BREACHED_BY_THE_OTHER_BOOKS_LOSSES_2026-09-17`.)

**Weekly calibration (run 2026-09-14, Monday): NO CHANGE to any parameter, nothing escalated.** Broker-sourced, 69 closes. Equities read **66.67% hit rate, payoff 1.086, breakeven 47.94% → +18.73 points of margin, +$5.01/trade expectancy, +$255.68 net** — healthy. It was nonetheless **report-only**, because the in-regime gate blocked it: only **4 of 51** equity closes happened under the current (2026-09-02) exit and sizing parameters, against the 20 required. That sample is rebuilding as designed and the gate stays shut roughly another month. A healthy edge does not loosen anything, by design.

---

## 6. Tomorrow's watchpoints (Friday 2026-09-18)

- **Both SPY legs lapse tonight.** Tomorrow the options book is empty and the desk holds no contracts at all.
- **VLO 390P expires tomorrow** — already closed, so nothing outstanding, but it will show in the expiry ledger.
- **DAY TRACK stays PAUSED all day Friday.** It does not compute or log a signal; the pause lifts at the first run Monday 2026-09-22, which is also the weekly-calibration run that will judge the three-loss sample in numbers.
- **The Friday review is due tomorrow** — hit rate, payoff, margin over breakeven, split by book, plus the drift check.
- **Capital is the binding constraint on everything.** At $369 deployable, nothing is fundable in either live book. It only changes if a position is exited or you add cash — and no exit is currently reachable: the nearest is **IBKR's RSI2 trigger at bid 90.45, 1.71% above spot**, and after that the **09-24 time stops on ABNB and UNP**, which will fire green or red and are the book's only mechanical loss discipline.
- **Two time stops land together on 09-24** (ABNB and UNP, both entered 09-10). That is a single day that recycles two of three slots at once — worth expecting rather than being surprised by.

---

*Sources: `get_accounts`, `get_portfolio`, `get_equity_positions`, `get_option_positions`, `get_equity_orders`, `get_option_orders`, `get_realized_pnl`, `get_equity_quotes`, `get_equity_technical_indicators` on account 718757339, 19:15–19:17Z. Broker reconciliation: ZERO DRIFT in both books — 3 equity positions matching the ledger share-for-share, 2 option contracts matching contract-for-contract. All P&L figures are broker-sourced, never taken from `trade_journal.json`.*
