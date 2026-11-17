# Manifest Fields

The JSON root contains `title`, `sources`, `decisions`, `phases`, `code_evidence` and `units`.

Use `requirement_coverage` to map required source capabilities to function IDs. Keep source requirement labels intact so omissions remain visible in PLAN.md.

1. `sources`: a mapping from document ID to repository relative path.
2. `decisions`: a mapping from an unresolved decision ID to its question.
3. `phases`: an ordered mapping from phase ID to display name.
4. `code_evidence`: evidence items with `tool`, `path`, `result` and `scope`. Store observed navigation results, not claims about unimplemented code.
5. `units`: the function records below.

Every unit has `id`, `slug`, `title`, `phase`, `goal`, `source_sections`, `inputs`, `outputs`, `depends_on`, `planned_files`, `planned_symbols`, `acceptance`, and `decision_dependencies`. IDs and slugs use ASCII letters, digits and underscores. Dependencies refer to existing unit IDs and form a directed acyclic graph. A later unit can set `deferred` to true. An optional nonempty string `owner` identifies an already assigned agent or role; otherwise the generated plan marks ownership unassigned and requires the receiving agent to record its identity before work.

`source_sections` names the source document ID and section, such as `product 5.1.4` or `implementation 6`. An acceptance scenario states a concrete input or condition and expected observable result. Include at least one ordinary success case and one failure, absence or boundary case.

Planned file and symbol names are proposed ownership and interface locations, not evidence that implementation exists. A symbol may be omitted for a bounded feasibility experiment or a deferred product direction when a program interface is not yet justified.

Place the output under `plans/<project>`. The source paths and proposed file paths remain relative to the repository root; subplan links are generated relative to their actual directories.

The renderer creates compact PROGRESS.md, PLAN.md with a Latest checkpoint, MAP.md and a separate SUBPLAN.md for every function. Each subplan includes an Owner field, current checkpoint, remaining acceptance, next action and handoff responsibilities. That subplan is the assigned function's implementation plan; another parallel implementation plan is unnecessary.

The assigned owner updates its own status and evidence before reporting a meaningful checkpoint or taking the next dependent function. The coordinator checks those actual edits and maintains shared progress, parent checkpoint and matching index and map entries. Manifest fields remain planned contracts and dependencies; a generated acceptance scenario is not a passing check. Preserve live checkpoints by rendering revisions into a fresh staging directory and applying only intentional changes. Consult parent source sections only when current task context is insufficient.
