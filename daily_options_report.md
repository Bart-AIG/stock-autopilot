# Daily report: trading day 2026-11-20 (Friday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20), before the 15:20–15:52 ET decision window. The decision-window run amends section 1 if it places a sleeve order. Figures are from the broker at 20:16Z.*

**Today in one line:** a heavy selloff, led by semis.
- QQQ is **−4.86%** at 613.68 (prior close 645.04).
- SOXX is **−9.87%** at 124.33.
- NVDL is **−25.7%** at 10.59.

**No agent orders today.** You sold all four SWING_M positions yourself in the app at 14:34–14:35Z, and you added one MU 2026-12-18 1000C at $2.50. That leaves **$26.98 of sleeve money**, so the sleeves can't take a meaningful position until cash comes back to the account.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
- **Your sales (placed_agent user, so they are recorded, not reversed):**

  | Name | Shares | Agent cost | Your sale | P/L |
  |---|---|---|---|---|
  | ILMN | 0.039407 | 200.22 | 198.225 | −$0.08 |
  | MRNA | 0.237278 | 216.16 | 201.73 | −$3.42 |
  | VLO | 0.050018 | 342.87 | 336.28 | −$0.33 |
  | MPC | 0.045934 | 373.36 | 367.14 | −$0.29 |

  Total realized: **−$4.12** (broker).
- **QLD is flat.** QQQ is below its 200-day average.
- **The 15:31 ET run decides** on $26.98 of sleeve money: about $10 for QLD and $0.77 per SWING_M name. Orders under $1 are skipped.
- **The month's picks:** MRNA, LITE, MU, DELL, WDC, ILMN, VLO, MPC, MRVL, VIAV.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:00Z returned `none`. There were no trades and no late exits.

## 3. LEVX sleeve (10%, live)
- **Sleeve:** $2.56.
- **Last night:** no position.
- **DAY leg (TQQQ):** out at every check. TQQQ fell from 47.52 at the open to about 41.8.
- **Tonight:** QQQ and SOXX are both below their 200-day averages, so both night targets are expected to be 0. The 15:46 ET run confirms this.
- No action was late or skipped. A null target on the catch-up slots without bars changed nothing, because nothing was held.

## 4. Your own options (the agent never closes them)
- MU 2027-01-15 ×4 (avg $3.3625) and MU 2026-12-18 ×3 (avg $3.14, including today's $2.50 add). They cost $2,287 and are marked at **$953**.
- You have set no price levels for these contracts.

## 5. Legacy book, options book, growth paper
- **Legacy book:** closed out on 10-14.
- **Options:** no agentic options are open.
- **Growth paper** (marked at 15:01 ET): $155.64 on $197.34 cost (**−21.13%**).
  - PLTR is −23.4% and NET is −24.0%, both near the −25% exit. The exit is checked on Monday.

## 6. Account and drawdown
- **Total value $979.98:** cash $26.98, options $953 (all yours), equity $0. This is below Robinhood's $2,000 margin-account minimum.
- **Sleeve money $26.98:** base $25.63, reserve $1.35, deployable $25.63.
- **Drawdown** (real sleeve money, `capital.py`): index 0.9073 against a high-water mark of 1.0220 (2026-10-09), **−11.22%**. No action. **$2.67** more of sleeve loss reaches the −20% notice, and **$4.19** reaches the −25% halt.
- **Sleeves vs QQQ:**

  | Period | Sleeves | QQQ |
  |---|---|---|
  | Today | +0.13% | −4.86% |
  | Week (from the 11-13 close) | −0.16% | −9.74% (679.89 → 613.68) |
  | Month to date | −0.74% | −11.12% (690.49 → 613.68) |
  | Since 2026-09-30 | −9.27% | −17.04% (739.71 → 613.68) |

  The sleeves held about $81 of stock at most this week, so these returns are mostly cash sitting still while QQQ fell. They are not evidence of an edge.

## 7. Friday review (week of 2026-11-16), from the broker
- **Sleeve trades:**
  - 11-16: bought MRNA $51.29.
  - 11-17: bought VLO and MPC ($51.25 each) at 15:31 ET, then sold both at 15:46 ET when the IBS leg turned off on fresher prices (+$0.29).
  - 11-18: sold ILMN (−$2.45), and re-bought VLO and MPC at $17.15 each.
  - 11-19: bought ILMN $7.89.
  - 11-20: you sold all four in the app (−$4.12).
- **Sleeve equity realized for the week:** about **−$6.28**.
- **Broker total for the week:** −$308.28. That includes your MU 1220C ×5 close on 11-17 (about −$302), which is your trade, not the sleeves'.
- **Execution fidelity:**
  - The decision window ran every day, Mon–Thu, at 20:31Z and 20:46Z, and every target was executed as `decide()` printed it. Friday's window has not run yet.
  - There were 32 market-hours scheduler runs each day Mon–Thu and 28 so far on Friday. No BBW slot was missed, and there were no late BBW or LEVX exits.
  - No LEVX DAY position was carried overnight.
- **Best execution:** on 11-17 the 15:46 re-decide unwound VLO and MPC within the window, exactly as the rule says.
- **Worst execution:** none by the agent. The binding constraint is capital: your option buys and today's sales leave the sleeves about $27 to trade with.

## 8. Next session (Monday 11-23)
- **09:31 ET:** sell any LEVX night position (none is expected).
- **Monday duties:** the weekly check, the BBW weekly search, growth paper research, and the −25% exit check on PLTR and NET.
- **TOM** comes on at the last trading day of November (11-30).
- **Proposals still waiting for you:** the BBW candidates NVDU and NVDA (from 11-02).
