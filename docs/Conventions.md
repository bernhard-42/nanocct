# 3. Conventions

Part of the nanocct design documents in `docs/`, indexed in [Design.md](Design.md); their section numbers and the `R-…` rule identifiers are shared across them.

## 3.1 Naming conventions


Every Python name is the OCCT name. Three generated additions exist because Python cannot express the C++ idiom; they follow one lexical rule:

> **OCCT names contain single underscores (`gp_Pnt`, `Geom_Curve`), so the parts of a generated name are separated by double underscores `__`.**

These conventions are the ones a user must know (they go into the README); everything else in section 6 is a rule about *what* is bound, not about names.

### 1. Every static method gets `_s` (R-STATIC-S)

- `BRep_Tool.Pnt_s(vertex)`, `gp_QuaternionNLerp.Interpolate_s(...)`, `XCAFDoc_DocumentTool.ShapeTool_s(label)` — code ported from cadquery-ocp keeps these calls unchanged (10).
- Only static member functions of a class: functions of a C++ namespace are module functions and keep their names (`TopoDS.Edge(shape)`, OCCT 8's `namespace TopoDS`).

### 2. Container instantiations: `<template>__<arg1>__<arg2>…` (6a)

- The concrete class: `Handle_X` for `handle<X>`, nested instantiations spelled recursively — `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`.
- The primary spelling is the generic accessor `NCollection_DataMap[TopoDS_Shape, Geom_Surface](...)`, where a Python type stands for the C++ argument: `float` → `double`, `int`, `bool`, `str` → `std::string`, an OCCT class for itself *and* for `handle<class>`. The five C++ scalars without a Python type of their own are spelled by marker types from `nanocct.NCollection`: `float32` → `float` (32-bit), `uchar` → `unsigned char`, `uint` → `unsigned int`, `ulong` → `unsigned long`, `ulonglong` → `unsigned long long` — so `NCollection_HArray1[float32]` is `NCollection_HArray1__float`, and `[float]` stays C++ `double`.

### 3. Out-parameters become results; colliding overloads get `<method>__<type1>__<type2>…` (R-OUT, R-COLLISION)

- A non-const reference to a primitive, enum or `handle<T>` is dropped from the parameters and returned, after the C++ return value if there is one — `curve, first, last = BRep_Tool.Curve_s(edge)`.
- Class-typed references (`gp_Pnt&`) stay parameters and are filled in place.
- When two overloads have the same inputs and differ only in those out-parameters, **each overload with out-parameters is named `<method>__<type1>__<type2>…`** with the Python types of its returned out-parameters in order:
    - `u, v, w = ics.Parameters__float__float__float(i)` next to `u1, v1, u2, v2 = ics.Parameters__float__float__float__float(i)`;
    - `curve = GeomTools.Read_s__Geom_Curve(stream)`;
    - `x, y, z = pnt.Coord__float__float__float()` next to `pnt.Coord()`, which returns the `gp_XYZ` as in C++ (`const gp_XYZ& Coord()`, `gp_Pnt.hxx:108`); `bnd.Get()` returns `Bnd_Box.Limits` and `bnd.Get__float__float__float__float__float__float()` the six numbers.
- An overload without out-parameters always keeps the plain name, even where a sibling class spells the same name differently (`gp_Dir.Coord()` has no `gp_XYZ` twin and returns the three floats). There is no exception: the name follows from the header alone.
- Types are spelled as in convention 2: `float`, `int`, `bool`, `str` — also for a text stream, `bytes` for a binary one — an enum or class by its Python name, a container by its concrete name.
- The suffix appears only where a collision exists, and after a static's `_s` (`GeomTools.Read_s__Geom_Curve(stream)`).

### Two further name adjustments, mechanical and rare

- A C++ identifier that is a Python keyword gets a trailing underscore (`GProp_PEquation.Type.None_`, R-KEYWORD).
- A mutable reference to a primitive (`double& Value(i, j)`) is bound as the getter plus a `Set<Name>` / `__setitem__` addition (R-REF-PRIMITIVE, Python additions).

## 3.2 Parameter conventions


Overloads that Python cannot tell apart and that carry no new name (section 6 has the rules and the counts), plus the parameter types that need a word:

- **Const twins: only the non-const overload is bound** (R-CONST-TWIN).
    - `const gp_XYZ& Origin() const` / `gp_XYZ& Origin()`, `TopoDS.Vertex(const TopoDS_Shape&)` / `(TopoDS_Shape&)`.
    - Python objects are never const, so the non-const overload is the one C++ would select.
    - Class results of the bound twin are views into their owner (`arr[i].SetX(…)` edits the container); primitives are values with a `Set<Name>` addition.
- **Scalar width: `double` over `float`, `int` over `size_t`/`unsigned`/`long`** (R-WIDTH).
    - `Abs(double)`/`Abs(float)`, `Value(int)`/`Value(size_t)` are both bound; a Python `float`/`int` goes to the wider one.
- **Strings:** `const char*`, `char` and `TCollection_AsciiString`/`ExtendedString` parameters all take a `str` (a `char` a one-character one) and behave alike; UTF-16 (`char16_t`) round-trips as `str`. A `const char*` with a null default (`LDOM_XmlWriter(const char* theEncoding = nullptr)`, `STEPCAFControl_Writer::Transfer(…, const char* theIsMulti = nullptr)`) is `str | None = None` (R-CSTR-NULL). **Trap, OCCT's own default:** `TCollection_ExtendedString("pärt")` selects `ExtendedString(const char*, theIsMultiByte = false)` and copies the UTF-8 *bytes* as characters (`"pÃ¤rt"`); pass `True` (`TCollection_ExtendedString("pärt", True)`) for non-ASCII text — as in C++.
- **Handles:** every `handle<T>` parameter accepts `None` (the null handle); a returned null handle is `None`.
- **`std::ostream&` / `std::istream&`:**
    - an output stream parameter becomes a returned `str` (`bytes` for **document streams whatever the format** — `BinTools`, the `Bin*`/`Xml*` OCAF driver packages and the format-agnostic `PCDM`/`CDF`/`TDocStd_Application` entry points; a serialised XML document is bytes with an encoding declaration, `data.decode()`/`xml.etree` take it — and for the binary flavour of a format that has both: `RWStl.WriteBinary_s(mesh) -> (ok, bytes)` next to `WriteAscii(mesh) -> (ok, str)`);
    - an input stream parameter takes a text (`io.StringIO`, an open file) or binary (`io.BytesIO`) file-like object — never a `str`, so the file-path overloads stay reachable. A reader that *sniffs* which flavour it got takes bytes, the superset: `RWStl.ReadStream_s(io.BytesIO(...))` accepts binary and ASCII STL alike, while `ReadAsciiStream` stays `typing.TextIO`. Same for the mesh readers — `RWGltf_CafReader.Perform(io.BytesIO(...))` reads a binary `.glb` and a JSON `.gltf` alike, because `RWMesh_CafReader` opens its own files with `std::ios_base::binary` (`RWMesh_CafReader.hxx:187,225`).
- **Optional pointers are dropped** (R-OPTIONAL-PTR): a pointer parameter with a null default (`bool* theIsStored = nullptr` in `BRep_Tool::CurveOnSurface`, `unsigned* theErrorCode = 0` in `BRepFill_AdvancedEvolved::IsDone`, `Standard_OStream* = nullptr` in `BRepBuilderAPI_FastSewing::GetStatuses`) is not in the Python signature; the callee always gets the null pointer.
- The same holds for a **`std::shared_ptr<T>` parameter defaulted to its own empty form** (`RWPly_PlyWriterContext::Open(name, const std::shared_ptr<std::ostream>& = std::shared_ptr<std::ostream>())`): the type has no caster, but its default needs none — the parameter is dropped and the callee gets `nullptr`, which is that same empty `shared_ptr`. `Open(path)` therefore works; without the rule the whole method would be skipped, and `RWPly_PlyWriterContext` — every other member of which needs the stream `Open` creates — would be bound and unusable.
- **Fixed-size arrays are sequences** (R-FIXED-ARRAY): `const int (&theNodes)[3]` takes any sequence of 3 ints; a non-const `gp_Pnt theP[8]` is an out-parameter returned as a list of 8 (`ok, corners = obb.GetVertex()`); a `double myPeriod[3]` member is a list property.
- **Pointer results** (R-RESULT, R-PTR-REF): a returned `T*` (also `T*&`) is the object itself, referencing the owner and keeping it alive (`fuse.Builder()`, `builder.PDS()`); a returned `Transient*` is a handle.
