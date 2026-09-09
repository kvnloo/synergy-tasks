# Idea cycle

Synergy develops in cycles. Each cycle has a planning half and an implementation half. Nothing ships without passing through both.

## Planning half
1. **Ideate 100.** Write 100 distinct ideas across at least eight areas (retention, access, trust, focus, accessibility and language, new briefs, responder tools, the loop itself, community, operations). One line each, no more than 140 characters. Check `ideas/ledger.md` first; an idea already marked `shipped` or `rejected` cannot be re-listed, an idea marked `open` or `deferred` may be re-listed with its original number.
2. **Score every idea.** Four factors, each 1–5:
   - **R Reach** — how many people it can touch in its first month. 1 = maintainers only, 5 = any reader on any device.
   - **I Immediacy** — how soon the effect lands after shipping. 1 = needs partners, adoption, or money first, 5 = the next page load.
   - **D Depth** — how much changes for one person: what they retain, what they can now do, or how well they live. 1 = cosmetic, 5 = changes an outcome.
   - **F Feasibility** — can it ship this cycle with what exists. 1 = needs a backend, spend, or a partner, 5 = a few files, no new dependency.
   - `Score = R × I × D × F` (max 625). Ties: higher D, then the idea that compounds (feeds the loop or a later cycle), then lower effort.
3. **Select three.** Take the three highest scores. Merge each with at most three other ideas from the same list that share a surface (same file, same UI region, same data) and do not pull F below 4.
4. **Write the plan.** `ideas/cycle-NNN.md` holds the table, the selection, and one-line merge rationale. The implementation plan for the three features must be decision-complete: files, anchors, contracts, verification.

## Implementation half
5. **Queue it.** Open one issue per feature in this repository (`Cycle NNN · <feature>`; labels `task`, `priority`, `claimable`, `type:prototype`; body in the task-form layout). The implementer posts a claim. Add roadmap items with `repo: kvnloo/synergy.ai`.
6. **Ship it.** One commit per feature. `main` stays deployable after every commit. Verify each feature with an observable check before starting the next.
7. **Close it.** Comment `Shipped in <repo>@<sha>` plus the observed result, then close the issue. Update `ideas/ledger.md` statuses (`shipped`, `merged into #n`, `deferred`, `rejected`).
8. **Retro.** Add an `Outcome` section to `ideas/cycle-NNN.md`: what shipped, what was cut, what the next cycle should weigh differently. Then start the next planning half.

## Design constraints (apply to every idea)
- No infinite feeds, autoplay, streaks that shame, or notifications.
- Nothing is ranked by money, compute spend, or token holdings.
- Reader data stays on the device unless the reader explicitly sends it.
- Every claim keeps its sources attached; every correction path leads to the task queue.
- Work in bounded blocks; leave the reader with a clear stopping point.
