# F003: Verify the reusable package and delivery

**Status:** Scoped package verification complete. Final coordinator publication of this plan and shared records remains pending.
**Owner:** `/root/planning_acceptance`, independent test author; the coordinator owns final package publication.

## Scope

Derive only necessary generator checks from the actual implementation, verify package integrity and links, and confirm remote publication.

## Inputs and outputs

Input: Ricardo's explicit development instructions and the current Roki development workflow. Output: reusable tooling and instruction changes in agent-me, with project product behavior excluded.

## Acceptance

Meaningful generation and preservation checks pass, copied components match their recorded sources, and the published repository includes the complete reusable workflow.

## Current checkpoint

November 16, 2026. The independent test author reused `/root/workflow_audit`'s feature reading report for renderer SHA256 `a8ade7aa86626d4570ffb0a200857d1d1772a0f1787767caa706b621660f4c50`, then independently confirmed that the current file still matches it. The report covers the confirmed F001 contract, CLI, manifest, generated navigation, optional owner compatibility, inherited decision blockers, dependency validation and refusal to overwrite existing output. No additional reader was dispatched.

Necessary acceptance coverage was added after implementation in `skills/plan-decomposition/tests/test_render_plan.py`, using only the standard library and disposable repositories. One complete generation case checks separate owned function plans, inputs and outcomes, linked progress/index/map, inherited blockers, legacy unassigned ownership and absence of generated application code. One preservation case checks that a later manifest cannot overwrite hand edited plans, progress or extra evidence files. One graph boundary case checks unknown dependencies and a cycle are rejected before creating output. No test expands the supported manifest schema or claims automatic owner maintenance or product acceptance.

Actual verification: `python3 -B -m unittest discover -s skills/plan-decomposition/tests -v` returned exit zero, 3 tests passed, zero failures or skips. The graph test exercises two distinct rejected inputs. Tests execute the real CLI in temporary repositories, resolve generated links, compare dependency edges and verify an exact content and directory snapshot survives rejected regeneration. No production source, shared progress, source manifest or Git state was changed by this author; no native build, browser, application or model run was launched.

The coordinator subsequently supplied the assembled verification checkpoint. Its root component checker passed 46 files with `runtime: false`; canonical and installed skill validations passed. The `.codex` software development copy and the Roki copy match canonical bytes. The stale installed `plan-decomposition` link was repaired to point to `agent-me`, and the Roki planning copy matches its source. The complete README example ran in an isolated temporary copy and produced two function subplans with resolved links and no application code. The independent workflow audit found two reviewer placeholder conflicts; they were fixed and narrowly rechecked, with no remaining material finding reported.

The coordinator also reports F001 payload publication and remote verification at `4079fc1540221fe08de6ebf402040de7cc59c9bf`, followed by F002 publication and remote verification of the complete aligned workflow, example and instructions at `d053621c47727613983c70828e560a7d012c8bf7`. These component, installation, example, audit and remote results are attributed to the coordinator and were not rerun by this author. The three passing CLI tests are reused unchanged. Runtime verification remains false; package checks and generated instructions do not establish automatic agent compliance or product acceptance. Publication of this final F003 checkpoint and the shared records remains separate from those already verified payload commits.

## Next action

The coordinator publishes this final verification plan with the shared progress and index records, then records and verifies the resulting remote commit. Return any later concrete generator failure to `/root/portable_planning` without weakening these expectations. `/root/planning_acceptance` retains ownership of this verification plan for later checkpoints. No new tests, code changes, commits or pushes were performed for this assembled evidence update.
