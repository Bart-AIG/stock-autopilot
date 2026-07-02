# Options autopilot — server-side routine + sub-hourly cron-job.org trigger

The options automation runs as a **Claude Code Routine** (claude.ai/code/routines):
a saved prompt that executes as a full Claude session on Anthropic-managed cloud,
with Ryan's claude.ai connectors (incl. Robinhood) attached and **no permission
prompts**. This replaces the old in-session CronCreate job, which died with the
session (observed 2026-07-02: a freshly armed job vanished in ~25 min after a
connection reset).

Design mirrors the report pipeline: **cron-job.org is the precise scheduler**
(routines' built-in schedules have a 1-hour minimum), firing the routine's API
trigger sub-hourly during market hours, with the routine's **native hourly
schedule kept as a backstop** in case the cron-job.org token/job fails.

## The routine (created by Ryan at claude.ai/code/routines — it belongs to his account)

- **Name:** `Options autopilot`
- **Prompt:** the OPTIONS AUTOMATION RUN prompt (heartbeat → exits-first → gated
  single entry → ledger log; obey CLAUDE.md HARD RULES 6 & 8; market-hours guard;
  do nothing if the broker connector is unavailable).
- **Repository:** `Bart-AIG/stock-autopilot` with **Allow unrestricted branch
  pushes** enabled (the ledger + heartbeat must land on `master`).
- **Connectors:** Robinhood (+ GitHub if listed). Remove everything else —
  least privilege.
- **Triggers:**
  1. **Schedule — hourly** (backstop; coarse but keeps the book managed if the
     API trigger dies).
  2. **API** — generates a per-routine URL + bearer token (shown ONCE; store it
     only in cron-job.org).

## The cron-job.org job (sub-hourly precision)

- **URL:** `https://api.anthropic.com/v1/claude_code/routines/<ROUTINE_ID>/fire`
- **Method:** POST
- **Headers:**

| Header | Value |
|---|---|
| `Authorization` | `Bearer <ROUTINE_API_TOKEN>` |
| `anthropic-beta` | `experimental-cc-routine-2026-04-01` |
| `anthropic-version` | `2023-06-01` |
| `Content-Type` | `application/json` |

- **Body:** `{"text":"scheduled sub-hourly options check (cron-job.org)"}`
- **Schedule:** `25,55 8-14 * * 1-5`, timezone **America/Chicago** — :25/:55
  each hour, 8:25–14:55 CT. The 8:25 pre-open fire is absorbed by the routine's
  market-open guard; 14:55 is the near-close management pass. Off the :00/:30
  marks intentionally. ~14 fires/day.
- **Success:** HTTP 200 with a JSON body containing the new session id/URL.
  401/403 = token problem (regenerate in the routine editor, update cron-job.org).

## Limits / operations

- **Every fire starts a real session** that draws subscription usage, and
  routines have a **daily run cap** per account (visible at claude.ai/code/routines).
  If runs start getting rejected, back the schedule off (hourly, or `55 8-14`).
- **Heartbeat:** the routine's first run each trading day stamps
  `automation_heartbeat.json` on `master`. A stale heartbeat on a trading day
  means the automation is down — check cron-job.org history and the routine's
  run list.
- **No in-session cron:** once the routine is live, interactive sessions must
  NOT arm their own CronCreate automation (two automations trading in parallel).
  Sessions verify the heartbeat instead and alert Ryan if it's stale.
- The API `/fire` endpoint is beta (`experimental-cc-routine-2026-04-01`) —
  if fires start failing after a platform change, check the routines docs for a
  new dated header.
