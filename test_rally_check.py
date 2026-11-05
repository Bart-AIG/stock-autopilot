"""Tests for rally_check.py (fragile-rally flag for SPY / QQQ)."""
from datetime import date, timedelta

import rally_check as rc


def _bars(closes, vols, start=date(2025, 1, 1)):
    return [{"date": str(start + timedelta(days=i)), "close": c, "volume": v}
            for i, (c, v) in enumerate(zip(closes, vols))]


def _series(rally=0.06, vol_late=1.0, n=260):
    """Flat at 100 for n-20 bars, then a linear rally into a new high over the last 20."""
    closes = [100.0] * (n - 20) + [100 * (1 + rally * (i + 1) / 20) for i in range(20)]
    vols = [1_000_000.0] * (n - 20) + [1_000_000.0 * vol_late] * 20
    return closes, vols


def _ew(closes_like, ew_rally, n=260):
    return [100.0] * (n - 20) + [100 * (1 + ew_rally * (i + 1) / 20) for i in range(20)]


def test_fragile_when_light_volume_and_narrow():
    c, v = _series(rally=0.06, vol_late=0.7)
    r = rc.check(_bars(c, v), _bars(_ew(c, 0.02), v))
    assert r["state"] == "FRAGILE"
    assert r["gain_20d_pct"] == 6.0 and r["volume_ratio"] == 0.7
    assert r["vs_equal_weight_pts"] == 4.0


def test_thin_narrow_healthy():
    c, v = _series(rally=0.06, vol_late=0.7)
    assert rc.check(_bars(c, v), _bars(_ew(c, 0.06), v))["state"] == "THIN"
    c, v = _series(rally=0.06, vol_late=1.2)
    assert rc.check(_bars(c, v), _bars(_ew(c, 0.02), v))["state"] == "NARROW"
    assert rc.check(_bars(c, v), _bars(_ew(c, 0.06), v))["state"] == "HEALTHY"


def test_no_rally_when_small_gain_or_far_from_high():
    c, v = _series(rally=0.02, vol_late=0.7)
    assert rc.check(_bars(c, v), _bars(_ew(c, 0.0), v))["state"] == "NO RALLY"
    c, v = _series(rally=0.06, vol_late=0.7)
    c[100] = 200.0                       # an old high far above today
    assert rc.check(_bars(c, v), _bars(_ew(c, 0.0), v))["state"] == "NO RALLY"


def test_no_data_and_missing_equal_weight():
    c, v = _series()
    assert rc.check(_bars(c[:100], v[:100]), _bars(c, v))["state"] == "NO DATA"
    other = _bars(c, v, start=date(2020, 1, 1))   # dates never line up
    r = rc.check(_bars(c, v), other)
    assert r["vs_equal_weight_pts"] is None and r["state"] in ("THIN", "HEALTHY")


def test_summary_flag_and_since():
    fr = {"QQQ": {"state": "FRAGILE", "date": "2026-09-22"}, "SPY": {"state": "NO RALLY", "date": "2026-09-22"}}
    s = rc.summary(fr, prior={"flag": "FRAGILE", "since": "2026-09-21"})
    assert s["flag"] == "FRAGILE" and s["since"] == "2026-09-21"
    s = rc.summary({"SPY": {"state": "THIN", "date": "2026-10-20"}}, prior=s)
    assert s["flag"] == "WATCH" and s["since"] == "2026-10-20"
    assert rc.summary({"SPY": {"state": "HEALTHY", "date": "2026-10-21"}})["flag"] == "OK"
