"""OCCT package MeshVS (toolkit TKMeshVS)"""

import enum
from typing import overload

import nanoocp.AIS
import nanoocp.Bnd
import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Prs3d
import nanoocp.PrsMgr
import nanoocp.Quantity
import nanoocp.Select3D
import nanoocp.SelectBasics
import nanoocp.SelectMgr
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TCollection
import nanoocp.gp


MeshVS_BP_Mesh: int = 5

MeshVS_BP_NodalColor: int = 10

MeshVS_BP_ElemColor: int = 15

MeshVS_BP_Text: int = 20

MeshVS_BP_Vector: int = 25

MeshVS_BP_User: int = 30

MeshVS_BP_Default: int = 30

class MeshVS_EntityType(enum.IntEnum):
    MeshVS_ET_NONE = 0

    MeshVS_ET_Node = 1

    MeshVS_ET_0D = 2

    MeshVS_ET_Link = 4

    MeshVS_ET_Face = 8

    MeshVS_ET_Volume = 16

    MeshVS_ET_Element = 30

    MeshVS_ET_All = 31

MeshVS_ET_NONE: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_NONE

MeshVS_ET_Node: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_Node

MeshVS_ET_0D: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_0D

MeshVS_ET_Link: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_Link

MeshVS_ET_Face: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_Face

MeshVS_ET_Volume: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_Volume

MeshVS_ET_Element: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_Element

MeshVS_ET_All: MeshVS_EntityType = MeshVS_EntityType.MeshVS_ET_All

MeshVS_DMF_WireFrame: int = 1

MeshVS_DMF_Shading: int = 2

MeshVS_DMF_Shrink: int = 3

MeshVS_DMF_OCCMask: int = 3

MeshVS_DMF_VectorDataPrs: int = 4

MeshVS_DMF_NodalColorDataPrs: int = 8

MeshVS_DMF_ElementalColorDataPrs: int = 16

MeshVS_DMF_TextDataPrs: int = 32

MeshVS_DMF_EntitiesWithData: int = 64

MeshVS_DMF_DeformedPrsWireFrame: int = 128

MeshVS_DMF_DeformedPrsShading: int = 256

MeshVS_DMF_DeformedPrsShrink: int = 384

MeshVS_DMF_DeformedMask: int = 384

MeshVS_DMF_SelectionPrs: int = 512

MeshVS_DMF_HilightPrs: int = 1024

MeshVS_DMF_User: int = 2048

class MeshVS_MeshSelectionMethod(enum.IntEnum):
    """
    this enumeration describe what type of sensitive entity will be built
    in 0-th selection mode (it means that whole mesh is selected )
    """

    MeshVS_MSM_PRECISE = 0

    MeshVS_MSM_NODES = 1

    MeshVS_MSM_BOX = 2

MeshVS_MSM_PRECISE: MeshVS_MeshSelectionMethod = MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE

MeshVS_MSM_NODES: MeshVS_MeshSelectionMethod = MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES

MeshVS_MSM_BOX: MeshVS_MeshSelectionMethod = MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX

class MeshVS_DrawerAttribute(enum.IntEnum):
    """
    Is it allowed to draw beam and face's edge overlapping with this beam.
    Is mesh drawn with reflective material
    Is colored mesh data representation drawn with reflective material
    What part of face or link will be shown if shrink mode.
    It is recommended this coeff to be between 0 and 1.
    How many nodes is possible to be in face
    If this parameter is true, the compute method CPU time will be displayed in console window
    If this parameter is true, the compute selection method CPU time will be displayed in console
    window If this parameter is false, the nodes won't be shown in viewer, otherwise will be.//! If
    this parameter is true, the selectable nodes map will be updated automatically when hidden
    elements change//! If this parameter is false, the face's edges are not shown Warning: in
    wireframe mode this parameter is ignored Is mesh drawing in smooth shading mode Is back faces of
    volume elements should be suppressed The integer keys for most useful constants attuning mesh
    presentation appearance WARNING: DA_TextExpansionFactor, DA_TextSpace, DA_TextDisplayType have
    no effect and might be removed in the future.
    """

    MeshVS_DA_InteriorStyle = 0

    MeshVS_DA_InteriorColor = 1

    MeshVS_DA_BackInteriorColor = 2

    MeshVS_DA_EdgeColor = 3

    MeshVS_DA_EdgeType = 4

    MeshVS_DA_EdgeWidth = 5

    MeshVS_DA_HatchStyle = 6

    MeshVS_DA_FrontMaterial = 7

    MeshVS_DA_BackMaterial = 8

    MeshVS_DA_BeamType = 9

    MeshVS_DA_BeamWidth = 10

    MeshVS_DA_BeamColor = 11

    MeshVS_DA_MarkerType = 12

    MeshVS_DA_MarkerColor = 13

    MeshVS_DA_MarkerScale = 14

    MeshVS_DA_TextColor = 15

    MeshVS_DA_TextHeight = 16

    MeshVS_DA_TextFont = 17

    MeshVS_DA_TextExpansionFactor = 18

    MeshVS_DA_TextSpace = 19

    MeshVS_DA_TextStyle = 20

    MeshVS_DA_TextDisplayType = 21

    MeshVS_DA_TextTexFont = 22

    MeshVS_DA_TextFontAspect = 23

    MeshVS_DA_VectorColor = 24

    MeshVS_DA_VectorMaxLength = 25

    MeshVS_DA_VectorArrowPart = 26

    MeshVS_DA_IsAllowOverlapped = 27

    MeshVS_DA_Reflection = 28

    MeshVS_DA_ColorReflection = 29

    MeshVS_DA_ShrinkCoeff = 30

    MeshVS_DA_MaxFaceNodes = 31

    MeshVS_DA_ComputeTime = 32

    MeshVS_DA_ComputeSelectionTime = 33

    MeshVS_DA_DisplayNodes = 34

    MeshVS_DA_SelectableAuto = 35

    MeshVS_DA_ShowEdges = 36

    MeshVS_DA_SmoothShading = 37

    MeshVS_DA_SupressBackFaces = 38

    MeshVS_DA_User = 39

MeshVS_DA_InteriorStyle: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle

MeshVS_DA_InteriorColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor

MeshVS_DA_BackInteriorColor: MeshVS_DrawerAttribute = ...

MeshVS_DA_EdgeColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor

MeshVS_DA_EdgeType: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_EdgeType

MeshVS_DA_EdgeWidth: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth

MeshVS_DA_HatchStyle: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle

MeshVS_DA_FrontMaterial: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial

MeshVS_DA_BackMaterial: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial

MeshVS_DA_BeamType: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_BeamType

MeshVS_DA_BeamWidth: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth

MeshVS_DA_BeamColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_BeamColor

MeshVS_DA_MarkerType: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_MarkerType

MeshVS_DA_MarkerColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor

MeshVS_DA_MarkerScale: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale

MeshVS_DA_TextColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextColor

MeshVS_DA_TextHeight: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextHeight

MeshVS_DA_TextFont: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextFont

MeshVS_DA_TextExpansionFactor: MeshVS_DrawerAttribute = ...

MeshVS_DA_TextSpace: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextSpace

MeshVS_DA_TextStyle: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextStyle

MeshVS_DA_TextDisplayType: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType

MeshVS_DA_TextTexFont: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont

MeshVS_DA_TextFontAspect: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect

MeshVS_DA_VectorColor: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_VectorColor

MeshVS_DA_VectorMaxLength: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength

MeshVS_DA_VectorArrowPart: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart

MeshVS_DA_IsAllowOverlapped: MeshVS_DrawerAttribute = ...

MeshVS_DA_Reflection: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_Reflection

MeshVS_DA_ColorReflection: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection

MeshVS_DA_ShrinkCoeff: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff

MeshVS_DA_MaxFaceNodes: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes

MeshVS_DA_ComputeTime: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime

MeshVS_DA_ComputeSelectionTime: MeshVS_DrawerAttribute = ...

MeshVS_DA_DisplayNodes: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes

MeshVS_DA_SelectableAuto: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto

MeshVS_DA_ShowEdges: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges

MeshVS_DA_SmoothShading: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading

MeshVS_DA_SupressBackFaces: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces

MeshVS_DA_User: MeshVS_DrawerAttribute = MeshVS_DrawerAttribute.MeshVS_DA_User

class MeshVS_SelectionModeFlags(enum.IntEnum):
    MeshVS_SMF_Mesh = 0

    MeshVS_SMF_Node = 1

    MeshVS_SMF_0D = 2

    MeshVS_SMF_Link = 4

    MeshVS_SMF_Face = 8

    MeshVS_SMF_Volume = 16

    MeshVS_SMF_Element = 30

    MeshVS_SMF_All = 31

    MeshVS_SMF_Group = 256

MeshVS_SMF_Mesh: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh

MeshVS_SMF_Node: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Node

MeshVS_SMF_0D: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_0D

MeshVS_SMF_Link: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Link

MeshVS_SMF_Face: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Face

MeshVS_SMF_Volume: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Volume

MeshVS_SMF_Element: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Element

MeshVS_SMF_All: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_All

MeshVS_SMF_Group: MeshVS_SelectionModeFlags = MeshVS_SelectionModeFlags.MeshVS_SMF_Group

class MeshVS_Buffer:
    def __init__(self, theSize: int) -> None:
        """Constructor of the buffer of the requested size"""

    def __float__(self) -> float:
        """Interpret the buffer as a reference to double"""

    def __int__(self) -> int:
        """Interpret the buffer as a reference to int"""

class MeshVS_DataSource(nanoocp.Standard.Standard_Transient):
    """
    The deferred class using for the following tasks:
    1) Receiving geometry data about single element of node by its number;
    2) Receiving type of element or node by its number;
    3) Receiving topological information about links between element and nodes it consist of;
    4) Receiving information about what element cover this node;
    5) Receiving information about all nodes and elements the object consist of
    6) Activation of advanced mesh selection. In the advanced mesh selection mode there is created:
    - one owner for the whole mesh and for all selection modes
    - one sensitive entity for the whole mesh and for each selection mode
    Receiving of IDs of detected entities (nodes and elements) in a viewer is achieved by
    implementation of a group of methods GetDetectedEntities.
    """

    def GetGeom(self, ID: int, IsElement: bool, Coords: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[bool, int, MeshVS_EntityType]:
        """
        Returns geometry information about node or element
        ID is the numerical identificator of node or element
        IsElement indicates this ID describe node ( if false ) or element ( if true
        ) Coords is an array of coordinates of node(s). For node it is only 3 numbers: X, Y, Z in the
        strict order For element it is 3*n numbers, where n is number of this element vertices The
        order is strict also: X1, Y1, Z1, X2,...., where Xi, Yi, Zi are coordinates of vertices
        NbNodes is number of nodes. It is recommended this parameter to be set to 1 for node.
        Type is type of node or element (from enumeration). It is recommended this parameter to be set
        to MeshVS_ET_Node for node.
        """

    def GetGeomType(self, ID: int, IsElement: bool) -> tuple[bool, MeshVS_EntityType]:
        """
        This method is similar to GetGeom, but returns only element or node type.
        """

    def Get3DGeom(self, ID: int) -> tuple[bool, int, nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]]:
        """
        This method returns topology information about 3D-element
        Returns false if element with ID isn't 3D or because other troubles
        """

    def GetNodesByElement(self, ID: int, NodeIDs: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[bool, int]:
        """
        This method returns information about nodes this element consist of.
        ID is the numerical identificator of element.
        NodeIDs is the output array of nodes IDs in correct order,
        the same as coordinates returned by GetGeom().
        NbNodes is number of nodes (number of items set in NodeIDs).
        Returns False if element does not exist
        """

    def GetAllNodes(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger:
        """This method returns map of all nodes the object consist of."""

    def GetAllElements(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger:
        """This method returns map of all elements the object consist of."""

    def GetNormal(self, Id: int, Max: int) -> tuple[bool, float, float, float]:
        """
        This method calculates normal of face, which is using for correct reflection presentation.
        There is default method, for advance reflection this method can be redefined.
        Id is the numerical identificator of only element!
        Max is maximal number of nodes an element can consist of
        nx, ny, nz  are values whose represent coordinates of normal (will be returned)
        In the redefined method you can return normal with length more then 1, but in this case
        the appearance of element will be more bright than usual. For ordinary brightness you must
        return normal with length 1
        """

    def GetNodeNormal(self, ranknode: int, ElementId: int) -> tuple[bool, float, float, float]:
        """
        This method return normal of node ranknode of face Id,
        which is using for smooth shading presentation.
        Returns false if normal isn't defined.
        """

    def GetNormalsByElement(self, Id: int, IsNodal: bool, MaxNodes: int) -> tuple[bool, nanoocp.NCollection.NCollection_HArray1[float]]:
        """
        This method puts components of normal vectors at each node of a mesh face (at each face of a
        mesh volume) into the output array. Returns false if some problem was detected during
        calculation of normals. Id is an identifier of the mesh element. IsNodal, when true, means
        that normals at mesh element nodes are needed. If nodal normals are not available, or IsNodal
        is false, or the mesh element is a volume, then the output array contents depend on the
        element type: face: a normal calculated by GetNormal() is duplicated for each node of the
        face; volume: normals to all faces of the volume are computed (not for each node!). MaxNodes
        is maximal number of nodes an element can consist of. Normals contains the result.
        """

    def GetAllGroups(self, Ids: nanoocp.TColStd.TColStd_PackedMapOfInteger) -> None:
        """This method returns map of all groups the object contains."""

    def GetGroup(self, Id: int, Ids: nanoocp.TColStd.TColStd_PackedMapOfInteger) -> tuple[bool, MeshVS_EntityType]:
        """This method returns map of all group elements."""

    def IsAdvancedSelectionEnabled(self) -> bool:
        """
        Returns True if advanced mesh selection is enabled.
        Default implementation returns False.
        It should be redefined to return True for advanced
        mesh selection activation.
        """

    def GetBoundingBox(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns the bounding box of the whole mesh.
        It is used in advanced selection mode to define roughly
        the sensitive area of the mesh.
        It can be redefined to get access to a box computed in advance.
        """

    @overload
    def GetDetectedEntities(self, Prs: MeshVS_Mesh | None, X: float, Y: float, aTol: float) -> tuple[bool, nanoocp.TColStd.TColStd_HPackedMapOfInteger, nanoocp.TColStd.TColStd_HPackedMapOfInteger, float]:
        """
        Returns maps of entities (nodes and elements) detected
        by mouse click at the point (X,Y) on the current view plane,
        with the tolerance aTol.
        DMin - is out argument should return actual detection tolerance.
        Returns True if something is detected.
        It should be redefined if the advanced mesh selection is
        activated. Default implementation returns False.
        """

    @overload
    def GetDetectedEntities(self, Prs: MeshVS_Mesh | None, XMin: float, YMin: float, XMax: float, YMax: float, aTol: float) -> tuple[bool, nanoocp.TColStd.TColStd_HPackedMapOfInteger, nanoocp.TColStd.TColStd_HPackedMapOfInteger]:
        """
        Returns maps of entities (nodes and elements) detected
        by mouse selection with rectangular box (XMin, YMin, XMax, YMax)
        on the current view plane, with the tolerance aTol.
        Returns True if something is detected.
        It should be redefined if the advanced mesh selection is
        activated. Default implementation returns False.
        """

    @overload
    def GetDetectedEntities(self, Prs: MeshVS_Mesh | None, Polyline: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], aBox: nanoocp.Bnd.Bnd_Box2d, aTol: float) -> tuple[bool, nanoocp.TColStd.TColStd_HPackedMapOfInteger, nanoocp.TColStd.TColStd_HPackedMapOfInteger]:
        """
        Returns maps of entities (nodes and elements) detected
        by mouse selection with the polyline <Polyline>
        on the current view plane, with the tolerance aTol.
        Returns True if something is detected.
        It should be redefined if the advanced mesh selection is
        activated. Default implementation returns False.
        """

    @overload
    def GetDetectedEntities(self, Prs: MeshVS_Mesh | None) -> tuple[bool, nanoocp.TColStd.TColStd_HPackedMapOfInteger, nanoocp.TColStd.TColStd_HPackedMapOfInteger]:
        """
        Filter out the maps of mesh entities so as to keep
        only the entities that are allowed to be selected
        according to the current context.
        Returns True if any of the maps has been changed.
        It should be redefined if the advanced mesh selection is
        activated. Default implementation returns False.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_PrsBuilder(nanoocp.Standard.Standard_Transient):
    """
    This class is parent for all builders using in MeshVS_Mesh.
    It provides base fields and methods all buildes need.
    """

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None:
        """
        Builds presentation of certain type of data.
        Prs is presentation object which this method constructs.
        IDs is set of numeric identificators forming object appearance.
        IDsToExclude is set of IDs to exclude from processing. If some entity
        has been excluded, it is not processed by other builders.
        IsElement indicates, IDs is identificators of nodes or elements.
        DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """

    def CustomBuild(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, DisplayMode: int) -> None:
        """
        This method is called to build presentation of custom elements (they have MeshVS_ET_0D type).
        IDs is set of numeric identificators of elements for custom building.
        IDsToExclude is set of IDs to exclude from processing. If some entity
        has been excluded, it is not processed by other builders.
        DisplayMode is numeric constant describing display mode (see MeshVS_DisplayModeFlags.hxx)
        """

    def CustomSensitiveEntity(self, Owner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, SelectMode: int) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """
        This method is called to build sensitive of custom elements ( they have MeshVS_ET_0D type )
        """

    def GetFlags(self) -> int:
        """Returns flags, assigned with builder during creation"""

    def TestFlags(self, DisplayMode: int) -> bool:
        """
        Test whether display mode has flags assigned with this builder.
        This method has default implementation and can be redefined for advance behavior
        Returns true only if display mode is appropriate for this builder
        """

    def GetId(self) -> int:
        """Returns builder ID"""

    def GetPriority(self) -> int:
        """Returns priority; as priority bigger, as soon builder will be called."""

    def GetDataSource(self) -> MeshVS_DataSource:
        """
        Returns custom data source or default ( from MeshVS_Mesh ) if custom is NULL
        """

    def SetDataSource(self, newDS: MeshVS_DataSource | None) -> None:
        """Change custom data source"""

    def GetDrawer(self) -> MeshVS_Drawer:
        """
        Returns custom drawer or default ( from MeshVS_Mesh ) if custom is NULL
        """

    def SetDrawer(self, newDr: MeshVS_Drawer | None) -> None:
        """Change custom drawer"""

    def SetExcluding(self, state: bool) -> None:
        """
        Set excluding state. If it is true, the nodes or elements, processed by current
        builder will be noted and next builder won't process its.
        """

    def IsExcludingOn(self) -> bool:
        """Read excluding state"""

    def SetPresentationManager(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None) -> None:
        """Set presentation manager for builder"""

    def GetPresentationManager(self) -> nanoocp.PrsMgr.PrsMgr_PresentationManager:
        """Get presentation manager of builder"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_Mesh(nanoocp.AIS.AIS_InteractiveObject):
    """
    the main class provides interface to create mesh presentation as a whole
    """

    @overload
    def __init__(self, theIsAllowOverlapped: bool = False) -> None:
        """
        Constructor.
        theIsAllowOverlapped is true, if it is allowed to draw edges overlapped with beams
        Its value is stored in drawer
        """

    @overload
    def __init__(self, theOther: MeshVS_Mesh) -> None: ...

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Returns true for supported display modes basing on a list of defined builders.
        """

    def Compute(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theDispMode: int) -> None:
        """
        Computes presentation using builders added to sequence. Each builder computes
        own part of mesh presentation according to its type.
        """

    def ComputeSelection(self, theSel: nanoocp.SelectMgr.SelectMgr_Selection | None, theSelMode: int) -> None:
        """Computes selection according to SelectMode"""

    def HilightSelected(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theOwners: nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Draw selected owners presentation"""

    def HilightOwnerWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theColor: nanoocp.Prs3d.Prs3d_Drawer | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """Draw hilighted owner presentation"""

    def ClearSelected(self) -> None:
        """Clears internal selection presentation"""

    def GetBuildersCount(self) -> int:
        """How many builders there are in sequence"""

    def GetBuilder(self, Index: int) -> MeshVS_PrsBuilder:
        """Returns builder by its index in sequence"""

    def GetBuilderById(self, Id: int) -> MeshVS_PrsBuilder:
        """Returns builder by its ID"""

    def GetFreeId(self) -> int:
        """
        Returns the smallest positive ID, not occupied by any builder.
        This method using when builder is created with ID = -1
        """

    def AddBuilder(self, Builder: MeshVS_PrsBuilder | None, TreatAsHilighter: bool = False) -> None:
        """
        Adds builder to tale of sequence.
        PrsBuilder is builder to be added
        If TreatAsHilighter is true, MeshVS_Mesh will use this builder to create
        presentation of hilighted and selected owners.
        Only one builder can be hilighter, so that if you call this method with
        TreatAsHilighter = true some times, only last builder will be hilighter
        WARNING: As minimum one builder must be added as hilighter, otherwise selection cannot be
        computed
        """

    @overload
    def SetHilighter(self, Builder: MeshVS_PrsBuilder | None) -> None:
        """Changes hilighter ( see above )"""

    @overload
    def SetHilighter(self, Index: int) -> bool:
        """Sets builder with sequence index "Index" as hilighter"""

    def SetHilighterById(self, Id: int) -> bool:
        """Sets builder with identificator "Id" as hilighter"""

    def GetHilighter(self) -> MeshVS_PrsBuilder:
        """Returns hilighter"""

    def RemoveBuilder(self, Index: int) -> None:
        """
        Removes builder from sequence. If it is hilighter, hilighter will be NULL
        ( Don't remember to set it to other after!!! )
        """

    def RemoveBuilderById(self, Id: int) -> None:
        """Removes builder with identificator Id"""

    @overload
    def FindBuilder(self, TypeString: str) -> MeshVS_PrsBuilder:
        """
        Deprecated in OCCT: This method will be removed right after 7.9 release. Use FindBuilder(const occ::handle<Standard_Type>&) instead or directly iterate under sequence of builders.

        Finds builder by its type the string represents
        """

    @overload
    def FindBuilder(self, TypeString: nanoocp.Standard.Standard_Type | None) -> MeshVS_PrsBuilder:
        """Finds builder by its type the type represents"""

    def GetOwnerMaps(self, IsElement: bool) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.SelectMgr.SelectMgr_EntityOwner]:
        """Returns map of owners."""

    def GetDataSource(self) -> MeshVS_DataSource:
        """Returns default builders' data source"""

    def SetDataSource(self, aDataSource: MeshVS_DataSource | None) -> None:
        """Sets default builders' data source"""

    def GetDrawer(self) -> MeshVS_Drawer:
        """Returns default builders' drawer"""

    def SetDrawer(self, aDrawer: MeshVS_Drawer | None) -> None:
        """Sets default builders' drawer"""

    def IsHiddenElem(self, ID: int) -> bool:
        """
        Returns True if specified element is hidden
        By default no elements are hidden
        """

    def IsHiddenNode(self, ID: int) -> bool:
        """
        Returns True if specified node is hidden.
        By default all nodes are hidden
        """

    def IsSelectableElem(self, ID: int) -> bool:
        """Returns True if specified element is not hidden"""

    def IsSelectableNode(self, ID: int) -> bool:
        """Returns True if specified node is specified as selectable."""

    def GetHiddenNodes(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns map of hidden nodes (may be null handle)"""

    def SetHiddenNodes(self, Ids: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> None:
        """
        Sets map of hidden nodes, which shall not be displayed individually.
        If nodes shared by some elements shall not be drawn,
        they should be included into that map
        """

    def GetHiddenElems(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns map of hidden elements (may be null handle)"""

    def SetHiddenElems(self, Ids: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> None:
        """Sets map of hidden elements"""

    def GetSelectableNodes(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns map of selectable elements (may be null handle)"""

    def SetSelectableNodes(self, Ids: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> None:
        """Sets map of selectable nodes."""

    def UpdateSelectableNodes(self) -> None:
        """
        Automatically computes selectable nodes; the node is considered
        as being selectable if it is either not hidden, or is hidden
        but referred by at least one non-hidden element.
        Thus all nodes that are visible (either individually, or as ends or
        corners of elements) are selectable by default.
        """

    def GetMeshSelMethod(self) -> MeshVS_MeshSelectionMethod:
        """Returns set mesh selection method (see MeshVS.cdl)"""

    def SetMeshSelMethod(self, M: MeshVS_MeshSelectionMethod) -> None:
        """Sets mesh selection method (see MeshVS.cdl)"""

    def IsWholeMeshOwner(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """Returns True if the given owner represents a whole mesh."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_CommonSensitiveEntity(nanoocp.Select3D.Select3D_SensitiveSet):
    """Sensitive entity covering entire mesh for global selection."""

    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theParentMesh: MeshVS_Mesh | None, theSelMethod: MeshVS_MeshSelectionMethod) -> None:
        """Default constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NbSubElements(self) -> int:
        """Number of elements."""

    def Size(self) -> int:
        """Returns the amount of sub-entities of the complex entity"""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of sub-entity with index theIdx in sub-entity list
        """

    def Center(self, theIdx: int, theAxis: int) -> float:
        """
        Returns geometry center of sensitive entity index theIdx along the given axis theAxis
        """

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps items with indexes theIdx1 and theIdx2"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        Returns bounding box of the triangulation. If location
        transformation is set, it will be applied
        """

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of a mesh"""

    def GetConnected(self) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """Create a copy."""

class MeshVS_DataSource3D(MeshVS_DataSource):
    def GetPrismTopology(self, BasePoints: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]: ...

    def GetPyramidTopology(self, BasePoints: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]: ...

    @staticmethod
    def CreatePrismTopology(BasePoints: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]: ...

    @staticmethod
    def CreatePyramidTopology(BasePoints: int) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_DeformedDataSource(MeshVS_DataSource):
    """
    The class provides default class which helps to represent node displacements by deformed mesh
    This class has an internal handle to canonical non-deformed mesh data source and
    map of displacement vectors. The displacement can be magnified to useful size.
    All methods is implemented with calling the corresponding methods of non-deformed data source.
    """

    @overload
    def __init__(self, theNonDeformDS: MeshVS_DataSource | None, theMagnify: float) -> None:
        """
        Constructor
        theNonDeformDS is canonical non-deformed data source, by which we are able to calculate
        deformed mesh geometry
        theMagnify is coefficient of displacement magnify
        """

    @overload
    def __init__(self, theOther: MeshVS_DeformedDataSource) -> None: ...

    def GetGeom(self, ID: int, IsElement: bool, Coords: nanoocp.NCollection.NCollection_Array1[float]) -> tuple[bool, int, MeshVS_EntityType]: ...

    def GetGeomType(self, ID: int, IsElement: bool) -> tuple[bool, MeshVS_EntityType]: ...

    def Get3DGeom(self, ID: int) -> tuple[bool, int, nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]]: ...

    def GetNodesByElement(self, ID: int, NodeIDs: nanoocp.NCollection.NCollection_Array1[int]) -> tuple[bool, int]: ...

    def GetAllNodes(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger: ...

    def GetAllElements(self) -> nanoocp.TColStd.TColStd_PackedMapOfInteger: ...

    def GetVectors(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.gp.gp_Vec]:
        """This method returns map of nodal displacement vectors"""

    def SetVectors(self, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.gp.gp_Vec]) -> None:
        """This method sets map of nodal displacement vectors (Map)."""

    def GetVector(self, ID: int, Vect: nanoocp.gp.gp_Vec) -> bool:
        """This method returns vector ( Vect ) assigned to node number ID."""

    def SetVector(self, ID: int, Vect: nanoocp.gp.gp_Vec) -> None:
        """This method sets vector ( Vect ) assigned to node number ID."""

    def SetNonDeformedDataSource(self, theDS: MeshVS_DataSource | None) -> None: ...

    def GetNonDeformedDataSource(self) -> MeshVS_DataSource:
        """
        With this methods you can read and change internal canonical data source
        """

    def SetMagnify(self, theMagnify: float) -> None: ...

    def GetMagnify(self) -> float:
        """
        With this methods you can read and change magnify coefficient of nodal displacements
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_Drawer(nanoocp.Standard.Standard_Transient):
    """
    This class provided the common interface to share between classes
    big set of constants affecting to object appearance. By default, this class
    can store integers, doubles, OCC colors, OCC materials. Each of OCC enum members
    can be stored as integers.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_Drawer) -> None: ...

    def Assign(self, aDrawer: MeshVS_Drawer | None) -> None:
        """This method copies other drawer contents to this."""

    def SetInteger(self, Key: int, Value: int) -> None: ...

    def SetDouble(self, Key: int, Value: float) -> None: ...

    def SetBoolean(self, Key: int, Value: bool) -> None: ...

    def SetColor(self, Key: int, Value: nanoocp.Quantity.Quantity_Color) -> None: ...

    def SetMaterial(self, Key: int, Value: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None: ...

    def SetAsciiString(self, Key: int, Value: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def GetInteger(self, Key: int) -> tuple[bool, int]: ...

    def GetDouble(self, Key: int) -> tuple[bool, float]: ...

    def GetBoolean(self, Key: int) -> tuple[bool, bool]: ...

    def GetColor(self, Key: int, Value: nanoocp.Quantity.Quantity_Color) -> bool: ...

    def GetMaterial(self, Key: int, Value: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> bool: ...

    def GetAsciiString(self, Key: int, Value: nanoocp.TCollection.TCollection_AsciiString) -> bool: ...

    def RemoveInteger(self, Key: int) -> bool: ...

    def RemoveDouble(self, Key: int) -> bool: ...

    def RemoveBoolean(self, Key: int) -> bool: ...

    def RemoveColor(self, Key: int) -> bool: ...

    def RemoveMaterial(self, Key: int) -> bool: ...

    def RemoveAsciiString(self, Key: int) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_DummySensitiveEntity(nanoocp.Select3D.Select3D_SensitiveEntity):
    """
    This class allows to create owners to all elements or nodes,
    both hidden and shown, but these owners user cannot select "by hands"
    in viewer. They means for internal application tasks, for example, receiving
    all owners, both for hidden and shown entities.
    """

    @overload
    def __init__(self, theOwnerId: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_DummySensitiveEntity) -> None: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    def NbSubElements(self) -> int: ...

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3: ...

    def BVH(self) -> None: ...

    def ToBuildBVH(self) -> bool: ...

    def Clear(self) -> None: ...

    def HasInitLocation(self) -> bool: ...

    def InvInitLocation(self) -> nanoocp.gp.gp_GTrsf: ...

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_TwoColors:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_TwoColors) -> None: ...

    def __eq__(self, TwoColors: MeshVS_TwoColors) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def r1(self) -> int: ...

    @r1.setter
    def r1(self, arg: int, /) -> None: ...

    @property
    def g1(self) -> int: ...

    @g1.setter
    def g1(self, arg: int, /) -> None: ...

    @property
    def b1(self) -> int: ...

    @b1.setter
    def b1(self, arg: int, /) -> None: ...

    @property
    def r2(self) -> int: ...

    @r2.setter
    def r2(self, arg: int, /) -> None: ...

    @property
    def g2(self) -> int: ...

    @g2.setter
    def g2(self, arg: int, /) -> None: ...

    @property
    def b2(self) -> int: ...

    @b2.setter
    def b2(self, arg: int, /) -> None: ...

class MeshVS_ElementalColorPrsBuilder(MeshVS_PrsBuilder):
    """
    This class provides methods to create presentation of elements with
    assigned colors. The class contains two color maps: map of same colors for front
    and back side of face and map of different ones,
    """

    @overload
    def __init__(self, Parent: MeshVS_Mesh | None, Flags: int = 16, DS: MeshVS_DataSource | None = None, Id: int = -1, Priority: int = 15) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: MeshVS_ElementalColorPrsBuilder) -> None: ...

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None:
        """Builds presentation of elements with assigned colors."""

    def GetColors1(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Quantity.Quantity_Color]:
        """Returns map of colors same for front and back side of face."""

    def SetColors1(self, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Quantity.Quantity_Color]) -> None:
        """Sets map of colors same for front and back side of face."""

    def HasColors1(self) -> bool:
        """Returns true, if map of colors isn't empty"""

    def GetColor1(self, ID: int, theColor: nanoocp.Quantity.Quantity_Color) -> bool:
        """Returns color assigned with element number ID"""

    def SetColor1(self, ID: int, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color assigned with element number ID"""

    def GetColors2(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.MeshVS.MeshVS_TwoColors]:
        """Returns map of different colors for front and back side of face"""

    def SetColors2(self, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.MeshVS.MeshVS_TwoColors]) -> None:
        """Sets map of different colors for front and back side of face"""

    def HasColors2(self) -> bool:
        """Returns true, if map isn't empty"""

    @overload
    def GetColor2(self, ID: int, theColor: MeshVS_TwoColors) -> bool:
        """Returns colors assigned with element number ID"""

    @overload
    def GetColor2(self, ID: int, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color) -> bool:
        """
        Returns colors assigned with element number ID
        theColor1 is the front element color
        theColor2 is the back element color
        """

    @overload
    def SetColor2(self, ID: int, theTwoColors: MeshVS_TwoColors) -> None:
        """Sets colors assigned with element number ID"""

    @overload
    def SetColor2(self, ID: int, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color assigned with element number ID
        theColor1 is the front element color
        theColor2 is the back element color
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_MeshEntityOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """
    The custom owner. This class provides methods to store owner information:
    1) An address of element or node data structure
    2) Type of node or element owner assigned
    3) ID of node or element owner assigned
    """

    def __init__(self, theOther: MeshVS_MeshEntityOwner) -> None: ...

    def Type(self) -> MeshVS_EntityType:
        """Returns type of element or node data structure"""

    def ID(self) -> int:
        """Returns ID of element or node data structure"""

    def IsGroup(self) -> bool:
        """Returns true if owner represents group of nodes or elements"""

    def IsHilighted(self, PM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, Mode: int = 0) -> bool:
        """Returns true if owner is hilighted"""

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None:
        """Hilights owner with the certain color"""

    def Unhilight(self, PM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, Mode: int = 0) -> None:
        """Strip hilight of owner"""

    def Clear(self, PM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, Mode: int = 0) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_MeshOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """
    The custom mesh owner used for advanced mesh selection. This class provides methods to store
    information: 1) IDs of hilighted mesh nodes and elements 2) IDs of mesh nodes and elements
    selected on the mesh
    """

    @overload
    def __init__(self, theSelObj: nanoocp.SelectMgr.SelectMgr_SelectableObject, theDS: MeshVS_DataSource | None, thePriority: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_MeshOwner) -> None: ...

    def GetDataSource(self) -> MeshVS_DataSource: ...

    def GetSelectedNodes(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns ids of selected mesh nodes"""

    def GetSelectedElements(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns ids of selected mesh elements"""

    def AddSelectedEntities(self, Nodes: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None, Elems: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> None:
        """Saves ids of selected mesh entities"""

    def ClearSelectedEntities(self) -> None:
        """Clears ids of selected mesh entities"""

    def GetDetectedNodes(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns ids of hilighted mesh nodes"""

    def GetDetectedElements(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """Returns ids of hilighted mesh elements"""

    def SetDetectedEntities(self, Nodes: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None, Elems: nanoocp.TColStd.TColStd_HPackedMapOfInteger | None) -> None:
        """Saves ids of hilighted mesh entities"""

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theColor: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None: ...

    def Unhilight(self, PM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, Mode: int = 0) -> None: ...

    def IsForcedHilight(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_MeshPrsBuilder(MeshVS_PrsBuilder):
    """This class provides methods to compute base mesh presentation"""

    @overload
    def __init__(self, Parent: MeshVS_Mesh | None, Flags: int = 3, DS: MeshVS_DataSource | None = None, Id: int = -1, Priority: int = 5) -> None:
        """
        Creates builder with certain display mode flags, data source, ID and priority
        """

    @overload
    def __init__(self, theOther: MeshVS_MeshPrsBuilder) -> None: ...

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None:
        """Builds base mesh presentation by calling the methods below"""

    def BuildNodes(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, DisplayMode: int) -> None:
        """Builds nodes presentation"""

    def BuildElements(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, DisplayMode: int) -> None:
        """Builds elements presentation"""

    def BuildHilightPrs(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool) -> None:
        """Builds presentation of hilighted entity"""

    @staticmethod
    def AddVolumePrs(Topo: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]] | None, Nodes: nanoocp.NCollection.NCollection_Array1[float], NbNodes: int, Array: nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives | None, IsReflected: bool, IsShrinked: bool, IsSelect: bool, ShrinkCoef: float) -> None:
        """Add to array polygons or polylines representing volume"""

    @staticmethod
    def HowManyPrimitives(Topo: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]] | None, AsPolygons: bool, IsSelect: bool, NbNodes: int) -> tuple[int, int]:
        """
        Calculate how many polygons or polylines are necessary to draw passed topology
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_NodalColorPrsBuilder(MeshVS_PrsBuilder):
    """
    This class provides methods to create presentation of nodes with assigned color.
    There are two ways of presentation building
    1. Without using texture.
    In this case colors of nodes are specified with DataMapOfIntegerColor and presentation
    is built with gradient fill between these nodes (default behaviour)
    2. Using texture.
    In this case presentation is built with spectrum filling between nodes. For example, if
    one node has blue color and second one has violet color, parameters of this class may be
    set to fill presentation between nodes with solar spectrum.
    Methods:
    UseTexture - activates/deactivates this way
    SetColorMap - sets colors used for generation of texture
    SetColorindices - specifies correspondence between node IDs and indices of colors from color map
    """

    @overload
    def __init__(self, Parent: MeshVS_Mesh | None, Flags: int = 8, DS: MeshVS_DataSource | None = None, Id: int = -1, Priority: int = 10) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_NodalColorPrsBuilder) -> None: ...

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None:
        """Builds presentation of nodes with assigned color."""

    def GetColors(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Quantity.Quantity_Color]:
        """Returns map of colors assigned to nodes."""

    def SetColors(self, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Quantity.Quantity_Color]) -> None:
        """Sets map of colors assigned to nodes."""

    def HasColors(self) -> bool:
        """Returns true, if map isn't empty"""

    def GetColor(self, ID: int, theColor: nanoocp.Quantity.Quantity_Color) -> bool:
        """Returns color assigned to single node"""

    def SetColor(self, ID: int, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color assigned to single node"""

    def UseTexture(self, theToUse: bool) -> None:
        """Specify whether texture must be used to build presentation"""

    def IsUseTexture(self) -> bool:
        """Verify whether texture is used to build presentation"""

    def SetColorMap(self, theColors: nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]) -> None:
        """
        Set colors to be used for texrture presentation
        theColors - colors for valid coordinates (laying in range [0, 1])
        """

    def GetColorMap(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]:
        """Return colors used for texrture presentation"""

    def SetInvalidColor(self, theInvalidColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Set color representing invalid texture coordinate
        (laying outside range [0, 1])
        """

    def GetInvalidColor(self) -> nanoocp.Quantity.Quantity_Color:
        """
        Return color representing invalid texture coordinate
        (laying outside range [0, 1])
        """

    def SetTextureCoords(self, theMap: nanoocp.NCollection.NCollection_DataMap[int, float]) -> None:
        """
        Specify correspondence between node IDs and texture coordinates (range [0, 1])
        """

    def GetTextureCoords(self) -> nanoocp.NCollection.NCollection_DataMap[int, float]:
        """
        Get correspondence between node IDs and texture coordinates (range [0, 1])
        """

    def SetTextureCoord(self, theID: int, theCoord: float) -> None:
        """
        Specify correspondence between node ID and texture coordinate (range [0, 1])
        """

    def GetTextureCoord(self, theID: int) -> float:
        """
        Return correspondence between node IDs and texture coordinate (range [0, 1])
        """

    def AddVolumePrs(self, theTopo: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]] | None, theNodes: nanoocp.NCollection.NCollection_Array1[int], theCoords: nanoocp.NCollection.NCollection_Array1[float], theArray: nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives | None, theIsShaded: bool, theNbColors: int, theNbTexColors: int, theColorRatio: float) -> None:
        """Add to array polygons or polylines representing volume"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SensitiveFace(nanoocp.Select3D.Select3D_SensitiveFace):
    """
    This class provides custom sensitive face, which will be selected if it center is in rectangle.
    """

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theSensType: nanoocp.Select3D.Select3D_TypeOfSensitivity = Select3D_TypeOfSensitivity.Select3D_TOS_INTERIOR) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_SensitiveFace) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SensitiveMesh(nanoocp.Select3D.Select3D_SensitiveEntity):
    """
    This class provides custom mesh sensitive entity used in advanced mesh selection.
    """

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theMode: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_SensitiveMesh) -> None: ...

    def GetMode(self) -> int: ...

    def GetConnected(self) -> nanoocp.Select3D.Select3D_SensitiveEntity: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether sensitive overlaps current selecting volume."""

    def NbSubElements(self) -> int:
        """Returns the amount of mesh nodes"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns bounding box of mesh"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of mesh"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SensitivePolyhedron(nanoocp.Select3D.Select3D_SensitiveEntity):
    """
    This class is used to detect selection of a polyhedron. The main
    principle of detection algorithm is to search for overlap with
    each polyhedron's face separately, treating them as planar convex
    polygons.
    """

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theNodes: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], theTopo: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]] | None) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_SensitivePolyhedron) -> None: ...

    def GetConnected(self) -> nanoocp.Select3D.Select3D_SensitiveEntity: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool: ...

    def NbSubElements(self) -> int:
        """Returns the amount of nodes of polyhedron"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3: ...

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SensitiveSegment(nanoocp.Select3D.Select3D_SensitiveSegment):
    """
    This class provides custom sensitive face, which will be selected if it center is in rectangle.
    """

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theFirstPnt: nanoocp.gp.gp_Pnt, theLastPnt: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_SensitiveSegment) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SensitiveQuad(nanoocp.Select3D.Select3D_SensitiveEntity):
    """
    This class contains description of planar quadrangle and defines methods
    for its detection by OCCT BVH selection mechanism
    """

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theQuadVerts: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt]) -> None: ...

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, thePnt1: nanoocp.gp.gp_Pnt, thePnt2: nanoocp.gp.gp_Pnt, thePnt3: nanoocp.gp.gp_Pnt, thePnt4: nanoocp.gp.gp_Pnt) -> None:
        """
        Creates a new instance and initializes quadrangle vertices with the given points
        """

    @overload
    def __init__(self, theOther: MeshVS_SensitiveQuad) -> None: ...

    def NbSubElements(self) -> int:
        """Returns the amount of sub-entities in sensitive"""

    def GetConnected(self) -> nanoocp.Select3D.Select3D_SensitiveEntity:
        """Returns a copy of this sensitive quadrangle"""

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether the box overlaps current selecting volume"""

    def CenterOfGeometry(self) -> nanoocp.gp.gp_Pnt:
        """Returns center of the box"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns coordinates of the box"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_SymmetricPairHasher:
    """Provides symmetric hash methods pair of integers."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_SymmetricPairHasher) -> None: ...

    @overload
    def __call__(self, theNodePair: tuple[int, int]) -> int:
        """
        Computes a hash code for the node pair
        @param theNodePair the node pair which hash code is to be computed
        @return a computed hash code
        """

    @overload
    def __call__(self, thePair1: tuple[int, int], thePair2: tuple[int, int]) -> bool: ...

class MeshVS_TextPrsBuilder(MeshVS_PrsBuilder):
    """
    This class provides methods to create text data presentation.
    It store map of texts assigned with nodes or elements.
    """

    @overload
    def __init__(self, Parent: MeshVS_Mesh | None, Height: float, Color: nanoocp.Quantity.Quantity_Color, Flags: int = 32, DS: MeshVS_DataSource | None = None, Id: int = -1, Priority: int = 20) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_TextPrsBuilder) -> None: ...

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, theDisplayMode: int) -> None:
        """Builds presentation of text data"""

    def GetTexts(self, IsElement: bool) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns map of text assigned with nodes ( IsElement = False ) or elements ( IsElement = True )
        """

    def SetTexts(self, IsElement: bool, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Sets map of text assigned with nodes or elements"""

    def HasTexts(self, IsElement: bool) -> bool:
        """Returns True if map isn't empty"""

    def GetText(self, IsElement: bool, ID: int, Text: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns text assigned with single node or element"""

    def SetText(self, IsElement: bool, ID: int, Text: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets text assigned with single node or element"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MeshVS_Tool:
    """This class provides auxiliary methods to create different aspects"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_Tool) -> None: ...

    @overload
    @staticmethod
    def CreateAspectFillArea3d(theDr: MeshVS_Drawer | None, UseDefaults: bool = True) -> nanoocp.Graphic3d.Graphic3d_AspectFillArea3d:
        """
        Creates fill area aspect with values from Drawer according to keys from DrawerAttribute
        """

    @overload
    @staticmethod
    def CreateAspectFillArea3d(theDr: MeshVS_Drawer | None, Mat: nanoocp.Graphic3d.Graphic3d_MaterialAspect, UseDefaults: bool = True) -> nanoocp.Graphic3d.Graphic3d_AspectFillArea3d:
        """
        Creates fill aspect with values from Drawer according to keys from DrawerAttribute
        and specific material aspect
        """

    @staticmethod
    def CreateAspectLine3d(theDr: MeshVS_Drawer | None, UseDefaults: bool = True) -> nanoocp.Graphic3d.Graphic3d_AspectLine3d:
        """
        Creates line aspect with values from Drawer according to keys from DrawerAttribute
        """

    @staticmethod
    def CreateAspectMarker3d(theDr: MeshVS_Drawer | None, UseDefaults: bool = True) -> nanoocp.Graphic3d.Graphic3d_AspectMarker3d:
        """
        Creates marker aspect with values from Drawer according to keys from DrawerAttribute
        """

    @staticmethod
    def CreateAspectText3d(theDr: MeshVS_Drawer | None, UseDefaults: bool = True) -> nanoocp.Graphic3d.Graphic3d_AspectText3d:
        """
        Creates text aspect with values from Drawer according to keys from DrawerAttribute
        """

    @staticmethod
    def GetNormal(Nodes: nanoocp.NCollection.NCollection_Array1[float], Norm: nanoocp.gp.gp_Vec) -> bool:
        """
        Get one of normals to polygon described by these points.
        If the polygon isn't planar, function returns false
        """

    @staticmethod
    def GetAverageNormal(Nodes: nanoocp.NCollection.NCollection_Array1[float], Norm: nanoocp.gp.gp_Vec) -> bool:
        """
        Get an average of normals to non-planar polygon described by these points or compute
        normal of planar polygon. If the polygon isn't planar, function returns false
        """

class MeshVS_TwoNodes:
    """
    Structure containing two IDs (of nodes) for using as a key in a map
    (as representation of a mesh link)
    """

    @overload
    def __init__(self, aFirst: int = 0, aSecond: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_TwoNodes) -> None: ...

    def __eq__(self, theTwoNode: MeshVS_TwoNodes) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def First(self) -> int: ...

    @First.setter
    def First(self, arg: int, /) -> None: ...

    @property
    def Second(self) -> int: ...

    @Second.setter
    def Second(self, arg: int, /) -> None: ...

class MeshVS_VectorPrsBuilder(MeshVS_PrsBuilder):
    """
    This class provides methods to create vector data presentation.
    It store map of vectors assigned with nodes or elements.
    In simplified mode vectors draws with thickened ends instead of arrows
    """

    @overload
    def __init__(self, Parent: MeshVS_Mesh | None, MaxLength: float, VectorColor: nanoocp.Quantity.Quantity_Color, Flags: int = 4, DS: MeshVS_DataSource | None = None, Id: int = -1, Priority: int = 25, IsSimplePrs: bool = False) -> None: ...

    @overload
    def __init__(self, theOther: MeshVS_VectorPrsBuilder) -> None: ...

    def Build(self, Prs: nanoocp.Graphic3d.Graphic3d_Structure | None, IDs: nanoocp.TColStd.TColStd_PackedMapOfInteger, IDsToExclude: nanoocp.TColStd.TColStd_PackedMapOfInteger, IsElement: bool, theDisplayMode: int) -> None:
        """Builds vector data presentation"""

    def DrawVector(self, theTrsf: nanoocp.gp.gp_Trsf, Length: float, MaxLength: float, ArrowPoints: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Lines: nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives | None, ArrowLines: nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives | None, Triangles: nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives | None) -> None:
        """
        Adds to array of polygons and polylines some primitive representing single vector
        """

    @staticmethod
    def calculateArrow(Points: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt], Length: float, ArrowPart: float) -> float:
        """Calculates points of arrow presentation"""

    def GetVectors(self, IsElement: bool) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.gp.gp_Vec]:
        """Returns map of vectors assigned with nodes or elements"""

    def SetVectors(self, IsElement: bool, Map: nanoocp.NCollection.NCollection_DataMap[int, nanoocp.gp.gp_Vec]) -> None:
        """Sets map of vectors assigned with nodes or elements"""

    def HasVectors(self, IsElement: bool) -> bool:
        """Returns true, if map isn't empty"""

    def GetVector(self, IsElement: bool, ID: int, Vect: nanoocp.gp.gp_Vec) -> bool:
        """Returns vector assigned with certain node or element"""

    def SetVector(self, IsElement: bool, ID: int, Vect: nanoocp.gp.gp_Vec) -> None:
        """Sets vector assigned with certain node or element"""

    def GetMinMaxVectorValue(self, IsElement: bool) -> tuple[float, float]:
        """
        Calculates minimal and maximal length of vectors in map
        ( nodal, if IsElement = False or elemental, if IsElement = True )
        """

    def SetSimplePrsMode(self, IsSimpleArrow: bool) -> None:
        """
        Sets flag that indicates is simple vector arrow mode uses or not
        default value is False
        """

    def SetSimplePrsParams(self, theLineWidthParam: float, theStartParam: float, theEndParam: float) -> None:
        """
        Sets parameters of simple vector arrwo presentation
        theLineWidthParam - coefficient of vector line width (to draw line instead of arrow)
        theStartParam and theEndParam parameters of start and end of thickened ends
        position of thickening calculates according to parameters and maximum vector length
        default values are:
        theLineWidthParam = 2.5
        theStartParam     = 0.85
        theEndParam       = 0.95
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

def BindTwoColors(arg0: nanoocp.Quantity.Quantity_Color, arg1: nanoocp.Quantity.Quantity_Color) -> MeshVS_TwoColors: ...

def ExtractColor(arg0: MeshVS_TwoColors, arg1: int) -> nanoocp.Quantity.Quantity_Color: ...

def ExtractColors(arg0: MeshVS_TwoColors, arg1: nanoocp.Quantity.Quantity_Color, arg2: nanoocp.Quantity.Quantity_Color) -> None: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.MeshVS
MeshVS_Array1OfSequenceOfInteger = nanoocp.NCollection.NCollection_Array1[nanoocp.NCollection.NCollection_Sequence[int]]
MeshVS_HArray1OfSequenceOfInteger = nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_Sequence[int]]
