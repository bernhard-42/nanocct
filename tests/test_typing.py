"""The stubs must be precise: mypy and ty must accept the good lines of every tests/typing/check_*.py and report
exactly the lines marked `# error` (NCollection_Xxx[T] spelling, nested classes, C++ namespaces as modules)."""
import re
import subprocess
import sys
from pathlib import Path

import pytest

CHECKS = sorted((Path(__file__).parent / "typing").glob("check_*.py"))


def _expected(check: Path) -> set[int]:
    return {i + 1 for i, line in enumerate(check.read_text().splitlines())
            if "# error:" in line and not line.lstrip().startswith(('"""', "Lines"))}   # markers on code lines only


def _reported_lines(cmd: list[str], check: Path) -> set[int]:
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=check.parents[1])
    out = proc.stdout + proc.stderr
    lines = {int(m.group(1)) for m in re.finditer(rf"{re.escape(check.name)}:(\d+)", out)}
    if lines == set():
        assert proc.returncode == 0, out
    return lines


@pytest.mark.parametrize("check", CHECKS, ids=lambda p: p.stem)
@pytest.mark.parametrize("checker", ["mypy", "ty"])
def test_type_checker_reports_exactly_the_marked_lines(checker, check):
    if checker == "mypy":
        cmd = [sys.executable, "-m", "mypy", "--no-error-summary", "--hide-error-context", str(check)]
    else:
        cmd = [sys.executable, "-m", "ty", "check", "--output-format", "concise", str(check)]
    assert _reported_lines(cmd, check) == _expected(check)
