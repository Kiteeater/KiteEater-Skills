---
name: project-issue-log
description: Record project setup issues, code review findings, implementation course corrections, technical-stack direction changes, and their resolutions into a persistent project log. Use when Codex discovers a non-trivial problem, adjustment, decision, workaround, or fix that should be written down for future sessions instead of left only in chat history.
---

# Project Issue Log

Use this skill to persist notable project friction and its outcome.

## What Counts As A Log-Worthy Entry

Record an entry when work reveals something future sessions could lose without a written note:

- a code review finding that changed code or future work
- a technical direction change or rejected implementation path
- a feature implementation adjustment caused by constraints
- an environment, tooling, build, test, or integration problem
- a workaround that should eventually be removed
- a decision with tradeoffs that will matter later

Skip trivial edits or obvious one-line fixes unless they changed the plan.

## Default Output

Write entries to `docs/project-issue-log.md` in the current workspace.

If the file does not exist, create it with a short heading and start appending entries.

## Entry Shape

Each entry should capture:

- date
- title
- category
- current status
- problem
- solution or decision
- impact
- follow-up, if any

Keep the writing compact and factual. Prefer operational language over narrative.

## Recommended Workflow

1. Decide whether the event is important enough to preserve.
2. Summarize the problem in one or two sentences.
3. Summarize the fix, decision, or chosen direction.
4. Capture the impact on code, architecture, scope, or follow-up work.
5. Append the entry to the project log.

## Preferred Tooling

Use `scripts/log_issue.py` in this skill when possible, because it keeps the format consistent.

Example:

```bash
python3 /absolute/path/to/project-issue-log/scripts/log_issue.py \
  --workspace /path/to/workspace \
  --title "Report status hid rollback failure details" \
  --category "code-review" \
  --status "resolved" \
  --problem "Code review found that teardown failures were collapsed into a generic summary." \
  --solution "Preserved teardown failure detail in the final report and added a focused test." \
  --impact "Future runs now distinguish product failures from environment cleanup failures." \
  --follow-up "Watch for similar status-folding bugs in dynamic evaluation."
```

## If The Script Is Not A Good Fit

Edit `docs/project-issue-log.md` directly, but preserve the same fields and ordering.

## Quality Bar

- Prefer one meaningful entry over many noisy entries.
- Do not hide uncertainty; say when a decision is temporary.
- Record rejected directions when they explain why the chosen path exists.
- Mention file paths only when they materially help future debugging.
