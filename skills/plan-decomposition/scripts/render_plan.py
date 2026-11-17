#!/usr/bin/env python3
"""Render a validated function manifest into subplans and a dependency map."""
import argparse
import json
import os
import re
from pathlib import Path


def validate(data):
    units = data["units"]
    ids = [unit["id"] for unit in units]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("Function IDs must be nonempty and unique")
    for unit in units:
        for key in ("id", "slug"):
            if not re.fullmatch(r"[A-Za-z0-9_]+", unit[key]):
                raise ValueError("Unsafe function ID or folder slug")
        for key in ("title", "goal", "source_sections", "inputs", "outputs", "planned_files"):
            if not unit.get(key):
                raise ValueError(f"{unit['id']}: missing {key}")
        if "owner" in unit and (not isinstance(unit["owner"], str) or not unit["owner"].strip()):
            raise ValueError(f"{unit['id']}: owner must be a nonempty string")
        if len(unit.get("acceptance", [])) < 2:
            raise ValueError(f"{unit['id']}: include success and boundary acceptance cases")
        if unit["phase"] not in data["phases"]:
            raise ValueError("Unknown phase")
        if set(unit["depends_on"]) - set(ids):
            raise ValueError("Unknown function dependency")
        if set(unit["decision_dependencies"]) - set(data["decisions"]):
            raise ValueError("Unknown decision dependency")
    edges = {unit["id"]: unit["depends_on"] for unit in units}
    visited, active = set(), set()

    def visit(node):
        if node in active:
            raise ValueError("Function dependency cycle")
        if node in visited:
            return
        active.add(node)
        for dependency in edges[node]:
            visit(dependency)
        active.remove(node)
        visited.add(node)

    for node in ids:
        visit(node)
    for references in data.get("requirement_coverage", {}).values():
        if not references or set(references) - set(ids):
            raise ValueError("Invalid requirement coverage references")


def numbered(values):
    return "\n".join(f"{index}. {value}" for index, value in enumerate(values, 1)) or "None."


def render(data, destination, repository):
    validate(data)
    if destination.exists():
        raise FileExistsError("Output already exists; use a fresh staging directory")
    folders = {unit["id"]: f"functions/{unit['id']}_{unit['slug']}" for unit in data["units"]}
    by_id = {unit["id"]: unit for unit in data["units"]}

    def decisions_for(unit):
        result = set(unit["decision_dependencies"])
        for dependency in unit["depends_on"]:
            result.update(decisions_for(by_id[dependency]))
        return sorted(result)

    destination.mkdir(parents=True)
    source_links = {key: os.path.relpath(repository / value, destination) for key, value in data["sources"].items()}
    index = [f"# {data['title']}", "Planning only. No application functionality is implemented by these documents.", "**Latest checkpoint:** Planning scaffolds generated; implementation and acceptance are not inferred.", "## Source documents"]
    index.insert(2, "Resume from [PROGRESS.md](PROGRESS.md) and the current SUBPLAN.md. Consult parent sections only when the current task is unclear, and keep progress current at meaningful checkpoints.")
    index += [f"1. [{key}]({value})" for key, value in source_links.items()]
    index += ["## How to use", "Resume from PROGRESS.md and choose a function only when needed. Read its SUBPLAN.md, opening dependency contracts or relevant parent sections only to resolve uncertainty, and settle decisions before work that depends on them. Each independently assigned function has its own SUBPLAN.md, which is its implementation plan and maintained handoff. Its assigned owner records identity before work and updates the current status, evidence, remaining acceptance and next action at meaningful checkpoints. Implement approved behavior first; use independent test authoring only for necessary new checks and verification appropriate to the change. The coordinator maintains shared progress, parent checkpoint and matching PLAN.md and MAP.md entries. Planned paths and symbols are proposals.", "See [MAP.md](MAP.md) for the dependency map and navigation evidence.", "## Open decisions", numbered([f"**{key}:** {value}" for key, value in data["decisions"].items()])]
    mapping = [f"# {data['title']} Map", "This is a planned capability and dependency map. Planned application symbols are not evidence of implemented code; observed repository tooling is listed separately.", "## Existing code evidence"]
    for evidence in data.get("code_evidence", []):
        path = os.path.relpath(repository / evidence["path"], destination)
        mapping.append(f"**{evidence['tool']}**, [{evidence['path']}]({path}): {evidence['result']} Scope: {evidence['scope']}.")
    if data.get("requirement_coverage"):
        index.append("## Required capability coverage")
        for requirement, references in data["requirement_coverage"].items():
            links = ", ".join(f"[{ref}]({folders[ref]}/SUBPLAN.md)" for ref in references)
            index.append(f"**{requirement}:** {links}")
    mapping += ["## Reading the diagrams", "An arrow means the target consumes a result or contract from the source. Dashed arrows cross phase boundaries. All function nodes are planned or deferred, not implemented. Decision IDs are unresolved product choices, not approvals. Decision dependencies include blockers inherited through prior functions."]
    for phase, name in data["phases"].items():
        selected = [unit for unit in data["units"] if unit["phase"] == phase]
        if not selected:
            continue
        index.append(f"## {name}")
        mapping += [f"## {name}", "```mermaid", "flowchart TD"]
        selected_ids = {unit["id"] for unit in selected}
        for unit in selected:
            label = unit["id"] + ": " + unit["title"]
            mapping.append(f"    unit_{unit['id']}[\"{label.replace(chr(34), chr(39))}\"]")
        external = sorted({dep for unit in selected for dep in unit["depends_on"] if dep not in selected_ids})
        for dependency in external:
            mapping.append(f'    unit_{dependency}["{dependency}: previous phase"]')
        for unit in selected:
            for dependency in unit["depends_on"]:
                arrow = "-->" if dependency in selected_ids else "-.->"
                mapping.append(f"    unit_{dependency} {arrow} unit_{unit['id']}")
        mapping.append("```")
        for unit in selected:
            folder = destination / folders[unit["id"]]
            folder.mkdir(parents=True)
            decision_ids = decisions_for(unit)
            status = "Deferred" if unit.get("deferred") else "Blocked by decisions " + ", ".join(decision_ids) if decision_ids else "Planned"
            entry = f"[{unit['id']}: {unit['title']}]({folders[unit['id']]}/SUBPLAN.md), {status}."
            index.append(entry)
            mapping.append(entry)
            dependencies = [f"[{dep}](../{Path(folders[dep]).name}/SUBPLAN.md)" for dep in unit["depends_on"]]
            sources = [f"[{key}]({os.path.relpath(repository / value, folder)})" for key, value in data["sources"].items()]
            body = [f"# {unit['id']}: {unit['title']}", f"**Status:** {status}. Planning only; implementation requires a separate request.", f"**Phase:** {name}", f"**Owner:** {unit.get('owner', 'Unassigned. The receiving agent records its identity here before work')}", f"**Goal:** {unit['goal']}", "This SUBPLAN.md is the implementation plan for this function. The assigned owner maintains this same file throughout implementation, verification and handoff.", "## Source and scope", ", ".join(sources), numbered(unit["source_sections"]), "This unit owns only the behavior described here. Keep source plans and unrelated capabilities unchanged.", "## Inputs", numbered(unit["inputs"]), "## Outputs", numbered(unit["outputs"]), "## Dependencies", numbered(dependencies), "## Proposed ownership", numbered([f"`{path}`" for path in unit["planned_files"]]), "These paths describe future implementation or evidence ownership; no application scaffolding is created by this plan.", "## Proposed function boundaries", numbered([f"`{symbol}`" for symbol in unit.get("planned_symbols", [])]), "## Acceptance scenarios", numbered(unit["acceptance"]), "## Open decisions", numbered([f"**{key}:** {data['decisions'][key]}" for key in unit["decision_dependencies"]]), "## Handoff", "The outgoing owner records the exact source reference, completed and remaining scope, evidence and next action in this same plan. The incoming agent records its identity and takes continuous plan ownership. A chat reply does not replace the plan update. The coordinator reviews owner authored changes and maintains shared progress and map entries. Preserve the existing publication permissions.", "## Current checkpoint", "Planning scaffold only. No implementation, integration, runtime outcome or acceptance is established. At meaningful checkpoints the owner records the source reference, completed work, relevant check commands and results, evidence limits and unresolved questions here, and keeps the top Status field consistent. Preserve superseded checkpoints as history.", "## Remaining acceptance", "All acceptance scenarios above remain unverified. The owner replaces this summary with the specific outstanding scenarios and evidence limits as work progresses.", "## Next action", "Record the assigned owner and source reference, resolve only the decisions this function depends on, then implement the authorized behavior. Keep the next concrete action current after each meaningful checkpoint.", "## Execution sequence", numbered(["Read PROGRESS.md and this subplan; consult dependency contracts or relevant parent sections only when the current task is unclear.", "Resolve the listed product decisions; preserve already confirmed answers.", "Record owner identity and source, then implement only the authorized behavior in this unit. TDD is disabled; a failing test is not a prerequisite.", "Reuse existing checks and add only necessary meaningful behavior, integration or regression coverage. Use independent test authoring for a material new coverage gap.", "Verify only the relevant changed behavior and record actual output, failures and limits. Documentation may use manual or integrity checks; do not run redundant suites.", "Before reporting a meaningful checkpoint or taking the next dependent function, the owner updates this same plan: Status, current evidence, remaining acceptance and next action. The coordinator checks that update and synchronizes PROGRESS.md, the parent Latest checkpoint, and matching PLAN.md and MAP.md status, ownership and dependency entries when their facts change."]), "[Progress](../../PROGRESS.md) · [Overall plan](../../PLAN.md) · [Function map](../../MAP.md)"]
            if decision_ids != unit["decision_dependencies"]:
                position = body.index("## Handoff")
                body[position:position] = ["## Inherited decision dependencies", numbered([f"**{key}:** {data['decisions'][key]}" for key in decision_ids if key not in unit["decision_dependencies"]]), "These decisions affect dependency integration. They are not permission to reopen settled behavior or prevent independent fixture based preparation."]
            (folder / "SUBPLAN.md").write_text("\n\n".join(body) + "\n")
    (destination / "PLAN.md").write_text("\n\n".join(index) + "\n")
    (destination / "MAP.md").write_text("\n\n".join(mapping).replace("\n\nflowchart TD", "\nflowchart TD").replace("\n\n    ", "\n    ").replace("\n\n```\n", "\n```\n") + "\n")
    progress = [f"# {data['title']} Progress", "**Active function:** Unassigned.", "**Latest checkpoint:** Planning scaffolds generated. No implementation status is inferred by the renderer.", "**Next action:** Select a function from [PLAN.md](PLAN.md) for the authorized work, then read only its SUBPLAN.md.", "**Reading rule:** Consult relevant dependency contracts, map sections or parent plan sections only when the current task is unclear, incomplete, stale or contradictory. Read a complete parent plan only when narrower reading cannot resolve the question or the user requests a broad review.", "**Update rule:** At completion, a verification result, a blocker, a material decision or handoff, the assigned owner updates its own SUBPLAN.md before reporting or taking the next dependent function. The coordinator checks that actual update and maintains this note, the parent Latest checkpoint and matching PLAN.md and MAP.md entries. Record actual evidence, limits and next action; keep detailed history in the owned subplan."]
    (destination / "PROGRESS.md").write_text("\n\n".join(progress) + "\n")
    (destination / "manifest.json").write_text(json.dumps(data, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    args = parser.parse_args()
    render(json.loads(args.manifest.read_text()), args.output.resolve(), args.repository.resolve())
    print(f"Created subplans and MAP.md in {args.output}")


if __name__ == "__main__":
    main()
