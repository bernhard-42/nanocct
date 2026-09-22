"""OCCT package STEPCAFControl (toolkit TKDESTEP)"""

from typing import TextIO, overload

import nanoocp.DE
import nanoocp.DESTEP
import nanoocp.IFSelect
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.STEPConstruct
import nanoocp.STEPControl
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepDimTol
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.StepVisual
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XCAFDimTolObjects
import nanoocp.XCAFDoc
import nanoocp.XSControl
import nanoocp.STEPCAFControl
import nanoocp.TopTools


class STEPCAFControl_ActorWrite(nanoocp.STEPControl.STEPControl_ActorWrite):
    """
    Extends ActorWrite from STEPControl by analysis of
    whether shape is assembly (based on information from DECAF)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPCAFControl_ActorWrite) -> None: ...

    def IsAssembly(self, theModel: nanoocp.StepData.StepData_StepModel | None, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Check whether shape S is assembly
        Returns True if shape is registered in assemblies map
        """

    def SetStdMode(self, stdmode: bool = True) -> None:
        """
        Set standard mode of work
        In standard mode Actor (default) behaves exactly as its
        ancestor, also map is cleared
        """

    def ClearMap(self) -> None:
        """Clears map of shapes registered as assemblies"""

    def RegisterAssembly(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Registers shape to be written as assembly
        The shape should be TopoDS_Compound (else does nothing)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPCAFControl_Controller(nanoocp.STEPControl.STEPControl_Controller):
    """
    Extends Controller from STEPControl in order to provide
    ActorWrite adapted for writing assemblies from DECAF
    Note that ActorRead from STEPControl is used for reading
    (inherited automatically)
    """

    @overload
    def __init__(self) -> None:
        """Initializes the use of STEP Norm (the first time)"""

    @overload
    def __init__(self, theOther: STEPCAFControl_Controller) -> None: ...

    @staticmethod
    def Init() -> bool:
        """
        Standard Initialisation. It creates a Controller for STEP-XCAF
        and records it to various names, available to select it later
        Returns True when done, False if could not be done
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPCAFControl_ExternFile(nanoocp.Standard.Standard_Transient):
    """
    Auxiliary class serving as container for data resulting
    from translation of external file
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty structure"""

    @overload
    def __init__(self, theOther: STEPCAFControl_ExternFile) -> None: ...

    def SetWS(self, WS: nanoocp.XSControl.XSControl_WorkSession | None) -> None: ...

    def GetWS(self) -> nanoocp.XSControl.XSControl_WorkSession: ...

    def SetLoadStatus(self, stat: nanoocp.IFSelect.IFSelect_ReturnStatus) -> None: ...

    def GetLoadStatus(self) -> nanoocp.IFSelect.IFSelect_ReturnStatus: ...

    def SetTransferStatus(self, isok: bool) -> None: ...

    def GetTransferStatus(self) -> bool: ...

    def SetWriteStatus(self, stat: nanoocp.IFSelect.IFSelect_ReturnStatus) -> None: ...

    def GetWriteStatus(self) -> nanoocp.IFSelect.IFSelect_ReturnStatus: ...

    def SetName(self, name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def GetName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetLabel(self, L: nanoocp.TDF.TDF_Label) -> None: ...

    def GetLabel(self) -> nanoocp.TDF.TDF_Label: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPCAFControl_GDTProperty:
    """
    This class provides tools for access (read)
    the GDT properties.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPCAFControl_GDTProperty) -> None: ...

    @staticmethod
    def GetDimModifiers(theCRI: nanoocp.StepRepr.StepRepr_CompoundRepresentationItem | None, theModifiers: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif]) -> None: ...

    @staticmethod
    def GetDimClassOfTolerance(theLAF: nanoocp.StepShape.StepShape_LimitsAndFits | None) -> tuple[bool, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade]: ...

    @staticmethod
    def GetDimType(theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> tuple[bool, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType]: ...

    @staticmethod
    def GetDatumTargetType(theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> tuple[bool, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType]: ...

    @staticmethod
    def GetDimQualifierType(theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> tuple[bool, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier]: ...

    @overload
    @staticmethod
    def GetTolValueType(theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> tuple[bool, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue]: ...

    @overload
    @staticmethod
    def GetTolValueType(theType: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceTypeValue) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def GetDimTypeName(theType: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionType) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def GetDimQualifierName(theQualifier: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionQualifier) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def GetDimModifierName(theModifier: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def GetLimitsAndFits(theHole: bool, theFormVariance: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionFormVariance, theGrade: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionGrade) -> nanoocp.StepShape.StepShape_LimitsAndFits: ...

    @staticmethod
    def GetDatumTargetName(theDatumType: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumTargetType) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @overload
    @staticmethod
    def GetGeomToleranceType(theType: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType) -> nanoocp.StepDimTol.StepDimTol_GeometricToleranceType: ...

    @overload
    @staticmethod
    def GetGeomToleranceType(theType: nanoocp.StepDimTol.StepDimTol_GeometricToleranceType) -> nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType: ...

    @staticmethod
    def GetGeomTolerance(theType: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceType) -> nanoocp.StepDimTol.StepDimTol_GeometricTolerance: ...

    @staticmethod
    def GetGeomToleranceModifier(theModifier: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif) -> nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier: ...

    @staticmethod
    def GetDatumRefModifiers(theModifiers: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif], theModifWithVal: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumModifWithValue, theValue: float, theUnit: nanoocp.StepBasic.StepBasic_Unit) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier]: ...

    @staticmethod
    def GetTessellation(theShape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.StepVisual.StepVisual_TessellatedGeometricSet: ...

class STEPCAFControl_Reader:
    """
    Provides a tool to read STEP file and put it into
    DECAF document. Besides transfer of shapes (including
    assemblies) provided by STEPControl, supports also
    colors and part names

    This reader supports reading files with external references
    i.e. multifile reading
    It behaves as usual Reader (from STEPControl) for the main
    file (e.g. if it is single file)
    Results of reading other files can be accessed by name of the
    file or by iterating on a readers
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a reader with an empty
        STEP model and sets ColorMode, LayerMode, NameMode and
        PropsMode to true.
        """

    @overload
    def __init__(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a reader tool and attaches it to an already existing Session
        Clears the session if it was not yet set for STEP
        """

    @overload
    def __init__(self, theOther: STEPCAFControl_Reader) -> None: ...

    def Init(self, WS: nanoocp.XSControl.XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Clears the internal data structures and attaches to a new session
        Clears the session if it was not yet set for STEP
        """

    @overload
    def ReadFile(self, theFileName: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Loads a file and returns the read status
        Provided for use like single-file reader.
        @param[in] theFileName  file to open
        @return read status
        """

    @overload
    def ReadFile(self, theFileName: str, theParams: nanoocp.DESTEP.DESTEP_Parameters) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Loads a file and returns the read status
        Provided for use like single-file reader.
        @param[in] theFileName  file to open
        @param[in] theParams  default configuration parameters
        @return read status
        """

    def ReadStream(self, theName: str, theIStream: TextIO) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Loads a file from stream and returns the read status.
        @param[in] theName  auxiliary stream name
        @param[in] theIStream  stream to read from
        @return read status
        """

    def NbRootsForTransfer(self) -> int:
        """
        Returns number of roots recognized for transfer
        Shortcut for Reader().NbRootsForTransfer()
        """

    def TransferOneRoot(self, num: int, doc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates currently loaded STEP file into the document
        Returns True if succeeded, and False in case of fail
        Provided for use like single-file reader
        """

    def Transfer(self, doc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates currently loaded STEP file into the document
        Returns True if succeeded, and False in case of fail
        Provided for use like single-file reader
        """

    @overload
    def Perform(self, filename: nanoocp.TCollection.TCollection_AsciiString, doc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, filename: nanoocp.TCollection.TCollection_AsciiString, doc: nanoocp.TDocStd.TDocStd_Document | None, theParams: nanoocp.DESTEP.DESTEP_Parameters, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, filename: str, doc: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, filename: str, doc: nanoocp.TDocStd.TDocStd_Document | None, theParams: nanoocp.DESTEP.DESTEP_Parameters, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translate STEP file given by filename into the document
        Return True if succeeded, and False in case of fail
        """

    def ExternFiles(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.STEPCAFControl.STEPCAFControl_ExternFile]:
        """
        Returns data on external files
        Returns Null handle if no external files are read
        """

    def ExternFile(self, name: str) -> tuple[bool, STEPCAFControl_ExternFile]:
        """
        Returns data on external file by its name
        Returns False if no external file with given name is read
        """

    def ChangeReader(self) -> nanoocp.STEPControl.STEPControl_Reader:
        """Returns basic reader"""

    def Reader(self) -> nanoocp.STEPControl.STEPControl_Reader:
        """Returns basic reader as const"""

    @staticmethod
    def FindInstance(NAUO: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None, STool: nanoocp.XCAFDoc.XCAFDoc_ShapeTool | None, Tool: nanoocp.STEPConstruct.STEPConstruct_Tool, ShapeLabelMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> nanoocp.TDF.TDF_Label:
        """
        Returns label of instance of an assembly component
        corresponding to a given NAUO
        """

    def SetColorMode(self, colormode: bool) -> None:
        """Set ColorMode for indicate read Colors or not."""

    def GetColorMode(self) -> bool: ...

    def SetNameMode(self, namemode: bool) -> None:
        """Set NameMode for indicate read Name or not."""

    def GetNameMode(self) -> bool: ...

    def SetLayerMode(self, layermode: bool) -> None:
        """Set LayerMode for indicate read Layers or not."""

    def GetLayerMode(self) -> bool: ...

    def SetPropsMode(self, propsmode: bool) -> None:
        """PropsMode for indicate read Validation properties or not."""

    def GetPropsMode(self) -> bool: ...

    def SetMetaMode(self, theMetaMode: bool) -> None:
        """MetaMode for indicate read Metadata or not."""

    def GetMetaMode(self) -> bool: ...

    def SetProductMetaMode(self, theProductMetaMode: bool) -> None:
        """MetaMode for indicate whether to read Product Metadata or not."""

    def GetProductMetaMode(self) -> bool: ...

    def SetSHUOMode(self, shuomode: bool) -> None:
        """Set SHUO mode for indicate write SHUO or not."""

    def GetSHUOMode(self) -> bool: ...

    def SetGDTMode(self, gdtmode: bool) -> None:
        """Set GDT mode for indicate write GDT or not."""

    def GetGDTMode(self) -> bool: ...

    def SetMatMode(self, matmode: bool) -> None:
        """Set Material mode"""

    def GetMatMode(self) -> bool: ...

    def SetViewMode(self, viewmode: bool) -> None:
        """Set View mode"""

    def GetViewMode(self) -> bool:
        """Get View mode"""

    def GetShapeLabelMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
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

class STEPCAFControl_Writer:
    """
    Provides a tool to write DECAF document to the
    STEP file. Besides transfer of shapes (including
    assemblies) provided by STEPControl, supports also
    colors and part names

    Also supports multifile writing
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a writer with an empty
        STEP model and sets ColorMode, LayerMode, NameMode and
        PropsMode to true.
        """

    @overload
    def __init__(self, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theScratch: bool = True) -> None:
        """
        Creates a reader tool and attaches it to an already existing Session
        Clears the session if it was not yet set for STEP
        Clears the internal data structures
        """

    @overload
    def __init__(self, theOther: STEPCAFControl_Writer) -> None: ...

    def Init(self, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theScratch: bool = True) -> None:
        """
        Clears the internal data structures and attaches to a new session
        Clears the session if it was not yet set for STEP
        """

    def Write(self, theFileName: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Writes all the produced models into file
        In case of multimodel with extern references,
        filename will be a name of root file, all other files
        have names of corresponding parts
        Provided for use like single-file writer
        """

    def WriteStream(self) -> tuple[nanoocp.IFSelect.IFSelect_ReturnStatus, str]:
        """
        Writes all the produced models into the stream.
        Provided for use like single-file writer
        """

    @overload
    def Transfer(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document (or single label) to a STEP model
        The mode of translation of shape is AsIs
        If multi is not null pointer, it switches to multifile
        mode (with external refs), and string pointed by <multi>
        gives prefix for names of extern files (can be empty string)
        Returns True if translation is OK
        """

    @overload
    def Transfer(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theParams: nanoocp.DESTEP.DESTEP_Parameters, theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document (or single label) to a STEP model
        This method uses if need to set parameters avoiding
        initialization from Interface_Static
        @param theParams  configuration parameters
        @param theMode    mode of translation of shape is AsIs
        @param theIsMulti if multi is not null pointer, it switches to multifile
        mode (with external refs), and string pointed by <multi>
        gives prefix for names of extern files (can be empty string)
        @param theProgress progress indicator
        Returns True if translation is OK
        """

    @overload
    def Transfer(self, theLabel: nanoocp.TDF.TDF_Label, theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """Method to transfer part of the document specified by label"""

    @overload
    def Transfer(self, theLabel: nanoocp.TDF.TDF_Label, theParams: nanoocp.DESTEP.DESTEP_Parameters, theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Method to transfer part of the document specified by label
        This method uses if need to set parameters avoiding
        initialization from Interface_Static
        """

    @overload
    def Transfer(self, theLabelSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Method to writing sequence of root assemblies
        or part of the file specified by use by one label
        """

    @overload
    def Transfer(self, theLabelSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theParams: nanoocp.DESTEP.DESTEP_Parameters, theMode: nanoocp.STEPControl.STEPControl_StepModelType = STEPControl_StepModelType.STEPControl_AsIs, theIsMulti: str | None = None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Method to writing sequence of root assemblies
        or part of the file specified by use by one label.
        This method is utilized if there's a need to set parameters avoiding
        initialization from Interface_Static
        """

    @overload
    def Perform(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theFileName: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool: ...

    @overload
    def Perform(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theFileName: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document and writes it to a STEP file
        Returns True if translation is OK
        """

    @overload
    def Perform(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theFileName: str, theParams: nanoocp.DESTEP.DESTEP_Parameters, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers a document and writes it to a STEP file
        This method is utilized if there's a need to set parameters avoiding
        initialization from Interface_Static
        Returns True if translation is OK
        """

    def ExternFiles(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.STEPCAFControl.STEPCAFControl_ExternFile]:
        """
        Returns data on external files
        Returns Null handle if no external files are read
        """

    @overload
    def ExternFile(self, theLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, STEPCAFControl_ExternFile]:
        """
        Returns data on external file by its original label
        Returns False if no external file with given name is read
        """

    @overload
    def ExternFile(self, theName: str) -> tuple[bool, STEPCAFControl_ExternFile]:
        """
        Returns data on external file by its name
        Returns False if no external file with given name is read
        """

    def ChangeWriter(self) -> nanoocp.STEPControl.STEPControl_Writer:
        """Returns basic reader for root file"""

    def Writer(self) -> nanoocp.STEPControl.STEPControl_Writer:
        """Returns basic reader as const"""

    def SetColorMode(self, theColorMode: bool) -> None:
        """Set ColorMode for indicate write Colors or not."""

    def GetColorMode(self) -> bool: ...

    def SetNameMode(self, theNameMode: bool) -> None:
        """Set NameMode for indicate write Name or not."""

    def GetNameMode(self) -> bool: ...

    def SetLayerMode(self, theLayerMode: bool) -> None:
        """Set LayerMode for indicate write Layers or not."""

    def GetLayerMode(self) -> bool: ...

    def SetPropsMode(self, thePropsMode: bool) -> None:
        """PropsMode for indicate write Validation properties or not."""

    def GetPropsMode(self) -> bool: ...

    def SetMetadataMode(self, theMetadataMode: bool) -> None:
        """Set MetadataMode for indicate write metadata or not."""

    def GetMetadataMode(self) -> bool: ...

    def SetSHUOMode(self, theSHUOMode: bool) -> None:
        """Set SHUO mode for indicate write SHUO or not."""

    def GetSHUOMode(self) -> bool: ...

    def SetDimTolMode(self, theDimTolMode: bool) -> None:
        """Set dimtolmode for indicate write D&GTs or not."""

    def GetDimTolMode(self) -> bool: ...

    def SetMaterialMode(self, theMaterialMode: bool) -> None:
        """Set flag for indicate write material or not."""

    def GetMaterialMode(self) -> bool: ...

    def SetVisualMaterialMode(self, theVisualMaterialMode: bool) -> None:
        """Set flag for indicate write visual material or not."""

    def GetVisualMaterialMode(self) -> bool: ...

    def SetCleanDuplicates(self, theCleanDuplicates: bool) -> None:
        """
        Set clean duplicates flag.
        If set to True, duplicates will be removed from the model.
        @param theCleanDuplicates the flag to set.
        """

    def GetCleanDuplicates(self) -> bool:
        """
        Returns the flag indicating whether duplicates should be removed from the model.
        @return the flag indicating whether duplicates should be removed from the model.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
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
