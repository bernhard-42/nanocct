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

**Multiple inheritance (verified 2026-09-20).** nanobind supports one base and reuses the derived pointer as the base pointer without adjustment: a bound base must be at **offset 0** of the derived object. Measured: `NCollection_HArray1<T>` (`: Array1<T>, Standard_Transient`) bound with base `Standard_Transient` returned `myLowerBound` from `GetRefCount()` (5 for an array starting at 5), and `NCollection_Shared<T>` (`: Standard_Transient, T`) bound with base `T` crashed on the first `T` method. Rule for a class `S` with several bases: nanobind's base is the offset-0 one (`mi_traits<S>::base` in `nanoocp_common.h`, declared for the NCollection H-types and `Shared` via forward declarations so every TU agrees); members of the other base are bound with lambdas taking `base&` and `static_cast`ing to `S&` (an adjusting downcast); an **MI registry** (`nanoocp_register_mi<S>`) gives the `handle<T>` caster two conversions: Python `S` → `handle<Standard_Transient>` (`to_transient` on the stored pointer, then `dynamic_cast<T*>`, so a wrong target type fails cleanly) and `handle<Standard_Transient>` holding an `S` → the stored pointer (`dynamic_cast<void*>` to the complete object, then to the base). Verified: `HArray1(5, 9).GetRefCount() == 1`; a `Sequence<handle<Standard_Transient>>` round-trips an `HArray1` and a `Shared<Map<int>>` by identity with exact reference counts; `isinstance(h, NCollection_Array1[T])` is `True`, `isinstance(h, Standard_Transient)` is `False` (documented). Generated OCCT classes with several bases are not handled yet (open item).

**Construction.** nanobind constructs value types with placement new, which needs either no class-level `operator new` or a public `operator new(size_t, void*)` (`DEFINE_STANDARD_ALLOC` provides one; `DEFINE_NCOLLECTION_ALLOC` does not). Classes failing this, classes with a non-public base (`Message_LazyProgressScope : protected Message_ProgressScope`, whose inherited `operator new` is inaccessible even to C++) and abstract classes get no constructors; the report says so. A class with only non-public constructors gets no implicit default constructor either (`Standard_Type`). Among `nb::new_` overloads the zero-argument one must be registered first (nanobind requirement) — constructors are sorted by required-parameter count.

## 5. Package layout and generator

### 5.1 Modules and names

- One extension module per OCCT **toolkit**: `nanoocp._TKMath`, `nanoocp._TKernel`, … (mirrors OCCT's link graph; parallel compilation; all share `NB_DOMAIN nanoocp` so types cross module boundaries). Each toolkit module first imports the toolkit modules it links against (from `EXTERNLIB.cmake`), so base classes and parameter types are registered before use.
- One Python module per OCCT **package**: `nanoocp.gp.gp_Pnt`, `nanoocp.Geom.Geom_CartesianPoint`. Implementation: the toolkit module creates a submodule per package, sets its `__name__` to `nanoocp.<pkg>` (so `gp_Pnt.__module__ == "nanoocp.gp"`), registers it in `sys.modules["nanoocp._<TK>.<pkg>"]`, and a generated shim `src/nanoocp/<pkg>.py` does `from nanoocp._<TK>.<pkg> import *`.
- **C++ namespaces** (OCCT 8 uses them in the math packages and in ModelingData: `MathUtils`, `Geom2dGridEval`, `TopoDS`, `Geom2dEval_RepCurveDesc`, `BRepGraphInc`): a namespace named like its package **is** the package module (`MathUtils::DepressCubic` → `nanoocp.MathUtils.DepressCubic`, `Geom2dGridEval::CurveD1` → `nanoocp.Geom2dGridEval.CurveD1`, `TopoDS::Vertex` → `nanoocp.TopoDS.Vertex`); every other namespace becomes a **submodule** (`Geom2dEval_RepCurveDesc::Base` → `nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc.Base`, nested namespaces nest). Implementation: `def_submodule` in the declare phase, registered in `sys.modules["nanoocp._<TK>.<pkg>.<ns>"]`; the shim of such a package is a Python package `src/nanoocp/<pkg>/__init__.py` with one module per namespace (`<pkg>/<ns>.py`), so `from nanoocp.Geom2dEval.Geom2dEval_RepCurveDesc import Base` works and the stubs follow the same layout (`<pkg>/__init__.pyi`, `<pkg>/<ns>.pyi`). nanobind also registers a submodule under `<parent __name__>.<ns>` = `nanoocp.<pkg>.<ns>`; that key is popped again, otherwise `import nanoocp.<pkg>.<ns>` would find the extension object without importing the package shim (observed as `cannot import name 'Geom2dEval' from 'nanoocp'`). Namespaces in `overrides.toml [skip] namespaces` (`std`, `detail`, `Detail`, `Internal`) are not bound; anonymous namespaces are reported.
- **Nested classes** (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`, `Geom2dAdaptor_Curve::BezierData`) are bound into their outer class (`nanoocp.Geom2d.Geom2d_Curve.ResD1`, `__qualname__ == "Geom2d_Curve.ResD1"`), after it, and skipped when the outer class is; the manifest keys are the C++ names (`Geom2d_Curve::ResD1`), and `parse.py_path(name, package)` gives the Python attribute path used by the `NCollection_Xxx[T]` accessor tables, the stubs and cross-package lookups.
- Registration happens in two phases per toolkit: **declare** all classes and enums of all packages, then **define** members. Reason: nanobind converts default-argument values to Python objects at `.def` time, so every type used in a default must already exist. Packages are declared in base-class dependency order (`FSD_BinaryFile : Storage_BaseDriver` needs `Storage` before `FSD`; computed from the IR, cycles would be reported), classes within a package likewise.
- Cross-package lookups at registration time (exception bases) go through the extension submodule `nanoocp._<TK>.<pkg>`, never through the `nanoocp.<pkg>` shim: importing the shim while the toolkit module is still initialising freezes a half-filled namespace (observed: `nanoocp.Standard` with 42 of 120 names).

### 5.2 Generator architecture

`generator/` is a Python package, run as `python -m generator --toolkit TKMath [--package gp]`:

- `occt.py`: reads OCCT's own `TOOLKITS.cmake`, `PACKAGES.cmake`, `FILES.cmake`, `EXTERNLIB.cmake` for the module → toolkit → package → header tree and toolkit dependencies. No hand-maintained lists.
- `parse.py`: **libclang AST** (`clang.cindex`), one translation unit per package (an umbrella header including all package headers), `PARSE_SKIP_FUNCTION_BODIES`. Builds the IR in `model.py`. It uses the **system libclang that pairs with the `clang` on `PATH`** (located from `clang -print-resource-dir`) and falls back to the pip `libclang` wheel. Reason: the pip wheel is stuck at clang 18 and cannot parse the libc++ of the current Apple SDK (`__builtin_clzg`); the pip wheel also ships no builtin headers, so `-resource-dir` must be passed explicitly. Cross-platform behaviour of this selection is *unverified* (macOS only so far).
- `emit.py`: IR → C++ with plain f-strings. No template engine.
- `overrides.toml`: the only hand-maintained input; each entry is a documented deviation. Sections: `inout` (the four `Transforms` methods whose `double&` parameters are in/out), `skip.classes` (internal helpers such as `Standard_Static_Assert<true>`), `skip.headers` (platform-specific internals OCCT only includes under `#ifdef`, e.g. `OSD_WNT.hxx`), `skip.methods` (declared in a header but never defined in the libraries — `OSD_Path::LocateExecFile`, one `TCollection_AsciiString::IsEqual` overload — found as link errors; an `nm`-based checker could automate this), `skip.namespaces` (`std`: only `std::hash` specialisations; `detail`/`Detail`/`Internal`: header-only implementation helpers), `instantiate.extra`.
- `src/cpp/manifest.json`: classes bound by earlier runs, so a class whose base lives in a not-yet-generated package is skipped with a report line instead of aborting at import (`nb_type_new: base type not known`).

Regular expressions are used only for CMake list files, for recognising `std::basic_ostream`-like canonical types, and for tokenising type spellings into identifiers to collect `#include`s — never to parse C++.

Type spellings are emitted **as written in the header** (e.g. `Standard_Size`, `size_t`) so the generated C++ is portable; the *canonical* type is used only for analysis (out-param detection, unsupported types). Exceptions: types nested in a class are spelled fully qualified (`gp_Dir::D`), because inside the class the header says just `D`; likewise non-template classes and enums declared in an OCCT namespace (`Geom2dEval_RepCurveDesc::Base`, written `Base` inside the namespace).

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
| anonymous enum (`enum { BVH_Constants_MaxTreeDepth = 32 };`) | integer attributes on the module/class | C++ integer constants |
| `constexpr` constants, functions, classes, enums in a namespace (`MathUtils::THE_NEWTON_MAX_ITER`, `MathLin::LeastSquares`, `Geom2dGridEval::CurveD1`, `Geom2dEval_RepCurveDesc::Base`) | attributes of the package module when the namespace is named like the package, else of the submodule `nanoocp.<pkg>.<ns>` (5.1) | OCCT 8 uses namespaces as packages-within-packages |
| function/class templates in a namespace (`MathSys::Newton<FuncSetType>`), type aliases in a namespace | not bound, reported | need a concrete functor type; the classic `math_*` classes are the Python-facing API |
| free function with `double&`/`int&` out-parameters (`MathUtils::DepressCubic`) | out-params returned as a tuple, like methods | |
| public nested class/struct (`Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`) | attribute of the outer class, fields/methods 1:1 | OCCT 8 result structs (`EvalD1() -> ResD1`), also inside `std::optional`/`NCollection_Array1<…>`; non-public nested classes stay out |
| class declaring no constructor | implicit default constructor bound only if `std::is_default_constructible_v<T>` (compile-time helper `nanoocp_implicit_default_ctor`) | a reference member deletes the implicit constructor without the header saying so (`MathRoot::MultipleGetValueFn`) |
| default argument naming something from a namespace unqualified (`= LeastSquaresMethod::QR` inside `namespace MathLin`, `= THE_2PI` via `using namespace MathUtils`) | qualified from the AST reference (`MathLin::LeastSquaresMethod::QR`, `MathUtils::THE_2PI`) | the expression is emitted outside the namespace |
| method declared, never defined by OCCT (`math_NewtonMinimum::IsConvex`, `OSD_Path::LocateExecFile`) | skipped automatically | `generator/symbols.py`: `nm` on the toolkit library vs. methods without an inline definition (bodies are parsed so `get_definition()` sees out-of-class inline definitions; pure virtuals excluded); overload-specific cases stay in `overrides.toml` |
| class with several bases (`IMeshData_Edge : IMeshData_TessellatedShape, IMeshData_StatusOwner`) | first base only, others reported | nanobind single inheritance (4.2) |
| array parameter (`const Poly_CoherentTriangle *pTri[2]`) | skipped | |
| class whose implicit copy/move constructor does not compile (`math_GlobOptMin`) | skipped via `overrides.toml` | nanobind instantiates the move wrapper unconditionally |
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
| `std::ostream&`/`std::istream&` (`DumpJson`, `InitFromJson`), raw pointers to primitives, references to pointers (`char*&`), pointers to incomplete types (`_xlocale*`), `double&` *returns* (`ChangeValue`), C-array fields, reference-typed fields, template members, nested class templates, non-public bases | skipped | reported; to be revisited per case (e.g. `DumpJson` → `str`) |

### 6a. NCollection containers (hand-written binders)

**Facts.** OCCT 8.0.1 spells containers directly in its API (`Geom_BSplineCurve(const NCollection_Array1<gp_Pnt>& Poles, …)`; 2050 distinct `NCollection_*<…>` spellings in the installed headers), and the pre-8.0 typedef names (`TColgp_Array1OfPnt`, `TopTools_ListOfShape`, 972 headers) live in `src/Deprecated/NCollectionAliases`, outside every toolkit, each marked deprecated with "use `NCollection_Array1<gp_Pnt>` directly". The reference documentation for the container API is therefore the template class page. `NCollection_HArray1<T>` derives from both `NCollection_Array1<T>` and `Standard_Transient`; `NCollection_Array1` has a virtual destructor (polymorphic).

**Decision (2026-09-20, option b).** One hand-written C++ binder per template kind in `src/cpp/common/nanoocp_ncollection.h` (`nanoocp::bind_NCollection_Array1<T>(module, name)`, `bind_NCollection_HArray1<T>`), instantiated by the generator. The alternative — instantiating template members generically via libclang with argument substitution — was rejected: dependent types, `enable_if` overloads and members that do not compile for every element type would each need a special rule, for the same user-visible result.

- **Which instantiations:** every `NCollection_X<…>` (also inside `handle<…>`, also nested) that appears in a bound signature, collected while parsing; nested arguments and `requires` (`Array1<T>` before `HArray1<T>`) are bound first. Over-approximation (unused instantiations) only costs compile time.
- **Primary spelling `NCollection_Array1[T]`** (revised 2026-09-20, replaces "home = element package"): `nanoocp.NCollection.NCollection_Array1[gp.gp_Pnt](1, 4)` mirrors the docs' `NCollection_Array1<gp_Pnt>`. `NCollection_Array1` is a generated `Template` object (`nanoocp/_templates.py`, table in the `NCollection` shim from `manifest.json`) mapping Python element types to the bound classes: `float → double`, `int → int`, `bool → bool`, `str → std::string`, an OCCT class for itself **and** for `handle<class>`, a bound instantiation for a nested container; other C++ scalars (`float`, `size_t`, `char`…) are reachable only by the concrete name. Unbound element types raise `TypeError` listing what is bound; calling the template itself raises `TypeError` with a hint.
- **Concrete classes:** one per C++ instantiation, named `template__arg1__arg2` (double underscore separates arguments — OCCT names never contain `__`; `handle<X>` → `Handle_X`; nested left to right; defaulted template arguments such as hashers are omitted): `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`. They are what `type()`, `repr` and stubs show. All of them live in **`nanoocp.NCollection`** (the doc page's package), bound by the first toolkit that needs them (`manifest.json` records `by`, the binding package, so regeneration is idempotent — verified by running the generator twice). Because a later toolkit adds to `NCollection`, `import nanoocp` imports **all toolkit modules eagerly** in dependency order and shims have a module `__getattr__` fallback.
- **Deprecated typedef names:** parsed from `NCollectionAliases` (one libclang TU, ~1 s) and exposed as lazy aliases: `nanoocp.TColStd.TColStd_Array1OfReal is nanoocp.Standard.NCollection_Array1_double`; prefixes that are not packages in 8.0 (`TColgp`) become alias-only modules. So both 7.x-era docs/OCP code and 8.0 docs resolve.
- **1:1 methods** with OCCT names and signatures; **docstrings extracted from the template header** by the generator into `ncollection_docs.h` (first overload wins); a **coverage check** reports template members that are neither bound nor listed as knowingly skipped (`Move`, `operator=`, `EmplaceValue`, iterators, allocation operators).
- **Python additions** (never replacements, marked "Python addition" in their docstrings): `__len__` (= `Length`), `__iter__` (values `Lower()..Upper()`), `__setitem__` (= `SetValue`). `__call__` and `__getitem__` are OCCT's own `operator()`/`operator[]` = `Value` with the **OCCT index**, not 0-based. `Change*` accessors are bound only for class element types (`double&` cannot be exposed).
- **HArray1 / HArray2 / HSequence / Shared (revised, see 4.2 "Multiple inheritance"):** bound with the offset-0 base (`Array1<T>`, `Array2<T>`, `Sequence<T>`, `T`), so the container API is inherited with an exact pointer and `isinstance(h, NCollection_Array1[T])` holds; `GetRefCount`, `DynamicType`, `IsKind`, `IsInstance`, `get_type_*` are bound through adjusting casts; handles convert both ways through the MI registry. The first version (base `Standard_Transient`, Array API re-bound, implicit conversion) was wrong and is gone. `h.Array1()` returns a sliced copy of static type `Array1` (returning `const A&` would make nanobind copy the dynamic type); `h.ChangeArray1() is h`. Stubs: the H-types derive from the generic container class; `NCollection_Shared[T]` is typed as an accessor with one overload per bound instantiation returning the concrete class (which derives from `T`'s class), because `Generic[_T]` cannot derive from `_T`.
- **Lesson recorded:** nanobind copy-constructs the *dynamic* type for polymorphic by-value/const-reference returns whenever that type is registered. For Transient classes this yields an owned private copy, which is harmless but can surprise; relevant wherever OCCT returns a polymorphic value class by const reference.

- **List / Sequence / HSequence** (2026-09-20): nested `Iterator` classes bound as `NCollection_List__int.Iterator` (1:1 with `NCollection_List<T>::Iterator`; `TopTools_ListIteratorOfListOfShape`-style aliases resolve to them), with `nb::keep_alive` on the container. `size_t` overloads that duplicate `int` ones are not bound (Python cannot distinguish them); `At`/`ChangeAt` (size_t only) are. `Contains`/`Remove(item)`/`__contains__` are bound only when `T` has `operator==` (compile-time trait; `gp_Pnt` has none, `TopoDS_Shape` has). Members returning the inserted element (`Append` → `T&`) return a view for class types and a value for scalars. Members inherited from the non-template bases (`NCollection_BaseList::Extent`, …) are covered by the docs/coverage extractor via `bases`. Python additions: `__len__`, `__iter__`, `__contains__`, and for Sequence `__getitem__`/`__setitem__` (1-based like `Value`). Generic stubs for the three kinds; verified with mypy and ty. Divergence: ty rejects `NCollection_List[int].Iterator` (nested class through a specialised generic), mypy accepts it — typed code uses the concrete `NCollection_List__int.Iterator`.
- **Ordering lesson:** instantiations are registered in the toolkit's *declaration* order, so packages are also *emitted* in that order; otherwise an `HSequence<T>` bound by an early-running package could precede the `Sequence<T>` its implicit conversion needs (observed as `implicitly_convertible: destination type unknown`).

- **Map / DataMap / IndexedMap / IndexedDataMap** (2026-09-20): the hasher template argument is dropped from key and name only when it equals its default `NCollection_DefaultHasher<Key>` (`defaults` per kind in `BINDERS`, applied by `instance_args`); a custom hasher stays part of both, so it cannot be merged with the default instantiation (a different C++ type). Shared base members (`NCollection_BaseMap`: `NbBuckets`, `Extent`, …) in one helper. `Seek`/`ChangeSeek` return `None` for absent keys (a view for class items, a value for scalars); `Find(key, item&)`/`FindFromKey(key, item&)` only for class items (in-place). Skipped: `Contained` (`std::optional<std::reference_wrapper<…>>`), `Emplace*`, `Items()`/`IndexedItems()` views, `GetHasher`. Python additions: `__len__`, `__contains__`, `__iter__` over keys (index order for the indexed kinds), `__getitem__`/`__setitem__`/`__delitem__` on DataMap (`Find`/`Bind`/`UnBind`, `KeyError` when unbound), `__getitem__(index)` on the indexed kinds, `items()` → list of `(key, value)`. The indexed maps' iterators do not derive from `NCollection_BaseMap::Iterator` (no `Initialize`/`Reset`), the others do. Enums count as element types (`NCollection_IndexedMap[Message_MetricType]`).
- **`[instantiate]` override:** instantiations to bind although no bound OCCT signature uses them (`NCollection_Map<int>`, `NCollection_DataMap<int, double>`, …), registered by the `NCollection` package. Used to exercise binders that the current scope does not reach yet, and available for user conveniences.

- **Array2 / HArray2 / DynamicArray / DoubleMap / Shared** (2026-09-20): `Array2<T>` derives from `Array1<T>` in 8.0 and inherits its binding (`__len__`/`__iter__` are flat, row-major; `Value(i)` is hidden by `Value(row, col)` as in C++; `a[(row, col)]` is the Python addition). `DynamicArray` is 0-based (`Lower() == 0`). `DoubleMap` has two default hashers (both stripped when default); iteration yields `(key1, key2)` pairs. `Shared<T>` requires `T` to be bound (class or instantiation), otherwise the instantiation is skipped with a report (`Standard_HMutex = Shared<Standard_Mutex>` is skipped because `Standard_Mutex` is not bound).

All 14 container kinds of the scope are bound.

### 6c. Aliases of OCCT class templates (instantiated from the header)

OCCT 8 turned several classic classes into class templates with aliases: `using math_Vector = math_VectorBase<double>;`, `math_IntegerVector`, `Bnd_B2d/B3d/B2f/B3f`, `BVH_Vec3d = BVH::VectorType<double, 3>::Type` (→ `NCollection_Vec3<double>`), `BVH_Builder3d`, `TColStd_PackedMapOfInteger = NCollection_PackedMap<int>`, `NCollection_String`, later `Extrema_ExtPC = Extrema_GGExtPC<Adaptor3d_Curve, …>`, `GeomLProp_CLProps`. These are not containers, so 6a does not apply; they are the one place where the generic option (a) is used (decision 2026-09-20).

Rule: a package-level `typedef`/`using` whose canonical type is an instantiation of an OCCT class template (not an NCollection binder kind, not `handle`, not `std::`) is bound as a normal class **under the alias name** (`nanoocp.math.math_Vector`, C++ type `math_VectorBase<double>`): the template's definition is walked with the ordinary class walker while a substitution map rewrites every type spelling and default argument — template parameters → arguments (position-wise, using the parameter names of *every* declaration of the template, because a forward declaration may name them differently and libclang spells some dependent types with those names), and the injected class name → the full instantiation (`math_VectorBase` → `math_VectorBase<double>`). Arguments come from the canonical type when the alias goes through a metafunction (`BVH::VectorType<…>::Type`); non-type arguments (`BVH_Builder<double, 3>`) are taken as written. Members whose types stay dependent (libclang's `type-parameter-0-0`, e.g. `T* begin()`) are skipped and reported. Instantiations have no library symbols, so the `nm` check does not apply to them. The same instantiation aliased in several packages is bound once (manifest key = canonical spelling) and aliased elsewhere; the same alias repeated in several headers of one package is bound once. Docstrings come from the template. Stubs: stubgen emits a full concrete class for the alias (no generic class, unlike 6a). Verified: `math_Vector` constructors (incl. from `gp_XYZ`), operators, `math_Matrix.Row()` returning `math_Vector`, `BVH_Vec3d`, `Bnd_B3d`, `TColStd_PackedMapOfInteger`.

### 6b. Type stubs

`python -m generator.stubs` (after the build; it imports the extension) runs nanobind's `StubGen` (API, recursive: the CLI refuses `-r` for modules without `__file__`) per package module into `src/nanoocp/<pkg>.pyi` — or `<pkg>/__init__.pyi` plus `<pkg>/<ns>.pyi` for a package with namespaces (5.1) — (cross-references come out as `nanoocp.Standard.X` because of the `__module__` rule) and adds: the deprecated typedef aliases as assignments; in `NCollection/__init__.pyi` a hand-written **`Generic[_T]` class per container kind** (`generator/stubs/<kind>.pyi`, kept in step with the binder) and every instantiation as `class NCollection_Array1__double(NCollection_Array1[float]): ...`. In every other stub the concrete instantiation names in OCCT signatures are rewritten to the generic spelling (`nanoocp.NCollection.NCollection_Array1__double` → `nanoocp.NCollection.NCollection_Array1[float]`, nested arguments included, missing `import nanoocp.<pkg>` lines added), because the checker types `NCollection_Array1[float](…)` as the generic and would otherwise reject passing it to any OCCT method (`Geom2d_BezierCurve(poles)`); the concrete class derives from the generic one, so results stay assignable. Verified with **mypy** and **ty** (`tests/test_typing.py` runs both on every `tests/typing/check_*.py`): `a[2]` is `float`, `h.Value(1)` is `Standard_Persistent`, `def f(arr: NCollection_Array1[float])` accepts every double array, nested classes and namespace modules resolve (`check_namespaces.py`), and the deliberate errors (wrong element type, wrong overload, `HArray1[X]` passed as `Array1[float]`, `Base` assigned to `Full`) are reported by both checkers. Known imprecision: null handles are typed as the class, not `X | None` (same as nanobind's own handle stubs).

## 7. Build and packaging

- `CMakeLists.txt` at the root: `find_package(OpenCASCADE)` from `NANOOCP_OCCT_DIR` (default `deps/occt-8.0.1`), one `nanobind_add_module` per toolkit from `src/cpp/toolkits.cmake`, `INSTALL_RPATH` pointing at the OCCT lib dir for development builds.
- `pyproject.toml`: scikit-build-core, `wheel.py-api = "cp312"`, `build-dir = "build/{wheel_tag}"` (incremental rebuilds), `wheel.packages = ["src/nanoocp"]`. Development loop: regenerate → `uv sync --reinstall-package nanoocp` → `pytest`.
- Wheels: bundling OCCT dylibs (delocate/auditwheel/delvewheel) is not done yet.
- Tests: `tests/test_<pkg>.py` per package, each generator rule exercised at least once.

## 8. Open questions and next steps

1. `ModelingData` (`TKG2d`, `TKG3d`, `TKGeomBase`, `TKBRep`); the `Extrema_*`/`GeomLProp_*` aliases of ModelingAlgorithms will exercise 6c further.
3. Stubs for the remaining container kinds as their binders arrive; stubs for OCCT out-param tuples are already produced by stubgen.
4. Generator on Linux and Windows (libclang selection, MSVC/libstdc++ header discovery, platform-dependent `#ifdef`s in OCCT headers such as `OSD_*`).
5. Vendor RapidJSON; decide whether to vendor the ~23 clang builtin headers so the pip `libclang` fallback works without a host clang.
6. Wheel bundling and CI matrix.
7. Repository initialisation (`git init`) — pending the user's go.
8. Python-side subclassing of OCCT classes (nanobind trampolines) — not planned for now.

## 9. Working state and how to continue (kept current for context resets)

**State on 2026-09-20 (branch `main`, no remote):** FoundationClasses complete — `TKernel` (18 packages) and `TKMath` (21 packages) — and the first ModelingData toolkit `TKG2d` (6 packages: `Geom2d`, `Adaptor2d`, `Geom2dAdaptor`, `Geom2dHash`, `Geom2dGridEval`, `Geom2dEval`) generated, built, stubbed; all 14 NCollection container kinds bound (6a); class-template aliases instantiated (6c); C++ namespaces and nested classes bound (5.1); 118 tests pass (`tests/`), mypy and ty included. `TKG3d`, `TKGeomBase`, `TKBRep` and everything after are not generated yet. A clean regeneration (`rm src/cpp/manifest.json`, then the three toolkits in order) reproduces the checked-in sources byte for byte.

**Development loop** (venv is `.venv`, managed by `uv`; `deps/occt-8.0.1` and `deps/freetype` are built, `deps/occt-build` is the ninja tree for incremental OCCT rebuilds):

```bash
uv run python -m generator --toolkit TKernel          # regenerate a toolkit (all packages); --package X for one package
uv run python -m generator --toolkit TKMath
uv run python -m generator --toolkit TKG2d
uv sync --reinstall-package nanoocp                    # build + install (scikit-build-core, build dir build/{wheel_tag})
uv run python -m generator.stubs                       # .pyi stubs (after the build; imports the extension)
uv run pytest tests -q
```

Generation order matters the first time after deleting `src/cpp/manifest.json`: dependencies first (`TKernel`, then `TKMath`, …), because the manifest carries bound classes/instantiations across runs. Regenerating everything: `rm src/cpp/manifest.json` then all toolkits in dependency order. A faster compile-only check without installing: `cmake --build build/dev` (configured with `-DPython_EXECUTABLE=$PWD/.venv/bin/python -DCMAKE_INSTALL_PREFIX=$PWD/build/stage`).

**Debugging a nanobind "Critical nanobind error" at import** (Release builds hide the message): build the Debug tree `build/debug` (`cmake -S . -B build/debug -G Ninja -DCMAKE_BUILD_TYPE=Debug -DPython_EXECUTABLE=$PWD/.venv/bin/python -DCMAKE_INSTALL_PREFIX=$PWD/build/stage-debug`, `cmake --build build/debug`, `cmake --install build/debug`, copy `src/nanoocp/*.py` into `build/stage-debug/nanoocp/`), then `PYTHONPATH=build/stage-debug .venv/bin/python -S -c "import nanoocp._TKMath"` — `-S` is required because the editable-install `.pth` hook would otherwise load the Release module. For a C++ exception at init: `lldb --batch -o "break set -E c++" -o run -o "bt 12" -- .venv/bin/python -S -c "import nanoocp._TKernel"`.

**Recurring pitfalls:** safe-chain hides packages younger than 48 h from `uv`; the user overrides it themselves (nanobind is in the exclusions now). A `str.replace(old, new)` with an empty `old` inserts `new` between every character — it happened once to `parse.py` and was recovered exactly; use asserts on anchors. Partial regeneration of a single package is safe (toolkit module stays complete, manifest entries of the package are refreshed). Every new package tends to reveal one or two OCCT-specific idioms: the report printed by the generator (`- …: reason`) is the place to look, and the compiler/linker tells the rest.

**Next steps, in order:** (1) ModelingData continued: `TKG3d` (expect the 3D twins of everything TKG2d brought: `GeomEval_RepCurveDesc`/`GeomEval_RepSurfaceDesc` namespaces, `ResD1`-style nested structs, `GeomGridEval`), then `TKGeomBase` (`Extrema_*`/`GeomLProp_*` aliases (6c), `ExtremaPC`/`LProp_CurveUtils` namespaces) and `TKBRep` (`TopoDS` namespace functions with `const T&`/`T&` overload pairs, `BRepGraph*` iterator namespaces incl. `Detail` — skipped). Python subclassing of `Adaptor3d_Curve` remains not planned. (2) ModelingAlgorithms. (3) Phase 2 (`ApplicationFramework` subset, `DataExchange`), plus the font slice of Visualization (`Font`, `StdPrs_BRepFont`, `StdPrs_BRepTextBuilder` — TKService/TKV3d must be added as toolkits). (4) Linux/Windows runs of the generator and the wheel pipeline (bundle OCCT dylibs; the static FreeType is inside `libTKService`).

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
- **2026-09-20** — Multiple-inheritance rule discovered and fixed (offset-0 base + MI registry in the handle caster); `Array2`, `HArray2`, `DynamicArray`, `DoubleMap`, `Shared` bound — all 14 NCollection kinds done (72 tests).
- **2026-09-20** — Aliases of OCCT class templates instantiated from the header (6c): `math_Vector`, `Bnd_B*`, `BVH_Vec*`, `TColStd_PackedMapOfInteger`, … (99 tests). Partial regeneration (`--package`) keeps the toolkit module complete (package order stored in the manifest).
- **2026-09-20** — Rest of `TKMath` generated (21 packages, 98 tests): namespaces descended (constants bound, templates reported), anonymous enums as constants, `nm`-based check for declared-but-undefined methods (full-body parsing), first-base-only rule for multi-base classes, array parameters skipped, template arguments respelled recursively (nested types), non-type template arguments kept as written, `math_GlobOptMin` skipped. Open: aliases of OCCT class templates (`math_Vector`, `Extrema_ExtPC`, …).
- **2026-09-20** — `TKG2d` generated (6 packages, 118 tests). C++ namespaces bound: package-named namespace = package module, others = submodules backed by Python sub-packages (`nanoocp/<pkg>/<ns>.py`, stubs alongside); `std`/`detail`/`Detail`/`Internal` skipped via `overrides.toml`. Public nested classes bound into their outer class. Namespace functions bound (with out-param tuples) and their defaults qualified from AST references. `nm` regex fixed for `operator()` (`Geom2dHash_CurveHasher`, `std::hash` were wrongly reported undefined). Implicit default constructors guarded by `std::is_default_constructible_v`; reference-typed fields skipped. Stubs: concrete container names rewritten to the generic spelling in OCCT signatures; `stubgen` driven through its API. Regenerating `TKernel`/`TKMath` with these rules added the `MathUtils`/`MathLin`/`MathOpt`/`MathRoot`/`MathSys`/`MathPoly`/`MathInteg` namespace functions and `NCollection_Primes`.
