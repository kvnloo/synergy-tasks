#!/usr/bin/env python3
"""Verified OSS Loop GitHub event handlers (stdlib + PyYAML)."""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = os.environ.get("GITHUB_REPOSITORY", "kvnloo/synergy-tasks")
TOKEN = os.environ["GITHUB_TOKEN"]
API = "https://api.github.com"
VERDICTS = {
    "APPROVE_EXACT_HEAD": "approved-exact-head",
    "CHANGES_REQUIRED": "changes-required",
    "DISCARD_DUPLICATE": "discard-duplicate",
    "DISCARD_WRONG_DIRECTION": "discard-wrong-direction",
    "BLOCKED_EXTERNAL": "blocked-external",
}


def api(method: str, path: str, data=None):
    body = None if data is None else json.dumps(data).encode()
    req = urllib.request.Request(API + path, body, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as response:
        raw = response.read()
        return json.loads(raw) if raw else None


def event():
    return json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())


def parse_block(body: str, kind: str):
    pattern = rf"```yaml\s*\n# verified-oss-loop {kind}\s*\n(.*?)\n```"
    match = re.search(pattern, body or "", re.DOTALL)
    if not match:
        return None
    value = yaml.safe_load(match.group(1)) or {}
    if not isinstance(value, dict):
        return None
    # PyYAML turns RFC3339 into datetime; normalize back to strings for JSON/markers.
    for key, item in list(value.items()):
        if isinstance(item, datetime):
            value[key] = item.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return value


def labels(issue):
    return {item["name"] for item in issue.get("labels", [])}


def set_labels(number: int, add=(), remove=()):
    issue = api("GET", f"/repos/{REPO}/issues/{number}")
    names = (labels(issue) - set(remove)) | set(add)
    api("PUT", f"/repos/{REPO}/issues/{number}/labels", {"labels": sorted(names)})


def comment(number: int, body: str):
    api("POST", f"/repos/{REPO}/issues/{number}/comments", {"body": body})


def iso(value):
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def claim_marker(comments):
    marker = re.compile(r"<!-- synergy-claim (\{.*?\}) -->")
    for item in reversed(comments or []):
        match = marker.search(item.get("body") or "")
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                continue
    return None


def open_pr_for(issue: int):
    """Return an open PR whose body contains Fixes #<issue>, else None.

    Uses the pulls list API (not search) so issue numbers cannot false-positive.
    """
    pattern = re.compile(rf"\bFixes\s+#{int(issue)}\b", re.I)
    pulls = api("GET", f"/repos/{REPO}/pulls?state=open&per_page=100") or []
    for pull in pulls:
        if pattern.search(pull.get("body") or ""):
            return pull
    return None


def handle_claim():
    ev = event(); issue = ev["issue"]; number = issue["number"]
    body = (ev["comment"].get("body") or "").strip(); actor = ev["comment"]["user"]["login"]
    if body == "/release":
        marker = claim_marker(api("GET", f"/repos/{REPO}/issues/{number}/comments?per_page=100"))
        if marker and marker.get("claimant") == actor and "claimed" in labels(issue):
            set_labels(number, ["claimable"], ["claimed"]); comment(number, "Released.")
        return
    claim = parse_block(body, "claim")
    if not claim:
        return
    error = None
    try:
        if int(claim.get("issue", 0)) != number:
            error = "Claim issue does not match this issue."
        elif claim.get("claimant") != actor:
            error = "Claimant must match the comment author."
        elif "claimable" not in labels(issue) or "claimed" in labels(issue):
            error = "Task is not claimable right now."
        elif iso(claim["expires_at"]) <= iso(claim["claimed_at"]):
            error = "Claim expiry must follow claim time."
        elif (iso(claim["expires_at"]) - iso(claim["claimed_at"])).total_seconds() > 168 * 3600:
            error = "Claim lease exceeds 168 hours."
        else:
            existing = open_pr_for(number)
            if existing:
                error = f"DISCARD_DUPLICATE: PR #{existing['number']} already covers this issue."
    except (KeyError, TypeError, ValueError):
        error = "Claim fields or RFC3339 timestamps are invalid."
    if error:
        comment(number, error); return
    marker_data = {key: claim[key] for key in ("claimant", "expires_at", "harness", "claimed_at")}
    marker = json.dumps(marker_data, separators=(",", ":"))
    set_labels(number, ["claimed"], ["claimable"])
    comment(number, f"Claim accepted until {claim['expires_at']} (UTC). Post `/release` to give it back.\n\n<!-- synergy-claim {marker} -->")


def handle_expire():
    issues = api("GET", f"/repos/{REPO}/issues?state=open&labels=claimed&per_page=100")
    now = datetime.now(timezone.utc)
    for issue in issues:
        comments = api("GET", f"/repos/{REPO}/issues/{issue['number']}/comments?per_page=100")
        marker = claim_marker(comments)
        if marker and iso(marker["expires_at"]) < now and not open_pr_for(issue["number"]):
            set_labels(issue["number"], ["claimable"], ["claimed"])
            comment(issue["number"], "Claim expired; the task is back in the queue.")


def handle_receipt():
    pr = event()["pull_request"]; number = pr["number"]
    receipt = parse_block(pr.get("body") or "", "receipt") or {}
    missing = []
    for key in ("issue", "base_revision", "head_revision", "changed_files", "ai_assistance"):
        if key not in receipt: missing.append(key)
    tests = receipt.get("tests") or {}
    for key in ("red", "green"):
        if key not in tests: missing.append(f"tests.{key}")
    issue_number = receipt.get("issue")
    if issue_number and not re.search(rf"\bFixes\s+#{int(issue_number)}\b", pr.get("body") or "", re.I):
        missing.append(f"Fixes #{issue_number}")
    if receipt.get("head_revision") != pr["head"]["sha"]:
        missing.append(f"head_revision {receipt.get('head_revision')} does not match PR head {pr['head']['sha']} — update the receipt after every push")
    try:
        linked = api("GET", f"/repos/{REPO}/issues/{int(issue_number)}") if issue_number else None
        if not linked or linked["state"] != "open" or "claimed" not in labels(linked): missing.append("linked issue must be open and claimed")
    except (ValueError, urllib.error.HTTPError): missing.append("linked issue is invalid")
    if missing:
        set_labels(number, ["blocked"], ["needs-review"]); comment(number, "Receipt incomplete:\n- " + "\n- ".join(missing))
    else:
        set_labels(number, ["needs-review"], ["blocked"]); comment(number, f"Receipt complete for {pr['head']['sha']}. Waiting for an independent review verdict.")


def handle_review():
    ev = event()
    if "pull_request" not in ev["issue"]: return
    review = parse_block(ev["comment"].get("body") or "", "review")
    if not review: return
    number = ev["issue"]["number"]; pr = api("GET", f"/repos/{REPO}/pulls/{number}")
    if ev["comment"]["user"]["login"] == pr["user"]["login"]:
        comment(number, "Reviewer must not be the author (Verified OSS Loop §6)."); return
    if review.get("head_revision") != pr["head"]["sha"]:
        comment(number, "Review head_revision does not match the current PR head."); return
    verdict = review.get("verdict")
    if verdict not in VERDICTS:
        comment(number, "Unknown review verdict."); return
    set_labels(number, [VERDICTS[verdict]], VERDICTS.values())


def field(body: str, label: str):
    match = re.search(rf"^### {re.escape(label)}\s*\n\s*\n(.*?)(?=\n### |\Z)", body or "", re.M | re.S)
    return match.group(1).strip() if match else ""


def handle_learn():
    ev = event(); pr = ev["pull_request"]
    match = re.search(r"\bFixes\s+#(\d+)\b", pr.get("body") or "", re.I)
    if not match: return
    issue_number = int(match.group(1)); path = f"receipts/{issue_number}.yaml"
    try:
        api("GET", f"/repos/{REPO}/contents/{path}"); return
    except urllib.error.HTTPError as exc:
        if exc.code != 404: raise
    issue = api("GET", f"/repos/{REPO}/issues/{issue_number}")
    result = "KEEP" if pr.get("merged") else "DISCARD"
    record = {"hypothesis": field(issue.get("body", ""), "Solution hypothesis"), "result": result,
              "observed_evidence": [pr["html_url"], pr.get("merge_commit_sha")], "regressions": [],
              "reusable_lesson": "", "roadmap_effect": "none"}
    import base64
    content = yaml.safe_dump(record, sort_keys=False).encode()
    api("PUT", f"/repos/{REPO}/contents/{path}", {"message": f"receipt: #{issue_number} {result}", "content": base64.b64encode(content).decode(), "branch": "main",
        "committer": {"name": "github-actions[bot]", "email": "41898282+github-actions[bot]@users.noreply.github.com"}})


if __name__ == "__main__":
    {"claim": handle_claim, "expire": handle_expire, "receipt": handle_receipt,
     "review": handle_review, "learn": handle_learn}[sys.argv[1]]()
