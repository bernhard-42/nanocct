"""OCCT package AppParCurves (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.gp
import nanoocp.math


class AppParCurves_Constraint(enum.IntEnum):
    """
    -   NoConstraint: this point has no constraints.
    -   PassPoint: the approximation curve passes through this point.
    -   TangencyPoint: this point has a tangency constraint.
    -   CurvaturePoint: this point has a curvature constraint.
    """

    AppParCurves_NoConstraint = 0

    AppParCurves_PassPoint = 1

    AppParCurves_TangencyPoint = 2

    AppParCurves_CurvaturePoint = 3

AppParCurves_NoConstraint: AppParCurves_Constraint = AppParCurves_Constraint.AppParCurves_NoConstraint

AppParCurves_PassPoint: AppParCurves_Constraint = AppParCurves_Constraint.AppParCurves_PassPoint

AppParCurves_TangencyPoint: AppParCurves_Constraint = ...

AppParCurves_CurvaturePoint: AppParCurves_Constraint = ...

class AppParCurves:
    """
    Parallel Approximation in n curves.
    This package gives all the algorithms used to approximate a MultiLine
    described by the tool MLineTool.
    The result of the approximation will be a MultiCurve.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AppParCurves) -> None: ...

    @staticmethod
    def BernsteinMatrix(NbPoles: int, U: nanoocp.math.math_Vector, A: nanoocp.math.math_Matrix) -> None: ...

    @staticmethod
    def Bernstein(NbPoles: int, U: nanoocp.math.math_Vector, A: nanoocp.math.math_Matrix, DA: nanoocp.math.math_Matrix) -> None: ...

    @staticmethod
    def SecondDerivativeBernstein(U: float, DDA: nanoocp.math.math_Vector) -> None: ...

    @staticmethod
    def SplineFunction(NbPoles: int, Degree: int, Parameters: nanoocp.math.math_Vector, FlatKnots: nanoocp.math.math_Vector, A: nanoocp.math.math_Matrix, DA: nanoocp.math.math_Matrix, Index: nanoocp.math.math_IntegerVector) -> None: ...

class AppParCurves_ConstraintCouple:
    """
    associates an index and a constraint for an object.
    This couple is used by AppDef_TheVariational when performing approximations.
    """

    @overload
    def __init__(self) -> None:
        """returns an indefinite ConstraintCouple."""

    @overload
    def __init__(self, TheIndex: int, Cons: AppParCurves_Constraint) -> None:
        """
        Create a couple the object <Index> will have the
        constraint <Cons>.
        """

    @overload
    def __init__(self, theOther: AppParCurves_ConstraintCouple) -> None: ...

    def Index(self) -> int:
        """returns the index of the constraint object."""

    def Constraint(self) -> AppParCurves_Constraint:
        """returns the constraint of the object."""

    def SetIndex(self, TheIndex: int) -> None:
        """Changes the index of the constraint object."""

    def SetConstraint(self, Cons: AppParCurves_Constraint) -> None:
        """Changes the constraint of the object."""

class AppParCurves_MultiPoint:
    """
    This class describes Points composing a MultiPoint.
    These points can be 2D or 3D. The user must first give the
    3D Points and then the 2D Points.
    They are Poles of a Bezier Curve.
    This class is used either to define data input or
    results when performing the approximation of several lines in parallel.
    """

    @overload
    def __init__(self) -> None:
        """creates an indefinite MultiPoint."""

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """creates a MultiPoint only composed of 3D points."""

    @overload
    def __init__(self, tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """creates a MultiPoint only composed of 2D points."""

    @overload
    def __init__(self, NbPoints: int, NbPoints2d: int) -> None:
        """
        constructs a set of Points used to approximate a
        Multiline.
        These Points can be of 2 or 3 dimensions.
        Points will be initialized with SetPoint and SetPoint2d.
        NbPoints is the number of 3D Points.
        NbPoints2d is the number of 2D Points.
        """

    @overload
    def __init__(self, tabP: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], tabP2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        constructs a set of Points used to approximate a
        Multiline.
        These Points can be of 2 or 3 dimensions.
        Points will be initialized with SetPoint and SetPoint2d.
        NbPoints is the total number of Points.
        """

    @overload
    def __init__(self, theOther: AppParCurves_MultiPoint) -> None: ...

    def SetPoint(self, Index: int, Point: nanoocp.gp.gp_Pnt) -> None:
        """
        the 3d Point of range Index of this MultiPoint is
        set to <Point>.
        An exception is raised if Index < 0 or
        Index > number of 3d Points.
        """

    def Point(self, Index: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the 3d Point of range Index.
        An exception is raised if Index < 0 or
        Index < number of 3d Points.
        """

    def SetPoint2d(self, Index: int, Point: nanoocp.gp.gp_Pnt2d) -> None:
        """
        The 2d Point of range Index is set to <Point>.
        An exception is raised if Index > 3d Points or
        Index > total number of Points.
        """

    def Point2d(self, Index: int) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the 2d Point of range Index.
        An exception is raised if index <= number of
        3d Points or Index > total number of Points.
        """

    def Dimension(self, Index: int) -> int:
        """
        returns the dimension of the point of range Index.
        An exception is raised if Index <0 or Index > NbCurves.
        """

    def NbPoints(self) -> int:
        """returns the number of points of dimension 3D."""

    def NbPoints2d(self) -> int:
        """returns the number of points of dimension 2D."""

    def Transform(self, CuIndex: int, x: float, dx: float, y: float, dy: float, z: float, dz: float) -> None:
        """
        Applies a transformation to the curve of range
        <CuIndex>.
        newx = x + dx*oldx
        newy = y + dy*oldy    for all points of the curve.
        newz = z + dz*oldz
        """

    def Transform2d(self, CuIndex: int, x: float, dx: float, y: float, dy: float) -> None:
        """
        Applies a transformation to the Curve of range
        <CuIndex>.
        newx = x + dx*oldx
        newy = y + dy*oldy    for all points of the curve.
        """

    def Dump(self) -> str:
        """
        Prints on the stream o information on the current
        state of the object.
        Is used to redefine the operator <<.
        """

class AppParCurves_MultiCurve:
    """
    This class describes a MultiCurve approximating a Multiline.
    As a Multiline is a set of n lines, a MultiCurve is a set
    of n curves. These curves are Bezier curves.
    A MultiCurve is composed of m MultiPoint.
    The approximating degree of these n curves is the same for
    each one.

    Example of a MultiCurve composed of MultiPoints:

    P1______P2_____P3______P4________........_____PNbMPoints

    Q1______Q2_____Q3______Q4________........_____QNbMPoints
    .                                               .
    .                                               .
    .                                               .
    R1______R2_____R3______R4________........_____RNbMPoints

    Pi, Qi, ..., Ri are points of dimension 2 or 3.

    (Pi, Qi, ...Ri), i= 1,...NbPoles are MultiPoints.
    each MultiPoint has got NbPol Poles.
    """

    @overload
    def __init__(self) -> None:
        """returns an indefinite MultiCurve."""

    @overload
    def __init__(self, NbPol: int) -> None:
        """
        creates a MultiCurve, describing Bezier curves all
        containing the same number of MultiPoint.
        An exception is raised if Degree < 0.
        """

    @overload
    def __init__(self, tabMU: nanoocp.NCollection.NCollection_Array1[nanoocp.AppParCurves.AppParCurves_MultiPoint]) -> None:
        """
        creates a MultiCurve, describing Bezier curves all
        containing the same number of MultiPoint.
        Each MultiPoint must have NbCurves Poles.
        """

    @overload
    def __init__(self, theOther: AppParCurves_MultiCurve) -> None: ...

    def SetNbPoles(self, nbPoles: int) -> None:
        """
        The number of poles of the MultiCurve
        will be set to <nbPoles>.
        """

    def SetValue(self, Index: int, MPoint: AppParCurves_MultiPoint) -> None:
        """
        sets the MultiPoint of range Index to the value
        <MPoint>.
        An exception is raised if Index <0 or Index >NbMPoint.
        """

    def NbCurves(self) -> int:
        """
        Returns the number of curves resulting from the
        approximation of a MultiLine.
        """

    def NbPoles(self) -> int:
        """
        Returns the number of poles on curves resulting from the approximation of a MultiLine.
        """

    def Degree(self) -> int:
        """returns the degree of the curves."""

    def Dimension(self, CuIndex: int) -> int:
        """
        returns the dimension of the CuIndex curve.
        An exception is raised if CuIndex<0 or CuIndex>NbCurves.
        """

    @overload
    def Curve(self, CuIndex: int, TabPnt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        returns the Pole array of the curve of range CuIndex.
        An exception is raised if the dimension of the curve
        is 2d.
        """

    @overload
    def Curve(self, CuIndex: int, TabPnt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d]) -> None:
        """
        returns the Pole array of the curve of range CuIndex.
        An exception is raised if the dimension of the curve
        is 3d.
        """

    @overload
    def Value(self, Index: int) -> AppParCurves_MultiPoint:
        """
        returns the Index MultiPoint.
        An exception is raised if Index <0 or Index >Degree+1.
        """

    @overload
    def Value(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    @overload
    def Value(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    def Pole(self, CuIndex: int, Nieme: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the Nieme pole of the CuIndex curve.
        the curve must be a 3D curve.
        """

    def Pole2d(self, CuIndex: int, Nieme: int) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the Nieme pole of the CuIndex curve.
        the curve must be a 2D curve.
        """

    def Transform(self, CuIndex: int, x: float, dx: float, y: float, dy: float, z: float, dz: float) -> None:
        """
        Applies a transformation to the curve of range
        <CuIndex>.
        newx = x + dx*oldx
        newy = y + dy*oldy    for all points of the curve.
        newz = z + dz*oldz
        """

    def Transform2d(self, CuIndex: int, x: float, dx: float, y: float, dy: float) -> None:
        """
        Applies a transformation to the Curve of range
        <CuIndex>.
        newx = x + dx*oldx
        newy = y + dy*oldy    for all points of the curve.
        """

    @overload
    def D1(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    @overload
    def D1(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    @overload
    def D2(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    @overload
    def D2(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        returns the value of the point with a parameter U
        on the Bezier curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    def Dump(self) -> str:
        """
        Prints on the stream o information on the current
        state of the object.
        Is used to redefine the operator <<.
        """

class AppParCurves_MultiBSpCurve(AppParCurves_MultiCurve):
    """
    This class describes a MultiBSpCurve approximating a Multiline.
    Just as a Multiline is a set of a given number of lines, a MultiBSpCurve is a set
    of a specified number of bsplines defined by:
    -   A specified number of MultiPoints - the poles of a specified number of curves
    -   The degree of approximation identical for each of the specified number of curves.

    Example of a MultiBSpCurve composed of a specified number of MultiPoints:

    P1______P2_____P3______P4________........_____PNbMPoints

    Q1______Q2_____Q3______Q4________........_____QNbMPoints
    .                                               .
    .                                               .
    .                                               .
    R1______R2_____R3______R4________........_____RNbMPoints

    Pi, Qi, ..., Ri are points of dimension 2 or 3.

    (Pi, Qi, ...Ri), i= 1,...NbPoles are MultiPoints.
    each MultiPoint has got NbPol Poles.
    MultiBSpCurves are created by the SplineValue method in the ComputeLine
    class, and by the Value method in TheVariational class. MultiBSpCurve
    provides the information required to create the BSpline defined by the approximation.
    """

    @overload
    def __init__(self) -> None:
        """returns an indefinite MultiBSpCurve."""

    @overload
    def __init__(self, NbPol: int) -> None:
        """
        creates a MultiBSpCurve, describing BSpline curves all
        containing the same number of MultiPoint.
        An exception is raised if Degree < 0.
        """

    @overload
    def __init__(self, tabMU: nanoocp.NCollection.NCollection_Array1[nanoocp.AppParCurves.AppParCurves_MultiPoint], Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        creates a MultiBSpCurve, describing BSpline curves all
        containing the same number of MultiPoint.
        Each MultiPoint must have NbCurves Poles.
        """

    @overload
    def __init__(self, SC: AppParCurves_MultiCurve, Knots: nanoocp.NCollection.NCollection_Array1[float], Mults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        creates a MultiBSpCurve, describing BSpline
        curves, taking control points from <SC>.
        """

    @overload
    def __init__(self, theOther: AppParCurves_MultiBSpCurve) -> None: ...

    def SetKnots(self, theKnots: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Knots of the multiBSpCurve are assigned to <theknots>."""

    def SetMultiplicities(self, theMults: nanoocp.NCollection.NCollection_Array1[int]) -> None:
        """
        Multiplicities of the multiBSpCurve are assigned
        to <theMults>.
        """

    def Knots(self) -> nanoocp.NCollection.NCollection_Array1[float]:
        """
        Returns an array of Reals containing
        the multiplicities of curves resulting from the approximation.
        """

    def Multiplicities(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """
        Returns an array of Reals containing the
        multiplicities of curves resulting from the approximation.
        """

    def Degree(self) -> int:
        """returns the degree of the curve(s)."""

    @overload
    def Value(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    @overload
    def Value(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    @overload
    def D1(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    @overload
    def D1(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    @overload
    def D2(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 3d.
        """

    @overload
    def D2(self, CuIndex: int, U: float, Pt: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d, V2: nanoocp.gp.gp_Vec2d) -> None:
        """
        returns the value of the point with a parameter U
        on the BSpline curve number CuIndex.
        An exception is raised if CuIndex <0 or > NbCurves.
        An exception is raised if the curve dimension is 2d.
        """

    def Dump(self) -> str:
        """
        Prints on the stream o information on the current
        state of the object.
        Is used to redefine the operator <<.
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.AppParCurves
AppParCurves_Array1OfConstraintCouple = nanoocp.NCollection.NCollection_Array1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple]
AppParCurves_Array1OfMultiPoint = nanoocp.NCollection.NCollection_Array1[nanoocp.AppParCurves.AppParCurves_MultiPoint]
AppParCurves_HArray1OfConstraintCouple = nanoocp.NCollection.NCollection_HArray1[nanoocp.AppParCurves.AppParCurves_ConstraintCouple]
AppParCurves_SequenceOfMultiCurve = nanoocp.NCollection.NCollection_Sequence[nanoocp.AppParCurves.AppParCurves_MultiCurve]
