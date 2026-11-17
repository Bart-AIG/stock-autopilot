# Daily report: trading day 2026-11-17 (Tuesday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20). This is the first run at or after 2:15 PM CT, and it comes before the 15:20–15:52 ET decision window. **The decision-window run will add today's sleeve orders, and the 15:46 ET run will make tonight's LEVX NIGHT decision.** All figures are from the broker at 20:16Z, not the close.*

**Today in one line:** a second down day, again led by semis.
- QQQ is **−1.39%** at 652.52 (prior close 661.75).
- SOXX is **−1.70%** at 138.83.
- NVDL is **−4.0%** at 15.70.

**Decision window (amended by the 15:31 ET run, 20:31Z):** SWING_M **bought VLO $51.25 and MPC $51.25** (IBS leg on each: IBS 0.181 and 0.163, both above their 200-day). Both filled at 20:32Z: VLO 0.14099 sh @ 363.50 (order 6afcb9d4), MPC 0.129791 sh @ 394.865 (order 6afcb9d6). ILMN and MRNA held. QLD stays flat.

**Amended by the 15:46 ET run (20:46Z):**
- **Decision-window re-check on fresher prices: SWING_M SOLD VLO and MPC.** At 15:46 their IBS read 0.277 and 0.262, above the 0.2 entry cut, so `decide()` no longer held them through the close. The procedure says a later window run corrects any difference, so both were sold at 20:47Z: VLO 0.14099 sh @ 364.5228 (+$0.14, order 6afcbd50), MPC 0.129791 sh @ 395.9878 (+$0.15, order 6afcbd52). ILMN (RSI2) and MRNA (RSI2 + IBS) are still held. QLD is still flat.
- **LEVX NIGHT: no position tonight.** QQQ 654.06 is below its 200-day (682.58) and SOXX 139.72 is below its 200-day (160.63), so both targets are 0. Nothing was bought.
- **BBW:** the 20:30Z candle returned `none`.
- **You closed your MU 2026-12-18 1220C ×5 yourself** at 20:34:52Z, at 1.03 ($515 proceeds, −$919.67 on a $1,434.67 basis). It is now in `_closed_positions`. You hold no MU option now, so the MU price alerts kept from the 1160C (and the 900 / 983 / 1000 ones) can be removed whenever you say.
- **Sleeve money is now the whole account, $2,313.44** (base $2,197.77, reserve $115.67, deployable $1,968.15), because you hold no positions of your own. Drawdown index 0.9069, **−11.26%** from the high-water mark: $228 of further sleeve loss reaches the −20% notice and $358 reaches the −25% halt.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
- **Held, both SWING_M:**
  - ILMN 0.384363 sh at 200.49 against a 215.76 cost (−$5.87).
  - MRNA 0.237278 sh at 206.57 against a 216.16 cost (−$2.28).
  - **New today:** VLO 0.14099 sh @ 363.50 and MPC 0.129791 sh @ 394.865 (IBS leg each, $51.25 each).
- **Decision (15:31 ET, `sleeves.py decide`):** MRNA held on RSI2 + IBS (RSI2 2.1, IBS 0.118); ILMN held on RSI2 (202.50 still below its 5-day SMA 206.00). LITE, MU, DELL, WDC, MRVL and VIAV are below their 200-day, so out.
- **QLD: flat, confirmed.** QQQ 654.07 is below its 200-day (682.58). RSI2 is 6.8, but the RSI2 and IBS legs need price above the 200-day.
- **The month's picks:** MRNA, LITE, MU, DELL, WDC, ILMN, VLO, MPC, MRVL, VIAV.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through the 20:00Z one returned `none` (no signal). There were no trades and no late exits.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $170.77 (10% of the base, on sleeve money).
- **Last night:** no position, so there was nothing to sell this morning.
- **DAY leg (TQQQ):** every :00 and :30 check through 15:30 was out (the reference is 53.33), and nothing was bought.
- **Tonight (preview; the 15:46 run decides):**
  - QQQ 652.52 is below its 200-day (≈682), so the TQQQ night target is 0.
  - SOXX 138.83 is below its 200-day (≈160), so the SOXL night target is 0.
  - So no night position is expected.
- No action was late, skipped or left with a null target.

## 4. Your own option (the agent never closes it)
- **MU 2026-12-18 1220C ×5,** marked at about **$485** (the broker's average is $2.869, a basis of about $1,435). Nothing changed today.

## 5. Legacy book, options book, growth paper
- The legacy book was closed out on 10-14. No agentic options are open.
- **Growth paper** (15:01 ET mark): $158.13 on $197.34 cost (**−19.87%**).
  - Open: PLTR −17.6%, NET −22.3%, CRWD −19.7%.
  - Two slots are empty.

## 6. Account and drawdown
- **Total value $2,282.61:** cash $1,671.54, options $485 (all yours), equity $126.07.
- **Deposit:** the broker shows $0 pending. Yesterday's report showed a $100 deposit pending, and cash has not risen, so it has not landed yet. Worth checking in the app.
- **Sleeve money $1,797.61** (total minus your option): base $1,707.73, reserve $89.88, deployable $1,581.66.
- **Drawdown** (real sleeve money, `capital.py`):
  - The index is 0.9064 against a high-water mark of 1.0220 (2026-10-09): **−11.31%**. No action.
  - **$176** more of sleeve loss reaches the −20% notice. **$277** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | −0.06% | −1.39% |
  | Month to date | −0.84% | not computed here |
  | Since 2026-09-30 | −9.36% | −11.79% (739.71 → 652.52) |

## 7. Next session (Wednesday 11-18)
- **09:31 ET:** sell any LEVX night position (none is expected).
- **TOM** stays off until the last trading day of November (11-30).
- **Proposals still waiting for you:** BBW NVDU and NVDA (from 11-02).
