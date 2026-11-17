# Agent Me

A reusable software development toolbox for AI coding agents.

The agent reads a skill catalog, selects the capabilities needed for the current task, and loads their instructions. The same combination supports existing codebases and new projects.

Start with the [skill catalog](skills/software-development/SKILLS.md). The [combination entrypoint](skills/software-development/SKILL.md) explains how the roles work together.

## Selected capabilities

1. **Serena: code navigation.** Find functions, classes and references before changing existing code. Use the results to locate ownership and understand affected code.

2. **Matt Pocock grilling: requirements clarification.** Turn unresolved product decisions into focused questions with recommended answers. Continue once the user has settled the behavior and acceptance criteria.

3. **Superpowers: independent implementation.** Split a feature into tasks with clear files, interfaces and expected results. Give each feature task a fresh implementation agent.

4. **Playwright planner and generator: web test authoring.** A planning agent creates the test plan, and a separate generation agent writes executable tests. Use the project's native test framework for libraries, backend services and command line tools.

5. **Superpowers verification: independent acceptance.** A fresh verifier runs meaningful checks and reads their output and exit codes. Report completion only when the evidence supports it.

6. **Matt Pocock code review: independent review.** Separate reviewers check requirements compliance and project coding standards. Report the findings for both areas.

## Working principles

[Ricardo's development instructions](skills/software-development/references/ricardo-development-rules.md) preserve confirmed workflow requests for future projects, including no TDD and continuous owner plan updates. The repository instructions and skill catalog load this shared reference.

Read existing context before asking questions. Preserve decisions the user has already made. Return unresolved product and acceptance decisions to the user while handling routine implementation details autonomously.

Keep feature implementation, acceptance test ownership, verification and review separate. A failing test that exposes a product defect goes back to the implementation owner.

Load the stages relevant to the task. A small correction does not need every stage.

## Use with Codex

Clone this repository and link the combination into your personal skills directory:

```bash
git clone https://github.com/RicadoGz/agent-me.git
cd agent-me
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/skills/software-development" "$HOME/.agents/skills/software-development"
```

If a skill with that name already exists, inspect it before replacing anything.

Invoke the combination with:

```text
Use $software-development to implement this feature.
```

The repository's [AGENTS.md](AGENTS.md) points agents to the catalog while working here. To use that convention across other projects, add a pointer to the installed catalog in your own global instructions.

## Runtime setup

The repository includes skill instructions, source snapshots and the selected Playwright agent definitions. Serena's server and the target project's browser testing environment are separate runtime dependencies.

Follow [Serena setup](skills/software-development/references/serena.md) to connect code navigation. For web tests, follow the [Playwright component](skills/software-development/components/playwright/SKILL.md) and configure the actual project, application and authorized browser connection.

Check the package without launching a browser:

```bash
python3 skills/software-development/scripts/check_components.py
```

Add `--runtime` to check local Serena and Playwright executable versions as well. It looks for Playwright in the current project's `node_modules` first; set `SOFTWARE_DEVELOPMENT_PLAYWRIGHT_CLI` to use a different CLI path. Python 3.11 or later is required for the checker.

## Sources and licensing

The [source manifest](skills/software-development/sources.json) records fixed upstream revisions and file hashes. The [third party notices](THIRD_PARTY.md) identify the included components and their licenses.

Local package checks do not establish that a target application passes its tests. Each project needs its own runtime verification.
