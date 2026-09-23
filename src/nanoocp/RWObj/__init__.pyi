"""OCCT package RWObj (toolkit TKDEOBJ)"""

import enum
from typing import BinaryIO, overload

import nanoocp.BVH
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.RWMesh
from nanoocp.RWObj import RWObj_Tools as RWObj_Tools
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XCAFPrs
import nanoocp.TDF


class RWObj_SubMeshReason(enum.IntEnum):
    """Reason for creating a new group within OBJ reader."""

    RWObj_SubMeshReason_NewObject = 0

    RWObj_SubMeshReason_NewGroup = 1

    RWObj_SubMeshReason_NewMaterial = 2

    RWObj_SubMeshReason_NewSmoothGroup = 3

RWObj_SubMeshReason_NewObject: RWObj_SubMeshReason = RWObj_SubMeshReason.RWObj_SubMeshReason_NewObject

RWObj_SubMeshReason_NewGroup: RWObj_SubMeshReason = RWObj_SubMeshReason.RWObj_SubMeshReason_NewGroup

RWObj_SubMeshReason_NewMaterial: RWObj_SubMeshReason = ...

RWObj_SubMeshReason_NewSmoothGroup: RWObj_SubMeshReason = ...

class RWObj:
    """
    This class provides methods to read and write triangulation from / to the OBJ files.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWObj) -> None: ...

    @staticmethod
    def ReadFile(theFile: str, aProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read specified OBJ file and returns its content as triangulation.
        In case of error, returns Null handle.
        """

class RWObj_Material:
    """Material definition for OBJ file format."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWObj_Material) -> None: ...

    @property
    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """material name (identifier) as defined in MTL file"""

    @Name.setter
    def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def DiffuseTexture(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """path to the texture image file defining diffuse color"""

    @DiffuseTexture.setter
    def DiffuseTexture(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def SpecularTexture(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """path to the texture image file defining specular color"""

    @SpecularTexture.setter
    def SpecularTexture(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def BumpTexture(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """path to the texture image file defining normal map"""

    @BumpTexture.setter
    def BumpTexture(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def AmbientColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    @AmbientColor.setter
    def AmbientColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def DiffuseColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    @DiffuseColor.setter
    def DiffuseColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def SpecularColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    @SpecularColor.setter
    def SpecularColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def Shininess(self) -> float: ...

    @Shininess.setter
    def Shininess(self, arg: float, /) -> None: ...

    @property
    def Transparency(self) -> float: ...

    @Transparency.setter
    def Transparency(self, arg: float, /) -> None: ...

class RWObj_SubMesh:
    """Sub-mesh definition for OBJ reader."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWObj_SubMesh) -> None: ...

    @property
    def Object(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name of active object"""

    @Object.setter
    def Object(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Group(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name of active group"""

    @Group.setter
    def Group(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def SmoothGroup(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name of active smoothing group"""

    @SmoothGroup.setter
    def SmoothGroup(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Material(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name of active material"""

    @Material.setter
    def Material(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

class RWObj_Reader(nanoocp.Standard.Standard_Transient):
    """
    An abstract class implementing procedure to read OBJ file.

    This class is not bound to particular data structure
    and can be used to read the file directly into arbitrary data model.
    To use it, create descendant class and implement interface methods.

    Call method Read() to read the file.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Read(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Open stream and pass it to Read method
        Returns true if success, false on error.
        """

    @overload
    def Read(self, theStream: BinaryIO, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Reads data from OBJ file.
        Unicode paths can be given in UTF-8 encoding.
        Returns true if success, false on error or user break.
        """

    @overload
    def Probe(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Open stream and pass it to Probe method.
        @param theFile     path to the file
        @param theProgress progress indicator
        @return TRUE if success, FALSE on error or user break.
        @sa FileComments(), ExternalFiles(), NbProbeNodes(), NbProbeElems().
        """

    @overload
    def Probe(self, theStream: BinaryIO, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Probe data from OBJ file (comments, external references) without actually reading mesh data.
        Although mesh data will not be collected, the full file content will be parsed, due to OBJ
        format limitations.
        @param theStream   input stream
        @param theFile     path to the file
        @param theProgress progress indicator
        @return TRUE if success, FALSE on error or user break.
        @sa FileComments(), ExternalFiles(), NbProbeNodes(), NbProbeElems().
        """

    def FileComments(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns file comments (lines starting with # at the beginning of file).
        """

    def ExternalFiles(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TCollection.TCollection_AsciiString]:
        """Return the list of external file references."""

    def NbProbeNodes(self) -> int:
        """Number of probed nodes."""

    def NbProbeElems(self) -> int: ...

    def MemoryLimit(self) -> int:
        """Returns memory limit in bytes; -1 (no limit) by default."""

    def SetMemoryLimit(self, theMemLimit: int) -> None:
        """
        Specify memory limit in bytes, so that import will be aborted
        by specified limit before memory allocation error occurs.
        """

    def Transformation(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """
        Return transformation from one coordinate system to another; no transformation by default.
        """

    def SetTransformation(self, theCSConverter: nanoocp.RWMesh.RWMesh_CoordinateSystemConverter) -> None:
        """
        Setup transformation from one coordinate system to another.
        OBJ file might be exported following various coordinate system conventions,
        so that it might be useful automatically transform data during file reading.
        """

    def IsSinglePrecision(self) -> bool:
        """
        Return single precision flag for reading vertex data (coordinates); FALSE by default.
        """

    def SetSinglePrecision(self, theIsSinglePrecision: bool) -> None:
        """
        Setup single/double precision flag for reading vertex data (coordinates).
        """

class RWObj_IShapeReceiver:
    """Interface to store shape attributes into document."""

    def BindNamedShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theName: nanoocp.TCollection.TCollection_AsciiString, theMaterial: RWObj_Material, theIsRootShape: bool) -> None:
        """
        @param theShape       shape to register
        @param theName        shape name
        @param theMaterial    shape material
        @param theIsRootShape indicates that this is a root object (free shape)
        """

class RWObj_TriangulationReader(RWObj_Reader):
    """RWObj_Reader implementation dumping OBJ file into Poly_Triangulation."""

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: RWObj_TriangulationReader) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetCreateShapes(self, theToCreateShapes: bool) -> None:
        """Set flag to create shapes."""

    def SetShapeReceiver(self, theReceiver: RWObj_IShapeReceiver) -> None:
        """Set shape receiver callback."""

    def GetTriangulation(self) -> nanoocp.Poly.Poly_Triangulation:
        """Create Poly_Triangulation from collected data"""

    def ResultShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return result shape."""

class RWObj_CafReader(nanoocp.RWMesh.RWMesh_CafReader):
    """The OBJ mesh reader into XDE document."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWObj_CafReader) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsSinglePrecision(self) -> bool:
        """
        Return single precision flag for reading vertex data (coordinates); FALSE by default.
        """

    def SetSinglePrecision(self, theIsSinglePrecision: bool) -> None:
        """
        Setup single/double precision flag for reading vertex data (coordinates).
        """

class RWObj_CafWriter(nanoocp.Standard.Standard_Transient):
    """OBJ writer context from XCAF document."""

    @overload
    def __init__(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Main constructor.
        @param[in] theFile  path to output OBJ file
        """

    @overload
    def __init__(self, theOther: RWObj_CafWriter) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to OBJ coordinate system."""

    def ChangeCoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to OBJ coordinate system."""

    def SetCoordinateSystemConverter(self, theConverter: nanoocp.RWMesh.RWMesh_CoordinateSystemConverter) -> None:
        """Set transformation from OCCT to OBJ coordinate system."""

    def DefaultStyle(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """
        Return default material definition to be used for nodes with only color defined.
        """

    def SetDefaultStyle(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> None:
        """
        Set default material definition to be used for nodes with only color defined.
        """

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRootLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theLabelFilter: nanoocp.NCollection.NCollection_Map[nanoocp.TCollection.TCollection_AsciiString], theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write OBJ file and associated MTL material file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument     input document
        @param[in] theRootLabels   list of root shapes to export
        @param[in] theLabelFilter  optional filter with document nodes to export,
        with keys defined by XCAFPrs_DocumentExplorer::DefineChildId() and
        filled recursively (leaves and parent assembly nodes at all
        levels); when not NULL, all nodes not included into the map will be
        ignored
        @param[in] theFileInfo     map with file metadata to put into OBJ header section
        @param[in] theProgress     optional progress indicator
        @return FALSE on file writing failure
        """

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write OBJ file and associated MTL material file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument     input document
        @param[in] theFileInfo     map with file metadata to put into glTF header section
        @param[in] theProgress     optional progress indicator
        @return FALSE on file writing failure
        """

class RWObj_MtlReader:
    """Reader of mtl files."""

    @overload
    def __init__(self, theMaterials: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.RWObj.RWObj_Material]) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: RWObj_MtlReader) -> None: ...

    def Read(self, theFolder: nanoocp.TCollection.TCollection_AsciiString, theFile: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Read the file."""

class RWObj_ObjMaterialMap(nanoocp.RWMesh.RWMesh_MaterialMap):
    """Material MTL file writer for OBJ export."""

    @overload
    def __init__(self, theFile: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: RWObj_ObjMaterialMap) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AddMaterial(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> nanoocp.TCollection.TCollection_AsciiString:
        """Add material"""

    def DefineMaterial(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style, theKey: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Virtual method actually defining the material (e.g. export to the file).
        """

class RWObj_ObjWriterContext:
    """Auxiliary low-level tool writing OBJ file."""

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: RWObj_ObjWriterContext) -> None: ...

    def IsOpened(self) -> bool:
        """Return true if file has been opened."""

    def Close(self) -> bool:
        """Correctly close the file."""

    def HasNormals(self) -> bool:
        """Return true if normals are defined."""

    def SetNormals(self, theHasNormals: bool) -> None:
        """Set if normals are defined."""

    def HasTexCoords(self) -> bool:
        """Return true if normals are defined."""

    def SetTexCoords(self, theHasTexCoords: bool) -> None:
        """Set if normals are defined."""

    def WriteHeader(self, theNbNodes: int, theNbElems: int, theMatLib: nanoocp.TCollection.TCollection_AsciiString, theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> bool:
        """Write the header."""

    def ActiveMaterial(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return active material or empty string if not set."""

    def WriteActiveMaterial(self, theMaterial: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Set active material."""

    def WriteTriangle(self, theTri: nanoocp.BVH.BVH_Vec3i) -> bool:
        """Writing a triangle"""

    def WriteQuad(self, theQuad: nanoocp.BVH.BVH_Vec4i) -> bool:
        """Writing a quad"""

    def WriteVertex(self, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Writing a vector"""

    def WriteNormal(self, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Writing a vector"""

    def WriteTexCoord(self, theValue: nanoocp.BVH.BVH_Vec2f) -> bool:
        """Writing a vector"""

    def WriteGroup(self, theValue: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Writing a group name"""

    def FlushFace(self, theNbNodes: int) -> None:
        """Increment indices shift."""

    @property
    def NbFaces(self) -> int: ...

    @NbFaces.setter
    def NbFaces(self, arg: int, /) -> None: ...
