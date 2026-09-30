"""Every toolkit module must be importable on its own.

`nanocct/__init__.py` imports nothing since 2026-09-24 (Design.md 6a), so whichever module a user reaches first is
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
    results = _run_all({tk: f"import nanocct._{tk}" for tk in _toolkits()})
    assert all(r.returncode == 0 for r in results.values()), "toolkit modules that cannot stand alone:\n" + _first_failure(results)


# Walks a toolkit module's packages (and their classes, three levels deep) and returns {member: raw NCollection spellings}
# found in its signatures. nanobind renders a signature when it is read, naming an unregistered type by its C++ spelling.
_RAW_NCOLLECTION = r"""
import importlib, json, re, sys, types
ext = importlib.import_module("nanocct._" + sys.argv[1])
def raw(text):
    return sorted(set(re.findall(r"\bNCollection_\w+<", text)))
def scan():
    found = {}
    def walk(obj, path, depth):
        for name, attr in list(vars(obj).items()):
            sig = getattr(attr, "__nb_signature__", None)
            if sig is not None:
                hits = [h for s in sig for h in raw(s[0] if isinstance(s, tuple) else str(s))]
                if hits:
                    found[path + "." + name] = sorted(set(hits))
            elif depth < 3 and (isinstance(attr, types.ModuleType) and depth == 0      # the packages (nanocct.TDataStd)
                                or isinstance(attr, type) and attr.__module__.startswith("nanocct") and not name.startswith("_")):
                walk(attr, path + "." + name, depth + 1)
    walk(ext, sys.argv[1], 0)
    return found
alone = scan()
import nanocct.all  # noqa: F401  -- every toolkit: whatever resolves now was only missing its owner
everything = scan()
print(json.dumps(sorted(m for m in alone if m not in everything)))
"""


def test_a_toolkit_imported_alone_resolves_the_instantiations_it_uses():
    """6a ownership: the first package in emit order that needs an instantiation binds it, and every later user only uses
    it -- so a toolkit must import the owner's toolkit, or its members that take or return the instantiation are
    uncallable until something else loads it. With only TKLCAF imported `TDataStd_RealList.List()` raised "Unable to
    convert function return value" (TKGeomBase binds NCollection_List<double>): 63 members in 10 toolkits, found by the
    final review (2026-09-30), fixed by the instantiation edges of _base_import_edges. A member whose signature names an
    NCollection type raw when its toolkit is imported alone, but not once every toolkit is, lacks such an edge."""
    with ThreadPoolExecutor(8) as pool:
        futures = {tk: pool.submit(subprocess.run, [sys.executable, "-c", _RAW_NCOLLECTION, tk], capture_output=True,
                                   text=True, cwd=ROOT) for tk in _toolkits()}
        results = {tk: f.result() for tk, f in futures.items()}
    assert all(r.returncode == 0 for r in results.values()), _first_failure(results)
    missing = {tk: json.loads(r.stdout) for tk, r in results.items() if json.loads(r.stdout) != []}
    assert missing == {}, "members whose instantiation's owner toolkit is not imported:\n" + "\n".join(
        f"{tk}: {len(m)}, e.g. {m[:3]}" for tk, m in sorted(missing.items()))


def test_every_package_shim_imports_on_its_own():
    """The same for what a user actually writes -- `from nanocct.gp import gp_Pnt` -- including the packages whose
    shim carries a late R-LINK import (TKDE, TKDECascade, TKDEGLTF -> TKXSBase, which they link but cannot import
    while registering)."""
    results = _run_all({pkg: f"import nanocct.{pkg}" for pkg in _packages()})
    assert all(r.returncode == 0 for r in results.values()), "package shims that cannot stand alone:\n" + _first_failure(results)


def test_importing_one_package_does_not_load_every_toolkit():
    """The point of the 45-way split: `gp` must not drag in STEP, IGES and OpenGL. Without this the lazy
    __init__.py could regress to the eager one unnoticed -- it cost 172 ms and 179 MB to reach gp_Pnt."""
    out = _import("import re, sys; from nanocct.gp import gp_Pnt; "
                  "print(len([m for m in sys.modules if re.fullmatch(r'nanocct\\._TK\\w+', m)]))")
    assert out.returncode == 0, out.stderr
    loaded = int(out.stdout.strip().splitlines()[-1])
    assert loaded <= 4, f"importing nanocct.gp loaded {loaded} toolkit extensions; it needs _TKernel and _TKMath"


def test_ncollection_loads_every_toolkit_that_binds_into_it():
    """`nanocct.NCollection` is the one module other toolkits bind into (6a), and loading an instantiation's element
    types does not load the toolkit that binds it (215 of 799 instantiations, 2026-09-27) -- so importing the
    package loads each of those toolkits, and every instantiation is an ordinary attribute afterwards: no module
    __getattr__, no completion table. The other packages stay lazy: importing gp does not import NCollection."""
    out = _import("import re, sys\n"
                  "import nanocct.gp\n"
                  "gp_alone = 'nanocct.NCollection' in sys.modules\n"
                  "from nanocct import NCollection\n"
                  "loaded = len([m for m in sys.modules if re.fullmatch(r'nanocct\\._TK\\w+', m)])\n"
                  "print(gp_alone, loaded, 'NCollection_List__TopoDS_Shape' in vars(NCollection), hasattr(NCollection, '__getattr__'))")
    assert out.returncode == 0, out.stderr
    gp_alone, loaded, in_dict, has_getattr = out.stdout.strip().splitlines()[-1].split()
    assert gp_alone == "False", "importing nanocct.gp imported nanocct.NCollection, and with it most toolkits"
    assert in_dict == "True" and has_getattr == "False"
    assert 30 <= int(loaded) < len(_toolkits()), f"import nanocct.NCollection loaded {loaded} toolkits (37 on 2026-09-27)"


def test_a_missing_name_still_raises_attribute_error():
    """A misspelt name is an AttributeError, not an import attempt."""
    out = _import("from nanocct import NCollection\n"
                  "try:\n"
                  "    NCollection.NCollection_NoSuchThing\n"
                  "except AttributeError as e:\n"
                  "    print('AttributeError', e)")
    assert out.returncode == 0, out.stderr
    assert "AttributeError" in out.stdout


def test_import_all_loads_every_toolkit():
    """`import nanocct.all` is the opt-in for everything: it warms Gatekeeper's verification of the OCCT libraries
    after a wheel install on macOS, and it is what makes OCCT's plugin registries complete -- a DE provider only
    exists once its toolkit has been loaded, because OCCT registers them from static initialisers."""
    out = _import("import re, sys, nanocct.all\n"
                  "print(len([m for m in sys.modules if re.fullmatch(r'nanocct\\._TK\\w+', m)]), len(nanocct.all.TOOLKITS))")
    assert out.returncode == 0, out.stderr
    loaded, declared = (int(x) for x in out.stdout.strip().splitlines()[-1].split())
    assert loaded == declared == len(_toolkits()), f"loaded {loaded}, declared {declared}, expected {len(_toolkits())}"


def test_import_nanocct_alone_loads_nothing_but_attribute_access_works():
    """`import nanocct` then `nanocct.gp.gp_Pnt` is the spelling people arrive with from OCP, and it works without
    giving up laziness: PEP 562 module __getattr__ imports the package on first access (Design.md 5.1). Importing
    nanocct itself must load no toolkit at all."""
    out = _import("import re, sys, nanocct\n"
                  "before = len([m for m in sys.modules if re.fullmatch(r'nanocct\\._TK\\w+', m)])\n"
                  "x = nanocct.gp.gp_Pnt(1, 2, 3).X()\n"
                  "after = len([m for m in sys.modules if re.fullmatch(r'nanocct\\._TK\\w+', m)])\n"
                  "print(before, after, x, 'gp' in dir(nanocct))")
    assert out.returncode == 0, out.stderr
    before, after, x, has_gp = out.stdout.strip().splitlines()[-1].split()
    assert int(before) == 0, f"import nanocct loaded {before} toolkits; it must load none"
    assert 0 < int(after) <= 4 and x == "1.0" and has_gp == "True"


def test_an_unknown_attribute_on_nanocct_is_an_attribute_error():
    """The lazy package lookup must not turn a typo into an import attempt."""
    out = _import("import nanocct\n"
                  "try:\n"
                  "    nanocct.NoSuchPackage\n"
                  "except AttributeError as e:\n"
                  "    print('AttributeError', e)")
    assert out.returncode == 0, out.stderr
    assert "AttributeError" in out.stdout

