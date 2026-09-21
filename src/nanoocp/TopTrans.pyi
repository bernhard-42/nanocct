"""OCCT package TopTrans (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.TopAbs
import nanoocp.gp


class TopTrans_CurveTransition:
    """
    This algorithm is used to compute the transition
    of a Curve intersecting a curvilinear boundary.

    The geometric elements are described locally at
    the intersection point by a second order
    development.

    The curve is described by the intersection point,
    the tangent vector and the curvature.

    The boundary is described by a set of curve
    elements, a curve element is either :

    - A curve.

    - A curve and an orientation called a half-curve,
    the boundary of the curve is before or after the
    intersection point depending on the orientation.
    """

    @overload
    def __init__(self) -> None:
        """Create an empty Curve Transition."""

    @overload
    def __init__(self, theOther: TopTrans_CurveTransition) -> None: ...

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir, Curv: float) -> None:
        """
        Initialize a Transition with the local description
        of a Curve.
        """

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir) -> None:
        """Initialize a Transition with the local description of a straight line."""

    def Compare(self, Tole: float, Tang: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir, Curv: float, S: nanoocp.TopAbs.TopAbs_Orientation, Or: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Add a curve element to the boundary. If Or is
        REVERSED the curve is before the intersection,
        else if Or is FORWARD the curv is after the
        intersection and if Or is INTERNAL the
        intersection is in the middle of the curv.
        """

    def StateBefore(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        returns the state of the curve before the
        intersection, this is the position relative to the
        boundary of a point very close to the intersection
        on the negative side of the tangent.
        """

    def StateAfter(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        returns the state of the curve after the
        intersection, this is the position relative to the
        boundary of a point very close to the intersection
        on the positive side of the tangent.
        """

class TopTrans_SurfaceTransition:
    """
    This algorithm is used to compute the transition
    of a 3D surface intersecting a topological surfacic
    boundary on a 3D curve ( intersection curve ).
    The boundary is described by a set of faces
    each face is described by
    - its support surface,
    - an orientation defining its matter side.
    The geometric elements are described locally at the
    intersection point by a second order development.
    A surface is described by the normal vector, the
    principal directions and the principal curvatures.
    A curve is described by the tangent, the normal
    and the curvature.
    The algorithm keeps track of the two faces elements
    closest to the part of the curve "before" and "after"
    the intersection, these two elements are updated
    for each new face.
    The position of the curve can be computed when at
    least one surface element has been given, this
    position is "In","Out" or "On" for the part of the
    curve "Before" or "After" the intersection.
    """

    @overload
    def __init__(self) -> None:
        """Create an empty Surface Transition."""

    @overload
    def __init__(self, theOther: TopTrans_SurfaceTransition) -> None: ...

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir, MaxD: nanoocp.gp.gp_Dir, MinD: nanoocp.gp.gp_Dir, MaxCurv: float, MinCurv: float) -> None:
        """
        Initialize a Surface Transition with the local
        description of the intersection curve and of the
        reference surface.
        PREQUESITORY : Norm oriented OUTSIDE "geometric matter\"
        """

    @overload
    def Reset(self, Tgt: nanoocp.gp.gp_Dir, Norm: nanoocp.gp.gp_Dir) -> None:
        """
        Initialize a Surface Transition with the local
        description of a straight line.
        """

    @overload
    def Compare(self, Tole: float, Norm: nanoocp.gp.gp_Dir, MaxD: nanoocp.gp.gp_Dir, MinD: nanoocp.gp.gp_Dir, MaxCurv: float, MinCurv: float, S: nanoocp.TopAbs.TopAbs_Orientation, O: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Add a face element to the boundary.

        - S defines topological orientation for the face :
        S FORWARD means: along the intersection curve on the
        reference surface, transition states while crossing
        the face are OUT,IN.
        S REVERSED means states are IN,OUT.
        S INTERNAL means states are IN,IN.

        - O defines curve's position on face :
        O FORWARD means the face is before the intersection
        O REVERSED means the face is AFTER
        O INTERNAL means the curve intersection is in the face.
        PREQUESITORY : Norm oriented OUTSIDE "geometric matter\"
        """

    @overload
    def Compare(self, Tole: float, Norm: nanoocp.gp.gp_Dir, S: nanoocp.TopAbs.TopAbs_Orientation, O: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """Add a plane or a cylindric face to the boundary."""

    def StateBefore(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the state of the reference surface before
        the interference, this is the position relative to
        the surface of a point very close to the intersection
        on the negative side of the tangent.
        """

    def StateAfter(self) -> nanoocp.TopAbs.TopAbs_State:
        """
        Returns the state of the reference surface after
        interference, this is the position relative to the
        surface of a point very close to the intersection
        on the positive side of the tangent.
        """

    @staticmethod
    def GetBefore(Tran: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopAbs.TopAbs_State: ...

    @staticmethod
    def GetAfter(Tran: nanoocp.TopAbs.TopAbs_Orientation) -> nanoocp.TopAbs.TopAbs_State: ...
