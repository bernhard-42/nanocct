"""The NCollection_Xxx[T] spelling must be precisely typed: mypy and ty must accept the good lines of
tests/typing/check_ncollection.py and report exactly the lines marked `# error`."""
import re
import subprocess
import sys
from pathlib import Path

import pytest

CHECK = Path(__file__).parent / "typing" / "check_ncollection.py"
EXPECTED = {i + 1 for i, line in enumerate(CHECK.read_text().splitlines())
            if "# error:" in line and not line.lstrip().startswith(('"""', "Lines"))}   # markers on code lines only


def _reported_lines(cmd: list[str]) -> set[int]:
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=CHECK.parents[1])
    out = proc.stdout + proc.stderr
    lines = {int(m.group(1)) for m in re.finditer(rf"{re.escape(CHECK.name)}:(\d+)", out)}
    if lines == set():
        assert proc.returncode == 0, out
    return lines


@pytest.mark.parametrize("checker", ["mypy", "ty"])
def test_type_checker_reports_exactly_the_marked_lines(checker):
    if checker == "mypy":
        cmd = [sys.executable, "-m", "mypy", "--no-error-summary", "--hide-error-context", str(CHECK)]
    else:
        cmd = [sys.executable, "-m", "ty", "check", "--output-format", "concise", str(CHECK)]
    assert _reported_lines(cmd) == EXPECTED
