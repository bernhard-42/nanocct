"""OCCT package AIS (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Aspect
import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.Font
import nanoocp.Geom
import nanoocp.Graphic3d
import nanoocp.Image
import nanoocp.Media
from nanoocp.Media import Media_Timer as AIS_AnimationTimer
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Prs3d
import nanoocp.PrsMgr
from nanoocp.PrsMgr import PrsMgr_DisplayStatus as AIS_DisplayStatus
import nanoocp.Quantity
import nanoocp.Select3D
import nanoocp.SelectBasics
import nanoocp.SelectMgr
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopLoc
import nanoocp.TopoDS
import nanoocp.V3d
import nanoocp.WNT
import nanoocp.gp


class AIS_KindOfInteractive(enum.IntEnum):
    """
    Declares the type of Interactive Object.
    This type can be used for fast pre-filtering of objects of specific group.
    """

    AIS_KindOfInteractive_None = 0

    AIS_KindOfInteractive_Datum = 1

    AIS_KindOfInteractive_Shape = 2

    AIS_KindOfInteractive_Object = 3

    AIS_KindOfInteractive_Relation = 4

    AIS_KindOfInteractive_Dimension = 5

    AIS_KindOfInteractive_LightSource = 6

    AIS_KOI_None = 0

    AIS_KOI_Datum = 1

    AIS_KOI_Shape = 2

    AIS_KOI_Object = 3

    AIS_KOI_Relation = 4

    AIS_KOI_Dimension = 5

AIS_KindOfInteractive_None: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KindOfInteractive_None

AIS_KindOfInteractive_Datum: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KindOfInteractive_Datum

AIS_KindOfInteractive_Shape: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KindOfInteractive_Shape

AIS_KindOfInteractive_Object: AIS_KindOfInteractive = ...

AIS_KindOfInteractive_Relation: AIS_KindOfInteractive = ...

AIS_KindOfInteractive_Dimension: AIS_KindOfInteractive = ...

AIS_KindOfInteractive_LightSource: AIS_KindOfInteractive = ...

AIS_KOI_None: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_None

AIS_KOI_Datum: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_Datum

AIS_KOI_Shape: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_Shape

AIS_KOI_Object: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_Object

AIS_KOI_Relation: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_Relation

AIS_KOI_Dimension: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KOI_Dimension

class AIS_DragAction(enum.IntEnum):
    """Dragging action."""

    AIS_DragAction_Start = 0

    AIS_DragAction_Confirmed = 1

    AIS_DragAction_Update = 2

    AIS_DragAction_Stop = 3

    AIS_DragAction_Abort = 4

AIS_DragAction_Start: AIS_DragAction = AIS_DragAction.AIS_DragAction_Start

AIS_DragAction_Confirmed: AIS_DragAction = AIS_DragAction.AIS_DragAction_Confirmed

AIS_DragAction_Update: AIS_DragAction = AIS_DragAction.AIS_DragAction_Update

AIS_DragAction_Stop: AIS_DragAction = AIS_DragAction.AIS_DragAction_Stop

AIS_DragAction_Abort: AIS_DragAction = AIS_DragAction.AIS_DragAction_Abort

class AIS_DisplayMode(enum.IntEnum):
    """
    Sets display modes other than neutral point ones,
    for interactive objects. The possibilities include:
    -   wireframe,
    -   shaded,
    """

    AIS_WireFrame = 0

    AIS_Shaded = 1

AIS_WireFrame: AIS_DisplayMode = AIS_DisplayMode.AIS_WireFrame

AIS_Shaded: AIS_DisplayMode = AIS_DisplayMode.AIS_Shaded

class AIS_SelectionScheme(enum.IntEnum):
    """Sets selection schemes for interactive contexts."""

    AIS_SelectionScheme_UNKNOWN = -1

    AIS_SelectionScheme_Replace = 0

    AIS_SelectionScheme_Add = 1

    AIS_SelectionScheme_Remove = 2

    AIS_SelectionScheme_XOR = 3

    AIS_SelectionScheme_Clear = 4

    AIS_SelectionScheme_ReplaceExtra = 5

AIS_SelectionScheme_UNKNOWN: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_UNKNOWN

AIS_SelectionScheme_Replace: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace

AIS_SelectionScheme_Add: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Add

AIS_SelectionScheme_Remove: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Remove

AIS_SelectionScheme_XOR: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_XOR

AIS_SelectionScheme_Clear: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Clear

AIS_SelectionScheme_ReplaceExtra: AIS_SelectionScheme = ...

class AIS_SelectStatus(enum.IntEnum):
    AIS_SS_Added = 0

    AIS_SS_Removed = 1

    AIS_SS_NotDone = 2

AIS_SS_Added: AIS_SelectStatus = AIS_SelectStatus.AIS_SS_Added

AIS_SS_Removed: AIS_SelectStatus = AIS_SelectStatus.AIS_SS_Removed

AIS_SS_NotDone: AIS_SelectStatus = AIS_SelectStatus.AIS_SS_NotDone

class AIS_SelectionModesConcurrency(enum.IntEnum):
    """
    The mode specifying how multiple active Selection Modes should be treated during activation of
    new one.
    """

    AIS_SelectionModesConcurrency_Single = 0

    AIS_SelectionModesConcurrency_GlobalOrLocal = 1

    AIS_SelectionModesConcurrency_Multiple = 2

AIS_SelectionModesConcurrency_Single: AIS_SelectionModesConcurrency = ...

AIS_SelectionModesConcurrency_GlobalOrLocal: AIS_SelectionModesConcurrency = ...

AIS_SelectionModesConcurrency_Multiple: AIS_SelectionModesConcurrency = ...

class AIS_StatusOfDetection(enum.IntEnum):
    AIS_SOD_Error = 0

    AIS_SOD_Nothing = 1

    AIS_SOD_AllBad = 2

    AIS_SOD_Selected = 3

    AIS_SOD_OnlyOneDetected = 4

    AIS_SOD_OnlyOneGood = 5

    AIS_SOD_SeveralGood = 6

AIS_SOD_Error: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_Error

AIS_SOD_Nothing: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_Nothing

AIS_SOD_AllBad: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_AllBad

AIS_SOD_Selected: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_Selected

AIS_SOD_OnlyOneDetected: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_OnlyOneDetected

AIS_SOD_OnlyOneGood: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_OnlyOneGood

AIS_SOD_SeveralGood: AIS_StatusOfDetection = AIS_StatusOfDetection.AIS_SOD_SeveralGood

class AIS_StatusOfPick(enum.IntEnum):
    AIS_SOP_Error = 0

    AIS_SOP_NothingSelected = 1

    AIS_SOP_Removed = 2

    AIS_SOP_OneSelected = 3

    AIS_SOP_SeveralSelected = 4

AIS_SOP_Error: AIS_StatusOfPick = AIS_StatusOfPick.AIS_SOP_Error

AIS_SOP_NothingSelected: AIS_StatusOfPick = AIS_StatusOfPick.AIS_SOP_NothingSelected

AIS_SOP_Removed: AIS_StatusOfPick = AIS_StatusOfPick.AIS_SOP_Removed

AIS_SOP_OneSelected: AIS_StatusOfPick = AIS_StatusOfPick.AIS_SOP_OneSelected

AIS_SOP_SeveralSelected: AIS_StatusOfPick = AIS_StatusOfPick.AIS_SOP_SeveralSelected

class AIS_TypeOfIso(enum.IntEnum):
    """Declares the type of isoparameter displayed."""

    AIS_TOI_IsoU = 0

    AIS_TOI_IsoV = 1

    AIS_TOI_Both = 2

AIS_TOI_IsoU: AIS_TypeOfIso = AIS_TypeOfIso.AIS_TOI_IsoU

AIS_TOI_IsoV: AIS_TypeOfIso = AIS_TypeOfIso.AIS_TOI_IsoV

AIS_TOI_Both: AIS_TypeOfIso = AIS_TypeOfIso.AIS_TOI_Both

class AIS_TypeOfAxis(enum.IntEnum):
    """Declares the type of axis."""

    AIS_TOAX_Unknown = 0

    AIS_TOAX_XAxis = 1

    AIS_TOAX_YAxis = 2

    AIS_TOAX_ZAxis = 3

AIS_TOAX_Unknown: AIS_TypeOfAxis = AIS_TypeOfAxis.AIS_TOAX_Unknown

AIS_TOAX_XAxis: AIS_TypeOfAxis = AIS_TypeOfAxis.AIS_TOAX_XAxis

AIS_TOAX_YAxis: AIS_TypeOfAxis = AIS_TypeOfAxis.AIS_TOAX_YAxis

AIS_TOAX_ZAxis: AIS_TypeOfAxis = AIS_TypeOfAxis.AIS_TOAX_ZAxis

class AIS_TypeOfAttribute(enum.IntEnum):
    AIS_TOA_Line = 0

    AIS_TOA_Dimension = 1

    AIS_TOA_Wire = 2

    AIS_TOA_Plane = 3

    AIS_TOA_Vector = 4

    AIS_TOA_UIso = 5

    AIS_TOA_VIso = 6

    AIS_TOA_Free = 7

    AIS_TOA_UnFree = 8

    AIS_TOA_Section = 9

    AIS_TOA_Hidden = 10

    AIS_TOA_Seen = 11

    AIS_TOA_FaceBoundary = 12

    AIS_TOA_FirstAxis = 13

    AIS_TOA_SecondAxis = 14

    AIS_TOA_ThirdAxis = 15

AIS_TOA_Line: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Line

AIS_TOA_Dimension: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Dimension

AIS_TOA_Wire: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Wire

AIS_TOA_Plane: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Plane

AIS_TOA_Vector: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Vector

AIS_TOA_UIso: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_UIso

AIS_TOA_VIso: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_VIso

AIS_TOA_Free: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Free

AIS_TOA_UnFree: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_UnFree

AIS_TOA_Section: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Section

AIS_TOA_Hidden: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Hidden

AIS_TOA_Seen: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_Seen

AIS_TOA_FaceBoundary: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_FaceBoundary

AIS_TOA_FirstAxis: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_FirstAxis

AIS_TOA_SecondAxis: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_SecondAxis

AIS_TOA_ThirdAxis: AIS_TypeOfAttribute = AIS_TypeOfAttribute.AIS_TOA_ThirdAxis

class AIS_ManipulatorMode(enum.IntEnum):
    """
    Mode to make definite kind of transformations with AIS_Manipulator object.
    """

    AIS_MM_None = 0

    AIS_MM_Translation = 1

    AIS_MM_Rotation = 2

    AIS_MM_Scaling = 3

    AIS_MM_TranslationPlane = 4

AIS_MM_None: AIS_ManipulatorMode = AIS_ManipulatorMode.AIS_MM_None

AIS_MM_Translation: AIS_ManipulatorMode = AIS_ManipulatorMode.AIS_MM_Translation

AIS_MM_Rotation: AIS_ManipulatorMode = AIS_ManipulatorMode.AIS_MM_Rotation

AIS_MM_Scaling: AIS_ManipulatorMode = AIS_ManipulatorMode.AIS_MM_Scaling

AIS_MM_TranslationPlane: AIS_ManipulatorMode = AIS_ManipulatorMode.AIS_MM_TranslationPlane

class AIS_MouseGesture(enum.IntEnum):
    """Mouse gesture - only one can be active at one moment."""

    AIS_MouseGesture_NONE = 0

    AIS_MouseGesture_SelectRectangle = 1

    AIS_MouseGesture_SelectLasso = 2

    AIS_MouseGesture_Zoom = 3

    AIS_MouseGesture_ZoomVertical = 4

    AIS_MouseGesture_ZoomWindow = 5

    AIS_MouseGesture_Pan = 6

    AIS_MouseGesture_RotateOrbit = 7

    AIS_MouseGesture_RotateView = 8

    AIS_MouseGesture_Drag = 9

AIS_MouseGesture_NONE: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_NONE

AIS_MouseGesture_SelectRectangle: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_SelectRectangle

AIS_MouseGesture_SelectLasso: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_SelectLasso

AIS_MouseGesture_Zoom: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_Zoom

AIS_MouseGesture_ZoomVertical: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_ZoomVertical

AIS_MouseGesture_ZoomWindow: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_ZoomWindow

AIS_MouseGesture_Pan: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_Pan

AIS_MouseGesture_RotateOrbit: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_RotateOrbit

AIS_MouseGesture_RotateView: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_RotateView

AIS_MouseGesture_Drag: AIS_MouseGesture = AIS_MouseGesture.AIS_MouseGesture_Drag

class AIS_NavigationMode(enum.IntEnum):
    """Camera navigation mode."""

    AIS_NavigationMode_Orbit = 0

    AIS_NavigationMode_FirstPersonFlight = 1

    AIS_NavigationMode_FirstPersonWalk = 2

AIS_NavigationMode_Orbit: AIS_NavigationMode = AIS_NavigationMode.AIS_NavigationMode_Orbit

AIS_NavigationMode_FirstPersonFlight: AIS_NavigationMode = ...

AIS_NavigationMode_FirstPersonWalk: AIS_NavigationMode = ...

AIS_NavigationMode_LOWER: int = 0

AIS_NavigationMode_UPPER: int = 2

class AIS_TypeOfPlane(enum.IntEnum):
    """Declares the type of plane."""

    AIS_TOPL_Unknown = 0

    AIS_TOPL_XYPlane = 1

    AIS_TOPL_XZPlane = 2

    AIS_TOPL_YZPlane = 3

AIS_TOPL_Unknown: AIS_TypeOfPlane = AIS_TypeOfPlane.AIS_TOPL_Unknown

AIS_TOPL_XYPlane: AIS_TypeOfPlane = AIS_TypeOfPlane.AIS_TOPL_XYPlane

AIS_TOPL_XZPlane: AIS_TypeOfPlane = AIS_TypeOfPlane.AIS_TOPL_XZPlane

AIS_TOPL_YZPlane: AIS_TypeOfPlane = AIS_TypeOfPlane.AIS_TOPL_YZPlane

class AIS_RotationMode(enum.IntEnum):
    """Camera rotation mode."""

    AIS_RotationMode_BndBoxActive = 0

    AIS_RotationMode_PickLast = 1

    AIS_RotationMode_PickCenter = 2

    AIS_RotationMode_CameraAt = 3

    AIS_RotationMode_BndBoxScene = 4

AIS_RotationMode_BndBoxActive: AIS_RotationMode = AIS_RotationMode.AIS_RotationMode_BndBoxActive

AIS_RotationMode_PickLast: AIS_RotationMode = AIS_RotationMode.AIS_RotationMode_PickLast

AIS_RotationMode_PickCenter: AIS_RotationMode = AIS_RotationMode.AIS_RotationMode_PickCenter

AIS_RotationMode_CameraAt: AIS_RotationMode = AIS_RotationMode.AIS_RotationMode_CameraAt

AIS_RotationMode_BndBoxScene: AIS_RotationMode = AIS_RotationMode.AIS_RotationMode_BndBoxScene

AIS_RotationMode_LOWER: int = 0

AIS_RotationMode_UPPER: int = 4

class AIS_TrihedronSelectionMode(enum.IntEnum):
    """Enumeration defining selection modes supported by AIS_Trihedron."""

    AIS_TrihedronSelectionMode_EntireObject = 0

    AIS_TrihedronSelectionMode_Origin = 1

    AIS_TrihedronSelectionMode_Axes = 2

    AIS_TrihedronSelectionMode_MainPlanes = 3

AIS_TrihedronSelectionMode_EntireObject: AIS_TrihedronSelectionMode = ...

AIS_TrihedronSelectionMode_Origin: AIS_TrihedronSelectionMode = ...

AIS_TrihedronSelectionMode_Axes: AIS_TrihedronSelectionMode = ...

AIS_TrihedronSelectionMode_MainPlanes: AIS_TrihedronSelectionMode = ...

class AIS_ViewSelectionTool(enum.IntEnum):
    """Selection mode"""

    AIS_ViewSelectionTool_Picking = 0

    AIS_ViewSelectionTool_RubberBand = 1

    AIS_ViewSelectionTool_Polygon = 2

    AIS_ViewSelectionTool_ZoomWindow = 3

AIS_ViewSelectionTool_Picking: AIS_ViewSelectionTool = ...

AIS_ViewSelectionTool_RubberBand: AIS_ViewSelectionTool = ...

AIS_ViewSelectionTool_Polygon: AIS_ViewSelectionTool = ...

AIS_ViewSelectionTool_ZoomWindow: AIS_ViewSelectionTool = ...

class AIS_ViewInputBufferType(enum.IntEnum):
    """Input buffer type."""

    AIS_ViewInputBufferType_UI = 0

    AIS_ViewInputBufferType_GL = 1

AIS_ViewInputBufferType_UI: AIS_ViewInputBufferType = ...

AIS_ViewInputBufferType_GL: AIS_ViewInputBufferType = ...

class AIS_WalkTranslation(enum.IntEnum):
    """Walking translation components."""

    AIS_WalkTranslation_Forward = 0

    AIS_WalkTranslation_Side = 1

    AIS_WalkTranslation_Up = 2

AIS_WalkTranslation_Forward: AIS_WalkTranslation = AIS_WalkTranslation.AIS_WalkTranslation_Forward

AIS_WalkTranslation_Side: AIS_WalkTranslation = AIS_WalkTranslation.AIS_WalkTranslation_Side

AIS_WalkTranslation_Up: AIS_WalkTranslation = AIS_WalkTranslation.AIS_WalkTranslation_Up

class AIS_WalkRotation(enum.IntEnum):
    """Walking rotation components."""

    AIS_WalkRotation_Yaw = 0

    AIS_WalkRotation_Pitch = 1

    AIS_WalkRotation_Roll = 2

AIS_WalkRotation_Yaw: AIS_WalkRotation = AIS_WalkRotation.AIS_WalkRotation_Yaw

AIS_WalkRotation_Pitch: AIS_WalkRotation = AIS_WalkRotation.AIS_WalkRotation_Pitch

AIS_WalkRotation_Roll: AIS_WalkRotation = AIS_WalkRotation.AIS_WalkRotation_Roll

class AIS:
    """
    Application Interactive Services provide the means to create links between an application GUI
    viewer and the packages which are used to manage selection and presentation. The tools AIS
    defined in order to do this include different sorts of entities: both the selectable viewable
    objects themselves and the context and attribute managers to define their selection and display.
    To orient the user as he works in a modeling environment, views and selections must be
    comprehensible. There must be several different sorts of selectable and viewable object defined.
    These must also be interactive, that is, connecting graphic representation and the underlying
    reference geometry. These entities are called Interactive Objects, and are divided into four
    types:
    -   the Datum
    -   the Relation
    -   the Object
    -   None.
    The Datum groups together the construction elements such as lines, circles, points, trihedra,
    plane trihedra, planes and axes. The Relation is made up of constraints on one or more
    interactive shapes and the corresponding reference geometry. For example, you might want to
    constrain two edges in a parallel relation. This constraint is considered as an object in its
    own right, and is shown as a sensitive primitive. This takes the graphic form of a perpendicular
    arrow marked with the || symbol and lying between the two edges. The Object type includes
    topological shapes, and connections between shapes. None, in order not to eliminate the object,
    tells the application to look further until it finds an object definition in its generation
    which is accepted. Inside these categories, you have the possibility of an additional
    characterization by means of a signature. The signature provides an index to the further
    characterization. By default, the Interactive Object has a None type and a signature of 0
    (equivalent to None.) If you want to give a particular type and signature to your interactive
    object, you must redefine the two virtual methods: Type and Signature. In the C++ inheritance
    structure of the package, each class representing a specific Interactive Object inherits
    AIS_InteractiveObject. Among these inheriting classes, PrsDim_Relation functions as the abstract
    mother class for tinheriting classes defining display of specific relational constraints and
    types of dimension. Some of these include:
    -   display of constraints based on relations of symmetry, tangency, parallelism and
    concentricity
    -   display of dimensions for angles, offsets, diameters, radii and chamfers.
    No viewer can show everything at once with any coherence or clarity.
    Views must be managed carefully both sequentially and at any given instant.
    Another function of the view is that of a context to carry out design in.
    The design changes are applied to the objects in the view and then extended to the underlying
    reference geometry by a solver. To make sense of this complicated visual data, several display
    and selection tools are required. To facilitate management, each object and each construction
    element has a selection priority. There are also means to modify the default priority. To define
    an environment of dynamic detection, you can use standard filter classes or create your own. A
    filter questions the owner of the sensitive primitive to determine if it has the desired
    qualities. If it answers positively, it is kept. If not, it is rejected. The standard filters
    supplied in AIS include:
    - AIS_AttributeFilter
    - AIS_SignatureFilter
    - AIS_TypeFilter.
    A set of functions allows you to choose the interactive objects which you want to act on, the
    selection modes which you want to activate. An interactive object can have a certain number of
    graphic attributes which are specific to it, such as visualization mode, color, and material. By
    the same token, the interactive context has a set of graphic attributes, the Drawer which is
    valid by default for the objects it controls. When an interactive object is visualized, the
    required graphic attributes are first taken from the object's own Drawer if one exists, or from
    the context drawer for the others.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AIS) -> None: ...

class AIS_AnimationProgress:
    """Structure defining current animation progress."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AIS_AnimationProgress) -> None: ...

    @property
    def Pts(self) -> float:
        """global presentation timestamp"""

    @Pts.setter
    def Pts(self, arg: float, /) -> None: ...

    @property
    def LocalPts(self) -> float:
        """presentation within current animation"""

    @LocalPts.setter
    def LocalPts(self, arg: float, /) -> None: ...

    @property
    def LocalNormalized(self) -> float:
        """normalized position within current animation within 0..1 range"""

    @LocalNormalized.setter
    def LocalNormalized(self, arg: float, /) -> None: ...

class AIS_Animation(nanoocp.Standard.Standard_Transient):
    """
    Class represents a basic animation class.
    AIS_Animation can be used as:

    - Animation Implementor
    Sub-classes should override method AIS_Animation::update() to perform specific animation.
    AIS package provides limited number of such animation atoms - classes AIS_AnimationObject and
    AIS_AnimationCamera, which could be enough for defining a simple animation. In general case,
    application is expected defining own AIS_Animation sub-classes implementing
    application-specific animation logic (e.g. another interpolation or another kind of
    transformations - like color transition and others). The basic conception of
    AIS_Animation::update() is defining an exact scene state for the current presentation
    timestamp, providing a smooth and continuous animation well defined at any time step and in
    any direction. So that a time difference between two sequential drawn Viewer frames can vary
    from frame to frame without visual artifacts, increasing rendering framerate would not lead to
    animation being executed too fast and low framerate (on slow hardware) would not lead to
    animation played longer than defined duration. Hence, implementation should avoid usage of
    incremental step logic or should apply it very carefully.

    - Animation Container
    AIS_Animation (no sub-classing) can be used to aggregate a sequence of Animation items
    (children). Each children should be defined with its own duration and start time (presentation
    timestamp). It is possible defining collection of nested AIS_Animation items, so that within
    each container level children define start playback time relative to its holder.

    - Animation playback Controller
    It is suggested that application would define a single AIS_Animation instance (optional
    sub-classing) for controlling animation playback as whole. Such controller should be filled in
    by other AIS_Animation as children objects, and will be managed by application by calling
    StartTimer(), UpdateTimer() and IsStopped() methods.

    Note, that AIS_Animation::StartTimer() defines a timer calculating an elapsed time, not a
    multimedia timer executing Viewer updates at specific intervals! Application should avoid using
    implicit and immediate Viewer updates to ensure that AIS_Animation::UpdateTimer() is called
    before each redrawing of a Viewer content. Redrawing logic should be also managed at application
    level for managing a smooth animation (by defining a multimedia timer provided by used GUI
    framework executing updates at desired framerate, or as continuous redraws in loop).
    """

    @overload
    def __init__(self, theAnimationName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates empty animation."""

    @overload
    def __init__(self, theOther: AIS_Animation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Animation name."""

    def StartPts(self) -> float:
        """@return start time of the animation in the timeline"""

    def SetStartPts(self, thePtsStart: float) -> None:
        """Sets time limits for animation in the animation timeline"""

    def Duration(self) -> float:
        """@return duration of the animation in the timeline"""

    def UpdateTotalDuration(self) -> None:
        """Update total duration considering all animations on timeline."""

    def HasOwnDuration(self) -> bool:
        """Return true if duration is defined."""

    def OwnDuration(self) -> float:
        """@return own duration of the animation in the timeline"""

    def SetOwnDuration(self, theDuration: float) -> None:
        """Defines duration of the animation."""

    def Add(self, theAnimation: AIS_Animation | None) -> None:
        """
        Add single animation to the timeline.
        @param theAnimation input animation
        """

    def Clear(self) -> None:
        """Clear animation timeline - remove all animations from it."""

    def Find(self, theAnimationName: nanoocp.TCollection.TCollection_AsciiString) -> AIS_Animation:
        """Return the child animation with the given name."""

    def Remove(self, theAnimation: AIS_Animation | None) -> bool:
        """Remove the child animation."""

    def Replace(self, theAnimationOld: AIS_Animation | None, theAnimationNew: AIS_Animation | None) -> bool:
        """Replace the child animation."""

    def CopyFrom(self, theOther: AIS_Animation | None) -> None:
        """
        Clears own children and then copy child animations from another object.
        Copy also Start Time and Duration values.
        """

    def Children(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.AIS.AIS_Animation]:
        """Return sequence of child animations."""

    def StartTimer(self, theStartPts: float, thePlaySpeed: float, theToUpdate: bool, theToStopTimer: bool = False) -> None:
        """
        Start animation with internally defined timer instance.
        Calls ::Start() internally.

        Note, that this method initializes a timer calculating an elapsed time (presentation
        timestamps within AIS_Animation::UpdateTimer()), not a multimedia timer executing Viewer
        updates at specific intervals! Viewer redrawing should be managed at application level, so
        that AIS_Animation::UpdateTimer() is called once right before each redrawing of a Viewer
        content.

        @param theStartPts    starting timer position (presentation timestamp)
        @param thePlaySpeed   playback speed (1.0 means normal speed)
        @param theToUpdate    flag to update defined animations to specified start position
        @param theToStopTimer flag to pause timer at the starting position
        """

    def UpdateTimer(self) -> float:
        """
        Update single frame of animation, update timer state
        @return current time of timeline progress.
        """

    def ElapsedTime(self) -> float:
        """Return elapsed time."""

    def Timer(self) -> nanoocp.Media.Media_Timer:
        """Return playback timer."""

    def SetTimer(self, theTimer: nanoocp.Media.Media_Timer | None) -> None:
        """Set playback timer."""

    def Start(self, theToUpdate: bool) -> None:
        """
        Start animation. This method changes status of the animation to Started.
        This status defines whether animation is to be performed in the timeline or not.
        @param theToUpdate call Update() method
        """

    def Pause(self) -> None:
        """Pause the process timeline."""

    def Stop(self) -> None:
        """
        Stop animation. This method changed status of the animation to Stopped.
        This status shows that animation will not be performed in the timeline or it is finished.
        """

    def IsStopped(self) -> bool:
        """
        Check if animation is to be performed in the animation timeline.
        @return True if it is stopped of finished.
        """

    def Update(self, thePts: float) -> bool:
        """
        Update single frame of animation, update timer state
        @param[in] thePts  the time moment within [0; Duration()]
        @return True if timeline is in progress
        """

class AIS_InteractiveObject(nanoocp.SelectMgr.SelectMgr_SelectableObject):
    """
    Defines a class of objects with display and selection services.
    Entities which are visualized and selected are Interactive Objects.
    Specific attributes of entities such as arrow aspect for dimensions must be loaded in a
    Prs3d_Drawer.

    You can make use of classes of standard Interactive Objects for which all necessary methods have
    already been programmed, or you can implement your own classes of Interactive Objects. Key
    interface methods to be implemented by every Interactive Object:
    * Presentable Object (PrsMgr_PresentableObject)
    Consider defining an enumeration of supported Display Mode indexes for particular Interactive
    Object or class of Interactive Objects.
    - AcceptDisplayMode() accepting display modes implemented by this object;
    - Compute() computing presentation for the given display mode index;
    * Selectable Object (SelectMgr_SelectableObject)
    Consider defining an enumeration of supported Selection Mode indexes for particular
    Interactive Object or class of Interactive Objects.
    - ComputeSelection() computing selectable entities for the given selection mode index.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Type(self) -> AIS_KindOfInteractive:
        """
        Returns the kind of Interactive Object; AIS_KindOfInteractive_None by default.
        """

    def Signature(self) -> int:
        """
        Specifies additional characteristics of Interactive Object of Type(); -1 by default.
        Among the datums, this signature is attributed to the shape.
        The remaining datums have the following default signatures:
        - Point          signature 1
        - Axis           signature 2
        - Trihedron      signature 3
        - PlaneTrihedron signature 4
        - Line           signature 5
        - Circle         signature 6
        - Plane          signature 7.
        """

    def Redisplay(self, AllModes: bool = False) -> None:
        """
        Updates the active presentation; if <AllModes> = true
        all the presentations inside are recomputed.
        IMPORTANT: It is preferable to call Redisplay method of
        corresponding AIS_InteractiveContext instance for cases when it
        is accessible. This method just redirects call to myCTXPtr,
        so this class field must be up to date for proper result.
        """

    def HasInteractiveContext(self) -> bool:
        """
        Indicates whether the Interactive Object has a pointer to an interactive context.
        """

    def InteractiveContext(self) -> AIS_InteractiveContext:
        """Returns the context pointer to the interactive context."""

    def SetContext(self, aCtx: AIS_InteractiveContext | None) -> None:
        """
        Sets the interactive context aCtx and provides a link
        to the default drawing tool or "Drawer" if there is none.
        """

    def HasOwner(self) -> bool:
        """
        Returns true if the object has an owner attributed to it.
        The owner can be a shape for a set of sub-shapes or a sub-shape for sub-shapes which it is
        composed of, and takes the form of a transient.
        """

    def GetOwner(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the owner of the Interactive Object.
        The owner can be a shape for a set of sub-shapes or
        a sub-shape for sub-shapes which it is composed of,
        and takes the form of a transient.
        There are two types of owners:
        -   Direct owners, decomposition shapes such as
        edges, wires, and faces.
        -   Users, presentable objects connecting to sensitive
        primitives, or a shape which has been decomposed.
        """

    def SetOwner(self, theApplicativeEntity: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Allows you to attribute the owner theApplicativeEntity to
        an Interactive Object. This can be a shape for a set of
        sub-shapes or a sub-shape for sub-shapes which it
        is composed of. The owner takes the form of a transient.
        """

    def ClearOwner(self) -> None:
        """
        Each Interactive Object has methods which allow us to attribute an Owner to it in the form of
        a Transient. This method removes the owner from the graphic entity.
        """

    def ProcessDragging(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theDragFrom: nanoocp.BVH.BVH_Vec2i, theDragTo: nanoocp.BVH.BVH_Vec2i, theAction: AIS_DragAction) -> bool:
        """
        Drag object in the viewer.
        @param[in] theCtx       interactive context
        @param[in] theView      active View
        @param[in] theOwner     the owner of detected entity
        @param[in] theDragFrom  drag start point
        @param[in] theDragTo    drag end point
        @param[in] theAction    drag action
        @return FALSE if object rejects dragging action (e.g. AIS_DragAction_Start)
        """

    def GetContext(self) -> AIS_InteractiveContext:
        """Returns the context pointer to the interactive context."""

    def HasPresentation(self) -> bool:
        """
        Returns TRUE when this object has a presentation in the current DisplayMode()
        """

    def Presentation(self) -> nanoocp.Graphic3d.Graphic3d_Structure:
        """
        Returns the current presentation of this object according to the current DisplayMode()
        """

    def SetAspect(self, anAspect: nanoocp.Prs3d.Prs3d_BasicAspect | None) -> None:
        """
        Deprecated in OCCT: Deprecated method, results might be undefined

        Sets the graphic basic aspect to the current presentation.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class AIS_GlobalStatus(nanoocp.Standard.Standard_Transient):
    """Stores information about objects in graphic context:"""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: AIS_GlobalStatus) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DisplayMode(self) -> int:
        """Returns the display mode."""

    def SetDisplayMode(self, theMode: int) -> None:
        """Sets display mode."""

    def IsHilighted(self) -> bool:
        """Returns TRUE if object is highlighted"""

    def SetHilightStatus(self, theStatus: bool) -> None:
        """Sets highlighted state."""

    def SetHilightStyle(self, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Changes applied highlight style for a particular object"""

    def HilightStyle(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """Returns applied highlight style for a particular object"""

    def SelectionModes(self) -> nanoocp.NCollection.NCollection_List[int]:
        """Returns active selection modes of the object."""

    def IsSModeIn(self, theMode: int) -> bool:
        """Return TRUE if selection mode was registered."""

    def AddSelectionMode(self, theMode: int) -> bool:
        """Add selection mode."""

    def RemoveSelectionMode(self, theMode: int) -> bool:
        """Remove selection mode."""

    def ClearSelectionModes(self) -> None:
        """Remove all selection modes."""

    def IsSubIntensityOn(self) -> bool: ...

    def SetSubIntensity(self, theIsOn: bool) -> None: ...

class AIS_Selection(nanoocp.Standard.Standard_Transient):
    """Class holding the list of selected owners."""

    @overload
    def __init__(self) -> None:
        """creates a new selection."""

    @overload
    def __init__(self, theOther: AIS_Selection) -> None: ...

    def __iter__(self) -> AIS_Selection:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Python addition: see __iter__."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Clear(self) -> None:
        """removes all the object of the selection."""

    def Select(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theFilter: nanoocp.SelectMgr.SelectMgr_Filter | None, theSelScheme: AIS_SelectionScheme, theIsDetected: bool) -> AIS_SelectStatus:
        """
        if the object is not yet in the selection, it will be added.
        if the object is already in the selection, it will be removed.
        @param[in] theOwner element to change selection state
        @param[in] theFilter context filter
        @param[in] theSelScheme selection scheme
        @param[in] theIsDetected flag of object detection
        @return result of selection
        """

    def AddSelect(self, theObject: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> AIS_SelectStatus:
        """
        the object is always add int the selection.
        faster when the number of objects selected is great.
        """

    def ClearAndSelect(self, theObject: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theFilter: nanoocp.SelectMgr.SelectMgr_Filter | None, theIsDetected: bool) -> None:
        """
        clears the selection and adds the object in the selection.
        @param[in] theObject element to change selection state
        @param[in] theFilter context filter
        @param[in] theIsDetected flag of object detection
        """

    def IsSelected(self, theObject: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """checks if the object is in the selection."""

    def Objects(self) -> nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_EntityOwner]:
        """Return the list of selected objects."""

    def Extent(self) -> int:
        """Return the number of selected objects."""

    def IsEmpty(self) -> bool:
        """Return true if list of selected objects is empty."""

    def Init(self) -> None:
        """Start iteration through selected objects."""

    def More(self) -> bool:
        """Return true if iterator points to selected object."""

    def Next(self) -> None:
        """Continue iteration through selected objects."""

    def Value(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Return selected object at iterator position."""

    def SelectOwners(self, thePickedOwners: nanoocp.NCollection.NCollection_Array1[nanoocp.SelectMgr.SelectMgr_EntityOwner], theSelScheme: AIS_SelectionScheme, theToAllowSelOverlap: bool, theFilter: nanoocp.SelectMgr.SelectMgr_Filter | None) -> None:
        """
        Select or deselect owners depending on the selection scheme.
        @param[in] thePickedOwners elements to change selection state
        @param[in] theSelScheme selection scheme, defines how owner is selected
        @param[in] theToAllowSelOverlap selection flag, if true - overlapped entities are allowed
        @param[in] theFilter context filter to skip not acceptable owners
        """

class AIS_InteractiveContext(nanoocp.Standard.Standard_Transient):
    """
    The Interactive Context allows you to manage graphic behavior and selection of Interactive
    Objects in one or more viewers. Class methods make this highly transparent. It is essential to
    remember that an Interactive Object which is already known by the Interactive Context must be
    modified using Context methods. You can only directly call the methods available for an
    Interactive Object if it has not been loaded into an Interactive Context.

    Each selectable object must specify the selection mode that is
    responsible for selection of object as a whole (global selection mode).
    Interactive context itself supports decomposed object selection with selection filters support.
    By default, global selection mode is equal to 0, but it might be redefined if needed.
    """

    @overload
    def __init__(self, MainViewer: nanoocp.V3d.V3d_Viewer | None) -> None:
        """
        @name object display management
        Constructs the interactive context object defined by the principal viewer MainViewer.
        """

    @overload
    def __init__(self, theOther: AIS_InteractiveContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DisplayStatus(self, anIobj: AIS_InteractiveObject | None) -> nanoocp.PrsMgr.PrsMgr_DisplayStatus:
        """
        Returns the display status of the entity anIobj.
        This will be one of the following:
        - AIS_DS_Displayed displayed in main viewer
        - AIS_DS_Erased    hidden in main viewer
        - AIS_DS_Temporary temporarily displayed
        - AIS_DS_None      nowhere displayed.
        """

    def Status(self, anObj: AIS_InteractiveObject | None, astatus: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Returns the status of the Interactive Context for the view of the Interactive Object.
        """

    @overload
    def IsDisplayed(self, anIobj: AIS_InteractiveObject | None) -> bool:
        """Returns true if Object is displayed in the interactive context."""

    @overload
    def IsDisplayed(self, aniobj: AIS_InteractiveObject | None, aMode: int) -> bool: ...

    def SetAutoActivateSelection(self, theIsAuto: bool) -> None:
        """
        Enable or disable automatic activation of default selection mode while displaying the object.
        """

    def GetAutoActivateSelection(self) -> bool:
        """
        Manages displaying the new object should also automatically activate default selection mode;
        TRUE by default.
        """

    @overload
    def Display(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Displays the object in this Context using default Display Mode.
        This will be the object's default display mode, if there is one. Otherwise, it will be the
        context mode. The Interactive Object's default selection mode is activated if
        GetAutoActivateSelection() is TRUE. In general, this is 0.
        """

    @overload
    def Display(self, theIObj: AIS_InteractiveObject | None, theDispMode: int, theSelectionMode: int, theToUpdateViewer: bool, theDispStatus: nanoocp.PrsMgr.PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.PrsMgr_DisplayStatus_None) -> None:
        """
        Sets status, display mode and selection mode for specified Object
        If theSelectionMode equals -1, theIObj will not be activated: it will be displayed but will
        not be selectable.
        """

    @overload
    def Display(self, theIObj: AIS_InteractiveObject | None, theDispMode: int, theSelectionMode: int, theToUpdateViewer: bool, theToAllowDecomposition: bool, theDispStatus: nanoocp.PrsMgr.PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.PrsMgr_DisplayStatus_None) -> None:
        """
        Deprecated in OCCT: Deprecated method Display() with obsolete argument theToAllowDecomposition

        @name obsolete methods
        """

    @overload
    def Load(self, theObj: AIS_InteractiveObject | None, theSelectionMode: int = -1) -> None:
        """
        Allows you to load the Interactive Object with a given selection mode,
        and/or with the desired decomposition option, whether the object is visualized or not.
        The loaded objects will be selectable but displayable in highlighting only when detected by
        the Selector.
        """

    @overload
    def Load(self, theObj: AIS_InteractiveObject | None, theSelectionMode: int, arg2: bool) -> None:
        """
        Deprecated in OCCT: Deprecated method Load() with obsolete last argument theToAllowDecomposition
        """

    def Erase(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Hides the object. The object's presentations are simply flagged as invisible and therefore
        excluded from redrawing. To show hidden objects, use Display().
        """

    def EraseAll(self, theToUpdateViewer: bool) -> None:
        """
        Hides all objects. The object's presentations are simply flagged as invisible and therefore
        excluded from redrawing. To show all hidden objects, use DisplayAll().
        """

    def DisplayAll(self, theToUpdateViewer: bool) -> None:
        """Displays all hidden objects."""

    def EraseSelected(self, theToUpdateViewer: bool) -> None:
        """
        Hides selected objects. The object's presentations are simply flagged as invisible and
        therefore excluded from redrawing. To show hidden objects, use Display().
        """

    def DisplaySelected(self, theToUpdateViewer: bool) -> None:
        """Displays current objects."""

    def ClearPrs(self, theIObj: AIS_InteractiveObject | None, theMode: int, theToUpdateViewer: bool) -> None:
        """
        Empties the graphic presentation of the mode indexed by aMode.
        Warning! Removes theIObj. theIObj is still active if it was previously activated.
        """

    def Remove(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes Object from every viewer."""

    def RemoveAll(self, theToUpdateViewer: bool) -> None:
        """Removes all the objects from Context."""

    @overload
    def Redisplay(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool, theAllModes: bool = False) -> None:
        """
        Recomputes the seen parts presentation of the Object.
        If theAllModes equals true, all presentations are present in the object even if unseen.
        """

    @overload
    def Redisplay(self, theTypeOfObject: AIS_KindOfInteractive, theSignature: int, theToUpdateViewer: bool) -> None:
        """
        Recomputes the Prs/Selection of displayed objects of a given type and a given signature.
        if signature = -1  doesn't take signature criterion.
        """

    def RecomputePrsOnly(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool, theAllModes: bool = False) -> None:
        """
        Recomputes the displayed presentations, flags the others.
        Doesn't update presentations.
        """

    def RecomputeSelectionOnly(self, anIObj: AIS_InteractiveObject | None) -> None:
        """
        Recomputes the active selections, flags the others.
        Doesn't update presentations.
        """

    def Update(self, theIObj: AIS_InteractiveObject | None, theUpdateViewer: bool) -> None:
        """
        Updates displayed interactive object by checking and recomputing its flagged as "to be
        recomputed" presentation and selection structures. This method does not force any
        recomputation on its own. The method recomputes selections even if they are loaded without
        activation in particular selector.
        """

    @overload
    def HighlightStyle(self, theStyleType: nanoocp.Prs3d.Prs3d_TypeOfHighlight) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        @name highlighting management
        Returns default highlight style settings (could be overridden by PrsMgr_PresentableObject).

        Tip: although highlighting style is defined by Prs3d_Drawer,
        only a small set of properties derived from it's base class Graphic3d_PresentationAttributes
        will be actually used in most cases.

        Default highlight style for all types is Aspect_TOHM_COLOR. Other defaults:
        - Prs3d_TypeOfHighlight_Dynamic
        * Color: Quantity_NOC_CYAN1;
        * Layer: Graphic3d_ZLayerId_Top,
        object highlighting is drawn on top of main scene within Immediate Layers,
        so that V3d_View::RedrawImmediate() will be enough to see update;
        - Prs3d_TypeOfHighlight_LocalDynamic
        * Color: Quantity_NOC_CYAN1;
        * Layer: Graphic3d_ZLayerId_Topmost,
        object parts highlighting is drawn on top of main scene within Immediate Layers
        with depth cleared (even overlapped geometry will be revealed);
        - Prs3d_TypeOfHighlight_Selected
        * Color: Quantity_NOC_GRAY80;
        * Layer: Graphic3d_ZLayerId_UNKNOWN,
        object highlighting is drawn on top of main scene within the same layer
        as object itself (e.g. Graphic3d_ZLayerId_Default by default) and increased
        priority.

        @param[in] theStyleType highlight style to modify
        @return drawer associated to specified highlight type

        @sa MoveTo() using Prs3d_TypeOfHighlight_Dynamic and Prs3d_TypeOfHighlight_LocalDynamic types
        @sa SelectDetected() using Prs3d_TypeOfHighlight_Selected and
        Prs3d_TypeOfHighlight_LocalSelected types
        @sa PrsMgr_PresentableObject::DynamicHilightAttributes() overriding
        Prs3d_TypeOfHighlight_Dynamic and Prs3d_TypeOfHighlight_LocalDynamic defaults on object level
        @sa PrsMgr_PresentableObject::HilightAttributes() overriding Prs3d_TypeOfHighlight_Selected
        and Prs3d_TypeOfHighlight_LocalSelected defaults on object level
        """

    @overload
    def HighlightStyle(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        Returns current dynamic highlight style settings corresponding to
        Prs3d_TypeOfHighlight_Dynamic. This is just a short-cut to
        HighlightStyle(Prs3d_TypeOfHighlight_Dynamic).
        """

    @overload
    def HighlightStyle(self, theObj: AIS_InteractiveObject | None) -> tuple[bool, nanoocp.Prs3d.Prs3d_Drawer]:
        """
        Returns highlight style of the object if it is marked as highlighted via global status
        @param[in] theObj  the object to check
        """

    @overload
    def HighlightStyle(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> tuple[bool, nanoocp.Prs3d.Prs3d_Drawer]:
        """
        Returns highlight style of the owner if it is selected
        @param[in] theOwner  the owner to check
        """

    @overload
    def SetHighlightStyle(self, theStyleType: nanoocp.Prs3d.Prs3d_TypeOfHighlight, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Setup highlight style settings.
        Tip: it is better modifying existing style returned by method HighlightStyle()
        instead of creating a new Prs3d_Drawer to avoid unexpected results due misconfiguration.

        If a new highlight style is created, its presentation Zlayer should be checked,
        otherwise highlighting might not work as expected.
        """

    @overload
    def SetHighlightStyle(self, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Setup the style of dynamic highlighting corresponding to Prs3d_TypeOfHighlight_Selected.
        This is just a short-cut to SetHighlightStyle(Prs3d_TypeOfHighlight_Dynamic,theStyle).
        """

    def SelectionStyle(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        Returns current selection style settings corresponding to Prs3d_TypeOfHighlight_Selected.
        This is just a short-cut to HighlightStyle(Prs3d_TypeOfHighlight_Selected).
        """

    def SetSelectionStyle(self, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Setup the style of selection highlighting.
        This is just a short-cut to SetHighlightStyle(Prs3d_TypeOfHighlight_Selected,theStyle).
        """

    @overload
    def IsHilighted(self, theObj: AIS_InteractiveObject | None) -> bool:
        """
        Returns true if the object is marked as highlighted via its global status
        @param[in] theObj  the object to check
        """

    @overload
    def IsHilighted(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """
        Returns true if the owner is marked as selected
        @param[in] theOwner  the owner to check
        """

    def HilightWithColor(self, theObj: AIS_InteractiveObject | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theToUpdateViewer: bool) -> None:
        """Changes the color of all the lines of the object in view."""

    def Unhilight(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes highlighting from the Object."""

    def DisplayPriority(self, theIObj: AIS_InteractiveObject | None) -> nanoocp.Graphic3d.Graphic3d_DisplayPriority:
        """
        @name object presence management (View affinity, Layer, Priority)
        Returns the display priority of the Object.
        """

    @overload
    def SetDisplayPriority(self, theIObj: AIS_InteractiveObject | None, thePriority: nanoocp.Graphic3d.Graphic3d_DisplayPriority) -> None:
        """
        Sets the display priority of the seen parts presentation of the Object.
        """

    @overload
    def SetDisplayPriority(self, theIObj: AIS_InteractiveObject | None, thePriority: int) -> None:
        """
        Deprecated in OCCT: Deprecated since OCCT7.7, Graphic3d_DisplayPriority should be passed instead of integer number to SetDisplayPriority()
        """

    def GetZLayer(self, theIObj: AIS_InteractiveObject | None) -> int:
        """Get Z layer id set for displayed interactive object."""

    def SetZLayer(self, theIObj: AIS_InteractiveObject | None, theLayerId: int) -> None:
        """
        Set Z layer id for interactive object.
        The Z layers can be used to display temporarily presentations of some object in front of the
        other objects in the scene. The ids for Z layers are generated by V3d_Viewer.
        """

    def SetViewAffinity(self, theIObj: AIS_InteractiveObject | None, theView: nanoocp.V3d.V3d_View | None, theIsVisible: bool) -> None:
        """
        Setup object visibility in specified view.
        Has no effect if object is not displayed in this context.
        """

    def DisplayMode(self) -> int:
        """
        @name Display Mode management
        Returns the Display Mode setting to be used by default.
        """

    @overload
    def SetDisplayMode(self, theMode: int, theToUpdateViewer: bool) -> None:
        """
        Sets the display mode of seen Interactive Objects (which have no overridden Display Mode).
        """

    @overload
    def SetDisplayMode(self, theIObj: AIS_InteractiveObject | None, theMode: int, theToUpdateViewer: bool) -> None:
        """
        Sets the display mode of seen Interactive Objects.
        theMode provides the display mode index of the entity theIObj.
        """

    def UnsetDisplayMode(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Unsets the display mode of seen Interactive Objects."""

    def SetLocation(self, theObject: AIS_InteractiveObject | None, theLocation: nanoocp.TopLoc.TopLoc_Location) -> None:
        """
        @name object local transformation management
        Puts the location on the initial graphic representation and the selection for the Object.
        """

    def ResetLocation(self, theObject: AIS_InteractiveObject | None) -> None:
        """Puts the Object back into its initial position."""

    def HasLocation(self, theObject: AIS_InteractiveObject | None) -> bool:
        """Returns true if the Object has a location."""

    def Location(self, theObject: AIS_InteractiveObject | None) -> nanoocp.TopLoc.TopLoc_Location:
        """Returns the location of the Object."""

    def SetTransformPersistence(self, theObject: AIS_InteractiveObject | None, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """Sets transform persistence."""

    def SetPixelTolerance(self, thePrecision: int = 2) -> None:
        """
        @name mouse picking logic (detection and dynamic highlighting of entities under cursor)
        Setup pixel tolerance for MoveTo() operation.
        @sa MoveTo().
        """

    def PixelTolerance(self) -> int:
        """
        Returns the pixel tolerance, default is 2.
        Pixel Tolerance extends sensitivity within MoveTo() operation (picking by point)
        and can be adjusted by application based on user input precision (e.g. screen pixel density,
        input device precision, etc.).
        """

    def SetSelectionSensitivity(self, theObject: AIS_InteractiveObject | None, theMode: int, theNewSensitivity: int) -> None:
        """
        Allows to manage sensitivity of a particular selection of interactive object theObject
        and changes previous sensitivity value of all sensitive entities in selection with theMode
        to the given theNewSensitivity.
        """

    def LastActiveView(self) -> nanoocp.V3d.V3d_View:
        """Returns last active View (argument of MoveTo()/Select() methods)."""

    @overload
    def MoveTo(self, theXPix: int, theYPix: int, theView: nanoocp.V3d.V3d_View | None, theToRedrawOnUpdate: bool) -> AIS_StatusOfDetection:
        """
        Relays mouse position in pixels theXPix and theYPix to the interactive context selectors.
        This is done by the view theView passing this position to the main viewer and updating it.
        If theToRedrawOnUpdate is set to false, callee should call RedrawImmediate() to highlight
        detected object.
        @sa PickingStrategy()
        @sa HighlightStyle() defining default dynamic highlight styles of detected owners
        (Prs3d_TypeOfHighlight_Dynamic and Prs3d_TypeOfHighlight_LocalDynamic)
        @sa PrsMgr_PresentableObject::DynamicHilightAttributes() defining per-object dynamic highlight
        style of detected owners (overrides defaults)
        """

    @overload
    def MoveTo(self, theAxis: nanoocp.gp.gp_Ax1, theView: nanoocp.V3d.V3d_View | None, theToRedrawOnUpdate: bool) -> AIS_StatusOfDetection:
        """
        Relays axis theAxis to the interactive context selectors.
        This is done by the view theView passing this axis to the main viewer and updating it.
        If theToRedrawOnUpdate is set to false, callee should call RedrawImmediate() to highlight
        detected object.
        @sa PickingStrategy()
        """

    def ClearDetected(self, theToRedrawImmediate: bool = False) -> bool:
        """
        Clears the list of entities detected by MoveTo() and resets dynamic highlighting.
        @param theToRedrawImmediate if TRUE, the main Viewer will be redrawn on update
        @return TRUE if viewer needs to be updated (e.g. there were actually dynamically highlighted
        entities)
        """

    def HasDetected(self) -> bool:
        """
        Returns true if there is a mouse-detected entity in context.
        @sa DetectedOwner(), HasNextDetected(), HilightPreviousDetected(), HilightNextDetected().
        """

    def DetectedOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """
        Returns the owner of the detected sensitive primitive which is currently dynamically
        highlighted. WARNING! This method is irrelevant to
        InitDetected()/MoreDetected()/NextDetected().
        @sa HasDetected(), HasNextDetected(), HilightPreviousDetected(), HilightNextDetected().
        """

    def DetectedInteractive(self) -> AIS_InteractiveObject:
        """
        Returns the interactive objects last detected in context.
        In general this is just a wrapper for
        occ::down_cast<AIS_InteractiveObject>(DetectedOwner()->Selectable()).
        @sa DetectedOwner()
        """

    def HasDetectedShape(self) -> bool:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Returns true if there is a detected shape in local context.
        @sa HasDetected(), DetectedShape()
        """

    def DetectedShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Returns the shape detected in local context.
        @sa DetectedOwner()
        """

    def HasNextDetected(self) -> bool:
        """
        returns True if other entities were detected in the last mouse detection
        @sa HilightPreviousDetected(), HilightNextDetected().
        """

    def HilightNextDetected(self, theView: nanoocp.V3d.V3d_View | None, theToRedrawImmediate: bool = True) -> int:
        """
        If more than 1 object is detected by the selector, only the "best" owner is hilighted at the
        mouse position. This Method allows the user to hilight one after another the other detected
        entities. If The method select is called, the selected entity will be the hilighted one!
        WARNING: Loop Method. When all the detected entities have been hilighted, the next call will
        hilight the first one again.
        @return the Rank of hilighted entity
        @sa HasNextDetected(), HilightPreviousDetected().
        """

    def HilightPreviousDetected(self, theView: nanoocp.V3d.V3d_View | None, theToRedrawImmediate: bool = True) -> int:
        """
        Same as previous methods in reverse direction.
        @sa HasNextDetected(), HilightNextDetected().
        """

    def InitDetected(self) -> None:
        """
        @name iteration through detected entities
        Initialization for iteration through mouse-detected objects in
        interactive context or in local context if it is opened.
        @sa DetectedCurrentOwner(), MoreDetected(), NextDetected().
        """

    def MoreDetected(self) -> bool:
        """
        Return TRUE if there is more mouse-detected objects after the current one
        during iteration through mouse-detected interactive objects.
        @sa DetectedCurrentOwner(), InitDetected(), NextDetected().
        """

    def NextDetected(self) -> None:
        """
        Gets next current object during iteration through mouse-detected interactive objects.
        @sa DetectedCurrentOwner(), InitDetected(), MoreDetected().
        """

    def DetectedCurrentOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """
        Returns the owner from detected list pointed by current iterator position.
        WARNING! This method is irrelevant to DetectedOwner() which returns last picked Owner
        regardless of iterator position!
        @sa InitDetected(), MoreDetected(), NextDetected().
        """

    @overload
    def AddSelect(self, theObject: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> AIS_StatusOfPick:
        """
        @name Selection management
        Adds object in the selection.
        """

    @overload
    def AddSelect(self, theObject: AIS_InteractiveObject | None) -> AIS_StatusOfPick:
        """Adds object in the selection."""

    def SelectRectangle(self, thePntMin: nanoocp.BVH.BVH_Vec2i, thePntMax: nanoocp.BVH.BVH_Vec2i, theView: nanoocp.V3d.V3d_View | None, theSelScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> AIS_StatusOfPick:
        """
        Selects objects within the bounding rectangle.
        Viewer should be explicitly redrawn after selection.
        @param[in] thePntMin  rectangle lower point (in pixels)
        @param[in] thePntMax  rectangle upper point (in pixels)
        @param[in] theView    active view where rectangle is defined
        @param[in] theSelScheme  selection scheme
        @return picking status
        @sa StdSelect_ViewerSelector3d::AllowOverlapDetection()
        """

    def SelectPolygon(self, thePolyline: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theView: nanoocp.V3d.V3d_View | None, theSelScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> AIS_StatusOfPick:
        """
        Select everything found in the polygon defined by bounding polyline.
        Viewer should be explicitly redrawn after selection.
        @param[in] thePolyline   polyline defining polygon bounds (in pixels)
        @param[in] theView       active view where polyline is defined
        @param[in] theSelScheme  selection scheme
        @return picking status
        """

    def SelectPoint(self, thePnt: nanoocp.BVH.BVH_Vec2i, theView: nanoocp.V3d.V3d_View | None, theSelScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> AIS_StatusOfPick:
        """
        Selects the topmost object picked by the point in the view,
        Viewer should be explicitly redrawn after selection.
        @param[in] thePnt   point pixel coordinates within the view
        @param[in] theView  active view where point is defined
        @param[in] theSelScheme  selection scheme
        @return picking status
        """

    def SelectDetected(self, theSelScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> AIS_StatusOfPick:
        """
        Select and hilights the previous detected via AIS_InteractiveContext::MoveTo() method;
        unhilights the previous picked.
        Viewer should be explicitly redrawn after selection.
        @param[in] theSelScheme  selection scheme
        @return picking status

        @sa HighlightStyle() defining default highlight styles of selected owners
        (Prs3d_TypeOfHighlight_Selected and Prs3d_TypeOfHighlight_LocalSelected)
        @sa PrsMgr_PresentableObject::HilightAttributes() defining per-object highlight style of
        selected owners (overrides defaults)
        For all selection schemes, allowing to select an object,
        HandleMouseClick is available
        """

    @overload
    def BoundingBoxOfSelection(self, theView: nanoocp.V3d.V3d_View | None) -> nanoocp.Bnd.Bnd_Box:
        """Returns bounding box of selected objects."""

    @overload
    def BoundingBoxOfSelection(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Deprecated in OCCT: BoundingBoxOfSelection() should be called with View argument
        """

    @overload
    def Select(self, theOwners: nanoocp.NCollection.NCollection_Array1[nanoocp.SelectMgr.SelectMgr_EntityOwner], theSelScheme: AIS_SelectionScheme) -> AIS_StatusOfPick:
        """
        Sets list of owner selected/deselected using specified selection scheme.
        @param theOwners owners to change selection state
        @param theSelScheme selection scheme
        @return picking status
        """

    @overload
    def Select(self, theXPMin: int, theYPMin: int, theXPMax: int, theYPMax: int, theView: nanoocp.V3d.V3d_View | None, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectRectangle() taking AIS_SelectionScheme_Replace should be called instead

        Selects everything found in the bounding rectangle defined by the pixel minima and maxima,
        XPMin, YPMin, XPMax, and YPMax in the view. The objects detected are passed to the main
        viewer, which is then updated.
        """

    @overload
    def Select(self, thePolyline: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theView: nanoocp.V3d.V3d_View | None, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectPolygon() taking AIS_SelectionScheme_Replace should be called instead

        polyline selection; clears the previous picked list
        """

    @overload
    def Select(self, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectDetected() taking AIS_SelectionScheme_Replace should be called instead

        Stores and hilights the previous detected; Unhilights the previous picked.
        @sa MoveTo().
        """

    @overload
    def FitSelected(self, theView: nanoocp.V3d.V3d_View | None, theMargin: float, theToUpdate: bool) -> None: ...

    @overload
    def FitSelected(self, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Fits the view correspondingly to the bounds of selected objects.
        Infinite objects are ignored if infinite state of AIS_InteractiveObject is set to true.
        """

    def ToHilightSelected(self) -> bool:
        """
        Return value specified whether selected object must be hilighted when mouse cursor is moved
        above it
        @sa MoveTo()
        """

    def SetToHilightSelected(self, toHilight: bool) -> None:
        """
        Specify whether selected object must be hilighted when mouse cursor is moved above it (in
        MoveTo method). By default this value is false and selected object is not hilighted in this
        case.
        @sa MoveTo()
        """

    def AutomaticHilight(self) -> bool:
        """
        Returns true if the automatic highlight mode is active; TRUE by default.
        @sa MoveTo(), Select(), HilightWithColor(), Unhilight()
        """

    def SetAutomaticHilight(self, theStatus: bool) -> None:
        """
        Sets the highlighting status of detected and selected entities.
        This function allows you to disconnect the automatic mode.

        MoveTo() will fill the list of detected entities
        and Select() will set selected state to detected objects regardless of this flag,
        but with disabled AutomaticHiligh() their highlighting state will be left unaffected,
        so that application will be able performing custom highlighting in a different way, if needed.

        This API should be distinguished from SelectMgr_SelectableObject::SetAutoHilight()
        that is used to implement custom highlighting logic for a specific interactive object class.

        @sa MoveTo(), Select(), HilightWithColor(), Unhilight()
        """

    @overload
    def SetSelected(self, theOwners: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theToUpdateViewer: bool) -> None:
        """
        Unhighlights previously selected owners and marks them as not selected.
        Marks owner given as selected and highlights it.
        Performs selection filters check.
        """

    @overload
    def SetSelected(self, theObject: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Puts the interactive object aniObj in the list of selected objects.
        Performs selection filters check.
        """

    @overload
    def AddOrRemoveSelected(self, theObject: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None: ...

    @overload
    def AddOrRemoveSelected(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theToUpdateViewer: bool) -> None:
        """
        Allows to highlight or unhighlight the owner given depending on its selection status
        """

    def SetSelectedState(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theIsSelected: bool) -> bool:
        """
        Updates Selected state of specified owner without calling HilightSelected().
        Has no effect if Selected state is not changed, and redirects to AddOrRemoveSelected()
        otherwise.
        @param theOwner owner object to set selected state
        @param theIsSelected new selected state
        @return TRUE if Selected state has been changed
        """

    def HilightSelected(self, theToUpdateViewer: bool) -> None:
        """Highlights selected objects."""

    def UnhilightSelected(self, theToUpdateViewer: bool) -> None:
        """Removes highlighting from selected objects."""

    def UpdateSelected(self, theToUpdateViewer: bool) -> None:
        """
        Updates the list of selected objects:
        i.e. highlights the newly selected ones and unhighlights previously selected objects.
        @sa HilightSelected().
        """

    def ClearSelected(self, theToUpdateViewer: bool) -> None:
        """
        Empties previous selected objects in order to get the selected objects detected by the
        selector using UpdateSelected.
        """

    @overload
    def IsSelected(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """Returns true is the owner given is selected"""

    @overload
    def IsSelected(self, theObj: AIS_InteractiveObject | None) -> bool:
        """Returns true is the object given is selected"""

    def FirstSelectedObject(self) -> AIS_InteractiveObject:
        """Returns the first selected object in the list of current selected."""

    def NbSelected(self) -> int:
        """
        Count a number of selected entities using InitSelected()+MoreSelected()+NextSelected()
        iterator.
        @sa SelectedOwner(), InitSelected(), MoreSelected(), NextSelected().
        """

    def InitSelected(self) -> None:
        """
        Initializes a scan of the selected objects.
        @sa SelectedOwner(), MoreSelected(), NextSelected().
        """

    def MoreSelected(self) -> bool:
        """
        Returns true if there is another object found by the scan of the list of selected objects.
        @sa SelectedOwner(), InitSelected(), NextSelected().
        """

    def NextSelected(self) -> None:
        """
        Continues the scan to the next object in the list of selected objects.
        @sa SelectedOwner(), InitSelected(), MoreSelected().
        """

    def SelectedOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """
        Returns the owner of the selected entity.
        @sa InitSelected(), MoreSelected(), NextSelected().
        """

    def SelectedInteractive(self) -> AIS_InteractiveObject:
        """
        Return Handle(AIS_InteractiveObject)::DownCast (SelectedOwner()->Selectable()).
        @sa SelectedOwner().
        """

    def HasSelectedShape(self) -> bool:
        """
        Returns TRUE if the interactive context has a shape selected.
        @sa SelectedShape().
        """

    def SelectedShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the selected shape.
        Basically it is just a shape returned stored by StdSelect_BRepOwner with graphic
        transformation being applied:
        @code
        const occ::handle<StdSelect_BRepOwner> aBRepOwner = Handle(StdSelect_BRepOwner)::DownCast
        (SelectedOwner()); TopoDS_Shape aSelShape    = aBRepOwner->Shape(); TopoDS_Shape
        aLocatedShape = aSelShape.Located (aBRepOwner->Location() * aSelShape.Location());
        @endcode
        @sa SelectedOwner(), HasSelectedShape().
        """

    def HasApplicative(self) -> bool:
        """
        Returns SelectedInteractive()->HasOwner().
        @sa SelectedOwner().
        """

    def Applicative(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns SelectedInteractive()->GetOwner().
        @sa SelectedOwner().
        """

    def BeginImmediateDraw(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - Graphic3d_ZLayerId with IsImmediate flag should be used instead

        @name immediate mode rendering
        """

    def ImmediateAdd(self, theObj: AIS_InteractiveObject | None, theMode: int = 0) -> bool:
        """
        Deprecated in OCCT: Deprecated method - Graphic3d_ZLayerId with IsImmediate flag should be used instead
        """

    @overload
    def EndImmediateDraw(self, theView: nanoocp.V3d.V3d_View | None) -> bool: ...

    @overload
    def EndImmediateDraw(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - Graphic3d_ZLayerId with IsImmediate flag should be used instead
        """

    def IsImmediateModeOn(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - Graphic3d_ZLayerId with IsImmediate flag should be used instead
        """

    def RedrawImmediate(self, theViewer: nanoocp.V3d.V3d_Viewer | None) -> None:
        """
        Redraws immediate structures in all views of the viewer given taking into account its
        visibility.
        """

    def SetSelectionModeActive(self, theObj: AIS_InteractiveObject | None, theMode: int, theToActivate: bool, theConcurrency: AIS_SelectionModesConcurrency = ..., theIsForce: bool = False) -> None:
        """
        @name management of active Selection Modes
        Activates or deactivates the selection mode for specified object.
        Has no effect if selection mode was already active/deactivated.
        @param theObj         object to activate/deactivate selection mode
        @param theMode        selection mode to activate/deactivate;
        deactivation of -1 selection mode will effectively deactivate all
        selection modes; activation of -1 selection mode with
        AIS_SelectionModesConcurrency_Single will deactivate all selection
        modes, and will has no effect otherwise
        @param theToActivate  activation/deactivation flag
        @param theConcurrency specifies how to handle already activated selection modes;
        default value (AIS_SelectionModesConcurrency_Multiple) means active
        selection modes should be left as is,
        AIS_SelectionModesConcurrency_Single can be used if only one selection
        mode is expected to be active and
        AIS_SelectionModesConcurrency_GlobalOrLocal can be used if either
        AIS_InteractiveObject::GlobalSelectionMode() or any combination of Local
        selection modes is acceptable; this value is considered only if
        theToActivate set to TRUE
        @param theIsForce     when set to TRUE, the display status will be ignored while activating
        selection mode
        """

    @overload
    def Activate(self, theObj: AIS_InteractiveObject | None, theMode: int = 0, theIsForce: bool = False) -> None:
        """
        Activates the selection mode aMode whose index is given, for the given interactive entity
        anIobj.
        """

    @overload
    def Activate(self, theMode: int, theIsForce: bool = False) -> None:
        """Activates the given selection mode for the all displayed objects."""

    @overload
    def Deactivate(self, theObj: AIS_InteractiveObject | None) -> None:
        """Deactivates all the activated selection modes of an object."""

    @overload
    def Deactivate(self, theObj: AIS_InteractiveObject | None, theMode: int) -> None:
        """
        Deactivates all the activated selection modes of the interactive object anIobj with a given
        selection mode aMode.
        """

    @overload
    def Deactivate(self, theMode: int) -> None:
        """Deactivates the given selection mode for all displayed objects."""

    @overload
    def Deactivate(self) -> None:
        """Deactivates all the activated selection mode at all displayed objects."""

    def ActivatedModes(self, anIobj: AIS_InteractiveObject | None, theList: nanoocp.NCollection.NCollection_List[int]) -> None:
        """Returns the list of activated selection modes."""

    def EntityOwners(self, theIObj: AIS_InteractiveObject | None, theMode: int = -1) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_IndexedMap[nanoocp.SelectMgr.SelectMgr_EntityOwner]]:
        """
        Returns a collection containing all entity owners created for the interactive object in
        specified selection mode (in all active modes if the Mode == -1)
        """

    def FilterType(self) -> nanoocp.SelectMgr.SelectMgr_FilterType:
        """
        @name Selection Filters management
        @return the context selection filter type.
        """

    def SetFilterType(self, theFilterType: nanoocp.SelectMgr.SelectMgr_FilterType) -> None:
        """
        Sets the context selection filter type.
        SelectMgr_TypeFilter_OR selection filter is used by default.
        @param theFilterType the filter type.
        """

    def Filters(self) -> nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_Filter]:
        """Returns the list of filters active in a local context."""

    def GlobalFilter(self) -> nanoocp.SelectMgr.SelectMgr_AndOrFilter:
        """@return the context selection global context filter."""

    def AddFilter(self, theFilter: nanoocp.SelectMgr.SelectMgr_Filter | None) -> None:
        """Allows you to add the filter."""

    def RemoveFilter(self, theFilter: nanoocp.SelectMgr.SelectMgr_Filter | None) -> None:
        """Removes a filter from context."""

    def RemoveFilters(self) -> None:
        """Remove all filters from context."""

    def PickingStrategy(self) -> nanoocp.SelectMgr.SelectMgr_PickingStrategy:
        """
        Return picking strategy; SelectMgr_PickingStrategy_FirstAcceptable by default.
        @sa MoveTo(), Filters()
        """

    def SetPickingStrategy(self, theStrategy: nanoocp.SelectMgr.SelectMgr_PickingStrategy) -> None:
        """
        Setup picking strategy - which entities detected by picking line will be accepted, considering
        Selection Filters. By default (SelectMgr_PickingStrategy_FirstAcceptable), Selection Filters
        reduce the list of entities so that the context accepts topmost in remaining.

        This means that entities behind non-selectable (by filters) parts can be picked by user.
        If this behavior is undesirable, and user wants that non-selectable (by filters) parts
        should remain an obstacle for picking, SelectMgr_PickingStrategy_OnlyTopmost can be set
        instead.

        Notice, that since Selection Manager operates only objects registered in it,
        SelectMgr_PickingStrategy_OnlyTopmost will NOT prevent picking entities behind
        visible by unregistered in Selection Manager presentations (e.g. deactivated).
        Hence, SelectMgr_PickingStrategy_OnlyTopmost changes behavior only with Selection Filters
        enabled.
        """

    def DefaultDrawer(self) -> nanoocp.Prs3d.Prs3d_Drawer:
        """
        @name common properties
        Returns the default attribute manager.
        This contains all the color and line attributes which can be used by interactive objects which
        do not have their own attributes.
        """

    def SetDefaultDrawer(self, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """
        Sets the default attribute manager; should be set at context creation time.
        Warning - this setter doesn't update links to the default drawer of already displayed objects!
        """

    def CurrentViewer(self) -> nanoocp.V3d.V3d_Viewer:
        """Returns the current viewer."""

    def SelectionManager(self) -> nanoocp.SelectMgr.SelectMgr_SelectionManager: ...

    def MainPrsMgr(self) -> nanoocp.PrsMgr.PrsMgr_PresentationManager: ...

    def MainSelector(self) -> nanoocp.SelectMgr.SelectMgr_ViewerSelector: ...

    def UpdateCurrentViewer(self) -> None:
        """Updates the current viewer."""

    @overload
    def DisplayedObjects(self, aListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        Returns the list of displayed objects of a particular Type WhichKind and Signature
        WhichSignature. By Default, WhichSignature equals -1. This means that there is a check on type
        only.
        """

    @overload
    def DisplayedObjects(self, theWhichKind: AIS_KindOfInteractive, theWhichSignature: int, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        gives the list of displayed objects of a particular Type and signature.
        by Default, <WhichSignature> = -1 means control only on <WhichKind>.
        """

    @overload
    def ErasedObjects(self, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        Returns the list theListOfIO of erased objects (hidden objects) particular Type WhichKind and
        Signature WhichSignature. By Default, WhichSignature equals 1. This means that there is a
        check on type only.
        """

    @overload
    def ErasedObjects(self, theWhichKind: AIS_KindOfInteractive, theWhichSignature: int, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        gives the list of erased objects (hidden objects)
        Type and signature by Default, <WhichSignature> = -1 means control only on <WhichKind>.
        """

    @overload
    def ObjectsByDisplayStatus(self, theStatus: nanoocp.PrsMgr.PrsMgr_DisplayStatus, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        Returns the list theListOfIO of objects with indicated display status particular Type
        WhichKind and Signature WhichSignature. By Default, WhichSignature equals 1. This means that
        there is a check on type only.
        """

    @overload
    def ObjectsByDisplayStatus(self, WhichKind: AIS_KindOfInteractive, WhichSignature: int, theStatus: nanoocp.PrsMgr.PrsMgr_DisplayStatus, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]) -> None:
        """
        gives the list of objects with indicated display status
        Type and signature by Default, <WhichSignature> = -1 means control only on <WhichKind>.
        """

    def ObjectsInside(self, aListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject], WhichKind: AIS_KindOfInteractive = AIS_KindOfInteractive.AIS_KindOfInteractive_None, WhichSignature: int = -1) -> None:
        """
        fills <aListOfIO> with objects of a particular Type and Signature with no consideration of
        display status. by Default, <WhichSignature> = -1 means control only on <WhichKind>. if
        <WhichKind> = AIS_KindOfInteractive_None and <WhichSignature> = -1, all the objects are put
        into the list.
        """

    def ObjectIterator(self) -> "NCollection_DataMap<opencascade::handle<AIS_InteractiveObject>, opencascade::handle<AIS_GlobalStatus>, NCollection_DefaultHasher<opencascade::handle<AIS_InteractiveObject>>>::Iterator":
        """Create iterator through all objects registered in context."""

    def RebuildSelectionStructs(self) -> None:
        """Rebuilds 1st level of BVH selection forcibly"""

    def Disconnect(self, theAssembly: AIS_InteractiveObject | None, theObjToDisconnect: AIS_InteractiveObject | None = None) -> None:
        """
        Disconnects theObjToDisconnect from theAssembly and removes dependent selection structures
        """

    def ObjectsForView(self, theListOfIO: nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject], theView: nanoocp.V3d.V3d_View | None, theIsVisibleInView: bool, theStatus: nanoocp.PrsMgr.PrsMgr_DisplayStatus = PrsMgr_DisplayStatus.PrsMgr_DisplayStatus_None) -> None:
        """
        Query objects visible or hidden in specified view due to affinity mask.
        """

    def GravityPoint(self, theView: nanoocp.V3d.V3d_View | None) -> nanoocp.gp.gp_Pnt:
        """Return rotation gravity point."""

    @overload
    def DisplayActiveSensitive(self, aView: nanoocp.V3d.V3d_View | None) -> None:
        """
        @name debug visualization
        Visualization of sensitives - for debugging purposes!
        """

    @overload
    def DisplayActiveSensitive(self, anObject: AIS_InteractiveObject | None, aView: nanoocp.V3d.V3d_View | None) -> None:
        """Visualization of sensitives - for debugging purposes!"""

    def ClearActiveSensitive(self, aView: nanoocp.V3d.V3d_View | None) -> None:
        """Clear visualization of sensitives."""

    def SetLocalAttributes(self, theIObj: AIS_InteractiveObject | None, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, theToUpdateViewer: bool) -> None:
        """
        @name common object display attributes
        Sets the graphic attributes of the interactive object, such as visualization mode, color, and
        material.
        """

    def UnsetLocalAttributes(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Removes the settings for local attributes of the Object and returns to defaults.
        """

    def SetCurrentFacingModel(self, aniobj: AIS_InteractiveObject | None, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None:
        """
        change the current facing model apply on polygons for SetColor(), SetTransparency(),
        SetMaterial() methods default facing model is Aspect_TOFM_TWO_SIDE. This mean that attributes
        is applying both on the front and back face.
        """

    def HasColor(self, aniobj: AIS_InteractiveObject | None) -> bool:
        """Returns true if a view of the Interactive Object has color."""

    def Color(self, aniobj: AIS_InteractiveObject | None, acolor: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns the color of the Object in the interactive context."""

    def SetColor(self, theIObj: AIS_InteractiveObject | None, theColor: nanoocp.Quantity.Quantity_Color, theToUpdateViewer: bool) -> None:
        """Sets the color of the selected entity."""

    def UnsetColor(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes the color selection for the selected entity."""

    def Width(self, aniobj: AIS_InteractiveObject | None) -> float:
        """
        Returns the width of the Interactive Object in the interactive context.
        """

    def SetWidth(self, theIObj: AIS_InteractiveObject | None, theValue: float, theToUpdateViewer: bool) -> None:
        """Sets the width of the Object."""

    def UnsetWidth(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes the width setting of the Object."""

    def SetMaterial(self, theIObj: AIS_InteractiveObject | None, theMaterial: nanoocp.Graphic3d.Graphic3d_MaterialAspect, theToUpdateViewer: bool) -> None:
        """Provides the type of material setting for the view of the Object."""

    def UnsetMaterial(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes the type of material setting for viewing the Object."""

    def SetTransparency(self, theIObj: AIS_InteractiveObject | None, theValue: float, theToUpdateViewer: bool) -> None:
        """
        Provides the transparency settings for viewing the Object.
        The transparency value aValue may be between 0.0, opaque, and 1.0, fully transparent.
        """

    def UnsetTransparency(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """Removes the transparency settings for viewing the Object."""

    def SetPolygonOffsets(self, theIObj: AIS_InteractiveObject | None, theMode: int, theFactor: float, theUnits: float, theToUpdateViewer: bool) -> None:
        """
        Sets up polygon offsets for the given AIS_InteractiveObject.
        It simply calls AIS_InteractiveObject::SetPolygonOffsets().
        """

    def HasPolygonOffsets(self, anObj: AIS_InteractiveObject | None) -> bool:
        """Simply calls AIS_InteractiveObject::HasPolygonOffsets()."""

    def PolygonOffsets(self, anObj: AIS_InteractiveObject | None) -> tuple[int, float, float]:
        """Retrieves current polygon offsets settings for Object."""

    def SetTrihedronSize(self, theSize: float, theToUpdateViewer: bool) -> None:
        """
        @name trihedron display attributes
        Sets the size aSize of the trihedron.
        Is used to change the default value 100 mm for display of trihedra.
        Use of this function in one of your own interactive objects requires a call to the Compute
        function of the new class. This will recalculate the presentation for every trihedron
        displayed.
        """

    def TrihedronSize(self) -> float:
        """returns the current value of trihedron size."""

    @overload
    def SetPlaneSize(self, theSizeX: float, theSizeY: float, theToUpdateViewer: bool) -> None:
        """
        @name plane display attributes
        Sets the plane size defined by the length in the X direction XSize and that in the Y direction
        YSize.
        """

    @overload
    def SetPlaneSize(self, theSize: float, theToUpdateViewer: bool) -> None:
        """Sets the plane size aSize."""

    def PlaneSize(self) -> tuple[bool, float, float]:
        """
        Returns true if the length in the X direction XSize is the same as that in the Y direction
        YSize.
        """

    @overload
    def SetDeviationCoefficient(self, theIObj: AIS_InteractiveObject | None, theCoefficient: float, theToUpdateViewer: bool) -> None:
        """
        @name tessellation deviation properties for automatic triangulation
        Sets the deviation coefficient theCoefficient.
        Drawings of curves or patches are made with respect to a maximal chordal deviation.
        A Deviation coefficient is used in the shading display mode.
        The shape is seen decomposed into triangles.
        These are used to calculate reflection of light from the surface of the object.
        The triangles are formed from chords of the curves in the shape.
        The deviation coefficient theCoefficient gives the highest value of the angle with which a
        chord can deviate from a tangent to a curve. If this limit is reached, a new triangle is
        begun. This deviation is absolute and is set through the method: SetMaximalChordialDeviation.
        The default value is 0.001.
        In drawing shapes, however, you are allowed to ask for a relative deviation.
        This deviation will be: SizeOfObject * DeviationCoefficient.
        """

    @overload
    def SetDeviationCoefficient(self, theCoefficient: float) -> None:
        """
        Sets the deviation coefficient theCoefficient.
        Drawings of curves or patches are made with respect to a maximal chordal deviation.
        A Deviation coefficient is used in the shading display mode.
        The shape is seen decomposed into triangles.
        These are used to calculate reflection of light from the surface of the object.
        The triangles are formed from chords of the curves in the shape.
        The deviation coefficient theCoefficient gives the highest value of the angle with which a
        chord can deviate from a tangent to a curve. If this limit is reached, a new triangle is
        begun. This deviation is absolute and is set through the method: SetMaximalChordialDeviation.
        The default value is 0.001.
        In drawing shapes, however, you are allowed to ask for a relative deviation.
        This deviation will be: SizeOfObject * DeviationCoefficient.
        """

    @overload
    def SetDeviationAngle(self, theIObj: AIS_InteractiveObject | None, theAngle: float, theToUpdateViewer: bool) -> None: ...

    @overload
    def SetDeviationAngle(self, theAngle: float) -> None:
        """default 20 degrees"""

    def SetAngleAndDeviation(self, theIObj: AIS_InteractiveObject | None, theAngle: float, theToUpdateViewer: bool) -> None:
        """
        Calls the AIS_Shape SetAngleAndDeviation to set both Angle and Deviation coefficients
        """

    def DeviationCoefficient(self) -> float:
        """
        Returns the deviation coefficient.
        Drawings of curves or patches are made with respect to a maximal chordal deviation.
        A Deviation coefficient is used in the shading display mode.
        The shape is seen decomposed into triangles.
        These are used to calculate reflection of light from the surface of the object.
        The triangles are formed from chords of the curves in the shape.
        The deviation coefficient gives the highest value of the angle with which a chord can deviate
        from a tangent to a curve. If this limit is reached, a new triangle is begun. This deviation
        is absolute and is set through Prs3d_Drawer::SetMaximalChordialDeviation. The default value is
        0.001. In drawing shapes, however, you are allowed to ask for a relative deviation. This
        deviation will be: SizeOfObject * DeviationCoefficient.
        """

    def DeviationAngle(self) -> float: ...

    def HiddenLineAspect(self) -> nanoocp.Prs3d.Prs3d_LineAspect:
        """
        @name HLR (Hidden Line Removal) display attributes
        Initializes hidden line aspect in the default drawing tool, or Drawer.
        The default values are:
        Color: Quantity_NOC_YELLOW
        Type of line: Aspect_TOL_DASH
        Width: 1.
        """

    def SetHiddenLineAspect(self, theAspect: nanoocp.Prs3d.Prs3d_LineAspect | None) -> None:
        """
        Sets the hidden line aspect anAspect.
        Aspect defines display attributes for hidden lines in HLR projections.
        """

    def DrawHiddenLine(self) -> bool:
        """
        returns true if the hidden lines are to be drawn.
        By default the hidden lines are not drawn.
        """

    def EnableDrawHiddenLine(self) -> None: ...

    def DisableDrawHiddenLine(self) -> None: ...

    def SetIsoNumber(self, NbIsos: int, WhichIsos: AIS_TypeOfIso = AIS_TypeOfIso.AIS_TOI_Both) -> None:
        """
        @name iso-line display attributes
        Sets the number of U and V isoparameters displayed.
        """

    def IsoNumber(self, WhichIsos: AIS_TypeOfIso = AIS_TypeOfIso.AIS_TOI_Both) -> int:
        """Returns the number of U and V isoparameters displayed."""

    @overload
    def IsoOnPlane(self, theToSwitchOn: bool) -> None:
        """Returns True if drawing isoparameters on planes is enabled."""

    @overload
    def IsoOnPlane(self) -> bool:
        """
        Returns True if drawing isoparameters on planes is enabled.
        if <forUIsos> = False,
        """

    @overload
    def IsoOnTriangulation(self, theIsEnabled: bool, theObject: AIS_InteractiveObject | None) -> None:
        """
        Enables or disables on-triangulation build for isolines for a particular object.
        In case if on-triangulation builder is disabled, default on-plane builder will compute
        isolines for the object given.
        """

    @overload
    def IsoOnTriangulation(self, theToSwitchOn: bool) -> None:
        """
        Enables or disables on-triangulation build for isolines for default drawer.
        In case if on-triangulation builder is disabled, default on-plane builder will compute
        isolines for the object given.
        """

    @overload
    def IsoOnTriangulation(self) -> bool:
        """
        Returns true if drawing isolines on triangulation algorithm is enabled.
        """

    def Hilight(self, theObj: AIS_InteractiveObject | None, theIsToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Deprecated method Hilight()

        Updates the display in the viewer to take dynamic detection into account.
        On dynamic detection by the mouse cursor, sensitive primitives are highlighted.
        The highlight color of entities detected by mouse movement is white by default.
        """

    def SetSelectedAspect(self, theAspect: nanoocp.Prs3d.Prs3d_BasicAspect | None, theToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Deprecated method - presentation attributes should be assigned directly to object

        Sets the graphic basic aspect to the current presentation of ALL selected objects.
        """

    @overload
    def ShiftSelect(self, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectDetected() taking AIS_SelectionScheme_XOR should be called instead

        Adds the last detected to the list of previous picked.
        If the last detected was already declared as picked, removes it from the Picked List.
        @sa MoveTo().
        """

    @overload
    def ShiftSelect(self, thePolyline: nanoocp.NCollection.NCollection_Array1[nanoocp.gp.gp_Pnt2d], theView: nanoocp.V3d.V3d_View | None, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectPolygon() taking AIS_SelectionScheme_XOR should be called instead

        Adds the last detected to the list of previous picked.
        If the last detected was already declared as picked, removes it from the Picked List.
        """

    @overload
    def ShiftSelect(self, theXPMin: int, theYPMin: int, theXPMax: int, theYPMax: int, theView: nanoocp.V3d.V3d_View | None, theToUpdateViewer: bool) -> AIS_StatusOfPick:
        """
        Deprecated in OCCT: This method is deprecated - SelectRectangle() taking AIS_SelectionScheme_XOR should be called instead

        Rectangle of selection; adds new detected entities into the picked list,
        removes the detected entities that were already stored.
        """

    def SetCurrentObject(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Updates the view of the current object in open context.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def AddOrRemoveCurrentObject(self, theObj: AIS_InteractiveObject | None, theIsToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Allows to add or remove the object given to the list of current and highlight/unhighlight it
        correspondingly. Is valid for global context only; for local context use method
        AddOrRemoveSelected. Since this method makes sense only for neutral point selection of a whole
        object, if 0 selection of the object is empty this method simply does nothing.
        """

    def UpdateCurrent(self) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Updates the list of current objects, i.e. hilights new current objects, removes hilighting
        from former current objects. Objects selected when there is no open local context are called
        current objects; those selected in open local context, selected objects.
        """

    def IsCurrent(self, theObject: AIS_InteractiveObject | None) -> bool:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Returns true if there is a non-null interactive object in Neutral Point.
        Objects selected when there is no open local context are called current objects;
        those selected in open local context, selected objects.
        """

    def InitCurrent(self) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Initializes a scan of the current selected objects in Neutral Point.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def MoreCurrent(self) -> bool:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Returns true if there is another object found by the scan of the list of current objects.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def NextCurrent(self) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Continues the scan to the next object in the list of current objects.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def Current(self) -> AIS_InteractiveObject:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Returns the current interactive object.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def NbCurrents(self) -> int:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context
        """

    def HilightCurrents(self, theToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Highlights current objects.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def UnhilightCurrents(self, theToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Removes highlighting from current objects.
        Objects selected when there is no open local context are called current objects; those
        selected in open local context, selected objects.
        """

    def ClearCurrents(self, theToUpdateViewer: bool) -> None:
        """
        Deprecated in OCCT: Local Context is deprecated - local selection should be used without Local Context

        Empties previous current objects in order to get the current objects detected by the selector
        using UpdateCurrent. Objects selected when there is no open local context are called current
        objects; those selected in open local context, selected objects.
        """

    def DetectedCurrentShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Deprecated in OCCT: Local Context is deprecated - ::DetectedCurrentOwner() should be called instead

        @return current mouse-detected shape or empty (null) shape, if current interactive object
        is not a shape (AIS_Shape) or there is no current mouse-detected interactive object at all.
        @sa DetectedCurrentOwner(), InitDetected(), MoreDetected(), NextDetected().
        """

    def DetectedCurrentObject(self) -> AIS_InteractiveObject:
        """
        Deprecated in OCCT: Local Context is deprecated - ::DetectedCurrentOwner() should be called instead

        @return current mouse-detected interactive object or null object, if there is no currently
        detected interactives
        @sa DetectedCurrentOwner(), InitDetected(), MoreDetected(), NextDetected().
        """

    def SubIntensityColor(self) -> nanoocp.Quantity.Quantity_Color:
        """
        @name sub-intensity management (deprecated)
        Sub-intensity allows temporary highlighting of particular objects with specified color in a
        manner of selection highlight, but without actual selection (e.g., global status and owner's
        selection state will not be updated). The method returns the color of such highlighting. By
        default, it is Quantity_NOC_GRAY40.
        """

    def SetSubIntensityColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sub-intensity allows temporary highlighting of particular objects with specified color in a
        manner of selection highlight, but without actual selection (e.g., global status and owner's
        selection state will not be updated). The method sets up the color for such highlighting. By
        default, this is Quantity_NOC_GRAY40.
        """

    def SubIntensityOn(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Highlights, and removes highlights from, the displayed object which is displayed at Neutral
        Point with subintensity color. Available only for active local context. There is no effect if
        there is no local context. If a local context is open, the presentation of the Interactive
        Object activates the selection mode.
        """

    def SubIntensityOff(self, theIObj: AIS_InteractiveObject | None, theToUpdateViewer: bool) -> None:
        """
        Removes the subintensity option for the entity.
        If a local context is open, the presentation of the Interactive Object activates the selection
        mode.
        """

    def Selection(self) -> AIS_Selection:
        """Returns selection instance"""

    def SetSelection(self, theSelection: AIS_Selection | None) -> None:
        """
        Sets selection instance to manipulate a container of selected owners
        @param theSelection an instance of the selection
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class AIS_BaseAnimationObject(AIS_Animation):
    """Animation defining object transformation."""

    def __init__(self, theOther: AIS_BaseAnimationObject) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_AnimationAxisRotation(AIS_BaseAnimationObject):
    """Animation defining object transformation."""

    @overload
    def __init__(self, theAnimationName: nanoocp.TCollection.TCollection_AsciiString, theContext: AIS_InteractiveContext | None, theObject: AIS_InteractiveObject | None, theAxis: nanoocp.gp.gp_Ax1, theAngleStart: float, theAngleEnd: float) -> None:
        """
        Constructor with initialization.
        @param[in] theAnimationName animation identifier
        @param[in] theContext       interactive context where object have been displayed
        @param[in] theObject        object to apply rotation
        @param[in] theAxis          rotation axis
        @param[in] theAngleStart    rotation angle at the start of animation
        @param[in] theAngleEnd      rotation angle at the end   of animation
        """

    @overload
    def __init__(self, theOther: AIS_AnimationAxisRotation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_AnimationCamera(AIS_Animation):
    """Camera animation."""

    @overload
    def __init__(self, theAnimationName: nanoocp.TCollection.TCollection_AsciiString, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: AIS_AnimationCamera) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def View(self) -> nanoocp.V3d.V3d_View:
        """Return the target view."""

    def SetView(self, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Set target view."""

    def CameraStart(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Return camera start position."""

    def SetCameraStart(self, theCameraStart: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Define camera start position."""

    def CameraEnd(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Return camera end position."""

    def SetCameraEnd(self, theCameraEnd: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Define camera end position."""

class AIS_AnimationObject(AIS_BaseAnimationObject):
    """Animation defining object transformation."""

    @overload
    def __init__(self, theAnimationName: nanoocp.TCollection.TCollection_AsciiString, theContext: AIS_InteractiveContext | None, theObject: AIS_InteractiveObject | None, theTrsfStart: nanoocp.gp.gp_Trsf, theTrsfEnd: nanoocp.gp.gp_Trsf) -> None:
        """
        Constructor with initialization.
        Note that start/end transformations specify exactly local transformation of the object,
        not the transformation to be applied to existing local transformation.
        @param[in] theAnimationName animation identifier
        @param[in] theContext       interactive context where object have been displayed
        @param[in] theObject        object to apply local transformation
        @param[in] theTrsfStart     local transformation at the start of animation (e.g.
        theObject->LocalTransformation())
        @param[in] theTrsfEnd       local transformation at the end   of animation
        """

    @overload
    def __init__(self, theOther: AIS_AnimationObject) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_AttributeFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    Selects Interactive Objects, which have the desired width or color.
    The filter questions each Interactive Object in local
    context to determine whether it has an non-null
    owner, and if so, whether it has the required color
    and width attributes. If the object returns true in each
    case, it is kept. If not, it is rejected.
    This filter is used only in an open local context.
    In the Collector viewer, you can only locate
    Interactive Objects, which answer positively to the
    filters, which are in position when a local context is open.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty attribute filter object.
        This filter object determines whether selectable
        interactive objects have a non-null owner.
        """

    @overload
    def __init__(self, aCol: nanoocp.Quantity.Quantity_NameOfColor) -> None:
        """
        Constructs an attribute filter object defined by the
        color attribute aCol.
        """

    @overload
    def __init__(self, aWidth: float) -> None:
        """
        Constructs an attribute filter object defined by the line
        width attribute aWidth.
        """

    @overload
    def __init__(self, theOther: AIS_AttributeFilter) -> None: ...

    def HasColor(self) -> bool:
        """
        Indicates that the Interactive Object has the color
        setting specified by the argument aCol at construction time.
        """

    def HasWidth(self) -> bool:
        """
        Indicates that the Interactive Object has the width
        setting specified by the argument aWidth at
        construction time.
        """

    def SetColor(self, theCol: nanoocp.Quantity.Quantity_NameOfColor) -> None:
        """Sets the color."""

    def SetWidth(self, theWidth: float) -> None:
        """Sets the line width."""

    def UnsetColor(self) -> None:
        """Removes the setting for color from the filter."""

    def UnsetWidth(self) -> None:
        """Removes the setting for width from the filter."""

    def IsOk(self, anObj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """
        Indicates that the selected Interactive Object passes
        the filter. The owner, anObj, can be either direct or
        user. A direct owner is the corresponding
        construction element, whereas a user is the
        compound shape of which the entity forms a part.
        If the Interactive Object returns true
        when detected by the Local Context selector through
        the mouse, the object is kept; if not, it is rejected.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_Axis(AIS_InteractiveObject):
    """
    Locates the x, y and z axes in an Interactive Object.
    These are used to orient it correctly in presentations
    from different viewpoints, or to construct a revolved
    shape, for example, from one of the axes. Conversely,
    an axis can be created to build a revolved shape and
    then situated relative to one of the axes of the view.
    """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Line | None) -> None:
        """Initializes the line aComponent"""

    @overload
    def __init__(self, anAxis: nanoocp.Geom.Geom_Axis1Placement | None) -> None:
        """Initializes the axis1 position anAxis."""

    @overload
    def __init__(self, theAxis: nanoocp.gp.gp_Ax1, theLength: float = -1.0) -> None:
        """
        Initializes the ray as axis with start point and direction
        @param[in] theAxis Start point and direction of the ray
        @param[in] theLength Optional length of the ray (ray is infinite by default).
        """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Axis2Placement | None, anAxisType: AIS_TypeOfAxis) -> None:
        """
        initializes the axis2 position
        aComponent. The coordinate system used is right-handed.
        """

    @overload
    def __init__(self, theOther: AIS_Axis) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Component(self) -> nanoocp.Geom.Geom_Line:
        """
        Returns the axis entity aComponent and identifies it
        as a component of a shape.
        """

    def SetComponent(self, aComponent: nanoocp.Geom.Geom_Line | None) -> None:
        """Sets the coordinates of the lin aComponent."""

    def Axis2Placement(self) -> nanoocp.Geom.Geom_Axis2Placement:
        """
        Returns the position of axis2 and positions it by
        identifying it as the x, y, or z axis and giving its
        direction in 3D space. The coordinate system used is right-handed.
        """

    def SetAxis2Placement(self, aComponent: nanoocp.Geom.Geom_Axis2Placement | None, anAxisType: AIS_TypeOfAxis) -> None:
        """
        Allows you to provide settings for aComponent:the
        position and direction of an axis in 3D space. The
        coordinate system used is right-handed.
        """

    def SetAxis1Placement(self, anAxis: nanoocp.Geom.Geom_Axis1Placement | None) -> None:
        """Constructs a new line to serve as the axis anAxis in 3D space."""

    def TypeOfAxis(self) -> AIS_TypeOfAxis:
        """Returns the type of axis."""

    def SetTypeOfAxis(self, theTypeAxis: AIS_TypeOfAxis) -> None:
        """
        Constructs the entity theTypeAxis to stock information
        concerning type of axis.
        """

    def IsXYZAxis(self) -> bool:
        """
        Returns a signature of 2 for axis datums. When you
        activate mode 2 by a signature, you pick AIS objects
        of type AIS_Axis.
        """

    def AcceptDisplayMode(self, aMode: int) -> bool:
        """Returns true if the interactive object accepts the display mode aMode."""

    def Signature(self) -> int: ...

    def Type(self) -> AIS_KindOfInteractive: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def SetWidth(self, aValue: float) -> None: ...

    def SetDisplayAspect(self, theNewDatumAspect: nanoocp.Prs3d.Prs3d_LineAspect | None) -> None:
        """Set required visualization parameters."""

    def UnsetColor(self) -> None: ...

    def UnsetWidth(self) -> None: ...

class AIS_BadEdgeFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """A Class"""

    @overload
    def __init__(self) -> None:
        """Constructs an empty filter object for bad edges."""

    @overload
    def __init__(self, theOther: AIS_BadEdgeFilter) -> None: ...

    def ActsOn(self, aType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

    def IsOk(self, EO: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    def SetContour(self, Index: int) -> None:
        """sets <myContour> with current contour. used by IsOk."""

    def AddEdge(self, anEdge: nanoocp.TopoDS.TopoDS_Edge, Index: int) -> None:
        """Adds an edge to the list of non-selectable edges."""

    def RemoveEdges(self, Index: int) -> None:
        """
        removes from the list of non-selectable edges
        all edges in the contour <Index>.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_C0RegularityFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    @overload
    def __init__(self, aShape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @overload
    def __init__(self, theOther: AIS_C0RegularityFilter) -> None: ...

    def ActsOn(self, aType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> bool: ...

    def IsOk(self, EO: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_CameraFrustum(AIS_InteractiveObject):
    """
    Presentation for drawing camera frustum.
    Default configuration is built with filling and some transparency.
    """

    @overload
    def __init__(self) -> None:
        """Constructs camera frustum with default configuration."""

    @overload
    def __init__(self, theOther: AIS_CameraFrustum) -> None: ...

    class SelectionMode(enum.IntEnum):
        """Selection modes supported by this object"""

        SelectionMode_Edges = 0

        SelectionMode_Volume = 1

    SelectionMode_Edges: AIS_CameraFrustum.SelectionMode = SelectionMode.SelectionMode_Edges

    SelectionMode_Volume: AIS_CameraFrustum.SelectionMode = SelectionMode.SelectionMode_Volume

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetCameraFrustum(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Sets camera frustum."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Setup custom color."""

    def UnsetColor(self) -> None:
        """Restore default color."""

    def UnsetTransparency(self) -> None:
        """Restore transparency setting."""

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """Return true if specified display mode is supported."""

class AIS_Circle(AIS_InteractiveObject):
    """
    Constructs circle datums to be used in construction of
    composite shapes.
    """

    @overload
    def __init__(self, aCircle: nanoocp.Geom.Geom_Circle | None) -> None:
        """
        Initializes this algorithm for constructing AIS circle
        datums initializes the circle aCircle
        """

    @overload
    def __init__(self, theCircle: nanoocp.Geom.Geom_Circle | None, theUStart: float, theUEnd: float, theIsFilledCircleSens: bool = False) -> None:
        """
        Initializes this algorithm for constructing AIS circle datums.
        Initializes the circle theCircle, the arc
        starting point theUStart, the arc ending point theUEnd,
        and the type of sensitivity theIsFilledCircleSens.
        """

    @overload
    def __init__(self, theOther: AIS_Circle) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Signature(self) -> int:
        """Returns index 6 by default."""

    def Type(self) -> AIS_KindOfInteractive:
        """Indicates that the type of Interactive Object is a datum."""

    def Circle(self) -> nanoocp.Geom.Geom_Circle:
        """Returns the circle component defined in SetCircle."""

    def Parameters(self) -> tuple[float, float]:
        """
        Constructs instances of the starting point and the end
        point parameters, theU1 and theU2.
        """

    def SetCircle(self, theCircle: nanoocp.Geom.Geom_Circle | None) -> None:
        """Allows you to provide settings for the circle datum aCircle."""

    def SetFirstParam(self, theU: float) -> None:
        """Allows you to set the parameter theU for the starting point of an arc."""

    def SetLastParam(self, theU: float) -> None:
        """Allows you to provide the parameter theU for the end point of an arc."""

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def SetWidth(self, aValue: float) -> None:
        """
        Assigns the width aValue to the solid line boundary of the circle datum.
        """

    def UnsetColor(self) -> None:
        """Removes color from the solid line boundary of the circle datum."""

    def UnsetWidth(self) -> None:
        """
        Removes width settings from the solid line boundary of the circle datum.
        """

    def IsFilledCircleSens(self) -> bool:
        """Returns the type of sensitivity for the circle;"""

    def SetFilledCircleSens(self, theIsFilledCircleSens: bool) -> None:
        """
        Sets the type of sensitivity for the circle. If theIsFilledCircleSens set to true
        then the whole circle will be detectable, otherwise only the boundary of the circle.
        """

class AIS_ColoredDrawer(nanoocp.Prs3d.Prs3d_Drawer):
    """Customizable properties."""

    @overload
    def __init__(self, theLink: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: AIS_ColoredDrawer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsHidden(self) -> bool: ...

    def SetHidden(self, theToHide: bool) -> None: ...

    def HasOwnMaterial(self) -> bool: ...

    def UnsetOwnMaterial(self) -> None: ...

    def SetOwnMaterial(self) -> None: ...

    def HasOwnColor(self) -> bool: ...

    def UnsetOwnColor(self) -> None: ...

    def SetOwnColor(self, arg0: nanoocp.Quantity.Quantity_Color) -> None: ...

    def HasOwnTransparency(self) -> bool: ...

    def UnsetOwnTransparency(self) -> None: ...

    def SetOwnTransparency(self, arg0: float) -> None: ...

    def HasOwnWidth(self) -> bool: ...

    def UnsetOwnWidth(self) -> None: ...

    def SetOwnWidth(self, arg0: float) -> None: ...

    @property
    def myIsHidden(self) -> bool:
        """@name list of overridden properties"""

    @myIsHidden.setter
    def myIsHidden(self, arg: bool, /) -> None: ...

    @property
    def myHasOwnMaterial(self) -> bool: ...

    @myHasOwnMaterial.setter
    def myHasOwnMaterial(self, arg: bool, /) -> None: ...

    @property
    def myHasOwnColor(self) -> bool: ...

    @myHasOwnColor.setter
    def myHasOwnColor(self, arg: bool, /) -> None: ...

    @property
    def myHasOwnTransp(self) -> bool: ...

    @myHasOwnTransp.setter
    def myHasOwnTransp(self, arg: bool, /) -> None: ...

    @property
    def myHasOwnWidth(self) -> bool: ...

    @myHasOwnWidth.setter
    def myHasOwnWidth(self, arg: bool, /) -> None: ...

class AIS_Shape(AIS_InteractiveObject):
    """
    A framework to manage presentation and selection of shapes.
    AIS_Shape is the interactive object which is used the
    most by applications. There are standard functions
    available which allow you to prepare selection
    operations on the constituent elements of shapes -
    vertices, edges, faces etc - in an open local context.
    The selection modes specific to "Shape" type objects
    are referred to as Standard Activation Mode. These
    modes are only taken into account in open local
    context and only act on Interactive Objects which
    have redefined the virtual method
    AcceptShapeDecomposition so that it returns true.
    Several advanced functions are also available. These
    include functions to manage deviation angle and
    deviation coefficient - both HLR and non-HLR - of
    an inheriting shape class. These services allow you to
    select one type of shape interactive object for higher
    precision drawing. When you do this, the
    Prs3d_Drawer::IsOwn... functions corresponding to the
    above deviation angle and coefficient functions return
    true indicating that there is a local setting available
    for the specific object.

    This class allows to map textures on shapes using native UV parametric space of underlying
    surface of each Face (this means that texture will be visually duplicated on all Faces). To
    generate texture coordinates, appropriate shading attribute should be set before computing
    presentation in AIS_Shaded display mode:
    @code
    occ::handle<AIS_Shape> aPrs = new AIS_Shape();
    aPrs->Attributes()->SetupOwnShadingAspect();
    aPrs->Attributes()->ShadingAspect()->Aspect()->SetTextureMapOn();
    aPrs->Attributes()->ShadingAspect()->Aspect()->SetTextureMap (new Graphic3d_Texture2D
    (Graphic3d_NOT_2D_ALUMINUM));
    @endcode
    The texture itself is parametrized in (0,1)x(0,1).
    """

    @overload
    def __init__(self, shap: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Initializes construction of the shape shap from wires,
        edges and vertices.
        """

    @overload
    def __init__(self, theOther: AIS_Shape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Signature(self) -> int:
        """Returns index 0. This value refers to SHAPE from TopAbs_ShapeEnum"""

    def Type(self) -> AIS_KindOfInteractive:
        """Returns Object as the type of Interactive Object."""

    def AcceptShapeDecomposition(self) -> bool:
        """Returns true if the Interactive Object accepts shape decomposition."""

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """Return true if specified display mode is supported."""

    def Shape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns this shape object."""

    def SetShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Constructs an instance of the shape object theShape."""

    def Set(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Alias for ::SetShape()."""

    @overload
    def SetOwnDeviationCoefficient(self) -> bool: ...

    @overload
    def SetOwnDeviationCoefficient(self, aCoefficient: float) -> None:
        """Sets a local value for deviation coefficient for this specific shape."""

    @overload
    def SetOwnDeviationAngle(self) -> bool:
        """Sets a local value for deviation angle for this specific shape."""

    @overload
    def SetOwnDeviationAngle(self, anAngle: float) -> None:
        """
        sets myOwnDeviationAngle field in Prs3d_Drawer & recomputes presentation
        """

    def SetAngleAndDeviation(self, anAngle: float) -> None:
        """
        this compute a new angle and Deviation from the value anAngle
        and set the values stored in myDrawer with these that become local to the shape
        """

    def UserAngle(self) -> float:
        """gives back the angle initial value put by the User."""

    def OwnDeviationCoefficient(self) -> tuple[bool, float, float]:
        """
        Returns true and the values of the deviation
        coefficient aCoefficient and the previous deviation
        coefficient aPreviousCoefficient. If these values are
        not already set, false is returned.
        """

    def OwnDeviationAngle(self) -> tuple[bool, float, float]:
        """
        Returns true and the values of the deviation angle
        anAngle and the previous deviation angle aPreviousAngle.
        If these values are not already set, false is returned.
        """

    def SetTypeOfHLR(self, theTypeOfHLR: nanoocp.Prs3d.Prs3d_TypeOfHLR) -> None:
        """Sets the type of HLR algorithm used by the shape"""

    def TypeOfHLR(self) -> nanoocp.Prs3d.Prs3d_TypeOfHLR:
        """Gets the type of HLR algorithm"""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets the color aColor in the reconstructed
        compound shape. Acts via the Drawer methods below on the appearance of:
        -   free boundaries:
        Prs3d_Drawer_FreeBoundaryAspect,
        -   isos: Prs3d_Drawer_UIsoAspect,
        Prs3dDrawer_VIsoAspect,
        -   shared boundaries:
        Prs3d_Drawer_UnFreeBoundaryAspect,
        -   shading: Prs3d_Drawer_ShadingAspect,
        -   visible line color in hidden line mode:
        Prs3d_Drawer_SeenLineAspect
        -   hidden line color in hidden line mode:
        Prs3d_Drawer_HiddenLineAspect.
        """

    def UnsetColor(self) -> None:
        """Removes settings for color in the reconstructed compound shape."""

    def SetWidth(self, aValue: float) -> None:
        """
        Sets the value aValue for line width in the reconstructed compound shape.
        Changes line aspects for lines presentation.
        """

    def UnsetWidth(self) -> None:
        """
        Removes the setting for line width in the reconstructed compound shape.
        """

    def SetMaterial(self, aName: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """
        Allows you to provide settings for the material aName
        in the reconstructed compound shape.
        """

    def UnsetMaterial(self) -> None:
        """Removes settings for material in the reconstructed compound shape."""

    def SetTransparency(self, aValue: float = 0.6) -> None:
        """
        Sets the value aValue for transparency in the reconstructed compound shape.
        """

    def UnsetTransparency(self) -> None:
        """
        Removes the setting for transparency in the reconstructed compound shape.
        """

    @overload
    def BoundingBox(self) -> nanoocp.Bnd.Bnd_Box:
        """
        Constructs a bounding box with which to reconstruct
        compound topological shapes for presentation.
        """

    @overload
    def BoundingBox(self, theBndBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Returns bounding box of object correspondingly to its current display mode.
        This method requires presentation to be already computed, since it relies on bounding box of
        presentation structures, which are supposed to be same/close amongst different display modes
        of this object.
        """

    def Color(self, aColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Returns the Color attributes of the shape accordingly to
        the current facing model;
        """

    def Material(self) -> nanoocp.Graphic3d.Graphic3d_NameOfMaterial:
        """
        Returns the NameOfMaterial attributes of the shape accordingly to
        the current facing model;
        """

    def Transparency(self) -> float:
        """
        Returns the transparency attributes of the shape accordingly to
        the current facing model;
        """

    @staticmethod
    def SelectionType(theSelMode: int) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Return shape type for specified selection mode."""

    @staticmethod
    def SelectionMode(theShapeType: nanoocp.TopAbs.TopAbs_ShapeEnum) -> int:
        """Return selection mode for specified shape type."""

    def TextureRepeatUV(self) -> nanoocp.gp.gp_Pnt2d:
        """
        @name methods to alter texture mapping properties
        Return texture repeat UV values; (1, 1) by default.
        """

    def SetTextureRepeatUV(self, theRepeatUV: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Sets the number of occurrences of the texture on each face. The texture itself is
        parameterized in (0,1) by (0,1). Each face of the shape to be textured is parameterized in UV
        space (Umin,Umax) by (Vmin,Vmax).
        """

    def TextureOriginUV(self) -> nanoocp.gp.gp_Pnt2d:
        """Return texture origin UV position; (0, 0) by default."""

    def SetTextureOriginUV(self, theOriginUV: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Use this method to change the origin of the texture.
        The texel (0,0) will be mapped to the surface (myUVOrigin.X(), myUVOrigin.Y()).
        """

    def TextureScaleUV(self) -> nanoocp.gp.gp_Pnt2d:
        """Return scale factor for UV coordinates; (1, 1) by default."""

    def SetTextureScaleUV(self, theScaleUV: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Use this method to scale the texture (percent of the face).
        You can specify a scale factor for both U and V.
        Example: if you set ScaleU and ScaleV to 0.5 and you enable texture repeat,
        the texture will appear twice on the face in each direction.
        """

    @staticmethod
    def computeHlrPresentation(theProjector: nanoocp.Graphic3d.Graphic3d_Camera | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> None:
        """Compute HLR presentation for specified shape."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class AIS_ColoredShape(AIS_Shape):
    """Presentation of the shape with customizable sub-shapes properties."""

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theShape: AIS_Shape | None) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theOther: AIS_ColoredShape) -> None: ...

    def CustomAspects(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> AIS_ColoredDrawer:
        """
        @name sub-shape aspects
        Customize properties of specified sub-shape.
        The shape will be stored in the map but ignored, if it is not sub-shape of main Shape!
        This method can be used to mark sub-shapes with customizable properties.
        """

    def ClearCustomAspects(self) -> None:
        """Reset the map of custom sub-shape aspects."""

    def UnsetCustomAspects(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theToUnregister: bool = False) -> None:
        """
        Reset custom properties of specified sub-shape.
        @param theToUnregister unregister or not sub-shape from the map
        """

    def SetCustomColor(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Customize color of specified sub-shape"""

    def SetCustomTransparency(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theTransparency: float) -> None:
        """Customize transparency of specified sub-shape"""

    def SetCustomWidth(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theLineWidth: float) -> None:
        """Customize line width of specified sub-shape"""

    def CustomAspectsMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.AIS.AIS_ColoredDrawer, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Return the map of custom aspects."""

    def ChangeCustomAspectsMap(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.AIS.AIS_ColoredDrawer, nanoocp.TopTools.TopTools_ShapeMapHasher]:
        """Return the map of custom aspects."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        @name global aspects
        Setup color of entire shape.
        """

    def SetWidth(self, theLineWidth: float) -> None:
        """Setup line width of entire shape."""

    def SetTransparency(self, theValue: float) -> None:
        """Sets transparency value."""

    def SetMaterial(self, theAspect: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """Sets the material aspect."""

    def UnsetTransparency(self) -> None:
        """
        Removes the setting for transparency in the reconstructed compound shape.
        """

    def UnsetWidth(self) -> None:
        """Setup line width of entire shape."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_ColorScale(AIS_InteractiveObject):
    """
    Class for drawing a custom color scale.

    The color scale consists of rectangular color bar (composed of fixed
    number of color intervals), optional labels, and title.
    The labels can be positioned either at the boundaries of the intervals,
    or at the middle of each interval.
    Colors and labels can be either defined automatically or set by the user.
    Automatic labels are calculated from numerical limits of the scale,
    its type (logarithmic or plain), and formatted by specified format string.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: AIS_ColorScale) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    @staticmethod
    def FindColor_s(theValue: float, theMin: float, theMax: float, theColorsCount: int, theColorHlsMin: nanoocp.BVH.BVH_Vec3d, theColorHlsMax: nanoocp.BVH.BVH_Vec3d, theColor: nanoocp.Quantity.Quantity_Color) -> bool: ...

    @overload
    @staticmethod
    def FindColor_s(theValue: float, theMin: float, theMax: float, theColorsCount: int, theColor: nanoocp.Quantity.Quantity_Color) -> bool:
        """
        Calculate color according passed value; returns true if value is in range or false, if isn't
        """

    @staticmethod
    def hueToValidRange(theHue: float) -> float:
        """
        Shift hue into valid range.
        Lightness and Saturation should be specified in valid range [0.0, 1.0],
        however Hue might be given out of Quantity_Color range to specify desired range for
        interpolation.
        """

    def FindColor(self, theValue: float, theColor: nanoocp.Quantity.Quantity_Color) -> bool:
        """
        Calculate color according passed value; returns true if value is in range or false, if isn't
        """

    def GetMin(self) -> float:
        """Returns minimal value of color scale, 0.0 by default."""

    def SetMin(self, theMin: float) -> None:
        """Sets the minimal value of color scale."""

    def GetMax(self) -> float:
        """Returns maximal value of color scale, 1.0 by default."""

    def SetMax(self, theMax: float) -> None:
        """Sets the maximal value of color scale."""

    def GetRange(self) -> tuple[float, float]:
        """
        Returns minimal and maximal values of color scale, 0.0 to 1.0 by default.
        """

    def SetRange(self, theMin: float, theMax: float) -> None:
        """
        Sets the minimal and maximal value of color scale.
        Note that values order will be ignored - the minimum and maximum values will be swapped if
        needed.
        ::SetReversed() should be called to swap displaying order.
        """

    def HueMin(self) -> float:
        """
        Returns the hue angle corresponding to minimum value, 230 by default (blue).
        """

    def HueMax(self) -> float:
        """
        Returns the hue angle corresponding to maximum value, 0 by default (red).
        """

    def HueRange(self) -> tuple[float, float]:
        """
        Returns the hue angle range corresponding to minimum and maximum values, 230 to 0 by default
        (blue to red).
        """

    def SetHueRange(self, theMinAngle: float, theMaxAngle: float) -> None:
        """
        Sets hue angle range corresponding to minimum and maximum values.
        The valid angle range is [0, 360], see Quantity_Color and Quantity_TOC_HLS for more details.
        """

    def ColorRange(self, theMinColor: nanoocp.Quantity.Quantity_Color, theMaxColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Returns color range corresponding to minimum and maximum values, blue to red by default.
        """

    def SetColorRange(self, theMinColor: nanoocp.Quantity.Quantity_Color, theMaxColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color range corresponding to minimum and maximum values."""

    def GetLabelType(self) -> nanoocp.Aspect.Aspect_TypeOfColorScaleData:
        """
        Returns the type of labels, Aspect_TOCSD_AUTO by default.
        Aspect_TOCSD_AUTO - labels as boundary values for intervals
        Aspect_TOCSD_USER - user specified label is used
        """

    def SetLabelType(self, theType: nanoocp.Aspect.Aspect_TypeOfColorScaleData) -> None:
        """
        Sets the type of labels.
        Aspect_TOCSD_AUTO - labels as boundary values for intervals
        Aspect_TOCSD_USER - user specified label is used
        """

    def GetColorType(self) -> nanoocp.Aspect.Aspect_TypeOfColorScaleData:
        """
        Returns the type of colors, Aspect_TOCSD_AUTO by default.
        Aspect_TOCSD_AUTO - value between Red and Blue
        Aspect_TOCSD_USER - user specified color from color map
        """

    def SetColorType(self, theType: nanoocp.Aspect.Aspect_TypeOfColorScaleData) -> None:
        """
        Sets the type of colors.
        Aspect_TOCSD_AUTO - value between Red and Blue
        Aspect_TOCSD_USER - user specified color from color map
        """

    def GetNumberOfIntervals(self) -> int:
        """Returns the number of color scale intervals, 10 by default."""

    def SetNumberOfIntervals(self, theNum: int) -> None:
        """Sets the number of color scale intervals."""

    def GetTitle(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the color scale title string, empty string by default."""

    def SetTitle(self, theTitle: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Sets the color scale title string."""

    def GetFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the format for numbers, "%.4g" by default.
        The same like format for function printf().
        Used if GetLabelType() is TOCSD_AUTO;
        """

    def Format(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the format of text."""

    def SetFormat(self, theFormat: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets the color scale auto label format specification."""

    def GetLabel(self, theIndex: int) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Returns the user specified label with index theIndex.
        Index is in range from 1 to GetNumberOfIntervals() or to
        GetNumberOfIntervals() + 1 if IsLabelAtBorder() is true.
        Returns empty string if label not defined.
        """

    def GetIntervalColor(self, theIndex: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns the user specified color from color map with index (starts at 1).
        Returns default color if index is out of range in color map.
        """

    def SetIntervalColor(self, theColor: nanoocp.Quantity.Quantity_Color, theIndex: int) -> None:
        """
        Sets the color of the specified interval.
        Note that list is automatically resized to include specified index.
        @param theColor color value to set
        @param theIndex index in range [1, GetNumberOfIntervals()];
        appended to the end of list if -1 is specified
        """

    def GetLabels(self, theLabels: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """Returns the user specified labels."""

    def Labels(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]:
        """Returns the user specified labels."""

    def SetLabels(self, theSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_ExtendedString]) -> None:
        """
        Sets the color scale labels.
        The length of the sequence should be equal to GetNumberOfIntervals() or to
        GetNumberOfIntervals() + 1 if IsLabelAtBorder() is true. If length of the sequence does not
        much the number of intervals, then these labels will be considered as "free" and will be
        located at the virtual intervals corresponding to the number of labels (with flag
        IsLabelAtBorder() having the same effect as in normal case).
        """

    @overload
    def GetColors(self, theColors: nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]) -> None: ...

    @overload
    def GetColors(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]:
        """Returns the user specified colors."""

    def SetColors(self, theSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]) -> None:
        """
        Sets the color scale colors.
        The length of the sequence should be equal to GetNumberOfIntervals().
        """

    def SetUniformColors(self, theLightness: float, theHueFrom: float, theHueTo: float) -> None:
        """
        Populates colors scale by colors of the same lightness value in CIE Lch
        color space, distributed by hue, with perceptually uniform differences
        between consequent colors.
        See MakeUniformColors() for description of parameters.
        """

    @staticmethod
    def MakeUniformColors(theNbColors: int, theLightness: float, theHueFrom: float, theHueTo: float) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Quantity.Quantity_Color]:
        """
        Generates sequence of colors of the same lightness value in CIE Lch
        color space (see #Quantity_TOC_CIELch), with hue values in the specified range.
        The colors are distributed across the range such as to have perceptually
        same difference between neighbour colors.
        For each color, maximal chroma value fitting in sRGB gamut is used.

        @param theNbColors - number of colors to generate
        @param theLightness - lightness to be used (0 is black, 100 is white, 32 is
        lightness of pure blue)
        @param theHueFrom - hue value at the start of the scale
        @param theHueTo - hue value defining the end of the scale

        Hue value can be out of the range [0, 360], interpreted as modulo 360.
        The colors of the scale will be in the order of increasing hue if
        theHueTo > theHueFrom, and decreasing otherwise.
        """

    def GetLabelPosition(self) -> nanoocp.Aspect.Aspect_TypeOfColorScalePosition:
        """
        Returns the position of labels concerning color filled rectangles, Aspect_TOCSP_RIGHT by
        default.
        """

    def SetLabelPosition(self, thePos: nanoocp.Aspect.Aspect_TypeOfColorScalePosition) -> None:
        """Sets the color scale labels position relative to color bar."""

    def GetTitlePosition(self) -> nanoocp.Aspect.Aspect_TypeOfColorScalePosition:
        """
        Returns the position of color scale title, Aspect_TOCSP_LEFT by default.
        """

    def SetTitlePosition(self, thePos: nanoocp.Aspect.Aspect_TypeOfColorScalePosition) -> None:
        """
        Deprecated in OCCT: AIS_ColorScale::SetTitlePosition() has no effect!

        Sets the color scale title position.
        """

    def IsReversed(self) -> bool:
        """
        Returns TRUE if the labels and colors used in reversed order, FALSE by default.
        - Normal,   bottom-up order with Minimal value on the Bottom and Maximum value on Top.
        - Reversed, top-down  order with Maximum value on the Bottom and Minimum value on Top.
        """

    def SetReversed(self, theReverse: bool) -> None:
        """Sets true if the labels and colors used in reversed order."""

    def IsSmoothTransition(self) -> bool:
        """
        Return TRUE if color transition between neighbor intervals
        should be linearly interpolated, FALSE by default.
        """

    def SetSmoothTransition(self, theIsSmooth: bool) -> None:
        """Setup smooth color transition."""

    def IsLabelAtBorder(self) -> bool:
        """
        Returns TRUE if the labels are placed at border of color intervals, TRUE by default.
        The automatically generated label will show value exactly on the current position:
        - value connecting two neighbor intervals (TRUE)
        - value in the middle of interval (FALSE)
        """

    def SetLabelAtBorder(self, theOn: bool) -> None:
        """
        Sets true if the labels are placed at border of color intervals (TRUE by default).
        If set to False, labels will be drawn at color intervals rather than at borders.
        """

    def IsLogarithmic(self) -> bool:
        """
        Returns TRUE if the color scale has logarithmic intervals, FALSE by default.
        """

    def SetLogarithmic(self, isLogarithmic: bool) -> None:
        """Sets true if the color scale has logarithmic intervals."""

    def SetLabel(self, theLabel: nanoocp.TCollection.TCollection_ExtendedString, theIndex: int) -> None:
        """
        Sets the color scale label at index.
        Note that list is automatically resized to include specified index.
        @param theLabel new label text
        @param theIndex index in range [1, GetNumberOfIntervals()] or [1, GetNumberOfIntervals() + 1]
        if IsLabelAtBorder() is true;
        label is appended to the end of list if negative index is specified
        """

    def GetSize(self) -> tuple[int, int]:
        """
        Returns the size of color bar, 0 and 0 by default
        (e.g. should be set by user explicitly before displaying).
        """

    def SetSize(self, theBreadth: int, theHeight: int) -> None:
        """Sets the size of color bar."""

    def GetBreadth(self) -> int:
        """
        Returns the breadth of color bar, 0 by default
        (e.g. should be set by user explicitly before displaying).
        """

    def SetBreadth(self, theBreadth: int) -> None:
        """Sets the width of color bar."""

    def GetHeight(self) -> int:
        """
        Returns the height of color bar, 0 by default
        (e.g. should be set by user explicitly before displaying).
        """

    def SetHeight(self, theHeight: int) -> None:
        """Sets the height of color bar."""

    def GetPosition(self) -> tuple[float, float]:
        """Returns the bottom-left position of color scale, 0x0 by default."""

    def SetPosition(self, theX: int, theY: int) -> None:
        """Sets the position of color scale."""

    def GetXPosition(self) -> int:
        """Returns the left position of color scale, 0 by default."""

    def SetXPosition(self, theX: int) -> None:
        """Sets the left position of color scale."""

    def GetYPosition(self) -> int:
        """Returns the bottom position of color scale, 0 by default."""

    def SetYPosition(self, theY: int) -> None:
        """Sets the bottom position of color scale."""

    def GetTextHeight(self) -> int:
        """Returns the font height of text labels, 20 by default."""

    def SetTextHeight(self, theHeight: int) -> None:
        """Sets the height of text of color scale."""

    def TextWidth(self, theText: nanoocp.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns the width of text.
        @param[in] theText  the text of which to calculate width.
        """

    def TextHeight(self, theText: nanoocp.TCollection.TCollection_ExtendedString) -> int:
        """
        Returns the height of text.
        @param[in] theText  the text of which to calculate height.
        """

    def TextSize(self, theText: nanoocp.TCollection.TCollection_ExtendedString, theHeight: int) -> tuple[int, int, int]: ...

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """Return true if specified display mode is supported."""

    def Compute(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theMode: int) -> None:
        """Compute presentation."""

    def ComputeSelection(self, arg0: nanoocp.SelectMgr.SelectMgr_Selection | None, arg1: int) -> None:
        """Compute selection - not implemented for color scale."""

class AIS_ConnectedInteractive(AIS_InteractiveObject):
    """
    Creates an arbitrary located instance of another Interactive Object,
    which serves as a reference.
    This allows you to use the Connected Interactive
    Object without having to recalculate presentation,
    selection or graphic structure. These are deduced
    from your reference object.
    The relation between the connected interactive object
    and its source is generally one of geometric transformation.
    AIS_ConnectedInteractive class supports selection mode 0 for any InteractiveObject and
    all standard modes if its reference based on AIS_Shape.
    Descendants may redefine ComputeSelection() though.
    Also ConnectedInteractive will handle HLR if its reference based on AIS_Shape.
    """

    @overload
    def __init__(self, aTypeOfPresentation3d: nanoocp.PrsMgr.PrsMgr_TypeOfPresentation3d = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView) -> None:
        """
        Disconnects the previous view and sets highlight
        mode to 0. This highlights the wireframe presentation
        aTypeOfPresentation3d.
        Top_AllView deactivates hidden line removal.
        """

    @overload
    def __init__(self, theOther: AIS_ConnectedInteractive) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Type(self) -> AIS_KindOfInteractive:
        """Returns KOI_Object"""

    def Signature(self) -> int:
        """Returns 0"""

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None) -> None:
        """
        Establishes the connection between the Connected
        Interactive Object, anotherIobj, and its reference.
        """

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None, theLocation: nanoocp.gp.gp_Trsf) -> None: ...

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None, theLocation: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """
        Establishes the connection between the Connected
        Interactive Object, anotherIobj, and its reference.
        Locates instance in aLocation.
        """

    def HasConnection(self) -> bool:
        """
        Returns true if there is a connection established
        between the presentation and its source reference.
        """

    def ConnectedTo(self) -> AIS_InteractiveObject:
        """Returns the connection with the reference Interactive Object."""

    def Disconnect(self) -> None:
        """
        Clears the connection with a source reference. The
        presentation will no longer be displayed.
        Warning Must be done before deleting the presentation.
        """

    def AcceptShapeDecomposition(self) -> bool:
        """
        Informs the graphic context that the interactive Object
        may be decomposed into sub-shapes for dynamic selection.
        """

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """Return true if reference presentation accepts specified display mode."""

class AIS_ExclusionFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    A framework to reject or to accept only objects of
    given types and/or signatures.
    Objects are stored, and the stored objects - along
    with the flag settings - are used to define the filter.
    Objects to be filtered are compared with the stored
    objects added to the filter, and are accepted or
    rejected according to the exclusion flag setting.
    -   Exclusion flag on
    -   the function IsOk answers true for all objects,
    except those of the types and signatures stored
    in the filter framework
    -   Exclusion flag off
    -   the function IsOk answers true for all objects
    which have the same type and signature as the stored ones.
    """

    @overload
    def __init__(self, ExclusionFlagOn: bool = True) -> None:
        """
        Constructs an empty exclusion filter object defined by
        the flag setting ExclusionFlagOn.
        By default, the flag is set to true.
        """

    @overload
    def __init__(self, TypeToExclude: AIS_KindOfInteractive, ExclusionFlagOn: bool = True) -> None:
        """
        All the AIS objects of <TypeToExclude>
        Will be rejected by the IsOk Method.
        """

    @overload
    def __init__(self, TypeToExclude: AIS_KindOfInteractive, SignatureInType: int, ExclusionFlagOn: bool = True) -> None:
        """
        Constructs an exclusion filter object defined by the
        enumeration value TypeToExclude, the signature
        SignatureInType, and the flag setting ExclusionFlagOn.
        By default, the flag is set to true.
        """

    @overload
    def __init__(self, theOther: AIS_ExclusionFilter) -> None: ...

    def IsOk(self, anObj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool: ...

    @overload
    def Add(self, TypeToExclude: AIS_KindOfInteractive) -> bool:
        """Adds the type TypeToExclude to the list of types."""

    @overload
    def Add(self, TypeToExclude: AIS_KindOfInteractive, SignatureInType: int) -> bool: ...

    @overload
    def Remove(self, TypeToExclude: AIS_KindOfInteractive) -> bool: ...

    @overload
    def Remove(self, TypeToExclude: AIS_KindOfInteractive, SignatureInType: int) -> bool: ...

    def Clear(self) -> None: ...

    def IsExclusionFlagOn(self) -> bool: ...

    def SetExclusionFlag(self, theStatus: bool) -> None: ...

    def IsStored(self, aType: AIS_KindOfInteractive) -> bool: ...

    def ListOfStoredTypes(self, TheList: nanoocp.NCollection.NCollection_List[int]) -> None: ...

    def ListOfSignature(self, aType: AIS_KindOfInteractive, TheStoredList: nanoocp.NCollection.NCollection_List[int]) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_GraphicTool:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AIS_GraphicTool) -> None: ...

    @overload
    @staticmethod
    def GetLineColor(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, TheTypeOfAttributes: AIS_TypeOfAttribute) -> nanoocp.Quantity.Quantity_NameOfColor: ...

    @overload
    @staticmethod
    def GetLineColor(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, TheTypeOfAttributes: AIS_TypeOfAttribute, TheLineColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @staticmethod
    def GetLineWidth(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, TheTypeOfAttributes: AIS_TypeOfAttribute) -> float: ...

    @staticmethod
    def GetLineType(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, TheTypeOfAttributes: AIS_TypeOfAttribute) -> nanoocp.Aspect.Aspect_TypeOfLine: ...

    @staticmethod
    def GetLineAtt(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, TheTypeOfAttributes: AIS_TypeOfAttribute) -> tuple[nanoocp.Quantity.Quantity_NameOfColor, float, nanoocp.Aspect.Aspect_TypeOfLine]: ...

    @overload
    @staticmethod
    def GetInteriorColor(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> nanoocp.Quantity.Quantity_NameOfColor: ...

    @overload
    @staticmethod
    def GetInteriorColor(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @staticmethod
    def GetMaterial(aDrawer: nanoocp.Prs3d.Prs3d_Drawer | None) -> nanoocp.Graphic3d.Graphic3d_MaterialAspect: ...

class AIS_LightSource(AIS_InteractiveObject):
    """
    Interactive object for a light source.
    Each type of light source has it's own presentation:
    - Ambient light is displayed as a sphere at view corner;
    - Positional light is represented by a sphere or marker;
    - Spot light is represented by a cone;
    - Directional light is represented by a set of arrows at the corner of view.
    In addition, light source name could be displayed, and clicking on presentation will
    enable/disable light.
    """

    @overload
    def __init__(self, theLightSource: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Initializes the light source by copying Graphic3d_CLight settings."""

    @overload
    def __init__(self, theOther: AIS_LightSource) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Light(self) -> nanoocp.Graphic3d.Graphic3d_CLight:
        """Returns the light."""

    def SetLight(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Set the light."""

    def ToDisplayName(self) -> bool:
        """
        @name Light properties
        Returns TRUE if the light source name should be displayed; TRUE by default.
        """

    def SetDisplayName(self, theToDisplay: bool) -> None:
        """Show/hide light source name."""

    def ToDisplayRange(self) -> bool:
        """
        Returns TRUE to display light source range as sphere (positional light) or cone (spot light);
        TRUE by default. Has no effect for non-zoomable presentation.
        """

    def SetDisplayRange(self, theToDisplay: bool) -> None:
        """Show/hide light source range shaded presentation."""

    def Size(self) -> float:
        """Returns the size of presentation; 50 by default."""

    def SetSize(self, theSize: float) -> None:
        """Sets the size of presentation."""

    def ArcSize(self) -> int:
        """Returns Sensitive sphere arc size in pixels; 20 by default."""

    def SetArcSize(self, theSize: int) -> None:
        """Sets the size of sensitive sphere arc."""

    def IsZoomable(self) -> bool:
        """
        Returns TRUE if transform-persistence is allowed;
        TRUE by default for Ambient and Directional lights
        and FALSE by default for Positional and Spot lights.
        """

    def SetZoomable(self, theIsZoomable: bool) -> None:
        """Sets if transform-persistence is allowed."""

    def SetDraggable(self, theIsDraggable: bool) -> None:
        """Sets if dragging is allowed."""

    def ToSwitchOnClick(self) -> bool:
        """Returns TRUE if mouse click will turn light on/off; TRUE by default."""

    def SetSwitchOnClick(self, theToHandle: bool) -> None:
        """Sets if mouse click should turn light on/off."""

    def NbArrows(self) -> int:
        """Returns a number of directional light arrows to display; 5 by default."""

    def SetNbArrows(self, theNbArrows: int) -> None:
        """
        Returns a number of directional light arrows to display (supported values: 1, 3, 5, 9).
        """

    def MarkerImage(self, theIsEnabled: bool) -> nanoocp.Graphic3d.Graphic3d_MarkerImage:
        """
        Returns light source icon.
        @param[in] theIsEnabled  marker index for enabled/disabled light source states
        """

    def MarkerType(self, theIsEnabled: bool) -> nanoocp.Aspect.Aspect_TypeOfMarker:
        """
        Returns light source icon.
        @param[in] theIsEnabled  marker index for enabled/disabled light source states
        """

    def SetMarkerImage(self, theImage: nanoocp.Graphic3d.Graphic3d_MarkerImage | None, theIsEnabled: bool) -> None:
        """Sets custom icon to light source."""

    def SetMarkerType(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker, theIsEnabled: bool) -> None:
        """Sets standard icon to light source."""

    def NbSplitsQuadric(self) -> int:
        """Returns tessellation level for quadric surfaces; 30 by default."""

    def SetNbSplitsQuadric(self, theNbSplits: int) -> None:
        """Sets tessellation level for quadric surfaces."""

    def NbSplitsArrow(self) -> int:
        """Returns tessellation level for arrows; 20 by default."""

    def SetNbSplitsArrow(self, theNbSplits: int) -> None:
        """Sets tessellation level for arrows."""

    def Type(self) -> AIS_KindOfInteractive:
        """Returns kind of the object."""

class AIS_LightSourceOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """Owner of AIS_LightSource presentation."""

    @overload
    def __init__(self, theObject: AIS_LightSource | None, thePriority: int = 5) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: AIS_LightSourceOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HandleMouseClick(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsDoubleClick: bool) -> bool:
        """Handle mouse button click event."""

    def HilightWithColor(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None:
        """
        Highlights selectable object's presentation with display mode in presentation manager with
        given highlight style. Also a check for auto-highlight is performed - if selectable object
        manages highlighting on its own, execution will be passed to
        SelectMgr_SelectableObject::HilightOwnerWithColor method.
        """

    def IsForcedHilight(self) -> bool:
        """Always update dynamic highlighting."""

class AIS_Line(AIS_InteractiveObject):
    """
    Constructs line datums to be used in construction of
    composite shapes.
    """

    @overload
    def __init__(self, aLine: nanoocp.Geom.Geom_Line | None) -> None:
        """Initializes the line aLine."""

    @overload
    def __init__(self, aStartPoint: nanoocp.Geom.Geom_Point | None, aEndPoint: nanoocp.Geom.Geom_Point | None) -> None:
        """
        Initializes a starting point aStartPoint
        and a finishing point aEndPoint for the line.
        """

    @overload
    def __init__(self, theOther: AIS_Line) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Signature(self) -> int:
        """Returns the signature 5."""

    def Type(self) -> AIS_KindOfInteractive:
        """Returns the type Datum."""

    def Line(self) -> nanoocp.Geom.Geom_Line:
        """Constructs an infinite line."""

    def StartPoint(self) -> nanoocp.Geom.Geom_Point:
        """
        Returns the starting point of the line set by SetPoints.
        @return handle to the start point
        """

    def EndPoint(self) -> nanoocp.Geom.Geom_Point:
        """
        Returns the end point of the line set by SetPoints.
        @return handle to the end point
        """

    def Points(self) -> tuple[nanoocp.Geom.Geom_Point, nanoocp.Geom.Geom_Point]:
        """
        Deprecated in OCCT: Use StartPoint() and EndPoint() instead

        Returns the starting point thePStart and the end point thePEnd of the line set by SetPoints.
        @deprecated Use StartPoint() and EndPoint() instead.
        """

    def SetLine(self, theLine: nanoocp.Geom.Geom_Line | None) -> None:
        """
        Sets the infinite line.
        @param[in] theLine the geometric line
        """

    def SetPoints(self, thePStart: nanoocp.Geom.Geom_Point | None, thePEnd: nanoocp.Geom.Geom_Point | None) -> None:
        """
        Sets the starting point and ending point of the
        infinite line to create a finite line segment.
        @param[in] thePStart the starting point
        @param[in] thePEnd the ending point
        """

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Provides a new color setting aColor for the line in the drawing tool, or "Drawer".
        """

    def SetWidth(self, aValue: float) -> None:
        """
        Provides the new width setting aValue for the line in
        the drawing tool, or "Drawer".
        """

    def UnsetColor(self) -> None:
        """Removes the color setting and returns the original color."""

    def UnsetWidth(self) -> None:
        """Removes the width setting and returns the original width."""

class AIS_Manipulator(AIS_InteractiveObject):
    """
    Interactive object class to manipulate local transformation of another interactive
    object or a group of objects via mouse.
    It manages three types of manipulations in 3D space:
    - translation through axis
    - scaling within axis
    - rotation around axis
    To enable one of this modes, selection mode (from 1 to 3) is to be activated.
    There are three orthogonal transformation axes defined by position property of
    the manipulator. Particular transformation mode can be disabled for each
    of the axes or all of them. Furthermore each of the axes can be hidden or
    made visible.
    The following steps demonstrate how to attach, configure and use manipulator
    for an interactive object:
    Step 1. Create manipulator object and adjust it appearance:
    @code
    occ::handle<AIS_Manipulator> aManipulator = new AIS_Manipulator();
    aManipulator->SetPart (0, AIS_Manipulator::Scaling, false);
    aManipulator->SetPart (1, AIS_Manipulator::Rotation, false);
    // Attach manipulator to already displayed object and manage manipulation modes
    aManipulator->AttachToObject (anAISObject);
    aManipulator->EnableMode (AIS_Manipulator::Translation);
    aManipulator->EnableMode (AIS_Manipulator::Rotation);
    aManipulator->EnableMode (AIS_Manipulator::Scaling);
    @endcode
    Note that you can enable only one manipulation mode but have all visual parts displayed.
    This code allows you to view manipulator and select its manipulation parts.
    Note that manipulator activates mode on part selection.
    If this mode is activated, no selection will be performed for manipulator.
    It can be activated with highlighting. To enable this:
    @code
    aManipulator->SetModeActivationOnDetection (true);
    @endcode
    Step 2. To perform transformation of object use next code in your event processing chain:
    @code
    // catch mouse button down event
    if (aManipulator->HasActiveMode())
    {
    aManipulator->StartTransform (anXPix, anYPix, aV3dView);
    }
    ...
    // or track mouse move event
    if (aManipulator->HasActiveMode())
    {
    aManipulator->Transform (anXPix, anYPix, aV3dView);
    aV3dView->Redraw();
    }
    ...
    // or catch mouse button up event (apply) or escape event (cancel)
    aManipulator->StopTransform(/*bool toApply*/);
    @endcode
    Step 3. To deactivate current manipulation mode use:
    @code aManipulator->DeactivateCurrentMode();
    @endcode
    Step 4. To detach manipulator from object use:
    @code
    aManipulator->Detach();
    @endcode
    The last method erases manipulator object.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a manipulator object with default placement and all parts to be displayed.
        """

    @overload
    def __init__(self, thePosition: nanoocp.gp.gp_Ax2) -> None:
        """
        Constructs a manipulator object with input location and positions of axes and all parts to be
        displayed.
        """

    @overload
    def __init__(self, theOther: AIS_Manipulator) -> None: ...

    class ManipulatorSkin(enum.IntEnum):
        """@name Setters for parameters"""

        ManipulatorSkin_Shaded = 0

        ManipulatorSkin_Flat = 1

    ManipulatorSkin_Shaded: AIS_Manipulator.ManipulatorSkin = ManipulatorSkin.ManipulatorSkin_Shaded

    ManipulatorSkin_Flat: AIS_Manipulator.ManipulatorSkin = ManipulatorSkin.ManipulatorSkin_Flat

    class OptionsForAttach:
        """
        Behavior settings to be applied when performing transformation:
        - FollowTranslation - whether the manipulator will be moved together with an object.
        - FollowRotation - whether the manipulator will be rotated together with an object.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: AIS_Manipulator.OptionsForAttach) -> None: ...

        def SetAdjustPosition(self, theApply: bool) -> AIS_Manipulator.OptionsForAttach: ...

        def SetAdjustSize(self, theApply: bool) -> AIS_Manipulator.OptionsForAttach: ...

        def SetEnableModes(self, theApply: bool) -> AIS_Manipulator.OptionsForAttach: ...

        @property
        def AdjustPosition(self) -> bool: ...

        @AdjustPosition.setter
        def AdjustPosition(self, arg: bool, /) -> None: ...

        @property
        def AdjustSize(self) -> bool: ...

        @AdjustSize.setter
        def AdjustSize(self, arg: bool, /) -> None: ...

        @property
        def EnableModes(self) -> bool: ...

        @EnableModes.setter
        def EnableModes(self, arg: bool, /) -> None: ...

    class BehaviorOnTransform:
        """
        Behavior settings to be applied when performing transformation:
        - FollowTranslation - whether the manipulator will be moved together with an object.
        - FollowRotation - whether the manipulator will be rotated together with an object.
        """

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: AIS_Manipulator.BehaviorOnTransform) -> None: ...

        def SetFollowTranslation(self, theApply: bool) -> AIS_Manipulator.BehaviorOnTransform: ...

        def SetFollowRotation(self, theApply: bool) -> AIS_Manipulator.BehaviorOnTransform: ...

        def SetFollowDragging(self, theApply: bool) -> AIS_Manipulator.BehaviorOnTransform: ...

        @property
        def FollowTranslation(self) -> bool: ...

        @FollowTranslation.setter
        def FollowTranslation(self, arg: bool, /) -> None: ...

        @property
        def FollowRotation(self) -> bool: ...

        @FollowRotation.setter
        def FollowRotation(self, arg: bool, /) -> None: ...

        @property
        def FollowDragging(self) -> bool: ...

        @FollowDragging.setter
        def FollowDragging(self, arg: bool, /) -> None: ...

    @overload
    def SetPart(self, theAxisIndex: int, theMode: AIS_ManipulatorMode, theIsEnabled: bool) -> None:
        """
        Disable or enable visual parts for translation, rotation or scaling for some axis.
        By default all parts are enabled (will be displayed).
        @warning Enabling or disabling of visual parts of manipulator does not manage the manipulation
        (selection) mode.
        @warning Raises program error if axis index is < 0 or > 2.
        """

    @overload
    def SetPart(self, theMode: AIS_ManipulatorMode, theIsEnabled: bool) -> None:
        """
        Disable or enable visual parts for translation, rotation or scaling for ALL axes.
        By default all parts are enabled (will be displayed).
        @warning Enabling or disabling of visual parts of manipulator does not manage the manipulation
        (selection) mode.
        @warning Raises program error if axis index is < 0 or > 2.
        """

    @overload
    def Attach(self, theObject: AIS_InteractiveObject | None, theOptions: AIS_Manipulator.OptionsForAttach = ...) -> None:
        """
        Attaches himself to the input interactive object and become displayed in the same context.
        It is placed in the center of object bounding box, and its size is adjusted to the object
        bounding box.
        """

    @overload
    def Attach(self, theObject: nanoocp.NCollection.NCollection_HSequence[nanoocp.AIS.AIS_InteractiveObject] | None, theOptions: AIS_Manipulator.OptionsForAttach = ...) -> None:
        """
        Attaches himself to the input interactive object group and become displayed in the same
        context. It become attached to the first object, baut manage manipulation of the whole group.
        It is placed in the center of object bounding box, and its size is adjusted to the object
        bounding box.
        """

    def EnableMode(self, theMode: AIS_ManipulatorMode) -> None:
        """
        Enable manipualtion mode.
        @warning It activates selection mode in the current context.
        If manipulator is not displayed, no mode will be activated.
        """

    def SetModeActivationOnDetection(self, theToEnable: bool) -> None:
        """
        Enables mode activation on detection (highlighting).
        By default, mode is activated on selection of manipulator part.
        @warning If this mode is enabled, selection of parts does nothing.
        """

    def IsModeActivationOnDetection(self) -> bool:
        """@return true if manual mode activation is enabled."""

    def ProcessDragging(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theDragFrom: nanoocp.BVH.BVH_Vec2i, theDragTo: nanoocp.BVH.BVH_Vec2i, theAction: AIS_DragAction) -> bool:
        """
        Drag object in the viewer.
        @param[in] theCtx       interactive context
        @param[in] theView      active View
        @param[in] theOwner     the owner of detected entity
        @param[in] theDragFrom  drag start point
        @param[in] theDragTo    drag end point
        @param[in] theAction    drag action
        @return FALSE if object rejects dragging action (e.g. AIS_DragAction_Start)
        """

    def StartTransform(self, theX: int, theY: int, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Init start (reference) transformation.
        @warning It is used in chain with StartTransform-Transform(gp_Trsf)-StopTransform
        and is used only for custom transform set. If Transform(const int, const
        int) is used, initial data is set automatically, and it is reset on
        DeactivateCurrentMode call if it is not reset yet.
        """

    @overload
    def Transform(self, aTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Apply to the owning objects the input transformation.
        @remark The transformation is set using SetLocalTransformation for owning objects.
        The location of the manipulator is stored also in Local Transformation,
        so that there's no need to redisplay objects.
        @warning It is used in chain with StartTransform-Transform(gp_Trsf)-StopTransform
        and is used only for custom transform set.
        @warning It will does nothing if transformation is not initiated (with StartTransform() call).
        """

    @overload
    def Transform(self, theX: int, theY: int, theView: nanoocp.V3d.V3d_View | None) -> nanoocp.gp.gp_Trsf:
        """
        Apply transformation made from mouse moving from start position
        (save on the first Transform() call and reset on DeactivateCurrentMode() call.)
        to the in/out mouse position (theX, theY)
        """

    def RecomputeTransformation(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Apply camera transformation to flat skin manipulator"""

    def RecomputeSelection(self, theMode: AIS_ManipulatorMode) -> None:
        """
        Recomputes sensitive primitives for the given selection mode.
        @param theMode selection mode to recompute sensitive primitives
        """

    def StopTransform(self, theToApply: bool = True) -> None:
        """
        Reset start (reference) transformation.
        @param[in] theToApply  option to apply or to cancel the started transformation.
        @warning It is used in chain with StartTransform-Transform(gp_Trsf)-StopTransform
        and is used only for custom transform set.
        """

    def ObjectTransformation(self, theX: int, theY: int, theView: nanoocp.V3d.V3d_View | None, theTrsf: nanoocp.gp.gp_Trsf) -> bool:
        """
        Computes transformation of parent object according to the active mode and input motion vector.
        You can use this method to get object transformation according to current mode or use own
        algorithm to implement any other transformation for modes.
        @return transformation of parent object.
        """

    def DeactivateCurrentMode(self) -> None:
        """
        Make inactive the current selected manipulator part and reset current axis index and current
        mode. After its call HasActiveMode() returns false.
        @sa HasActiveMode()
        """

    def Detach(self) -> None:
        """
        Detaches himself from the owner object, and removes itself from context.
        """

    def Objects(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.AIS.AIS_InteractiveObject]:
        """@return all owning objects."""

    @overload
    def Object(self) -> AIS_InteractiveObject:
        """@return the first (leading) object of the owning objects."""

    @overload
    def Object(self, theIndex: int) -> AIS_InteractiveObject:
        """
        @return one of the owning objects.
        @warning raises program error if theIndex is more than owning objects count or less than 1.
        """

    def IsAttached(self) -> bool:
        """
        @return true if manipulator is attached to some interactive object (has owning object).
        """

    def HasActiveMode(self) -> bool:
        """
        @return true if some part of manipulator is selected (transformation mode is active, and
        owning object can be transformed).
        """

    def HasActiveTransformation(self) -> bool: ...

    @overload
    def StartTransformation(self) -> nanoocp.gp.gp_Trsf: ...

    @overload
    def StartTransformation(self, theIndex: int) -> nanoocp.gp.gp_Trsf: ...

    def SetZoomPersistence(self, theToEnable: bool) -> None:
        """
        @name Configuration of graphical transformations
        Enable or disable zoom persistence mode for the manipulator. With
        this mode turned on the presentation will keep fixed screen size.
        @warning when turned on this option overrides transform persistence
        properties and local transformation to achieve necessary visual effect.
        @warning revise use of AdjustSize argument of of \\sa AttachToObjects method
        when enabling zoom persistence.
        """

    def ZoomPersistence(self) -> bool:
        """Returns state of zoom persistence mode, whether it turned on or off."""

    def SetTransformPersistence(self, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """
        Redefines transform persistence management to setup transformation for sub-presentation of
        axes.
        @warning this interactive object does not support custom transformation persistence when
        using \\sa ZoomPersistence mode. In this mode the transformation persistence flags for
        presentations are overridden by this class.
        @warning Invokes debug assertion to catch incompatible usage of the method with \\sa
        ZoomPersistence mode, silently does nothing in release mode.
        @warning revise use of AdjustSize argument of of \\sa AttachToObjects method
        when enabling zoom persistence.
        """

    def SkinMode(self) -> AIS_Manipulator.ManipulatorSkin:
        """@return current manipulator skin mode."""

    def SetSkinMode(self, theSkinMode: AIS_Manipulator.ManipulatorSkin) -> None:
        """Sets skin mode for the manipulator."""

    def ActiveMode(self) -> AIS_ManipulatorMode: ...

    def ActiveAxisIndex(self) -> int: ...

    def Position(self) -> nanoocp.gp.gp_Ax2:
        """@return poition of manipulator interactive object."""

    def SetPosition(self, thePosition: nanoocp.gp.gp_Ax2) -> None:
        """Sets position of the manipulator object."""

    def Size(self) -> float: ...

    def SetSize(self, theSideLength: float) -> None:
        """Sets size (length of side of the manipulator cubic bounding box."""

    def SetGap(self, theValue: float) -> None:
        """Sets gaps between translator, scaler and rotator sub-presentations."""

    def SetTransformBehavior(self, theSettings: AIS_Manipulator.BehaviorOnTransform) -> None:
        """
        Sets behavior settings for transformation action carried on the manipulator,
        whether it translates, rotates together with the transformed object or not.
        """

    def ChangeTransformBehavior(self) -> AIS_Manipulator.BehaviorOnTransform:
        """
        @return behavior settings for transformation action of the manipulator.
        """

    def TransformBehavior(self) -> AIS_Manipulator.BehaviorOnTransform:
        """
        @return behavior settings for transformation action of the manipulator.
        """

    def Compute(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theMode: int = 0) -> None:
        """
        @name Presentation computation
        Fills presentation.
        @note Manipulator presentation does not use display mode and for all modes has the same
        presentation.
        """

    def ComputeSelection(self, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, theMode: int) -> None:
        """
        Computes selection sensitive zones (triangulation) for manipulator.
        @param[in] theNode  Selection mode that is treated as transformation mode.
        """

    def IsAutoHilight(self) -> bool:
        """
        Disables auto highlighting to use HilightSelected() and HilightOwnerWithColor() overridden
        methods.
        """

    def ClearSelected(self) -> None:
        """
        Method which clear all selected owners belonging
        to this selectable object (for fast presentation draw).
        """

    def HilightSelected(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Method which draws selected owners (for fast presentation draw)."""

    def HilightOwnerWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """
        Method which hilight an owner belonging to
        this selectable object (for fast presentation draw).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_ManipulatorOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """Entity owner for selection management of AIS_Manipulator object."""

    @overload
    def __init__(self, theSelObject: nanoocp.SelectMgr.SelectMgr_SelectableObject | None, theIndex: int, theMode: AIS_ManipulatorMode, thePriority: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: AIS_ManipulatorOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None: ...

    def IsHilighted(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> bool: ...

    def Unhilight(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> None: ...

    def Mode(self) -> AIS_ManipulatorMode: ...

    def Index(self) -> int:
        """@return index of manipulator axis."""

class AIS_MediaPlayer(AIS_InteractiveObject):
    """Presentation for video playback."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: AIS_MediaPlayer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def OpenInput(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theToWait: bool) -> None:
        """Open specified file."""

    def PresentFrame(self, theLeftCorner: nanoocp.BVH.BVH_Vec2i, theMaxSize: nanoocp.BVH.BVH_Vec2i) -> bool:
        """Display new frame."""

    def PlayerContext(self) -> nanoocp.Media.Media_PlayerContext:
        """Return player context."""

    def PlayPause(self) -> None:
        """Switch playback state."""

    def SetClosePlayer(self) -> None:
        """Schedule player to be closed."""

    def Duration(self) -> float:
        """Return duration."""

class AIS_MultipleConnectedInteractive(AIS_InteractiveObject):
    """
    Defines an Interactive Object by gathering together
    several object presentations. This is done through a
    list of interactive objects. These can also be
    Connected objects. That way memory-costly
    calculations of presentation are avoided.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes the Interactive Object with multiple
        connections to AIS_Interactive objects.
        """

    @overload
    def __init__(self, theOther: AIS_MultipleConnectedInteractive) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None, theLocation: nanoocp.TopLoc.TopLoc_Datum3D | None, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> AIS_InteractiveObject: ...

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None) -> AIS_InteractiveObject:
        """
        Establishes the connection between the Connected Interactive Object, theInteractive, and its
        reference. Copies local transformation and transformation persistence mode from
        theInteractive.
        @return created instance object (AIS_ConnectedInteractive or AIS_MultipleConnectedInteractive)
        """

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None, theLocation: nanoocp.gp.gp_Trsf) -> AIS_InteractiveObject:
        """
        Establishes the connection between the Connected Interactive Object, theInteractive, and its
        reference. Locates instance in theLocation and copies transformation persistence mode from
        theInteractive.
        @return created instance object (AIS_ConnectedInteractive or AIS_MultipleConnectedInteractive)
        """

    @overload
    def Connect(self, theAnotherObj: AIS_InteractiveObject | None, theLocation: nanoocp.gp.gp_Trsf, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> AIS_InteractiveObject:
        """
        Establishes the connection between the Connected Interactive Object, theInteractive, and its
        reference. Locates instance in theLocation and applies specified transformation persistence
        mode.
        @return created instance object (AIS_ConnectedInteractive or AIS_MultipleConnectedInteractive)
        """

    def Type(self) -> AIS_KindOfInteractive: ...

    def Signature(self) -> int: ...

    def HasConnection(self) -> bool:
        """Returns true if the object is connected to others."""

    def Disconnect(self, theInteractive: AIS_InteractiveObject | None) -> None:
        """Removes the connection with theInteractive."""

    def DisconnectAll(self) -> None:
        """Clears all the connections to objects."""

    def AcceptShapeDecomposition(self) -> bool:
        """
        Informs the graphic context that the interactive Object
        may be decomposed into sub-shapes for dynamic selection.
        """

    def GetAssemblyOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Returns common entity owner if the object is an assembly"""

    def GlobalSelOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Returns the owner of mode for selection of object as a whole"""

    def SetContext(self, theCtx: AIS_InteractiveContext | None) -> None:
        """Assigns interactive context."""

class AIS_Plane(AIS_InteractiveObject):
    """
    Constructs plane datums to be used in construction of
    composite shapes.
    """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Plane | None, aCurrentMode: bool = False) -> None:
        """
        initializes the plane aComponent. If
        the mode aCurrentMode equals true, the drawing
        tool, "Drawer" is not initialized.
        """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Plane | None, aCenter: nanoocp.gp.gp_Pnt, aCurrentMode: bool = False) -> None:
        """
        initializes the plane aComponent and
        the point aCenter. If the mode aCurrentMode
        equals true, the drawing tool, "Drawer" is not
        initialized. aCurrentMode equals true, the drawing
        tool, "Drawer" is not initialized.
        """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Axis2Placement | None, aPlaneType: AIS_TypeOfPlane, aCurrentMode: bool = False) -> None: ...

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Plane | None, aCenter: nanoocp.gp.gp_Pnt, aPmin: nanoocp.gp.gp_Pnt, aPmax: nanoocp.gp.gp_Pnt, aCurrentMode: bool = False) -> None:
        """
        initializes the plane aComponent, the
        point aCenter, and the minimum and maximum
        points, aPmin and aPmax. If the mode
        aCurrentMode equals true, the drawing tool, "Drawer" is not initialized.
        """

    @overload
    def __init__(self, theOther: AIS_Plane) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetSize(self, aValue: float) -> None:
        """Same value for x and y directions"""

    @overload
    def SetSize(self, Xval: float, YVal: float) -> None:
        """
        Sets the size defined by the length along the X axis
        XVal and the length along the Y axis YVal.
        """

    def UnsetSize(self) -> None: ...

    def Size(self) -> tuple[bool, float, float]: ...

    def HasOwnSize(self) -> bool: ...

    def SetMinimumSize(self, theValue: float) -> None:
        """Sets transform persistence for zoom with value of minimum size"""

    def UnsetMinimumSize(self) -> None:
        """Unsets transform persistence zoom"""

    def HasMinimumSize(self) -> bool:
        """Returns true if transform persistence for zoom is set"""

    def Signature(self) -> int: ...

    def Type(self) -> AIS_KindOfInteractive: ...

    def Component(self) -> nanoocp.Geom.Geom_Plane:
        """Returns the component specified in SetComponent."""

    def SetComponent(self, aComponent: nanoocp.Geom.Geom_Plane | None) -> None:
        """Creates an instance of the plane aComponent."""

    def PlaneAttributes(self, aCenter: nanoocp.gp.gp_Pnt, aPmin: nanoocp.gp.gp_Pnt, aPmax: nanoocp.gp.gp_Pnt) -> tuple[bool, nanoocp.Geom.Geom_Plane]:
        """
        Returns the settings for the selected plane
        aComponent, provided in SetPlaneAttributes.
        These include the points aCenter, aPmin, and aPmax
        """

    def SetPlaneAttributes(self, aComponent: nanoocp.Geom.Geom_Plane | None, aCenter: nanoocp.gp.gp_Pnt, aPmin: nanoocp.gp.gp_Pnt, aPmax: nanoocp.gp.gp_Pnt) -> None:
        """
        Allows you to provide settings other than default ones
        for the selected plane. These include: center point
        aCenter, maximum aPmax and minimum aPmin.
        """

    def Center(self) -> nanoocp.gp.gp_Pnt:
        """Returns the coordinates of the center point."""

    def SetCenter(self, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """Provides settings for the center theCenter other than (0, 0, 0)."""

    def SetAxis2Placement(self, aComponent: nanoocp.Geom.Geom_Axis2Placement | None, aPlaneType: AIS_TypeOfPlane) -> None:
        """
        Allows you to provide settings for the position and
        direction of one of the plane's axes, aComponent, in
        3D space. The coordinate system used is
        right-handed, and the type of plane aPlaneType is one of:
        -   AIS_ TOPL_Unknown
        -   AIS_ TOPL_XYPlane
        -   AIS_ TOPL_XZPlane
        -   AIS_ TOPL_YZPlane}.
        """

    def Axis2Placement(self) -> nanoocp.Geom.Geom_Axis2Placement:
        """
        Returns the position of the plane's axis2 system
        identifying the x, y, or z axis and giving the plane a
        direction in 3D space. An axis2 system is a right-handed coordinate system.
        """

    def TypeOfPlane(self) -> AIS_TypeOfPlane:
        """Returns the type of plane - xy, yz, xz or unknown."""

    def IsXYZPlane(self) -> bool:
        """Returns the type of plane - xy, yz, or xz."""

    def CurrentMode(self) -> bool:
        """Returns the non-default current display mode set by SetCurrentMode."""

    def SetCurrentMode(self, theCurrentMode: bool) -> None:
        """
        Allows you to provide settings for a non-default
        current display mode.
        """

    def AcceptDisplayMode(self, aMode: int) -> bool:
        """Returns true if the display mode selected, aMode, is valid for planes."""

    def SetContext(self, aCtx: AIS_InteractiveContext | None) -> None:
        """
        connection to <aCtx> default drawer implies a recomputation of Frame values.
        """

    def TypeOfSensitivity(self) -> nanoocp.Select3D.Select3D_TypeOfSensitivity:
        """Returns the type of sensitivity for the plane;"""

    def SetTypeOfSensitivity(self, theTypeOfSensitivity: nanoocp.Select3D.Select3D_TypeOfSensitivity) -> None:
        """Sets the type of sensitivity for the plane."""

    def ComputeSelection(self, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, theMode: int) -> None: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def UnsetColor(self) -> None: ...

class AIS_PlaneTrihedron(AIS_InteractiveObject):
    """
    To construct a selectable 2d axis system in a 3d
    drawing. This can be placed anywhere in the 3d
    system, and provides a coordinate system for
    drawing curves and shapes in a plane.
    There are 3 selection modes:
    -   mode 0   selection of the whole plane "trihedron"
    -   mode 1   selection of the origin of the plane "trihedron"
    -   mode 2   selection of the axes.
    Warning
    For the presentation of planes and trihedra, the
    millimetre is default unit of length, and 100 the default
    value for the representation of the axes. If you modify
    these dimensions, you must temporarily recover the
    Drawer object. From inside it, take the Aspects in
    which the values for length are stocked, for example,
    PlaneAspect for planes and LineAspect for
    trihedra. Change these values and recalculate the presentation.
    """

    @overload
    def __init__(self, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """
        Initializes the plane aPlane. The plane trihedron is
        constructed from this and an axis.
        """

    @overload
    def __init__(self, theOther: AIS_PlaneTrihedron) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Component(self) -> nanoocp.Geom.Geom_Plane:
        """Returns the component specified in SetComponent."""

    def SetComponent(self, aPlane: nanoocp.Geom.Geom_Plane | None) -> None:
        """Creates an instance of the component object aPlane."""

    def XAxis(self) -> AIS_Line:
        """Returns the "XAxis"."""

    def YAxis(self) -> AIS_Line:
        """Returns the "YAxis"."""

    def Position(self) -> AIS_Point:
        """Returns the point of origin of the plane trihedron."""

    def SetLength(self, theLength: float) -> None:
        """Sets the length of the X and Y axes."""

    def GetLength(self) -> float:
        """Returns the length of X and Y axes."""

    def AcceptDisplayMode(self, aMode: int) -> bool:
        """Returns true if the display mode selected, aMode, is valid."""

    def Signature(self) -> int: ...

    def Type(self) -> AIS_KindOfInteractive:
        """Returns datum as the type of Interactive Object."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Allows you to provide settings for the color aColor."""

    def SetXLabel(self, theLabel: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def SetYLabel(self, theLabel: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

class AIS_Point(AIS_InteractiveObject):
    """
    Constructs point datums to be used in construction of
    composite shapes. The datum is displayed as the plus marker +.
    """

    @overload
    def __init__(self, aComponent: nanoocp.Geom.Geom_Point | None) -> None:
        """
        Initializes the point aComponent from which the point
        datum will be built.
        """

    @overload
    def __init__(self, theOther: AIS_Point) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Signature(self) -> int:
        """Returns index 1, the default index for a point."""

    def Type(self) -> AIS_KindOfInteractive:
        """Indicates that a point is a datum."""

    def Component(self) -> nanoocp.Geom.Geom_Point:
        """Returns the component specified in SetComponent."""

    def SetComponent(self, aComponent: nanoocp.Geom.Geom_Point | None) -> None:
        """Constructs an instance of the point aComponent."""

    def AcceptDisplayMode(self, aMode: int) -> bool:
        """Returns true if the display mode selected is valid for point datums."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Allows you to provide settings for the Color."""

    def UnsetColor(self) -> None:
        """Allows you to remove color settings."""

    def SetMarker(self, aType: nanoocp.Aspect.Aspect_TypeOfMarker) -> None:
        """
        Allows you to provide settings for a marker. These include
        -   type of marker,
        -   marker color,
        -   scale factor.
        """

    def UnsetMarker(self) -> None:
        """Removes the marker settings."""

    def HasMarker(self) -> bool:
        """Returns true if the point datum has a marker."""

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex:
        """Converts a point into a vertex."""

class AIS_PointCloud(AIS_InteractiveObject):
    """
    Interactive object for set of points.
    The presentation supports two display modes:
    - Points.
    - Bounding box for highlighting.
    Presentation provides selection by bounding box.
    Selection and consequently highlighting can disabled by
    setting default selection mode to -1. There will be no way
    to select object from interactive view. Any calls to
    AIS_InteractiveContext::AddOrRemoveSelected should be also prohibited,
    to avoid programmatic highlighting (workaround is setting non-supported
    hilight mode, e.g. 100);
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: AIS_PointCloud) -> None: ...

    class DisplayMode(enum.IntEnum):
        """Display modes supported by this Point Cloud object"""

        DM_Points = 0

        DM_BndBox = 2

    DM_Points: AIS_PointCloud.DisplayMode = DisplayMode.DM_Points

    DM_BndBox: AIS_PointCloud.DisplayMode = DisplayMode.DM_BndBox

    class SelectionMode(enum.IntEnum):
        """Selection modes supported by this Point Cloud object"""

        SM_Points = 0

        SM_SubsetOfPoints = 1

        SM_BndBox = 2

    SM_Points: AIS_PointCloud.SelectionMode = SelectionMode.SM_Points

    SM_SubsetOfPoints: AIS_PointCloud.SelectionMode = SelectionMode.SM_SubsetOfPoints

    SM_BndBox: AIS_PointCloud.SelectionMode = SelectionMode.SM_BndBox

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetPoints(self, thePoints: nanoocp.Graphic3d.Graphic3d_ArrayOfPoints | None) -> None:
        """
        Sets the points from array of points.
        Method will not copy the input data - array will be stored as handle.
        @param[in] thePoints  the array of points
        """

    @overload
    def SetPoints(self, theCoords: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Pnt] | None, theColors: nanoocp.NCollection.NCollection_HArray1[nanoocp.Quantity.Quantity_Color] | None = None, theNormals: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_Dir] | None = None) -> None:
        """
        Sets the points with optional colors.
        The input data will be copied into internal buffer.
        The input arrays should have equal length, otherwise
        the presentation will not be computed and displayed.
        @param[in] theCoords   the array of coordinates
        @param[in] theColors   optional array of colors
        @param[in] theNormals  optional array of normals
        """

    def GetPoints(self) -> nanoocp.Graphic3d.Graphic3d_ArrayOfPoints:
        """
        Get the points array.
        Method might be overridden to fill in points array dynamically from application data
        structures.
        @return the array of points
        """

    def GetBoundingBox(self) -> nanoocp.Bnd.Bnd_Box:
        """Get bounding box for presentation."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Setup custom color. Affects presentation only when no per-point color attribute has been
        assigned.
        """

    def UnsetColor(self) -> None:
        """Restore default color."""

    def SetMaterial(self, theMat: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """
        Setup custom material. Affects presentation only when normals are defined.
        """

    def UnsetMaterial(self) -> None:
        """Restore default material."""

class AIS_PointCloudOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """Custom owner for highlighting selected points."""

    @overload
    def __init__(self, theOrigin: AIS_PointCloud | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: AIS_PointCloudOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SelectedPoints(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """
        Return selected points.
        WARNING! Indexation starts with 0 (shifted by -1 comparing to
        Graphic3d_ArrayOfPoints::Vertice()).
        """

    def DetectedPoints(self) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """
        Return last detected points.
        WARNING! Indexation starts with 0 (shifted by -1 comparing to
        Graphic3d_ArrayOfPoints::Vertice()).
        """

    def IsForcedHilight(self) -> bool:
        """Always update dynamic highlighting."""

    def HilightWithColor(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None:
        """Handle dynamic highlighting."""

    def Unhilight(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> None:
        """Removes highlighting."""

    def Clear(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> None:
        """Clears presentation."""

class AIS_RubberBand(AIS_InteractiveObject):
    """
    Presentation for drawing rubber band selection.
    It supports rectangle and polygonal selection.
    It is constructed in 2d overlay.
    Default configuration is built without filling.
    For rectangle selection use SetRectangle() method.
    For polygonal selection use AddPoint() and GetPoints() methods.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs rubber band with default configuration: empty filling and white solid lines.
        @warning It binds this object with Graphic3d_ZLayerId_TopOSD layer.
        """

    @overload
    def __init__(self, theLineColor: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_TypeOfLine, theLineWidth: float = 1.0, theIsPolygonClosed: bool = True) -> None:
        """
        Constructs the rubber band with empty filling and defined line style.
        @param[in] theLineColor  color of rubber band lines
        @param[in] theType  type of rubber band lines
        @param[in] theLineWidth  width of rubber band line. By default it is 1.
        @warning It binds this object with Graphic3d_ZLayerId_TopOSD layer.
        """

    @overload
    def __init__(self, theLineColor: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_TypeOfLine, theFillColor: nanoocp.Quantity.Quantity_Color, theTransparency: float = 1.0, theLineWidth: float = 1.0, theIsPolygonClosed: bool = True) -> None:
        """
        Constructs the rubber band with defined filling and line parameters.
        @param[in] theLineColor  color of rubber band lines
        @param[in] theType  type of rubber band lines
        @param[in] theFillColor  color of rubber band filling
        @param[in] theTransparency  transparency of the filling. 0 is for opaque filling. By default
        it is transparent.
        @param[in] theLineWidth  width of rubber band line. By default it is 1.
        @warning It binds this object with Graphic3d_ZLayerId_TopOSD layer.
        """

    @overload
    def __init__(self, theOther: AIS_RubberBand) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetRectangle(self, theMinX: int, theMinY: int, theMaxX: int, theMaxY: int) -> None:
        """Sets rectangle bounds."""

    def AddPoint(self, thePoint: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Adds last point to the list of points. They are used to build polygon for rubber band.
        @sa RemoveLastPoint(), GetPoints()
        """

    def RemoveLastPoint(self) -> None:
        """
        Remove last point from the list of points for the rubber band polygon.
        @sa AddPoint(), GetPoints()
        """

    def Points(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.BVH.BVH_Vec2i]:
        """@return points for the rubber band polygon."""

    def ClearPoints(self) -> None:
        """Remove all points for the rubber band polygon."""

    def LineColor(self) -> nanoocp.Quantity.Quantity_Color:
        """@return the Color attributes."""

    def SetLineColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color of lines for rubber band presentation."""

    def FillColor(self) -> nanoocp.Quantity.Quantity_Color:
        """@return the color of rubber band filling."""

    def SetFillColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color of rubber band filling."""

    def SetLineWidth(self, theWidth: float) -> None:
        """Sets width of line for rubber band presentation."""

    def LineWidth(self) -> float:
        """@return width of lines."""

    def SetLineType(self, theType: nanoocp.Aspect.Aspect_TypeOfLine) -> None:
        """Sets type of line for rubber band presentation."""

    def LineType(self) -> nanoocp.Aspect.Aspect_TypeOfLine:
        """@return type of lines."""

    def SetFillTransparency(self, theValue: float) -> None:
        """
        Sets fill transparency.
        @param[in] theValue  the transparency value. 1.0 is for transparent background
        """

    def FillTransparency(self) -> float:
        """@return fill transparency."""

    @overload
    def SetFilling(self, theIsFilling: bool) -> None:
        """Enable or disable filling of rubber band."""

    @overload
    def SetFilling(self, theColor: nanoocp.Quantity.Quantity_Color, theTransparency: float) -> None:
        """
        Enable filling of rubber band with defined parameters.
        @param[in] theColor  color of filling
        @param[in] theTransparency  transparency of the filling. 0 is for opaque filling.
        """

    def IsFilling(self) -> bool:
        """@return true if filling of rubber band is enabled."""

    def IsPolygonClosed(self) -> bool:
        """@return true if automatic closing of rubber band is enabled."""

    def SetPolygonClosed(self, theIsPolygonClosed: bool) -> None:
        """
        Automatically create an additional line connecting the first and
        the last screen points to close the boundary polyline
        """

class AIS_TypeFilter(nanoocp.SelectMgr.SelectMgr_Filter):
    """
    Selects Interactive Objects through their types. The
    filter questions each Interactive Object in local context
    to determine whether it has an non-null owner, and if
    so, whether it is of the desired type. If the object
    returns true in each case, it is kept. If not, it is rejected.
    By default, the interactive object has a None type
    and a signature of 0. A filter for type specifies a
    choice of type out of a range at any level enumerated
    for type or kind. The choice could be for kind of
    interactive object, of dimension, of unit, or type of axis,
    plane or attribute.
    If you want to give a particular type and signature to
    your Interactive Object, you must redefine two virtual
    methods: Type and Signature.
    This filter is used in both Neutral Point and open local contexts.
    In the Collector viewer, you can only locate
    Interactive Objects which answer positively to the
    positioned filters when a local context is open.
    Warning
    When you close a local context, all temporary
    interactive objects are deleted, all selection modes
    concerning the context are cancelled, and all content
    filters are emptied.
    """

    @overload
    def __init__(self, aGivenKind: AIS_KindOfInteractive) -> None:
        """Initializes filter for type, aGivenKind."""

    @overload
    def __init__(self, theOther: AIS_TypeFilter) -> None: ...

    def IsOk(self, anobj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """
        Returns False if the transient is not an Interactive
        Object, or if the type of the Interactive Object is not
        the same as that stored in the filter.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_SignatureFilter(AIS_TypeFilter):
    """
    Selects Interactive Objects through their signatures
    and types. The signature provides an
    additional characterization of an object's type, and
    takes the form of an index. The filter questions each
    Interactive Object in local context to determine
    whether it has an non-null owner, and if so, whether
    it has the desired signature. If the object returns true
    in each case, it is kept. If not, it is rejected.
    By default, the interactive object has a None type
    and a signature of 0. If you want to give a particular
    type and signature to your Interactive Object, you
    must redefine two virtual methods: Type and Signature.
    This filter is only used in an open local contexts.
    In the Collector viewer, you can only locate
    Interactive Objects which answer positively to the
    positioned filters when a local context is open.
    Warning
    Some signatures have already been used by standard
    objects delivered in AIS. These include:
    -   signature 0 - Shape
    -   signature 1 - Point
    -   signature 2 - Axis
    -   signature 3 - Trihedron
    -   signature 4 - PlaneTrihedron
    -   signature 5 - Line
    -   signature 6 - Circle
    -   signature 7 - Plane
    """

    @overload
    def __init__(self, aGivenKind: AIS_KindOfInteractive, aGivenSignature: int) -> None:
        """
        Initializes the signature filter, adding the signature
        specification, aGivenSignature, to that for type,
        aGivenKind, in AIS_TypeFilter.
        """

    @overload
    def __init__(self, theOther: AIS_SignatureFilter) -> None: ...

    def IsOk(self, anobj: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> bool:
        """
        Returns False if the transient is not an AIS_InteractiveObject.
        Returns False if the signature of InteractiveObject
        is not the same as the stored one in the filter...
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_TextLabel(AIS_InteractiveObject):
    """Presentation of the text."""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: AIS_TextLabel) -> None: ...

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """Return TRUE for supported display mode."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Setup color of entire text."""

    def SetTransparency(self, theValue: float) -> None:
        """Setup transparency within [0, 1] range."""

    def UnsetTransparency(self) -> None:
        """Removes the transparency setting."""

    def SetMaterial(self, arg0: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """Material has no effect for text label."""

    def SetText(self, theText: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Setup text."""

    def SetPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None:
        """Setup position."""

    def SetHJustification(self, theHJust: nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment) -> None:
        """Setup horizontal justification."""

    def SetVJustification(self, theVJust: nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment) -> None:
        """Setup vertical justification."""

    def SetAngle(self, theAngle: float) -> None:
        """Setup angle."""

    def SetZoomable(self, theIsZoomable: bool) -> None:
        """Setup zoomable property."""

    def SetHeight(self, theHeight: float) -> None:
        """Setup height."""

    def SetFontAspect(self, theFontAspect: nanoocp.Font.Font_FontAspect) -> None:
        """Setup font aspect."""

    def SetFont(self, theFont: str) -> None:
        """Setup font."""

    def SetOrientation3D(self, theOrientation: nanoocp.gp.gp_Ax2) -> None:
        """Setup label orientation in the model 3D space."""

    def UnsetOrientation3D(self) -> None:
        """Reset label orientation in the model 3D space."""

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """Returns position."""

    def Text(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the label text."""

    def FontName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the font of the label text."""

    def FontAspect(self) -> nanoocp.Font.Font_FontAspect:
        """Returns the font aspect of the label text."""

    def Orientation3D(self) -> nanoocp.gp.gp_Ax2:
        """Returns label orientation in the model 3D space."""

    def HasOrientation3D(self) -> bool:
        """
        Returns true if the current text placement mode uses text orientation in the model 3D space.
        """

    def SetFlipping(self, theIsFlipping: bool) -> None: ...

    def HasFlipping(self) -> bool: ...

    def HasOwnAnchorPoint(self) -> bool:
        """Returns flag if text uses position as point of attach"""

    def SetOwnAnchorPoint(self, theOwnAnchorPoint: bool) -> None:
        """Set flag if text uses position as point of attach"""

    def SetDisplayType(self, theDisplayType: nanoocp.Aspect.Aspect_TypeOfDisplayText) -> None:
        """
        Define the display type of the text.

        TODT_NORMAL     Default display. Text only.
        TODT_SUBTITLE   There is a subtitle under the text.
        TODT_DEKALE     The text is displayed with a 3D style.
        TODT_BLEND      The text is displayed in XOR.
        TODT_DIMENSION  Dimension line under text will be invisible.
        """

    def SetColorSubTitle(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Modifies the colour of the subtitle for the TODT_SUBTITLE TextDisplayType
        and the colour of backgroubd for the TODT_DEKALE TextDisplayType.
        """

    def TextFormatter(self) -> nanoocp.Font.Font_TextFormatter:
        """
        Returns text presentation formatter; NULL by default, which means standard text formatter will
        be used.
        """

    def SetTextFormatter(self, theFormatter: nanoocp.Font.Font_TextFormatter | None) -> None:
        """Setup text formatter for presentation. It's empty by default."""

    @staticmethod
    def get_type_name() -> str:
        """CASCADE RTTI"""

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type:
        """CASCADE RTTI"""

    def DynamicType(self) -> nanoocp.Standard.Standard_Type:
        """CASCADE RTTI"""

class AIS_TexturedShape(AIS_Shape):
    """
    This class allows to map textures on shapes.
    Presentations modes AIS_WireFrame (0) and AIS_Shaded (1) behave in the same manner as in
    AIS_Shape, whilst new modes 2 (bounding box) and 3 (texture mapping) extends it functionality.

    The texture itself is parametrized in (0,1)x(0,1).
    Each face of a shape located in UV space is provided with these parameters:
    - Umin - starting position in U
    - Umax - ending   position in U
    - Vmin - starting position in V
    - Vmax - ending   position in V
    Each face is triangulated and a texel is assigned to each node.
    Facets are then filled using a linear interpolation of texture between each 'three texels'.
    User can act on:
    - the number of occurrences of the texture on the face
    - the position of the origin of the texture
    - the scale factor of the texture
    """

    @overload
    def __init__(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        @name main methods
        Initializes the textured shape.
        """

    @overload
    def __init__(self, theOther: AIS_TexturedShape) -> None: ...

    def SetTextureFileName(self, theTextureFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the texture source. <theTextureFileName> can specify path to texture image or one of the
        standard predefined textures. The accepted file types are those used in Image_AlienPixMap with
        extensions such as rgb, png, jpg and more. To specify the standard predefined texture, the
        <theTextureFileName> should contain integer - the Graphic3d_NameOfTexture2D enumeration index.
        Setting texture source using this method resets the source pixmap (if was set previously).
        """

    def SetTexturePixMap(self, theTexturePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """
        Sets the texture source. <theTexturePixMap> specifies image data.
        Please note that the data should be in Bottom-Up order, the flag of Image_PixMap::IsTopDown()
        will be ignored by graphic driver. Setting texture source using this method resets the source
        by filename (if was set previously).
        """

    def TextureMapState(self) -> bool:
        """@return flag to control texture mapping (for presentation mode 3)"""

    def SetTextureMapOn(self) -> None:
        """Enables texture mapping"""

    def SetTextureMapOff(self) -> None:
        """Disables texture mapping"""

    def TextureFile(self) -> str:
        """@return path to the texture file"""

    def TexturePixMap(self) -> nanoocp.Image.Image_PixMap:
        """@return the source pixmap for texture map"""

    def UpdateAttributes(self) -> None:
        """
        @name methods to alter texture mapping properties
        Use this method to display the textured shape without recomputing the whole presentation.
        Use this method when ONLY the texture content has been changed.
        If other parameters (ie: scale factors, texture origin, texture repeat...) have changed, the
        whole presentation has to be recomputed:
        @code
        if (myShape->DisplayMode() == 3)
        {
        myAISContext->RecomputePrsOnly (myShape);
        }
        else
        {
        myAISContext->SetDisplayMode (myShape, 3, false);
        myAISContext->Display        (myShape, true);
        }
        @endcode
        """

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets the color."""

    def UnsetColor(self) -> None:
        """Removes settings for the color."""

    def SetMaterial(self, theAspect: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """Sets the material aspect."""

    def UnsetMaterial(self) -> None:
        """Removes settings for material aspect."""

    def EnableTextureModulate(self) -> None:
        """Enables texture modulation"""

    def DisableTextureModulate(self) -> None:
        """Disables texture modulation"""

    def TextureRepeat(self) -> bool:
        """@return texture repeat flag"""

    def URepeat(self) -> float:
        """@return texture repeat U value"""

    def VRepeat(self) -> float:
        """@return texture repeat V value"""

    def SetTextureRepeat(self, theToRepeat: bool, theURepeat: float = 1.0, theVRepeat: float = 1.0) -> None:
        """
        Sets the number of occurrences of the texture on each face. The texture itself is
        parameterized in (0,1) by (0,1). Each face of the shape to be textured is parameterized in UV
        space (Umin,Umax) by (Vmin,Vmax). If RepeatYN is set to false, texture coordinates are clamped
        in the range (0,1)x(0,1) of the face.
        """

    def TextureOrigin(self) -> bool:
        """@return true if texture UV origin has been modified"""

    def TextureUOrigin(self) -> float:
        """@return texture origin U position (0.0 by default)"""

    def TextureVOrigin(self) -> float:
        """@return texture origin V position (0.0 by default)"""

    def SetTextureOrigin(self, theToSetTextureOrigin: bool, theUOrigin: float = 0.0, theVOrigin: float = 0.0) -> None:
        """
        Use this method to change the origin of the texture. The texel (0,0) will be mapped to the
        surface (UOrigin,VOrigin)
        """

    def TextureScale(self) -> bool:
        """@return true if scale factor should be applied to texture mapping"""

    def TextureScaleU(self) -> float:
        """@return scale factor for U coordinate (1.0 by default)"""

    def TextureScaleV(self) -> float:
        """@return scale factor for V coordinate (1.0 by default)"""

    def SetTextureScale(self, theToSetTextureScale: bool, theScaleU: float = 1.0, theScaleV: float = 1.0) -> None:
        """
        Use this method to scale the texture (percent of the face).
        You can specify a scale factor for both U and V.
        Example: if you set ScaleU and ScaleV to 0.5 and you enable texture repeat,
        the texture will appear twice on the face in each direction.
        """

    @overload
    def ShowTriangles(self) -> bool:
        """@return true if displaying of triangles is requested"""

    @overload
    def ShowTriangles(self, theToShowTriangles: bool) -> None:
        """
        Use this method to show the triangulation of the shape (for debugging etc.).
        """

    def TextureModulate(self) -> bool:
        """@return true if texture color modulation is turned on"""

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Return true if specified display mode is supported (extends AIS_Shape with Display Mode 3).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class AIS_Triangulation(AIS_InteractiveObject):
    """
    Interactive object that draws data from Poly_Triangulation, optionally with colors associated
    with each triangulation vertex. For maximum efficiency colors are represented as 32-bit integers
    instead of classic Quantity_Color values.
    Interactive selection of triangles and vertices is not yet implemented.
    """

    @overload
    def __init__(self, aTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> None:
        """Constructs the Triangulation display object"""

    @overload
    def __init__(self, theOther: AIS_Triangulation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColors(self, aColor: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """
        Set the color for each node.
        Each 32-bit color is Alpha << 24 + Blue << 16 + Green << 8 + Red
        Order of color components is essential for further usage by OpenGL
        """

    def GetColors(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """
        Get the color for each node.
        Each 32-bit color is Alpha << 24 + Blue << 16 + Green << 8 + Red
        """

    def HasVertexColors(self) -> bool:
        """Returns true if triangulation has vertex colors."""

    def SetTriangulation(self, aTriangulation: nanoocp.Poly.Poly_Triangulation | None) -> None: ...

    def GetTriangulation(self) -> nanoocp.Poly.Poly_Triangulation:
        """Returns Poly_Triangulation ."""

    def SetTransparency(self, aValue: float = 0.6) -> None:
        """
        Sets the value aValue for transparency in the reconstructed compound shape.
        """

    def UnsetTransparency(self) -> None:
        """
        Removes the setting for transparency in the reconstructed compound shape.
        """

class AIS_Trihedron(AIS_InteractiveObject):
    """
    Create a selectable trihedron
    The trihedron includes 1 origin, 3 axes and 3 labels.
    Default text of labels are "X", "Y", "Z".
    Color of origin and any axis, color of arrows and labels may be changed.
    Visual presentation might be shown in two, shaded and wireframe modes, wireframe by default).
    There are 4 modes of selection:
    - AIS_TrihedronSelectionMode_EntireObject to select trihedron,  priority = 1
    - AIS_TrihedronSelectionMode_Origin       to select its origin, priority = 5
    - AIS_TrihedronSelectionMode_Axes         to select its axis,   priority = 3
    - AIS_TrihedronSelectionMode_MainPlanes   to select its planes, priority = 2

    Warning!
    For the presentation of trihedron, the default unit of length is the millimetre,
    and the default value for the representation of the axes is 100.
    If you modify these dimensions, you must temporarily recover the Drawer.
    From inside it, you take the aspect in which the values for length are stocked.
    For trihedron, this is Prs3d_Drawer_LineAspect.
    You change the values inside this Aspect and recalculate the presentation.
    """

    @overload
    def __init__(self, theComponent: nanoocp.Geom.Geom_Axis2Placement | None) -> None:
        """Initializes a trihedron entity."""

    @overload
    def __init__(self, theOther: AIS_Trihedron) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DatumDisplayMode(self) -> nanoocp.Prs3d.Prs3d_DatumMode:
        """Returns datum display mode."""

    def SetDatumDisplayMode(self, theMode: nanoocp.Prs3d.Prs3d_DatumMode) -> None:
        """
        Sets Shading or Wireframe display mode, triangle or segment graphic group is used relatively.
        """

    def Component(self) -> nanoocp.Geom.Geom_Axis2Placement:
        """Returns the right-handed coordinate system set in SetComponent."""

    def SetComponent(self, theComponent: nanoocp.Geom.Geom_Axis2Placement | None) -> None:
        """Constructs the right-handed coordinate system aComponent."""

    def HasOwnSize(self) -> bool:
        """
        Returns true if the trihedron object has a size other
        than the default size of 100 mm. along each axis.
        """

    def Size(self) -> float:
        """Returns the size of trihedron object; 100.0 by DEFAULT."""

    def SetSize(self, theValue: float) -> None:
        """Sets the size of trihedron object."""

    def UnsetSize(self) -> None:
        """
        Removes any non-default settings for size of this trihedron object.
        If the object has 1 color, the default size of the
        drawer is reproduced, otherwise DatumAspect becomes null.
        """

    def HasTextColor(self) -> bool:
        """Returns true if trihedron has own text color"""

    def TextColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns trihedron text color"""

    @overload
    def SetTextColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color of label of trihedron axes."""

    @overload
    def SetTextColor(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color of label of trihedron axis."""

    def HasArrowColor(self) -> bool:
        """Returns true if trihedron has own arrow color"""

    def ArrowColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns trihedron arrow color"""

    @overload
    def SetArrowColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetArrowColor(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets color of arrow of trihedron axes."""

    def DatumPartColor(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts) -> nanoocp.Quantity.Quantity_Color:
        """Returns color of datum part: origin or some of trihedron axes."""

    def SetDatumPartColor(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color of datum part: origin or some of trihedron axes.
        If presentation is shading mode, this color is set for both sides of facing model
        """

    def SetOriginColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color of origin.
        Standard_DEPRECATED("This method is deprecated - SetColor() should be called instead")
        """

    def SetXAxisColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color of x-axis.
        Standard_DEPRECATED("This method is deprecated - SetColor() should be called instead")
        """

    def SetYAxisColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color of y-axis.
        Standard_DEPRECATED("This method is deprecated - SetColor() should be called instead")
        """

    def SetAxisColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets color of z-axis.
        Standard_DEPRECATED("This method is deprecated - SetColor() should be called instead")
        """

    def ToDrawArrows(self) -> bool:
        """Returns true if arrows are to be drawn"""

    def SetDrawArrows(self, theToDraw: bool) -> None:
        """Sets whether to draw the arrows in visualization"""

    def SelectionPriority(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts) -> int:
        """Returns priority of selection for owner of the given type"""

    def SetSelectionPriority(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts, thePriority: int) -> None:
        """Sets priority of selection for owner of the given type"""

    def Label(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Returns text of axis. Parameter thePart should be XAxis, YAxis or ZAxis
        """

    def SetLabel(self, thePart: nanoocp.Prs3d.Prs3d_DatumParts, theName: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Sets text label for trihedron axis. Parameter thePart should be XAxis, YAxis or ZAxis
        """

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets the color theColor for this trihedron object, it changes color of axes.
        """

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        Returns true if the display mode selected, aMode, is valid for trihedron datums.
        """

    def Signature(self) -> int:
        """Returns index 3, selection of the planes XOY, YOZ, XOZ."""

    def Type(self) -> AIS_KindOfInteractive:
        """Indicates that the type of Interactive Object is datum."""

    def UnsetColor(self) -> None:
        """Removes the settings for color."""

    def ClearSelected(self) -> None:
        """
        Method which clear all selected owners belonging
        to this selectable object (for fast presentation draw).
        """

    def HilightSelected(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theOwners: nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Method which draws selected owners (for fast presentation draw)."""

    def HilightOwnerWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """
        Method which highlights an owner belonging to
        this selectable object (for fast presentation draw).
        """

class AIS_TrihedronOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """Entity owner for selection management of AIS_Trihedron object."""

    @overload
    def __init__(self, theSelObject: nanoocp.SelectMgr.SelectMgr_SelectableObject | None, theDatumPart: nanoocp.Prs3d.Prs3d_DatumParts, thePriority: int) -> None:
        """Creates an owner of AIS_Trihedron object."""

    @overload
    def __init__(self, theOther: AIS_TrihedronOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DatumPart(self) -> nanoocp.Prs3d.Prs3d_DatumParts:
        """Returns the datum part identifier."""

    def HilightWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theMode: int) -> None:
        """Highlights selectable object's presentation."""

    def IsHilighted(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> bool:
        """
        Returns true if the presentation manager thePM
        highlights selections corresponding to the selection mode aMode.
        """

    def Unhilight(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theMode: int) -> None:
        """
        Removes highlighting from the owner of a detected
        selectable object in the presentation manager thePM.
        """

class AIS_ViewInputBuffer:
    """Auxiliary structure defining viewer events"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: AIS_ViewInputBuffer) -> None: ...

    def Reset(self) -> None:
        """Reset events buffer."""

    @property
    def IsNewGesture(self) -> bool:
        """transition from one action to another"""

    @IsNewGesture.setter
    def IsNewGesture(self, arg: bool, /) -> None: ...

    @property
    def ZoomActions(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Aspect.Aspect_ScrollDelta]:
        """the queue with zoom actions"""

    @ZoomActions.setter
    def ZoomActions(self, arg: nanoocp.NCollection.NCollection_Sequence[nanoocp.Aspect.Aspect_ScrollDelta], /) -> None: ...

    @property
    def Orientation(self) -> AIS_ViewInputBuffer._orientation: ...

    @Orientation.setter
    def Orientation(self, arg: AIS_ViewInputBuffer._orientation, /) -> None: ...

    @property
    def MoveTo(self) -> AIS_ViewInputBuffer._highlighting: ...

    @MoveTo.setter
    def MoveTo(self, arg: AIS_ViewInputBuffer._highlighting, /) -> None: ...

    @property
    def Selection(self) -> AIS_ViewInputBuffer._selection: ...

    @Selection.setter
    def Selection(self, arg: AIS_ViewInputBuffer._selection, /) -> None: ...

    @property
    def Panning(self) -> AIS_ViewInputBuffer._panningParams: ...

    @Panning.setter
    def Panning(self, arg: AIS_ViewInputBuffer._panningParams, /) -> None: ...

    @property
    def Dragging(self) -> AIS_ViewInputBuffer._draggingParams: ...

    @Dragging.setter
    def Dragging(self, arg: AIS_ViewInputBuffer._draggingParams, /) -> None: ...

    @property
    def OrbitRotation(self) -> AIS_ViewInputBuffer._orbitRotation: ...

    @OrbitRotation.setter
    def OrbitRotation(self, arg: AIS_ViewInputBuffer._orbitRotation, /) -> None: ...

    @property
    def ViewRotation(self) -> AIS_ViewInputBuffer._viewRotation: ...

    @ViewRotation.setter
    def ViewRotation(self, arg: AIS_ViewInputBuffer._viewRotation, /) -> None: ...

    @property
    def ZRotate(self) -> AIS_ViewInputBuffer._zrotateParams: ...

    @ZRotate.setter
    def ZRotate(self, arg: AIS_ViewInputBuffer._zrotateParams, /) -> None: ...

class AIS_WalkPart:
    """Walking value."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: AIS_WalkPart) -> None: ...

    def IsEmpty(self) -> bool:
        """Return TRUE if delta is empty."""

    @property
    def Value(self) -> float:
        """value"""

    @Value.setter
    def Value(self, arg: float, /) -> None: ...

    @property
    def Pressure(self) -> float:
        """key pressure"""

    @Pressure.setter
    def Pressure(self, arg: float, /) -> None: ...

    @property
    def Duration(self) -> float:
        """duration"""

    @Duration.setter
    def Duration(self, arg: float, /) -> None: ...

class AIS_WalkDelta:
    """Walking values."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: AIS_WalkDelta) -> None: ...

    @overload
    def __getitem__(self, thePart: AIS_WalkTranslation) -> AIS_WalkPart:
        """Return translation component."""

    @overload
    def __getitem__(self, thePart: AIS_WalkRotation) -> AIS_WalkPart:
        """Return rotation component."""

    def IsJumping(self) -> bool:
        """Return jumping state."""

    def SetJumping(self, theIsJumping: bool) -> None:
        """Set jumping state."""

    def IsCrouching(self) -> bool:
        """Return crouching state."""

    def SetCrouching(self, theIsCrouching: bool) -> None:
        """Set crouching state."""

    def IsRunning(self) -> bool:
        """Return running state."""

    def SetRunning(self, theIsRunning: bool) -> None:
        """Set running state."""

    def IsDefined(self) -> bool:
        """
        Return TRUE if navigation keys are pressed even if delta from the previous frame is empty.
        """

    def SetDefined(self, theIsDefined: bool) -> None:
        """Set if any navigation key is pressed."""

    def IsEmpty(self) -> bool:
        """Return TRUE when both Rotation and Translation deltas are empty."""

    def ToMove(self) -> bool:
        """Return TRUE if translation delta is defined."""

    def ToRotate(self) -> bool:
        """Return TRUE if rotation delta is defined."""

class AIS_ViewController(nanoocp.Aspect.Aspect_WindowInputListener):
    """
    Auxiliary structure for handling viewer events between GUI and Rendering threads.

    Class implements the following features:
    - Buffers storing the state of user input (mouse, touches and keyboard).
    - Mapping mouse/multi-touch input to View camera manipulations (panning/rotating/zooming).
    - Input events are not applied immediately but queued for separate processing from two working
    threads
    UI thread receiving user input and Rendering thread for OCCT 3D Viewer drawing.
    """

    def __init__(self) -> None:
        """Empty constructor."""

    def InputBuffer(self, theType: AIS_ViewInputBufferType) -> AIS_ViewInputBuffer:
        """Return input buffer."""

    def ChangeInputBuffer(self, theType: AIS_ViewInputBufferType) -> AIS_ViewInputBuffer:
        """Return input buffer."""

    def ViewAnimation(self) -> AIS_AnimationCamera:
        """Return view animation; empty (but not NULL) animation by default."""

    def SetViewAnimation(self, theAnimation: AIS_AnimationCamera | None) -> None:
        """Set view animation to be handled within handleViewRedraw()."""

    def AbortViewAnimation(self) -> None:
        """Interrupt active view animation."""

    def ObjectsAnimation(self) -> AIS_Animation:
        """Return objects animation; empty (but not NULL) animation by default."""

    def SetObjectsAnimation(self, theAnimation: AIS_Animation | None) -> None:
        """Set object animation to be handled within handleViewRedraw()."""

    def ToPauseObjectsAnimation(self) -> bool:
        """
        Return TRUE if object animation should be paused on mouse click; FALSE by default.
        """

    def SetPauseObjectsAnimation(self, theToPause: bool) -> None:
        """Set if object animation should be paused on mouse click."""

    def IsContinuousRedraw(self) -> bool:
        """
        Return TRUE if continuous redrawing is enabled; FALSE by default.
        This option would request a next viewer frame to be completely redrawn right after current
        frame is finished.
        """

    def SetContinuousRedraw(self, theToEnable: bool) -> None:
        """Enable or disable continuous updates."""

    def RotationMode(self) -> AIS_RotationMode:
        """
        @name global parameters
        Return camera rotation mode, AIS_RotationMode_BndBoxActive by default.
        """

    def SetRotationMode(self, theMode: AIS_RotationMode) -> None:
        """Set camera rotation mode."""

    def NavigationMode(self) -> AIS_NavigationMode:
        """Return camera navigation mode; AIS_NavigationMode_Orbit by default."""

    def SetNavigationMode(self, theMode: AIS_NavigationMode) -> None:
        """Set camera navigation mode."""

    def MouseAcceleration(self) -> float:
        """
        Return mouse input acceleration ratio in First Person mode; 1.0 by default.
        """

    def SetMouseAcceleration(self, theRatio: float) -> None:
        """Set mouse input acceleration ratio."""

    def OrbitAcceleration(self) -> float:
        """Return orbit rotation acceleration ratio; 1.0 by default."""

    def SetOrbitAcceleration(self, theRatio: float) -> None:
        """Set orbit rotation acceleration ratio."""

    def ToShowPanAnchorPoint(self) -> bool:
        """
        Return TRUE if panning anchor point within perspective projection should be displayed in 3D
        Viewer; TRUE by default.
        """

    def SetShowPanAnchorPoint(self, theToShow: bool) -> None:
        """
        Set if panning anchor point within perspective projection should be displayed in 3D Viewer.
        """

    def ToShowRotateCenter(self) -> bool:
        """
        Return TRUE if rotation point should be displayed in 3D Viewer; TRUE by default.
        """

    def SetShowRotateCenter(self, theToShow: bool) -> None:
        """Set if rotation point should be displayed in 3D Viewer."""

    def ToLockOrbitZUp(self) -> bool:
        """
        Return TRUE if camera up orientation within AIS_NavigationMode_Orbit rotation mode should be
        forced Z up; FALSE by default.
        """

    def SetLockOrbitZUp(self, theToForceUp: bool) -> None:
        """
        Set if camera up orientation within AIS_NavigationMode_Orbit rotation mode should be forced Z
        up.
        """

    def ToAllowTouchZRotation(self) -> bool:
        """
        Return TRUE if z-rotation via two-touches gesture is enabled; FALSE by default.
        """

    def SetAllowTouchZRotation(self, theToEnable: bool) -> None:
        """Set if z-rotation via two-touches gesture is enabled."""

    def ToAllowRotation(self) -> bool:
        """Return TRUE if camera rotation is allowed; TRUE by default."""

    def SetAllowRotation(self, theToEnable: bool) -> None:
        """Set if camera rotation is allowed."""

    def ToAllowPanning(self) -> bool:
        """Return TRUE if panning is allowed; TRUE by default."""

    def SetAllowPanning(self, theToEnable: bool) -> None:
        """Set if panning is allowed."""

    def ToAllowZooming(self) -> bool:
        """Return TRUE if zooming is allowed; TRUE by default."""

    def SetAllowZooming(self, theToEnable: bool) -> None:
        """Set if zooming is allowed."""

    def ToAllowZFocus(self) -> bool:
        """Return TRUE if ZFocus change is allowed; TRUE by default."""

    def SetAllowZFocus(self, theToEnable: bool) -> None:
        """Set if ZFocus change is allowed."""

    def ToAllowHighlight(self) -> bool:
        """
        Return TRUE if dynamic highlight on mouse move is allowed; TRUE by default.
        """

    def SetAllowHighlight(self, theToEnable: bool) -> None:
        """Set if dragging object is allowed."""

    def ToAllowDragging(self) -> bool:
        """Return TRUE if dragging object is allowed; TRUE by default."""

    def SetAllowDragging(self, theToEnable: bool) -> None:
        """Set if dynamic highlight on mouse move is allowed."""

    def ToStickToRayOnZoom(self) -> bool:
        """
        Return TRUE if picked point should be projected to picking ray on zooming at point; TRUE by
        default.
        """

    def SetStickToRayOnZoom(self, theToEnable: bool) -> None:
        """
        Set if picked point should be projected to picking ray on zooming at point.
        """

    def ToStickToRayOnRotation(self) -> bool:
        """
        Return TRUE if picked point should be projected to picking ray on rotating around point; TRUE
        by default.
        """

    def SetStickToRayOnRotation(self, theToEnable: bool) -> None:
        """
        Set if picked point should be projected to picking ray on rotating around point.
        """

    def ToInvertPitch(self) -> bool:
        """
        Return TRUE if pitch direction should be inverted while processing
        Aspect_VKey_NavLookUp/Aspect_VKey_NavLookDown; FALSE by default.
        """

    def SetInvertPitch(self, theToInvert: bool) -> None:
        """Set flag inverting pitch direction."""

    def WalkSpeedAbsolute(self) -> float:
        """Return normal walking speed, in m/s; 1.5 by default."""

    def SetWalkSpeedAbsolute(self, theSpeed: float) -> None:
        """Set normal walking speed, in m/s; 1.5 by default."""

    def WalkSpeedRelative(self) -> float:
        """Return walking speed relative to scene bounding box; 0.1 by default."""

    def SetWalkSpeedRelative(self, theFactor: float) -> None:
        """Set walking speed relative to scene bounding box."""

    def ThrustSpeed(self) -> float:
        """Return active thrust value; 0.0f by default."""

    def SetThrustSpeed(self, theSpeed: float) -> None:
        """Set active thrust value."""

    def HasPreviousMoveTo(self) -> bool:
        """Return TRUE if previous position of MoveTo has been defined."""

    def PreviousMoveTo(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return previous position of MoveTo event in 3D viewer."""

    def ResetPreviousMoveTo(self) -> None:
        """Reset previous position of MoveTo."""

    def ToDisplayXRAuxDevices(self) -> bool:
        """
        Return TRUE to display auxiliary tracked XR devices (like tracking stations).
        """

    def SetDisplayXRAuxDevices(self, theToDisplay: bool) -> None:
        """Set if auxiliary tracked XR devices should be displayed."""

    def ToDisplayXRHands(self) -> bool:
        """Return TRUE to display XR hand controllers."""

    def SetDisplayXRHands(self, theToDisplay: bool) -> None:
        """Set if tracked XR hand controllers should be displayed."""

    def ChangeKeys(self) -> nanoocp.Aspect.Aspect_VKeySet:
        """Return keyboard state."""

    def Keys(self) -> nanoocp.Aspect.Aspect_VKeySet:
        """
        @name keyboard input
        Return keyboard state.
        """

    def KeyDown(self, theKey: int, theTime: float, thePressure: float = 1.0) -> None:
        """
        Press key.
        Default implementation updates internal cache.
        @param theKey key pressed
        @param theTime event timestamp
        """

    def KeyUp(self, theKey: int, theTime: float) -> None:
        """
        Release key.
        Default implementation updates internal cache.
        @param theKey key pressed
        @param theTime event timestamp
        """

    def KeyFromAxis(self, theNegative: int, thePositive: int, theTime: float, thePressure: float) -> None:
        """
        Simulate key up/down events from axis value.
        Default implementation updates internal cache.
        """

    def FetchNavigationKeys(self, theCrouchRatio: float, theRunRatio: float) -> AIS_WalkDelta:
        """Fetch active navigation actions."""

    def MouseGestureMap(self) -> nanoocp.NCollection.NCollection_DataMap__unsigned_int__AIS_MouseGesture:
        """
        @name mouse input
        Return map defining mouse gestures.
        """

    def ChangeMouseGestureMap(self) -> nanoocp.NCollection.NCollection_DataMap__unsigned_int__AIS_MouseGesture:
        """Return map defining mouse gestures."""

    def MouseSelectionSchemes(self) -> nanoocp.NCollection.NCollection_DataMap__unsigned_int__AIS_SelectionScheme:
        """Return map defining mouse selection schemes."""

    def ChangeMouseSelectionSchemes(self) -> nanoocp.NCollection.NCollection_DataMap__unsigned_int__AIS_SelectionScheme:
        """Return map defining mouse gestures."""

    def MouseDoubleClickInterval(self) -> float:
        """Return double click interval in seconds; 0.4 by default."""

    def SetMouseDoubleClickInterval(self, theSeconds: float) -> None:
        """Set double click interval in seconds."""

    @overload
    def SelectInViewer(self, thePnt: nanoocp.BVH.BVH_Vec2i, theScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> None:
        """
        Perform selection in 3D viewer.
        This method is expected to be called from UI thread.
        @param thePnt picking point
        @param theScheme selection scheme
        """

    @overload
    def SelectInViewer(self, thePnts: nanoocp.NCollection.NCollection_Sequence[nanoocp.BVH.BVH_Vec2i], theScheme: AIS_SelectionScheme = AIS_SelectionScheme.AIS_SelectionScheme_Replace) -> None:
        """
        Perform selection in 3D viewer.
        This method is expected to be called from UI thread.
        @param thePnts picking point
        @param theScheme selection scheme
        """

    def UpdateRubberBand(self, thePntFrom: nanoocp.BVH.BVH_Vec2i, thePntTo: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Update rectangle selection tool.
        This method is expected to be called from UI thread.
        @param thePntFrom rectangle first   corner
        @param thePntTo   rectangle another corner
        """

    def UpdatePolySelection(self, thePnt: nanoocp.BVH.BVH_Vec2i, theToAppend: bool) -> None:
        """
        Update polygonal selection tool.
        This method is expected to be called from UI thread.
        @param thePnt new point to add to polygon
        @param theToAppend append new point or update the last point
        """

    def UpdateZoom(self, theDelta: nanoocp.Aspect.Aspect_ScrollDelta) -> bool:
        """
        Update zoom event (e.g. from mouse scroll).
        This method is expected to be called from UI thread.
        @param theDelta mouse cursor position to zoom at and zoom delta
        @return TRUE if new zoom event has been created or FALSE if existing one has been updated
        """

    def UpdateZRotation(self, theAngle: float) -> bool:
        """
        Update Z rotation event.
        @param theAngle rotation angle, in radians.
        @return TRUE if new zoom event has been created or FALSE if existing one has been updated
        """

    def UpdateMouseScroll(self, theDelta: nanoocp.Aspect.Aspect_ScrollDelta) -> bool:
        """
        Update mouse scroll event; redirects to UpdateZoom by default.
        This method is expected to be called from UI thread.
        @param theDelta mouse cursor position and delta
        @return TRUE if new event has been created or FALSE if existing one has been updated
        """

    def UpdateMouseButtons(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButtons: int, theModifiers: int, theIsEmulated: bool) -> bool:
        """
        Handle mouse button press/release event.
        This method is expected to be called from UI thread.
        @param thePoint      mouse cursor position
        @param theButtons    pressed buttons
        @param theModifiers  key modifiers
        @param theIsEmulated if TRUE then mouse event comes NOT from real mouse
        but emulated from non-precise input like touch on screen
        @return TRUE if View should be redrawn
        """

    def UpdateMousePosition(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButtons: int, theModifiers: int, theIsEmulated: bool) -> bool:
        """
        Handle mouse cursor movement event.
        This method is expected to be called from UI thread.
        @param thePoint      mouse cursor position
        @param theButtons    pressed buttons
        @param theModifiers  key modifiers
        @param theIsEmulated if TRUE then mouse event comes NOT from real mouse
        but emulated from non-precise input like touch on screen
        @return TRUE if View should be redrawn
        """

    def UpdateMouseClick(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsDoubleClick: bool) -> bool:
        """
        Handle mouse button click event (emulated by UpdateMouseButtons() while releasing single
        button). Note that as this method is called by UpdateMouseButtons(), it should be executed
        from UI thread. Default implementation redirects to SelectInViewer(). This method is expected
        to be called from UI thread.
        @param thePoint      mouse cursor position
        @param theButton     clicked button
        @param theModifiers  key modifiers
        @param theIsDoubleClick flag indicating double mouse click
        @return TRUE if View should be redrawn
        """

    def PressMouseButton(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsEmulated: bool) -> bool:
        """
        Handle mouse button press event.
        This method is expected to be called from UI thread.
        Default implementation redirects to UpdateMousePosition().
        @param thePoint      mouse cursor position
        @param theButton     pressed button
        @param theModifiers  key modifiers
        @param theIsEmulated if TRUE then mouse event comes NOT from real mouse
        but emulated from non-precise input like touch on screen
        @return TRUE if window content should be redrawn
        """

    def ReleaseMouseButton(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsEmulated: bool) -> bool:
        """
        Handle mouse button release event.
        This method is expected to be called from UI thread.
        Default implementation redirects to UpdateMousePosition().
        @param thePoint      mouse cursor position
        @param theButton     released button
        @param theModifiers  key modifiers
        @param theIsEmulated if TRUE then mouse event comes NOT from real mouse
        but emulated from non-precise input like touch on screen
        @return TRUE if window content should be redrawn
        """

    def LastMouseFlags(self) -> int:
        """Return active key modifiers passed with last mouse event."""

    def LastMousePosition(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return last mouse position."""

    def PressedMouseButtons(self) -> int:
        """Return currently pressed mouse buttons."""

    def TouchToleranceScale(self) -> float:
        """
        @name multi-touch input
        Return scale factor for adjusting tolerances for starting multi-touch gestures; 1.0 by default
        This scale factor is expected to be computed from touch screen resolution.
        """

    def SetTouchToleranceScale(self, theTolerance: float) -> None:
        """
        Set scale factor for adjusting tolerances for starting multi-touch gestures.
        """

    def AddTouchPoint(self, theId: int, thePnt: nanoocp.BVH.BVH_Vec2d, theClearBefore: bool = False) -> None:
        """
        Add touch point with the given ID.
        This method is expected to be called from UI thread.
        @param theId touch unique identifier
        @param thePnt touch coordinates
        @param theClearBefore if TRUE previously registered touches will be removed
        """

    def RemoveTouchPoint(self, theId: int, theClearSelectPnts: bool = False) -> bool:
        """
        Remove touch point with the given ID.
        This method is expected to be called from UI thread.
        @param theId touch unique identifier
        @param theClearSelectPnts if TRUE will initiate clearing of selection points
        @return TRUE if point has been removed
        """

    def UpdateTouchPoint(self, theId: int, thePnt: nanoocp.BVH.BVH_Vec2d) -> None:
        """
        Update touch point with the given ID.
        If point with specified ID was not registered before, it will be added.
        This method is expected to be called from UI thread.
        @param theId touch unique identifier
        @param thePnt touch coordinates
        """

    def HasTouchPoints(self) -> bool:
        """
        @name multi-touch input
        Return TRUE if touches map is not empty.
        """

    def Update3dMouse(self, theEvent: nanoocp.WNT.WNT_HIDSpaceMouse) -> bool:
        """
        @name 3d mouse input
        Process 3d mouse input event (redirects to translation, rotation and keys).
        """

    def ProcessExpose(self) -> None:
        """
        @name resize events
        Handle expose event (window content has been invalidation and should be redrawn).
        Default implementation does nothing.
        """

    def ProcessConfigure(self, theIsResized: bool) -> None:
        """
        Handle window resize event.
        Default implementation does nothing.
        """

    def ProcessInput(self) -> None:
        """
        Handle window input event immediately.
        Default implementation does nothing - input events are accumulated in internal buffer until
        explicit FlushViewEvents() call.
        """

    def ProcessFocus(self, theIsActivated: bool) -> None:
        """
        Handle focus event.
        Default implementation resets cached input state (pressed keys).
        """

    def ProcessClose(self) -> None:
        """
        Handle window close event.
        Default implementation does nothing.
        """

    def EventTime(self) -> float:
        """Return event time (e.g. current time)."""

    def ResetViewInput(self) -> None:
        """
        Reset input state (pressed keys, mouse buttons, etc.) e.g. on window focus loss.
        This method is expected to be called from UI thread.
        """

    def UpdateViewOrientation(self, theOrientation: nanoocp.V3d.V3d_TypeOfOrientation, theToFitAll: bool) -> None:
        """
        Reset view orientation.
        This method is expected to be called from UI thread.
        """

    def FlushViewEvents(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theToHandle: bool = False) -> None:
        """
        Update buffer for rendering thread.
        This method is expected to be called within synchronization barrier between GUI
        and Rendering threads (e.g. GUI thread should be locked beforehand to avoid data races).
        @param theCtx interactive context
        @param theView active view
        @param theToHandle if TRUE, the HandleViewEvents() will be called
        """

    def HandleViewEvents(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Process events within rendering thread."""

    def OnSelectionChanged(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Callback called by handleMoveTo() on Selection in 3D Viewer.
        This method is expected to be called from rendering thread.
        """

    def OnObjectDragged(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theAction: AIS_DragAction) -> None:
        """
        Callback called by handleMoveTo() on dragging object in 3D Viewer.
        This method is expected to be called from rendering thread.
        """

    def OnSubviewChanged(self, theCtx: AIS_InteractiveContext | None, theOldView: nanoocp.V3d.V3d_View | None, theNewView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Callback called by HandleViewEvents() on Selection of another (sub)view.
        This method is expected to be called from rendering thread.
        """

    def PickPoint(self, thePnt: nanoocp.gp.gp_Pnt, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theCursor: nanoocp.BVH.BVH_Vec2i, theToStickToPickRay: bool) -> bool:
        """
        Pick closest point under mouse cursor.
        This method is expected to be called from rendering thread.
        @param[out] thePnt    result point
        @param[in] theCtx     interactive context
        @param[in] theView    active view
        @param[in] theCursor  mouse cursor
        @param[in] theToStickToPickRay  when TRUE, the result point will lie on picking ray
        @return TRUE if result has been found
        """

    def PickAxis(self, theTopPnt: nanoocp.gp.gp_Pnt, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theAxis: nanoocp.gp.gp_Ax1) -> bool:
        """
        Pick closest point by axis.
        This method is expected to be called from rendering thread.
        @param[out] theTopPnt  result point
        @param[in] theCtx     interactive context
        @param[in] theView    active view
        @param[in] theAxis    selection axis
        @return TRUE if result has been found
        """

    def GravityPoint(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> nanoocp.gp.gp_Pnt:
        """
        Compute rotation gravity center point depending on rotation mode.
        This method is expected to be called from rendering thread.
        """

    def FitAllAuto(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Modify view camera to fit all objects.
        Default implementation fits either all visible and all selected objects (swapped on each
        call).
        """

    def handleViewOrientationKeys(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Handle hot-keys defining new camera orientation (Aspect_VKey_ViewTop and similar keys).
        Default implementation starts an animated transaction from the current to the target camera
        orientation, when specific action key was pressed. This method is expected to be called from
        rendering thread.
        """

    def handleNavigationKeys(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> AIS_WalkDelta:
        """
        Perform navigation (Aspect_VKey_NavForward and similar keys).
        This method is expected to be called from rendering thread.
        """

    def handleCameraActions(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theWalk: AIS_WalkDelta) -> None:
        """
        Perform immediate camera actions (rotate/zoom/pan) on gesture progress.
        This method is expected to be called from rendering thread.
        """

    def handleMoveTo(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Perform moveto/selection/dragging.
        This method is expected to be called from rendering thread.
        """

    def toAskNextFrame(self) -> bool:
        """Return TRUE if another frame should be drawn right after this one."""

    def setAskNextFrame(self, theToDraw: bool = True) -> None:
        """Set if another frame should be drawn right after this one."""

    def hasPanningAnchorPoint(self) -> bool:
        """Return if panning anchor point has been defined."""

    def panningAnchorPoint(self) -> nanoocp.gp.gp_Pnt:
        """Return active panning anchor point."""

    def setPanningAnchorPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Set active panning anchor point."""

    def handlePanning(self, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Handle panning event myGL.Panning."""

    def handleZRotate(self, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Handle Z rotation event myGL.ZRotate."""

    def MinZoomDistance(self) -> float:
        """Return minimal camera distance for zoom operation."""

    def SetMinZoomDistance(self, theDist: float) -> None:
        """Set minimal camera distance for zoom operation."""

    def handleZoom(self, theView: nanoocp.V3d.V3d_View | None, theParams: nanoocp.Aspect.Aspect_ScrollDelta, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Handle zoom event myGL.ZoomActions.
        This method is expected to be called from rendering thread.
        """

    def handleZFocusScroll(self, theView: nanoocp.V3d.V3d_View | None, theParams: nanoocp.Aspect.Aspect_ScrollDelta) -> None:
        """
        Handle ZScroll event myGL.ZoomActions.
        This method is expected to be called from rendering thread.
        """

    def handleOrbitRotation(self, theView: nanoocp.V3d.V3d_View | None, thePnt: nanoocp.gp.gp_Pnt, theToLockZUp: bool) -> None:
        """
        Handle orbital rotation events myGL.OrbitRotation.
        @param theView view to modify
        @param thePnt 3D point to rotate around
        @param theToLockZUp amend camera to exclude roll angle (put camera Up vector to plane
        containing global Z and view direction)
        """

    def handleViewRotation(self, theView: nanoocp.V3d.V3d_View | None, theYawExtra: float, thePitchExtra: float, theRoll: float, theToRestartOnIncrement: bool) -> None:
        """
        Handle view direction rotation events myGL.ViewRotation.
        This method is expected to be called from rendering thread.
        @param theView       camera to modify
        @param theYawExtra   extra yaw increment
        @param thePitchExtra extra pitch increment
        @param theRoll       roll value
        @param theToRestartOnIncrement flag indicating flight mode
        """

    def handleViewRedraw(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """
        Handle view redraw.
        This method is expected to be called from rendering thread.
        """

    def handleXRInput(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, theWalk: AIS_WalkDelta) -> None:
        """
        Perform XR input.
        This method is expected to be called from rendering thread.
        """

    def handleXRTurnPad(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Handle trackpad view turn action."""

    def handleXRTeleport(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Handle trackpad teleportation action."""

    def handleXRPicking(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Handle picking on trigger click."""

    def handleXRHighlight(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Perform dynamic highlighting for active hand."""

    def handleXRPresentations(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None) -> None:
        """Display auxiliary XR presentations."""

    def handleXRMoveTo(self, theCtx: AIS_InteractiveContext | None, theView: nanoocp.V3d.V3d_View | None, thePose: nanoocp.gp.gp_Trsf, theToHighlight: bool) -> int:
        """Perform picking with/without dynamic highlighting for XR pose."""

class AIS_ViewCube(AIS_InteractiveObject):
    """
    Interactive object for displaying the view manipulation cube.

    View cube consists of several parts that are responsible for different camera manipulations:
    @li Cube sides represent main views: top, bottom, left, right, front and back.
    @li Edges represent rotation of one of main views on 45 degrees.
    @li Vertices represent rotation of one of man views in two directions.

    The object is expected to behave like a trihedron in the view corner,
    therefore its position should be defined using transformation persistence flags:
    @code SetTransformPersistence (new Graphic3d_TransformPers (Graphic3d_TMF_TriedronPers,
    Aspect_TOTP_LEFT_LOWER, NCollection_Vec2<int> (100, 100)); @endcode

    View Cube parts are sensitive to detection, or dynamic highlighting (but not selection),
    and every its owner AIS_ViewCubeOwner corresponds to camera transformation.
    @code
    for (aViewCube->StartAnimation (aDetectedOwner); aViewCube->HasAnimation(); )
    {
    aViewCube->UpdateAnimation();
    ... // updating of application window
    }
    @endcode
    or
    @code aViewCube->HandleClick (aDetectedOwner); @endcode
    that includes transformation loop.
    This loop allows external actions like application updating. For this purpose AIS_ViewCube has
    virtual interface onAfterAnimation(), that is to be redefined on application level.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: AIS_ViewCube) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsBoxSide(theOrient: nanoocp.V3d.V3d_TypeOfOrientation) -> bool:
        """Return TRUE if specified orientation belongs to box side."""

    @staticmethod
    def IsBoxEdge(theOrient: nanoocp.V3d.V3d_TypeOfOrientation) -> bool:
        """Return TRUE if specified orientation belongs to box edge."""

    @staticmethod
    def IsBoxCorner(theOrient: nanoocp.V3d.V3d_TypeOfOrientation) -> bool:
        """Return TRUE if specified orientation belongs to box corner (vertex)."""

    def ViewAnimation(self) -> AIS_AnimationCamera:
        """Return view animation."""

    def SetViewAnimation(self, theAnimation: AIS_AnimationCamera | None) -> None:
        """Set view animation."""

    def ToAutoStartAnimation(self) -> bool:
        """
        Return TRUE if automatic camera transformation on selection (highlighting) is enabled; TRUE by
        default.
        """

    def SetAutoStartAnimation(self, theToEnable: bool) -> None:
        """
        Enable/disable automatic camera transformation on selection (highlighting).
        The automatic logic can be disabled if application wants performing action manually
        basing on picking results (AIS_ViewCubeOwner).
        """

    def IsFixedAnimationLoop(self) -> bool:
        """
        Return TRUE if camera animation should be done in uninterruptible loop; TRUE by default.
        """

    def SetFixedAnimationLoop(self, theToEnable: bool) -> None:
        """Set if camera animation should be done in uninterruptible loop."""

    def ResetStyles(self) -> None:
        """
        Reset all size and style parameters to default.
        @warning It doesn't reset position of View Cube
        """

    def Size(self) -> float:
        """
        @name Geometry management API
        @return size (width and height) of View cube sides; 100 by default.
        """

    def SetSize(self, theValue: float, theToAdaptAnother: bool = True) -> None:
        """
        Sets size (width and height) of View cube sides.
        @param theToAdaptAnother if TRUE, then other parameters will be adapted to specified size
        """

    def BoxFacetExtension(self) -> float:
        """Return box facet extension to edge/corner facet split; 10 by default."""

    def SetBoxFacetExtension(self, theValue: float) -> None:
        """Set new value of box facet extension."""

    def AxesPadding(self) -> float:
        """Return padding between axes and 3D part (box); 10 by default."""

    def SetAxesPadding(self, theValue: float) -> None:
        """Set new value of padding between axes and 3D part (box)."""

    def BoxEdgeGap(self) -> float:
        """Return gap between box edges and box sides; 0 by default."""

    def SetBoxEdgeGap(self, theValue: float) -> None:
        """Set new value of box edges gap."""

    def BoxEdgeMinSize(self) -> float:
        """Return minimal size of box edge; 2 by default."""

    def SetBoxEdgeMinSize(self, theValue: float) -> None:
        """Set new value of box edge minimal size."""

    def BoxCornerMinSize(self) -> float:
        """Return minimal size of box corner; 2 by default."""

    def SetBoxCornerMinSize(self, theValue: float) -> None:
        """Set new value of box corner minimal size."""

    def RoundRadius(self) -> float:
        """
        Return relative radius of side corners (round rectangle); 0.0 by default.
        The value in within [0, 0.5] range meaning absolute radius = RoundRadius() / Size().
        """

    def SetRoundRadius(self, theValue: float) -> None:
        """
        Set relative radius of View Cube sides corners (round rectangle).
        The value should be within [0, 0.5] range.
        """

    def AxesRadius(self) -> float:
        """Returns radius of axes of the trihedron; 1.0 by default."""

    def SetAxesRadius(self, theRadius: float) -> None:
        """Sets radius of axes of the trihedron."""

    def AxesConeRadius(self) -> float:
        """Returns radius of cone of axes of the trihedron; 3.0 by default."""

    def SetAxesConeRadius(self, theRadius: float) -> None:
        """Sets radius of cone of axes of the trihedron."""

    def AxesSphereRadius(self) -> float:
        """
        Returns radius of sphere (central point) of the trihedron; 4.0 by default.
        """

    def SetAxesSphereRadius(self, theRadius: float) -> None:
        """Sets radius of sphere (central point) of the trihedron."""

    def ToDrawAxes(self) -> bool:
        """@return TRUE if trihedron is drawn; TRUE by default."""

    def SetDrawAxes(self, theValue: bool) -> None:
        """Enable/disable drawing of trihedron."""

    def ToDrawEdges(self) -> bool:
        """@return TRUE if edges of View Cube is drawn; TRUE by default."""

    def SetDrawEdges(self, theValue: bool) -> None:
        """Enable/disable drawing of edges of View Cube."""

    def ToDrawVertices(self) -> bool:
        """
        Return TRUE if vertices (vertex) of View Cube is drawn; TRUE by default.
        """

    def SetDrawVertices(self, theValue: bool) -> None:
        """Enable/disable drawing of vertices (corners) of View Cube."""

    def IsYup(self) -> bool:
        """
        Return TRUE if application expects Y-up viewer orientation instead of Z-up; FALSE by default.
        """

    def SetYup(self, theIsYup: bool, theToUpdateLabels: bool = True) -> None:
        """Set if application expects Y-up viewer orientation instead of Z-up."""

    def BoxSideStyle(self) -> nanoocp.Prs3d.Prs3d_ShadingAspect:
        """
        @name Style management API
        Return shading style of box sides.
        """

    def BoxEdgeStyle(self) -> nanoocp.Prs3d.Prs3d_ShadingAspect:
        """Return shading style of box edges."""

    def BoxCornerStyle(self) -> nanoocp.Prs3d.Prs3d_ShadingAspect:
        """Return shading style of box corners."""

    def BoxColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return value of front color for the 3D part of object."""

    def SetBoxColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Set new value of front color for the 3D part of object.
        @param[in] theColor  input color value.
        """

    def BoxTransparency(self) -> float:
        """Return transparency for 3D part of object."""

    def SetBoxTransparency(self, theValue: float) -> None:
        """
        Set new value of transparency for 3D part of object.
        @param[in] theValue  input transparency value
        """

    def InnerColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return color of sides back material."""

    def SetInnerColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Set color of sides back material. Alias for:
        @code Attributes()->ShadingAspect()->Aspect()->ChangeBackMaterial().SetColor() @endcode
        """

    def BoxSideLabel(self, theSide: nanoocp.V3d.V3d_TypeOfOrientation) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return box side label or empty string if undefined.
        Default labels: FRONT, BACK, LEFT, RIGHT, TOP, BOTTOM.
        """

    def SetBoxSideLabel(self, theSide: nanoocp.V3d.V3d_TypeOfOrientation, theLabel: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set box side label."""

    def TextColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return text color of labels of box sides; BLACK by default."""

    def SetTextColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Set color of text labels on box sides. Alias for:
        @code Attributes()->TextAspect()->SetColor() @endcode
        """

    def Font(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return font name that is used for displaying of sides and axes text. Alias for:
        @code Attributes()->TextAspect()->Aspect()->SetFont() @endcode
        """

    def SetFont(self, theFont: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Set font name that is used for displaying of sides and axes text. Alias for:
        @code Attributes()->TextAspect()->SetFont() @endcode
        """

    def FontHeight(self) -> float:
        """Return height of font"""

    def SetFontHeight(self, theValue: float) -> None:
        """
        Change font height. Alias for:
        @code Attributes()->TextAspect()->SetHeight() @endcode
        """

    def AxisLabel(self, theAxis: nanoocp.Prs3d.Prs3d_DatumParts) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return axes labels or empty string if undefined.
        Default labels: X, Y, Z.
        """

    def SetAxesLabels(self, theX: nanoocp.TCollection.TCollection_AsciiString, theY: nanoocp.TCollection.TCollection_AsciiString, theZ: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set axes labels."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Set new value of color for the whole object.
        @param[in] theColor  input color value.
        """

    def UnsetColor(self) -> None:
        """Reset color for the whole object."""

    def SetTransparency(self, theValue: float) -> None:
        """
        Set new value of transparency for the whole object.
        @param[in] theValue  input transparency value.
        """

    def UnsetTransparency(self) -> None:
        """Reset transparency for the whole object."""

    def SetMaterial(self, theMat: nanoocp.Graphic3d.Graphic3d_MaterialAspect) -> None:
        """Sets the material for the interactive object."""

    def UnsetMaterial(self) -> None:
        """Sets the material for the interactive object."""

    def Duration(self) -> float:
        """
        @name animation methods
        Return duration of animation in seconds; 0.5 sec by default
        """

    def SetDuration(self, theValue: float) -> None:
        """
        Set duration of animation.
        @param[in] theValue  input value of duration in seconds
        """

    def ToResetCameraUp(self) -> bool:
        """
        Return TRUE if new camera Up direction should be always set to default value for a new camera
        Direction; FALSE by default. When this flag is FALSE, the new camera Up will be set as current
        Up orthogonalized to the new camera Direction, and will set to default Up on second click.
        """

    def SetResetCamera(self, theToReset: bool) -> None:
        """
        Set if new camera Up direction should be always set to default value for a new camera
        Direction.
        """

    def ToFitSelected(self) -> bool:
        """
        Return TRUE if animation should fit selected objects and FALSE to fit entire scene; TRUE by
        default.
        """

    def SetFitSelected(self, theToFitSelected: bool) -> None:
        """Set if animation should fit selected objects or to fit entire scene."""

    def HasAnimation(self) -> bool:
        """@return TRUE if View Cube has unfinished animation of view camera."""

    def StartAnimation(self, theOwner: AIS_ViewCubeOwner | None) -> None:
        """
        Start camera transformation corresponding to the input detected owner.
        @param[in] theOwner  detected owner.
        """

    def UpdateAnimation(self, theToUpdate: bool) -> bool:
        """
        Perform one step of current camera transformation.
        theToUpdate[in]  enable/disable update of view.
        @return TRUE if animation is not stopped.
        """

    def HandleClick(self, theOwner: AIS_ViewCubeOwner | None) -> None:
        """
        Perform camera transformation corresponding to the input detected owner.
        """

    def AcceptDisplayMode(self, theMode: int) -> bool:
        """
        @name Presentation computation
        Return TRUE for supported display mode.
        """

    def GlobalSelOwner(self) -> nanoocp.SelectMgr.SelectMgr_EntityOwner:
        """Global selection has no meaning for this class."""

    def Compute(self, thePrsMgr: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theMode: int = 0) -> None:
        """
        Compute 3D part of View Cube.
        @param[in] thePrsMgr  presentation manager.
        @param[in] thePrs  input presentation that is to be filled with flat presentation primitives.
        @param[in] theMode  display mode.
        @warning this object accept only 0 display mode.
        """

    def ComputeSelection(self, theSelection: nanoocp.SelectMgr.SelectMgr_Selection | None, theMode: int) -> None:
        """
        Redefine computing of sensitive entities for View Cube.
        @param[in] theSelection  input selection object that is to be filled with sensitive entities.
        @param[in] theMode  selection mode.
        @warning object accepts only 0 selection mode.
        """

    def IsAutoHilight(self) -> bool:
        """
        Disables auto highlighting to use HilightSelected() and HilightOwnerWithColor() overridden
        methods.
        """

    def ClearSelected(self) -> None:
        """
        Method which clear all selected owners belonging to this selectable object.
        @warning this object does not support selection.
        """

    def HilightOwnerWithColor(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theStyle: nanoocp.Prs3d.Prs3d_Drawer | None, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None) -> None:
        """
        Method which highlights input owner belonging to this selectable object.
        @param[in] thePM  presentation manager
        @param[in] theStyle  style for dynamic highlighting.
        @param[in] theOwner  input entity owner.
        """

    def HilightSelected(self, thePM: nanoocp.PrsMgr.PrsMgr_PresentationManager | None, theSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.SelectMgr.SelectMgr_EntityOwner]) -> None:
        """Method which draws selected owners."""

    def UnsetAttributes(self) -> None:
        """
        Set default parameters for visual attributes
        @sa Attributes()
        """

    def UnsetHilightAttributes(self) -> None:
        """
        Set default parameters for dynamic highlighting attributes, reset highlight attributes
        """

class AIS_ViewCubeOwner(nanoocp.SelectMgr.SelectMgr_EntityOwner):
    """
    Redefined entity owner that is highlighted when owner is detected,
    even if Interactive Context highlighted on last detection procedure.
    """

    @overload
    def __init__(self, theObject: AIS_ViewCube | None, theOrient: nanoocp.V3d.V3d_TypeOfOrientation, thePriority: int = 5) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: AIS_ViewCubeOwner) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsForcedHilight(self) -> bool:
        """
        @return TRUE. This owner will always call method
        Hilight for its Selectable Object when the owner is detected.
        """

    def MainOrientation(self) -> nanoocp.V3d.V3d_TypeOfOrientation:
        """Return new orientation to set."""

    def HandleMouseClick(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButton: int, theModifiers: int, theIsDoubleClick: bool) -> bool:
        """Handle mouse button click event."""

class AIS_ViewCubeSensitive(nanoocp.Select3D.Select3D_SensitivePrimitiveArray):
    """Simple sensitive element for picking by point only."""

    @overload
    def __init__(self, theOwner: nanoocp.SelectMgr.SelectMgr_EntityOwner | None, theTris: nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: AIS_ViewCubeSensitive) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Matches(self, theMgr: nanoocp.SelectBasics.SelectBasics_SelectingVolumeManager, thePickResult: nanoocp.SelectBasics.SelectBasics_PickResult) -> bool:
        """Checks whether element overlaps current selecting volume."""

class AIS_XRTrackedDevice(AIS_InteractiveObject):
    """Auxiliary textured mesh presentation of tracked XR device."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theTris: nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles | None, theTexture: nanoocp.Image.Image_Texture | None) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: AIS_XRTrackedDevice) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Role(self) -> nanoocp.Aspect.Aspect_XRTrackedDeviceRole:
        """Return device role."""

    def SetRole(self, theRole: nanoocp.Aspect.Aspect_XRTrackedDeviceRole) -> None:
        """Set device role."""

    def LaserColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return laser color."""

    def SetLaserColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Set laser color."""

    def LaserLength(self) -> float:
        """Return laser length."""

    def SetLaserLength(self, theLength: float) -> None:
        """Set laser length."""

    def UnitFactor(self) -> float:
        """Return unit scale factor."""

    def SetUnitFactor(self, theFactor: float) -> None:
        """Set unit scale factor."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.AIS
import nanoocp.TopTools
AIS_DataMapOfShapeDrawer = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.AIS.AIS_ColoredDrawer, nanoocp.TopTools.TopTools_ShapeMapHasher]
AIS_ListOfInteractive = nanoocp.NCollection.NCollection_List[nanoocp.AIS.AIS_InteractiveObject]
AIS_NArray1OfEntityOwner = nanoocp.NCollection.NCollection_Array1[nanoocp.SelectMgr.SelectMgr_EntityOwner]
AIS_NListOfEntityOwner = nanoocp.NCollection.NCollection_List[nanoocp.SelectMgr.SelectMgr_EntityOwner]
