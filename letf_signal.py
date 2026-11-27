"""Joint leveraged-ETF signal: the rule from docs/joint-letf-process.md as pure functions.

  ON   when the index closes more than 2% above its 200-day simple moving average
  OFF  when it closes more than 2% below it; in between, the state does not change
  SIZE while ON, the share of the sleeve in the 3x fund = min(100%, 50% / (3 x 20-day realized vol))

The same arithmetic as letf_joint_backtest.rules() (band) and its "recommended" rule (size);
test_letf_signal.py checks the two agree. No network, no broker, no trading.
Ryan places every joint trade himself.
"""
from __future__ import annotations

import math
import statistics
from datetime import date

BAND = 0.02
SMA_N = 200
VOL_N = 20
VOL_TARGET = 0.50
LEVERAGE = 3
REBALANCE_PTS = 100.0 / 6      # a size change worth trading: 0.5x of exposure on a 3x fund
FUNDS = {"SPY": ("UPRO", "core"), "QQQ": ("TQQQ", "optional, at most half the sleeve"),
         "SOXX": ("SOXL", "satellite, a quarter of the sleeve or less")}


def band_states(closes: list[float], band: float = BAND, n: int = SMA_N) -> list[int]:
    """State after each close (1 = ON, 0 = OFF). It starts OFF and changes only on a close beyond a line."""
    out, cur, run = [], 0, 0.0
    for i, px in enumerate(closes):
        run += px
        if i >= n:
            run -= closes[i - n]
        if i >= n - 1:
            m = run / n
            if px > m * (1 + band):
                cur = 1
            elif px < m * (1 - band):
                cur = 0
        out.append(cur)
    return out


def sma(closes: list[float], n: int = SMA_N) -> float | None:
    return sum(closes[-n:]) / n if len(closes) >= n else None


def vol20(closes: list[float], n: int = VOL_N) -> float | None:
    """Annualized standard deviation (n-1) of the last n daily log returns."""
    if len(closes) < n + 1:
        return None
    r = [math.log(closes[i] / closes[i - 1]) for i in range(len(closes) - n, len(closes))]
    return statistics.stdev(r) * math.sqrt(252)


def size_pct(vol: float | None, lev: int = LEVERAGE, target: float = VOL_TARGET) -> float | None:
    """Share of the sleeve (percent) in the leveraged fund while the signal is ON."""
    if not vol:
        return None
    return round(min(1.0, target / (lev * vol)) * 100, 1)


def reading(sym: str, dates: list[str], closes: list[float]) -> dict:
    """Everything the push and the report need for one index, as of the last close given."""
    st = band_states(closes)
    since = dates[-1]
    for i in range(len(st) - 1, 0, -1):
        if st[i] != st[i - 1]:
            since = dates[i]
            break
    else:
        since = None
    m = sma(closes)
    v = vol20(closes)
    fund, role = FUNDS.get(sym, ("?", ""))
    return {"sym": sym, "fund": fund, "role": role, "date": dates[-1], "close": round(closes[-1], 2),
            "sma200": round(m, 2) if m else None, "on_line": round(m * (1 + BAND), 2) if m else None,
            "off_line": round(m * (1 - BAND), 2) if m else None,
            "vs_sma_pct": round((closes[-1] / m - 1) * 100, 1) if m else None,
            "state": "ON" if st[-1] else "OFF", "since": since,
            "vol20_pct": round(v * 100, 1) if v else None, "size_pct": size_pct(v)}


def action(r: dict, prior_state: str | None = None) -> str:
    f = r["fund"]
    if r["state"] == "ON" and prior_state == "OFF":
        return f"BUY {f}: {r['size_pct']:.0f}% of this leg, rest in cash"
    if r["state"] == "OFF" and prior_state == "ON":
        return f"SELL all {f}"
    if r["state"] == "ON":
        return (f"hold {f} at {r['size_pct']:.0f}% of this leg (trade only if yours differs by more than "
                f"{REBALANCE_PTS:.0f} points); out below {r['off_line']:.2f}")
    return f"hold no {f}; turns ON above {r['on_line']:.2f}"


def action_live(r: dict, confirmed_state: str) -> str:
    """The action for a live reading: a state the close has not confirmed yet is conditional."""
    if r["state"] != confirmed_state:
        return "if it closes here: " + action(r, confirmed_state)
    return action(r)


def line(r: dict) -> str:
    return (f"{r['sym']} {r['close']:.2f} | 200d {r['sma200']:.2f} ({r['vs_sma_pct']:+.1f}%) | {r['state']}"
            f"{' since ' + r['since'][5:] if r['since'] else ''} | vol {r['vol20_pct']:.0f}%")


def weekday(d: str) -> int:
    return date.fromisoformat(d).weekday()


def decide(confirmed: dict[str, dict], live: dict[str, dict] | None, state: dict, session: str,
           final: bool, friday_window: bool) -> tuple[dict, list[str], bool, str]:
    """Pure. confirmed = readings on completed closes; live = readings with the live price as today's
    close (None after the close). Returns (new state, reasons to push, important?, kind).

    Push only when: a confirmed close flips a state; a live price is past the line that would flip it
    (once per index per session); the Friday update (before the close with live prices, or after it if
    the preview was missed); a catch-up when no weekly update went out for 8+ days; the first reading."""
    new = {k: (dict(v) if isinstance(v, dict) else v) for k, v in state.items()}
    new.setdefault("confirmed", {})
    new.setdefault("headsup", {})
    why, important, kind = [], False, ""
    sent = [d for d in (state.get("weekly_session"), state.get("preview_session")) if d]
    last_any = max(sent) if sent else None

    for s, r in confirmed.items():
        prev = state.get("confirmed", {}).get(s, {}).get("state")
        if prev and prev != r["state"] and final:
            why.append(f"{s} turned {r['state']} on the {r['since'] or r['date']} close: {action(r, prev)}")
            important = True
        if final or not prev:
            new["confirmed"][s] = {"state": r["state"], "date": r["date"], "size_pct": r["size_pct"]}

    if live and not final:
        for s, r in live.items():
            cur = state.get("confirmed", {}).get(s, {}).get("state") or confirmed[s]["state"]
            past = (cur == "ON" and r["close"] < r["off_line"]) or (cur == "OFF" and r["close"] > r["on_line"])
            if past and new["headsup"].get(s) != session:
                side = f"below the OFF line {r['off_line']:.2f}" if cur == "ON" else f"above the ON line {r['on_line']:.2f}"
                todo = f"sell all {r['fund']}" if cur == "ON" else f"buy {r['fund']} at {r['size_pct']:.0f}% of the leg"
                why.append(f"{s} is {r['close']:.2f}, {side}. If it closes there the rule says {todo}. Check at 2:45 pm CT")
                new["headsup"][s] = session
                important = True

    last = state.get("weekly_session")
    if friday_window and not final and state.get("preview_session") != session:
        why.append("Friday update, live prices, before the close")
        new["preview_session"] = session
        new["preview"] = {s: {"state": r["state"], "size_pct": r["size_pct"]} for s, r in (live or confirmed).items()}
        kind = "friday_preview"
    elif final and weekday(session) == 4 and last != session:
        pv = state.get("preview") if state.get("preview_session") == session else None
        changed = [s for s, r in confirmed.items() if pv and s in pv and (
            pv[s]["state"] != r["state"] or abs((pv[s]["size_pct"] or 0) - (r["size_pct"] or 0)) >= REBALANCE_PTS)]
        if not pv:
            why.append("Friday update, on the close")
            kind = "friday_close"
        elif changed:
            why.append("The close changed the Friday update for " + ", ".join(changed))
            kind = "friday_close"
            important = True
        new["weekly_session"] = session
    elif final and (not last_any or (date.fromisoformat(session) - date.fromisoformat(last_any)).days >= 8):
        why.append("First reading of the joint leveraged-ETF signal" if not last_any
                   else f"Catch-up: no weekly update since {last_any}")
        new["weekly_session"] = session
        kind = kind or "catch_up"

    if final:
        new["final_session"] = session
    return new, why, important, kind
