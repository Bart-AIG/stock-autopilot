# Daily report — trading day 2026-09-24 (Thursday)

*Written by the 19:15Z scheduled run (2:15 PM CT, the v11 threshold). Master carried the 2026-09-23 report, so this run owned the duty. Broker read at 19:15:33–35Z: zero drift in both books.*

## 1. DAY TRACK (PAPER, day 7)
- **Opening range** (QQQ, 1-minute bars): 734.6301 – 736.02, open 735.29 / close 735.79, body 36% of range → **LONG**.
- **Result: SKIP (late entry).** The anti-chase ceiling was 736.02 + 0.5 × 1.3899 = **736.7150**. Spot was 737.0759–737.20 when the bars first became readable (~13:46Z), 0.36–0.49 above the ceiling. No position, 0R.
- Unlike the 09-22 skip, which was about capital, this one was about the setup. There was $2,164 deployable against a ~$737 share. The cause is the lag between the signal and the first run that can act on it: the OR closed at 13:35Z but was first readable at 13:46Z, and in those 11 minutes QQQ drifted +1.41, more than the 0.925 of headroom.
- **Running tally:** 7 paper days, 5 signals taken (2 winners +6.48R / +1.35R, 3 losers −1R each), 2 skips. `graduate()` needs ≥10 days and ≥8 signals, and signals are the binding constraint. Next review is the Monday 2026-09-28 calibration. The track stays in PAPER.

## 2. Positions
| Name | Sleeve | Entry | Mark (19:15Z) | P/L | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|---|
| V | swing | 368.0799 × 2.716801 | 366.91 | −$3.18 / −0.32% | 3d | **2026-10-05** | RSI2 8.6 dip, 9.6% above a rising 200-day. Broad financials de-risk, not a company-specific drop. PT raises into the weakness (RBC $466, Wolfe $460). |
| BMY | swing | 61.4439 × 11.734281 | 60.768 | −$7.93 / −1.10% | 0d | **2026-10-08** | Deepest oversold of the morning's list (RSI2 2.1). Dip inside a rising 200-day (+4.1% cushion). No company-specific news behind the −10% slide. Piper raised its PT to $82. Clean Phase 3 Sotyktu data. Earnings 10-29 fall outside the window. |

Both are underwater, so the RSI2≥70 take-profit can't fire on either one; it only fires on green positions. Neither is green enough for a trail alert (V needs $432.98, BMY $72.29). No price stops (HARD RULE 5). Options book: **flat**.

**V thesis note:** today brought the proposed $167.5M Burke v. Visa ATM-fee settlement (V's share ~$88.8M, ~0.2% of annual revenue, one-time). I judged it immaterial: it belongs to the long-running antitrust overhang and isn't a new break, and V closed out the session up ~1.5% with the news already public.

## 3. Actions taken today
**① TIME STOP / SELL — ABNB and UNP (autonomous, 13:37Z).** Both were entered 2026-09-10, so 2026-09-24 is day 14 exactly and `report.py`'s `days_held >= 14` branch fired. The 09-23 report had pre-announced both ("TIME STOP in 1d").
- ABNB: 6.573584 sh @ 152.5273 → **−$111.73 (−10.02%)**, order 6ab5279c.
- UNP: 3.858199 sh @ 274.5265 → **−$40.84 (−3.71%)**, order 6ab527a0.
- Why it wasn't a judgment call: neither hit its target (183.08 / 298.32), and neither could print a green RSI2 bounce. HARD RULE 5 forbids price stops, so the 14-day time stop was the only exit either position could ever have had. That is exactly the case it was built for on 09-02. Quotes were re-taken at 13:37Z, after the opening auction. ABNB was +2% on the day at the fill, so the exit was sold *into* a bounce.
- **Lesson written to the ledger (ABNB):** analysts raising targets into a decline is evidence the market is repricing the stock rather than the company getting worse. That read was correct, and the trade still lost 10%. Price targets are 12-month fundamental marks and say nothing about the timing of a 2-week mean-reversion trade.
- Broker-confirmed realized P/L today: **−$152.53** across 2 closing trades (equity book; no options cap involved).

**② BUY — BMY $721.00 (autonomous, 14:18Z).** 11.734281 sh @ 61.4439, order 6ab53133. Taken on the first run with both today's report on master and the clock past 14:15Z (the opening-deferral preference).
- Sizing: deployable $2,163.62 ÷ 3 remaining slots = $721. Two slots would have meant $1,082, which breaches the 30% per-name cap ($998), so filling toward four slots was forced.
- Contrary evidence was logged, not omitted: a bearish Dec 62.50 put sweep and a $403K CMO Form 4 sale. Both are small.

## 4. Candidates considered and SKIPPED
- **USB / JPM / SCHW / MS / BAC (banks), declined on HARD RULE 7 thesis.** The sector is being de-rated on named drivers: a hiking Fed read as negative for bank margins (10y ~4.98%), credit-quality worries, and the AI-agent payments disintermediation story. Jefferies cut JPM's PT this morning. Their 10-13..10-15 earnings fall *after* a 10-08 time stop, so the earnings flag is not the reason. Owning record: `holdings.json._WHY_THE_OVERSOLD_BANKS_ARE_A_HARD_RULE_7_DECLINE_NOT_A_CORRELATION_DECLINE_2026-09-24`.
- **UNH, B, so no position.** The trend and the analysts are fine, but the intermediate structure is a downtrend rather than a dip (20-day < 50-day, −15% off the high in ~2 months).
- **HPQ, C.** The demand thesis is weakened: planning for a mid-single-digit 2027 PC unit decline, the DRAM/NAND cost shock, and a mean PT 13% below spot.
- **PATH, C.** AI-software name on the losing side of the same disintermediation story. **DIA:** index ETF, no thesis.
- **FCEL, C (spec).** The stop is 17.9% wide on a high-beta speculative name. It does not merit concentrated sizing.
- **EPD, excluded under the sector steer** (energy/midstream, de-emphasized oil complex). Reply to override.
- **ABNB, re-entry flagged by the report (RSI2 3.6).** Not taken. It is the same stalled hold the time stop just recycled, and nothing has changed about why it stalled.
- **Options (CORE):** no candidate answered "why now". Separately, today's IV sweep read **8 of 8 core names rich** on ex-gap IV/RV. The durable finding is that for nine sessions this came from realized vol draining, not from premium being bid. Owning record: `holdings.json._THE_CORE_LIST_HAS_READ_8_OF_8_RICH_FOR_NINE_SESSIONS_AND_THE_CAUSE_IS_THE_DENOMINATOR_NOT_THE_PREMIUM`.

**The third equity slot was left open on grade, not on capital or throttle.** $1,443 deployable and 1 of 3 equity entries used both permitted it; the A-grade bar did not. That cash is what is left after funding every A-grade idea, and the capital policy treats that as a correct state. It is not a `_cash_hold`.

## 5. Book state (broker, 19:15Z)
- Total value **$3,318.51**. Equity $1,709.50, options $0, cash = buying power = **unleveraged buying power $1,609.01** (no margin used).
- Operational reserve 5% = **$165.93**. **Deployable $1,443.08**, enough for two ~$721 slots, above the $600 minimum.
- Equity slots: **2 of the 3–4 target**. Throttles: equity 1/3, options 0/3. Options realized P/L $0.00 vs the −$400 cap.
- Premium at risk: $0 (CORE). No hedge is currently held.
- Calibration changes this week: none applied. Monday 09-28 is the next run, which is also the next `graduate()` review.

## 6. Tomorrow's watchpoints (Fri 2026-09-25)
- **DAY TRACK:** compute the OR on the first run ≥13:45Z. Watch whether the signal-to-action lag skips the setup a second day running.
- **V:** RSI2 is sitting near 69 (report 68.8) but the position is still underwater. The take-profit fires only on an RSI2≥70 cross *while green* (price > 368.08).
- **BMY:** day 1 of 14. No catalyst until the 10-02 dividend record date.
- **Friday review is due.** It belongs to the run that writes Friday's daily report (first run ≥19:15Z), not to the first run of the day. The week's P/L comes from the broker.
- Time stops coming up: V 10-05, BMY 10-08.
