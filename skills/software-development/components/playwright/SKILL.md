---
name: software-development-playwright
description: Independent web test planning and generation for the software development combo, using the official Playwright planner and generator definitions.
---

# Playwright Test Authoring

Use this component for web acceptance tests. Read approved behavior and the target project's Playwright configuration. Expected outcomes come from requirements, not merely from current application behavior.

Official definitions are pinned to Playwright `1.65.1`:

1. [Planner](agents/playwright_test_planner.toml) creates a test plan.
2. [Generator](agents/playwright_test_generator.toml) turns it into executable tests.

Dispatch separate fresh contexts, independent of the product implementer. Give each role the specification, exact project path, configuration, seed and file ownership. The coordinator may read the role's `developer_instructions` and use a generic subagent when named roles are unavailable. Its MCP tools must actually be available before using browser dependent operations.

Use the target project's installed Playwright CLI. Target projects use their own compatible Playwright dependency, configuration and fixtures. Create or adapt those inside the authorized project when needed. These definitions are source references, not a claim that every project already has dependencies or named roles registered.

Before browser operations, follow the host environment's browser control rules. Where an exclusive browser lease is required, acquire it and use only task owned targets on its endpoint. Adapt the project's seed and fixture to that connection. Upstream setup tools must not launch an unregistered browser or use a preexisting user page. If the tool cannot use the authorized connection, prepare the plan and source offline, record live validation as pending, and repair the connection before claiming runtime proof.

Keep exploration within the approved local or test application and permitted actions. Browser access does not authorize sending, submitting, purchases or other external side effects.

Hand generated tests to the independent verifier. This bundle selects planner and generator; test repair remains a separate responsibility.

Sources: [official usage](https://playwright.dev/docs/test-agents), [official generation source](https://github.com/microsoft/playwright/blob/v1.65.1/packages/playwright/src/agents/generateAgents.ts).
