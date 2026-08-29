# Options sleeve — technical + thesis-gated directional longs

Status: **live and trading.** The Agentic account is `limited_margin` /
`option_level_3` (since 2026-08-21; the "cash account / Level 2" framing in older
sections of this doc predates the upgrade). This sleeve uses **only data we already
have for free** — the Robinhood broker MCP for live chains/greeks/IV — and is
**separate** from the equity swing/momentum book with its own caps.
**Where this doc and CLAUDE.md HARD RULE 8 disagree, HARD RULE 8 wins** — it
carries the dated amendments; this doc is the strategy rationale.

It keeps our existing technical edge and expresses the view with a single, defined-risk
long option. (An order-flow confirmation layer — e.g. Unusual Whales — is an OPTIONAL
future upgrade, deliberately left out to avoid a paid feed; see "Optional upgrade".)

## Why long single-leg only (updated 2026-08-24 — the reason changed, the rule did not)
The agentic API places **single-leg long options only**. This is no longer a
level-2 limitation (the account is level 3): it is the **order endpoint itself** —
`place_option_order` rejects any multi-leg order with a 400 ("Multi-leg options
orders aren't supported in Robinhood agentic accounts yet"), measured 2026-08-24
by actually sending a reviewed vertical. Two traps discovered the same day:
- **`review_option_order` false-greens multi-leg** — it accepts a spread payload
  and returns a complete, healthy preview. A clean review proves nothing; only a
  fill does.
- **Legging a spread as two orders is arithmetically impossible here.** A short
  leg sent alone is margined standalone — full cash-secured collateral on a put
  (the entire strike value), or a banned naked call. Leg two always fails, and
  leg one is left as an orphaned full-premium single leg at 4–9× the vertical's
  theta. Never leg.

**Spreads remain in the playbook as a DELIVERABLE:** when a thesis genuinely wants
a vertical, the desk specs it completely (both legs quoted live, net debit, max
profit, breakevens, invalidation, hold period) and **Ryan places it in the app**,
where multi-leg works normally. Any name may be surveyed for a spread spec
(Ryan, 2026-08-24); the ≤10%-of-mid / real-OI gate on both legs is unchanged.
Full detail: CLAUDE.md HARD RULE 8.

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

## Risk & sizing (its own sleeve) — corrected 2026-08-24 to the readings that actually govern
- **$1,500 is a PER-TRADE maximum, NOT a total-sleeve budget** (2026-08-14 sizing
  amendment, Ryan live turn — supersedes the 2026-08-05 "total ≤ $1,500" reading an
  earlier version of this bullet carried). $1,500 is reserved for A++ CORE setups;
  TACTICAL scalps are sized $300–1,000 (Ryan widened the band from $300–600 on
  2026-08-24). Premium scales with conviction — full pre-trade checklist every
  time. Max loss = premium paid (defined).
- **Total deployment is bounded by `unleveraged_buying_power`** from
  `get_portfolio`, never `buying_power` — **NO MARGIN BORROWING, EVER** (Ryan,
  2026-08-21). ~~keep ≥$250 unencumbered~~ — **the flat $250 reserve is RETIRED
  as of 2026-08-28T20:42:36Z** (master commit `1322da9`, capital-policy repeal).
  It is replaced by an **OPERATIONAL RESERVE of 5% of total account value**,
  which **SCALES** — recompute it from `get_portfolio.total_value` every run and
  never hard-code a dollar figure. **Deployable = `unleveraged_buying_power −
  0.05 × total_value`.** (At the 2026-08-29 account size of $3,960.58 that is
  $198.03, i.e. *looser* than the old $250 — do not treat the retired number as a
  stricter floor to fall back on. **Known conflict, stated rather than resolved
  silently:** routine prompt v8's FOUR LAWS #4 still reads "leave ≥$250
  unencumbered"; per the CLAUDE.md capital-policy amendment the 5% rule governs
  until Ryan pastes v9, and a run finding the conflict must apply the 5% rule and
  report the prompt as stale — see `holdings.json._PROMPT_V9_PASTE_REQUIRED`.)
  The old "settled cash / T+1 /
  good-faith violation" mechanics are obsolete on the `limited_margin` account
  (settlement is instant); the intent — never deploy money that does not exist —
  is unchanged.
- Ryan's manually-placed options (`placed_agent: "user"`) do NOT count against
  agentic premium accounting (2026-08-03 agentic sub-sleeve amendment). Separate
  from the equity per-name/spec caps.
- **Daily realized-loss cap −$400** (settled by the v4 prompt paste 2026-08-21):
  when hit, no NEW entries until the next trading day; exits still run.
- Structural limits: max 5 open agentic positions (2 tactical / 3 core, hedge
  excluded), max 3 per correlated theme, max 2 entries/run and 8/day, DTE floor 7.

## Exits (2026-08-05 exit-method amendment — replaces the flat −50% cut / fixed +50–100% TP)
Modeled on how experienced options traders manage long premium: stops on the
UNDERLYING's chart (not the option's leveraged P&L, which whipsaws on vol), the
~21-DTE management rule (theta and gamma both accelerate in the final 3 weeks),
and time stops (a flat long option is a losing long option).

**Losers — thesis-first, patience scaled to time-to-expiry:**

| Time left | A −50% premium print means | Hard backstop |
|---|---|---|
| **>45 DTE** | Alert + thesis re-check only — hold if the setup is intact | **−70%** |
| **21–45 DTE** | Re-check; sell only if ≤−50% holds ≥2 consecutive runs AND the thesis re-check fails | **−65%** |
| **7–21 DTE** | Cut stands, confirmed by one re-check the following run | **−50%** (and flat by DTE 2) |

- **PRIMARY exit at any DTE:** the underlying closes through the trade's
  `setup_invalidation` level (recorded in the ledger at entry) or the HARD RULE 7
  thesis breaks. Premium % is the backstop, not the trigger.
- **Time stop / 21-DTE review (replaces the old DTE<~14 roll-off):** at 21 DTE every
  swing position gets a roll/close decision; flat or losing at 21 DTE = close or
  roll, never hold into the theta/gamma window.
- Backstops are unconditional — only `manual_hold_override` or the hedge-put
  exemption (defensive-posture insurance) suspends them.

**Winners — pop-banking + trailing ratchet, no fixed ceiling:**
- **Pop-bank:** a one-day gain ≥ +80% (or a blow-off spike into overbought) → sell
  into strength and recycle the capital into the next trade.
- **Ratchet:** arms at +50%; track `peak_premium` in `_current_state` each run; exit
  if the gain gives back ~40% of its peak (peak +100% → exit floor ≈ +60%). The
  floor only moves up.
- **Let it ride:** while trend + momentum + thesis all hold, no fixed take-profit —
  the pop rule, the ratchet, and the 21-DTE review are the only winner exits.
- Short-DTE entries keep the quicker +30–50% banking.
- **Before earnings:** still close/roll — no naked long gamma into a binary unless
  that was the explicit thesis.

## Execution & bookkeeping
- Review with `review_option_order` (show quote, greeks, fees, and **max loss**), then
  use the **one-tap batch approval** flow (same as equities).
- **Order pricing on exits — work the spread, don't just cross it (Ryan, 2026-07-21).**
  A sell-to-close should NOT default to a fully marketable price (i.e. essentially
  hitting the bid) — that needlessly gives up the spread on every single exit. Instead:
  pull the live bid/ask (`get_option_quotes`), place the closing `limit` order at or
  near the **midpoint** (or a touch better, toward the ask), and only step the price
  down toward the bid if it isn't filling and the exit is time-sensitive (a mechanical
  −50% stop or a fast-moving name shouldn't be left unfilled for long — some slippage
  from mid is fine to guarantee the fill, but starting at the bid on the first try is
  not). This applies to every mechanical exit (TP, stop, thesis-close, DTE/earnings
  roll-off) — check the realized fill against the quoted mid when logging it so a
  pattern of bad fills can be caught later.
- Record fills in `holdings.json` under a new sleeve, e.g.:
  ```json
  {"symbol": "NVDA", "sleeve": "options", "type": "call",
   "option_id": "<uuid>", "expiry": "2026-07-17", "strike": 180,
   "contracts": 1, "entry_premium": 1.45, "entry_date": "2026-06-15",
   "thesis": "momentum >200MA + intact thesis", "tp": 2.9, "sl": 0.72}
  ```
  Removed on close (or reduced on a partial).

## Known friction: $150 cap vs. ~0.35 delta on higher-priced underlyings (flagged 2026-07-09 — RESOLVED 2026-08-05)
**RESOLVED via option (a) below:** Ryan raised the budget to $1,500 total (see "Risk &
sizing" above), so the ~0.35-delta liquid strike now fits on most candidates — prefer it
over a cheap illiquid strike. Section kept for history:
The default contract profile (~30–45 DTE, ~0.35 delta) and the ≤$150/trade premium cap
are in tension once the underlying isn't cheap. Rule of thumb from live chain checks
this session: a ~0.35-delta, ~45 DTE contract runs roughly 4-8% of the stock price in
premium, so it only clears the $150 cap when the stock trades below roughly $25-35 (all
our filled entries so far — SMR ~$8, F ~$14, TE ~$7.64 — happened to be that cheap by
coincidence, not by rule). On 2026-07-09 the full options-candidate list from the report
(MU ~$1015, LITE ~$755, AAOI ~$121, ACN ~$130, NOW ~$101) all failed: at 0.35 delta every
one of them priced at $200-800+/contract; pulling the strike further OTM to fit the $150
cap drags delta down to ~0.03-0.17, which no longer expresses the thesis with any
conviction. LIN (an RSI2 swing signal, ~$520) hit the identical wall the same day. This
isn't a one-off skip — it's the entry gate silently rejecting most of the candidate list
by construction, so it will keep recurring every run until one of these changes:
- **(a)** raise the premium cap as the account grows (currently sized for a ~$2.7k account);
- **(b)** accept a lower target delta (~0.15-0.20) for underlyings where 0.35 delta don't
  fit the cap, trading conviction for affordability;
- **(c)** have `report.py` pre-filter the options-candidates section to names whose
  chain can actually produce a ~0.35-delta contract under the current cap, so the
  in-session/automated check isn't repeatedly re-deriving "too expensive" on the same
  large-cap momentum names.
Needs Ryan's call — this doc flags it and proposes the options rather than picking one
unilaterally, since it's a sizing-policy question, not a single trade decision.

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
