"""Run pytest in a child interpreter and fail when nanobind reports leaked objects at the child's exit.

nanobind prints `nanobind: leaked N instances!` (and types, functions) to stderr when the interpreter shuts down with
objects it created still alive -- after pytest has reported, so no test can see it. A leak there is a reference cycle no
garbage collector sees, or a C++ object keeping a Python one past the end (Design.md R-KEPT); the suite has none, and this
keeps it that way. Usage: python tools/pytest_leakcheck.py <pytest arguments>. Exit code: pytest's, or 1 on a leak report
after a passing run.
"""
from __future__ import annotations

import subprocess
import sys

MARK = b"nanobind: leaked"


def main(argv: list[str]) -> int:
    child = subprocess.Popen([sys.executable, "-m", "pytest", *argv], stderr=subprocess.PIPE)
    assert child.stderr is not None
    leaked = False
    for line in child.stderr:                      # passed through as it comes, so a long run still shows its progress
        sys.stderr.buffer.write(line)
        sys.stderr.buffer.flush()
        leaked = leaked or MARK in line
    rc = child.wait()
    if leaked:
        sys.stderr.write("pytest_leakcheck: nanobind reported leaked objects at interpreter exit (see above)\n")
        return rc if rc != 0 else 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
