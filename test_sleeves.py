"""Checks that sleeves.py makes the same in/out decisions as the backtested rules
(robust_backtest.swing) on synthetic prices laid on the real exchange calendar.
Run: python test_sleeves.py"""

import random
from datetime import date, timedelta

import robust_backtest as rb
import sleeves as sl


def series(seed):
    random.seed(seed)
    d, days = date(2025, 6, 2), []
    while d <= date(2026, 9, 30):
        if sl.is_session(d):
            days.append(d.isoformat())
        d += timedelta(days=1)
    C, H, L, p = [], [], [], 100.0
    for _ in days:
        p *= 1 + random.gauss(0.0006, 0.018) or 1e-6
        C.append(p)
        H.append(p * (1 + abs(random.gauss(0, 0.008))))
        L.append(p * (1 - abs(random.gauss(0, 0.008))))
    return days, C, H, L


def main():
    rb.FEE = 0.0
    checked = mismatches = 0
    for seed in range(40):
        days, C, H, L = series(seed)
        ret = rb.swing(days, C, H, L, None, lev=1, cash={})
        # backtest membership on day i+1 = decision taken at the close of day i
        legs = sl.fresh_legs()
        for i in range(201, len(days) - 1):
            legs, _ = sl.step(legs, C[:i], C[i], H[i], L[i], sl.is_tom(days[i + 1]))
            if days[i + 1][:7] == days[-1][:7]:
                continue            # the backtest's own TOM grouping is incomplete for the last month
            held_bt = ret[days[i + 1]] != 0.0
            checked += 1
            mismatches += held_bt != sl.is_in(legs)
        # replay() == step-by-step state
        assert sl.replay(days[:-1], C[:-1], H[:-1], L[:-1]) == legs
    print(f"checked {checked} decisions, {mismatches} mismatches")
    assert mismatches == 0
    assert sl.is_tom("2026-09-30") and sl.is_tom("2026-10-01") and sl.is_tom("2026-10-05")
    assert not sl.is_tom("2026-10-06") and not sl.is_tom("2026-09-29")
    assert sl.next_session(date(2026, 11, 25)) == date(2026, 11, 27)
    print("ok")


if __name__ == "__main__":
    main()
