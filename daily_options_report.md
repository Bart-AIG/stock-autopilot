# Daily report: trading day 2026-11-27 (Friday, half day, close 13:00 ET)

*Written by the first post-close run (18:01Z, 13:01 ET, prompt v20). Figures are from the broker at about 18:03Z.*

**Today in one line:** a strong half-day rally after Thanksgiving, with a late push in the final minutes.
- QQQ **+2.65%** at 650.76 (prior close 633.93). Still below its 200-day average (about 683).
- SOXX **+4.73%** at 134.03. NVDL **+1.40%** at 13.76.

**Agent orders today:** none.

**Your own trades today (agentic account):** you sold your **5 SOXL 2026-11-27 32C** in-app (recorded by the 16:16Z run, about +$612 realized on an $863 basis). You still hold **1 NFLX 2027-06-17 60C** (mark about $868). The agent never closes your positions.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
**No orders. A half day has no 15:20-15:52 ET decision window, so the rules placed nothing (CLAUDE.md, "Half-day closes").**
- **What the rules would have done at today's close (shadow run at 12:21 ET, journaled, you were notified once):** the turn-of-month leg switches on at today's close, because Monday 11-30 is the month's last trading day. `sleeves.py decide` would BUY **QLD $994.84** and **MRNA / LITE / MU / DELL / WDC / MRVL / VIAV at $74.61 each**, about $1,517 in all, and KEEP ILMN / VLO / MPC.
- **Monday's 15:20-15:52 ET window buys them**, since the turn-of-month leg is still on that day. The cost is one session of turn-of-month exposure, which today was a +2.65% QQQ day.
- SWING_M holds:

  | Name | Shares | Avg cost | Price | Value | P/L |
  |---|---|---|---|---|---|
  | ILMN | 0.368508 | 205.07 | 205.98 | $75.91 | +$0.34 |
  | VLO | 0.228449 | 330.80 | 329.55 | $75.29 | −$0.29 |
  | MPC | 0.210889 | 358.34 | 360.28 | $75.98 | +$0.41 |

## 2. BBW (NVDL, 20%)
- No position. The day's last candle (12:45-13:00 ET) closed 13.76: **no signal**. No candle gave a signal today.

## 3. LEVX (10%, live)
- Half day: morning exit only (`levx.EARLY_CLOSE`), and nothing was held from Wednesday night. **No DAY leg and no NIGHT position today**, so nothing is carried over the weekend. Next NIGHT decision: Monday 15:46 ET.

## 4. Legacy book and options
- Legacy run-off: closed (since 2026-10-14). No agentic options are open.

## 5. Growth paper book
- No daily mark today: the mark runs on the first run after 15:00 ET and a half day has none. Monday's run marks it.

## 6. Money and drawdown
- Total $3,486.29. Your positions (NFLX call) $868.00. **Sleeve money $2,618.29**; base $2,487.38; reserve $130.91; deployable $2,260.44.
- Sleeves: **+0.50% today**, −0.40% month to date, **−8.95% since 2026-09-30** (QQQ −12.02% since its 739.71 close that day).
- Drawdown **−10.92%** from the high-water mark (2026-10-09). **$267.00** more sleeve loss to the −20% notice, **$413.95** to the −25% halt.

## 7. Next session (Monday 2026-11-30)
- **Last trading day of November: turn-of-month leg ON.** The 15:20-15:52 ET window is expected to buy QLD and the seven SWING_M picks (about $1,500), on Monday's prices.
- **Tuesday 12-01 is the first session of December:** new SWING_M picks from the November closes, the first-session resize check, the BBW monthly review and the growth scorecard.
- Monday's first run after 10:30 ET: BBW weekly search and growth paper weekly research.
- Next half day: 2026-12-24.
