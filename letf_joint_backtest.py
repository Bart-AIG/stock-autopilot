"""Joint-account leveraged-ETF research (run 2026-11-26, Ryan's request: day/swing trade daily
leveraged ETFs in the joint account, trades placed by hand, "maybe we trade on daily rsi or
moving averages ... or weekly").

What it tests: hand-executable rules (one decision a day at most, most of them weekly or
monthly), each signal computed on the UNDERLYING index ETF and held in a 2x or 3x daily fund.
Synthetic funds are built from the underlying's total return, the 3-month T-bill (FRED DTB3)
plus a financing spread, and the expense ratio; the spread is calibrated on the real funds.

Taxes: the joint account is taxable. Each run is also scored after tax with FIFO lots, a
30-day wash-sale deferral on re-entry after a loss sale, annual netting, loss carryforward,
T-bill interest taxed as ordinary income, and liquidation at the end.

Read-only research. Touches no ledger, report or account. Data: data/letf/ (letf_fetch.py).
Output: letf_joint_results.md.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

D = Path("data/letf")
COST_BPS = 5.0            # per side: spread + slippage on a hand-placed market order (measured 1-5 bp round trip)
ER = {1: 0.0, 2: 0.0095, 3: 0.0085}  # QLD 0.95%, TQQQ 0.82% / UPRO 0.89% / SOXL 0.75%
TAX_ST, TAX_LT = 0.32, 0.15  # assumption, Texas has no state income tax
START_EQUITY = 25_000.0


# ----------------------------------------------------------------------------- data
def load(sym: str) -> pd.DataFrame:
    df = pd.read_csv(D / f"{sym.replace('^', 'IDX_')}.csv", parse_dates=["date"]).set_index("date").sort_index()
    df = df[(df["close"] > 0)].copy()
    df = df[~df.index.duplicated(keep="last")]
    f = (df["adj"] / df["close"]).fillna(1.0)
    out = pd.DataFrame({"o": df["open"].fillna(df["close"]) * f, "c": df["adj"].fillna(df["close"])})
    # bad open prints: an open more than 25% from both closes around it is replaced by the prior close
    prev = out["c"].shift(1)
    bad = ((out["o"] / prev - 1).abs() > 0.25) & ((out["o"] / out["c"] - 1).abs() > 0.25)
    out.loc[bad, "o"] = prev[bad]
    return out


def tbill(index: pd.DatetimeIndex) -> pd.Series:
    p = D / "DTB3.csv"
    t = pd.read_csv(p)
    t.columns = ["date", "rate"]
    t["date"] = pd.to_datetime(t["date"])
    t["rate"] = pd.to_numeric(t["rate"], errors="coerce")
    s = t.set_index("date")["rate"].dropna() / 100.0
    return s.reindex(index.union(s.index)).ffill().reindex(index).fillna(0.02)


# ----------------------------------------------------------------------------- indicators
def rsi(c: pd.Series, n: int) -> pd.Series:
    d = c.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = up / dn.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).fillna(100)


def period_end(idx: pd.DatetimeIndex, freq: str) -> pd.Series:
    """True on the last trading day of each week ('W') or month ('M')."""
    key = idx.to_period("W-FRI" if freq == "W" else "M")
    s = pd.Series(key, index=idx)
    return s != s.shift(-1)


# ----------------------------------------------------------------------------- rules
# Each rule returns target exposure (multiple of the underlying, 0..L) decided at the close of
# each day, using only data up to that close, plus a mask of the days a decision is allowed.
def rules(u: pd.DataFrame, L: int) -> dict[str, tuple[pd.Series, pd.Series]]:
    c = u["c"]
    idx = c.index
    every = pd.Series(True, index=idx)
    s200, s50, s5 = c.rolling(200).mean(), c.rolling(50).mean(), c.rolling(5).mean()
    up = c > s200
    out: dict[str, tuple[pd.Series, pd.Series]] = {}

    out["buy_hold"] = (pd.Series(float(L), index=idx), every)
    out["sma200_daily"] = (up.astype(float) * L, every)

    # 200-day with a 2% band: in above +2%, out below -2%, otherwise keep
    st, cur = [], 0.0
    for px, m in zip(c.values, s200.values):
        if not np.isnan(m):
            if px > m * 1.02:
                cur = 1.0
            elif px < m * 0.98:
                cur = 0.0
        st.append(cur)
    out["sma200_band2"] = (pd.Series(st, index=idx) * L, every)

    # weekly: Friday close vs the 40-week average of Friday closes
    we = period_end(idx, "W")
    wc = c[we]
    w40 = (wc > wc.rolling(40).mean()).astype(float)
    out["weekly_40wk"] = (w40.reindex(idx).ffill().fillna(0) * L, we)

    # weekly RSI(14) above 50
    wr = (rsi(wc, 14) > 50).astype(float)
    out["weekly_rsi50"] = (wr.reindex(idx).ffill().fillna(0) * L, we)

    # monthly: month-end close vs the 10-month average (Faber 2007)
    me = period_end(idx, "M")
    mc = c[me]
    m10 = (mc > mc.rolling(10).mean()).astype(float)
    out["monthly_10mo"] = (m10.reindex(idx).ffill().fillna(0) * L, me)

    out["golden_cross"] = ((s50 > s200).astype(float) * L, every)

    # Connors RSI(2) dip inside an uptrend, out on a close above the 5-day (the house SWING_Q leg)
    r2 = rsi(c, 2)
    st, on = [], False
    for px, a, b5, rr, m in zip(c.values, up.values, s5.values, r2.values, s200.values):
        if np.isnan(m):
            on = False
        elif on:
            on = not (px > b5)
        else:
            on = bool(rr < 10 and a)
        st.append(1.0 if on else 0.0)
    dip = pd.Series(st, index=idx)
    out["rsi2_dip"] = (dip * L, every)

    # trend + volatility target: above the 200-day, exposure = min(L, 50% / 20-day realised vol);
    # decided weekly, traded only when it moves by 0.5x or more (handled in the simulator)
    vol = np.log(c).diff().rolling(20).std() * math.sqrt(252)
    vt = (0.50 / vol).clip(upper=L).where(up, 0.0).fillna(0.0)
    out["sma200_voltarget"] = (vt, we)

    band = out["sma200_band2"][0] / L       # the 2%-band trend state, 0 or 1
    for tgt in (0.40, 0.50, 0.60):
        v = (tgt / vol).clip(upper=L).fillna(0.0)
        out[f"band2_vol{int(tgt*100)}"] = ((v * band).fillna(0.0), every)

    # THE RECOMMENDED RULE: the 2%-band trend state checked every day (exits are daily), the size
    # min(L, 50% / 20-day realised vol) set on the last trading day of each week
    v_week = (0.50 / vol).clip(upper=L).where(we).ffill().fillna(0.0)
    out["recommended"] = ((v_week * band).fillna(0.0), every)

    # hybrid: 2x while above the 200-day, 3x while an RSI(2) dip is open, 0 below
    if L == 3:
        out["sma200_2x_rsi2_3x"] = ((up.astype(float) * 2 + dip).clip(upper=3), every)
    return out


# ----------------------------------------------------------------------------- simulator
@dataclass
class Lot:
    shares: float
    basis: float      # total $ basis
    start: pd.Timestamp


@dataclass
class TaxBook:
    lots: list = field(default_factory=list)
    st: float = 0.0
    lt: float = 0.0
    carry: float = 0.0          # capital loss carryforward (positive number = loss)
    deferred: float = 0.0       # wash-sale loss waiting for a re-entry
    deferred_until: pd.Timestamp | None = None
    deferred_start: pd.Timestamp | None = None
    paid: float = 0.0

    def buy(self, shares: float, cost: float, d: pd.Timestamp):
        start = d
        if self.deferred and self.deferred_until is not None and d <= self.deferred_until:
            cost += self.deferred          # disallowed loss moves into the new basis
            start = self.deferred_start or d
            self.deferred = 0.0
        self.lots.append(Lot(shares, cost, start))

    def sell(self, shares: float, proceeds: float, d: pd.Timestamp):
        px = proceeds / shares if shares else 0.0
        left = shares
        while left > 1e-12 and self.lots:
            lot = self.lots[0]
            take = min(left, lot.shares)
            frac = take / lot.shares
            basis = lot.basis * frac
            gain = take * px - basis
            longterm = (d - lot.start).days > 365
            if gain < 0:
                # wash sale if bought back within 30 days (checked on the next buy)
                self.deferred += -gain
                self.deferred_until = d + pd.Timedelta(days=30)
                self.deferred_start = lot.start
            else:
                if longterm:
                    self.lt += gain
                else:
                    self.st += gain
            lot.shares -= take
            lot.basis -= basis
            left -= take
            if lot.shares <= 1e-12:
                self.lots.pop(0)

    def expire_deferred(self, d: pd.Timestamp):
        """A loss not followed by a re-entry inside 30 days is allowed: book it."""
        if self.deferred and self.deferred_until is not None and d > self.deferred_until:
            longterm = self.deferred_start is not None and (self.deferred_until - pd.Timedelta(days=30) - self.deferred_start).days > 365
            if longterm:
                self.lt -= self.deferred
            else:
                self.st -= self.deferred
            self.deferred = 0.0

    def year_end(self, interest: float) -> float:
        st, lt = self.st, self.lt
        # carryforward offsets ST first, then LT
        c = self.carry
        use = min(c, max(st, 0)); st -= use; c -= use
        use = min(c, max(lt, 0)); lt -= use; c -= use
        if st < 0 and lt > 0:
            o = min(-st, lt); st += o; lt -= o
        if lt < 0 and st > 0:
            o = min(-lt, st); lt += o; st -= o
        loss = -min(st, 0) - min(lt, 0)
        self.carry = c + loss
        tax = max(st, 0) * TAX_ST + max(lt, 0) * TAX_LT + max(interest, 0) * TAX_ST
        self.st = self.lt = 0.0
        self.paid += tax
        return tax


def synth(u: pd.DataFrame, rf: pd.Series, L: int, spread: float) -> pd.DataFrame:
    """Daily-reset L-times fund from the underlying's total return. Close-to-close return
    L*r - financing; close-to-open L*r_overnight (the reset happens at the close)."""
    c, o = u["c"], u["o"]
    r_cc = c / c.shift(1) - 1
    r_co = o / c.shift(1) - 1
    fin = ((L - 1) * (rf + spread) + ER[L]) / 252
    R_cc = (L * r_cc - fin).clip(lower=-0.999)
    R_co = (L * r_co).clip(lower=-0.999)
    R_oc = (1 + R_cc) / (1 + R_co) - 1
    return pd.DataFrame({"cc": R_cc, "co": R_co, "oc": R_oc}).fillna(0.0)


def simulate(u, rf, L, spread, expo, allowed, execution="close", rebalance_band=0.5, taxed=True, start=None, end=None):
    """Track fund $ and cash $. A decision taken at the close of day t is executed at that close
    ('close') or at the next open ('open'). Returns a dict of daily equity and stats."""
    f = synth(u, rf, L, spread)
    idx = u.index
    sel = (idx >= (start or idx[0])) & (idx <= (end or idx[-1]))
    days = idx[sel]
    target_w = (expo / L).clip(0, 1)
    fund, cash = 0.0, START_EQUITY
    price = 100.0                       # synthetic fund price, for lot accounting
    book = TaxBook()
    interest_year = 0.0
    eq = []
    trades = 0
    in_mkt = 0
    pending = None                      # weight to execute at the next open
    cur_w_target = 0.0
    year = days[0].year
    pos_days = 0
    cost = COST_BPS / 1e4
    for i, d in enumerate(days):
        R = f.loc[d]
        r_cash = rf.loc[d] / 252
        # overnight segment (close of yesterday -> open)
        if i > 0:
            fund *= 1 + R["co"]
            p_open = price * (1 + R["co"])
        else:
            p_open = price
        if pending is not None and i > 0:
            fund, cash, n = _trade(fund, cash, pending, cost, book, p_open, d)
            trades += n
            pending = None
        # session segment
        if i > 0:
            fund *= 1 + R["oc"]
            price = p_open * (1 + R["oc"])
            interest = cash * r_cash
            cash += interest
            interest_year += interest
        # decision at today's close
        if allowed.loc[d]:
            w = float(target_w.loc[d])
            tot = fund + cash
            cur = fund / tot if tot > 0 else 0.0
            if (w == 0) != (cur < 1e-6):
                need = True                      # an entry or a full exit always trades
            elif 0.001 < w < 0.999 or 0.001 < cur < 0.999:
                need = abs(w - cur) * L >= rebalance_band
            else:
                need = abs(w - cur) > 0.01
            if need:
                if execution == "close":
                    fund, cash, n = _trade(fund, cash, w, cost, book, price, d)
                    trades += n
                else:
                    pending = w
                cur_w_target = w
        if fund > 0:
            pos_days += 1
        # taxes
        if taxed:
            book.expire_deferred(d)
            nxt = days[i + 1] if i + 1 < len(days) else None
            if nxt is None or nxt.year != d.year:
                tax = book.year_end(interest_year)
                interest_year = 0.0
                if tax > 0:
                    if cash >= tax:
                        cash -= tax
                    else:
                        short = tax - cash
                        cash = 0.0
                        if fund > 0:
                            frac = min(1.0, short / fund)
                            for lot in book.lots:
                                lot.shares *= 1 - frac
                                lot.basis *= 1 - frac
                            fund *= 1 - frac
        eq.append(fund + cash)
    eq = pd.Series(eq, index=days)
    final_after = eq.iloc[-1]
    if taxed and fund > 0:
        # liquidate at the end: tax the open lots
        book.sell(sum(l.shares for l in book.lots), fund, days[-1] + pd.Timedelta(days=1))
        book.expire_deferred(days[-1] + pd.Timedelta(days=40))
        final_after -= book.year_end(0.0)
    return {"eq": eq, "trades": trades, "time_in": pos_days / len(days), "final_after_tax": final_after,
            "tax_paid": book.paid}


def _trade(fund, cash, w, cost, book, price, d):
    tot = fund + cash
    want = tot * w
    delta = want - fund
    if abs(delta) < 1e-6:
        return fund, cash, 0
    if delta > 0:
        delta = min(delta, cash / (1 + cost))
    c = abs(delta) * cost
    if delta > 0:
        book.buy(delta / price, delta + c, d)
        fund += delta
        cash -= delta + c
    else:
        sh = -delta / price
        book.sell(sh, -delta - c, d)
        fund += delta
        cash += -delta - c
    return fund, cash, 1


def stats(eq: pd.Series, rf: pd.Series, final_after: float | None = None) -> dict:
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    r = eq.pct_change().dropna()
    cagr = (eq.iloc[-1] / eq.iloc[0]) ** (1 / yrs) - 1 if eq.iloc[-1] > 0 else -1.0
    dd = (eq / eq.cummax() - 1).min()
    ex = r - rf.reindex(r.index).fillna(0) / 252
    sharpe = ex.mean() / r.std() * math.sqrt(252) if r.std() > 0 else 0.0
    yearly = eq.resample("YE").last().pct_change()
    first = eq.resample("YE").last().iloc[0] / eq.iloc[0] - 1
    yearly.iloc[0] = first
    out = {"cagr": cagr, "mdd": dd, "sharpe": sharpe, "worst_year": yearly.min(), "years": yrs}
    if final_after is not None:
        out["cagr_after_tax"] = (final_after / eq.iloc[0]) ** (1 / yrs) - 1 if final_after > 0 else -1.0
    return out


# ----------------------------------------------------------------------------- battery
SPREAD = {"QQQ": 0.005, "SPY": 0.0075, "SOXX": 0.0075, "^GSPC": 0.0075}   # calibrated on TQQQ/QLD, UPRO/SPXL, SOXL
HALVES = {"QQQ": "2013-01-01", "SPY": "2010-01-01", "SOXX": "2014-01-01", "^GSPC": "2006-01-01"}


def run_one(sym, L, rule, execution="close", taxed=True, start=None, end=None, u=None, rf=None):
    u = load(sym) if u is None else u
    rf = tbill(u.index) if rf is None else rf
    expo, allowed = rules(u, L)[rule]
    res = simulate(u, rf, L, SPREAD[sym], expo, allowed, execution=execution, taxed=taxed, start=start, end=end)
    st = stats(res["eq"], rf, res["final_after_tax"] if taxed else None)
    st.update(trades_yr=res["trades"] / st["years"], time_in=res["time_in"])
    return st, res


def battery(syms=("QQQ", "SPY", "SOXX")):
    rows = []
    for sym in syms:
        u = load(sym)
        rf = tbill(u.index)
        start = u.index[200]          # every rule has its 200 days of history
        for L in (1, 2, 3):
            rl = rules(u, L)
            for rule in rl:
                if L == 1 and (rule in ("sma200_voltarget", "sma200_2x_rsi2_3x") or rule.startswith("band2_vol")):
                    continue
                for ex in ("close", "open"):
                    if rule == "buy_hold" and ex == "open":
                        continue
                    full, _ = run_one(sym, L, rule, ex, True, start=start, u=u, rf=rf)
                    pre, _ = run_one(sym, L, rule, ex, False, start=start, u=u, rf=rf)
                    full = dict(full, cagr=pre["cagr"], mdd=pre["mdd"], sharpe=pre["sharpe"], worst_year=pre["worst_year"])
                    h1, _ = run_one(sym, L, rule, ex, False, start=start, end=pd.Timestamp(HALVES[sym]) - pd.Timedelta(days=1), u=u, rf=rf)
                    h2, _ = run_one(sym, L, rule, ex, False, start=pd.Timestamp(HALVES[sym]), u=u, rf=rf)
                    rows.append(dict(sym=sym, L=L, rule=rule, ex=ex, **{k: full[k] for k in ("cagr", "cagr_after_tax", "mdd", "sharpe", "worst_year", "trades_yr", "time_in")},
                                     h1_cagr=h1["cagr"], h1_mdd=h1["mdd"], h2_cagr=h2["cagr"], h2_mdd=h2["mdd"],
                                     start=str(start.date()), half=HALVES[sym]))
                    print(sym, L, rule, ex, f"{full['cagr']*100:.1f} / {full['mdd']*100:.0f}", flush=True)
    return pd.DataFrame(rows)


def signals(syms=("SPY", "QQQ", "SOXX"), sleeve_3x={"SPY": "UPRO", "QQQ": "TQQQ", "SOXX": "SOXL"}):
    """The weekly numbers for the recommended rule, on unadjusted closes (the prices Ryan sees)."""
    lines = []
    for sym in syms:
        raw = pd.read_csv(D / f"{sym}.csv", parse_dates=["date"]).set_index("date")["close"].sort_index()
        u = load(sym)
        band = rules(u, 3)["sma200_band2"][0].iloc[-1] > 0
        s200 = raw.rolling(200).mean().iloc[-1]
        vol = float(np.log(u["c"]).diff().rolling(20).std().iloc[-1] * math.sqrt(252))
        size = min(1.0, 0.50 / vol / 3)
        lines.append(f"{sym} {raw.index[-1].date()}: close {raw.iloc[-1]:.2f}, 200-day {s200:.2f} ({(raw.iloc[-1] / s200 - 1) * 100:+.1f}%), "
                     f"state {'ON' if band else 'OFF'}, turn ON above {s200 * 1.02:.2f}, turn OFF below {s200 * 0.98:.2f}, "
                     f"20-day vol {vol * 100:.0f}%, size if ON {size * 100:.0f}% of the sleeve in {sleeve_3x[sym]} (rest cash)")
    return lines


def recommended_table():
    rows = []
    for sym in ("SPY", "QQQ", "SOXX", "^GSPC"):
        u = load(sym)
        rf = tbill(u.index)
        start = u.index[200]
        for L in (2, 3):
            for ex in ("close", "open"):
                pre, r = run_one(sym, L, "recommended", ex, False, start=start, u=u, rf=rf)
                tx, _ = run_one(sym, L, "recommended", ex, True, start=start, u=u, rf=rf)
                rows.append(dict(sym=sym, L=L, ex=ex, start=str(start.date()), cagr=pre["cagr"], cagr_after_tax=tx["cagr_after_tax"],
                                 mdd=pre["mdd"], sharpe=pre["sharpe"], worst_year=pre["worst_year"], trades_yr=pre["trades_yr"]))
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "signals":
        print("\n".join(signals()))
    elif len(sys.argv) > 1 and sys.argv[1] == "recommended":
        t = recommended_table()
        t.to_csv("data/letf/_recommended.csv", index=False)
        print(t.round(3).to_string(index=False))
    else:
        df = battery()
        df.to_csv("data/letf/_battery.csv", index=False)
