# 7. Binding rules (1:1 and the documented deviations)

Part of the nanocct design documents in `docs/`, indexed in [Design.md](Design.md); their section numbers and the `R-…` rule identifiers are shared across them.

Every rule carries an identifier (`R-OUT`, `R-STREAM-OUT`, …) that the code cites in a comment at the rule's sites: `grep -rn R-COLLISION generator/` finds the implementation of a rule, and a comment in the generator points back here. The rules are grouped by theme; 3.1, 3.2 and the Python additions of Design.md summarise the user-facing ones.

Each rule is one entry: the **C++ Idiom** it covers, **OCCT examples** from the OCCT 8.0.1 headers, the **Rule** (why the binding does what it does), what the binding does in **Python**, and **Python examples**, which run as part of the test suite (`tests/test_doc_examples.py`). An identifier that covers several idioms has one case per idiom.

Counts describe OCCT 8.0.1 as generated on macOS; a number marked in the source (`<!-- count: … -->`) is recounted by `tests/test_doc_counts.py` from the generated code, so it cannot go stale unseen. An unmarked count says "measured once": it was counted when its rule was written and is not recounted. Timings are illustrative: measured on an Apple M5 (macOS), best of several runs, and not re-measured on every change.

## 7.1 The 1:1 baseline

### R-BASELINE

- **C++ Idiom**

    Method, constructor, static method, public field, enum

- **OCCT examples**

    - `gp_Pnt::gp_Pnt(const double theXp, const double theYp, const double theZp)` (a constructor)
    - `double gp_Pnt::Distance(const gp_Pnt& theOther) const` (a method)
    - `static gp_Pnt BRep_Tool::Pnt(const TopoDS_Vertex& V)` (a static method; R-STATIC-S adds `_s`)
    - `double Bnd_Range::Bounds::Min` (a public field)
    - `enum TopAbs_ShapeEnum { TopAbs_COMPOUND, TopAbs_COMPSOLID, TopAbs_SOLID, TopAbs_SHELL, TopAbs_FACE, TopAbs_WIRE, TopAbs_EDGE, TopAbs_VERTEX, TopAbs_SHAPE }` (an enum)

- **Rule**

    - 1:1.
    - Overloads are chained `.def`s, resolved by nanobind.

- **Python**

    - Same name (a static method with the suffix `_s`, R-STATIC-S).

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from nanocct.Bnd import Bnd_Range
    from nanocct.gp import gp_Pnt
    from nanocct.TopAbs import TopAbs_ShapeEnum

    point = gp_Pnt(1, 2, 3)                           # the constructor
    assert gp_Pnt().X() == 0.0                        # another overload of it, chosen by nanobind
    assert point.Distance(gp_Pnt(1, 2, 5)) == 2.0     # the method
    vertex = BRepBuilderAPI_MakeVertex(point).Vertex()
    assert BRep_Tool.Pnt_s(vertex).Z() == 3.0         # the static method (the _s is R-STATIC-S)
    assert Bnd_Range(1.0, 3.0).Get().Min == 1.0       # the public field
    assert int(TopAbs_ShapeEnum.TopAbs_FACE) == 4     # the enum
    ```
### R-DOCSTRING

- **C++ Idiom**

    `//!` comments

- **OCCT examples**

    - `//! Defines a 3D cartesian point.` above `class gp_Pnt` (`gp_Pnt.hxx:30`)
    - `//! Computes the distance between two points.` above `double gp_Pnt::Distance(const gp_Pnt& theOther) const` (`gp_Pnt.hxx:130`)
    - `double Min; //!< Minimum value of the range` in `struct Bnd_Range::Bounds` (`Bnd_Range.hxx:38`, a trailing comment)

- **Rule**

    - Class and member docs come from `raw_comment`.

- **Python**

    - Docstrings.

- **Python examples**

    ```python
    from nanocct.Bnd import Bnd_Range
    from nanocct.gp import gp_Pnt

    assert gp_Pnt.__doc__ == "Defines a 3D cartesian point."
    assert gp_Pnt.Distance.__doc__.endswith("\n\nComputes the distance between two points.")   # after nanobind's signature
    assert vars(Bnd_Range.Bounds)["Min"].__doc__ == "Minimum value of the range"
    ```

## 7.2 Names

What a member, class or enumerator is called in Python (the user-facing summary is 3.1).

### R-STATIC-S

- **C++ Idiom**

    Every static member function

- **OCCT examples**

    - `static gp_Pnt BRep_Tool::Pnt(const TopoDS_Vertex& V)`
    - `static occ::handle<XCAFDoc_ShapeTool> XCAFDoc_DocumentTool::ShapeTool(const TDF_Label& acces)`
    - `static occ::handle<XCAFDoc_NoteBalloon> XCAFDoc_NoteBalloon::Set(const TDF_Label& theLabel, const TCollection_ExtendedString& theUserName, const TCollection_ExtendedString& theTimeStamp, const TCollection_ExtendedString& theComment)` (next to the inherited instance `void XCAFDoc_Note::Set(const TCollection_ExtendedString& theUserName, const TCollection_ExtendedString& theTimeStamp)`)
    - `TopoDS_Edge& TopoDS::Edge(TopoDS_Shape& theShape)` (a function of a C++ namespace)
    - `static int NCollection_Array2::BeginPosition(int theRowLower, int /*theRowUpper*/, int theColLower, int theColUpper)` (bound by a hand-written binder)

- **Rule**

    - Code ported from cadquery-ocp keeps every static call unchanged (the porting guide, 10).
    - It also retires a whole class of bugs: Python cannot hold a static and an instance method of one name, nanobind refuses the second registration (*"mismatched static/instance method flags in function overloads"*), and without the suffix the collision would have to be decided over whole inheritance chains (`XCAFDoc_NoteBalloon`'s static `Set` against `XCAFDoc_Note`'s instance `Set` two levels up aborts the import of `_TKXCAF`).
    - With every static suffixed a static and an instance method can never share a name.
    - The hand-written binders follow the same rule (`get_type_name_s`, `NCollection_Array2.BeginPosition_s`).

- **Python**

    - Bound as `Name_s` (`BRep_Tool.Pnt_s`, `XCAFDoc_DocumentTool.ShapeTool_s`).
    - Functions of a C++ namespace are module functions and keep their names (`TopoDS.Edge`).

- **Python examples**

    ```python
    from nanocct import TopoDS
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from nanocct.Geom import Geom_Line
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array2
    from nanocct.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_NoteBalloon

    maker = BRepBuilderAPI_MakeEdge(gp_Pnt(0, 0, 0), gp_Pnt(2, 0, 0))
    assert not TopoDS.Edge(maker.Shape()).IsNull()          # a namespace function keeps its name
    assert BRep_Tool.Pnt_s(maker.Vertex2()).X() == 2.0      # a static method: Name_s
    assert hasattr(XCAFDoc_DocumentTool, "ShapeTool_s") and not hasattr(XCAFDoc_DocumentTool, "ShapeTool")
    assert hasattr(XCAFDoc_NoteBalloon, "Set_s") and hasattr(XCAFDoc_NoteBalloon, "Set")   # static and instance Set side by side
    assert Geom_Line.get_type_name_s() == "Geom_Line"
    assert NCollection_Array2[float].BeginPosition_s(1, 2, 1, 3) == 4                       # a hand-written binder's static
    ```
### R-KEYWORD

- **C++ Idiom**

    C++ identifier that is a Python keyword

- **OCCT examples**

    `GProp_PEquation::Type::None`, the parameter `with` of `TDF_TagSource::Restore` and other overrides of `TDF_Attribute::Restore`:

    - `enum class GProp_PEquation::Type { None, Point, Line, Plane, Space }`
    - `void TDF_TagSource::Restore(const occ::handle<TDF_Attribute>& with) override` (`TDF_Attribute.hxx:284` itself names the parameter `anAttribute`)

- **Rule**

    - PEP 8 / pybind11 convention.
    - Applies to enumerators, methods, fields, functions and parameter names (the stub `Restore(self, with: …)` would be a syntax error), and to the names of classes, enums, constants, type aliases and namespaces, through every Python path that names them (none in OCCT 8.0.1 is a keyword).

- **Python**

    - Trailing underscore (`None_`, `with_`).

- **Python examples**

    ```python
    from nanocct.GProp import GProp_PEquation
    from nanocct.TDF import TDF_TagSource

    assert GProp_PEquation.Type.None_.name == "None_"    # the enumerator None
    source = TDF_TagSource()
    source.Set(5)
    copy = TDF_TagSource()
    copy.Restore(with_=source)                            # the parameter with
    assert copy.Get() == 5
    ```
### R-TEMPLATE-NAME

- **C++ Idiom**

    Explicit template specialisation without an OCCT typedef

- **OCCT examples**

    `NCollection_Lerp<gp_Trsf>`:

    - `template <> class NCollection_Lerp<gp_Trsf>` (`gp_TrsfNLerp.hxx:32`; no header declares a typedef of it)
    - `void NCollection_Lerp<gp_Trsf>::Interpolate(double theT, gp_Trsf& theResult) const`

- **Rule**

    - The 7a naming: `<` and `,` → `__`, `>` dropped.

- **Python**

    - Named `NCollection_Lerp__gp_Trsf`.

- **Python examples**

    ```python
    from nanocct.gp import NCollection_Lerp__gp_Trsf, gp_Trsf, gp_Vec

    start, end = gp_Trsf(), gp_Trsf()
    end.SetTranslation(gp_Vec(2, 0, 0))
    lerp = NCollection_Lerp__gp_Trsf(start, end)
    half = gp_Trsf()
    lerp.Interpolate(0.5, half)
    assert half.TranslationPart().X() == 1.0
    ```
### R-ALIAS

- **C++ Idiom**

    `typedef`/`using` of a bound class, at package level or in a namespace

- **OCCT examples**

    - `using CurveD1 = Geom_Curve::ResD1` in `namespace GeomGridEval` (`GeomGridEval.hxx:30`)
    - the deprecated `using GCE2d_MakeSegment = GC_MakeSegment2d` (`GCE2d_MakeSegment.hxx:25`, with `Standard_DEPRECATED_STD(...)` before the `=`)
    - `typedef StdPrs_BRepFont Font_BRepFont` (`Font_BRepFont.hxx:21`, a target in a later toolkit)
    - `typedef double Standard_Real` (`Standard_TypeDef.hxx:76`, a scalar typedef)
    - `typedef OSD_StreamBuffer<std::istream> OSD_IStreamBuffer` (`OSD_StreamBuffer.hxx:41`, a skipped target)

- **Rule**

    - A target in a *later* toolkit is **not** aliased and is reported: the module would have to import a toolkit that imports it back, and the half-initialised module has no submodules registered yet -- aliased, `Font_BRepFont = StdPrs_BRepFont` (TKService → TKV3d) makes `import nanocct._TKV3d` fail on its own.
    - R-CONV skips a forward target for the same reason.
    - Scalar typedefs (`Standard_Real`) and aliases of unbound types are not exposed (reported when in a namespace, and at package level when the target is a skipped class or a member of one: `OSD_IStreamBuffer`, 6.2).
    - Deprecated class aliases are kept (they are how 7.x code and docs resolve).

- **Python**

    - Attribute alias (`nanocct.GeomGridEval.CurveD1 is nanocct.Geom.Geom_Curve.ResD1`).
    - The stub says `CurveD1 = nanocct.Geom.Geom_Curve.ResD1` (stubgen would write `from nanocct.Geom import ResD1 as CurveD1`, which is wrong for nested classes and, per the typing spec, not a re-export — ty enforces that; `generator/stubs.py` writes the assignment).

- **Python examples**

    ```python
    import nanocct.Font
    import nanocct.Geom
    import nanocct.GeomGridEval
    import nanocct.OSD
    import nanocct.Standard
    from nanocct.GC import GC_MakeSegment2d
    from nanocct.GCE2d import GCE2d_MakeSegment

    assert nanocct.GeomGridEval.CurveD1 is nanocct.Geom.Geom_Curve.ResD1
    assert GCE2d_MakeSegment is GC_MakeSegment2d                 # a deprecated alias is kept
    assert not hasattr(nanocct.Font, "Font_BRepFont")            # StdPrs_BRepFont lives in the later TKV3d
    assert not hasattr(nanocct.Standard, "Standard_Real")        # a scalar typedef
    assert not hasattr(nanocct.OSD, "OSD_IStreamBuffer")         # its target class is skipped
    ```
### R-NAMESPACE

- **C++ Idiom**

    `constexpr` constants, functions, classes, enums in a namespace

- **OCCT examples**

    `MathUtils::THE_NEWTON_MAX_ITER`, `MathLin::LeastSquares`, `Geom2dGridEval::CurveD1`, `Geom2dEval_RepCurveDesc::Base`:

    - `size_t MathUtils::THE_NEWTON_MAX_ITER = 100` (`MathUtils_Config.hxx:30`, package `MathUtils`)
    - `LeastSquaresResult MathLin::LeastSquares(const math_Matrix& theA, const math_Vector& theB, LeastSquaresMethod theMethod = LeastSquaresMethod::QR, double theTolerance = 1.0e-15)`
    - `enum class MathLin::LeastSquaresMethod { NormalEquations, QR, SVD }`
    - `struct Geom2dGridEval::CurveD1 { gp_Pnt2d Point; gp_Vec2d D1; }`
    - `class Geom2dEval_RepCurveDesc::Base : public Standard_Transient` (`Geom2dEval_RepCurveDesc.hxx:58`, a namespace of package `Geom2dEval`)

- **Rule**

    - OCCT 8 uses namespaces as packages-within-packages.

- **Python**

    - Attributes of the package module when the namespace is named like the package, else of the submodule `nanocct.<pkg>.<ns>` (6.1).

- **Python examples**

    ```python
    import nanocct.Geom2dEval.Geom2dEval_RepCurveDesc as desc
    import nanocct.Geom2dGridEval
    import nanocct.MathLin
    import nanocct.MathUtils
    from nanocct.math import math_Matrix, math_Vector

    assert nanocct.MathUtils.THE_NEWTON_MAX_ITER == 100          # namespace MathUtils of package MathUtils
    matrix = math_Matrix(1, 2, 1, 1, 1.0)
    rhs = math_Vector(1, 2, 0.0)
    rhs.SetValue(1, 1.0)
    rhs.SetValue(2, 3.0)
    result = nanocct.MathLin.LeastSquares(matrix, rhs, nanocct.MathLin.LeastSquaresMethod.SVD)
    assert result.IsDone() and abs(result.Solution.Value(1) - 2.0) < 1e-12
    assert nanocct.Geom2dGridEval.CurveD1.__name__ == "CurveD1"
    assert issubclass(desc.Full, desc.Base)                       # the submodule nanocct.Geom2dEval.Geom2dEval_RepCurveDesc
    ```
### R-NESTED

- **C++ Idiom**

    Public nested class/struct

- **OCCT examples**

    `Geom2d_Curve::ResD1`, `Bnd_Range::Bounds`:

    - `struct Geom2d_Curve::ResD1 { gp_Pnt2d Point; gp_Vec2d D1; }`
    - `struct Bnd_Range::Bounds { double Min; double Max; }`
    - `[[nodiscard]] virtual ResD1 Geom2d_Curve::EvalD1(const double U) const = 0` (an OCCT 8 result struct)
    - `[[nodiscard]] std::optional<Bounds> Bnd_Range::Get() const` (inside `std::optional`)
    - `NCollection_Array1<GeomGridEval::CurveD1> GeomGridEval_Circle::EvaluateGridD1(const NCollection_Array1<double>& theParams) const` (inside `NCollection_Array1<…>`; `GeomGridEval::CurveD1` is `Geom_Curve::ResD1`)

- **Rule**

    - OCCT 8 result structs (`EvalD1() -> ResD1`), also inside `std::optional`/`NCollection_Array1<…>`.
    - Non-public nested classes stay out.

- **Python**

    - Attribute of the outer class, fields/methods 1:1.

- **Python examples**

    ```python
    from nanocct.Bnd import Bnd_Range
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_FastSewing
    from nanocct.Geom2d import Geom2d_Circle, Geom2d_Curve
    from nanocct.gp import gp_Ax2d, gp_Circ2d, gp_Dir2d, gp_Pnt2d

    circle = Geom2d_Circle(gp_Circ2d(gp_Ax2d(gp_Pnt2d(0, 0), gp_Dir2d(1, 0)), 1.0))
    d1 = circle.EvalD1(0.0)
    assert isinstance(d1, Geom2d_Curve.ResD1) and (d1.Point.X(), d1.D1.Y()) == (1.0, 1.0)

    bounds = Bnd_Range(1.0, 3.0).Get()                            # std::optional<Bnd_Range::Bounds>
    assert isinstance(bounds, Bnd_Range.Bounds) and (bounds.Min, bounds.Max) == (1.0, 3.0)
    assert Bnd_Range().Get() is None                              # a void range: nullopt

    assert not hasattr(BRepBuilderAPI_FastSewing, "FS_Vertex")    # a protected nested struct
    ```
### R-ENUM

#### Case 1: unscoped enum

- **C++ Idiom**

    Unscoped enum

- **OCCT examples**

    - `enum TopAbs_ShapeEnum { TopAbs_COMPOUND, TopAbs_COMPSOLID, TopAbs_SOLID, TopAbs_SHELL, TopAbs_FACE, TopAbs_WIRE, TopAbs_EDGE, TopAbs_VERTEX, TopAbs_SHAPE }`
    - `enum TopoDS_TShape::BitLayout : uint16_t { …, Bits_Reserved = 0xF000 }` (`TopoDS_TShape.hxx:69`, a class-nested enum)
    - `enum Font_FontAspect { …, Font_FA_Bold = Font_FontAspect_Bold, … }` (`Font_FontAspect.hxx:30`, below the comment `// old aliases`)
    - `enum Resource_FormatType { …, Resource_ANSI = Resource_FormatType_ANSI, … }` (`Resource_FormatType.hxx:65`)
    - `enum BinTools_FormatVersion { …, BinTools_FormatVersion_CURRENT = BinTools_FormatVersion_VERSION_4 }` (`BinTools_FormatVersion.hxx:30`)

- **Rule**

    - Matches C++: an unscoped enumerator lives in the enclosing namespace/class.
    - Code written for OCCT 7.x spells them that way (build123d imports such names, `Font_FA_Bold` among them).
    - nanobind's `export_values()` iterates the Python enum class, which hides aliases (`nb_enum.cpp:428`), so the emitter exports those itself.
    - A scoped `enum class` stays nested (`gp_Dir.D.NZ`; `gp_Dir.Z` is the method).

- **Python**

    - `nb::enum_` with `is_arithmetic` (`int(e)` works).
    - The enumerators are also **exported into the enclosing scope** (`.export_values()`: `nanocct.TopAbs.TopAbs_FACE is TopAbs_ShapeEnum.TopAbs_FACE`, `TopoDS_TShape.Bits_Reserved` for a class-nested enum).
    - An **alias enumerator** (`Font_FA_Bold = Font_FontAspect_Bold`, OCCT's "old aliases"; `Resource_ANSI`, `BinTools_FormatVersion_CURRENT`) is exported by name after it.

- **Python examples**

    ```python
    import nanocct.BinTools
    import nanocct.Font
    import nanocct.TopAbs
    from nanocct.BinTools import BinTools_FormatVersion
    from nanocct.Font import Font_FontAspect
    from nanocct.gp import gp_Dir
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopoDS import TopoDS_TShape

    assert nanocct.TopAbs.TopAbs_FACE is TopAbs_ShapeEnum.TopAbs_FACE      # exported into the module
    assert int(TopAbs_ShapeEnum.TopAbs_FACE) == 4                          # is_arithmetic
    assert int(TopoDS_TShape.Bits_Reserved) == 0xF000                      # exported into the class
    assert nanocct.Font.Font_FA_Bold == Font_FontAspect.Font_FontAspect_Bold
    assert nanocct.BinTools.BinTools_FormatVersion_CURRENT == BinTools_FormatVersion.BinTools_FormatVersion_VERSION_4
    assert "Font_FA_Bold" not in [e.name for e in Font_FontAspect]          # hidden from iteration: export_values() misses it
    assert not hasattr(gp_Dir, "NZ") and gp_Dir(gp_Dir.D.NZ).Z() == -1.0   # the scoped gp_Dir::D stays nested
    ```

#### Case 2: nested `enum class`

- **C++ Idiom**

    Nested `enum class`

- **OCCT examples**

    - `enum class gp_Dir::D { X, Y, Z, NX, NY, NZ }`
    - `enum class GProp_PEquation::Type { None, Point, Line, Plane, Space }`

- **Rule**

    - The nested `enum class` stays an attribute of its class, as in C++.

- **Python**

    - Attribute of the class (`gp_Dir.D.Z`).

- **Python examples**

    ```python
    from nanocct.gp import gp_Dir
    from nanocct.GProp import GProp_PEquation

    assert gp_Dir(gp_Dir.D.Z).Z() == 1.0
    assert not hasattr(gp_Dir, "NX")                          # the enumerators stay inside gp_Dir.D
    assert GProp_PEquation.Type.Plane.name == "Plane"
    ```
### R-ENUM-ARG

- **C++ Idiom**

    A parameter of an enum type or a `std::optional` of one, by value or reference

- **OCCT examples**

    - `BRepGraph_ChildExplorer::BRepGraph_ChildExplorer(const BRepGraph& theGraph, const BRepGraph_NodeId theRoot, const std::optional<BRepGraph_NodeId::Kind>& theAvoidKind, bool theEmitAvoidKind, TraversalMode theMode = TraversalMode::Recursive)` (registered first)
    - `BRepGraph_ChildExplorer::BRepGraph_ChildExplorer(const BRepGraph& theGraph, const BRepGraph_NodeId theRoot, BRepGraph_NodeId::Kind theTargetKind, bool theCumLoc, bool theCumOri, TraversalMode theMode = TraversalMode::Recursive)` (C++'s choice)
    - `BRepGraph_ChildExplorer::BRepGraph_ChildExplorer(const BRepGraph& theGraph, const BRepGraph_NodeId theRoot, BRepGraph_NodeId::Kind theTargetKind, const std::optional<BRepGraph_NodeId::Kind>& theAvoidKind, bool theEmitAvoidKind, TraversalMode theMode = TraversalMode::Recursive)` (the `std::optional` case)
    - `void TopoDS_Shape::Orientation(TopAbs_Orientation theOrient)`

- **Rule**

    - C++ converts an enum to an int, never an int to an enum.
    - nanobind's enum caster takes any int that is an enumerator's value in its convert pass, `True`/`False` included (`nb_enum.cpp`, nanobind 3.1.0), and overload resolution needs that pass whenever another argument needs a conversion: `BRepGraph_ChildExplorer(g, BRepGraph_SolidId.Start_s(), Kind.Edge, True, False)` (the typed id becomes a `BRepGraph_NodeId`) would reach `(…, AvoidKind, EmitAvoidKind, TraversalMode)`, registered first, instead of C++'s `(…, TargetKind, CumLoc, CumOri)`.
    - Registration order cannot fix it: the two overloads differ in arity.
    - The optional too: its caster hands the convert flag to the enum caster, and the same call would reach `(…, TargetKind, std::optional<Kind> AvoidKind, EmitAvoidKind)` with `AvoidKind = Kind(1)`; `None` still gives `nullopt`.
    - 2639<!-- count: enum-arg --> arguments carry it (OCCT 8.0.1).
    - A field of an enum type (`def_rw`) still converts; it has no overloads.

- **Python**

    - `nb::arg(...).noconvert()`: only the enum's own enumerators are accepted, an `int` or `bool` raises `TypeError` (`TopAbs_ShapeEnum(4)` converts explicitly).

- **Python examples**

    ```python
    from nanocct.BRepGraph import BRepGraph, BRepGraph_ChildExplorer, BRepGraph_NodeId, BRepGraph_SolidId
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox

    graph = BRepGraph()
    graph.Clear()
    graph.Shapes().Add(BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape())
    explorer = BRepGraph_ChildExplorer(graph, BRepGraph_SolidId.Start_s(), BRepGraph_NodeId.Kind.Edge, True, False)
    edges = 0
    while explorer.More():                    # (TargetKind, CumLoc, CumOri), as in C++
        edges += 1
        explorer.Next()
    assert edges == 24
    root = BRepGraph_NodeId(BRepGraph_SolidId.Start_s())
    assert BRepGraph_ChildExplorer(graph, root, None, False).More()   # None: an empty std::optional AvoidKind
    ```

    ```python
    from nanocct.TopAbs import TopAbs_Orientation
    from nanocct.TopoDS import TopoDS_Vertex

    vertex = TopoDS_Vertex()
    try:
        vertex.Orientation(1)                 # an int is not an enumerator
        raise AssertionError("an int was accepted")
    except TypeError:
        pass
    vertex.Orientation(TopAbs_Orientation(1))                         # the explicit conversion
    assert vertex.Orientation() == TopAbs_Orientation.TopAbs_REVERSED
    ```
### R-ANON-ENUM

- **C++ Idiom**

    Anonymous enum

- **OCCT examples**

    - `enum { BVH_Constants_MaxTreeDepth = 32 };` (`BVH_Constants.hxx:17`, the first of its enumerators, at file scope)
    - `enum { FrustumVert_LeftBottomNear, FrustumVert_LeftBottomFar, … }` in `class Graphic3d_Camera` (`Graphic3d_Camera.hxx:755`)

- **Rule**

    - C++ integer constants.

- **Python**

    - Integer attributes on the module/class.

- **Python examples**

    ```python
    import nanocct.BVH
    from nanocct.Graphic3d import Graphic3d_Camera

    assert nanocct.BVH.BVH_Constants_MaxTreeDepth == 32 and type(nanocct.BVH.BVH_Constants_MaxTreeDepth) is int
    assert Graphic3d_Camera.FrustumVert_LeftBottomNear == 0 and Graphic3d_Camera.FrustumVert_LeftBottomFar == 1
    ```

## 7.3 Parameters and results

How arguments go in and results come out (the user-facing summary is 3.2).

### R-OUT

#### Case 1: non-const reference to a primitive as parameter

- **C++ Idiom**

    Non-const reference to a primitive (`double&`, `int&`, enum) as parameter

- **OCCT examples**

    - `void gp_Pnt::Coord(double& theXp, double& theYp, double& theZp) const` (pure out, the common case)
    - `const BinObjMgt_Persistent& BinObjMgt_Persistent::GetInteger(int& theValue) const` (returns `*this` for chaining)
    - `Storage_BaseDriver& FSD_File::GetReference(int& aValue) override` (returns `*this` through the base's type)
    - `void HLRAlgo_Coincidence::State3D(TopAbs_State& stbef, TopAbs_State& staft) const` (enum out-parameters)
    - `static occ::handle<Geom_Curve> BRep_Tool::Curve(const TopoDS_Edge& E, double& First, double& Last)` (a non-void result)

- **Rule**

    - Pure-out is the common case (`gp_Pnt::Coord`).
    - The out-param lambda copies class results (`auto`), and a copied `Persistent` shares its raw buffers — abort at destruction.
    - A base's dropped self-reference that an override kept would give the override another signature.

- **Python**

    - Dropped from the signature, **returned** (bare value if it is the only result, else a tuple; a non-void return comes first).
    - A result that is a reference to the class itself (`const BinObjMgt_Persistent& GetInteger(int&)`, `*this` for chaining) is dropped like a chained stream: `GetInteger() -> int` -- also a reference to one of its bases, as an override of the base's virtual returns it (`Storage_BaseDriver& FSD_File::GetReference(int&) override`). The same next to a stream parameter of any member, operator or not: a stream always goes through a lambda, whose `auto` result would copy `*this`.

- **Python examples**

    ```python
    from nanocct.BinObjMgt import BinObjMgt_Persistent
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from nanocct.gp import gp_Pnt
    from nanocct.HLRAlgo import HLRAlgo_Coincidence
    from nanocct.TopAbs import TopAbs_State

    # the R-COLLISION suffix tells it from Coord() -> gp_XYZ, which has the same Python signature
    assert gp_Pnt(1, 2, 3).Coord__float__float__float() == (1.0, 2.0, 3.0)

    coincidence = HLRAlgo_Coincidence()
    coincidence.SetState3D(TopAbs_State.TopAbs_IN, TopAbs_State.TopAbs_OUT)
    assert coincidence.State3D() == (TopAbs_State.TopAbs_IN, TopAbs_State.TopAbs_OUT)

    edge = BRepBuilderAPI_MakeEdge(gp_Pnt(0, 0, 0), gp_Pnt(2, 0, 0)).Edge()
    curve, first, last = BRep_Tool.Curve_s(edge)      # the handle result first, then the out-parameters
    assert (first, last) == (0.0, 2.0)

    persistent = BinObjMgt_Persistent()
    persistent.PutInteger(42)
    persistent.SetPosition(persistent.Position() - 4)
    assert persistent.GetInteger() == 42              # *this dropped: the int alone
    ```

    ```python
    import os
    import tempfile
    from nanocct.FSD import FSD_File
    from nanocct.Storage import Storage_OpenMode

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "values.fsd")
        writer = FSD_File()
        writer.Open(path, Storage_OpenMode.Storage_VSWrite)
        writer.PutReference(7)
        writer.Close()
        reader = FSD_File()
        reader.Open(path, Storage_OpenMode.Storage_VSRead)
        assert reader.GetReference() == 7             # the override drops *this as the base's virtual does
        reader.Close()
    ```

#### Case 2: free function with `double&`/`int&` out-parameters

- **C++ Idiom**

    Free function with `double&`/`int&` out-parameters

- **OCCT examples**

    `MathUtils::DepressCubic`:

    - `void MathUtils::DepressCubic(double theB, double theC, double theD, double& theP, double& theQ, double& theShift)`

- **Rule**

    - Out-parameters of a free function are treated like those of methods.

- **Python**

    - Out-params returned as a tuple, like methods.

- **Python examples**

    ```python
    from nanocct import MathUtils

    # x^3 + 3x^2 with x = t - 1 is t^3 - 3t + 2: (p, q, shift)
    assert MathUtils.DepressCubic(3.0, 0.0, 0.0) == (-3.0, 2.0, 1.0)
    ```

#### Case 3: the lambda's own temporaries

- **C++ Idiom**

    The lambda's own temporaries

- **OCCT examples**

    - `static int IGESConvGeom::SplineCurveFromIGES(const occ::handle<IGESGeom_SplineCurve>& igesent, const double epscoef, const double epsgeom, occ::handle<Geom_BSplineCurve>& result)` (an out-parameter called `result` of a non-void method)

- **Rule**

    - OCCT calls parameters `result` (`IGESConvGeom::SplineCurveFromIGES(…, handle<Geom_BSplineCurve>& result)`).
    - A bare `result` is a redefinition when such a parameter is an out-parameter of a non-void method — `TKDEIGES` would not compile.
    - The per-parameter temporaries (`<name>_out`, `<name>_arr`, `<name>_stream`) derive from the parameter's own name, so a clash there needs two OCCT parameters `x` and `x_out` in one signature; the compiler would say so.

- **Python**

    - Prefixed `nanocct_` (`nanocct_result` for the C++ return value).

- **Python examples**

    ```python
    from nanocct.IGESConvGeom import IGESConvGeom

    # bound (TKDEIGES compiles): the int result first, then the out-parameter `result`
    assert IGESConvGeom.SplineCurveFromIGES_s.__doc__.startswith(
        "SplineCurveFromIGES_s(igesent: nanocct.IGESGeom.IGESGeom_SplineCurve | None, epscoef: float, epsgeom: float)"
        " -> tuple[int, nanocct.Geom.Geom_BSplineCurve]")
    ```
### R-INOUT

- **C++ Idiom**

    Same as R-OUT, but the method reads the value too

- **OCCT examples**

    `gp_Trsf::Transforms`:

    - `void gp_Trsf::Transforms(double& theX, double& theY, double& theZ) const`
    - `static void ElCLib::AdjustPeriodic(const double UFirst, const double ULast, const double Precision, double& U1, double& U2)`
    - `bool Bnd_Sphere::IsOut(const gp_XYZ& thePnt, double& theMaxDist) const`
    - `bool gp_Pnt::InitFromJson(const Standard_SStream& theSStream, int& theStreamPos)` (listed for every class as `*::InitFromJson`)
    - `static void GeomLib::ExtendCurveToPoint(occ::handle<Geom_BoundedCurve>& Curve, const gp_Pnt& Point, const int Cont, const bool After)` (a handle, R-OUT-HANDLE)

- **Rule**

    - Listed in `overrides.toml [inout]`.
    - Not derivable from syntax.

- **Python**

    - Parameter kept **and** returned.

- **Python examples**

    ```python
    import io
    import math
    from nanocct.ElCLib import ElCLib
    from nanocct.gp import gp_Pnt, gp_Trsf, gp_Vec

    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(1, 2, 3))
    assert trsf.Transforms(1.0, 1.0, 1.0) == (2.0, 3.0, 4.0)

    u1, u2 = ElCLib.AdjustPeriodic_s(0.0, 2 * math.pi, 1e-9, 7.0, 8.0)   # moved into the period
    assert math.isclose(u1, 7.0 - 2 * math.pi) and math.isclose(u2, 8.0 - 2 * math.pi)

    point = gp_Pnt()
    ok, position = point.InitFromJson(io.StringIO(gp_Pnt(1, 2, 3).DumpJson()), 1)   # read from position 1 on
    assert ok and position > 1 and point.Coord__float__float__float() == (1.0, 2.0, 3.0)
    ```
### R-REF-CLASS

- **C++ Idiom**

    Non-const reference to a class (`gp_XYZ&`)

- **OCCT examples**

    - `void gp_Trsf::Transforms(gp_XYZ& theCoord) const`
    - `static void TDF_Tool::Entry(const TDF_Label& aLabel, TCollection_AsciiString& anEntry)`
    - `static const occ::handle<Geom_Curve>& BRep_Tool::Curve(const TopoDS_Edge& E, TopLoc_Location& L, double& First, double& Last)` (next to out-parameters)

- **Rule**

    - nanobind by-reference semantics.

- **Python**

    - Passed and **mutated in place**.

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.gp import gp_Trsf, gp_Vec, gp_XYZ
    from nanocct.TCollection import TCollection_AsciiString
    from nanocct.TDF import TDF_Data, TDF_Tool
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopLoc import TopLoc_Location
    from nanocct import TopoDS

    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(0, 0, 5))
    xyz = gp_XYZ(1, 1, 1)
    assert trsf.Transforms(xyz) is None and xyz.Z() == 6.0

    data = TDF_Data()
    entry = TCollection_AsciiString()
    TDF_Tool.Entry_s(data.Root().FindChild(3, True), entry)
    assert entry.ToCString() == "0:3"

    moved = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape().Moved(TopLoc_Location(trsf))
    location = TopLoc_Location()
    curve, first, last = BRep_Tool.Curve_s(TopoDS.Edge(TopExp_Explorer(moved, TopAbs_ShapeEnum.TopAbs_EDGE).Current()), location)
    assert location.Transformation().TranslationPart().Z() == 5.0
    ```
### R-OPTIONAL-PTR

- **C++ Idiom**

    Pointer parameter with a null default whose pointee Python cannot pass: a primitive or an enum (`bool*`, `unsigned int*`), `void`, another pointer, a function, a stream (`Standard_OStream*`), or a class only forward-declared and without an installed header; or a `std::shared_ptr` to a stream defaulted to its own empty form. A pointer to a bound class is R-PTR-NULL, a `const char*` R-CSTR-NULL

- **OCCT examples**

    `bool* theIsStored = nullptr` in `BRep_Tool::CurveOnSurface`, `unsigned int* theErrorCode = nullptr` in `BRepFill_AdvancedEvolved::IsDone`, `Standard_OStream* = nullptr` in `BRepBuilderAPI_FastSewing::GetStatuses`, `void* const Addr = nullptr` in `TopOpeBRepBuild_WireEdgeSet`, `RWPly_PlyWriterContext::Open`:

    - `static occ::handle<Geom2d_Curve> BRep_Tool::CurveOnSurface(const TopoDS_Edge& E, const TopoDS_Face& F, double& First, double& Last, bool* theIsStored = nullptr)`
    - `bool BRepFill_AdvancedEvolved::IsDone(unsigned int* theErrorCode = nullptr) const`
    - `FS_VARStatuses BRepBuilderAPI_FastSewing::GetStatuses(Standard_OStream* const theOS = nullptr)`
    - `TopOpeBRepBuild_WireEdgeSet::TopOpeBRepBuild_WireEdgeSet(const TopoDS_Shape& F, void* const Addr = nullptr)` (a constructor)
    - `bool RWPly_PlyWriterContext::Open(const TCollection_AsciiString& theName, const std::shared_ptr<std::ostream>& theStream = std::shared_ptr<std::ostream>())`

- **Rule**

    - Decided by the pointee type alone (`_OPTIONAL_PTR_REASONS` in `parse.py`), not by what the callee does with it: no caster exists for such a pointer, so the parameter cannot be passed from Python at all, and only its null default makes the member callable.
    - Without the rule 59<!-- count: optional-ptr --> members (each overload counted, OCCT 8.0.1) would be skipped entirely (`AdvancedEvolved` would have no `IsDone`), and `Open` is the only way to use `RWPly_PlyWriterContext` at all.

- **Python**

    - Dropped from the signature.
    - The lambda passes `nullptr` (constructors through a placement-new lambda / `nb::new_`).

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_FastSewing
    from nanocct.BRepFill import BRepFill_AdvancedEvolved
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopOpeBRepBuild import TopOpeBRepBuild_WireEdgeSet
    from nanocct import TopoDS

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    face = TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())
    edge = TopoDS.Edge(TopExp_Explorer(face, TopAbs_ShapeEnum.TopAbs_EDGE).Current())
    pcurve, first, last = BRep_Tool.CurveOnSurface_s(edge, face)   # no theIsStored
    assert pcurve is not None and last > first

    assert BRepFill_AdvancedEvolved().IsDone() is False              # no theErrorCode
    assert BRepBuilderAPI_FastSewing(1e-6).GetStatuses() == 0        # no theOS
    assert TopOpeBRepBuild_WireEdgeSet(face).Face().IsSame(face)     # no Addr
    ```

    ```python
    import os
    import tempfile
    from nanocct.RWPly import RWPly_PlyWriterContext

    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "mesh.ply")
        context = RWPly_PlyWriterContext()
        assert context.Open(path)                     # no theStream: OCCT opens the file itself
        assert context.Close()
        assert os.path.exists(path)
    ```
### R-CSTR-NULL

- **C++ Idiom**

    `const char*` parameter with a null default

- **OCCT examples**

    `LDOM_XmlWriter(const char* theEncoding = nullptr)`, `STEPCAFControl_Writer::Transfer(…, const char* const theIsMulti = nullptr)`, `TDF_DerivedAttribute`, `BinMDF_ADriver`/`XmlMDF_ADriver`, the `VrmlData_*` names — 15<!-- count: cstr-null --> parameters in scope (OCCT 8.0.1):

    - `LDOM_XmlWriter::LDOM_XmlWriter(const char* theEncoding = nullptr)`
    - `bool STEPCAFControl_Writer::Transfer(const occ::handle<TDocStd_Document>& theDoc, const STEPControl_StepModelType theMode = STEPControl_AsIs, const char* const theIsMulti = nullptr, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `static NewDerived TDF_DerivedAttribute::Register(NewDerived theNewAttributeFunction, const char* theNameSpace = nullptr, const char* theTypeName = nullptr)` (not bound: its function-pointer parameter)
    - `BinMDF_ADriver::BinMDF_ADriver(const occ::handle<Message_Messenger>& theMsgDriver, const char* const theName = nullptr)` (protected)
    - `void VrmlData_ShapeConvert::AddShape(const TopoDS_Shape& theShape, const char* theName = nullptr)`

- **Rule**

    - nanobind's `const char*` caster rejects `None`, so an emitted default `static_cast<const char*>(nullptr)` would make the zero-argument call `LDOM_XmlWriter()` a `TypeError`.
    - Not R-OPTIONAL-PTR because a `const char*` has a caster (R-CSTRING): a `str` can be passed, so the parameter stays. A non-const `char*` has none and is R-OPTIONAL-PTR.

- **Python**

    - Kept in the signature as `str | None = None`.
    - The lambda passes the `str`'s UTF-8 buffer or `nullptr` (`nanocct::OptionalCString` caster, `nb::arg(...).none()`).

- **Python examples**

    ```python
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.LDOM import LDOM_Document, LDOM_XmlWriter
    from nanocct.STEPCAFControl import STEPCAFControl_Writer
    from nanocct.VrmlData import VrmlData_Scene, VrmlData_ShapeConvert

    document = LDOM_Document.createDocument_s("root")
    for writer in (LDOM_XmlWriter(), LDOM_XmlWriter(None), LDOM_XmlWriter("UTF-8")):
        assert writer.Write(document) == '<?xml version="1.0" encoding="UTF-8"?>\n<root/>'

    scene = VrmlData_Scene()
    converter = VrmlData_ShapeConvert(scene)
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    converter.AddShape(box)
    converter.AddShape(box, "box")
    converter.AddShape(box, None)

    assert "theIsMulti: str | None = None" in STEPCAFControl_Writer.Transfer.__doc__
    ```
### R-PTR-NULL

- **C++ Idiom**

    Pointer to a class nanocct binds (complete, or forward-declared with an installed header, R-PTR-INCOMPLETE), with a null default or without one. Every other pointer with a null default is R-OPTIONAL-PTR; `const char*`/`const char16_t*` are strings (R-CSTR-NULL, R-CHAR16); a listed array taken by its first element is a sequence (R-ARRAY-PTR)

- **OCCT examples**

    With a null default: `BSplCLib_Cache(…, const NCollection_Array1<double>* theWeights = nullptr)`, `const gp_XYZ*`, `const Standard_Transient*`, `const Image_PixMap*`, `NCollection_List<TopoDS_Shape>*` …; without one: `BSplCLib::D0(…, const NCollection_Array1<double>* Weights, …, const NCollection_Array1<int>* Mults, …)`, `PLib::CoefficientsPoles(…, WCoefs, …, WPoles)`, the 2D `BSplCLib_Cache::BuildCache`, `OpenGl_Context*` …:

    - `BSplCLib_Cache::BSplCLib_Cache(const int& theDegree, const bool& thePeriodic, const NCollection_Array1<double>& theFlatKnots, const NCollection_Array1<gp_Pnt>& thePoles, const NCollection_Array1<double>* theWeights = nullptr)`
    - `static void BSplCLib::D0(const double U, const int Index, const int Degree, const bool Periodic, const NCollection_Array1<gp_Pnt>& Poles, const NCollection_Array1<double>* Weights, const NCollection_Array1<double>& Knots, const NCollection_Array1<int>* Mults, gp_Pnt& P)`
    - `static void PLib::CoefficientsPoles(const NCollection_Array1<gp_Pnt>& Coefs, const NCollection_Array1<double>* WCoefs, NCollection_Array1<gp_Pnt>& Poles, NCollection_Array1<double>* WPoles)`
    - `void BSplCLib_Cache::BuildCache(const double& theParameter, const NCollection_Array1<double>& theFlatKnots, const NCollection_Array1<gp_Pnt2d>& thePoles2d, const NCollection_Array1<double>* theWeights)` (the 2D form, no default)
    - `static NCollection_Array1<double>* BSplCLib::NoWeights()` (returns that `nullptr`)

- **Rule**

    - nanobind's pointer caster rejects `None` without `.none()`.
    - With a null default the default itself would be refused, so omitting the argument would be a `TypeError` too (`BSplCLib_Cache(1, False, knots, poles)`).
    - Without one, OCCT's documented null pointer ("No weights (BSplCLib::NoWeights()) means the curve is non rational", `BSplCLib.hxx`; `NoWeights()` returns that `nullptr`, so its result could not even be passed back) would be unreachable.
    - The cost, as in C++ and as with a null handle: `None` where OCCT does not expect a null pointer crashes the process unless OCCT checks it itself (measured: `Extrema_GlobOptFuncCS(None, None).Value(x)` segfaults; null handles already do the same, `BRepBuilderAPI_MakeEdge(None)` and `Geom_TrimmedCurve(None, 0.0, 1.0)` segfault while `GeomAdaptor_Curve(None)` raises `Standard_NullObject`).
    - Only a pointer to a class without a default: `const char*`/`const char16_t*` are strings (R-CSTR-NULL, R-CHAR16).
    - Not R-OPTIONAL-PTR because the pointee is a bound class: Python can pass one (or `None`), so the parameter stays, whether OCCT reads through it or writes through it.
    - Audited against overload resolution: a `None` call can reach another overload (`GeomGridEval_OtherSurface(None)`: the adaptor pointer instead of the handle constructor, both "no surface").

- **Python**

    - A class pointer takes `None` (`nullptr`), like a handle (R-HANDLE): `nb::arg(...).none()`, stub `T | None`.
    - With a null default also `= None`.

- **Python examples**

    ```python
    from nanocct.BSplCLib import BSplCLib_Cache
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array1

    knots = NCollection_Array1[float](1, 4)
    for i, value in enumerate((0.0, 0.0, 1.0, 1.0), start=1):
        knots.SetValue(i, value)
    poles = NCollection_Array1[gp_Pnt](1, 2)
    poles.SetValue(1, gp_Pnt(0, 0, 0))
    poles.SetValue(2, gp_Pnt(2, 0, 0))

    # theWeights omitted (= None) or passed as None: the non-rational cache
    for cache in (BSplCLib_Cache(1, False, knots, poles), BSplCLib_Cache(1, False, knots, poles, None)):
        cache.BuildCache(0.25, knots, poles)
        point = gp_Pnt()
        cache.D0(0.25, point)
        assert point.Coord__float__float__float() == (0.5, 0.0, 0.0)
    ```

    ```python
    from nanocct.BSplCLib import BSplCLib
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array1
    from nanocct.PLib import PLib

    knots = NCollection_Array1[float](1, 4)
    for i, value in enumerate((0.0, 0.0, 1.0, 1.0), start=1):
        knots.SetValue(i, value)
    poles = NCollection_Array1[gp_Pnt](1, 2)
    poles.SetValue(1, gp_Pnt(0, 0, 0))
    poles.SetValue(2, gp_Pnt(2, 0, 0))

    assert BSplCLib.NoWeights_s() is None             # OCCT's "no weights" null pointer
    point = gp_Pnt()
    BSplCLib.D0_s(0.25, 2, 1, False, poles, BSplCLib.NoWeights_s(), knots, None, point)   # non rational, flat knots
    assert point.Coord__float__float__float() == (0.5, 0.0, 0.0)

    out = NCollection_Array1[gp_Pnt](1, 2)
    PLib.CoefficientsPoles_s(poles, None, out, None)  # no weights in, none out
    assert out.Value(2).X() == 2.0
    ```
### R-FIXED-ARRAY

- **C++ Idiom**

    C array of a primitive or bound class with a known size, as parameter or member

- **OCCT examples**

    `gp_Pnt theP[8]` in `Bnd_OBB::GetVertex`, `const int (&theEdges)[3]` in `BRepMesh_Triangle`, `double myPeriod[3]` in `BOPAlgo_MakePeriodic::PeriodicityParams`:

    - `bool Bnd_OBB::GetVertex(gp_Pnt theP[8]) const`
    - `BRepMesh_Triangle::BRepMesh_Triangle(const int (&theEdges)[3], const bool (&theOrientations)[3], const BRepMesh_DegreeOfFreedom theMovability)`
    - `void BRepMesh_Triangle::Edges(int (&theEdges)[3], bool (&theOrientations)[3]) const` (non-const: returned)
    - `double BOPAlgo_MakePeriodic::PeriodicityParams::myPeriod[3]` (a member)

- **Rule**

    - Arrays of unknown size (`double theCoeff[]`), of pointers or of std types stay out (R-ARRAY).

- **Python**

    - Non-const → out-parameter returned as a list of N (suffix type `list`).
    - Const → any sequence of N (`std::array` caster, copied into a C array for the call).
    - Member → list property (`def_prop_rw`, read-only when const).

- **Python examples**

    ```python
    from nanocct.BOPAlgo import BOPAlgo_MakePeriodic
    from nanocct.Bnd import Bnd_OBB
    from nanocct.BRepBndLib import BRepBndLib
    from nanocct.BRepMesh import BRepMesh_Free, BRepMesh_Triangle
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox

    obb = Bnd_OBB()
    BRepBndLib.AddOBB_s(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), obb)
    ok, corners = obb.GetVertex()                     # gp_Pnt theP[8]: a list of 8
    assert ok and len(corners) == 8

    triangle = BRepMesh_Triangle((1, 2, 3), [True, False, True], BRepMesh_Free)   # any sequence of 3
    assert triangle.Edges() == ([1, 2, 3], [True, False, True])

    params = BOPAlgo_MakePeriodic.PeriodicityParams()
    params.myPeriod = (1.0, 2.0, 3.0)
    assert params.myPeriod == [1.0, 2.0, 3.0]
    ```
### R-OUT-HANDLE

- **C++ Idiom**

    Non-const reference to a `handle<T>`

- **OCCT examples**

    `BRep_Tool::CurveOnSurface(E, handle<Geom2d_Curve>& C, handle<Geom_Surface>& S, L, double& First, double& Last)`, `GeomTools::Read(handle<Geom_Surface>&, istream&)`:

    - `static void BRep_Tool::CurveOnSurface(const TopoDS_Edge& E, occ::handle<Geom2d_Curve>& C, occ::handle<Geom_Surface>& S, TopLoc_Location& L, double& First, double& Last)`
    - `static void GeomTools::Read(occ::handle<Geom_Surface>& S, Standard_IStream& IS)`
    - `static void GeomTools::Read(occ::handle<Geom_Curve>& C, Standard_IStream& IS)` (differs only in the out-handle type)
    - `static void GeomLib::ExtendCurveToPoint(occ::handle<Geom_BoundedCurve>& Curve, const gp_Pnt& Point, const int Cont, const bool After)` (in/out)

- **Rule**

    - The caster hands the callee a *temporary* handle, so a handle assigned by the callee would be lost silently.
    - Methods that read the handle first are in/out via `overrides.toml [inout]` (`GeomLib::ExtendCurveToPoint(Curve, …)` keeps `Curve` and returns the extended curve; 14 entries, each checked against the `.cxx`).
    - Overloads that differ only in the out-handle type are told apart by the R-COLLISION suffix (`GeomTools.Read_s__Geom_Curve`, `Read_s__Geom2d_Curve`, `Read_s__Geom_Surface`).

- **Python**

    - An **out-parameter** like `double&`: dropped from the signature, returned (`C, S, First, Last = CurveOnSurface(E, L)`).

- **Python examples**

    ```python
    import io
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.GC import GC_MakeSegment
    from nanocct.GeomLib import GeomLib
    from nanocct.GeomTools import GeomTools
    from nanocct.gp import gp_Pnt
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopLoc import TopLoc_Location
    from nanocct import TopoDS

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    edge = TopoDS.Edge(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_EDGE).Current())
    C, S, First, Last = BRep_Tool.CurveOnSurface_s(edge, TopLoc_Location())
    assert C is not None and S is not None and Last > First

    segment = GC_MakeSegment(gp_Pnt(0, 0, 0), gp_Pnt(1, 0, 0)).Value()
    curve = GeomTools.Read_s__Geom_Curve(io.StringIO(GeomTools.Write_s(segment)))
    assert (curve.FirstParameter(), curve.LastParameter()) == (0.0, 1.0)

    extended = GeomLib.ExtendCurveToPoint_s(segment, gp_Pnt(2, 0, 0), 1, True)   # Curve read, the result returned
    assert extended.EndPoint().X() == 2.0 and segment.EndPoint().X() == 1.0
    ```
### R-HANDLE

- **C++ Idiom**

    `handle<T>` return; `handle<T>` parameter

- **OCCT examples**

    - `static occ::handle<Geom_Surface> BRep_Tool::Surface(const TopoDS_Face& F)` (a box face's surface is a `Geom_Plane`)
    - `occ::handle<Geom_Geometry> Geom_Line::Copy() const final`
    - `const occ::handle<XSControl_Controller>& XSControl_WorkSession::NormAdaptor() const` (null until a controller is set)
    - `void TopoDS_Shape::TShape(const occ::handle<TopoDS_TShape>& theTShape)` (a parameter)

- **Rule**

    - A caster.

- **Python**

    - Most-derived registered type.
    - Null → `None`.
    - A parameter accepts `None` (`nb::arg(...).none()`, 5.2).

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.Geom import Geom_Line, Geom_Plane
    from nanocct.gp import gp_Dir, gp_Pnt
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct import TopoDS
    from nanocct.XSControl import XSControl_WorkSession

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    face = TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())
    assert type(BRep_Tool.Surface_s(face)) is Geom_Plane                   # declared handle<Geom_Surface>
    assert type(Geom_Line(gp_Pnt(), gp_Dir(1, 0, 0)).Copy()) is Geom_Line  # declared handle<Geom_Geometry>

    assert XSControl_WorkSession().NormAdaptor() is None                   # a null handle

    box.TShape(None)                                                       # a null handle as argument
    assert box.IsNull()
    ```
### R-NCHANDLE

- **C++ Idiom**

    `NCollection_Handle<X>` return or parameter — OCCT's reference-counted owner of a *non*-Transient `X`

- **OCCT examples**

    `StepVisual_TessellatedGeometricSet::Items()`/`Init`, `StepVisual_TessellatedCurveSet::Curves()`/`Init`, `StepVisual_RepositionedTessellatedGeometricSet::Init` — the only 5 public signatures:

    - `NCollection_Handle<NCollection_Array1<occ::handle<StepVisual_TessellatedItem>>> StepVisual_TessellatedGeometricSet::Items() const`
    - `void StepVisual_TessellatedGeometricSet::Init(const occ::handle<TCollection_HAsciiString>& theName, const NCollection_Handle<NCollection_Array1<occ::handle<StepVisual_TessellatedItem>>>& theItems)`
    - `NCollection_Handle<NCollection_DynamicArray<occ::handle<NCollection_HSequence<int>>>> StepVisual_TessellatedCurveSet::Curves() const`
    - `void StepVisual_TessellatedCurveSet::Init(const occ::handle<TCollection_HAsciiString>& theName, const occ::handle<StepVisual_CoordinatesList>& theCoordList, const NCollection_Handle<NCollection_DynamicArray<occ::handle<NCollection_HSequence<int>>>>& theCurves)`
    - `void StepVisual_RepositionedTessellatedGeometricSet::Init(const occ::handle<TCollection_HAsciiString>& theName, const NCollection_Handle<NCollection_Array1<occ::handle<StepVisual_TessellatedItem>>>& theItems, const occ::handle<StepGeom_Axis2Placement3d>& theLocation)`

- **Rule**

    - The handle `delete`s what it holds and a Python-created `X` is owned by Python, so a parameter cannot share it: after `Init(…, items)` later edits to `items` do not reach the entity, edits through `Items()` do.
    - Only the array structure is copied, the elements are handles and stay shared.
    - `get()` on a null handle dereferences null (`NCollection_Handle.hxx`), so `IsNull()` is asked first.

- **Python**

    - Transparent, like R-HANDLE: a result is the bound `X`, **shared** with its owner (edits reach the entity) and kept alive by a heap copy of the handle (`keep_alive`), a null handle is `None`.
    - A parameter takes an `X` or `None` and **copies** the `X` into a new handle (caster in `nanocct_casters.h`; the generator treats it like `handle`: `.none()`, class behind it = `X`, never instantiated as a class).

- **Python examples**

    ```python
    import gc
    from nanocct.NCollection import NCollection_Array1
    from nanocct.StepVisual import StepVisual_TessellatedGeometricSet, StepVisual_TessellatedItem
    from nanocct.TCollection import TCollection_HAsciiString

    entity = StepVisual_TessellatedGeometricSet()
    assert entity.Items() is None                     # a null handle
    first, second = StepVisual_TessellatedItem(), StepVisual_TessellatedItem()
    items = NCollection_Array1[StepVisual_TessellatedItem](1, 1)
    items.SetValue(1, first)
    entity.Init(TCollection_HAsciiString("set"), items)
    items.SetValue(1, second)
    assert entity.Items().Value(1) is first           # Init took a copy of the array
    shared = entity.Items()
    shared.SetValue(1, second)
    assert entity.Items().Value(1) is second          # the result is the entity's own array
    del entity
    gc.collect()
    assert shared.Value(1) is second                  # kept alive by its copy of the handle
    ```
### R-REFWRAP

- **C++ Idiom**

    `std::reference_wrapper<T>` result

- **OCCT examples**

    `NCollection_FlatMap::Contained()` → `std::optional<std::reference_wrapper<const K>>`, `NCollection_FlatDataMap::Contained()` → an optional pair of them; 5<!-- count: refwrap --> members, all BRepGraph maps:

    - `std::optional<std::reference_wrapper<const TheKeyType>> NCollection_FlatMap::Contained(const TheKeyType& theKey) const`
    - `std::optional<std::pair<std::reference_wrapper<const TheKeyType>, std::reference_wrapper<TheItemType>>> NCollection_FlatDataMap::Contained(const TheKeyType& theKey)` (a mutable value)

- **Rule**

    - nanobind has no caster for it (the members would raise `TypeError`).
    - Results only, no OCCT parameter takes one.

- **Python**

    - A `const T` is returned as a **copy**.
    - A mutable `T` is returned as a reference into its owner that keeps the owner alive (`reference_internal`): edits reach the map as in C++ (caster in `nanocct_casters.h`).

- **Python examples**

    ```python
    import gc
    from nanocct.BRepGraph import BRepGraph_NodeId
    from nanocct.BRepGraph import NCollection_FlatMap__BRepGraph_NodeId__NCollection_DefaultHasher__BRepGraph_NodeId as NodeSet
    from nanocct.BRepGraphInc import BRepGraphInc_Storage
    from nanocct.BRepGraphInc import (
        NCollection_FlatDataMap__BRepGraph_NodeId__BRepGraphInc_Storage_CachedShape__NCollection_DefaultHasher__BRepGraph_NodeId as CacheMap)

    key = BRepGraph_NodeId(BRepGraph_NodeId.Kind.Face, 3)
    nodes = NodeSet()
    nodes.Add(key)
    assert nodes.Contained(key) == key                # const K: a copy
    assert nodes.Contained(BRepGraph_NodeId(BRepGraph_NodeId.Kind.Face, 99)) is None

    cache = CacheMap()
    cache.Bind(key, BRepGraphInc_Storage.CachedShape())
    stored_key, value = cache.Contained(key)
    value.StoredSubtreeGen = 7                        # a mutable reference: the edit reaches the map
    assert cache.Find(key).StoredSubtreeGen == 7
    del cache
    gc.collect()
    assert value.StoredSubtreeGen == 7                # and the value keeps the map alive
    ```
### R-NULL

- **C++ Idiom**

    OCCT undefined behaviour on null input

- **OCCT examples**

    `BRep_Tool::Surface(aNullFace)` dereferences the null `TShape`, `BRep_Tool.cxx:125`; likewise `Curve`, `Pnt`, `Triangulation`:

    - `static occ::handle<Geom_Surface> BRep_Tool::Surface(const TopoDS_Face& F)` (`BRep_Tool.cxx:124-125`: `const BRep_TFace* TF = static_cast<const BRep_TFace*>(F.TShape().get());` then `TF->Surface()`)
    - `static occ::handle<Geom_Curve> BRep_Tool::Curve(const TopoDS_Edge& E, double& First, double& Last)`
    - `static gp_Pnt BRep_Tool::Pnt(const TopoDS_Vertex& V)`
    - `static const occ::handle<Poly_Triangulation>& BRep_Tool::Triangulation(const TopoDS_Face& theFace, TopLoc_Location& theLocation, const Poly_MeshPurpose theMeshPurpose = Poly_MeshPurpose_NONE)`

- **Rule**

    - Guards would be a hand-maintained list that hides the OCCT contract.
    - Callers check `IsNull()` as in C++ (build123d does).
    - Revisit if it bites in practice.

- **Python**

    - **Faithful**: the process crashes as it does in C++.
    - No guards are inserted.

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct import TopoDS
    from nanocct.TopoDS import TopoDS_Face

    def surface_of(face):
        if face.IsNull():                             # checked first, as in C++: OCCT would dereference the null TShape
            return None
        return BRep_Tool.Surface_s(face)

    assert surface_of(TopoDS_Face()) is None
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    assert surface_of(TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())) is not None
    ```
### R-RESULT

#### Case 1: `T*` / `T&` return, T Transient

- **C++ Idiom**

    `T*` / `T&` return, `T` a `Standard_Transient` descendant

- **OCCT examples**

    - `const GeomAdaptor_Curve& GeomAdaptor_TransformedCurve::Curve() const` (inherited by `BRepAdaptor_Curve`: a member held by value)
    - `const LDOM_MemManager& LDOM_MemManager::Self() const` (returns `*this`)
    - `Storage_BaseDriver& FSD_File::PutInteger(const int aValue) override` (returns `*this` for chaining)

- **Rule**

    - Never let nanobind own a Transient.
    - Without the refcount-0 case the last Python reference would `delete` a member (*"pointer being freed was not allocated"*; 71<!-- count: result-refcount0 --> call sites, OCCT 8.0.1).
    - A plain `keep_alive<0, 1>` would make a method returning `*this` (`LDOM_MemManager::Self()`, `FSD_File::PutInteger()`, …) keep itself alive for ever: nanobind 3.1.0's `keep_alive_py` has no nurse == patient check, and the cycle is invisible to the garbage collector (`tests/test_lifetime.py`).

- **Python**

    - Wrapped in `handle<T>` (same Python object as before).
    - A `T&` whose reference count is **0** at return is not handle-owned — a member held by value (`BRepAdaptor_Curve::Curve()` → its `GeomAdaptor_Curve`) or static storage — so it gets one permanent reference and, for methods, the owner is kept alive as long as the result — `keep_alive<0, 1>` except when the result is `self` (`nanocct::KeepOwnerUnlessSelf`, `nanocct_call_policies.h`).

- **Python examples**

    ```python
    import gc
    from nanocct.BRepAdaptor import BRepAdaptor_Curve
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
    from nanocct.gp import gp_Pnt
    from nanocct.LDOM import LDOM_MemManager

    adaptor = BRepAdaptor_Curve(BRepBuilderAPI_MakeEdge(gp_Pnt(0, 0, 0), gp_Pnt(1, 0, 0)).Edge())
    curve = adaptor.Curve()          # the GeomAdaptor_Curve member, kept alive by its owner
    del adaptor
    gc.collect()
    assert (curve.FirstParameter(), curve.LastParameter()) == (0.0, 1.0)

    manager = LDOM_MemManager(16)
    assert manager.Self() is manager  # *this: the same Python object, no self-keep-alive
    ```

#### Case 2: `T` return by value, T Transient

- **C++ Idiom**

    `T` return by value, `T` a `Standard_Transient` descendant

- **OCCT examples**

    - `Geom2dAdaptor_Curve Geom2dGcc_QualifiedCurve::Qualified() const`

- **Rule**

    - A nanobind-owned copy has reference count 0, and the first `handle<T>` parameter it meets deletes memory nanobind owns when that handle goes (`Geom2dGcc_QualifiedCurve::Qualified()` into `Adaptor2d_OffsetCurve`; 12<!-- count: result-value-transient --> sites, `tests/test_lifetime.py`).

- **Python**

    - Moved into `handle<T>(new T(...))`, as every Transient constructor does; methods, free functions and R-ITER getters alike.
    - The handle caster refuses a Transient whose reference count is 0 (a TypeError), whatever path produced it.

- **Python examples**

    ```python
    import gc
    from nanocct.Adaptor2d import Adaptor2d_OffsetCurve
    from nanocct.GccEnt import GccEnt_Position
    from nanocct.Geom2d import Geom2d_Circle
    from nanocct.Geom2dAdaptor import Geom2dAdaptor_Curve
    from nanocct.Geom2dGcc import Geom2dGcc_QualifiedCurve
    from nanocct.gp import gp_Ax2d, gp_Circ2d, gp_Dir2d, gp_Pnt2d

    circle = Geom2d_Circle(gp_Circ2d(gp_Ax2d(gp_Pnt2d(0, 0), gp_Dir2d(1, 0)), 1.0))
    qualified = Geom2dGcc_QualifiedCurve(Geom2dAdaptor_Curve(circle), GccEnt_Position.GccEnt_unqualified)
    adaptor = qualified.Qualified()   # a new Geom2dAdaptor_Curve, owned by a handle
    assert adaptor.GetRefCount() == 1

    offset = Adaptor2d_OffsetCurve(adaptor, 0.5)   # the handle parameter shares it
    del adaptor
    gc.collect()
    assert offset.Value(0.0).X() == 1.5
    ```

#### Case 3: `T*` return, other class

- **C++ Idiom**

    `T*` return, `T` not a Transient

- **OCCT examples**

    - `const NCollection_Array1<double>* Geom_BSplineCurve::Weights() const`
    - `const BOPAlgo_PBuilder& BRepAlgoAPI_BuilderAlgo::Builder() const` (`BOPAlgo_PBuilder` = `BOPAlgo_Builder*`)
    - `BOPDS_PDS BOPAlgo_Builder::PDS()` (`BOPDS_PDS` = `BOPDS_DS*`)

- **Rule**

    - The result points into its object: `Geom_BSplineCurve.Weights()`, `BRepAlgoAPI_BuilderAlgo.Builder()`, `BOPAlgo_Builder.PDS()` would dangle once the owner is collected (a silent read of freed memory or a segfault, `tests/test_lifetime.py`).
    - The keep-alives of R-CTOR-KEEP and R-METHOD-KEEP make the rest of the chain hold: where the pointee belongs to a third object, the owner keeps that object (`BOPAlgo_Builder::PPaveFiller()`: the builder keeps the filler through `PerformWithFiller`'s slot).
    - A static method's or free function's pointer result still dangles once its true owner is collected.

- **Python**

    - `rv_policy::reference_internal` for a method: the result keeps its object alive (`keep_alive<0, 1>` on a new wrapper; nanobind hands back an existing wrapper unchanged, `self` included, so `return this` cannot keep itself alive).
    - `rv_policy::reference` for a static method or a free function, which have no object to tie it to.

- **Python examples**

    ```python
    import gc
    from nanocct.GC import GC_MakeCircle
    from nanocct.GeomConvert import GeomConvert
    from nanocct.gp import gp_Pnt

    circle = GC_MakeCircle(gp_Pnt(0, 0, 0), gp_Pnt(1, 1, 0), gp_Pnt(2, 0, 0)).Value()
    bspline = GeomConvert.CurveToBSplineCurve_s(circle)
    weights = bspline.Weights()       # points into the curve, keeps the curve alive
    del bspline
    gc.collect()
    assert weights[weights.Lower()] == 1.0
    ```

#### Case 4: `T&` (mutable) return, other class

- **C++ Idiom**

    `T&` (mutable) return, `T` not a Transient

- **OCCT examples**

    - `gp_XYZ& gp_Pnt::ChangeCoord()`
    - `static BRepMesh_DiscretFactory& BRepMesh_DiscretFactory::Get()` (a singleton)
    - `TopoDS_Vertex& TopoDS::Vertex(TopoDS_Shape& theShape)` (a free function)

- **Rule**

    - In-place edits via `ChangeXxx()`.
    - A free function has no `self` to tie the reference to. The mutable `TopoDS::Xxx(TopoDS_Shape&)` overloads are the ones bound (R-CONST-TWIN drops their `const&` twins), so their results are copies.

- **Python**

    - `rv_policy::reference_internal` for methods.
    - `rv_policy::reference` for static methods (`BRepMesh_DiscretFactory::Get()`, a singleton: `reference_internal` needs a `self`, and every call would fail with *"Unable to convert function return value"*).
    - **Copied** for free functions (`TopoDS::Vertex(TopoDS_Shape&)`).

- **Python examples**

    ```python
    from nanocct.BRepMesh import BRepMesh_DiscretFactory
    from nanocct.gp import gp_Pnt

    point = gp_Pnt(1, 2, 3)
    point.ChangeCoord().SetX(5.0)     # edits the point in place
    assert point.X() == 5.0

    assert BRepMesh_DiscretFactory.Get_s() is BRepMesh_DiscretFactory.Get_s()   # the singleton itself
    ```

#### Case 5: `const T&` return, other class

- **C++ Idiom**

    `const T&` return, `T` not a Transient

- **OCCT examples**

    - `const gp_XYZ& gp_Pnt::XYZ() const` (copy-constructible: copied)
    - `const Extrema_ExtCC& GeomAPI_ExtremaCurveCurve::Extrema() const` (not copyable: by reference)

- **Rule**

    - nanobind's copy of a class without a usable copy constructor is no error but an abort of the whole process (*"Critical nanobind error"*): `GeomAPI_ExtremaCurveCurve::Extrema()` returns `const Extrema_ExtCC&`, and `Extrema_ExtCC` deletes its copy constructor in the non-const form `T(T&)`; `Extrema_ExtPS` holds a non-copyable `Extrema_GenExtPS` by value.
    - The compiler knows exactly which classes cannot be copied -- a deleted `T(const T&)` or `T(T&)`, a non-copyable member or base -- where the header would have to be interpreted; nanobind 3.1 takes the policy as a compile-time tag type, hence a type alias.
    - A copy that drops state is not visible in the header: the list comes from reading every OCCT copy constructor that sets a member to a constant; caches recomputed on demand and containers that null their pointers before a deep copy are fine. `Geom2dAPI_InterCurveCurve::Intersector()`'s copy would raise `StdFail_NotDone` on every accessor.

- **Python**

    - Copied (`rv_policy::copy`) when `T` is copy-constructible.
    - Otherwise returned by reference -- `reference_internal` for a method (the result keeps its owner alive), `reference` for a static method or free function (no owner).
    - `nanocct::cref_policy<R, HasOwner>` (`nanocct_call_policies.h`) picks the policy at compile time from `std::is_copy_constructible`.
    - Also by reference: an owner (R-COPY: its copy would share what its destructor frees, decided by the generator), and a result that names a class of `overrides.toml [not_value_copy]`, itself or as a container element -- classes whose copy constructor drops state (`IntRes2d_Intersection`/`Geom2dInt_GInter`: `done = false`, `Intf_SectionLine`: `closed = false`, `IntTools_CommonPrt`: `myAllNullFlag = false`).

- **Python examples**

    ```python
    import gc
    from nanocct.GC import GC_MakeSegment
    from nanocct.GeomAPI import GeomAPI_ExtremaCurveCurve
    from nanocct.gp import gp_Pnt

    point = gp_Pnt(1, 2, 3)
    xyz = point.XYZ()                 # a copy
    xyz.SetX(9.0)
    assert point.X() == 1.0

    api = GeomAPI_ExtremaCurveCurve(GC_MakeSegment(gp_Pnt(0, 0, 0), gp_Pnt(1, 0, 0)).Value(),
                                    GC_MakeSegment(gp_Pnt(0, 1, 1), gp_Pnt(1, 1, 1)).Value())
    extrema = api.Extrema()           # Extrema_ExtCC cannot be copied: a reference that keeps api alive
    del api
    gc.collect()
    assert extrema.IsDone() and extrema.NbExt() == 1
    ```
### R-PTR-REF

- **C++ Idiom**

    `T*&` or `T* const&` return

- **OCCT examples**

    `BRepAlgoAPI_BuilderAlgo::Builder()`, `DSFiller()`:

    - `const BOPAlgo_PBuilder& BRepAlgoAPI_BuilderAlgo::Builder() const` (`BOPAlgo_PBuilder` = `BOPAlgo_Builder*`: a `BOPAlgo_Builder* const&`)
    - `const BOPAlgo_PPaveFiller& BRepAlgoAPI_BuilderAlgo::DSFiller() const` (`BOPAlgo_PPaveFiller` = `BOPAlgo_PaveFiller*`)
    - `virtual const IMeshData::IEdgePtr& IMeshData_Wire::GetEdge(const int theIndex) const = 0` (`IMeshData::IEdgePtr` = `IMeshData_Edge*`, a Transient)
    - `NCollection_ListNode*& NCollection_ListNode::Next()` (a mutable `T*&`)

- **Rule**

    - nanobind cannot return a reference to a pointer.

- **Python**

    - The pointer, copied out by a lambda: `rv_policy::reference_internal` for a class (the result keeps its owner alive, as for any `T*` result of a method, R-RESULT; `reference` for a static method), a handle for a Transient.

- **Python examples**

    ```python
    import gc
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Fuse
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.gp import gp_Pnt

    fuse = BRepAlgoAPI_Fuse(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape(),
                            BRepPrimAPI_MakeBox(gp_Pnt(0.5, 0.5, 0.5), 1.0, 1.0, 1.0).Shape())
    builder = fuse.Builder()          # the BOPAlgo_Builder* the fuse owns, tied to the fuse
    filler = fuse.DSFiller()
    del fuse
    gc.collect()
    assert type(builder).__name__ == "BOPAlgo_BOP" and builder.Arguments().Size() == 1
    assert type(filler).__name__ == "BOPAlgo_PaveFiller"
    ```

    ```python
    from nanocct.BRepMesh import BRepMesh_ModelBuilder
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.IMeshTools import IMeshTools_Parameters

    model = BRepMesh_ModelBuilder().Perform(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), IMeshTools_Parameters())
    wire = model.GetFace(0).GetWire(0)
    edge = wire.GetEdge(0)            # IMeshData_Edge* const&: a handle (the model holds the other reference)
    assert edge.GetRefCount() == 2 and wire.EdgesNb() == 4
    del edge, wire                    # mesh data lives in the model's allocator: released before the model
    ```
### R-PTR-INCOMPLETE

- **C++ Idiom**

    `T*` or `T&` where `T` is only forward-declared in the package's translation unit

- **OCCT examples**

    `BOPDS_DS* BOPAlgo_Builder::PDS()`:

    - `BOPDS_PDS BOPAlgo_Builder::PDS()` (`BOPDS_PDS.hxx` only declares `class BOPDS_DS;` and `typedef BOPDS_DS* BOPDS_PDS;`; `BOPDS_DS.hxx` exists: bound)
    - `static clocale_t Standard_CLocaleSentry::GetCLocale()` (`clocale_t` = `locale_t`: skipped)
    - `const AVStream& Media_FormatContext::Stream(unsigned int theIndex) const` (`struct AVStream;`, `Media_FormatContext.hxx:24`: skipped)
    - `static int64_t Media_FormatContext::SecondsToUnits(const AVRational& theTimeBase, double theTimeSeconds)` (skipped; the `SecondsToUnits(double theTimeSeconds)` overload is bound)
    - `virtual bool Xw_Window::ProcessMessage(Aspect_WindowInputListener& theListener, XEvent& theMsg)` (skipped)

- **Rule**

    - `Standard_CLocaleSentry::GetCLocale()` (`locale_t`, no header), `const AVStream&`/`const AVRational&` (FFmpeg, `Media_*`) and `XEvent&` (X11, `Xw_Window::ProcessMessage`) stay out — references included (they would compile to `typeid` of an incomplete type).

- **Python**

    - Bound when `T.hxx` exists in the OCCT install: the emitter includes it (the class behind every parameter/result type is an include candidate, 6.2).

- **Python examples**

    ```python
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Fuse
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.gp import gp_Pnt
    from nanocct.Media import Media_FormatContext

    fuse = BRepAlgoAPI_Fuse(BRepPrimAPI_MakeBox(1.0, 1.0, 1.0).Shape(),
                            BRepPrimAPI_MakeBox(gp_Pnt(0.5, 0.5, 0.5), 1.0, 1.0, 1.0).Shape())
    ds = fuse.Builder().PDS()         # BOPDS_DS*: only forward-declared, but BOPDS_DS.hxx exists
    assert type(ds).__name__ == "BOPDS_DS" and ds.NbShapes() > ds.NbSourceShapes()

    assert not hasattr(Media_FormatContext, "Stream")                         # const AVStream&: no header
    assert "theTimeBase" not in Media_FormatContext.SecondsToUnits_s.__doc__   # only the (double) overload
    ```
### R-REF-PRIMITIVE

- **C++ Idiom**

    Non-const method returning a mutable reference to a primitive

- **OCCT examples**

    `double& math_Matrix::Value(i, j)`, `double& gp_XYZ::ChangeCoord(i)`, `bool& BRepTools_ReShape::ModeConsiderLocation()`:

    - `double& math_Matrix::Value(const int Row, const int Col)`
    - `double& gp_XYZ::ChangeCoord(const int theIndex)`
    - `virtual bool& BRepTools_ReShape::ModeConsiderLocation()`
    - `double& math_Matrix::operator()(const int Row, const int Col)` (an operator: `__setitem__`)

- **Rule**

    - Python cannot hold a reference to a `double`.
    - The setter docstrings say "Python addition".

- **Python**

    - Getter under the C++ name (returns the value) plus a **Python addition** setter: `Set<Name>` with a `Change` prefix dropped (`SetValue(i, j, v)`, `SetModeConsiderLocation(b)`) unless OCCT already has a method of that name (`gp_XYZ::SetCoord`), and for `operator()`/`operator[]` `__setitem__` (+ `__getitem__`) with a tuple index for several arguments (`a[(2, 1)] = 7.0`).

- **Python examples**

    ```python
    from nanocct.BRepTools import BRepTools_ReShape
    from nanocct.gp import gp_XYZ
    from nanocct.math import math_Matrix

    matrix = math_Matrix(1, 2, 1, 2, 0.0)
    matrix.SetValue(2, 1, 7.0)        # the setter of double& Value(i, j)
    assert matrix.Value(2, 1) == 7.0
    matrix[(1, 2)] = 3.0              # operator()(i, j): a tuple index
    assert matrix[(1, 2)] == 3.0 and matrix(1, 2) == 3.0
    assert "Python addition" in matrix.SetValue.__doc__

    xyz = gp_XYZ(1.0, 2.0, 3.0)
    assert xyz.ChangeCoord(1) == 1.0 and not hasattr(xyz, "SetChangeCoord")   # SetCoord exists in OCCT
    xyz.SetCoord(1, 5.0)
    assert xyz.X() == 5.0

    reshape = BRepTools_ReShape()
    reshape.SetModeConsiderLocation(True)
    assert reshape.ModeConsiderLocation() is True
    ```
### R-DEFAULT

- **C++ Idiom**

    Default argument

- **OCCT examples**

    - `TCollection_AsciiString::TCollection_AsciiString(const TCollection_ExtendedString& theExtendedString, const char theReplaceNonAscii = 0)` (a `char` written as `0`)
    - `NCollection_IncAllocator::NCollection_IncAllocator(const size_t theBlockSize = THE_DEFAULT_BLOCK_SIZE)` (a static member of the class, unqualified)
    - `XSAlgo_ShapeProcessor::XSAlgo_ShapeProcessor(const ParameterMap& theParameters, const DE_ShapeFixParameters& theShapeFixParameters = {})` (braced)

- **Rule**

    - The expression is emitted outside the class scope.
    - `static_cast` from a braced-init-list is not C++ (`error: expected expression`).

- **Python**

    - Cast to `std::decay_t<ParamType>` (a `char` default written as `0` becomes a 1-char `str`).
    - Unqualified static members/enumerators of the class are qualified (`NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE`).
    - A **braced** default (`= {}`: `XSAlgo_ShapeProcessor(…, const DE_ShapeFixParameters& = {})`, the `ParameterMap` of `SetShapeFixParameters`, 8<!-- count: default-braced --> sites: 4 in `TKXSBase`, 2 each in `TKDEIGES` and `TKDESTEP`) is **list-initialised** `std::decay_t<T>{ }` instead.

- **Python examples**

    ```python
    from nanocct.NCollection import NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString as ParameterMap
    from nanocct.NCollection import NCollection_IncAllocator
    from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString
    from nanocct.XSAlgo import XSAlgo_ShapeProcessor

    assert "theReplaceNonAscii: str = '\\x00'" in TCollection_AsciiString.__init__.__doc__   # char 0 -> a 1-char str
    assert TCollection_AsciiString(TCollection_ExtendedString("abc")).ToCString() == "abc"

    assert "theBlockSize: int = 12288" in NCollection_IncAllocator.__init__.__doc__   # THE_DEFAULT_BLOCK_SIZE
    NCollection_IncAllocator()

    processor = XSAlgo_ShapeProcessor(ParameterMap())    # theShapeFixParameters = {}
    assert type(processor).__name__ == "XSAlgo_ShapeProcessor"
    ```
### R-DEFAULT-QUAL

#### Case 1: nested type, unqualified

- **C++ Idiom**

    Default argument naming a nested type unqualified

- **OCCT examples**

    `= Options()` inside `BRepGraphInc_Populate`:

    - `[[nodiscard]] static BuildStatus BRepGraphInc_Populate::Perform(BRepGraph& theGraph, const TopoDS_Shape& theShape, bool theParallel, const Options& theOptions = Options())`
    - `[[nodiscard]] static BuildStatus BRepGraphInc_Populate::Append(BRepGraph& theGraph, const TopoDS_Shape& theShape, bool theParallel, const Options& theOptions = Options())`

- **Rule**

    - Same mechanism as the namespace case.

- **Python**

    - Qualified from the AST type reference.

- **Python examples**

    ```python
    from nanocct.BRepGraph import BRepGraph
    from nanocct.BRepGraphInc import BRepGraphInc_Populate
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox

    graph = BRepGraph()
    status = BRepGraphInc_Populate.Perform_s(graph, BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)   # = Options()
    assert status == BRepGraphInc_Populate.BuildStatus.Success
    ```

#### Case 2: enumerator or static member of an enclosing or base class, unqualified

- **C++ Idiom**

    Default argument naming an enumerator or static member of an *enclosing* or *base* class unqualified

- **OCCT examples**

    `= IterationFilter_None` inside `Font_TextFormatter::Iterator` and `Graphic3d_LightSet::Iterator`:

    - `Font_TextFormatter::Iterator::Iterator(const Font_TextFormatter& theFormatter, IterationFilter theFilter = IterationFilter_None)`
    - `Graphic3d_LightSet::Iterator::Iterator(const Graphic3d_LightSet& theSet, IterationFilter theFilter = IterationFilter_None)`

- **Rule**

    - The nested class sees the outer class's names, the emitted expression does not.

- **Python**

    - Qualified through the class chain of the referenced declaration (`Font_TextFormatter::IterationFilter_None`).

- **Python examples**

    ```python
    from nanocct.Graphic3d import Graphic3d_CLight, Graphic3d_LightSet, Graphic3d_TypeOfLightSource

    lights = Graphic3d_LightSet()
    lights.Add(Graphic3d_CLight(Graphic3d_TypeOfLightSource.Graphic3d_TypeOfLightSource_Ambient))
    assert Graphic3d_LightSet.Iterator(lights).More()       # theFilter = IterationFilter_None
    assert not Graphic3d_LightSet.Iterator(lights, Graphic3d_LightSet.IterationFilter_ExcludeAmbient).More()
    ```

#### Case 3: name from a namespace, unqualified

- **C++ Idiom**

    Default argument naming something from a namespace unqualified

- **OCCT examples**

    `= LeastSquaresMethod::QR` inside `namespace MathLin`, `= THE_2PI` via `using namespace MathUtils`:

    - `LeastSquaresResult MathLin::LeastSquares(const math_Matrix& theA, const math_Vector& theB, LeastSquaresMethod theMethod = LeastSquaresMethod::QR, double theTolerance = 1.0e-15)`
    - `TrigResult MathRoot::Trigonometric(double theA, double theB, double theC, double theD, double theE, double theInfBound = 0.0, double theSupBound = THE_2PI, double theEps = 1.5e-12)`

- **Rule**

    - The expression is emitted outside the namespace.

- **Python**

    - Qualified from the AST reference (`MathLin::LeastSquaresMethod::QR`, `MathUtils::THE_2PI`).

- **Python examples**

    ```python
    from math import pi
    from nanocct import MathLin, MathRoot

    assert "theMethod: nanocct.MathLin.LeastSquaresMethod = LeastSquaresMethod.QR" in MathLin.LeastSquares.__doc__
    roots = MathRoot.Trigonometric(0.0, 0.0, 0.0, 1.0, 0.0)   # sin(x) = 0 on [0, theSupBound = THE_2PI]
    assert roots.NbRoots == 2 and roots.Roots[0] == 0.0 and abs(roots.Roots[1] - pi) < 1e-12
    ```
### R-DEFAULT-UNBOUND

- **C++ Idiom**

    Default argument of a type no binding knows

- **OCCT examples**

    None in OCCT 8.0.1: no generator report has a "default argument of unbound type" line. `BRepGraph_OccurrenceId` (a nested class template instantiation, `using BRepGraph_OccurrenceId = BRepGraph_NodeId::Typed<BRepGraph_NodeId::Kind::Occurrence>`, `BRepGraph_NodeId.hxx:415`) is bound, and so is the member whose default names it:

    - `[[nodiscard]] BRepGraph_OccurrenceId BRepGraph::EditorView::ProductOps::Append(const BRepGraph_ProductId theParentProduct, const BRepGraph_ProductId theReferencedProduct, const TopLoc_Location& thePlacement, const BRepGraph_OccurrenceId theParentOccurrence = BRepGraph_OccurrenceId(), BRepGraph_OccurrenceRefId* theOutOccurrenceRefId = nullptr)` (a `nullptr` default as well)

- **Rule**

    - nanobind converts defaults to Python at `.def` time → `std::bad_cast` aborts the module import.
    - `nullptr` defaults are fine (→ `None`).

- **Python**

    - Member skipped, reported.

- **Python examples**

    ```python
    from nanocct.BRepGraph import BRepGraph

    append = BRepGraph.EditorView.ProductOps.Append.__doc__.splitlines()[0]
    assert "theParentOccurrence: nanocct.BRepGraph.BRepGraph_OccurrenceId = " in append        # a bound type: kept
    assert "theOutOccurrenceRefId: nanocct.BRepGraph.BRepGraph_OccurrenceRefId | None = None" in append   # nullptr
    ```
### R-CHAR

- **C++ Idiom**

    `char` parameter

- **OCCT examples**

    - `TCollection_AsciiString::TCollection_AsciiString(const int theLength, const char theFiller)`
    - `void TCollection_AsciiString::ChangeAll(const char theChar, const char theNewChar, const bool theCaseSensitive = true)`
    - `void TCollection_AsciiString::Center(const int theWidth, const char theFiller)`
    - `static bool Interface_Static::Init(const char* const family, const char* const name, const char type, const char* const init = "")`

- **Rule**

    - nanobind convention.

- **Python**

    - 1-character `str` whose UTF-8 form is one byte (ASCII): `"é"` is a `TypeError`, and a `char` result of 0x80 or more raises `UnicodeDecodeError`.

- **Python examples**

    ```python
    from nanocct.TCollection import TCollection_AsciiString

    text = TCollection_AsciiString(3, "x")        # const char theFiller
    assert text.ToCString() == "xxx"
    text.ChangeAll("x", "y")
    assert text.ToCString() == "yyy"
    for bad in ("xy", "é"):                        # not one character, not ASCII
        try:
            text.ChangeAll(bad, "z")
        except TypeError:
            pass
        else:
            raise AssertionError(f"{bad!r} must be rejected")
    ```
### R-CHAR16

- **C++ Idiom**

    `char16_t` / `const char16_t*`; `char32_t`

- **OCCT examples**

    `Standard_ExtString` (= `const char16_t*`), the UTF-16 API of `TCollection_ExtendedString`; `Standard_Utf32Char` (= `char32_t`): the code-point API of `Font_FTFont::AdvanceX/HasSymbol/RenderGlyph`, `Font_TextFormatter::Iterator::Symbol`:

    - `const char16_t* TCollection_ExtendedString::ToExtString() const`
    - `char16_t TCollection_ExtendedString::Value(const int theWhere) const`
    - `void TCollection_ExtendedString::SetValue(const int theWhere, const char16_t theWhat)`
    - `static bool Font_FTFont::IsCharFromCJK(char32_t theUChar)`
    - `char32_t Font_TextFormatter::Iterator::Symbol() const`

- **Rule**

    - `ToExtString()` round-trips.
    - `wchar_t` (only in hasher specialisations) is not cast.
    - `PyUnicode_FromKindAndData` is not in the limited API.

- **Python**

    - `str` (1 character / UTF-16 string), casters in `nanocct_casters.h` (stable-ABI `PyUnicode_AsUTF16String` / `PyUnicode_DecodeUTF16`, `PyUnicode_ReadChar` / `PyUnicode_DecodeUTF32`).
    - A `char32_t` is a 1-character `str` in both directions (`font.HasSymbol("€")`; an `int` is rejected).
    - A `char16_t` is one UTF-16 code unit: a character outside the Basic Multilingual Plane (`"😀"`) is a `TypeError` there.

- **Python examples**

    ```python
    from nanocct.Font import Font_FTFont
    from nanocct.TCollection import TCollection_ExtendedString

    text = TCollection_ExtendedString("Grüße €", True)    # theIsMultiByte: the str arrives as UTF-8
    assert text.ToExtString() == "Grüße €"               # const char16_t* -> str
    assert text.Value(3) == "ü"                          # char16_t -> a 1-character str
    text.SetValue(7, "$")
    assert text.ToExtString() == "Grüße $"

    assert Font_FTFont.IsCharFromCJK_s("漢") and not Font_FTFont.IsCharFromCJK_s("A")   # char32_t
    try:
        Font_FTFont.IsCharFromCJK_s(0x6F22)              # a code point is a str, not an int
    except TypeError:
        pass
    else:
        raise AssertionError("an int must be rejected")
    ```
### R-CSTRING

- **C++ Idiom**

    `const char*`

- **OCCT examples**

    `Standard_CString`:

    - `typedef const char* Standard_CString;` (`Standard_TypeDef.hxx:132`)
    - `const char* TCollection_AsciiString::ToCString() const`
    - `TCollection_AsciiString::TCollection_AsciiString(const char* const theMessage)`
    - `TCollection_ExtendedString::TCollection_ExtendedString(const char* const theString, const bool theIsMultiByte = false)` (UTF-8 in with `theIsMultiByte` set)
    - `TCollection_AsciiString::TCollection_AsciiString(const TCollection_ExtendedString& theExtendedString, const char theReplaceNonAscii = 0)` (UTF-8 out with the default, the `?`-replacement overload with a character)

- **Rule**

    - **Limitation:** `TCollection_AsciiString` holds 8-bit (Latin-1-like) text.
    - `ToCString()` on such content raises `UnicodeDecodeError` in Python (OCCT treats U+0080..U+00FF as representable).
    - Use the `ExtendedString` UTF-8 paths: the `?`-replacement overload replaces only characters above U+00FF, and U+0080..U+00FF stay single bytes (`IsAnAscii`, `Standard_ExtCharacter.hxx:53`), so its `ToCString()` raises as well.

- **Python**

    - `str`, UTF-8.

- **Python examples**

    ```python
    from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString

    assert TCollection_AsciiString("Grüße").ToCString() == "Grüße"        # str in and out, UTF-8
    text = TCollection_ExtendedString("café", True)
    assert TCollection_AsciiString(text).ToCString() == "café"             # the UTF-8 path
    latin = TCollection_AsciiString(text, "?")                             # é (U+00E9) stays the byte 0xE9
    try:
        latin.ToCString()
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError("8-bit content is not UTF-8")
    assert TCollection_AsciiString(TCollection_ExtendedString("a€b", True), "?").ToCString() == "a?b"
    ```
### R-STL

- **C++ Idiom**

    `std::vector/map/set/pair/optional/shared_ptr/function/string_view` of supported types

- **OCCT examples**

    - `std::pair<double, double> BRepMesh_ConeRangeSplitter::GetSplitSteps(const IMeshTools_Parameters& theParameters, std::pair<int, int>& theStepsNb) const` (a non-const reference: an out-parameter)
    - `static std::pair<ShapeProcess::Operation, bool> ShapeProcess::ToOperationFlag(const char* theName)`
    - `std::optional<int> BOPDS_Interf::GetIndexNew() const`
    - `bool TCollection_AsciiString::EndsWith(const std::string_view& theEndString) const`
    - `virtual bool OSD_FileSystem::IsOpenIStream(const std::shared_ptr<std::istream>& theStream) const = 0` (skipped, reported)

- **Rule**

    - `std::shared_ptr<std::istream>`, `std::vector<NestedStruct>` are skipped (reported).

- **Python**

    - Native Python objects via nanobind's STL casters.
    - A **non-const reference** to one (`BRepMesh_ConeRangeSplitter::GetSplitSteps(…, std::pair<int, int>&)`) is an out-parameter like `double&` (R-OUT; suffix type `tuple`/`list`/`dict`/`str`) because the caster hands the callee a temporary. It is the only one in OCCT 8.0.1, and its header does not export it (no `Standard_EXPORT`): bound on macOS and Linux, skipped on Windows (R-UNDEFINED).

- **Python examples**

    ```python
    from nanocct.BOPDS import BOPDS_InterfVV
    from nanocct.OSD import OSD_FileSystem
    from nanocct.TCollection import TCollection_AsciiString

    assert TCollection_AsciiString("model.step").EndsWith(".step")   # const std::string_view& <- str
    interference = BOPDS_InterfVV()
    assert interference.GetIndexNew() is None                       # an empty std::optional<int>
    interference.SetIndexNew(7)
    assert interference.GetIndexNew() == 7
    assert not hasattr(OSD_FileSystem, "IsOpenIStream")             # std::shared_ptr<std::istream>
    ```

    ```python
    from nanocct.ShapeProcess import ShapeProcess

    operation, found = ShapeProcess.ToOperationFlag_s("FixShape")   # std::pair<Operation, bool> -> a tuple
    assert found and operation == ShapeProcess.Operation.FixShape
    assert ShapeProcess.ToOperationFlag_s("NoSuchOperation")[1] is False
    ```
### R-BITSET

- **C++ Idiom**

    `std::bitset<N>` parameter, result or member

- **OCCT examples**

    `ShapeProcess::OperationsFlags` = `std::bitset<ShapeProcess::Operation::Last + 1>`, the only one in scope (`using OperationsFlags = std::bitset<Operation::Last + 1>;`, `ShapeProcess.hxx:74`):

    - `static bool ShapeProcess::Perform(const occ::handle<ShapeProcess_Context>& theContext, const OperationsFlags& theOperations, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `TopoDS_Shape XSAlgo_ShapeProcessor::ProcessShape(const TopoDS_Shape& theShape, const ShapeProcess::OperationsFlags& theOperations, const Message_ProgressRange& theProgress)`
    - `void Transfer_ActorOfTransientProcess::SetProcessingFlags(const ShapeProcess::OperationsFlags& theFlags)`
    - `const XSAlgo_ShapeProcessor::ProcessingFlags& Transfer_ActorOfTransientProcess::GetProcessingFlags() const` (`ProcessingFlags` = `std::pair<ShapeProcess::OperationsFlags, bool>`)

- **Rule**

    - nanobind's arithmetic enums are Python `IntEnum`s, so the enumerators go in as ints and the ints that come back compare and hash equal to them (measured).
    - The caster (`nanocct_casters.h`) takes any iterable of indices — set, frozenset, list, tuple — and rejects `str`, `bytes`, `dict`, a negative index and an index ≥ N, so the name-taking twin stays reachable (`ShapeProcess.Perform_s(context, "sequence")` next to `Perform(context, flags)`).
    - 19<!-- count: bitset --> members in four toolkits (OCCT 8.0.1: `TKXSBase` 8, `TKDESTEP` 6, `TKDEIGES` 4, `TKShHealing` 1).

- **Python**

    - The **set of the indices whose bit is set**: `proc.ProcessShape(shape, {ShapeProcess.FixShape, ShapeProcess.SameParameter}, range)`, and the same set comes back (`{1, 15}`).

- **Python examples**

    ```python
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.DE import DE_ShapeFixParameters
    from nanocct.Message import Message_ProgressRange
    from nanocct.ShapeProcess import ShapeProcess
    from nanocct.Transfer import Transfer_ActorOfTransientProcess
    from nanocct.XSAlgo import XSAlgo_ShapeProcessor

    actor = Transfer_ActorOfTransientProcess()
    actor.SetProcessingFlags({ShapeProcess.FixShape, ShapeProcess.SameParameter})
    flags, used = actor.GetProcessingFlags()
    assert flags == {1, 15} and used is True
    try:
        actor.SetProcessingFlags({99})                # an index >= N
    except TypeError:
        pass
    else:
        raise AssertionError("an index >= N must be rejected")
    processor = XSAlgo_ShapeProcessor(DE_ShapeFixParameters())
    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    assert not processor.ProcessShape(box, {ShapeProcess.FixShape}, Message_ProgressRange()).IsNull()
    assert any("seq: str" in line for line in ShapeProcess.Perform_s.__doc__.splitlines())   # the name-taking twin
    ```
### R-STREAM-OUT

- **C++ Idiom**

    `std::ostream&` (`Standard_OStream&`) parameter

- **OCCT examples**

    `DumpJson`, `Dump`, `Print`, `BRepTools::Write(shape, stream)`:

    - `void gp_Pnt::DumpJson(Standard_OStream& theOStream, int theDepth = -1) const` (also `Dump`, `Print`)
    - `static void BRepTools::Write(const TopoDS_Shape& theShape, Standard_OStream& theStream, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `static void BinTools::Write(const TopoDS_Shape& theShape, Standard_OStream& theStream, const Message_ProgressRange& theRange = Message_ProgressRange())` (a binary package)
    - `bool IGESControl_Writer::Write(Standard_OStream& S, const bool fnes = false)` (a non-void result)
    - `static Standard_OStream& TopAbs::Print(const TopAbs_ShapeEnum theShapeType, Standard_OStream& theStream)` (a returned stream, for chaining)

- **Rule**

    - The out-param rule applied to streams.
    - `str` decoded with `surrogateescape` so a stray non-UTF-8 byte is lossless.
    - **Binary formats are `bytes`**: the packages listed in `overrides.toml [stream] binary_packages` (`BinTools`; `PCDM` and `CDF` — `PCDM_Writer::Write`, `PCDM_Reader::Read`, `CDF_Application::Read`, `PCDM::FileDriverType` carry binary *and* XML OCAF documents, and `bytes` is the superset; `BinLDrivers` & co.) return `bytes` from their `ostream&` parameters (`BinTools.Write_s(shape)` is byte-identical to the file form, tested).
    - Not a file-like target: OCCT's stream APIs are of modest size, and the file-path overloads exist for bulk I/O.

- **Python**

    - Dropped from the signature, the written text is **returned as `str`** (a tuple after a non-void result, like out-params).
    - A returned `Standard_OStream&` (chaining, `TopAbs::Print`) is dropped.

- **Python examples**

    ```python
    from nanocct.BinTools import BinTools
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.BRepTools import BRepTools
    from nanocct.gp import gp_Pnt
    from nanocct.IGESControl import IGESControl_Writer
    from nanocct.TopAbs import TopAbs, TopAbs_ShapeEnum

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    assert gp_Pnt(1, 2, 3).DumpJson() == '"gp_Pnt": [1, 2, 3]'
    assert "CASCADE Topology" in BRepTools.Write_s(box)        # the BREP text
    assert isinstance(BinTools.Write_s(box), bytes)            # a binary package

    writer = IGESControl_Writer()
    writer.AddShape(box)
    ok, iges = writer.Write()                                  # the bool result first, then the text
    assert ok and isinstance(iges, str)

    assert TopAbs.Print_s(TopAbs_ShapeEnum.TopAbs_FACE) == "FACE"   # the chained stream is dropped
    ```
### R-STREAM-IN

- **C++ Idiom**

    `std::istream&` / `const Standard_SStream&` parameter (a non-const `std::stringstream&` the callee may write into is not an input: it is reported as an iostream type; OCCT 8.0.1 has none)

- **OCCT examples**

    `BRepTools::Read(shape, stream, builder)`, `InitFromJson(sstream, pos)`, `GeomTools::Read`:

    - `static void BRepTools::Read(TopoDS_Shape& Sh, Standard_IStream& S, const BRep_Builder& B, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `bool gp_Pnt::InitFromJson(const Standard_SStream& theSStream, int& theStreamPos)`
    - `static void GeomTools::Read(occ::handle<Geom_Surface>& S, Standard_IStream& IS)`
    - `static Standard_IStream& BinTools::GetReal(Standard_IStream& IS, double& theValue)` (a binary package, a returned stream)
    - `void BinObjMgt_Persistent::SetIStream(Standard_IStream& theStream)` (stores the reference: skipped)

- **Rule**

    - Deliberately *not* a `str`: `Read(shape, "x.brep", builder)` must keep hitting the file-path overload; a non-file-like argument falls through to the next overload (`nanocct::TextInput` caster).
    - `InitFromJson`'s `int& theStreamPos` is in/out (`overrides.toml [inout] "*::InitFromJson"`, start at 1).
    - In a binary package the parameter is a **binary file-like object** (`typing.BinaryIO`: `io.BytesIO`, a file opened `"rb"`; `nanocct::BinaryInput` caster, `read()` must return `bytes`, so a text file-like falls through).
    - A returned `Standard_IStream&` next to the parameter (`BinObjMgt_Persistent::Read`, `BinTools::GetReal`, `GeomTools_UndefinedTypeHandler::ReadCurve`) is chaining and dropped, as for `ostream&`.
    - Constructors keep streams unsupported (an object may hold the reference), and the two OCCT methods that *store* a stream reference (`BinObjMgt_Persistent::SetOStream/SetIStream`) are in `[skip] methods`.

- **Python**

    - A **text file-like object** (`typing.TextIO`: `io.StringIO`, an open file; anything with `read()`), read completely into a `std::stringstream` for the call.

- **Python examples**

    ```python
    import io
    import struct
    from nanocct.BinObjMgt import BinObjMgt_Persistent
    from nanocct.BinTools import BinTools
    from nanocct.BRep import BRep_Builder
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.BRepTools import BRepTools
    from nanocct.gp import gp_Pnt
    from nanocct.TopoDS import TopoDS_Shape

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    shape = TopoDS_Shape()
    BRepTools.Read_s(shape, io.StringIO(BRepTools.Write_s(box)), BRep_Builder())   # a text file-like object
    assert shape.ShapeType() == box.ShapeType()

    point = gp_Pnt()
    ok, position = point.InitFromJson(io.StringIO(gp_Pnt(1, 2, 3).DumpJson()), 1)  # theStreamPos in and out
    assert ok and position > 1 and point.Z() == 3.0

    assert BinTools.GetReal_s(io.BytesIO(struct.pack("<d", 2.5))) == 2.5   # binary; the returned stream is dropped
    assert not hasattr(BinObjMgt_Persistent, "SetIStream")
    ```

    ```python
    import io
    import os
    import tempfile
    from nanocct.BinTools import BinTools
    from nanocct.BRep import BRep_Builder
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.BRepTools import BRepTools
    from nanocct.TopoDS import TopoDS_Shape

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    with tempfile.TemporaryDirectory() as folder:
        path = os.path.join(folder, "box.brep")
        assert BRepTools.Write_s(box, path)
        shape = TopoDS_Shape()
        assert BRepTools.Read_s(shape, path, BRep_Builder())     # a str is a file path, not a stream
    try:
        BinTools.Read_s(TopoDS_Shape(), io.StringIO("text"))     # a binary package refuses a text file-like
    except TypeError:
        pass
    else:
        raise AssertionError("a text file-like must not reach a binary stream")
    ```

## 7.4 Overloads that Python cannot tell apart

See 3.1 (3) and 3.2.

### R-COLLISION

- **C++ Idiom**

    Overloads that coincide once out-params are dropped — overloads that differ only in the *width* of their parameters, out-parameters included, are R-WIDTH twins, not a collision: both keep the plain name, in R-WIDTH's order

- **OCCT examples**

    `gp_Pnt::Coord()` → `gp_XYZ` and `Coord(double&, double&, double&)`; `GeomAPI_IntCS::Parameters(Index, U&, V&, W&)` for a point and `Parameters(Index, U1&, V1&, U2&, V2&)` for a segment; `GeomTools::Read(handle<Geom_Curve>&, istream&)` / `Geom2d_Curve` / `Geom_Surface`; the R-WIDTH twins `Graphic3d_Vertex::Coord(double&, double&, double&)` / `Coord(float&, float&, float&)`:

    - `const gp_XYZ& gp_Pnt::Coord() const` / `void gp_Pnt::Coord(double& theXp, double& theYp, double& theZp) const`
    - `void GeomAPI_IntCS::Parameters(const int Index, double& U, double& V, double& W) const` / `void GeomAPI_IntCS::Parameters(const int Index, double& U1, double& V1, double& U2, double& V2) const`
    - `static void GeomTools::Read(occ::handle<Geom_Curve>& C, Standard_IStream& IS)` (also for `Geom2d_Curve` and `Geom_Surface`)
    - `bool BOPDS_PaveBlock::HasEdge() const` / `bool BOPDS_PaveBlock::HasEdge(int& theEdge) const`
    - `void Graphic3d_Vertex::Coord(float& theX, float& theY, float& theZ) const` / `void Graphic3d_Vertex::Coord(double& theX, double& theY, double& theZ) const`

- **Rule**

    - Python cannot dispatch on results, so the overloads must get distinct names.
    - The suffix is unique within a group because C++ overloads cannot share a parameter list, it is stable across OCCT versions (unlike a number) and derivable from the reference docs — the same principle as `_s` (R-STATIC-S), applied only where a collision exists (the `operator>>` groups are not bound anyway).
    - A winner rule (scalar result / most out-params / deprecated loses) would make overloads unreachable that carry different information (`GeomAPI_IntCS::Parameters`, `GeomTools::Read`, `CSLib::Normal`, `Units::ToSI` with its dimension handle).

- **Python**

    - Every overload that has out-parameters is bound as **`Name__<type1>__<type2>…`** — the Python types of its removed out-parameters in C++ order (`float`, `int`, `bool`, `str`; `str`/`bytes` for a stream; an enum or class by its Python name, a container instantiation by its 7a name): `Coord__float__float__float()`, `Parameters__float__float__float(i)` and `Parameters__float__float__float__float(i)`, `Read_s__Geom_Curve(stream)`, `Normal_s__CSLib_NormalStatus(…)`, `Knots__NCollection_HArray1__double()`.
    - An overload **without** out-parameters keeps the plain name and means what it means in C++ (`BRep_Tool.Parameter_s(V, E)` → `float`, `BOPDS_PaveBlock.HasEdge()` → `bool`), `gp_Pnt.Coord()` → `gp_XYZ` next to `Coord__float__float__float()`, `Bnd_Box.Get()` → `Bnd_Box.Limits` next to `Get__float__float__float__float__float__float()` — without exception: the name must follow from the header.
    - The suffix comes after `_s` when both apply (`Name_s__float`).
    - The docstring's first line names the C++ overload.
    - It applies to methods and namespace functions.

- **Python examples**

    ```python
    import io
    from nanocct.BOPDS import BOPDS_PaveBlock
    from nanocct.Bnd import Bnd_Box
    from nanocct.Geom import Geom_Line
    from nanocct.GeomTools import GeomTools
    from nanocct.gp import gp_Dir, gp_Pnt, gp_XYZ

    point = gp_Pnt(1, 2, 3)
    assert isinstance(point.Coord(), gp_XYZ)                         # no out-parameters: the plain name
    assert point.Coord__float__float__float() == (1.0, 2.0, 3.0)    # Coord(double&, double&, double&)
    assert "the C++ overload Coord(double &, double &, double &)" in point.Coord__float__float__float.__doc__

    box = Bnd_Box(gp_Pnt(0, 0, 0), gp_Pnt(1, 2, 3))
    assert isinstance(box.Get(), Bnd_Box.Limits)
    assert box.Get__float__float__float__float__float__float() == (0.0, 0.0, 0.0, 1.0, 2.0, 3.0)
    assert hasattr(BOPDS_PaveBlock, "HasEdge") and hasattr(BOPDS_PaveBlock, "HasEdge__int")

    text = GeomTools.Write_s(Geom_Line(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0)))
    assert isinstance(GeomTools.Read_s__Geom_Curve(io.StringIO(text)), Geom_Line)   # static: _s, then the suffix
    ```
### R-CONST-TWIN

- **C++ Idiom**

    Overloads that differ only in constness — of the method (`const gp_XYZ& Origin() const` / `gp_XYZ& Origin()`) or of a parameter

- **OCCT examples**

    `math_Vector::Value(i)`, `NCollection_Vec3::x()`, `BRepGraph::Editor()`; `TopoDS::Vertex(const TopoDS_Shape&)` / `(TopoDS_Shape&)`, `NCollection_Mat4::Map(const T*)` / `(T*)`:

    - `const TheItemType& math_VectorBase::Value(const int theNum) const` / `TheItemType& math_VectorBase::Value(const int theNum)` (`math_Vector` is `math_VectorBase<double>`)
    - `Element_t NCollection_Vec3::x() const` / `Element_t& NCollection_Vec3::x()`
    - `[[nodiscard]] const EditorView& BRepGraph::Editor() const` / `[[nodiscard]] EditorView& BRepGraph::Editor()`
    - `const TopoDS_Vertex& TopoDS::Vertex(const TopoDS_Shape& theShape)` / `TopoDS_Vertex& TopoDS::Vertex(TopoDS_Shape& theShape)`
    - `const TopoDS_Edge& BRepClass_Edge::Edge() const` / `TopoDS_Edge& BRepClass_Edge::Edge()`

- **Rule**

    - Python objects are never const, so C++ itself would select the non-const overload on any Python-held object.
    - Header order would otherwise decide whether `arr[i].SetX()` edits the container (`reference_internal`) or a copy.

- **Python**

    - Only the **least const** twin is bound.
    - The others are reported.

- **Python examples**

    ```python
    from nanocct import TopoDS
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from nanocct.BRepClass import BRepClass_Edge
    from nanocct.BVH import BVH_Vec3d
    from nanocct.gp import gp_Pnt
    from nanocct.TopAbs import TopAbs_Orientation

    vertex = TopoDS.Vertex(BRepBuilderAPI_MakeVertex(gp_Pnt(1, 2, 3)).Shape())   # Vertex(TopoDS_Shape&)
    assert TopoDS.Vertex.__doc__.count("Vertex(theShape:") == 1                  # the const& twin is not bound

    edge = BRepClass_Edge()
    edge.Edge().Orientation(TopAbs_Orientation.TopAbs_REVERSED)   # the non-const Edge(): a reference into edge
    assert edge.Edge().Orientation() == TopAbs_Orientation.TopAbs_REVERSED

    vec = BVH_Vec3d(1.0, 2.0, 3.0)            # NCollection_Vec3<double>: the non-const x() returns double&
    vec.Setx(4.0)
    assert vec.x() == 4.0
    ```
### R-WIDTH

- **C++ Idiom**

    Overloads that differ only in the width of scalar parameters or in their text type

- **OCCT examples**

    `Abs(double)` / `Abs(float)`, `Min`, `Max`, `Quantity_Color::Convert_sRGB_To_LinearRGB`, `NCollection_PackedMap(size_t)` / `(int)`, `Poly_ArrayOfNodes::Value(int)` / `(size_t)`; text: `TCollection_AsciiString::Cat(const char*)` / `(std::string_view)` / `(char)`, `TCollection_ExtendedString(const char*, bool = false)` / `(const char16_t*)`:

    - `double Abs(const double theValue)` / `float Abs(const float theValue)` (`Standard_Real.hxx:141`, `Standard_ShortReal.hxx:35`)
    - `static double Quantity_Color::Convert_sRGB_To_LinearRGB(double thesRGBValue)` / `static float Quantity_Color::Convert_sRGB_To_LinearRGB(float thesRGBValue)`
    - `NCollection_PackedMap::NCollection_PackedMap(const size_t theNbBuckets = 1)` / `NCollection_PackedMap::NCollection_PackedMap(const int theNbBuckets)` (the narrow one declared first)
    - `gp_Pnt Poly_ArrayOfNodes::Value(int theIndex) const` / `gp_Pnt Poly_ArrayOfNodes::Value(const size_t theIndex) const`
    - `TCollection_ExtendedString::TCollection_ExtendedString(const char* const theString, const bool theIsMultiByte = false)` / `TCollection_ExtendedString::TCollection_ExtendedString(const char16_t* const theString)`

- **Rule**

    - nanobind takes the first overload a Python `float`/`int`/`str` fits.
    - A `float` twin first would round every value to float32; a `size_t`/`unsigned` twin first would reject negative indices.
    - Header order is not a rule: it is right for `Abs` (`Standard.Abs(-1e300) == 1e300` verified), but `NCollection_PackedMap(const size_t)` and `Graphic3d_Vertex::Coord(float&, float&, float&)` are declared before the twin registered first.
    - For text, "widest first" is wrong: `Resource_Manager::SetResource(name, const char16_t*)` stores the value through `Resource_Unicode`'s format, which with the default `NoConversion` makes `Value(name)` return Latin-1 bytes for "Größe" (measured in C++), while the `const char*` overload stores the UTF-8 as it is.
    - The C++ literal order keeps C++'s behaviour, including `TCollection_ExtendedString("Größe")` reading one byte per character unless `theIsMultiByte` is `true` (Pythonic-OCCT.md, Strings).

- **Python**

    - `double` is registered before `float`, and `int` before every other integer width, narrower or wider (`Value(int)` before `Value(size_t)`, `operator<<(const int)` before `operator<<(const uint8_t)`): a Python `int` is tried as `int` first, and a value outside its range falls through to the other twin (R-UNREACHABLE). `order_by_width()` in `emit.py`, also for constructors and namespace functions.
    - Every pair is reported.
    - Text is ordered as C++ resolves a narrow string literal: `const char*` (exact match) before `std::string_view`/`std::string` (a conversion), then `const char16_t*`, then `char`, `char16_t`, `char32_t` (`_TEXT_RANK`).
    - A twin that can never be reached this way is not bound (R-UNREACHABLE).

- **Python examples**

    ```python
    import nanocct.Standard
    from nanocct.Quantity import Quantity_Color
    from nanocct.TCollection import TCollection_ExtendedString

    assert nanocct.Standard.Abs(-1e300) == 1e300                   # Abs(double), not Abs(float)
    linear = Quantity_Color.Convert_sRGB_To_LinearRGB_s(0.5)       # the double overload: no float32 rounding
    assert abs(linear - ((0.5 + 0.055) / 1.055) ** 2.4) < 1e-15
    assert TCollection_ExtendedString("Größe").Length() == 7         # const char*: one character per UTF-8 byte, as in C++
    assert TCollection_ExtendedString("Größe", True).Length() == 5   # theIsMultiByte decodes it
    ```
### R-UNREACHABLE

- **C++ Idiom**

    An overload that an earlier-registered one takes over for every call it accepts, per number of passed arguments

- **OCCT examples**

    `Abs(float)` after `Abs(double)`, `AssignCat(char)` after `AssignCat(const char*)`, `TCollection_ExtendedString(const char16_t*)` after `(const char*, bool = false)`, `XSControl_Utils::ToHString(const char16_t*)` after `(const char*)`:

    - `float Abs(const float theValue)` after `double Abs(const double theValue)`
    - `void TCollection_AsciiString::AssignCat(const char theOther)` after `void TCollection_AsciiString::AssignCat(const char* const theCString)`
    - `void TCollection_AsciiString::AssignCat(const std::string_view& theStringView)` after the same
    - `TCollection_ExtendedString::TCollection_ExtendedString(const char16_t* const theString)` after `TCollection_ExtendedString::TCollection_ExtendedString(const char* const theString, const bool theIsMultiByte = false)`
    - `occ::handle<TCollection_HExtendedString> XSControl_Utils::ToHString(const char16_t* const strcon) const` after `occ::handle<TCollection_HAsciiString> XSControl_Utils::ToHString(const char* const strcon) const`

- **Rule**

    - It can never be called from Python: nanobind stops at the first overload that accepts the arguments.
    - "Takes over" is decided per parameter: a `double` covers a `float` and a string type covers any text, but an `int` never covers another integer width (nanobind's range check fails over: `Poly_ArrayOfNodes::Value(2**31)` reaches the `size_t` twin, measured), and a class covers only itself.
    - Overloads with out-parameters are left alone, R-COLLISION may give them names of their own.
    - A keyword call that names a dropped twin's parameter is not covered: it fails with `TypeError`.

- **Python**

    - Not bound, reported (`drop_unreachable()` in `emit.py`).
    - 72<!-- count: unreachable --> overloads are dropped (OCCT 8.0.1).

- **Python examples**

    ```python
    from nanocct.TCollection import TCollection_AsciiString, TCollection_ExtendedString

    text = TCollection_AsciiString("ab")
    text.AssignCat("c")                                   # AssignCat(const char*) takes every str
    assert text.ToCString() == "abc"
    assert "AssignCat(self, theOther: str)" not in TCollection_AsciiString.AssignCat.__doc__   # AssignCat(char)
    try:
        text.AssignCat(theStringView="d")                 # the parameter of the dropped std::string_view twin
        raise AssertionError("a dropped twin was called")
    except TypeError:
        pass
    assert "__init__(self, theString: str) -> None" not in TCollection_ExtendedString.__init__.__doc__   # (const char16_t*)
    ```
### R-UNBOUND-TYPE

- **C++ Idiom**

    A parameter or result whose class or enum no binding registers: bound nowhere, bound only through its R-NONCOPYABLE wrapper, or a `Standard_Failure` descendant, which is a Python exception type and never a value

- **OCCT examples**

    Bound nowhere: `FILE*` from `OSD_OpenFile`, `rapidjson::ParseErrorCode`, internal classes such as `Storage_BucketOfPersistent`, `TDF_LabelNode`, `BRepMesh_VertexTool`, the nested `BRepGraph_CacheMesh::*Entry`; bound only through its R-NONCOPYABLE wrapper: `IntTools_FClass2d&`, whose typeid is not the wrapper's; a `Standard_Failure` descendant: `MoniTool_CaseData::AddRaised(const Standard_Failure&, …)`:

    - `FILE* OSD_OpenFile(const TCollection_ExtendedString& theName, const char* theMode)`
    - `static const char* RWGltf_GltfJsonParser::FormatParseError(rapidjson::ParseErrorCode theCode)`
    - `TDF_AttributeIterator::TDF_AttributeIterator(const TDF_LabelNodePtr aLabelNode, const bool withoutForgotten = true)`
    - `IntTools_FClass2d& IntTools_Context::FClass2d(const TopoDS_Face& aF)`
    - `void MoniTool_CaseData::AddRaised(const Standard_Failure& theException, const char* const name = "")`

- **Rule**

    - Such a member cannot be called (no Python object of the type exists) or fails on every non-null result with nanobind's "Unable to convert function return value" -- `OSD_OpenFile` would even open the file first and leak the `FILE*`.
    - Its stub would spell the C++ type as a string, platform-specific (`"__sFILE"` on macOS).
    - Class names are judged against `known`.
    - An **NCollection binder instantiation** is judged by its registry key, which parse computes exactly as `_note_instance` records it (`parse._binder_key`; unbound when the registry has none -- raw-pointer elements, `NCollection_IndexedMap<Graphic3d_CStructure *>` -- or skipped it, or for a nested class other than a kind's `Iterator`, `DynamicArray<T>::DynamicIterator`).
    - Comparing spellings instead fails on default arguments (`math_VectorBase<>` vs `<double>`, dropped hashers): 841 members would be skipped wrongly.
    - Other template instantiations (7c) are not judged; their stubs keep the quoted C++ name.
    - In a 7c walk the STL-style iterator types have no declaration, so they are recognised by name (`_STL_ITERATORS`, `::iterator`, `::DynamicIterator`): `NCollection_Iterator<Container>::ValueIter()` returns `typename Container::iterator` (R-ITERATOR).
    - R-DEFAULT-UNBOUND is the older special case for defaults.
    - A **standard-library enum** has no Python type either and makes the member unbindable already in the parse (`param '…': std::X (a standard-library enum, no Python type)`): libstdc++ spells `std::ios_base::openmode` as the enum `std::_Ios_Openmode` where libc++ and MSVC have an integer, so `OSD_OpenFileDescriptor(name, mode)` would be bound on Linux and raise `TypeError`.

- **Python**

    - Member not bound, reported (`Emitter._skip_unbound()`).
    - 38<!-- count: unbound-type --> members are skipped (OCCT 8.0.1).

- **Python examples**

    ```python
    import nanocct.OSD
    from nanocct.IntTools import IntTools_Context
    from nanocct.MoniTool import MoniTool_CaseData
    from nanocct.RWGltf import RWGltf_GltfJsonParser
    from nanocct.TDF import TDF_AttributeIterator

    assert not hasattr(nanocct.OSD, "OSD_OpenFile")                  # FILE*
    assert not hasattr(RWGltf_GltfJsonParser, "FormatParseError_s")   # rapidjson::ParseErrorCode
    assert "aLabelNode" not in TDF_AttributeIterator.__init__.__doc__  # TDF_LabelNode*: the other constructors stay
    assert not hasattr(IntTools_Context, "FClass2d")                  # IntTools_FClass2d: only its wrapper is bound
    assert not hasattr(MoniTool_CaseData, "AddRaised")                # Standard_Failure is a Python exception type
    ```
### R-OVERLOAD-ORDER

- **C++ Idiom**

    Overloads of the same name and arity where one takes, position by position, the same types or derived classes of the other's

- **OCCT examples**

    `PLib::CoefficientsPoles(const NCollection_Array2<gp_Pnt>&, …)` after `(const NCollection_Array1<gp_Pnt>&, …)`, `GeomToIGES_GeomCurve::TransferCurve(Geom_BSplineCurve)` after `(Geom_Curve)`, `BOPTools_AlgoTools::IsSplitToReverse(TopoDS_Face, …)` after `(TopoDS_Shape, …)`, a copy constructor after one from the base class:

    - `static void PLib::CoefficientsPoles(const NCollection_Array2<gp_Pnt>& Coefs, const NCollection_Array2<double>* WCoefs, NCollection_Array2<gp_Pnt>& Poles, NCollection_Array2<double>* WPoles)` after `static void PLib::CoefficientsPoles(const NCollection_Array1<gp_Pnt>& Coefs, const NCollection_Array1<double>* WCoefs, NCollection_Array1<gp_Pnt>& Poles, NCollection_Array1<double>* WPoles)`
    - `occ::handle<IGESData_IGESEntity> GeomToIGES_GeomCurve::TransferCurve(const occ::handle<Geom_BSplineCurve>& start, const double Udeb, const double Ufin)` after `occ::handle<IGESData_IGESEntity> GeomToIGES_GeomCurve::TransferCurve(const occ::handle<Geom_Curve>& start, const double Udeb, const double Ufin)`
    - `static bool BOPTools_AlgoTools::IsSplitToReverse(const TopoDS_Face& theSplit, const TopoDS_Face& theShape, const occ::handle<IntTools_Context>& theContext, int* theError = nullptr)` after the `const TopoDS_Shape&` overload
    - `IGESToBRep_TopoCurve::IGESToBRep_TopoCurve(const IGESToBRep_TopoCurve& CS)` after `IGESToBRep_TopoCurve::IGESToBRep_TopoCurve(const IGESToBRep_CurveAndSurface& CS)` (the copy constructor after one from the base class)

- **Rule**

    - nanobind calls the first registered overload that accepts the arguments, and a derived object is accepted by a base parameter in its first pass.
    - C++ overload resolution picks the most derived.
    - Otherwise `CoefficientsPoles_s` with `Array2` arguments runs the curve algorithm on the flat data (measured).
    - 53<!-- count: overload-order --> overloads are moved (OCCT 8.0.1).

- **Python**

    - The overload taking the derived class is **registered first**, otherwise header order (`order_by_derivation()` in `emit.py`, after R-WIDTH, also for constructors and namespace functions).
    - Every move is reported as `overload-collision`.
    - The class hierarchy comes from the package's parse (`parse._class_ancestors`, template bases such as `NCollection_Array2<T> : NCollection_Array1<T>`) closed over the manifest's `bases` of every bound class (a package that only forward-declares `Geom_BSplineCurve` cannot see its bases).

- **Python examples**

    ```python
    from nanocct.GeomToIGES import GeomToIGES_GeomCurve
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array2
    from nanocct.PLib import PLib

    points, reals = NCollection_Array2[gp_Pnt], NCollection_Array2[float]
    coefs, poles, wcoefs, weights = points(1, 2, 1, 2), points(1, 2, 1, 2), reals(1, 2, 1, 2), reals(1, 2, 1, 2)
    for (i, j), xyz in {(1, 1): (0, 0, 0), (2, 1): (1, 0, 0), (1, 2): (0, 1, 0), (2, 2): (0, 0, 1)}.items():
        coefs.SetValue(i, j, gp_Pnt(*xyz))
        wcoefs.SetValue(i, j, 1.0 if (i, j) == (1, 1) else 0.0)
    PLib.CoefficientsPoles_s(coefs, wcoefs, poles, weights)    # the Array2 (surface) overload, registered first
    assert poles.Value(2, 2).Coord__float__float__float() == (1.0, 1.0, 1.0)   # c11 + c21 + c12 + c22

    overloads = [l for l in GeomToIGES_GeomCurve.TransferCurve.__doc__.splitlines() if l.startswith("TransferCurve(")]
    assert "Geom_BSplineCurve" in overloads[0] and "Geom_Curve |" in overloads[-1]
    ```
### R-CTOR-AMBIGUOUS

- **C++ Idiom**

    Constructor overloads whose call with some number of arguments is ambiguous in C++

- **OCCT examples**

    `IntPolyh_Array(const int aIncrement = 256)` next to `IntPolyh_Array(const int aN, const int aIncrement = 256)`: `IntPolyh_Array<T>(5)` does not compile:

    - `IntPolyh_Array::IntPolyh_Array(const int aIncrement = 256)` (`IntPolyh_Array.hxx:69`)
    - `IntPolyh_Array::IntPolyh_Array(const int aN, const int aIncrement = 256)` (`IntPolyh_Array.hxx:83`)

- **Rule**

    - nanobind's `nb::init<Args…>` always calls the constructor with every bound parameter (Python fills the defaults), so the ambiguity is a compile error.
    - Decided by `resolve_ctor_arities()` in `emit.py` (pure, unit-tested).
    - Reported as `overload-collision`.

- **Python**

    - A constructor is bound with the largest number of leading parameters whose call is unambiguous (`nb::init<>()` for the first one above, the second in full).
    - A constructor with no such arity is skipped.
    - No `implicitly_convertible` when the one-argument call is ambiguous.

- **Python examples**

    ```python
    from nanocct.IntPolyh import IntPolyh_ArrayOfEdges, IntPolyh_ArrayOfPoints

    assert IntPolyh_ArrayOfPoints(5).NbItems() == 0          # (aN, aIncrement = 256)
    assert IntPolyh_ArrayOfPoints(5, 10).NbItems() == 0
    assert IntPolyh_ArrayOfEdges().NbItems() == 0             # (aIncrement = 256), bound without its argument
    signatures = [l for l in IntPolyh_ArrayOfEdges.__init__.__doc__.splitlines() if l.startswith("__init__")]
    assert signatures[:2] == ["__init__(self) -> None", "__init__(self, aN: int, aIncrement: int = 256) -> None"]
    ```

## 7.5 Operators, conversions, hashing, iteration

The Python additions of Design.md, section 2.

### R-OPERATOR

- **C++ Idiom**

    `operator+ - * / % ^ & | == != < <= > >= () []`, unary `- + !`

- **OCCT examples**

    - `gp_Vec gp_Vec::operator+(const gp_Vec& theOther) const`
    - `gp_Vec gp_Vec::operator-() const` (unary)
    - `double& math_Matrix::operator()(const int Row, const int Col)`
    - `bool BOPDS_Pave::operator<(const BOPDS_Pave& theOther) const`
    - `char32_t NCollection_UtfString::operator[](const int theCharIndex) const`
    - `bool BinObjMgt_Persistent::operator!() const` (not bound)

- **Rule**

    - Member operators.
    - Bound with `nb::is_operator()`.
    - Unary `!` is not bound: Python has no protocol that `not` would call, `not x` asks `__bool__`. Its one site, `bool BinObjMgt_Persistent::operator!() const { return IsError(); }`, has `operator bool() const { return IsOK(); }` next to it (R-CONV-SCALAR), so `not persistent` is the C++ `!persistent`.

- **Python**

    - `__add__` … `__call__`, `__neg__` …
    - `operator!`: not bound, reported as an operator without a Python equivalent.

- **Python examples**

    ```python
    from nanocct.BinObjMgt import BinObjMgt_Persistent
    from nanocct.BOPDS import BOPDS_Pave
    from nanocct.gp import gp_Vec
    from nanocct.math import math_Matrix
    from nanocct.NCollection import NCollection_UtfString__char16_t

    v, w = gp_Vec(1, 2, 3), gp_Vec(0, 1, 0)
    assert (v + w).Y() == 3.0 and (-v).X() == -1.0
    assert v * w == 2.0 and (v ^ w).Z() == 1.0        # the dot and the cross product
    assert v.__add__(1) is NotImplemented              # nb::is_operator(): Python then raises its own TypeError
    matrix = math_Matrix(1, 2, 1, 2, 3.0)
    assert matrix(1, 2) == 3.0                         # operator(): __call__
    persistent = BinObjMgt_Persistent()
    assert not hasattr(persistent, "__not__") and (not persistent) == persistent.IsError()   # operator! is __bool__'s negation
    first, second = BOPDS_Pave(), BOPDS_Pave()
    first.SetParameter(1.0)
    second.SetParameter(2.0)
    assert first < second
    assert NCollection_UtfString__char16_t("abc")[1] == "b"   # operator[]: __getitem__
    ```
### R-IOP

- **C++ Idiom**

    `void operator+=` etc., or `T& operator+=` returning `*this`

- **OCCT examples**

    - `void gp_Vec::operator+=(const gp_Vec& theOther)`
    - `void gp_Vec::operator^=(const gp_Vec& theRight)` (the cross product in place)
    - `void math_Matrix::operator*=(const double Right)`
    - `NCollection_Vec3& NCollection_Vec3::operator+=(const NCollection_Vec3& theAdd)` (returns `*this`)

- **Rule**

    - OCCT in-place operators return `void` (or `*this`: `NCollection_Vec2/3/4`, `NCollection_Mat3/4`, the NCollection iterators, `NCollection_UtfString`, `Message_ExecStatus`).

- **Python**

    - `__iadd__` … returning `self` (same object).

- **Python examples**

    ```python
    from nanocct.gp import gp_Vec
    from nanocct.math import math_Matrix
    from nanocct.Quantity import NCollection_Vec3__float

    v = gp_Vec(1, 2, 3)
    before = v
    v += gp_Vec(1, 1, 1)                  # void operator+=: __iadd__ returns self
    assert v is before and v.X() == 2.0
    v ^= gp_Vec(0, 0, 1)                  # the cross product in place
    assert v is before and (v.X(), v.Y(), v.Z()) == (3.0, -2.0, 0.0)
    matrix = math_Matrix(1, 2, 1, 2, 1.0)
    same = matrix
    matrix *= 2.0
    assert matrix is same and matrix(1, 1) == 2.0
    a = NCollection_Vec3__float(1.0, 2.0, 3.0)
    same = a
    a += NCollection_Vec3__float(1.0, 1.0, 1.0)   # NCollection_Vec3& operator+=: the same object too
    assert a is same and a.x() == 2.0
    ```
### R-FREE-OP

- **C++ Idiom**

    Free `operator*(double, gp_Vec)`; a **hidden friend** operator declared in the class body

- **OCCT examples**

    `friend NCollection_Vec3 operator+(const NCollection_Vec3&, const NCollection_Vec3&)` in `NCollection_Vec2/3/4`, `friend math_Matrix operator*(double, const math_Matrix&)`, `friend bool operator==(const BRepGraph_ItemId&, const BRepGraph_ItemId&)`, `NCollection_UtfString::operator+`:

    - `gp_Vec operator*(const double theScalar, const gp_Vec& theV)` (free, in `gp_Vec.hxx`)
    - `friend NCollection_Vec3 operator+(const NCollection_Vec3& theLeft, const NCollection_Vec3& theRight)` (in `NCollection_Vec3`)
    - `friend math_Matrix operator*(const double Left, const math_Matrix& Right)` (in `math_Matrix`, defined in `math_Matrix.lxx`)
    - `friend bool operator==(const BRepGraph_ItemId& theLeft, const BRepGraph_ItemId& theRight)` (in `BRepGraph_ItemId`)
    - `friend NCollection_UtfString operator+(const NCollection_UtfString& theLeft, const NCollection_UtfString& theRight)` (in `NCollection_UtfString`)

- **Rule**

    - A hidden friend is found by ADL only, and a walk of the enclosing scope never meets it — silently, since nothing reports a `FRIEND_DECL`.
    - The lambda has no library symbol to check (R-UNDEFINED does not apply).

- **Python**

    - `__rmul__` on `gp_Vec` (reflected when the class is the 2nd operand, normal when it is the 1st).
    - The friend is handed to the same pass from the class walk (`Class.friend_ops`) and bound through a lambda that finds it by ADL (`v + v` on `Graphic3d_Vec3`, `2.0 * m` on `math_Matrix`; `Graphic3d_Vec3` is the C++ alias of `NCollection_Vec3<float>`, `NCollection_Vec3__float` in Python).

- **Python examples**

    ```python
    from nanocct.BRepGraph import BRepGraph_ItemId
    from nanocct.gp import gp_Vec
    from nanocct.math import math_Matrix
    from nanocct.NCollection import NCollection_UtfString__char16_t
    from nanocct.Quantity import NCollection_Vec3__float

    assert (2.0 * gp_Vec(1, 2, 3)).Z() == 6.0     # free operator*(double, gp_Vec): gp_Vec.__rmul__
    v = NCollection_Vec3__float(1.0, 2.0, 3.0)      # Graphic3d_Vec3 in C++
    assert (v + v).z() == 6.0                       # hidden friend operator+
    m = math_Matrix(1, 2, 1, 2, 3.0)
    assert (2.0 * m)(1, 2) == 6.0                   # hidden friend operator*(double, const math_Matrix&)
    assert BRepGraph_ItemId() == BRepGraph_ItemId() # hidden friend operator==
    text = NCollection_UtfString__char16_t("ab") + NCollection_UtfString__char16_t("c")
    assert text.Length() == 3
    ```
### R-STR

- **C++ Idiom**

    OCCT's print operator: `Standard_OStream& operator<<(Standard_OStream&, const T&)` free, as a hidden friend or as a member `Standard_OStream& T::operator<<(Standard_OStream&) const` (or not const); the member `VrmlData_Scene& operator<<(Standard_IStream&)`

- **OCCT examples**

    Free in three `math_*.hxx`, 22 `math_*.lxx`, `TDF_Label.lxx`, `AppParCurves_MultiPoint.lxx`, `FairCurve_Batten.lxx`, `FairCurve_MinimalVariation.lxx`, `IntRes2d_Transition.lxx` and `Standard_Type.hxx`; as a hidden friend in `math_VectorBase`, `TCollection_AsciiString`, `TCollection_ExtendedString`, `VrmlData_Scene`; as a member in `TDF_Label`, `TDF_Attribute`, `TDF_Data`, `TDF_DataSet`, `TDF_AttributeDelta`, `TFunction_DriverTable` (`{ return Dump(anOS); }`, `TDF_AttributeDelta`'s with `OS`) and `CDM_MetaData` (not const, `return Print(anOStream);` in the `.cxx`):

    - `Standard_OStream& operator<<(Standard_OStream& o, const math_Matrix& mat)` (free, in `math_Matrix.lxx`)
    - `friend Standard_OStream& operator<<(Standard_OStream& theStream, const TCollection_AsciiString& theString)` (a hidden friend)
    - `Standard_OStream& TDF_Label::operator<<(Standard_OStream& anOS) const` (the member form; `TDF_Label.lxx` has the free one too)
    - `VrmlData_Scene& VrmlData_Scene::operator<<(Standard_IStream& theInput)` (the member reader)
    - `Standard_OStream& operator<<(Standard_OStream& OS, const gp_Pnt& P)` (in `BinTools_ShapeSetBase.hxx`: binary, not bound)

- **Rule**

    - The stream is the *first* operand, so neither R-FREE-OP nor R-STREAM-OUT reached it.
    - The filter is not decoration: `BinTools_ShapeSetBase.hxx` declares `operator<<(Standard_OStream&, const gp_Pnt&)`, which writes three binary doubles (`BinTools_ShapeSetBase.cxx:29`), and `BinObjMgt_Persistent`'s is its binary `Write` — a blanket rule would have given `gp_Pnt` a `__str__` returning bytes.
    - `repr()` is not touched: a 30-line `math_Matrix` dump is not a representation.
    - **Platform difference:** `IntRes2d_Transition`'s operator and BinTools' two carry no `Standard_EXPORT`, so on Windows R-UNDEFINED skips them first — Windows binds 41 `__str__`, macOS and Linux 42.

- **Python**

    - `T.__str__`, returning exactly the text OCCT writes (a lambda streams into a `std::ostringstream`, decoded like R-STREAM-OUT).
    - The member reader becomes `Read(TextIO)` (R-STREAM-IN), its `*this` result dropped like R-OUT's.
    - **Only when the operator prints `T`**: it is declared in `T`'s own header (`X.hxx` or its `X.lxx`), its stream is text (not a `[stream] binary_packages` package -- the free form, a hidden friend and a nested class's operator alike), `T` is no exception class, and `T` has no member form bound already (TDF has both).

- **Python examples**

    ```python
    import io
    from nanocct.gp import gp_Pnt
    from nanocct.math import math_Matrix
    from nanocct.TCollection import TCollection_AsciiString
    from nanocct.TDF import TDF_Data
    from nanocct.VrmlData import VrmlData_Scene

    matrix = math_Matrix(1, 2, 1, 2, 3.0)
    assert str(matrix).startswith("math_Matrix of RowNumber = 2 and ColNumber = 2")
    assert repr(matrix).startswith("<nanocct.math.math_Matrix object at ")   # repr() is not touched
    assert str(TCollection_AsciiString("abc")) == "abc"                     # the hidden friend
    label = TDF_Data().Root()
    assert str(label) == label.Dump()                                       # the member form
    scene = VrmlData_Scene()
    scene.Read(io.StringIO("#VRML V2.0 utf8\nShape { geometry Box { size 1 2 3 } }\n"))   # the member reader
    assert "Box" in str(scene)
    assert "__str__" not in vars(gp_Pnt)              # BinTools' operator<< for gp_Pnt writes binary doubles
    ```
### R-CONV-SCALAR

- **C++ Idiom**

    Conversion operator `operator bool/int/double()`, const or not

- **OCCT examples**

    - `MeshVS_Buffer::operator double&()` (not const)
    - `MeshVS_Buffer::operator int&()` (not const)
    - `GeomAPI_ProjectPointOnCurve::operator int() const` (`NbPoints()`)
    - `GeomAPI_ProjectPointOnCurve::operator double() const` (`LowerDistance()`)
    - `BinObjMgt_Persistent::operator bool() const` (`IsOK()`)

- **Rule**

    - The lambda's `self` follows the operator's constness: `MeshVS_Buffer::operator double&()`/`int&()` are **not** const, and a `const` self makes the `static_cast` fail to compile.

- **Python**

    - `__bool__`/`__int__`/`__float__`.

- **Python examples**

    ```python
    from nanocct.BinObjMgt import BinObjMgt_Persistent
    from nanocct.GC import GC_MakeSegment
    from nanocct.GeomAPI import GeomAPI_ProjectPointOnCurve
    from nanocct.gp import gp_Pnt
    from nanocct.MeshVS import MeshVS_Buffer

    segment = GC_MakeSegment(gp_Pnt(0, 0, 0), gp_Pnt(10, 0, 0)).Value()
    projector = GeomAPI_ProjectPointOnCurve(gp_Pnt(5, 3, 0), segment)
    assert int(projector) == projector.NbPoints() == 1
    assert float(projector) == projector.LowerDistance() and abs(float(projector) - 3.0) < 1e-9
    assert bool(BinObjMgt_Persistent())                # operator bool(): IsOK()
    # the non-const operator double&()/int&() are bound too (a fresh buffer's content is undefined, so not read here)
    assert "__float__" in vars(MeshVS_Buffer) and "__int__" in vars(MeshVS_Buffer)
    ```
### R-NULL-BOOL

- **C++ Idiom**

    A class with a public `bool IsNull()` (or `Standard_Boolean`; no parameters, not static, const or not) and no `operator bool`; derived classes inherit it

- **OCCT examples**

    7<!-- count: null-bool --> classes (OCCT 8.0.1) -- `TopoDS_Shape`, `TDF_Label`, `BRepGraph`, `StepData_SelectType`, `XCAFDoc_AssemblyItemId`, `Poly_MakeLoops::Link`, `PeriodicInterval` (`PeriodicInterval::IsNull()` is not const); derived classes (`TopoDS_Edge`) inherit it:

    - `bool TopoDS_Shape::IsNull() const`
    - `bool TDF_Label::IsNull() const`
    - `bool StepData_SelectType::IsNull() const`
    - `bool Poly_MakeLoops::Link::IsNull() const`
    - `bool PeriodicInterval::IsNull()` (in `IntCurve_IntConicConic_Tool.hxx`)

- **Rule**

    - Python's truthiness, derived mechanically like `__len__` from `Length` and R-ITER from `More`/`Next`/`Value`: a null handle is already `None` (falsy, R-HANDLE) and an empty container already falsy (`__len__`), so a null value object is falsy too.
    - On all 7<!-- count: null-bool --> classes "null" means none or empty (no TShape, no label node, no stored entity, an empty path or interval, `!IsValid()`); none of them has `__len__` or `__iter__` to compete.
    - Truthiness is *not null*, not *has children*: an empty compound is true.
    - Without it every object would be true and `if shape:` would hold for a null shape, silently.
    - A `__bool__` raising `TypeError`, on the grounds that OCCT has no `operator bool`, does not fit: the Python additions' are not limited to C++ operators.

- **Python**

    - `__bool__` = `not IsNull()` (docstring "Python addition"), the lambda's `self` following `IsNull`'s constness.
    - With an `operator bool` R-CONV-SCALAR binds the real one instead.

- **Python examples**

    ```python
    from nanocct.BRep import BRep_Builder
    from nanocct.TDF import TDF_Data, TDF_Label
    from nanocct.TopoDS import TopoDS_Compound, TopoDS_Edge, TopoDS_Shape

    assert not TopoDS_Shape() and not TopoDS_Edge()    # null: no TShape; TopoDS_Edge inherits __bool__
    compound = TopoDS_Compound()
    BRep_Builder().MakeCompound(compound)
    assert compound and compound.NbChildren() == 0     # not null, though empty
    assert not TDF_Label() and TDF_Data().Root()
    assert "Python addition" in TopoDS_Shape.__bool__.__doc__
    ```
### R-CONV

- **C++ Idiom**

    Conversion operator `operator T() const` / `operator const handle<T>&() const` with a bound class `T`, const or not

- **OCCT examples**

    `gce_MakeLin` → `gp_Lin`, `GC_MakeSegment` → `handle<Geom_TrimmedCurve>`, `BRepGraph_EdgeId` → `BRepGraph_NodeId`, `BRepBuilderAPI_MakeShape` → `TopoDS_Shape`:

    - `gce_MakeLin::operator gp_Lin() const`
    - `GC_MakeSegment::operator const occ::handle<Geom_TrimmedCurve>&() const`
    - `BRepGraph_NodeId::Typed<TheKind>::operator BRepGraph_NodeId() const` (`BRepGraph_EdgeId` is `BRepGraph_NodeId::Typed<BRepGraph_NodeId::Kind::Edge>`)
    - `BRepBuilderAPI_MakeShape::operator TopoDS_Shape()` (not const)
    - `XmlObjMgt_Persistent::operator XmlObjMgt_Element&()` (and its twin `XmlObjMgt_Persistent::operator const XmlObjMgt_Element&() const`)

- **Rule**

    - Emitted in a phase of its own after every definition of the toolkit (a class's zero-argument `__new__` must come first).
    - A target in a *later* toolkit would be skipped and reported (none at present: `NCollection_Vec3<float>` is instantiated on demand by `Quantity` in a clean run, so `Quantity_Color` → `BVH_Vec3f` works).
    - Enum targets have no Python spelling.

- **Python**

    - `T(aFrom)` constructor overload on `T` plus, unless `explicit`, `nb::implicitly_convertible` (a From passes where a T is expected).
    - A handle conversion returns the same object.
    - Const/non-const twins (`XmlObjMgt_Persistent::operator XmlObjMgt_Element&` and `const&`; `OpenGl_TextureSet::TextureSlot::operator occ::handle<OpenGl_Texture>&` and `const&`) give one conversion.

- **Python examples**

    ```python
    from nanocct.Bnd import Bnd_Box
    from nanocct.BRepBndLib import BRepBndLib
    from nanocct.BRepGraph import BRepGraph_EdgeId, BRepGraph_NodeId
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.BVH import BVH_Vec3f
    from nanocct.GC import GC_MakeSegment
    from nanocct.gce import gce_MakeLin
    from nanocct.Geom import Geom_TrimmedCurve
    from nanocct.gp import gp_Lin, gp_Pnt
    from nanocct.Quantity import Quantity_Color, Quantity_NameOfColor
    from nanocct.TopoDS import TopoDS_Shape

    assert gp_Lin(gce_MakeLin(gp_Pnt(0, 0, 0), gp_Pnt(1, 0, 0))).Direction().X() == 1.0
    segment = GC_MakeSegment(gp_Pnt(0, 0, 0), gp_Pnt(1, 0, 0))
    assert Geom_TrimmedCurve(segment) is segment.Value()      # a handle conversion: the same object
    assert BRepGraph_NodeId(BRepGraph_EdgeId(3)).Index == 3
    maker = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0)
    assert TopoDS_Shape(maker).IsSame(maker.Shape())
    box = Bnd_Box()
    BRepBndLib.Add_s(maker, box)                               # implicit: the maker passes as a TopoDS_Shape
    assert not box.IsVoid()
    assert BVH_Vec3f(Quantity_Color(Quantity_NameOfColor.Quantity_NOC_RED)).x() == 1.0
    ```
### R-IMPLICIT-CONV

- **C++ Idiom**

    Non-`explicit` converting constructor `T(const A&)`

- **OCCT examples**

    - `TCollection_AsciiString::TCollection_AsciiString(const char* const theMessage)`
    - `OSD_Path::OSD_Path(const TCollection_AsciiString& aDependentName, const OSD_SysType aSysType = OSD_Default)` (takes the converted string)
    - `Quantity_Color::Quantity_Color(const Quantity_NameOfColor theName)`
    - `LDOMString::LDOMString(const char* aValue)`
    - `explicit Quantity_ColorRGBA::Quantity_ColorRGBA(const Quantity_Color& theRgb)` (`explicit`: no conversion)

- **Rule**

    - C++ implicit conversion semantics, 1:1.

- **Python**

    - `nb::implicitly_convertible<A, T>` — `OSD_Path("/x")` works because `TCollection_AsciiString(const char*)` is implicit.

- **Python examples**

    ```python
    from nanocct.Graphic3d import Graphic3d_MaterialAspect, Graphic3d_NameOfMaterial
    from nanocct.OSD import OSD_Path
    from nanocct.Quantity import Quantity_Color, Quantity_ColorRGBA, Quantity_NameOfColor

    path = OSD_Path("part.step")                    # the str becomes the TCollection_AsciiString parameter
    assert path.Name().ToCString() == "part" and path.Extension().ToCString() == ".step"
    material = Graphic3d_MaterialAspect(Graphic3d_NameOfMaterial.Graphic3d_NameOfMaterial_Gold)
    material.SetColor(Quantity_NameOfColor.Quantity_NOC_RED)   # through Quantity_Color(const Quantity_NameOfColor)
    assert material.Color().Name() == Quantity_NameOfColor.Quantity_NOC_RED
    red = Quantity_Color(Quantity_NameOfColor.Quantity_NOC_RED)
    try:
        Quantity_ColorRGBA(red).IsEqual(red)        # Quantity_ColorRGBA(const Quantity_Color&) is explicit
        converted = True
    except TypeError:
        converted = False
    assert not converted
    ```
### R-IMPLICIT-COPY

- **C++ Idiom**

    Implicit copy constructor (none declared; a declared `T(const T&) = default` is the same constructor and goes the same way)

- **OCCT examples**

    None declared: `TopoDS_Shape`, `gp_Pnt`, …:

    - `TopoDS_Shape` declares only `TopoDS_Shape()` (`TopoDS_Shape.hxx:46`)
    - `gp_Pnt` declares `gp_Pnt()`, `gp_Pnt(const gp_XYZ& theCoord)` and `gp_Pnt(const double theXp, const double theYp, const double theZp)` (`gp_Pnt.hxx:37`, `gp_Pnt.hxx:42`, `gp_Pnt.hxx:48`)
    - `TopLoc_Location::TopLoc_Location(const TopLoc_Location& theOther) = default` (`TopLoc_Location.hxx:44`)
    - `gp_Dir::gp_Dir(const gp_Dir&) = default` (`gp_Dir.hxx:89`)

- **Rule**

    - `TopoDS_Shape(aVertex)` is the C++ way to upcast a shape.
    - Sub-classes convert implicitly as in C++.

- **Python**

    - `__init__(theOther)` bound when `std::is_copy_constructible_v<T>` (helper `nanocct_implicit_copy_ctor`, after the declared constructors) and R-COPY allows it.

- **Python examples**

    ```python
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeVertex
    from nanocct.gp import gp_Pnt
    from nanocct.TopLoc import TopLoc_Location
    from nanocct.TopoDS import TopoDS_Shape

    vertex = BRepBuilderAPI_MakeVertex(gp_Pnt(1, 2, 3)).Vertex()
    shape = TopoDS_Shape(vertex)                    # the copy constructor takes the sub-class: an upcast
    assert type(shape) is TopoDS_Shape and shape.IsSame(vertex)
    point = gp_Pnt(1, 2, 3)
    copy = gp_Pnt(point)
    copy.SetX(9.0)
    assert point.X() == 1.0                          # a copy
    assert TopLoc_Location(TopLoc_Location()).IsIdentity()   # T(const T&) = default, bound the same way
    ```
### R-COPY

- **C++ Idiom**

    A copy the bindings make or offer of a class whose implicit copy duplicates a raw pointer (or a reference) that a destructor may free: the class is an **owner** when a user-provided destructor the headers do not show empty (a body with statements, or one defined in a `.cxx`) sits in a class whose own part holds such a pointer -- the class itself, a base or a member held by value, recursively; a class with its own (not defaulted) copy constructor is trusted and not looked into. Read from the layout walk (`_Held.copy_owners`, generator/parse.py) with R-CTOR-KEEP's probe for what only substitution spells

- **OCCT examples**

    Trusted, with their own copy constructor: NCollection's containers, `TCollection_AsciiString`, `LDOM_NodeList`. Owners and views:

    - `IntPatch_PrmPrmIntersection_T3Bits::~IntPatch_PrmPrmIntersection_T3Bits()` (defined in the `.cxx`; the class holds `int* p;`, `IntPatch_PrmPrmIntersection_T3Bits.hxx:44`)
    - `IntPatch_Polyhedron::~IntPatch_Polyhedron()` (`{ Destroy(); }`)
    - `const BinObjMgt_Persistent& BinObjMgt_Persistent::GetAsciiString(TCollection_AsciiString& theValue) const` (an owner's `const T&`, `*this`)
    - `BRepGraph_MutGuard<BRepGraphInc::EdgeDef> BRepGraph::EditorView::EdgeOps::Mut(const BRepGraph_EdgeId theEdge)` (an owner by value: built on the heap)
    - `Extrema_ExtCC2d` holds `const Adaptor2d_Curve2d* myC;` and declares no destructor (`Extrema_ExtCC2d.hxx:128`): a view

- **Rule**

    - The copy shares the pointers and the second destructor frees them again: `IntPatch_PrmPrmIntersection_T3Bits(a)`, `BOPAlgo_PaveFiller(pf)`, `BOPAlgo_Builder(b)`, `IntPatch_Polyhedron(p)`, `LocOpe_CSIntersector(a)` crash (double free / use after free; 20 such classes (measured once), identified by their destructors' text, all owners by this rule), and a view's copy that kept only the original would read a freed curve after `ext.Initialize(c2)` (`Extrema_ExtCC2d`, heap-use-after-free).
    - In C++ nobody copies these classes; in Python `Cls(other)` looks harmless.
    - Derived from the headers, so it over-approximates: a destructor in a `.cxx` that frees nothing (`= default`, e.g. `Extrema_GenExtPS`) makes an owner too -- a lost copy constructor, never a crash.
    - Cost of the snapshot: +30 ns per view copy (`Extrema_ExtCC2d(ext)` 69 → 100 ns).

- **Python**

    - **No implicit copy constructor** (reported, category `copy`: 308<!-- count: copy-no-ctor --> classes, OCCT 8.0.1 -- `TopExp_Explorer`, `BOPAlgo_PaveFiller`, `IntPatch_Polyhedron`, every `AIS_InteractiveObject`, `TDF_Data`, …).
    - A `const T&` result comes back by reference (`reference_internal`, `reference` without an owner; e.g. `BinObjMgt_Persistent::GetAsciiString()` returns `*this`).
    - A `T` by value without its own move or copy constructor is built on the heap, `new T(call)` (guaranteed copy elision, `take_ownership`; 20<!-- count: copy-heap --> sites, the `BRepGraph_MutGuard`s, whose move constructor an implicit instantiation does not show).
    - With out-parameters such a member is reported and skipped.
    - An R-ITER element is never copied out.
    - A binder instantiation over owner elements is skipped, and `NCollection_Shared<T>` loses its constructor from a `T` (`bind_NCollection_Shared<T, false>`: `NCollection_Shared<NCollection_EBTree<int, Bnd_Box2d>>`).
    - Every other class holding pointers -- a **view** -- keeps its copy, which keeps the original **and what the original's method slots hold now** (`nanocct::keep_view_arg`, `keep_slots_of`; 528<!-- count: copy-keep-original --> implicit copies): the original's next `Initialize` would drop the argument the copy still points to.

- **Python examples**

    ```python
    import gc
    from nanocct.BinObjMgt import BinObjMgt_Persistent
    from nanocct.BOPAlgo import BOPAlgo_PaveFiller
    from nanocct.Extrema import Extrema_ExtCC2d
    from nanocct.Geom2d import Geom2d_Line
    from nanocct.Geom2dAdaptor import Geom2dAdaptor_Curve
    from nanocct.gp import gp_Dir2d, gp_Pnt2d
    from nanocct.TCollection import TCollection_AsciiString

    try:
        BOPAlgo_PaveFiller(BOPAlgo_PaveFiller())   # an owner: no copy constructor
        copied = True
    except TypeError:
        copied = False
    assert not copied
    persistent = BinObjMgt_Persistent()
    persistent.PutAsciiString(TCollection_AsciiString("hello"))
    assert persistent.GetAsciiString(TCollection_AsciiString()) is persistent   # *this by reference, not a copy

    first = Geom2dAdaptor_Curve(Geom2d_Line(gp_Pnt2d(0, 0), gp_Dir2d(1, 0)), -10.0, 10.0)
    extrema = Extrema_ExtCC2d(first, Geom2dAdaptor_Curve(Geom2d_Line(gp_Pnt2d(0, 1), gp_Dir2d(1, 0)), -10.0, 10.0))
    copy = Extrema_ExtCC2d(extrema)                # a view: the copy keeps the original and its arguments
    del extrema
    gc.collect()
    copy.Perform(first, -10.0, 10.0)
    assert copy.IsDone() and copy.IsParallel()
    ```
### R-IMPLICIT-DEFAULT

- **C++ Idiom**

    Class declaring no constructor

- **OCCT examples**

    - `struct MeshVS_TwoColors` declares no constructor: six bit-fields and `operator==` (`MeshVS_TwoColors.hxx:21`)
    - `struct MathRoot::MultipleGetValueFn` declares no constructor and holds `const math_Vector& mySamples;` (`MathRoot_MultipleUtils.hxx:143`, `MathRoot_MultipleUtils.hxx:145`)

- **Rule**

    - A reference member deletes the implicit constructor without the header saying so (`MathRoot::MultipleGetValueFn`).

- **Python**

    - Implicit default constructor bound only if `std::is_default_constructible_v<T>` (compile-time helper `nanocct_implicit_default_ctor`).

- **Python examples**

    ```python
    from nanocct.MathRoot import MultipleGetValueFn
    from nanocct.MeshVS import MeshVS_TwoColors

    colors = MeshVS_TwoColors()                     # the implicit default constructor
    colors.r1 = 255
    assert colors.r1 == 255
    try:
        MultipleGetValueFn()                        # a reference member: no default constructor
        constructed = True
    except TypeError:
        constructed = False
    assert not constructed
    ```
### R-HASH

- **C++ Idiom**

    `std::hash<T>` specialised by OCCT (specialisations in the `.lxx` part of a header count)

- **OCCT examples**

    `TopoDS_Shape` and its sub-classes, `gp_Pnt`, `TopLoc_Location`, `Quantity_Color`, `TDF_Label`, `TCollection_AsciiString`, …:

    - `size_t std::hash<TopoDS_Shape>::operator()(const TopoDS_Shape& theShape) const`
    - `size_t std::hash<gp_Pnt>::operator()(const gp_Pnt& thePnt) const`
    - `size_t std::hash<TDF_Label>::operator()(const TDF_Label& theLabel) const` (in `TDF_Label.lxx`)
    - `size_t std::hash<TCollection_AsciiString>::operator()(const TCollection_AsciiString& theString) const` (in `TCollection_AsciiString.lxx`)
    - `size_t std::hash<occ::handle<TCollection_HAsciiString>>::operator()(const occ::handle<TCollection_HAsciiString>& theString) const` (on the handle: not bound)

- **Rule**

    - nanobind keeps identity hashing even with `__eq__`; a value-equal shape must hash equal to be a dict key.
    - Classes with `operator==` but no `std::hash` are unhashable instead of identity-hashed (R-UNHASHABLE).
    - `std::hash<handle<TCollection_HAsciiString>>` is a specialisation on the handle, not the class, and is not bound.

- **Python**

    - `__hash__` calling `std::hash<T>`.

- **Python examples**

    ```python
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TCollection import TCollection_AsciiString, TCollection_HAsciiString
    from nanocct.TDF import TDF_Data
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    faces = list(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE))
    again = list(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE))
    assert faces[0] == again[0] and faces[0] is not again[0]
    assert {faces[0]: "first"}[again[0]] == "first"          # a value-equal shape is the same dict key
    assert len(set(faces + again)) == 6
    data = TDF_Data()
    assert hash(data.Root()) == hash(data.Root())            # std::hash<TDF_Label>, in TDF_Label.lxx
    assert hash(TCollection_AsciiString("a")) == hash(TCollection_AsciiString("a"))
    assert TCollection_HAsciiString.__hash__ is object.__hash__   # the handle's specialisation is not bound
    ```
### R-UNHASHABLE

- **C++ Idiom**

    A class whose bound `__eq__` compares against its **own** type and that has no `std::hash`

- **OCCT examples**

    57<!-- count: unhashable --> classes on macOS, OCCT 8.0.1 — `Bnd_Range`, the `NCollection_Vec*`/`Mat*` instantiations, `Graphic3d_MaterialAspect`, `Quantity_Date`, the `LDOM*` family, the position iterators and `NCollection_OccAllocator`:

    - `bool Bnd_Range::operator==(const Bnd_Range& theOther) const`
    - `bool NCollection_Vec3::operator==(const NCollection_Vec3& theOther) const`
    - `bool Graphic3d_MaterialAspect::operator==(const Graphic3d_MaterialAspect& theOther) const`
    - `bool Quantity_Date::operator==(const Quantity_Date& anOther) const`
    - `friend bool operator==(const NCollection_ForwardRangeIterator& theLhs, NCollection_ForwardRangeSentinel)` (another type: would stay hashable; the class is not bound, R-ITERATOR)

- **Rule**

    - nanobind never touches `tp_hash`, and CPython's *"define `__eq__` and `__hash__` becomes `None`"* rule fires only at **type creation** — a `.def()` afterwards does not trigger it (measured), so these classes would keep `object.__hash__` and `a == b` would hold while `hash(a) != hash(b)`: a dict or set lookup by an equal value would miss **without raising**.
    - Unhashable at least fails loudly, and `id()`-keyed dicts still work.
    - pybind11 does this automatically (`add_class_method`); nanobind leaves it to the binding.
    - **Not** applied when the only `operator==` takes another type (OCCT 8.0.1's one such pair is not bound, R-ITERATOR; `tests/test_generator.py` covers the rule with a synthetic pair): `NCollection_ForwardRangeIterator == NCollection_ForwardRangeSentinel` is an exhaustion test, so iterator-to-iterator `==` still falls back to identity and the identity hash stays consistent with it.
    - The stub needs `# type: ignore[assignment]`, as typeshed's own unhashable classes do (`generator/stubs.py`).

- **Python**

    - `cls.attr("__hash__") = nb::none()`, emitted after the `.def` chain.
    - Reported, category `hash`.

- **Python examples**

    ```python
    from nanocct.Bnd import Bnd_Range

    a, b = Bnd_Range(0.0, 1.0), Bnd_Range(0.0, 1.0)
    assert a == b and Bnd_Range.__hash__ is None
    try:
        {a}
        hashable = True
    except TypeError:
        hashable = False
    assert not hashable                              # fails loudly instead of missing silently
    assert {id(a): "a"}[id(a)] == "a"                # id()-keyed dicts still work
    ```
### R-CTOR-KEEP

- **C++ Idiom**

    - A constructor parameter taken by reference or pointer (not a handle, not a primitive) whose class, or a base of it, the object holds a pointer or reference to **anywhere in its layout**, or whose own layout holds a pointer to a class the object's layout holds too (the new object can copy the pointer out of the argument; `_Held.shares_pointees`, constructors only -- see R-METHOD-KEEP).
    - Anywhere in its layout: a data member of any access of the class itself, of every base, or inside a member it holds by value, recursively, with types compared **canonically** (typedefs resolved).
    - A container (`BINDERS`) or `std::` type held by value counts by its type arguments only, a `void *` member as holding any object.

- **OCCT examples**

    - `TDF_ChildIterator::TDF_ChildIterator(const TDF_Label& aLabel, const bool allLevels = false)` (`TDF_ChildIterator(label)` stores the label's `TDF_LabelNode*`: the argument's own layout)
    - `GeomBndLib_Surface::GeomBndLib_Surface(const Adaptor3d_Surface& theSurf)` (`GeomBndLib_Surface`'s `const Adaptor3d_Surface* myAdaptorRef`; also BRepGraph's iterators' `const BRepGraph* myGraph`)
    - `BRepAlgoAPI_Cut::BRepAlgoAPI_Cut(const TopoDS_Shape& S1, const TopoDS_Shape& S2, const BOPAlgo_PaveFiller& aDSF, const bool bFWD = true, const Message_ProgressRange& theRange = Message_ProgressRange())` (`BRepAlgoAPI_Cut`'s base `BRepAlgoAPI_BuilderAlgo` with the typedef'd `BOPAlgo_PPaveFiller myDSFiller`; also every VRML node through `VrmlData_Node::myScene`)
    - `Extrema_GenExtCS::Extrema_GenExtCS(const Adaptor3d_Curve& C, const Adaptor3d_Surface& S, const int NbT, const int NbU, const int NbV, const double Tol1, const double Tol2)` (`Extrema_GenExtCS` through its `Extrema_FuncExtCS myF`, a member held by value)
    - `CPnts_UniformDeflection::CPnts_UniformDeflection(const Adaptor3d_Curve& C, const double Deflection, const double Resolution, const bool WithControl)` (a `void *` member: `CPnts_UniformDeflection::myCurve`, also `TopOpeBRepDS_CurveExplorer::myDS`)

- **Rule**

    - The object keeps the address, and Python would collect the argument under it: `GeomBndLib_Surface(GeomAdaptor_Surface(s)).Add(…)` segfaults, `BRepGraph_CompoundsOfChild(g, g.Topo().Gen().CompoundRefIds(n))` iterates a freed copy (`Size()` 53778742144), `BRepAlgoAPI_Cut(box, cyl, pf)` reads a collected pave filler in `SectionEdges()` and `CPnts_UniformDeflection(GeomAdaptor_Curve(c), …)` a collected adaptor in `Next()` (both segfaults) -- the last two through a base's typedef'd pointer and a `void *` member, which the class's own members compared as spelled miss.
    - Derived from the headers, so it over-keeps where the layout says more than the constructor does: a member of the same type that the constructor does not set, and every `void *` holder (`OSD_File` keeps its `OSD_Path`) -- the argument only lives longer.
    - Methods that store a pointer: R-METHOD-KEEP.
    - A copy of an R-CTOR-KEEP owner keeps the original and what its slots hold (R-COPY): otherwise `Extrema_ExtCC2d(other)` reads the original's collected curve (segfault).
    - A Transient's argument lives as long as its C++ object (R-KEPT), except one that can own the object, which lives as long as its Python object.
    - Not covered: a pointer the object reaches two levels into the argument (`TDF_AttributeIterator(label)` holds `TDF_Attribute*`, reached through the label's node).

- **Python**

    - `nb::keep_alive<1, k>` on the argument (`<0, k>` for a Transient: `nb::new_` hands its extras to `__new__(cls, args…)`, which returns the object, and to a no-op `__init__`, where the nurse is `None` and nanobind ignores it -- `nb_class.h` `new_::execute`, `nb_type.cpp` `keep_alive_py`).
    - A **copy constructor** of a class holding pointers keeps the original, whose pointers the copy shares, and what the original's slots hold (R-COPY) -- a declared one by the rule above, the implicit one through `nanocct_implicit_copy_ctor<T, true>` (528<!-- count: copy-keep-original -->, OCCT 8.0.1; an owner's is not bound at all, R-COPY).
    - A parameter kept because its own layout shares pointees with the object's gets `nanocct::keep_view_arg<1, k>` instead of `keep_alive` (89: it keeps the argument's slots' arguments too).
    - Move constructors are not bound.
    - The layout is read by `_Held` (generator/parse.py) from the class's cursor, the instantiated type's fields (`Type.get_fields()`) and, for an implicit instantiation, its template's bases with the arguments substituted.
    - Layout that exists only as a spelling after template substitution -- a class template's by-value member or base (`Extrema_GGExtPC`'s `TheEPC myExtPC`, `BVH_Box`'s bases) -- is completed by a **layout probe** at the end of the package: `using nanocct_layout_N = …; static_assert(sizeof(nanocct_layout_N) != 0, "");` appended to the umbrella, up to 10 rounds since a probed layout can pend in turn (`_resolve_held_layout`; libclang builds the type even for a private member type, reporting only the access error).
    - A class the package's headers only declare is completed by including its header in the probe -- the header of every class named in the spelling, since a template argument has to be complete too (`NCollection_CellFilter<BRepMesh_CircleInspector>::Cell`).
    - Whatever stays open is reported, category `lifetime`, for the classes whose parameters it leaves undecided -- none (OCCT 8.0.1).
    - 568<!-- count: ctor-keep --> arguments (OCCT 8.0.1).

- **Python examples**

    ```python
    import gc
    from nanocct.Bnd import Bnd_Box
    from nanocct.CPnts import CPnts_UniformDeflection
    from nanocct.Geom import Geom_Circle, Geom_SphericalSurface
    from nanocct.GeomAdaptor import GeomAdaptor_Curve, GeomAdaptor_Surface
    from nanocct.GeomBndLib import GeomBndLib_Surface
    from nanocct.gp import gp_Ax2, gp_Ax3

    bounds = GeomBndLib_Surface(GeomAdaptor_Surface(Geom_SphericalSurface(gp_Ax3(), 2.0)))
    points = CPnts_UniformDeflection(GeomAdaptor_Curve(Geom_Circle(gp_Ax2(), 5.0)), 0.05, 1e-6, True)
    gc.collect()                      # both temporary adaptors live as long as the objects holding their address
    box = Bnd_Box()
    bounds.Add(1e-7, box)
    assert 2.0 <= box.Get().Xmax < 2.5
    radii = set()
    while points.More():
        radii.add(round(points.Point().Distance(gp_Ax2().Location()), 6))
        points.Next()
    assert radii == {5.0}
    ```

    ```python
    import gc
    from nanocct.BOPAlgo import BOPAlgo_PaveFiller
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Cut
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
    from nanocct.gp import gp_Ax2, gp_Dir, gp_Pnt
    from nanocct.NCollection import NCollection_List
    from nanocct.TopoDS import TopoDS_Shape

    box = BRepPrimAPI_MakeBox(2, 2, 2).Shape()
    cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(1, 1, -1), gp_Dir(0, 0, 1)), 0.5, 4).Shape()
    arguments = NCollection_List[TopoDS_Shape]()
    arguments.Append(box)
    arguments.Append(cylinder)
    filler = BOPAlgo_PaveFiller()
    filler.SetArguments(arguments)
    filler.Perform()
    cut = BRepAlgoAPI_Cut(box, cylinder, filler)   # the base's myDSFiller points to the filler
    del filler, arguments
    gc.collect()
    assert cut.IsDone() and cut.SectionEdges().Size() > 0
    ```

    ```python
    import gc
    import sys
    from nanocct.Extrema import Extrema_GenExtCS
    from nanocct.Geom import Geom_Line, Geom_SphericalSurface
    from nanocct.GeomAdaptor import GeomAdaptor_Curve, GeomAdaptor_Surface
    from nanocct.gp import gp_Ax3, gp_Dir, gp_Pnt
    from nanocct.TDF import TDF_ChildIterator, TDF_Data

    data = TDF_Data()
    root = data.Root()
    root.FindChild(1, True)
    root.FindChild(2, True)
    children = TDF_ChildIterator(root, False)   # copies the label's TDF_LabelNode*, so it keeps the label
    del data, root
    gc.collect()
    assert [label.Tag() for label in children] == [1, 2]

    curve = GeomAdaptor_Curve(Geom_Line(gp_Pnt(0, 0, 3), gp_Dir(1, 1, 0)), -10.0, 10.0)
    before = sys.getrefcount(curve)
    extrema = Extrema_GenExtCS(curve, GeomAdaptor_Surface(Geom_SphericalSurface(gp_Ax3(), 2.0)), 20, 20, 20, 1e-7, 1e-7)
    assert sys.getrefcount(curve) - before == 1     # held inside the by-value member myF
    del extrema
    gc.collect()
    assert sys.getrefcount(curve) - before == 0     # released with the object
    ```
### R-METHOD-KEEP

- **C++ Idiom**

    - A method parameter taken by reference or pointer (not a handle, a primitive, a stream, `bytes` or a returned out-parameter) of a class the object can hold the address of by R-CTOR-KEEP's layout rule.
    - For a const method only through a `mutable` member.
    - Static methods never.

- **OCCT examples**

    - `void Extrema_ExtPS::Initialize(const Adaptor3d_Surface& S, const double Uinf, const double Usup, const double Vinf, const double Vsup, const double TolU, const double TolV)` (stores `&S` in `const Adaptor3d_Surface* myS`)
    - `void BOPDS_SubIterator::SetSubSet1(const NCollection_List<int>& theLI)` (one slot per parameter; `SetSubSet2` has its own)
    - `void Extrema_ExtCC2d::Initialize(const Adaptor2d_Curve2d& C2, const double V1, const double V2, const double TolC1 = 1.0e-10, const double TolC2 = 1.0e-10)`
    - `bool Poly_Triangulation::MinMax(Bnd_Box& theBox, const gp_Trsf& theTrsf, const bool theIsAccurate = false) const` (a const method: OCCT 8.0.1 has one mutable pointer member, `RWMesh_TriangulationReader::myLoadingStatistic`, and `Poly_Triangulation`'s `mutable std::atomic<Bnd_Box*> myCachedMinMax` counts by its type argument -- the one const method with a slot)

- **Rule**

    - `Extrema_ExtPS::Initialize(S, …)` stores `&S` and `Perform()` reads it: with the surface dropped, or passed as a temporary (`Extrema_ExtPC().Initialize(BRepAdaptor_Curve(e), …)`), `Perform()` would read freed memory (segfault).
    - `nb::keep_alive<1, k>` would keep every argument of a loop of calls -- and nanobind's duplicate check walks the whole list on each call (84 µs per call after 200 000 distinct arguments, measured) -- while a slot keeps the last one.
    - The rule rests on one assumption: a repeated call to the same declaration stores into the same member (OCCT's setters, `Initialize`, `Load`).
    - Slots are not shared between declarations, so a constructor's argument stays when `Initialize` is called: sharing would release an argument another member still points to.
    - Measured: +8 ns per call on `BOPDS_SubIterator::SetSubSet1` (22 → 30 ns); the one shared table adds about 1 ns (`Extrema_ExtCC2d.Initialize` 39 → 40 ns).
    - Over-keeps where the layout says more than the method does, as R-CTOR-KEEP (a `void *` member holds anything: `TopOpeBRepBuild_Builder` has about 170 slots).
    - A Transient's slots live on its C++ object (R-KEPT), except for an argument that can own the object, and on the Python object of a Transient OCCT created itself.
    - Not covered:
        - An address stored into another object reached through a pointer member is not seen by the layout rule.
        - A method that repoints the object at a pointee of its argument (`TDF_ChildIterator::Initialize(label)`): R-CTOR-KEEP's argument-layout test is for constructors only -- on methods (180 more slots) it mostly matches BRepGraph's editor and the RAII `BRepGraph_MutGuard` it is handed (both hold `BRepGraph*`), so `ops.SetTolerance(ops.Mut(id), t)` would keep the guard in the editor's slot while the guard keeps the editor (R-RESULT-KEEP): a keep-alive cycle, 16 instances leaked and the guard's `markModified()` never run.
    - A copy of the object keeps the original and what its slots hold when it is made (R-COPY): keeping the original alone is not enough, its next call would release the argument the copy points to.

- **Python**

    - `nb::call_policy<nanocct::keep_slot<nanocct_slots, k, n>>()` (`nanocct_call_policies.h`): the argument -- after an implicit conversion the converted object -- goes into slot `n` of the object and releases what the slot held.
    - One slot per (declaration, parameter), numbered per generated file and named by the address of the file's `nanocct::slot_tag<nanocct_slots>::id` and that number (`namespace { struct nanocct_slots {}; }` per file).
    - The slots of all objects are in **one** table for all extension modules (`nanocct::slots()`, a capsule on the `nanocct` package like the MI registry -- a copy made by one toolkit must see what a method of another toolkit stored, R-COPY), found by the object's `PyObject*` (guarded by a mutex, not by the GIL), created on first use and released through `nb::keep_alive_cb`, which nanobind runs after the object's C++ destructor -- the destructor still sees its arguments.
    - An object passed to itself is not stored.
    - Documented nanobind API only (`call_policy`, `keep_alive_cb`).
    - 811<!-- count: method-keep-slots --> parameters in 50<!-- count: method-keep-files --> generated files (OCCT 8.0.1).
    - An in-out parameter that qualifies is reported instead: it is copied into the binding's lambda, so a kept address would dangle anyway (none, OCCT 8.0.1).

- **Python examples**

    ```python
    import gc
    from nanocct.Extrema import Extrema_ExtPS
    from nanocct.Geom import Geom_Plane
    from nanocct.GeomAdaptor import GeomAdaptor_Surface
    from nanocct.gp import gp_Pln, gp_Pnt

    extrema = Extrema_ExtPS()
    extrema.Initialize(GeomAdaptor_Surface(Geom_Plane(gp_Pln())), -10.0, 10.0, -10.0, 10.0, 1e-7, 1e-7)
    gc.collect()                      # the temporary surface lives in the object's slot
    extrema.Perform(gp_Pnt(1, 2, 3))
    assert extrema.IsDone() and extrema.NbExt() == 1
    assert abs(extrema.SquareDistance(1) - 9.0) < 1e-9
    ```

    ```python
    import sys
    from nanocct.BOPDS import BOPDS_SubIterator
    from nanocct.NCollection import NCollection_List

    first, second, other = NCollection_List[int](), NCollection_List[int](), NCollection_List[int]()
    def counts():
        return [sys.getrefcount(first), sys.getrefcount(second), sys.getrefcount(other)]
    before = counts()
    iterator = BOPDS_SubIterator()
    iterator.SetSubSet1(first)
    iterator.SetSubSet2(other)        # its own slot
    iterator.SetSubSet1(second)       # the same slot as the first call: `first` is released
    assert [now - then for now, then in zip(counts(), before)] == [0, 1, 1]
    del iterator
    assert counts() == before         # the slots go with the object
    ```
### R-KEPT

- **C++ Idiom**

    - A Transient the bindings construct -- a declared constructor, the implicit default or copy constructor, a by-value result, a conversion -- whose bound constructors or methods, or a bound base's, keep an argument (R-CTOR-KEEP, R-METHOD-KEEP) that **cannot own the object**.
    - Cannot own the object: no class the argument's type reaches through what it owns -- bases, members by value and behind typed pointers, a container's or `std::` type's elements, a handle's or owning smart pointer's target, recursively -- is a handle whose target is related to the object's class (a base of it, or derived from it).
    - Decided by `parse._cycle_path` at the end of the package (`Param.kept_cpp`), the class decision over all packages in the driver (`_decide_kept_classes`; manifest `keepers` and `kept`, so a partial run sees the other toolkits' classes).

- **OCCT examples**

    - `IntPatch_PolyhedronBVH::IntPatch_PolyhedronBVH(const IntPatch_Polyhedron& thePoly)` (keeps `const IntPatch_Polyhedron* myPoly`)
    - `void IntPatch_PolyhedronBVH::Init(const IntPatch_Polyhedron& thePoly)` (the same through a method)
    - `void Poly_Triangulation::SetCachedMinMax(const Bnd_Box& theBox)` (a bound base's method: `RWMesh_TriangulationSource` derives from `Poly_Triangulation`)
    - `VrmlData_Box::VrmlData_Box(const VrmlData_Scene& theScene, const char* theName, const double sizeX = 2., const double sizeY = 2., const double sizeZ = 2.)` (an argument that can own the object: the scene holds its nodes)
    - `virtual void Standard_Transient::Delete() const` (what `Kept<T>` overrides)

- **Rule**

    - `IntPatch_PolyhedronBVH(poly)` appended to an `NCollection_HSequence`, then `del bvh, poly`: kept by the Python object, the argument goes with it and `Center()` reads the freed polyhedron (segfault on release, heap-use-after-free under ASan); the same through `Init(poly)`.
    - Kept by the C++ object instead, an argument that owns the object would never be released: a `VrmlData_Box` keeping its scene, added to that scene, keeps both alive (`nanobind: leaked` at exit, measured) -- hence the cycle check, derived from the headers like R-CTOR-KEEP.
    - Measured: a slot on a `Kept<T>` within noise (`IntPatch_PolyhedronBVH.Init` 106 → 109 ns: `typeid(*p) == typeid(Kept<Self>)` first, the cross-cast to `kept_base` only for a subclass -- 140 ns without that test); a new Python object of a `Kept<T>` +20 to +30 ns (the registry hit: `Poly_Triangulation()` 89 → 110 ns, `IntPatch_PolyhedronBVH(poly)` 275 → 304 ns), an existing one +2 ns; generation time unchanged (46 s).
    - Not covered (residual):
        - A Transient OCCT creates itself keeps method arguments by its Python object.
        - A cycle through a subclass of a member's type, a `void *` or a class the headers only declare is not seen -- it leaks, never crashes.
        - A `Kept<T>` handed out by nanobind's own casters as a base-class `T*`/`T&` shows the base type, as an unbound OCCT subclass does.
        - One held by a C++ static at exit cannot release (`nanobind: leaked` at exit -- the safe side).
        - The worker-thread queue is tested by a prototype only (`std::thread`), not with an OCCT worker thread: no OCCT path reachable from Python drops a handle on one (BRepMesh drops an outdated triangulation on the calling thread, BRepMesh_ModelPreProcessor.cxx:345).

- **Python**

    - Constructed as **`nanocct::Kept<T>`** (`nanocct_lifetime.h`): `T` itself at offset 0 plus a `kept_base` holding the object's slots -- R-METHOD-KEEP's slots and the constructor's kept arguments move from the table onto the C++ object (`keep_slot<…, Self, true>`, `keep_arg<…>`; 106<!-- count: kept-slots-cpp --> method and 31<!-- count: kept-ctor-args-cpp --> constructor parameters), so they live exactly as long as the C++ object, whoever drops it last.
    - `Kept<T>` overrides `Standard_Transient::Delete()` (the only definition in OCCT 8.0.1, Standard_Transient.hxx:134): it takes the slots out under the slot table's mutex, runs `T::Delete()` and releases afterwards -- `~kept_base` runs before `~T`, whose destructor may still read them. The mutex is looked up when the object is constructed (by a binding, with the GIL held): `Delete()` runs wherever the last handle goes, and the first lookup in a toolkit imports `nanocct`.
    - A release on a thread with a Python thread state takes the GIL (`nb::gil_scoped_acquire`); on an OCCT worker thread (no thread state) it never waits -- the references go into a per-module queue that one `Py_AddPendingCall` drains on the main thread (waiting deadlocks while the Python thread that started the algorithm holds the GIL, measured in a prototype); after finalisation nothing is released.
    - Python never sees the subclass: `nanocct::register_kept<T>` enters `typeid(Kept<T>)` into the MI registry with `T` as the type to show, which the handle caster looks up anyway.
    - An argument that **can** own the object stays kept by the Python object, reported with the path (category `kept`, 45, OCCT 8.0.1: every VRML node's scene through `VrmlData_Scene::myLstNodes` (`VrmlData_WorldInfo`'s through `VrmlData_Scene::myWorldInfo`), `TDocStd_Owner::SetDocument` through `TDF_Data::myRoot`, `MeshVS_MeshOwner`'s selectable object, OpenGl's shader manager and workspace, Graphic3d's structures, layers and structure manager, the original of a `Graphic3d_ClipPlane` copy through `Graphic3d_ClipPlane::myNextInChain`, the subviews of `V3d_View` and `Graphic3d_CView`, `BRepGraph_LayerHistory::Absorb`).
    - Not constructed as `Kept<T>` when the subclass cannot be formed -- a final class, a private destructor, a final `Delete()`, a multiple-inheritance H-collection -- or its own vtable would name a virtual function no OCCT library exports (`Class.virtual_symbols` against every toolkit's symbols: `new T` uses T's vtable from the library, `Kept<T>` its own): reported, kept by the Python object (none, OCCT 8.0.1).
    - 54<!-- count: kept-classes --> classes (OCCT 8.0.1), 47<!-- count: kept-own --> by their own members, 7<!-- count: kept-base --> by a base's (`RWMesh_TriangulationSource` and `RWGltf_GltfLatePrimitiveArray` through `Poly_Triangulation::SetCachedMinMax`, BinXCAF's two drivers through BinL's).

- **Python examples**

    ```python
    import gc
    import sys
    from nanocct.Geom import Geom_SphericalSurface
    from nanocct.GeomAdaptor import GeomAdaptor_Surface
    from nanocct.gp import gp_Ax3
    from nanocct.IntPatch import IntPatch_Polyhedron, IntPatch_PolyhedronBVH
    from nanocct.NCollection import NCollection_HSequence
    from nanocct.Standard import Standard_Transient

    poly = IntPatch_Polyhedron(GeomAdaptor_Surface(Geom_SphericalSurface(gp_Ax3(), 2.0)), 6, 6)
    before = sys.getrefcount(poly)
    bvh = IntPatch_PolyhedronBVH(poly)          # keeps &poly
    centres = [bvh.Center(i, axis) for i in range(bvh.Size()) for axis in range(3)]
    sequence = NCollection_HSequence[Standard_Transient]()
    sequence.Append(bvh)                        # OCCT holds the BVH now
    del bvh
    gc.collect()
    assert sys.getrefcount(poly) - before == 1  # kept by the C++ object, not by its dropped Python object
    again = sequence.Value(1)
    assert type(again).__name__ == "IntPatch_PolyhedronBVH"   # never the subclass
    assert [again.Center(i, axis) for i in range(again.Size()) for axis in range(3)] == centres
    del again
    sequence.Clear()                            # the last handle goes: Delete() releases the polyhedron
    assert sys.getrefcount(poly) - before == 0
    ```

    ```python
    import gc
    import sys
    from nanocct.VrmlData import VrmlData_Box, VrmlData_Scene

    scene = VrmlData_Scene()
    before = sys.getrefcount(scene)
    box = VrmlData_Box(scene, "box", 1.0, 2.0, 3.0)
    scene.AddNode(box)                # the scene holds the node: the scene can own it
    assert sys.getrefcount(scene) - before == 1   # kept by the node's Python object
    del box
    gc.collect()
    assert sys.getrefcount(scene) - before == 0   # not by its C++ object, which the scene holds: no cycle
    ```
### R-RESULT-KEEP

- **C++ Idiom**

    - A result by value, or a `const T&` that R-RESULT copies, of a class whose layout holds pointers (R-CTOR-KEEP's layout walk; no exemption for a class with a destructor).
    - An argument the call writes into -- a non-const reference or pointer to such a class.
    - An R-ITER element of such a class.
    - Not a handle (its Transient's Python object may already exist and would collect the keep-alives of every call) and not a `std::` type (a type caster's copy).

- **OCCT examples**

    - `[[nodiscard]] const TopoView& BRepGraph::Topo() const` (copied: `BRepGraph::TopoView` holds `BRepGraph*`)
    - `StreamBuffer Message_Messenger::Send(Message_Gravity theGravity)` (`Message_Messenger::StreamBuffer` and `Message_ProgressRange` use their pointer *in* the destructor: `~StreamBuffer() { Flush(); }`, `~Message_ProgressRange() { Close(); }`)
    - `static Message_ProgressRange Message_ProgressIndicator::Start(const occ::handle<Message_ProgressIndicator>& theProgress)` (a static method)
    - `const VrmlData_Scene& VrmlData_Node::Scene() const` (`VrmlData_Scene` cannot be copied: by reference)
    - `const XCAFPrs_DocumentNode& XCAFPrs_DocumentExplorer::Current() const` (an R-ITER element)

- **Rule**

    - The result points into what produced it: `g.Topo()` (`BRepGraph::TopoView`, holding `BRepGraph*`) would read the collected graph once `g` is gone (segfault); `doc.Main()` after the document and `TDF_Data().Root()` would read freed label nodes.
    - Derived from the layout, so it over-keeps where a class only owns what it points to (an `NCollection_PackedMap<int>` copy keeps its producer) -- the producer only lives longer.
    - +12 ns per call (`g.Topo()`: 35 → 48 ns), +5 ns for the slots (42 → 47 ns).
    - Not covered:
        - A handle result of a pointer-holding Transient other than R-OWNER's (OCCT creates it, so it is no `nanocct::Kept<T>`, R-KEPT).
        - A public data member of such a class assigned from Python (R-FIELD).

- **Python**

    - `nb::call_policy<nanocct::keep_view<R, false, nurse, elem, patients…>>()` (`nanocct_call_policies.h`): the result (`nurse` 0; `elem`: its position in an out-parameter tuple) or the argument written into (`nurse` k) keeps `self` for a method, and every argument whose class, or a pointer in whose own layout, the result's layout can hold -- also for a static method or a free function (`Message_ProgressIndicator::Start_s(progress)` keeps `progress`) -- with `nb::keep_alive_obj`, and what those objects' method slots hold now (`nanocct::keep_view_of`, R-COPY: a producer's next `Initialize` must not free what the result points to).
    - A fresh result holds one call's arguments; an argument written into keeps them for good, nanobind skipping duplicates.
    - R-ITER: `nanocct_def_iter<T, true>`, every element keeps the iterated object.
    - Decided after the layout probe (`parse._note_views`, `_decide_views`); a dependent spelling of a 7c walk is probed as the class behind it (`std::remove_cv_t<std::remove_pointer_t<std::remove_reference_t<…>>>`: `NCollection_Array1<T>::const_reference` hides a reference).
    - Only a fresh object collects producers, so no keep-alive cycle can form: a `const T&` that comes back by reference (a class that cannot be copied, decided at compile time in `keep_view`, or `[not_value_copy]`) may be an object Python already has -- `VrmlData_Node::Scene()` hands back the scene the node keeps, which would then keep the node: both would leak -- and keeps none.
    - An argument written into whose class the object keeps elsewhere (a kept constructor or method parameter of that class or a base) does not keep the object back either, reported, category `lifetime` (91<!-- count: lifetime-lines -->, OCCT 8.0.1, 56<!-- count: lifetime-topopebrepbuild --> of them TopOpeBRepBuild's over-kept `void *` holders).
    - 207<!-- count: result-keep-results --> results and 308<!-- count: result-keep-args --> arguments written into (OCCT 8.0.1); 20<!-- count: iter-keeps --> iterators whose elements keep what they point into, R-OWNER's included.

- **Python examples**

    ```python
    import gc
    import sys
    from nanocct.BRepGraph import BRepGraph
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.Message import Message_Gravity, Message_Messenger

    graph = BRepGraph()
    graph.Clear()
    graph.Shapes().Add(BRepPrimAPI_MakeBox(10.0, 20.0, 30.0).Shape())
    topo = graph.Topo()               # a copy holding BRepGraph*: keeps the graph
    del graph
    gc.collect()
    assert (topo.Vertices().Nb(), topo.Edges().Nb(), topo.Faces().Nb()) == (8, 12, 6)

    messenger = Message_Messenger()
    before = sys.getrefcount(messenger)
    buffer = messenger.Send(Message_Gravity.Message_Info)
    assert sys.getrefcount(messenger) - before == 1   # ~StreamBuffer flushes into the messenger
    del buffer
    assert sys.getrefcount(messenger) - before == 0
    ```

    ```python
    import sys
    from nanocct.VrmlData import VrmlData_Box, VrmlData_Scene

    scene = VrmlData_Scene()
    box = VrmlData_Box(scene, "box", 1.0, 2.0, 3.0)
    before = sys.getrefcount(box)
    same = box.Scene()
    assert same is scene                         # by reference: the object Python already has
    assert sys.getrefcount(box) == before        # it keeps no producer, so no scene <-> node cycle
    ```

    ```python
    import sys
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeSphere
    from nanocct.TCollection import TCollection_ExtendedString
    from nanocct.TDocStd import TDocStd_Document
    from nanocct.XCAFDoc import XCAFDoc_DocumentTool
    from nanocct.XCAFPrs import XCAFPrs_DocumentExplorer

    document = TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
    tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
    tool.AddShape(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), False)
    tool.AddShape(BRepPrimAPI_MakeSphere(1.0).Shape(), False)
    explorer = XCAFPrs_DocumentExplorer(document, 0)
    before = sys.getrefcount(explorer)
    nodes = list(explorer)
    assert [node.Id.ToCString() for node in nodes] == ["0:1:1:1.", "0:1:1:2."]
    assert sys.getrefcount(explorer) - before == 2   # every element keeps the explorer
    ```
### R-OWNER

#### Case 1: an OCAF object, its owner known by its type

- **C++ Idiom**

    - An OCAF object whose owner is known by its type: a `TDF_Label` and every `TDF_Attribute` point into the `TDF_LabelNode` tree of a `TDF_Data`, whose root carries a `TDocStd_Owner` with a raw pointer to the `TDocStd_Document`.
    - Every result, tuple element (out-handles), argument written into, R-ITER element and binder element (7a) of such a type -- also a handle of one, or one of the ten NCollection kinds holding them -- gets the owners, instead of R-RESULT-KEEP's producers.

- **OCCT examples**

    - `bool TDF_Label::FindAttribute(const Standard_GUID& anID, occ::handle<TDF_Attribute>& anAttribute) const` (out-handles: `FindAttribute`)
    - `void XCAFDoc_ShapeTool::GetFreeShapes(NCollection_Sequence<TDF_Label>& FreeLabels) const` (an argument written into: `NCollection_Sequence<TDF_Label>`)
    - `static occ::handle<XCAFDoc_ShapeTool> XCAFDoc_DocumentTool::ShapeTool(const TDF_Label& acces)` (an attribute handle)
    - `TDF_Label XCAFDoc_ShapeTool::AddShape(const TopoDS_Shape& S, const bool makeAssembly = true, const bool makePrepare = true)` (a label result)
    - `static occ::handle<TDocStd_Document> TDocStd_Document::Get(const TDF_Label& L)` (the way back to the document)

- **Rule**

    - The owner is not in the layout: an XCAF tool (`ShapeTool_s(doc.Main())`) and every label it hands out (`AddShape`, 47 such methods in TKXCAF, measured once) would point into a document collected under them (segfaults).
    - Keeping only the producer would also tie each label to its tool, and `lbl = tool.NewShape(); tool.SetShape(lbl, s)` -- the tool keeping the label (R-METHOD-KEEP) -- would be a keep-alive cycle leaking the whole document.
    - The document too, not only the data: `TDocStd_Document.Get_s(label)` follows the owner attribute's raw pointer.
    - Bounded: the owners' Python objects are unique per C++ object, so repeated results add no records.
    - +60 ns per call (`label.FindChild`: 40 → 100 ns).
    - Not covered:
        - An attribute created in Python and attached later (`label.AddAttribute(attr)`) keeps nothing.
        - A `TDF_Data` kept by a C++ `TDF_Transaction` after its document is gone has a dangling owner pointer, which the rule then follows (`TDocStd_Owner::GetDocument`, as OCCT itself would).

- **Python**

    - `nanocct::owners<T>` (`nanocct_lifetime.h`): `keep(nurse, value)` keeps the `TDF_Data` and, when it has one, the `TDocStd_Document`, through their handles' Python objects (`nb::keep_alive_obj`); a handle or container recurses into its elements.
    - The generator's verdict (`parse._owned`, by name: `TDF_Label`, `TDF_Data`, a `TDF_Attribute` or derived, the containers) is the `Owned` argument of `keep_view`, which `static_assert`s it against the trait.
    - The definitions (`nanocct_ocaf.h`, `struct ocaf_owners`) are complete only where the emitter includes that header, so a file applying the rule without it does not compile, and the header's TDF/TDocStd names reach R-LINK.
    - 448<!-- count: owner-results --> results, 17<!-- count: owner-tuple --> tuple elements, 114<!-- count: owner-args --> arguments written into, in 19<!-- count: owner-files --> generated files (OCCT 8.0.1).

- **Python examples**

    ```python
    import gc
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TCollection import TCollection_ExtendedString
    from nanocct.TDocStd import TDocStd_Document
    from nanocct.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ShapeTool

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    tool = XCAFDoc_DocumentTool.ShapeTool_s(TDocStd_Document(TCollection_ExtendedString("XmlXCAF")).Main())
    gc.collect()                      # the tool keeps the document it points into
    label = tool.AddShape(box, False)
    del tool
    gc.collect()                      # the label keeps the data and the document, not the tool
    assert XCAFDoc_ShapeTool.GetShape_s(label).IsSame(box)
    assert TDocStd_Document.Get_s(label).Main().Depth() == 1
    ```

    ```python
    import gc
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.NCollection import NCollection_Sequence
    from nanocct.TCollection import TCollection_ExtendedString
    from nanocct.TDF import TDF_Label
    from nanocct.TDocStd import TDocStd_Document
    from nanocct.TNaming import TNaming_NamedShape
    from nanocct.XCAFDoc import XCAFDoc_DocumentTool

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    document = TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
    tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
    tool.AddShape(box, False)
    labels = NCollection_Sequence[TDF_Label]()
    tool.GetFreeShapes(labels)        # the sequence written into keeps the owners of its labels
    found, named = labels.Value(1).FindAttribute(TNaming_NamedShape.GetID_s())   # the out-handle too
    del document, tool
    gc.collect()
    assert labels.Length() == 1 and found and named.Get().IsSame(box)
    ```

#### Case 2: an object whose layout holds a label

- **C++ Idiom**

    A class that is no OCAF type itself but whose layout holds a `TDF_Label`, given an OCAF object as a handle argument it takes labels from: a `TDocStd_Document`, a `TDF_Data`, a `TDF_Attribute` (or derived)

- **OCCT examples**

    - `XCAFPrs_DocumentExplorer::XCAFPrs_DocumentExplorer(const occ::handle<TDocStd_Document>& theDocument, const XCAFPrs_DocumentExplorerFlags theFlags, const XCAFPrs_Style& theDefStyle = XCAFPrs_Style())` (its `NCollection_DynamicArray<XCAFPrs_DocumentNode> myNodeStack` holds labels; the header only forward-declares the document)
    - `void XCAFPrs_DocumentExplorer::Init(const occ::handle<TDocStd_Document>& theDocument, const TDF_Label& theRoot, const XCAFPrs_DocumentExplorerFlags theFlags, const XCAFPrs_Style& theDefStyle = XCAFPrs_Style())`
    - `XCAFDoc_AssemblyIterator::XCAFDoc_AssemblyIterator(const occ::handle<TDocStd_Document>& theDoc, const int theLevel = INT_MAX)`
    - `bool STEPCAFControl_Reader::Transfer(const occ::handle<TDocStd_Document>& doc, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `TDF_DeltaOnAddition::TDF_DeltaOnAddition(const occ::handle<TDF_Attribute>& anAtt)`

- **Rule**

    - The labels point into the `TDF_LabelNode` tree of the argument's document, and nothing keeps that document: the handle argument is not stored, or stored next to labels that need the document too. `XCAFPrs_DocumentExplorer(doc, 0)` iterated after `del doc` reads the freed label tree (a segfault, `tests/test_lifetime.py`).
    - Decided from the layout, not by name: the class's layout (its members, its bases', what it holds by value, a container's elements) holds a `TDF_LabelNode*`, the pointer inside every `TDF_Label`. Decided at the end of the package, once the layout probe completed every layout.
    - Not for an OCAF type itself: Case 1 keeps its owners already, and an attribute keeping another attribute could close a cycle.
    - A forward declaration is enough to recognise the document (`_derives_from`), which the headers holding the labels mostly have.

- **Python**

    - The object keeps such an argument: `keep_alive` for a constructor, a slot for a method (R-METHOD-KEEP: a second `Init(doc)` replaces the first document), the `nanocct::Kept<T>` slots for a Transient (R-KEPT, with its cycle guard).
    - Applies to `XCAFPrs_DocumentExplorer`, `XCAFDoc_AssemblyIterator`, `XCAFDoc_AssemblyGraph`, `STEPCAFControl_Reader`/`Writer` (`Transfer`, `Perform`), the `TDF`, `TDataStd` and `TNaming` deltas, `TDF_DataSet.AddAttribute`, `TDF_RelocationTable.SetRelocation`, `TNaming_Identifier` and `TNaming_Name` (OCCT 8.0.1).

- **Python examples**

    ```python
    import gc
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TCollection import TCollection_ExtendedString
    from nanocct.TDocStd import TDocStd_Document
    from nanocct.XCAFDoc import XCAFDoc_DocumentTool
    from nanocct.XCAFPrs import XCAFPrs_DocumentExplorer

    document = TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
    tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
    for i in range(3):
        tool.AddShape(BRepPrimAPI_MakeBox(1.0 + i, 2.0, 3.0).Shape(), False)
    del tool
    explorer = XCAFPrs_DocumentExplorer(document, 0)
    del document
    gc.collect()                      # the explorer keeps the document its labels point into
    tags = []
    while explorer.More():
        tags.append(explorer.Current().Label.Tag())
        explorer.Next()
    assert tags == [1, 2, 3]
    ```
### R-ALLOCATOR

- **C++ Idiom**

    A class that holds an NCollection allocator (`occ::handle<NCollection_IncAllocator>` or another `NCollection_BaseAllocator`, its own member or a base's) and hands out Transients it may have placed in that allocator

- **OCCT examples**

    - `const IMeshData::IFaceHandle& BRepMeshData_Model::GetFace(const int theIndex) const override` (`IFaceHandle` = `occ::handle<IMeshData_Face>`; the model creates its faces with `new (myAllocator) BRepMeshData_Face(theFace, myAllocator)`, `BRepMeshData_Model.cxx:51`)
    - `const IMeshData::IEdgeHandle& BRepMeshData_Model::AddEdge(const TopoDS_Edge& theEdge) override`
    - `DEFINE_INC_ALLOC` (`IMeshData_Types.hxx:54`): an `operator new` into the allocator and an `operator delete` that does nothing

- **Rule**

    - The object's memory goes with the allocator, not with its handle: releasing the last handle frees nothing (the no-op `operator delete`), and the producer's destructor releases the allocator and with it every object placed there. A face kept from `model.GetFace(0)` after `del model` points into freed memory (a bus error under MallocScribble on macOS, an access violation on Windows; `tests/test_lifetime.py`).
    - Decided from the producer's layout -- it holds an allocator -- because the result type does not say it: Python sees the face as the interface `IMeshData_Face`, the allocator-placed `BRepMeshData_*` classes are not bound (their `operator new` takes an allocator).
    - Where such a producer hands out an object from the ordinary heap, the producer lives as long as the result -- longer than needed, never a crash (candidates: `BOPAlgo_Builder::Context()`, the `History()` of the BOPAlgo/BRepAlgoAPI algorithms).
    - Not for a type descriptor (`DynamicType()`, `Standard_Type` is static) or an allocator itself (`Allocator()`: not placed in its own memory).

- **Python**

    - The result keeps the producer alive (`nanocct::KeepOwnerUnlessSelf`, as R-RESULT case 1): a handle result, or a pointer or reference to a Transient, of a non-static method of such a class.
    - The chain holds: a wire from a face keeps the face, the face keeps the model.

- **Python examples**

    ```python
    import gc
    from nanocct.BRepMesh import BRepMesh_ModelBuilder
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeCone
    from nanocct.IMeshTools import IMeshTools_Parameters

    params = IMeshTools_Parameters()
    params.Deflection, params.Angle = 0.1, 0.5
    model = BRepMesh_ModelBuilder().Perform(BRepPrimAPI_MakeCone(1.0, 0.5, 2.0).Shape(), params)
    face = model.GetFace(0)                  # placed in the model's allocator
    del model
    gc.collect()                             # the face keeps the model, and with it its own memory
    assert face.WiresNb() == 1
    ```

### R-BYTES

- **C++ Idiom**

    A `const uint8_t*` input-buffer parameter immediately followed by its length, on a member listed in `overrides.toml [bytes] members`

- **OCCT examples**

    - `static TCollection_AsciiString FSD_Base64::Encode(const uint8_t* theData, const size_t theDataLen)`
    - `WNT_HIDSpaceMouse::WNT_HIDSpaceMouse(unsigned long theProductId, const uint8_t* theData, size_t theSize)` (a constructor that keeps the pointer)
    - `static void NCollection_UtfString::strCopy(uint8_t* theStrDst, const uint8_t* theStrSrc, const int theSizeBytes)` (private: not listed)
    - `bool Image_AlienPixMap::Load(const uint8_t* theData, const size_t theLength, const TCollection_AsciiString& theFileName)` (an image file from memory)
    - `static size_t FSD_Base64::Decode(uint8_t* theDecodedData, const size_t theDataLen, const char* theEncodedStr, const size_t theStrLen)` (a non-const output buffer: stays unbound)

- **Rule**

    - Without it the whole method is unbindable — a raw pointer to a primitive — which would keep `FSD_Base64::Encode` out.
    - Listed rather than inferred because "the next integer is the length" is a convention and not a type, so each entry is read in the header once.
    - Only the **const** form: a non-const `uint8_t*` is an output buffer the caller sizes and owns, which `bytes` cannot express, so such an overload stays unbound and the report still says why.
    - **Constructors too**: `_ctor` (parse.py) passes the qualified name, the emitter binds a placement `__init__` lambda and adds `nb::keep_alive<1, k>` for every `bytes` parameter, because an object may keep the pointer -- `WNT_HIDSpaceMouse` stores `myData(theData)` (`WNT_HIDSpaceMouse.cxx:154`).
    - A Transient constructor with a `bytes` parameter is refused at generation (the `nb::new_` numbering is not verified).
    - A header scan in `tests/test_generator.py` keeps the list complete: 3 members (OCCT 8.0.1), `NCollection_UtfString::strCopy` excluded as private.

- **Python**

    - One `nb::bytes` parameter.
    - The length is dropped from the signature and passed as `theData.size()`.

- **Python examples**

    ```python
    import base64
    import numpy as np
    from nanocct.FSD import FSD_Base64

    data = bytes(range(256))
    assert FSD_Base64.Encode_s.__doc__.startswith("Encode_s(theData: bytes) ->")   # the length is gone
    encoded = FSD_Base64.Encode_s(data).ToCString()
    assert encoded == base64.b64encode(data).decode()
    assert bytes(np.asarray(FSD_Base64.Decode_s(encoded, len(encoded)))) == data
    assert "theDecodedData" not in FSD_Base64.Decode_s.__doc__                       # the output-buffer overload
    ```

    ```python
    from nanocct.Image import Image_AlienPixMap, Image_Format, Image_PixMap
    from nanocct.TCollection import TCollection_AsciiString

    pixmap = Image_PixMap()
    assert pixmap.InitZero(Image_Format.Image_Format_BGR, 5, 3)
    source = Image_AlienPixMap()
    assert source.InitCopy(pixmap)
    ok, png = source.Save__bytes(TCollection_AsciiString(".png"))
    assert ok and png.startswith(b"\x89PNG")

    image = Image_AlienPixMap()
    assert image.Load(png, TCollection_AsciiString("memory.png"))   # Load(const uint8_t*, size_t, name)
    assert (image.SizeX(), image.SizeY()) == (5, 3)
    ```
### R-ARRAY-PTR

- **C++ Idiom**

    An integer count immediately followed by a `const T*` to a class that is really an array of T taken by its first element, on a member listed in `overrides.toml [array] members`

- **OCCT examples**

    `VrmlData_Coordinate`, `VrmlData_Color`, `VrmlData_Normal`, `VrmlData_TextureCoordinate` (their scene constructors), `VrmlData_ArrayVec3d::SetValues`, `VrmlData_Color::SetColors`, `VrmlData_TextureCoordinate::SetPoints` -- 7 members, all storing the pointer:

    - `VrmlData_Coordinate::VrmlData_Coordinate(const VrmlData_Scene& theScene, const char* theName, const size_t nPoints = 0, const gp_XYZ* arrPoints = nullptr)`
    - `void VrmlData_ArrayVec3d::SetValues(const size_t nValues, const gp_XYZ* arrValues)` (`myArray = arrValues`)
    - `void VrmlData_TextureCoordinate::SetPoints(const size_t nPoints, const gp_XY* arrPoints)`
    - `bool Graphic3d_Buffer::Init(const int theNbElems, const Graphic3d_Attribute* theAttribs, const int theNbAttribs)` (the same idiom, not listed: its `NCollection_Array1<Graphic3d_Attribute>` overload covers it, Excluded.md)

- **Rule**

    - Bound as a class pointer (R-PTR-NULL) the parameter takes one object, and a count above 1 makes OCCT read past it (AddressSanitizer: heap-buffer-overflow).
    - Listed rather than inferred, as for R-BYTES: a count next to a pointer is a convention, not a type (`Graphic3d_TransformPers(..., theViewportHeight, gp_Pnt* theAnchor)` is one point).
    - The object keeps the pointer, so the elements are copied into memory that lives as long as the object: the allocator of the object the entry names -- for the VrmlData nodes their scene's, where OCCT's own reader puts the arrays (`VrmlData_ArrayVec3d::AllocateValues`, `VrmlData_Geometry.cxx`). A node keeps its scene (R-CTOR-KEEP), so the copy outlives every Python variable.
    - A copy, unlike C++: changing the Python sequence or its elements after the call does not change the node.
    - A repeated `SetColors`/`SetPoints`/`SetValues` leaves the previous array in the scene's allocator until the scene goes, as OCCT's reader does.

- **Python**

    - One sequence parameter of the element type (`Sequence[gp_XYZ]`, `std::vector<T>` in the binding); the count is dropped and passed as its length.
    - A null default is the empty sequence, which passes `nullptr` as the C++ default does.
    - `nanocct::allocator_copy` (`nanocct_lifetime.h`) makes the copy; the sequence itself is not kept.

- **Python examples**

    ```python
    import gc
    from nanocct.gp import gp_XY, gp_XYZ
    from nanocct.VrmlData import VrmlData_Color, VrmlData_Coordinate, VrmlData_Scene, VrmlData_TextureCoordinate

    scene = VrmlData_Scene()
    points = [gp_XYZ(1, 2, 3), gp_XYZ(4, 5, 6), gp_XYZ(7, 8, 9)]
    coordinates = VrmlData_Coordinate(scene, "c", points)       # the count is len(points)
    assert coordinates.Length() == 3 and coordinates.Coordinate(2).Z() == 9.0
    points[2].SetZ(0.0)                                         # a copy: the node does not see it
    assert coordinates.Coordinate(2).Z() == 9.0
    assert VrmlData_Coordinate(scene, "empty").Length() == 0    # the C++ default: no array

    colors = VrmlData_Color(scene, "rgb")
    colors.SetColors([gp_XYZ(1, 0, 0), gp_XYZ(0, 1, 0)])
    assert colors.Length() == 2 and colors.Color(1).Green() == 1.0
    assert VrmlData_TextureCoordinate(scene, "uv", [gp_XY(0, 0), gp_XY(1, 0.5)]).Length() == 2

    del scene, points
    gc.collect()
    assert coordinates.Coordinate(1).X() == 4.0                 # in the scene's allocator; the node keeps the scene
    ```
### R-VIEW

- **C++ Idiom**

    A class holding a large contiguous array, listed in `overrides.toml [views] classes`, or an `NCollection` array whose element type is a packed run of numpy scalars

- **OCCT examples**

    `Poly_ArrayOfNodes`, `Poly_ArrayOfUVNodes`, `Image_PixMap`, `NCollection_Buffer`:

    - `Poly_ArrayOfNodes& Poly_Triangulation::InternalNodes()`
    - `Poly_ArrayOfUVNodes& Poly_Triangulation::InternalUVNodes()`
    - `uint8_t* Image_PixMap::ChangeRow(size_t theRow)` (rows of `SizeRowBytes()`, possibly bottom-up)
    - `static occ::handle<NCollection_Buffer> FSD_Base64::Decode(const char* theStr, const size_t theLen)` (returns an `NCollection_Buffer`)
    - `NCollection_Array1<NCollection_Vec3<float>>& Poly_Triangulation::InternalNormals()` (an `NCollection` array of packed scalars)

- **Rule**

    - **Which** class gets views is data, so it is an override list.
    - **How** each builds its view is a `nanocct_def_views<T>` specialisation in `src/cpp/common/nanocct_views.h`, because every case has runtime branches a config file cannot carry — `Poly_ArrayOfNodes`' dtype follows `IsDoublePrecision()` (stride 24 `gp_Pnt` → float64, 12 `NCollection_Vec3<float>` → float32), while `Poly_Triangulation`'s normals are *always* float32 because `InternalNormals()` is an ordinary `NCollection_Array1`, not an aliased array.
    - **`__array__`, not `…Array()` accessors**: an accessor such as `ValuesArray()` would read like an OCCT method and not be one — OCCT has dozens of method names ending in `…Array`, and `Geom_BSplineCurve.WeightsArray()` returns an OCCT array.
    - **The protocol, measured on numpy 2.5.3**: numpy casts a requested `dtype` itself (and raises itself when `copy=False` makes that impossible), but *trusts* `copy=True` — what `np.array(obj)` passes — and a view returned for it stays shared, so the copy is `__array__`'s job.
    - `ndarray::cast` keeps the static type, so the stub still names the exact dtype, and numpy's stubs carry it through `np.asarray`.
    - The generic `NCollection_Array1[T]` has no `__array__`, so `np.asarray` on it is `NDArray[Any]`, not an error.
    - A name listed without a specialisation does not link, and `tests/test_views.py` turns that into a test failure instead.
    - **The return type is a numpy array, not a buffer object**: the consumer applies numpy operations on arrival, so a buffer would only be `np.asarray`'d — and it is not free anyway, since nanobind's framework-agnostic `nb::ndarray<double, ndim<2>, c_contig>` **as a return type produces a bare `PyCapsule`** (measured — no `memoryview`, no `__dlpack__`; that form is meant for parameters), while a real buffer-protocol object would mean hand-rolling a `Py_bf_getbuffer` slot per class for no gain.
    - `reference_internal` ties the view's lifetime to the owner — verified on the stable ABI with a destructor counter: dropping every Python reference to the owner leaves the view valid and destroys the owner exactly when the last view goes.
    - `Image_PixMap` is the case that settles the argument: its rows are padded, so the view needs a stride from `SizeRowBytes()` (measured — a FreeImage-loaded 5-pixel-wide RGB image has 16, not 15, and a shape-only view would silently shear it), and its rows may run bottom-up, so it starts at `Row(0)` with a **negative** row stride and `view[y, x]` stays `PixelColor(x, y)` whatever `IsTopDown()` says.
    - The generic containers are the other half and need no generator change at all: one `if constexpr` in the hand-written `NCollection` binder over a table of element types (`src/cpp/common/nanocct_elem_view.h`) covers 47 bound instantiations (OCCT 8.0.1, the nine `NCollection_Vec2/3/4` arrays included), and every entry in that table `static_assert`s that the type really is N packed scalars with no padding and no vtable, so an OCCT layout change is a compile error rather than a wrong array.
    - `generator/stubs.py` lifts a concrete container's `__array__` (with its docstring) out of the class that otherwise collapses into the generic, and adds the numpy imports nanobind's stubgen only adds for signatures it infers itself.
    - Measured: **903× faster** than the per-value loop on a 5 153-node face (1.1 µs against 1.0 ms), and one `cp312-abi3` wheel — a byte-identical `_TKMath.abi3.so` in all three venvs — gives identical results on Python 3.12, 3.13 and 3.14.
    - An NCollection container's view counts as one of its views: a call that would reallocate the array raises `BufferError` while the view lives (R-VIEW-GUARD).
    - The per-class views of nanocct_views.h are not counted.

- **Python**

    - numpy's array protocol, `__array__(dtype=None, copy=None)`.
    - A class of `overrides.toml [views]`: returning the view cast with `rv_policy::reference_internal`, or with `rv_policy::copy` when `copy` is `True` (`nanocct::array_protocol`); reported, category `view`.
    - An `NCollection` array: returning the view cast with `rv_policy::reference` and an owner capsule that keeps the container's Python object and counts as one of its views (`nanocct::container_array`, `nanocct::export_view`), or with `rv_policy::copy` when `copy` is `True`; not reported.

- **Python examples**

    ```python
    import gc
    import numpy as np
    from nanocct import TopoDS
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepMesh import BRepMesh_IncrementalMesh
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopLoc import TopLoc_Location

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    BRepMesh_IncrementalMesh(box, 0.1)
    face = TopoDS.Face(TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE).Current())
    triangulation = BRep_Tool.Triangulation_s(face, TopLoc_Location())
    nodes = np.asarray(triangulation.InternalNodes())    # a view of the triangulation's own storage
    assert nodes.shape == (triangulation.NbNodes(), 3) and nodes.dtype == np.float64 and not nodes.flags["OWNDATA"]
    assert np.asarray(triangulation.InternalNormals()).dtype == np.float32
    copy = np.array(triangulation.InternalNodes())       # copy=True: an independent copy
    del triangulation, face, box
    gc.collect()
    assert np.array_equal(nodes, copy)                   # the view keeps its owner alive
    ```

    ```python
    import numpy as np
    from nanocct.Image import Image_Format, Image_PixMap
    from nanocct.Quantity import Quantity_Color, Quantity_ColorRGBA, Quantity_TypeOfColor

    pixmap = Image_PixMap()
    assert pixmap.InitZero(Image_Format.Image_Format_RGB, 5, 3, 16)    # 15 bytes of pixels, rows of 16
    red = Quantity_Color(1.0, 0.0, 0.0, Quantity_TypeOfColor.Quantity_TOC_RGB)
    pixmap.SetPixelColor(1, 2, Quantity_ColorRGBA(red, 1.0))
    view = np.asarray(pixmap)
    assert view.shape == (3, 5, 3) and view.dtype == np.uint8
    assert pixmap.IsTopDown() is False and view.strides == (-16, 3, 1)   # padded rows, bottom-up
    assert view[2, 1].tolist() == [255, 0, 0]                             # view[y, x] is PixelColor(x, y)
    ```

    ```python
    import numpy as np
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array1
    from nanocct.TopoDS import TopoDS_Shape

    points = NCollection_Array1[gp_Pnt](1, 3)
    points.SetValue(2, gp_Pnt(1, 2, 3))
    view, copy = np.asarray(points), np.array(points)
    view[0] = [7, 8, 9]                                  # writes go straight into the array
    assert points.Value(1).X() == 7.0 and copy[0, 0] == 0.0
    assert view.shape == (3, 3) and view[1].tolist() == [1.0, 2.0, 3.0]
    assert not hasattr(NCollection_Array1[TopoDS_Shape], "__array__")   # nothing packed to view
    ```
### R-ADDON

#### Case 1: computation, not data

- **C++ Idiom**

    Work that is a *computation* rather than data, where a per-item Python loop would dominate

- **OCCT examples**

    - `void BRepGProp_Face::Normal(const double U, const double V, gp_Pnt& P, gp_Vec& VNor) const` (one normal per call)
    - `static bool BRepLib::EnsureNormalConsistency(const TopoDS_Shape& S, const double theAngTol = 0.001, const bool ForceComputeNormals = false)`
    - `static const occ::handle<Poly_PolygonOnTriangulation>& BRep_Tool::PolygonOnTriangulation(const TopoDS_Edge& E, const occ::handle<Poly_Triangulation>& T, const TopLoc_Location& L)` (one edge per call)
    - `GeomAbs_CurveType GeomAdaptor_TransformedCurve::GetType() const override` (inherited by `BRepAdaptor_Curve`)

- **Rule**

    - A view moves what is already in memory; these produce something.
    - `NormalsFromSurface` because OCCT offers surface normals only as `BRepGProp_Face::Normal(u, v, ...)`, one call at a time, and `Poly_Triangulation`'s stored normals are not a substitute — `BRepLib::EnsureNormalConsistency` fills a whole shape in 0.1 ms but flips 2 of 1773 nodes on a fused solid.
    - `EdgeSegments` because an edge carries ~26 points against a face's ~128, so per-item Python overhead never amortises: vectorising *inside* each edge gave 221 ms for 33 370 edges against pure Python's 274 ms, while moving the loop to C++ gave **19.7 ms**.
    - The face path stays in Python precisely because it does amortise.
    - **A helper returns whatever only it can know**: `EdgeSegments` decides which edges to skip, so it returns each kept edge's `GeomAbs_CurveType` alongside its segment count — a caller could not align a type array with the counts afterwards without redoing the lookups the helper exists to avoid (the Python loop a caller would need, `BRepAdaptor_Curve(e).GetType()` over the 33 388 edges of the 219-leaf assembly, takes 24.4 ms -- more than `EdgeSegments` as a whole, curve types included, 17.5 ms; best of 7, macOS).
    - Measured in one process over a 219-leaf assembly, 1.97 M nodes, extraction only: the same pure-Python algorithm 1425.8 ms, views + AddOns **366.4 ms** — 3.9x faster than pure Python, `compute()` to `compute()`.

- **Python**

    - A function in `nanocct.AddOns.<Concern>`, hand-written in `src/cpp/AddOns/`.

- **Python examples**

    ```python
    import numpy as np
    from nanocct import TopoDS
    from nanocct.AddOns.Tessellator import NormalsFromSurface
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepMesh import BRepMesh_IncrementalMesh
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeSphere
    from nanocct.BRepTools import BRepTools
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopLoc import TopLoc_Location

    sphere = BRepPrimAPI_MakeSphere(10.0).Shape()
    BRepMesh_IncrementalMesh(sphere, 0.5)
    face = TopoDS.Face(TopExp_Explorer(sphere, TopAbs_ShapeEnum.TopAbs_FACE).Current())
    triangulation = BRep_Tool.Triangulation_s(face, TopLoc_Location())
    u0, u1, v0, v1 = BRepTools.UVBounds_s(face)
    uv = np.ascontiguousarray(np.clip(np.asarray(triangulation.InternalUVNodes()), [u0, v0], [u1, v1]))
    normals = NormalsFromSurface(face, uv)               # one BRepGProp_Face::Normal per node, in C++
    assert np.allclose(normals, np.asarray(triangulation.InternalNodes()) / 10.0)
    ```

    ```python
    from nanocct.AddOns.Tessellator import EdgeSegments
    from nanocct.BRepMesh import BRepMesh_IncrementalMesh
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeCylinder
    from nanocct.GeomAbs import GeomAbs_CurveType

    cylinder = BRepPrimAPI_MakeCylinder(1.0, 2.0).Shape()
    BRepMesh_IncrementalMesh(cylinder, 0.1)
    segments, per_edge, edge_types = EdgeSegments(cylinder)   # every edge's polyline in one call
    assert len(segments) == 2 * per_edge.sum()
    circle, line = GeomAbs_CurveType.GeomAbs_Circle, GeomAbs_CurveType.GeomAbs_Line
    assert [GeomAbs_CurveType(t) for t in edge_types] == [circle, line, circle]   # aligned with the counts
    ```

#### Case 2: an unfixed OCCT bug

- **C++ Idiom**

    (second reason, rare) An OCCT bug that hits often, is reported upstream and is not fixed there

- **OCCT examples**

    - `ShapeUpgrade_UnifySameDomain::ShapeUpgrade_UnifySameDomain(const TopoDS_Shape& aShape, const bool UnifyEdges = true, const bool UnifyFaces = true, const bool ConcatBSplines = false)` (the class the AddOn mirrors)
    - `void ShapeUpgrade_UnifySameDomain::UnionPCurves(const NCollection_Sequence<TopoDS_Shape>& theChain, TopoDS_Edge& theEdge)` (protected)
    - `static void Geom2dConvert::ConcatC1(NCollection_Array1<occ::handle<Geom2d_BSplineCurve>>& ArrayOfCurves, const NCollection_Array1<double>& ArrayOfToler, occ::handle<NCollection_HArray1<int>>& ArrayOfIndices, occ::handle<NCollection_HArray1<occ::handle<Geom2d_BSplineCurve>>>& ArrayOfConcatenated, bool& ClosedFlag, const double ClosedTolerance)`
    - `bool Geom2dConvert_CompCurveToBSplineCurve::Add(const occ::handle<Geom2d_BoundedCurve>& NewCurve, const double Tolerance, const bool After = false)` (the default `After = false` is the bug)

- **Rule**

    - The purpose is temporary: when OCCT fixes the bug, the callers go back to the OCCT class and the AddOn is deleted.
    - So every such AddOn carries **a canary test asserting that plain OCCT still fails on the reproducer** — when an OCCT update makes it fail, that is the signal to remove it — and a test that its members' `__nb_signature__` entries are among the OCCT binding's.
    - First case, `AddOns.ShapeClean.ShapeUpgrade_UnifySameDomain` (`src/cpp/AddOns/ShapeClean.cpp`), for **OCCT issue #1541**: `Geom2dConvert::ConcatC1` calls `Geom2dConvert_CompCurveToBSplineCurve::Add` without `After = true` (`Geom2dConvert.cxx:1444`; the 3D twin passes it, `GeomConvert.cxx:1298`), so when `UnionPCurves` merges a full circle made of >= 2 arcs with a non-line pcurve on a non-planar face, the pcurve starts at the wrong junction.
    - The edge tolerance inflates to ~0.6 and `ShapeFix_Wire::FixDegenerated` replaces the edge in the spherical face with a degenerated one.
    - build123d runs the class after every boolean.
    - A sphere cut from a box with its centre outside the box broke in 53 of 300 random orientations (centre inside: 0 of 300).
    - The workaround touches only that case: a face pass, then the edge pass with enough junction vertices of each such circle kept that no closed pcurve loop is concatenated, then those circles merged with `Add(..., After = true)` and the three histories composed.
    - The face pass has to come first — on the raw cut the junctions still touch the edges between the faces being merged, and detection finds 0 vertices against 2 after it.
    - Measured: identical face/edge/vertex counts, validity and tolerance to the Python original (`safe_clean.py`) on 600 random cuts, 0 invalid results against OCCT's 29; build123d's suite with the workaround in both call sites, 2 465 IDs, no behavioural difference; ~0.19 ms per clean in Python, so R-ADDON's first reason does not apply — correctness does.
    - Only what build123d calls is mirrored (constructor, `AllowInternalEdges`, `Build`, `Shape`, `History`).

- **Python**

    - A class in `nanocct.AddOns.<Concern>` with the **OCCT class's own name** and, for each member it has, the signature, defaults and docstring of nanocct's binding of that class, so that a caller switches back by changing the import only.
    - **OCCT's source is never patched** (side effects unknown).

- **Python examples**

    ```python
    from nanocct.AddOns.ShapeClean import ShapeUpgrade_UnifySameDomain as Workaround
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Cut
    from nanocct.BRepCheck import BRepCheck_Analyzer
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeSphere
    from nanocct.gp import gp_Pnt
    from nanocct.ShapeUpgrade import ShapeUpgrade_UnifySameDomain

    box = BRepPrimAPI_MakeBox(gp_Pnt(-0.5, -0.5, -0.5), 1.0, 1.0, 1.0).Shape()
    centre = gp_Pnt(-0.8941468682889828, -0.05608050987114277, 0.16128077950256148)   # outside the box
    cut = BRepAlgoAPI_Cut(box, BRepPrimAPI_MakeSphere(centre, 0.5).Shape()).Shape()

    def clean(unifier_class):
        unifier = unifier_class(cut, True, True, True)
        unifier.AllowInternalEdges(False)
        unifier.Build()
        return unifier.Shape()

    assert Workaround.__name__ == ShapeUpgrade_UnifySameDomain.__name__   # switching back is an import change
    assert not BRepCheck_Analyzer(clean(ShapeUpgrade_UnifySameDomain)).IsValid()   # OCCT issue #1541
    assert BRepCheck_Analyzer(clean(Workaround)).IsValid()
    ```
### R-VIEW-GUARD

- **C++ Idiom**

    A live **view** into an NCollection container -- an element reference, a numpy array over its storage (`__array__`), an **iterator** (the binder's `Iterator` classes, the Python iterators of `__iter__`, and an R-ITER class constructed or `Init`/`Initialize`d from a container) -- and a call that would invalidate it

- **OCCT examples**

    `ChangeValue`/`ChangeFirst`/`ChangeLast`/`ChangeAt`, a List's or vector's `Append`/`Prepend`/`Insert*` result, a map's `ChangeFind`/`ChangeSeek`/`Bound`/`ChangeFromIndex`, an iterator's `ChangeValue`, `LinearVector::ToArray1`'s aliasing array:

    - `reference NCollection_Array1::ChangeValue(const int theIndex)` (`reference` = `TheItemType&`)
    - `TheItemType& NCollection_List::Append(const TheItemType& theItem)`
    - `TheItemType& NCollection_DataMap::ChangeFind(const TheKeyType& theKey)`
    - `void Graphic3d_Camera::FrustumPoints(NCollection_Array1<NCollection_Vec3<double>>& thePoints, const NCollection_Mat4<double>& theModelWorld = NCollection_Mat4<double>()) const` (resizes its argument)
    - `static void TopExp::MapShapes(const TopoDS_Shape& S, const TopAbs_ShapeEnum T, NCollection_IndexedMap<TopoDS_Shape, TopTools_ShapeMapHasher>& M)` (adds to its argument)

- **Rule**

    - A view would read freed memory after the container moved or freed what it points into: `a.ChangeValue(1)` after `a.Resize(…)`, `np.asarray(a)` after `Resize`, a Sequence's `ChangeValue` after `Remove`, a List's `Append` result after `Clear` (heap-use-after-free under ASan), and every iterator kind -- `List.Iterator`/`Sequence.Iterator` after `Clear`/`Remove`, a `DataMap.Iterator` and `for k in map` after an `Add`/`Bind` that grows the table, `iter(list)` after `Clear` (ASan).
    - OCCT changes containers passed in: `Graphic3d_Camera::FrustumPoints` resizes its array argument (Graphic3d_Camera.cxx:1743), `TopExp::MapShapes` adds to the map.
    - The check runs after argument conversion because a call policy's `precall` runs before it, and raising there would pre-empt another overload taking the same container `const` (`PLib::SetPoles`).
    - Consequence, as for `bytearray`: an iterator or view still referenced blocks the container until it is released (`del it`).
    - A numpy view taken before an OCCT call that fills the array blocks that call -- take the view after it.
    - Measured: a view handed out +40 to +55 ns (`ChangeValue` 44 → 83-99 ns), the same view returned again +7 ns, `np.asarray` +70 ns, a `for` loop +75 ns, a checked call +2 to +3 ns while nothing is viewed and +6 to +8 ns otherwise.
    - Not covered (residual): what OCCT itself does to a container it owns -- the 149<!-- count: view-guard-lines --> reported methods, an OCCT object changing a container it was handed earlier or reaches through a handle (`handle<NCollection_HArray1<…>>` arguments are not checked), the R-VIEW classes of nanocct_views.h (`Poly_ArrayOfNodes` after `Poly_Triangulation::ResizeNodes`), and a container wrapped in `NCollection_Shared` (bound at a non-zero offset).

- **Python**

    - The call raises **`BufferError`** (Python's rule for `bytearray` while a buffer is exported).
    - Views are counted per **C++ container address** in **one** table for all extension modules (`nanocct::view_table()`, a capsule on the `nanocct` package like the slot table; two Python wrappers of one container agree), mutex-protected, with an atomic count of all live views as the fast path.
    - A view's count goes when it dies (`nb::keep_alive_cb`; a numpy array: its owner capsule, which also keeps the container's Python object -- nanobind refuses `reference_internal` for an ndarray with an owner).
    - Which call invalidates which view is OCCT's container code, read once (7a, the R-VIEW-GUARD table): the binder checks its own members exactly (a `Resize` to the same length, an `Assign` of the same size, an append below `Capacity()` pass; a hashed map's insert is checked against its iterators only, which cache the bucket array; `Remove(it)` through the iterator itself is allowed).
    - **Every generated function** taking a container by **non-const reference or pointer** (`Param.guarded`, parse.py `_mutable_container`; inside a 7c walk from the substituted spelling) checks it, after nanobind converted the arguments: a direct binding goes through `&nanocct::guarded<static_cast<…>(&C::M), k…>::call`, same signature, stubs unchanged; a lambda or constructor body starts with `nanocct::refuse_viewed_argument(x, k)` -- 1 867<!-- count: view-guard-params --> parameters in 35<!-- count: view-guard-toolkits --> toolkits (1 102<!-- count: view-guard-wrapped --> wrapped bindings, 106<!-- count: view-guard-lambda --> lambda checks).
    - A **container data member** (by value) gets a setter that checks (`nanocct_def_container_field`, 44).
    - An R-ITER class's constructor or `Init`/`Initialize` taking a container registers the object as an iterator of it (`nanocct::view_of<iterator, …>`, 23<!-- count: view-guard-iterators --> sites: `NCollection_Iterator<…>`, BRepGraph's iterators over a parents vector, `TopOpeBRepDS_InterferenceIterator`).
    - A method handing out a container its object owns by non-const reference is **reported**, category `view-guard` (149, OCCT 8.0.1: `TDF_DataSet::Labels()`, `AIS_ColoredShape::ChangeCustomAspectsMap()`, …).

- **Python examples**

    ```python
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array1

    def refuses(call):
        try:
            call()
        except BufferError:
            return True
        return False

    points = NCollection_Array1[gp_Pnt](1, 3)
    point = points.ChangeValue(1)                        # an element reference: a view
    assert not refuses(lambda: points.Resize(1, 3, True))   # the same length keeps the storage
    assert refuses(lambda: points.Resize(1, 5, True))       # a new buffer would leave `point` dangling
    del point
    points.Resize(1, 5, True)                            # released: allowed
    assert points.Length() == 5
    ```

    ```python
    from nanocct.gp import gp_Vec
    from nanocct.NCollection import NCollection_DataMap, NCollection_List
    from nanocct.TopoDS import TopoDS_Shape

    def refuses(call):
        try:
            call()
        except BufferError:
            return True
        return False

    shapes = NCollection_List[TopoDS_Shape]()
    appended = shapes.Append(TopoDS_Shape())             # a view into the new node
    assert refuses(shapes.Clear)
    vectors = NCollection_DataMap[int, gp_Vec]()
    vectors.Bind(1, gp_Vec(1, 2, 3))
    vector = vectors.ChangeFind(1)
    assert not refuses(lambda: vectors.Bind(2, gp_Vec()))   # growth relinks the nodes, keeps them
    assert refuses(lambda: vectors.UnBind(2))               # removal frees a node
    keys = iter(vectors)
    assert refuses(lambda: vectors.Bind(3, gp_Vec()))       # the iterator caches the bucket array
    ```

    ```python
    import numpy as np
    from nanocct.BVH import BVH_Vec3d
    from nanocct.Graphic3d import Graphic3d_Camera
    from nanocct.NCollection import NCollection_Array1

    camera = Graphic3d_Camera()
    points = NCollection_Array1[BVH_Vec3d](1, 3)
    view = np.asarray(points)
    try:
        camera.FrustumPoints(points)                     # OCCT resizes its argument
        raise AssertionError("not refused")
    except BufferError:
        pass
    del view                                             # take the view after the call
    camera.FrustumPoints(points)
    assert np.asarray(points).shape == (points.Length(), 3)
    ```

    ```python
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.NCollection import NCollection_IndexedMap
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp
    from nanocct.TopoDS import TopoDS_Shape
    from nanocct.TopTools import TopTools_ShapeMapHasher

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    faces = NCollection_IndexedMap[TopoDS_Shape, TopTools_ShapeMapHasher]()
    it = iter(faces)
    try:
        TopExp.MapShapes_s(box, TopAbs_ShapeEnum.TopAbs_FACE, faces)   # OCCT adds to its argument
        raise AssertionError("not refused")
    except BufferError:
        pass
    del it
    TopExp.MapShapes_s(box, TopAbs_ShapeEnum.TopAbs_FACE, faces)
    assert faces.Extent() == 6
    ```
### R-ITER

- **C++ Idiom**

    A class with `More() -> bool` (or `Standard_Boolean`, as for R-NULL-BOOL's `IsNull()`), `Next()` and a parameterless `Value()` or `Current()` returning a value

- **OCCT examples**

    `TopExp_Explorer`, `TopoDS_Iterator`, `BRepTools_WireExplorer`, `Adaptor3d_TopolTool`, the `BRepGraph` iterators; also the seven hand-written binder `Iterator` classes of 7a — `NCollection_List__int.Iterator`, the map iterators yielding `Value()`: the key for `Map`, the value for `DataMap` — and through them `Graphic3d_SequenceOfHClipPlane.Iterator`:

    - `const TopoDS_Shape& TopExp_Explorer::Current() const` (with `bool TopExp_Explorer::More() const` and `void TopExp_Explorer::Next()`)
    - `const TopoDS_Shape& TopoDS_Iterator::Value() const`
    - `virtual occ::handle<Adaptor2d_Curve2d> Adaptor3d_TopolTool::Value()` (a handle by value)
    - `[[nodiscard]] const NodeType& BRepGraph_Iterator::Current() const` (a dependent `const T&` of a 7c instantiation)
    - `Standard_Persistent* Storage_BucketIterator::Value() const` (a Transient pointer: not iterable)

- **Rule**

    - Python addition (Python additions).
    - The element is copied out before `Next()`, so `Value()` results that are Transient pointers/references are excluded (`Storage_BucketIterator`).
    - **Dependent `const T&` results of a 7c instantiation**: libclang gives the pointee no declaration, so parse says `OTHER`; the emitter accepts `const X &` when `X` is not a Transient according to the manifest's bases (`Emitter._copyable_const_ref`) -- 49 more classes iterable (measured once): the `BRepGraph_Iterator<…Def>`, `RefsIterator::RefIterator<…Ref>` and `DefsIterator::DefsOfParent<…>` instantiations (`list(BRepGraph_EdgeIterator(g))`) and the flat maps' `Iterator`.
    - A `Key()`-only iterator (`TColStd_PackedMapOfInteger.Iterator`) is not covered.
    - An element of a class holding pointers keeps the iterated object and what its slots hold (R-RESULT-KEEP, `nanocct_def_iter<T, true>`).
    - An element of an owner class (R-COPY) is never copied out, so such a class is not iterable (none, OCCT 8.0.1).
    - An OCAF one keeps its owners (R-OWNER: the elements of `TDF_ChildIterator(root)` outlive the iterator and the data's variable).
    - An object of such a class constructed or initialised from an NCollection container counts as an iterator of it (R-VIEW-GUARD).

- **Python**

    - `__iter__` returning an `nb::make_iterator` over a cursor that yields `Value()` (or `Current()`) then calls `Next()` on the object itself, ending when `!More()` — the object is exhausted afterwards, like a file (a second `for` over it yields nothing).
    - No `__next__` on the object, and no C++ exception to end a loop (0.46 µs for a 6-face explorer, against 8.4 µs with an exception).
    - `nanocct_def_iter` in `nanocct_class_helpers.h`, `Emitter._iter_getter`.

- **Python examples**

    ```python
    import gc
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.TDF import TDF_ChildIterator, TDF_Data
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer
    from nanocct.TopoDS import TopoDS_Iterator

    box = BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()
    explorer = TopExp_Explorer(box, TopAbs_ShapeEnum.TopAbs_FACE)
    assert len(list(explorer)) == 6
    assert list(explorer) == [] and not explorer.More()      # exhausted, like a file
    assert not hasattr(explorer, "__next__")
    assert [s.ShapeType() for s in TopoDS_Iterator(box)] == [TopAbs_ShapeEnum.TopAbs_SHELL]

    data = TDF_Data()
    data.Root().FindChild(1, True)
    data.Root().FindChild(2, True)
    labels = list(TDF_ChildIterator(data.Root()))
    del data
    gc.collect()
    assert [label.Tag() for label in labels] == [1, 2]       # the elements keep their owners
    ```

    ```python
    from nanocct.BRepGraph import BRepGraph, BRepGraph_EdgeIterator
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.gp import gp_Vec
    from nanocct.NCollection import NCollection_DataMap, NCollection_List
    from nanocct.Storage import Storage_BucketIterator
    from nanocct.TColStd import TColStd_PackedMapOfInteger

    values = NCollection_List[int]()
    for i in (1, 2, 3):
        values.Append(i)
    assert list(NCollection_List[int].Iterator(values)) == [1, 2, 3]
    vectors = NCollection_DataMap[int, gp_Vec]()
    vectors.Bind(7, gp_Vec(1, 2, 3))
    assert [v.X() for v in NCollection_DataMap[int, gp_Vec].Iterator(vectors)] == [1.0]   # the value, not the key

    graph = BRepGraph()
    assert graph.Shapes().Add(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()).IsOk()
    assert len(list(BRepGraph_EdgeIterator(graph))) == 12     # a dependent const T& result

    assert not hasattr(Storage_BucketIterator, "__iter__")               # Value() is a Transient pointer
    assert not hasattr(TColStd_PackedMapOfInteger.Iterator, "__iter__")  # Key() only
    ```
### R-ITERATOR

- **C++ Idiom**

    STL-style iterators (`begin()`/`end()`)

- **OCCT examples**

    `NCollection_ForwardRangeIterator`, `NCollection_IndexedIterator`, `NCollection_StlIterator`, `NCollection_UtfIterator`, `NCollection_DynamicArray::DynamicIterator`, and the end marker of a forward range, `NCollection_ForwardRangeSentinel`:

    - `NCollection_ForwardRangeIterator<TopExp_Explorer> TopExp_Explorer::begin()`
    - `NCollection_ForwardRangeSentinel TopExp_Explorer::end() const`
    - `iterator NCollection_Array1::begin()` (`iterator` = `NCollection_IndexedIterator<std::random_access_iterator_tag, …>`)
    - `iterator NCollection_Map::begin() const` (`iterator` = `NCollection_StlIterator<std::forward_iterator_tag, Iterator, TheKeyType, true>`)
    - `NCollection_UtfIterator<Type> NCollection_UtfString::Iterator() const`
    - `iterator NCollection_DynamicArray::begin()` (`iterator` = `DynamicIterator<false>`)

- **Rule**

    - Python iterates with `__iter__` (containers, and R-ITER above).

- **Python**

    - Skipped.
    - The iterator classes themselves are not instantiated for a signature that names one, and the end marker `NCollection_ForwardRangeSentinel` is not bound: Python could not use either.

- **Python examples**

    ```python
    import nanocct.NCollection as NCollection
    import nanocct.TopExp as TopExp
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox
    from nanocct.NCollection import NCollection_Array1
    from nanocct.TopAbs import TopAbs_ShapeEnum
    from nanocct.TopExp import TopExp_Explorer

    values = NCollection_Array1[float](1, 3)
    assert not hasattr(values, "begin") and not hasattr(values, "end")
    assert len(list(values)) == 3                    # __iter__ instead
    explorer = TopExp_Explorer(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape(), TopAbs_ShapeEnum.TopAbs_FACE)
    assert not hasattr(explorer, "begin") and not hasattr(explorer, "end")
    assert not hasattr(TopExp, "NCollection_ForwardRangeIterator__TopExp_Explorer")
    assert not hasattr(NCollection, "NCollection_ForwardRangeSentinel")
    assert len(list(explorer)) == 6                  # R-ITER instead of the range-for adapter
    ```

## 7.6 Classes and members that need special handling, and what is skipped

### R-FIELD

- **C++ Idiom**

    Public data member

- **OCCT examples**

    - `gp_Pnt2d* BRepMesh_FaceChecker::Segment::Point1` (a raw pointer to a class: read-only, a copy)
    - `IMeshData::IEdgePtr BRepMesh_FaceChecker::Segment::EdgePtr` (`IMeshData_Edge*`, a pointer to a Transient: not bound)
    - `BRepGraphInc_Storage BRepGraph_Data::myIncStorage` (a type with a deleted assignment: `def_ro`)
    - `occ::handle<Poly_PolygonOnTriangulation> PolygonOnTriHashKey::Poly` (a handle member: the setter takes `None`)
    - `unsigned Graphic3d_CStructure::stick : 1` (a bit-field)

- **Rule**

    - A member of a type with a deleted assignment (`BRepGraphInc_Storage`) breaks `def_rw`.
    - A pointer member's `def_rw` setter would store the address of the Python object assigned, kept by nothing: `seg.Point1 = gp_Pnt2d(3, 4)` and `opts.LightName = "..."` (a pointer into the str's buffer) would read freed memory afterwards (heap-use-after-free under ASan).

- **Python**

    - `def_rw` when the member type is copy-assignable, `def_ro` otherwise (helper `nanocct_def_field`, compile time).
    - A **raw pointer** member (a class, or a `const char*`/`const char16_t*` string) is **read-only** and reads as a **copy** of what it points to -- a `str`, an independent object, `None` for null (`nanocct_def_pointer_field`; 28, OCCT 8.0.1: `BRepMesh_FaceChecker::Segment.Point1/Point2`, `V3d_ImageDumpOptions.LightName`, the `OpenGl_Context` function tables, `Graphic3d_BoundBuffer.Colors` -- the first element of its array).
    - Not bound, reported: a pointer to a Transient (a handle may not own it: `Segment.EdgePtr`), to an owner (R-COPY), or to a class the compiler cannot copy -- asked through a probe, `std::conditional_t<std::is_copy_constructible_v<P>, int, char>` read back as a type (`NCollection_ListNode`, `NCollection_IncAllocator::IBlock` with its `std::atomic` members, the abstract `OpenGl_Element`; 6).
    - A **handle** member's setter also takes `None` (`nb::for_setter(nb::arg("value").none())`: the getter reads a null handle as `None`, R-HANDLE, and a plain `def_rw` setter refuses it -- `GeomHash.PolygonOnTriHashKey.Poly`).
    - A **bit-field** (`unsigned stick : 1` in `Graphic3d_CStructure`, `unsigned int r1 : 8` … in `MeshVS_TwoColors` -- the only public ones in the install) is a `def_prop_rw` through lambdas, since no pointer-to-member exists (`Field.is_bitfield`).
    - An **NCollection container** member's setter raises `BufferError` while the container has live views (`nanocct_def_container_field`, R-VIEW-GUARD).

- **Python examples**

    ```python
    from nanocct.BRepGraph import BRepGraph_Data
    from nanocct.BRepMesh import BRepMesh_FaceChecker
    from nanocct.GeomHash import PolygonOnTriHashKey
    from nanocct.Graphic3d import Graphic3d_CStructure
    from nanocct.gp import gp_Pnt2d

    segment = BRepMesh_FaceChecker.Segment()
    assert segment.Point1 is None                      # a null pointer reads as None
    try:
        segment.Point1 = gp_Pnt2d(3, 4)                # read-only: nothing would keep the point alive
        raise AssertionError("a pointer member must be read-only")
    except AttributeError:
        pass
    assert not hasattr(segment, "EdgePtr")             # a pointer to a Transient: not bound

    assert BRepGraph_Data.myIncStorage.fset is None    # deleted assignment: def_ro

    key = PolygonOnTriHashKey()
    key.Poly = None                                    # a handle member takes None
    assert key.Poly is None

    assert Graphic3d_CStructure.stick.fset is not None   # a bit-field: a read/write property
    ```
### R-STATIC-DATA

- **C++ Idiom**

    Public `static const`/`static constexpr` data member of a class

- **OCCT examples**

    `RWGltf_GltfAccessor::INVALID_ID`, `NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE`, `BRepGraph_NodeId::THE_INVALID_INDEX`, `SelectBasics_SelectingVolumeManager::Point`:

    - `static const int RWGltf_GltfAccessor::INVALID_ID = -1`
    - `static constexpr size_t NCollection_IncAllocator::THE_DEFAULT_BLOCK_SIZE = 1024 * 12`
    - `static const SelectMgr_SelectionType SelectBasics_SelectingVolumeManager::Point = SelectMgr_SelectionType_Point` (an enum)
    - `static const char* const TopTools_ShapeSet::THE_ASCII_VERSIONS[TopTools_FormatVersion_VERSION_3 + 1]` (an array: reported)
    - `static const double IntPatch_WLineTool::myMaxConcatAngle` (the value is in the `.cxx`)

- **Rule**

    - The value is copied into a prvalue because an in-class-initialised `static const int X = 5;` has no definition whose address a reference could take (`nb::cast(C::X)` would odr-use it and fail to link).
    - A non-`const` static is a variable, which a class attribute would only snapshot.
    - R-FIELD covers instance members and R-NAMESPACE namespace constants.

- **Python**

    - A **read-only static property** returning the value: `cls.def_prop_ro_static("X", [](nb::handle) { return static_cast<std::remove_cv_t<decltype(C::X)>>(C::X); })` (a plain class attribute would be replaced by any assignment).
    - An enum type no binding registers is reported (R-UNBOUND-TYPE), as are arrays (`TopTools_ShapeSet::THE_ASCII_VERSIONS`) and non-`const` statics.
    - A static whose value is not in the header (`static const double X;`, defined in the `.cxx`) is read through its symbol, so R-UNDEFINED checks it against the library (`symbols.defined_symbols` counts data symbols too) -- `IntPatch_WLineTool::myMaxConcatAngle` has no `Standard_EXPORT` and would be `LNK2019` on Windows.

- **Python examples**

    ```python
    from nanocct.NCollection import NCollection_IncAllocator
    from nanocct.RWGltf import RWGltf_GltfAccessor
    from nanocct.SelectBasics import SelectBasics_SelectingVolumeManager
    from nanocct.SelectMgr import SelectMgr_SelectionType
    from nanocct.TopTools import TopTools_ShapeSet

    assert RWGltf_GltfAccessor.INVALID_ID == -1
    assert NCollection_IncAllocator.THE_DEFAULT_BLOCK_SIZE == 1024 * 12
    assert SelectBasics_SelectingVolumeManager.Point == SelectMgr_SelectionType.SelectMgr_SelectionType_Point
    try:
        RWGltf_GltfAccessor.INVALID_ID = 0             # a read-only static property, not a class attribute
        raise AssertionError("a static constant must be read-only")
    except AttributeError:
        pass
    assert not hasattr(TopTools_ShapeSet, "THE_ASCII_VERSIONS")   # an array: reported, not bound
    ```
### R-MI

- **C++ Idiom**

    Class with several bases

- **OCCT examples**

    `IMeshData_Edge : IMeshData_TessellatedShape, IMeshData_StatusOwner`:

    - `class IMeshData_Edge : public IMeshData_TessellatedShape, public IMeshData_StatusOwner`
    - `class Message_LazyProgressScope : protected Message_ProgressScope` (the base provides `operator new`: no constructor)
    - `class BRepAlgoAPI_Algo : public BRepBuilderAPI_MakeShape, protected BOPAlgo_Options` (`BOPAlgo_Options` provides `operator new`)
    - `class RWObj_CafReader : public RWMesh_CafReader, protected RWObj_IShapeReceiver` (a non-public base without `operator new`: still constructible)

- **Rule**

    - nanobind single inheritance (5.2).

- **Python**

    - First base only, others reported.
    - A **non-public** base is dropped the same way, and costs the class its constructors only when that base provides `operator new` (`Message_LazyProgressScope`, `BRepAlgoAPI_Algo`; 5.2).

- **Python examples**

    ```python
    from nanocct.BOPAlgo import BOPAlgo_Options
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Algo
    from nanocct.IMeshData import IMeshData_Edge, IMeshData_StatusOwner, IMeshData_TessellatedShape
    from nanocct.Message import Message_LazyProgressScope
    from nanocct.RWObj import RWObj_CafReader

    assert IMeshData_Edge.__bases__ == (IMeshData_TessellatedShape,)   # the first base only
    assert not issubclass(IMeshData_Edge, IMeshData_StatusOwner)
    assert not issubclass(BRepAlgoAPI_Algo, BOPAlgo_Options)           # the protected base is dropped
    try:
        Message_LazyProgressScope()                    # its protected base provides operator new
        raise AssertionError("Message_LazyProgressScope must have no constructor")
    except TypeError:
        pass
    assert type(RWObj_CafReader()).__name__ == "RWObj_CafReader"       # a protected base without operator new
    ```
### R-USING

- **C++ Idiom**

    `using Base::name;` in a public section

- **OCCT examples**

    `BRepAlgoAPI_Algo : protected BOPAlgo_Options` re-exports `SetFuzzyValue`, `SetRunParallel`, `HasErrors`, `GetReport`, … — 14 members every boolean has and build123d calls; `Blend_FuncInv::Set` un-hides base overloads:

    - `using BOPAlgo_Options::SetFuzzyValue;` in `class BRepAlgoAPI_Algo : public BRepBuilderAPI_MakeShape, protected BOPAlgo_Options` (`BRepAlgoAPI_Algo.hxx:52`, one of the 14 at lines 41–54)
    - `using Blend_FuncInv::Set;` next to `void BlendFunc_ChamfInv::Set(const double Dist1, const double Dist2, const int Choix) override` (`BlendFunc_ChamfInv.hxx:52`; also `BlendFunc_ConstThroatInv.hxx:48`)
    - `using BRepGraph_ReverseIterator::EdgeParentsOf<BRepGraph_ReverseIterator::FaceFromEdgeCoEdgeTraits>::EdgeParentsOf;` in `BRepGraph_FacesOfEdge` (`BRepGraph_ReverseIterator.hxx:754`, `using Base::Base;`)
    - `using BRepFeat_Builder::Perform;` in a protected section of `BRepFeat_MakeCylindricalHole` (`BRepFeat_MakeCylindricalHole.hxx:98–100`: not public, so not re-exported)

- **Rule**

    - A member pointer of the base would need the inaccessible upcast, and nanobind never merges overloads across classes, so without the rule a derived overload set hides the base's.
    - The member's symbol belongs to the base's library (the base's own binding runs the nm check).

- **Python**

    - The base's overloads of `name` (resolved with `clang_getOverloadedDecl`) are bound **on the derived class through lambdas** calling `self.name(...)` on the derived object.
    - Out-parameters, streams and results follow the usual rules (class results are copied, a `T*` keeps `reference`).
    - `using Base::Base;` binds the base's constructors on the derived class (`BRepGraph_FacesOfEdge(theGraph, theEdge)`; default/copy/move are not inherited in C++, the derived class gets its own implicit ones).

- **Python examples**

    ```python
    from nanocct.BlendFunc import BlendFunc_ChamfInv
    from nanocct.BOPAlgo import BOPAlgo_Options
    from nanocct.BRepAlgoAPI import BRepAlgoAPI_Fuse
    from nanocct.BRepGraph import BRepGraph, BRepGraph_EdgeId, BRepGraph_FacesOfEdge
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeBox

    fuse = BRepAlgoAPI_Fuse()
    fuse.SetFuzzyValue(1e-5)                           # BOPAlgo_Options::SetFuzzyValue on the derived object
    assert fuse.FuzzyValue() == 1e-5 and not isinstance(fuse, BOPAlgo_Options)

    overloads = [line for line in BlendFunc_ChamfInv.Set.__doc__.splitlines() if line.startswith("Set(")]
    assert len(overloads) == 2                         # its own Set(Dist1, Dist2, Choix) and Blend_FuncInv::Set

    graph = BRepGraph()
    graph.Clear()
    assert graph.Shapes().Add(BRepPrimAPI_MakeBox(1.0, 2.0, 3.0).Shape()).IsOk()
    faces = BRepGraph_FacesOfEdge(graph, BRepGraph_EdgeId(0))   # a constructor of the base (using Base::Base)
    assert len(list(faces)) == 2                       # an edge of a box bounds two faces
    ```
### R-NONCOPYABLE

- **C++ Idiom**

    Class whose implicit copy/move constructor does not compile although the traits say copyable: a member `NCollection_CellFilter<…>` or `NCollection_Map<…CellFilter<…>::Cell>`, a container of a type whose copy constructor is deleted, or such a class held by value

- **OCCT examples**

    `math_GlobOptMin`, `BRepExtrema_ProximityValueTool`, `BRepMesh_CircleTool`, `BRepMesh_VertexTool`, the `CellFilter` instantiations themselves (a `CellFilter` member); `NCollection_Sequence<CSLib_Class2d>` in `BRepTopAdaptor_FClass2d` (a container); `BRepExtrema_ShapeProximity`, `BRepMesh_Delaun` (held by value):

    - `NCollection_CellFilter<NCollection_CellFilter_Inspector> math_GlobOptMin::myFilter`
    - `NCollection_Sequence<CSLib_Class2d> BRepTopAdaptor_FClass2d::TabClass` (with `CSLib_Class2d::CSLib_Class2d(const CSLib_Class2d&) = delete`)
    - `BRepMesh_CircleTool BRepMesh_Delaun::myCircles` (such a class held by value)
    - `IMeshData::VertexCellFilter BRepMesh_VertexTool::myCellFilter` (in `class BRepMesh_VertexTool : public Standard_Transient`: skipped)

- **Rule**

    - nanobind instantiates its copy/move wrappers from `std::is_copy/move_constructible` (no hook for move).
    - The wrapper is what Python sees (`type(opt).__name__ == "math_GlobOptMin"`), no OCCT API returns a reference to one of them.

- **Python**

    - **Detected by the parser** (field types; `overrides.toml [skip] noncopyable` remains for cases it cannot see, currently empty) and bound through a generated wrapper struct — except a **Transient** class (`BRepMesh_VertexTool`), which is skipped: the wrapper would be the registered type while OCCT hands out the OCCT class, and nanobind's copy wrapper would not compile — with deleted copy and move constructors and inherited constructors, under the original name.
    - Member pointers still name the OCCT class, lambdas take the wrapper.
    - Reported (category `noncopyable`).

- **Python examples**

    ```python
    import nanocct.BRepMesh as BRepMesh
    from nanocct.BRepBuilderAPI import BRepBuilderAPI_MakeFace
    from nanocct.BRepTopAdaptor import BRepTopAdaptor_FClass2d
    from nanocct.gp import gp_Pln, gp_Pnt2d
    from nanocct.TopAbs import TopAbs_State

    face = BRepBuilderAPI_MakeFace(gp_Pln(), 0.0, 1.0, 0.0, 1.0).Face()
    classifier = BRepTopAdaptor_FClass2d(face, 1e-7)   # the wrapper struct, under the original name
    assert type(classifier).__name__ == "BRepTopAdaptor_FClass2d"
    assert classifier.Perform(gp_Pnt2d(0.5, 0.5)) == TopAbs_State.TopAbs_IN
    try:
        BRepTopAdaptor_FClass2d(classifier)            # no copy constructor
        raise AssertionError("the wrapper must not be copyable")
    except TypeError:
        pass
    assert not hasattr(BRepMesh, "BRepMesh_VertexTool")   # a Transient: skipped
    ```
### R-INCOMPLETE

- **C++ Idiom**

    Class with a data member of a type declared but never defined in the headers

- **OCCT examples**

    - `NCollection_LinearVector<Slot> BRepGraph_CacheMesh::mySlots` (`BRepGraph_CacheMesh::Slot`, defined in the `.cxx`; through `NCollection_LinearVector<Slot>`; `struct Slot;` at `BRepGraph_CacheMesh.hxx:317`)
    - `std::unique_ptr<Geom_OsculatingSurface> Geom_OffsetSurface::myOscSurf` (`class Geom_OsculatingSurface;` only: exempt)
    - `NCollection_Handle<BRepFill_Generator> BRepOffsetAPI_ThruSections::myBFGenerator` (`class BRepFill_Generator;` only: exempt)

- **Rule**

    - `nb::class_` needs the destructor.
    - `unique_ptr`/`shared_ptr`/`handle`/`NCollection_Handle` members are exempt (pointee may stay incomplete, `Geom_OffsetSurface`, `BRepOffsetAPI_ThruSections`).

- **Python**

    - Class skipped, reported.

- **Python examples**

    ```python
    import nanocct.BRepGraph as BRepGraph
    from nanocct.BRepOffsetAPI import BRepOffsetAPI_ThruSections
    from nanocct.Geom import Geom_OffsetSurface, Geom_Plane
    from nanocct.gp import gp_Pln

    assert not hasattr(BRepGraph, "BRepGraph_CacheMesh")       # skipped
    assert Geom_OffsetSurface(Geom_Plane(gp_Pln()), 1.0).Offset() == 1.0   # unique_ptr member: bound
    assert BRepOffsetAPI_ThruSections(True).IsDone() is False   # NCollection_Handle member: bound
    ```
### R-UNDEFINED

- **C++ Idiom**

    Method, constructor or free function declared, never defined by OCCT

- **OCCT examples**

    `math_NewtonMinimum::IsConvex`, `OSD_Path::LocateExecFile`, the overload `GeomInt_WLApprox::Perform()` next to three defined `Perform` overloads, three `Geom2dGcc_FunctionTanCuCuCu` constructors, `TopOpeBRepDS`'s `FUN_scanloi`/`FDSSDM_s1s2makesordor`:

    - `bool math_NewtonMinimum::IsConvex() const`
    - `bool OSD_Path::LocateExecFile(OSD_Path& aPath)`
    - `void GeomInt_WLApprox::Perform()`
    - `Geom2dGcc_FunctionTanCuCuCu::Geom2dGcc_FunctionTanCuCuCu(const Geom2dAdaptor_Curve& C1, const gp_Pnt2d& P2, const gp_Pnt2d& P3)` (one of the three)
    - `void FUN_scanloi(const NCollection_List<occ::handle<TopOpeBRepDS_Interference>>& lII, NCollection_List<occ::handle<TopOpeBRepDS_Interference>>& lFOR, int& FOR, NCollection_List<occ::handle<TopOpeBRepDS_Interference>>& lREV, int& REV, NCollection_List<occ::handle<TopOpeBRepDS_Interference>>& lINT, int& INT)` (a free function)

- **Rule**

    - `generator/symbols.py`: `nm` on the toolkit library vs. libclang's `Cursor.mangled_name` of every method/constructor without an inline definition (bodies are parsed so `get_definition()` sees out-of-class inline definitions; pure virtuals excluded).
    - Mangled names make the check exact and overload-aware; the platform mangling matches `nm` on macOS (leading underscore included, verified) and Linux.
    - **Windows uses `dumpbin /EXPORTS` on `<install>/win64/<vcNN>/lib/<TK>.lib`**: `Standard_EXPORT` is `__declspec(dllexport)`, so the import library's export list answers the same question, and `dumpbin` is located through `vswhere -products *` so no vcvars environment is needed.
    - It is *stricter* than the macOS check in one way and cleaner in another: the trailing `Summary` block of a `.lib` dump is indented like the exports and has to be stopped at explicitly, and MSVC has no C1/C2 constructor split, so Windows does not produce the abstract-class constructor false positives macOS does (34 of its 133<!-- count: undefined-lines --> `undefined` lines).

- **Python**

    - Skipped automatically, per overload.

- **Python examples**

    ```python
    from nanocct import TopOpeBRepDS
    from nanocct.Geom2dGcc import Geom2dGcc_FunctionTanCuCuCu
    from nanocct.GeomInt import GeomInt_WLApprox
    from nanocct.math import math_NewtonMinimum
    from nanocct.OSD import OSD_Path

    assert not hasattr(math_NewtonMinimum, "IsConvex")
    assert not hasattr(OSD_Path, "LocateExecFile")
    assert not hasattr(TopOpeBRepDS, "FUN_scanloi")
    assert "P3" not in Geom2dGcc_FunctionTanCuCuCu.__init__.__doc__   # the constructors ending in a gp_Pnt2d P3
    try:
        GeomInt_WLApprox().Perform()                   # only this overload is missing, the others are bound
        raise AssertionError("Perform() has no definition in the library")
    except TypeError:
        pass
    ```
### R-UNDEFINED-COPY

- **C++ Idiom**

    Copy constructor declared in the header but never defined in the library (the pre-C++11 idiom to forbid copies)

- **OCCT examples**

    `GCPnts_DistFunction`:

    - `GCPnts_DistFunction::GCPnts_DistFunction(const GCPnts_DistFunction& theOther)`
    - `GCPnts_DistFunction2d::GCPnts_DistFunction2d(const GCPnts_DistFunction2d& theOther)`
    - `SelectMgr_BVHThreadPool::Sentry::Sentry(const Sentry&)` (*"This method should not be called (prohibited)."*)

- **Rule**

    - nanobind's copy wrapper is instantiated for every `std::is_copy_constructible` type → link error.
    - Detected by `nm` (`Class::Class(Class const&)` absent; `= default` counts as defined).

- **Python**

    - Class skipped, reported.

- **Python examples**

    ```python
    import nanocct.GCPnts as GCPnts
    from nanocct.SelectMgr import SelectMgr_BVHThreadPool

    assert not hasattr(GCPnts, "GCPnts_DistFunction")
    assert not hasattr(GCPnts, "GCPnts_DistFunction2d")
    assert not hasattr(SelectMgr_BVHThreadPool, "Sentry")
    ```
### R-DEPRECATED

- **C++ Idiom**

    Deprecated member

- **OCCT examples**

    `Standard_DEPRECATED("use Poles() returning const reference instead")`:

    - `void Geom_BSplineCurve::Poles(NCollection_Array1<gp_Pnt>& P) const` (`Geom_BSplineCurve.hxx:775`, next to the undeprecated `Poles()`)
    - `bool NCollection_Map::Contains(const NCollection_Map& theOther) const` (deprecated, next to the undeprecated `Contains(const TheKeyType& theKey)`)

- **Rule**

    - The OCCT docs are the nanocct docs, and 7.x-era code keeps working (build123d calls two deprecated members).
    - The message is read through `clang_getCursorPlatformAvailability` (cindex exposes only the availability kind).
    - The extension is compiled with `-Wno-deprecated-declarations`.
    - The hand-written NCollection binders read the same attribute (`generator/ncollection.py`).
    - Overloads share one docstring constant there, so when they disagree about deprecation the shared one follows the **undeprecated** overload and the deprecated one gets `<name>_deprecated` (`NCollection_Map::Contains`, the only such case in the 15 templates; nanobind renders a docstring per overload as soon as they differ).

- **Python**

    - **Bound**, OCCT's message becomes the first line of the docstring (`Deprecated in OCCT: use Poles() …`).
    - No runtime warning.

- **Python examples**

    ```python
    import warnings
    from nanocct.GC import GC_MakeCircle
    from nanocct.Geom import Geom_BSplineCurve
    from nanocct.GeomConvert import GeomConvert
    from nanocct.gp import gp_Pnt
    from nanocct.NCollection import NCollection_Array1__gp_Pnt, NCollection_Map__int

    assert "Deprecated in OCCT: use Poles() returning const reference instead" in Geom_BSplineCurve.Poles.__doc__
    circle = GC_MakeCircle(gp_Pnt(0, 0, 0), gp_Pnt(1, 1, 0), gp_Pnt(2, 0, 0)).Value()
    curve = GeomConvert.CurveToBSplineCurve_s(circle)
    poles = NCollection_Array1__gp_Pnt(1, curve.NbPoles())
    with warnings.catch_warnings():
        warnings.simplefilter("error")                 # no runtime warning
        curve.Poles(poles)                             # the deprecated overload is bound
    assert poles.Value(1).IsEqual(curve.Pole(1), 0.0)

    assert NCollection_Map__int.Contains.__doc__.count("Deprecated in OCCT") == 1   # one overload of two
    ```
### R-LINK

- **C++ Idiom**

    A header forward-declares a class of a toolkit that OCCT's own `EXTERNLIB.cmake` does not link

- **OCCT examples**

    `DE_Provider.hxx` names `XSControl_WorkSession` and `TDocStd_Document`, `TKDE` links only `TKernel`/`TKMath`/`TKBRep`:

    - `class XSControl_WorkSession;` and `class TDocStd_Document;` (`DE_Provider.hxx:24–25`)
    - `virtual bool DE_Provider::Read(const TCollection_AsciiString& thePath, const occ::handle<TDocStd_Document>& theDocument, occ::handle<XSControl_WorkSession>& theWS, const Message_ProgressRange& theProgress = Message_ProgressRange())`
    - `set(OCCT_TKDE_EXTERNAL_LIBS TKernel TKMath TKBRep)` (OCCT source, `src/DataExchange/TKDE/EXTERNLIB.cmake:2–6`)
    - `XSAlgo_ShapeProcessor::XSAlgo_ShapeProcessor(const ParameterMap& theParameters, const DE_ShapeFixParameters& theShapeFixParameters = {})` (a `TKDE` default in a `TKXSBase` signature)

- **Rule**

    - The `handle<T>` caster instantiates `typeid(T)`, so a forward declaration is not enough: `_TKDE` would fail to link with `Undefined symbols: typeinfo for TDocStd_Document, typeinfo for XSControl_WorkSession`.
    - The **import** list is EXTERNLIB plus the extra toolkits that come *earlier* in the canonical order: `_TKXSBase` imports `_TKDE` because `XSAlgo_ShapeProcessor(…, const DE_ShapeFixParameters& = {})` has a default nanobind converts at `.def` time, while `_TKDE` does not import `_TKXSBase` — a toolkit generated *later* can never be needed at an earlier one's registration time (when the earlier one was generated its classes were not in the manifest, so such a base or default would have been skipped), and importing it back would be a cycle.
    - `TKDE` (→ `TKLCAF`, `TKXSBase`), `TKXSBase` (→ `TKDE`), `TKDECascade`, `TKDEGLTF`, `TKDEOBJ`, `TKDEPLY`, `TKDESTL` (→ `TKXSBase`) and `TKService` (→ `TKGeomBase`, `overrides.toml [link] extra`) are the toolkits that need extra libraries (`src/cpp/toolkits.cmake`).

- **Python**

    - The module links that toolkit too: the generator collects the toolkits owning the headers it emitted (`Emitter.includes`, `OcctTree.toolkit_of_header`), subtracts the EXTERNLIB closure and writes `set(NANOCCT_<TK>_EXTRA_LIBS …)` into `src/cpp/toolkits.cmake`, which `CMakeLists.txt` adds to the link line.

- **Python examples**

    ```python
    from nanocct.DE import DE_Provider
    from nanocct.NCollection import NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString
    from nanocct.XSAlgo import XSAlgo_ShapeProcessor

    reads = [line for line in DE_Provider.Read.__doc__.splitlines() if line.startswith("Read(")]
    assert any("nanocct.XSControl.XSControl_WorkSession" in line for line in reads)   # a TKXSBase type
    assert any("nanocct.TDocStd.TDocStd_Document" in line for line in reads)          # a TKLCAF type

    # the DE_ShapeFixParameters default (TKDE) is converted when TKXSBase registers the constructor
    processor = XSAlgo_ShapeProcessor(NCollection_DataMap__TCollection_AsciiString__TCollection_AsciiString())
    assert type(processor).__name__ == "XSAlgo_ShapeProcessor"
    ```
### R-IMPORT-BASE

- **C++ Idiom**

    A class whose base another toolkit binds: `NCollection_Shared<T>` wrapping a `T` bound elsewhere (7a, "wraps"), or a class deriving from such an instantiation

- **OCCT examples**

    `TKMesh` wraps a `TKBool` `DataMap`; `XmlObjMgt_RRelocationTable` : `NCollection_DataMap<int, handle<Standard_Transient>>`, which `TKBinL` binds:

    - `class NCollection_Shared : public Standard_Transient, public T` (`NCollection_Shared.hxx:35–38`)
    - `typedef NCollection_Shared<NCollection_DataMap<TopoDS_Shape, int, TopTools_ShapeMapHasher>> IMeshData::DMapOfShapeInteger` (`TKMesh`; the `DataMap` is bound by `TKBool`)
    - `class XmlObjMgt_RRelocationTable : public NCollection_DataMap<int, occ::handle<Standard_Transient>>`
    - `const NCollection_List<double>& TDataStd_RealList::List() const` (`TKLCAF`; `NCollection_List<double>` is bound by `TKGeomBase`)

- **Rule**

    - `NCollection_Shared<T>` derives from `T`, so nanobind aborts the import with *"base type … not known to nanobind"* if the base is not registered.
    - OCCT's link graph has no such edge, and ordering `nanocct/all.py` alone is not enough: another module's import chain can reach the wrapper first (`_TKV3d` → `_TKMesh`).
    - **A signature using an instantiation another toolkit binds** gets the same edge (7a ownership: the first package in emit order that needs an instantiation binds it, every later user only uses it): without it the member is uncallable until something else loads the owner -- `TDataStd_RealList.List()` with only TKLCAF imported would raise *"Unable to convert function return value"* (`NCollection_List<double>` is TKGeomBase's).
    - The owner precedes the class using it in emit order, so this edge cannot close a cycle; `tests/test_import.py` imports each toolkit alone and checks that no signature names an instantiation raw that another toolkit binds.

- **Python**

    - The wrapper's module **imports** the base's, and `nanocct/all.py` orders them accordingly.

- **Python examples**

    ```python
    from nanocct.IMeshData import DMapOfShapeInteger
    from nanocct.TDataStd import TDataStd_RealList
    from nanocct.XmlObjMgt import XmlObjMgt_RRelocationTable

    # the bases, bound by TKBool and TKBinL, are registered before TKMesh and TKXmlL derive from them
    assert DMapOfShapeInteger.__mro__[1].__name__ == "NCollection_DataMap__TopoDS_Shape__int__TopTools_ShapeMapHasher"
    assert XmlObjMgt_RRelocationTable.__mro__[1].__name__ == "NCollection_DataMap__int__Handle_Standard_Transient"

    values = TDataStd_RealList()
    values.Append(1.5)
    assert list(values.List()) == [1.5]                # NCollection_List<double>, bound by TKGeomBase
    ```
### R-PRELUDE

- **C++ Idiom**

    Header that is not self-contained

- **OCCT examples**

    `GeomGridEval_Line.hxx` calls `Geom_Line::Lin()` with `gp_Lin` only forward-declared; `IntWalk_PWalking.hxx` names `handle<IntSurf_LineOn2S>` and `ChFiKPart_ComputeData_ChPlnCon.hxx` `ChFiDS_ChamfMode` without any declaration:

    - `const gp_Lin& aLin = myGeom->Lin();` in the inline `GeomGridEval_Line::EvaluateGrid` (`GeomGridEval_Line.hxx:66`), with `class gp_Lin;` only (`Geom_Line.hxx:26`)
    - `const occ::handle<IntSurf_LineOn2S>& IntWalk_PWalking::Line() const` (`IntWalk_PWalking.hxx:120`)
    - `bool ChFiKPart_MakeChamfer(TopOpeBRepDS_DataStructure& DStr, const occ::handle<ChFiDS_SurfData>& Data, const ChFiDS_ChamfMode theMode, …)` (`ChFiKPart_ComputeData_ChPlnCon.hxx:20–22`)
    - `const occ::handle<Adaptor2d_Curve2d>& Contap_Line::Arc() const` (`Contap_Line.hxx:80`, an extra header of `HLRTopoBRep.cpp`)

- **Rule**

    - Reported.
    - A survey of all 1 494 ModelingAlgorithms headers finds only these two cases in umbrella order; the include-list check finds the Contap case.

- **Python**

    - The parser reads `incomplete type 'X'`, `use of undeclared identifier 'X'` or `unknown type name 'X'` from the diagnostics, includes `X.hxx` before the package headers and parses again; the generated `.cpp` includes it first too.
    - The same loop runs on the **emitted include list** of every package (`parse.include_prelude`, one TU with bodies skipped): the identifier-based extra includes may pull in a header that is not self-contained (`HLRTopoBRep.cpp` includes `Contap_Contour.hxx`, whose `Contap_Line.hxx` names `handle<Adaptor2d_Curve2d>` undeclared).

- **Python examples**

    ```python
    from nanocct.Geom import Geom_Line
    from nanocct.GeomGridEval import GeomGridEval_Line
    from nanocct.gp import gp_Dir, gp_Pnt
    from nanocct.IntWalk import IntWalk_PWalking
    from nanocct.NCollection import NCollection_Array1__double

    params = NCollection_Array1__double(1, 2)
    params.SetValue(1, 0.0)
    params.SetValue(2, 2.0)
    points = GeomGridEval_Line(Geom_Line(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0))).EvaluateGrid(params)
    assert points.Value(2).X() == 2.0                  # parsed with <gp_Lin.hxx> included first
    assert hasattr(IntWalk_PWalking, "Line")           # parsed with <IntSurf_LineOn2S.hxx> included first
    ```
### R-SKIP-HEADER

- **C++ Idiom**

    Public header including a private `.pxx` that is not installed

- **OCCT examples**

    `GeomBndLib_Line.hxx`, `_Line2d`, and `GeomBndLib_Curve.hxx`/`_Curve2d.hxx` which include them; OCCT 8.0.1 packaging bug:

    - `#include <GeomBndLib_InfiniteHelpers.pxx>` (`GeomBndLib_Line.hxx:18`, `GeomBndLib_Line2d.hxx:18`; the file is only in the OCCT source, `src/ModelingData/TKGeomBase/GeomBndLib/`)
    - `#include <GeomBndLib_Line.hxx>` (`GeomBndLib_Curve.hxx:22`)
    - `#include <GeomBndLib_Line2d.hxx>` (`GeomBndLib_Curve2d.hxx:22`)

- **Rule**

    - `BndLib_Add3dCurve` and the per-type `GeomBndLib_Circle` … classes remain.

- **Python**

    - Skipped via `overrides.toml [skip] headers`.

- **Python examples**

    ```python
    import nanocct.GeomBndLib as GeomBndLib
    from nanocct.Bnd import Bnd_Box
    from nanocct.BndLib import BndLib_Add3dCurve
    from nanocct.GC import GC_MakeCircle
    from nanocct.GeomAdaptor import GeomAdaptor_Curve
    from nanocct.GeomBndLib import GeomBndLib_Circle
    from nanocct.gp import gp_Pnt

    assert not hasattr(GeomBndLib, "GeomBndLib_Line") and not hasattr(GeomBndLib, "GeomBndLib_Curve")
    circle = GC_MakeCircle(gp_Pnt(-1, 0, 0), gp_Pnt(0, 1, 0), gp_Pnt(1, 0, 0)).Value()
    box = Bnd_Box()
    BndLib_Add3dCurve.Add_s(GeomAdaptor_Curve(circle), 0.0, box)   # any curve type
    assert abs(box.CornerMax().Y() - 1.0) < 1e-9
    assert abs(GeomBndLib_Circle(circle).Box(0.0).CornerMax().Y() - 1.0) < 1e-9   # the per-type class
    ```
### R-TEMPLATE-SKIP

- **C++ Idiom**

    Function/class templates in a namespace or at package level that no typedef instantiates, type aliases in a namespace whose target is not bound (member templates: R-UNSUPPORTED)

- **OCCT examples**

    - `template <typename FuncSetType> VectorResult MathSys::Newton(FuncSetType& theFunc, const math_Vector& theStart, const math_Vector& theTolX, double theTolF, size_t theMaxIter = 100)` (`MathSys::Newton<FuncSetType>`)
    - `typedef std::deque<gp_Pnt, NCollection_OccAllocator<gp_Pnt>> IMeshData::Model::SequenceOfPnt` (an alias of a type that is not bound)
    - `template <class TheConfType> class DE_PluginHolder` (a package-level class template no typedef instantiates)
    - `using GeomGridEval::CurveD1 = Geom_Curve::ResD1;` (an alias of a bound class: bound, R-ALIAS)

- **Rule**

    - Need a concrete functor type.
    - The classic `math_*` classes are the Python-facing API.
    - A class template is bound per instantiation (7c): one that no typedef instantiates has no class to bind (`DE_PluginHolder<T>`, reported as `template (not bound)`).

- **Python**

    - Not bound, reported.

- **Python examples**

    ```python
    import nanocct.DE as DE
    import nanocct.GeomGridEval as GeomGridEval
    import nanocct.IMeshData as IMeshData
    import nanocct.MathSys as MathSys
    from nanocct.Geom import Geom_Curve
    from nanocct.math import math_NewtonFunctionSetRoot

    assert not hasattr(MathSys, "Newton")              # a function template: no concrete functor type
    assert hasattr(math_NewtonFunctionSetRoot, "Perform")   # the classic class
    assert not hasattr(IMeshData, "Model")             # IMeshData::Model holds only aliases of std::deque
    assert GeomGridEval.CurveD1 is Geom_Curve.ResD1    # an alias of a bound class (R-ALIAS)
    assert not hasattr(DE, "DE_PluginHolder")          # a package-level class template, no typedef
    ```
### R-TEMPLATE-BASE

- **C++ Idiom**

    A base that is itself a template instantiation

- **OCCT examples**

    - `template <class T, int N> class BVH_PrimitiveSet : public BVH_Object<T, N>, public BVH_Set<T, N>` (`BVH_PrimitiveSet<double, 3> : BVH_Object<double, 3>`)
    - `class BRepExtrema_ProximityDistTool : public BVH_Distance<double, 3, BVH_Vec3d, BRepExtrema_TriangleSet>` (`BVH_Distance<…> : BVH_Traverse<…> : BVH_BaseTraverse<double>`)
    - `class BRepExtrema_TriangleSet : public BVH_PrimitiveSet3d` (a typedef)
    - `class BRepExtrema_OverlapTool : public BVH_PairTraverse<double, 3>` (defaulted arguments)
    - `template <class T, int N> class BVH_Box : public BVH_BaseBox<T, N, BVH_Box>` (the CRTP base, `template <class T, int N, template <class /*T*/, int /*N*/> class TheDerivedBox> class BVH_BaseBox` empty, its members in `class BVH_BaseBox<T, 3, BVH_Box>`)

- **Rule**

    - A base that is itself a template instantiation is only spellable after substitution (`BVH_PrimitiveSet<double, 3> : BVH_Object<double, 3>`, `BVH_Distance<…> : BVH_Traverse<…> : BVH_BaseTraverse<double>`).
    - Whether an instantiation is abstract only the compiler can tell (`BVH_PrimitiveSet<double, 3>` through `BVH_Set`'s pure virtuals).
    - Two template bodies OCCT cannot compile for the argument are in `overrides.toml`: `BVH_PairTraverse<…, void, double>::Select()` and the whole `BOPTools_PairSelector<2>` (an OCCT bug).

- **Python**

    - Such spellings are collected during the walk and resolved by a **probe re-parse** — the package umbrella plus one `using nanocct_probe_i = <spelling>;` per base gives each a libclang `Type` to instantiate from (up to four rounds for deeper chains).
    - A base written through a typedef (`BRepExtrema_TriangleSet : BVH_PrimitiveSet3d`) or with defaulted arguments (`BVH_PairTraverse<double, 3>`) is named as the instantiation is (canonical arguments).
    - What still cannot be instantiated — the empty CRTP base `BVH_BaseBox<T, N, BVH_Box>` with its template template parameter and a partial specialisation holding the members, the `rapidjson` bases of `RWGltf_GltfJsonParser` and `RWGltf_GltfOStreamWriter` — is **dropped from the derived class's bases** (reported; the base's members are not inherited: `BVH_Box.Transform/Transformed`) instead of skipping the class; a Transient class whose only path to `Standard_Transient` was such a base is skipped.
    - `NCollection_UBTree<int, Bnd_Box>::Selector` (a nested class of an instantiation) is bound with its instantiation (7c, nested classes), so the internal `*BndBoxTreeSelector*` classes keep it as their base, with the `Selector` interface.
    - The constructors of an instantiation are registered inside `nanocct_if_concrete<T>` (a generic lambda, instantiated only when `!std::is_abstract_v<T>`).
    - This binds the BVH chain end to end: `BRepExtrema_ShapeProximity` with `ProxPntStatus*`, `ElementSet1/2` (`BRepExtrema_TriangleSet`), `OverlapSubShapes1/2`, `BRepExtrema_ProximityDistTool/OverlapTool`, `BOPTools_BoxTree`, `IntPatch_PolyhedronBVH`.

- **Python examples**

    ```python
    from nanocct.Bnd import BVH_Box__double__3
    from nanocct.BRepClass3d import BRepClass3d_BndBoxTreeSelectorPoint
    from nanocct.BRepExtrema import BRepExtrema_OverlapTool, BRepExtrema_ProximityDistTool, BRepExtrema_TriangleSet
    from nanocct.BVH import BVH_PrimitiveSet3d

    assert [c.__name__ for c in BRepExtrema_ProximityDistTool.__mro__[1:4]] == [
        "BVH_Distance__double__3__NCollection_Vec3__double__BRepExtrema_TriangleSet",
        "BVH_Traverse__double__3__BRepExtrema_TriangleSet__double", "BVH_BaseTraverse__double"]
    assert BRepExtrema_TriangleSet.__mro__[1] is BVH_PrimitiveSet3d                 # through a typedef
    assert BRepExtrema_OverlapTool.__mro__[1].__name__ == "BVH_PairTraverse__double__3__void__double"
    assert not hasattr(BVH_Box__double__3, "Transform") and hasattr(BVH_Box__double__3, "Add")   # base dropped
    assert BRepClass3d_BndBoxTreeSelectorPoint.__mro__[1].__qualname__ == "NCollection_UBTree__int__Bnd_Box.Selector"
    try:
        BVH_PrimitiveSet3d()                           # abstract: no constructor registered
        raise AssertionError("BVH_PrimitiveSet<double, 3> is abstract")
    except TypeError:
        pass
    ```
### R-ARRAY

- **C++ Idiom**

    Array parameter or member that R-FIXED-ARRAY cannot express: unknown size (`const double theCoeff[]`), pointers (`const Poly_CoherentTriangle *pTri[2]`), std types (`std::array<std::complex>`)

- **OCCT examples**

    - `void BRepGProp_Gauss::Compute(const BRepGProp_Face& theSurface, const gp_Pnt& theLocation, const double theCoeff[], const bool theIsByPoint, double& theOutMass, gp_Pnt& theOutGravityCenter, gp_Mat& theOutInertia)` (`BRepGProp_Gauss`: unknown size)
    - `bool Poly_CoherentTriangulation::FindTriangle(const Poly_CoherentLink& theLink, const Poly_CoherentTriangle* pTri[2]) const` (pointers)
    - `std::array<std::complex<double>, THE_MAX_POLY_DEGREE> MathPoly::GeneralPolyResult::ComplexRoots = {}` (a std type)
    - `bool IntImp_ComputeTangence(const gp_Vec DPuv[], const double EpsUV[], double Tgduv[], IntImp_ConstIsoparametric TabIso[])` (a free function)

- **Rule**

    - Reported: 7<!-- count: array-lines --> lines.

- **Python**

    - Skipped.

- **Python examples**

    ```python
    import nanocct.MathPoly as MathPoly
    from nanocct.BRepGProp import BRepGProp_Gauss
    from nanocct.Poly import Poly_CoherentTriangulation

    overloads = [line for line in BRepGProp_Gauss.Compute.__doc__.splitlines() if line.startswith("Compute(")]
    assert len(overloads) > 0 and all("theCoeff" not in line for line in overloads)
    assert not hasattr(Poly_CoherentTriangulation, "FindTriangle")
    assert not hasattr(MathPoly.GeneralPolyResult(), "ComplexRoots")
    ```
### R-DELETED

- **C++ Idiom**

    Deleted members, move constructors

- **OCCT examples**

    - `gp::gp() = delete` (`gp.hxx:47`)
    - `GeomGridEval_Line::GeomGridEval_Line(const GeomGridEval_Line&) = delete`
    - `GeomGridEval_Line::GeomGridEval_Line(GeomGridEval_Line&&) = delete`
    - `TCollection_AsciiString::TCollection_AsciiString(TCollection_AsciiString&& theOther)` (a move constructor)

- **Rule**

    - Reported for methods (a `deleted` report line); deleted constructors, move constructors and `operator=` are skipped without a report line.

- **Python**

    - Skipped.

- **Python examples**

    ```python
    from nanocct.GeomGridEval import GeomGridEval_Line
    from nanocct.gp import gp
    from nanocct.TCollection import TCollection_AsciiString

    try:
        gp()                                           # gp() = delete: no constructor
        raise AssertionError("gp() is deleted")
    except TypeError:
        pass
    assert gp.Origin_s().X() == 0.0                    # the static members are bound
    inits = [line for line in GeomGridEval_Line.__init__.__doc__.splitlines() if line.startswith("__init__(")]
    assert len(inits) == 1                             # no copy or move constructor
    assert "theOther:" not in TCollection_AsciiString.__init__.__doc__   # the move constructor is not bound
    ```
### R-UNSUPPORTED

- **C++ Idiom**

    Raw pointers to primitives (also when they appear as `T*` in a 7c instantiation), references to pointers (`char*&`), pointers to incomplete types (`_xlocale*`), C-array fields that R-FIXED-ARRAY cannot express (R-ARRAY), reference-typed fields, template members, nested class templates, non-public bases, `std::ostream&` *returns* and stream members

- **OCCT examples**

    `NCollection_Mat4<float>::Map(float*)`, `math_VectorBase<double>(const double* theTab, …)`; stream members of `BinTools_IStream`, `Message_PrinterOStream`:

    - `static NCollection_Mat4<Element_t>& NCollection_Mat4::Map(Element_t* theData)` (`NCollection_Mat4<float>::Map(float*)`)
    - `math_VectorBase::math_VectorBase(const TheItemType* theTab, const int theLower, const int theUpper)` (`math_VectorBase<double>(const double* theTab, …)`)
    - `bool Transfer_Finder::GetStringAttribute(const char* const name, const char*& val) const` (a reference to a pointer)
    - `Standard_OStream& Message_PrinterOStream::GetStream() const` (a `std::ostream&` return)
    - `Standard_IStream& BinTools_IStream::Stream()` (a stream member)

- **Rule**

    - Reported.
    - A raw pointer to a primitive in a 7c instantiation — `NCollection_Mat4<float>::Map(float*)`, `math_VectorBase<double>(const double* theTab, …)` — would take a pointer to a temporary.

- **Python**

    - Skipped.

- **Python examples**

    ```python
    from nanocct.BinTools import BinTools_IStream
    from nanocct.BVH import BVH_Mat4f
    from nanocct.math import math_Vector
    from nanocct.Message import Message_PrinterOStream
    from nanocct.Transfer import Transfer_Finder

    assert not hasattr(BVH_Mat4f, "Map")               # NCollection_Mat4<float>::Map(float*)
    assert "theTab" not in math_Vector.__init__.__doc__   # math_VectorBase<double>(const double* theTab, ...)
    assert not hasattr(Transfer_Finder, "GetStringAttribute")   # const char*& val
    assert hasattr(Transfer_Finder, "StringAttribute")          # OCCT's value-returning twin
    assert not hasattr(Message_PrinterOStream, "GetStream")
    assert not hasattr(BinTools_IStream, "Stream")
    ```

## 7a. NCollection containers (hand-written binders)

### Facts

- OCCT 8.0.1 spells containers directly in its API (`Geom_BSplineCurve(const NCollection_Array1<gp_Pnt>& Poles, …)`; 2050 distinct `NCollection_*<…>` spellings in the installed headers).
- The pre-8.0 typedef names (`TColgp_Array1OfPnt`, `TopTools_ListOfShape`, 972 headers) live in `src/Deprecated/NCollectionAliases`, outside every toolkit, each marked deprecated with "use `NCollection_Array1<gp_Pnt>` directly". The reference documentation for the container API is therefore the template class page.
- `NCollection_HArray1<T>` derives from both `NCollection_Array1<T>` and `Standard_Transient`; `NCollection_Array1` has a virtual destructor (polymorphic).

### Design

- One hand-written C++ binder per template kind in `src/cpp/common/nanocct_ncollection.h` (`nanocct::bind_NCollection_Array1<T>(module, name)`, `bind_NCollection_HArray1<T>`), instantiated by the generator.
- The alternative — instantiating template members generically via libclang with argument substitution — is not used: dependent types, `enable_if` overloads and members that do not compile for every element type would each need a special rule, for the same user-visible result.
- All 15 container kinds of the scope are bound.

### Which instantiations, and their names

- **Which:** every `NCollection_X<…>` (also inside `handle<…>`, also nested) that appears in a bound signature, collected while parsing; nested arguments and `requires` (`Array1<T>` before `HArray1<T>`) are bound first. Over-approximation (unused instantiations) only costs compile time. A template that *is* a binder kind's nested class (`NCollection_TListIterator<T>` = `NCollection_List<T>::Iterator`, `BINDERS[...]["nested_from"]`) registers the owner instantiation instead of a 7c class of its own (`TopOpeBRepDS_HDataStructure::SameDomain` returns `NCollection_List__TopoDS_Shape.Iterator`; binding it twice aborted the import).
- **Primary spelling `NCollection_Array1[T]`**: `nanocct.NCollection.NCollection_Array1[gp.gp_Pnt](1, 4)` mirrors the docs' `NCollection_Array1<gp_Pnt>`.
    - `NCollection_Array1` is a small generated class (a subclass of `Generic` in `nanocct/_templates.py`) whose `_instances` table, written into the `NCollection` shim from `manifest.json`, maps the Python element types to the bound classes: `float → double`, `int → int`, `bool → bool`, `str → std::string`, the markers `float32`, `uchar`, `uint`, `ulong`, `ulonglong` for the C++ scalars without a Python type, an OCCT class for itself **and** for `handle<class>`, a bound instantiation for a nested container. **Every bound container instantiation is reachable this way** (`tests/test_NCollection.py` asserts it). The markers are keys only: they live in `nanocct/_templates.py`, subclass `float`/`int` (the values are plain Python floats and ints, converted and range-checked by the bound class), and are aliases of `float`/`int` in the stubs, because precision is not a Python type — every C++ scalar parameter of the bindings is typed by its Python type the same way. So a type checker does not tell `NCollection_HArray1[float32]` from `NCollection_HArray1[float]`; handing the wrong one to OCCT fails at runtime (`TypeError`). A C++ name in the brackets (`NCollection_Array1['double']`) raises a `TypeError` naming the Python spelling. The keys are the types themselves, as Python passes them to `__class_getitem__` (the type for one argument, a tuple for several), so `NCollection_Array1[gp_Pnt]` is one dict lookup and returns `NCollection_Array1__gp_Pnt` itself; a key the generator spelled wrong fails at import instead of degrading into "not bound".
    - **`isinstance(x, NCollection_Array1)`** holds for every instantiation and for everything C++ derives from one: `HArray1<T>` and `Array2<T>` are `Array1<T>`, `HArray2<T>` is `Array2<T>` and `Array1<T>`, `HSequence<T>` is `Sequence<T>`, `NCollection_Shared<T>` is `T` -- one rule for all 15 kinds, decided on the class's MRO by an `abc` `__subclasshook__`, and pinned by `tests/test_NCollection.py` (every instantiation against its own generic, and exactly the C++ bases, nothing else). The relation is virtual: `__mro__` does not list the generic class. A real base is impossible because nanobind allows one base and the four derived kinds already use it for their C++ base (`HArray1<T> : Array1<T>`), which is what lets an `HArray1` be passed where OCCT takes an `Array1&`; tag base classes for the other 11 kinds are not used, for exactly that inconsistency (measured).
    - Cost (M5): the subscription itself ~60 ns; `A = NCollection_Array1[gp_Pnt]` once and `A(1, 100)` in a loop costs the same as `NCollection_Array1__gp_Pnt(1, 100)` (both are the same class). Across build123d, cadquery, ocp_tessellate, ocpsvg and ocp_gordon, few container constructions sit inside a loop, each next to µs of OCCT work.
    - Other C++ scalars (`float`, `size_t`, `char`…) are reachable only by the concrete name.
    - An unbound combination raises `TypeError` naming it (`NCollection_Array1[gp_Pnt, gp_Pnt] is not bound by nanocct`) and `NCollection_Array1.bound()` lists what is; calling the template itself raises `TypeError` with a hint.
- **Concrete classes:** one per C++ instantiation, named `template__arg1__arg2` (double underscore separates arguments — OCCT names never contain `__`; `handle<X>` → `Handle_X`; nested left to right; defaulted template arguments such as hashers are omitted): `NCollection_DataMap__TopoDS_Shape__Handle_Geom_Surface`. They are what `type()`, `repr` and stubs show.
    - All of them live in **`nanocct.NCollection`** (the doc page's package), bound by the first toolkit that needs them (`manifest.json` records `by`, the binding package, so regeneration is idempotent — verified by running the generator twice).
    - **`nanocct.NCollection` is the one module a later toolkit writes into**, and the only one: every 7c instantiation is bound by the package that declares it. So `import nanocct` imports nothing, each `nanocct.<pkg>` shim pulls in its own toolkit (which imports what its registration needs), and **importing `nanocct.NCollection` imports every toolkit that binds an instantiation into it** (33<!-- count: ncollection-eager -->), so every instantiation is an ordinary attribute afterwards. The OCCT design forces it: loading an instantiation's element types does not load the toolkit that binds it (e.g. `NCollection_Array1<handle<Geom2d_BSplineCurve>>` is bound after TKG2d), so a lazy table keyed by what is loaded answers differently depending on import order, and the alternative -- a `{class name -> binding toolkit}` table with a module `__getattr__` -- is machinery that would serve only this one package. Measured: `import nanocct.NCollection` ~160 ms (a lazy table: 8 ms); after `import build123d`, which already loads 31 toolkits and imports `NCollection`, +28 ms; `from nanocct.gp import gp_Pnt` does not import `NCollection` and loads `_TKernel` and `_TKMath` alone (13 ms; all 45 toolkits would cost 172 ms and 179 MB). No C++-side state is involved, so nothing here stands in the way of a free-threaded (`abi3t`) build.
    - Three toolkits link a toolkit that comes *later* in the order and therefore cannot import it at registration time (R-LINK: `TKDE`, `TKDECascade`, `TKDEGLTF` -> `TKXSBase`). Their shims import it afterwards, at Python level, or the members naming those types are uncallable.
- **The pre-8.0 typedef names are not exposed.** `TColgp_Array1OfPnt`, `TopTools_ListOfShape`, `Graphic3d_Vec3` and the rest of `src/Deprecated/NCollectionAliases` are not bound, and neither are the alias-only modules they would need (`TColgp`, `TColGeom`, `TColGeom2d`). nanocct binds OCCT 8 and code using it spells the 8.0 names — the container itself (`NCollection_Array1[gp_Pnt]`, `nanocct.NCollection.NCollection_List__TopoDS_Shape`). **7c aliases are unaffected**: `TColStd_PackedMapOfInteger`, `BVH_Vec3d` and their kind are typedefs OCCT still declares, bound as real classes under the alias name, not as Python-level aliases.
- **`[instantiate]` override:** instantiations to bind although no bound OCCT signature uses them (`NCollection_Map<int>`, `NCollection_DataMap<int, double>`, …), registered by the `NCollection` package. Used to exercise binders that the current scope does not reach yet, and available for user conveniences.

### Methods, docstrings, Python additions

- **1:1 methods** with OCCT names and signatures.
- **Docstrings extracted from the template header** by the generator into `ncollection_docs.h` (first overload wins).
- A **coverage check** reports template members that are neither bound nor listed as knowingly skipped (`Move`, `operator=`, `EmplaceValue`, iterators, allocation operators).
- **Python additions** (never replacements, marked "Python addition" in their docstrings): `__len__` (= `Length`), `__iter__` (values `Lower()..Upper()`), `__setitem__` (= `SetValue`). `__call__` and `__getitem__` are OCCT's own `operator()`/`operator[]` = `Value` with the **OCCT index**, not 0-based.
- `Change*` accessors are bound only for class element types (`double&` cannot be exposed).

### The H-types: HArray1 / HArray2 / HSequence / Shared (see 4.2 "Multiple inheritance")

- Bound with the offset-0 base (`Array1<T>`, `Array2<T>`, `Sequence<T>`, `T`), so the container API is inherited with an exact pointer and `isinstance(h, NCollection_Array1[T])` holds.
- `GetRefCount`, `DynamicType`, `IsKind`, `IsInstance`, `get_type_*` are bound through adjusting casts; handles convert both ways through the MI registry.
- `h.Array1()` returns a sliced copy of static type `Array1` (returning `const A&` would make nanobind copy the dynamic type); `h.ChangeArray1() is h`.
- Stubs: the H-types derive from the generic container class; `NCollection_Shared[T]` is typed as an accessor with one overload per bound instantiation returning the concrete class (which derives from `T`'s class), because `Generic[_T]` cannot derive from `_T`.
- nanobind copy-constructs the *dynamic* type for polymorphic by-value/const-reference returns whenever that type is registered. For a Transient class that is an owned private copy with reference count 0, which is **not** harmless: the first `handle<T>` parameter it meets deletes memory nanobind owns. So a Transient returned by value goes into a handle (R-RESULT), and the handle caster refuses a count-0 Transient.

### List / Sequence / HSequence

- Nested `Iterator` classes bound as `NCollection_List__int.Iterator` (1:1 with `NCollection_List<T>::Iterator`; `TopTools_ListIteratorOfListOfShape`-style aliases resolve to them), with `nb::keep_alive` on the container; they are iterable (R-ITER: `iter(it)` is an `nb::make_iterator` yielding `Value()` while `More()`, which advances `it` itself; the object has no `__next__`; all seven binder kinds with an `Iterator`).
- **A class deriving from a binder's nested Iterator** (`Graphic3d_SequenceOfHClipPlane::Iterator : NCollection_Sequence<handle<Graphic3d_ClipPlane>>::Iterator` — the only way to iterate a view's clip planes, `myItems` being protected) **or from a binder instantiation itself** (`BinObjMgt_RRelocationTable : NCollection_DataMap<int, handle<Standard_Transient>>`, `XmlObjMgt_RRelocationTable`, `XmlObjMgt_SRelocationTable : NCollection_IndexedMap<handle<Standard_Transient>>`) is declared in the **templates phase**, after the instantiation that registers its base (`Class.after_templates`; the parser spells the base with the manifest key — canonical arguments, defaults such as the hasher left out — and registers the owner instantiation). The declare phase of every package runs before any templates phase, so the base would not exist yet otherwise. The derived class inherits the container's Python API (`table.IsEmpty()`, `Extent()`, `Bind`, …).
- `size_t` overloads that duplicate `int` ones are not bound (Python cannot distinguish them); `At`/`ChangeAt` (size_t only) are.
- `Contains`/`Remove(item)`/`__contains__` are bound only when `T` has `operator==` (compile-time trait; `gp_Pnt` has none, `TopoDS_Shape` has).
- Members returning the inserted element (`Append` → `T&`) return a view for class types and a value for scalars.
- Members inherited from the non-template bases (`NCollection_BaseList::Extent`, …) are covered by the docs/coverage extractor via `bases`.
- Python additions: `__len__`, `__iter__`, `__contains__`, and for Sequence `__getitem__`/`__setitem__` (1-based like `Value`).
- Generic stubs for the three kinds; verified with mypy and ty. Divergence: ty rejects `NCollection_List[int].Iterator` (nested class through a specialised generic), mypy accepts it — typed code uses the concrete `NCollection_List__int.Iterator`.
- **Ordering lesson:** instantiations are registered in the toolkit's *declaration* order, so packages are also *emitted* in that order; otherwise an `HSequence<T>` bound by an early-running package could precede the `Sequence<T>` its implicit conversion needs (observed as `implicitly_convertible: destination type unknown`).

### Map / DataMap / IndexedMap / IndexedDataMap

- The hasher template argument is dropped from key and name only when it equals its default `NCollection_DefaultHasher<Key>` (`defaults` per kind in `BINDERS`, applied by `instance_args`); a custom hasher stays part of both, so it cannot be merged with the default instantiation (a different C++ type).
- Shared base members (`NCollection_BaseMap`: `NbBuckets`, `Extent`, …) in one helper.
- `Seek`/`ChangeSeek` return `None` for absent keys; `ChangeSeek` is a view for class items, `Seek` (and `DoubleMap`'s `Seek1`/`Seek2`, which return a key) a copy as `Find` is -- a `const` pointer bound as a view would be writable from Python and could corrupt a `DoubleMap`'s keys; scalars are values; `Find(key, item&)`/`FindFromKey(key, item&)` only for class items (in-place).
- Skipped: `Contained` (`std::optional<std::reference_wrapper<…>>`), `Emplace*`, `Items()`/`IndexedItems()` views, `GetHasher`.
- Python additions: `__len__`, `__contains__`, `__iter__` over keys (index order for the indexed kinds), `__getitem__`/`__setitem__`/`__delitem__` on DataMap (`Find`/`Bind`/`UnBind`, `KeyError` when unbound), `__getitem__(index)` on the indexed kinds, `items()` → list of `(key, value)`.
- The indexed maps' iterators do not derive from `NCollection_BaseMap::Iterator` (no `Initialize`/`Reset`), the others do.
- Enums count as element types (`NCollection_IndexedMap[Message_MetricType]`).

### Array2 / HArray2 / DynamicArray / DoubleMap / Shared

- `Array2<T>` derives from `Array1<T>` in 8.0 and inherits its binding (`__len__`/`__iter__` are flat, row-major; `Value(i)` is hidden by `Value(row, col)` as in C++; `a[(row, col)]` is the Python addition).
- `DynamicArray` is 0-based (`Lower() == 0`).
- `DoubleMap` has two default hashers (both stripped when default); iteration yields `(key1, key2)` pairs.
- `Shared<T>` requires `T` to be bound (class or instantiation), otherwise the instantiation is skipped with a report (`Standard_HMutex = Shared<Standard_Mutex>` is skipped because `Standard_Mutex` is not bound).

### Elements with OCAF owners (R-OWNER)

- A container keeps the owners of every element Python puts in (`own`/`own_all` in each writing member: `Append`, `SetValue`, `Bind`, `Add`, `Assign`, `Exchange`, the map set operations, …); an element copied out (`Value`, `First`, `Find`, `FindKey`, `items()`, an iterator's `Value()`/`Key()`) keeps its own (`owned`, returning `nb::typed<nb::object, T>` so the stubs keep `T`); a lookup that writes into an argument (`Find(key, item)`) gives it the owners (`own_out`); a copy of the container keeps its source (`keep_if_owned`). A container a bound call fills is covered by R-OWNER's policy on that call (`GetFreeShapes(labels)`).
- For every other element type these compile to nothing (`owners<T>::active` is false; a `keep_if_owned` that does not apply is an empty `nb::call_guard<>`) -- measured: `NCollection_Sequence[int].Value` 21 ns with and without the rule.
- The binders that do not apply it -- Array2/HArray2, DynamicArray, LinearVector, Shared -- `static_assert` that their element type has no owners, so an OCAF instantiation of one does not compile instead of losing its owners silently (none in OCCT 8.0.1).

### Views a container refuses to invalidate (R-VIEW-GUARD)

What invalidates what, read in OCCT 8.0.1's container code. *Any view* = element references, numpy arrays and iterators; *iterators* = iterators only. Everything not listed keeps every view valid (`SetValue`, `Init`, `CopyValues`, `Reverse`, a Sequence's `Exchange(I, J)`, an IndexedMap's `Substitute`/`Swap`, inserting into a List, Sequence, DynamicArray or any map's nodes).

| Container | Refuses while any view lives | Refuses while an iterator lives |
|---|---|---|
| `Array1`, `HArray1` | `Resize` to another length, `Assign` of another size (a new buffer; the same size copies in place) | -- |
| `Array2`, `HArray2` | `Resize`/`ResizeWithTrim` without data to another number of elements, with data to another shape (`resizeImpl` moves `*this` into a temporary); `Assign` of another size | -- |
| `List` | `Clear`, `Assign`, `RemoveFirst`, `Remove(item)`, `Remove(it)` -- except the iterator it goes through; `Exchange` (both lists); the source of `Append`/`Prepend`/`InsertBefore`/`InsertAfter(theOther, …)`, whose nodes move | -- |
| `Sequence`, `HSequence` | `Clear`, `Assign`, `Remove` (also `Remove(it)`, except that iterator); `Split` (both: the tail moves, `theSeq` is cleared); the source of `Append`/`Prepend`/`Insert*(…, theSeq)` | -- |
| `Map`, `DataMap`, `DoubleMap` | `Clear`, `Assign`, `Exchange` (both), `Remove`/`UnBind`/`UnBind1`/`UnBind2`/`__delitem__`; `Map`'s set operations that remove or exchange (`Intersect`, `Intersection`, `Subtract`, `Subtraction`, `Differ`, `Difference`) and `Union` into a third map (it clears) | every insert -- `Add`, `Added`, `Bind`, `TryBind`, `Bound`, `TryBound`, `__setitem__`, `Unite`, `Union` into an operand -- and `ReSize`: the table may grow, and an iterator caches the bucket array the growth frees (`NCollection_BaseMap.hxx`, `Iterator::PNext`); element references live in the nodes, which growth relinks |
| `IndexedMap`, `IndexedDataMap` | `Clear`, `Assign`, `Exchange` (both), `RemoveLast`, `RemoveFromIndex`, `RemoveKey` | -- (an iterator holds the map and an index, `NCollection_IndexedMap.hxx`) |
| `DynamicArray` | `Clear`, `Assign`, `EraseLast` (blocks never move: appends and inserts keep every element in place) | -- |
| `LinearVector` | growing past `Capacity()` (`Append`, `Appended`, `InsertBefore`/`InsertAfter`, `SetValue`/`__setitem__` past the end, `Reserve`, `Resize`), shrinking (`Resize` below `Size()`), `Erase`, `EraseLast`, `Clear` | -- |

- Views come from the binder: `elem_view_of_self` on every member returning an element reference of a class type (`def_elem`, the `Change*` members, `ChangeSeek`), `iterator_of_self` on `__iter__`, `iterator_of_arg` on an `Iterator`'s constructor and `Initialize` (a re-initialised iterator moves to its new container), `elem_view_of_iterator` on an `Iterator`'s `ChangeValue`, `container_array` for `__array__` (`np.array(a)`, `copy=True`, is a copy and no view).
- A scalar or handle element is returned by value and is no view.

### LinearVector

- `NCollection_LinearVector<T>`, OCCT 8's contiguous 0-based vector with `size_t` indices and BRepGraph's container of choice (`NCollection_LinearVector<BRepGraph_NodeId>` …).
- `Data()`/`begin()`/`end()` (raw element pointers) are not bound.
- A typedef of a binder instantiation (`BVH_Array3d = NCollection_LinearVector<NCollection_Vec3<double>>`) is an attribute alias of the concrete class, not a 7c class of its own.
- Container-typed **fields** (`MathRoot::MultipleResult::Roots`) and template arguments of instantiated templates (`NCollection_Iterator<NCollection_DynamicArray<Poly_CoherentTriangle>>`) register their instantiations like parameters do.
- `NCollection_FlatDataMap`/`FlatMap` (BRepGraph's open-addressing maps) are bound as 7c instantiations, with their nested `Iterator`: `for n in NCollection_FlatMap__BRepGraph_NodeId__….Iterator(m)`. Their `Items()` returns an `NCollection_ItemsView::View`, an STL-style range that stays unbound.

## 7b. Type stubs

- `python -m generator.stubs` (after the build; it imports the extension) runs nanobind's `StubGen` (API, recursive: the CLI refuses `-r` for modules without `__file__`) per package module into `src/nanocct/<pkg>.pyi` — or `<pkg>/__init__.pyi` plus `<pkg>/<ns>.pyi` for a package with namespaces (6.1). Cross-references come out as `nanocct.Standard.X` because of the `__module__` rule.
- It adds:
    - the deprecated typedef aliases as assignments — stubgen binds them as `from M import A as B`, which is no re-export; it writes that import on one line when it fits in 70 characters and as a parenthesised block otherwise (nanobind `stubgen.py`); both forms are rewritten (`tests/test_typing.py` asserts that no stub binds a class under another name);
    - in `NCollection/__init__.pyi` a hand-written **`Generic[_T]` class per container kind** (`generator/stubs/<kind>.pyi`, kept in step with the binder -- `tests/test_typing.py` checks every stub member against the runtime) and every instantiation as `class NCollection_Array1__double(NCollection_Array1[float]): ...`; the members the binder binds for some element types only (`Change*` for class elements, `List.Contains` where the element has `operator==`) are not in the generic class but lifted from stubgen's concrete class of each instantiation (an H class from its sibling), like `__array__`;
    - in every other stub, the concrete instantiation names in OCCT signatures rewritten to the generic spelling (`nanocct.NCollection.NCollection_Array1__double` → `nanocct.NCollection.NCollection_Array1[float]`, nested arguments included, missing `import nanocct.<pkg>` lines added), because the checker types `NCollection_Array1[float](…)` as the generic and would otherwise reject passing it to any OCCT method (`Geom2d_BezierCurve(poles)`); the concrete class derives from the generic one, so results stay assignable.
    - **except `NCollection_Shared<T>`**, which derives from T and so has no generic class (its name in the stub is the lookup object `_NCollection_Shared_template`): its instantiations keep their concrete names, `OpenGl_Context.SharedResources() -> nanocct.NCollection.NCollection_Shared__NCollection_DataMap__…` (`NCollection_Shared[…]` would be an unresolved type, and the results `Any`)
    - enum defaults qualified through the parameter's annotation: stubgen writes an enum default by `repr()` (nanobind's `StubGen.expr_str` tests `int` before `enum.Enum`, and OCCT's enums are `IntEnum`), so `Continuity: nanocct.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2` would name an enum its module does not define; it becomes `= nanocct.GeomAbs.GeomAbs_Shape.GeomAbs_C2` (`_qualified_enum_defaults`, 217<!-- count: stub-enum-defaults --> sites, OCCT 8.0.1)
    - **names with one leading or trailing underscore are kept** (`StubGen(..., include_private=True)`): stubgen treats them as private, but here they are C++ names -- the R-KEYWORD enum values (`GProp_PEquation.Type.None_`, five `None_` in BRepGraph), OCCT's own `Image_ColorRGB32.a_()`/`Seta_` and `AdvApp2Var_SysBase.mainial_`, and the eight structs `AIS_ViewInputBuffer::_orientation` & co., which the stubs would otherwise reference without defining (nanocct's own `_Generic` machinery stays out of the NCollection stub)
    - a bare class name that a member of the enclosing class shadows, qualified with its module: `BRepGraphInc_Storage` has a method `EdgeCurve3DRep`, so its `-> EdgeCurve3DRep` would mean the method, not the module's class; likewise `def Status(self) -> Status` in `ExtremaPC`/`MathUtils` (`_unshadowed_class_names`, per class body, a nested class checked against its own members only). The same for a builtin type: `LDOM_SBuffer` (bound on Windows only) has a method `str`, so its `xsputn(self, s: str, ...)` is written `s: builtins.str`, and the stub imports `builtins`.
    - `__eq__`/`__ne__` operands typed `object` (`_eq_accepts_object`): nanobind returns `NotImplemented` for an operand no overload takes, so `TopoDS_Shape() == 1` is `False`, and stubgen's C++ operand type would be an incompatible override of `object.__eq__` (200 `[override]` errors); a single definition gets `object`, an overload set keeps its overloads -- they say which types compare by value, `TCollection_AsciiString == str` -- and gains a last `(self, other: object) -> bool`
- **The 355 per-module stub runs go through a thread pool, one worker per core** (`NANOCCT_JOBS`, 6.2; `=1` is the sequential path): each runs in a subprocess of its own and writes one file nothing else touches — **96.4 s sequentially, 13.7 s pooled, byte-identical at 1, 6 and 18 jobs**. They are 97 % of a sequential run (97.8 s of 100.8 s, 276 ms per module and flat) against 2.9 s for everything after them (the alias assignments, `NCollection.pyi`, the generic rewrite), which reads the files the pool wrote and stays sequential. The `stub <file>` lines keep the sequential order — the futures are awaited in submission order, and `math` is the last of the 355.
- Verified with **mypy** and **ty** (`tests/test_typing.py` runs both on every `tests/typing/check_*.py`): `a[2]` is `float`, `h.Value(1)` is `Standard_Persistent`, `def f(arr: NCollection_Array1[float])` accepts every double array, nested classes and namespace modules resolve (`check_namespaces.py`), and the deliberate errors (wrong element type, wrong overload, `HArray1[X]` passed as `Array1[float]`, `Base` assigned to `Full`) are reported by both checkers.
- **The stubs themselves are checked by a ratchet** (`test_stub_errors_do_not_grow`): mypy over every module of the installed stubs (copied out: mypy silences errors in an installed package), counted per error code against `STUB_ERROR_PINS` -- 761 errors (OCCT 8.0.1), all the C++ shape Python typing cannot express (673 `[override]` from C++ name hiding, operator pairs, overloads Python cannot tell apart, the quoted names of template instantiations). Every other code must stay at zero, and the pinned ones must not grow: real bugs show up exactly that way (`[assignment]` for R-PTR-NULL, `[name-defined]` for the unqualified enum defaults, a growing `[overload-cannot-match]` for base-before-derived). Exact on macOS, where the pins were measured, so a drop has to lower its pin; upper bounds elsewhere, since the stubs differ per platform. About 4 s.
- Known imprecision: a *returned* null handle is typed as the class, not `X | None` (same as nanobind's own handle stubs); handle *parameters* are `X | None` since `.none()` is emitted.
- Returned stream text is `str` (`nanocct_stream_text` returns `nb::str`; an `nb::object` would type every `DumpJson()`/`Print()`/`Write()` result as `object` in the stubs).
- The generic nested `Iterator` classes use their own type variables (`_IT`, `_IK`, `_IV`): a nested class cannot reuse the outer class's `_T` (mypy then treats it as non-generic and `Value()` is `Never`), and every concrete instantiation gets a concrete `class Iterator(NCollection_List.Iterator[int]): ...`, so `NCollection_List__int.Iterator(l).Value()` is `int` and `for x in it` types `x` (`tests/typing/check_iterators.py`). The generic-spelling rewrite leaves a concrete name alone when a nested-class access follows (`class Iterator(nanocct.NCollection.NCollection_Sequence__Handle_Graphic3d_ClipPlane.Iterator)`), the ty divergence above.
- **The five marker keys are aliases** (`float32 = float`, `uchar = int`, `uint = int`, `ulong = int`, `ulonglong = int`) in the `NCollection/__init__.pyi` header, and `generator/stubs.py` spells the five C++ scalars with them (`nanocct.NCollection.float32` …), so the instantiations over them collapse into their generic base like every other one and OCCT's signatures that use them get the generic spelling (`Poly_Triangulation.SetNormals(theNormals: NCollection_HArray1[float32] | None)`). Variants that keep precision apart statically (numpy scalar types, distinct marker classes, `float` subclasses with self-type overloads for the 55 write members) were tested and not taken.
- **The hasher is an optional last type parameter** of the four hashed kinds whose instantiations use a custom one (`NCollection_Map`, `IndexedMap`, `DataMap`, `IndexedDataMap`): `_H = TypeVar('_H', default=object)` (PEP 696, from `typing_extensions`, since `typing.TypeVar` takes `default` only from Python 3.13), and `_IH` for their nested `Iterator`. So `NCollection_Map[TopoDS_Shape, TopTools_ShapeMapHasher]` type-checks as it runs, and `NCollection_Map[int]` is the default hasher. The two are different types, as they are different bound classes. Without it the generic classes would have no parameter for the hasher while the concrete bases and OCCT's signatures pass it — 234 wrong-arity errors when mypy checks the stubs (measured, mypy 2.3.1). `DoubleMap` keeps its two keys only: both bound instantiations use the default hashers.

## 7c. Aliases of OCCT class templates (instantiated from the header)

### What they are

- OCCT 8 turned several classic classes into class templates with aliases: `using math_Vector = math_VectorBase<double>;`, `math_IntegerVector`, `Bnd_B2d/B3d/B2f/B3f`, `BVH_Vec3d = BVH::VectorType<double, 3>::Type` (→ `NCollection_Vec3<double>`), `BVH_Builder3d`, `TColStd_PackedMapOfInteger = NCollection_PackedMap<int>`, `NCollection_String`, later `Extrema_ExtPC = Extrema_GGExtPC<Adaptor3d_Curve, …>`, `GeomLProp_CLProps`.
- These are not containers, so 7a does not apply; they are the one place where the generic option (a) is used.

### Rule

- A package-level `typedef`/`using` whose canonical type is an instantiation of an OCCT class template (not an NCollection binder kind, not `handle`, not `std::`) — or an **un-aliased instantiation used as a base class** (`BRepGraph_WiresOfEdge : EdgeParentsOf<…>`, `Poly_ArrayOfNodes : NCollection_AliasedArray<>`, bound under the mangled name) — is bound as a normal class **under the alias name** (`nanocct.math.math_Vector`, C++ type `math_VectorBase<double>`).
- The template's definition is walked with the ordinary class walker while a substitution map rewrites every type spelling and default argument:
    - template parameters → arguments (position-wise, using the parameter names of *every* declaration of the template, because a forward declaration may name them differently and libclang spells some dependent types with those names);
    - the injected class name → the full instantiation (`math_VectorBase` → `math_VectorBase<double>`).
- Arguments come from the canonical type when the alias goes through a metafunction (`BVH::VectorType<…>::Type`); non-type arguments (`BVH_Builder<double, 3>`) are taken as written.
- Members whose types stay dependent (libclang's `type-parameter-0-0`, e.g. `T* begin()`) are skipped and reported.
- A default `T(0)` whose argument is a multi-word builtin (`NCollection_Vec3<unsigned long>` in `Image_PixMapData`) is spelled as a C-style cast, `(unsigned long)(0)` — `unsigned long(0)` is not C++. `NCollection_Vec3<unsigned long>::cwiseAbs` is in `overrides.toml [skip] methods` (`std::abs(unsigned long)` is ambiguous).
- An instantiation with a **raw pointer as template argument** (`HLRBRep_SLProps = GeomLProp_SLPropsBase<void*, …>`, `HLRBRep_CLProps` over `const HLRBRep_Curve*`, the `Extrema_G*<void*, HLRBRep_CurveTool, …>` locators) is not bound and reported: every member takes or returns the pointer (R-UNSUPPORTED), and `const T&` with `T` a pointer is `T* const&`, not what the substitution spells.
- A member whose *body* does not compile for the argument (`IntPolyh_Array<IntPolyh_Edge>::Dump()` calls `(*this)[i].Dump()`, but `IntPolyh_Edge::Dump` takes an `int` and `IntPolyh_PointNormal` has none) cannot be seen from the signature: it is listed in `overrides.toml [skip] methods` with the instantiation name (three entries, found as compile errors).
- Instantiations have no library symbols, so the `nm` check does not apply to them.
- The same instantiation aliased in several packages is bound once (manifest key = canonical spelling) and aliased elsewhere; the same alias repeated in several headers of one package is bound once.
- Docstrings come from the template. Stubs: stubgen emits a full concrete class for the alias (no generic class, unlike 7a).
- Verified: `math_Vector` constructors (incl. from `gp_XYZ`), operators, `math_Matrix.Row()` returning `math_Vector`, `BVH_Vec3d`, `Bnd_B3d`, `TColStd_PackedMapOfInteger`.
- **Names spell every template argument**, unlike 7a, which drops a default hasher: `NCollection_Map<int>` is `NCollection.NCollection_Map__int`, but the OCCT 8 flat maps -- not among the 15 binder kinds, so instantiated here -- are `BRepGraph.NCollection_FlatMap__BRepGraph_UID__NCollection_DefaultHasher__BRepGraph_UID` (five such classes, all in BRepGraph/BRepGraphInc, homed in the package that uses them, no `NCollection_FlatMap[...]` accessor), and `NCollection_AliasedArray<>` (every argument defaulted) is `Poly.NCollection_AliasedArray__`. The names are public (released with 8.0.1.0), so they stay; `tests/test_BRepGraph.py` pins them, so an OCCT change to a default argument cannot rename them unnoticed.

### On-demand instantiation

- Besides aliases and base classes, every instantiation of an OCCT class template that appears in a bound signature, field or typedef (`BRepGraph_MutGuard<BRepGraphInc::EdgeDef>` returned by `EditorView::EdgeOps::Mut`) is instantiated under its mangled name unless an earlier package or run bound it (manifest); its own template arguments are registered too.
    - The type is stripped of references, pointers and cv-qualifiers first: tested on the *declared* type, whose canonical kind is `LVALUEREFERENCE` for a `const T&` parameter, an instantiation reachable **only** through a reference parameter (`RWPly_PlyWriterContext::WriteVertex(…, const NCollection_Vec4<uint8_t>&)`) would never be instantiated, and the method would be bound with a type nanobind never sees — a `TypeError` for every argument list, unreported, because the parameter itself is bindable.
- **Template bases of instantiations:** a base spelled only after substitution is instantiated through a probe re-parse, or dropped from the derived class's bases when it cannot be (R-TEMPLATE-BASE, 7.6).
- A private member typedef used in a public signature (`BRepGraph_MutGuard::TypeId`) is spelled by its underlying type.
- **Instantiations named by the members of an instantiation:** inside a walk a member's type is dependent (`NCollection_Vec4<Element_t>::xyz()` returns `NCollection_Vec3<Element_t>`), libclang gives it no declaration, and without a record the member would be bound with an unregistered type (`Vec4__unsigned_char().xyz()` would raise `TypeError`). `parse._note_dependent_use` records the substituted spelling (`NCollection_Vec3<unsigned char>`) and the R-TEMPLATE-BASE probe instantiates it. Not recorded: binder kinds (7a), `handle`, `std::`, the walked instantiation itself spelled with its arguments (`NCollection_AliasedArray<MyAlignSize>` inside `NCollection_AliasedArray<>` would be bound twice under the keys `<>` and `<16>`, and the module would fail to initialise: nanobind's "already registered"), and the uses of a member that ends up skipped (the `begin()`/`end()` range iterators would add classes of their own).

- **Partial specialisations:** an instantiation that comes from a partial specialisation is walked from that specialisation, not from the primary template -- `BVH_Tree<T, N, Arity>` is empty and `BVH_Tree<T, N, BVH_BinaryTree> : public BVH_TreeBase<T, N>` (`BVH_BinaryTree.hxx`) is the real class, so the four `BVH_Tree` instantiations would otherwise be bound without a member or a base. libclang reports the primary template even for such an instantiation (`clang_getSpecializedCursorTemplate`), so `parse._matching_specialisation` matches the specialisations declared in the translation unit against the arguments: a pattern argument must be a bare parameter of the specialisation (it is bound to the argument, the substitution uses the specialisation's own parameter names) or equal the argument literally; a pattern like `T*` or `X<T>`, or more than one match, is not walked (reported). An explicit (full) specialisation is a class of its own, bound from its declaration like any class, and is not instantiated from the template. Measured once over all 297 7c instantiations (OCCT 8.0.1): exactly the four `BVH_Tree` ones match (`NCollection_DefaultHasher` has specialisations, no 7c use of it matches); the base `BVH_TreeBase<T, N>` comes in through R-TEMPLATE-BASE (`<double, 2>`, `<double, 3>`, `<float, 3>`) with `Length`, `Depth`, `MinPoint`/`MaxPoint`, the node buffers.
- **Nested classes of an instantiation:** walked with the instantiation's substitution still active and bound into it like any nested class (`NCollection_FlatMap<K, H>::Iterator` → `<outer>.Iterator`, `NCollection_UBTree<int, Bnd_Box>::TreeNode`/`Selector`, `NCollection_UBTreeFiller<…>::ObjBnd`, `TColStd_PackedMapOfInteger.Iterator`, `BOPTools_BoxPairSelector.PairIDs`); skipped, they would also drop `UBTree<int, Bnd_Box>::Selector` as the base of `BRepClass3d_BndBoxTreeSelectorPoint`/`Line` and `BRepBuilderAPI_BndBoxTreeSelector`. The outer class gets its final name and Python path only after the walk (the alias, for `TColStd_PackedMapOfInteger`), so `parse._reparent_nested` points the nested classes at it; an alias instantiation is added with its nested classes (`add_class`). An STL-style iterator is not instantiated at all (R-ITERATOR), so neither is its helper `NCollection_ForwardRangeIterator::PostfixProxy`.

### Nested templates and dependent names (BRepGraph)

- The template may be nested in a class or namespace (`BRepGraph_NodeId::Typed<Kind::Face>` = `BRepGraph_FaceId`, `BRepGraph_RefsIterator::RefIterator<…>`): the definition is found by descending every reopening of the enclosing scopes, and the injected class name maps to the full instantiation when written bare, to the qualified template name when written with arguments (`Typed<TheKind>`).
- Names the template writes unqualified are qualified during the walk: its own member types (`using TypedId = …; TypedId CurrentId()` → `BRepGraph_Iterator<…>::TypedId`, valid C++ once the instantiation is concrete) and types/templates of the enclosing scopes (`DefTraits<IdType>` → `BRepGraph_ReverseIterator::DefTraits<…>`). A qualified spelling of another template with the same leaf name (`BRepGraph_RefId::Typed`) is left alone.
- Defaulted template arguments come from the parameter's default (`bool IsFull = false`); one libclang cannot spell at all (`NCollection_AliasedArray<>`) stays out of the name but is substituted.
- libclang exposes no members on an instantiated specialisation cursor (verified: zero children), so walking the definition is the only route.
- Dependent results: `T&` written as such becomes a mutable reference (`reference_internal`, class element types only); a pointer, or a typedef hiding one (`LinearVector<T>::iterator`), is skipped — nanobind would take ownership of an element — except `const char*` (`NCollection_String::ToCString`).
- Partial `std::hash<Tmpl<K>>` specialisations give `__hash__` to every instantiation; `template <> struct std::hash<X>` written at file scope (semantic parent `std::__1`) is recognised like the `namespace std {}` form.
