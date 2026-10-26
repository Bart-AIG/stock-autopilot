# Daily report — trading day 2026-10-26 (Monday)

*Written by the run that started 19:19Z (15:19 ET), invoked with **prompt v17**. Figures are broker figures priced at 19:19Z, not the close. This run started one minute before the 15:20–15:52 ET decision window, so it placed no sleeve orders. The decision-window run (expected ~19:25Z, 15:25 ET) amends Section 1 with its orders.*

**Today in one line:** a strong day for QQQ (+1.31%, 713.61 vs 704.40) and QLD (+2.61%, 88.40). The sleeves went into today in cash after Friday's exits. Drawdown on sleeve value is −1.81%, far from the −20% notice level.

## 1. Sleeves
Both sleeves hold **nothing**: everything was sold in Friday's decision window. Cash is **$544.68** (plus a $100 deposit still pending, not spendable). Total value is $2,070.68, so the 5% reserve is $103.53 and **deployable cash is $441.15** for today's window.

This month's SWING_M picks (fixed 10-01, from `sleeves_state.json`, current for today): MRNA, MU, LITE, DELL, WDC, AMD, INTC, VIAV, MRVL, ILMN.

**Decision window (amended by the 15:25 ET run, prices at 19:25:40Z, total value $2,040.68):** `sleeves.py decide` put two SWING_M names in and everything else out.
- **SWING_Q (QLD): OUT.** QQQ 713.40, RSI(2) 64.5, IBS 0.81, above its 200-day. No leg is on, so no QLD today.
- **MRNA: BOUGHT $58.16**, 0.297068 sh @ $195.78 (order `6adfa953`, filled 19:26:12Z). RSI(2) leg: RSI(2) 9.7 < 10, price above the 200-day. Exits when price closes above its 5-day SMA (~$217).
- **ILMN: BOUGHT $58.16**, 0.216248 sh @ $268.95 (order `6adfa956`, filled 19:26:14Z). IBS leg: IBS 0.195 < 0.2, above the 200-day. Exits at IBS > 0.8 or after 5 sessions.
- MU, LITE, DELL, WDC, AMD, INTC, VIAV, MRVL: out (no leg on).
- Trade approvals are off; both orders filled at once. Cash left ~$428.

## 2. Legacy run-off
Done. No `sleeve: "swing"` positions remain.

## 3. Options
No agentic options. Ryan's own **MU 2026-12-18 1220C ×2** (`placed_agent: "user"`): mark $1,526 vs $1,755 cost (−$229). It is his position: the agent records it and never closes it.

## 4. Growth paper sleeve
The Monday research and check ran at the 15:24Z run (see the journal). No real orders.

## 5. Account vs QQQ
- Today: the account has no sleeve exposure, so its move comes only from Ryan's MU call. QQQ +1.31%.
- Sleeve value $3,539.68 vs high-water mark $3,604.85: **−1.81%**.

## 6. Tomorrow and this week
- **Turn of the month:** the TOM leg turns on at Friday 10-30's close (last trading day of October) and holds through the first 3 sessions of November. QLD and every SWING_M pick with the leg on will be bought in Friday's window.
- **Month roll:** new SWING_M picks are fixed on Monday 11-02 (first session of November) from the 10-30 closes.
