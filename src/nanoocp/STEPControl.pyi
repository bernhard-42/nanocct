"""OCCT package STEPControl (toolkit TKDESTEP)"""

import enum
from typing import TextIO, overload

import nanoocp.DE
import nanoocp.DESTEP
import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.XSControl
import nanoocp.gp
import nanoocp.TCollection


class STEPControl_StepModelType(enum.IntEnum):
    """
    Gives you the choice of translation mode for an Open
    CASCADE shape that is being translated to STEP.
    - STEPControl_AsIs translates an Open CASCADE shape to its
    highest possible STEP representation.
    - STEPControl_ManifoldSolidBrep translates an Open CASCADE shape
    to a STEP manifold_solid_brep or brep_with_voids entity.
    - STEPControl_FacetedBrep translates an Open CASCADE shape
    into a STEP faceted_brep entity.
    -  STEPControl_ShellBasedSurfaceModel translates an Open CASCADE shape
    into a STEP shell_based_surface_model entity.
    - STEPControl_GeometricCurveSet
    translates an Open CASCADE shape into a STEP geometric_curve_set entity.
    """

    STEPControl_AsIs = 0

    STEPControl_ManifoldSolidBrep = 1

    STEPControl_BrepWithVoids = 2

    STEPControl_FacetedBrep = 3

    STEPControl_FacetedBrepAndBrepWithVoids = 4

    STEPControl_ShellBasedSurfaceModel = 5

    STEPControl_GeometricCurveSet = 6

    STEPControl_Hybrid = 7

STEPControl_AsIs: STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs

STEPControl_ManifoldSolidBrep: STEPControl_StepModelType = ...

STEPControl_BrepWithVoids: STEPControl_StepModelType = ...

STEPControl_FacetedBrep: STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_FacetedBrep

STEPControl_FacetedBrepAndBrepWithVoids: STEPControl_StepModelType = ...

STEPControl_ShellBasedSurfaceModel: STEPControl_StepModelType = ...

STEPControl_GeometricCurveSet: STEPControl_StepModelType = ...

STEPControl_Hybrid: STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_Hybrid

class STEPControl_ActorRead(nanoocp.Transfer.Transfer_ActorOfTransientProcess):
    """
    This class performs the transfer of an Entity from
    AP214 and AP203, either Geometric or Topologic.

    I.E. for each type of Entity, it invokes the appropriate Tool
    then returns the Binder which contains the Result
    """

    @overload
    def __init__(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> None: ...

    @overload
    def __init__(self, theOther: STEPControl_ActorRead) -> None: ...

    def Recognize(self, start: nanoocp.Standard.Standard_Transient | None) -> bool: ...

    def Transfer(self, start: nanoocp.Standard.Standard_Transient | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder: ...

    def TransferShape(self, start: nanoocp.Standard.Standard_Transient | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., isManifold: bool = True, theUseTrsf: bool = False, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder:
        """
        theUseTrsf - special flag for using Axis2Placement from ShapeRepresentation for transform root
        shape
        """

    def PrepareUnits(self, rep: nanoocp.StepRepr.StepRepr_Representation | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors) -> None:
        """set units and tolerances context by given ShapeRepresentation"""

    def ResetUnits(self, theModel: nanoocp.StepData.StepData_StepModel | None, theLocalFactors: nanoocp.StepData.StepData_Factors) -> None:
        """
        reset units and tolerances context to default
        (mm, radians, read.precision.val, etc.)
        """

    def SetModel(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """Set model"""

    def ComputeTransformation(self, Origin: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, Target: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, OrigContext: nanoocp.StepRepr.StepRepr_Representation | None, TargContext: nanoocp.StepRepr.StepRepr_Representation | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, Trsf: nanoocp.gp.gp_Trsf, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """
        Computes transformation defined by two axis placements (in MAPPED_ITEM
        or ITEM_DEFINED_TRANSFORMATION) taking into account their
        representation contexts (i.e. units, which may be different)
        Returns True if transformation is computed and is not an identity.
        """

    def ComputeSRRWT(self, SRR: nanoocp.StepRepr.StepRepr_RepresentationRelationship | None, TP: nanoocp.Transfer.Transfer_TransientProcess | None, Trsf: nanoocp.gp.gp_Trsf, theLocalFactors: nanoocp.StepData.StepData_Factors = ...) -> bool:
        """
        Computes transformation defined by given
        REPRESENTATION_RELATIONSHIP_WITH_TRANSFORMATION
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPControl_ActorWrite(nanoocp.Transfer.Transfer_ActorOfFinderProcess):
    """
    This class performs the transfer of a Shape from TopoDS
    to AP203 or AP214 (CD2 or DIS)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPControl_ActorWrite) -> None: ...

    def Recognize(self, start: nanoocp.Transfer.Transfer_Finder | None) -> bool: ...

    def Transfer(self, start: nanoocp.Transfer.Transfer_Finder | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder: ...

    def TransferSubShape(self, start: nanoocp.Transfer.Transfer_Finder | None, SDR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., shapeGroup: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None = None, isManifold: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[nanoocp.Transfer.Transfer_Binder, nanoocp.StepGeom.StepGeom_GeometricRepresentationItem]: ...

    def TransferShape(self, start: nanoocp.Transfer.Transfer_Finder | None, SDR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., shapeGroup: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None = None, isManifold: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder: ...

    def TransferCompound(self, start: nanoocp.Transfer.Transfer_Finder | None, SDR: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, theLocalFactors: nanoocp.StepData.StepData_Factors = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Transfer.Transfer_Binder: ...

    def SetMode(self, M: STEPControl_StepModelType) -> None: ...

    def Mode(self) -> STEPControl_StepModelType: ...

    def SetGroupMode(self, mode: int) -> None: ...

    def GroupMode(self) -> int: ...

    def SetTolerance(self, Tol: float) -> None: ...

    def IsAssembly(self, theModel: nanoocp.StepData.StepData_StepModel | None, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Customizable method to check whether shape S should
        be written as assembly or not
        Default implementation uses flag GroupMode and analyses
        the shape itself
        NOTE: this method can modify shape
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPControl_Controller(nanoocp.XSControl.XSControl_Controller):
    """defines basic controller for STEP processor"""

    @overload
    def __init__(self) -> None:
        """
        Initializes the use of STEP Norm (the first time) and
        returns a Controller
        """

    @overload
    def __init__(self, theOther: STEPControl_Controller) -> None: ...

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Creates a new empty Model ready to receive data of the Norm.
        It is taken from STEP Template Model
        """

    def ActorRead(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """Returns the Actor for Read attached to the pair (norm,appli)"""

    def Customise(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> nanoocp.XSControl.XSControl_WorkSession: ...

    def TransferWriteShape(self, shape: nanoocp.TopoDS.TopoDS_Shape, FP: nanoocp.Transfer.Transfer_FinderProcess | None, model: nanoocp.Interface.Interface_InterfaceModel | None, modetrans: int = 0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Takes one Shape and transfers it to the InterfaceModel
        (already created by NewModel for instance)
        <modeshape> is to be interpreted by each kind of XstepAdaptor
        Returns a status : 0 OK  1 No result  2 Fail  -1 bad modeshape
        -2 bad model (requires a StepModel)
        modeshape : 1 Facetted BRep, 2 Shell, 3 Manifold Solid
        """

    @staticmethod
    def Init() -> bool:
        """
        Standard Initialisation. It creates a Controller for STEP
        and records it to various names, available to select it later
        Returns True when done, False if could not be done
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPControl_Reader(nanoocp.XSControl.XSControl_Reader):
    """
    Reads STEP files, checks them and translates their contents
    into Open CASCADE models. The STEP data can be that of
    a whole model or that of a specific list of entities in the model.
    As in XSControl_Reader, you specify the list using a selection.
    For the translation of iges files it is possible to use next sequence:
    To change translation parameters
    class Interface_Static should be used before beginning of
    translation (see STEP Parameters and General Parameters)
    Creation of reader - STEPControl_Reader reader;
    To load s file in a model use method reader.ReadFile("filename.stp")
    To print load results reader.PrintCheckLoad(failsonly,mode)
    where mode is equal to the value of enumeration IFSelect_PrintCount
    For definition number of candidates :
    int nbroots = reader. NbRootsForTransfer();
    To transfer entities from a model the following methods can be used:
    for the whole model - reader.TransferRoots();
    to transfer a list of entities: reader.TransferList(list);
    to transfer one entity occ::handle<Standard_Transient>
    ent = reader.RootForTransfer(num);
    reader.TransferEntity(ent), or
    reader.TransferOneRoot(num), or
    reader.TransferOne(num), or
    reader.TransferRoot(num)
    To obtain the result the following method can be used:
    reader.NbShapes() and reader.Shape(num); or reader.OneShape();
    To print the results of transfer use method:
    reader.PrintCheckTransfer(failwarn,mode);
    where printfail is equal to the value of enumeration
    IFSelect_PrintFail, mode see above; or reader.PrintStatsTransfer();
    Gets correspondence between a STEP entity and a result
    shape obtained from it.
    occ::handle<XSControl_WorkSession>
    WS = reader.WS();
    if ( WS->TransferReader()->HasResult(ent) )
    TopoDS_Shape shape = WS->TransferReader()->ShapeResult(ent);
    """

    @overload
    def __init__(self) -> None:
        """Creates a reader object with an empty STEP model."""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a Reader for STEP from an already existing Session
        Clears the session if it was not yet set for STEP
        """

    @overload
    def __init__(self, theOther: STEPControl_Reader) -> None: ...

    def StepModel(self) -> nanoocp.StepData.StepData_StepModel:
        """
        Returns the model as a StepModel.
        It can then be consulted (header, product)
        """

    @overload
    def ReadFile(self, filename: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus: ...

    @overload
    def ReadFile(self, filename: str, theParams: nanoocp.DESTEP.DESTEP_Parameters) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Loads a file and returns the read status
        Zero for a Model which compies with the Controller
        """

    @overload
    def ReadStream(self, theName: str, theIStream: TextIO) -> nanoocp.IFSelect.IFSelect_ReturnStatus: ...

    @overload
    def ReadStream(self, theName: str, theParams: nanoocp.DESTEP.DESTEP_Parameters, theIStream: TextIO) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Loads a file from stream and returns the read status"""

    def TransferRoot(self, num: int = 1, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a root given its rank in the list of candidate roots
        Default is the first one
        Returns True if a shape has resulted, false else
        Same as inherited TransferOneRoot, kept for compatibility
        """

    def NbRootsForTransfer(self) -> int:
        """
        Determines the list of root entities from Model which are candidate for
        a transfer to a Shape (type of entities is PRODUCT)
        """

    def FileUnits(self, theUnitLengthNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString], theUnitAngleNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString], theUnitSolidAngleNames: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Returns sequence of all unit names for shape representations
        found in file
        """

    def SetSystemLengthUnit(self, theLengthUnit: float) -> None:
        """
        Sets system length unit used by transfer process.
        Performs only if a model is not NULL
        """

    def SystemLengthUnit(self) -> float:
        """
        Returns system length unit used by transfer process.
        Performs only if a model is not NULL
        """

class STEPControl_Writer:
    """
    This class creates and writes
    STEP files from Open CASCADE models. A STEP file can be
    written to an existing STEP file or to a new one.
    Translation can be performed in one or several operations. Each
    translation operation outputs a distinct root entity in the STEP file.
    """

    @overload
    def __init__(self) -> None:
        """Creates a Writer from scratch"""

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a Writer from an already existing Session
        If <scratch> is True (D), clears already recorded data
        """

    @overload
    def __init__(self, theOther: STEPControl_Writer) -> None: ...

    def SetTolerance(self, Tol: float) -> None:
        """
        Sets a length-measure value that
        will be written to uncertainty-measure-with-unit
        when the next shape is translated.
        """

    def UnsetTolerance(self) -> None:
        """Unsets the tolerance formerly forced by SetTolerance"""

    def SetWS(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """Sets a specific session to <me>"""

    def WS(self) -> nanoocp.XSControl.XSControl_WorkSession:
        """Returns the session used in <me>"""

    def Model(self, newone: bool = False) -> nanoocp.StepData.StepData_StepModel:
        """
        Returns the produced model. Produces a new one if not yet done
        or if <newone> is True
        This method allows for instance to edit product or header
        data before writing.
        """

    @overload
    def Transfer(self, sh: nanoocp.TopoDS.TopoDS_Shape, mode: STEPControl_StepModelType, compgraph: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Translates shape sh to a STEP
        entity. mode defines the STEP entity type to be output:
        - STEPControlStd_AsIs translates a shape to its highest possible
        STEP representation.
        - STEPControlStd_ManifoldSolidBrep translates a shape to a STEP
        manifold_solid_brep or brep_with_voids entity.
        - STEPControlStd_FacetedBrep translates a shape into a STEP
        faceted_brep entity.
        - STEPControlStd_ShellBasedSurfaceModel translates a shape into a STEP
        shell_based_surface_model entity.
        - STEPControlStd_GeometricCurveSet translates a shape into a STEP
        geometric_curve_set entity.
        """

    @overload
    def Transfer(self, sh: nanoocp.TopoDS.TopoDS_Shape, mode: STEPControl_StepModelType, theParams: nanoocp.DESTEP.DESTEP_Parameters, compgraph: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Translates shape sh to a STEP entity"""

    def Write(self, theFileName: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Writes a STEP model in the file identified by filename."""

    def WriteStream(self) -> tuple[nanoocp.IFSelect.IFSelect_ReturnStatus, str]:
        """Writes a STEP model in the std::ostream."""

    def PrintStatsTransfer(self, what: int, mode: int = 0) -> None:
        """
        Displays the statistics for the
        last translation. what defines the kind of statistics that are displayed:
        - 0 gives general statistics (number of translated roots,
        number of warnings, number of fail messages),
        - 1 gives root results,
        - 2 gives statistics for all checked entities,
        - 3 gives the list of translated entities,
        - 4 gives warning and fail messages,
        - 5 gives fail messages only.
        mode is used according to the use of what. If what is 0, mode is
        ignored. If what is 1, 2 or 3, mode defines the following:
        - 0 lists the numbers of STEP entities in a STEP model,
        - 1 gives the number, identifier, type and result type for each
        STEP entity and/or its status (fail, warning, etc.),
        - 2 gives maximum information for each STEP entity (i.e. checks),
        - 3 gives the number of entities by the type of a STEP entity,
        - 4 gives the number of of STEP entities per result type and/or status,
        - 5 gives the number of pairs (STEP or result type and status),
        - 6 gives the number of pairs (STEP or result type and status)
        AND the list of entity numbers in the STEP model.
        """

    def CleanDuplicateEntities(self) -> None: ...

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are converted and stored in the internal map.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the internal map.
        Parameters from @p theAdditionalParameters are copied to the internal map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        """

    def GetShapeFixParameters(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns parameters for shape processing that was set by SetParameters() method.
        @return the parameters for shape processing. Empty map if no parameters were set.
        """

    def SetShapeProcessFlags(self, theFlags: set[int]) -> None:
        """
        Sets flags defining operations to be performed on shapes.
        @param theFlags The flags defining operations to be performed on shapes.
        """

    def GetShapeProcessFlags(self) -> tuple[set[int], bool]:
        """
        Returns flags defining operations to be performed on shapes.
        @return Pair of values defining operations to be performed on shapes and a boolean value
        that indicates whether the flags were set.
        """
