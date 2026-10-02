# 6. Package layout and generator

Part of the nanocct design documents in `docs/`, indexed in [Design.md](Design.md); their section numbers and the `R-…` rule identifiers are shared across them.


## 6.1 Modules and names

- **One extension module per OCCT toolkit**: `nanocct._TKMath`, `nanocct._TKernel`, …
    - mirrors OCCT's link graph; parallel compilation; all share `NB_DOMAIN nanocct` so types cross module boundaries;
    - each toolkit module first imports the toolkit modules OCCT links it against (from `EXTERNLIB.cmake`) plus the R-LINK extras that precede it in the canonical order, so base classes and default-argument types are registered before use; an extra that comes *later* is linked but not imported — that is what keeps the import graph a DAG while `_TKXSBase` imports `_TKDE` and `_TKDE` only links `libTKXSBase`.
    - **R-IMPORT-BASE:** it also imports the toolkit that binds `T` when it binds `NCollection_Shared<T>`, because the wrapper *derives* from `T` (7a) and nanobind needs the base registered first. OCCT's link graph does not imply that edge — `TKMesh` wraps a `NCollection_DataMap<TopoDS_Shape, int, TopTools_ShapeMapHasher>` that `TKBool` binds, and neither toolkit links the other. Unlike the R-LINK extras this edge ignores the EXTERNLIB order, since that order is precisely what puts the base toolkit too late; a cycle among these edges aborts the generator. The same edge goes to the toolkit binding any instantiation the toolkit's signatures use (R-IMPORT-BASE, 6).
- **One Python module per OCCT package**: `nanocct.gp.gp_Pnt`, `nanocct.Geom.Geom_CartesianPoint`.
    - `import nanocct` loads **nothing**, and `nanocct.gp` is resolved on first attribute access by a PEP 562 module `__getattr__` over the generated package list, so both `from nanocct.gp import gp_Pnt` and `import nanocct` + `nanocct.gp.gp_Pnt` work and neither costs more than the toolkit it needs. The one package that is eager is `nanocct.NCollection`, because other toolkits bind into it (7a). `nanocct/__init__.pyi` declares the submodules with `import nanocct.X as X`, the re-export form the typing spec requires, or a checker would reject `nanocct.gp`.
    - Implementation: the toolkit module creates a submodule per package, sets its `__name__` to `nanocct.<pkg>` (so `gp_Pnt.__module__ == "nanocct.gp"`), registers it in `sys.modules["nanocct._<TK>.<pkg>"]`, and a generated shim `src/nanocct/<pkg>.py` does `from nanocct._<TK>.<pkg> import *`.
- **C++ namespaces** (OCCT 8 uses them in the math packages and in ModelingData: `MathUtils`, `Geom2dGridEval`, `TopoDS`, `Geom2dEval_RepCurveDesc`, `BRepGraphInc`):
    - a namespace named like its package **is** the package module (`MathUtils::DepressCubic` → `nanocct.MathUtils.DepressCubic`, `Geom2dGridEval::CurveD1` → `nanocct.Geom2dGridEval.CurveD1`, `TopoDS::Vertex` → `nanocct.TopoDS.Vertex`);
    - every other namespace becomes a **submodule** (`Geom2dEval_RepCurveDesc::Base` → `nanocct.Geom2dEval.Geom2dEval_RepCurveDesc.Base`, nested namespaces nest);
    - implementation: `def_submodule` in the declare phase, registered in `sys.modules["nanocct._<TK>.<pkg>.<ns>"]`; the shim of such a package is a Python package `src/nanocct/<pkg>/__init__.py` with one module per namespace (`<pkg>/<ns>.py`), so `from nanocct.Geom2dEval.Geom2dEval_RepCurveDesc import Base` works and the stubs follow the same layout (`<pkg>/__init__.pyi`, `<pkg>/<ns>.pyi`);
    - nanobind also registers a submodule under `<parent __name__>.<ns>` = `nanocct.<pkg>.<ns>`; that key is popped again, otherwise `import nanocct.<pkg>.<ns>` would find the extension object without importing the package shim (observed as `cannot import name 'Geom2dEval' from 'nanocct'`);
    - namespaces in `overrides.toml [skip] namespaces` (`std`, `detail`, `Detail`, `Internal`) are not bound; anonymous namespaces are reported.
- **Nested classes** (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`, `Geom2dAdaptor_Curve::BezierData`, also when defined out of class: `class BRepGraph::ShapesView { … }`):
    - bound into their outer class (`nanocct.Geom2d.Geom2d_Curve.ResD1`, `__qualname__ == "Geom2d_Curve.ResD1"`), after it, and skipped when the outer class is;
    - the manifest keys are the C++ names (`Geom2d_Curve::ResD1`), and `parse.py_path(name, package, paths)` gives the Python attribute path used by the `NCollection_Xxx[T]` accessor tables, the stubs and cross-package lookups;
    - the name alone cannot tell a *class* named like its package from the package-named namespace (`BRepGraph::ShapesView` must stay `BRepGraph.ShapesView`), nor an alias name of an instantiation: `manifest.json` `paths` records those, computed from the AST.
- **Two registration phases per toolkit**: **declare** all classes and enums of all packages, then **define** members.
    - Reason: nanobind converts default-argument values to Python objects at `.def` time, so every type used in a default must already exist.
    - Packages are declared in base-class dependency order (`FSD_BinaryFile : Storage_BaseDriver` needs `Storage` before `FSD`; computed from the IR, cycles would be reported), classes within a package likewise.
- **Cross-package lookups at registration time** (exception bases) go through the extension submodule `nanocct._<TK>.<pkg>`, never through the `nanocct.<pkg>` shim: importing the shim while the toolkit module is still initialising freezes a half-filled namespace (observed: `nanocct.Standard` with 42 of 120 names).

## 6.2 Generator architecture

`generator/` is a Python package, run as `python -m generator --toolkit TKMath [--package gp]`.

### Files

- `occt.py`: reads OCCT's own `TOOLKITS.cmake`, `PACKAGES.cmake`, `FILES.cmake`, `EXTERNLIB.cmake` for the module → toolkit → package → header tree and toolkit dependencies. No hand-maintained lists.
- `parse.py`: **libclang AST** (`clang.cindex`), one translation unit per package (an umbrella header including all package headers). Builds the IR in `model.py`. File-scope declarations in a package's `X.lxx` (the inline part `X.hxx` includes at its end) count as declarations of `X.hxx`: `std::hash<TDF_Label>`, `std::hash<TCollection_AsciiString>`, `std::hash<TopLoc_Location>`, `ShallowDump(TopLoc_Location)`, `IsEqual(AsciiString, AsciiString)`, the definition of `math_Matrix`'s friend `operator*(double, math_Matrix)` (deduplicated against the in-class friend), `NCollection_UtfStringTool`, the `TDF_Attribute*Msk` constants all live there, and would otherwise be missing (equal strings would hash by identity). Out-of-line member template definitions and explicit specialisations of member class templates (`BRepGraphInc_Storage::TypedStorePlanes<T>`, private) found at file scope are left to the class walk; `opencascade::MurmurHash` (`Standard_HashUtils.lxx`) is a skipped namespace.
    - Function bodies are parsed, because the `nm` check for declared-but-undefined methods needs to see out-of-class inline definitions (`get_definition()`).
    - It uses the **system libclang that pairs with the `clang` on `PATH`** (located from `clang -print-resource-dir`) and falls back to the pip `libclang` wheel. Reason: the pip wheel is stuck at clang 18 and cannot parse the libc++ of the current Apple SDK (`__builtin_clzg`); the pip wheel also ships no builtin headers, so `-resource-dir` must be passed explicitly. On Linux and Windows the pip wheel's clang 18 is the one used; it spells some types differently from Xcode's, one reason the generated API differs per platform (6.3).
- `binders.py`: the data-only `BINDERS` table of the NCollection binder kinds (7a) — separate from `ncollection.py` (docstring extraction, coverage check, deprecated aliases; needs libclang) so that `parse.py`, `stubs.py` and `__main__.py` import it at top level without a cycle.
- `emit.py`: IR → C++ with plain f-strings, no template engine. The `#include` list is the package headers (prelude first) plus the header of every identifier the emitted code mentions **and of every class behind a typedef in a signature** (`IMeshData::IFaceHandle` = `handle<IMeshData_Face>`, whose header nothing else pulls in), checked by `parse.include_prelude` (R-PRELUDE). `Emitter.emit()` is one method per phase (`_functions`, `_declare_class`, `_define_class`, `_conversions`, `_aliases`, `_includes`); `resolve_overload_collisions()` is a pure function on the IR (unit-tested).
- `parallel.py`: the worker side of the parallel mode below — a pool that parses and emits whole packages in separate processes. Its own module because macOS *spawns* workers: a spawned child re-imports the module holding the callable, and a function defined in `generator/__main__.py` is unreachable that way.
- `report.py`: categories for the report lines and the `report.txt` writer/reader (6.3).
- `model.py`: the IR; `ResultKind`, `StreamKind`, `ConversionKind` are `StrEnum`s. The 7c substitution state is one `Substitution` object in `parse.py` (`_SUBST`), set up and cleared by `_instantiate_template`.
- `symbols.py`: the exported-symbol list of a toolkit library for R-UNDEFINED (6) — `nm` on macOS and Linux, `dumpbin /EXPORTS` on Windows.
- `src/cpp/manifest.json`: classes bound by earlier runs, so a class whose base lives in a not-yet-generated package is skipped with a report line instead of aborting at import (`nb_type_new: base type not known`).
    - A class skipped that way — or because its own base was skipped just before — is removed from the manifest again, so neither a later package nor a later toolkit derives from a class that does not exist. In OCCT 8.0.1 six classes are skipped for their base, all over a `std::` stream base (`LDOM_SBuffer`, `Standard_ArrayStreamBuffer`, `OSD_StreamBuffer<std::istream>` …), and none for a base skipped just before; `tests/test_generator.py::test_emitter_ambiguous_constructor_and_skipped_base_chain` drives the whole cascade on a synthetic header.
    - Its nested classes and **nested enums** go with it (in the test, `Rules_Unbound::Status`): they leave the manifest and the `NCollection_Xxx[T]` accessor table, a typedef of them is reported instead of aliased (R-ALIAS), and an NCollection instantiation over them is skipped and reported (`NCollection_DynamicArray<Rules_Unbound::Status>`). Left in the manifest, the alias would abort the import of its toolkit (`no attribute` for the skipped class) and the accessor entry would break `NCollection_DynamicArray[T]` for every `T` (`Template._resolve` resolves all entries at once). Members whose signature still names such a type stay bound and uncallable (9, usability).

### Parallel generation (`NANOCCT_JOBS`)

The generator parses and emits every package in a process pool, **one worker per core by default**; `NANOCCT_JOBS=<n>` sets the count and **`NANOCCT_JOBS=1` is the sequential path**, which is what a byte-for-byte comparison is run against (the pools are then never entered). The worker count is capped at the number of packages, so a `--package` run does not pay for idle processes.

Measured on macOS (M5, 18 cores — 6 performance + 12 efficiency, 48 GB), 45 toolkits, 355 packages, **byte-identical output including `manifest.json` at every job count**:

| jobs | parse | emit | total |
|---|---|---|---|
| 1 | 104.5 s | 54.2 s | **161.8 s** |
| 4 | 59.9 s | 15.6 s | 77.7 s |
| 10 | 30.1 s | 8.5 s | 40.9 s |
| 14 | 25.3 s | 7.4 s | 34.9 s |
| **18** (default) | 20.7 s | 6.8 s | **29.9 s — 5.4×** |

More workers keep paying off past the six performance cores, so the default is the core count rather than a guess at the useful number. That the result is identical at 4, 10, 14 and 18 jobs is what says it does not depend on how the packages were distributed.

`parallel.jobs_from_env()` is the one place that decides the count, for these pools and for the stub subprocesses of 7b (**96.4 s → 13.7 s**). A clean regeneration plus stubs takes **43.6 s** (sequentially **258 s**).

A package normally inherits three things from the packages parsed or emitted before it. Each one is an explicit input; left implicit, each is hidden order-dependence, in the sequential generator too:

- **The parser's cross-package state** — `parse._DETECTED_NONCOPYABLE` and the `_derives_from` memo, whose value may have been computed in a translation unit where more was visible. `parse.collect_state()`/`carry_state()` make it an input/output the driver merges at a barrier, a cached `True` never overwritten by a `False`. Without it exactly one binding of ~65 000 differs (`BRepClass3d_SolidExplorer::Intersector`).
- **`known_elsewhere`** — which 7c instantiations an earlier package already bound. `_known_elsewhere_sets()` derives it from the previous round's IRs, replaying what the sequential loop does to `known`: the classes of every earlier toolkit (folded in at each toolkit boundary, a regenerated package's old entries deleted first) plus the classes of the earlier packages of its own toolkit. **Only instantiation spellings are kept**, in both paths: `parse_package` consults the set for nothing else — measured, **339 queries in a 45-toolkit run and every one a name containing `<`** — and those are also the only names R-UNDEFINED cannot remove under us, since it drops classes by plain name only.
- **Instantiation ownership** — who emits a 7a/7c instantiation, which the sequential loop decides *by* emitting (first package to need it claims it). `Emitter.assign_templates()` runs exactly the decisions and nothing else, and the driver runs it over every package in emit order against one shared registry before the pool starts; each package then knows whether it owns a key or aliases it (`Emitter.preassigned`). It is the same code the sequential path runs (`_claim_template()`, shared with the declare phase), not a second implementation. The claim loop must stay *outside* `plan()`: R-DEFAULT-UNBOUND reads the registry during the define phase, so claiming a package's keys up front would let a member see a class `emit()` has not declared yet.

The parse iterates to a fixpoint. **Round 1 runs with the manifest alone** — an empty set in a clean run — so every package instantiates everything it uses (550 instantiation classes against 391 in the steady state) and the owner of an instantiation is the first package in canonical order that has it, which is exactly the sequential rule. **Round 2 parses again with that derived answer and is the result.** The test is on the *inputs*: when the sets derived from a round's output are the sets that round was given, another round would repeat it. Two rounds suffice in practice; four without a fixpoint fails the run rather than writing a result nothing justifies.

Two checks, one free and one on demand:

- **Every parallel run** re-computes `known_elsewhere` the sequential way as the loop walks the packages and compares it with what the pool was given, naming the package and the differing entries and exiting 1 on a mismatch — the derivation simulated from IRs against the accumulation itself.
- **`tests/test_generator.py::test_a_parallel_run_reproduces_a_serial_one_byte_for_byte`**, six toolkits, **skipped unless `NANOCCT_AB=1`**: it has to run the generator serially to have something to compare against, which costs 43 s against the parallel run's 15 s — the whole speedup, spent to re-prove it. Run it after a change to the parse or the emit phase.

### `overrides.toml` — the only hand-maintained input

Each entry is a documented deviation with a one-line reason. Sections:

- `inout`: the four `gp_*::Transforms` methods whose `double&` parameters are in/out and the two `Geom_Transformation`/`Geom2d_Transformation::Transforms` that forward to them, `Bnd_Sphere::IsOut` (`theMaxDist` compared, then lowered), `ElCLib::AdjustPeriodic` (`U1`/`U2` moved into the period from their incoming values), `BVH_BuildQueue::Fetch` (`wasBusy` from the last call), `Hermit::Solutionbis` (some branches set only one of `Knotmin`/`Knotmax`), `*::InitFromJson` for every class, `Font_FontMgr::FindFont` (`Font_FontAspect&`: the aspect looked for, replaced when an alias maps to another style — `Font_FontMgr.cxx:1060`), and the methods that read and replace a `handle<T>&` — `GeomLib::ExtendCurveToPoint` and five more, `*::ReadCompleteInfo`. OCCT's `@param[in][out]` markers are too sparse to derive the list (`gp_Trsf::Transforms` has none; a survey of the bound headers: every marked non-const primitive/enum reference in the bound headers is either in the list, a protected member or an unbound function template).
- `skip.classes`: internal helpers such as `Standard_Static_Assert<true>`.
- `skip.noncopyable`: `math_GlobOptMin`, bound through a wrapper with deleted copy/move.
- `skip.headers`: platform-specific internals OCCT only includes under `#ifdef`, e.g. `OSD_WNT.hxx`.
- `skip.methods`: members of a 7c instantiation whose template *body* does not compile for the argument — `IntPolyh_Array<IntPolyh_Edge>::Dump` calls `Edge::Dump()` which takes an `int`. Declared-but-undefined members need no entry since the `nm` check compares mangled names per overload (R-UNDEFINED).
- `skip.namespaces`: `std` (only `std::hash` specialisations); `detail`/`Detail`/`Internal` (header-only implementation helpers).
- `instantiate.extra`: container instantiations to bind although no signature uses them (7a).
- `include.packages` / `include.headers`: allowlists for a partial toolkit/package (currently empty); names are validated against `PACKAGES.cmake`/`FILES.cmake`, the other headers are reported.
- `stream.binary_packages`: packages whose streams carry a binary format (R-STREAM-OUT, R-STREAM-IN).

### Principles

- Regular expressions are used only for CMake list files, for recognising `std::basic_ostream`-like canonical types, and for tokenising type spellings into identifiers to collect `#include`s — never to parse C++.
- Type spellings are emitted **as written in the header** (e.g. `Standard_Size`, `size_t`) so the generated C++ is portable; the *canonical* type is used only for analysis (out-param detection, unsupported types).
    - Exceptions: types nested in a class are spelled fully qualified (`gp_Dir::D`), because inside the class the header says just `D`; likewise non-template classes and enums declared in an OCCT namespace (`Geom2dEval_RepCurveDesc::Base`, written `Base` inside the namespace).

## 6.3 Output

- Per toolkit: `src/cpp/<TK>/<pkg>.cpp` (one per package, `nanocct_declare_<pkg>` + `nanocct_define_<pkg>`), `src/cpp/<TK>/_<TK>.cpp` (module init), `src/cpp/<TK>/report.txt`, `src/nanocct/<pkg>.py`, `src/cpp/toolkits.cmake` (the toolkit list in link order plus a `NANOCCT_<TK>_EXTRA_LIBS` line per toolkit that needs one, R-LINK; the lists are kept in `manifest.json` so a partial run does not drop another toolkit's).
- **Generated files are not tracked.** Only three files under `src/` are hand-written and in git: `src/cpp/common/nanocct_common.h`, `src/cpp/common/nanocct_ncollection.h` and `src/nanocct/py.typed`. Everything else — 400 `<pkg>.cpp`, 45 `report.txt`, `manifest.json`, `toolkits.cmake`, `common/ncollection_docs.h` and 742 `.py`/`.pyi` shims, 1 190 files — is regenerated.
    - **Why:** OCCT's headers are platform-dependent, so one generation platform cannot serve the others. `WNT_Window.hxx:34` sits inside `#if defined(_WIN32) && !defined(OCCT_UWP)` (lines 22-175), so a macOS generation produces **no `WNT_Window` at all** and a Windows user would have no native window class. The converse is *not* symmetric: `Cocoa_Window` (`:60`) is **not** guarded — the `#if defined(__APPLE__)` at `:19` closes at `:21` around an include — so it is declared everywhere and only *defined* on macOS. On Windows it therefore binds as five classes with **zero methods** (R-UNDEFINED finds none of them in `TKService.lib`), which is the other half of the same argument: each platform must generate for itself. The standard library diverges too. The code is ephemeral and builds in a few minutes; `report.txt` is a debug and verification tool for a build, and the `.so` files are its result.
    - **The cost**: `report.txt` has no git history, so a regeneration that loses a member is not visible as a `git diff` — it is a per-build artefact to read on the spot. The toolkit tests that assert on it work only after a generation: the contract is **fetch deps → generate → build → test**, which is what CI does on each platform anyway.
    - Users installing a wheel never need libclang; building from source does.
- **The report**: every run prints everything not bound and why and, for a full toolkit run, writes it to `report.txt`.
    - One line per omission: `category<TAB>package<TAB>what: why`; categories assigned from the message text by the table in `generator/report.py` (a message no pattern knows lands in `misc`, currently empty; tests assert that).
    - The file is the coverage instrument: a regeneration that loses a member shows up as a change in `report.txt` (compared against the previous build's copy, not against git), and `tests/test_TKBRep.py::test_unbindable_classes_are_reported_not_bound` reads it.
