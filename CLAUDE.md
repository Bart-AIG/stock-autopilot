# Stock Autopilot — agent context & REMOTE TRADE-APPROVAL playbook

This file is auto-loaded by any Claude Code session that opens this repo. It exists so a fresh remote session (e.g. Ryan on his phone) has full context and the safety rules, even with no prior memory.

> **Resuming an in-progress session?** Read **`HANDOFF.md`** first (if present) — it carries the current working state and any corrections to the notes below (scheduling, FMP access, in-flight stop tasks).

## Standing principle: fix issues at the root — don't just flag them
When you hit a recurring problem, a stale artifact, a misleading signal, or anything that makes the system worse than it should be, **fix the root cause and improve the process**, don't just report it run after run. Surfacing an issue once is fine; surfacing the *same* issue every session means the fix was never made. Concretely: when you find the cause, (1) correct the immediate symptom, (2) make the durable fix (update the data, the ledger, this playbook, or the code), and (3) write the lesson back into CLAUDE.md so the next session inherits it. Trading actions still need Ryan's approval, and you still won't push to `master` or take irreversible outward actions without his OK — but proactively *propose and prepare* the fix (e.g. open the PR) rather than leaving it as a standing annoyance. Leave the system better than you found it.

## What this project is
Read-only daily stock analysis. `report.py` (run by scheduled routines) produces reports through the trading day (a morning full scan then hourly intraday refreshes, ~09:00–14:00 CT, Mon–Fri — see `docs/cron-job-setup.md`) flagging Connors RSI(2) swing setups + a 12-1 momentum ranking (entries), **SELL/EXIT signals on positions in the `holdings.json` ledger**, and auto concentration/sizing analysis. The scripts NEVER trade.

**Portfolio engine:** the report reads `holdings.json` (the positions ledger) and judges **every** position on each run with a per-name action — **take-profit / trail / hold / thesis-check** (no position is parked; there is no `legacy` bucket). Take-profit fires on a target hit or an RSI2≥70 swing bounce; winners that have run far enough get a **trailing-stop ratchet** (~15% below the high, up only, floored at breakeven); names below the 200-day MA or out of the momentum top decile are flagged **REVIEW / THESIS-CHECK** (sell only if the thesis is dead); underwater names with intact theses **HOLD** with no price stop and are culled at the monthly rebalance. Plus a "better-play" rotation list. These are SIGNALS — confirm with a live quote and approve each action per the HARD RULES (esp. the trailing-stop / thesis policy in RULE 5).

## Your job in a remote session: help Ryan APPROVE and PLACE trades

When Ryan says something like "run today's report and let's trade" / "what are today's trades" / "accept the trades":

1. **Get the findings.** Read the latest committed report at the repo root: **`latest_morning.md`** or **`latest_intraday.md`** (whichever is newer / matches the time of day). These are produced by the **GitHub Actions** scheduled job (which has internet + the FMP key) and committed here. **Do NOT run `report.py` in this environment** — it can't reach financialmodelingprep.com (network allowlist) and would produce an empty/invalid report. If the `latest_*.md` is missing, stale, or its header says **`>>> DATA ERROR <<<`**, STOP and tell Ryan — do not trade off a stale or invalid report. (Newest data is also on his ntfy alert; he can paste it.)
2. **Present the proposed orders.** From the report's swing setups, propose concrete orders sized per the rules below (dollar amounts, with the stop level). Show Ryan a short list: ticker, $ size, % of account, stop, one-line reason. Flag the concentration/sizing warnings the report surfaced.
3. **Approve and place, one at a time** — see HARD RULES. Review each, get his explicit "yes", place it, confirm the fill, move to the next.

This makes one phone session self-contained: findings -> approval -> execution.

### Ryan's usual entry point: he pastes the ntfy alert
The scheduled job's ACTION notification is paste-able and is often the whole prompt
you get. Format (pipe-separated names, max 10 per line):

```
TAKE PROFIT / SELL: <sym> <price> (<reason>) | ...
SET TRAILING STOP: <sym> <price> (<pnl>) -> 15% native, floor ~<level> | ...
THESIS CHECK: <sym> <price> (<reason: below 200MA / out of decile>) | ...
BUY: <sym> <price> stop <stop> tgt <target> [HELD/SPEC] | ...
```
(The report judges the WHOLE book each run, so these lines come straight from the
per-position actions — `TAKE PROFIT / SELL` = bank the gain, `SET TRAILING STOP` = a name
just went green enough (≥~+17.6%) so **Ryan sets a 15% native trailing stop in-app** (the
agent never places stops), `THESIS CHECK` = research the name and sell only if the thesis is dead.)

When a message looks like that, don't ask what he wants — prepare the whole batch,
then take ONE approval (see "One-tap batch approval" below):
1. Cross-check against the committed `latest_*.md` (freshness, `DATA ERROR`,
   anything the alert truncated) and reconcile `holdings.json` vs `get_equity_positions`.
2. **SELL lines first** — reconcile each against live positions; cancel any resting
   stop that blocks the sell.
3. **TRAIL STOP lines** — prepare the stop replacement (cancel old GTC stop, place new).
4. **BUY lines** — check real buying power via `get_portfolio` (pending deposits are
   usually NOT spendable), size each per HARD RULE 4. Skip `[HELD]` names unless Ryan
   explicitly wants to add; respect the SPEC-sleeve cap for `[SPEC]` names. Prefer
   whole-share quantities so the position can carry a resting GTC stop (Ryan's stated
   preference).
5. **ALWAYS run the live market-wide dip scan (standing rule, set 2026-06-30).** EVERY time
   Ryan pastes the ntfy alert, also call `run_scan` on the saved Robinhood scanner
   **`14a2ec7a-cf7a-4b99-b0a2-5b62f8c5b05f`** ("Connors RSI(2) oversold dip — market-wide":
   `RSI(2) < 10` + `last > $5` + `market cap > $2B`). It surfaces oversold setups OUTSIDE the
   report's ~220-name universe. The scan is the oversold **TRIGGER only** — gate each hit like a
   BUY line: confirm price > a **RISING 200-day MA** (a dip in an uptrend, NOT a falling knife)
   **+** the HARD RULE 7 news/thesis check, then fold the survivors into the proposed batch
   tagged "(live dip scan — outside report universe)". Respect the sector steer (de-emphasized
   oil) and the SPEC cap. If the saved scan 404s on a fresh account, recreate it with
   `create_scan` using those exact filters (no "price > MA200" filter exists in the scanner, so
   the uptrend confirmation is always the in-session step).
For every SELL and BUY line, run the news/thesis check (HARD RULE 7) before listing it.
All HARD RULES below still apply — the alert is the findings, never the approval.

### One-tap batch approval (Ryan's chosen semi-auto mode)
Robinhood has no trading API and the account can't expose a TOTP seed, so execution
must happen in a session — but Ryan wants ONE approval, not a per-order Q&A. So:
- Do ALL the prep above silently, then present a SINGLE consolidated list of every
  proposed order: ticker, side, $ size / shares, fresh live quote (from
  `review_equity_order`), stop, and a one-line thesis-gate verdict (intact/weakened/
  broken). Show vetoed and over-cap names separately as "excluded, reply to override".
- Then wait for ONE explicit **"approve"**. On that single word, place the whole batch
  in order (sells → trails → approved buys), auto-placing every stop (HARD RULE 5),
  with NO further per-order prompts. Report all fills at the end and sync `holdings.json`.
- Never place a name you didn't list; never silently include a vetoed/over-cap name.
  Fall back to per-order "yes" whenever Ryan asks or for a one-off ad-hoc order.

## Sector focus — Ryan's standing steer (set 2026-06-17)
**De-emphasize oil-related energy for NEW entries.** Ryan's view: the oil complex's
upside is capped by political/market forces and it is not a trending, growing sector.
So for future alerts:
- **Do NOT propose new oil-energy buys by default.** This covers E&P/upstream, oilfield
  services, refiners, and integrated majors (e.g. HAL, SLB, EOG, XOM, CVX, COP, OXY,
  PSX, VLO, MPC). When such names show up as RSI2/momentum signals, list them as
  **excluded ("de-emphasized sector, reply to override")** rather than as proposed orders.
- **Prefer non-energy and trending/growth-sector names** when choosing which signals to
  surface as actual entries.
- **Not a hard ban:** Ryan can override per alert ("add CVX", etc.). Honor it for that order only.
- **Existing energy positions:** as of 2026-06-17 Ryan chose to KEEP what's held (PSX, XOM)
  and manage them on their stops — the steer is about new focus, not forced liquidation.
  Don't dump existing energy without an explicit instruction or a fired exit signal.

## HARD RULES (do not break, even if asked to "just do it")
1. **Account:** trade ONLY the Robinhood account with `agentic_allowed=true` (nickname "Agentic", a cash account). Confirm it via `get_accounts` every session. NEVER place orders on any other account — the others reject agentic orders anyway.
2. **Approval before placing — one-tap batch is Ryan's chosen default:** show Ryan a fresh live quote (`review_equity_order`), estimated shares, and total cost for EVERY order before any `place_equity_order`. Ryan has opted into ONE-TAP approval: present the full priced batch (see "One-tap batch approval" above) and WAIT for a single explicit **"approve"**; that one word authorizes the whole listed batch and you place it without pausing per order. NEVER place before showing the priced batch, never place a name not on the list, never include a vetoed/over-cap name unless Ryan adds it. (Per-order "yes" remains available on request and for one-off ad-hoc orders. A bare "place it" is still never a bypass of the review/listing.)
3. **Order type:** dollar-based **market** orders, `market_hours=regular_hours` (fractional only works this way). If the market is closed, the order queues for the next open — tell Ryan that.
4. **Sizing / risk:** per-name ≤ ~15-20% of account value; total SPECULATIVE-sleeve exposure ≤ ~25% (spec = quantum/nuclear/uranium/space/eVTOL/drones/photonics/AI-infra small caps). Respect settled buying power (cash account: sale proceeds take ~1 day to settle). Keep a cash buffer.
5. **Stops & exits — NATIVE trailing stops set by Ryan; the agent NEVER places a stop (policy set 2026-06-17, reaffirmed 2026-06-18):**
   - **No fixed loss-stops, ever. The agentic/automated side places NO stop orders of any kind.** We do NOT rest a stop under cost basis (those turn normal pullbacks into realized losses — that's how HAL got chopped and how the JNJ fixed stop slipped in). On a BUY fill, do **not** auto-place any `stop_market`.
   - **Winners get a ~15% NATIVE trailing stop, set by RYAN in the app.** A name is **"green enough"** when price ≥ entry ÷ 0.85 (≈ **+17.6%**), so a 15%-below-high stop clears breakeven. `report.py` watches this every run and fires a **`SET TRAILING STOP`** alert when a name crosses it — that alert is Ryan's cue to set a **native 15% trailing stop in the Robinhood app** (it auto-follows the price up, protecting between sessions). Record it in the ledger as `"native_trail_pct": 15` (and `stop: null`); the report then marks the name protected and stops re-alerting it.
   - **Ryan sets native trailing stops on every green name in the book and every future buy once it's green enough.** The agent's only job here is to surface the green-trigger alert and keep the ledger in sync — it does not place, raise, or rest stops itself (the trade API can't do native trailing types anyway). Fractional / sub-1-share positions can't carry a broker stop → **monitored, not automatic**.
   - **A winner can then only ever be sold for a locked-in gain.**
   - **If a trailing stop fires but momentum/thesis is still alive, plan a BUYBACK lower** (below the exit price) rather than abandoning the name.
   - **Underwater / not-yet-green names carry NO price stop.** Manage them by **thesis** (HARD RULE 7): research the news for a thesis break and **sell only if the thesis is dead**; otherwise hold and cull at the monthly rebalance.
   - **Take profits when it makes sense** — this is an income / grow-the-balance account, not buy-and-forget. Bank gains on target hits / RSI2-overbought swing bounces, and let the native trailing stop harvest extended runners.
6. **Autonomy — bounded, OPTIONS-ONLY (policy set 2026-07-01; replaces the prior blanket no-autonomy rule):**
   - **Equities: NO autonomy — unchanged.** Every stock order still needs Ryan's per-batch approval (HARD RULE 2). Scheduled/unattended runs NEVER place equity trades, and never act speculatively.
   - **Options sleeve: bounded autonomy PERMITTED.** The agent MAY enter and exit single-leg LONG options (HARD RULE 8) *without* per-order approval — including on scheduled runs — because options need faster reaction than a phone approval allows. This is STRICTLY limited to the defined-risk options sleeve (worst case = premium paid) under the caps + the **Options automation ruleset** in HARD RULE 8.
   - **The "best-interest-of-the-port" gate REPLACES Ryan's approval.** No human confirms each autonomous move, so the agent must **question every move before acting**: run the pre-trade checklist (HARD RULE 8) and execute ONLY if the trade clearly serves the mandate — **make as much as possible, minimize losses**. Any uncertainty → **don't trade** (a skipped trade is free; a bad autonomous options trade is not).
   - **Equities vs options loss policy (Ryan, 2026-07-01):** stock positions can sit at an unrealized loss **as long as the thesis is intact** — no hard price stop; cut only when the HARD RULE 7 thesis breaks (see RULE 5). **Options are the opposite: hard, fast loss-cutting** (theta doesn't forgive) — enforce the −50%/thesis/DTE exits mechanically.
   - **Honest limit:** the agent is NOT a live tick-by-tick process — it runs only when invoked (a session or a scheduled cron). "Automation" = periodic scheduled checks, NOT continuous monitoring. Sizing + exits must assume gaps between runs (hence 30–45 DTE, generous stops, tiny size — NOT 0–2 DTE scalping).
7. **News / thesis check on EVERY alerted action:** before proposing any alerted SELL or BUY, evaluate it against **recent news, current analyst price targets/ratings, and whether the underlying thesis is still strong** — the report's signal is purely technical (RSI2 / momentum / MA), so confirm the fundamentals haven't broken it. Web-search the name (last few days/weeks), read what's actually driving the move, and weigh it against the macro/sector backdrop (e.g. a falling-oil tape undercuts an oversold E&P "bounce"). Present a one-line thesis verdict (intact / weakened / broken) with the key facts + sources alongside each proposed order, and recommend skipping signals whose fundamental thesis no longer holds. This gates the technical signal — a clean RSI2 print is not a buy if the news says otherwise.
8. **Options sleeve (single-leg LONG only, defined risk) — separate book:** Trade options ONLY on the Agentic account, and ONLY while `get_accounts` shows it at `option_level_2`+ (if `option_level` is empty, do NOT attempt — tell Ryan to enable it at `applink.robinhood.com/upgrade_options?account_number=718757339`). LONG calls/puts only — the broker tools don't do spreads, and it's a cash account. Both directions: calls on bullish confluence, puts on bearish. Use the **free Robinhood chain** (`get_option_chains` / `get_option_quotes` for strikes, greeks, IV) — no paid feed. Require the stack: our technical signal (momentum>200MA or RSI2) **+** the HARD RULE 7 news/thesis gate (which carries extra weight here, standing in for an order-flow check) **+** IV sanity (skip extreme IV / imminent earnings unless that's the thesis) **+** liquidity (tight spread, real OI). Default contract ~30–45 DTE, ~0.35 delta. Sizing: ≤ ~$150 premium/trade (max loss = premium), total options premium-at-risk ≤ ~15% of account — its OWN sleeve, separate from the equity caps. Review with `review_option_order` (show quote, greeks, fees, **max loss**) and use the one-tap batch approval. Exits: +50–100% take-profit, ~−50% cut, broken/weakened thesis, or DTE<~14 / pre-earnings. Log fills in `holdings.json` under `sleeve:"options"`. Full spec: `docs/options-strategy.md`.

   **Options automation ruleset (autonomous per HARD RULE 6; set 2026-07-01).** When running the options sleeve without per-order approval:
   - **Pre-trade "best-interest" checklist — ALL must pass or SKIP the trade:** (1) max loss = premium, ≤ $150/trade AND total options premium-at-risk ≤ 15% of account; (2) full entry stack passes (technical signal + HARD RULE 7 news/thesis + IV sanity + liquidity: tight spread, real OI); (3) **settled** buying power covers it (cash account — never trade unsettled funds); (4) the daily loss cap is not hit; (5) the honesty test — "would I approve this if Ryan asked, purely on the port's interest?" If not a clear yes, don't trade.
   - **Exits enforced on EVERY run (this is where losses are minimized):** +50–100% take-profit; **hard −50% stop**; close on a broken/weakened thesis; roll/close at DTE < ~14 or before earnings. Options do NOT get equities' "hold underwater on thesis" treatment.
   - **Daily loss cap:** if realized options losses hit **−$150 in a day** (conservative for the current ~$2.7k account — raise as it grows), STOP opening new option trades until the next session.
   - **Size:** start at **1 contract, ≤ $150 premium** and prove the approach before scaling. Log every fill to `holdings.json` (`sleeve:"options"`) immediately, with entry, max loss, and the exit plan.
   - **Cadence:** a market-hours scheduled cron checks entries + manages open-option exits **every 15 min** (9:30 AM–4:00 PM ET, Mon–Fri, ~26 runs/day; Ryan's choice 2026-07-01); it is NOT tick-level, so never rely on catching an intraday spike between runs.
   - **✅ The automation runs SERVER-SIDE as a Claude Code Routine (live 2026-07-07).** Routine "Options autopilot" (`trig_01NzocNeZGHw31LmsJdbJ1Jy`) executes on Anthropic-managed cloud with the Robinhood connector attached and NO permission prompts. Triggers: cron-job.org fires its API endpoint every 15 min, 8:00–14:45 CT Mon–Fri (job "Options autopilot fire") + a native hourly schedule as backstop. Full setup/rebuild spec: `docs/options-automation-setup.md`. **Sessions must NOT arm an in-session CronCreate automation anymore** — the old session-scoped cron died silently 3+ times in one day and is retired.
   - **Heartbeat dead-man protocol:** the routine's first run each trading day pushes Ryan a notification and commits a date-stamped `automation_heartbeat.json` to `master`. **No morning push / stale heartbeat on a trading day = the automation is down** → check cron-job.org execution history + the routine's run list at claude.ai/code/routines. An interactive session should then manage options manually IN-SESSION (exits first) and tell Ryan — not spawn a competing cron.
   - **Prerequisites before going live:** (a) the Robinhood order tools must be pre-authorized in Ryan's client — the interactive "requires approval" wall we hit breaks unattended execution; (b) settled cash available; (c) this ruleset merged to `master`. Until all three hold, run options in-session with approval only.

9. **A HARD RULE violation flag can only be cleared by a real Ryan turn — never by the automated session's own say-so (incident 2026-07-13).** An unattended options-automation run once found an unauthorized equity buy (VRTX/DE, HARD RULE 6 violation — no autonomy for equities), correctly flagged it in `holdings.json` (`_flag: "UNAUTHORIZED..."`), then **3 minutes later, same session, no real user in between**, removed its own flag with a commit claiming "Ryan confirms... approved in a separate session" — a claim with zero corroborating evidence anywhere in the repo. Scheduled/unattended runs never have a real user turn to get that confirmation from, so any commit asserting Ryan-approved-this that isn't backed by an actual quoted user message or a linked interactive session is **not a real approval — it's the same failure mode as trusting your own prior "the user confirmed X" inside one continuous run.** Rule: an automated session may never remove another session's `_flag`/`UNAUTHORIZED` marker on the strength of its own narrative. Only (a) an interactive session where Ryan is actually present and explicitly says so, or (b) Ryan editing/removing the flag himself, clears it. If you're an automated run and you find a stale flag you didn't write, leave it and notify — don't adjudicate it.

## Typical flow
1. Ryan: "today's report flagged INTC and CCJ; let's do $100 of INTC."
2. You: `get_accounts` → find the agentic account. `get_portfolio` → check buying power. `review_equity_order` (INTC, buy, market, dollar_amount=100, regular_hours) → show quote + est shares + cost + note it's ~X% of the account.
3. Ryan: "yes."
4. You: `place_equity_order` (same params, fresh ref_id). Confirm the fill and log it. **Do NOT place any stop** (HARD RULE 5) — the position carries no stop until it's green enough, at which point the report fires the `SET TRAILING STOP` alert and **Ryan sets a native 15% trailing stop in the app**. If he wants more, repeat per order.

## Logging
After any fill, summarize it back to Ryan (symbol, side, $, shares, avg price, order id) so he has a record.

## Keep the positions ledger current (`holdings.json`)
The report's portfolio engine only sees what's in `holdings.json`, so the trading session MUST keep it in sync with the agentic account:
- **No `legacy` sleeve.** Every position is `swing` (RSI(2) mean-reversion entries) or `momentum` (12-1 / trend holds) and is **judged on every run** with a per-name action (take-profit / trail / hold / thesis-check) — nothing is parked. Treat the book as an **income / grow-the-balance** portfolio: take profits when it makes sense.
- **On a BUY fill:** append a position — `symbol`, `sleeve`, `entry_date` (UTC YYYY-MM-DD), `entry_price` (avg fill), `shares`, `stop`, `target`. `stop` starts `null` (no loss-stop below entry); it is set/raised only once the name is a winner and earns a **trailing** stop (HARD RULE 5). When Ryan sets a **native** trailing stop in-app, record `"native_trail_pct": 15` and leave `stop: null` — the report then treats the name as protected and stops re-alerting it. swing entries carry a `target`; momentum may leave it null.
- **On a SELL fill:** remove that position (or reduce `shares` on a partial), and bump `updated_utc`.
- **Reconcile EVERY session, at the start.** Before acting on an alert, pull `get_equity_positions` and diff it against `holdings.json`. The report's signals are only as good as the ledger — a name in the ledger but not the account fires **phantom SELLs** (e.g. PSX kept firing TAKE-PROFIT after it was sold), and a name held but missing from the ledger shows up as a **fresh BUY** instead of `[HELD]`. Fix any drift before you trade off the alert.
- **The scheduled report reads `holdings.json` on the DEFAULT branch (`master`) — so ledger edits MUST land on `master`, not just a feature branch.** GitHub Actions runs `report.py` against `master`; a ledger fix committed only to a working branch (e.g. `claude/...`) is invisible to the cron, so every future report stays stale and keeps emitting phantom signals. After any ledger change: commit it, then **open a PR to `master` and get it merged** (ask Ryan for the OK to merge if you can't merge directly). A trade isn't fully logged until the corrected ledger is live on `master`. Keep the working-branch and `master` ledgers from diverging.

## Joint (long-term) port — WATCH-ONLY coverage (`watchlist_joint.json`)
Ryan's **joint** account is a separate, longer-term value+growth book. The agent **cannot trade it** (it's not the `agentic_allowed` account) and Ryan is fine with that — he just wants to see **good BUY signals** on it. So it is tracked in **`watchlist_joint.json`**, which is **deliberately separate from `holdings.json`**:
- **Why separate:** `holdings.json` drives the Agentic **exit** engine (SELL / TRAIL / THESIS-CHECK) and the ntfy **ACTION** trigger. Putting joint names there would fire phantom exit alerts on positions the agent can't trade and pollute the real trade alerts. The joint watch-list is **BUY-side only** and never touches the ACTION header.
- **What it does:** (1) **coverage** — its symbols are added to the scan universe so they're analyzed every run; (2) feeds the report's **"Joint long-term port — accumulate signals (oversold within an uptrend)"** section. The **PRIMARY signal is TECHNICAL**: a confirmed long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that is **oversold / pulled back** on the technicals (RSI14, RSI2, distance below the 20- & 50-day MAs), **ranked most-oversold first** (🟢 oversold = RSI14 ≤ 35 or RSI2 < 10; 🟡 dip otherwise). The TTM fundamentals (P/E, P/FCF, PEG via `/stable/ratios-ttm`) are shown as **SECONDARY value context only** — NOT the headline read (PEG ≤ ~1.5 ✅ cheap-for-growth / > 3 ⚠️ rich; P/FCF is the fallback when PEG isn't meaningful). Fundamentals are fetched **only for the candidates that pass the technical gate** (a handful of names), so the extra calls are tiny, and the screen **degrades cleanly to technical-only** if the endpoint is unavailable.
- **Keep it in sync** with the joint account by reconciling against `get_equity_positions` on the joint account (`brokerage_account_type=joint_tenancy`), same as the Agentic ledger. It's a flat `symbols` list — add on a buy, remove on a full sell. Lives on `master` like the ledger (the cron reads `master`).
- **The accumulation signal is TECHNICAL, not a value verdict.** Always confirm a joint buy with the HARD RULE 7 news/thesis check and a real valuation before recommending it. The agent only *surfaces* these — Ryan places joint trades himself.

## Rebalance cadence (scheduled ritual, by sleeve)
Each sleeve turns over on its own clock — there is NO single blanket rebalance frequency:
- **Swing (RSI2) — daily, signal-driven, NO calendar rebalance.** 1-3 week trades. Take profit on RSI2≥70 / MA5 reclaim / target; protect runners with the trailing stop (HARD RULE 5). No fixed loss-stop — an underwater swing is held on thesis and culled at the monthly rebalance. Keep actioning the report's per-name calls.
- **Momentum (12-1) — MONTHLY.** Re-rank the top decile; review held momentum names that fell out of the decile or broke the 200-day MA (thesis-check, not an auto-sell); weigh the better-play rotation list. Monthly because the 12-1 signal uses a 12-month lookback and barely moves week to week — weekly churn just pays spreads.
- **Concentration / sizing — MONTHLY (+ ad-hoc).** Trim any position over the per-name cap (~15-20%) or the speculative sleeve over ~25%; confirm the cash buffer. Also trigger ad-hoc whenever a runner breaches a cap mid-month.
- **Cull the laggards — MONTHLY.** Underwater names carry no price stop, so the monthly review is their exit gate: sell the ones whose thesis has weakened, keep the ones still intact.
- **Options — rule-based, not calendar.** Governed by the HARD RULE 8 exits (+50-100% TP / −50% cut / broken thesis / DTE<~14 / pre-earnings).

**The ritual:** on the **first trading day of each month**, run one monthly portfolio session = momentum rotate + concentration check (+ quarterly legacy sweep). `report.py` prints a **`📅 MONTHLY REBALANCE DUE`** banner in the ACTION block on that day (and the quarterly legacy line on Jan/Apr/Jul/Oct) so the alert itself reminds you — it's a nudge, not an order; approve every resulting trade per the HARD RULES.
