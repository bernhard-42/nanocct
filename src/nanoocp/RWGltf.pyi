"""OCCT package RWGltf (toolkit TKDEGLTF)"""

import enum
from typing import BinaryIO, overload

import nanoocp.Bnd
import nanoocp.Image
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.RWMesh
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.XCAFDoc
import nanoocp.XCAFPrs
import nanoocp.RWGltf
import nanoocp.TDF
import nanoocp.TopTools
import nanoocp.gp


class RWGltf_GltfArrayType(enum.IntEnum):
    """Low-level glTF enumeration defining Array type."""

    RWGltf_GltfArrayType_UNKNOWN = 0

    RWGltf_GltfArrayType_Indices = 1

    RWGltf_GltfArrayType_Position = 2

    RWGltf_GltfArrayType_Normal = 3

    RWGltf_GltfArrayType_Color = 4

    RWGltf_GltfArrayType_TCoord0 = 5

    RWGltf_GltfArrayType_TCoord1 = 6

    RWGltf_GltfArrayType_Joint = 7

    RWGltf_GltfArrayType_Weight = 8

RWGltf_GltfArrayType_UNKNOWN: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN

RWGltf_GltfArrayType_Indices: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices

RWGltf_GltfArrayType_Position: RWGltf_GltfArrayType = ...

RWGltf_GltfArrayType_Normal: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal

RWGltf_GltfArrayType_Color: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color

RWGltf_GltfArrayType_TCoord0: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0

RWGltf_GltfArrayType_TCoord1: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1

RWGltf_GltfArrayType_Joint: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint

RWGltf_GltfArrayType_Weight: RWGltf_GltfArrayType = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight

class RWGltf_GltfBufferViewTarget(enum.IntEnum):
    """Low-level glTF enumeration defining BufferView target."""

    RWGltf_GltfBufferViewTarget_UNKNOWN = 0

    RWGltf_GltfBufferViewTarget_ARRAY_BUFFER = 34962

    RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER = 34963

RWGltf_GltfBufferViewTarget_UNKNOWN: RWGltf_GltfBufferViewTarget = ...

RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: RWGltf_GltfBufferViewTarget = ...

RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: RWGltf_GltfBufferViewTarget = ...

class RWGltf_GltfAccessorCompType(enum.IntEnum):
    """Low-level glTF enumeration defining Accessor component type."""

    RWGltf_GltfAccessorCompType_UNKNOWN = 0

    RWGltf_GltfAccessorCompType_Int8 = 5120

    RWGltf_GltfAccessorCompType_UInt8 = 5121

    RWGltf_GltfAccessorCompType_Int16 = 5122

    RWGltf_GltfAccessorCompType_UInt16 = 5123

    RWGltf_GltfAccessorCompType_UInt32 = 5125

    RWGltf_GltfAccessorCompType_Float32 = 5126

RWGltf_GltfAccessorCompType_UNKNOWN: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_Int8: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_UInt8: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_Int16: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_UInt16: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_UInt32: RWGltf_GltfAccessorCompType = ...

RWGltf_GltfAccessorCompType_Float32: RWGltf_GltfAccessorCompType = ...

class RWGltf_GltfAccessorLayout(enum.IntEnum):
    """
    Low-level glTF enumeration defining Accessor layout.
    Similar to Graphic3d_TypeOfData but does not define actual type and includes matrices.
    """

    RWGltf_GltfAccessorLayout_UNKNOWN = 0

    RWGltf_GltfAccessorLayout_Scalar = 1

    RWGltf_GltfAccessorLayout_Vec2 = 2

    RWGltf_GltfAccessorLayout_Vec3 = 3

    RWGltf_GltfAccessorLayout_Vec4 = 4

    RWGltf_GltfAccessorLayout_Mat2 = 5

    RWGltf_GltfAccessorLayout_Mat3 = 6

    RWGltf_GltfAccessorLayout_Mat4 = 7

RWGltf_GltfAccessorLayout_UNKNOWN: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Scalar: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Vec2: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Vec3: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Vec4: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Mat2: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Mat3: RWGltf_GltfAccessorLayout = ...

RWGltf_GltfAccessorLayout_Mat4: RWGltf_GltfAccessorLayout = ...

class RWGltf_WriterTrsfFormat(enum.IntEnum):
    """Transformation format."""

    RWGltf_WriterTrsfFormat_Compact = 0

    RWGltf_WriterTrsfFormat_Mat4 = 1

    RWGltf_WriterTrsfFormat_TRS = 2

RWGltf_WriterTrsfFormat_Compact: RWGltf_WriterTrsfFormat = ...

RWGltf_WriterTrsfFormat_Mat4: RWGltf_WriterTrsfFormat = ...

RWGltf_WriterTrsfFormat_TRS: RWGltf_WriterTrsfFormat = ...

RWGltf_WriterTrsfFormat_LOWER: int = 0

RWGltf_WriterTrsfFormat_UPPER: int = 2

class RWGltf_GltfAlphaMode(enum.IntEnum):
    """Low-level glTF enumeration defining Alpha Mode."""

    RWGltf_GltfAlphaMode_Opaque = 0

    RWGltf_GltfAlphaMode_Mask = 1

    RWGltf_GltfAlphaMode_Blend = 2

RWGltf_GltfAlphaMode_Opaque: RWGltf_GltfAlphaMode = RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Opaque

RWGltf_GltfAlphaMode_Mask: RWGltf_GltfAlphaMode = RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Mask

RWGltf_GltfAlphaMode_Blend: RWGltf_GltfAlphaMode = RWGltf_GltfAlphaMode.RWGltf_GltfAlphaMode_Blend

class RWGltf_GltfPrimitiveMode(enum.IntEnum):
    """
    Low-level glTF enumeration defining Primitive type.
    Similar to Graphic3d_TypeOfData but does not define actual type and includes matrices.
    """

    RWGltf_GltfPrimitiveMode_UNKNOWN = -1

    RWGltf_GltfPrimitiveMode_Points = 0

    RWGltf_GltfPrimitiveMode_Lines = 1

    RWGltf_GltfPrimitiveMode_LineLoop = 2

    RWGltf_GltfPrimitiveMode_LineStrip = 3

    RWGltf_GltfPrimitiveMode_Triangles = 4

    RWGltf_GltfPrimitiveMode_TriangleStrip = 5

    RWGltf_GltfPrimitiveMode_TriangleFan = 6

RWGltf_GltfPrimitiveMode_UNKNOWN: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_Points: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_Lines: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_LineLoop: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_LineStrip: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_Triangles: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_TriangleStrip: RWGltf_GltfPrimitiveMode = ...

RWGltf_GltfPrimitiveMode_TriangleFan: RWGltf_GltfPrimitiveMode = ...

class RWGltf_GltfRootElement(enum.IntEnum):
    """Root elements within glTF JSON document."""

    RWGltf_GltfRootElement_Asset = 0

    RWGltf_GltfRootElement_Scenes = 1

    RWGltf_GltfRootElement_Scene = 2

    RWGltf_GltfRootElement_Nodes = 3

    RWGltf_GltfRootElement_Meshes = 4

    RWGltf_GltfRootElement_Accessors = 5

    RWGltf_GltfRootElement_BufferViews = 6

    RWGltf_GltfRootElement_Buffers = 7

    RWGltf_GltfRootElement_NB_MANDATORY = 8

    RWGltf_GltfRootElement_Animations = 8

    RWGltf_GltfRootElement_Materials = 9

    RWGltf_GltfRootElement_Programs = 10

    RWGltf_GltfRootElement_Samplers = 11

    RWGltf_GltfRootElement_Shaders = 12

    RWGltf_GltfRootElement_Skins = 13

    RWGltf_GltfRootElement_Techniques = 14

    RWGltf_GltfRootElement_Textures = 15

    RWGltf_GltfRootElement_Images = 16

    RWGltf_GltfRootElement_ExtensionsUsed = 17

    RWGltf_GltfRootElement_ExtensionsRequired = 18

    RWGltf_GltfRootElement_NB = 19

RWGltf_GltfRootElement_Asset: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Scenes: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Scene: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Nodes: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Meshes: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Accessors: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_BufferViews: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Buffers: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_NB_MANDATORY: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Materials: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Programs: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Samplers: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Shaders: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Skins: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Techniques: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Textures: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_Images: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_ExtensionsUsed: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_ExtensionsRequired: RWGltf_GltfRootElement = ...

RWGltf_GltfRootElement_NB: RWGltf_GltfRootElement = RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB

RWGltf_GltfRootElement_Animations: RWGltf_GltfRootElement = ...

class RWGltf_CafReader(nanoocp.RWMesh.RWMesh_CafReader):
    """The glTF (GL Transmission Format) mesh reader into XDE document."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWGltf_CafReader) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ToParallel(self) -> bool:
        """
        Return TRUE if multithreaded optimizations are allowed; FALSE by default.
        """

    def SetParallel(self, theToParallel: bool) -> None:
        """Setup multithreaded execution."""

    def ToSkipEmptyNodes(self) -> bool:
        """
        Return TRUE if Nodes without Geometry should be ignored, TRUE by default.
        """

    def SetSkipEmptyNodes(self, theToSkip: bool) -> None:
        """Set flag to ignore nodes without Geometry."""

    def ToLoadAllScenes(self) -> bool:
        """
        Return TRUE if all scenes in the document should be loaded, FALSE by default which means only
        main (default) scene will be loaded.
        """

    def ToApplyScale(self) -> bool:
        """
        Return TRUE if non-uniform scaling should be applied directly to the triangulation.
        FALSE if the average scale should be applied to the transformation matrix.
        """

    def SetLoadAllScenes(self, theToLoadAll: bool) -> None:
        """
        Set flag to flag to load all scenes in the document, FALSE by default which means only main
        (default) scene will be loaded.
        """

    def ToUseMeshNameAsFallback(self) -> bool:
        """
        Set flag to use Mesh name in case if Node name is empty, TRUE by default.
        """

    def SetMeshNameAsFallback(self, theToFallback: bool) -> None:
        """Set flag to use Mesh name in case if Node name is empty."""

    def IsDoublePrecision(self) -> bool:
        """
        Return flag to fill in triangulation using double or single precision; FALSE by default.
        """

    def SetDoublePrecision(self, theIsDouble: bool) -> None:
        """Set flag to fill in triangulation using double or single precision."""

    def ToSkipLateDataLoading(self) -> bool:
        """
        Returns TRUE if data loading should be skipped and can be performed later; FALSE by default.
        """

    def SetToSkipLateDataLoading(self, theToSkip: bool) -> None:
        """Sets flag to skip data loading."""

    def SetToApplyScale(self, theToApplyScale: bool) -> None:
        """
        Set flag to apply non-uniform scaling directly to the triangulation (modify nodes).
        TRUE by default. In case of FALSE the average scale is applied to the transformation matrix.
        """

    def ToKeepLateData(self) -> bool:
        """
        Returns TRUE if data should be loaded into itself without its transferring to new structure.
        It allows to keep information about deferred storage to load/unload this data later.
        TRUE by default.
        """

    def SetToKeepLateData(self, theToKeep: bool) -> None:
        """
        Sets flag to keep information about deferred storage to load/unload data later.
        """

    def ToPrintDebugMessages(self) -> bool:
        """
        Returns TRUE if additional debug information should be print; FALSE by default.
        """

    def SetToPrintDebugMessages(self, theToPrint: bool) -> None:
        """Sets flag to print debug information."""

class RWGltf_DracoParameters:
    """Draco compression parameters"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_DracoParameters) -> None: ...

    @property
    def DracoCompression(self) -> bool:
        """
        flag to use Draco compression (FALSE by default). If it is TRUE, compression is used
        """

    @DracoCompression.setter
    def DracoCompression(self, arg: bool, /) -> None: ...

    @property
    def CompressionLevel(self) -> int:
        """Draco compression level [0-10] (7 by default)"""

    @CompressionLevel.setter
    def CompressionLevel(self, arg: int, /) -> None: ...

    @property
    def QuantizePositionBits(self) -> int:
        """quantization bits for position attribute (14 by default)"""

    @QuantizePositionBits.setter
    def QuantizePositionBits(self, arg: int, /) -> None: ...

    @property
    def QuantizeNormalBits(self) -> int:
        """quantization bits for normal attribute (10 by default)"""

    @QuantizeNormalBits.setter
    def QuantizeNormalBits(self, arg: int, /) -> None: ...

    @property
    def QuantizeTexcoordBits(self) -> int:
        """quantization bits for texture coordinate attribute (12 by default)"""

    @QuantizeTexcoordBits.setter
    def QuantizeTexcoordBits(self, arg: int, /) -> None: ...

    @property
    def QuantizeColorBits(self) -> int:
        """quantization bits for color attributes (8 by default)"""

    @QuantizeColorBits.setter
    def QuantizeColorBits(self, arg: int, /) -> None: ...

    @property
    def QuantizeGenericBits(self) -> int:
        """quantization bits for skinning and custom attributes (12 by default)"""

    @QuantizeGenericBits.setter
    def QuantizeGenericBits(self, arg: int, /) -> None: ...

    @property
    def UnifiedQuantization(self) -> bool:
        """
        quantize positions of all primitives using the same quantization grid (FALSE by default)
        """

    @UnifiedQuantization.setter
    def UnifiedQuantization(self, arg: bool, /) -> None: ...

class RWGltf_GltfBufferView:
    """Low-level glTF data structure defining BufferView."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_GltfBufferView) -> None: ...

    @property
    def Id(self) -> int:
        """index of bufferView in the array of bufferViews"""

    @Id.setter
    def Id(self, arg: int, /) -> None: ...

    @property
    def ByteOffset(self) -> int:
        """offset to the beginning of the data in buffer"""

    @ByteOffset.setter
    def ByteOffset(self, arg: int, /) -> None: ...

    @property
    def ByteLength(self) -> int:
        """length of the data"""

    @ByteLength.setter
    def ByteLength(self, arg: int, /) -> None: ...

    @property
    def ByteStride(self) -> int:
        """[0, 255]"""

    @ByteStride.setter
    def ByteStride(self, arg: int, /) -> None: ...

    @property
    def Target(self) -> RWGltf_GltfBufferViewTarget: ...

    @Target.setter
    def Target(self, arg: RWGltf_GltfBufferViewTarget, /) -> None: ...

class RWGltf_GltfAccessor:
    """Low-level glTF data structure defining Accessor."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWGltf_GltfAccessor) -> None: ...

    @property
    def Id(self) -> int:
        """identifier"""

    @Id.setter
    def Id(self, arg: int, /) -> None: ...

    @property
    def ByteOffset(self) -> int:
        """byte offset"""

    @ByteOffset.setter
    def ByteOffset(self, arg: int, /) -> None: ...

    @property
    def Count(self) -> int:
        """size"""

    @Count.setter
    def Count(self, arg: int, /) -> None: ...

    @property
    def ByteStride(self) -> int:
        """[0, 255] for glTF 1.0"""

    @ByteStride.setter
    def ByteStride(self, arg: int, /) -> None: ...

    @property
    def Type(self) -> RWGltf_GltfAccessorLayout:
        """layout type"""

    @Type.setter
    def Type(self, arg: RWGltf_GltfAccessorLayout, /) -> None: ...

    @property
    def ComponentType(self) -> RWGltf_GltfAccessorCompType:
        """component type"""

    @ComponentType.setter
    def ComponentType(self, arg: RWGltf_GltfAccessorCompType, /) -> None: ...

    @property
    def BndBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """bounding box"""

    @BndBox.setter
    def BndBox(self, arg: nanoocp.Bnd.BVH_Box__double__3, /) -> None: ...

    @property
    def IsCompressed(self) -> bool:
        """flag indicating KHR_draco_mesh_compression"""

    @IsCompressed.setter
    def IsCompressed(self, arg: bool, /) -> None: ...

class RWGltf_GltfFace(nanoocp.Standard.Standard_Transient):
    """
    Low-level glTF data structure holding single Face (one primitive array) definition.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_GltfFace) -> None: ...

    @property
    def NodePos(self) -> RWGltf_GltfAccessor:
        """accessor for nodal positions"""

    @NodePos.setter
    def NodePos(self, arg: RWGltf_GltfAccessor, /) -> None: ...

    @property
    def NodeNorm(self) -> RWGltf_GltfAccessor:
        """accessor for nodal normals"""

    @NodeNorm.setter
    def NodeNorm(self, arg: RWGltf_GltfAccessor, /) -> None: ...

    @property
    def NodeUV(self) -> RWGltf_GltfAccessor:
        """accessor for nodal UV texture coordinates"""

    @NodeUV.setter
    def NodeUV(self, arg: RWGltf_GltfAccessor, /) -> None: ...

    @property
    def Indices(self) -> RWGltf_GltfAccessor:
        """accessor for indexes"""

    @Indices.setter
    def Indices(self, arg: RWGltf_GltfAccessor, /) -> None: ...

    @property
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """original Face or face list"""

    @Shape.setter
    def Shape(self, arg: nanoocp.TopoDS.TopoDS_Shape, /) -> None: ...

    @property
    def Style(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """face style"""

    @Style.setter
    def Style(self, arg: nanoocp.XCAFPrs.XCAFPrs_Style, /) -> None: ...

    @property
    def NbIndexedNodes(self) -> int:
        """
        transient variable for merging several faces into one while writing Indices
        """

    @NbIndexedNodes.setter
    def NbIndexedNodes(self, arg: int, /) -> None: ...

class RWGltf_CafWriter(nanoocp.Standard.Standard_Transient):
    """glTF writer context from XCAF document."""

    @overload
    def __init__(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theIsBinary: bool) -> None:
        """
        Main constructor.
        @param[in] theFile      path to output glTF file
        @param[in] theIsBinary  flag to write into binary glTF format (.glb)
        """

    @overload
    def __init__(self, theOther: RWGltf_CafWriter) -> None: ...

    class Mesh:
        """Mesh"""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: RWGltf_CafWriter.Mesh) -> None: ...

        @property
        def NodesVec(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float]:
            """vector for mesh nodes"""

        @NodesVec.setter
        def NodesVec(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float], /) -> None: ...

        @property
        def NormalsVec(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float]:
            """vector for mesh normals"""

        @NormalsVec.setter
        def NormalsVec(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float], /) -> None: ...

        @property
        def TexCoordsVec(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.NCollection_Vec2__float]:
            """vector for mesh texture UV coordinates"""

        @TexCoordsVec.setter
        def TexCoordsVec(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.NCollection_Vec2__float], /) -> None: ...

        @property
        def IndicesVec(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.Poly_Triangle]:
            """vector for mesh indices"""

        @IndicesVec.setter
        def IndicesVec(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.Poly_Triangle], /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to glTF coordinate system."""

    def ChangeCoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from OCCT to glTF coordinate system."""

    def SetCoordinateSystemConverter(self, theConverter: nanoocp.RWMesh.RWMesh_CoordinateSystemConverter) -> None:
        """Set transformation from OCCT to glTF coordinate system."""

    def IsBinary(self) -> bool:
        """
        Return flag to write into binary glTF format (.glb), specified within class constructor.
        """

    def TransformationFormat(self) -> RWGltf_WriterTrsfFormat:
        """
        Return preferred transformation format for writing into glTF file;
        RWGltf_WriterTrsfFormat_Compact by default.
        """

    def SetTransformationFormat(self, theFormat: RWGltf_WriterTrsfFormat) -> None:
        """Set preferred transformation format for writing into glTF file."""

    def NodeNameFormat(self) -> nanoocp.RWMesh.RWMesh_NameFormat:
        """
        Return name format for exporting Nodes; RWMesh_NameFormat_InstanceOrProduct by default.
        """

    def SetNodeNameFormat(self, theFormat: nanoocp.RWMesh.RWMesh_NameFormat) -> None:
        """Set name format for exporting Nodes."""

    def MeshNameFormat(self) -> nanoocp.RWMesh.RWMesh_NameFormat:
        """
        Return name format for exporting Meshes; RWMesh_NameFormat_Product by default.
        """

    def SetMeshNameFormat(self, theFormat: nanoocp.RWMesh.RWMesh_NameFormat) -> None:
        """Set name format for exporting Meshes."""

    def IsForcedUVExport(self) -> bool:
        """
        Return TRUE to export UV coordinates even if there are no mapped texture; FALSE by default.
        """

    def SetForcedUVExport(self, theToForce: bool) -> None:
        """
        Set flag to export UV coordinates even if there are no mapped texture; FALSE by default.
        """

    def DefaultStyle(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """
        Return default material definition to be used for nodes with only color defined.
        """

    def SetDefaultStyle(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> None:
        """
        Set default material definition to be used for nodes with only color defined.
        """

    def ToEmbedTexturesInGlb(self) -> bool:
        """
        Return flag to write image textures into GLB file (binary gltf export); TRUE by default.
        When set to FALSE, texture images will be written as separate files.
        Has no effect on writing into non-binary format.
        """

    def SetToEmbedTexturesInGlb(self, theToEmbedTexturesInGlb: bool) -> None:
        """Set flag to write image textures into GLB file (binary gltf export)."""

    def ToMergeFaces(self) -> bool:
        """Return flag to merge faces within a single part; FALSE by default."""

    def SetMergeFaces(self, theToMerge: bool) -> None:
        """
        Set flag to merge faces within a single part.
        May reduce JSON size thanks to smaller number of primitive arrays.
        """

    def ToSplitIndices16(self) -> bool:
        """
        Return flag to prefer keeping 16-bit indexes while merging face; FALSE by default.
        """

    def SetSplitIndices16(self, theToSplit: bool) -> None:
        """
        Set flag to prefer keeping 16-bit indexes while merging face.
        Has effect only with ToMergeFaces() option turned ON.
        May reduce binary data size thanks to smaller triangle indexes.
        """

    def ToParallel(self) -> bool:
        """
        Return TRUE if multithreaded optimizations are allowed; FALSE by default.
        """

    def SetParallel(self, theToParallel: bool) -> None:
        """Setup multithreaded execution."""

    def CompressionParameters(self) -> RWGltf_DracoParameters:
        """Return Draco parameters"""

    def SetCompressionParameters(self, theDracoParameters: RWGltf_DracoParameters) -> None:
        """Set Draco parameters"""

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theRootLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theLabelFilter: nanoocp.NCollection.NCollection_Map[nanoocp.TCollection.TCollection_AsciiString], theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write glTF file and associated binary file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument     input document
        @param[in] theRootLabels   list of root shapes to export
        @param[in] theLabelFilter  optional filter with document nodes to export,
        with keys defined by XCAFPrs_DocumentExplorer::DefineChildId() and
        filled recursively (leaves and parent assembly nodes at all
        levels); when not NULL, all nodes not included into the map will be
        ignored
        @param[in] theFileInfo     map with file metadata to put into glTF header section
        @param[in] theProgress     optional progress indicator
        @return FALSE on file writing failure
        """

    @overload
    def Perform(self, theDocument: nanoocp.TDocStd.TDocStd_Document | None, theFileInfo: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Write glTF file and associated binary file.
        Triangulation data should be precomputed within shapes!
        @param[in] theDocument     input document
        @param[in] theFileInfo     map with file metadata to put into glTF header section
        @param[in] theProgress     optional progress indicator
        @return FALSE on file writing failure
        """

class RWGltf_GltfPrimArrayData:
    """
    An element within primitive array - vertex attribute or element indexes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theType: RWGltf_GltfArrayType) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_GltfPrimArrayData) -> None: ...

    @property
    def StreamData(self) -> nanoocp.NCollection.NCollection_Buffer: ...

    @StreamData.setter
    def StreamData(self, arg: nanoocp.NCollection.NCollection_Buffer, /) -> None: ...

    @property
    def StreamUri(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @StreamUri.setter
    def StreamUri(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def StreamOffset(self) -> int: ...

    @StreamOffset.setter
    def StreamOffset(self, arg: int, /) -> None: ...

    @property
    def StreamLength(self) -> int: ...

    @StreamLength.setter
    def StreamLength(self, arg: int, /) -> None: ...

    @property
    def Accessor(self) -> RWGltf_GltfAccessor: ...

    @Accessor.setter
    def Accessor(self, arg: RWGltf_GltfAccessor, /) -> None: ...

    @property
    def Type(self) -> RWGltf_GltfArrayType: ...

    @Type.setter
    def Type(self, arg: RWGltf_GltfArrayType, /) -> None: ...

class RWGltf_GltfLatePrimitiveArray(nanoocp.RWMesh.RWMesh_TriangulationSource):
    """Mesh data wrapper for delayed primitive array loading from glTF file."""

    def __init__(self, theId: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Entity id."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Entity name."""

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Assign entity name."""

    def PrimitiveMode(self) -> RWGltf_GltfPrimitiveMode:
        """Return type of primitive array."""

    def SetPrimitiveMode(self, theMode: RWGltf_GltfPrimitiveMode) -> None:
        """Set type of primitive array."""

    def HasStyle(self) -> bool:
        """Return true if primitive array has assigned material"""

    def BaseColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return base color."""

    def MaterialPbr(self) -> RWGltf_MaterialMetallicRoughness:
        """Return PBR material definition."""

    def SetMaterialPbr(self, theMat: RWGltf_MaterialMetallicRoughness | None) -> None:
        """Set PBR material definition."""

    def MaterialCommon(self) -> RWGltf_MaterialCommon:
        """Return common (obsolete) material definition."""

    def SetMaterialCommon(self, theMat: RWGltf_MaterialCommon | None) -> None:
        """Set common (obsolete) material definition."""

    def Data(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.RWGltf.RWGltf_GltfPrimArrayData]:
        """Return primitive array data elements."""

    def AddPrimArrayData(self, theType: RWGltf_GltfArrayType) -> RWGltf_GltfPrimArrayData:
        """Add primitive array data element."""

    def HasDeferredData(self) -> bool:
        """
        Return TRUE if there is deferred storage and some triangulation data
        that can be loaded using LoadDeferredData().
        """

    def LoadStreamData(self) -> nanoocp.Poly.Poly_Triangulation:
        """
        Load primitive array saved as stream buffer to new triangulation object.
        """

class RWGltf_MaterialCommon(nanoocp.Standard.Standard_Transient):
    """glTF 1.0 format common (obsolete) material definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_MaterialCommon) -> None: ...

    @property
    def AmbientTexture(self) -> nanoocp.Image.Image_Texture:
        """image defining ambient color"""

    @AmbientTexture.setter
    def AmbientTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def DiffuseTexture(self) -> nanoocp.Image.Image_Texture:
        """image defining diffuse color"""

    @DiffuseTexture.setter
    def DiffuseTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def SpecularTexture(self) -> nanoocp.Image.Image_Texture:
        """image defining specular color"""

    @SpecularTexture.setter
    def SpecularTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """material identifier"""

    @Id.setter
    def Id(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """material name"""

    @Name.setter
    def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

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
    def EmissiveColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    @EmissiveColor.setter
    def EmissiveColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def Shininess(self) -> float: ...

    @Shininess.setter
    def Shininess(self, arg: float, /) -> None: ...

    @property
    def Transparency(self) -> float: ...

    @Transparency.setter
    def Transparency(self, arg: float, /) -> None: ...

class RWGltf_MaterialMetallicRoughness(nanoocp.Standard.Standard_Transient):
    """glTF 2.0 format PBR material definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWGltf_MaterialMetallicRoughness) -> None: ...

    @property
    def BaseColorTexture(self) -> nanoocp.Image.Image_Texture:
        """RGB texture for the base color"""

    @BaseColorTexture.setter
    def BaseColorTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def MetallicRoughnessTexture(self) -> nanoocp.Image.Image_Texture:
        """RG texture packing the metallic and roughness properties together"""

    @MetallicRoughnessTexture.setter
    def MetallicRoughnessTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def EmissiveTexture(self) -> nanoocp.Image.Image_Texture:
        """
        RGB emissive map controls the color and intensity of the light being emitted by the material
        """

    @EmissiveTexture.setter
    def EmissiveTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def OcclusionTexture(self) -> nanoocp.Image.Image_Texture:
        """R occlusion map indicating areas of indirect lighting"""

    @OcclusionTexture.setter
    def OcclusionTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def NormalTexture(self) -> nanoocp.Image.Image_Texture:
        """normal map"""

    @NormalTexture.setter
    def NormalTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """material identifier"""

    @Id.setter
    def Id(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """material name"""

    @Name.setter
    def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def BaseColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """
        base color (or scale factor to the texture); [1.0, 1.0, 1.0, 1.0] by default
        """

    @BaseColor.setter
    def BaseColor(self, arg: nanoocp.Quantity.Quantity_ColorRGBA, /) -> None: ...

    @property
    def EmissiveFactor(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """emissive color; [0.0, 0.0, 0.0] by default"""

    @EmissiveFactor.setter
    def EmissiveFactor(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def Metallic(self) -> float:
        """
        metalness (or scale factor to the texture) within range [0.0, 1.0]; 1.0 by default
        """

    @Metallic.setter
    def Metallic(self, arg: float, /) -> None: ...

    @property
    def Roughness(self) -> float:
        """
        roughness (or scale factor to the texture) within range [0.0, 1.0]; 1.0 by default
        """

    @Roughness.setter
    def Roughness(self, arg: float, /) -> None: ...

    @property
    def AlphaCutOff(self) -> float:
        """alpha cutoff value; 0.5 by default"""

    @AlphaCutOff.setter
    def AlphaCutOff(self, arg: float, /) -> None: ...

    @property
    def AlphaMode(self) -> RWGltf_GltfAlphaMode:
        """alpha mode; RWGltf_GltfAlphaMode_Opaque by default"""

    @AlphaMode.setter
    def AlphaMode(self, arg: RWGltf_GltfAlphaMode, /) -> None: ...

    @property
    def IsDoubleSided(self) -> bool:
        """specifies whether the material is double sided; FALSE by default"""

    @IsDoubleSided.setter
    def IsDoubleSided(self, arg: bool, /) -> None: ...

class RWGltf_GltfJsonParser:
    """INTERNAL tool for parsing glTF document (JSON structure)."""

    def __init__(self, theRootShapes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """Empty constructor."""

    @staticmethod
    def FormatParseError(theCode: "rapidjson::ParseErrorCode") -> str:
        """Auxiliary method for formatting error code."""

    def SetFilePath(self, theFilePath: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set file path."""

    def SetProbeHeader(self, theToProbe: bool) -> None:
        """Set flag for probing file without complete reading."""

    def ErrorPrefix(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return prefix for reporting issues."""

    def SetErrorPrefix(self, theErrPrefix: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set prefix for reporting issues."""

    def SetAttributeMap(self, theAttribMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.RWMesh.RWMesh_NodeAttributes, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Set map for storing node attributes."""

    def SetScaleMap(self, theScaleMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.gp.gp_XYZ, nanoocp.TopTools.TopTools_ShapeMapHasher]) -> None:
        """Set map for storing non-uniform scalings."""

    def SetExternalFiles(self, theExternalFiles: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Set list for storing external files."""

    def SetMetadata(self, theMetadata: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Set metadata map."""

    def SetReadAssetExtras(self, theToRead: bool) -> None:
        """Set flag to translate asset.extras into metadata."""

    def CoordinateSystemConverter(self) -> nanoocp.RWMesh.RWMesh_CoordinateSystemConverter:
        """Return transformation from glTF to OCCT coordinate system."""

    def SetCoordinateSystemConverter(self, theConverter: nanoocp.RWMesh.RWMesh_CoordinateSystemConverter) -> None:
        """Set transformation from glTF to OCCT coordinate system."""

    def SetBinaryFormat(self, theBinBodyOffset: int, theBinBodyLen: int) -> None:
        """Initialize binary format."""

    def SetSkipEmptyNodes(self, theToSkip: bool) -> None:
        """Set flag to ignore nodes without Geometry, TRUE by default."""

    def SetLoadAllScenes(self, theToLoadAll: bool) -> None:
        """
        Set flag to flag to load all scenes in the document, FALSE by default which means only main
        (default) scene will be loaded.
        """

    def SetMeshNameAsFallback(self, theToFallback: bool) -> None:
        """
        Set flag to use Mesh name in case if Node name is empty, TRUE by default.
        """

    def SetToApplyScale(self, theToApplyScale: bool) -> None:
        """
        Set flag to apply non-uniform scaling directly to the triangulation (modify nodes).
        TRUE by default. In case of FALSE the average scale is applied to the transformation matrix.
        """

    def Parse(self, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """Parse glTF document."""

    def FaceList(self) -> nanoocp.NCollection.NCollection_DynamicArray[nanoocp.TopoDS.TopoDS_Face]:
        """Return face list for loading triangulation."""

class RWGltf_GltfMaterialMap(nanoocp.RWMesh.RWMesh_MaterialMap):
    """Material manager for exporting into glTF format."""

    @overload
    def __init__(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theDefSamplerId: int) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: RWGltf_GltfMaterialMap) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AddGlbImages(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> str:
        """
        Add material images into GLB stream.
        @param[in][out] theBinFile   output file stream
        @param[in] theStyle    material images to add
        """

    def FlushGlbBufferViews(self, theWriter: RWGltf_GltfOStreamWriter, theBinDataBufferId: int) -> int:
        """
        Add bufferView's into RWGltf_GltfRootElement_BufferViews section with images collected by
        AddImagesToGlb().
        """

    def FlushGlbImages(self, theWriter: RWGltf_GltfOStreamWriter) -> None:
        """
        Write RWGltf_GltfRootElement_Images section with images collected by AddImagesToGlb().
        """

    def AddImages(self, theWriter: RWGltf_GltfOStreamWriter, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> bool:
        """
        Add material images in case of non-GLB file
        (an alternative to AddImagesToGlb() + FlushBufferViews() + FlushImagesGlb()).
        """

    def AddMaterial(self, theWriter: RWGltf_GltfOStreamWriter, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> bool:
        """Add material."""

    def AddTextures(self, theWriter: RWGltf_GltfOStreamWriter, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> bool:
        """Add material textures."""

    def NbImages(self) -> int:
        """Return extent of images map."""

    def NbTextures(self) -> int:
        """Return extent of textures map."""

    @staticmethod
    def baseColorTexture(theMat: nanoocp.XCAFDoc.XCAFDoc_VisMaterial | None) -> nanoocp.Image.Image_Texture:
        """Return base color texture."""

class RWGltf_GltfOStreamWriter:
    """rapidjson::Writer wrapper for forward declaration."""

class RWGltf_TriangulationReader(nanoocp.RWMesh.RWMesh_TriangulationReader):
    """RWMesh_TriangulationReader implementation creating Poly_Triangulation."""

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LoadStreamData(self, theSourceMesh: nanoocp.RWMesh.RWMesh_TriangulationSource | None, theDestMesh: nanoocp.Poly.Poly_Triangulation | None) -> bool:
        """
        Loads only primitive arrays saved as stream buffer
        (it is primarily glTF data encoded in base64 saved to temporary buffer during glTF file
        reading).
        """

    def ReadStream(self, theSourceMesh: RWGltf_GltfLatePrimitiveArray | None, theDestMesh: nanoocp.Poly.Poly_Triangulation | None, theStream: BinaryIO, theAccessor: RWGltf_GltfAccessor, theType: RWGltf_GltfArrayType) -> bool:
        """
        Fills triangulation, lines and points data.
        @param theSourceGltfMesh source glTF triangulation
        @param theDestMesh       triangulation to be modified
        @param theStream         input stream to read from
        @param theAccessor       buffer accessor
        @param theType           array type
        @return FALSE on error
        """

class RWGltf_GltfSceneNodeMap(nanoocp.NCollection.NCollection_IndexedMap[nanoocp.XCAFPrs.XCAFPrs_DocumentNode]):
    """Indexed map of scene nodes with custom search algorithm."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWGltf_GltfSceneNodeMap) -> None: ...

    def FindIndex(self, theNodeId: nanoocp.TCollection.TCollection_AsciiString) -> int:
        """Find index from document node string identifier."""

def RWGltf_GltfParseAttribType(theType: str) -> RWGltf_GltfArrayType:
    """Parse GltfArrayType from string."""

def RWGltf_GltfParseAccessorType(theType: str) -> RWGltf_GltfAccessorLayout:
    """Parse GltfAccessorLayout from string."""

def RWGltf_GltfParseAlphaMode(theType: str) -> RWGltf_GltfAlphaMode:
    """Parse RWGltf_GltfAlphaMode from string."""

def RWGltf_GltfRootElementName(theElem: RWGltf_GltfRootElement) -> str:
    """Root elements within glTF JSON document - names array."""
