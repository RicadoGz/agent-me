# Reusable workflow alignment

Updated November 16, 2026. Reference: Ricardo's current Roki development practice and his explicit instructions. The baseline library revision was `a6819e067efcfafbd1f6e8bdfedb134a21e1843a`. The comparison covers agent development tools and instructions; no application feature is requested or implemented here.

## Differences and resulting workflow

1. The library lacked the portable planning capability used by the current project. It now includes `skills/plan-decomposition`, a standard library generator, manifest guidance and a complete example. Every independently delivered function gets its own directory and `SUBPLAN.md`, alongside compact progress, a selection index and a linked dependency map.
2. Entry instructions described the plan as optional or conditional on another planning request. The project instructions, catalog and combination now make the owned subplan the primary execution and handoff document before function implementation. Existing plans are maintained rather than duplicated.
3. Worker templates treated a temporary brief as the main requirement source and omitted plan maintenance. Dispatch now carries the owned subplan, update responsibility, compact progress, file ownership, dependencies, acceptance and publication permissions. Reports include the same plan's current checkpoint; reviewers check the actual update.
4. Shared progress and mapping responsibilities were incomplete. Owners maintain their own status, source, evidence, remaining acceptance and next action. The coordinator checks those edits and synchronizes PROGRESS.md, the parent checkpoint and changed PLAN.md or MAP.md statuses. Dependency and ownership map facts change only with actual changes; earlier evidence is preserved.
5. Older component snapshots still required failing tests before implementation or broad repeated validation. The current implementation first and necessary test adaptations were migrated into nine component files. The two active TDD component files and their manifest entries were removed. Upstream revisions, attribution and licenses are preserved; hashes describe intentional local adaptations.
6. Some execution instructions required complete parent plans or specs on each task. Function execution now starts from compact progress and its assigned subplan. Relevant dependency or source sections resolve concrete uncertainty. Legacy workspace helpers support compatible flat task formats and never replace maintained function plans.
7. The current role and publication boundaries are reusable. Functions receive fresh scoped implementers where independent implementation is used; necessary test authorship, verification and review keep their responsibilities. Existing authorization controls per function commit, push, remote SHA verification and coordinator integration. Low impact documentation uses suitable manual checks.
8. Explicit reusable requests remain in `ricardo-development-rules.md` with their confirmation date. New collaboration corrections update that reference and the relevant templates. Project requirements stay in their own plans. This is a maintained development toolkit, not activity monitoring inside a product.

The generator's initial plans distinguish proposed interfaces, source presence, observed outcomes and formal acceptance. Generated ownership and checkpoint instructions are responsibilities for agents and their coordinator; the generator does not automatically execute work or synchronize live status.

## Portability

The reusable package excludes Roki product specifications, its fourteen function IDs, dated execution handoffs, lane assignments, application stack requirements, local native runner paths, ports and live process rules. Generic work uses the receiving project's existing layout, permissions, build constraints and confirmed decisions.

The complete [example manifest](../examples/function-planning/manifest.json) and [source requirements](../examples/function-planning/requirements.md) generate a planning hierarchy without creating application code. Existing output is refused; later revisions are rendered into fresh staging output and intentionally merged into maintained records.

## Verification

An independent reader documented the actual generator interface and boundaries before an independent test author added necessary acceptance checks after implementation. Three CLI tests passed with zero failures or skips: generated ownership and navigation with inherited blockers, exact preservation of edited existing output, and unknown or cyclic dependency rejection before output creation. Detailed commands and source identity are in the [F003 verification plan](../plans/toolbox/functions/F003_verification/SUBPLAN.md).

Final assembled checks passed: 46 component hashes matched with runtime checks disabled; selected instruction links resolved; both skill metadata validations passed. The documented complete example generated two owned function plans and resolved links in an isolated temporary copy. Installed development copies match the canonical package; the installed planning capability now links to the reusable library, and the current project tooling is synchronized. Independent instruction review found two legacy reviewer placeholder conflicts, both corrected and narrowly rechecked with no remaining material finding.

These checks establish reusable tooling delivery. Actual agent adherence is tested through the small fresh chat trial in the README; generator tests do not claim that behavior, application acceptance or a live model result.
