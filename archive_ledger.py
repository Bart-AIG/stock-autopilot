#!/usr/bin/env python3
"""
archive_ledger.py: move old notes out of holdings.json and old entries out of trade_journal.json.
Nothing is deleted. Every key and every entry is preserved verbatim in an archive file.

Why (audit 2026-11-13, finding 7; Ryan, live turn: "7. accepted, lets do that"): holdings.json was
1.97 MB, of which 1.87 MB was 347 notes from the August and September process that the sleeve
process does not read. trade_journal.json was 9.4 MB, 92% of it older than 30 days.

  holdings.json       keeps the keys in KEEP (the book, closed positions, the sleeve process
                      state, resolved flags). Every other top-level key moves to
                      ledger_findings_archive.json under the same name.
  trade_journal.json  keeps entries from the last JOURNAL_KEEP_DAYS days. Older entries move to
                      trade_journal_archive_YYYY-MM.json, by the month of their run_utc.
                      Fills and exits also live in holdings.json._closed_positions and at the
                      broker, which is the record for P&L.

Run it only when no routine run is writing the ledger (after the bell, or a weekend), on a
checkout that is level with origin/master, and land it before the next run.

  python3 archive_ledger.py --dry-run          show what would move
  python3 archive_ledger.py --today 2026-11-13 do it (the date sets the journal cutoff)

Safe to run again: it only moves what is outside KEEP or older than the cutoff.
"""

from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEEP = (
    "_comment", "updated_utc", "positions", "_closed_positions", "_SLEEVE_PROCESS",
    "_CALIBRATION_REGIME_START", "_CALIBRATION_REGIME_START_note", "_resolved_flags",
    "_findings_archive_pointer",
)
JOURNAL_KEEP_DAYS = 30
LEDGER_COMMENT = (
    "Positions ledger. positions[] holds the sleeve positions (sleeve swing_q, swing_m, bbw, levx) "
    "and Ryan's own positions (placed_agent 'user': never sold by the agent). _closed_positions[] "
    "holds every closed position. _SLEEVE_PROCESS holds the sleeve process state, including the "
    "real-money drawdown reading (drawdown_real, written by capital.py). The agent places no stop "
    "orders. Notes from the earlier processes are in ledger_findings_archive.json."
)
POINTER = (
    "Notes and findings from the August and September 2026 processes live in "
    "ledger_findings_archive.json under their original key names (first move 2026-08-28; the rest "
    "moved 2026-11-13; nothing deleted). A holdings.json._KEY named in CLAUDE.md that is not in "
    "this file is there. Journal entries older than 30 days are in "
    "trade_journal_archive_YYYY-MM.json. Keep THIS file to the book plus live state."
)


def _load(p: Path, indent: int):
    """Load a JSON file and insist it is in the format we will write back."""
    text = p.read_text()
    obj = json.loads(text)
    tail = "\n" if text.endswith("\n") else ""
    if json.dumps(obj, indent=indent) + tail != text:
        raise SystemExit(f"{p.name} does not round-trip at indent={indent}: stopping, nothing written")
    return obj, tail


def _run_utc(e: dict) -> str:
    return str(e.get("run_utc") or e.get("timestamp_utc") or "")


def plan(root: Path, today: str) -> dict:
    ledger, l_tail = _load(root / "holdings.json", 2)
    arch_p = root / "ledger_findings_archive.json"
    arch, a_tail = _load(arch_p, 2) if arch_p.exists() else ({}, "")
    journal, j_tail = _load(root / "trade_journal.json", 2)

    moved, kept = {}, {}
    for k, v in ledger.items():
        (kept if k in KEEP else moved)[k] = v
    kept_original = len(kept)
    for k, v in moved.items():
        name = k
        if k in arch and arch[k] != v:
            name = f"{k}__from_holdings_{today}"       # same name, different content: keep both
        arch[name] = v
    if moved:
        arch[f"_moved_{today}"] = (
            f"{len(moved)} top-level keys moved here from holdings.json on {today} by archive_ledger.py "
            "(audit finding 7). Verbatim, original names; restorable by moving a key back.")
        kept["_comment"] = LEDGER_COMMENT
        kept["_findings_archive_pointer"] = POINTER

    cutoff = (date.fromisoformat(today) - timedelta(days=JOURNAL_KEEP_DAYS)).isoformat()
    live, old = [], {}
    for e in journal["entries"]:
        ru = _run_utc(e)
        if ru and ru[:10] < cutoff:
            old.setdefault(ru[:7], []).append(e)
        else:
            live.append(e)                              # recent, or undated: stays
    months = {}
    for m, es in old.items():
        mp = root / f"trade_journal_archive_{m}.json"
        if mp.exists():
            cur, _ = _load(mp, 1)
        else:
            cur = {"_comment": f"Entries of trade_journal.json with run_utc in {m}, moved out by "
                               "archive_ledger.py. Verbatim. The live journal holds the last 30 days.",
                   "entries": []}
        cur["entries"].extend(es)
        cur["entries"].sort(key=_run_utc)
        months[m] = cur
    new_journal = dict(journal)
    new_journal["entries"] = live
    return {
        "ledger": kept, "ledger_tail": l_tail, "archive": arch, "archive_tail": a_tail,
        "journal": new_journal, "journal_tail": j_tail, "months": months, "cutoff": cutoff,
        "counts": {
            "ledger_keys_before": len(ledger), "ledger_keys_kept": kept_original, "ledger_keys_moved": len(moved),
            "ledger_bytes_before": len(json.dumps(ledger, indent=2)), "ledger_bytes_after": len(json.dumps(kept, indent=2)),
            "journal_entries_before": len(journal["entries"]), "journal_entries_kept": len(live),
            "journal_entries_moved": sum(len(v) for v in old.values()),
            "journal_moved_by_month": {m: len(v) for m, v in sorted(old.items())},
            "journal_bytes_before": len(json.dumps(journal, indent=2)),
            "journal_bytes_after": len(json.dumps(new_journal, indent=2)),
        },
        "_moved": moved, "_old": old,
    }


def check(root: Path, p: dict) -> None:
    """Nothing lost: every moved key and entry is in an archive, byte for byte."""
    c = p["counts"]
    assert c["ledger_keys_kept"] + c["ledger_keys_moved"] == c["ledger_keys_before"]
    assert c["journal_entries_kept"] + c["journal_entries_moved"] == c["journal_entries_before"]
    for k, v in p["_moved"].items():
        hits = [n for n in p["archive"] if n == k or n.startswith(k + "__from_holdings_")]
        assert any(p["archive"][n] == v for n in hits), f"{k} missing from the archive"
    for m, es in p["_old"].items():
        have = {json.dumps(e, sort_keys=True) for e in p["months"][m]["entries"]}
        assert all(json.dumps(e, sort_keys=True) in have for e in es), f"entries missing from {m}"


def write(root: Path, p: dict) -> None:
    (root / "holdings.json").write_text(json.dumps(p["ledger"], indent=2) + p["ledger_tail"])
    (root / "ledger_findings_archive.json").write_text(json.dumps(p["archive"], indent=2) + p["archive_tail"])
    (root / "trade_journal.json").write_text(json.dumps(p["journal"], indent=2) + p["journal_tail"])
    for m, cur in p["months"].items():
        (root / f"trade_journal_archive_{m}.json").write_text(json.dumps(cur, indent=1))


def main(argv: list[str]) -> int:
    root = Path(argv[argv.index("--root") + 1]) if "--root" in argv else HERE
    today = argv[argv.index("--today") + 1] if "--today" in argv else date.today().isoformat()
    p = plan(root, today)
    check(root, p)
    print(json.dumps({"today": today, "journal_cutoff": p["cutoff"], **p["counts"]}, indent=1))
    if "--dry-run" in argv:
        print("dry run: nothing written")
        return 0
    write(root, p)
    print("written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
