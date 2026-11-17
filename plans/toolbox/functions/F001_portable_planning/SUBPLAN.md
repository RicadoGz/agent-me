# F001: Package function plans and map generation

**Status:** Complete for scoped implementation and independent generator acceptance. The coordinator published the F001 delivery and verified its remote SHA; assembled package verification and final shared records remain coordinator owned.
**Owner:** `/root/portable_planning`, fresh scoped implementation agent.

## Scope

Own skills/plan-decomposition, its generator and package documentation; use the current Roki tooling as the source standard. Preserve editable live plans and meaningful generator validation.

## Inputs and outputs

Input: Ricardo's explicit development instructions and the current Roki development workflow. Output: reusable tooling and instruction changes in agent-me, with project product behavior excluded.

## Acceptance

A standalone sample generates one subplan per function, compact progress, linked index and dependency map, and refuses to overwrite live output.

## Current checkpoint

November 16, 2026 publication checkpoint: the coordinator reports the F001 delivery published at `4079fc1540221fe08de6ebf402040de7cc59c9bf`, with the actual remote SHA verified. This is coordinator supplied publication evidence; this implementation owner did not commit, push or repeat the remote check. The scoped implementation and independent acceptance below remain unchanged. No code or check was rerun for this plan update.

November 16, 2026: the coordinator supplied the independent acceptance result from `/root/planning_acceptance`, recorded in [F003 verification](../F003_verification/SUBPLAN.md) and `skills/plan-decomposition/tests/test_render_plan.py`. The reported command `python3 -B -m unittest discover -s skills/plan-decomposition/tests -v` returned exit zero: three tests passed, zero failures or skips. The independently checked renderer SHA256 remains `a8ade7aa86626d4570ffb0a200857d1d1772a0f1787767caa706b621660f4c50`.

The three real CLI acceptance cases cover separate owned subplans and linked progress, index and map with dependency and inherited decision status, legacy unassigned owner compatibility, exact preservation of edited output on rejected regeneration, and rejection of unknown and cyclic dependencies before output creation. These results complete the approved F001 generator acceptance. They are attributed independent evidence, not checks rerun by this implementation owner. No code edit, further check, commit or push accompanied this checkpoint.

## Remaining limits

The renderer generates planning scaffolds; it does not automatically maintain live ownership or prove application behavior. Owners and the coordinator follow the maintained plan responsibilities. The accepted cases cover the meaningful generation and preservation contract, not every possible malformed manifest. Assembled component integrity, installed copy consistency and publication of final shared records remain with the coordinator. The F001 delivery publication is established only by the attributed coordinator checkpoint above.

## Earlier implementation checkpoint

November 16, 2026: `/root/portable_planning` packaged the four source planning files under `skills/plan-decomposition` and adapted them into reusable function based planning. Every generated function now has an explicit Owner field and a SUBPLAN.md designated as its implementation plan, with current checkpoint, outstanding acceptance, next action and transfer responsibilities. The generated PLAN.md has a Latest checkpoint, MAP.md retains dependency navigation, and PROGRESS.md assigns owner updates separately from coordinator shared records. An optional nonempty string `owner` in a manifest records an existing assignment; legacy manifests remain supported with an explicit unassigned receipt action.

Implementation first and no TDD are reflected in the generated execution sequence. Necessary new checks and independent authoring are conditional on a material coverage gap; planned cases remain distinct from actual passing outcomes. Product specific deferral language was generalized. No application source, installed copies, shared catalog, source manifest or other function plan was edited by this owner.

Actual checks: Python `compile` accepted the generator source without emitting bytecode. One disposable two function, two phase CLI smoke generated exactly two linked subplans plus PROGRESS.md, PLAN.md, MAP.md and manifest.json, exit zero. All generated source and navigation links resolved in the temporary repository. A second invocation against that same output exited one and left a manually written progress sentinel unchanged. No persistent tests were authored; the independent author receives the interfaces and behavior below. Source was then simplified to avoid duplicating all acceptance scenario text in the remaining acceptance field; the final one function disposable generation check also passed after that simplification, with an unverified acceptance summary and one generated subplan. No project activation, language server, native command, application, browser or model task was used.

Independent verification interface: `validate(data)` raises before output writes for unsafe or duplicate IDs, unknown phase or dependencies, cyclic dependencies, unknown decisions, invalid requirement coverage, fewer than two acceptance cases or a supplied blank/nonstring owner. `render(data, destination: Path, repository: Path)` validates, refuses existing output with FileExistsError, generates one directory per unit using stable ID and slug, maps root relative source paths to working relative Markdown links, inherits unresolved decision blockers through dependencies and writes only the new output tree. CLI: `python3 skills/plan-decomposition/scripts/render_plan.py MANIFEST OUTPUT --repository ROOT`. The existing no overwrite contract preserves hand edited plan state; revisions use a fresh staging tree. These are implementation observations for independent test derivation, not a claim that every validation branch was executed.

## Next action

Preserve the published F001 implementation and passing independent result. `/root/portable_planning` retains continuous ownership of this same plan and supports a later concrete planning generator defect with a scoped correction and necessary checks. The coordinator completes assembled verification and publishes the final shared progress and index records. No additional F001 source change or check is scheduled.
