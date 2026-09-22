"""OCCT package DEIGES (toolkit TKDEIGES)"""

import enum
from typing import overload

import nanoocp.DE
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XSControl


class DEIGES_Parameters:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DEIGES_Parameters) -> None: ...

    class ReadMode_BSplineContinuity(enum.IntEnum):
        ReadMode_BSplineContinuity_C0 = 0

        ReadMode_BSplineContinuity_C1 = 1

        ReadMode_BSplineContinuity_C2 = 2

    ReadMode_BSplineContinuity_C0: DEIGES_Parameters.ReadMode_BSplineContinuity = ...

    ReadMode_BSplineContinuity_C1: DEIGES_Parameters.ReadMode_BSplineContinuity = ...

    ReadMode_BSplineContinuity_C2: DEIGES_Parameters.ReadMode_BSplineContinuity = ...

    class ReadMode_Precision(enum.IntEnum):
        ReadMode_Precision_File = 0

        ReadMode_Precision_User = 1

    ReadMode_Precision_File: DEIGES_Parameters.ReadMode_Precision = ReadMode_Precision.ReadMode_Precision_File

    ReadMode_Precision_User: DEIGES_Parameters.ReadMode_Precision = ReadMode_Precision.ReadMode_Precision_User

    class ReadMode_MaxPrecision(enum.IntEnum):
        ReadMode_MaxPrecision_Preferred = 0

        ReadMode_MaxPrecision_Forced = 1

    ReadMode_MaxPrecision_Preferred: DEIGES_Parameters.ReadMode_MaxPrecision = ...

    ReadMode_MaxPrecision_Forced: DEIGES_Parameters.ReadMode_MaxPrecision = ...

    class ReadMode_SurfaceCurve(enum.IntEnum):
        ReadMode_SurfaceCurve_Default = 0

        ReadMode_SurfaceCurve_2DUse_Preferred = 2

        ReadMode_SurfaceCurve_2DUse_Forced = -2

        ReadMode_SurfaceCurve_3DUse_Preferred = 3

        ReadMode_SurfaceCurve_3DUse_Forced = -3

    ReadMode_SurfaceCurve_Default: DEIGES_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_2DUse_Preferred: DEIGES_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_2DUse_Forced: DEIGES_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_3DUse_Preferred: DEIGES_Parameters.ReadMode_SurfaceCurve = ...

    ReadMode_SurfaceCurve_3DUse_Forced: DEIGES_Parameters.ReadMode_SurfaceCurve = ...

    class WriteMode_BRep(enum.IntEnum):
        WriteMode_BRep_Faces = 0

        WriteMode_BRep_BRep = 1

    WriteMode_BRep_Faces: DEIGES_Parameters.WriteMode_BRep = WriteMode_BRep.WriteMode_BRep_Faces

    WriteMode_BRep_BRep: DEIGES_Parameters.WriteMode_BRep = WriteMode_BRep.WriteMode_BRep_BRep

    class WriteMode_ConvertSurface(enum.IntEnum):
        WriteMode_ConvertSurface_Off = 0

        WriteMode_ConvertSurface_On = 1

    WriteMode_ConvertSurface_Off: DEIGES_Parameters.WriteMode_ConvertSurface = ...

    WriteMode_ConvertSurface_On: DEIGES_Parameters.WriteMode_ConvertSurface = ...

    class WriteMode_PrecisionMode(enum.IntEnum):
        WriteMode_PrecisionMode_Least = -1

        WriteMode_PrecisionMode_Average = 0

        WriteMode_PrecisionMode_Greatest = 1

        WriteMode_PrecisionMode_Session = 2

    WriteMode_PrecisionMode_Least: DEIGES_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Average: DEIGES_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Greatest: DEIGES_Parameters.WriteMode_PrecisionMode = ...

    WriteMode_PrecisionMode_Session: DEIGES_Parameters.WriteMode_PrecisionMode = ...

    class WriteMode_PlaneMode(enum.IntEnum):
        WriteMode_PlaneMode_Plane = 0

        WriteMode_PlaneMode_BSpline = 1

    WriteMode_PlaneMode_Plane: DEIGES_Parameters.WriteMode_PlaneMode = WriteMode_PlaneMode.WriteMode_PlaneMode_Plane

    WriteMode_PlaneMode_BSpline: DEIGES_Parameters.WriteMode_PlaneMode = WriteMode_PlaneMode.WriteMode_PlaneMode_BSpline

    def InitFromStatic(self) -> None:
        """Initialize parameters"""

    def Reset(self) -> None:
        """Reset used parameters"""

    @staticmethod
    def GetDefaultShapeFixParameters() -> nanoocp.DE.DE_ShapeFixParameters:
        """Returns default shape fix parameters for transferring IGES files."""

    @property
    def ReadBSplineContinuity(self) -> DEIGES_Parameters.ReadMode_BSplineContinuity: ...

    @ReadBSplineContinuity.setter
    def ReadBSplineContinuity(self, arg: DEIGES_Parameters.ReadMode_BSplineContinuity, /) -> None: ...

    @property
    def ReadPrecisionMode(self) -> DEIGES_Parameters.ReadMode_Precision: ...

    @ReadPrecisionMode.setter
    def ReadPrecisionMode(self, arg: DEIGES_Parameters.ReadMode_Precision, /) -> None: ...

    @property
    def ReadPrecisionVal(self) -> float: ...

    @ReadPrecisionVal.setter
    def ReadPrecisionVal(self, arg: float, /) -> None: ...

    @property
    def ReadMaxPrecisionMode(self) -> DEIGES_Parameters.ReadMode_MaxPrecision: ...

    @ReadMaxPrecisionMode.setter
    def ReadMaxPrecisionMode(self, arg: DEIGES_Parameters.ReadMode_MaxPrecision, /) -> None: ...

    @property
    def ReadMaxPrecisionVal(self) -> float: ...

    @ReadMaxPrecisionVal.setter
    def ReadMaxPrecisionVal(self, arg: float, /) -> None: ...

    @property
    def ReadSameParamMode(self) -> bool: ...

    @ReadSameParamMode.setter
    def ReadSameParamMode(self, arg: bool, /) -> None: ...

    @property
    def ReadSurfaceCurveMode(self) -> DEIGES_Parameters.ReadMode_SurfaceCurve: ...

    @ReadSurfaceCurveMode.setter
    def ReadSurfaceCurveMode(self, arg: DEIGES_Parameters.ReadMode_SurfaceCurve, /) -> None: ...

    @property
    def EncodeRegAngle(self) -> float: ...

    @EncodeRegAngle.setter
    def EncodeRegAngle(self, arg: float, /) -> None: ...

    @property
    def ReadApproxd1(self) -> bool: ...

    @ReadApproxd1.setter
    def ReadApproxd1(self, arg: bool, /) -> None: ...

    @property
    def ReadFaultyEntities(self) -> bool: ...

    @ReadFaultyEntities.setter
    def ReadFaultyEntities(self, arg: bool, /) -> None: ...

    @property
    def ReadOnlyVisible(self) -> bool: ...

    @ReadOnlyVisible.setter
    def ReadOnlyVisible(self, arg: bool, /) -> None: ...

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
    def WriteBRepMode(self) -> DEIGES_Parameters.WriteMode_BRep: ...

    @WriteBRepMode.setter
    def WriteBRepMode(self, arg: DEIGES_Parameters.WriteMode_BRep, /) -> None: ...

    @property
    def WriteConvertSurfaceMode(self) -> DEIGES_Parameters.WriteMode_ConvertSurface: ...

    @WriteConvertSurfaceMode.setter
    def WriteConvertSurfaceMode(self, arg: DEIGES_Parameters.WriteMode_ConvertSurface, /) -> None: ...

    @property
    def WriteHeaderAuthor(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @WriteHeaderAuthor.setter
    def WriteHeaderAuthor(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def WriteHeaderCompany(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @WriteHeaderCompany.setter
    def WriteHeaderCompany(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def WriteHeaderProduct(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @WriteHeaderProduct.setter
    def WriteHeaderProduct(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def WriteHeaderReciever(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @WriteHeaderReciever.setter
    def WriteHeaderReciever(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def WritePrecisionMode(self) -> DEIGES_Parameters.WriteMode_PrecisionMode: ...

    @WritePrecisionMode.setter
    def WritePrecisionMode(self, arg: DEIGES_Parameters.WriteMode_PrecisionMode, /) -> None: ...

    @property
    def WritePrecisionVal(self) -> float: ...

    @WritePrecisionVal.setter
    def WritePrecisionVal(self, arg: float, /) -> None: ...

    @property
    def WritePlaneMode(self) -> DEIGES_Parameters.WriteMode_PlaneMode: ...

    @WritePlaneMode.setter
    def WritePlaneMode(self, arg: DEIGES_Parameters.WriteMode_PlaneMode, /) -> None: ...

    @property
    def WriteOffsetMode(self) -> bool: ...

    @WriteOffsetMode.setter
    def WriteOffsetMode(self, arg: bool, /) -> None: ...

    @property
    def WriteColor(self) -> bool: ...

    @WriteColor.setter
    def WriteColor(self, arg: bool, /) -> None: ...

    @property
    def WriteName(self) -> bool: ...

    @WriteName.setter
    def WriteName(self, arg: bool, /) -> None: ...

    @property
    def WriteLayer(self) -> bool: ...

    @WriteLayer.setter
    def WriteLayer(self, arg: bool, /) -> None: ...

class DEIGES_ConfigurationNode(nanoocp.DE.DE_ShapeFixConfigurationNode):
    """
    The purpose of this class is to configure the transfer process for IGES format
    Stores the necessary settings for DEIGES_Provider.
    Configures and creates special provider to transfer IGES files.

    Nodes grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "IGES"
    The supported CAD extensions are ".igs", ".iges"
    The import process is supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """Initializes all fields by default"""

    @overload
    def __init__(self, theNode: DEIGES_ConfigurationNode | None) -> None:
        """
        Copies values of all fields
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DEIGES_ConfigurationNode) -> None: ...

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
    def InternalParameters(self) -> DEIGES_Parameters: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: DEIGES_Parameters, /) -> None: ...

class DEIGES_Provider(nanoocp.DE.DE_Provider):
    """
    The class to transfer IGES files.
    Reads and Writes any IGES files into/from OCCT.
    Each operation needs configuration node.

    Providers grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "IGES"
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
    def __init__(self, theOther: DEIGES_Provider) -> None: ...

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
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
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
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
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
