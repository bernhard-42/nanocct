"""Generator unit tests: the IR that parse_package builds from synthetic headers (one per Design.md 6 rule), the
overload-collision resolver, the report categories, and the reproducibility of a regeneration against the checked-in
sources. No compiler is involved except the regeneration test's libclang parse (TKG2d, ~5 s)."""
import filecmp
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from generator import parse
from generator.binders import BINDERS
from generator.emit import Emitter, resolve_overload_collisions
from generator.model import ConversionKind, Method, Param, ResultKind, StreamKind
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
    assert names == ["Rules_Thing", "Rules_Value", "Rules_Value::Nested"]
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
    assert categorize(ir.report[-1]) == "override"
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


def test_emitter_static_rename_and_collision(rules_ir):
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert '.def_static("Length_s"' in cpp and '.def("Length"' in cpp
    assert 'nb::arg("theIn").none()' in cpp and 'occ::handle<Rules_Thing> theOut{};' in cpp
    assert '.def("SetValue"' in cpp                         # Python addition for double& Value(i)
    assert "    .export_values();" in cpp                   # Mode exported into the class, Kind not
    assert cpp.count(".export_values()") == 1
    assert any("Parameter(const gp_Pnt &, double &): same Python signature as Parameter(const gp_Pnt &)" in r for r in em.report)
    assert any("Rules_Value::Length: static overloads renamed to Length_s" in r for r in em.report)


def test_resolve_overload_collisions_prefers_scalar_result():
    def m(name, params, scalar, result="void"):
        return Method(name=name, params=params, result=result, result_kind=ResultKind.VALUE, result_class="", is_static=False,
                      is_const=True, is_noexcept=False, doc="", result_scalar=scalar)
    p = Param(name="v", type="const gp_Pnt &", default=None, is_out=False)
    out = Param(name="u", type="double &", default=None, is_out=True)
    direct = m("Parameter", [p], True, "double")
    with_out = m("Parameter", [p, out], True, "bool")
    ordered, unreachable = resolve_overload_collisions([with_out, direct])
    assert ordered == [direct, with_out] and unreachable == [(with_out, direct)]
    # void results: the overload with the most out-params wins
    a = m("Coord", [], False, "gp_XYZ"); a.result_scalar = False
    b = m("Coord", [out, Param(name="w", type="double &", default=None, is_out=True)], False)
    ordered, unreachable = resolve_overload_collisions([a, b])
    assert ordered == [b, a] and unreachable == [(a, b)]
    # a deprecated overload loses even when the rule would prefer it
    dep = m("Knots", [Param(name="k", type="occ::handle<NCollection_HArray1<double>> &", default=None, is_out=True, is_handle=True)], False)
    dep.is_deprecated = True
    keep = m("Knots", [], False, "const occ::handle<NCollection_HArray1<double>> &")
    ordered, unreachable = resolve_overload_collisions([dep, keep])
    assert ordered == [keep, dep] and unreachable == [(dep, keep)]
    # distinct Python signatures: untouched, header order
    ordered, unreachable = resolve_overload_collisions([m("X", [p], True), m("X", [], True)])
    assert [len(x.params) for x in ordered] == [1, 0] and unreachable == []


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
