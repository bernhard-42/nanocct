"""OCCT package HelixBRep (toolkit TKHelix)"""

from typing import overload

import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.TopoDS
import nanoocp.gp


class HelixBRep_BuilderHelix:
    """
    Implementation of building helix wire
    Values of Error Status returned by algo:
    0 - OK
    1 - object is just initialized, it means that no input parameters were set
    2 - approximation fails

    10 - R < tolerance - starting point is too close to axis
    11 - step (Pitch) < tolerance
    12 - Height < tolerance
    13 - TaperAngle < 0 or TaperAngle > Pi/2 - TolAng
    Warning Status:
    0 - OK
    1 - tolerance reached by approximation > requested tolerance.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: HelixBRep_BuilderHelix) -> None: ...

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiams: nanoocp.NCollection.NCollection_Array1[float], theHeights: nanoocp.NCollection.NCollection_Array1[float], thePitches: nanoocp.NCollection.NCollection_Array1[float], theIsPitches: nanoocp.NCollection.NCollection_Array1[bool]) -> None: ...

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiam: float, theHeights: nanoocp.NCollection.NCollection_Array1[float], thePitches: nanoocp.NCollection.NCollection_Array1[float], theIsPitches: nanoocp.NCollection.NCollection_Array1[bool]) -> None: ...

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiam1: float, theDiam2: float, theHeights: nanoocp.NCollection.NCollection_Array1[float], thePitches: nanoocp.NCollection.NCollection_Array1[float], theIsPitches: nanoocp.NCollection.NCollection_Array1[bool]) -> None: ...

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiams: nanoocp.NCollection.NCollection_Array1[float], thePitches: nanoocp.NCollection.NCollection_Array1[float], theNbTurns: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Sets parameters of general composite helix"""

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiam: float, thePitches: nanoocp.NCollection.NCollection_Array1[float], theNbTurns: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Sets parameters of pure helix"""

    @overload
    def SetParameters(self, theAxis: nanoocp.gp.gp_Ax3, theDiam1: float, theDiam2: float, thePitches: nanoocp.NCollection.NCollection_Array1[float], theNbTurns: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Sets parameters of pure spiral"""

    def SetApproxParameters(self, theTolerance: float, theMaxDegree: int, theContinuity: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets parameters for approximation"""

    def Perform(self) -> None:
        """Performs calculations"""

    def ToleranceReached(self) -> float:
        """Gets tolerance reached by approximation"""

    def ErrorStatus(self) -> int:
        """Returns error status of algorithm"""

    def WarningStatus(self) -> int:
        """Returns warning status of algorithm"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gets result of algorithm"""
