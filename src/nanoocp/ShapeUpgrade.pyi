"""OCCT package ShapeUpgrade (toolkit TKShHealing)"""

from typing import overload

import nanoocp.BRepTools
import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.GeomAbs
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.ShapeAnalysis
import nanoocp.ShapeBuild
import nanoocp.ShapeExtend
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.TopTools


class ShapeUpgrade:
    """
    This package provides tools for splitting and converting shapes by some criteria.
    It provides modifications of the kind when one topological
    object can be converted or split in to several ones.
    In particular this package contains high level API classes which perform:
    converting geometry of shapes up to given continuity,
    splitting revolutions by U to segments less than given value,
    converting to beziers, splitting closed faces.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeUpgrade) -> None: ...

    @overload
    @staticmethod
    def C0BSplineToSequenceOfC1BSplineCurve(BS: nanoocp.Geom.Geom_BSplineCurve | None) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Geom.Geom_BoundedCurve]]:
        """Unifies same domain faces and edges of specified shape"""

    @overload
    @staticmethod
    def C0BSplineToSequenceOfC1BSplineCurve(BS: nanoocp.Geom2d.Geom2d_BSplineCurve | None) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Geom2d.Geom2d_BoundedCurve]]:
        """
        Converts C0 B-Spline curve into sequence of C1 B-Spline curves.
        This method splits B-Spline at the knots with multiplicities equal to degree,
        i.e. unlike method GeomConvert::C0BSplineToArrayOfC1BSplineCurve
        this one does not use any tolerance and therefore does not change the geometry of B-Spline.
        Returns True if C0 B-Spline was successfully split,
        else returns False (if BS is C1 B-Spline).
        """

class ShapeUpgrade_Tool(nanoocp.Standard.Standard_Transient):
    """
    Tool is a root class for splitting classes
    Provides context for recording changes, basic
    precision value and limit (minimal and maximal)
    values for tolerances
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_Tool) -> None: ...

    def Set(self, tool: ShapeUpgrade_Tool | None) -> None:
        """Copy all fields from another Root object"""

    def SetContext(self, context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> None:
        """Sets context"""

    def Context(self) -> nanoocp.ShapeBuild.ShapeBuild_ReShape:
        """Returns context"""

    def SetPrecision(self, preci: float) -> None:
        """Sets basic precision value"""

    def Precision(self) -> float:
        """Returns basic precision value"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance"""

    def MinTolerance(self) -> float:
        """Returns minimal allowed tolerance"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance"""

    def MaxTolerance(self) -> float:
        """Returns maximal allowed tolerance"""

    def LimitTolerance(self, toler: float) -> float:
        """Returns tolerance limited by [myMinTol,myMaxTol]"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_EdgeDivide(ShapeUpgrade_Tool):
    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_EdgeDivide) -> None: ...

    def Clear(self) -> None: ...

    def SetFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets supporting surface by face"""

    def Compute(self, E: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    def HasCurve2d(self) -> bool: ...

    def HasCurve3d(self) -> bool: ...

    def Knots2d(self) -> nanoocp.NCollection.NCollection_HSequence[float]: ...

    def Knots3d(self) -> nanoocp.NCollection.NCollection_HSequence[float]: ...

    def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d | None) -> None:
        """Sets the tool for splitting pcurves."""

    def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d | None) -> None:
        """Sets the tool for splitting 3D curves."""

    def GetSplitCurve2dTool(self) -> ShapeUpgrade_SplitCurve2d:
        """Returns the tool for splitting pcurves."""

    def GetSplitCurve3dTool(self) -> ShapeUpgrade_SplitCurve3d:
        """Returns the tool for splitting 3D curves."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ClosedEdgeDivide(ShapeUpgrade_EdgeDivide):
    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ClosedEdgeDivide) -> None: ...

    def Compute(self, anEdge: nanoocp.TopoDS.TopoDS_Edge) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_FaceDivide(ShapeUpgrade_Tool):
    """
    Divides a Face (both edges in the wires, by splitting
    curves and pcurves, and the face itself, by splitting
    supporting surface) according to splitting criteria.
    * The domain of the face to divide is defined by the PCurves
    of the wires on the Face.

    * all the PCurves are supposed to be defined (in the parametric
    space of the supporting surface).

    The result is available after the call to the Build method.
    It is a Shell containing all the resulting Faces.

    All the modifications made during splitting are recorded in the
    external context (ShapeBuild_ReShape).
    """

    @overload
    def __init__(self) -> None:
        """Creates empty constructor."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize by a Face."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_FaceDivide) -> None: ...

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize by a Face."""

    def SetSurfaceSegmentMode(self, Segment: bool) -> None:
        """
        Purpose sets mode for trimming (segment) surface by
        wire UV bounds.
        """

    def Perform(self, theArea: float = 0.0) -> bool:
        """
        Performs splitting and computes the resulting shell
        The context is used to keep track of former splittings
        in order to keep sharings. It is updated according to
        modifications made.
        The optional argument <theArea> is used to initialize
        the tool for splitting surface in the case of
        splitting into N parts where N is user-defined.
        """

    def SplitSurface(self, theArea: float = 0.0) -> bool:
        """
        Performs splitting of surface and computes the shell
        from source face.
        The optional argument <theArea> is used to initialize
        the tool for splitting surface in the case of
        splitting into N parts where N is user-defined.
        """

    def SplitCurves(self) -> bool:
        """
        Performs splitting of curves of all the edges in the
        shape and divides these edges.
        """

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives the resulting Shell, or Face, or Null shape if not done."""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries the status of last call to Perform
        OK   : no splitting was done (or no call to Perform)
        DONE1: some edges were split
        DONE2: surface was split
        DONE3: surface was modified without splitting
        FAIL1: some fails encountered during splitting wires
        FAIL2: face cannot be split
        """

    def SetSplitSurfaceTool(self, splitSurfaceTool: ShapeUpgrade_SplitSurface | None) -> None:
        """Sets the tool for splitting surfaces."""

    def SetWireDivideTool(self, wireDivideTool: ShapeUpgrade_WireDivide | None) -> None:
        """Sets the tool for dividing edges on Face."""

    def GetSplitSurfaceTool(self) -> ShapeUpgrade_SplitSurface:
        """
        Returns the tool for splitting surfaces.
        This tool must be already initialized.
        """

    def GetWireDivideTool(self) -> ShapeUpgrade_WireDivide:
        """
        Returns the tool for dividing edges on Face.
        This tool must be already initialized.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ClosedFaceDivide(ShapeUpgrade_FaceDivide):
    """
    Divides a Face with one or more seam edge to avoid closed faces.
    Splitting is performed by U and V direction. The number of
    resulting faces can be defined by user.
    """

    @overload
    def __init__(self) -> None:
        """Creates empty constructor."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initialize by a Face."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ClosedFaceDivide) -> None: ...

    def SplitSurface(self, theArea: float = 0.0) -> bool:
        """
        Performs splitting of surface and computes the shell
        from source face.
        """

    def SetNbSplitPoints(self, num: int) -> None:
        """
        Sets the number of cutting lines by which closed face will be split.
        The resulting faces will be num+1.
        """

    def GetNbSplitPoints(self) -> int:
        """Returns the number of splitting points"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitCurve(nanoocp.Standard.Standard_Transient):
    """Splits a curve with a criterion."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitCurve) -> None: ...

    def Init(self, First: float, Last: float) -> None:
        """Initializes with curve first and last parameters."""

    def SetSplitValues(self, SplitValues: nanoocp.NCollection.NCollection_HSequence[float] | None) -> None:
        """Sets the parameters where splitting has to be done."""

    def Build(self, Segment: bool) -> None:
        """
        If Segment is True, the result is composed with
        segments of the curve bounded by the SplitValues. If
        Segment is False, the result is composed with trimmed
        Curves all based on the same complete curve.
        """

    def SplitValues(self) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        returns all the splitting values including the
        First and Last parameters of the input curve
        Merges input split values and new ones into myGlobalKnots
        """

    def Compute(self) -> None:
        """Calculates points for correction/splitting of the curve"""

    def Perform(self, Segment: bool = True) -> None:
        """
        Performs correction/splitting of the curve.
        First defines splitting values by method Compute(), then calls method Build().
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status
        OK    - no splitting is needed
        DONE1 - splitting required and gives more than one segment
        DONE2 - splitting is required, but gives only one segment (initial)
        DONE3 - geometric form of the curve or parametrisation is modified
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitCurve2d(ShapeUpgrade_SplitCurve):
    """Splits a 2d curve with a criterion."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitCurve2d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None) -> None:
        """Initializes with pcurve with its first and last parameters."""

    @overload
    def Init(self, C: nanoocp.Geom2d.Geom2d_Curve | None, First: float, Last: float) -> None:
        """Initializes with pcurve with its parameters."""

    def Build(self, Segment: bool) -> None:
        """
        If Segment is True, the result is composed with
        segments of the curve bounded by the SplitValues. If
        Segment is False, the result is composed with trimmed
        Curves all based on the same complete curve.
        """

    def GetCurves(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom2d.Geom2d_Curve]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ConvertCurve2dToBezier(ShapeUpgrade_SplitCurve2d):
    """converts/splits a 2d curve to a list of beziers"""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ConvertCurve2dToBezier) -> None: ...

    def Compute(self) -> None:
        """
        Converts curve into a list of beziers, and stores the
        splitting parameters on original curve.
        """

    def Build(self, Segment: bool) -> None:
        """
        Splits a list of beziers computed by Compute method according
        the split values and splitting parameters.
        """

    def SplitParams(self) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        Returns the list of split parameters in original curve parametrisation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitCurve3d(ShapeUpgrade_SplitCurve):
    """Splits a 3d curve with a criterion."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitCurve3d) -> None: ...

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None) -> None:
        """Initializes with curve with its first and last parameters."""

    @overload
    def Init(self, C: nanoocp.Geom.Geom_Curve | None, First: float, Last: float) -> None:
        """Initializes with curve with its parameters."""

    def Build(self, Segment: bool) -> None:
        """
        If Segment is True, the result is composed with
        segments of the curve bounded by the SplitValues. If
        Segment is False, the result is composed with trimmed
        Curves all based on the same complete curve.
        """

    def GetCurves(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Geom.Geom_Curve]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ConvertCurve3dToBezier(ShapeUpgrade_SplitCurve3d):
    """converts/splits a 3d curve of any type to a list of beziers"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ConvertCurve3dToBezier) -> None: ...

    def SetLineMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Line to bezier."""

    def GetLineMode(self) -> bool:
        """Returns the Geom_Line conversion mode."""

    def SetCircleMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Circle to bezier."""

    def GetCircleMode(self) -> bool:
        """Returns the Geom_Circle conversion mode."""

    def SetConicMode(self, mode: bool) -> None:
        """Returns the Geom_Conic conversion mode."""

    def GetConicMode(self) -> bool:
        """Performs converting and computes the resulting shape."""

    def Compute(self) -> None:
        """
        Converts curve into a list of beziers, and stores the
        splitting parameters on original curve.
        """

    def Build(self, Segment: bool) -> None:
        """
        Splits a list of beziers computed by Compute method according
        the split values and splitting parameters.
        """

    def SplitParams(self) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        Returns the list of split parameters in original curve parametrisation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitSurface(nanoocp.Standard.Standard_Transient):
    """Splits a Surface with a criterion."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitSurface) -> None: ...

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """Initializes with single supporting surface."""

    @overload
    def Init(self, S: nanoocp.Geom.Geom_Surface | None, UFirst: float, ULast: float, VFirst: float, VLast: float, theArea: float = 0.0) -> None:
        """Initializes with single supporting surface with bounding parameters."""

    def SetUSplitValues(self, UValues: nanoocp.NCollection.NCollection_HSequence[float] | None) -> None:
        """Sets U parameters where splitting has to be done"""

    def SetVSplitValues(self, VValues: nanoocp.NCollection.NCollection_HSequence[float] | None) -> None:
        """Sets V parameters where splitting has to be done"""

    def Build(self, Segment: bool) -> None:
        """
        Performs splitting of the supporting surface.
        If resulting surface is B-Spline and Segment is True,
        the result is composed with segments of the surface bounded
        by the U and V SplitValues (method Geom_BSplineSurface::Segment
        is used).
        If Segment is False, the result is composed with
        Geom_RectangularTrimmedSurface all based on the same complete
        surface.
        Fields myNbResultingRow and myNbResultingCol must be set to
        specify the size of resulting grid of surfaces.
        """

    def Compute(self, Segment: bool = True) -> None:
        """Calculates points for correction/splitting of the surface."""

    def Perform(self, Segment: bool = True) -> None:
        """
        Performs correction/splitting of the surface.
        First defines splitting values by method Compute(), then calls method Build().
        """

    def USplitValues(self) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        returns all the U splitting values including the
        First and Last parameters of the input surface
        """

    def VSplitValues(self) -> nanoocp.NCollection.NCollection_HSequence[float]:
        """
        returns all the splitting V values including the
        First and Last parameters of the input surface
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Returns the status
        OK    - no splitting is needed
        DONE1 - splitting required and gives more than one patch
        DONE2 - splitting is required, but gives only single patch (initial)
        DONE3 - geometric form of the surface or parametrisation is modified
        """

    def ResSurfaces(self) -> nanoocp.ShapeExtend.ShapeExtend_CompositeSurface:
        """Returns obtained surfaces after splitting as CompositeSurface"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ConvertSurfaceToBezierBasis(ShapeUpgrade_SplitSurface):
    """
    Converts a plane, bspline surface, surface of revolution, surface
    of extrusion, offset surface to grid of bezier basis surface (
    bezier surface,
    surface of revolution based on bezier curve,
    offset surface based on any previous type).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ConvertSurfaceToBezierBasis) -> None: ...

    def Build(self, Segment: bool) -> None:
        """
        Splits a list of beziers computed by Compute method according
        the split values and splitting parameters.
        """

    def Compute(self, Segment: bool) -> None:
        """
        Converts surface into a grid of bezier based surfaces, and
        stores this grid.
        """

    def Segments(self) -> nanoocp.ShapeExtend.ShapeExtend_CompositeSurface:
        """
        Returns the grid of bezier based surfaces correspondent to
        original surface.
        """

    def SetPlaneMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Plane to Bezier"""

    def GetPlaneMode(self) -> bool:
        """Returns the Geom_Pline conversion mode."""

    def SetRevolutionMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_SurfaceOfRevolution to Bezier"""

    def GetRevolutionMode(self) -> bool:
        """Returns the Geom_SurfaceOfRevolution conversion mode."""

    def SetExtrusionMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier"""

    def GetExtrusionMode(self) -> bool:
        """Returns the Geom_SurfaceOfLinearExtrusion conversion mode."""

    def SetBSplineMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_BSplineSurface to Bezier"""

    def GetBSplineMode(self) -> bool:
        """Returns the Geom_BSplineSurface conversion mode."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_FaceDivideArea(ShapeUpgrade_FaceDivide):
    """Divides face by max area criterium."""

    @overload
    def __init__(self) -> None:
        """Creates empty constructor."""

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    @overload
    def __init__(self, theOther: ShapeUpgrade_FaceDivideArea) -> None: ...

    def Perform(self, theArea: float = 0.0) -> bool:
        """
        Performs splitting and computes the resulting shell
        The context is used to keep track of former splittings
        """

    def MaxArea(self) -> float:
        """Set max area allowed for faces"""

    def SetMaxArea(self, theValue: float) -> None:
        """Python addition: sets the value MaxArea() returns by reference in C++."""

    def NbParts(self) -> int:
        """Set number of parts expected"""

    def SetNbParts(self, theValue: int) -> None:
        """Python addition: sets the value NbParts() returns by reference in C++."""

    def SetNumbersUVSplits(self, theNbUsplits: int, theNbVsplits: int) -> None:
        """
        Set fixed numbers of splits in U and V directions.
        Only for "Splitting By Numbers" mode
        """

    def SetSplittingByNumber(self, theIsSplittingByNumber: bool) -> None:
        """
        Set splitting mode
        If the mode is "splitting by number",
        the face is splitted approximately into <myNbParts> parts,
        the parts are similar to squares in 2D.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_FixSmallCurves(ShapeUpgrade_Tool):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeUpgrade_FixSmallCurves) -> None: ...

    def Init(self, theEdge: nanoocp.TopoDS.TopoDS_Edge, theFace: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def Approx(self) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float, float]: ...

    def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d | None) -> None:
        """Sets the tool for splitting 3D curves."""

    def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d | None) -> None:
        """Sets the tool for splitting pcurves."""

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries the status of last call to Perform
        OK   :
        DONE1:
        DONE2:
        FAIL1:
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_FixSmallBezierCurves(ShapeUpgrade_FixSmallCurves):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: ShapeUpgrade_FixSmallBezierCurves) -> None: ...

    def Approx(self) -> tuple[bool, nanoocp.Geom.Geom_Curve, nanoocp.Geom2d.Geom2d_Curve, nanoocp.Geom2d.Geom2d_Curve, float, float]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_RemoveInternalWires(ShapeUpgrade_Tool):
    """Removes all internal wires having area less than specified min area"""

    @overload
    def __init__(self) -> None:
        """Creates empty constructor."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: ShapeUpgrade_RemoveInternalWires) -> None: ...

    def Init(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def Perform(self) -> bool:
        """
        Removes all internal wires having area less than area specified as minimal allowed area
        """

    @overload
    def Perform(self, theSeqShapes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        If specified sequence of shape contains -
        1.wires then these wires will be removed if they have area less than allowed min area.
        2.faces than internal wires from these faces will be removed if they have area less than
        allowed min area.
        """

    def GetResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Get result shape"""

    def MinArea(self) -> float:
        """
        Set min area allowed for holes( all holes having area less than mi area will be removed)
        """

    def SetMinArea(self, theValue: float) -> None:
        """Python addition: sets the value MinArea() returns by reference in C++."""

    def RemoveFaceMode(self) -> bool:
        """
        Set mode which manage removing faces which have outer wires consisting only from edges
        belonginig to removed internal wires.
        By default it is equal to true.
        """

    def SetRemoveFaceMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value RemoveFaceMode() returns by reference in C++.
        """

    def RemovedFaces(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns sequence of removed faces."""

    def RemovedWires(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns sequence of removed faces."""

    def Status(self, theStatus: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries status of last call to Perform()
        : OK - nothing was done
        :DONE1 - internal wires were removed
        :DONE2 - small faces were removed.
        :FAIL1 - initial shape is not specified
        :FAIL2 - specified sub-shape is not belonged to inotial shape.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_RemoveLocations(nanoocp.Standard.Standard_Transient):
    """Removes all locations sub-shapes of specified shape"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_RemoveLocations) -> None: ...

    def Remove(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Removes all location correspondingly to RemoveLevel."""

    def GetResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns shape with removed locations."""

    def SetRemoveLevel(self, theLevel: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """
        sets level starting with that location will be removed,
        by default TopAbs_SHAPE. In this case locations will be kept for specified shape
        and if specified shape is TopAbs_COMPOUND for sub-shapes of first level.
        """

    def RemoveLevel(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        sets level starting with that location will be removed.Value of level can be set to
        TopAbs_SHAPE,TopAbs_COMPOUND,TopAbs_SOLID,TopAbs_SHELL,TopAbs_FACE.By default TopAbs_SHAPE.
        In this case location will be removed for all shape types for exception of compound.
        """

    def ModifiedShape(self, theInitShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns modified shape obtained from initial shape."""

    def GetModifiedShapesMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Returns map of modified shapes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_ShapeDivide:
    """Divides a all faces in shell with given criteria Shell."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivide) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    def SetPrecision(self, Prec: float) -> None:
        """Defines the spatial precision used for splitting"""

    def SetMaxTolerance(self, maxtol: float) -> None:
        """Sets maximal allowed tolerance"""

    def SetMinTolerance(self, mintol: float) -> None:
        """Sets minimal allowed tolerance"""

    def SetSurfaceSegmentMode(self, Segment: bool) -> None:
        """
        Purpose sets mode for trimming (segment) surface by
        wire UV bounds.
        """

    def Perform(self, newContext: bool = True) -> bool:
        """
        Performs splitting and computes the resulting shape
        If newContext is True (default), the internal context
        will be cleared at start, else previous substitutions
        will be acting.
        """

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives the resulting Shape, or Null shape if not done."""

    def GetContext(self) -> nanoocp.ShapeBuild.ShapeBuild_ReShape:
        """
        Returns context with all the modifications made during
        last call(s) to Perform() recorded
        """

    def SetContext(self, context: nanoocp.ShapeBuild.ShapeBuild_ReShape | None) -> None:
        """
        Sets context with recorded modifications to be applied
        during next call(s) to Perform(shape,false)
        """

    def SetMsgRegistrator(self, msgreg: nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator | None) -> None:
        """Sets message registrator"""

    def MsgRegistrator(self) -> nanoocp.ShapeExtend.ShapeExtend_BasicMsgRegistrator:
        """Returns message registrator"""

    def SendMsg(self, shape: nanoocp.TopoDS.TopoDS_Shape, message: nanoocp.Message.Message_Msg, gravity: nanoocp.Message.Message_Gravity = Message_Gravity.Message_Info) -> None:
        """
        Sends a message to be attached to the shape.
        Calls corresponding message of message registrator.
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries the status of last call to Perform
        OK   : no splitting was done (or no call to Perform)
        DONE1: some edges were split
        DONE2: surface was split
        FAIL1: some errors occurred
        """

    def SetSplitFaceTool(self, splitFaceTool: ShapeUpgrade_FaceDivide | None) -> None:
        """Sets the tool for splitting faces."""

    def SetEdgeMode(self, aEdgeMode: int) -> None:
        """
        Sets mode for splitting 3d curves from edges.
        0 - only curve 3d from free edges.
        1 - only curve 3d from shared edges.
        2 -  all curve 3d.
        """

class ShapeUpgrade_ShapeConvertToBezier(ShapeUpgrade_ShapeDivide):
    """
    API class for performing conversion of 3D, 2D curves to bezier curves
    and surfaces to bezier based surfaces (
    bezier surface,
    surface of revolution based on bezier curve,
    offset surface based on any previous type).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeConvertToBezier) -> None: ...

    def Set2dConversion(self, mode: bool) -> None:
        """Sets mode for conversion 2D curves to bezier."""

    def Get2dConversion(self) -> bool:
        """Returns the 2D conversion mode."""

    def Set3dConversion(self, mode: bool) -> None:
        """Sets mode for conversion 3d curves to bezier."""

    def Get3dConversion(self) -> bool:
        """Returns the 3D conversion mode."""

    def SetSurfaceConversion(self, mode: bool) -> None:
        """
        Sets mode for conversion surfaces curves to
        bezier basis.
        """

    def GetSurfaceConversion(self) -> bool:
        """Returns the surface conversion mode."""

    def Set3dLineConversion(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Line to bezier."""

    def Get3dLineConversion(self) -> bool:
        """Returns the Geom_Line conversion mode."""

    def Set3dCircleConversion(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Circle to bezier."""

    def Get3dCircleConversion(self) -> bool:
        """Returns the Geom_Circle conversion mode."""

    def Set3dConicConversion(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Conic to bezier."""

    def Get3dConicConversion(self) -> bool:
        """Returns the Geom_Conic conversion mode."""

    def SetPlaneMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_Plane to Bezier"""

    def GetPlaneMode(self) -> bool:
        """Returns the Geom_Pline conversion mode."""

    def SetRevolutionMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_SurfaceOfRevolution to Bezier"""

    def GetRevolutionMode(self) -> bool:
        """Returns the Geom_SurfaceOfRevolution conversion mode."""

    def SetExtrusionMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_SurfaceOfLinearExtrusion to Bezier"""

    def GetExtrusionMode(self) -> bool:
        """Returns the Geom_SurfaceOfLinearExtrusion conversion mode."""

    def SetBSplineMode(self, mode: bool) -> None:
        """Sets mode for conversion Geom_BSplineSurface to Bezier"""

    def GetBSplineMode(self) -> bool:
        """Returns the Geom_BSplineSurface conversion mode."""

    def Perform(self, newContext: bool = True) -> bool:
        """Performs converting and computes the resulting shape"""

class ShapeUpgrade_ShapeDivideAngle(ShapeUpgrade_ShapeDivide):
    """
    Splits all surfaces of revolution, cylindrical, toroidal,
    conical, spherical surfaces in the given shape so that
    each resulting segment covers not more than defined number
    of degrees (to segments less than 90).
    """

    @overload
    def __init__(self, MaxAngle: float) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, MaxAngle: float, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivideAngle) -> None: ...

    def InitTool(self, MaxAngle: float) -> None:
        """Resets tool for splitting face with given angle"""

    def SetMaxAngle(self, MaxAngle: float) -> None:
        """Set maximal angle (calls InitTool)"""

    def MaxAngle(self) -> float:
        """Returns maximal angle"""

class ShapeUpgrade_ShapeDivideArea(ShapeUpgrade_ShapeDivide):
    """Divides faces from specified shape by max area criterium."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivideArea) -> None: ...

    def MaxArea(self) -> float:
        """Set max area allowed for faces"""

    def SetMaxArea(self, theValue: float) -> None:
        """Python addition: sets the value MaxArea() returns by reference in C++."""

    def NbParts(self) -> int:
        """
        Set number of parts expected
        for the case of splitting by number
        """

    def SetNbParts(self, theValue: int) -> None:
        """Python addition: sets the value NbParts() returns by reference in C++."""

    def SetNumbersUVSplits(self, theNbUsplits: int, theNbVsplits: int) -> None:
        """
        Set fixed numbers of splits in U and V directions.
        Only for "Splitting By Numbers" mode
        """

    def SetSplittingByNumber(self, theIsSplittingByNumber: bool) -> None:
        """
        Set splitting mode
        If the mode is "splitting by number",
        the face is splitted approximately into <myNbParts> parts,
        the parts are similar to squares in 2D.
        """

class ShapeUpgrade_ShapeDivideClosed(ShapeUpgrade_ShapeDivide):
    """
    Divides all closed faces in the shape. Class
    ShapeUpgrade_ClosedFaceDivide is used as divide tool.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialises tool with shape and default parameter."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivideClosed) -> None: ...

    def SetNbSplitPoints(self, num: int) -> None:
        """
        Sets the number of cuts applied to divide closed faces.
        The number of resulting faces will be num+1.
        """

class ShapeUpgrade_ShapeDivideClosedEdges(ShapeUpgrade_ShapeDivide):
    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialises tool with shape and default parameter."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivideClosedEdges) -> None: ...

    def SetNbSplitPoints(self, num: int) -> None:
        """
        Sets the number of cuts applied to divide closed edges.
        The number of resulting faces will be num+1.
        """

class ShapeUpgrade_ShapeDivideContinuity(ShapeUpgrade_ShapeDivide):
    """API Tool for converting shapes with C0 geometry into C1 ones"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Initialize by a Shape."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShapeDivideContinuity) -> None: ...

    def SetTolerance(self, Tol: float) -> None:
        """Sets tolerance."""

    def SetTolerance2d(self, Tol: float) -> None:
        """Sets tolerance."""

    def SetBoundaryCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Defines a criterion of continuity for the boundary (all the
        Wires)

        The possible values are C0, G1, C1, G2, C2, C3, CN The
        default is C1 to respect the Cas.Cade Shape Validity.
        G1 and G2 are not authorized.
        """

    def SetPCurveCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Defines a criterion of continuity for the boundary (all the
        pcurves of Wires)

        The possible values are C0, G1, C1, G2, C2, C3, CN The
        default is C1 to respect the Cas.Cade Shape Validity.
        G1 and G2 are not authorized.
        """

    def SetSurfaceCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape = GeomAbs_Shape.GeomAbs_C1) -> None:
        """
        Defines a criterion of continuity for the boundary (all the
        Wires)

        The possible values are C0, G1, C1, G2, C2, C3, CN The
        default is C1 to respect the Cas.Cade Shape Validity.
        G1 and G2 are not authorized.
        """

class ShapeUpgrade_ShellSewing:
    """
    This class provides a tool for applying sewing algorithm from
    BRepBuilderAPI: it takes a shape, calls sewing for each shell,
    and then replaces sewed shells with use of ShapeBuild_ReShape
    """

    @overload
    def __init__(self) -> None:
        """Creates a ShellSewing, empty"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_ShellSewing) -> None: ...

    def ApplySewing(self, shape: nanoocp.TopoDS.TopoDS_Shape, tol: float = 0.0) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Builds a new shape from a former one, by calling Sewing from
        BRepBuilderAPI. Rebuilt solids are oriented to be "not infinite"

        If <tol> is not given (i.e. value 0. by default), it is
        computed as the mean tolerance recorded in <shape>

        If no shell has been sewed, this method returns the input
        shape
        """

class ShapeUpgrade_SplitCurve2dContinuity(ShapeUpgrade_SplitCurve2d):
    """
    Corrects/splits a 2d curve with a continuity criterion.
    Tolerance is used to correct the curve at a knot that respects
    geometrically the criterion, in order to reduce the
    multiplicity of the knot.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitCurve2dContinuity) -> None: ...

    def SetCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets criterion for splitting."""

    def SetTolerance(self, Tol: float) -> None:
        """Sets tolerance."""

    def Compute(self) -> None:
        """Calculates points for correction/splitting of the curve"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitCurve3dContinuity(ShapeUpgrade_SplitCurve3d):
    """
    Corrects/splits a 2d curve with a continuity criterion.
    Tolerance is used to correct the curve at a knot that respects
    geometrically the criterion, in order to reduce the
    multiplicity of the knot.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitCurve3dContinuity) -> None: ...

    def SetCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets criterion for splitting."""

    def SetTolerance(self, Tol: float) -> None:
        """Sets tolerance."""

    def Compute(self) -> None:
        """Calculates points for correction/splitting of the curve"""

    def GetCurve(self) -> nanoocp.Geom.Geom_Curve: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitSurfaceAngle(ShapeUpgrade_SplitSurface):
    """
    Splits a surfaces of revolution, cylindrical, toroidal,
    conical, spherical so that each resulting segment covers
    not more than defined number of degrees.
    """

    @overload
    def __init__(self, MaxAngle: float) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitSurfaceAngle) -> None: ...

    def SetMaxAngle(self, MaxAngle: float) -> None:
        """Set maximal angle"""

    def MaxAngle(self) -> float:
        """Returns maximal angle"""

    def Compute(self, Segment: bool) -> None:
        """
        Performs splitting of the supporting surface(s).
        First defines splitting values, then calls inherited method.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitSurfaceArea(ShapeUpgrade_SplitSurface):
    """
    Split surface in the parametric space
    in according specified number of splits on the
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitSurfaceArea) -> None: ...

    def NbParts(self) -> int:
        """Set number of split for surfaces"""

    def SetNbParts(self, theValue: int) -> None:
        """Python addition: sets the value NbParts() returns by reference in C++."""

    def SetSplittingIntoSquares(self, theIsSplittingIntoSquares: bool) -> None:
        """
        Set splitting mode
        If the mode is "splitting into squares",
        the face is splitted approximately into <myNbParts> parts,
        the parts are similar to squares in 2D.
        """

    def SetNumbersUVSplits(self, theNbUsplits: int, theNbVsplits: int) -> None:
        """
        Set fixed numbers of splits in U and V directions.
        Only for "Splitting Into Squares" mode
        """

    def Compute(self, Segment: bool = True) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_SplitSurfaceContinuity(ShapeUpgrade_SplitSurface):
    """
    Splits a Surface with a continuity criterion.
    At the present moment C1 criterion is used only.
    This tool works with tolerance. If C0 surface can be corrected
    at a knot with given tolerance then the surface is corrected,
    otherwise it is spltted at that knot.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: ShapeUpgrade_SplitSurfaceContinuity) -> None: ...

    def SetCriterion(self, Criterion: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Sets criterion for splitting."""

    def SetTolerance(self, Tol: float) -> None:
        """Sets tolerance."""

    def Compute(self, Segment: bool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_UnifySameDomain(nanoocp.Standard.Standard_Transient):
    """
    This tool tries to unify faces and edges of the shape which lie on the same geometry.
    Faces/edges are considering as 'same-domain' if a group of neighbouring faces/edges
    are lying on coincident surfaces/curves.
    In this case these faces/edges can be unified into one face/edge.
    ShapeUpgrade_UnifySameDomain is initialized by a shape and the next optional parameters:
    UnifyFaces - tries to unify all possible faces
    UnifyEdges - tries to unify all possible edges
    ConcatBSplines - if this flag is set to true then all neighbouring edges, which lay
    on BSpline or Bezier curves with C1 continuity on their common vertices,
    will be merged into one common edge.

    The input shape can be of any type containing faces or edges - compsolid, solid, shell,
    wire, compound of any kind of shapes. The algorithm preserves the structure of compsolids,
    solids, shells and wires. E.g., if two shells have a common edge and the faces sharing
    this edge lie on the same surface the algorithm will not unify these faces, otherwise
    the structure of shells would be broken. However, if such faces belong to different
    compounds of faces they will be unified.

    The output result of the tool is the unified shape.

    All the modifications of initial shape are recorded during unifying.
    Methods History are intended to:
    - set a place holder for the history of modifications of sub-shapes of
    the initial shape;
    - get the collected history.
    The algorithm provides a place holder for the history and collects the
    history by default.
    To avoid collecting of the history the place holder should be set to null handle.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, UnifyEdges: bool = True, UnifyFaces: bool = True, ConcatBSplines: bool = False) -> None:
        """
        Constructor defining input shape and necessary flags.
        It does not perform unification.
        """

    @overload
    def __init__(self, theOther: ShapeUpgrade_UnifySameDomain) -> None: ...

    def Initialize(self, aShape: nanoocp.TopoDS.TopoDS_Shape, UnifyEdges: bool = True, UnifyFaces: bool = True, ConcatBSplines: bool = False) -> None:
        """
        Initializes with a shape and necessary flags.
        It does not perform unification.
        If you intend to nullify the History place holder do it after
        initialization.
        """

    def AllowInternalEdges(self, theValue: bool) -> None:
        """
        Sets the flag defining whether it is allowed to create
        internal edges inside merged faces in the case of non-manifold
        topology. Without this flag merging through multi connected edge
        is forbidden. Default value is false.
        """

    def KeepShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets the shape for avoid merging of the faces/edges.
        This shape can be vertex or edge.
        If the shape is a vertex it forbids merging of connected edges.
        If the shape is a edge it forbids merging of connected faces.
        This method can be called several times to keep several shapes.
        """

    def KeepShapes(self, theShapes: nanoocp.NCollection.NCollection_Map[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """
        Sets the map of shapes for avoid merging of the faces/edges.
        It allows passing a ready to use map instead of calling many times
        the method KeepShape.
        """

    def SetSafeInputMode(self, theValue: bool) -> None:
        """
        Sets the flag defining the behavior of the algorithm regarding
        modification of input shape.
        If this flag is equal to True then the input (original) shape can't be
        modified during modification process. Default value is true.
        """

    def SetLinearTolerance(self, theValue: float) -> None:
        """
        Sets the linear tolerance. It plays the role of chord error when
        taking decision about merging of shapes. Default value is Precision::Confusion().
        """

    def SetAngularTolerance(self, theValue: float) -> None:
        """
        Sets the angular tolerance. If two shapes form a connection angle greater than
        this value they will not be merged. Default value is Precision::Angular().
        """

    def Build(self) -> None:
        """Performs unification and builds the resulting shape."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Gives the resulting shape"""

    def History(self) -> nanoocp.BRepTools.BRepTools_History:
        """Returns the history of the processed shapes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class ShapeUpgrade_WireDivide(ShapeUpgrade_Tool):
    """
    Divides edges in the wire lying on the face or free wires or
    free edges with a criterion.
    Splits 3D curve and pcurve(s) of the edge on the face.
    Other pcurves which may be associated with the edge are simply
    copied.
    If 3D curve is split then pcurve on the face is split as
    well, and vice-versa.
    Input shape is not modified.
    The modifications made are recorded in external context
    (ShapeBuild_ReShape). This tool is applied to all edges
    before splitting them in order to keep sharing.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: ShapeUpgrade_WireDivide) -> None: ...

    @overload
    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Initializes by wire and face"""

    @overload
    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """Initializes by wire and surface"""

    @overload
    def Load(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None:
        """Loads working wire"""

    @overload
    def Load(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Creates wire of one edge and calls Load for wire"""

    def SetFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None:
        """Sets supporting surface by face"""

    @overload
    def SetSurface(self, S: nanoocp.Geom.Geom_Surface | None) -> None:
        """Sets supporting surface"""

    @overload
    def SetSurface(self, S: nanoocp.Geom.Geom_Surface | None, L: nanoocp.TopLoc.TopLoc_Location) -> None:
        """Sets supporting surface with location"""

    def Perform(self) -> None:
        """
        Computes the resulting wire by splitting all the edges
        according to splitting criteria.
        All the modifications made are recorded in context
        (ShapeBuild_ReShape). This tool is applied to all edges
        before splitting them in order to keep sharings.
        If no supporting face or surface is defined, only 3d
        splitting criteria are used.
        """

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """
        Gives the resulting Wire (equal to initial one if not done
        or Null if not loaded)
        """

    def Status(self, status: nanoocp.ShapeExtend.ShapeExtend_Status) -> bool:
        """
        Queries status of last call to Perform()
        OK - no edges were split, wire left untouched
        DONE1 - some edges were split
        FAIL1 - some edges have no 3d curve (skipped)
        FAIL2 - some edges have no pcurve (skipped)
        """

    def SetSplitCurve3dTool(self, splitCurve3dTool: ShapeUpgrade_SplitCurve3d | None) -> None:
        """Sets the tool for splitting 3D curves."""

    def SetSplitCurve2dTool(self, splitCurve2dTool: ShapeUpgrade_SplitCurve2d | None) -> None:
        """Sets the tool for splitting pcurves."""

    def SetTransferParamTool(self, TransferParam: nanoocp.ShapeAnalysis.ShapeAnalysis_TransferParameters | None) -> None:
        """Sets the tool for Transfer parameters between curves and pcurves."""

    def SetEdgeDivideTool(self, edgeDivideTool: ShapeUpgrade_EdgeDivide | None) -> None:
        """Sets tool for splitting edge"""

    def GetEdgeDivideTool(self) -> ShapeUpgrade_EdgeDivide:
        """returns tool for splitting edges"""

    def GetTransferParamTool(self) -> nanoocp.ShapeAnalysis.ShapeAnalysis_TransferParameters:
        """Returns the tool for Transfer of parameters."""

    def SetEdgeMode(self, EdgeMode: int) -> None:
        """
        Sets mode for splitting 3d curves from edges.
        0 - only curve 3d from free edges.
        1 - only curve 3d from shared edges.
        2 - all curve 3d.
        """

    def SetFixSmallCurveTool(self, FixSmallCurvesTool: ShapeUpgrade_FixSmallCurves | None) -> None:
        """Sets tool for fixing small curves with specified min tolerance;"""

    def GetFixSmallCurveTool(self) -> ShapeUpgrade_FixSmallCurves:
        """Returns tool for fixing small curves"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
