"""Tests for watchlists.py (agent-managed Robinhood watchlists)."""
import watchlists as w


def test_joint_holdings_skips_stubs_and_zero():
    pos = [{"symbol": "META", "quantity": "13"}, {"symbol": "EPIX^", "quantity": "25"},
           {"symbol": "AMZN", "quantity": "0"}, {"symbol": "GOOGL", "quantity": "1.5"}]
    assert w.joint_holdings(pos) == ["GOOGL", "META"]


def test_buy_zone_is_managed_alerts_in_rank_order():
    q = {"candidates": ["SKHY", "AVGO", "B", "MCO"], "managed_alerts": {"MCO": {}, "SKHY": {}, "B": {}}}
    assert w.buy_zone(q) == ["SKHY", "B", "MCO"]


def test_rebuy_drops_closed():
    r = {"names": {"CRCL": {"stage": "CLOSED (bought back)"}, "WULF": {"stage": "TURNING"}}}
    assert w.rebuy(r) == ["WULF"]


def test_sleeves_vehicle_then_picks_no_dupes():
    s = {"vehicle": {"QQQ": "QLD"}, "picks": [{"symbol": "MU"}, {"symbol": "QQQ"}, {"symbol": "AMD"}]}
    assert w.sleeves(s) == ["QQQ", "QLD", "MU", "AMD"]


def test_diff_and_batches():
    add, rm = w.diff(["A", "B", "C"], ["C", "D", "A"])
    assert add == ["D"] and rm == ["B"]
    assert [len(b) for b in w.batches(list("x" * 85))] == [40, 40, 5]


def test_theme_symbols_dedupes():
    st = {"themes": {"a": {"symbols": ["RCAT", "KTOS"]}, "b": {"symbols": ["KTOS", "FCX"]}}}
    assert w.theme_symbols(st) == ["RCAT", "KTOS", "FCX"]
