"""OCCT package BRepFill (toolkit TKBool)"""

import enum
from typing import overload

import nanoocp.Adaptor3d
import nanoocp.AppCont
import nanoocp.AppParCurves
import nanoocp.BRepMAT2d
import nanoocp.Bisector
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.GeomFill
import nanoocp.GeomPlate
import nanoocp.Law
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopoDS
import nanoocp.gp


class BRepFill_ThruSectionErrorStatus(enum.IntEnum):
    """Errors that can occur at thrusection algorithm."""

    BRepFill_ThruSectionErrorStatus_Done = 0

    BRepFill_ThruSectionErrorStatus_NotDone = 1

    BRepFill_ThruSectionErrorStatus_NotSameTopology = 2

    BRepFill_ThruSectionErrorStatus_ProfilesInconsistent = 3

    BRepFill_ThruSectionErrorStatus_WrongUsage = 4

    BRepFill_ThruSectionErrorStatus_Null3DCurve = 5

    BRepFill_ThruSectionErrorStatus_Failed = 6

BRepFill_ThruSectionErrorStatus_Done: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_NotDone: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_NotSameTopology: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_ProfilesInconsistent: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_WrongUsage: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_Null3DCurve: BRepFill_ThruSectionErrorStatus = ...

BRepFill_ThruSectionErrorStatus_Failed: BRepFill_ThruSectionErrorStatus = ...

class BRepFill_TransitionStyle(enum.IntEnum):
    BRepFill_Modified = 0

    BRepFill_Right = 1

    BRepFill_Round = 2

BRepFill_Modified: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Modified

BRepFill_Right: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Right

BRepFill_Round: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Round

class BRepFill_TypeOfContact(enum.IntEnum):
    """A pair of bound shapes with the result."""

    BRepFill_NoContact = 0

    BRepFill_Contact = 1

    BRepFill_ContactOnBorder = 2

BRepFill_NoContact: BRepFill_TypeOfContact = BRepFill_TypeOfContact.BRepFill_NoContact

BRepFill_Contact: BRepFill_TypeOfContact = BRepFill_TypeOfContact.BRepFill_Contact

BRepFill_ContactOnBorder: BRepFill_TypeOfContact = BRepFill_TypeOfContact.BRepFill_ContactOnBorder

class BRepFill:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill) -> None: ...

    @staticmethod
    def Face(Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Face:
        """Computes a ruled surface between two edges."""

    @staticmethod
    def Shell(Wire1: nanoocp.TopoDS.TopoDS_Wire, Wire2: nanoocp.TopoDS.TopoDS_Wire) -> nanoocp.TopoDS.TopoDS_Shell:
        """
        Computes a ruled surface between two wires.
        The wires must have the same number of edges.
        """

    @staticmethod
    def Axe(Spine: nanoocp.TopoDS.TopoDS_Shape, Profile: nanoocp.TopoDS.TopoDS_Wire, AxeProf: nanoocp.gp.gp_Ax3, Tol: float) -> bool:
        """
        Computes <AxeProf> as Follow. <Location> is
        the Position of the nearest vertex V of <Profile>
        to <Spine>.<XDirection> is confused with the tangent
        to <Spine> at the projected point of V on the Spine.
        <Direction> is normal to <Spine>.
        <Spine> is a plane wire or a plane face.
        """

    @staticmethod
    def ComputeACR(wire: nanoocp.TopoDS.TopoDS_Wire, ACR: nanoocp.NCollection.NCollection_Array1[float]) -> None:
        """Compute ACR on a wire"""

    @staticmethod
    def InsertACR(wire: nanoocp.TopoDS.TopoDS_Wire, ACRcuts: nanoocp.NCollection.NCollection_Array1[float], prec: float) -> nanoocp.TopoDS.TopoDS_Wire:
        """Insert ACR on a wire"""

class BRepFill_LocationLaw(nanoocp.Standard.Standard_Transient):
    """Location Law on a Wire."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_LocationLaw) -> None: ...

    def GetStatus(self) -> nanoocp.GeomFill.GeomFill_PipeError:
        """
        Return a error status, if the status is not PipeOk then
        it exist a parameter tlike the law is not valuable for t.
        """

    def TransformInG0Law(self) -> None:
        """
        Apply a linear transformation on each law, to have
        continuity of the global law between the edges.
        """

    def TransformInCompatibleLaw(self, AngularTolerance: float) -> None:
        """
        Apply a linear transformation on each law, to reduce
        the dicontinuities of law at one rotation.
        """

    def DeleteTransform(self) -> None: ...

    def NbHoles(self, Tol: float = 1e-07) -> int: ...

    def Holes(self, Interval: nanoocp.NCollection.NCollection_Array1[int]) -> None: ...

    def NbLaw(self) -> int:
        """Return the number of elementary Law"""

    def Law(self, Index: int) -> nanoocp.GeomFill.GeomFill_LocationLaw:
        """
        Return the elementary Law of rank <Index>
        <Index> have to be in [1, NbLaw()]
        """

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """return the path"""

    def Edge(self, Index: int) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Return the Edge of rank <Index> in the path
        <Index> have to be in [1, NbLaw()]
        """

    def Vertex(self, Index: int) -> nanoocp.TopoDS.TopoDS_Vertex:
        """
        Return the vertex of rank <Index> in the path
        <Index> have to be in [0, NbLaw()]
        """

    def PerformVertex(self, Index: int, InputVertex: nanoocp.TopoDS.TopoDS_Vertex, TolMin: float, OutputVertex: nanoocp.TopoDS.TopoDS_Vertex, Location: int = 0) -> None:
        """
        Compute <OutputVertex> like a transformation of
        <InputVertex> the transformation is given by
        evaluation of the location law in the vertex of
        rank <Index>.
        <Location> is used to manage discontinuities:
        - -1 : The law before the vertex is used.
        -  1 : The law after the vertex is used.
        -  0 : Average of the both laws is used.
        """

    def CurvilinearBounds(self, Index: int) -> tuple[float, float]:
        """Return the Curvilinear Bounds of the <Index> Law"""

    def IsClosed(self) -> bool: ...

    def IsG1(self, Index: int, SpatialTolerance: float = 1e-07, AngularTolerance: float = 0.0001) -> int:
        """
        Compute the Law's continuity between 2 edges of the path
        The result can be :
        -1 : Case Not connex
        0  : It is connex (G0)
        1  : It is tangent (G1)
        """

    def D0(self, Abscissa: float, Section: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Apply the Law to a shape, for a given Curvilinear abscissa"""

    def Parameter(self, Abscissa: float) -> tuple[int, float]:
        """Find the index Law and the parameter, for a given Curvilinear abscissa"""

    def Abscissa(self, Index: int, Param: float) -> float:
        """
        Return the curvilinear abscissa corresponding to a point
        of the path, defined by <Index> of Edge and a parameter
        on the edge.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_ACRLaw(BRepFill_LocationLaw):
    """
    Build Location Law, with a Wire. In the case
    of guided contour and trihedron by reduced
    curvilinear abscissa
    """

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Wire, Law: nanoocp.GeomFill.GeomFill_LocationGuide | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_ACRLaw) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_AdvancedEvolved:
    """
    Constructs an evolved volume from a spine (wire or face)
    and a profile (wire).
    """

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BRepFill_AdvancedEvolved) -> None: ...

    def Perform(self, theSpine: nanoocp.TopoDS.TopoDS_Wire, theProfile: nanoocp.TopoDS.TopoDS_Wire, theTolerance: float, theSolidReq: bool = True) -> None: ...

    def IsDone(self) -> bool: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns the resulting shape."""

    def SetTemporaryDirectory(self, thePath: str) -> None:
        """Sets directory where the debug shapes will be saved"""

    def SetParallelMode(self, theVal: bool) -> None:
        """Sets/Unsets computation in parallel mode"""

class BRepFill_MultiLine(nanoocp.AppCont.AppCont_Function):
    """
    Class used to compute the 3d curve and the
    two 2d curves resulting from the intersection of a
    surface of linear extrusion( Bissec, Dz) and the 2
    faces.
    These 3 curves will have the same parametrization
    as the Bissectrice.
    This class is to be sent to an approximation
    routine.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Face1: nanoocp.TopoDS.TopoDS_Face, Face2: nanoocp.TopoDS.TopoDS_Face, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Inv1: bool, Inv2: bool, Bissec: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_MultiLine) -> None: ...

    def IsParticularCase(self) -> bool:
        """
        Search if the Projection of the Bissectrice on the
        faces needs an approximation or not.
        Returns true if the approximation is not needed.
        """

    def Continuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """
        Returns the continuity between the two faces
        seShape from GeomAbsparated by myBis.
        """

    def Curves(self) -> tuple[nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve]:
        """raises if IsParticularCase is <False>."""

    def FirstParameter(self) -> float:
        """returns the first parameter of the Bissectrice."""

    def LastParameter(self) -> float:
        """returns the last parameter of the Bissectrice."""

    @overload
    def Value(self, U: float) -> nanoocp.gp.gp_Pnt:
        """Returns the current point on the 3d curve"""

    @overload
    def Value(self, theU: float, thePnt2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], thePnt: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> bool:
        """Returns the point at parameter <theU>."""

    def ValueOnF1(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the current point on the PCurve of the
        first face
        """

    def ValueOnF2(self, U: float) -> nanoocp.gp.gp_Pnt2d:
        """
        returns the current point on the PCurve of the
        first face
        """

    def Value3dOnF1OnF2(self, U: float, P3d: nanoocp.gp.gp_Pnt, PF1: nanoocp.gp.gp_Pnt2d, PF2: nanoocp.gp.gp_Pnt2d) -> None: ...

    def D1(self, theU: float, theVec2d: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec2d], theVec: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Vec]) -> bool:
        """Returns the derivative at parameter <theU>."""

class BRepFill_ApproxSeewing:
    """
    Evaluate the 3dCurve and the PCurves described in a MultiLine from BRepFill.
    The parametrization of those curves is not imposed by the Bissectrice.
    The parametrization is given approximately by the abscissa of the curve3d.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, ML: BRepFill_MultiLine) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_ApproxSeewing) -> None: ...

    def Perform(self, ML: BRepFill_MultiLine) -> None: ...

    def IsDone(self) -> bool: ...

    def Curve(self) -> nanoocp.Geom.Geom_Curve:
        """returns the approximation of the 3d Curve"""

    def CurveOnF1(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        returns the approximation of the PCurve on the
        first face of the MultiLine
        """

    def CurveOnF2(self) -> nanoocp.Geom2d.Geom2d_Curve:
        """
        returns the approximation of the PCurve on the
        first face of the MultiLine
        """

class BRepFill_CompatibleWires:
    """
    Constructs a sequence of Wires (with good orientation
    and origin) agreed each other so that the surface passing
    through these sections is not twisted
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Sections: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_CompatibleWires) -> None: ...

    def Init(self, Sections: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def SetPercent(self, percent: float = 0.01) -> None: ...

    def Perform(self, WithRotation: bool = True) -> None:
        """
        Performs CompatibleWires According to the orientation
        and the origin of each other
        """

    def IsDone(self) -> bool: ...

    def GetStatus(self) -> BRepFill_ThruSectionErrorStatus: ...

    def Shape(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]:
        """returns the generated sequence."""

    def GeneratedShapes(self, SubSection: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the shapes created from a subshape
        <SubSection> of a section.
        """

    def Generated(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def IsDegeneratedFirstSection(self) -> bool: ...

    def IsDegeneratedLastSection(self) -> bool: ...

class BRepFill_ComputeCLine:
    @overload
    def __init__(self, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """Initializes the fields of the algorithm."""

    @overload
    def __init__(self, Line: BRepFill_MultiLine, degreemin: int = 3, degreemax: int = 8, Tolerance3d: float = 1e-05, Tolerance2d: float = 1e-05, cutting: bool = False, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint = ..., LastC: nanoocp.AppParCurves.AppParCurves_Constraint = ...) -> None:
        """
        The MultiLine <Line> will be approximated until tolerances
        will be reached.
        The approximation will be done from degreemin to degreemax
        with a cutting if the corresponding boolean is True.
        """

    @overload
    def __init__(self, theOther: BRepFill_ComputeCLine) -> None: ...

    def Perform(self, Line: BRepFill_MultiLine) -> None:
        """runs the algorithm after having initialized the fields."""

    def SetDegrees(self, degreemin: int, degreemax: int) -> None:
        """changes the degrees of the approximation."""

    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None:
        """Changes the tolerances of the approximation."""

    def SetConstraints(self, FirstC: nanoocp.AppParCurves.AppParCurves_Constraint, LastC: nanoocp.AppParCurves.AppParCurves_Constraint) -> None:
        """Changes the constraints of the approximation."""

    def SetMaxSegments(self, theMaxSegments: int) -> None:
        """Changes the max number of segments, which is allowed for cutting."""

    def SetInvOrder(self, theInvOrder: bool) -> None:
        """
        Set inverse order of degree selection:
        if theInvOrdr = true, current degree is chosen by inverse order -
        from maxdegree to mindegree.
        By default inverse order is used.
        """

    def SetHangChecking(self, theHangChecking: bool) -> None:
        """
        Set value of hang checking flag
        if this flag = true, possible hang of algorithm is checked
        and algorithm is forced to stop.
        By default hang checking is used.
        """

    def IsAllApproximated(self) -> bool:
        """
        returns False if at a moment of the approximation,
        the status NoApproximation has been sent by the user
        when more points were needed.
        """

    def IsToleranceReached(self) -> bool:
        """returns False if the status NoPointsAdded has been sent."""

    def Error(self, Index: int) -> tuple[float, float]:
        """returns the tolerances 2d and 3d of the <Index> MultiCurve."""

    def NbMultiCurves(self) -> int:
        """
        Returns the number of MultiCurve doing the approximation
        of the MultiLine.
        """

    def Value(self, Index: int = 1) -> nanoocp.AppParCurves.AppParCurves_MultiCurve:
        """returns the approximation MultiCurve of range <Index>."""

    def Parameters(self, Index: int) -> tuple[float, float]: ...

class BRepFill_CurveConstraint(nanoocp.GeomPlate.GeomPlate_CurveConstraint):
    """
    same as CurveConstraint from GeomPlate
    with BRepAdaptor_Surface instead of
    GeomAdaptor_Surface
    """

    @overload
    def __init__(self, Boundary: nanoocp.Adaptor3d.Adaptor3d_CurveOnSurface | None, Order: int, NPt: int = 10, TolDist: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1) -> None:
        """
        Create a constraint
        Order is the order of the constraint. The possible values for order are -1,0,1,2.
        Order i means constraints Gi
        Npt is the number of points associated with the constraint.
        TolDist is the maximum error to satisfy for G0 constraints
        TolAng is the maximum error to satisfy for G1 constraints
        TolCurv is the maximum error to satisfy for G2 constraints
        These errors can be replaced by laws of criterion.
        """

    @overload
    def __init__(self, Boundary: nanoocp.Adaptor3d.Adaptor3d_Curve | None, Tang: int, NPt: int = 10, TolDist: float = 0.0001) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_CurveConstraint) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_Draft:
    @overload
    def __init__(self, Shape: nanoocp.TopoDS.TopoDS_Shape, Dir: nanoocp.gp.gp_Dir, Angle: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Draft) -> None: ...

    def SetOptions(self, Style: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Right, AngleMin: float = 0.01, AngleMax: float = 3.0) -> None: ...

    def SetDraft(self, IsInternal: bool = False) -> None: ...

    @overload
    def Perform(self, LengthMax: float) -> None: ...

    @overload
    def Perform(self, Surface: nanoocp.Geom.Geom_Surface | None, KeepInsideSurface: bool = True) -> None: ...

    @overload
    def Perform(self, StopShape: nanoocp.TopoDS.TopoDS_Shape, KeepOutSide: bool = True) -> None: ...

    def IsDone(self) -> bool: ...

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell:
        """
        Returns the draft surface
        To have the complete shape
        you have to use the Shape() methode.
        """

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

class BRepFill_Edge3DLaw(BRepFill_LocationLaw):
    """Build Location Law, with a Wire."""

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Wire, Law: nanoocp.GeomFill.GeomFill_LocationLaw | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Edge3DLaw) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_DraftLaw(BRepFill_Edge3DLaw):
    """Build Location Law, with a Wire."""

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Wire, Law: nanoocp.GeomFill.GeomFill_LocationDraft | None) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_DraftLaw) -> None: ...

    def CleanLaw(self, TolAngular: float) -> None:
        """To clean the little discontinuities."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_EdgeFaceAndOrder:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, anEdge: nanoocp.TopoDS.TopoDS_Edge, aFace: nanoocp.TopoDS.TopoDS_Face, anOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_EdgeFaceAndOrder) -> None: ...

class BRepFill_EdgeOnSurfLaw(BRepFill_LocationLaw):
    """Build Location Law, with a Wire and a Surface."""

    @overload
    def __init__(self, Path: nanoocp.TopoDS.TopoDS_Wire, Surf: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_EdgeOnSurfLaw) -> None: ...

    def HasResult(self) -> bool:
        """
        returns <False> if one Edge of <Path> do not have
        representation on <Surf>. In this case it is
        impossible to use this object.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_Evolved:
    """
    Constructs an evolved volume from a spine (wire or face)
    and a profile ( wire).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Wire, AxeProf: nanoocp.gp.gp_Ax3, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Solid: bool = False) -> None:
        """
        Creates an evolved shape by sweeping the <Profile>
        along the <Spine>. <AxeProf> is used to set the
        position of <Profile> along <Spine> as follows:
        <AxeProf> slides on the profile with direction
        colinear to the normal to <Spine>, and its
        <XDirection> mixed with the tangent to <Spine>.
        """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Face, Profile: nanoocp.TopoDS.TopoDS_Wire, AxeProf: nanoocp.gp.gp_Ax3, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Solid: bool = False) -> None:
        """
        Creates an evolved shape by sweeping the <Profile>
        along the <Spine>
        """

    @overload
    def __init__(self, theOther: BRepFill_Evolved) -> None: ...

    @overload
    def Perform(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Wire, AxeProf: nanoocp.gp.gp_Ax3, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Solid: bool = False) -> None: ...

    @overload
    def Perform(self, Spine: nanoocp.TopoDS.TopoDS_Face, Profile: nanoocp.TopoDS.TopoDS_Wire, AxeProf: nanoocp.gp.gp_Ax3, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Solid: bool = False) -> None:
        """
        Performs an evolved shape by sweeping the <Profile>
        along the <Spine>
        """

    def IsDone(self) -> bool: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns the generated shape."""

    def GeneratedShapes(self, SpineShape: nanoocp.TopoDS.TopoDS_Shape, ProfShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the shapes created from a subshape
        <SpineShape> of the spine and a subshape
        <ProfShape> on the profile.
        """

    def JoinType(self) -> nanoocp.GeomAbs.GeomAbs_JoinType: ...

    def Top(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return the face Top if <Solid> is True in the constructor."""

    def Bottom(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return the face Bottom if <Solid> is True in the constructor."""

class BRepFill_FaceAndOrder:
    """A structure containing Face and Order of constraint"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aFace: nanoocp.TopoDS.TopoDS_Face, anOrder: nanoocp.GeomAbs.GeomAbs_Shape) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_FaceAndOrder) -> None: ...

class BRepFill_Filling:
    """
    N-Side Filling
    This algorithm avoids to build a face from:
    * a set of edges defining the bounds of the face and some
    constraints the surface support has to satisfy
    * a set of edges and points defining some constraints
    the support surface has to satisfy
    * an initial surface to deform for satisfying the constraints
    * a set of parameters to control the constraints.

    The support surface of the face is computed by deformation
    of the initial surface in order to satisfy the given constraints.
    The set of bounding edges defines the wire of the face.

    If no initial surface is given, the algorithm computes it
    automatically.
    If the set of edges is not connected (Free constraint)
    missing edges are automatically computed.

    Limitations:
    * If some constraints are not compatible
    The algorithm does not take them into account.
    So the constraints will not be satisfied in an area containing
    the incompatibilities.
    * The constraints defining the bound of the face have to be
    entered in order to have a continuous wire.

    Other Applications:
    * Deformation of a face to satisfy internal constraints
    * Deformation of a face to improve Gi continuity with
    connected faces
    """

    @overload
    def __init__(self, Degree: int = 3, NbPtsOnCur: int = 15, NbIter: int = 2, Anisotropie: bool = False, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1, MaxDeg: int = 8, MaxSegments: int = 9) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: BRepFill_Filling) -> None: ...

    def SetConstrParam(self, Tol2d: float = 1e-05, Tol3d: float = 0.0001, TolAng: float = 0.01, TolCurv: float = 0.1) -> None:
        """
        Sets the values of Tolerances used to control the constraint.
        Tol2d:
        Tol3d:   it is the maximum distance allowed between the support surface
        and the constraints
        TolAng:  it is the maximum angle allowed between the normal of the surface
        and the constraints
        TolCurv: it is the maximum difference of curvature allowed between
        the surface and the constraint
        """

    def SetResolParam(self, Degree: int = 3, NbPtsOnCur: int = 15, NbIter: int = 2, Anisotropie: bool = False) -> None:
        """
        Sets the parameters used for resolution.
        The default values of these parameters have been chosen for a good
        ratio quality/performance.
        Degree:      it is the order of energy criterion to minimize for computing
        the deformation of the surface.
        The default value is 3
        The recommended value is i+2 where i is the maximum order of the
        constraints.
        NbPtsOnCur:  it is the average number of points for discretisation
        of the edges.
        NbIter:      it is the maximum number of iterations of the process.
        For each iteration the number of discretisation points is
        increased.
        Anisotropie:
        """

    def SetApproxParam(self, MaxDeg: int = 8, MaxSegments: int = 9) -> None:
        """Sets the parameters used for approximation of the surface"""

    def LoadInitSurface(self, aFace: nanoocp.TopoDS.TopoDS_Face) -> None:
        """
        Loads the initial Surface
        The initial surface must have orthogonal local coordinates,
        i.e. partial derivatives dS/du and dS/dv must be orthogonal
        at each point of surface.
        If this condition breaks, distortions of resulting surface
        are possible.
        """

    @overload
    def Add(self, anEdge: nanoocp.TopoDS.TopoDS_Edge, Order: nanoocp.GeomAbs.GeomAbs_Shape, IsBound: bool = True) -> int:
        """
        Adds a new constraint which also defines an edge of the wire
        of the face
        Order: Order of the constraint:
        GeomAbs_C0 : the surface has to pass by 3D representation
        of the edge
        GeomAbs_G1 : the surface has to pass by 3D representation
        of the edge and to respect tangency with the first
        face of the edge
        GeomAbs_G2 : the surface has to pass by 3D representation
        of the edge and to respect tangency and curvature
        with the first face of the edge.
        """

    @overload
    def Add(self, anEdge: nanoocp.TopoDS.TopoDS_Edge, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape, IsBound: bool = True) -> int:
        """
        Adds a new constraint which also defines an edge of the wire
        of the face
        Order: Order of the constraint:
        GeomAbs_C0 : the surface has to pass by 3D representation
        of the edge
        GeomAbs_G1 : the surface has to pass by 3D representation
        of the edge and to respect tangency with the
        given face
        GeomAbs_G2 : the surface has to pass by 3D representation
        of the edge and to respect tangency and curvature
        with the given face.
        """

    @overload
    def Add(self, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """
        Adds a free constraint on a face. The corresponding edge has to
        be automatically recomputed.
        It is always a bound.
        """

    @overload
    def Add(self, Point: nanoocp.gp.gp_Pnt) -> int:
        """Adds a punctual constraint"""

    @overload
    def Add(self, U: float, V: float, Support: nanoocp.TopoDS.TopoDS_Face, Order: nanoocp.GeomAbs.GeomAbs_Shape) -> int:
        """Adds a punctual constraint."""

    def Build(self) -> None:
        """Builds the resulting faces"""

    def IsDone(self) -> bool: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    @overload
    def G0Error(self) -> float: ...

    @overload
    def G0Error(self, Index: int) -> float: ...

    @overload
    def G1Error(self) -> float: ...

    @overload
    def G1Error(self, Index: int) -> float: ...

    @overload
    def G2Error(self) -> float: ...

    @overload
    def G2Error(self, Index: int) -> float: ...

class BRepFill_Generator:
    """
    Compute a topological surface (a shell) using
    generating wires. The face of the shell will be
    ruled surfaces passing by the wires.
    The wires must have the same number of edges.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Generator) -> None: ...

    def AddWire(self, Wire: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def Perform(self) -> None:
        """Compute the shell."""

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell: ...

    def Generated(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns all the shapes created"""

    def GeneratedShapes(self, SSection: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the shapes created from a subshape
        <SSection> of a section.
        """

    def ResultShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a modified shape in the constructed shell,
        If shape is not changed (replaced) during operation => returns the same shape
        """

    def SetMutableInput(self, theIsMutableInput: bool) -> None:
        """
        Sets the mutable input state
        If true then the input profile can be modified
        inside the operation. Default value is true.
        """

    def IsMutableInput(self) -> bool:
        """Returns the current mutable input state"""

    def GetStatus(self) -> BRepFill_ThruSectionErrorStatus:
        """Returns status of the operation"""

class BRepFill_SectionLaw(nanoocp.Standard.Standard_Transient):
    """Build Section Law, with an Vertex, or an Wire"""

    def NbLaw(self) -> int: ...

    def Law(self, Index: int) -> nanoocp.GeomFill.GeomFill_SectionLaw: ...

    def IndexOfEdge(self, anEdge: nanoocp.TopoDS.TopoDS_Shape) -> int: ...

    def IsConstant(self) -> bool: ...

    def IsUClosed(self) -> bool: ...

    def IsVClosed(self) -> bool: ...

    def IsDone(self) -> bool: ...

    def IsVertex(self) -> bool:
        """Say if the input shape is a vertex."""

    def ConcatenedLaw(self) -> nanoocp.GeomFill.GeomFill_SectionLaw: ...

    def Continuity(self, Index: int, TolAngular: float) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VertexTol(self, Index: int, Param: float) -> float: ...

    def Vertex(self, Index: int, Param: float) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def D0(self, U: float, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def CurrentEdge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_NSections(BRepFill_SectionLaw):
    """Build Section Law, with N Sections"""

    @overload
    def __init__(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape], Build: bool = True) -> None: ...

    @overload
    def __init__(self, S: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape], Trsfs: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Trsf], P: nanoocp.NCollection.NCollection_Sequence[float], VF: float, VL: float, Build: bool = True) -> None:
        """Construct"""

    @overload
    def __init__(self, theOther: BRepFill_NSections) -> None: ...

    def IsVertex(self) -> bool:
        """Say if the input shape is a vertex."""

    def IsConstant(self) -> bool:
        """Say if the Law is Constant."""

    def ConcatenedLaw(self) -> nanoocp.GeomFill.GeomFill_SectionLaw:
        """Give the law build on a concatenated section"""

    def Continuity(self, Index: int, TolAngular: float) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VertexTol(self, Index: int, Param: float) -> float: ...

    def Vertex(self, Index: int, Param: float) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def D0(self, Param: float, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_OffsetAncestors:
    """
    this class is used to find the generating shapes
    of an OffsetWire.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Paral: BRepFill_OffsetWire) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_OffsetAncestors) -> None: ...

    def Perform(self, Paral: BRepFill_OffsetWire) -> None: ...

    def IsDone(self) -> bool: ...

    def HasAncestor(self, S1: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def Ancestor(self, S1: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        may return a Null Shape if S1 is not a subShape
        of <Paral>;
        if Perform is not done.
        """

class BRepFill_OffsetWire:
    """
    Constructs a Offset Wire to a spine (wire or face).
    Offset direction will be to outer region in case of
    positive offset value and to inner region in case of
    negative offset value.
    Inner/Outer region for open wire is defined by the
    following rule: when we go along the wire (taking into
    account of edges orientation) then outer region will be
    on the right side, inner region will be on the left side.
    In case of closed wire, inner region will always be
    inside the wire (at that, edges orientation is not taken
    into account).
    The Wire or the Face must be planar and oriented correctly.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Face, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_OffsetWire) -> None: ...

    def Init(self, Spine: nanoocp.TopoDS.TopoDS_Face, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, IsOpenResult: bool = False) -> None:
        """Initialize the evaluation of Offsetting."""

    def Perform(self, Offset: float, Alt: float = 0.0) -> None:
        """
        Performs an OffsetWire at an altitude <Alt> from
        the face (According to the orientation of the
        face)
        """

    def PerformWithBiLo(self, WSP: nanoocp.TopoDS.TopoDS_Face, Offset: float, Locus: nanoocp.BRepMAT2d.BRepMAT2d_BisectingLocus, Link: nanoocp.BRepMAT2d.BRepMAT2d_LinkTopoBilo, Join: nanoocp.GeomAbs.GeomAbs_JoinType = GeomAbs_JoinType.GeomAbs_Arc, Alt: float = 0.0) -> None:
        """Performs an OffsetWire"""

    def IsDone(self) -> bool: ...

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """returns the generated shape."""

    def GeneratedShapes(self, SpineShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the shapes created from a subshape
        <SpineShape> of the spine.
        Returns the last computed Offset.
        """

    def JoinType(self) -> nanoocp.GeomAbs.GeomAbs_JoinType: ...

class BRepFill_Pipe:
    """
    Create a shape by sweeping a shape (the profile)
    along a wire (the spine).

    For each edge or vertex from the spine the user
    may ask for the shape generated from each subshape
    of the profile.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Shape, aMode: nanoocp.GeomFill.GeomFill_Trihedron = GeomFill_Trihedron.GeomFill_IsCorrectedFrenet, ForceApproxC1: bool = False, GeneratePartCase: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Pipe) -> None: ...

    def Perform(self, Spine: nanoocp.TopoDS.TopoDS_Wire, Profile: nanoocp.TopoDS.TopoDS_Shape, GeneratePartCase: bool = False) -> None: ...

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Profile(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ErrorOnSurface(self) -> float: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    def Face(self, ESpine: nanoocp.TopoDS.TopoDS_Edge, EProfile: nanoocp.TopoDS.TopoDS_Edge) -> nanoocp.TopoDS.TopoDS_Face:
        """
        Returns the face created from an edge of the spine
        and an edge of the profile.
        if the edges are not in the spine or the profile
        """

    def Edge(self, ESpine: nanoocp.TopoDS.TopoDS_Edge, VProfile: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.TopoDS.TopoDS_Edge:
        """
        Returns the edge created from an edge of the spine
        and a vertex of the profile.
        if the edge or the vertex are not in the spine or
        the profile.
        """

    def Section(self, VSpine: nanoocp.TopoDS.TopoDS_Vertex) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape created from the profile at the
        position of the vertex VSpine.
        if the vertex is not in the Spine
        """

    def PipeLine(self, Point: nanoocp.gp.gp_Pnt) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Create a Wire by sweeping the Point along the <spine>
        if the <Spine> is undefined
        """

class BRepFill_Section:
    """To store section definition"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Profile: nanoocp.TopoDS.TopoDS_Shape, V: nanoocp.TopoDS.TopoDS_Vertex, WithContact: bool, WithCorrection: bool) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Section) -> None: ...

    def Set(self, IsLaw: bool) -> None: ...

    def OriginalShape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire: ...

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def ModifiedShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def IsLaw(self) -> bool: ...

    def IsPunctual(self) -> bool: ...

    def WithContact(self) -> bool: ...

    def WithCorrection(self) -> bool: ...

class BRepFill_PipeShell(nanoocp.Standard.Standard_Transient):
    """
    Computes a topological shell using some wires
    (spines and profiles) and displacement option
    Perform general sweeping construction
    """

    @overload
    def __init__(self, Spine: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """
        Set an sweep's mode
        If no mode are set, the mode used in MakePipe is used
        """

    @overload
    def __init__(self, theOther: BRepFill_PipeShell) -> None: ...

    @overload
    def Set(self, Frenet: bool = False) -> None:
        """
        Set an Frenet or an CorrectedFrenet trihedron
        to perform the sweeping
        """

    @overload
    def Set(self, Axe: nanoocp.gp.gp_Ax2) -> None:
        """
        Set an fixed trihedron to perform the sweeping
        all sections will be parallel.
        """

    @overload
    def Set(self, BiNormal: nanoocp.gp.gp_Dir) -> None:
        """
        Set an fixed BiNormal direction to perform
        the sweeping
        """

    @overload
    def Set(self, SpineSupport: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Set support to the spine to define the BiNormal
        at the spine, like the normal the surfaces.
        Warning: To be effective, Each edge of the <spine> must
        have an representation on one face of<SpineSupport>
        """

    @overload
    def Set(self, AuxiliarySpine: nanoocp.TopoDS.TopoDS_Wire, CurvilinearEquivalence: bool = True, KeepContact: BRepFill_TypeOfContact = BRepFill_TypeOfContact.BRepFill_NoContact) -> None:
        """
        Set an auxiliary spine to define the Normal
        For each Point of the Spine P, an Point Q is evaluated
        on <AuxiliarySpine>
        If <CurvilinearEquivalence>
        Q split <AuxiliarySpine> with the same length ratio
        than P split <Spline>.
        Else the plan define by P and the tangent to the <Spine>
        intersect <AuxiliarySpine> in Q.
        If <KeepContact> equals BRepFill_NoContact: The Normal is defined
        by the vector PQ.
        If <KeepContact> equals BRepFill_Contact: The Normal is defined to
        achieve that the sweeped section is in contact to the
        auxiliarySpine. The width of section is constant all along the path.
        In other words, the auxiliary spine lies on the swept surface,
        but not necessarily is a boundary of this surface. However,
        the auxiliary spine has to be close enough to the main spine
        to provide intersection with any section all along the path.
        If <KeepContact> equals BRepFill_ContactOnBorder: The auxiliary spine
        becomes a boundary of the swept surface and the width of section varies
        along the path.
        """

    def SetDiscrete(self) -> None:
        """Set a Discrete trihedron to perform the sweeping"""

    def SetMaxDegree(self, NewMaxDegree: int) -> None:
        """Define the maximum V degree of resulting surface"""

    def SetMaxSegments(self, NewMaxSegments: int) -> None:
        """
        Define the maximum number of spans in V-direction
        on resulting surface
        """

    def SetForceApproxC1(self, ForceApproxC1: bool) -> None:
        """
        Set the flag that indicates attempt to approximate
        a C1-continuous surface if a swept surface proved
        to be C0.
        Give section to sweep.
        Possibilities are:
        - Give one or several profile
        - Give one profile and an homotetic law.
        - Automatic compute of correspondence between profile, and section on the sweeped shape
        - correspondence between profile, and section on the sweeped shape defined by a vertex of the
        spine
        """

    def SetIsBuildHistory(self, theIsBuildHistory: bool) -> None:
        """
        Sets the build history flag.
        If set to True, the pipe shell will store the history of the sections
        and the spine, which can be used for further modifications or analysis.
        """

    def IsBuildHistory(self) -> bool:
        """
        Returns the build history flag.
        If True, the pipe shell stores the history of the sections and the spine.
        """

    @overload
    def Add(self, Profile: nanoocp.TopoDS.TopoDS_Shape, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Set an section. The correspondence with the spine, will be automatically performed.
        """

    @overload
    def Add(self, Profile: nanoocp.TopoDS.TopoDS_Shape, Location: nanoocp.TopoDS.TopoDS_Vertex, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Set an section. The correspondence with the spine, is given by Location.
        """

    @overload
    def SetLaw(self, Profile: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.Law.Law_Function | None, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Set an section and an homotetic law.
        The homotetie's centers is given by point on the <Spine>.
        """

    @overload
    def SetLaw(self, Profile: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.Law.Law_Function | None, Location: nanoocp.TopoDS.TopoDS_Vertex, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """
        Set an section and an homotetic law.
        The homotetie center is given by point on the <Spine>
        """

    def DeleteProfile(self, Profile: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Delete an section."""

    def IsReady(self) -> bool:
        """
        Say if <me> is ready to build the shape
        return False if <me> do not have section definition
        """

    def GetStatus(self) -> nanoocp.GeomFill.GeomFill_PipeError:
        """Get a status, when Simulate or Build failed."""

    def SetTolerance(self, Tol3d: float = 0.0001, BoundTol: float = 0.0001, TolAngular: float = 0.01) -> None: ...

    def SetTransition(self, Mode: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Modified, Angmin: float = 0.01, Angmax: float = 6.0) -> None:
        """
        Set the Transition Mode to manage discontinuities
        on the sweep.
        """

    def Simulate(self, NumberOfSection: int, Sections: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Perform simulation of the sweep:
        Some Section are returned.
        """

    def Build(self) -> bool:
        """Builds the resulting shape (redefined from MakeShape)."""

    def MakeSolid(self) -> bool:
        """
        Transform the sweeping Shell in Solid.
        If the section are not closed returns False
        """

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the result Shape."""

    def ErrorOnSurface(self) -> float: ...

    def FirstShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the bottom of the sweep."""

    def LastShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the TopoDS Shape of the top of the sweep."""

    def Profiles(self, theProfiles: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Returns the list of original profiles"""

    def Spine(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns the spine"""

    def Generated(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Returns the list of shapes generated from the
        shape <S>.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_SectionPlacement:
    """Place a shape in a local axis coordinate"""

    @overload
    def __init__(self, Law: BRepFill_LocationLaw | None, Section: nanoocp.TopoDS.TopoDS_Shape, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """Automatic placement"""

    @overload
    def __init__(self, Law: BRepFill_LocationLaw | None, Section: nanoocp.TopoDS.TopoDS_Shape, Vertex: nanoocp.TopoDS.TopoDS_Shape, WithContact: bool = False, WithCorrection: bool = False) -> None:
        """Placement on vertex"""

    @overload
    def __init__(self, theOther: BRepFill_SectionPlacement) -> None: ...

    def Transformation(self) -> nanoocp.gp.gp_Trsf: ...

    def AbscissaOnPath(self) -> float: ...

class BRepFill_ShapeLaw(BRepFill_SectionLaw):
    """Build Section Law, with an Vertex, or an Wire"""

    @overload
    def __init__(self, V: nanoocp.TopoDS.TopoDS_Vertex, Build: bool = True) -> None: ...

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, Build: bool = True) -> None:
        """Construct an constant Law"""

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, L: nanoocp.Law.Law_Function | None, Build: bool = True) -> None:
        """Construct an evolutive Law"""

    @overload
    def __init__(self, theOther: BRepFill_ShapeLaw) -> None: ...

    def IsVertex(self) -> bool:
        """Say if the input shape is a vertex."""

    def IsConstant(self) -> bool:
        """Say if the Law is Constant."""

    def ConcatenedLaw(self) -> nanoocp.GeomFill.GeomFill_SectionLaw:
        """Give the law build on a concatenated section"""

    def Continuity(self, Index: int, TolAngular: float) -> nanoocp.GeomAbs.GeomAbs_Shape: ...

    def VertexTol(self, Index: int, Param: float) -> float: ...

    def Vertex(self, Index: int, Param: float) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def D0(self, Param: float, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Edge(self, Index: int) -> nanoocp.TopoDS.TopoDS_Edge: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class BRepFill_Sweep:
    """
    Topological Sweep Algorithm
    Computes an Sweep shell using a generating
    wire, an SectionLaw and an LocationLaw.
    """

    @overload
    def __init__(self, Section: BRepFill_SectionLaw | None, Location: BRepFill_LocationLaw | None, WithKPart: bool) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_Sweep) -> None: ...

    def SetBounds(self, FirstShape: nanoocp.TopoDS.TopoDS_Wire, LastShape: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def SetTolerance(self, Tol3d: float, BoundTol: float = 1.0, Tol2d: float = 1e-05, TolAngular: float = 0.01) -> None:
        """
        Set Approximation Tolerance
        Tol3d : Tolerance to surface approximation
        Tol2d : Tolerance used to perform curve approximation
        Normally the 2d curve are approximated with a
        tolerance given by the resolution on support surfaces,
        but if this tolerance is too large Tol2d is used.
        TolAngular : Tolerance (in radian) to control the angle
        between tangents on the section law and
        tangent of iso-v on approximated surface
        """

    def SetAngularControl(self, AngleMin: float = 0.01, AngleMax: float = 6.0) -> None:
        """
        Tolerance  To controle Corner management.

        If the discontinuity is lesser than <AngleMin> in radian The
        Transition Performed will be always "Modified\"
        """

    def SetForceApproxC1(self, ForceApproxC1: bool) -> None:
        """
        Set the flag that indicates attempt to approximate
        a C1-continuous surface if a swept surface proved
        to be C0.
        """

    def Build(self, ReversedEdges: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], Tapes: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], Rails: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher], Transition: BRepFill_TransitionStyle = BRepFill_TransitionStyle.BRepFill_Modified, Continuity: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C2, Approx: nanoocp.GeomFill.GeomFill_ApproxStyle = GeomFill_ApproxStyle.GeomFill_Location, Degmax: int = 11, Segmax: int = 30) -> None:
        """
        Build the Sweep Surface
        Transition define Transition strategy
        Approx define Approximation Strategy
        - GeomFill_Section : The composed Function Location X Section
        is directly approximated.
        - GeomFill_Location : The location law is approximated, and the
        SweepSurface builds an algebraic composition
        of approximated location law and section law
        This option is Ok, if Section.Surface() methode
        is effective.
        Continuity : The continuity in v waiting on the surface
        Degmax     : The maximum degree in v required on the surface
        Segmax     : The maximum number of span in v required on
        the surface.
        """

    def IsDone(self) -> bool:
        """Say if the Shape is Build."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the Sweeping Shape"""

    def ErrorOnSurface(self) -> float:
        """Get the Approximation error."""

    def SubShape(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape]: ...

    def InterFaces(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Sections(self) -> nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape]: ...

    def Tape(self, Index: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the Tape corresponding to Index-th edge of section"""

class BRepFill_TrimEdgeTool:
    """Geometric Tool using to construct Offset Wires."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Bisec: nanoocp.Bisector.Bisector_Bisec, S1: nanoocp.Geom2d.Geom2d_Geometry | None, S2: nanoocp.Geom2d.Geom2d_Geometry | None, Offset: float) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_TrimEdgeTool) -> None: ...

    def IntersectWith(self, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, InitShape1: nanoocp.TopoDS.TopoDS_Shape, InitShape2: nanoocp.TopoDS.TopoDS_Shape, End1: nanoocp.TopoDS.TopoDS_Vertex, End2: nanoocp.TopoDS.TopoDS_Vertex, theJoinType: nanoocp.GeomAbs.GeomAbs_JoinType, IsOpenResult: bool, Params: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> None: ...

    def AddOrConfuse(self, Start: bool, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Params: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> None: ...

    def IsInside(self, P: nanoocp.gp.gp_Pnt2d) -> bool: ...

class BRepFill_TrimShellCorner:
    """Trims sets of faces in the corner to make proper parts of pipe"""

    @overload
    def __init__(self, theFaces: nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape] | None, theTransition: BRepFill_TransitionStyle, theAxeOfBisPlane: nanoocp.gp.gp_Ax2, theIntPointCrossDir: nanoocp.gp.gp_Vec) -> None:
        """
        Constructor: takes faces to intersect,
        type of transition (it can be RightCorner or RoundCorner)
        and axis of bisector plane
        theIntersectPointCrossDirection : prev path direction at the origin point of theAxeOfBisPlane
        cross next path direction at the origin point of theAxeOfBisPlane. used when EE has more than
        one vertices
        """

    @overload
    def __init__(self, theOther: BRepFill_TrimShellCorner) -> None: ...

    def AddBounds(self, Bounds: nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape] | None) -> None: ...

    def AddUEdges(self, theUEdges: nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape] | None) -> None: ...

    def AddVEdges(self, theVEdges: nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape] | None, theIndex: int) -> None: ...

    def Perform(self) -> None: ...

    def IsDone(self) -> bool: ...

    def HasSection(self) -> bool: ...

    def Modified(self, S: nanoocp.TopoDS.TopoDS_Shape, theModified: nanoocp.NCollection.NCollection_List[nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

class BRepFill_TrimSurfaceTool:
    """
    Compute the Pcurves and the 3d curves resulting
    of the trimming of a face by an extruded surface.
    """

    @overload
    def __init__(self, Bis: nanoocp.Geom2d.Geom2d_Curve | None, Face1: nanoocp.TopoDS.TopoDS_Face, Face2: nanoocp.TopoDS.TopoDS_Face, Edge1: nanoocp.TopoDS.TopoDS_Edge, Edge2: nanoocp.TopoDS.TopoDS_Edge, Inv1: bool, Inv2: bool) -> None: ...

    @overload
    def __init__(self, theOther: BRepFill_TrimSurfaceTool) -> None: ...

    def IntersectWith(self, EdgeOnF1: nanoocp.TopoDS.TopoDS_Edge, EdgeOnF2: nanoocp.TopoDS.TopoDS_Edge, Points: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt]) -> None:
        """
        Intersect <Bis> with the projection of the edges
        <EdgeOnFi> and returns the intersecting parameters
        on Bis and on the edges
        P.X() : Parameter on Bis
        P.Y() : Parameter on EdgeOnF1
        P.Z() : Parameter on EdgeOnF2
        raises if <Edge> is not a edge of Face1 or Face2.
        """

    def IsOnFace(self, Point: nanoocp.gp.gp_Pnt2d) -> bool:
        """returns True if the Line (P, DZ) intersect the Faces"""

    def ProjOn(self, Point: nanoocp.gp.gp_Pnt2d, Edge: nanoocp.TopoDS.TopoDS_Edge) -> float:
        """
        returns the parameter of the point <Point> on the
        Edge <Edge>, assuming that the point is on the edge.
        """

    def Project(self, U1: float, U2: float) -> tuple[nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.GeomAbs.GeomAbs_Shape]: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopTools
BRepFill_DataMapOfShapeHArray2OfShape = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.NCollection.NCollection_HArray2[nanoocp.TopoDS.TopoDS_Shape], nanoocp.TopTools.TopTools_ShapeMapHasher]
