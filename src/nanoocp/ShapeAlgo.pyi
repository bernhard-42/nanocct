"""OCCT package ShapeAlgo (toolkit TKShHealing)"""

from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.ShapeAnalysis
import nanoocp.ShapeExtend
import nanoocp.ShapeFix
import nanoocp.Standard
import nanoocp.TopoDS


class ShapeAlgo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeAlgo) -> None: ...

    @staticmethod
    def Init() -> None:
        """
        Provides initerface to the algorithms from Shape Healing.
        Creates and initializes default AlgoContainer.
        """

    @staticmethod
    def SetAlgoContainer(aContainer: ShapeAlgo_AlgoContainer | None) -> None:
        """Sets default AlgoContainer"""

    @staticmethod
    def AlgoContainer() -> ShapeAlgo_AlgoContainer:
        """Returns default AlgoContainer"""

class ShapeAlgo_AlgoContainer(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeAlgo_AlgoContainer) -> None: ...

    def SetToolContainer(self, TC: ShapeAlgo_ToolContainer | None) -> None:
        """Sets ToolContainer"""

    def ToolContainer(self) -> ShapeAlgo_ToolContainer:
        """Returns ToolContainer"""

    def ConnectNextWire(self, saw: nanoocp.ShapeAnalysis.ShapeAnalysis_Wire | None, nextsewd: nanoocp.ShapeExtend.ShapeExtend_WireData | None, maxtol: float) -> tuple[bool, float, bool, bool]:
        """
        Finds the best way to connect and connects <nextsewd> to already
        built <sewd> (in <saw>).
        Returns False if <nextsewd> cannot be connected, otherwise - True.
        <maxtol> specifies the maximum tolerance with which <nextsewd> can
        be added.
        <distmin> is used to receive the minimum distance between <nextsewd>
        and <sewd>.
        <revsewd>   is True if <sewd>     has been reversed before connecting.
        <revnextwd> is True if <nextsewd> has been reversed before connecting.
        Uses functionality of ShapeAnalysis_Wire.
        """

    @overload
    def ApproxBSplineCurve(self, bspline: nanoocp.Geom.Geom_BSplineCurve | None, seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom.Geom_Curve]) -> None: ...

    @overload
    def ApproxBSplineCurve(self, bspline: nanoocp.Geom2d.Geom2d_BSplineCurve | None, seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.Geom2d.Geom2d_Curve]) -> None: ...

    @overload
    def C0BSplineToSequenceOfC1BSplineCurve(self, BS: nanoocp.Geom.Geom_BSplineCurve | None) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Geom.Geom_BoundedCurve]]: ...

    @overload
    def C0BSplineToSequenceOfC1BSplineCurve(self, BS: nanoocp.Geom2d.Geom2d_BSplineCurve | None) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Geom2d.Geom2d_BoundedCurve]]:
        """
        Converts C0 B-Spline curve into sequence of C1 B-Spline curves.
        Calls ShapeUpgrade::C0BSplineToSequenceOfC1BSplineCurve.
        """

    def C0ShapeToC1Shape(self, shape: nanoocp.TopoDS.TopoDS_Shape, tol: float) -> nanoocp.TopoDS.TopoDS_Shape:
        """Converts a shape on C0 geometry into the shape on C1 geometry."""

    def ConvertSurfaceToBSpline(self, surf: nanoocp.Geom.Geom_Surface | None, UF: float, UL: float, VF: float, VL: float) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Converts a surface to B-Spline.
        Uses ShapeConstruct.
        """

    def HomoWires(self, wireIn1: nanoocp.TopoDS.TopoDS_Wire, wireIn2: nanoocp.TopoDS.TopoDS_Wire, wireOut1: nanoocp.TopoDS.TopoDS_Wire, wireOut2: nanoocp.TopoDS.TopoDS_Wire, byParam: bool) -> bool:
        """
        Return 2 wires with the same number of edges. The both Edges
        number i of these wires have got the same ratio between
        theirs parameter lengths and their wire parameter lengths.
        """

    def OuterWire(self, face: nanoocp.TopoDS.TopoDS_Face) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the outer wire on the face <Face>."""

    def ConvertToPeriodic(self, surf: nanoocp.Geom.Geom_Surface | None) -> nanoocp.Geom.Geom_Surface:
        """
        Converts surface to periodic form.
        Calls ShapeCustom_Surface.
        """

    def GetFaceUVBounds(self, F: nanoocp.TopoDS.TopoDS_Face) -> tuple[float, float, float, float]:
        """Computes exact UV bounds of all wires on the face"""

    def ConvertCurveToBSpline(self, C3D: nanoocp.Geom.Geom_Curve | None, First: float, Last: float, Tol3d: float, Continuity: nanoocp.GeomAbs.GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> nanoocp.Geom.Geom_BSplineCurve:
        """Convert Geom_Curve to Geom_BSplineCurve"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeAlgo_ToolContainer(nanoocp.Standard.Standard_Transient):
    """Returns tools used by AlgoContainer"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeAlgo_ToolContainer) -> None: ...

    def FixShape(self) -> nanoocp.ShapeFix.ShapeFix_Shape:
        """Returns ShapeFix_Shape"""

    def EdgeProjAux(self) -> nanoocp.ShapeFix.ShapeFix_EdgeProjAux:
        """Returns ShapeFix_EdgeProjAux"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
