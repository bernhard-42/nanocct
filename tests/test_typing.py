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


STUBS = sorted((Path(__file__).parents[1] / "src" / "nanocct").rglob("*.pyi"))


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


def test_no_stub_binds_a_class_under_another_name_by_import():
    """A C++ typedef alias (using Prs3d_Presentation = Graphic3d_Structure) must be an assignment in the stub:
    `from M import A as B` is not a re-export (typing spec; ty enforces it). generator/stubs.py rewrites stubgen's
    imports, which come in two layouts -- one line up to 70 characters, else a parenthesised block. It knew only the
    block until 2026-09-27: 9 aliases in 7 stubs had stayed imports, found when the shorter package name nanocct put
    Prs3d's and PrsMgr's alias on one line too."""
    import ast
    offenders = []
    for stub in STUBS:
        for node in ast.walk(ast.parse(stub.read_text())):
            if isinstance(node, ast.ImportFrom):
                offenders += [f"{stub.name}: {a.name} as {a.asname}" for a in node.names
                              if a.asname is not None and a.asname != a.name]
    assert offenders == []
    prs3d = next(s for s in STUBS if s.name == "Prs3d.pyi").read_text()
    assert "Prs3d_Presentation = nanocct.Graphic3d.Graphic3d_Structure" in prs3d
