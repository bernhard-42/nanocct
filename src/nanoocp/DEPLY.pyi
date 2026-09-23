"""OCCT package DEPLY (toolkit TKDEPLY)"""

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


class DEPLY_ConfigurationNode(nanoocp.DE.DE_ConfigurationNode):
    """
    The purpose of this class is to configure the transfer process for PLY format
    Stores the necessary settings for DEPLY_Provider.
    Configures and creates special provider to transfer PLY files.

    Nodes grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "PLY"
    The supported CAD extension is ".ply"
    The import process isn't supported.
    The export process is supported.
    """

    @overload
    def __init__(self) -> None:
        """Initializes all field by default"""

    @overload
    def __init__(self, theNode: DEPLY_ConfigurationNode | None) -> None:
        """
        Copies values of all fields
        @param[in] theNode object to copy
        """

    @overload
    def __init__(self, theOther: DEPLY_ConfigurationNode) -> None: ...

    class RWPly_InternalSection:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: DEPLY_ConfigurationNode.RWPly_InternalSection) -> None: ...

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
        def WriteNormals(self) -> bool:
            """Flag for write normals"""

        @WriteNormals.setter
        def WriteNormals(self, arg: bool, /) -> None: ...

        @property
        def WriteColors(self) -> bool:
            """Flag for write colors"""

        @WriteColors.setter
        def WriteColors(self, arg: bool, /) -> None: ...

        @property
        def WriteTexCoords(self) -> bool:
            """Flag for write UV / texture coordinates"""

        @WriteTexCoords.setter
        def WriteTexCoords(self, arg: bool, /) -> None: ...

        @property
        def WritePartId(self) -> bool:
            """Flag for write part Id as element attribute"""

        @WritePartId.setter
        def WritePartId(self, arg: bool, /) -> None: ...

        @property
        def WriteFaceId(self) -> bool:
            """
            Flag for write face Id as element attribute. Cannot be combined with HasPartId
            """

        @WriteFaceId.setter
        def WriteFaceId(self, arg: bool, /) -> None: ...

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
    def InternalParameters(self) -> DEPLY_ConfigurationNode.RWPly_InternalSection: ...

    @InternalParameters.setter
    def InternalParameters(self, arg: DEPLY_ConfigurationNode.RWPly_InternalSection, /) -> None: ...

class DEPLY_Provider(nanoocp.DE.DE_Provider):
    """
    The class to transfer PLY files.
    Writes any PLY files from OCCT.
    Each operation needs configuration node.

    Providers grouped by Vendor name and Format type.
    The Vendor name is "OCC"
    The Format type is "PLY"
    The import process isn't supported.
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
    def __init__(self, theOther: DEPLY_Provider) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

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
