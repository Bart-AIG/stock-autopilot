# Daily Report — Thursday, 2026-09-10 — **BOTH BOOKS**

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:16 CT / 19:16 UTC by the first run at or after the report window — in-session, 44 minutes before the bell. All quotes stamped 19:16Z. Prompt v10.*

Broker-reconciled at 19:16Z: **1 option + 4 equities, zero drift** on quantity *and* average price. `get_option_orders` for 2026-09-10 is empty; `get_equity_orders` returns exactly three orders — all this desk's own `placed_agent="agentic"` fills — so nothing unauthorized landed and no sibling run placed anything across today's 33 runs.

**Headline: three actions today — LLY was time-stopped out for −$25.30, and both freed slots were refilled with A-grade entries (ABNB $1,114, UNP $1,100). The equity book went from 2 positions to 4 and is now FULLY DEPLOYED: $14.84 of deployable cash remains against a ~$600 minimum entry.** That transition is the single most important thing in this report, and §5 explains what it changes about how the next idea gets judged.

---

## 1. Positions

### Equity swing book — 4 open (target 3-4, band 3-5) — **the book is full**

| Name | Entry (date) | Shares | Mark 19:16Z | P/L | % | Day | Held | **Time stop** | Why we own it |
|---|---|---|---|---|---|---|---|---|---|
| **MMM** | 173.3371 (08-31) | 2.884552 | 162.795 | −$30.41 | −6.08% | −0.98% | **10 of 14** | **2026-09-14 (Mon)** | RSI(2) dip in an industrial with an intact margin-recovery story. Still prints RSI2 0.9 on today's screen — the setup has **deepened, not resolved**, which is the uncomfortable case: the signal that got us in is now stronger than at entry while the position is down 6%. |
| **GD** | 374.4437 (09-01) | 1.335314 | 353.4049 | −$28.09 | −5.62% | **+0.21%** | **9 of 14** | **2026-09-15 (Tue)** | RSI(2) dip in defense. Thesis re-confirmed **INTACT 09-09** (FY26 EPS guidance raised to $16.80-16.90, Gulfstream +15.1%, new $194.1M Mission Systems award). Re-checks 2026-10-09. The only book name green today. |
| **ABNB** | 169.5209 (09-10) | 6.573584 | 167.88 | −$10.79 | −0.97% | −1.03% | **0 of 14** | **2026-09-24 (Thu)** | **NEW today.** RSI(2) mean-reversion in a rising 200-day uptrend with a wide trend cushion. Full reasoning in §2. |
| **UNP** | 285.1071 (09-10) | 3.858199 | 285.04 | −$0.26 | −0.02% | **+0.11%** | **0 of 14** | **2026-09-24 (Thu)** | **NEW today.** The strongest full-stack setup graded all day — RSI2 2.2, 61.6 sessions of trend cushion, an earnings beat and a dividend raise behind it, and green against a −0.62% tape. Full reasoning in §2. |

**Equity book: $3,214.36 cost → $3,144.81 mark, −$69.55 unrealized (−2.16%).**

**All four are red**, which is the structural reason no take-profit could fire today — see §5.

### Options book — 1 open (the hedge)

| Contract | Entry | Mark 19:16Z | P/L | DTE | Status |
|---|---|---|---|---|---|
| **SPY 2026-11-20 700P ×1** | $749.00 (08-06) | 6.53 → **$653.00** | **−$96.00 (−12.8%)** | **71** | Authorized defensive hedge. **EXEMPT from all premium backstops** — it is insurance, expected to decay in a rising tape. Roll/close decision with Ryan at ~21 DTE (≈2026-10-30). Delta −0.166, theta −$11.09/day, IV 21.3%, OI 32,652. **Up $106 today** on the soft tape — doing exactly its job. |

No TACTICAL and no CORE position is open. Options slots used: **0 of 2 TACTICAL, 0 of 3 CORE** (hedge excluded).

---

## 2. Actions taken today — three

### ① SELL — LLY 0.420254 sh @ $1,129.5485, 13:36:25Z, order `6aa2b259` — **TIME STOP**

**Which rule fired:** the 14-day time stop, entered 2026-08-27, due 2026-09-10. Not a take-profit and not a thesis sell — the position's thesis was researched **intact** on 09-08 and was still intact when it was sold. The time stop fires **green or red**, and this one fired red: **−$25.30, −5.06%.**

**Why the book has this rule at all, since selling an intact thesis at a loss looks wrong on its face:** HARD RULE 5 forbids price stops outright, so without a time stop a stalled swing simply runs until the monthly cull. The time stop is the *only* mechanical loss discipline this book has. It is also the one exit that cannot collapse onto the entry price — measured across the whole book, the RSI2≥70 take-profit trigger sits a mean **0.84%** from entry, so both price-based exits cluster right where we bought and neither one ever closes a loser.

**The execution detail worth keeping:** LLY was sold **into the best print of its entire 14-day hold** — the fill at 1129.5485 was +0.47% against the prior close on a day the S&P fell 0.62%. That is the time stop working the way it is supposed to when a bounce happens to coincide with the deadline.

**Cross-validation:** three separate runs reached this slot independently this morning and **all three** reached the LLY time stop. One placed it; the other two reconciled to the same figures and correctly declined to double-sell. That is the exit logic agreeing with itself from three cold starts.

### ② BUY — ABNB 6.573584 sh @ $169.5209, $1,114.36, 14:21:02Z, order `6aa2bcce` — **grade A**

**Signal:** RSI(2) swing setup off the committed report. **Trend gate:** rising 200-day with real cushion. **Earnings:** verified clean — nothing inside the 14-day window.

**Sizing, and this is the new policy in action:** deployable $1,115.03 ÷ 1 remaining slot = **$1,114.36**. Under the pre-09-02 rules this would have been a $400-500 entry. The concentration policy Ryan set on 09-02 replaced the standard band with *size = deployable ÷ remaining slots*, floor ~$600, cap 30% of account value ($1,202 at the time). The entry used 27.8% of the account — inside the cap, and more than double what the old rules would have deployed.

**Execution quality:** review gate returned `order_checks {}` — no alerts. Quote at review: bid 169.53 / ask 169.60, a **$0.07 spread = 0.04% of mid**. The fill at 169.5209 came in **below the ask**.

### ③ BUY — UNP 3.858199 sh @ $285.1071, $1,100.00, 18:20:30Z, order `6aa2f4ee` — **grade A**

**Why this one was the best setup graded all day**, and it cleared every leg rather than most of them:

- **Technical:** RSI2 **2.2** — the lowest non-held name on the board. RSI14 34.4, −4.7% vs the 20-day, −3.5% vs the 50-day, momentum 12-1 **+33.3%**.
- **Trend gate:** the 200-day SMA is rising **monotonically** (255.467 on 08-19 → 260.934 on 09-09, +0.3905/session) and spot sits **24.06 points = 61.6 sessions** above it. Against a 14-day hold that is 4× the cushion needed. Compare to the two names declined on this exact gate today: SBUX had ~20 sessions, CL had **1.3**.
- **News / thesis (HARD RULE 7) — intact and strengthening:** Q2 2026 adj EPS $3.41 vs $3.24 est and revenue +12% to $6.864B, both beats; quarterly dividend **raised** $0.04 to $1.42; consensus Overweight with a FactSet mean PT of $332.70 (+16.7%); three upward PT revisions in six weeks.
- **Why NOW:** the RSI2 print is a 2-period extreme **today**, and UNP was **+0.09% green against SPY −0.61% / QQQ −1.00%**. The trend-maturity gate *confirmed* rather than diverged — the exact opposite of NVDA, which was declined this morning on a −2.31% vs −1.08% divergence.
- **Decisively:** there is **no adverse catalyst behind the slide.** The most recent company-specific news is a beat and a dividend raise.

**The three honest negatives, stated rather than buried** (all were weighed and none disqualified it): PEG 3.2 is the report's own "rich" flag — but the report itself calls the value columns secondary context, P/E 23.0 is unremarkable for a Class I rail, and PEG penalises mature compounders by construction; the UNP/Norfolk Southern $85B merger is a real overhang, but the STB timetable has **nothing binary inside a 14-day hold** (comments 11-18, DOJ/DOT preliminary 12-03, final briefs 2027-05-28); Baupost cut UNP 23% in Q2, offset by Viking Global **initiating** a 2,047,332-share position the same quarter — and both are 06-30 13F data, ~10 weeks stale.

**Sizing:** $1,100 = 27.4% of account value, inside the $1,202 per-name cap. This entry took the book to 4 of the 3-4 target and to full deployment.

---

## 3. Candidates considered and **SKIPPED** — 30+ names graded, **zero others** cleared

This is the most educational section, so here is the full shape of the day: **the report's boards carried 26 RSI2 setups this morning and grew to 25-26 names through the session. Two were taken. Everything else was declined, and grade B got no position at all — not a small one.**

**The morning sweep (14:00Z) — 26 setups, zero A.** Collapsed by cohort: healthcare rout 7 (LLY had just been time-stopped out of that same complex), payments/financials de-rating 4, index ETFs 4, correlated-with-book 3 (RTX vs GD; EMR/TKR vs MMM), broken-not-dipping 2 (GE, AMZN). Two were worked to a real verdict and both graded **B**:

- **NVDA** — best trend structure on the board (+10.7% over a rising 200-day), but a **DOJ antitrust probe into the Groq deal** opened ~09-09, day 2, unresolved, with the tape confirming it (NVDA −2.31% vs QQQ −1.08%). Trend-maturity gate (c) divergence.
- **TGT** — best relative strength on the board (−0.43%) and an intact-to-improving company thesis, but UBS 09-04 puts it on the wrong side of the tariff-refund split, and crude >$100 is a direct consumer headwind **the day before CPI**.

**The afternoon names, each declined on a *different* gate** — worth reading as a set, because it shows the gates are doing independent work rather than all firing together:

| Name | Grade | The gate that actually killed it |
|---|---|---|
| **SBUX** | B | **Thesis, not technicals.** RSI2 deepened to 1.0 — *more* oversold than UNP — and it still didn't qualify. A 09-08 Oppenheimer de-rating, an open-ended union boycott (08-25), the 08-20 restructuring, P/E 57.5, PEG −2.3 (negative = declining earnings). **A deeper technical print does not repair a thesis.** |
| **CL** | C | **Trend gate, on arithmetic.** 200-day rising, but spot sat **+0.10% above it — 0.086 points against a +0.065/session slope = ~1.3 sessions of cushion.** The average climbs through the price almost immediately. |
| **ROST** | B | **Re-entry inside the window.** Time-stopped out of this book on 09-03, 7 days ago. Nothing distinguishes today from the hold that just failed, and re-entering restarts the clock the time stop just ended. |
| **JNJ** | B | Thesis is genuinely strong (UBS Buy/$320 on 09-02, HSBC raised to $320 that morning) — declined on setup quality, not on the story. |
| **AMZN** | B | Broken-not-dipping, and it sits in the exact mega-cap complex being de-rated today (QQQ −1.00% vs SPY −0.62%). Tape diverges against a long. |
| **QQQ** | — | The index *is* the thing selling off, and a long QQQ **partially cancels our own SPY 700P hedge**. Self-defeating by construction. |
| **DLTR** | B | The last new name of the day (19:01Z board). Trigger was live (RSI2 8.48) and momentum strong (+34.3%), but: the 200-day gives only a **10.1-session cushion against a 14-session hold**, and the move is a **post-earnings de-rating through a beat** (−13.2% in 12 sessions; actual EPS 1.39 vs 1.03 est and it gapped 132.18 → 120.00 anyway) — the broken-not-dipping cohort, not a dip. |

**No options candidate was taken, and neither track was close:**

- **TACTICAL — barred outright, before any trigger was measured.** Tomorrow's **CPI at 08:30 ET** lands *inside* the hard time stop of any scalp opened today (flat by the close of the next session = 2026-09-11). The 2026-08-26 capstone forbids opening breakout scalps into an unresolved scheduled catalyst. Note this bar is scoped to TACTICAL's own window — CPI does **not** bar a CORE swing or an equity swing, whose 21-45 day and 14-day horizons routinely span a macro print.
- **CORE — failed IV sanity on our own measured rows, and had no "why NOW".** From today's `iv_history.json` sweep: **SPY 1.2134 raw / 1.4464 ex-gap; QQQ 1.0525 / 1.4034.** Index premium is at or near a series record. That is a reason to be careful *buying* premium — and emphatically not a thesis to *sell* it, since naked shorts are banned at any level.

**Spread specs handed to Ryan today: none.** No thesis reached the bar where a vertical would have been the right vehicle.

---

## 4. Sleeve state

| | |
|---|---|
| **Total account value** | **$4,012.23** |
| Equity value | $3,145.78 |
| Options value | $651.00 (the hedge) |
| Cash | $215.45 |
| **Unleveraged buying power** | **$215.45** — *equal to cash and to `buying_power`, so **no margin is extended**. FOUR LAWS #4 clean.* |
| Operational reserve (5% of total, recomputed) | **$200.61** |
| **Deployable** | **$14.84** |
| Per-name cap (30% of account) | $1,203.67 |
| Minimum entry | ~$600 |
| **Equity slots** | **4 of the 3-4 target** (band 3-5) |
| Equity entry throttle | **2 of 3 used** |
| Options entry throttle | **0 of 8 used** |
| Options premium at risk | $749 basis — **hedge only**, and it is exempt |
| **Realized today (broker)** | **−$25.30** — one closing trade, the LLY equity time stop |
| **Realized options today** | **$0.00** against the **−$400** cap — *today's −$25.30 is an **equity** loss and does not touch the options cap* |
| Weekly calibration | **Done for this week** (09-08, the week's first trading day — 09-07 was Labor Day). Verdict **NO CHANGE**, nothing escalated: equities n=55 / margin **+18.3 pts** over breakeven, options n=17 / margin −0.3 pts, both report-only (equities because only 2 of 55 closes are in-regime under the 09-02 parameters, options because n<20). Next due the week of 09-14. |
| Monthly rebalance | Not due (falls on the first trading day of the month; 09-01 has passed). |

---

## 5. What full deployment actually changes — read this part

The book crossed into full deployment at 18:20Z today, and it changes the *nature* of every future decline, not just the arithmetic.

**Until today, a "no trade" meant the desk looked at a name and judged it not good enough.** That is a statement about the name. **From here, the binding constraint is capital: $14.84 deployable against a ~$600 minimum.** The next several "no trade" lines will be about the wallet, not the setup — and the report will say which, every time, because those two mean completely different things.

**The rotation gate is now ACTIVE.** Under Ryan's 08-29 capital policy, once deployable cash drops below one position size a new idea does not queue — **it must be graded better than the weakest position currently held**, and if it is, we sell that one to fund it. The bar therefore tightens automatically as the book fills. Three things about this that matter:

1. **"Weakest" means weakest on the entry stack** — thesis strength, setup quality, distance to target. **Never simply the biggest loser.** Selling a sound underwater thesis to chase a fresher signal is exactly the churn HARD RULE 5 exists to prevent.
2. **A rotation sell is an exit** and obeys every exit rule: the thesis check, the ownership gate, and the notify-once duty.
3. **It is dormant in practice until 09-14**, and by arithmetic rather than by preference: nothing on today's board out-grades what we hold, and the two oldest positions (MMM 09-14, GD 09-15) time-stop within four sessions and free their capital on their own.

**The honest counterweight, because concentration is the half of this policy that is easy to get wrong:** four $900 positions and eight $450 positions have the **same expected return** on the same deployed capital — the concentrated book simply carries **more variance**. It only pays if the top four ideas are genuinely better than ideas five through eight. **Fewer positions must mean more selective, never merely bigger.** Two entries out of 30+ names graded today is what that looks like when it is working.

---

## 6. Tomorrow's watchpoints

| When | What | Why it matters |
|---|---|---|
| **Fri 09-11, 08:30 ET** | **US CPI** | The binding macro event. Bars the TACTICAL options track today and tomorrow morning by the hard-time-stop rule. Does **not** bar equity swings or CORE. Both new positions (ABNB, UNP) were graded **with CPI already inside their window** — it was priced into the grade, not treated as a bar. |
| **Fri 09-11** | Gap risk on a **fully deployed** book | With $14.84 of dry powder, a gap cannot be averaged into and HARD RULE 4 forbids adding to a loser without Ryan anyway. The book is positioned and stays positioned. |
| **Mon 09-14** | **MMM time stop** (day 14 of 14) | Mechanical — fires **green or red**, no discretion. Currently −6.08%. Frees ~$470-500. This is also the date the rotation gate stops being dormant. |
| **Tue 09-15** | **GD time stop** (day 14 of 14) | Mechanical. Currently −5.62%, thesis confirmed intact 09-09. Frees ~$470. |
| **Tue 09-16** | **FOMC, live 25bp expected** | Inside ABNB's and UNP's windows. Priced into both grades. |
| Week of 09-14 | Weekly calibration due | First trading day of the week. Watch whether equities reach 20 in-regime closes — until then the parameters can only be *reported*, never tuned. |
| ~2026-10-30 | Hedge ~21 DTE | The SPY 700P roll/close decision is **Ryan's**, not mechanical. 71 DTE today, so this is far off. |

---

*Both books reconciled against the broker at 19:16Z with zero drift. No autonomous sell was made on any `placed_agent: "user"` position — there are none in the book. No HARD RULE 9 flag was created, cleared, or adjudicated by this run.*
