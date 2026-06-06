# Stock Autopilot

Read-only daily market analysis for a small Robinhood account. **It generates reports; it does NOT place trades.** All execution happens in an interactive session with per-order human approval.

## What it does
Two strategies, one history pull per name (FMP Starter API):
1. **12-1 cross-sectional momentum** — multi-week/monthly trend ranking (Jegadeesh-Titman).
2. **Connors RSI(2) mean-reversion swing** — buy oversold (RSI2<10) names inside a rising 200-day uptrend; 1-3 week holds with ATR-style stops/targets.

The report flags **ACTION / NO ACTION**, tags each setup by theme, and auto-warns on:
- **Correlated clusters** (e.g. many AI/semi setups = one bet, not diversification)
- **Speculative names** (size tiny; keep total spec exposure ≤ ~20-25%)
- **Wide stops** (>15% = extreme volatility)

## Run
```
FMP_API_KEY=xxx python report.py --mode morning     # full scan
FMP_API_KEY=xxx python report.py --mode intraday     # live-price refresh on near-trigger names
```
Reports are written to `logs/report_*.md` (+ `.json`). Key is read from `FMP_API_KEY` env var, else `.env`.

## Schedule
- 9:30 AM CT — morning full scan
- 2:30 PM CT — intraday refresh
Runs as local Windows tasks and/or a remote claude.ai routine.

## Guardrails (non-negotiable)
- **No unattended trading.** Scheduled runs are analysis-only.
- Every order needs per-order user approval, placed only on the agentic cash account.
- Stops on every entry; per-name cap ~15-20%; benchmark monthly vs SPY.

## Files
- `report.py` — combined twice-daily report (both strategies + concentration analysis)
- `analyze.py` — universe, FMP data helpers, momentum + indicator math, theme map
- `logs/` — generated reports (gitignored except as noted)
