# KiteEater Skills

Public skill repository for AI engineering workflows, architecture coaching, and reusable Codex-style skills.

## Featured Skill

### `ai-architecture-coach`

An architecture-first coaching skill for AI / Agent / RAG / Workflow / Memory / Coding Agent projects.

It is designed for people who do not just want answers or code, but want to build stronger system thinking while solving real project problems.

What it does:
- turns vague "build me an agent" requests into system design questions
- compares architecture options before recommending one
- highlights boundaries, risks, failure modes, and evaluation loops
- teaches the reasoning behind the recommendation
- blocks premature implementation until core architecture analysis is complete

What it is not:
- not a generic Q&A helper
- not a buzzword generator
- not a "just add memory / more agents" assistant
- not a code-first shortcut that skips architecture

## Why This Repo Exists

Many AI project prompts sound like:
- "Help me build a coding agent"
- "Add memory"
- "Make the RAG smarter"
- "Use multi-agent architecture"

Those requests often skip the real engineering work:
- What should the model do vs. tools, APIs, or rules?
- Where is the system boundary?
- What state exists?
- What will fail first?
- How will we know the system is actually better?

This repository packages skills that push the conversation back toward system design, implementation discipline, and engineering judgment.

## Repository Layout

```text
.
├── README.md
├── .gitignore
└── ai-architecture-coach/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── design-spec.md
        ├── modes.md
        ├── output-template.md
        ├── anti-patterns.md
        ├── recovery-playbook.md
        ├── few-shots.md
        └── final-prompts.md
```

## Skill Highlights

`ai-architecture-coach` uses a fixed operating model:

1. `Review Mode`
   When the user already has an architecture, module split, workflow, or draft system.
2. `Architecture Decompose Mode`
   When the user mostly has a goal, a wish, or a vague solution idea.
3. `Implementation Guide Mode`
   Only after the architecture gate passes.
4. `Learning Loop Mode`
   Always closes the answer with compact learning points and next practice.

It also enforces an implementation gate before giving implementation guidance:
- goal is explicit
- system boundary is explicit
- at least 2 approaches were compared
- recommendation and rationale were given
- at least 3 key risks were identified
- MVP scope is defined

## Good Fit

Use this repo if you want skills that help with:
- AI architecture reviews
- agent and workflow design
- RAG debugging and evaluation
- memory design decisions
- coding-agent system decomposition
- engineering mentorship through responses

## Example Prompts

- "Use `$ai-architecture-coach` to review my coding agent architecture."
- "Use `$ai-architecture-coach` to help me decompose a RAG system before implementation."
- "Use `$ai-architecture-coach` to compare workflow vs planner-executor for this tool-using assistant."
- "Use `$ai-architecture-coach` to explain why my current multi-agent design is overcomplicated."

## Start Here

- Main skill entry: [ai-architecture-coach/SKILL.md](./ai-architecture-coach/SKILL.md)
- Full design spec: [ai-architecture-coach/references/design-spec.md](./ai-architecture-coach/references/design-spec.md)
- Reusable prompt versions: [ai-architecture-coach/references/final-prompts.md](./ai-architecture-coach/references/final-prompts.md)
- Response skeleton: [ai-architecture-coach/references/output-template.md](./ai-architecture-coach/references/output-template.md)

## Design Philosophy

This repo favors:
- architecture before implementation
- recommendation before neutrality
- trade-off analysis before buzzwords
- failure-mode thinking before happy-path demos
- evaluation before "it feels smarter"
- user growth alongside practical delivery

If a skill cannot explain why a design should exist, where it will fail, and how to evaluate it, it is not ready.
