# Daily report — trading day 2026-11-13 (Friday)

> **Amended 2026-11-13T23:51Z:** routine runs failed from 20:18Z to 21:19Z on the usage limit (cause: an interactive research session). The decision window, the LEVX NIGHT slot and three BBW candles had no run. Nothing was due except one MRNA entry (about $72), which was not taken. BBW had no signal and LEVX's targets were 0.

*Written by the run that started 20:16Z (15:16 ET, prompt v19). It is the first run at or after 2:15 PM CT and comes before the 15:20–15:52 ET decision window, so **the decision-window run will add today's sleeve orders and tonight's LEVX NIGHT decision.** Figures are broker figures at 20:16Z, not the close.*

**Today in one line:** a risk-off day led by semis. QQQ is **−1.26%** (679.51 vs 688.17), SOXX **−3.72%** (149.23), NVDA's 2× fund NVDL **−4.0%** (17.82) and MU **−3.4%** (771.11). The agent has placed no orders so far today.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
- Held: ILMN 0.384363 sh (SWING_M, RSI(2) leg), now 208.10. No QLD.
- **Decision window: DID NOT RUN (amended 2026-11-13T23:51Z by an interactive session).** The account's 5-hour usage limit was reached at about 20:18Z, so the 20:31Z and 20:46Z routine runs failed and no sleeve order was placed. At closing prices `decide()` would have bought about $72 of MRNA (RSI(2) 7.5, IBS 0.17) and kept ILMN; QLD stays flat (QQQ 679.90 is below its 200-day 682.24). No exit was missed. Monday's window decides again.

## 2. BBW sleeve (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:00Z returned `none` (no signal). No trades and no late exits.

## 3. LEVX sleeve (10%): first live day (v19 observed 19:16Z)
- **Mode: live.** Sleeve ≈ $236 (10% of the base).
- **Last night:** no position (the sleeve wasn't live yet).
- **DAY leg (TQQQ):** every check from 14:30 on (the first v19 run) was out. The 15:00 bar closed at about 57.5, ~7% under the band of max(open 59.91, prior close 59.88) × (1 + its 14-session average move). Nothing was bought, and nothing is held.
- **Tonight's NIGHT decision:** this run doesn't make it. The 15:46 ET run does: TQQQ if QQQ is above its 200-day, SOXL if SOXX is above its 200-day. No action was late, skipped or left on a null target.

## 4. Ryan's own option (the agent never closes it)
- MU 2026-12-18 1220C **×4**. Ryan added one contract @ 1.70 at 19:30:59Z, so the basis is now $1,327.67. It's valued at about **$692** (about −$636), with MU at 771.11.

## 5. Legacy book / options book / growth paper
- The legacy book was closed out on 10-14. No agentic options are open. The 15:01 ET run (or the next run after 15:00) marks growth paper.

## 6. Account and drawdown
- Total value is **$2,501.91**: cash $1,729.87, options $692, equity $80.04. Total value was $2,730 at yesterday's window. Most of the fall is Ryan's $170 MU add, paid from cash, plus the option's mark.
- Sleeve value (measured without Ryan's own P/L and the deposits) is **$4,172.91**, which is **−0.07%** from its $4,176 high-water mark. No drawdown action.

## 7. Next session (Monday 11-16)
- First run: sell any LEVX night position (09:31 ET), then the BBW weekly search and growth-paper research after 10:30 ET, and the weekly check.
- TOM stays off until the last trading day of November.
