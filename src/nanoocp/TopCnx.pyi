"""OCCT package TopCnx (toolkit TKHLR)"""

from typing import overload

import nanoocp.TopAbs
import nanoocp.gp


class TopCnx_EdgeFaceTransition:
    """
    TheEdgeFaceTransition is an algorithm to compute
    the cumulated transition for interferences on an
    edge.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty algorithm."""

    @overload
    def __init__(self, theOther: TopCnx_EdgeFaceTransition) -> None: ...

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir, Curv: float) -> None:
        """
        Initialize the algorithm with the local
        description of the edge.
        """

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir) -> None:
        """Initialize the algorithm with a linear Edge."""

    def AddInterference(self, Tole: float, Tang: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir, Curv: float, Or: nanoocp.TopAbs.TopAbs_Orientation, Tr: nanoocp.TopAbs.TopAbs_Orientation, BTr: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Add a curve element to the boundary. Or is the
        orientation of the interference on the boundary
        curve. Tr is the transition of the interference.
        BTr is the boundary transition of the
        interference.
        """

    def Transition(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the current cumulated transition."""

    def BoundaryTransition(self) -> nanoocp.TopAbs.TopAbs_Orientation:
        """Returns the current cumulated BoundaryTransition."""
