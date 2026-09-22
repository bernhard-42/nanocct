"""OCCT package StdSelect (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Prs3d
import nanoocp.PrsMgr
import nanoocp.Select3D
import nanoocp.SelectMgr
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.V3d
import nanoocp.TopTools


class StdSelect_TypeOfEdge(enum.IntEnum):
    """
    Provides values for different types of edges. These
    values are used to filter edges in frameworks
    inheriting StdSelect_EdgeFilter.
    """

    StdSelect_AnyEdge = 0

    StdSelect_Line = 1

    StdSelect_Circle = 2

StdSelect_AnyEdge: StdSelect_TypeOfEdge = StdSelect_TypeOfEdge.StdSelect_AnyEdge

StdSelect_Line: StdSelect_TypeOfEdge = StdSelect_TypeOfEdge.StdSelect_Line

StdSelect_Circle: StdSelect_TypeOfEdge = StdSelect_TypeOfEdge.StdSelect_Circle

class StdSelect_TypeOfFace(enum.IntEnum):
    """
    Provides values for different types of faces. These
    values are used to filter faces in frameworks inheriting
    StdSelect_FaceFilter.
    """

    StdSelect_AnyFace = 0

    StdSelect_Plane = 1

    StdSelect_Cylinder = 2

    StdSelect_Sphere = 3

    StdSelect_Torus = 4

    StdSelect_Revol = 5

    StdSelect_Cone = 6

StdSelect_AnyFace: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_AnyFace

StdSelect_Plane: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Plane

StdSelect_Cylinder: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Cylinder

StdSelect_Sphere: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Sphere

StdSelect_Torus: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Torus

StdSelect_Revol: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Revol

StdSelect_Cone: StdSelect_TypeOfFace = StdSelect_TypeOfFace.StdSelect_Cone

class StdSelect_TypeOfSelectionImage(enum.IntEnum):
    """Type of output selection image."""

    StdSelect_TypeOfSelectionImage_NormalizedDepth = 0

    StdSelect_TypeOfSelectionImage_NormalizedDepthInverted = 1

    StdSelect_TypeOfSelectionImage_UnnormalizedDepth = 2

    StdSelect_TypeOfSelectionImage_ColoredDetectedObject = 3

    StdSelect_TypeOfSelectionImage_ColoredEntity = 4

    StdSelect_TypeOfSelectionImage_ColoredEntityType = 5

    StdSelect_TypeOfSelectionImage_ColoredOwner = 6

    StdSelect_TypeOfSelectionImage_ColoredSelectionMode = 7

    StdSelect_TypeOfSelectionImage_SurfaceNormal = 8

StdSelect_TypeOfSelectionImage_NormalizedDepth: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_UnnormalizedDepth: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_ColoredDetectedObject: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_ColoredEntity: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_ColoredEntityType: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_ColoredOwner: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_ColoredSelectionMode: StdSelect_TypeOfSelectionImage = ...

StdSelect_TypeOfSelectionImage_SurfaceNormal: StdSelect_TypeOfSelectionImage = ...

class StdSelect:
    """
    The StdSelect package provides the following services
    -   the definition of selection modes for topological shapes
    -   the definition of several concrete filtertandard
    Selection2d.ap classes
    -   2D and 3D viewer selectors.
    Note that each new Interactive Object must have all
    its selection modes defined.
    Standard Classes is useful to build
    3D Selectable Objects, and to process
    3D Selections:

    - Implementation of View Selector for dynamic selection
    in Views from V3d.

    - Implementation of Tool class to decompose 3D BRep Objects
    into sensitive Primitives for every desired mode of selection
    (selection of vertex,edges,wires,faces,...)

    -  Implementation of dedicated Sensitives Entities:
    Text for 2D Views (linked to Specific 2D projectors.)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdSelect) -> None: ...

    @staticmethod
    def SetDrawerForBRepOwner(aSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        puts The same drawer in every BRepOwner Of SensitivePrimitive
        Used Only for hilight Of BRepOwner...
        """

class StdSelect_BRepOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """
    Defines Specific Owners for Sensitive Primitives
    (Sensitive Segments,Circles...).
    Used in Dynamic Selection Mechanism.
    A BRepOwner has an Owner (the shape it represents)
    and Users (One or More Transient entities).
    The highlight-unhighlight methods are empty and
    must be redefined by each User.
    """

    @overload
    def __init__(self, aPriority: int) -> None:
        """
        Constructs an owner specification framework defined
        by the priority aPriority.
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, aPriority: int = 0, ComesFromDecomposition: bool = False) -> None:
        """
        Constructs an owner specification framework defined
        by the shape aShape and the priority aPriority.
        aShape and aPriority are stored in this framework. If
        more than one owner are detected during dynamic
        selection, the one with the highest priority is the one stored.
        """

    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape, theOrigin: nanoocp.SelectMgr.SelectMgr_SelectableObject | None, aPriority: int = 0, FromDecomposition: bool = False) -> None:
        """
        Constructs an owner specification framework defined
        by the shape aShape, the selectable object theOrigin
        and the priority aPriority.
        aShape, theOrigin and aPriority are stored in this
        framework. If more than one owner are detected
        during dynamic selection, the one with the highest
        priority is the one stored.
        """

    @overload
    def __init__(self, theOther: StdSelect_BRepOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HasShape(self) -> bool:
        """returns False if no shape was set"""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the shape."""

    def HasHilightMode(self) -> bool:
        """Returns true if this framework has a highlight mode defined for it."""

    def SetHilightMode(self, theMode: int) -> None:
        """
        Sets the highlight mode for this framework.
        This defines the type of display used to highlight the
        owner of the shape when it is detected by the selector.
        The default type of display is wireframe, defined by the index 0.
        """

    def ResetHilightMode(self) -> None:
        """
        Resets the higlight mode for this framework.
        This defines the type of display used to highlight the
        owner of the shape when it is detected by the selector.
        The default type of display is wireframe, defined by the index 0.
        """

    def HilightMode(self) -> int:
        """
        Returns the highlight mode for this framework.
        This defines the type of display used to highlight the
        owner of the shape when it is detected by the selector.
        The default type of display is wireframe, defined by the index 0.
        """

    def IsHilighted(self, aPM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, aMode: int = 0) -> bool:
        """
        Returns true if an object with the selection mode
        aMode is highlighted in the presentation manager aPM.
        """

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None: ...

    def Unhilight(self, aPM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, aMode: int = 0) -> None:
        """
        Removes highlighting from the type of shape
        identified the selection mode aMode in the presentation manager aPM.
        """

    def Clear(self, aPM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, aMode: int = 0) -> None:
        """
        Clears the presentation manager object aPM of all
        shapes with the selection mode aMode.
        """

    def SetLocation(self, aLoc: nanoocp.TopLoc.TopLoc_Location) -> None: ...

    def UpdateHighlightTrsf(self, theViewer: nanoocp.V3d.V3d_Viewer | None, theManager: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theDispMode: int) -> None:
        """
        Implements immediate application of location transformation of parent object to dynamic
        highlight structure
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class StdSelect_BRepSelectionTool:
    """
    Tool to create specific selections (sets of primitives)
    for Shapes from Topology.
    These Selections may be used in dynamic selection
    Mechanism
    Given a Shape and a mode of selection
    (selection of vertices,
    edges,faces ...) , This Tool Computes corresponding sensitive primitives,
    puts them in an entity called Selection (see package SelectMgr) and returns it.

    A Priority for the decomposed pickable objects can be given ;
    by default There is A Preset Hierarchy:
    Vertex             priority : 5
    Edge               priority : 4
    Wire               priority : 3
    Face               priority : 2
    Shell,solid,shape  priority : 1
    the default priority in the following methods has no sense - it's only taken in account
    when the user gives a value between 0 and 10.
    IMPORTANT : This decomposition creates BRepEntityOwner instances (from StdSelect).
    which are stored in the Sensitive Entities coming from The Decomposition.

    the result of picking in a ViewerSelector return EntityOwner from SelectMgr;
    to know what kind of object was picked :

    ENTITY_OWNER -> Selectable() gives the selectableobject which
    was decomposed into pickable elements.
    occ::down_cast<StdSelect_BRepOwner>(ENTITY_OWNER) -> Shape()
    gives the real picked shape (edge,vertex,shape...)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StdSelect_BRepSelectionTool) -> None: ...

    @overload
    @staticmethod
    def Load(aSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, aShape: nanoocp.TopoDS.TopoDS_Shape, aType: nanoocp.TopAbs.TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: bool = True, aPriority: int = -1, NbPOnEdge: int = 9, MaximalParameter: float = 500.0) -> None:
        """
        Decomposition of <aShape> into sensitive entities following
        a mode of decomposition <aType>. These entities are stored in <aSelection>.
        BrepOwners are created to store the identity of the picked shapes
        during the selection process.
        In those BRepOwners is also stored the original shape.
        But One can't get the selectable object which was decomposed to give
        the sensitive entities.
        maximal parameter is used for infinite objects, to limit the sensitive Domain....
        If AutoTriangulation = True, a Triangulation will be
        computed for faces which have no existing one.
        if AutoTriangulation = False the old algorithm will be
        called to compute sensitive entities on faces.
        """

    @overload
    @staticmethod
    def Load(aSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, Origin: nanoocp.SelectMgr.SelectMgr_SelectableObject | None, aShape: nanoocp.TopoDS.TopoDS_Shape, aType: nanoocp.TopAbs.TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: bool = True, aPriority: int = -1, NbPOnEdge: int = 9, MaximalParameter: float = 500.0) -> None:
        """
        Same functionalities. The only
        difference is that the selectable object from which the
        selection comes is stored in each Sensitive EntityOwner;
        decomposition of <aShape> into sensitive entities following
        a mode of decomposition <aType>. These entities are stored in <aSelection>
        The Major difference is that the known users are first inserted in the
        BRepOwners. the original shape is the last user...
        (see EntityOwner from SelectBasics and BrepOwner)...
        """

    @staticmethod
    def GetStandardPriority(theShape: nanoocp.TopoDS.TopoDS_Shape, theType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int:
        """
        Returns the standard priority of the shape aShap having the type aType.
        This priority is passed to a StdSelect_BRepOwner object.
        You can use the function Load to modify the
        selection priority of an owner to make one entity
        more selectable than another one.
        """

    @staticmethod
    def ComputeSensitive(theShape: nanoocp.TopoDS.TopoDS_Shape, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, theDeflection: float, theDeflAngle: float, theNbPOnEdge: int, theMaxiParam: float, theAutoTriang: bool = True) -> None:
        """
        Computes the sensitive primitives, stores them in the SelectMgr_Selection object, and returns
        this object.
        @param[in] theShape        shape to compute sensitive entities
        @param[in] theOwner        selectable owner object
        @param[in] theSelection    selection to append new sensitive entities
        @param[in] theDeflection   linear deflection
        @param[in] theDeflAngle    angular deflection
        @param[in] theNbPOnEdge    sensitivity parameters for edges and wires
        @param[in] theMaxiParam    sensitivity parameters for infinite objects (the default value is
        500)
        @param[in] theAutoTriang   flag to compute triangulation for the faces which have none
        """

    @staticmethod
    def GetSensitiveForFace(theFace: nanoocp.TopoDS.TopoDS_Face, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theOutList: nanoocp.NCollection.NCollection_Sequence[nanoocp.Select3D.Select3D_SensitiveEntity], theAutoTriang: bool = True, theNbPOnEdge: int = 9, theMaxiParam: float = 500.0, theInteriorFlag: bool = True) -> bool:
        """
        Creates the 3D sensitive entities for Face selection.
        @param[in]  theFace         face to compute sensitive entities
        @param[in]  theOwner        selectable owner object
        @param[out] theOutList     output result list to append created entities
        @param[in]  theAutoTriang   obsolete flag (has no effect)
        @param[in]  theNbPOnEdge    sensitivity parameters
        @param[in]  theMaxiParam    sensitivity parameters
        @param[in]  theInteriorFlag flag indicating that face interior (TRUE) or face boundary (FALSE)
        should be selectable
        """

    @staticmethod
    def GetSensitiveForCylinder(theSubfacesMap: nanoocp.NCollection.NCollection_IndexedMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.TopTools.TopTools_ShapeMapHasher], theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None) -> bool:
        """
        Creates a sensitive cylinder.
        @param[in] theSubfacesMap map of cylinder faces
        @param[in] theOwner       selectable owner object
        @param[in] theSelection   selection to append new sensitive entities
        """

    @staticmethod
    def GetEdgeSensitive(theShape: nanoocp.TopoDS.TopoDS_Shape, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, theDeflection: float, theDeviationAngle: float, theNbPOnEdge: int, theMaxiParam: float) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """
        Create a sensitive edge or sensitive wire.
        @param[in]  theShape          either TopoDS_Edge or TopoDS_Wire to compute sensitive entities
        @param[in]  theOwner          selectable owner object
        @param[in]  theSelection      selection to append new sensitive entities
        @param[in]  theDeflection     linear deflection
        @param[in]  theDeviationAngle angular deflection
        @param[in]  theNbPOnEdge      sensitivity parameters
        @param[out] theMaxiParam      sensitivity parameters
        """

    @staticmethod
    def PreBuildBVH(theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None) -> None:
        """
        Traverses the selection given and pre-builds BVH trees for heavyweight
        sensitive entities containing more than BVH_PRIMITIVE_LIMIT (defined in .cxx file)
        sub-elements.
        """

class StdSelect_EdgeFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    A framework to define a filter to select a specific type of edge.
    The types available include:
    -   any edge
    -   a linear edge
    -   a circular edge.
    """

    @overload
    def __init__(self, Edge: StdSelect_TypeOfEdge) -> None:
        """Constructs an edge filter object defined by the type of edge Edge."""

    @overload
    def __init__(self, theOther: StdSelect_EdgeFilter) -> None: ...

    def SetType(self, aNewType: StdSelect_TypeOfEdge) -> None:
        """
        Sets the type of edge aNewType. aNewType is to be highlighted in selection.
        """

    def Type(self) -> StdSelect_TypeOfEdge:
        """Returns the type of edge to be highlighted in selection."""

    def IsOk(self, anobj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    def ActsOn(self, aStandardMode: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StdSelect_FaceFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    A framework to define a filter to select a specific type of face.
    The types available include:
    -   any face
    -   a planar face
    -   a cylindrical face
    -   a spherical face
    -   a toroidal face
    -   a revol face.
    """

    @overload
    def __init__(self, aTypeOfFace: StdSelect_TypeOfFace) -> None:
        """
        Constructs a face filter object defined by the type of face aTypeOfFace.
        """

    @overload
    def __init__(self, theOther: StdSelect_FaceFilter) -> None: ...

    def SetType(self, aNewType: StdSelect_TypeOfFace) -> None:
        """
        Sets the type of face aNewType. aNewType is to be highlighted in selection.
        """

    def Type(self) -> StdSelect_TypeOfFace:
        """Returns the type of face to be highlighted in selection."""

    def IsOk(self, anobj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    def ActsOn(self, aStandardMode: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StdSelect_Shape(nanoocp.PrsMgr.PrsMgr_PresentableObject):
    """Presentable shape only for purpose of display for BRepOwner..."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None = None) -> None: ...

    @overload
    def __init__(self, theOther: StdSelect_Shape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Compute(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theMode: int) -> None: ...

    @overload
    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape: ...

    @overload
    def Shape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class StdSelect_ShapeTypeFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    A filter framework which allows you to define a filter for a specific shape type.
    """

    @overload
    def __init__(self, aType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> None:
        """Constructs a filter object defined by the shape type aType."""

    @overload
    def __init__(self, theOther: StdSelect_ShapeTypeFilter) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Type(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the type of shape selected by the filter."""

    def IsOk(self, anobj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    def ActsOn(self, aStandardMode: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

# C++ typedef aliases
StdSelect_ViewerSelector3d = nanoocp.SelectMgr.SelectMgr_ViewerSelector
