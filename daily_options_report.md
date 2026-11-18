# Daily report: trading day 2026-11-18 (Wednesday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20). Section 1 was amended by the 15:31 ET decision-window run. Section 3 was amended by the 15:46 ET run with tonight's LEVX NIGHT decision. All figures are from the broker at 20:16Z, not the close.*

**Today in one line:** a small up day for QQQ, a red day for semis and NVDL.
- QQQ is **+0.28%** at 658.81 (prior close 656.95).
- SOXX is **−0.44%** at 140.84.
- NVDL is **−5.9%** at 15.265.

**The day's main event was your MU purchase, not an agent trade.** At 19:21–19:22Z you bought MU calls in the app (details in section 4). That cash came out of the same pool the sleeves use. **Sleeve money fell from $2,313 this morning to $602**, so every sleeve's target is now about a quarter of what it was. The agent's only orders today were the three SWING_M trades at 15:31 ET (section 1).

## 1. Sleeves (SWING_Q 40% / SWING_M 30%): decided at 15:31 ET
*Amended by the decision-window run that started at 20:31Z (15:31 ET). `sleeves.py decide` ran on 20:31:32Z prices with sleeve money $601.90.*
- **QLD stays flat.** QQQ 658.06 is below its 200-day (682.80), so neither the RSI2 leg nor the IBS leg can be on.
- **SWING_M orders, all filled by 20:32:29Z:**
  - **Sold ILMN**, 0.384363 sh at 209.38 (cost 215.76): **−$2.45** realized. Its IBS leg reached the 5-session limit (IBS 0.785, RSI2 75.6).
  - **Bought VLO**, $17.15 = 0.050018 sh at 342.87. RSI2 6.3 and IBS 0.09, above its 200-day.
  - **Bought MPC**, $17.15 = 0.045934 sh at 373.36. RSI2 4.6 and IBS 0.162, above its 200-day.
  - **Kept MRNA**, 0.237278 sh. RSI2 1.1 and IBS 0.058, so both legs are on. No mid-month resize.
- The other six picks (LITE, MU, DELL, WDC, MRVL, VIAV) are below their 200-day, so they are out.
- Trade approvals are off, and both buys were tradable and fractional. A later run in the window may re-decide on fresher prices (yesterday's 15:46 ET re-decide sold MPC).
- **The month's picks:** MRNA, LITE, MU, DELL, WDC, ILMN, VLO, MPC, MRVL, VIAV.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle from 14:30Z through 20:00Z returned `none` (no signal). There were no trades and no late exits.
- NVDL is down 5.9% today, but the entry rule needs a pullback after a breakout plus MACD > 0, and neither held.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $57.21. That is 10% of the base, and the base is now much smaller (see the top of this report).
- **Last night:** no position, so there was nothing to sell this morning.
- **DAY leg (TQQQ):** every :00 and :30 check from 10:00 to 15:00 was out. The reference is 52.82 (today's open), and TQQQ closed no bar above its band. Nothing was bought.
- **Tonight (decided by the 15:46 ET run, 20:46Z):**
  - QQQ 659.06 is below its 200-day (682.81), so the TQQQ night target is 0.
  - SOXX 141.18 is below its 200-day (160.77), so the SOXL night target is 0.
  - No night position. Nothing to sell at tomorrow's 09:31 run.
- **15:46 ET re-check:** sleeve money $276.78 (total $2,232.78 minus your options at $1,956.00), base $262.94, deployable $181.71. The swing decision re-run gave the same answer as 15:31 (hold MRNA, VLO, MPC; nothing else on), so no order was placed. Drawdown -11.3% from the high-water mark; $27.16 more sleeve loss reaches the -20% notice, $42.76 the -25% halt.
- No action was late, skipped or left with a null target.

## 4. Your own options (the agent never closes them)
| Contract | Qty | Your cost | Bought (UTC) |
|---|---|---|---|
| MU 2027-01-15 1200C | 3 | $3.40 ($1,020) | 19:22:00 |
| MU 2026-12-18 1000C | 2 | $3.46 ($692) | 19:22:19 |

- The two positions together cost $1,712. The broker marks them at **$1,614** (−$98).
- You were notified about them once, at 19:31Z.
- You still have no price levels set for these contracts. The MU price alerts kept from earlier contracts are still on until you say to remove them.

## 5. Legacy book, options book, growth paper
- **Legacy book:** closed out on 10-14.
- **Options:** no agentic options are open.
- **Growth paper** (marked at 15:16 ET): $167.07 on $197.34 cost (**−15.34%**, up from −19.87% yesterday).
  - Open: PLTR −17.1%, NET −16.3%, CRWD −12.6%.
  - None is near its −25% exit. Two slots are empty.

## 6. Account and drawdown
- **Total value $2,216.17:**
  - cash $474.41
  - options $1,614 (all yours)
  - equity $127.76
- **Sleeve money $602.17** (total minus your options):
  - base $572.06
  - reserve $30.11
  - deployable $444.30
- **Drawdown** (real sleeve money, `capital.py`):
  - The index is 0.9071 against a high-water mark of 1.0220 (2026-10-09): **−11.25%**. No action.
  - In dollars, the notice and halt lines are now close because sleeve money is small: **$59** more of sleeve loss reaches the −20% notice, and **$93** reaches the −25% halt.
  - Your option buy did not move the reading. Sleeve money left with it, so the percentage is unchanged.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | +0.01% | +0.28% |
  | Month to date | −0.77% | not computed here |
  | Since 2026-09-30 | −9.29% | −10.94% (739.71 → 658.81) |

## 7. Next session (Thursday 11-19)
- **09:31 ET:** sell any LEVX night position (none is expected).
- **TOM** stays off until the last trading day of November (11-30).
- **Proposals still waiting for you:** the BBW candidates NVDU and NVDA (from 11-02).
