# Daily report — trading day 2026-09-30 (Wednesday)

*Written by the 19:15Z scheduled run (2:15 PM CT), invoked with **prompt v15**. Broker read 19:15Z: **zero drift** in both books. Every P&L figure comes from the broker (`get_realized_pnl`, `get_equity_orders`).*

## 1. Day track (PAPER)
- **Opening range (QQQ, 09:30–09:35 ET, 1-min bars):** high 742.75 / low 739.76, open 740.19 → close 741.73. The body was 51% of the range, so the signal was **LONG** (vehicle QQQ).
- **No paper trade: skipped for cash.** `plan_entry()` returned *skip*: deployable cash was $668.92 against one QQQ share at $741.52. The swing book was full (4 of 4 slots).
- This is the known structural constraint: a long signal can't be funded while the swing book is fully deployed. A short signal via PSQ (~$25/share) still fits.
- **Running paper tally:** 11 paper days, 8 signals, **+6.47R** (unchanged). Monday's 10-05 calibration runs `graduate()`. **Still PAPER until then.**

## 2. Positions
| Name | Shares | Entry | Mark ~19:15Z | P/L | Grade (19:07Z report) | Why we own it |
|---|---|---|---|---|---|---|
| **MRK** | 4.194296 | 147.82 | 146.06 | −1.2% | A+ 12/12 #11 | **NEW today.** Pharma leader on a 21-EMA pullback |
| DE | 0.930369 | 681.45 | 670.90 | −1.5% | A+ 12/12 #13 | Ag-equipment leader bought on an RSI2 dip (RSI2 now 2.9) |
| ABBV | 2.408819 | 263.61 | 262.87 | −0.3% | A+ 12/12 #14 | Pharma leader on a 21-EMA pullback |
| FCX | 8.630265 | 71.84 | 70.56 | −1.8% | B 8/12 #57 (still inside the top-25% hold bar, ~#57 of 229) | Copper leader dip. Held on thesis; sold if its rank leaves the top 25% |

- **Options:** none. No stops on the swing book (HARD RULE 5).
- All four positions are underwater, so none is close to green-enough for a native trail.
- **Earnings:** MRK reports 10-29 and ABBV 10-30. Both are about 4 weeks out, beyond a normal 1–3 week swing. If either is still held in late October, the print becomes a live risk.

## 3. Actions today (both autonomous, `placed_agent: agentic`)
1. **SELL TGT (take-profit)** — 14:15:53Z, all 3.980133 sh @ **158.5629**. **Realized +$6.10 (+1.0%)**, per the broker.
   - **Why:** live RSI2 was 70.6 at 158.64, and the position was green (entry 157.03). The RSI2 ≥70 cross *is* the exit, with no magnitude test.
   - **Why the wait until 14:15Z:** the condition was first seen at 13:47Z, with RSI2 76.5 at 159.60. The execution was **deferred**, because the only report on master was yesterday's 19:08Z report, and a stale report means no autonomous equity trade. It executed on the first run that had today's 14:06Z report.
   - The deferral cost about $4 (159.60 → 158.56). That is the price of the freshness rule, and it is working as designed.
2. **BUY MRK $620** — 14:16:50Z, 4.194296 sh @ **147.8198**.
   - **Setup:** A+ #10 in the 14:06Z report, 21-EMA pullback. The TGT proceeds reopened one slot.
   - **Sizing:** it just cleared the $600 minimum.
   - **Freshness gate:** all four inputs (live quote, trigger on the live price, news check, grade age) passed. The evidence is in `holdings.json` under `positions[MRK]._freshness_gate`.
   - **Context:** this re-enters a name the book took profit on yesterday at 149.12. That is signal-based, not a chase.
   - **Since the fill:** MRK slid to 146.06 on a −2.2% day. It is still A+ #11.

## 4. Skipped
- **Equity entries:** none possible after 14:16Z. Equity deployable = $847.56 unleveraged BP − $166.31 reserve − $665.25 options bucket = **$16.00**, well under the $600 minimum, and the book holds 4 of 4 slots. TGT re-appeared as an A+ 21-EMA pullback from 16:08Z, and GILD appeared as a new A+ #20 21-EMA pullback. **Neither was funded.**
- **Rotation (does a new name beat the weakest holding?):** not triggered. Every holding is still A+, except FCX at B, which is inside the hold bar. Rotation sells only on the entry stack, and selling a sound underwater name to buy a fresher signal is the churn HARD RULE 5 forbids.
- **Options, re-graded on this run's quotes** (19:15:20–19:15:48Z, 2026-10-30 monthly, 30 DTE, bucket $665.25):
  - **TGT 157.5C** (4.75 / 5.55): spread 15.5% of mid. **Fails** the 10% bar. OI 114, delta .51.
  - **TGT 162.5C** (3.00 / 3.25): spread 8.0% passes. **Fails** on OI 86 (under 100) and on payoff: breakeven 165.63 is above the 164.44 target.
  - **DE 720C** (6.30 / 7.60): **fails** spread (18.7%), OI (24) and delta (.22; the floor is .25).
  - **DE 700C** (11.10 / 12.70): costs $1,270, over the bucket. **Fails.**
  - **Not priced, because each has its own earnings before the 10-30 expiry:** GILD (10-29), MRK (10-29), ABBV (10-30). The next monthly (11-20) is 51 DTE, outside the 21–45 window.
  - **No options entry** on any run today. Every run re-quoted and re-graded (v15 duty). The binding problem all day was TGT's and DE's spreads and open interest.
- **Excluded B/C RSI2 dips** (listed by the report, not setups): IBKR, KO, NUE, IWM, FCX, MA, V, JNJ, UNH, EOG.

## 5. Sleeve state
- Account total **$3,326.24**; cash = unleveraged BP = **$847.56**. **No margin.**
- 5% operational reserve: $166.31.
- **Options bucket:** $665.25 (20%), **$0 at risk**. Options realized $0.00 against the −$400 cap. Options entries today: 0 of 3.
- **Equity:** 1 of 3 entries used today (MRK). **Slots: 4 of 4** (target filled). Equity realized today: **+$6.10** (TGT).

## 6. Calibration
No change this week. In-regime closes (since 2026-09-25) are far below n=20, and `recommend()` only reports at that size.

## 7. Tomorrow's watchpoints
- **Take-profit:** an RSI2 ≥70 cross on any *green* name. All four are red now, and ABBV is closest (−0.3%).
- **GRADE EXIT:** FCX fell from #33 to **#57** today, about at the edge of the top 25% (~57 of 229). **One more notch down and it is sold, green or red.** This is the most likely action tomorrow.
- **DE:** RSI2 is 2.9, deeply oversold on an A+ name. It is held, so there is no add; Law 3 bars adding to a loser without Ryan.
- **Day track:** QQQ long signals stay unfundable while the book is full. The Monday 10-05 calibration decides the phase on 11+ days / 8 signals / +6.47R.
- Equity entries are throttled to 3 per day and reset at the 09:30 ET open.
