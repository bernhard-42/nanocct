"""OCCT package GProp (toolkit TKGeomBase)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.gp


class GProp_ValueType(enum.IntEnum):
    """Algorithms:"""

    GProp_Mass = 0

    GProp_CenterMassX = 1

    GProp_CenterMassY = 2

    GProp_CenterMassZ = 3

    GProp_InertiaXX = 4

    GProp_InertiaYY = 5

    GProp_InertiaZZ = 6

    GProp_InertiaXY = 7

    GProp_InertiaXZ = 8

    GProp_InertiaYZ = 9

    GProp_Unknown = 10

GProp_Mass: GProp_ValueType = GProp_ValueType.GProp_Mass

GProp_CenterMassX: GProp_ValueType = GProp_ValueType.GProp_CenterMassX

GProp_CenterMassY: GProp_ValueType = GProp_ValueType.GProp_CenterMassY

GProp_CenterMassZ: GProp_ValueType = GProp_ValueType.GProp_CenterMassZ

GProp_InertiaXX: GProp_ValueType = GProp_ValueType.GProp_InertiaXX

GProp_InertiaYY: GProp_ValueType = GProp_ValueType.GProp_InertiaYY

GProp_InertiaZZ: GProp_ValueType = GProp_ValueType.GProp_InertiaZZ

GProp_InertiaXY: GProp_ValueType = GProp_ValueType.GProp_InertiaXY

GProp_InertiaXZ: GProp_ValueType = GProp_ValueType.GProp_InertiaXZ

GProp_InertiaYZ: GProp_ValueType = GProp_ValueType.GProp_InertiaYZ

GProp_Unknown: GProp_ValueType = GProp_ValueType.GProp_Unknown

class GProp:
    """
    This package defines algorithms to compute the global properties
    of a set of points, a curve, a surface, a solid (non infinite
    region of space delimited with geometric entities), a compound
    geometric system (heterogeneous composition of the previous
    entities).

    Global properties are:
    . length, area, volume,
    . centre of mass,
    . axis of inertia,
    . moments of inertia,
    . radius of gyration.

    It provides also a class to compile the average point or
    line of a set of points.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: GProp) -> None: ...

    @staticmethod
    def HOperator(G: nanoocp.gp.gp_Pnt, Q: nanoocp.gp.gp_Pnt, Mass: float, Operator: nanoocp.gp.gp_Mat) -> None:
        """
        methods of package
        Computes the matrix Operator, referred to as the
        "Huyghens Operator" of a geometric system at the
        point Q of the space, using the following data:
        - Mass, i.e. the mass of the system,
        - G, the center of mass of the system.
        The "Huyghens Operator" is used to compute
        Inertia/Q, the matrix of inertia of the system at
        the point Q using Huyghens' theorem:
        Inertia/Q = Inertia/G + HOperator (Q, G, Mass)
        where Inertia/G is the matrix of inertia of the
        system relative to its center of mass as returned by
        the function MatrixOfInertia on any GProp_GProps object.
        """

class GProp_GProps:
    """
    Implements a general mechanism to compute the global properties of
    a "compound geometric system" in 3D space by composition of the
    global properties of elementary geometric entities such as a curve,
    surface, solid, or set of points. It is also possible to compose
    the properties of several "compound geometric systems".

    To compute the global properties of a compound geometric system:
    - declare a GProp_GProps using a constructor which initializes the
    instance and defines the location point used to compute the
    inertia,
    - compose the global properties of the geometric components into
    the system using the method Add().

    To compute the global properties of the geometric components of
    the system, use the services of the following frameworks:
    - GProp_PGProps for a set of points,
    - CGProps       for a curve,
    - SGProps       for a surface,
    - VGProps       for a "solid".
    The CGProps, SGProps and VGProps frameworks are generic and must
    be instantiated for the application (see BRepGProp / GeomGProp).

    The global properties computed are:
    - the dimension (length, area or volume),
    - the mass,
    - the centre of mass,
    - the moments of inertia (static moments and quadratic moments),
    - the moment about an axis,
    - the radius of gyration about an axis,
    - the principal properties of inertia
    (see GProp_PrincipalProps):
    - the principal moments,
    - the principal axes of inertia,
    - the principal radii of gyration.

    Example:
    @code
    // Declares the GProps; the absolute origin (0, 0, 0) is used as the
    // default reference point to compute the centre of mass.
    GProp_GProps aSystem;

    // Computes the inertia of a 3D curve.
    Your_CGProps aComponent1(theCurve, ...);

    // Computes the inertia of two surfaces.
    Your_SGProps aComponent2(theSurface1, ...);
    Your_SGProps aComponent3(theSurface2, ...);

    // Composes the global properties of components 1, 2, 3. A density
    // can be associated with the components; it defaults to 1.0.
    const double aDensity1 = 2.0;
    const double aDensity2 = 3.0;
    aSystem.Add(aComponent1, aDensity1);
    aSystem.Add(aComponent2, aDensity2);
    aSystem.Add(aComponent3);

    // Returns the centre of mass of the system in the absolute
    // Cartesian coordinate system.
    const gp_Pnt aG = aSystem.CentreOfMass();

    // Computes the principal properties of inertia of the system.
    const GProp_PrincipalProps aPp = aSystem.PrincipalProperties();

    // Returns the principal moments and radii of gyration.
    double aIxx, aIyy, aIzz, aRxx, aRyy, aRzz;
    aPp.Moments(aIxx, aIyy, aIzz);
    aPp.RadiusOfGyration(aRxx, aRyy, aRzz);
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """
        The origin (0, 0, 0) of the absolute Cartesian coordinate system
        is used to compute the global properties.
        """

    @overload
    def __init__(self, SystemLocation: nanoocp.gp.gp_Pnt) -> None:
        """
        The point SystemLocation is used to compute the global properties
        of the system. For greater accuracy, define this point close to
        the location of the system; for example a point near the centre
        of mass of the system.

        At initialization the framework is empty: it retains no
        dimensional information such as mass or inertia. It is, however,
        ready to bring together global properties of various other
        systems whose global properties have already been computed using
        another framework. To do this, use Add() to define the components
        of the system, once per component, and then use the interrogation
        functions to access the computed values.

        @param[in] SystemLocation reference point of the system used for
        inertia accumulation
        """

    @overload
    def __init__(self, theOther: GProp_GProps) -> None: ...

    def Add(self, Item: GProp_GProps, Density: float = 1.0) -> None:
        """
        Either:
        - initializes the global properties retained by this framework
        from those retained by the framework Item, or
        - brings together the global properties retained by this
        framework with those retained by the framework Item.

        The value Density (1.0 by default) is used as the density of the
        system analysed by Item. Sometimes the density has already been
        accounted for at construction time of Item - for example when
        Item is a GProp_PGProps framework built to compute the global
        properties of a set of weighted points, or another GProp_GProps
        object that already retains composite global properties. In these
        cases the real density was already taken into account at
        construction of Item. Note that this is not checked: if the
        density of parts of the system is taken into account two or more
        times, the result of the computation will be wrong.

        Notes:
        - The reference point of Item may differ from the reference point
        of this framework. Huygens' theorem is applied automatically to
        transfer inertia values to the reference point of this
        framework.
        - Add() is used once per component of the system. After all
        components are composed, the interrogation functions return
        values for the system as a whole.
        - The system whose global properties have been brought together
        by this framework is referred to as the "current system". The
        current system itself is not retained: only its global
        properties are.

        @param[in] Item    framework holding the global properties of the
        component to compose
        @param[in] Density density of the component (default 1.0)
        @throws Standard_DomainError if Density is less than or equal to
        gp::Resolution().
        """

    def Mass(self) -> float:
        """
        Returns the mass of the current system.

        If no density has been attached to the components of the current
        system, the returned value corresponds to:
        - the total length of the edges of the current system if this
        framework retains only linear properties (for example, when
        using only LinearProperties() to combine properties of lines
        from shapes), or
        - the total area of the faces of the current system if this
        framework retains only surface properties (for example, when
        using only SurfaceProperties() to combine properties of
        surfaces from shapes), or
        - the total volume of the solids of the current system if this
        framework retains only volume properties (for example, when
        using only VolumeProperties() to combine properties of volumes
        from solids).

        @warning A length, an area or a volume is computed in the current
        unit system. The mass of a single object is its length,
        area or volume multiplied by its density. Be consistent
        with respect to the units used.
        """

    def CentreOfMass(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the centre of mass of the current system. With a uniform
        gravitational field this is also the centre of gravity. The
        coordinates returned for the centre of mass are expressed in the
        absolute Cartesian coordinate system.
        """

    def MatrixOfInertia(self) -> nanoocp.gp.gp_Mat:
        """
        Returns the matrix of inertia. It is a symmetric matrix whose
        coefficients are the quadratic moments of inertia:
        @verbatim
        | Ixx  Ixy  Ixz |
        matrix = | Ixy  Iyy  Iyz |
        | Ixz  Iyz  Izz |
        @endverbatim
        Ixx, Iyy, Izz are the moments of inertia; Ixy, Ixz, Iyz are the
        products of inertia.

        The matrix of inertia is returned in the central coordinate
        system (G, Gx, Gy, Gz), where G is the centre of mass of the
        system and Gx, Gy, Gz are parallel to the X(1, 0, 0), Y(0, 1, 0)
        and Z(0, 0, 1) directions of the absolute Cartesian coordinate
        system. To compute the matrix of inertia at another location use
        GProp::HOperator() (Huygens' theorem).
        """

    def StaticMoments(self) -> tuple[float, float, float]:
        """
        Returns the static moments of inertia of the current system -
        i.e. the moments of inertia about the three axes of the absolute
        Cartesian coordinate system.

        @param[out] Ix static moment of inertia about X
        @param[out] Iy static moment of inertia about Y
        @param[out] Iz static moment of inertia about Z
        """

    def MomentOfInertia(self, A: nanoocp.gp.gp_Ax1) -> float:
        """
        Computes the moment of inertia of the system about the axis A.
        @param[in] A axis about which the moment of inertia is computed
        """

    def PrincipalProperties(self) -> GProp_PrincipalProps:
        """
        Computes the principal properties of inertia of the current
        system. There is always a set of axes for which the products of
        inertia of a geometric system are equal to 0 - i.e. the matrix of
        inertia of the system is diagonal. These axes are the principal
        axes of inertia; their origin coincides with the centre of mass
        of the system. The associated moments are called the principal
        moments of inertia.

        This function computes the eigen values and eigen vectors of the
        matrix of inertia of the system. Results are stored in a
        GProp_PrincipalProps framework which can be queried to access
        the value sought.
        """

    def RadiusOfGyration(self, A: nanoocp.gp.gp_Ax1) -> float:
        """
        Returns the radius of gyration of the current system about the
        axis A.
        @param[in] A axis about which the radius of gyration is computed
        """

class GProp_CelGProps(GProp_GProps):
    """
    Computes the global properties of bounded curves in 3D space.
    Supports elementary curves from the gp package: Lin, Circ, Elips, Parab.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Circ, U1: float, U2: float, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, C: nanoocp.gp.gp_Lin, U1: float, U2: float, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: GProp_CelGProps) -> None: ...

    def SetLocation(self, CLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Circ, U1: float, U2: float) -> None: ...

    @overload
    def Perform(self, C: nanoocp.gp.gp_Lin, U1: float, U2: float) -> None: ...

class GProp_PEquation:
    """
    Analyzes a collection of 3D points to decide whether they are
    coincident, collinear, coplanar, or span 3D space, within a given
    tolerance.

    Uses principal-axis analysis (eigendecomposition of the inertia matrix)
    to determine the dimensionality of the cloud. Depending on the result
    type, the corresponding accessor (Point(), Line(), Plane() or Box())
    returns the fitted geometric entity.

    The raw PCA results (Barycentre(), PrincipalAxis(), Extent()) are
    always available regardless of the fitted type.
    """

    @overload
    def __init__(self, thePnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theTol: float) -> None:
        """
        Constructs the analysis from a set of points and a tolerance.
        @param[in] thePnts array of points to analyze
        @param[in] theTol  tolerance for dimensional collapse detection
        """

    @overload
    def __init__(self, theOther: GProp_PEquation) -> None: ...

    class Type(enum.Enum):
        """Type of geometric entity that best fits the cloud."""

        Point = 1

        Line = 2

        Plane = 3

        Space = 4

    def GetType(self) -> GProp_PEquation.Type:
        """Returns the type of the fitted entity."""

    def IsPlanar(self) -> bool:
        """Returns true if points are coplanar within tolerance."""

    def IsLinear(self) -> bool:
        """Returns true if points are collinear within tolerance."""

    def IsPoint(self) -> bool:
        """Returns true if points are coincident within tolerance."""

    def IsSpace(self) -> bool:
        """Returns true if points span 3D space."""

    def Plane(self) -> nanoocp.gp.gp_Pln:
        """
        Returns the mean plane.
        @throws Standard_NoSuchObject if !IsPlanar().
        """

    def Line(self) -> nanoocp.gp.gp_Lin:
        """
        Returns the mean line.
        @throws Standard_NoSuchObject if !IsLinear().
        """

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the mean point.
        @throws Standard_NoSuchObject if !IsPoint().
        """

    def Box(self, theP: nanoocp.gp.gp_Pnt, theV1: nanoocp.gp.gp_Vec, theV2: nanoocp.gp.gp_Vec, theV3: nanoocp.gp.gp_Vec) -> None:
        """
        Returns a bounding box aligned with the principal axes.
        @param[out] theP  corner of the box (minimum projection on principal axes)
        @param[out] theV1 first box edge vector (along first principal axis)
        @param[out] theV2 second box edge vector (along second principal axis)
        @param[out] theV3 third box edge vector (along third principal axis)
        @throws Standard_NoSuchObject if !IsSpace().
        """

    def Barycentre(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the centre of mass of the cloud (always valid after construction).
        """

    def PrincipalAxis(self, theIndex: int) -> nanoocp.gp.gp_Vec:
        """
        Returns the unit principal axis at @p theIndex (1, 2 or 3),
        ordered by eigenvalue.
        """

    def Extent(self, theIndex: int) -> float:
        """
        Returns the extent (max - min projection) along principal axis
        @p theIndex (1, 2 or 3).
        """

class GProp_PGProps(GProp_GProps):
    """
    Computes global properties (mass, barycentre, inertia matrix) of a
    weighted set of 3D points.

    Each point carries a mass; by default the mass is unit. Contributions are
    accumulated incrementally via AddPoint() or from arrays passed to a
    constructor. As a GProp_GProps subclass, an instance can be composed
    into a larger system via GProp_GProps::Add().

    Inertia is accumulated at the absolute origin and stored in the inherited
    GProp_GProps::inertia member, matching the legacy contract of this class.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty point set, located at the origin, with zero mass."""

    @overload
    def __init__(self, thePnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None:
        """Creates a point set from an array of points (unit mass each)."""

    @overload
    def __init__(self, thePnts: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]) -> None:
        """Creates a point set from a 2D array of points (unit mass each)."""

    @overload
    def __init__(self, thePnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theDensity: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """
        Creates a point set from points and corresponding densities.
        @param[in] thePnts    point array
        @param[in] theDensity per-point mass array (same length as thePnts)
        @throws Standard_DomainError if a density <= gp::Resolution() or if the
        arrays have different lengths.
        """

    @overload
    def __init__(self, thePnts: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theDensity: nanoocp.NCollection.NCollection_Array2[float]) -> None:
        """
        Creates a point set from 2D arrays of points and corresponding densities.
        @param[in] thePnts    point array
        @param[in] theDensity per-point mass array (same dimensions as thePnts)
        @throws Standard_DomainError on dimension mismatch or non-positive density.
        """

    @overload
    def __init__(self, theOther: GProp_PGProps) -> None: ...

    @overload
    def AddPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Adds a point with unit mass."""

    @overload
    def AddPoint(self, thePnt: nanoocp.gp.gp_Pnt, theDensity: float) -> None:
        """
        Adds a point with a given mass.
        @throws Standard_DomainError if theDensity <= gp::Resolution().
        """

    @overload
    @staticmethod
    def Barycentre(thePnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> nanoocp.gp.gp_Pnt:
        """Computes the barycentre of a set of points (unit mass)."""

    @overload
    @staticmethod
    def Barycentre(thePnts: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt]) -> nanoocp.gp.gp_Pnt:
        """Computes the barycentre of a 2D array of points (unit mass)."""

    @overload
    @staticmethod
    def Barycentre(thePnts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theDensity: nanoocp.NCollection.NCollection_Array1[float], theG: nanoocp.gp.gp_Pnt) -> float:
        """
        Computes the weighted barycentre and total mass of a set of points.
        @param[in]  thePnts    point array
        @param[in]  theDensity per-point mass array
        @param[out] theMass    total mass (sum of densities)
        @param[out] theG       weighted barycentre
        @throws Standard_DimensionError on length mismatch.
        """

    @overload
    @staticmethod
    def Barycentre(thePnts: nanoocp.NCollection.NCollection_Array2[nanoocp.gp.gp_Pnt], theDensity: nanoocp.NCollection.NCollection_Array2[float], theG: nanoocp.gp.gp_Pnt) -> float:
        """
        Computes the weighted barycentre and total mass for a 2D point array.
        @throws Standard_DimensionError on dimension mismatch.
        """

class GProp_PrincipalProps:
    """
    A framework to present the principal properties of
    inertia of a system of which global properties are
    computed by a GProp_GProps object.
    There is always a set of axes for which the
    products of inertia of a geometric system are equal
    to 0; i.e. the matrix of inertia of the system is
    diagonal. These axes are the principal axes of
    inertia. Their origin is coincident with the center of
    mass of the system. The associated moments are
    called the principal moments of inertia.
    This sort of presentation object is created, filled and
    returned by the function PrincipalProperties for
    any GProp_GProps object, and can be queried to access the result.
    Note: The system whose principal properties of
    inertia are returned by this framework is referred to
    as the current system. The current system,
    however, is retained neither by this presentation
    framework nor by the GProp_GProps object which activates it.
    """

    @overload
    def __init__(self) -> None:
        """creates an undefined PrincipalProps."""

    @overload
    def __init__(self, theOther: GProp_PrincipalProps) -> None: ...

    @overload
    def HasSymmetryAxis(self) -> bool:
        """
        returns true if the geometric system has an axis of symmetry.
        For comparing moments relative tolerance 1.e-10 is used.
        Usually it is enough for objects, restricted by faces with
        analytical geometry.
        """

    @overload
    def HasSymmetryAxis(self, aTol: float) -> bool:
        """
        returns true if the geometric system has an axis of symmetry.
        aTol is relative tolerance for checking equality of moments
        If aTol == 0, relative tolerance is ~ 1.e-16 (Epsilon(I))
        """

    @overload
    def HasSymmetryPoint(self) -> bool:
        """
        returns true if the geometric system has a point of symmetry.
        For comparing moments relative tolerance 1.e-10 is used.
        Usually it is enough for objects, restricted by faces with
        analytical geometry.
        """

    @overload
    def HasSymmetryPoint(self, aTol: float) -> bool:
        """
        returns true if the geometric system has a point of symmetry.
        aTol is relative tolerance for checking equality of moments
        If aTol == 0, relative tolerance is ~ 1.e-16 (Epsilon(I))
        """

    def Moments(self) -> tuple[float, float, float]:
        """
        Ixx, Iyy and Izz return the principal moments of inertia
        in the current system.
        Notes :
        - If the current system has an axis of symmetry, two
        of the three values Ixx, Iyy and Izz are equal. They
        indicate which eigen vectors define an infinity of
        axes of principal inertia.
        - If the current system has a center of symmetry, Ixx,
        Iyy and Izz are equal.
        """

    def FirstAxisOfInertia(self) -> nanoocp.gp.gp_Vec:
        """
        returns the first axis of inertia.

        if the system has a point of symmetry there is an infinity of
        solutions. It is not possible to defines the three axis of
        inertia.
        """

    def SecondAxisOfInertia(self) -> nanoocp.gp.gp_Vec:
        """
        returns the second axis of inertia.

        if the system has a point of symmetry or an axis of symmetry the
        second and the third axis of symmetry are undefined.
        """

    def ThirdAxisOfInertia(self) -> nanoocp.gp.gp_Vec:
        """
        returns the third axis of inertia.
        This and the above functions return the first, second or third eigen vector of the
        matrix of inertia of the current system.
        The first, second and third principal axis of inertia
        pass through the center of mass of the current
        system. They are respectively parallel to these three eigen vectors.
        Note that:
        - If the current system has an axis of symmetry, any
        axis is an axis of principal inertia if it passes
        through the center of mass of the system, and runs
        parallel to a linear combination of the two eigen
        vectors of the matrix of inertia, corresponding to the
        two eigen values which are equal. If the current
        system has a center of symmetry, any axis passing
        through the center of mass of the system is an axis
        of principal inertia. Use the functions
        HasSymmetryAxis and HasSymmetryPoint to
        check these particular cases, where the returned
        eigen vectors define an infinity of principal axis of inertia.
        - The Moments function can be used to know which
        of the three eigen vectors corresponds to the two
        eigen values which are equal.

        if the system has a point of symmetry or an axis of symmetry the
        second and the third axis of symmetry are undefined.
        """

    def RadiusOfGyration(self) -> tuple[float, float, float]:
        """
        Returns the principal radii of gyration Rxx, Ryy
        and Rzz are the radii of gyration of the current
        system about its three principal axes of inertia.
        Note that:
        - If the current system has an axis of symmetry,
        two of the three values Rxx, Ryy and Rzz are equal.
        - If the current system has a center of symmetry,
        Rxx, Ryy and Rzz are equal.
        """

class GProp_SelGProps(GProp_GProps):
    """
    Computes the global properties of a bounded elementary surface in 3D
    (surfaces from the gp package: Cylinder, Cone, Sphere, Torus).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: GProp_SelGProps) -> None: ...

    def SetLocation(self, SLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...

class GProp_UndefinedAxis(nanoocp.Standard.Standard_DomainError):
    pass

class GProp_VelGProps(GProp_GProps):
    """
    Computes the global properties and the volume of a geometric solid
    (3D closed region of space). Supports elementary solids from the gp
    package: Cylinder, Cone, Sphere, Torus.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, S: nanoocp.gp.gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: GProp_VelGProps) -> None: ...

    def SetLocation(self, VLocation: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...

    @overload
    def Perform(self, S: nanoocp.gp.gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...
