# Daily report: trading day 2026-11-19 (Thursday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20), before the 15:20–15:52 ET decision window. The decision-window run amends section 1 with the swing sleeve orders. Figures are from the broker at 20:16Z.*

**Today in one line:** a broad down day, led by tech and semis.
- QQQ is **−2.02%** at 646.20 (prior close 659.51).
- SOXX is **−2.39%** at 138.46.
- NVDL is **−4.9%** at 14.50.

One agent order today: the decision-window buy of ILMN ($7.89). Every BBW and LEVX check came back flat.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
*Decided by the 15:31 ET decision-window run (20:31Z), sleeve money $276.69.*
- **QLD stays flat.** QQQ 644.85 is below its 200-day (683.00); RSI2 8.0 and IBS 0.016 would both be "on" but need price above the 200-day.
- **Bought ILMN $7.89** (0.039407 sh @ 200.215, filled 20:31:55Z). IBS leg: IBS 0.038, above its 200-day (180.79).
- **Kept MRNA, VLO, MPC** (each still in: MRNA RSI2+IBS, VLO RSI2+IBS, MPC RSI2+IBS). No resize mid-month.
- LITE, MU, DELL, WDC, MRVL, VIAV are below their 200-day averages, so out.
- Holdings at the decision:

  | Name | Shares | Cost | Now | P/L |
  |---|---|---|---|---|
  | MRNA | 0.237278 | 216.16 | 198.54 | −$4.18 (−8.2%) |
  | VLO | 0.050018 | 342.88 | 340.29 | −$0.13 (−0.8%) |
  | MPC | 0.045934 | 373.36 | 370.28 | −$0.14 (−0.8%) |
  | ILMN | 0.039407 | 200.22 | 200.10 | $0.00 |

- Every target was executed as `decide()` printed it. Trade approvals are off; the order filled at once.
- **The month's picks:** MRNA, LITE, MU, DELL, WDC, ILMN, VLO, MPC, MRVL, VIAV.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:15Z returned `none` (no signal). There were no trades and no late exits.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $26.32 (10% of a $263 base).
- **Last night:** no position, so there was nothing to sell this morning.
- **DAY leg (TQQQ):** every :00 and :30 check from 10:00 to 15:30 was out. The reference is 55.19 (today's open), and TQQQ fell all day to about 49, so it never closed a bar above its band. Nothing was bought.
- **Tonight:** the 15:46 ET run decides. QQQ and SOXX are both below their 200-day averages, so both night targets are expected to be 0.
- No action was late, skipped or left with a null target.

## 4. Your own options (the agent never closes them)
- MU 2027-01-15 1200C ×4 (avg $3.3625) and MU 2026-12-18 1000C ×2 (avg $3.46). They cost $2,037 and are marked at **$1,860** (−$177). MU is −1.7% at 693.56.
- You have set no price levels for these contracts. The MU price alerts kept from earlier contracts stay on until you say to remove them.

## 5. Legacy book, options book, growth paper
- **Legacy book:** closed out on 10-14.
- **Options:** no agentic options are open.
- **Growth paper** (marked at 15:02 ET): $166.57 on $197.34 cost (**−15.59%**).
  - Open: PLTR −18.5%, NET −17.0%, CRWD −11.3%.
  - None is at its −25% exit. Two slots are empty.

## 6. Account and drawdown
- **Total value $2,137.07:** cash $195.55, options $1,860 (all yours), equity $81.52.
- **Sleeve money $277.07** (total minus your options): base $263.22, reserve $13.85, deployable $181.70.
- **Drawdown** (real sleeve money, `capital.py`): index 0.9074 against a high-water mark of 1.0220 (2026-10-09), **−11.22%**. No action. **$27.41** more of sleeve loss reaches the −20% notice, and **$43.01** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | +0.16% | −2.02% |
  | Month to date | −0.74% | −6.41% (690.49 → 646.20) |
  | Since 2026-09-30 | −9.26% | −12.64% (739.71 → 646.20) |

  The sleeves held only about $81 of stock today, so these returns are mostly cash sitting still while QQQ fell.

## 7. Next session (Friday 11-20)
- **09:31 ET:** sell any LEVX night position (none is expected).
- **TOM** stays off until the last trading day of November (11-30).
- **Friday review** is written by the 14:15 CT run.
- **Proposals still waiting for you:** the BBW candidates NVDU and NVDA (from 11-02).
