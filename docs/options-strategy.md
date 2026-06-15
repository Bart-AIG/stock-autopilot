# Options sleeve — technical + thesis-gated directional longs

Status: **design landed; ready once we trade it.** The Agentic account now has options
enabled (Level 2). This sleeve uses **only data we already have for free** — the
Robinhood broker MCP for live chains/greeks/IV — and is **separate** from the equity
swing/momentum book with its own caps.

It keeps our existing technical edge and expresses the view with a single, defined-risk
long option. (An order-flow confirmation layer — e.g. Unusual Whales — is an OPTIONAL
future upgrade, deliberately left out to avoid a paid feed; see "Optional upgrade".)

## Why long single-leg only
The Agentic account is a **cash** account and the broker tools place **single-leg**
options only (no spreads). So the playable Level-2 structure is long calls/puts, where
the loss is capped at the premium paid — the right risk shape for experimenting.

## Data source (free, already connected)
The Robinhood broker MCP provides everything needed to find, price, and risk-check a
contract:
- `get_option_chains` / `get_option_instruments` — expirations, strikes, calls/puts.
- `get_option_quotes` — live bid/ask, **greeks (delta), and implied volatility**.
No FMP or paid options feed required (FMP has no options data).

## Signal stack — ALL must agree
1. **Our technical signal** (from `report.py`): bullish = momentum top-decile & price
   > 200-day MA, or a clean RSI(2) oversold-in-uptrend setup → **call**. Bearish =
   momentum breakdown / below 200-day MA with a failed bounce → **put**.
2. **News/thesis gate (HARD RULE 7):** this carries extra weight here — it is the
   primary confirmation that the move is real (it's standing in for the order-flow
   check we chose not to pay for). Recent news + analyst posture must support the
   direction; a broken/weakened thesis vetoes the trade.
3. **IV sanity (from the chain):** check implied vol / rough IV rank — don't buy premium
   when vol is extreme. Avoid an imminent earnings date unless the event IS the thesis.
4. **Liquidity:** tight bid/ask and real open interest only.

## Direction
**Both directions** — long calls on bullish confluence, long puts on bearish confluence.

## Contract selection (default profile)
- **~30–45 DTE** (limit theta), **~0.35 delta**, **liquid**. Pull the chain via
  `get_option_chains` → filter expiration/strike/type → price + greeks via
  `get_option_quotes`.

## Risk & sizing (its own sleeve)
- **≤ ~$150 premium per trade** — max loss = premium paid (defined).
- **Total options premium-at-risk ≤ ~15% of account value** at any time; only a few
  concurrent. Separate from the equity per-name/spec caps.
- Cash account: premium paid from settled cash; respect buying power + the buffer.

## Exits
- **Take profit** ~+50–100% of premium.
- **Cut** ~−50% of premium.
- **Close on a broken/weakened thesis.**
- **Time/event:** close when **DTE < ~14** (theta) or **before earnings** — no naked
  long gamma into a binary unless that was the explicit thesis.

## Execution & bookkeeping
- Review with `review_option_order` (show quote, greeks, fees, and **max loss**), then
  use the **one-tap batch approval** flow (same as equities).
- Record fills in `holdings.json` under a new sleeve, e.g.:
  ```json
  {"symbol": "NVDA", "sleeve": "options", "type": "call",
   "option_id": "<uuid>", "expiry": "2026-07-17", "strike": 180,
   "contracts": 1, "entry_premium": 1.45, "entry_date": "2026-06-15",
   "thesis": "momentum >200MA + intact thesis", "tp": 2.9, "sl": 0.72}
  ```
  Removed on close (or reduced on a partial).

## Honest tradeoff
Without an order-flow/dark-pool feed we are NOT confirming that institutions are
positioning the same way before paying for premium — so there's less edge than a
flow-confirmed version. The news/thesis gate must carry that weight. Size small and
treat early trades as calibration.

## Build TODO (now unblocked)
- Extend the report (or a new `options_scan`) to surface candidates: take our technical
  names → pull the Robinhood chain → filter by IV/liquidity/delta/DTE → propose a
  specific contract → feed it into the alert + one-tap batch.
- Add the options leg to the alert/approval flow.

## Optional upgrade (later, if you ever want the edge back)
Re-introduce an order-flow confirmation layer (Unusual Whales or similar). The signal
stack already has a slot for it (between steps 1 and 2). That's a paid feed, so it's
intentionally deferred.
