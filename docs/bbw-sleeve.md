# BBW sleeves — 15-minute Bollinger-squeeze strategies, the weekly search, the monthly review

Set 2026-11-01. Code `bbw.py`, tests `test_bbw.py`, state `bbw_state.json`, price cache
`data/intraday15/`. Routine duties: `docs/routine-prompt-v18.md`.

**Authority (Ryan, REAL live turns 2026-11-01):**
- *"just add this as a sleeve to the auto options routine, we also need to always search for
  similar strategys on other names including leveraged variations or others to see if there
  is another that tests well and we should add it"*
- sizing: *"20%, from SWING_Q"* (SWING_Q 70 → 50, SWING_M 30, BBW 20)
- new finds: *"Propose to me, I approve"*
- *"We need a way to remove bad strats or rotate less effective ones for new ones if one starts
  to not perform well. Maybe monthly"*

## The rules (TrendSpider's published "NVDL BBW Strategy", 15-minute bars)

| | Rule |
|---|---|
| Entry | Upper Bollinger band (20, 2) crosses ABOVE the close (price was above the band and closes back inside), AND MACD(19, 39) > 0, AND close > close 10 candles ago, AND a Bollinger-width 15-candle low in the last 5 candles |
| Fill | Next candle's open |
| Stop | Close ≤ entry − 2.5% |
| Trail | Close ≤ highest close since entry − 6% |
| Time | Exit after 50 candles (~2 sessions) any P/L; after 10 candles if losing |

The entry is a **pullback after a breakout**, not a breakout. The other reading ("close crosses
above the upper band") made +32% over the same window against TrendSpider's ~+95%; the literal
reading made +92.9%, so the literal reading is the one TrendSpider ran.

## Evidence (measured 2026-11-01, Robinhood 5-minute bars → 15-minute candles)

Robinhood's real 5-minute history starts 2026-02-23 (earlier bars are interpolated filler), so
the test window is 2026-02-23 → 2026-10-30.

| Symbol | Strategy | Buy & hold | Trades | Win | Max DD |
|---|---|---|---|---|---|
| **NVDL** | **+92.9%** | −5.0% | 23 | 39% | −3.2% |
| NVDA | +35.7% | +6.1% | 22 | 41% | −2.1% |
| SOXL | −1.7% | +10.7% | 24 | 33% | −29.5% |
| TQQQ | −1.9% | +24.4% | 24 | 25% | −17.2% |
| QQQ | +4.7% | +13.5% | 25 | 28% | −4.5% |

- Matches TrendSpider: ~+95–100% over the same window on their chart, 41% wins.
- Stable to the stop and trail (2–3% / 5–7% all gave +90–95%); more sensitive to the 50-candle
  hold (40 → +70%).
- **Concentrated:** without its 3 best trades NVDL makes +30.5%.
- **Overnight risk:** 9 of 10 winners exited on the 50-candle time rule, i.e. held ~2 days. The
  2.5% stop is checked at candle closes, so it cannot stop an overnight gap on a 2x fund
  (NVDA reports 2026-11-17).
- **Does not generalize:** it failed on SOXL, TQQQ and QQQ. Ryan chose to run it with this on
  the table; the weekly search and monthly review exist to catch it if it stops working.

## Cadence: cron-job.org MUST fire every 15 minutes, one minute after each candle closes

Today's job fires at **:25 and :55** (every 30 minutes), which misses half the candles and
evaluates them 10 minutes late. Change the "Options autopilot fire" job on cron-job.org:

| Field | New value |
|---|---|
| Schedule | `1,16,31,46 8-14 * * 1-5` |
| Timezone | America/Chicago |
| Plus a second job (same URL, headers, body) | `1 15 * * 1-5` (the 3:01 PM CT run handles the day's last candle; its order queues for the next open, which is the tested fill) |

That is 25 fires a day instead of ~14. The decision window (15:20–15:52 ET = 2:20–2:52 PM CT)
still gets two fires (2:31 and 2:46 CT). Keep the routine's native hourly backstop. A missed
fire is handled: the next run checks every candle it missed and exits late (and says so); it
never enters on a stale signal. If routine runs start being rejected for volume, tell Ryan:
the fallback is :01/:31 (every 30 minutes), which halves the BBW sleeve's precision.

## Weekly search (Mondays, routine step 4b)

- **Universe** (`bbw_state.json` `universe`): NVDA, AMD, TSLA, AAPL, AMZN, GOOGL, META, MSFT,
  AVGO, PLTR, MU, QQQ, SPY, SMH and their leveraged funds (NVDL, NVDU, AMDL, TSLL, AAPU, AMZU,
  GGLL, MSFU, PLTU, QLD, TQQQ, SPXL, SOXL, USD, TECL). Symbols the connector can't find are
  dropped with a note.
- **Variant family** (kept small on purpose, because every extra variant is another chance to
  find luck): the template, 30- and 80-candle holds, MACD(12,26), a 20-candle squeeze.
- **Out-of-sample discipline:** the best variant is picked on the first 60% of the data and
  judged on the last 40%, which the pick never saw.
- **Pass rules (all):** ≥15 trades (≥6 out of sample); beats buy-and-hold and is positive both
  in and out of sample; still positive without its 3 best trades; drawdown no worse than −15%;
  ≥4 months of data.
- **First run, 2026-11-01:** NVDL passes (out of sample +34.3% vs −8.5%); NVDA passes with the
  80-candle hold (+11.5% vs −1.3%) but shares NVDL's underlying; SOXL, TQQQ, QQQ fail.
- A pass is **proposed to Ryan**, never added by a run.

## Monthly review (first session of the month)

| Verdict | When | What happens |
|---|---|---|
| PAUSE | strategy's live compounded return ≥20% below its own high | **Automatic:** no new entries; open position still exits; Ryan resumes or retires it |
| PROPOSE RETIRE | ≥10 live trades and the average live trade ≤ 0 | Sent to Ryan |
| WATCH | fails the pass rules on recent data | Reported |
| PROPOSE ROTATE | a passing candidate scores ≥10 pts above a WATCH/RETIRE/PAUSE strategy | Sent to Ryan |
| PROPOSE ADD | a passing candidate, room to add | Sent to Ryan (with the same-underlying note) |
| KEEP | otherwise | — |

Only an interactive session with a real Ryan turn edits `strategies` (add, retire, rotate,
resume, re-weight).
