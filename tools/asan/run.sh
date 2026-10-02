#!/bin/bash
# pytest under AddressSanitizer against build/asan (`make asan`, macOS): run.sh <pytest arguments>. A read of freed memory
# or past an allocation aborts with ASan's report (halt_on_error), where a release build often passes by coincidence -- the
# freed memory still holds the old value. Every child interpreter a test starts runs under ASan too (strip_env=0 keeps
# DYLD_INSERT_LIBRARIES in the environment). Not through /usr/bin/env: SIP strips DYLD_* from what a protected binary
# starts, and ASan then fails with "Interceptors are not working". PYTHONMALLOC=malloc and MallocNanoZone=0 let ASan see
# Python's own allocations; PYTHONFAULTHANDLER would catch the signal first and hide the report.
set -euo pipefail
R="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PY="$R/build/asan/venv/bin/python"
[ -x "$PY" ] || { echo "no $PY -- run make asan" >&2; exit 1; }
LIB="$(/usr/bin/clang++ -print-file-name=libclang_rt.asan_osx_dynamic.dylib)"
[ -f "$LIB" ] || { echo "no ASan runtime at $LIB" >&2; exit 1; }
cd "$R"
unset PYTHONFAULTHANDLER VIRTUAL_ENV
export DYLD_INSERT_LIBRARIES="$LIB" ASAN_OPTIONS="strip_env=0:halt_on_error=1:detect_leaks=0:color=never"
export PYTHONMALLOC=malloc MallocNanoZone=0
exec "$PY" tools/pytest_leakcheck.py -q -p no:cacheprovider "$@"
