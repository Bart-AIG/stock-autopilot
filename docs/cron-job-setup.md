# Driving the report schedule from cron-job.org

GitHub's built-in `schedule:` cron is best-effort — it routinely fires minutes to
**hours** late and is occasionally skipped. To get punctual, DST-aware runs we
drive the report from **[cron-job.org](https://cron-job.org)**, which calls the
workflow's `workflow_dispatch` REST endpoint on a precise schedule.

The GitHub workflow keeps **one** native cron purely as a safety-net; cron-job.org
is the real scheduler.

---

## What each cron-job.org job does

It sends an authenticated `POST` to GitHub's "create a workflow dispatch event"
endpoint, passing the report `mode` in the body. A successful trigger returns
**HTTP 204** (no content).

**Endpoint (same for all three jobs):**

```
POST https://api.github.com/repos/Bart-AIG/stock-autopilot/actions/workflows/stock-report.yml/dispatches
```

**Headers (same for all three):**

| Header | Value |
|--------|-------|
| `Accept` | `application/vnd.github+json` |
| `Authorization` | `Bearer YOUR_TOKEN_HERE` |
| `X-GitHub-Api-Version` | `2022-11-28` |
| `Content-Type` | `application/json` |

**Body — one job per slot:**

| Job | Time (ET) | Request body |
|-----|-----------|--------------|
| Morning (full scan) | 10:00 | `{"ref":"master","inputs":{"mode":"morning"}}` |
| Midday refresh | 12:30 | `{"ref":"master","inputs":{"mode":"intraday"}}` |
| Power-hour refresh | 15:30 | `{"ref":"master","inputs":{"mode":"intraday"}}` |

Run them **Mon–Fri** only. Set the cron-job.org job timezone to
**America/New_York** so the ET times track DST automatically (this is the main
win over GitHub's fixed-UTC cron).

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

Each run scans ~217 names ≈ 217 FMP calls. Three runs/day ≈ 650+ calls/day
(more on days the safety-net also fires). Confirm your FMP plan's daily/minute
limits comfortably cover that before relying on it.

## Verifying

- A good trigger returns **204** in cron-job.org's execution history.
- **401/403** = token problem (wrong/expired token, or missing Actions:write).
- **404** = usually a wrong repo path or the token can't see the repo.
- After a 204, a new run appears under the repo's **Actions** tab within seconds,
  and you get the ntfy alert (heartbeat on a no-trade day, high-priority on ACTION).
