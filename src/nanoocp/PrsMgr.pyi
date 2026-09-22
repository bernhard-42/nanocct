"""OCCT package PrsMgr (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Aspect
import nanoocp.Bnd
import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Prs3d
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TopLoc
import nanoocp.V3d
import nanoocp.gp
import nanoocp.PrsMgr


class PrsMgr_DisplayStatus(enum.IntEnum):
    """To give the display status of an Interactive Object."""

    PrsMgr_DisplayStatus_Displayed = 0

    PrsMgr_DisplayStatus_Erased = 1

    PrsMgr_DisplayStatus_None = 2

    AIS_DS_Displayed = 0

    AIS_DS_Erased = 1

    AIS_DS_None = 2

PrsMgr_DisplayStatus_Displayed: PrsMgr_DisplayStatus = ...

PrsMgr_DisplayStatus_Erased: PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.PrsMgr_DisplayStatus_Erased

PrsMgr_DisplayStatus_None: PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.PrsMgr_DisplayStatus_None

AIS_DS_Displayed: PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.AIS_DS_Displayed

AIS_DS_Erased: PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.AIS_DS_Erased

AIS_DS_None: PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.AIS_DS_None

class PrsMgr_TypeOfPresentation3d(enum.IntEnum):
    """The type of presentation."""

    PrsMgr_TOP_AllView = 0

    PrsMgr_TOP_ProjectorDependent = 1

PrsMgr_TOP_AllView: PrsMgr_TypeOfPresentation3d = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView

PrsMgr_TOP_ProjectorDependent: PrsMgr_TypeOfPresentation3d = ...

class PrsMgr_Presentation(nanoocp.Graphic3d.Graphic3d_Structure):
    def __init__(self, theOther: PrsMgr_Presentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Presentation(self) -> nanoocp.Graphic3d.Graphic3d_Structure:
        """Deprecated in OCCT: Dummy to simplify porting - returns self"""

    def PresentationManager(self) -> PrsMgr_PresentationManager:
        """
        returns the PresentationManager in which the presentation has been created.
        """

    def SetUpdateStatus(self, theUpdateStatus: bool) -> None: ...

    def MustBeUpdated(self) -> bool: ...

    def Mode(self) -> int:
        """Return display mode index."""

    def Display(self) -> None:
        """Display structure."""

    def Erase(self) -> None:
        """Remove structure."""

    def Highlight(self, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Highlight structure."""

    def Unhighlight(self) -> None:
        """Unhighlight structure."""

    def IsDisplayed(self) -> bool:
        """Return TRUE if structure has been displayed and in no hidden state."""

    def Clear(self, theWithDestruction: bool = True) -> None:
        """
        removes the whole content of the presentation.
        Does not remove the other connected presentations.
        """

    def Compute(self) -> None:
        """Compute structure using presentation manager."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class PrsMgr_PresentableObject(nanoocp.Standard.Standard_Transient):
    """
    A framework to supply the Graphic3d structure of the object to be presented.
    On the first display request, this structure is created by calling the appropriate algorithm and
    retaining this framework for further display. This abstract framework is inherited in
    Application Interactive Services (AIS), notably by AIS_InteractiveObject. Consequently, 3D
    presentation should be handled by the relevant daughter classes and their member functions in
    AIS. This is particularly true in the creation of new interactive objects.

    Key interface methods to be implemented by every Selectable Object:
    - AcceptDisplayMode() accepting display modes implemented by this object;
    - Compute() computing presentation for the given display mode index.

    Warning! Methods managing standard attributes (SetColor(), SetWidth(), SetMaterial()) have
    different meaning for objects of different type (or no meaning at all). Sub-classes might
    override these methods to modify Prs3d_Drawer or class properties providing a convenient
    short-cut depending on application needs. For more sophisticated configuring, Prs3d_Drawer
    should be modified directly, while short-cuts might be left unimplemented.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Presentations(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.PrsMgr.PrsMgr_Presentation]:
        """Return presentations."""

    def ZLayer(self) -> int:
        """Get ID of Z layer for main presentation."""

    def SetZLayer(self, theLayerId: int) -> None:
        """
        Set Z layer ID and update all presentations of the presentable object.
        The layers mechanism allows drawing objects in higher layers in overlay of objects in lower
        layers.
        """

    def IsMutable(self) -> bool:
        """
        Returns true if object has mutable nature (content or location are be changed regularly).
        Mutable object will be managed in different way than static onces (another optimizations).
        """

    def SetMutable(self, theIsMutable: bool) -> None:
        """
        Sets if the object has mutable nature (content or location will be changed regularly).
        This method should be called before object displaying to take effect.
        """

    def ViewAffinity(self) -> nanoocp.Graphic3d.Graphic3d_ViewAffinity:
        """Return view affinity mask."""

    def HasDisplayMode(self) -> bool:
        """
        Returns true if the Interactive Object has display mode setting overriding global setting
        (within Interactive Context).
        """

    def DisplayMode(self) -> int:
        """
        Returns the display mode setting of the Interactive Object.
        The range of supported display mode indexes should be specified within object definition and
        filtered by AccepDisplayMode().
        @sa AcceptDisplayMode()
        """

    def SetDisplayMode(self, theMode: int) -> None:
        """
        Sets the display mode for the interactive object.
        An object can have its own temporary display mode, which is different from that proposed by
        the interactive context.
        @sa AcceptDisplayMode()
        """

    def UnsetDisplayMode(self) -> None:
        """Removes display mode settings from the interactive object."""

    def HasHilightMode(self) -> bool:
        """
        Returns true if the Interactive Object is in highlight mode.
        @sa HilightAttributes()
        """

    def HilightMode(self) -> int:
        """
        Returns highlight display mode.
        This is obsolete method for backward compatibility - use ::HilightAttributes() and
        ::DynamicHilightAttributes() instead.
        @sa HilightAttributes()
        """

    def SetHilightMode(self, theMode: int) -> None:
        """
        Sets highlight display mode.
        This is obsolete method for backward compatibility - use ::HilightAttributes() and
        ::DynamicHilightAttributes() instead.
        @sa HilightAttributes()
        """

    def UnsetHilightMode(self) -> None:
        """
        Unsets highlight display mode.
        @sa HilightAttributes()
        """

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Returns true if the class of objects accepts specified display mode index.
        The interactive context can have a default mode of representation for the set of Interactive
        Objects. This mode may not be accepted by a given class of objects. Consequently, this virtual
        method allowing us to get information about the class in question must be implemented. At
        least one display mode index should be accepted by this method. Although subclass can leave
        default implementation, it is highly desired defining exact list of supported modes instead,
        which is usually an enumeration for one object or objects class sharing similar list of
        display modes.
        """

    def DefaultDisplayMode(self) -> int:
        """Returns the default display mode."""

    @overload
    def ToBeUpdated(self, theToIncludeHidden: bool = False) -> bool:
        """
        Returns TRUE if any active presentation has invalidation flag.
        @param theToIncludeHidden when TRUE, also checks hidden presentations
        """

    @overload
    def ToBeUpdated(self, ListOfMode: nanoocp.NCollection.NCollection_List[int]) -> None:
        """
        Deprecated in OCCT: This method is deprecated - UpdatePresentations() should be called instead

        @name deprecated methods
        gives the list of modes which are flagged "to be updated".
        """

    @overload
    def SetToUpdate(self, theMode: int) -> None:
        """
        Flags presentation to be updated; UpdatePresentations() will recompute these presentations.
        @param theMode presentation (display mode) to invalidate, or -1 to invalidate them all
        """

    @overload
    def SetToUpdate(self) -> None:
        """flags all the Presentations to be Updated."""

    def IsInfinite(self) -> bool:
        """
        Returns true if the interactive object is infinite; FALSE by default.
        This flag affects various operations operating on bounding box of graphic presentations of
        this object. For instance, infinite objects are not taken in account for View FitAll. This
        does not necessarily means that object is actually infinite, auxiliary objects might be also
        marked with this flag to achieve desired behavior.
        """

    def SetInfiniteState(self, theFlag: bool = True) -> None:
        """Sets if object should be considered as infinite."""

    def TypeOfPresentation3d(self) -> PrsMgr_TypeOfPresentation3d:
        """
        Returns information on whether the object accepts display in HLR mode or not.
        """

    def SetTypeOfPresentation(self, theType: PrsMgr_TypeOfPresentation3d) -> None:
        """Set type of presentation."""

    def DisplayStatus(self) -> PrsMgr_DisplayStatus:
        """
        Return presentation display status; PrsMgr_DisplayStatus_None by default.
        """

    def Attributes(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        @name presentation attributes
        Returns the attributes settings.
        """

    def SetAttributes(self, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Initializes the drawing tool theDrawer."""

    def HilightAttributes(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        Returns the hilight attributes settings.
        When not NULL, overrides both Prs3d_TypeOfHighlight_LocalSelected and
        Prs3d_TypeOfHighlight_Selected defined within AIS_InteractiveContext::HighlightStyle().
        @sa AIS_InteractiveContext::HighlightStyle()
        """

    def SetHilightAttributes(self, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Initializes the hilight drawing tool theDrawer."""

    def DynamicHilightAttributes(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        Returns the hilight attributes settings.
        When not NULL, overrides both Prs3d_TypeOfHighlight_LocalDynamic and
        Prs3d_TypeOfHighlight_Dynamic defined within AIS_InteractiveContext::HighlightStyle().
        @sa AIS_InteractiveContext::HighlightStyle()
        """

    def SetDynamicHilightAttributes(self, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Initializes the dynamic hilight drawing tool."""

    def UnsetHilightAttributes(self) -> None:
        """Clears settings provided by the hilight drawing tool theDrawer."""

    def SynchronizeAspects(self) -> None:
        """
        Synchronize presentation aspects after their modification.

        This method should be called after modifying primitive aspect properties (material, texture,
        shader) so that modifications will take effect on already computed presentation groups (thus
        avoiding re-displaying the object).
        """

    def TransformPersistence(self) -> nanoocp.Graphic3d.Graphic3d_TransformPers:
        """
        @name object transformation
        Returns Transformation Persistence defining a special Local Coordinate system where this
        presentable object is located or NULL handle if not defined. Position of the object having
        Transformation Persistence is mutable and depends on camera position. The same applies to a
        bounding box of the object.
        @sa Graphic3d_TransformPers class description
        """

    def SetTransformPersistence(self, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """
        Sets up Transform Persistence defining a special Local Coordinate system where this object
        should be located. Note that management of Transform Persistence object is more expensive than
        of the normal one, because it requires its position being recomputed basing on camera position
        within each draw call / traverse.
        @sa Graphic3d_TransformPers class description
        """

    def LocalTransformationGeom(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """
        Return the local transformation.
        Note that the local transformation of the object having Transformation Persistence
        is applied within Local Coordinate system defined by this Persistence.
        """

    @overload
    def SetLocalTransformation(self, theTrsf: nanoocp.gp.gp_Trsf) -> None: ...

    @overload
    def SetLocalTransformation(self, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """
        Sets local transformation to theTransformation.
        Note that the local transformation of the object having Transformation Persistence
        is applied within Local Coordinate system defined by this Persistence.
        """

    def HasTransformation(self) -> bool:
        """
        Returns true if object has a transformation that is different from the identity.
        """

    def TransformationGeom(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """
        Return the transformation taking into account transformation of parent object(s).
        Note that the local transformation of the object having Transformation Persistence
        is applied within Local Coordinate system defined by this Persistence.
        """

    def LocalTransformation(self) -> nanoocp.gp.gp_Trsf:
        """
        Return the local transformation.
        Note that the local transformation of the object having Transformation Persistence
        is applied within Local Coordinate system defined by this Persistence.
        """

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """
        Return the transformation taking into account transformation of parent object(s).
        Note that the local transformation of the object having Transformation Persistence
        is applied within Local Coordinate system defined by this Persistence.
        """

    def InversedTransformation(self) -> nanoocp.gp.gp_GTrsf:
        """Return inversed transformation."""

    def CombinedParentTransformation(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """Return combined parent transformation."""

    def ResetTransformation(self) -> None:
        """resets local transformation to identity."""

    def UpdateTransformation(self) -> None:
        """
        Updates final transformation (parent + local) of presentable object and its presentations.
        """

    def RecomputeTransformation(self, theProjector: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """
        Calculates object presentation for specific camera position.
        Each of the views in the viewer and every modification such as rotation, for example, entails
        recalculation.
        @param theProjector [in] view orientation
        """

    def ClipPlanes(self) -> nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane:
        """
        @name clipping planes
        Get clip planes.
        @return set of previously added clip planes for all display mode presentations.
        """

    def SetClipPlanes(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None) -> None:
        """
        Set clip planes for graphical clipping for all display mode presentations.
        The composition of clip planes truncates the rendering space to convex volume.
        Please be aware that number of supported clip plane is limited.
        The planes which exceed the limit are ignored.
        Besides of this, some planes can be already set in view where the object is shown:
        the number of these planes should be subtracted from limit to predict the maximum
        possible number of object clipping planes.
        """

    def AddClipPlane(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane | None) -> None:
        """
        Adds clip plane for graphical clipping for all display mode
        presentations. The composition of clip planes truncates the rendering
        space to convex volume. Please be aware that number of supported
        clip plane is limited. The planes which exceed the limit are ignored.
        Besides of this, some planes can be already set in view where the object
        is shown: the number of these planes should be subtracted from limit
        to predict the maximum possible number of object clipping planes.
        @param[in] thePlane  the clip plane to be appended to map of clip planes.
        """

    def RemoveClipPlane(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane | None) -> None:
        """
        Removes previously added clip plane.
        @param[in] thePlane  the clip plane to be removed from map of clip planes.
        """

    def Parent(self) -> PrsMgr_PresentableObject:
        """
        @name parent/children properties
        Returns parent of current object in scene hierarchy.
        """

    def Children(self) -> nanoocp.NCollection.NCollection_List[nanoocp.PrsMgr.PrsMgr_PresentableObject]:
        """Returns children of the current object."""

    def AddChild(self, theObject: PrsMgr_PresentableObject | None) -> None:
        """Makes theObject child of current object in scene hierarchy."""

    def AddChildWithCurrentTransformation(self, theObject: PrsMgr_PresentableObject | None) -> None:
        """
        Makes theObject child of current object in scene hierarchy with keeping the current global
        transformation So the object keeps the same position/orientation in the global CS.
        """

    def RemoveChild(self, theObject: PrsMgr_PresentableObject | None) -> None:
        """Removes theObject from children of current object in scene hierarchy."""

    def RemoveChildWithRestoreTransformation(self, theObject: PrsMgr_PresentableObject | None) -> None:
        """
        Removes theObject from children of current object in scene hierarchy with keeping the current
        global transformation. So the object keeps the same position/orientation in the global CS.
        """

    def HasOwnPresentations(self) -> bool:
        """Returns true if object should have own presentations."""

    def BoundingBox(self, theBndBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Returns bounding box of object correspondingly to its current display mode.
        This method requires presentation to be already computed, since it relies on bounding box of
        presentation structures, which are supposed to be same/close amongst different display modes
        of this object.
        """

    def SetIsoOnTriangulation(self, theIsEnabled: bool) -> None:
        """
        @name simplified presentation properties API
        Enables or disables on-triangulation build of isolines according to the flag given.
        """

    def CurrentFacingModel(self) -> nanoocp.Aspect.Aspect_TypeOfFacingModel:
        """Returns the current facing model which is in effect."""

    def SetCurrentFacingModel(self, theModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None:
        """
        change the current facing model apply on polygons for SetColor(), SetTransparency(),
        SetMaterial() methods default facing model is Aspect_TOFM_TWO_SIDE. This mean that attributes
        is applying both on the front and back face.
        """

    def HasColor(self) -> bool:
        """Returns true if the Interactive Object has color."""

    def Color(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns the color setting of the Interactive Object."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Only the interactive object knowns which Drawer attribute is affected by the color, if any
        (ex: for a wire,it's the wireaspect field of the drawer, but for a vertex, only the point
        aspect field is affected by the color). WARNING : Do not forget to set the corresponding
        fields here (hasOwnColor and myDrawer->SetColor())
        """

    def UnsetColor(self) -> None:
        """
        Removes color settings. Only the Interactive Object
        knows which Drawer attribute is affected by the color
        setting. For a wire, for example, wire aspect is the
        attribute affected. For a vertex, however, only point
        aspect is affected by the color setting.
        """

    def HasWidth(self) -> bool:
        """Returns true if the Interactive Object has width."""

    def Width(self) -> float:
        """Returns the width setting of the Interactive Object."""

    def SetWidth(self, theWidth: float) -> None:
        """
        Allows you to provide the setting aValue for width.
        Only the Interactive Object knows which Drawer attribute is affected by the width setting.
        """

    def UnsetWidth(self) -> None:
        """Reset width to default value."""

    def HasMaterial(self) -> bool:
        """Returns true if the Interactive Object has a setting for material."""

    def Material(self) -> nanoocp.Graphic3d.Graphic3d_NameOfMaterial:
        """Returns the current material setting as enumeration value."""

    def SetMaterial(self, aName: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """
        Sets the material aMat defining this display attribute
        for the interactive object.
        Material aspect determines shading aspect, color and
        transparency of visible entities.
        """

    def UnsetMaterial(self) -> None:
        """Removes the setting for material."""

    def IsTransparent(self) -> bool:
        """Returns true if there is a transparency setting."""

    def Transparency(self) -> float:
        """
        Returns the transparency setting.
        This will be between 0.0 and 1.0.
        At 0.0 an object will be totally opaque, and at 1.0, fully transparent.
        """

    def SetTransparency(self, aValue: float = 0.6) -> None:
        """
        Attributes a setting aValue for transparency.
        The transparency value should be between 0.0 and 1.0.
        At 0.0 an object will be totally opaque, and at 1.0, fully transparent.
        Warning At a value of 1.0, there may be nothing visible.
        """

    def UnsetTransparency(self) -> None:
        """Removes the transparency setting. The object is opaque by default."""

    def HasPolygonOffsets(self) -> bool:
        """Returns true if <myDrawer> has non-null shading aspect"""

    def PolygonOffsets(self) -> tuple[int, float, float]:
        """Retrieves current polygon offsets settings from <myDrawer>."""

    def SetPolygonOffsets(self, aMode: int, aFactor: float = 1.0, aUnits: float = 0.0) -> None:
        """
        Sets up polygon offsets for this object.
        @sa Graphic3d_Aspects::SetPolygonOffsets()
        """

    def UnsetAttributes(self) -> None:
        """Clears settings provided by the drawing tool aDrawer."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def ToPropagateVisualState(self) -> bool:
        """
        Get value of the flag "propagate visual state"
        It means that the display/erase/color visual state is propagated automatically to all
        children; by default, the flag is true
        """

    def SetPropagateVisualState(self, theFlag: bool) -> None:
        """Change the value of the flag "propagate visual state\""""

class PrsMgr_PresentationManager(nanoocp.Standard.Standard_Transient):
    """
    A framework to manage 3D displays, graphic entities and their updates.
    Used in the AIS package (Application Interactive Services), to enable the advanced user to
    define the default display mode of a new interactive object which extends the list of signatures
    and types. Definition of new display types is handled by calling the presentation algorithms
    provided by the StdPrs package.
    """

    @overload
    def __init__(self, theStructureManager: nanoocp.Graphic3d.Graphic3d_StructureManager | None) -> None:
        """
        Creates a framework to manage displays and graphic entities with the 3D view
        theStructureManager.
        """

    @overload
    def __init__(self, theOther: PrsMgr_PresentationManager) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Display(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> None:
        """
        Displays the presentation of the object in the given Presentation manager with the given mode.
        The mode should be enumerated by the object which inherits PresentableObject.
        """

    def Erase(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> None:
        """
        erases the presentation of the object in the given
        Presentation manager with the given mode.
        If @theMode is -1, then erases all presentations of the object.
        """

    def Clear(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> None:
        """
        Clears the presentation of the presentable object thePrsObject in this framework with the
        display mode theMode.
        """

    def SetVisibility(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int, theValue: bool) -> None:
        """Sets the visibility of presentable object."""

    def Unhighlight(self, thePrsObject: PrsMgr_PresentableObject | None) -> None:
        """Removes highlighting from the presentation of the presentable object."""

    def SetDisplayPriority(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int, theNewPrior: nanoocp.Graphic3d.Graphic3d_DisplayPriority) -> None:
        """
        Sets the display priority theNewPrior of the
        presentable object thePrsObject in this framework with the display mode theMode.
        """

    def DisplayPriority(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int) -> nanoocp.Graphic3d.Graphic3d_DisplayPriority:
        """
        Returns the display priority of the presentable object
        thePrsObject in this framework with the display mode theMode.
        """

    def SetZLayer(self, thePrsObject: PrsMgr_PresentableObject | None, theLayerId: int) -> None:
        """Set Z layer ID for all presentations of the object."""

    def GetZLayer(self, thePrsObject: PrsMgr_PresentableObject | None) -> int:
        """
        Get Z layer ID assigned to all presentations of the object.
        Method returns -1 value if object has no presentations and is
        impossible to get layer index.
        """

    def IsDisplayed(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> bool: ...

    def IsHighlighted(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> bool:
        """
        Returns true if the presentation of the presentable
        object thePrsObject in this framework with the display mode theMode is highlighted.
        """

    def Update(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> None:
        """
        Updates the presentation of the presentable object
        thePrsObject in this framework with the display mode theMode.
        """

    def BeginImmediateDraw(self) -> None:
        """
        Resets the transient list of presentations previously displayed in immediate mode
        and begins accumulation of new list by following AddToImmediateList()/Color()/Highlight()
        calls.
        """

    def ClearImmediateDraw(self) -> None:
        """
        Resets the transient list of presentations previously displayed in immediate mode.
        """

    def AddToImmediateList(self, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None) -> None:
        """
        Stores thePrs in the transient list of presentations to be displayed in immediate mode.
        Will be taken in account in EndImmediateDraw method.
        """

    def EndImmediateDraw(self, theViewer: nanoocp.V3d.V3d_Viewer | None) -> None:
        """
        Allows rapid drawing of the each view in theViewer by avoiding an update of the whole
        background.
        """

    def RedrawImmediate(self, theViewer: nanoocp.V3d.V3d_Viewer | None) -> None:
        """
        Clears and redisplays immediate structures of the viewer taking into account its affinity.
        """

    def IsImmediateModeOn(self) -> bool:
        """
        Returns true if Presentation Manager is accumulating transient list of presentations to be
        displayed in immediate mode.
        """

    def Color(self, thePrsObject: PrsMgr_PresentableObject | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int = 0, theSelObj: PrsMgr_PresentableObject | None = None, theImmediateStructLayerId: int = -3) -> None:
        """
        Highlights the graphic object thePrsObject in the color theColor.
        thePrsObject has the display mode theMode;
        this has the default value of 0, that is, the wireframe display mode.
        """

    def Connect(self, thePrsObject: PrsMgr_PresentableObject | None, theOtherObject: PrsMgr_PresentableObject | None, theMode: int = 0, theOtherMode: int = 0) -> None: ...

    def Transform(self, thePrsObject: PrsMgr_PresentableObject | None, theTransformation: nanoocp.TopLoc.TopLoc_Datum3D | None, theMode: int = 0) -> None:
        """
        Sets the transformation theTransformation for the presentable object thePrsObject.
        thePrsObject has the display mode theMode; this has the default value of 0, that is, the
        wireframe display mode.
        """

    def StructureManager(self) -> nanoocp.Graphic3d.Graphic3d_StructureManager:
        """Returns the structure manager."""

    def HasPresentation(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0) -> bool:
        """
        Returns true if there is a presentation of the
        presentable object thePrsObject in this framework, thePrsObject having the display mode
        theMode.
        """

    def Presentation(self, thePrsObject: PrsMgr_PresentableObject | None, theMode: int = 0, theToCreate: bool = False, theSelObj: PrsMgr_PresentableObject | None = None) -> PrsMgr_Presentation:
        """
        Returns the presentation Presentation of the presentable object thePrsObject in this
        framework. When theToCreate is true - automatically creates presentation for specified mode
        when not exist. Optional argument theSelObj specifies parent decomposed object to inherit its
        view affinity.
        """

    def UpdateHighlightTrsf(self, theViewer: nanoocp.V3d.V3d_Viewer | None, theObj: PrsMgr_PresentableObject | None, theMode: int = 0, theSelObj: PrsMgr_PresentableObject | None = None) -> None:
        """
        Allows to apply location transformation to shadow highlight presentation immediately.
        @param theObj defines the base object, it local transformation will be applied to
        corresponding highlight structure
        @param theMode defines display mode of the base object
        @param theSelObj defines the object produced after decomposition of the base object for local
        selection
        """

# C++ typedef aliases
Prs3d_Presentation = nanoocp.Graphic3d.Graphic3d_Structure
