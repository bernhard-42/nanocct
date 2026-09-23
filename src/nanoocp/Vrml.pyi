"""OCCT package Vrml (toolkit TKDEVRML)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class Vrml_AsciiTextJustification(enum.IntEnum):
    Vrml_LEFT = 0

    Vrml_CENTER = 1

    Vrml_RIGHT = 2

Vrml_LEFT: Vrml_AsciiTextJustification = Vrml_AsciiTextJustification.Vrml_LEFT

Vrml_CENTER: Vrml_AsciiTextJustification = Vrml_AsciiTextJustification.Vrml_CENTER

Vrml_RIGHT: Vrml_AsciiTextJustification = Vrml_AsciiTextJustification.Vrml_RIGHT

class Vrml_ConeParts(enum.IntEnum):
    Vrml_ConeSIDES = 0

    Vrml_ConeBOTTOM = 1

    Vrml_ConeALL = 2

Vrml_ConeSIDES: Vrml_ConeParts = Vrml_ConeParts.Vrml_ConeSIDES

Vrml_ConeBOTTOM: Vrml_ConeParts = Vrml_ConeParts.Vrml_ConeBOTTOM

Vrml_ConeALL: Vrml_ConeParts = Vrml_ConeParts.Vrml_ConeALL

class Vrml_CylinderParts(enum.IntEnum):
    Vrml_CylinderSIDES = 0

    Vrml_CylinderTOP = 1

    Vrml_CylinderBOTTOM = 2

    Vrml_CylinderALL = 3

Vrml_CylinderSIDES: Vrml_CylinderParts = Vrml_CylinderParts.Vrml_CylinderSIDES

Vrml_CylinderTOP: Vrml_CylinderParts = Vrml_CylinderParts.Vrml_CylinderTOP

Vrml_CylinderBOTTOM: Vrml_CylinderParts = Vrml_CylinderParts.Vrml_CylinderBOTTOM

Vrml_CylinderALL: Vrml_CylinderParts = Vrml_CylinderParts.Vrml_CylinderALL

class Vrml_FaceType(enum.IntEnum):
    Vrml_UNKNOWN_FACE_TYPE = 0

    Vrml_CONVEX = 1

Vrml_UNKNOWN_FACE_TYPE: Vrml_FaceType = Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE

Vrml_CONVEX: Vrml_FaceType = Vrml_FaceType.Vrml_CONVEX

class Vrml_FontStyleFamily(enum.IntEnum):
    Vrml_SERIF = 0

    Vrml_SANS = 1

    Vrml_TYPEWRITER = 2

Vrml_SERIF: Vrml_FontStyleFamily = Vrml_FontStyleFamily.Vrml_SERIF

Vrml_SANS: Vrml_FontStyleFamily = Vrml_FontStyleFamily.Vrml_SANS

Vrml_TYPEWRITER: Vrml_FontStyleFamily = Vrml_FontStyleFamily.Vrml_TYPEWRITER

class Vrml_FontStyleStyle(enum.IntEnum):
    Vrml_NONE = 0

    Vrml_BOLD = 1

    Vrml_ITALIC = 2

Vrml_NONE: Vrml_FontStyleStyle = Vrml_FontStyleStyle.Vrml_NONE

Vrml_BOLD: Vrml_FontStyleStyle = Vrml_FontStyleStyle.Vrml_BOLD

Vrml_ITALIC: Vrml_FontStyleStyle = Vrml_FontStyleStyle.Vrml_ITALIC

class Vrml_MaterialBindingAndNormalBinding(enum.IntEnum):
    Vrml_DEFAULT = 0

    Vrml_OVERALL = 1

    Vrml_PER_PART = 2

    Vrml_PER_PART_INDEXED = 3

    Vrml_PER_FACE = 4

    Vrml_PER_FACE_INDEXED = 5

    Vrml_PER_VERTEX = 6

    Vrml_PER_VERTEX_INDEXED = 7

Vrml_DEFAULT: Vrml_MaterialBindingAndNormalBinding = Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT

Vrml_OVERALL: Vrml_MaterialBindingAndNormalBinding = Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL

Vrml_PER_PART: Vrml_MaterialBindingAndNormalBinding = ...

Vrml_PER_PART_INDEXED: Vrml_MaterialBindingAndNormalBinding = ...

Vrml_PER_FACE: Vrml_MaterialBindingAndNormalBinding = ...

Vrml_PER_FACE_INDEXED: Vrml_MaterialBindingAndNormalBinding = ...

Vrml_PER_VERTEX: Vrml_MaterialBindingAndNormalBinding = ...

Vrml_PER_VERTEX_INDEXED: Vrml_MaterialBindingAndNormalBinding = ...

class Vrml_SeparatorRenderCulling(enum.IntEnum):
    Vrml_OFF = 0

    Vrml_ON = 1

    Vrml_AUTO = 2

Vrml_OFF: Vrml_SeparatorRenderCulling = Vrml_SeparatorRenderCulling.Vrml_OFF

Vrml_ON: Vrml_SeparatorRenderCulling = Vrml_SeparatorRenderCulling.Vrml_ON

Vrml_AUTO: Vrml_SeparatorRenderCulling = Vrml_SeparatorRenderCulling.Vrml_AUTO

class Vrml_SFImageNumber(enum.IntEnum):
    """qualifies VRML geometry shapes."""

    Vrml_NULL = 0

    Vrml_ONE = 1

    Vrml_TWO = 2

    Vrml_THREE = 3

    Vrml_FOUR = 4

Vrml_NULL: Vrml_SFImageNumber = Vrml_SFImageNumber.Vrml_NULL

Vrml_ONE: Vrml_SFImageNumber = Vrml_SFImageNumber.Vrml_ONE

Vrml_TWO: Vrml_SFImageNumber = Vrml_SFImageNumber.Vrml_TWO

Vrml_THREE: Vrml_SFImageNumber = Vrml_SFImageNumber.Vrml_THREE

Vrml_FOUR: Vrml_SFImageNumber = Vrml_SFImageNumber.Vrml_FOUR

class Vrml_VertexOrdering(enum.IntEnum):
    Vrml_UNKNOWN_ORDERING = 0

    Vrml_CLOCKWISE = 1

    Vrml_COUNTERCLOCKWISE = 2

Vrml_UNKNOWN_ORDERING: Vrml_VertexOrdering = Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING

Vrml_CLOCKWISE: Vrml_VertexOrdering = Vrml_VertexOrdering.Vrml_CLOCKWISE

Vrml_COUNTERCLOCKWISE: Vrml_VertexOrdering = Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE

class Vrml_ShapeType(enum.IntEnum):
    Vrml_UNKNOWN_SHAPE_TYPE = 0

    Vrml_SOLID = 1

Vrml_UNKNOWN_SHAPE_TYPE: Vrml_ShapeType = Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE

Vrml_SOLID: Vrml_ShapeType = Vrml_ShapeType.Vrml_SOLID

class Vrml_Texture2Wrap(enum.IntEnum):
    Vrml_REPEAT = 0

    Vrml_CLAMP = 1

Vrml_REPEAT: Vrml_Texture2Wrap = Vrml_Texture2Wrap.Vrml_REPEAT

Vrml_CLAMP: Vrml_Texture2Wrap = Vrml_Texture2Wrap.Vrml_CLAMP

class Vrml_WWWAnchorMap(enum.IntEnum):
    Vrml_MAP_NONE = 0

    Vrml_POINT = 1

Vrml_MAP_NONE: Vrml_WWWAnchorMap = Vrml_WWWAnchorMap.Vrml_MAP_NONE

Vrml_POINT: Vrml_WWWAnchorMap = Vrml_WWWAnchorMap.Vrml_POINT

class Vrml:
    """
    Vrml package implements the specification of the
    VRML (Virtual Reality Modeling Language ). VRML
    is a standard language for describing interactive
    3-D objects and worlds delivered across Internet.
    Actual version of Vrml package have made for objects
    of VRML version 1.0.
    This package is used by VrmlConverter package.
    The developer should already be familiar with VRML
    specification before using this package.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Vrml) -> None: ...

    @staticmethod
    def VrmlHeaderWriter() -> str:
        """
        Writes a header in anOStream (VRML file).
        Writes one line of commentary in anOStream (VRML file).
        """

    @staticmethod
    def CommentWriter(aComment: str) -> str: ...

class Vrml_AsciiText(nanoocp.Standard.Standard_Transient):
    """
    defines a AsciiText node of VRML specifying geometry shapes.
    This node represents strings of text characters from ASCII coded
    character set. All subsequent strings advance y by -( size * spacing).
    The justification field determines the placement of the strings in the x
    dimension. LEFT (the default) places the left edge of each string at x=0.
    CENTER places the center of each string at x=0. RIGHT places the right edge
    of each string at x=0. Text is rendered from left to right, top to
    bottom in the font set by FontStyle.
    The default value for the wigth field indicates the natural width
    should be used for that string.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aString: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString] | None, aSpacing: float, aJustification: Vrml_AsciiTextJustification, aWidth: float) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_AsciiText) -> None: ...

    def SetString(self, aString: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString] | None) -> None: ...

    def String(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString]: ...

    def SetSpacing(self, aSpacing: float) -> None: ...

    def Spacing(self) -> float: ...

    def SetJustification(self, aJustification: Vrml_AsciiTextJustification) -> None: ...

    def Justification(self) -> Vrml_AsciiTextJustification: ...

    def SetWidth(self, aWidth: float) -> None: ...

    def Width(self) -> float: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_Cone:
    """
    defines a Cone node of VRML specifying geometry shapes.
    This node represents a simple cone, whose central axis is aligned
    with the y-axis. By default, the cone is centred at (0,0,0)
    and has size of -1 to +1 in the all three directions.
    the cone has a radius of 1 at the bottom and height of 2,
    with its apex at 1 and its bottom at -1. The cone has two parts:
    the sides and the bottom
    """

    @overload
    def __init__(self, aParts: Vrml_ConeParts = Vrml_ConeParts.Vrml_ConeALL, aBottomRadius: float = 1.0, aHeight: float = 2.0) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Cone) -> None: ...

    def SetParts(self, aParts: Vrml_ConeParts) -> None: ...

    def Parts(self) -> Vrml_ConeParts: ...

    def SetBottomRadius(self, aBottomRadius: float) -> None: ...

    def BottomRadius(self) -> float: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_Coordinate3(nanoocp.Standard.Standard_Transient):
    """
    defines a Coordinate3 node of VRML specifying
    properties of geometry and its appearance.
    This node defines a set of 3D coordinates to be used by a subsequent IndexedFaceSet,
    IndexedLineSet, or PointSet node. This node does not produce a visible result
    during rendering; it simply replaces the current coordinates in the rendering
    state for subsequent nodes to use.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aPoint: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Coordinate3) -> None: ...

    def SetPoint(self, aPoint: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec] | None) -> None: ...

    def Point(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_Cube:
    """
    defines a Cube node of VRML specifying geometry shapes.
    This node represents a cuboid aligned with the coordinate axes.
    By default, the cube is centred at (0,0,0) and measures 2 units
    in each dimension, from -1 to +1.
    A cube's width is its extent along its object-space X axis, its height is
    its extent along the object-space Y axis, and its depth is its extent along its
    object-space Z axis.
    """

    @overload
    def __init__(self, aWidth: float = 2.0, aHeight: float = 2.0, aDepth: float = 2.0) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Cube) -> None: ...

    def SetWidth(self, aWidth: float) -> None: ...

    def Width(self) -> float: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def SetDepth(self, aDepth: float) -> None: ...

    def Depth(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_Cylinder:
    """
    defines a Cylinder node of VRML specifying geometry shapes.
    This node represents a simple capped cylinder centred around the y-axis.
    By default, the cylinder is centred at (0,0,0)
    and has size of -1 to +1 in the all three dimensions.
    The cylinder has three parts:
    the sides, the top (y=+1) and the bottom (y=-1)
    """

    @overload
    def __init__(self, aParts: Vrml_CylinderParts = Vrml_CylinderParts.Vrml_CylinderALL, aRadius: float = 1.0, aHeight: float = 2.0) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Cylinder) -> None: ...

    def SetParts(self, aParts: Vrml_CylinderParts) -> None: ...

    def Parts(self) -> Vrml_CylinderParts: ...

    def SetRadius(self, aRadius: float) -> None: ...

    def Radius(self) -> float: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_DirectionalLight:
    """
    defines a directional light node of VRML specifying
    properties of lights.
    This node defines a directional light source that illuminates
    along rays parallel to a given 3-dimensional vector
    Color is written as an RGB triple.
    Light intensity must be in the range 0.0 to 1.0, inclusive.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aOnOff: bool, aIntensity: float, aColor: nanoocp.Quantity.Quantity_Color, aDirection: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_DirectionalLight) -> None: ...

    def SetOnOff(self, aOnOff: bool) -> None: ...

    def OnOff(self) -> bool: ...

    def SetIntensity(self, aIntensity: float) -> None: ...

    def Intensity(self) -> float: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def Color(self) -> nanoocp.Quantity.Quantity_Color: ...

    def SetDirection(self, aDirection: nanoocp.gp.gp_Vec) -> None: ...

    def Direction(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

class Vrml_FontStyle:
    """
    defines a FontStyle node of VRML of properties of geometry
    and its appearance.
    The size field specifies the height (in object space units)
    of glyphs rendered and determines the vertical spacing of
    adjacent lines of text.
    """

    @overload
    def __init__(self, aSize: float = 10.0, aFamily: Vrml_FontStyleFamily = Vrml_FontStyleFamily.Vrml_SERIF, aStyle: Vrml_FontStyleStyle = Vrml_FontStyleStyle.Vrml_NONE) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_FontStyle) -> None: ...

    def SetSize(self, aSize: float) -> None: ...

    def Size(self) -> float: ...

    def SetFamily(self, aFamily: Vrml_FontStyleFamily) -> None: ...

    def Family(self) -> Vrml_FontStyleFamily: ...

    def SetStyle(self, aStyle: Vrml_FontStyleStyle) -> None: ...

    def Style(self) -> Vrml_FontStyleStyle: ...

    def Print(self) -> str: ...

class Vrml_Group:
    """
    defines a Group node of VRML specifying group properties.
    This node defines the base class for all group nodes. Group is a node that
    contains an ordered list of child nodes. This node is simply a container for
    the child nodes and does not alter the traversal state in any way.
    During traversal, state accumulated for a child is passed on to each successive
    child and then to the parents of the group (Group does not push or pop traversal
    state as separator does).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Group) -> None: ...

    def Print(self) -> str: ...

class Vrml_IndexedFaceSet(nanoocp.Standard.Standard_Transient):
    """
    defines a IndexedFaceSet node of VRML specifying geometry shapes.
    This node represents a 3D shape formed by constructing faces (polygons) from
    vertices located at the current coordinates. IndexedFaceSet uses the indices
    in its coordIndex to define polygonal faces. An index of -1 separates faces
    (so a -1 at the end of the list is optional).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aMaterialIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aNormalIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aTextureCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_IndexedFaceSet) -> None: ...

    def SetCoordIndex(self, aCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def CoordIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetMaterialIndex(self, aMaterialIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def MaterialIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetNormalIndex(self, aNormalIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def NormalIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetTextureCoordIndex(self, aTextureCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def TextureCoordIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_IndexedLineSet(nanoocp.Standard.Standard_Transient):
    """
    defines a IndexedLineSet node of VRML specifying geometry shapes.
    This node represents a 3D shape formed by constructing polylines from vertices
    located at the current coordinates. IndexedLineSet uses the indices in its coordIndex
    field to specify the polylines. An index of -1 separates one polyline from the next
    (thus, a final -1 is optional). the current polyline has ended and the next one begins.
    Treatment of the current material and normal binding is as follows: The PER_PART binding
    specifies a material or normal for each segment of the line. The PER_FACE binding
    specifies a material or normal for each polyline. PER_VERTEX specifies a material or
    normal for each vertex. The corresponding _INDEXED bindings are the same, but use
    the materialIndex or normalIndex indices. The DEFAULT material binding is equal
    to OVERALL. The DEFAULT normal binding is equal to PER_VERTEX_INDEXED;
    if insufficient normals exist in the state, the lines will be drawn unlit. The same
    rules for texture coordinate generation as IndexedFaceSet are used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aMaterialIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aNormalIndex: nanoocp.NCollection.NCollection_HArray1[int] | None, aTextureCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_IndexedLineSet) -> None: ...

    def SetCoordIndex(self, aCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def CoordIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetMaterialIndex(self, aMaterialIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def MaterialIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetNormalIndex(self, aNormalIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def NormalIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def SetTextureCoordIndex(self, aTextureCoordIndex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def TextureCoordIndex(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_Info:
    """
    defines a Info node of VRML specifying properties of geometry
    and its appearance.
    It is used to store information in the scene graph,
    Typically for application-specific purposes, copyright messages,
    or other strings.
    """

    @overload
    def __init__(self, aString: nanoocp.TCollection.TCollection_AsciiString = ...) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Info) -> None: ...

    def SetString(self, aString: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def String(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def Print(self) -> str: ...

class Vrml_Instancing:
    """
    defines "instancing" - using the same instance of a node
    multiple times.
    It is accomplished by using the "DEF" and "USE" keywords.
    The DEF keyword both defines a named node, and creates a single
    instance of it.
    The USE keyword indicates that the most recently defined instance
    should be used again.
    If several nades were given the same name, then the last DEF
    encountered during parsing "wins".
    DEF/USE is limited to a single file.
    """

    @overload
    def __init__(self, aString: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Adds "DEF <myName>" in anOStream (VRML file)."""

    @overload
    def __init__(self, theOther: Vrml_Instancing) -> None: ...

    def DEF(self) -> str:
        """Adds "USE <myName>" in anOStream (VRML file)."""

    def USE(self) -> str: ...

class Vrml_LOD(nanoocp.Standard.Standard_Transient):
    """
    defines a LOD (level of detailization) node of VRML specifying properties
    of geometry and its appearance.
    This group node is used to allow applications to switch between
    various representations of objects automatically. The children of this
    node typically represent the same object or objects at the varying
    of Levels Of Detail (LOD), from highest detail to lowest.

    The specified center point of the LOD is transformed by current
    transformation into world space, and the distance from the transformed
    center to the world-space eye point is calculated.
    If thedistance is less than the first value in the ranges array,
    than the first child of the LOD group is drawn. If between
    the first and second values in the range array, the second child
    is drawn, etc.
    If there are N values in the range array, the LOD group should
    have N+1 children.
    Specifying too few children will result in the last child being
    used repeatedly for the lowest levels of detail; if too many children
    are specified, the extra children will be ignored.
    Each value in the ranges array should be greater than the previous
    value, otherwise results are undefined.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aRange: nanoocp.NCollection.NCollection_HArray1[float] | None, aCenter: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_LOD) -> None: ...

    def SetRange(self, aRange: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    def Range(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def SetCenter(self, aCenter: nanoocp.gp.gp_Vec) -> None: ...

    def Center(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_Material(nanoocp.Standard.Standard_Transient):
    """
    defines a Material node of VRML specifying properties of geometry
    and its appearance.
    This node defines the current surface material properties for all subsequent shapes.
    Material sets several components of the current material during traversal. Different shapes
    interpret materials with multiple values differently. To bind materials to shapes, use a
    MaterialBinding node.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aAmbientColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None, aDiffuseColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None, aSpecularColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None, aEmissiveColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None, aShininess: nanoocp.NCollection.NCollection_HArray1[float] | None, aTransparency: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Material) -> None: ...

    def SetAmbientColor(self, aAmbientColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> None: ...

    def AmbientColor(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color]: ...

    def SetDiffuseColor(self, aDiffuseColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> None: ...

    def DiffuseColor(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color]: ...

    def SetSpecularColor(self, aSpecularColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> None: ...

    def SpecularColor(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color]: ...

    def SetEmissiveColor(self, aEmissiveColor: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None) -> None: ...

    def EmissiveColor(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color]: ...

    def SetShininess(self, aShininess: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    def Shininess(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def SetTransparency(self, aTransparency: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None: ...

    def Transparency(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_MaterialBinding:
    """
    defines a MaterialBinding node of VRML specifying properties of geometry
    and its appearance.
    Material nodes may contain more than one material. This node specifies how the current
    materials are bound to shapes that follow in the scene graph. Each shape node may
    interpret bindings differently. For example, a Sphere node is always drawn using the first
    material in the material node, no matter what the current MaterialBinding, while a Cube
    node may use six different materials to draw each of its six faces, depending on the
    MaterialBinding.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_MaterialBinding) -> None: ...

    def SetValue(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...

    def Value(self) -> Vrml_MaterialBindingAndNormalBinding: ...

    def Print(self) -> str: ...

class Vrml_MatrixTransform:
    """
    defines a MatrixTransform node of VRML specifying matrix and transform
    properties.
    This node defines 3D transformation with a 4 by 4 matrix.
    By default:
    a11=1  a12=0  a13=0  a14=0
    a21=0  a22=1  a23=0  a24=0
    a31=0  a32=0  a33=1  a34=0
    a41=0  a42=0  a43=0  a44=1
    It is written to the file in row-major order as 16 Real numbers
    separated by whitespace. For example , matrix expressing a translation
    of 7.3 units along the X axis is written as:
    1  0  0  0   0  1  0  0   0  0  1  0   7.3 0  0  1
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aMatrix: nanoocp.gp.gp_Trsf) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_MatrixTransform) -> None: ...

    def SetMatrix(self, aMatrix: nanoocp.gp.gp_Trsf) -> None: ...

    def Matrix(self) -> nanoocp.gp.gp_Trsf: ...

    def Print(self) -> str: ...

class Vrml_Normal(nanoocp.Standard.Standard_Transient):
    """
    defines a Normal node of VRML specifying properties of geometry
    and its appearance.
    This node defines a set of 3D surface normal vectors to be used by vertex-based shape
    nodes (IndexedFaceSet, IndexedLineSet, PointSet) that follow it in the scene graph. This
    node does not produce a visible result during rendering; it simply replaces the current
    normals in the rendering state for subsequent nodes to use. This node contains one
    multiple-valued field that contains the normal vectors.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aVector: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Normal) -> None: ...

    def SetVector(self, aVector: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec] | None) -> None: ...

    def Vector(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_NormalBinding:
    """
    defines a NormalBinding node of VRML specifying properties of geometry
    and its appearance.
    This node specifies how the current normals are bound to shapes that follow in the scene
    graph. Each shape node may interpret bindings differently.
    The bindings for faces and vertices are meaningful only for shapes that are made from
    faces and vertices. Similarly, the indexed bindings are only used by the shapes that allow
    indexing. For bindings that require multiple normals, be sure to have at least as many
    normals defined as are necessary; otherwise, errors will occur.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_NormalBinding) -> None: ...

    def SetValue(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...

    def Value(self) -> Vrml_MaterialBindingAndNormalBinding: ...

    def Print(self) -> str: ...

class Vrml_SFRotation:
    """
    defines SFRotation type of VRML field types.
    The 4 values represent an axis of rotation followed by amount of
    right-handed rotation about the that axis, in radians.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aRotationX: float, aRotationY: float, aRotationZ: float, anAngle: float) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_SFRotation) -> None: ...

    def SetRotationX(self, aRotationX: float) -> None: ...

    def RotationX(self) -> float: ...

    def SetRotationY(self, aRotationY: float) -> None: ...

    def RotationY(self) -> float: ...

    def SetRotationZ(self, aRotationZ: float) -> None: ...

    def RotationZ(self) -> float: ...

    def SetAngle(self, anAngle: float) -> None: ...

    def Angle(self) -> float: ...

class Vrml_OrthographicCamera:
    """
    specifies a OrthographicCamera node of VRML specifying properties of cameras.
    An orthographic camera defines a parallel projection from a viewpoint. This camera does
    not diminish objects with distance, as a PerspectiveCamera does. The viewing volume for
    an orthographic camera is a rectangular parallelepiped (a box).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aPosition: nanoocp.gp.gp_Vec, aOrientation: Vrml_SFRotation, aFocalDistance: float, aHeight: float) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_OrthographicCamera) -> None: ...

    def SetPosition(self, aPosition: nanoocp.gp.gp_Vec) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Vec: ...

    def SetOrientation(self, aOrientation: Vrml_SFRotation) -> None: ...

    def Orientation(self) -> Vrml_SFRotation: ...

    def SetFocalDistance(self, aFocalDistance: float) -> None: ...

    def FocalDistance(self) -> float: ...

    def SetHeight(self, aHeight: float) -> None: ...

    def Height(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_PerspectiveCamera:
    """
    specifies a PerspectiveCamera node of VRML specifying properties of cameras.
    A perspective camera defines a perspective projection from a viewpoint. The viewing
    volume for a perspective camera is a truncated right pyramid.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aPosition: nanoocp.gp.gp_Vec, aOrientation: Vrml_SFRotation, aFocalDistance: float, aHeightAngle: float) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_PerspectiveCamera) -> None: ...

    def SetPosition(self, aPosition: nanoocp.gp.gp_Vec) -> None: ...

    def Position(self) -> nanoocp.gp.gp_Vec: ...

    def SetOrientation(self, aOrientation: Vrml_SFRotation) -> None: ...

    def Orientation(self) -> Vrml_SFRotation: ...

    def SetFocalDistance(self, aFocalDistance: float) -> None: ...

    def FocalDistance(self) -> float: ...

    def SetAngle(self, aHeightAngle: float) -> None: ...

    def Angle(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_PointLight:
    """
    defines a point light node of VRML specifying
    properties of lights.
    This node defines a point light source at a fixed 3D location
    A point source illuminates equally in all directions;
    that is omni-directional.
    Color is written as an RGB triple.
    Light intensity must be in the range 0.0 to 1.0, inclusive.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aOnOff: bool, aIntensity: float, aColor: nanoocp.Quantity.Quantity_Color, aLocation: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_PointLight) -> None: ...

    def SetOnOff(self, aOnOff: bool) -> None: ...

    def OnOff(self) -> bool: ...

    def SetIntensity(self, aIntensity: float) -> None: ...

    def Intensity(self) -> float: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def Color(self) -> nanoocp.Quantity.Quantity_Color: ...

    def SetLocation(self, aLocation: nanoocp.gp.gp_Vec) -> None: ...

    def Location(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

class Vrml_PointSet:
    """defines a PointSet node of VRML specifying geometry shapes."""

    @overload
    def __init__(self, aStartIndex: int = 0, aNumPoints: int = -1) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_PointSet) -> None: ...

    def SetStartIndex(self, aStartIndex: int) -> None: ...

    def StartIndex(self) -> int: ...

    def SetNumPoints(self, aNumPoints: int) -> None: ...

    def NumPoints(self) -> int: ...

    def Print(self) -> str: ...

class Vrml_Rotation:
    """
    defines a Rotation node of VRML specifying matrix and transform properties.
    This node defines a 3D rotation about an arbitrary axis through the origin.
    Bydefault: myRotation = (0 0 1 0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aRotation: Vrml_SFRotation) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Rotation) -> None: ...

    def SetRotation(self, aRotation: Vrml_SFRotation) -> None: ...

    def Rotation(self) -> Vrml_SFRotation: ...

    def Print(self) -> str: ...

class Vrml_Scale:
    """
    defines a Scale node of VRML specifying transform
    properties.
    This node defines a 3D scaling about the origin.
    By default:
    myRotation = (1 1 1)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aScaleFactor: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Scale) -> None: ...

    def SetScaleFactor(self, aScaleFactor: nanoocp.gp.gp_Vec) -> None: ...

    def ScaleFactor(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

class Vrml_Separator:
    """
    defines a Separator node of VRML specifying group properties.
    This group node performs a push (save) of the traversal state before traversing its children
    and a pop (restore) after traversing them. This isolates the separator's children from the
    rest of the scene graph. A separator can include lights, cameras, coordinates, normals,
    bindings, and all other properties.
    Separators can also perform render culling. Render culling skips over traversal of the
    separator's children if they are not going to be rendered, based on the comparison of the
    separator's bounding box with the current view volume. Culling is controlled by the
    renderCulling field. These are set to AUTO by default, allowing the implementation to
    decide whether or not to cull.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aRenderCulling: Vrml_SeparatorRenderCulling) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Separator) -> None: ...

    def SetRenderCulling(self, aRenderCulling: Vrml_SeparatorRenderCulling) -> None: ...

    def RenderCulling(self) -> Vrml_SeparatorRenderCulling: ...

    def Print(self) -> str: ...

class Vrml_SFImage(nanoocp.Standard.Standard_Transient):
    """defines SFImage type of VRML field types."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aWidth: int, aHeight: int, aNumber: Vrml_SFImageNumber, anArray: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_SFImage) -> None: ...

    def SetWidth(self, aWidth: int) -> None: ...

    def Width(self) -> int: ...

    def SetHeight(self, aHeight: int) -> None: ...

    def Height(self) -> int: ...

    def SetNumber(self, aNumber: Vrml_SFImageNumber) -> None: ...

    def Number(self) -> Vrml_SFImageNumber: ...

    def SetArray(self, anArray: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None: ...

    def Array(self) -> nanoocp.NCollection.NCollection_HArray1[int]: ...

    def ArrayFlag(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_ShapeHints:
    """
    defines a ShapeHints node of VRML specifying properties of geometry and its appearance.
    The ShapeHints node indicates that IndexedFaceSets are solid, contain ordered vertices, or
    contain convex faces.
    These hints allow VRML implementations to optimize certain rendering features.
    Optimizations that may be performed include enabling back-face culling and disabling
    two-sided lighting. For example, if an object is solid and has ordered vertices, an
    implementation may turn on backface culling and turn off two-sided lighting. To ensure
    that an IndexedFaceSet can be viewed from either direction, set shapeType to be
    UNKNOWN_SHAPE_TYPE.
    If you know that your shapes are closed and will alwsys be viewed from the outside, set
    vertexOrdering to be either CLOCKWISE or COUNTERCLOCKWISE (depending on
    how you built your object), and set shapeType to be SOLID. Placing this near the top of
    your VRML file will allow the scene to be rendered much faster.
    The ShapeHints node also affects how default normals are generated. When an
    IndexedFaceSet has to generate default normals, it uses the creaseAngle field to determine
    which edges should be smoothly shaded and which ones should have a sharp crease. The
    crease angle is the angle between surface normals on adjacent polygons. For example, a
    crease angle of .5 radians (the default value) means that an edge between two adjacent
    polygonal faces will be smooth shaded if the normals to the two faces form an angle that is
    less than .5 radians (about 30 degrees). Otherwise, it will be faceted.
    """

    @overload
    def __init__(self, aVertexOrdering: Vrml_VertexOrdering = Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING, aShapeType: Vrml_ShapeType = Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE, aFaceType: Vrml_FaceType = Vrml_FaceType.Vrml_CONVEX, aAngle: float = 0.5) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_ShapeHints) -> None: ...

    def SetVertexOrdering(self, aVertexOrdering: Vrml_VertexOrdering) -> None: ...

    def VertexOrdering(self) -> Vrml_VertexOrdering: ...

    def SetShapeType(self, aShapeType: Vrml_ShapeType) -> None: ...

    def ShapeType(self) -> Vrml_ShapeType: ...

    def SetFaceType(self, aFaceType: Vrml_FaceType) -> None: ...

    def FaceType(self) -> Vrml_FaceType: ...

    def SetAngle(self, aAngle: float) -> None: ...

    def Angle(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_Sphere:
    """
    defines a Sphere node of VRML specifying geometry shapes.
    This node represents a sphere.
    By default, the sphere is centred at (0,0,0) and has a radius of 1.
    """

    @overload
    def __init__(self, aRadius: float = 1.0) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Sphere) -> None: ...

    def SetRadius(self, aRadius: float) -> None: ...

    def Radius(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_SpotLight:
    """
    specifies a spot light node of VRML nodes specifying
    properties of lights.
    This node defines a spotlight light source.
    A spotlight is placed at a fixed location in 3D-space
    and illuminates in a cone along a particular direction.
    The intensity of the illumination drops off exponentially
    as a ray of light diverges from this direction toward
    the edges of cone.
    The rate of drop-off and agle of the cone are controlled
    by the dropOfRate and cutOffAngle
    Color is written as an RGB triple.
    Light intensity must be in the range 0.0 to 1.0, inclusive.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aOnOff: bool, aIntensity: float, aColor: nanoocp.Quantity.Quantity_Color, aLocation: nanoocp.gp.gp_Vec, aDirection: nanoocp.gp.gp_Vec, aDropOffRate: float, aCutOffAngle: float) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_SpotLight) -> None: ...

    def SetOnOff(self, anOnOff: bool) -> None: ...

    def OnOff(self) -> bool: ...

    def SetIntensity(self, aIntensity: float) -> None: ...

    def Intensity(self) -> float: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def Color(self) -> nanoocp.Quantity.Quantity_Color: ...

    def SetLocation(self, aLocation: nanoocp.gp.gp_Vec) -> None: ...

    def Location(self) -> nanoocp.gp.gp_Vec: ...

    def SetDirection(self, aDirection: nanoocp.gp.gp_Vec) -> None: ...

    def Direction(self) -> nanoocp.gp.gp_Vec: ...

    def SetDropOffRate(self, aDropOffRate: float) -> None: ...

    def DropOffRate(self) -> float: ...

    def SetCutOffAngle(self, aCutOffAngle: float) -> None: ...

    def CutOffAngle(self) -> float: ...

    def Print(self) -> str: ...

class Vrml_Switch:
    """
    defines a Switch node of VRML specifying group properties.
    This group node traverses one, none, or all of its children.
    One can use this node to switch on and off the effects of some
    properties or to switch between different properties.
    The whichChild field specifies the index of the child to traverse,
    where the first child has index 0.
    A value of -1 (the default) means do not traverse any children.
    A value of -3 traverses all children, making the switch behave exactly
    like a regular Group.
    """

    @overload
    def __init__(self, aWhichChild: int = -1) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Switch) -> None: ...

    def SetWhichChild(self, aWhichChild: int) -> None: ...

    def WhichChild(self) -> int: ...

    def Print(self) -> str: ...

class Vrml_Texture2:
    """
    defines a Texture2 node of VRML specifying properties of geometry
    and its appearance.
    This property node defines a texture map and parameters for that map
    The texture can be read from the URL specified by the filename field.
    To turn off texturing, set the filename field to an empty string ("").
    Textures can alsobe specified inline by setting the image field
    to contain the texture data.
    By default:
    myFilename ("")
    myImage (0 0 0)
    myWrapS (Vrml_REPEAT)
    myWrapT (Vrml_REPEAT)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aFilename: nanoocp.TCollection.TCollection_AsciiString, aImage: Vrml_SFImage | None, aWrapS: Vrml_Texture2Wrap, aWrapT: Vrml_Texture2Wrap) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Texture2) -> None: ...

    def SetFilename(self, aFilename: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Filename(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetImage(self, aImage: Vrml_SFImage | None) -> None: ...

    def Image(self) -> Vrml_SFImage: ...

    def SetWrapS(self, aWrapS: Vrml_Texture2Wrap) -> None: ...

    def WrapS(self) -> Vrml_Texture2Wrap: ...

    def SetWrapT(self, aWrapT: Vrml_Texture2Wrap) -> None: ...

    def WrapT(self) -> Vrml_Texture2Wrap: ...

    def Print(self) -> str: ...

class Vrml_Texture2Transform:
    """
    defines a Texture2Transform node of VRML specifying properties of geometry
    and its appearance.
    This node defines a 2D transformation applied to texture coordinates.
    This affect the way textures are applied to the surfaces of subsequent
    shapes.
    Transformation consisits of (in order) a non-uniform scale about an
    arbitrary center point, a rotation about that same point, and
    a translation. This allows a user to change the size and position of
    the textures on the shape.
    By default:
    myTranslation (0 0)
    myRotation (0)
    myScaleFactor (1 1)
    myCenter (0 0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aTranslation: nanoocp.gp.gp_Vec2d, aRotation: float, aScaleFactor: nanoocp.gp.gp_Vec2d, aCenter: nanoocp.gp.gp_Vec2d) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Texture2Transform) -> None: ...

    def SetTranslation(self, aTranslation: nanoocp.gp.gp_Vec2d) -> None: ...

    def Translation(self) -> nanoocp.gp.gp_Vec2d: ...

    def SetRotation(self, aRotation: float) -> None: ...

    def Rotation(self) -> float: ...

    def SetScaleFactor(self, aScaleFactor: nanoocp.gp.gp_Vec2d) -> None: ...

    def ScaleFactor(self) -> nanoocp.gp.gp_Vec2d: ...

    def SetCenter(self, aCenter: nanoocp.gp.gp_Vec2d) -> None: ...

    def Center(self) -> nanoocp.gp.gp_Vec2d: ...

    def Print(self) -> str: ...

class Vrml_TextureCoordinate2(nanoocp.Standard.Standard_Transient):
    """
    defines a TextureCoordinate2 node of VRML specifying properties of geometry
    and its appearance.
    This node defines a set of 2D coordinates to be used to map textures
    to the vertices of subsequent PointSet, IndexedLineSet, or IndexedFaceSet
    objects. It replaces the current texture coordinates in the rendering
    state for the shapes to use.
    Texture coordinates range from 0 to 1 across the texture.
    The horizontal coordinate, called S, is specified first, followed
    by vertical coordinate, T.
    By default:
    myPoint (0 0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aPoint: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec2d] | None) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_TextureCoordinate2) -> None: ...

    def SetPoint(self, aPoint: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec2d] | None) -> None: ...

    def Point(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Vec2d]: ...

    def Print(self) -> str: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Vrml_Transform:
    """
    defines a Transform of VRML specifying transform
    properties.
    This node defines a geometric 3D transformation consisting of (in order)
    a (possibly) non-uniform scale about an arbitrary point, a rotation about
    an arbitrary point and axis and translation.
    By default:
    myTranslation (0,0,0)
    myRotation  (0,0,1,0)
    myScaleFactor (1,1,1)
    myScaleOrientation (0,0,1,0)
    myCenter (0,0,0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aTranslation: nanoocp.gp.gp_Vec, aRotation: Vrml_SFRotation, aScaleFactor: nanoocp.gp.gp_Vec, aScaleOrientation: Vrml_SFRotation, aCenter: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Transform) -> None: ...

    def SetTranslation(self, aTranslation: nanoocp.gp.gp_Vec) -> None: ...

    def Translation(self) -> nanoocp.gp.gp_Vec: ...

    def SetRotation(self, aRotation: Vrml_SFRotation) -> None: ...

    def Rotation(self) -> Vrml_SFRotation: ...

    def SetScaleFactor(self, aScaleFactor: nanoocp.gp.gp_Vec) -> None: ...

    def ScaleFactor(self) -> nanoocp.gp.gp_Vec: ...

    def SetScaleOrientation(self, aScaleOrientation: Vrml_SFRotation) -> None: ...

    def ScaleOrientation(self) -> Vrml_SFRotation: ...

    def SetCenter(self, aCenter: nanoocp.gp.gp_Vec) -> None: ...

    def Center(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

class Vrml_TransformSeparator:
    """
    defines a TransformSeparator node of VRML specifying group properties.
    This group node is similar to separator node in that it saves state
    before traversing its children and restores it afterwards.
    This node can be used to isolate transformations to light sources
    or objects.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_TransformSeparator) -> None: ...

    def Print(self) -> str: ...

class Vrml_Translation:
    """
    defines a Translation of VRML specifying transform
    properties.
    This node defines a translation by 3D vector.
    By default:
    myTranslation (0,0,0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aTranslation: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_Translation) -> None: ...

    def SetTranslation(self, aTranslation: nanoocp.gp.gp_Vec) -> None: ...

    def Translation(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...

class Vrml_WWWAnchor:
    """
    defines a WWWAnchor node of VRML specifying group properties.
    The WWWAnchor group node loads a new scene into a VRML browser
    when one of its children is closen. Exactly how a user "chooses"
    a child of the WWWAnchor is up to the VRML browser.
    WWWAnchor with an empty ("") name does nothing when its
    children are chosen.
    WWWAnchor behaves like a Separator, pushing the traversal state
    before traversing its children and popping it afterwards.
    """

    @overload
    def __init__(self, aName: nanoocp.TCollection.TCollection_AsciiString = ..., aDescription: nanoocp.TCollection.TCollection_AsciiString = ..., aMap: Vrml_WWWAnchorMap = Vrml_WWWAnchorMap.Vrml_MAP_NONE) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_WWWAnchor) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetMap(self, aMap: Vrml_WWWAnchorMap) -> None: ...

    def Map(self) -> Vrml_WWWAnchorMap: ...

    def Print(self) -> str: ...

class Vrml_WWWInline:
    """
    defines a WWWInline node of VRML specifying group properties.
    The WWWInline group node reads its children from anywhere in the
    World Wide Web.
    Exactly when its children are read is not defined;
    reading the children may be delayed until the WWWInline is actually
    displayed.
    WWWInline with an empty ("") name does nothing.
    WWWInline behaves like a Separator, pushing the traversal state
    before traversing its children and popping it afterwards.
    By defaults:
    myName  ("")
    myBboxSize (0,0,0)
    myBboxCenter  (0,0,0)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, aName: nanoocp.TCollection.TCollection_AsciiString, aBboxSize: nanoocp.gp.gp_Vec, aBboxCenter: nanoocp.gp.gp_Vec) -> None: ...

    @overload
    def __init__(self, theOther: Vrml_WWWInline) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetBboxSize(self, aBboxSize: nanoocp.gp.gp_Vec) -> None: ...

    def BboxSize(self) -> nanoocp.gp.gp_Vec: ...

    def SetBboxCenter(self, aBboxCenter: nanoocp.gp.gp_Vec) -> None: ...

    def BboxCenter(self) -> nanoocp.gp.gp_Vec: ...

    def Print(self) -> str: ...
