# Mentor Explainer Patterns

Use these patterns when the answer needs to be more vivid, more teachable, or easier to remember.

## 1. Job -> Risk -> Fix -> Principle

This is the default pattern for engineering explanations.

Template:
- "This code's real job is ..."
- "The risk before the change was ..."
- "The change fixes that by ..."
- "The deeper principle is ..."

Use this for:
- file walkthroughs
- engineering hardening
- refactors
- infra and boundary-layer code

## 2. What It Looks Like vs What It Really Means

Use when the surface reading is misleading.

Template:
- "On the surface, this looks like ..."
- "But the real issue is ..."

Examples:
- "On the surface, this looks like adding a timeout. But the real change is turning an ambiguous hang into an explicit failure path."
- "On the surface, this looks like moving polling code. But the real change is putting completion logic in the layer that can actually observe completion."

## 3. Why This Layer

Use when explaining architecture or separation of concerns.

Template:
- "This logic belongs here because this layer is the first place that can reliably observe ..."
- "It does not belong in the lower layer because that layer only knows ..."

This pattern is especially useful for:
- host adapters
- service boundaries
- repositories vs domain logic
- controllers vs business services

## 4. Without This, What Goes Wrong

Use to make the risk concrete.

Template:
- "Without this, the system can ..."
- "That leads to ..."

Examples:
- silent hangs
- stale state
- false success
- duplicate work
- rollback gaps
- misleading logs

## 5. Teach The Instinct, Not Just The Patch

Use for code review.

Template:
- "The bug is ..."
- "A junior engineer might miss it because ..."
- "The instinct to build is ..."

This makes the answer feel like mentorship instead of a checklist.

## 6. Aha Lines

Use one, not many. It should sharpen the core idea, not sound theatrical.

Examples:
- "The key distinction is between the API call finishing and the business workflow finishing."
- "This code is buying determinism."
- "The abstraction is doing its job only if the upper layer no longer has to care how messy the host is."
- "The fix is really about ownership: the layer that can observe completion should own completion."

## 7. Plain-Language Rewrites

If a sentence sounds abstract, rewrite it into cause and effect.

Instead of:
"This improves robustness."

Prefer:
"This prevents the pipeline from waiting forever when the host never resolves."

Instead of:
"This refines separation of concerns."

Prefer:
"This moves file-change waiting out of the host adapter and into the pipeline, because only the pipeline knows which files count as proof that repair actually happened."

## 8. Endings That Teach

Close by giving the user a reusable engineering rule.

Examples:
- "When you are choosing where logic belongs, put it in the first layer that can observe the thing you are trying to guarantee."
- "If a dependency can hang, success and failure must both be explicit outcomes."
- "If a signal can lie, pair it with a stronger signal before using it to drive control flow."
