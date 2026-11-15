---
name: software-development
description: Software development combo for existing codebases and new features. Read the catalog to select Serena navigation, clarification, independent implementation, test authoring, verification and review.
---

# Software Development Combo

Read [SKILLS.md](SKILLS.md) first. Select the stages needed for the actual request and read their linked instructions. A small correction need not activate every stage.

The approved selections are Serena, Matt Pocock grilling, Superpowers subagent development, Playwright planner and generator, Superpowers verification, and Matt Pocock code review. Other vendored Superpowers folders are supporting dependencies. Source versions and hashes are in [sources.json](sources.json).

## Navigation and requirements

For existing code, use Serena to locate relevant symbols and references before splitting implementation work. Read [references/serena.md](references/serena.md) for activation. Report unavailable semantic navigation accurately; use repository search to make independent progress when possible.

Read supplied context and current code before asking questions. Load [grilling](components/mattpocock/grilling/SKILL.md) for unresolved choices that affect scope, behavior or acceptance. Preserve settled answers and proceed when requirements are clear.

## Independent implementation

For a feature with separable deliverables, load [writing plans](components/superpowers/writing-plans/SKILL.md) and [subagent development](components/superpowers/subagent-driven-development/SKILL.md). Give each implementer explicit responsibility, file scope, interfaces, approved requirements and a verification command. Use a fresh agent context per feature task. Independent tasks may run concurrently when file and runtime ownership do not overlap.

This combination follows the user approved requirements: an unresolved product or acceptance decision returns to the user. Routine implementation choices remain the coordinator's responsibility. This replaces the upstream instruction to settle product ambiguities through autonomous rulings. Preserve the execution method already chosen by the user.

Resolve a referenced `superpowers:` skill from `components/superpowers/<skill-name>/SKILL.md` in this folder, reading it only when relevant. Preserve the current project's workflow and existing authorization for commits, branches and external actions.

## Independent test authoring

For a web feature, load [Playwright test authoring](components/playwright/SKILL.md). Dispatch a test planner and a separate test generator with approved requirements and relevant project context. The feature implementer is not the sole author or approver of acceptance tests.

For backend, library or CLI work, assign a separate test author using the project's actual test framework and confirmed requirements. Disclose that this is native test authoring rather than Playwright; preserve the user's selection instead of silently substituting TEA or Agentic QE.

The test author owns acceptance expectations and test files. Repeat acceptance file ownership and the current commit permissions explicitly in every implementer brief, including when using upstream templates that suggest writing tests and committing. Implementers return disputed expectations to that author or the user. Fix confirmed product defects in product code. Keep legitimately corrected test expectations traceable to approved behavior.

## Independent verification and review

Dispatch a fresh verifier using [verification before completion](components/superpowers/verification-before-completion/SKILL.md). It reads approved requirements, relevant changes and test instructions, reruns meaningful checks, and reports commands, exit codes, failures, skips and uncertainty. It returns defects to their owner and preserves product code and acceptance expectations during verification.

For completed feature changes, use [code review](components/mattpocock/code-review/SKILL.md) with a fixed comparison base and identifiable specification. A task base recorded before implementation and an approved local specification satisfy these inputs; reuse them instead of requesting redundant tracker setup or asking for a base already known. Keep its requirements and standards reviewers independent. Project standards and approved scope govern findings.

Report what changed, what was checked and remaining gaps. Browser work follows the host environment's browser ownership, permission and cleanup rules before any page operation. The catalog describes available components; it is not evidence that a project has passed acceptance.
