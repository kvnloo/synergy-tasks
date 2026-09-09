# Cycle 001 — 2026-09-09

## Ideas

| # | Idea | R | I | D | F | Score | Status |
|---|---|---|---|---|---|---|---|
| 1 | Recall prompts per brief: one cue per slide plus a chain rebuild; reveal, then self-grade | 5 | 5 | 4 | 5 | 500 | shipped |
| 2 | "Due today" recall queue on the home page from the self-grades, scheduled on the device | 4 | 4 | 4 | 5 | 320 | merged into #1 |
| 3 | Priming line on slide 1: the five questions this brief answers, shown before reading | 4 | 4 | 3 | 5 | 240 | merged into #1 |
| 4 | Chain-rebuild drill: shuffled chain steps to put back in order | 4 | 4 | 4 | 4 | 256 | open |
| 5 | Two-sentence explanation box after reading, compared against the brief summary | 4 | 4 | 4 | 5 | 320 | open |
| 6 | "Next brief" picks a different topic than the last one read | 3 | 3 | 2 | 5 | 90 | open |
| 7 | Honest retention ledger: claims recalled this month, device-only | 3 | 3 | 2 | 5 | 90 | open |
| 8 | Export recall prompts as CSV for flashcard apps | 3 | 4 | 3 | 5 | 180 | open |
| 9 | Progressive prompts: cue → free recall → apply to a new country | 3 | 3 | 4 | 4 | 144 | open |
| 10 | "How to read a brief" sixty-second onboarding | 5 | 5 | 3 | 5 | 375 | merged into #1 |
| 11 | Installable app; whole site works offline after the first visit | 5 | 5 | 4 | 4 | 400 | shipped |
| 12 | Open data: `data/briefs.json` export of every brief, CC-BY-4.0 | 4 | 4 | 3 | 5 | 240 | merged into #11 |
| 13 | Share metadata so links preview cleanly in messaging apps | 5 | 5 | 2 | 4 | 200 | merged into #11 |
| 14 | Data-saver mode: skip webfonts and animation on slow connections | 5 | 4 | 2 | 4 | 160 | open |
| 15 | Print/PDF brief pack with sources for offline teaching | 4 | 4 | 3 | 4 | 192 | open |
| 16 | RSS/Atom feed of briefs | 3 | 5 | 2 | 5 | 150 | open |
| 17 | QR poster per brief for clinics and classrooms | 3 | 4 | 2 | 5 | 120 | open |
| 18 | Embeddable brief widget for partner sites | 4 | 3 | 3 | 3 | 108 | open |
| 19 | One-command self-host mirror for intranets | 3 | 3 | 3 | 4 | 108 | open |
| 20 | SMS/USSD brief digest | 5 | 2 | 3 | 1 | 30 | open |
| 21 | "Flag a problem" on every slide, routed to the brief's open verify-evidence task | 5 | 5 | 3 | 5 | 375 | shipped |
| 22 | "Verify this source" three-minute micro-task: supports/contradicts plus the exact passage | 4 | 5 | 4 | 4 | 320 | merged into #21 |
| 23 | "One claim to check today" on the home page | 4 | 5 | 3 | 5 | 300 | merged into #21 |
| 24 | Last-reviewed date on every brief | 5 | 5 | 2 | 5 | 250 | merged into #21 |
| 25 | Evidence type badges: guidance, peer-reviewed, reporting, dataset | 5 | 4 | 4 | 4 | 320 | open |
| 26 | Strongest counter-evidence field per slide | 4 | 4 | 4 | 3 | 192 | open |
| 27 | Change log per brief, including retractions | 4 | 4 | 3 | 4 | 192 | open |
| 28 | Source link liveness check in CI | 4 | 5 | 3 | 5 | 300 | open |
| 29 | Archive snapshot link per source | 4 | 4 | 3 | 4 | 192 | open |
| 30 | Sentence-level anchors into source passages | 4 | 2 | 5 | 2 | 80 | open |
| 31 | Focus reader: hide chrome, optional 25-minute block | 4 | 4 | 3 | 5 | 240 | open |
| 32 | "You're done for today" end state; no infinite scroll, ever | 4 | 5 | 2 | 5 | 200 | open |
| 33 | Ninety-minute deep session: three briefs plus recall, then a break cue | 3 | 3 | 3 | 4 | 108 | open |
| 34 | Read-later list exported as a calendar file, never a notification | 3 | 3 | 2 | 4 | 72 | open |
| 35 | Weekly rhythm marker instead of daily streaks | 3 | 3 | 2 | 5 | 90 | open |
| 36 | Opt-in paced auto-advance in the reader | 2 | 3 | 2 | 4 | 48 | open |
| 37 | Reduced-motion audit across all animations | 3 | 4 | 2 | 5 | 120 | open |
| 38 | Single-task whiteboard mode | 2 | 3 | 2 | 4 | 48 | open |
| 39 | Session summary card on close: read, recall next | 3 | 4 | 3 | 4 | 144 | open |
| 40 | Keyboard-first navigation audit | 3 | 4 | 2 | 5 | 120 | open |
| 41 | Read-aloud via browser speech synthesis | 4 | 5 | 3 | 5 | 300 | open |
| 42 | Dyslexia-friendly type and spacing toggle | 3 | 5 | 2 | 5 | 150 | open |
| 43 | Screen-reader and keyboard audit of the reader dialog | 4 | 5 | 3 | 4 | 240 | open |
| 44 | Plain-language variant per slide | 5 | 3 | 3 | 2 | 90 | open |
| 45 | Inline glossary for humanitarian terms | 5 | 5 | 2 | 5 | 250 | open |
| 46 | i18n scaffold plus first community translation | 5 | 3 | 5 | 2 | 150 | open |
| 47 | Right-to-left layout support | 4 | 3 | 3 | 3 | 108 | open |
| 48 | Community translation UI that outputs a PR-ready file | 4 | 3 | 4 | 3 | 144 | open |
| 49 | Multilingual glossary | 4 | 3 | 3 | 3 | 108 | open |
| 50 | High-contrast theme | 3 | 5 | 2 | 5 | 150 | open |
| 51 | Brief: sleep as public-health infrastructure (shift work, heat, light) | 5 | 4 | 4 | 4 | 320 | open |
| 52 | Brief: psychological first aid in crises | 5 | 4 | 4 | 4 | 320 | open |
| 53 | Brief: micronutrient deficiency chains in food insecurity | 5 | 3 | 4 | 3 | 180 | open |
| 54 | Brief: vaccine cold-chain logistics | 5 | 3 | 4 | 3 | 180 | open |
| 55 | Brief: household air pollution and clean cooking | 5 | 3 | 4 | 3 | 180 | open |
| 56 | Brief: road traffic injury, leading killer of ages 5–29 | 5 | 3 | 4 | 3 | 180 | open |
| 57 | Brief: water, sanitation, and child mortality | 5 | 3 | 4 | 3 | 180 | open |
| 58 | Brief: urban air pollution and healthspan | 5 | 3 | 4 | 3 | 180 | open |
| 59 | Brief: tobacco control policy transfer | 4 | 3 | 4 | 3 | 144 | open |
| 60 | Brief: movement and physical activity in low-resource settings | 4 | 3 | 3 | 3 | 108 | open |
| 61 | Printable heat-safety checklist for outdoor workers | 4 | 4 | 3 | 4 | 192 | open |
| 62 | Work/rest schedule calculator for heat | 3 | 3 | 3 | 3 | 81 | open |
| 63 | Sleep protocol checklist for shift responders | 4 | 3 | 3 | 3 | 108 | open |
| 64 | Micronutrient quick reference for field workers | 3 | 2 | 3 | 3 | 54 | open |
| 65 | Language Relay failure-mode checklist as an interactive tool | 3 | 3 | 3 | 4 | 108 | open |
| 66 | Needs Map research questionnaire as a static form that files an issue | 3 | 3 | 3 | 4 | 108 | open |
| 67 | Displacement definitions-versus-numbers explainer widget | 3 | 3 | 3 | 3 | 81 | open |
| 68 | Source Kit: paste URLs, get a cited packet with retrieval dates | 4 | 4 | 4 | 4 | 256 | open |
| 69 | Hypothesis quality checker (user, mechanism, measure, stop condition) | 3 | 4 | 3 | 5 | 180 | open |
| 70 | Prototype template gallery (alert, checklist, referral map) | 3 | 3 | 3 | 3 | 81 | open |
| 71 | Micro-task lane on the board: five-minute tasks beside forty-five-minute ones | 4 | 4 | 4 | 4 | 256 | open |
| 72 | Time estimates on task cards | 4 | 4 | 2 | 5 | 160 | open |
| 73 | Board filters by brief, type, and time | 3 | 4 | 2 | 5 | 120 | open |
| 74 | Duplicate-task detector before proposing | 3 | 4 | 3 | 4 | 144 | open |
| 75 | Brief JSON schema so write-brief tasks produce valid content | 4 | 4 | 4 | 4 | 256 | open |
| 76 | `scripts/import_brief.py`: contributions folder into `content.js` | 4 | 3 | 4 | 4 | 192 | open |
| 77 | Impact counter on the home page | 4 | 4 | 2 | 5 | 160 | open |
| 78 | Contributor page built from `board.json` | 3 | 3 | 2 | 5 | 90 | open |
| 79 | "Verified by" credits in the brief footer | 3 | 4 | 2 | 4 | 96 | open |
| 80 | Daily intake run from `docs/INTAKE.md` | 3 | 3 | 3 | 3 | 81 | open |
| 81 | Persist whiteboard drafts on the device (memory-only today) | 4 | 5 | 3 | 5 | 300 | open |
| 82 | Export whiteboard as PNG | 2 | 3 | 2 | 4 | 48 | open |
| 83 | Propose → claim → run in one flow from the whiteboard | 2 | 3 | 3 | 3 | 54 | open |
| 84 | Claude Code adapter end-to-end check | 2 | 2 | 2 | 2 | 16 | open |
| 85 | Worker verify-lane UI polish | 2 | 3 | 2 | 4 | 48 | open |
| 86 | Graduate tasks to per-project repositories | 2 | 2 | 3 | 3 | 36 | open |
| 87 | Jurisdiction power-map cards per country | 4 | 2 | 4 | 2 | 64 | open |
| 88 | Board freshness through an edge worker | 2 | 2 | 1 | 2 | 8 | open |
| 89 | Rotating brief maintainers ("adopt a brief") | 2 | 2 | 3 | 3 | 36 | open |
| 90 | Test suite for `app.js` modules with `node --test` | 2 | 3 | 2 | 4 | 48 | open |
| 91 | Volunteer onboarding page: three paths (verify, donate compute, write) | 4 | 5 | 3 | 5 | 300 | open |
| 92 | Code of conduct and safety guide | 3 | 4 | 2 | 5 | 120 | open |
| 93 | Public changelog generated from git history | 3 | 4 | 1 | 5 | 60 | open |
| 94 | Lighthouse and accessibility check in CI | 3 | 4 | 2 | 5 | 120 | open |
| 95 | Performance budget: under 100 KB of JS, no blocking fonts | 4 | 4 | 2 | 4 | 128 | open |
| 96 | Explicit no-tracking statement and subresource integrity | 3 | 5 | 1 | 5 | 75 | open |
| 97 | Sitemap and metadata for discoverability | 4 | 4 | 1 | 5 | 80 | open |
| 98 | Newsletter wired to a provider | 3 | 2 | 2 | 2 | 24 | open |
| 99 | Discussion link per brief for open questions | 3 | 4 | 2 | 5 | 120 | open |
| 100 | Office-hours page with a static schedule | 2 | 3 | 2 | 5 | 60 | open |

### Selection
- Top scores: #1 (500), #11 (400), then #21 and #10 tied at 375. Tie-break: D equal (3); #21 compounds (every flag feeds the verify-evidence queue) → **#21 selected**, #10 merged into F1.
- **F1 Retain what you read** = #1 + #2 + #3 + #10. Same surface: reader dialog + home. Rationale: reading without retrieval decays within days; a cue per slide plus a spaced return turns a seven-minute read into knowledge someone can use.
- **F2 Works anywhere** = #11 + #12 + #13. Same surface: shell files + head. Rationale: the people these briefs are about often have the worst connectivity; offline-first plus open data is the cheapest reach multiplier available.
- **F3 Fix what's wrong in three minutes** = #21 + #22 + #23 + #24. Same surface: evidence drawer + home + `content.js`. Rationale: trust compounds only if correction is cheaper than complaint; every reader becomes a verifier without a subscription.

## Outcome

Shipped:
- **F1 Retain what you read** (ideas #1+#2+#3+#10) in `kvnloo/synergy.ai@ddf90a3` — six prompts per brief, device-local grades, due strip on home.
- **F2 Works anywhere** (ideas #11+#12+#13) — service worker shell, install manifest, `data/briefs.json` CC-BY-4.0, share metadata.
- **F3 Fix what's wrong in three minutes** (ideas #21+#22+#23+#24) — reviewed dates, per-source verify form, home claim-of-the-day, correction path into the task queue.

Cut: none. All three features shipped as scoped.

Weighting for cycle 002: new briefs scored high on reach × depth but feasibility stayed at 3; batch one content-only brief as a fourth item when F stays ≥4 for the code features, or accept a two-feature code cycle plus one brief. Trust tooling (evidence badges, source liveness) is the next compounding surface after F3.
