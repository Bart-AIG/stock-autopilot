# Daily report: trading day 2026-11-23 (Monday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20), before the 15:20–15:52 ET decision window. The decision-window run amends section 1 if it places a sleeve order. Figures are from the broker at 20:16Z.*

**Today in one line:** a broad, semi-led rebound.
- QQQ is **+7.18%** at 652.11 (prior close 608.45).
- SOXX is **+13.32%** at 139.84.
- NVDL is **+62.9%** at 16.83.

**No agent orders so far today.** You sold all your MU options in the app at 16:44–16:45Z (+$238 realized). The whole account, **$2,651.64**, is now sleeve money.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
- **No sleeve positions are open.**
- **QLD:** QQQ at 652.11 is still below its 200-day average (about 683.3), so SWING_Q stays flat whatever the RSI(2) and IBS readings say.
- **The 15:31 ET run decides** on $2,651.64 of sleeve money: QLD target about $1,008 if it were on, and about $76 per SWING_M name with a signal.
- **The month's picks:** MRNA, LITE, MU, DELL, WDC, ILMN, VLO, MPC, MRVL, VIAV.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:00Z returned `none`. There were no trades and no late exits.
- Monday weekly search ran at 15:31Z (see `bbw_state.json` `last_search`).

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $251.91.
- **Last night:** no position.
- **DAY leg (TQQQ):** out at every check through 15:00. The reference level was 50.17; TQQQ opened near it and traded below it, closing the 15:00 check at 48.99.
- **Tonight:** QQQ (652.11) and SOXX (139.84) are both below their 200-day averages, so both night targets are 0. The 15:46 ET run confirms this.
- No action was late or skipped. No targets were null.

## 4. Your own options
- **Closed by you, 16:44–16:45Z:**

  | Contract | Qty | Your sale | Realized |
  |---|---|---|---|
  | MU 2026-12-18 1000C | 3 | 3.95 | +$243.00 |
  | MU 2027-01-15 1200C | 4 | 3.35 | −$5.00 |

  Rows are in `holdings.json._closed_positions`. You hold no options now.
- The five MU price alerts kept from the 1160C era can be removed now that you hold no MU option. They stay until you say so.

## 5. Legacy book, options book, growth paper
- **Legacy book:** closed out on 10-14.
- **Options:** no agentic options are open.
- **Growth paper** (marked at 15:01 ET): $134.57 on $164.01 cost (**−17.95%**). CRWD is −24.57%, close to the −25% exit. That exit is checked on Mondays and was held at today's check.

## 6. Account and drawdown
- **Total value $2,651.64:** all cash, plus a $100 pending deposit. That is above Robinhood's $2,000 margin-account minimum again.
- **Sleeve money $2,651.64:** base $2,519.06, reserve $132.58, deployable $2,519.06.
- **Drawdown** (real sleeve money, `capital.py`): index 0.9073 against a high-water mark of 1.0220 (2026-10-09), **−11.22%**. No action. **$262.20** more of sleeve loss reaches the −20% notice, and **$411.54** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | 0.00% | +7.18% |
  | Month to date | −0.74% | −5.56% (690.49 → 652.11) |
  | Since 2026-09-30 | −9.27% | −11.84% (739.71 → 652.11) |

  The sleeves held no stock today, so they missed the rebound entirely. With QQQ under its 200-day average, that is what the rules do.

## 7. Tomorrow
- **Turn of the month:** not yet. The TOM leg turns on at the 11-27 close (the last trading day of November, a half session).
- **Thanksgiving:** markets are closed Thursday 11-26 and close at 1:00 PM ET on Friday 11-27.
