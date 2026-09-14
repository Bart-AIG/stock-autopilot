# DAY TRACK — the one-page mechanical spec (set 2026-09-14)

**Authority:** Ryan, REAL live turn 2026-09-14, answering five design decisions: *"1. Let's make the
change. 2. Whichever you recommend is fine. 3. 5-20%. 4. Sure. 5. Let's do it."* Decision 1 lifts
HARD RULE 5's no-stop policy **for DAY TRACK positions only**. Decision 2 picks the index
opening-range system below. Decision 3 sets the risk-per-trade band at 5–20% of equity. Decision 4
accepts the paper phase and the capital priority below. Decision 5 retires the TACTICAL options
track and narrows CORE's catalyst bar.

**Why it exists.** 2026-08-27 → 09-14: 407 market-hours runs, 85 fully-evaluated intraday options
triggers, **zero** options trades, three post-hoc "the vetoed break worked" findings, 22 KB of new
vetoes. The mechanical parts of the system traded; the judgment parts wrote essays. This track is
**executed, not judged**. Every rule below is a number or a formula computable from bars. A run
either fires or it does not. Code: `day_track.py` (pure functions, self-tested). Nothing in this
document may be re-derived, softened or extended by an unattended run; edits come only from an
interactive session with a real Ryan turn.

## The system (adapted 5-minute opening-range trade on QQQ)
| Item | Rule |
|---|---|
| Signal instrument | **QQQ** only. One theme, one trade per day. |
| Opening range | 09:30–09:35 ET, built from **1-minute bars** (max high / min low). Never from a 5-minute bucket (feed-hole bug). |
| Direction | OR bar close > open → **long**; close < open → **short**; body < 10% of range → **no trade today**. |
| Entry | First run at/after 09:35 ET that can act: **market order, whole shares**. Long = buy **QQQ**. Short = buy **PSQ** (1x inverse; no borrow, no margin, no options). |
| Late-entry gate | Skip if price is already **> 0.5 × OR range beyond the OR edge**. A missed entry is never recovered by chasing. |
| Initial stop | The **opposite OR edge**, pushed to **0.1 × ATR14(daily)** if the range is tighter. Placed at the **broker** as a resting `stop_market`, GFD, the same run as the fill. On PSQ, translate: `psq_stop = psq_entry × (1 + stop_dist_pct/100)`. |
| Size | `shares = floor(min(deployable_cash, RISK_PCT × equity ÷ stop_pct) ÷ price)`. Deployable = `unleveraged_buying_power − 0.05 × total_value`. **RISK_PCT starts at 5% (band 5–20, `calibrate.BANDS["day_risk_pct"]`)**. At this account size **cash binds first**; RISK_PCT is the ceiling on risk per trade, not a target. |
| Exits (every run) | **+1R** → stop to breakeven. **+2R** → trail `stop = max(stop, session_high − 1.5 × ATR14(5-min))`, ratchets in the trade's favour only. **Chop:** first run ≥ 12:00 ET with P&L inside ±0.5R → close at market. **Flat:** first run ≥ 15:30 ET → close at market, cancel the stop. **Never overnight.** |
| Daily limit | **One** day trade per trading day. Stop hit = done for the day. |
| Pause | 3 consecutive losing days, or a week at ≤ −3R → **pause for the rest of that week**, escalate in the daily report. Total account value < **$2,600** → pause (cushion over the $2,000 margin-equity minimum). |
| Capital priority | The DAY TRACK claims deployable cash at its entry run. Swing-book entries that day happen **after** the day trade is flat or was skipped. Swing positions are **never** sold to fund a day trade. |

## Phases
- **PAPER (now → graduation).** Every trading day the first run at/after 09:35 ET computes the
  entry with `day_track.plan_entry()` and records the trade **it could actually have taken, at the
  quote it actually saw**, into `day_track_paper.json`. Later runs apply `manage()` against the
  bars and record exits at the stop / chop / flat prices. Paper needs no orders, so it runs under
  prompt v10 with no rule conflict.
- **GRADUATION.** `day_track.graduate()`: ≥ 10 paper trading days **and** ≥ 8 signals **and**
  expectancy > 0 **and** win rate above the payoff-implied breakeven. The Monday calibration
  evaluates it and writes the verdict to `holdings.json._DAY_TRACK`.
- **LIVE.** Requires graduation **and** the run being invoked with prompt **v11** (the stamp on its
  own invocation), because live needs stop-order authority the stored v10 forbids. Live starts at
  RISK_PCT 5; the weekly calibration may move it inside 5–20 **only on in-regime evidence**
  (≥ 20 live day trades, positive margin). The KILL branch (margin ≤ 0 → halve, pause, escalate) is
  exempt from the in-regime gate, as everywhere else.
- **Phase 2 (after ≥ 20 live trades with positive margin):** vehicles TQQQ / SQQQ instead of
  QQQ / PSQ, so risk per trade can approach Ryan's band without margin. Proposed to Ryan, not
  self-granted.

## What a run does (six lines)
1. **09:35–09:50 ET run:** 1-minute QQQ bars → `plan_entry()`. PAPER: log it. LIVE: broker
   pre-check (`get_equity_orders` today — a filled DAY order this run did not place = sibling
   entered, **stand down**), then market buy, then `stop_market` the same minute, then ledger.
2. **Every later run:** re-quote, `manage()`. `raise_stop` → cancel/replace the resting stop.
   `close` → market sell + cancel stop. Log one line.
3. **≥ 15:30 ET run:** flat, no exceptions. If the position vanished (stop filled), reconcile
   from `get_equity_orders`, record the R-multiple, done.
4. **Post-close:** `_DAY_TRACK.results` gains one row (date, direction, entry, exit, reason, R).
5. **Monday calibration:** `edge_stats()` on the DAY rows **separately** from the swing book;
   `graduate()` while in paper; `recommend()` inside `day_risk_pct` once live.
6. **Daily report:** a DAY TRACK section — today's signal, the trade or the skip reason, R, and
   the running paper/live tally. Nothing else is written about this track anywhere.

## What this track is NOT
Not a judgment track. No news check, no regime label, no volume-confirmation clause, no catalyst
screen, no "why now". Those gates produced zero trades in two weeks on the track this replaces;
this one's risk control is the resting stop, the chop rule and the flat rule. If the edge is not
there, `graduate()` and the KILL branch say so with numbers, and the answer is to stop, not to add
a gate.
