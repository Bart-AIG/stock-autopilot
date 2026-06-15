"""LLM news/thesis veto-gate. Implements HARD RULE 7 for the unattended path.

For each GATEABLE order (buys), ask Claude to check recent news + analyst views
and judge whether the thesis behind the technical signal still holds. The gate can
only VETO — it can never invent a trade the mechanical report didn't surface.

Fail-safe semantics (deliberate):
  - On ANY error/uncertainty for a BUY  -> VETO (don't deploy capital on doubt).
  - SELLS / TRAILS are not gateable (gateable=False) and pass through untouched —
    exits reduce risk and must not be blocked by a flaky model call.

Requires ANTHROPIC_API_KEY. Model + web-search are configurable via env.
"""

from __future__ import annotations

import json
import os

GATE_MODEL = os.environ.get("AT_GATE_MODEL", "claude-opus-4-8")
GATE_ENABLED = os.environ.get("AT_GATE_ENABLED", "1") != "0"

_SYSTEM = (
    "You are a risk gate for an automated swing-trading bot. The bot proposes a BUY "
    "from a purely technical signal (Connors RSI(2) oversold inside an uptrend). Your "
    "job is to veto buys whose fundamental thesis is broken or clearly weakened by "
    "RECENT news, current analyst ratings/price targets, or the macro/sector backdrop "
    "(e.g. a falling-oil tape undercuts an oversold E&P bounce). You CANNOT propose new "
    "trades. Be conservative: when the recent picture is genuinely negative or unclear, "
    "veto. Respond ONLY with JSON: "
    '{"verdict":"intact|weakened|broken","approve":true|false,'
    '"reason":"<=240 chars","sources":["url", ...]}.'
)


def _gate_one(client, order: dict) -> dict:
    sym = order["symbol"]
    prompt = (
        f"Ticker {sym}. Proposed BUY at ~{order.get('entry_ref')} "
        f"(RSI2={order.get('rsi2')}), stop {order.get('stop')}, target {order.get('target')}. "
        "Check the last few days/weeks of news and current analyst targets. Is the thesis "
        "still strong enough to take this oversold-bounce buy? Veto if not."
    )
    msg = client.messages.create(
        model=GATE_MODEL,
        max_tokens=1024,
        system=_SYSTEM,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < 0:
        raise ValueError(f"gate returned no JSON for {sym}: {text[:200]}")
    verdict = json.loads(text[start : end + 1])
    return {
        "approve": bool(verdict.get("approve")),
        "verdict": verdict.get("verdict", "unknown"),
        "reason": verdict.get("reason", ""),
        "sources": verdict.get("sources", []),
    }


def apply_gate(orders: list[dict]) -> list[dict]:
    """Annotate each order with a `gate` result and an `approved` flag.

    Non-gateable orders are auto-approved. Gateable buys get the LLM verdict; any
    failure fails CLOSED (approved=False, vetoed)."""
    if not GATE_ENABLED:
        for o in orders:
            o["approved"] = True
            o["gate"] = {"verdict": "gate-disabled", "reason": "AT_GATE_ENABLED=0"}
        return orders

    client = None
    if any(o.get("gateable") for o in orders):
        try:
            import anthropic  # lazy: only needed when there's a buy to gate
            client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
        except Exception as exc:  # noqa: BLE001 — fail closed below
            client = None
            init_err = str(exc)

    for o in orders:
        if not o.get("gateable"):
            o["approved"] = True
            o["gate"] = {"verdict": "n/a", "reason": "not gateable (exit/trail)"}
            continue
        if client is None:
            o["approved"] = False
            o["gate"] = {"verdict": "error", "reason": f"gate unavailable: {init_err}"}
            continue
        try:
            res = _gate_one(client, o)
            o["approved"] = res["approve"]
            o["gate"] = res
        except Exception as exc:  # noqa: BLE001 — fail closed
            o["approved"] = False
            o["gate"] = {"verdict": "error", "reason": f"gate failed: {exc}"[:240]}

    return orders
