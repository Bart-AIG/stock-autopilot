# Stock Autopilot — agent context & REMOTE TRADE-APPROVAL playbook

This file is auto-loaded by any Claude Code session that opens this repo. It exists so a fresh remote session (e.g. Ryan on his phone) has full context and the safety rules, even with no prior memory.

> **Resuming an in-progress session?** Read **`HANDOFF.md`** first (if present) — it carries the current working state and any corrections to the notes below (scheduling, FMP access, in-flight stop tasks).

## What this project is
Read-only daily stock analysis. `report.py` (run by scheduled routines) produces reports through the trading day (a morning full scan then hourly intraday refreshes, ~09:00–14:00 ET, Mon–Fri — see `docs/cron-job-setup.md`) flagging Connors RSI(2) swing setups + a 12-1 momentum ranking, with auto concentration/sizing analysis. The scripts NEVER trade.

## Your job in a remote session: help Ryan APPROVE and PLACE trades

When Ryan says something like "run today's report and let's trade" / "what are today's trades" / "accept the trades":

1. **Get the findings.** Read the latest committed report at the repo root: **`latest_morning.md`** or **`latest_intraday.md`** (whichever is newer / matches the time of day). These are produced by the **GitHub Actions** scheduled job (which has internet + the FMP key) and committed here. **Do NOT run `report.py` in this environment** — it can't reach financialmodelingprep.com (network allowlist) and would produce an empty/invalid report. If the `latest_*.md` is missing, stale, or its header says **`>>> DATA ERROR <<<`**, STOP and tell Ryan — do not trade off a stale or invalid report. (Newest data is also on his ntfy alert; he can paste it.)
2. **Present the proposed orders.** From the report's swing setups, propose concrete orders sized per the rules below (dollar amounts, with the stop level). Show Ryan a short list: ticker, $ size, % of account, stop, one-line reason. Flag the concentration/sizing warnings the report surfaced.
3. **Approve and place, one at a time** — see HARD RULES. Review each, get his explicit "yes", place it, confirm the fill, move to the next.

This makes one phone session self-contained: findings -> approval -> execution.

## HARD RULES (do not break, even if asked to "just do it")
1. **Account:** trade ONLY the Robinhood account with `agentic_allowed=true` (nickname "Agentic", a cash account). Confirm it via `get_accounts` every session. NEVER place orders on any other account — the others reject agentic orders anyway.
2. **Per-order approval, always:** for EACH order, first call `review_equity_order`, show Ryan the live quote, estimated shares, and total cost, then WAIT for his explicit "yes" before `place_equity_order`. One order at a time. Never batch-place on a single "yes." Never skip the review.
3. **Order type:** dollar-based **market** orders, `market_hours=regular_hours` (fractional only works this way). If the market is closed, the order queues for the next open — tell Ryan that.
4. **Sizing / risk:** per-name ≤ ~15-20% of account value; total SPECULATIVE-sleeve exposure ≤ ~25% (spec = quantum/nuclear/uranium/space/eVTOL/drones/photonics/AI-infra small caps). Respect settled buying power (cash account: sale proceeds take ~1 day to settle). Keep a cash buffer.
5. **Stops:** every new position should have a stop level (the report gives one). Fractional positions can't rest broker stops (Robinhood: stops/limits need whole shares) — for those, the stop is monitored, not automatic. Tell Ryan this. For whole-share positions, offer to place a resting GTC stop.
6. **No autonomy:** only act on Ryan's explicit, current instruction for THIS session. Do not place anything speculatively. Scheduled/unattended runs must NEVER trade.

## Typical flow
1. Ryan: "today's report flagged INTC and CCJ; let's do $100 of INTC."
2. You: `get_accounts` → find the agentic account. `get_portfolio` → check buying power. `review_equity_order` (INTC, buy, market, dollar_amount=100, regular_hours) → show quote + est shares + cost + note it's ~X% of the account.
3. Ryan: "yes."
4. You: `place_equity_order` (same params, fresh ref_id). Confirm the fill. If he wants more, repeat per order.

## Logging
After any fill, summarize it back to Ryan (symbol, side, $, shares, avg price, order id) so he has a record.
