"""OCCT package DEVRML (toolkit TKDEVRML)"""

import enum
from typing import overload

import nanoocp.DE
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.RWMesh
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XSControl


class DEVRML_ConfigurationNode(nanoocp.DE.DE_ConfigurationNode):
    """
    The purpose of this class is to configure the transfer process for VRML format
    Stores the necessary settings for DEVRML_Provider.
    Configures and creates special provider to transfer VRML files.

    Nodes grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "VRML"
    The supported CAD extensions are ".vrml", ".wrl"
    The import process is supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """Initializes all field by default"""

    @overload
    def __init__(self, theNode: DEVRML_ConfigurationNode | None) -> None:
        """
        Copies values of all fields
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DEVRML_ConfigurationNode) -> None: ...

    class WriteMode_WriterVersion(enum.IntEnum):
        WriteMode_WriterVersion_1 = 1

        WriteMode_WriterVersion_2 = 2

    WriteMode_WriterVersion_1: DEVRML_ConfigurationNode.WriteMode_WriterVersion = WriteMode_WriterVersion.WriteMode_WriterVersion_1

    WriteMode_WriterVersion_2: DEVRML_ConfigurationNode.WriteMode_WriterVersion = WriteMode_WriterVersion.WriteMode_WriterVersion_2

    class WriteMode_RepresentationType(enum.IntEnum):
        WriteMode_RepresentationType_Shaded = 0

        WriteMode_RepresentationType_Wireframe = 1

        WriteMode_RepresentationType_Both = 2

    WriteMode_RepresentationType_Shaded: DEVRML_ConfigurationNode.WriteMode_RepresentationType = ...

    WriteMode_RepresentationType_Wireframe: DEVRML_ConfigurationNode.WriteMode_RepresentationType = ...

    WriteMode_RepresentationType_Both: DEVRML_ConfigurationNode.WriteMode_RepresentationType = ...

    class Vrml_InternalSection:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: DEVRML_ConfigurationNode.Vrml_InternalSection) -> None: ...

        @property
        def ReadFileUnit(self) -> float: ...

        @ReadFileUnit.setter
        def ReadFileUnit(self, arg: float, /) -> None: ...

        @property
        def ReadFileCoordinateSys(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystem: ...

        @ReadFileCoordinateSys.setter
        def ReadFileCoordinateSys(self, arg: nanoocp.RWMesh.RWMesh_CoordinateSystem, /) -> None: ...

        @property
        def ReadSystemCoordinateSys(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystem: ...

        @ReadSystemCoordinateSys.setter
        def ReadSystemCoordinateSys(self, arg: nanoocp.RWMesh.RWMesh_CoordinateSystem, /) -> None: ...

        @property
        def ReadFillIncomplete(self) -> bool: ...

        @ReadFillIncomplete.setter
        def ReadFillIncomplete(self, arg: bool, /) -> None: ...

        @property
        def WriterVersion(self) -> DEVRML_ConfigurationNode.WriteMode_WriterVersion:
            """Setting up writer version (1/2)"""

        @WriterVersion.setter
        def WriterVersion(self, arg: DEVRML_ConfigurationNode.WriteMode_WriterVersion, /) -> None: ...

        @property
        def WriteRepresentationType(self) -> DEVRML_ConfigurationNode.WriteMode_RepresentationType:
            """Setting up representation (shaded/wireframe/both)"""

        @WriteRepresentationType.setter
        def WriteRepresentationType(self, arg: DEVRML_ConfigurationNode.WriteMode_RepresentationType, /) -> None: ...

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

    @property
    def InternalParameters(self) -> DEVRML_ConfigurationNode.Vrml_InternalSection: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: DEVRML_ConfigurationNode.Vrml_InternalSection, /) -> None: ...

class DEVRML_Provider(nanoocp.DE.DE_Provider):
    """
    The class to transfer VRML files.
    Reads and Writes any VRML files into/from OCCT.
    Each operation needs configuration node.

    Providers grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "VRML"
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
    def __init__(self, theOther: DEVRML_Provider) -> None: ...

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
