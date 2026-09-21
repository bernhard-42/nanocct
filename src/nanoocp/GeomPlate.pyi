"""OCCT package GeomPlate (toolkit TKGeomAlgo)"""

from typing import overload

import nanoocp.Adaptor2d
import nanoocp.Adaptor3d
import nanoocp.AdvApp2Var
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomLProp
import nanoocp.Law
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Plate
import nanoocp.Standard
import nanoocp.gp


class GeomPlate_Aij:
    """A structure containing indexes of two normals and its cross product"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anInd1: int, anInd2: int, aVec: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: GeomPlate_Aij) -> None: ...

class GeomPlate_BuildAveragePlane:
    """
    This class computes an average inertial plane with an
    array of points.
    Computes the initial surface (average plane) in the cases
    when the initial surface is not given.
    """

    @overload
    def __init__(self, Normals: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Vec], Pts: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None) -> None:
        """Creates the plane from the "best vector\""""

    @overload
    def __init__(self, Pts: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, NbBoundPoints: int, Tol: float, POption: int, NOption: int) -> None:
        """
        Tol is a Tolerance to make the difference between
        the result plane and the result line.
        if POption = 1 : automatic parametrisation
        if POption = 2 : parametrisation by eigen vectors
        if NOption = 1 : the average plane is the inertial plane.
        if NOption = 2 : the average plane is the plane of max. flux.
        """

    @overload
    def __init__(self, theOther: GeomPlate_BuildAveragePlane) -> None: ...

    def Plane(self) -> nanoocp.Geom.Geom_Plane:
        """Return the average Plane."""

    def Line(self) -> nanoocp.Geom.Geom_Line:
        """Return a Line when 2 eigenvalues are null."""

    def IsPlane(self) -> bool:
        """return OK if is a plane."""

    def IsLine(self) -> bool:
        """return OK if is a line."""

    def MinMaxBox(self) -> tuple[float, float, float, float]:
        """
        computes the minimal box to include all normal
        projection points of the initial array on the plane.
        """

    @staticmethod
    def HalfSpace(NewNormals: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Vec], Normals: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Vec], Bset: nanoocp.NCollection.NCollection_Sequence[nanoocp.GeomPlate.GeomPlate_Aij], LinTol: float, AngTol: float) -> bool: ...

class GeomPlate_CurveConstraint(nanoocp.Standard.Standard_Transient):
    """Defines curves as constraints to be used to deform a surface."""

    @overload
    def __init__(self) -> None:
        """Initializes an empty curve constraint object."""

    @overload
    def __init__(self, Boundary: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Order: int, NPt: int = 10, TolDist: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1) -> None:
        """
        Create a constraint
        Order is the order of the constraint. The possible values for order are -1,0,1,2.
        Order i means constraints Gi
        Npt is the number of points associated with the constraint.
        TolDist is the maximum error to satisfy for G0 constraints
        TolAng is the maximum error to satisfy for G1 constraints
        TolCurv is the maximum error to satisfy for G2 constraints
        These errors can be replaced by laws of criterion.
        Raises ConstructionError if Order is not -1 , 0, 1, 2
        """

    @overload
    def __init__(self, theOther: GeomPlate_CurveConstraint) -> None: ...

    def SetOrder(self, Order: int) -> None:
        """
        Allows you to set the order of continuity required for
        the constraints: G0, G1, and G2, controlled
        respectively by G0Criterion G1Criterion and G2Criterion.
        """

    def Order(self) -> int:
        """Returns the order of constraint, one of G0, G1 or G2."""

    def NbPoints(self) -> int:
        """
        Returns the number of points on the curve used as a
        constraint. The default setting is 10. This parameter
        affects computation time, which increases by the cube of
        the number of points.
        """

    def SetNbPoints(self, NewNb: int) -> None:
        """
        Allows you to set the number of points on the curve
        constraint. The default setting is 10. This parameter
        affects computation time, which increases by the cube of
        the number of points.
        """

    def SetG0Criterion(self, G0Crit: nanoocp.Law.Law_Function | None) -> None:
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface for each point of the
        constraint. If this criterion is not set, TolDist, the
        distance tolerance from the constructor, is used.
        """

    def SetG1Criterion(self, G1Crit: nanoocp.Law.Law_Function | None) -> None:
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises ConstructionError if the curve is not on a surface
        """

    def SetG2Criterion(self, G2Crit: nanoocp.Law.Law_Function | None) -> None: ...

    def G0Criterion(self, U: float) -> float:
        """
        Returns the G0 criterion at the parametric point U on
        the curve. This is the greatest distance allowed between
        the constraint and the target surface at U.
        """

    def G1Criterion(self, U: float) -> float:
        """
        Returns the G1 criterion at the parametric point U on
        the curve. This is the greatest angle allowed between
        the constraint and the target surface at U.
        Raises ConstructionError if the curve is not on a surface
        """

    def G2Criterion(self, U: float) -> float:
        """
        Returns the G2 criterion at the parametric point U on
        the curve. This is the greatest difference in curvature
        allowed between the constraint and the target surface at U.
        Raises ConstructionError if the curve is not on a surface
        """

    def FirstParameter(self) -> float: ...

    def LastParameter(self) -> float: ...

    def Length(self) -> float: ...

    def LPropSurf(self, U: float) -> nanoocp.GeomLProp.GeomLProp_SLProps: ...

    def D0(self, U: float, P: nanoocp.gp.gp_Pnt) -> None: ...

    def D1(self, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    def D2(self, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec, V4: nanoocp.gp.gp_Vec, V5: nanoocp.gp.gp_Vec) -> None: ...

    def Curve3d(self) -> nanoocp.Adaptor3d.Adaptor3d_Curve: ...

    def SetCurve2dOnSurf(self, Curve2d: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """loads a 2d curve associated the surface resulting of the constraints"""

    def Curve2dOnSurf(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """Returns a 2d curve associated the surface resulting of the constraints"""

    def SetProjectedCurve(self, Curve2d: nanoocp.Adaptor2d.Adaptor2d_Curve2d | None, TolU: float, TolV: float) -> None:
        """
        loads a 2d curve resulting from the normal projection of
        the curve on the initial surface
        """

    def ProjectedCurve(self) -> nanoocp.Adaptor2d.Adaptor2d_Curve2d:
        """
        Returns the projected curve resulting from the normal projection of the
        curve on the initial surface
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomPlate_PointConstraint(nanoocp.Standard.Standard_Transient):
    """Defines points as constraints to be used to deform a surface."""

    @overload
    def __init__(self, Pt: nanoocp.gp.gp_Pnt, Order: int, TolDist: float = 0.0001) -> None:
        """
        Constructs a point constraint object defined by Pt, a 3D point
        Order gives the order of constraint, one of:
        -   -1 i.e. none, or 0 i.e.G0 when assigned to Pt
        -   -1 i.e. none, 0 i.e. G0, 1 i.e. G1, 2 i.e. G2 when
        assigned to U, V and Surf.
        In this constructor, only TolDist is given.
        Distance tolerance represents the greatest distance
        allowed between the constraint and the target surface.
        Angular tolerance represents the largest angle allowed
        between the constraint and the target surface. Curvature
        tolerance represents the greatest difference in curvature
        allowed between the constraint and the target surface.
        Raises ConstructionError if Order is not 0 or -1
        """

    @overload
    def __init__(self, U: float, V: float, Surf: nanoocp.Geom.Geom_Surface | None, Order: int, TolDist: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1) -> None:
        """
        Constructs a point constraint object defined by
        the intersection point of U and V on the surface Surf.
        Order gives the order of constraint, one of:
        -   -1 i.e. none, or 0 i.e.G0 when assigned to Pt
        -   -1 i.e. none, 0 i.e. G0, 1 i.e. G1, 2 i.e. G2 when
        assigned to U, V and Surf.
        In this constructor the surface to be generated must
        respect several tolerance values only:
        -   the distance tolerance TolDist
        -   the angular tolerance TolAng
        -   the curvature tolerance, TolCurv.
        Distance tolerance represents the greatest distance
        allowed between the constraint and the target surface.
        Angular tolerance represents the largest angle allowed
        between the constraint and the target surface. Curvature
        tolerance represents the greatest difference in curvature
        allowed between the constraint and the target surface.Creates a punctual constraint.
        """

    @overload
    def __init__(self, theOther: GeomPlate_PointConstraint) -> None: ...

    def SetOrder(self, Order: int) -> None: ...

    def Order(self) -> int:
        """
        Returns the order of constraint: G0, G1, and G2,
        controlled respectively by G0Criterion G1Criterion and G2Criterion.
        """

    def SetG0Criterion(self, TolDist: float) -> None:
        """
        Allows you to set the G0 criterion. This is the law
        defining the greatest distance allowed between the
        constraint and the target surface. If this criterion is not
        set, {TolDist, the distance tolerance from the constructor, is used
        """

    def SetG1Criterion(self, TolAng: float) -> None:
        """
        Allows you to set the G1 criterion. This is the law
        defining the greatest angle allowed between the
        constraint and the target surface. If this criterion is not
        set, TolAng, the angular tolerance from the constructor, is used.
        Raises ConstructionError if the point is not on the surface
        """

    def SetG2Criterion(self, TolCurv: float) -> None:
        """
        Allows you to set the G2 criterion. This is the law
        defining the greatest difference in curvature allowed
        between the constraint and the target surface. If this
        criterion is not set, TolCurv, the curvature tolerance from
        the constructor, is used.
        Raises ConstructionError if the point is not on the surface
        """

    def G0Criterion(self) -> float:
        """
        Returns the G0 criterion. This is the greatest distance
        allowed between the constraint and the target surface.
        """

    def G1Criterion(self) -> float:
        """
        Returns the G1 criterion. This is the greatest angle
        allowed between the constraint and the target surface.
        Raises ConstructionError if the point is not on the surface.
        """

    def G2Criterion(self) -> float:
        """
        Returns the G2 criterion. This is the greatest difference
        in curvature allowed between the constraint and the target surface.
        Raises ConstructionError if the point is not on the surface
        """

    def D0(self, P: nanoocp.gp.gp_Pnt) -> None: ...

    def D1(self, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec) -> None: ...

    def D2(self, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec, V2: nanoocp.gp.gp_Vec, V3: nanoocp.gp.gp_Vec, V4: nanoocp.gp.gp_Vec, V5: nanoocp.gp.gp_Vec) -> None: ...

    def HasPnt2dOnSurf(self) -> bool: ...

    def SetPnt2dOnSurf(self, Pnt: nanoocp.gp.gp_Pnt2d) -> None: ...

    def Pnt2dOnSurf(self) -> nanoocp.gp.gp_Pnt2d: ...

    def LPropSurf(self) -> nanoocp.GeomLProp.GeomLProp_SLProps: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class GeomPlate_BuildPlateSurface:
    """
    This class provides an algorithm for constructing such a plate surface that
    it conforms to given curve and/or point constraints.
    The algorithm accepts or constructs an initial surface
    and looks for a deformation of it satisfying the
    constraints and minimizing energy input.
    A BuildPlateSurface object provides a framework for:
    -   defining or setting constraints
    -   implementing the construction algorithm
    -   consulting the result.
    """

    @overload
    def __init__(self, Degree: int = 3, NbPtsOnCur: int = 10, NbIter: int = 3, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, Anisotropie: bool = False) -> None:
        """
        Initializes the BuildPlateSurface framework for
        deforming plate surfaces using curve and point
        constraints. You use the first constructor if you have
        an initial surface to work with at construction time. If
        not, you use the second. You can add one later by
        using the method LoadInitSurface. If no initial
        surface is loaded, one will automatically be computed.
        The curve and point constraints will be defined by
        using the method Add.
        Before the call to the algorithm, the curve constraints
        will be transformed into sequences of discrete points.
        Each curve defined as a constraint will be given the
        value of NbPtsOnCur as the average number of points on it.
        Several arguments serve to improve performance of
        the algorithm. NbIter, for example, expresses the
        number of iterations allowed and is used to control the
        duration of computation. To optimize resolution,
        Degree will have the default value of 3.
        The surface generated must respect several tolerance values:
        -   2d tolerance given by Tol2d, with a default value of 0.00001
        -   3d tolerance expressed by Tol3d, with a default value of 0.0001
        -   angular tolerance given by TolAng, with a default
        value of 0.01, defining the greatest angle allowed
        between the constraint and the target surface.
        Exceptions
        Standard_ConstructionError if NbIter is less than 1 or Degree is less than 3.
        """

    @overload
    def __init__(self, Surf: nanoocp.Geom.Geom_Surface | None, Degree: int = 3, NbPtsOnCur: int = 10, NbIter: int = 3, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, Anisotropie: bool = False) -> None: ...

    @overload
    def __init__(self, NPoints: nanoocp.NCollection.NCollection_HArray1[int] | None, TabCurve: nanoocp.NCollection.NCollection_HArray1[nanoocp.Adaptor3d.Adaptor3d_Curve] | None, Tang: nanoocp.NCollection.NCollection_HArray1[int] | None, Degree: int, NbIter: int = 3, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, Anisotropie: bool = False) -> None:
        """
        Constructor compatible with the old version
        with this constructor the constraint are given in a Array of Curve on Surface
        The array NbPoints contains the number of points for each constraint.
        The Array Tang contains the order of constraint for each Constraint: The possible values for
        this order has to be -1 , 0 , 1 , 2 . Order i means constraint Gi. NbIter is the maximum
        number of iteration to optimise the number of points for resolution Degree is the degree of
        resolution for Plate Tol2d is the tolerance used to test if two points of different constraint
        are identical in the parametric space of the initial surface Tol3d is used to test if two
        identical points in the 2d space are identical in 3d space TolAng is used to compare the angle
        between normal of two identical points in the 2d space Raises ConstructionError;
        """

    def Init(self) -> None:
        """Resets all constraints"""

    def LoadInitSurface(self, Surf: nanoocp.Geom.Geom_Surface | None) -> None:
        """Loads the initial Surface"""

    @overload
    def Add(self, Cont: GeomPlate_CurveConstraint | None) -> None:
        """Adds the linear constraint cont."""

    @overload
    def Add(self, Cont: GeomPlate_PointConstraint | None) -> None:
        """Adds the point constraint cont."""

    def SetNbBounds(self, NbBounds: int) -> None: ...

    def Perform(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Calls the algorithm and computes the plate surface using
        the loaded constraints. If no initial surface is given, the
        algorithm automatically computes one.
        Exceptions
        Standard_RangeError if the value of the constraint is
        null or if plate is not done.
        """

    def CurveConstraint(self, order: int) -> GeomPlate_CurveConstraint:
        """returns the CurveConstraints of order order"""

    def PointConstraint(self, order: int) -> GeomPlate_PointConstraint:
        """returns the PointConstraint of order order"""

    def Disc2dContour(self, nbp: int, Seq2d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY]) -> None: ...

    def Disc3dContour(self, nbp: int, iordre: int, Seq3d: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XYZ]) -> None: ...

    def IsDone(self) -> bool:
        """Tests whether computation of the plate has been completed."""

    def Surface(self) -> GeomPlate_Surface:
        """
        Returns the result of the computation. This surface can
        then be used by GeomPlate_MakeApprox for
        converting the resulting surface into a BSpline.
        """

    def SurfInit(self) -> nanoocp.Geom.Geom_Surface:
        """Returns the initial surface"""

    def Sense(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Allows you to ensure that the array of curves returned by
        Curves2d has the correct orientation. Returns the
        orientation of the curves in the array returned by
        Curves2d. Computation changes the orientation of
        these curves. Consequently, this method returns the
        orientation prior to computation.
        """

    def Curves2d(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom2d.Geom2d_Curve]:
        """
        Extracts the array of curves on the plate surface which
        correspond to the curve constraints set in Add.
        """

    def Order(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Returns the order of the curves in the array returned by
        Curves2d. Computation changes this order.
        Consequently, this method returns the order of the
        curves prior to computation.
        """

    @overload
    def G0Error(self) -> float:
        """Returns the max distance between the result and the constraints"""

    @overload
    def G0Error(self, Index: int) -> float:
        """Returns the max distance between the result and the constraint Index"""

    @overload
    def G1Error(self) -> float:
        """Returns the max angle between the result and the constraints"""

    @overload
    def G1Error(self, Index: int) -> float:
        """Returns the max angle between the result and the constraint Index"""

    @overload
    def G2Error(self) -> float:
        """
        Returns the max difference of curvature between the result and the constraints
        """

    @overload
    def G2Error(self, Index: int) -> float:
        """
        Returns the max difference of curvature between the result and the constraint Index
        """

class GeomPlate_MakeApprox:
    """Allows you to convert a GeomPlate surface into a BSpline."""

    @overload
    def __init__(self, SurfPlate: GeomPlate_Surface | None, PlateCrit: nanoocp.AdvApp2Var.AdvApp2Var_Criterion, Tol3d: float, Nbmax: int, dgmax: int, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, EnlargeCoeff: float = 1.1) -> None:
        """
        Converts SurfPlate into a Geom_BSplineSurface with
        n Bezier pieces (n<=Nbmax) of degree <= dgmax
        and an approximation error < Tol3d if possible
        the criterion CritPlate is satisfied if possible
        """

    @overload
    def __init__(self, SurfPlate: GeomPlate_Surface | None, Tol3d: float, Nbmax: int, dgmax: int, dmax: float, CritOrder: int = 0, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1, EnlargeCoeff: float = 1.1) -> None:
        """
        Converts SurfPlate into a Geom_BSplineSurface with
        n Bezier pieces (n<=Nbmax) of degree <= dgmax
        and an approximation error < Tol3d if possible
        if CritOrder = -1 , no criterion is used
        if CritOrder = 0 , a PlateG0Criterion is used with max value > 10*dmax
        if CritOrder = 1 , a PlateG1Criterion is used with max value > 10*dmax
        WARNING : for CritOrder = 0 or 1, only the constraints points of SurfPlate
        are used to evaluate the value of the criterion
        """

    @overload
    def __init__(self, theOther: GeomPlate_MakeApprox) -> None: ...

    def Surface(self) -> nanoocp.Geom.Geom_BSplineSurface:
        """
        Returns the BSpline surface extracted from the
        GeomPlate_MakeApprox object.
        """

    def ApproxError(self) -> float:
        """
        Returns the error in computation of the approximation
        surface. This is the distance between the entire target
        BSpline surface and the entire original surface
        generated by BuildPlateSurface and converted by GeomPlate_Surface.
        """

    def CriterionError(self) -> float:
        """
        Returns the criterion error in computation of the
        approximation surface. This is estimated relative to the
        curve and point constraints only.
        """

class GeomPlate_PlateG0Criterion(nanoocp.AdvApp2Var.AdvApp2Var_Criterion):
    """this class contains a specific G0 criterion for GeomPlate_MakeApprox"""

    @overload
    def __init__(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY], G0Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XYZ], Maximum: float, Type: nanoocp.AdvApp2Var.AdvApp2Var_CriterionType = AdvApp2Var_CriterionType.AdvApp2Var_Absolute, Repart: nanoocp.AdvApp2Var.AdvApp2Var_CriterionRepartition = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomPlate_PlateG0Criterion) -> None: ...

    def Value(self, P: nanoocp.AdvApp2Var.AdvApp2Var_Patch, C: nanoocp.AdvApp2Var.AdvApp2Var_Context) -> None: ...

    def IsSatisfied(self, P: nanoocp.AdvApp2Var.AdvApp2Var_Patch) -> bool: ...

class GeomPlate_PlateG1Criterion(nanoocp.AdvApp2Var.AdvApp2Var_Criterion):
    """this class contains a specific G1 criterion for GeomPlate_MakeApprox"""

    @overload
    def __init__(self, Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY], G1Data: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XYZ], Maximum: float, Type: nanoocp.AdvApp2Var.AdvApp2Var_CriterionType = AdvApp2Var_CriterionType.AdvApp2Var_Absolute, Repart: nanoocp.AdvApp2Var.AdvApp2Var_CriterionRepartition = ...) -> None: ...

    @overload
    def __init__(self, theOther: GeomPlate_PlateG1Criterion) -> None: ...

    def Value(self, P: nanoocp.AdvApp2Var.AdvApp2Var_Patch, C: nanoocp.AdvApp2Var.AdvApp2Var_Context) -> None: ...

    def IsSatisfied(self, P: nanoocp.AdvApp2Var.AdvApp2Var_Patch) -> bool: ...

class GeomPlate_Surface(nanoocp.Geom.Geom_Surface):
    """
    Describes the characteristics of plate surface objects
    returned by BuildPlateSurface::Surface. These can be
    used to verify the quality of the resulting surface before
    approximating it to a Geom_BSpline surface generated
    by MakeApprox. This proves necessary in cases where
    you want to use the resulting surface as the support for
    a shape. The algorithmically generated surface cannot
    fill this function as is, and as a result must be converted first.
    """

    @overload
    def __init__(self, Surfinit: nanoocp.Geom.Geom_Surface | None, Surfinter: nanoocp.Plate.Plate_Plate) -> None: ...

    @overload
    def __init__(self, theOther: GeomPlate_Surface) -> None: ...

    def UReverse(self) -> None:
        """
        Reverses the U direction of parametrization of <me>.
        The bounds of the surface are not modified.
        """

    def UReversedParameter(self, U: float) -> float:
        """
        Return the parameter on the Ureversed surface for
        the point of parameter U on <me>.
        @code
        me->UReversed()->Value(me->UReversedParameter(U),V)
        @endcode
        is the same point as
        @code
        me->Value(U,V)
        @endcode
        """

    def VReverse(self) -> None:
        """
        Reverses the V direction of parametrization of <me>.
        The bounds of the surface are not modified.
        """

    def VReversedParameter(self, V: float) -> float:
        """
        Return the parameter on the Vreversed surface for
        the point of parameter V on <me>.
        @code
        me->VReversed()->Value(U,me->VReversedParameter(V))
        @endcode
        is the same point as
        @code
        me->Value(U,V)
        @endcode
        """

    def TransformParameters(self, T: nanoocp.gp.gp_Trsf) -> tuple[float, float]:
        """
        Computes the parameters on the transformed surface for
        the transform of the point of parameters U,V on <me>.
        @code
        me->Transformed(T)->Value(U',V')
        @endcode
        is the same point as
        @code
        me->Value(U,V).Transformed(T)
        @endcode
        Where U',V' are the new values of U,V after calling
        @code
        me->TransformParameters(U,V,T)
        @endcode
        This methods does not change <U> and <V>

        It can be redefined. For example on the Plane,
        Cylinder, Cone, Revolved and Extruded surfaces.
        """

    def ParametricTransformation(self, T: nanoocp.gp.gp_Trsf) -> nanoocp.gp.gp_GTrsf2d:
        """
        Returns a 2d transformation used to find the new
        parameters of a point on the transformed surface.
        @code
        me->Transformed(T)->Value(U',V')
        @endcode
        is the same point as
        @code
        me->Value(U,V).Transformed(T)
        @endcode
        Where U',V' are obtained by transforming U,V with
        the 2d transformation returned by
        @code
        me->ParametricTransformation(T)
        @endcode
        This method returns an identity transformation

        It can be redefined. For example on the Plane,
        Cylinder, Cone, Revolved and Extruded surfaces.
        """

    def Bounds(self) -> tuple[float, float, float, float]: ...

    def IsUClosed(self) -> bool:
        """
        Is the surface closed in the parametric direction U ?
        Returns True if for each parameter V the distance
        between the point P (UFirst, V) and P (ULast, V) is
        lower or equal to Resolution from gp. UFirst and ULast
        are the parametric bounds in the U direction.
        """

    def IsVClosed(self) -> bool:
        """
        Is the surface closed in the parametric direction V ?
        Returns True if for each parameter U the distance
        between the point P (U, VFirst) and P (U, VLast) is
        lower or equal to Resolution from gp. VFirst and VLast
        are the parametric bounds in the V direction.
        """

    def IsUPeriodic(self) -> bool:
        """
        Is the parametrization of a surface periodic in the
        direction U ?
        It is possible only if the surface is closed in this
        parametric direction and if the following relation is
        satisfied :
        for each parameter V the distance between the point
        P (U, V) and the point P (U + T, V) is lower or equal
        to Resolution from package gp. T is the parametric period
        and must be a constant.
        """

    def UPeriod(self) -> float:
        """
        returns the Uperiod.
        raises if the surface is not uperiodic.
        """

    def IsVPeriodic(self) -> bool:
        """
        Is the parametrization of a surface periodic in the
        direction U ?
        It is possible only if the surface is closed in this
        parametric direction and if the following relation is
        satisfied :
        for each parameter V the distance between the point
        P (U, V) and the point P (U + T, V) is lower or equal
        to Resolution from package gp. T is the parametric period
        and must be a constant.
        """

    def VPeriod(self) -> float:
        """
        returns the Vperiod.
        raises if the surface is not vperiodic.
        """

    def UIso(self, U: float) -> nanoocp.Geom.Geom_Curve:
        """Computes the U isoparametric curve."""

    def VIso(self, V: float) -> nanoocp.Geom.Geom_Curve:
        """Computes the V isoparametric curve."""

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Global Continuity of the surface in direction U and V :
        C0 : only geometric continuity,
        C1 : continuity of the first derivative all along the surface,
        C2 : continuity of the second derivative all along the surface,
        C3 : continuity of the third derivative all along the surface,
        G1 : tangency continuity all along the surface,
        G2 : curvature continuity all along the surface,
        CN : the order of continuity is infinite.
        Example :
        If the surface is C1 in the V parametric direction and C2
        in the U parametric direction Shape = C1.
        """

    def IsCNu(self, N: int) -> bool:
        """
        Returns the order of continuity of the surface in the
        U parametric direction.
        Raised if N < 0.
        """

    def IsCNv(self, N: int) -> bool:
        """
        Returns the order of continuity of the surface in the
        V parametric direction.
        Raised if N < 0.
        """

    def EvalD0(self, U: float, V: float) -> nanoocp.gp.gp_Pnt:
        """
        Computes the point of parameter U,V on the surface.

        Raised only for an "OffsetSurface" if it is not possible to
        compute the current point.
        """

    def EvalD1(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD1:
        """
        Computes the point P and the first derivatives in the
        directions U and V at this point.
        Raised if the continuity of the surface is not C1.
        """

    def EvalD2(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD2:
        """
        Computes the point P, the first and the second derivatives in
        the directions U and V at this point.
        Raised if the continuity of the surface is not C2.
        """

    def EvalD3(self, U: float, V: float) -> nanoocp.Geom.Geom_Surface.ResD3:
        """
        Computes the point P, the first,the second and the third
        derivatives in the directions U and V at this point.
        Raised if the continuity of the surface is not C2.
        """

    def EvalDN(self, U: float, V: float, Nu: int, Nv: int) -> nanoocp.gp.gp_Vec:
        """
        ---Purpose ;
        Computes the derivative of order Nu in the direction U and Nv
        in the direction V at the point P(U, V).

        Raised if the continuity of the surface is not CNu in the U
        direction or not CNv in the V direction.
        Raised if Nu + Nv < 1 or Nu < 0 or Nv < 0.
        """

    def Copy(self) -> nanoocp.Geom.Geom_Geometry: ...

    def Transform(self, T: nanoocp.gp.gp_Trsf) -> None:
        """
        Transformation of a geometric object. This transformation
        can be a translation, a rotation, a symmetry, a scaling
        or a complex transformation obtained by combination of
        the previous elementaries transformations.
        (see class Transformation of the package Geom).
        """

    def CallSurfinit(self) -> nanoocp.Geom.Geom_Surface: ...

    def SetBounds(self, Umin: float, Umax: float, Vmin: float, Vmax: float) -> None: ...

    def RealBounds(self) -> tuple[float, float, float, float]: ...

    def Constraints(self, Seq: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_XY]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.GeomPlate
GeomPlate_Array1OfHCurve = nanoocp.NCollection.NCollection_Array1[nanoocp.Adaptor3d.Adaptor3d_Curve]
GeomPlate_HArray1OfHCurve = nanoocp.NCollection.NCollection_HArray1[nanoocp.Adaptor3d.Adaptor3d_Curve]
GeomPlate_SequenceOfAij = nanoocp.NCollection.NCollection_Sequence[nanoocp.GeomPlate.GeomPlate_Aij]
