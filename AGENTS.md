# Agent Instructions

For implementation work, start with the project's compact PROGRESS.md and assigned function's SUBPLAN.md. Every independently delivered function needs its own owned plan before implementation. If that structure is absent, use [plan decomposition](skills/plan-decomposition/SKILL.md) to create function folders, subplans, progress, index and map. The subplan is the primary execution and handoff document.

For software implementation, feature development or onboarding an existing codebase, first read [the skill catalog](skills/software-development/SKILLS.md), then load the relevant parts of [the combination](skills/software-development/SKILL.md).

Before a new development task or meaningful behavior change, use [the development brief](skills/dev-brief/SKILL.md). Inspect current code first, then explain the plan, important decisions, one learning point and verification in plain Chinese. Preserve existing authorization and read only requests.

Read [Ricardo's reusable development instructions](skills/software-development/references/ricardo-development-rules.md) when using this template. Keep his confirmed workflow requests current there and apply them to delegated agents; these are agent collaboration rules, not application behavior tracking.

Select capabilities as the task progresses. Preserve confirmed requirements and use independent implementation, test authoring, verification and review roles where the task needs them.

For delegated work, follow [plan ownership and handoff](skills/software-development/SKILL.md#plan-ownership-and-handoff): each owner continuously maintains its own subplan and the coordinator maintains shared progress. Carry the plan path and update responsibility into every worker assignment.

At completion, verification results, blockers, decisions and handoffs, the owner updates its current plan before reporting. The coordinator checks that actual edit and synchronizes progress, the parent checkpoint and changed status entries in PLAN.md and MAP.md. Read only the current plan and necessary linked context; broader parent plans are for unresolved questions.

When maintaining this package, preserve upstream attribution and license files. Update source hashes only for intentional source changes. Run `python3 skills/software-development/scripts/check_components.py` before publishing changes.
