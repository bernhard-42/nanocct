"""OCCT package AppCont (toolkit TKGeomBase)"""

from typing import overload

import nanoocp.AppParCurves
import nanoocp.NCollection
import nanoocp.gp


class AppCont_Function:
    """
    Class describing a continuous 3d and/or function f(u).
    This class must be provided by the user to use the approximation algorithm FittingCurve.
    """

    def GetNumberOfPoints(self) -> tuple[int, int]:
        """Get number of 3d and 2d points returned by "Value" and "D1" functions."""

    def GetNbOf3dPoints(self) -> int:
        """Get number of 3d points returned by "Value" and "D1" functions."""

    def GetNbOf2dPoints(self) -> int:
        """Get number of 2d points returned by "Value" and "D1" functions."""

    def FirstParameter(self) -> float:
        """Returns the first parameter of the function."""

    def LastParameter(self) -> float:
        """Returns the last parameter of the function."""

    def Value(self, theU: float, thePnt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], thePnt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> bool:
        """Returns the point at parameter <theU>."""

    def D1(self, theU: float, theVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], theVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """Returns the derivative at parameter <theU>."""

    def PeriodInformation(self, arg0: int) -> tuple[bool, float]:
        """
        Return information about peridicity in output paramateters space.
        @param theDimIdx Defines index in output parameters space. 1 <= theDimIdx <= 3 * myNbPnt + 2 *
        myNbPnt2d.
        """

class PeriodicityInfo:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: PeriodicityInfo) -> None: ...

    @property
    def isPeriodic(self) -> bool: ...

    @isPeriodic.setter
    def isPeriodic(self, arg: bool, /) -> None: ...

    @property
    def myPeriod(self) -> float: ...

    @myPeriod.setter
    def myPeriod(self, arg: float, /) -> None: ...

class AppCont_LeastSquare:
    @overload
    def __init__(self, SSP: AppCont_Function, U0: float, U1: float, FirstCons: nanoocp.AppParCurves.AppParCurves_Constraint, LastCons: nanoocp.AppParCurves.AppParCurves_Constraint, Deg: int, NbPoints: int) -> None: ...

    @overload
    def __init__(self, theOther: AppCont_LeastSquare) -> None: ...

    def Value(self) -> nanoocp.AppParCurves.AppParCurves_MultiCurve: ...

    def Error(self) -> tuple[float, float, float]: ...

    def IsDone(self) -> bool: ...
