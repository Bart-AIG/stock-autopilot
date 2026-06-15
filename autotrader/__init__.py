"""Stock Autopilot — auto-trader decision/execution layer.

>>> STATUS: PARKED (not the active mode). <<<
The fully-unattended Robinhood path this package was built for is blocked: Robinhood
has no trading API and the account can't expose an authenticator-app TOTP seed, so a
scheduled job can't log in headlessly. The ACTIVE mode is instead **semi-auto one-tap
approval, executed in a Claude session** — see the "One-tap batch approval" section in
CLAUDE.md. This code is retained because (a) the guardrail + news/thesis-gate logic is
the reference the session mode follows, and (b) it's ~90% reusable for a future pivot
to a broker WITH an official API (e.g. Alpaca), where only the executor swaps out.

This package turns the read-only strategy report into REAL orders, with hard
guardrails and an LLM news/thesis veto-gate, so a job could place trades without a
human in the loop — once a headless-capable broker is wired in.

Pipeline (see run.py):
    report.py  ->  logs/report_*_<mode>.json   (mechanical signals)
        |
    build_orders.py   parse signals + holdings -> proposed orders
        |
    guardrails.py     enforce caps / allowlist / staleness / sizing
        |
    thesis_gate.py    LLM checks recent news+analysts; can VETO a buy (never create one)
        |
    executor_robinhood.py   place market orders + GTC whole-share stops (robin_stocks)

SAFETY DEFAULTS (read before enabling):
  - DRY-RUN by default. Nothing is placed unless env AUTOTRADE_LIVE=1 AND
    Robinhood credentials are present. The first CI run should be dry-run so you
    can read the orders.json it WOULD have placed.
  - Only trades the agentic cash account, only tickers in TODAY's report.
  - Conservative caps live in guardrails.py.

These rules mirror CLAUDE.md (the human playbook). Unattended trading is OFF in
CLAUDE.md for in-session safety; this package is the *opt-in* automated path Ryan
explicitly enabled for experimentation.
"""
