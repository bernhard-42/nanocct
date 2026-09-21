"""OCCT package BRepGProp (toolkit TKTopAlgo)"""

import enum
from typing import overload

import nanoocp.BRepAdaptor
import nanoocp.GProp
import nanoocp.GeomAbs
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.gp
import nanoocp.math
from nanoocp.math import math_Vector as math_Vector


class BRepGProp:
    """
    Provides global functions to compute a shape's global
    properties for lines, surfaces or volumes, and bring
    them together with the global properties already
    computed for a geometric system.
    The global properties computed for a system are :
    - its mass,
    - its center of mass,
    - its matrix of inertia,
    - its moment about an axis,
    - its radius of gyration about an axis,
    - and its principal properties of inertia such as
    principal axis, principal moments, principal radius of gyration.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGProp) -> None: ...

    @staticmethod
    def LinearProperties(S: nanoocp.TopoDS.TopoDS_Shape, LProps: nanoocp.GProp.GProp_GProps, SkipShared: bool = False, UseTriangulation: bool = False) -> None:
        """
        Computes the linear global properties of the shape S,
        i.e. the global properties induced by each edge of the
        shape S, and brings them together with the global
        properties still retained by the framework LProps. If
        the current system of LProps was empty, its global
        properties become equal to the linear global
        properties of S.
        For this computation no linear density is attached to
        the edges. So, for example, the added mass
        corresponds to the sum of the lengths of the edges of
        S. The density of the composed systems, i.e. that of
        each component of the current system of LProps, and
        that of S which is considered to be equal to 1, must be coherent.
        Note that this coherence cannot be checked. You are
        advised to use a separate framework for each
        density, and then to bring these frameworks together
        into a global one.
        The point relative to which the inertia of the system is
        computed is the reference point of the framework LProps.
        Note: if your programming ensures that the framework
        LProps retains only linear global properties (brought
        together for example, by the function
        LinearProperties) for objects the density of which is
        equal to 1 (or is not defined), the function Mass will
        return the total length of edges of the system analysed by LProps.
        Warning
        No check is performed to verify that the shape S
        retains truly linear properties. If S is simply a vertex, it
        is not considered to present any additional global properties.
        SkipShared is a special flag, which allows taking in calculation
        shared topological entities or not.
        For ex., if SkipShared = True, edges, shared by two or more faces,
        are taken into calculation only once.
        If we have cube with sizes 1, 1, 1, its linear properties = 12
        for SkipEdges = true and 24 for SkipEdges = false.
        UseTriangulation is a special flag, which defines preferable
        source of geometry data. If UseTriangulation = false,
        exact geometry objects (curves) are used, otherwise polygons of
        triangulation are used first.
        """

    @overload
    @staticmethod
    def SurfaceProperties(S: nanoocp.TopoDS.TopoDS_Shape, SProps: nanoocp.GProp.GProp_GProps, SkipShared: bool = False, UseTriangulation: bool = False) -> None:
        """
        Computes the surface global properties of the
        shape S, i.e. the global properties induced by each
        face of the shape S, and brings them together with
        the global properties still retained by the framework
        SProps. If the current system of SProps was empty,
        its global properties become equal to the surface
        global properties of S.
        For this computation, no surface density is attached
        to the faces. Consequently, the added mass
        corresponds to the sum of the areas of the faces of
        S. The density of the component systems, i.e. that
        of each component of the current system of
        SProps, and that of S which is considered to be
        equal to 1, must be coherent.
        Note that this coherence cannot be checked. You
        are advised to use a framework for each different
        value of density, and then to bring these
        frameworks together into a global one.
        The point relative to which the inertia of the system
        is computed is the reference point of the framework SProps.
        Note : if your programming ensures that the
        framework SProps retains only surface global
        properties, brought together, for example, by the
        function SurfaceProperties, for objects the density
        of which is equal to 1 (or is not defined), the
        function Mass will return the total area of faces of
        the system analysed by SProps.
        Warning
        No check is performed to verify that the shape S
        retains truly surface properties. If S is simply a
        vertex, an edge or a wire, it is not considered to
        present any additional global properties.
        SkipShared is a special flag, which allows taking in calculation
        shared topological entities or not.
        For ex., if SkipShared = True, faces, shared by two or more shells,
        are taken into calculation only once.
        UseTriangulation is a special flag, which defines preferable
        source of geometry data. If UseTriangulation = false,
        exact geometry objects (surfaces) are used,
        otherwise face triangulations are used first.
        """

    @overload
    @staticmethod
    def SurfaceProperties(S: nanoocp.TopoDS.TopoDS_Shape, SProps: nanoocp.GProp.GProp_GProps, Eps: float, SkipShared: bool = False) -> float:
        """
        Updates <SProps> with the shape <S>, that contains its principal properties.
        The surface properties of all the faces in <S> are computed.
        Adaptive 2D Gauss integration is used.
        Parameter Eps sets maximal relative error of computed mass (area) for each face.
        Error is calculated as std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        Method returns estimation of relative error reached for whole shape.
        WARNING: if Eps > 0.001 algorithm performs non-adaptive integration.
        SkipShared is a special flag, which allows taking in calculation
        shared topological entities or not
        For ex., if SkipShared = True, faces, shared by two or more shells,
        are taken into calculation only once.
        """

    @overload
    @staticmethod
    def VolumeProperties(S: nanoocp.TopoDS.TopoDS_Shape, VProps: nanoocp.GProp.GProp_GProps, OnlyClosed: bool = False, SkipShared: bool = False, UseTriangulation: bool = False) -> None:
        """
        Computes the global volume properties of the solid
        S, and brings them together with the global
        properties still retained by the framework VProps. If
        the current system of VProps was empty, its global
        properties become equal to the global properties of S for volume.
        For this computation, no volume density is attached
        to the solid. Consequently, the added mass
        corresponds to the volume of S. The density of the
        component systems, i.e. that of each component of
        the current system of VProps, and that of S which
        is considered to be equal to 1, must be coherent to each other.
        Note that this coherence cannot be checked. You
        are advised to use a separate framework for each
        density, and then to bring these frameworks
        together into a global one.
        The point relative to which the inertia of the system
        is computed is the reference point of the framework VProps.
        Note: if your programming ensures that the
        framework VProps retains only global properties of
        volume (brought together for example, by the
        function VolumeProperties) for objects the density
        of which is equal to 1 (or is not defined), the
        function Mass will return the total volume of the
        solids of the system analysed by VProps.
        Warning
        The shape S must represent an object whose
        global volume properties can be computed. It may
        be a finite solid, or a series of finite solids all
        oriented in a coherent way. Nonetheless, S must be
        exempt of any free boundary. Note that these
        conditions of coherence are not checked by this
        algorithm, and results will be false if they are not respected.
        SkipShared a is special flag, which allows taking in calculation
        shared topological entities or not.
        For ex., if SkipShared = True, the volumes formed by the equal
        (the same TShape, location and orientation) faces are taken
        into calculation only once.
        UseTriangulation is a special flag, which defines preferable
        source of geometry data. If UseTriangulation = false,
        exact geometry objects (surfaces) are used,
        otherwise face triangulations are used first.
        """

    @overload
    @staticmethod
    def VolumeProperties(S: nanoocp.TopoDS.TopoDS_Shape, VProps: nanoocp.GProp.GProp_GProps, Eps: float, OnlyClosed: bool = False, SkipShared: bool = False) -> float:
        """
        Updates <VProps> with the shape <S>, that contains its principal properties.
        The volume properties of all the FORWARD and REVERSED faces in <S> are computed.
        If OnlyClosed is True then computed faces must belong to closed Shells.
        Adaptive 2D Gauss integration is used.
        Parameter Eps sets maximal relative error of computed mass (volume) for each face.
        Error is calculated as std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        Method returns estimation of relative error reached for whole shape.
        WARNING: if Eps > 0.001 algorithm performs non-adaptive integration.
        SkipShared is a special flag, which allows taking in calculation shared
        topological entities or not.
        For ex., if SkipShared = True, the volumes formed by the equal
        (the same TShape, location and orientation)
        faces are taken into calculation only once.
        """

    @overload
    @staticmethod
    def VolumePropertiesGK(S: nanoocp.TopoDS.TopoDS_Shape, VProps: nanoocp.GProp.GProp_GProps, Eps: float = 0.001, OnlyClosed: bool = False, IsUseSpan: bool = False, CGFlag: bool = False, IFlag: bool = False, SkipShared: bool = False) -> float:
        """
        Updates <VProps> with the shape <S>, that contains its principal properties.
        The volume properties of all the FORWARD and REVERSED faces in <S> are computed.
        If OnlyClosed is True then computed faces must belong to closed Shells.
        Adaptive 2D Gauss integration is used.
        Parameter IsUseSpan says if it is necessary to define spans on a face.
        This option has an effect only for BSpline faces.
        Parameter Eps sets maximal relative error of computed property for each face.
        Error is delivered by the adaptive Gauss-Kronrod method of integral computation
        that is used for properties computation.
        Method returns estimation of relative error reached for whole shape.
        Returns negative value if the computation is failed.
        SkipShared is a special flag, which allows taking in calculation
        shared topological entities or not.
        For ex., if SkipShared = True, the volumes formed by the equal
        (the same TShape, location and orientation) faces are taken into calculation only once.
        """

    @overload
    @staticmethod
    def VolumePropertiesGK(S: nanoocp.TopoDS.TopoDS_Shape, VProps: nanoocp.GProp.GProp_GProps, thePln: nanoocp.gp.gp_Pln, Eps: float = 0.001, OnlyClosed: bool = False, IsUseSpan: bool = False, CGFlag: bool = False, IFlag: bool = False, SkipShared: bool = False) -> float: ...

class BRepGProp_Cinert(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of bounded curves
    in 3D space. The curve must have at least a continuity C1.
    It can be a curve as defined in the template CurveTool from
    package GProp. This template gives the minimum of methods
    required to evaluate the global properties of a curve 3D with
    the algorithms of GProp.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: BRepGProp_Cinert) -> None: ...

    def SetLocation(self, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    def Perform(self, C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> None: ...

class BRepGProp_Domain:
    """
    Arc iterator. Returns only Forward and Reversed edges from
    the face in an undigested order.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Constructor. Initializes the domain with the face."""

    def __iter__(self) -> BRepGProp_Domain:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Python addition: see __iter__."""

    @overload
    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initializes the domain with the face."""

    @overload
    def Init(self) -> None:
        """Initializes the exploration with the face already set."""

    def More(self) -> bool:
        """Returns True if there is another arc of curve in the list."""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns the current edge."""

    def Next(self) -> None:
        """
        Sets the index of the arc iterator to the next arc of
        curve.
        """

class BRepGProp_EdgeTool:
    """
    Provides the required methods to instantiate
    CGProps from GProp with a Curve from BRepAdaptor.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGProp_EdgeTool) -> None: ...

    @staticmethod
    def FirstParameter(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> float:
        """
        Returns the parametric value of the start point of
        the curve. The curve is oriented from the start point
        to the end point.
        """

    @staticmethod
    def LastParameter(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> float:
        """
        Returns the parametric value of the end point of
        the curve. The curve is oriented from the start point
        to the end point.
        """

    @staticmethod
    def IntegrationOrder(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve) -> int:
        """
        Returns the number of Gauss points required to do
        the integration with a good accuracy using the
        Gauss method. For a polynomial curve of degree n
        the maxima of accuracy is obtained with an order
        of integration equal to 2*n-1.
        """

    @staticmethod
    def Value(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float) -> nanoocp.gp.gp_Pnt:
        """Returns the point of parameter U on the loaded curve."""

    @staticmethod
    def D1(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, U: float, P: nanoocp.gp.gp_Pnt, V1: nanoocp.gp.gp_Vec) -> None:
        """
        Returns the point of parameter U and the first derivative
        at this point.
        """

    @staticmethod
    def NbIntervals(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, S: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Returns the number of intervals for continuity
        <S>. May be one if Continuity(me) >= <S>
        """

    @staticmethod
    def Intervals(C: nanoocp.BRepAdaptor.BRepAdaptor_Curve, T: nanoocp.NCollection.NCollection_Array1[float], S: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """
        Stores in <T> the parameters bounding the intervals
        of continuity <S>.

        The array must provide enough room to accommodate
        for the parameters. i.e. T.Length() > NbIntervals()
        """

class BRepGProp_Face:
    @overload
    def __init__(self, IsUseSpan: bool = False) -> None:
        """
        Constructor. Initializes the object with a flag IsUseSpan
        that says if it is necessary to define spans on a face.
        This option has an effect only for BSpline faces. Spans
        are returned by the methods GetUKnots and GetTKnots.
        """

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, IsUseSpan: bool = False) -> None:
        """
        Constructor. Initializes the object with the face and the
        flag IsUseSpan that says if it is necessary to define
        spans on a face. This option has an effect only for
        BSpline faces. Spans are returned by the methods GetUKnots
        and GetTKnots.
        """

    @overload
    def __init__(self, theOther: BRepGProp_Face) -> None: ...

    @overload
    def Load(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def Load(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool:
        """
        Loading the boundary arc.
        Returns FALSE if edge has no P-Curve.
        """

    @overload
    def Load(self, IsFirstParam: bool, theIsoType: nanoocp.GeomAbs.GeomAbs_IsoType) -> None:
        """
        Loading the boundary arc. This arc is either a top, bottom,
        left or right bound of a UV rectangle in which the
        parameters of surface are defined.
        If IsFirstParam is equal to true, the face is
        initialized by either left of bottom bound. Otherwise it is
        initialized by the top or right one.
        If theIsoType is equal to GeomAbs_IsoU, the face is
        initialized with either left or right bound. Otherwise -
        with either top or bottom one.
        """

    def VIntegrationOrder(self) -> int: ...

    def NaturalRestriction(self) -> bool:
        """Returns true if the face is not trimmed."""

    def GetFace(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns the TopoDS face."""

    def Value2d(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """Returns the value of the boundary curve of the face."""

    def SIntOrder(self, Eps: float) -> int: ...

    def SVIntSubs(self) -> int: ...

    def SUIntSubs(self) -> int: ...

    def UKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def VKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def LIntOrder(self, Eps: float) -> int: ...

    def LIntSubs(self) -> int: ...

    def LKnots(self, Knots: nanoocp.NCollection.NCollection_Array1[float]) -> None: ...

    def UIntegrationOrder(self) -> int:
        """
        Returns the number of points required to do the
        integration in the U parametric direction with
        a good accuracy.
        """

    def Bounds(self) -> tuple[float, float, float, float]:
        """Returns the parametric bounds of the Face."""

    def Normal(self, U: float, V: float, P: nanoocp.gp.gp_Pnt, VNor: nanoocp.gp.gp_Vec) -> None:
        """
        Computes the point of parameter U, V on the Face <S> and
        the normal to the face at this point.
        """

    def FirstParameter(self) -> float:
        """
        Returns the parametric value of the start point of
        the current arc of curve.
        """

    def LastParameter(self) -> float:
        """
        Returns the parametric value of the end point of
        the current arc of curve.
        """

    def IntegrationOrder(self) -> int:
        """
        Returns the number of points required to do the
        integration along the parameter of curve.
        """

    def D12d(self, U: float, P: nanoocp.gp.gp_Pnt2d, V1: nanoocp.gp.gp_Vec2d) -> None:
        """
        Returns the point of parameter U and the first derivative
        at this point of a boundary curve.
        """

    def GetUKnots(self, theUMin: float, theUMax: float) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns an array of U knots of the face. The first and last
        elements of the array will be theUMin and theUMax. The
        middle elements will be the U Knots of the face greater
        then theUMin and lower then theUMax in increasing order.
        If the face is not a BSpline, the array initialized with
        theUMin and theUMax only.
        @param[in] theUMin lower U bound
        @param[in] theUMax upper U bound
        @return array of U knot values
        """

    def GetUKnots__NCollection_HArray1__double(self, theUMin: float, theUMax: float) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        GetUKnots__NCollection_HArray1__double: the C++ overload GetUKnots(const double, const double, occ::handle<NCollection_HArray1<double>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use GetUKnots() returning handle by value instead

        @deprecated Use GetUKnots() returning handle by value instead.
        """

    def GetTKnots(self, theTMin: float, theTMax: float) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns an array of combination of T knots of the arc and
        V knots of the face. The first and last elements of the
        array will be theTMin and theTMax. The middle elements will
        be the Knots of the arc and the values of parameters of
        arc on which the value points have V coordinates close to V
        knots of face. All the parameter will be greater then
        theTMin and lower then theTMax in increasing order.
        If the face is not a BSpline, the array initialized with
        theTMin and theTMax only.
        @param[in] theTMin lower T bound
        @param[in] theTMax upper T bound
        @return array of T knot values
        """

    def GetTKnots__NCollection_HArray1__double(self, theTMin: float, theTMax: float) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        GetTKnots__NCollection_HArray1__double: the C++ overload GetTKnots(const double, const double, occ::handle<NCollection_HArray1<double>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use GetTKnots() returning handle by value instead

        @deprecated Use GetTKnots() returning handle by value instead.
        """

class BRepGProp_Gauss:
    """
    Class performs computing of the global inertia properties
    of geometric object in 3D space by adaptive and non-adaptive
    2D Gauss integration algorithms.
    """

    def __init__(self, theType: BRepGProp_Gauss.BRepGProp_GaussType) -> None:
        """Constructor"""

    class BRepGProp_GaussType(enum.IntEnum):
        """
        @name public API
        Describes types of geometric objects.
        - Vinert is 3D closed region of space delimited with:
        -- Surface;
        -- Point and Surface;
        -- Plane and Surface.
        - Sinert is face in 3D space.
        """

        Vinert = 0

        Sinert = 1

    Vinert: BRepGProp_Gauss.BRepGProp_GaussType = BRepGProp_GaussType.Vinert

    Sinert: BRepGProp_Gauss.BRepGProp_GaussType = BRepGProp_GaussType.Sinert

    @overload
    def Compute(self, theSurface: BRepGProp_Face, theLocation: nanoocp.gp.gp_Pnt, theOutGravityCenter: nanoocp.gp.gp_Pnt, theOutInertia: nanoocp.gp.gp_Mat) -> float:
        """
        Computes the global properties of a surface. Surface can be closed.
        The method is quick and its precision is enough for many cases of analytical surfaces.
        Non-adaptive 2D Gauss integration with predefined numbers of Gauss points
        is used. Numbers of points depend on types of surfaces and curves.
        Error of the computation is not calculated.
        @param theSurface - bounding surface of the region;
        @param theLocation - surface location;
        @param[out] theOutMass - mass (volume) of region;
        @param[out] theOutGravityCenter - garvity center of region;
        @param[out] theOutInertia - matrix of inertia;
        """

    @overload
    def Compute(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theLocation: nanoocp.gp.gp_Pnt, theOutGravityCenter: nanoocp.gp.gp_Pnt, theOutInertia: nanoocp.gp.gp_Mat) -> float:
        """
        Computes the global properties of a surface. Surface can be closed.
        The method is quick and its precision is enough for many cases of analytical surfaces.
        Non-adaptive 2D Gauss integration with predefined numbers of Gauss points
        is used. Numbers of points depend on types of surfaces and curves.
        Error of the computation is not calculated.
        @param theSurface - bounding surface of the region;
        @param theDomain - surface boundings;
        @param theLocation - surface location;
        @param[out] theOutMass - mass (volume) of region;
        @param[out] theOutGravityCenter - garvity center of region;
        @param[out] theOutInertia - matrix of inertia;
        """

    @overload
    def Compute(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theLocation: nanoocp.gp.gp_Pnt, theEps: float, theOutGravityCenter: nanoocp.gp.gp_Pnt, theOutInertia: nanoocp.gp.gp_Mat) -> tuple[float, float]:
        """
        Computes the global properties of the face. Adaptive 2D Gauss integration is used.
        If Epsilon more than 0.001 then algorithm performs non-adaptive integration.
        @param theSurface - bounding surface of the region;
        @param theDomain - surface boundings;
        @param theLocation - surface location;
        @param theEps - maximal relative error of computed mass (square) for face;
        @param[out] theOutMass - mass (volume) of region;
        @param[out] theOutGravityCenter - garvity center of region;
        @param[out] theOutInertia - matrix of inertia;
        @return value of error which is calculated as
        std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        """

class BRepGProp_Sinert(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of a face in 3D space.
    The face 's requirements to evaluate the global properties
    are defined in the template FaceTool from package GProp.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, SLocation: nanoocp.gp.gp_Pnt) -> None:
        """
        Builds a Sinert to evaluate the global properties of
        the face <S>. If isNaturalRestriction is true the domain of S is defined
        with the natural bounds, else it defined with an iterator
        of Edge from TopoDS (see DomainTool from GProp)
        """

    @overload
    def __init__(self, S: BRepGProp_Face, SLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, SLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepGProp_Sinert) -> None: ...

    def SetLocation(self, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Eps: float) -> float: ...

    def GetEpsilon(self) -> float:
        """
        If previously used method contained Eps parameter
        get actual relative error of the computation, else return 1.0.
        """

class BRepGProp_UFunction(nanoocp.math.math_Function):
    """
    This class represents the integrand function for
    computation of an inner integral. The returned value
    depends on the value type and the flag IsByPoint.

    The type of returned value is the one of the following
    values:
    -  GProp_Mass - volume computation.
    -  GProp_CenterMassX, GProp_CenterMassY,
    GProp_CenterMassZ - X, Y and Z coordinates of center
    of mass computation.
    -  GProp_InertiaXX, GProp_InertiaYY, GProp_InertiaZZ,
    GProp_InertiaXY, GProp_InertiaXZ, GProp_InertiaYZ
    - moments of inertia computation.

    If the flag IsByPoint is set to true, the value is
    returned for the region of space that is delimited by a
    surface and a point. Otherwise all computations are
    performed for the region of space delimited by a surface
    and a plane.
    """

    def __init__(self, theOther: BRepGProp_UFunction) -> None: ...

    def SetValueType(self, theType: nanoocp.GProp.GProp_ValueType) -> None:
        """Setting the type of the value to be returned."""

    def SetVParam(self, theVParam: float) -> None:
        """
        Setting the V parameter that is constant during the
        integral computation.
        """

    def Value(self, X: float) -> tuple[bool, float]:
        """Returns a value of the function."""

class BRepGProp_TFunction(nanoocp.math.math_Function):
    """
    This class represents the integrand function for the outer
    integral computation. The returned value represents the
    integral of UFunction. It depends on the value type and the
    flag IsByPoint.
    """

    def __init__(self, theOther: BRepGProp_TFunction) -> None: ...

    def Init(self) -> None: ...

    def SetNbKronrodPoints(self, theNbPoints: int) -> None:
        """
        Setting the expected number of Kronrod points for the outer
        integral computation. This number is required for
        computation of a value of tolerance for inner integral
        computation. After GetStateNumber method call, this number
        is recomputed by the same law as in
        math_KronrodSingleIntegration, i.e. next number of points
        is equal to the current number plus a square root of the
        current number. If the law in math_KronrodSingleIntegration
        is changed, the modification algo should be modified
        accordingly.
        """

    def SetValueType(self, aType: nanoocp.GProp.GProp_ValueType) -> None:
        """
        Setting the type of the value to be returned. This
        parameter is directly passed to the UFunction.
        """

    def SetTolerance(self, aTol: float) -> None:
        """Setting the tolerance for inner integration"""

    def ErrorReached(self) -> float:
        """
        Returns the relative reached error of all values computation since
        the last call of GetStateNumber method.
        """

    def AbsolutError(self) -> float:
        """
        Returns the absolut reached error of all values computation since
        the last call of GetStateNumber method.
        """

    def Value(self, X: float) -> tuple[bool, float]:
        """
        Returns a value of the function. The value represents an
        integral of UFunction. It is computed with the predefined
        tolerance using the adaptive Gauss-Kronrod method.
        """

    def GetStateNumber(self) -> int:
        """
        Redefined method. Remembers the error reached during
        computation of integral values since the object creation
        or the last call of GetStateNumber. It is invoked in each
        algorithm from the package math. Particularly in the
        algorithm math_KronrodSingleIntegration that is used to
        compute the integral of TFunction.
        """

class BRepGProp_Vinert(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of a geometric solid
    (3D closed region of space) delimited with :
    . a surface
    . a point and a surface
    . a plane and a surface

    The surface can be :
    . a surface limited with its parametric values U-V,
    . a surface limited in U-V space with its curves of restriction,

    The surface 's requirements to evaluate the global properties
    are defined in the template SurfaceTool from package GProp.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, O: nanoocp.gp.gp_Pnt, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, Pl: nanoocp.gp.gp_Pln, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, VLocation: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the global properties of a region of 3D space
        delimited with the surface <S> and the point VLocation. S can be closed
        The method is quick and its precision is enough for many cases of analytical
        surfaces.
        Non-adaptive 2D Gauss integration with predefined numbers of Gauss points
        is used. Numbers of points depend on types of surfaces and curves.
        Error of the computation is not calculated.
        """

    @overload
    def __init__(self, S: BRepGProp_Face, O: nanoocp.gp.gp_Pnt, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, Pl: nanoocp.gp.gp_Pln, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None: ...

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None:
        """
        Computes the global properties of a region of 3D space
        delimited with the surface <S> and the point VLocation. S can be closed
        Adaptive 2D Gauss integration is used.
        Parameter Eps sets maximal relative error of computed mass (volume) for face.
        Error is calculated as std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        """

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: nanoocp.gp.gp_Pnt, VLocation: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the global properties of the region of 3D space
        delimited with the surface <S> and the point VLocation.
        The method is quick and its precision is enough for many cases of analytical
        surfaces.
        Non-adaptive 2D Gauss integration with predefined numbers of Gauss points
        is used. Numbers of points depend on types of surfaces and curves.
        Error of the computation is not calculated.
        """

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: nanoocp.gp.gp_Pln, VLocation: nanoocp.gp.gp_Pnt) -> None:
        """
        Computes the global properties of the region of 3D space
        delimited with the surface <S> and the plane Pln.
        The method is quick and its precision is enough for many cases of analytical
        surfaces.
        Non-adaptive 2D Gauss integration with predefined numbers of Gauss points
        is used. Numbers of points depend on types of surfaces and curves.
        Error of the computation is not calculated.
        """

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: nanoocp.gp.gp_Pnt, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None:
        """
        Computes the global properties of the region of 3D space
        delimited with the surface <S> and the point VLocation.
        Adaptive 2D Gauss integration is used.
        Parameter Eps sets maximal relative error of computed mass (volume) for face.
        Error is calculated as std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        WARNING: if Eps > 0.001 algorithm performs non-adaptive integration.
        """

    @overload
    def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: nanoocp.gp.gp_Pln, VLocation: nanoocp.gp.gp_Pnt, Eps: float) -> None:
        """
        Computes the global properties of the region of 3D space
        delimited with the surface <S> and the plane Pln.
        Adaptive 2D Gauss integration is used.
        Parameter Eps sets maximal relative error of computed mass (volume) for face.
        Error is calculated as std::abs((M(i+1)-M(i))/M(i+1)), M(i+1) and M(i) are values
        for two successive steps of adaptive integration.
        WARNING: if Eps > 0.001 algorithm performs non-adaptive integration.
        """

    @overload
    def __init__(self, theOther: BRepGProp_Vinert) -> None: ...

    def SetLocation(self, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, O: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, O: nanoocp.gp.gp_Pnt, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, Pl: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, Pl: nanoocp.gp.gp_Pln, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: nanoocp.gp.gp_Pnt, Eps: float) -> float: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: nanoocp.gp.gp_Pln, Eps: float) -> float: ...

    def GetEpsilon(self) -> float:
        """
        If previously used methods contain Eps parameter
        gets actual relative error of the computation, else returns 1.0.
        """

class BRepGProp_VinertGK(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of a geometric solid
    (3D closed region of space) delimited with :
    -  a point and a surface
    -  a plane and a surface

    The surface can be :
    -  a surface limited with its parametric values U-V,
    (naturally restricted)
    -  a surface limited in U-V space with its boundary
    curves.

    The surface's requirements to evaluate the global
    properties are defined in the template FaceTool class from
    the package GProp.

    The adaptive 2D algorithm of Gauss-Kronrod integration of
    double integral is used.

    The inner integral is computed along U parameter of
    surface. The integrand function is encapsulated in the
    support class UFunction that is defined below.

    The outer integral is computed along T parameter of a
    bounding curve. The integrand function is encapsulated in
    the support class TFunction that is defined below.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theSurface: BRepGProp_Face, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the naturally restricted surface
        and the point VLocation.
        """

    @overload
    def __init__(self, theSurface: BRepGProp_Face, thePoint: nanoocp.gp.gp_Pnt, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the naturally restricted surface
        and the point VLocation. The inertia is computed with
        respect to thePoint.
        """

    @overload
    def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the surface bounded by the domain
        and the point VLocation.
        """

    @overload
    def __init__(self, theSurface: BRepGProp_Face, thePlane: nanoocp.gp.gp_Pln, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the naturally restricted surface
        and the plane.
        """

    @overload
    def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePoint: nanoocp.gp.gp_Pnt, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the surface bounded by the domain
        and the point VLocation. The inertia is computed with
        respect to thePoint.
        """

    @overload
    def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePlane: nanoocp.gp.gp_Pln, theLocation: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> None:
        """
        Constructor. Computes the global properties of a region of
        3D space delimited with the surface bounded by the domain
        and the plane.
        """

    @overload
    def __init__(self, theOther: BRepGProp_VinertGK) -> None: ...

    def SetLocation(self, theLocation: nanoocp.gp.gp_Pnt) -> None:
        """Sets the vertex that delimit 3D closed region of space."""

    @overload
    def Perform(self, theSurface: BRepGProp_Face, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the naturally restricted surface and the
        point VLocation.
        """

    @overload
    def Perform(self, theSurface: BRepGProp_Face, thePoint: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the naturally restricted surface and the
        point VLocation. The inertia is computed with respect to
        thePoint.
        """

    @overload
    def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the surface bounded by the domain and the
        point VLocation.
        """

    @overload
    def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePoint: nanoocp.gp.gp_Pnt, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the surface bounded by the domain and the
        point VLocation. The inertia is computed with respect to
        thePoint.
        """

    @overload
    def Perform(self, theSurface: BRepGProp_Face, thePlane: nanoocp.gp.gp_Pln, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the naturally restricted surface and the
        plane.
        """

    @overload
    def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePlane: nanoocp.gp.gp_Pln, theTolerance: float = 0.001, theCGFlag: bool = False, theIFlag: bool = False) -> float:
        """
        Computes the global properties of a region of 3D space
        delimited with the surface bounded by the domain and the
        plane.
        """

    def GetErrorReached(self) -> float:
        """Returns the relative reached computation error."""

class BRepGProp_MeshCinert(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of
    of polylines represented by set of points.
    This class is used for computation of global
    properties of edge, which has no exact geometry
    (3d or 2d curve), but has any of allowed
    polygons.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepGProp_MeshCinert) -> None: ...

    def SetLocation(self, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    def Perform(self, theNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """
        Computes the global properties of
        of polylines represented by set of points.
        """

    @staticmethod
    def PreparePolygon(theE: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        Prepares set of 3d points on base of any available edge polygons:
        3D polygon, polygon on triangulation, 2d polygon on surface.
        @param[in] theE the edge to extract polygon from
        @return array of 3D points, or null handle if edge has no polygons
        """

    @staticmethod
    def PreparePolygon__NCollection_HArray1__gp_Pnt(theE: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt]:
        """
        PreparePolygon__NCollection_HArray1__gp_Pnt: the C++ overload PreparePolygon(const TopoDS_Edge &, occ::handle<NCollection_HArray1<gp_Pnt>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Use PreparePolygon() returning handle by value instead

        @deprecated Use PreparePolygon() returning handle by value instead.
        """

class BRepGProp_MeshProps(nanoocp.GProp.GProp_GProps):
    """
    Computes the global properties of a surface mesh. The mesh can be
    interpreted as just a surface or as a piece of volume limited by this surface.
    """

    @overload
    def __init__(self, theType: BRepGProp_MeshProps.BRepGProp_MeshObjType) -> None:
        """Constructor takes the type of object."""

    @overload
    def __init__(self, theOther: BRepGProp_MeshProps) -> None: ...

    class BRepGProp_MeshObjType(enum.IntEnum):
        """
        Describes types of geometric objects.
        - Vinert is 3D closed region of space delimited with
        Point and surface mesh;
        - Sinert is surface mesh in 3D space.
        """

        Vinert = 0

        Sinert = 1

    Vinert: BRepGProp_MeshProps.BRepGProp_MeshObjType = BRepGProp_MeshObjType.Vinert

    Sinert: BRepGProp_MeshProps.BRepGProp_MeshObjType = BRepGProp_MeshObjType.Sinert

    def SetLocation(self, theLocation: nanoocp.gp.gp_Pnt) -> None:
        """Sets the point relative which the calculation is to be done"""

    @overload
    def Perform(self, theMesh: nanoocp.Poly.Poly_Triangulation | None, theLoc: nanoocp.TopLoc.TopLoc_Location, theOri: nanoocp.TopAbs.TopAbs_Orientation) -> None:
        """
        Computes the global properties of a surface mesh of 3D space.
        Calculation of surface properties is performed by numerical integration
        over triangle surfaces using Gauss cubature formulas.
        Depending on the mesh object type used in constructor this method can
        calculate the surface or volume properties of the mesh.
        """

    @overload
    def Perform(self, theMesh: nanoocp.Poly.Poly_Triangulation | None, theOri: nanoocp.TopAbs.TopAbs_Orientation) -> None: ...

    def GetMeshObjType(self) -> BRepGProp_MeshProps.BRepGProp_MeshObjType:
        """Get type of mesh object"""
