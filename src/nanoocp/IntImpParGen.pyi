"""OCCT package IntImpParGen (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.IntRes2d
import nanoocp.gp


class IntImpParGen:
    """
    Gives a generic algorithm to intersect Implicit Curves
    and Bounded Parametric Curves.

    Level: Internal

    All the methods of all the classes are Internal.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntImpParGen) -> None: ...

    @overload
    @staticmethod
    def DetermineTransition(Pos1: nanoocp.IntRes2d.IntRes2d_Position, Tan1: nanoocp.gp.gp_Vec2d, Norm1: nanoocp.gp.gp_Vec2d, Trans1: nanoocp.IntRes2d.IntRes2d_Transition, Pos2: nanoocp.IntRes2d.IntRes2d_Position, Tan2: nanoocp.gp.gp_Vec2d, Norm2: nanoocp.gp.gp_Vec2d, Trans2: nanoocp.IntRes2d.IntRes2d_Transition, Tol: float) -> None:
        """
        Template class for an implicit curve.
        Math function, instantiated inside the Intersector.
        Tool used by the package IntCurve and IntImpParGen
        """

    @overload
    @staticmethod
    def DetermineTransition(Pos1: nanoocp.IntRes2d.IntRes2d_Position, Tan1: nanoocp.gp.gp_Vec2d, Trans1: nanoocp.IntRes2d.IntRes2d_Transition, Pos2: nanoocp.IntRes2d.IntRes2d_Position, Tan2: nanoocp.gp.gp_Vec2d, Trans2: nanoocp.IntRes2d.IntRes2d_Transition, Tol: float) -> bool: ...

    @staticmethod
    def DeterminePosition(Dom1: nanoocp.IntRes2d.IntRes2d_Domain, P1: nanoocp.gp.gp_Pnt2d, Tol: float) -> nanoocp.IntRes2d.IntRes2d_Position: ...

    @staticmethod
    def NormalizeOnDomain(Dom1: nanoocp.IntRes2d.IntRes2d_Domain) -> tuple[float, float]: ...

class IntImpParGen_ImpTool:
    """Template class for an implicit curve."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IntImpParGen_ImpTool) -> None: ...

def NormalizeOnDomain(arg1: nanoocp.IntRes2d.IntRes2d_Domain) -> tuple[float, float]: ...

def Determine_Position(arg1: nanoocp.IntRes2d.IntRes2d_Domain, arg2: nanoocp.gp.gp_Pnt2d, arg3: float) -> nanoocp.IntRes2d.IntRes2d_Position: ...

def Determine_Transition(Pos1: nanoocp.IntRes2d.IntRes2d_Position, Tan1: nanoocp.gp.gp_Vec2d, Norm1: nanoocp.gp.gp_Vec2d, Trans1: nanoocp.IntRes2d.IntRes2d_Transition, Pos2: nanoocp.IntRes2d.IntRes2d_Position, Tan2: nanoocp.gp.gp_Vec2d, Norm2: nanoocp.gp.gp_Vec2d, Trans2: nanoocp.IntRes2d.IntRes2d_Transition, ToleranceAng: float) -> None: ...
