"""Hard guardrails for the auto-trader. Conservative defaults; override via env.

Every limit here is a SAFETY ceiling, not a target. The point is that even a
buggy signal or a confused LLM can't do much damage: small per-order size, a
small daily budget, a daily-loss kill-switch, and a ticker allowlist that only
ever contains names the report itself surfaced today.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone


def _envf(name: str, default: float) -> float:
    try:
        return float(os.environ[name])
    except (KeyError, ValueError):
        return default


@dataclass(frozen=True)
class Guardrails:
    # --- sizing ceilings ---
    max_per_order_usd: float = _envf("AT_MAX_PER_ORDER_USD", 300.0)
    max_per_day_usd: float = _envf("AT_MAX_PER_DAY_USD", 600.0)
    per_name_cap_pct: float = _envf("AT_PER_NAME_CAP_PCT", 0.18)   # 18% of account value
    spec_sleeve_cap_pct: float = _envf("AT_SPEC_CAP_PCT", 0.25)    # 25% total speculative
    cash_buffer_usd: float = _envf("AT_CASH_BUFFER_USD", 50.0)
    # --- circuit breakers ---
    daily_loss_kill_usd: float = _envf("AT_DAILY_LOSS_KILL_USD", -150.0)  # halt buys if day P&L <= this
    report_max_age_min: float = _envf("AT_REPORT_MAX_AGE_MIN", 240.0)     # refuse a stale report
    # --- policy ---
    skip_held_buys: bool = os.environ.get("AT_SKIP_HELD_BUYS", "1") != "0"
    allow_speculative: bool = os.environ.get("AT_ALLOW_SPEC", "1") != "0"


GUARDRAILS = Guardrails()


def report_is_fresh(generated_utc: str, g: Guardrails = GUARDRAILS) -> tuple[bool, str]:
    """A report older than report_max_age_min (or with no timestamp) is untradeable."""
    try:
        ts = datetime.fromisoformat(generated_utc)
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return False, f"unparseable generated_utc {generated_utc!r}"
    age_min = (datetime.now(timezone.utc) - ts).total_seconds() / 60.0
    if age_min > g.report_max_age_min:
        return False, f"report is {age_min:.0f} min old (> {g.report_max_age_min:.0f})"
    return True, f"{age_min:.0f} min old"


def per_name_cap_usd(account_value: float, g: Guardrails = GUARDRAILS) -> float:
    """The most we'll hold in ONE name, as a dollar figure."""
    return account_value * g.per_name_cap_pct


def size_buy_usd(
    *,
    account_value: float,
    buying_power: float,
    spent_today: float,
    existing_position_usd: float,
    g: Guardrails = GUARDRAILS,
) -> tuple[float, str]:
    """Return the dollar size for a new buy after every ceiling, and a note.

    Stacks: per-order cap, remaining daily budget, remaining per-name room, and
    settled buying power minus the cash buffer. Returns 0.0 (with the binding
    reason) when there's no room — the caller then skips the name.
    """
    per_order = g.max_per_order_usd
    daily_left = max(0.0, g.max_per_day_usd - spent_today)
    name_room = max(0.0, per_name_cap_usd(account_value, g) - existing_position_usd)
    spendable = max(0.0, buying_power - g.cash_buffer_usd)

    size = min(per_order, daily_left, name_room, spendable)
    if size <= 0:
        binding = min(
            ("per-order", per_order), ("daily-budget", daily_left),
            ("per-name-cap", name_room), ("buying-power", spendable),
            key=lambda kv: kv[1],
        )[0]
        return 0.0, f"no room (binding: {binding})"
    binding = min(
        ("per-order", per_order), ("daily-budget", daily_left),
        ("per-name-cap", name_room), ("buying-power", spendable),
        key=lambda kv: kv[1],
    )[0]
    return round(size, 2), f"sized to ${size:.2f} (binding: {binding})"
