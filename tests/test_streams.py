"""std::ostream& / std::istream& parameters (Design.md 6): an output stream comes back as a str, an input stream is a
text file-like object (io.StringIO, an open file) so that it cannot be confused with a file-path overload."""
import io
import os
import tempfile

import pytest

from nanoocp import BRep, BRepTools, Bnd, Geom, GeomTools, TopAbs, TopoDS, gp


def _edge() -> TopoDS.TopoDS_Edge:
    e = TopoDS.TopoDS_Edge()
    BRep.BRep_Builder().MakeEdge(e, Geom.Geom_Line(gp.gp_Pnt(), gp.gp_Dir(1.0, 0.0, 0.0)), 1e-7)
    return e


def test_dump_json_round_trip():
    text = gp.gp_Pnt(1.0, 2.0, 3.0).DumpJson()                        # DumpJson(Standard_OStream&, depth) -> str
    assert text == '"gp_Pnt": [1, 2, 3]'
    p = gp.gp_Pnt()
    done, pos = p.InitFromJson(io.StringIO(text), 1)                   # InitFromJson(const Standard_SStream&, int& pos): pos is in/out, starts at 1
    assert done and p.Coord() == (1.0, 2.0, 3.0) and pos > 1
    box = Bnd.Bnd_Box()
    box.Add(gp.gp_Pnt(1.0, 2.0, 3.0))
    assert box.DumpJson() == '"CornerMin": [1, 2, 3], "CornerMax": [1, 2, 3], "Gap": 0, "Flags": 0'
    assert TopAbs.TopAbs.Print(TopAbs.TopAbs_ShapeEnum.TopAbs_FACE) == "FACE"   # Standard_OStream& Print(x, Standard_OStream&): the stream result is dropped


def test_brep_text_streams_and_path_overloads():
    e = _edge()
    text = BRepTools.BRepTools.Write(e)                                # Write(shape, Standard_OStream&) -> str
    assert text.startswith("DBRep_DrawableShape") or "CASCADE Topology" in text
    back = TopoDS.TopoDS_Shape()
    BRepTools.BRepTools.Read(back, io.StringIO(text), BRep.BRep_Builder())          # Read(shape, Standard_IStream&, builder)
    assert back.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    path = os.path.join(tempfile.mkdtemp(), "e.brep")
    with open(path, "w") as f:
        f.write(text)
    from_path = TopoDS.TopoDS_Shape()
    assert BRepTools.BRepTools.Read(from_path, path, BRep.BRep_Builder()) is True   # the file-path overload stays reachable
    assert from_path.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    with open(path) as f:                                              # any object with read()
        from_file = TopoDS.TopoDS_Shape()
        BRepTools.BRepTools.Read(from_file, f, BRep.BRep_Builder())
    assert from_file.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
    with pytest.raises(TypeError):
        BRepTools.BRepTools.Read(from_file, 42, BRep.BRep_Builder())   # neither a path nor a file-like object


def test_geomtools_write():
    text = GeomTools.GeomTools.Write(Geom.Geom_Circle(gp.gp_Ax2(), 2.0))
    assert text.split()[0] == "2"                                      # curve type code of a circle in the BRep geometry format


def test_binary_stream_is_a_lossless_str():
    from nanoocp import BinTools
    data = BinTools.BinTools.Write(_edge())                            # a binary format: str via surrogateescape, never raises
    assert isinstance(data, str) and len(data.encode("utf-8", "surrogateescape")) > len(data)
    back = TopoDS.TopoDS_Shape()
    BinTools.BinTools.Read(back, io.StringIO(data))                    # the inverse encoding on the way in
    assert back.ShapeType() == TopAbs.TopAbs_ShapeEnum.TopAbs_EDGE
