"""Generated bindings for TKMeshVS (Visualization: MeshVS): OCCT's mesh presentation for AIS -- a `MeshVS_Mesh` is an
`AIS_InteractiveObject` that draws a mesh from a `MeshVS_DataSource`, with per-node and per-element colours, vectors
and text. The drawer, the builders and the sensitive entities are all usable; the data source is not, because OCCT's
only concrete ones live in `Draw` (2d, roadmap 8.5)."""
import importlib
from pathlib import Path

import pytest

from nanoocp.AIS import AIS_InteractiveObject
from nanoocp.MeshVS import (MeshVS_BP_Mesh, MeshVS_Buffer, MeshVS_DMF_Shading, MeshVS_DMF_WireFrame, MeshVS_DataSource,
                            MeshVS_DrawerAttribute, MeshVS_Drawer, MeshVS_EntityType, MeshVS_Mesh, MeshVS_MeshPrsBuilder,
                            MeshVS_SelectionModeFlags, MeshVS_Tool, MeshVS_TwoColors, MeshVS_TwoNodes)
from nanoocp.Quantity import Quantity_Color, Quantity_NOC_BLUE, Quantity_NOC_RED

REPORT = Path(__file__).parents[1] / "src" / "cpp" / "TKMeshVS" / "report.txt"


def test_the_package_imports():
    assert importlib.import_module("nanoocp.MeshVS").__name__ == "nanoocp.MeshVS"


def test_the_drawer_holds_the_four_attribute_kinds():
    """MeshVS_Drawer is the attribute bag every builder reads: colours, doubles, booleans and integers under the
    MeshVS_DrawerAttribute enum. The getters have out-parameters, so they return (found, value) -- R-OUT."""
    drawer = MeshVS_Drawer()
    drawer.SetColor(MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor, Quantity_Color(Quantity_NOC_RED))
    colour = Quantity_Color()
    assert drawer.GetColor(MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor, colour)
    assert colour.Name() == Quantity_NOC_RED

    drawer.SetDouble(MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff, 0.8)
    assert drawer.GetDouble(MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff) == (True, 0.8)

    drawer.SetBoolean(MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes, True)
    assert drawer.GetBoolean(MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes) == (True, True)

    drawer.SetInteger(MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes, 8)
    assert drawer.GetInteger(MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes) == (True, 8)

    assert drawer.GetDouble(MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth)[0] is False   # never set


def test_a_mesh_is_an_ais_object_with_a_drawer():
    mesh = MeshVS_Mesh()
    assert isinstance(mesh, AIS_InteractiveObject)
    assert mesh.DynamicType().Name() == "MeshVS_Mesh"
    assert mesh.GetDataSource() is None                           # nothing to draw yet
    assert mesh.GetDrawer() is not None                           # ... but a drawer from the start

    drawer = MeshVS_Drawer()
    drawer.SetColor(MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor, Quantity_Color(Quantity_NOC_BLUE))
    mesh.SetDrawer(drawer)
    colour = Quantity_Color()
    assert mesh.GetDrawer().GetColor(MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor, colour)
    assert colour.Name() == Quantity_NOC_BLUE


def test_the_data_source_is_the_gap(tmp_path):
    """MeshVS_DataSource has six pure virtuals -- one of them `void* GetAddr(...)`, which has no Python spelling at
    all -- and OCCT's only concrete implementations are XSDRAWSTL_DataSource/DataSource3D in `Draw`, which is out of
    scope (2). So a mesh cannot be fed from Python today: it needs either those Draw classes or a trampoline for the
    abstract base (roadmap 8.5). Everything around it works, which is what the rest of this file shows."""
    with pytest.raises(TypeError):
        MeshVS_DataSource()                                       # abstract: no constructor bound
    assert MeshVS_Mesh().GetDataSource() is None


def test_the_display_and_builder_flags_are_plain_ints():
    """MeshVS_DisplayModeFlags and MeshVS_BuilderPriority are `typedef int` plus an anonymous enum, so their
    enumerators bind as module-level ints -- which is how OCCT uses them, as a bitmask."""
    assert isinstance(MeshVS_DMF_Shading, int) and isinstance(MeshVS_BP_Mesh, int)
    assert MeshVS_DMF_WireFrame | MeshVS_DMF_Shading == 3

    assert [e.name for e in MeshVS_EntityType] == ["MeshVS_ET_NONE", "MeshVS_ET_Node", "MeshVS_ET_0D", "MeshVS_ET_Link",
                                                   "MeshVS_ET_Face", "MeshVS_ET_Volume", "MeshVS_ET_Element", "MeshVS_ET_All"]
    assert MeshVS_SelectionModeFlags.MeshVS_SMF_Node in list(MeshVS_SelectionModeFlags)


def test_the_tool_builds_the_presentation_aspects():
    """MeshVS_Tool turns a drawer into the Graphic3d aspects the builders hand to the presentation."""
    drawer = MeshVS_Drawer()
    drawer.SetColor(MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor, Quantity_Color(Quantity_NOC_RED))
    assert MeshVS_Tool.CreateAspectFillArea3d(drawer) is not None
    assert MeshVS_Tool.CreateAspectLine3d(drawer) is not None
    assert MeshVS_Tool.CreateAspectMarker3d(drawer) is not None
    assert MeshVS_Tool.CreateAspectText3d(drawer) is not None


def test_the_small_value_types():
    nodes = MeshVS_TwoNodes(3, 7)
    assert (nodes.First, nodes.Second) == (3, 7)
    assert [f for f in dir(MeshVS_TwoColors()) if not f.startswith("_")] == ["b1", "b2", "g1", "g2", "r1", "r2"]


def test_the_buffer_converts_to_float_and_int():
    """MeshVS_Buffer's `operator double&()` and `operator int&()` are **non-const**, which is what forced
    R-CONV-SCALAR to carry the operator's constness into the emitted lambda (2026-09-23)."""
    buffer = MeshVS_Buffer(64)
    assert isinstance(float(buffer), float) and isinstance(int(buffer), int)


def test_report_is_six_lines():
    """All six are `void*`: MeshVS_DataSource hands out raw addresses for the application's own mesh objects
    (`GetAddr`, `GetGroupAddr`, `MeshVS_MeshEntityOwner::Owner`) and MeshVS_Buffer casts itself to one."""
    lines = [line for line in REPORT.read_text().splitlines() if not line.startswith("#")]
    assert len(lines) == 6
    assert all("void pointer" in line or "operator void *" in line for line in lines)
