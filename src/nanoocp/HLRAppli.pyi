"""OCCT package HLRAppli (toolkit TKHLR)"""

from typing import overload

import nanoocp.HLRBRep
import nanoocp.TopoDS


class HLRAppli_ReflectLines:
    """
    This class builds reflect lines on a shape
    according to the axes of view defined by user.
    Reflect lines are represented by edges in 3d.
    """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: HLRAppli_ReflectLines) -> None: ...

    def SetAxes(self, Nx: float, Ny: float, Nz: float, XAt: float, YAt: float, ZAt: float, XUp: float, YUp: float, ZUp: float) -> None:
        """
        Sets the normal to the plane of visualisation,
        the coordinates of the view point and
        the coordinates of the vertical direction vector.
        """

    def Perform(self) -> None: ...

    def GetResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns resulting compound of reflect lines
        represented by edges in 3d
        """

    def GetCompoundOf3dEdges(self, type: nanoocp.HLRBRep.HLRBRep_TypeOfResultingEdge, visible: bool, In3d: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        returns resulting compound of lines
        of specified type and visibility
        represented by edges in 3d or 2d
        """
