"""Tests for setups.py (chart-setup score, set 2026-10-14). No network.
Run: python test_setups.py"""
import math

import setups


def rows(closes, vols=None):
    """Oldest-first closes -> FMP-style rows, newest first."""
    vols = vols or [1e6] * len(closes)
    return [{"price": c, "volume": v} for c, v in zip(closes, vols)][::-1]


def uptrend(n=80, start=50.0):
    return [start * (1 + 0.004 * i) + math.sin(i / 2) * 0.4 for i in range(n)]


def wedge(n=90, top=100.0, breakout=False):
    """Zig-zag between two falling, converging lines: upper 100 -> 82, lower 90 -> 78."""
    out = []
    for i in range(n):
        u = top - 18 * i / n
        lw = top * 0.9 - 12 * i / n
        frac = (math.sin(i * 2 * math.pi / 15) + 1) / 2     # 15-session swings
        out.append(lw + (u - lw) * (0.05 + 0.9 * frac))
    if breakout:
        out[-2] = top - 18 * (n - 2) / n - 1               # just under the line
        out[-1] = top - 18 * (n - 1) / n + 2.5             # closes above it
    return out


def test_falling_wedge_found_and_breakout():
    base = uptrend(60, 80.0)
    xs = base + wedge(90)
    w = setups.falling_wedge(xs, xs, xs, [1e6] * len(xs))
    assert w and w["pattern"] == "falling wedge", w
    assert w["age"] is None
    xs_b = base + wedge(90, breakout=True)
    vols = [1e6] * (len(xs_b) - 1) + [3e6]
    s = setups.score(rows(xs_b, vols))
    assert s["pattern"]["name"] == "falling wedge", s
    assert s["pattern"]["state"] == "fresh_breakout", s
    assert any("on volume" in w for w in s["why"]), s
    assert s["score"] >= setups.score(rows(base + wedge(90)))["score"]


def test_double_bottom():
    xs = uptrend(80, 90.0)
    xs += [110 - i for i in range(15)]          # fall to 96
    xs += [96.8 + i * 0.8 for i in range(10)]   # bounce to 104
    xs += [103.2 - i * 0.75 for i in range(10)]  # back down to ~96.45
    xs += [97.0 + i * 0.5 for i in range(6)]    # turning up
    d = setups.double_bottom(xs, xs, xs)
    assert d and d["pattern"] == "double bottom", d
    assert abs(d["trigger"] - max(xs[95:106])) < 1e-9


def test_ohlc_rows():
    """Full OHLC rows: highs/lows feed the trendlines, the close decides breakouts."""
    base = uptrend(60, 80.0)
    xs = base + wedge(90)
    full = [{"close": c, "high": c * 1.01, "low": c * 0.99, "volume": 1e6} for c in xs][::-1]
    C, H, L, V = setups._chrono(full)
    assert H[-1] == xs[-1] * 1.01 and L[-1] == xs[-1] * 0.99 and C[-1] == xs[-1]
    w = setups.falling_wedge(C, H, L, V)
    assert w and w["pattern"] == "falling wedge", w
    s = setups.score(full)
    assert s and "flags" in s and s["pattern"]["name"] == "falling wedge", s


def test_falling_knife_penalized():
    xs = [200 - i * 0.6 for i in range(160)]   # steady decline, new lows every day
    s = setups.score(rows(xs))
    assert "PENALTY: fresh 60-day low" in s["why"]
    assert s["label"] == "WEAK", s


def test_short_history_is_none():
    assert setups.score(rows(uptrend(100))) is None


def test_live_state():
    s = {"pattern": {"name": "falling wedge", "state": "near", "trigger": 50.0, "support": 45.0}}
    assert setups.live_state(s, 50.5) == "BREAKING OUT NOW"
    assert setups.live_state(s, 44.0) == "BROKE SUPPORT"
    assert setups.live_state(s, 48.0) is None
    assert setups.live_state(None, 48.0) is None


def test_labels():
    assert setups.label_for(75) == "STRONG"
    assert setups.label_for(40) == "CONSTRUCTIVE"
    assert setups.label_for(20) == "NEUTRAL"
    assert setups.label_for(0) == "WEAK"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
