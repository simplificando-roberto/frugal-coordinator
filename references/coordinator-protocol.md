# Coordinator protocol

## Purpose

The expensive model owns direction and accountability. Cheaper models do bounded work that can be reviewed. This division saves tokens because the expensive model does not repeatedly absorb repository history, long logs, or routine investigation.

## Before a turn

Write a compact task state:

- Objective and acceptance checks.
- Constraints and permission boundaries.
- Decisions already made and the next decision that needs judgment.
- References to inputs, artifacts, and workflow IDs.

Set a call and context budget. A measured configuration used eight tool calls per turn, with twelve only when justified, 80K context tokens, one compaction, and 20K tool-result tokens. Teams must tune these values. The point is a stopping rule: summarize or delegate before the coordinator expands its context without a purpose.

Frequent calls are expensive even when individual commands are small. Compaction also rebuilds context. Avoid opening complete instruction files, runbooks, logs, artifacts, and diffs in the coordinator unless a specific decision requires it. Prefer a targeted search, a narrow file range, or a cheap digest with cited evidence.

## Delegation boundary

Delegate work that is bounded, inspectable, and low-authority:

- Repository research, inventories, extraction, classification, and document summaries.
- Routine reviews and cheap digests of logs, artifacts, and diffs.
- Narrow implementation with tests in an isolated workspace.
- Mechanical checks that need little judgment.

Retain secrets, credentials, privileged systems, remote hosts, production changes, communication outside the team, irreversible choices, prioritization, and final acceptance. Do not put secrets in a brief or child prompt. A successful child result is evidence, not permission to commit, publish, deploy, merge, send, or change an external system.

## Leaf contract

Every leaf should name its objective, allowed inputs, writable scope, verification command or evidence, output format, terminal marker if the tool supports one, and stop condition. Give it the smallest capable model. Add an isolated workspace for write-capable implementation when the tool supports it.

Use structured output for data that another leaf consumes. Ask for a short conclusion, evidence locations, risks, and unanswered questions. Do not ask the coordinator to ingest raw command output unless it is needed to decide.

## Durable execution

Validate a workflow before starting it. Declare limits for nodes, concurrency, elapsed time, cost if available, nesting depth, and continuation turns. Start once, save the workflow ID, then wait through an event, callback, background watcher, or one durable wait command. Never spend model turns asking whether a workflow is done.

Treat timeout, maximum-turn, or cost-limit states as budget exhaustion. Accept a leaf only after its terminal-success state, non-empty artifact, required marker where applicable, and the parent's review. Reuse completed siblings only when the workflow tool provides a safe resume mechanism.

## Cost-aware priority

Use the ordinary execution lane by default. Choose an urgent lane only for an explicit request or an active correction and verification loop. Faster dispatch may remove a queue delay, but it must not bypass tests, security checks, freshness checks, locks, or cancellation of obsolete work. Do not reserve warm capacity merely because an agent asks for speed. This prevents small tasks from creating a permanent infrastructure and token bill.

## Parent verification

The coordinator checks the final artifact, intended diff, tests, and any external effect. Review the work against the original acceptance checks, not the leaf's self-report. Escalate conflicting evidence to a strong model only when the coordinator cannot resolve it from concise evidence.

## Why this saves tokens

The largest savings come from fewer expensive calls and less repeated context. Shared briefs avoid copying the same background into every leaf. Durable waits remove status-chasing turns. Cheap digests keep multi-megabyte logs and full diffs outside the expensive context. A small number of well-scoped leaves is cheaper than a chain of agents rediscovering the same task.
