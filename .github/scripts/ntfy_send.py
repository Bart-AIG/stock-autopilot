"""Send one ntfy push from a GitHub runner. Shared by the notify workflows.

Priority order on Ryan's phone (set 2026-10-05, his request): Joint risk watch and
Quality @ 200-day pushes outrank the Stock Autopilot report pushes.
  urgent  Joint risk RED / ORANGE, CRACK WATCH
  high    other Joint risk and Quality @ 200-day pushes; report DATA ERROR
  default Stock Autopilot ACTION
  min     Stock Autopilot no-trade heartbeat (silent)

Delivery: if the NTFY_TOKEN secret is set, every publish is authenticated, so it counts
against Ryan's own ntfy account instead of the shared GitHub runner IP. Anonymous
publishes share a per-IP daily quota with every other job on that runner, which is how
the 2026-10-05 RED risk push was lost (HTTP 429, "daily message quota reached").
Retries cover transient errors. With --fallback-issue, a push that still fails opens a
GitHub issue instead (GitHub emails the repo's watchers), so a risk alert is never
silently dropped. With --soft, a failure prints a workflow warning and exits 0, so the
caller's next steps (e.g. committing the report) still run.
"""
import argparse
import os
import subprocess
import sys
import time

TOPIC_URL = 'https://ntfy.sh/stk-ap-rb-9k4m7q2x'
MAX_BYTES = 3800


def publish(title, body, priority, click, tags, token):
    cmd = ['curl', '-sS', '-w', '\n__HTTP__%{http_code}',
           '-H', f'Title: {title}', '-H', f'Priority: {priority}']
    if click:
        cmd += ['-H', f'Click: {click}']
    if tags:
        cmd += ['-H', f'Tags: {tags}']
    if token:
        cmd += ['-H', f'Authorization: Bearer {token}']
    cmd += ['--data-binary', '@-', TOPIC_URL]
    r = subprocess.run(cmd, input=body.encode(), capture_output=True)
    out = r.stdout.decode(errors='ignore')
    code = out.rsplit('__HTTP__', 1)[-1].strip() if '__HTTP__' in out else '000'
    detail = out.rsplit('__HTTP__', 1)[0].strip()[-300:]
    return code, detail + r.stderr.decode(errors='ignore')[-300:]


def open_issue(title, body):
    r = subprocess.run(['gh', 'issue', 'create', '--title', f'ALERT (ntfy push failed): {title}',
                        '--body', body], capture_output=True, text=True)
    print(r.stdout, r.stderr)
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--title', required=True)
    ap.add_argument('--priority', default='default')
    ap.add_argument('--file')
    ap.add_argument('--message')
    ap.add_argument('--click')
    ap.add_argument('--tags')
    ap.add_argument('--tries', type=int, default=3)
    ap.add_argument('--fallback-issue', action='store_true')
    ap.add_argument('--soft', action='store_true')
    a = ap.parse_args()

    body = a.message if a.message is not None else open(a.file, encoding='utf-8').read()
    full = body
    if len(body.encode()) > MAX_BYTES:
        body = body.encode()[:MAX_BYTES - 100].decode(errors='ignore')
        body += '\n... full report: ' + (a.click or 'see repo')
    token = os.environ.get('NTFY_TOKEN', '')

    for i in range(a.tries):
        code, detail = publish(a.title, body, a.priority, a.click, a.tags, token)
        print(f'ntfy attempt {i + 1}: HTTP {code} ({"token" if token else "anonymous"}) {detail}')
        if code == '200':
            return 0
        if i + 1 < a.tries:
            time.sleep(15 * (i + 1))

    msg = f'ntfy delivery failed after {a.tries} tries: {a.title}'
    if a.fallback_issue and open_issue(a.title, full[:60000]):
        print(f'::warning::{msg}. Opened a GitHub issue instead.')
        return 0
    if a.soft:
        print(f'::warning::{msg}')
        return 0
    print(f'::error::{msg}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
