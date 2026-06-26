"""
Daily stock analysis pipeline (read-only, no trading).

Ranking engine: Jegadeesh-Titman 12-1 cross-sectional momentum, scaled to a
curated liquid universe (free-tier data can't cover the full Russell 1000).
For each name we make ONE history call and compute:
  - 12-1 momentum: total return over [t-13mo, t-1mo] (skips the last month to
    avoid short-term reversal contamination). THIS is the ranking signal.
  - Context only (not used for ranking): RSI(14), MA50/MA200 position,
    5-day return, volume surge.

It does NOT place trades and does NOT touch Robinhood. Trade decisions are
layered on top, with live positions and per-order user approval.

CAVEAT: FMP free-tier 'light' closes may be UNADJUSTED for splits/dividends,
which adds error to 12-month returns vs the spec's adjusted-close basis.

Usage:
    python analyze.py                # rank full universe, show top 20
    python analyze.py --show 30      # show more rows

Reads FMP_API_KEY from .env in the same folder.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = "https://financialmodelingprep.com/stable"
HERE = Path(__file__).resolve().parent
LOGS = HERE / "logs"

# 12-1 momentum parameters (calendar days).
SKIP_DAYS = 30      # skip most recent ~1 month (reversal contamination)
FORMATION_DAYS = 395  # ~13 months back = formation start
MIN_PRICE = 5.00    # liquidity floor
TOP_DECILE_FRAC = 0.10

# Liquid US universe (~180 names) across all sectors. FMP Starter tier unlocks
# full symbol coverage + 300 calls/min, so universe size is no longer quota-bound
# (1 history call per name; ~180 x 2 runs/day is trivial at 300/min).
UNIVERSE: list[str] = [
    # Tech / semis / software
    "AAPL","MSFT","NVDA","AMD","AVGO","GOOGL","META","AMZN","TSLA","ORCL",
    "CRM","ADBE","NOW","INTC","QCOM","TXN","AMAT","LRCX","KLAC","MU",
    "ARM","SMCI","MRVL","ADI","NXPI","ON","MCHP","INTU","IBM","CSCO",
    "ACN","SNOW","PLTR","CRWD","PANW","ZS","NET","DDOG","DELL","HPQ","WDAY",
    # Internet / media / comm / social
    "NFLX","DIS","CMCSA","T","VZ","TMUS","WBD","SPOT","RBLX",
    "PINS","ROKU","EA","TTWO","BABA","PDD","MELI","SE","RDDT","UBER",
    "ABNB","SHOP","DASH",
    # Consumer discretionary
    "HD","LOW","NKE","MCD","SBUX","CMG","BKNG","MAR","TJX","ROST",
    "LULU","ULTA","DG","DLTR","TGT","F","GM","RIVN","NIO","DKNG",
    # Consumer staples
    "WMT","COST","PG","KO","PEP","MDLZ","CL","KMB","MO","PM","GIS","KHC",
    # Financials / payments
    "JPM","BAC","WFC","C","GS","MS","AXP","V","MA","PYPL",
    "SOFI","COIN","HOOD","SCHW","BLK","SPGI","CME","BK","USB","PNC","COF","KKR","BX",
    # Healthcare / pharma / biotech
    "UNH","JNJ","LLY","PFE","MRK","ABBV","BMY","AMGN","GILD","TMO",
    "DHR","ABT","MDT","CVS","ISRG","VRTX","REGN","MRNA","CI",
    # Energy
    "XOM","CVX","COP","SLB","OXY","MPC","PSX","VLO","EOG","KMI","WMB","HAL","DVN",
    # Industrials
    "BA","CAT","DE","GE","HON","MMM","LMT","RTX","UPS","FDX","UNP","GD","NOC","EMR","ETN",
    # Materials
    "LIN","FCX","NEM","NUE",
    # --- SPECULATIVE / THEMATIC SLEEVE (high volatility, narrative-driven) ---
    # Size these SMALL; cap total speculative exposure (~<=20-25% of account).
    # Quantum computing
    "IONQ","RGTI","QBTS","QUBT","LAES",
    # Nuclear / SMR / uranium
    "SMR","OKLO","CCJ","LEU","UEC","UUUU","DNN","NNE","BWXT",
    # Nuclear / AI-power utilities
    "CEG","VST","GEV","TLN",
    # Space + AI small-caps
    "RKLB","ASTS","SOUN","BBAI",
    # AI infra / datacenter / HPC
    "APLD","IREN","WULF","CRWV","RBRK","INOD",
    # AI healthcare + gene editing
    "TEM","CRSP",
    # eVTOL + drones
    "JOBY","ACHR","RCAT","ONDS",
    # Batteries / clean energy
    "QS","TE","FCEL",
    # Photonics / optical (LITE/COHR/MTSI/VIAV are established mid-caps)
    "POET","AAOI","LASR","LITE","COHR","MTSI","VIAV",
    # Special situation: ex-Ekso Bionics, renamed. DORMANT until ~200d history accrues.
    "CHRN",
    # Broad-market ETFs (context + holdable)
    "SPY","QQQ","IWM","DIA",
]

# Tickers treated as the speculative sleeve (smaller sizing, exposure cap).
SPECULATIVE: set[str] = {
    "IONQ","RGTI","QBTS","QUBT","LAES",
    "SMR","OKLO","CCJ","LEU","UEC","UUUU","DNN","NNE","BWXT",
    "CEG","VST","GEV","TLN","RKLB","ASTS","SOUN","BBAI",
    "APLD","IREN","WULF","CRWV","RBRK","INOD","TEM","CRSP",
    "QS","TE","FCEL","JOBY","ACHR","RCAT","ONDS",
    "POET","AAOI","LASR","CHRN",
}

# Theme tags, used to detect CORRELATED clusters in a report (many setups in one
# theme = one bet, not N). Unmapped tickers fall back to "Other".
THEME_MAP: dict[str, str] = {
    **{t: "Semis" for t in ("NVDA","AMD","AVGO","INTC","QCOM","TXN","AMAT","LRCX",
                            "KLAC","MU","ARM","SMCI","MRVL","ADI","NXPI","ON","MCHP")},
    **{t: "AI-software" for t in ("PLTR","SNOW","CRWD","PANW","ZS","NET","DDOG","SOUN","BBAI")},
    **{t: "AI-infra" for t in ("APLD","IREN","WULF","CRWV","RBRK","INOD")},
    **{t: "Photonics" for t in ("POET","AAOI","LASR","LITE","COHR","MTSI","VIAV")},
    **{t: "Quantum" for t in ("IONQ","RGTI","QBTS","QUBT","LAES")},
    **{t: "AI-health" for t in ("TEM",)},
    **{t: "Uranium" for t in ("CCJ","LEU","UEC","UUUU","DNN")},
    **{t: "Nuclear" for t in ("SMR","OKLO","NNE","BWXT","CEG","VST","GEV","TLN")},
    **{t: "Space" for t in ("RKLB","ASTS")},
    **{t: "eVTOL/Drones" for t in ("JOBY","ACHR","RCAT","ONDS")},
    **{t: "Battery/H2" for t in ("QS","TE","FCEL")},
    **{t: "Gene-edit" for t in ("CRSP",)},
    **{t: "Energy" for t in ("XOM","CVX","COP","SLB","OXY","MPC","PSX","VLO","EOG",
                             "KMI","WMB","HAL","DVN","EPD")},
    **{t: "Index-ETF" for t in ("SPY","QQQ","IWM","DIA")},
    # --- Joint-watch names not otherwise mapped (so theme/cluster tags render) ---
    **{t: "AI-software" for t in ("PATH","FIG")},
    **{t: "Semis" for t in ("TSEM","AEHR")},
    **{t: "Space" for t in ("BKSY",)},
    **{t: "Financials" for t in ("IBKR","ACGL")},
    **{t: "Industrials" for t in ("EME",)},
    **{t: "BTC-mining" for t in ("HIVE",)},
    **{t: "Comm" for t in ("NOK",)},
    **{t: "Mining" for t in ("TMC",)},
}

# Themes that move together as one risk factor (the "AI/tech complex").
AI_COMPLEX: set[str] = {"Semis", "AI-software", "AI-infra", "Photonics", "Quantum", "AI-health"}


def theme_of(sym: str) -> str:
    return THEME_MAP.get(sym, "Other")


def load_api_key() -> str:
    # Prefer the environment variable (used by the remote routine); fall back to
    # the local .env file (used when running on your machine).
    env_key = os.environ.get("FMP_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()
    env_path = HERE / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("FMP_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("ERROR: FMP_API_KEY not set (env var) and not found in .env")


def fmp_history(sym: str, key: str, days: int = 430) -> list[dict] | None:
    """One history call per name. Returns rows (newest-first) or None on paywall/empty."""
    to_d = datetime.now(timezone.utc).date()
    from_d = to_d - timedelta(days=days)
    url = (f"{BASE}/historical-price-eod/light?symbol={sym}"
           f"&from={from_d}&to={to_d}&apikey={key}")
    for attempt in range(2):
        try:
            with urllib.request.urlopen(url, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data if isinstance(data, list) and data else None
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt == 0:
                time.sleep(2)
                continue
            return None  # 402 paywall or other -> skip this name
    return None


def fmp_fundamentals(sym: str, key: str) -> dict:
    """TTM valuation snapshot for the long-term VALUE lens: P/E, P/FCF, PEG.

    ONE call to /stable/ratios-ttm. PEG (P/E ÷ earnings growth) is the key 'value for
    growth' read — it discounts a high P/E by the growth rate, which is exactly the
    'value in high-growth names' question. Returns {} on paywall/empty/error so the
    caller degrades gracefully to the price-only screen (fundamentals are OPTIONAL —
    if the data tier doesn't expose this endpoint, the screen still works on price)."""
    url = f"{BASE}/ratios-ttm?symbol={sym}&apikey={key}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
        return {}
    if not (isinstance(data, list) and data and isinstance(data[0], dict)):
        return {}
    d = data[0]

    def pick(*keys):
        # FMP field spellings have drifted across versions — try the known aliases.
        for k in keys:
            v = d.get(k)
            if isinstance(v, (int, float)):
                return round(float(v), 1)
        return None

    out = {
        "pe": pick("priceToEarningsRatioTTM", "peRatioTTM"),
        "pfcf": pick("priceToFreeCashFlowsRatioTTM", "priceToFreeCashFlowRatioTTM", "pfcfRatioTTM"),
        "peg": pick("priceEarningsToGrowthRatioTTM", "pegRatioTTM"),
    }
    return out if any(v is not None for v in out.values()) else {}


def price_on_or_before(rows_desc: list[dict], target: str) -> float | None:
    """rows_desc is newest-first. Return the close on/just before target date."""
    for r in rows_desc:
        if r.get("date", "") <= target and "price" in r:
            return r["price"]
    return None


def compute_rsi(closes: list[float], period: int = 14) -> float | None:
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, period + 1):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0)); losses.append(max(-d, 0.0))
    ag = sum(gains) / period; al = sum(losses) / period
    for i in range(period + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        ag = (ag * (period - 1) + max(d, 0.0)) / period
        al = (al * (period - 1) + max(-d, 0.0)) / period
    if al == 0:
        return 100.0
    return round(100 - (100 / (1 + ag / al)), 1)


def analyze(sym: str, rows_desc: list[dict]) -> dict | None:
    """Compute 12-1 momentum (ranking signal) + context from one history series."""
    today = datetime.now(timezone.utc).date()
    end_target = str(today - timedelta(days=SKIP_DAYS))       # formation end (~1mo ago)
    start_target = str(today - timedelta(days=FORMATION_DAYS))  # formation start (~13mo ago)

    p_end = price_on_or_before(rows_desc, end_target)
    p_start = price_on_or_before(rows_desc, start_target)
    if not p_start or not p_end or p_start <= 0:
        return None  # insufficient history at an endpoint -> exclude (no look-ahead fudge)

    mom = round((p_end / p_start - 1) * 100, 1)

    closes_desc = [r["price"] for r in rows_desc if "price" in r]
    vols_desc = [r["volume"] for r in rows_desc if "volume" in r]
    price = closes_desc[0] if closes_desc else None
    if not price or price < MIN_PRICE:
        return None  # liquidity floor

    closes_chrono = list(reversed(closes_desc))
    ma50 = round(sum(closes_desc[:50]) / 50, 2) if len(closes_desc) >= 50 else None
    ma200 = round(sum(closes_desc[:200]) / 200, 2) if len(closes_desc) >= 200 else None
    ret5 = round((closes_desc[0] / closes_desc[5] - 1) * 100, 1) if len(closes_desc) > 5 else None

    vol_surge = None
    if len(vols_desc) >= 21 and vols_desc[0]:
        avg20 = sum(vols_desc[1:21]) / 20
        if avg20:
            vol_surge = round(vols_desc[0] / avg20, 2)

    return {
        "symbol": sym,
        "close": round(price, 2),
        "mom_12_1_pct": mom,          # RANKING SIGNAL
        "rsi14": compute_rsi(closes_chrono),
        "ret_5d_pct": ret5,
        "ma50": ma50,
        "ma200": ma200,
        "above_ma200": (price > ma200) if ma200 else None,
        "vol_surge_x": vol_surge,
        "hist_days": len(rows_desc),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", type=int, default=20, help="rows to print")
    args = ap.parse_args()

    key = load_api_key()
    LOGS.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")

    print(f"12-1 momentum scan over {len(UNIVERSE)} names (1 history call each)...")
    results, blocked = [], []
    for i, sym in enumerate(UNIVERSE, 1):
        rows = fmp_history(sym, key)
        if rows is None:
            blocked.append(sym)
        else:
            row = analyze(sym, rows)
            if row:
                results.append(row)
        if i % 20 == 0:
            print(f"  {i}/{len(UNIVERSE)} scanned, {len(results)} ranked, {len(blocked)} blocked/skipped")
        time.sleep(0.2)  # be gentle on the free tier

    results.sort(key=lambda r: r["mom_12_1_pct"], reverse=True)
    n_decile = max(1, int(len(results) * TOP_DECILE_FRAC))
    for rank, r in enumerate(results, 1):
        r["rank"] = rank
        r["in_top_decile"] = rank <= n_decile

    out = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "strategy": "12-1 cross-sectional momentum (scaled), rank by mom_12_1_pct desc",
        "universe": len(UNIVERSE),
        "ranked": len(results),
        "blocked_or_skipped": blocked,
        "top_decile_n": n_decile,
        "results": results,
    }
    out_path = LOGS / f"momentum_{stamp}.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(f"\nRanked {len(results)} names ({len(blocked)} blocked/skipped). Top decile = {n_decile}.")
    print(f"{'#':>3} {'SYM':6}{'mom12-1%':>10}{'close':>9}{'RSI':>6}{'5d%':>7}{'>200MA':>8}{'surge':>7}")
    for r in results[: args.show]:
        print(f"{r['rank']:>3} {r['symbol']:6}{r['mom_12_1_pct']:>10}{r['close']:>9}"
              f"{str(r['rsi14']):>6}{str(r['ret_5d_pct']):>7}{str(r['above_ma200'])[0]:>8}{str(r['vol_surge_x']):>7}")
    print(f"\nWrote {out_path}")
    print("NOTE: ranking fact-base only. No trades placed. No Robinhood access.")


if __name__ == "__main__":
    main()
