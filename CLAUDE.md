# Stock Autopilot — agent context & REMOTE TRADE-APPROVAL playbook

This file is auto-loaded by any Claude Code session that opens this repo. It exists so a fresh remote session (e.g. Ryan on his phone) has full context and the safety rules, even with no prior memory.

> **Resuming an in-progress session?** Read **`HANDOFF.md`** first (if present) — it carries the current working state and any corrections to the notes below (scheduling, FMP access, in-flight stop tasks).

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
TRAIL STOP: <sym> <old_stop>-><new_stop> | ...
THESIS CHECK: <sym> <price> (<reason: below 200MA / out of decile>) | ...
BUY: <sym> <price> stop <stop> tgt <target> [HELD/SPEC] | ...
```
(The report judges the WHOLE book each run, so these lines come straight from the
per-position actions — `TAKE PROFIT / SELL` = bank the gain, `TRAIL STOP` = ratchet the
GTC stop up, `THESIS CHECK` = research the name and sell only if the thesis is dead.)

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
5. **Stops & exits — TRAILING profit-locks, never stale loss-stops (policy set 2026-06-17):**
   - **No fixed loss-stops below entry.** We do NOT rest a stop under our cost basis — those just turn normal pullbacks into realized losses (that's how HAL got chopped). Stale stops are banned.
   - **Winners get a TRAILING stop = ~15% below the running high**, ratcheted **UP only** and **floored at breakeven (entry)**. It only *activates* once a name has run far enough that "15% below high" clears entry (~+18%). Place/raise it as a GTC `stop_market` sell on the **whole-share** portion, and **re-raise it each session** when a new high lifts the level. A winner can then only ever be sold for a **locked-in gain**. (Robinhood has no native trailing order — WE ratchet the fixed `stop_price` up each run. Fractional remainders / sub-1-share positions can't rest a broker stop → **monitored, not automatic**.)
   - **If a trailing stop fires but momentum/thesis is still alive, plan a BUYBACK lower** (below the exit price) rather than abandoning the name.
   - **Underwater / not-yet-trailing names carry NO price stop.** Manage them by **thesis** (HARD RULE 7): research the news for a thesis break and **sell only if the thesis is dead**; otherwise hold and cull at the monthly rebalance.
   - **Take profits when it makes sense** — this is an income / grow-the-balance account, not buy-and-forget. Bank gains on target hits / RSI2-overbought swing bounces, and let the trailing stop harvest extended runners.
   - Confirm a buy actually filled (`get_equity_positions` → `shares_available_for_sells`) before placing any stop sell.
6. **No autonomy:** only act on Ryan's explicit, current instruction for THIS session. Do not place anything speculatively. Scheduled/unattended runs must NEVER trade.
7. **News / thesis check on EVERY alerted action:** before proposing any alerted SELL or BUY, evaluate it against **recent news, current analyst price targets/ratings, and whether the underlying thesis is still strong** — the report's signal is purely technical (RSI2 / momentum / MA), so confirm the fundamentals haven't broken it. Web-search the name (last few days/weeks), read what's actually driving the move, and weigh it against the macro/sector backdrop (e.g. a falling-oil tape undercuts an oversold E&P "bounce"). Present a one-line thesis verdict (intact / weakened / broken) with the key facts + sources alongside each proposed order, and recommend skipping signals whose fundamental thesis no longer holds. This gates the technical signal — a clean RSI2 print is not a buy if the news says otherwise.
8. **Options sleeve (single-leg LONG only, defined risk) — separate book:** Trade options ONLY on the Agentic account, and ONLY while `get_accounts` shows it at `option_level_2`+ (if `option_level` is empty, do NOT attempt — tell Ryan to enable it at `applink.robinhood.com/upgrade_options?account_number=718757339`). LONG calls/puts only — the broker tools don't do spreads, and it's a cash account. Both directions: calls on bullish confluence, puts on bearish. Use the **free Robinhood chain** (`get_option_chains` / `get_option_quotes` for strikes, greeks, IV) — no paid feed. Require the stack: our technical signal (momentum>200MA or RSI2) **+** the HARD RULE 7 news/thesis gate (which carries extra weight here, standing in for an order-flow check) **+** IV sanity (skip extreme IV / imminent earnings unless that's the thesis) **+** liquidity (tight spread, real OI). Default contract ~30–45 DTE, ~0.35 delta. Sizing: ≤ ~$150 premium/trade (max loss = premium), total options premium-at-risk ≤ ~15% of account — its OWN sleeve, separate from the equity caps. Review with `review_option_order` (show quote, greeks, fees, **max loss**) and use the one-tap batch approval. Exits: +50–100% take-profit, ~−50% cut, broken/weakened thesis, or DTE<~14 / pre-earnings. Log fills in `holdings.json` under `sleeve:"options"`. Full spec: `docs/options-strategy.md`.

## Typical flow
1. Ryan: "today's report flagged INTC and CCJ; let's do $100 of INTC."
2. You: `get_accounts` → find the agentic account. `get_portfolio` → check buying power. `review_equity_order` (INTC, buy, market, dollar_amount=100, regular_hours) → show quote + est shares + cost + note it's ~X% of the account.
3. Ryan: "yes."
4. You: `place_equity_order` (same params, fresh ref_id). Confirm the fill, then **immediately place the resting GTC `stop_market` sell on the whole-share portion** (HARD RULE 5) and note any fractional remainder as monitored. If he wants more, repeat per order.

## Logging
After any fill, summarize it back to Ryan (symbol, side, $, shares, avg price, order id) so he has a record.

## Keep the positions ledger current (`holdings.json`)
The report's portfolio engine only sees what's in `holdings.json`, so the trading session MUST keep it in sync with the agentic account:
- **No `legacy` sleeve.** Every position is `swing` (RSI(2) mean-reversion entries) or `momentum` (12-1 / trend holds) and is **judged on every run** with a per-name action (take-profit / trail / hold / thesis-check) — nothing is parked. Treat the book as an **income / grow-the-balance** portfolio: take profits when it makes sense.
- **On a BUY fill:** append a position — `symbol`, `sleeve`, `entry_date` (UTC YYYY-MM-DD), `entry_price` (avg fill), `shares`, `stop`, `target`. `stop` starts `null` (no loss-stop below entry); it is set/raised only once the name is a winner and earns a **trailing** stop (HARD RULE 5). swing entries carry a `target`; momentum may leave it null.
- **On a SELL fill:** remove that position (or reduce `shares` on a partial), and bump `updated_utc`.
- When in doubt, reconcile against `get_equity_positions` so the ledger matches reality, then **commit `holdings.json`** so the next scheduled report evaluates the right book.

## Rebalance cadence (scheduled ritual, by sleeve)
Each sleeve turns over on its own clock — there is NO single blanket rebalance frequency:
- **Swing (RSI2) — daily, signal-driven, NO calendar rebalance.** 1-3 week trades. Take profit on RSI2≥70 / MA5 reclaim / target; protect runners with the trailing stop (HARD RULE 5). No fixed loss-stop — an underwater swing is held on thesis and culled at the monthly rebalance. Keep actioning the report's per-name calls.
- **Momentum (12-1) — MONTHLY.** Re-rank the top decile; review held momentum names that fell out of the decile or broke the 200-day MA (thesis-check, not an auto-sell); weigh the better-play rotation list. Monthly because the 12-1 signal uses a 12-month lookback and barely moves week to week — weekly churn just pays spreads.
- **Concentration / sizing — MONTHLY (+ ad-hoc).** Trim any position over the per-name cap (~15-20%) or the speculative sleeve over ~25%; confirm the cash buffer. Also trigger ad-hoc whenever a runner breaches a cap mid-month.
- **Cull the laggards — MONTHLY.** Underwater names carry no price stop, so the monthly review is their exit gate: sell the ones whose thesis has weakened, keep the ones still intact.
- **Options — rule-based, not calendar.** Governed by the HARD RULE 8 exits (+50-100% TP / −50% cut / broken thesis / DTE<~14 / pre-earnings).

**The ritual:** on the **first trading day of each month**, run one monthly portfolio session = momentum rotate + concentration check (+ quarterly legacy sweep). `report.py` prints a **`📅 MONTHLY REBALANCE DUE`** banner in the ACTION block on that day (and the quarterly legacy line on Jan/Apr/Jul/Oct) so the alert itself reminds you — it's a nudge, not an order; approve every resulting trade per the HARD RULES.
