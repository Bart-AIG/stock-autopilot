# Daily report — trading day 2026-09-16 (Wednesday, FOMC)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-15 report, so this run owned the duty and took it rather than deferring. Quotes stamped 19:19–19:21Z, ~40 minutes before the bell and well outside the opening-auction window.*

**One line:** The Fed hiked 25bp with a hawkish dot plot, the market took it calmly for half an hour and then gave it all back during Chair Warsh's press conference — SPY went **+0.34% → −0.84%** intraday. The desk placed **one** trade all day (IBKR, this morning, before the decision), the DAY TRACK's paper signal stopped out at −1.00R, and nothing else in any book cleared its bar. **Your own SPY strangle expires tomorrow and your resting $0.50 sell order on the 770C will not fill — see §5.**

---

## 1. DAY TRACK — paper day 2 of 10

**Phase: PAPER.** No order was placed and none was placeable. Both of the phase's locks are worth restating because one of them opened last night and it would be easy to misread that as graduation:

- **Lock (a) — prompt authority: OPEN since 2026-09-15.** Stop-order authority on `sleeve:"day"` positions needs prompt v11, and v11 is live. Discharged; it is no longer a blocker and should stop being reported as one.
- **Lock (b) — `day_track.graduate()`: STILL CLOSED, and it never depended on the prompt.** It needs ≥10 paper days and ≥8 signals with positive expectancy. We are at **2 days, 2 signals**. Earliest arithmetically possible go-live is a Monday on or after **2026-09-28**, and only the Monday calibration may flip it.

### Today's signal

| Field | Value |
|---|---|
| Opening range (QQQ, 09:30–09:35 ET, one-minute bars) | high **708.79** / low **707.86** / open **708.01** / close **708.45** |
| Range | 0.93 pts (0.131% of spot); body 47.3% of range — clears the 10% doji filter |
| Direction | **LONG** (OR close above OR open) → vehicle QQQ, no PSQ translation |
| Entry (paper) | **708.43** at 13:35:30Z · stop **707.86** (opposite OR edge) · 1 share · R = **$0.57** |
| Size binding constraint | **cash**, not risk. 1 share — see the quantization note below |
| Outcome | **STOPPED, −1.00R, −$0.57.** The 13:36 bar — the first full minute after entry — printed a low of 707.650, breaching the stop by 0.21 |

**Two things this paper day taught, both recorded in the ledger:**

1. **Long-side quantization.** On the short side the vehicle is PSQ at ~$26, so the same dollar risk buys 56 shares and sizing is smooth. On the long side the vehicle is QQQ at ~$708, so deployable cash of $1,417 buys **one share** and the position is 1-share granular. The track's risk arithmetic is therefore much coarser long than short at this account size. Not a defect to patch mid-week — a property to measure, and the reason phase 2 (TQQQ/SQQQ) exists as a proposal for you after ≥20 live trades.
2. **`manage()` must be fed the adverse extreme since the last pass, not the current price.** A concurrent 13:45Z run ratcheted the stop to 708.95 at "+2.44R" — every step of that pass was correct, and its conclusion was wrong, because the position it was managing had already stopped 24 minutes earlier. A stop cannot ratchet after it has been hit. The 14:00Z run caught it and restated the day at −1.00R. In paper this cost nothing; live it would have been a fictional open position.

**Running paper tally: 2 signals, 2 stopped, −2.00R.** Honest reading at n=2: **both signals were directionally right and both were stopped inside two minutes.** That is a stop-distance question, not a direction question, and it is exactly what the 10-day paper sample exists to answer. No run may add a filter to fix it — if the edge is not there, `graduate()` says so in numbers.

---

## 2. Positions — all three books

### Equity swing book (3 of the 3–4 target)

| Name | Entry | Shares | Now (19:20Z) | P/L | Day | Held | Time stop | Why we own it |
|---|---|---|---|---|---|---|---|---|
| **ABNB** | 169.5209 (09-10) | 6.573584 | 166.73 | **−$18.35 (−1.65%)** | −0.95% | 6d/14 | **09-24** | RSI2 3.4 in a confirmed uptrend (200-day rising monotonically, +20.7% above it). Bought because analysts marked estimates **up** through the week price marked down — mean PT rose $179.75 → $183.24 across a −7.7% week. The decline repriced the market, not the company. |
| **UNP** | 285.1071 (09-10) | 3.858199 | 280.86 | **−$16.39 (−1.49%)** | −1.10% | 6d/14 | **09-24** | Same cohort of entries. Rail operator, oversold inside an intact trend. Its RSI2 take-profit armed briefly this morning at 71.7 while ~+0.30% green, then decayed to 12 within thirty minutes as the tape turned — see §4. |
| **IBKR** | 87.2999 (09-16) | 8.109516 | 85.30 | **−$16.22 (−2.29%)** | **−3.94%** | 0d/14 | **09-30** | Today's entry. Full write-up in §3. |

**Book: −$50.95 on $2,922.32 of cost (−1.74%).** Every position is red and every position fell today — the book currently has **zero dispersion**: it is one macro factor expressed three ways. That is a real, measured concentration risk and it is the reason §4 declined a fourth name.

**No exit fired, and this is determinate on the cheapest leg alone:** all three are red at the live bid, and the RSI2≥70 take-profit requires a **green** position (an RSI2 print on an underwater name is an *optional* exit-into-strength routed to thesis, never a mechanical loss-realization). No target, no trail crossing (triggers 199.44 / 335.42 / 102.71 — none near), no time stop inside its 3-day warning. The 19:07Z report independently judges all three **HOLD (thesis-watch)** and its ACTION block is empty.

**A fast adverse move is not an exit trigger.** The swing book carries no price stop by design (HARD RULE 5). Its loss discipline is the 14-day time stop, and for ABNB and UNP that is **2026-09-24** — eight days out, green or red.

### Options book — your positions, not the desk's

| Contract | Qty | Your cost | Mark (19:20Z) | P/L | Expiry |
|---|---|---|---|---|---|
| SPY 2026-09-17 **770 Call** | 1 | $27.00 | **$1.50** (bid 0.01 / ask 0.02) | **−$25.50** | **tomorrow** |
| SPY 2026-09-17 **731 Put** | 1 | $28.00 | **$25.50** (bid 0.25 / ask 0.26) | **−$2.50** | **tomorrow** |

Both legs are `placed_agent='user'` — you opened this strangle in the app on 09-15. **The ownership gate is engaged: the desk does not close, trim, roll or re-price either leg, and has not.** Detection was notified once on 09-15; this section is the standing record, not a re-notification. See §5 for the one thing that is genuinely new and time-sensitive.

**Desk options book: empty.** 0 of 3 CORE slots used, 0 of 3 entries today, $0.00 realized against the −$400 daily cap.

---

## 3. Action taken today — the IBKR entry, and the event it was sized around

**Filled 16:24:37.62Z · order `6aaac2c5` · $707.96 market order · 8.109516 sh @ $87.2999 · placed_agent `agentic` · zero fees.** Review gate returned `order_checks {}` on a $0.02 spread (0.023% of mid). Broker re-read immediately before sending, twice.

**Why it cleared the bar:**
- **Technical:** RSI2 8.6 on the live print (17.3 on the settled 09-15 close), 200-day SMA 79.72 **rising monotonically** across 22 sessions (+5.93%, zero down-ticks) with spot 9.5% above it, mom12-1 +49.0%.
- **The discriminator against the other financials on the board:** USB, BAC and PNC all had the 20-day *below* the 50-day — the configuration that certifies a downtrend rather than a dip. IBKR's 20-day sat **above** its 50-day (+0.60%) with spot 5–6% under both. That is a sharp pullback inside an intact intermediate uptrend, which is the Connors setup; the others were not.
- **Thesis (HARD RULE 7):** consensus **OVERWEIGHT**, mean PT $108.72–109.42 (+24.6% over the fill), Goldman Buy $113, BofA Buy $114. August operating metrics strong on every line — DARTs 4.276M **+23% YoY**, client equity $962.8B **+35%**, accounts 5.46M **+35%**, margin loans $101.5B **+41%**. The −7% session on 09-01 was a UBS downgrade to *Neutral* at a $102 target — still 17% above our fill — landing the same day the 10-year hit 4.80%.
- **`[ERN]` clean and verified, not assumed:** the calendar returned 64 events for the window, so it was not degraded-empty, and IBKR appears nowhere. Q3 prints mid-October, outside the 09-30 time stop.

**Sizing was the event adjustment, and it was deliberate:** $707.96 = deployable ÷ 2 remaining slots = **18.3% of the account**, not the $1,161 per-name cap. The run named the unresolved FOMC as its reason for sizing under the cap.

**A concurrent 16:20Z run graded this same name off this same report and DEFERRED it.** The two runs agreed on every measured leg and split on one judgement: whether v11's "macro is a sizing input, not a bar" permits a reduced-size entry ahead of the decision. One said yes and traded; one said no. Both readings are defensible and the disagreement is logged rather than smoothed over — the broker-first sibling check cannot see another run's *decision*, only its *fills*.

### The duty that entry wrote, discharged here

The entry recorded that IBKR's FOMC sensitivity is **two-sided with opposite signs** — higher rates *help* net interest income on $185.6B of client credit balances, while a hawkish de-rating *hurts* through risk appetite, margin loans and trading velocity — and imposed a duty on the first run after the decision to say which channel dominated.

**The event:** the Fed hiked 25bp to **3.75–4.00%**, unanimously, its first increase since 2023. The dot plot moved hard: **16 of 18 policymakers now see at least one more hike this year** (six of 18 in June), median year-end 4.00–4.25% held through 2027. 2026 inflation forecast raised to 3.7%, unemployment cut to 4.1%, and the "supply shocks" characterisation of inflation was **dropped**.

**The verdict — the de-rating channel dominated, and it is not close.** IBKR **−3.94%** today against XLF −2.31%, SPY −0.84%, QQQ −0.43%. It fell **1.7× its own sector ETF and 4.7× the index on the day the Fed delivered the hike that is the NII channel's entire thesis.** The entry contemplated exactly this fork and took the side that lost.

**What that does and does not mean.** It is a thesis-check verdict on a held position, **not an exit trigger** — converting a cross-sectional price measurement into a sale would hand the book the discretionary price stop HARD RULE 5 exists to forbid. The position's written invalidations are company-specific (a reversal in monthly client-metric growth, a PT-revision cluster reversing the overweight consensus, a regulatory action) and **none has occurred**. It stays. The 09-30 time stop is the adjudicator. The part of the process that held up is the sizing: under the cap rather than at it, which is why the cost of being on the wrong side of this fork is −$16.22 rather than −$27.

---

## 4. Candidates considered and SKIPPED

The 19:07Z report's RSI2 board carried **19 names**, up from **9** at 18:07Z. That doubling is itself the most important thing on the board today.

**Board breadth: 9 → 19 names (3.9% → 8.3% of a 229-name universe) inside the single hour of the press conference.** Ten arrivals — C, LRCX, MS, IWM, FCX, DIA, EPD, SCHW, TKR, AMZN — and not one of them is a name-specific event. Connors RSI(2) presumes an *idiosyncratic* pullback inside an intact uptrend; when 8% of the universe goes oversold in the same hour, the screen has stopped selecting dislocated names and is measuring the index. The arithmetic is fine; the object it refers to changed. **This is not a veto and must not harden into one** — a macro selloff is exactly what mean reversion exists to exploit. It changes the question asked of each candidate (is this name dislocated, or is it just long the market?), never the answer.

| Candidate | RSI2 | Day | Grade | Why it was declined |
|---|---|---|---|---|
| **LRCX** | 2.9 | −1.71% | **B** | The only arrival with a real structural case: momentum top decile (#13, mom12-1 +245%), above a rising 200-day, mean PT **$383.96** vs a $266 price (+44%), BofA $385, Berenberg raised to $420. **The thesis gate is what declined it.** The decline has two named, *live, unresolved* drivers: the 09-14 Anthropic/OpenAI "pace the frontier" essay that took the semicap complex down 7–8% in a session, and a rate shock the Fed just reinforced — and LRCX is explicitly the kind of capital-intensive high-multiple name that de-rates on discount rates. RSI2 mean reversion works when a decline *lacks* a fundamental driver. Add a four-insider selling cluster at the highs (CEO $9.6M and a director $3.0M on 09-09, an SVP $17.4M on 09-02, the CLO $1.5M on 08-31 — ~$31M). And it is **−1.71% against SMH −0.22%**: the weak name inside a *strong* sector today, not a dip in a leader. **A B-grade gets no position, not a small one.** |
| **C, MS, SCHW** | 2.8–8.8 | −2 to −4% | **C** | The bank/broker cohort, already graded down twice today and worse now: XLF −2.31% against SPY −0.84%, with the cohort leading its own sector down. A cohort falling 2–4% against a −0.8% index is a repricing, not an oversold dip inside an intact uptrend. The desk also already holds IBKR inside this cohort. |
| **WMB, EPD** | 2.2, 8.7 | — | — | **Excluded on your standing sector steer** — no new oil-energy entries. Listed, not proposed. |
| **IWM, DIA** | 4.0, 7.7 | −1.28%, — | **C** | Index ETFs. No company thesis is available for one, and an index printing RSI2<10 on FOMC day is a restatement of "the market fell" — the identical factor the book is already long three times over. |
| **FDX** | 3.9 | −2.19% | **B+** | Graded in full at 17:25Z and declined; earnings settled by option term structure rather than by the calendar. Unchanged and worse on the tape since. |
| **AMZN, FCX, TKR, PFE, CVS** | 4.4–9.8 | −1.1 to −2.5% | **B/C** | Screened, not fully worked up, and the honest reason is that none reaches the A bar on the technical stack alone — AMZN's RSI2 of 9.8 is the shallowest print on the board, and none of the others carries a momentum-decile or sector-relative case that a full thesis workup could rescue into an A. Stated plainly rather than implied. |
| **IBKR, UNP** | 5.4, 8.9 | — | — | **HELD.** A buy is an *add*; both are red, and adding to a losing position needs your explicit approval (FOUR LAWS #3). Not proposed. |

**Capital declined nothing.** Deployable was **$711.57** (`unleveraged_buying_power` $901.56 − the 5% operational reserve $189.99), which clears the $600 minimum entry; the 4th slot of the 3–4 target was open; 2 of 3 entries remained on the throttle; no cash hold sits on this capital (the FOMC hold dissolved on its own written mechanics at 18:00Z and was deleted). **The bar declined it.** Zero A-grades.

**The UNP take-profit that armed and decayed.** At the open UNP printed RSI2 71.7 while ~+0.30% green — the take-profit condition read *fired*. It was not taken: the ledger's gate defers a mechanical exit to a fresh committed report, and today's first report did not land until ~14:00Z. **By the time it landed, RSI2 had decayed 80 → 12 inside thirty minutes and UNP was red.** That is worth stating as a cost, not a save: the report gate cannot outrun a 2-period RSI, and a real, rule-compliant take-profit was structurally unreachable. It is recorded in the ledger as a finding for the Monday calibration rather than patched mid-week by a run acting on its own authority.

**Options: no entry, no candidate evaluated.** Under v11 a macro event is a sizing input and not a bar — but "not a bar" supplies no thesis, and no CORE thesis exists on this board. TACTICAL is retired and was not hunted. No `iv_history` row is owed; today's nine core-list rows are already written.

---

## 5. ⚠️ Your SPY strangle — one thing only you can act on

Both legs expire **tomorrow, 2026-09-17**.

- **The 770 Call is effectively dead.** SPY is 751.07; the call is bid **$0.01** / ask $0.02, delta 0.008, `chance_of_profit_long` 0.8%. Mark $1.50 against the $27.00 you paid.
- **Your resting sell order will not fill.** You placed a good-for-day limit **sell-to-close at $0.50 credit** on that call at 17:13Z (order `6aaace42`). The bid is $0.01 — fifty times below your limit. It has processed 0 of 1 and, being GFD, it **expires unfilled at the bell** unless you re-price it. The desk has not touched it and will not.
- **The 731 Put is the live leg and today helped it.** Mark $25.50 against $28.00 paid, delta −0.05, and SPY fell 6.3 points during the press conference. It is still ~20 points out of the money with one session left.

Combined strangle: **−$28.00 on $55.00 of premium.** Nothing here is a desk decision — flagging it because the clock is the binding constraint and a resting order that cannot fill is easy to forget about.

---

## 6. Sleeve state

| | |
|---|---|
| Total account value | **$3,799.89** |
| Cash = buying power = **unleveraged** buying power | **$901.56** — identical, so no margin is being extended (FOUR LAWS #4 unambiguous) |
| Equity value / options value | $2,870.33 / $28.00 |
| Operational reserve (5% of total, recomputed) | **$189.99** |
| **Deployable** | **$711.57** |
| Per-name cap (30%) | $1,139.97 |
| Equity slots | **3 of the 3–4 target** used; 1 open |
| Equity entries today | **1 of 3** (IBKR) |
| Options entries today / open CORE | 0 of 3 / **0 of 3** |
| Realized P/L today — options | **$0.00** against the −$400 cap (read from the ledger, not typed) |
| Realized P/L today — equities | $0.00 |
| Unrealized — equity book | **−$50.95** |
| DAY TRACK | PAPER, day 2 of 10, −2.00R cumulative. Account $3,799.89 is above the $2,600 pause floor |

**Reconciliation: ZERO DRIFT in both books.** Broker shows IBKR 8.109516 @ 87.30, ABNB 6.573584 @ 169.52, UNP 3.858199 @ 285.11 (all fully sellable, none held), and both SPY 09-17 legs. The ledger carries five rows = three equities + your two legs, matching one-for-one. The only order on this account today is the ledgered IBKR fill plus your own 17:13Z sell limit.

---

## 7. Tomorrow's watchpoints

1. **Your SPY strangle expires.** The 770C is worthless and its resting $0.50 order dies at tonight's bell; the 731P needs a ~20-point further drop. Your call entirely.
2. **The presser leg is unfinished.** SPY closed the report window at 751.07, −0.84%, after being +0.34% at 18:20Z. JPMorgan's pre-decision scenario map put "hike + material further tightening needed" at −1% to −2%; we are inside that bucket. Tomorrow tells us whether it was a one-day repricing or the start of one.
3. **The RSI2 board should be re-counted at the first report.** If it stays near 19 names, today's macro-breadth reading is confirmed and the entry question stays "is this name dislocated or just long the market?" If it drains back toward 9, the arrivals were a one-hour artifact.
4. **IBKR is the live test.** The de-rating channel won today. Its thesis invalidations are company-specific and none has tripped; the 09-30 time stop, not the price, is the adjudicator. Watch for a PT-revision cluster — that is the one thing that would turn this from a bad tape into a broken thesis.
5. **ABNB and UNP hit their 14-day time stop on 09-24** — six sessions out, and they are sold green or red on that date. Within three days of it, an RSI2 bounce becomes the preferred way out.
6. **DAY TRACK paper day 3.** QQQ opening range at 09:30–09:35 ET, one trade, no discretion.

---

*No HARD RULE 9 flag was created, cleared, or adjudicated today. No Ryan turn is claimed, quoted, or implied anywhere in this report — every decision above was taken under the standing authorizations already on master.*
