#!/bin/bash
# Run a command inside the nanoOCP manylinux_2_28 container (deps/manylinux.Dockerfile), with the repository mounted
# at /work. Everything the Linux build does -- generate, compile, test, and later `auditwheel repair` -- goes through
# here, so there is one Linux environment and it is the same one CI uses.
#
#   deps/run-manylinux.sh <command...>        e.g. deps/run-manylinux.sh cmake --version
#   deps/run-manylinux.sh                     an interactive shell
#
# The container runs as the invoking user, so nothing on the mounted tree comes out root-owned; HOME is set because
# that uid has no passwd entry inside and cmake would otherwise write to //.cmake.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
IMAGE=nanoocp-manylinux

docker build -q -t "$IMAGE" -f "$HERE/manylinux.Dockerfile" "$HERE" > /dev/null

tty_flags=()
if [ -t 0 ] && [ $# -eq 0 ]; then tty_flags=(-it); fi
exec docker run --rm "${tty_flags[@]}" -u "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$ROOT:/work" -w /work "$IMAGE" \
  bash -lc "${*:-bash}"
