# Driving the report schedule from cron-job.org

GitHub's built-in `schedule:` cron is best-effort — it routinely fires minutes to
**hours** late and is occasionally skipped. To get punctual, DST-aware runs we
drive the report from **[cron-job.org](https://cron-job.org)**, which calls the
workflow's `workflow_dispatch` REST endpoint on a precise schedule.

The GitHub workflow keeps **one** native cron purely as a safety-net; cron-job.org
is the real scheduler.

---

## The cron-job.org job

A **single** job fires **hourly, ~09:00–14:00 CT, Mon–Fri**. It sends an
authenticated `POST` to GitHub's "create a workflow dispatch event" endpoint with
`mode=auto`. The workflow itself then decides morning vs intraday from the Central
time of day (first run of the day, before 10:00 CT → `morning` full scan; every
later run → `intraday` live-price refresh). A successful trigger returns
**HTTP 204** (no content).

> **Why one job + `auto`** instead of three mode-specific jobs: one job can only
> send one fixed body, so the *workflow* picks the mode by CT hour. This is safe
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
**America/Chicago** so those hours track DST automatically (this is the main win
over GitHub's fixed-UTC cron). That yields 6 runs/day: 09:00 CT (morning) then
10:00/11:00/12:00/13:00/14:00 CT (intraday). The workflow's "Determine mode" step
reads the hour in America/Chicago too, so the schedule and the mode decision stay
in the same timezone.

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

`.github/workflows/stock-report.yml` keeps a single native cron (**13:00 UTC**,
Mon–Fri — pre-market in Central time) that runs a morning scan if cron-job.org
is down. Because it fires before the market opens, it acts as an early baseline
that the real 09:00 CT morning run overwrites; it never clobbers
`latest_morning.md` mid-session. On a normal day it still produces one duplicate
morning scan (~218 FMP calls). Once cron-job.org is verified for a few days, you
can delete the entire `schedule:` block from the workflow to eliminate the
duplicate — `workflow_dispatch` keeps working.

## FMP usage note

Each run scans the universe plus any held symbols not in it (~218 history
calls); intraday also live-quotes every near-trigger name **and every held
position** (a few dozen quote calls). Six runs/day ≈ ~1,500 calls/day, more on
days the safety-net also fires. The FMP **Starter** plan (300 calls/min, **no
daily cap**) covers this comfortably — each run's calls are spread over ~45s,
well under the per-minute limit.

## Verifying

- A good trigger returns **204** in cron-job.org's execution history.
- **401/403** = token problem (wrong/expired token, or missing Actions:write).
- **404** = usually a wrong repo path or the token can't see the repo.
- **422** = the body is missing the required `"ref":"master"` (only `inputs` sent).
- After a 204, a new run appears under the repo's **Actions** tab within seconds,
  and you get the ntfy alert (heartbeat on a no-trade day, high-priority on ACTION).
  The run log's "Determine mode" step prints the resolved mode + CT hour, so you
  can confirm `auto` picked the slot you expected.

---

## Second job: the bottom watch's after-close reading (added 2026-11-20)

The bottom watch (`.github/workflows/bottom-watch.yml`) needs no cron-job.org job for its
intraday readings: it runs by itself right after every Stock Report run on master, so it
inherits the hourly 09:00 to 14:00 CT schedule above.

It does need one for a **punctual after-close reading**. Without it, the confirmed
reading and the daily summary push wait for one of GitHub's own crons, which arrive hours
late (5 to 8 hours on 2026-11-20).

Clone the Stock Report job and change three things:

| Setting | Value |
|---------|-------|
| URL | `https://api.github.com/repos/Bart-AIG/stock-autopilot/actions/workflows/bottom-watch.yml/dispatches` |
| Request body | `{"ref":"master"}` |
| Schedule | `20 15 * * 1-5`, timezone **America/Chicago** (3:20 pm Central, 20 minutes after the close) |

Headers and token stay the same as the Stock Report job (the token needs Actions
read/write on this repository, which it already has). A good trigger returns **204**.
On a half day the reading taken at 3:20 pm is still the confirmed one.

**The request body is the setting a clone gets wrong.** The Stock Report job's body is
`{"ref":"master","inputs":{"mode":"auto"}}`. The bottom watch has no `mode` input, so GitHub
rejects that body with **422** `Unexpected inputs provided: ["mode"]` and creates no run
(measured 2026-11-20 by sending that body to the bottom watch from a session). For this job
the body must be exactly `{"ref":"master"}`.

**Checking it.** A rejected request leaves no trace on GitHub, so from the repository a
failed fire and a job that has not fired yet look the same. A failure shows only in the
job's execution history in cron-job.org. Press TEST RUN there:

- **204**, and a new "Bottom watch" run with event `workflow_dispatch` in the Actions tab
  within seconds = the URL, the body and the token are right.
- **422** = the body (above). **401/403** = the token. **404** = a typo in the URL.
- A test after the close, on a day whose confirmed reading is already recorded, sends no
  push and commits nothing: the run prints "The final reading for <date> is already
  recorded. Nothing to do." and exits. The 204 and the new run are the only signs it worked.
- A test does not prove the schedule or the timezone. Only a `workflow_dispatch` run that
  starts at 3:20 pm Central on a weekday does.

**Status (2026-11-20).** Ryan added the job as "Bottom watch after close". His test run
returned **204** at 23:33:34Z, and Bottom watch run #6 (event `workflow_dispatch`) started on
GitHub in the same second, found the day's confirmed reading recorded, wrote nothing and sent
no push. The schedule preview in cron-job.org showed 3:20 PM, Monday to Friday,
America/Chicago.

**Schedule verified (2026-11-23).** The first scheduled fire arrived on time: run #15 (event
`workflow_dispatch`) started at 21:20:07Z, 3:20:07 pm Central, and wrote the confirmed reading and
the daily summary. The same day a `workflow_run` run followed each of the six Stock Report
runs (runs #9 to #14, 15:15Z to 20:07Z). Health check from now on: a weekday with no
`workflow_dispatch` run of Bottom watch at 3:20 pm Central means this job failed.

The job also fires on market holidays (Thanksgiving, 2026-11-26, is the first). That is
harmless: with no trading that day, the run sees the last session's confirmed reading
already recorded and exits.

## Two dates that stop the cron-job.org GitHub jobs

Both were read from GitHub's response to the 2026-11-20 test run of the bottom watch job.
If the Stock Report job sends the same token and headers, as a clone does, they apply to it
too, and the bottom watch's intraday readings depend on the Stock Report runs.

| Date | What happens | What to do before it |
|------|--------------|----------------------|
| **2027-06-09** 05:00 UTC | The GitHub token expires (`github-authentication-token-expiration` header). Every fire then returns **401**: no hourly Stock Report, so no intraday bottom watch readings, and no punctual after-close reading. Only GitHub's own late crons are left. | Create a new fine-grained token (Actions read and write on this repository) and paste it into the `Authorization` header of every cron-job.org job that calls `api.github.com`. Press TEST RUN on each and expect 204. |
| **2028-03-10** | GitHub ends support for REST API version `2022-11-28`, which the jobs pin in `X-GitHub-Api-Version` (`Sunset` header). A request that names an unsupported version returns **410**. | Change the header to a supported version (`2026-03-10` is the current one, and it has breaking changes). Change the bottom watch job first, press TEST RUN, and change the Stock Report job only after a 204. |

Sources: [REST API version 2026-03-10 is now available](https://github.blog/changelog/2026-03-12-rest-api-version-2026-03-10-is-now-available/)
and [API Versions](https://docs.github.com/en/rest/about-the-rest-api/api-versions).
This is the failure of 2026-08-18 again (the Options autopilot trigger's token died and
nobody saw it for three trading days), so the dates are written down here.
