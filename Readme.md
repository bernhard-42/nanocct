![](./nanocct.png)

---

# -&nbsp;-&nbsp; *E X P E R I M E N T A L*  &nbsp;-&nbsp;-

---

# nanocct

**Open Cascade bindings created with nanobind for the stable ABI of Python 3**

---

[Open Cascade](https://github.com/Open-Cascade-SAS/OCCT) (OCCT) is a commonly used 3D CAD kernel for open source projects. It already has established Python bindings in [OCP](https://github.com/cadquery/OCP) and [pythonocc](https://github.com/tpaviot/pythonocc-core), and a whole ecosystem builds on them. _nanocct_ takes a different route, started fresh with OCCT 8 and [nanobind](https://github.com/wjakob/nanobind) and makes OCCT 8 available to Python, class for class and method for method, so that code reads like the OCCT reference manual.


## Design principles


_nanocct_ follows **3 design principles**:

1. **One wheel per platform for the stable ABI of Python 3**: The bindings are built with nanobind against the Python 3 stable ABI, so a single `cp312-abi3` wheel runs on 3.12, 3.13, 3.14 and later without a rebuild. ([Design 4.1](Design.md#41-stable-abi))

2. **Coverage of Open Cascade**: Support of the OCCT modules *FoundationClasses*, *ModelingData*, *ModelingAlgorithms*, _Visualization_ (without _VTK_, which would break principle 1), _ApplicationFramework_, and _DataExchange_, and keep the syntax as near to the Open Cascade C++ API as possible ([Design 2](Design.md#2-scope))

3. **Make the bindings Python'ish**: Provide addon features that make _nanocct_ fit well into the Python ecosystem, within the constraints of principle 2 (e.g. names stay OCCT's CamelCase). ([Design 2c](Design.md#2c-python-additions))


## Key features

From principle 2:

- **The OCCT reference manual is the documentation.** Names follow the OCCT headers, without renaming for Python taste, so the [Open Cascade reference manual](https://occt3d.com/dev/doc/refman/html/index.html) applies as it is, and OCCT's own `//!` comments are the docstrings. ([Design 2a](Design.md#2a-naming-conventions))

From principle 3 (see [Pythonic-OCCT.md](./Pythonic-OCCT.md)):

- **The OCCT 8 collection classes are Python generics.** `NCollection_IndexedDataMap[TCollection_AsciiString, TCollection_AsciiString]()` creates that instantiation, and `isinstance(x, NCollection_Array1)` holds for every array, whatever its element type. [Design 2a](Design.md#2a-naming-conventions), [6a](Design.md#6a-ncollection-containers-hand-written-binders)
- **Zero-copy access to OCCT's arrays.** Triangulation nodes, triangles, UVs and normals, the `NCollection` arrays and `Image_PixMap` are numpy views of OCCT's own memory through `np.asarray(obj)`, not copies. ([Design 2c](Design.md#2c-python-additions))
- **Iterators.** `for e in TopExp_Explorer(shape, TopAbs_EDGE)` and `for x in array`: every OCCT iterator with `More()`/`Next()`/`Value()` and every `NCollection` container is a Python iterable. ([Design 2c](Design.md#2c-python-additions))
- **Out-parameters come back as results.** A C++ reference parameter that OCCT writes into is part of the Python return value: `curve, first, last = BRep_Tool.Curve_s(edge)`. ([Design 2b](Design.md#2b-parameter-conventions))
- **Data exchange in memory.** An output stream is a returned `str` (`bytes` for binary formats), an input stream any file-like object: `BRepTools.Write_s(shape)` returns the BREP text, STEP and the OCAF documents work the same way. ([Design 2b](Design.md#2b-parameter-conventions))
- **Type stubs in the package**, checked with mypy and ty as part of the test suite. ([Design 6b](Design.md#6b-type-stubs))

_nanocct_ ships a few selected **AddOns** ([Design 6](Design.md#6-binding-rules-11-and-the-documented-deviations), R-ADDON): 
- C++ helpers where a Python loop over OCCT calls would dominate (`nanocct.AddOns.Tessellator`) 
- Workarounds (not patches and very rarely) for OCCT bugs that hit often and are not fixed upstream — each with a test that fails once OCCT fixes the bug, so it can be removed again (`nanocct.AddOns.ShapeClean.ShapeClean`)


## Validation

_nanocct_ **comes with its own test suite** of about 900 tests, run against the repaired wheel in a fresh environment by every build (`make test`), on all five platforms in CI. One test file per toolkit checks that the bindings behave as OCCT does; the generator itself is tested on synthetic headers that exercise its binding rules. Lifetime tests drop the owner or the result of every ownership rule in a fresh interpreter with the allocator's scribbling switched on, leak tests check that repeating each life cycle keeps memory flat, and the type stubs are checked with mypy and ty.

_nanocct_ is also **validated against real code.** The full test suites of nanocct-enabled versions of [build123d](https://github.com/gumyr/build123d) (2 465 tests), ocpsvg, ocp_gordon and ocp_tessellate run on _nanocct_ with the same outcome, test by test, as with the OCP bindings they were written for.


## A first look

```python
import numpy as np
from nanocct.BRep import BRep_Tool
from nanocct.BRepMesh import BRepMesh_IncrementalMesh
from nanocct.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from nanocct.BRepTools import BRepTools
from nanocct.TopAbs import TopAbs_ShapeEnum
from nanocct.TopExp import TopExp_Explorer
from nanocct.TopLoc import TopLoc_Location
import nanocct.TopoDS as TopoDS

shape = BRepPrimAPI_MakeCylinder(5.0, 10.0).Shape()
BRepMesh_IncrementalMesh(shape, 0.1)

for face in TopExp_Explorer(shape, TopAbs_ShapeEnum.TopAbs_FACE):
    mesh = BRep_Tool.Triangulation_s(TopoDS.Face(face), TopLoc_Location())
    nodes = np.asarray(mesh.InternalNodes())    # (N, 3) numpy view of OCCT's memory, no copy

edge = TopoDS.Edge(next(iter(TopExp_Explorer(shape, TopAbs_ShapeEnum.TopAbs_EDGE))))
curve, first, last = BRep_Tool.Curve_s(edge)    # out-parameters come back in the result
brep = BRepTools.Write_s(shape)                 # a BREP in memory, as str
```

## Status

- OCCT 8.0.1, 45 toolkits: FoundationClasses, ModelingData, ModelingAlgorithms, Visualization (without VTK), ApplicationFramework and DataExchange. [Design 2](Design.md#2-scope)
- Built and tested on five platforms: macOS arm64 and x86_64, Linux x86_64 and aarch64 (`manylinux_2_28`) and Windows x64. The wheels bundle OCCT, FreeType and FreeImage; the only Python dependency is numpy.
- Not on PyPI yet (the distribution will be `nanocct`): download the wheels from the [release page](https://github.com/bernhard-42/nanocct/releases) or build them from source with the `Makefile`. [Design 7](Design.md#7-build-and-packaging)
- Porting from OCP: [Design 8b](Design.md#8b-porting-from-ocp-cadquery-ocp-to-nanocct)

## How to start with build123d on nanocct

Neither wheel is on PyPI yet: download them from the [release page](https://github.com/bernhard-42/nanocct/releases) to `dist`, or build them first (see [How to build nanocct](#how-to-build-nanocct)), they land in `dist/`.

### Use the OCP shim

The shim is a compatibility layer: a thin facade that maps OCP calls to nanocct calls, so packages that still import OCP run unchanged on top of nanocct while they are ported. In an environment with build123d installed, install nanocct and the shim wheel from `dist/`:

```bash
uv pip install dist/nanocct-*.whl "dist/cadquery_ocp_novtk-8.0.1.0.0+shim-py3-none-any.whl"
```

The shim replaces the installed `cadquery-ocp-novtk` by itself; `uv pip list` shows it as `cadquery-ocp-novtk 8.0.1.0.0+shim`. build123d and ocp-tessellate then work as before — their full test suites pass through the shim with the same outcome, test by test, as with the original OCP bindings. The OCCT bug workarounds of nanocct's AddOns reach build123d only through nanocctbuild.

### Use nanocctbuild

```bash
make nanocctbuild
```

This downloads ocpsvg, ocp-gordon, ocp-tessellate, build123d and ocp-viewer-core from PyPI, patches them to use nanocct directly, and installs them with the nanocct wheel from `dist/` into a new Python 3.14 environment `_scratch/.venv` (an existing one there is replaced). Install ocp-vscode or ocp-viewer into it if you want to view objects built with build123d on top of nanocct; both run on the patched ocp-viewer-core.

## How to build nanocct

Prerequisites: `git`, `curl`, [uv](https://docs.astral.sh/uv/), CMake and Ninja; on macOS the Xcode command line tools, on Linux Docker (the build runs in a `manylinux_2_28` container), on Windows Git Bash and the Visual Studio Build Tools (MSVC). [Design 3](Design.md#3-toolchain-and-third-party-dependencies), [Design 7](Design.md#7-build-and-packaging)

- Clone the repo

    ```bash
    git clone https://github.com/bernhard-42/nanocct
    cd nanocct
    ```

- Create the Python environment the build uses (`.venv`)

    ```bash
    make env
    ```

- Build the dependencies OCCT 8.0.1, FreeType, FreeImage and RapidJSON

    ```bash
    make deps
    ```

- Build the bindings: generate, compile, stubs, pack and repair the wheel, test the repaired wheel in a fresh environment, and the shim's wheel -- both wheels into `dist/`

    ```bash
    make wheels
    ```

## License

nanocct's own code is Apache-2.0 ([LICENSE](LICENSE)). The wheels bundle OCCT (LGPL-2.1 with the OCCT exception), FreeType and FreeImage; [licenses/](licenses/README.md) and [NOTICE](NOTICE) say which terms apply and why.
