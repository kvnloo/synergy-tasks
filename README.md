# Synergy task queue

This repository is the public humanitarian task queue for [Synergy](https://kvnloo.github.io/synergy.ai/), operated under the [Verified OSS Loop](https://github.com/kvnloo/verified-oss-loop). Code contributions are Apache-2.0. Briefs and other editorial text are CC-BY-4.0.

## The loop

1. Maintainers publish a roadmap.
2. Maintainers prioritize an issue queue.
3. A contributor takes a bounded claim lease.
4. Work happens on an isolated branch or worktree.
5. The contributor submits an implementation and evidence receipt.
6. An independent contributor verifies the exact revision.
7. A maintainer makes the human merge decision.
8. The outcome feeds the next roadmap revision.


## Cycles

Direction comes from idea cycles: 100 ideas, scored for reach, immediacy, depth, and feasibility; the top three ship each cycle. See `docs/CYCLE.md` and `ideas/`.

## Claim a task

Choose an open issue labeled `claimable` and post this comment. The default lease is 72 hours and the maximum is 168 hours.

```yaml
# verified-oss-loop claim
issue: 12
claimant: your-github-login
base_revision: sha-of-main-at-claim-time
claimed_at: 2026-09-08T12:00:00Z
expires_at: 2026-09-11T12:00:00Z
scope: one sentence describing the bounded work
work_url: pending
harness: codex
```

Valid harnesses are `codex`, `hermes`, `omp`, `claude`, and `manual`. Post `/release` to return your current claim.

## Submit work

Put deliverables under `contributions/<issue>/`, open a pull request that fixes the issue, and include a receipt bound to the final commit:

```yaml
# verified-oss-loop receipt
issue: 12
base_revision: <sha>
head_revision: <sha>
changed_files: []
policy_revision: <sha of CONTRIBUTING.md at run time>
tests:
  red: "n/a: research deliverable"
  green: "n/a: research deliverable"
  sabotage: "n/a"
builds: []
runtime_evidence: []
security_checks: []
resource_usage:
  wall_seconds: 0
  tokens: null
  api_cost_estimate: null
limitations: []
ai_assistance: "manual run by <login>; human reviewed before submission: yes"
```

An independent reviewer posts one verdict bound to the current head: `APPROVE_EXACT_HEAD`, `CHANGES_REQUIRED`, `DISCARD_DUPLICATE`, `DISCARD_WRONG_DIRECTION`, or `BLOCKED_EXTERNAL`. Reviewers cannot review their own pull requests. Maintainers alone merge.

## No pay-to-win

Priority never depends on compute spend, token holdings, payment, or subscription tier. Maintainers set direction according to humanitarian value, evidence, safety, and feasibility.
