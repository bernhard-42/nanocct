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
from generator.emit import Emitter, resolve_ctor_arities, resolve_overload_collisions, resolve_static_renames
from generator.model import Class, Constructor, ConversionKind, Method, Param, ResultKind, StreamKind
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
#include <Standard_DefineAlloc.hxx>
#include <Standard_OStream.hxx>
#include <gp_Pnt.hxx>
#include <gp_XYZ.hxx>
#include <NCollection_Array1.hxx>
#include <NCollection_DynamicArray.hxx>
#include <NCollection_List.hxx>
#include <NCollection_Sequence.hxx>
#include <NCollection_DataMap.hxx>
#include <NCollection_DefineAlloc.hxx>
#include <utility>
#include <memory>
#include <gp_Trsf.hxx>
#include <bitset>
#include <mutex>

class Rules_Fwd;

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
  //! A chaining result (*this) next to an out-parameter is dropped: the lambda would copy self (BinObjMgt_Persistent::GetInteger).
  const Rules_Value& GetOne(int& theV) const { theV = 1; return *this; }
  //! In/out parameter (listed in overrides [inout] by the test).
  void Transforms(double& theX) const { theX += 1.0; }
  //! Non-const reference to a class: mutated in place, stays a parameter.
  void Fill(gp_XYZ& theXYZ) const { theXYZ.SetX(1.0); }
  //! handle<T> parameter: accepts None; handle<T>& is an out-parameter.
  void Handles(const occ::handle<Rules_Thing>& theIn, occ::handle<Rules_Thing>& theOut) const { theOut = theIn; }
  //! std::ostream& -> the text comes back as a str.
  void Dump(Standard_OStream& theStream) const { theStream << "x"; }
  //! An std type without a caster that is not a stream: reported by name (DE_Wrapper::GlobalLoadMutex).
  static std::mutex& LoadMutex() { static std::mutex aMutex; return aMutex; }
  //! A braced default (`= {}`): list-initialised, because static_cast from a braced-init-list is not C++.
  void Braced(const gp_XYZ& theXYZ = {}) const { (void)theXYZ; }
  //! std::bitset<N> is a set of flag indices in Python (R-BITSET); its size is a non-type template argument.
  void Flags(const std::bitset<4>& theFlags) const { (void)theFlags; }
  std::bitset<4> GetFlags() const { return std::bitset<4>(); }
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
  //! Const / non-const conversion twins (XmlObjMgt_Persistent::operator XmlObjMgt_Element&): one conversion.
  operator const gp_XYZ&() const { return myOrigin; }
  operator gp_XYZ&() { return myOrigin; }
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

  //! R-OPTIONAL-PTR: an optional output pointer with a null default is dropped (BRepFill_AdvancedEvolved::IsDone).
  bool Optional(const int theA, unsigned int* theErrorCode = NULL) const { if (theErrorCode) *theErrorCode = 0; return theA > 0; }
  //! R-FIXED-ARRAY: gp_Pnt theP[8] out (Bnd_OBB::GetVertex), const int (&)[3] in (BRepMesh_Triangle), a double[3] member.
  bool Corners(gp_Pnt theP[8]) const { theP[0] = gp_Pnt(1, 2, 3); return true; }
  int SumNodes(const int (&theNodes)[3]) const { return theNodes[0] + theNodes[1] + theNodes[2]; }
  double myPeriod[3] = {1.0, 2.0, 3.0};
  //! R-PTR-REF: a T*& result is returned as the pointer (BRepAlgoAPI_BuilderAlgo::Builder()).
  gp_Pnt*& PtrRef() { return myPtr; }
  //! R-PTR-INCOMPLETE: a pointer to a class only forward-declared here, whose header exists (BOPAlgo_Builder::PDS()).
  Rules_Fwd* Fwd() const { return nullptr; }
  //! A member template declared here and defined in Rules.lxx: reported once, as a template member.
  template <class T> T Half(const T theV) const;
  //! R-CSTR-NULL: a const char* with a null default stays in the signature as `str | None = None` (LDOM_XmlWriter, STEPCAFControl_Writer::Write).
  const char* Encoding(const char* const theEncoding = nullptr) const { return theEncoding == nullptr ? "none" : theEncoding; }

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
  gp_Pnt* myPtr = nullptr;
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

//! A protected base that *provides* operator new (DEFINE_STANDARD_ALLOC, as Message_ProgressScope does): the
//! allocation function is inherited inaccessibly, so `new Rules_LazyScope(...)` does not compile even in C++.
class Rules_AllocOptions
{
public:
  DEFINE_STANDARD_ALLOC
  int Level() const { return 1; }
};

//! Message_LazyProgressScope : protected Message_ProgressScope -- bound, but with no constructor.
class Rules_LazyScope : protected Rules_AllocOptions
{
public:
  Rules_LazyScope() {}
  using Rules_AllocOptions::Level;
};

//! R-USING: inherited constructors (using Base::Base) -- every base constructor except copy/move becomes one of the derived class.
class Rules_Inherit : public Rules_Value
{
public:
  using Rules_Value::Rules_Value;
};

//! An element type with a deleted copy constructor (CSLib_Class2d).
class Rules_NoCopy
{
public:
  Rules_NoCopy() {}
  Rules_NoCopy(const Rules_NoCopy&) = delete;
};

//! R-NONCOPYABLE detected: a container of such elements held by value (BRepTopAdaptor_FClass2d), and a class holding this one.
class Rules_Holder
{
public:
  Rules_Holder() {}
  NCollection_Sequence<Rules_NoCopy> mySeq;
};
class Rules_Holder2
{
public:
  Rules_Holder2() {}
  Rules_Holder myHolder;
};

//! Class-level operator new without the placement form (DEFINE_NCOLLECTION_ALLOC): fine while trivially copyable
//! (Poly_CoherentTriPtr) ...
class Rules_Alloc
{
public:
  DEFINE_NCOLLECTION_ALLOC
  int myA = 0;
};
//! ... but not with a base (BRepMeshData_Curve): nanobind's copy wrapper needs placement new.
class Rules_AllocDerived : public Rules_Value
{
public:
  DEFINE_NCOLLECTION_ALLOC
};

//! An array reference parameter (BRepMesh_Triangle::Initialize) and a std::pair& out-parameter (BRepMesh_ConeRangeSplitter).
class Rules_Arrays
{
public:
  Rules_Arrays() {}
  void Nodes(int (&theNodes)[3]) const { theNodes[0] = 1; }
  double Steps(const int theN, std::pair<int, int>& theSteps) const { theSteps = {theN, theN}; return 1.0; }
};

//! 6c: an instantiation reachable ONLY through a reference parameter must still be instantiated. `const T&` has
//! canonical kind LVALUEREFERENCE, so the plain-template check answered False for it and the method bound with a type
//! nanobind never saw -- RWPly_PlyWriterContext::WriteVertex(..., const NCollection_Vec4<uint8_t>&) was uncallable
//! (2026-09-23). Rules_TOnly<short> appears nowhere else: no typedef, no field, no by-value parameter.
template <class T>
class Rules_TOnly
{
public:
  Rules_TOnly(T theV = T(0)) : myV(theV) {}
  T Value() const { return myV; }

private:
  T myV;
};

//! R-OPTIONAL-PTR: a std::shared_ptr<T> parameter defaulted to its own empty form is dropped rather than skipping the
//! whole method; nullptr is exactly that default (RWPly_PlyWriterContext::Open, whose every other member needs the
//! stream it opens).
class Rules_Sink
{
public:
  Rules_Sink() {}
  bool Take(const Rules_TOnly<short>& theOnly) const { return theOnly.Value() > 0; }
  bool Open(const char* theName, const std::shared_ptr<std::ostream>& theStream = std::shared_ptr<std::ostream>()) const
  {
    return theName != nullptr && theStream == nullptr;
  }
};

//! R-TEMPLATE-BASE: a template base of an alias instantiation is spelled only after substitution and instantiated through a
//! probe typedef (BVH_PrimitiveSet<double, 3> : BVH_Object<double, 3>); a CRTP base with a template template parameter cannot
//! be instantiated (BVH_Box<double, 3> : BVH_BaseBox<double, 3, BVH_Box>) and is dropped.
template <class T>
class Rules_TBase
{
public:
  T BaseValue() const { return T(); }
};
template <class T>
class Rules_TDerived : public Rules_TBase<T>
{
public:
  T Value() const { return T(); }
};
typedef Rules_TDerived<double> Rules_TDouble;
template <class T, template <class> class TheDerived>
class Rules_CrtpBase
{
};
template <class T>
class Rules_Crtp : public Rules_CrtpBase<T, Rules_Crtp>
{
public:
  T X() const { return T(); }
};
typedef Rules_Crtp<int> Rules_CrtpInt;

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

//! Visualization-era idioms (TKService, 2026-09-22): bit-fields, hidden friends, alias enumerators, references to headerless types.
class Rules_NoHeader;
//! An unscoped enum whose "old aliases" repeat earlier values (Font_FontAspect): exported by name, Python's Enum hides aliases.
enum Rules_Aspect { Rules_Aspect_Regular = 0, Rules_Aspect_Bold, Rules_A_Regular = Rules_Aspect_Regular, Rules_A_Bold = Rules_Aspect_Bold };
class Rules_Vis
{
public:
  Rules_Vis() {}
  enum Filter { Filter_None = 0, Filter_All = 1 };
  //! A nested class whose constructor defaults to an enumerator of the enclosing class (Font_TextFormatter::Iterator).
  class Iterator
  {
  public:
    Iterator(const Rules_Vis& theOwner, Filter theFilter = Filter_None) { (void)theOwner; (void)theFilter; }
  };
  //! R-FIELD: bit-fields have no pointer-to-member (Graphic3d_CStructure).
  unsigned stick : 1;
  unsigned visible : 1;
  int myPlain = 0;
  //! R-PTR-INCOMPLETE for references: no Rules_NoHeader.hxx exists (const AVStream& in Media_CodecContext).
  bool Init(const Rules_NoHeader& theStream) const { (void)theStream; return true; }
  //! R-CHAR16 family: char32_t is a 1-character str (Font_FTFont::AdvanceX).
  float Advance(char32_t theUChar) const { return static_cast<float>(theUChar); }
  //! R-FREE-OP: a hidden friend operator (NCollection_Vec3) is bound as a dunder on the class operand.
  friend Rules_Vis operator+(const Rules_Vis& theLeft, const Rules_Vis& theRight) { (void)theRight; return theLeft; }
  //! R-COLLISION with R-WIDTH: out-parameter overloads differing only in width are one overload, no suffix (Graphic3d_Vertex::Coord).
  void Coord(double& theX, double& theY) const { theX = 1.0; theY = 2.0; }
  void Coord(float& theX, float& theY) const { theX = 1.0f; theY = 2.0f; }
};
//! A 6c instantiation whose default `T(0)` becomes a multi-word builtin (NCollection_Vec3<unsigned long>).
template <class T>
class Rules_TVec
{
public:
  Rules_TVec(T theX = T(0)) : myX(theX) {}
  T X() const { return myX; }
private:
  T myX;
};
typedef Rules_TVec<unsigned long> Rules_TVecUL;

//! 6a: a nested class deriving from a binder instantiation's nested Iterator (Graphic3d_SequenceOfHClipPlane::Iterator) is
//! declared after the templates phase, where the base exists.
class Rules_PntSeq
{
public:
  class Iterator : public NCollection_Sequence<gp_Pnt>::Iterator
  {
  public:
    Iterator() = default;
    Iterator(const Rules_PntSeq& theSeq) : NCollection_Sequence<gp_Pnt>::Iterator(theSeq.myItems) {}
  };
  Rules_PntSeq() {}
  void Append(const gp_Pnt& theP) { myItems.Append(theP); }

protected:
  NCollection_Sequence<gp_Pnt> myItems;
};

//! 6a: a class deriving from a binder instantiation itself (BinObjMgt_RRelocationTable : NCollection_DataMap<int,
//! handle<Standard_Transient>>): declared after the templates phase too, the base spelled as the manifest key.
class Rules_Table : public NCollection_DataMap<int, double>
{
public:
  int Tag() const { return myTag; }
  void SetTag(const int theTag) { myTag = theTag; }

private:
  int myTag = 0;
};

//! Transient through a template base (SelectMgr_RectangularFrustum : SelectMgr_Frustum<4> : ... : Standard_Transient,
//! BRepExtrema_TriangleSet : BVH_PrimitiveSet<double, 3>): both the instantiation and the derived class are Transient.
template <class T>
class Rules_TTransient : public Standard_Transient
{
public:
  Rules_TTransient() {}
  T Tag() const { return T(); }
};
class Rules_ViaTemplate : public Rules_TTransient<int>
{
public:
  Rules_ViaTemplate() {}
};
typedef Rules_TTransient<double> Rules_TTransientD;
//! ... also when the base is written through a typedef (BRepExtrema_TriangleSet : BVH_PrimitiveSet3d).
class Rules_ViaTypedef : public Rules_TTransientD
{
public:
  Rules_ViaTypedef() {}
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

#include <Rules.lxx>
"""

# The inline part OCCT keeps in X.lxx, included at the end of X.hxx: file-scope declarations there belong to the package
# (std::hash<TDF_Label>, TopLoc_Location's ShallowDump, math_Matrix's friend operator* definition); out-of-line member
# template definitions and explicit specialisations of member templates (BRepGraphInc_Storage::TypedStorePlanes<T>) do not.
LXX = """
namespace std
{
template <>
struct hash<Rules_Ambiguous>
{
  size_t operator()(const Rules_Ambiguous&) const noexcept { return 7; }
};
}
inline int Twice(const Rules_Ambiguous&) { return 2; }
template <class T> T Rules_Value::Half(const T theV) const { return theV / 2; }
"""


def _parse_rules(tmp: Path) -> parse.PackageIR:
    """parse_package on a synthetic package 'Rules' (one header) placed in a private include directory."""
    parse.configure_libclang()
    real = load_tree(OCCT_SRC, OCCT)
    inc = tmp / "include" / "opencascade"
    inc.mkdir(parents=True)
    (inc / "Rules.hxx").write_text(HEADER)
    (inc / "Rules.lxx").write_text(LXX)
    (inc / "Rules_Fwd.hxx").write_text("class Rules_Fwd { public: int A = 1; };\n")     # exists, not included by Rules.hxx (R-PTR-INCOMPLETE)
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
    assert names[:16] == ["Rules_Thing", "Rules_Value", "Rules_Value::Nested", "Rules_Ambiguous", "Rules_Unbound", "Rules_Orphan", "Rules_Options",
                          "Rules_Algo", "Rules_AllocOptions", "Rules_LazyScope", "Rules_Inherit", "Rules_NoCopy", "Rules_Holder", "Rules_Holder2",
                          "Rules_Alloc", "Rules_Arrays"]
    assert set(names[16:]) == {"Rules_TDerived<double>", "Rules_Crtp<int>", "Rules_TBase<double>", "Rules_Iter", "Rules_Vis", "Rules_Vis::Iterator",
                               "Rules_TVec<unsigned long>", "Rules_PntSeq", "Rules_PntSeq::Iterator", "Rules_Table", "Rules_ViaTemplate",
                               "Rules_TTransient<int>", "Rules_ViaTypedef", "Rules_TTransient<double>", "Rules_Sink",
                               "Rules_TOnly<short>"}   # alias instantiations, probe bases, the reference-only instantiation
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
    one = _method(rules_ir, "Rules_Value", "GetOne")
    assert one.result == "void" and [p.is_out for p in one.params] == [True]


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
    (inc / "Rules.lxx").write_text(LXX)
    (inc / "Rules_Fwd.hxx").write_text("class Rules_Fwd { public: int A = 1; };\n")     # exists, not included by Rules.hxx (R-PTR-INCOMPLETE)
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
    assert [(k.kind, k.target_class, k.is_explicit) for k in value.conversions] == [(ConversionKind.CLASS, "gp_Pnt", False),
                                                                                  (ConversionKind.CLASS, "gp_XYZ", False), (ConversionKind.CLASS, "gp_XYZ", False)]
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


def test_ir_lxx_declarations_belong_to_the_package(rules_ir):
    """Rules.lxx (included at the end of Rules.hxx) contributes its file-scope declarations under the header's name:
    std::hash<Rules_Ambiguous> makes the class hashable, the free Twice(Rules_Ambiguous) is a package function; the
    out-of-line definition of the member template Half is not reported as a free template."""
    assert "Rules_Ambiguous" in rules_ir.hashable
    twice = [f for f in rules_ir.functions if f.name == "Twice" and f.scope == ()]
    assert [(f.header, [p.type for p in f.params]) for f in twice] == [("Rules.hxx", ["const Rules_Ambiguous &"])]
    assert [line for line in rules_ir.report if line.startswith("Half:")] == []
    assert "Rules_Value::Half: template member" in rules_ir.report


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
    assert cpp.count(".export_values()") == 3            # Mode, Rules_Aspect, Rules_Vis::Filter
    assert '.def("Parameter", static_cast<double (Rules_Value::*)(const gp_Pnt &) const' in cpp     # no out-params: plain name
    assert '.def("Parameter__float"' in cpp                                                       # R-COLLISION suffix
    assert any("Parameter(const gp_Pnt &, double &): same Python signature as another overload after out-param removal -> bound as Parameter__float" in r for r in em.report)
    assert [p.out_py for p in _method(rules_ir, "Rules_Value", "Coord").params] == ["float", "float"]
    # R-CONST-TWIN: the const Origin() is skipped, the non-const one (reference_internal) bound
    assert cpp.count('.def("Origin"') == 1 and 'gp_XYZ & (Rules_Value::*)() const' not in cpp
    assert "Rules_Value::Origin() const: const twin of a less const overload -> not bound" in em.report
    # conversion operators: the const/non-const twins to gp_XYZ give one conversion (emission mutates the IR: first emitter only)
    assert cpp.count("nanoocp_conversion<Rules_Value, gp_XYZ>(") == 1 and cpp.count("nanoocp_conversion<Rules_Value, gp_Pnt>(") == 1
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
    known = {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Unbound": "Rules", "Rules_Orphan": "Rules", "Rules_Value": "Rules",
             "Rules_TBase<double>": "Rules", "Rules_TDerived<double>": "Rules", "Rules_Crtp<int>": "Rules", "Rules_TTransient<int>": "Rules",
             "Rules_TTransient<double>": "Rules"}
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
    # the non-public base is dropped (R-MI) and reported; Rules_Options declares no operator new, so the class is
    # still constructible -- only a base that provides one makes `new Derived` ill-formed (Rules_LazyScope below)
    assert algo.bases == [] and algo.constructible is True
    assert "Rules_Algo: non-public base Rules_Options dropped; its members are not bound" in algo.skipped
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
    assert '.def("Fuzzy", [](const Rules_Algo &self) { auto nanoocp_result = self.Fuzzy(); return nanoocp_result; }' in block
    assert block.count('.def("Flag"') == 2 and "&Rules_Options::" not in block
    assert '.def("Dump", [](const Rules_Algo &self) { std::ostringstream theS_stream; self.Dump(theS_stream); return nanoocp_stream_text(theS_stream); }' in block
    # inherited constructors: Rules_Value(const gp_Pnt&) becomes Rules_Inherit's; the default and copy constructors are not inherited
    # in C++ (the derived class gets its own implicit ones, R-IMPLICIT-DEFAULT/-COPY)
    inherit = next(c for c in rules_ir.classes if c.name == "Rules_Inherit")
    assert [[p.type for p in k.params] for k in inherit.ctors] == [["const gp_Pnt &"]] and not inherit.has_declared_ctor
    tail = cpp[cpp.index('m.attr("Rules_Inherit"))'):]
    assert "nanoocp_implicit_default_ctor<Rules_Inherit>" in cpp and '.def(nb::init<const gp_Pnt &>(), nb::arg("thePnt")' in tail


def test_ir_instantiation_reachable_only_through_a_reference_parameter(rules_ir):
    """6c: `const Rules_TOnly<short>&` has canonical kind LVALUEREFERENCE, so the plain-template check has to run on the
    stripped declaration type. Until 2026-09-23 it ran on the reference and answered False, and the method was bound
    with a type nanobind never saw -- RWPly_PlyWriterContext::WriteVertex was a TypeError for every argument list, and
    nothing reported it because the parameter itself is perfectly bindable."""
    assert any(c.name == "Rules_TOnly<short>" for c in rules_ir.classes)
    take = _method(rules_ir, "Rules_Sink", "Take")
    assert take.skip_reason is None and [p.type for p in take.params] == ["const Rules_TOnly<short> &"]


def test_ir_shared_ptr_parameter_with_its_own_empty_default_is_dropped(rules_ir):
    """R-OPTIONAL-PTR: std::shared_ptr<std::ostream> has no caster, but a parameter defaulted to its own empty form
    needs none -- the omitted parameter is passed as nullptr, which is that same empty shared_ptr. Without it the whole
    method is skipped, and RWPly_PlyWriterContext (every other member of which needs an open stream) is bound but
    unusable."""
    open_ = _method(rules_ir, "Rules_Sink", "Open")
    assert open_.skip_reason is None
    assert [(p.name, p.omitted) for p in open_.params] == [("theName", False), ("theStream", True)]
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Value": "Rules"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert "self.Open(theName, nullptr)" in cpp              # the omitted stream is passed as nullptr
    assert '.def("Open", [](const Rules_Sink &self, const char * theName)' in cpp   # ... and is gone from the signature
    assert not any("Rules_Sink::Open" in r for r in em.report + rules_ir.report)


def test_ir_non_public_base_blocks_construction_only_when_it_provides_operator_new(rules_ir):
    """A non-public base is always dropped (its members are not inherited publicly), but it only costs the class its
    constructors when it *provides* operator new: the allocation function is then inherited inaccessibly and
    `new Derived(...)` is ill-formed in C++ too (verified with a compile test on Message_LazyProgressScope, 2026-09-23).
    Until TKDEOBJ every non-public base was taken to block construction, which cost RWObj_CafReader -- the OBJ reader
    into an XDE document -- its public default constructor."""
    by = {c.name: c for c in rules_ir.classes}
    lazy, algo = by["Rules_LazyScope"], by["Rules_Algo"]
    assert lazy.bases == [] and lazy.constructible is False
    assert "Rules_LazyScope: non-public base Rules_AllocOptions provides operator new -> inaccessible, class not constructible" in lazy.skipped
    assert algo.bases == [] and algo.constructible is True         # same shape, but Rules_Options has no operator new
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Value": "Rules"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert "Rules_LazyScope: operator new is not public -> no constructors" in em.report
    assert "nb::init<>()" not in cpp.split('m.attr("Rules_LazyScope"))')[1].split(";")[0]
    assert "nb::init<>()" in cpp.split('m.attr("Rules_Algo"))')[1].split(";")[0]   # ... while Rules_Algo keeps its


def test_ir_noncopyable_detection_hidden_placement_new_arrays_and_std_out(rules_ir):
    by = {c.name: c for c in rules_ir.classes}
    # R-NONCOPYABLE detected: a container of a deleted-copy element, and a class holding that class by value
    assert by["Rules_Holder"].noncopyable and by["Rules_Holder2"].noncopyable and not by["Rules_NoCopy"].noncopyable
    assert "Rules_Holder: member mySeq of type NCollection_Sequence<Rules_NoCopy> is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)" in by["Rules_Holder"].skipped
    assert "Rules_Holder2: member myHolder of type Rules_Holder is not copyable -> bound through the non-copyable wrapper (R-NONCOPYABLE)" in by["Rules_Holder2"].skipped
    # class-level operator new without placement form: constructible=False; skipped only when not trivially copyable
    assert by["Rules_Alloc"].constructible is False and "Rules_AllocDerived" not in by
    assert any(r.startswith("Rules_AllocDerived: operator new is not public (no placement form) and the class is not trivially copyable") for r in rules_ir.report)
    # int (&)[3] is a fixed array returned as a list of 3 (R-FIXED-ARRAY); std::pair<int, int>& is an out-parameter (R-OUT), type name tuple
    nodes = _method(rules_ir, "Rules_Arrays", "Nodes")
    assert nodes.skip_reason is None and [(p.type, p.array_len, p.is_out, p.out_py) for p in nodes.params] == [("int", 3, True, "list")]
    steps = _method(rules_ir, "Rules_Arrays", "Steps")
    assert steps.skip_reason is None and [(p.name, p.is_out, p.out_py) for p in steps.params] == [("theN", False, ""), ("theSteps", True, "tuple")]


def test_ir_optional_pointer_fixed_arrays_pointer_results(rules_ir):
    # R-OPTIONAL-PTR: the null-defaulted pointer is dropped from the signature, the callee gets nullptr
    opt = _method(rules_ir, "Rules_Value", "Optional")
    assert opt.skip_reason is None and [(p.name, p.omitted) for p in opt.params] == [("theA", False), ("theErrorCode", True)]
    # R-FIXED-ARRAY: out array -> list of N, const array reference -> a sequence of N in, a member -> list property
    corners = _method(rules_ir, "Rules_Value", "Corners")
    assert [(p.type, p.array_len, p.is_out, p.out_py) for p in corners.params] == [("gp_Pnt", 8, True, "list")]
    nodes = _method(rules_ir, "Rules_Value", "SumNodes")
    assert [(p.type, p.array_len, p.is_out) for p in nodes.params] == [("int", 3, False)]
    value = next(c for c in rules_ir.classes if c.name == "Rules_Value")
    assert [(f.name, f.type, f.array_len) for f in value.fields if f.name == "myPeriod"] == [("myPeriod", "double", 3)]
    # R-PTR-REF: gp_Pnt*& -> gp_Pnt* with rv_policy::reference through a lambda
    ptr = _method(rules_ir, "Rules_Value", "PtrRef")
    assert ptr.skip_reason is None and ptr.result == "gp_Pnt *" and ptr.result_kind == ResultKind.PTR_CLASS and ptr.force_lambda
    # R-PTR-INCOMPLETE: Rules_Fwd is only forward-declared, but Rules_Fwd.hxx exists in the include directory
    fwd = _method(rules_ir, "Rules_Value", "Fwd")
    assert fwd.skip_reason is None and fwd.result_class_name == "Rules_Fwd"
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Value": "Rules"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert '.def("Optional", [](const Rules_Value &self, const int theA) { auto nanoocp_result = self.Optional(theA, nullptr); return nanoocp_result; }, nb::arg("theA")' in cpp
    assert "gp_Pnt theP[8]{}; auto nanoocp_result = self.Corners(theP); std::array<gp_Pnt, 8> theP_out;" in cpp
    assert "const std::array<int, 3> &theNodes) { int theNodes_arr[3]; std::copy(theNodes.begin(), theNodes.end(), theNodes_arr);" in cpp
    assert '.def_prop_rw("myPeriod", [](const Rules_Value &self) { std::array<double, 3> a;' in cpp
    assert '.def("PtrRef", [](Rules_Value &self) { auto nanoocp_result = self.PtrRef(); return nanoocp_result; }, nb::rv_policy::reference' in cpp
    # R-CSTR-NULL: the null-defaulted const char* is kept (unlike R-OPTIONAL-PTR) and takes str or None through nanoocp::OptionalCString
    enc = _method(rules_ir, "Rules_Value", "Encoding")
    assert enc.skip_reason is None and [(p.name, p.cstr_none, p.omitted, p.default) for p in enc.params] == [("theEncoding", True, False, "nullptr")]
    assert ('.def("Encoding", [](const Rules_Value &self, nanoocp::OptionalCString theEncoding) { auto nanoocp_result = self.Encoding(theEncoding.ptr); return nanoocp_result; }, '
            'nb::arg("theEncoding").none() = nb::none()') in cpp


def test_ir_and_emitter_visualization_idioms(rules_ir):
    """Bit-fields, hidden friends, alias enumerators, headerless references, char32_t, multi-word casts, width twins with
    out-parameters (found with TKService, 2026-09-22)."""
    by = {c.name: c for c in rules_ir.classes}
    vis = by["Rules_Vis"]
    # R-FIELD bit-fields are fields with is_bitfield, bound through lambdas
    assert [(f.name, f.is_bitfield) for f in vis.fields] == [("stick", True), ("visible", True), ("myPlain", False)]
    # R-PTR-INCOMPLETE for references: Rules_NoHeader has no header -> skipped and reported
    init = _method(rules_ir, "Rules_Vis", "Init")
    assert init.skip_reason == "param 'theStream': reference to incomplete type"
    assert "Rules_Vis::Init(): param 'theStream': reference to incomplete type" in vis.skipped
    # char32_t -> str
    assert _method(rules_ir, "Rules_Vis", "Advance").params[0].type == "char32_t"
    # hidden friend operator collected on the class
    assert [(f.name, f.is_operator, f.skip_reason) for f in vis.friend_ops] == [("operator+", True, None)]
    # alias enumerators recorded
    aspect = next(e for e in rules_ir.enums if e.py_name == "Rules_Aspect")
    assert aspect.aliases == ["Rules_A_Regular", "Rules_A_Bold"]
    # the nested class's default is qualified through the enclosing class
    it = next(n for n in vis.nested if n.py_name == "Iterator")
    assert it.ctors[0].params[1].default == "Rules_Vis::Filter_None"
    # the multi-word functional cast is spelled as a C-style cast
    tvec = by["Rules_TVec<unsigned long>"]
    assert tvec.ctors[0].params[0].default == "(unsigned long)(0)"
    em = Emitter(rules_ir, OCCT / "include" / "opencascade",
                 {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard", "Rules_Vis": "Rules", "Rules_Vis::Filter": "Rules",
                  "Rules_TTransient<int>": "Rules", "Rules_TTransient<double>": "Rules"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert '.def_prop_rw("stick", [](const Rules_Vis &self) { return static_cast<unsigned int>(self.stick); }, [](Rules_Vis &self, unsigned int v) { self.stick = v; }, R"nbdoc(' in cpp
    assert 'nanoocp_def_field(nb::borrow<nb::class_<Rules_Vis>>(m.attr("Rules_Vis")), "myPlain"' in cpp
    assert '.def("__add__", [](const Rules_Vis & theLeft, const Rules_Vis & theRight) { return theLeft + theRight; }, nb::is_operator()) /* free operator+ */' in cpp
    assert 'm.attr("Rules_A_Regular") = m.attr("Rules_Aspect").attr("Rules_A_Regular");' in cpp
    assert 'm.attr("Rules_A_Bold") = m.attr("Rules_Aspect").attr("Rules_A_Bold");' in cpp
    assert 'm.attr("Rules_Aspect_Bold") = ' not in cpp                # a first-value enumerator comes through export_values()
    assert "static_cast<std::decay_t<Rules_Vis::Filter>>(Rules_Vis::Filter_None)" in cpp
    assert "static_cast<std::decay_t<unsigned long>>((unsigned long)(0))" in cpp
    # R-COLLISION with width twins: both Coord overloads keep the plain name, the double one first
    assert cpp.count('.def("Coord", [](const Rules_Vis &self)') == 2 and "Coord__float__float" not in cpp
    assert cpp.index("double theX{}; double theY{};") < cpp.index("float theX{}; float theY{};")
    # Transient through a template base: both classes get nb::new_ constructors returning handles (2026-09-22)
    assert by["Rules_ViaTemplate"].is_transient and by["Rules_TTransient<int>"].is_transient and by["Rules_ViaTemplate"].bases == ["Rules_TTransient<int>"]
    assert by["Rules_ViaTypedef"].is_transient and by["Rules_ViaTypedef"].bases == ["Rules_TTransient<double>"]
    assert "nb::new_([]() { return opencascade::handle<Rules_ViaTemplate>(new Rules_ViaTemplate()); })" in cpp
    assert "new (self) Rules_ViaTemplate" not in cpp
    # 6a: the binder-Iterator-derived class is declared in the templates phase, after its base's instantiation
    it = by["Rules_PntSeq::Iterator"]
    assert it.after_templates and it.bases == ["NCollection_Sequence<gp_Pnt>::Iterator"]
    assert "NCollection_Sequence<gp_Pnt>" in rules_ir.instances
    templates_fn = cpp[cpp.index("void nanoocp_templates_Rules"):cpp.index("void nanoocp_define_Rules")]
    decl = 'nb::class_<Rules_PntSeq::Iterator, NCollection_Sequence<gp_Pnt>::Iterator> cls(m.attr("Rules_PntSeq"), "Iterator"'
    assert decl in templates_fn and templates_fn.index("bind_NCollection_Sequence<gp_Pnt>") < templates_fn.index(decl)
    # 6a: a class deriving from the binder instantiation itself
    table = by["Rules_Table"]
    assert table.after_templates and table.bases == ["NCollection_DataMap<int, double>"] and "NCollection_DataMap<int, double>" in rules_ir.instances
    decl = 'nb::class_<Rules_Table, NCollection_DataMap<int, double>> cls(m, "Rules_Table"'
    assert decl in templates_fn and templates_fn.index("bind_NCollection_DataMap<int, double>") < templates_fn.index(decl)


def test_ir_template_bases_of_instantiations(rules_ir):
    by = {c.name: c for c in rules_ir.classes}
    # the alias instantiation's template base was instantiated through the probe re-parse and names the derived's base
    assert "Rules_TBase<double>" in by and [m.name for m in by["Rules_TBase<double>"].methods] == ["BaseValue"]
    assert by["Rules_TDerived<double>"].py_name == "Rules_TDouble" and by["Rules_TDerived<double>"].bases == ["Rules_TBase<double>"]
    # the CRTP base cannot be instantiated: dropped, the class binds without it
    crtp = by["Rules_Crtp<int>"]
    assert crtp.py_name == "Rules_CrtpInt" and crtp.bases == [] and [m.name for m in crtp.methods] == ["X"]
    assert any(r.startswith("Rules_Crtp<int>: template base Rules_CrtpBase<int, Rules_Crtp<int>> cannot be instantiated -> dropped") for r in rules_ir.report)


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
    width_ok = {"Abs", "Min", "Max", "Convert_LinearRGB_To_sRGB", "Convert_sRGB_To_LinearRGB", "Value", "SetValue", "ReSize", "__init__",
                "SetWidth", "SetScale", "AddVertex", "SetCoord"}    # Graphic3d_AspectLine3d/AspectMarker3d/ArrayOfPrimitives/Vertex: double and float overloads
    unexpected = [d for d in dups if not (d[2][0] in width_ok and any(t in ("float", "int") for t in d[2][1]))
                  and not (d[0] in ("TCollection", "Standard", "Resource") and "str" in d[2][1])
                  and d[1] != "Standard_Mutex.Sentry"         # Sentry(Standard_Mutex&) / Sentry(Standard_Mutex*): the same call
                  and (d[1], d[2][0]) != ("Graphic3d_Vertex", "Coord")   # Coord(double&...) / Coord(float&...): width twins with out-params only
                  # str-kind twins outside TCollection (decision 2026-09-21, unchanged): Add(const char*) / Add(AsciiString) /
                  # Add(char) all append the same text, and XSControl_Utils::ToHString returns the same text as an
                  # HAsciiString instead of an HExtendedString (a Draw helper class)
                  and (d[1], d[2][0]) not in (("Interface_LineBuffer", "Add"), ("XSControl_Utils", "ToHString"))]
    assert unexpected == [], unexpected
    assert len(dups) < 90        # 61 with TKService, 71 with TKXSBase (2026-09-22)


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


# Design.md 6 R-LINK
def test_extra_link_libraries_from_the_emitted_includes(rules_ir):
    """A toolkit module links every OCCT toolkit whose types it names, not only OCCT's own EXTERNLIB closure: the
    handle caster instantiates typeid(T), so a forward-declared class of another toolkit (DE_Provider names
    XSControl_WorkSession and TDocStd_Document, neither in TKDE's EXTERNLIB) leaves an undefined typeinfo symbol.
    The Emitter records the include list it wrote; the toolkit's extra libraries are the owners of those headers
    minus the link closure."""
    tree = load_tree(OCCT_SRC, OCCT)
    assert tree.toolkit_of_header["TDocStd_Document.hxx"] == "TKLCAF"
    assert tree.toolkit_of_header["XSControl_WorkSession.hxx"] == "TKXSBase"
    assert tree.toolkit_of_header["gp_Pnt.hxx"] == "TKMath"
    closure = tree.link_closure("TKDE")                      # EXTERNLIB: TKernel, TKMath, TKBRep (transitively)
    assert {"TKDE", "TKernel", "TKMath", "TKBRep"} <= closure
    assert closure.isdisjoint({"TKLCAF", "TKXSBase"})        # what OCCT itself does not link
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    em.emit()
    assert "Rules.hxx" in em.includes
    assert "gp_Pnt.hxx" in em.includes                       # a parameter type's header, not one of the package's own
    extra = sorted({tree.toolkit_of_header[h] for h in em.includes if h in tree.toolkit_of_header} - tree.link_closure("TKBRep"))
    assert extra == []                                       # gp_Pnt is TKMath, already in TKBRep's closure
    assert sorted({tree.toolkit_of_header[h] for h in em.includes if h in tree.toolkit_of_header}
                  - tree.link_closure("TKernel")) == ["TKMath"]   # from TKernel's point of view gp_Pnt would be an extra library


def test_generated_toolkits_cmake_declares_the_extra_link_libraries():
    """The checked-in toolkits.cmake carries what the generator computed (R-LINK); TKDE is the first toolkit that needs it."""
    cmake = (ROOT / "src" / "cpp" / "toolkits.cmake").read_text()
    assert "set(NANOOCP_TKDE_EXTRA_LIBS TKLCAF TKXSBase)" in cmake
    assert "${NANOOCP_${tk}_EXTRA_LIBS}" in (ROOT / "CMakeLists.txt").read_text()


def test_unsupported_std_types_are_reported_by_name(rules_ir):
    """An std type nanobind has no caster for is named in the report: a std::mutex& result read as "iostream type"
    before 2026-09-22 (DE_Wrapper::GlobalLoadMutex, StdPrs_BRepFont::Mutex, SelectMgr_BVHThreadPool::BVHThread::BVHMutex)."""
    line = next(r for r in rules_ir.report if "LoadMutex" in r)
    assert line.endswith("unsupported std type: std::mutex")
    assert categorize(line) == "std"
    assert all("iostream type" not in r for r in rules_ir.report if "LoadMutex" in r)
    assert any("Dump" not in r or "iostream" not in r for r in rules_ir.report)   # the ostream& member is a stream, not skipped


# Design.md 6 R-DEFAULT
def test_a_braced_default_is_list_initialised(rules_ir):
    """`= {}` in the header (XSAlgo_ShapeProcessor's DE_ShapeFixParameters, the ParameterMap of SetShapeFixParameters,
    3 more in TKXSBase) must be emitted as std::decay_t<T>{} -- static_cast from a braced-init-list does not compile
    ("expected expression", 2026-09-22)."""
    assert _method(rules_ir, "Rules_Value", "Braced").params[0].default == "{ }"   # libclang spells the tokens
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert 'nb::arg("theXYZ") = std::decay_t<const gp_XYZ &>{ }' in cpp
    assert "static_cast<std::decay_t<const gp_XYZ &>>({ })" not in cpp


# Design.md 6 R-BITSET
def test_a_bitset_is_a_set_of_indices(rules_ir):
    """std::bitset<N> is cast to a Python set of the indices whose bit is set, so it is not reported as an unsupported
    std type; its size is a non-type template argument (libclang gives an INVALID type, which the std check skips)."""
    assert all("bitset" not in line for line in rules_ir.report), [l for l in rules_ir.report if "bitset" in l]
    assert _method(rules_ir, "Rules_Value", "Flags").skip_reason is None
    assert _method(rules_ir, "Rules_Value", "GetFlags").skip_reason is None
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert '.def("Flags"' in cpp and '.def("GetFlags"' in cpp


# Design.md 6 R-STATIC-S
def test_resolve_static_renames_follows_the_inheritance_chain():
    """Python cannot hold a static and an instance method of one name, and nanobind refuses the second registration
    across inheritance too: a def_static on a derived class finds the base's inherited instance method. The real case
    is XCAFDoc_NoteBalloon (static Set only) : XCAFDoc_NoteComment : XCAFDoc_Note (instance Set) -- the import of
    _TKXCAF aborted with "mismatched static/instance method flags in function overloads" (2026-09-22)."""
    def cls(name, base, *methods):
        return Class(name=name, py_name=name, bases=[base] if base != "" else [], header=f"{name}.hxx", doc="",
                     is_transient=True, is_exception=False, is_abstract=False,
                     methods=[Method(name=n, params=[], result="void", result_kind=ResultKind.VALUE, result_class="",
                                     is_static=static, is_const=False, is_noexcept=False, doc="") for n, static in methods])
    note = cls("XCAFDoc_Note", "TDF_Attribute", ("Set", False))
    comment = cls("XCAFDoc_NoteComment", "XCAFDoc_Note", ("Set", True), ("Set", False))
    balloon = cls("XCAFDoc_NoteBalloon", "XCAFDoc_NoteComment", ("Set", True))
    renames = resolve_static_renames([note, comment, balloon])
    assert renames["XCAFDoc_NoteComment"] == {"Set"}      # static and instance in the same class (the pre-2026-09-22 rule)
    assert renames["XCAFDoc_NoteBalloon"] == {"Set"}      # only a static of its own: the instance Set is two levels up
    assert renames["XCAFDoc_Note"] == set()               # declares no static Set, so it has nothing to rename
    # the other direction: the base has the static, a descendant the instance -> the base's static is the one to rename
    base = cls("Base", "", ("Get", True))
    derived = cls("Derived", "Base", ("Get", False))
    renames = resolve_static_renames([base, derived])
    assert renames["Base"] == {"Get"} and renames["Derived"] == set()
    # unrelated classes do not interact, and a skipped overload does not count
    other = cls("Other", "", ("Set", True))
    assert resolve_static_renames([note, other])["Other"] == set()
    skipped = cls("Skipped", "XCAFDoc_Note", ("Set", True))
    skipped.methods[0].skip_reason = "x"
    assert resolve_static_renames([note, skipped])["Skipped"] == set()


# Design.md 6 R-OUT
def test_the_lambda_temporary_cannot_collide_with_a_parameter(rules_ir):
    """99 OCCT parameters are called `result` (IGESConvGeom::SplineCurveFromIGES(..., handle<Geom_BSplineCurve>&
    result)); when such a parameter is an out-parameter of a non-void method, a bare `result` for the C++ return value
    is a redefinition in the same lambda (TKDEIGES did not compile, 2026-09-22). Generated temporaries carry the
    nanoocp_ prefix, which no OCCT name uses."""
    em = Emitter(rules_ir, OCCT / "include" / "opencascade", {"gp_Pnt": "gp", "gp_XYZ": "gp", "Standard_Transient": "Standard"},
                 {"gp": "TKMath", "Standard": "TKernel", "Rules": "TKRules"}, {}, ["TKernel", "TKMath", "TKRules"], {})
    cpp = em.emit()
    assert "auto nanoocp_result = " in cpp
    assert re.search(r"\bauto result\b", cpp) is None and re.search(r"> result\(", cpp) is None


def test_third_party_include_paths_are_passed_to_clang():
    """An installed OCCT header can include a third-party one: RWGltf_GltfJsonParser.hxx has
    #include <rapidjson/document.h> under HAVE_RAPIDJSON, so the parse needs the same include path the build used
    (deps/rapidjson from deps/fetch-rapidjson.sh). Without it the TKDEGLTF parse failed with "file not found"."""
    tree = load_tree(OCCT_SRC, OCCT)
    args = parse.clang_args(tree)
    assert "-DHAVE_RAPIDJSON" in args
    rapidjson = OCCT.parent / "rapidjson" / "include"
    if rapidjson.is_dir():
        assert f"-I{rapidjson}" in args
        assert (rapidjson / "rapidjson" / "document.h").exists()
    assert "${NANOOCP_RAPIDJSON_DIR}" in (ROOT / "CMakeLists.txt").read_text()   # ... and the C++ build too
