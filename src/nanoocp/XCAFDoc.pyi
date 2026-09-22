"""OCCT package XCAFDoc (toolkit TKXCAF)"""

import enum
from typing import overload

import nanoocp.Graphic3d
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TCollection
import nanoocp.TDF
import nanoocp.TDataStd
import nanoocp.TDocStd
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.UnitsMethods
import nanoocp.XCAFDimTolObjects
import nanoocp.XCAFNoteObjects
import nanoocp.XCAFView
import nanoocp.gp


class XCAFDoc_ColorType(enum.IntEnum):
    """
    Defines types of color assignments
    Color of shape is defined following way
    in dependance with type of color.
    If type of color is XCAFDoc_ColorGen - then this color
    defines default color for surfaces and curves.
    If for shape color with types XCAFDoc_ColorSurf or XCAFDoc_ColorCurv is specified
    then such color overrides generic color.
    simple color
    color of surfaces
    color of curves
    """

    XCAFDoc_ColorGen = 0

    XCAFDoc_ColorSurf = 1

    XCAFDoc_ColorCurv = 2

XCAFDoc_ColorGen: XCAFDoc_ColorType = XCAFDoc_ColorType.XCAFDoc_ColorGen

XCAFDoc_ColorSurf: XCAFDoc_ColorType = XCAFDoc_ColorType.XCAFDoc_ColorSurf

XCAFDoc_ColorCurv: XCAFDoc_ColorType = XCAFDoc_ColorType.XCAFDoc_ColorCurv

class XCAFDoc:
    """
    Definition of general structure of DECAF document
    and tools to work with it

    The document is composed of sections, each section
    storing its own kind of data and managing by corresponding
    tool
    Some properties can be attached directly to shapes. These properties are:
    * Name (the standard definition from OCAF) - class TDataStd_Name
    * Centroid (for the validation of transfer) - class XCAFDoc_Centroid
    * Volume (for the validation of transfer) - class XCAFDoc_Volume
    * Area (for the validation of transfer) - class XCafDoc_Area
    Management of these attributes is realized by OCAF. For getting
    the attributes attached to a label the method class
    TDF_Label::FindAttribute() should be used.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc) -> None: ...

    @staticmethod
    def AssemblyGUID() -> nanoocp.Standard.Standard_GUID:
        """
        class for containing GraphNodes.
        Returns GUID for UAttribute identifying assembly
        """

    @staticmethod
    def ShapeRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Returns GUID for TreeNode representing assembly link"""

    @staticmethod
    def ColorRefGUID(type: XCAFDoc_ColorType) -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of colors"""

    @staticmethod
    def DimTolRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of DGT"""

    @staticmethod
    def DimensionRefFirstGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of Dimension"""

    @staticmethod
    def DimensionRefSecondGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of Dimension"""

    @staticmethod
    def GeomToleranceRefGUID() -> nanoocp.Standard.Standard_GUID:
        """
        Return GUIDs for TreeNode representing specified types of GeomTolerance
        """

    @staticmethod
    def DatumRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of datum"""

    @staticmethod
    def DatumTolRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing connections Datum-Toler"""

    @staticmethod
    def LayerRefGUID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def MaterialRefGUID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def VisMaterialRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUID for TreeNode representing Visualization Material."""

    @staticmethod
    def NoteRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for representing notes"""

    @staticmethod
    def InvisibleGUID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def ColorByLayerGUID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def ExternRefGUID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns GUID for UAttribute identifying external reference on no-step file
        """

    @staticmethod
    def SHUORefGUID() -> nanoocp.Standard.Standard_GUID:
        """
        Returns GUID for UAttribute identifying specified higher usage occurrence
        """

    @staticmethod
    def ViewRefGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of View"""

    @staticmethod
    def ViewRefShapeGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of View"""

    @staticmethod
    def ViewRefGDTGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of View"""

    @staticmethod
    def ViewRefPlaneGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for TreeNode representing specified types of View"""

    @staticmethod
    def ViewRefNoteGUID() -> nanoocp.Standard.Standard_GUID:
        """Return GUIDs for GraphNode representing specified types of View"""

    @staticmethod
    def ViewRefAnnotationGUID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def LockGUID() -> nanoocp.Standard.Standard_GUID:
        """Returns GUID for UAttribute identifying lock flag"""

    @staticmethod
    def AttributeInfo(theAtt: nanoocp.TDF.TDF_Attribute | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Prints attribute information into a string.
        @param theAtt an XDE attribute
        @return the generated info value
        """

class XCAFDoc_AssemblyItemId:
    """
    Unique item identifier in the hierarchical product structure.
    A full path to an assembly component in the "part-of" graph starting from
    the root node.
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty item ID."""

    @overload
    def __init__(self, thePath: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Constructs an item ID from a list of strings, where every
        string is a label entry.
        \\param[in]  thePath - list of label entries.
        """

    @overload
    def __init__(self, theString: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Constructs an item ID from a formatted path, where label entries
        are separated by '/' symbol.
        \\param[in]  theString - formatted full path.
        """

    @overload
    def __init__(self, theOther: XCAFDoc_AssemblyItemId) -> None: ...

    @overload
    def Init(self, thePath: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Initializes the item ID from a list of strings, where every
        string is a label entry.
        \\param[in]  thePath - list of label entries.
        """

    @overload
    def Init(self, theString: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Initializes the item ID from a formatted path, where label entries
        are separated by '/' symbol.
        \\param[in]  theString - formatted full path.
        """

    def IsNull(self) -> bool:
        """Returns true if the full path is empty, otherwise - false."""

    def Nullify(self) -> None:
        """Clears the full path."""

    def IsChild(self, theOther: XCAFDoc_AssemblyItemId) -> bool:
        """
        Checks if this item is a child of the given item.
        \\param[in]  theOther - potentially ancestor item.
        \\return true if the item is a child of theOther item, otherwise - false.
        """

    def IsDirectChild(self, theOther: XCAFDoc_AssemblyItemId) -> bool:
        """
        Checks if this item is a direct child of the given item.
        \\param[in]  theOther - potentially parent item.
        \\return true if the item is a direct child of theOther item, otherwise - false.
        """

    def IsEqual(self, theOther: XCAFDoc_AssemblyItemId) -> bool:
        """
        Checks for item IDs equality.
        \\param[in]  theOther - the item ID to check equality with.
        \\return true if this ID is equal to theOther, otherwise - false.
        """

    def GetPath(self) -> nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]:
        """Returns the full path as a list of label entries."""

    def ToString(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the full pass as a formatted string."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __eq__(self, theOther: XCAFDoc_AssemblyItemId) -> bool: ...

    def __hash__(self) -> int: ...

class XCAFDoc_AssemblyItemRef(nanoocp.TDF.TDF_Attribute):
    """
    An attribute that describes a weak reference to an assembly item
    or to a subshape or to an assembly label attribute.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty reference attribute."""

    @overload
    def __init__(self, theOther: XCAFDoc_AssemblyItemRef) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Get(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_AssemblyItemRef:
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """

    @overload
    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId) -> XCAFDoc_AssemblyItemRef:
        """
        Create (if not exist) a reference to an assembly item.
        \\param[in]  theLabel  - label to add the attribute.
        \\param[in]  theItemId - assembly item ID.
        \\return A handle to the attribute instance.
        """

    @overload
    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef:
        """
        Create (if not exist) a reference to an assembly item's label attribute.
        \\param[in]  theLabel  - label to add the attribute.
        \\param[in]  theItemId - assembly item ID.
        \\param[in]  theGUID   - assembly item's label attribute ID.
        \\return A handle to the attribute instance.
        """

    @overload
    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theShapeIndex: int) -> XCAFDoc_AssemblyItemRef:
        """
        Create (if not exist) a reference to an assembly item's subshape.
        \\param[in]  theLabel      - label to add the attribute.
        \\param[in]  theItemId     - assembly item ID.
        \\param[in]  theShapeIndex - assembly item's subshape index.
        \\return A handle to the attribute instance.
        """

    def IsOrphan(self) -> bool:
        """
        Checks if the reference points to a really existing item in XDE document.
        """

    def HasExtraRef(self) -> bool:
        """Checks if the reference points on an item's shapeindex or attribute."""

    def IsGUID(self) -> bool:
        """Checks is the reference points to an item's attribute."""

    def IsSubshapeIndex(self) -> bool:
        """Checks is the reference points to an item's subshape."""

    def GetGUID(self) -> nanoocp.Standard.Standard_GUID:
        """
        Returns the assembly item's attribute that the reference points to.
        If the reference doesn't point to an attribute, returns an empty GUID.
        """

    def GetSubshapeIndex(self) -> int:
        """
        Returns the assembly item's subshape that the reference points to.
        If the reference doesn't point to a subshape, returns 0.
        """

    def GetItem(self) -> XCAFDoc_AssemblyItemId:
        """Returns the assembly item ID that the reference points to."""

    @overload
    def SetItem(self, theItemId: XCAFDoc_AssemblyItemId) -> None:
        """
        Sets the assembly item ID that the reference points to.
        Extra reference data (if any) will be cleared.
        """

    @overload
    def SetItem(self, thePath: nanoocp.NCollection.NCollection_List[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets the assembly item ID from a list of label entries
        that the reference points to.
        Extra reference data (if any) will be cleared.
        """

    @overload
    def SetItem(self, theString: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the assembly item ID from a formatted path
        that the reference points to.
        Extra reference data (if any) will be cleared.
        """

    def SetGUID(self, theAttrGUID: nanoocp.Standard.Standard_GUID) -> None:
        """
        Sets the assembly item's label attribute that the reference points to.
        The base assembly item will not change.
        """

    def SetSubshapeIndex(self, theShapeIndex: int) -> None:
        """
        Sets the assembly item's subshape that the reference points to.
        The base assembly item will not change.
        """

    def ClearExtraRef(self) -> None:
        """Reverts the reference to empty state."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Restore(self, theAttrFrom: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, theAttrInto: nanoocp.TDF.TDF_Attribute | None, theRT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

class XCAFDoc_AssemblyIterator:
    """Iterator in depth along the assembly tree."""

    @overload
    def __init__(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theLevel: int = 2147483647) -> None:
        """
        Constructs iterator starting from assembly roots.
        \\param[in]       theDoc   - document to iterate.
        \\param [in, opt] theLevel - max level of hierarchy to reach (INT_MAX is for no limit).
        """

    @overload
    def __init__(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None, theRoot: XCAFDoc_AssemblyItemId, theLevel: int = 2147483647) -> None:
        """
        Constructs iterator starting from the specified position in the assembly tree.
        \\param[in]       theDoc   - document to iterate.
        \\param[in]       theRoot  - assembly item to start iterating from.
        \\param [in, opt] theLevel - max level of hierarchy to reach (INT_MAX is for no limit).
        """

    @overload
    def __init__(self, theOther: XCAFDoc_AssemblyIterator) -> None: ...

    def __iter__(self) -> XCAFDoc_AssemblyIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> XCAFDoc_AssemblyItemId:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """
        \\return true if there is still something to iterate, false -- otherwise.
        """

    def Next(self) -> None:
        """Moves depth-first iterator to the next position."""

    def Current(self) -> XCAFDoc_AssemblyItemId:
        """\\return current item."""

class XCAFDoc_AssemblyGraph(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None) -> None:
        """
        \\brief Constructs graph from XCAF document.
        Construction of a formal graph will be done immediately.
        \\param[in]  theDoc - document to iterate.
        """

    @overload
    def __init__(self, theLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        \\brief Constructs graph from XCAF label.
        Construction of a formal graph will be done immediately. The specified
        label is used as a starting position.
        \\param[in]  theDoc   - document to iterate.
        \\param[in]  theLabel - starting position.
        """

    @overload
    def __init__(self, theOther: XCAFDoc_AssemblyGraph) -> None: ...

    class NodeType(enum.IntEnum):
        """\\brief Type of the graph node."""

        NodeType_UNDEFINED = 0

        NodeType_AssemblyRoot = 1

        NodeType_Subassembly = 2

        NodeType_Occurrence = 3

        NodeType_Part = 4

        NodeType_Subshape = 5

    NodeType_UNDEFINED: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_UNDEFINED

    NodeType_AssemblyRoot: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_AssemblyRoot

    NodeType_Subassembly: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_Subassembly

    NodeType_Occurrence: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_Occurrence

    NodeType_Part: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_Part

    NodeType_Subshape: XCAFDoc_AssemblyGraph.NodeType = NodeType.NodeType_Subshape

    class Iterator:
        """\\brief Graph iterator."""

        @overload
        def __init__(self, theGraph: XCAFDoc_AssemblyGraph | None, theNode: int = 1) -> None:
            """
            \\brief Accepting the assembly graph and starting node to iterate.
            Iteration starts from the specified node.
            \\param[in]  theGraph - assembly graph to iterate.
            \\param[in]  theNode  - graph node ID.
            """

        @overload
        def __init__(self, theOther: XCAFDoc_AssemblyGraph.Iterator) -> None: ...

        def __iter__(self) -> XCAFDoc_AssemblyGraph.Iterator:
            """
            Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
            """

        def __next__(self) -> int:
            """Python addition: see __iter__."""

        def More(self) -> bool:
            """
            Checks if there are more graph nodes to iterate.
            \\return true/false.
            """

        def Current(self) -> int:
            """\\return 1-based ID of the current node."""

        def Next(self) -> None:
            """Moves iterator to the next position."""

    def GetShapeTool(self) -> XCAFDoc_ShapeTool:
        """\\return Document shape tool."""

    def GetRoots(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger:
        """
        \\brief Returns IDs of the root nodes.
        \\return IDs of the root nodes.
        """

    def IsDirectLink(self, theNode1: int, theNode2: int) -> bool:
        """
        \\brief Checks whether the assembly graph contains (n1, n2) directed link.
        \\param[in]  theNode1 - one-based ID of the first node.
        \\param[in]  theNode2 - one-based ID of the second node.
        \\return true/false.
        """

    def HasChildren(self, theNode: int) -> bool:
        """
        \\brief Checks whether direct children exist for the given node.
        \\param[in]  theNode - one-based node ID.
        \\return true/false.
        """

    def GetChildren(self, theNode: int) -> nanoocp.TColStd.TColStd_PackedMapOfInteger:
        """
        \\brief Returns IDs of child nodes for the given node.
        \\param[in]  theNode - one-based node ID.
        \\return set of child IDs.
        """

    def GetNodeType(self, theNode: int) -> XCAFDoc_AssemblyGraph.NodeType:
        """
        \\brief Returns the node type from \\ref NodeType enum.
        \\param[in]  theNode - one-based node ID.
        \\return node type.
        \\sa NodeType
        """

    def GetNode(self, theNode: int) -> nanoocp.TDF.TDF_Label:
        """
        \\brief returns object ID by node ID.
        \\param[in]  theNode - one-based node ID.
        \\return persistent ID.
        """

    def GetNodes(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TDF.TDF_Label]:
        """
        \\brief Returns the unordered set of graph nodes.
        \\return graph nodes.
        """

    def NbNodes(self) -> int:
        """
        \\brief Returns the number of graph nodes.
        \\return number of graph nodes.
        """

    def GetLinks(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TColStd.TColStd_PackedMapOfInteger]:
        """
        \\brief Returns the collection of graph links in the form of adjacency matrix.
        \\return graph links.
        """

    def NbLinks(self) -> int:
        """
        \\brief Returns the number of graph links.
        \\return number of graph links.
        """

    def NbOccurrences(self, theNode: int) -> int:
        """
        Returns quantity of part usage occurrences.
        \\param[in]  theNode - one-based part ID.
        \\return usage occurrence quantity.
        """

class XCAFDoc_AssemblyTool:
    """Provides generic methods for traversing assembly tree and graph"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_AssemblyTool) -> None: ...

class XCAFDoc_Area(nanoocp.TDataStd.TDataStd_Real):
    """attribute to store area"""

    @overload
    def __init__(self) -> None:
        """
        class methods
        =============
        """

    @overload
    def __init__(self, theOther: XCAFDoc_Area) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Set(self, vol: float) -> None:
        """Sets a value of volume"""

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, area: float) -> XCAFDoc_Area:
        """Find, or create, an Area attribute and set its value"""

    def Get(self) -> float: ...

    @staticmethod
    def Get_s(label: nanoocp.TDF.TDF_Label) -> tuple[bool, float]:
        """
        Returns volume of area as argument and success status
        returns false if no such attribute at the <label>
        """

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Centroid(nanoocp.TDF.TDF_Attribute):
    """attribute to store centroid"""

    @overload
    def __init__(self) -> None:
        """
        class methods
        =============
        """

    @overload
    def __init__(self, theOther: XCAFDoc_Centroid) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, pnt: nanoocp.gp.gp_Pnt) -> XCAFDoc_Centroid:
        """
        Find, or create, a Location attribute and set it's value
        the Location attribute is returned.
        Location methods
        ===============
        """

    def Set(self, pnt: nanoocp.gp.gp_Pnt) -> None: ...

    def Get(self) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def Get_s(label: nanoocp.TDF.TDF_Label, pnt: nanoocp.gp.gp_Pnt) -> bool:
        """
        Returns point as argument
        returns false if no such attribute at the <label>
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_ClippingPlaneTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Provide tool for management of ClippingPlane section of document.
    Provide tool to store, retrieve, remove and modify clipping planes.
    Each clipping plane consists of gp_Pln and its name.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_ClippingPlaneTool) -> None: ...

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_ClippingPlaneTool:
        """Creates (if not exist) ClippingPlaneTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which ClippingPlanes are stored"""

    def IsClippingPlane(self, theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to a ClippingPlane table and
        is a ClippingPlane definition
        """

    @overload
    def GetClippingPlane(self, theLabel: nanoocp.TDF.TDF_Label, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_ExtendedString) -> tuple[bool, bool]: ...

    @overload
    def GetClippingPlane(self, theLabel: nanoocp.TDF.TDF_Label, thePlane: nanoocp.gp.gp_Pln) -> tuple[bool, nanoocp.TCollection.TCollection_HAsciiString, bool]:
        """
        Returns ClippingPlane defined by label lab
        Returns False if the label is not in ClippingPlane table
        or does not define a ClippingPlane
        """

    @overload
    def AddClippingPlane(self, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_ExtendedString, theCapping: bool) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddClippingPlane(self, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theCapping: bool) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddClippingPlane(self, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddClippingPlane(self, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label:
        """
        Adds a clipping plane definition to a ClippingPlane table and returns
        its label (returns existing label if the same clipping plane
        is already defined)
        """

    def RemoveClippingPlane(self, theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Removes clipping plane from the ClippingPlane table
        Return false and do nothing if clipping plane is referenced in at least one View
        """

    def GetClippingPlanes(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of clipping planes currently stored
        in the ClippingPlane table
        """

    def UpdateClippingPlane(self, theLabelL: nanoocp.TDF.TDF_Label, thePlane: nanoocp.gp.gp_Pln, theName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Sets new value of plane and name to the given clipping plane label
        or do nothing, if the given label is not a clipping plane label
        """

    def SetCapping(self, theClippingPlaneL: nanoocp.TDF.TDF_Label, theCapping: bool) -> None:
        """Set new value of capping for given clipping plane label"""

    def GetCapping(self, theClippingPlaneL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Get capping value for given clipping plane label
        Return capping value
        """

    def GetCapping__bool(self, theClippingPlaneL: nanoocp.TDF.TDF_Label) -> tuple[bool, bool]:
        """
        GetCapping__bool: the C++ overload GetCapping(const TDF_Label &, bool &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Get capping value for given clipping plane label
        Return true if Label is valid and capping exists.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Color(nanoocp.TDF.TDF_Attribute):
    """attribute to store color"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_Color) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, C: nanoocp.Quantity.Quantity_Color) -> XCAFDoc_Color: ...

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, C: nanoocp.Quantity.Quantity_ColorRGBA) -> XCAFDoc_Color: ...

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, C: nanoocp.Quantity.Quantity_NameOfColor) -> XCAFDoc_Color: ...

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, R: float, G: float, B: float, alpha: float = 1.0) -> XCAFDoc_Color:
        """
        Find, or create, a Color attribute and set it's value
        the Color attribute is returned.
        """

    @overload
    def Set(self, C: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def Set(self, C: nanoocp.Quantity.Quantity_ColorRGBA) -> None: ...

    @overload
    def Set(self, C: nanoocp.Quantity.Quantity_NameOfColor) -> None: ...

    @overload
    def Set(self, R: float, G: float, B: float, alpha: float = 1.0) -> None: ...

    def GetColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    def GetColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA: ...

    def GetNOC(self) -> nanoocp.Quantity.Quantity_NameOfColor: ...

    def GetRGB(self) -> tuple[float, float, float]: ...

    def GetAlpha(self) -> float: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_ColorTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Provides tools to store and retrieve attributes (colors)
    of TopoDS_Shape in and from TDocStd_Document
    A Document is intended to hold different
    attributes of ONE shape and it's sub-shapes
    Provide tools for management of Colors section of document.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_ColorTool) -> None: ...

    @staticmethod
    def AutoNaming() -> bool:
        """
        Returns current auto-naming mode; TRUE by default.
        If TRUE then for added colors the TDataStd_Name attribute will be automatically added.
        This setting is global.
        """

    @staticmethod
    def SetAutoNaming(theIsAutoNaming: bool) -> None:
        """See also AutoNaming()."""

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_ColorTool:
        """Creates (if not exist) ColorTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which colors are stored"""

    def ShapeTool(self) -> XCAFDoc_ShapeTool:
        """Returns internal XCAFDoc_ShapeTool tool"""

    def IsColor(self, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to a colortable and
        is a color definition
        """

    @overload
    @staticmethod
    def GetColor_s(lab: nanoocp.TDF.TDF_Label, col: nanoocp.Quantity.Quantity_Color) -> bool: ...

    @overload
    @staticmethod
    def GetColor_s(lab: nanoocp.TDF.TDF_Label, col: nanoocp.Quantity.Quantity_ColorRGBA) -> bool:
        """
        Returns color defined by label lab
        Returns False if the label is not in colortable
        or does not define a color
        """

    @overload
    @staticmethod
    def GetColor_s(L: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType, colorL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns label with color assigned to <L> as <type>
        Returns False if no such color is assigned
        """

    @overload
    @staticmethod
    def GetColor_s(L: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_Color) -> bool: ...

    @overload
    @staticmethod
    def GetColor_s(L: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_ColorRGBA) -> bool:
        """
        Returns color assigned to <L> as <type>
        Returns False if no such color is assigned
        """

    @overload
    def FindColor(self, col: nanoocp.Quantity.Quantity_Color, lab: nanoocp.TDF.TDF_Label) -> bool: ...

    @overload
    def FindColor(self, col: nanoocp.Quantity.Quantity_ColorRGBA, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Finds a color definition in a colortable and returns
        its label if found
        Returns False if color is not found in colortable
        """

    @overload
    def FindColor(self, col: nanoocp.Quantity.Quantity_Color) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def FindColor(self, col: nanoocp.Quantity.Quantity_ColorRGBA) -> nanoocp.TDF.TDF_Label:
        """
        Finds a color definition in a colortable and returns
        its label if found (or Null label else)
        """

    @overload
    def AddColor(self, col: nanoocp.Quantity.Quantity_Color) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddColor(self, col: nanoocp.Quantity.Quantity_ColorRGBA) -> nanoocp.TDF.TDF_Label:
        """
        Adds a color definition to a colortable and returns
        its label (returns existing label if the same color
        is already defined)
        """

    def RemoveColor(self, lab: nanoocp.TDF.TDF_Label) -> None:
        """Removes color from the colortable"""

    def GetColors(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of colors currently stored
        in the colortable
        """

    @overload
    def SetColor(self, L: nanoocp.TDF.TDF_Label, colorL: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType) -> None:
        """
        Sets a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color
        defined by <colorL>. Color of shape is defined following way
        in dependance with type of color.
        If type of color is XCAFDoc_ColorGen - then this color
        defines default color for surfaces and curves.
        If for shape color with types XCAFDoc_ColorSurf or XCAFDoc_ColorCurv is specified
        then such color overrides generic color.
        """

    @overload
    def SetColor(self, L: nanoocp.TDF.TDF_Label, Color: nanoocp.Quantity.Quantity_Color, type: XCAFDoc_ColorType) -> None: ...

    @overload
    def SetColor(self, L: nanoocp.TDF.TDF_Label, Color: nanoocp.Quantity.Quantity_ColorRGBA, type: XCAFDoc_ColorType) -> None:
        """
        Sets a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color <Color>
        in the colortable
        Adds a color as necessary
        """

    @overload
    def SetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, colorL: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType) -> bool:
        """
        Sets a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color
        defined by <colorL>
        Returns False if cannot find a label for shape S
        """

    @overload
    def SetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, Color: nanoocp.Quantity.Quantity_Color, type: XCAFDoc_ColorType) -> bool: ...

    @overload
    def SetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, Color: nanoocp.Quantity.Quantity_ColorRGBA, type: XCAFDoc_ColorType) -> bool:
        """
        Sets a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color <Color>
        in the colortable
        Adds a color as necessary
        Returns False if cannot find a label for shape S
        """

    @overload
    def UnSetColor(self, L: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType) -> None:
        """
        Removes a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color
        """

    @overload
    def UnSetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType) -> bool:
        """
        Removes a link with GUID defined by <type> (see
        XCAFDoc::ColorRefGUID()) from label <L> to color
        Returns True if such link existed
        """

    @overload
    def IsSet(self, L: nanoocp.TDF.TDF_Label, type: XCAFDoc_ColorType) -> bool: ...

    @overload
    def IsSet(self, S: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType) -> bool:
        """
        Returns True if label <L> has a color assignment
        of the type <type>
        """

    @overload
    def GetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, colorL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns label with color assigned to <L> as <type>
        Returns False if no such color is assigned
        """

    @overload
    def GetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_Color) -> bool: ...

    @overload
    def GetColor(self, S: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_ColorRGBA) -> bool:
        """
        Returns color assigned to <L> as <type>
        Returns False if no such color is assigned
        """

    @staticmethod
    def IsVisible(L: nanoocp.TDF.TDF_Label) -> bool:
        """Return TRUE if object on this label is visible, FALSE if invisible."""

    def SetVisibility(self, shapeLabel: nanoocp.TDF.TDF_Label, isvisible: bool = True) -> None:
        """
        Set the visibility of object on label. Do nothing if there no any object.
        Set UAttribute with corresponding GUID.
        """

    def IsColorByLayer(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """Return TRUE if object color defined by its Layer, FALSE if not."""

    def SetColorByLayer(self, shapeLabel: nanoocp.TDF.TDF_Label, isColorByLayer: bool = False) -> None:
        """
        Set the Color defined by Layer flag on label. Do nothing if there no any object.
        Set UAttribute with corresponding GUID.
        """

    @overload
    def SetInstanceColor(self, theShape: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_Color, isCreateSHUO: bool = True) -> bool: ...

    @overload
    def SetInstanceColor(self, theShape: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_ColorRGBA, isCreateSHUO: bool = True) -> bool:
        """
        Sets the color of component that styled with SHUO structure
        Returns FALSE if no sush component found
        NOTE: create SHUO structeure if it is necessary and if <isCreateSHUO>
        """

    @overload
    def GetInstanceColor(self, theShape: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_Color) -> bool: ...

    @overload
    def GetInstanceColor(self, theShape: nanoocp.TopoDS.TopoDS_Shape, type: XCAFDoc_ColorType, color: nanoocp.Quantity.Quantity_ColorRGBA) -> bool:
        """
        Gets the color of component that styled with SHUO structure
        Returns FALSE if no sush component or color type
        """

    def IsInstanceVisible(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Gets the visibility status of component that styled with SHUO structure
        Returns FALSE if no sush component
        """

    def ReverseChainsOfTreeNodes(self) -> bool:
        """
        Reverses order in chains of TreeNodes (from Last to First) under
        each Color Label since we became to use function ::Prepend()
        instead of ::Append() in method SetColor() for acceleration
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Datum(nanoocp.TDF.TDF_Attribute):
    """attribute to store datum"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_Datum) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @overload
    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, anIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> XCAFDoc_Datum: ...

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_Datum: ...

    def Set(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, anIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def GetName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetDescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetIdentification(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetObject(self) -> nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject:
        """
        Returns dimension object data taken from the paren's label and its sub-labels.
        """

    def SetObject(self, theDatumObject: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject | None) -> None:
        """
        Updates parent's label and its sub-labels with data taken from theDatumObject.
        Old data associated with the label will be lost.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_Dimension(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Attribute that identifies a dimension in the GD&T table.
    Its parent label is used as a container to store data provided
    by XCAFDimTolObjects_DimensionObject.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_Dimension) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_Dimension: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def SetObject(self, theDimensionObject: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject | None) -> None:
        """
        Updates parent's label and its sub-labels with data taken from theDimensionObject.
        Old data associated with the label will be lost.
        """

    def GetObject(self) -> nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject:
        """
        Returns dimension object data taken from the parent's label and its sub-labels.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_GeomTolerance(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """Attribute to store dimension and tolerance"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_GeomTolerance) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_GeomTolerance: ...

    def SetObject(self, theGeomToleranceObject: nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject | None) -> None:
        """
        Updates parent's label and its sub-labels with data taken from theGeomToleranceObject.
        Old data associated with the label will be lost.
        """

    def GetObject(self) -> nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject:
        """
        Returns geometry tolerance object data taken from the paren's label and its sub-labels.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_DimTol(nanoocp.TDF.TDF_Attribute):
    """attribute to store dimension and tolerance"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_DimTol) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, kind: int, aVal: nanoocp.NCollection.NCollection_HArray1[float] | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> XCAFDoc_DimTol: ...

    def Set(self, kind: int, aVal: nanoocp.NCollection.NCollection_HArray1[float] | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def GetKind(self) -> int: ...

    def GetVal(self) -> nanoocp.NCollection.NCollection_HArray1[float]: ...

    def GetName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetDescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_DimTolTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Attribute containing GD&T section of XCAF document.
    Provide tools for GD&T section management.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_DimTolTool) -> None: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_DimTolTool:
        """Creates (if not exist) DimTolTool attribute."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the standard GD&T tool GUID."""

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label under which GD&T table is stored."""

    def ShapeTool(self) -> XCAFDoc_ShapeTool:
        """Returns internal XCAFDoc_ShapeTool tool"""

    def IsDimension(self, theLab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label belongs to a GD&T table and
        is a Dimension definition.
        """

    def GetDimensionLabels(self, theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of Dimension labels currently stored
        in the GD&T table.
        """

    @overload
    def SetDimension(self, theFirstLS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theSecondLS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theDimL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a dimension to sequences target labels."""

    @overload
    def SetDimension(self, theFirstL: nanoocp.TDF.TDF_Label, theSecondL: nanoocp.TDF.TDF_Label, theDimL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a dimension to target labels."""

    @overload
    def SetDimension(self, theL: nanoocp.TDF.TDF_Label, theDimL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a dimension to the target label."""

    def GetRefDimensionLabels(self, theShapeL: nanoocp.TDF.TDF_Label, theDimensions: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all Dimension labels defined for theShapeL."""

    def AddDimension(self) -> nanoocp.TDF.TDF_Label:
        """Adds a dimension definition to the GD&T table and returns its label."""

    def IsGeomTolerance(self, theLab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label belongs to the GD&T table and is a dimension tolerance.
        """

    def GetGeomToleranceLabels(self, theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of Tolerance labels currently stored in the GD&T table.
        """

    @overload
    def SetGeomTolerance(self, theL: nanoocp.TDF.TDF_Label, theGeomTolL: nanoocp.TDF.TDF_Label) -> None:
        """
        Sets a geometry tolerance from theGeomTolL to theL label.
        Checks if theGeomTolL is a geometry tolerance definition first.
        """

    @overload
    def SetGeomTolerance(self, theL: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theGeomTolL: nanoocp.TDF.TDF_Label) -> None:
        """
        Sets a geometry tolerance from theGeomTolL to sequence of labels theL.
        Checks if theGeomTolL is a geometry tolerance definition first.
        """

    def GetRefGeomToleranceLabels(self, theShapeL: nanoocp.TDF.TDF_Label, theDimTols: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all GeomTolerance labels defined for theShapeL."""

    def AddGeomTolerance(self) -> nanoocp.TDF.TDF_Label:
        """
        Adds a GeomTolerance definition to the GD&T table and returns its label.
        """

    def IsDimTol(self, theLab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if theLab belongs to the GD&T table and is a dmension tolerance.
        """

    def GetDimTolLabels(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """Returns a sequence of D&GTs currently stored in the GD&T table."""

    @overload
    def FindDimTol(self, theKind: int, theVal: nanoocp.NCollection.NCollection_HArray1[float] | None, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Finds a dimension tolerance definition in the GD&T table
        satisfying the specified kind, values, name and description
        and returns its label if found.
        Returns False if dimension tolerance is not found in DGTtable.
        """

    @overload
    def FindDimTol(self, theKind: int, theVal: nanoocp.NCollection.NCollection_HArray1[float] | None, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label:
        """
        Finds a dimension tolerance in the GD&T table
        satisfying the specified kind, values, name and description
        and returns its label if found (or Null label else).
        """

    def AddDimTol(self, theKind: int, theVal: nanoocp.NCollection.NCollection_HArray1[float] | None, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label:
        """
        Adds a dimension tolerance definition with the specified
        kind, value, name and description to the GD&T table and returns its label.
        """

    @overload
    def SetDimTol(self, theL: nanoocp.TDF.TDF_Label, theDimTolL: nanoocp.TDF.TDF_Label) -> None:
        """Sets existing dimension tolerance to theL label."""

    @overload
    def SetDimTol(self, theL: nanoocp.TDF.TDF_Label, theKind: int, theVal: nanoocp.NCollection.NCollection_HArray1[float] | None, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label:
        """Creates a dimension tolerance and sets it to theL label."""

    @staticmethod
    def GetRefShapeLabel(theL: nanoocp.TDF.TDF_Label, theShapeLFirst: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theShapeLSecond: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Gets all shape labels referred by theL label of the GD&T table.
        Returns False if there are no shape labels added to the sequences.
        """

    def GetDimTol(self, theDimTolL: nanoocp.TDF.TDF_Label) -> tuple[bool, int, nanoocp.NCollection.NCollection_HArray1[float], nanoocp.TCollection.TCollection_HAsciiString, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns dimension tolerance assigned to theDimTolL label.
        Returns False if no such dimension tolerance is assigned.
        """

    def IsDatum(self, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to the GD&T table and
        is a Datum definition.
        """

    def GetDatumLabels(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of Datums currently stored
        in the GD&T table.
        """

    def FindDatum(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theIdentification: nanoocp.TCollection.TCollection_HAsciiString | None, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Finds a datum satisfying the specified name, description and
        identification and returns its label if found.
        """

    @overload
    def AddDatum(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddDatum(self) -> nanoocp.TDF.TDF_Label:
        """Adds a datum definition to the GD&T table and returns its label."""

    @overload
    def SetDatum(self, theShapeLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theDatumL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a datum to the sequence of shape labels."""

    @overload
    def SetDatum(self, theL: nanoocp.TDF.TDF_Label, theTolerL: nanoocp.TDF.TDF_Label, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Sets a datum to theL label and binds it with theTolerL label.
        A datum with the specified name, description and identification
        is created if it isn't found in the GD&T table.
        """

    def SetDatumToGeomTol(self, theDatumL: nanoocp.TDF.TDF_Label, theTolerL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a datum from theDatumL label to theToletL label."""

    def GetDatum(self, theDatumL: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.TCollection.TCollection_HAsciiString, nanoocp.TCollection.TCollection_HAsciiString, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns datum assigned to theDatumL label.
        Returns False if no such datum is assigned.
        """

    @staticmethod
    def GetDatumOfTolerLabels(theDimTolL: nanoocp.TDF.TDF_Label, theDatums: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all Datum labels defined for theDimTolL label."""

    @staticmethod
    def GetDatumWithObjectOfTolerLabels(theDimTolL: nanoocp.TDF.TDF_Label, theDatums: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns all Datum labels with XCAFDimTolObjects_DatumObject defined for label theDimTolL.
        """

    def GetTolerOfDatumLabels(self, theDatumL: nanoocp.TDF.TDF_Label, theTols: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all GeomToleranses labels defined for theDatumL label."""

    def GetRefDatumLabel(self, theShapeL: nanoocp.TDF.TDF_Label, theDatum: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns Datum label defined for theShapeL label."""

    def IsLocked(self, theViewL: nanoocp.TDF.TDF_Label) -> bool:
        """Returns true if the given GDT is marked as locked."""

    def Lock(self, theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Mark the given GDT as locked."""

    def GetGDTPresentations(self, theGDTLabelToShape: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TDF.TDF_Label, nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """fill the map GDT label -> shape presentation"""

    def SetGDTPresentations(self, theGDTLabelToPrs: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TDF.TDF_Label, nanoocp.TopoDS.TopoDS_Shape]) -> None:
        """
        Set shape presentation for GDT labels according to given map (theGDTLabelToPrs)
        theGDTLabelToPrsName map is an additional argument, can be used to set presentation names.
        If label is not in the theGDTLabelToPrsName map, the presentation name will be empty
        """

    def Unlock(self, theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Unlock the given GDT."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_DocumentTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Defines sections structure of an XDE document.
    attribute marking CAF document as being DECAF document.
    Creates the sections structure of the document.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_DocumentTool) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label, IsAcces: bool = True) -> XCAFDoc_DocumentTool:
        """
        Create (if not exist) DocumentTool attribute
        on 0.1 label if <IsAcces> is true, else
        on <L> label.
        This label will be returned by DocLabel();
        If the attribute is already set it won't be reset on
        <L> even if <IsAcces> is false.
        ColorTool and ShapeTool attributes are also set by this method.
        """

    @staticmethod
    def IsXCAFDocument(Doc: nanoocp.TDocStd.TDocStd_Document | None) -> bool: ...

    @staticmethod
    def DocLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """
        Returns label where the DocumentTool attribute is or
        0.1 if DocumentTool is not yet set.
        """

    @staticmethod
    def ShapesLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 1."""

    @staticmethod
    def ColorsLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 2."""

    @staticmethod
    def LayersLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 3."""

    @staticmethod
    def DGTsLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 4."""

    @staticmethod
    def MaterialsLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 5."""

    @staticmethod
    def ViewsLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 7."""

    @staticmethod
    def ClippingPlanesLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 8."""

    @staticmethod
    def NotesLabel(acces: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 9."""

    @staticmethod
    def VisMaterialLabel(theLabel: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """Returns sub-label of DocLabel() with tag 10."""

    @staticmethod
    def ShapeTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_ShapeTool:
        """Creates (if it does not exist) ShapeTool attribute on ShapesLabel()."""

    @staticmethod
    def CheckShapeTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the ShapeTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def ColorTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_ColorTool:
        """Creates (if it does not exist) ColorTool attribute on ColorsLabel()."""

    @staticmethod
    def CheckColorTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the ColorTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def VisMaterialTool(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_VisMaterialTool:
        """
        Creates (if it does not exist) XCAFDoc_VisMaterialTool attribute on VisMaterialLabel().
        Should not be confused with MaterialTool() defining physical/manufacturing materials.
        """

    @staticmethod
    def CheckVisMaterialTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the VisMaterialTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def LayerTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_LayerTool:
        """Creates (if it does not exist) LayerTool attribute on LayersLabel()."""

    @staticmethod
    def CheckLayerTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the LayerTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def DimTolTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_DimTolTool:
        """Creates (if it does not exist) DimTolTool attribute on DGTsLabel()."""

    @staticmethod
    def CheckDimTolTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the DimTolTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def MaterialTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_MaterialTool:
        """Creates (if it does not exist) DimTolTool attribute on DGTsLabel()."""

    @staticmethod
    def CheckMaterialTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the MaterialTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def ViewTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_ViewTool:
        """Creates (if it does not exist) ViewTool attribute on ViewsLabel()."""

    @staticmethod
    def CheckViewTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the ViewTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def ClippingPlaneTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_ClippingPlaneTool:
        """
        Creates (if it does not exist) ClippingPlaneTool attribute on ClippingPlanesLabel().
        """

    @staticmethod
    def CheckClippingPlaneTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the ClippingPlaneTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @staticmethod
    def NotesTool(acces: nanoocp.TDF.TDF_Label) -> XCAFDoc_NotesTool:
        """Creates (if it does not exist) NotesTool attribute on NotesLabel()."""

    @staticmethod
    def CheckNotesTool(theAcces: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks for the NotesTool attribute on the label's document
        Returns TRUE if Tool exists, ELSE if it has not been created
        """

    @overload
    @staticmethod
    def GetLengthUnit(theDoc: nanoocp.TDocStd.TDocStd_Document | None, theBaseUnit: nanoocp.UnitsMethods.UnitsMethods_LengthUnit) -> tuple[bool, float]:
        """
        Returns value of current internal unit for the document
        converted to base unit type.
        """

    @overload
    @staticmethod
    def GetLengthUnit(theDoc: nanoocp.TDocStd.TDocStd_Document | None) -> tuple[bool, float]:
        """Returns value of current internal unit for the document in meter"""

    @overload
    @staticmethod
    def SetLengthUnit(theDoc: nanoocp.TDocStd.TDocStd_Document | None, theUnitValue: float) -> None:
        """Sets value of current internal unit to the document in meter"""

    @overload
    @staticmethod
    def SetLengthUnit(theDoc: nanoocp.TDocStd.TDocStd_Document | None, theUnitValue: float, theBaseUnit: nanoocp.UnitsMethods.UnitsMethods_LengthUnit) -> None:
        """
        Sets value of current internal unit to the document
        @param theUnitValue must be represented in the base unit type
        """

    def Init(self) -> None:
        """to be called when reading this attribute from file"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def AfterRetrieval(self, forceIt: bool = False) -> bool:
        """
        To init this derived attribute after the attribute restore using the base restore-methods
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Editor:
    """Tool for edit structure of document."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_Editor) -> None: ...

    @overload
    @staticmethod
    def Expand(theDoc: nanoocp.TDF.TDF_Label, theShape: nanoocp.TDF.TDF_Label, theRecursively: bool = True) -> bool:
        """
        Converts shape (compound/compsolid/shell/wire) to assembly.
        @param[in] theDoc input document
        @param[in] theShape input shape label
        @param[in] theRecursively recursively expand a compound subshape
        @return True if shape successfully expanded
        """

    @overload
    @staticmethod
    def Expand(theDoc: nanoocp.TDF.TDF_Label, theRecursively: bool = True) -> bool:
        """
        Converts all compounds shapes in the document to assembly
        @param[in] theDoc input document
        @param[in] theRecursively recursively expand a compound subshape
        @return True if shape successfully expanded
        """

    @overload
    @staticmethod
    def Extract(theSrcLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theDstLabel: nanoocp.TDF.TDF_Label, theIsNoVisMat: bool = False) -> bool:
        """
        Clones all labels to a new position, keeping the structure with all the attributes
        @param[in] theSrcLabels original labels to copy from
        @param[in] theDstLabel label to set result as a component of or a main document's label to
        simply set new shape
        @param[in] theIsNoVisMat get a VisMaterial attributes as is or convert to color
        @return True if shape successfully extracted
        """

    @overload
    @staticmethod
    def Extract(theSrcLabel: nanoocp.TDF.TDF_Label, theDstLabel: nanoocp.TDF.TDF_Label, theIsNoVisMat: bool = False) -> bool:
        """
        Clones the label to a new position, keeping the structure with all the attributes
        @param[in] theSrcLabel original label to copy from
        @param[in] theDstLabel label to set result as a component of or a main document's label to
        simply set new shape
        @param[in] theIsNoVisMat get a VisMaterial attributes as is or convert to color
        @return True if shape successfully extracted
        """

    @staticmethod
    def CloneShapeLabel(theSrcLabel: nanoocp.TDF.TDF_Label, theSrcShapeTool: XCAFDoc_ShapeTool | None, theDstShapeTool: XCAFDoc_ShapeTool | None, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.TDF.TDF_Label, nanoocp.TDF.TDF_Label]) -> nanoocp.TDF.TDF_Label:
        """
        Copies shapes label with keeping of shape structure (recursively)
        @param[in] theSrcLabel original label to copy from
        @param[in] theSrcShapeTool shape tool to get
        @param[in] theDstShapeTool shape tool to set
        @param[out] theMap relating map of the original shapes label and labels created from them
        @return result shape label
        """

    @staticmethod
    def CloneMetaData(theSrcLabel: nanoocp.TDF.TDF_Label, theDstLabel: nanoocp.TDF.TDF_Label, theVisMatMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.XCAFDoc.XCAFDoc_VisMaterial, nanoocp.XCAFDoc.XCAFDoc_VisMaterial], theToCopyColor: bool = True, theToCopyLayer: bool = True, theToCopyMaterial: bool = True, theToCopyVisMaterial: bool = True, theToCopyAttributes: bool = True) -> None:
        """
        Copies metadata contains from the source label to the destination label.
        Protected against creating a new label for non-existent tools
        @param[in] theSrcLabel original label to copy from
        @param[in] theDstLabel destination shape label to set attributes
        @param[in] theVisMatMap relating map of the original VisMaterial and created. Can be NULL for
        the same document
        @param[in] theToCopyColor copying visible value and shape color (handled all color type)
        @param[in] theToCopyLayer copying layer
        @param[in] theToCopyMaterial copying  material
        @param[in] theToCopyVisMaterial copying visual material
        @param[in] theToCopyAttributes copying of other node attributes, for example, a shape's
        property
        """

    @staticmethod
    def GetParentShapeLabels(theLabel: nanoocp.TDF.TDF_Label, theRelatedLabels: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None:
        """
        Gets shape labels that has down relation with the input label.
        @param[in] theLabel input label
        @param[out] theRelatedLabels output labels
        """

    @staticmethod
    def GetChildShapeLabels(theLabel: nanoocp.TDF.TDF_Label, theRelatedLabels: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> None:
        """
        Gets shape labels that has up relation with the input label.
        @param[in] theLabel input label
        @param[out] theRelatedLabels output labels
        """

    @staticmethod
    def FilterShapeTree(theShapeTool: XCAFDoc_ShapeTool | None, theLabelsToKeep: nanoocp.NCollection.NCollection_Map[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Filters original shape tree with keeping structure.
        The result will include the full label hierarchy lower then input labels.
        Any higher hierarchy labels will be filtered to keep only necessary labels.
        All not related shape labels with input will be cleared (all attributes will be removed).

        The result impact directly into original document and existed shape labels.
        Attributes related to removed shape can became invalide.
        For example, GDT with relation on removed shape label(s) and without
        attachment point(s) became invalid for visualization.

        @param[in] theShapeTool shape tool to extract from
        @param[in] theLabelsToKeep labels to keep
        @return true if the tree was filtered successfully.
        """

    @staticmethod
    def RescaleGeometry(theLabel: nanoocp.TDF.TDF_Label, theScaleFactor: float, theForceIfNotRoot: bool = False) -> bool:
        """
        Applies geometrical scaling to the following assembly components:
        - part geometry
        - sub-assembly/part occurrence location
        - part's centroid, area and volume attributes
        - PMIs (warnings and errors are reported if it is impossible to make changes)
        Normally, should start from a root sub-assembly, but if theForceIfNotRoot true
        scaling will be applied forcibly. If theLabel corresponds to the shape tool
        scaling is applied to the whole assembly.
        @param[in] theLabel starting label
        @param[in] theScaleFactor scale factor, should be positive
        @param[in] theForceIfNotRoot allows scaling of a non root assembly if true,
        otherwise - returns false
        @return true in case of success, otherwise - false.
        """

class XCAFDoc_GraphNode(nanoocp.TDF.TDF_Attribute):
    """
    This attribute allow user multirelation tree of labels.
    This GraphNode is experimental Graph that not control looping and redundance.
    Attribute containing sequence of father's and child's labels.
    Provide create and work with Graph in XCAFDocument.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_GraphNode) -> None: ...

    @staticmethod
    def Find(L: nanoocp.TDF.TDF_Label) -> tuple[bool, XCAFDoc_GraphNode]:
        """
        class methods working on the node
        =================================
        Shortcut to search a Graph node attribute with default
        GraphID. Returns true if found.
        """

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_GraphNode:
        """
        Finds or Creates a GraphNode attribute on the label <L>
        with the default Graph ID, returned by the method
        <GetDefaultGraphID>. Returns the created/found GraphNode
        attribute.
        """

    @overload
    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label, ExplicitGraphID: nanoocp.Standard.Standard_GUID) -> XCAFDoc_GraphNode:
        """
        Finds or Creates a GraphNode attribute on the label
        <L>, with an explicit tree ID. <ExplicitGraphID> is
        the ID returned by <TDF_Attribute::ID> method.
        Returns the found/created GraphNode attribute.
        """

    @staticmethod
    def GetDefaultGraphID() -> nanoocp.Standard.Standard_GUID:
        """
        returns a default Graph ID. this ID is used by the
        <Set> method without explicit tree ID.
        Instance methods:
        ================
        """

    def SetGraphID(self, explicitID: nanoocp.Standard.Standard_GUID) -> None: ...

    def SetFather(self, F: XCAFDoc_GraphNode | None) -> int:
        """
        Set GraphNode <F> as father of me and returns index of <F>
        in Sequence that containing Fathers GraphNodes.
        return index of <F> from GraphNodeSequnece
        """

    def SetChild(self, Ch: XCAFDoc_GraphNode | None) -> int:
        """
        Set GraphNode <Ch> as child of me and returns index of <Ch>
        in Sequence that containing Children GraphNodes.
        return index of <Ch> from GraphNodeSequnece
        """

    @overload
    def UnSetFather(self, F: XCAFDoc_GraphNode | None) -> None:
        """
        Remove <F> from Fathers GraphNodeSequence.
        and remove link between father and child.
        """

    @overload
    def UnSetFather(self, Findex: int) -> None:
        """
        Remove Father GraphNode by index from Fathers GraphNodeSequence.
        and remove link between father and child.
        """

    @overload
    def UnSetChild(self, Ch: XCAFDoc_GraphNode | None) -> None:
        """
        Remove <Ch> from GraphNodeSequence.
        and remove link between father and child.
        """

    @overload
    def UnSetChild(self, Chindex: int) -> None:
        """
        Remove Child GraphNode by index from Children GraphNodeSequence.
        and remove link between father and child.
        """

    def GetFather(self, Findex: int) -> XCAFDoc_GraphNode:
        """Return GraphNode by index from GraphNodeSequence."""

    def GetChild(self, Chindex: int) -> XCAFDoc_GraphNode:
        """Return GraphNode by index from GraphNodeSequence."""

    def FatherIndex(self, F: XCAFDoc_GraphNode | None) -> int:
        """Return index of <F>, or zero if there is no such Graphnode."""

    def ChildIndex(self, Ch: XCAFDoc_GraphNode | None) -> int:
        """Return index of <Ch>, or zero if there is no such Graphnode."""

    def IsFather(self, Ch: XCAFDoc_GraphNode | None) -> bool:
        """returns TRUE if <me> is father of <Ch>."""

    def IsChild(self, F: XCAFDoc_GraphNode | None) -> bool:
        """returns TRUE if <me> is child of <F>."""

    def NbFathers(self) -> int:
        """return Number of Fathers GraphNodes."""

    def NbChildren(self) -> int:
        """
        return Number of Childrens GraphNodes.
        Implementation of Attribute methods:
        ===================================
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """
        Returns the Graph ID (default or explicit one depending
        on the Set method used).
        """

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def References(self, aDataSet: nanoocp.TDF.TDF_DataSet | None) -> None: ...

    def Dump(self) -> str: ...

    def BeforeForget(self) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_LayerTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Provides tools to store and retrieve attributes (Layers)
    of TopoDS_Shape in and from TDocStd_Document
    A Document is intended to hold different
    attributes of ONE shape and it's sub-shapes
    Provide tools for management of Layers section of document.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_LayerTool) -> None: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_LayerTool:
        """Creates (if not exist) LayerTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which Layers are stored"""

    def ShapeTool(self) -> XCAFDoc_ShapeTool:
        """Returns internal XCAFDoc_ShapeTool tool"""

    def IsLayer(self, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to a Layertable and
        is a Layer definition
        """

    def GetLayer(self, lab: nanoocp.TDF.TDF_Label, aLayer: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns Layer defined by label lab
        Returns False if the label is not in Layertable
        or does not define a Layer
        """

    @overload
    def FindLayer(self, aLayer: nanoocp.TCollection.TCollection_ExtendedString, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Finds a Layer definition in a Layertable and returns
        its label if found
        Returns False if Layer is not found in Layertable
        """

    @overload
    def FindLayer(self, aLayer: nanoocp.TCollection.TCollection_ExtendedString, theToFindWithProperty: bool = False, theToFindVisible: bool = True) -> nanoocp.TDF.TDF_Label:
        """
        Finds a Layer definition in a Layertable by name
        Returns first founded label with the same name if <theToFindWithProperty> is false
        If <theToFindWithProperty> is true returns first label that
        contains or not contains visible attr, according to the <theToFindVisible> parameter
        """

    @overload
    def AddLayer(self, theLayer: nanoocp.TCollection.TCollection_ExtendedString) -> nanoocp.TDF.TDF_Label:
        """
        Adds a Layer definition to a Layertable and returns
        its label (returns existing label if the same Layer
        is already defined)
        """

    @overload
    def AddLayer(self, theLayer: nanoocp.TCollection.TCollection_ExtendedString, theToFindVisible: bool) -> nanoocp.TDF.TDF_Label:
        """
        Adds a Layer definition to a Layertable and returns its label
        Returns existing label (if it is already defined)
        of visible or invisible layer, according to <theToFindVisible> parameter
        """

    def RemoveLayer(self, lab: nanoocp.TDF.TDF_Label) -> None:
        """Removes Layer from the Layertable"""

    def GetLayerLabels(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of Layers currently stored
        in the Layertable
        """

    @overload
    def SetLayer(self, L: nanoocp.TDF.TDF_Label, LayerL: nanoocp.TDF.TDF_Label, shapeInOneLayer: bool = False) -> None:
        """
        Sets a link from label <L> to Layer
        defined by <LayerL>
        optional parameter <shapeInOneLayer> show could shape be
        in number of layers or only in one.
        """

    @overload
    def SetLayer(self, L: nanoocp.TDF.TDF_Label, aLayer: nanoocp.TCollection.TCollection_ExtendedString, shapeInOneLayer: bool = False) -> None:
        """
        Sets a link from label <L> to Layer <aLayer>
        in the Layertable
        Adds a Layer as necessary
        optional parameter <shapeInOneLayer> show could shape be
        in number of layers or only in one.
        """

    @overload
    def SetLayer(self, Sh: nanoocp.TopoDS.TopoDS_Shape, LayerL: nanoocp.TDF.TDF_Label, shapeInOneLayer: bool = False) -> bool:
        """
        Sets a link from label that containing shape <Sh>
        with layer that situated at label <LayerL>.
        optional parameter <shapeInOneLayer> show could shape be
        in number of layers or only in one.
        return FALSE if no such shape <Sh> or label <LayerL>
        """

    @overload
    def SetLayer(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayer: nanoocp.TCollection.TCollection_ExtendedString, shapeInOneLayer: bool = False) -> bool:
        """
        Sets a link from label that containing shape <Sh>
        with layer <aLayer>. Add <aLayer> to LayerTable if nessesery.
        optional parameter <shapeInOneLayer> show could shape be
        in number of layers or only in one.
        return FALSE if no such shape <Sh>.
        """

    @overload
    def UnSetLayers(self, L: nanoocp.TDF.TDF_Label) -> None:
        """Removes a link from label <L> to all layers"""

    @overload
    def UnSetLayers(self, Sh: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Remove link between shape <Sh> and all Layers at LayerTable.
        return FALSE if no such shape <Sh> in XCAF Document.
        """

    @overload
    def UnSetOneLayer(self, L: nanoocp.TDF.TDF_Label, aLayer: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Remove link from label <L> and Layer <aLayer>.
        returns FALSE if no such layer.
        """

    @overload
    def UnSetOneLayer(self, L: nanoocp.TDF.TDF_Label, aLayerL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Remove link from label <L> and Layer <aLayerL>.
        returns FALSE if <aLayerL> is not a layer label.
        """

    @overload
    def UnSetOneLayer(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayer: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Remove link between shape <Sh> and layer <aLayer>.
        returns FALSE if no such layer <aLayer> or shape <Sh>.
        """

    @overload
    def UnSetOneLayer(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayerL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Remove link between shape <Sh> and layer <aLayerL>.
        returns FALSE if no such layer <aLayerL> or shape <Sh>.
        """

    @overload
    def IsSet(self, L: nanoocp.TDF.TDF_Label, aLayer: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns True if label <L> has a Layer associated
        with the <aLayer>.
        """

    @overload
    def IsSet(self, L: nanoocp.TDF.TDF_Label, aLayerL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label <L> has a Layer associated
        with the <aLayerL> label.
        """

    @overload
    def IsSet(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayer: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Returns True if shape <Sh> has a Layer associated
        with the <aLayer>.
        """

    @overload
    def IsSet(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayerL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if shape <Sh> has a Layer associated
        with the <aLayerL>.
        """

    @overload
    def GetLayers__NCollection_HSequence__TCollection_ExtendedString(self, L: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_ExtendedString]]:
        """
        GetLayers__NCollection_HSequence__TCollection_ExtendedString: the C++ overload GetLayers(const TDF_Label &, occ::handle<NCollection_HSequence<TCollection_ExtendedString>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Return sequence of strings <aLayerS> that associated with label <L>.
        """

    @overload
    def GetLayers__NCollection_HSequence__TCollection_ExtendedString(self, Sh: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_ExtendedString]]:
        """
        GetLayers__NCollection_HSequence__TCollection_ExtendedString: the C++ overload GetLayers(const TopoDS_Shape &, occ::handle<NCollection_HSequence<TCollection_ExtendedString>> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Return sequence of strings <aLayerS> that associated with shape <Sh>.
        """

    @overload
    def GetLayers(self, L: nanoocp.TDF.TDF_Label, aLayerLS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Return sequence of labels <aLayerSL> that associated with label <L>."""

    @overload
    def GetLayers(self, L: nanoocp.TDF.TDF_Label) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_ExtendedString]:
        """Return sequence of strings that associated with label <L>."""

    @overload
    def GetLayers(self, Sh: nanoocp.TopoDS.TopoDS_Shape, aLayerLS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Return sequence of labels <aLayerLS> that associated with shape <Sh>."""

    @overload
    def GetLayers(self, Sh: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_ExtendedString]:
        """Return sequence of strings that associated with shape <Sh>."""

    @staticmethod
    def GetShapesOfLayer(theLayerL: nanoocp.TDF.TDF_Label, theShLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Return sequanese of shape labels that assigned with layers to <ShLabels>.
        """

    def IsVisible(self, layerL: nanoocp.TDF.TDF_Label) -> bool:
        """Return TRUE if layer is visible, FALSE if invisible."""

    def SetVisibility(self, layerL: nanoocp.TDF.TDF_Label, isvisible: bool = True) -> None:
        """
        Set the visibility of layer. If layer is invisible when on it's layer
        will set UAttribute with corresponding GUID.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_LengthUnit(nanoocp.TDF.TDF_Attribute):
    """Used to define a Length Unit attribute containing a length unit info"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_LengthUnit) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns the GUID of the attribute."""

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUnitName: nanoocp.TCollection.TCollection_AsciiString, theUnitValue: float) -> XCAFDoc_LengthUnit:
        """
        Finds or creates a LengthUnit attribute
        @param theUnitName - name of the unit: mm, m, cm, km, micron, in, min, nin, ft, stat.mile
        @param theUnitValue - length scale factor to meter
        The LengthUnit attribute is returned.
        """

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUnitValue: float) -> XCAFDoc_LengthUnit:
        """
        Finds or creates a LengthUnit attribute
        @param theUnitValue - length scale factor to meter
        The LengthUnit attribute is returned.
        """

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID, theUnitName: nanoocp.TCollection.TCollection_AsciiString, theUnitValue: float) -> XCAFDoc_LengthUnit:
        """
        Finds, or creates, a LengthUnit attribute with explicit user defined GUID
        @param theUnitName - name of the unit: mm, m, cm, km, micron, in, min, nin, ft, stat.mile
        @param theUnitValue - length scale factor to meter
        The LengthUnit attribute is returned
        """

    def Set(self, theUnitName: nanoocp.TCollection.TCollection_AsciiString, theUnitValue: float) -> None:
        """
        Creates a LengthUnit attribute
        @param theUnitName - name of the unit: mm, m, cm, km, micron, in, min, nin, ft, stat.mile
        @param theUnitValue - length scale factor to meter
        """

    def GetUnitName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Length unit description (could be arbitrary text)"""

    def GetUnitValue(self) -> float:
        """Returns length unit scale factor to meter"""

    def IsEmpty(self) -> bool: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, theWith: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, theInto: nanoocp.TDF.TDF_Attribute | None, theRT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Location(nanoocp.TDF.TDF_Attribute):
    """attribute to store TopLoc_Location"""

    @overload
    def __init__(self) -> None:
        """
        class methods
        =============
        """

    @overload
    def __init__(self, theOther: XCAFDoc_Location) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, Loc: nanoocp.TopLoc.TopLoc_Location) -> XCAFDoc_Location:
        """
        Find, or create, a Location attribute and set it's value
        the Location attribute is returned.
        Location methods
        ===============
        """

    def Set(self, Loc: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    def Get(self) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns True if there is a reference on the same label"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_Material(nanoocp.TDF.TDF_Attribute):
    """attribute to store material"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_Material) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aDensity: float, aDensName: nanoocp.TCollection.TCollection_HAsciiString | None, aDensValType: nanoocp.TCollection.TCollection_HAsciiString | None) -> XCAFDoc_Material: ...

    def Set(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aDensity: float, aDensName: nanoocp.TCollection.TCollection_HAsciiString | None, aDensValType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def GetName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetDescription(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetDensity(self) -> float: ...

    def GetDensName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def GetDensValType(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, With: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, Into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_MaterialTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Provides tools to store and retrieve attributes (materials)
    of TopoDS_Shape in and from TDocStd_Document
    A Document is intended to hold different
    attributes of ONE shape and it's sub-shapes
    Provide tools for management of Materialss section of document.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_MaterialTool) -> None: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_MaterialTool:
        """Creates (if not exist) MaterialTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which colors are stored"""

    def ShapeTool(self) -> XCAFDoc_ShapeTool:
        """Returns internal XCAFDoc_ShapeTool tool"""

    def IsMaterial(self, lab: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to a material table and
        is a Material definition
        """

    def GetMaterialLabels(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of materials currently stored
        in the material table
        """

    def AddMaterial(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aDensity: float, aDensName: nanoocp.TCollection.TCollection_HAsciiString | None, aDensValType: nanoocp.TCollection.TCollection_HAsciiString | None) -> nanoocp.TDF.TDF_Label:
        """Adds a Material definition to a table and returns its label"""

    @overload
    def SetMaterial(self, L: nanoocp.TDF.TDF_Label, MatL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a link with GUID"""

    @overload
    def SetMaterial(self, L: nanoocp.TDF.TDF_Label, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aDensity: float, aDensName: nanoocp.TCollection.TCollection_HAsciiString | None, aDensValType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """
        Sets a link with GUID
        Adds a Material as necessary
        """

    @staticmethod
    def GetMaterial(MatL: nanoocp.TDF.TDF_Label) -> tuple[bool, nanoocp.TCollection.TCollection_HAsciiString, nanoocp.TCollection.TCollection_HAsciiString, float, nanoocp.TCollection.TCollection_HAsciiString, nanoocp.TCollection.TCollection_HAsciiString]:
        """
        Returns Material assigned to <MatL>
        Returns False if no such Material is assigned
        """

    @staticmethod
    def GetDensityForShape(ShapeL: nanoocp.TDF.TDF_Label) -> float:
        """
        Find referred material and return density from it
        if no material --> return 0
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_Note(nanoocp.TDF.TDF_Attribute):
    """
    A base note attribute.
    Any note contains the name of the user created the note
    and the creation timestamp.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsMine(theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """Checks if the given label represents a note."""

    @staticmethod
    def Get(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_Note:
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """

    def Set(self, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Sets the user name and the timestamp of the note.
        \\param[in]  theUserName  - the user associated with the note.
        \\param[in]  theTimeStamp - timestamp of the note.
        \\return A handle to the attribute instance.
        """

    def UserName(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the user name, who created the note."""

    def TimeStamp(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the timestamp of the note."""

    def IsOrphan(self) -> bool:
        """Checks if the note isn't linked to annotated items."""

    def GetObject(self) -> nanoocp.XCAFNoteObjects.XCAFNoteObjects_NoteObject:
        """Returns auxiliary data object"""

    def SetObject(self, theObject: nanoocp.XCAFNoteObjects.XCAFNoteObjects_NoteObject | None) -> None:
        """Updates auxiliary data"""

    def Restore(self, theAttrFrom: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, theAttrInto: nanoocp.TDF.TDF_Attribute | None, theRT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class XCAFDoc_NoteComment(XCAFDoc_Note):
    """
    A comment note attribute.
    Contains a textual comment.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty comment note."""

    @overload
    def __init__(self, theOther: XCAFDoc_NoteComment) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns default attribute GUID"""

    @staticmethod
    def Get(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_NoteComment:
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """

    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theComment: nanoocp.TCollection.TCollection_ExtendedString) -> XCAFDoc_NoteComment:
        """
        Create (if not exist) a comment note on the given label.
        \\param[in]  theLabel     - note label.
        \\param[in]  theUserName  - the name of the user, who created the note.
        \\param[in]  theTimeStamp - creation timestamp of the note.
        \\param[in]  theComment   - comment text.
        """

    def Set(self, theComment: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Sets the comment text."""

    def Comment(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the comment text."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Restore(self, theAttrFrom: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, theAttrInto: nanoocp.TDF.TDF_Attribute | None, theRT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

class XCAFDoc_NoteBalloon(XCAFDoc_NoteComment):
    """
    A comment note attribute.
    Contains a textual comment.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty comment note."""

    @overload
    def __init__(self, theOther: XCAFDoc_NoteBalloon) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns default attribute GUID"""

    @staticmethod
    def Get(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_NoteBalloon:
        """
        Finds a reference attribute on the given label and returns it, if it is found
        """

    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theComment: nanoocp.TCollection.TCollection_ExtendedString) -> XCAFDoc_NoteBalloon:
        """
        Create (if not exist) a comment note on the given label.
        \\param[in]  theLabel     - note label.
        \\param[in]  theUserName  - the name of the user, who created the note.
        \\param[in]  theTimeStamp - creation timestamp of the note.
        \\param[in]  theComment   - comment text.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

class XCAFDoc_NoteBinData(XCAFDoc_Note):
    @overload
    def __init__(self) -> None:
        """Creates an empty binary data note."""

    @overload
    def __init__(self, theOther: XCAFDoc_NoteBinData) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns default attribute GUID"""

    @staticmethod
    def Get(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_NoteBinData:
        """
        Finds a binary data attribute on the given label and returns it, if it is found
        """

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theFile: nanoocp.OSD.OSD_File) -> XCAFDoc_NoteBinData:
        """
        Create (if not exist) a binary note with data loaded from a binary file.
        \\param[in]  theLabel     - label to add the attribute.
        \\param[in]  theUserName  - the name of the user, who created the note.
        \\param[in]  theTimeStamp - creation timestamp of the note.
        \\param[in]  theTitle     - file title.
        \\param[in]  theMIMEtype  - MIME type of the file.
        \\param[in]  theFile      - input binary file.
        \\return A handle to the attribute instance.
        """

    @overload
    @staticmethod
    def Set_s(theLabel: nanoocp.TDF.TDF_Label, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theData: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> XCAFDoc_NoteBinData:
        """
        Create (if not exist) a binary note byte data array.
        \\param[in]  theLabel     - label to add the attribute.
        \\param[in]  theUserName  - the name of the user, who created the note.
        \\param[in]  theTimeStamp - creation timestamp of the note.
        \\param[in]  theTitle     - data title.
        \\param[in]  theMIMEtype  - MIME type of data.
        \\param[in]  theData      - byte data array.
        \\return A handle to the attribute instance.
        """

    @overload
    def Set(self, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theFile: nanoocp.OSD.OSD_File) -> bool:
        """
        Sets title, MIME type and data from a binary file.
        \\param[in]  theTitle     - file title.
        \\param[in]  theMIMEtype  - MIME type of the file.
        \\param[in]  theFile      - input binary file.
        """

    @overload
    def Set(self, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theData: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> None:
        """
        Sets title, MIME type and data from a byte array.
        \\param[in]  theTitle     - data title.
        \\param[in]  theMIMEtype  - MIME type of data.
        \\param[in]  theData      - byte data array.
        """

    def Title(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the note title."""

    def MIMEtype(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns data MIME type."""

    def Size(self) -> int:
        """Size of data in bytes."""

    def Data(self) -> nanoocp.NCollection.NCollection_HArray1__unsigned_char:
        """Returns byte data array."""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Restore(self, theAttrFrom: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def Paste(self, theAttrInto: nanoocp.TDF.TDF_Attribute | None, theRT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def Dump(self) -> str: ...

class XCAFDoc_NotesTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    A tool to annotate items in the hierarchical product structure.
    There are two basic entities, which operates the notes tool: notes
    and annotated items. A note is a user defined data structure derived
    from \\ref XCAFDoc_Note attribute that is attached to a separate label under
    the notes hive. An annotated item is represented by \\ref XCAFDoc_AssemblyItemRef
    attribute attached to a separate label under the annotated items
    hive. Notes are linked with annotated items by means of \\ref XCAFDoc_GraphNode
    attribute. Notes play parent roles and annotated items - child roles.

    ------------------------
    | XCAFDoc_DocumentTool |
    |          0:1         |
    ------------------------
    |1
    ------------------------
    |  XCAFDoc_NotesTool   |
    |         0:1:9        |
    ------------------------
    |1
    |   -------------------     ---------------------------
    +___|      Notes      |-----|       XCAFDoc_Note      |
    |  1|     0:1:9:1     |1   *|         0:1:9:1:*       |
    |   -------------------     ---------------------------
    |                                        !*
    |                              { XCAFDoc_GraphNode }
    |                                       *!
    |   -------------------     ---------------------------
    +___| Annotated items |-----| XCAFDoc_AssemblyItemRef |
    1|     0:1:9:2     |1   *|         0:1:9:2:*       |
    -------------------     ---------------------------

    A typical annotation procedure is illustrated by the code example below:
    \\code{.c++}
    // Get the notes tool from a XCAF document
    occ::handle<XCAFDoc_NotesTool> aNotesTool = XCAFDoc_DocumentTool::NotesTool(aDoc->Main());
    // Create new comment note
    occ::handle<XCAFDoc_Note> aNote = aNotesTool->CreateComment(aUserName, aTimestamp, aComment);
    if (!aNote.IsNull()) {
    occ::handle<XCAFDoc_AssemblyItemRef> aRef = aNotesTool->AddNote(aNote->Label(),
    anAssemblyItemId); if (aRef.IsNull()) {
    // Process error...
    }
    }
    \\endcode
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty notes tool."""

    @overload
    def __init__(self, theOther: XCAFDoc_NotesTool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Returns default attribute GUID"""

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_NotesTool:
        """Create (if not exist) a notes tool from XCAFDoc on theLabel."""

    def GetNotesLabel(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label of the notes hive."""

    def GetAnnotatedItemsLabel(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label of the annotated items hive."""

    def NbNotes(self) -> int:
        """Returns the number of labels in the notes hive."""

    def NbAnnotatedItems(self) -> int:
        """Returns the number of labels in the annotated items hive."""

    @overload
    def GetNotes(self, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns all labels from the notes hive.
        The label sequence isn't cleared beforehand.
        \\param[out]  theNoteLabels - sequence of labels.
        """

    @overload
    def GetNotes(self, theItemId: XCAFDoc_AssemblyItemId, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Gets all note labels of the assembly item.
        Notes linked to item's subshapes or attributes aren't
        taken into account. The label sequence isn't cleared beforehand.
        \\param[in]  theItemId      - assembly item ID.
        \\param[out]  theNoteLabels - sequence of labels.
        \\return number of added labels.
        """

    @overload
    def GetNotes(self, theItemLabel: nanoocp.TDF.TDF_Label, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Gets all note labels of the labeled item.
        Notes linked to item's attributes aren't
        taken into account. The label sequence isn't cleared beforehand.
        \\param[in]  theItemLabel   - item label.
        \\param[out]  theNoteLabels - sequence of labels.
        \\return number of added labels.
        """

    def GetAnnotatedItems(self, theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns all labels from the annotated items hive.
        The label sequence isn't cleared beforehand.
        \\param[out]  theNoteLabels - sequence of labels.
        """

    @overload
    def IsAnnotatedItem(self, theItemId: XCAFDoc_AssemblyItemId) -> bool:
        """
        Checks if the given assembly item is annotated.
        \\param[in]  theItemId - assembly item ID.
        \\return true if the item is annotated, otherwise - false.
        """

    @overload
    def IsAnnotatedItem(self, theItemLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Checks if the given labeled item is annotated.
        \\param[in]  theItemLabel - item label.
        \\return true if the item is annotated, otherwise - false.
        """

    @overload
    def FindAnnotatedItem(self, theItemId: XCAFDoc_AssemblyItemId) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given assembly item ID in the annotated items hive.
        \\param[in]  theItemId - assembly item ID.
        \\return annotated item label if it is found, otherwise - null label.
        """

    @overload
    def FindAnnotatedItem(self, theItemLabel: nanoocp.TDF.TDF_Label) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given labeled item in the annotated items hive.
        \\param[in]  theItemLabel - item label.
        \\return annotated item label if it is found, otherwise - null label.
        """

    @overload
    def FindAnnotatedItemAttr(self, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given assembly item's attribute in the annotated items hive.
        \\param[in]  theItemId - assembly item ID.
        \\param[in]  theGUID   - assembly item's attribute GUID.
        \\return annotated item label if it is found, otherwise - null label.
        """

    @overload
    def FindAnnotatedItemAttr(self, theItemLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given labeled item's attribute in the annotated items hive.
        \\param[in]  theItemLabel - item label.
        \\param[in]  theGUID      - item's attribute GUID.
        \\return annotated item label if it is found, otherwise - null label.
        """

    @overload
    def FindAnnotatedItemSubshape(self, theItemId: XCAFDoc_AssemblyItemId, theSubshapeIndex: int) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given assembly item's subshape in the annotated items hive.
        \\param[in]  theItemId        - assembly item ID.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\return annotated item label if it is found, otherwise - null label.
        """

    @overload
    def FindAnnotatedItemSubshape(self, theItemLabel: nanoocp.TDF.TDF_Label, theSubshapeIndex: int) -> nanoocp.TDF.TDF_Label:
        """
        Finds a label of the given labeled item's subshape in the annotated items hive.
        \\param[in]  theItemLabel     - item label.
        \\param[in]  theSubshapeIndex - labeled item's subshape index.
        \\return annotated item label if it is found, otherwise - null label.
        """

    def CreateComment(self, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theComment: nanoocp.TCollection.TCollection_ExtendedString) -> XCAFDoc_Note:
        """
        Create a new comment note.
        Creates a new label under the notes hive and attaches \\ref XCAFDoc_NoteComment
        attribute (derived ftom \\ref XCAFDoc_Note).
        \\param[in]  theUserName  - the user associated with the note.
        \\param[in]  theTimeStamp - timestamp of the note.
        \\param[in]  theComment   - textual comment.
        \\return a handle to the base note attribute.
        """

    def CreateBalloon(self, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theComment: nanoocp.TCollection.TCollection_ExtendedString) -> XCAFDoc_Note:
        """
        Create a new 'balloon' note.
        Creates a new label under the notes hive and attaches \\ref XCAFDoc_NoteBalloon
        attribute (derived ftom \\ref XCAFDoc_Note).
        \\param[in]  theUserName  - the user associated with the note.
        \\param[in]  theTimeStamp - timestamp of the note.
        \\param[in]  theComment   - textual comment.
        \\return a handle to the base note attribute.
        """

    @overload
    def CreateBinData(self, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theFile: nanoocp.OSD.OSD_File) -> XCAFDoc_Note:
        """
        Create a new note with data loaded from a binary file.
        Creates a new label under the notes hive and attaches \\ref XCAFDoc_NoteComment
        attribute (derived ftom \\ref XCAFDoc_Note).
        \\param[in]  theUserName  - the user associated with the note.
        \\param[in]  theTimeStamp - timestamp of the note.
        \\param[in]  theTitle     - file title.
        \\param[in]  theMIMEtype  - MIME type of the file.
        \\param[in]  theFile      - input binary file.
        \\return a handle to the base note attribute.
        """

    @overload
    def CreateBinData(self, theUserName: nanoocp.TCollection.TCollection_ExtendedString, theTimeStamp: nanoocp.TCollection.TCollection_ExtendedString, theTitle: nanoocp.TCollection.TCollection_ExtendedString, theMIMEtype: nanoocp.TCollection.TCollection_AsciiString, theData: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> XCAFDoc_Note:
        """
        Create a new note with data loaded from a byte data array.
        Creates a new label under the notes hive and attaches \\ref XCAFDoc_NoteComment
        attribute (derived ftom \\ref XCAFDoc_Note).
        \\param[in]  theUserName  - the user associated with the note.
        \\param[in]  theTimeStamp - timestamp of the note.
        \\param[in]  theTitle     - data title.
        \\param[in]  theMIMEtype  - MIME type of the file.
        \\param[in]  theData      - byte data array.
        \\return a handle to the base note attribute.
        """

    @overload
    def GetAttrNotes(self, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Gets all note labels of the assembly item's attribute.
        Notes linked to the item itself or to item's subshapes
        aren't taken into account. The label sequence isn't cleared beforehand.
        \\param[in]  theItemId      - assembly item ID.
        \\param[in]  theGUID        - assembly item's attribute GUID.
        \\param[out]  theNoteLabels - sequence of labels.
        \\return number of added labels.
        """

    @overload
    def GetAttrNotes(self, theItemLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Gets all note labels of the labeled item's attribute.
        Notes linked to the item itself or to item's subshapes
        aren't taken into account. The label sequence isn't cleared beforehand.
        \\param[in]  theItemLabel   - item label.
        \\param[in]  theGUID        - item's attribute GUID.
        \\param[out]  theNoteLabels - sequence of labels.
        \\return number of added labels.
        """

    def GetSubshapeNotes(self, theItemId: XCAFDoc_AssemblyItemId, theSubshapeIndex: int, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Gets all note labels of the annotated item.
        Notes linked to the item itself or to item's attributes
        taken into account. The label sequence isn't cleared beforehand.
        \\param[in]  theItemId        - assembly item ID.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\param[out]  theNoteLabels   - sequence of labels.
        \\return number of added labels.
        """

    @overload
    def AddNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the assembly item.
        \\param[in]  theNoteLabel - note label.
        \\param[in]  theItemId    - assembly item ID.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def AddNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the labeled item.
        \\param[in]  theNoteLabel - note label.
        \\param[in]  theItemLabel - item label.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def AddNoteToAttr(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the assembly item's attribute.
        \\param[in]  theNoteLabel - note label.
        \\param[in]  theItemId    - assembly item ID.
        \\param[in]  theGUID      - assembly item's attribute GUID.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def AddNoteToAttr(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the labeled item's attribute.
        \\param[in]  theNoteLabel - note label.
        \\param[in]  theItemLabel - item label.
        \\param[in]  theGUID      - assembly item's attribute GUID.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def AddNoteToSubshape(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theSubshapeIndex: int) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the assembly item's subshape.
        \\param[in]  theNoteLabel     - note label.
        \\param[in]  theItemId        - assembly item ID.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def AddNoteToSubshape(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label, theSubshapeIndex: int) -> XCAFDoc_AssemblyItemRef:
        """
        Adds the given note to the labeled item's subshape.
        \\param[in]  theNoteLabel     - note label.
        \\param[in]  theItemLabel     - item label.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\return a handle to the assembly reference attribute.
        """

    @overload
    def RemoveNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theDelIfOrphan: bool = False) -> bool:
        """
        Removes the given note from the assembly item.
        \\param[in]  theNoteLabel   - note label.
        \\param[in]  theItemId      - assembly item ID.
        \\param[in]  theDelIfOrphan - deletes the note from the notes hive
        if there are no more assembly items
        linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label, theDelIfOrphan: bool = False) -> bool:
        """
        Removes the given note from the labeled item.
        \\param[in]  theNoteLabel   - note label.
        \\param[in]  theItemLabel   - item label.
        \\param[in]  theDelIfOrphan - deletes the note from the notes hive
        if there are no more labeled items
        linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveSubshapeNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theSubshapeIndex: int, theDelIfOrphan: bool = False) -> bool:
        """
        Removes the given note from the assembly item's subshape.
        \\param[in]  theNoteLabel     - note label.
        \\param[in]  theItemId        - assembly item ID.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\param[in]  theDelIfOrphan   - deletes the note from the notes hive
        if there are no more assembly item's
        subshape linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveSubshapeNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label, theSubshapeIndex: int, theDelIfOrphan: bool = False) -> bool:
        """
        Removes the given note from the labeled item's subshape.
        \\param[in]  theNoteLabel     - note label.
        \\param[in]  theItemLabel     - item label.
        \\param[in]  theSubshapeIndex - labeled item's subshape index.
        \\param[in]  theDelIfOrphan   - deletes the note from the notes hive
        if there are no more assembly item's
        subshape linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveAttrNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID, theDelIfOrphan: bool = False) -> bool:
        """
        Removes a note from the assembly item's attribute.
        \\param[in]  theNoteLabel   - note label.
        \\param[in]  theItemId      - assembly item ID.
        \\param[in]  theGUID        - assembly item's attribute GUID.
        \\param[in]  theDelIfOrphan - deletes the note from the notes hive
        if there are no more assembly item's
        attribute linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveAttrNote(self, theNoteLabel: nanoocp.TDF.TDF_Label, theItemLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID, theDelIfOrphan: bool = False) -> bool:
        """
        Removes a note from the labeled item's attribute.
        \\param[in]  theNoteLabel   - note label.
        \\param[in]  theItemLabel   - item label.
        \\param[in]  theGUID        - labeled item's attribute GUID.
        \\param[in]  theDelIfOrphan - deletes the note from the notes hive
        if there are no more assembly item's
        attribute linked with the note.
        \\return true if the note is removed, otherwise - false.
        """

    @overload
    def RemoveAllNotes(self, theItemId: XCAFDoc_AssemblyItemId, theDelIfOrphan: bool = False) -> bool:
        """
        Removes all notes from the assembly item.
        \\param[in]  theItemId      - assembly item ID.
        \\param[in]  theDelIfOrphan - deletes removed notes from the notes
        hive if there are no more annotated items
        linked with the notes.
        \\return true if the notes are removed, otherwise - false.
        """

    @overload
    def RemoveAllNotes(self, theItemLabel: nanoocp.TDF.TDF_Label, theDelIfOrphan: bool = False) -> bool:
        """
        Removes all notes from the labeled item.
        \\param[in]  theItemLabel   - item label.
        \\param[in]  theDelIfOrphan - deletes removed notes from the notes
        hive if there are no more annotated items
        linked with the notes.
        \\return true if the notes are removed, otherwise - false.
        """

    def RemoveAllSubshapeNotes(self, theItemId: XCAFDoc_AssemblyItemId, theSubshapeIndex: int, theDelIfOrphan: bool = False) -> bool:
        """
        Removes all notes from the assembly item's subshape.
        \\param[in]  theItemId        - assembly item ID.
        \\param[in]  theSubshapeIndex - assembly item's subshape index.
        \\param[in]  theDelIfOrphan   - deletes removed notes from the notes
        hive if there are no more annotated items
        linked with the notes.
        \\return true if the notes are removed, otherwise - false.
        """

    @overload
    def RemoveAllAttrNotes(self, theItemId: XCAFDoc_AssemblyItemId, theGUID: nanoocp.Standard.Standard_GUID, theDelIfOrphan: bool = False) -> bool:
        """
        Removes all notes from the assembly item's attribute.
        \\param[in]  theItemId      - assembly item ID.
        \\param[in]  theGUID        - assembly item's attribute GUID.
        \\param[in]  theDelIfOrphan - deletes removed notes from the notes
        hive if there are no more annotated items
        linked with the notes.
        \\return true if the notes are removed, otherwise - false.
        """

    @overload
    def RemoveAllAttrNotes(self, theItemLabel: nanoocp.TDF.TDF_Label, theGUID: nanoocp.Standard.Standard_GUID, theDelIfOrphan: bool = False) -> bool:
        """
        Removes all notes from the labeled item's attribute.
        \\param[in]  theItemLabel   - item label.
        \\param[in]  theGUID        - labeled item's attribute GUID.
        \\param[in]  theDelIfOrphan - deletes removed notes from the notes
        hive if there are no more annotated items
        linked with the notes.
        \\return true if the notes are removed, otherwise - false.
        """

    def DeleteNote(self, theNoteLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Deletes the given note.
        Removes all links with items annotated by the note.
        \\param[in]  theNoteLabel - note label.
        \\return true if the note is deleted, otherwise - false.
        """

    def DeleteNotes(self, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> int:
        """
        Deletes the given notes.
        Removes all links with items annotated by the notes.
        \\param[in]  theNoteLabels - note label sequence.
        \\return number of deleted notes.
        """

    def DeleteAllNotes(self) -> int:
        """
        Deletes all notes.
        Clears all annotations.
        \\return number of deleted notes.
        """

    def NbOrphanNotes(self) -> int:
        """Returns number of notes that aren't linked to annotated items."""

    def GetOrphanNotes(self, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns note labels that aren't linked to annotated items.
        The label sequence isn't cleared beforehand.
        \\param[out]  theNoteLabels - sequence of labels.
        """

    def DeleteOrphanNotes(self) -> int:
        """
        Deletes all notes that aren't linked to annotated items.
        \\return number of deleted notes.
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """@}"""

    def Dump(self) -> str: ...

class XCAFDoc_ShapeMapTool(nanoocp.TDF.TDF_Attribute):
    """attribute containing map of sub shapes"""

    @overload
    def __init__(self) -> None:
        """Creates an empty tool"""

    @overload
    def __init__(self, theOther: XCAFDoc_ShapeMapTool) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_ShapeMapTool:
        """Create (if not exist) ShapeTool from XCAFDoc on <L>."""

    def IsSubShape(self, sub: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks whether shape <sub> is subshape of shape stored on
        label shapeL
        """

    def SetShape(self, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets representation (TopoDS_Shape) for top-level shape"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Restore(self, with_: nanoocp.TDF.TDF_Attribute | None) -> None: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

    def Paste(self, into: nanoocp.TDF.TDF_Attribute | None, RT: nanoocp.TDF.TDF_RelocationTable | None) -> None: ...

    def GetMap(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher]: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDoc_ShapeTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    A tool to store shapes in an XDE
    document in the form of assembly structure, and to maintain this structure.
    Attribute containing Shapes section of DECAF document.
    Provide tools for management of Shapes section.
    The API provided by this class allows to work with this
    structure regardless of its low-level implementation.
    All the shapes are stored on child labels of a main label which is
    XCAFDoc_DocumentTool::LabelShapes(). The label for assembly also has
    sub-labels, each of which represents the instance of
    another shape in that assembly (component). Such sub-label
    stores reference to the label of the original shape in the form
    of TDataStd_TreeNode with GUID XCAFDoc::ShapeRefGUID(), and its
    location encapsulated into the NamedShape.
    For correct work with an XDE document, it is necessary to use
    methods for analysis and methods for working with shapes.
    For example:
    if ( STool->IsAssembly(aLabel) )
    { bool subchilds = false; (default)
    int nbc = STool->NbComponents
    (aLabel[,subchilds]);
    }
    If subchilds is True, commands also consider sub-levels. By
    default, only level one is checked.
    In this example, number of children from the first level of
    assembly will be returned. Methods for creation and initialization:
    Constructor:
    XCAFDoc_ShapeTool::XCAFDoc_ShapeTool()
    Getting a guid:
    Standard_GUID GetID ();
    Creation (if does not exist) of ShapeTool on label L:
    occ::handle<XCAFDoc_ShapeTool> XCAFDoc_ShapeTool::Set(const TDF_Label& L)
    Analyze whether shape is a simple shape or an instance or a
    component of an assembly or it is an assembly ( methods of analysis).
    For example:
    STool->IsShape(aLabel) ;
    Analyze that the label represents a shape (simple
    shape, assembly or reference) or
    STool->IsTopLevel(aLabel);
    Analyze that the label is a label of a top-level shape.
    Work with simple shapes, assemblies and instances (
    methods for work with shapes).
    For example:
    Add shape:
    bool makeAssembly;
    // True to interpret a Compound as an Assembly, False to take it
    as a whole
    aLabel = STool->AddShape(aShape, makeAssembly);
    Get shape:
    TDF_Label aLabel...
    // A label must be present if
    (aLabel.IsNull()) { ... no such label : abandon .. }
    TopoDS_Shape aShape;
    aShape = STool->GetShape(aLabel);
    if (aShape.IsNull())
    { ... this label is not for a Shape ... }
    To get a label from shape.
    bool findInstance = false;
    (this is default value)
    aLabel = STool->FindShape(aShape [,findInstance]);
    if (aLabel.IsNull())
    { ... no label found for this shape ... }
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty tool
        Creates a tool to work with a document <Doc>
        Attaches to label XCAFDoc::LabelShapes()
        """

    @overload
    def __init__(self, theOther: XCAFDoc_ShapeTool) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_ShapeTool:
        """Create (if not exist) ShapeTool from XCAFDoc on <L>."""

    def IsTopLevel(self, L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label is a label of top-level shape,
        as opposed to component of assembly or subshape
        """

    @staticmethod
    def IsFree(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label is not used by any assembly, i.e.
        contains sublabels which are assembly components
        This is relevant only if IsShape() is True
        (There is no Father TreeNode on this <L>)
        """

    @staticmethod
    def IsShape(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label represents a shape (simple shape,
        assembly or reference)
        """

    @staticmethod
    def IsSimpleShape(L: nanoocp.TDF.TDF_Label) -> bool:
        """Returns True if the label is a label of simple shape"""

    @staticmethod
    def IsReference(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Return true if <L> is a located instance of other shape
        i.e. reference
        """

    @staticmethod
    def IsAssembly(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label is a label of assembly, i.e.
        contains sublabels which are assembly components
        This is relevant only if IsShape() is True
        """

    @staticmethod
    def IsComponent(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Return true if <L> is reference serving as component
        of assembly
        """

    @staticmethod
    def IsCompound(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label is a label of compound, i.e.
        contains some sublabels
        This is relevant only if IsShape() is True
        """

    @staticmethod
    def IsSubShape_s(L: nanoocp.TDF.TDF_Label) -> bool:
        """Return true if <L> is subshape of the top-level shape"""

    def IsSubShape(self, shapeL: nanoocp.TDF.TDF_Label, sub: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Checks whether shape <sub> is subshape of shape stored on
        label shapeL
        """

    def SearchUsingMap(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.TDF.TDF_Label, findWithoutLoc: bool, findSubshape: bool) -> bool: ...

    def Search(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.TDF.TDF_Label, findInstance: bool = True, findComponent: bool = True, findSubshape: bool = True) -> bool:
        """
        General tool to find a (sub) shape in the document
        * If findInstance is True, and S has a non-null location,
        first tries to find the shape among the top-level shapes
        with this location
        * If not found, and findComponent is True, tries to find the shape
        among the components of assemblies
        * If not found, tries to find the shape without location
        among top-level shapes
        * If not found and findSubshape is True, tries to find a
        shape as a subshape of top-level simple shapes
        Returns False if nothing is found
        """

    @overload
    def FindShape(self, S: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.TDF.TDF_Label, findInstance: bool = False) -> bool:
        """
        Returns the label corresponding to shape S
        (searches among top-level shapes, not including subcomponents
        of assemblies and subshapes)
        If findInstance is False (default), search for the
        input shape without location
        If findInstance is True, searches for the
        input shape as is.
        Return True if <S> is found.
        """

    @overload
    def FindShape(self, S: nanoocp.TopoDS.TopoDS_Shape, findInstance: bool = False) -> nanoocp.TDF.TDF_Label:
        """
        Does the same as previous method
        Returns Null label if not found
        """

    @overload
    @staticmethod
    def GetShape(L: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        To get TopoDS_Shape from shape's label
        For component, returns new shape with correct location
        Returns False if label does not contain shape
        """

    @overload
    @staticmethod
    def GetShape(L: nanoocp.TDF.TDF_Label) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        To get TopoDS_Shape from shape's label
        For component, returns new shape with correct location
        Returns Null shape if label does not contain shape
        """

    @staticmethod
    def GetOneShape_s(theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Gets shape from a sequence of shape's labels
        @param[in] theLabels a sequence of labels to get shapes from
        @return original shape in case of one label and a compound of shapes in case of more
        """

    def GetOneShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Gets shape from a sequence of all top-level shapes which are free
        @return original shape in case of one label and a compound of shapes in case of more
        """

    def NewShape(self) -> nanoocp.TDF.TDF_Label:
        """
        Creates new (empty) top-level shape.
        Initially it holds empty TopoDS_Compound
        """

    def SetShape(self, L: nanoocp.TDF.TDF_Label, S: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets representation (TopoDS_Shape) for top-level shape."""

    def AddShape(self, S: nanoocp.TopoDS.TopoDS_Shape, makeAssembly: bool = True, makePrepare: bool = True) -> nanoocp.TDF.TDF_Label:
        """
        Adds a new top-level (creates and returns a new label)
        If makeAssembly is True, treats TopAbs_COMPOUND shapes
        as assemblies (creates assembly structure).
        NOTE: <makePrepare> replace components without location
        in assembly by located components to avoid some problems.
        If AutoNaming() is True then automatically attaches names.
        """

    def RemoveShape(self, L: nanoocp.TDF.TDF_Label, removeCompletely: bool = True) -> bool:
        """
        Removes shape (whole label and all its sublabels)
        If removeCompletely is true, removes complete shape
        If removeCompletely is false, removes instance(location) only
        Returns False (and does nothing) if shape is not free
        or is not top-level shape
        """

    def Init(self) -> None:
        """set hasComponents into false"""

    @staticmethod
    def SetAutoNaming(V: bool) -> None:
        """
        Sets auto-naming mode to <V>. If True then for added
        shapes, links, assemblies and SHUO's, the TDataStd_Name attribute
        is automatically added. For shapes it contains a shape type
        (e.g. "SOLID", "SHELL", etc); for links it has a form
        "=>[0:1:1:2]" (where a tag is a label containing a shape
        without a location); for assemblies it is "ASSEMBLY", and
        "SHUO" for SHUO's.
        This setting is global; it cannot be made a member function
        as it is used by static methods as well.
        By default, auto-naming is enabled.
        See also AutoNaming().
        """

    @staticmethod
    def AutoNaming() -> bool:
        """
        Returns current auto-naming mode. See SetAutoNaming() for
        description.
        """

    def ComputeShapes(self, L: nanoocp.TDF.TDF_Label) -> None:
        """recursive"""

    def ComputeSimpleShapes(self) -> None:
        """Compute a sequence of simple shapes"""

    def GetShapes(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """Returns a sequence of all top-level shapes"""

    def GetFreeShapes(self, FreeLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of all top-level shapes
        which are free (i.e. not referred by any other)
        """

    @staticmethod
    def GetUsers(L: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], getsubchilds: bool = False) -> int:
        """
        Returns list of labels which refer shape L as component
        Returns number of users (0 if shape is free)
        """

    @staticmethod
    def GetLocation(L: nanoocp.TDF.TDF_Label) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns location of instance"""

    @staticmethod
    def GetReferredShape(L: nanoocp.TDF.TDF_Label, Label: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns label which corresponds to a shape referred by L
        Returns False if label is not reference
        """

    @staticmethod
    def NbComponents(L: nanoocp.TDF.TDF_Label, getsubchilds: bool = False) -> int:
        """Returns number of Assembles components"""

    @staticmethod
    def GetComponents(L: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], getsubchilds: bool = False) -> bool:
        """
        Returns list of components of assembly
        Returns False if label is not assembly
        """

    @overload
    def AddComponent(self, assembly: nanoocp.TDF.TDF_Label, comp: nanoocp.TDF.TDF_Label, Loc: nanoocp.TopLoc.TopLoc_Location) -> nanoocp.TDF.TDF_Label:
        """
        Adds a component given by its label and location to the assembly
        Note: assembly must be IsAssembly() or IsSimpleShape()
        """

    @overload
    def AddComponent(self, assembly: nanoocp.TDF.TDF_Label, comp: nanoocp.TopoDS.TopoDS_Shape, expand: bool = False) -> nanoocp.TDF.TDF_Label:
        """
        Adds a shape (located) as a component to the assembly
        If necessary, creates an additional top-level shape for
        component and return the Label of component.
        If expand is True and component is Compound, it will
        be created as assembly also
        Note: assembly must be IsAssembly() or IsSimpleShape()
        """

    def RemoveComponent(self, comp: nanoocp.TDF.TDF_Label) -> None:
        """Removes a component from its assembly"""

    def UpdateAssemblies(self) -> None:
        """Top-down update for all assembly compounds stored in the document."""

    def FindSubShape(self, shapeL: nanoocp.TDF.TDF_Label, sub: nanoocp.TopoDS.TopoDS_Shape, L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Finds a label for subshape <sub> of shape stored on
        label shapeL
        Returns Null label if it is not found
        """

    @overload
    def AddSubShape(self, shapeL: nanoocp.TDF.TDF_Label, sub: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TDF.TDF_Label:
        """
        Adds a label for subshape <sub> of shape stored on
        label shapeL
        Returns Null label if it is not subshape
        """

    @overload
    def AddSubShape(self, shapeL: nanoocp.TDF.TDF_Label, sub: nanoocp.TopoDS.TopoDS_Shape, addedSubShapeL: nanoocp.TDF.TDF_Label) -> bool:
        """
        Adds (of finds already existed) a label for subshape <sub> of shape stored on
        label shapeL. Label addedSubShapeL returns added (found) label or empty in case of wrong
        subshape. Returns True, if new shape was added, False in case of already existed
        subshape/wrong subshape
        """

    def FindMainShapeUsingMap(self, sub: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TDF.TDF_Label: ...

    def FindMainShape(self, sub: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TDF.TDF_Label:
        """
        Performs a search among top-level shapes to find
        the shape containing <sub> as subshape
        Checks only simple shapes, and returns the first found
        label (which should be the only one for valid model)
        """

    @staticmethod
    def GetSubShapes(L: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns list of labels identifying subshapes of the given shape
        Returns False if no subshapes are placed on that label
        """

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which shapes are stored"""

    @overload
    def Dump(self, deep: bool) -> str: ...

    @overload
    def Dump(self) -> str: ...

    @staticmethod
    def DumpShape(L: nanoocp.TDF.TDF_Label, level: int = 0, deep: bool = False) -> str:
        """
        Print to std::ostream <theDumpLog> type of shape found on <L> label
        and the entry of <L>, with <level> tabs before.
        If <deep>, print also TShape and Location addresses
        """

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def IsExternRef(L: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if the label is a label of external references, i.e.
        there are some reference on the no-step files, which are
        described in document only their names
        """

    @overload
    def SetExternRefs(self, SHAS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def SetExternRefs(self, L: nanoocp.TDF.TDF_Label, SHAS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]) -> None:
        """Sets the names of references on the no-step files"""

    @staticmethod
    def GetExternRefs(L: nanoocp.TDF.TDF_Label, SHAS: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HAsciiString]) -> None:
        """Gets the names of references on the no-step files"""

    def SetSHUO(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> tuple[bool, XCAFDoc_GraphNode]:
        """
        Sets the SHUO structure between upper_usage and next_usage
        create multy-level (if number of labels > 2) SHUO from first to last
        Initialise out <MainSHUOAttr> by main upper_usage SHUO attribute.
        Returns FALSE if some of labels in not component label
        """

    @staticmethod
    def GetSHUO(SHUOLabel: nanoocp.TDF.TDF_Label) -> tuple[bool, XCAFDoc_GraphNode]:
        """
        Returns founded SHUO GraphNode attribute <aSHUOAttr>
        Returns false in other case
        """

    @staticmethod
    def GetAllComponentSHUO(CompLabel: nanoocp.TDF.TDF_Label, SHUOAttrs: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Attribute]) -> bool:
        """
        Returns founded SHUO GraphNodes of indicated component
        Returns false in other case
        """

    @staticmethod
    def GetSHUOUpperUsage(NextUsageL: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns the sequence of labels of SHUO attributes,
        which is upper_usage for this next_usage SHUO attribute
        (that indicated by label)
        NOTE: returns upper_usages only on one level (not recurse)
        NOTE: do not clear the sequence before filling
        """

    @staticmethod
    def GetSHUONextUsage(UpperUsageL: nanoocp.TDF.TDF_Label, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns the sequence of labels of SHUO attributes,
        which is next_usage for this upper_usage SHUO attribute
        (that indicated by label)
        NOTE: returns next_usages only on one level (not recurse)
        NOTE: do not clear the sequence before filling
        """

    def RemoveSHUO(self, SHUOLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Remove SHUO from component sublabel,
        remove all dependencies on other SHUO.
        Returns FALSE if cannot remove SHUO dependencies.
        NOTE: remove any styles that associated with this SHUO.
        """

    def FindComponent(self, theShape: nanoocp.TopoDS.TopoDS_Shape, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Search the path of labels in the document,
        that corresponds the component from any assembly
        Try to search the sequence of labels with location that
        produce this shape as component of any assembly
        NOTE: Clear sequence of labels before filling
        """

    def GetSHUOInstance(self, theSHUO: XCAFDoc_GraphNode | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Search for the component shape that styled by shuo
        Returns null shape if no any shape is found.
        """

    def SetInstanceSHUO(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> XCAFDoc_GraphNode:
        """
        Search for the component shape by labelks path
        and set SHUO structure for founded label structure
        Returns null attribute if no component in any assembly found.
        """

    def GetAllSHUOInstances(self, theSHUO: XCAFDoc_GraphNode | None, theSHUOShapeSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TopoDS.TopoDS_Shape]) -> bool:
        """
        Searching for component shapes that styled by shuo
        Returns empty sequence of shape if no any shape is found.
        """

    @staticmethod
    def FindSHUO(Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> tuple[bool, XCAFDoc_GraphNode]:
        """
        Searches the SHUO by labels of components
        from upper_usage component to next_usage
        Returns null attribute if no SHUO found
        """

    def SetLocation(self, theShapeLabel: nanoocp.TDF.TDF_Label, theLoc: nanoocp.TopLoc.TopLoc_Location, theRefLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Sets location to the shape label
        If label is reference -> changes location attribute
        If label is free shape -> creates reference with location to it
        @param[in] theShapeLabel the shape label to change location
        @param[in] theLoc location to set
        @param[out] theRefLabel the reference label with new location
        @return TRUE if new location was set
        """

    def Expand(self, Shape: nanoocp.TDF.TDF_Label) -> bool:
        """Convert Shape (compound/compsolid/shell/wire) to assembly"""

    @overload
    def GetNamedProperties(self, theLabel: nanoocp.TDF.TDF_Label, theToCreate: bool = False) -> nanoocp.TDataStd.TDataStd_NamedData:
        """
        Method to get NamedData attribute assigned to the given shape label.
        @param[in] theLabel     the shape Label
        @param[in] theToCreate  create and assign attribute if it doesn't exist
        @return Handle to the NamedData attribute or Null if there is none
        """

    @overload
    def GetNamedProperties(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theToCreate: bool = False) -> nanoocp.TDataStd.TDataStd_NamedData:
        """
        Method to get NamedData attribute assigned to a label of the given shape.
        @param[in] theShape     input shape
        @param[in] theToCreate  create and assign attribute if it doesn't exist
        @return Handle to the NamedData attribute or Null if there is none
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_View(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """Attribute to store view"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_View) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def Set(theLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_View: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def SetObject(self, theViewObject: nanoocp.XCAFView.XCAFView_Object | None) -> None:
        """
        Updates parent's label and its sub-labels with data taken from theViewObject.
        Old data associated with the label will be lost.
        """

    def GetObject(self) -> nanoocp.XCAFView.XCAFView_Object:
        """
        Returns view object data taken from the paren's label and its sub-labels.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_ViewTool(nanoocp.TDataStd.TDataStd_GenericEmpty):
    """
    Provides tools to store and retrieve Views
    in and from TDocStd_Document
    Each View contains parts XCAFDoc_View attribute
    with all information about camera and view window.
    Also each view contain information of displayed shapes and GDTs
    as sets of shape and GDT labels.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDoc_ViewTool) -> None: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_ViewTool:
        """Creates (if not exist) ViewTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """Returns the label under which Views are stored"""

    def IsView(self, theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns True if label belongs to a View table and
        is a View definition
        """

    def GetViewLabels(self, theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of View labels currently stored
        in the View table
        """

    @overload
    def SetView(self, theShapes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theGDTs: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theClippingPlanes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theNotes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theAnnotations: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theViewL: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def SetView(self, theShapes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theGDTs: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theClippingPlanes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theViewL: nanoocp.TDF.TDF_Label) -> None: ...

    @overload
    def SetView(self, theShapes: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theGDTs: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Sets a link with GUID"""

    def SetClippingPlanes(self, theClippingPlaneLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label], theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Set Clipping planes to given View"""

    def RemoveView(self, theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Remove View"""

    def GetViewLabelsForShape(self, theShapeL: nanoocp.TDF.TDF_Label, theViews: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all View labels defined for label ShapeL"""

    def GetViewLabelsForGDT(self, theGDTL: nanoocp.TDF.TDF_Label, theViews: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all View labels defined for label GDTL"""

    def GetViewLabelsForClippingPlane(self, theClippingPlaneL: nanoocp.TDF.TDF_Label, theViews: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all View labels defined for label ClippingPlaneL"""

    def GetViewLabelsForNote(self, theNoteL: nanoocp.TDF.TDF_Label, theViews: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all View labels defined for label NoteL"""

    def GetViewLabelsForAnnotation(self, theAnnotationL: nanoocp.TDF.TDF_Label, theViews: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """Returns all View labels defined for label AnnotationL"""

    def AddView(self) -> nanoocp.TDF.TDF_Label:
        """Adds a view definition to a View table and returns its label"""

    def GetRefShapeLabel(self, theViewL: nanoocp.TDF.TDF_Label, theShapeLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns shape labels defined for label theViewL
        Returns False if the theViewL is not in View table
        """

    def GetRefGDTLabel(self, theViewL: nanoocp.TDF.TDF_Label, theGDTLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns GDT labels defined for label theViewL
        Returns False if the theViewL is not in View table
        """

    def GetRefClippingPlaneLabel(self, theViewL: nanoocp.TDF.TDF_Label, theClippingPlaneLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns ClippingPlane labels defined for label theViewL
        Returns False if the theViewL is not in View table
        """

    def GetRefNoteLabel(self, theViewL: nanoocp.TDF.TDF_Label, theNoteLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns Notes labels defined for label theViewL
        Returns False if the theViewL is not in View table
        """

    def GetRefAnnotationLabel(self, theViewL: nanoocp.TDF.TDF_Label, theAnnotationLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> bool:
        """
        Returns Annotation labels defined for label theViewL
        Returns False if the theViewL is not in View table
        """

    def IsLocked(self, theViewL: nanoocp.TDF.TDF_Label) -> bool:
        """Returns true if the given View is marked as locked"""

    def Lock(self, theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Mark the given View as locked"""

    def Unlock(self, theViewL: nanoocp.TDF.TDF_Label) -> None:
        """Unlock the given View"""

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

class XCAFDoc_VisMaterialCommon:
    """Common (obsolete) material definition."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: XCAFDoc_VisMaterialCommon) -> None: ...

    def IsEqual(self, theOther: XCAFDoc_VisMaterialCommon) -> bool:
        """Compare two materials."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def DiffuseTexture(self) -> nanoocp.Image.Image_Texture:
        """image defining diffuse color"""

    @DiffuseTexture.setter
    def DiffuseTexture(self, arg: nanoocp.Image.Image_Texture, /) -> None: ...

    @property
    def AmbientColor(self) -> nanoocp.Quantity.Quantity_Color:
        """ambient  color"""

    @AmbientColor.setter
    def AmbientColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def DiffuseColor(self) -> nanoocp.Quantity.Quantity_Color:
        """diffuse  color"""

    @DiffuseColor.setter
    def DiffuseColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def SpecularColor(self) -> nanoocp.Quantity.Quantity_Color:
        """specular color"""

    @SpecularColor.setter
    def SpecularColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def EmissiveColor(self) -> nanoocp.Quantity.Quantity_Color:
        """emission color"""

    @EmissiveColor.setter
    def EmissiveColor(self, arg: nanoocp.Quantity.Quantity_Color, /) -> None: ...

    @property
    def Shininess(self) -> float:
        """shininess value"""

    @Shininess.setter
    def Shininess(self, arg: float, /) -> None: ...

    @property
    def Transparency(self) -> float:
        """transparency value within [0, 1] range with 0 meaning opaque"""

    @Transparency.setter
    def Transparency(self, arg: float, /) -> None: ...

    @property
    def IsDefined(self) -> bool:
        """defined flag; TRUE by default"""

    @IsDefined.setter
    def IsDefined(self, arg: bool, /) -> None: ...

class XCAFDoc_VisMaterialPBR:
    """Metallic-roughness PBR material definition."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: XCAFDoc_VisMaterialPBR) -> None: ...

    def IsEqual(self, theOther: XCAFDoc_VisMaterialPBR) -> bool:
        """Compare two materials."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

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
        metalness  (or scale factor to the texture) within range [0.0, 1.0]; 1.0 by default
        """

    @Metallic.setter
    def Metallic(self, arg: float, /) -> None: ...

    @property
    def Roughness(self) -> float:
        """
        roughness  (or scale factor to the texture) within range [0.0, 1.0]; 1.0 by default
        """

    @Roughness.setter
    def Roughness(self, arg: float, /) -> None: ...

    @property
    def RefractionIndex(self) -> float:
        """IOR (index of refraction) within range [1.0, 3.0]; 1.5 by default"""

    @RefractionIndex.setter
    def RefractionIndex(self, arg: float, /) -> None: ...

    @property
    def IsDefined(self) -> bool:
        """defined flag; TRUE by default"""

    @IsDefined.setter
    def IsDefined(self, arg: bool, /) -> None: ...

class XCAFDoc_VisMaterial(nanoocp.TDF.TDF_Attribute):
    """
    Attribute storing Material definition for visualization purposes.

    Visualization material provides extended information about how object should be displayed on the
    screen (albedo, metalness, roughness - not just a single color as in case of XCAFDoc_Color). It
    is expected to correlate with physical material properties (XCAFDoc_Material), but not
    necessarily (like painted/polished/rusty object).

    The document defines the list of visualization materials via global attribute
    XCAFDoc_VisMaterialTool, while particular material assignment to the shape is done through
    tree-nodes links. Therefore, XCAFDoc_VisMaterialTool methods should be used for managing
    XCAFDoc_VisMaterial attributes.

    Visualization material definition consists of two options: Common and PBR (for Physically Based
    Rendering). Common material definition is an obsolete model defined by very first version of
    OpenGL graphics API and having specific hardware-accelerated implementation in past (like T&L).
    PBR metallic-roughness model is closer to physical material properties, and intended to be used
    within physically-based renderer.

    For compatibility reasons, this attribute allows defining both material models,
    so that it is up-to Data Exchange and Application deciding which one to define and use for
    rendering (depending on viewer capabilities). Automatic conversion from one model to another is
    possible, but lossy (converted material will not look the same).

    Within Data Exchange, different file formats have different capabilities for storing
    visualization material properties from simple color (STEP, IGES), to common (OBJ, glTF 1.0) and
    PBR (glTF 2.0). This should be taken into account while defining or converting document into one
    or another format - material definition might be lost or disturbed.

    @sa XCAFDoc_VisMaterialTool
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: XCAFDoc_VisMaterial) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID:
        """Return attribute GUID."""

    def IsEmpty(self) -> bool:
        """Return TRUE if material definition is empty."""

    def FillMaterialAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """Fill in material aspect."""

    def FillAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Fill in graphic aspects."""

    def HasPbrMaterial(self) -> bool:
        """
        Return TRUE if metal-roughness PBR material is defined; FALSE by default.
        """

    def PbrMaterial(self) -> XCAFDoc_VisMaterialPBR:
        """
        Return metal-roughness PBR material.
        Note that default constructor creates an empty material (@sa
        XCAFDoc_VisMaterialPBR::IsDefined).
        """

    def SetPbrMaterial(self, theMaterial: XCAFDoc_VisMaterialPBR) -> None:
        """Setup metal-roughness PBR material."""

    def UnsetPbrMaterial(self) -> None:
        """Setup undefined metal-roughness PBR material."""

    def HasCommonMaterial(self) -> bool:
        """Return TRUE if common material is defined; FALSE by default."""

    def CommonMaterial(self) -> XCAFDoc_VisMaterialCommon:
        """
        Return common material.
        Note that default constructor creates an empty material (@sa
        XCAFDoc_VisMaterialCommon::IsDefined).
        """

    def SetCommonMaterial(self, theMaterial: XCAFDoc_VisMaterialCommon) -> None:
        """Setup common material."""

    def UnsetCommonMaterial(self) -> None:
        """Setup undefined common material."""

    def BaseColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return base color."""

    def AlphaMode(self) -> nanoocp.Graphic3d.Graphic3d_AlphaMode:
        """Return alpha mode; Graphic3d_AlphaMode_BlendAuto by default."""

    def AlphaCutOff(self) -> float:
        """Return alpha cutoff value; 0.5 by default."""

    def SetAlphaMode(self, theMode: nanoocp.Graphic3d.Graphic3d_AlphaMode, theCutOff: float = 0.5) -> None:
        """Set alpha mode."""

    def FaceCulling(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel:
        """
        Returns if the material is double or single sided; Graphic3d_TypeOfBackfacingModel_Auto by
        default.
        """

    def SetFaceCulling(self, theFaceCulling: nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel) -> None:
        """Specifies whether the material is double or single sided."""

    def IsDoubleSided(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method, FaceCulling() should be used instead
        """

    def SetDoubleSided(self, theIsDoubleSided: bool) -> None:
        """
        Deprecated in OCCT: Deprecated method, SetFaceCulling() should be used instead
        """

    def RawName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Return material name / tag (transient data, not stored in the document).
        """

    def SetRawName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set material name / tag (transient data, not stored in the document)."""

    def IsEqual(self, theOther: XCAFDoc_VisMaterial | None) -> bool:
        """
        Compare two materials.
        Performs deep comparison by actual values - e.g. can be useful for merging materials.
        """

    def ConvertToCommonMaterial(self) -> XCAFDoc_VisMaterialCommon:
        """Return Common material or convert PBR into Common material."""

    def ConvertToPbrMaterial(self) -> XCAFDoc_VisMaterialPBR:
        """Return PBR material or convert Common into PBR material."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """
        @name interface implementation
        Return GUID of this attribute type.
        """

    def Restore(self, theWith: nanoocp.TDF.TDF_Attribute | None) -> None:
        """
        Restore attribute from specified state.
        @param[in] theWith  attribute state to restore (copy into this)
        """

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Create a new empty attribute."""

    def Paste(self, theInto: nanoocp.TDF.TDF_Attribute | None, theRelTable: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """
        Paste this attribute into another one.
        @param theInto [in/out] target attribute to copy this into
        @param[in] theRelTable  relocation table
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class XCAFDoc_VisMaterialTool(nanoocp.TDF.TDF_Attribute):
    """
    Provides tools to store and retrieve attributes (visualization materials) of TopoDS_Shape in and
    from TDocStd_Document.

    This attribute defines the list of visualization materials (XCAFDoc_VisMaterial) within the
    whole document. Particular material is assigned to the shape through tree-nodes links.

    Visualization materials might co-exists with independent color attributes (XCAFDoc_ColorTool),
    but beware to preserve consistency between them (it is better using one attribute type at once
    to avoid ambiguity). Unlike color attributes, list of materials should be managed explicitly by
    application, so that there is no tool eliminating material duplicates or removing unused
    materials.

    @sa XCAFDoc_VisMaterial
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: XCAFDoc_VisMaterialTool) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def Set(L: nanoocp.TDF.TDF_Label) -> XCAFDoc_VisMaterialTool:
        """Creates (if not exist) ColorTool."""

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def BaseLabel(self) -> nanoocp.TDF.TDF_Label:
        """returns the label under which colors are stored"""

    def ShapeTool(self) -> XCAFDoc_ShapeTool:
        """Returns internal XCAFDoc_ShapeTool tool"""

    def IsMaterial(self, theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """Returns TRUE if Label belongs to a Material Table."""

    @staticmethod
    def GetMaterial(theMatLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_VisMaterial:
        """
        Returns Material defined by specified Label, or NULL if the label is not in Material Table.
        """

    @overload
    def AddMaterial(self, theMat: XCAFDoc_VisMaterial | None, theName: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TDF.TDF_Label: ...

    @overload
    def AddMaterial(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TDF.TDF_Label:
        """Adds Material definition to a Material Table and returns its Label."""

    def RemoveMaterial(self, theLabel: nanoocp.TDF.TDF_Label) -> None:
        """Removes Material from the Material Table"""

    def GetMaterials(self, Labels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TDF.TDF_Label]) -> None:
        """
        Returns a sequence of Materials currently stored in the Material Table.
        """

    @overload
    def SetShapeMaterial(self, theShapeLabel: nanoocp.TDF.TDF_Label, theMaterialLabel: nanoocp.TDF.TDF_Label) -> None:
        """Sets new material to the shape."""

    @overload
    def SetShapeMaterial(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theMaterialLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Sets a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material label.
        @param[in] theShape  shape
        @param[in] theMaterialLabel  material label
        @return FALSE if cannot find a label for shape
        """

    @overload
    def UnSetShapeMaterial(self, theShapeLabel: nanoocp.TDF.TDF_Label) -> None:
        """
        Removes a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material.
        """

    @overload
    def UnSetShapeMaterial(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Removes a link with GUID XCAFDoc::VisMaterialRefGUID() from shape label to material.
        @return TRUE if such link existed
        """

    @overload
    def IsSetShapeMaterial(self, theLabel: nanoocp.TDF.TDF_Label) -> bool:
        """Returns TRUE if label has a material assignment."""

    @overload
    def IsSetShapeMaterial(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """Returns TRUE if shape has a material assignment."""

    @overload
    @staticmethod
    def GetShapeMaterial_s(theShapeLabel: nanoocp.TDF.TDF_Label, theMaterialLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns label with material assigned to shape label.
        @param[in] theShapeLabel  shape label
        @param[out] theMaterialLabel  material label
        @return FALSE if no material is assigned
        """

    @overload
    @staticmethod
    def GetShapeMaterial_s(theShapeLabel: nanoocp.TDF.TDF_Label) -> XCAFDoc_VisMaterial:
        """Returns material assigned to the shape label."""

    @overload
    def GetShapeMaterial(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theMaterialLabel: nanoocp.TDF.TDF_Label) -> bool:
        """
        Returns label with material assigned to shape.
        @param[in] theShape  shape
        @param[out] theMaterialLabel  material label
        @return FALSE if no material is assigned
        """

    @overload
    def GetShapeMaterial(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> XCAFDoc_VisMaterial:
        """Returns material assigned to shape or NULL if not assigned."""

    def ID(self) -> nanoocp.Standard.Standard_GUID:
        """Returns GUID of this attribute type."""

    def Restore(self, arg0: nanoocp.TDF.TDF_Attribute | None) -> None:
        """Does nothing."""

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute:
        """Creates new instance of this tool."""

    def Paste(self, arg0: nanoocp.TDF.TDF_Attribute | None, arg1: nanoocp.TDF.TDF_RelocationTable | None) -> None:
        """Does nothing."""

class XCAFDoc_Volume(nanoocp.TDataStd.TDataStd_Real):
    """attribute to store volume"""

    @overload
    def __init__(self) -> None:
        """
        class methods
        =============
        """

    @overload
    def __init__(self, theOther: XCAFDoc_Volume) -> None: ...

    @staticmethod
    def GetID() -> nanoocp.Standard.Standard_GUID: ...

    def ID(self) -> nanoocp.Standard.Standard_GUID: ...

    def Set(self, vol: float) -> None:
        """Sets a value of volume"""

    @staticmethod
    def Set_s(label: nanoocp.TDF.TDF_Label, vol: float) -> XCAFDoc_Volume:
        """Find, or create, an Volume attribute and set its value"""

    def Get(self) -> float: ...

    @staticmethod
    def Get_s(label: nanoocp.TDF.TDF_Label) -> tuple[bool, float]:
        """
        Returns volume as argument
        returns false if no such attribute at the <label>
        """

    def Dump(self) -> str: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NewEmpty(self) -> nanoocp.TDF.TDF_Attribute: ...

# C++ typedef aliases
XCAFDoc_PartId = nanoocp.TCollection.TCollection_AsciiString

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopTools
import nanoocp.XCAFDoc
XCAFDoc_DataMapOfShapeLabel = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TDF.TDF_Label, nanoocp.TopTools.TopTools_ShapeMapHasher]
