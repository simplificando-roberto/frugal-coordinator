---
name: frugal-coordinator
description: Coordinate bounded work through cheaper models while retaining authority, safety, and final verification.
---

# Frugal coordinator

Use this skill when a costly primary model coordinates engineering, research, or operational work and cheaper models can complete bounded parts. It is for a coordinator, not a generic parallel-agent workflow. Do not use it when the task is truly small, inseparable from the current turn, or requires authority that cannot be delegated.

## Coordinator protocol

1. State the objective, constraints, acceptance checks, and the next irreversible decision. Keep only these, concise status, and references in the coordinator context.
2. Make a turn budget before reading broadly. A practical starting point is eight tool calls, 80K context tokens, one compaction, and 20K tool-result tokens. Treat these as adjustable limits, not universal facts.
3. Delegate research, inventory, summaries, routine review, bounded scripts, and contained fixes. Each leaf gets a closed prompt, only the inputs it needs, a permission boundary, a time or cost limit, and an output contract.
4. Keep secrets, credentials, remote access, production changes, irreversible decisions, and final verification with the coordinator. Completion from a delegate never authorizes an external action.
5. Start each durable workflow once. Record its run identifier and use the configured durable wait command. Do not poll with model turns, repeated status calls, short sleeps, or monitoring subagents.
6. Read a cheap digest or a narrow range before opening full logs, long documents, or complete diffs. Preserve evidence, not raw output.
7. Verify artifacts, diffs, tests, and external effects yourself before reporting success. A budget exhaustion or partial artifact is not success.

## Decide whether to delegate

Delegate when the work has a clear output, can use a limited input set, is routine or independently checkable, and does not need retained authority. Prefer direct work when writing the brief would cost more than the task, when the result depends on live decisions in this turn, or when a secret or irreversible operation is involved.

Use fan-out only for independent leaves. Give each leaf a separate ownership boundary. Use a stronger child only for genuine ambiguity, architecture, or adjudication between conflicting evidence.

## Context and call budgets

Keep the coordinator's context to the task contract, short state, decisions, and references such as paths or workflow IDs. Do not forward the whole conversation by default. Read files by relevant range or search result. Ask a cheap leaf for a bounded digest before admitting a long artifact to the primary context.

Declare workflow limits for node count, concurrency, wall time, estimated cost where available, depth, and continuation turns. Stop or re-plan at a limit. Count generated output, cache use, and reasoning separately where the platform reports them. Do not claim a parent's accumulated usage as a leaf's cost.

## Example model levels

This table is only an example. Replace every entry during adoption.

| Level | Example models | Suitable work |
| --- | --- | --- |
| Strong | gpt-5.6-sol | Architecture, ambiguous tradeoffs, final adjudication |
| Medium | gpt-5.6-terra | Bounded implementation and integration with tests |
| Cheap | gpt-5.6-luna, GLM Flash | Research, extraction, classification, routine review, and digests |

## Adapt this skill

Change all of the following for your team:

- Models assigned to strong, medium, and cheap levels.
- Per-turn coordinator budgets for tool calls, context, compactions, and tool output.
- The delegation tool and its workflow, validation, start, digest, and status commands.
- The canonical instruction-file name and any wrapper-file name.
- The durable wait command, its timeout, and how completion is reported.

Copy and adapt [assets/adaptation-checklist.md](assets/adaptation-checklist.md) before enforcing this skill across repositories.

## Read the detailed references when needed

- For the full protocol and token rationale, read [references/coordinator-protocol.md](references/coordinator-protocol.md).
- For a canonical instruction file, wrapper, and idempotent propagation, read [references/instruction-layering.md](references/instruction-layering.md).
- For briefs, model levels, durable waits, digests, and fan-out, read [references/delegation-patterns.md](references/delegation-patterns.md).

