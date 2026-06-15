# Options sleeve — flow-confirmed directional longs

Status: **design landed; not yet live.** Two gates remain (see bottom): enable
options on the Agentic account, and connect the Unusual Whales (UW) MCP. Until both
are done, options orders are rejected and UW data is unavailable.

This sleeve is **separate** from the equity swing/momentum book and has its own caps.
It keeps our existing technical edge and uses UW as the *confirmation* that smart money
agrees — then expresses the view with a single, defined-risk long option.

## Why long single-leg only
The Agentic account is a **cash** account and the broker tools place **single-leg**
options only (no spreads). So the playable Level-2 structures are long calls/puts
(cash-secured puts tie up cash; covered calls need 100 shares). Long options cap the
loss at the premium paid — the right risk shape for experimenting.

## Signal stack — ALL must agree
1. **Our technical signal** (from `report.py`): bullish = momentum top-decile & price
   > 200-day MA, or a clean RSI(2) oversold-in-uptrend setup → **call**. Bearish =
   momentum breakdown / below 200-day MA with a failed bounce → **put**.
2. **Unusual Whales confirmation** (direction must match):
   - `get_flow_alerts` / options flow: ask-side sweeps, net premium on the side of the
     trade, repeat prints — not one-off lottos.
   - `get_dark_pool_trades`: supportive accumulation/distribution.
   - optional tailwinds: `get_congress_trades`, insider/institutional.
3. **IV sanity:** check IV rank from the chain — don't buy premium when IV rank is
   extreme. Avoid an imminent earnings date unless the event IS the thesis.
4. **News/thesis gate (HARD RULE 7):** the fundamental check still gates everything.

## Direction
**Both directions** — long calls on bullish confluence, long puts on bearish confluence.

## Contract selection (default profile)
- **~30–45 DTE** (limit theta), **~0.35 delta**, on a **liquid** contract (tight
  bid/ask, real open interest). Source via `get_option_chains` → `get_option_instruments`
  filtered by expiration/strike/type; price/greeks via `get_option_quotes`.

## Risk & sizing (its own sleeve)
- **≤ ~$150 premium per trade** — max loss = premium paid (defined).
- **Total options premium-at-risk ≤ ~15% of account value** at any time; only a few
  concurrent positions. This budget is **separate** from the equity per-name/spec caps.
- Cash account: premium is paid from settled cash; respect buying power + the buffer.

## Exits
- **Take profit** at ~+50–100% of premium.
- **Cut** at ~−50% of premium.
- **Close on reversal** of the flow or a broken/weakened thesis.
- **Time/event:** close when **DTE < ~14** (theta bleed) or **before earnings** — no
  naked long gamma held into a binary unless that was the explicit thesis.

## Execution & bookkeeping
- Review with `review_option_order` (show quote, greeks, fees, and **max loss**), then
  use the **one-tap batch approval** flow (same as equities).
- Record fills in `holdings.json` under a new sleeve, e.g.:
  ```json
  {"symbol": "NVDA", "sleeve": "options", "type": "call",
   "option_id": "<uuid>", "expiry": "2026-07-17", "strike": 180,
   "contracts": 1, "entry_premium": 1.45, "entry_date": "2026-06-15",
   "thesis": "momentum + bullish UW sweeps", "tp": 2.9, "sl": 0.72}
  ```
  An option position is removed on close (or reduced on a partial).

## Gates before this can run
1. **Enable options on the Agentic account** (Level 2 is enough):
   `https://applink.robinhood.com/upgrade_options?account_number=718757339`
   The account must then show `option_level_2`+ in `get_accounts`.
2. **Connect Unusual Whales MCP** (see `.mcp.json`): set `UW_API_KEY` as an env secret
   and allowlist `api.unusualwhales.com` in the environment. Then the candidate scan
   can pull live flow/dark-pool confirmation.

## Build TODO (once gates clear)
- Extend the report (or a new `options_scan`) to surface candidates: take our technical
  names, query UW for confluence, filter by IV/liquidity, propose a contract.
- Add an options leg to the alert + one-tap batch.
- Extend the parked `autotrader/` executor with `review/place_option_order` if/when an
  unattended broker path exists (not Robinhood).
