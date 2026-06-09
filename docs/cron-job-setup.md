# Driving the report schedule from cron-job.org

GitHub's built-in `schedule:` cron is best-effort — it routinely fires minutes to
**hours** late and is occasionally skipped. To get punctual, DST-aware runs we
drive the report from **[cron-job.org](https://cron-job.org)**, which calls the
workflow's `workflow_dispatch` REST endpoint on a precise schedule.

The GitHub workflow keeps **one** native cron purely as a safety-net; cron-job.org
is the real scheduler.

---

## The cron-job.org job

A **single** job fires **hourly, ~09:00–14:00 ET, Mon–Fri**. It sends an
authenticated `POST` to GitHub's "create a workflow dispatch event" endpoint with
`mode=auto`. The workflow itself then decides morning vs intraday from the Eastern
time of day (first run of the day, before 10:00 ET → `morning` full scan; every
later run → `intraday` live-price refresh). A successful trigger returns
**HTTP 204** (no content).

> **Why one job + `auto`** instead of three mode-specific jobs: one job can only
> send one fixed body, so the *workflow* picks the mode by ET hour. This is safe
> because cron-job.org fires on time — the mislabel bug we fixed earlier was
> GitHub's own cron firing hours late and crossing the morning/intraday boundary.

**Endpoint:**

```
POST https://api.github.com/repos/Bart-AIG/stock-autopilot/actions/workflows/stock-report.yml/dispatches
```

**Headers:**

| Header | Value |
|--------|-------|
| `Accept` | `application/vnd.github+json` |
| `Authorization` | `Bearer YOUR_TOKEN_HERE` |
| `X-GitHub-Api-Version` | `2022-11-28` |
| `Content-Type` | `application/json` |

**Request body** (the `ref` is REQUIRED — without it the API returns **422**):

```json
{"ref":"master","inputs":{"mode":"auto"}}
```

**Schedule:** every hour at minute 0, hours **9–14**, **Mon–Fri**. In a standard
cron expression that's `0 9-14 * * 1-5`. Set the cron-job.org job timezone to
**America/New_York** so those hours track DST automatically (this is the main win
over GitHub's fixed-UTC cron). That yields 6 runs/day: 09:00 (morning) then
10:00/11:00/12:00/13:00/14:00 (intraday).

> Want to force a specific mode for a one-off test, instead of `auto`? Send
> `"mode":"morning"` or `"mode":"intraday"` in the body — the workflow honors an
> explicit mode and skips the time-of-day guess.

---

## The GitHub token

cron-job.org needs a token to trigger the workflow. Use a **fine-grained
Personal Access Token**, scoped as tightly as possible:

- **Resource owner / repository access:** *Only select repositories* →
  `Bart-AIG/stock-autopilot`
- **Repository permissions:** `Actions` → **Read and write**
  (and `Contents` → **Read** if GitHub asks for it)
- **Expiration:** short (e.g. 90 days). Set a calendar reminder to rotate it —
  when it expires, cron-job.org triggers start failing (the safety-net cron is
  your backstop until you rotate).

> Create the token yourself in GitHub → *Settings → Developer settings →
> Fine-grained tokens*. Paste it only into cron-job.org's Authorization header.
> Never commit it or share it in chat.

---

## Safety-net cron

`.github/workflows/stock-report.yml` keeps a single native cron (~16:00 UTC,
Mon–Fri) that runs a morning scan if cron-job.org is down. On a normal day this
**also** fires (late) and produces one duplicate morning scan (~217 FMP calls).
Once cron-job.org is verified for a few days, you can delete the entire
`schedule:` block from the workflow to eliminate the duplicate — `workflow_dispatch`
keeps working.

## FMP usage note

Each run scans ~217 names ≈ 217 FMP calls (intraday adds ~20 live-quote calls).
Six runs/day ≈ ~1,400 calls/day, more on days the safety-net also fires. The FMP
**Starter** plan (300 calls/min, **no daily cap**) covers this comfortably — each
run's calls are spread over ~45s, well under the per-minute limit.

## Verifying

- A good trigger returns **204** in cron-job.org's execution history.
- **401/403** = token problem (wrong/expired token, or missing Actions:write).
- **404** = usually a wrong repo path or the token can't see the repo.
- **422** = the body is missing the required `"ref":"master"` (only `inputs` sent).
- After a 204, a new run appears under the repo's **Actions** tab within seconds,
  and you get the ntfy alert (heartbeat on a no-trade day, high-priority on ACTION).
  The run log's "Determine mode" step prints the resolved mode + ET hour, so you
  can confirm `auto` picked the slot you expected.
