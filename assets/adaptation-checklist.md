# Adaptation checklist

Complete this checklist before adopting the skill.

- [ ] Name the expensive coordinating model as `<expensive-model>`.
- [ ] Map `<strong-model>`, `<medium-model>`, and `<cheap-model>` to available models and their intended work.
- [ ] Set the coordinator limits for calls, context, compactions, and tool-result size.
- [ ] Set workflow limits for nodes, concurrency, wall time, cost, depth, and continuation turns.
- [ ] Replace `<delegation-tool>` with the approved command or service.
- [ ] Replace `<instruction-file>` and choose any wrapper-file names.
- [ ] Replace `<durable-wait-command>` and set its timeout and completion signal.
- [ ] Choose bootstrap, strict, or error behavior for repositories without the managed block.
- [ ] Define the isolated-workspace rule for write-capable leaves.
- [ ] Define who may approve external actions after parent verification.
- [ ] Test idempotent propagation in a disposable repository before a broad rollout.

