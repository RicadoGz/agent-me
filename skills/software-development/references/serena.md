# Serena Setup and Activation

This combination selects Serena `2.1.0`. Install its server separately using the official package source, for example with an existing `uv` installation:

```bash
uv venv "$HOME/.codex/tools/software-development-runtime"
uv pip install --python "$HOME/.codex/tools/software-development-runtime/bin/python" \
  uv 'serena-agent @ https://github.com/oraios/serena/archive/refs/tags/v2.1.0.tar.gz'
```

The included `scripts/start_serena.sh` wrapper adds that runtime's executables to `PATH`, allowing Serena to find the installed `uv` and `uvx` executables.

Register Serena with Codex using the absolute path to this package's wrapper:

```bash
codex mcp add serena -- /absolute/path/to/software-development/scripts/start_serena.sh \
  start-mcp-server --context codex --agent-interface tools --project-from-cwd \
  --enable-web-dashboard false --open-web-dashboard false --enable-gui-log-window false
```

Inspect an existing `serena` MCP entry before replacing it. Set `SOFTWARE_DEVELOPMENT_RUNTIME` if the runtime is installed elsewhere; otherwise the wrapper uses `${CODEX_HOME:-$HOME/.codex}/tools/software-development-runtime`.

Activate the intended project before using symbol and reference tools. `--project-from-cwd` detects a recognized project from the current directory; explicitly activate the target path when none is detected.

New projects have no existing symbols to inspect until code exists. Language server support and project dependencies affect semantic navigation, so report actual availability rather than assuming indexing succeeded.

The example disables browser dashboards and graphical log windows. It does not require controlling a browser.

Sources: [official client setup](https://oraios.github.io/serena/02-usage/030_clients.html), [selected release](https://github.com/oraios/serena/releases/tag/v2.1.0).
