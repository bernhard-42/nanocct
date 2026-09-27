"""Every toolkit module must be importable on its own.

`OCP3x/__init__.py` imports nothing since 2026-09-24 (Design.md 6a), so whichever module a user reaches first is
the one that has to bring up its own dependencies. Until then the eager import always loaded all 45 in one working
order, which hid five modules that could not stand alone: `_TKV3d` and `_TKMeshVS` died on a cross-toolkit alias
that imported back into a half-initialised module, and `_TKXmlL`, `_TKXml` and `_TKXmlXCAF` aborted outright because
their classes derive from instantiations `TKBinL` binds and nothing said so.

Both failures are silent in the wrong way: the second is a `nanobind` `fail()`, which aborts the process with
"Critical nanobind error" and no traceback. So each import runs in a subprocess of its own, and the check is simply
that it exits 0.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
MANIFEST = ROOT / "src" / "cpp" / "manifest.json"

pytestmark = pytest.mark.skipif(not MANIFEST.exists(), reason="generated sources not present (run the generator)")


def _toolkits() -> list[str]:
    return sorted(set(json.loads(MANIFEST.read_text())["packages"].values()))


def _packages() -> dict[str, str]:
    return json.loads(MANIFEST.read_text())["packages"]


def _import(statement: str) -> subprocess.CompletedProcess:
    """One import in a fresh interpreter: a registration failure aborts the process rather than raising."""
    return subprocess.run([sys.executable, "-c", statement], capture_output=True, text=True, cwd=ROOT)


def _first_failure(results: dict[str, subprocess.CompletedProcess]) -> str:
    bad = {name: r for name, r in results.items() if r.returncode != 0}
    return "\n".join(f"{name}: rc={r.returncode} {(r.stderr or '').strip().splitlines()[-1:]}"
                     for name, r in sorted(bad.items()))


def _run_all(statements: dict[str, str]) -> dict[str, subprocess.CompletedProcess]:
    with ThreadPoolExecutor(min(16, len(statements))) as pool:
        futures = {name: pool.submit(_import, stmt) for name, stmt in statements.items()}
        return {name: f.result() for name, f in futures.items()}


def test_every_toolkit_module_imports_on_its_own():
    """No toolkit may depend on another having been imported first: the import list each module emits
    (EXTERNLIB + the R-LINK extras that precede it + the base-class edges of _base_import_edges) must be complete."""
    results = _run_all({tk: f"import OCP3x._{tk}" for tk in _toolkits()})
    assert all(r.returncode == 0 for r in results.values()), "toolkit modules that cannot stand alone:\n" + _first_failure(results)


def test_every_package_shim_imports_on_its_own():
    """The same for what a user actually writes -- `from OCP3x.gp import gp_Pnt` -- including the packages whose
    shim carries a late R-LINK import (TKDE, TKDECascade, TKDEGLTF -> TKXSBase, which they link but cannot import
    while registering)."""
    results = _run_all({pkg: f"import OCP3x.{pkg}" for pkg in _packages()})
    assert all(r.returncode == 0 for r in results.values()), "package shims that cannot stand alone:\n" + _first_failure(results)


def test_importing_one_package_does_not_load_every_toolkit():
    """The point of the 45-way split: `gp` must not drag in STEP, IGES and OpenGL. Without this the lazy
    __init__.py could regress to the eager one unnoticed -- it cost 172 ms and 179 MB to reach gp_Pnt."""
    out = _import("import re, sys; from OCP3x.gp import gp_Pnt; "
                  "print(len([m for m in sys.modules if re.fullmatch(r'OCP3x\\._TK\\w+', m)]))")
    assert out.returncode == 0, out.stderr
    loaded = int(out.stdout.strip().splitlines()[-1])
    assert loaded <= 4, f"importing OCP3x.gp loaded {loaded} toolkit extensions; it needs _TKernel and _TKMath"


def test_ncollection_loads_every_toolkit_that_binds_into_it():
    """`OCP3x.NCollection` is the one module other toolkits bind into (6a), and loading an instantiation's element
    types does not load the toolkit that binds it (215 of 799 instantiations, 2026-09-27) -- so importing the
    package loads each of those toolkits, and every instantiation is an ordinary attribute afterwards: no module
    __getattr__, no completion table. The other packages stay lazy: importing gp does not import NCollection."""
    out = _import("import re, sys\n"
                  "import OCP3x.gp\n"
                  "gp_alone = 'OCP3x.NCollection' in sys.modules\n"
                  "from OCP3x import NCollection\n"
                  "loaded = len([m for m in sys.modules if re.fullmatch(r'OCP3x\\._TK\\w+', m)])\n"
                  "print(gp_alone, loaded, 'NCollection_List__TopoDS_Shape' in vars(NCollection), hasattr(NCollection, '__getattr__'))")
    assert out.returncode == 0, out.stderr
    gp_alone, loaded, in_dict, has_getattr = out.stdout.strip().splitlines()[-1].split()
    assert gp_alone == "False", "importing OCP3x.gp imported OCP3x.NCollection, and with it most toolkits"
    assert in_dict == "True" and has_getattr == "False"
    assert 30 <= int(loaded) < len(_toolkits()), f"import OCP3x.NCollection loaded {loaded} toolkits (37 on 2026-09-27)"


def test_a_missing_name_still_raises_attribute_error():
    """A misspelt name is an AttributeError, not an import attempt."""
    out = _import("from OCP3x import NCollection\n"
                  "try:\n"
                  "    NCollection.NCollection_NoSuchThing\n"
                  "except AttributeError as e:\n"
                  "    print('AttributeError', e)")
    assert out.returncode == 0, out.stderr
    assert "AttributeError" in out.stdout


def test_import_all_loads_every_toolkit():
    """`import OCP3x.all` is the opt-in for everything: it warms Gatekeeper's verification of the OCCT libraries
    after a wheel install on macOS, and it is what makes OCCT's plugin registries complete -- a DE provider only
    exists once its toolkit has been loaded, because OCCT registers them from static initialisers."""
    out = _import("import re, sys, OCP3x.all\n"
                  "print(len([m for m in sys.modules if re.fullmatch(r'OCP3x\\._TK\\w+', m)]), len(OCP3x.all.TOOLKITS))")
    assert out.returncode == 0, out.stderr
    loaded, declared = (int(x) for x in out.stdout.strip().splitlines()[-1].split())
    assert loaded == declared == len(_toolkits()), f"loaded {loaded}, declared {declared}, expected {len(_toolkits())}"


def test_import_ocp3x_alone_loads_nothing_but_attribute_access_works():
    """`import OCP3x` then `OCP3x.gp.gp_Pnt` is the spelling people arrive with from OCP, and it works without
    giving up laziness: PEP 562 module __getattr__ imports the package on first access (Design.md 5.1). Importing
    OCP3x itself must load no toolkit at all."""
    out = _import("import re, sys, OCP3x\n"
                  "before = len([m for m in sys.modules if re.fullmatch(r'OCP3x\\._TK\\w+', m)])\n"
                  "x = OCP3x.gp.gp_Pnt(1, 2, 3).X()\n"
                  "after = len([m for m in sys.modules if re.fullmatch(r'OCP3x\\._TK\\w+', m)])\n"
                  "print(before, after, x, 'gp' in dir(OCP3x))")
    assert out.returncode == 0, out.stderr
    before, after, x, has_gp = out.stdout.strip().splitlines()[-1].split()
    assert int(before) == 0, f"import OCP3x loaded {before} toolkits; it must load none"
    assert 0 < int(after) <= 4 and x == "1.0" and has_gp == "True"


def test_an_unknown_attribute_on_ocp3x_is_an_attribute_error():
    """The lazy package lookup must not turn a typo into an import attempt."""
    out = _import("import OCP3x\n"
                  "try:\n"
                  "    OCP3x.NoSuchPackage\n"
                  "except AttributeError as e:\n"
                  "    print('AttributeError', e)")
    assert out.returncode == 0, out.stderr
    assert "AttributeError" in out.stdout

