# nanoOCP design

**nano**bind-based **O**pen **C**ascade for **P**ython

Living document. Every design decision goes here with its rationale and the evidence it rests on; when a decision changes, the entry is updated and the change is logged in the [decision log](#decision-log) at the end. Facts marked *unverified* have not been tested yet.

## 1. Goals

- Python bindings for Open CASCADE Technology (OCCT) 8.0.1, generated from the OCCT headers.
- **1:1 with the OCCT API**: same class, method, parameter and enum names, same package structure, OCCT's own `//!` comments as docstrings, so the OCCT reference documentation serves as the nanoOCP documentation. Deviations exist only where Python cannot express a C++ idiom; each one is a documented rule (section 6).
- **nanobind** as the binding library, in **stable-ABI mode** (`abi3`), so one wheel per platform covers all supported CPython versions.
- The generator must be **simple and efficient**: one Python program, libclang for parsing, plain string emission, generated C++ checked into the repository.
- Platforms for the generator and the wheels: macOS (Apple Silicon), Linux (x86_64 and aarch64), Windows.

## 2. Scope

Phase 1: `FoundationClasses`, `ModelingData`, `ModelingAlgorithms`. Phase 2: `ApplicationFramework` (only what `DataExchange` needs) and `DataExchange`. `Draw` is out. `Visualization` is out **except the font/text-to-BRep slice**: the `Font` package (TKService) and `StdPrs_BRepFont` / `StdPrs_BRepTextBuilder` (TKV3d) — `Font_BRepFont` and `Font_BRepTextBuilder` are typedefs of these (`Font_BRepFont.hxx:21`).

Visualization toolkits must be *compiled* regardless, because `TKXCAF`, `TKVCAF`, `TKRWMesh`, `TKBinXCAF`, `TKXmlXCAF` and the `TKDE*` toolkits link `TKV3d`/`TKService` (their `EXTERNLIB.cmake`). `TKOpenGl` is not linked by anything in scope and is excluded (`USE_OPENGL=OFF`).

Sizes (headers per module, `V8_0_1`): FoundationClasses 575, ModelingData 686, ModelingAlgorithms 1412, ApplicationFramework 420, DataExchange 1994.

## 3. Toolchain and third-party dependencies

### 3.1 OCCT

OCCT is built locally from the `V8_0_1` tag (sources extracted with `git archive` from a checkout into `deps/occt-src`, i.e. the exact tag, not a working tree). Script: `deps/build-occt.sh`; install prefix `deps/occt-8.0.1`. Configuration:

| Option | Value | Why |
|---|---|---|
| compiler | Apple clang (`/usr/bin/clang++`), system libc++ | Wheels must not depend on a conda/Homebrew C++ runtime. The previous `/opt/local/occt-8_0_1-novtk` install was built inside micromamba and links `@rpath/libc++.1.dylib` without an `LC_RPATH`, which makes extension modules fail to load. |
| `BUILD_CPP_STANDARD` | C++17 | OCCT default. |
| `CMAKE_BUILD_TYPE`, `BUILD_OPT_PROFILE` | Release, Production (`-O3 -flto`) | Same as the OCP build scripts. |
| `BUILD_RELEASE_DISABLE_EXCEPTIONS` | **OFF** | OCCT must throw `Standard_Failure` in release builds so Python sees exceptions. |
| `CMAKE_OSX_DEPLOYMENT_TARGET` | 11.1 | Wheel platform tag `macosx_11_0_arm64`, same as OCP. |
| `BUILD_MODULE_Draw`, `USE_VTK`, `USE_TBB`, `USE_TK`, `USE_XLIB`, `USE_OPENGL`, `USE_GLES2`, `USE_FFMPEG` | OFF | Not needed in scope. |
| `USE_FREETYPE` | ON, static build from `deps/build-freetype.sh` | Required by the font slice (`Font_FTFont.cxx` is entirely `#ifdef HAVE_FREETYPE`). |
| `USE_RAPIDJSON` | ON (header-only, currently from Homebrew) | glTF reader/writer (`TKDEGLTF`). To be vendored. |

**No conda/micromamba anywhere.** The user's OCP build scripts in `~/Development/CAD/ocp-build-system/local-build/` are a reference for the CMake options only.

### 3.2 Third-party policy: no vcpkg (for now)

The compiled third-party surface for the whole scope is one library, FreeType. FreeType 2.14.3 (sha256 verified against the Homebrew formula) builds in 2 s with its own CMake and `FT_DISABLE_ZLIB/BZIP2/PNG/HARFBUZZ/BROTLI=TRUE` into a static archive that links against nothing but libSystem (verified with a link test loading Helvetica). It is linked into `libTKService` (149 exported `FT_*` symbols; `otool -L libTKService.dylib` shows only libSystem/libobjc/libc++). vcpkg would replace that one step with a bootstrap and a triplet per platform, and builds FreeType with the optional dependencies enabled by default. Revisit if the list grows (Draco, TBB, FreeImage); OCCT 8.0.1 has native `BUILD_USE_VCPKG` support.

Linux additionally needs **fontconfig** (used unconditionally under `HAVE_FREETYPE` in `Font_FontMgr.cxx:86,708`): system package in the manylinux image, bundled by auditwheel. Accepted by the user. Windows enumerates fonts via the registry (*unverified*).

### 3.3 Python side

Python ≥ 3.12, `uv` project, nanobind ≥ 3.1.0 (the `handle<T>` caster uses `nb::keep_alive_cb`, public since 3.1.0), scikit-build-core, pip `libclang` (fallback parser, see 5.2), pytest.

## 4. Runtime model

### 4.1 Stable ABI

`nanobind_add_module(... STABLE_ABI NB_DOMAIN nanoocp ...)` in linked mode: `Py_LIMITED_API=0x030C0000`, module file `*.abi3.so`, floor Python 3.12. nanobind's split mode (backend module, floor 3.10) was rejected: it adds a runtime dependency on `nanobind-backend` for two extra Python versions.

**Gotcha (verified):** nanobind silently drops `STABLE_ABI` unless `find_package(Python ... Development.SABIModule)` is requested; the first PoC produced `cpython-314-darwin.so` because of this.

### 4.2 Three kinds of C++ types

1. **Value types** (`gp_*`, `TopoDS_Shape`, `Bnd_Box`, …): plain `nb::class_<T>` with `nb::init<...>`; references returned by OCCT are copied (nanobind's default policy for lvalue references).
2. **`Standard_Transient` descendants**: `nb::class_<T, Base>` plus a type caster for `opencascade::handle<T>` (alias `occ::handle<T>`, `Standard_Handle.hxx:419`) in `src/cpp/common/nanoocp_common.h`, modeled on nanobind's `shared_ptr` caster. The Python instance never owns the C++ object; a heap-allocated `handle<Standard_Transient>` is attached with `nb::keep_alive_cb`, so OCCT's intrusive reference count governs lifetime on both sides. Constructors are `nb::new_` lambdas returning `handle<T>` so that Python-created objects go through the same path. Verified in `poc/test_poc.py`: refcount 1 after construction, 2 after C++ stores the handle, object survives Python GC, comes back as its most-derived type, `load() is back` (nanobind instance map), `None` ↔ null handle.
3. **`Standard_Failure` descendants**: Python exception classes created with `PyErr_NewExceptionWithDoc` (stable ABI), mirroring the C++ hierarchy (`Standard_OutOfRange → Standard_RangeError → Standard_DomainError → Standard_Failure → RuntimeError`). `Standard_Failure` itself derives from `std::exception` in OCCT 8 and provides `what()`. Translation C++ → Python does **not** use `nb::exception<T>` (catch by derived type): the `DEFINE_STANDARD_EXCEPTION` classes are header-only, so their `typeinfo` is duplicated per shared object and a `catch (Derived&)` in the extension module does not match an object thrown inside `libTKMath` (verified: `Standard_ConstructionError` arrived as `Standard_Failure`). Instead every toolkit module registers one translator that catches `Standard_Failure&` and dispatches on `typeid(e).name()` through a per-module map; unknown names are rethrown to the next module's translator (nanobind tries the newest first) and the TKernel translator falls back to `Standard_Failure`. Exceptions can also be raised from Python and caught by their bases.

A `handle<T>` *parameter* must be declared `nb::arg("x").none()` or nanobind rejects `None` before the caster runs (verified).

**Returned pointers and references.** nanobind's default for a returned raw pointer is *take ownership*, which would `delete` an OCCT object that is still reference-counted (`Standard_Transient::This()` returns `Standard_Transient*`). Rules: a pointer or reference to a `Standard_Transient` descendant is wrapped into a `handle<T>` in a lambda (`t.This() is t` holds); a pointer to any other class gets `rv_policy::reference`; a *mutable* reference to a class (`ChangeXxx()` accessors) gets `rv_policy::reference_internal` so in-place edits reach the owner; const references and values are copied (nanobind default).

**Construction.** nanobind constructs value types with placement new, which needs either no class-level `operator new` or a public `operator new(size_t, void*)` (`DEFINE_STANDARD_ALLOC` provides one; `DEFINE_NCOLLECTION_ALLOC` does not). Classes failing this, classes with a non-public base (`Message_LazyProgressScope : protected Message_ProgressScope`, whose inherited `operator new` is inaccessible even to C++) and abstract classes get no constructors; the report says so. A class with only non-public constructors gets no implicit default constructor either (`Standard_Type`). Among `nb::new_` overloads the zero-argument one must be registered first (nanobind requirement) — constructors are sorted by required-parameter count.

## 5. Package layout and generator

### 5.1 Modules and names

- One extension module per OCCT **toolkit**: `nanoocp._TKMath`, `nanoocp._TKernel`, … (mirrors OCCT's link graph; parallel compilation; all share `NB_DOMAIN nanoocp` so types cross module boundaries). Each toolkit module first imports the toolkit modules it links against (from `EXTERNLIB.cmake`), so base classes and parameter types are registered before use.
- One Python module per OCCT **package**: `nanoocp.gp.gp_Pnt`, `nanoocp.Geom.Geom_CartesianPoint`. Implementation: the toolkit module creates a submodule per package, sets its `__name__` to `nanoocp.<pkg>` (so `gp_Pnt.__module__ == "nanoocp.gp"`), registers it in `sys.modules["nanoocp._<TK>.<pkg>"]`, and a generated shim `src/nanoocp/<pkg>.py` does `from nanoocp._<TK>.<pkg> import *`.
- Registration happens in two phases per toolkit: **declare** all classes and enums of all packages, then **define** members. Reason: nanobind converts default-argument values to Python objects at `.def` time, so every type used in a default must already exist. Packages are declared in base-class dependency order (`FSD_BinaryFile : Storage_BaseDriver` needs `Storage` before `FSD`; computed from the IR, cycles would be reported), classes within a package likewise.
- Cross-package lookups at registration time (exception bases) go through the extension submodule `nanoocp._<TK>.<pkg>`, never through the `nanoocp.<pkg>` shim: importing the shim while the toolkit module is still initialising freezes a half-filled namespace (observed: `nanoocp.Standard` with 42 of 120 names).

### 5.2 Generator architecture

`generator/` is a Python package, run as `python -m generator --toolkit TKMath [--package gp]`:

- `occt.py`: reads OCCT's own `TOOLKITS.cmake`, `PACKAGES.cmake`, `FILES.cmake`, `EXTERNLIB.cmake` for the module → toolkit → package → header tree and toolkit dependencies. No hand-maintained lists.
- `parse.py`: **libclang AST** (`clang.cindex`), one translation unit per package (an umbrella header including all package headers), `PARSE_SKIP_FUNCTION_BODIES`. Builds the IR in `model.py`. It uses the **system libclang that pairs with the `clang` on `PATH`** (located from `clang -print-resource-dir`) and falls back to the pip `libclang` wheel. Reason: the pip wheel is stuck at clang 18 and cannot parse the libc++ of the current Apple SDK (`__builtin_clzg`); the pip wheel also ships no builtin headers, so `-resource-dir` must be passed explicitly. Cross-platform behaviour of this selection is *unverified* (macOS only so far).
- `emit.py`: IR → C++ with plain f-strings. No template engine.
- `overrides.toml`: the only hand-maintained input; each entry is a documented deviation. Sections: `inout` (the four `Transforms` methods whose `double&` parameters are in/out), `skip.classes` (internal helpers such as `Standard_Static_Assert<true>`), `skip.headers` (platform-specific internals OCCT only includes under `#ifdef`, e.g. `OSD_WNT.hxx`), `skip.methods` (declared in a header but never defined in the libraries — `OSD_Path::LocateExecFile`, one `TCollection_AsciiString::IsEqual` overload — found as link errors; an `nm`-based checker could automate this).
- `src/cpp/manifest.json`: classes bound by earlier runs, so a class whose base lives in a not-yet-generated package is skipped with a report line instead of aborting at import (`nb_type_new: base type not known`).

Regular expressions are used only for CMake list files, for recognising `std::basic_ostream`-like canonical types, and for tokenising type spellings into identifiers to collect `#include`s — never to parse C++.

Type spellings are emitted **as written in the header** (e.g. `Standard_Size`, `size_t`) so the generated C++ is portable; the *canonical* type is used only for analysis (out-param detection, unsupported types). Exception: types nested in a class are spelled fully qualified (`gp_Dir::D`), because inside the class the header says just `D`.

### 5.3 Output

Per toolkit `src/cpp/<TK>/<pkg>.cpp` (one per package, `nanoocp_declare_<pkg>` + `nanoocp_define_<pkg>`), `src/cpp/<TK>/_<TK>.cpp` (module init), `src/nanoocp/<pkg>.py`, `src/cpp/toolkits.cmake`. Generated files are checked in; users never need libclang. Every run prints a **report of everything not bound and why**.

## 6. Binding rules (1:1 and the documented deviations)

| C++ idiom | Python | Rule |
|---|---|---|
| method, constructor, static method, public field, enum | same name | 1:1; overloads are chained `.def`s, resolved by nanobind |
| `//!` comments | docstrings | class and member docs come from `raw_comment` |
| non-const reference to a primitive (`double&`, `int&`, enum) as parameter | dropped from the signature, **returned** (bare value if it is the only result, else a tuple; a non-void return comes first) | pure-out is the common case (`gp_Pnt::Coord`) |
| same, but the method reads the value too (`gp_Trsf::Transforms`) | parameter kept **and** returned | listed in `overrides.toml [inout]`; not derivable from syntax |
| non-const reference to a class (`gp_XYZ&`) | passed and **mutated in place** | nanobind by-reference semantics |
| `operator+ - * / % ^ & \| == != < <= > >= () []`, unary `- + !` | `__add__` … `__call__`, `__neg__` … | member operators; `nb::is_operator()` |
| `void operator+=` etc. | `__iadd__` … returning `self` (same object) | OCCT in-place operators return `void` |
| free `operator*(double, gp_Vec)` | `__rmul__` on `gp_Vec` (reflected when the class is the 2nd operand, normal when it is the 1st) | |
| static and instance method with the same name | static gets suffix `_s` (`gp_QuaternionNLerp.Interpolate_s`) | Python cannot overload across static/instance; same choice as OCP |
| explicit template specialisation without an OCCT typedef (`NCollection_Lerp<gp_Trsf>`) | `NCollection_Lerp_gp_Trsf` | `<`, `,` → `_`, `>` dropped |
| unscoped enum | `nb::enum_` with `is_arithmetic` (`int(e)` works) | matches C++ implicit conversion |
| nested `enum class` | attribute of the class (`gp_Dir.D.Z`) | |
| `handle<T>` return | most-derived registered type; null → `None` | caster |
| `T*` / `T&` return, T Transient | wrapped in `handle<T>` (same Python object as before) | never let nanobind own a Transient |
| `T*` return, other class | `rv_policy::reference` | |
| `T&` (mutable) return, other class | `rv_policy::reference_internal` | in-place edits via `ChangeXxx()` |
| non-`explicit` converting constructor `T(const A&)` | `nb::implicitly_convertible<A, T>` — `OSD_Path("/x")` works because `TCollection_AsciiString(const char*)` is implicit | C++ implicit conversion semantics, 1:1 |
| default argument | cast to `std::decay_t<ParamType>` (a `char` default written as `0` becomes a 1-char `str`); unqualified static members/enumerators of the class are qualified (`NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE`) | the expression is emitted outside the class scope |
| `char` parameter | 1-character `str` | nanobind convention |
| `const char*` (`Standard_CString`) | `str`, UTF-8 | **limitation:** `TCollection_AsciiString` holds 8-bit (Latin-1-like) text; `ToCString()` on such content raises `UnicodeDecodeError` in Python (OCCT treats U+0080..U+00FF as representable). Use the `?`-replacement overload or the `ExtendedString` UTF-8 paths. |
| `std::vector/map/set/pair/optional/shared_ptr/function/string_view` of supported types | native Python objects via nanobind's STL casters | `std::shared_ptr<std::istream>`, `std::vector<NestedStruct>` are skipped (reported) |
| deprecated (`Standard_DEPRECATED`), deleted, move constructors | skipped | reported |
| `std::ostream&`/`std::istream&` (`DumpJson`, `InitFromJson`), raw pointers to primitives, references to pointers (`char*&`), pointers to incomplete types (`_xlocale*`), `double&` *returns* (`ChangeValue`), C-array fields, template members, nested classes, non-public bases | skipped | reported; to be revisited per case (e.g. `DumpJson` → `str`) |

### 6a. NCollection containers (hand-written binders)

**Facts.** OCCT 8.0.1 spells containers directly in its API (`Geom_BSplineCurve(const NCollection_Array1<gp_Pnt>& Poles, …)`; 2050 distinct `NCollection_*<…>` spellings in the installed headers), and the pre-8.0 typedef names (`TColgp_Array1OfPnt`, `TopTools_ListOfShape`, 972 headers) live in `src/Deprecated/NCollectionAliases`, outside every toolkit, each marked deprecated with "use `NCollection_Array1<gp_Pnt>` directly". The reference documentation for the container API is therefore the template class page. `NCollection_HArray1<T>` derives from both `NCollection_Array1<T>` and `Standard_Transient`; `NCollection_Array1` has a virtual destructor (polymorphic).

**Decision (2026-09-20, option b).** One hand-written C++ binder per template kind in `src/cpp/common/nanoocp_ncollection.h` (`nanoocp::bind_NCollection_Array1<T>(module, name)`, `bind_NCollection_HArray1<T>`), instantiated by the generator. The alternative — instantiating template members generically via libclang with argument substitution — was rejected: dependent types, `enable_if` overloads and members that do not compile for every element type would each need a special rule, for the same user-visible result.

- **Which instantiations:** every `NCollection_X<…>` (also inside `handle<…>`, also nested) that appears in a bound signature, collected while parsing; nested arguments and `requires` (`Array1<T>` before `HArray1<T>`) are bound first. Over-approximation (unused instantiations) only costs compile time.
- **Primary spelling `NCollection_Array1[T]`** (revised 2026-09-20, replaces "home = element package"): `nanoocp.NCollection.NCollection_Array1[gp.gp_Pnt](1, 4)` mirrors the docs' `NCollection_Array1<gp_Pnt>`. `NCollection_Array1` is a generated `Template` object (`nanoocp/_templates.py`, table in the `NCollection` shim from `manifest.json`) mapping Python element types to the bound classes: `float → double`, `int → int`, `bool → bool`, `str → std::string`, an OCCT class for itself **and** for `handle<class>`, a bound instantiation for a nested container; other C++ scalars (`float`, `size_t`, `char`…) are reachable only by the concrete name. Unbound element types raise `TypeError` listing what is bound; calling the template itself raises `TypeError` with a hint.
- **Concrete classes:** one per C++ instantiation, named `template__arg1__arg2` (double underscore separates arguments — OCCT names never contain `__`; `handle<X>` → `Handle_X`; nested left to right; defaulted template arguments such as hashers are omitted): `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`. They are what `type()`, `repr` and stubs show. All of them live in **`nanoocp.NCollection`** (the doc page's package), bound by the first toolkit that needs them (`manifest.json` records `by`, the binding package, so regeneration is idempotent — verified by running the generator twice). Because a later toolkit adds to `NCollection`, `import nanoocp` imports **all toolkit modules eagerly** in dependency order and shims have a module `__getattr__` fallback.
- **Deprecated typedef names:** parsed from `NCollectionAliases` (one libclang TU, ~1 s) and exposed as lazy aliases: `nanoocp.TColStd.TColStd_Array1OfReal is nanoocp.Standard.NCollection_Array1_double`; prefixes that are not packages in 8.0 (`TColgp`) become alias-only modules. So both 7.x-era docs/OCP code and 8.0 docs resolve.
- **1:1 methods** with OCCT names and signatures; **docstrings extracted from the template header** by the generator into `ncollection_docs.h` (first overload wins); a **coverage check** reports template members that are neither bound nor listed as knowingly skipped (`Move`, `operator=`, `EmplaceValue`, iterators, allocation operators).
- **Python additions** (never replacements, marked "Python addition" in their docstrings): `__len__` (= `Length`), `__iter__` (values `Lower()..Upper()`), `__setitem__` (= `SetValue`). `__call__` and `__getitem__` are OCCT's own `operator()`/`operator[]` = `Value` with the **OCCT index**, not 0-based. `Change*` accessors are bound only for class element types (`double&` cannot be exposed).
- **HArray1 and single inheritance:** nanobind supports one base. `HArray1<T>` is bound with base `Standard_Transient` (handle semantics, `IsKind`, up-cast to `Standard_Transient` parameters) and the full `Array1` API bound on it again; `nb::implicitly_convertible<HArray1<T>, Array1<T>>` plus an `Array1(const HArray1&)` constructor overload let an `HArray1` be passed where C++ takes `const NCollection_Array1<T>&` (as a copy). Consequences: `isinstance(h, NCollection_Array1_X)` is `False`; `h.Array1()` returns a sliced copy of static type `Array1` (returning `const A&` would make nanobind copy the dynamic type); `h.ChangeArray1() is h`.
- **Lesson recorded:** nanobind copy-constructs the *dynamic* type for polymorphic by-value/const-reference returns whenever that type is registered. For Transient classes this yields an owned private copy, which is harmless but can surprise; relevant wherever OCCT returns a polymorphic value class by const reference.

- **List / Sequence / HSequence** (2026-09-20): nested `Iterator` classes bound as `NCollection_List__int.Iterator` (1:1 with `NCollection_List<T>::Iterator`; `TopTools_ListIteratorOfListOfShape`-style aliases resolve to them), with `nb::keep_alive` on the container. `size_t` overloads that duplicate `int` ones are not bound (Python cannot distinguish them); `At`/`ChangeAt` (size_t only) are. `Contains`/`Remove(item)`/`__contains__` are bound only when `T` has `operator==` (compile-time trait; `gp_Pnt` has none, `TopoDS_Shape` has). Members returning the inserted element (`Append` → `T&`) return a view for class types and a value for scalars. Members inherited from the non-template bases (`NCollection_BaseList::Extent`, …) are covered by the docs/coverage extractor via `bases`. Python additions: `__len__`, `__iter__`, `__contains__`, and for Sequence `__getitem__`/`__setitem__` (1-based like `Value`). Generic stubs for the three kinds; verified with mypy and ty. Divergence: ty rejects `NCollection_List[int].Iterator` (nested class through a specialised generic), mypy accepts it — typed code uses the concrete `NCollection_List__int.Iterator`.
- **Ordering lesson:** instantiations are registered in the toolkit's *declaration* order, so packages are also *emitted* in that order; otherwise an `HSequence<T>` bound by an early-running package could precede the `Sequence<T>` its implicit conversion needs (observed as `implicitly_convertible: destination type unknown`).

- **Map / DataMap / IndexedMap / IndexedDataMap** (2026-09-20): the hasher template argument is dropped from key and name only when it equals its default `NCollection_DefaultHasher<Key>` (`defaults` per kind in `BINDERS`, applied by `instance_args`); a custom hasher stays part of both, so it cannot be merged with the default instantiation (a different C++ type). Shared base members (`NCollection_BaseMap`: `NbBuckets`, `Extent`, …) in one helper. `Seek`/`ChangeSeek` return `None` for absent keys (a view for class items, a value for scalars); `Find(key, item&)`/`FindFromKey(key, item&)` only for class items (in-place). Skipped: `Contained` (`std::optional<std::reference_wrapper<…>>`), `Emplace*`, `Items()`/`IndexedItems()` views, `GetHasher`. Python additions: `__len__`, `__contains__`, `__iter__` over keys (index order for the indexed kinds), `__getitem__`/`__setitem__`/`__delitem__` on DataMap (`Find`/`Bind`/`UnBind`, `KeyError` when unbound), `__getitem__(index)` on the indexed kinds, `items()` → list of `(key, value)`. The indexed maps' iterators do not derive from `NCollection_BaseMap::Iterator` (no `Initialize`/`Reset`), the others do. Enums count as element types (`NCollection_IndexedMap[Message_MetricType]`).
- **`[instantiate]` override:** instantiations to bind although no bound OCCT signature uses them (`NCollection_Map<int>`, `NCollection_DataMap<int, double>`, …), registered by the `NCollection` package. Used to exercise binders that the current scope does not reach yet, and available for user conveniences.

Remaining kinds to bind the same way: `Shared` (36 typedefs), `DynamicArray` (34), `Array2` (32), `HArray2` (28), `DoubleMap` (12).

### 6b. Type stubs

`python -m generator.stubs` (after the build; it imports the extension) runs nanobind's `stubgen` per package module into `src/nanoocp/<pkg>.pyi` (cross-references come out as `nanoocp.Standard.X` because of the `__module__` rule) and adds: the deprecated typedef aliases as assignments; in `NCollection.pyi` a hand-written **`Generic[_T]` class per container kind** (`generator/stubs/<kind>.pyi`, kept in step with the binder) and every instantiation as `class NCollection_Array1__double(NCollection_Array1[float]): ...`. Verified with **mypy** and **ty** (`tests/test_typing.py` runs both on `tests/typing/check_ncollection.py`): `a[2]` is `float`, `h.Value(1)` is `Standard_Persistent`, `def f(arr: NCollection_Array1[float])` accepts every double array, and the five deliberate errors (wrong element type, wrong overload, `HArray1[X]` passed as `Array1[float]`) are reported by both checkers. Known imprecision: the checker types `NCollection_Array1[float](…)` as the generic, so assigning it to the concrete subclass is rejected (the reverse is fine); null handles are typed as the class, not `X | None` (same as nanobind's own handle stubs).

## 7. Build and packaging

- `CMakeLists.txt` at the root: `find_package(OpenCASCADE)` from `NANOOCP_OCCT_DIR` (default `deps/occt-8.0.1`), one `nanobind_add_module` per toolkit from `src/cpp/toolkits.cmake`, `INSTALL_RPATH` pointing at the OCCT lib dir for development builds.
- `pyproject.toml`: scikit-build-core, `wheel.py-api = "cp312"`, `build-dir = "build/{wheel_tag}"` (incremental rebuilds), `wheel.packages = ["src/nanoocp"]`. Development loop: regenerate → `uv sync --reinstall-package nanoocp` → `pytest`.
- Wheels: bundling OCCT dylibs (delocate/auditwheel/delvewheel) is not done yet.
- Tests: `tests/test_<pkg>.py` per package, each generator rule exercised at least once.

## 8. Open questions and next steps

1. Remaining NCollection binder kinds (section 6a), then the rest of `TKMath` and `ModelingData`.
3. Stubs for the remaining container kinds as their binders arrive; stubs for OCCT out-param tuples are already produced by stubgen.
4. Generator on Linux and Windows (libclang selection, MSVC/libstdc++ header discovery, platform-dependent `#ifdef`s in OCCT headers such as `OSD_*`).
5. Vendor RapidJSON; decide whether to vendor the ~23 clang builtin headers so the pip `libclang` fallback works without a host clang.
6. Wheel bundling and CI matrix.
7. Repository initialisation (`git init`) — pending the user's go.
8. Python-side subclassing of OCCT classes (nanobind trampolines) — not planned for now.

## Decision log

- **2026-09-20** — nanobind stable ABI (linked mode, 3.12+) chosen over split mode; PoC verified against OCCT (`poc/`).
- **2026-09-20** — `handle<T>` caster with intrusive refcount + `keep_alive_cb`, constructors via `nb::new_` (verified lifetime semantics).
- **2026-09-20** — One extension per toolkit, Python namespace per package (`nanoocp.gp.gp_Pnt`), out-params → tuples (user decisions).
- **2026-09-20** — Local OCCT build from `V8_0_1` with Apple clang, no conda; exceptions enabled; OpenGL/X11/Tk/TBB/VTK/Draw off.
- **2026-09-20** — Fonts are in scope (user needs text-to-BRep) → FreeType required; built statically from source; fontconfig on Linux accepted.
- **2026-09-20** — vcpkg declined for now (single compiled dependency); revisit if the list grows.
- **2026-09-20** — Generator: libclang AST, system libclang preferred over the pip wheel; type spellings as written; two-phase declare/define; manifest for cross-run base checks; `_s` suffix for mixed static/instance names; `overrides.toml` for in/out parameters. First package `gp` generated and tested (13 tests).
- **2026-09-20** — TKernel generated (18 packages, 44 tests). New rules: Transient pointer/reference returns wrapped in handles, `reference`/`reference_internal` policies, constructibility from `operator new` accessibility, exception translation by dynamic type name across DSOs (replaces `nb::exception`), implicit conversions from non-explicit constructors, defaults cast to the parameter type and qualified, package declaration order by base dependencies, `skip.headers`/`skip.methods` overrides, STL casters.
- **2026-09-20** — NCollection containers: option (b) hand-written binders; `Array1`/`HArray1` done (53 tests). Instantiations from signature scanning, home = element package, eager toolkit import, deprecated typedef aliases, docstrings extracted from the template header, coverage check.
- **2026-09-20** — `NCollection_Xxx[T]` accessor as primary spelling; concrete names with `__` separators; all instantiations homed in `nanoocp.NCollection`; type stubs (stubgen + generic container classes) verified with mypy and ty. mypy and ty added as dev dependencies (user request).
- **2026-09-20** — NCollection `List`, `Sequence`, `HSequence` binders with nested iterators (62 tests); packages emitted in declaration order.
- **2026-09-20** — NCollection hashed kinds (`Map`, `DataMap`, `IndexedMap`, `IndexedDataMap`) with default-hasher stripping, `[instantiate]` override, enums as element types (68 tests).
