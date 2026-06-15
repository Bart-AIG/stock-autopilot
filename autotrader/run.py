"""Orchestrator: report JSON -> guardrails -> LLM gate -> execute. Dry-run by default.

Run inside the SAME GitHub Actions job that produced the report (the JSON lives in
logs/, which is gitignored). Usage:

    python -m autotrader.run --mode intraday

Exit is non-zero only on a hard error; a clean "halt" (stale/DATA ERROR/kill-switch)
is reported and exits 0 so the workflow can still publish the report.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from .build_orders import REPO, build_proposals, load_report
from .executor_robinhood import RobinhoodExecutor
from .guardrails import GUARDRAILS
from .thesis_gate import apply_gate

ORDERS_OUT = REPO / "logs" / "orders.json"


def _candidate_symbols(report: dict) -> list[str]:
    syms = {e["symbol"] for e in report.get("exit_signals", [])}
    syms |= {t["symbol"] for t in report.get("trail_suggestions", [])}
    syms |= {s["symbol"] for s in report.get("swing_setups", [])}
    return sorted(syms)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=["morning", "intraday"])
    args = ap.parse_args()

    report, src = load_report(args.mode)
    ex = RobinhoodExecutor()  # dry-run unless AUTOTRADE_LIVE=1 + creds
    ex.login()
    snap = ex.snapshot(_candidate_symbols(report))

    # Daily-loss kill-switch: never OPEN risk on a bad day; exits still allowed.
    halt_buys = snap.day_pnl <= GUARDRAILS.daily_loss_kill_usd
    proposal = build_proposals(
        report, account_value=snap.account_value, buying_power=snap.buying_power,
        positions=snap.positions, quotes=snap.quotes,
    )

    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "mode": args.mode, "source_report": src, "dry_run": ex.dry_run,
        "account_value": snap.account_value, "buying_power": snap.buying_power,
        "day_pnl": snap.day_pnl, "halt": proposal["halt"],
        "kill_switch_tripped": halt_buys, "orders": [], "skipped": proposal["skipped"],
    }

    if proposal["halt"]:
        _write(out)
        print(f"HALT: {proposal['halt']} — nothing executed.")
        return 0

    orders = proposal["orders"]
    if halt_buys:
        for o in orders:
            if o["kind"] == "buy":
                o["approved"] = False
                o["gate"] = {"verdict": "kill-switch", "reason": f"day P&L {snap.day_pnl:.0f} <= {GUARDRAILS.daily_loss_kill_usd:.0f}"}
        orders = [o for o in orders if o["kind"] != "buy" or "gate" in o]

    orders = apply_gate(orders)

    # Execute: sells, then trails, then approved buys (risk down before risk up).
    rank = {"sell": 0, "trail": 1, "buy": 2}
    for o in sorted(orders, key=lambda x: rank.get(x["kind"], 9)):
        if o["kind"] == "buy" and not o.get("approved", False):
            o["result"] = {"ok": False, "skipped": "vetoed/kill-switch"}
        else:
            o["result"] = ex.execute(o)
        out["orders"].append(o)

    out["execution_log"] = ex.log
    _write(out)
    _print_summary(out)
    return 0


def _write(out: dict) -> None:
    ORDERS_OUT.parent.mkdir(exist_ok=True)
    ORDERS_OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")


def _print_summary(out: dict) -> None:
    mode = "DRY-RUN" if out["dry_run"] else "LIVE"
    print(f"[{mode}] {len(out['orders'])} order(s); {len(out['skipped'])} skipped. -> {ORDERS_OUT}")
    for o in out["orders"]:
        g = o.get("gate", {})
        tag = "" if o.get("approved", True) else f" VETO({g.get('verdict')}: {g.get('reason')})"
        print(f"  {o['kind'].upper()} {o['symbol']} {o.get('result', {}).get('action', '')}{tag}")


if __name__ == "__main__":
    raise SystemExit(main())
