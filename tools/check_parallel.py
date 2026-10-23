"""Check that a parallel generation reproduces a serial one byte for byte (`make check-parallel`).

NANOCCT_JOBS>1 parses and emits in a pool, deriving the two inputs a package normally inherits from the packages before
it (Generator.md 6.2): who already bound which instantiation, and the parser's cross-package state. This runs the
generator twice over three toolkits -- serially (NANOCCT_JOBS=1) and with one worker per core (NANOCCT_JOBS=0) -- into a
temporary directory and compares every file. Three toolkits, because the interesting cases are cross-toolkit: an
instantiation owned by an earlier toolkit (NCollection_Array1<gp_Pnt2d>, owned by TKMath, used by TKG2d) and a class
deriving from one.

Not part of `make test`: the serial run costs what the parallel one saves (76 s against 22 s on a 24-core Windows
machine, measured 2026-10-23), and the per-run known_elsewhere check of every parallel generation (__main__) carries
the normal case. Run it after a change to the parse or the emit phase.

Usage: python tools/check_parallel.py [generator arguments, e.g. --occt DIR]. Exit code: 0 when the two runs wrote the
same files with the same bytes, 1 otherwise; a failing generator run fails the check with its output.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parents[1]
TOOLKITS = ["TKernel", "TKMath", "TKG2d"]


def _files(tree: Path) -> list[Path]:
    return sorted(p.relative_to(tree) for p in tree.rglob("*") if p.is_file())


def main(argv: list[str]) -> int:
    flags = [f for tk in TOOLKITS for f in ("--toolkit", tk)]
    with tempfile.TemporaryDirectory() as tmp:
        outs = {}
        for name, jobs in (("serial", "1"), ("parallel", "0")):
            outs[name] = Path(tmp) / name
            print(f"check-parallel: {name} generation of {', '.join(TOOLKITS)} (NANOCCT_JOBS={jobs})", flush=True)
            run = subprocess.run([sys.executable, "-m", "generator", *argv, *flags, "--out", str(outs[name])],
                                 cwd=ROOT, capture_output=True, text=True, env={**os.environ, "NANOCCT_JOBS": jobs})
            if run.returncode != 0:
                sys.stdout.write(run.stdout)
                sys.stderr.write(run.stderr)
                print(f"check-parallel: the {name} generation failed (exit {run.returncode})", file=sys.stderr)
                return 1
        serial, parallel = _files(outs["serial"]), _files(outs["parallel"])
        differ = [f"only in one run: {p}" for p in sorted(set(serial) ^ set(parallel))]
        differ += [f"differs: {p}" for p in serial if p in set(parallel)
                   and (outs["serial"] / p).read_bytes() != (outs["parallel"] / p).read_bytes()]
    if len(differ) > 0:
        print("check-parallel: the parallel generation does not reproduce the serial one:", file=sys.stderr)
        for line in differ:
            print(f"  {line}", file=sys.stderr)
        return 1
    print(f"check-parallel: {len(serial)} files byte-identical")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
