"""OCCT package IGESGeom (toolkit TKDEIGES)"""

from typing import overload

import nanoocp.IGESBasic
import nanoocp.IGESData
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class IGESGeom:
    """This package consists of B-Rep and CSG Solid entities"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom) -> None: ...

    @staticmethod
    def Init() -> None:
        """Prepares dynamic data (Protocol, Modules) for this package"""

    @staticmethod
    def Protocol() -> IGESGeom_Protocol:
        """Returns the Protocol for this Package"""

class IGESGeom_Boundary(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESBoundary, Type <141> Form <0>
    in package IGESGeom
    A boundary entity identifies a surface boundary consisting
    of a set of curves lying on the surface
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Boundary) -> None: ...

    def Init(self, aType: int, aPreference: int, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None, allModelCurves: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None, allSenses: nanoocp.NCollection.NCollection_HArray1[int] | None, allParameterCurves: nanoocp.IGESBasic.IGESBasic_HArray1OfHArray1OfIGESEntity | None) -> None:
        """
        This method is used to set the fields of the class
        Boundary
        - aType              : Type of bounded surface representation
        - aPreference        : Preferred representation of
        Trimming Curve
        - aSurface           : Untrimmed surface to be bounded
        - allModelCurves     : Model Space Curves
        - allSenses          : Orientation flags of all Model Space
        Curves
        - allParameterCurves : Parameter Space Curves
        raises exception if allSenses, allModelCurves and
        allParameterCurves do not have same dimensions
        """

    def BoundaryType(self) -> int:
        """
        returns type of bounded surface representation
        0 = Boundary entities may only reference model space trimming
        curves. Associated surface representation may be parametric
        1 = Boundary entities must reference model space curves and
        associated parameter space curve collections. Associated
        surface must be a parametric representation
        """

    def PreferenceType(self) -> int:
        """
        returns preferred representation of trimming curves
        0 = Unspecified
        1 = Model space
        2 = Parameter space
        3 = Representations are of equal preference
        """

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the surface to be bounded"""

    def NbModelSpaceCurves(self) -> int:
        """returns the number of model space curves"""

    def ModelSpaceCurve(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Model Space Curve
        raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """

    def Sense(self, Index: int) -> int:
        """
        returns the sense of a particular model space curve
        1 = model curve direction does not need reversal
        2 = model curve direction needs to be reversed
        raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """

    def NbParameterCurves(self, Index: int) -> int:
        """
        returns the number of parameter curves associated with one
        model space curve referred to by Index
        raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """

    def ParameterCurves(self, Index: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity]:
        """
        returns an array of parameter space curves associated with
        a model space curve referred to by the Index
        raises exception if Index <= 0 or Index > NbModelSpaceCurves()
        """

    def ParameterCurve(self, Index: int, Num: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns an individual parameter curve
        raises exception if Index or Num is out of range
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_BoundedSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines BoundedSurface, Type <143> Form <0>
    in package IGESGeom
    A bounded surface is used to communicate trimmed
    surfaces. The surface and trimming curves are assumed
    to be represented parametrically.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_BoundedSurface) -> None: ...

    def Init(self, aType: int, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None, allBounds: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_Boundary] | None) -> None:
        """
        This method is used to set the fields of the class
        BoundedSurface
        - aType     : Type of bounded surface representation
        - aSurface  : Surface entity to be bounded
        - allBounds : Array of boundary entities
        """

    def RepresentationType(self) -> int:
        """
        returns the type of Bounded surface representation
        0 = The boundary entities may only reference model space curves
        1 = The boundary entities may reference both model space curves
        and associated parameter space curve representations
        """

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the bounded surface"""

    def NbBoundaries(self) -> int:
        """returns the number of boundaries"""

    def Boundary(self, Index: int) -> IGESGeom_Boundary:
        """
        returns boundary entity
        raises exception if Index <= 0 or Index > NbBoundaries()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_BSplineCurve(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESBSplineCurve, Type <126> Form <0-5>
    in package IGESGeom
    A parametric equation obtained by dividing two summations
    involving weights (which are real numbers), the control
    points, and B-Spline basis functions
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_BSplineCurve) -> None: ...

    def Init(self, anIndex: int, aDegree: int, aPlanar: bool, aClosed: bool, aPolynom: bool, aPeriodic: bool, allKnots: nanoocp.NCollection.NCollection_HArray1[float] | None, allWeights: nanoocp.NCollection.NCollection_HArray1[float] | None, allPoles: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None, aUmin: float, aUmax: float, aNorm: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        BSplineCurve. Beware about indexation of arrays
        - anIndex      : Upper index of the sum
        - aDegree      : Degree of basis functions
        - aPlanar      : 0 = nonplanar curve, 1 = planar curve
        - aClosed      : 0 = open curve, 1 = closed curve
        - aPolynom     : 0 = rational, 1 = polynomial
        - aPeriodic    : 0 = nonperiodic, 1 = periodic
        - allKnots     : Knot sequence values [-Degree,Index+1]
        - allWeights   : Array of weights     [0,Index]
        - allPoles     : X, Y, Z coordinates of all control points
        [0,Index]
        - aUmin, aUmax : Starting and ending parameter values
        - aNorm        : Unit normal (if the curve is planar)
        raises exception if allWeights & allPoles are not of same size.
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Shape of the Curve)
        Error if not in range [0-5]
        """

    def UpperIndex(self) -> int:
        """returns the upper index of the sum (see Knots,Poles)"""

    def Degree(self) -> int:
        """returns the degree of basis functions"""

    def IsPlanar(self) -> bool:
        """returns True if the curve is Planar, False if non-planar"""

    def IsClosed(self) -> bool:
        """returns True if the curve is closed, False if open"""

    def IsPolynomial(self, flag: bool = False) -> bool:
        """
        returns True if the curve is polynomial, False if rational
        <flag> False (D) : computed from the list of weights
        (all must be equal)
        <flag> True : as recorded
        """

    def IsPeriodic(self) -> bool:
        """returns True if the curve is periodic, False otherwise"""

    def NbKnots(self) -> int:
        """returns the number of knots (i.e. Degree + UpperIndex + 2)"""

    def Knot(self, anIndex: int) -> float:
        """
        returns the knot referred to by anIndex,
        inside the range [-Degree,UpperIndex+1]
        raises exception if
        anIndex < -Degree() or anIndex > (NbKnots() - Degree())
        Note : Knots are numbered from -Degree (not from 1)
        """

    def NbPoles(self) -> int:
        """returns number of poles (i.e. UpperIndex + 1)"""

    def Weight(self, anIndex: int) -> float:
        """
        returns the weight referred to by anIndex, in [0,UpperIndex]
        raises exception if anIndex < 0 or anIndex > UpperIndex()
        """

    def Pole(self, anIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the pole referred to by anIndex, in [0,UpperIndex]
        raises exception if anIndex < 0 or anIndex > UpperIndex()
        """

    def TransformedPole(self, anIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the anIndex'th pole after applying Transf. Matrix
        raises exception if an Index < 0 or an Index > UpperIndex()
        """

    def UMin(self) -> float:
        """returns starting parameter value"""

    def UMax(self) -> float:
        """returns ending parameter value"""

    def Normal(self) -> nanoocp.gp.gp_XYZ:
        """if the curve is nonplanar then (0, 0, 0) is returned"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_BSplineSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESBSplineSurface, Type <128> Form <0-9>
    in package IGESGeom
    A parametric equation obtained by dividing two summations
    involving weights (which are real numbers), the control
    points, and B-Spline basis functions
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_BSplineSurface) -> None: ...

    def Init(self, anIndexU: int, anIndexV: int, aDegU: int, aDegV: int, aCloseU: bool, aCloseV: bool, aPolynom: bool, aPeriodU: bool, aPeriodV: bool, allKnotsU: nanoocp.NCollection.NCollection_HArray1[float] | None, allKnotsV: nanoocp.NCollection.NCollection_HArray1[float] | None, allWeights: nanoocp.NCollection.NCollection_HArray2[float] | None, allPoles: nanoocp.NCollection.NCollection_HArray2[nanoocp.gp.gp_XYZ] | None, aUmin: float, aUmax: float, aVmin: float, aVmax: float) -> None:
        """
        This method is used to set the fields of the class
        BSplineSurface
        - anIndexU             : Upper index of first sum
        - anIndexV             : Upper index of second sum
        - aDegU, aDegV         : Degrees of first and second sets
        of basis functions
        - aCloseU, aCloseV     : 1 = Closed in U, V directions
        0 = open in U, V directions
        - aPolynom             : 0 = Rational, 1 = polynomial
        - aPeriodU, aPeriodV   : 0 = Non periodic in U or V direction
        1 = Periodic in U or V direction
        - allKnotsU, allKnotsV : Knots in U and V directions
        - allWeights           : Array of weights
        - allPoles             : XYZ coordinates of all control points
        - aUmin                : Starting value of U direction
        - aUmax                : Ending value of U direction
        - aVmin                : Starting value of V direction
        - aVmax                : Ending value of V direction
        raises exception if allWeights & allPoles are not of same size.
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Shape of the Surface)
        Error if not in range [0-9]
        """

    def UpperIndexU(self) -> int:
        """returns the upper index of the first sum (U)"""

    def UpperIndexV(self) -> int:
        """returns the upper index of the second sum (V)"""

    def DegreeU(self) -> int:
        """returns degree of first set of basis functions"""

    def DegreeV(self) -> int:
        """returns degree of second set of basis functions"""

    def IsClosedU(self) -> bool:
        """True if closed in U direction else False"""

    def IsClosedV(self) -> bool:
        """True if closed in V direction else False"""

    def IsPolynomial(self, flag: bool = False) -> bool:
        """
        True if polynomial, False if rational
        <flag> False (D) : computed from Weights
        <flag> True : recorded
        """

    def IsPeriodicU(self) -> bool:
        """True if periodic in U direction else False"""

    def IsPeriodicV(self) -> bool:
        """True if periodic in V direction else False"""

    def NbKnotsU(self) -> int:
        """
        returns number of knots in U direction
        KnotsU are numbered from -DegreeU
        """

    def NbKnotsV(self) -> int:
        """
        returns number of knots in V direction
        KnotsV are numbered from -DegreeV
        """

    def KnotU(self, anIndex: int) -> float:
        """
        returns the value of knot referred to by anIndex in U direction
        raises exception if
        anIndex < -DegreeU() or anIndex > (NbKnotsU() - DegreeU())
        """

    def KnotV(self, anIndex: int) -> float:
        """
        returns the value of knot referred to by anIndex in V direction
        raises exception if
        anIndex < -DegreeV() or anIndex > (NbKnotsV() - DegreeV())
        """

    def NbPolesU(self) -> int:
        """returns number of poles in U direction"""

    def NbPolesV(self) -> int:
        """returns number of poles in V direction"""

    def Weight(self, anIndex1: int, anIndex2: int) -> float:
        """
        returns the weight referred to by anIndex1, anIndex2
        raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU()
        or if anIndex2 <= 0 or anIndex2 > NbPolesV()
        """

    def Pole(self, anIndex1: int, anIndex2: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the control point referenced by anIndex1, anIndex2
        raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU()
        or if anIndex2 <= 0 or anIndex2 > NbPolesV()
        """

    def TransformedPole(self, anIndex1: int, anIndex2: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the control point referenced by anIndex1, anIndex2
        after applying the Transf.Matrix
        raises exception if anIndex1 <= 0 or anIndex1 > NbPolesU()
        or if anIndex2 <= 0 or anIndex2 > NbPolesV()
        """

    def UMin(self) -> float:
        """returns starting value in the U direction"""

    def UMax(self) -> float:
        """returns ending value in the U direction"""

    def VMin(self) -> float:
        """returns starting value in the V direction"""

    def VMax(self) -> float:
        """returns ending value in the V direction"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_CircularArc(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESCircularArc, Type <100> Form <0>
    in package IGESGeom
    A circular arc is a connected portion of a parent circle
    which consists of more than one point. The definition space
    coordinate system is always chosen so that the circular arc
    remains in a plane either coincident with or parallel to
    the XT, YT plane.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_CircularArc) -> None: ...

    def Init(self, aZT: float, aCenter: nanoocp.gp.gp_XY, aStart: nanoocp.gp.gp_XY, anEnd: nanoocp.gp.gp_XY) -> None:
        """
        This method is used to set the fields of the class
        CircularArc
        - aZT     : Shift above the Z plane
        - aCenter : Center of the circle of which the arc forms a part
        - aStart  : Starting point of the circular arc
        - anEnd   : Ending point of the circular arc
        """

    def Center(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the center of the circle of which arc forms a part"""

    def TransformedCenter(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the center of the circle of which arc forms a part
        after applying Transf. Matrix
        """

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the start point of the arc"""

    def TransformedStartPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the start point of the arc after applying Transf. Matrix"""

    def ZPlane(self) -> float:
        """
        returns the parallel displacement of the plane containing the
        arc from the XT, YT plane
        """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the end point of the arc"""

    def TransformedEndPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the end point of the arc after applying Transf. Matrix"""

    def Radius(self) -> float:
        """returns the radius of the circle of which arc forms a part"""

    def Angle(self) -> float:
        """returns the angle subtended by the arc at the center in radians"""

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """Z-Axis of circle (i.e. [0,0,1])"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """Z-Axis after applying Trans. Matrix"""

    def IsClosed(self) -> bool:
        """True if StartPoint = EndPoint"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_CompositeCurve(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESCompositeCurve, Type <102> Form <0>
    in package IGESGeom
    A composite curve is defined as an ordered list of entities
    consisting of a point, connect point and parametrised curve
    entities (excluding the CompositeCurve entity).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_CompositeCurve) -> None: ...

    def Init(self, allEntities: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESData.IGESData_IGESEntity] | None) -> None:
        """
        This method is used to set the fields of the class
        CompositeCurve
        - allEntities : Constituent Entities of the composite curve
        """

    def NbCurves(self) -> int:
        """returns the number of curves contained in the CompositeCurve"""

    def Curve(self, Index: int) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Component of the CompositeCurve (a curve or a point)
        raises exception if Index <= 0 or Index > NbCurves()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_ConicArc(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESConicArc, Type <104> Form <0-3> in package IGESGeom
    A conic arc is a bounded connected portion of a parent
    conic curve which consists of more than one point. The
    parent conic curve is either an ellipse, a parabola, or
    a hyperbola. The definition space coordinate system is
    always chosen so that the conic arc lies in a plane either
    coincident with or parallel to XT, YT plane. Within such
    a plane a conic is defined by the six coefficients in the
    following equation.
    A*XT^2 + B*XT*YT + C*YT^2 + D*XT + E*YT + F = 0
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_ConicArc) -> None: ...

    def Init(self, A: float, B: float, C: float, D: float, E: float, F: float, ZT: float, aStart: nanoocp.gp.gp_XY, anEnd: nanoocp.gp.gp_XY) -> None:
        """
        This method is used to set the fields of the class
        ConicalArc
        - A, B, C, D, E, F : Coefficients of the equation
        defining conic arc
        - ZT               : Parallel ZT displacement of the arc
        from XT, YT plane.
        - aStart           : Starting point of the conic arc
        - anEnd            : End point of the conic arc
        """

    def OwnCorrect(self) -> bool:
        """
        sets the Form Number equal to ComputedFormNumber,
        returns True if changed
        """

    def ComputedFormNumber(self) -> int:
        """
        Computes the Form Number according to the equation
        1 for Ellipse, 2 for Hyperbola, 3 for Parabola
        """

    def Equation(self) -> tuple[float, float, float, float, float, float]: ...

    def ZPlane(self) -> float:
        """returns the Z displacement of the arc from XT, YT plane"""

    def StartPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the starting point of the arc"""

    def TransformedStartPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the starting point of the arc after applying
        Transf. Matrix
        """

    def EndPoint(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the end point of the arc"""

    def TransformedEndPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        returns the end point of the arc after applying
        Transf. Matrix
        """

    def IsFromEllipse(self) -> bool:
        """returns True if parent conic curve is an ellipse"""

    def IsFromParabola(self) -> bool:
        """returns True if parent conic curve is a parabola"""

    def IsFromHyperbola(self) -> bool:
        """returns True if parent conic curve is a hyperbola"""

    def IsClosed(self) -> bool:
        """returns True if StartPoint = EndPoint"""

    def Axis(self) -> nanoocp.gp.gp_Dir:
        """Z-Axis of conic (i.e. [0,0,1])"""

    def TransformedAxis(self) -> nanoocp.gp.gp_Dir:
        """Z-Axis after applying Trans. Matrix"""

    def Definition(self, Center: nanoocp.gp.gp_Pnt, MainAxis: nanoocp.gp.gp_Dir) -> tuple[float, float]:
        """
        Returns a Definition computed from equation, easier to use
        <Center> : the center of the conic (meaningless for
        a parabola) (defined with Z displacement)
        <MainAxis> : the Main Axis of the conic (for a Circle,
        arbitrary the X Axis)
        <Rmin,Rmax> : Minor and Major Radii of the conic
        For a Circle, Rmin = Rmax,
        For a Parabola, Rmin = Rmax = the Focal
        Warning : the basic definition (by equation) is not very stable,
        limit cases may be approximative
        """

    def TransformedDefinition(self, Center: nanoocp.gp.gp_Pnt, MainAxis: nanoocp.gp.gp_Dir) -> tuple[float, float]:
        """
        Same as Definition, but the Location is applied on the
        Center and the MainAxis
        """

    def ComputedDefinition(self) -> tuple[float, float, float, float, float, float]:
        """
        Computes and returns the coordinates of the definition of
        a comic from its equation. Used by Definition &
        TransformedDefinition, or may be called directly if needed
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_CopiousData(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESCopiousData, Type <106> Form <1-3,11-13,63>
    in package IGESGeom
    This entity stores data points in the form of pairs,
    triples, or sextuples. An interpretation flag value
    signifies which of these forms is being used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_CopiousData) -> None: ...

    def Init(self, aDataType: int, aZPlane: float, allData: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """
        This method is used to set the fields of the class
        CopiousData
        - aDataType : Specifies whether data is a pair or a triple
        or a sextuple.
        - aZPlane   : Common Z value for all points if datatype = 1
        - allData   : Data to be read in groups of 2, 3 or 6
        """

    def SetPolyline(self, mode: bool) -> None:
        """
        Sets Copious Data to be a Polyline if <mode> is True
        (Form = 11-12-13) or a Set of Points else (Form 1-2-3)
        """

    def SetClosedPath2D(self) -> None:
        """
        Sets Copious Data to be a Closed Path 2D (Form 63)
        Warning : DataType is not checked and must be set to ONE by Init
        """

    def IsPointSet(self) -> bool:
        """Returns True if <me> is a Set of Points (Form 1-2-3)"""

    def IsPolyline(self) -> bool:
        """Returns True if <me> is a Polyline (Form 11-12-13)"""

    def IsClosedPath2D(self) -> bool:
        """Returns True if <me> is a Closed Path 2D (Form 63)"""

    def DataType(self) -> int:
        """
        returns data type
        1 = XY ( with common Z given by plane)
        2 = XYZ ( point)
        3 = XYZ + Vec(XYZ) (point + normal vector)
        """

    def NbPoints(self) -> int:
        """returns the number of tuples"""

    def Data(self, NumPoint: int, NumData: int) -> float:
        """
        Returns an individual Data, given the N0 of the Point
        and the B0 of the Coordinate (according DataType)
        """

    def ZPlane(self) -> float:
        """
        If datatype = 1, then returns common z value for all data
        else returns 0
        """

    def Point(self, anIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the coordinates of the point specified by the anIndex
        raises exception if anIndex <= 0 or anIndex > NbPoints()
        """

    def TransformedPoint(self, anIndex: int) -> nanoocp.gp.gp_Pnt:
        """
        returns the coordinates of the point specified by the anIndex
        after applying Transf. Matrix
        raises exception if anIndex <= 0 or anIndex > NbPoints()
        """

    def Vector(self, anIndex: int) -> nanoocp.gp.gp_Vec:
        """
        returns i, j, k values if 3-tuple else returns (0, 0, 0)
        raises exception if anIndex <= 0 or anIndex > NbPoints()
        """

    def TransformedVector(self, anIndex: int) -> nanoocp.gp.gp_Vec:
        """
        returns transformed vector if 3-tuple else returns (0, 0, 0)
        raises exception if anIndex <= 0 or anIndex > NbPoints()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_CurveOnSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESCurveOnSurface, Type <142> Form <0>
    in package IGESGeom
    A curve on a parametric surface entity associates a given
    curve with a surface and identifies the curve as lying on
    the surface.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_CurveOnSurface) -> None: ...

    def Init(self, aMode: int, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None, aCurveUV: nanoocp.IGESData.IGESData_IGESEntity | None, aCurve3D: nanoocp.IGESData.IGESData_IGESEntity | None, aPreference: int) -> None:
        """
        This method is used to set the fields of the class
        CurveOnSurface
        - aMode       : Way the curve on the surface has been created
        - aSurface    : Surface on which the curve lies
        - aCurveUV    : Curve S (UV)
        - aCurve3D    : Curve C (3D)
        - aPreference : 0 = Unspecified
        1 = S o B is preferred
        2 = C is preferred
        3 = C and S o B are equally preferred
        """

    def CreationMode(self) -> int:
        """
        returns the mode in which the curve is created on the surface
        0 = Unspecified
        1 = Projection of a given curve on the surface
        2 = Intersection of two surfaces
        3 = Isoparametric curve, i.e:- either a `u` parametric
        or a `v` parametric curve
        """

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the surface on which the curve lies"""

    def CurveUV(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns curve S"""

    def Curve3D(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns curve C"""

    def PreferenceMode(self) -> int:
        """
        returns preference mode
        0 = Unspecified
        1 = S o B is preferred
        2 = C is preferred
        3 = C and S o B are equally preferred
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Direction(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESDirection, Type <123> Form <0>
    in package IGESGeom
    A direction entity is a non-zero vector in Euclidean 3-space
    that is defined by its three components (direction ratios)
    with respect to the coordinate axes. If x, y, z are the
    direction ratios then (x^2 + y^2 + z^2) > 0
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Direction) -> None: ...

    def Init(self, aDirection: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        Direction
        - aDirection : Direction ratios, Z is 0 by default
        """

    def Value(self) -> nanoocp.gp.gp_Vec: ...

    def TransformedValue(self) -> nanoocp.gp.gp_Vec:
        """returns the Direction value after applying Transformation matrix"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Flash(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESFlash, Type <125> Form <0 - 4>
    in package IGESGeom
    A flash entity is a point in the ZT=0 plane that locates
    a particular closed area. That closed area can be defined
    in one of two ways. First, it can be an arbitrary closed
    area defined by any entity capable of defining a closed
    area. The points of this entity must all lie in the ZT=0
    plane. Second, it can be a member of a predefined set of
    flash shapes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Flash) -> None: ...

    def Init(self, aPoint: nanoocp.gp.gp_XY, aDim: float, anotherDim: float, aRotation: float, aReference: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        This method is used to set the fields of the class Flash
        - aPoint     : Reference of flash
        - aDim       : First flash sizing parameter
        - anotherDim : Second flash sizing parameter
        - aRotation  : Rotation of flash about reference point
        in radians
        - aReference : Pointer to the referenced entity or Null
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Nature of the Flash :
        0 Unspecified, then given by Reference, 1->4 various
        Specialisations (Circle,Rectangle, etc...) )
        Error if not in range [0-4]
        """

    def ReferencePoint(self) -> nanoocp.gp.gp_Pnt2d:
        """returns the referenced point, Z = 0 always"""

    def TransformedReferencePoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the referenced point after applying Transf. Matrix"""

    def Dimension1(self) -> float:
        """returns first flash sizing parameter"""

    def Dimension2(self) -> float:
        """returns second flash sizing parameter"""

    def Rotation(self) -> float:
        """
        returns the angle in radians of the rotation of flash about the
        reference point
        """

    def ReferenceEntity(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the referenced entity or Null handle."""

    def HasReferenceEntity(self) -> bool:
        """returns True if referenced entity is present."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_GeneralModule(nanoocp.IGESData.IGESData_GeneralModule):
    """
    Definition of General Services for IGESGeom (specific part)
    This Services comprise : Shared & Implied Lists, Copy, Check
    """

    @overload
    def __init__(self) -> None:
        """Creates a GeneralModule from IGESGeom and puts it into GeneralLib"""

    @overload
    def __init__(self, theOther: IGESGeom_GeneralModule) -> None: ...

    def OwnSharedCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a given IGESEntity <ent>, from
        its specific parameters : specific for each type
        """

    def DirChecker(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """
        Returns a DirChecker, specific for each type of Entity
        (identified by its Case Number) : this DirChecker defines
        constraints which must be respected by the DirectoryPart
        """

    def OwnCheckCase(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check for each type of Entity"""

    def NewVoid(self, CN: int) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """Specific creation of a new void entity"""

    def OwnCopyCase(self, CN: int, entfrom: nanoocp.IGESData.IGESData_IGESEntity | None, entto: nanoocp.IGESData.IGESData_IGESEntity | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies parameters which are specific of each Type of Entity"""

    def CategoryNumber(self, CN: int, ent: nanoocp.Standard.Standard_Transient | None, shares: nanoocp.Interface.Interface_ShareTool) -> int:
        """
        Returns a category number which characterizes an entity
        Shape for all, but Drawing for :
        Flash; Point with a symbol; Plane with a symbol
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Line(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESLine, Type <110> Form <0>
    in package IGESGeom
    A line is a bounded, connected portion of a parent straight
    line which consists of more than one point. A line is
    defined by its end points.

    From IGES-5.3, two other Forms are admitted (same params) :
    0 remains for standard limited line (the default)
    1 for semi-infinite line (End is just a passing point)
    2 for full infinite Line (both Start and End are arbitrary)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Line) -> None: ...

    def Init(self, aStart: nanoocp.gp.gp_XYZ, anEnd: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class Line
        - aStart : Start point of the line
        - anEnd  : End point of the line
        """

    def Infinite(self) -> int:
        """Returns the Infinite status i.e. the Form Number : 0 1 2"""

    def SetInfinite(self, status: int) -> None:
        """
        Sets the Infinite status
        Does nothing if <status> is not 0 1 or 2
        """

    def StartPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the start point of the line"""

    def TransformedStartPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the start point of the line after applying Transf. Matrix"""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the end point of the line"""

    def TransformedEndPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns the end point of the line after applying Transf. Matrix"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_OffsetCurve(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESOffsetCurve, Type <130> Form <0>
    in package IGESGeom
    An OffsetCurve entity contains the data necessary to
    determine the offset of a given curve C. This entity
    points to the base curve to be offset and contains
    offset distance and other pertinent information.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_OffsetCurve) -> None: ...

    def Init(self, aBaseCurve: nanoocp.IGESData.IGESData_IGESEntity | None, anOffsetType: int, aFunction: nanoocp.IGESData.IGESData_IGESEntity | None, aFunctionCoord: int, aTaperedOffsetType: int, offDistance1: float, arcLength1: float, offDistance2: float, arcLength2: float, aNormalVec: nanoocp.gp.gp_XYZ, anOffsetParam: float, anotherOffsetParam: float) -> None:
        """
        This method is used to set the fields of the class
        OffsetCurve
        - aBaseCurve         : The curve entity to be offset
        - anOffsetType       : Offset distance flag
        1 = Single value, uniform distance
        2 = Varying linearly
        3 = As a specified function
        - aFunction          : Curve entity, one coordinate of which
        describes offset as a function of its
        parameter (0 unless OffsetType = 3)
        - aFunctionCoord     : Particular coordinate of curve
        describing offset as function of its
        parameters. (used if OffsetType = 3)
        - aTaperedOffsetType : Tapered offset type flag
        1 = Function of arc length
        2 = Function of parameter
        (Only used if OffsetType = 2 or 3)
        - offDistance1       : First offset distance
        (Only used if OffsetType = 1 or 2)
        - arcLength1         : Arc length or parameter value of
        first offset distance
        (Only used if OffsetType = 2)
        - offDistance2       : Second offset distance
        - arcLength2         : Arc length or parameter value of
        second offset distance
        (Only used if OffsetType = 2)
        - aNormalVec         : Unit vector normal to plane containing
        curve to be offset
        - anOffsetParam      : Start parameter value of offset curve
        - anotherOffsetParam : End parameter value of offset curve
        """

    def BaseCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the curve to be offset"""

    def OffsetType(self) -> int:
        """
        returns the offset distance flag
        1 = Single value offset (uniform distance)
        2 = Offset distance varying linearly
        3 = Offset distance specified as a function
        """

    def Function(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns the function defining the offset if at all the offset
        is described as a function or Null Handle.
        """

    def HasFunction(self) -> bool:
        """returns True if function defining the offset is present."""

    def FunctionParameter(self) -> int:
        """
        returns particular coordinate of the curve which describes offset
        as a function of its parameters. (only used if OffsetType() = 3)
        """

    def TaperedOffsetType(self) -> int:
        """
        returns tapered offset type flag (only used if OffsetType() = 2 or 3)
        1 = Function of arc length
        2 = Function of parameter
        """

    def FirstOffsetDistance(self) -> float:
        """returns first offset distance (only used if OffsetType() = 1 or 2)"""

    def ArcLength1(self) -> float:
        """
        returns arc length or parameter value (depending on value of
        offset distance flag) of first offset distance
        (only used if OffsetType() = 2)
        """

    def SecondOffsetDistance(self) -> float:
        """returns the second offset distance"""

    def ArcLength2(self) -> float:
        """
        returns arc length or parameter value (depending on value of
        offset distance flag) of second offset distance
        (only used if OffsetType() = 2)
        """

    def NormalVector(self) -> nanoocp.gp.gp_Vec:
        """returns unit vector normal to plane containing curve to be offset"""

    def TransformedNormalVector(self) -> nanoocp.gp.gp_Vec:
        """
        returns unit vector normal to plane containing curve to be offset
        after applying Transf. Matrix
        """

    def Parameters(self) -> tuple[float, float]: ...

    def StartParameter(self) -> float:
        """returns Start Parameter value of the offset curve"""

    def EndParameter(self) -> float:
        """returns End   Parameter value of the offset curve"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_OffsetSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESOffsetSurface, Type <140> Form <0>
    in package IGESGeom
    An offset surface is a surface defined in terms of an
    already existing surface.If S(u, v) is a parametrised
    regular surface and N(u, v) is a differential field of
    unit normal vectors defined on the whole surface, and
    "d" a fixed non zero real number, then offset surface
    to S is a parametrised surface S(u, v) given by
    O(u, v) = S(u, v) + d * N(u, v);
    u1 <= u <= u2; v1 <= v <= v2;
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_OffsetSurface) -> None: ...

    def Init(self, anIndicatoR: nanoocp.gp.gp_XYZ, aDistance: float, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None) -> None:
        """
        This method is used to set the fields of the class
        OffsetSurface
        - anIndicator : Offset indicator
        - aDistance   : Offset distance
        - aSurface    : Surface that is offset
        """

    def OffsetIndicator(self) -> nanoocp.gp.gp_Vec:
        """returns the offset indicator"""

    def TransformedOffsetIndicator(self) -> nanoocp.gp.gp_Vec:
        """returns the offset indicator after applying Transf. Matrix"""

    def Distance(self) -> float:
        """returns the distance by which surface is offset"""

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the surface that has been offset"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Plane(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESPlane, Type <108> Form <-1,0,1>
    in package IGESGeom
    A plane entity can be used to represent unbounded plane,
    as well as bounded portion of a plane. In either of the
    above cases the plane is defined within definition space
    by means of coefficients A, B, C, D where at least one of
    A, B, C is non-zero and A * XT + B * YT + C * ZT = D
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Plane) -> None: ...

    def Init(self, A: float, B: float, C: float, D: float, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, attach: nanoocp.gp.gp_XYZ, aSize: float) -> None: ...

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Type of Bound :
        0 no Bound, 1 (External) Bound, -1 Hole)
        Remark that Init keeps this Value and must be consistent :
        aCurve Null if FormNumber = 0, Non-Null else
        Error if not in ranges [0-1] or [10-12]
        """

    def Equation(self) -> tuple[float, float, float, float]: ...

    def TransformedEquation(self) -> tuple[float, float, float, float]: ...

    def HasBoundingCurve(self) -> bool:
        """returns True if there exists a bounding curve"""

    def HasBoundingCurveHole(self) -> bool:
        """returns True if bounding curve exists and bounded portion is negative"""

    def BoundingCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """
        returns Optional Bounding Curve, can be positive (normal clipping)
        or negative (hole) according to Form Number
        """

    def HasSymbolAttach(self) -> bool:
        """returns True if SymbolSize() > 0, False if SymbolSize() = 0"""

    def SymbolAttach(self) -> nanoocp.gp.gp_Pnt:
        """returns (X, Y, Z) if symbol exists else returns (0, 0, 0)"""

    def TransformedSymbolAttach(self) -> nanoocp.gp.gp_Pnt:
        """
        returns (X, Y, Z) if symbol exists after applying Transf. Matrix
        else returns (0, 0, 0)
        """

    def SymbolSize(self) -> float:
        """Size of optional display symbol"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Point(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESPoint, Type <116> Form <0>
    in package IGESGeom
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Point) -> None: ...

    def Init(self, aPoint: nanoocp.gp.gp_XYZ, aSymbol: nanoocp.IGESBasic.IGESBasic_SubfigureDef | None) -> None:
        """
        This method is used to set the fields of the class Point
        - aPoint  : Coordinates of point
        - aSymbol : SubfigureDefinition entity specifying the
        display symbol if there exists one, or zero
        """

    def Value(self) -> nanoocp.gp.gp_Pnt:
        """returns coordinates of the point"""

    def TransformedValue(self) -> nanoocp.gp.gp_Pnt:
        """returns coordinates of the point after applying Transf. Matrix"""

    def HasDisplaySymbol(self) -> bool:
        """returns True if symbol exists"""

    def DisplaySymbol(self) -> nanoocp.IGESBasic.IGESBasic_SubfigureDef:
        """returns display symbol entity if it exists"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_Protocol(nanoocp.IGESData.IGESData_Protocol):
    """Description of Protocol for IGESGeom"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_Protocol) -> None: ...

    def NbResources(self) -> int:
        """
        Gives the count of Resource Protocol. Here, one
        (Protocol from IGESBasic)
        """

    def Resource(self, num: int) -> nanoocp.Interface.Interface_Protocol:
        """Returns a Resource, given a rank."""

    def TypeNumber(self, atype: nanoocp.Standard.Standard_Type | None) -> int:
        """
        Returns a Case Number, specific of each recognized Type
        This Case Number is then used in Libraries : the various
        Modules attached to this class of Protocol must use them
        in accordance (for a given value of TypeNumber, they must
        consider the same Type as the Protocol defines)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_ReadWriteModule(nanoocp.IGESData.IGESData_ReadWriteModule):
    """
    Defines Geom File Access Module for IGESGeom (specific parts)
    Specific actions concern : Read and Write Own Parameters of
    an IGESEntity.
    """

    @overload
    def __init__(self) -> None:
        """Creates a ReadWriteModule & puts it into ReaderLib & WriterLib"""

    @overload
    def __init__(self, theOther: IGESGeom_ReadWriteModule) -> None: ...

    def CaseIGES(self, typenum: int, formnum: int) -> int:
        """Defines Case Numbers for Entities of IGESGeom"""

    def ReadOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """Reads own parameters from file for an Entity of IGESGeom"""

    def WriteOwnParams(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_RuledSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESRuledSurface, Type <118> Form <0-1>
    in package IGESGeom
    A ruled surface is formed by moving a line connecting points
    of equal relative arc length or equal relative parametric
    value on two parametric curves from a start point to a
    terminate point on the curves. The parametric curves may be
    points, lines, circles, conics, rational B-splines,
    parametric splines or any parametric curve defined in
    the IGES specification.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_RuledSurface) -> None: ...

    def Init(self, aCurve: nanoocp.IGESData.IGESData_IGESEntity | None, anotherCurve: nanoocp.IGESData.IGESData_IGESEntity | None, aDirFlag: int, aDevFlag: int) -> None:
        """
        This method is used to set the fields of the class
        RuledSurface
        - aCurve       : First parametric curve
        - anotherCurve : Second parametric curve
        - aDirFlag     : Direction Flag
        0 = Join first to first, last to last
        1 = Join first to last, last to first
        - aDevFlag     : Developable Surface Flag
        1 = Developable
        0 = Possibly not
        """

    def SetRuledByParameter(self, mode: bool) -> None:
        """
        Sets <me> to be Ruled by Parameter (Form 1) if <mode> is
        True, or Ruled by Length (Form 0) else
        """

    def IsRuledByParameter(self) -> bool:
        """Returns True if Form is 1"""

    def FirstCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the first curve"""

    def SecondCurve(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the second curve"""

    def DirectionFlag(self) -> int:
        """
        return the sense of direction
        0 = Join first to first, last to last
        1 = Join first to last, last to first
        """

    def IsDevelopable(self) -> bool:
        """returns True if developable else False"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_SpecificModule(nanoocp.IGESData.IGESData_SpecificModule):
    """
    Defines Services attached to IGES Entities :
    Dump & OwnCorrect, for IGESGeom
    """

    @overload
    def __init__(self) -> None:
        """Creates a SpecificModule from IGESGeom & puts it into SpecificLib"""

    @overload
    def __init__(self, theOther: IGESGeom_SpecificModule) -> None: ...

    def OwnDump(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Specific Dump (own parameters) for IGESGeom"""

    def OwnCorrect(self, CN: int, ent: nanoocp.IGESData.IGESData_IGESEntity | None) -> bool:
        """
        Performs non-ambiguous Correction on Entities which support
        them (Boundary,ConicArc,Flash,OffsetCurve,TransformationMatrix)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_SplineCurve(nanoocp.IGESData.IGESData_IGESEntity):
    """
    Defines IGESSplineCurve, Type <112> Form <0>
    in package IGESGeom
    The parametric spline is a sequence of parametric
    polynomial segments. The curve could be of the type
    Linear, Quadratic, Cubic, Wilson-Fowler, Modified
    Wilson-Fowler, B-Spline. The N polynomial segments
    are delimited by the break points:
    T(1), T(2), T(3), ..., T(N+1).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_SplineCurve) -> None: ...

    def Init(self, aType: int, aDegree: int, nbDimensions: int, allBreakPoints: nanoocp.NCollection.NCollection_HArray1[float] | None, allXPolynomials: nanoocp.NCollection.NCollection_HArray2[float] | None, allYPolynomials: nanoocp.NCollection.NCollection_HArray2[float] | None, allZPolynomials: nanoocp.NCollection.NCollection_HArray2[float] | None, allXvalues: nanoocp.NCollection.NCollection_HArray1[float] | None, allYvalues: nanoocp.NCollection.NCollection_HArray1[float] | None, allZvalues: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """
        This method is used to set the fields of the class
        SplineCurve
        - aType           : Spline Type
        1 = Linear
        2 = Quadratic
        3 = Cubic
        4 = Wilson-Fowler
        5 = Modified Wilson-Fowler
        6 = B Spline
        - aDegree         : Degree of continuity w.r.t. arc length
        - nbDimensions    : Number of dimensions
        2 = Planar
        3 = Non-planar
        - allBreakPoints  : Array of break points
        - allXPolynomials : X coordinate polynomials of segments
        - allYPolynomials : Y coordinate polynomials of segments
        - allZPolynomials : Z coordinate polynomials of segments
        - allXValues      : Values of 1st, 2nd, 3rd derivatives of
        X polynomials at the terminate point
        and values of X at terminate point
        - allYValues      : Values of 1st, 2nd, 3rd derivatives of
        Y polynomials at the terminate point
        and values of Y at terminate point
        - allZvalues      : Values of 1st, 2nd, 3rd derivatives of
        Z polynomials at the terminate point
        and values of Z at terminate point
        raises exception if allXPolynomials, allYPolynomials
        & allZPolynomials are not of same size OR allXValues, allYValues
        & allZValues are not of size 4
        """

    def SplineType(self) -> int:
        """returns the type of Spline curve"""

    def Degree(self) -> int:
        """returns the degree of the curve"""

    def NbDimensions(self) -> int:
        """
        returns the number of dimensions
        2 = Planar
        3 = Non-planar
        """

    def NbSegments(self) -> int:
        """returns the number of segments"""

    def BreakPoint(self, Index: int) -> float:
        """
        returns breakpoint of piecewise polynomial
        raises exception if Index <= 0 or Index > NbSegments() + 1
        """

    def XCoordPolynomial(self, Index: int) -> tuple[float, float, float, float]:
        """
        returns X coordinate polynomial for segment referred to by Index
        raises exception if Index <= 0 or Index > NbSegments()
        """

    def YCoordPolynomial(self, Index: int) -> tuple[float, float, float, float]:
        """
        returns Y coordinate polynomial for segment referred to by Index
        raises exception if Index <= 0 or Index > NbSegments()
        """

    def ZCoordPolynomial(self, Index: int) -> tuple[float, float, float, float]:
        """
        returns Z coordinate polynomial for segment referred to by Index
        raises exception if Index <= 0 or Index > NbSegments()
        """

    def XValues(self) -> tuple[float, float, float, float]:
        """
        returns the value of X polynomial, the values of 1st, 2nd and
        3rd derivatives of the X polynomial at the terminate point
        """

    def YValues(self) -> tuple[float, float, float, float]:
        """
        returns the value of Y polynomial, the values of 1st, 2nd and
        3rd derivatives of the Y polynomial at the termminate point
        """

    def ZValues(self) -> tuple[float, float, float, float]:
        """
        returns the value of Z polynomial, the values of 1st, 2nd and
        3rd derivatives of the Z polynomial at the termminate point
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_SplineSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESSplineSurface, Type <114> Form <0>
    in package IGESGeom
    A parametric spline surface is a grid of polynomial
    patches. Patch could be of the type Linear, Quadratic,
    Cubic, Wilson-Fowler, Modified Wilson-Fowler, B-Spline
    The M * N grid of patches is defined by the 'u' break
    points TU(1), TU(2), ..., TU(M+1) and the 'v' break
    points TV(1), TV(2), TV(3) ..., TV(N+1).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_SplineSurface) -> None: ...

    def Init(self, aBoundaryType: int, aPatchType: int, allUBreakpoints: nanoocp.NCollection.NCollection_HArray1[float] | None, allVBreakpoints: nanoocp.NCollection.NCollection_HArray1[float] | None, allXCoeffs: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]] | None, allYCoeffs: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]] | None, allZCoeffs: nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]] | None) -> None:
        """
        This method is used to set the fields of the class
        SplineSurface
        - aBoundaryType   : Type of Spline boundary
        1 = Linear
        2 = Quadratic
        3 = Cubic
        4 = Wilson-Fowler
        5 = Modified Wilson-Fowler
        6 = B-spline
        - aPatchType      : Type of patch contained in the grid
        1 = Cartesian Product
        0 = Unspecified
        - allUBreakpoints : u values of grid lines
        - allVBreakpoints : v values of grid lines
        - allXCoeffs      : X coefficients of M x N patches
        - allYCoeffs      : Y coefficients of M x N patches
        - allZCoeffs      : Z coefficients of M x N patches
        raises exception if allXCoeffs, allYCoeffs & allZCoeffs are not
        of the same size.
        or if the size of each element of the double array is not 16
        """

    def NbUSegments(self) -> int:
        """returns the number of U segments"""

    def NbVSegments(self) -> int:
        """returns the number of V segments"""

    def BoundaryType(self) -> int:
        """returns boundary type"""

    def PatchType(self) -> int:
        """returns patch type"""

    def UBreakPoint(self, anIndex: int) -> float:
        """
        returns U break point of the grid line referred to by anIndex
        raises exception if anIndex <= 0 or anIndex > NbUSegments() + 1
        """

    def VBreakPoint(self, anIndex: int) -> float:
        """
        returns V break point of the grid line referred to by anIndex
        raises exception if anIndex <= 0 or anIndex > NbVSegments() + 1
        """

    def XPolynomial(self, anIndex1: int, anIndex2: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        returns X polynomial of patch referred to by anIndex1, anIndex2
        raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments()
        or anIndex2 <= 0 or anIndex2 > NbVSegments()
        """

    def YPolynomial(self, anIndex1: int, anIndex2: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        returns Y polynomial of patch referred to by anIndex1, anIndex2
        raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments()
        or anIndex2 <= 0 or anIndex2 > NbVSegments()
        """

    def ZPolynomial(self, anIndex1: int, anIndex2: int) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        returns Z polynomial of patch referred to by anIndex1, anIndex2
        raises exception if anIndex1 <= 0 or anIndex1 > NbUSegments()
        or anIndex2 <= 0 or anIndex2 > NbVSegments()
        """

    def Polynomials(self) -> tuple[nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]], nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]], nanoocp.NCollection.NCollection_HArray2[nanoocp.NCollection.NCollection_HArray1[float]]]:
        """
        returns in one all the polynomial values "in bulk"
        useful for massive treatments
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_SurfaceOfRevolution(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESSurfaceOfRevolution, Type <120> Form <0>
    in package IGESGeom
    A surface of revolution is defined by an axis of rotation
    a generatrix, and start and terminate rotation angles. The
    surface is created by rotating the generatrix about the axis
    of rotation through the start and terminate rotation angles.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_SurfaceOfRevolution) -> None: ...

    def Init(self, anAxis: IGESGeom_Line | None, aGeneratrix: nanoocp.IGESData.IGESData_IGESEntity | None, aStartAngle: float, anEndAngle: float) -> None:
        """
        This method is used to set the fields of the class Line
        - anAxis      : Axis of revolution
        - aGeneratrix : The curve which is revolved about the axis
        - aStartAngle : Start angle of the surface of revolution
        - anEndAngle  : End angle of the surface of revolution
        """

    def AxisOfRevolution(self) -> IGESGeom_Line:
        """returns the axis of revolution"""

    def Generatrix(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the curve which is revolved about the axis"""

    def StartAngle(self) -> float:
        """returns start angle of revolution"""

    def EndAngle(self) -> float:
        """returns end angle of revolution"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_TabulatedCylinder(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESTabulatedCylinder, Type <122> Form <0>
    in package IGESGeom
    A tabulated cylinder is a surface formed by moving a line
    segment called generatrix parallel to itself along a curve
    called directrix. The curve may be a line, circular arc,
    conic arc, parametric spline curve, rational B-spline
    curve or composite curve.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_TabulatedCylinder) -> None: ...

    def Init(self, aDirectrix: nanoocp.IGESData.IGESData_IGESEntity | None, anEnd: nanoocp.gp.gp_XYZ) -> None:
        """
        This method is used to set the fields of the class
        TabulatedCylinder
        - aDirectrix : Directrix Curve of the tabulated cylinder
        - anEnd      : Coordinates of the terminate point of the
        generatrix
        The start point of the directrix is identical to the start
        point of the generatrix
        """

    def Directrix(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the directrix curve of the tabulated cylinder"""

    def EndPoint(self) -> nanoocp.gp.gp_Pnt:
        """returns end point of generatrix of the tabulated cylinder"""

    def TransformedEndPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        returns end point of generatrix of the tabulated cylinder
        after applying Transf. Matrix
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_ToolBoundary:
    """
    Tool to work on a Boundary. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBoundary, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolBoundary) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Boundary | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Boundary | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Boundary | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Boundary <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_Boundary | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Boundary
        (if BoundaryType = 0, Nullify all ParameterCurves)
        """

    def DirChecker(self, ent: IGESGeom_Boundary | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Boundary | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Boundary | None, entto: IGESGeom_Boundary | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Boundary | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolBoundedSurface:
    """
    Tool to work on a BoundedSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBoundedSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolBoundedSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_BoundedSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_BoundedSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_BoundedSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a BoundedSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_BoundedSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_BoundedSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_BoundedSurface | None, entto: IGESGeom_BoundedSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_BoundedSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolBSplineCurve:
    """
    Tool to work on a BSplineCurve. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBSplineCurve, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolBSplineCurve) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_BSplineCurve | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_BSplineCurve | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_BSplineCurve | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a BSplineCurve <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_BSplineCurve | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_BSplineCurve | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_BSplineCurve | None, entto: IGESGeom_BSplineCurve | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_BSplineCurve | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolBSplineSurface:
    """
    Tool to work on a BSplineSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolBSplineSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolBSplineSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_BSplineSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_BSplineSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_BSplineSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a BSplineSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_BSplineSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_BSplineSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_BSplineSurface | None, entto: IGESGeom_BSplineSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_BSplineSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolCircularArc:
    """
    Tool to work on a CircularArc. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCircularArc, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolCircularArc) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_CircularArc | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_CircularArc | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_CircularArc | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CircularArc <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_CircularArc | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_CircularArc | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_CircularArc | None, entto: IGESGeom_CircularArc | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_CircularArc | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolCompositeCurve:
    """
    Tool to work on a CompositeCurve. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCompositeCurve, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolCompositeCurve) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_CompositeCurve | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_CompositeCurve | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_CompositeCurve | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CompositeCurve <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_CompositeCurve | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_CompositeCurve | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_CompositeCurve | None, entto: IGESGeom_CompositeCurve | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_CompositeCurve | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolConicArc:
    """
    Tool to work on a ConicArc. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolConicArc, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolConicArc) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_ConicArc | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_ConicArc | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_ConicArc | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a ConicArc <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_ConicArc | None) -> bool:
        """
        Sets automatic unambiguous Correction on a ConicArc
        (FormNumber recomputed according case Ellips-Parab-Hyperb)
        """

    def DirChecker(self, ent: IGESGeom_ConicArc | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_ConicArc | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_ConicArc | None, entto: IGESGeom_ConicArc | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_ConicArc | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolCopiousData:
    """
    Tool to work on a CopiousData. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCopiousData, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolCopiousData) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_CopiousData | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_CopiousData | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_CopiousData | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CopiousData <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_CopiousData | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_CopiousData | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_CopiousData | None, entto: IGESGeom_CopiousData | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_CopiousData | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolCurveOnSurface:
    """
    Tool to work on a CurveOnSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolCurveOnSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolCurveOnSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_CurveOnSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_CurveOnSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_CurveOnSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a CurveOnSurface <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_CurveOnSurface | None) -> bool:
        """
        Sets automatic unambiguous Correction on a CurveOnSurface
        (its CurveUV must have UseFlag at 5)
        """

    def DirChecker(self, ent: IGESGeom_CurveOnSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_CurveOnSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_CurveOnSurface | None, entto: IGESGeom_CurveOnSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_CurveOnSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolDirection:
    """
    Tool to work on a Direction. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolDirection, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolDirection) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Direction | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Direction | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Direction | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Direction <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_Direction | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Direction | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Direction | None, entto: IGESGeom_Direction | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Direction | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolFlash:
    """
    Tool to work on a Flash. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolFlash, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolFlash) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Flash | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Flash | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Flash | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Flash <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_Flash | None) -> bool:
        """
        Sets automatic unambiguous Correction on a Flash
        (LineFont in Directory Entry forced to Rank = 1)
        """

    def DirChecker(self, ent: IGESGeom_Flash | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Flash | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Flash | None, entto: IGESGeom_Flash | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Flash | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolLine:
    """
    Tool to work on a Line. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolLine, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolLine) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Line | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Line | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Line | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Line <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_Line | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Line | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Line | None, entto: IGESGeom_Line | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Line | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolOffsetCurve:
    """
    Tool to work on a OffsetCurve. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolOffsetCurve, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolOffsetCurve) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_OffsetCurve | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_OffsetCurve | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_OffsetCurve | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a OffsetCurve <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_OffsetCurve | None) -> bool:
        """
        Sets automatic unambiguous Correction on a OffsetCurve
        (if OffsetType is not 3, OffsetFunction is cleared)
        """

    def DirChecker(self, ent: IGESGeom_OffsetCurve | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_OffsetCurve | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_OffsetCurve | None, entto: IGESGeom_OffsetCurve | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_OffsetCurve | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolOffsetSurface:
    """
    Tool to work on a OffsetSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolOffsetSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolOffsetSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_OffsetSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_OffsetSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_OffsetSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a OffsetSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_OffsetSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_OffsetSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_OffsetSurface | None, entto: IGESGeom_OffsetSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_OffsetSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolPlane:
    """
    Tool to work on a Plane. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPlane, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolPlane) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Plane | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Plane | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Plane | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Plane <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_Plane | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Plane | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Plane | None, entto: IGESGeom_Plane | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Plane | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolPoint:
    """
    Tool to work on a Point. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolPoint, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolPoint) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_Point | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_Point | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_Point | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a Point <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_Point | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_Point | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_Point | None, entto: IGESGeom_Point | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_Point | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolRuledSurface:
    """
    Tool to work on a RuledSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolRuledSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolRuledSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_RuledSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_RuledSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_RuledSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a RuledSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_RuledSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_RuledSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_RuledSurface | None, entto: IGESGeom_RuledSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_RuledSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolSplineCurve:
    """
    Tool to work on a SplineCurve. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSplineCurve, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolSplineCurve) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_SplineCurve | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_SplineCurve | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_SplineCurve | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SplineCurve <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_SplineCurve | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_SplineCurve | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_SplineCurve | None, entto: IGESGeom_SplineCurve | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_SplineCurve | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolSplineSurface:
    """
    Tool to work on a SplineSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSplineSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolSplineSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_SplineSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_SplineSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_SplineSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SplineSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_SplineSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_SplineSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_SplineSurface | None, entto: IGESGeom_SplineSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_SplineSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolSurfaceOfRevolution:
    """
    Tool to work on a SurfaceOfRevolution. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolSurfaceOfRevolution, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolSurfaceOfRevolution) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_SurfaceOfRevolution | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_SurfaceOfRevolution | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_SurfaceOfRevolution | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a SurfaceOfRevolution <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_SurfaceOfRevolution | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_SurfaceOfRevolution | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_SurfaceOfRevolution | None, entto: IGESGeom_SurfaceOfRevolution | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_SurfaceOfRevolution | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolTabulatedCylinder:
    """
    Tool to work on a TabulatedCylinder. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTabulatedCylinder, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolTabulatedCylinder) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_TabulatedCylinder | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_TabulatedCylinder | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_TabulatedCylinder | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TabulatedCylinder <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_TabulatedCylinder | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_TabulatedCylinder | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_TabulatedCylinder | None, entto: IGESGeom_TabulatedCylinder | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_TabulatedCylinder | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolTransformationMatrix:
    """
    Tool to work on a TransformationMatrix. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTransformationMatrix, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolTransformationMatrix) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_TransformationMatrix | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_TransformationMatrix | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_TransformationMatrix | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TransformationMatrix <ent>, from
        its specific (own) parameters
        """

    def OwnCorrect(self, ent: IGESGeom_TransformationMatrix | None) -> bool:
        """
        Sets automatic unambiguous Correction on a TransformationMatrix
        (FormNumber if 0 or 1, recomputed according Positive/Negative)
        """

    def DirChecker(self, ent: IGESGeom_TransformationMatrix | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_TransformationMatrix | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_TransformationMatrix | None, entto: IGESGeom_TransformationMatrix | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_TransformationMatrix | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_ToolTrimmedSurface:
    """
    Tool to work on a TrimmedSurface. Called by various Modules
    (ReadWriteModule, GeneralModule, SpecificModule)
    """

    @overload
    def __init__(self) -> None:
        """Returns a ToolTrimmedSurface, ready to work"""

    @overload
    def __init__(self, theOther: IGESGeom_ToolTrimmedSurface) -> None: ...

    def ReadOwnParams(self, ent: IGESGeom_TrimmedSurface | None, IR: nanoocp.IGESData.IGESData_IGESReaderData | None, PR: nanoocp.IGESData.IGESData_ParamReader) -> None:
        """
        Reads own parameters from file. <PR> gives access to them,
        <IR> detains parameter types and values
        """

    def WriteOwnParams(self, ent: IGESGeom_TrimmedSurface | None, IW: nanoocp.IGESData.IGESData_IGESWriter) -> None:
        """Writes own parameters to IGESWriter"""

    def OwnShared(self, ent: IGESGeom_TrimmedSurface | None, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Lists the Entities shared by a TrimmedSurface <ent>, from
        its specific (own) parameters
        """

    def DirChecker(self, ent: IGESGeom_TrimmedSurface | None) -> nanoocp.IGESData.IGESData_DirChecker:
        """Returns specific DirChecker"""

    def OwnCheck(self, ent: IGESGeom_TrimmedSurface | None, shares: nanoocp.Interface.Interface_ShareTool) -> nanoocp.Interface.Interface_Check:
        """Performs Specific Semantic Check"""

    def OwnCopy(self, entfrom: IGESGeom_TrimmedSurface | None, entto: IGESGeom_TrimmedSurface | None, TC: nanoocp.Interface.Interface_CopyTool) -> None:
        """Copies Specific Parameters"""

    def OwnDump(self, ent: IGESGeom_TrimmedSurface | None, dumper: nanoocp.IGESData.IGESData_IGESDumper, own: int) -> str:
        """Dump of Specific Parameters"""

class IGESGeom_TransformationMatrix(nanoocp.IGESData.IGESData_TransfEntity):
    """
    defines IGESTransformationMatrix, Type <124> Form <0>
    in package IGESGeom
    The transformation matrix entity transforms three-row column
    vectors by means of matrix multiplication and then a vector
    addition. This entity can be considered as an "operator"
    entity in that it starts with the input vector, operates on
    it as described above, and produces the output vector.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_TransformationMatrix) -> None: ...

    def Init(self, aMatrix: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """
        This method is used to set the fields of the class
        TransformationMatrix
        - aMatrix : 3 x 4 array containing elements of the
        transformation matrix
        raises exception if aMatrix is not 3 x 4 array
        """

    def SetFormNumber(self, form: int) -> None:
        """
        Changes FormNumber (indicates the Type of Transf :
        Transformation 0-1 or Coordinate System 10-11-12)
        Error if not in ranges [0-1] or [10-12]
        """

    def Data(self, I: int, J: int) -> float:
        """
        returns individual Data
        Error if I not in [1-3] or J not in [1-4]
        """

    def Value(self) -> nanoocp.gp.gp_GTrsf:
        """
        returns the transformation matrix
        4th row elements of GTrsf will always be 0, 0, 0, 1 (not defined)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class IGESGeom_TrimmedSurface(nanoocp.IGESData.IGESData_IGESEntity):
    """
    defines IGESTrimmedSurface, Type <144> Form <0>
    in package IGESGeom
    A simple closed curve in Euclidean plane divides the
    plane in to two disjoint, open connected components; one
    bounded, one unbounded. The bounded one is called the
    interior region to the curve. Unbounded component is called
    exterior region to the curve. The domain of the trimmed
    surface is defined as the interior of the outer boundaries
    and exterior of the inner boundaries and includes the
    boundary curves.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: IGESGeom_TrimmedSurface) -> None: ...

    def Init(self, aSurface: nanoocp.IGESData.IGESData_IGESEntity | None, aFlag: int, anOuter: IGESGeom_CurveOnSurface | None, allInners: nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_CurveOnSurface] | None) -> None:
        """
        This method is used to set the fields of the class
        TrimmedSurface
        - aSurface  : Surface to be trimmed
        - aFlag     : Outer boundary type
        False = The outer boundary is the boundary of
        rectangle D which is the domain of the
        surface to be trimmed
        True  = otherwise
        - anOuter   : Closed curve which constitutes outer boundary
        - allInners : Array of closed curves which constitute the
        inner boundary
        """

    def Surface(self) -> nanoocp.IGESData.IGESData_IGESEntity:
        """returns the surface to be trimmed"""

    def HasOuterContour(self) -> bool:
        """returns True if outer contour exists"""

    def OuterContour(self) -> IGESGeom_CurveOnSurface:
        """returns the outer contour of the trimmed surface"""

    def OuterBoundaryType(self) -> int:
        """
        returns the outer contour type of the trimmed surface
        0  : The outer boundary is the boundary of D
        1  : otherwise
        """

    def NbInnerContours(self) -> int:
        """returns the number of inner boundaries"""

    def InnerContour(self, Index: int) -> IGESGeom_CurveOnSurface:
        """
        returns the Index'th inner contour
        raises exception if Index <= 0 or Index > NbInnerContours()
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.IGESGeom
IGESGeom_Array1OfBoundary = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGeom.IGESGeom_Boundary]
IGESGeom_Array1OfCurveOnSurface = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGeom.IGESGeom_CurveOnSurface]
IGESGeom_Array1OfTransformationMatrix = nanoocp.NCollection.NCollection_Array1[nanoocp.IGESGeom.IGESGeom_TransformationMatrix]
IGESGeom_HArray1OfBoundary = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_Boundary]
IGESGeom_HArray1OfCurveOnSurface = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_CurveOnSurface]
IGESGeom_HArray1OfTransformationMatrix = nanoocp.NCollection.NCollection_HArray1[nanoocp.IGESGeom.IGESGeom_TransformationMatrix]
