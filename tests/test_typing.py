"""The stubs must be precise: mypy and ty must accept the good lines of every tests/typing/check_*.py and report
exactly the lines marked `# error` (NCollection_Xxx[T] spelling, nested classes, C++ namespaces as modules)."""
import re
import shutil
import subprocess
import sys
from collections import Counter
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


def test_every_stub_member_exists_at_runtime():
    """A stub may only promise what the runtime has: for every class of the shipped stubs, each member it declares must
    exist on the runtime class -- for a generic NCollection class on every instantiation, since the runtime generic is only
    the NCollection_X[T] lookup. The hand-written generic stubs had drifted from the binder by 34 members (statics without
    their _s, Iterator.__next__, Change*/Contains for element types the binder leaves them out for; final review
    2026-09-30), which mypy and ty accepted -- a lie that type-checks is invisible to the ratchet below."""
    import ast
    import importlib

    import nanocct
    from nanocct._templates import Generic
    pkg = Path(nanocct.__file__).parent

    def check(node: ast.ClassDef, targets: list, path: str, lies: list[str]) -> None:
        for m in node.body:
            if isinstance(m, (ast.FunctionDef, ast.ClassDef)):
                absent = [t for t in targets if not hasattr(t, m.name)]
                if len(absent) > 0:
                    lies.append(f"{path}.{m.name} (absent on {len(absent)} of {len(targets)}, e.g. {absent[0].__name__})")
                elif isinstance(m, ast.ClassDef):
                    check(m, [getattr(t, m.name) for t in targets], f"{path}.{m.name}", lies)

    lies: list[str] = []
    for stub in sorted(pkg.rglob("*.pyi")):
        module = ".".join(stub.relative_to(pkg.parent).with_suffix("").parts).removesuffix(".__init__")
        if module == "nanocct":
            continue                               # the package stub only re-exports the packages
        mod = importlib.import_module(module)
        for node in ast.parse(stub.read_text(encoding="utf-8")).body:
            if isinstance(node, ast.FunctionDef) and not hasattr(mod, node.name):
                lies.append(f"{module}.{node.name}")
            elif isinstance(node, ast.ClassDef) and node.name == "_NCollection_Shared_members":
                # the members every NCollection_Shared<T> adds to its T (a stub-only base, NCollection_Shared being a
                # lookup object in the stub): checked on every instantiation
                check(node, list(mod.NCollection_Shared._instances.values()), f"{module}.NCollection_Shared", lies)
            elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):   # _X: stub-only typing helpers
                runtime = getattr(mod, node.name, None)
                if runtime is None:
                    lies.append(f"{module}.{node.name}")
                    continue
                targets = list(runtime._instances.values()) if isinstance(runtime, type) and issubclass(runtime, Generic) \
                    and "_instances" in vars(runtime) else [runtime]
                check(node, targets, f"{module}.{node.name}", lies)
    assert lies == [], f"{len(lies)} stub members the runtime does not have:\n" + "\n".join(lies[:60])


# mypy's errors in the shipped stubs, per error code (State.md 8.22-8.24). Every one left is the C++ shape of OCCT that
# Python typing cannot express -- [override] is C++ name hiding, [misc] operator pairs such as `*=`/`*` with different
# operand sets, [overload-cannot-match]/[overload-overlap] overloads Python cannot tell apart (reachable int widths, a
# handle and a pointer to the same class), [valid-type]/[name-defined] the quoted C++ names of template instantiations
# that R-UNBOUND-TYPE does not judge. A real bug showed up as a new code ([assignment]: R-PTR-NULL; [name-defined]: the
# unqualified enum defaults) or as a growing count ([overload-cannot-match]: base-before-derived, R-OVERLOAD-ORDER), so
# every other code must stay at zero and these must not grow. Measured on macOS with mypy 2.3.1 (uv.lock); a mypy
# upgrade may move them.
STUB_ERROR_PINS = {"override": 887, "valid-type": 14, "misc": 33, "name-defined": 20, "overload-cannot-match": 15,
                   "overload-overlap": 6}


def test_stub_errors_do_not_grow(tmp_path):
    """A ratchet on mypy over every module of the installed stubs. mypy silences errors inside an installed package, so
    the package's .py/.pyi files are copied out and checked as source. The compiled extension modules (nanocct._TK*,
    imported by nanocct.all) have nothing mypy can read and are declared as such -- any other missing import counts.
    On macOS, where the pins were measured, a count must match exactly: when one drops, lower its pin. The stubs are not
    identical across platforms (Cocoa on macOS, R-UNDEFINED on Windows), so elsewhere the pins are upper bounds."""
    import nanocct
    pkg = Path(nanocct.__file__).parent
    extensions: list[str] = []
    for f in pkg.rglob("*"):
        if f.suffix in (".py", ".pyi") or f.name == "py.typed":
            dst = tmp_path / "nanocct" / f.relative_to(pkg)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst)
        elif f.suffix in (".so", ".pyd") and f.parent == pkg:
            extensions.append("nanocct." + f.name.split(".")[0])
    assert len(extensions) > 40
    (tmp_path / "mypy.ini").write_text("[mypy]\n" + "".join(f"\n[mypy-{m}]\nignore_missing_imports = True\n" for m in sorted(extensions)))
    proc = subprocess.run([sys.executable, "-m", "mypy", "--no-incremental", "--config-file", "mypy.ini", "-p", "nanocct"],
                          cwd=tmp_path, capture_output=True, text=True)
    errors = [line for line in proc.stdout.splitlines() if ": error: " in line]
    assert len(errors) > 0 or proc.returncode == 0, proc.stdout + proc.stderr    # a mypy crash is not a clean run
    counts = Counter(m.group(1) if (m := re.search(r"\[([a-z-]+)\]$", line)) is not None else "?" for line in errors)
    grown = sorted(code for code, n in counts.items() if n > STUB_ERROR_PINS.get(code, 0))
    assert grown == [], "mypy errors grew in the stubs:\n" + "\n".join(
        f"[{code}] {counts[code]} > {STUB_ERROR_PINS.get(code, 0)}:\n  " + "\n  ".join(
            line for line in errors if line.endswith(f"[{code}]"))[:4000] for code in grown)
    if sys.platform == "darwin":
        dropped = {code: (counts.get(code, 0), pin) for code, pin in STUB_ERROR_PINS.items() if counts.get(code, 0) < pin}
        assert dropped == {}, f"fewer mypy errors than pinned (now, pin): {dropped} -- lower STUB_ERROR_PINS"
