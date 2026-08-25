# Daily Options Report — Tuesday, 2026-08-25

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:20 CT / 19:20 UTC by the first run at or past the 14:15 CT window, from live quotes timestamped 19:16Z. Not deferred to a tidier slot.*

**One-line summary: a flat day by decision, not by accident — the desk placed nothing across twenty-seven runs, and the single tactical trigger it had been testing all afternoon finally *fired* at 14:45 ET, *failed its hold clause* five minutes later by six hundredths of a point, and has since round-tripped completely. The most useful thing produced today was not a trade; it was discovering that the level everyone had been watching for seven runs is mechanically expiring overnight — and, in this run, that the level replacing it is moving the *other* way and will cross it tomorrow for reasons that have nothing to do with the market.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark 19:16Z | P/L at mark | What an exit nets (at bid) | DTE | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | agentic (hedge) | 7.49 | 6.215 | −$127.50 / −17.02% | −$129.00 (bid 6.20, **0.48%** spread) | 87 | Working as designed |

**Book: basis $749.00 → mark value $621.50. Unrealized −$127.50.** Greeks: delta −0.151, theta **−$8.99/day**, IV 20.39%, OI 26,164, volume 426.

**Why we own it:** this is the authorized defensive hedge under your Aug–Oct drawdown posture — insurance, not a directional bet. It is *expected* to bleed in a flat-to-up tape and is explicitly exempt from every premium backstop. Its decision point is the ~21-DTE roll/close conversation with you, still ~66 days out. Today it behaved exactly as a 0.15-delta, 87-DTE put should on a green day: the tape rose, the put lost roughly a day of theta plus a little delta, and nothing about that is a signal. **No action, and none contemplated.**

One honest note on the number: it is down from −$91 in yesterday's report. That is not deterioration of the thesis — it is two more sessions of carry (−$9/day) plus SPY grinding a little higher. The hedge is designed to look like this right up until the day it doesn't.

---

## 2. Actions taken today

**None. Zero entries, zero exits, zero orders sent.** Realized P/L **$0.00** on **0 closing trades** — broker-confirmed via `get_realized_pnl` for 2026-08-25, not taken from the journal.

Reconciliation ran clean on every check: one open contract, quantity 1.0000 at average_price 749.00, all `pending_*` fields zero, no overnight assignment, exercise, expiration, or unauthorized fill. The lot invariant was asserted in code rather than eyeballed (1 × 7.49 × 100 = 749.00 = max_loss = broker average price).

---

## 3. What we considered — and why each one was declined

This is the section worth your time. Six things were genuinely worked today; none of them cleared.

### 3.1 TACTICAL — the QQQ 20-day trigger. It fired. Then it failed.

The desk carried a two-sided trigger on QQQ's 20-day SMA (710.3985) all session: a *completed* 5-minute close beyond the level, on volume above the trailing-30-minute baseline, *held* on the following bar.

At 18:45Z it finally fired on the upside — the bar closed **710.570**, clearing the level by **+0.1715**, on **168.8%** of the reconciled trailing-30 baseline. Both entry clauses, cleanly, for the first time all day.

Then the hold clause failed. The next bar closed **710.340** — short by **0.0585 points**. By 18:55Z the gap had widened to 0.1385, and as I write this QQQ is **709.74**, back below the level and essentially back where it broke from. **The break round-tripped in full inside thirty minutes.**

That is the *seventh* failed level test of the session. The honest read: today's tape had no follow-through in either direction, and the trigger did its job — it refused six near-misses and then correctly gave back the one it caught, because the hold clause exists precisely to filter breaks like this one.

**Grade: no candidate. Not taken.**

### 3.2 The level itself is expiring — and the one replacing it moves the other way

The 19:00Z run computed the 20-day's roll-off schedule for the first time and *retired* the level. This run finished the job it left open: the 50-day.

With QQQ **flat at 709.74**, the two moving averages walk toward each other from opposite sides purely because of which old closes leave the window:

| After the close on | 20-day | 50-day | Gap |
|---|---|---|---|
| 2026-08-24 (actual) | 710.3985 | 713.2256 | 20d is **2.83 below** |
| 2026-08-25 | 712.1110 | 712.9936 | 0.88 below |
| **2026-08-26** | **714.5115** | **712.3084** | **20d is 2.20 ABOVE — they cross** |
| 2026-08-27 | 715.8210 | 711.9060 | 3.92 above |
| 2026-08-28 | 716.9085 | 711.6506 | 5.26 above |

The 20-day climbs +7.0 points over five sessions on a *motionless* index, because the late-July crash closes (675.49, 661.73, 683.55, 687.99, 700.07) are dropping out one per night. The 50-day drifts *down* −2.2 points because it is shedding the far richer mid-June closes (721.34, 744.00, 729.86, 722.51, 740.62).

**Two things follow, and both matter tomorrow:**

1. **The 20-day is not a level to trade against — it is a level departing.** A run that re-derives only its *value* each morning will keep scoring a widening gap as a near-miss. It is retired.
2. **A "20-day crosses above the 50-day" print lands tomorrow, and it is an artifact — not a momentum signal.** It happens on a flat index. Anyone reading that cross as a bullish golden-cross-style confirmation would be reading the July crash falling out of a lookback window as evidence about August. Flagging it now so no future run trades it.

**The live structural reference for tomorrow is the 50-day (~712.99 after tonight's close), because it is falling *toward* price rather than running away from it** — plus the session high/low. Everything else gets re-derived from tomorrow's own tape.

*Data-quality footnote:* today's session high is 714.04 (opening bar, clean). The session low reads **708.77** on the 5-minute feed and **708.88** on the 30-minute — an 0.11-point disagreement, which is itself another instance of the truncation defect the 18:45Z and 19:00Z runs root-caused in both series today. Treat the low as ~708.8 and don't quote either feed to three decimals.

### 3.3 CORE on index and mega-cap tech — blocked by tomorrow's NVDA print

CORE requires 21–45 DTE. The only qualifying board is **2026-09-18 (24 DTE)**, and on any index or mega-cap tech name that board spans **NVDA's 2026-08-26 after-the-close print**. The 2026-08-05 exit engine says *close* before earnings — opening into them is the same rule pointed the wrong way, and the "unless earnings *is* the thesis" exception doesn't apply, because the desk has no edge on a print the entire market is positioned for.

Worth recording honestly: the crush argument for this block is **weaker than it looks**. Term structure measured live today puts the 09-18 board at 41.92% IV against 41.08% at 31 DTE this morning — about **one vol point** of event premium, not thirty-five. The event premium is almost entirely in the 3-DTE 08-28 board (77.2% IV, 5.73% implied move, range 199.92–224.22). So the block stands on the *rule*, not on a crush the numbers don't support. **This block is dated, not structural — it expires with the print, and runs on 08-27 must hunt CORE properly rather than citing it.**

### 3.4 CORE outside tech — nine names screened, nine declined

CORE was *not* structurally unavailable today, and the desk deliberately proved that rather than hiding behind the block. Nine liquid non-tech names were worked. **TLT** got the full treatment: the 09-18 board quotes beautifully (84C at **1.68% of mid**, delta 0.415, OI 51,155) — a CORE-eligible, print-immune, tightly-quoted chain demonstrably exists. It was declined **on its merits**: stale catalyst, ex-gap IV/RV ratio 1.122 (premium is not cheap), and a breakeven above the 50-day, meaning the single leg pays roughly nothing at the price the thesis said to bank. GDX and GLD failed the trend-maturity gate; EEM failed "why NOW"; the rest were inert.

TLT was re-checked at 17:05Z and again now — 83.325 → 83.375 over two hours, five cents. **No new information, so the decline was not re-litigated.** Re-pricing a vehicle whose underlying hasn't moved is how a desk talks itself into a trade it already declined.

### 3.5 The equity report's RSI2 names — untradeable, now measured twice

Five candidates off the committed equity screen were quoted on the monthly board at target delta: **RTX 12.8–18.0%** of mid, **TXN 14.3%**, **LMT 14.1%** (chain-wide 12.6–21.6%), **TKR 38.0–43.7%**, **GD 45.2–52.4%**. The CORE gate is ≤10%. **Five of five failed**, spanning 12.6–52.4%.

This independently reproduces the 2026-08-14 post-mortem (4 of 5, same range). The equity report remains the only comprehensive screen we have and stays a real CORE source — but its hit rate into a *tradeable options chain* is now measured twice at approximately zero, and a run should expect to screen and discard the whole list. **These five are not "blocked pending the print" — they are untradeable for options at this account size at any time.**

### 3.6 Fading the NVDA print — not a candidate at any grade

The 08-28 straddle costs 12.150 against a 212.07 spot: a **5.73% implied move** just to break even. That is a coin flip against a heavily-taxed vehicle, and the DTE-7 floor bans that board outright anyway. Not considered further.

---

## 4. Sleeve state

| | |
|---|---|
| Premium at risk — TACTICAL | **$0** (0 of 2 slots) |
| Premium at risk — CORE | **$0** (0 of 3 slots) |
| Hedge (excluded from slots) | $749 basis / $621.50 mark |
| Account value | $4,091.21 — equity $445.65, options $622.00, cash $3,023.56 |
| `unleveraged_buying_power` | **$3,023.56** — equal to `buying_power`, so **no margin is being extended** |
| Deployable after the $250 reserve | **$2,773.56** |
| Realized P/L today | **$0.00** vs the −$400 cap — **not binding** |
| Entries used | **0 of 8** today, 0 of 2 this run |
| Margin-equity floor | $4,091 vs the $2,000 minimum — clear |

Every slot is open and capital is not the constraint. **The constraint today was the absence of a setup that cleared its gates** — which is the correct reason to be flat, and worth saying plainly rather than dressing up.

---

## 5. Tomorrow's watchpoints

1. **NVDA reports after the close, Wednesday 2026-08-26.** Implied move 5.73% (range ~199.92–224.22). NVDA closed today at 212.26, +1.81%, making session highs *into* its own print. The desk will not be long premium across it.
2. **The 20/50 SMA cross prints tomorrow and is an artifact.** See §3.2. Do not read it as a momentum signal; it happens on a flat index.
3. **Use the 50-day (~712.99 after tonight) as the live structural level, not the 20-day.** Re-derive both from tomorrow's tape — inherit nothing but the retirement.
4. **CORE on index and mega-cap tech unblocks Thursday 08-27**, once the print clears. That is a real hunt, not a formality.
5. **Timing hole worth knowing:** the 2026-09-18 board is CORE-eligible (21–45 DTE) only through **08-28**; the next monthly, 2026-10-16, doesn't enter the window until **09-01**. On monthly-only chains that is a genuine two-session gap where no compliant CORE expiry exists.
6. **Tactical:** tight-chain names only (SPY, QQQ, NVDA, mega-caps at ≤3% of mid), sized $300–1,000, and any trigger must reference a *structural* level with both its price and volume clauses re-derived off the same fresh window. Today's seven failed tests are the argument for that discipline, not against it.

---

*Governance note: no Ryan approval is claimed or implied anywhere in this report. Nothing was armed, placed, or approved. The equity autonomy ban and the ownership gate were not touched.*
