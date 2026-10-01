# Limit-entry backtest — run 2026-10-01 19:29Z

Period 2019-01-02 → 2026-10-01 (7.7 yrs). SWING_Q = QQQ signals at 2x; SWING_M = monthly top-10 at 1x; MIX = 70/30, monthly rebalance (live split). 1 bp per side. Self-check passed: with the limit off, the code reproduces the tested sleeve exactly.

**QQQ buy-and-hold:** 23.2%/yr, max DD -35.1%.


## Optimistic fills (limit fills if the low touches it)

| Variant | MIX CAGR / max DD | MIX 2019–22 | MIX 2023–26 | SWING_Q CAGR / DD | SWING_M CAGR / DD |
|---|---|---|---|---|---|
| Baseline (buy at the close, as tested) | **37.7% / -22.2%** | 37.5% / -20% | 38.5% / -22% | 40.5% / -28% | 29.5% / -21% |
| RSI-trigger price | **37.2% / -22.5%** | 37.0% / -20% | 38.0% / -23% | 39.4% / -28% | 30.0% / -22% |
| RSI-trigger price -1% | **37.7% / -22.4%** | 38.3% / -20% | 37.8% / -22% | 40.3% / -28% | 30.1% / -21% |
| pct: 1% below prior close | **31.4% / -26.3%** | 29.1% / -26% | 34.6% / -25% | 34.4% / -35% | 22.6% / -25% |
| pct: 2% below prior close | **34.5% / -23.0%** | 32.2% / -22% | 37.7% / -23% | 37.3% / -30% | 26.5% / -23% |
| pct: 3% below prior close | **36.9% / -22.9%** | 37.2% / -20% | 37.2% / -23% | 39.4% / -28% | 29.2% / -22% |
| pct: 5% below prior close | **39.2% / -22.7%** | 40.0% / -19% | 39.0% / -23% | 42.1% / -28% | 30.8% / -20% |

## Pessimistic fills (the low must trade 0.1% through the limit)

| Variant | MIX CAGR / max DD | MIX 2019–22 | MIX 2023–26 | SWING_Q CAGR / DD | SWING_M CAGR / DD |
|---|---|---|---|---|---|
| RSI-trigger price | **36.3% / -22.5%** | 36.5% / -20% | 36.7% / -23% | 38.5% / -28% | 29.3% / -22% |
| RSI-trigger price -1% | **37.6% / -22.4%** | 38.1% / -20% | 37.7% / -22% | 40.3% / -28% | 29.7% / -21% |
| pct: 1% below prior close | **26.9% / -26.5%** | 25.2% / -27% | 29.4% / -25% | 29.7% / -35% | 18.8% / -25% |
| pct: 2% below prior close | **32.8% / -23.1%** | 30.6% / -22% | 35.9% / -23% | 36.1% / -30% | 23.7% / -24% |
| pct: 3% below prior close | **36.4% / -22.9%** | 36.6% / -20% | 36.9% / -23% | 39.4% / -28% | 27.7% / -22% |
| pct: 5% below prior close | **39.1% / -22.7%** | 39.9% / -19% | 38.9% / -23% | 42.1% / -28% | 30.3% / -20% |

## Fill detail (per position, extra return vs buying at the close that day)

| Variant | Fills | SWING_Q (QLD, 2x) | SWING_M (per name) |
|---|---|---|---|
| RSI-trigger price | opt. | 7/yr; 64% confirmed (+-80 bp each) / 36% not (+116 bp each); net -9 bp per fill | 69/yr; 55% confirmed (+-80 bp each) / 45% not (+113 bp each); net +6 bp per fill |
| RSI-trigger price -1% | opt. | 2/yr; 83% confirmed (+-53 bp each) / 17% not (+232 bp each); net -5 bp per fill | 37/yr; 75% confirmed (+-43 bp each) / 25% not (+182 bp each); net +13 bp per fill |
| pct: 1% below prior close | opt. | 28/yr; 44% confirmed (+-135 bp each) / 56% not (+82 bp each); net -14 bp per fill | 549/yr; 36% confirmed (+-127 bp each) / 64% not (+57 bp each); net -9 bp per fill |
| pct: 2% below prior close | opt. | 9/yr; 67% confirmed (+-68 bp each) / 33% not (+66 bp each); net -24 bp per fill | 305/yr; 42% confirmed (+-119 bp each) / 58% not (+75 bp each); net -7 bp per fill |
| pct: 3% below prior close | opt. | 3/yr; 65% confirmed (+-78 bp each) / 35% not (+64 bp each); net -28 bp per fill | 176/yr; 46% confirmed (+-109 bp each) / 54% not (+95 bp each); net +0 bp per fill |
| pct: 5% below prior close | opt. | 0/yr; 0% confirmed (+0 bp each) / 100% not (+299 bp each); net +299 bp per fill | 60/yr; 50% confirmed (+-108 bp each) / 50% not (+143 bp each); net +19 bp per fill |
| RSI-trigger price | pess. | 7/yr; 65% confirmed (+-90 bp each) / 35% not (+112 bp each); net -20 bp per fill | 65/yr; 58% confirmed (+-82 bp each) / 42% not (+110 bp each); net -2 bp per fill |
| RSI-trigger price -1% | pess. | 2/yr; 83% confirmed (+-53 bp each) / 17% not (+232 bp each); net -5 bp per fill | 34/yr; 76% confirmed (+-48 bp each) / 24% not (+177 bp each); net +6 bp per fill |
| pct: 1% below prior close | pess. | 25/yr; 47% confirmed (+-140 bp each) / 53% not (+67 bp each); net -30 bp per fill | 520/yr; 37% confirmed (+-132 bp each) / 63% not (+52 bp each); net -16 bp per fill |
| pct: 2% below prior close | pess. | 8/yr; 66% confirmed (+-86 bp each) / 34% not (+57 bp each); net -37 bp per fill | 286/yr; 43% confirmed (+-128 bp each) / 57% not (+69 bp each); net -15 bp per fill |
| pct: 3% below prior close | pess. | 3/yr; 65% confirmed (+-78 bp each) / 35% not (+64 bp each); net -28 bp per fill | 166/yr; 47% confirmed (+-118 bp each) / 53% not (+90 bp each); net -7 bp per fill |
| pct: 5% below prior close | pess. | 0/yr; 0% confirmed (+0 bp each) / 100% not (+299 bp each); net +299 bp per fill | 57/yr; 50% confirmed (+-117 bp each) / 50% not (+140 bp each); net +13 bp per fill |

*Confirmed* = the close kept the position (the gain is the entry below the close). *Not* = the close did not confirm, sold at the close the same day (loss incl. two fees).
