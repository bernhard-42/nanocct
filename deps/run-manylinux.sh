#!/bin/bash
# Run a command inside the nanocct manylinux_2_28 container (deps/manylinux.Dockerfile), with the repository mounted
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
# The image follows the host's architecture: manylinux_2_28_x86_64 on x86_64, manylinux_2_28_aarch64 on arm64
# (deps/manylinux.Dockerfile takes it as ARCH). One image per architecture, so a box that has built both keeps both.
# Lowercase: docker rejects a repository name with capitals ("invalid reference format: ... must be lowercase",
# which the rename to nanocct ran into on 2026-09-28).
ARCH="$(uname -m)"
if [ "$ARCH" = "arm64" ]; then ARCH=aarch64; fi          # macOS spells it arm64, the manylinux images aarch64
IMAGE="nanocct-manylinux-$ARCH"

docker build -q -t "$IMAGE" --build-arg ARCH="$ARCH" -f "$HERE/manylinux.Dockerfile" "$HERE" > /dev/null

tty_flags=()
if [ -t 0 ] && [ $# -eq 0 ]; then tty_flags=(-it); fi
exec docker run --rm "${tty_flags[@]}" -u "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$ROOT:/work" -w /work "$IMAGE" \
  bash -lc "${*:-bash}"
