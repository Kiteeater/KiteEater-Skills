---
name: architecture-tradeoff-log
description: Record architecture gaps, design trade-offs, rejected options, and final decisions during project setup or implementation. Use when Codex finds a structural problem, unclear boundary, risky dependency, scaling concern, or a non-trivial design choice that should be preserved for later review.
---

# Architecture Tradeoff Log

Use this skill to preserve design judgment, not just outcomes.

This skill is for moments when the project exposes a real structural issue: weak boundaries, messy ownership, risky dependencies, scaling concerns, temporary fixes turning permanent, or a design choice that will matter later.

Do not use it for trivial bug fixes, formatting changes, or obvious one-step edits with no real trade-off.

## What Counts As Log-Worthy

Record an entry when at least one of these is true:

- module boundaries are unclear or conflicting
- data flow is indirect, duplicated, or hard to reason about
- a dependency choice could lock the project into a bad path later
- a temporary workaround is becoming part of the design
- the original approach was rejected for a meaningful reason
- the chosen solution solves one problem while creating a new cost

If the issue is local, obvious, and has no lasting design impact, skip it.

## Default Output

Write entries to `docs/architecture-tradeoff-log.md` in the current workspace.

If the file does not exist, create it and append entries in chronological order.

Use `scripts/log_tradeoff.py` when possible so the entry shape stays consistent.

## Required Entry Shape

Every entry must include these sections in this order:

1. Discovery
2. Current State
3. Chosen Solution
4. Trade-offs And Understanding
5. Rejected Options
6. Final Outcome
7. Follow-up

Also include these short fields near the top:

- date
- title
- status
- impact scope

Recommended status values:

- `open`
- `partial`
- `resolved`
- `temporary`

Detailed wording template lives in [references/entry-template.md](references/entry-template.md).

## Operating Rules

Follow this sequence:

1. Decide whether the issue is structural enough to preserve.
2. State the current situation in plain language.
3. Name the actual problem, not just the symptom.
4. Record the solution that was chosen.
5. Record at least one rejected option and why it lost.
6. Explain the gain and the cost of the chosen path.
7. State whether the issue is resolved, partial, or still open.
8. Append the entry to `docs/architecture-tradeoff-log.md`.

## Preferred Tooling

Use the bundled script when you can:

```bash
python3 /absolute/path/to/architecture-tradeoff-log/scripts/log_tradeoff.py \
  --workspace /path/to/workspace \
  --title "Split orchestration from provider calls" \
  --status "resolved" \
  --impact-scope "evaluation pipeline, adapter layer" \
  --discovery "The pipeline mixed orchestration rules with provider-specific request code." \
  --current-state "Pipeline steps were tightly coupled to one provider shape, which made retries and provider swaps hard." \
  --chosen-solution "Moved provider-specific request building into adapters and kept orchestration in the pipeline layer." \
  --tradeoffs "This improves boundaries and future swaps, but adds one more abstraction layer to maintain." \
  --rejected-option "Keep the current shape and patch special cases. Rejected because the coupling would keep growing." \
  --final-outcome "Resolved for the current pipeline. Provider logic is now isolated behind adapters." \
  --follow-up "Watch whether adapter interfaces stay small as more providers are added."
```

If the script is not a good fit, append the entry manually, but preserve the same field order and section names.

## Writing Rules

- Keep it concrete. Avoid theory words unless they point to a real code or system boundary.
- Prefer "module A owns X, module B also writes X" over vague claims like "responsibilities are blurry."
- Always include both upside and downside for the chosen solution.
- Do not pretend the chosen solution is perfect.
- If the decision is temporary, say so directly.
- If you are unsure, write "uncertain, but more likely X because Y."

## Quality Bar

A good entry lets a future session answer these questions fast:

- what was broken in the structure
- what options were considered
- why the chosen path won
- what cost was accepted
- what risk still remains

If the entry cannot answer those five questions, rewrite it shorter and clearer.

## Done Condition

This skill is done only when:

- the issue is confirmed to be structural enough to record
- the chosen solution is named clearly
- at least one rejected option is written down
- the downside of the chosen path is stated directly
- the log entry has been appended to `docs/architecture-tradeoff-log.md`
