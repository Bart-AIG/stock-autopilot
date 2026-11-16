# Daily report: trading day 2026-11-16 (Monday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20). This is the first run at or after 2:15 PM CT, and it comes before the 15:20–15:52 ET decision window. **The decision-window run adds today's sleeve orders, and the 15:46 ET run makes tonight's LEVX NIGHT decision.** All figures are from the broker at 20:16Z, not the close.*

**Today in one line:** another risk-off day led by semis.
- QQQ is **−2.77%** at 661.09 (prior close 679.89).
- SOXX is **−5.35%** at 141.31.
- NVDL is **−9.0%** at 16.23.

The agent has placed no orders so far today.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
- **Held:** ILMN 0.384363 sh (SWING_M) at 199.18, against a 215.76 cost (−$6.37). No QLD.
- **Decision window:** not yet run. QQQ (661.09) is below its 200-day average (≈682.4), so SWING_Q's RSI(2) and IBS legs can't turn on today.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through the 20:00Z one returned `none` (no signal). There were no trades and no late exits.
- **Weekly search (15:35Z):** the cache was refreshed for 8 symbols. NVDL, NVDU and NVDA passed. NVDU and NVDA were already proposed on 11-02 and are waiting for you. Both have the same underlying as the live NVDL, so adding either one adds to the same bet. Nothing new was proposed.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** ≈ $171 (10% of the base, on sleeve money).
- **Last night:** no position. The 11-13 NIGHT slot had no run because of the usage-limit outage, so there was nothing to sell this morning.
- **DAY leg (TQQQ):** every :00 and :30 check through 15:00 was out, and nothing was bought. The 15:30 check is still to come.
- **Tonight (preview; the 15:46 run decides):**
  - QQQ 661.09 is below its 200-day (≈682.4), so the TQQQ night target is 0.
  - SOXX 141.31 is below its 200-day (≈160.5), so the SOXL night target is 0.
  - So no night position is expected.
- No action was late, skipped or left with a null target.

## 4. Your own option (the agent never closes it)
- **MU 2026-12-18 1220C ×5.** You added 1 contract at 1.07 at 19:18:46Z. The broker's average is $2.869 (basis about $1,435), and the position is marked at about **$545**.

## 5. Legacy book, options book, growth paper
- The legacy book was closed out on 10-14. No agentic options are open.
- **Growth paper** (15:01 ET mark): $163.42 on $197.34 cost (**−17.2%**).
  - Open: PLTR −15.4%, NET −18.2%, CRWD −17.9%.
  - NVDA and NTRA were exited on paper. Two slots are empty.

## 6. Account and drawdown
- **Total value $2,344.39:** cash $1,722.83, options $545 (all yours), equity $76.56. A $100 deposit is pending.
- **Sleeve money $1,799.39** (total minus your option): base $1,709.42, reserve $89.97, deployable $1,632.86.
- **Drawdown** (real sleeve money, `capital.py`):
  - The index is 0.9073 against a high-water mark of 1.0220 (2026-10-09): **−11.22%**. No action.
  - **$178** more of sleeve loss reaches the −20% notice. **$279** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | −0.16% | −2.77% |
  | Month to date | −0.75% | not computed here |
  | Since 2026-09-30 | −9.27% | −10.63% (739.71 → 661.09) |

## 7. Next session (Tuesday 11-17)
- **09:31 ET:** sell any LEVX night position (none is expected).
- **TOM** stays off until the last trading day of November (11-30).
- **Proposals still waiting for you:** BBW NVDU and NVDA (from 11-02).
