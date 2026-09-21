"""Generator unit tests: the IR that parse_package builds from synthetic headers (one per Design.md 6 rule), the
overload-collision resolver, the report categories, and the reproducibility of a regeneration against the checked-in
sources. No compiler is involved except the regeneration test's libclang parse (TKG2d, ~5 s)."""
import filecmp
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from generator import parse
from generator.binders import BINDERS
from generator.emit import Emitter, resolve_ctor_arities, resolve_overload_collisions
from generator.model import Constructor, ConversionKind, Method, Param, ResultKind, StreamKind
from generator.occt import OcctTree, Package, load_tree
from generator.report import CATEGORIES, categorize

ROOT = Path(__file__).parents[1]
OCCT_SRC = ROOT / "deps" / "occt-src"
OCCT = ROOT / "deps" / "occt-8.0.1"

pytestmark = pytest.mark.skipif(not (OCCT / "include" / "opencascade" / "Standard_Transient.hxx").exists(),
                                reason="local OCCT build (deps/occt-8.0.1) not present")

HEADER = """
#include <Standard_Transient.hxx>
#include <Standard_Handle.hxx>
#include <Standard_Macro.hxx>
#include <Standard_OStream.hxx>
#include <gp_Pnt.hxx>
#include <gp_XYZ.hxx>
#include <NCollection_Array1.hxx>
#include <NCollection_DynamicArray.hxx>
#include <NCollection_List.hxx>
#include <gp_Trsf.hxx>

//! A Transient class for the handle rules.
class Rules_Thing : public Standard_Transient
{
public:
  Rules_Thing() {}
  DEFINE_STANDARD_RTTI_INLINE(Rules_Thing, Standard_Transient)
};

//! A value class exercising one Design.md section 6 rule per member.
class Rules_Value
{
public:
  Rules_Value() {}
  //! A non-explicit converting constructor: implicit conversion from gp_Pnt.
  Rules_Value(const gp_Pnt& thePnt) { (void)thePnt; }

  //! Pure out-parameters -> returned as a tuple.
  void Coord(double& theX, double& theY) const { theX = 1.0; theY = 2.0; }
  //! In/out parameter (listed in overrides [inout] by the test).
  void Transforms(double& theX) const { theX += 1.0; }
  //! Non-const reference to a class: mutated in place, stays a parameter.
  void Fill(gp_XYZ& theXYZ) const { theXYZ.SetX(1.0); }
  //! handle<T> parameter: accepts None; handle<T>& is an out-parameter.
  void Handles(const occ::handle<Rules_Thing>& theIn, occ::handle<Rules_Thing>& theOut) const { theOut = theIn; }
  //! std::ostream& -> the text comes back as a str.
  void Dump(Standard_OStream& theStream) const { theStream << "x"; }
  //! Mutable reference to a primitive -> getter + SetValue Python addition.
  double& Value(int theIndex) { (void)theIndex; return myValue; }
  //! Static and instance method with the same name -> Static_s.
  static double Length(const gp_Pnt& theP) { return theP.X(); }
  double Length() const { return myValue; }
  //! Overloads that collide after out-param removal: the scalar one wins.
  double Parameter(const gp_Pnt& theP) const { return theP.X(); }
  bool Parameter(const gp_Pnt& theP, double& theU) const { theU = theP.X(); return true; }
  //! Deprecated member: bound, the message becomes the docstring's first line.
  Standard_DEPRECATED("use Length() instead")
  double OldLength() const { return myValue; }
  //! Conversion operator to a bound class.
  operator gp_Pnt() const { return gp_Pnt(); }
  //! A container in the signature registers the instantiation.
  int Count(const NCollection_Array1<gp_Pnt>& thePoles) const { return thePoles.Length(); }
  //! NCollection_TListIterator<T> is NCollection_List<T>::Iterator: registers the List instantiation, no 6c class (TopOpeBRepDS).
  NCollection_TListIterator<gp_Pnt> Iter(const NCollection_List<gp_Pnt>& theList) const { return NCollection_TListIterator<gp_Pnt>(theList); }
  //! const / non-const twins: only the non-const one is bound (R-CONST-TWIN).
  const gp_XYZ& Origin() const { return myOrigin; }
  gp_XYZ& Origin() { return myOrigin; }
  //! Scalar width twins: double before float, int before size_t (R-WIDTH).
  float Scale(const float theS) const { return theS; }
  double Scale(const double theS) const { return theS; }
  int Width(const size_t theN) const { return static_cast<int>(theN); }
  int Width(const int theN) const { return theN; }

  //! A public nested class.
  struct Nested
  {
    double Val = 0.0;
  };
  Nested Get() const { return Nested(); }

  //! A nested unscoped enum (exported into the class) and a scoped one (stays nested).
  enum Mode { Mode_A, Mode_B };
  enum class Kind { K1, K2 };

private:
  double myValue = 0.0;
  gp_XYZ myOrigin;
};

//! Constructors whose one-argument call is ambiguous in C++ (IntPolyh_Array<T>): the first is bound with no argument.
class Rules_Ambiguous
{
public:
  Rules_Ambiguous(const int theIncrement = 256) { (void)theIncrement; }
  Rules_Ambiguous(const int theN, const int theIncrement = 256) { (void)theN; (void)theIncrement; }
};

//! A class whose base no binding knows (the test's Emitter does not know gp_Trsf), and a class deriving from it.
//! Its nested enum goes with it: no alias, instantiation or manifest entry may name it (BRepExtrema_ProximityDistTool::ProxPnt_Status).
class Rules_Unbound : public gp_Trsf
{
public:
  enum Status { Status_A, Status_B };
};
class Rules_Orphan : public Rules_Unbound {};
typedef Rules_Unbound::Status Rules_Status;
//! A signature naming the skipped class's enum through a container.
inline int Rules_CountStatus(const NCollection_DynamicArray<Rules_Unbound::Status>& theS) { return theS.Length(); }

//! A protected base whose members are re-exported with using-declarations (BRepAlgoAPI_Algo : protected BOPAlgo_Options).
class Rules_Options
{
public:
  void SetFuzzy(const double theV) { myFuzzy = theV; }
  double Fuzzy() const { return myFuzzy; }
  bool Flag() const { return true; }
  bool Flag(const int theI) const { return theI > 0; }
  void Dump(Standard_OStream& theS) const { theS << "opts"; }

private:
  double myFuzzy = 0.0;
};

//! R-USING: the base is inaccessible from outside, the using-declarations make the listed members public again.
class Rules_Algo : protected Rules_Options
{
public:
  Rules_Algo() {}
  using Rules_Options::SetFuzzy;
  using Rules_Options::Fuzzy;
  using Rules_Options::Flag;
  using Rules_Options::Dump;
};

//! R-USING: inherited constructors (using Base::Base) -- every base constructor except copy/move becomes one of the derived class.
class Rules_Inherit : public Rules_Value
{
public:
  using Rules_Value::Rules_Value;
};

//! More()/Next()/Value(): its own Python iterator (R-ITER).
class Rules_Iter
{
public:
  Rules_Iter() {}
  bool More() const { return myI < 3; }
  void Next() { ++myI; }
  const gp_Pnt& Value() const { return myP; }

private:
  int myI = 0;
  gp_Pnt myP;
};

//! A namespace named like the package is the package module itself.
namespace Rules
{
  //! A free function with an out-parameter.
  inline int Helper(int theA, int& theB) { theB = theA; return theA + 1; }
  constexpr double THE_CONST = 1.5;
}

//! Another namespace becomes a submodule.
namespace RulesNs
{
  inline int Twice(int theA) { return 2 * theA; }
}
"""


def _parse_rules(tmp: Path) -> parse.PackageIR:
    """parse_package on a synthetic package 'Rules' (one header) placed in a private include directory."""
    parse.configure_libclang()
    real = load_tree(OCCT_SRC, OCCT)
    inc = tmp / "include" / "opencascade"
    inc.mkdir(parents=True)
    (inc / "Rules.hxx").write_text(HEADER)
    fake = OcctTree(src=real.src, install=inc.parents[1])
    args = parse.clang_args(real) + [f"-I{inc}"]
    pkg = Package(name="Rules", toolkit="TKRules", module="Test", headers=["Rules.hxx"])
    return parse.parse_package(fake, pkg, args=args)


@pytest.fixture(scope="module")
def rules_ir(tmp_path_factory) -> parse.PackageIR:
    return _parse_rules(tmp_path_factory.mktemp("occt"))


def _method(ir: parse.PackageIR, cls: str, name: str, nparams: int | None = None) -> Method:
    c = next(c for c in ir.classes if c.name == cls)
    hits = [m for m in c.methods if m.name == name and (nparams is None or len(m.params) == nparams)]
    assert len(hits) == 1, [(m.name, len(m.params)) for m in c.methods if m.name == name]
    return hits[0]


def test_ir_classes_and_nesting(rules_ir):
    names = [c.name for c in rules_ir.classes]
    assert names == ["Rules_Thing", "Rules_Value", "Rules_Value::Nested", "Rules_Ambiguous", "Rules_Unbound", "Rules_Orphan", "Rules_Options",
                     "Rules_Algo", "Rules_Inherit", "Rules_Iter"]
    thing = rules_ir.classes[0]
    assert thing.is_transient is True and thing.bases == ["Standard_Transient"]
    nested = rules_ir.classes[2]
    assert nested.py_name == "Nested" and nested.outer == "Rules_Value" and nested.scope == ("Rules_Value",)
    assert [f.name for f in nested.fields] == ["Val"]


def test_ir_out_parameters(rules_ir):
    coord = _method(rules_ir, "Rules_Value", "Coord")
    assert [(p.name, p.is_out, p.is_inout) for p in coord.params] == [("theX", True, False), ("theY", True, False)]
    fill = _method(rules_ir, "Rules_Value", "Fill")
    assert fill.params[0].is_out is False and fill.params[0].class_name == "gp_XYZ"     # class reference: in place
    handles = _method(rules_ir, "Rules_Value", "Handles")
    assert [(p.is_handle, p.is_out) for p in handles.params] == [(True, False), (True, True)]
    assert handles.params[0].class_name == "Rules_Thing"


def test_ir_inout_from_override(monkeypatch, tmp_path_factory):
    monkeypatch.setattr(parse, "_INOUT", {"Rules_Value::Transforms"})
    ir = _parse_rules(tmp_path_factory.mktemp("occt2"))
    tr = _method(ir, "Rules_Value", "Transforms")
    assert (tr.params[0].is_out, tr.params[0].is_inout) == (True, True)


def test_header_allowlist_override(monkeypatch, tmp_path_factory):
    # overrides.toml [include] headers: a partial package (the font slice) binds only the listed headers
    monkeypatch.setattr(parse, "_INCLUDE_HEADERS", {"Rules": ["Rules.hxx"]})
    tmp = tmp_path_factory.mktemp("occt3")
    inc = tmp / "include" / "opencascade"
    inc.mkdir(parents=True)
    (inc / "Rules_Other.hxx").write_text("class Rules_Other { public: int X() const { return 1; } };\n")
    parse.configure_libclang()
    real = load_tree(OCCT_SRC, OCCT)
    (inc / "Rules.hxx").write_text(HEADER)
    pkg = Package(name="Rules", toolkit="TKRules", module="Test", headers=["Rules.hxx", "Rules_Other.hxx"])
    ir = parse.parse_package(OcctTree(src=real.src, install=inc.parents[1]), pkg, args=parse.clang_args(real) + [f"-I{inc}"])
    assert ir.headers == ["Rules.hxx"] and "Rules_Other" not in [c.name for c in ir.classes]
    assert "Rules_Other.hxx: not in the allowlist (overrides.toml [include] headers)" in ir.report
    assert categorize("Rules_Other.hxx: not in the allowlist (overrides.toml [include] headers)") == "override"
    with pytest.raises(ValueError):                  # a name that is not a header of the package
        monkeypatch.setattr(parse, "_INCLUDE_HEADERS", {"Rules": ["Nope.hxx"]})
        parse.parse_package(OcctTree(src=real.src, install=inc.parents[1]), pkg, args=parse.clang_args(real) + [f"-I{inc}"])


def test_ir_streams_and_mutable_primitive_reference(rules_ir):
    dump = _method(rules_ir, "Rules_Value", "Dump")
    assert dump.params[0].stream == StreamKind.OUT and dump.skip_reason is None
    value = _method(rules_ir, "Rules_Value", "Value")
    assert value.result_kind == ResultKind.REF_PRIMITIVE and value.result == "double"


def test_ir_deprecated_member_is_bound_with_note(rules_ir):
    old = _method(rules_ir, "Rules_Value", "OldLength")
    assert old.skip_reason is None
    assert old.doc.splitlines()[0] == "Deprecated in OCCT: use Length() instead"
    assert old.doc.splitlines()[-1] == "Deprecated member: bound, the message becomes the docstring's first line."


def test_ir_conversion_operator_and_implicit_ctor(rules_ir):
    value = next(c for c in rules_ir.classes if c.name == "Rules_Value")
    assert [(k.kind, k.target, k.is_explicit) for k in value.conversions] == [(ConversionKind.CLASS, "gp_Pnt", False)]
    implicit = [k for k in value.ctors if k.is_implicit]
    assert len(implicit) == 1 and implicit[0].params[0].type == "const gp_Pnt &"


def test_ir_enums(rules_ir):
    value = next(c for c in rules_ir.classes if c.name == "Rules_Value")
    kinds = {e.py_name: e.is_scoped for e in value.enums}
    assert kinds == {"Mode": False, "Kind": True}


def test_ir_namespaces_functions_constants(rules_ir):
    fns = {(f.scope, f.name): f for f in rules_ir.functions}
    helper = fns[((), "Helper")]                 # namespace Rules == package -> module level
    assert helper.qualified == "Rules::Helper" and [p.is_out for p in helper.params] == [False, True]
    assert ((("RulesNs",), "Twice") in fns) and rules_ir.namespaces == [("RulesNs",)]
    assert [(k.py_name, k.cpp) for k in rules_ir.constants] == [("THE_CONST", "Rules::THE_CONST")]


def test_ir_container_instantiation_registered(rules_ir):
    assert "NCollection_Array1<gp_Pnt>" in rules_ir.instances
    assert rules_ir.instances["NCollection_Array1<gp_Pnt>"].template in BINDERS
    # a nested template of a binder kind (NCollection_TListIterator<T> = NCollection_List<T>::Iterator) registers its owner
    assert "NCollection_List<gp_Pnt>" in rules_ir.instances
    assert not any(c.name.startswith("NCollection_TListIterator") for c in rules_ir.classes)
    assert _method(rules_ir, "Rules_Value", "Iter").skip_reason is None


def test_emitter_static_rename_and_collision(rules_ir):
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert '.def_static("Length_s"' in cpp and '.def("Length"' in cpp
    assert 'nb::arg("theIn").none()' in cpp and 'occ::handle<Rules_Thing> theOut{};' in cpp
    assert '.def("SetValue"' in cpp                         # Python addition for double& Value(i)
    assert "    .export_values();" in cpp                   # Mode exported into the class, Kind not
    assert cpp.count(".export_values()") == 1
    assert '.def("Parameter", static_cast<double (Rules_Value::*)(const gp_Pnt &) const' in cpp     # no out-params: plain name
    assert '.def("Parameter__float"' in cpp                                                       # R-COLLISION suffix
    assert any("Parameter(const gp_Pnt &, double &): same Python signature as another overload after out-param removal -> bound as Parameter__float" in r for r in em.report)
    assert [p.out_py for p in _method(rules_ir, "Rules_Value", "Coord").params] == ["float", "float"]
    # R-CONST-TWIN: the const Origin() is skipped, the non-const one (reference_internal) bound
    assert cpp.count('.def("Origin"') == 1 and 'gp_XYZ & (Rules_Value::*)() const' not in cpp
    assert "Rules_Value::Origin() const: const twin of a less const overload -> not bound" in em.report
    # R-WIDTH: the wider twin is registered first although the header declares it second
    assert cpp.index('(Rules_Value::*)(const double) const') < cpp.index('(Rules_Value::*)(const float) const')
    assert cpp.index('(Rules_Value::*)(const int) const>(&Rules_Value::Width)') < cpp.index('(Rules_Value::*)(const size_t) const>(&Rules_Value::Width)')
    assert "Rules_Value::Scale(const float): same Python signature as Scale(const double) -> registered after it (width preference)" in em.report
    # R-ITER: More/Next/Value -> __iter__/__next__ through nanoocp_def_iter; Rules_Value (no More) gets none
    assert cpp.count("nanoocp_def_iter<") == 1 and "nanoocp_def_iter<Rules_Iter>" in cpp
    assert "Rules_Iter: __iter__ added (More/Next/Value)" in em.report
    assert any("Rules_Value::Length: static overloads renamed to Length_s" in r for r in em.report)


def test_ir_records_mangled_names(rules_ir):
    # R-UNDEFINED compares libclang's mangling with nm's symbol list, per overload
    coord = _method(rules_ir, "Rules_Value", "Coord")
    assert coord.mangled.endswith("ZNK11Rules_Value5CoordERdS0_")
    ctors = next(c for c in rules_ir.classes if c.name == "Rules_Ambiguous").ctors
    assert [k.mangled.endswith(m) for k, m in zip(ctors, ["15Rules_AmbiguousC1Ei", "15Rules_AmbiguousC1Eii"])] == [True, True]


def test_emitter_ambiguous_constructor_and_skipped_base_chain(rules_ir):
    known = {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Unbound": "Rules", "Rules_Orphan": "Rules", "Rules_Value": "Rules"}
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", known, {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {},
                 ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    # R-CTOR-AMBIGUOUS: Rules_Ambiguous(5) is ambiguous in C++ -> nb::init<>() plus the two-argument form, no implicit conversion from int
    block = cpp[cpp.index('m.attr("Rules_Ambiguous"))'):]
    block = block[:block.index(";")]                       # the .def chain of Rules_Ambiguous
    assert ".def(nb::init<>()" in block and ".def(nb::init<const int, const int>()" in block and ".def(nb::init<const int>()" not in block
    assert "implicitly_convertible<std::decay_t<const int>, Rules_Ambiguous>" not in cpp
    assert any(r.startswith("Rules_Ambiguous::Rules_Ambiguous(const int): a call with all arguments is ambiguous") and r.endswith("bound with the first 0") for r in em.report)
    # a class whose base is skipped is skipped too, and both are handed back so the manifest forgets them
    assert "nb::class_<Rules_Unbound" not in cpp and "nb::class_<Rules_Orphan" not in cpp
    assert "Rules_Unbound: base class gp_Trsf is not bound (package not generated) -> class skipped" in em.report
    assert "Rules_Orphan: base class Rules_Unbound is not bound (skipped) -> class skipped" in em.report
    # the nested enum of a skipped class is skipped with it: no attribute alias to a non-existent attribute (which aborted
    # the import of TKTopAlgo), no accessor entry, no instantiation of a container over it -- and handed back for the manifest
    assert em.skipped == {"Rules_Unbound", "Rules_Orphan", "Rules_Unbound::Status"}
    assert 'attr("Rules_Status")' not in cpp and "bind_NCollection_DynamicArray<Rules_Unbound::Status>" not in cpp
    assert "Rules_Status = Rules_Unbound::Status: type alias of a type that is not bound (skipped)" in em.report
    assert ("NCollection_DynamicArray<Rules_Unbound::Status>: element type Rules_Unbound::Status is not bound (its class is skipped) "
            "-> instantiation skipped") in em.report
    assert em.templates["NCollection_DynamicArray<Rules_Unbound::Status>"]["skipped"] is True


def test_ir_and_emitter_using_declarations(rules_ir):
    # R-USING: `using Rules_Options::X;` in a public section of Rules_Algo (protected base) re-exports the base's overloads
    algo = next(c for c in rules_ir.classes if c.name == "Rules_Algo")
    assert algo.bases == [] and algo.constructible is False        # the non-public base is dropped (R-MI) and reported
    assert "Rules_Algo: non-public base Rules_Options dropped; class not constructible" in algo.skipped
    via = sorted((m.name, len(m.params), m.via_using) for m in algo.methods)
    assert via == [("Dump", 1, "Rules_Options"), ("Flag", 0, "Rules_Options"), ("Flag", 1, "Rules_Options"),
                   ("Fuzzy", 0, "Rules_Options"), ("SetFuzzy", 1, "Rules_Options")]
    assert all(m.defined_in_header for m in algo.methods)           # the symbol belongs to the base's library: no nm check here
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Value": "Rules"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    start = cpp.index('m.attr("Rules_Algo"))')
    block = cpp[start:cpp.index('m.attr("Rules_Iter"))', start)]          # the .def chain of Rules_Algo (lambda bodies contain ';')
    # bound through lambdas on the derived class (a member pointer of Rules_Options would need the inaccessible upcast)
    assert '.def("SetFuzzy", [](Rules_Algo &self, const double theV) { self.SetFuzzy(theV); }' in block
    assert '.def("Fuzzy", [](const Rules_Algo &self) { auto result = self.Fuzzy(); return result; }' in block
    assert block.count('.def("Flag"') == 2 and "&Rules_Options::" not in block
    assert '.def("Dump", [](const Rules_Algo &self) { std::ostringstream theS_stream; self.Dump(theS_stream); return nanoocp_stream_text(theS_stream); }' in block
    # inherited constructors: Rules_Value(const gp_Pnt&) becomes Rules_Inherit's; the default and copy constructors are not inherited
    # in C++ (the derived class gets its own implicit ones, R-IMPLICIT-DEFAULT/-COPY)
    inherit = next(c for c in rules_ir.classes if c.name == "Rules_Inherit")
    assert [[p.type for p in k.params] for k in inherit.ctors] == [["const gp_Pnt &"]] and not inherit.has_declared_ctor
    tail = cpp[cpp.index('m.attr("Rules_Inherit"))'):]
    assert "nanoocp_implicit_default_ctor<Rules_Inherit>" in cpp and '.def(nb::init<const gp_Pnt &>(), nb::arg("thePnt")' in tail


def test_resolve_ctor_arities():
    def k(*types_defaults):
        return Constructor(params=[Param(name=f"p{i}", type=t, default=d, is_out=False) for i, (t, d) in enumerate(types_defaults)], doc="")
    a = k(("const int", "256"))
    b = k(("const int", None), ("const int", "256"))
    assert resolve_ctor_arities([a, b]) == [(a, 0), (b, 2)]            # IntPolyh_Array<T>
    c = k()
    assert resolve_ctor_arities([c, a]) == [(a, 1)]                    # X() ambiguous with X(int = 256): a keeps its argument, c is out
    d = k(("const gp_Pnt &", None), ("const int", "1"))
    assert resolve_ctor_arities([a, b, d]) == [(a, 0), (b, 2), (d, 2)]  # different first type: no interaction
    skipped = k(("const int", None)); skipped.skip_reason = "x"
    assert resolve_ctor_arities([skipped, a]) == [(a, 1)]              # skipped overloads do not count


def test_resolve_overload_collisions_suffixes_by_out_params():
    def m(name, params, result="void"):
        return Method(name=name, params=params, result=result, result_kind=ResultKind.VALUE, result_class="", is_static=False,
                      is_const=True, is_noexcept=False, doc="")
    p = Param(name="v", type="const gp_Pnt &", default=None, is_out=False)
    out = Param(name="u", type="double &", default=None, is_out=True, out_py="float")
    out_i = Param(name="n", type="int &", default=None, is_out=True, out_py="int")
    direct = m("Parameter", [p], "double")
    with_out = m("Parameter", [p, out], "bool")
    assert resolve_overload_collisions([with_out, direct]) == [(with_out, "__float"), (direct, "")]     # header order kept
    # both with out-params: both suffixed, no plain name
    a = m("Parameters", [out, out, out]); b = m("Parameters", [out, out, out, out])
    assert resolve_overload_collisions([a, b]) == [(a, "__float__float__float"), (b, "__float__float__float__float")]
    # handle out-parameter: the class name; enum: its name; stream: str
    h = Param(name="C", type="occ::handle<Geom_Curve> &", default=None, is_out=True, is_handle=True, out_py="Geom_Curve")
    st = Param(name="os", type="Standard_OStream &", default=None, is_out=False, stream=StreamKind.OUT)
    r1 = m("Read", [h]); r2 = m("Read", [Param(name="S", type="occ::handle<Geom_Surface> &", default=None, is_out=True, is_handle=True, out_py="Geom_Surface")])
    assert resolve_overload_collisions([r1, r2]) == [(r1, "__Geom_Curve"), (r2, "__Geom_Surface")]
    s0 = m("Show", []); s1 = m("Show", [st]); s2 = m("Show", [out, out_i])
    assert resolve_overload_collisions([s0, s1, s2]) == [(s0, ""), (s1, "__str"), (s2, "__float__int")]
    # an in/out parameter stays an input: no collision
    io_ = Param(name="x", type="double &", default=None, is_out=True, is_inout=True, out_py="float")
    assert [sfx for _, sfx in resolve_overload_collisions([m("T", [io_]), m("T", [])])] == ["", ""]
    # distinct Python signatures: untouched; skipped overloads ignored
    sk = m("X", [p]); sk.skip_reason = "x"
    assert [sfx for _, sfx in resolve_overload_collisions([m("X", [p]), m("X", []), sk])] == ["", ""]
    assert len(resolve_overload_collisions([sk])) == 0


def test_stub_duplicate_signatures_are_only_width_or_string_kinds():
    """Overloads with identical Python signatures in the checked-in stubs (nanobind takes the first registered) may only
    be scalar-width twins (R-WIDTH, wider first) or the str-accepting kinds of TCollection (const char* / char /
    AsciiString / char16_t*); const twins and out-param collisions must be gone (R-CONST-TWIN, R-COLLISION)."""
    sig_re = re.compile(r"^(\s*)def (\w+)\((.*?)\)(?: -> (.*?))?:(?: \.\.\.)?$")
    cls_re = re.compile(r"^(\s*)class (\w+)")
    dups: list[tuple[str, str, tuple]] = []
    for pyi in sorted((ROOT / "src" / "nanoocp").rglob("*.pyi")):
        scope: list[tuple[int, str]] = []
        seen: dict[tuple, int] = {}
        for line in pyi.read_text().splitlines():
            m = cls_re.match(line)
            if m is not None:
                indent = len(m.group(1))
                scope = [s for s in scope if s[0] < indent] + [(indent, m.group(2))]
                continue
            m = sig_re.match(line)
            if m is None:
                continue
            indent, name, args = len(m.group(1)), m.group(2), m.group(3)
            owner = ".".join(s[1] for s in scope if s[0] < indent)
            types = tuple(re.sub(r"\s*=.*$", "", a.split(":", 1)[1]).strip() if ":" in a else a.strip()
                          for a in re.split(r",\s*(?![^\[]*\])", args) if a.strip() != "")
            key = (owner, name, types)
            seen[key] = seen.get(key, 0) + 1
            if seen[key] == 2:
                dups.append((pyi.stem, owner, (name, types)))
    width_ok = {"Abs", "Min", "Max", "Convert_LinearRGB_To_sRGB", "Convert_sRGB_To_LinearRGB", "Value", "SetValue", "ReSize", "__init__"}
    unexpected = [d for d in dups if not (d[2][0] in width_ok and any(t in ("float", "int") for t in d[2][1]))
                  and not (d[0] in ("TCollection", "Standard", "Resource") and "str" in d[2][1])
                  and d[1] != "Standard_Mutex.Sentry"]        # Sentry(Standard_Mutex&) / Sentry(Standard_Mutex*): the same call
    assert unexpected == [], unexpected
    assert len(dups) < 60


def test_report_categories_are_complete_for_the_checked_in_reports():
    from generator.report import read_report
    seen = set()
    for report in sorted((ROOT / "src" / "cpp").glob("TK*/report.txt")):
        for cat, _, msg in read_report(report):
            assert cat == categorize(msg) and cat != "misc", msg
            seen.add(cat)
    assert seen <= {c for c, _ in CATEGORIES}
    assert categorize("Foo::bar(): some idiom nobody expected") == "misc"


def test_regeneration_of_TKG2d_reproduces_the_checked_in_sources(tmp_path):
    """The generator, run with the checked-in manifest, must reproduce src/cpp/TKG2d byte for byte (the reviewer's
    'clean regeneration is canonical' check, automated for the smallest toolkit)."""
    (tmp_path / "cpp").mkdir()
    shutil.copy(ROOT / "src" / "cpp" / "manifest.json", tmp_path / "cpp" / "manifest.json")
    subprocess.run([sys.executable, "-m", "generator", "--toolkit", "TKG2d", "--out", str(tmp_path)], check=True, cwd=ROOT,
                   capture_output=True, text=True)
    generated = tmp_path / "cpp" / "TKG2d"
    checked_in = ROOT / "src" / "cpp" / "TKG2d"
    cmp = filecmp.dircmp(generated, checked_in)
    assert cmp.left_only == [] and cmp.right_only == []
    assert cmp.diff_files == [], cmp.diff_files
    for shim in ("Geom2d.py", "Adaptor2d.py"):
        assert (tmp_path / "nanoocp" / shim).read_text() == (ROOT / "src" / "nanoocp" / shim).read_text()


def test_incremental_run_refuses_to_rehome_an_instantiation(tmp_path):
    """An incremental run that would bind an instantiation an earlier, not regenerated toolkit could own in a clean run
    fails loudly (Design.md 9); --allow-rehoming overrides. Simulated by dropping NCollection_Array1<gp_Pnt2d> (owned by
    TKMath/BSplCLib) from a copy of the manifest and regenerating TKG2d, which uses it."""
    import json
    (tmp_path / "cpp").mkdir()
    manifest = json.loads((ROOT / "src" / "cpp" / "manifest.json").read_text())
    assert manifest["templates"]["NCollection_Array1<gp_Pnt2d>"]["toolkit"] == "TKMath"
    del manifest["templates"]["NCollection_Array1<gp_Pnt2d>"]
    (tmp_path / "cpp" / "manifest.json").write_text(json.dumps(manifest))
    cmd = [sys.executable, "-m", "generator", "--toolkit", "TKG2d", "--out", str(tmp_path)]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert proc.returncode == 1
    assert "rehoming: NCollection_Array1<gp_Pnt2d> is newly bound by TKG2d/" in proc.stderr
    assert "TKMath" in proc.stderr.split("rehoming:")[1].splitlines()[0]     # TKMath (gp_Pnt2d's toolkit) is a candidate owner
    assert "TKernel" not in proc.stderr.split("rehoming:")[1].splitlines()[0]  # TKernel cannot own it: gp_Pnt2d is TKMath
    assert not (tmp_path / "cpp" / "TKG2d").exists()                          # nothing was written
    proc = subprocess.run(cmd + ["--allow-rehoming"], cwd=ROOT, capture_output=True, text=True)
    assert proc.returncode == 0 and "rehoming: NCollection_Array1<gp_Pnt2d>" in proc.stderr
    assert "NCollection_Array1<gp_Pnt2d>" in (tmp_path / "cpp" / "TKG2d" / "Geom2d.cpp").read_text()
