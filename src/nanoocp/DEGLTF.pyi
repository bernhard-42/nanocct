"""OCCT package DEGLTF (toolkit TKDEGLTF)"""

from typing import overload

import nanoocp.DE
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.RWGltf
import nanoocp.RWMesh
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XSControl


class DEGLTF_ConfigurationNode(nanoocp.DE.DE_ConfigurationNode):
    """
    The purpose of this class is to configure the transfer process for glTF format
    Stores the necessary settings for DEGLTF_Provider.
    Configures and creates special provider to transfer glTF files.

    Nodes grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "GLTF"
    The supported CAD extensions are ".gltf", ".glb"
    The import process is supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """Initializes all field by default"""

    @overload
    def __init__(self, theNode: DEGLTF_ConfigurationNode | None) -> None:
        """
        Copies values of all fields
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DEGLTF_ConfigurationNode) -> None: ...

    class RWGltf_InternalSection:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: DEGLTF_ConfigurationNode.RWGltf_InternalSection) -> None: ...

        @property
        def FileLengthUnit(self) -> float:
            """
            File length units to convert from while reading the file, defined as scale factor for m (meters)
            """

        @FileLengthUnit.setter
        def FileLengthUnit(self, arg: float, /) -> None: ...

        @property
        def SystemCS(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystem:
            """System origin coordinate system to perform conversion into during read"""

        @SystemCS.setter
        def SystemCS(self, arg: nanoocp.RWMesh.RWMesh_CoordinateSystem, /) -> None: ...

        @property
        def FileCS(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystem:
            """File origin coordinate system to perform conversion during read"""

        @FileCS.setter
        def FileCS(self, arg: nanoocp.RWMesh.RWMesh_CoordinateSystem, /) -> None: ...

        @property
        def ReadSinglePrecision(self) -> bool:
            """
            Flag for reading vertex data with single or double floating point precision
            """

        @ReadSinglePrecision.setter
        def ReadSinglePrecision(self, arg: bool, /) -> None: ...

        @property
        def ReadCreateShapes(self) -> bool:
            """Flag for create a single triangulation"""

        @ReadCreateShapes.setter
        def ReadCreateShapes(self, arg: bool, /) -> None: ...

        @property
        def ReadRootPrefix(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Root folder for generating root labels names"""

        @ReadRootPrefix.setter
        def ReadRootPrefix(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def ReadFillDoc(self) -> bool:
            """Flag for fill document from shape sequence"""

        @ReadFillDoc.setter
        def ReadFillDoc(self, arg: bool, /) -> None: ...

        @property
        def ReadFillIncomplete(self) -> bool:
            """
            Flag for fill the document with partially retrieved data even if reader has failed with error
            """

        @ReadFillIncomplete.setter
        def ReadFillIncomplete(self, arg: bool, /) -> None: ...

        @property
        def ReadMemoryLimitMiB(self) -> int:
            """Memory usage limit"""

        @ReadMemoryLimitMiB.setter
        def ReadMemoryLimitMiB(self, arg: int, /) -> None: ...

        @property
        def ReadParallel(self) -> bool:
            """Flag to use multithreading"""

        @ReadParallel.setter
        def ReadParallel(self, arg: bool, /) -> None: ...

        @property
        def ReadSkipEmptyNodes(self) -> bool:
            """Flag to ignore nodes without Geometry"""

        @ReadSkipEmptyNodes.setter
        def ReadSkipEmptyNodes(self, arg: bool, /) -> None: ...

        @property
        def ReadLoadAllScenes(self) -> bool:
            """Flag to load all scenes in the document"""

        @ReadLoadAllScenes.setter
        def ReadLoadAllScenes(self, arg: bool, /) -> None: ...

        @property
        def ReadUseMeshNameAsFallback(self) -> bool:
            """Flag to use Mesh name in case if Node name is empty"""

        @ReadUseMeshNameAsFallback.setter
        def ReadUseMeshNameAsFallback(self, arg: bool, /) -> None: ...

        @property
        def ReadSkipLateDataLoading(self) -> bool:
            """Flag to skip triangulation loading"""

        @ReadSkipLateDataLoading.setter
        def ReadSkipLateDataLoading(self, arg: bool, /) -> None: ...

        @property
        def ReadKeepLateData(self) -> bool:
            """
            Flag to keep information about deferred storage to load/unload triangulation later
            """

        @ReadKeepLateData.setter
        def ReadKeepLateData(self, arg: bool, /) -> None: ...

        @property
        def ReadPrintDebugMessages(self) -> bool:
            """Flag to print additional debug information"""

        @ReadPrintDebugMessages.setter
        def ReadPrintDebugMessages(self, arg: bool, /) -> None: ...

        @property
        def ReadApplyScale(self) -> bool:
            """
            Flag to apply non-uniform scale factor to the triangulations (modify nodes coordinates)
            """

        @ReadApplyScale.setter
        def ReadApplyScale(self, arg: bool, /) -> None: ...

        @property
        def WriteComment(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Export special comment"""

        @WriteComment.setter
        def WriteComment(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def WriteAuthor(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """Author of exported file name"""

        @WriteAuthor.setter
        def WriteAuthor(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def WriteTrsfFormat(self) -> nanoocp.RWGltf.RWGltf_WriterTrsfFormat:
            """Transformation format to write into glTF file"""

        @WriteTrsfFormat.setter
        def WriteTrsfFormat(self, arg: nanoocp.RWGltf.RWGltf_WriterTrsfFormat, /) -> None: ...

        @property
        def WriteNodeNameFormat(self) -> nanoocp.RWMesh.RWMesh_NameFormat:
            """Name format for exporting Nodes"""

        @WriteNodeNameFormat.setter
        def WriteNodeNameFormat(self, arg: nanoocp.RWMesh.RWMesh_NameFormat, /) -> None: ...

        @property
        def WriteMeshNameFormat(self) -> nanoocp.RWMesh.RWMesh_NameFormat:
            """Name format for exporting Meshes"""

        @WriteMeshNameFormat.setter
        def WriteMeshNameFormat(self, arg: nanoocp.RWMesh.RWMesh_NameFormat, /) -> None: ...

        @property
        def WriteForcedUVExport(self) -> bool:
            """Export UV coordinates even if there are no mapped texture"""

        @WriteForcedUVExport.setter
        def WriteForcedUVExport(self, arg: bool, /) -> None: ...

        @property
        def WriteEmbedTexturesInGlb(self) -> bool:
            """Flag to write image textures into GLB file"""

        @WriteEmbedTexturesInGlb.setter
        def WriteEmbedTexturesInGlb(self, arg: bool, /) -> None: ...

        @property
        def WriteMergeFaces(self) -> bool:
            """Flag to merge faces within a single part"""

        @WriteMergeFaces.setter
        def WriteMergeFaces(self, arg: bool, /) -> None: ...

        @property
        def WriteSplitIndices16(self) -> bool:
            """Flag to prefer keeping 16-bit indexes while merging face"""

        @WriteSplitIndices16.setter
        def WriteSplitIndices16(self, arg: bool, /) -> None: ...

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

    @property
    def InternalParameters(self) -> DEGLTF_ConfigurationNode.RWGltf_InternalSection: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: DEGLTF_ConfigurationNode.RWGltf_InternalSection, /) -> None: ...

class DEGLTF_Provider(nanoocp.DE.DE_Provider):
    """
    The class to transfer glTF files.
    Reads and Writes any glTF files into/from OCCT.
    Each operation needs configuration node.

    Providers grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "GLTF"
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
    def __init__(self, theOther: DEGLTF_Provider) -> None: ...

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
