---
name: software-development
description: Software development combo for existing codebases and new features. Read the catalog to select Serena navigation, clarification, independent implementation, test authoring, verification and review.
---

# Software Development Combo

Read [SKILLS.md](SKILLS.md) first. Select the stages needed for the actual request and read their linked instructions. A small correction need not activate every stage.

Before a new development task or meaningful behavior change, use [dev brief](../dev-brief/SKILL.md). It covers code inspection, the four part explanation, one learning point and the boundary between ordinary technical choices and important user decisions. Reuse the settled brief within the same scope.

Implement the approved behavior first. Reuse existing checks and add or update only necessary behavior or regression tests when a material coverage gap remains. For documentation or low impact edits, use an appropriate manual, syntax or integrity check. Repeat checks only after relevant changes, failures or unresolved concerns. Preserve existing acceptance expectations.

Every independently delivered function has its own directory and owned SUBPLAN.md before implementation. Resume from compact PROGRESS.md and that assigned subplan; it is the primary execution and handoff document. Consult dependency contracts, map sections or parent plan sections only when the current task is unclear, incomplete, stale or contradictory. Give each worker scoped context rather than the complete roadmap. Follow the plan ownership and handoff responsibilities below at meaningful checkpoints.

The approved selections are Serena, Matt Pocock grilling, Superpowers subagent development, Playwright planner and generator, Superpowers verification, and Matt Pocock code review, with plan decomposition as the planning extension. Other vendored Superpowers folders are supporting dependencies. Source versions and hashes are in [sources.json](sources.json).

## Plan ownership and handoff

Read and apply [Ricardo's reusable development instructions](references/ricardo-development-rules.md) before loading workflow components. They define implementation first with TDD disabled, necessary tests, continuous owner plan maintenance and explicit agent handoffs. Preserve these user requirements when a vendored component prescribes a different process. Record newly confirmed reusable instructions in that reference; product requirements belong in the project's plan.

## Navigation and requirements

For existing code, use Serena to locate relevant symbols and references before splitting implementation work. Read [references/serena.md](references/serena.md) for activation. Report unavailable semantic navigation accurately; use repository search to make independent progress when possible.

Read supplied context and current code before asking questions. Load [grilling](components/mattpocock/grilling/SKILL.md) for unresolved choices that affect scope, behavior or acceptance. Preserve settled answers and proceed when requirements are clear.

## Independent implementation

Before implementing independently delivered functions, use [plan decomposition](../plan-decomposition/SKILL.md) to establish one folder and owned SUBPLAN.md per function, compact PROGRESS.md, selection index PLAN.md and linked MAP.md. Reuse and update an existing structure. The current subplan carries the function scope, inputs, outputs, dependencies, acceptance, owner, current evidence, remaining work and next action. Use the index to select work; use the map or parent plan only to resolve an actual question.

For a feature with separable deliverables, load [writing plans](components/superpowers/writing-plans/SKILL.md) and [subagent development](components/superpowers/subagent-driven-development/SKILL.md). Give each implementer its owned SUBPLAN.md path, explicit responsibility, file scope, interfaces, approved requirements, necessary verification and publication permissions. Require it to update that same plan at meaningful checkpoints; the coordinator checks the edit and maintains shared progress and changed index or map entries. Use a fresh agent context per feature task. Independent tasks may run concurrently when file and runtime ownership do not overlap.

This combination follows the user approved requirements: an unresolved product or acceptance decision returns to the user. Routine implementation choices remain the coordinator's responsibility. This replaces the upstream instruction to settle product ambiguities through autonomous rulings. Preserve the execution method already chosen by the user.

Resolve a referenced `superpowers:` skill from `components/superpowers/<skill-name>/SKILL.md` in this folder, reading it only when relevant. Preserve the current project's workflow and existing authorization for commits, branches and external actions.

## Independent test authoring

When a web behavior needs new acceptance coverage, load [Playwright test authoring](components/playwright/SKILL.md). Give the planner and separate generator the confirmed requirements and the specific coverage gap. Reuse sufficient existing coverage. The feature implementer is not the sole author or approver of acceptance expectations.

When backend, library or CLI behavior needs new acceptance coverage, assign a separate author using the project's actual framework and confirmed requirements. Limit new cases to the identified behavior or regression gap. Preserve the user's selected tools.

The test author owns acceptance expectations and test files. Repeat acceptance file ownership and the current commit permissions explicitly in every implementer brief, including when using upstream templates that suggest writing tests and committing. Implementers return disputed expectations to that author or the user. Fix confirmed product defects in product code. Keep legitimately corrected test expectations traceable to approved behavior.

## Independent verification and review

Dispatch a fresh verifier using [verification before completion](components/superpowers/verification-before-completion/SKILL.md). It reads approved requirements, relevant changes and test instructions, reruns meaningful checks, and reports commands, exit codes, failures, skips and uncertainty. It returns defects to their owner and preserves product code and acceptance expectations during verification.

For completed feature changes, use [code review](components/mattpocock/code-review/SKILL.md) with a fixed comparison base and identifiable specification. A task base recorded before implementation and an approved local specification satisfy these inputs; reuse them instead of requesting redundant tracker setup or asking for a base already known. Keep its requirements and standards reviewers independent. Project standards and approved scope govern findings.

Report what changed, what was checked and remaining gaps. Browser work follows the host environment's browser ownership, permission and cleanup rules before any page operation. The catalog describes available components; it is not evidence that a project has passed acceptance.
