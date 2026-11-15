#!/bin/sh
set -eu
runtime_dir="${SOFTWARE_DEVELOPMENT_RUNTIME:-${CODEX_HOME:-$HOME/.codex}/tools/software-development-runtime}"
export PATH="$runtime_dir/bin:${PATH:-/usr/local/bin:/usr/bin:/bin}"
if [ -x "$runtime_dir/bin/serena" ]; then
    exec "$runtime_dir/bin/serena" "$@"
fi
if command -v serena >/dev/null 2>&1; then
    exec serena "$@"
fi
printf '%s\n' 'Serena is not installed. Follow references/serena.md.' >&2
exit 127
