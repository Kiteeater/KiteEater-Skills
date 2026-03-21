# Modes

Use this file to route requests and keep outputs proportional to the input maturity.

## 1. Scoping Mode

### Trigger

Use when the user mostly has a topic, question, or vague ambition.

Examples:

- "帮我研究这个市场"
- "这个方向值不值得做"
- "我想找机会"

### Goal

Turn a broad ask into:

- one decision question
- three to five assumptions
- a first-pass attack surface
- the next few materials to inspect

### Depth

Keep the response lean. Focus on framing and prioritization, not conclusions.

## 2. Corpus Decode Mode

### Trigger

Use when the user supplied materials, but the decision is still not explicit.

Examples:

- competitor landing pages
- reviews
- earnings call excerpts
- notes from interviews

### Goal

Translate the corpus into:

- what the materials imply
- what assumptions they reveal
- what they still do not prove

### Depth

Summarize only enough to support the judgment structure. Do not produce a document recap.

## 3. Attack Surface Mode

### Trigger

Use when the user already has a thesis, strategy, or opportunity claim and wants it challenged.

Examples:

- "我觉得这个方向值得做，你帮我拆一下"
- "帮我找这个市场的薄弱点"
- "从投资人视角挑战这个想法"

### Goal

Pressure-test the idea by:

- naming hidden assumptions
- defining failure conditions
- surfacing strongest counterarguments
- identifying which evidence would actually settle the debate

### Depth

Bias toward falsification and sharp questions. This mode should feel adversarial in service of better thinking.

## 4. Decision Memo Mode

### Trigger

Use when the user already has enough materials and wants a judgment call.

Examples:

- "基于这些材料帮我形成判断"
- "给我一个阶段性结论"
- "把这些资料整理成可决策的结论"

### Goal

Produce a concise memo with:

- the current read
- evidence-backed claims
- unresolved risks
- the next materials most likely to change the decision

### Depth

This is the deepest mode. Keep the structure stable and bind claims to evidence types whenever possible.

## Mode Switching

Switch upward when the user adds more materials or asks for a stronger judgment.

- `Scoping` -> `Corpus Decode` when meaningful materials appear
- `Corpus Decode` -> `Attack Surface` when the user adds a thesis to challenge
- `Attack Surface` -> `Decision Memo` when there is enough evidence to support a stage judgment

Do not switch downward unless the user explicitly wants a lighter response.

## Completion Rule

A response is complete when it gives the user:

- a clearer decision than they started with
- the assumptions that matter most
- the specific evidence gap that matters next

If the answer only sounds smart but does not change what the user should inspect or decide next, it is not complete.
