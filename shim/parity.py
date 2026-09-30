"""build123d's and ocp-tessellate's own test suites through the OCP shim, compared test by test with the real OCP.

    python shim/parity.py [--build123d DIR] [--ocp-tessellate SDIST] [--dist DIR] [--work DIR] [--python 3.14]
                          [--reuse-venvs]

`make shim-parity` runs it with the wheels of `make wheel shim` (dist/) and a work directory under build/.

What it does, all inside --work (never in the build123d checkout, never in any existing venv):

1. `git archive HEAD` of the build123d checkout, extracted twice -- one copy per side, because the suite writes files
   into its working directory and the two sides run at the same time.
   ocp-tessellate comes from the verified sdist nanocctbuild fetched (build/nanocctbuild/sdist), extracted once per
   side, with the files of nanocctbuild/tools/files (its test image) and only the tests/test_build123d.py part of its
   hand-made patch (nanocctbuild/tools/manual): that part drops the BuildSheet tests, BuildSheet not being in build123d;
   the rest of the patch is the port to nanocct, and both sides here run on OCP. Its cadquery tests are left out.
2. Two fresh venvs on --python, each with build123d's and ocp-tessellate's runtime dependencies (their pyprojects'
   [project].dependencies) and the pytest plugins of build123d's `development` extra (pytest-cov left out). Neither
   package is installed; ocp-tessellate is imported from its copy. build123d itself is *not* installed:
   setuptools-scm collects package data from git, so an install from an archive loses the fonts; the suite imports
   it from the copy through PYTHONPATH=<copy>/src instead.
     baseline  the real `cadquery-ocp-novtk` from PyPI, as the dependency list says;
     shim      nanocct's wheel and the shim wheel (cadquery-ocp-novtk 8.0.1.0.0+shim), given as files so the
               resolver takes them instead of PyPI's.
   Before running, each venv is asked where `OCP` comes from, so a baseline that silently got the shim (or the
   reverse) fails here instead of producing a perfect "parity".
3. `python -m pytest tests -q -p no:cacheprovider --junitxml=... --rootdir <copy> -c <copy>/pyproject.toml` in each
   copy, build123d then ocp-tessellate, both sides in parallel.
4. Per suite, the two JUnit files compared per test ID (classname::name): outcome counts per side, IDs present on one
   side only, and every ID whose outcome differs. Exit status 0 only if, in every suite, the ID sets are equal and no
   outcome differs.

A green run is necessary, not sufficient: some build123d tests assert nothing (`test_exporters_in_memory` passed with
an empty buffer).
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


def clean_env(paths: list[Path]) -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "VIRTUAL_ENV", "PYTHONHOME")}
    env["PYTHONPATH"] = os.pathsep.join(str(p) for p in paths)
    return env


def extract_sdist(tarball: Path, dest: Path) -> None:
    """The sdist in dest (recreated), plus nanocctbuild's extra files and the test-only part of its hand-made patch."""
    pkg = tarball.name.removesuffix(".tar.gz")
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    run(["tar", "-xzf", str(tarball), "-C", str(dest.parent)])
    (dest.parent / pkg).rename(dest)
    files = ROOT / "nanocctbuild" / "tools" / "files" / pkg
    if files.is_dir():
        shutil.copytree(files, dest, dirs_exist_ok=True)
    manual = (ROOT / "nanocctbuild" / "tools" / "manual" / f"{pkg}.patch").read_text()
    sections = ["--- " + part for part in manual.split("\n--- ")[1:] if part.startswith("a/tests/test_build123d.py")]
    if manual.startswith("--- a/tests/test_build123d.py"):
        sections.insert(0, manual.split("\n--- ")[0])
    test_patch = "\n".join(sections)
    if "nanocct" in test_patch:
        sys.exit(f"{pkg}: the test_build123d.py part of the hand-made patch now ports to nanocct -- only its BuildSheet "
                 "removal is meant for the parity check; split it before running this")
    if test_patch != "":
        run(["patch", "-p1", "--forward", "--quiet", "-d", str(dest)], input=test_patch.rstrip("\n") + "\n", text=True)


def run_suite(exe: Path, copy: Path, paths: list[Path], extra: list[str], junit: Path, log: Path) -> int:
    # rootdir and config pinned to the copy: its pyproject.toml has no pytest section, so pytest would search upwards
    # and, with --work inside this repository (`make shim-parity`: build/shim-parity), take nanocct's own pyproject.toml
    # -- its settings (pythonpath = ".") and a rootdir that puts the side's path into every test ID, so the two sides
    # had no ID in common (2026-09-26)
    with log.open("w") as out:
        return subprocess.run([str(exe), "-m", "pytest", "tests", "-q", "-p", "no:cacheprovider", f"--junitxml={junit}",
                               "--rootdir", str(copy), "-c", str(copy / "pyproject.toml"), *extra],
                              cwd=copy, env=clean_env(paths), stdout=out, stderr=subprocess.STDOUT).returncode


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
    ap.add_argument("--ocp-tessellate", type=Path, default=None,
                    help="its sdist (default: the one nanocctbuild fetched into build/nanocctbuild/sdist)")
    ap.add_argument("--dist", type=Path, default=ROOT / "dist", help="where nanocct's and the shim's wheels are")
    ap.add_argument("--work", type=Path, default=ROOT / "build" / "shim-parity")
    ap.add_argument("--python", default="3.14")
    ap.add_argument("--reuse-venvs", action="store_true", help="keep existing venvs in --work (after a first full run)")
    args = ap.parse_args(argv)

    nanocct_whl, shim_whl = one_wheel(args.dist, "nanocct-*.whl"), one_wheel(args.dist, "cadquery_ocp_novtk-*.whl")
    tess_sdist = args.ocp_tessellate
    if tess_sdist is None:
        found = sorted((ROOT / "build" / "nanocctbuild" / "sdist").glob("ocp_tessellate-*.tar.gz"))
        if len(found) != 1:
            sys.exit("no ocp_tessellate sdist in build/nanocctbuild/sdist -- run nanocctbuild/nanocctbuild.sh first")
        tess_sdist = found[0]
    work = args.work.resolve()
    work.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()

    copies = {side: work / side / "build123d" for side in SIDES}
    tess = {side: work / side / "ocp_tessellate" for side in SIDES}
    commit = ""
    for side in SIDES:
        commit = extract(args.build123d, copies[side])
        extract_sdist(tess_sdist, tess[side])
    deps, plugins = requirements(copies["baseline"])
    tess_deps = list(tomllib.loads((tess["baseline"] / "pyproject.toml").read_text())["project"]["dependencies"])
    common = [*deps, *tess_deps, *plugins]
    packages = {"baseline": common, "shim": [str(nanocct_whl), str(shim_whl), *common]}
    exes = {side: make_venv(work / side / "venv", args.python, packages[side], args.reuse_venvs) for side in SIDES}

    origin = {}
    for side in SIDES:
        lines = run([str(exes[side]), "-c", WHERE_IS_OCP], capture_output=True, text=True,
                    env=clean_env([copies[side] / "src"])).stdout.split()
        origin[side] = {"OCP": lines[0], "version": lines[1], "native": lines[2] == "True"}
        print(f"{side}: OCP from {lines[0]} (cadquery-ocp-novtk {lines[1]}, native modules: {lines[2]})", flush=True)
    if origin["baseline"]["native"] is not True or origin["shim"]["native"] is not False:
        sys.exit("the baseline must import the real (native) OCP and the shim side the pure-Python shim")

    # (suite, working copy per side, PYTHONPATH per side, extra pytest arguments)
    suites = {
        "build123d": (copies, {s: [copies[s] / "src"] for s in SIDES}, []),
        # test_cadquery.py and test_color.py need cadquery, which is not part of this check
        "ocp_tessellate": (tess, {s: [tess[s], copies[s] / "src"] for s in SIDES},
                           ["--ignore", "tests/test_cadquery.py", "--ignore", "tests/test_color.py"]),
    }

    def run_side(side: str) -> dict[str, int]:
        return {name: run_suite(exes[side], where[side], paths[side], extra, work / side / f"junit-{name}.xml",
                                work / side / f"pytest-{name}.log")
                for name, (where, paths, extra) in suites.items()}

    with ThreadPoolExecutor(2) as pool:
        codes = dict(zip(SIDES, pool.map(run_side, SIDES)))

    summary = {"build123d_commit": commit, "ocp_tessellate_sdist": tess_sdist.name, "python": args.python,
               "nanocct_wheel": nanocct_whl.name, "shim_wheel": shim_whl.name, "ocp": origin, "suites": {}}
    clean = True
    for name in suites:
        results = {side: outcomes(work / side / f"junit-{name}.xml") for side in SIDES}
        only = {side: sorted(set(results[side]) - set(results[other])) for side, other in (SIDES, SIDES[::-1])}
        differ = sorted(t for t in set(results["baseline"]) & set(results["shim"])
                        if results["baseline"][t] != results["shim"][t])
        summary["suites"][name] = {
            "pytest_exit": {side: codes[side][name] for side in SIDES},
            "counts": {side: dict(Counter(results[side].values())) for side in SIDES},
            "ids": {side: len(results[side]) for side in SIDES}, "only_in": only,
            "differing": {t: {side: results[side][t] for side in SIDES} for t in differ},
        }
        print(f"== {name}")
        for side in SIDES:
            print(f"{side:8} {len(results[side])} IDs  {dict(Counter(results[side].values()))}  "
                  f"(pytest exit {codes[side][name]}, log {work / side / f'pytest-{name}.log'})")
        print(f"only in baseline: {len(only['baseline'])}, only in shim: {len(only['shim'])}, "
              f"differing outcomes: {len(differ)}")
        for t in differ:
            print(f"  {t}: baseline {results['baseline'][t]}, shim {results['shim'][t]}")
        clean = clean and len(differ) == 0 and len(only["baseline"]) == 0 and len(only["shim"]) == 0
    summary["minutes"] = round((time.monotonic() - started) / 60, 1)
    (work / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"summary: {work / 'summary.json'} ({summary['minutes']} min)")
    return 0 if clean else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
