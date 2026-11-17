"""Acceptance checks for portable function plan generation."""

import copy
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_plan.py"


class RenderPlanAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="function_plan_acceptance_")
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        (self.repository / "docs").mkdir()
        (self.repository / "docs" / "requirements.md").write_text(
            "# Sample requirements\n\nPrepare, inspect and deliver one result.\n"
        )
        (self.repository / "src").mkdir()
        (self.repository / "src" / "existing.py").write_text("EXISTING = True\n")
        self.manifest_path = self.repository / "functions.json"
        self.output = self.repository / "plans" / "sample"

    def manifest(self):
        def unit(identifier, slug, title, phase, dependencies, decisions):
            return {
                "id": identifier,
                "slug": slug,
                "title": title,
                "phase": phase,
                "goal": f"Deliver {title.lower()} independently.",
                "source_sections": ["requirements 1"],
                "inputs": [f"Authorized input for {identifier}"],
                "outputs": [f"Inspectable result for {identifier}"],
                "depends_on": dependencies,
                "planned_files": [f"src/{slug}.py"],
                "planned_symbols": [f"{slug}_result"],
                "acceptance": [
                    f"Valid {identifier} input produces its inspectable result.",
                    f"Missing {identifier} input produces no fabricated result.",
                ],
                "decision_dependencies": decisions,
            }

        units = [
            unit("F010", "prepare", "Prepare input", "foundation", [], []),
            unit("F020", "inspect", "Inspect result", "foundation", ["F010"], ["D1"]),
            unit("F030", "deliver", "Deliver result", "delivery", ["F020"], []),
        ]
        units[0]["owner"] = "/root/receiver_one"
        units[1]["owner"] = "/root/receiver_two"
        return {
            "title": "Portable sample",
            "sources": {"requirements": "docs/requirements.md"},
            "decisions": {"D1": "Which result format is approved?"},
            "phases": {"foundation": "Foundation", "delivery": "Delivery"},
            "code_evidence": [{
                "tool": "fixture inspection",
                "path": "src/existing.py",
                "result": "An existing source file was inspected.",
                "scope": "Source presence only, no application acceptance.",
            }],
            "requirement_coverage": {"Authorized delivery": ["F010", "F020", "F030"]},
            "units": units,
        }

    def run_renderer(self, manifest, output=None):
        self.manifest_path.write_text(json.dumps(manifest))
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.manifest_path),
             str(output or self.output), "--repository", str(self.repository)],
            cwd=self.repository,
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @staticmethod
    def snapshot(directory):
        return {
            path.relative_to(directory).as_posix(): path.read_bytes() if path.is_file() else None
            for path in directory.rglob("*")
        }

    def test_generates_owned_function_plans_with_working_navigation_and_blockers(self):
        manifest = self.manifest()
        self.assert_success(self.run_renderer(manifest))

        expected = {
            f"functions/{unit['id']}_{unit['slug']}/SUBPLAN.md"
            for unit in manifest["units"]
        }
        actual = {
            path.relative_to(self.output).as_posix()
            for path in self.output.glob("functions/*/SUBPLAN.md")
        }
        self.assertEqual(actual, expected)
        for name in ("PROGRESS.md", "PLAN.md", "MAP.md", "manifest.json"):
            self.assertTrue((self.output / name).is_file(), name)
        self.assertEqual(json.loads((self.output / "manifest.json").read_text()), manifest)

        index = (self.output / "PLAN.md").read_text()
        mapping = (self.output / "MAP.md").read_text()
        for unit in manifest["units"]:
            relative = f"functions/{unit['id']}_{unit['slug']}/SUBPLAN.md"
            self.assertIn(relative, index)
            self.assertIn(relative, mapping)
            plan = (self.output / relative).read_text()
            self.assertIn(unit["goal"], plan)
            self.assertIn(unit["inputs"][0], plan)
            self.assertIn(unit["outputs"][0], plan)
            self.assertIn(unit["acceptance"][0], plan)
            for heading in ("## Current checkpoint", "## Remaining acceptance", "## Next action"):
                self.assertIn(heading, plan)
            self.assertFalse((self.repository / unit["planned_files"][0]).exists())
            status = next(line for line in plan.splitlines() if line.startswith("**Status:**"))
            if unit["id"] == "F010":
                self.assertIn("Planned", status)
                self.assertIn("**Owner:** /root/receiver_one", plan)
            else:
                self.assertIn("Blocked", status)
                self.assertIn("D1", status)
            if unit["id"] == "F030":
                self.assertIn("**Owner:** Unassigned", plan)
                self.assertIn("Which result format is approved?", plan)

        edges = set(re.findall(r"unit_(\w+)\s+(?:-->|-\.->)\s+unit_(\w+)", mapping))
        self.assertEqual(edges, {("F010", "F020"), ("F020", "F030")})
        for document in self.output.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                if not target.startswith(("https://", "http://", "#")):
                    resolved = document.parent / target.split("#", 1)[0]
                    self.assertTrue(resolved.resolve().exists(), (document, target))

    def test_existing_output_keeps_owner_edits_and_extra_files(self):
        manifest = self.manifest()
        self.assert_success(self.run_renderer(manifest))
        plan = self.output / "functions/F010_prepare/SUBPLAN.md"
        plan.write_text(plan.read_text() + "\nOwner checkpoint: actual evidence retained.\n")
        (self.output / "PROGRESS.md").write_text("Maintained progress and next action.\n")
        (self.output / "owner_notes.md").write_text("Unpublished handoff evidence.\n")
        before = self.snapshot(self.output)

        updated_manifest = copy.deepcopy(manifest)
        updated_manifest["title"] = "A later planning revision"
        result = self.run_renderer(updated_manifest)

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.snapshot(self.output), before)

    def test_invalid_dependency_graph_is_rejected_before_output_creation(self):
        for boundary in ("unknown dependency", "dependency cycle"):
            with self.subTest(boundary=boundary):
                manifest = self.manifest()
                manifest["units"][0]["depends_on"] = [
                    "F999" if boundary == "unknown dependency" else "F030"
                ]
                output = self.repository / "plans" / boundary.replace(" ", "_")

                result = self.run_renderer(manifest, output)

                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
