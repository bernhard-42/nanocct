"""OCCT package VrmlData (toolkit TKDEVRML)"""

from collections.abc import Sequence
import enum
from typing import overload

import nanoocp.Bnd
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.gp


class VrmlData_ErrorStatus(enum.IntEnum):
    """Status of read/write or other operation."""

    VrmlData_StatusOK = 0

    VrmlData_EmptyData = 1

    VrmlData_UnrecoverableError = 2

    VrmlData_GeneralError = 3

    VrmlData_EndOfFile = 4

    VrmlData_NotVrmlFile = 5

    VrmlData_CannotOpenFile = 6

    VrmlData_VrmlFormatError = 7

    VrmlData_NumericInputError = 8

    VrmlData_IrrelevantNumber = 9

    VrmlData_BooleanInputError = 10

    VrmlData_StringInputError = 11

    VrmlData_NodeNameUnknown = 12

    VrmlData_NonPositiveSize = 13

    VrmlData_ReadUnknownNode = 14

    VrmlData_NonSupportedFeature = 15

    VrmlData_OutputStreamUndefined = 16

    VrmlData_NotImplemented = 17

VrmlData_StatusOK: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_StatusOK

VrmlData_EmptyData: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_EmptyData

VrmlData_UnrecoverableError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_UnrecoverableError

VrmlData_GeneralError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_GeneralError

VrmlData_EndOfFile: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_EndOfFile

VrmlData_NotVrmlFile: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NotVrmlFile

VrmlData_CannotOpenFile: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_CannotOpenFile

VrmlData_VrmlFormatError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_VrmlFormatError

VrmlData_NumericInputError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NumericInputError

VrmlData_IrrelevantNumber: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_IrrelevantNumber

VrmlData_BooleanInputError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_BooleanInputError

VrmlData_StringInputError: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_StringInputError

VrmlData_NodeNameUnknown: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NodeNameUnknown

VrmlData_NonPositiveSize: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NonPositiveSize

VrmlData_ReadUnknownNode: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_ReadUnknownNode

VrmlData_NonSupportedFeature: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NonSupportedFeature

VrmlData_OutputStreamUndefined: VrmlData_ErrorStatus = ...

VrmlData_NotImplemented: VrmlData_ErrorStatus = VrmlData_ErrorStatus.VrmlData_NotImplemented

class VrmlData_Node(nanoocp.Standard.Standard_Transient):
    """Abstract VRML Node"""

    def Scene(self) -> VrmlData_Scene:
        """Query the Scene that contains this Node"""

    def Name(self) -> str:
        """Query the name"""

    def ReadNode(self, theBuffer: VrmlData_InBuffer, Type: nanoocp.Standard.Standard_Type | None = None) -> tuple[VrmlData_ErrorStatus, VrmlData_Node]:
        """
        Read a complete node definition from VRML stream
        @param theBuffer
        Buffer receiving the input data.
        @param theNode
        <tt>[out]</tt> Node restored from the buffer data
        @param Type
        Node type to be checked. If it is NULL(default) no type checking is done.
        Otherwise the created node is matched and an error is returned if
        no match detected.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, then it would not be written."""

    def WriteClosing(self) -> VrmlData_ErrorStatus:
        """Write the closing brace in the end of a node output."""

    def Clone(self, arg0: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.<p>
        This method nullifies the argument node if its member myScene differs
        from that one of the current instance.
        """

    @staticmethod
    def ReadBoolean(theBuffer: VrmlData_InBuffer) -> tuple[VrmlData_ErrorStatus, bool]:
        """Read one boolean value (TRUE or FALSE)."""

    @staticmethod
    def ReadString(theBuffer: VrmlData_InBuffer, theRes: nanoocp.TCollection.TCollection_AsciiString) -> VrmlData_ErrorStatus:
        """Read one quoted string, the quotes are removed."""

    @staticmethod
    def ReadMultiString(theBuffer: VrmlData_InBuffer, theRes: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]) -> VrmlData_ErrorStatus:
        """Read one quoted string, the quotes are removed."""

    @staticmethod
    def ReadInteger(theBuffer: VrmlData_InBuffer) -> tuple[VrmlData_ErrorStatus, int]:
        """Read one integer value."""

    @staticmethod
    def OK(theStat: VrmlData_ErrorStatus) -> bool: ...

    @staticmethod
    def OK__VrmlData_ErrorStatus(theStat: VrmlData_ErrorStatus) -> tuple[bool, VrmlData_ErrorStatus]:
        """
        OK__VrmlData_ErrorStatus: the C++ overload OK(VrmlData_ErrorStatus &, const VrmlData_ErrorStatus); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @staticmethod
    def GlobalIndent() -> int:
        """Define the common Indent in spaces, for writing all nodes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Material(VrmlData_Node):
    """Implementation of the Material node"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theAmbientIntensity: float = -1.0, theShininess: float = -1.0, theTransparency: float = -1.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Material) -> None: ...

    def AmbientIntensity(self) -> float:
        """Query the Ambient Intensity value"""

    def Shininess(self) -> float:
        """Query the Shininess value"""

    def Transparency(self) -> float:
        """Query the Transparency value"""

    def AmbientColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Query the Ambient color"""

    def DiffuseColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Query the Diffuse color"""

    def EmissiveColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Query the Emissive color"""

    def SpecularColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Query the Specular color"""

    def SetAmbientIntensity(self, theAmbientIntensity: float) -> None:
        """Set the Ambient Intensity value"""

    def SetShininess(self, theShininess: float) -> None:
        """Set the Shininess value"""

    def SetTransparency(self, theTransparency: float) -> None:
        """Set the Transparency value"""

    def SetAmbientColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Query the Ambient color"""

    def SetDiffuseColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Query the Diffuse color"""

    def SetEmissiveColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Query the Emissive color"""

    def SetSpecularColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Query the Specular color"""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to the Scene output."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, so that it should not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Texture(VrmlData_Node):
    """Implementation of the Texture node"""

    def RepeatS(self) -> bool:
        """Query the RepeatS value"""

    def RepeatT(self) -> bool:
        """Query the RepeatT value"""

    def SetRepeatS(self, theFlag: bool) -> None:
        """Set the RepeatS flag"""

    def SetRepeatT(self, theFlag: bool) -> None:
        """Set the RepeatT flag"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_TextureTransform(VrmlData_Node):
    """Implementation of the TextureTransform node"""

    def Center(self) -> nanoocp.gp.gp_XY:
        """Query the Center"""

    def Rotation(self) -> float:
        """Query the Rotation"""

    def Scale(self) -> nanoocp.gp.gp_XY:
        """Query the Scale"""

    def Translation(self) -> nanoocp.gp.gp_XY:
        """Query the Translation"""

    def SetCenter(self, V: nanoocp.gp.gp_XY) -> None:
        """Set the Center"""

    def SetRotation(self, V: float) -> None:
        """Set the Rotation"""

    def SetScale(self, V: nanoocp.gp.gp_XY) -> None:
        """Set the Scale"""

    def SetTranslation(self, V: nanoocp.gp.gp_XY) -> None:
        """Set the Translation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Appearance(VrmlData_Node):
    """Implementation of the Appearance node type"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Appearance) -> None: ...

    def Material(self) -> VrmlData_Material:
        """Query the Material"""

    def Texture(self) -> VrmlData_Texture:
        """Query the Texture"""

    def TextureTransform(self) -> VrmlData_TextureTransform:
        """Query the TextureTransform"""

    def SetMaterial(self, theMat: VrmlData_Material | None) -> None:
        """Set the Material"""

    def SetTexture(self, theTexture: VrmlData_Texture | None) -> None:
        """Set the Texture"""

    def SetTextureTransform(self, theTT: VrmlData_TextureTransform | None) -> None:
        """Set the Texture Transform"""

    def Clone(self, arg0: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.<p>
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node from input stream."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, so that it should not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_ArrayVec3d(VrmlData_Node):
    """
    Implementatioon of basic node for Coordinate, Normal and Color
    (array of triplets).
    """

    def Length(self) -> int:
        """Query the number of vectors"""

    def Values(self) -> nanoocp.gp.gp_XYZ:
        """Query the array"""

    def AllocateValues(self, theLength: int) -> bool:
        """
        Create a data array and assign the field myArray.
        @return
        True if allocation was successful.
        """

    def SetValues(self, nValues: int, arrValues: nanoocp.gp.gp_XYZ) -> None:
        """Set the array data"""

    def ReadArray(self, theBuffer: VrmlData_InBuffer, theName: str, isScale: bool) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def WriteArray(self, theName: str, isScale: bool) -> VrmlData_ErrorStatus:
        """Write the Node to the output stream currently opened in Scene."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, so that it should not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Geometry(VrmlData_Node):
    """
    Implementation of the Geometry node.
    Contains the topological representation (TopoDS_Shell) of the VRML geometry
    """

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the shape. This method checks the flag myIsModified; if True it
        should rebuild the shape presentation.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Box(VrmlData_Geometry):
    """
    Implementation of the Box node.
    This node is defined by Size vector, assuming that the box center is located
    in (0., 0., 0.) and that each corner is 0.5*|Size| distance from the center.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, sizeX: float = 2.0, sizeY: float = 2.0, sizeZ: float = 2.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Box) -> None: ...

    def Size(self) -> nanoocp.gp.gp_XYZ:
        """Query the Box size"""

    def SetSize(self, theSize: nanoocp.gp.gp_XYZ) -> None:
        """Set the Box Size"""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the primitive topology. This method returns a Null shape if there
        is an internal error during the primitive creation (zero radius, etc.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Color(VrmlData_ArrayVec3d):
    """Implementation of the node Color"""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, nColors: int = 0, arrColors: nanoocp.gp.gp_XYZ = None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: VrmlData_Color) -> None: ...

    def Color(self, i: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Query one color
        @param i
        index in the array of colors [0 .. N-1]
        @return
        the color value for the index. If index irrelevant, returns (0., 0., 0.)
        """

    def SetColors(self, nColors: int, arrColors: nanoocp.gp.gp_XYZ) -> None:
        """Set the array data"""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.<p>
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to the Scene output."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Cone(VrmlData_Geometry):
    """
    Implementation of the Cone node.
    The cone is located with its middle of the height segment in (0., 0., 0.)
    The height is oriented along OY.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theBottomRadius: float = 1.0, theHeight: float = 2.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Cone) -> None: ...

    def BottomRadius(self) -> float:
        """Query the Bottom Radius"""

    def Height(self) -> float:
        """Query the Height"""

    def HasBottom(self) -> bool:
        """Query if the bottom circle is included"""

    def HasSide(self) -> bool:
        """Query if the side surface is included"""

    def SetBottomRadius(self, theRadius: float) -> None:
        """Set the Bottom Radius"""

    def SetHeight(self, theHeight: float) -> None:
        """Set the Height"""

    def SetFaces(self, hasBottom: bool, hasSide: bool) -> None:
        """Set which faces are included"""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the primitive topology. This method returns a Null shape if there
        is an internal error during the primitive creation (zero radius, etc.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Coordinate(VrmlData_ArrayVec3d):
    """Implementation of the node Coordinate"""

    @overload
    def __init__(self) -> None:
        """Empty Constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, nPoints: int = 0, arrPoints: nanoocp.gp.gp_XYZ = None) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Coordinate) -> None: ...

    def Coordinate(self, i: int) -> nanoocp.gp.gp_XYZ:
        """
        Query one point
        @param i
        index in the array of points [0 .. N-1]
        @return
        the coordinate for the index. If index irrelevant, returns (0., 0., 0.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to the Scene output."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Cylinder(VrmlData_Geometry):
    """Implementation of the Cylinder node"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theRadius: float = 1.0, theHeight: float = 2.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Cylinder) -> None: ...

    def Radius(self) -> float:
        """Query the Radius"""

    def Height(self) -> float:
        """Query the Height"""

    def HasBottom(self) -> bool:
        """Query if the bottom circle is included"""

    def HasSide(self) -> bool:
        """Query if the side surface is included"""

    def HasTop(self) -> bool:
        """Query if the top surface is included"""

    def SetRadius(self, theRadius: float) -> None:
        """Set the Radius"""

    def SetHeight(self, theHeight: float) -> None:
        """Set the Height"""

    def SetFaces(self, hasBottom: bool, hasSide: bool, hasTop: bool) -> None:
        """Set which faces are included"""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the primitive topology. This method returns a Null shape if there
        is an internal error during the primitive creation (zero radius, etc.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Faceted(VrmlData_Geometry):
    """
    Common API of faceted Geometry nodes: IndexedFaceSet, ElevationGrid,
    Extrusion.
    """

    def IsCCW(self) -> bool:
        """Query "Is Counter-Clockwise" attribute"""

    def IsSolid(self) -> bool:
        """Query "Is Solid" attribute"""

    def IsConvex(self) -> bool:
        """Query "Is Convex" attribute"""

    def CreaseAngle(self) -> float:
        """Query the Crease Angle"""

    def SetCCW(self, theValue: bool) -> None:
        """Set "Is Counter-Clockwise" attribute"""

    def SetSolid(self, theValue: bool) -> None:
        """Set "Is Solid" attribute"""

    def SetConvex(self, theValue: bool) -> None:
        """Set "Is Convex" attribute"""

    def SetCreaseAngle(self, theValue: float) -> None:
        """Set "Is Convex" attribute"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Group(VrmlData_Node):
    """Implementation of node "Group\""""

    @overload
    def __init__(self, isTransform: bool = False) -> None:
        """
        Empty constructor.
        @param isTransform
        True if the group of type Transform is defined
        @param theAlloc
        Allocator used for the list of children
        """

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isTransform: bool = False) -> None:
        """
        Constructor.
        @param theName
        Name of the Group node
        @param isTransform
        True if the group of type Transform is defined
        @param theAlloc
        Allocator used for the list of children
        """

    @overload
    def __init__(self, theOther: VrmlData_Group) -> None: ...

    def AddNode(self, theNode: VrmlData_Node | None) -> VrmlData_Node:
        """Add one node to the Group."""

    def RemoveNode(self, theNode: VrmlData_Node | None) -> bool:
        """
        Remove one node from the Group.
        @return
        True if the node was located and removed, False if none removed.
        """

    def NodeIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_VrmlData_Node.Iterator:
        """Create iterator on nodes belonging to the Group."""

    def Box(self) -> nanoocp.Bnd.Bnd_B3f:
        """Query the bounding box."""

    def SetBox(self, theBox: nanoocp.Bnd.Bnd_B3f) -> None:
        """Set the bounding box."""

    def SetTransform(self, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Set the transformation. Returns True if the group is Transform type,
        otherwise do nothing and return False.
        """

    def GetTransform(self) -> nanoocp.gp.gp_Trsf:
        """
        Query the transform value.
        For group without transformation this always returns Identity
        """

    def IsTransform(self) -> bool:
        """Query if the node is Transform type."""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    def FindNode(self, theName: str, theLocation: nanoocp.gp.gp_Trsf) -> VrmlData_Node:
        """
        Find a node by its name, inside this Group
        @param theName
        Name of the node to search for.
        @param theLocation
        Location of the found node with respect to this Group.
        """

    def Shape(self, theShape: nanoocp.TopoDS.TopoDS_Shape, pMapApp: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_TShape, nanoocp.VrmlData.VrmlData_Appearance]) -> None:
        """Get the shape representing the group geometry."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_ImageTexture(VrmlData_Texture):
    """Implementation of the ImageTexture node"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theURL: str | None = None, theRepS: bool = False, theRepT: bool = False) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_ImageTexture) -> None: ...

    def URL(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]:
        """Query the associated URL."""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_InBuffer:
    """Structure passed to the methods dealing with input stream."""

    def __init__(self, theOther: VrmlData_InBuffer) -> None: ...

    @property
    def Line(self) -> list[str]: ...

    @Line.setter
    def Line(self, arg: Sequence[str], /) -> None: ...

    @property
    def IsProcessed(self) -> bool: ...

    @IsProcessed.setter
    def IsProcessed(self, arg: bool, /) -> None: ...

    @property
    def LineCount(self) -> int: ...

    @LineCount.setter
    def LineCount(self, arg: int, /) -> None: ...

class VrmlData_Normal(VrmlData_ArrayVec3d):
    """Implementation of the node Normal"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, nVec: int = 0, arrVec: nanoocp.gp.gp_XYZ = None) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Normal) -> None: ...

    def Normal(self, i: int) -> nanoocp.gp.gp_XYZ:
        """
        Query one normal
        @param i
        index in the array of normals [0 .. N-1]
        @return
        the normal value for the index. If index irrelevant, returns (0., 0., 0.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to the Scene output."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_TextureCoordinate(VrmlData_Node):
    """Implementation of the node TextureCoordinate"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, nPoints: int = 0, arrPoints: nanoocp.gp.gp_XY = None) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_TextureCoordinate) -> None: ...

    def AllocateValues(self, theLength: int) -> bool:
        """
        Create a data array and assign the field myArray.
        @return
        True if allocation was successful.
        """

    def Length(self) -> int:
        """Query the number of points"""

    def Points(self) -> nanoocp.gp.gp_XY:
        """Query the points"""

    def SetPoints(self, nPoints: int, arrPoints: nanoocp.gp.gp_XY) -> None:
        """Set the points array"""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_IndexedFaceSet(VrmlData_Faceted):
    """Implementation of IndexedFaceSet node"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isCCW: bool = True, isSolid: bool = True, isConvex: bool = True, theCreaseAngle: float = 0.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_IndexedFaceSet) -> None: ...

    def Normals(self) -> VrmlData_Normal:
        """Query the Normals."""

    def Colors(self) -> VrmlData_Color:
        """Query the Colors."""

    def TextureCoords(self) -> VrmlData_TextureCoordinate:
        """Query the Texture Coordinates."""

    def Coordinates(self) -> VrmlData_Coordinate:
        """Query the Coordinates."""

    def SetCoordinates(self, theCoord: VrmlData_Coordinate | None) -> None:
        """Set the nodes"""

    def SetNormals(self, theNormals: VrmlData_Normal | None) -> None:
        """Set the normals node"""

    def SetNormalPerVertex(self, isNormalPerVertex: bool) -> None:
        """Set the boolean value "normalPerVertex\""""

    def GetColor(self, iFace: int, iVertex: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Query a color for one node in the given element. The color is
        interpreted according to fields myColors, myArrColorInd,
        myColorPerVertex, as defined in VRML 2.0.
        @param iFace
        rank of the polygon [0 .. N-1]
        @param iVertex
        rank of the vertex in the polygon [0 .. M-1]. This parameter is ignored
        if (myColorPerVertex == False)
        @return
        Color value (RGB); if the color is indefinite then returns (0., 0., 0.)
        """

    def SetColors(self, theColors: VrmlData_Color | None) -> None:
        """Set the Color node"""

    def SetColorPerVertex(self, isColorPerVertex: bool) -> None:
        """Set the boolean value "colorPerVertex\""""

    def SetTextureCoords(self, tc: VrmlData_TextureCoordinate | None) -> None:
        """Set the Texture Coordinate node"""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the shape. This method checks the flag myIsModified; if True it
        should rebuild the shape presentation.
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, so that it should not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_IndexedLineSet(VrmlData_Geometry):
    """Data type to store a set of polygons."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, isColorPerVertex: bool = True) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: VrmlData_IndexedLineSet) -> None: ...

    def Coordinates(self) -> VrmlData_Coordinate:
        """Query the Coordinates."""

    def SetCoordinates(self, theCoord: VrmlData_Coordinate | None) -> None:
        """Set the nodes"""

    def Colors(self) -> VrmlData_Color:
        """Query the Colors."""

    def SetColors(self, theColors: VrmlData_Color | None) -> None:
        """Set the Color node"""

    def GetColor(self, iFace: int, iVertex: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Query a color for one node in the given element. The color is
        interpreted according to fields myColors, myArrColorInd,
        myColorPerVertex, as defined in VRML 2.0.
        @param iFace
        rank of the polygon [0 .. N-1]
        @param iVertex
        rank of the vertex in the polygon [0 .. M-1]. This parameter is ignored
        if (myColorPerVertex == False)
        @return
        Color value (RGB); if the color is indefinite then returns (0., 0., 0.)
        """

    def SetColorPerVertex(self, isColorPerVertex: bool) -> None:
        """Set the boolean value "colorPerVertex\""""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the shape. This method checks the flag myIsModified; if True it
        should rebuild the shape presentation.
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, so that it should not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_WorldInfo(VrmlData_Node):
    """Data type for WorldInfo node"""

    @overload
    def __init__(self) -> None:
        """Empty Constructor."""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str | None = None, theTitle: str | None = None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: VrmlData_WorldInfo) -> None: ...

    def SetTitle(self, theString: str) -> None:
        """Set or modify the title."""

    def AddInfo(self, theString: str) -> None:
        """Add a string to the list of info strings."""

    def Title(self) -> str:
        """Query the title string."""

    def InfoIterator(self) -> "NCollection_TListIterator<char const*>":
        """Return the iterator of Info strings."""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the Node from input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to the Scene output."""

    def IsDefault(self) -> bool:
        """Returns True if the node is default, then it would not be written."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Scene:
    """Block of comments describing class VrmlData_Scene"""

    def __init__(self, arg0: nanoocp.NCollection.NCollection_IncAllocator | None = None) -> None:
        """Constructor."""

    def Status(self) -> VrmlData_ErrorStatus:
        """
        Query the status of the previous operation.
        Normally it should be equal to VrmlData_StatusOK (no error).
        """

    def SetVrmlDir(self, arg0: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Add the given directory path to the list of VRML file search directories.
        This method forms the list of directories ordered according to the
        sequence of this method calls. When an Inline node is found, the URLs
        in that node are matched with these directories.
        The last (implicit) search directory is the current process directory
        ("."). It takes effect if the list is empty or if there is no match with
        existing directories.
        """

    def SetLinearScale(self, theScale: float) -> None:
        """
        Set the scale factor that would be further used in methods
        ReadReal, ReadXYZ and ReadXY. All coordinates, distances and sized are
        multiplied by this factor during reading the data.
        """

    def VrmlDirIterator(self) -> nanoocp.NCollection.NCollection_List__TCollection_ExtendedString.Iterator:
        """
        Returns the directory iterator, to check the presence of requested VRML
        file in each iterated directory.
        """

    def GetIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_VrmlData_Node.Iterator:
        """Iterator of Nodes"""

    def NamedNodesIterator(self) -> "NCollection_Map<opencascade::handle<VrmlData_Node>, NCollection_DefaultHasher<opencascade::handle<VrmlData_Node>>>::Iterator":
        """Get the iterator of named nodes."""

    def Allocator(self) -> nanoocp.NCollection.NCollection_IncAllocator:
        """Allocator used by all nodes contained in the Scene."""

    def AddNode(self, theN: VrmlData_Node | None, isTopLevel: bool = True) -> VrmlData_Node:
        """
        Add a Node. If theN belongs to another Scene, it is cloned.
        <p>VrmlData_WorldInfo cannot be added, in this case the method
        returns a NULL handle.
        """

    @overload
    def FindNode(self, theName: str, theType: nanoocp.Standard.Standard_Type | None = None) -> VrmlData_Node:
        """
        Find a node by its name.
        @param theName
        Name of the node to find.
        @param theType
        Type to match. If this value is NULL, the first found node with the
        given name is returned. If theType is given, only the node that has
        that type is returned.
        """

    @overload
    def FindNode(self, theName: str, theLocation: nanoocp.gp.gp_Trsf) -> VrmlData_Node:
        """
        Find a node by its name.
        @param theName
        Name of the node to search for.
        @param theLocation
        Location of the found node with respect to the whole VRML shape.
        """

    def GetShape(self, M: nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_TShape, nanoocp.VrmlData.VrmlData_Appearance]) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Convert the scene to a Shape, with the information on materials defined
        for each sub-shape. This method should be used instead of TopoDS_Shape
        explicit conversion operator when you need to retrieve the material
        aspect for each face or edge in the returned topological object.
        @param M
        Data Map that binds an Appearance instance to each created TFace or
        TEdge if the Appearance node is defined in VRML scene for that geometry.
        @return
        TopoDS_Shape (Compound) holding all the scene, similar to the result of
        explicit TopoDS_Shape conversion operator.
        """

    def WorldInfo(self) -> VrmlData_WorldInfo:
        """Query the WorldInfo member."""

    @staticmethod
    def ReadLine(theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """
        Read a VRML line. Empty lines and comments are skipped.
        The processing starts here from theBuffer.LinePtr; if there is at least
        one non-empty character (neither space nor comment), this line is used
        without reading the next one.
        @param theLine
        Buffer receiving the input line
        @param theInput
        Input stream
        @param theLen
        Length of the input buffer (maximal line length)
        """

    @staticmethod
    def ReadWord(theBuffer: VrmlData_InBuffer, theStr: nanoocp.TCollection.TCollection_AsciiString) -> VrmlData_ErrorStatus:
        """Read a single word from the input stream, delimited by whitespace."""

    def Dump(self) -> str:
        """Diagnostic dump of the contents"""

    def ReadReal(self, theBuffer: VrmlData_InBuffer, isApplyScale: bool, isOnlyPositive: bool) -> tuple[VrmlData_ErrorStatus, float]:
        """Read one real value."""

    def ReadXYZ(self, theBuffer: VrmlData_InBuffer, theXYZ: nanoocp.gp.gp_XYZ, isApplyScale: bool, isOnlyPositive: bool) -> VrmlData_ErrorStatus:
        """Read one triplet of real values."""

    def ReadXY(self, theBuffer: VrmlData_InBuffer, theXYZ: nanoocp.gp.gp_XY, isApplyScale: bool, isOnlyPositive: bool) -> VrmlData_ErrorStatus:
        """Read one doublet of real values."""

    def GetLineError(self) -> int:
        """Query the line where the error occurred (if the status is not OK)"""

    def SetIndent(self, nSpc: int) -> None:
        """
        Store the indentation for VRML output.
        @param nSpc
        number of spaces to insert at every indentation level
        """

    def WriteXYZ(self, theXYZ: nanoocp.gp.gp_XYZ, isScale: bool, thePostfix: str | None = None) -> VrmlData_ErrorStatus:
        """
        Write a triplet of real values on a separate line.
        @param theXYZ
        The value to be output.
        @param isScale
        If True, then each component is divided by myLinearScale.
        @param thePostfix
        Optional string that is added before the end of the line.
        """

    def WriteLine(self, theLine0: str, theLine1: str | None = None, theIndent: int = 0) -> VrmlData_ErrorStatus:
        """
        Write a string to the output stream respecting the indentation. The string
        can be defined as two substrings that will be separated by a space.
        Each of the substrings can be NULL, then it is ignored. If both
        are NULL, then a single newline is output (without indent).
        @param theLine0
        The first part of string to output
        @param theLine1
        The second part of string to output
        @param theIndent
        - 0 value ignored.
        - negative decreases the current indent and then outputs.
        - positive outputs and then increases the current indent.
        @return
        Error status of the stream, or a special error if myOutput == NULL.
        """

    def WriteNode(self, thePrefix: str, arg1: VrmlData_Node | None) -> VrmlData_ErrorStatus:
        """Write the given node to output stream 'myOutput'."""

    def IsDummyWrite(self) -> bool:
        """
        Query if the current write operation is dummy, i.e., for the purpose of
        collecting information before the real write is commenced.
        """

class VrmlData_ShapeConvert:
    """Algorithm converting one shape or a set of shapes to VrmlData_Scene."""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theScale: float = 1.0) -> None:
        """
        Constructor.
        @param theScene
        Scene receiving all Vrml data.
        @param theScale
        Scale factor, considering that VRML standard specifies coordinates in
        meters. So if your data are in mm, you should provide theScale=0.001
        """

    @overload
    def __init__(self, theOther: VrmlData_ShapeConvert) -> None: ...

    class ShapeData:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: VrmlData_ShapeConvert.ShapeData) -> None: ...

        @property
        def Name(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

        @Name.setter
        def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

        @Shape.setter
        def Shape(self, arg: nanoocp.TopoDS.TopoDS_Shape, /) -> None: ...

        @property
        def Node(self) -> VrmlData_Node: ...

        @Node.setter
        def Node(self, arg: VrmlData_Node, /) -> None: ...

    def AddShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theName: str | None = None) -> None:
        """
        Add one shape to the internal list, may be called several times with
        different shapes.
        """

    def Convert(self, theExtractFaces: bool, theExtractEdges: bool, theDeflection: float = 0.01, theDeflAngle: float = 0.3490658503988659) -> None:
        """
        Convert all accumulated shapes and store them in myScene.
        The internal data structures are cleared in the end of conversion.
        @param theExtractFaces
        If True,  converter extracst faces from the shapes.
        @param theExtractEdges
        If True,  converter extracts edges from the shapes.
        @param theDeflection
        Deflection for tessellation of geometrical lines/surfaces. Existing mesh
        is used if its deflection is smaller than the one given by this
        parameter.
        @param theDeflAngle
        Angular deflection for tessellation of geometrical lines.
        """

    def ConvertDocument(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None) -> None:
        """
        Add all shapes start from given document with colors and names to the internal structure
        """

class VrmlData_ShapeNode(VrmlData_Node):
    """Implementation of the Shape node type"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_ShapeNode) -> None: ...

    def Appearance(self) -> VrmlData_Appearance:
        """Query the Appearance."""

    def Geometry(self) -> VrmlData_Geometry:
        """Query the Geometry."""

    def SetAppearance(self, theAppear: VrmlData_Appearance | None) -> None:
        """Set the Appearance"""

    def SetGeometry(self, theGeometry: VrmlData_Geometry | None) -> None:
        """Set the Geometry"""

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    def IsDefault(self) -> bool:
        """Check if the Shape Node is writeable."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_Sphere(VrmlData_Geometry):
    """Implementation of the Sphere node."""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str, theRadius: float = 1.0) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: VrmlData_Sphere) -> None: ...

    def Radius(self) -> float:
        """Query the sphere radius"""

    def SetRadius(self, theRadius: float) -> None:
        """Set the sphere radius"""

    def TShape(self) -> nanoocp.TopoDS.TopoDS_TShape:
        """
        Query the primitive topology. This method returns a Null shape if there
        is an internal error during the primitive creation (zero radius, etc.)
        """

    def Clone(self, theOther: VrmlData_Node | None) -> VrmlData_Node:
        """
        Create a copy of this node.
        If the parameter is null, a new copied node is created. Otherwise new node
        is not created, but rather the given one is modified.
        """

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Fill the Node internal data from the given input stream."""

    def Write(self, thePrefix: str) -> VrmlData_ErrorStatus:
        """Write the Node to output stream."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class VrmlData_UnknownNode(VrmlData_Node):
    """
    Definition of UnknownNode -- placeholder for node types that
    are not processed now.
    """

    @overload
    def __init__(self) -> None:
        """Empty Constructor."""

    @overload
    def __init__(self, theScene: VrmlData_Scene, theName: str | None = None, theTitle: str | None = None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: VrmlData_UnknownNode) -> None: ...

    def Read(self, theBuffer: VrmlData_InBuffer) -> VrmlData_ErrorStatus:
        """Read the unknown node, till the last closing brace of it."""

    def GetTitle(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Query the title of the unknown node."""

    def IsDefault(self) -> bool:
        """Check if the Node is non-writeable -- always returns true."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

def IsEqual(theOne: VrmlData_Node | None, theTwo: VrmlData_Node | None) -> bool: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.VrmlData
VrmlData_ListOfNode = nanoocp.NCollection.NCollection_List[nanoocp.VrmlData.VrmlData_Node]
