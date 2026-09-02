"""
Weekly CALIBRATION — measure the strategy's own edge and adapt the parameters to it.

WHY THIS EXISTS (Ryan, live turn 2026-09-02): "i think maybe i am influencing too much
and want you to try and figure out how to optimize this system periodically in the market
as it changes." Hand-tuning a strategy from a handful of recent trades is how a desk
overfits to noise; this module replaces that with a measurement made on the SAME statistic
every week, from the broker's own record, with pre-authorized adjustment bands and an
explicit escalation when a change would fall outside them.

WHAT IT IS NOT: a forecaster. It does not predict the regime. It measures whether THIS
strategy's edge is currently present, which is the only question the parameters depend on.
The RSI(2) book is a mean-reversion engine: it works in range-bound tapes and degrades in
trending ones. Rather than trying to classify the tape, the primary signal here is the
strategy's OWN trailing hit rate — a direct measurement of the edge, not a proxy for it.

ALL FUNCTIONS ARE PURE. The caller (a scheduled run, which has broker access via the
Robinhood connector) fetches the trade history and feeds it in. That keeps this module
testable offline and keeps the network in one place.

Usage from a run:
    from calibrate import edge_stats, recommend, format_report
    eq = [t for t in broker_trades if t["side"] == "sell"]      # equities
    print(format_report(recommend(edge_stats(eq), current_params)))
"""

from __future__ import annotations

import json
import statistics as st
import sys
from dataclasses import dataclass, asdict

# ---------------------------------------------------------------------------
# Pre-authorized adjustment bands. A recommendation inside its band is applied
# by the run and logged; one outside it is ESCALATED to Ryan and NOT applied.
# These bands are the whole safety model of this module — widen them only with
# Ryan's explicit instruction, never because a measurement wants more room.
# ---------------------------------------------------------------------------
BANDS = {
    "swing_time_stop_days": (8, 21),      # report.SWING_TIME_STOP_DAYS
    "target_positions":     (3, 5),       # concurrent equity swing positions
    "rsi2_oversold":        (5.0, 15.0),  # report.RSI2_OVERSOLD (entry trigger)
}

# The edge is measured against the BREAKEVEN win rate implied by the payoff ratio,
# never against an absolute number: at payoff 1.0 you need 50%, at payoff 2.0 only 33%.
# Comparing a raw win rate to a fixed threshold is the classic way to misread a strategy.
MIN_TRADES_FOR_ACTION = 20    # below this, report but NEVER adjust — n is too small
DEGRADED_MARGIN_PTS   = 5.0   # margin over breakeven under this = tighten
HEALTHY_MARGIN_PTS    = 15.0  # margin over breakeven above this = the edge is intact
KILL_MARGIN_PTS       = 0.0   # margin at or below this = halve size and escalate


@dataclass
class EdgeStats:
    n: int
    wins: int
    losses: int
    win_rate: float          # fraction
    mean_win: float
    mean_loss: float         # negative
    payoff_ratio: float      # mean_win / abs(mean_loss)
    expectancy: float        # per trade, $
    net: float
    breakeven_win_rate: float
    margin_pts: float        # (win_rate - breakeven) in PERCENTAGE POINTS


def edge_stats(trades: list[dict], key: str = "realized_gain") -> EdgeStats | None:
    """Compute the edge statistics for a list of closed trades.

    `trades` is the broker's per-trade realized P&L (get_pnl_trade_history), newest
    first or oldest first — order does not matter here. Returns None on an empty list
    or when the sample has no losses (a payoff ratio needs both sides; a lossless
    sample is not evidence of an infinite edge, it is evidence of too few trades)."""
    if not trades:
        return None
    g = [float(t[key]) for t in trades]
    w = [x for x in g if x > 0]
    l = [x for x in g if x < 0]
    if not w or not l:
        return None
    mean_win, mean_loss = st.mean(w), st.mean(l)
    payoff = mean_win / abs(mean_loss)
    breakeven = abs(mean_loss) / (mean_win + abs(mean_loss))
    win_rate = len(w) / len(g)
    return EdgeStats(
        n=len(g), wins=len(w), losses=len(l), win_rate=win_rate,
        mean_win=mean_win, mean_loss=mean_loss, payoff_ratio=payoff,
        expectancy=sum(g) / len(g), net=sum(g),
        breakeven_win_rate=breakeven, margin_pts=(win_rate - breakeven) * 100.0,
    )


def _clamp(name: str, value):
    lo, hi = BANDS[name]
    return max(lo, min(hi, value)), (lo <= value <= hi)


def recommend(stats: EdgeStats | None, current: dict,
              in_regime_trades: int | None = None) -> dict:
    """Turn an edge measurement into parameter recommendations.

    `current` holds the live values, e.g.
        {"swing_time_stop_days": 14, "target_positions": 4, "rsi2_oversold": 10.0}

    `in_regime_trades` is how many of the sampled trades CLOSED UNDER THE CURRENT
    PARAMETER SET. Defaults to stats.n (i.e. "the whole sample is in-regime").

    WHY THIS ARGUMENT EXISTS — it caught a real bug on this module's first run.
    Fed the live book's 53 closes, the calibration returned HEALTHY and proposed
    loosening swing_time_stop_days 14 -> 16. Every one of those 53 trades closed
    BEFORE the time stop existed (it was dead code until 2026-09-02), so the sample
    contained exactly zero evidence about the parameter it wanted to change. Tuning a
    parameter on data that predates it is not calibration, it is superstition — and it
    is indistinguishable from the real thing unless you count the in-regime trades.
    After a parameter change, that parameter's evidence resets to zero.

    The logic is deliberately boring and one-directional per state — a calibration that
    can argue itself into any answer is not a calibration:

      • margin <= KILL      -> the edge is GONE. Halve position size, pause new entries,
                               ESCALATE. Never "wait one more week" — that reasoning is
                               how a losing system survives its own review.
      • margin <  DEGRADED  -> tighten: shorter time stop (recycle faster), stricter entry
                               (lower RSI2 trigger), fewer concurrent positions.
      • margin >  HEALTHY   -> the edge is present. Do NOT loosen the entry trigger — a
                               working strategy is not an invitation to take worse setups.
                               Allow a slightly longer time stop so winners get room.
      • otherwise           -> hold everything. No change is the most common correct output.
    """
    out = {"stats": asdict(stats) if stats else None, "changes": {},
           "escalate": [], "notes": [], "verdict": ""}

    if stats is None:
        out["verdict"] = "INSUFFICIENT DATA — no adjustment"
        out["notes"].append("Sample empty or one-sided (needs both wins and losses).")
        return out

    if stats.n < MIN_TRADES_FOR_ACTION:
        out["verdict"] = f"REPORT ONLY — n={stats.n} < {MIN_TRADES_FOR_ACTION}"
        out["notes"].append(
            f"Measured margin {stats.margin_pts:+.1f} pts over a {stats.breakeven_win_rate:.0%} "
            f"breakeven, but n is too small to act on. Report, do not adjust.")
        return out

    in_regime = stats.n if in_regime_trades is None else in_regime_trades
    m = stats.margin_pts

    # The KILL branch is deliberately exempt from the in-regime gate below: if the book
    # is losing money, "these trades predate the current settings" is not a reason to
    # keep sizing into it. Risk-off never waits for a clean sample.
    if m > KILL_MARGIN_PTS and in_regime < MIN_TRADES_FOR_ACTION:
        out["verdict"] = (f"REPORT ONLY — only {in_regime} of {stats.n} trades closed under "
                          f"the current parameters (need {MIN_TRADES_FOR_ACTION})")
        out["notes"].append(
            f"Measured margin {stats.margin_pts:+.1f} pts, but the sample largely predates "
            f"the current settings, so it carries no evidence about them. Tuning on it "
            f"would be superstition. Report, do not adjust; the evidence rebuilds as "
            f"trades close under the new parameters.")
        return out

    proposed = dict(current)

    if m <= KILL_MARGIN_PTS:
        out["verdict"] = "EDGE GONE — halve size, pause new entries, ESCALATE"
        out["escalate"].append(
            f"Trailing {stats.n} trades show a {m:+.1f} pt margin over the "
            f"{stats.breakeven_win_rate:.0%} breakeven win rate implied by a "
            f"{stats.payoff_ratio:.2f} payoff. Expectancy ${stats.expectancy:+.2f}/trade. "
            f"The strategy is not currently profitable. Position size halved and new "
            f"entries paused pending Ryan's review.")
        out["changes"]["position_size_multiplier"] = 0.5
        out["changes"]["new_entries"] = "PAUSED"
        return out

    if m < DEGRADED_MARGIN_PTS:
        out["verdict"] = f"DEGRADED ({m:+.1f} pts) — tighten"
        proposed["swing_time_stop_days"] = current["swing_time_stop_days"] - 3
        proposed["rsi2_oversold"] = current["rsi2_oversold"] - 2.0
        proposed["target_positions"] = current["target_positions"] - 1
        out["notes"].append(
            "Edge present but thin: recycle capital faster, demand a deeper oversold "
            "print, and carry fewer concurrent positions until the margin recovers.")
    elif m > HEALTHY_MARGIN_PTS:
        out["verdict"] = f"HEALTHY ({m:+.1f} pts) — hold entry bar, allow room"
        proposed["swing_time_stop_days"] = current["swing_time_stop_days"] + 2
        out["notes"].append(
            "Edge intact. Time stop loosened slightly so winners get room. The entry "
            "trigger is deliberately NOT loosened — a working strategy is not a reason "
            "to take worse setups.")
    else:
        out["verdict"] = f"STABLE ({m:+.1f} pts) — no change"
        out["notes"].append("Everything inside tolerance. No change is the correct output.")

    for k, v in proposed.items():
        if k not in BANDS or v == current.get(k):
            continue
        clamped, in_band = _clamp(k, v)
        if not in_band:
            out["escalate"].append(
                f"{k}: measurement wants {v}, which is outside its authorized band "
                f"{BANDS[k]}. Clamped to {clamped}; the full change needs Ryan.")
        if clamped != current.get(k):
            out["changes"][k] = clamped
    return out


def format_report(rec: dict) -> str:
    s, lines = rec.get("stats"), []
    lines.append(f"VERDICT: {rec['verdict']}")
    if s:
        lines.append(
            f"  n={s['n']}  win rate {s['win_rate']:.0%} ({s['wins']}W/{s['losses']}L)  "
            f"payoff {s['payoff_ratio']:.2f}  expectancy ${s['expectancy']:+.2f}/trade  "
            f"net ${s['net']:+.2f}")
        lines.append(
            f"  breakeven win rate {s['breakeven_win_rate']:.0%} -> "
            f"MARGIN {s['margin_pts']:+.1f} pts")
    for n in rec["notes"]:
        lines.append(f"  note: {n}")
    for k, v in rec["changes"].items():
        lines.append(f"  CHANGE: {k} -> {v}")
    for e in rec["escalate"]:
        lines.append(f"  *** ESCALATE TO RYAN: {e}")
    if not rec["changes"] and not rec["escalate"]:
        lines.append("  no parameter changes")
    return "\n".join(lines)


if __name__ == "__main__":
    # Feed it the broker's trade list as JSON on stdin:
    #   [{"realized_gain": "12.67"}, {"realized_gain": "-8.07"}, ...]
    blob = json.load(sys.stdin)
    trades = blob["trades"] if isinstance(blob, dict) else blob
    current = {"swing_time_stop_days": 14, "target_positions": 4, "rsi2_oversold": 10.0}
    print(format_report(recommend(edge_stats(trades), current)))
