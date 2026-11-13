# Sleeve money and the real-money drawdown (set 2026-11-13)

**Authority:** Ryan, REAL live turn 2026-11-13, answering the audit of the same day:
*"lets fix finding 4. 5."*

Code: `capital.py` (tests: `test_capital.py`). Run duties: `docs/routine-prompt-v20.md`.
History rebuild: `capital_backfill.py`.

## What was wrong

| # | Finding | Measured on 2026-11-13 |
|---|---|---|
| 5 | Sleeve targets were sized on total account value, which includes Ryan's own option positions. The sleeves cannot spend that money. | Targets added up to $2,367 against about $1,775 of deployable cash. From mid-October the sleeves held $63 to $650 while targets were computed on $1,200 to $2,900, so SWING_M ran at up to twice its tested share of the money that existed. |
| 4 | The drawdown rule measured total value with Ryan's option losses and his deposits added back. | It read $4,172 against a $4,176 high, while real sleeve money was about $1,800. The -25% halt could not fire until the sleeves had lost about $1,040, more than half of the money they held. |

## The rule

| Term | Definition |
|---|---|
| User value | Market value of every position Ryan placed himself (`placed_agent: "user"`). Today that is his MU options. |
| Sleeve money | `total_value` minus user value. It is cash plus the positions the agent holds. |
| Base | 95% of sleeve money. Every sleeve weight is a share of the base. |
| Reserve | 5% of sleeve money, never spent. |
| Deployable | `unleveraged_buying_power` minus the reserve, never below 0. |
| Sleeve P/L | The broker's all-time realized P/L on stocks, plus the unrealized P/L of the agent's open positions. Only changes in it are used. |
| Index | The sleeves' unit value, 1.0 at the 2026-09-30 close. At each reading it is multiplied by 1 + (change in sleeve P/L since the last reading) / (sleeve money at the last reading). |
| Drawdown | Index divided by its high-water mark, minus 1. |

- **Sizing (finding 5):** wherever a sleeve formula used `total_value`, it now uses sleeve money.
  That covers the base, the reserve, deployable, the `--tv` passed to `sleeves.py decide` and
  `levx.py decide`, the BBW target and the GROWTH paper notional. The four sleeve targets now
  add up to the base, so every sleeve can be funded at its tested weight at the same time.
- **Drawdown (finding 4):** the lines are unchanged. At -20% notify Ryan once. At -25%, beyond
  the tested -23%, notify him and place no new sleeve buys until a live Ryan turn. Sells always run.
- **Ryan's own trades and deposits never move the index.** They change sleeve money, not sleeve
  P/L. His 2026-10-13 instruction stands: his trades never halt the sleeves.

## How a run uses it

Every market-hours run, after the broker reconcile and before any order:

```
python3 capital.py money --tv <total_value> --user-value <user value> --ubp <unleveraged_buying_power>
python3 capital.py drawdown --tv <total_value> --user-value <user value> \
        --unrealized <U> --realized <R> --now <UTC, ISO> --write
```

- `U` is the sum over the agent's open positions of quantity x (price - average cost).
- `R` is `get_realized_pnl(account_number, asset_classes=["equity"], span="all")` `total_returns`,
  read fresh every time. A sale moves P/L from `U` to `R`, so a stale `R` would show a gain or
  loss that never happened.
- `--write` stores the state in `holdings.json` under `_SLEEVE_PROCESS.drawdown_real`.

The tool prints an `action`:

| Action | What the run does |
|---|---|
| `none` | Nothing. |
| `notify` | The drawdown passed -20%. Notify Ryan once, with the numbers. |
| `halt_notify` | It passed -25%. Notify Ryan and place no new sleeve buys, starting now. |
| `halted` | The halt is still on. No new sleeve buys. |
| `suspect` | The reading was not applied. No new sleeve buys this run; tell Ryan the numbers once. |
| `suspect_repeat` | Still not applied on a later run. No new sleeve buys, no second notice. |

It also prints the sleeves' return today, month to date and since 2026-09-30, and the dollars of
further loss that would reach each line at today's sleeve money.

## Guards built into the tool

| Guard | Why |
|---|---|
| The reading comes before the run's orders. | A position is carried by the money that existed when it was bought. |
| A new high must hold for two readings in a row. | One wrong input cannot ratchet the high-water mark. A false high would overstate every later drawdown. |
| One reading cannot move the index by more than 20%. | A funded book cannot do that in 15 minutes. It means a wrong input, or a deposit and a trade between two readings. The index, the high-water mark and the last reading are left untouched and the run reports `suspect`. A correct reading on the next run clears it. If it persists, an interactive session checks the numbers and runs `python3 capital.py rebase ... --by "<who checked, and why>" --write`, which moves the starting point without moving the index. |
| With under $1 of sleeve money at the last reading, a P/L change is skipped. | There is no base to measure it against. |
| The halt is sticky. | Only `python3 capital.py lift --by "<Ryan's words>" --now <UTC> --write`, run by an interactive session on a live Ryan turn, clears it (HARD RULE 9). A lift moves the high-water mark to the current index, so the -20% and -25% lines start fresh from there. |
| `--write` refuses a ledger that does not round-trip at indent=2. | A formatting diff never lands on the ledger. |

## The rebuilt history

`capital_backfill.py` rebuilt the index from the 2026-09-30 close out of three sources: the
ledger's closed and open sleeve positions, each day's cash from the journal's post-close
reconciliation line, and daily closes. Two cross-checks held:

- The ledger's realized P/L matched the broker's daily figures to within $0.14 over the period
  (-$45.47 against -$45.33).
- Before Ryan's first option purchase, rebuilt sleeve money matched the journal's total account
  value to within $2.27 on all seven days.

| Close | Sleeve money | Ryan's positions | Sleeve P/L since 9-30 | Index | Drawdown | QQQ |
|---|---|---|---|---|---|---|
| 2026-09-30 | $3,316 | $1 | +0 | 1.0000 | 0.0% | +0.0% |
| 2026-10-05 | $3,492 | $0 | +71 | 1.0214 | 0.0% | +2.2% |
| 2026-10-09 | $994 | $2,360 | +73 | 1.0220 | 0.0% | +1.6% |
| 2026-10-14 | $573 | $1,087 | +43 | 0.9928 | -2.9% | -1.5% |
| 2026-10-16 | $541 | $679 | +10 | 0.9363 | -8.4% | -4.1% |
| 2026-10-23 | $445 | $1,130 | +19 | 0.9566 | -6.4% | -4.8% |
| 2026-10-30 | $520 | $1,147 | -5 | 0.9141 | -10.6% | -6.7% |
| 2026-11-05 | $113 | $1,272 | -21 | 0.8490 | -16.9% | -12.5% |
| 2026-11-09 | $63 | $1,251 | -11 | 0.9261 | -9.4% | -8.2% |
| 2026-11-11 | $1,982 | $867 | -12 | 0.9099 | -11.0% | -6.7% |
| 2026-11-12 | $1,980 | $750 | -13 | 0.9093 | -11.0% | -7.0% |

What the history says:

1. **The high-water mark is 1.0220, set at the 2026-10-09 close.** The index was 0.9093 at the
   2026-11-12 close: 11.0% below its high and 9.1% below the start. QQQ was 7.0% below its own
   start. On real money the sleeves have tracked QQQ since go-live and run slightly behind it.
   The old add-back scorecard said +6.7% against -4.8% on 2026-10-26; that figure was wrong.
2. **The worst reading was -16.9% on 2026-11-05,** when the sleeves held $113 and QQQ fell 6.5%
   in a day. The old measure read about -0.1% that day.
3. **Sleeve money fell from $3,490 to $63** between 2026-10-08 and 2026-11-10 as Ryan's option
   purchases used the account's cash, then returned to about $1,980 when he sold six contracts
   on 2026-11-11.

Limits of the rebuild: daily closes rather than run-by-run readings, so a deposit and a trade on
the same day share one denominator (the largest such effect is 2026-11-11, about 1.7 points of
index). Cash for 2026-11-05 and 2026-11-06 was read as $0.00 from the journal.

## Changing it

The lines (-20%, -25%), the reserve (5%) and the definitions change only on a live Ryan turn.
No unattended run lifts a halt, moves the high-water mark, or edits `drawdown_real` by hand.
The retired add-back figures stay in `_SLEEVE_PROCESS.drawdown_basis` for the record; no run
writes them any more.
