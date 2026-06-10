# Stock Autopilot — agent context & REMOTE TRADE-APPROVAL playbook

This file is auto-loaded by any Claude Code session that opens this repo. It exists so a fresh remote session (e.g. Ryan on his phone) has full context and the safety rules, even with no prior memory.

> **Resuming an in-progress session?** Read **`HANDOFF.md`** first (if present) — it carries the current working state and any corrections to the notes below (scheduling, FMP access, in-flight stop tasks).

## What this project is
Read-only daily stock analysis. `report.py` (run by scheduled routines) produces reports through the trading day (a morning full scan then hourly intraday refreshes, ~09:00–14:00 CT, Mon–Fri — see `docs/cron-job-setup.md`) flagging Connors RSI(2) swing setups + a 12-1 momentum ranking (entries), **SELL/EXIT signals on positions in the `holdings.json` ledger**, and auto concentration/sizing analysis. The scripts NEVER trade.

**Dashboard:** the scheduled run also regenerates **`DASHBOARD.md`** (read-only rear-view:
open positions vs stops, spec-sleeve %, closed-trade scorecard from `trade_log.json`).
It is informational only — never a source of trade decisions; use `latest_*.md` for those.

**Exit engine:** the report reads `holdings.json` (the positions ledger) and flags sells. Swing sleeve (classic-fast): RSI2≥70 OR price reclaims the 5-day MA OR target hit OR stop hit OR ~10-trading-day time-stop OR close below the 200-day MA. Momentum sleeve: fell out of the top decile OR below the 200-day MA, plus a "better-play" rotation list. Winners up ≥1R get a trail-your-stop suggestion. These are SIGNALS — confirm with a live quote and approve each sell per the HARD RULES.

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
SELL: <sym> <price> (<exit reasons>) | ...
TRAIL STOP: <sym> <old_stop>-><new_stop> | ...
BUY: <sym> <price> stop <stop> tgt <target> [HELD/SPEC] | ...
```

When a message looks like that, don't ask what he wants — run the flow above:
1. Cross-check against the committed `latest_*.md` (freshness, `DATA ERROR`,
   anything the alert truncated) and reconcile `holdings.json` vs `get_equity_positions`.
2. **SELL lines first** — propose each sell with a live quote, per-order approval.
3. **TRAIL STOP lines** — propose the stop replacement (cancel old GTC stop, place new)
   per-order approval.
4. **BUY lines** — check real buying power via `get_portfolio` (pending deposits are
   usually NOT spendable), then propose 1-2 sized entries. Skip `[HELD]` names unless
   Ryan explicitly wants to add; respect the SPEC-sleeve cap for `[SPEC]` names. Prefer
   whole-share quantities so the position can carry a resting GTC stop (Ryan's stated
   preference).
All HARD RULES below still apply — the alert is the findings, never the approval.

## HARD RULES (do not break, even if asked to "just do it")
1. **Account:** trade ONLY the Robinhood account with `agentic_allowed=true` (nickname "Agentic", a cash account). Confirm it via `get_accounts` every session. NEVER place orders on any other account — the others reject agentic orders anyway.
2. **Per-order approval, always:** for EACH order, first call `review_equity_order`, show Ryan the live quote, estimated shares, and total cost, then WAIT for his explicit "yes" before `place_equity_order`. One order at a time. Never batch-place on a single "yes." Never skip the review.
3. **Order type:** dollar-based **market** orders, `market_hours=regular_hours` (fractional only works this way). If the market is closed, the order queues for the next open — tell Ryan that.
4. **Sizing / risk:** per-name ≤ ~15-20% of account value; total SPECULATIVE-sleeve exposure ≤ ~25% (spec = quantum/nuclear/uranium/space/eVTOL/drones/photonics/AI-infra small caps). Respect settled buying power (cash account: sale proceeds take ~1 day to settle). Keep a cash buffer.
5. **Stops — place them at order time:** every new position should have a stop level (the report gives one). **As soon as a buy fills, immediately place a resting GTC `stop_market` sell on the WHOLE-SHARE portion of that position** (round the filled quantity DOWN to whole shares; e.g. a 2.39-share fill → stop 2 shares). Do this without waiting to be asked — it's part of placing the order. Robinhood resting stops need whole shares, so the fractional remainder (and any position under 1 whole share) can't rest a broker stop — call those out explicitly as **monitored, not automatic**. Confirm the buy actually filled (`get_equity_positions` → `shares_available_for_sells`) before placing the stop sell.
6. **No autonomy:** only act on Ryan's explicit, current instruction for THIS session. Do not place anything speculatively. Scheduled/unattended runs must NEVER trade.

## Typical flow
1. Ryan: "today's report flagged INTC and CCJ; let's do $100 of INTC."
2. You: `get_accounts` → find the agentic account. `get_portfolio` → check buying power. `review_equity_order` (INTC, buy, market, dollar_amount=100, regular_hours) → show quote + est shares + cost + note it's ~X% of the account.
3. Ryan: "yes."
4. You: `place_equity_order` (same params, fresh ref_id). Confirm the fill, then **immediately place the resting GTC `stop_market` sell on the whole-share portion** (HARD RULE 5) and note any fractional remainder as monitored. If he wants more, repeat per order.

## Logging
After any fill, summarize it back to Ryan (symbol, side, $, shares, avg price, order id) so he has a record.

## Keep the positions ledger current (`holdings.json`)
The report's exit engine only sees what's in `holdings.json`, so the trading session MUST keep it in sync with the agentic account:
- **On a BUY fill:** append a position — `symbol`, `sleeve` (`swing` for RSI(2) entries, `momentum` for 12-1 holds, `legacy` for pre-strategy names), `entry_date` (UTC YYYY-MM-DD), `entry_price` (avg fill), `shares`, `stop`, `target` (swing entries carry stop+target+entry_date; momentum/legacy may leave them null).
- **On a SELL fill:** remove that position (or reduce `shares` on a partial), bump `updated_utc`,
  **and APPEND the closed trade to `trade_log.json`** — symbol, sleeve, entry_date, entry_price,
  exit_date (UTC), exit_price (avg fill), shares, pnl (USD), pnl_pct, days_held, exit_reason
  (the report's exit rule, or 'manual'), r_multiple = (exit-entry)/(entry-stop) when a stop existed
  else null. Never edit past entries — it's the performance record the dashboard reads.
- When in doubt, reconcile against `get_equity_positions` so the ledger matches reality, then **commit `holdings.json`** so the next scheduled report evaluates the right book.
