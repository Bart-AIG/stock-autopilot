# Joint account: leveraged ETF process (proposed 2026-11-26)

Ryan places every trade by hand. The agent cannot trade the joint account. Evidence for every rule below: `letf_joint_results.md`. Nothing here is a forecast; the numbers are backtests.

## The rule, in one box

| | |
|---|---|
| **Fund** | UPRO (3x S&P 500). Signals come from **SPY**, never from UPRO itself |
| **Turn ON** | SPY closes more than **2% above** its 200-day simple moving average |
| **Turn OFF** | SPY closes more than **2% below** its 200-day average |
| **In between** | Do nothing. Keep whatever state you are in |
| **Size while ON** | % of the sleeve in UPRO = the smaller of 100% and 16.7% / SPY's 20-day realized volatility. The rest stays in cash. Set every Friday |
| **When to trade** | At the close on the day it fires (2:45-2:55 PM CT), or the next morning. The backtest found under 1.2 points a year between the two |
| **Exits** | Only the OFF line. No stops, no targets, no news overrides |

Backtest 1993-2026, after 5 bp a side: **17.3% a year before tax, about 14.5% after tax, worst drawdown -48%, about 3 trades a year.** Holding SPY: 10.6% / 10.0% / -55%. Holding UPRO-like 3x: 13.0% / 12.4% / -98%.

## Before the first trade

1. **Do not fund this sleeve with margin.** The joint account is at about 2x today (net equity $49,533, cash -$48,224 on 2026-11-26). A 3x fund on margin is leverage on leverage, and Robinhood can raise a position's maintenance requirement or sell without notice. Fund the sleeve only with money that does not increase the margin balance: the debit is zero, or you sell the same dollar amount of other holdings that day.
2. **Cap the sleeve at 20% of net equity** (about $9,900 today). The backtest's worst drawdown on this sleeve was -48%, so plan on losing about half of it at some point. At 20% that is about -10% on the whole account.
3. **Use UPRO for the S&P sleeve.** The agentic account trades QLD, TQQQ and SOXL. A loss you take in the joint on one of those within 30 days of an agentic buy is a wash sale (purchases in your other accounts count). UPRO has no overlap today.
4. **Optional second leg: TQQQ on QQQ's signal, at most half the sleeve.** Same rule. It needs the daily exit check, because weekly-only checks cost 3 to 5 points a year on Nasdaq. It overlaps with the agentic account's TQQQ and QLD for wash sales.
5. **SOXL: a small satellite at most** (a quarter of the sleeve or less), same rule on SOXX. The rule held SOXL at 41-45% size through a -58% drop in October 2026 before it exited on Nov 2.

## The phone push does the arithmetic (live 2026-11-27)

The **LETF signal** job (`.github/workflows/letf-signal.yml`, code `letf_signal.py`) reads SPY, QQQ and SOXX after every hourly Stock Report run and pushes to your phone. The latest numbers are always in `letf_signal_report.md` (the push links to it). It never trades and uses no Claude usage.

| Push | When | What to do |
|---|---|---|
| **LETF Friday update** | The first run at or after 1:00 pm CT on a Friday (about 1:09 pm), with live prices | The weekly step below. If the close then changes the answer, a second push says so |
| **LETF heads-up** | Any day a live price is past the line that would flip a signal, once per index per day | Look again near 2:45 pm CT and trade only if it is still across |
| **LETF signal: X turned ON / OFF** | A confirmed close flipped a signal (one you did not act on, or one that changed on the close) | Trade the next morning. The backtest found that as good as trading at the close |
| **Catch-up** | No weekly update for 8 days (a missed Friday) | The weekly step, on Monday |

The push decides nothing for you and does not know what you hold. The signal is the **close**; a heads-up is a cue to look.

Optional backup if the push ever goes quiet: a Robinhood alert on SPY crossing its 200-day SMA (`price_crosses_sma`, period 200, daily bars). It never needs re-setting.

## Every Friday, when the update arrives (10 minutes, before the 3:00 PM CT close)

1. Read the update. It gives each index's state, its ON and OFF lines, its 20-day volatility and the size.
2. **It says BUY:** buy UPRO for the size it gives.
3. **It says SELL:** sell all UPRO.
4. **It says hold, with a size:** compare the size to what you hold. Trade only if it differs by more than a sixth of the sleeve, which is about 0.5x of exposure (the backtest's threshold).
5. Log it: date, SPY close, 200-day, state, size, the trade if any.

## Any day a heads-up arrives

1. Near 2:45 PM CT, check SPY against the line in the push. If it is still across, place the trade before the 3:00 PM CT close. Otherwise do nothing.
2. If you miss the close, the confirmed-flip push follows after the close. Trade the next morning; that is equally valid in the backtest.

The job reads the unadjusted closes your Robinhood chart shows, while the backtest used dividend-adjusted closes. That changed the SPY signal on 2.2% of days from 2011 to 2026, and the rule's result by -0.5 to +0.4 points a year across the three indexes.

## Size table (SPY's 20-day realized volatility to % of the sleeve in UPRO)

| SPY 20-day vol | 15% or less | 20% | 25% | 30% | 35% | 40% | 50% |
|---|---|---|---|---|---|---|---|
| % of sleeve in UPRO | 100% | 83% | 67% | 56% | 48% | 42% | 33% |
| Exposure to the S&P | 3.0x | 2.5x | 2.0x | 1.7x | 1.4x | 1.3x | 1.0x |

In the backtest the rule was ON 77% of days, at 2.9x on average.

## What NOT to do (each is a measured loser)

1. **Do not buy a leveraged fund while its index is OFF.** That is dip buying in a downtrend, the pattern behind most of the joint's **-$17,969** on 33 leveraged-fund closes since 2026-10-15.
2. **No single-stock leveraged funds** (NVDL, MUU, AAOX, COHX, NEBX and the like) in this process. Round-trip spreads were 0.3% to 1.1% when measured, and each has earnings gaps and no long history.
3. **No day trading.** The only day rules that beat costs need a check every 30 minutes or a 3:50 PM buy and 9:31 AM sell every day, and the agentic account already runs them.
4. **Do not use RSI as the trigger.** RSI(2) dips lose 4 to 5 points a year to short-term tax in this account. Weekly RSI(14) > 50 was the worst trend rule on every index.
5. **No stops, no overrides on headlines.** The tested rule has none. The OFF line is the exit.
6. **Do not hold a 3x fund "until it comes back".** Held through 2000-02, the 3x Nasdaq and semis funds went to zero.

## What to expect

- **Losing years are normal.** The S&P rule lost money in 11 of 33 years and trailed plain SPY in 12. Bad ones: 2022 -36%, 2018 -24%, 2007 -23%, **2026 to date -23%** (out in March, back in in April, out at the November low).
- **The payoff is skipping crashes.** 2000-02 rule -18% / +3% / -14% against -46% / -46% / -63% for 3x held; 2008 +1% against -86%.
- **Whipsaws cost tax too.** Most gains are short term. A re-entry within 30 days of a loss exit defers that loss (wash sale). The backtest's tax drag was about 3 points a year at 32% short-term / 15% long-term.
- **A crash straight out of a calm uptrend is not covered.** The rule was out before Black Monday 1987 only because the S&P had already closed 5.4% under its 200-day that Friday.

## Today (closes of 2026-11-25; the lines move a little each day)

| Index | Close | 200-day | State | Turns ON above | 20-day vol | Size if ON |
|---|---|---|---|---|---|---|
| SPY (for UPRO) | 716.70 | 733.16 | **OFF** since 11-20 | **747.82** (+4.3%) | 32% | 53% of the sleeve |
| QQQ (for TQQQ) | 633.93 | 683.50 | **OFF** since 11-05 | **697.17** (+10.0%) | 48% | 35% |
| SOXX (for SOXL) | 127.98 | 161.20 | **OFF** since 11-02 | **164.43** (+28.5%) | 99% | 17% |

**Today the process holds no leveraged index fund.** The next action is an entry, not an exit. The only leveraged fund in the joint today is MUU (25 shares, about $235), a single-stock fund outside this process.
