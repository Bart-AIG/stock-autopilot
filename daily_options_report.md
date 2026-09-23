# Daily report — trading day 2026-09-23 (Wednesday)

*Written by the 19:20Z scheduled run — the first run at or after 2:15 PM CT (19:15Z), which is the v11 threshold. Master carried the 2026-09-22 report, so this run owned the duty and took it. Quotes stamped 19:19:36–19:19:47Z venue time, well past the opening auction.*

**One line:** **The DAY TRACK took its signal and it is working — a paper short sitting at +1.37R on a stop that cannot lose — while both real-money books stood down for the third straight session, and today that stand-down finally became a judgement rather than an excuse.** Capital has been the stated reason since Monday; this session actually graded the board and found **zero A-grades among the four gradable setups**, so the rotation gate failed on the merits too. The thing to watch is **tomorrow**: ABNB and UNP both hit their 14-day time stops, which mechanically releases **~$2,062** and ends the freeze on a date rather than on a decision.

> ⚠️ **This report was written ten minutes before the day track's exit.** The paper row is still open; the 15:30 ET flat rule fires at 19:30Z. That close is a **material** event and is the one sanctioned reason to rewrite this file today — the run that executes it should amend §1 with the final R.

---

## 1. DAY TRACK — paper day 6, signal TAKEN, working at +1.37R

| | |
|---|---|
| **Phase** | **PAPER** (day **6 of 10**; **5 signals of 8** once today's row closes). Nothing has ever been placed at the broker. |
| **Status** | ACTIVE — `track_status(3312.11, [-1,-1,6.4774], [])` → not paused. |
| **Today** | **ENTER → SHORT**, `plan_entry` → `action='enter'` at 13:46Z |

**The signal:**

| | |
|---|---|
| Opening range | **745.085 – 747.12** (open 746.97, close 745.085) from five settled 1-minute bars, 13:30–13:34:59Z |
| Body | **1.885 of 2.035 points = 92.6% of range** — the doji gate (body < 10%) is nowhere near in play |
| Direction | **SHORT** — the range closed exactly on its floor |
| Late-entry gate | **PASSED by 0.36 points**, the narrowest clearance the track has recorded. Floor 744.0675; QQQ printed 744.43. Three minutes later on the same drift this would have skipped as a chase. |
| Vehicle | **PSQ 4 shares @ 24.6212 = $98.48** (paper). Stop 747.12 signal / 24.5322 PSQ, 2.69 pts = 0.3614%. |
| Size binding | `bound_by='cash'` — risk at the stop is **$0.36**, 0.011% of the account against a 5% ceiling. **Cash binds ~450× before RISK_PCT does.** |

**How it has been managed** — 26 passes, every one logged with its inputs:

- **Breakeven armed at 14:18Z/14:20Z** and, for a short, a breakeven stop is **permanent** — it only ever ratchets down. From that moment the row **cannot lose**. This is the first day track signal to reach that state.
- **The 2.0R trail never armed.** It required QQQ ≤ 739.05; the session low was 738.191 but price was never *at* the arm level on a pass. Documented in `_DAY_TRACK_THE_RATCHET_IS_CADENCE_SAMPLED_BY_DESIGN_2026-09-23` — at a 15-minute cadence the ratchet samples the tape, it does not follow it, and that is by design, not a defect.
- **The path was choppy and honest:** 1.978R → 1.454 → 1.208 → 1.186 → 1.346 → 1.364 → 1.398 → 1.242 → **1.368R now**, on QQQ's 740.75 ask at 19:19:47Z. Peak-to-trough give-back of 0.79R without ever threatening the stop.
- **ATR14(5-min) 0.5016**, flat against 0.5049 at the prior pass after four consecutive contractions. The 19:15Z bucket was excluded as provisional.
- **Feed integrity:** the 18:15Z 5-minute bucket remains a known **hole** (−63.4% vs its 1-minute sum) and sits inside the ATR window. Left uncorrected and **labelled**, because `manage()` is ATR-independent below 2.0R — the number it would corrupt gates nothing at 1.37R.

**The exit will be the flat rule, not the trail.** `manage()` returns `close` at 19:30Z regardless of price. Expected result: a **winner of roughly +1.3R to +1.4R on a $98 notional** — i.e. about **$0.49** of paper P&L. That number is the point of the honest-scope note in the row: this is a real trade in **shape** and a trivial one in **size**, and it is a valid sample for direction, stop, timing and the manage ladder — which is exactly what the paper phase measures — and **no evidence at all** about what this strategy does at fundable size.

`graduate(6, [-1,-1,-1,6.4774])` → **`go_live: False`, "paper 6d / 4 trades; need 10d and 8 trades"**. Graduation is a Monday-calibration decision and no run promotes the phase mid-week.

---

## 2. Actions taken today

**None, in either real-money book. No order was placed at the broker in any book today** — `get_equity_orders(created_at_gte=2026-09-23)` is empty and `get_option_positions` is `[]`.

The only executed action of the session was the **day track's paper entry and its 26 management passes**, and one piece of **volunteered research**: a full HARD RULE 7 re-check on ABNB at 17:45Z, described in §4.

---

## 3. Actions considered and SKIPPED — and why this matters more today than yesterday

For three sessions the equity stand-down was reported as *"capital-blocked"* and no candidate was graded at all. **That is a weaker claim than it sounds** — it says the desk could not have acted, not that it should not have. The 18:19Z run graded the board. The answer:

| Name | Grade | Why it does not get a position |
|---|---|---|
| **BAC** | **C** | **Trend cushion EXPIRES inside the hold.** SMA200 55.2704 rising 0.0409/day turns a 1.32% cushion today into **0.28% by the time-stop date**. −8.90%/30d. Also correlated with held V. |
| **BMY** | **C** | −7.10%/30d, a staircase of lower lows rather than a dip. Cushion 2.16% at the stop date. |
| **UNH** | **B** | Cushion 3.03%, −4.40%/30d — but nothing answers **"why NOW"**. **A B-grade gets no position, not a small one.** |
| **JPM** | **B** | Best cushion (4.32% at the stop date) and the shallowest decline, but **disqualified on correlation** with held V and with BAC. Its −3.4% on 09-22 was a sector repricing, not a name-specific dip. |
| ABNB, V | — | **HELD** already. |
| VLO, MPC, PSX | — | **Excluded unread** on the standing de-emphasized-energy steer. |

**Zero A-grades.** So the rotation gate fails twice over: nothing on the board beats the weakest held name (ABNB, thesis *weakened*), and even if something had, rotating today would buy ~18 hours of exposure and spend a slot the day before **two open by themselves**.

The durable finding this produced is worth carrying forward on its own: **project the 200-day average to the time-stop date and test the cushion THERE, not today.** BAC is the worked case — it passes the written trend gate today with a monotonically rising average and zero down-ticks, and the cushion is gone by the exit date. One slope and one multiplication. Recorded as `_THE_ROTATION_GATE_WAS_ANSWERED_ON_THE_MERITS_2026-09-23`.

**Options: no candidate was evaluated and none was owed.** With $102.61 deployable against a $500 CORE low end, the book is closed on arithmetic before judgement is reached. No IV row is owed for a name that was never worked — and per the standing rule, a pre-14:00Z ATM reading would be an upper bound anyway.

---

## 4. Equity positions — three swings, all red, two exiting tomorrow

| Name | Entry | Mark | P/L | Day | % of acct | Day held | Time stop |
|---|---|---|---|---|---|---|---|
| **ABNB** | 169.5209 × 6.573584 | 151.78 | **−$116.62 (−10.47%)** | **−6.20%** | 30.1% | 13/14 | **2026-09-24 → TOMORROW** |
| **UNP** | 285.1071 × 3.858199 | 275.945 | −$35.35 (−3.21%) | **+0.56%** | 32.1% | 13/14 | **2026-09-24 → TOMORROW** |
| **V** | 368.0799 × 2.716801 | 361.435 | −$18.05 (−1.81%) | −0.17% | 29.6% | 2/14 | 2026-10-05 |

**Why we own them, one line each.** **ABNB** — an RSI2 dip inside a +20% cushion over a rising 200-day, bought because analyst price targets were being marked *up* through the week price was marked *down*. **UNP** — the lowest non-held RSI2 print on a 25-name board, with 61 sessions of trend cushion, a Q2 beat-and-raise and a +16.7% consensus gap. **V** — the only non-energy candidate on 09-21 clearing both halves of the strategy with real margin, on a trend cushion that arithmetically cannot expire inside the hold.

**No exit fired today, and the reason is structural rather than discretionary:** all three are **red**, and the RSI2≥70 take-profit is a *profit-banking* authority gated on `price > entry` — it cannot fire on a loser by construction (the 2026-08-26 correction). HARD RULE 5 forbids a price stop. So the only live mechanism is the time stop, and it fires tomorrow on two of the three.

**ABNB's thesis was re-researched at 17:45Z and the verdict is WEAKENED, NOT BROKEN** — so no autonomous thesis sell. The −6.2% session is **sector-wide**: ABNB and TRIP both fell >4% and EXPE as much as 6% the same day, on agentic-commerce disintermediation fears (Meta's Muse moving into travel search and booking). There is **no guidance cut, no downgrade, no regulatory action, no company event.** RBC reiterated **Outperform with a $195 target** on 09-21, naming that exact AI-agent risk and judging ABNB *"somewhat better protected than many other online marketplaces"*. Company news in the window is neutral-to-positive (Instacart grocery rollout 09-22; a $250M housing initiative 09-15). The two insider sales pre-date the de-rating and are routine Form 4s.

**Why that research was done even though it changes nothing today, and why it is not written back as `thesis_checked: intact`:** the time stop closes the position tomorrow whatever the verdict, so intact and broken differ here by **one session of exposure**. It was done because the *reverse* case is the dangerous one — a run that let a −6% day stand as an implicit thesis break would have sold on the technical alone, which the rules forbid. And a *weakened* finding must never be recorded as an *intact* suppression verdict.

**The read that tomorrow's run should inherit:** this is a **narrative / multiple de-rating on a structural question the market cannot resolve quickly**, not a fundamental break. That distinction keeps it out of the thesis-sell path — but it is also the reason ABNB **should not be re-graded as a fresh RSI2 entry** tomorrow merely because it prints RSI2 1.6. A mean-reversion setup assumes the move is noise; here the driver is a re-rating of the business model, so the oversold print is precisely what a de-rating looks like from inside it. **Re-grade from scratch on post-event numbers, or skip — never carry the pre-event grade forward.**

---

## 5. Sleeve state

| | |
|---|---|
| **Total account value** | **$3,312.11** |
| Cash = `buying_power` = **`unleveraged_buying_power`** | **$268.22** — identical, so **no margin is extended** and FOUR LAWS #4 is unambiguous |
| Equity value | $3,043.89 (three swings) |
| Options value | **$0.00** — book empty, zero rows |
| Operational reserve (5% of total, recomputed) | **$165.61** |
| **Deployable** | **$102.61** — 17% of the $600 minimum equity entry, 20% of the $500 CORE options low end |
| Realized options P/L today | **$0.00** across 0 closing option trades, vs the **−$400** cap → full headroom |
| Options entries used | **0 of 3** |
| Equity entries used | **0 of 3** |
| Equity slots | **3 of the 3–4 target filled** — inside band, ~92% deployed |
| Day track | 1 of 1 trade for the day, spent (paper) |

Both counters are **broker-measured, not defaulted**: `get_realized_pnl(options, 09-23..09-23)` returns 0 trades / $0, corroborated by an empty `get_equity_orders` and an empty `get_option_positions`. **Reconciliation against the broker showed ZERO DRIFT in both books** — all three equity positions match the ledger to six decimals and are fully sellable, no shares held for anything.

**This is a correct state under the capital policy, not a breach.** There is no cash floor. Cash is the residual of quality: three A-grade positions are funded, the book is ~92% deployed, and the live gate is **rotation**, not sizing.

---

## 6. Tomorrow's watchpoints

1. **THE TIME STOPS FIRE — this is the whole story.** ABNB and UNP both entered 2026-09-10, so day 14 is **2026-09-24**. Both are sold **green or red**, on their own `TIME STOP / SELL (stalled)` alert line, and neither should be re-litigated as a thesis sell. At today's marks that releases **~$2,062** and leaves the book holding **V alone**, with **2–3 free slots** and roughly **$2,220 deployable** against a ~$166 reserve. **The rotation gate does not relax — it goes dormant**, because cash will cover a full position outright with no sell side at all.
2. **Do not let the freeze framing distort tomorrow's grading in either direction.** It made marginal candidates look like a last chance this week; tomorrow it will make full-size funding feel like an obligation. Neither is true. The minimum entry is ~$600, the per-name cap is 30% of account value, and **a B-grade still gets no position.**
3. **ABNB specifically: re-grade from scratch or skip.** See §4 — the oversold print is the de-rating, not noise.
4. **Day track:** paper day 7 of 10, signals 5 of 8 after tonight's close. Two more clean signals and four more sessions to a graduation decision, which only the Monday calibration may make. The long/short capital asymmetry remains escalated and **unfixed** — at ~$100 deployable a short signal funds four PSQ shares and a long signal cannot buy one QQQ share. Fixing it means editing the spec, and no unattended run may.
5. **Options:** the book becomes fundable tomorrow for the first time in a week. That is permission to *hunt*, not a reason to *own* — a newly affordable vehicle supplies no thesis.

---

*Filed by the 19:20Z scheduled run, prompt v11. No live user turn occurred in this session; nothing here claims or implies Ryan's approval of anything.*
