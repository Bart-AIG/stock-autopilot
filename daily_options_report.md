# Daily report — trading day 2026-11-05 (Thursday)

*Written by the run that started 20:16Z (15:16 ET, prompt v18). This is before the 15:20–15:52 ET decision window, so **the decision-window run will add today's sleeve orders to Section 1.** Figures are broker figures at 20:17Z, not the close.*

**Today in one line:** a sharp sell-off. QQQ is **−5.83%** (651.64 vs 691.95), NVDA about −8%. The account has **$0 cash**, so the sleeves can't make new buys today.

## 1. Sleeves (swing)
- **SWING_Q (QLD):** holds 1.564326 sh (cost 83.25, bought yesterday). At 73.15 it is worth **$114.43 (−$15.80, −12.1%)**.
- **SWING_M:** flat. Yesterday's six names were never funded.
- **Decision window (ran 15:31 ET):** no orders placed.
  - `sleeves.py decide` on live prices at 20:31Z: QQQ 649.45, so RSI(2) 9.1 and IBS 0.015. **QLD is a KEEP.** Its target is $650.59, but there's no mid-month resize.
  - SWING_M wanted 7 names at $39.04 each: MRNA, MU, DELL, ILMN, VLO, MPC and MRVL. LITE, WDC and VIAV are off and weren't held.
  - **Every buy went unfunded.** Deployable cash is $0 minus the 5% reserve, so it's below zero. No sell was due.

## 2. BBW sleeve (NVDL, 20% of the base)
- No position. `bbw.py decide` found **no signal** on every candle today through 20:00Z (15:00–15:15 ET). No trades and no late exits.
- NVDL is at 22.83 (−17.4%). Even if a signal fires, there's no cash to fund it.
- The 11-02 search proposals (NVDU and NVDA) are still waiting for Ryan.

## 3. Legacy run-off
None open.

## 4. Options
- There are no agentic options.
- **Ryan's MU 2026-12-18 1220C ×8** (`placed_agent: "user"`): he added 3 more today at 1.90.
  - Mark 1.585 (bid 1.47 / ask 1.70): worth **$1,268**, about **−$2,045** against a $3,313 basis.
  - Delta 0.025, theta −$12.77/contract/day, and the broker puts the chance of profit at ~1.2%.
  - It's his position: the agent only notifies (done earlier today) and never closes it.

## 5. Growth paper sleeve
- Mark at 20:01Z: **$260.30, −20.86%**.
  - NVDA −8.0% on the day, PLTR −9.2%, NET −9.6%, CRWD −8.4%, NTRA −6.0%.
  - **NET is −33.6%, past the −25% exit line. It is reviewed Monday 11-09.**

## 6. Account
- Total value **$1,386.45**: options $1,272 (broker mark), QLD $114.45, cash $0.
- **QQQ since 2026-09-30:** 739.77 → 651.64 = **−11.91%**. Month to date: **−5.63%** (vs 690.49 on 10-30).
- **Sleeve drawdown** (Ryan's trades and $1,000 of deposits excluded): sleeve value ≈ $4,171. That is above the $3,604.85 high-water mark, so there's no −20% notice and no −25% halt.
  - Caveat: today's MU add looks deposit-funded and isn't in `deposit_excluded` yet, so this figure is overstated. It doesn't change the result: on a real sleeve basis (QLD ≈ $114 plus about $0 cash) the sleeves are tiny.
- About 92% of the account is Ryan's MU option. **The sleeves are effectively unfunded:** SWING_Q's target is ~$660 and BBW's is ~$263, against $0 cash.

## 7. Tomorrow / due
- **Fri 11-06:** TOM is off. Holds depend on the RSI2 and IBS legs only. After a −5.8% day QQQ may print RSI(2) < 10. The rules say buy only if price is still above the 200-day, and cash will still be $0 unless a deposit or a sale lands.
- The Friday review is written by the 14:15 CT run.
- **Mon 11-09:** growth paper exit check (NET), the weekly BBW search, and the weekly check.
