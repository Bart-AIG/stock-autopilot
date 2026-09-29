"""
OPTIONS GRADE + EXIT MONITOR — pure functions, no network (Ryan, live turn 2026-09-29).

Authority: "update this rule, to total options money is capped at 20% of account. no other rule
on how much per trade. make sure these get graded using options related things as well as the
name itself and make sure its based off current info before the options trade is made, then
monitor it for exit."

So this module does three jobs, and every run that touches options calls it:

  1. SIZING. The ONLY dollar limit is the bucket: total agentic premium at risk (hedge included)
     <= 20% of get_portfolio.total_value. There is NO per-trade cap -- one trade may use the
     whole remaining bucket. (The 2026-09-25 "max 50% of the bucket per trade" rule is VOID.)
     Every other limit still applies: max 3 open CORE positions, 1 entry/run, 3/day, the -$400
     daily loss cap, the -40% bucket pause, no margin.

  2. GRADE. grade_contract() grades the TRADE, not just the stock: the underlying's quality
     grade (grade.py letter) AND the contract itself -- liquidity, open interest, delta, DTE,
     implied vs realized vol, breakeven against the thesis target, and theta burn. A great
     stock on a bad contract is not a trade. Only a combined A or A+ may be entered.
     It runs on CURRENT data only: a quote older than MAX_QUOTE_AGE_S, or one taken in the
     opening auction window, is a hard fail -- re-quote and re-grade immediately before sending.

  3. EXIT. exit_check() is the 2026-08-05 exit engine as a formula, evaluated every run on every
     open agentic option position: setup break / thesis break first, DTE-scaled premium
     backstops on losers, pop-bank and a trailing ratchet on winners, the 21-DTE review, the
     flat-by-DTE-2 rule and the pre-earnings close. Ownership and the hedge exemption are
     respected: a placed_agent 'user' position returns 'notify', never 'close'.

Nothing here places an order. The run acts on the returned dict and records it in the ledger.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

# ---- sizing -----------------------------------------------------------------------------
BUCKET_PCT = 0.20                 # total options premium at risk <= 20% of total_value

# ---- contract hard gates (fail any one = not tradeable) --------------------------------
MAX_SPREAD_PCT_OF_MID = 10.0      # each leg
MIN_OPEN_INTEREST = 100           # each leg
DTE_MIN, DTE_MAX = 21, 45         # CORE window
ABS_DELTA_MIN, ABS_DELTA_MAX = 0.25, 0.60
MIN_TARGET_PAYOFF_RATIO = 0.20    # at the thesis target the trade must return >= 20% of premium
MAX_QUOTE_AGE_S = 120             # "current info": quote must be <= 2 min old when graded
OPEN_WINDOW_UTC = ("13:30", "13:35")  # never grade/price off the opening auction
HEDGE_SYMBOLS = ("SPY", "QQQ")

# ---- exit engine (2026-08-05 amendment) ------------------------------------------------
POP_BANK_1D = 0.80                # one-day gain >= +80% -> sell into strength
RATCHET_ARM = 0.50                # peak gain >= +50% arms the lock
RATCHET_GIVEBACK = 0.40           # exit if the gain gives back 40% of its peak
REVIEW_DTE = 21
FLAT_BY_DTE = 2


def bucket(total_value: float, premium_at_risk: float) -> dict:
    """The bucket and what is left of it. There is no per-trade cap: 'remaining' IS the max
    a new trade may cost."""
    cap = round(BUCKET_PCT * total_value, 2)
    return {"bucket": cap, "premium_at_risk": round(premium_at_risk, 2),
            "remaining": round(max(0.0, cap - premium_at_risk), 2)}


def _age_s(updated_at: str, now: datetime) -> float:
    """Seconds since a connector timestamp like '2026-09-29T16:12:15.498108766Z' (nanosecond
    fractions are cut to microseconds, which datetime can parse)."""
    s = updated_at.replace("Z", "+00:00")
    m = re.match(r"^(.*?T\d\d:\d\d:\d\d)(\.\d+)?(.*)$", s)
    frac = (m.group(2) or "")[:7]
    ts = datetime.fromisoformat(m.group(1) + frac + (m.group(3) or "+00:00"))
    return (now - ts).total_seconds()


def _f(x) -> float | None:
    return None if x in (None, "") else float(x)


def grade_contract(*, symbol: str, side: str, underlying_letter: str | None,
                   underlying_bottom_decile_below_200: bool = False,
                   legs: list[dict], spot: float, target: float, dte: int,
                   iv_rv_ex_gap: float | None, binary_event_before_expiry: bool,
                   event_is_thesis: bool = False, bucket_remaining: float,
                   now: datetime | None = None) -> dict:
    """Grade one candidate trade on CURRENT data.

    side: 'call' or 'put' (direction of the long leg).
    legs: the raw get_option_quotes 'quote' dicts plus 'strike' and 'role' ('long' | 'short').
          One leg = single long option; two legs = debit vertical (same type/expiry).
    target: the thesis target on the underlying (the price the thesis says to bank at).
    iv_rv_ex_gap: today's ex-gap IV/RV ratio from iv_history.json (None if not computed).

    Returns {'tradeable', 'grade', 'underlying', 'option_score', 'fails', 'points', 'cost',
    'max_loss', 'payoff_at_target', 'breakeven'}. Only grade A/A+ with tradeable=True may enter.
    """
    now = now or datetime.now(timezone.utc)
    fails: list[str] = []
    pts: dict[str, int] = {}

    # --- 1. the NAME ---------------------------------------------------------------------
    u = (underlying_letter or "").upper()
    if symbol.upper() in HEDGE_SYMBOLS and side == "put":
        u_eff = "A"                                   # authorized hedge vehicle
    elif side == "call":
        u_eff = u if u in ("A+", "A") else ""
        if not u_eff:
            fails.append(f"underlying grade {u or 'none'} -- calls need A/A+")
    else:
        u_eff = "A" if underlying_bottom_decile_below_200 else ""
        if not u_eff:
            fails.append("puts need a bottom-decile name below its 200-day (or SPY/QQQ hedge)")

    # --- 2. CURRENT INFO -----------------------------------------------------------------
    hhmm = now.strftime("%H:%M")
    if OPEN_WINDOW_UTC[0] <= hhmm < OPEN_WINDOW_UTC[1]:
        fails.append(f"opening auction window ({hhmm}Z) -- re-quote after 13:35Z")
    for lg in legs:
        age = _age_s(lg["updated_at"], now)
        if age > MAX_QUOTE_AGE_S:
            fails.append(f"{lg['role']} quote is {age:.0f}s old (> {MAX_QUOTE_AGE_S}s) -- re-quote")

    # --- 3. the CONTRACT -----------------------------------------------------------------
    if not DTE_MIN <= dte <= DTE_MAX:
        fails.append(f"DTE {dte} outside {DTE_MIN}-{DTE_MAX}")
    worst_spread, min_oi = 0.0, 10 ** 9
    for lg in legs:
        bid, ask = _f(lg["bid_price"]), _f(lg["ask_price"])
        mid = (bid + ask) / 2 if bid and ask else 0.0
        sp = 100 * (ask - bid) / mid if mid else 999.0
        worst_spread = max(worst_spread, sp)
        min_oi = min(min_oi, int(lg.get("open_interest") or 0))
    if worst_spread > MAX_SPREAD_PCT_OF_MID:
        fails.append(f"spread {worst_spread:.1f}% of mid > {MAX_SPREAD_PCT_OF_MID}%")
    if min_oi < MIN_OPEN_INTEREST:
        fails.append(f"open interest {min_oi} < {MIN_OPEN_INTEREST}")

    long_leg = next(lg for lg in legs if lg["role"] == "long")
    short_leg = next((lg for lg in legs if lg["role"] == "short"), None)
    delta = abs(_f(long_leg["delta"]) or 0.0) - (abs(_f(short_leg["delta"]) or 0.0) if short_leg else 0.0)
    long_delta = abs(_f(long_leg["delta"]) or 0.0)
    if not ABS_DELTA_MIN <= long_delta <= ABS_DELTA_MAX:
        fails.append(f"long-leg delta {long_delta:.2f} outside {ABS_DELTA_MIN}-{ABS_DELTA_MAX}")

    # cost at the TOUCH (what an entry actually pays): long at ask, short at bid
    debit = _f(long_leg["ask_price"]) - (_f(short_leg["bid_price"]) if short_leg else 0.0)
    cost = round(100 * debit, 2)
    if cost > bucket_remaining:
        fails.append(f"cost ${cost:.0f} > bucket remaining ${bucket_remaining:.0f}")

    if binary_event_before_expiry and not event_is_thesis:
        fails.append("underlying's own earnings/binary event before expiry")

    # payoff at the thesis target, at expiry (conservative: ignores remaining time value)
    k_long = float(long_leg["strike"])
    sgn = 1 if side == "call" else -1
    intrinsic = max(0.0, sgn * (target - k_long))
    if short_leg:
        width = abs(float(short_leg["strike"]) - k_long)
        intrinsic = min(intrinsic, width)
    payoff = intrinsic - debit
    ratio = payoff / debit if debit > 0 else -1.0
    breakeven = k_long + sgn * debit
    if ratio < MIN_TARGET_PAYOFF_RATIO:
        fails.append(f"pays {ratio:+.0%} of premium at the ${target} target -- wrong vehicle")

    # --- 4. SCORE (0-10) -----------------------------------------------------------------
    pts["spread"] = 2 if worst_spread <= 3 else 1 if worst_spread <= 6 else 0
    pts["open_interest"] = 2 if min_oi >= 1000 else 1 if min_oi >= 300 else 0
    if iv_rv_ex_gap is None:
        pts["iv_vs_rv"] = 0
    else:
        pts["iv_vs_rv"] = 2 if iv_rv_ex_gap <= 1.0 else 1 if iv_rv_ex_gap <= 1.2 else 0
    pts["payoff_at_target"] = 2 if ratio >= 1.0 else 1 if ratio >= 0.5 else 0
    theta = abs(_f(long_leg["theta"]) or 0.0) - (abs(_f(short_leg["theta"]) or 0.0) if short_leg else 0.0)
    theta_pct = 100 * theta / debit if debit > 0 else 99.0
    pts["theta_per_day"] = 2 if theta_pct <= 2.0 else 1 if theta_pct <= 3.5 else 0
    score = sum(pts.values())

    # --- 5. COMBINED GRADE: a great stock on a bad contract is not a trade ----------------
    if not u_eff:
        g = "C"
    elif score >= 8:
        g = "A+" if u_eff == "A+" else "A"
    elif score >= 6:
        g = "A"
    elif score >= 4:
        g = "B"
    else:
        g = "C"
    return {"tradeable": not fails and g in ("A+", "A"), "grade": g, "underlying": u or u_eff,
            "option_score": score, "points": pts, "fails": fails, "cost": cost, "max_loss": cost,
            "net_delta": round(delta, 3), "theta_pct_per_day": round(theta_pct, 2),
            "breakeven": round(breakeven, 2), "payoff_at_target": round(100 * payoff, 2),
            "payoff_ratio": round(ratio, 2), "worst_spread_pct": round(worst_spread, 2),
            "min_open_interest": min_oi}


def exit_check(*, entry_premium: float, mark: float, prior_close_mark: float | None,
               peak_premium: float, dte: int, entry_dte: int, side: str, underlying_px: float,
               setup_invalidation: float | None, thesis_broken: bool = False,
               runs_at_or_below_minus50: int = 0, thesis_recheck_failed: bool = False,
               earnings_next_session: bool = False, earnings_is_thesis: bool = False,
               placed_agent: str = "agentic", hedge: bool = False,
               manual_hold_override: bool = False) -> dict:
    """One exit pass on one open option position (premiums per share; a vertical passes its
    NET premium). Returns {'action': 'hold'|'alert'|'close'|'notify', 'reason', 'gain',
    'peak_premium'}. 'close' on a placed_agent 'user' position becomes 'notify' -- the ownership
    gate. The caller persists peak_premium and runs_at_or_below_minus50 in _current_state."""
    gain = mark / entry_premium - 1
    peak = max(peak_premium, mark)
    peak_gain = peak / entry_premium - 1

    def out(action: str, reason: str) -> dict:
        if action == "close" and placed_agent == "user":
            action, reason = "notify", f"{reason} -- Ryan's position: ask first"
        return {"action": action, "reason": reason, "gain": round(gain, 4),
                "peak_premium": round(peak, 4)}

    # 1. thesis / setup break -- the PRIMARY exit
    if thesis_broken:
        return out("close", "thesis broken (HARD RULE 7)")
    if setup_invalidation is not None and not hedge:
        broke = underlying_px <= setup_invalidation if side == "call" else underlying_px >= setup_invalidation
        if broke:
            return out("close", f"setup break: underlying {underlying_px} through {setup_invalidation}")
    # 2. expiry-window rules
    if dte <= FLAT_BY_DTE:
        return out("close", f"flat by DTE {FLAT_BY_DTE}")
    if earnings_next_session and not earnings_is_thesis:
        return out("close", "earnings before the next session -- close pre-print")
    # 3. winners
    if prior_close_mark and mark / prior_close_mark - 1 >= POP_BANK_1D:
        return out("close", f"pop-bank: +{mark / prior_close_mark - 1:.0%} in one day")
    if peak_gain >= RATCHET_ARM:
        floor = peak_gain * (1 - RATCHET_GIVEBACK)
        if gain <= floor:
            return out("close", f"ratchet: gain {gain:+.0%} <= floor {floor:+.0%} (peak {peak_gain:+.0%})")
    # 4. losers -- DTE-scaled backstops (hedge / manual override exempt)
    if not hedge and not manual_hold_override:
        if dte > 45:
            if gain <= -0.70:
                return out("close", "hard backstop -70% (>45 DTE)")
        elif dte >= 21:
            if gain <= -0.65:
                return out("close", "hard backstop -65% (21-45 DTE)")
            if gain <= -0.50 and runs_at_or_below_minus50 >= 2 and thesis_recheck_failed:
                return out("close", "-50% held 2 runs and thesis re-check failed")
        else:
            if gain <= -0.50 and runs_at_or_below_minus50 >= 2:
                return out("close", "-50% cut confirmed on re-check (<21 DTE)")
        if gain <= -0.50:
            return out("alert", f"{gain:+.0%}: re-check thesis; cut rules above apply next run")
    # 5. 21-DTE management review
    if entry_dte > REVIEW_DTE and dte <= REVIEW_DTE and not hedge:
        if gain <= 0:
            return out("close", f"21-DTE review: {gain:+.0%} -- flat/losing is closed, not held into theta")
        return out("alert", f"21-DTE review: {gain:+.0%} -- winner; ratchet + pop rules govern")
    return out("hold", f"working, {gain:+.0%}")


# ---------------------------------------------------------------------------
# self-tests -- fixtures are REAL quotes taken 2026-09-29 ~16:12Z
# ---------------------------------------------------------------------------
def _selftest() -> None:
    now = datetime(2026, 9, 29, 16, 13, tzinfo=timezone.utc)
    nvda_240c = {"role": "long", "strike": 240.0, "bid_price": "4.60", "ask_price": "4.80",
                 "delta": "0.353063", "theta": "-0.131693", "open_interest": 7327,
                 "updated_at": "2026-09-29T16:12:15.498108766Z"}
    nvda_250c = {"role": "short", "strike": 250.0, "bid_price": "2.07", "ask_price": "2.18",
                 "delta": "0.196801", "theta": "-0.094932", "open_interest": 8192,
                 "updated_at": "2026-09-29T16:12:25.690579983Z"}
    mrk_1525c = {"role": "long", "strike": 152.5, "bid_price": "3.85", "ask_price": "4.25",
                 "delta": "0.401712", "theta": "-0.098808", "open_interest": 5,
                 "updated_at": "2026-09-29T16:12:15.572181065Z"}
    b = bucket(3330.52, 0.0)
    assert b["bucket"] == 666.1 and b["remaining"] == 666.1

    # NVDA single leg: liquid, A+ name, $480 now fits (no per-trade cap)
    g = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c],
                       spot=230.275, target=255.0, dte=31, iv_rv_ex_gap=1.05,
                       binary_event_before_expiry=False, bucket_remaining=b["remaining"], now=now)
    assert g["cost"] == 480.0 and not any("bucket" in f for f in g["fails"]), g
    # the same trade with a target that barely clears the strike is the wrong vehicle
    g2 = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c],
                        spot=230.275, target=242.0, dte=31, iv_rv_ex_gap=1.05,
                        binary_event_before_expiry=False, bucket_remaining=666.1, now=now)
    assert not g2["tradeable"] and any("wrong vehicle" in f for f in g2["fails"])
    # vertical: net debit at the touch 4.80 - 2.07 = 2.73 -> $273, capped payoff
    v = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c, nvda_250c],
                       spot=230.275, target=250.0, dte=31, iv_rv_ex_gap=1.05,
                       binary_event_before_expiry=False, bucket_remaining=666.1, now=now)
    assert v["cost"] == 273.0 and v["payoff_at_target"] == 727.0, v
    # MRK: A+ stock, 5 contracts open -> a great name on an untradeable contract
    m = grade_contract(symbol="MRK", side="call", underlying_letter="A+", legs=[mrk_1525c],
                       spot=147.435, target=160.0, dte=31, iv_rv_ex_gap=1.0,
                       binary_event_before_expiry=False, bucket_remaining=666.1, now=now)
    assert not m["tradeable"] and any("open interest" in f for f in m["fails"])
    # B-grade underlying never passes, however good the contract
    bb = grade_contract(symbol="NVDA", side="call", underlying_letter="B", legs=[nvda_240c],
                        spot=230.275, target=255.0, dte=31, iv_rv_ex_gap=0.9,
                        binary_event_before_expiry=False, bucket_remaining=666.1, now=now)
    assert not bb["tradeable"] and bb["grade"] == "C"
    # stale quote fails: current info only
    late = datetime(2026, 9, 29, 16, 20, tzinfo=timezone.utc)
    s = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c],
                       spot=230.275, target=255.0, dte=31, iv_rv_ex_gap=1.05,
                       binary_event_before_expiry=False, bucket_remaining=666.1, now=late)
    assert any("re-quote" in f for f in s["fails"]) and not s["tradeable"]
    # own earnings before expiry fails
    e = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c],
                       spot=230.275, target=255.0, dte=31, iv_rv_ex_gap=1.05,
                       binary_event_before_expiry=True, bucket_remaining=666.1, now=now)
    assert not e["tradeable"]
    # cost above what's left of the bucket fails
    c = grade_contract(symbol="NVDA", side="call", underlying_letter="A+", legs=[nvda_240c],
                       spot=230.275, target=255.0, dte=31, iv_rv_ex_gap=1.05,
                       binary_event_before_expiry=False, bucket_remaining=400.0, now=now)
    assert any("bucket remaining" in f for f in c["fails"])

    # exit engine
    base = dict(entry_premium=4.8, peak_premium=4.8, dte=30, entry_dte=31, side="call",
                underlying_px=231.0, setup_invalidation=222.0, prior_close_mark=4.8)
    assert exit_check(mark=4.9, **base)["action"] == "hold"
    assert exit_check(mark=4.0, **{**base, "underlying_px": 221.5})["action"] == "close"
    assert exit_check(mark=1.6, **base)["action"] == "close"                    # -67% backstop
    assert exit_check(mark=2.3, **base)["action"] == "alert"                    # -52%: re-check
    assert exit_check(mark=2.3, runs_at_or_below_minus50=2, thesis_recheck_failed=True,
                      **base)["action"] == "close"
    assert exit_check(mark=9.0, **base)["action"] == "close"                    # +88% in a day: pop
    pk = {**base, "peak_premium": 9.6, "prior_close_mark": 8.0}                 # peak +100%
    assert exit_check(mark=7.5, **pk)["action"] == "close"                      # +56% <= floor +60%
    assert exit_check(mark=8.5, **pk)["action"] == "hold"
    assert exit_check(mark=4.5, **{**base, "dte": 21})["action"] == "close"     # 21-DTE, losing
    assert exit_check(mark=4.0, **{**base, "underlying_px": 221.0},
                      placed_agent="user")["action"] == "notify"               # ownership gate
    assert exit_check(mark=1.0, hedge=True, **{**base, "setup_invalidation": None})["action"] == "hold"
    assert exit_check(mark=4.9, earnings_next_session=True, **base)["action"] == "close"
    print("options_grade selftest OK")


if __name__ == "__main__":
    _selftest()
