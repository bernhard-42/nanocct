"""OCCT package Aspect (toolkit TKService)"""

import enum
from typing import overload

import nanoocp.BVH
import nanoocp.Graphic3d
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.WNT
import nanoocp.gp


class Aspect_GridDrawMode(enum.IntEnum):
    """
    Defines the grid draw mode. The grid may be drawn
    by using lines or points.
    """

    Aspect_GDM_Lines = 0

    Aspect_GDM_Points = 1

    Aspect_GDM_None = 2

Aspect_GDM_Lines: Aspect_GridDrawMode = Aspect_GridDrawMode.Aspect_GDM_Lines

Aspect_GDM_Points: Aspect_GridDrawMode = Aspect_GridDrawMode.Aspect_GDM_Points

Aspect_GDM_None: Aspect_GridDrawMode = Aspect_GridDrawMode.Aspect_GDM_None

class Aspect_ColorSpace(enum.IntEnum):
    """Texture color spaces accepted by XR composer."""

    Aspect_ColorSpace_sRGB = 0

    Aspect_ColorSpace_Linear = 1

Aspect_ColorSpace_sRGB: Aspect_ColorSpace = Aspect_ColorSpace.Aspect_ColorSpace_sRGB

Aspect_ColorSpace_Linear: Aspect_ColorSpace = Aspect_ColorSpace.Aspect_ColorSpace_Linear

class Aspect_XAtom(enum.IntEnum):
    """
    Defines custom identifiers(atoms) for X window custom named properties

    Category: Instantiated classes
    """

    Aspect_XA_DELETE_WINDOW = 0

Aspect_XA_DELETE_WINDOW: Aspect_XAtom = Aspect_XAtom.Aspect_XA_DELETE_WINDOW

class Aspect_Eye(enum.IntEnum):
    """Camera eye index within stereoscopic pair."""

    Aspect_Eye_Left = 0

    Aspect_Eye_Right = 1

Aspect_Eye_Left: Aspect_Eye = Aspect_Eye.Aspect_Eye_Left

Aspect_Eye_Right: Aspect_Eye = Aspect_Eye.Aspect_Eye_Right

class Aspect_FillMethod(enum.IntEnum):
    """
    Defines the fill methods to
    write bitmaps in a window.
    """

    Aspect_FM_NONE = 0

    Aspect_FM_CENTERED = 1

    Aspect_FM_TILED = 2

    Aspect_FM_STRETCH = 3

Aspect_FM_NONE: Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_NONE

Aspect_FM_CENTERED: Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_CENTERED

Aspect_FM_TILED: Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_TILED

Aspect_FM_STRETCH: Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_STRETCH

class Aspect_GradientFillMethod(enum.IntEnum):
    """Defines the fill methods to write gradient background in a window."""

    Aspect_GradientFillMethod_None = 0

    Aspect_GradientFillMethod_Horizontal = 1

    Aspect_GradientFillMethod_Vertical = 2

    Aspect_GradientFillMethod_Diagonal1 = 3

    Aspect_GradientFillMethod_Diagonal2 = 4

    Aspect_GradientFillMethod_Corner1 = 5

    Aspect_GradientFillMethod_Corner2 = 6

    Aspect_GradientFillMethod_Corner3 = 7

    Aspect_GradientFillMethod_Corner4 = 8

    Aspect_GradientFillMethod_Elliptical = 9

    Aspect_GFM_NONE = 0

    Aspect_GFM_HOR = 1

    Aspect_GFM_VER = 2

    Aspect_GFM_DIAG1 = 3

    Aspect_GFM_DIAG2 = 4

    Aspect_GFM_CORNER1 = 5

    Aspect_GFM_CORNER2 = 6

    Aspect_GFM_CORNER3 = 7

    Aspect_GFM_CORNER4 = 8

Aspect_GradientFillMethod_None: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Horizontal: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Vertical: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Diagonal1: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Diagonal2: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Corner1: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Corner2: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Corner3: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Corner4: Aspect_GradientFillMethod = ...

Aspect_GradientFillMethod_Elliptical: Aspect_GradientFillMethod = ...

Aspect_GFM_NONE: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_NONE

Aspect_GFM_HOR: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_HOR

Aspect_GFM_VER: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_VER

Aspect_GFM_DIAG1: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_DIAG1

Aspect_GFM_DIAG2: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_DIAG2

Aspect_GFM_CORNER1: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_CORNER1

Aspect_GFM_CORNER2: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_CORNER2

Aspect_GFM_CORNER3: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_CORNER3

Aspect_GFM_CORNER4: Aspect_GradientFillMethod = Aspect_GradientFillMethod.Aspect_GFM_CORNER4

class Aspect_GraphicsLibrary(enum.IntEnum):
    """Graphics API enumeration."""

    Aspect_GraphicsLibrary_OpenGL = 0

    Aspect_GraphicsLibrary_OpenGLES = 1

Aspect_GraphicsLibrary_OpenGL: Aspect_GraphicsLibrary = ...

Aspect_GraphicsLibrary_OpenGLES: Aspect_GraphicsLibrary = ...

class Aspect_GridType(enum.IntEnum):
    """Defines the grid type : Rectangular or Circular."""

    Aspect_GT_Rectangular = 0

    Aspect_GT_Circular = 1

Aspect_GT_Rectangular: Aspect_GridType = Aspect_GridType.Aspect_GT_Rectangular

Aspect_GT_Circular: Aspect_GridType = Aspect_GridType.Aspect_GT_Circular

class Aspect_TypeOfResize(enum.IntEnum):
    """
    Defines the type of Resize Window method applied
    by the user.
    """

    Aspect_TOR_UNKNOWN = 0

    Aspect_TOR_NO_BORDER = 1

    Aspect_TOR_TOP_BORDER = 2

    Aspect_TOR_RIGHT_BORDER = 3

    Aspect_TOR_BOTTOM_BORDER = 4

    Aspect_TOR_LEFT_BORDER = 5

    Aspect_TOR_TOP_AND_RIGHT_BORDER = 6

    Aspect_TOR_RIGHT_AND_BOTTOM_BORDER = 7

    Aspect_TOR_BOTTOM_AND_LEFT_BORDER = 8

    Aspect_TOR_LEFT_AND_TOP_BORDER = 9

Aspect_TOR_UNKNOWN: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_UNKNOWN

Aspect_TOR_NO_BORDER: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_NO_BORDER

Aspect_TOR_TOP_BORDER: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_TOP_BORDER

Aspect_TOR_RIGHT_BORDER: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_RIGHT_BORDER

Aspect_TOR_BOTTOM_BORDER: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_BOTTOM_BORDER

Aspect_TOR_LEFT_BORDER: Aspect_TypeOfResize = Aspect_TypeOfResize.Aspect_TOR_LEFT_BORDER

Aspect_TOR_TOP_AND_RIGHT_BORDER: Aspect_TypeOfResize = ...

Aspect_TOR_RIGHT_AND_BOTTOM_BORDER: Aspect_TypeOfResize = ...

Aspect_TOR_BOTTOM_AND_LEFT_BORDER: Aspect_TypeOfResize = ...

Aspect_TOR_LEFT_AND_TOP_BORDER: Aspect_TypeOfResize = ...

class Aspect_XRActionType(enum.IntEnum):
    """XR action type."""

    Aspect_XRActionType_InputDigital = 0

    Aspect_XRActionType_InputAnalog = 1

    Aspect_XRActionType_InputPose = 2

    Aspect_XRActionType_InputSkeletal = 3

    Aspect_XRActionType_OutputHaptic = 4

Aspect_XRActionType_InputDigital: Aspect_XRActionType = ...

Aspect_XRActionType_InputAnalog: Aspect_XRActionType = ...

Aspect_XRActionType_InputPose: Aspect_XRActionType = Aspect_XRActionType.Aspect_XRActionType_InputPose

Aspect_XRActionType_InputSkeletal: Aspect_XRActionType = ...

Aspect_XRActionType_OutputHaptic: Aspect_XRActionType = ...

class Aspect_XRGenericAction(enum.IntEnum):
    """Generic XR action."""

    Aspect_XRGenericAction_IsHeadsetOn = 0

    Aspect_XRGenericAction_InputAppMenu = 1

    Aspect_XRGenericAction_InputSysMenu = 2

    Aspect_XRGenericAction_InputTriggerPull = 3

    Aspect_XRGenericAction_InputTriggerClick = 4

    Aspect_XRGenericAction_InputGripClick = 5

    Aspect_XRGenericAction_InputTrackPadPosition = 6

    Aspect_XRGenericAction_InputTrackPadTouch = 7

    Aspect_XRGenericAction_InputTrackPadClick = 8

    Aspect_XRGenericAction_InputThumbstickPosition = 9

    Aspect_XRGenericAction_InputThumbstickTouch = 10

    Aspect_XRGenericAction_InputThumbstickClick = 11

    Aspect_XRGenericAction_InputPoseBase = 12

    Aspect_XRGenericAction_InputPoseFront = 13

    Aspect_XRGenericAction_InputPoseHandGrip = 14

    Aspect_XRGenericAction_InputPoseFingerTip = 15

    Aspect_XRGenericAction_OutputHaptic = 16

Aspect_XRGenericAction_IsHeadsetOn: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputAppMenu: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputSysMenu: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputTriggerPull: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputTriggerClick: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputGripClick: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputTrackPadPosition: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputTrackPadTouch: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputTrackPadClick: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputThumbstickPosition: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputThumbstickTouch: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputThumbstickClick: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputPoseBase: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputPoseFront: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputPoseHandGrip: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_InputPoseFingerTip: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_OutputHaptic: Aspect_XRGenericAction = ...

Aspect_XRGenericAction_NB: int = 17

class Aspect_XRTrackedDeviceRole(enum.IntEnum):
    """Predefined tracked devices."""

    Aspect_XRTrackedDeviceRole_Head = 0

    Aspect_XRTrackedDeviceRole_LeftHand = 1

    Aspect_XRTrackedDeviceRole_RightHand = 2

    Aspect_XRTrackedDeviceRole_Other = 3

Aspect_XRTrackedDeviceRole_Head: Aspect_XRTrackedDeviceRole = ...

Aspect_XRTrackedDeviceRole_LeftHand: Aspect_XRTrackedDeviceRole = ...

Aspect_XRTrackedDeviceRole_RightHand: Aspect_XRTrackedDeviceRole = ...

Aspect_XRTrackedDeviceRole_Other: Aspect_XRTrackedDeviceRole = ...

Aspect_XRTrackedDeviceRole_NB: int = 4

class Aspect_HatchStyle(enum.IntEnum):
    """Definition of all available hatch styles."""

    Aspect_HS_SOLID = 0

    Aspect_HS_HORIZONTAL = 7

    Aspect_HS_HORIZONTAL_WIDE = 11

    Aspect_HS_VERTICAL = 8

    Aspect_HS_VERTICAL_WIDE = 12

    Aspect_HS_DIAGONAL_45 = 5

    Aspect_HS_DIAGONAL_45_WIDE = 9

    Aspect_HS_DIAGONAL_135 = 6

    Aspect_HS_DIAGONAL_135_WIDE = 10

    Aspect_HS_GRID = 3

    Aspect_HS_GRID_WIDE = 4

    Aspect_HS_GRID_DIAGONAL = 1

    Aspect_HS_GRID_DIAGONAL_WIDE = 2

    Aspect_HS_NB = 13

Aspect_HS_SOLID: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_SOLID

Aspect_HS_HORIZONTAL: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_HORIZONTAL

Aspect_HS_HORIZONTAL_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_HORIZONTAL_WIDE

Aspect_HS_VERTICAL: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_VERTICAL

Aspect_HS_VERTICAL_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_VERTICAL_WIDE

Aspect_HS_DIAGONAL_45: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45

Aspect_HS_DIAGONAL_45_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_DIAGONAL_45_WIDE

Aspect_HS_DIAGONAL_135: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135

Aspect_HS_DIAGONAL_135_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_DIAGONAL_135_WIDE

Aspect_HS_GRID: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_GRID

Aspect_HS_GRID_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_GRID_WIDE

Aspect_HS_GRID_DIAGONAL: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL

Aspect_HS_GRID_DIAGONAL_WIDE: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_GRID_DIAGONAL_WIDE

Aspect_HS_NB: Aspect_HatchStyle = Aspect_HatchStyle.Aspect_HS_NB

class Aspect_InteriorStyle(enum.IntEnum):
    """Interior types for primitive faces."""

    Aspect_IS_EMPTY = -1

    Aspect_IS_SOLID = 0

    Aspect_IS_HATCH = 1

    Aspect_IS_HIDDENLINE = 2

    Aspect_IS_POINT = 3

    Aspect_IS_HOLLOW = -1

Aspect_IS_EMPTY: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_EMPTY

Aspect_IS_SOLID: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_SOLID

Aspect_IS_HATCH: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_HATCH

Aspect_IS_HIDDENLINE: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_HIDDENLINE

Aspect_IS_POINT: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_POINT

Aspect_IS_HOLLOW: Aspect_InteriorStyle = Aspect_InteriorStyle.Aspect_IS_HOLLOW

class Aspect_PolygonOffsetMode(enum.IntEnum):
    Aspect_POM_Off = 0

    Aspect_POM_Fill = 1

    Aspect_POM_Line = 2

    Aspect_POM_Point = 4

    Aspect_POM_All = 7

    Aspect_POM_None = 8

    Aspect_POM_Mask = 15

Aspect_POM_Off: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_Off

Aspect_POM_Fill: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_Fill

Aspect_POM_Line: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_Line

Aspect_POM_Point: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_Point

Aspect_POM_All: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_All

Aspect_POM_None: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_None

Aspect_POM_Mask: Aspect_PolygonOffsetMode = Aspect_PolygonOffsetMode.Aspect_POM_Mask

Aspect_VKeyFlags_NONE: int = 0

Aspect_VKeyFlags_SHIFT: int = 256

Aspect_VKeyFlags_CTRL: int = 512

Aspect_VKeyFlags_ALT: int = 1024

Aspect_VKeyFlags_MENU: int = 2048

Aspect_VKeyFlags_META: int = 4096

Aspect_VKeyFlags_ALL: int = 7936

Aspect_VKeyMouse_NONE: int = 0

Aspect_VKeyMouse_LeftButton: int = 8192

Aspect_VKeyMouse_MiddleButton: int = 16384

Aspect_VKeyMouse_RightButton: int = 32768

Aspect_VKeyMouse_MainButtons: int = 57344

class Aspect_TypeOfColorScaleData(enum.IntEnum):
    """Defines the using type of colors and labels"""

    Aspect_TOCSD_AUTO = 0

    Aspect_TOCSD_USER = 1

Aspect_TOCSD_AUTO: Aspect_TypeOfColorScaleData = Aspect_TypeOfColorScaleData.Aspect_TOCSD_AUTO

Aspect_TOCSD_USER: Aspect_TypeOfColorScaleData = Aspect_TypeOfColorScaleData.Aspect_TOCSD_USER

class Aspect_TypeOfColorScaleOrientation(enum.IntEnum):
    """Defines the type of color scale orientation"""

    Aspect_TOCSO_NONE = 0

    Aspect_TOCSO_LEFT = 1

    Aspect_TOCSO_RIGHT = 2

    Aspect_TOCSO_CENTER = 3

Aspect_TOCSO_NONE: Aspect_TypeOfColorScaleOrientation = ...

Aspect_TOCSO_LEFT: Aspect_TypeOfColorScaleOrientation = ...

Aspect_TOCSO_RIGHT: Aspect_TypeOfColorScaleOrientation = ...

Aspect_TOCSO_CENTER: Aspect_TypeOfColorScaleOrientation = ...

class Aspect_TypeOfColorScalePosition(enum.IntEnum):
    """Defines the type of position for color scale labels"""

    Aspect_TOCSP_NONE = 0

    Aspect_TOCSP_LEFT = 1

    Aspect_TOCSP_RIGHT = 2

    Aspect_TOCSP_CENTER = 3

Aspect_TOCSP_NONE: Aspect_TypeOfColorScalePosition = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_NONE

Aspect_TOCSP_LEFT: Aspect_TypeOfColorScalePosition = Aspect_TypeOfColorScalePosition.Aspect_TOCSP_LEFT

Aspect_TOCSP_RIGHT: Aspect_TypeOfColorScalePosition = ...

Aspect_TOCSP_CENTER: Aspect_TypeOfColorScalePosition = ...

class Aspect_TypeOfDeflection(enum.IntEnum):
    """
    Defines if the maximal chordial deflection used when
    drawing an object is absolute or relative to the size
    of the object.
    """

    Aspect_TOD_RELATIVE = 0

    Aspect_TOD_ABSOLUTE = 1

Aspect_TOD_RELATIVE: Aspect_TypeOfDeflection = Aspect_TypeOfDeflection.Aspect_TOD_RELATIVE

Aspect_TOD_ABSOLUTE: Aspect_TypeOfDeflection = Aspect_TypeOfDeflection.Aspect_TOD_ABSOLUTE

class Aspect_TypeOfDisplayText(enum.IntEnum):
    """Define the display type of the text."""

    Aspect_TODT_NORMAL = 0

    Aspect_TODT_SUBTITLE = 1

    Aspect_TODT_DEKALE = 2

    Aspect_TODT_BLEND = 3

    Aspect_TODT_DIMENSION = 4

    Aspect_TODT_SHADOW = 5

Aspect_TODT_NORMAL: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL

Aspect_TODT_SUBTITLE: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_SUBTITLE

Aspect_TODT_DEKALE: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_DEKALE

Aspect_TODT_BLEND: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_BLEND

Aspect_TODT_DIMENSION: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_DIMENSION

Aspect_TODT_SHADOW: Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_SHADOW

class Aspect_TypeOfFacingModel(enum.IntEnum):
    Aspect_TOFM_BOTH_SIDE = 0

    Aspect_TOFM_BACK_SIDE = 1

    Aspect_TOFM_FRONT_SIDE = 2

Aspect_TOFM_BOTH_SIDE: Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE

Aspect_TOFM_BACK_SIDE: Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BACK_SIDE

Aspect_TOFM_FRONT_SIDE: Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE

class Aspect_TypeOfHighlightMethod(enum.IntEnum):
    """
    Definition of a highlight method

    TOHM_COLOR          drawn in the highlight color
    (default white)
    TOHM_BOUNDBOX       enclosed by the boundary box
    (default white)
    """

    Aspect_TOHM_COLOR = 0

    Aspect_TOHM_BOUNDBOX = 1

Aspect_TOHM_COLOR: Aspect_TypeOfHighlightMethod = Aspect_TypeOfHighlightMethod.Aspect_TOHM_COLOR

Aspect_TOHM_BOUNDBOX: Aspect_TypeOfHighlightMethod = Aspect_TypeOfHighlightMethod.Aspect_TOHM_BOUNDBOX

class Aspect_TypeOfLine(enum.IntEnum):
    """Definition of line types"""

    Aspect_TOL_EMPTY = -1

    Aspect_TOL_SOLID = 0

    Aspect_TOL_DASH = 1

    Aspect_TOL_DOT = 2

    Aspect_TOL_DOTDASH = 3

    Aspect_TOL_USERDEFINED = 4

Aspect_TOL_EMPTY: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_EMPTY

Aspect_TOL_SOLID: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_SOLID

Aspect_TOL_DASH: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DASH

Aspect_TOL_DOT: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DOT

Aspect_TOL_DOTDASH: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_DOTDASH

Aspect_TOL_USERDEFINED: Aspect_TypeOfLine = Aspect_TypeOfLine.Aspect_TOL_USERDEFINED

class Aspect_TypeOfMarker(enum.IntEnum):
    """Definition of types of markers"""

    Aspect_TOM_EMPTY = -1

    Aspect_TOM_POINT = 0

    Aspect_TOM_PLUS = 1

    Aspect_TOM_STAR = 2

    Aspect_TOM_X = 3

    Aspect_TOM_O = 4

    Aspect_TOM_O_POINT = 5

    Aspect_TOM_O_PLUS = 6

    Aspect_TOM_O_STAR = 7

    Aspect_TOM_O_X = 8

    Aspect_TOM_RING1 = 9

    Aspect_TOM_RING2 = 10

    Aspect_TOM_RING3 = 11

    Aspect_TOM_BALL = 12

    Aspect_TOM_USERDEFINED = 13

Aspect_TOM_EMPTY: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_EMPTY

Aspect_TOM_POINT: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_POINT

Aspect_TOM_PLUS: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_PLUS

Aspect_TOM_STAR: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_STAR

Aspect_TOM_X: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_X

Aspect_TOM_O: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_O

Aspect_TOM_O_POINT: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_O_POINT

Aspect_TOM_O_PLUS: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_O_PLUS

Aspect_TOM_O_STAR: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_O_STAR

Aspect_TOM_O_X: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_O_X

Aspect_TOM_RING1: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_RING1

Aspect_TOM_RING2: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_RING2

Aspect_TOM_RING3: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_RING3

Aspect_TOM_BALL: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_BALL

Aspect_TOM_USERDEFINED: Aspect_TypeOfMarker = Aspect_TypeOfMarker.Aspect_TOM_USERDEFINED

class Aspect_TypeOfStyleText(enum.IntEnum):
    """
    Define the style of the text.

    TOST_NORMAL
    Default text. The text is displayed like any other graphic object.
    This text can be hidden by another object that is nearest from the
    point of view.
    TOST_ANNOTATION
    The text is always visible. The text is displayed
    over the other object according to the priority.
    """

    Aspect_TOST_NORMAL = 0

    Aspect_TOST_ANNOTATION = 1

Aspect_TOST_NORMAL: Aspect_TypeOfStyleText = Aspect_TypeOfStyleText.Aspect_TOST_NORMAL

Aspect_TOST_ANNOTATION: Aspect_TypeOfStyleText = Aspect_TypeOfStyleText.Aspect_TOST_ANNOTATION

class Aspect_TypeOfTriedronPosition(enum.IntEnum):
    """
    Definition of the Trihedron position in the views.
    It is defined as a bitmask to simplify handling vertical and horizontal alignment independently.
    """

    Aspect_TOTP_CENTER = 0

    Aspect_TOTP_TOP = 1

    Aspect_TOTP_BOTTOM = 2

    Aspect_TOTP_LEFT = 4

    Aspect_TOTP_RIGHT = 8

    Aspect_TOTP_LEFT_LOWER = 6

    Aspect_TOTP_LEFT_UPPER = 5

    Aspect_TOTP_RIGHT_LOWER = 10

    Aspect_TOTP_RIGHT_UPPER = 9

Aspect_TOTP_CENTER: Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER

Aspect_TOTP_TOP: Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_TOP

Aspect_TOTP_BOTTOM: Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_BOTTOM

Aspect_TOTP_LEFT: Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_LEFT

Aspect_TOTP_RIGHT: Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_RIGHT

Aspect_TOTP_LEFT_LOWER: Aspect_TypeOfTriedronPosition = ...

Aspect_TOTP_LEFT_UPPER: Aspect_TypeOfTriedronPosition = ...

Aspect_TOTP_RIGHT_LOWER: Aspect_TypeOfTriedronPosition = ...

Aspect_TOTP_RIGHT_UPPER: Aspect_TypeOfTriedronPosition = ...

class Aspect_VKeyBasic(enum.IntEnum):
    """
    Enumeration defining virtual keys irrelevant to current keyboard layout for simplified hot-keys
    management logic.
    """

    Aspect_VKey_UNKNOWN = 0

    Aspect_VKey_A = 1

    Aspect_VKey_B = 2

    Aspect_VKey_C = 3

    Aspect_VKey_D = 4

    Aspect_VKey_E = 5

    Aspect_VKey_F = 6

    Aspect_VKey_G = 7

    Aspect_VKey_H = 8

    Aspect_VKey_I = 9

    Aspect_VKey_J = 10

    Aspect_VKey_K = 11

    Aspect_VKey_L = 12

    Aspect_VKey_M = 13

    Aspect_VKey_N = 14

    Aspect_VKey_O = 15

    Aspect_VKey_P = 16

    Aspect_VKey_Q = 17

    Aspect_VKey_R = 18

    Aspect_VKey_S = 19

    Aspect_VKey_T = 20

    Aspect_VKey_U = 21

    Aspect_VKey_V = 22

    Aspect_VKey_W = 23

    Aspect_VKey_X = 24

    Aspect_VKey_Y = 25

    Aspect_VKey_Z = 26

    Aspect_VKey_0 = 27

    Aspect_VKey_1 = 28

    Aspect_VKey_2 = 29

    Aspect_VKey_3 = 30

    Aspect_VKey_4 = 31

    Aspect_VKey_5 = 32

    Aspect_VKey_6 = 33

    Aspect_VKey_7 = 34

    Aspect_VKey_8 = 35

    Aspect_VKey_9 = 36

    Aspect_VKey_F1 = 37

    Aspect_VKey_F2 = 38

    Aspect_VKey_F3 = 39

    Aspect_VKey_F4 = 40

    Aspect_VKey_F5 = 41

    Aspect_VKey_F6 = 42

    Aspect_VKey_F7 = 43

    Aspect_VKey_F8 = 44

    Aspect_VKey_F9 = 45

    Aspect_VKey_F10 = 46

    Aspect_VKey_F11 = 47

    Aspect_VKey_F12 = 48

    Aspect_VKey_Up = 49

    Aspect_VKey_Down = 50

    Aspect_VKey_Left = 51

    Aspect_VKey_Right = 52

    Aspect_VKey_Plus = 53

    Aspect_VKey_Minus = 54

    Aspect_VKey_Equal = 55

    Aspect_VKey_PageUp = 56

    Aspect_VKey_PageDown = 57

    Aspect_VKey_Home = 58

    Aspect_VKey_End = 59

    Aspect_VKey_Escape = 60

    Aspect_VKey_Back = 61

    Aspect_VKey_Enter = 62

    Aspect_VKey_Backspace = 63

    Aspect_VKey_Space = 64

    Aspect_VKey_Delete = 65

    Aspect_VKey_Tilde = 66

    Aspect_VKey_Tab = 67

    Aspect_VKey_Comma = 68

    Aspect_VKey_Period = 69

    Aspect_VKey_Semicolon = 70

    Aspect_VKey_Slash = 71

    Aspect_VKey_BracketLeft = 72

    Aspect_VKey_Backslash = 73

    Aspect_VKey_BracketRight = 74

    Aspect_VKey_Apostrophe = 75

    Aspect_VKey_Numlock = 76

    Aspect_VKey_Scroll = 77

    Aspect_VKey_Numpad0 = 78

    Aspect_VKey_Numpad1 = 79

    Aspect_VKey_Numpad2 = 80

    Aspect_VKey_Numpad3 = 81

    Aspect_VKey_Numpad4 = 82

    Aspect_VKey_Numpad5 = 83

    Aspect_VKey_Numpad6 = 84

    Aspect_VKey_Numpad7 = 85

    Aspect_VKey_Numpad8 = 86

    Aspect_VKey_Numpad9 = 87

    Aspect_VKey_NumpadMultiply = 88

    Aspect_VKey_NumpadAdd = 89

    Aspect_VKey_NumpadSubtract = 90

    Aspect_VKey_NumpadDivide = 91

    Aspect_VKey_MediaNextTrack = 92

    Aspect_VKey_MediaPreviousTrack = 93

    Aspect_VKey_MediaStop = 94

    Aspect_VKey_MediaPlayPause = 95

    Aspect_VKey_VolumeMute = 96

    Aspect_VKey_VolumeDown = 97

    Aspect_VKey_VolumeUp = 98

    Aspect_VKey_BrowserBack = 99

    Aspect_VKey_BrowserForward = 100

    Aspect_VKey_BrowserRefresh = 101

    Aspect_VKey_BrowserStop = 102

    Aspect_VKey_BrowserSearch = 103

    Aspect_VKey_BrowserFavorites = 104

    Aspect_VKey_BrowserHome = 105

    Aspect_VKey_ViewTop = 106

    Aspect_VKey_ViewBottom = 107

    Aspect_VKey_ViewLeft = 108

    Aspect_VKey_ViewRight = 109

    Aspect_VKey_ViewFront = 110

    Aspect_VKey_ViewBack = 111

    Aspect_VKey_ViewAxoLeftProj = 112

    Aspect_VKey_ViewAxoRightProj = 113

    Aspect_VKey_ViewFitAll = 114

    Aspect_VKey_ViewRoll90CW = 115

    Aspect_VKey_ViewRoll90CCW = 116

    Aspect_VKey_ViewSwitchRotate = 117

    Aspect_VKey_Shift = 118

    Aspect_VKey_Control = 119

    Aspect_VKey_Alt = 120

    Aspect_VKey_Menu = 121

    Aspect_VKey_Meta = 122

    Aspect_VKey_NavInteract = 123

    Aspect_VKey_NavForward = 124

    Aspect_VKey_NavBackward = 125

    Aspect_VKey_NavSlideLeft = 126

    Aspect_VKey_NavSlideRight = 127

    Aspect_VKey_NavSlideUp = 128

    Aspect_VKey_NavSlideDown = 129

    Aspect_VKey_NavRollCCW = 130

    Aspect_VKey_NavRollCW = 131

    Aspect_VKey_NavLookLeft = 132

    Aspect_VKey_NavLookRight = 133

    Aspect_VKey_NavLookUp = 134

    Aspect_VKey_NavLookDown = 135

    Aspect_VKey_NavCrouch = 136

    Aspect_VKey_NavJump = 137

    Aspect_VKey_NavThrustForward = 138

    Aspect_VKey_NavThrustBackward = 139

    Aspect_VKey_NavThrustStop = 140

    Aspect_VKey_NavSpeedIncrease = 141

    Aspect_VKey_NavSpeedDecrease = 142

Aspect_VKey_UNKNOWN: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_UNKNOWN

Aspect_VKey_A: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_A

Aspect_VKey_B: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_B

Aspect_VKey_C: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_C

Aspect_VKey_D: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_D

Aspect_VKey_E: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_E

Aspect_VKey_F: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F

Aspect_VKey_G: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_G

Aspect_VKey_H: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_H

Aspect_VKey_I: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_I

Aspect_VKey_J: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_J

Aspect_VKey_K: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_K

Aspect_VKey_L: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_L

Aspect_VKey_M: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_M

Aspect_VKey_N: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_N

Aspect_VKey_O: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_O

Aspect_VKey_P: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_P

Aspect_VKey_Q: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Q

Aspect_VKey_R: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_R

Aspect_VKey_S: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_S

Aspect_VKey_T: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_T

Aspect_VKey_U: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_U

Aspect_VKey_V: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_V

Aspect_VKey_W: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_W

Aspect_VKey_X: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_X

Aspect_VKey_Y: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Y

Aspect_VKey_Z: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Z

Aspect_VKey_0: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_0

Aspect_VKey_1: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_1

Aspect_VKey_2: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_2

Aspect_VKey_3: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_3

Aspect_VKey_4: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_4

Aspect_VKey_5: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_5

Aspect_VKey_6: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_6

Aspect_VKey_7: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_7

Aspect_VKey_8: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_8

Aspect_VKey_9: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_9

Aspect_VKey_F1: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F1

Aspect_VKey_F2: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F2

Aspect_VKey_F3: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F3

Aspect_VKey_F4: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F4

Aspect_VKey_F5: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F5

Aspect_VKey_F6: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F6

Aspect_VKey_F7: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F7

Aspect_VKey_F8: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F8

Aspect_VKey_F9: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F9

Aspect_VKey_F10: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F10

Aspect_VKey_F11: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F11

Aspect_VKey_F12: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_F12

Aspect_VKey_Up: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Up

Aspect_VKey_Down: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Down

Aspect_VKey_Left: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Left

Aspect_VKey_Right: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Right

Aspect_VKey_Plus: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Plus

Aspect_VKey_Minus: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Minus

Aspect_VKey_Equal: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Equal

Aspect_VKey_PageUp: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_PageUp

Aspect_VKey_PageDown: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_PageDown

Aspect_VKey_Home: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Home

Aspect_VKey_End: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_End

Aspect_VKey_Escape: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Escape

Aspect_VKey_Back: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Back

Aspect_VKey_Enter: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Enter

Aspect_VKey_Backspace: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Backspace

Aspect_VKey_Space: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Space

Aspect_VKey_Delete: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Delete

Aspect_VKey_Tilde: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Tilde

Aspect_VKey_Tab: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Tab

Aspect_VKey_Comma: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Comma

Aspect_VKey_Period: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Period

Aspect_VKey_Semicolon: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Semicolon

Aspect_VKey_Slash: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Slash

Aspect_VKey_BracketLeft: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BracketLeft

Aspect_VKey_Backslash: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Backslash

Aspect_VKey_BracketRight: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BracketRight

Aspect_VKey_Apostrophe: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Apostrophe

Aspect_VKey_Numlock: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numlock

Aspect_VKey_Scroll: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Scroll

Aspect_VKey_Numpad0: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad0

Aspect_VKey_Numpad1: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad1

Aspect_VKey_Numpad2: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad2

Aspect_VKey_Numpad3: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad3

Aspect_VKey_Numpad4: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad4

Aspect_VKey_Numpad5: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad5

Aspect_VKey_Numpad6: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad6

Aspect_VKey_Numpad7: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad7

Aspect_VKey_Numpad8: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad8

Aspect_VKey_Numpad9: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Numpad9

Aspect_VKey_NumpadMultiply: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NumpadMultiply

Aspect_VKey_NumpadAdd: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NumpadAdd

Aspect_VKey_NumpadSubtract: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NumpadSubtract

Aspect_VKey_NumpadDivide: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NumpadDivide

Aspect_VKey_MediaNextTrack: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_MediaNextTrack

Aspect_VKey_MediaPreviousTrack: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_MediaPreviousTrack

Aspect_VKey_MediaStop: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_MediaStop

Aspect_VKey_MediaPlayPause: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_MediaPlayPause

Aspect_VKey_VolumeMute: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_VolumeMute

Aspect_VKey_VolumeDown: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_VolumeDown

Aspect_VKey_VolumeUp: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_VolumeUp

Aspect_VKey_BrowserBack: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserBack

Aspect_VKey_BrowserForward: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserForward

Aspect_VKey_BrowserRefresh: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserRefresh

Aspect_VKey_BrowserStop: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserStop

Aspect_VKey_BrowserSearch: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserSearch

Aspect_VKey_BrowserFavorites: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserFavorites

Aspect_VKey_BrowserHome: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_BrowserHome

Aspect_VKey_ViewTop: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewTop

Aspect_VKey_ViewBottom: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewBottom

Aspect_VKey_ViewLeft: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewLeft

Aspect_VKey_ViewRight: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewRight

Aspect_VKey_ViewFront: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewFront

Aspect_VKey_ViewBack: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewBack

Aspect_VKey_ViewAxoLeftProj: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewAxoLeftProj

Aspect_VKey_ViewAxoRightProj: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewAxoRightProj

Aspect_VKey_ViewFitAll: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewFitAll

Aspect_VKey_ViewRoll90CW: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CW

Aspect_VKey_ViewRoll90CCW: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewRoll90CCW

Aspect_VKey_ViewSwitchRotate: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_ViewSwitchRotate

Aspect_VKey_Shift: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Shift

Aspect_VKey_Control: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Control

Aspect_VKey_Alt: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Alt

Aspect_VKey_Menu: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Menu

Aspect_VKey_Meta: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_Meta

Aspect_VKey_NavInteract: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavInteract

Aspect_VKey_NavForward: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavForward

Aspect_VKey_NavBackward: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavBackward

Aspect_VKey_NavSlideLeft: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSlideLeft

Aspect_VKey_NavSlideRight: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSlideRight

Aspect_VKey_NavSlideUp: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSlideUp

Aspect_VKey_NavSlideDown: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSlideDown

Aspect_VKey_NavRollCCW: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavRollCCW

Aspect_VKey_NavRollCW: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavRollCW

Aspect_VKey_NavLookLeft: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavLookLeft

Aspect_VKey_NavLookRight: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavLookRight

Aspect_VKey_NavLookUp: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavLookUp

Aspect_VKey_NavLookDown: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavLookDown

Aspect_VKey_NavCrouch: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavCrouch

Aspect_VKey_NavJump: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavJump

Aspect_VKey_NavThrustForward: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavThrustForward

Aspect_VKey_NavThrustBackward: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavThrustBackward

Aspect_VKey_NavThrustStop: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavThrustStop

Aspect_VKey_NavSpeedIncrease: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSpeedIncrease

Aspect_VKey_NavSpeedDecrease: Aspect_VKeyBasic = Aspect_VKeyBasic.Aspect_VKey_NavSpeedDecrease

Aspect_VKey_Lower: int = 0

Aspect_VKey_ModifiersLower: int = 118

Aspect_VKey_ModifiersUpper: int = 122

Aspect_VKey_NavigationKeysLower: int = 123

Aspect_VKey_NavigationKeysUpper: int = 142

Aspect_VKey_Upper: int = 142

Aspect_VKey_NB: int = 143

Aspect_VKey_MAX: int = 255

class Aspect_WidthOfLine(enum.IntEnum):
    """
    Definition of line types

    WOL_THIN            thin line (1 pixel width)
    WOL_MEDIUM          medium width of 0.5 MM
    WOL_THICK           thick width of 0.7 MM
    WOL_VERYTHICK       very thick width of 1.5 MM
    WOL_USERDEFINED     defined by Users
    """

    Aspect_WOL_THIN = 0

    Aspect_WOL_MEDIUM = 1

    Aspect_WOL_THICK = 2

    Aspect_WOL_VERYTHICK = 3

    Aspect_WOL_USERDEFINED = 4

Aspect_WOL_THIN: Aspect_WidthOfLine = Aspect_WidthOfLine.Aspect_WOL_THIN

Aspect_WOL_MEDIUM: Aspect_WidthOfLine = Aspect_WidthOfLine.Aspect_WOL_MEDIUM

Aspect_WOL_THICK: Aspect_WidthOfLine = Aspect_WidthOfLine.Aspect_WOL_THICK

Aspect_WOL_VERYTHICK: Aspect_WidthOfLine = Aspect_WidthOfLine.Aspect_WOL_VERYTHICK

Aspect_WOL_USERDEFINED: Aspect_WidthOfLine = Aspect_WidthOfLine.Aspect_WOL_USERDEFINED

class Aspect_AspectFillAreaDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_AspectLineDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_AspectMarkerDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_Background:
    """
    This class allows the definition of
    a window background.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a window background.
        Default color : NOC_MATRAGRAY.
        """

    @overload
    def __init__(self, AColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Creates a window background with the colour <AColor>."""

    @overload
    def __init__(self, theOther: Aspect_Background) -> None: ...

    def SetColor(self, AColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the colour of the window background <me>."""

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the colour of the window background <me>."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_Grid(nanoocp.Standard.Standard_Transient):
    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetXOrigin(self, anOrigin: float) -> None:
        """defines the x Origin of the grid."""

    def SetYOrigin(self, anOrigin: float) -> None:
        """defines the y Origin of the grid."""

    def SetRotationAngle(self, anAngle: float) -> None:
        """defines the orientation of the grid."""

    def Rotate(self, anAngle: float) -> None:
        """Rotate the grid from a relative angle."""

    def Translate(self, aDx: float, aDy: float) -> None:
        """Translate the grid from a relative distance."""

    def SetColors(self, aColor: nanoocp.Quantity.Quantity_Color, aTenthColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Change the colors of the grid"""

    def Hit(self, X: float, Y: float) -> tuple[float, float]:
        """
        returns the point of the grid the closest to the point X,Y
        if the grid is active. If the grid is not active returns
        X,Y.
        """

    def Compute(self, X: float, Y: float) -> tuple[float, float]:
        """returns the point of the grid the closest to the point X,Y"""

    def Activate(self) -> None:
        """
        activates the grid. The Hit method will return
        gridx and gridx computed according to the steps
        of the grid.
        """

    def Deactivate(self) -> None:
        """
        deactivates the grid. The hit method will return
        gridx and gridx as the enter value X & Y.
        """

    def XOrigin(self) -> float:
        """returns the x Origin of the grid."""

    def YOrigin(self) -> float:
        """returns the x Origin of the grid."""

    def RotationAngle(self) -> float:
        """returns the x Angle of the grid."""

    def IsActive(self) -> bool:
        """Returns TRUE when the grid is active."""

    def Colors(self, aColor: nanoocp.Quantity.Quantity_Color, aTenthColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns the colors of the grid."""

    def SetDrawMode(self, aDrawMode: Aspect_GridDrawMode) -> None:
        """Change the grid aspect."""

    def DrawMode(self) -> Aspect_GridDrawMode:
        """Returns the grid aspect."""

    def Display(self) -> None:
        """Display the grid at screen."""

    def Erase(self) -> None:
        """Erase the grid from screen."""

    def IsDisplayed(self) -> bool:
        """Returns TRUE when the grid is displayed at screen."""

    def Init(self) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_CircularGrid(Aspect_Grid):
    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetRadiusStep(self, aStep: float) -> None:
        """defines the x step of the grid."""

    def SetDivisionNumber(self, aNumber: int) -> None:
        """defines the step of the grid."""

    def SetGridValues(self, XOrigin: float, YOrigin: float, RadiusStep: float, DivisionNumber: int, RotationAngle: float) -> None: ...

    def Compute(self, X: float, Y: float) -> tuple[float, float]:
        """returns the point of the grid the closest to the point X,Y"""

    def RadiusStep(self) -> float:
        """returns the x step of the grid."""

    def DivisionNumber(self) -> int:
        """returns the x step of the grid."""

    def SetRadius(self, theRadius: float) -> None:
        """
        Set the circular grid radius (plane-local units). 0.0 (default) means
        unbounded - the shader draws the grid to the horizon.
        """

    def Radius(self) -> float:
        """Return the bounded radius. 0.0 means unbounded."""

    def SetZOffset(self, theOffset: float) -> None:
        """
        Set signed offset along the plane normal for display only; snap math
        stays on the plane. Use a small negative value to avoid z-fighting with
        coplanar geometry.
        """

    def ZOffset(self) -> float:
        """Return the display-time Z-offset along the plane normal."""

    def SetArcRange(self, theStart: float, theEnd: float) -> None:
        """
        Restrict the grid to an angular wedge, walking counter-clockwise from
        @p theStart to @p theEnd (radians, measured from the rotated plane X
        axis). Setting both values equal (e.g. both 0.0) returns to full-circle
        rendering - the sentinel used for unbounded.
        """

    def AngleStart(self) -> float:
        """
        Return the arc start angle (radians). Meaningful only when IsArc() is true.
        """

    def AngleEnd(self) -> float:
        """
        Return the arc end angle (radians). Meaningful only when IsArc() is true.
        """

    def IsArc(self) -> bool:
        """Return TRUE when the grid is restricted to an angular wedge."""

    def Init(self) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_DisplayConnection(nanoocp.Standard.Standard_Transient):
    """
    This class creates and provides connection with X server.
    Raises exception if can not connect to X server.
    On Windows and Mac OS X (in case when Cocoa used) platforms this class does nothing.
    WARNING: Do not close display connection manually!
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor. Creates connection with display name taken from "DISPLAY" environment
        variable
        """

    @overload
    def __init__(self, theDisplayName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Constructor. Creates connection with display specified in theDisplayName.
        Display name should be in format "hostname:number" or "hostname:number.screen_number", where:
        hostname
        - Specifies the name of the host machine on which the display is physically attached.
        number
        - Specifies the number of the display server on that host machine.
        screen_number
        - Specifies the screen to be used on that server. Optional variable.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsOwnDisplay(self) -> bool:
        """@return TRUE if X Display has been allocated by this class"""

    def GetAtom(self, theAtom: Aspect_XAtom) -> int:
        """
        @return identifier(atom) for custom named property associated with windows that use current
        connection to X server.
        """

    def GetDisplayName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return display name for this connection."""

class Aspect_DisplayConnectionDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_GenId:
    """This class permits the creation and control of integer identifiers."""

    @overload
    def __init__(self) -> None:
        """
        Creates an available set of identifiers with the lower bound 0 and the upper bound INT_MAX
        / 2.
        """

    @overload
    def __init__(self, theLow: int, theUpper: int) -> None:
        """
        Creates an available set of identifiers with specified range.
        Raises IdentDefinitionError if theUpper is less than theLow.
        """

    @overload
    def __init__(self, theOther: Aspect_GenId) -> None: ...

    @overload
    def Free(self) -> None:
        """Free all identifiers - make the whole range available again."""

    @overload
    def Free(self, theId: int) -> None:
        """
        Free specified identifier. Warning - method has no protection against double-freeing!
        """

    def HasFree(self) -> bool:
        """Returns true if there are available identifiers in range."""

    def Available(self) -> int:
        """Returns the number of available identifiers."""

    def Lower(self) -> int:
        """Returns the lower identifier in range."""

    def Next(self) -> int:
        """
        Returns the next available identifier.
        Warning: Raises IdentDefinitionError if all identifiers are busy.
        """

    def Next__int(self) -> tuple[bool, int]:
        """
        Next__int: the C++ overload Next(int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Generates the next available identifier.
        @param[out] theId  generated identifier
        @return FALSE if all identifiers are busy.
        """

    def Upper(self) -> int:
        """Returns the upper identifier in range."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_GradientBackground(Aspect_Background):
    """This class allows the definition of a window gradient background."""

    @overload
    def __init__(self) -> None:
        """
        Creates a window gradient background.
        Default color is Quantity_NOC_BLACK.
        Default fill method is Aspect_GradientFillMethod_None.
        """

    @overload
    def __init__(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color, theMethod: Aspect_GradientFillMethod = ...) -> None:
        """Creates a window gradient background with two colours."""

    @overload
    def __init__(self, theOther: Aspect_GradientBackground) -> None: ...

    def SetColors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color, theMethod: Aspect_GradientFillMethod = ...) -> None:
        """Modifies the colours of the window gradient background."""

    def Colors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns colours of the window gradient background."""

    def BgGradientFillMethod(self) -> Aspect_GradientFillMethod:
        """Returns the current gradient background fill mode."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_GraphicDeviceDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_GridParams:
    """
    Grid appearance for V3d_View::GridDisplay: color, scale, bounds, arc, draw mode,
    background and adaptive flags.
    """

    @overload
    def __init__(self) -> None:
        """
        Construct with sensible defaults: grey lines on the plane origin with
        axis coloring enabled, 1/100 plane-unit spacing, overlay mode,
        unbounded in extent and radius.
        """

    @overload
    def __init__(self, theOther: Aspect_GridParams) -> None: ...

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Return grid line color."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Set grid line color."""

    def Origin(self) -> nanoocp.gp.gp_Pnt:
        """Return local offset of the grid origin within the plane."""

    def SetOrigin(self, theOrigin: nanoocp.gp.gp_Pnt) -> None:
        """Set local offset of the grid origin within the plane."""

    def AccentColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return every-tenth-line / accent colour rendered by the shader."""

    def SetAccentColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Set every-tenth-line / accent colour rendered by the shader."""

    def AccentScaleX(self) -> float:
        """
        Return accent overlay scale along the plane X/radial direction.
        Zero disables the accent layer on that axis.
        """

    def SetAccentScaleX(self, theScale: float) -> None:
        """Set accent overlay scale along the plane X/radial direction."""

    def AccentScaleY(self) -> float:
        """
        Return accent overlay scale along the plane Y direction.
        Zero disables the accent layer on that axis.
        """

    def SetAccentScaleY(self, theScale: float) -> None:
        """Set accent overlay scale along the plane Y direction."""

    def AccentAngularScale(self) -> float:
        """
        Return accent overlay angular scale for circular-grid spokes.
        Zero disables the angular accent layer.
        """

    def SetAccentAngularScale(self, theScale: float) -> None:
        """Set accent overlay angular scale for circular-grid spokes."""

    def Scale(self) -> float:
        """
        Return major-grid scale factor along the plane X direction (cells per plane unit).
        """

    def SetScale(self, theScale: float) -> None:
        """
        Set major-grid scale factor along the plane X direction (cells per plane unit).
        Must be non-negative; zero is a valid "unused" sentinel.
        """

    def ScaleY(self) -> float:
        """
        Return explicit Y-direction scale. When 0.0, renderer falls back to Scale() (isotropic).
        """

    def SetScaleY(self, theScaleY: float) -> None:
        """
        Set explicit Y-direction scale. Pass 0.0 to mirror Scale() (isotropic, default).
        """

    def EffectiveScaleY(self) -> float:
        """Effective Y-direction scale actually consumed by the renderer."""

    def LineThickness(self) -> float:
        """
        Return line thickness in plane units (minimum pixel-space line width is derived from fwidth).
        """

    def SetLineThickness(self, theThickness: float) -> None:
        """Set line thickness in plane units."""

    def RotationAngle(self) -> float:
        """
        Return in-plane rotation angle (radians) applied to the grid axes around the plane normal.
        """

    def SetRotationAngle(self, theAngle: float) -> None:
        """
        Set in-plane rotation angle (radians) applied to the grid axes around the plane normal.
        """

    def AngularDivisions(self) -> int:
        """
        Return the angular subdivision count of the half-circle for circular grids.
        Zero means rectangular grid (default); any positive value switches the
        renderer to polar rings (Scale -> radial step) and spokes at pi/N rad.
        """

    def SetAngularDivisions(self, theDivisions: int) -> None:
        """
        Set angular subdivision count (0 = rectangular grid, N>0 = circular with N spokes per 180
        deg).
        """

    def IsCircular(self) -> bool:
        """Return TRUE when the parameters describe a circular (polar) grid."""

    def SizeX(self) -> float:
        """Return rectangular bounded extent along plane X; 0.0 means unbounded."""

    def SetSizeX(self, theSize: float) -> None:
        """Set rectangular bounded extent along plane X; 0.0 means unbounded."""

    def SizeY(self) -> float:
        """Return rectangular bounded extent along plane Y; 0.0 means unbounded."""

    def SetSizeY(self, theSize: float) -> None:
        """Set rectangular bounded extent along plane Y; 0.0 means unbounded."""

    def Radius(self) -> float:
        """Return circular bounded radius; 0.0 means unbounded."""

    def SetRadius(self, theRadius: float) -> None:
        """Set circular bounded radius; 0.0 means unbounded."""

    def ZOffset(self) -> float:
        """Return signed plane-normal offset applied at render time."""

    def SetZOffset(self, theOffset: float) -> None:
        """Set signed plane-normal offset applied at render and echo time."""

    def AngleStart(self) -> float:
        """
        Return arc start angle (radians). Meaningful only when IsArc() is true.
        """

    def AngleEnd(self) -> float:
        """Return arc end angle (radians). Meaningful only when IsArc() is true."""

    def SetArcRange(self, theStart: float, theEnd: float) -> None:
        """
        Restrict the circular grid to an angular wedge [start, end], walking CCW.
        Equal start and end (e.g. 0.0 and 0.0) returns to full-circle rendering.
        """

    def IsBounded(self) -> bool:
        """Return TRUE when the parameters describe a bounded rectangle or disc."""

    def IsArc(self) -> bool:
        """Return TRUE when the circular grid is restricted to a sub-arc."""

    def DrawMode(self) -> Aspect_GridDrawMode:
        """Return draw mode: lines, points at grid intersections, or none."""

    def SetDrawMode(self, theMode: Aspect_GridDrawMode) -> None:
        """
        Set draw mode. Aspect_GDM_None suppresses rendering entirely; Points draws
        dots at grid-line intersections, Lines (default) draws the full grid.
        """

    def IsBackground(self) -> bool:
        """
        Return TRUE if grid is drawn as a view-space background (behind all geometry).
        """

    def SetIsBackground(self, theIsBackground: bool) -> None:
        """Set background-mode rendering on/off."""

    def IsDrawAxis(self) -> bool:
        """
        Return TRUE if axis lines on the grid plane are drawn in red/green/blue.
        """

    def SetIsDrawAxis(self, theIsDrawAxis: bool) -> None:
        """Set axis coloring on/off."""

    def IsViewAdaptive(self) -> bool:
        """
        Return TRUE if grid spacing and visible extents adapt to the camera view.
        """

    def SetIsViewAdaptive(self, theIsViewAdaptive: bool) -> None:
        """
        Set view-adaptive grid on/off. When enabled, shader renderer keeps the
        screen-space grid step stable by scaling the cell spacing with camera zoom.
        """

class Aspect_Window(nanoocp.Standard.Standard_Transient):
    """Defines a window."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsVirtual(self) -> bool:
        """Returns True if the window <me> is virtual"""

    def SetVirtual(self, theVirtual: bool) -> None:
        """Setup the virtual state"""

    def TopLeft(self) -> nanoocp.BVH.BVH_Vec2i:
        """Returns window top-left corner."""

    def Dimensions(self) -> nanoocp.BVH.BVH_Vec2i:
        """Returns window dimensions."""

    def DisplayConnection(self) -> Aspect_DisplayConnection:
        """Returns connection to Display or NULL."""

    def Background(self) -> Aspect_Background:
        """Returns the window background."""

    def BackgroundFillMethod(self) -> Aspect_FillMethod:
        """Returns the current image background fill mode."""

    def GradientBackground(self) -> Aspect_GradientBackground:
        """Returns the window gradient background."""

    @overload
    def SetBackground(self, theBack: Aspect_Background) -> None: ...

    @overload
    def SetBackground(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the window background."""

    @overload
    def SetBackground(self, theBackground: Aspect_GradientBackground) -> None: ...

    @overload
    def SetBackground(self, theFirstColor: nanoocp.Quantity.Quantity_Color, theSecondColor: nanoocp.Quantity.Quantity_Color, theFillMethod: Aspect_GradientFillMethod) -> None:
        """Modifies the window gradient background."""

    def IsMapped(self) -> bool:
        """
        Returns True if the window <me> is opened
        and False if the window is closed.
        """

    def Map(self) -> None:
        """Opens the window <me>."""

    def Unmap(self) -> None:
        """Closes the window <me>."""

    def DoResize(self) -> Aspect_TypeOfResize:
        """Apply the resizing to the window <me>."""

    def DoMapping(self) -> bool:
        """
        Apply the mapping change to the window <me>.
        and returns TRUE if the window is mapped at screen.
        """

    def Ratio(self) -> float:
        """
        Returns The Window RATIO equal to the physical
        WIDTH/HEIGHT dimensions
        """

    def Position(self) -> tuple[int, int, int, int]:
        """Returns The Window POSITION in PIXEL"""

    def Size(self) -> tuple[int, int]:
        """Returns The Window SIZE in PIXEL"""

    def NativeHandle(self) -> int:
        """
        Returns native Window handle (HWND on Windows, Window with Xlib, and so on)
        """

    def NativeParentHandle(self) -> int:
        """
        Returns parent of native Window handle (HWND on Windows, Window with Xlib, and so on)
        """

    def SetTitle(self, theTitle: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets window title."""

    def InvalidateContent(self, theDisp: Aspect_DisplayConnection | None) -> None:
        """
        Invalidate entire window content.

        Implementation is expected to allow calling this method from non-GUI thread,
        e.g. by queuing exposure event into window message queue or in other thread-safe manner.

        Optional display argument should be passed when called from non-GUI thread
        on platforms implementing thread-unsafe connections to display.
        NULL can be passed instead otherwise.
        """

    def DevicePixelRatio(self) -> float:
        """Return device pixel ratio (logical to backing store scale factor)."""

    def ConvertPointToBacking(self, thePnt: nanoocp.BVH.BVH_Vec2d) -> nanoocp.BVH.BVH_Vec2d:
        """Convert point from logical units into backing store units."""

    def ConvertPointFromBacking(self, thePnt: nanoocp.BVH.BVH_Vec2d) -> nanoocp.BVH.BVH_Vec2d:
        """Convert point from backing store units to logical units."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_NeutralWindow(Aspect_Window):
    """
    Defines a platform-neutral window.
    This class is intended to be used in context when window management (including OpenGL context
    creation) is performed on application side (e.g. using external framework).

    Window properties should be managed by application and assigned to this class as properties.
    """

    @overload
    def __init__(self) -> None:
        """
        Empty constructor.
        Note that window is considered "mapped" by default.
        """

    @overload
    def __init__(self, theOther: Aspect_NeutralWindow) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def NativeHandle(self) -> int:
        """Return native handle of this drawable."""

    def NativeParentHandle(self) -> int:
        """Return native handle of the parent drawable."""

    def SetNativeHandle(self, theWindow: int) -> bool:
        """
        Set native handle.
        @return true if definition has been changed
        """

    def IsMapped(self) -> bool:
        """Return true if window is not hidden."""

    def Map(self) -> None:
        """Change window mapped flag to TRUE."""

    def Unmap(self) -> None:
        """Change window mapped flag to FALSE."""

    def DoResize(self) -> Aspect_TypeOfResize:
        """Resize window - do nothing."""

    def DoMapping(self) -> bool:
        """Map window - do nothing."""

    def Ratio(self) -> float:
        """Returns window ratio equal to the physical width/height dimensions."""

    def Position(self) -> tuple[int, int, int, int]:
        """Return the window position."""

    @overload
    def SetPosition(self, theX1: int, theY1: int) -> bool: ...

    @overload
    def SetPosition(self, theX1: int, theY1: int, theX2: int, theY2: int) -> bool:
        """
        Set the window position.
        @return true if position has been changed
        """

    def Size(self) -> tuple[int, int]:
        """Return the window size."""

    def SetSize(self, theWidth: int, theHeight: int) -> bool:
        """
        Set the window size.
        @return true if size has been changed
        """

class Aspect_XRAction(nanoocp.Standard.Standard_Transient):
    """XR action definition."""

    @overload
    def __init__(self, theId: nanoocp.TCollection.TCollection_AsciiString, theType: Aspect_XRActionType) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRAction) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return action id."""

    def Type(self) -> Aspect_XRActionType:
        """Return action type."""

    def IsValid(self) -> bool:
        """Return TRUE if action is defined."""

    def RawHandle(self) -> int:
        """Return action handle."""

    def SetRawHandle(self, theHande: int) -> None:
        """Set action handle."""

class Aspect_XRActionSet(nanoocp.Standard.Standard_Transient):
    """XR action set."""

    @overload
    def __init__(self, theId: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRActionSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Id(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return action id."""

    def RawHandle(self) -> int:
        """Return action handle."""

    def SetRawHandle(self, theHande: int) -> None:
        """Set action handle."""

    def AddAction(self, theAction: Aspect_XRAction | None) -> None:
        """Add action."""

    def Actions(self) -> nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Aspect.Aspect_XRAction]:
        """Return map of actions."""

class Aspect_XRAnalogActionData:
    """Analog input XR action data."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRAnalogActionData) -> None: ...

    def IsChanged(self) -> bool:
        """Return TRUE if delta is non-zero."""

    @property
    def ActiveOrigin(self) -> int:
        """The origin that caused this action's current state"""

    @ActiveOrigin.setter
    def ActiveOrigin(self, arg: int, /) -> None: ...

    @property
    def UpdateTime(self) -> float:
        """
        Time relative to now when this event happened. Will be negative to indicate a past time
        """

    @UpdateTime.setter
    def UpdateTime(self, arg: float, /) -> None: ...

    @property
    def VecXYZ(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """the current state of this action"""

    @VecXYZ.setter
    def VecXYZ(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def DeltaXYZ(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """deltas since the previous update"""

    @DeltaXYZ.setter
    def DeltaXYZ(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def IsActive(self) -> bool:
        """
        whether or not this action is currently available to be bound in the active action set
        """

    @IsActive.setter
    def IsActive(self, arg: bool, /) -> None: ...

class Aspect_XRDigitalActionData:
    """Digital input XR action data."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRDigitalActionData) -> None: ...

    @property
    def ActiveOrigin(self) -> int:
        """The origin that caused this action's current state"""

    @ActiveOrigin.setter
    def ActiveOrigin(self, arg: int, /) -> None: ...

    @property
    def UpdateTime(self) -> float:
        """
        Time relative to now when this event happened. Will be negative to indicate a past time
        """

    @UpdateTime.setter
    def UpdateTime(self, arg: float, /) -> None: ...

    @property
    def IsActive(self) -> bool:
        """
        whether or not this action is currently available to be bound in the active action set
        """

    @IsActive.setter
    def IsActive(self, arg: bool, /) -> None: ...

    @property
    def IsPressed(self) -> bool:
        """
        Aspect_InputActionType_Digital state - The current state of this action; will be true if currently pressed
        """

    @IsPressed.setter
    def IsPressed(self, arg: bool, /) -> None: ...

    @property
    def IsChanged(self) -> bool:
        """
        Aspect_InputActionType_Digital state - this is true if the state has changed since the last frame
        """

    @IsChanged.setter
    def IsChanged(self, arg: bool, /) -> None: ...

class Aspect_XRHapticActionData:
    """Haptic output XR action data."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRHapticActionData) -> None: ...

    def IsValid(self) -> bool:
        """Return TRUE if data is not empty."""

    @property
    def Delay(self) -> float:
        """delay in seconds before start"""

    @Delay.setter
    def Delay(self, arg: float, /) -> None: ...

    @property
    def Duration(self) -> float:
        """duration in seconds"""

    @Duration.setter
    def Duration(self, arg: float, /) -> None: ...

    @property
    def Frequency(self) -> float:
        """vibration frequency"""

    @Frequency.setter
    def Frequency(self, arg: float, /) -> None: ...

    @property
    def Amplitude(self) -> float:
        """vibration amplitude"""

    @Amplitude.setter
    def Amplitude(self, arg: float, /) -> None: ...

class Aspect_TrackedDevicePose:
    """Describes a single pose for a tracked object (for XR)."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_TrackedDevicePose) -> None: ...

    @property
    def Orientation(self) -> nanoocp.gp.gp_Trsf:
        """device to absolute transformation"""

    @Orientation.setter
    def Orientation(self, arg: nanoocp.gp.gp_Trsf, /) -> None: ...

    @property
    def Velocity(self) -> nanoocp.gp.gp_Vec:
        """velocity in tracker space in m/s"""

    @Velocity.setter
    def Velocity(self, arg: nanoocp.gp.gp_Vec, /) -> None: ...

    @property
    def AngularVelocity(self) -> nanoocp.gp.gp_Vec:
        """angular velocity in radians/s"""

    @AngularVelocity.setter
    def AngularVelocity(self, arg: nanoocp.gp.gp_Vec, /) -> None: ...

    @property
    def IsValidPose(self) -> bool:
        """indicates valid pose"""

    @IsValidPose.setter
    def IsValidPose(self, arg: bool, /) -> None: ...

    @property
    def IsConnectedDevice(self) -> bool:
        """indicates connected state"""

    @IsConnectedDevice.setter
    def IsConnectedDevice(self, arg: bool, /) -> None: ...

class Aspect_XRPoseActionData:
    """Pose input XR action data."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_XRPoseActionData) -> None: ...

    @property
    def Pose(self) -> Aspect_TrackedDevicePose:
        """pose state"""

    @Pose.setter
    def Pose(self, arg: Aspect_TrackedDevicePose, /) -> None: ...

    @property
    def ActiveOrigin(self) -> int:
        """The origin that caused this action's current state"""

    @ActiveOrigin.setter
    def ActiveOrigin(self, arg: int, /) -> None: ...

    @property
    def IsActive(self) -> bool:
        """
        whether or not this action is currently available to be bound in the active action set
        """

    @IsActive.setter
    def IsActive(self, arg: bool, /) -> None: ...

class Aspect_XRSession(nanoocp.Standard.Standard_Transient):
    """Extended Reality (XR) Session interface."""

    class TrackingUniverseOrigin(enum.IntEnum):
        """
        Identifies which style of tracking origin the application wants to use for the poses it is
        requesting.
        """

        TrackingUniverseOrigin_Seated = 0

        TrackingUniverseOrigin_Standing = 1

    TrackingUniverseOrigin_Seated: Aspect_XRSession.TrackingUniverseOrigin = ...

    TrackingUniverseOrigin_Standing: Aspect_XRSession.TrackingUniverseOrigin = ...

    class InfoString(enum.IntEnum):
        """Info string enumeration."""

        InfoString_Vendor = 0

        InfoString_Device = 1

        InfoString_Tracker = 2

        InfoString_SerialNumber = 3

    InfoString_Vendor: Aspect_XRSession.InfoString = InfoString.InfoString_Vendor

    InfoString_Device: Aspect_XRSession.InfoString = InfoString.InfoString_Device

    InfoString_Tracker: Aspect_XRSession.InfoString = InfoString.InfoString_Tracker

    InfoString_SerialNumber: Aspect_XRSession.InfoString = InfoString.InfoString_SerialNumber

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsOpen(self) -> bool:
        """Return TRUE if session is opened."""

    def Open(self) -> bool:
        """Initialize session."""

    def Close(self) -> None:
        """Release session."""

    def WaitPoses(self) -> bool:
        """Fetch actual poses of tracked devices."""

    def RecommendedViewport(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return recommended viewport Width x Height for rendering into VR."""

    def EyeToHeadTransform(self, theEye: Aspect_Eye) -> nanoocp.BVH.BVH_Mat4d:
        """Return transformation from eye to head."""

    def HeadToEyeTransform(self, theEye: Aspect_Eye) -> nanoocp.BVH.BVH_Mat4d:
        """Return transformation from head to eye."""

    def ProjectionMatrix(self, theEye: Aspect_Eye, theZNear: float, theZFar: float) -> nanoocp.BVH.BVH_Mat4d:
        """Return projection matrix."""

    def HasProjectionFrustums(self) -> bool:
        """
        Return FALSE if projection frustums are unsupported and general 4x4 projection matrix should
        be fetched instead
        """

    def ProcessEvents(self) -> None:
        """Receive XR events."""

    def UnitFactor(self) -> float:
        """
        Return unit scale factor defined as scale factor for m (meters); 1.0 by default.
        """

    def SetUnitFactor(self, theFactor: float) -> None:
        """Set unit scale factor."""

    def Aspect(self) -> float:
        """Return aspect ratio."""

    def FieldOfView(self) -> float:
        """Return field of view."""

    def IOD(self) -> float:
        """
        Return Intra-ocular Distance (IOD); also known as Interpupillary Distance (IPD).
        Defined in meters by default (@sa UnitFactor()).
        """

    def DisplayFrequency(self) -> float:
        """Return display frequency or 0 if unknown."""

    def ProjectionFrustum(self, theEye: Aspect_Eye) -> "Aspect_FrustumLRBT<double>":
        """
        Return projection frustum.
        @sa HasProjectionFrustums().
        """

    def HeadPose(self) -> nanoocp.gp.gp_Trsf:
        """
        Return head orientation in right-handed system:
        +y is up
        +x is to the right
        -z is forward
        Distance unit is meters by default (@sa UnitFactor()).
        """

    def LeftHandPose(self) -> nanoocp.gp.gp_Trsf:
        """Return left hand orientation."""

    def RightHandPose(self) -> nanoocp.gp.gp_Trsf:
        """Return right hand orientation."""

    def TrackedPoses(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Aspect.Aspect_TrackedDevicePose]:
        """Return number of tracked poses array."""

    def HasTrackedPose(self, theDevice: int) -> bool:
        """Return TRUE if device orientation is defined."""

    def NamedTrackedDevice(self, theDevice: Aspect_XRTrackedDeviceRole) -> int:
        """Return index of tracked device of known role, or -1 if undefined."""

    @overload
    def LoadRenderModel(self, theDevice: int) -> tuple[nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles, nanoocp.Image.Image_Texture]:
        """
        Load model for displaying device.
        @param[in] theDevice   device index
        @param[out] theTexture  texture source
        @return model triangulation or NULL if not found
        """

    @overload
    def LoadRenderModel(self, theDevice: int, theToApplyUnitFactor: bool) -> tuple[nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles, nanoocp.Image.Image_Texture]:
        """
        Load model for displaying device.
        @param[in] theDevice   device index
        @param[in] theToApplyUnitFactor  flag to apply unit scale factor
        @param[out] theTexture  texture source
        @return model triangulation or NULL if not found
        """

    def GetDigitalActionData(self, theAction: Aspect_XRAction | None) -> Aspect_XRDigitalActionData:
        """
        Fetch data for digital input action (like button).
        @param[in] theAction  action of Aspect_XRActionType_InputDigital type
        """

    def GetAnalogActionData(self, theAction: Aspect_XRAction | None) -> Aspect_XRAnalogActionData:
        """
        Fetch data for digital input action (like axis).
        @param[in] theAction  action of Aspect_XRActionType_InputAnalog type
        """

    def GetPoseActionDataForNextFrame(self, theAction: Aspect_XRAction | None) -> Aspect_XRPoseActionData:
        """
        Fetch data for pose input action (like fingertip position).
        The returned values will match the values returned by the last call to WaitPoses().
        @param[in] theAction  action of Aspect_XRActionType_InputPose type
        """

    def TriggerHapticVibrationAction(self, theAction: Aspect_XRAction | None, theParams: Aspect_XRHapticActionData) -> None:
        """Trigger vibration."""

    def AbortHapticVibrationAction(self, theAction: Aspect_XRAction | None) -> None:
        """Abort vibration."""

    def TrackingOrigin(self) -> Aspect_XRSession.TrackingUniverseOrigin:
        """Return tracking origin."""

    def SetTrackingOrigin(self, theOrigin: Aspect_XRSession.TrackingUniverseOrigin) -> None:
        """Set tracking origin."""

    def GenericAction(self, theDevice: Aspect_XRTrackedDeviceRole, theAction: Aspect_XRGenericAction) -> Aspect_XRAction:
        """Return generic action for specific hand or NULL if undefined."""

    def GetString(self, theInfo: Aspect_XRSession.InfoString) -> nanoocp.TCollection.TCollection_AsciiString:
        """Query information."""

class Aspect_OpenVRSession(Aspect_XRSession):
    """OpenVR wrapper implementing Aspect_XRSession interface."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Aspect_OpenVRSession) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsHmdPresent() -> bool:
        """
        Return TRUE if an HMD may be presented on the system (e.g. to show VR checkbox in application
        GUI). This is fast check, and even if it returns TRUE, opening session may fail.
        """

    def IsOpen(self) -> bool:
        """Return TRUE if session is opened."""

    def Open(self) -> bool:
        """Initialize session."""

    def Close(self) -> None:
        """Release session."""

    def WaitPoses(self) -> bool:
        """Fetch actual poses of tracked devices."""

    def RecommendedViewport(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return recommended viewport Width x Height for rendering into VR."""

    def EyeToHeadTransform(self, theEye: Aspect_Eye) -> nanoocp.BVH.BVH_Mat4d:
        """
        Return transformation from eye to head.
        vr::GetEyeToHeadTransform() wrapper.
        """

    def ProjectionMatrix(self, theEye: Aspect_Eye, theZNear: float, theZFar: float) -> nanoocp.BVH.BVH_Mat4d:
        """Return projection matrix."""

    def HasProjectionFrustums(self) -> bool:
        """Return TRUE."""

    def ProcessEvents(self) -> None:
        """Receive XR events."""

    def GetString(self, theInfo: Aspect_XRSession.InfoString) -> nanoocp.TCollection.TCollection_AsciiString:
        """Query information."""

    def NamedTrackedDevice(self, theDevice: Aspect_XRTrackedDeviceRole) -> int:
        """Return index of tracked device of known role."""

    def GetDigitalActionData(self, theAction: Aspect_XRAction | None) -> Aspect_XRDigitalActionData:
        """Fetch data for digital input action (like button)."""

    def GetAnalogActionData(self, theAction: Aspect_XRAction | None) -> Aspect_XRAnalogActionData:
        """Fetch data for analog input action (like axis)."""

    def GetPoseActionDataForNextFrame(self, theAction: Aspect_XRAction | None) -> Aspect_XRPoseActionData:
        """Fetch data for pose input action (like fingertip position)."""

    def SetTrackingOrigin(self, theOrigin: Aspect_XRSession.TrackingUniverseOrigin) -> None:
        """Set tracking origin."""

class Aspect_IdentDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_RectangularGrid(Aspect_Grid):
    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetXStep(self, aStep: float) -> None:
        """defines the x step of the grid."""

    def SetYStep(self, aStep: float) -> None:
        """defines the y step of the grid."""

    def SetAngle(self, anAngle1: float, anAngle2: float) -> None:
        """
        defines the angle of the second network
        the fist angle is given relatively to the horizontal.
        the second angle is given relatively to the vertical.
        """

    def SetGridValues(self, XOrigin: float, YOrigin: float, XStep: float, YStep: float, RotationAngle: float) -> None: ...

    def Compute(self, X: float, Y: float) -> tuple[float, float]:
        """returns the point of the grid the closest to the point X,Y"""

    def XStep(self) -> float:
        """returns the x step of the grid."""

    def YStep(self) -> float:
        """returns the x step of the grid."""

    def FirstAngle(self) -> float:
        """returns the x Angle of the grid, relatively to the horizontal."""

    def SecondAngle(self) -> float:
        """returns the y Angle of the grid, relatively to the vertical."""

    def SetSizeX(self, theSize: float) -> None:
        """
        Set full extent of the bounded grid along the plane X direction (plane-local units).
        0.0 (default) means unbounded - the shader draws the grid to the horizon.
        """

    def SizeX(self) -> float:
        """Return the bounded-region extent along plane X. 0.0 means unbounded."""

    def SetSizeY(self, theSize: float) -> None:
        """
        Set full extent of the bounded grid along the plane Y direction (plane-local units).
        0.0 (default) means unbounded.
        """

    def SizeY(self) -> float:
        """Return the bounded-region extent along plane Y. 0.0 means unbounded."""

    def SetZOffset(self, theOffset: float) -> None:
        """
        Set signed offset (plane-local units) applied along the plane normal for
        display only - snap math stays on the plane. Use a small negative value
        to push the grid slightly below coplanar geometry and avoid z-fighting.
        """

    def ZOffset(self) -> float:
        """Return the display-time Z-offset along the plane normal."""

    def Init(self) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_ScrollDelta:
    """Parameters for mouse scroll action."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theValue: float, theFlags: int = 0) -> None:
        """Constructor with undefined point."""

    @overload
    def __init__(self, thePnt: nanoocp.BVH.BVH_Vec2i, theValue: float, theFlags: int = 0) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Aspect_ScrollDelta) -> None: ...

    def HasPoint(self) -> bool:
        """Return true if action has point defined."""

    def ResetPoint(self) -> None:
        """Reset at point."""

    @property
    def Point(self) -> nanoocp.BVH.BVH_Vec2i:
        """scale position"""

    @Point.setter
    def Point(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

    @property
    def Delta(self) -> float:
        """delta in pixels"""

    @Delta.setter
    def Delta(self, arg: float, /) -> None: ...

    @property
    def Flags(self) -> int:
        """key flags"""

    @Flags.setter
    def Flags(self, arg: int, /) -> None: ...

class Aspect_SkydomeBackground:
    """This class allows the definition of a window skydome background."""

    @overload
    def __init__(self) -> None:
        """
        Creates a window skydome background.
        By default skydome is initialized with sun at its zenith (0.0, 1.0, 0.0),
        average clody (0.2), zero time parameter, zero fogginess, 512x512 texture size.
        """

    @overload
    def __init__(self, theSunDirection: nanoocp.gp.gp_Dir, theCloudiness: float, theTime: float, theFogginess: float, theSize: int) -> None:
        """
        Creates a window skydome background with given parameters.
        @param[in] theSunDirection direction to the sun (moon). Sun direction with negative Y
        component
        represents moon with (-X, -Y, -Z) direction.
        @param[in] theCloudiness   cloud intensity, 0.0 means no clouds at all and 1.0 - high clody.
        @param[in] theTime         time parameter of simulation. Might be tweaked to slightly change
        appearance.
        @param[in] theFogginess    fog intensity, 0.0 means no fog and 1.0 - high fogginess
        @param[in] theSize         size of cubemap side in pixels.
        """

    @overload
    def __init__(self, theOther: Aspect_SkydomeBackground) -> None: ...

    def SunDirection(self) -> nanoocp.gp.gp_Dir:
        """
        Get sun direction. By default this value is (0, 1, 0)
        Sun direction with negative Y component represents moon with (-X, -Y, -Z) direction.
        """

    def Cloudiness(self) -> float:
        """
        Get cloud intensity. By default this value is 0.2
        0.0 means no clouds at all and 1.0 - high clody.
        """

    def TimeParameter(self) -> float:
        """
        Get time of cloud simulation. By default this value is 0.0
        This value might be tweaked to slightly change appearance of clouds.
        """

    def Fogginess(self) -> float:
        """
        Get fog intensity. By default this value is 0.0
        0.0 means no fog and 1.0 - high fogginess
        """

    def Size(self) -> int:
        """Get size of cubemap. By default this value is 512"""

    def SetSunDirection(self, theSunDirection: nanoocp.gp.gp_Dir) -> None:
        """
        Set sun direction. By default this value is (0, 1, 0)
        Sun direction with negative Y component represents moon with (-X, -Y, -Z) direction.
        """

    def SetCloudiness(self, theCloudiness: float) -> None:
        """
        Set cloud intensity. By default this value is 0.2
        0.0 means no clouds at all and 1.0 - high clody.
        """

    def SetTimeParameter(self, theTime: float) -> None:
        """
        Set time of cloud simulation. By default this value is 0.0
        This value might be tweaked to slightly change appearance of clouds.
        """

    def SetFogginess(self, theFogginess: float) -> None:
        """
        Set fog intensity. By default this value is 0.0
        0.0 means no fog and 1.0 - high fogginess
        """

    def SetSize(self, theSize: int) -> None:
        """Set size of cubemap. By default this value is 512"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Aspect_Touch:
    """Structure holding touch position - original and current location."""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, thePnt: nanoocp.BVH.BVH_Vec2d, theIsPreciseDevice: bool) -> None: ...

    @overload
    def __init__(self, theX: float, theY: float, theIsPreciseDevice: bool) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: Aspect_Touch) -> None: ...

    def Delta(self) -> nanoocp.BVH.BVH_Vec2d:
        """Return values delta."""

    @property
    def From(self) -> nanoocp.BVH.BVH_Vec2d:
        """original touch position"""

    @From.setter
    def From(self, arg: nanoocp.BVH.BVH_Vec2d, /) -> None: ...

    @property
    def To(self) -> nanoocp.BVH.BVH_Vec2d:
        """current  touch position"""

    @To.setter
    def To(self, arg: nanoocp.BVH.BVH_Vec2d, /) -> None: ...

    @property
    def IsPreciseDevice(self) -> bool:
        """
        precise device input (e.g. mouse cursor, NOT emulated from touch screen)
        """

    @IsPreciseDevice.setter
    def IsPreciseDevice(self, arg: bool, /) -> None: ...

class Aspect_VKeySet(nanoocp.Standard.Standard_Transient):
    """Structure defining key state."""

    def __init__(self) -> None:
        """Main constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Modifiers(self) -> int:
        """Return active modifiers."""

    def DownTime(self, theKey: int) -> float:
        """Return timestamp of press event."""

    def TimeUp(self, theKey: int) -> float:
        """Return timestamp of release event."""

    def IsFreeKey(self, theKey: int) -> bool:
        """Return TRUE if key is in Free state."""

    def IsKeyDown(self, theKey: int) -> bool:
        """Return TRUE if key is in Pressed state."""

    def Mutex(self) -> "std::__1::shared_mutex":
        """
        Return mutex for thread-safe updates.
        All operations in class implicitly locks this mutex,
        so this method could be used only for batch processing of keys.
        """

    def Reset(self) -> None:
        """Reset the key state into unpressed state."""

    def KeyDown(self, theKey: int, theTime: float, thePressure: float = 1.0) -> None:
        """
        Press key.
        @param theKey key pressed
        @param theTime event timestamp
        """

    def KeyUp(self, theKey: int, theTime: float) -> None:
        """
        Release key.
        @param theKey key pressed
        @param theTime event timestamp
        """

    def KeyFromAxis(self, theNegative: int, thePositive: int, theTime: float, thePressure: float) -> None:
        """Simulate key up/down events from axis value."""

    def HoldDuration__float(self, theKey: int, theTime: float) -> tuple[bool, float]:
        """
        HoldDuration__float: the C++ overload HoldDuration(Aspect_VKey, double, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Return duration of the button in pressed state.
        @param theKey      key to check
        @param theTime     current time (for computing duration from key down time)
        @param theDuration key press duration
        @return TRUE if key was in pressed state
        """

    def HoldDuration__float__float(self, theKey: int, theTime: float) -> tuple[bool, float, float]:
        """
        HoldDuration__float__float: the C++ overload HoldDuration(Aspect_VKey, double, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Return duration of the button in pressed state.
        @param theKey      key to check
        @param theTime     current time (for computing duration from key down time)
        @param theDuration key press duration
        @param thePressure key pressure
        @return TRUE if key was in pressed state
        """

class Aspect_WindowDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_WindowError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Aspect_WindowInputListener:
    """Defines a listener for window input events."""

    def EventTime(self) -> float:
        """Return event time (e.g. current time)."""

    def ProcessExpose(self) -> None:
        """
        Handle expose event (window content has been invalidation and should be redrawn).
        """

    def ProcessConfigure(self, theIsResized: bool) -> None:
        """Handle window resize event."""

    def ProcessInput(self) -> None:
        """Handle window input event immediately (flush input buffer or ignore)."""

    def ProcessFocus(self, theIsActivated: bool) -> None:
        """Handle focus event."""

    def ProcessClose(self) -> None:
        """Handle window close event."""

    def Keys(self) -> Aspect_VKeySet:
        """
        @name keyboard input
        Return keyboard state.
        """

    def ChangeKeys(self) -> Aspect_VKeySet:
        """Return keyboard state."""

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

    def UpdateMouseScroll(self, theDelta: Aspect_ScrollDelta) -> bool:
        """
        @name mouse input
        Update mouse scroll event.
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
        @return TRUE if window content should be redrawn
        """

    def UpdateMousePosition(self, thePoint: nanoocp.BVH.BVH_Vec2i, theButtons: int, theModifiers: int, theIsEmulated: bool) -> bool:
        """
        Handle mouse cursor movement event.
        This method is expected to be called from UI thread.
        Default implementation does nothing.
        @param thePoint      mouse cursor position
        @param theButtons    pressed buttons
        @param theModifiers  key modifiers
        @param theIsEmulated if TRUE then mouse event comes NOT from real mouse
        but emulated from non-precise input like touch on screen
        @return TRUE if window content should be redrawn
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

    def PressedMouseButtons(self) -> int:
        """Return currently pressed mouse buttons."""

    def LastMouseFlags(self) -> int:
        """Return active key modifiers passed with last mouse event."""

    def LastMousePosition(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return last mouse position."""

    def HasTouchPoints(self) -> bool:
        """
        @name multi-touch input
        Return TRUE if touches map is not empty.
        """

    def TouchPoints(self) -> nanoocp.NCollection.NCollection_IndexedDataMap__unsigned_long__Aspect_Touch:
        """Return map of active touches."""

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

    def Get3dMouseTranslationScale(self) -> float:
        """
        @name 3d mouse input
        Return acceleration ratio for translation event; 2.0 by default.
        """

    def Set3dMouseTranslationScale(self, theScale: float) -> None:
        """Set acceleration ratio for translation event."""

    def Get3dMouseRotationScale(self) -> float:
        """Return acceleration ratio for rotation event; 4.0 by default."""

    def Set3dMouseRotationScale(self, theScale: float) -> None:
        """Set acceleration ratio for rotation event."""

    def To3dMousePreciseInput(self) -> bool:
        """Return quadric acceleration flag; TRUE by default."""

    def Set3dMousePreciseInput(self, theIsQuadric: bool) -> None:
        """Set quadric acceleration flag."""

    def Get3dMouseIsNoRotate(self) -> "NCollection_Vec3<bool>":
        """
        Return 3d mouse rotation axes (tilt/roll/spin) ignore flag; (FALSE, FALSE, FALSE) by default.
        """

    def Change3dMouseIsNoRotate(self) -> "NCollection_Vec3<bool>":
        """
        Return 3d mouse rotation axes (tilt/roll/spin) ignore flag; (FALSE, FALSE, FALSE) by default.
        """

    def Get3dMouseToReverse(self) -> "NCollection_Vec3<bool>":
        """
        Return 3d mouse rotation axes (tilt/roll/spin) reverse flag; (TRUE, FALSE, FALSE) by default.
        """

    def Change3dMouseToReverse(self) -> "NCollection_Vec3<bool>":
        """
        Return 3d mouse rotation axes (tilt/roll/spin) reverse flag; (TRUE, FALSE, FALSE) by default.
        """

    def Update3dMouse(self, theEvent: nanoocp.WNT.WNT_HIDSpaceMouse) -> bool:
        """
        Process 3d mouse input event (redirects to translation, rotation and keys).
        """

    def update3dMouseTranslation(self, theEvent: nanoocp.WNT.WNT_HIDSpaceMouse) -> bool:
        """Process 3d mouse input translation event."""

    def update3dMouseRotation(self, theEvent: nanoocp.WNT.WNT_HIDSpaceMouse) -> bool:
        """Process 3d mouse input rotation event."""

    def update3dMouseKeys(self, theEvent: nanoocp.WNT.WNT_HIDSpaceMouse) -> bool:
        """Process 3d mouse input keys event."""

def Aspect_VKey2Modifier(theKey: int) -> int:
    """Return modifier flags for specified modifier key."""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Aspect
Aspect_TouchMap = nanoocp.NCollection.NCollection_IndexedDataMap__unsigned_long__Aspect_Touch
