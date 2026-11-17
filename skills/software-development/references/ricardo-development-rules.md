# Ricardo development instructions

These are reusable instructions for development agents working with Ricardo. They record his explicit workflow requests and corrections, not behavior collected by Roki or a feature to implement in an application. Apply them when reusing this toolbox in a future project. Current explicit user instructions take precedence.

Confirmed November 16, 2026.

## Implementation and necessary tests

Implement the requested behavior first. TDD is disabled: do not invoke a TDD skill, require a failing test before implementation or impose a test first sequence from a vendored template. Add or run only tests needed for meaningful changed behavior, critical integration or a concrete regression risk. Reuse sufficient existing checks. Documentation and low impact changes use appropriate manual or integrity checks. Apply these instructions to delegated agents too.

## Owned plans and agent handoff

Each assigned owner maintains its own function subplan throughout the work. At implementation or integration completion, a verification result, a blocker, a material decision or a handoff, update its current status, observed evidence and limits, and next concrete action before reporting the checkpoint or taking the next dependent function. Keep the top status consistent with the current checkpoint and identify superseded records as history. Source implementation, integration, observed behavior and formal acceptance remain separate claims.

Include the owned plan path and update responsibility in every worker assignment. For a handoff to a different agent, the outgoing owner records the exact source reference, completed and remaining scope, relevant checks, unresolved evidence and next action in that plan. The incoming agent reads it, records the transfer of responsibility and continues maintaining it. A chat reply or shared summary does not replace the owner's plan update.

The coordinator maintains shared progress, parent checkpoints and indexes from owner deliveries. Check the actual owned plan changes when reviewing a delivery; return missing or stale updates to that owner. Preserve narrow file ownership so concurrent workers do not overwrite shared records. Existing publication permissions and necessary test limits still apply.

## Maintaining these instructions

When Ricardo gives a new reusable development instruction or corrects the collaboration process, update this file with the confirmed rule and date. Keep project specific requirements in that project's plan. Summarize the instruction rather than collecting screen activity, application usage or private work content. Replace superseded rules explicitly and preserve unrelated confirmed choices.

Carry applicable rules and the owned plan path into worker assignments. When a rule changes, update relevant toolbox entry pointers and installed copies so future projects actually receive it. Keep this file as the shared reference instead of accumulating conflicting copies of the rules across templates. Publish repository changes only within the user's existing authorization and verify actual remote delivery when publication is authorized.
