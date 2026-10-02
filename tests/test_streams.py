"""std::ostream& / std::istream& parameters (Binding-Rules.md): an output stream comes back as a str, an input stream is a
text file-like object (io.StringIO, an open file) so that it cannot be confused with a file-path overload."""
import io
import os
import tempfile

import pytest

from nanocct import BRep, BRepTools, Bnd, Geom, GeomTools, TopAbs, TopoDS, gp


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
    Standard_EXPORT (IntRes2d_Transition.lxx:19), so the Windows DLL does not export it and R-UNDEFINED skips it there
    -- C++ could not call it on Windows either (measured on gauss 2026-09-25)."""
    from conftest import report
    from nanocct.IntRes2d import IntRes2d_Transition

    if "__str__" in vars(IntRes2d_Transition):
        assert str(IntRes2d_Transition()).startswith("   Position : ")
    else:
        assert any("operator<<(std::ostream &, IntRes2d_Transition &): declared in the header, no definition in libTKGeomAlgo"
                   in line for line in report("TKGeomAlgo")[2])


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
