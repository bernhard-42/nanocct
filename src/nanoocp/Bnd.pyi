"""OCCT package Bnd (toolkit TKMath)"""

from collections.abc import Sequence
import enum
from typing import TextIO, overload

import nanoocp.NCollection
import nanoocp.gp


class Bnd_B2d:
    """
    Template class for 2D bounding box.
    This is a base template that is instantiated for double and float.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_XY, theHSize: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def __init__(self, theCenter: Sequence[float], theHSize: Sequence[float]) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Bnd_B2d) -> None: ...

    def IsVoid(self) -> bool:
        """Returns True if the box is void (non-initialized)."""

    def Clear(self) -> None:
        """Reset the box data."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """Update the box by a point."""

    @overload
    def Add(self, theBox: Bnd_B2d) -> None:
        """Update the box by another box."""

    def CornerMin(self) -> nanoocp.gp.gp_XY:
        """
        Query a box corner: (Center - HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def CornerMax(self) -> nanoocp.gp.gp_XY:
        """
        Query a box corner: (Center + HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def SquareExtent(self) -> float:
        """
        Query the square diagonal. If the box is VOID (see method IsVoid())
        then a very big real value is returned.
        """

    def Enlarge(self, theDiff: float) -> None:
        """Extend the Box by the absolute value of theDiff."""

    def Limit(self, theOtherBox: Bnd_B2d) -> bool:
        """
        Limit the Box by the internals of theOtherBox.
        Returns True if the limitation takes place, otherwise False
        indicating that the boxes do not intersect.
        """

    def Transformed(self, theTrsf: nanoocp.gp.gp_Trsf2d) -> Bnd_B2d:
        """
        Transform the bounding box with the given transformation.
        The resulting box will be larger if theTrsf contains rotation.
        """

    @overload
    def IsOut(self, thePnt: nanoocp.gp.gp_XY) -> bool:
        """
        Check the given point for the inclusion in the Box.
        Returns True if the point is outside.
        """

    @overload
    def IsOut(self, theCenter: nanoocp.gp.gp_XY, theRadius: float, isCircleHollow: bool = False) -> bool:
        """
        Check a circle for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B2d) -> bool:
        """
        Check the given box for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B2d, theTrsf: nanoocp.gp.gp_Trsf2d) -> bool:
        """
        Check the given box oriented by the given transformation
        for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theLine: nanoocp.gp.gp_Ax2d) -> bool:
        """
        Check the given Line for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsOut(self, theP0: nanoocp.gp.gp_XY, theP1: nanoocp.gp.gp_XY) -> bool:
        """
        Check the Segment defined by the couple of input points
        for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsIn(self, theBox: Bnd_B2d) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns
        True if 'this' box is fully inside 'theBox'.
        """

    @overload
    def IsIn(self, theBox: Bnd_B2d, theTrsf: nanoocp.gp.gp_Trsf2d) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'
        transformed by 'theTrsf'. Returns True if 'this' box is fully
        inside the transformed 'theBox'.
        """

    @overload
    def SetCenter(self, theCenter: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def SetCenter(self, theCenter: Sequence[float]) -> None:
        """Set the Center coordinates"""

    @overload
    def SetHSize(self, theHSize: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def SetHSize(self, theHSize: Sequence[float]) -> None:
        """
        Set the HSize (half-diagonal) coordinates.
        All components of theHSize must be non-negative.
        """

    def Center(self) -> list[float]:
        """Get the Center coordinates"""

    def HSize(self) -> list[float]:
        """Get the HSize (half-diagonal) coordinates"""

class Bnd_B2f:
    """
    Template class for 2D bounding box.
    This is a base template that is instantiated for double and float.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_XY, theHSize: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def __init__(self, theCenter: Sequence[float], theHSize: Sequence[float]) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Bnd_B2f) -> None: ...

    def IsVoid(self) -> bool:
        """Returns True if the box is void (non-initialized)."""

    def Clear(self) -> None:
        """Reset the box data."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """Update the box by a point."""

    @overload
    def Add(self, theBox: Bnd_B2f) -> None:
        """Update the box by another box."""

    def CornerMin(self) -> nanoocp.gp.gp_XY:
        """
        Query a box corner: (Center - HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def CornerMax(self) -> nanoocp.gp.gp_XY:
        """
        Query a box corner: (Center + HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def SquareExtent(self) -> float:
        """
        Query the square diagonal. If the box is VOID (see method IsVoid())
        then a very big real value is returned.
        """

    def Enlarge(self, theDiff: float) -> None:
        """Extend the Box by the absolute value of theDiff."""

    def Limit(self, theOtherBox: Bnd_B2f) -> bool:
        """
        Limit the Box by the internals of theOtherBox.
        Returns True if the limitation takes place, otherwise False
        indicating that the boxes do not intersect.
        """

    def Transformed(self, theTrsf: nanoocp.gp.gp_Trsf2d) -> Bnd_B2f:
        """
        Transform the bounding box with the given transformation.
        The resulting box will be larger if theTrsf contains rotation.
        """

    @overload
    def IsOut(self, thePnt: nanoocp.gp.gp_XY) -> bool:
        """
        Check the given point for the inclusion in the Box.
        Returns True if the point is outside.
        """

    @overload
    def IsOut(self, theCenter: nanoocp.gp.gp_XY, theRadius: float, isCircleHollow: bool = False) -> bool:
        """
        Check a circle for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B2f) -> bool:
        """
        Check the given box for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B2f, theTrsf: nanoocp.gp.gp_Trsf2d) -> bool:
        """
        Check the given box oriented by the given transformation
        for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theLine: nanoocp.gp.gp_Ax2d) -> bool:
        """
        Check the given Line for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsOut(self, theP0: nanoocp.gp.gp_XY, theP1: nanoocp.gp.gp_XY) -> bool:
        """
        Check the Segment defined by the couple of input points
        for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsIn(self, theBox: Bnd_B2f) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns
        True if 'this' box is fully inside 'theBox'.
        """

    @overload
    def IsIn(self, theBox: Bnd_B2f, theTrsf: nanoocp.gp.gp_Trsf2d) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'
        transformed by 'theTrsf'. Returns True if 'this' box is fully
        inside the transformed 'theBox'.
        """

    @overload
    def SetCenter(self, theCenter: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def SetCenter(self, theCenter: Sequence[float]) -> None:
        """Set the Center coordinates"""

    @overload
    def SetHSize(self, theHSize: nanoocp.gp.gp_XY) -> None: ...

    @overload
    def SetHSize(self, theHSize: Sequence[float]) -> None:
        """
        Set the HSize (half-diagonal) coordinates.
        All components of theHSize must be non-negative.
        """

    def Center(self) -> list[float]:
        """Get the Center coordinates"""

    def HSize(self) -> list[float]:
        """Get the HSize (half-diagonal) coordinates"""

class Bnd_B3d:
    """
    Template class for 3D bounding box.
    This is a base template that is instantiated for double and float.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_XYZ, theHSize: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def __init__(self, theCenter: Sequence[float], theHSize: Sequence[float]) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Bnd_B3d) -> None: ...

    def IsVoid(self) -> bool:
        """Returns True if the box is void (non-initialized)."""

    def Clear(self) -> None:
        """Reset the box data."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Update the box by a point."""

    @overload
    def Add(self, theBox: Bnd_B3d) -> None:
        """Update the box by another box."""

    def CornerMin(self) -> nanoocp.gp.gp_XYZ:
        """
        Query the lower corner: (Center - HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def CornerMax(self) -> nanoocp.gp.gp_XYZ:
        """
        Query the upper corner: (Center + HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def SquareExtent(self) -> float:
        """
        Query the square diagonal. If the box is VOID (see method IsVoid())
        then a very big real value is returned.
        """

    def Enlarge(self, theDiff: float) -> None:
        """Extend the Box by the absolute value of theDiff."""

    def Limit(self, theOtherBox: Bnd_B3d) -> bool:
        """
        Limit the Box by the internals of theOtherBox.
        Returns True if the limitation takes place, otherwise False
        indicating that the boxes do not intersect.
        """

    def Transformed(self, theTrsf: nanoocp.gp.gp_Trsf) -> Bnd_B3d:
        """
        Transform the bounding box with the given transformation.
        The resulting box will be larger if theTrsf contains rotation.
        """

    @overload
    def IsOut(self, thePnt: nanoocp.gp.gp_XYZ) -> bool:
        """
        Check the given point for the inclusion in the Box.
        Returns True if the point is outside.
        """

    @overload
    def IsOut(self, theCenter: nanoocp.gp.gp_XYZ, theRadius: float, isSphereHollow: bool = False) -> bool:
        """
        Check a sphere for the intersection with the current box.
        Returns True if there is no intersection between boxes. If the
        parameter 'IsSphereHollow' is True, then the intersection is not
        reported for a box that is completely inside the sphere (otherwise
        this method would report an intersection).
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B3d) -> bool:
        """
        Check the given box for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B3d, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Check the given box oriented by the given transformation
        for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theLine: nanoocp.gp.gp_Ax1, isRay: bool = False, theOverthickness: float = 0.0) -> bool:
        """
        Check the given Line for the intersection with the current box.
        Returns True if there is no intersection.
        isRay==True means intersection check with the positive half-line
        theOverthickness is the addition to the size of the current box
        (may be negative). If positive, it can be treated as the thickness
        of the line 'theLine' or the radius of the cylinder along 'theLine'
        """

    @overload
    def IsOut(self, thePlane: nanoocp.gp.gp_Ax3) -> bool:
        """
        Check the given Plane for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsIn(self, theBox: Bnd_B3d) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns
        True if 'this' box is fully inside 'theBox'.
        """

    @overload
    def IsIn(self, theBox: Bnd_B3d, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'
        transformed by 'theTrsf'. Returns True if 'this' box is fully
        inside the transformed 'theBox'.
        """

    @overload
    def SetCenter(self, theCenter: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def SetCenter(self, theCenter: Sequence[float]) -> None:
        """Set the Center coordinates"""

    @overload
    def SetHSize(self, theHSize: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def SetHSize(self, theHSize: Sequence[float]) -> None:
        """
        Set the HSize (half-diagonal) coordinates.
        All components of theHSize must be non-negative.
        """

    def Center(self) -> list[float]:
        """Get the Center coordinates"""

    def HSize(self) -> list[float]:
        """Get the HSize (half-diagonal) coordinates"""

class Bnd_B3f:
    """
    Template class for 3D bounding box.
    This is a base template that is instantiated for double and float.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_XYZ, theHSize: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def __init__(self, theCenter: Sequence[float], theHSize: Sequence[float]) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Bnd_B3f) -> None: ...

    def IsVoid(self) -> bool:
        """Returns True if the box is void (non-initialized)."""

    def Clear(self) -> None:
        """Reset the box data."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Update the box by a point."""

    @overload
    def Add(self, theBox: Bnd_B3f) -> None:
        """Update the box by another box."""

    def CornerMin(self) -> nanoocp.gp.gp_XYZ:
        """
        Query the lower corner: (Center - HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def CornerMax(self) -> nanoocp.gp.gp_XYZ:
        """
        Query the upper corner: (Center + HSize). You must make sure that
        the box is NOT VOID (see IsVoid()), otherwise the method returns
        irrelevant result.
        """

    def SquareExtent(self) -> float:
        """
        Query the square diagonal. If the box is VOID (see method IsVoid())
        then a very big real value is returned.
        """

    def Enlarge(self, theDiff: float) -> None:
        """Extend the Box by the absolute value of theDiff."""

    def Limit(self, theOtherBox: Bnd_B3f) -> bool:
        """
        Limit the Box by the internals of theOtherBox.
        Returns True if the limitation takes place, otherwise False
        indicating that the boxes do not intersect.
        """

    def Transformed(self, theTrsf: nanoocp.gp.gp_Trsf) -> Bnd_B3f:
        """
        Transform the bounding box with the given transformation.
        The resulting box will be larger if theTrsf contains rotation.
        """

    @overload
    def IsOut(self, thePnt: nanoocp.gp.gp_XYZ) -> bool:
        """
        Check the given point for the inclusion in the Box.
        Returns True if the point is outside.
        """

    @overload
    def IsOut(self, theCenter: nanoocp.gp.gp_XYZ, theRadius: float, isSphereHollow: bool = False) -> bool:
        """
        Check a sphere for the intersection with the current box.
        Returns True if there is no intersection between boxes. If the
        parameter 'IsSphereHollow' is True, then the intersection is not
        reported for a box that is completely inside the sphere (otherwise
        this method would report an intersection).
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B3f) -> bool:
        """
        Check the given box for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theOtherBox: Bnd_B3f, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Check the given box oriented by the given transformation
        for the intersection with the current box.
        Returns True if there is no intersection between boxes.
        """

    @overload
    def IsOut(self, theLine: nanoocp.gp.gp_Ax1, isRay: bool = False, theOverthickness: float = 0.0) -> bool:
        """
        Check the given Line for the intersection with the current box.
        Returns True if there is no intersection.
        isRay==True means intersection check with the positive half-line
        theOverthickness is the addition to the size of the current box
        (may be negative). If positive, it can be treated as the thickness
        of the line 'theLine' or the radius of the cylinder along 'theLine'
        """

    @overload
    def IsOut(self, thePlane: nanoocp.gp.gp_Ax3) -> bool:
        """
        Check the given Plane for the intersection with the current box.
        Returns True if there is no intersection.
        """

    @overload
    def IsIn(self, theBox: Bnd_B3f) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'. Returns
        True if 'this' box is fully inside 'theBox'.
        """

    @overload
    def IsIn(self, theBox: Bnd_B3f, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Check that the box 'this' is inside the given box 'theBox'
        transformed by 'theTrsf'. Returns True if 'this' box is fully
        inside the transformed 'theBox'.
        """

    @overload
    def SetCenter(self, theCenter: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def SetCenter(self, theCenter: Sequence[float]) -> None:
        """Set the Center coordinates"""

    @overload
    def SetHSize(self, theHSize: nanoocp.gp.gp_XYZ) -> None: ...

    @overload
    def SetHSize(self, theHSize: Sequence[float]) -> None:
        """
        Set the HSize (half-diagonal) coordinates.
        All components of theHSize must be non-negative.
        """

    def Center(self) -> list[float]:
        """Get the Center coordinates"""

    def HSize(self) -> list[float]:
        """Get the HSize (half-diagonal) coordinates"""

class Bnd_Box:
    """
    Describes a bounding box in 3D space.
    A bounding box is parallel to the axes of the coordinates
    system. If it is finite, it is defined by the three intervals:
    -   [ Xmin,Xmax ],
    -   [ Ymin,Ymax ],
    -   [ Zmin,Zmax ].
    A bounding box may be infinite (i.e. open) in one or more
    directions. It is said to be:
    -   OpenXmin if it is infinite on the negative side of the   "X Direction";
    -   OpenXmax if it is infinite on the positive side of the "X Direction";
    -   OpenYmin if it is infinite on the negative side of the   "Y Direction";
    -   OpenYmax if it is infinite on the positive side of the "Y Direction";
    -   OpenZmin if it is infinite on the negative side of the   "Z Direction";
    -   OpenZmax if it is infinite on the positive side of the "Z Direction";
    -   WholeSpace if it is infinite in all six directions. In this
    case, any point of the space is inside the box;
    -   Void if it is empty. In this case, there is no point included in the box.
    A bounding box is defined by:
    -   six bounds (Xmin, Xmax, Ymin, Ymax, Zmin and
    Zmax) which limit the bounding box if it is finite,
    -   eight flags (OpenXmin, OpenXmax, OpenYmin,
    OpenYmax, OpenZmin, OpenZmax,
    WholeSpace and Void) which describe the
    bounding box if it is infinite or empty, and
    -   a gap, which is included on both sides in any direction
    when consulting the finite bounds of the box.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty Box.
        The constructed box is qualified Void. Its gap is null.
        """

    @overload
    def __init__(self, theMin: nanoocp.gp.gp_Pnt, theMax: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a bounding box, it contains:
        -   minimum/maximum point of bounding box,
        The constructed box is qualified Void. Its gap is null.
        """

    @overload
    def __init__(self, theOther: Bnd_Box) -> None: ...

    class Limits:
        """
        Structure containing the box limits (Xmin, Xmax, Ymin, Ymax, Zmin, Zmax).
        The values include the gap and account for open directions.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: Bnd_Box.Limits) -> None: ...

        @property
        def Xmin(self) -> float:
            """Minimum X coordinate"""

        @Xmin.setter
        def Xmin(self, arg: float, /) -> None: ...

        @property
        def Xmax(self) -> float:
            """Maximum X coordinate"""

        @Xmax.setter
        def Xmax(self, arg: float, /) -> None: ...

        @property
        def Ymin(self) -> float:
            """Minimum Y coordinate"""

        @Ymin.setter
        def Ymin(self, arg: float, /) -> None: ...

        @property
        def Ymax(self) -> float:
            """Maximum Y coordinate"""

        @Ymax.setter
        def Ymax(self, arg: float, /) -> None: ...

        @property
        def Zmin(self) -> float:
            """Minimum Z coordinate"""

        @Zmin.setter
        def Zmin(self, arg: float, /) -> None: ...

        @property
        def Zmax(self) -> float:
            """Maximum Z coordinate"""

        @Zmax.setter
        def Zmax(self, arg: float, /) -> None: ...

    def SetWhole(self) -> None:
        """
        Sets this bounding box so that it covers the whole of 3D space.
        It is infinitely long in all directions.
        """

    def SetVoid(self) -> None:
        """
        Sets this bounding box so that it is empty. All points are outside a void box.
        """

    @overload
    def Set(self, P: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets this bounding box so that it bounds
        -   the point P. This involves first setting this bounding box
        to be void and then adding the point P.
        """

    @overload
    def Set(self, P: nanoocp.gp.gp_Pnt, D: nanoocp.gp.gp_Dir) -> None:
        """
        Sets this bounding box so that it bounds
        the half-line defined by point P and direction D, i.e. all
        points M defined by M=P+u*D, where u is greater than
        or equal to 0, are inside the bounding volume. This
        involves first setting this box to be void and then adding the half-line.
        """

    @overload
    def Update(self, aXmin: float, aYmin: float, aZmin: float, aXmax: float, aYmax: float, aZmax: float) -> None:
        """
        Enlarges this bounding box, if required, so that it
        contains at least:
        -   interval [ aXmin,aXmax ] in the "X Direction",
        -   interval [ aYmin,aYmax ] in the "Y Direction",
        -   interval [ aZmin,aZmax ] in the "Z Direction";
        """

    @overload
    def Update(self, X: float, Y: float, Z: float) -> None:
        """Adds a point of coordinates (X,Y,Z) to this bounding box."""

    def GetGap(self) -> float:
        """Returns the gap of this bounding box."""

    def SetGap(self, Tol: float) -> None:
        """Set the gap of this bounding box to abs(Tol)."""

    def Enlarge(self, Tol: float) -> None:
        """
        Enlarges the box with a tolerance value.
        (minvalues-std::abs(<tol>) and maxvalues+std::abs(<tol>))
        This means that the minimum values of its X, Y and Z
        intervals of definition, when they are finite, are reduced by
        the absolute value of Tol, while the maximum values are
        increased by the same amount.
        """

    @overload
    def Get(self) -> tuple[float, float, float, float, float, float]:
        """
        Returns the bounds of this bounding box. The gap is included.
        If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        Standard_ConstructionError exception will be thrown if the box is void.
        if IsVoid()
        """

    @overload
    def Get(self) -> Bnd_Box.Limits:
        """
        Returns the bounds of this bounding box as a Limits structure.
        The gap is included. If this bounding box is infinite (i.e. "open"),
        returned values may be equal to +/- Precision::Infinite().
        If the box is void, returns raw internal values.
        Can be used with C++17 structured bindings:
        @code
        auto [xmin, xmax, ymin, ymax, zmin, zmax] = aBox.Get();
        @endcode
        """

    def GetXMin(self) -> float:
        """
        Returns the Xmin value (IsOpenXmin() ? -Precision::Infinite() : Xmin - GetGap()).
        """

    def GetXMax(self) -> float:
        """
        Returns the Xmax value (IsOpenXmax() ? Precision::Infinite() : Xmax + GetGap()).
        """

    def GetYMin(self) -> float:
        """
        Returns the Ymin value (IsOpenYmin() ? -Precision::Infinite() : Ymin - GetGap()).
        """

    def GetYMax(self) -> float:
        """
        Returns the Ymax value (IsOpenYmax() ? Precision::Infinite() : Ymax + GetGap()).
        """

    def GetZMin(self) -> float:
        """
        Returns the Zmin value (IsOpenZmin() ? -Precision::Infinite() : Zmin - GetGap()).
        """

    def GetZMax(self) -> float:
        """
        Returns the Zmax value (IsOpenZmax() ? Precision::Infinite() : Zmax + GetGap()).
        """

    def CornerMin(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the lower corner of this bounding box. The gap is included.
        If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        Standard_ConstructionError exception will be thrown if the box is void.
        if IsVoid()
        """

    def CornerMax(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the upper corner of this bounding box. The gap is included.
        If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        Standard_ConstructionError exception will be thrown if the box is void.
        if IsVoid()
        """

    def Center(self) -> nanoocp.gp.gp_Pnt | None:
        """
        Returns the center of this bounding box. The gap is included.
        If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        Returns std::nullopt if the box is void.
        """

    def OpenXmin(self) -> None:
        """
        The Box will be infinitely long in the Xmin
        direction.
        """

    def OpenXmax(self) -> None:
        """
        The Box will be infinitely long in the Xmax
        direction.
        """

    def OpenYmin(self) -> None:
        """
        The Box will be infinitely long in the Ymin
        direction.
        """

    def OpenYmax(self) -> None:
        """
        The Box will be infinitely long in the Ymax
        direction.
        """

    def OpenZmin(self) -> None:
        """
        The Box will be infinitely long in the Zmin
        direction.
        """

    def OpenZmax(self) -> None:
        """
        The Box will be infinitely long in the Zmax
        direction.
        """

    def IsOpen(self) -> bool:
        """Returns true if this bounding box has at least one open direction."""

    def IsOpenXmin(self) -> bool:
        """Returns true if this bounding box is open in the Xmin direction."""

    def IsOpenXmax(self) -> bool:
        """Returns true if this bounding box is open in the Xmax direction."""

    def IsOpenYmin(self) -> bool:
        """Returns true if this bounding box is open in the Ymin direction."""

    def IsOpenYmax(self) -> bool:
        """Returns true if this bounding box is open in the Ymax direction."""

    def IsOpenZmin(self) -> bool:
        """Returns true if this bounding box is open in the Zmin direction."""

    def IsOpenZmax(self) -> bool:
        """Returns true if this bounding box is open in the Zmax direction."""

    def IsWhole(self) -> bool:
        """
        Returns true if this bounding box is infinite in all 6 directions (WholeSpace flag).
        """

    def IsVoid(self) -> bool:
        """Returns true if this bounding box is empty (Void flag)."""

    def IsXThin(self, tol: float) -> bool:
        """true if xmax-xmin < tol."""

    def IsYThin(self, tol: float) -> bool:
        """true if ymax-ymin < tol."""

    def IsZThin(self, tol: float) -> bool:
        """true if zmax-zmin < tol."""

    def IsThin(self, tol: float) -> bool:
        """
        Returns true if IsXThin, IsYThin and IsZThin are all true,
        i.e. if the box is thin in all three dimensions.
        """

    def Transformed(self, T: nanoocp.gp.gp_Trsf) -> Bnd_Box:
        """
        Returns a bounding box which is the result of applying the
        transformation T to this bounding box.
        Warning
        Applying a geometric transformation (for example, a
        rotation) to a bounding box generally increases its
        dimensions. This is not optimal for algorithms which use it.
        """

    @overload
    def Add(self, Other: Bnd_Box) -> None:
        """Adds the box <Other> to <me>."""

    @overload
    def Add(self, P: nanoocp.gp.gp_Pnt) -> None:
        """Adds a Pnt to the box."""

    @overload
    def Add(self, P: nanoocp.gp.gp_Pnt, D: nanoocp.gp.gp_Dir) -> None:
        """Extends <me> from the Pnt <P> in the direction <D>."""

    @overload
    def Add(self, D: nanoocp.gp.gp_Dir) -> None:
        """
        Extends the Box in the given Direction, i.e. adds
        an half-line. The box may become infinite in
        1,2 or 3 directions.
        """

    @overload
    def IsOut(self, P: nanoocp.gp.gp_Pnt) -> bool:
        """Returns True if the Pnt is out the box."""

    @overload
    def IsOut(self, L: nanoocp.gp.gp_Lin) -> bool:
        """Returns False if the line intersects the box."""

    @overload
    def IsOut(self, P: nanoocp.gp.gp_Pln) -> bool:
        """Returns False if the plane intersects the box."""

    @overload
    def IsOut(self, Other: Bnd_Box) -> bool:
        """Returns False if the <Box> intersects or is inside <me>."""

    @overload
    def IsOut(self, Other: Bnd_Box, T: nanoocp.gp.gp_Trsf) -> bool:
        """
        Returns False if the transformed <Box> intersects
        or is inside <me>.
        """

    @overload
    def IsOut(self, T1: nanoocp.gp.gp_Trsf, Other: Bnd_Box, T2: nanoocp.gp.gp_Trsf) -> bool:
        """
        Returns False if the transformed <Box> intersects
        or is inside the transformed box <me>.
        """

    @overload
    def IsOut(self, P1: nanoocp.gp.gp_Pnt, P2: nanoocp.gp.gp_Pnt, D: nanoocp.gp.gp_Dir) -> bool:
        """
        Returns False if the flat band lying between two parallel
        lines represented by their reference points <P1>, <P2> and
        direction <D> intersects the box.
        """

    def Contains(self, theP: nanoocp.gp.gp_Pnt) -> bool:
        """Returns True if the point is inside or on the boundary of this box."""

    def Intersects(self, theOther: Bnd_Box) -> bool:
        """Returns True if the other box intersects or is inside this box."""

    def Distance(self, Other: Bnd_Box) -> float:
        """Computes the minimum distance between two boxes."""

    def Dump(self) -> None: ...

    def SquareExtent(self) -> float:
        """Computes the squared diagonal of me."""

    def FinitePart(self) -> Bnd_Box:
        """
        Returns a finite part of an infinite bounding box (returns self if this is already finite
        box). This can be a Void box in case if its sides has been defined as infinite (Open) without
        adding any finite points. WARNING! This method relies on Open flags, the infinite points added
        using Add() method will be returned as is.
        """

    def HasFinitePart(self) -> bool:
        """Returns TRUE if this box has finite part."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

class Bnd_BoundSortBox:
    """
    A tool to compare a bounding box or a plane with a set of
    bounding boxes. It sorts the set of bounding boxes to give
    the list of boxes which intersect the element being compared.
    The boxes being sorted generally bound a set of shapes,
    while the box being compared bounds a shape to be
    compared. The resulting list of intersecting boxes therefore
    gives the list of items which potentially intersect the shape to be compared.
    How to use this class:
    - Create an instance of this class.
    - Initialize it with the set of boxes to be sorted using one of the
    Initialize() methods.
    - Call the Compare() method with the box or plane to be compared.
    Compare() will return the list of indices of the boxes which intersect
    the box or plane passed as argument.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty comparison algorithm for bounding boxes.
        The bounding boxes are then defined using the Initialize function.
        """

    @overload
    def __init__(self, theOther: Bnd_BoundSortBox) -> None: ...

    @overload
    def Initialize(self, theSetOfBoxes: nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box] | None) -> None:
        """
        Initializes this comparison algorithm with the set of boxes.
        @param theSetOfBoxes The set of bounding boxes to be used by this algorithm.
        """

    @overload
    def Initialize(self, theEnclosingBox: Bnd_Box, theSetOfBoxes: nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box] | None) -> None:
        """
        Initializes this comparison algorithm with the set of boxes and the bounding box
        that encloses all those boxes. This version of initialization can be used if complete
        box is known in advance to avoid calculating it again inside the algorithm.
        @param theEnclosingBox The bounding box that contains all the boxes in @p theSetOfBoxes.
        @param theSetOfBoxes The set of bounding boxes to be used by this algorithm.
        """

    @overload
    def Initialize(self, theEnclosingBox: Bnd_Box, theNbBoxes: int) -> None:
        """
        Initializes this comparison algorithm with the bounding box that encloses all the boxes
        that will be used by this algorithm. and the expected number of those boxes.
        Boxes to be considered can then be added using the Add() method.
        @param theEnclosingBox The bounding box that contains all the boxes to be sorted.
        @param theNbComponents The number of components to be added.
        """

    def Add(self, theBox: Bnd_Box, theIndex: int) -> None:
        """
        Adds the bounding box theBox at position boxIndex in the internal array of boxes
        to be sorted by this comparison algorithm. This function is used only in
        conjunction with the Initialize(const Bnd_Box&, const int) method.
        Exceptions:
        - Standard_OutOfRange if boxIndex is not in the range [ 1,nbComponents ] where
        nbComponents is the maximum number of bounding boxes declared for this algorithm at
        initialization.
        - Standard_MultiplyDefined if a box already exists at position @p theIndex in the
        internal array of boxes.
        @param theBox The bounding box to be added.
        @param theIndex The index of the bounding box in the internal array where the box
        will be added. The index is 1-based.
        """

    @overload
    def Compare(self, theBox: Bnd_Box) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Compares the bounding box theBox, with the set of bounding boxes provided to this
        algorithm at initialization, and returns the list of indices of bounding boxes
        that intersect the @p theBox or are inside it.
        The indices correspond to the indices of the bounding boxes in the array provided
        to this algorithm at initialization.
        @param theBox The bounding box to be compared.
        @return The list of indices of bounding boxes that intersect the bounding box theBox
        or are inside it.
        """

    @overload
    def Compare(self, thePlane: nanoocp.gp.gp_Pln) -> nanoocp.NCollection.NCollection_List[int]:
        """
        Compares the plane @p thePlane with the set of bounding boxes provided to this
        algorithm at initialization, and returns the list of indices of bounding boxes
        that intersect the @p thePlane.
        The indices correspond to the indices of the bounding boxes in the array provided
        to this algorithm at initialization.
        @param thePlane The plane to be compared.
        @return The list of indices of bounding boxes that intersect the plane thePlane.
        """

class Bnd_Box2d:
    """
    Describes a bounding box in 2D space.
    A bounding box is parallel to the axes of the coordinates
    system. If it is finite, it is defined by the two intervals:
    -   [ Xmin,Xmax ], and
    -   [ Ymin,Ymax ].
    A bounding box may be infinite (i.e. open) in one or more
    directions. It is said to be:
    -   OpenXmin if it is infinite on the negative side of the   "X Direction";
    -   OpenXmax if it is infinite on the positive side of the   "X Direction";
    -   OpenYmin if it is infinite on the negative side of the   "Y Direction";
    -   OpenYmax if it is infinite on the positive side of the   "Y Direction";
    -   WholeSpace if it is infinite in all four directions. In
    this case, any point of the space is inside the box;
    -   Void if it is empty. In this case, there is no point included in the box.
    A bounding box is defined by four bounds (Xmin, Xmax, Ymin and Ymax) which
    limit the bounding box if it is finite, six flags (OpenXmin, OpenXmax, OpenYmin,
    OpenYmax, WholeSpace and Void) which describe the bounding box if it is infinite or empty, and
    -   a gap, which is included on both sides in any direction when consulting the finite bounds of
    the box.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bnd_Box2d) -> None: ...

    class Limits:
        """
        Structure containing the 2D box limits (Xmin, Xmax, Ymin, Ymax).
        The values include the gap and account for open directions.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: Bnd_Box2d.Limits) -> None: ...

        @property
        def Xmin(self) -> float:
            """Minimum X coordinate"""

        @Xmin.setter
        def Xmin(self, arg: float, /) -> None: ...

        @property
        def Xmax(self) -> float:
            """Maximum X coordinate"""

        @Xmax.setter
        def Xmax(self, arg: float, /) -> None: ...

        @property
        def Ymin(self) -> float:
            """Minimum Y coordinate"""

        @Ymin.setter
        def Ymin(self, arg: float, /) -> None: ...

        @property
        def Ymax(self) -> float:
            """Maximum Y coordinate"""

        @Ymax.setter
        def Ymax(self, arg: float, /) -> None: ...

    def SetWhole(self) -> None:
        """
        Sets this bounding box so that it covers the whole 2D
        space, i.e. it is infinite in all directions.
        """

    def SetVoid(self) -> None:
        """
        Sets this 2D bounding box so that it is empty. All points are outside a void box.
        """

    @overload
    def Set(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets this 2D bounding box so that it bounds
        the point P. This involves first setting this bounding box
        to be void and then adding the point PThe rectangle bounds the point <P>.
        """

    @overload
    def Set(self, thePnt: nanoocp.gp.gp_Pnt2d, theDir: nanoocp.gp.gp_Dir2d) -> None:
        """
        Sets this 2D bounding box so that it bounds
        the half-line defined by point P and direction D, i.e. all
        points M defined by M=P+u*D, where u is greater than
        or equal to 0, are inside the bounding area. This involves
        first setting this 2D box to be void and then adding the half-line.
        """

    @overload
    def Update(self, aXmin: float, aYmin: float, aXmax: float, aYmax: float) -> None:
        """
        Enlarges this 2D bounding box, if required, so that it
        contains at least:
        -   interval [ aXmin,aXmax ] in the "X Direction",
        -   interval [ aYmin,aYmax ] in the "Y Direction\"
        """

    @overload
    def Update(self, X: float, Y: float) -> None:
        """Adds a point of coordinates (X,Y) to this bounding box."""

    def GetGap(self) -> float:
        """Returns the gap of this 2D bounding box."""

    def SetGap(self, Tol: float) -> None:
        """Set the gap of this 2D bounding box to abs(Tol)."""

    def Enlarge(self, theTol: float) -> None:
        """
        Enlarges the box with a tolerance value.
        This means that the minimum values of its X and Y
        intervals of definition, when they are finite, are reduced by
        the absolute value of Tol, while the maximum values are
        increased by the same amount.
        """

    @overload
    def Get(self) -> tuple[float, float, float, float]:
        """
        Returns the bounds of this 2D bounding box.
        The gap is included. If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        if IsVoid()
        """

    @overload
    def Get(self) -> Bnd_Box2d.Limits:
        """
        Returns the bounds of this 2D bounding box as a Limits structure.
        The gap is included. If this bounding box is infinite (i.e. "open"),
        returned values may be equal to +/- Precision::Infinite().
        If the box is void, returns raw internal values.
        Can be used with C++17 structured bindings:
        @code
        auto [xmin, xmax, ymin, ymax] = aBox.Get();
        @endcode
        """

    def GetXMin(self) -> float:
        """
        Returns the Xmin value (IsOpenXmin() ? -Precision::Infinite() : Xmin - GetGap()).
        """

    def GetXMax(self) -> float:
        """
        Returns the Xmax value (IsOpenXmax() ? Precision::Infinite() : Xmax + GetGap()).
        """

    def GetYMin(self) -> float:
        """
        Returns the Ymin value (IsOpenYmin() ? -Precision::Infinite() : Ymin - GetGap()).
        """

    def GetYMax(self) -> float:
        """
        Returns the Ymax value (IsOpenYmax() ? Precision::Infinite() : Ymax + GetGap()).
        """

    def Center(self) -> nanoocp.gp.gp_Pnt2d | None:
        """
        Returns the center of this 2D bounding box. The gap is included.
        If this bounding box is infinite (i.e. "open"), returned values
        may be equal to +/- Precision::Infinite().
        Returns std::nullopt if the box is void.
        """

    def OpenXmin(self) -> None:
        """The Box will be infinitely long in the Xmin direction."""

    def OpenXmax(self) -> None:
        """The Box will be infinitely long in the Xmax direction."""

    def OpenYmin(self) -> None:
        """The Box will be infinitely long in the Ymin direction."""

    def OpenYmax(self) -> None:
        """The Box will be infinitely long in the Ymax direction."""

    def IsOpenXmin(self) -> bool:
        """Returns true if this bounding box is open in the Xmin direction."""

    def IsOpenXmax(self) -> bool:
        """Returns true if this bounding box is open in the Xmax direction."""

    def IsOpenYmin(self) -> bool:
        """Returns true if this bounding box is open in the Ymin direction."""

    def IsOpenYmax(self) -> bool:
        """Returns true if this bounding box is open in the Ymax direction."""

    def IsWhole(self) -> bool:
        """
        Returns true if this bounding box is infinite in all 4
        directions (Whole Space flag).
        """

    def IsVoid(self) -> bool:
        """Returns true if this 2D bounding box is empty (Void flag)."""

    def Transformed(self, T: nanoocp.gp.gp_Trsf2d) -> Bnd_Box2d:
        """
        Returns a bounding box which is the result of applying the
        transformation T to this bounding box.
        Warning
        Applying a geometric transformation (for example, a
        rotation) to a bounding box generally increases its
        dimensions. This is not optimal for algorithms which use it.
        """

    @overload
    def Add(self, Other: Bnd_Box2d) -> None:
        """Adds the 2d box <Other> to <me>."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt2d) -> None:
        """Adds the 2d point."""

    @overload
    def Add(self, thePnt: nanoocp.gp.gp_Pnt2d, theDir: nanoocp.gp.gp_Dir2d) -> None:
        """Extends bounding box from thePnt in the direction theDir."""

    @overload
    def Add(self, D: nanoocp.gp.gp_Dir2d) -> None:
        """
        Extends the Box in the given Direction, i.e. adds
        a half-line. The box may become infinite in 1 or 2
        directions.
        """

    @overload
    def IsOut(self, P: nanoocp.gp.gp_Pnt2d) -> bool:
        """Returns True if the 2d pnt <P> is out <me>."""

    @overload
    def IsOut(self, theL: nanoocp.gp.gp_Lin2d) -> bool:
        """Returns True if the line doesn't intersect the box."""

    @overload
    def IsOut(self, theP0: nanoocp.gp.gp_Pnt2d, theP1: nanoocp.gp.gp_Pnt2d) -> bool:
        """Returns True if the segment doesn't intersect the box."""

    @overload
    def IsOut(self, Other: Bnd_Box2d) -> bool:
        """Returns True if <Box2d> is out <me>."""

    @overload
    def IsOut(self, theOther: Bnd_Box2d, theTrsf: nanoocp.gp.gp_Trsf2d) -> bool:
        """Returns True if transformed <Box2d> is out <me>."""

    @overload
    def IsOut(self, T1: nanoocp.gp.gp_Trsf2d, Other: Bnd_Box2d, T2: nanoocp.gp.gp_Trsf2d) -> bool:
        """
        Compares a transformed bounding with a transformed
        bounding. The default implementation is to make a copy
        of <me> and <Other>, to transform them and to test.
        """

    def Contains(self, theP: nanoocp.gp.gp_Pnt2d) -> bool:
        """Returns True if the 2d point is inside or on the boundary of this box."""

    def Intersects(self, theOther: Bnd_Box2d) -> bool:
        """Returns True if the other 2d box intersects or is inside this box."""

    def Distance(self, theOther: Bnd_Box2d) -> float:
        """Computes the minimum distance between two 2D boxes."""

    def Dump(self) -> None: ...

    def SquareExtent(self) -> float:
        """Computes the squared diagonal of me."""

class Bnd_OBB:
    """
    The class describes the Oriented Bounding Box (OBB),
    much tighter enclosing volume for the shape than the
    Axis Aligned Bounding Box (AABB).
    The OBB is defined by a center of the box, the axes and the halves
    of its three dimensions.
    The OBB can be used more effectively than AABB as a rejection mechanism
    for non-interfering objects.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theBox: Bnd_Box) -> None:
        """Constructor to create OBB from AABB."""

    @overload
    def __init__(self, theCenter: nanoocp.gp.gp_Pnt, theXDirection: nanoocp.gp.gp_Dir, theYDirection: nanoocp.gp.gp_Dir, theZDirection: nanoocp.gp.gp_Dir, theHXSize: float, theHYSize: float, theHZSize: float) -> None:
        """Constructor taking all defining parameters"""

    @overload
    def __init__(self, theOther: Bnd_OBB) -> None: ...

    class HalfSizes:
        """
        Structure containing the OBB half-size dimensions.
        Can be used with C++17 structured bindings:
        @code
        auto [aHX, aHY, aHZ] = anOBB.GetHalfSizes();
        @endcode
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: Bnd_OBB.HalfSizes) -> None: ...

        @property
        def X(self) -> float:
            """Half-size along X axis"""

        @X.setter
        def X(self, arg: float, /) -> None: ...

        @property
        def Y(self) -> float:
            """Half-size along Y axis"""

        @Y.setter
        def Y(self, arg: float, /) -> None: ...

        @property
        def Z(self) -> float:
            """Half-size along Z axis"""

        @Z.setter
        def Z(self, arg: float, /) -> None: ...

    def ReBuild(self, theListOfPoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theListOfTolerances: nanoocp.NCollection.NCollection_Array1[float] = None, theIsOptimal: bool = False) -> None:
        """
        Creates new OBB covering every point in theListOfPoints.
        Tolerance of every such point is set by *theListOfTolerances array.
        If this array is not void (not null-pointer) then the resulted Bnd_OBB
        will be enlarged using tolerances of points lying on the box surface.
        <theIsOptimal> flag defines the mode in which the OBB will be built.
        Constructing Optimal box takes more time, but the resulting box is usually
        more tight. In case of construction of Optimal OBB more possible
        axes are checked.
        """

    def SetCenter(self, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """Sets the center of OBB"""

    def SetXComponent(self, theXDirection: nanoocp.gp.gp_Dir, theHXSize: float) -> None:
        """Sets the X component of OBB - direction and size"""

    def SetYComponent(self, theYDirection: nanoocp.gp.gp_Dir, theHYSize: float) -> None:
        """Sets the Y component of OBB - direction and size"""

    def SetZComponent(self, theZDirection: nanoocp.gp.gp_Dir, theHZSize: float) -> None:
        """Sets the Z component of OBB - direction and size"""

    def Position(self) -> nanoocp.gp.gp_Ax3:
        """
        Returns the local coordinates system of this oriented box.
        So that applying it to axis-aligned box ((-XHSize, -YHSize, -ZHSize), (XHSize, YHSize,
        ZHSize)) will produce this oriented box.
        @code
        gp_Trsf aLoc;
        aLoc.SetTransformation (theOBB.Position(), gp::XOY());
        @endcode
        """

    def Center(self) -> nanoocp.gp.gp_XYZ:
        """Returns the center of OBB"""

    def XDirection(self) -> nanoocp.gp.gp_XYZ:
        """Returns the X Direction of OBB"""

    def YDirection(self) -> nanoocp.gp.gp_XYZ:
        """Returns the Y Direction of OBB"""

    def ZDirection(self) -> nanoocp.gp.gp_XYZ:
        """Returns the Z Direction of OBB"""

    def XHSize(self) -> float:
        """Returns the X Dimension of OBB"""

    def YHSize(self) -> float:
        """Returns the Y Dimension of OBB"""

    def ZHSize(self) -> float:
        """Returns the Z Dimension of OBB"""

    def GetHalfSizes(self) -> Bnd_OBB.HalfSizes:
        """
        Returns the half-size dimensions of the OBB as a HalfSizes structure.
        Can be used with C++17 structured bindings:
        @code
        auto [aHX, aHY, aHZ] = anOBB.GetHalfSizes();
        @endcode
        """

    def IsVoid(self) -> bool:
        """Checks if the box is empty."""

    def SetVoid(self) -> None:
        """Clears this box"""

    def SetAABox(self, theFlag: bool) -> None:
        """Sets the flag for axes aligned box"""

    def IsAABox(self) -> bool:
        """Returns TRUE if the box is axes aligned"""

    def Enlarge(self, theGapAdd: float) -> None:
        """Enlarges the box with the given value"""

    def SquareExtent(self) -> float:
        """Returns square diagonal of this box"""

    @overload
    def IsOut(self, theOther: Bnd_OBB) -> bool:
        """Check if the box do not interfere the other box."""

    @overload
    def IsOut(self, theP: nanoocp.gp.gp_Pnt) -> bool:
        """Check if the point is inside of <this>."""

    def Contains(self, theP: nanoocp.gp.gp_Pnt) -> bool:
        """Returns True if the point is inside or on the boundary of this OBB."""

    def Intersects(self, theOther: Bnd_OBB) -> bool:
        """Returns True if the other OBB intersects or is inside this OBB."""

    def IsCompletelyInside(self, theOther: Bnd_OBB) -> bool:
        """Check if the theOther is completely inside *this."""

    @overload
    def Add(self, theOther: Bnd_OBB) -> None:
        """
        Rebuilds this in order to include all previous objects
        (which it was created from) and theOther.
        """

    @overload
    def Add(self, theP: nanoocp.gp.gp_Pnt) -> None:
        """
        Rebuilds this in order to include all previous objects
        (which it was created from) and theP.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Bnd_Range:
    """
    This class describes a range in 1D space restricted
    by two real values.
    A range can be void indicating there is no point included in the range.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor. Creates VOID range."""

    @overload
    def __init__(self, theMin: float, theMax: float) -> None:
        """Constructor. Never creates VOID range."""

    @overload
    def __init__(self, theOther: Bnd_Range) -> None: ...

    class IntersectStatus(enum.IntEnum):
        """
        Status of intersection check with a periodic value.
        @sa IsIntersected()
        """

        IntersectStatus_Out = 0

        IntersectStatus_In = 1

        IntersectStatus_Boundary = 2

    IntersectStatus_Out: Bnd_Range.IntersectStatus = IntersectStatus.IntersectStatus_Out

    IntersectStatus_In: Bnd_Range.IntersectStatus = IntersectStatus.IntersectStatus_In

    IntersectStatus_Boundary: Bnd_Range.IntersectStatus = IntersectStatus.IntersectStatus_Boundary

    class Bounds:
        """
        Structure containing the range bounds (Min, Max).
        Can be used with C++17 structured bindings:
        @code
        auto [aMin, aMax] = aRange.Get();
        @endcode
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: Bnd_Range.Bounds) -> None: ...

        @property
        def Min(self) -> float:
            """Minimum value of the range"""

        @Min.setter
        def Min(self, arg: float, /) -> None: ...

        @property
        def Max(self) -> float:
            """Maximum value of the range"""

        @Max.setter
        def Max(self, arg: float, /) -> None: ...

    def Common(self, theOther: Bnd_Range) -> None:
        """Replaces <this> with common-part of <this> and theOther"""

    def Union(self, theOther: Bnd_Range) -> bool:
        """
        Joins *this and theOther to one interval.
        Replaces *this to the result.
        Returns false if the operation cannot be done (e.g.
        input arguments are empty or separated).
        @sa use method ::Add() to merge two ranges unconditionally
        """

    def Split(self, theVal: float, theList: nanoocp.NCollection.NCollection_List[nanoocp.Bnd.Bnd_Range], thePeriod: float = 0.0) -> None:
        """
        Splits <this> to several sub-ranges by theVal value
        (e.g. range [3, 15] will be split by theVal==5 to the two
        ranges: [3, 5] and [5, 15]). New ranges will be pushed to
        theList (theList must be initialized correctly before
        calling this method).
        If thePeriod != 0.0 then at least one boundary of
        new ranges (if <*this> intersects theVal+k*thePeriod) will be equal to
        theVal+thePeriod*k, where k is an integer number (k = 0, +/-1, +/-2, ...).
        (let thePeriod in above example be 4 ==> we will obtain
        four ranges: [3, 5], [5, 9], [9, 13] and [13, 15].
        """

    def IsIntersected(self, theVal: float, thePeriod: float = 0.0) -> Bnd_Range.IntersectStatus:
        """
        Checks if <this> intersects values like
        theVal+k*thePeriod, where k is an integer number (k = 0, +/-1, +/-2, ...).

        ATTENTION!!!
        If (myFirst == myLast) then this function will return only either Out or Boundary.
        """

    @overload
    def Add(self, theParameter: float) -> None:
        """Extends <this> to include theParameter"""

    @overload
    def Add(self, theRange: Bnd_Range) -> None:
        """
        Extends this range to include both ranges.
        @sa use method ::Union() to check if two ranges overlap method merging
        """

    def GetMin(self) -> tuple[bool, float]:
        """
        Obtain MIN boundary of <this>.
        If <this> is VOID the method returns false.
        """

    def GetMax(self) -> tuple[bool, float]:
        """
        Obtain MAX boundary of <this>.
        If <this> is VOID the method returns false.
        """

    def GetBounds(self) -> tuple[bool, float, float]:
        """
        Obtain first and last boundary of <this>.
        If <this> is VOID the method returns false.
        """

    def Get(self) -> Bnd_Range.Bounds | None:
        """
        Returns the bounds of this range as a Bounds structure.
        Returns std::nullopt if IsVoid().
        Can be used with C++17 structured bindings:
        @code
        if (auto aBounds = aRange.Get())
        {
        auto [aMin, aMax] = *aBounds;
        }
        @endcode
        """

    def GetIntermediatePoint(self, theLambda: float) -> tuple[bool, float]:
        """
        Obtain theParameter satisfied to the equation
        (theParameter-MIN)/(MAX-MIN) == theLambda.
        *  theLambda == 0 --> MIN boundary will be returned;
        *  theLambda == 0.5 --> Middle point will be returned;
        *  theLambda == 1 --> MAX boundary will be returned;
        *  theLambda < 0 --> the value less than MIN will be returned;
        *  theLambda > 1 --> the value greater than MAX will be returned.
        If <this> is VOID the method returns false.
        """

    def Center(self) -> float | None:
        """
        Returns the center of this range ((Min + Max) / 2).
        Returns std::nullopt if IsVoid().
        """

    def Delta(self) -> float:
        """Returns range value (MAX-MIN). Returns negative value for VOID range."""

    def IsVoid(self) -> bool:
        """Is <this> initialized."""

    def SetVoid(self) -> None:
        """Initializes <this> by default parameters. Makes <this> VOID."""

    def Enlarge(self, theDelta: float) -> None:
        """Extends this to the given value (in both side)"""

    def Shifted(self, theVal: float) -> Bnd_Range:
        """Returns the copy of <*this> shifted by theVal"""

    def Shift(self, theVal: float) -> None:
        """Shifts <*this> by theVal"""

    def TrimFrom(self, theValLower: float) -> None:
        """
        Trims the First value in range by the given lower limit.
        Marks range as Void if the given Lower value is greater than range Max.
        """

    def TrimTo(self, theValUpper: float) -> None:
        """
        Trim the Last value in range by the given Upper limit.
        Marks range as Void if the given Upper value is smaller than range Max.
        """

    @overload
    def IsOut(self, theValue: float) -> bool:
        """Returns True if the value is out of this range."""

    @overload
    def IsOut(self, theRange: Bnd_Range) -> bool:
        """Returns True if the given range is out of this range."""

    def Contains(self, theValue: float) -> bool:
        """Returns True if the value is within this range."""

    def Intersects(self, theRange: Bnd_Range) -> bool:
        """Returns True if the given range intersects (overlaps with) this range."""

    def Min(self) -> float | None:
        """
        Returns the MIN boundary of <this>.
        Returns std::nullopt if IsVoid().
        """

    def Max(self) -> float | None:
        """
        Returns the MAX boundary of <this>.
        Returns std::nullopt if IsVoid().
        """

    def __eq__(self, theOther: Bnd_Range) -> bool:
        """Returns TRUE if theOther is equal to <*this>"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Bnd_Sphere:
    """
    This class represents a bounding sphere of a geometric entity
    (triangle, segment of line or whatever else).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theCntr: nanoocp.gp.gp_XYZ, theRad: float, theU: int, theV: int) -> None:
        """Constructor of a definite sphere"""

    @overload
    def __init__(self, theOther: Bnd_Sphere) -> None: ...

    def U(self) -> int:
        """Returns the U parameter on shape"""

    def V(self) -> int:
        """Returns the V parameter on shape"""

    def IsValid(self) -> bool:
        """
        Returns validity status, indicating that this
        sphere corresponds to a real entity
        """

    def SetValid(self, isValid: bool) -> None: ...

    def Center(self) -> nanoocp.gp.gp_XYZ:
        """Returns center of sphere object"""

    def Radius(self) -> float:
        """Returns the radius value"""

    def Distances(self, theXYZ: nanoocp.gp.gp_XYZ) -> tuple[float, float]:
        """
        Calculate and return minimal and maximal distance to sphere.
        NOTE: This function is tightly optimized; any modifications
        may affect performance!
        """

    def SquareDistances(self, theXYZ: nanoocp.gp.gp_XYZ) -> tuple[float, float]:
        """
        Calculate and return minimal and maximal distance to sphere.
        NOTE: This function is tightly optimized; any modifications
        may affect performance!
        """

    def Project(self, theNode: nanoocp.gp.gp_XYZ, theProjNode: nanoocp.gp.gp_XYZ) -> tuple[bool, float, bool]:
        """
        Projects a point on entity.
        Returns true if success
        """

    def Distance(self, theNode: nanoocp.gp.gp_XYZ) -> float: ...

    def SquareDistance(self, theNode: nanoocp.gp.gp_XYZ) -> float: ...

    def Add(self, theOther: Bnd_Sphere) -> None: ...

    @overload
    def IsOut(self, theOther: Bnd_Sphere) -> bool: ...

    @overload
    def IsOut(self, thePnt: nanoocp.gp.gp_XYZ) -> tuple[bool, float]: ...

    def SquareExtent(self) -> float: ...

class Bnd_Tools:
    """Defines a set of static methods operating with bounding boxes"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Bnd_Tools) -> None: ...

    @overload
    @staticmethod
    def Bnd2BVH(theBox: Bnd_Box2d) -> "BVH_Box<double, 2>":
        """
        @name Bnd_Box to BVH_Box conversion
        Converts the given Bnd_Box2d to BVH_Box
        """

    @overload
    @staticmethod
    def Bnd2BVH(theBox: Bnd_Box) -> "BVH_Box<double, 3>":
        """Converts the given Bnd_Box to BVH_Box"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Bnd
Bnd_Array1OfBox = nanoocp.NCollection.NCollection_Array1[nanoocp.Bnd.Bnd_Box]
Bnd_HArray1OfBox = nanoocp.NCollection.NCollection_HArray1[nanoocp.Bnd.Bnd_Box]
