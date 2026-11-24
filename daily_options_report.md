# Daily report: trading day 2026-11-24 (Tuesday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20), before the 15:20–15:52 ET decision window. The decision-window runs amend section 1. Figures are from the broker at 20:16Z unless marked.*

**Today in one line:** a semi-led selloff that gave back part of Monday's rebound.
- QQQ is **−2.18%** at 636.82 (prior close 651.03).
- SOXX is **−7.95%** at 129.08 (prior close 140.22).
- NVDL is **−14.55%** at 14.27 (prior close 16.70).

**Agent orders today:** none so far. You placed no trades in the agentic account today. You hold no positions of your own, so the whole account is sleeve money.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
*Before the decision window. The 15:20–15:52 ET runs decide on fresh prices and amend this section.*
- **SWING_M holds** the three names bought Monday at 15:31 ET:

  | Name | Shares | Avg cost | Price 20:16Z | Value | P/L |
  |---|---|---|---|---|---|
  | ILMN | 0.368508 | 205.07 | 205.67 | $75.79 | +$0.22 |
  | VLO | 0.228449 | 330.80 | 325.52 | $74.36 | −$1.21 |
  | MPC | 0.210889 | 358.34 | 355.58 | $74.99 | −$0.58 |

- **QLD:** QQQ (636.82) is still below its 200-day average (about 683), so SWING_Q stays flat.
- Today's state (`sleeves_state.json`) is built for 2026-11-24, so the window can trade.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:00Z returned `none`. No trades and no late exits.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $259.34.
- **Last night:** no position (both indexes were below their 200-day averages at Monday's close).
- **DAY leg (TQQQ):** out at every check through 15:00. The reference level was 49.10 (Monday's close); TQQQ opened at 46.61 and never got back to it. It was 45.90 at 20:16Z.
- **Tonight:** QQQ (636.82, 200-day about 683) and SOXX (129.08, 200-day about 161) are both below their 200-day averages, so both night targets are 0 on 20:16Z prices. The 15:46 ET run makes the decision.
- No action was late or skipped. No targets were null.

## 4. Your own positions
- None. You hold no options or stock of your own in the agentic account.

## 5. Legacy book, options book, growth paper
- **Legacy book:** closed out on 10-14.
- **Options:** no agentic options are open.
- **Growth paper** (marked at 15:16 ET): $136.13 on $164.01 cost (**−17.00%**). NET −20.65%, CRWD −22.95% (the −25% exit is at 204.34; it is checked on Mondays, next 11-30), LLY +2.48%. Two slots are empty.

## 6. Account and drawdown
- **Total value $2,729.92:** $2,504.83 cash plus $225.09 in the three SWING_M names. That is above Robinhood's $2,000 margin-account minimum.
- **Sleeve money $2,729.92:** base $2,593.42, reserve $136.50, deployable $2,368.33.
- **Drawdown** (real sleeve money, `capital.py`): index 0.9068 against a high-water mark of 1.0220 (2026-10-09), **−11.27%**. No action. **$268.52** more of sleeve loss reaches the −20% notice, and **$422.36** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | −0.04% | −2.18% (651.03 → 636.82) |
  | Month to date | −0.80% | −7.77% (690.49 → 636.82) |
  | Since 2026-09-30 | −9.32% | −13.91% (739.71 → 636.82) |

  The sleeves are about 92% cash with QQQ under its 200-day average, which is what the rules do. That is why they barely moved today.

## 7. Tomorrow
- **Turn of the month:** not yet. The TOM leg turns on at the 11-27 close (the last trading day of November, a half session closing at 1:00 PM ET).
- **Thanksgiving:** markets are closed Thursday 11-26.
- **December picks:** the month's SWING_M list is fixed on the first session of December (12-01) from the November closes.
