"""
DAY TRACK — mechanical opening-range day trading on QQQ (authorized by Ryan, live turn 2026-09-14).

WHY THIS EXISTS. Two weeks of autonomous operation (2026-08-27 .. 2026-09-14) produced 407
market-hours runs, 85 fully-evaluated intraday options triggers and ZERO options trades, while
the rulebook grew 22 KB of vetoes. The parts of the system that were MECHANICAL executed; the
parts that relied on judgment produced analysis. This module is the mechanical replacement for
the retired TACTICAL options track: one decision per day, every number computed from bars, every
exit a formula the run can evaluate without opinion.

THE STRATEGY (adapted from the 5-minute opening-range-breakout family: Zarattini & Aziz 2023 on
QQQ/TQQQ, and their 2024 stocks-in-play follow-up; adapted because this account cannot use the
4x leverage those papers assume and is polled every ~15 minutes rather than watched tick by tick):
  - Signal instrument: QQQ. Opening range = the first 5 minutes (09:30-09:35 ET), built from
    ONE-MINUTE bars (max of highs, min of lows) because 5-minute buckets from the feed are
    sometimes a single constituent minute (CLAUDE.md, feed-hole finding).
  - Direction = the OR bar's close vs open. A doji (body < 10% of range) = no trade today.
  - Entry: as early as the first run at/after 09:35 ET can act, in the OR direction. LONG via
    QQQ shares; SHORT via PSQ shares (1x inverse) — no margin, no short borrow, no options.
  - Initial stop: the OPPOSITE edge of the opening range, never closer than 0.1 x ATR14(daily).
  - Late-entry gate: if the run's price is already beyond the OR edge by more than 0.5 x the
    OR range, the stop is too far in R terms — SKIP. A missed entry is not recovered by chasing.
  - Size: shares = floor(min(deployable_cash, RISK_PCT x equity / stop_pct) / price). At this
    account size deployable CASH binds long before RISK_PCT does; RISK_PCT (band 5-20%, Ryan's
    choice) is the CEILING on risk per trade, not a target.
  - Dynamic exits (re-evaluated every run, stop lives at the BROKER as a resting stop order):
      * +1R reached  -> stop to breakeven.
      * +2R reached  -> trail: stop = max(stop, session_high - 1.5 x ATR14(5-min)), up only.
      * chop rule    -> first run at/after 12:00 ET with P&L inside +/-0.5R: close at market.
      * flat rule    -> first run at/after 15:30 ET: close at market, cancel the stop. NEVER
                        carried overnight; a GFD stop dies at the bell and the desk is absent.
  - Limits: ONE day trade per trading day. After 3 consecutive losing days OR a week at <= -3R,
    the track PAUSES for the rest of that week and escalates. Track pauses whenever total
    account value < $2,600 (cushion above the $2,000 margin-equity minimum).
  - Phases: PAPER first (log the trade the run COULD have taken, at the price it actually saw),
    then LIVE once graduate() says so. Live also requires the routine prompt that carries the
    stop-order authority (v11) — HARD RULE 5 still forbids stops for every other position.

ALL FUNCTIONS ARE PURE. The run fetches bars/quotes/portfolio via the Robinhood connector and
feeds them in. `python3 day_track.py` runs the self-tests.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, asdict

# ---------------------------------------------------------------------------
# Parameters. RISK_PCT is inside calibrate.BANDS["day_risk_pct"] = (5, 20) and may be moved by
# the weekly calibration only on in-regime evidence. Everything else is fixed by the spec.
# ---------------------------------------------------------------------------
SIGNAL_SYMBOL   = "QQQ"
LONG_VEHICLE    = "QQQ"
SHORT_VEHICLE   = "PSQ"          # 1x inverse. Phase 2 (after graduate()): TQQQ / SQQQ.
OR_MINUTES      = 5
DOJI_BODY_FRAC  = 0.10           # body < 10% of range = no signal
MIN_STOP_ATR    = 0.10           # stop distance >= 0.1 x ATR14(daily)
LATE_ENTRY_FRAC = 0.50           # skip if price is > 0.5 x OR range beyond the OR edge
RISK_PCT_START  = 5.0            # bottom of Ryan's 5-20 band; calibration may raise it
BREAKEVEN_R     = 1.0
TRAIL_START_R   = 2.0
TRAIL_ATR_MULT  = 1.5
CHOP_R          = 0.5
CHOP_TIME_ET    = "12:00"
FLAT_TIME_ET    = "15:30"
MAX_TRADES_DAY  = 1
PAUSE_CONSEC_LOSSES = 3
PAUSE_WEEK_R    = -3.0
MIN_EQUITY_USD  = 2600.0
PAPER_MIN_DAYS  = 10
PAPER_MIN_SIGNALS = 8


@dataclass
class OpeningRange:
    high: float
    low: float
    open: float
    close: float
    bars: int

    @property
    def range(self) -> float:
        return self.high - self.low

    @property
    def direction(self) -> str:
        """'long', 'short', or 'none' (doji / degenerate range)."""
        if self.range <= 0:
            return "none"
        if abs(self.close - self.open) < DOJI_BODY_FRAC * self.range:
            return "none"
        return "long" if self.close > self.open else "short"


def _bf(bar: dict, field: str) -> float:
    """One OHLC field off a bar, accepting BOTH spellings.

    get_equity_historicals returns 'open_price'/'high_price'/'low_price'/'close_price';
    the terse 'open'/'high'/'low'/'close' form is what hand-built fixtures and most
    other feeds use. Reading only the terse form raised KeyError on every real
    connector bar — see holdings.json._DAY_TRACK_BAR_SCHEMA_MISMATCH. Prefer the
    connector spelling so a bar carrying both is read the way the broker meant it."""
    for key in (f"{field}_price", field):
        if key in bar:
            return float(bar[key])
    raise KeyError(
        f"bar has no {field!r} field (tried {field}_price, {field}); keys={sorted(bar)}"
    )


def opening_range(minute_bars: list[dict]) -> OpeningRange | None:
    """Build the OR from the first OR_MINUTES one-minute bars of the session (each bar a dict
    with open/high/low/close — either spelling, see _bf — in time order, starting at 09:30 ET).
    Returns None if fewer than OR_MINUTES bars are present — the run must wait, never guess."""
    bars = minute_bars[:OR_MINUTES]
    if len(bars) < OR_MINUTES:
        return None
    return OpeningRange(
        high=max(_bf(b, "high") for b in bars),
        low=min(_bf(b, "low") for b in bars),
        open=_bf(bars[0], "open"),
        close=_bf(bars[-1], "close"),
        bars=len(bars),
    )


def atr(bars: list[dict], n: int = 14) -> float | None:
    """Wilder-free simple ATR over the last n bars (true range averaged). None if < n+1 bars."""
    if len(bars) < n + 1:
        return None
    trs = []
    for prev, cur in zip(bars[-n - 1:-1], bars[-n:]):
        h, l, pc = _bf(cur, "high"), _bf(cur, "low"), _bf(prev, "close")
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    return sum(trs) / n


def initial_stop(or_: OpeningRange, direction: str, atr_daily: float) -> float:
    """Opposite OR edge, pushed out to MIN_STOP_ATR x ATR14(daily) if the range is tighter."""
    min_dist = MIN_STOP_ATR * atr_daily
    if direction == "long":
        return min(or_.low, or_.high - min_dist) if or_.range < min_dist else or_.low
    return max(or_.high, or_.low + min_dist) if or_.range < min_dist else or_.high


def late_entry_ok(or_: OpeningRange, direction: str, price: float) -> bool:
    """False when price has already run more than LATE_ENTRY_FRAC x OR range beyond the edge."""
    if direction == "long":
        return price <= or_.high + LATE_ENTRY_FRAC * or_.range
    return price >= or_.low - LATE_ENTRY_FRAC * or_.range


def size(price: float, stop: float, equity: float, deployable_cash: float,
         risk_pct: float = RISK_PCT_START) -> dict:
    """Whole shares. Risk cap = risk_pct% of equity; cash cap = deployable. The binding one wins.
    Returns shares, dollars, risk_usd (actual $ at the stop), and which cap bound."""
    stop_dist = abs(price - stop)
    if stop_dist <= 0 or price <= 0:
        return {"shares": 0, "dollars": 0.0, "risk_usd": 0.0, "bound_by": "invalid"}
    risk_budget = risk_pct / 100.0 * equity
    by_risk = risk_budget / (stop_dist / price)          # dollars of position the risk allows
    dollars_cap = min(deployable_cash, by_risk)
    shares = math.floor(dollars_cap / price)
    return {
        "shares": shares,
        "dollars": round(shares * price, 2),
        "risk_usd": round(shares * stop_dist, 2),
        "r_usd": round(shares * stop_dist, 2),
        "bound_by": "cash" if deployable_cash < by_risk else "risk",
    }


def plan_entry(minute_bars: list[dict], daily_bars: list[dict], price_now: float,
               equity: float, deployable_cash: float, risk_pct: float = RISK_PCT_START) -> dict:
    """The whole entry decision in one call. Returns a dict with 'action' in
    {'wait','skip','enter'} and the reason; on 'enter' it carries vehicle/side/stop/size/R."""
    or_ = opening_range(minute_bars)
    if or_ is None:
        return {"action": "wait", "reason": f"fewer than {OR_MINUTES} one-minute bars yet"}
    direction = or_.direction
    if direction == "none":
        return {"action": "skip", "reason": "doji opening bar (body < 10% of range)",
                "or": asdict(or_)}
    a = atr(daily_bars, 14)
    if a is None:
        return {"action": "wait", "reason": "need 15 daily bars for ATR14"}
    stop = initial_stop(or_, direction, a)
    if not late_entry_ok(or_, direction, price_now):
        return {"action": "skip", "reason": "late entry: price already > 0.5 x OR range beyond the edge",
                "or": asdict(or_), "price_now": price_now, "stop": stop}
    sz = size(price_now, stop, equity, deployable_cash, risk_pct)
    if sz["shares"] < 1:
        return {"action": "skip", "reason": "cannot afford one whole share inside the caps",
                "or": asdict(or_), "size": sz}
    return {
        "action": "enter", "direction": direction,
        "vehicle": LONG_VEHICLE if direction == "long" else SHORT_VEHICLE,
        "signal_symbol": SIGNAL_SYMBOL, "or": asdict(or_), "atr14_daily": round(a, 4),
        "entry_px_expected": price_now, "stop_px_signal": round(stop, 4),
        "stop_dist_pct": round(abs(price_now - stop) / price_now * 100, 4),
        "size": sz, "risk_pct_used": risk_pct,
        "note": ("stop is expressed on the SIGNAL symbol; for PSQ translate as "
                 "psq_stop = psq_entry * (1 + stop_dist_pct/100) since PSQ moves ~-1x QQQ"),
    }


def r_multiple(direction: str, entry: float, price: float, stop_dist: float) -> float:
    move = (price - entry) if direction == "long" else (entry - price)
    return move / stop_dist if stop_dist else 0.0


def manage(direction: str, entry: float, stop: float, price: float, session_extreme: float,
           atr5: float | None, time_et: str, stop_dist: float) -> dict:
    """One management pass. Returns {'action': 'hold'|'raise_stop'|'close', 'stop': new_stop,
    'reason', 'r'}. session_extreme = session high (long) or low (short) since entry. The stop
    only ever ratchets in the trade's favor. Time strings are 'HH:MM' ET, compared lexically."""
    r = r_multiple(direction, entry, price, stop_dist)
    # 1. stop already hit (the broker order should have filled; the run reconciles)
    if (direction == "long" and price <= stop) or (direction == "short" and price >= stop):
        return {"action": "close", "stop": stop, "reason": "stop level reached", "r": round(r, 3)}
    # 2. hard flat rule
    if time_et >= FLAT_TIME_ET:
        return {"action": "close", "stop": stop, "reason": "flat rule (>= 15:30 ET)", "r": round(r, 3)}
    # 3. chop rule
    if time_et >= CHOP_TIME_ET and abs(r) < CHOP_R:
        return {"action": "close", "stop": stop, "reason": "chop rule (>= 12:00 ET, |R| < 0.5)", "r": round(r, 3)}
    # 4. ratchets
    new_stop = stop
    if r >= TRAIL_START_R and atr5:
        trail = (session_extreme - TRAIL_ATR_MULT * atr5) if direction == "long" \
            else (session_extreme + TRAIL_ATR_MULT * atr5)
        new_stop = max(new_stop, trail) if direction == "long" else min(new_stop, trail)
    if r >= BREAKEVEN_R:
        new_stop = max(new_stop, entry) if direction == "long" else min(new_stop, entry)
    if new_stop != stop:
        return {"action": "raise_stop", "stop": round(new_stop, 4),
                "reason": f"ratchet at {r:.2f}R", "r": round(r, 3)}
    return {"action": "hold", "stop": stop, "reason": f"working, {r:.2f}R", "r": round(r, 3)}


def track_status(equity: float, recent_results_r: list[float], week_results_r: list[float]) -> dict:
    """Pause logic. recent_results_r = R-multiples of the most recent closed day trades, newest
    LAST; week_results_r = this week's. Returns {'paused': bool, 'reason'}."""
    if equity < MIN_EQUITY_USD:
        return {"paused": True, "reason": f"equity ${equity:,.0f} < ${MIN_EQUITY_USD:,.0f} cushion"}
    tail = recent_results_r[-PAUSE_CONSEC_LOSSES:]
    if len(tail) == PAUSE_CONSEC_LOSSES and all(x < 0 for x in tail):
        return {"paused": True, "reason": f"{PAUSE_CONSEC_LOSSES} consecutive losing days — rest of week"}
    if sum(week_results_r) <= PAUSE_WEEK_R:
        return {"paused": True, "reason": f"week at {sum(week_results_r):.2f}R <= {PAUSE_WEEK_R}R — rest of week"}
    return {"paused": False, "reason": "active"}


def graduate(paper_days: int, paper_trades_r: list[float]) -> dict:
    """PAPER -> LIVE decision. Needs enough days and signals AND positive expectancy AND a
    win rate above the breakeven implied by the payoff ratio (same statistic calibrate.py uses)."""
    n = len(paper_trades_r)
    if paper_days < PAPER_MIN_DAYS or n < PAPER_MIN_SIGNALS:
        return {"go_live": False, "reason": f"paper {paper_days}d / {n} trades; need "
                f"{PAPER_MIN_DAYS}d and {PAPER_MIN_SIGNALS} trades"}
    wins = [x for x in paper_trades_r if x > 0]
    losses = [x for x in paper_trades_r if x < 0]
    expectancy = sum(paper_trades_r) / n
    if not wins or not losses:
        return {"go_live": expectancy > 0 and bool(wins), "reason": "one-sided sample; "
                f"expectancy {expectancy:.2f}R", "expectancy_r": round(expectancy, 3)}
    payoff = (sum(wins) / len(wins)) / abs(sum(losses) / len(losses))
    breakeven_wr = 1 / (1 + payoff)
    wr = len(wins) / n
    ok = expectancy > 0 and wr > breakeven_wr
    return {"go_live": ok, "expectancy_r": round(expectancy, 3), "win_rate": round(wr, 3),
            "payoff": round(payoff, 3), "breakeven_win_rate": round(breakeven_wr, 3),
            "margin_pts": round((wr - breakeven_wr) * 100, 1),
            "reason": "criteria met" if ok else "expectancy or margin not positive"}


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------
def _selftest() -> None:
    mb = [dict(open=700.0, high=700.8, low=699.6, close=700.5),
          dict(open=700.5, high=701.2, low=700.3, close=701.0),
          dict(open=701.0, high=701.5, low=700.7, close=701.3),
          dict(open=701.3, high=701.9, low=701.0, close=701.6),
          dict(open=701.6, high=702.0, low=701.2, close=701.8)]
    orr = opening_range(mb)
    assert orr and orr.high == 702.0 and orr.low == 699.6 and orr.direction == "long"
    assert opening_range(mb[:4]) is None
    doji = [dict(open=700.0, high=701.0, low=699.0, close=700.05)] * 5
    assert opening_range(doji).direction == "none"

    # CONNECTOR SCHEMA — verbatim get_equity_historicals(QQQ, interval='minute') bars,
    # 2026-09-14 13:30-13:34Z. The terse-key fixtures above CANNOT catch a code path that
    # only reads 'high'/'low'/'open'/'close', because they encode the same assumption as
    # the bug; this case is the one that fails if _bf is ever removed. Values are strings
    # from the wire, on purpose.
    wire = [{"begins_at": "2026-09-14T13:30:00Z", "open_price": "703.330000",
             "close_price": "702.860000", "high_price": "703.670000",
             "low_price": "702.800000", "volume": 682593, "session": "reg"},
            {"begins_at": "2026-09-14T13:31:00Z", "open_price": "702.870000",
             "close_price": "703.160000", "high_price": "703.607600",
             "low_price": "702.750000", "volume": 178772, "session": "reg"},
            {"begins_at": "2026-09-14T13:32:00Z", "open_price": "703.160000",
             "close_price": "703.630000", "high_price": "703.860000",
             "low_price": "703.090000", "volume": 110956, "session": "reg"},
            {"begins_at": "2026-09-14T13:33:00Z", "open_price": "703.640000",
             "close_price": "703.310000", "high_price": "703.990000",
             "low_price": "703.279700", "volume": 234331, "session": "reg"},
            {"begins_at": "2026-09-14T13:34:00Z", "open_price": "703.290000",
             "close_price": "703.340000", "high_price": "703.690000",
             "low_price": "703.090000", "volume": 151811, "session": "reg"}]
    wor = opening_range(wire)
    assert wor and wor.high == 703.99 and wor.low == 702.75, wor
    assert wor.open == 703.33 and wor.close == 703.34, wor
    assert wor.direction == "none", wor          # body 0.01 < 0.1 * 1.24 range -> doji
    wdaily = [dict(open_price="700", high_price="708",
                   low_price="694", close_price="701")] * 16
    assert abs(atr(wdaily) - 14.0) < 1e-9        # atr() reads the wire schema too

    daily = [dict(open=700, high=708, low=694, close=701)] * 16
    assert abs(atr(daily) - 14.0) < 1e-9
    assert atr(daily[:10]) is None

    # stop = OR low (range 2.4 > 0.1*14=1.4)
    assert initial_stop(orr, "long", 14.0) == 699.6
    tight = OpeningRange(high=700.5, low=700.0, open=700.0, close=700.4, bars=5)
    assert abs(initial_stop(tight, "long", 14.0) - (700.5 - 1.4)) < 1e-9

    assert late_entry_ok(orr, "long", 702.5)            # 0.5 above edge, range 2.4 -> ok
    assert not late_entry_ok(orr, "long", 703.5)        # 1.5 above edge > 1.2 -> skip

    sz = size(price=702.0, stop=699.6, equity=3884.0, deployable_cash=1470.0, risk_pct=5.0)
    assert sz["shares"] == 2 and sz["bound_by"] == "cash", sz   # cash binds at this size
    sz2 = size(price=702.0, stop=699.6, equity=3884.0, deployable_cash=200000.0, risk_pct=5.0)
    assert sz2["bound_by"] == "risk" and sz2["risk_usd"] <= 0.05 * 3884 + 2.4, sz2

    plan = plan_entry(mb, daily, 702.0, 3884.0, 1470.0)
    assert plan["action"] == "enter" and plan["vehicle"] == "QQQ" and plan["size"]["shares"] == 2
    assert plan_entry(doji, daily, 700.0, 3884.0, 1470.0)["action"] == "skip"
    assert plan_entry(mb, daily, 704.0, 3884.0, 1470.0)["reason"].startswith("late entry")

    sd = 2.4
    m = manage("long", 702.0, 699.6, 703.0, 703.2, 0.6, "10:15", sd)
    assert m["action"] == "hold"
    m = manage("long", 702.0, 699.6, 704.5, 704.6, 0.6, "10:30", sd)        # +1.04R
    assert m["action"] == "raise_stop" and m["stop"] == 702.0
    m = manage("long", 702.0, 702.0, 707.0, 707.5, 0.6, "11:00", sd)        # +2.08R -> trail
    assert m["action"] == "raise_stop" and abs(m["stop"] - (707.5 - 0.9)) < 1e-9
    m = manage("long", 702.0, 699.6, 702.3, 702.9, 0.6, "12:05", sd)        # chop
    assert m["action"] == "close" and m["reason"].startswith("chop")
    m = manage("long", 702.0, 699.6, 705.0, 705.5, 0.6, "15:31", sd)        # flat
    assert m["action"] == "close" and m["reason"].startswith("flat")
    m = manage("short", 702.0, 704.4, 701.0, 700.8, 0.6, "10:15", sd)
    assert m["action"] == "hold"
    m = manage("short", 702.0, 704.4, 699.5, 699.4, 0.6, "10:20", sd)       # +1.04R short
    assert m["action"] == "raise_stop" and m["stop"] == 702.0

    assert track_status(3884, [1, -1, -1, -1], [-1, -1, -1])["paused"]
    assert track_status(3884, [1, -1, 2], [1, -1, 2])["paused"] is False
    assert track_status(2400, [], [])["paused"]
    assert track_status(3884, [], [-1, -1.2, -0.9])["paused"]

    assert graduate(5, [1] * 10)["go_live"] is False
    g = graduate(10, [1.5, -1, 2.0, -1, 0.8, -1, 1.2, 3.0])
    assert g["go_live"] and g["expectancy_r"] > 0, g
    g = graduate(10, [-1, -1, 0.3, -1, 0.2, -1, -1, 0.1])
    assert g["go_live"] is False
    print("day_track selftest OK")


if __name__ == "__main__":
    _selftest()
