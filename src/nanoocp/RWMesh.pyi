"""OCCT package RWMesh (toolkit TKRWMesh)"""

import enum
from typing import TextIO, overload

import nanoocp.Image
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDataStd
import nanoocp.TDocStd
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.XCAFDoc
import nanoocp.XCAFPrs
import nanoocp.gp
import nanoocp.TopTools


class RWMesh_NameFormat(enum.IntEnum):
    """Name format preference for XCAF shape labels."""

    RWMesh_NameFormat_Empty = 0

    RWMesh_NameFormat_Product = 1

    RWMesh_NameFormat_Instance = 2

    RWMesh_NameFormat_InstanceOrProduct = 3

    RWMesh_NameFormat_ProductOrInstance = 4

    RWMesh_NameFormat_ProductAndInstance = 5

    RWMesh_NameFormat_ProductAndInstanceAndOcaf = 6

RWMesh_NameFormat_Empty: RWMesh_NameFormat = RWMesh_NameFormat.RWMesh_NameFormat_Empty

RWMesh_NameFormat_Product: RWMesh_NameFormat = RWMesh_NameFormat.RWMesh_NameFormat_Product

RWMesh_NameFormat_Instance: RWMesh_NameFormat = RWMesh_NameFormat.RWMesh_NameFormat_Instance

RWMesh_NameFormat_InstanceOrProduct: RWMesh_NameFormat = ...

RWMesh_NameFormat_ProductOrInstance: RWMesh_NameFormat = ...

RWMesh_NameFormat_ProductAndInstance: RWMesh_NameFormat = ...

RWMesh_NameFormat_ProductAndInstanceAndOcaf: RWMesh_NameFormat = ...

class RWMesh_CoordinateSystem(enum.IntEnum):
    """
    Standard coordinate system definition.
    Open CASCADE does not force application using specific coordinate system,
    although Draw Harness and samples define +Z-up +Y-forward coordinate system for camera view
    manipulation. This enumeration defines two commonly used conventions - Z-up and Y-up..
    """

    RWMesh_CoordinateSystem_Undefined = -1

    RWMesh_CoordinateSystem_posYfwd_posZup = 0

    RWMesh_CoordinateSystem_negZfwd_posYup = 1

    RWMesh_CoordinateSystem_Blender = 0

    RWMesh_CoordinateSystem_glTF = 1

    RWMesh_CoordinateSystem_Zup = 0

    RWMesh_CoordinateSystem_Yup = 1

RWMesh_CoordinateSystem_Undefined: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_posYfwd_posZup: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_negZfwd_posYup: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_Blender: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_glTF: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_Zup: RWMesh_CoordinateSystem = ...

RWMesh_CoordinateSystem_Yup: RWMesh_CoordinateSystem = ...

class RWMesh_CafReaderStatusEx(enum.IntEnum):
    """Extended status bits."""

    RWMesh_CafReaderStatusEx_NONE = 0

    RWMesh_CafReaderStatusEx_Partial = 1

RWMesh_CafReaderStatusEx_NONE: RWMesh_CafReaderStatusEx = ...

RWMesh_CafReaderStatusEx_Partial: RWMesh_CafReaderStatusEx = ...

class RWMesh:
    """Auxiliary tools for RWMesh package."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWMesh) -> None: ...

    @staticmethod
    def ReadNameAttribute(theLabel: nanoocp.TDF.TDF_Label) -> nanoocp.TCollection.TCollection_AsciiString:
        """Read name attribute from label."""

    @staticmethod
    def FormatName(theFormat: RWMesh_NameFormat, theLabel: nanoocp.TDF.TDF_Label, theRefLabel: nanoocp.TDF.TDF_Label) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Generate name for specified labels.
        @param[in] theFormat   name format to apply
        @param[in] theLabel    instance label
        @param[in] theRefLabel product label
        """

class RWMesh_CoordinateSystemConverter:
    """
    Coordinate system converter defining the following tools:
    - Initialization for commonly used coordinate systems Z-up and Y-up.
    - Perform length unit conversion (scaling).
    - Conversion of three basic elements:
    a) mesh node Positions,
    b) mesh node Normals,
    c) model nodes Transformations (locations).

    RWMesh_CoordinateSystem enumeration is used for convenient conversion between two commonly
    used coordinate systems, to make sure that imported model is oriented up.
    But gp_Ax3 can be used instead for defining a conversion between arbitrary systems (e.g.
    including non-zero origin).

    The converter requires defining explicitly both input and output systems,
    so that if either input or output is undefined, then conversion will be skipped.
    Length units conversion and coordinate system conversion are decomposed,
    so that application might specify no length units conversion but Y-up to Z-up coordinate system
    conversion.

    Class defines dedicated methods for parameters of input and output systems.
    This allows passing tool through several initialization steps,
    so that a reader can initialize input length units (only if file format defines such
    information), while application specifies output length units, and conversion will be done only
    when both defined.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: RWMesh_CoordinateSystemConverter) -> None: ...

    @staticmethod
    def StandardCoordinateSystem(theSys: RWMesh_CoordinateSystem) -> nanoocp.gp.gp_Ax3:
        """Return a standard coordinate system definition."""

    def IsEmpty(self) -> bool:
        """
        Return TRUE if there is no transformation (target and current coordinates systems are same).
        """

    def InputLengthUnit(self) -> float:
        """
        Return source length units, defined as scale factor to m (meters).
        -1.0 by default, which means that NO conversion will be applied (regardless output length
        unit).
        """

    def SetInputLengthUnit(self, theInputScale: float) -> None:
        """Set source length units as scale factor to m (meters)."""

    def OutputLengthUnit(self) -> float:
        """
        Return destination length units, defined as scale factor to m (meters).
        -1.0 by default, which means that NO conversion will be applied (regardless input length
        unit).
        """

    def SetOutputLengthUnit(self, theOutputScale: float) -> None:
        """Set destination length units as scale factor to m (meters)."""

    def HasInputCoordinateSystem(self) -> bool:
        """
        Return TRUE if source coordinate system has been set; FALSE by default.
        """

    def InputCoordinateSystem(self) -> nanoocp.gp.gp_Ax3:
        """Source coordinate system; UNDEFINED by default."""

    @overload
    def SetInputCoordinateSystem(self, theSysFrom: nanoocp.gp.gp_Ax3) -> None: ...

    @overload
    def SetInputCoordinateSystem(self, theSysFrom: RWMesh_CoordinateSystem) -> None:
        """Set source coordinate system."""

    def HasOutputCoordinateSystem(self) -> bool:
        """
        Return TRUE if destination coordinate system has been set; FALSE by default.
        """

    def OutputCoordinateSystem(self) -> nanoocp.gp.gp_Ax3:
        """Destination coordinate system; UNDEFINED by default."""

    @overload
    def SetOutputCoordinateSystem(self, theSysTo: nanoocp.gp.gp_Ax3) -> None: ...

    @overload
    def SetOutputCoordinateSystem(self, theSysTo: RWMesh_CoordinateSystem) -> None:
        """Set destination coordinate system."""

    def Init(self, theInputSystem: nanoocp.gp.gp_Ax3, theInputLengthUnit: float, theOutputSystem: nanoocp.gp.gp_Ax3, theOutputLengthUnit: float) -> None:
        """Initialize transformation."""

    def TransformTransformation(self, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """Transform transformation."""

    def TransformPosition(self, thePos: nanoocp.gp.gp_XYZ) -> None:
        """Transform position."""

    def TransformNormal(self, theNorm: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Transform normal (e.g. exclude translation/scale part of transformation).
        """

class RWMesh_NodeAttributes:
    """Attributes of the node."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWMesh_NodeAttributes) -> None: ...

    @property
    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name for the user"""

    @Name.setter
    def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def RawName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """name within low-level format structure"""

    @RawName.setter
    def RawName(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

    @property
    def NamedData(self) -> nanoocp.TDataStd.TDataStd_NamedData:
        """optional metadata"""

    @NamedData.setter
    def NamedData(self, arg: nanoocp.TDataStd.TDataStd_NamedData, /) -> None: ...

    @property
    def Style(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """presentation style"""

    @Style.setter
    def Style(self, arg: nanoocp.XCAFPrs.XCAFPrs_Style, /) -> None: ...

class RWMesh_CafReader(nanoocp.Standard.Standard_Transient):
    """
    The general interface for importing mesh data into XDE document.

    The tool implements auxiliary structures for creating an XDE document in two steps:
    1) Creating TopoDS_Shape hierarchy (myRootShapes)
    and Shape attributes (myAttribMap) separately within performMesh().
    Attributes include names and styles.
    2) Filling XDE document from these auxiliary structures.
    Named elements are expanded within document structure, while Compounds having no named
    children will remain collapsed. In addition, unnamed nodes can be filled with generated names
    like "Face", "Compound" via generateNames() method, and the very root unnamed node can be
    filled from file name like "MyModel.obj".
    """

    class CafDocumentTools:
        """Structure holding tools for filling the document."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: RWMesh_CafReader.CafDocumentTools) -> None: ...

        @property
        def ShapeTool(self) -> nanoocp.XCAFDoc.XCAFDoc_ShapeTool: ...

        @ShapeTool.setter
        def ShapeTool(self, arg: nanoocp.XCAFDoc.XCAFDoc_ShapeTool, /) -> None: ...

        @property
        def ColorTool(self) -> nanoocp.XCAFDoc.XCAFDoc_ColorTool: ...

        @ColorTool.setter
        def ColorTool(self, arg: nanoocp.XCAFDoc.XCAFDoc_ColorTool, /) -> None: ...

        @property
        def VisMaterialTool(self) -> nanoocp.XCAFDoc.XCAFDoc_VisMaterialTool: ...

        @VisMaterialTool.setter
        def VisMaterialTool(self, arg: nanoocp.XCAFDoc.XCAFDoc_VisMaterialTool, /) -> None: ...

        @property
        def ComponentMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

        @ComponentMap.setter
        def ComponentMap(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher], /) -> None: ...

        @property
        def OriginalShapeMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

        @OriginalShapeMap.setter
        def OriginalShapeMap(self, arg: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher], /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Document(self) -> nanoocp.TDocStd.TDocStd_Document:
        """Return target document."""

    def SetDocument(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None) -> None:
        """
        Set target document.
        Set system length unit according to the units of the document
        """

    def RootPrefix(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return prefix for generating root labels names."""

    def SetRootPrefix(self, theRootPrefix: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set prefix for generating root labels names"""

    def ToFillIncompleteDocument(self) -> bool:
        """
        Flag indicating if partially read file content should be put into the XDE document, TRUE by
        default.

        Partial read means unexpected end of file, critical parsing syntax errors in the middle of
        file, or reached memory limit indicated by performMesh() returning FALSE. Partial read allows
        importing a model even in case of formal reading failure, so that it will be up to user to
        decide if processed data has any value.

        In case of partial read (performMesh() returns FALSE, but there are some data that could be
        put into document), Perform() will return TRUE and result flag will have failure bit set.
        @sa MemoryLimitMiB(), ExtraStatus().
        """

    def SetFillIncompleteDocument(self, theToFillIncomplete: bool) -> None:
        """
        Set flag allowing partially read file content to be put into the XDE document.
        """

    def MemoryLimitMiB(self) -> int:
        """Return memory usage limit in MiB, -1 by default which means no limit."""

    def SetMemoryLimitMiB(self, theLimitMiB: int) -> None:
        """
        Set memory usage limit in MiB; can be ignored by reader implementation!
        """

    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter:
        """Return coordinate system converter."""

    def SetCoordinateSystemConverter(self, theConverter: RWMesh_CoordinateSystemConverter) -> None:
        """Set coordinate system converter."""

    def SystemLengthUnit(self) -> float:
        """
        Return the length unit to convert into while reading the file, defined as scale factor for m
        (meters); -1.0 by default, which means that NO conversion will be applied.
        """

    def SetSystemLengthUnit(self, theUnits: float) -> None:
        """
        Set system length units to convert into while reading the file, defined as scale factor for m
        (meters).
        """

    def HasSystemCoordinateSystem(self) -> bool:
        """
        Return TRUE if system coordinate system has been defined; FALSE by default.
        """

    def SystemCoordinateSystem(self) -> nanoocp.gp.gp_Ax3:
        """
        Return system coordinate system; UNDEFINED by default, which means that no conversion will be
        done.
        """

    @overload
    def SetSystemCoordinateSystem(self, theCS: nanoocp.gp.gp_Ax3) -> None: ...

    @overload
    def SetSystemCoordinateSystem(self, theCS: RWMesh_CoordinateSystem) -> None:
        """
        Set system origin coordinate system to perform conversion into during read.
        """

    def FileLengthUnit(self) -> float:
        """
        Return the length unit to convert from while reading the file, defined as scale factor for m
        (meters). Can be undefined (-1.0) if file format is unitless.
        """

    def SetFileLengthUnit(self, theUnits: float) -> None:
        """
        Set (override) file length units to convert from while reading the file, defined as scale
        factor for m (meters).
        """

    def HasFileCoordinateSystem(self) -> bool:
        """Return TRUE if file origin coordinate system has been defined."""

    def FileCoordinateSystem(self) -> nanoocp.gp.gp_Ax3:
        """
        Return file origin coordinate system; can be UNDEFINED, which means no conversion will be
        done.
        """

    @overload
    def SetFileCoordinateSystem(self, theCS: nanoocp.gp.gp_Ax3) -> None: ...

    @overload
    def SetFileCoordinateSystem(self, theCS: RWMesh_CoordinateSystem) -> None:
        """
        Set (override) file origin coordinate system to perform conversion during read.
        """

    @overload
    def Perform(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Open stream and pass it to Perform method.
        The Document instance should be set beforehand.
        """

    @overload
    def Perform(self, theStream: TextIO, theProgress: nanoocp.Message.Message_ProgressRange, theFile: nanoocp.TCollection.TCollection_AsciiString = ...) -> bool:
        """Read the data from specified file."""

    def ExtraStatus(self) -> int:
        """
        Return extended status flags.
        @sa RWMesh_CafReaderStatusEx enumeration.
        """

    def SingleShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return result as a single shape."""

    def ExternalFiles(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Return the list of complementary files - external references (textures, data, etc.).
        """

    def Metadata(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """Return metadata map."""

    @overload
    def ProbeHeader(self, theFile: nanoocp.TCollection.TCollection_AsciiString, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """Open stream and pass it to ProbeHeader method."""

    @overload
    def ProbeHeader(self, theStream: TextIO, theFile: nanoocp.TCollection.TCollection_AsciiString = ..., theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Read the header data from specified file without reading entire model.
        The main purpose is collecting metadata and external references - for copying model into a new
        location, for example. Can be NOT implemented (unsupported by format / reader).
        """

class RWMesh_ShapeIterator:
    """
    This is a virtual base class for other shape iterators.
    Provides an abstract interface for iterating over the elements of a shape.
    It defines a set of pure virtual methods that must be implemented by
    derived classes to handle specific types of shapes and their elements.
    """

    def ExploredShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return explored shape."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return shape."""

    def More(self) -> bool:
        """Return true if iterator points to the valid triangulation."""

    def Next(self) -> None:
        """Find next value."""

    def IsEmpty(self) -> bool:
        """Return true if mesh data is defined."""

    def Style(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """Return shape material."""

    def HasColor(self) -> bool:
        """Return TRUE if shape color is set."""

    def Color(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return shape color."""

    def ElemLower(self) -> int:
        """Lower element index in current triangulation."""

    def ElemUpper(self) -> int:
        """Upper element index in current triangulation."""

    def NbNodes(self) -> int:
        """Return number of nodes for the current shape."""

    def NodeLower(self) -> int:
        """Lower node index in current shape."""

    def NodeUpper(self) -> int:
        """Upper node index in current shape."""

    def NodeTransformed(self, theNode: int) -> nanoocp.gp.gp_Pnt:
        """Return the node with specified index with applied transformation."""

class RWMesh_EdgeIterator(RWMesh_ShapeIterator):
    """
    Auxiliary class to iterate through edges.
    Provides functionality to iterate through the edges of a shape.
    It inherits from `RWMesh_ShapeIterator` and implements
    methods to access and manipulate edge data.
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Auxiliary constructor.
        @param[in] theShape The shape to iterate.
        @param[in] theStyle The style of the shape.
        """

    @overload
    def __init__(self, theLabel: nanoocp.TDF.TDF_Label, theLocation: nanoocp.TopLoc.TopLoc_Location, theToMapColors: bool = False, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Main constructor.
        @param[in] theLabel The label of the shape.
        @param[in] theLocation The location of the shape.
        @param[in] theToMapColors Flag to indicate if colors should be mapped.
        @param[in] theStyle The style of the shape.
        """

    def More(self) -> bool:
        """Return true if iterator points to the valid triangulation."""

    def Next(self) -> None:
        """Find next value."""

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Return current edge."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return current edge."""

    def Polygon3D(self) -> nanoocp.Poly.Poly_Polygon3D:
        """Return current edge data."""

    def IsEmpty(self) -> bool:
        """Return true if geometry data is defined."""

    def ElemLower(self) -> int:
        """Lower element index in current triangulation."""

    def ElemUpper(self) -> int:
        """Upper element index in current triangulation."""

    def NbNodes(self) -> int:
        """Return number of nodes for the current edge."""

    def NodeLower(self) -> int:
        """Lower node index in current triangulation."""

    def NodeUpper(self) -> int:
        """Upper node index in current triangulation."""

    def node(self, theNode: int) -> nanoocp.gp.gp_Pnt:
        """Return the node with specified index with applied transformation."""

class RWMesh_FaceIterator(RWMesh_ShapeIterator):
    """
    Auxiliary class to iterate through triangulated faces.
    Class is designed to provide an interface for iterating over the faces
    of a shape, specifically focusing on triangulated faces.
    It inherits from the `RWMesh_ShapeIterator` base class and
    extends its functionality to handle faces with triangulation data.
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Auxiliary constructor.
        @param[in] theShape Shape containing the face data
        @param[in] theStyle Style information for the face
        """

    @overload
    def __init__(self, theLabel: nanoocp.TDF.TDF_Label, theLocation: nanoocp.TopLoc.TopLoc_Location, theToMapColors: bool = False, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Main constructor.
        @param[in] theLabel Label containing the face data
        @param[in] theLocation Location of the face
        @param[in] theToMapColors Flag to indicate if colors should be mapped
        @param[in] theStyle Style information for the face
        """

    def More(self) -> bool:
        """Return true if iterator points to the valid triangulation."""

    def Next(self) -> None:
        """Find next value."""

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face:
        """Return current face."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return current face."""

    def Triangulation(self) -> nanoocp.Poly.Poly_Triangulation:
        """Return current face triangulation."""

    def IsEmptyMesh(self) -> bool:
        """Return true if mesh data is defined."""

    def IsEmpty(self) -> bool:
        """Return true if mesh data is defined."""

    def FaceStyle(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """Return face material."""

    def HasFaceColor(self) -> bool:
        """Return TRUE if face color is set."""

    def FaceColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return face color."""

    def NbTriangles(self) -> int:
        """Return number of elements of specific type for the current face."""

    def ElemLower(self) -> int:
        """Lower element index in current triangulation."""

    def ElemUpper(self) -> int:
        """Upper element index in current triangulation."""

    def TriangleOriented(self, theElemIndex: int) -> nanoocp.Poly.Poly_Triangle:
        """Return triangle with specified index with applied Face orientation."""

    def HasNormals(self) -> bool:
        """Return true if triangulation has defined normals."""

    def HasTexCoords(self) -> bool:
        """Return true if triangulation has defined normals."""

    def NormalTransformed(self, theNode: int) -> nanoocp.gp.gp_Dir:
        """
        Return normal at specified node index with face transformation applied and face orientation
        applied.
        """

    def NbNodes(self) -> int:
        """Return number of nodes for the current face."""

    def NodeLower(self) -> int:
        """Lower node index in current triangulation."""

    def NodeUpper(self) -> int:
        """Upper node index in current triangulation."""

    def NodeTexCoord(self, theNode: int) -> nanoocp.gp.gp_Pnt2d:
        """Return texture coordinates for the node."""

    def node(self, theNode: int) -> nanoocp.gp.gp_Pnt:
        """Return the node with specified index with applied transformation."""

    def normal(self, theNode: int) -> nanoocp.gp.gp_Dir:
        """
        Return normal at specified node index without face transformation applied.
        """

    def triangle(self, theElemIndex: int) -> nanoocp.Poly.Poly_Triangle:
        """Return triangle with specified index."""

class RWMesh_MaterialMap(nanoocp.Standard.Standard_Transient):
    """
    Material manager.
    Provides an interface for collecting all materials within the document before writing it into
    file, and for copying associated image files (textures) into sub-folder near by exported model.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DefaultStyle(self) -> nanoocp.XCAFPrs.XCAFPrs_Style:
        """
        Return default material definition to be used for nodes with only color defined.
        """

    def SetDefaultStyle(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> None:
        """
        Set default material definition to be used for nodes with only color defined.
        """

    def FindMaterial(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> nanoocp.TCollection.TCollection_AsciiString:
        """Find already registered material"""

    def AddMaterial(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style) -> nanoocp.TCollection.TCollection_AsciiString:
        """Register material and return its name identifier."""

    def CreateTextureFolder(self) -> bool:
        """
        Create texture folder "modelName/textures"; for example:
        MODEL:  Path/ModelName.gltf
        IMAGES: Path/ModelName/textures/
        Warning! Output folder is NOT cleared.
        """

    def CopyTexture(self, theResTexture: nanoocp.TCollection.TCollection_AsciiString, theTexture: nanoocp.Image.Image_Texture | None, theKey: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Copy and rename texture file to the new location.
        @param[out] theResTexture  result texture file path (relative to the model)
        @param[in] theTexture  original texture
        @param[in] theKey  material key
        """

    def DefineMaterial(self, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style, theKey: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Virtual method actually defining the material (e.g. export to the file).
        """

    def IsFailed(self) -> bool:
        """Return failed flag."""

class RWMesh_TriangulationReader(nanoocp.Standard.Standard_Transient):
    """Interface for reading primitive array from the buffer."""

    class LoadingStatistic:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: RWMesh_TriangulationReader.LoadingStatistic) -> None: ...

        def Reset(self) -> None: ...

        def PrintStatistic(self, thePrefix: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

        @property
        def ExpectedNodesNb(self) -> int: ...

        @ExpectedNodesNb.setter
        def ExpectedNodesNb(self, arg: int, /) -> None: ...

        @property
        def LoadedNodesNb(self) -> int: ...

        @LoadedNodesNb.setter
        def LoadedNodesNb(self, arg: int, /) -> None: ...

        @property
        def ExpectedTrianglesNb(self) -> int: ...

        @ExpectedTrianglesNb.setter
        def ExpectedTrianglesNb(self, arg: int, /) -> None: ...

        @property
        def DegeneratedTrianglesNb(self) -> int: ...

        @DegeneratedTrianglesNb.setter
        def DegeneratedTrianglesNb(self, arg: int, /) -> None: ...

        @property
        def LoadedTrianglesNb(self) -> int: ...

        @LoadedTrianglesNb.setter
        def LoadedTrianglesNb(self, arg: int, /) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def FileName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns file name for reporting issues."""

    def SetFileName(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets file name for reporting issues."""

    def CoordinateSystemConverter(self) -> RWMesh_CoordinateSystemConverter:
        """Returns coordinate system converter using for correct data loading."""

    def SetCoordinateSystemConverter(self, theConverter: RWMesh_CoordinateSystemConverter) -> None:
        """Sets coordinate system converter."""

    def IsDoublePrecision(self) -> bool:
        """
        Returns flag to fill in triangulation using double or single precision; FALSE by default.
        """

    def SetDoublePrecision(self, theIsDouble: bool) -> None:
        """Sets flag to fill in triangulation using double or single precision."""

    def ToSkipDegenerates(self) -> bool:
        """
        Returns TRUE if degenerated triangles should be skipped during mesh loading (only indexes will
        be checked).
        """

    def SetToSkipDegenerates(self, theToSkip: bool) -> None:
        """
        Sets flag to skip degenerated triangles during mesh loading (only indexes will be checked).
        """

    def ToPrintDebugMessages(self) -> bool:
        """Returns TRUE if additional debug information should be print."""

    def SetToPrintDebugMessages(self, theToPrint: bool) -> None:
        """Sets flag to print debug information."""

    def StartStatistic(self) -> None:
        """
        Starts and reset internal object that accumulates nodes/triangles statistic during data
        reading.
        """

    def StopStatistic(self) -> None:
        """
        Stops and nullify internal object that accumulates nodes/triangles statistic during data
        reading.
        """

    def PrintStatistic(self) -> None:
        """
        Prints loading statistic.
        This method should be used between StartStatistic() and StopStatistic() calls
        for correct results.
        """

    def Load(self, theSourceMesh: RWMesh_TriangulationSource | None, theDestMesh: nanoocp.Poly.Poly_Triangulation | None, theFileSystem: nanoocp.OSD.OSD_FileSystem | None) -> bool:
        """Loads primitive array."""

class RWMesh_TriangulationSource(nanoocp.Poly.Poly_Triangulation):
    """
    Mesh data wrapper for delayed triangulation loading.
    Class inherits Poly_Triangulation so that it can be put temporarily into TopoDS_Face within
    assembly structure.
    """

    def __init__(self) -> None:
        """Constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Reader(self) -> RWMesh_TriangulationReader:
        """Returns reader allowing to read data from the buffer."""

    def SetReader(self, theReader: RWMesh_TriangulationReader | None) -> None:
        """Sets reader allowing to read data from the buffer."""

    def DegeneratedTriNb(self) -> int:
        """
        Returns number of degenerated triangles collected during data reading.
        Used for debug statistic purpose.
        """

    def ChangeDegeneratedTriNb(self) -> int:
        """
        Gets access to number of degenerated triangles to collect them during data reading.
        """

    def SetDegeneratedTriNb(self, theValue: int) -> None:
        """
        Python addition: sets the value ChangeDegeneratedTriNb() returns by reference in C++.
        """

    def HasGeometry(self) -> bool:
        """Returns TRUE if triangulation has some geometry."""

    def NbEdges(self) -> int:
        """Returns the number of edges for this triangulation."""

    def Edge(self, theIndex: int) -> int:
        """
        Returns edge at the given index.
        @param[in] theIndex edge index within [1, NbEdges()] range
        @return edge node indices, with each node defined within [1, NbNodes()] range
        """

    def SetEdge(self, theIndex: int, theEdge: int) -> None:
        """
        Sets an edge.
        @param[in] theIndex edge index within [1, NbEdges()] range
        @param[in] theEdge edge node indices, with each node defined within [1, NbNodes()] range
        """

    def NbDeferredNodes(self) -> int:
        """
        @name late-load deferred data interface
        Returns number of nodes for deferred loading.
        Note: this is estimated values defined in object header, which might be different from
        actually loaded values (due to broken header or extra mesh processing). Always check
        triangulation size of actually loaded data in code to avoid out-of-range issues.
        """

    def SetNbDeferredNodes(self, theNbNodes: int) -> None:
        """Sets number of nodes for deferred loading."""

    def NbDeferredTriangles(self) -> int:
        """
        Returns number of triangles for deferred loading.
        Note: this is estimated values defined in object header, which might be different from
        actually loaded values (due to broken header or extra mesh processing). Always check
        triangulation size of actually loaded data in code to avoid out-of-range issues.
        """

    def SetNbDeferredTriangles(self, theNbTris: int) -> None:
        """Sets number of triangles for deferred loading."""

    def InternalEdges(self) -> nanoocp.NCollection.NCollection_Array1[int]:
        """
        Returns an internal array of edges.
        Edge()/SetEdge() should be used instead in portable code.
        """

    def ResizeEdges(self, theNbEdges: int, theToCopyOld: bool) -> None:
        """
        Method resizing an internal array of triangles.
        @param[in] theNbTriangles  new number of triangles
        @param[in] theToCopyOld    copy old triangles into the new array
        """

class RWMesh_VertexIterator(RWMesh_ShapeIterator):
    """
    Auxiliary class to iterate through vertices.
    Provides functionality to iterate through the vertices of a shape.
    It inherits from `RWMesh_ShapeIterator` and implements
    methods to access and manipulate vertex data.
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Auxiliary constructor.
        @param[in] theShape The shape to iterate.
        @param[in] theStyle The style of the shape.
        """

    @overload
    def __init__(self, theLabel: nanoocp.TDF.TDF_Label, theLocation: nanoocp.TopLoc.TopLoc_Location, theToMapColors: bool = False, theStyle: nanoocp.XCAFPrs.XCAFPrs_Style = ...) -> None:
        """
        Main constructor.
        @param[in] theLabel The label of the shape.
        @param[in] theLocation The location of the shape.
        @param[in] theToMapColors Flag to indicate if colors should be mapped.
        @param[in] theStyle The style of the shape.
        """

    def More(self) -> bool:
        """Return true if iterator points to the valid triangulation."""

    def Next(self) -> None:
        """Find next value."""

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Return current edge."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Return current vertex."""

    def Point(self) -> nanoocp.gp.gp_Pnt:
        """Return current vertex data."""

    def IsEmpty(self) -> bool:
        """Return true if geometry data is defined."""

    def ElemLower(self) -> int:
        """Lower element index in current triangulation."""

    def ElemUpper(self) -> int:
        """Upper element index in current triangulation."""

    def NbNodes(self) -> int:
        """Return number of nodes for the current edge."""

    def NodeLower(self) -> int:
        """Lower node index in current triangulation."""

    def NodeUpper(self) -> int:
        """Upper node index in current triangulation."""

    def node(self, arg0: int) -> nanoocp.gp.gp_Pnt:
        """Return the node with specified index with applied transformation."""
