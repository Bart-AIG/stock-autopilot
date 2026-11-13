#!/usr/bin/env python3
"""
capital.py: sleeve money and the real-money drawdown check. Pure functions, no network.

Authority: Ryan, REAL live turn 2026-11-13, answering the audit of the same day:
"lets fix finding 4. 5.". Spec and the rebuilt history: docs/sleeve-money.md.

WHAT WAS WRONG
  Finding 5  Sleeve targets were sized on total account value, which includes Ryan's own
             option positions. The sleeves cannot spend that money, so the targets added
             up to more than the cash that existed, and the sleeves ran off their tested mix.
  Finding 4  The drawdown rule measured total value with Ryan's option losses and his
             deposits added back ($4,172 on 2026-11-13, against about $1,800 of real
             sleeve money), so the -25% halt could not fire until about half of the real
             sleeve money was gone.

DEFINITIONS
  user value    market value of every position Ryan placed himself (placed_agent "user")
  sleeve money  total_value - user value: cash plus the positions the agent holds
  base          95% of sleeve money (the 5% operational reserve is 5% of sleeve money)
  deployable    unleveraged_buying_power - reserve, never below 0
  sleeve P/L    realized P/L of every stock position closed in the account (the broker's
                all-time equity figure; Ryan's own positions are options, so none of it is
                his) plus the unrealized P/L of the agent's open positions. Only CHANGES in
                this number are used, so the starting level does not matter.
  index         the sleeves' unit value, 1.0 at the 2026-09-30 close. At each reading:
                    index *= 1 + (sleeve P/L now - sleeve P/L at the last reading)
                                 / sleeve money at the last reading
                Deposits, withdrawals and Ryan's own trades change sleeve money but not
                sleeve P/L, so they never move the index.
  drawdown      index / its high-water mark - 1.
                At -20% notify Ryan once. At -25% notify him and place no new sleeve buys
                until a live Ryan turn lifts the halt. Sells always run.

A READING MUST COME BEFORE THE RUN'S ORDERS. A position is carried by the money that existed
when it was bought, so each run takes its reading after the broker reconcile and before it
places anything.

USAGE
  python3 capital.py money --tv 2493.54 --user-value 684.00 --ubp 1729.87
  python3 capital.py drawdown --tv 2493.54 --user-value 684.00 --unrealized -3.26 \
          --realized 32.64 --now 2026-11-13T21:20Z [--write]
      --realized   the broker's all-time equity realized P/L (get_realized_pnl, span "all",
                   asset_classes ["equity"], field total_returns). Read it fresh for every
                   reading: when a position is sold its P/L moves from unrealized to
                   realized, and a stale figure would show a gain or loss that never happened.
      --unrealized sum over the agent's open positions of quantity x (price - average cost)
      --write      store the new state in holdings.json (_SLEEVE_PROCESS.drawdown_real)
      Prints status, action, the index, the drawdown, the sleeves' return today, month to
      date and since 2026-09-30, and the dollars of further loss that would reach each line.
  python3 capital.py lift --by "<Ryan's words>" --now ISO [--write]
      Interactive sessions with a live Ryan turn only (HARD RULE 9). Clears the halt and
      moves the high-water mark to the current index, so the -20% / -25% lines start fresh.
  python3 capital.py rebase --tv .. --user-value .. --unrealized .. --realized .. --now ISO \
          --by "<who checked, and why>" [--write]
      Interactive sessions only. Clears a "suspect" state after the inputs were checked by
      hand: today's numbers become the starting point and the index does not move.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "holdings.json"
STATE_KEY = ("_SLEEVE_PROCESS", "drawdown_real")

RESERVE_FRAC = 0.05          # operational reserve, as a share of sleeve money
DD_NOTIFY = -0.20            # notify Ryan once
DD_HALT = -0.25              # beyond the tested -23%: no new sleeve buys until a live Ryan turn
DD_REARM = -0.15             # a sent notice re-arms once the drawdown is back above this
MAX_STEP = 0.20              # one reading cannot move the index by more than this: see update()
MIN_MONEY = 1.0              # below this the sleeves held nothing, so a P/L change has no base


# ------------------------------------------------------------------ sleeve money (finding 5)

def sleeve_money(total_value: float, user_value: float) -> float:
    """Money the sleeves actually hold: the account minus Ryan's own positions."""
    for name, v in (("total_value", total_value), ("user_value", user_value)):
        if v is None or isinstance(v, bool) or not math.isfinite(float(v)):
            raise ValueError(f"{name} must be a number, got {v!r}")
    total_value, user_value = float(total_value), float(user_value)
    if total_value < 0 or user_value < 0:
        raise ValueError("total_value and user_value cannot be negative")
    if user_value > total_value + 0.01:
        raise ValueError(f"user_value {user_value} is above total_value {total_value}: check the inputs")
    return max(0.0, total_value - user_value)


def money(total_value: float, user_value: float, ubp: float | None = None) -> dict:
    """The four numbers every sleeve formula starts from."""
    m = sleeve_money(total_value, user_value)
    out = {
        "total_value": round(float(total_value), 2),
        "user_value": round(float(user_value), 2),
        "sleeve_money": round(m, 2),
        "base": round((1 - RESERVE_FRAC) * m, 2),
        "reserve": round(RESERVE_FRAC * m, 2),
    }
    if ubp is not None:
        out["unleveraged_buying_power"] = round(float(ubp), 2)
        out["deployable"] = round(max(0.0, float(ubp) - RESERVE_FRAC * m), 2)
    return out


# ------------------------------------------------------------------ drawdown (finding 4)

def new_state(index: float = 1.0, hwm_index: float | None = None, hwm_utc: str | None = None) -> dict:
    return {"index": float(index), "hwm_index": float(hwm_index if hwm_index is not None else index),
            "hwm_utc": hwm_utc, "drawdown_pct": 0.0, "status": "ok", "notice_utc": None,
            "halt": None, "suspect": None, "last": None, "marks": None, "lifts": []}


def et_date(now: str) -> str:
    """The US trading date (ET) of an ISO UTC timestamp such as 2026-11-13T19:31Z."""
    t = datetime.fromisoformat(now.strip().replace("Z", "+00:00"))
    if t.tzinfo is None:
        t = t.replace(tzinfo=timezone.utc)
    return t.astimezone(ZoneInfo("America/New_York")).date().isoformat()


def update(state: dict, *, total_value: float, user_value: float, unrealized: float,
           realized: float, now: str) -> tuple[dict, dict]:
    """One reading. Returns (new_state, result). `state` is not modified.

    result["status"]  ok / notify / halt / suspect
    result["action"]  none / notify (send the -20% notice now) / halt_notify (halt starts now:
                      notify, no new sleeve buys) / halted (already halted: no new buys, no
                      new notice) / suspect (the reading was NOT applied: no new sleeve buys
                      this run, tell Ryan the numbers once) / suspect_repeat (still not
                      applied: no new sleeve buys, no new notice)
    """
    st = json.loads(json.dumps(state))          # deep copy
    for k, v in new_state().items():
        st.setdefault(k, v)
    m_now = sleeve_money(total_value, user_value)
    last = st.get("last")
    for name, v in (("realized", realized), ("unrealized", unrealized)):
        if v is None or isinstance(v, bool) or not math.isfinite(float(v)):
            raise ValueError(f"{name} must be a number, got {v!r}")
    pnl = float(realized) + float(unrealized)
    notes: list[str] = []
    step = 0.0
    if last:
        m_last = float(last["sleeve_money"])
        d_pnl = pnl - float(last["sleeve_pnl"])
        if m_last >= MIN_MONEY:
            step = d_pnl / m_last
        elif abs(d_pnl) > 0.005:
            notes.append(f"sleeve money at the last reading was ${m_last:.2f}, so the P/L change of "
                         f"${d_pnl:.2f} has no base and was not applied")
        if abs(step) > MAX_STEP:
            # A fully funded book cannot lose or gain 20% between two readings. This is a
            # wrong input, or a deposit and a trade landing between the same two readings.
            # The index, the high-water mark and the last reading stay as they were, so the
            # next reading is taken from the same point. Only the marker below is stored.
            keep = json.loads(json.dumps(state))
            sus = dict(keep.get("suspect") or {"since_utc": now, "count": 0})
            sus.update({"count": int(sus["count"]) + 1, "last_utc": now, "step_pct": round(100 * step, 1),
                        "pnl_change": round(d_pnl, 2), "sleeve_money_last": round(m_last, 2)})
            keep["suspect"] = sus
            first = sus["count"] == 1
            res = _result(st, "suspect", "suspect" if first else "suspect_repeat", notes + [
                f"one reading would move the index {step:+.1%} (P/L change ${d_pnl:+.2f} on "
                f"${m_last:.2f} of sleeve money). Not applied. Check --realized, --unrealized "
                "and that the reading came before this run's orders. Place no new sleeve buys "
                "this run." + (" Tell Ryan the numbers (once)." if first else " Ryan was already told.")
                + " An interactive session clears it with `capital.py rebase`."])
            return keep, res
    day = et_date(now)
    marks = st.get("marks") or {}
    if marks.get("day") != day:                 # first reading of a trading day
        marks["day"], marks["day_start_index"] = day, float(st["index"])
    if marks.get("month") != day[:7]:           # first reading of a month
        marks["month"], marks["month_start_index"] = day[:7], float(st["index"])
    st["marks"] = marks
    st["suspect"] = None                        # a normal reading clears the marker
    before = float(st["index"])
    st["index"] = before * (1 + step)
    # A new high must hold for two readings in a row, so one bad input cannot ratchet the
    # high-water mark (a false high would overstate every later drawdown).
    confirmed = min(before, st["index"])
    if confirmed > float(st["hwm_index"]) + 1e-12:
        st["hwm_index"], st["hwm_utc"] = confirmed, now
    dd = st["index"] / float(st["hwm_index"]) - 1
    st["drawdown_pct"] = round(100 * dd, 2)
    st["last"] = {"utc": now, "sleeve_pnl": round(pnl, 2), "realized": round(float(realized), 2),
                  "unrealized": round(float(unrealized), 2), "sleeve_money": round(m_now, 2),
                  "total_value": round(float(total_value), 2), "user_value": round(float(user_value), 2)}

    halt = st.get("halt")
    if halt and halt.get("status") == "ACTIVE":
        status, action = "halt", "halted"                       # sticky until a live Ryan turn
    elif dd <= DD_HALT:
        st["halt"] = {"status": "ACTIVE", "set_utc": now, "index": round(st["index"], 6),
                      "drawdown_pct": st["drawdown_pct"]}
        st["notice_utc"] = st.get("notice_utc") or now
        status, action = "halt", "halt_notify"
    elif dd <= DD_NOTIFY:
        status = "notify"
        action = "none" if st.get("notice_utc") else "notify"
        st["notice_utc"] = st.get("notice_utc") or now
    else:
        status, action = "ok", "none"
        if st.get("notice_utc") and dd > DD_REARM:
            st["notice_utc"] = None                             # recovered: the notice re-arms
    st["status"] = status
    return st, _result(st, status, action, notes)


def _pct(idx: float, ref) -> float | None:
    return round(100 * (idx / float(ref) - 1), 2) if ref else None


def _result(st: dict, status: str, action: str, notes: list[str]) -> dict:
    idx, hwm = float(st["index"]), float(st["hwm_index"])
    m = float((st.get("last") or {}).get("sleeve_money") or 0.0)
    dd = idx / hwm - 1
    out = {
        "status": status, "action": action,
        "index": round(idx, 6), "hwm_index": round(hwm, 6), "hwm_utc": st.get("hwm_utc"),
        "drawdown_pct": round(100 * dd, 2),
        "since_start_pct": round(100 * (idx - 1), 2),
        "today_pct": _pct(idx, (st.get("marks") or {}).get("day_start_index")),
        "month_to_date_pct": _pct(idx, (st.get("marks") or {}).get("month_start_index")),
        "notify_at_index": round(hwm * (1 + DD_NOTIFY), 6),
        "halt_at_index": round(hwm * (1 + DD_HALT), 6),
        # what a further loss would have to be, at today's sleeve money, to reach each line
        "usd_to_notify": round(max(0.0, m * (1 - hwm * (1 + DD_NOTIFY) / idx)), 2) if idx > 0 else None,
        "usd_to_halt": round(max(0.0, m * (1 - hwm * (1 + DD_HALT) / idx)), 2) if idx > 0 else None,
        "new_sleeve_buys_allowed": status not in ("halt", "suspect"),
        "notes": notes,
    }
    return out


def lift(state: dict, *, now: str, by: str) -> dict:
    """Lift the halt on a live Ryan turn: the high-water mark moves to the current index."""
    if not by or not by.strip():
        raise ValueError("--by must quote the live Ryan turn that lifts the halt")
    st = json.loads(json.dumps(state))
    st.setdefault("lifts", []).append({
        "utc": now, "by": by.strip(), "index": round(float(st["index"]), 6),
        "old_hwm_index": round(float(st["hwm_index"]), 6), "drawdown_pct_at_lift": st.get("drawdown_pct"),
        "halt_was": st.get("halt")})
    st["hwm_index"], st["hwm_utc"] = float(st["index"]), now
    st["halt"], st["notice_utc"], st["status"], st["drawdown_pct"] = None, None, "ok", 0.0
    return st


def rebase(state: dict, *, total_value: float, user_value: float, unrealized: float,
           realized: float, now: str, by: str) -> dict:
    """Accept today's numbers as the new starting point WITHOUT moving the index. For an
    interactive session clearing a `suspect` state after checking the inputs by hand."""
    if not by or not by.strip():
        raise ValueError("--by must say who checked the numbers and why")
    st = json.loads(json.dumps(state))
    st["last"] = {"utc": now, "sleeve_pnl": round(float(realized) + float(unrealized), 2),
                  "realized": round(float(realized), 2), "unrealized": round(float(unrealized), 2),
                  "sleeve_money": round(sleeve_money(total_value, user_value), 2),
                  "total_value": round(float(total_value), 2), "user_value": round(float(user_value), 2)}
    st["suspect"] = None
    st.setdefault("rebases", []).append({"utc": now, "by": by.strip(),
                                         "note": "starting point moved; the index did not change"})
    return st


# ------------------------------------------------------------------ ledger I/O

def read_state(path: Path = LEDGER) -> dict:
    h = json.loads(Path(path).read_text())
    node = h
    for k in STATE_KEY:
        node = (node or {}).get(k)
    if node is None:
        raise SystemExit(f"{'.'.join(STATE_KEY)} is missing from {path}")
    return node


def write_state(st: dict, path: Path = LEDGER) -> None:
    """Store the state. The ledger is indent=2 with default ensure_ascii; if a plain reload and
    dump would not reproduce the file byte for byte, refuse, so a formatting diff never lands."""
    p = Path(path)
    text = p.read_text()
    h = json.loads(text)
    if json.dumps(h, indent=2) + ("\n" if text.endswith("\n") else "") != text:
        raise SystemExit("holdings.json does not round-trip at indent=2: not writing. "
                         "Apply the printed state by hand, matching the file's own format.")
    h[STATE_KEY[0]][STATE_KEY[1]] = st
    p.write_text(json.dumps(h, indent=2) + ("\n" if text.endswith("\n") else ""))


# ------------------------------------------------------------------ CLI

def _arg(argv: list[str], name: str, cast=float, default=None):
    if name not in argv:
        return default
    return cast(argv[argv.index(name) + 1])


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = argv[0]
    path = Path(_arg(argv, "--ledger", str, str(LEDGER)))
    if cmd == "money":
        print(json.dumps(money(_arg(argv, "--tv"), _arg(argv, "--user-value"), _arg(argv, "--ubp")), indent=1))
        return 0
    if cmd == "drawdown":
        missing = [a for a in ("--tv", "--user-value", "--unrealized", "--realized", "--now") if a not in argv]
        if missing:
            print(f"missing {', '.join(missing)}; see --help")
            return 2
        st = read_state(path)
        new, res = update(st, total_value=_arg(argv, "--tv"), user_value=_arg(argv, "--user-value"),
                          unrealized=_arg(argv, "--unrealized"), realized=_arg(argv, "--realized"),
                          now=_arg(argv, "--now", str))
        res["sleeve_money"] = (new.get("last") or {}).get("sleeve_money")
        if "--write" in argv:
            write_state(new, path)              # on "suspect" only the marker changes
            res["written"] = True
        print(json.dumps(res, indent=1))
        return 0
    if cmd == "rebase":
        st = rebase(read_state(path), total_value=_arg(argv, "--tv"), user_value=_arg(argv, "--user-value"),
                    unrealized=_arg(argv, "--unrealized"), realized=_arg(argv, "--realized"),
                    now=_arg(argv, "--now", str), by=_arg(argv, "--by", str))
        if "--write" in argv:
            write_state(st, path)
        print(json.dumps({"index": st["index"], "hwm_index": st["hwm_index"], "last": st["last"]}, indent=1))
        return 0
    if cmd == "lift":
        st = lift(read_state(path), now=_arg(argv, "--now", str), by=_arg(argv, "--by", str))
        if "--write" in argv:
            write_state(st, path)
        print(json.dumps({k: st[k] for k in ("index", "hwm_index", "hwm_utc", "status", "halt")}, indent=1))
        return 0
    print(f"unknown command {cmd!r}; see --help")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
