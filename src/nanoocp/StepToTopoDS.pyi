"""OCCT package StepToTopoDS (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.Geom
import nanoocp.Geom2d
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.StepVisual
import nanoocp.TCollection
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.gp


class StepToTopoDS_BuilderError(enum.IntEnum):
    StepToTopoDS_BuilderDone = 0

    StepToTopoDS_BuilderOther = 1

StepToTopoDS_BuilderDone: StepToTopoDS_BuilderError = ...

StepToTopoDS_BuilderOther: StepToTopoDS_BuilderError = ...

class StepToTopoDS_TranslateShellError(enum.IntEnum):
    StepToTopoDS_TranslateShellDone = 0

    StepToTopoDS_TranslateShellOther = 1

StepToTopoDS_TranslateShellDone: StepToTopoDS_TranslateShellError = ...

StepToTopoDS_TranslateShellOther: StepToTopoDS_TranslateShellError = ...

class StepToTopoDS_TranslateFaceError(enum.IntEnum):
    StepToTopoDS_TranslateFaceDone = 0

    StepToTopoDS_TranslateFaceOther = 1

StepToTopoDS_TranslateFaceDone: StepToTopoDS_TranslateFaceError = ...

StepToTopoDS_TranslateFaceOther: StepToTopoDS_TranslateFaceError = ...

class StepToTopoDS_TranslateEdgeError(enum.IntEnum):
    StepToTopoDS_TranslateEdgeDone = 0

    StepToTopoDS_TranslateEdgeOther = 1

StepToTopoDS_TranslateEdgeDone: StepToTopoDS_TranslateEdgeError = ...

StepToTopoDS_TranslateEdgeOther: StepToTopoDS_TranslateEdgeError = ...

class StepToTopoDS_TranslateVertexError(enum.IntEnum):
    StepToTopoDS_TranslateVertexDone = 0

    StepToTopoDS_TranslateVertexOther = 1

StepToTopoDS_TranslateVertexDone: StepToTopoDS_TranslateVertexError = ...

StepToTopoDS_TranslateVertexOther: StepToTopoDS_TranslateVertexError = ...

class StepToTopoDS_TranslateVertexLoopError(enum.IntEnum):
    StepToTopoDS_TranslateVertexLoopDone = 0

    StepToTopoDS_TranslateVertexLoopOther = 1

StepToTopoDS_TranslateVertexLoopDone: StepToTopoDS_TranslateVertexLoopError = ...

StepToTopoDS_TranslateVertexLoopOther: StepToTopoDS_TranslateVertexLoopError = ...

class StepToTopoDS_TranslatePolyLoopError(enum.IntEnum):
    StepToTopoDS_TranslatePolyLoopDone = 0

    StepToTopoDS_TranslatePolyLoopOther = 1

StepToTopoDS_TranslatePolyLoopDone: StepToTopoDS_TranslatePolyLoopError = ...

StepToTopoDS_TranslatePolyLoopOther: StepToTopoDS_TranslatePolyLoopError = ...

class StepToTopoDS_GeometricToolError(enum.IntEnum):
    StepToTopoDS_GeometricToolDone = 0

    StepToTopoDS_GeometricToolIsDegenerated = 1

    StepToTopoDS_GeometricToolHasNoPCurve = 2

    StepToTopoDS_GeometricToolWrong3dParameters = 3

    StepToTopoDS_GeometricToolNoProjectiOnCurve = 4

    StepToTopoDS_GeometricToolOther = 5

StepToTopoDS_GeometricToolDone: StepToTopoDS_GeometricToolError = ...

StepToTopoDS_GeometricToolIsDegenerated: StepToTopoDS_GeometricToolError = ...

StepToTopoDS_GeometricToolHasNoPCurve: StepToTopoDS_GeometricToolError = ...

StepToTopoDS_GeometricToolWrong3dParameters: StepToTopoDS_GeometricToolError = ...

StepToTopoDS_GeometricToolNoProjectiOnCurve: StepToTopoDS_GeometricToolError = ...

StepToTopoDS_GeometricToolOther: StepToTopoDS_GeometricToolError = ...

class StepToTopoDS_TranslateEdgeLoopError(enum.IntEnum):
    StepToTopoDS_TranslateEdgeLoopDone = 0

    StepToTopoDS_TranslateEdgeLoopOther = 1

StepToTopoDS_TranslateEdgeLoopDone: StepToTopoDS_TranslateEdgeLoopError = ...

StepToTopoDS_TranslateEdgeLoopOther: StepToTopoDS_TranslateEdgeLoopError = ...

class StepToTopoDS_TranslateSolidError(enum.IntEnum):
    StepToTopoDS_TranslateSolidDone = 0

    StepToTopoDS_TranslateSolidOther = 1

StepToTopoDS_TranslateSolidDone: StepToTopoDS_TranslateSolidError = ...

StepToTopoDS_TranslateSolidOther: StepToTopoDS_TranslateSolidError = ...

class StepToTopoDS:
    """
    This package implements the mapping between AP214
    Shape representation and CAS.CAD Shape Representation.
    The source schema is Part42 (which is included in AP214)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS) -> None: ...

    @staticmethod
    def DecodeBuilderError(Error: StepToTopoDS_BuilderError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeShellError(Error: StepToTopoDS_TranslateShellError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeFaceError(Error: StepToTopoDS_TranslateFaceError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeEdgeError(Error: StepToTopoDS_TranslateEdgeError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeVertexError(Error: StepToTopoDS_TranslateVertexError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeVertexLoopError(Error: StepToTopoDS_TranslateVertexLoopError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodePolyLoopError(Error: StepToTopoDS_TranslatePolyLoopError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeGeometricToolError(Error: StepToTopoDS_GeometricToolError) -> str: ...

class StepToTopoDS_Root:
    """
    This class implements the common services for
    all classes of StepToTopoDS which report error
    and sets and returns precision.
    """

    def __init__(self, theOther: StepToTopoDS_Root) -> None: ...

    def IsDone(self) -> bool: ...

    def Precision(self) -> float:
        """Returns the value of "MyPrecision\""""

    def SetPrecision(self, preci: float) -> None:
        """Sets the value of "MyPrecision\""""

    def MaxTol(self) -> float:
        """Returns the value of "MaxTol\""""

    def SetMaxTol(self, maxpreci: float) -> None:
        """Sets the value of MaxTol"""

class StepToTopoDS_Builder(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_Builder) -> None: ...

    @overload
    def Init(self, theManifoldSolid: nanoocp.StepShape.StepShape_ManifoldSolidBrep | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theBRepWithVoids: nanoocp.StepShape.StepShape_BrepWithVoids | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theFB: nanoocp.StepShape.StepShape_FacetedBrep | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theFBABWV: nanoocp.StepShape.StepShape_FacetedBrepAndBrepWithVoids | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, S: nanoocp.StepShape.StepShape_ShellBasedSurfaceModel | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, S: nanoocp.StepShape.StepShape_EdgeBasedWireframeModel | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def Init(self, S: nanoocp.StepShape.StepShape_FaceBasedSurfaceModel | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def Init(self, S: nanoocp.StepShape.StepShape_GeometricSet | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., RA: nanoocp.Transfer.Transfer_ActorOfTransientProcess | None = None, isManifold: bool = False, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theTSo: nanoocp.StepVisual.StepVisual_TessellatedSolid | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Init(self, theTSh: nanoocp.StepVisual.StepVisual_TessellatedShell | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Init(self, theTF: nanoocp.StepVisual.StepVisual_TessellatedFace | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool: ...

    @overload
    def Init(self, theTSS: nanoocp.StepVisual.StepVisual_TessellatedSurfaceSet | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_BuilderError: ...

class StepToTopoDS_GeometricTool:
    """
    This class contains some algorithmic services
    specific to the mapping STEP to CAS.CADE
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_GeometricTool) -> None: ...

    @staticmethod
    def PCurve(SC: nanoocp.StepGeom.StepGeom_SurfaceCurve | None, S: nanoocp.StepGeom.StepGeom_Surface | None, last: int = 0) -> tuple[int, nanoocp.StepGeom.StepGeom_Pcurve]: ...

    @staticmethod
    def IsSeamCurve(SC: nanoocp.StepGeom.StepGeom_SurfaceCurve | None, S: nanoocp.StepGeom.StepGeom_Surface | None, E: nanoocp.StepShape.StepShape_Edge | None, EL: nanoocp.StepShape.StepShape_EdgeLoop | None) -> bool: ...

    @staticmethod
    def IsLikeSeam(SC: nanoocp.StepGeom.StepGeom_SurfaceCurve | None, S: nanoocp.StepGeom.StepGeom_Surface | None, E: nanoocp.StepShape.StepShape_Edge | None, EL: nanoocp.StepShape.StepShape_EdgeLoop | None) -> bool: ...

    @staticmethod
    def UpdateParam3d(C: nanoocp.Geom.Geom_Curve | None, preci: float) -> tuple[bool, float, float]: ...

class StepToTopoDS_MakeTransformed(StepToTopoDS_Root):
    """Produces instances by Transformation of a basic item"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_MakeTransformed) -> None: ...

    @overload
    def Compute(self, Origin: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, Target: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """
        Computes a transformation to pass from an Origin placement to
        a Target placement. Returns True when done
        If not done, the transformation will by Identity
        """

    @overload
    def Compute(self, Operator: nanoocp.StepGeom.StepGeom_CartesianTransformationOperator3d | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """Computes a transformation defined by an operator 3D"""

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """
        Returns the computed transformation (Identity if not yet or
        if failed)
        """

    def Transform(self, shape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Applies the computed transformation to a shape
        Returns False if the transformation is Identity
        """

    def TranslateMappedItem(self, mapit: nanoocp.StepRepr.StepRepr_MappedItem | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Translates a MappedItem. More precisely
        A MappedItem has a MappingSource and a MappingTarget
        MappingSource has a MappedRepresentation and a MappingOrigin
        MappedRepresentation is the basic item to be instanced
        MappingOrigin is the starting placement
        MappingTarget is the final placement

        Hence, the transformation from MappingOrigin and MappingTarget
        is computed, the MappedRepr. is converted to a Shape, then
        transformed as an instance of this Shape
        """

class StepToTopoDS_NMTool:
    """
    Provides data to process non-manifold topology when
    reading from STEP.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, MapOfRI: nanoocp.NCollection.NCollection_DataMap[nanoocp.StepRepr.StepRepr_RepresentationItem, nanoocp.TopoDS.TopoDS_Shape], MapOfRINames: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_NMTool) -> None: ...

    def Init(self, MapOfRI: nanoocp.NCollection.NCollection_DataMap[nanoocp.StepRepr.StepRepr_RepresentationItem, nanoocp.TopoDS.TopoDS_Shape], MapOfRINames: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TopoDS.TopoDS_Shape]) -> None: ...

    def SetActive(self, isActive: bool) -> None: ...

    def IsActive(self) -> bool: ...

    def CleanUp(self) -> None: ...

    @overload
    def IsBound(self, RI: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> bool: ...

    @overload
    def IsBound(self, RIName: nanoocp.TCollection.TCollection_AsciiString) -> bool: ...

    @overload
    def Bind(self, RI: nanoocp.StepRepr.StepRepr_RepresentationItem | None, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Bind(self, RIName: nanoocp.TCollection.TCollection_AsciiString, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def Find(self, RI: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Find(self, RIName: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def RegisterNMEdge(self, Edge: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def IsSuspectedAsClosing(self, BaseShell: nanoocp.TopoDS.TopoDS_Shape, SuspectedShell: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def IsPureNMShell(self, Shell: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def SetIDEASCase(self, IDEASCase: bool) -> None: ...

    def IsIDEASCase(self) -> bool: ...

class StepToTopoDS_PointPair:
    """Stores a pair of Points from step"""

    @overload
    def __init__(self, P1: nanoocp.StepGeom.StepGeom_CartesianPoint | None, P2: nanoocp.StepGeom.StepGeom_CartesianPoint | None) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_PointPair) -> None: ...

    def GetPoint1(self) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

    def GetPoint2(self) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

    def __eq__(self, thePointPair: StepToTopoDS_PointPair) -> bool: ...

    def __hash__(self) -> int: ...

class StepToTopoDS_Tool:
    """
    This Tool Class provides Information to build
    a Cas.Cad BRep from a ProSTEP Shape model.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, Map: nanoocp.NCollection.NCollection_DataMap[nanoocp.StepShape.StepShape_TopologicalRepresentationItem, nanoocp.TopoDS.TopoDS_Shape], TP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_Tool) -> None: ...

    def Init(self, Map: nanoocp.NCollection.NCollection_DataMap[nanoocp.StepShape.StepShape_TopologicalRepresentationItem, nanoocp.TopoDS.TopoDS_Shape], TP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None: ...

    def IsBound(self, TRI: nanoocp.StepShape.StepShape_TopologicalRepresentationItem | None) -> bool: ...

    def Bind(self, TRI: nanoocp.StepShape.StepShape_TopologicalRepresentationItem | None, S: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def Find(self, TRI: nanoocp.StepShape.StepShape_TopologicalRepresentationItem | None) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ClearEdgeMap(self) -> None: ...

    def IsEdgeBound(self, PP: StepToTopoDS_PointPair) -> bool: ...

    def BindEdge(self, PP: StepToTopoDS_PointPair, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def FindEdge(self, PP: StepToTopoDS_PointPair) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def ClearVertexMap(self) -> None: ...

    def IsVertexBound(self, PG: nanoocp.StepGeom.StepGeom_CartesianPoint | None) -> bool: ...

    def BindVertex(self, P: nanoocp.StepGeom.StepGeom_CartesianPoint | None, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def FindVertex(self, P: nanoocp.StepGeom.StepGeom_CartesianPoint | None) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    @overload
    def ComputePCurve(self, B: bool) -> None: ...

    @overload
    def ComputePCurve(self) -> bool: ...

    def TransientProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess: ...

    @overload
    def AddContinuity(self, GeomSurf: nanoocp.Geom.Geom_Surface | None) -> None: ...

    @overload
    def AddContinuity(self, GeomCurve: nanoocp.Geom.Geom_Curve | None) -> None: ...

    @overload
    def AddContinuity(self, GeomCur2d: nanoocp.Geom2d.Geom2d_Curve | None) -> None: ...

    def C0Surf(self) -> int: ...

    def C1Surf(self) -> int: ...

    def C2Surf(self) -> int: ...

    def C0Cur2(self) -> int: ...

    def C1Cur2(self) -> int: ...

    def C2Cur2(self) -> int: ...

    def C0Cur3(self) -> int: ...

    def C1Cur3(self) -> int: ...

    def C2Cur3(self) -> int: ...

class StepToTopoDS_TranslateCompositeCurve(StepToTopoDS_Root):
    """
    Translate STEP entity composite_curve to TopoDS_Wire
    If surface is given, the curve is assumed to lie on that
    surface and in case if any segment of it is a
    curve_on_surface, the pcurve for that segment will be taken.
    Note: a segment of composite_curve may be itself
    composite_curve. Only one-level protection against
    cyclic references is implemented.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, CC: nanoocp.StepGeom.StepGeom_CompositeCurve | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """Translates standalone composite_curve"""

    @overload
    def __init__(self, CC: nanoocp.StepGeom.StepGeom_CompositeCurve | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, S: nanoocp.StepGeom.StepGeom_Surface | None, Surf: nanoocp.Geom.Geom_Surface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """Translates composite_curve lying on surface"""

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateCompositeCurve) -> None: ...

    @overload
    def Init(self, CC: nanoocp.StepGeom.StepGeom_CompositeCurve | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """Translates standalone composite_curve"""

    @overload
    def Init(self, CC: nanoocp.StepGeom.StepGeom_CompositeCurve | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, S: nanoocp.StepGeom.StepGeom_Surface | None, Surf: nanoocp.Geom.Geom_Surface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """Translates composite_curve lying on surface"""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Wire:
        """Returns result of last translation or null wire if failed."""

    def IsInfiniteSegment(self) -> bool:
        """
        Returns True if composite_curve contains a segment with infinite parameters.
        """

class StepToTopoDS_TranslateCurveBoundedSurface(StepToTopoDS_Root):
    """Translate curve_bounded_surface into TopoDS_Face"""

    @overload
    def __init__(self) -> None:
        """Create empty tool"""

    @overload
    def __init__(self, CBS: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """Translate surface"""

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateCurveBoundedSurface) -> None: ...

    def Init(self, CBS: nanoocp.StepGeom.StepGeom_CurveBoundedSurface | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """Translate surface"""

    def Value(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Returns result of last translation or null wire if failed."""

class StepToTopoDS_TranslateEdge(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, E: nanoocp.StepShape.StepShape_Edge | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateEdge) -> None: ...

    def Init(self, E: nanoocp.StepShape.StepShape_Edge | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def MakeFromCurve3D(self, C3D: nanoocp.StepGeom.StepGeom_Curve | None, EC: nanoocp.StepShape.StepShape_EdgeCurve | None, Vend: nanoocp.StepShape.StepShape_Vertex | None, preci: float, E: nanoocp.TopoDS.TopoDS_Edge, V1: nanoocp.TopoDS.TopoDS_Vertex, V2: nanoocp.TopoDS.TopoDS_Vertex, T: StepToTopoDS_Tool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None:
        """
        Warning! C3D is assumed to be a Curve 3D ...
        other cases to checked before calling this
        """

    def MakePCurve(self, PCU: nanoocp.StepGeom.StepGeom_Pcurve | None, ConvSurf: nanoocp.Geom.Geom_Surface | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> nanoocp.Geom2d.Geom2d_Curve: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateEdgeError: ...

class StepToTopoDS_TranslateEdgeLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, FB: nanoocp.StepShape.StepShape_FaceBound | None, F: nanoocp.TopoDS.TopoDS_Face, S: nanoocp.Geom.Geom_Surface | None, SS: nanoocp.StepGeom.StepGeom_Surface | None, ss: bool, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateEdgeLoop) -> None: ...

    def Init(self, FB: nanoocp.StepShape.StepShape_FaceBound | None, F: nanoocp.TopoDS.TopoDS_Face, S: nanoocp.Geom.Geom_Surface | None, SS: nanoocp.StepGeom.StepGeom_Surface | None, ss: bool, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateEdgeLoopError: ...

class StepToTopoDS_TranslateFace(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, FS: nanoocp.StepShape.StepShape_FaceSurface | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theTSS: nanoocp.StepVisual.StepVisual_TessellatedSurfaceSet | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theTF: nanoocp.StepVisual.StepVisual_TessellatedFace | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theHasGeom: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateFace) -> None: ...

    @overload
    def Init(self, theFaceSurface: nanoocp.StepShape.StepShape_FaceSurface | None, theTopoDSTool: StepToTopoDS_Tool, theTopoDSToolNM: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def Init(self, theTF: nanoocp.StepVisual.StepVisual_TessellatedFace | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool: ...

    @overload
    def Init(self, theTSS: nanoocp.StepVisual.StepVisual_TessellatedSurfaceSet | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateFaceError: ...

class StepToTopoDS_TranslatePolyLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, PL: nanoocp.StepShape.StepShape_PolyLoop | None, T: StepToTopoDS_Tool, S: nanoocp.Geom.Geom_Surface | None, F: nanoocp.TopoDS.TopoDS_Face, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslatePolyLoop) -> None: ...

    def Init(self, PL: nanoocp.StepShape.StepShape_PolyLoop | None, T: StepToTopoDS_Tool, S: nanoocp.Geom.Geom_Surface | None, F: nanoocp.TopoDS.TopoDS_Face, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslatePolyLoopError: ...

class StepToTopoDS_TranslateShell(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateShell) -> None: ...

    @overload
    def Init(self, CFS: nanoocp.StepShape.StepShape_ConnectedFaceSet | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theTSh: nanoocp.StepVisual.StepVisual_TessellatedShell | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateShellError: ...

class StepToTopoDS_TranslateSolid(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateSolid) -> None: ...

    def Init(self, theTSo: nanoocp.StepVisual.StepVisual_TessellatedSolid | None, theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theTool: StepToTopoDS_Tool, theNMTool: StepToTopoDS_NMTool, theReadTessellatedWhenNoBRepOnly: bool, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateSolidError: ...

class StepToTopoDS_TranslateVertex(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, V: nanoocp.StepShape.StepShape_Vertex | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateVertex) -> None: ...

    def Init(self, V: nanoocp.StepShape.StepShape_Vertex | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateVertexError: ...

class StepToTopoDS_TranslateVertexLoop(StepToTopoDS_Root):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, VL: nanoocp.StepShape.StepShape_VertexLoop | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: StepToTopoDS_TranslateVertexLoop) -> None: ...

    def Init(self, VL: nanoocp.StepShape.StepShape_VertexLoop | None, T: StepToTopoDS_Tool, NMTool: StepToTopoDS_NMTool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def Error(self) -> StepToTopoDS_TranslateVertexLoopError: ...
