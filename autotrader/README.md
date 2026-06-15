# Auto-trader (decision/execution layer) — PARKED

> **Status: not the active mode.** Fully-unattended Robinhood trading is blocked —
> Robinhood has no trading API and the account can't expose an authenticator-app TOTP
> seed, so a scheduled job can't log in headlessly. The **active** mode is **semi-auto
> one-tap approval, run in a Claude session** (see "One-tap batch approval" in
> `CLAUDE.md`). This package is kept as the reference for the session's sizing/gate
> logic and as a ~90%-reusable base for a future pivot to a broker with an official API
> (e.g. **Alpaca**) — only `executor_robinhood.py` would be swapped.

Turns the read-only strategy report into REAL trades with hard guardrails and an
LLM news/thesis veto-gate.

## Pipeline
```
report.py → logs/report_*_<mode>.json   (mechanical RSI2/momentum/MA signals)
   → build_orders.py   propose sells / trail-stops / buys, sized down
   → guardrails.py     caps · allowlist · staleness · kill-switch
   → thesis_gate.py    Claude checks recent news+analysts; VETOES weak/broken buys
   → executor_robinhood.py   market orders + GTC whole-share stops (robin_stocks)
```
Run it **inside the same GitHub Actions job that made the report** — the JSON lives
in `logs/` (gitignored), so a fresh checkout won't see it.

```bash
python -m autotrader.run --mode intraday
```

## Safety model
- **Dry-run by default.** Nothing places unless `AUTOTRADE_LIVE=1` **and** all RH
  creds are set. The first runs should be dry-run — read `logs/orders.json` to see
  exactly what it WOULD do.
- **Allowlist:** only tickers in *today's* report can be traded.
- **Sized down:** ≤ `$300`/order, ≤ `$600`/day, ≤ 18% of account per name, keep a
  cash buffer, respect the speculative-sleeve cap.
- **Kill-switch:** if day P&L ≤ `-$150`, all BUYS are blocked (exits still run).
- **LLM gate fails CLOSED:** any gate error/uncertainty vetoes the buy. Exits and
  trail-stops are never gated (risk reduction must not be blocked).
- **Stops placed atomically:** every buy fill immediately gets a GTC `stop_market`
  on its whole-share portion; the fractional remainder is monitored only.

All limits are env-overridable — see `guardrails.py` (`AT_MAX_PER_ORDER_USD`,
`AT_MAX_PER_DAY_USD`, `AT_DAILY_LOSS_KILL_USD`, `AT_PER_NAME_CAP_PCT`, …).

## Going live (your steps — I can't do these)
1. **Add GitHub Actions secrets** (Settings → Secrets → Actions):
   `RH_USERNAME`, `RH_PASSWORD`, `RH_TOTP_SECRET` (your Robinhood 2FA seed),
   and `ANTHROPIC_API_KEY` (for the gate).
2. **Add a workflow step** after "Generate report":
   ```yaml
   - name: Auto-trade (live)
     env:
       AUTOTRADE_LIVE: '1'
       RH_USERNAME: ${{ secrets.RH_USERNAME }}
       RH_PASSWORD: ${{ secrets.RH_PASSWORD }}
       RH_TOTP_SECRET: ${{ secrets.RH_TOTP_SECRET }}
       ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
     run: |
       pip install -r autotrader/requirements.txt
       python -m autotrader.run --mode ${{ steps.m.outputs.mode }}
   ```
   Leave `AUTOTRADE_LIVE` unset (or `0`) to keep the step in dry-run.
3. **Validate small first.** robin_stocks is an unofficial library — confirm a
   single tiny order behaves before raising the caps. Watch `logs/orders.json` and
   your ntfy alerts.

## Known limitations / TODO
- `robin_stocks` call signatures vary by version — verify `order_sell_stop_loss`,
  `order_buy_fractional_by_price`, and the positions/quote helpers against your
  installed version on the first live run.
- The executor does not yet re-sync `holdings.json` after a live fill (the human
  flow still owns the ledger). Wire that in once live fills are trusted, so the
  exit engine stays accurate.
- No partial-position scaling yet — exits sell the whole position.
