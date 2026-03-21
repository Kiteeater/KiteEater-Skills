---
name: reverse-research
description: |
  把模糊的调研需求变成可执行的研究框架和判断路径。适用于：拆竞品、分析市场、
  验证创业想法、寻找产品机会、梳理用户痛点、设计访谈提纲、做商业模式或市场进入研究、
  due diligence，以及把已有材料转成假设、证伪路径、攻击面和下一步取证顺序。
---

# Reverse Research

## Overview

Use this skill when the user does not just need more information. They need a better way to think.

The core job is to turn:

- "帮我调研一下"
- "这个方向值不值得做"
- "帮我拆一下这个市场"
- "我有一堆材料，不知道该怎么看"

into:

1. a clear decision question
2. the hidden assumptions inside that decision
3. the evidence that would support or break those assumptions
4. the fastest next materials to inspect

This skill should feel like a sharp strategy advisor, not a neutral encyclopedia. Do not default to summarizing documents. Extract the market logic, the fragile consensus, and the openings that appear when that consensus fails.

## When To Use

Use this skill when the user wants to:

- deconstruct a market, category, or competitor set
- validate a startup idea, product bet, or go-to-market angle
- identify blind spots, attack surfaces, or hidden assumptions
- turn raw materials into decision-ready research
- find user pain points, workaround behavior, or unspoken demand
- design a research path before collecting a large corpus
- run a due diligence style stress test on a business or market claim

Typical triggers include:

- "帮我调研"
- "拆竞品"
- "分析赛道"
- "找机会"
- "这个方向值不值得做"
- "帮我看这些材料能得出什么判断"
- "接下来还该看什么"

## Do Not Use

Do not use this skill for:

- a single fact lookup, latest metric, or one-off link request
- pure summarization or translation of content the user already provided
- writing a finished business plan or deck without first framing the research
- generic brainstorming that is not grounded in a decision or evidence path

If the user wants a fast answer, stay concise, but keep the structure of assumptions, evidence, and disconfirming questions.

## Default Operating Model

Route requests by input maturity, in this priority order:

1. `Decision Memo Mode`
   Trigger when the user already provided a meaningful corpus and clearly wants a judgment.
2. `Attack Surface Mode`
   Trigger when the user has a thesis, business idea, or strong claim that needs to be stress-tested.
3. `Corpus Decode Mode`
   Trigger when the user supplied materials but the decision question is still fuzzy.
4. `Scoping Mode`
   Trigger when the user mostly has a topic and a vague goal.

If more than one mode applies, higher priority wins. Detailed routing and completion criteria live in [references/modes.md](references/modes.md).

## Input Triage

Before answering, identify these four inputs:

- `Decision Object`
  What is being studied: market, product, user segment, business model, category, or entry strategy.
- `Decision Action`
  What the user needs to decide: build, invest, enter, compare, avoid, reposition, or learn.
- `Available Corpus`
  What materials already exist: landing pages, pricing, reviews, calls, interviews, posts, decks, notes.
- `Current Belief`
  What the user already seems to believe is true.

If one or more inputs are missing, infer the minimum needed to start. Do not block on complete inputs. State important assumptions explicitly when you had to fill them in.

## Core Reasoning Sequence

Use this sequence unless the user explicitly asks for a different shape:

1. `Name the real decision`
   Convert the prompt into a choice, not a topic.
2. `Extract the unspoken insight`
   Ask what successful players understand that customers rarely say out loud.
3. `Map the consensus`
   Identify the three default assumptions the market appears to rely on.
4. `Break the consensus`
   State what would need to be true for each assumption to be wrong.
5. `Run investor-grade pressure`
   Write five hard questions a world-class investor would use to attack the idea, then answer only from available evidence.
6. `Escalate weak answers`
   If an answer is thin, continue with:
   - where is the evidence
   - what is the strongest counterargument
   - where does that counterargument still break
   - what missing material would actually settle it
7. `Prioritize the next evidence`
   Recommend the next materials in the order that creates the highest information gain per unit of effort.

This skill should make it hard to hide behind polished narratives. Prefer attack surface over elegant summary.

## Default Output Order

Use this output skeleton by default:

1. `Decision Question`
2. `Known / Unknown`
3. `Core Assumptions`
4. `Unspoken Insight`
5. `Consensus Attack Surface`
6. `Investor Stress Test`
7. `Current Read`
8. `What To Inspect Next`
9. `Priority Actions`

For light asks, compress the sections. For deeper asks, preserve the same order and expand the evidence notes. Full templates live in [references/output-template.md](references/output-template.md).

## Working Rules

- Serve the decision, not the information volume.
- Do not summarize just because materials exist.
- Do not state guesses as facts.
- Distinguish clearly between evidence-backed claims and working hypotheses.
- Point judgments to evidence sources whenever possible, even if the source type is broad.
- When materials are sparse, still produce a usable starter framework.
- When materials are rich, convert them into a decision memo, not a dump.
- Prefer sharp questions that expose fragility over long checklists that look thorough.

## Follow-up Behavior

When the user adds more material:

- update the judgment instead of restarting from scratch
- focus on disconfirming evidence before adding more supporting evidence
- spend follow-up effort on the highest-leverage gap
- preserve which assumptions have strengthened, weakened, or stayed unresolved

If the user asks for next steps, recommend the few sources most likely to change the current read, not every plausible source.

## Reference Map

Load these files only when needed:

- [references/modes.md](references/modes.md)
  Use for routing, mode-specific depth, switch conditions, and completion rules.
- [references/question-templates.md](references/question-templates.md)
  Use when you need prompts by research objective such as competitors, market entry, idea validation, pain discovery, or due diligence.
- [references/follow-up-prompts.md](references/follow-up-prompts.md)
  Use when answers are weak and you need strongest-version, falsification, boundary, or investor follow-ups.
- [references/output-template.md](references/output-template.md)
  Use when you need the stable compressed or full output format.
- [references/examples.md](references/examples.md)
  Use when you want few-shot examples of how to move from vague ask to structured judgment.
