"""OCCT package DESTEP (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.DE
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Resource
import nanoocp.STEPControl
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.UnitsMethods
import nanoocp.XSControl


class DESTEP_Parameters:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DESTEP_Parameters) -> None: ...

    class ReadMode_BSplineContinuity(enum.IntEnum):
        ReadMode_BSplineContinuity_C0 = 0

        ReadMode_BSplineContinuity_C1 = 1

        ReadMode_BSplineContinuity_C2 = 2

    ReadMode_BSplineContinuity_C0: DESTEP_Parameters.ReadMode_BSplineContinuity = ...

    ReadMode_BSplineContinuity_C1: DESTEP_Parameters.ReadMode_BSplineContinuity = ...

    ReadMode_BSplineContinuity_C2: DESTEP_Parameters.ReadMode_BSplineContinuity = ...

    class ReadMode_Precision(enum.IntEnum):
        ReadMode_Precision_File = 0

        ReadMode_Precision_User = 1

    ReadMode_Precision_File: DESTEP_Parameters.ReadMode_Precision = ReadMode_Precision.ReadMode_Precision_File

    ReadMode_Precision_User: DESTEP_Parameters.ReadMode_Precision = ReadMode_Precision.ReadMode_Precision_User

    class ReadMode_MaxPrecision(enum.IntEnum):
        ReadMode_MaxPrecision_Preferred = 0

        ReadMode_MaxPrecision_Forced = 1

    ReadMode_MaxPrecision_Preferred: DESTEP_Parameters.ReadMode_MaxPrecision = ...

    ReadMode_MaxPrecision_Forced: DESTEP_Parameters.ReadMode_MaxPrecision = ...

    class ReadMode_SurfaceCurve(enum.IntEnum):
        ReadMode_SurfaceCurve_Default = 0

        ReadMode_SurfaceCurve_2DUse_Preferred = 2

        ReadMode_SurfaceCurve_2DUse_Forced = -2

        ReadMode_SurfaceCurve_3DUse_Preferred = 3

        ReadMode_SurfaceCurve_3DUse_Forced = -3

    ReadMode_SurfaceCurve_Default: DESTEP_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_2DUse_Preferred: DESTEP_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_2DUse_Forced: DESTEP_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_3DUse_Preferred: DESTEP_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_3DUse_Forced: DESTEP_Parameters.ReadMode_SurfaceCurve = ...

    class AngleUnitMode(enum.IntEnum):
        AngleUnitMode_File = 0

        AngleUnitMode_Rad = 1

        AngleUnitMode_Deg = 2

    AngleUnitMode_File: DESTEP_Parameters.AngleUnitMode = AngleUnitMode.AngleUnitMode_File

    AngleUnitMode_Rad: DESTEP_Parameters.AngleUnitMode = AngleUnitMode.AngleUnitMode_Rad

    AngleUnitMode_Deg: DESTEP_Parameters.AngleUnitMode = AngleUnitMode.AngleUnitMode_Deg

    class ReadMode_ProductContext(enum.IntEnum):
        ReadMode_ProductContext_All = 1

        ReadMode_ProductContext_Design = 2

        ReadMode_ProductContext_Analysis = 3

    ReadMode_ProductContext_All: DESTEP_Parameters.ReadMode_ProductContext = ...

    ReadMode_ProductContext_Design: DESTEP_Parameters.ReadMode_ProductContext = ...

    ReadMode_ProductContext_Analysis: DESTEP_Parameters.ReadMode_ProductContext = ...

    class ReadMode_ShapeRepr(enum.IntEnum):
        ReadMode_ShapeRepr_All = 1

        ReadMode_ShapeRepr_ABSR = 2

        ReadMode_ShapeRepr_MSSR = 3

        ReadMode_ShapeRepr_GBSSR = 4

        ReadMode_ShapeRepr_FBSR = 5

        ReadMode_ShapeRepr_EBWSR = 6

        ReadMode_ShapeRepr_GBWSR = 7

    ReadMode_ShapeRepr_All: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_All

    ReadMode_ShapeRepr_ABSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_ABSR

    ReadMode_ShapeRepr_MSSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_MSSR

    ReadMode_ShapeRepr_GBSSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_GBSSR

    ReadMode_ShapeRepr_FBSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_FBSR

    ReadMode_ShapeRepr_EBWSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_EBWSR

    ReadMode_ShapeRepr_GBWSR: DESTEP_Parameters.ReadMode_ShapeRepr = ReadMode_ShapeRepr.ReadMode_ShapeRepr_GBWSR

    class ReadMode_AssemblyLevel(enum.IntEnum):
        ReadMode_AssemblyLevel_All = 1

        ReadMode_AssemblyLevel_Assembly = 2

        ReadMode_AssemblyLevel_Structure = 3

        ReadMode_AssemblyLevel_Shape = 4

    ReadMode_AssemblyLevel_All: DESTEP_Parameters.ReadMode_AssemblyLevel = ReadMode_AssemblyLevel.ReadMode_AssemblyLevel_All

    ReadMode_AssemblyLevel_Assembly: DESTEP_Parameters.ReadMode_AssemblyLevel = ...

    ReadMode_AssemblyLevel_Structure: DESTEP_Parameters.ReadMode_AssemblyLevel = ...

    ReadMode_AssemblyLevel_Shape: DESTEP_Parameters.ReadMode_AssemblyLevel = ...

    class RWMode_Tessellated(enum.IntEnum):
        RWMode_Tessellated_Off = 0

        RWMode_Tessellated_On = 1

        RWMode_Tessellated_OnNoBRep = 2

    RWMode_Tessellated_Off: DESTEP_Parameters.RWMode_Tessellated = RWMode_Tessellated.RWMode_Tessellated_Off

    RWMode_Tessellated_On: DESTEP_Parameters.RWMode_Tessellated = RWMode_Tessellated.RWMode_Tessellated_On

    RWMode_Tessellated_OnNoBRep: DESTEP_Parameters.RWMode_Tessellated = RWMode_Tessellated.RWMode_Tessellated_OnNoBRep

    class WriteMode_PrecisionMode(enum.IntEnum):
        WriteMode_PrecisionMode_Least = -1

        WriteMode_PrecisionMode_Average = 0

        WriteMode_PrecisionMode_Greatest = 1

        WriteMode_PrecisionMode_Session = 2

    WriteMode_PrecisionMode_Least: DESTEP_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Average: DESTEP_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Greatest: DESTEP_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Session: DESTEP_Parameters.WriteMode_PrecisionMode = ...

    class WriteMode_Assembly(enum.IntEnum):
        WriteMode_Assembly_Off = 0

        WriteMode_Assembly_On = 1

        WriteMode_Assembly_Auto = 2

    WriteMode_Assembly_Off: DESTEP_Parameters.WriteMode_Assembly = WriteMode_Assembly.WriteMode_Assembly_Off

    WriteMode_Assembly_On: DESTEP_Parameters.WriteMode_Assembly = WriteMode_Assembly.WriteMode_Assembly_On

    WriteMode_Assembly_Auto: DESTEP_Parameters.WriteMode_Assembly = WriteMode_Assembly.WriteMode_Assembly_Auto

    class WriteMode_StepSchema(enum.IntEnum):
        WriteMode_StepSchema_AP214CD = 1

        WriteMode_StepSchema_AP214DIS = 2

        WriteMode_StepSchema_AP203 = 3

        WriteMode_StepSchema_AP214IS = 4

        WriteMode_StepSchema_AP242DIS = 5

    WriteMode_StepSchema_AP214CD: DESTEP_Parameters.WriteMode_StepSchema = WriteMode_StepSchema.WriteMode_StepSchema_AP214CD

    WriteMode_StepSchema_AP214DIS: DESTEP_Parameters.WriteMode_StepSchema = ...

    WriteMode_StepSchema_AP203: DESTEP_Parameters.WriteMode_StepSchema = WriteMode_StepSchema.WriteMode_StepSchema_AP203

    WriteMode_StepSchema_AP214IS: DESTEP_Parameters.WriteMode_StepSchema = WriteMode_StepSchema.WriteMode_StepSchema_AP214IS

    WriteMode_StepSchema_AP242DIS: DESTEP_Parameters.WriteMode_StepSchema = ...

    class WriteMode_VertexMode(enum.IntEnum):
        WriteMode_VertexMode_OneCompound = 0

        WriteMode_VertexMode_SingleVertex = 1

    WriteMode_VertexMode_OneCompound: DESTEP_Parameters.WriteMode_VertexMode = ...

    WriteMode_VertexMode_SingleVertex: DESTEP_Parameters.WriteMode_VertexMode = ...

    def InitFromStatic(self) -> None:
        """Initialize parameters"""

    def Reset(self) -> None:
        """Reset used parameters"""

    def GetString(self, theMode: DESTEP_Parameters.ReadMode_ProductContext) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @staticmethod
    def GetDefaultShapeFixParameters() -> nanoocp.DE.DE_ShapeFixParameters:
        """Returns default shape fix parameters for transferring STEP files."""

    @property
    def ReadBSplineContinuity(self) -> DESTEP_Parameters.ReadMode_BSplineContinuity: ...

    @ReadBSplineContinuity.setter
    def ReadBSplineContinuity(self, arg: DESTEP_Parameters.ReadMode_BSplineContinuity, /) -> None: ...

    @property
    def ReadPrecisionMode(self) -> DESTEP_Parameters.ReadMode_Precision: ...

    @ReadPrecisionMode.setter
    def ReadPrecisionMode(self, arg: DESTEP_Parameters.ReadMode_Precision, /) -> None: ...

    @property
    def ReadPrecisionVal(self) -> float: ...

    @ReadPrecisionVal.setter
    def ReadPrecisionVal(self, arg: float, /) -> None: ...

    @property
    def ReadMaxPrecisionMode(self) -> DESTEP_Parameters.ReadMode_MaxPrecision: ...

    @ReadMaxPrecisionMode.setter
    def ReadMaxPrecisionMode(self, arg: DESTEP_Parameters.ReadMode_MaxPrecision, /) -> None: ...

    @property
    def ReadMaxPrecisionVal(self) -> float: ...

    @ReadMaxPrecisionVal.setter
    def ReadMaxPrecisionVal(self, arg: float, /) -> None: ...

    @property
    def ReadSameParamMode(self) -> bool: ...

    @ReadSameParamMode.setter
    def ReadSameParamMode(self, arg: bool, /) -> None: ...

    @property
    def ReadSurfaceCurveMode(self) -> DESTEP_Parameters.ReadMode_SurfaceCurve: ...

    @ReadSurfaceCurveMode.setter
    def ReadSurfaceCurveMode(self, arg: DESTEP_Parameters.ReadMode_SurfaceCurve, /) -> None: ...

    @property
    def EncodeRegAngle(self) -> float: ...

    @EncodeRegAngle.setter
    def EncodeRegAngle(self, arg: float, /) -> None: ...

    @property
    def AngleUnit(self) -> DESTEP_Parameters.AngleUnitMode: ...

    @AngleUnit.setter
    def AngleUnit(self, arg: DESTEP_Parameters.AngleUnitMode, /) -> None: ...

    @property
    def ReadProductMode(self) -> bool: ...

    @ReadProductMode.setter
    def ReadProductMode(self, arg: bool, /) -> None: ...

    @property
    def ReadProductContext(self) -> DESTEP_Parameters.ReadMode_ProductContext: ...

    @ReadProductContext.setter
    def ReadProductContext(self, arg: DESTEP_Parameters.ReadMode_ProductContext, /) -> None: ...

    @property
    def ReadShapeRepr(self) -> DESTEP_Parameters.ReadMode_ShapeRepr: ...

    @ReadShapeRepr.setter
    def ReadShapeRepr(self, arg: DESTEP_Parameters.ReadMode_ShapeRepr, /) -> None: ...

    @property
    def ReadTessellated(self) -> DESTEP_Parameters.RWMode_Tessellated:
        """Defines whether tessellated shapes should be translated"""

    @ReadTessellated.setter
    def ReadTessellated(self, arg: DESTEP_Parameters.RWMode_Tessellated, /) -> None: ...

    @property
    def ReadAssemblyLevel(self) -> DESTEP_Parameters.ReadMode_AssemblyLevel: ...

    @ReadAssemblyLevel.setter
    def ReadAssemblyLevel(self, arg: DESTEP_Parameters.ReadMode_AssemblyLevel, /) -> None: ...

    @property
    def ReadRelationship(self) -> bool: ...

    @ReadRelationship.setter
    def ReadRelationship(self, arg: bool, /) -> None: ...

    @property
    def ReadShapeAspect(self) -> bool: ...

    @ReadShapeAspect.setter
    def ReadShapeAspect(self, arg: bool, /) -> None: ...

    @property
    def ReadConstrRelation(self) -> bool: ...

    @ReadConstrRelation.setter
    def ReadConstrRelation(self, arg: bool, /) -> None: ...

    @property
    def ReadSubshapeNames(self) -> bool: ...

    @ReadSubshapeNames.setter
    def ReadSubshapeNames(self, arg: bool, /) -> None: ...

    @property
    def ReadCodePage(self) -> nanoocp.Resource.Resource_FormatType: ...

    @ReadCodePage.setter
    def ReadCodePage(self, arg: nanoocp.Resource.Resource_FormatType, /) -> None: ...

    @property
    def ReadNonmanifold(self) -> bool: ...

    @ReadNonmanifold.setter
    def ReadNonmanifold(self, arg: bool, /) -> None: ...

    @property
    def ReadIdeas(self) -> bool: ...

    @ReadIdeas.setter
    def ReadIdeas(self, arg: bool, /) -> None: ...

    @property
    def ReadAllShapes(self) -> bool: ...

    @ReadAllShapes.setter
    def ReadAllShapes(self, arg: bool, /) -> None: ...

    @property
    def ReadRootTransformation(self) -> bool:
        """
        <!/ Mode to variate apply or not transformation placed in the root shape representation
        """

    @ReadRootTransformation.setter
    def ReadRootTransformation(self, arg: bool, /) -> None: ...

    @property
    def ReadColor(self) -> bool: ...

    @ReadColor.setter
    def ReadColor(self, arg: bool, /) -> None: ...

    @property
    def ReadName(self) -> bool: ...

    @ReadName.setter
    def ReadName(self, arg: bool, /) -> None: ...

    @property
    def ReadLayer(self) -> bool: ...

    @ReadLayer.setter
    def ReadLayer(self, arg: bool, /) -> None: ...

    @property
    def ReadProps(self) -> bool: ...

    @ReadProps.setter
    def ReadProps(self, arg: bool, /) -> None: ...

    @property
    def ReadMetadata(self) -> bool: ...

    @ReadMetadata.setter
    def ReadMetadata(self, arg: bool, /) -> None: ...

    @property
    def ReadProductMetadata(self) -> bool:
        """Parameter for metadata reading"""

    @ReadProductMetadata.setter
    def ReadProductMetadata(self, arg: bool, /) -> None: ...

    @property
    def WritePrecisionMode(self) -> DESTEP_Parameters.WriteMode_PrecisionMode:
        """Parameter for product metadata reading"""

    @WritePrecisionMode.setter
    def WritePrecisionMode(self, arg: DESTEP_Parameters.WriteMode_PrecisionMode, /) -> None: ...

    @property
    def WritePrecisionVal(self) -> float: ...

    @WritePrecisionVal.setter
    def WritePrecisionVal(self, arg: float, /) -> None: ...

    @property
    def WriteAssembly(self) -> DESTEP_Parameters.WriteMode_Assembly: ...

    @WriteAssembly.setter
    def WriteAssembly(self, arg: DESTEP_Parameters.WriteMode_Assembly, /) -> None: ...

    @property
    def WriteSchema(self) -> DESTEP_Parameters.WriteMode_StepSchema: ...

    @WriteSchema.setter
    def WriteSchema(self, arg: DESTEP_Parameters.WriteMode_StepSchema, /) -> None: ...

    @property
    def WriteTessellated(self) -> DESTEP_Parameters.RWMode_Tessellated:
        """Defines whether tessellated shapes should be translated"""

    @WriteTessellated.setter
    def WriteTessellated(self, arg: DESTEP_Parameters.RWMode_Tessellated, /) -> None: ...

    @property
    def WriteProductName(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @WriteProductName.setter
    def WriteProductName(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def WriteSurfaceCurMode(self) -> bool: ...

    @WriteSurfaceCurMode.setter
    def WriteSurfaceCurMode(self, arg: bool, /) -> None: ...

    @property
    def WriteUnit(self) -> nanoocp.UnitsMethods.UnitsMethods_LengthUnit: ...

    @WriteUnit.setter
    def WriteUnit(self, arg: nanoocp.UnitsMethods.UnitsMethods_LengthUnit, /) -> None: ...

    @property
    def WriteVertexMode(self) -> DESTEP_Parameters.WriteMode_VertexMode: ...

    @WriteVertexMode.setter
    def WriteVertexMode(self, arg: DESTEP_Parameters.WriteMode_VertexMode, /) -> None: ...

    @property
    def WriteSubshapeNames(self) -> bool: ...

    @WriteSubshapeNames.setter
    def WriteSubshapeNames(self, arg: bool, /) -> None: ...

    @property
    def WriteColor(self) -> bool: ...

    @WriteColor.setter
    def WriteColor(self, arg: bool, /) -> None: ...

    @property
    def WriteNonmanifold(self) -> bool: ...

    @WriteNonmanifold.setter
    def WriteNonmanifold(self, arg: bool, /) -> None: ...

    @property
    def WriteName(self) -> bool: ...

    @WriteName.setter
    def WriteName(self, arg: bool, /) -> None: ...

    @property
    def WriteLayer(self) -> bool: ...

    @WriteLayer.setter
    def WriteLayer(self, arg: bool, /) -> None: ...

    @property
    def WriteProps(self) -> bool: ...

    @WriteProps.setter
    def WriteProps(self, arg: bool, /) -> None: ...

    @property
    def WriteMetadata(self) -> bool: ...

    @WriteMetadata.setter
    def WriteMetadata(self, arg: bool, /) -> None: ...

    @property
    def WriteMaterial(self) -> bool: ...

    @WriteMaterial.setter
    def WriteMaterial(self, arg: bool, /) -> None: ...

    @property
    def WriteVisMaterial(self) -> bool: ...

    @WriteVisMaterial.setter
    def WriteVisMaterial(self, arg: bool, /) -> None: ...

    @property
    def WriteModelType(self) -> nanoocp.STEPControl.STEPControl_StepModelType: ...

    @WriteModelType.setter
    def WriteModelType(self, arg: nanoocp.STEPControl.STEPControl_StepModelType, /) -> None: ...

    @property
    def CleanDuplicates(self) -> bool: ...

    @CleanDuplicates.setter
    def CleanDuplicates(self, arg: bool, /) -> None: ...

    @property
    def WriteScalingTrsf(self) -> bool: ...

    @WriteScalingTrsf.setter
    def WriteScalingTrsf(self, arg: bool, /) -> None: ...

class DESTEP_ConfigurationNode(nanoocp.DE.DE_ShapeFixConfigurationNode):
    """
    The purpose of this class is to configure the transfer process for STEP format
    Stores the necessary settings for DESTEP_Provider.
    Configures and creates special provider to transfer STEP files.

    Nodes grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "STEP"
    The supported CAD extensions are ".stp", ".step", ".stpz"
    The import process is supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """Initializes all field by default"""

    @overload
    def __init__(self, theNode: DESTEP_ConfigurationNode | None) -> None:
        """
        Copies values of all fields
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DESTEP_ConfigurationNode) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Load(self, theResource: nanoocp.DE.DE_ConfigurationContext | None) -> bool:
        """
        Updates values according the resource
        @param[in] theResource input resource to use
        @return true if theResource loading has ended correctly
        """

    def Save(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Writes configuration to the string
        @return result resource string
        """

    def Copy(self) -> nanoocp.DE.DE_ConfigurationNode:
        """
        Copies values of all fields
        @return new object with the same field values
        """

    def BuildProvider(self) -> nanoocp.DE.DE_Provider:
        """
        Creates new provider for the own format
        @return new created provider
        """

    def IsImportSupported(self) -> bool:
        """
        Checks the import supporting
        @return true if import is supported
        """

    def IsExportSupported(self) -> bool:
        """
        Checks the export supporting
        @return true if export is supported
        """

    def IsStreamSupported(self) -> bool:
        """
        Checks for stream support.
        @return true if streams are supported
        """

    def GetFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gets CAD format name of associated provider
        @return provider CAD format
        """

    def GetVendor(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gets provider's vendor name of associated provider
        @return provider's vendor name
        """

    def GetExtensions(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Gets list of supported file extensions
        @return list of extensions
        """

    def CheckContent(self, theBuffer: nanoocp.NCollection.NCollection_Buffer | None) -> bool:
        """
        Checks the file content to verify a format
        @param[in] theBuffer read stream buffer to check content
        @return true if file is supported by a current provider
        """

    @property
    def InternalParameters(self) -> DESTEP_Parameters: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: DESTEP_Parameters, /) -> None: ...

class DESTEP_Provider(nanoocp.DE.DE_Provider):
    """
    The class to transfer STEP files.
    Reads and Writes any STEP files into/from OCCT.
    Each operation needs configuration node.

    Providers grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "STEP"
    The import process is supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor
        Configure translation process with global configuration
        """

    @overload
    def __init__(self, theNode: nanoocp.DE.DE_ConfigurationNode | None) -> None:
        """
        Configure translation process
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DESTEP_Provider) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theDocument document to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theDocument document to save result
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theShape shape to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theDocument document to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theShape shape to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theShape shape to save result
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theDocument document to save result
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theShape shape to save result
        @param[in] theProgress progress indicator
        @return true if Read operation has ended correctly
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theDocument document to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theDocument document to export
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theShape shape to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theDocument document to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: nanoocp.XSControl.XSControl_WorkSession | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, nanoocp.XSControl.XSControl_WorkSession]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theShape shape to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theShape shape to export
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theDocument document to export
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theShape shape to export
        @param[in] theProgress progress indicator
        @return true if Write operation has ended correctly
        """

    def GetFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gets CAD format name of associated provider
        @return provider CAD format
        """

    def GetVendor(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gets provider's vendor name of associated provider
        @return provider's vendor name
        """
