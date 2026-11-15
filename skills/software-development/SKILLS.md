# Software Development Skill Catalog

Read this catalog before selecting tools for a software development task. Choose only the stages relevant to the current request, then open their instructions.

1. **Code navigation: Serena.** Locate functions, classes and references to understand where behavior lives and what a change could affect. Use it when reading or changing existing code, following the [setup and activation notes](references/serena.md).

2. **Requirements clarification: Matt Pocock grilling.** Turn unresolved requirements into focused questions with recommended answers before implementation. Load [grilling](components/mattpocock/grilling/SKILL.md) when behavior, scope or acceptance remains unclear, preserving decisions already settled.

3. **Feature implementation: Superpowers.** Split features into tasks with clear file ownership and interfaces, assigning a fresh implementation agent to each task. Read [planning](components/superpowers/writing-plans/SKILL.md) and [independent implementation](components/superpowers/subagent-driven-development/SKILL.md), applying this combination's rule to ask the user about unresolved product decisions.

4. **Test authoring: Playwright planner and generator.** The planning agent creates a web test plan, and the generation agent writes executable tests from it. Use the [test authoring component](components/playwright/SKILL.md) for web features and an independent native test author for backend, library or command line work.

5. **Acceptance verification: Superpowers.** A separate verifier runs meaningful commands, reads their output and exit codes, and checks what the evidence actually proves. Load [verification](components/superpowers/verification-before-completion/SKILL.md) before reporting completion, returning failures to the responsible implementation or test author.

6. **Code review: Matt Pocock code review.** Independent reviewers check requirements compliance and coding standards separately. Read [the review skill](components/mattpocock/code-review/SKILL.md) with an identifiable specification and fixed comparison base.

Read [SKILL.md](SKILL.md) for coordination rules and [sources.json](sources.json) for fixed source versions and hashes. Run `python3 scripts/check_components.py` from this directory to check package integrity.

The catalog is available immediately after installing the skill. Live Serena navigation requires MCP setup, and live Playwright testing requires the target application's configuration, fixtures and authorized browser connection.
