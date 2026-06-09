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
Goal: reports run on time, 3×/day, Mon–Fri — morning full scan ~10:00 ET,
intraday refresh ~12:30 ET, intraday refresh ~15:30 ET.

- **Primary driver = cron-job.org** hitting the workflow's `workflow_dispatch`
  REST endpoint (on-time and DST-aware). GitHub's own cron is best-effort and was
  firing **hours late**, so it's been reduced to a single daily **backstop**
  (~16:00 UTC) to avoid duplicate FMP scans.
- **Mode bug fixed:** morning-vs-intraday is no longer guessed from the wall
  clock (a late GitHub cron used to cross 17:00 UTC and mislabel a morning run as
  intraday, overwriting `latest_intraday.md`). Dispatch now passes `mode`
  explicitly; any native cron ⇒ morning.
- Merged to `master`: PR #2 (3×/day + delay-proof mode) and PR #3 (cron-job.org
  primary + backstop). Full setup steps: `docs/cron-job-setup.md`.
- **Remaining (Ryan's manual steps):**
  1. Create a GitHub **fine-grained PAT** — repo `Bart-AIG/stock-autopilot` only,
     **Actions: Read and write**, ~90-day expiry. (Account → Developer settings →
     Fine-grained tokens, i.e. https://github.com/settings/personal-access-tokens/new
     — NOT the repo's Settings page.)
  2. Create the 3 cron-job.org jobs (timezone America/New_York) per
     `docs/cron-job-setup.md`.
  3. Test one — expect **HTTP 204**, then a run appears under the Actions tab.
- **Interim:** until those jobs exist, only the single backstop run/day fires
  (fewer than before). Optional once verified: delete the `schedule:` block from
  the workflow to drop the duplicate backstop scan.

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
