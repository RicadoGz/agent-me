---
name: plan-decomposition
description: Break an existing product or implementation plan into the smallest independently verifiable capabilities, create one subfolder and SUBPLAN.md per function, and generate a linked MAP.md of scope, dependencies and code evidence.
---

# Plan Decomposition and Function Map

Every independently assigned function has its own `functions/<id>_<slug>/SUBPLAN.md`. That file is the function's implementation plan and maintained handoff throughout the work.

Start with the repository instructions, compact PROGRESS.md if present, and the current subplan or affected plan section. Read source product or implementation sections only as needed to establish scope and resolve unclear, missing or contradictory requirements. A complete source review is appropriate when a new decomposition cannot otherwise establish its boundaries, or the user requests it; it is not the default for every task. Preserve source documents and confirmed decisions. Use [the software development catalog](../software-development/SKILLS.md) to select planning and code navigation capabilities, and apply [the reusable development instructions](../software-development/references/ricardo-development-rules.md).

A function is one behavior with identifiable inputs, outputs and an independent acceptance check. Split a broad capability until another agent can own and verify it without inventing product behavior. Keep setup and scaffolding with the capability they support. Do not create a folder per line of code or pretend that a proposed function already exists.

For unresolved choices, retain the decision ID and mark affected units as blocked for implementation. Describe conditional work without choosing a branch for the user. Independent planning can continue. Keep unrelated or deferred product directions outside the current function rather than inventing detailed interfaces for them.

Create a structured manifest using [the field reference](references/manifest.md). Each unit needs a stable ID, scope, source sections, dependencies, inputs, outputs, proposed file ownership, proposed symbols, acceptance scenarios and decision dependencies. Include an assigned owner when known; otherwise the receiving agent records its identity before work. Use English unless the user requests another artifact language.

Run `scripts/render_plan.py MANIFEST OUTPUT_DIRECTORY` to create the hierarchy. The script validates IDs and dependencies before writing and refuses an existing output directory. On later revisions, update the manifest and render to a fresh staging directory, compare changes, then preserve hand edited subplans while applying the intended updates.

The output contains PROGRESS.md, PLAN.md, MAP.md, manifest.json and one `functions/<id>_<slug>/SUBPLAN.md` per unit. PROGRESS.md is the compact resume point; PLAN.md is the selection index; MAP.md contains diagrams and linked function locations; each SUBPLAN.md is the independent handoff. Read the current subplan by default, not every subplan or the entire parent plan.

The assigned owner continuously maintains its same subplan. Before reporting a completion, verification result, blocker, material decision or handoff, or taking the next dependent function, update its top Status, current source and evidence, limits, remaining acceptance and next concrete action. Preserve superseded records as history. Every worker assignment includes this plan path and update responsibility; an outgoing owner records the exact handoff, and the incoming agent records its identity and continues maintenance. A chat reply does not replace the plan update.

The coordinator checks the actual owner authored update, then maintains shared PROGRESS.md, the parent Latest checkpoint and matching PLAN.md and MAP.md entries. Change map ownership and dependency facts when they change. Implement authorized behavior first; TDD is disabled. Reuse existing checks and add only necessary meaningful validation. Preserve live progress when revising generated scaffolds.

For a code map, read Serena's instructions and the repository's runtime constraints before activating a project or inspecting relevant symbols. If language server activation would start work outside the permitted build or resource scope, use targeted repository inspection and record that navigation boundary. Record the tool, path and observed result in manifest evidence. A repository with no application implementation gets a planned dependency map and an explicit statement that an application call graph is unavailable. Keep existing tooling evidence separate from planned application functions. Use repository inspection as supplemental evidence when a language backend is unavailable and disclose that boundary.

Validate source coverage, dependency acyclicity, link targets, decision blockers, the generated folder count and meaningful acceptance cases. A directory tree or diagram is a planning artifact, not runtime validation. Create planning files only; application implementation requires its own user request. Report exact paths and give one representative subplan.
