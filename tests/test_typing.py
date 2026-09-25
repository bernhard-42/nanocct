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
        # --python: ty does not take its environment from the interpreter that runs it (mypy does) -- it looks for
        # VIRTUAL_ENV, then ./.venv, then `python` on PATH. The manylinux container's venv is .venv-ml, so ty fell back
        # to the system Python 3.12 and could not resolve numpy (check_views.py, measured on banach 2026-09-25).
        cmd = [sys.executable, "-m", "ty", "check", "--python", sys.executable, "--output-format", "concise", str(check)]
    assert _reported_lines(cmd, check) == _expected(check)


STUBS = sorted((Path(__file__).parents[1] / "src" / "nanoocp").rglob("*.pyi"))


def test_every_stub_is_valid_python():
    """Every .pyi must parse: mypy only reaches the modules a check file imports, so a keyword used as a parameter name
    (`def RealVal(self, param: str, def: float)` in ShapeProcess.pyi until 2026-09-22, R-KEYWORD) went unnoticed."""
    import ast
    assert len(STUBS) > 100
    for stub in STUBS:
        try:
            ast.parse(stub.read_text(), filename=str(stub))
        except SyntaxError as e:
            pytest.fail(f"{stub.relative_to(STUBS[0].parents[1])}: {e}")
