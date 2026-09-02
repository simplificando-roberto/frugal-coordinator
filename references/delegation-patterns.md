# Delegation patterns

## Model levels

Configure levels by capability and cost, not provider name. Cheap leaves handle research, extraction, classification, routine review, and digests. Medium leaves handle a narrow implementation or integration task with tests. Strong leaves handle architecture, unresolved ambiguity, and adjudication. The coordinator should not create a strong child merely to repeat its own planning.

Choose the smallest level that can meet the output contract. A model that only reports usage after completion cannot enforce a native token ceiling. In that case use observable limits such as node count, wall time, continuation count, and cost reporting where available.

## Shared brief with context cuts

Write one Markdown brief from [the template](../assets/brief-template.md). It separates objective, current state, facts, conventions, verification, constraints, and output contract. Each leaf receives only the sections it needs plus a short delta prompt. For example, a research leaf may need objective, facts, and constraints, while an implementation leaf also needs verification and output contract.

Section cuts prevent repeated background from being copied into every prompt. Keep headings stable and use exact section names. If the delegation tool cannot select sections natively, generate a small per-leaf excerpt before dispatch.

## Durable waits and cheap digests

Start a workflow once and record its ID. Use `<durable-wait-command> <workflow-id>` through a background task, callback, or a single blocking wait with a meaningful timeout. Do not poll with short waits, repeated status requests, or model prompts.

When a child produces a large log, diff, or artifact, route it to a cheap digest leaf. Ask for a fixed-size answer with key facts, evidence references, risks, and open questions. The coordinator then reads the digest first and opens only the narrow source range needed for a decision.

## Fan-out and review

Fan out independent leaves with different questions or file ownership. Bound concurrency so a large queue does not turn into uncontrolled spend. Give write-capable leaves isolated workspaces and explicit file boundaries. Do not fan out dependent steps until the required prior artifact exists.

The parent reviews each artifact, diff, and test result. Completed leaves do not authorize an external side effect. If leaves disagree, compare their evidence first. Escalate only the disputed point to a stronger model when that is cheaper than having the coordinator reconstruct all context.

## Example leaf prompts

Research leaf:

```text
Objective: <answer one checkable question>.
Inputs: <paths, brief sections, or references>. Do not edit or poll.
Return: <short result format with evidence and uncertainties>. Stop after <limit>.
```

Implementation leaf:

```text
Objective: <bounded change>.
Scope: <allowed files and workspace>. Verify with <command or check>.
Return: <summary, changed files, verification, and risks>. Do not take external actions.
```

