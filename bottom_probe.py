"""TEMPORARY probe (round 2), run once on a GitHub runner from the session branch. Deleted before merge.

1. Which sources can the runner read VIX from (FMP, Yahoo, Cboe, FRED)?
2. What does the FMP quote return for QQQ / SPY (fields, timestamp)?
3. Pull the monthly series Ryan asked about (Shiller P/E, M2, margin debt) into
   data/bottom/macro/*.csv so the backtest can test them. Never prints the API key.
"""
import csv
import html as htmllib
import io
import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
KEY = os.environ.get("FMP_API_KEY", "")
BASE = "https://financialmodelingprep.com/stable"
OUT = Path(__file__).parent / "data" / "bottom" / "macro"
OUT.mkdir(parents=True, exist_ok=True)
MON = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}


def get(url, binary=False, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            b = r.read()
            return r.status, (b if binary else b.decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        return e.code, (b"" if binary else "")
    except Exception as e:  # noqa: BLE001
        return 0, (b"" if binary else type(e).__name__)


def section(t):
    print("\n" + "=" * 8, t, "=" * 8, flush=True)


def save(name, rows):
    rows = sorted(set(rows))
    with open(OUT / name, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["date", "value"])
        w.writerows(rows)
    print(f"saved {name}: {len(rows)} rows, {rows[0] if rows else None} .. {rows[-1] if rows else None}")


def fmp():
    section("FMP quote")
    for sym in ("QQQ", "SPY", "%5EVIX", "^VIX"):
        st, body = get(f"{BASE}/quote?symbol={sym}&apikey={KEY}")
        try:
            d = json.loads(body)
        except Exception:  # noqa: BLE001
            d = None
        if isinstance(d, list) and d:
            q = d[0]
            ts = q.get("timestamp")
            print(sym, st, "keys:", sorted(q.keys()))
            print("   ", {k: q.get(k) for k in ("price", "open", "dayHigh", "dayLow", "volume", "previousClose", "timestamp")},
                  "ts_utc:", datetime.fromtimestamp(ts, timezone.utc).isoformat() if ts else None)
        else:
            print(sym, st, "no data:", str(body)[:160].replace(KEY, "***") if KEY else str(body)[:160])
    section("FMP history")
    today = datetime.now(timezone.utc).date()
    for sym, frm in (("QQQ", today - timedelta(days=12)), ("%5EVIX", today - timedelta(days=12)),
                     ("QQQ", "2015-01-01"), ("%5EVIX", "2015-01-01")):
        st, body = get(f"{BASE}/historical-price-eod/full?symbol={sym}&from={frm}&to={today}&apikey={KEY}")
        try:
            d = json.loads(body)
        except Exception:  # noqa: BLE001
            d = None
        if isinstance(d, list) and d:
            print(sym, frm, st, "rows", len(d), "newest", {k: d[0].get(k) for k in ("date", "open", "high", "low", "close", "volume")},
                  "oldest", d[-1].get("date"))
        else:
            print(sym, frm, st, "no data:", (str(body)[:160].replace(KEY, "***") if KEY else str(body)[:160]))


def yahoo():
    section("Yahoo ^VIX")
    for host in ("query1", "query2"):
        st, body = get(f"https://{host}.finance.yahoo.com/v8/finance/chart/%5EVIX?range=10d&interval=1d")
        try:
            r = json.loads(body)["chart"]["result"][0]
            m = r["meta"]
            cl = r["indicators"]["quote"][0]["close"]
            ds = [datetime.fromtimestamp(t, timezone.utc).date().isoformat() for t in r["timestamp"]]
            print(host, st, "price", m.get("regularMarketPrice"), "time",
                  datetime.fromtimestamp(m.get("regularMarketTime", 0), timezone.utc).isoformat(), "last3", list(zip(ds, cl))[-3:])
        except Exception as e:  # noqa: BLE001
            print(host, st, "fail", type(e).__name__, str(body)[:160])


def cboe():
    section("Cboe")
    st, body = get("https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv")
    lines = body.strip().splitlines()
    print("history csv", st, "lines", len(lines), "head", lines[:1], "tail", lines[-2:])
    st, body = get("https://cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json")
    try:
        d = json.loads(body)
        dd = d.get("data", {})
        print("delayed json", st, "top keys", sorted(d.keys()), "data keys", sorted(dd.keys())[:40])
        print("   ", {k: dd.get(k) for k in ("symbol", "current_price", "close", "prev_day_close", "open", "high", "low", "last_trade_time")},
              "timestamp", d.get("timestamp"))
    except Exception as e:  # noqa: BLE001
        print("delayed json", st, "fail", type(e).__name__, str(body)[:160])


def fred(series, name):
    st, body = get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}")
    rows = []
    for ln in body.strip().splitlines()[1:]:
        p = ln.split(",")
        if len(p) >= 2:
            try:
                rows.append((p[0], float(p[1])))
            except ValueError:
                pass
    print("FRED", series, st, "rows", len(rows), "tail", rows[-2:])
    if rows and name:
        save(name, rows)
    return rows


def cape():
    section("Shiller P/E")
    st, body = get("https://www.multpl.com/shiller-pe/table/by-month")
    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body, flags=re.S):
        txt = htmllib.unescape(re.sub(r"<[^>]+>", " ", tr))
        m = re.search(r"([A-Z][a-z]{2})\w* (\d{1,2}), (\d{4})\D+?(\d+\.\d+)", txt, flags=re.S)
        if m and m.group(1).lower() in MON:
            rows.append((f"{m.group(3)}-{MON[m.group(1).lower()]:02d}-01", float(m.group(4))))
    print("multpl", st, "len", len(body), "rows", len(rows))
    if len(rows) < 300:
        print("   head:", body[:300].replace("\n", " "))
        st, b = get("http://www.econ.yale.edu/~shiller/data/ie_data.xls", binary=True)
        print("shiller xls", st, "bytes", len(b))
        try:
            import xlrd
            sh = xlrd.open_workbook(file_contents=b).sheet_by_name("Data")
            col = None
            for r in range(0, 12):
                for c in range(sh.ncols):
                    if str(sh.cell_value(r, c)).strip().upper() in ("CAPE", "P/E10"):
                        col = c
            print("   cape column", col)
            for r in range(8, sh.nrows):
                dv, v = sh.cell_value(r, 0), sh.cell_value(r, col)
                if isinstance(dv, float) and isinstance(v, float) and dv > 1900:
                    y = int(dv)
                    mth = int(round((dv - y) * 100))
                    rows.append((f"{y}-{max(1, min(12, mth)):02d}-01", round(v, 2)))
        except Exception as e:  # noqa: BLE001
            print("   xls fail", type(e).__name__, e)
    if rows:
        save("CAPE.csv", rows)


def margin():
    section("FINRA margin debt")
    rows = []

    def ym(x):
        if isinstance(x, datetime):
            return f"{x.year}-{x.month:02d}-01"
        s = str(x).strip()
        m = re.match(r"^(\d{4})-(\d{1,2})", s)
        if m:
            return f"{m.group(1)}-{int(m.group(2)):02d}-01"
        m = re.match(r"^([A-Za-z]{3})[A-Za-z]*[-\s'](\d{2,4})$", s)
        if m and m.group(1).lower() in MON:
            y = int(m.group(2))
            y = y if y > 100 else (1900 + y if y >= 90 else 2000 + y)
            return f"{y}-{MON[m.group(1).lower()]:02d}-01"
        return None

    def num(x):
        if isinstance(x, (int, float)):
            return float(x)
        try:
            return float(str(x).replace(",", "").replace("$", "").strip())
        except ValueError:
            return None

    page_st, page = get("https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics")
    links = sorted(set(re.findall(r'href="([^"]+\.xlsx?)"', page)))
    print("page", page_st, "len", len(page), "xlsx links", links[:6])
    cands = [("https://www.finra.org" + u if u.startswith("/") else u) for u in links]
    cands.append("https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx")
    for u in cands:
        st, b = get(u, binary=True)
        print("xlsx", st, len(b), u)
        if st == 200 and len(b) > 2000:
            try:
                import openpyxl
                ws = openpyxl.load_workbook(io.BytesIO(b), data_only=True).worksheets[0]
                for i, row in enumerate(ws.iter_rows(values_only=True)):
                    if i < 3:
                        print("   row", i, row[:4])
                    if row and row[0] is not None and len(row) > 1:
                        d, v = ym(row[0]), num(row[1])
                        if d and v:
                            rows.append((d, v))
            except Exception as e:  # noqa: BLE001
                print("   xlsx fail", type(e).__name__, e)
        if len(rows) > 200:
            break
    if len(rows) < 200:
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", page, flags=re.S):
            cells = [htmllib.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, flags=re.S)]
            if len(cells) >= 2:
                d, v = ym(cells[0]), num(cells[1])
                if d and v:
                    rows.append((d, v))
        print("html rows", len(rows))
        if len(rows) < 200:
            print("   page head:", page[:300].replace("\n", " "))
    if rows:
        save("MARGIN_DEBT.csv", rows)


def curl(url, out, ua=UA, extra=()):
    import subprocess
    cmd = ["curl", "-sSL", "--compressed", "--max-time", "25", "-o", str(out), "-w", "%{http_code}", "-A", ua,
           "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "-H", "Accept-Language: en-US,en;q=0.9"]
    cmd += list(extra) + [url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    size = Path(out).stat().st_size if Path(out).exists() else 0
    return r.stdout.strip()[-3:], size


def fred_curl(series, name):
    tmp = Path("/tmp") / f"{series}.csv"
    for ua in ("curl/8.5.0", UA):
        code, size = curl(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}", tmp, ua=ua)
        rows = []
        if code == "200" and size > 50:
            for ln in tmp.read_text(errors="replace").strip().splitlines()[1:]:
                p = ln.split(",")
                try:
                    rows.append((p[0], float(p[1])))
                except (ValueError, IndexError):
                    pass
        print("FRED curl", series, "ua", ua[:12], code, size, "rows", len(rows), "tail", rows[-2:], flush=True)
        if rows:
            save(name, rows)
            return rows
    return []


def fed_h6():
    section("Federal Reserve H.6 (M2)")
    import zipfile
    tmp = Path("/tmp/h6.zip")
    code, size = curl("https://www.federalreserve.gov/datadownload/Output.aspx?rel=H6&filetype=zip", tmp)
    print("zip", code, size)
    if code != "200" or size < 1000:
        return
    try:
        z = zipfile.ZipFile(tmp)
    except Exception as e:  # noqa: BLE001
        print("not a zip", type(e).__name__, tmp.read_bytes()[:200])
        return
    print("files", z.namelist())
    for nm in z.namelist():
        if not nm.lower().endswith(".xml") or "struct" in nm.lower():
            continue
        x = z.read(nm).decode("utf-8", "replace")
        blocks = re.findall(r"<kf:Series\b([^>]*)>(.*?)</kf:Series>", x, flags=re.S)
        print(nm, "series", len(blocks))
        for attrs, body in blocks:
            name = (re.search(r'SERIES_NAME="([^"]+)"', attrs) or [None, "?"])[1]
            desc = (re.search(r"<common:AnnotationText>([^<]+)", body) or [None, ""])[1]
            obs = re.findall(r'OBS_VALUE="([^"]+)"[^>]*TIME_PERIOD="([^"]+)"', body) or \
                [(v, t) for t, v in re.findall(r'TIME_PERIOD="([^"]+)"[^>]*OBS_VALUE="([^"]+)"', body)]
            print("   ", name, "|", desc[:70], "| obs", len(obs), "| last", obs[-1] if obs else None)
            if re.match(r"^M2(_N)?\.M$", name) and obs:
                rows = []
                for v, t in obs:
                    try:
                        rows.append((t[:7] + "-01", float(v)))
                    except ValueError:
                        pass
                save(f"M2__{name.replace('.', '_')}.csv", rows)


def finra_curl():
    section("FINRA margin debt via curl")
    for i, u in enumerate(("https://www.finra.org/sites/default/files/2021-03/margin-statistics.xlsx",
                           "https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics",
                           "https://www.finra.org/investors/learn-to-invest/advanced-investing/margin-statistics")):
        tmp = Path(f"/tmp/finra{i}")
        for ua in (UA, "curl/8.5.0"):
            code, size = curl(u, tmp, ua=ua)
            print(code, size, ua[:12], u, flush=True)
            if code == "200" and size > 5000:
                b = tmp.read_bytes()
                if b[:2] == b"PK":
                    try:
                        import openpyxl
                        ws = openpyxl.load_workbook(io.BytesIO(b), data_only=True).worksheets[0]
                        rows = []
                        for j, row in enumerate(ws.iter_rows(values_only=True)):
                            if j < 3:
                                print("   row", j, row[:4])
                            if row and row[0] is not None and len(row) > 1 and isinstance(row[1], (int, float)):
                                s0 = row[0].strftime("%Y-%m") if isinstance(row[0], datetime) else str(row[0]).strip()
                                m = re.match(r"^(\d{4})-(\d{1,2})", s0)
                                m2 = re.match(r"^([A-Za-z]{3})[A-Za-z]*[-\s'](\d{2,4})$", s0)
                                if m:
                                    rows.append((f"{m.group(1)}-{int(m.group(2)):02d}-01", float(row[1])))
                                elif m2 and m2.group(1).lower() in MON:
                                    y = int(m2.group(2))
                                    y = y if y > 100 else (1900 + y if y >= 90 else 2000 + y)
                                    rows.append((f"{y}-{MON[m2.group(1).lower()]:02d}-01", float(row[1])))
                        if rows:
                            save("MARGIN_DEBT.csv", rows)
                            return
                    except Exception as e:  # noqa: BLE001
                        print("   xlsx fail", type(e).__name__, e)
                else:
                    page = b.decode("utf-8", "replace")
                    print("   html title:", (re.search(r"<title>([^<]*)", page) or [None, ""])[1][:80],
                          "| xlsx links:", sorted(set(re.findall(r'href="([^"]+\.xlsx?)"', page)))[:5])
                break


def vendor_check():
    section("FMP vs the repo's Robinhood history")
    today = datetime.now(timezone.utc).date()
    for sym, fsym in (("QQQ", "QQQ"), ("SPY", "SPY"), ("VIX", "%5EVIX")):
        st, body = get(f"{BASE}/historical-price-eod/full?symbol={fsym}&from=1999-01-01&to={today}&apikey={KEY}")
        try:
            d = json.loads(body)
        except Exception:  # noqa: BLE001
            d = []
        f = {r["date"]: r for r in d if isinstance(r, dict)} if isinstance(d, list) else {}
        base = {r["date"]: r for r in csv.DictReader(open(Path(__file__).parent / "data" / "bottom" / f"{sym}.csv"))}
        both = sorted(set(f) & set(base))
        diffs = [(dd, float(base[dd]["close"]), f[dd]["close"], round(f[dd]["close"] / float(base[dd]["close"]) - 1, 4)) for dd in both]
        bad = [x for x in diffs if abs(x[3]) > 0.003]
        only_f = sorted(set(f) - set(base))
        only_b = sorted(x for x in set(base) - set(f) if f and x >= min(f))
        print(sym, "status", st, "fmp rows", len(f), "from", min(f) if f else None, "| overlap", len(both),
              "| closes off by >0.3%:", len(bad), bad[:6], "... last", bad[-3:])
        print("    dates only in FMP:", len(only_f), only_f[:4], only_f[-3:], "| only in repo:", len(only_b), only_b[:6])
        lo = [(dd, float(base[dd]["low"]), f[dd]["low"]) for dd in both if abs(f[dd]["low"] / float(base[dd]["low"]) - 1) > 0.01]
        print("    lows off by >1%:", len(lo), lo[:5], flush=True)


if __name__ == "__main__":
    print("key present:", bool(KEY))
    vendor_check()          # round 3: only the vendor comparison, so it is at the end of the log
