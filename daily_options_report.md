# Daily report — Friday 2026-09-04 (pre-holiday; next session TUESDAY 09-08)

*Written 19:20Z / 2:20 PM CT, 40 minutes before the bell, by the first run at or after the 14:15 CT window. Covers BOTH books.*

**Headline: no trades today, in either book, on the 29th consecutive market-hours run.** Capital was open all day ($1,266.69 deployable, both throttles unused) and the equity entry licence was live from 14:10Z. Nothing was bought because nothing graded A. That is the correct output under the full-deployment policy, not a failure of it — but it is now four sessions since the last fill, so section 3 is written to show you exactly what was turned down and why, and section 5 flags the one question only you can settle.

---

## 1. Positions

**Equity book — 4 swings, all held, all red.** Marks at 19:19Z.

| Name | Entry | Mark | P/L | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|
| LLY | 1189.7553 | 1141.745 | **−$20.17 / −4.04%** | 8d | **09-10** | RSI(2) oversold inside a rising 200-day; pharma megacap, thesis re-checked intact |
| MDLZ | 62.5899 | 61.4503 | **−$9.14 / −1.82%** | 7d | **09-11** | Connors mean-reversion in defensive staples; thesis intact |
| MMM | 173.3371 | 168.350 | **−$14.39 / −2.88%** | 4d | **09-14** | RSI(2) dip in an industrial uptrend; still above its 200-day with >200 sessions of cushion |
| GD | 374.4437 | 358.465 | **−$21.34 / −4.27%** | 3d | **09-15** | Defense prime, oversold; full HARD RULE 7 re-check at 15:05Z came back **intact, arguably strengthening** |

**Book total: $1,934.92 on $1,999.96 cost = −$65.04 / −3.25%.**

Every one of these is red, which matters mechanically: **the RSI(2)≥70 take-profit is gated on `price > entry`, so it is structurally unavailable on all four** — it cannot fire no matter what RSI does. That leaves the 14-day time stop as the only mechanical exit in play, and the nearest is LLY on **09-10** (it enters the 3-day warning window on **09-07**). Neither is due today.

**Options book — 1 position, your hedge.**

| Contract | Entry | Mark | P/L | DTE |
|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | $749.00 | $455.50 | **−$293.50 / −39.2%** | 77 |

This is the authorized defensive hedge and it is **exempt from every premium backstop** — it is insurance, expected to bleed in a market that keeps grinding up, and it is held to its ~21-DTE roll/close decision **with you**, not by the desk. At 77 DTE that decision is roughly five weeks out. No action.

---

## 2. Actions taken today

**None.** No order was placed or cancelled in either book. Both `get_equity_orders` and `get_option_orders` return empty for 09-04, confirmed on every run. Realized P/L for the trading day: **$0.00 options, $0.00 equities.**

---

## 3. Candidates considered and skipped — the educational section

Seven names were graded today across four report refreshes. The report table changed **four times** (14:02Z morning → 15:01Z intraday → 16:48Z morning → 19:02Z intraday), and names entered and left it, so this is not one screen re-read 29 times.

**PM (Philip Morris) — graded A−, and the closest thing to a trade all day.** Its thesis is *verifiably intact*: Q2 beat with an FY26 guidance raise, FDA authorization for ZYN ULTRA, consensus overweight, mean price target 207.46 (+12.5%). It is a textbook Connors setup. It was still declined, and the reason is worth understanding because it is the new concentration policy actually biting: **the book is full at 4 of the 3–4 target, so a fifth entry takes the whole $1,155 per-name cap and becomes the largest position this account has ever held.** The policy reserves that for A/A+ only — *"a B-grade gets no position, not a small one."* Under the old $400–500 sizing PM would probably have been bought. Under 30%-of-account sizing, A− is not enough. That is the trade-off you chose on 09-02, working as intended.

**PATH (UiPath) — vetoed, and it exposed a real hole in the screen.** It printed RSI(2) 5.5 and closed today **−16%**. That oversold reading is not a dip — it *is* Wednesday night's earnings gap. Revenue beat and FY27 guidance was raised, and the stock fell anyway; Canaccord cut it Buy→Hold. The report's Earnings column was **blank**, because the `[ERN]` flag only looks *forward* and the print had already happened. A durable finding was recorded this morning to add a look-back leg to that check. (It is also on your 08-05 joint de-risk sell list.)

**LIN (Linde) — vetoed on trend structure, and it produced the day's sharpest measurement.** It nominally cleared "above a rising 200-day" by +0.26% — but that average is rising only because *old low closes are rolling out of the window*, and at its current slope it would cross **above** LIN's price in **4 sessions**, inside a 14-session hold. The uptrend gate would have expired before the trade did. The desk then tested that detector against all four held names — LLY 120 sessions of cushion, MMM >200, MDLZ 53, GD 40 — confirming it is specific to LIN and not a general defect.

**KMI (Kinder Morgan) — excluded on your sector steer** (nat-gas midstream; outside the enumerated E&P/services/refiner/major list but inside its intent), and independently sub-A: RSI(2) 9.7 barely inside the gate, absent from the momentum top decile, whole objective +4.8%. **Reply to override.**

**LLY / MMM / GD — excluded as already held.** A "buy" on a held name is an *add*, and FOUR LAWS #3 bars adding to a losing position without your approval; HARD RULE 9 bars an unattended run from supplying that approval on your behalf. CL surfaced late in the 19:02Z table and does not clear the A/A+ bar a full book demands.

**Options, TACTICAL — one trigger fired and was declined four separate ways.** QQQ lost its 20-day (717.7140) at 17:25Z on the only volume reading of this arc that cleared *every* denominator. It still was not tradeable: (1) that level was pre-screened **NOT TRADEABLE** at 17:35Z — five crossings today, eight sessions closing both sides; (2) the break fully **reversed** by 18:45Z and the reclaim then failed the volume clause on both bars (72%/65% of baseline, participation *falling* as price rose); (3) **index disagreement** — SPY never closed below its own 20-day all session; (4) the weekend. Which brings up the day's most useful finding:

> **Monday is Labor Day.** The next session is **Tuesday 09-08**, so this weekend is **~96 hours, not ~72**. Three runs today inherited the wrong number before one measured it. The measured post-holiday median gap of **0.417%** is larger than a TACTICAL scalp's *entire* −30% stop distance — and neither the stop nor the profit target is enforceable while the market is shut. Opening a Friday-afternoon scalp is not a stop-managed trade; it is an unmanaged coin flip with a bigger magnitude than either exit.

**Options, CORE — no candidate answered "why NOW", and there is a hard calendar block:** **ADBE and ORCL both report 09-10 pm**, which sits inside *every* 21–45 DTE window available today.

---

## 4. Sleeve state

| | |
|---|---|
| Account value | **$3,849.89** |
| Cash | $1,459.18 — **equal to `unleveraged_buying_power`, so no margin is extended** |
| Operational reserve (5%) | $192.49 |
| **Deployable** | **$1,266.69** |
| Per-name cap (30%) | $1,154.97 |
| Equity slots | **4 open of the 3–4 target** (hard band 3–5) |
| Options premium at risk | $749 hedge only — $0 TACTICAL, $0 CORE |
| Realized today | $0.00 options vs the −$400 cap; $0.00 equities |
| Throttles used | Options **0 of 8**; equities **0 of 3** |

No `_cash_hold` record exists and none is claimed — the idle cash is the residual of finding nothing A-grade, not a deliberate hold, and under the policy that distinction is the one that matters.

No calibration change was applied this week; the weekly calibration runs on the first trading day of the week and this is a Friday.

---

## 5. Watchpoints for Tuesday 09-08

1. **One question needs you, and it decides whether the desk trades at all on a full-book day.** The concentration policy targets 3–4 swings with a hard band of 3–5, and sizes each entry as `deployable ÷ remaining slots`. **At 4 open, that denominator is undefined** — "slots to target" is zero (no entry at any size), "slots to band max" is one (a $1,155 entry). The desk has applied the **stricter** reading and escalated rather than settling it. *Recommendation: treat 3–4 as the operating target and the 5th as headroom for an A/A+ only — otherwise the target quietly becomes a floor.* Logged as `_open_questions_for_ryan.q4`.
2. **LLY enters its time-stop warning window on 09-07 and the stop fires 09-10.** It will be sold green or red — that is the book's only mechanical loss discipline. MDLZ follows on 09-11.
3. **The 96-hour gap.** Four positions, no price stops, ~$1,935 exposed across a long weekend. That is by design (HARD RULE 5 forbids stops), but it is the largest uncovered window of the month.
4. **ADBE and ORCL print 09-10 pm** — blocks CORE options entries in the 21–45 DTE window and is a market-wide catalyst for Wednesday.
5. **Levels:** SPY 20-day 769.2065 (spot 769.68, barely above); QQQ 20-day 717.7140 (spot 717.71, sitting exactly on it). QQQ's 20-day has been ruled **not tradeable** as a trigger — it has been crossed too many times to define anything.

---

*Both books reconciled against the broker with ZERO DRIFT on every run today. No stop orders exist or were placed. No autonomous sell was executed, so no notification was owed.*
