# Daily report: trading day 2026-11-25 (Wednesday)

*Written by the run that started at 20:16Z (15:16 ET, prompt v20), before the 15:20–15:52 ET decision window. The decision-window runs amend section 1. Figures are from the broker at 20:16Z unless marked.*

**Today in one line:** a weak open, a midday recovery, and a red close into the Thanksgiving break.
- QQQ is **−0.88%** at 632.48 (prior close 638.10).
- SOXX is **−1.41%** at 126.81 (prior close 128.62).
- NVDL is **−9.47%** at 13.335 (prior close 14.73).

**Agent orders today:** none so far.

**Your own trades today (agentic account):** you bought **1 NFLX 2027-06-17 60C** at 7.25 (filled 14:30Z) and **3 more SOXL 2026-11-27 32C** at 0.95 (filled 17:55Z). You now hold 5 of the SOXL calls ($863 basis). Both are recorded as yours. The agent never closes them.

## 1. Sleeves (SWING_Q 40% / SWING_M 30%)
*Pre-window snapshot. The decision-window run fills in the orders.*
- **SWING_M holds** the three names bought Monday:

  | Name | Shares | Avg cost | Price 20:16Z | Value | P/L |
  |---|---|---|---|---|---|
  | ILMN | 0.368508 | 205.07 | 201.505 | $74.26 | −$1.31 |
  | VLO | 0.228449 | 330.80 | 324.205 | $74.06 | −$1.51 |
  | MPC | 0.210889 | 358.34 | 347.835 | $73.35 | −$2.22 |

- Legs going into today (from yesterday's close): ILMN IBS (day 4 of 5), VLO RSI2 + IBS (IBS day 5 of 5), MPC RSI2 + IBS (IBS day 4 of 5). The window decides on today's prices.
- **QLD:** QQQ (632.48) is below its 200-day average (about 683.5), so SWING_Q stays flat.
- The other seven picks had no leg on at yesterday's close.
- Today's state (`sleeves_state.json`) is built for 2026-11-25, so the window can trade.

## 2. BBW (NVDL, 20%)
- Flat all day. Every 15-minute candle through 20:00Z showed no entry signal. No trades and no late exits.

## 3. LEVX (10%, live)
- **Last night:** no position (QQQ and SOXX both below their 200-day averages).
- **DAY leg today:** TQQQ never closed above its trigger at a check (the 15:00 check closed at 44.795 against a reference of 46.19, yesterday's close). No trades.
- **Tonight's NIGHT decision (15:46 ET run):** QQQ 632.48 vs its 200-day about 683.5, SOXX 126.81 vs its 200-day about 161.2. Both are below, so expect no night position, target $0.

## 4. Legacy run-off and options
- Legacy book: closed. No agentic options open.
- Your options, marked by the broker at 20:16Z: **$1,640 in total** (NFLX 60C x1, cost $725; SOXL 32C x5, cost $863). **The SOXL calls expire Friday 11-27. Friday is an early close (1:00 PM ET), and Robinhood's sell-out time for that contract is 17:45Z (12:45 PM ET).**

## 5. Growth paper book
- Marked at the 15:01 ET run: $134.68 against $164.01 cost, **−17.9%**. NET −21.7%, CRWD −23.5% (the −25% exit line is 204.34; it is checked Mondays, next 11-30), LLY +1.4%. Two slots are empty.

## 6. Money and drawdown
- Total $2,778.24 = your options $1,640.00 + **sleeve money $1,138.24**. Base $1,081.33, reserve $56.91, cash $916.59, deployable $859.68.
- Sleeves vs QQQ: today +0.01% (QQQ −0.88%); month to date −0.81%; since 2026-09-30 **−9.33%** (QQQ −14.5% from 739.71).
- Drawdown from the 2026-10-09 high-water mark: **−11.28%**. A further $111.84 of sleeve loss reaches the −20% notice; $175.99 reaches the −25% halt.

## 7. Tomorrow and what's due
- **Thursday 11-26: market closed (Thanksgiving).**
- **Friday 11-27 closes at 1:00 PM ET, and the swing sleeves have no decision run that day. This needs your decision before Friday.**
  - `sleeves.py` treats an early close as an ordinary session, so the backtest's fill is Friday's 1:00 PM close.
  - The routine only places swing orders in the 15:20–15:52 ET window, which on Friday comes after the bell. So nothing gets decided at Friday's close.
  - It matters this Friday in particular. Monday 11-30 is November's last trading day, so the turn-of-month leg comes on at Friday's close. That means QLD (about $430) and every pick (about $32 each), roughly $750 in all.
  - With no run, those buys slip to Monday's window, and the sleeves miss Monday's session. Held names (ILMN, VLO, MPC) carry over the weekend whatever their legs say.
  - LEVX already handles early closes: Friday is a morning sell only, with no night entry.
  - **The fix to approve, if you want it:** on early-close days (11-27, 12-24), a decision window of 12:20–12:52 ET. The cron already fires at 11:16, 11:31 and 11:46 CT, so only the prompt and `CLAUDE.md` change, not cron-job.org.
- Turn of the month: TOM is on for Monday 11-30 and the first three December sessions (held through Thursday 12-03's close). December's picks are fixed on Tuesday 12-01.
