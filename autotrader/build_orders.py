"""Turn the report's mechanical signals + the holdings ledger into proposed orders.

Input  : the report JSON (logs/report_*_<mode>.json) written by report.py, plus
         holdings.json and a live account snapshot (value / buying power / positions).
Output : a list of proposed orders (sells, trail-stop replacements, buys) already
         passed through the sizing guardrails. The LLM veto-gate (thesis_gate.py)
         runs AFTER this, and the executor runs last.

The order of operations matches the human playbook: SELLS first (reduce risk),
then TRAIL-STOP moves, then BUYS (only names in today's report, sized down).
"""

from __future__ import annotations

import glob
import json
import os
from pathlib import Path

from .guardrails import GUARDRAILS, Guardrails, report_is_fresh, size_buy_usd

REPO = Path(__file__).resolve().parent.parent


def latest_report_json(mode: str) -> Path | None:
    """Newest report JSON for this mode. Lives in logs/ (gitignored) — so this is
    meant to run in the SAME workflow job that produced it."""
    matches = sorted(glob.glob(str(REPO / "logs" / f"report_*_{mode}.json")))
    return Path(matches[-1]) if matches else None


def load_report(mode: str) -> dict:
    jf = latest_report_json(mode)
    if not jf:
        raise FileNotFoundError(f"no logs/report_*_{mode}.json — run report.py first")
    return json.loads(jf.read_text(encoding="utf-8")), jf.name


def build_proposals(
    report: dict,
    *,
    account_value: float,
    buying_power: float,
    positions: dict[str, dict],
    quotes: dict[str, float],
    g: Guardrails = GUARDRAILS,
) -> dict:
    """Build the proposed order set from a report dict + a live account snapshot.

    positions: {symbol: {"shares": float, "available": float}} from the broker.
    quotes:    {symbol: last_price} for sizing buys / valuing existing names.
    Returns {"orders": [...], "skipped": [...], "halt": str|None}.
    """
    orders: list[dict] = []
    skipped: list[dict] = []

    action = report.get("action", "")
    if action == "DATA ERROR":
        return {"orders": [], "skipped": [], "halt": "report action == DATA ERROR"}

    fresh, why = report_is_fresh(report.get("generated_utc", ""), g)
    if not fresh:
        return {"orders": [], "skipped": [], "halt": f"stale report: {why}"}

    # Allowlist: only symbols the report surfaced today may be traded at all.
    allow = {e["symbol"] for e in report.get("exit_signals", [])}
    allow |= {t["symbol"] for t in report.get("trail_suggestions", [])}
    allow |= {s["symbol"] for s in report.get("swing_setups", [])}

    # 1) SELLS — every exit signal on a name we actually hold. Exits reduce risk,
    #    so they are NOT sized and (by default) NOT vetoable.
    for e in report.get("exit_signals", []):
        sym = e["symbol"]
        pos = positions.get(sym)
        if not pos or pos.get("available", 0) <= 0:
            skipped.append({"symbol": sym, "kind": "sell", "why": "not held / nothing sellable"})
            continue
        orders.append({
            "kind": "sell", "symbol": sym, "qty": "all",
            "available": pos["available"], "sleeve": e.get("sleeve"),
            "reason": "; ".join(e.get("reasons", [])), "gateable": False,
        })

    # 2) TRAIL STOPS — replace the resting GTC stop with the report's higher one.
    for t in report.get("trail_suggestions", []):
        sym = t["symbol"]
        if sym not in positions:
            skipped.append({"symbol": sym, "kind": "trail", "why": "not held"})
            continue
        orders.append({
            "kind": "trail", "symbol": sym,
            "old_stop": t["old_stop"], "new_stop": t["new_stop"],
            "reason": f"up {t.get('r')}R — trail to lock gains", "gateable": False,
        })

    # 3) BUYS — swing setups, sized down, allowlisted, gated by the LLM later.
    exiting = {o["symbol"] for o in orders if o["kind"] == "sell"}
    spent_today = 0.0
    for s in report.get("swing_setups", []):
        sym = s["symbol"]
        if sym in exiting:
            skipped.append({"symbol": sym, "kind": "buy", "why": "also an exit today"})
            continue
        if s.get("held") and g.skip_held_buys:
            skipped.append({"symbol": sym, "kind": "buy", "why": "[HELD] — skip adding"})
            continue
        if s.get("speculative") and not g.allow_speculative:
            skipped.append({"symbol": sym, "kind": "buy", "why": "[SPEC] disabled"})
            continue

        existing_usd = 0.0
        if sym in positions and sym in quotes:
            existing_usd = positions[sym].get("shares", 0) * quotes[sym]

        size, note = size_buy_usd(
            account_value=account_value, buying_power=buying_power,
            spent_today=spent_today, existing_position_usd=existing_usd, g=g,
        )
        if size <= 0:
            skipped.append({"symbol": sym, "kind": "buy", "why": note})
            continue

        orders.append({
            "kind": "buy", "symbol": sym, "dollar_amount": size,
            "stop": s.get("stop"), "target": s.get("target"),
            "sleeve": "swing", "speculative": bool(s.get("speculative")),
            "entry_ref": s.get("price"), "rsi2": s.get("rsi2"),
            "sizing": note, "gateable": True,  # buys get the news/thesis veto
        })
        spent_today += size

    return {"orders": orders, "skipped": skipped, "halt": None}
