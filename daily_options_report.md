# Daily report — trading day 2026-09-17 (Thursday)

*Written by the 19:19Z scheduled run (2:19 PM CT — the first run at or after the v11 2:15 PM CT threshold). Master carried the 2026-09-16 report, so this run owned the duty and took it rather than deferring. All quotes stamped 19:19–19:22Z — well past the opening auction, ~38 minutes before the bell.*

**One line:** The desk placed **nothing** in any book today, and for once that is not a judgment call — it is arithmetic. The DAY TRACK took paper signal #3, stopped out at −1.00R for the **third consecutive day**, and **tripped both pause conditions at once**, so it is shut down until Monday. The equity book has $369.14 of deployable cash against a $600 minimum entry, and the only route left — a rotation — was worked properly today and **declined on evidence, not on capital**: the name the desk would have had to sell was upgraded by UBS yesterday, and the name it would have bought is diverging *down* from a sector that is up 2.5%. Ryan closed his VLO puts himself at −$360, which spends 90% of the day's options loss cap.

---

## 1. DAY TRACK — paper day 3 of 10, and the track is now PAUSED

**Phase: PAPER.** Nothing was placed. Read both gates carefully — they are independent and only one has ever opened:

- **Lock (a) — prompt v11 stop authority: OPEN (discharged since 2026-09-15T16:18Z).** This run is likewise invoked with v11. This is not a blocker and should stop being reported as one.
- **Lock (b) — `day_track.graduate()`: CLOSED, and it has nothing to do with the prompt.** `graduate(3, [−1.0, −1.0, −1.0])` → `go_live: false — "paper 3d / 3 trades; need 10d and 8 trades"`. **A live prompt stamp is not a graduation**, and no run promotes the phase itself mid-week.

### Today's signal

| Field | Value |
|---|---|
| Opening range (QQQ, 1-min bars 13:30–13:34Z) | high **716.43** / low **714.06** / open **715.98** / close **714.115** |
| Body | −1.865 pts = **78.7% of range** (far clear of the 10% doji cut) |
| Direction | **SHORT** → vehicle **PSQ** |
| Entry | 7 sh @ **25.965** (QQQ 714.38), 13:35:12Z venue |
| Stop | **25.8905** (QQQ 716.43 = the OR high), stop distance **0.287%** |
| Size | $181.75, **cash-bound** — risk budget at 5% would have permitted ~$71,000 of position; cash binds at ~1/380th of it |
| Result | **Stopped out 14:27Z. −1.00R = −$0.52** |

### The pause, and why it fired

`day_track.track_status(...)` → **`{paused: True, reason: "3 consecutive losing days — rest of week"}`**. **Both** conditions tripped on the same close:

1. Three consecutive losing days (09-15, 09-16, 09-17 — all −1.00R).
2. Week at **−3.00R**, at the −3.00R limit.

The third condition, equity below $2,600, is **not** implicated — the account is $3,444.80.

**No new DAY TRACK signal may be taken through Friday 2026-09-19.** The first run of Monday 2026-09-22 re-evaluates. Because no signals accrue while paused, the earliest arithmetically possible go-live slips to **a Monday on or after 2026-10-05**.

**Running tally: 3 paper days, 3 signals, 0 wins, −3.00R, −$1.55 notional.** Worth stating plainly rather than burying: *the direction was right on two of the three days and the stop was hit anyway.* A 0.287% stop on a day QQQ's ATR14 is 8.25 points (~1.15%) is a quarter of an average day's range — the opening-range edge is a genuinely tight one and it will take the full 10-day sample to know whether it is an edge at all. That is exactly what the paper phase is for, and the pause is the spec protecting the sample rather than the spec failing.

---

## 2. Positions — all three swings HOLD, none close to an exit

Quotes 19:19Z. RSI2 computed Wilder from own daily bars with the live print appended.

| Name | Sleeve | Shares | Entry | Live | P/L | RSI2 | RSI2=70 needs | Target | Held | **Time stop** |
|---|---|---|---|---|---|---|---|---|---|---|
| **ABNB** | swing | 6.573584 | 169.5209 | 165.69 | **−2.26%** (−$25.19) | **6.84** | 170.09 | 183.08 | 7d/14 | **2026-09-24** |
| **UNP** | swing | 3.858199 | 285.1071 | 282.48 | **−0.92%** (−$10.14) | **46.02** | 285.40 | 298.32 | 7d/14 | **2026-09-24** |
| **IBKR** | swing | 8.109516 | 87.2999 | 88.955 | **+1.90%** (+$13.42) | **58.67** | 90.46 | 96.14 | 1d/14 | **2026-09-30** |

**Why we own each:**
- **ABNB** — Connors RSI(2) mean-reversion, entered 09-10 off the committed report. The setup is not merely intact, it is *deeper*: ABNB appears on **today's** RSI2 board at 7.4 (marked HELD), i.e. the oversold condition that justified the entry has extended rather than resolved. No price stop by policy; recycled by the time stop on 09-24 if it neither reverts nor breaks.
- **UNP** — RSI(2) entry 09-10. **Thesis materially strengthened yesterday:** UBS upgraded UNP to **Buy from Neutral** and raised its target **$310 → $339** (Wadewitz, 09-16), citing 3.5% 2027 volume growth, intermodal +6–7%, and merger optionality on Norfolk Southern worth $19.40–21.90 of 2030 EPS. Street mean target **$334.04** against a $282.48 spot.
- **IBKR** — autonomous entry 09-16 at 16:24Z, day 1 of 14, the only green name in the book (+2.44% today).

**No exit fires, on any of the three mechanisms:**
- **Take-profit (RSI2≥70 while green):** nothing is close. ABNB needs 170.09, UNP 285.40, IBKR 90.46 — and ABNB and UNP are red anyway, which routes them to thesis, never to a mechanical exit.
- **Time stop (14d):** earliest is 09-24, seven days out.
- **Target hit:** none. ABNB +10.5% away, UNP +5.6%, IBKR +8.1%.
- **Trailing-stop trigger (green enough, entry ÷ 0.85):** ABNB 199.44, UNP 335.42, IBKR 102.71. Nothing near. No `SET TRAILING STOP` alert for Ryan today.
- **Thesis flags:** none researched to broken. UNP's went the other way — see above.

**Options (both Ryan's, ownership gate engaged, notify-once already discharged):**

| Contract | Qty | Basis | Mark 19:21Z | Delta | Status |
|---|---|---|---|---|---|
| SPY 2026-09-17 **770C** | 1 | 0.27 ($27) | **0.015** | 0.0166 | expires tonight, 7.09 pts OTM |
| SPY 2026-09-17 **731P** | 1 | 0.28 ($28) | **0.005** | −0.0028 | expires tonight, 31.9 pts OTM |

SPY 762.91. **No exercise or assignment exposure on either leg** — both will expire worthless. Ryan's FOMC strangle cost $55 and is worth $2.00. The desk may not act on these and did not.

---

## 3. Actions taken today — NONE by the desk

Zero orders placed in any book. `get_equity_orders` for 2026-09-17 returns **empty**; the only options order today is Ryan's own.

**Ryan's trade (recorded, not acted on):** he closed the **VLO 2026-09-18 390P ×2** at 14:55:36Z for 0.75 ($150 gross) against a $510 basis — **−$360 realized**. He first rested a 1.30 limit at 14:44Z and cancelled it. `placed_agent='user'` on both sides of the round trip, so the ownership gate applied throughout and the desk correctly neither closed it nor advised into it mid-flight. VLO is down only −0.62% today against a tape up 1%+, so the exit was into weakness in his favour — the puts simply ran out of time with expiry tomorrow.

---

## 4. Candidates considered and SKIPPED — the rotation was worked, not waved away

Today's report (19:07Z, header clean, no DATA ERROR) put **seven** names on the RSI(2) board: CVS 4.5, LRCX 5.4, BMY 7.0, DASH 7.1, ABNB 7.4 *(HELD)*, VZ 8.0, SCHW 8.5.

**The capital fact first, stated honestly:** deployable is **$369.14** against a **~$600 minimum entry**. Under the concentration policy a sub-$600 entry is *a skipped opportunity, not a small one*, so no outright entry exists today. **But capital is not a sufficient reason to stop**, because the rotation gate is precisely the route that survives a full book — selling a position frees $700–1,090, which clears the minimum. So the gate was actually applied.

**Weakest position on the ENTRY STACK.** Not the biggest loser — ABNB is the biggest loser and is *not* the weakest, because its setup deepened. On setup decay the candidate was **UNP**: RSI2 has drifted from oversold to a neutral 46.02 without the price reverting, i.e. the mean-reversion signal that justified the entry has dissipated while the position sat.

**The comparison, both sides:**

| | UNP (the sell side) | LRCX (the best buy candidate) |
|---|---|---|
| Setup | RSI2 46.02 — **decayed**, the weak half | RSI2 5.4, −9.9% vs 20d, −12.7% vs 50d — **the strongest print on the board** |
| Thesis | **Strengthened 09-16**: UBS upgrade to Buy, PT $310→$339, street mean $334 vs $282 spot | BofA PO $385 vs $269 — but the oversold print is *manufactured by a live, unresolved narrative*: the 09-14 Amodei "pace the frontier" essay knocked LRCX −8.2% premarket in a sector-wide AI-slowdown repricing |
| Tape confirmation | −0.92%, quiet | **Diverging the wrong way — SMH is +2.52% today and LRCX is not participating.** A mean-reversion entry needs the bounce to be starting; this one is being left behind by its own sector |
| Insider | — | CEO Timothy Archer sold **30,000 shares / $9.58M on 09-09**, eight days ago |
| Grade | — | **B.** Not A-grade. |

**Verdict: NO ROTATION.** It fails on both halves independently. LRCX grades **B**, and under the concentration policy *a B-grade gets no position, not a small one*. And UNP is not the sound-thesis-being-churned case the rule warns about in the abstract — it is a name whose fundamental thesis was **upgraded yesterday**, with 18% of street-mean upside left and seven days still on its time-stop clock that will recycle the capital mechanically anyway. Selling that to buy a semi that is failing to bounce with its sector is exactly the churn HARD RULE 5 forbids.

**Also excluded:** CVS (deepest RSI2 at 4.5, but PEG 3.7 / "rich" on the joint screen and it is a joint-book holding — not graded A for the agentic swing book), BMY / DASH / VZ / SCHW (B-grade prints, none clears the rotation bar against a book whose weakest name was just upgraded), ABNB (already held — a new buy would ADD, and see the cap note below).

**Concentration note, standing from the 18:35Z run:** on a $3,444.80 account, ABNB is **31.62%** and UNP **31.64%** — both above the **30% per-name cap**, pushed there not by the positions moving but by Ryan's −$360 VLO close shrinking the denominator. The ruling is **STOP ADDING, not sell** (the cap is a sizing gate, and HARD RULE 5 permits a sale only on a target, an RSI2≥70 print while green, or a broken thesis — none of which applies). The book is already stopped on capital, so this binds nothing today, but it independently rules out any ADD to ABNB or UNP.

**Options — capital-blocked, not thesis-blocked, and say which:** 0 of 3 CORE slots used, 0 of 3 daily entries used. Deployable **$369.14** cannot fund the $500–1,000 CORE band, so no CORE candidate was armed. Separately, the loss cap has only **$40** of headroom (see §5), which would gate a new entry the moment it is spent. No spread was specced for Ryan today. TACTICAL remains retired.

---

## 5. Sleeve state

| | |
|---|---|
| Total account value | **$3,444.80** |
| Cash = buying power = **unleveraged** buying power | **$541.38** (identical → **nothing borrowed**, FOUR LAWS #4 satisfied unambiguously) |
| Equity value | $2,900.42 |
| Options value | $3.00 |
| Operational reserve (5% of total, recomputed) | **$172.24** |
| **Deployable** | **$369.14** — below the $600 equity minimum and below the CORE band |
| Options premium at risk (agentic) | **$0.00** — the desk holds no options |
| Options premium at risk (Ryan's, not desk budget) | $55 basis, $2.00 mark |
| **Realized options P/L today** | **−$360.00**, 1 closing trade — *read from the ledger and broker-confirmed (`get_realized_pnl` 2026-09-17), not typed from a default* |
| Daily options loss cap | −$400 → **$40.00 headroom, 90% spent, NOT hit** |
| Options entry throttle | 0 of 3 used |
| Equity entry throttle | 0 of 3 used |
| Open equity slots | **3 of the 3–4 target** (band 3–5) |

**On the cap attribution, because it is genuinely ambiguous and the answer was to be strict:** the −$360 is Ryan's own loss on a `placed_agent='user'` round trip. Whether a user position's realized loss counts against the *desk's* −$400 daily options cap has never been tested. The governance tie-breaker is "where either is stricter, the stricter rule applies", so the desk **counts it**. It gated nothing today — capital blocked the options book first — but it is the honest reading and it is flagged for Ryan's ruling.

**Calibration:** not due. The week's calibration ran Monday 2026-09-14; no parameter changed this week. Next Monday 2026-09-21 also runs `day_track.graduate()` — **expected verdict: not yet**, on days and signals, and the pause means no new signals accrue before then.

**Monthly rebalance:** not due. Next on the first trading day of October.

---

## 6. Tomorrow's watchpoints

- **Friday 2026-09-18 is quad-witching.** Expect inflated volume and wider-than-usual opening markets; the standing rule against pricing any decision off the opening auction print matters more than usual.
- **Ryan's SPY 731P/770C expire worthless tonight.** Nothing to do; the ledger rows come out on tomorrow's first run.
- **The DAY TRACK is PAUSED through Friday.** Tomorrow's first post-bell run should compute the opening range for the record but **must not take a signal**, and must not read the v11 stamp as permission — the pause and the graduation gate are separate from the prompt version.
- **DAY TRACK re-evaluation: Monday 2026-09-22**, first run of the week.
- **ABNB and UNP time stops land Thursday 2026-09-24** — both fire green or red, and they will free ~$2,180 of capital, which is the first real opportunity this book has had to make a full-size entry in a week. The `TIME_STOP_WARN_DAYS` annotation starts appearing on the report from 09-21.
- **Capital stays the binding constraint until then.** Nothing changes that except an exit, and the only scheduled exits are those two time stops.
- **Levels:** SPY 762.91 (+1.15%), QQQ 716.83 (+1.72%) — both at session highs post-FOMC. QQQ ATR14 daily 8.2514.

---

*Written by an unattended scheduled run. No Ryan approval is claimed, quoted, or implied anywhere in this report (HARD RULE 9). Every figure above was read from the broker or the ledger this run, not carried forward.*
