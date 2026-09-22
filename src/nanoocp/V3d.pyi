"""OCCT package V3d (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Aspect
import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.Graphic3d
from nanoocp.Graphic3d import Graphic3d_CLight as V3d_Light
import nanoocp.Image
import nanoocp.NCollection
import nanoocp.Prs3d
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class V3d_TypeOfOrientation(enum.IntEnum):
    """
    Determines the type of orientation as a combination of standard DX/DY/DZ directions.
    This enumeration defines a model orientation looking towards the user's eye, which is an
    opposition to Camera main direction. For example, V3d_Xneg defines +X Camera main direction.

    This enumeration defines only main Camera direction, so that the Camera up direction should be
    defined elsewhere for unambiguous Camera definition. Open CASCADE does not force application
    using specific coordinate system, although Draw Harness and samples define +Z-up +Y-forward
    coordinate system for camera view manipulation. Therefore, this enumeration also defines
    V3d_TypeOfOrientation_Zup_* aliases defining front/back/left/top camera orientations for +Z-up
    convention as well as V3d_TypeOfOrientation_Yup_* aliases for another commonly used in other
    systems +Y-up convention. Applications using other coordinate system can define their own
    enumeration, when found suitable.
    """

    V3d_Xpos = 0

    V3d_Ypos = 1

    V3d_Zpos = 2

    V3d_Xneg = 3

    V3d_Yneg = 4

    V3d_Zneg = 5

    V3d_XposYpos = 6

    V3d_XposZpos = 7

    V3d_YposZpos = 8

    V3d_XnegYneg = 9

    V3d_XnegYpos = 10

    V3d_XnegZneg = 11

    V3d_XnegZpos = 12

    V3d_YnegZneg = 13

    V3d_YnegZpos = 14

    V3d_XposYneg = 15

    V3d_XposZneg = 16

    V3d_YposZneg = 17

    V3d_XposYposZpos = 18

    V3d_XposYnegZpos = 19

    V3d_XposYposZneg = 20

    V3d_XnegYposZpos = 21

    V3d_XposYnegZneg = 22

    V3d_XnegYposZneg = 23

    V3d_XnegYnegZpos = 24

    V3d_XnegYnegZneg = 25

    V3d_TypeOfOrientation_Zup_AxoLeft = 24

    V3d_TypeOfOrientation_Zup_AxoRight = 19

    V3d_TypeOfOrientation_Zup_Front = 4

    V3d_TypeOfOrientation_Zup_Back = 1

    V3d_TypeOfOrientation_Zup_Top = 2

    V3d_TypeOfOrientation_Zup_Bottom = 5

    V3d_TypeOfOrientation_Zup_Left = 3

    V3d_TypeOfOrientation_Zup_Right = 0

    V3d_TypeOfOrientation_Yup_AxoLeft = 21

    V3d_TypeOfOrientation_Yup_AxoRight = 18

    V3d_TypeOfOrientation_Yup_Front = 2

    V3d_TypeOfOrientation_Yup_Back = 5

    V3d_TypeOfOrientation_Yup_Top = 1

    V3d_TypeOfOrientation_Yup_Bottom = 4

    V3d_TypeOfOrientation_Yup_Left = 0

    V3d_TypeOfOrientation_Yup_Right = 3

V3d_Xpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Xpos

V3d_Ypos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Ypos

V3d_Zpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Zpos

V3d_Xneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Xneg

V3d_Yneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Yneg

V3d_Zneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_Zneg

V3d_XposYpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYpos

V3d_XposZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposZpos

V3d_YposZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_YposZpos

V3d_XnegYneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYneg

V3d_XnegYpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYpos

V3d_XnegZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegZneg

V3d_XnegZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegZpos

V3d_YnegZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_YnegZneg

V3d_YnegZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_YnegZpos

V3d_XposYneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYneg

V3d_XposZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposZneg

V3d_YposZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_YposZneg

V3d_XposYposZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYposZpos

V3d_XposYnegZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYnegZpos

V3d_XposYposZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYposZneg

V3d_XnegYposZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYposZpos

V3d_XposYnegZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYnegZneg

V3d_XnegYposZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYposZneg

V3d_XnegYnegZpos: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYnegZpos

V3d_XnegYnegZneg: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYnegZneg

V3d_TypeOfOrientation_Zup_AxoLeft: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_AxoRight: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Front: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Back: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Top: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Bottom: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Left: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Zup_Right: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_AxoLeft: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_AxoRight: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Front: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Back: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Top: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Bottom: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Left: V3d_TypeOfOrientation = ...

V3d_TypeOfOrientation_Yup_Right: V3d_TypeOfOrientation = ...

class V3d_StereoDumpOptions(enum.IntEnum):
    """
    Options to be used with image dumping.
    Notice that the value will have no effect with disabled stereo output.
    """

    V3d_SDO_MONO = 0

    V3d_SDO_LEFT_EYE = 1

    V3d_SDO_RIGHT_EYE = 2

    V3d_SDO_BLENDED = 3

V3d_SDO_MONO: V3d_StereoDumpOptions = V3d_StereoDumpOptions.V3d_SDO_MONO

V3d_SDO_LEFT_EYE: V3d_StereoDumpOptions = V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE

V3d_SDO_RIGHT_EYE: V3d_StereoDumpOptions = V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE

V3d_SDO_BLENDED: V3d_StereoDumpOptions = V3d_StereoDumpOptions.V3d_SDO_BLENDED

class V3d_TypeOfView(enum.IntEnum):
    """Defines the type of projection of the view."""

    V3d_ORTHOGRAPHIC = 0

    V3d_PERSPECTIVE = 1

V3d_ORTHOGRAPHIC: V3d_TypeOfView = V3d_TypeOfView.V3d_ORTHOGRAPHIC

V3d_PERSPECTIVE: V3d_TypeOfView = V3d_TypeOfView.V3d_PERSPECTIVE

class V3d_TypeOfVisualization(enum.IntEnum):
    """
    Determines the type of visualization in the view, either
    WIREFRAME or ZBUFFER (shading).
    """

    V3d_WIREFRAME = 0

    V3d_ZBUFFER = 1

V3d_WIREFRAME: V3d_TypeOfVisualization = V3d_TypeOfVisualization.V3d_WIREFRAME

V3d_ZBUFFER: V3d_TypeOfVisualization = V3d_TypeOfVisualization.V3d_ZBUFFER

class V3d_TypeOfAxe(enum.IntEnum):
    """Determines the axis type through the coordinates X, Y, Z."""

    V3d_X = 0

    V3d_Y = 1

    V3d_Z = 2

V3d_X: V3d_TypeOfAxe = V3d_TypeOfAxe.V3d_X

V3d_Y: V3d_TypeOfAxe = V3d_TypeOfAxe.V3d_Y

V3d_Z: V3d_TypeOfAxe = V3d_TypeOfAxe.V3d_Z

class V3d:
    """
    This package contains the set of commands and services
    of the 3D Viewer. It provides a set of high level commands
    to control the views and viewing modes.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: V3d) -> None: ...

    @staticmethod
    def GetProjAxis(theOrientation: V3d_TypeOfOrientation) -> nanoocp.gp.gp_Dir:
        """
        Determines the orientation vector corresponding to the predefined orientation type.
        """

    @staticmethod
    def ArrowOfRadius(garrow: nanoocp.Graphic3d.Graphic3d_Group | None, X0: float, Y0: float, Z0: float, DX: float, DY: float, DZ: float, Alpha: float, Lng: float) -> None:
        """
        Compute the graphic structure of arrow.
        X0,Y0,Z0 : coordinate of the arrow.
        DX,DY,DZ : Direction of the arrow.
        Alpha    : Angle of arrow.
        Lng      : Length of arrow.
        """

    @staticmethod
    def CircleInPlane(gcircle: nanoocp.Graphic3d.Graphic3d_Group | None, X0: float, Y0: float, Z0: float, VX: float, VY: float, VZ: float, Radius: float) -> None:
        """
        Compute the graphic structure of circle.
        X0,Y0,Z0 : Center of circle.
        VX,VY,VZ : Axis of circle.
        Radius   : Radius of circle.
        """

    @staticmethod
    def SwitchViewsinWindow(aPreviousView: V3d_View | None, aNextView: V3d_View | None) -> None: ...

    @staticmethod
    def TypeOfOrientationToString(theType: V3d_TypeOfOrientation) -> str:
        """
        Returns the string name for a given orientation type.
        @param theType orientation type
        @return string identifier from the list Xpos, Ypos, Zpos and others
        """

    @staticmethod
    def TypeOfOrientationFromString(theTypeString: str) -> V3d_TypeOfOrientation:
        """
        Returns the orientation type from the given string identifier (using case-insensitive
        comparison).
        @param theTypeString string identifier
        @return orientation type or V3d_TypeOfOrientation if string identifier is invalid
        """

    @staticmethod
    def TypeOfOrientationFromString__V3d_TypeOfOrientation(theTypeString: str) -> tuple[bool, V3d_TypeOfOrientation]:
        """
        TypeOfOrientationFromString__V3d_TypeOfOrientation: the C++ overload TypeOfOrientationFromString(const char *const, V3d_TypeOfOrientation &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Determines the shape type from the given string identifier (using case-insensitive
        comparison).
        @param theTypeString string identifier
        @param theType detected shape type
        @return TRUE if string identifier is known
        """

class V3d_AmbientLight(nanoocp.Graphic3d.Graphic3d_CLight):
    """Creation of an ambient light source in a viewer."""

    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color = ...) -> None:
        """
        Constructs an ambient light source in the viewer.
        The default Color of this light source is WHITE.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class V3d_BadValue(nanoocp.Standard.Standard_OutOfRange):
    pass

class V3d_CircularGrid(nanoocp.Aspect.Aspect_CircularGrid):
    """
    @deprecated Kept for backward compatibility. CPU-generated circular grid bound to a
    V3d_Viewer. New code should drive grids through V3d_View::GridDisplay(Aspect_GridParams,
    gp_Ax3), which renders an AA, shader-based grid and supports unbounded extents, background mode,
    arc ranges and per-axis scales. This class consumes the same Aspect_CircularGrid
    parameters where the CPU path can render them; arc ranges (AngleStart/AngleEnd) are not
    supported by the CPU path and are reported via Message::SendWarning() and ignored.
    """

    def __init__(self, theOther: V3d_CircularGrid) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColors(self, aColor: nanoocp.Quantity.Quantity_Color, aTenthColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Updates the grid colors and triggers a re-display when they actually change.
        @param[in] aColor      color of the regular rings / spokes
        @param[in] aTenthColor color of every 10-th ring
        """

    def Display(self) -> None:
        """Display the CPU grid in the owning viewer's structure manager."""

    def Erase(self) -> None:
        """
        Erase the CPU grid (the underlying Graphic3d_Structure is hidden, not destroyed).
        """

    def IsDisplayed(self) -> bool:
        """Returns true if the grid structure is currently displayed."""

    def GraphicValues(self) -> tuple[float, float]:
        """
        Returns the grid extent and Z offset (alias for Radius/ZOffset).
        @param[out] Radius outermost ring radius
        @param[out] OffSet plane-normal displacement of the rendered grid
        """

    def SetGraphicValues(self, Radius: float, OffSet: float) -> None:
        """
        Sets the grid extent and Z offset (alias for SetRadius/SetZOffset).
        @param[in] Radius outermost ring radius
        @param[in] OffSet plane-normal displacement
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """
        Dumps the content of me into the stream.
        @param[in,out] theOStream destination stream
        @param[in]     theDepth   recursion depth (-1 for full)
        """

class V3d_PositionLight(nanoocp.Graphic3d.Graphic3d_CLight):
    """Base class for Positional, Spot and Directional Light classes."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class V3d_DirectionalLight(V3d_PositionLight):
    """Directional light source for a viewer."""

    @overload
    def __init__(self, theDirection: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XposYposZpos, theColor: nanoocp.Quantity.Quantity_Color = ..., theIsHeadlight: bool = False) -> None: ...

    @overload
    def __init__(self, theDirection: nanoocp.gp.gp_Dir, theColor: nanoocp.Quantity.Quantity_Color = ..., theIsHeadlight: bool = False) -> None:
        """Creates a directional light source in the viewer."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetDirection(self, theDirection: V3d_TypeOfOrientation) -> None:
        """Defines the direction of the light source by a predefined orientation."""

    @overload
    def SetDirection(self, theVx: float, theVy: float, theVz: float) -> None: ...

    @overload
    def SetDirection(self, theDir: nanoocp.gp.gp_Dir) -> None:
        """Sets direction of directional/spot light."""

class V3d_ImageDumpOptions:
    """The structure defines options for image dump functionality."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: V3d_ImageDumpOptions) -> None: ...

    @property
    def Width(self) -> int:
        """
        Width  of image dump to allocate an image, 0 by default (meaning that image should be already allocated).
        """

    @Width.setter
    def Width(self, arg: int, /) -> None: ...

    @property
    def Height(self) -> int:
        """
        Height of image dump to allocate an image, 0 by default (meaning that image should be already allocated).
        """

    @Height.setter
    def Height(self, arg: int, /) -> None: ...

    @property
    def BufferType(self) -> nanoocp.Graphic3d.Graphic3d_BufferType:
        """Which buffer to dump (color / depth), Graphic3d_BT_RGB by default."""

    @BufferType.setter
    def BufferType(self, arg: nanoocp.Graphic3d.Graphic3d_BufferType, /) -> None: ...

    @property
    def StereoOptions(self) -> V3d_StereoDumpOptions:
        """
        Dumping stereoscopic camera, V3d_SDO_MONO by default (middle-point monographic projection).
        """

    @StereoOptions.setter
    def StereoOptions(self, arg: V3d_StereoDumpOptions, /) -> None: ...

    @property
    def TileSize(self) -> int:
        """
        The view dimension limited for tiled dump, 0 by default (automatic tiling depending on hardware capabilities).
        """

    @TileSize.setter
    def TileSize(self, arg: int, /) -> None: ...

    @property
    def ToAdjustAspect(self) -> bool:
        """
        Flag to override active view aspect ratio by (Width / Height) defined for image dump (TRUE by default).
        """

    @ToAdjustAspect.setter
    def ToAdjustAspect(self, arg: bool, /) -> None: ...

    @property
    def TargetZLayerId(self) -> int:
        """
        Target z layer id which defines the last layer to be drawn before image dump.
        """

    @TargetZLayerId.setter
    def TargetZLayerId(self, arg: int, /) -> None: ...

    @property
    def IsSingleLayer(self) -> bool: ...

    @IsSingleLayer.setter
    def IsSingleLayer(self, arg: bool, /) -> None: ...

    @property
    def LightName(self) -> str: ...

    @LightName.setter
    def LightName(self, arg: str, /) -> None: ...

class V3d_Viewer(nanoocp.Standard.Standard_Transient):
    """
    Defines services on Viewer type objects.
    The methods of this class allow editing and
    interrogation of the parameters linked to the viewer
    its friend classes (View,light,plane).
    """

    @overload
    def __init__(self, theDriver: nanoocp.Graphic3d.Graphic3d_GraphicDriver | None) -> None:
        """
        Create a Viewer with the given graphic driver and with default parameters:
        - View orientation: V3d_XposYnegZpos
        - View background: Quantity_NOC_GRAY30
        - Shading model: V3d_GOURAUD
        """

    @overload
    def __init__(self, theOther: V3d_Viewer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IfMoreViews(self) -> bool:
        """Returns True if One View more can be defined in this Viewer."""

    def CreateView(self) -> V3d_View:
        """Creates a view in the viewer according to its default parameters."""

    @overload
    def SetViewOn(self) -> None:
        """Activates all of the views of a viewer attached to a window."""

    @overload
    def SetViewOn(self, theView: V3d_View | None) -> None:
        """
        Activates a particular view in the Viewer.
        Must be call if the Window attached to the view has been Deiconified.
        """

    @overload
    def SetViewOff(self) -> None:
        """
        Deactivates all the views of a Viewer
        attached to a window.
        """

    @overload
    def SetViewOff(self, theView: V3d_View | None) -> None:
        """
        Deactivates a particular view in the Viewer.
        Must be call if the Window attached to the view
        has been Iconified .
        """

    def Update(self) -> None:
        """Deprecated, Redraw() should be used instead."""

    def Redraw(self) -> None:
        """
        Redraws all the views of the Viewer even if no
        modification has taken place. Must be called if
        all the views of the Viewer are exposed, as for
        example in a global DeIconification.
        """

    def RedrawImmediate(self) -> None:
        """Updates layer of immediate presentations."""

    def Invalidate(self) -> None:
        """Invalidates viewer content but does not redraw it."""

    def Remove(self) -> None:
        """Suppresses the Viewer."""

    def Driver(self) -> nanoocp.Graphic3d.Graphic3d_GraphicDriver:
        """Return Graphic Driver instance."""

    def StructureManager(self) -> nanoocp.Graphic3d.Graphic3d_StructureManager:
        """Returns the structure manager associated to this viewer."""

    def DefaultRenderingParams(self) -> nanoocp.Graphic3d.Graphic3d_RenderingParams:
        """
        Return default Rendering Parameters.
        By default these parameters are set in a new V3d_View.
        """

    def SetDefaultRenderingParams(self, theParams: nanoocp.Graphic3d.Graphic3d_RenderingParams) -> None:
        """Set default Rendering Parameters."""

    def SetDefaultBackgroundColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Defines the default background colour of views
        attached to the viewer by supplying the color object
        """

    def GetGradientBackground(self) -> nanoocp.Aspect.Aspect_GradientBackground:
        """Returns the gradient background of the view."""

    def SetDefaultBgGradientColors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color, theFillStyle: nanoocp.Aspect.Aspect_GradientFillMethod = ...) -> None:
        """
        Defines the default gradient background colours of views
        attached to the viewer by supplying the colour objects
        """

    def DefaultViewSize(self) -> float:
        """Returns the default size of the view."""

    def SetDefaultViewSize(self, theSize: float) -> None:
        """Gives a default size for the creation of views of the viewer."""

    def DefaultViewProj(self) -> V3d_TypeOfOrientation:
        """Returns the default Projection."""

    def SetDefaultViewProj(self, theOrientation: V3d_TypeOfOrientation) -> None:
        """Sets the default projection for creating views in the viewer."""

    def DefaultVisualization(self) -> V3d_TypeOfVisualization:
        """Returns the default type of Visualization."""

    def SetDefaultVisualization(self, theType: V3d_TypeOfVisualization) -> None:
        """Gives the default visualization mode."""

    def DefaultShadingModel(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """
        Returns the default type of Shading; Graphic3d_TypeOfShadingModel_Phong by default.
        """

    def SetDefaultShadingModel(self, theType: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel) -> None:
        """Gives the default type of SHADING."""

    def DefaultTypeOfView(self) -> V3d_TypeOfView:
        """
        Returns the default type of View (orthographic or perspective projection) to be returned by
        CreateView() method.
        """

    def SetDefaultTypeOfView(self, theType: V3d_TypeOfView) -> None:
        """
        Set the default type of View (orthographic or perspective projection) to be returned by
        CreateView() method.
        """

    def DefaultBackgroundColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the default background colour object."""

    def DefaultBgGradientColors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns the gradient background colour objects of the view."""

    def GetAllZLayers(self, theLayerSeq: nanoocp.NCollection.NCollection_Sequence[int]) -> None:
        """
        Return all Z layer ids in sequence ordered by overlay level from lowest layer to highest (
        foreground ). The first layer ID in sequence is the default layer that can't be removed.
        """

    def AddZLayer(self, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings = ...) -> tuple[bool, int]:
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value.
        The Z layers are controlled entirely by viewer, it is not possible to add a layer to a
        particular view. Custom layers will be inserted before Graphic3d_ZLayerId_Top (e.g. between
        Graphic3d_ZLayerId_Default and before Graphic3d_ZLayerId_Top).
        @param[out] theLayerId  id of created layer
        @param[in] theSettings  new layer settings
        @return FALSE if the layer can not be created
        """

    def InsertLayerBefore(self, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerAfter: int) -> tuple[bool, int]:
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value.
        The Z layers are controlled entirely by viewer, it is not possible to add a layer to a
        particular view. Layer rendering order is defined by its position in list (altered by
        theLayerAfter) and IsImmediate() flag (all layers with IsImmediate() flag are drawn
        afterwards);
        @param[out] theNewLayerId  id of created layer; layer id is arbitrary and does not depend on
        layer position in the list
        @param[in] theSettings     new layer settings
        @param[in] theLayerAfter   id of layer to append new layer before
        @return FALSE if the layer can not be created
        """

    def InsertLayerAfter(self, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerBefore: int) -> tuple[bool, int]:
        """
        Add a new top-level Z layer to all managed views and get its ID as <theLayerId> value.
        The Z layers are controlled entirely by viewer, it is not possible to add a layer to a
        particular view. Layer rendering order is defined by its position in list (altered by
        theLayerAfter) and IsImmediate() flag (all layers with IsImmediate() flag are drawn
        afterwards);
        @param[out] theNewLayerId  id of created layer; layer id is arbitrary and does not depend on
        layer position in the list
        @param[in] theSettings     new layer settings
        @param[in] theLayerBefore  id of layer to append new layer after
        @return FALSE if the layer can not be created
        """

    def RemoveZLayer(self, theLayerId: int) -> bool:
        """
        Remove Z layer with ID <theLayerId>.
        Method returns false if the layer can not be removed or doesn't exists.
        By default, there are always default bottom-level layer that can't be removed.
        """

    def ZLayerSettings(self, theLayerId: int) -> nanoocp.Graphic3d.Graphic3d_ZLayerSettings:
        """Returns the settings of a single Z layer."""

    def SetZLayerSettings(self, theLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings) -> None:
        """Sets the settings for a single Z layer."""

    def ActiveViews(self) -> nanoocp.NCollection.NCollection_List[nanoocp.V3d.V3d_View]:
        """Return a list of active views."""

    def ActiveViewIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_V3d_View.Iterator:
        """Return an iterator for active views."""

    def LastActiveView(self) -> bool:
        """returns true if there is only one active view."""

    def DefinedViews(self) -> nanoocp.NCollection.NCollection_List[nanoocp.V3d.V3d_View]:
        """Return a list of defined views."""

    def DefinedViewIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_V3d_View.Iterator:
        """Return an iterator for defined views."""

    def SetDefaultLights(self) -> None:
        """
        @name lights management
        Defines default lights:
        positional-light 0.3 0. 0.
        directional-light V3d_XnegYposZpos
        directional-light V3d_XnegYneg
        ambient-light
        """

    @overload
    def SetLightOn(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Activates MyLight in the viewer."""

    @overload
    def SetLightOn(self) -> None:
        """Activates all the lights defined in this viewer."""

    @overload
    def SetLightOff(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Deactivates MyLight in this viewer."""

    @overload
    def SetLightOff(self) -> None:
        """Deactivate all the Lights defined in this viewer."""

    def AddLight(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Adds Light in Sequence Of Lights."""

    def DelLight(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Delete Light in Sequence Of Lights."""

    def UpdateLights(self) -> None:
        """Updates the lights of all the views of a viewer."""

    def IsGlobalLight(self, TheLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> bool: ...

    def ActiveLights(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_CLight]:
        """Return a list of active lights."""

    def ActiveLightIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_Graphic3d_CLight.Iterator:
        """Return an iterator for defined lights."""

    def DefinedLights(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_CLight]:
        """Return a list of defined lights."""

    def DefinedLightIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_Graphic3d_CLight.Iterator:
        """Return an iterator for defined lights."""

    def Erase(self) -> None:
        """
        @name objects management
        Erase all Objects in All the views.
        """

    def UnHighlight(self) -> None:
        """UnHighlight all Objects in All the views."""

    def ComputedMode(self) -> bool:
        """returns true if the computed mode can be used."""

    def SetComputedMode(self, theMode: bool) -> None:
        """Set if the computed mode can be used."""

    def DefaultComputedMode(self) -> bool:
        """returns true if by default the computed mode must be used."""

    def SetDefaultComputedMode(self, theMode: bool) -> None:
        """Set if by default the computed mode must be used."""

    def PrivilegedPlane(self) -> nanoocp.gp.gp_Ax3:
        """@name privileged plane management"""

    def SetPrivilegedPlane(self, thePlane: nanoocp.gp.gp_Ax3) -> None: ...

    def DisplayPrivilegedPlane(self, theOnOff: bool, theSize: float = 1.0) -> None: ...

    def ActivateGrid(self, aGridType: nanoocp.Aspect.Aspect_GridType, aGridDrawMode: nanoocp.Aspect.Aspect_GridDrawMode) -> None:
        """
        Activates the grid in all views of <me>. Lazily creates the V3d_RectangularGrid
        / V3d_CircularGrid on first use and displays it.
        @param[in] aGridType     rectangular or circular
        @param[in] aGridDrawMode lines, points or none
        """

    def DeactivateGrid(self) -> None:
        """Deactivates the grid in all views of <me>."""

    def IsGridActive(self) -> bool:
        """Returns true if a grid is currently active in <me>."""

    @overload
    def Grid(self, theToCreate: bool = True) -> nanoocp.Aspect.Aspect_Grid:
        """
        Returns the currently selected grid (rectangular / circular per GridType()).
        @param[in] theToCreate when false, returns null instead of allocating
        """

    @overload
    def Grid(self, theGridType: nanoocp.Aspect.Aspect_GridType, theToCreate: bool = True) -> nanoocp.Aspect.Aspect_Grid:
        """
        Returns the grid of the requested type.
        @param[in] theGridType rectangular or circular
        @param[in] theToCreate when false, returns null instead of allocating
        """

    def GridType(self) -> nanoocp.Aspect.Aspect_GridType:
        """Returns the currently selected grid type (rectangular / circular)."""

    def GridDrawMode(self) -> nanoocp.Aspect.Aspect_GridDrawMode:
        """Returns the draw mode (lines / points / none) of the active grid."""

    def RectangularGridValues(self) -> tuple[float, float, float, float, float]:
        """
        Returns the rectangular grid definition.
        @param[out] theXOrigin       grid origin X (snap reference)
        @param[out] theYOrigin       grid origin Y
        @param[out] theXStep         interval between two vertical lines
        @param[out] theYStep         interval between two horizontal lines
        @param[out] theRotationAngle in-plane rotation angle, radians
        """

    def SetRectangularGridValues(self, XOrigin: float, YOrigin: float, XStep: float, YStep: float, RotationAngle: float) -> None:
        """
        Sets the rectangular grid definition.
        @param[in] XOrigin       grid origin X
        @param[in] YOrigin       grid origin Y
        @param[in] XStep         interval between two vertical lines
        @param[in] YStep         interval between two horizontal lines
        @param[in] RotationAngle in-plane rotation angle, radians
        """

    def RectangularGridGraphicValues(self) -> tuple[float, float, float]:
        """
        Returns the rectangular grid extent.
        @param[out] theXSize  width  along grid X
        @param[out] theYSize  height along grid Y
        @param[out] theOffSet plane-normal displacement of the rendered grid
        """

    def SetRectangularGridGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None:
        """
        Sets the rectangular grid extent.
        @param[in] XSize  width  along grid X
        @param[in] YSize  height along grid Y
        @param[in] OffSet plane-normal displacement
        """

    def CircularGridValues(self) -> tuple[float, float, float, int, float]:
        """
        Returns the circular grid definition.
        @param[out] theXOrigin        grid origin X (snap reference)
        @param[out] theYOrigin        grid origin Y
        @param[out] theRadiusStep     radial interval between two concentric circles
        @param[out] theDivisionNumber number of sectors per half-circle
        @param[out] theRotationAngle  in-plane rotation angle, radians
        """

    def SetCircularGridValues(self, XOrigin: float, YOrigin: float, RadiusStep: float, DivisionNumber: int, RotationAngle: float) -> None:
        """
        Sets the circular grid definition.
        @param[in] XOrigin        grid origin X
        @param[in] YOrigin        grid origin Y
        @param[in] RadiusStep     radial interval between two concentric circles
        @param[in] DivisionNumber number of sectors per half-circle (>= 1)
        @param[in] RotationAngle  in-plane rotation angle, radians
        """

    def CircularGridGraphicValues(self) -> tuple[float, float]:
        """
        Returns the circular grid extent.
        @param[out] theRadius outermost ring radius
        @param[out] theOffSet plane-normal displacement of the rendered grid
        """

    def SetCircularGridGraphicValues(self, Radius: float, OffSet: float) -> None:
        """
        Sets the circular grid extent.
        @param[in] Radius outermost ring radius
        @param[in] OffSet plane-normal displacement
        """

    @overload
    def SetGridEcho(self, showGrid: bool = True) -> None:
        """
        Toggle the snap-hit echo marker drawn by ConvertToGrid() at the snapped point.
        @param[in] showGrid when TRUE, the marker is shown on every snap hit
        """

    @overload
    def SetGridEcho(self, aMarker: nanoocp.Graphic3d.Graphic3d_AspectMarker3d | None) -> None:
        """
        Replaces the default echo marker.
        Default attributes when this overload is not called:
        Aspect_TOM_STAR, Quantity_NOC_GRAY90, size 3.0.
        @param[in] aMarker custom marker aspect to use for echo display
        """

    def GridEcho(self) -> bool:
        """Returns TRUE when the snap-hit echo marker is enabled."""

    def ShowGridEcho(self, theView: V3d_View | None, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> None:
        """
        Displays the echo marker in a single view.
        @param[in] theView view in which to draw the echo
        @param[in] thePoint world-space snapped point
        """

    def HideGridEcho(self, theView: V3d_View | None) -> None:
        """
        Temporarily hides the echo marker in a single view (e.g. while not snapping).
        @param[in] theView view in which to hide the echo
        """

    def IsActive(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - IsGridActive() should be used instead

        @name deprecated methods
        Returns true if a grid is activated in <me>.
        """

    def InitActiveViews(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveViews() should be used instead

        Initializes an internal iterator on the active views.
        """

    def MoreActiveViews(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - ActiveViews() should be used instead

        Returns true if there are more active view(s) to return.
        """

    def NextActiveViews(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveViews() should be used instead

        Go to the next active view (if there is not, ActiveView will raise an exception)
        """

    def ActiveView(self) -> V3d_View:
        """
        Deprecated in OCCT: Deprecated method - ActiveViews() should be used instead
        """

    def InitDefinedViews(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - DefinedViews() should be used instead

        Initializes an internal iterator on the Defined views.
        """

    def MoreDefinedViews(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - DefinedViews() should be used instead

        returns true if there are more Defined view(s) to return.
        """

    def NextDefinedViews(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - DefinedViews() should be used instead

        Go to the next Defined view (if there is not, DefinedView will raise an exception)
        """

    def DefinedView(self) -> V3d_View:
        """
        Deprecated in OCCT: Deprecated method - DefinedViews() should be used instead
        """

    def InitActiveLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        Initializes an internal iteratator on the active Lights.
        """

    def MoreActiveLights(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        returns true if there are more active Light(s) to return.
        """

    def NextActiveLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        Go to the next active Light (if there is not, ActiveLight() will raise an exception)
        """

    def ActiveLight(self) -> nanoocp.Graphic3d.Graphic3d_CLight:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead
        """

    def InitDefinedLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - DefinedLights() should be used instead

        Initializes an internal iterattor on the Defined Lights.
        """

    def MoreDefinedLights(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - DefinedLights() should be used instead

        Returns true if there are more Defined Light(s) to return.
        """

    def NextDefinedLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - DefinedLights() should be used instead

        Go to the next Defined Light (if there is not, DefinedLight() will raise an exception)
        """

    def DefinedLight(self) -> nanoocp.Graphic3d.Graphic3d_CLight:
        """
        Deprecated in OCCT: Deprecated method - DefinedLights() should be used instead
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class V3d_Trihedron(nanoocp.Standard.Standard_Transient):
    """Class for presentation of trihedron object."""

    @overload
    def __init__(self) -> None:
        """Creates a default trihedron."""

    @overload
    def __init__(self, theOther: V3d_Trihedron) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsWireframe(self) -> bool:
        """Return TRUE if wireframe presentation is set; FALSE by default."""

    def SetWireframe(self, theAsWireframe: bool) -> None:
        """Switch wireframe / shaded trihedron."""

    def TransformPersistence(self) -> nanoocp.Graphic3d.Graphic3d_TransformPers:
        """Return trihedron position."""

    def SetPosition(self, thePosition: nanoocp.Aspect.Aspect_TypeOfTriedronPosition) -> None:
        """Setup the corner to draw the trihedron."""

    def Scale(self) -> float:
        """Return scale factor."""

    def SetScale(self, theScale: float) -> None:
        """Setup the scale factor."""

    def SizeRatio(self) -> float:
        """Return size ratio factor."""

    def SetSizeRatio(self, theRatio: float) -> None:
        """Setup the size ratio factor."""

    def ArrowDiameter(self) -> float:
        """Return arrow diameter."""

    def SetArrowDiameter(self, theDiam: float) -> None:
        """Setup the arrow diameter."""

    def NbFacets(self) -> int:
        """Return number of facets for tessellation."""

    def SetNbFacets(self, theNbFacets: int) -> None:
        """Setup the number of facets for tessellation."""

    def LabelAspect(self, theAxis: V3d_TypeOfAxe) -> nanoocp.Prs3d.Prs3d_TextAspect:
        """
        Return text aspect for specified axis.
        @param[in] theAxis  axis index
        @return text aspect
        """

    @overload
    def SetLabelsColor(self, theXColor: nanoocp.Quantity.Quantity_Color, theYColor: nanoocp.Quantity.Quantity_Color, theZColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Setup per-label color."""

    @overload
    def SetLabelsColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Setup color of text labels."""

    def ArrowAspect(self, theAxis: V3d_TypeOfAxe) -> nanoocp.Prs3d.Prs3d_ShadingAspect:
        """
        Return shading aspect for specified axis.
        @param[in] theAxis  axis index
        @return shading aspect
        """

    def SetArrowsColor(self, theXColor: nanoocp.Quantity.Quantity_Color, theYColor: nanoocp.Quantity.Quantity_Color, theZColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Setup colors of arrows."""

    def OriginAspect(self) -> nanoocp.Prs3d.Prs3d_ShadingAspect:
        """Return shading aspect of origin sphere."""

    def Label(self, theAxis: V3d_TypeOfAxe) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return axis text.
        @param[in] theAxis  axis index
        @return text of the label
        """

    def SetLabels(self, theX: nanoocp.TCollection.TCollection_AsciiString, theY: nanoocp.TCollection.TCollection_AsciiString, theZ: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Setup per-axis text."""

    @overload
    def Display(self, theView: V3d_View | None) -> None: ...

    @overload
    def Display(self, theView: V3d_View) -> None:
        """Display trihedron."""

    def Erase(self) -> None:
        """Erase trihedron."""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class V3d_View(nanoocp.Standard.Standard_Transient):
    """
    Defines the application object VIEW for the
    VIEWER application.
    The methods of this class allow the editing
    and inquiring the parameters linked to the view.
    Provides a set of services common to all types of view.
    Warning: The default parameters are defined by the class
    Viewer (Example : SetDefaultViewSize()).
    Certain methods are mouse oriented, and it is
    necessary to know the difference between the start and
    the continuation of this gesture in putting the method
    into operation.
    Example : Shifting the eye-view along the screen axes.

    View->Move(10.,20.,0.,True)     (Starting motion)
    View->Move(15.,-5.,0.,False)    (Next motion)
    """

    @overload
    def __init__(self, theViewer: V3d_Viewer | None, theType: V3d_TypeOfView = V3d_TypeOfView.V3d_ORTHOGRAPHIC) -> None:
        """Initializes the view."""

    @overload
    def __init__(self, theViewer: V3d_Viewer | None, theView: V3d_View | None) -> None:
        """Initializes the view by copying."""

    @overload
    def __init__(self, theOther: V3d_View) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetWindow(self, theWindow: nanoocp.Aspect.Aspect_Window | None) -> None:
        """
        Activates the view in the specified Window
        If <aContext> is not NULL the graphic context is used
        to draw something in this view.
        Otherwise an internal graphic context is created.
        Warning: The view is centered and resized to preserve
        the height/width ratio of the window.
        """

    @overload
    def SetWindow(self, theParentView: V3d_View | None, theSize: nanoocp.BVH.BVH_Vec2d, theCorner: nanoocp.Aspect.Aspect_TypeOfTriedronPosition = ..., theOffset: nanoocp.BVH.BVH_Vec2d = ..., theMargins: nanoocp.BVH.BVH_Vec2i = ...) -> None:
        """
        Activates the view as subview of another view.
        @param[in] theParentView parent view to put subview into
        @param[in] theSize subview dimensions;
        values >= 2   define size in pixels,
        values <= 1.0 define size as a fraction of parent view
        @param[in] theCorner corner within parent view
        @param[in] theOffset offset from the corner;
        values >= 1   define offset in pixels,
        values <  1.0 define offset as a fraction of parent view
        @param[in] theMargins subview margins in pixels

        Example: to split parent view horizontally into 2 subview,
        define one subview with Size=(0.5,1.0),Offset=(0.0,0.0), and 2nd with
        Size=(0.5,1.0),Offset=(5.0,0.0);
        """

    def SetMagnify(self, theWindow: nanoocp.Aspect.Aspect_Window | None, thePreviousView: V3d_View | None, theX1: int, theY1: int, theX2: int, theY2: int) -> None: ...

    def Remove(self) -> None:
        """Destroys the view."""

    def Update(self) -> None:
        """Deprecated, Redraw() should be used instead."""

    def Redraw(self) -> None:
        """
        Redisplays the view even if there has not
        been any modification.
        Must be called if the view is shown.
        (Ex: DeIconification ) .
        """

    def RedrawImmediate(self) -> None:
        """Updates layer of immediate presentations."""

    def Invalidate(self) -> None:
        """Invalidates view content but does not redraw it."""

    def IsInvalidated(self) -> bool:
        """Returns true if cached view content has been invalidated."""

    def IsInvalidatedImmediate(self) -> bool:
        """Returns true if immediate layer content has been invalidated."""

    def InvalidateImmediate(self) -> None:
        """
        Invalidates view content within immediate layer but does not redraw it.
        """

    def MustBeResized(self) -> None:
        """
        Must be called when the window supporting the
        view changes size.
        if the view is not mapped on a window.
        Warning: The view is centered and resized to preserve
        the height/width ratio of the window.
        """

    def DoMapping(self) -> None:
        """
        Must be called when the window supporting the
        view is mapped or unmapped.
        """

    def IsEmpty(self) -> bool:
        """
        Returns the status of the view regarding
        the displayed structures inside
        Returns True is The View is empty
        """

    def UpdateLights(self) -> None:
        """Updates the lights of the view."""

    def SetAutoZFitMode(self, theIsOn: bool, theScaleFactor: float = 1.0) -> None:
        """
        Sets the automatic z-fit mode and its parameters.
        The auto z-fit has extra parameters which can controlled from application level
        to ensure that the size of viewing volume will be sufficiently large to cover
        the depth of unmanaged objects, for example, transformation persistent ones.
        @param[in] theScaleFactor  the scale factor for Z-range.
        The range between Z-min, Z-max projection volume planes
        evaluated by z fitting method will be scaled using this coefficient.
        Program error exception is thrown if negative or zero value
        is passed.
        """

    def AutoZFitMode(self) -> bool:
        """returns TRUE if automatic z-fit mode is turned on."""

    def AutoZFitScaleFactor(self) -> float:
        """returns scale factor parameter of automatic z-fit mode."""

    def AutoZFit(self) -> None:
        """
        If automatic z-range fitting is turned on, adjusts Z-min and Z-max
        projection volume planes with call to ZFitAll.
        """

    def ZFitAll(self, theScaleFactor: float = 1.0) -> None:
        """
        Change Z-min and Z-max planes of projection volume to match the
        displayed objects.
        """

    @overload
    def SetBackgroundColor(self, theType: nanoocp.Quantity.Quantity_TypeOfColor, theV1: float, theV2: float, theV3: float) -> None:
        """
        Defines the background color of the view by the color definition type and the three
        corresponding values.
        """

    @overload
    def SetBackgroundColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Defines the background color of the view."""

    def SetBgGradientColors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color, theFillStyle: nanoocp.Aspect.Aspect_GradientFillMethod = ..., theToUpdate: bool = False) -> None:
        """
        Defines the gradient background colors of the view by supplying the colors
        and the fill method (horizontal by default).
        """

    def SetBgGradientStyle(self, theMethod: nanoocp.Aspect.Aspect_GradientFillMethod = ..., theToUpdate: bool = False) -> None:
        """Defines the gradient background fill method of the view."""

    @overload
    def SetBackgroundImage(self, theFileName: str, theFillStyle: nanoocp.Aspect.Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_CENTERED, theToUpdate: bool = False) -> None:
        """
        Defines the background texture of the view by supplying the texture image file name
        and fill method (centered by default).
        """

    @overload
    def SetBackgroundImage(self, theTexture: nanoocp.Graphic3d.Graphic3d_Texture2D | None, theFillStyle: nanoocp.Aspect.Aspect_FillMethod = Aspect_FillMethod.Aspect_FM_CENTERED, theToUpdate: bool = False) -> None:
        """
        Defines the background texture of the view by supplying the texture and fill method (centered
        by default)
        """

    def SetBgImageStyle(self, theFillStyle: nanoocp.Aspect.Aspect_FillMethod, theToUpdate: bool = False) -> None:
        """Defines the textured background fill method of the view."""

    def SetBackgroundCubeMap(self, theCubeMap: nanoocp.Graphic3d.Graphic3d_CubeMap | None, theToUpdatePBREnv: bool = True, theToUpdate: bool = False) -> None:
        """
        Sets environment cubemap as background.
        @param theCubeMap cubemap source to be set as background
        @param theToUpdatePBREnv defines whether IBL maps will be generated or not (see
        'GeneratePBREnvironment')
        """

    def BackgroundSkydome(self) -> nanoocp.Aspect.Aspect_SkydomeBackground:
        """Returns skydome aspect;"""

    def SetBackgroundSkydome(self, theAspect: nanoocp.Aspect.Aspect_SkydomeBackground, theToUpdatePBREnv: bool = True) -> None:
        """
        Sets skydome aspect
        @param theAspect cubemap generation parameters
        @param theToUpdatePBREnv defines whether IBL maps will be generated or not
        """

    def IsImageBasedLighting(self) -> bool:
        """
        Returns TRUE if IBL (Image Based Lighting) from background cubemap is enabled.
        """

    def SetImageBasedLighting(self, theToEnableIBL: bool, theToUpdate: bool = False) -> None:
        """
        Enables or disables IBL (Image Based Lighting) from background cubemap.
        Has no effect if PBR is not used.
        @param[in] theToEnableIBL enable or disable IBL from background cubemap
        @param[in] theToUpdate redraw the view
        """

    def GeneratePBREnvironment(self, theToUpdate: bool = False) -> None:
        """Activates IBL from background cubemap."""

    def ClearPBREnvironment(self, theToUpdate: bool = False) -> None:
        """
        Disables IBL from background cubemap; fills PBR specular probe and irradiance map with white
        color.
        """

    def SetTextureEnv(self, theTexture: nanoocp.Graphic3d.Graphic3d_TextureEnv | None) -> None:
        """
        Sets the environment texture to use. No environment texture by default.
        """

    def SetAxis(self, X: float, Y: float, Z: float, Vx: float, Vy: float, Vz: float) -> None:
        """
        Definition of an axis from its origin and
        its orientation .
        This will be the current axis for rotations and movements.
        Warning! raises BadValue from V3d if the vector normal is NULL. .
        """

    def SetVisualization(self, theType: V3d_TypeOfVisualization) -> None:
        """Defines the visualization type in the view."""

    @overload
    def SetLightOn(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Activates theLight in the view."""

    @overload
    def SetLightOn(self) -> None:
        """Activates all the lights defined in this view."""

    @overload
    def SetLightOff(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Deactivate theLight in this view."""

    @overload
    def SetLightOff(self) -> None:
        """Deactivate all the Lights defined in this view."""

    def IsActiveLight(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> bool:
        """Returns TRUE when the light is active in this view."""

    def SetImmediateUpdate(self, theImmediateUpdate: bool) -> bool:
        """sets the immediate update mode and returns the previous one."""

    def Trihedron(self, theToCreate: bool = True) -> V3d_Trihedron:
        """Returns trihedron object."""

    def ZBufferTriedronSetup(self, theXColor: nanoocp.Quantity.Quantity_Color = ..., theYColor: nanoocp.Quantity.Quantity_Color = ..., theZColor: nanoocp.Quantity.Quantity_Color = ..., theSizeRatio: float = 0.8, theAxisDiametr: float = 0.05, theNbFacettes: int = 12) -> None:
        """
        Customization of the ZBUFFER Triedron.
        XColor,YColor,ZColor - colors of axis
        SizeRatio - ratio of decreasing of the trihedron size when its physical
        position comes out of the view
        AxisDiametr - diameter relatively to axis length
        NbFacettes - number of facets of cylinders and cones
        """

    def TriedronDisplay(self, thePosition: nanoocp.Aspect.Aspect_TypeOfTriedronPosition = Aspect_TypeOfTriedronPosition.Aspect_TOTP_CENTER, theColor: nanoocp.Quantity.Quantity_Color = ..., theScale: float = 0.02, theMode: V3d_TypeOfVisualization = V3d_TypeOfVisualization.V3d_WIREFRAME) -> None:
        """
        Display of the Triedron.
        Initialize position, color and length of Triedron axes.
        The scale is a percent of the window width.
        """

    def TriedronErase(self) -> None:
        """Erases the Triedron."""

    def GetGraduatedTrihedron(self) -> nanoocp.Graphic3d.Graphic3d_GraduatedTrihedron:
        """Returns data of a graduated trihedron."""

    def GraduatedTrihedronDisplay(self, theTrihedronData: nanoocp.Graphic3d.Graphic3d_GraduatedTrihedron) -> None:
        """Displays a graduated trihedron."""

    def GraduatedTrihedronErase(self) -> None:
        """Erases a graduated trihedron from the view."""

    def SetFront(self) -> None:
        """
        modify the Projection of the view perpendicularly to
        the privileged plane of the viewer.
        """

    @overload
    def Rotate(self, Ax: float, Ay: float, Az: float, Start: bool = True) -> None:
        """
        Rotates the eye about the coordinate system of
        reference of the screen
        for which the origin is the view point of the projection,
        with a relative angular value in RADIANS with respect to
        the initial position expressed by Start = true
        Warning! raises BadValue from V3d
        If the eye, the view point, or the high point are
        aligned or confused.
        """

    @overload
    def Rotate(self, Ax: float, Ay: float, Az: float, X: float, Y: float, Z: float, Start: bool = True) -> None:
        """
        Rotates the eye about the coordinate system of
        reference of the screen
        for which the origin is Gravity point {X,Y,Z},
        with a relative angular value in RADIANS with respect to
        the initial position expressed by Start = true
        If the eye, the view point, or the high point are
        aligned or confused.
        """

    @overload
    def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, X: float, Y: float, Z: float, Start: bool = True) -> None:
        """
        Rotates the eye about one of the coordinate axes of
        of the view for which the origin is the Gravity point{X,Y,Z}
        with an relative angular value in RADIANS with
        respect to the initial position expressed by
        Start = true
        """

    @overload
    def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, Start: bool = True) -> None:
        """
        Rotates the eye about one of the coordinate axes of
        of the view for which the origin is the view point of the
        projection with an relative angular value in RADIANS with
        respect to the initial position expressed by
        Start = true
        """

    @overload
    def Rotate(self, Angle: float, Start: bool = True) -> None:
        """
        Rotates the eye around the current axis a relative
        angular value in RADIANS with respect to the initial
        position expressed by Start = true
        """

    @overload
    def Move(self, Dx: float, Dy: float, Dz: float, Start: bool = True) -> None:
        """
        Movement of the eye parallel to the coordinate system
        of reference of the screen a distance relative to the
        initial position expressed by Start = true.
        """

    @overload
    def Move(self, Axe: V3d_TypeOfAxe, Length: float, Start: bool = True) -> None:
        """
        Movement of the eye parallel to one of the axes of the
        coordinate system of reference of the view a distance
        relative to the initial position expressed by
        Start = true.
        """

    @overload
    def Move(self, Length: float, Start: bool = True) -> None:
        """
        Movement of the eye parllel to the current axis
        a distance relative to the initial position
        expressed by Start = true
        """

    @overload
    def Translate(self, Dx: float, Dy: float, Dz: float, Start: bool = True) -> None:
        """
        Movement of the ye and the view point parallel to the
        frame of reference of the screen a distance relative
        to the initial position expressed by
        Start = true
        """

    @overload
    def Translate(self, Axe: V3d_TypeOfAxe, Length: float, Start: bool = True) -> None:
        """
        Movement of the eye and the view point parallel to one
        of the axes of the fame of reference of the view a
        distance relative to the initial position
        expressed by Start = true
        """

    @overload
    def Translate(self, Length: float, Start: bool = True) -> None:
        """
        Movement of the eye and view point parallel to
        the current axis a distance relative to the initial
        position expressed by Start = true
        """

    def Place(self, theXp: int, theYp: int, theZoomFactor: float = 1.0) -> None:
        """
        places the point of the view corresponding
        at the pixel position x,y at the center of the window
        and updates the view.
        """

    @overload
    def Turn(self, Ax: float, Ay: float, Az: float, Start: bool = True) -> None:
        """
        Rotation of the view point around the frame of reference
        of the screen for which the origin is the eye of the
        projection with a relative angular value in RADIANS
        with respect to the initial position expressed by
        Start = true
        """

    @overload
    def Turn(self, Axe: V3d_TypeOfAxe, Angle: float, Start: bool = True) -> None:
        """
        Rotation of the view point around one of the axes of the
        frame of reference of the view for which the origin is
        the eye of the projection with an angular value in
        RADIANS relative to the initial position expressed by
        Start = true
        """

    @overload
    def Turn(self, Angle: float, Start: bool = True) -> None:
        """
        Rotation of the view point around the current axis an
        angular value in RADIANS relative to the initial
        position expressed by Start = true
        """

    def SetTwist(self, Angle: float) -> None:
        """
        Defines the angular position of the high point of
        the reference frame of the view with respect to the
        Y screen axis with an absolute angular value in
        RADIANS.
        """

    def SetEye(self, X: float, Y: float, Z: float) -> None:
        """Defines the position of the eye.."""

    def SetDepth(self, Depth: float) -> None:
        """
        Defines the Depth of the eye from the view point
        without update the projection .
        """

    @overload
    def SetProj(self, Vx: float, Vy: float, Vz: float) -> None:
        """Defines the orientation of the projection."""

    @overload
    def SetProj(self, theOrientation: V3d_TypeOfOrientation, theIsYup: bool = False) -> None:
        """
        Defines the orientation of the projection .
        @param theOrientation camera direction
        @param theIsYup       flag indicating Y-up (TRUE) or Z-up (FALSE) convention
        """

    def SetAt(self, X: float, Y: float, Z: float) -> None:
        """Defines the position of the view point."""

    @overload
    def SetUp(self, Vx: float, Vy: float, Vz: float) -> None:
        """Defines the orientation of the high point."""

    @overload
    def SetUp(self, Orientation: V3d_TypeOfOrientation) -> None:
        """Defines the orientation(SO) of the high point."""

    def SetViewOrientationDefault(self) -> None:
        """
        Saves the current state of the orientation of the view
        which will be the return state at ResetViewOrientation.
        """

    def ResetViewOrientation(self) -> None:
        """
        Resets the orientation of the view.
        Updates the view
        """

    def Panning(self, theDXv: float, theDYv: float, theZoomFactor: float = 1.0, theToStart: bool = True) -> None:
        """
        Translates the center of the view along "x" and "y" axes of
        view projection. Can be used to perform interactive panning operation.
        In that case the DXv, DXy parameters specify panning relative to the
        point where the operation is started.
        @param[in] theDXv  the relative panning on "x" axis of view projection, in view space
        coordinates.
        @param[in] theDYv  the relative panning on "y" axis of view projection, in view space
        coordinates.
        @param[in] theZoomFactor  the zooming factor.
        @param[in] theToStart  pass TRUE when starting panning to remember view
        state prior to panning for relative arguments. If panning is started,
        passing {0, 0} for {theDXv, theDYv} will return view to initial state.
        Performs update of view.
        """

    def SetCenter(self, theXp: int, theYp: int) -> None:
        """
        Relocates center of screen to the point, determined by
        {Xp, Yp} pixel coordinates relative to the bottom-left corner of
        screen. To calculate pixel coordinates for any point from world
        coordinate space, it can be projected using "Project".
        @param[in] theXp  the x coordinate.
        @param[in] theYp  the y coordinate.
        """

    def SetSize(self, theSize: float) -> None:
        """
        Defines the view projection size in its maximum dimension,
        keeping the initial height/width ratio unchanged.
        """

    def SetZSize(self, SetZSize: float) -> None:
        """
        Defines the Depth size of the view
        Front Plane will be set to Size/2.
        Back Plane will be set to -Size/2.
        Any Object located Above the Front Plane or
        behind the Back Plane will be Clipped .
        NOTE than the XY Size of the View is NOT modified .
        """

    def SetZoom(self, Coef: float, Start: bool = True) -> None:
        """
        Zooms the view by a factor relative to the initial
        value expressed by Start = true
        Updates the view.
        """

    def SetScale(self, Coef: float) -> None:
        """
        Zooms the view by a factor relative to the value
        initialised by SetViewMappingDefault().
        Updates the view.
        """

    def SetAxialScale(self, Sx: float, Sy: float, Sz: float) -> None:
        """
        Sets anisotropic (axial) scale factors <Sx>, <Sy>, <Sz> for view <me>.
        Anisotropic scaling operation is performed through multiplying
        the current view orientation matrix by a scaling matrix:
        || Sx  0   0   0 ||
        || 0   Sy  0   0 ||
        || 0   0   Sz  0 ||
        || 0   0   0   1 ||
        Updates the view.
        """

    @overload
    def FitAll(self, theMargin: float = 0.01, theToUpdate: bool = True) -> None:
        """
        Adjust view parameters to fit the displayed scene, respecting height / width ratio.
        The Z clipping range (depth range) is fitted if AutoZFit flag is TRUE.
        Throws program error exception if margin coefficient is < 0 or >= 1.
        Updates the view.
        @param[in] theMargin  the margin coefficient for view borders.
        @param[in] theToUpdate  flag to perform view update.
        """

    @overload
    def FitAll(self, theBox: nanoocp.Bnd.Bnd_Box, theMargin: float = 0.01, theToUpdate: bool = True) -> None:
        """
        Adjust view parameters to fit the displayed scene, respecting height / width ratio
        according to the custom bounding box given.
        Throws program error exception if margin coefficient is < 0 or >= 1.
        Updates the view.
        @param[in] theBox  the custom bounding box to fit.
        @param[in] theMargin  the margin coefficient for view borders.
        @param[in] theToUpdate  flag to perform view update.
        """

    @overload
    def FitAll(self, theMinXv: float, theMinYv: float, theMaxXv: float, theMaxYv: float) -> None:
        """
        Centers the defined projection window so that it occupies
        the maximum space while respecting the initial
        height/width ratio.
        NOTE than the original Z size of the view is NOT modified .
        """

    def DepthFitAll(self, Aspect: float = 0.01, Margin: float = 0.01) -> None:
        """
        Adjusts the viewing volume so as not to clip the displayed objects by front and back
        and back clipping planes. Also sets depth value automatically depending on the
        calculated Z size and Aspect parameter.
        NOTE than the original XY size of the view is NOT modified .
        """

    def WindowFit(self, theMinXp: int, theMinYp: int, theMaxXp: int, theMaxYp: int) -> None:
        """
        Centers the defined PIXEL window so that it occupies
        the maximum space while respecting the initial height/width ratio.
        NOTE than the original Z size of the view is NOT modified.
        @param[in] theMinXp  pixel coordinates of minimal corner on x screen axis.
        @param[in] theMinYp  pixel coordinates of minimal corner on y screen axis.
        @param[in] theMaxXp  pixel coordinates of maximal corner on x screen axis.
        @param[in] theMaxYp  pixel coordinates of maximal corner on y screen axis.
        """

    def SetViewMappingDefault(self) -> None:
        """
        Saves the current view mapping. This will be the
        state returned from ResetViewmapping.
        """

    def ResetViewMapping(self) -> None:
        """
        Resets the centering of the view.
        Updates the view
        """

    def Reset(self, theToUpdate: bool = True) -> None:
        """Resets the centering and the orientation of the view."""

    @overload
    def Convert(self, Vp: int) -> float:
        """
        Converts the PIXEL value
        to a value in the projection plane.
        """

    @overload
    def Convert(self, Vv: float) -> int:
        """
        Converts tha value of the projection plane into
        a PIXEL value.
        """

    @overload
    def Convert(self, Xv: float, Yv: float) -> tuple[int, int]:
        """
        Converts the point defined in the reference frame
        of the projection plane into a point PIXEL.
        """

    @overload
    def Convert(self, X: float, Y: float, Z: float) -> tuple[int, int]:
        """
        Projects the point defined in the reference frame of
        the view into the projected point in the associated window.
        """

    def Convert__float__float(self, Xp: int, Yp: int) -> tuple[float, float]:
        """
        Convert__float__float: the C++ overload Convert(const int, const int, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Converts the point PIXEL into a point projected
        in the reference frame of the projection plane.
        """

    def Convert__float__float__float(self, Xp: int, Yp: int) -> tuple[float, float, float]:
        """
        Convert__float__float__float: the C++ overload Convert(const int, const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Converts the projected point into a point
        in the reference frame of the view corresponding
        to the intersection with the projection plane
        of the eye/view point vector.
        """

    def ConvertWithProj(self, Xp: int, Yp: int) -> tuple[float, float, float, float, float, float]:
        """
        Converts the projected point into a point
        in the reference frame of the view corresponding
        to the intersection with the projection plane
        of the eye/view point vector and returns the
        projection ray for further computations.
        """

    @overload
    def ConvertToGrid(self, Xp: int, Yp: int) -> tuple[float, float, float]:
        """
        Converts the projected point into the nearest grid point
        in the reference frame of the view corresponding
        to the intersection with the projection plane
        of the eye/view point vector and display the grid marker.
        Warning: When the grid is not active the result is identical to the above Convert() method.
        How to use:
        1) Enable the grid echo display
        myViewer->SetGridEcho(true);
        2) When application receive a move event:
        2.1) Check if any object is detected
        if( myInteractiveContext->MoveTo(x,y) == AIS_SOD_Nothing ) {
        2.2) Check if the grid is active
        if( myViewer->Grid()->IsActive() ) {
        2.3) Display the grid echo and gets the grid point
        myView->ConvertToGrid(x,y,X,Y,Z);
        myView->Viewer()->ShowGridEcho (myView, Graphic3d_Vertex (X,Y,Z));
        myView->RedrawImmediate();
        2.4) Else this is the standard case
        } else myView->Convert(x,y,X,Y,Z);
        """

    @overload
    def ConvertToGrid(self, Xp: int, Yp: int, theGridPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """
        Converts the projected point into the nearest visible grid point.
        @return TRUE when an active grid accepts the point; FALSE otherwise.
        Unlike the double-output overload, this method has no unproject fallback
        and is intended for grid echo / snap-hit callers.
        """

    @overload
    def ConvertToGrid(self, X: float, Y: float, Z: float) -> tuple[float, float, float]:
        """
        Converts the point into the nearest grid point
        and display the grid marker.
        """

    def ConvertToGridEcho(self, Xp: int, Yp: int, theGridPoint: nanoocp.Graphic3d.Graphic3d_Vertex, theEchoPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """
        Converts the projected point into the nearest visible grid point and echo display point.
        The echo display point is suitable only for displaying the grid echo marker.
        """

    def Project__float__float(self, theX: float, theY: float, theZ: float) -> tuple[float, float]:
        """
        Project__float__float: the C++ overload Project(const double, const double, const double, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Converts the point defined in the user space of
        the view to the projection plane at the depth
        relative to theZ.
        """

    def Project__float__float__float(self, theX: float, theY: float, theZ: float) -> tuple[float, float, float]:
        """
        Project__float__float__float: the C++ overload Project(const double, const double, const double, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Converts the point defined in the user space of
        the view to the projection plane at the depth
        relative to theZ.
        """

    @overload
    def BackgroundColor(self, Type: nanoocp.Quantity.Quantity_TypeOfColor) -> tuple[float, float, float]:
        """
        Returns the Background color values of the view
        depending of the color Type.
        """

    @overload
    def BackgroundColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the Background color object of the view."""

    def GradientBackgroundColors(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color) -> None:
        """Returns the gradient background colors of the view."""

    def GradientBackground(self) -> nanoocp.Aspect.Aspect_GradientBackground:
        """Returns the gradient background of the view."""

    def Scale(self) -> float:
        """
        Returns the current value of the zoom expressed with
        respect to SetViewMappingDefault().
        """

    @overload
    def AxialScale(self) -> tuple[float, float, float]:
        """Returns the current values of the anisotropic (axial) scale factors."""

    @overload
    def AxialScale(self, Dx: int, Dy: int, Axis: V3d_TypeOfAxe) -> None:
        """
        Performs anisotropic scaling of <me> view along the given <Axis>.
        The scale factor is calculated on a basis of
        the mouse pointer displacement <Dx,Dy>.
        The calculated scale factor is then passed to SetAxialScale(Sx, Sy, Sz) method.
        """

    def Size(self) -> tuple[float, float]:
        """Returns the height and width of the view."""

    def ZSize(self) -> float:
        """Returns the Depth of the view ."""

    def Eye(self) -> tuple[float, float, float]:
        """Returns the position of the eye."""

    def FocalReferencePoint(self) -> tuple[float, float, float]:
        """Returns the position of point which emanating the projections."""

    def ProjReferenceAxe(self, Xpix: int, Ypix: int) -> tuple[float, float, float, float, float, float]:
        """
        Returns the coordinate of the point (Xpix,Ypix)
        in the view (XP,YP,ZP), and the projection vector of the
        view passing by the point (for PerspectiveView).
        """

    def Depth(self) -> float:
        """Returns the Distance between the Eye and View Point."""

    def Proj(self) -> tuple[float, float, float]:
        """Returns the projection vector."""

    def At(self) -> tuple[float, float, float]:
        """Returns the position of the view point."""

    def Up(self) -> tuple[float, float, float]:
        """Returns the vector giving the position of the high point."""

    def Twist(self) -> float:
        """
        Returns in RADIANS the orientation of the view around
        the visual axis measured from the Y axis of the screen.
        """

    def ShadingModel(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """
        Returns the current shading model; Graphic3d_TypeOfShadingModel_Phong by default.
        """

    def SetShadingModel(self, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel) -> None:
        """Defines the shading model for the visualization."""

    def TextureEnv(self) -> nanoocp.Graphic3d.Graphic3d_TextureEnv: ...

    def Visualization(self) -> V3d_TypeOfVisualization:
        """Returns the current visualisation mode."""

    def ActiveLights(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_CLight]:
        """Returns a list of active lights."""

    def ActiveLightIterator(self) -> nanoocp.NCollection.NCollection_List__Handle_Graphic3d_CLight.Iterator:
        """Return iterator for defined lights."""

    def LightLimit(self) -> int:
        """Returns the MAX number of light associated to the view."""

    def Viewer(self) -> V3d_Viewer:
        """Returns the viewer in which the view has been created."""

    def IfWindow(self) -> bool:
        """Returns True if MyView is associated with a window ."""

    def Window(self) -> nanoocp.Aspect.Aspect_Window:
        """Returns the Aspect Window associated with the view."""

    def Type(self) -> V3d_TypeOfView:
        """Returns the Type of the View"""

    def Pan(self, theDXp: int, theDYp: int, theZoomFactor: float = 1.0, theToStart: bool = True) -> None:
        """
        Translates the center of the view along "x" and "y" axes of
        view projection. Can be used to perform interactive panning operation.
        In that case the DXp, DXp parameters specify panning relative to the
        point where the operation is started.
        @param[in] theDXp  the relative panning on "x" axis of view projection, in pixels.
        @param[in] theDYp  the relative panning on "y" axis of view projection, in pixels.
        @param[in] theZoomFactor  the zooming factor.
        @param[in] theToStart  pass TRUE when starting panning to remember view
        state prior to panning for relative arguments. Passing 0 for relative
        panning parameter should return view panning to initial state.
        Performs update of view.
        """

    def Zoom(self, theXp1: int, theYp1: int, theXp2: int, theYp2: int) -> None:
        """
        Zoom the view according to a zoom factor computed
        from the distance between the 2 mouse position.
        @param[in] theXp1  the x coordinate of first mouse position, in pixels.
        @param[in] theYp1  the y coordinate of first mouse position, in pixels.
        @param[in] theXp2  the x coordinate of second mouse position, in pixels.
        @param[in] theYp2  the y coordinate of second mouse position, in pixels.
        """

    def StartZoomAtPoint(self, theXp: int, theYp: int) -> None:
        """
        Defines starting point for ZoomAtPoint view operation.
        @param[in] theXp  the x mouse coordinate, in pixels.
        @param[in] theYp  the y mouse coordinate, in pixels.
        """

    def ZoomAtPoint(self, theMouseStartX: int, theMouseStartY: int, theMouseEndX: int, theMouseEndY: int) -> None:
        """Zooms the model at a pixel defined by the method StartZoomAtPoint()."""

    def StartRotation(self, X: int, Y: int, zRotationThreshold: float = 0.0) -> None:
        """
        Begin the rotation of the view around the screen axis
        according to the mouse position <X,Y>.
        Warning: Enable rotation around the Z screen axis when <zRotationThreshold>
        factor is > 0 soon the distance from the start point and the center
        of the view is > (medium viewSize * <zRotationThreshold> ).
        Generally a value of 0.4 is usable to rotate around XY screen axis
        inside the circular threshold area and to rotate around Z screen axis
        outside this area.
        """

    def Rotation(self, X: int, Y: int) -> None:
        """
        Continues the rotation of the view
        with an angle computed from the last and new mouse position <X,Y>.
        """

    def SetFocale(self, Focale: float) -> None:
        """
        Change View Plane Distance for Perspective Views
        Warning! raises TypeMismatch from Standard if the view
        is not a perspective view.
        """

    def Focale(self) -> float:
        """Returns the View Plane Distance for Perspective Views"""

    def View(self) -> nanoocp.Graphic3d.Graphic3d_CView:
        """Returns the associated Graphic3d view."""

    def SetComputedMode(self, theMode: bool) -> None:
        """Switches computed HLR mode in the view."""

    def ComputedMode(self) -> bool:
        """Returns the computed HLR mode state."""

    def WindowFitAll(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int) -> None:
        """idem than WindowFit"""

    def FitMinMax(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None, theBox: nanoocp.Bnd.Bnd_Box, theMargin: float, theResolution: float = 0.0, theToEnlargeIfLine: bool = True) -> bool:
        """
        Transform camera eye, center and scale to fit in the passed bounding box specified in WCS.
        @param[in] theCamera  the camera
        @param[in] theBox     the bounding box
        @param[in] theMargin  the margin coefficient for view borders
        @param[in] theResolution  the minimum size of projection of bounding box in Xv or Yv direction
        when it considered to be a thin plane or point (without a volume);
        in this case only the center of camera is adjusted
        @param[in] theToEnlargeIfLine  when TRUE - in cases when the whole bounding box projected into
        thin line going along Z-axis of screen,
        the view plane is enlarged such thatwe see the whole line on
        rotation, otherwise only the center of camera is adjusted.
        @return TRUE if the fit all operation can be done
        """

    def SetGrid(self, aPlane: nanoocp.gp.gp_Ax3, aGrid: nanoocp.Aspect.Aspect_Grid | None) -> None:
        """
        Defines or updates the grid plane and snap object on this view.
        @param[in] aPlane grid plane (origin + axes)
        @param[in] aGrid  snap object (Aspect_RectangularGrid or Aspect_CircularGrid)
        """

    def SetGridActivity(self, aFlag: bool) -> None:
        """
        Activates / deactivates snap on this view.
        @param[in] aFlag true to enable snap, false to disable
        """

    def IsGridActive(self) -> bool:
        """
        Return TRUE if either viewer-managed grid or per-view shader grid is active.
        """

    def IsShaderGridActive(self) -> bool:
        """Return TRUE if the per-view shader grid is active."""

    @overload
    def GridDisplay(self, theParams: nanoocp.Aspect.Aspect_GridParams) -> None:
        """
        Display a shader-rendered grid on the viewer's privileged plane.
        @param[in] theParams appearance: color, scale, bounds, arc, draw-mode, background /
        view-adaptive flags
        """

    @overload
    def GridDisplay(self, theParams: nanoocp.Aspect.Aspect_GridParams, thePlane: nanoocp.gp.gp_Ax3) -> None:
        """
        Display a shader-rendered grid on an explicit plane (overrides the viewer's
        privileged plane for this view only).
        @param[in] theParams appearance parameters; see the single-argument overload
        @param[in] thePlane  world-space grid plane (origin + axes)
        """

    def GridErase(self) -> None:
        """Erase the shader-rendered grid from this view."""

    def Dump(self, theFile: str, theBufferType: nanoocp.Graphic3d.Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_RGB) -> bool:
        """
        Dumps the full contents of the View into the image file. This is an alias for ToPixMap() with
        Image_AlienPixMap.
        @param theFile destination image file (image format is determined by file extension like .png,
        .bmp, .jpg)
        @param theBufferType buffer to dump
        @return FALSE when the dump has failed
        """

    @overload
    def ToPixMap(self, theImage: nanoocp.Image.Image_PixMap, theParams: V3d_ImageDumpOptions) -> bool:
        """
        Dumps the full contents of the view to a pixmap with specified parameters.
        Internally this method calls Redraw() with an offscreen render buffer of requested target size
        (theWidth x theHeight), so that there is no need resizing a window control for making a dump
        of different size.
        """

    @overload
    def ToPixMap(self, theImage: nanoocp.Image.Image_PixMap, theWidth: int, theHeight: int, theBufferType: nanoocp.Graphic3d.Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_RGB, theToAdjustAspect: bool = True, theTargetZLayerId: int = -5, theIsSingleLayer: int = 0, theStereoOptions: V3d_StereoDumpOptions = V3d_StereoDumpOptions.V3d_SDO_MONO, theLightName: str = '') -> bool:
        """
        Dumps the full contents of the view to a pixmap.
        Internally this method calls Redraw() with an offscreen render buffer of requested target size
        (theWidth x theHeight), so that there is no need resizing a window control for making a dump
        of different size.
        @param theImage          target image, will be re-allocated to match theWidth x theHeight
        @param theWidth          target image width
        @param theHeight         target image height
        @param theBufferType     type of the view buffer to dump (color / depth)
        @param theToAdjustAspect when true, active view aspect ratio will be overridden by (theWidth /
        theHeight)
        @param theStereoOptions  how to dump stereographic camera
        """

    def SetBackFacingModel(self, theModel: nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel = ...) -> None:
        """Manages display of the back faces"""

    def BackFacingModel(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel:
        """
        Returns current state of the back faces display; Graphic3d_TypeOfBackfacingModel_Auto by
        default, which means that backface culling is defined by each presentation.
        """

    def AddClipPlane(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane | None) -> None:
        """
        Adds clip plane to the view. The composition of clip planes truncates the
        rendering space to convex volume. Number of supported clip planes can be consulted
        by PlaneLimit method of associated Graphic3d_GraphicDriver.
        Please be aware that the planes which exceed the limit are ignored during rendering.
        @param[in] thePlane  the clip plane to be added to view.
        """

    def RemoveClipPlane(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane | None) -> None:
        """
        Removes clip plane from the view.
        @param[in] thePlane  the clip plane to be removed from view.
        """

    def ClipPlanes(self) -> nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane:
        """
        Get clip planes.
        @return sequence clip planes that have been set for the view
        """

    def SetClipPlanes(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None) -> None:
        """
        Sets sequence of clip planes to the view. The planes that have been set
        before are removed from the view. The composition of clip planes
        truncates the rendering space to convex volume. Number of supported
        clip planes can be consulted by InquirePlaneLimit method of
        Graphic3d_GraphicDriver. Please be aware that the planes that
        exceed the limit are ignored during rendering.
        @param[in] thePlanes  the clip planes to set.
        """

    def PlaneLimit(self) -> int:
        """Returns the MAX number of clipping planes associated to the view."""

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Change camera used by view."""

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """
        Returns camera object of the view.
        @return: handle to camera object, or NULL if 3D view does not use
        the camera approach.
        """

    def DefaultCamera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Return default camera."""

    def RenderingParams(self) -> nanoocp.Graphic3d.Graphic3d_RenderingParams:
        """
        Returns current rendering parameters and effect settings.
        By default it returns default parameters of current viewer.
        To define view-specific settings use method V3d_View::ChangeRenderingParams().
        @sa V3d_Viewer::DefaultRenderingParams()
        """

    def ChangeRenderingParams(self) -> nanoocp.Graphic3d.Graphic3d_RenderingParams:
        """Returns reference to current rendering parameters and effect settings."""

    def IsCullingEnabled(self) -> bool:
        """@return flag value of objects culling mechanism"""

    def SetFrustumCulling(self, theMode: bool) -> None:
        """
        Turn on/off automatic culling of objects outside frustum (ON by default)
        """

    def DiagnosticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theFlags: nanoocp.Graphic3d.Graphic3d_DiagnosticInfo) -> None:
        """
        Fill in the dictionary with diagnostic info.
        Should be called within rendering thread.

        This API should be used only for user output or for creating automated reports.
        The format of returned information (e.g. key-value layout)
        is NOT part of this API and can be changed at any time.
        Thus application should not parse returned information to weed out specific parameters.
        @param theDict  destination map for information
        @param theFlags defines the information to be retrieved
        """

    @overload
    def StatisticInformation(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns string with statistic performance info."""

    @overload
    def StatisticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Fills in the dictionary with statistic performance info."""

    def GravityPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns the Objects number and the gravity center of ALL viewable points in the view
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    def IsSubview(self) -> bool:
        """
        @name subvew management
        Return TRUE if this is a subview of another view.
        """

    def ParentView(self) -> V3d_View:
        """Return parent View or NULL if this is not a subview."""

    def Subviews(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.V3d.V3d_View]:
        """Return subview list."""

    def PickSubview(self, thePnt: nanoocp.BVH.BVH_Vec2i) -> V3d_View:
        """Pick subview from the given 2D point."""

    def AddSubview(self, theView: V3d_View | None) -> None:
        """Add subview to the list."""

    def RemoveSubview(self, theView: V3d_View) -> bool:
        """Remove subview from the list."""

    def IfMoreLights(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        @name deprecated methods
        Returns True if One light more can be
        activated in this View.
        """

    def InitActiveLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        initializes an iteration on the active Lights.
        """

    def MoreActiveLights(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        returns true if there are more active Light(s) to return.
        """

    def NextActiveLights(self) -> None:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead

        Go to the next active Light (if there is not, ActiveLight will raise an exception)
        """

    def ActiveLight(self) -> nanoocp.Graphic3d.Graphic3d_CLight:
        """
        Deprecated in OCCT: Deprecated method - ActiveLights() should be used instead
        """

class V3d_Plane(nanoocp.Standard.Standard_Transient):
    """
    Obsolete clip plane presentation class.
    Ported on new core of Graphic3d_ClipPlane approach.
    Please access Graphic3d_ClipPlane via ClipPlane() method
    to use it for standard clipping workflow.
    Example of use:
    @code

    occ::handle<V3d_Plane> aPlane (0, 1, 0, -20);
    occ::handle<V3d_View> aView;
    aView->AddClipPlane (aPlane->ClipPlane());

    aPlane->Display (aView);
    aPlane->SetPlane (0, 1, 0, -30);
    aView->RemoveClipPlane (aPlane->ClipPlane());

    @endcode
    Use interface of this class to modify plane equation synchronously
    with clipping equation.
    """

    @overload
    def __init__(self, theA: float = 0.0, theB: float = 0.0, theC: float = 1.0, theD: float = 0.0) -> None:
        """Creates a clipping plane from plane coefficients."""

    @overload
    def __init__(self, theOther: V3d_Plane) -> None: ...

    def SetPlane(self, theA: float, theB: float, theC: float, theD: float) -> None:
        """Change plane equation."""

    def Display(self, theView: V3d_View | None, theColor: nanoocp.Quantity.Quantity_Color = ...) -> None:
        """Display the plane representation in the chosen view."""

    def Erase(self) -> None:
        """Erase the plane representation."""

    def Plane(self) -> tuple[float, float, float, float]:
        """Returns the parameters of the plane."""

    def IsDisplayed(self) -> bool:
        """Returns TRUE when the plane representation is displayed."""

    def ClipPlane(self) -> nanoocp.Graphic3d.Graphic3d_ClipPlane:
        """
        Use this method to pass clipping plane implementation for
        standard clipping workflow.
        @return clipping plane implementation handle.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class V3d_PositionalLight(V3d_PositionLight):
    """
    Creation and modification of an isolated (positional) light source.
    It is also defined by the color and two attenuation factors ConstAttentuation() and
    LinearAttentuation(). The resulting attenuation factor determining the illumination of a surface
    depends on the following formula:
    @code
    F = 1 / (ConstAttenuation() + LinearAttenuation() * Distance)
    @endcode
    Where Distance is the distance of the isolated source from the surface.
    """

    def __init__(self, thePos: nanoocp.gp.gp_Pnt, theColor: nanoocp.Quantity.Quantity_Color = ...) -> None:
        """
        Creates an isolated light source in the viewer with default attenuation factors (1.0, 0.0).
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Position__float__float__float(self) -> tuple[float, float, float]:
        """
        Position__float__float__float: the C++ overload Position(double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns location of positional/spot light.
        """

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """Returns location of positional/spot light; (0, 0, 0) by default."""

    @overload
    def SetPosition(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def SetPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None:
        """Setup location of positional/spot light."""

class V3d_RectangularGrid(nanoocp.Aspect.Aspect_RectangularGrid):
    """
    @deprecated Kept for backward compatibility. CPU-generated grid bound to a V3d_Viewer.
    New code should drive grids through V3d_View::GridDisplay(Aspect_GridParams, gp_Ax3),
    which renders an AA, shader-based grid and supports unbounded extents, background mode, arc
    ranges and per-axis scales. This class consumes the same Aspect_RectangularGrid
    parameters where the CPU path can render them; unsupported parameters are reported
    via Message::SendWarning() and ignored.
    """

    def __init__(self, theOther: V3d_RectangularGrid) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColors(self, aColor: nanoocp.Quantity.Quantity_Color, aTenthColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Updates the grid colors and triggers a re-display when they actually change.
        @param[in] aColor      color of the regular lines / points
        @param[in] aTenthColor color of every 10-th line
        """

    def Display(self) -> None:
        """Display the CPU grid in the owning viewer's structure manager."""

    def Erase(self) -> None:
        """
        Erase the CPU grid (the underlying Graphic3d_Structure is hidden, not destroyed).
        """

    def IsDisplayed(self) -> bool:
        """Returns true if the grid structure is currently displayed."""

    def GraphicValues(self) -> tuple[float, float, float]:
        """
        Returns the grid bounds and Z offset (alias for SizeX/SizeY/ZOffset).
        @param[out] XSize  width  along grid X
        @param[out] YSize  height along grid Y
        @param[out] OffSet plane-normal displacement of the rendered grid
        """

    def SetGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None:
        """
        Sets the grid bounds and Z offset (alias for SetSizeX/SetSizeY/SetZOffset).
        @param[in] XSize  width  along grid X
        @param[in] YSize  height along grid Y
        @param[in] OffSet plane-normal displacement
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """
        Dumps the content of me into the stream.
        @param[in,out] theOStream destination stream
        @param[in]     theDepth   recursion depth (-1 for full)
        """

class V3d_SpotLight(V3d_PositionLight):
    """
    Creation and modification of a spot.
    The attenuation factor F determines the illumination of a surface:
    @code
    F = 1/(ConstAttenuation() + LinearAttenuation() * Distance)
    @endcode
    Where Distance is the distance from the source to the surface.
    The default values (1.0, 0.0) correspond to a minimum of attenuation.
    The concentration factor determines the dispersion of the light on the surface, the default
    value (1.0) corresponds to a minimum of dispersion.
    """

    @overload
    def __init__(self, thePos: nanoocp.gp.gp_Pnt, theDirection: V3d_TypeOfOrientation = V3d_TypeOfOrientation.V3d_XnegYnegZpos, theColor: nanoocp.Quantity.Quantity_Color = ...) -> None: ...

    @overload
    def __init__(self, thePos: nanoocp.gp.gp_Pnt, theDirection: nanoocp.gp.gp_Dir, theColor: nanoocp.Quantity.Quantity_Color = ...) -> None:
        """
        Creates a light source of the Spot type in the viewer with default attenuation factors (1.0,
        0.0), concentration factor 1.0 and spot angle 30 degrees.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetDirection(self, theOrientation: V3d_TypeOfOrientation) -> None:
        """
        Defines the direction of the light source
        according to a predefined directional vector.
        """

    @overload
    def SetDirection(self, theVx: float, theVy: float, theVz: float) -> None: ...

    @overload
    def SetDirection(self, theDir: nanoocp.gp.gp_Dir) -> None:
        """Sets direction of directional/spot light."""

    def Position__float__float__float(self) -> tuple[float, float, float]:
        """
        Position__float__float__float: the C++ overload Position(double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns location of positional/spot light.
        """

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """Returns location of positional/spot light; (0, 0, 0) by default."""

    @overload
    def SetPosition(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def SetPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None:
        """Setup location of positional/spot light."""

class V3d_UnMapped(nanoocp.Standard.Standard_DomainError):
    pass

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.V3d
V3d_ListOfLight = nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_CLight]
