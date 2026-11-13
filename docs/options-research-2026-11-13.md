# Options: why the tracks were retired, and what real prices say (2026-11-13)

**Asked by Ryan, live turn 2026-11-13:** *"Why did we retire the options tracks? Did we never
determine a good way to implement options trading. I know there is definitely a strategy out
there or the knowledge to do it well. Can we figure that out?"*

**Short answer.** The retired tracks bought option premium, which is the side that pays the
premium, at a cadence that could not manage the exits. The documented edge is on the selling
side. This document tests that side on real option prices for the first time. It made a small
average profit that cannot be told apart from zero, has shrunk since 2022, and cannot be sized
safely on this account. Options stay closed in the agent account. Section 6 lists what would
change that.

Code: `options_backtest.py` (tests: `test_options_backtest.py`). Data: `data/options/spy_put_cycles.json`.

## 1. Why the tracks were retired (the record)

| Track | What it did | Result | Retired |
|---|---|---|---|
| Long single legs and debit spreads, 7 to 45 days | Bought calls and puts on graded names | -$572 over the 3 months to 2026-09-24; average loss 1.4 times the average win | 2026-09-30, with the options bucket |
| TACTICAL scalps | Intraday breakout options, exits checked every 15 minutes | 407 market-hours runs, 85 fully evaluated triggers, 0 trades; both exits sat inside one median overnight gap | 2026-09-14 |
| 0DTE credit spreads (shortlist idea) | Never traded | Modelled only: "the credit is unverified; log real quotes first". Banned at a 15-minute cadence | Never opened |

Three things were wrong with the approach, in order of weight:

1. **It bought premium.** An option buyer pays the volatility premium on every trade and needs
   to be right on direction, size and timing. The agent's stock signals had no such edge on a
   7 to 45 day horizon.
2. **The exits could not be enforced.** A run every 15 minutes with no resting order cannot
   manage a short-dated option. That is what the TACTICAL gap study measured.
3. **The chains were too wide.** Of five single-name candidates in the week of 2026-08-10, four
   quoted 12% to 50% of mid.

A selling strategy was never tested, because there were no historical option prices to test it on.

## 2. What is new: real historical option prices

Robinhood keeps daily price bars for expired option contracts back to at least November 2017
(a December 2015 contract returned nothing):

```
get_option_instruments(chain_symbol="SPY", expiration_dates="2020-03-20", type="put",
                       state="expired", strike_price="300.0000")      -> the contract id
get_option_historicals(instrument_ids=[id], start_time=..., end_time=..., interval="day")
```

Data notes, all measured on 2026-11-13:

| Check | Result |
|---|---|
| Is the price the close? | Yes. Before June 2020 a bar's open equals its close. On 2020-03-12, 03-13 and 03-20 the SPY 300 put's bar matched SPY's closing intrinsic value, not the open's. |
| Coverage | All 530 strikes priced for 106 monthly cycles. 5 odd-dollar strikes were not listed, 9 had no trade on the entry day and 1 had a placeholder price; all 15 were replaced by the nearest $5 strike. |
| Internal consistency | Put prices fall with the strike in all 106 cycles. |
| Fields not to use | `high_price` and `low_price` are noisy (some sit at 1 cent). Bars flagged `interpolated` carry no trade. |
| Intraday bars | 5-minute bars exist for a contract that expired the day before (2026-11-12). A June 2024 contract returned only gap-fill. Same-day (0DTE) ideas cannot be tested over years from this source. |
| Check against a published index | Selling the at-the-money put each cycle tracks the Cboe PutWrite index over the same 106 cycles with a correlation of 0.966. The index made 8.1% a year including interest on the collateral; this test made 4.5% before interest. |
| Pull cost | 530 contract lookups and 106 price calls: about 7 minutes across three background workers, and about 1.2 million tokens. Their saved tool output was parsed by script, so no price was retyped. **Do pulls like this after the bell:** this one exhausted the account's 5-hour usage allowance during market hours and the trading routine's runs failed for the last 40 minutes of the session (CLAUDE.md, usage incident 2026-11-13). |

## 3. The test

- **Trade:** sell SPY puts or put credit spreads at the close of the first trading day after each
  monthly expiration, into the next monthly expiration (25 to 35 days), and hold to expiration.
- **Strikes:** spot x (1 - z x VIX x sqrt(days / 365)) for z = 0, 0.5, 1, 1.5, 2. On 2026-11-13
  z = 0.5 was a 27-delta put and z = 1.0 a 16-delta put.
- **Sample:** 106 cycles, 2017-12-18 to 2026-10-16. It includes February 2018, the fourth quarter
  of 2018, March 2020, 2022 and April 2025.
- **Costs:** half a bid/ask spread per leg at entry (the larger of 1 cent and 0.4% of the leg;
  measured live at 1.5 to 2 cents on $3.50 to $8 legs), $0.04 a contract in fees, and a second
  crossing when the short strike ends within 1% of the money.
- **Fixed-width spreads** price the long leg from implied volatility interpolated between the
  pulled strikes. On the live chain of 2026-11-13 the method was within half a cent on 6 strikes.

## 4. Results

Per one contract or one spread, every month, at the modelled cost. SPY held over the same cycles
returned 14.2% a year with a -28.6% drawdown at cycle ends.

| Structure | Win rate | Avg credit | Max risk | Avg P/L a month | Worst month | t-stat | Capital at risk each month: growth a year / worst drawdown |
|---|---|---|---|---|---|---|---|
| Cash-secured put, at the money | 78.3% | $740 | $43,062 | +$200 | -$8,601 | 1.28 | 100% collateralised: 4.5% / -27% (before interest on the cash) |
| Cash-secured put, 27 delta | 86.8% | $405 | $42,251 | +$131 | -$7,897 | 0.94 | 100% collateralised: 2.7% / -26% |
| Put spread, short 27 delta, $5 wide | 84.9% | $87 | $413 | +$15 | -$465 | 0.90 | 10%: 3.4% / -24%. 20%: 4.1% / -45%. 50%: -15.1% / -94% |
| Put spread, short 27 delta, $10 wide | 84.9% | $153 | $847 | +$28 | -$902 | 0.91 | 10%: 3.2% / -24%. 20%: 4.3% / -47% |
| Put spread, short 16 delta, $10 wide | 89.6% | $81 | $919 | +$23 | -$954 | 1.12 | 10%: 2.7% / -14%. 20%: 4.7% / -29% |
| Put spread, short 16 delta / long z = 2 | 90.6% | $144 | $2,152 | +$53 | -$2,010 | 1.03 | 10%: 2.0% / -13%. 20%: 3.6% / -25% |

What the numbers say about the $5-wide spread, the only size this account could hold:

1. **The average is positive and small.** $15 a month per spread, $1,588 over 106 months.
   Trading costs took $5 of the $20 gross.
2. **It is not distinguishable from zero.** The 90% interval for the mean is -3.3% to +10.1% of
   risk per month, with an 18% chance the true mean is zero or negative.
3. **It needs an 82% win rate to break even and got 84.9%.** Sixteen losing months averaged
   -$385; ninety winning months averaged +$86.
4. **The edge has shrunk.** $24 a month for expirations in 2018-21, $8 a month in 2022-26.
5. **It cannot be sized up.** With half the capital at risk each month the account loses 94%.
   Growth peaks near 15% to 20% of capital at risk, at about 4% a year with a -34% to -45% drawdown.
6. **Selling after a dip did not help.** Entries after a down week made $2 a month; entries after
   an up week made $25. Entries with the VIX under 14 lost $28 a month. These splits are small
   samples (20 to 59 cycles) and are descriptions, not rules.

By expiration year, one $5-wide spread a month: 2018 -$700, 2019 +$555, 2020 +$319, 2021 +$971,
2022 -$427, 2023 +$57, 2024 +$485, 2025 -$17, 2026 +$344 (10 months).

At twice the modelled cost the average falls from $15.0 to $9.7 a month.

## 5. Why it does not fit this account today

| Constraint | Number |
|---|---|
| Sleeve money (2026-11-13) | About $1,800 |
| One $5-wide SPY put spread at risk | $413, which is 23% of it |
| Size that maximised growth in the test | 15% to 20% of capital at risk |
| Expected profit at one $3-wide spread a month ($250 at risk) | About $9 a month, with an 18% chance the edge is zero |
| What the money earns in the sleeves it would come from | About 30% a year in the backtests |
| Index options instead (XSP, cash-settled) | $0.78 in fees per spread against $0.08 for SPY (order preview, 2026-11-13), and 5-contract quotes 5 to 6 cents wide |

One option contract controls about $75,000 of SPY. On $1,800 that is too coarse in both
directions: a long option is far more exposure than any tested sleeve weight, and a short spread
small enough to survive earns single dollars.

## 6. What would change the answer

1. **Size.** With sleeve money above about $15,000 a $5-wide spread is under 3% of it, several
   expirations can be staggered, and the test is worth repeating as a paper sleeve first.
2. **A larger sample.** Weekly entries give about four times the cycles for the same years. That
   would narrow the interval in point 2 above.
3. **A timing rule that holds up.** Entries tied to the sleeves' own signals, or an exit at half
   the credit using daily bars, are untested. The dip split above is a first warning that the
   obvious timing idea may be backwards.
4. **Multi-leg orders.** The connector's order tools now describe multi-leg spreads as supported
   on level-3 accounts, and a two-leg SPY put credit spread reviewed clean on 2026-11-13 ($500
   collateral, $0.08 in fees). On 2026-08-24 the same review was clean and the order was then
   rejected, so this is unproven until one order is accepted. A test order priced far from the
   market and cancelled at once would settle it for no cost. It needs a live Ryan turn.

## 7. Also considered

| Idea | Why not |
|---|---|
| Buy calls on the swing sleeves' signals instead of QLD | One QQQ contract is about $68,000 of exposure against a sleeve target of about $700. A deep in-the-money call costs more than the account. |
| Hold LEVX's overnight edge through options | Crossing an option's bid/ask twice a day costs roughly 0.5% a round trip (estimate) against a measured 0.02% for TQQQ shares. |
| Cash-secured puts or covered calls in the agent account | $43,000 of collateral per SPY contract; the sleeves hold fractional shares. |
| Covered calls on the joint account's SOXL at the sell-ladder prices | 104 shares is one contract, which would sell the whole position at the first rung instead of 26 shares. The joint account has no options approval. |

## 8. What the published evidence says

| Finding | Source |
|---|---|
| Buying index options has lost money on average. At-the-money S&P 500 straddles lost about 3% a week, and put returns ran below the risk-free rate. | Coval and Shumway, "Expected Option Returns", Journal of Finance 56(3), 2001. [EconPapers](https://econpapers.repec.org/RePEc:bla:jfinan:v:56:y:2001:i:3:p:983-1009) |
| Selling the at-the-money S&P 500 put each month returned 9.54% a year from 1986 to 2018 with 9.95% volatility, against 14.93% volatility for the S&P 500 at a comparable return. The figures are before costs, and the index history before 2007 was built after the fact. | Bondarenko, "Historical Performance of Put-Writing Strategies", 2019, commissioned by Cboe. [Cboe summary](https://www.cboe.com/insights/posts/white-paper-shows-volatility-risk-premium-facilitated-higher-risk-adjusted-returns-for-put-index), [CXO Advisory review](https://www.cxoadvisory.com/equity-options/performance-of-cboe-putwrite-indexes) |
| Retail option traders favour cheap, short-dated contracts with an average bid/ask spread of 12.6%, and lose money on average. | Bryzgalova, Pavlova and Sikorskaya, "Retail Trading in Options and the Rise of the Big Three Wholesalers", Journal of Finance 78(6), 2023. [London Business School](https://www.london.edu/faculty-and-research/academic-research/r/retail-trading-in-options-and-the-rise-of-the-big-three-wholesalers) |
| Robinhood charges $0.50 a contract on index options ($0.35 with Gold) and nothing on stock and ETF options beyond regulatory fees. Index options settle in cash. | Robinhood, [Trading fees](https://robinhood.com/us/en/support/articles/trading-fees-on-robinhood) and [Index options](https://robinhood.com/us/en/support/articles/index-options) |

The Cboe PutWrite index against the S&P 500 total return, from Yahoo Finance daily closes
(`^PUT`, `^SP500TR`) pulled 2026-11-13:

| Window | PutWrite index: return a year / worst drawdown | S&P 500 total return: return a year / worst drawdown |
|---|---|---|
| 2005 to 2026 | 7.6% / -37% | 10.8% / -55% |
| 2005 to 2011 | 6.0% / -37% | 2.8% / -55% |
| 2012 to 2026 | 8.3% / -30% | 14.8% / -34% |
| 2018 to 2026 | 8.1% / -30% | 14.1% / -34% |

Read together: the premium is real and sits on the selling side, which is the opposite of what the
retired tracks did. It paid best when stocks went nowhere (2005 to 2011). Since 2012 the index has
earned a little over half of what the S&P 500 earned, with almost the same worst drawdown. That
matches section 4.

## 9. Not verified

- The other Cboe strategy indices (BuyWrite, iron condor, put protection, weekly PutWrite): Yahoo
  serves only their latest value, and the background literature review stopped when the usage limit
  was reached. Nothing from it is used here.
- Whether XSP options are European-style on Robinhood (no early assignment) and their tax treatment.
  The sources found confirm cash settlement only.
- Bid/ask spreads before 2026. The cost model uses spreads measured on 2026-11-13.
- Any exit before expiration. The test holds every position to expiration.
