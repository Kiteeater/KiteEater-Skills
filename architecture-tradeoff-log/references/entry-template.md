# Architecture Tradeoff Entry Template

Use this exact shape unless the user asks for a different output.

```md
## [YYYY-MM-DD] Short Title

- Status:
- Impact Scope:

### 1. Discovery
What was discovered, and where did it show up?

### 2. Current State
What does the system look like right now? What is true today?

### 3. Chosen Solution
What was changed or decided?

### 4. Trade-offs And Understanding
Why did this option win? What did it improve? What cost did it introduce?

### 5. Rejected Options
- Option A: Why it was not chosen.
- Option B: Why it was not chosen.

### 6. Final Outcome
Is the problem resolved, partially resolved, or still open?

### 7. Follow-up
What should be watched, cleaned up, or revisited later?
```

## Minimum Standard

Do not leave these vague:

- the actual structural problem
- the reason the chosen solution won
- the downside that was accepted
- the remaining risk

## Good Short Example

```md
## [2026-03-22 14:30] Separate queue ownership from worker execution

- Status: resolved
- Impact Scope: job queue, worker runtime

### 1. Discovery
Retries and queue visibility rules were mixed into worker code.

### 2. Current State
Workers both executed jobs and decided retry timing, which made failure handling inconsistent.

### 3. Chosen Solution
Moved retry policy and visibility timeout handling into the queue layer. Workers now only execute jobs and return results.

### 4. Trade-offs And Understanding
This makes worker behavior simpler and more predictable, but the queue layer now carries more responsibility and needs stronger tests.

### 5. Rejected Options
- Keep retry logic inside each worker: rejected because behavior would keep drifting across workers.
- Add a shared helper and leave ownership split: rejected because ownership would still stay ambiguous.

### 6. Final Outcome
Resolved for the current queue flow. Failure handling is now centralized.

### 7. Follow-up
Watch whether delayed jobs need a separate policy object later.
```
