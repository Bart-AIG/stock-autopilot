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

## Scheduling — repo side DONE, cron-job.org setup IN PROGRESS
Goal: reports run on time, Mon–Fri, through market hours — a morning full-scan
baseline then hourly intraday refreshes.

- **Cadence (current):** ONE cron-job.org job firing **hourly, ~09:00–14:00 ET,
  Mon–Fri** (6 runs/day). It sends `mode=auto`; the workflow then picks the mode
  by Eastern hour: **before 10:00 ET → morning** full scan (baseline + cache →
  `latest_morning.md`); **10:00–14:00 ET → intraday** live-price refresh →
  `latest_intraday.md`. (Earlier plan was 3 separate mode-specific jobs at
  10:00/12:30/15:30; collapsed to one hourly job — see PR for the auto-mode change.)
- **Primary driver = cron-job.org** hitting the workflow's `workflow_dispatch`
  REST endpoint (on-time and DST-aware). GitHub's own cron is best-effort and was
  firing **hours late**, so it's been reduced to a single daily **backstop**
  (~16:00 UTC) to avoid duplicate FMP scans.
- **Mode logic:** decided in the workflow's "Determine mode" step. Native cron
  (backstop) is hard-pinned to `morning` so a late fire can never mislabel. An
  explicit `mode=morning|intraday` in the dispatch body overrides the clock (handy
  for tests). `mode=auto` (the hourly job) uses the ET-hour rule above. Trusting
  the clock is safe now ONLY because cron-job.org is punctual — the old mislabel
  bug was GitHub's own cron firing hours late across the boundary.
- Merged to `master`: PR #2 (3×/day + delay-proof mode), PR #3 (cron-job.org
  primary + backstop). NEW PR: single hourly job + `mode=auto` time-of-day logic.
  Full setup steps: `docs/cron-job-setup.md`.
- **Remaining (Ryan's manual steps):**
  1. Fine-grained PAT — DONE (repo-scoped, Actions: Read and write).
  2. Merge the auto-mode PR.
  3. Configure the single cron-job.org job: schedule `0 9-14 * * 1-5`, timezone
     **America/New_York**, POST to the dispatch endpoint with the 4 headers and
     body `{"ref":"master","inputs":{"mode":"auto"}}` (the `ref` is REQUIRED —
     omitting it gives a 422). See `docs/cron-job-setup.md`.
  4. Test run — expect **HTTP 204**, then a run appears under the Actions tab; its
     "Determine mode" log line shows the resolved mode + ET hour.
- **Interim:** until the job is live, only the single backstop run/day fires.
  Optional once verified for a few days: delete the `schedule:` block to drop the
  duplicate backstop scan (the noon backstop currently also refreshes
  `latest_morning.md`, so leaving it in keeps that file fresh daily).

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

## Quick open-items checklist
- [ ] Ryan: finish cron-job.org setup (PAT → 3 jobs → test 204).
- [ ] Ryan: confirm the pending stop-level decision.
- [ ] Optional: remove the GitHub `schedule:` backstop once cron-job.org is proven.
