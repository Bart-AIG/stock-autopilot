"""Agent-managed Robinhood watchlists (set 2026-10-13, Ryan's live turn).

Ryan asked to replace his hand-kept Robinhood watchlists with lists the agent keeps.
The old general lists were archived to watchlist_archive.json and emptied; his theme
lists (Drones, Raw materials, Growth opportunities, Cryptos to Watch) stay his.

Five lists are agent-managed, each mirroring a file the system already keeps, so a
list is never a second source of truth:

    joint_holdings  <- live joint positions (get_equity_positions on the joint account)
    buy_zone        <- quality_watch_state.json managed_alerts (the 15 alert slots)
    rebuy           <- rebuy_watch.json names still being watched
    sleeves         <- sleeves_state.json: QQQ + its vehicle (QLD) + this month's SWING_M picks
    macro           <- fixed benchmarks the Joint risk watch grades

A watchlist does not notify anyone; the routines' Robinhood alerts do. The lists are
visibility only. Pure functions, no network: the Quality @ 200-day routine (step 4d of
docs/quality-watch-prompt.md) fetches and writes with the Robinhood connector.

Write scope: a run may add/remove symbols ONLY on lists whose id is in
watchlists.json["managed"]. Ryan's own lists, including the theme lists, are read-only.
"""
from __future__ import annotations

import json
from pathlib import Path

STATE = Path(__file__).resolve().parent / "watchlists.json"

MACRO = ["SPY", "QQQ", "HYG", "KRE", "VIXY", "USO", "IEF", "TIP"]

# The connector's symbol lookup intermittently fails a whole batch on one valid ticker
# (2026-10-13: QQQI then RLI, both fine on retry). Small batches bound the blast radius.
BATCH = 40


def load_state(path: Path = STATE) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _read(name: str) -> dict:
    try:
        return json.loads((STATE.parent / name).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def joint_holdings(positions: list[dict]) -> list[str]:
    """Live joint positions. Skips stubs like 'EPIX^' (delisted, no instrument)."""
    out = []
    for p in positions:
        s = (p.get("symbol") or "").strip()
        q = float(p.get("quantity") or 0)
        if s and q > 0 and s.isalnum() and s not in out:
            out.append(s)
    return sorted(out)


def buy_zone(qstate: dict) -> list[str]:
    """The names holding a Quality @ 200-day alert slot, best rank first."""
    managed = list((qstate.get("managed_alerts") or {}).keys())
    order = {s: i for i, s in enumerate(qstate.get("candidates") or [])}
    return sorted(managed, key=lambda s: order.get(s, len(order)))


def rebuy(rstate: dict) -> list[str]:
    """Re-buy names still being watched (a CLOSED stage means bought back or dropped)."""
    return [s for s, v in (rstate.get("names") or {}).items()
            if "CLOSED" not in str((v or {}).get("stage", "")).upper()]


def sleeves(sstate: dict) -> list[str]:
    """SWING_Q's signal symbol and its traded vehicle, then the SWING_M picks."""
    out = []
    for sig, vehicle in (sstate.get("vehicle") or {}).items():
        out += [sig, vehicle]
    out += [p["symbol"] for p in sstate.get("picks") or [] if p.get("symbol")]
    seen: list[str] = []
    for s in out:
        if s not in seen:
            seen.append(s)
    return seen


def desired_all(joint_positions: list[dict]) -> dict[str, list[str]]:
    """Target contents for every managed list, from the repo state on disk."""
    return {
        "joint_holdings": joint_holdings(joint_positions),
        "buy_zone": buy_zone(_read("quality_watch_state.json")),
        "rebuy": rebuy(_read("rebuy_watch.json")),
        "sleeves": sleeves(_read("sleeves_state.json")),
        "macro": list(MACRO),
    }


def diff(current: list[str], desired: list[str]) -> tuple[list[str], list[str]]:
    """(to_add, to_remove), each in a stable order."""
    cur, want = set(current), set(desired)
    return [s for s in desired if s not in cur], sorted(cur - want)


def batches(symbols: list[str], size: int = BATCH) -> list[list[str]]:
    return [symbols[i:i + size] for i in range(0, len(symbols), size)]


def theme_symbols(state: dict | None = None) -> list[str]:
    """Stock symbols on Ryan's theme lists (cached in watchlists.json by the routine),
    so report.py scans and values them. Crypto pairs are skipped."""
    st = state if state is not None else load_state()
    out: list[str] = []
    for t in (st.get("themes") or {}).values():
        for s in t.get("symbols") or []:
            if s not in out:
                out.append(s)
    return out
