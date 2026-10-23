"""Tests for wash_sale.py (joint-account wash-sale watch)."""
import wash_sale as ws

TODAY = "2026-10-23"
TRADES = [
    {"timestamp": "2026-10-22T23:58:13Z", "symbol": "AMZN", "side": "sell", "realized_gain": "-40.38"},
    {"timestamp": "2026-10-22T13:33:47Z", "symbol": "META", "side": "sell", "realized_gain": "-1287.61"},
    {"timestamp": "2026-10-16T19:08:18Z", "symbol": "META", "side": "sell", "realized_gain": "-444.35"},
    {"timestamp": "2026-10-22T23:57:02Z", "symbol": "RBRK", "side": "sell", "realized_gain": "1388.47"},
    {"timestamp": "2026-10-07T14:16:49Z", "symbol": "ADBE", "side": "sell", "realized_gain": "-0.16"},
    {"timestamp": "2026-09-22T10:00:00Z", "symbol": "OLD", "side": "sell", "realized_gain": "-500"},
    {"timestamp": "2026-09-23T10:00:00Z", "symbol": "EDGE", "side": "sell", "realized_gain": "-50"},
    {"timestamp": "2026-10-10T10:00:00Z", "symbol": "MU 1160C", "side": "sell", "realized_gain": "-900"},
]


def test_lockouts_sums_losses_and_dates():
    lk = ws.lockouts(TRADES, TODAY)
    assert set(lk) == {"AMZN", "META", "EDGE"}          # gain, tiny loss, expired, option skipped
    assert lk["META"]["loss_usd"] == -1731.96 and lk["META"]["sales"] == 2
    assert lk["META"]["last_loss_sale"] == "2026-10-22" and lk["META"]["clear"] == "2026-11-22"
    assert lk["EDGE"]["clear"] == "2026-10-24"           # 30 days back is still open today
    assert list(lk)[0] == "EDGE"                          # soonest clear first


def test_buys_in_window_any_account_and_ira():
    lk = ws.lockouts(TRADES, TODAY)
    orders = [
        {"symbol": "AMZN", "side": "buy", "cumulative_quantity": "15", "last_transaction_at": "2026-10-23T15:55:00Z", "account_number": "116713985343", "placed_agent": "user"},
        {"symbol": "META", "side": "buy", "cumulative_quantity": "1", "last_transaction_at": "2026-10-01T15:00:00Z", "account_number": "661726109", "placed_agent": "user"},
        {"symbol": "META", "side": "buy", "cumulative_quantity": "1", "last_transaction_at": "2026-08-01T15:00:00Z", "account_number": "116713985343"},
        {"symbol": "RBRK", "side": "buy", "cumulative_quantity": "1", "last_transaction_at": "2026-10-23T15:00:00Z", "account_number": "116713985343"},
    ]
    hits = ws.buys_in_window(lk, orders, TRADES, {"661726109": "ira_roth"})
    assert [(h["symbol"], h["account"]) for h in hits] == [("AMZN", "116713985343"), ("META", "661726109")]
    amzn, meta = hits
    assert amzn["after_sale"] and not amzn["permanent"]
    assert meta["permanent"] and not meta["after_sale"]   # buy before the sale also washes
    assert amzn["shares"] == 15 and not amzn["managed"]
    robo = ws.buys_in_window(lk, [{"symbol": "META", "side": "buy", "cumulative_quantity": "0.05",
                                   "last_transaction_at": "2026-10-19T15:00:00Z", "account_number": "181054271778",
                                   "placed_agent": "advisory"}], TRADES)
    assert robo[0]["managed"] and robo[0]["after_sale"]
    assert "META 0.05 sh (...1778)" in ws.report(lk, robo, {}, {}, TODAY)


def test_sell_traps_recent_buys_on_held_names():
    pos = [{"symbol": "META", "quantity": "30"}, {"symbol": "NOW", "quantity": "46"}, {"symbol": "EPIX^", "quantity": "25"}]
    orders = [
        {"symbol": "META", "side": "buy", "cumulative_quantity": "5", "last_transaction_at": "2026-10-22T15:15:00Z"},
        {"symbol": "NOW", "side": "buy", "cumulative_quantity": "5", "last_transaction_at": "2026-08-05T15:15:00Z"},
    ]
    assert ws.sell_traps(pos, orders, TODAY) == {"META": "2026-11-22"}


def test_events_and_report():
    prev = {"PATH": {"clear": "2026-10-23"}, "META": {"clear": "2026-11-16"}}
    now = ws.lockouts(TRADES, TODAY)
    ev = ws.events(prev, now)
    assert ev == {"locked": ["AMZN", "EDGE"], "cleared": ["PATH"], "extended": ["META"]}
    txt = ws.report(now, [], {"META": "2026-11-22"}, ev, TODAY)
    assert "Cleared, safe to buy again:** PATH" in txt and "| 2026-11-22 | META | $1,732 | 2 |" in txt
    assert ws.watchlist_symbols({"lockouts": now}) == ["EDGE", "AMZN", "META"]
