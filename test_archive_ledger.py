#!/usr/bin/env python3
"""Tests for archive_ledger.py on a synthetic ledger. Run: python3 test_archive_ledger.py"""

import contextlib
import io
import json
import tempfile
from pathlib import Path

import archive_ledger as A


def make(root: Path):
    ledger = {"_comment": "old comment", "updated_utc": "x", "positions": [{"symbol": "ILMN", "note": "dash —"}],
              "_closed_positions": [{"symbol": "QLD", "realized_pnl": 1.5}],
              "_SLEEVE_PROCESS": {"start_utc": "2026-09-30T20:14Z"}, "_resolved_flags": [{"a": 1}],
              "_OLD_FINDING_2026-09-01": {"text": "long note"}, "_DAY_TRACK": {"phase": "paper"},
              "_CLASH": {"v": 2}}
    archive = {"_comment": "archive", "_CLASH": {"v": 1}}
    journal = {"entries": [{"run_utc": "2026-08-11T16:55:00Z", "headline": "a"},
                           {"run_utc": "2026-09-30T20:14Z", "headline": "b"},
                           {"run_utc": "2026-10-13T21:19Z", "headline": "c"},
                           {"run_utc": "2026-10-14T13:24:00Z", "headline": "d"},
                           {"timestamp_utc": "2026-11-13T19:47Z", "headline": "e"},
                           {"headline": "undated stays"}]}
    (root / "holdings.json").write_text(json.dumps(ledger, indent=2))
    (root / "ledger_findings_archive.json").write_text(json.dumps(archive, indent=2))
    (root / "trade_journal.json").write_text(json.dumps(journal, indent=2))
    return ledger, archive, journal


def run(root: Path, *extra):
    with contextlib.redirect_stdout(io.StringIO()):
        assert A.main(["--root", str(root), "--today", "2026-11-13", *extra]) == 0


def test_moves_everything_and_loses_nothing():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        ledger, archive, journal = make(root)
        run(root, "--dry-run")
        assert json.loads((root / "holdings.json").read_text()) == ledger          # dry run writes nothing
        run(root)
        h = json.loads((root / "holdings.json").read_text())
        a = json.loads((root / "ledger_findings_archive.json").read_text())
        j = json.loads((root / "trade_journal.json").read_text())
        assert set(h) == {"_comment", "updated_utc", "positions", "_closed_positions", "_SLEEVE_PROCESS",
                          "_resolved_flags", "_findings_archive_pointer"}
        for k in ("positions", "_closed_positions", "_SLEEVE_PROCESS", "_resolved_flags", "updated_utc"):
            assert h[k] == ledger[k]
        assert a["_OLD_FINDING_2026-09-01"] == ledger["_OLD_FINDING_2026-09-01"] and a["_DAY_TRACK"] == ledger["_DAY_TRACK"]
        assert a["_CLASH"] == {"v": 1} and a["_CLASH__from_holdings_2026-11-13"] == {"v": 2}   # both kept
        assert a["_comment"] == "archive" and "_moved_2026-11-13" in a
        assert [e["headline"] for e in j["entries"]] == ["d", "e", "undated stays"]
        months = {p.name: json.loads(p.read_text())["entries"] for p in root.glob("trade_journal_archive_*.json")}
        assert {k: [e["headline"] for e in v] for k, v in months.items()} == {
            "trade_journal_archive_2026-08.json": ["a"], "trade_journal_archive_2026-09.json": ["b"],
            "trade_journal_archive_2026-10.json": ["c"]}
        # formats: ledger and journal stay indent=2 with escaped non-ASCII
        assert (root / "holdings.json").read_text() == json.dumps(h, indent=2) and "\\u2014" in (root / "holdings.json").read_text()
        assert (root / "trade_journal.json").read_text() == json.dumps(j, indent=2)
        # a second run changes nothing; a later run appends to the month files
        snap = {p.name: p.read_text() for p in root.iterdir()}
        run(root)
        assert {p.name: p.read_text() for p in root.iterdir()} == snap
        with contextlib.redirect_stdout(io.StringIO()):
            assert A.main(["--root", str(root), "--today", "2026-11-20"]) == 0      # cutoff moves to 10-21
        j2 = json.loads((root / "trade_journal.json").read_text())
        oct_ = json.loads((root / "trade_journal_archive_2026-10.json").read_text())["entries"]
        assert [e["headline"] for e in j2["entries"]] == ["e", "undated stays"] and [e["headline"] for e in oct_] == ["c", "d"]


def test_refuses_a_file_in_another_format():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        ledger, _, _ = make(root)
        (root / "holdings.json").write_text(json.dumps(ledger, indent=1))
        try:
            run(root)
        except SystemExit as e:
            assert "round-trip" in str(e)
        else:
            raise AssertionError("rewrote a ledger that was not indent=2")
        assert (root / "holdings.json").read_text() == json.dumps(ledger, indent=1)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("ok")
