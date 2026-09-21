"""OCCT package BRepTopAdaptor (toolkit TKTopAlgo)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.BRepAdaptor
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.gp


class BRepTopAdaptor_FClass2d:
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, Tol: float) -> None: ...

    def PerformInfinitePoint(self) -> nanoocp.TopAbs.TopAbs_State: ...

    def Perform(self, Puv: nanoocp.gp.gp_Pnt2d, RecadreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State: ...

    def Destroy(self) -> None: ...

    def Copy(self, Other: "BRepTopAdaptor_FClass2d") -> "BRepTopAdaptor_FClass2d": ...

    def TestOnRestriction(self, Puv: nanoocp.gp.gp_Pnt2d, Tol: float, RecadreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State:
        """
        Test a point with +- an offset (Tol) and returns
        On if some points are OUT an some are IN
        (Caution: Internal use. see the code for more details)
        """

class BRepTopAdaptor_HVertex(nanoocp.Adaptor3d.Adaptor3d_HVertex):
    @overload
    def __init__(self, Vtx: nanoocp.TopoDS.TopoDS_Vertex, Curve: nanoocp.BRepAdaptor.BRepAdaptor_Curve2d | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepTopAdaptor_HVertex) -> None: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def ChangeVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Value(self) -> nanoocp.gp.gp_Pnt2d: ...

    def Parameter(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float: ...

    def Resolution(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """Parametric resolution (2d)."""

    def Orientation(self) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    def IsSame(self, Other: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepTopAdaptor_Tool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, Tol2d: float) -> None: ...

    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol2d: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepTopAdaptor_Tool) -> None: ...

    @overload
    def Init(self, F: nanoocp.TopoDS.TopoDS_Face, Tol2d: float) -> None: ...

    @overload
    def Init(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None, Tol2d: float) -> None: ...

    def GetTopolTool(self) -> BRepTopAdaptor_TopolTool: ...

    def SetTopolTool(self, TT: BRepTopAdaptor_TopolTool | None) -> None: ...

    def GetSurface(self) -> nanoocp.Adaptor3d.Adaptor3d_Surface: ...

    def Destroy(self) -> None: ...

class BRepTopAdaptor_TopolTool(nanoocp.Adaptor3d.Adaptor3d_TopolTool):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Surface: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    def __iter__(self) -> BRepTopAdaptor_TopolTool:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """Python addition: see __iter__."""

    @overload
    def Initialize(self) -> None: ...

    @overload
    def Initialize(self, S: nanoocp.Adaptor3d.Adaptor3d_Surface | None) -> None: ...

    @overload
    def Initialize(self, Curve: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> None: ...

    def Init(self) -> None: ...

    def More(self) -> bool: ...

    def Value(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d: ...

    def Next(self) -> None: ...

    def InitVertexIterator(self) -> None: ...

    def MoreVertex(self) -> bool: ...

    def Vertex(self) -> nanoocp.Adaptor3d.Adaptor3d_HVertex: ...

    def NextVertex(self) -> None: ...

    def Classify(self, P2d: nanoocp.gp.gp_Pnt2d, Tol: float, RecadreOnPeriodic: bool = True) -> nanoocp.TopAbs.TopAbs_State: ...

    def IsThePointOn(self, P2d: nanoocp.gp.gp_Pnt2d, Tol: float, RecadreOnPeriodic: bool = True) -> bool:
        """see the code for specifications)"""

    @overload
    def Orientation(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> nanoocp.TopAbs.TopAbs_Orientation: ...

    @overload
    def Orientation(self, C: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        If the function returns the orientation of the arc.
        If the orientation is FORWARD or REVERSED, the arc is
        a "real" limit of the surface.
        If the orientation is INTERNAL or EXTERNAL, the arc is
        considered as an arc on the surface.
        """

    def Destroy(self) -> None: ...

    def Has3d(self) -> bool:
        """
        answers if arcs and vertices may have 3d representations,
        so that we could use Tol3d and Pnt methods.
        """

    @overload
    def Tol3d(self, C: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None) -> float:
        """returns 3d tolerance of the arc C"""

    @overload
    def Tol3d(self, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> float:
        """returns 3d tolerance of the vertex V"""

    def Pnt(self, V: nanoocp.Adaptor3d.Adaptor3d_HVertex | None) -> nanoocp.gp.gp_Pnt:
        """returns 3d point of the vertex V"""

    def ComputeSamplePoints(self) -> None: ...

    def NbSamplesU(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def NbSamplesV(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def NbSamples(self) -> int:
        """compute the sample-points for the intersections algorithms"""

    def SamplePoint(self, Index: int, P2d: nanoocp.gp.gp_Pnt2d, P3d: nanoocp.gp.gp_Pnt) -> None: ...

    def DomainIsInfinite(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.BRepTopAdaptor
import nanoocp.TopTools
BRepTopAdaptor_MapOfShapeTool = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.BRepTopAdaptor.BRepTopAdaptor_Tool, nanoocp.TopTools.TopTools_ShapeMapHasher]
