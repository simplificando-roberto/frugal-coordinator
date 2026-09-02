# Instruction layering

## Canonical file and wrapper

Choose one canonical instruction file, such as `<instruction-file>`. Put team policy there. Keep tool-specific wrapper files minimal so they point readers to the canonical file instead of duplicating policy. The supplied [wrapper template](../assets/CLAUDE.md.template) shows the pattern.

This avoids drift. A policy edit has one source, and every agent reads the same rules even when its tool expects a different filename.

## Managed policy block

Put the token policy in a marked block inside the canonical instruction file. Use the exact start and end markers from [the block template](../assets/token-efficiency-block.md). The synchronizer owns only text between those markers. It must preserve all content before, after, and outside the block.

The markers make updates deterministic. They also let a checker identify malformed, missing, duplicated, or reversed markers before it changes a repository.

## Idempotent propagation

Use a script or service with this behavior for every target repository:

1. Find the canonical instruction file and wrapper file.
2. If only the canonical file exists, create the minimal wrapper.
3. If a legacy wrapper contains the real policy and is newer, require a migration decision or promote it once according to team policy.
4. Insert the managed block if both markers are absent and the repository is eligible.
5. Replace only the content between one valid marker pair if both markers exist.
6. Regenerate the wrapper from the template.
7. Report one result per repository, then continue with the next repository.

Run the same transformation twice in a test. The second run must produce no file changes. Do not make commits, pushes, pull requests, or other external changes as part of synchronization unless a separate, explicit workflow authorizes them.

## Repositories without a managed block

Decide the policy before rollout and encode it as a mode:

- Bootstrap mode may add one valid marker pair to repositories that already have the canonical instruction file.
- Strict mode must leave repositories without the block unchanged and report `missing-managed-block`.
- Error mode must leave malformed or duplicate markers unchanged and report `invalid-managed-block`.

Fail closed for malformed markers in that repository only. Continue processing the others. Never replace a full instruction file just to update one managed block, since teams often keep local rules outside the shared policy.

