"""OCCT package DE (toolkit TKDE)"""

import enum
from typing import BinaryIO, overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.DE


class DE_ConfigurationContext(nanoocp.Standard.Standard_Transient):
    """
    Provides convenient interface to resource file
    Allows loading of the resource file and getting attributes'
    values starting from some scope, for example
    if scope is defined as "ToV4" and requested parameter
    is "exec.op", value of "ToV4.exec.op" parameter from
    the resource file will be returned
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, theOther: DE_ConfigurationContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Load(self, theConfiguration: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Import the custom configuration
        Save all parameters with their values.
        @param[in] theConfiguration path to configuration file or string value
        @return true in case of success, false otherwise
        """

    def LoadFile(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Import the resource file.
        Save all parameters with their values.
        @param[in] theFile path to the resource file
        @return true in case of success, false otherwise
        """

    def LoadStr(self, theResource: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Import the resource string.
        Save all parameters with their values.
        @param[in] theResource string with resource content
        @return true in case of success, false otherwise
        """

    def IsParamSet(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """
        Checks for existing the parameter name
        @param[in] theParam complex parameter name
        @param[in] theScope base parameter name
        @return true if parameter is defined in the resource file
        """

    def GetReal(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> tuple[bool, float]:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[out] theValue value to get by parameter
        @param[in] theScope base parameter name
        @return false if parameter is not defined or has a wrong type
        """

    def GetInteger(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> tuple[bool, int]:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[out] theValue value to get by parameter
        @param[in] theScope base parameter name
        @return false if parameter is not defined or has a wrong type
        """

    def GetBoolean(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> tuple[bool, bool]:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[out] theValue value to get by parameter
        @param[in] theScope base parameter name
        @return false if parameter is not defined or has a wrong type
        """

    def GetString(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[out] theValue value to get by parameter
        @param[in] theScope base parameter name
        @return false if parameter is not defined or has a wrong type
        """

    def GetStringSeq(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString], theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[out] theValue value to get by parameter
        @param[in] theScope base parameter name
        @return false if parameter is not defined or has a wrong type
        """

    def RealVal(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theDefValue: float, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> float:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[in] theDefValue value by default if param is not found or has wrong type
        @param[in] theScope base parameter name
        @return specific type value
        """

    def IntegerVal(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theDefValue: int, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> int:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[in] theDefValue value by default if param is not found or has wrong type
        @param[in] theScope base parameter name
        @return specific type value
        """

    def BooleanVal(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theDefValue: bool, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[in] theDefValue value by default if param is not found or has wrong type
        @param[in] theScope base parameter name
        @return specific type value
        """

    def StringVal(self, theParam: nanoocp.TCollection.TCollection_AsciiString, theDefValue: nanoocp.TCollection.TCollection_AsciiString, theScope: nanoocp.TCollection.TCollection_AsciiString = ...) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gets value of parameter as being of specific type
        @param[in] theParam complex parameter name
        @param[in] theDefValue value by default if param is not found or has wrong type
        @param[in] theScope base parameter name
        @return specific type value
        """

    def GetInternalMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Gets internal resource map
        @return map with resource value
        """

class DE_ConfigurationNode(nanoocp.Standard.Standard_Transient):
    """
    Base class to work with CAD transfer properties.
    Stores the necessary settings for a single Provider type.
    Configures and creates special provider to transfer CAD files.

    Nodes are grouped by Vendor's name and Format type.
    The Vendor name is not defined by default.
    The Format type is not defined by default.
    The supported CAD extensions are not defined by default.
    The import process is not supported.
    The export process is not supported.

    The algorithm for standalone transfer operation:
    1) Create new empty Node object
    2) Configure the current Node
    2.1) Use the external resource file to configure (::Load)
    2.2) Change the internal parameters directly:
    2.2.1) Change field values of "GlobalParameters"
    2.2.2) Change field values of "InternalParameters"
    3) Create one-time transfer provider (::BuildProvider)
    4) Initiate the transfer process:
    4.1) Import (if "::IsImportSupported: returns TRUE)
    4.1.1) Validate the support of input format (::CheckContent or ::CheckExtension)
    4.1.2) Use created provider's "::Read" method
    4.2) Export (if "::IsExportSupported: returns TRUE)
    4.2.1) Use created provider's "::Write" method
    5) Check the provider's output
    """

    class DE_SectionGlobal:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: DE_ConfigurationNode.DE_SectionGlobal) -> None: ...

        @property
        def LengthUnit(self) -> float:
            """
            Target Unit (scaling based on MM) for the transfer process, default 1.0 (MM)
            """

        @LengthUnit.setter
        def LengthUnit(self, arg: float, /) -> None: ...

        @property
        def SystemUnit(self) -> float:
            """
            System Unit (scaling based on MM) to be used when initial
            unit is unknown, default 1.0 (MM)
            """

        @SystemUnit.setter
        def SystemUnit(self, arg: float, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Load(self, theResourcePath: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """
        Updates values according the resource file
        @param[in] theResourcePath file path to resource
        @return True if Load was successful
        """

    @overload
    def Load(self, theResource: DE_ConfigurationContext | None) -> bool:
        """
        Updates values according the resource
        @param[in] theResource input resource to use
        @return True if Load was successful
        """

    @overload
    def Save(self, theResourcePath: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Writes configuration to the resource file
        @param[in] theResourcePath file path to resource
        @return True if Save was successful
        """

    @overload
    def Save(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Writes configuration to the string
        @return result resource string
        """

    def BuildProvider(self) -> DE_Provider:
        """
        Creates new provider for the own format
        @return new created provider
        """

    def Copy(self) -> DE_ConfigurationNode:
        """
        Copies values of all fields
        @return new object with the same field values
        """

    def UpdateLoad(self, theToImport: bool, theToKeep: bool) -> bool:
        """
        Update loading status. Checking for the ability to read and write.
        @param[in] theToImport flag to updates for import. true-import, false-export
        @param[in] theToKeep flag to save update result
        @return true, if node can be used
        """

    def IsImportSupported(self) -> bool:
        """
        Checks for import support.
        @return true if import is supported
        """

    def IsExportSupported(self) -> bool:
        """
        Checks for export support.
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

    def CheckExtension(self, theExtension: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Checks the file extension to verify a format
        @param[in] theExtension input file extension
        @return true if file is supported by a current provider
        """

    def CheckContent(self, theBuffer: nanoocp.NCollection.NCollection_Buffer | None) -> bool:
        """
        Checks the file content to verify a format
        @param[in] theBuffer read stream buffer to check content
        @return true if file is supported by a current provider
        """

    def IsEnabled(self) -> bool:
        """
        Gets the provider loading status
        @return true if the load is correct
        """

    def SetEnabled(self, theIsLoaded: bool) -> None:
        """
        Sets the provider loading status
        @param[in] theIsLoaded input load status
        """

    def CustomActivation(self, arg0: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Custom function to activate commercial DE component.
        The input is special sequence of values that described in
        specific component documentation. Order is important.
        Each component can have own way of activation.

        The main goal - real-time loading plug-in activation.
        OpenSource components don't need to have activation process.
        """

    def Register(self, theWrapper: DE_Wrapper | None) -> None:
        """
        Registers configuration node with the specified wrapper
        @param[in] theWrapper wrapper to register with
        """

    def UnRegister(self, theWrapper: DE_Wrapper | None) -> None:
        """
        Unregisters configuration node from the specified wrapper
        @param[in] theWrapper wrapper to unregister from
        """

    @property
    def GlobalParameters(self) -> DE_ConfigurationNode.DE_SectionGlobal: ...

    @GlobalParameters.setter
    def GlobalParameters(self, arg: DE_ConfigurationNode.DE_SectionGlobal, /) -> None: ...

class DE_Provider(nanoocp.Standard.Standard_Transient):
    """
    Base class to make transfer process.
    Reads or Writes specialized CAD files into/from OCCT.
    Each operation needs the Configuration Node.

    Providers are grouped by Vendor's name and Format type.
    The Vendor name is not defined by default.
    The Format type is not defined by default.
    The import process is not supported.
    The export process is not supported.

    The algorithm for standalone transfer operation:
    1) Create new empty Provider object
    2) Configure the current object by special Configuration Node (::SetNode)
    3) Initiate the transfer process:
    3.1) Call the required Read method (if Read methods are implemented)
    3.2) Call the required Write method (if Write methods are implemented)
    4) Validate the output values
    """

    class WriteStreamNode:
        """
        Node to store write stream information
        Contains relative path and reference to output stream
        """

        def __init__(self, theOther: DE_Provider.WriteStreamNode) -> None: ...

        @property
        def Path(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Relative path to the output file"""

        @Path.setter
        def Path(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    class ReadStreamNode:
        """
        Node to store read stream information
        Contains relative path and reference to input stream
        """

        def __init__(self, theOther: DE_Provider.ReadStreamNode) -> None: ...

        @property
        def Path(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Relative path to the input file"""

        @Path.setter
        def Path(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theDocument document to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theDocument document to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theDocument document to save result
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theDocument document to save result
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theShape shape to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theShape shape to save result
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads a CAD file, according internal configuration
        @param[in] thePath path to the import CAD file
        @param[out] theShape shape to save result
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theShape shape to save result
        @param[in] theProgress progress indicator
        @return True if Read was successful
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theDocument document to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theDocument document to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theDocument document to export
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theDocument document to export
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theShape shape to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theShape shape to export
        @param[in] theWS current work session
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes a CAD file, according internal configuration
        @param[in] thePath path to the export CAD file
        @param[out] theShape shape to export
        @param[in] theProgress progress indicator
        @return True if Write was successful
        """

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theShape shape to export
        @param[in] theProgress progress indicator
        @return True if Write was successful
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

    def GetNode(self) -> DE_ConfigurationNode:
        """
        Gets internal configuration node
        @return configuration node object
        """

    def SetNode(self, theNode: DE_ConfigurationNode | None) -> None:
        """
        Sets internal configuration node
        @param[in] theNode configuration node to set
        """

class DE_Wrapper(nanoocp.Standard.Standard_Transient):
    """
    The main class for working with CAD file exchange.
    Loads and Saves special CAD transfer property.
    Consolidates all supported Formats and Vendors.
    Automatically recognizes CAD format and uses the preferred existed Vendor.
    Note:
    If Vendor's format is not binded, the configuration loading doesn't affect on its property.

    Nodes are grouped by Vendor's name and Format's type.
    The Vendors may have the same supported CAD formats.
    Use a Vendor's priority for transfer operations.

    The algorithm for standalone transfer operation:
    1) Work with global wrapper directly or make deep copy and work with it
    2) Update the supported vendors and formats
    2.1) Create and initialize specialized configuration node of the required format and Vendor.
    2.2) Bind the created node to the internal map(::Bind)
    3) Configure the transfer property by resource string or file (::Load)
    3.1) Configuration can disable or enable some Vendors and formats
    3.2) Configuration can change the priority of Vendors
    4) Initiate the transfer process by calling "::Write" or "::Read" methods
    5) Validate the transfer process output
    """

    @overload
    def __init__(self) -> None:
        """Initializes all field by default"""

    @overload
    def __init__(self, theWrapper: DE_Wrapper | None) -> None:
        """
        Copies values of all fields
        @param[in] theWrapper object to copy
        """

    @overload
    def __init__(self, theOther: DE_Wrapper) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GlobalWrapper() -> DE_Wrapper:
        """
        Gets global configuration singleton.
        If wrapper is not set, create it by default as base class object.
        @return point to global configuration
        """

    @staticmethod
    def SetGlobalWrapper(theWrapper: DE_Wrapper | None) -> None:
        """
        Sets global configuration singleton
        @param[in] theWrapper object to set as global configuration
        """

    @overload
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
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
    def Read(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
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
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theDocument document to save result
        @param[in] theWS current work session
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
    def Read(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Reads streams according to internal configuration
        @param[in] theStreams streams to read from
        @param[out] theShape shape to save result
        @param[in] theWS current work session
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
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
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
    def Write(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
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

    @overload
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theDocument: nanoocp.TDocStd.TDocStd_Document | None, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theDocument document to export
        @param[in] theWS current work session
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
    def Write(self, theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theShape: nanoocp.TopoDS.TopoDS_Shape, theWS: "XSControl_WorkSession" | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, "XSControl_WorkSession"]:
        """
        Writes streams according to internal configuration
        @param[in] theStreams streams to write to
        @param[out] theShape shape to export
        @param[in] theWS current work session
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

    @overload
    def Load(self, theResource: nanoocp.TCollection.TCollection_AsciiString = ..., theIsRecursive: bool = True) -> bool:
        """
        Updates values according the resource file
        @param[in] theResource file path to resource or resource value
        @param[in] theIsRecursive flag to update all nodes
        @return true if theResource has loaded correctly
        """

    @overload
    def Load(self, theResource: DE_ConfigurationContext | None, theIsRecursive: bool = True) -> bool:
        """
        Updates values according the resource
        @param[in] theResource input resource to use
        @param[in] theIsRecursive flag to update all nodes
        @return true if theResource has loaded correctly
        """

    @overload
    def Save(self, theResourcePath: nanoocp.TCollection.TCollection_AsciiString, theIsRecursive: bool = True, theFormats: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString] = ..., theVendors: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString] = ...) -> bool:
        """
        Writes configuration to the resource file
        @param[in] theResourcePath file path to resource
        @param[in] theIsRecursive flag to write values of all nodes
        @param[in] theFormats list of formats to save. If empty, saves all available
        @param[in] theVendors list of providers to save. If empty, saves all available
        @return true if the Configuration has saved correctly
        """

    @overload
    def Save(self, theIsRecursive: bool = True, theFormats: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString] = ..., theVendors: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString] = ...) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Writes configuration to the string
        @param[in] theIsRecursive flag to write values of all nodes
        @param[in] theFormats list of formats to save. If empty, saves all available
        @param[in] theVendors list of providers to save. If empty, saves all available
        @return result resource string
        """

    def Bind(self, theNode: DE_ConfigurationNode | None) -> bool:
        """
        Creates new node copy and adds to the map
        @param[in] theNode input node to copy
        @return true if binded
        """

    def UnBind(self, theNode: DE_ConfigurationNode | None) -> bool:
        """
        Removes node with the same type from the map
        @param[in] theNode input node to remove the same
        @return true if removed
        """

    def Find(self, theFormat: nanoocp.TCollection.TCollection_AsciiString, theVendor: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, DE_ConfigurationNode]:
        """
        Finds a node associated with input format and vendor
        @param[in] theFormat input node CAD format
        @param[in] theVendor input node vendor name
        @param[out] theNode output node
        @return true if the node is found
        """

    @overload
    def ChangePriority(self, theFormat: nanoocp.TCollection.TCollection_AsciiString, theVendorPriority: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString], theToDisable: bool = False) -> None:
        """
        Changes provider priority to one format if it exists
        @param[in] theFormat input node CAD format
        @param[in] theVendorPriority priority of work with vendors
        @param[in] theToDisable flag for disabling nodes that are not included in the priority
        """

    @overload
    def ChangePriority(self, theVendorPriority: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString], theToDisable: bool = False) -> None:
        """
        Changes provider priority to all loaded nodes
        @param[in] theVendorPriority priority of work with vendors
        @param[in] theToDisable flag for disabling nodes that are not included in the priority
        """

    def FindProvider(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theToImport: bool) -> tuple[bool, DE_Provider]:
        """
        Find available provider from the configuration.
        If there are several providers, choose the one with the highest priority.
        @param[in] thePath path to the CAD file
        @param[in] theToImport flag to finds for import. true-import, false-export
        @param[out] theProvider created new provider
        @return true if provider found and created
        """

    @overload
    def FindReadProvider(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theCheckContent: bool) -> tuple[bool, DE_Provider]:
        """
        Find available read provider from the configuration for file-based operations.
        If there are several providers, choose the one with the highest priority.
        @param[in] thePath path to the CAD file (for extension and content checking)
        @param[in] theCheckContent flag to enable content checking via file reading
        @param[out] theProvider created new provider
        @return true if provider found and created
        """

    @overload
    def FindReadProvider(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theStream: BinaryIO) -> tuple[bool, DE_Provider]:
        """
        Find available read provider from the configuration for stream-based operations.
        If there are several providers, choose the one with the highest priority.
        @param[in] thePath path to the CAD file (for extension extraction)
        @param[in] theStream input stream for content checking
        @param[out] theProvider created new provider
        @return true if provider found and created
        """

    def FindWriteProvider(self, thePath: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, DE_Provider]:
        """
        Find available write provider from the configuration.
        If there are several providers, choose the one with the highest priority.
        @param[in] thePath path to the CAD file (for extension checking only)
        @param[out] theProvider created new provider
        @return true if provider found and created
        """

    def UpdateLoad(self, theToForceUpdate: bool = False) -> None:
        """
        Updates all registered nodes, all changes will be saved in nodes
        @param[in] theToForceUpdate flag that turns on/of nodes, according to updated ability to
        import/export
        """

    def KeepUpdates(self) -> bool:
        """
        Gets flag that keeps changes on configuration nodes which are being updated, false by default
        """

    def SetKeepUpdates(self, theToKeepUpdates: bool) -> None:
        """
        Sets flag that keeps changes on configuration nodes which are being updated, false by default
        """

    def Nodes(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.DE.DE_ConfigurationNode]]:
        """
        Gets format map, contains vendor map with nodes
        @return internal map of formats
        """

    def Copy(self) -> DE_Wrapper:
        """
        Copies values of all fields
        @return new object with the same field values
        """

    @property
    def GlobalParameters(self) -> DE_ConfigurationNode.DE_SectionGlobal:
        """Internal parameters for the all translators"""

    @GlobalParameters.setter
    def GlobalParameters(self, arg: DE_ConfigurationNode.DE_SectionGlobal, /) -> None: ...

class DE_ShapeFixParameters:
    """Struct for shape healing parameters storage"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DE_ShapeFixParameters) -> None: ...

    class FixMode(enum.Enum):
        """Enum, classifying a type of value for parameters"""

        FixOrNot = -1

        NotFix = 0

        Fix = 1

    @property
    def Tolerance3d(self) -> float: ...

    @Tolerance3d.setter
    def Tolerance3d(self, arg: float, /) -> None: ...

    @property
    def MaxTolerance3d(self) -> float: ...

    @MaxTolerance3d.setter
    def MaxTolerance3d(self, arg: float, /) -> None: ...

    @property
    def MinTolerance3d(self) -> float: ...

    @MinTolerance3d.setter
    def MinTolerance3d(self, arg: float, /) -> None: ...

    @property
    def DetalizationLevel(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    @DetalizationLevel.setter
    def DetalizationLevel(self, arg: nanoocp.TopAbs.TopAbs_ShapeEnum, /) -> None: ...

    @property
    def NonManifold(self) -> bool: ...

    @NonManifold.setter
    def NonManifold(self, arg: bool, /) -> None: ...

    @property
    def FixFreeShellMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixFreeShellMode.setter
    def FixFreeShellMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixFreeFaceMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixFreeFaceMode.setter
    def FixFreeFaceMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixFreeWireMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixFreeWireMode.setter
    def FixFreeWireMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSameParameterMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSameParameterMode.setter
    def FixSameParameterMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSolidMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSolidMode.setter
    def FixSolidMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixShellOrientationMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixShellOrientationMode.setter
    def FixShellOrientationMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def CreateOpenSolidMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @CreateOpenSolidMode.setter
    def CreateOpenSolidMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixShellMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixShellMode.setter
    def FixShellMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixFaceOrientationMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixFaceOrientationMode.setter
    def FixFaceOrientationMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixFaceMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixFaceMode.setter
    def FixFaceMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixWireMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixWireMode.setter
    def FixWireMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixOrientationMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixOrientationMode.setter
    def FixOrientationMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixAddNaturalBoundMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixAddNaturalBoundMode.setter
    def FixAddNaturalBoundMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixMissingSeamMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixMissingSeamMode.setter
    def FixMissingSeamMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSmallAreaWireMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSmallAreaWireMode.setter
    def FixSmallAreaWireMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def RemoveSmallAreaFaceMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @RemoveSmallAreaFaceMode.setter
    def RemoveSmallAreaFaceMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixIntersectingWiresMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixIntersectingWiresMode.setter
    def FixIntersectingWiresMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixLoopWiresMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixLoopWiresMode.setter
    def FixLoopWiresMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSplitFaceMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSplitFaceMode.setter
    def FixSplitFaceMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def AutoCorrectPrecisionMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @AutoCorrectPrecisionMode.setter
    def AutoCorrectPrecisionMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def ModifyTopologyMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @ModifyTopologyMode.setter
    def ModifyTopologyMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def ModifyGeometryMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @ModifyGeometryMode.setter
    def ModifyGeometryMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def ClosedWireMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @ClosedWireMode.setter
    def ClosedWireMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def PreferencePCurveMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @PreferencePCurveMode.setter
    def PreferencePCurveMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixReorderMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixReorderMode.setter
    def FixReorderMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSmallMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSmallMode.setter
    def FixSmallMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixConnectedMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixConnectedMode.setter
    def FixConnectedMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixEdgeCurvesMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixEdgeCurvesMode.setter
    def FixEdgeCurvesMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixDegeneratedMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixDegeneratedMode.setter
    def FixDegeneratedMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixLackingMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixLackingMode.setter
    def FixLackingMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSelfIntersectionMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSelfIntersectionMode.setter
    def FixSelfIntersectionMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def RemoveLoopMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @RemoveLoopMode.setter
    def RemoveLoopMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixReversed2dMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixReversed2dMode.setter
    def FixReversed2dMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixRemovePCurveMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixRemovePCurveMode.setter
    def FixRemovePCurveMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixRemoveCurve3dMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixRemoveCurve3dMode.setter
    def FixRemoveCurve3dMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixAddPCurveMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixAddPCurveMode.setter
    def FixAddPCurveMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixAddCurve3dMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixAddCurve3dMode.setter
    def FixAddCurve3dMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSeamMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSeamMode.setter
    def FixSeamMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixShiftedMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixShiftedMode.setter
    def FixShiftedMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixEdgeSameParameterMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixEdgeSameParameterMode.setter
    def FixEdgeSameParameterMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixNotchedEdgesMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixNotchedEdgesMode.setter
    def FixNotchedEdgesMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixTailMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixTailMode.setter
    def FixTailMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def MaxTailAngle(self) -> DE_ShapeFixParameters.FixMode: ...

    @MaxTailAngle.setter
    def MaxTailAngle(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def MaxTailWidth(self) -> DE_ShapeFixParameters.FixMode: ...

    @MaxTailWidth.setter
    def MaxTailWidth(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixSelfIntersectingEdgeMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixSelfIntersectingEdgeMode.setter
    def FixSelfIntersectingEdgeMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixIntersectingEdgesMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixIntersectingEdgesMode.setter
    def FixIntersectingEdgesMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixNonAdjacentIntersectingEdgesMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixNonAdjacentIntersectingEdgesMode.setter
    def FixNonAdjacentIntersectingEdgesMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixVertexPositionMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixVertexPositionMode.setter
    def FixVertexPositionMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

    @property
    def FixVertexToleranceMode(self) -> DE_ShapeFixParameters.FixMode: ...

    @FixVertexToleranceMode.setter
    def FixVertexToleranceMode(self, arg: DE_ShapeFixParameters.FixMode, /) -> None: ...

class DE_ShapeFixConfigurationNode(DE_ConfigurationNode):
    """Base class to work with shape healing parameters for child classes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Load(self, theResource: DE_ConfigurationContext | None) -> bool:
        """
        Updates values according the resource
        @param[in] theResource input resource to use
        @return True if Load was successful
        """

    def Save(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Writes configuration to the string
        @return result resource string
        """

    @property
    def ShapeFixParameters(self) -> DE_ShapeFixParameters:
        """Shape healing parameters"""

    @ShapeFixParameters.setter
    def ShapeFixParameters(self, arg: DE_ShapeFixParameters, /) -> None: ...

class DE_ValidationUtils:
    """
    Utility class providing static methods for common validation operations
    used across DataExchange providers. Includes validation for configuration nodes,
    file paths, streams, and other common scenarios with optional verbose error reporting.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: DE_ValidationUtils) -> None: ...

    @staticmethod
    def ValidateConfigurationNode(theNode: DE_ConfigurationNode | None, theExpectedType: nanoocp.Standard.Standard_Type | None, theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Validates that configuration node is not null and matches expected type
        @param[in] theNode configuration node to validate
        @param[in] theExpectedType expected RTTI type
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error messages via Message::SendFail
        @return true if node is valid, false otherwise
        """

    @staticmethod
    def ValidateFileForReading(thePath: nanoocp.TCollection.TCollection_AsciiString, theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Checks if file exists and is readable
        @param[in] thePath file path to check
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error messages via Message::SendFail
        @return true if file exists and is readable, false otherwise
        """

    @staticmethod
    def ValidateFileForWriting(thePath: nanoocp.TCollection.TCollection_AsciiString, theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Checks if file location is writable (file may or may not exist)
        @param[in] thePath file path to check
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error messages via Message::SendFail
        @return true if location is writable, false otherwise
        """

    @staticmethod
    def ValidateReadStreamList(theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.ReadStreamNode], theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Validates read stream list, warns if multiple streams
        @param[in] theStreams read stream list to validate
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error/warning messages
        @return true if stream list is valid, false otherwise
        """

    @staticmethod
    def ValidateWriteStreamList(theStreams: nanoocp.NCollection.NCollection_List[nanoocp.DE.DE_Provider.WriteStreamNode], theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Validates write stream list, warns if multiple streams
        @param[in] theStreams write stream list to validate
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error/warning messages
        @return true if stream list is valid, false otherwise
        """

    @staticmethod
    def ValidateDocument(theDocument: nanoocp.TDocStd.TDocStd_Document | None, theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Validates that TDocStd_Document handle is not null
        @param[in] theDocument document to validate
        @param[in] theContext context string for error messages
        @param[in] theIsVerbose if true, sends detailed error messages via Message::SendFail
        @return true if document is not null, false otherwise
        """

    @staticmethod
    def WarnLengthUnitNotSupported(theLengthUnit: float, theContext: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True) -> bool:
        """
        Sends warning when format doesn't support length unit scaling
        @param[in] theLengthUnit length unit value to check
        @param[in] theContext context string for warning messages
        @param[in] theIsVerbose if true, sends warning messages via Message::SendWarning
        @return true always (this is just a warning)
        """

    @overload
    @staticmethod
    def CreateContentBuffer(thePath: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, nanoocp.NCollection.NCollection_Buffer]:
        """
        Creates buffer by reading from file stream for content checking
        @param[in] thePath file path for reading
        @param[out] theBuffer output buffer with file content
        @return true if successful, false otherwise
        """

    @overload
    @staticmethod
    def CreateContentBuffer(theStream: BinaryIO) -> tuple[bool, nanoocp.NCollection.NCollection_Buffer]:
        """
        Creates buffer by reading from input stream for content checking
        @param[in,out] theStream input stream to read from (position will be restored)
        @param[out] theBuffer output buffer with stream content
        @return true if successful, false otherwise
        """
