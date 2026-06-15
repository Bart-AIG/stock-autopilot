"""Robinhood execution layer (robin_stocks). DRY-RUN by default.

Mirrors exactly what the human session does: market sells to exit, cancel+replace
a resting GTC stop for a trail, dollar-based market buys, then a GTC stop_market on
the WHOLE-SHARE portion of each fill (the fractional remainder stays monitored).

!! VERIFY before trusting with real money !!
  - robin_stocks is an UNOFFICIAL library; function signatures vary by version. The
    calls below target a recent robin_stocks. Validate each on a tiny live order (or
    the smallest possible size) before raising the caps.
  - Live trading requires AUTOTRADE_LIVE=1 plus RH_USERNAME / RH_PASSWORD /
    RH_TOTP_SECRET in the environment (GitHub Actions secrets). Without all of those
    this class stays in dry-run and only logs what it WOULD do.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass, field


def live_enabled() -> bool:
    creds = all(os.environ.get(k) for k in ("RH_USERNAME", "RH_PASSWORD", "RH_TOTP_SECRET"))
    return os.environ.get("AUTOTRADE_LIVE", "0") == "1" and creds


@dataclass
class Snapshot:
    account_value: float
    buying_power: float
    day_pnl: float
    positions: dict[str, dict] = field(default_factory=dict)  # sym -> {shares, available}
    quotes: dict[str, float] = field(default_factory=dict)


class RobinhoodExecutor:
    def __init__(self, dry_run: bool | None = None):
        # Default: live only when explicitly enabled AND creds present.
        self.dry_run = (not live_enabled()) if dry_run is None else dry_run
        self.rh = None
        self.log: list[str] = []

    # --- session ---------------------------------------------------------
    def login(self) -> None:
        if self.dry_run:
            self._note("DRY-RUN: skipping Robinhood login")
            return
        import pyotp
        import robin_stocks.robinhood as rh
        totp = pyotp.TOTP(os.environ["RH_TOTP_SECRET"]).now()
        rh.login(os.environ["RH_USERNAME"], os.environ["RH_PASSWORD"], mfa_code=totp)
        self.rh = rh
        self._note("logged in to Robinhood")

    # --- read state ------------------------------------------------------
    def snapshot(self, symbols: list[str]) -> Snapshot:
        """Account value, buying power, day P&L, positions, and quotes for `symbols`.
        In dry-run, returns a configurable placeholder account so sizing still runs."""
        if self.dry_run:
            av = float(os.environ.get("AT_DRYRUN_ACCOUNT_VALUE", "3000"))
            bp = float(os.environ.get("AT_DRYRUN_BUYING_POWER", "800"))
            return Snapshot(account_value=av, buying_power=bp, day_pnl=0.0,
                            positions={}, quotes={s: 0.0 for s in symbols})
        rh = self.rh
        port = rh.profiles.load_portfolio_profile()
        acct = rh.profiles.load_account_profile()
        equity = float(port.get("equity") or 0)
        prev = float(port.get("equity_previous_close") or equity)
        cash = float(acct.get("portfolio_cash") or acct.get("cash") or 0)
        buying_power = float(acct.get("buying_power") or 0)
        positions = {}
        for p in rh.account.get_open_stock_positions():
            sym = rh.stocks.get_symbol_by_url(p["instrument"])
            qty = float(p.get("quantity") or 0)
            held = float(p.get("shares_held_for_sells") or 0)
            if qty > 0:
                positions[sym] = {"shares": qty, "available": qty - held}
        quotes = {}
        for s in symbols:
            try:
                quotes[s] = float(rh.stocks.get_latest_price(s)[0])
            except Exception:  # noqa: BLE001
                quotes[s] = 0.0
        return Snapshot(account_value=equity + cash, buying_power=buying_power,
                        day_pnl=equity - prev, positions=positions, quotes=quotes)

    # --- write orders ----------------------------------------------------
    def execute(self, order: dict) -> dict:
        """Place one order. Returns a result record (also appended to self.log)."""
        kind = order["kind"]
        if kind == "sell":
            return self._sell_all(order)
        if kind == "trail":
            return self._trail(order)
        if kind == "buy":
            return self._buy(order)
        return {"ok": False, "why": f"unknown kind {kind}"}

    def _sell_all(self, o: dict) -> dict:
        sym, qty = o["symbol"], o.get("available")
        if self.dry_run:
            return self._dry(f"SELL {sym} qty={qty} (market) + cancel any resting stop")
        self._cancel_open_sells(sym)  # free shares held by a resting stop
        res = self.rh.orders.order_sell_market(sym, qty, timeInForce="gfd")
        return self._done(f"SELL {sym} {qty}", res)

    def _trail(self, o: dict) -> dict:
        sym, new_stop = o["symbol"], o["new_stop"]
        if self.dry_run:
            return self._dry(f"TRAIL {sym}: cancel old stop, place GTC stop_market @ {new_stop} on whole shares")
        self._cancel_open_sells(sym)
        whole = self._whole_shares(sym)
        if whole < 1:
            return self._done(f"TRAIL {sym}: <1 whole share — monitored only", None)
        res = self.rh.orders.order_sell_stop_loss(sym, whole, new_stop, timeInForce="gtc")
        return self._done(f"TRAIL {sym} {whole}@{new_stop}", res)

    def _buy(self, o: dict) -> dict:
        sym, usd, stop = o["symbol"], o["dollar_amount"], o.get("stop")
        if self.dry_run:
            return self._dry(f"BUY {sym} ${usd} (market) then GTC stop_market @ {stop} on whole-share portion")
        buy = self.rh.orders.order_buy_fractional_by_price(sym, usd, timeInForce="gfd")
        # Confirm the fill before stopping; round filled qty DOWN to whole shares.
        whole = self._whole_shares(sym)
        stop_res = None
        if stop and whole >= 1:
            stop_res = self.rh.orders.order_sell_stop_loss(sym, whole, stop, timeInForce="gtc")
        return self._done(f"BUY {sym} ${usd}; stop {whole}@{stop}", {"buy": buy, "stop": stop_res})

    # --- helpers ---------------------------------------------------------
    def _whole_shares(self, sym: str) -> int:
        for p in self.rh.account.get_open_stock_positions():
            if self.rh.stocks.get_symbol_by_url(p["instrument"]) == sym:
                return int(math.floor(float(p.get("shares_available_for_sells") or p.get("quantity") or 0)))
        return 0

    def _cancel_open_sells(self, sym: str) -> None:
        for od in self.rh.orders.get_all_open_stock_orders():
            try:
                if od.get("side") == "sell" and self.rh.stocks.get_symbol_by_url(od["instrument"]) == sym:
                    self.rh.orders.cancel_stock_order(od["id"])
            except Exception:  # noqa: BLE001
                pass

    def _note(self, m: str) -> None:
        self.log.append(m)

    def _dry(self, m: str) -> dict:
        self._note("DRY-RUN: " + m)
        return {"ok": True, "dry_run": True, "action": m}

    def _done(self, m: str, res) -> dict:
        self._note("PLACED: " + m)
        return {"ok": True, "dry_run": False, "action": m, "result": res}
