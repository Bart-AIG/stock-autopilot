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

## ⚠️ Routine prompt drift — the stored prompt must be updated by RYAN when run DUTIES change (found 2026-08-11)

Each fire clones the repo fresh and obeys the CURRENT `CLAUDE.md` on `master` for
**rules** (budgets, caps, gates — merging a PR to master is the real update path,
and runs have correctly applied every amendment this way). BUT the routine's
**stored prompt** contains a numbered TASK LIST, and runs execute that list — a
duty that only exists in `CLAUDE.md` gets skipped. That is why the **daily EOD
report (HARD RULE 8, added 2026-08-07) never ran**: `daily_options_report.md` was
never created; the 14:31/14:46 CT runs each day just did "no action" because
step 5 wasn't in their list. The stored prompt also hardcodes stale numbers
($150/15%/−$150/DTE<14 — all superseded), which runs have so far correctly
overridden from CLAUDE.md, but is a latent conflict.

**Fix (Ryan only — agents cannot edit an `http_api`-created routine):** at
claude.ai/code/routines → "Option Autopilot" → replace the prompt with the
current version below. **Maintenance rule: any future CLAUDE.md amendment that
adds or changes a run DUTY (not just a threshold) needs this prompt updated too —
the session making the amendment must remind Ryan with the paste-ready text.**

### Current routine prompt (v2, 2026-08-11)

```
OPTIONS AUTOMATION RUN — read CLAUDE.md HARD RULES 6 & 8 on master FIRST and obey them exactly as the single source of truth: CLAUDE.md's current amendments ALWAYS override anything hardcoded in this prompt (bounded options autonomy; equities are NEVER traded autonomously). Only act if the US market is open (9:30 AM–4:00 PM ET); otherwise stop. Account: the Agentic cash account (agentic_allowed=true) via the Robinhood connector.

1) HEARTBEAT: if automation_heartbeat.json on master isn't stamped today, stamp it and push.
2) EXITS FIRST: manage every open option position per the HARD RULE 8 exit engine as currently written in CLAUDE.md (2026-08-05 exit-method amendment: setup-break primary, DTE-scaled premium backstops, pop-bank + trailing ratchet on winners, 21-DTE review). Honor the placed_agent exit gate (never auto-sell Ryan's own entries) and any manual_hold_override in holdings.json.
3) ENTRIES: max ONE new single-leg long option per run (up to 3/day), only if the FULL HARD RULE 8 pre-trade checklist passes as currently written in CLAUDE.md — including the trend-maturity gate (2026-08-10: project FORWARD — skip late-stage moves, already-priced catalysts, and positions the present tape diverges from; catch turns, never chase a completed trend) — within the $1,500 agentic premium-at-risk budget, settled cash only, −$400 daily loss cap, hard DTE floor 7. Any doubt = skip.
4) LOG: on any fill or state change, update holdings.json (sleeve:"options") and get it onto master (open the PR and merge it — standing instruction). Before ending, diff HEAD vs origin/master and merge any piled-up commits (branch-drift check).
5) DAILY EOD REPORT (HARD RULE 8 duty, 2026-08-07 — do NOT skip): on the FIRST run at or after 14:30 CT each trading day, write the full plain-language daily report to daily_options_report.md on master (overwrite daily): open positions with P/L and thesis refreshers; every action taken today with the full reasoning; every candidate considered and SKIPPED with the specific gate it failed; sleeve state vs the $1,500 budget and −$400 cap; tomorrow's watchpoints. Also push the compact ~10-line version via ntfy: curl -s -H 'Title: Options daily report' -d '<compact report>' https://ntfy.sh/stk-ap-rb-9k4m7q2x — on a zero-activity day a one-line push suffices.

If the broker connector is missing or fails, do nothing and end.
```

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
