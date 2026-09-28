# Stock Autopilot — Setup Kit (v2, 2026-09-28)

**A portable, self-configuring handoff file.** Upload it to Claude and it will
interview you, then build your own copy of the system around your answers.
The bundled version of this file (`STOCK-AUTOPILOT-KIT.md`) carries every script
and routine prompt in its appendices, so Claude has everything it needs.

---

## 🤖 INSTRUCTIONS TO CLAUDE — read this before anything else

You have been handed a **setup kit**, not a document to summarize.

**Do NOT** dump, summarize, or paste this file back at the user. **Do NOT**
generate any config until the interview below is finished.

Do this, in order:

1. **Greet the user in two sentences**: this kit builds a personal stock/options
   analysis-and-trading assistant plus an optional risk monitor for a second
   account, and you need to ask about a dozen questions first because the settings
   encode real money decisions that must be theirs.
2. **Show them "What this system actually is" and "Honest results so far"** below,
   in your own words, in under 15 lines. They must see the results before choosing.
3. **Run PART 1 — SETUP INTERVIEW.** Ask in the grouped rounds given. If you have
   an interactive question tool (e.g. AskUserQuestion), use it, one round per
   call, with the recommended option listed first. Otherwise ask in plain text,
   one round per message, and wait for an answer before continuing.
4. **Honor these interview rules:**
   - Every question has a **RECOMMENDED** answer. Say which it is and why in one line.
   - The column marked *"Ryan's setting"* is what the person who sent this kit
     runs today. Present it as a reference point, **never as the default.**
   - If the user says "just use the recommended settings for everything," accept
     that, but still confirm the four items marked 🔴.
   - If an answer is riskier than the recommendation, accept it (it is their
     account) and **write it into the generated files with a one-line note that
     it was a deliberate choice above the recommended setting.** Never silently
     soften it, and never editorialize about it more than once.
5. **Run PART 2 — BUILD**, using the appendix files, substituting the user's
   answers for every `{{PLACEHOLDER}}`.
6. **Finish with PART 3 — INFRASTRUCTURE CHECKLIST** as a numbered to-do list.

**If the user already has this system running** and uploaded the kit to change
something, skip the interview. Ask what they want to change, find the matching
section in the appendices, and make the edit in their repo (or give them the
exact text to paste if it lives in a stored routine prompt, which agents cannot
edit).

**Honesty requirements while doing this** (the system enforces the same on itself):
- You are configuring software that can place **real trades with real money**.
  Say so plainly once, at the start, without dramatizing it.
- You are **not** giving investment advice. The recommendations here are about
  *system safety settings* (how much autonomy, how big a cap), not what to buy.
- If the user seems unsure about a 🔴 item, recommend the more conservative option
  and tell them it can be widened later by editing one line.
- Do not promise the system makes money. The results section says why.

---

## 📋 What this system actually is (for the human reading it)

Five parts, all driven by files in one private GitHub repo:

1. **A daily report** (`report.py` + a GitHub Actions schedule). Scans ~220 liquid
   US stocks, gives each a **quality grade** (12 trend/strength traits, A+ to C),
   flags **buy setups** only when a top-graded "leader" pulls back, judges every
   held position for exits, and commits the report to the repo. **It never trades.**
2. **A rulebook (`CLAUDE.md`)**. Hard rules any Claude session must follow:
   which account, approval, sizing, stop policy, a news/thesis check before every
   trade, and anti-fabrication rules. It auto-loads in every session on the repo.
3. **The Autopilot routine** (a scheduled Claude Code routine with the Robinhood
   connector). Every 15-60 minutes in market hours it reconciles the account,
   manages positions, and, within strict caps, buys the report's signals and
   trades a small options "bucket". It writes a daily plain-English report.
4. **The Day Track** (inside the Autopilot, optional). A purely mechanical QQQ
   opening-range day trade with a broker-resting stop. It runs on **paper** until
   it proves itself (10 days, 8 signals, positive expectancy).
5. **The Risk Watch routine** (separate, optional, **advisory only**). Reads the
   user's Robinhood price alerts on market benchmarks (SPY, QQQ, credit, rates,
   volatility), grades market risk GREEN / YELLOW / ORANGE / RED every hour, checks
   the health of each holding in a second (long-term) account, and sends **sell
   recommendations** plus a staged **de-risk and reinvest plan** by phone. It never
   places an order on that account.

### How a trade decision is made (the current process)
- **Which names:** the quality grade. A/A+ = top 10% of the universe, at least 9
  of 12 traits, and beating SPY over 3 months. Only A/A+ names may be bought.
- **When:** an A/A+ name dips (RSI(2) < 10) or pulls back to its 21-day EMA while
  still above its 50-day. A dip on a B/C name is not a setup.
- **Exits:** (a) take profit when RSI(2) ≥ 70 while the position is green; (b)
  **grade exit**: sold when the name drops out of the top 25%, green or red; (c)
  once up ~17.6%, the owner sets a 15% native trailing stop in the Robinhood app;
  (d) sell if the news shows the thesis is broken. The agent never places stops on
  swing positions.
- **Sizing:** 3-4 concurrent positions, size = deployable cash ÷ open slots, max
  30% per name, no entry under ~$600, 5% cash reserve, **never margin**.
- **Options:** a fixed bucket (20% of the account), max half of it on one trade,
  calls only on A-graded names, puts only on the weakest names or SPY/QQQ as a
  hedge. If the bucket loses 40% from its start, new option trades stop until a
  monthly review.

### Prerequisites
- **Robinhood** with an **agentic trading account** enabled (the connector only
  trades an account marked `agentic_allowed`). Options level 2+ if trading options.
- **Claude** plan with Claude Code on the web and Routines (claude.ai/code).
- **GitHub** account (private repo holds the ledger, reports and history).
- **Financial Modeling Prep** API key (Starter tier or better) for market data.
- Optional: **ntfy.sh** (free phone alerts), **cron-job.org** (punctual scheduling).

---

## 📉 Honest results so far (read before choosing settings)

From the broker's own records on Ryan's ~$3,300-4,000 agentic account, 3 months to
2026-09-24:

| Book | Result |
|---|---|
| Equities (old RSI(2) dip-buying process) | ~+$6 over 49 closed trades. After full autonomy began 2026-08-26: 9 closes, 2 wins, **−$219** |
| Options | **−$572** (average loss 1.4× average win) |
| Account | ~$4,000 → **$3,319** |

Why the process changed on 2026-09-25: the old screen kept buying slow, unloved
defensive stocks because they were "oversold". The new quality grade is built on
well-researched factors (12-month momentum, nearness to the 52-week high), but
**this exact combination has no backtest and no live track record yet.** Treat it
as an experiment. That is why the recommendations below start at report-only or
approval-required, and start options off.

---

# PART 1 — SETUP INTERVIEW

Ask these in seven rounds. 🔴 marks the four questions that most affect how fast
money can be lost.

### Round 1 — Scope

| # | Question | Options | RECOMMENDED | Ryan's setting |
|---|---|---|---|---|
| 1.1 | Which books? | Equities only / Options only / Both | **Equities only to start** | Both |
| 1.2 | Run the Day Track? | Off / Paper only / Live after paper graduates | **Off or paper only** | Paper, live on graduation |
| 1.3 | Run the Risk Watch on a second (long-term) account? | Yes / No | **Yes** if they hold a second account they manage themselves; it never trades | Yes (joint account) |
| 1.4 | Roughly what is the trading account worth? And the second account? | free text | — | ~$3,300 / ~$93,000 |

### Round 2 — 🔴 Autonomy

Explain the ladder plainly before asking; most people should start at rung 1-2.

| Rung | What it means |
|---|---|
| **1. Report only** | It analyzes and alerts. The owner places every trade by hand. |
| **2. Approval required** | It proposes a priced batch; nothing is placed until the owner replies "approve". |
| **3. Mechanical exits autonomous** | It banks profits and runs grade exits on its own; every BUY needs approval. |
| **4. Entries + mechanical exits** | It buys A/A+ signals and runs exits on its own, inside caps. |
| **5. Full** | Adds selling on a broken thesis: judgment calls, unattended. |

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 2.1 🔴 | Autonomy rung for **equities**? | **Rung 2** for at least the first month | Rung 5 |
| 2.2 🔴 | Autonomy rung for **options**? | **Off, or rung 1-2.** Options need faster reaction than approval allows, so autonomy there is only for someone who already trusts the equity side | Autonomous, bounded |
| 2.3 | Daily written report of every decision and skip? | **Yes** | Yes |

### Round 3 — 🔴 Sizing and loss limits

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 3.1 | How many concurrent stock positions? | **4-6** at small size while learning | 3-4 (concentrated) |
| 3.2 🔴 | Max % of the account in one name? | **15%** | 30% |
| 3.3 | Minimum entry size (below it, skip the trade)? | **~10% of the account** | ~$600 |
| 3.4 🔴 | Options bucket (% of account reserved for options) and max per trade? | **10% bucket, max half per trade**, or options off | 20% bucket, 50% per trade |
| 3.5 | Options pause: stop new option entries after the bucket loses what %? | **30%** | 40% |
| 3.6 | Daily realized options loss that stops new entries for the day? | **~5% of the account** | −$400 |
| 3.7 | May it ever use margin? | **No, never** (hard rule) | No |

### Round 4 — Exits and posture

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 4.1 | Stop policy for stock swings | **No fixed stops; grade exit + take-profit + a 15% trailing stop the owner sets in-app once up ~17.6%** (explain: fixed stops under cost turn normal pullbacks into losses, so the grade exit is the loss discipline) | Same |
| 4.2 | Cash reserve | **5% of account value, always** (so an exit never fails) | 5% |
| 4.3 | Sectors to avoid for new buys? | free text | Oil/energy de-emphasized |
| 4.4 | Never buy with earnings inside the holding window? | **Yes** | Yes (absolute) |

### Round 5 — Risk Watch (skip if 1.3 = No)

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 5.1 | Which benchmark alerts? | **Start with Ryan's set** (table below) and adjust | Table below |
| 5.2 | "Core" names that should only ever be trimmed, never sold out? | free text | GOOGL, AMZN, META, NOW, ADBE, RBRK, V, JPM, QQQI, MSFT, ZTS, ISRG |
| 5.3 | Build a staged de-risk / reinvest plan on the QQQ levels? | **Yes** | Yes |
| 5.4 | Is margin currently used in that account? (the plan pays it off first) | yes/no | Yes |

**Ryan's benchmark alerts** (Robinhood price alerts; the Risk Watch reads whatever
is live, so these are a starting point, and the levels must be re-set to today's
prices):

| Alert | What it signals | Weight |
|---|---|---|
| SPY below its 50-day SMA | Early trend damage | 1 |
| SPY below ~−5% / ~−10% levels | Real drawdown | 2 (+1 below ~700) |
| QQQ below range top (733) | Rally stalling | 1 |
| QQQ below 20-day SMA / 50-day SMA | Short / medium trend turns down | 1 each |
| QQQ below range floor (700) | Uptrend broken | 2 |
| QQQ below 200-day (~666) | Bear-market regime; also the first REINVEST level | 3 |
| HYG below support | Credit stress (often leads stocks) | 2 |
| KRE below support | Regional-bank / funding stress | 2 |
| VIXY above level | Volatility spike | per code |
| IEF below / above levels | Rates rising / flight to safety | 1 |
| TIP below level | Real yields rising | 1 |
| USO above level | Oil shock | per code |

Tiers from the summed score: GREEN 0-1, YELLOW 2-3, ORANGE 4-6, RED 7+.

### Round 6 — Cadence and alerts

| # | Question | RECOMMENDED | Ryan's setting |
|---|---|---|---|
| 6.1 | How often should the Autopilot check in market hours? | **Hourly** | Every 15 min + hourly backstop |
| 6.2 | How should reports reach them? | **ntfy.sh phone push** (via GitHub Actions) | ntfy |
| 6.3 | Local timezone? | — | US Central |

### Round 7 — Identity and plumbing

**Never ask the user to paste an API key or password into the chat.**

| # | Question |
|---|---|
| 7.1 | Name to address in reports |
| 7.2 | GitHub username and repo name to create (e.g. `dadname/stock-autopilot`) |
| 7.3 | Robinhood account number of the agentic (trading) account; and of the second account if using the Risk Watch |
| 7.4 | Do they already have: Claude with Claude Code, GitHub, an FMP key, the ntfy app? |

**After Round 7, summarize every choice in a short table and get one confirmation
before building.**

---

# PART 2 — BUILD

Work in a Claude Code session on the user's new repo (claude.ai/code). Create
these files, substituting answers for every `{{PLACEHOLDER}}`
(`{{NAME}}`, `{{AGENTIC_ACCOUNT_NUMBER}}`, `{{JOINT_ACCOUNT_NUMBER}}`,
`{{NTFY_TOPIC}}`, `{{OWNER_EMAIL}}`, `{{GITHUB_OWNER}}/{{REPO}}`). Where an answer
turns a feature off, **omit those sections entirely** rather than leaving dead rules.

1. **Code** (Appendix A): copy `report.py`, `analyze.py`, `grade.py`,
   `calibrate.py`; add `day_track.py` + `docs/day-track-spec.md` only if the Day
   Track is on; add `risk_watch.py` only if the Risk Watch is on. Copy the
   workflows into `.github/workflows/` (`stock-report.yml` always;
   `eod-report-notify.yml` if reports go by ntfy; `joint-risk-notify.yml` if the
   Risk Watch is on). Leave the code logic unchanged; only placeholders and
   comments change. In `risk_watch.py`, set the `CORE`, `HIGH_BETA` and `SEMIS`
   sets to the second account's names (they are Ryan's today). Adjust `UNIVERSE` in
   `analyze.py` only if asked.
2. **`CLAUDE.md`** from the template in PART 2a below.
3. **Routine prompt for the Autopilot** (Appendix B), saved as
   `docs/routine-prompt-v1.md`. Appendix B is Ryan's live prompt with his
   identifiers removed. Adapt it: set the account size, bucket %, caps, position
   count and minimum entry from the interview; delete references to Ryan's own
   history (dated incidents, his SPY hedge put, "since 2026-08-26"); remove the
   options book if options are off and the Day Track section if it is off; set
   autonomy to the chosen rung (rung 1-2: replace the autonomous-entry language
   with "propose a priced batch and wait for approval"). **Change line 1 to
   `... (prompt v1, <today>)`** so every run can report which version it runs.
   Put this warning at the top of the file, above the prompt:
   > A stored routine prompt is a separate copy that agents cannot edit. When the
   > rulebook changes, re-paste it by hand or the two drift apart. The version
   > stamp on line 1 is how a run reports which copy it is actually running.
4. **Routine prompt for the Risk Watch** (Appendix C) as
   `docs/risk-watch-prompt.md`, with the second account's number filled in.
5. **Seed state files:**
   - `holdings.json`: `{"_comment": "Positions ledger. A buy APPENDS, a sell REMOVES. Reconcile against the broker every session; the broker wins any disagreement.", "updated_utc": "<today>", "positions": [], "_closed_positions": [], "_OPTIONS_BUCKET": {"start_utc": null, "start_bucket_usd": null, "realized_pnl_usd": 0, "pause_threshold_pct": <3.5 answer>}}`. Offer to add current positions (symbol, sleeve `swing`, entry date, entry price, shares).
   - `watchlist_joint.json`: `{"symbols": [<second-account tickers>]}` (Risk Watch only).
   - `joint_risk_state.json`: `{"last_checked_utc": null, "tier": "GREEN", "score": 0, "readings": [], "last_notified_utc": null, "last_notified_tier": null, "derisk_stage": 0, "reinvest_tranche": 0}`.
   - `day_track_paper.json`: `{"trades": []}` (Day Track only).
6. **`joint_derisk_plan.json`** (Risk Watch + 5.3 = yes): build it from the
   second account's LIVE positions (`get_equity_positions` + `get_portfolio` +
   quotes) in the shape of Appendix D. Stages are cumulative: stage 1 pays off
   margin with losing non-core names (tax-loss harvest, sell all shares so
   recent lots do not create a wash sale); stage 2 trims the biggest
   concentration; stage 3 trims high-beta names; stage 4 trims core overweights
   (never below a set weight). Reinvest tranches at the 200-day and ~−15% / ~−20%
   from the high, index income fund first. Express sells in **shares**, with $ only
   as an estimate at today's prices. Check tax lots (short vs long term) on gains.
7. **`README.md`** (what runs, when, where output lands) and **`SETTINGS.md`**
   (every interview answer with the date: this is what they read in three months).
8. Run `python -m py_compile *.py`, commit, and push to the default branch.

### PART 2a — `CLAUDE.md` template

Keep the rule numbering: the routine prompt cites HARD RULES 5-9 by number.

```markdown
# {{NAME}}'s Stock Autopilot — agent context & trade-approval playbook

Auto-loads in any Claude Code session on this repo. It is the rulebook. Where this
file and a stored routine prompt disagree, **the stricter rule wins.**

## What this project is
`report.py` (GitHub Actions, trading days) grades ~220 stocks on 12 quality traits,
flags buy setups when an A/A+ leader pulls back, judges every position in
`holdings.json`, and commits `latest_morning.md` / `latest_intraday.md`.
**The scripts never trade.** Do NOT run `report.py` inside a Claude session
(no market-data network access there); read the committed report instead.

## QUALITY-GRADE PROCESS
1. GRADE: A/A+ = top 10% of the universe AND >= 9/12 traits AND beating SPY over
   3 months (A+ = 11-12). B = top 25%. C = neither. Only A/A+ may be bought.
2. TRIGGER: RSI(2) < 10, or within +1% of the 21 EMA while above the 50 SMA with
   RSI(2) < 50. A dip on a B/C name is not a setup.
3. EXITS: RSI(2) >= 70 take-profit on a GREEN position; GRADE EXIT when a held
   name leaves the top 25% (green or red); owner-set 15% native trailing stop
   once price >= entry / 0.85; thesis sells per HARD RULE 7.
4. OPTIONS BUCKET: {{BUCKET_PCT}}% of total_value reserved; per trade max
   {{PER_TRADE_PCT}}% of the bucket; pause new option entries if bucket realized
   P/L reaches -{{PAUSE_PCT}}% of its start. State in holdings.json._OPTIONS_BUCKET.
5. The grade has no backtest. Do not tune its thresholds before 20 closes under it.

## HARD RULES
1. **Account:** trade ONLY account {{AGENTIC_ACCOUNT_NUMBER}} (agentic_allowed).
   Confirm with `get_accounts` every session. Never place orders elsewhere.
2. **Approval:** {{APPROVAL_RULE}} Before any order show a fresh quote
   (`review_equity_order`), shares, cost and % of account.
3. **Orders:** dollar-based market orders, regular hours.
4. **Sizing:** {{POSITIONS}} concurrent positions; size = deployable ÷ open slots;
   deployable = unleveraged_buying_power − 0.05 × total_value − unused options
   bucket; per-name cap {{PER_NAME_CAP}}%; minimum entry ${{MIN_ENTRY}} (below it,
   skip). **No margin, ever:** never deploy beyond `unleveraged_buying_power`.
   Earnings inside the hold window = no entry.
5. **Stops:** the agent never places a stop on a swing position. Winners get the
   owner's native 15% trail. {{DAY_TRACK_STOP_EXCEPTION}}
6. **Autonomy:** {{AUTONOMY_RULE}} Autonomous trades come only from the committed
   report's signals. Positions the owner bought himself (`placed_agent: "user"`)
   are never sold autonomously: detect, record, notify once, wait. The agent is
   not a live process; it runs only when invoked.
7. **News / thesis check before EVERY trade:** search recent news and analyst
   posture; one-line verdict intact / weakened / broken with sources. {{SECTOR_STEER}}
8. **Options:** {{OPTIONS_RULES}} Long single legs only, or debit verticals legged
   long-leg-first / short-leg-out-first (the agentic API rejects multi-leg
   tickets, and `review_option_order` falsely accepts them). No naked shorts ever.
   DTE floor 7. Liquidity: bid/ask within 10% of mid on the monthly expiry.
   Daily realized loss of ${{DAILY_LOSS_CAP}} stops new option entries (never exits).
9. **Never fabricate an approval.** A scheduled run can never claim or quote the
   owner's permission. If a gate needs his OK: skip, write why, notify once. Only
   a real typed message from {{NAME}} in an interactive session clears a flag.

## Operating rules (learned the hard way)
- **The broker is the ledger of record.** Reconcile `holdings.json` against
  `get_equity_positions` at the start of every run; the broker wins.
- **Re-read the broker immediately before any order** (`get_equity_orders` for
  today). Two scheduled runs can overlap; the repo lags a sibling's fill.
- **Start every run with** `git fetch origin master && git checkout -B <branch> origin/master`,
  and before committing check `git diff --stat origin/master` shows only files you
  meant to change. A stale clone can silently overwrite newer files.
- **Match each JSON file's existing indent** when writing it back.
- **"Today" is the US trading day (ET).** Post-close runs do not reset daily caps.
- **Daily report:** first run at/after 2:15 PM CT writes `daily_options_report.md`
  (committing it IS the delivery). Include every skipped candidate and why.
- **Weekly calibration** (first run Monday): `calibrate.py` on broker trade history,
  equities and options separately; adjust only inside bands; escalate the rest.
- **Fix problems at the root** and write the lesson back into this file.

## Risk Watch (second account, ADVISORY ONLY)
Routine "Risk watch" runs `docs/risk-watch-prompt.md` hourly. It reads the owner's
benchmark alerts, grades risk with `risk_watch.grade()`, checks each holding with
`holding_health()`, resolves the staged plan in `joint_derisk_plan.json` with
`derisk_stage()`, and commits `joint_risk_report.md` only on a change.
**It never places an order on any account.**
```

---

# PART 3 — INFRASTRUCTURE CHECKLIST

Present as a numbered to-do list. Secrets never go in the chat or the repo.

1. **Create a private GitHub repo** `{{GITHUB_OWNER}}/{{REPO}}`.
2. **Get an FMP API key** (financialmodelingprep.com, Starter tier) and save it as a
   GitHub Actions secret named `FMP_API_KEY` (repo → Settings → Secrets → Actions).
3. **Enable Actions** and run the "stock-report" workflow once by hand; confirm
   `latest_morning.md` appears in the repo.
4. **Robinhood:** turn on an agentic account; in claude.ai → Settings → Connectors,
   add the Robinhood connector. In a session, confirm `get_accounts` shows ONLY the
   trading account as `agentic_allowed`.
5. **Phone alerts:** install the ntfy app and subscribe to a long random topic name
   (`{{NTFY_TOPIC}}`). Topics are public to anyone who knows the name, so reports
   must never carry account numbers.
6. **Autopilot routine** (only if autonomy is on or they want scheduled reports):
   claude.ai/code/routines → new routine → attach the repo and the Robinhood
   connector → paste the prompt block from `docs/routine-prompt-v1.md` → schedule
   (e.g. hourly, market hours, Mon-Fri).
7. **Risk Watch routine** (if on): new routine → attach the repo and Robinhood →
   prompt: *"Open docs/risk-watch-prompt.md on master and execute the prompt in
   its code block, steps 0-6. Advisory only: never place, modify or cancel an
   order."* → schedule hourly at :40, 13:40-19:40 UTC, Mon-Fri.
8. **Create the benchmark alerts** in Robinhood (Round 5 table), at levels set from
   today's prices. Claude can create them with `create_alert` after the user
   confirms the list. Moving-average alerts may not appear in the mobile app's
   alert list even though they are active; `get_alerts` is the source of truth.
9. **Run report-only for at least two weeks** before enabling any trading, and
   read every daily report.

## After setup — the first month
- **Daily:** read the report. Ask "would I have made that trade?"
- **Weekly:** check the ledger against the broker yourself, once.
- **Monthly:** review the options bucket and underwater positions; re-check caps.
- **Widen slowly:** one setting at a time, after something specific justifies it.

---

## A closing note for whoever receives this

Most of these rules exist because something went wrong once: fixed stops turned
normal pullbacks into losses; an automated run invented an approval that was never
given; a ledger quietly disagreed with the broker for a week; two runs bought at
the same moment because each thought it was alone. The process that picks stocks
changed three weeks before this kit was written because the old one lost money.
Keep the reports, write down why when something surprises you, and let the system
earn wider limits.
