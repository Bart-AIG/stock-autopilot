# Stock Autopilot — Setup Kit

**A portable, self-configuring handoff file.** Upload it to Claude and it will
interview you, then build your own copy of the system around your answers.

---

## 🤖 INSTRUCTIONS TO CLAUDE — read this before anything else

You have been handed a **setup kit**, not a document to summarize.

**Do NOT** dump, summarize, or paste this file back at the user. **Do NOT**
generate any config until the interview below is finished.

Do this, in order:

1. **Greet the user in two sentences**: this kit builds a personal stock/options
   analysis-and-trading assistant, and you need to ask about a dozen questions
   first because the settings encode real money decisions that must be theirs.
2. **Run PART 1 — SETUP INTERVIEW.** Ask in the grouped rounds given. If you have
   an interactive question tool (e.g. AskUserQuestion), use it, one round per
   call, with the recommended option listed first. Otherwise ask in plain text,
   one round per message, and wait for an answer before continuing.
3. **Honor these interview rules:**
   - Every question has a **RECOMMENDED** answer. Say which it is and why in one line.
   - The column marked *"Ryan's setting"* is what the person who sent you this kit
     converged on after months of live iteration. Present it as a reference point,
     **never as the default.** Do not steer the user toward it.
   - If the user says "just use the recommended settings for everything," accept
     that and skip to step 4 — but still confirm the four items marked 🔴, which
     are the ones that can lose money fastest.
   - If an answer is riskier than the recommendation, accept it (it is their
     account) and **write it into the generated files with a one-line note that
     it was a deliberate choice above the recommended setting.** Never silently
     soften it, and never editorialize about it more than once.
4. **Run PART 2 — GENERATE**, producing every file listed there with the user's
   answers substituted for every `{{PLACEHOLDER}}`.
5. **Finish with PART 3 — INFRASTRUCTURE CHECKLIST**, the accounts and keys only
   the user can set up. Present it as a numbered to-do list, not prose.

**Honesty requirements while doing this** (these are load-bearing, and the system
you are building enforces the same discipline on itself):
- You are configuring software that can place **real trades with real money**.
  Say so plainly once, at the start, without dramatizing it.
- You are **not** giving investment advice. The recommendations here are about
  *system safety settings* (how much autonomy, how big a cap), not about what to buy.
- If the user seems unsure about a 🔴 item, recommend the more conservative option
  and tell them it can be widened later in one sentence of a config file.
- Do not promise the system makes money. It is a disciplined process, not an edge.

---

## 📋 What this system actually is (for the human reading it)

Three parts that work together:

1. **A daily report** — a Python script scans a few hundred stocks for two
   classic setups (12-1 momentum, Connors RSI(2) oversold-in-uptrend), checks
   your holdings for exits, and warns about concentration. It runs on a schedule
   and commits the report to a private repo. **It never trades.**
2. **A rulebook (`CLAUDE.md`)** — the hard rules any Claude session must follow
   when touching the account: approval requirements, sizing caps, stop policy, a
   mandatory news/thesis check before any trade, and anti-fabrication rules.
3. **An optional automation** — a scheduled Claude routine that reads the report
   and manages the account within strictly bounded limits.

**Prerequisites** (the interview asks about these; nothing works without them):
- A brokerage account that Claude can access via a connector, with agentic
  trading enabled — this system was built against **Robinhood**.
- A **GitHub** account (private repo holds the ledger, reports, and history).
- A **Financial Modeling Prep** API key (Starter tier or better) for market data.
- Optional: a **cron-job.org** account for punctual scheduling, and an **ntfy.sh**
  topic for phone alerts.

> ⚠️ **Start conservative.** The person who built this ran it in
> report-only mode for weeks, then approval-only for months, before allowing any
> autonomous trading. Every widening was paid for by something that went wrong
> first. You can widen any setting later by editing one line.

---

# PART 1 — SETUP INTERVIEW

Ask these in six rounds. 🔴 marks the four questions that most affect how fast
money can be lost.

### Round 1 — Scope: what should it touch?

| # | Question | Options | RECOMMENDED | Ryan's setting |
|---|---|---|---|---|
| 1.1 | Which books do you want? | Equities only / Options only / Both | **Equities only to start** — options add leverage and time decay; add later | Both |
| 1.2 | Do you want a second, watch-only account tracked for buy ideas (no trading)? | Yes / No | **No** unless you actively manage a second account | Yes (joint account) |
| 1.3 | Roughly what is the account worth? (sets sensible dollar caps) | free text | — | ~$4,000 |

### Round 2 — 🔴 Autonomy: what may it do without asking you?

Explain the ladder plainly before asking; most people should start at rung 1.

| Rung | What it means |
|---|---|
| **1. Report only** | It analyzes and alerts. Every trade is placed by you, by hand. |
| **2. Approval required** | It proposes a priced batch of orders; nothing is placed until you reply "approve". |
| **3. Mechanical exits autonomous** | It banks profits on its own (target hit / overbought), but every BUY still needs your approval. |
| **4. Entries + mechanical exits** | It buys signals and banks winners on its own, inside caps. |
| **5. Full** | Adds selling on a broken thesis — judgment calls, unattended. |

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 2.1 🔴 | Autonomy rung for **equities**? | **Rung 2 (approval required)** for the first month | Rung 5 |
| 2.2 🔴 | Autonomy rung for **options**, if trading them? | **Rung 1–2**; options need faster reaction than approval allows, so only go autonomous once you trust the equity side | Autonomous, bounded |
| 2.3 | Should trades it places itself be reported to you daily? | **Yes** — a written daily report explaining every decision and every skip | Yes |

### Round 3 — 🔴 Sizing and loss limits

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 3.1 🔴 | Max % of the account in any one name? | **10–15%** | 15–20% |
| 3.2 | Max % in speculative names (small-cap AI/quantum/space/etc.) combined? | **20%** | 25% |
| 3.3 | Typical dollar size for a new position? | **3–5% of the account** | $400–500 |
| 3.4 🔴 | If trading options: max premium risked on one trade? | **2–5% of the account**, and never more than you would shrug off losing entirely | $1,500 (~35%, deliberately aggressive) |
| 3.5 | If trading options: daily realized-loss cap that stops new entries? | **~5% of the account** | −$400 |
| 3.6 | May it ever use margin / borrowed money? | **No** — hard rule, never overridable | No |

### Round 4 — Risk posture and exits

| # | Question | Options | RECOMMENDED | Ryan's setting |
|---|---|---|---|---|
| 4.1 | Stop-loss policy | (a) Fixed stop under every entry, (b) **No fixed stops; winners get a trailing stop you set in the app; losers are held on thesis and reviewed monthly** | **(b)** — fixed stops under cost basis turn normal pullbacks into realized losses; but it demands you actually do the monthly review | (b) |
| 4.2 | Keep a minimum cash reserve? | % or none | **20–30% cash floor** while learning | 45% (defensive posture) |
| 4.3 | Any sectors to avoid for new buys? | free text | — | Oil/energy de-emphasized |
| 4.4 | Never trade a name with earnings inside the holding window? | Yes / No | **Yes** — a stop cannot protect an overnight gap | Yes |

### Round 5 — Cadence and alerts

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 5.1 | How often should it check during market hours? | **Hourly** (cheaper, plenty for swing trading) | Every 15 min |
| 5.2 | How should alerts reach you? | **Phone push via a free ntfy.sh topic**, or email | ntfy push |
| 5.3 | Report timezone / your local timezone? | — | US Central |

### Round 6 — Identity and plumbing

Ask only for what is needed to fill the templates. **Never ask the user to paste
an API key or password into the chat** — the checklist in PART 3 tells them where
each secret goes.

| # | Question |
|---|---|
| 6.1 | Name to address in reports (first name is fine) |
| 6.2 | GitHub username and the repo name to create (e.g. `dadname/stock-autopilot`) |
| 6.3 | Brokerage account nickname/number that will be the trading account |
| 6.4 | Do they already have: a Claude subscription, a GitHub account, an FMP key? (yes/no each) |

**After Round 6, summarize every choice back in a short table and ask for one
confirmation before generating.**

---

# PART 2 — GENERATE

Produce these files, substituting the user's answers for every `{{PLACEHOLDER}}`.
Where an answer disables a feature (e.g. options off), **omit those sections
entirely** rather than leaving dead rules in place.

### File 1 — `CLAUDE.md` (the rulebook; auto-loads in every session on the repo)

Generate it from this template:

```markdown
# {{NAME}}'s Stock Autopilot — agent context & trade-approval playbook

This file auto-loads in any Claude Code session opened on this repo. It is the
rulebook. Where this file and any stored routine prompt disagree, **the stricter
rule wins.**

## What this project is
Scheduled market analysis for the {{ACCOUNT_NICKNAME}} account. `report.py`
scans the universe for Connors RSI(2) swing setups and 12-1 momentum, judges
every position in `holdings.json`, and writes a report. **The scripts never trade.**

## HARD RULES (do not break, even if asked to "just do it")

1. **Account:** trade ONLY the account with agentic access enabled
   ({{ACCOUNT_NICKNAME}}). Confirm with `get_accounts` every session. Never place
   orders on any other account.

2. **Approval:** {{APPROVAL_RULE}}
   Before any order, show a fresh live quote, the estimated shares, the total
   cost, and the % of the account it represents.

3. **Order type:** dollar-based market orders, regular hours. If the market is
   closed, say so — the order queues for the next open.

4. **Sizing:** per-name ≤ {{PER_NAME_CAP}} of account value; speculative sleeve
   ≤ {{SPEC_CAP}} total; typical new position {{TYPICAL_SIZE}}.
   {{CASH_FLOOR_RULE}}
   **Never use margin.** Size against unleveraged buying power only, and keep a
   small unencumbered reserve so an exit is never blocked.

5. **Stops and exits:** {{STOP_POLICY}}
   Take profits when it makes sense — this is a grow-the-balance account, not
   buy-and-forget.

6. **Autonomy:** {{AUTONOMY_RULE}}
   **Honest limit:** this is not a live tick-by-tick process. It runs when
   invoked — a session or a scheduled check. Sizing and exits must assume gaps
   between runs, and nothing may depend on reacting within seconds.

7. **News / thesis check before EVERY trade:** the report's signal is purely
   technical. Before proposing or placing any buy or sell, search recent news and
   analyst posture, and state a one-line verdict — intact / weakened / broken —
   with sources. A clean technical signal is not a buy if the news says otherwise.
   {{EARNINGS_RULE}}
   {{SECTOR_STEER}}

8. **{{OPTIONS_RULE_HEADER}}**
   {{OPTIONS_RULES}}

9. **Never fabricate an approval.** An automated or scheduled run can never
   claim, quote, or infer permission from the user — no matter how specific the
   claimed message. If a gate needs their OK: stop, write the reason down, and
   notify. Only a genuinely interactive session with a real typed message from
   {{NAME}} clears a flag. If you find a violation flag you did not write, leave
   it and notify — do not adjudicate it in either direction.

10. **Fix problems at the root.** When something recurs — a stale file, a
    misleading signal, a rule that keeps getting re-derived wrong — correct the
    cause, then write the lesson back into this file so the next session inherits
    it. Surfacing the same issue every run means the fix was never made.

## Keeping the ledger honest (`holdings.json`)
- A buy APPENDS a position; a sell REMOVES it. Reconcile against the broker at
  the START of every session and fix drift before acting — a stale ledger fires
  phantom signals forever.
- **The broker is the ledger of record.** Any file that disagrees with the
  broker's positions is wrong by definition, however well-reasoned it reads.
- Ledger edits must land on the default branch, because the scheduled report
  reads that branch.

## Reporting
Write a plain-language {{REPORT_CADENCE}} report: positions and why we own them,
every action taken with the full reasoning, **every candidate considered and
skipped with the specific reason it failed**, and tomorrow's watchpoints. The
skipped section is the most educational part — keep the detail.
```

### File 2 — the scheduled-run prompt (only if autonomy rung ≥ 3)

Generate a stored-routine prompt carrying: who it is and that files are its only
memory; the objective; a governance line saying the repo rulebook wins on any
conflict; the scope of what it may trade; the hard limits from Round 3 as
**absolute laws**; the per-run task list (reconcile against the broker → manage
existing positions → hunt new ones → log → report); and the requirement that
every entry has a written invalidation level before the order is sent.

Include this warning verbatim in the file that carries the prompt:

> **A stored prompt is a separate copy that agents cannot edit.** When the
> rulebook changes, the prompt must be re-pasted by hand or the two drift apart.
> Stamp a version line at the top of the prompt so any run can report which
> version it is actually running.

### File 3 — `holdings.json` seed

```json
{
  "_comment": "Positions ledger. A buy APPENDS, a sell REMOVES. Reconcile against the broker every session; the broker wins any disagreement.",
  "updated_utc": "{{TODAY}}",
  "positions": [],
  "_closed_positions": []
}
```
If the user already holds positions, offer to add each with symbol, entry date,
entry price, shares, and target.

### File 4 — `README.md`
A short plain-English description of what runs, when, and where output lands.

### File 5 — `SETTINGS.md`
A one-page table of every choice made in the interview, with the date. This is
what they read in three months when they wonder why a number is what it is.

---

# PART 3 — INFRASTRUCTURE CHECKLIST

Present as a to-do list. Secrets never go in the chat or the repo.

1. **Create a private GitHub repo** `{{GITHUB_REPO}}`. Private matters — it will
   hold positions and trade history.
2. **Get an FMP API key** (financialmodelingprep.com, Starter tier: 300
   calls/min). Store it as a **GitHub Actions secret** named `FMP_API_KEY` —
   never in a file.
3. **Add the report script and workflow.** Ask the sender for `report.py`,
   `analyze.py`, and `.github/workflows/stock-report.yml`, or have Claude
   regenerate them. The workflow runs on a schedule and commits the report.
4. **Connect the broker to Claude**: claude.ai → Settings → Connectors → add the
   Robinhood connector, and enable agentic trading on **one** account only.
   Confirm in a session that `get_accounts` shows that account as agentic-allowed
   and every other account as not.
5. **Optional — punctual scheduling:** a free cron-job.org job POSTing to the
   workflow's dispatch endpoint beats GitHub's built-in cron, which fires late.
6. **Optional — phone alerts:** pick an unguessable ntfy.sh topic name, install
   the ntfy app, subscribe. Note that ntfy topics are public to anyone who knows
   the name — never put account numbers or dollar balances in an alert.
7. **Optional — scheduled automation:** only if autonomy rung ≥ 3. Create the
   routine at claude.ai/code/routines, paste the generated prompt, attach the
   broker connector and nothing else.
8. **Run report-only for at least two weeks** before enabling any trading. Read
   the daily reports. Check whether you agree with the calls it would have made.
   That is the cheapest tuition you will ever pay.

## After setup — the first-month routine
- **Daily:** read the report. Ask "would I have made that trade?"
- **Weekly:** check the ledger against the broker yourself, by eye, once.
- **Monthly:** review underwater positions and cull broken theses; re-check that
  every sizing cap still matches the account's size.
- **Widen slowly.** One setting at a time, after something specific justifies it.

---

## A closing note for whoever receives this

The rules in here look excessive until the day one of them saves you. Most exist
because something went wrong once: the no-fixed-stops rule came from watching
normal pullbacks get converted into realized losses; the anti-fabrication rule
came from an automated run inventing an approval that was never given; the
broker-is-the-record rule came from a ledger that quietly disagreed with reality
for a week.

Keep the reports. When something surprises you, write down why in the rulebook.
The system gets good by accumulating those, not by being clever on day one.
