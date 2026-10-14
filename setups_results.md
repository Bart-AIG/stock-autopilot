# Chart-setup score backtest (setups.py)

Run 2026-10-14 04:43Z. 159 large caps (S&P 100 + Nasdaq-100 as of end-2018), scored every 2 sessions from 2019-01-01, by the production scorer on daily OHLC + volume. Returns are in EXCESS of SPY over the same window. **In band** = price -8% to +5% vs its 200-day SMA, the Quality @ 200-day list's band.

Samples: 151260 total, 51418 in band.

## 1. Does ranking by score pick better names? (the question asked)

On each date the in-band names are ranked by setup score. **IC** = rank correlation of score with the next 63-session excess return (0 = no information; +0.05 is a useful ranking signal in practice). **Top 3** = the 3 highest-scored names' excess over the average in-band name that day. Non-overlapping = dates 63+ sessions apart, so each move counts once: trust that column, and its t-stat (|t| >= 2 is the usual bar).

| Sample | Dates | IC mean | IC > 0 | Non-overlap dates | IC (non-overlap) | t | Top 3 vs avg | Top 3 wins | Top 3 (non-overlap) | t |
|---|---|---|---|---|---|---|---|---|---|---|
| In band, 2019-2026 | 923 | -0.039 | 40% | 29 | -0.111 | -3.1 | -0.56% | 46% | -3.54% | -2.0 |
| In band, 2019-2022 | 480 | -0.031 | 40% | 15 | -0.125 | -2.5 | +0.04% | 50% | -3.89% | -1.8 |
| In band, 2023-2026 | 443 | -0.048 | 40% | 14 | -0.095 | -1.8 | -1.20% | 43% | -3.17% | -1.1 |
| All samples (any distance) | 923 | -0.037 | 39% | 29 | -0.060 | -2.1 | -1.32% | 40% | -3.44% | -2.0 |

## 2. Return by label and by score quintile

### In band: by label

| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |
|---|---|---|---|---|---|---|
| WEAK | 17842 | -0.06% | +0.35% | -0.62% | 48.2% | -0.96% |
| NEUTRAL | 14461 | -0.27% | -0.63% | -1.60% | 44.6% | -1.23% |
| CONSTRUCTIVE | 11030 | -0.27% | -0.75% | -1.63% | 44.9% | -1.40% |
| STRONG | 6324 | -0.53% | -1.06% | -1.65% | 45.0% | -1.27% |
| **All** | 49657 | -0.23% | -0.36% | -1.23% | 46.0% | -1.18% |

### In band: by score quintile (Q5 = highest scores)

| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |
|---|---|---|---|---|---|---|
| Q1 | 11227 | +0.09% | +0.57% | -0.35% | 49.0% | -0.62% |
| Q2 | 10353 | -0.33% | -0.24% | -1.19% | 46.3% | -1.59% |
| Q3 | 10723 | -0.24% | -0.62% | -1.64% | 44.4% | -1.07% |
| Q4 | 7903 | -0.13% | -0.49% | -1.36% | 45.6% | -1.12% |
| Q5 | 9451 | -0.56% | -1.17% | -1.85% | 44.3% | -1.54% |
| **All** | 49657 | -0.23% | -0.36% | -1.23% | 46.0% | -1.18% |

### In band, 2019-2022: by label

| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |
|---|---|---|---|---|---|---|
| WEAK | 8483 | +0.61% | +1.37% | +0.54% | 52.1% | +1.51% |
| NEUTRAL | 7267 | +0.18% | +0.51% | -0.34% | 48.8% | +1.05% |
| CONSTRUCTIVE | 5490 | +0.23% | +0.62% | -0.10% | 49.6% | +0.98% |
| STRONG | 3110 | -0.42% | +0.26% | -0.25% | 48.9% | +0.80% |
| **All** | 24350 | +0.26% | +0.80% | +0.03% | 50.1% | +1.16% |

### In band, 2023-2026: by label

| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |
|---|---|---|---|---|---|---|
| WEAK | 9359 | -0.65% | -0.57% | -1.73% | 44.7% | -3.34% |
| NEUTRAL | 7194 | -0.70% | -1.78% | -3.06% | 40.4% | -3.70% |
| CONSTRUCTIVE | 5540 | -0.74% | -2.10% | -3.45% | 40.2% | -3.91% |
| STRONG | 3214 | -0.64% | -2.34% | -3.57% | 41.1% | -3.45% |
| **All** | 25307 | -0.68% | -1.47% | -2.73% | 42.0% | -3.58% |

### All samples: by label

| Bucket | n (63d) | 21d excess | 63d excess | 63d median | 63d beat SPY | 126d excess |
|---|---|---|---|---|---|---|
| WEAK | 43230 | +0.24% | +0.73% | -0.40% | 48.8% | +0.04% |
| NEUTRAL | 46546 | -0.11% | -0.22% | -1.24% | 46.0% | +0.27% |
| CONSTRUCTIVE | 36634 | -0.13% | -0.37% | -1.25% | 45.8% | -0.32% |
| STRONG | 19918 | -0.41% | -0.99% | -1.52% | 45.1% | -0.97% |
| **All** | 146328 | -0.05% | -0.08% | -1.05% | 46.7% | -0.11% |

## 3. Each component on its own (in band, 63-session excess)

| Component | n with | Excess with | n without | Excess without | Difference | Beat SPY with |
|---|---|---|---|---|---|---|
| bull_flag:forming | 1345 | +0.64% | 48312 | -0.39% | +1.03% | 48.8% |
| bull_flag:near | 761 | -1.92% | 48896 | -0.33% | -1.59% | 41.8% |
| double_bottom:breakout | 2631 | -1.54% | 47026 | -0.29% | -1.25% | 43.0% |
| double_bottom:forming | 6281 | -0.44% | 43376 | -0.35% | -0.10% | 45.6% |
| double_bottom:fresh_breakout | 1474 | -0.94% | 48183 | -0.34% | -0.60% | 44.5% |
| double_bottom:near | 2979 | -1.29% | 46678 | -0.30% | -1.00% | 42.2% |
| falling_wedge:breakout | 1257 | -1.27% | 48400 | -0.33% | -0.94% | 45.4% |
| falling_wedge:forming | 1397 | +0.77% | 48260 | -0.39% | +1.16% | 49.7% |
| falling_wedge:fresh_breakout | 2539 | -0.78% | 47118 | -0.33% | -0.44% | 45.1% |
| falling_wedge:near | 2126 | -1.16% | 47531 | -0.32% | -0.84% | 43.8% |
| higher_low | 24550 | -0.67% | 25107 | -0.05% | -0.62% | 45.2% |
| macd_above | 16470 | -0.51% | 33187 | -0.28% | -0.23% | 45.4% |
| macd_cross | 9519 | -0.11% | 40138 | -0.42% | +0.30% | 46.8% |
| pen_60d_low | 5624 | +0.37% | 44033 | -0.45% | +0.82% | 48.1% |
| pen_falling_50d | 19491 | +0.26% | 30166 | -0.76% | +1.01% | 47.9% |
| reclaim_50d | 11513 | -0.44% | 38144 | -0.33% | -0.10% | 46.2% |
| rising_20d | 19159 | -0.82% | 30498 | -0.07% | -0.75% | 44.8% |
| rsi_divergence | 3420 | +0.41% | 46237 | -0.41% | +0.82% | 47.3% |
| up_volume | 23522 | -0.77% | 26135 | +0.02% | -0.79% | 45.3% |

## Honest limits

- Samples overlap: a 63-session return sampled every 2 sessions counts the same move ~31 times. The non-overlapping IC and top-3 columns, with their t-stats, are the evidence; the rest is description.
- The business-quality screen (margins, growth, ROE) can't be applied point in time, so this is the chart score on large caps near their 200-day, not the exact list.
- Constituents are as of end-2018 (no hindsight), but names acquired since drop out if FMP lacks their history: a small survivorship bias toward names that lasted.
- No costs: these are signal tests, not a strategy.
