"""R-MI-REF (Binding-Rules.md): every kind of crossing of a class stored by a base at a non-zero offset.

NCollection_Shared<T> derives from Standard_Transient and then T, and its Python object holds the address of the T part
(Runtime.md 5.2). Until 8.0.2.0 only the handle crossing converted between that address and the object: a reference
result read the wrong memory (ElementsOfDomain() of an empty structure had Size() 1, Add() crashed) and a reference
argument handed OCCT the wrong address. Each test here takes one kind of crossing through a real OCCT member, so a
crossing that is not converted fails here instead of in a mesher three calls later."""
import gc

import pytest

from nanocct.BRepMesh import (BRepMesh_Circle, BRepMesh_CircleInspector, BRepMesh_CircleTool, BRepMesh_DataStructureOfDelaun,
                              BRepMesh_Delaun, BRepMesh_Edge, BRepMesh_Free, BRepMesh_Frontier, BRepMesh_MeshTool,
                              BRepMesh_Triangle, BRepMesh_Vertex)
from nanocct.gp import gp_XY
from nanocct.NCollection import (NCollection_Array1, NCollection_DynamicArray, NCollection_IncAllocator,
                                 NCollection_Shared__NCollection_Array1__BRepMesh_Vertex,
                                 NCollection_Shared__NCollection_DynamicArray__int,
                                 NCollection_Shared__NCollection_PackedMap__int)
from nanocct.Precision import Precision


def _triangle_structure():
    """A structure holding one frontier triangle (0,0) (1,0) (0.5,0.5) and its element index."""
    structure = BRepMesh_DataStructureOfDelaun(NCollection_IncAllocator())
    nodes = [structure.AddNode(BRepMesh_Vertex(u, v, BRepMesh_Frontier)) for u, v in ((0.0, 0.0), (1.0, 0.0), (0.5, 0.5))]
    edges, orientations = [], []
    for i in range(3):
        link = structure.AddLink(BRepMesh_Edge(nodes[i], nodes[(i + 1) % 3], BRepMesh_Frontier))
        edges.append(abs(link))
        orientations.append(link > 0)
    element = structure.AddElement(BRepMesh_Triangle(edges, orientations, BRepMesh_Free))
    return structure, element


def _elements(structure):
    domain = structure.ElementsOfDomain()
    keys = []
    it = type(domain).Iterator(domain)
    while it.More():
        keys.append(it.Key())
        it.Next()
    return keys


def test_const_reference_result_reads_the_member():
    """const IMeshData::MapOfInteger& ElementsOfDomain() const: a member held by value."""
    empty = BRepMesh_DataStructureOfDelaun(NCollection_IncAllocator())
    assert empty.ElementsOfDomain().IsEmpty() is True
    assert empty.ElementsOfDomain().Size() == 0
    structure, element = _triangle_structure()
    assert structure.ElementsOfDomain().Size() == 1
    assert _elements(structure) == [element]


def test_reference_result_is_one_object_and_keeps_its_owner():
    structure, element = _triangle_structure()
    domain = structure.ElementsOfDomain()
    assert structure.ElementsOfDomain() is domain
    del structure
    gc.collect()
    assert domain.Size() == 1 and domain.Contains(element) is True


def test_mutable_reference_result_reads_the_member():
    """IMeshData::ListOfInteger& GetShotCircles(): the circles the inspected point lies in."""
    inspector = BRepMesh_CircleInspector(Precision.PConfusion_s(), 1, NCollection_IncAllocator())
    center = gp_XY()
    ok, radius = BRepMesh_CircleTool.MakeCircle_s(gp_XY(0, 0), gp_XY(1, 0), gp_XY(0, 1), center)
    assert ok is True
    inspector.Bind(1, BRepMesh_Circle(center, radius))
    inspector.SetPoint(gp_XY(0.5, 0.5))
    inspector.Inspect(1)
    assert inspector.GetShotCircles().Size() == 1 and inspector.GetShotCircles().IsEmpty() is False
    inspector.SetPoint(gp_XY(5.0, 5.0))
    inspector.Inspect(1)
    assert inspector.GetShotCircles().IsEmpty() is True


def test_reference_argument_reaches_the_call():
    """AddVertices(IMeshData::VectorOfInteger&): the centroid splits the triangle into three."""
    structure, _ = _triangle_structure()
    mesher = BRepMesh_Delaun(structure, 2, 2, True)
    point = structure.AddNode(BRepMesh_Vertex(0.5, 0.5 / 3.0, BRepMesh_Free))
    vertices = NCollection_Shared__NCollection_DynamicArray__int()
    vertices.Append(point)
    mesher.AddVertices(vertices)
    assert structure.ElementsOfDomain().Size() == 3
    assert sum(structure.ElementNodes(structure.GetElement(e)).count(point) for e in _elements(structure)) == 3


def test_constructor_reference_argument_reaches_the_constructor():
    """BRepMesh_Delaun(IMeshData::Array1OfVertexOfDelaun&): the result holds the four vertices passed in (and the
    nodes of the auxiliary triangle the algorithm starts from)."""
    corners = NCollection_Array1[BRepMesh_Vertex](1, 4)
    for i, (u, v) in enumerate(((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)), 1):
        corners[i] = BRepMesh_Vertex(u, v, BRepMesh_Free)
    vertices = NCollection_Shared__NCollection_Array1__BRepMesh_Vertex(corners)
    result = BRepMesh_Delaun(vertices).Result()
    nodes = {(round(result.GetNode(i).Coord().X(), 12), round(result.GetNode(i).Coord().Y(), 12))
             for i in range(1, result.NbNodes() + 1)}
    assert {(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)} <= nodes


def test_pointer_argument_takes_the_object_and_none(tmp_path):
    """DumpTriangles(const char*, IMeshData::MapOfInteger*): the triangles of the given map, or all of them for null."""
    structure, element = _triangle_structure()
    tool = BRepMesh_MeshTool(structure)
    empty = NCollection_Shared__NCollection_PackedMap__int()
    one = NCollection_Shared__NCollection_PackedMap__int()
    one.Add(element)
    sizes = {}
    for name, triangles in (("all", None), ("empty", empty), ("one", one)):
        tool.DumpTriangles(str(tmp_path / f"{name}.brep"), triangles)
        sizes[name] = (tmp_path / f"{name}.brep").stat().st_size
    assert sizes["one"] == sizes["all"]          # the structure's only triangle
    assert sizes["empty"] < sizes["one"]         # no triangle at all


def test_reference_argument_refuses_none_and_the_wrapped_class():
    structure, _ = _triangle_structure()
    mesher = BRepMesh_Delaun(structure, 2, 2, True)
    with pytest.raises(TypeError):
        mesher.AddVertices(None)
    plain = NCollection_DynamicArray[int]()          # the wrapped T, not an NCollection_Shared<T>
    plain.Append(0)
    with pytest.raises(TypeError):
        mesher.AddVertices(plain)
