# LEVX sleeve: liquid leveraged index funds, held overnight and on intraday breakouts

**Status: PROPOSED 2026-11-13. Not live.** Code `levx.py`, tests `test_levx.py`, state
`levx_state.json`, daily inputs `levx_inputs.json` (built by `.github/workflows/levx-build.yml`),
evidence `levx_results.md`, routine duties `docs/routine-prompt-v19.md` (paste-pending).

**Request (Ryan, REAL live turn 2026-11-13):** *"Lets work on a sleeve trade model that works
with SOXL, AAOX, SPCM, LITX, COHX and others like these. It should be either a day trade, swing
trade or you find the best way to trade it without limitations on the agent account. Backtest
till you feel confident you have found a optimal method to make the most amount of money
possible, with the funds we have in the agent account"*. That turn asked for the model. It did
not approve a weight, so nothing here trades until he does.

## The rules

| | Rule |
|---|---|
| Funds | TQQQ (3x Nasdaq-100, index QQQ) and SOXL (3x semiconductors, index SOXX). Half the sleeve each at night |
| NIGHT entry | At about 15:50 ET buy a fund if its index is above its 200-day average (today's live price counted in) |
| NIGHT size | The fund's half x min(1, 40% / annualised volatility of its last 20 overnight returns) |
| NIGHT exit | Sell at the first run after the next open (09:31 ET fire) |
| DAY (TQQQ only) | At each :00 and :30 bar close from 10:00 to 15:30 ET: hold TQQQ with the whole sleeve if that close is above the band, hold none if it is not. Band = max(today's open, prior close) x (1 + TQQQ's average move from the open at that time of day over the last 14 sessions) |
| DAY to NIGHT | At the NIGHT decision a DAY position is cut to the NIGHT size (or to zero) |
| Not in the rules | Stops, targets, news or earnings checks, grades. The tested rules have none |

- The DAY band rule is the long side of the noise-area breakout in Zarattini, Aziz & Barbon
  (2024). Their VWAP trailing stop is left out: on TQQQ it changed no result (14.4%/yr without
  it, 13.9% with it), and leaving it out means the rule needs no volume data.
- A DAY entry is taken only by the run that fires right after its bar closes (within 12
  minutes). A run that arrives later never chases it.

## Why these two funds, and the test for adding one

Costs decide everything here. Quoted spreads on 2026-11-13 (three samples, a volatile day):

| Fund | Spread, round trip | $ traded a day | Verdict |
|---|---|---|---|
| TQQQ | 1.8 bp | $3.9B | In |
| SOXL | 3.6 to 5.4 bp | $8.7B | In |
| QLD | 1.3 bp | $360M | Passes, but SWING_Q already holds it |
| NVDL | 5.8 bp | $330M | Borderline, and BBW already trades it |
| SPCH | 12.8 bp | $217M | Fails on spread |
| SPCM | 7 to 15 bp | $14M | Fails: spread, volume, no fractional buys, and SpaceX has no 200-day average until about March 2027 |
| LITX | 31 to 51 bp | $81M | Fails on spread |
| AAOX | 61 bp | $93M | Fails on spread (one cent on a $1.63 price) |
| COHX | 70 to 110 bp | $26M | Fails on spread |

The night edge is about 15 to 35 bp a night in a 3x index fund. A fund joins only if all of
these hold:

1. Quoted round-trip spread of 6 bp or less: the median of at least 3 samples on 2 different
   days, one of them in the last 15 minutes of a session.
2. At least $100M traded a day (20-day average) and fractional buys allowed.
3. Its index or stock has 250 sessions of history, and the fund itself has 60.
4. The NIGHT rule on that fund, net of twice its measured cost, was positive in both halves
   of the test (synthetic prices before the fund's launch are allowed and must be labelled).
5. It is proposed to Ryan with the numbers. Only a live Ryan turn adds a fund
   (`levx.FUNDS`; night shares must sum to 1).

Candidates that passed step 4 in the 15-fund test but have no spread samples yet: SPXL, UPRO,
SSO, TNA, USD, LABU.

## Evidence in one table

Live rules replayed on real 5-minute bars (`levx.simulate`), net of 1.5 bp a side for TQQQ and
2 bp for SOXL. Cells are return a year / worst drawdown / Sharpe. Full record: `levx_results.md`.

| | 2018-22 | 2023-26 | 2018-26 |
|---|---|---|---|
| LEVX | 45.9% / -35% / 1.24 | 65.2% / -32% / 1.50 | 54.0% / -35% / 1.36 |
| Night legs only | 29.9% / -30% / 0.99 | 41.0% / -27% / 1.18 | 34.6% / -34% / 1.08 |
| DAY leg only | 12.3% / -17% / 0.84 | 17.2% / -12% / 1.02 | 14.4% / -17% / 0.92 |
| LEVX at 2x costs (the planning case) | 33.4% / -35% / 0.99 | 50.7% / -33% / 1.26 | 40.7% / -35% / 1.11 |
| LEVX at 4x costs | 11.5% / -37% / 0.49 | 25.4% / -34% / 0.78 | 17.4% / -37% / 0.62 |

In the account (2019-26, monthly rebalance, split = SWING_Q / SWING_M / BBW / LEVX):

| Split | As tested | Pessimistic |
|---|---|---|
| 50 / 30 / 20 / 0 (live today) | 29.9% / -21% / 1.38 | 27.7% / -18% / 1.36 |
| 40 / 30 / 20 / 10 | 32.4% / -21% / 1.51 | 29.0% / -19% / 1.46 |
| 30 / 30 / 20 / 20 | 34.7% / -22% / 1.61 | 30.3% / -20% / 1.52 |
| 20 / 30 / 20 / 30 | 37.0% / -22% / 1.65 | 31.5% / -20% / 1.52 |
| 30 / 30 / 20 / 20 with NIGHT only | 31.2% / -21% / 1.52 | 27.7% / -18% / 1.46 |

- At pessimistic costs a NIGHT-only LEVX adds no return over the SWING_Q money it replaces.
  The gain comes from the same dollars working at night and in the day.
- LEVX fell 27.9% between 2026-10-01 and 11-12. The 30/30/20/20 split fell 15.9% in those six
  weeks against 13.2% for the live split. It does not protect in a Nasdaq selloff.

## How a day runs

No change to cron-job.org. The existing fires are enough.

| Fire (ET) | LEVX does |
|---|---|
| 09:31, 09:46 | MORNING: sell last night's position, first thing in the run |
| 10:01, 10:31 ... 15:31 | DAY: the TQQQ check for the bar that just closed |
| 10:16, 10:46 ... 15:16 | DAY catch-up only: makes an exit a missed run should have made. Never opens |
| 15:46 | NIGHT: cut any DAY position and set tonight's position, orders in before 15:58 |
| after 16:00 | nothing |

Each run: quotes for QQQ, SOXX, TQQQ, SOXL; in the DAY window also today's TQQQ 5-minute bars;
then `python3 levx.py decide LIVE.json --now <UTC> --tv <total value>`. It prints the mode, the
phase and each fund's target in dollars. The run trades the difference: sells first, buys last.

| If this goes wrong | What happens |
|---|---|
| The 09:31 run is missed | The 09:46 run sells. Selling anywhere from the open to 10:00 tested at 52% to 62% a year, with no pattern |
| A DAY check run is missed | No entry from that check. A missed exit is made by the next run and logged late |
| The 15:46 run is missed | No night position that night. A DAY position still on (16% of sessions) is carried overnight at full size and sold next morning. Reported |
| The morning inputs build fails | `decide` reports stale inputs: sells only that day, Ryan is told once |
| Robinhood returns incomplete 5-minute bars | The target is null: the position is left alone and nothing is opened |
| Trade approvals are switched on | No LEVX buys (an approval after the bell would fill at the next open, the opposite of the rule). Sells still go |

## Dollars at today's account size

Total value $2,492 (2026-11-13), base 95% = $2,367.

| Weight | Sleeve | NIGHT, each fund (at full size) | DAY (TQQQ) |
|---|---|---|---|
| 10% | $237 | up to $118 | $237 |
| 20% | $473 | up to $237 | $473 |
| 30% | $710 | up to $355 | $710 |

- Orders are dollar-based market orders in regular hours. Both funds allow fractional shares.
- At 20%, LEVX at full size is about 60% of the base in index exposure (20% x 3x), at night and
  in the day. That is on top of QLD, the SWING_M names and NVDL. No money is borrowed.
- About 1,000 orders a year.

## Guard rails

| Rule | Detail |
|---|---|
| Standing ban | No unattended run adds a gate, filter, news check or veto, changes a parameter, or adds a fund |
| Pause (automatic) | `python3 levx.py score` each morning. Sleeve 30% below its own high: Ryan is told. 40% below (the tested worst is 35%): entries stop until a live Ryan turn. Exits still run |
| Cost check (reported) | Each round trip logs fill against the quote mid. After 20 round trips in a fund: above 6 bp (TQQQ) or 8 bp (SOXL) Ryan is told; above 12 or 16 bp the run proposes a pause. At 4x the assumed cost the sleeve tested below QQQ |
| Account drawdown | The existing -20% notice and -25% buy halt on sleeve value apply to LEVX as to every sleeve |
| Capital | LEVX sells are a run's first orders and LEVX buys its last, so the swing sleeves and BBW are funded first. LEVX never sells another sleeve's position |
| Ownership | Never sells a `placed_agent: "user"` position, including TQQQ or SOXL he buys himself |
| No margin | Buys are capped by `unleveraged_buying_power` less the 5% reserve |

## Going live

| Step | Who | Effect |
|---|---|---|
| 1. Merge the branch to master | Ryan's OK | The "LEVX inputs build" Action starts writing `levx_inputs.json` each morning |
| 2. Paste `docs/routine-prompt-v19.md` | Ryan | PAPER: every run does the full procedure and logs what it would have traded. No orders |
| 3. Set the weight in a live turn | Ryan, then an interactive session | `levx.W_LEVX` is set and the funding sleeve's weight is cut in the same commit. `test_weights_fit_the_base` fails if the sleeves add to more than 100% |

Steps 2 and 3 can be done together. Paper measures timing and data problems. It cannot measure
trading cost, which is the main risk, so a small live weight teaches more than a long paper run.

## Open items and limits

- **Cash.** Sleeve targets are computed on total value, which includes Ryan's MU calls ($513).
  Deployable cash is about $1,775. At 30 / 30 / 20 / 20 the four sleeves want $2,367 when
  every signal is on, so the last in line (LEVX) is cut on those days.
- **The $2,000 line.** Robinhood keeps a $2,000 minimum for margin accounts. The account is at
  $2,492 including the calls. I could not confirm what Robinhood does to settlement below
  $2,000. If the account type changes to cash, the DAY leg must stop: same-day round trips
  on unsettled money are good-faith violations.
- **Wash sales.** LEVX buys SOXL and TQQQ almost every night the gate is on. A loss taken on
  either fund in the joint account, or any other account, within 30 days of one of those buys
  is a wash sale. Inside the sleeve, losses on daily round trips are deferred into the next
  purchase, and December losses can roll into the next tax year.
- **Taxes.** Every gain is short term.
- **DAY evidence is thinner than NIGHT.** One fund, one published rule, positive in both halves
  and in 8 of 9 years. It did not hold up on SOXL.
- **Calendar.** `levx.EARLY_CLOSE` lists the 13:00 closes through 2027-11-26. Add the next
  year's dates each December.
- **Thin funds.** Resting limit orders might cut the spread in AAOX, COHX and LITX. That is
  not tested: a missed fill breaks the rule, and fills come mostly when the price is moving
  against the order.
