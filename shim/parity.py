"""build123d's own test suite through the OCP shim, compared test by test with the real OCP (State.md 8.18, 8.6).

    python shim/parity.py [--build123d DIR] [--dist DIR] [--work DIR] [--python 3.14] [--reuse-venvs]

`make shim-parity` runs it with the wheels of `make wheel shim` (dist/) and a work directory under build/.

What it does, all inside --work (never in the build123d checkout, never in any existing venv):

1. `git archive HEAD` of the build123d checkout, extracted twice -- one copy per side, because the suite writes files
   into its working directory and the two sides run at the same time.
2. Two fresh venvs on --python, each with build123d's runtime dependencies (its pyproject's [project].dependencies)
   and the pytest plugins of its `development` extra (pytest-cov left out). build123d itself is *not* installed:
   setuptools-scm collects package data from git, so an install from an archive loses the fonts; the suite imports
   it from the copy through PYTHONPATH=<copy>/src instead.
     baseline  the real `cadquery-ocp-novtk` from PyPI, as the dependency list says;
     shim      OCP3x's wheel and the shim wheel (which *is* cadquery-ocp-novtk 8.0.1.0.0), given as files so the
               resolver takes them instead of PyPI's.
   Before running, each venv is asked where `OCP` comes from, so a baseline that silently got the shim (or the
   reverse) fails here instead of producing a perfect "parity".
3. `python -m pytest tests -q -p no:cacheprovider --junitxml=... --rootdir <copy> -c <copy>/pyproject.toml` in each
   copy, both sides in parallel.
4. The two JUnit files compared per test ID (classname::name): outcome counts per side, IDs present on one side only,
   and every ID whose outcome differs. Exit status 0 only if the ID sets are equal and no outcome differs.

A green run is necessary, not sufficient: some build123d tests assert nothing (`test_exporters_in_memory` passed with
an empty buffer, State.md 8.6).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import tomllib
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIDES = ("baseline", "shim")
WHERE_IS_OCP = ("import OCP, importlib.metadata as m; "
                "print(OCP.__file__); print(m.version('cadquery-ocp-novtk')); "
                "print(any(p.suffix in ('.so', '.pyd') for p in __import__('pathlib').Path(OCP.__file__).parent.rglob('*')))")


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    print("+", " ".join(str(c) for c in cmd), flush=True)
    return subprocess.run(cmd, check=True, **kw)


def one_wheel(dist: Path, pattern: str) -> Path:
    found = sorted(dist.glob(pattern))
    if len(found) != 1:
        sys.exit(f"expected exactly one {pattern} in {dist}, found {[f.name for f in found]} -- run `make wheel shim` first")
    return found[0]


def extract(build123d: Path, dest: Path) -> str:
    """A clean copy of build123d's HEAD in dest (recreated); returns the commit."""
    commit = run(["git", "-C", str(build123d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    archive = subprocess.Popen(["git", "-C", str(build123d), "archive", "HEAD"], stdout=subprocess.PIPE)
    run(["tar", "-x", "-C", str(dest)], stdin=archive.stdout)
    if archive.wait() != 0:
        sys.exit("git archive failed")
    return commit


def requirements(copy: Path) -> tuple[list[str], list[str]]:
    """(runtime dependencies, test plugins) from the copy's pyproject.toml."""
    project = tomllib.loads((copy / "pyproject.toml").read_text())["project"]
    plugins = [r for r in project["optional-dependencies"]["development"]
               if r.startswith("pytest") and not r.startswith("pytest-cov")]
    return list(project["dependencies"]), plugins


def make_venv(venv: Path, python: str, packages: list[str], reuse: bool) -> Path:
    exe = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if reuse and exe.exists():
        return exe
    run(["uv", "venv", "-q", "--clear", "-p", python, str(venv)])   # a rerun: uv refuses an existing venv without --clear
    run(["uv", "pip", "install", "-q", "-p", str(exe), *packages])
    return exe


def clean_env(copy: Path) -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "VIRTUAL_ENV", "PYTHONHOME")}
    env["PYTHONPATH"] = str(copy / "src")
    return env


def run_suite(exe: Path, copy: Path, junit: Path, log: Path) -> int:
    # rootdir and config pinned to the copy: its pyproject.toml has no pytest section, so pytest would search upwards
    # and, with --work inside this repository (`make shim-parity`: build/shim-parity), take OCP3x's own pyproject.toml
    # -- its settings (pythonpath = ".") and a rootdir that puts the side's path into every test ID, so the two sides
    # had no ID in common (2026-09-26)
    with log.open("w") as out:
        return subprocess.run([str(exe), "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider", f"--junitxml={junit}",
                               "--rootdir", str(copy), "-c", str(copy / "pyproject.toml")],
                              cwd=copy, env=clean_env(copy), stdout=out, stderr=subprocess.STDOUT).returncode


def outcomes(junit: Path) -> dict[str, str]:
    """test ID -> passed | failed | error | skipped. A repeated ID (parametrised subtests reported alike) keeps the
    worst outcome, so a failing repetition cannot hide behind a passing one."""
    rank = {"passed": 0, "skipped": 1, "failed": 2, "error": 3}
    result: dict[str, str] = {}
    for case in ET.parse(junit).getroot().iter("testcase"):
        test_id = f"{case.get('classname')}::{case.get('name')}"
        tags = {child.tag for child in case}
        outcome = "error" if "error" in tags else "failed" if "failure" in tags else "skipped" if "skipped" in tags else "passed"
        if test_id not in result or rank[outcome] > rank[result[test_id]]:
            result[test_id] = outcome
    return result


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="shim/parity.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--build123d", type=Path, default=Path.home() / "Development" / "CAD" / "build123d")
    ap.add_argument("--dist", type=Path, default=ROOT / "dist", help="where OCP3x's and the shim's wheels are")
    ap.add_argument("--work", type=Path, default=ROOT / "build" / "shim-parity")
    ap.add_argument("--python", default="3.14")
    ap.add_argument("--reuse-venvs", action="store_true", help="keep existing venvs in --work (after a first full run)")
    args = ap.parse_args(argv)

    ocp3x_whl, shim_whl = one_wheel(args.dist, "ocp3x-*.whl"), one_wheel(args.dist, "cadquery_ocp_novtk-*.whl")
    work = args.work.resolve()
    work.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()

    copies = {side: work / side / "build123d" for side in SIDES}
    commit = ""
    for copy in copies.values():
        commit = extract(args.build123d, copy)
    deps, plugins = requirements(copies["baseline"])
    packages = {"baseline": [*deps, *plugins], "shim": [str(ocp3x_whl), str(shim_whl), *deps, *plugins]}
    exes = {side: make_venv(work / side / "venv", args.python, packages[side], args.reuse_venvs) for side in SIDES}

    origin = {}
    for side in SIDES:
        lines = run([str(exes[side]), "-c", WHERE_IS_OCP], capture_output=True, text=True,
                    env=clean_env(copies[side])).stdout.split()
        origin[side] = {"OCP": lines[0], "version": lines[1], "native": lines[2] == "True"}
        print(f"{side}: OCP from {lines[0]} (cadquery-ocp-novtk {lines[1]}, native modules: {lines[2]})", flush=True)
    if origin["baseline"]["native"] is not True or origin["shim"]["native"] is not False:
        sys.exit("the baseline must import the real (native) OCP and the shim side the pure-Python shim")

    junit = {side: work / side / "junit.xml" for side in SIDES}
    with ThreadPoolExecutor(2) as pool:
        codes = dict(zip(SIDES, pool.map(lambda s: run_suite(exes[s], copies[s], junit[s], work / s / "pytest.log"), SIDES)))
    results = {side: outcomes(junit[side]) for side in SIDES}

    only = {side: sorted(set(results[side]) - set(results[other])) for side, other in (SIDES, SIDES[::-1])}
    differ = sorted(t for t in set(results["baseline"]) & set(results["shim"]) if results["baseline"][t] != results["shim"][t])
    summary = {
        "build123d_commit": commit, "python": args.python, "ocp3x_wheel": ocp3x_whl.name, "shim_wheel": shim_whl.name,
        "ocp": origin, "pytest_exit": codes, "counts": {side: dict(Counter(results[side].values())) for side in SIDES},
        "ids": {side: len(results[side]) for side in SIDES}, "only_in": only,
        "differing": {t: {side: results[side][t] for side in SIDES} for t in differ},
        "minutes": round((time.monotonic() - started) / 60, 1),
    }
    (work / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    for side in SIDES:
        print(f"{side:8} {summary['ids'][side]} IDs  {summary['counts'][side]}  (pytest exit {codes[side]}, log {work / side / 'pytest.log'})")
    print(f"only in baseline: {len(only['baseline'])}, only in shim: {len(only['shim'])}, differing outcomes: {len(differ)}")
    for t in differ:
        print(f"  {t}: baseline {results['baseline'][t]}, shim {results['shim'][t]}")
    print(f"summary: {work / 'summary.json'} ({summary['minutes']} min)")
    return 0 if len(differ) == 0 and len(only["baseline"]) == 0 and len(only["shim"]) == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
