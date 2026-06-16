# Session handoff — current working state

> Transient notes to bring a fresh Claude Code session up to speed (terminal,
> phone, or web). The **stable playbook is `CLAUDE.md`**; cron-job.org setup
> detail is in **`docs/cron-job-setup.md`**. Treat anything time-sensitive below
> as "last known" — re-read live state from the tools rather than trusting it.
>
> Last updated: 2026-06-09.

## FMP access
- FMP is now reachable from the Claude-on-the-web remote environment — the
  network allowlist was updated to permit the bare host `financialmodelingprep.com`.
  Confirmed with a live call this session.
- **Use the `/stable` API, not `/api/v3`.** The v3 endpoints now return
  `"Legacy Endpoint ... no longer supported"`. Working examples:
  `/stable/quote?symbol=AAPL`, `/stable/historical-price-eod/full?symbol=AAPL&from=…&to=…`.
  Multi-symbol quote and `batch-quote` are not on the current plan — call per symbol.
- **FMP plan = Starter:** 300 calls/minute, **no daily cap**, 20 GB / 30-day
  bandwidth. Comfortably covers the 3×/day cadence (~217-name scan per run).
- Operational rule from `CLAUDE.md` still stands: for trade decisions, use the
  **committed `latest_*.md` report**, not an ad-hoc local `report.py` run — that
  keeps every session reading the same source of truth. (The "can't reach FMP"
  reason in CLAUDE.md is now environment-specific, but the "use the committed
  report" guidance is unchanged.)

## Scheduling — LIVE (repo + cron-job.org both done)
Goal: reports run on time, Mon–Fri, through market hours — a morning full-scan
baseline then hourly intraday refreshes.

- **Cadence (current):** ONE cron-job.org job firing **hourly, ~09:00–14:00 CT,
  Mon–Fri** (6 runs/day). It sends `mode=auto`; the workflow then picks the mode
  by Central hour: **before 10:00 CT → morning** full scan (baseline + cache →
  `latest_morning.md`); **10:00–14:00 CT → intraday** live-price refresh →
  `latest_intraday.md`. So the 09:00 CT slot is the morning baseline; the five
  later slots are intraday. (Earlier plan was 3 separate mode-specific jobs;
  collapsed to one hourly job — see PR #5.)
- **Primary driver = cron-job.org** hitting the workflow's `workflow_dispatch`
  REST endpoint (on-time and DST-aware). GitHub's own cron is best-effort and was
  firing **hours late**, so it's been reduced to a single daily **backstop**
  (13:00 UTC — pre-market CT, so it's an early baseline the real 09:00 CT run
  overwrites, never a mid-session clobber of `latest_morning.md`).
- **Mode logic:** decided in the workflow's "Determine mode" step. Native cron
  (backstop) is hard-pinned to `morning` so a late fire can never mislabel. An
  explicit `mode=morning|intraday` in the dispatch body overrides the clock (handy
  for tests). `mode=auto` (the hourly job) uses the CT-hour rule above, read in
  `America/Chicago` to match the cron-job.org job's timezone. Trusting the clock
  is safe ONLY because cron-job.org is punctual — the old mislabel bug was
  GitHub's own cron firing hours late across the boundary.
- Merged to `master`: PR #2 (3×/day + delay-proof mode), PR #3 (cron-job.org
  primary + backstop), PR #5 (single hourly job + `mode=auto`), PR #6 (resolve
  `auto` by Central time so the 09:00 CT slot = morning). Full setup steps:
  `docs/cron-job-setup.md`.
- **Setup done (2026-06-09):**
  1. Fine-grained PAT — repo-scoped, Actions: Read and write. ✓
  2. cron-job.org job live: schedule `0 9-14 * * 1-5`, timezone
     **America/Chicago**, POST to the dispatch endpoint with the 4 headers and
     body `{"ref":"master","inputs":{"mode":"auto"}}` (the `ref` is REQUIRED —
     omitting it gives a 422). ✓ Test run returned **HTTP 204**.
- **Optional cleanup** once cron-job.org is proven over a few days: delete the
  `schedule:` block to drop the duplicate backstop scan (the backstop currently
  also refreshes `latest_morning.md`, so leaving it in keeps that file fresh daily
  even if cron-job.org or its token goes down).

## Trade / stops task — IN FLIGHT (specifics held off the public repo)
- A stop-loss tightening task is mid-flight on the agentic cash account. **Re-read
  live state** with `get_accounts` → the Agentic account, then `get_equity_orders`
  / `get_equity_positions`, and confirm specifics with Ryan (he has the details).
- Reminder from the playbook: only **whole-share** positions can hold resting GTC
  stops; **fractional** positions cannot (Robinhood) and are monitored only.
- **One open decision** for Ryan on a whole-share name whose intended new stop
  level went stale intraday (price gapped through it) — confirm the level with him
  before changing that order. Follow the per-order review + explicit-approval
  HARD RULE for any stop change.

## Rebalance cadence — LIVE (process now codified)
- Cadence is per-sleeve (full spec in `CLAUDE.md` → "Rebalance cadence"): swing +
  options are daily/rule-driven (no calendar rebalance); **momentum + concentration
  rebalance MONTHLY**, **legacy QUARTERLY** (Jan/Apr/Jul/Oct).
- **Anchor = first trading day of each month.** `report.py` now prints a
  **`📅 MONTHLY REBALANCE DUE`** banner in the ACTION block on that day (and the
  quarterly legacy-sweep line in Jan/Apr/Jul/Oct), so the ntfy alert reminds the
  session. First-trading-day = first Mon-Fri of the month (ignores holidays — a
  reminder nudge, may land a day early on Jan 1 / Jul 4 weeks).

## Quick open-items checklist
- [x] cron-job.org setup done (PAT, single hourly job, `mode=auto`, test 204).
- [x] Rebalance cadence codified (CLAUDE.md) + monthly nudge in report.py.
- [ ] Ryan: confirm the pending stop-level decision.
- [ ] Optional: remove the GitHub `schedule:` backstop once cron-job.org is proven.
