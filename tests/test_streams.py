"""std::ostream& / std::istream& parameters (Binding-Rules.md): an output stream comes back as a str, an input stream is a
text file-like object (io.StringIO, an open file) so that it cannot be confused with a file-path overload."""
import io
import os
import struct
import tempfile

import pytest

from nanocct import BRep, BRepPrimAPI, BRepTools, Bnd, Geom, Geom2d, GeomTools, TopAbs, TopoDS, gp


def _edge() -> TopoDS.TopoDS_Edge:
    e = TopoDS.TopoDS_Edge()
    BRep.BRep_Builder().MakeEdge(e, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    return e


def test_dump_json_round_trip():
    text = gp.gp_Pnt(1.0, 2.0, 3.0).DumpJson()                        # DumpJson(Standard_OStream&, depth) -> str
    assert text == '"gp_Pnt": [1, 2, 3]'
    p = gp.gp_Pnt()
    done, pos = p.InitFromJson(io.StringIO(text), 1)                   # InitFromJson(const Standard_SStream&, int& pos): pos is in/out, starts at 1
    assert done and p.Coord__float__float__float() == (1.0, 2.0, 3.0) and pos > 1
    box = Bnd.Bnd_Box()
    box.Add(gp.gp_Pnt(1.0, 2.0, 3.0))
    assert box.DumpJson() == '"CornerMin": [1, 2, 3], "CornerMax": [1, 2, 3], "Gap": 0, "Flags": 0'
    assert TopAbs.TopAbs.Print_s(TopAbs.TopAbs_ShapeEnum.TopAbs_FACE) == "FACE"   # Standard_OStream& Print(x, Standard_OStream&): the stream result is dropped


def test_brep_text_streams_and_path_overloads():
    e = _edge()
    text = BRepTools.BRepTools.Write_s(e)                                # Write(shape, Standard_OStream&) -> str
    assert text.startswith("DBRep_DrawableShape") or "CASCADE Topology" in text
    back = TopoDS.TopoDS_Shape()
    BRepTools.BRepTools.Read_s(back, io.StringIO(text), BRep.BRep_Builder())          # Read(shape, Standard_IStream&, builder)
    assert back.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    path = os.path.join(tempfile.mkdtemp(), "e.brep")
    with open(path, "w") as f:
        f.write(text)
    from_path = TopoDS.TopoDS_Shape()
    assert BRepTools.BRepTools.Read_s(from_path, path, BRep.BRep_Builder()) is True   # the file-path overload stays reachable
    assert from_path.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    with open(path) as f:                                              # any object with read()
        from_file = TopoDS.TopoDS_Shape()
        BRepTools.BRepTools.Read_s(from_file, f, BRep.BRep_Builder())
    assert from_file.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    with pytest.raises(TypeError):
        BRepTools.BRepTools.Read_s(from_file, 42, BRep.BRep_Builder())   # neither a path nor a file-like object


def test_geomtools_write():
    text = GeomTools.GeomTools.Write_s(Geom.Geom_Circle(gp.gp_Ax2(), 2.0))
    assert text.split()[0] == "2"                                      # curve type code of a circle in the BRep geometry format


def test_a_text_stream_takes_a_precision_hint():
    """R-STREAM-OUT: precision_hint=n is std::ostream::precision(n) on the stream the binding drops. GeomTools::Write(curve,
    stream) writes with the stream's precision; the default is a new stream's 6, so the text is what C++ writes into a new
    stream. A writer that sets its own precision overrides the hint, as it does a C++ caller's, and the docstring says so."""
    curve = Geom.Geom_TrimmedCurve(Geom.Geom_Circle(gp.gp_Ax2(gp.gp_Pnt(3, 0, 0), gp.gp_Dir(0, 0, 1)), 2), 18, 23, False, False)
    default = GeomTools.GeomTools.Write_s(curve)
    assert default == GeomTools.GeomTools.Write_s(curve, precision_hint=6)
    rough = GeomTools.GeomTools.Read_s__Geom_Curve(io.StringIO(default))
    assert rough.FirstParameter() != curve.FirstParameter()              # 6 significant digits
    exact = GeomTools.GeomTools.Read_s__Geom_Curve(io.StringIO(GeomTools.GeomTools.Write_s(curve, precision_hint=17)))
    assert (exact.FirstParameter(), exact.LastParameter()) == (curve.FirstParameter(), curve.LastParameter())
    with pytest.raises(TypeError):
        GeomTools.GeomTools.Write_s(curve, 17)                             # keyword-only: never taken for an OCCT argument
    point = gp.gp_Pnt(0.1, 0.0, 0.0)
    assert point.DumpJson() == '"gp_Pnt": [0.1, 0, 0]'
    assert point.DumpJson(precision_hint=17) == '"gp_Pnt": [0.10000000000000001, 0, 0]'
    assert point.DumpJson(-1, precision_hint=17) == point.DumpJson(precision_hint=17)   # after the OCCT arguments
    sphere = BRepPrimAPI.BRepPrimAPI_MakeSphere(gp.gp_Pnt(0.1, 0.2, 0.3), 1.234567891).Shape()
    brep = BRepTools.BRepTools.Write_s(sphere)
    assert "1.234567891" in brep                                         # not 6 digits: TopTools_ShapeSet and its geometry sets set their own
    assert BRepTools.BRepTools.Write_s(sphere, precision_hint=3) == brep   # the hint is overridden, as a C++ caller's precision is
    assert "A writer that sets its own" in BRepTools.BRepTools.Write_s.__doc__
    assert "precision_hint: the precision the stream" in point.DumpJson.__doc__


def test_a_binary_stream_and_str_take_no_precision_hint():
    """Binary packages write raw doubles, and __str__ (R-STR) takes no argument: neither has the keyword nor its line."""
    from nanocct import BinTools
    from nanocct.math import math_Vector
    with pytest.raises(TypeError):
        BinTools.BinTools.Write_s(_edge(), precision_hint=17)
    assert "precision" not in BinTools.BinTools.Write_s.__doc__
    assert "precision" not in math_Vector.__str__.__doc__
    assert "*, precision_hint: int = 6" in GeomTools.GeomTools.Write_s.__doc__


def test_a_stream_wrapper_parameter_takes_the_stream_it_wraps():
    """R-STREAM-WRAPPER: BinTools_OStream and BinTools_IStream only wrap a stream (their one constructor takes it, their
    state is private), so Python can make neither; a member taking one takes the stream itself -- bytes back, a BinaryIO
    in -- and the binding makes the wrapper on its stream. VrmlData_InBuffer is no wrapper: its public fields are the
    parse state VrmlData_Scene prepares (a new one's line buffer is uninitialised), so its members are unchanged."""
    from nanocct import BinTools, VrmlData
    curve = Geom.Geom_TrimmedCurve(Geom.Geom_Circle(gp.gp_Ax2(), 2.0), 1.0, 2.5)
    data = BinTools.BinTools_CurveSet.WriteCurve_s(curve)                # WriteCurve(curve, BinTools_OStream&)
    assert isinstance(data, bytes)
    back = BinTools.BinTools_CurveSet.ReadCurve_s(io.BytesIO(data))
    assert (back.FirstParameter(), back.LastParameter()) == (1.0, 2.5)
    surface = Geom.Geom_SphericalSurface(gp.gp_Ax3(), 1.5)
    assert isinstance(BinTools.BinTools_SurfaceSet.WriteSurface_s(surface), bytes)
    line = Geom2d.Geom2d_Line(gp.gp_Pnt2d(1.0, 2.0), gp.gp_Dir2d(0.0, 1.0))
    assert BinTools.BinTools_Curve2dSet.ReadCurve2d_s(io.BytesIO(BinTools.BinTools_Curve2dSet.WriteCurve2d_s(line))).Location().Y() == 2.0
    # ReadLocation(BinTools_IStream&): a simple location record -- its type byte (BinTools_ObjectType_SimpleLocation, 6) and
    # the 3x4 matrix, row by row, as little-endian doubles (BinTools_IStream::operator>>(gp_Trsf&))
    record = bytes([6]) + struct.pack("<12d", 1, 0, 0, 4.0, 0, 1, 0, 5.0, 0, 0, 1, 6.0)
    location = BinTools.BinTools_ShapeReader().ReadLocation(io.BytesIO(record))
    moved = location.Transformation().TranslationPart()
    assert (moved.X(), moved.Y(), moved.Z()) == (4.0, 5.0, 6.0)
    with pytest.raises(TypeError):                                        # a binary package: BinaryIO, not TextIO
        BinTools.BinTools_ShapeReader().ReadLocation(io.StringIO(""))
    # VrmlData_Box::Read(VrmlData_InBuffer&) still takes the struct, which nothing in Python can make
    assert "theBuffer: nanocct.VrmlData.VrmlData_InBuffer" in VrmlData.VrmlData_Box.Read.__doc__


def test_a_file_like_moves_on_by_what_occt_read(tmp_path):
    """R-STREAM-IN: after the call the file-like object is where the C++ stream would be -- after what OCCT read -- so two
    reads take two tokens, as GeomTools::GetReal does on one stream. The caster only peeks (a refused overload leaves the
    object as it was), an exception leaves it unmoved, and an object that cannot seek stays read to its end."""
    from nanocct import BinTools
    text = io.StringIO("1.25 7 tail")
    assert (GeomTools.GeomTools.GetReal_s(text), GeomTools.GeomTools.GetReal_s(text)) == (1.25, 7.0)
    assert text.read() == " tail"
    multibyte = io.StringIO("1\u00e9 7")                                 # the consumed UTF-8 bytes, counted as characters
    GeomTools.GeomTools.GetReal_s(multibyte)
    assert GeomTools.GeomTools.GetReal_s(multibyte) == 7.0 and multibyte.read() == ""
    path = tmp_path / "reals.txt"
    path.write_text("\u00e9\u00e9 2.5 3.5 x", encoding="utf-8")
    with open(path, encoding="utf-8") as f:                              # a text file: seek takes tell()'s cookies only
        f.read(3)
        assert (GeomTools.GeomTools.GetReal_s(f), GeomTools.GeomTools.GetReal_s(f)) == (2.5, 3.5)
        assert f.read() == " x"
    json = io.StringIO('"gp_Pnt": [1, 2, 3]')
    assert gp.gp_Pnt().InitFromJson(json, 1) == (True, 20) and json.tell() == 0   # a const stream: not moved
    refused = io.StringIO("not binary")
    with pytest.raises(TypeError):
        BinTools.BinTools.Read_s(TopoDS.TopoDS_Shape(), refused)
    assert refused.tell() == 0
    curves = [Geom.Geom_TrimmedCurve(Geom.Geom_Circle(gp.gp_Ax2(), r), 0.5, last) for r, last in ((2.0, 2.5), (3.0, 1.5))]
    binary = io.BytesIO(b"".join(BinTools.BinTools_CurveSet.WriteCurve_s(c) for c in curves))
    assert [BinTools.BinTools_CurveSet.ReadCurve_s(binary).LastParameter() for _ in curves] == [2.5, 1.5]
    assert binary.read() == b""
    garbage = io.BytesIO(b"garbage that is no BinTools header")
    with pytest.raises(Exception) as thrown:                            # OCCT throws: the object stays where it was
        BinTools.BinTools.Read_s(TopoDS.TopoDS_Shape(), garbage)
    assert thrown.type.__name__ == "Storage_StreamTypeMismatchError" and garbage.tell() == 0

    class Pipe:                                                           # read() only: no seek
        def __init__(self, text):
            self.text = text

        def read(self):
            text, self.text = self.text, ""
            return text

    pipe = Pipe("4.5 6")
    assert GeomTools.GeomTools.GetReal_s(pipe) == 4.5 and pipe.text == ""


def test_binary_stream_is_bytes(tmp_path):
    # the BinTools package carries a binary format (overrides.toml [stream] binary_packages): bytes out, BinaryIO in
    from nanocct import BinTools
    edge = _edge()
    data = BinTools.BinTools.Write_s(edge)
    assert isinstance(data, bytes) and data.startswith(b"\nOpen CASCADE Topology")
    back = TopoDS.TopoDS_Shape()
    BinTools.BinTools.Read_s(back, io.BytesIO(data))
    assert back.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    with pytest.raises(TypeError):                                     # a text file-like object does not match
        BinTools.BinTools.Read_s(back, io.StringIO("x"))
    path = str(tmp_path / "e.bin")                                     # the bytes equal the file form
    assert BinTools.BinTools.Write_s(edge, path) is True
    assert (tmp_path / "e.bin").read_bytes() == data
    assert BinTools.BinTools.Write_s.__doc__.splitlines()[0].endswith("-> bytes")
    assert "theStream: typing.BinaryIO" in BinTools.BinTools.Read_s.__doc__


# ---- R-STR: OCCT's "print me" operator<< as __str__ (roadmap 8.14) ----------------------------------------------

def test_print_operator_is_str():
    """`operator<<(Standard_OStream&, const T&)` -- free, hidden friend or the member form -- renders exactly what OCCT
    prints, which for these classes is their Dump(); repr() stays nanobind's default."""
    from nanocct.math import math_IntegerVector, math_Matrix, math_Vector
    from nanocct.TDF import TDF_Data

    m = math_Matrix(1, 2, 1, 2, 3.0)
    assert str(m) == m.Dump() and str(m).startswith("math_Matrix of RowNumber = 2 and ColNumber = 2")
    assert repr(m).startswith("<nanocct.math.math_Matrix object at ")
    v = math_Vector(1, 3, 2.0)
    assert str(v) == v.Dump()                                          # the friend of math_VectorBase<double>
    assert str(math_IntegerVector(1, 2, 7)).startswith("math_Vector of Length = 2")   # ... and of math_VectorBase<int>
    label = TDF_Data().Root()
    assert str(label) == label.Dump()                                  # member `operator<<(Standard_OStream&) const`


def test_print_operator_where_there_was_no_text_method():
    """IntRes2d_Transition has no Dump or Print, so its operator<< is its only text form. The operator carries no
    Standard_EXPORT (IntRes2d_Transition.lxx:19), nor does CDM_MetaData's member operator<<: the Windows DLLs export
    both through deps/occt-windows-exports.txt, so every platform binds them as __str__ (from 2026-10-03 until then they
    were skipped everywhere, because Windows could not link them)."""
    from nanocct.CDM import CDM_MetaData
    from nanocct.IntRes2d import IntRes2d_Transition

    assert "__str__" in vars(IntRes2d_Transition) and "__str__" in vars(CDM_MetaData)
    assert str(IntRes2d_Transition()) == "   Position : Milieu\n   Type de transition : Indeterminee\n\n"  # OCCT's


def test_operators_that_are_not_print_me_stay_unbound():
    """BinTools' operator<<(ostream&, const gp_Pnt&) writes binary doubles and belongs to another package's class;
    BinObjMgt_Persistent's is its binary Write; Standard_Failure is a Python exception whose str() is its message."""
    from conftest import report
    from nanocct.BinObjMgt import BinObjMgt_Persistent

    assert "__str__" not in vars(gp.gp_Pnt) and "__str__" not in vars(gp.gp_Trsf)
    assert "__str__" not in vars(BinObjMgt_Persistent)
    lines = report("TKBRep")[0] + report("TKBinL")[0] + report("TKernel")[0] + report("TKLCAF")[0]
    reasons = [line for line in lines if "not bound as __str__" in line]
    assert all(line.startswith("stream\t") for line in reasons)
    # BinTools' two operators carry no Standard_EXPORT: on Windows R-UNDEFINED skips them before R-STR sees them
    for operand in ("gp_Pnt", "gp_Trsf"):
        assert any(f"operand {operand} is not a class of this package" in line for line in reasons) or \
            any(f"operator<<(Standard_OStream &, const {operand} &): declared in the header, no definition in libTKBRep" in line
                for line in report("TKBRep")[2])
    assert any("BinObjMgt_Persistent &): not bound as __str__: binary stream" in line for line in reasons)
    assert any("const Standard_Failure &): not bound as __str__: exception class" in line for line in reasons)
    assert sum("member operator<<(Standard_OStream&) is bound as __str__ already" in line for line in reasons) == 3
