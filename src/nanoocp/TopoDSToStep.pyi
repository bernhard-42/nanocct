"""OCCT package TopoDSToStep (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.StepShape
import nanoocp.StepVisual
import nanoocp.TCollection
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.TopTools


class TopoDSToStep_BuilderError(enum.IntEnum):
    TopoDSToStep_BuilderDone = 0

    TopoDSToStep_NoFaceMapped = 1

    TopoDSToStep_BuilderOther = 2

TopoDSToStep_BuilderDone: TopoDSToStep_BuilderError = ...

TopoDSToStep_NoFaceMapped: TopoDSToStep_BuilderError = ...

TopoDSToStep_BuilderOther: TopoDSToStep_BuilderError = ...

class TopoDSToStep_MakeFaceError(enum.IntEnum):
    TopoDSToStep_FaceDone = 0

    TopoDSToStep_InfiniteFace = 1

    TopoDSToStep_NonManifoldFace = 2

    TopoDSToStep_NoWireMapped = 3

    TopoDSToStep_FaceOther = 4

TopoDSToStep_FaceDone: TopoDSToStep_MakeFaceError = TopoDSToStep_MakeFaceError.TopoDSToStep_FaceDone

TopoDSToStep_InfiniteFace: TopoDSToStep_MakeFaceError = ...

TopoDSToStep_NonManifoldFace: TopoDSToStep_MakeFaceError = ...

TopoDSToStep_NoWireMapped: TopoDSToStep_MakeFaceError = ...

TopoDSToStep_FaceOther: TopoDSToStep_MakeFaceError = TopoDSToStep_MakeFaceError.TopoDSToStep_FaceOther

class TopoDSToStep_MakeWireError(enum.IntEnum):
    TopoDSToStep_WireDone = 0

    TopoDSToStep_NonManifoldWire = 1

    TopoDSToStep_WireOther = 2

TopoDSToStep_WireDone: TopoDSToStep_MakeWireError = TopoDSToStep_MakeWireError.TopoDSToStep_WireDone

TopoDSToStep_NonManifoldWire: TopoDSToStep_MakeWireError = ...

TopoDSToStep_WireOther: TopoDSToStep_MakeWireError = TopoDSToStep_MakeWireError.TopoDSToStep_WireOther

class TopoDSToStep_MakeEdgeError(enum.IntEnum):
    TopoDSToStep_EdgeDone = 0

    TopoDSToStep_NonManifoldEdge = 1

    TopoDSToStep_EdgeOther = 2

TopoDSToStep_EdgeDone: TopoDSToStep_MakeEdgeError = TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeDone

TopoDSToStep_NonManifoldEdge: TopoDSToStep_MakeEdgeError = ...

TopoDSToStep_EdgeOther: TopoDSToStep_MakeEdgeError = TopoDSToStep_MakeEdgeError.TopoDSToStep_EdgeOther

class TopoDSToStep_MakeVertexError(enum.IntEnum):
    TopoDSToStep_VertexDone = 0

    TopoDSToStep_VertexOther = 1

TopoDSToStep_VertexDone: TopoDSToStep_MakeVertexError = ...

TopoDSToStep_VertexOther: TopoDSToStep_MakeVertexError = ...

class TopoDSToStep_FacetedError(enum.IntEnum):
    TopoDSToStep_FacetedDone = 0

    TopoDSToStep_SurfaceNotPlane = 1

    TopoDSToStep_PCurveNotLinear = 2

TopoDSToStep_FacetedDone: TopoDSToStep_FacetedError = ...

TopoDSToStep_SurfaceNotPlane: TopoDSToStep_FacetedError = ...

TopoDSToStep_PCurveNotLinear: TopoDSToStep_FacetedError = ...

class TopoDSToStep:
    """
    This package implements the mapping between CAS.CAD
    Shape representation and AP214 Shape Representation.
    The target schema is pms_c4 (a subset of AP214)

    How to use this Package :

    Entry point are context dependent. It can be :
    MakeManifoldSolidBrep
    MakeBrepWithVoids
    MakeFacetedBrep
    MakeFacetedBrepAndBrepWithVoids
    MakeShellBasedSurfaceModel
    Each of these classes call the Builder
    The class tool centralizes some common information.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep) -> None: ...

    @staticmethod
    def DecodeBuilderError(E: TopoDSToStep_BuilderError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeFaceError(E: TopoDSToStep_MakeFaceError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeWireError(E: TopoDSToStep_MakeWireError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeEdgeError(E: TopoDSToStep_MakeEdgeError) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def DecodeVertexError(E: TopoDSToStep_MakeVertexError) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns a new shape without undirect surfaces."""

    @overload
    @staticmethod
    def AddResult(FP: nanoocp.Transfer.Transfer_FinderProcess | None, Shape: nanoocp.TopoDS.TopoDS_Shape, entity: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an entity into the list of results (binders) for
        shape stored in FinderProcess
        """

    @overload
    @staticmethod
    def AddResult(FP: nanoocp.Transfer.Transfer_FinderProcess | None, Tool: TopoDSToStep_Tool) -> None:
        """
        Adds all entities recorded in Tool into the map of results
        (binders) stored in FinderProcess
        """

class TopoDSToStep_Root:
    """
    This class implements the common services for
    all classes of TopoDSToStep which report error.
    """

    def __init__(self, theOther: TopoDSToStep_Root) -> None: ...

    def Tolerance(self) -> float:
        """
        Returns (modifiable) the tolerance to be used for writing
        If not set, starts at 0.0001
        """

    def SetTolerance(self, theValue: float) -> None:
        """
        Python addition: sets the value Tolerance() returns by reference in C++.
        """

    def IsDone(self) -> bool: ...

class TopoDSToStep_Builder(TopoDSToStep_Root):
    """
    This builder Class provides services to build
    a ProSTEP Shape model from a Cas.Cad BRep.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theTessellatedGeomParam: int, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_Builder) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theTessellatedGeomParam: int, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def Error(self) -> TopoDSToStep_BuilderError: ...

    def Value(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_FacetedTool:
    """
    This Tool Class provides Information about Faceted Shapes
    to be mapped to STEP.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_FacetedTool) -> None: ...

    @staticmethod
    def CheckTopoDSShape(SH: nanoocp.TopoDS.TopoDS_Shape) -> TopoDSToStep_FacetedError: ...

class TopoDSToStep_MakeBrepWithVoids(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Solid from TopoDS and BrepWithVoids from
    StepShape. All the topology and geometry comprised
    into the shell or the solid are taken into account and
    translated.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Solid, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeBrepWithVoids) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_BrepWithVoids: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_MakeFacetedBrep(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Shell or Solid from TopoDS and FacetedBrep from
    StepShape. All the topology and geometry comprised
    into the shell or the solid are taken into account and
    translated.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Solid, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeFacetedBrep) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_FacetedBrep: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_MakeFacetedBrepAndBrepWithVoids(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Solid from TopoDS and FacetedBrepAndBrepWithVoids from
    StepShape. All the topology and geometry comprised
    into the shell or the solid are taken into account and
    translated.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Solid, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeFacetedBrepAndBrepWithVoids) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_FacetedBrepAndBrepWithVoids: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_MakeGeometricCurveSet(TopoDSToStep_Root):
    """
    This class implements the mapping between a Shape
    from TopoDS and a GeometricCurveSet from StepShape in order
    to create a GeometricallyBoundedWireframeRepresentation.
    """

    @overload
    def __init__(self, SH: nanoocp.TopoDS.TopoDS_Shape, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeGeometricCurveSet) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_GeometricCurveSet: ...

class TopoDSToStep_MakeManifoldSolidBrep(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Shell or Solid from TopoDS and ManifoldSolidBrep from
    StepShape. All the topology and geometry comprised
    into the shell or the solid are taken into account and
    translated.
    """

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Solid, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeManifoldSolidBrep) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_ManifoldSolidBrep: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_MakeShellBasedSurfaceModel(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Face, Shell or Solid from TopoDS and ShellBasedSurfaceModel
    from StepShape. All the topology and geometry comprised
    into the shape are taken into account and translated.
    """

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shell, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Solid, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeShellBasedSurfaceModel) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_ShellBasedSurfaceModel: ...

    def TessellatedValue(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...

class TopoDSToStep_MakeStepEdge(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Edge from TopoDS and TopologicalRepresentationItem from
    StepShape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, E: nanoocp.TopoDS.TopoDS_Edge, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeStepEdge) -> None: ...

    def Init(self, E: nanoocp.TopoDS.TopoDS_Edge, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def Error(self) -> TopoDSToStep_MakeEdgeError: ...

class TopoDSToStep_MakeStepFace(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Face from TopoDS and TopologicalRepresentationItem from
    StepShape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, F: nanoocp.TopoDS.TopoDS_Face, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeStepFace) -> None: ...

    def Init(self, F: nanoocp.TopoDS.TopoDS_Face, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def Error(self) -> TopoDSToStep_MakeFaceError: ...

class TopoDSToStep_MakeStepVertex(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Vertex from TopoDS and TopologicalRepresentationItem from
    StepShape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, V: nanoocp.TopoDS.TopoDS_Vertex, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeStepVertex) -> None: ...

    def Init(self, V: nanoocp.TopoDS.TopoDS_Vertex, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def Error(self) -> TopoDSToStep_MakeVertexError: ...

class TopoDSToStep_MakeStepWire(TopoDSToStep_Root):
    """
    This class implements the mapping between classes
    Wire from TopoDS and TopologicalRepresentationItem from
    StepShape.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, W: nanoocp.TopoDS.TopoDS_Wire, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeStepWire) -> None: ...

    def Init(self, W: nanoocp.TopoDS.TopoDS_Wire, T: TopoDSToStep_Tool, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Value(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def Error(self) -> TopoDSToStep_MakeWireError: ...

class TopoDSToStep_Tool:
    """
    This Tool Class provides Information to build
    a ProSTEP Shape model from a Cas.Cad BRep.
    """

    @overload
    def __init__(self, theModel: nanoocp.StepData.StepData_StepModel | None) -> None: ...

    @overload
    def __init__(self, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher], FacetedContext: bool, theSurfCurveMode: int) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_Tool) -> None: ...

    def Init(self, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher], FacetedContext: bool, theSurfCurveMode: int) -> None: ...

    def IsBound(self, S: nanoocp.TopoDS.TopoDS_Shape) -> bool: ...

    def Bind(self, S: nanoocp.TopoDS.TopoDS_Shape, T: nanoocp.StepShape.StepShape_TopologicalRepresentationItem | None) -> None: ...

    def Find(self, S: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem: ...

    def Faceted(self) -> bool: ...

    def SetCurrentShell(self, S: nanoocp.TopoDS.TopoDS_Shell) -> None: ...

    def CurrentShell(self) -> nanoocp.TopoDS.TopoDS_Shell: ...

    def SetCurrentFace(self, F: nanoocp.TopoDS.TopoDS_Face) -> None: ...

    def CurrentFace(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def SetCurrentWire(self, W: nanoocp.TopoDS.TopoDS_Wire) -> None: ...

    def CurrentWire(self) -> nanoocp.TopoDS.TopoDS_Wire: ...

    def SetCurrentEdge(self, E: nanoocp.TopoDS.TopoDS_Edge) -> None: ...

    def CurrentEdge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def SetCurrentVertex(self, V: nanoocp.TopoDS.TopoDS_Vertex) -> None: ...

    def CurrentVertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Lowest3DTolerance(self) -> float: ...

    def SetSurfaceReversed(self, B: bool) -> None: ...

    def SurfaceReversed(self) -> bool: ...

    def Map(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def PCurveMode(self) -> int:
        """
        Returns mode for writing pcurves
        (initialized by parameter write.surfacecurve.mode)
        """

class TopoDSToStep_WireframeBuilder(TopoDSToStep_Root):
    """
    This builder Class provides services to build
    a ProSTEP Wireframemodel from a Cas.Cad BRep.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, S: nanoocp.TopoDS.TopoDS_Shape, T: TopoDSToStep_Tool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_WireframeBuilder) -> None: ...

    def Init(self, S: nanoocp.TopoDS.TopoDS_Shape, T: TopoDSToStep_Tool, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> None: ...

    def Error(self) -> TopoDSToStep_BuilderError: ...

    def Value(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]: ...

    def GetTrimmedCurveFromEdge(self, E: nanoocp.TopoDS.TopoDS_Edge, F: nanoocp.TopoDS.TopoDS_Face, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher], theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]]:
        """
        Extraction of Trimmed Curves from TopoDS_Edge for the
        Creation of a GeometricallyBoundedWireframeRepresentation
        """

    def GetTrimmedCurveFromFace(self, F: nanoocp.TopoDS.TopoDS_Face, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher], theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]]:
        """
        Extraction of Trimmed Curves from TopoDS_Face for the
        Creation of a GeometricallyBoundedWireframeRepresentation
        """

    def GetTrimmedCurveFromShape(self, S: nanoocp.TopoDS.TopoDS_Shape, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher], theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]]:
        """
        Extraction of Trimmed Curves from any TopoDS_Shape for the
        Creation of a GeometricallyBoundedWireframeRepresentation
        """

class TopoDSToStep_MakeTessellatedItem(TopoDSToStep_Root):
    """
    This class implements the mapping between
    Face, Shell fromTopoDS and TriangulatedFace from StepVisual.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theShell: nanoocp.TopoDS.TopoDS_Shell, theTool: TopoDSToStep_Tool, theFP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theFace: nanoocp.TopoDS.TopoDS_Face, theTool: TopoDSToStep_Tool, theFP: nanoocp.Transfer.Transfer_FinderProcess | None, theToPreferSurfaceSet: bool, theLocalFactors: nanoocp.StepData.StepData_Factors, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def __init__(self, theOther: TopoDSToStep_MakeTessellatedItem) -> None: ...

    @overload
    def Init(self, theFace: nanoocp.TopoDS.TopoDS_Face, theTool: TopoDSToStep_Tool, theFP: nanoocp.Transfer.Transfer_FinderProcess | None, theToPreferSurfaceSet: bool, theLocalFactors: nanoocp.StepData.StepData_Factors, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    @overload
    def Init(self, theShell: nanoocp.TopoDS.TopoDS_Shell, theTool: TopoDSToStep_Tool, theFP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None: ...

    def Value(self) -> nanoocp.StepVisual.StepVisual_TessellatedItem: ...
