<!-- <policy-marker>:BEGIN -->
## Token efficiency and delegation

- The primary agent coordinates. It sets the objective, prioritizes, decides, and verifies. Delegate bounded work that does not need retained authority.
- Use `<delegation-tool>` with the cheapest capable level. Give each leaf a closed prompt, only needed inputs, an output contract, and explicit limits.
- Keep secrets, credentials, privileged access, external changes, irreversible decisions, and final verification with the coordinator.
- Do not pass full conversation history by default. Ask for concise digests before reading long logs, complete diffs, runbooks, or artifacts.
- Do not poll with model turns or short waits. Start once, record the workflow ID, and use `<durable-wait-command>`.
- Set per-turn and per-workflow budgets. Stop, summarize, or re-plan when a budget is exhausted.
- Treat partial results and time, turn, or cost limits as incomplete. Verify artifacts, diffs, tests, and external effects before completion.
<!-- <policy-marker>:END -->

