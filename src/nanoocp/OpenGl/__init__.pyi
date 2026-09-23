"""OCCT package OpenGl (toolkit TKOpenGl)"""

from collections.abc import Sequence
import enum
from typing import TextIO, overload

import nanoocp.Aspect
import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.Font
import nanoocp.Graphic3d
from nanoocp.Graphic3d import Graphic3d_Layer as OpenGl_Layer
import nanoocp.Image
import nanoocp.Message
import nanoocp.NCollection
from nanoocp.OpenGl import OpenGl_Raytrace as OpenGl_Raytrace
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopLoc
import nanoocp.gp


class OpenGl_ShaderProgramDumpLevel(enum.IntEnum):
    """Definition of shader programs source code dump levels."""

    OpenGl_ShaderProgramDumpLevel_Off = 0

    OpenGl_ShaderProgramDumpLevel_Short = 1

    OpenGl_ShaderProgramDumpLevel_Full = 2

OpenGl_ShaderProgramDumpLevel_Off: OpenGl_ShaderProgramDumpLevel = ...

OpenGl_ShaderProgramDumpLevel_Short: OpenGl_ShaderProgramDumpLevel = ...

OpenGl_ShaderProgramDumpLevel_Full: OpenGl_ShaderProgramDumpLevel = ...

class OpenGl_MaterialFlag(enum.IntEnum):
    """Material flag"""

    OpenGl_MaterialFlag_Front = 0

    OpenGl_MaterialFlag_Back = 1

OpenGl_MaterialFlag_Front: OpenGl_MaterialFlag = OpenGl_MaterialFlag.OpenGl_MaterialFlag_Front

OpenGl_MaterialFlag_Back: OpenGl_MaterialFlag = OpenGl_MaterialFlag.OpenGl_MaterialFlag_Back

class OpenGl_FeatureFlag(enum.IntEnum):
    OpenGl_FeatureNotAvailable = 0

    OpenGl_FeatureInExtensions = 1

    OpenGl_FeatureInCore = 2

OpenGl_FeatureNotAvailable: OpenGl_FeatureFlag = OpenGl_FeatureFlag.OpenGl_FeatureNotAvailable

OpenGl_FeatureInExtensions: OpenGl_FeatureFlag = OpenGl_FeatureFlag.OpenGl_FeatureInExtensions

OpenGl_FeatureInCore: OpenGl_FeatureFlag = OpenGl_FeatureFlag.OpenGl_FeatureInCore

class OpenGl_StateVariable(enum.IntEnum):
    """The enumeration of OCCT-specific OpenGL/GLSL variables."""

    OpenGl_OCC_MODEL_WORLD_MATRIX = 0

    OpenGl_OCC_WORLD_VIEW_MATRIX = 1

    OpenGl_OCC_PROJECTION_MATRIX = 2

    OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE = 3

    OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE = 4

    OpenGl_OCC_PROJECTION_MATRIX_INVERSE = 5

    OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE = 6

    OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE = 7

    OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE = 8

    OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE = 9

    OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE = 10

    OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE = 11

    OpenGl_OCC_CLIP_PLANE_EQUATIONS = 12

    OpenGl_OCC_CLIP_PLANE_CHAINS = 13

    OpenGl_OCC_CLIP_PLANE_COUNT = 14

    OpenGl_OCC_LIGHT_SOURCE_COUNT = 15

    OpenGl_OCC_LIGHT_SOURCE_TYPES = 16

    OpenGl_OCC_LIGHT_SOURCE_PARAMS = 17

    OpenGl_OCC_LIGHT_AMBIENT = 18

    OpenGl_OCC_LIGHT_SHADOWMAP_SIZE_BIAS = 19

    OpenGl_OCC_LIGHT_SHADOWMAP_SAMPLERS = 20

    OpenGl_OCC_LIGHT_SHADOWMAP_MATRICES = 21

    OpenGl_OCCT_TEXTURE_ENABLE = 22

    OpenGl_OCCT_DISTINGUISH_MODE = 23

    OpenGl_OCCT_PBR_MATERIAL = 24

    OpenGl_OCCT_COMMON_MATERIAL = 25

    OpenGl_OCCT_ALPHA_CUTOFF = 26

    OpenGl_OCCT_COLOR = 27

    OpenGl_OCCT_BACK_COLOR = 28

    OpenGl_OCCT_OIT_OUTPUT = 29

    OpenGl_OCCT_OIT_DEPTH_FACTOR = 30

    OpenGl_OCCT_TEXTURE_TRSF2D = 31

    OpenGl_OCCT_POINT_SIZE = 32

    OpenGl_OCCT_VIEWPORT = 33

    OpenGl_OCCT_LINE_WIDTH = 34

    OpenGl_OCCT_LINE_FEATHER = 35

    OpenGl_OCCT_LINE_STIPPLE_PATTERN = 36

    OpenGl_OCCT_LINE_STIPPLE_FACTOR = 37

    OpenGl_OCCT_WIREFRAME_COLOR = 38

    OpenGl_OCCT_QUAD_MODE_STATE = 39

    OpenGl_OCCT_ORTHO_SCALE = 40

    OpenGl_OCCT_SILHOUETTE_THICKNESS = 41

    OpenGl_OCCT_NB_SPEC_IBL_LEVELS = 42

    OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES = 43

OpenGl_OCC_MODEL_WORLD_MATRIX: OpenGl_StateVariable = ...

OpenGl_OCC_WORLD_VIEW_MATRIX: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCC_WORLD_VIEW_MATRIX

OpenGl_OCC_PROJECTION_MATRIX: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCC_PROJECTION_MATRIX

OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE: OpenGl_StateVariable = ...

OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE: OpenGl_StateVariable = ...

OpenGl_OCC_PROJECTION_MATRIX_INVERSE: OpenGl_StateVariable = ...

OpenGl_OCC_MODEL_WORLD_MATRIX_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_WORLD_VIEW_MATRIX_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_PROJECTION_MATRIX_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_MODEL_WORLD_MATRIX_INVERSE_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_WORLD_VIEW_MATRIX_INVERSE_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_PROJECTION_MATRIX_INVERSE_TRANSPOSE: OpenGl_StateVariable = ...

OpenGl_OCC_CLIP_PLANE_EQUATIONS: OpenGl_StateVariable = ...

OpenGl_OCC_CLIP_PLANE_CHAINS: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_CHAINS

OpenGl_OCC_CLIP_PLANE_COUNT: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCC_CLIP_PLANE_COUNT

OpenGl_OCC_LIGHT_SOURCE_COUNT: OpenGl_StateVariable = ...

OpenGl_OCC_LIGHT_SOURCE_TYPES: OpenGl_StateVariable = ...

OpenGl_OCC_LIGHT_SOURCE_PARAMS: OpenGl_StateVariable = ...

OpenGl_OCC_LIGHT_AMBIENT: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCC_LIGHT_AMBIENT

OpenGl_OCC_LIGHT_SHADOWMAP_SIZE_BIAS: OpenGl_StateVariable = ...

OpenGl_OCC_LIGHT_SHADOWMAP_SAMPLERS: OpenGl_StateVariable = ...

OpenGl_OCC_LIGHT_SHADOWMAP_MATRICES: OpenGl_StateVariable = ...

OpenGl_OCCT_TEXTURE_ENABLE: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_ENABLE

OpenGl_OCCT_DISTINGUISH_MODE: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_DISTINGUISH_MODE

OpenGl_OCCT_PBR_MATERIAL: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_PBR_MATERIAL

OpenGl_OCCT_COMMON_MATERIAL: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_COMMON_MATERIAL

OpenGl_OCCT_ALPHA_CUTOFF: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_ALPHA_CUTOFF

OpenGl_OCCT_COLOR: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_COLOR

OpenGl_OCCT_BACK_COLOR: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_BACK_COLOR

OpenGl_OCCT_OIT_OUTPUT: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_OIT_OUTPUT

OpenGl_OCCT_OIT_DEPTH_FACTOR: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_OIT_DEPTH_FACTOR

OpenGl_OCCT_TEXTURE_TRSF2D: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_TEXTURE_TRSF2D

OpenGl_OCCT_POINT_SIZE: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_POINT_SIZE

OpenGl_OCCT_VIEWPORT: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_VIEWPORT

OpenGl_OCCT_LINE_WIDTH: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_LINE_WIDTH

OpenGl_OCCT_LINE_FEATHER: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_LINE_FEATHER

OpenGl_OCCT_LINE_STIPPLE_PATTERN: OpenGl_StateVariable = ...

OpenGl_OCCT_LINE_STIPPLE_FACTOR: OpenGl_StateVariable = ...

OpenGl_OCCT_WIREFRAME_COLOR: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_WIREFRAME_COLOR

OpenGl_OCCT_QUAD_MODE_STATE: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_QUAD_MODE_STATE

OpenGl_OCCT_ORTHO_SCALE: OpenGl_StateVariable = OpenGl_StateVariable.OpenGl_OCCT_ORTHO_SCALE

OpenGl_OCCT_SILHOUETTE_THICKNESS: OpenGl_StateVariable = ...

OpenGl_OCCT_NB_SPEC_IBL_LEVELS: OpenGl_StateVariable = ...

OpenGl_OCCT_NUMBER_OF_STATE_VARIABLES: OpenGl_StateVariable = ...

class OpenGl_UniformStateType(enum.IntEnum):
    """Defines types of uniform state variables."""

    OpenGl_LIGHT_SOURCES_STATE = 0

    OpenGl_CLIP_PLANES_STATE = 1

    OpenGl_MODEL_WORLD_STATE = 2

    OpenGl_WORLD_VIEW_STATE = 3

    OpenGl_PROJECTION_STATE = 4

    OpenGl_MATERIAL_STATE = 5

    OpenGl_SURF_DETAIL_STATE = 6

    OpenGL_OIT_STATE = 7

    OpenGl_UniformStateType_NB = 8

OpenGl_LIGHT_SOURCES_STATE: OpenGl_UniformStateType = ...

OpenGl_CLIP_PLANES_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_CLIP_PLANES_STATE

OpenGl_MODEL_WORLD_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_MODEL_WORLD_STATE

OpenGl_WORLD_VIEW_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_WORLD_VIEW_STATE

OpenGl_PROJECTION_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_PROJECTION_STATE

OpenGl_MATERIAL_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_MATERIAL_STATE

OpenGl_SURF_DETAIL_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGl_SURF_DETAIL_STATE

OpenGL_OIT_STATE: OpenGl_UniformStateType = OpenGl_UniformStateType.OpenGL_OIT_STATE

OpenGl_UniformStateType_NB: OpenGl_UniformStateType = ...

class OpenGl_LayerFilter(enum.IntEnum):
    """
    Tool object to specify processed OpenGL layers
    for intermixed rendering of raytracable and non-raytracable layers.
    """

    OpenGl_LF_All = 0

    OpenGl_LF_Upper = 1

    OpenGl_LF_Bottom = 2

    OpenGl_LF_Single = 3

    OpenGl_LF_RayTracable = 4

OpenGl_LF_All: OpenGl_LayerFilter = OpenGl_LayerFilter.OpenGl_LF_All

OpenGl_LF_Upper: OpenGl_LayerFilter = OpenGl_LayerFilter.OpenGl_LF_Upper

OpenGl_LF_Bottom: OpenGl_LayerFilter = OpenGl_LayerFilter.OpenGl_LF_Bottom

OpenGl_LF_Single: OpenGl_LayerFilter = OpenGl_LayerFilter.OpenGl_LF_Single

OpenGl_LF_RayTracable: OpenGl_LayerFilter = OpenGl_LayerFilter.OpenGl_LF_RayTracable

class OpenGl_RenderFilter(enum.IntEnum):
    """Filter for rendering elements."""

    OpenGl_RenderFilter_Empty = 0

    OpenGl_RenderFilter_OpaqueOnly = 1

    OpenGl_RenderFilter_TransparentOnly = 2

    OpenGl_RenderFilter_NonRaytraceableOnly = 4

    OpenGl_RenderFilter_FillModeOnly = 8

    OpenGl_RenderFilter_SkipTrsfPersistence = 16

OpenGl_RenderFilter_Empty: OpenGl_RenderFilter = OpenGl_RenderFilter.OpenGl_RenderFilter_Empty

OpenGl_RenderFilter_OpaqueOnly: OpenGl_RenderFilter = ...

OpenGl_RenderFilter_TransparentOnly: OpenGl_RenderFilter = ...

OpenGl_RenderFilter_NonRaytraceableOnly: OpenGl_RenderFilter = ...

OpenGl_RenderFilter_FillModeOnly: OpenGl_RenderFilter = ...

OpenGl_RenderFilter_SkipTrsfPersistence: OpenGl_RenderFilter = ...

class OpenGl_GlFunctions:
    """Mega structure defines the complete list of OpenGL functions."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlFunctions) -> None: ...

    @staticmethod
    def debugPrintError(theName: str) -> bool:
        """
        Check glGetError(); defined for debugging purposes.
        @return TRUE on error
        """

    @staticmethod
    def readGlVersion() -> tuple[int, int]:
        """Read OpenGL version."""

    def load(self, theCtx: OpenGl_Context, theIsCoreProfile: bool) -> None:
        """Load functions."""

class OpenGl_ArbDbg:
    """Debug context routines"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbDbg) -> None: ...

class OpenGl_ArbFBO:
    """FBO is available on OpenGL 2.0+ hardware"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbFBO) -> None: ...

class OpenGl_ArbFBOBlit:
    """
    FBO blit is available in OpenGL 3.0+.
    Moved out from OpenGl_ArbFBO since it is unavailable in OpenGL ES 2.0.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbFBOBlit) -> None: ...

class OpenGl_ArbIns:
    """
    Instancing is available on OpenGL 3.0+ hardware
    (in core since OpenGL 3.1 or GL_ARB_draw_instanced extension).

    Note that this structure does not include glVertexAttribDivisor(),
    which has been introduced in later OpenGL versions (OpenGL 3.3 or OpenGL ES 3.0).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbIns) -> None: ...

class OpenGl_ArbSamplerObject:
    """
    Provide Sampler Object functionality (texture parameters stored independently from texture
    itself). Available since OpenGL 3.3+ (GL_ARB_sampler_objects extension) and OpenGL ES 3.0+.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbSamplerObject) -> None: ...

class OpenGl_ArbTBO:
    """TBO is available on OpenGL 3.0+ and OpenGL ES 3.2+ hardware"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbTBO) -> None: ...

class OpenGl_ArbTexBindless:
    """
    Provides bindless textures.
    This extension allows OpenGL applications to access texture objects in
    shaders without first binding each texture to one of a limited number of
    texture image units.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ArbTexBindless) -> None: ...

class OpenGl_Element:
    """Base interface for drawable elements."""

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None: ...

    def Release(self, theContext: OpenGl_Context) -> None:
        """
        Release GPU resources.
        Pointer to the context is used because this method might be called
        when the context is already being destroyed and usage of a handle
        would be unsafe
        """

    def IsFillDrawMode(self) -> bool:
        """
        Return TRUE if primitive type generates shaded triangulation (to be used in filters).
        """

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def UpdateMemStats(self, theStats: nanoocp.Graphic3d.Graphic3d_FrameStatsDataTmp) -> None:
        """
        Increment memory usage statistics.
        Default implementation puts EstimatedDataSize() into
        Graphic3d_FrameStatsCounter_EstimatedBytesGeom.
        """

    def UpdateDrawStats(self, theStats: nanoocp.Graphic3d.Graphic3d_FrameStatsDataTmp, theIsDetailed: bool) -> None:
        """
        Increment draw calls statistics.
        @param[in][out] theStats   frame counters to increment
        @param[in] theIsDetailed   indicate detailed dump (more counters - number of triangles,
        points, etc.)
        """

    def SynchronizeAspects(self) -> None:
        """Update parameters of the drawable elements."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_AspectsProgram:
    """OpenGl resources for custom shading program."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_AspectsProgram) -> None: ...

    def ShaderProgram(self, theCtx: OpenGl_Context | None, theShader: nanoocp.Graphic3d.Graphic3d_ShaderProgram | None) -> OpenGl_ShaderProgram:
        """Return shading program."""

    def UpdateRediness(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Update shader resource up-to-date state."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Release resource."""

class OpenGl_AspectsTextureSet:
    """OpenGl resources for custom textures."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_AspectsTextureSet) -> None: ...

    def IsReady(self) -> bool:
        """Return TRUE if resource is up-to-date."""

    def Invalidate(self) -> None:
        """Invalidate resource state."""

    def TextureSet(self, theCtx: OpenGl_Context | None, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None, theSprite: OpenGl_PointSprite | None, theSpriteA: OpenGl_PointSprite | None, theToHighlight: bool) -> OpenGl_TextureSet:
        """Return textures array."""

    def UpdateRediness(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Update texture resource up-to-date state."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Release texture resource."""

class OpenGl_AspectsSprite:
    """OpenGl resources for custom point sprites."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_AspectsSprite) -> None: ...

    def MarkerSize(self) -> float: ...

    def IsReady(self) -> bool:
        """Return TRUE if resource is up-to-date."""

    def Invalidate(self) -> None:
        """Invalidate resource state."""

    def HasPointSprite(self, theCtx: OpenGl_Context | None, theAspects: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> bool:
        """Return TRUE if OpenGl point sprite resource defines texture."""

    def IsDisplayListSprite(self, theCtx: OpenGl_Context | None, theAspects: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> bool:
        """
        Return TRUE if OpenGl point sprite resource defined by obsolete Display List (bitmap).
        """

    def Sprite(self, theCtx: OpenGl_Context | None, theAspects: nanoocp.Graphic3d.Graphic3d_Aspects | None, theIsAlphaSprite: bool) -> OpenGl_PointSprite:
        """Return sprite."""

    def UpdateRediness(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Update texture resource up-to-date state."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Release texture resource."""

class OpenGl_Aspects(OpenGl_Element):
    """The element holding Graphic3d_Aspects."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Create and assign parameters."""

    @overload
    def __init__(self, theOther: OpenGl_Aspects) -> None: ...

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_Aspects:
        """Return aspect."""

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Assign parameters."""

    def ShadingModel(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """Returns Shading Model."""

    def SetNoLighting(self) -> None:
        """Set if lighting should be disabled or not."""

    def TextureSet(self, theCtx: OpenGl_Context | None, theToHighlight: bool = False) -> OpenGl_TextureSet:
        """Returns textures map."""

    def ShaderProgramRes(self, theCtx: OpenGl_Context | None) -> OpenGl_ShaderProgram:
        """
        Init and return OpenGl shader program resource.
        @return shader program resource.
        """

    def MarkerSize(self) -> float:
        """@return marker size"""

    def HasPointSprite(self, theCtx: OpenGl_Context | None) -> bool:
        """Return TRUE if OpenGl point sprite resource defines texture."""

    def IsDisplayListSprite(self, theCtx: OpenGl_Context | None) -> bool:
        """
        Return TRUE if OpenGl point sprite resource defined by obsolete Display List (bitmap).
        """

    def SpriteRes(self, theCtx: OpenGl_Context | None, theIsAlphaSprite: bool) -> OpenGl_PointSprite:
        """
        Init and return OpenGl point sprite resource.
        @return point sprite texture.
        """

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None: ...

    def Release(self, theContext: OpenGl_Context) -> None: ...

    def SynchronizeAspects(self) -> None:
        """Update presentation aspects parameters after their modification."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_Resource(nanoocp.Standard.Standard_Transient):
    """
    Interface for OpenGl resource with following meaning:
    - object can be constructed at any time;
    - should be explicitly Initialized within active OpenGL context;
    - should be explicitly Released    within active OpenGL context (virtual Release() method);
    - can be destroyed at any time.
    Destruction of object with unreleased GPU resources will cause leaks
    which will be ignored in release mode and will immediately stop program execution in debug mode
    using assert.
    """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """
        Release GPU resources.
        Notice that implementation should be SAFE for several consecutive calls
        (thus should invalidate internal structures / ids to avoid multiple-free errors).
        @param theGlCtx - bound GL context, shouldn't be NULL.
        """

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_Buffer(OpenGl_Resource):
    """
    Buffer Object - is a general storage object for arbitrary data (see sub-classes).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def FormatTarget(theTarget: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format VBO target enumeration value."""

    def GetTarget(self) -> int:
        """Return buffer target."""

    def IsVirtual(self) -> bool:
        """
        Return TRUE if this is a virtual (for backward compatibility) VBO object.
        """

    def IsValid(self) -> bool:
        """@return true if current object was initialized"""

    def GetComponentsNb(self) -> int:
        """@return the number of components per generic vertex attribute."""

    def GetElemsNb(self) -> int:
        """
        @return number of vertex attributes / number of vertices specified within ::Init()
        """

    def SetElemsNb(self, theNbElems: int) -> None:
        """
        Overrides the number of vertex attributes / number of vertexes.
        It is up to user specifying this number correct (e.g. below initial value)!
        """

    def GetDataType(self) -> int:
        """@return data type of each component in the array."""

    def Create(self, theGlCtx: OpenGl_Context | None) -> bool:
        """
        Creates buffer object name (id) if not yet generated.
        Data should be initialized by another method.
        """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any."""

    def Bind(self, theGlCtx: OpenGl_Context | None) -> None:
        """Bind this buffer object."""

    def Unbind(self, theGlCtx: OpenGl_Context | None) -> None:
        """Unbind this buffer object."""

    def EstimatedDataSize(self) -> int:
        """
        @name advanced methods
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    @staticmethod
    def sizeOfGlType(theType: int) -> int:
        """@return size of specified GL type"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_FrameStats(nanoocp.Graphic3d.Graphic3d_FrameStats):
    """Class storing the frame statistics."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: OpenGl_FrameStats) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsFrameUpdated(self) -> tuple[bool, OpenGl_FrameStats]:
        """
        Copy stats values into another instance (create new instance, if not exists).
        The main use of this method is to track changes in statistics (e.g. in conjunction with
        IsEqual() method).
        @return TRUE if frame data has been changed so that the presentation should be updated
        """

class OpenGl_GlCore11Fwd:
    """
    OpenGL 1.1 core without deprecated Fixed Pipeline entry points.
    Notice that all functions within this structure are actually exported by system GL library.
    The main purpose for these hint - to control visibility of functions per GL version
    (global functions should not be used directly to achieve this effect!).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore11Fwd) -> None: ...

class OpenGl_GlCore11:
    """
    OpenGL 1.1 core.
    Notice that all functions within this structure are actually exported by system GL library.
    The main purpose for these hint - to control visibility of functions per GL version
    (global functions should not be used directly to achieve this effect!).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore11) -> None: ...

class OpenGl_GlCore12(OpenGl_GlCore11Fwd):
    """OpenGL 1.2 core based on 1.1 version."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore12) -> None: ...

class OpenGl_GlCore13(OpenGl_GlCore12):
    """OpenGL 1.3 without deprecated entry points."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore13) -> None: ...

class OpenGl_TextureFormat:
    """Stores parameters of OpenGL texture format."""

    @overload
    def __init__(self) -> None:
        """Empty constructor (invalid texture format)."""

    @overload
    def __init__(self, theOther: OpenGl_TextureFormat) -> None: ...

    @staticmethod
    def FindFormat(theCtx: OpenGl_Context | None, theFormat: nanoocp.Image.Image_Format, theIsColorMap: bool) -> OpenGl_TextureFormat:
        """
        Find texture format suitable to specified image format.
        @param[in] theCtx  OpenGL context defining supported texture formats
        @param[in] theFormat  image format
        @param[in] theIsColorMap  flag indicating color nature of image (to select sRGB texture)
        @return found format or invalid format
        """

    @staticmethod
    def FindSizedFormat(theCtx: OpenGl_Context | None, theSizedFormat: int) -> OpenGl_TextureFormat:
        """
        Find texture format suitable to specified internal (sized) texture format.
        @param[in] theCtx  OpenGL context defining supported texture formats
        @param[in] theSizedFormat  sized (internal) texture format (example: GL_RGBA8)
        @return found format or invalid format
        """

    @staticmethod
    def FindCompressedFormat(theCtx: OpenGl_Context | None, theFormat: nanoocp.Image.Image_CompressedFormat, theIsColorMap: bool) -> OpenGl_TextureFormat:
        """
        Find texture format suitable to specified compressed texture format.
        @param[in] theCtx  OpenGL context defining supported texture formats
        @param[in] theFormat  compressed texture format
        @return found format or invalid format
        """

    @staticmethod
    def FormatFormat(theInternalFormat: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format pixel format enumeration."""

    @staticmethod
    def FormatDataType(theDataType: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format data type enumeration."""

    def IsValid(self) -> bool:
        """Return TRUE if format is defined."""

    def InternalFormat(self) -> int:
        """Returns OpenGL internal format of the pixel data (example: GL_R32F)."""

    def SetInternalFormat(self, theInternal: int) -> None:
        """Sets texture internal format."""

    def PixelFormat(self) -> int:
        """Returns OpenGL format of the pixel data (example: GL_RED)."""

    def SetPixelFormat(self, theFormat: int) -> None:
        """Sets OpenGL format of the pixel data."""

    def DataType(self) -> int:
        """Returns OpenGL data type of the pixel data (example: GL_FLOAT)."""

    def SetDataType(self, theType: int) -> None:
        """Sets OpenGL data type of the pixel data."""

    def NbComponents(self) -> int:
        """Returns number of components (channels). Here for debugging purposes."""

    def SetNbComponents(self, theNbComponents: int) -> None:
        """Sets number of components (channels)."""

    def IsSRGB(self) -> bool:
        """Return TRUE if internal texture format is sRGB(A)."""

    def ImageFormat(self) -> nanoocp.Image.Image_Format:
        """
        Returns image format (best match or Image_Format_UNKNOWN if no suitable fit).
        """

    def SetImageFormat(self, theFormat: nanoocp.Image.Image_Format) -> None:
        """Sets image format."""

    def Internal(self) -> int:
        """Returns OpenGL internal format of the pixel data (example: GL_R32F)."""

    def Format(self) -> int:
        """Returns OpenGL format of the pixel data (example: GL_RED)."""

class OpenGl_TextureFormatSelector__unsigned_char:
    """Specialization for unsigned byte."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__unsigned_char) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__unsigned_short:
    """Specialization for unsigned short."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__unsigned_short) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__float:
    """Specialization for float."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__float) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__unsigned_int:
    """Specialization for unsigned int."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__unsigned_int) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__signed_char:
    """Specialization for signed byte."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__signed_char) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__short:
    """Specialization for signed short."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__short) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_TextureFormatSelector__int:
    """Specialization for signed int."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_TextureFormatSelector__int) -> None: ...

    @staticmethod
    def DataType() -> int: ...

    @staticmethod
    def Internal(theChannels: int) -> int: ...

class OpenGl_NamedResource(OpenGl_Resource):
    """Named resource object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ResourceId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return resource name."""

class OpenGl_Sampler(OpenGl_Resource):
    """
    Class implements OpenGL sampler object resource that
    stores the sampling parameters for a texture access.
    """

    def __init__(self, theParams: nanoocp.Graphic3d.Graphic3d_TextureParams | None) -> None:
        """Creates new sampler object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self, theContext: OpenGl_Context) -> None:
        """Destroys object - will release GPU memory if any."""

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage - not implemented."""

    def Create(self, theContext: OpenGl_Context | None) -> bool:
        """Creates an uninitialized sampler object."""

    def Init(self, theContext: OpenGl_Context | None, theTexture: OpenGl_Texture) -> bool:
        """
        Creates and initializes sampler object.
        Existing object will be reused if possible, however if existing Sampler Object has Immutable
        flag and texture parameters should be re-initialized, then Sampler Object will be recreated.
        """

    def IsValid(self) -> bool:
        """Returns true if current object was initialized."""

    @overload
    def Bind(self, theCtx: OpenGl_Context | None) -> None:
        """Binds sampler object to texture unit specified in parameters."""

    @overload
    def Bind(self, theCtx: OpenGl_Context | None, theUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """Binds sampler object to the given texture unit."""

    @overload
    def Unbind(self, theCtx: OpenGl_Context | None) -> None:
        """Unbinds sampler object from texture unit specified in parameters."""

    @overload
    def Unbind(self, theCtx: OpenGl_Context | None, theUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """Unbinds sampler object from the given texture unit."""

    def SetParameter(self, theCtx: OpenGl_Context | None, theTarget: int, theParam: int, theValue: int) -> None:
        """Sets specific sampler parameter."""

    def SamplerID(self) -> int:
        """Returns OpenGL sampler ID."""

    def IsImmutable(self) -> bool:
        """
        Return immutable flag preventing further modifications of sampler parameters, FALSE by
        default. Immutable flag might be set when Sampler Object is used within Bindless Texture.
        """

    def SetImmutable(self) -> None:
        """
        Setup immutable flag. It is not possible unsetting this flag without Sampler destruction.
        """

    def Parameters(self) -> nanoocp.Graphic3d.Graphic3d_TextureParams:
        """Returns texture parameters."""

    def SetParameters(self, theParams: nanoocp.Graphic3d.Graphic3d_TextureParams | None) -> None:
        """Sets texture parameters."""

    def ToUpdateParameters(self) -> bool:
        """Returns texture parameters initialization state."""

class OpenGl_Texture(OpenGl_NamedResource):
    """Texture resource."""

    @overload
    def __init__(self, theResourceId: nanoocp.TCollection.TCollection_AsciiString = ..., theParams: nanoocp.Graphic3d.Graphic3d_TextureParams | None = None) -> None:
        """Create uninitialized texture."""

    @overload
    def __init__(self, theFrom: OpenGl_TextureSet.TextureSlot) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def PixelSizeOfPixelFormat(theInternalFormat: int) -> int:
        """
        Return pixel size of pixel format in bytes.
        Note that this method considers that OpenGL natively supports this pixel format,
        which might be not the case - in the latter case, actual pixel size might differ!
        """

    def IsValid(self) -> bool:
        """@return true if current object was initialized"""

    def GetTarget(self) -> int:
        """
        @return target to which the texture is bound (GL_TEXTURE_1D, GL_TEXTURE_2D)
        """

    def Size(self) -> nanoocp.BVH.BVH_Vec3i:
        """Return texture dimensions (0 LOD)"""

    def SizeX(self) -> int:
        """Return texture width (0 LOD)"""

    def SizeY(self) -> int:
        """Return texture height (0 LOD)"""

    def SizeZ(self) -> int:
        """Return texture depth (0 LOD)"""

    def TextureId(self) -> int:
        """@return texture ID"""

    def GetFormat(self) -> int:
        """@return texture format (not sized)"""

    def SizedFormat(self) -> int:
        """@return texture format (sized)"""

    def IsAlpha(self) -> bool:
        """Return true for GL_RED and GL_ALPHA formats."""

    def SetAlpha(self, theValue: bool) -> None:
        """
        Setup to interpret the format as Alpha by Shader Manager
        (should be GL_ALPHA within compatible context or GL_RED otherwise).
        """

    def IsTopDown(self) -> bool:
        """
        Return if 2D surface is defined top-down (TRUE) or bottom-up (FALSE).
        Normally set from Image_PixMap::IsTopDown() within texture initialization.
        """

    def SetTopDown(self, theIsTopDown: bool) -> None:
        """Set if 2D surface is defined top-down (TRUE) or bottom-up (FALSE)."""

    def Create(self, theCtx: OpenGl_Context | None) -> bool:
        """
        Creates Texture id if not yet generated.
        Data should be initialized by another method.
        """

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any."""

    def Sampler(self) -> OpenGl_Sampler:
        """Return texture sampler."""

    def SetSampler(self, theSampler: OpenGl_Sampler | None) -> None:
        """Set texture sampler."""

    def InitSamplerObject(self, theCtx: OpenGl_Context | None) -> bool:
        """
        Initialize the Sampler Object (as OpenGL object).
        @param theCtx currently bound OpenGL context
        """

    @overload
    def Bind(self, theCtx: OpenGl_Context | None) -> None:
        """
        Bind this Texture to the unit specified in sampler parameters.
        Also binds Sampler Object if it is allocated.
        """

    @overload
    def Bind(self, theCtx: OpenGl_Context | None, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """
        Bind this Texture to specified unit.
        Also binds Sampler Object if it is allocated.
        """

    @overload
    def Unbind(self, theCtx: OpenGl_Context | None) -> None:
        """
        Unbind texture from the unit specified in sampler parameters.
        Also unbinds Sampler Object if it is allocated.
        """

    @overload
    def Unbind(self, theCtx: OpenGl_Context | None, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """
        Unbind texture from specified unit.
        Also unbinds Sampler Object if it is allocated.
        """

    def Revision(self) -> int:
        """Revision of associated data source."""

    def SetRevision(self, theRevision: int) -> None:
        """Set revision of associated data source."""

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theImage: nanoocp.Image.Image_PixMap, theType: nanoocp.Graphic3d.Graphic3d_TypeOfTexture, theIsColorMap: bool) -> bool:
        """Notice that texture will be unbound after this call."""

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theFormat: OpenGl_TextureFormat, theSizeXYZ: nanoocp.BVH.BVH_Vec3i, theType: nanoocp.Graphic3d.Graphic3d_TypeOfTexture, theImage: nanoocp.Image.Image_PixMap = None) -> bool:
        """
        Initialize the texture with specified format, size and texture type.
        If theImage is empty the texture data will contain trash.
        Notice that texture will be unbound after this call.
        """

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theFormat: OpenGl_TextureFormat, theSizeXY: nanoocp.BVH.BVH_Vec2i, theType: nanoocp.Graphic3d.Graphic3d_TypeOfTexture, theImage: nanoocp.Image.Image_PixMap = None) -> bool:
        """
        Initialize the 2D texture with specified format, size and texture type.
        If theImage is empty the texture data will contain trash.
        Notice that texture will be unbound after this call.
        """

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theTextureMap: nanoocp.Graphic3d.Graphic3d_TextureRoot | None) -> bool:
        """
        Initialize the texture with Graphic3d_TextureMap.
        It is an universal way to initialize.
        Suitable initialization method will be chosen.
        """

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theTextFormat: int, thePixelFormat: int, theDataType: int, theSizeX: int, theSizeY: int, theType: nanoocp.Graphic3d.Graphic3d_TypeOfTexture, theImage: nanoocp.Image.Image_PixMap = None) -> bool:
        """
        Deprecated in OCCT: Deprecated method, OpenGl_TextureFormat should be passed instead of separate parameters
        """

    @overload
    def Init(self, theCtx: OpenGl_Context | None, theImage: nanoocp.Image.Image_PixMap, theType: nanoocp.Graphic3d.Graphic3d_TypeOfTexture) -> bool:
        """
        Deprecated in OCCT: Deprecated method, theIsColorMap parameter should be explicitly specified
        """

    def GenerateMipmaps(self, theCtx: OpenGl_Context | None) -> bool:
        """Generate mipmaps."""

    def InitCompressed(self, theCtx: OpenGl_Context | None, theImage: nanoocp.Image.Image_CompressedPixMap, theIsColorMap: bool) -> bool:
        """Initialize the texture with Image_CompressedPixMap."""

    def Init2DMultisample(self, theCtx: OpenGl_Context | None, theNbSamples: int, theTextFormat: int, theSizeX: int, theSizeY: int) -> bool:
        """
        Initialize the 2D multisampling texture using glTexImage2DMultisample().
        """

    def InitRectangle(self, theCtx: OpenGl_Context | None, theSizeX: int, theSizeY: int, theFormat: OpenGl_TextureFormat) -> bool:
        """
        Allocates texture rectangle with specified format and size.
        \\note Texture data is not initialized (will contain trash).
        """

    def HasMipmaps(self) -> bool:
        """@return true if texture was generated within mipmaps"""

    def MaxMipmapLevel(self) -> int:
        """Return upper mipmap level index (0 means no mipmaps)."""

    def NbSamples(self) -> int:
        """Return number of MSAA samples."""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def IsPointSprite(self) -> bool:
        """Returns TRUE for point sprite texture."""

    def ImageDump(self, theImage: nanoocp.Image.Image_PixMap, theCtx: OpenGl_Context | None, theTexUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit, theLevel: int = 0, theCubeSide: int = 0) -> bool:
        """
        Auxiliary method for making an image dump from texture data.
        @param[out] theImage    result image data (will be overridden)
        @param[in] theCtx       active GL context
        @param[in] theTexUnit   texture slot to use
        @param[in] theLevel     mipmap level to dump
        @param[in] theCubeSide  cubemap side to dump within [0, 5] range
        @return FALSE on error
        """

    @overload
    @staticmethod
    def GetDataFormat(theCtx: OpenGl_Context | None, theFormat: nanoocp.Image.Image_Format) -> tuple[bool, int, int, int]: ...

    @overload
    @staticmethod
    def GetDataFormat(theCtx: OpenGl_Context | None, theData: nanoocp.Image.Image_PixMap) -> tuple[bool, int, int, int]:
        """
        Deprecated in OCCT: Deprecated method, OpenGl_TextureFormat::FindFormat() should be used instead
        """

    def InitCubeMap(self, theCtx: OpenGl_Context | None, theCubeMap: nanoocp.Graphic3d.Graphic3d_CubeMap | None, theSize: int, theFormat: nanoocp.Image.Image_Format, theToGenMipmap: bool, theIsColorMap: bool) -> bool:
        """
        Initializes 6 sides of cubemap.
        If theCubeMap is not NULL then size and format will be taken from it and corresponding
        arguments will be ignored. Otherwise this parameters will be taken from arguments.
        @param[in] theCtx          active OpenGL context
        @param[in] theCubeMap      cubemap definition, can be NULL
        @param[in] theSize         cubemap dimensions
        @param[in] theFormat       image format
        @param[in] theToGenMipmap  flag to generate mipmaped cubemap
        @param[in] theIsColorMap   flag indicating cubemap storing color values
        """

class OpenGl_VectorType__double:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_VectorType__double) -> None: ...

class OpenGl_VectorType__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_VectorType__float) -> None: ...

class OpenGl_MatrixType__double:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_MatrixType__double) -> None: ...

class OpenGl_MatrixType__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_MatrixType__float) -> None: ...

class OpenGl_Font(OpenGl_Resource):
    """Texture font."""

    def __init__(self, theFont: nanoocp.Font.Font_FTFont | None, theKey: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Main constructor."""

    class Tile:
        """Simple structure stores tile rectangle."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: OpenGl_Font.Tile) -> None: ...

        @property
        def uv(self) -> nanoocp.Font.Font_Rect:
            """UV coordinates in texture"""

        @uv.setter
        def uv(self, arg: nanoocp.Font.Font_Rect, /) -> None: ...

        @property
        def px(self) -> nanoocp.Font.Font_Rect:
            """pixel displacement coordinates"""

        @px.setter
        def px(self, arg: nanoocp.Font.Font_Rect, /) -> None: ...

        @property
        def texture(self) -> int:
            """GL texture ID"""

        @texture.setter
        def texture(self, arg: int, /) -> None: ...

    class RectI:
        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: OpenGl_Font.RectI) -> None: ...

        @property
        def Left(self) -> int: ...

        @Left.setter
        def Left(self, arg: int, /) -> None: ...

        @property
        def Right(self) -> int: ...

        @Right.setter
        def Right(self, arg: int, /) -> None: ...

        @property
        def Top(self) -> int: ...

        @Top.setter
        def Top(self, arg: int, /) -> None: ...

        @property
        def Bottom(self) -> int: ...

        @Bottom.setter
        def Bottom(self, arg: int, /) -> None: ...

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any"""

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage."""

    def ResourceKey(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return key of shared resource"""

    def FTFont(self) -> nanoocp.Font.Font_FTFont:
        """@return FreeType font instance specified on construction."""

    def IsValid(self) -> bool:
        """@return true if font was loaded successfully."""

    def WasInitialized(self) -> bool:
        """
        Notice that this method doesn't return initialization success state.
        Use IsValid() instead.
        @return true if initialization was already called.
        """

    def Init(self, theCtx: OpenGl_Context | None) -> bool:
        """
        Initialize GL resources.
        FreeType font instance should be already initialized!
        """

    def Ascender(self) -> float:
        """
        @return vertical distance from the horizontal baseline to the highest character coordinate
        """

    def Descender(self) -> float:
        """
        @return vertical distance from the horizontal baseline to the lowest character coordinate
        """

    def RenderGlyph(self, theCtx: OpenGl_Context | None, theUChar: str, theGlyph: OpenGl_Font.Tile) -> bool:
        """
        Render glyph to texture if not already.
        @param theCtx       active context
        @param theUChar     unicode symbol to render
        @param theGlyph     computed glyph position rectangle, texture ID and UV coordinates
        """

    def Texture(self) -> OpenGl_Texture:
        """@return first texture."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_VertexBuffer(OpenGl_Buffer):
    """
    Vertex Buffer Object - is a general storage object for vertex attributes (position, normal,
    color). Notice that you should use OpenGl_IndexBuffer specialization for array of indices.
    """

    def __init__(self) -> None:
        """Create uninitialized VBO."""

    def GetTarget(self) -> int:
        """Return buffer target GL_ARRAY_BUFFER."""

    def BindVertexAttrib(self, theGlCtx: OpenGl_Context | None, theAttribLoc: int) -> None:
        """Bind this VBO to active GLSL program."""

    def UnbindVertexAttrib(self, theGlCtx: OpenGl_Context | None, theAttribLoc: int) -> None:
        """Unbind any VBO from active GLSL program."""

    def BindAttribute(self, theCtx: OpenGl_Context | None, theMode: nanoocp.Graphic3d.Graphic3d_TypeOfAttribute) -> None:
        """
        Bind this VBO and enable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        @param theGlCtx - handle to bound GL context;
        @param theMode  - array mode (GL_VERTEX_ARRAY, GL_NORMAL_ARRAY, GL_COLOR_ARRAY,
        GL_INDEX_ARRAY, GL_TEXTURE_COORD_ARRAY).
        """

    def UnbindAttribute(self, theCtx: OpenGl_Context | None, theMode: nanoocp.Graphic3d.Graphic3d_TypeOfAttribute) -> None:
        """
        Unbind this VBO and disable specified attribute in OpenGl_Context::ActiveProgram() or FFP.
        @param theCtx handle to bound GL context
        @param theMode  array mode
        """

    @staticmethod
    def unbindAttribute(theGlCtx: OpenGl_Context | None, theMode: nanoocp.Graphic3d.Graphic3d_TypeOfAttribute) -> None:
        """
        Disable GLSL array pointer - either for active GLSL program OpenGl_Context::ActiveProgram()
        or for FFP using unbindFixed() when no program bound.
        """

    def HasColorAttribute(self) -> bool:
        """
        @name methods for interleaved attributes array
        @return true if buffer contains per-vertex color attribute
        """

    def HasNormalAttribute(self) -> bool:
        """@return true if buffer contains per-vertex normal attribute"""

    def BindAllAttributes(self, theGlCtx: OpenGl_Context | None) -> None:
        """
        Bind all vertex attributes to active program OpenGl_Context::ActiveProgram() or for FFP.
        Default implementation does nothing.
        """

    def BindPositionAttribute(self, theGlCtx: OpenGl_Context | None) -> None:
        """
        Bind vertex position attribute only. Default implementation does nothing.
        """

    def UnbindAllAttributes(self, theGlCtx: OpenGl_Context | None) -> None:
        """Unbind all vertex attributes. Default implementation does nothing."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_Caps(nanoocp.Standard.Standard_Transient):
    """
    Class to define graphic driver capabilities.
    Notice that these options will be ignored if particular functionality does not provided by GL
    driver
    """

    def __init__(self) -> None:
        """
        @name class methods
        Default constructor - initialize with most optimal values.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @property
    def sRGBDisable(self) -> bool:
        """Disables sRGB rendering (OFF by default)"""

    @sRGBDisable.setter
    def sRGBDisable(self, arg: bool, /) -> None: ...

    @property
    def compressedTexturesDisable(self) -> bool:
        """
        Disables uploading of compressed texture formats native to GPU (OFF by default)
        """

    @compressedTexturesDisable.setter
    def compressedTexturesDisable(self, arg: bool, /) -> None: ...

    @property
    def vboDisable(self) -> bool:
        """disallow VBO usage for debugging purposes (OFF by default)"""

    @vboDisable.setter
    def vboDisable(self, arg: bool, /) -> None: ...

    @property
    def pntSpritesDisable(self) -> bool:
        """
        flag permits Point Sprites usage, will significantly affect performance (OFF by default)
        """

    @pntSpritesDisable.setter
    def pntSpritesDisable(self, arg: bool, /) -> None: ...

    @property
    def keepArrayData(self) -> bool:
        """Disables freeing CPU memory after building VBOs (OFF by default)"""

    @keepArrayData.setter
    def keepArrayData(self, arg: bool, /) -> None: ...

    @property
    def ffpEnable(self) -> bool:
        """
        Enables FFP (fixed-function pipeline), do not use built-in GLSL programs (OFF by default)
        """

    @ffpEnable.setter
    def ffpEnable(self, arg: bool, /) -> None: ...

    @property
    def usePolygonMode(self) -> bool:
        """
        Enables Polygon Mode instead of built-in GLSL programs (OFF by default; unsupported on OpenGL ES)
        """

    @usePolygonMode.setter
    def usePolygonMode(self, arg: bool, /) -> None: ...

    @property
    def useSystemBuffer(self) -> bool:
        """
        Enables usage of system backbuffer for blitting (OFF by default on desktop OpenGL and ON on OpenGL ES for testing)
        """

    @useSystemBuffer.setter
    def useSystemBuffer(self, arg: bool, /) -> None: ...

    @property
    def swapInterval(self) -> int:
        """
        controls swap interval - 0 for VSync off and 1 for VSync on, 1 by default
        """

    @swapInterval.setter
    def swapInterval(self, arg: int, /) -> None: ...

    @property
    def useZeroToOneDepth(self) -> bool:
        """
        use [0, 1] depth range instead of [-1, 1] range, when possible (OFF by default)
        """

    @useZeroToOneDepth.setter
    def useZeroToOneDepth(self, arg: bool, /) -> None: ...

    @property
    def buffersNoSwap(self) -> bool:
        """
        @name context creation parameters

        Specify that driver should not swap back/front buffers at the end of frame.
        Useful when OCCT Viewer is integrated into existing OpenGL rendering pipeline as part,
        thus swapping part is performed outside.

        OFF by default.
        """

    @buffersNoSwap.setter
    def buffersNoSwap(self, arg: bool, /) -> None: ...

    @property
    def buffersOpaqueAlpha(self) -> bool:
        """
        Specify whether alpha component within color buffer should be written or not.
        With alpha write enabled, background is considered transparent by default
        and overridden by alpha value of last drawn object
        (e.g. it could be opaque or not in case of transparent material).
        With alpha writes disabled, color buffer will be kept opaque.

        ON by default.
        """

    @buffersOpaqueAlpha.setter
    def buffersOpaqueAlpha(self, arg: bool, /) -> None: ...

    @property
    def buffersDeepColor(self) -> bool:
        """
        Specify whether deep color format (10-bit per component / 30-bit RGB) should be used
        instead of  standard color format  (8-bit per component / 24-bit RGB) when available.
        Deep color provides higher accuracy within the same color range (sRGB)
        and doesn't enable wide color gamut / HDR support.
        Higher precision helps eliminating banding effect on smooth gradients.

        Effect of the flag will vary depending on platform:
        - used as a hint on systems with 24-bit RGB color defined as preferred pixels format
        but with 30-bit RGB color being activated systemwide (e.g. Windows);
        - ignored on systems with deep color defined as preferred pixel format (e.g. Linux / X11),
        deep 30-bit RGB color will be used regardless of the flag value;
        - ignored on configurations not supporting deep color (incompatible display / system / GPU /
        driver), standard 24-bit RGB color will be used instead.

        OFF by default.
        """

    @buffersDeepColor.setter
    def buffersDeepColor(self, arg: bool, /) -> None: ...

    @property
    def contextStereo(self) -> bool:
        """
        Request stereoscopic context (with Quad Buffer). This flag requires support in OpenGL driver.

        OFF by default.
        """

    @contextStereo.setter
    def contextStereo(self, arg: bool, /) -> None: ...

    @property
    def contextDebug(self) -> bool:
        """
        Request debug GL context. This flag requires support in OpenGL driver.

        When turned on OpenGL driver emits error and warning messages to provided callback
        (see OpenGl_Context - messages will be printed to standard output).
        Affects performance - thus should not be turned on by products in released state.

        OFF by default.
        """

    @contextDebug.setter
    def contextDebug(self, arg: bool, /) -> None: ...

    @property
    def contextSyncDebug(self) -> bool:
        """
        Request debug GL context to emit messages within main thread (when contextDebug is specified!).

        Some implementations performs GL rendering within dedicated thread(s),
        in this case debug messages will be pushed from unknown thread making call stack useless,
        since it does not interconnected to application calls.
        This option asks GL driver to switch into synchronized implementation.
        Affects performance - thus should not be turned on by products in released state.

        OFF by default.
        """

    @contextSyncDebug.setter
    def contextSyncDebug(self, arg: bool, /) -> None: ...

    @property
    def contextNoAccel(self) -> bool:
        """
        Disable hardware acceleration.

        This flag overrides default behavior, when accelerated context always preferred over software
        ones:
        - on Windows will force Microsoft software implementation;
        - on Mac OS X, forces Apple software implementation.

        Software implementations are dramatically slower - should never be used.

        OFF by default. Currently implemented only for Windows (WGL) and Mac OS X (Cocoa).
        """

    @contextNoAccel.setter
    def contextNoAccel(self, arg: bool, /) -> None: ...

    @property
    def contextCompatible(self) -> bool:
        """
        Request backward-compatible GL context. This flag requires support in OpenGL driver.

        Backward-compatible profile includes deprecated functionality like FFP (fixed-function
        pipeline), and might be useful for compatibility with application OpenGL code.

        Most drivers support all features within backward-compatibility profile,
        but some limit functionality to OpenGL 2.1 (e.g. OS X) when core profile is not explicitly
        requested.

        Requires OpenGL 3.2+ drivers.
        Has no effect on OpenGL ES 2.0+ drivers (which do not provide FFP compatibility).
        Interacts with ffpEnable option, which should be disabled within core profile.

        ON by default.
        """

    @contextCompatible.setter
    def contextCompatible(self, arg: bool, /) -> None: ...

    @property
    def contextNoExtensions(self) -> bool:
        """
        Disallow using OpenGL extensions.
        Should be used for debugging purposes only!

        OFF by default.
        """

    @contextNoExtensions.setter
    def contextNoExtensions(self, arg: bool, /) -> None: ...

    @property
    def contextMajorVersionUpper(self) -> int:
        """
        Synthetically restrict upper version of OpenGL functionality to be used.
        Should be used for debugging purposes only!

        (-1, -1) by default, which means no restriction.
        """

    @contextMajorVersionUpper.setter
    def contextMajorVersionUpper(self, arg: int, /) -> None: ...

    @property
    def contextMinorVersionUpper(self) -> int: ...

    @contextMinorVersionUpper.setter
    def contextMinorVersionUpper(self, arg: int, /) -> None: ...

    @property
    def isTopDownTextureUV(self) -> bool:
        """
        Define if 2D texture UV coordinates are defined top-down or bottom-up. FALSE by default.

        Proper rendering requires image texture uploading and UV texture coordinates being consistent,
        otherwise texture mapping might appear vertically flipped.
        Historically, OCCT used image library loading images bottom-up,
        so that applications have to generate UV accordingly (flip V when necessary, V' = 1.0 - V).

        Graphic driver now compares this flag with image layout reported by Image_PixMap::IsTopDown(),
        and in case of mismatch applies implicit texture coordinates conversion in GLSL program.
        """

    @isTopDownTextureUV.setter
    def isTopDownTextureUV(self, arg: bool, /) -> None: ...

    @property
    def glslWarnings(self) -> bool:
        """
        @name flags to activate verbose output
        Print GLSL program compilation/linkage warnings, if any. OFF by default.
        """

    @glslWarnings.setter
    def glslWarnings(self, arg: bool, /) -> None: ...

    @property
    def suppressExtraMsg(self) -> bool:
        """Suppress redundant messages from debug GL context. ON by default."""

    @suppressExtraMsg.setter
    def suppressExtraMsg(self, arg: bool, /) -> None: ...

    @property
    def glslDumpLevel(self) -> OpenGl_ShaderProgramDumpLevel:
        """Print GLSL program source code. OFF by default."""

    @glslDumpLevel.setter
    def glslDumpLevel(self, arg: OpenGl_ShaderProgramDumpLevel, /) -> None: ...

class OpenGl_LineAttributes(OpenGl_Resource):
    """
    Utility class to manage OpenGL resources of polygon hatching styles.
    @note the implementation is not supported by Core Profile and by ES version.
    """

    def __init__(self) -> None:
        """Default constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Release GL resources."""

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage - not implemented."""

    def SetTypeOfHatch(self, theGlCtx: OpenGl_Context, theStyle: nanoocp.Graphic3d.Graphic3d_HatchStyle | None) -> bool:
        """Sets type of the hatch."""

class OpenGl_MaterialCommon:
    """OpenGL material definition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_MaterialCommon) -> None: ...

    def Shine(self) -> float: ...

    def ChangeShine(self) -> float: ...

    def SetShine(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeShine() returns by reference in C++.
        """

    def SetColor(self, theColor: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Set material color."""

    @property
    def Diffuse(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """diffuse RGB coefficients + alpha"""

    @Diffuse.setter
    def Diffuse(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Emission(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """material RGB emission"""

    @Emission.setter
    def Emission(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def SpecularShininess(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """glossy  RGB coefficients + shininess"""

    @SpecularShininess.setter
    def SpecularShininess(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Ambient(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """ambient RGB coefficients"""

    @Ambient.setter
    def Ambient(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

class OpenGl_MaterialPBR:
    """OpenGL material definition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_MaterialPBR) -> None: ...

    def Metallic(self) -> float: ...

    def ChangeMetallic(self) -> float: ...

    def SetMetallic(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeMetallic() returns by reference in C++.
        """

    def Roughness(self) -> float: ...

    def ChangeRoughness(self) -> float: ...

    def SetRoughness(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeRoughness() returns by reference in C++.
        """

    def SetColor(self, theColor: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Set material color."""

    @property
    def BaseColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """base color of PBR material with alpha component"""

    @BaseColor.setter
    def BaseColor(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def EmissionIOR(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        light intensity which is emitted by PBR material and index of refraction
        """

    @EmissionIOR.setter
    def EmissionIOR(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Params(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """extra packed parameters"""

    @Params.setter
    def Params(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

class OpenGl_Material:
    """OpenGL material definition"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_Material) -> None: ...

    def SetColor(self, theColor: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Set material color."""

    def Init(self, theCtx: OpenGl_Context, theFront: nanoocp.Graphic3d.Graphic3d_MaterialAspect, theFrontColor: nanoocp.Quantity.Quantity_Color, theBack: nanoocp.Graphic3d.Graphic3d_MaterialAspect, theBackColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Initialize material"""

    def IsEqual(self, theOther: OpenGl_Material) -> bool:
        """
        Check this material for equality with another material (without tolerance!).
        """

    def __eq__(self, theOther: OpenGl_Material) -> bool:
        """
        Check this material for equality with another material (without tolerance!).
        """

    def __ne__(self, theOther: OpenGl_Material) -> bool:
        """
        Check this material for non-equality with another material (without tolerance!).
        """

    def PackedCommon(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Returns packed (serialized) representation of common material properties
        """

    @staticmethod
    def NbOfVec4Common() -> int: ...

    def PackedPbr(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns packed (serialized) representation of PBR material properties"""

    @staticmethod
    def NbOfVec4Pbr() -> int: ...

    @property
    def Common(self) -> list[OpenGl_MaterialCommon]: ...

    @Common.setter
    def Common(self, arg: Sequence[OpenGl_MaterialCommon], /) -> None: ...

    @property
    def Pbr(self) -> list[OpenGl_MaterialPBR]: ...

    @Pbr.setter
    def Pbr(self, arg: Sequence[OpenGl_MaterialPBR], /) -> None: ...

class OpenGl_TextureSet(nanoocp.Standard.Standard_Transient):
    """
    Class holding array of textures to be mapped as a set.
    Textures should be defined in ascending order of texture units within the set.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theNbTextures: int) -> None:
        """Constructor."""

    @overload
    def __init__(self, theTexture: OpenGl_Texture | None) -> None:
        """Constructor for a single texture."""

    @overload
    def __init__(self, theOther: OpenGl_TextureSet) -> None: ...

    class TextureSlot:
        """Texture slot - combination of Texture and binding Unit."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: OpenGl_TextureSet.TextureSlot) -> None: ...

        @property
        def Texture(self) -> OpenGl_Texture: ...

        @Texture.setter
        def Texture(self, arg: OpenGl_Texture, /) -> None: ...

        @property
        def Unit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit: ...

        @Unit.setter
        def Unit(self, arg: nanoocp.Graphic3d.Graphic3d_TextureUnit, /) -> None: ...

    class Iterator(NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot):
        """Class for iterating texture set."""

        @overload
        def __init__(self) -> None:
            """Empty constructor."""

        @overload
        def __init__(self, theSet: OpenGl_TextureSet | None) -> None:
            """Constructor."""

        @overload
        def __init__(self, theOther: OpenGl_TextureSet.Iterator) -> None: ...

        def Value(self) -> OpenGl_Texture:
            """Access texture."""

        def ChangeValue(self) -> OpenGl_Texture: ...

        def Unit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
            """Access texture unit."""

        def ChangeUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit: ...

        def SetUnit(self, theValue: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
            """
            Python addition: sets the value ChangeUnit() returns by reference in C++.
            """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def TextureSetBits(self) -> int:
        """
        Return texture units declared within the program, @sa Graphic3d_TextureSetBits.
        """

    def ChangeTextureSetBits(self) -> int:
        """
        Return texture units declared within the program, @sa Graphic3d_TextureSetBits.
        """

    def SetTextureSetBits(self, theValue: int) -> None:
        """
        Python addition: sets the value ChangeTextureSetBits() returns by reference in C++.
        """

    def IsEmpty(self) -> bool:
        """Return TRUE if texture array is empty."""

    def Size(self) -> int:
        """Return number of textures."""

    def Lower(self) -> int:
        """Return the lower index in texture set."""

    def Upper(self) -> int:
        """Return the upper index in texture set."""

    def First(self) -> OpenGl_Texture:
        """Return the first texture."""

    def ChangeFirst(self) -> OpenGl_Texture:
        """Return the first texture."""

    def FirstUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """Return the first texture unit."""

    def Last(self) -> OpenGl_Texture:
        """Return the last texture."""

    def ChangeLast(self) -> OpenGl_Texture:
        """Return the last texture."""

    def LastUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """Return the last texture unit."""

    def ChangeLastUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """Return the last texture unit."""

    def SetLastUnit(self, theValue: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """
        Python addition: sets the value ChangeLastUnit() returns by reference in C++.
        """

    def Value(self, theIndex: int) -> OpenGl_Texture:
        """Return the texture at specified position within [0, Size()) range."""

    def ChangeValue(self, theIndex: int) -> OpenGl_Texture:
        """Return the texture at specified position within [0, Size()) range."""

    def IsModulate(self) -> bool:
        """
        Return TRUE if texture color modulation has been enabled for the first texture
        or if texture is not set at all.
        """

    def HasNonPointSprite(self) -> bool:
        """
        Return TRUE if other than point sprite textures are defined within point set.
        """

    def HasPointSprite(self) -> bool:
        """Return TRUE if last texture is a point sprite."""

    def InitZero(self) -> None:
        """Nullify all handles."""

class NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot:
    """
    Helper class that allows to use NCollection iterators as STL iterators.
    NCollection iterator can be extended to STL iterator of any category by
    adding necessary methods: STL forward iterator requires IsEqual method,
    STL bidirectional iterator requires Previous method, and STL random access
    iterator requires Offset and Differ methods. See NCollection_DynamicArray as
    example of declaring custom STL iterators.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.OpenGl.OpenGl_TextureSet.TextureSlot]) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.OpenGl.OpenGl_TextureSet.TextureSlot], theOther: "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<OpenGl_TextureSet::TextureSlot>, OpenGl_TextureSet::TextureSlot, false>") -> None: ...

    def __iter__(self) -> NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> OpenGl_TextureSet.TextureSlot:
        """Python addition: see __iter__."""

    def Init(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.OpenGl.OpenGl_TextureSet.TextureSlot]) -> None: ...

    def More(self) -> bool: ...

    def Initialize(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.OpenGl.OpenGl_TextureSet.TextureSlot]) -> None: ...

    def ValueIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<OpenGl_TextureSet::TextureSlot>, OpenGl_TextureSet::TextureSlot, false>": ...

    def ChangeValueIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<OpenGl_TextureSet::TextureSlot>, OpenGl_TextureSet::TextureSlot, false>": ...

    def EndIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<OpenGl_TextureSet::TextureSlot>, OpenGl_TextureSet::TextureSlot, false>": ...

    def ChangeEndIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<OpenGl_TextureSet::TextureSlot>, OpenGl_TextureSet::TextureSlot, false>": ...

    def Next(self) -> None: ...

    def Value(self) -> OpenGl_TextureSet.TextureSlot: ...

    def ChangeValue(self) -> OpenGl_TextureSet.TextureSlot: ...

    def __eq__(self, theOther: NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot) -> bool: ...

    def __ne__(self, theOther: NCollection_Iterator__NCollection_Array1__OpenGl_TextureSet_TextureSlot) -> bool: ...

class OpenGl_Clipping:
    """
    This class contains logics related to tracking and modification of clipping plane
    state for particular OpenGl context. It contains information about enabled
    clipping planes and provides method to change clippings in context. The methods
    should be executed within OpenGl context associated with instance of this
    class.
    """

    def __init__(self) -> None:
        """
        @name general methods
        Default constructor.
        """

    def Init(self) -> None:
        """Initialize."""

    def Reset(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None) -> None:
        """
        Setup list of global (for entire view) clipping planes
        and clears local plane list if it was not released before.
        """

    def SetLocalPlanes(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None) -> None:
        """Setup list of local (for current object) clipping planes."""

    def IsCappingOn(self) -> bool:
        """@return true if there are enabled capping planes"""

    def IsClippingOrCappingOn(self) -> bool:
        """@return true if there are enabled clipping or capping planes"""

    def NbClippingOrCappingOn(self) -> int:
        """@return number of enabled clipping + capping planes"""

    def HasClippingChains(self) -> bool:
        """
        Return TRUE if there are clipping chains in the list (defining more than 1 sub-plane)
        """

    def HasDisabled(self) -> bool:
        """
        @name advanced method for disabling defined planes
        Return true if some clipping planes have been temporarily disabled.
        """

    def SetEnabled(self, thePlane: OpenGl_ClippingIterator, theIsEnabled: bool) -> bool:
        """Disable plane temporarily."""

    def DisableGlobal(self) -> None:
        """
        Temporarily disable all planes from the global (view) list, keep only local (object) list.
        """

    def RestoreDisabled(self) -> None:
        """
        Restore all temporarily disabled planes.
        Does NOT affect constantly disabled planes Graphic3d_ClipPlane::IsOn().
        """

    def CappedChain(self) -> nanoocp.Graphic3d.Graphic3d_ClipPlane:
        """
        Chain which is either temporary disabled or the only one enabled for Capping algorithm.
        """

    def CappedSubPlane(self) -> int:
        """
        Sub-plane index within filtered Chain; positive number for DisableAllExcept and negative for
        EnableAllExcept.
        """

    def IsCappingFilterOn(self) -> bool:
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are temporarily
        disabled except currently processed one.
        """

    def IsCappingDisableAllExcept(self) -> bool:
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are temporarily
        disabled except currently processed one.
        """

    def IsCappingEnableAllExcept(self) -> bool:
        """
        Return TRUE if capping algorithm is in state, when all clipping planes are enabled except
        currently rendered one.
        """

    def DisableAllExcept(self, theChain: nanoocp.Graphic3d.Graphic3d_ClipPlane | None, theSubPlaneIndex: int) -> None:
        """
        Temporarily disable all planes except specified one for Capping algorithm.
        Does not affect already disabled planes.
        """

    def EnableAllExcept(self, theChain: nanoocp.Graphic3d.Graphic3d_ClipPlane | None, theSubPlaneIndex: int) -> None:
        """
        Enable back planes disabled by ::DisableAllExcept() for Capping algorithm.
        Keeps only specified plane enabled.
        """

    def ResetCappingFilter(self) -> None:
        """Resets chain filter for Capping algorithm."""

class OpenGl_Context(nanoocp.Standard.Standard_Transient):
    """
    This class generalize access to the GL context and available extensions.

    Functions related to specific OpenGL version or extension are grouped into structures which can
    be accessed as fields of this class. The most simple way to check that required functionality is
    available - is NULL check for the group:
    @code
    if (myContext->core20 != NULL)
    {
    myGlProgram = myContext->core20->glCreateProgram();
    .. do more stuff ..
    }
    else
    {
    .. compatibility with outdated configurations ..
    }
    @endcode

    Current implementation provide access to OpenGL core functionality up to 4.6 version (core12,
    core13, core14, etc.) as well as several extensions (arbTBO, arbFBO, etc.).

    OpenGL context might be initialized in Core Profile. In this case deprecated functionality
    become unavailable. To select which core** function set should be used in specific case:
    - Determine the minimal OpenGL version required for implemented functionality and use it to
    access all functions.
    For example, if algorithm requires OpenGL 2.1+, it is better to write core20fwd->glEnable()
    rather than core11fwd->glEnable() for uniformity.
    - Validate minimal requirements at initialization/creation time and omit checks within code
    where algorithm should be already initialized.
    Properly escape code incompatible with Core Profile. The simplest way to check Core Profile
    is "if (core11ffp == NULL)".

    Simplified extensions classification:
    - prefixed with NV, AMD, ATI are vendor-specific (however may be provided by other vendors in
    some cases);
    - prefixed with EXT are accepted by 2+ vendors;
    - prefixed with ARB are accepted by Architecture Review Board and are candidates
    for inclusion into GL core functionality.
    Some functionality can be represented in several extensions simultaneously.
    In this case developer should be careful because different specification may differ
    in aspects (like enumeration values and error-handling).

    Notice that some systems provide mechanisms to simultaneously incorporate with GL contexts with
    different capabilities. For this reason OpenGl_Context should be initialized and used for each
    GL context independently.

    Matrices of OpenGl transformations:
    model -> world -> view -> projection
    These matrices might be changed for local transformation, transform persistent using direct
    access to current matrix of ModelWorldState, WorldViewState and ProjectionState After, these
    matrices should be applied using ApplyModelWorldMatrix, ApplyWorldViewMatrix,
    ApplyModelViewMatrix or ApplyProjectionMatrix.
    """

    def __init__(self, theCaps: OpenGl_Caps | None = None) -> None:
        """
        Empty constructor. You should call Init() to perform initialization with bound GL context.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def GetPowerOfTwo(theNumber: int, theThreshold: int) -> int:
        """
        Function for getting power of to number larger or equal to input number.
        @param theNumber    number to 'power of two'
        @param theThreshold upper threshold
        @return power of two number
        """

    @staticmethod
    def FormatGlEnumHex(theGlEnum: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format GL constant as hex value 0xABCD."""

    @staticmethod
    def FormatSize(theSize: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format size value."""

    @staticmethod
    def FormatGlError(theGlError: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return text description of GL error."""

    def forcedRelease(self) -> None:
        """Release all resources, including shared ones"""

    def Share(self, theShareCtx: OpenGl_Context | None) -> None:
        """
        Share GL context resources.
        theShareCtx - handle to context to retrieve handles to shared resources.
        """

    def Init(self, theIsCoreProfile: bool = False) -> bool:
        """
        Initialize class from currently bound OpenGL context. Method should be called only once.
        @return false if no GL context is bound to the current thread
        """

    def IsValid(self) -> bool:
        """@return true if this context is valid (has been initialized)"""

    def Window(self) -> int:
        """
        Return window handle currently bound to this OpenGL context (EGLSurface | HWND | GLXDrawable).
        """

    @staticmethod
    def ReadGlVersion() -> tuple[int, int]:
        """Read OpenGL version information from active context."""

    def CheckExtension(self, theExtName: str) -> bool:
        """Check if theExtName extension is supported by active GL context."""

    @staticmethod
    def CheckExtension_s(theExtString: str, theExtName: str) -> bool:
        """Check if theExtName extension is in extensions string."""

    def GraphicsLibrary(self) -> nanoocp.Aspect.Aspect_GraphicsLibrary:
        """Return active graphics library."""

    def IsGlGreaterEqual(self, theVerMajor: int, theVerMinor: int) -> bool:
        """
        @return true if detected GL version is greater or equal to requested one.
        """

    def VersionMajor(self) -> int:
        """Return cached GL version major number."""

    def VersionMinor(self) -> int:
        """Return cached GL version minor number."""

    def Functions(self) -> OpenGl_GlFunctions:
        """Access entire map of loaded OpenGL functions."""

    def ResetErrors(self, theToPrintErrors: bool = False) -> bool:
        """
        Clean up errors stack for this GL context (glGetError() in loop).
        @return true if some error has been cleared
        """

    def IsCurrent(self) -> bool:
        """
        This method uses system-dependent API to retrieve information
        about GL context bound to the current thread.
        @return true if current thread is bound to this GL context
        """

    def MakeCurrent(self) -> bool:
        """
        Activates current context.
        Class should be initialized with appropriate info.
        """

    def SwapBuffers(self) -> None:
        """
        Swap front/back buffers for this GL context (should be activated before!).
        """

    def SetSwapInterval(self, theInterval: int) -> bool:
        """Setup swap interval (VSync)."""

    def IsRender(self) -> bool:
        """Return true if active mode is GL_RENDER (cached state)"""

    def IsFeedback(self) -> bool:
        """Return true if active mode is GL_FEEDBACK (cached state)"""

    def AvailableMemory(self) -> int:
        """
        This function retrieves information from GL about free GPU memory that is:
        - OS-dependent. On some OS it is per-process and on others - for entire system.
        - Vendor-dependent. Currently available only on NVIDIA and AMD/ATi drivers only.
        - Numbers meaning may vary.
        You should use this info only for diagnostics purposes.
        @return free GPU dedicated memory in bytes.
        """

    @overload
    def MemoryInfo(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        This function retrieves information from GL about GPU memory
        and contains more vendor-specific values than AvailableMemory().
        """

    @overload
    def MemoryInfo(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """This function retrieves information from GL about GPU memory."""

    def DiagnosticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theFlags: nanoocp.Graphic3d.Graphic3d_DiagnosticInfo) -> None:
        """
        Fill in the dictionary with OpenGL info.
        Should be called with bound context.
        """

    def WindowBufferBits(self, theColorBits: nanoocp.BVH.BVH_Vec4i, theDepthStencilBits: nanoocp.BVH.BVH_Vec2i) -> None:
        """Fetches information about window buffer pixel format."""

    def GetResource(self, theKey: nanoocp.TCollection.TCollection_AsciiString) -> OpenGl_Resource:
        """
        Access shared resource by its name.
        @param  theKey - unique identifier;
        @return handle to shared resource or NULL.
        """

    def ShareResource(self, theKey: nanoocp.TCollection.TCollection_AsciiString, theResource: OpenGl_Resource | None) -> bool:
        """
        Register shared resource.
        Notice that after registration caller shouldn't release it by himself -
        it will be automatically released on context destruction.
        @param theKey      - unique identifier, shouldn't be empty;
        @param theResource - new resource to register, shouldn't be NULL.
        """

    def ReleaseResource(self, theKey: nanoocp.TCollection.TCollection_AsciiString, theToDelay: bool = False) -> None:
        """
        Release shared resource.
        If there are more than one reference to this resource
        (also used by some other existing object) then call will be ignored.
        This means that current object itself should nullify handle before this call.
        Notice that this is unrecommended operation at all and should be used
        only in case of fat resources to release memory for other needs.
        @param theKey     unique identifier
        @param theToDelay postpone release until next redraw call
        """

    def ReleaseDelayed(self) -> None:
        """Clean up the delayed release queue."""

    def SharedResources(self) -> nanoocp.NCollection.NCollection_Shared[nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.OpenGl.OpenGl_Resource]]:
        """Return map of shared resources."""

    def ChangeClipping(self) -> OpenGl_Clipping:
        """@return tool for management of clippings within this context."""

    def Clipping(self) -> OpenGl_Clipping:
        """@return tool for management of clippings within this context."""

    def ShaderManager(self) -> OpenGl_ShaderManager:
        """@return tool for management of shader programs within this context."""

    def TextureWrapClamp(self) -> int:
        """Either GL_CLAMP_TO_EDGE (1.2+) or GL_CLAMP (1.1)."""

    def HasTextureBaseLevel(self) -> bool:
        """
        @return true if texture parameters GL_TEXTURE_BASE_LEVEL/GL_TEXTURE_MAX_LEVEL are supported.
        """

    def SupportedTextureFormats(self) -> nanoocp.Image.Image_SupportedFormats:
        """Return map of supported texture formats."""

    def MaxDegreeOfAnisotropy(self) -> int:
        """@return maximum degree of anisotropy texture filter"""

    def MaxTextureSize(self) -> int:
        """@return value for GL_MAX_TEXTURE_SIZE"""

    def MaxCombinedTextureUnits(self) -> int:
        """@return value for GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS"""

    def MaxTextureUnitsFFP(self) -> int:
        """
        This method returns the multi-texture limit for obsolete fixed-function pipeline.
        Use MaxCombinedTextureUnits() instead for limits for using programmable pipeline.
        @return value for GL_MAX_TEXTURE_UNITS
        """

    def SpriteTextureUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Return texture unit to be used for sprites (Graphic3d_TextureUnit_PointSprite by default).
        """

    def HasTextureMultisampling(self) -> bool:
        """@return true if MSAA textures are supported."""

    def MaxMsaaSamples(self) -> int:
        """@return value for GL_MAX_SAMPLES"""

    def MaxDumpSizeX(self) -> int:
        """@return maximum FBO width for image dump"""

    def MaxDumpSizeY(self) -> int:
        """@return maximum FBO height for image dump"""

    def MaxDrawBuffers(self) -> int:
        """@return value for GL_MAX_DRAW_BUFFERS"""

    def MaxColorAttachments(self) -> int:
        """@return value for GL_MAX_COLOR_ATTACHMENTS"""

    def MaxClipPlanes(self) -> int:
        """
        Get maximum number of clip planes supported by OpenGl.
        This value is implementation dependent. At least 6
        planes should be supported by OpenGl (see specs).
        @return value for GL_MAX_CLIP_PLANES
        """

    def HasRayTracing(self) -> bool:
        """@return TRUE if ray tracing mode is supported"""

    def HasRayTracingTextures(self) -> bool:
        """@return TRUE if textures in ray tracing mode are supported"""

    def HasRayTracingAdaptiveSampling(self) -> bool:
        """
        @return TRUE if adaptive screen sampling in ray tracing mode is supported
        """

    def HasRayTracingAdaptiveSamplingAtomic(self) -> bool:
        """
        @return TRUE if atomic adaptive screen sampling in ray tracing mode is supported
        """

    def HasSRGB(self) -> bool:
        """Returns TRUE if sRGB rendering is supported."""

    def ToRenderSRGB(self) -> bool:
        """Returns TRUE if sRGB rendering is supported and permitted."""

    def IsWindowSRGB(self) -> bool:
        """
        Returns TRUE if window/surface buffer is sRGB-ready.

        When offscreen FBOs are created in sRGB, but window is not sRGB-ready,
        blitting into window should be done with manual gamma correction.

        In desktop OpenGL, window buffer can be considered as sRGB-ready by default,
        even when application has NOT requested sRGB-ready pixel format,
        and rendering is managed via GL_FRAMEBUFFER_SRGB state.

        In OpenGL ES, sRGB-ready window surface should be explicitly requested on construction,
        and cannot be disabled/enabled without GL_EXT_sRGB_write_control extension afterwards
        (GL_FRAMEBUFFER_SRGB can be considered as always tuned ON).
        """

    def SetWindowSRGB(self, theIsSRgb: bool) -> None:
        """
        Overrides if window/surface buffer is sRGB-ready or not (initialized with the context).
        """

    def IsWindowDeepColor(self) -> bool:
        """
        Returns TRUE if window/surface buffer has deep color (10bit per component / 30bit RGB) or
        better precision.
        """

    def Vec4FromQuantityColor(self, theColor: nanoocp.Quantity.NCollection_Vec4__float) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Convert Quantity_ColorRGBA into vec4
        with conversion or no conversion into non-linear sRGB
        basing on ToRenderSRGB() flag.
        """

    def Vec4LinearFromQuantityColor(self, theColor: nanoocp.Quantity.NCollection_Vec4__float) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Convert Quantity_ColorRGBA into vec4.
        Quantity_Color is expected to be linear RGB, hence conversion is NOT required
        """

    def Vec4sRGBFromQuantityColor(self, theColor: nanoocp.Quantity.NCollection_Vec4__float) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Convert Quantity_ColorRGBA (linear RGB) into non-linear sRGB vec4."""

    def HasPBR(self) -> bool:
        """
        Returns TRUE if PBR shading model is supported.
        Basically, feature requires OpenGL 3.0+ / OpenGL ES 3.0+ hardware; more precisely:
        - Graphics hardware with moderate capabilities for compiling long enough GLSL program.
        - FBO (e.g. for baking environment).
        - Multi-texturing with >= 4 units (LUT and IBL textures).
        - GL_RG32F texture format (arbTexRG + arbTexFloat)
        - Cubemap texture lookup textureCubeLod()/textureLod() with LOD index within Fragment Shader,
        which requires GLSL OpenGL 3.0+ / OpenGL ES 3.0+ or OpenGL 2.1 + GL_EXT_gpu_shader4
        extension.
        """

    def PBREnvLUTTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit where Environment Lookup Table is expected to be bound, or 0 if PBR is
        unavailable.
        """

    def PBRDiffIBLMapSHTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit where Diffuse (irradiance) IBL map's spherical harmonics coefficients is
        expected to be bound, or 0 if PBR is unavailable.
        """

    def PBRSpecIBLMapTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit where Specular IBL map is expected to be bound, or 0 if PBR is
        unavailable.
        """

    def ShadowMapTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit where shadow map is expected to be bound, or 0 if unavailable.
        """

    def DepthPeelingDepthTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit for occDepthPeelingDepth within enabled Depth Peeling.
        """

    def DepthPeelingFrontColorTexUnit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """
        Returns texture unit for occDepthPeelingFrontColor within enabled Depth Peeling.
        """

    def ToUseVbo(self) -> bool:
        """Returns true if VBO is supported and permitted."""

    def IsGlNormalizeEnabled(self) -> bool:
        """@return cached state of GL_NORMALIZE."""

    def SetGlNormalizeEnabled(self, isEnabled: bool) -> bool:
        """
        Sets GL_NORMALIZE enabled or disabled.
        @return old value of the flag
        """

    def PolygonMode(self) -> int:
        """@return cached state of polygon rasterization mode (glPolygonMode())."""

    def SetPolygonMode(self, theMode: int) -> int:
        """
        Sets polygon rasterization mode (glPolygonMode() function).
        @return old value of the rasterization mode.
        """

    def IsPolygonHatchEnabled(self) -> bool:
        """@return cached enabled state of polygon hatching rasterization."""

    def SetPolygonHatchEnabled(self, theIsEnabled: bool) -> bool:
        """
        Sets enabled state of polygon hatching rasterization
        without affecting currently selected hatching pattern.
        @return previous state of polygon hatching mode.
        """

    def PolygonHatchStyle(self) -> int:
        """@return cached state of polygon hatch type."""

    def SetPolygonHatchStyle(self, theStyle: nanoocp.Graphic3d.Graphic3d_HatchStyle | None) -> int:
        """
        Sets polygon hatch pattern.
        Zero-index value is a default alias for solid filling.
        @param theStyle type of hatch supported by base implementation of
        OpenGl_LineAttributes (Aspect_HatchStyle) or the type supported by custom
        implementation derived from OpenGl_LineAttributes class.
        @return old type of hatch.
        """

    def SetPolygonOffset(self, theOffset: nanoocp.Graphic3d.Graphic3d_PolygonOffset) -> None:
        """Sets and applies current polygon offset."""

    def PolygonOffset(self) -> nanoocp.Graphic3d.Graphic3d_PolygonOffset:
        """Returns currently applied polygon offset parameters."""

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Returns camera object."""

    def SetCamera(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Sets camera object to the context and update matrices."""

    def ApplyModelWorldMatrix(self) -> None:
        """
        Applies matrix into shader manager stored in ModelWorldState to OpenGl.
        In "model -> world -> view -> projection" it performs:
        model -> world
        """

    def ApplyWorldViewMatrix(self) -> None:
        """
        Applies matrix stored in WorldViewState to OpenGl.
        In "model -> world -> view -> projection" it performs:
        model -> world -> view,
        where model -> world is identical matrix
        """

    def ApplyModelViewMatrix(self) -> None:
        """
        Applies combination of matrices stored in ModelWorldState and WorldViewState to OpenGl.
        In "model -> world -> view -> projection" it performs:
        model -> world -> view
        """

    def ApplyProjectionMatrix(self) -> None:
        """
        Applies matrix stored in ProjectionState to OpenGl.
        In "model -> world -> view -> projection" it performs:
        view -> projection
        """

    def Messenger(self) -> nanoocp.Message.Message_Messenger:
        """@return messenger instance"""

    def PushMessage(self, theSource: int, theType: int, theId: int, theSeverity: int, theMessage: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Callback for GL_ARB_debug_output extension
        @param theSource   message source   within GL_DEBUG_SOURCE_   enumeration
        @param theType     message type     within GL_DEBUG_TYPE_     enumeration
        @param theId       message ID       within source
        @param theSeverity message severity within GL_DEBUG_SEVERITY_ enumeration
        @param theMessage  the message itself
        """

    def ExcludeMessage(self, theSource: int, theId: int) -> bool:
        """Adds a filter for messages with theId and theSource (GL_DEBUG_SOURCE_)"""

    def IncludeMessage(self, theSource: int, theId: int) -> bool:
        """
        Removes a filter for messages with theId and theSource (GL_DEBUG_SOURCE_)
        """

    def HasStereoBuffers(self) -> bool:
        """
        @return true if OpenGl context supports left and right rendering buffers.
        """

    def FrameStats(self) -> OpenGl_FrameStats:
        """
        @name methods to alter or retrieve current state
        Return structure holding frame statistics.
        """

    def SetFrameStats(self, theStats: OpenGl_FrameStats | None) -> None:
        """
        Set structure holding frame statistics.
        This call makes sense only if application defines OpenGl_FrameStats sub-class.
        """

    def ResizeViewport(self, theRect: Sequence[int]) -> None:
        """
        Resize the viewport (alias for glViewport).
        @param theRect viewport definition (x, y, width, height)
        """

    def ReadBuffer(self) -> int:
        """Return active read buffer."""

    def SetReadBuffer(self, theReadBuffer: int) -> None:
        """Switch read buffer, wrapper for ::glReadBuffer()."""

    def DrawBuffer(self, theIndex: int = 0) -> int:
        """
        Return active draw buffer attached to a render target referred by index (layout location).
        """

    def SetDrawBuffer(self, theDrawBuffer: int) -> None:
        """Switch draw buffer, wrapper for ::glDrawBuffer()."""

    def SetReadDrawBuffer(self, theBuffer: int) -> None:
        """Switch read/draw buffers."""

    def IsFrameBufferSRGB(self) -> bool:
        """
        Returns cached GL_FRAMEBUFFER_SRGB state.
        If TRUE, GLSL program is expected to write linear RGB color.
        Otherwise, GLSL program might need manually converting result color into sRGB color space.
        """

    def SetFrameBufferSRGB(self, theIsFbo: bool, theIsFboSRgb: bool = True) -> None:
        """
        Enables/disables GL_FRAMEBUFFER_SRGB flag.
        This flag can be set to:
        - TRUE when writing into offscreen FBO (always expected to be in sRGB or RGBF formats).
        - TRUE when writing into sRGB-ready window buffer (might require choosing proper pixel format
        on window creation).
        - FALSE if sRGB rendering is not supported or sRGB-not-ready window buffer is used for
        drawing.
        @param[in] theIsFbo flag indicating writing into offscreen FBO (always expected sRGB-ready
        when sRGB FBO is supported)
        or into window buffer (FALSE, sRGB-readiness might vary).
        @param[in] theIsFboSRgb flag indicating off-screen FBO is sRGB-ready
        """

    def ColorMaskRGBA(self) -> NCollection_Vec4__bool:
        """
        Return cached flag indicating writing into color buffer is enabled or disabled (glColorMask).
        """

    def SetColorMaskRGBA(self, theToWriteColor: NCollection_Vec4__bool) -> None:
        """Enable/disable writing into color buffer (wrapper for glColorMask)."""

    def ColorMask(self) -> bool:
        """
        Return cached flag indicating writing into color buffer is enabled or disabled (glColorMask).
        """

    def SetColorMask(self, theToWriteColor: bool) -> bool:
        """
        Enable/disable writing into color buffer (wrapper for glColorMask).
        Alpha component writes will be disabled unconditionally in case of caps->buffersOpaqueAlpha.
        """

    def AllowSampleAlphaToCoverage(self) -> bool:
        """Return TRUE if GL_SAMPLE_ALPHA_TO_COVERAGE usage is allowed."""

    def SetAllowSampleAlphaToCoverage(self, theToEnable: bool) -> None:
        """Allow GL_SAMPLE_ALPHA_TO_COVERAGE usage."""

    def SampleAlphaToCoverage(self) -> bool:
        """Return GL_SAMPLE_ALPHA_TO_COVERAGE state."""

    def SetSampleAlphaToCoverage(self, theToEnable: bool) -> bool:
        """Enable/disable GL_SAMPLE_ALPHA_TO_COVERAGE."""

    def FaceCulling(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel:
        """Return back face culling state."""

    def SetFaceCulling(self, theMode: nanoocp.Graphic3d.Graphic3d_TypeOfBackfacingModel) -> None:
        """Enable or disable back face culling (glEnable (GL_CULL_FACE))."""

    def ToCullBackFaces(self) -> bool:
        """Return back face culling state."""

    def SetCullBackFaces(self, theToEnable: bool) -> None:
        """
        Enable or disable back face culling (glCullFace() + glEnable(GL_CULL_FACE)).
        """

    def FetchState(self) -> None:
        """
        Fetch OpenGl context state. This class tracks value of several OpenGl
        state variables. Consulting the cached values is quicker than
        doing the same via OpenGl API. Call this method if any of the controlled
        OpenGl state variables has a possibility of being out-of-date.
        """

    def ActiveTextures(self) -> OpenGl_TextureSet:
        """@return active textures"""

    @overload
    def BindTextures(self, theTextures: OpenGl_TextureSet | None) -> OpenGl_TextureSet:
        """
        Deprecated in OCCT: BindTextures() with explicit GLSL program should be used instead

        Bind specified texture set to current context taking into account active GLSL program.
        """

    @overload
    def BindTextures(self, theTextures: OpenGl_TextureSet | None, theProgram: OpenGl_ShaderProgram | None) -> OpenGl_TextureSet:
        """
        Bind specified texture set to current context, or unbind previous one when NULL specified.
        @param[in] theTextures  texture set to bind
        @param[in] theProgram   program attributes; when not NULL,
        mock textures will be bound to texture units expected by GLSL program,
        but undefined by texture set
        @return previous texture set
        """

    def ActiveProgram(self) -> OpenGl_ShaderProgram:
        """@return active GLSL program"""

    def BindProgram(self, theProgram: OpenGl_ShaderProgram | None) -> bool:
        """
        Bind specified program to current context,
        or unbind previous one when NULL specified.
        @return true if some program is bound to context
        """

    def SetShadingMaterial(self, theAspect: OpenGl_Aspects, theHighlight: nanoocp.Graphic3d.Graphic3d_PresentationAttributes | None) -> None:
        """Setup current shading material."""

    @staticmethod
    def CheckIsTransparent__float__float(theAspect: OpenGl_Aspects, theHighlight: nanoocp.Graphic3d.Graphic3d_PresentationAttributes | None) -> tuple[bool, float, float]:
        """
        CheckIsTransparent__float__float: the C++ overload CheckIsTransparent(const OpenGl_Aspects *, const occ::handle<Graphic3d_PresentationAttributes> &, float &, float &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Checks if transparency is required for the given aspect and highlight style.
        """

    @staticmethod
    def CheckIsTransparent(theAspect: OpenGl_Aspects, theHighlight: nanoocp.Graphic3d.Graphic3d_PresentationAttributes | None) -> bool:
        """
        Checks if transparency is required for the given aspect and highlight style.
        """

    @overload
    def SetColor4fv(self, theColor: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Setup current color."""

    @overload
    def SetColor4fv(self, theFrontColor: nanoocp.Quantity.NCollection_Vec4__float, theBackColor: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Setup current front and back colors."""

    def SetTypeOfLine(self, theType: nanoocp.Aspect.Aspect_TypeOfLine, theFactor: float = 1.0) -> None:
        """Setup type of line."""

    @overload
    def SetLineStipple(self, thePattern: int) -> None:
        """
        Setup stipple line pattern with 1.0f factor; wrapper for glLineStipple().
        """

    @overload
    def SetLineStipple(self, theFactor: float, thePattern: int) -> None:
        """Setup type of line; wrapper for glLineStipple()."""

    def SetLineWidth(self, theWidth: float) -> None:
        """Setup width of line."""

    def SetPointSize(self, theSize: float) -> None:
        """Setup point size."""

    def SetPointSpriteOrigin(self) -> None:
        """
        Setup point sprite origin using GL_POINT_SPRITE_COORD_ORIGIN state:
        - GL_UPPER_LEFT when GLSL program is active;
        flipping should be handled in GLSL program for compatibility with OpenGL ES
        - GL_LOWER_LEFT for FFP
        """

    def SetTextureMatrix(self, theParams: nanoocp.Graphic3d.Graphic3d_TextureParams | None, theIsTopDown: bool) -> None:
        """
        Setup texture matrix to active GLSL program or to FFP global state using glMatrixMode
        (GL_TEXTURE).
        @param[in] theParams     texture parameters
        @param[in] theIsTopDown  texture top-down flag
        """

    def BindDefaultVao(self) -> None:
        """Bind default Vertex Array Object"""

    def DefaultFrameBuffer(self) -> OpenGl_FrameBuffer:
        """Default Frame Buffer Object."""

    def SetDefaultFrameBuffer(self, theFbo: OpenGl_FrameBuffer | None) -> OpenGl_FrameBuffer:
        """
        Setup new Default Frame Buffer Object and return previously set.
        This call doesn't change Active FBO!
        """

    def IsDebugContext(self) -> bool:
        """Return debug context initialization state."""

    def EnableFeatures(self) -> None: ...

    def DisableFeatures(self) -> None: ...

    def Resolution(self) -> int:
        """Return resolution for rendering text."""

    def ResolutionRatio(self) -> float:
        """
        Resolution scale factor (rendered resolution to standard resolution).
        This scaling factor for parameters like text size to be properly displayed on device (screen /
        printer).
        """

    def RenderScale(self) -> float:
        """
        Rendering scale factor (rendering viewport height to real window buffer height).
        """

    def HasRenderScale(self) -> bool:
        """Return TRUE if rendering scale factor is not 1."""

    def RenderScaleInv(self) -> float:
        """Rendering scale factor (inverted value)."""

    def LineWidthScale(self) -> float:
        """Return scale factor for line width."""

    def SetResolution(self, theResolution: int, theRatio: float, theScale: float) -> None:
        """
        Set resolution ratio.
        Note that this method rounds @theRatio to nearest integer.
        """

    def SetResolutionRatio(self, theRatio: float) -> None:
        """
        Set resolution ratio.
        Note that this method rounds @theRatio to nearest integer.
        """

    def LineFeather(self) -> float:
        """Return line feater width in pixels."""

    def SetLineFeather(self, theValue: float) -> None:
        """Set line feater width."""

    def Vendor(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return Graphics Driver's vendor."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def DumpJsonOpenGlState(self, theDepth: int = -1) -> str:
        """Dumps the content of openGL state into the stream"""

    def SetShadeModel(self, theModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel) -> None:
        """Set GL_SHADE_MODEL value."""

    @property
    def core11ffp(self) -> OpenGl_GlCore11:
        """OpenGL 1.1 core functionality"""

    @core11ffp.setter
    def core11ffp(self, arg: OpenGl_GlCore11, /) -> None: ...

    @property
    def core11fwd(self) -> OpenGl_GlCore11Fwd:
        """OpenGL 1.1 without deprecated entry points"""

    @core11fwd.setter
    def core11fwd(self, arg: OpenGl_GlCore11Fwd, /) -> None: ...

    @property
    def core15(self) -> OpenGl_GlCore15:
        """OpenGL 1.5 without deprecated entry points"""

    @core15.setter
    def core15(self, arg: OpenGl_GlCore15, /) -> None: ...

    @property
    def core20(self) -> OpenGl_GlCore20:
        """OpenGL 2.0 without deprecated entry points"""

    @core20.setter
    def core20(self, arg: OpenGl_GlCore20, /) -> None: ...

    @property
    def core30(self) -> OpenGl_GlCore30:
        """OpenGL 3.0 without deprecated entry points"""

    @core30.setter
    def core30(self, arg: OpenGl_GlCore30, /) -> None: ...

    @property
    def core32(self) -> OpenGl_GlCore32:
        """OpenGL 3.2 core profile"""

    @core32.setter
    def core32(self, arg: OpenGl_GlCore32, /) -> None: ...

    @property
    def core33(self) -> OpenGl_GlCore33:
        """OpenGL 3.3 core profile"""

    @core33.setter
    def core33(self, arg: OpenGl_GlCore33, /) -> None: ...

    @property
    def core41(self) -> OpenGl_GlCore41:
        """OpenGL 4.1 core profile"""

    @core41.setter
    def core41(self, arg: OpenGl_GlCore41, /) -> None: ...

    @property
    def core42(self) -> OpenGl_GlCore42:
        """OpenGL 4.2 core profile"""

    @core42.setter
    def core42(self, arg: OpenGl_GlCore42, /) -> None: ...

    @property
    def core43(self) -> OpenGl_GlCore43:
        """OpenGL 4.3 core profile"""

    @core43.setter
    def core43(self, arg: OpenGl_GlCore43, /) -> None: ...

    @property
    def core44(self) -> OpenGl_GlCore44:
        """OpenGL 4.4 core profile"""

    @core44.setter
    def core44(self, arg: OpenGl_GlCore44, /) -> None: ...

    @property
    def core45(self) -> OpenGl_GlCore45:
        """OpenGL 4.5 core profile"""

    @core45.setter
    def core45(self, arg: OpenGl_GlCore45, /) -> None: ...

    @property
    def core46(self) -> OpenGl_GlCore46:
        """OpenGL 4.6 core profile"""

    @core46.setter
    def core46(self, arg: OpenGl_GlCore46, /) -> None: ...

    @property
    def core15fwd(self) -> OpenGl_GlCore15:
        """
        obsolete entry left for code portability; core15 should be used instead
        """

    @core15fwd.setter
    def core15fwd(self, arg: OpenGl_GlCore15, /) -> None: ...

    @property
    def core20fwd(self) -> OpenGl_GlCore20:
        """
        obsolete entry left for code portability; core20 should be used instead
        """

    @core20fwd.setter
    def core20fwd(self, arg: OpenGl_GlCore20, /) -> None: ...

    @property
    def caps(self) -> OpenGl_Caps:
        """context options"""

    @caps.setter
    def caps(self, arg: OpenGl_Caps, /) -> None: ...

    @property
    def hasGetBufferData(self) -> bool:
        """flag indicating if GetBufferSubData() is supported"""

    @hasGetBufferData.setter
    def hasGetBufferData(self, arg: bool, /) -> None: ...

    @property
    def hasPackRowLength(self) -> bool:
        """
        supporting of GL_PACK_ROW_LENGTH   parameters (any desktop OpenGL; OpenGL ES 3.0)
        """

    @hasPackRowLength.setter
    def hasPackRowLength(self, arg: bool, /) -> None: ...

    @property
    def hasUnpackRowLength(self) -> bool:
        """
        supporting of GL_UNPACK_ROW_LENGTH parameters (any desktop OpenGL; OpenGL ES 3.0)
        """

    @hasUnpackRowLength.setter
    def hasUnpackRowLength(self, arg: bool, /) -> None: ...

    @property
    def hasHighp(self) -> bool:
        """highp in GLSL ES fragment shader is supported"""

    @hasHighp.setter
    def hasHighp(self, arg: bool, /) -> None: ...

    @property
    def hasUintIndex(self) -> bool:
        """
        GLuint for index buffer is supported (always available on desktop; on OpenGL ES - since 3.0 or as extension GL_OES_element_index_uint)
        """

    @hasUintIndex.setter
    def hasUintIndex(self, arg: bool, /) -> None: ...

    @property
    def hasTexRGBA8(self) -> bool:
        """
        always available on desktop; on OpenGL ES - since 3.0 or as extension GL_OES_rgb8_rgba8
        """

    @hasTexRGBA8.setter
    def hasTexRGBA8(self, arg: bool, /) -> None: ...

    @property
    def hasTexFloatLinear(self) -> bool:
        """
        texture-filterable state for 32-bit floating texture formats (always on desktop, GL_OES_texture_float_linear within OpenGL ES)
        """

    @hasTexFloatLinear.setter
    def hasTexFloatLinear(self, arg: bool, /) -> None: ...

    @property
    def hasTexSRGB(self) -> bool:
        """
        sRGB texture    formats (desktop OpenGL 2.1, OpenGL ES 3.0 or OpenGL ES 2.0 + GL_EXT_sRGB)
        """

    @hasTexSRGB.setter
    def hasTexSRGB(self, arg: bool, /) -> None: ...

    @property
    def hasFboSRGB(self) -> bool:
        """sRGB FBO render targets (desktop OpenGL 2.1, OpenGL ES 3.0)"""

    @hasFboSRGB.setter
    def hasFboSRGB(self, arg: bool, /) -> None: ...

    @property
    def hasSRGBControl(self) -> bool:
        """
        sRGB write control (any desktop OpenGL, OpenGL ES + GL_EXT_sRGB_write_control extension)
        """

    @hasSRGBControl.setter
    def hasSRGBControl(self, arg: bool, /) -> None: ...

    @property
    def hasFboRenderMipmap(self) -> bool:
        """FBO render target could be non-zero mipmap level of texture"""

    @hasFboRenderMipmap.setter
    def hasFboRenderMipmap(self, arg: bool, /) -> None: ...

    @property
    def hasFlatShading(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of Flat shading (Graphic3d_TypeOfShadingModel_Phong) (always available on desktop; on OpenGL ES - since 3.0 or as extension GL_OES_standard_derivatives)
        """

    @hasFlatShading.setter
    def hasFlatShading(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasGlslBitwiseOps(self) -> OpenGl_FeatureFlag:
        """
        GLSL supports bitwise operations; OpenGL 3.0 / OpenGL ES 3.0 (GLSL 130 / GLSL ES 300) or OpenGL 2.1 + GL_EXT_gpu_shader4
        """

    @hasGlslBitwiseOps.setter
    def hasGlslBitwiseOps(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasDrawBuffers(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of multiple draw buffers (desktop OpenGL 2.0, OpenGL ES 3.0, GL_ARB_draw_buffers, GL_EXT_draw_buffers)
        """

    @hasDrawBuffers.setter
    def hasDrawBuffers(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasFloatBuffer(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of float color buffer format (desktop OpenGL 3.0, GL_ARB_color_buffer_float, GL_EXT_color_buffer_float)
        """

    @hasFloatBuffer.setter
    def hasFloatBuffer(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasHalfFloatBuffer(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of half-float color buffer format (desktop OpenGL 3.0, GL_ARB_color_buffer_float, GL_EXT_color_buffer_half_float)
        """

    @hasHalfFloatBuffer.setter
    def hasHalfFloatBuffer(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasSampleVariables(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of MSAA variables in GLSL shader (desktop OpenGL 4.0, GL_ARB_sample_shading)
        """

    @hasSampleVariables.setter
    def hasSampleVariables(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def hasGeometryStage(self) -> OpenGl_FeatureFlag:
        """
        Complex flag indicating support of Geometry shader (desktop OpenGL 3.2, OpenGL ES 3.2, GL_EXT_geometry_shader)
        """

    @hasGeometryStage.setter
    def hasGeometryStage(self, arg: OpenGl_FeatureFlag, /) -> None: ...

    @property
    def arbDrawBuffers(self) -> bool:
        """GL_ARB_draw_buffers"""

    @arbDrawBuffers.setter
    def arbDrawBuffers(self, arg: bool, /) -> None: ...

    @property
    def arbNPTW(self) -> bool:
        """GL_ARB_texture_non_power_of_two"""

    @arbNPTW.setter
    def arbNPTW(self, arg: bool, /) -> None: ...

    @property
    def arbTexRG(self) -> bool:
        """GL_ARB_texture_rg"""

    @arbTexRG.setter
    def arbTexRG(self, arg: bool, /) -> None: ...

    @property
    def arbTexFloat(self) -> bool:
        """
        GL_ARB_texture_float (on desktop OpenGL - since 3.0 or as extension GL_ARB_texture_float; on OpenGL ES - since 3.0); @sa hasTexFloatLinear for linear filtering support
        """

    @arbTexFloat.setter
    def arbTexFloat(self, arg: bool, /) -> None: ...

    @property
    def arbSamplerObject(self) -> OpenGl_ArbSamplerObject:
        """
        GL_ARB_sampler_objects (on desktop OpenGL - since 3.3 or as extension GL_ARB_sampler_objects; on OpenGL ES - since 3.0)
        """

    @arbSamplerObject.setter
    def arbSamplerObject(self, arg: OpenGl_ArbSamplerObject, /) -> None: ...

    @property
    def arbTexBindless(self) -> OpenGl_ArbTexBindless:
        """GL_ARB_bindless_texture"""

    @arbTexBindless.setter
    def arbTexBindless(self, arg: OpenGl_ArbTexBindless, /) -> None: ...

    @property
    def arbTBO(self) -> OpenGl_ArbTBO:
        """
        GL_ARB_texture_buffer_object (on desktop OpenGL - since 3.1 or as extension GL_ARB_texture_buffer_object; on OpenGL ES - since 3.2)
        """

    @arbTBO.setter
    def arbTBO(self, arg: OpenGl_ArbTBO, /) -> None: ...

    @property
    def arbTboRGB32(self) -> bool:
        """
        GL_ARB_texture_buffer_object_rgb32 (3-component TBO), in core since 4.0 (on OpenGL ES - since 3.2)
        """

    @arbTboRGB32.setter
    def arbTboRGB32(self, arg: bool, /) -> None: ...

    @property
    def arbClipControl(self) -> bool:
        """GL_ARB_clip_control, in core since 4.5"""

    @arbClipControl.setter
    def arbClipControl(self, arg: bool, /) -> None: ...

    @property
    def arbIns(self) -> OpenGl_ArbIns:
        """
        GL_ARB_draw_instanced (on desktop OpenGL - since 3.1 or as extension GL_ARB_draw_instanced; on OpenGL ES - since 3.0 or as extension GL_ANGLE_instanced_arrays to WebGL 1.0)
        """

    @arbIns.setter
    def arbIns(self, arg: OpenGl_ArbIns, /) -> None: ...

    @property
    def arbDbg(self) -> OpenGl_ArbDbg:
        """
        GL_ARB_debug_output (on desktop OpenGL - since 4.3 or as extension GL_ARB_debug_output; on OpenGL ES - since 3.2 or as extension GL_KHR_debug)
        """

    @arbDbg.setter
    def arbDbg(self, arg: OpenGl_ArbDbg, /) -> None: ...

    @property
    def arbFBO(self) -> OpenGl_ArbFBO:
        """GL_ARB_framebuffer_object"""

    @arbFBO.setter
    def arbFBO(self, arg: OpenGl_ArbFBO, /) -> None: ...

    @property
    def arbFBOBlit(self) -> OpenGl_ArbFBOBlit:
        """
        glBlitFramebuffer function, moved out from OpenGl_ArbFBO structure for compatibility with OpenGL ES 2.0
        """

    @arbFBOBlit.setter
    def arbFBOBlit(self, arg: OpenGl_ArbFBOBlit, /) -> None: ...

    @property
    def arbSampleShading(self) -> bool:
        """GL_ARB_sample_shading"""

    @arbSampleShading.setter
    def arbSampleShading(self, arg: bool, /) -> None: ...

    @property
    def arbDepthClamp(self) -> bool:
        """
        GL_ARB_depth_clamp (on desktop OpenGL - since 3.2 or as extensions GL_ARB_depth_clamp,NV_depth_clamp; unavailable on OpenGL ES)
        """

    @arbDepthClamp.setter
    def arbDepthClamp(self, arg: bool, /) -> None: ...

    @property
    def extFragDepth(self) -> bool:
        """
        GL_EXT_frag_depth on OpenGL ES 2.0 (gl_FragDepthEXT built-in variable, before OpenGL ES 3.0)
        """

    @extFragDepth.setter
    def extFragDepth(self, arg: bool, /) -> None: ...

    @property
    def extDrawBuffers(self) -> bool:
        """GL_EXT_draw_buffers"""

    @extDrawBuffers.setter
    def extDrawBuffers(self, arg: bool, /) -> None: ...

    @property
    def extGS(self) -> OpenGl_ExtGS:
        """GL_EXT_geometry_shader4"""

    @extGS.setter
    def extGS(self, arg: OpenGl_ExtGS, /) -> None: ...

    @property
    def extBgra(self) -> bool:
        """GL_EXT_bgra or GL_EXT_texture_format_BGRA8888 on OpenGL ES"""

    @extBgra.setter
    def extBgra(self, arg: bool, /) -> None: ...

    @property
    def extTexR16(self) -> bool:
        """GL_EXT_texture_norm16 on OpenGL ES; always available on desktop"""

    @extTexR16.setter
    def extTexR16(self, arg: bool, /) -> None: ...

    @property
    def extAnis(self) -> bool:
        """GL_EXT_texture_filter_anisotropic"""

    @extAnis.setter
    def extAnis(self, arg: bool, /) -> None: ...

    @property
    def extPDS(self) -> bool:
        """GL_EXT_packed_depth_stencil"""

    @extPDS.setter
    def extPDS(self, arg: bool, /) -> None: ...

    @property
    def atiMem(self) -> bool:
        """GL_ATI_meminfo"""

    @atiMem.setter
    def atiMem(self, arg: bool, /) -> None: ...

    @property
    def nvxMem(self) -> bool:
        """GL_NVX_gpu_memory_info"""

    @nvxMem.setter
    def nvxMem(self, arg: bool, /) -> None: ...

    @property
    def oesSampleVariables(self) -> bool:
        """GL_OES_sample_variables"""

    @oesSampleVariables.setter
    def oesSampleVariables(self, arg: bool, /) -> None: ...

    @property
    def oesStdDerivatives(self) -> bool:
        """GL_OES_standard_derivatives"""

    @oesStdDerivatives.setter
    def oesStdDerivatives(self, arg: bool, /) -> None: ...

    @property
    def ModelWorldState(self) -> OpenGl_MatrixState__float:
        """state of orientation matrix"""

    @ModelWorldState.setter
    def ModelWorldState(self, arg: OpenGl_MatrixState__float, /) -> None: ...

    @property
    def WorldViewState(self) -> OpenGl_MatrixState__float:
        """state of orientation matrix"""

    @WorldViewState.setter
    def WorldViewState(self, arg: OpenGl_MatrixState__float, /) -> None: ...

    @property
    def ProjectionState(self) -> OpenGl_MatrixState__float:
        """state of projection  matrix"""

    @ProjectionState.setter
    def ProjectionState(self, arg: OpenGl_MatrixState__float, /) -> None: ...

class OpenGl_TextBuilder:
    """
    This class generates primitive array required for rendering textured text using OpenGl_Font
    instance.
    """

    @overload
    def __init__(self) -> None:
        """Creates empty object."""

    @overload
    def __init__(self, theOther: OpenGl_TextBuilder) -> None: ...

    def Perform(self, theFormatter: nanoocp.Font.Font_TextFormatter | None, theContext: OpenGl_Context | None, theFont: OpenGl_Font, theTextures: nanoocp.NCollection.NCollection_DynamicArray__unsigned_int, theVertsPerTexture: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.OpenGl.OpenGl_VertexBuffer], theTCrdsPerTexture: nanoocp.NCollection.NCollection_DynamicArray[nanoocp.OpenGl.OpenGl_VertexBuffer]) -> None:
        """Creates texture quads for the given text."""

class OpenGl_Text(OpenGl_Element):
    """Text rendering"""

    @overload
    def __init__(self) -> None:
        """
        @name methods for compatibility with layers
        Empty constructor
        """

    @overload
    def __init__(self, theTextParams: nanoocp.Graphic3d.Graphic3d_Text | None) -> None:
        """Creates new text in 3D space."""

    @overload
    def __init__(self, theOther: OpenGl_Text) -> None: ...

    def Reset(self, theCtx: OpenGl_Context | None) -> None:
        """
        Release cached VBO resources and the previous font if height changed.
        Cached structures will be refilled by the next render.
        Call Reset after modifying text parameters.
        """

    def Text(self) -> nanoocp.Graphic3d.Graphic3d_Text:
        """
        Returns text parameters
        @sa Reset()
        """

    def SetText(self, theText: nanoocp.Graphic3d.Graphic3d_Text | None) -> None:
        """
        Sets text parameters
        @sa Reset()
        """

    def Is2D(self) -> bool:
        """Return true if text is 2D"""

    def Set2D(self, theEnable: bool) -> None:
        """Set true if text is 2D"""

    def SetFontSize(self, theContext: OpenGl_Context | None, theFontSize: int) -> None:
        """Setup new font size"""

    @overload
    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None: ...

    @overload
    def Render(self, theCtx: OpenGl_Context | None, theTextAspect: OpenGl_Aspects, theResolution: int = 72, theFontHinting: nanoocp.Font.Font_Hinting = Font_Hinting.Font_Hinting_Off) -> None:
        """Perform rendering"""

    def Release(self, theContext: OpenGl_Context) -> None: ...

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def UpdateDrawStats(self, theStats: nanoocp.Graphic3d.Graphic3d_FrameStatsDataTmp, theIsDetailed: bool) -> None:
        """Increment draw calls statistics."""

    @staticmethod
    def FontKey(theAspect: OpenGl_Aspects, theHeight: int, theResolution: int, theFontHinting: nanoocp.Font.Font_Hinting) -> nanoocp.TCollection.TCollection_AsciiString:
        """Create key for shared resource"""

    @staticmethod
    def FindFont(theCtx: OpenGl_Context | None, theAspect: OpenGl_Aspects, theHeight: int, theResolution: int, theFontHinting: nanoocp.Font.Font_Hinting, theKey: nanoocp.TCollection.TCollection_AsciiString) -> OpenGl_Font:
        """Find shared resource for specified font or initialize new one"""

    @staticmethod
    def StringSize(theCtx: OpenGl_Context | None, theText: nanoocp.NCollection.NCollection_String, theTextAspect: OpenGl_Aspects, theHeight: float, theResolution: int, theFontHinting: nanoocp.Font.Font_Hinting) -> tuple[float, float, float]:
        """Compute text width"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def Init(self, theCtx: OpenGl_Context | None, theText: str, thePoint: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Deprecated in OCCT: Deprecated method Init() with obsolete arguments, use Init() and Text() instead of it

        Setup new string and position
        """

    def SetPosition(self, thePoint: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Deprecated in OCCT: Deprecated method SetPosition(), use Graphic3d_Text for it

        Setup new position
        """

class OpenGl_FrameStatsPrs(OpenGl_Element):
    """Element rendering frame statistics."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: OpenGl_FrameStatsPrs) -> None: ...

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Render element."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Release OpenGL resources."""

    def Update(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Update text."""

    def SetTextAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectText3d | None) -> None:
        """Assign text aspect."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_ElementNode:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ElementNode) -> None: ...

    @property
    def elem(self) -> OpenGl_Element: ...

    @elem.setter
    def elem(self, arg: OpenGl_Element, /) -> None: ...

    @property
    def next(self) -> OpenGl_ElementNode: ...

    @next.setter
    def next(self, arg: OpenGl_ElementNode, /) -> None: ...

class OpenGl_Group(nanoocp.Graphic3d.Graphic3d_Group):
    """Implementation of low-level graphic group."""

    def __init__(self, theStruct: nanoocp.Graphic3d.Graphic3d_Structure | None) -> None:
        """
        Create empty group.
        Will throw exception if not created by OpenGl_Structure.
        """

    def Clear(self, theToUpdateStructureMgr: bool) -> None: ...

    def Aspects(self) -> nanoocp.Graphic3d.Graphic3d_Aspects:
        """Return line aspect."""

    def HasPersistence(self) -> bool:
        """Return TRUE if group contains primitives with transform persistence."""

    def SetGroupPrimitivesAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Update aspect."""

    def SetPrimitivesAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Append aspect as an element."""

    def SynchronizeAspects(self) -> None:
        """Update presentation aspects after their modification."""

    def ReplaceAspects(self, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.Graphic3d.Graphic3d_Aspects, nanoocp.Graphic3d.Graphic3d_Aspects]) -> None:
        """Replace aspects specified in the replacement map."""

    def AddPrimitiveArray(self, theType: nanoocp.Graphic3d.Graphic3d_TypeOfPrimitiveArray, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theAttribs: nanoocp.Graphic3d.Graphic3d_Buffer | None, theBounds: nanoocp.Graphic3d.Graphic3d_BoundBuffer | None, theToEvalMinMax: bool) -> None:
        """Add primitive array element"""

    def AddText(self, theTextParams: nanoocp.Graphic3d.Graphic3d_Text | None, theToEvalMinMax: bool) -> None:
        """Adds a text for display"""

    def SetFlippingOptions(self, theIsEnabled: bool, theRefPlane: nanoocp.gp.gp_Ax2) -> None:
        """Add flipping element"""

    def SetStencilTestOptions(self, theIsEnabled: bool) -> None:
        """Add stencil test element"""

    def GlStruct(self) -> OpenGl_Structure: ...

    def AddElement(self, theElem: OpenGl_Element) -> None: ...

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None: ...

    def Release(self, theGlCtx: OpenGl_Context | None) -> None: ...

    def FirstNode(self) -> OpenGl_ElementNode:
        """Returns first OpenGL element node of the group."""

    def GlAspects(self) -> OpenGl_Aspects:
        """Returns OpenGL aspect."""

    def IsRaytracable(self) -> bool:
        """Is the group ray-tracable (contains ray-tracable elements)?"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_GlCore14(OpenGl_GlCore13):
    """OpenGL 1.4 core based on 1.3 version."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore14) -> None: ...

class OpenGl_GlCore15(OpenGl_GlCore14):
    """OpenGL 1.5 core based on 1.4 version."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore15) -> None: ...

class OpenGl_GlCore20(OpenGl_GlCore15):
    """OpenGL 2.0 core based on 1.5 version."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore20) -> None: ...

class OpenGl_ShaderObject(OpenGl_Resource):
    """Wrapper for OpenGL shader object."""

    def __init__(self, theType: int) -> None:
        """Creates uninitialized shader object."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LoadSource(self, theCtx: OpenGl_Context | None, theSource: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Loads shader source code."""

    def Compile(self, theCtx: OpenGl_Context | None) -> bool:
        """Compiles the shader object."""

    def LoadAndCompile(self, theCtx: OpenGl_Context | None, theId: nanoocp.TCollection.TCollection_AsciiString, theSource: nanoocp.TCollection.TCollection_AsciiString, theIsVerbose: bool = True, theToPrintSource: bool = True) -> bool:
        """
        Wrapper for compiling shader object with verbose printing on error.
        @param theCtx bound OpenGL context
        @param theId  GLSL program id to define file name
        @param theSource source code to load
        @param theIsVerbose flag to print log on error
        @param theToPrintSource flag to print source code on error
        """

    def DumpSourceCode(self, theCtx: OpenGl_Context | None, theId: nanoocp.TCollection.TCollection_AsciiString, theSource: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Print source code of this shader object to messenger."""

    def FetchInfoLog(self, theCtx: OpenGl_Context | None, theLog: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Fetches information log of the last compile operation."""

    def Create(self, theCtx: OpenGl_Context | None) -> bool:
        """Creates new empty shader object of specified type."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Destroys shader object."""

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage - not implemented."""

    def Type(self) -> int:
        """Returns type of shader object."""

    def updateDebugDump(self, theCtx: OpenGl_Context | None, theId: nanoocp.TCollection.TCollection_AsciiString, theFolder: nanoocp.TCollection.TCollection_AsciiString, theToBeautify: bool, theToReset: bool) -> bool:
        """
        Update the shader object from external file in the following way:
        1) If external file does not exist, then it will be created (current source code will be
        dumped, no recompilation) and FALSE will be returned. 2) If external file exists and it has
        the same timestamp as myDumpDate, nothing will be done and FALSE will be returned. 3)
        If external file exists and it has newer timestamp than myDumpDate, shader will be
        recompiled and TRUE will be returned.
        @param theCtx OpenGL context bound to this working thread
        @param theId  GLSL program id to define file name
        @param theFolder folder to store files
        @param theToBeautify flag improving formatting (add extra newlines)
        @param theToReset when TRUE, existing dumps will be overridden
        """

class OpenGl_SetterInterface:
    """Interface for generic setter of user-defined uniform variables."""

    def Set(self, theCtx: OpenGl_Context | None, theVariable: nanoocp.Graphic3d.Graphic3d_ShaderVariable | None, theProgram: OpenGl_ShaderProgram) -> None:
        """Sets user-defined uniform variable to specified program."""

class OpenGl_VariableSetterSelector:
    """Support tool for setting user-defined uniform variables."""

    @overload
    def __init__(self) -> None:
        """Creates new setter selector."""

    @overload
    def __init__(self, theOther: OpenGl_VariableSetterSelector) -> None: ...

    def Set(self, theCtx: OpenGl_Context | None, theVariable: nanoocp.Graphic3d.Graphic3d_ShaderVariable | None, theProgram: OpenGl_ShaderProgram) -> None:
        """Sets user-defined uniform variable to specified program."""

class OpenGl_ShaderUniformLocation:
    """Simple class represents GLSL program variable location."""

    @overload
    def __init__(self) -> None:
        """Construct an invalid location."""

    @overload
    def __init__(self, theLocation: int) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: OpenGl_ShaderUniformLocation) -> None: ...

    def IsValid(self) -> bool:
        """
        Note you may safely put invalid location in functions like glUniform* - the data passed in
        will be silently ignored.
        @return true if location is not equal to -1.
        """

    def __bool__(self) -> bool:
        """Return TRUE for non-invalid location."""

    def __int__(self) -> int:
        """
        Convert operators help silently put object to GL functions like glUniform*.
        """

class OpenGl_ShaderProgram(OpenGl_NamedResource):
    """Wrapper for OpenGL program object."""

    def __init__(self, theProxy: nanoocp.Graphic3d.Graphic3d_ShaderProgram | None = None, theId: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """
        Creates uninitialized shader program.

        WARNING! This constructor is not intended to be called anywhere but from
        OpenGl_ShaderManager::Create(). Manager has been designed to synchronize camera position,
        lights definition and other aspects of the program implicitly, as well as sharing same program
        across rendering groups.

        Program created outside the manager will be left detached from these routines,
        and them should be performed manually by caller.

        This constructor has been made public to provide more flexibility to re-use OCCT OpenGL
        classes without OCCT Viewer itself. If this is not the case - create the program using shared
        OpenGl_ShaderManager instance instead.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Create(self, theCtx: OpenGl_Context | None) -> bool:
        """Creates new empty shader program of specified type."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Destroys shader program."""

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage - cannot be easily estimated."""

    def AttachShader(self, theCtx: OpenGl_Context | None, theShader: OpenGl_ShaderObject | None) -> bool:
        """Attaches shader object to the program object."""

    def DetachShader(self, theCtx: OpenGl_Context | None, theShader: OpenGl_ShaderObject | None) -> bool:
        """Detaches shader object to the program object."""

    def Initialize(self, theCtx: OpenGl_Context | None, theShaders: nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderObject]) -> bool:
        """Initializes program object with the list of shader objects."""

    def Link(self, theCtx: OpenGl_Context | None, theIsVerbose: bool = True) -> bool:
        """
        Links the program object.
        @param theCtx bound OpenGL context
        @param theIsVerbose flag to print log on error
        """

    def FetchInfoLog(self, theCtx: OpenGl_Context | None, theLog: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Fetches information log of the last link operation."""

    def ApplyVariables(self, theCtx: OpenGl_Context | None) -> bool:
        """Fetches uniform variables from proxy shader program."""

    def Proxy(self) -> nanoocp.Graphic3d.Graphic3d_ShaderProgram:
        """@return proxy shader program."""

    def IsValid(self) -> bool:
        """@return true if current object was initialized"""

    def ProgramId(self) -> int:
        """@return program ID"""

    def HasTessellationStage(self) -> bool:
        """Return TRUE if program defines tessellation stage."""

    def NbLightsMax(self) -> int:
        """
        Return the length of array of light sources (THE_MAX_LIGHTS),
        to be used for initialization occLightSources (OpenGl_OCC_LIGHT_SOURCE_PARAMS).
        """

    def NbShadowMaps(self) -> int:
        """
        Return the length of array of shadow maps (THE_NB_SHADOWMAPS); 0 by default.
        """

    def NbClipPlanesMax(self) -> int:
        """
        Return the length of array of clipping planes (THE_MAX_CLIP_PLANES),
        to be used for initialization occClipPlaneEquations (OpenGl_OCC_CLIP_PLANE_EQUATIONS) and
        occClipPlaneChains (OpenGl_OCC_CLIP_PLANE_CHAINS).
        """

    def NbFragmentOutputs(self) -> int:
        """
        Return the length of array of Fragment Shader outputs (THE_NB_FRAG_OUTPUTS),
        to be used for initialization occFragColorArray/occFragColorN.
        """

    def HasAlphaTest(self) -> bool:
        """
        Return true if Fragment Shader should perform alpha test; FALSE by default.
        """

    def OitOutput(self) -> nanoocp.Graphic3d.Graphic3d_RenderTransparentMethod:
        """
        Return if Fragment Shader color should output the OIT values; OFF by default.
        """

    def TextureSetBits(self) -> int:
        """
        Return texture units declared within the program, @sa Graphic3d_TextureSetBits.
        """

    def GetUniformLocation(self, theCtx: OpenGl_Context | None, theName: str) -> OpenGl_ShaderUniformLocation:
        """Returns location of the specific uniform variable."""

    def GetAttributeLocation(self, theCtx: OpenGl_Context | None, theName: str) -> int:
        """Returns index of the generic vertex attribute by variable name."""

    def GetStateLocation(self, theVariable: OpenGl_StateVariable) -> OpenGl_ShaderUniformLocation:
        """Returns location of the OCCT state uniform variable."""

    @overload
    def GetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.BVH.BVH_Vec4i) -> bool:
        """
        Returns the value of the integer uniform variable.
        Wrapper for glGetUniformiv()
        """

    @overload
    def GetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """
        Returns the value of the float uniform variable.
        Wrapper for glGetUniformfv()
        """

    @overload
    def GetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: nanoocp.BVH.BVH_Vec4i) -> bool:
        """
        Returns the integer vertex attribute.
        Wrapper for glGetVertexAttribiv()
        """

    @overload
    def GetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """
        Returns the float vertex attribute.
        Wrapper for glGetVertexAttribfv()
        """

    def SetAttributeName(self, theCtx: OpenGl_Context | None, theIndex: int, theName: str) -> bool:
        """Wrapper for glBindAttribLocation()"""

    @overload
    def SetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: float) -> bool:
        """Wrapper for glVertexAttrib1f()"""

    @overload
    def SetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: nanoocp.Poly.NCollection_Vec2__float) -> bool:
        """Wrapper for glVertexAttrib2fv()"""

    @overload
    def SetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Wrapper for glVertexAttrib3fv()"""

    @overload
    def SetAttribute(self, theCtx: OpenGl_Context | None, theIndex: int, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """Wrapper for glVertexAttrib4fv()"""

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: int) -> bool:
        """
        Specifies the value of the integer uniform variable.
        Wrapper for glUniform1i()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.BVH.BVH_Vec2i) -> bool:
        """
        Specifies the value of the integer uniform 2D vector.
        Wrapper for glUniform2iv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.BVH.BVH_Vec3i) -> bool:
        """
        Specifies the value of the integer uniform 3D vector.
        Wrapper for glUniform3iv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.BVH.BVH_Vec4i) -> bool:
        """
        Specifies the value of the integer uniform 4D vector.
        Wrapper for glUniform4iv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: NCollection_Vec2__unsigned_int) -> bool:
        """
        Specifies the value of the unsigned integer uniform 2D vector (uvec2).
        Wrapper for glUniform2uiv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theName: str, theCount: int, theValue: NCollection_Vec2__unsigned_int) -> bool: ...

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theValue: NCollection_Vec2__unsigned_int) -> bool:
        """
        Specifies the value of the uvec2 uniform array
        Wrapper for glUniform2uiv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: float) -> bool:
        """
        Specifies the value of the float uniform variable.
        Wrapper for glUniform1f()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.Poly.NCollection_Vec2__float) -> bool:
        """
        Specifies the value of the float uniform 2D vector.
        Wrapper for glUniform2fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """
        Specifies the value of the float uniform 3D vector.
        Wrapper for glUniform3fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """
        Specifies the value of the float uniform 4D vector.
        Wrapper for glUniform4fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.Graphic3d.NCollection_Mat3__float) -> bool:
        """
        Specifies the value of the array of float uniform 3x3 matrices.
        Wrapper over glUniformMatrix3fv().
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theName: str, theValue: nanoocp.Graphic3d.NCollection_Mat3__float, theTranspose: int = 0) -> bool: ...

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.Graphic3d.NCollection_Mat3__float, theTranspose: int = 0) -> bool:
        """
        Specifies the value of the float uniform 3x3 matrix.
        Wrapper for glUniformMatrix3fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theName: str, theValue: nanoocp.BVH.BVH_Mat4f, theTranspose: int = 0) -> bool: ...

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theValue: nanoocp.BVH.BVH_Mat4f, theTranspose: int = 0) -> bool:
        """
        Specifies the value of the float uniform 4x4 matrix.
        Wrapper for glUniformMatrix4fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.BVH.BVH_Mat4f) -> bool:
        """
        Specifies the value of the array of float uniform 4x4 matrices.
        Wrapper over glUniformMatrix4fv().
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.Poly.NCollection_Vec2__float) -> bool:
        """
        Specifies the value of the float2 uniform array
        Wrapper over glUniform2fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """
        Specifies the value of the float3 uniform array
        Wrapper over glUniform3fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """
        Specifies the value of the float4 uniform array
        Wrapper over glUniform4fv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.BVH.BVH_Vec2i) -> bool:
        """
        Specifies the value of the int2 uniform array
        Wrapper over glUniform2iv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.BVH.BVH_Vec3i) -> bool:
        """
        Specifies the value of the int3 uniform array
        Wrapper over glUniform3iv()
        """

    @overload
    def SetUniform(self, theCtx: OpenGl_Context | None, theLocation: int, theCount: int, theData: nanoocp.BVH.BVH_Vec4i) -> bool:
        """
        Specifies the value of the int4 uniform array
        Wrapper over glUniform4iv()
        """

    @overload
    def SetSampler(self, theCtx: OpenGl_Context | None, theName: str, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> bool: ...

    @overload
    def SetSampler(self, theCtx: OpenGl_Context | None, theLocation: int, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> bool:
        """Specifies the value of the sampler uniform variable."""

    def UpdateDebugDump(self, theCtx: OpenGl_Context | None, theFolder: nanoocp.TCollection.TCollection_AsciiString = ..., theToBeautify: bool = False, theToReset: bool = False) -> bool:
        """
        Update the shader program from external files (per shader stage) in the following way:
        1) If external file does not exist, then it will be created (current source code will be
        dumped, no recompilation) and FALSE will be returned. 2) If external file exists and it has
        the same timestamp as myDumpDate, nothing will be done and FALSE will be returned. 3) If
        external file exists and it has newer timestamp than myDumpDate, shader will be recompiled
        and relinked and TRUE will be returned.
        @param theCtx OpenGL context bound to this working thread
        @param theFolder folder to store files; when unspecified, $CSF_ShadersDirectoryDump or current
        folder will be used instead
        @param theToBeautify flag improving formatting (add extra newlines)
        @param theToReset when TRUE, existing dumps will be overridden
        """

class OpenGl_ShaderGrid:
    """State and geometry model of the OpenGl shader-rendered grid."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ShaderGrid) -> None: ...

    def IsShown(self) -> bool:
        """Return TRUE if the grid is currently shown."""

    def IsBackground(self) -> bool:
        """Return TRUE if the grid is rendered as a background."""

    def Params(self) -> nanoocp.Aspect.Aspect_GridParams:
        """Return current parameters."""

    def Display(self, theParams: nanoocp.Aspect.Aspect_GridParams, thePlane: nanoocp.gp.gp_Ax3, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None, theContext: OpenGl_Context | None) -> bool:
        """
        Store grid state. Returns FALSE when parameters cannot produce a shader grid.
        """

    def Erase(self) -> None:
        """Clear grid state."""

    def AddZFitBounds(self, theGraphicBox: nanoocp.Bnd.Bnd_Box, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None) -> None:
        """Add helper bounds required by camera Z fitting."""

    def Echo(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None, theWidth: int, theHeight: int, theX: int, theY: int, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex, theDisplayPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """Return snapped point for the grid under the window pixel."""

    def SnapPoint(self, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex, theGridPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """Return snapped point for an arbitrary world point."""

    def SetUniforms(self, theContext: OpenGl_Context | None, theProgram: OpenGl_ShaderProgram | None, theCamera: nanoocp.Graphic3d.Graphic3d_Camera | None, theWorldView: nanoocp.BVH.BVH_Mat4f) -> None:
        """Upload shader uniforms for current grid state."""

    def DrawWorldView(self, theCurrentWorldView: nanoocp.BVH.BVH_Mat4f) -> nanoocp.BVH.BVH_Mat4f:
        """Return worldview matrix to use for drawing."""

class OpenGl_StateCounter:
    """
    Tool class to implement consistent state counter
    for objects inside the same driver instance.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_StateCounter) -> None: ...

    def Increment(self) -> int: ...

class OpenGl_GraphicDriver(nanoocp.Graphic3d.Graphic3d_GraphicDriver):
    """This class defines an OpenGl graphic driver"""

    @overload
    def __init__(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None, theToInitialize: bool = True) -> None:
        """
        Constructor.
        @param theDisp connection to display, required on Linux but optional on other systems
        @param theToInitialize perform initialization of default OpenGL context on construction
        """

    @overload
    def __init__(self, theOther: OpenGl_GraphicDriver) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ReleaseContext(self) -> None:
        """Release default context."""

    def InitContext(self) -> bool:
        """Perform initialization of default OpenGL context."""

    def InquireLimit(self, theType: nanoocp.Graphic3d.Graphic3d_TypeOfLimit) -> int:
        """Request limit of graphic resource of specific type."""

    def CreateStructure(self, theManager: nanoocp.Graphic3d.Graphic3d_StructureManager | None) -> nanoocp.Graphic3d.Graphic3d_CStructure: ...

    def RemoveStructure(self) -> nanoocp.Graphic3d.Graphic3d_CStructure: ...

    def CreateView(self, theMgr: nanoocp.Graphic3d.Graphic3d_StructureManager | None) -> nanoocp.Graphic3d.Graphic3d_CView: ...

    def RemoveView(self, theView: nanoocp.Graphic3d.Graphic3d_CView | None) -> None: ...

    def TextSize(self, theView: nanoocp.Graphic3d.Graphic3d_CView | None, theText: str, theHeight: float) -> tuple[float, float, float]: ...

    def DefaultTextHeight(self) -> float: ...

    def ViewExists(self, theWindow: nanoocp.Aspect.Aspect_Window | None) -> tuple[bool, nanoocp.Graphic3d.Graphic3d_CView]: ...

    def InsertLayerBefore(self, theNewLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerAfter: int) -> None:
        """
        Adds a layer to all views.
        @param[in] theNewLayerId id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings   new layer settings
        @param[in] theLayerAfter id of layer to append new layer before
        """

    def InsertLayerAfter(self, theNewLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerBefore: int) -> None:
        """
        Adds a layer to all views.
        @param[in] theNewLayerId  id of created layer
        @param[in] theSettings    new layer settings
        @param[in] theLayerBefore id of layer to append new layer after
        """

    def RemoveZLayer(self, theLayerId: int) -> None:
        """
        Removes Z layer. All structures displayed at the moment in layer will be displayed in
        default layer (the bottom-level z layer). By default, there are always default
        bottom-level layer that can't be removed. The passed theLayerId should be not less than 0
        (reserved for default layers that can not be removed).
        """

    def SetZLayerSettings(self, theLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings) -> None:
        """Sets the settings for a single Z layer."""

    def Options(self) -> OpenGl_Caps:
        """@return the visualization options"""

    def ChangeOptions(self) -> OpenGl_Caps:
        """@return the visualization options"""

    def SetBuffersNoSwap(self, theIsNoSwap: bool) -> None:
        """Specify swap buffer behavior."""

    def EnableVBO(self, theToTurnOn: bool) -> None:
        """
        VBO usage can be forbidden by this method even if it is supported by GL driver.
        Notice that disabling of VBO will cause rendering performance degradation.
        Warning! This method should be called only before any primitives are displayed in GL scene!
        """

    def IsVerticalSync(self) -> bool:
        """
        Returns TRUE if vertical synchronization with display refresh rate (VSync) should be used;
        TRUE by default.
        """

    def SetVerticalSync(self, theToEnable: bool) -> None:
        """
        Set if vertical synchronization with display refresh rate (VSync) should be used.
        """

    def MemoryInfo(self, theInfo: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, int]:
        """
        Returns information about GPU memory usage.
        Please read OpenGl_Context::MemoryInfo() for more description.
        """

    def GetSharedContext(self, theBound: bool = False) -> OpenGl_Context:
        """
        Method to retrieve valid GL context.
        Could return NULL-handle if no window created by this driver.
        @param theBound if TRUE then currently bound context will be returned,
        any context will be returned otherwise
        """

    def setDeviceLost(self) -> None:
        """Set device lost flag for redrawn views."""

    def GetStateCounter(self) -> OpenGl_StateCounter:
        """State counter for OpenGl structures."""

    def GetNextPrimitiveArrayUID(self) -> int:
        """Returns unique ID for primitive arrays."""

class OpenGl_Workspace(nanoocp.Standard.Standard_Transient):
    """
    Rendering workspace.
    Provides methods to render primitives and maintain GL state.
    """

    @overload
    def __init__(self, theView: OpenGl_View, theWindow: OpenGl_Window | None) -> None:
        """Constructor of rendering workspace."""

    @overload
    def __init__(self, theOther: OpenGl_Workspace) -> None: ...

    def Activate(self) -> bool:
        """Activate rendering context."""

    def View(self) -> OpenGl_View: ...

    def GetGlContext(self) -> OpenGl_Context: ...

    def FBOCreate(self, theWidth: int, theHeight: int) -> OpenGl_FrameBuffer: ...

    def FBORelease(self) -> OpenGl_FrameBuffer: ...

    def BufferDump(self, theFbo: OpenGl_FrameBuffer | None, theImage: nanoocp.Image.Image_PixMap, theBufferType: nanoocp.Graphic3d.Graphic3d_BufferType) -> bool: ...

    def Width(self) -> int: ...

    def Height(self) -> int: ...

    def SetUseZBuffer(self, theToUse: bool) -> bool:
        """
        Setup Z-buffer usage flag (without affecting GL state!).
        Returns previously set flag.
        """

    def UseZBuffer(self) -> bool:
        """@return true if usage of Z buffer is enabled."""

    def UseDepthWrite(self) -> bool:
        """@return true if depth writing is enabled."""

    def SetUseDepthWrite(self, theValue: bool) -> None:
        """
        Python addition: sets the value UseDepthWrite() returns by reference in C++.
        """

    def SetDefaultPolygonOffset(self, theOffset: nanoocp.Graphic3d.Graphic3d_PolygonOffset) -> nanoocp.Graphic3d.Graphic3d_PolygonOffset:
        """
        Configure default polygon offset parameters.
        Return previous settings.
        """

    def ToAllowFaceCulling(self) -> bool:
        """
        Return true if active group might activate face culling (e.g. primitives are closed).
        """

    def SetAllowFaceCulling(self, theToAllow: bool) -> bool:
        """
        Allow or disallow face culling.
        This call does NOT affect current state of back face culling;
        ApplyAspectFace() should be called to update state.
        """

    def ToHighlight(self) -> bool:
        """Return true if following structures should apply highlight color."""

    def HighlightStyle(self) -> nanoocp.Graphic3d.Graphic3d_PresentationAttributes:
        """Return highlight style."""

    def SetHighlightStyle(self, theStyle: nanoocp.Graphic3d.Graphic3d_PresentationAttributes | None) -> None:
        """Set highlight style."""

    def EdgeColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Return edge color taking into account highlight flag."""

    def InteriorColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Return Interior color taking into account highlight flag."""

    def BackInteriorColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Return back interior color taking into account highlight and distinguish flags.
        """

    def TextColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Return text color taking into account highlight flag."""

    def TextSubtitleColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Return text Subtitle color taking into account highlight flag."""

    def Aspects(self) -> OpenGl_Aspects:
        """Currently set aspects (can differ from applied)."""

    def SetAspects(self, theAspect: OpenGl_Aspects) -> OpenGl_Aspects:
        """Assign new aspects (will be applied within ApplyAspects())."""

    def TextureSet(self) -> OpenGl_TextureSet:
        """Return TextureSet from set Aspects or Environment texture."""

    def ApplyAspects(self, theToBindTextures: bool = True) -> OpenGl_Aspects:
        """
        Apply aspects.
        @param theToBindTextures flag to bind texture set defined by applied aspect
        @return aspect set by SetAspects()
        """

    def ResetAppliedAspect(self) -> None:
        """Clear the applied aspect state to default values."""

    def RenderFilter(self) -> int:
        """
        Get rendering filter.
        @sa ShouldRender()
        """

    def SetRenderFilter(self, theFilter: int) -> None:
        """
        Set filter for restricting rendering of particular elements.
        @sa ShouldRender()
        """

    def ShouldRender(self, theElement: OpenGl_Element, theGroup: OpenGl_Group) -> bool:
        """
        Checks whether the element can be rendered or not.
        @param[in] theElement  the element to check
        @param[in] theGroup    the group containing the element
        @return True if element can be rendered
        """

    def NbSkippedTransparentElements(self) -> int:
        """
        Return the number of skipped transparent elements within active OpenGl_RenderFilter_OpaqueOnly
        filter.
        @sa OpenGl_LayerList::Render()
        """

    def ResetSkippedCounter(self) -> None:
        """
        Reset skipped transparent elements counter.
        @sa OpenGl_LayerList::Render()
        """

    def NoneCulling(self) -> OpenGl_Aspects:
        """Returns face aspect for none culling mode."""

    def FrontCulling(self) -> OpenGl_Aspects:
        """Returns face aspect for front face culling mode."""

    def SetEnvironmentTexture(self, theTexture: OpenGl_TextureSet | None) -> None:
        """Sets a new environment texture."""

    def EnvironmentTexture(self) -> OpenGl_TextureSet:
        """Returns environment texture."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str:
        """@name type definition"""

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type:
        """@name type definition"""

    def DynamicType(self) -> nanoocp.Standard.Standard_Type:
        """@name type definition"""

class OpenGl_Structure(nanoocp.Graphic3d.Graphic3d_CStructure):
    """Implementation of low-level graphic structure."""

    def __init__(self, theManager: nanoocp.Graphic3d.Graphic3d_StructureManager | None) -> None:
        """Create empty structure"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def OnVisibilityChanged(self) -> None:
        """Setup structure graphic state"""

    @overload
    def Clear(self) -> None:
        """Clear graphic data"""

    @overload
    def Clear(self, theGlCtx: OpenGl_Context | None) -> None: ...

    def Connect(self, theStructure: nanoocp.Graphic3d.Graphic3d_CStructure) -> None:
        """Connect other structure to this one"""

    def Disconnect(self, theStructure: nanoocp.Graphic3d.Graphic3d_CStructure) -> None:
        """Disconnect other structure to this one"""

    def SetTransformation(self, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """Synchronize structure transformation"""

    def SetTransformPersistence(self, theTrsfPers: nanoocp.Graphic3d.Graphic3d_TransformPers | None) -> None:
        """Set transformation persistence."""

    def SetZLayer(self, theLayerIndex: int) -> None:
        """Set z layer ID to display the structure in specified layer"""

    def GraphicHighlight(self, theStyle: nanoocp.Graphic3d.Graphic3d_PresentationAttributes | None) -> None:
        """
        Highlights structure according to the given style and updates corresponding class fields
        (highlight status and style)
        """

    def GraphicUnhighlight(self) -> None:
        """
        Unighlights structure and updates corresponding class fields (highlight status and style)
        """

    def ShadowLink(self, theManager: nanoocp.Graphic3d.Graphic3d_StructureManager | None) -> nanoocp.Graphic3d.Graphic3d_CStructure:
        """Create shadow link to this structure"""

    def NewGroup(self, theStruct: nanoocp.Graphic3d.Graphic3d_Structure | None) -> nanoocp.Graphic3d.Graphic3d_Group:
        """Create new group within this structure"""

    def RemoveGroup(self, theGroup: nanoocp.Graphic3d.Graphic3d_Group | None) -> None:
        """Remove group from this structure"""

    def GlDriver(self) -> OpenGl_GraphicDriver:
        """Access graphic driver"""

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Renders the structure."""

    def Release(self, theGlCtx: OpenGl_Context | None) -> None:
        """Releases structure resources."""

    def ReleaseGlResources(self, theGlCtx: OpenGl_Context | None) -> None:
        """
        This method releases GL resources without actual elements destruction.
        As result structure could be correctly destroyed layer without GL context
        (after last window was closed for example).

        Notice however that reusage of this structure after calling this method is incorrect
        and will lead to broken visualization due to loosed data.
        """

    def InstancedStructure(self) -> OpenGl_Structure:
        """Returns instanced OpenGL structure."""

    def ModificationState(self) -> int:
        """Returns structure modification state (for ray-tracing)."""

    def ResetModificationState(self) -> None:
        """Resets structure modification state (for ray-tracing)."""

    def IsRaytracable(self) -> bool:
        """Is the structure ray-tracable (contains ray-tracable elements)?"""

    def updateLayerTransformation(self) -> None:
        """Update render transformation matrix."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_StructureShadow(OpenGl_Structure):
    """Dummy structure which just redirects to groups of another structure."""

    @overload
    def __init__(self, theManager: nanoocp.Graphic3d.Graphic3d_StructureManager | None, theStructure: OpenGl_Structure | None) -> None:
        """Create empty structure"""

    @overload
    def __init__(self, theOther: OpenGl_StructureShadow) -> None: ...

    def Connect(self, arg0: nanoocp.Graphic3d.Graphic3d_CStructure) -> None:
        """Raise exception on API misuse."""

    def Disconnect(self, arg0: nanoocp.Graphic3d.Graphic3d_CStructure) -> None:
        """Raise exception on API misuse."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_PointSprite(OpenGl_Texture):
    """
    Point sprite resource. On modern hardware it will be texture with extra parameters.
    On ancient hardware sprites will be drawn using bitmaps.
    """

    def __init__(self, theResourceId: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Create uninitialized resource."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any."""

    def IsPointSprite(self) -> bool:
        """Returns TRUE for point sprite texture."""

    def IsValid(self) -> bool:
        """@return true if current object was initialized"""

    def IsDisplayList(self) -> bool:
        """@return true if this is display list bitmap"""

    def DrawBitmap(self, theCtx: OpenGl_Context | None) -> None:
        """
        Draw sprite using glBitmap.
        Please call glRasterPos3fv() before to setup sprite position.
        """

    def SetDisplayList(self, theCtx: OpenGl_Context | None, theBitmapList: int) -> None:
        """Initialize point sprite as display list"""

class OpenGl_PrimitiveArray(OpenGl_Element):
    """Class for rendering of arbitrary primitive array."""

    @overload
    def __init__(self, theDriver: OpenGl_GraphicDriver) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theDriver: OpenGl_GraphicDriver, theType: nanoocp.Graphic3d.Graphic3d_TypeOfPrimitiveArray, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theAttribs: nanoocp.Graphic3d.Graphic3d_Buffer | None, theBounds: nanoocp.Graphic3d.Graphic3d_BoundBuffer | None) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: OpenGl_PrimitiveArray) -> None: ...

    DRAW_MODE_NONE: int = -1

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Render primitives to the window"""

    def Release(self, theContext: OpenGl_Context) -> None:
        """Release OpenGL resources (VBOs)"""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def UpdateDrawStats(self, theStats: nanoocp.Graphic3d.Graphic3d_FrameStatsDataTmp, theIsDetailed: bool) -> None:
        """Increment draw calls statistics."""

    def IsInitialized(self) -> bool:
        """
        Return true if VBOs initialization has been performed.
        VBO initialization is performed during first Render() call.
        Notice that this flag does not indicate VBOs validity.
        """

    def Invalidate(self) -> None:
        """Invalidate VBO content without destruction."""

    def DrawMode(self) -> int:
        """@return primitive type (GL_LINES, GL_TRIANGLES and others)"""

    def IsFillDrawMode(self) -> bool:
        """Return TRUE if primitive type generates shaded triangulation."""

    def Indices(self) -> nanoocp.Graphic3d.Graphic3d_IndexBuffer:
        """@return indices array"""

    def Attributes(self) -> nanoocp.Graphic3d.Graphic3d_Buffer:
        """@return attributes array"""

    def Bounds(self) -> nanoocp.Graphic3d.Graphic3d_BoundBuffer:
        """@return bounds array"""

    def GetUID(self) -> int:
        """Returns unique ID of primitive array."""

    def InitBuffers(self, theContext: OpenGl_Context | None, theType: nanoocp.Graphic3d.Graphic3d_TypeOfPrimitiveArray, theIndices: nanoocp.Graphic3d.Graphic3d_IndexBuffer | None, theAttribs: nanoocp.Graphic3d.Graphic3d_Buffer | None, theBounds: nanoocp.Graphic3d.Graphic3d_BoundBuffer | None) -> None:
        """Initialize indices, attributes and bounds with new data."""

    def IndexVbo(self) -> OpenGl_IndexBuffer:
        """Returns index VBO."""

    def AttributesVbo(self) -> OpenGl_VertexBuffer:
        """Returns attributes VBO."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_FrameBuffer(OpenGl_NamedResource):
    """
    Class implements FrameBuffer Object (FBO) resource
    intended for off-screen rendering.
    """

    def __init__(self, theResourceId: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Empty constructor"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def BufferDump(theGlCtx: OpenGl_Context | None, theFbo: OpenGl_FrameBuffer | None, theImage: nanoocp.Image.Image_PixMap, theBufferType: nanoocp.Graphic3d.Graphic3d_BufferType) -> bool:
        """
        Dump content into image.
        @param theGlCtx      bound OpenGL context
        @param theFbo        FBO to dump (or window buffer, if NULL)
        @param theImage      target image
        @param theBufferType buffer type (attachment) to dump
        @return TRUE on success
        """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any."""

    def NbSamples(self) -> int:
        """Number of multisampling samples."""

    def NbColorBuffers(self) -> int:
        """Number of color buffers."""

    def HasColor(self) -> bool:
        """Return true if FBO has been created with color attachment."""

    def HasDepth(self) -> bool:
        """Return true if FBO has been created with depth attachment."""

    def GetSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return textures width x height."""

    def GetSizeX(self) -> int:
        """Textures width."""

    def GetSizeY(self) -> int:
        """Textures height."""

    def GetVPSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return viewport width x height."""

    def GetVPSizeX(self) -> int:
        """Viewport width."""

    def GetVPSizeY(self) -> int:
        """Viewport height."""

    def GetInitVPSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return viewport width x height."""

    def GetInitVPSizeX(self) -> int:
        """Viewport width."""

    def GetInitVPSizeY(self) -> int:
        """Viewport height."""

    def IsValid(self) -> bool:
        """Returns true if current object was initialized"""

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthStencilTexture: OpenGl_Texture | None, theNbSamples: int = 0) -> bool:
        """
        Initialize FBO for rendering into single/multiple color buffer and depth textures.
        @param theGlCtx               currently bound OpenGL context
        @param theSize                texture width x height
        @param theColorFormats        list of color texture sized format (0 means no color
        attachment), e.g. GL_RGBA8
        @param theDepthStencilTexture depth-stencil texture
        @param theNbSamples           MSAA number of samples (0 means normal texture)
        @return true on success
        """

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormat: int, theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        Initialize FBO for rendering into textures.
        @param theGlCtx       currently bound OpenGL context
        @param theSize        texture width x height
        @param theColorFormat color         texture sized format (0 means no color attachment), e.g.
        GL_RGBA8
        @param theDepthFormat depth-stencil texture sized format (0 means no depth attachment), e.g.
        GL_DEPTH24_STENCIL8
        @param theNbSamples   MSAA number of samples (0 means normal texture)
        @return true on success
        """

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        Initialize FBO for rendering into single/multiple color buffer and depth textures.
        @param theGlCtx        currently bound OpenGL context
        @param theSize         texture width x height
        @param theColorFormats list of color texture sized format (0 means no color attachment), e.g.
        GL_RGBA8
        @param theDepthFormat  depth-stencil texture sized format (0 means no depth attachment), e.g.
        GL_DEPTH24_STENCIL8
        @param theNbSamples    MSAA number of samples (0 means normal texture)
        @return true on success
        """

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSizeX: int, theSizeY: int, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthStencilTexture: OpenGl_Texture | None, theNbSamples: int = 0) -> bool: ...

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSizeX: int, theSizeY: int, theColorFormat: int, theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        Deprecated in OCCT: Obsolete method, use Init() taking NCollection_Vec2<int>

        Initialize FBO for rendering into textures.
        """

    @overload
    def Init(self, theGlCtx: OpenGl_Context | None, theSizeX: int, theSizeY: int, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        Deprecated in OCCT: Obsolete method, use Init() taking NCollection_Vec2<int>

        Initialize FBO for rendering into single/multiple color buffer and depth textures.
        """

    @overload
    def InitLazy(self, theGlCtx: OpenGl_Context | None, theViewportSize: nanoocp.BVH.BVH_Vec2i, theColorFormat: int, theDepthFormat: int, theNbSamples: int = 0) -> bool: ...

    @overload
    def InitLazy(self, theGlCtx: OpenGl_Context | None, theViewportSize: nanoocp.BVH.BVH_Vec2i, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """(Re-)initialize FBO with specified dimensions."""

    @overload
    def InitLazy(self, theGlCtx: OpenGl_Context | None, theFbo: OpenGl_FrameBuffer, theToKeepMsaa: bool = True) -> bool:
        """(Re-)initialize FBO with properties taken from another FBO."""

    @overload
    def InitLazy(self, theGlCtx: OpenGl_Context | None, theViewportSizeX: int, theViewportSizeY: int, theColorFormat: int, theDepthFormat: int, theNbSamples: int = 0) -> bool: ...

    @overload
    def InitLazy(self, theGlCtx: OpenGl_Context | None, theViewportSizeX: int, theViewportSizeY: int, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        Deprecated in OCCT: Obsolete method, use InitLazy() taking NCollection_Vec2<int>

        (Re-)initialize FBO with specified dimensions.
        """

    def InitRenderBuffer(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int = 0) -> bool:
        """
        (Re-)initialize FBO with specified dimensions.
        The Render Buffer Objects will be used for Color, Depth and Stencil attachments (as opposite
        to textures).
        @param theGlCtx        currently bound OpenGL context
        @param theSize         render buffer width x height
        @param theColorFormats list of color render buffer sized format, e.g. GL_RGBA8; list should
        define only one element
        @param theDepthFormat  depth-stencil render buffer sized format, e.g. GL_DEPTH24_STENCIL8
        @param theNbSamples    MSAA number of samples (0 means normal render buffer)
        """

    @overload
    def InitWithRB(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormat: int, theDepthFormat: int, theColorRBufferFromWindow: int) -> bool:
        """
        (Re-)initialize FBO with specified dimensions.
        The Render Buffer Objects will be used for Color, Depth and Stencil attachments (as opposite
        to textures).
        @param theGlCtx       currently bound OpenGL context
        @param theSize        render buffer width x height
        @param theColorFormat color         render buffer sized format, e.g. GL_RGBA8
        @param theDepthFormat depth-stencil render buffer sized format, e.g. GL_DEPTH24_STENCIL8
        @param theColorRBufferFromWindow should be ID of already initialized RB object, which will be
        released within this class
        """

    @overload
    def InitWithRB(self, theGlCtx: OpenGl_Context | None, theSizeX: int, theSizeY: int, theColorFormat: int, theDepthFormat: int, theColorRBufferFromWindow: int = 0) -> bool:
        """
        Deprecated in OCCT: Obsolete method, use InitWithRB() taking NCollection_Vec2<int>

        (Re-)initialize FBO with specified dimensions.
        The Render Buffer Objects will be used for Color, Depth and Stencil attachments (as opposite
        to textures).
        """

    @overload
    def InitWrapper(self, theGlCtx: OpenGl_Context | None) -> bool:
        """
        Initialize class from currently bound FBO.
        Retrieved OpenGL objects will not be destroyed on Release.
        """

    @overload
    def InitWrapper(self, theGlContext: OpenGl_Context | None, theColorTextures: nanoocp.NCollection.NCollection_Sequence[nanoocp.OpenGl.OpenGl_Texture], theDepthTexture: OpenGl_Texture | None = None) -> bool:
        """Wrap existing color textures."""

    def SetupViewport(self, theGlCtx: OpenGl_Context | None) -> None:
        """Setup viewport to render into FBO"""

    def ChangeViewport(self, theVPSizeX: int, theVPSizeY: int) -> None:
        """Override viewport settings"""

    def BindBuffer(self, theGlCtx: OpenGl_Context | None) -> None:
        """
        Bind frame buffer for drawing and reading (to render into the texture).
        """

    def BindDrawBuffer(self, theGlCtx: OpenGl_Context | None) -> None:
        """
        Bind frame buffer for drawing GL_DRAW_FRAMEBUFFER (to render into the texture).
        """

    def BindReadBuffer(self, theGlCtx: OpenGl_Context | None) -> None:
        """Bind frame buffer for reading GL_READ_FRAMEBUFFER"""

    def UnbindBuffer(self, theGlCtx: OpenGl_Context | None) -> None:
        """Unbind frame buffer."""

    def ColorTexture(self, theColorBufferIndex: int = 0) -> OpenGl_Texture:
        """Returns the color texture for the given color buffer index."""

    def DepthStencilTexture(self) -> OpenGl_Texture:
        """Returns the depth-stencil texture."""

    def IsColorRenderBuffer(self) -> bool:
        """Returns TRUE if color Render Buffer is defined."""

    def ColorRenderBuffer(self) -> int:
        """Returns the color Render Buffer."""

    def IsDepthStencilRenderBuffer(self) -> bool:
        """Returns TRUE if depth Render Buffer is defined."""

    def DepthStencilRenderBuffer(self) -> int:
        """Returns the depth Render Buffer."""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def initRenderBuffer(self, theGlCtx: OpenGl_Context | None, theSize: nanoocp.BVH.BVH_Vec2i, theColorFormats: nanoocp.NCollection.NCollection_DynamicArray[int], theDepthFormat: int, theNbSamples: int, theColorRBufferFromWindow: int) -> bool:
        """
        (Re-)initialize FBO with specified dimensions.
        The Render Buffer Objects will be used for Color, Depth and Stencil attachments (as opposite
        to textures).
        @param theGlCtx        currently bound OpenGL context
        @param theSize         render buffer width x height
        @param theColorFormats list of color render buffer sized format, e.g. GL_RGBA8
        @param theDepthFormat  depth-stencil render buffer sized format, e.g. GL_DEPTH24_STENCIL8
        @param theNbSamples    MSAA number of samples (0 means normal render buffer)
        @param theColorRBufferFromWindow when specified - should be ID of already initialized RB
        object, which will be released within this class
        """

class OpenGl_GraduatedTrihedron(OpenGl_Element):
    """
    This class allows to render Graduated Trihedron, i.e. trihedron with grid.
    it is based on Graphic3d_GraduatedTrihedron parameters and support its customization
    on construction level only.
    @sa Graphic3d_GraduatedTrihedron
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: OpenGl_GraduatedTrihedron) -> None: ...

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Draw the element."""

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Release OpenGL resources."""

    def SetValues(self, theData: nanoocp.Graphic3d.Graphic3d_GraduatedTrihedron) -> None:
        """Setup configuration."""

    def SetMinMax(self, theMin: nanoocp.Quantity.NCollection_Vec3__float, theMax: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Sets up-to-date values of scene bounding box.
        Can be used in callback mechanism to get up-to-date values.
        @sa Graphic3d_GraduatedTrihedron::CubicAxesCallback
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_LayerList:
    """Class defining the list of layers."""

    @overload
    def __init__(self) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: OpenGl_LayerList) -> None: ...

    def NbPriorities(self) -> int:
        """Method returns the number of available priorities"""

    def NbStructures(self) -> int:
        """Number of displayed structures"""

    def NbImmediateStructures(self) -> int:
        """Return number of structures within immediate layers"""

    def InsertLayerBefore(self, theNewLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerAfter: int) -> None:
        """Insert a new layer with id."""

    def InsertLayerAfter(self, theNewLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerBefore: int) -> None:
        """Insert a new layer with id."""

    def RemoveLayer(self, theLayerId: int) -> None:
        """Remove layer by its id."""

    def AddStructure(self, theStruct: OpenGl_Structure, theLayerId: int, thePriority: nanoocp.Graphic3d.Graphic3d_DisplayPriority, isForChangePriority: bool = False) -> None:
        """
        Add structure to list with given priority. The structure will be inserted
        to specified layer. If the layer isn't found, the structure will be put
        to default bottom-level layer.
        """

    def RemoveStructure(self, theStructure: OpenGl_Structure) -> None:
        """Remove structure from structure list and return its previous priority"""

    def ChangeLayer(self, theStructure: OpenGl_Structure, theOldLayerId: int, theNewLayerId: int) -> None:
        """
        Change structure z layer
        If the new layer is not presented, the structure will be displayed
        in default z layer
        """

    def ChangePriority(self, theStructure: OpenGl_Structure, theLayerId: int, theNewPriority: nanoocp.Graphic3d.Graphic3d_DisplayPriority) -> None:
        """Changes structure priority within its ZLayer"""

    def Layer(self, theLayerId: int) -> nanoocp.Graphic3d.Graphic3d_Layer:
        """Returns reference to the layer with given ID."""

    def SetLayerSettings(self, theLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings) -> None:
        """Assign new settings to the layer."""

    def UpdateCulling(self, theWorkspace: OpenGl_Workspace | None, theToDrawImmediate: bool) -> None:
        """Update culling state - should be called before rendering."""

    def Render(self, theWorkspace: OpenGl_Workspace | None, theToDrawImmediate: bool, theFilterMode: OpenGl_LayerFilter, theLayersToProcess: int, theReadDrawFbo: OpenGl_FrameBuffer, theOitAccumFbo: OpenGl_FrameBuffer) -> None:
        """Render this element"""

    def Layers(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_Layer]:
        """Returns the set of OpenGL Z-layers."""

    def LayerIDs(self) -> nanoocp.NCollection.NCollection_DataMap[int, nanoocp.Graphic3d.Graphic3d_Layer]:
        """Returns the map of Z-layer IDs to indexes."""

    def InvalidateBVHData(self, theLayerId: int) -> None:
        """
        Marks BVH tree for given priority list as dirty and
        marks primitive set for rebuild.
        """

    def ModificationStateOfRaytracable(self) -> int:
        """Returns structure modification state (for ray-tracing)."""

    def FrustumCullingBVHBuilder(self) -> nanoocp.BVH.BVH_Builder3d:
        """Returns BVH tree builder for frustum culling."""

    def SetFrustumCullingBVHBuilder(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Assigns BVH tree builder for frustum culling."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_RaytraceMaterial:
    """Stores properties of surface material."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_RaytraceMaterial) -> None: ...

    class Physical:
        """Physically-based material properties (used in path tracing engine)."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, theOther: OpenGl_RaytraceMaterial.Physical) -> None: ...

        @property
        def Kc(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Weight of coat specular/glossy BRDF"""

        @Kc.setter
        def Kc(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def Kd(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Weight of base diffuse BRDF"""

        @Kd.setter
        def Kd(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def Ks(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Weight of base specular/glossy BRDF"""

        @Ks.setter
        def Ks(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def Kt(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Weight of base specular/glossy BTDF"""

        @Kt.setter
        def Kt(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def Le(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Radiance emitted by the surface"""

        @Le.setter
        def Le(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def FresnelCoat(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Fresnel coefficients of coat layer"""

        @FresnelCoat.setter
        def FresnelCoat(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def FresnelBase(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Fresnel coefficients of base layer"""

        @FresnelBase.setter
        def FresnelBase(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

        @property
        def Absorption(self) -> nanoocp.Quantity.NCollection_Vec4__float:
            """Absorption color/intensity"""

        @Absorption.setter
        def Absorption(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Ambient(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Ambient reflection coefficient"""

    @Ambient.setter
    def Ambient(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Diffuse(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Diffuse reflection coefficient"""

    @Diffuse.setter
    def Diffuse(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Specular(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Glossy  reflection coefficient"""

    @Specular.setter
    def Specular(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Emission(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Material emission"""

    @Emission.setter
    def Emission(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Reflection(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Specular reflection coefficient"""

    @Reflection.setter
    def Reflection(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Refraction(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Specular refraction coefficient"""

    @Refraction.setter
    def Refraction(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Transparency(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Material transparency"""

    @Transparency.setter
    def Transparency(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def TextureTransform(self) -> nanoocp.BVH.BVH_Mat4f:
        """Texture transformation matrix"""

    @TextureTransform.setter
    def TextureTransform(self, arg: nanoocp.BVH.BVH_Mat4f, /) -> None: ...

    @property
    def BSDF(self) -> OpenGl_RaytraceMaterial.Physical: ...

    @BSDF.setter
    def BSDF(self, arg: OpenGl_RaytraceMaterial.Physical, /) -> None: ...

class OpenGl_RaytraceLight:
    """Stores properties of OpenGL light source."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theEmission: nanoocp.Quantity.NCollection_Vec4__float, thePosition: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Creates new light source."""

    @overload
    def __init__(self, theOther: OpenGl_RaytraceLight) -> None: ...

    @property
    def Emission(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Diffuse intensity (in terms of OpenGL)"""

    @Emission.setter
    def Emission(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Position(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Position of light source (in terms of OpenGL)"""

    @Position.setter
    def Position(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

class BVH_Object__float__3(nanoocp.BVH.BVH_ObjectTransient):
    """
    Abstract geometric object bounded by BVH box.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    def Box(self) -> BVH_Box__float__3:
        """Returns AABB of the geometric object."""

class BVH_Set__float__3:
    """
    Set of abstract entities (bounded by BVH boxes). This is
    the minimal geometry interface needed to construct BVH.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def Box(self) -> BVH_Box__float__3:
        """Returns AABB of the entire set of objects."""

    @overload
    def Box(self, theIndex: int) -> BVH_Box__float__3:
        """Returns AABB of the given object."""

    def Size(self) -> int:
        """Returns total number of objects."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """Returns centroid position along the given axis."""

    def Swap(self, theIndex1: int, theIndex2: int) -> None:
        """Performs transposing the two given objects in the set."""

class BVH_PrimitiveSet__float__3(BVH_Object__float__3):
    """
    Set of abstract geometric primitives organized with bounding
    volume hierarchy (BVH). Unlike an object set, this collection
    is designed for storing structural elements of a single object
    (such as triangles in the object triangulation). Because there
    may be a large number of such elements, the implementations of
    this interface should be sufficiently optimized.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    def Box(self) -> BVH_Box__float__3:
        """Returns AABB of primitive set."""

    def BVH(self) -> "BVH_Tree<float, 3, BVH_BinaryTree>":
        """Returns BVH tree (and builds it if necessary)."""

    def Builder(self) -> BVH_Builder__float__3:
        """Returns the method (builder) used to construct BVH."""

    def SetBuilder(self, theBuilder: BVH_Builder__float__3 | None) -> None:
        """Sets the method (builder) used to construct BVH."""

class OpenGl_BVHTriangulation3f(BVH_PrimitiveSet__float__3):
    """
    Triangulation as an example of BVH primitive set.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theBuilder: BVH_Builder__float__3 | None) -> None:
        """Creates empty triangulation."""

    @overload
    def __init__(self, theOther: OpenGl_BVHTriangulation3f) -> None: ...

    def Size(self) -> int:
        """Returns total number of triangles."""

    def Box(self, theIndex: int) -> BVH_Box__float__3:
        """Returns AABB of the given triangle."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """Returns centroid position along the given axis."""

    def Swap(self, theIndex1: int, theIndex2: int) -> None:
        """Performs transposing the two given triangles in the set."""

    @property
    def Vertices(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float]:
        """Array of vertex coordinates."""

    @Vertices.setter
    def Vertices(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float], /) -> None: ...

    @property
    def Elements(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec4i]:
        """Array of indices of triangle vertices."""

    @Elements.setter
    def Elements(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.BVH.BVH_Vec4i], /) -> None: ...

class OpenGl_TriangleSet(OpenGl_BVHTriangulation3f):
    """Triangulation of single OpenGL primitive array."""

    @overload
    def __init__(self, theArrayID: int, theBuilder: BVH_Builder__float__3 | None) -> None:
        """Creates new OpenGL element triangulation."""

    @overload
    def __init__(self, theOther: OpenGl_TriangleSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AssociatedPArrayID(self) -> int:
        """Returns ID of associated primitive array."""

    def MaterialIndex(self) -> int:
        """Returns material index of triangle set."""

    def SetMaterialIndex(self, theMatID: int) -> None:
        """Sets material index for entire triangle set."""

    @overload
    def Box(self) -> BVH_Box__float__3:
        """Returns AABB of primitive set."""

    @overload
    def Box(self, theIndex: int) -> BVH_Box__float__3:
        """Returns AABB of the given triangle."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """Returns centroid position along the given axis."""

    def QuadBVH(self) -> BVH_Tree__float__3__BVH_QuadTree:
        """Returns quad BVH (QBVH) tree produced from binary BVH."""

    @property
    def Normals(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float]:
        """Array of vertex normals."""

    @Normals.setter
    def Normals(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Quantity.NCollection_Vec3__float], /) -> None: ...

    @property
    def TexCrds(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.NCollection_Vec2__float]:
        """Array of texture coords."""

    @TexCrds.setter
    def TexCrds(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.Poly.NCollection_Vec2__float], /) -> None: ...

class BVH_ObjectSet__float__3(BVH_Set__float__3):
    """
    Array of abstract entities (bounded by BVH boxes) to built BVH.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None:
        """Creates new set of geometric objects."""

    @overload
    def __init__(self, theOther: BVH_ObjectSet__float__3) -> None: ...

    def Clear(self) -> None:
        """Removes all geometric objects."""

    def Objects(self) -> "NCollection_DynamicArray<opencascade::handle<BVH_Object<float, 3>>>":
        """Returns reference to the array of geometric objects."""

    def Size(self) -> int:
        """Return total number of objects."""

    def Box(self, theIndex: int) -> BVH_Box__float__3:
        """Returns AABB of the given object."""

    def Center(self, theIndex: int, theAxis: int) -> float:
        """Returns centroid position along the given axis."""

    def Swap(self, theIndex1: int, theIndex2: int) -> None:
        """Performs transposing the two given objects in the set."""

class BVH_Geometry__float__3(BVH_ObjectSet__float__3):
    """
    BVH geometry as a set of abstract geometric objects
    organized with bounding volume hierarchy (BVH).
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theBuilder: BVH_Builder__float__3 | None) -> None:
        """Creates uninitialized BVH geometry."""

    @overload
    def __init__(self, theOther: BVH_Geometry__float__3) -> None: ...

    def IsDirty(self) -> bool:
        """Returns TRUE if geometry state should be updated."""

    def MarkDirty(self) -> None:
        """Marks geometry as outdated."""

    def Box(self) -> BVH_Box__float__3:
        """Returns AABB of the whole geometry."""

    def BVH(self) -> "BVH_Tree<float, 3, BVH_BinaryTree>":
        """Returns BVH tree (and builds it if necessary)."""

    def Builder(self) -> BVH_Builder__float__3:
        """Returns the method (builder) used to construct BVH."""

    def SetBuilder(self, theBuilder: BVH_Builder__float__3 | None) -> None:
        """Sets the method (builder) used to construct BVH."""

class OpenGl_RaytraceGeometry(BVH_Geometry__float__3):
    """Stores geometry of ray-tracing scene."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized ray-tracing geometry."""

    @overload
    def __init__(self, theOther: OpenGl_RaytraceGeometry) -> None: ...

    def ClearMaterials(self) -> None:
        """Clears only ray-tracing materials."""

    def Clear(self) -> None:
        """Clears ray-tracing geometry."""

    def ProcessAcceleration(self) -> bool:
        """
        @name methods related to acceleration structure
        Performs post-processing of high-level scene BVH.
        """

    def AccelerationOffset(self, theNodeIdx: int) -> int:
        """
        Returns offset of bottom-level BVH for given leaf node.
        If the node index is not valid the function returns -1.
        @note Can be used after processing acceleration structure.
        """

    def VerticesOffset(self, theNodeIdx: int) -> int:
        """
        Returns offset of triangulation vertices for given leaf node.
        If the node index is not valid the function returns -1.
        @note Can be used after processing acceleration structure.
        """

    def ElementsOffset(self, theNodeIdx: int) -> int:
        """
        Returns offset of triangulation elements for given leaf node.
        If the node index is not valid the function returns -1.
        @note Can be used after processing acceleration structure.
        """

    def TriangleSet(self, theNodeIdx: int) -> OpenGl_TriangleSet:
        """
        Returns triangulation data for given leaf node.
        If the node index is not valid the function returns NULL.
        @note Can be used after processing acceleration structure.
        """

    def QuadBVH(self) -> BVH_Tree__float__3__BVH_QuadTree:
        """Returns quad BVH (QBVH) tree produced from binary BVH."""

    def HasTextures(self) -> bool:
        """
        @name methods related to texture management
        Checks if scene contains textured objects.
        """

    def AddTexture(self, theTexture: OpenGl_Texture | None) -> int:
        """Adds new OpenGL texture to the scene and returns its index."""

    def UpdateTextureHandles(self, theContext: OpenGl_Context | None) -> bool:
        """Updates unique 64-bit texture handles to use in shaders."""

    def AcquireTextures(self, theContext: OpenGl_Context | None) -> bool:
        """
        Makes the OpenGL texture handles resident (must be called before using).
        """

    def ReleaseTextures(self, theContext: OpenGl_Context | None) -> bool:
        """
        Makes the OpenGL texture handles non-resident (must be called after using).
        """

    def TextureHandles(self) -> nanoocp.NCollection.NCollection_LinearVector__unsigned_long_long:
        """Returns array of texture handles."""

    def ReleaseResources(self, arg0: OpenGl_Context | None) -> None:
        """Releases OpenGL resources."""

    def TopLevelTreeDepth(self) -> int:
        """
        @name auxiliary methods
        Returns depth of top-level scene BVH from last build.
        """

    def BotLevelTreeDepth(self) -> int:
        """Returns maximum depth of bottom-level scene BVHs from last build."""

    @property
    def Sources(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.OpenGl.OpenGl_RaytraceLight]:
        """Array of properties of light sources."""

    @Sources.setter
    def Sources(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.OpenGl.OpenGl_RaytraceLight], /) -> None: ...

    @property
    def Materials(self) -> nanoocp.NCollection.NCollection_LinearVector[nanoocp.OpenGl.OpenGl_RaytraceMaterial]:
        """Array of 'front' material properties."""

    @Materials.setter
    def Materials(self, arg: nanoocp.NCollection.NCollection_LinearVector[nanoocp.OpenGl.OpenGl_RaytraceMaterial], /) -> None: ...

    @property
    def Ambient(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Global ambient from all light sources."""

    @Ambient.setter
    def Ambient(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

class OpenGl_HaltonSampler:
    """
    Compute points of the Halton sequence with digit-permutations for different bases.
    """

    @overload
    def __init__(self) -> None:
        """Init the permutation arrays using Faure-permutations."""

    @overload
    def __init__(self, theOther: OpenGl_HaltonSampler) -> None: ...

    @staticmethod
    def get_num_dimensions() -> int:
        """Return the number of supported dimensions."""

    def sample(self, theDimension: int, theIndex: int) -> float:
        """
        Return the Halton sample for the given dimension (component) and index.
        The client must have called initFaure() at least once before.
        dimension must be smaller than the value returned by get_num_dimensions().
        """

class OpenGl_TileSampler:
    """
    Tool object used for sampling screen tiles according to estimated pixel variance (used in path
    tracing engine). To improve GPU thread coherency, rendering window is split into pixel blocks or
    tiles. The important feature of this approach is that it is possible to keep the same number of
    tiles for any screen resolution (e.g. 256 tiles can be used for both 512 x 512 window and 1920 x
    1080 window). So, a smaller number of tiles allows to increase interactivity (FPS), but at the
    cost of higher per-frame variance ('noise'). On the contrary a larger number of tiles decrease
    interactivity, but leads to lower per-frame variance. Note that the total time needed to produce
    final final image is the same for both cases.
    """

    @overload
    def __init__(self) -> None:
        """Creates new tile sampler."""

    @overload
    def __init__(self, theOther: OpenGl_TileSampler) -> None: ...

    def TileSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Size of individual tile in pixels."""

    def VarianceScaleFactor(self) -> float:
        """
        Scale factor for quantization of visual error (float) into signed integer.
        """

    def NbTilesX(self) -> int:
        """Returns number of tiles in X dimension."""

    def NbTilesY(self) -> int:
        """Returns number of tiles in Y dimension."""

    def NbTiles(self) -> int:
        """Returns total number of tiles in viewport."""

    def ViewSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Returns ray-tracing viewport."""

    def NbOffsetTiles(self, theAdaptive: bool) -> nanoocp.BVH.BVH_Vec2i:
        """Number of tiles within offsets texture."""

    def NbOffsetTilesMax(self) -> nanoocp.BVH.BVH_Vec2i:
        """Maximum number of tiles within offsets texture."""

    def OffsetTilesViewport(self, theAdaptive: bool) -> nanoocp.BVH.BVH_Vec2i:
        """Viewport for rendering using offsets texture."""

    def OffsetTilesViewportMax(self) -> nanoocp.BVH.BVH_Vec2i:
        """Maximum viewport for rendering using offsets texture."""

    def MaxTileSamples(self) -> int:
        """Return maximum number of samples per tile."""

    def SetSize(self, theParams: nanoocp.Graphic3d.Graphic3d_RenderingParams, theSize: nanoocp.BVH.BVH_Vec2i) -> None:
        """Specifies size of ray-tracing viewport and recomputes tile size."""

    def GrabVarianceMap(self, theContext: OpenGl_Context | None, theTexture: OpenGl_Texture | None) -> None:
        """
        Fetches current error estimation from the GPU and
        builds 2D discrete distribution for tile sampling.
        """

    def Reset(self) -> None:
        """Resets (restart) tile sampler to initial state."""

    def UploadSamples(self, theContext: OpenGl_Context | None, theSamplesTexture: OpenGl_Texture | None, theAdaptive: bool) -> bool:
        """Uploads tile samples to the given OpenGL texture."""

    def UploadOffsets(self, theContext: OpenGl_Context | None, theOffsetsTexture: OpenGl_Texture | None, theAdaptive: bool) -> bool:
        """Uploads offsets of sampled tiles to the given OpenGL texture."""

class OpenGl_View(nanoocp.Graphic3d.Graphic3d_CView):
    """Implementation of OpenGl view."""

    def __init__(self, theMgr: nanoocp.Graphic3d.Graphic3d_StructureManager | None, theDriver: OpenGl_GraphicDriver | None, theCaps: OpenGl_Caps | None, theCounter: OpenGl_StateCounter) -> None:
        """Constructor."""

    def ReleaseGlResources(self, theCtx: OpenGl_Context | None) -> None:
        """Release OpenGL resources."""

    def Remove(self) -> None:
        """Deletes and erases the view."""

    def SetImmediateModeDrawToFront(self, theDrawToFrontBuffer: bool) -> bool:
        """
        @param theDrawToFrontBuffer Advanced option to modify rendering mode:
        1. TRUE.  Drawing immediate mode structures directly to the front buffer over the scene image.
        Fast, so preferred for interactive work (used by default).
        However these extra drawings will be missed in image dump since it is performed from back
        buffer. Notice that since no pre-buffering used the V-Sync will be ignored and rendering could
        be seen in run-time (in case of slow hardware) and/or tearing may appear. So this is strongly
        recommended to draw only simple (fast) structures.
        2. FALSE. Drawing immediate mode structures to the back buffer.
        The complete scene is redrawn first, so this mode is slower if scene contains complex data
        and/or V-Sync is turned on. But it works in any case and is especially useful for view dump
        because the dump image is read from the back buffer.
        @return previous mode.
        """

    def Window(self) -> nanoocp.Aspect.Aspect_Window:
        """Returns window associated with the view."""

    def IsDefined(self) -> bool:
        """Returns True if the window associated to the view is defined."""

    def Resized(self) -> None:
        """Handle changing size of the rendering window."""

    def Redraw(self) -> None:
        """Redraw content of the view."""

    def RedrawImmediate(self) -> None:
        """Redraw immediate content of the view."""

    def Invalidate(self) -> None:
        """
        Marks BVH tree for given priority list as dirty and marks primitive set for rebuild.
        """

    def IsInvalidated(self) -> bool:
        """Return true if view content cache has been invalidated."""

    def BufferDump(self, theImage: nanoocp.Image.Image_PixMap, theBufferType: nanoocp.Graphic3d.Graphic3d_BufferType) -> bool:
        """
        Dump active rendering buffer into specified memory buffer.
        In Ray-Tracing allow to get a raw HDR buffer using Graphic3d_BT_RGB_RayTraceHdrLeft buffer
        type, only Left view will be dumped ignoring stereoscopic parameter.
        """

    def ShadowMapDump(self, theImage: nanoocp.Image.Image_PixMap, theLightName: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Dumps the graphical contents of a shadowmap framebuffer into an image.
        @param theImage the image to store the shadow map.
        @param[in] theLightName  name of the light used to generate the shadow map.
        """

    def InvalidateBVHData(self, theLayerId: int) -> None:
        """
        Marks BVH tree and the set of BVH primitives of correspondent priority list with id theLayerId
        as outdated.
        """

    def InsertLayerBefore(self, theLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerAfter: int) -> None:
        """
        Add a layer to the view.
        @param[in] theNewLayerId  id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings    new layer settings
        @param[in] theLayerAfter  id of layer to append new layer before
        """

    def InsertLayerAfter(self, theNewLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings, theLayerBefore: int) -> None:
        """
        Add a layer to the view.
        @param[in] theNewLayerId   id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings     new layer settings
        @param[in] theLayerBefore  id of layer to append new layer after
        """

    def RemoveZLayer(self, theLayerId: int) -> None:
        """Remove a z layer with the given ID."""

    def SetZLayerSettings(self, theLayerId: int, theSettings: nanoocp.Graphic3d.Graphic3d_ZLayerSettings) -> None:
        """Sets the settings for a single Z layer of specified view."""

    def ZLayerMax(self) -> int:
        """
        Returns the maximum Z layer ID.
        First layer ID is Graphic3d_ZLayerId_Default, last ID is ZLayerMax().
        """

    def Layers(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_Layer]:
        """Returns the list of layers."""

    def Layer(self, theLayerId: int) -> nanoocp.Graphic3d.Graphic3d_Layer:
        """Returns layer with given ID or NULL if undefined."""

    def MinMaxValues(self, theToIncludeAuxiliary: bool) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns the bounding box of all structures displayed in the view.
        If theToIncludeAuxiliary is TRUE, then the boundary box also includes minimum and maximum
        limits of graphical elements forming parts of infinite and other auxiliary structures.
        @param theToIncludeAuxiliary consider also auxiliary presentations (with infinite flag or with
        trihedron transformation persistence)
        @return computed bounding box
        """

    def ZFitAllBounds(self, thePrimaryBox: nanoocp.Bnd.Bnd_Box, theGraphicBox: nanoocp.Bnd.Bnd_Box) -> None:
        """Return primary and graphical bounding boxes used by camera Z fitting."""

    def FBO(self) -> nanoocp.Standard.Standard_Transient:
        """Returns pointer to an assigned framebuffer object."""

    def SetFBO(self, theFbo: nanoocp.Standard.Standard_Transient | None) -> None:
        """Sets framebuffer object for offscreen rendering."""

    def FBOCreate(self, theWidth: int, theHeight: int) -> nanoocp.Standard.Standard_Transient:
        """
        Generate offscreen FBO in the graphic library.
        If not supported on hardware returns NULL.
        """

    def FBORelease(self) -> nanoocp.Standard.Standard_Transient:
        """Remove offscreen FBO from the graphic library"""

    def FBOGetDimensions(self, theFbo: nanoocp.Standard.Standard_Transient | None) -> tuple[int, int, int, int]:
        """Read offscreen FBO configuration."""

    def FBOChangeViewport(self, theFbo: nanoocp.Standard.Standard_Transient | None, theWidth: int, theHeight: int) -> None:
        """Change offscreen FBO viewport."""

    def DepthPeelingFbos(self) -> OpenGl_DepthPeeling:
        """Returns additional buffers for depth peeling OIT."""

    def GradientBackground(self) -> nanoocp.Aspect.Aspect_GradientBackground:
        """Returns gradient background fill colors."""

    def SetGradientBackground(self, theBackground: nanoocp.Aspect.Aspect_GradientBackground) -> None:
        """Sets gradient background fill colors."""

    def SetBackgroundImage(self, theTextureMap: nanoocp.Graphic3d.Graphic3d_TextureMap | None, theToUpdatePBREnv: bool = True) -> None:
        """
        Sets image texture or environment cubemap as background.
        @param[in] theTextureMap  source to set a background;
        should be either Graphic3d_Texture2D or Graphic3d_CubeMap
        @param[in] theToUpdatePBREnv  defines whether IBL maps will be generated or not
        (see GeneratePBREnvironment())
        """

    def SetTextureEnv(self, theTextureEnv: nanoocp.Graphic3d.Graphic3d_TextureEnv | None) -> None:
        """Sets environment texture for the view."""

    def BackgroundImageStyle(self) -> nanoocp.Aspect.Aspect_FillMethod:
        """Returns background image fill style."""

    def SetBackgroundImageStyle(self, theFillStyle: nanoocp.Aspect.Aspect_FillMethod) -> None:
        """Sets background image fill style."""

    def SetImageBasedLighting(self, theToEnableIBL: bool) -> None:
        """
        Enables or disables IBL (Image Based Lighting) from background cubemap.
        Has no effect if PBR is not used.
        @param[in] theToEnableIBL enable or disable IBL from background cubemap
        """

    def GridDisplay(self, theParams: nanoocp.Aspect.Aspect_GridParams, thePlane: nanoocp.gp.gp_Ax3) -> None:
        """Display a shader-rendered grid on the given plane."""

    def GridErase(self) -> None:
        """Erase the shader-rendered grid."""

    @overload
    def ShaderGridEcho(self, theX: int, theY: int, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """
        Return snapped point for the shader-rendered grid under the window pixel.
        """

    @overload
    def ShaderGridEcho(self, theX: int, theY: int, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex, theDisplayPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """
        Return snapped point and clip-safe display point for the shader-rendered grid echo marker.
        """

    def ShaderGridSnapPoint(self, thePoint: nanoocp.Graphic3d.Graphic3d_Vertex, theGridPoint: nanoocp.Graphic3d.Graphic3d_Vertex) -> bool:
        """
        Return snapped point for the shader-rendered grid from an arbitrary world point.
        """

    def SpecIBLMapLevels(self) -> int:
        """
        Returns number of mipmap levels used in specular IBL map.
        0 if PBR environment is not created.
        """

    def LocalOrigin(self) -> nanoocp.gp.gp_XYZ:
        """
        Returns local camera origin currently set for rendering, might be modified during rendering.
        """

    def SetLocalOrigin(self, theOrigin: nanoocp.gp.gp_XYZ) -> None:
        """Setup local camera origin currently set for rendering."""

    def Lights(self) -> nanoocp.Graphic3d.Graphic3d_LightSet:
        """Returns list of lights of the view."""

    def SetLights(self, theLights: nanoocp.Graphic3d.Graphic3d_LightSet | None) -> None:
        """Sets list of lights for the view."""

    def ClipPlanes(self) -> nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane:
        """Returns list of clip planes set for the view."""

    def SetClipPlanes(self, thePlanes: nanoocp.Graphic3d.Graphic3d_SequenceOfHClipPlane | None) -> None:
        """Sets list of clip planes for the view."""

    def DiagnosticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theFlags: nanoocp.Graphic3d.Graphic3d_DiagnosticInfo) -> None:
        """
        Fill in the dictionary with diagnostic info.
        Should be called within rendering thread.

        This API should be used only for user output or for creating automated reports.
        The format of returned information (e.g. key-value layout)
        is NOT part of this API and can be changed at any time.
        Thus application should not parse returned information to weed out specific parameters.
        """

    @overload
    def StatisticInformation(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns string with statistic performance info."""

    @overload
    def StatisticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Fills in the dictionary with statistic performance info."""

    def BackgroundColor(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Returns background color."""

    def ChangeGraduatedTrihedron(self) -> OpenGl_GraduatedTrihedron:
        """Change graduated trihedron."""

    def LayerList(self) -> OpenGl_LayerList:
        """Returns list of OpenGL Z-layers."""

    def GlWindow(self) -> OpenGl_Window:
        """Returns OpenGL window implementation."""

    def GlTextureEnv(self) -> OpenGl_TextureSet:
        """Returns OpenGL environment map."""

    def BVHTreeSelector(self) -> nanoocp.Graphic3d.Graphic3d_CullingTool:
        """
        Returns selector for BVH tree, providing a possibility to store information
        about current view volume and to detect which objects are overlapping it.
        """

    def HasImmediateStructures(self) -> bool:
        """Returns true if there are immediate structures to display"""

    def GraduatedTrihedronDisplay(self, theTrihedronData: nanoocp.Graphic3d.Graphic3d_GraduatedTrihedron) -> None:
        """
        @name obsolete Graduated Trihedron functionality
        Displays Graduated Trihedron.
        """

    def GraduatedTrihedronErase(self) -> None:
        """Erases Graduated Trihedron."""

    def GraduatedTrihedronMinMaxValues(self, theMin: nanoocp.Quantity.NCollection_Vec3__float, theMax: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Sets minimum and maximum points of scene bounding box for Graduated Trihedron stored in
        graphic view object.
        @param[in] theMin  the minimum point of scene.
        @param[in] theMax  the maximum point of scene.
        """

    def ToFlipOutput(self) -> bool:
        """Returns necessity to flip OY in projection matrix"""

    def SetToFlipOutput(self, theFlip: bool) -> None:
        """Sets state of flip OY necessity in projection matrix"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_StateInterface:
    """Defines interface for OpenGL state."""

    @overload
    def __init__(self) -> None:
        """Creates new state."""

    @overload
    def __init__(self, theOther: OpenGl_StateInterface) -> None: ...

    def Index(self) -> int:
        """Returns current state index."""

    def Update(self) -> None:
        """Increment current state."""

class OpenGl_ProjectionState(OpenGl_StateInterface):
    """Defines state of OCCT projection transformation."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized projection state."""

    @overload
    def __init__(self, theOther: OpenGl_ProjectionState) -> None: ...

    def Set(self, theProjectionMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Sets new projection matrix."""

    def ProjectionMatrix(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns current projection matrix."""

    def ProjectionMatrixInverse(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns inverse of current projection matrix."""

class OpenGl_ModelWorldState(OpenGl_StateInterface):
    """Defines state of OCCT model-world transformation."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized model-world state."""

    @overload
    def __init__(self, theOther: OpenGl_ModelWorldState) -> None: ...

    def Set(self, theModelWorldMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Sets new model-world matrix."""

    def ModelWorldMatrix(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns current model-world matrix."""

    def ModelWorldMatrixInverse(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns inverse of current model-world matrix."""

class OpenGl_WorldViewState(OpenGl_StateInterface):
    """Defines state of OCCT world-view transformation."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized world-view state."""

    @overload
    def __init__(self, theOther: OpenGl_WorldViewState) -> None: ...

    def Set(self, theWorldViewMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Sets new world-view matrix."""

    def WorldViewMatrix(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns current world-view matrix."""

    def WorldViewMatrixInverse(self) -> nanoocp.BVH.BVH_Mat4f:
        """Returns inverse of current world-view matrix."""

class OpenGl_LightSourceState(OpenGl_StateInterface):
    """Defines state of OCCT light sources."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized state of light sources."""

    @overload
    def __init__(self, theOther: OpenGl_LightSourceState) -> None: ...

    def Set(self, theLightSources: nanoocp.Graphic3d.Graphic3d_LightSet | None) -> None:
        """Sets new light sources."""

    def LightSources(self) -> nanoocp.Graphic3d.Graphic3d_LightSet:
        """Returns current list of light sources."""

    def SpecIBLMapLevels(self) -> int:
        """
        Returns number of mipmap levels used in specular IBL map.
        0 by default or in case of using non-PBR shading model.
        """

    def SetSpecIBLMapLevels(self, theSpecIBLMapLevels: int) -> None:
        """Sets number of mipmap levels used in specular IBL map."""

    def HasShadowMaps(self) -> bool:
        """Returns TRUE if shadowmap is set."""

    def ShadowMaps(self) -> OpenGl_ShadowMapArray:
        """Returns shadowmap."""

    def SetShadowMaps(self, theMap: OpenGl_ShadowMapArray | None) -> None:
        """Sets shadowmap."""

    def ToCastShadows(self) -> bool:
        """
        Returns TRUE if shadowmap should be enabled when available; TRUE by default.
        """

    def SetCastShadows(self, theToCast: bool) -> None:
        """Set if shadowmap should be enabled when available."""

class OpenGl_ClippingState:
    """Defines generic state of OCCT clipping state."""

    @overload
    def __init__(self) -> None:
        """Creates new clipping state."""

    @overload
    def __init__(self, theOther: OpenGl_ClippingState) -> None: ...

    def Index(self) -> int:
        """Returns current state index."""

    def Update(self) -> None:
        """Updates current state."""

    def Revert(self) -> None:
        """Reverts current state."""

class OpenGl_OitState(OpenGl_StateInterface):
    """
    Defines generic state of order-independent transparency rendering properties.
    """

    @overload
    def __init__(self) -> None:
        """Creates new uniform state."""

    @overload
    def __init__(self, theOther: OpenGl_OitState) -> None: ...

    def Set(self, theMode: nanoocp.Graphic3d.Graphic3d_RenderTransparentMethod, theDepthFactor: float) -> None:
        """
        Sets the uniform values.
        @param[in] theToEnableWrite  flag indicating whether color and coverage
        values for OIT processing should be written by shader program.
        @param[in] theDepthFactor  scalar factor [0-1] defining influence of depth
        component of a fragment to its final coverage coefficient.
        """

    def ActiveMode(self) -> nanoocp.Graphic3d.Graphic3d_RenderTransparentMethod:
        """
        Returns flag indicating whether writing of output for OIT processing
        should be enabled/disabled.
        """

    def DepthFactor(self) -> float:
        """
        Returns factor defining influence of depth component of a fragment
        to its final coverage coefficient.
        """

class OpenGl_MaterialState(OpenGl_StateInterface):
    """Defines generic state of material properties."""

    @overload
    def __init__(self) -> None:
        """Creates new material state."""

    @overload
    def __init__(self, theOther: OpenGl_MaterialState) -> None: ...

    def Set(self, theMat: OpenGl_Material, theAlphaCutoff: float, theToDistinguish: bool, theToMapTexture: bool) -> None:
        """Sets new material aspect."""

    def Material(self) -> OpenGl_Material:
        """Return front material."""

    def AlphaCutoff(self) -> float:
        """Alpha cutoff value."""

    def HasAlphaCutoff(self) -> bool:
        """Return TRUE if alpha test should be enabled."""

    def ToDistinguish(self) -> bool:
        """Distinguish front/back flag."""

    def ToMapTexture(self) -> bool:
        """Flag for mapping a texture."""

class OpenGl_Window(nanoocp.Standard.Standard_Transient):
    """
    This class represents low-level wrapper over window with GL context.
    The window itself should be provided to constructor.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_Window) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Resize(self) -> None:
        """Resizes the window."""

    def PlatformWindow(self) -> nanoocp.Aspect.Aspect_Window:
        """Return platform window."""

    def SizeWindow(self) -> nanoocp.Aspect.Aspect_Window:
        """Return window object defining dimensions."""

    def Width(self) -> int: ...

    def Height(self) -> int: ...

    def GetGlContext(self) -> OpenGl_Context:
        """Return OpenGL context."""

    def Activate(self) -> bool:
        """Makes GL context for this window active in current thread"""

    def SetSwapInterval(self, theToForceNoSync: bool) -> None:
        """
        Sets swap interval for this window according to the context's settings.
        """

class OpenGl_TextureSetPairIterator:
    """
    Class for iterating pair of texture sets through each defined texture slot.
    Note that iterator considers texture slots being in ascending order within OpenGl_TextureSet.
    """

    @overload
    def __init__(self, theSet1: OpenGl_TextureSet | None, theSet2: OpenGl_TextureSet | None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: OpenGl_TextureSetPairIterator) -> None: ...

    def More(self) -> bool:
        """Return TRUE if there are more texture units to pass through."""

    def Unit(self) -> nanoocp.Graphic3d.Graphic3d_TextureUnit:
        """Return current texture unit."""

    def Texture1(self) -> OpenGl_Texture:
        """Access texture from first texture set."""

    def Texture2(self) -> OpenGl_Texture:
        """Access texture from second texture set."""

    def Next(self) -> None:
        """Move iterator position to the next pair."""

class OpenGl_BackgroundArray(OpenGl_PrimitiveArray):
    """
    Tool class for generating reusable data for
    gradient or texture background rendering.
    """

    @overload
    def __init__(self, theType: nanoocp.Graphic3d.Graphic3d_TypeOfBackground) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: OpenGl_BackgroundArray) -> None: ...

    def Render(self, theWorkspace: OpenGl_Workspace | None, theProjection: nanoocp.Graphic3d.Graphic3d_Camera.Projection) -> None:
        """Render primitives to the window"""

    def IsDefined(self) -> bool:
        """Check if background parameters are set properly"""

    def SetTextureParameters(self, theFillMethod: nanoocp.Aspect.Aspect_FillMethod) -> None:
        """Sets background texture parameters"""

    def SetTextureFillMethod(self, theFillMethod: nanoocp.Aspect.Aspect_FillMethod) -> None:
        """Sets texture fill method"""

    def TextureFillMethod(self) -> nanoocp.Aspect.Aspect_FillMethod:
        """Gets background texture fill method"""

    def GradientFillMethod(self) -> nanoocp.Aspect.Aspect_GradientFillMethod:
        """Gets background gradient fill method"""

    def GradientColor(self, theIndex: int) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns color of gradient background for the given index."""

    def SetGradientFillMethod(self, theType: nanoocp.Aspect.Aspect_GradientFillMethod) -> None:
        """Sets type of gradient fill method"""

    def SetGradientParameters(self, theColor1: nanoocp.Quantity.Quantity_Color, theColor2: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_GradientFillMethod) -> None:
        """Sets background gradient parameters"""

class OpenGl_CappingAlgo:
    """Capping surface rendering algorithm."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_CappingAlgo) -> None: ...

    @staticmethod
    def RenderCapping(theWorkspace: OpenGl_Workspace | None, theStructure: OpenGl_Structure) -> None:
        """
        Draw capping surfaces by OpenGl for the clipping planes enabled in current context state.
        Depth buffer must be generated for the passed groups.
        @param[in] theWorkspace  the GL workspace, context state
        @param[in] theStructure  the structure to be capped
        """

class OpenGl_CappingPlaneResource(OpenGl_Resource):
    """
    Container of graphical resources for rendering capping plane
    associated to graphical clipping plane.
    This resource holds data necessary for OpenGl_CappingAlgo.
    This object is implemented as OpenGl resource for the following reasons:
    - one instance should be shared between contexts.
    - instance associated to Graphic3d_ClipPlane data by id.
    - should created and released within context (owns OpenGl elements and resources).
    """

    def __init__(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane | None) -> None:
        """
        Constructor.
        Create capping plane presentation associated to clipping plane data.
        @param[in] thePlane  the plane data.
        """

    def Update(self, theContext: OpenGl_Context | None, theObjAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """
        Update resource data in the passed context.
        @param[in] theContext    the context
        @param[in] theObjAspect  object aspect
        """

    def Release(self, theContext: OpenGl_Context) -> None:
        """
        Release associated OpenGl resources.
        @param[in] theContext  the resource context.
        """

    def EstimatedDataSize(self) -> int:
        """Returns estimated GPU memory usage - not implemented."""

    def Plane(self) -> nanoocp.Graphic3d.Graphic3d_ClipPlane:
        """Return parent clipping plane structure."""

    def AspectFace(self) -> OpenGl_Aspects:
        """@return aspect face for rendering capping surface."""

    def Orientation(self) -> nanoocp.BVH.BVH_Mat4f:
        """@return evaluated orientation matrix to transform infinite plane."""

    def Primitives(self) -> OpenGl_PrimitiveArray:
        """@return primitive array of vertices to render infinite plane."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_ClippingIterator:
    """The iterator through clipping planes."""

    @overload
    def __init__(self, theClipping: OpenGl_Clipping) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: OpenGl_ClippingIterator) -> None: ...

    def __iter__(self) -> OpenGl_ClippingIterator:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> nanoocp.Graphic3d.Graphic3d_ClipPlane:
        """Python addition: see __iter__."""

    def More(self) -> bool:
        """Return true if iterator points to the valid clipping plane."""

    def Next(self) -> None:
        """Go to the next clipping plane."""

    def IsDisabled(self) -> bool:
        """
        Return true if plane has been temporarily disabled either by Graphic3d_ClipPlane->IsOn()
        property or by temporary filter. Beware that this method does NOT handle a Chain filter for
        Capping algorithm OpenGl_Clipping::CappedChain()!
        """

    def Value(self) -> nanoocp.Graphic3d.Graphic3d_ClipPlane:
        """Return the plane at current iterator position."""

    def IsGlobal(self) -> bool:
        """Return true if plane from the global (view) list."""

    def PlaneIndex(self) -> int:
        """Return the plane index."""

class OpenGl_DepthPeeling(OpenGl_NamedResource):
    """Class provides FBOs for dual depth peeling."""

    def __init__(self) -> None:
        """Constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Release OpenGL resources"""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def AttachDepthTexture(self, theCtx: OpenGl_Context | None, theDepthStencilTexture: OpenGl_Texture | None) -> None:
        """
        Attach a texture image.
        Resets the active FBO to 0.
        """

    def DetachDepthTexture(self, theCtx: OpenGl_Context | None) -> None:
        """
        Detach a texture image.
        Resets the active FBO to 0.
        """

    def DepthPeelFbosOit(self) -> OpenGl_FrameBuffer:
        """Returns additional buffers for ping-pong"""

    def FrontBackColorFbosOit(self) -> OpenGl_FrameBuffer:
        """Returns additional buffers for ping-pong"""

    def BlendBackFboOit(self) -> OpenGl_FrameBuffer:
        """Returns additional FBO for depth peeling"""

class OpenGl_ExtGS:
    """Geometry shader as extension is available on OpenGL 2.0+"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_ExtGS) -> None: ...

class OpenGl_Flipper(OpenGl_Element):
    """
    Being rendered, the elements modifies current model-view matrix such that the axes of
    the specified reference system (in model space) become oriented in the following way:
    - X    - heads to the right side of view.
    - Y    - heads to the up side of view.
    - N(Z) - heads towards the screen.
    Originally, this element serves for need of flipping the 3D text of dimension presentations.
    """

    @overload
    def __init__(self, theReferenceSystem: nanoocp.gp.gp_Ax2) -> None:
        """
        Construct rendering element to flip model-view matrix
        along the reference system to ensure up-Y, right-X orientation.
        @param[in] theReferenceSystem  the reference coordinate system.
        """

    @overload
    def __init__(self, theOther: OpenGl_Flipper) -> None: ...

    def SetOptions(self, theIsEnabled: bool) -> None:
        """
        Set options for the element.
        @param[in] theIsEnabled  flag indicates whether the flipper
        matrix modification should be set up or restored back.
        """

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None: ...

    def Release(self, theCtx: OpenGl_Context) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_GlCore21(OpenGl_GlCore20):
    """OpenGL 2.1 core based on 2.0 version."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore21) -> None: ...

class OpenGl_GlCore30(OpenGl_GlCore21):
    """
    OpenGL 3.0 core.
    This is first version with deprecation model introduced
    - a lot of functionality regarding to fixed pipeline were marked deprecated.
    Notice that nothing were actually removed in this version (unless Forward context loaded)!
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore30) -> None: ...

class OpenGl_GlCore31(OpenGl_GlCore30):
    """OpenGL 3.1 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore31) -> None: ...

class OpenGl_GlCore32(OpenGl_GlCore31):
    """OpenGL 3.2 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore32) -> None: ...

class OpenGl_GlCore33(OpenGl_GlCore32):
    """OpenGL 3.3 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore33) -> None: ...

class OpenGl_GlCore40(OpenGl_GlCore33):
    """OpenGL 4.0 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore40) -> None: ...

class OpenGl_GlCore41(OpenGl_GlCore40):
    """OpenGL 4.1 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore41) -> None: ...

class OpenGl_GlCore42(OpenGl_GlCore41):
    """OpenGL 4.2 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore42) -> None: ...

class OpenGl_GlCore43(OpenGl_GlCore42):
    """OpenGL 4.3 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore43) -> None: ...

class OpenGl_GlCore44(OpenGl_GlCore43):
    """OpenGL 4.4 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore44) -> None: ...

class OpenGl_GlCore45(OpenGl_GlCore44):
    """OpenGL 4.5 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore45) -> None: ...

class OpenGl_GlCore46(OpenGl_GlCore45):
    """OpenGL 4.6 definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OpenGl_GlCore46) -> None: ...

class OpenGl_GraphicDriverFactory(nanoocp.Graphic3d.Graphic3d_GraphicDriverFactory):
    """This class for creation of OpenGl_GraphicDriver."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_GraphicDriverFactory) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CreateDriver(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None) -> nanoocp.Graphic3d.Graphic3d_GraphicDriver:
        """Creates new empty graphic driver."""

    def DefaultOptions(self) -> OpenGl_Caps:
        """Return default driver options."""

    def SetDefaultOptions(self, theOptions: OpenGl_Caps | None) -> None:
        """Set default driver options."""

class OpenGl_IndexBuffer(OpenGl_Buffer):
    """
    Index buffer is just a VBO with special target (GL_ELEMENT_ARRAY_BUFFER).
    """

    def __init__(self) -> None:
        """Empty constructor."""

    def GetTarget(self) -> int:
        """Return buffer object target (GL_ELEMENT_ARRAY_BUFFER)."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class OpenGl_PBREnvironment(OpenGl_NamedResource):
    """
    This class contains specular and diffuse maps required for Image Base Lighting (IBL) in PBR
    shading model with it's generation methods.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def Create(theCtx: OpenGl_Context | None, thePow2Size: int = 9, theSpecMapLevelsNum: int = 6, theId: nanoocp.TCollection.TCollection_AsciiString = ...) -> OpenGl_PBREnvironment:
        """
        Creates and initializes new PBR environment. It is the only way to create
        OpenGl_PBREnvironment.
        @param theCtx OpenGL context where environment will be created
        @param thePow2Size final size of texture's sides can be calculated as 2^thePow2Size;
        if thePow2Size less than 1 it will be set to 1
        @param theSpecMapLevelsNum number of mipmap levels used in specular IBL map;
        if theSpecMapLevelsNum less than 2 or less than Pow2Size + 1 it
        will be set to the corresponding values.
        @param theId OpenGl_Resource name
        @return handle to created PBR environment or NULL handle in case of fail
        """

    def Bind(self, theCtx: OpenGl_Context | None) -> None:
        """
        Binds diffuse and specular IBL maps to the corresponding texture units.
        """

    def Unbind(self, theCtx: OpenGl_Context | None) -> None:
        """Unbinds diffuse and specular IBL maps."""

    def Clear(self, theCtx: OpenGl_Context | None, theColor: nanoocp.Quantity.NCollection_Vec3__float = ...) -> None:
        """
        Fills all mipmaps of specular IBL map and diffuse IBL map with one color.
        So that environment illumination will be constant.
        """

    def Bake(self, theCtx: OpenGl_Context | None, theEnvMap: OpenGl_Texture | None, theZIsInverted: bool = False, theIsTopDown: bool = True, theDiffMapNbSamples: int = 1024, theSpecMapNbSamples: int = 256, theProbability: float = 0.9900000095367432) -> None:
        """
        Generates specular and diffuse (irradiance) IBL maps.
        @param theCtx OpenGL context
        @param theEnvMap source environment map
        @param theZIsInverted flags indicates whether environment cubemap has inverted Z axis or not
        @param theIsTopDown flags indicates whether environment cubemap has top-down memory layout or
        not
        @param theDiffMapNbSamples number of samples in Monte-Carlo integration for diffuse IBL
        spherical harmonics calculation
        @param theSpecMapNbSamples number of samples in Monte-Carlo integration for specular IBL map
        generation
        @param theProbability controls strength of samples number reducing strategy during specular
        IBL map baking (see 'SpecIBLMapSamplesFactor' for details) theZIsInverted and theIsTopDown can
        be taken from Graphic3d_CubeMap source of environment cubemap. theDiffMapNbSamples and
        theSpecMapNbSamples is the main parameter directly affected to performance.
        """

    def SpecMapLevelsNumber(self) -> int:
        """
        Returns number of mipmap levels used in specular IBL map.
        It can be different from value passed to creation method.
        """

    def Pow2Size(self) -> int:
        """
        Returns size of IBL maps sides as power of 2.
        So that the real size can be calculated as 2^Pow2Size()
        """

    def SizesAreDifferent(self, thePow2Size: int, theSpecMapLevelsNumber: int) -> bool:
        """
        Checks whether the given sizes affects to the current ones.
        It can be imagined as creation of new PBR environment.
        If creation method with this values returns the PBR environment having real sizes which are
        equals to current ones then this method will return false. It is handful when sizes are
        required to be changed. If this method returns false there is no reason to recreate PBR
        environment in order to change sizes.
        """

    def IsNeededToBeBound(self) -> bool:
        """
        Indicates whether IBL map's textures have to be bound or it is not obligate.
        """

    def Release(self, theCtx: OpenGl_Context) -> None:
        """
        Releases all OpenGL resources.
        It must be called before destruction.
        """

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def IsComplete(self) -> bool:
        """
        Checks completeness of PBR environment.
        Creation method returns only completed objects or null handles otherwise.
        """

class OpenGl_SetOfPrograms(nanoocp.Standard.Standard_Transient):
    """Alias to programs array of predefined length"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: OpenGl_SetOfPrograms) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ChangeValue(self, theProgramBits: int) -> OpenGl_ShaderProgram:
        """Access program by index"""

class OpenGl_SetOfShaderPrograms(nanoocp.Standard.Standard_Transient):
    """Alias to 2D programs array of predefined length"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, thePrograms: OpenGl_SetOfPrograms | None) -> None:
        """Constructor"""

    @overload
    def __init__(self, theOther: OpenGl_SetOfShaderPrograms) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ChangeValue(self, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theProgramBits: int) -> OpenGl_ShaderProgram:
        """Access program by index"""

class OpenGl_ShaderManager(nanoocp.Graphic3d.Graphic3d_ShaderManager):
    """This class is responsible for managing shader programs."""

    @overload
    def __init__(self, theContext: OpenGl_Context) -> None:
        """Creates new empty shader manager."""

    @overload
    def __init__(self, theOther: OpenGl_ShaderManager) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def clear(self) -> None:
        """Release all resources."""

    def UpdateSRgbState(self) -> None:
        """Fetch sRGB state from caps and invalidates programs, if necessary."""

    def LocalOrigin(self) -> nanoocp.gp.gp_XYZ:
        """Return local camera transformation."""

    def SetLocalOrigin(self, theOrigin: nanoocp.gp.gp_XYZ) -> None:
        """
        Setup local camera transformation for compensating float precision issues.
        """

    def LocalClippingPlaneW(self, thePlane: nanoocp.Graphic3d.Graphic3d_ClipPlane) -> float:
        """
        Return clipping plane W equation value moved considering local camera transformation.
        """

    def Create(self, theProxy: nanoocp.Graphic3d.Graphic3d_ShaderProgram | None, theShareKey: nanoocp.TCollection.TCollection_AsciiString) -> tuple[bool, OpenGl_ShaderProgram]:
        """
        Creates new shader program or re-use shared instance.
        @param[in] theProxy      program definition
        @param[out] theShareKey  sharing key
        @param[out] theProgram   OpenGL program
        @return true on success
        """

    def Unregister(self, theShareKey: nanoocp.TCollection.TCollection_AsciiString) -> OpenGl_ShaderProgram:
        """Unregisters specified shader program."""

    def ShaderPrograms(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.OpenGl.OpenGl_ShaderProgram]:
        """Returns list of registered shader programs."""

    def IsEmpty(self) -> bool:
        """Returns true if no program objects are registered in the manager."""

    @overload
    def BindFaceProgram(self, theTextures: OpenGl_TextureSet | None, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theAlphaMode: nanoocp.Graphic3d.Graphic3d_AlphaMode, theHasVertColor: bool, theEnableEnvMap: bool, theCustomProgram: OpenGl_ShaderProgram | None) -> bool: ...

    @overload
    def BindFaceProgram(self, theTextures: OpenGl_TextureSet | None, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theAlphaMode: nanoocp.Graphic3d.Graphic3d_AlphaMode, theInteriorStyle: nanoocp.Aspect.Aspect_InteriorStyle, theHasVertColor: bool, theToUseVertexColorForBackFaces: bool, theEnableEnvMap: bool, theEnableMeshEdges: bool, theCustomProgram: OpenGl_ShaderProgram | None) -> bool:
        """Bind program for filled primitives rendering"""

    def BindLineProgram(self, theTextures: OpenGl_TextureSet | None, theLineType: nanoocp.Aspect.Aspect_TypeOfLine, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theAlphaMode: nanoocp.Graphic3d.Graphic3d_AlphaMode, theHasVertColor: bool, theCustomProgram: OpenGl_ShaderProgram | None) -> bool:
        """Bind program for line rendering"""

    def BindMarkerProgram(self, theTextures: OpenGl_TextureSet | None, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theAlphaMode: nanoocp.Graphic3d.Graphic3d_AlphaMode, theHasVertColor: bool, theCustomProgram: OpenGl_ShaderProgram | None) -> bool:
        """Bind program for point rendering"""

    def BindFontProgram(self, theCustomProgram: OpenGl_ShaderProgram | None) -> bool:
        """Bind program for rendering alpha-textured font."""

    def BindOutlineProgram(self) -> bool:
        """Bind program for outline rendering"""

    def BindFboBlitProgram(self, theNbSamples: int, theIsFallback_sRGB: bool) -> bool:
        """
        Bind program for FBO blit operation.
        @param[in] theNbSamples        number of samples within source MSAA texture
        @param theIsFallback_sRGB[in]  flag indicating that destination buffer is not sRGB-ready
        """

    def BindOitCompositingProgram(self, theIsMSAAEnabled: bool) -> bool:
        """
        Bind program for blended order-independent transparency buffers compositing.
        """

    def BindOitDepthPeelingBlendProgram(self, theIsMSAAEnabled: bool) -> bool:
        """
        Bind program for Depth Peeling order-independent transparency back color blending.
        """

    def BindOitDepthPeelingFlushProgram(self, theIsMSAAEnabled: bool) -> bool:
        """Bind program for Depth Peeling order-independent transparency flush."""

    def BindStereoProgram(self, theStereoMode: nanoocp.Graphic3d.Graphic3d_StereoMode) -> bool:
        """Bind program for rendering stereoscopic image."""

    def BindBoundBoxProgram(self) -> bool:
        """Bind program for rendering bounding box."""

    def BoundBoxVertBuffer(self) -> OpenGl_VertexBuffer:
        """Returns bounding box vertex buffer."""

    def BindPBREnvBakingProgram(self, theIndex: int) -> bool:
        """Bind program for IBL maps generation in PBR pipeline."""

    def GetBgCubeMapProgram(self) -> nanoocp.Graphic3d.Graphic3d_ShaderProgram:
        """Generates shader program to render environment cubemap as background."""

    def GetBgSkydomeProgram(self) -> nanoocp.Graphic3d.Graphic3d_ShaderProgram:
        """Generates shader program to render skydome background."""

    def GetColoredQuadProgram(self) -> nanoocp.Graphic3d.Graphic3d_ShaderProgram:
        """Generates shader program to render correctly colored quad."""

    def BindGridProgram(self) -> bool:
        """
        Compile (once) and bind the GPU grid shader program.
        Returns FALSE if shader compilation fails or the GAPI is not supported.
        """

    @staticmethod
    def PBRShadingModelFallback(theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theIsPbrAllowed: bool = False) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """
        Resets PBR shading models to corresponding non-PBR ones if PBR is not allowed.
        """

    def LightSourceState(self) -> OpenGl_LightSourceState:
        """Returns current state of OCCT light sources."""

    def UpdateLightSourceStateTo(self, theLights: nanoocp.Graphic3d.Graphic3d_LightSet | None, theSpecIBLMapLevels: int, theShadowMaps: OpenGl_ShadowMapArray | None) -> None:
        """Updates state of OCCT light sources."""

    def SetCastShadows(self, theToCast: bool) -> bool:
        """
        Updates state of OCCT light sources to dynamically enable/disable shadowmap.
        @param[in] theToCast  flag to enable/disable shadowmap
        @return previous flag state
        """

    def UpdateLightSourceState(self) -> None:
        """Invalidate state of OCCT light sources."""

    def PushLightSourceState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT light sources to specified program (only on state change).
        Note that light sources definition depends also on WorldViewState.
        """

    def pushLightSourceState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """Pushes current state of OCCT light sources to specified program."""

    def ProjectionState(self) -> OpenGl_ProjectionState:
        """Returns current state of OCCT projection transform."""

    def UpdateProjectionStateTo(self, theProjectionMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Updates state of OCCT projection transform."""

    def PushProjectionState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT projection transform to specified program (only on state change).
        """

    def pushProjectionState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT projection transform to specified program.
        """

    def ModelWorldState(self) -> OpenGl_ModelWorldState:
        """Returns current state of OCCT model-world transform."""

    def UpdateModelWorldStateTo(self, theModelWorldMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Updates state of OCCT model-world transform."""

    def PushModelWorldState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT model-world transform to specified program (only on state
        change).
        """

    def pushModelWorldState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT model-world transform to specified program.
        """

    def WorldViewState(self) -> OpenGl_WorldViewState:
        """Returns current state of OCCT world-view transform."""

    def UpdateWorldViewStateTo(self, theWorldViewMatrix: nanoocp.BVH.BVH_Mat4f) -> None:
        """Updates state of OCCT world-view transform."""

    def PushWorldViewState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT world-view transform to specified program (only on state change).
        """

    def pushWorldViewState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT world-view transform to specified program.
        """

    def UpdateClippingState(self) -> None:
        """Updates state of OCCT clipping planes."""

    def RevertClippingState(self) -> None:
        """Reverts state of OCCT clipping planes."""

    def PushClippingState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of OCCT clipping planes to specified program (only on state change).
        """

    def pushClippingState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """Pushes current state of OCCT clipping planes to specified program."""

    def MaterialState(self) -> OpenGl_MaterialState:
        """Returns current state of material."""

    def UpdateMaterialStateTo(self, theMat: OpenGl_Material, theAlphaCutoff: float, theToDistinguish: bool, theToMapTexture: bool) -> None:
        """Updates state of material."""

    def UpdateMaterialState(self) -> None:
        """Updates state of material."""

    def PushMaterialState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """
        Pushes current state of material to specified program (only on state change).
        """

    def pushMaterialState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """Pushes current state of material to specified program."""

    def PushInteriorState(self, theProgram: OpenGl_ShaderProgram | None, theAspect: nanoocp.Graphic3d.Graphic3d_Aspects | None) -> None:
        """Setup interior style line edges variables."""

    def OitState(self) -> OpenGl_OitState:
        """Returns state of OIT uniforms."""

    def ResetOitState(self) -> None:
        """Reset the state of OIT rendering pass (only on state change)."""

    def SetOitState(self, theMode: nanoocp.Graphic3d.Graphic3d_RenderTransparentMethod) -> None:
        """
        Set the state of OIT rendering pass (only on state change).
        @param[in] theMode  flag indicating whether the special output should be written for OIT
        algorithm
        """

    def SetWeighedOitState(self, theDepthFactor: float) -> None:
        """
        Set the state of weighed OIT rendering pass (only on state change).
        @param[in] theDepthFactor  the scalar factor of depth influence to the fragment's coverage
        """

    def PushOitState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """Pushes state of OIT uniforms to the specified program."""

    def pushOitState(self, theProgram: OpenGl_ShaderProgram | None) -> None:
        """Pushes state of OIT uniforms to the specified program."""

    def PushState(self, theProgram: OpenGl_ShaderProgram | None, theShadingModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel = ...) -> None:
        """Pushes current state of OCCT graphics parameters to specified program."""

    def SetContext(self, theCtx: OpenGl_Context) -> None:
        """Overwrites context"""

    def IsSameContext(self, theCtx: OpenGl_Context) -> bool:
        """
        Returns true when provided context is the same as used one by shader manager.
        """

    def ChooseFaceShadingModel(self, theCustomModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theHasNodalNormals: bool) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """
        Choose Shading Model for filled primitives.
        Fallbacks to FACET model if there are no normal attributes.
        Fallbacks to corresponding non-PBR models if PBR is unavailable.
        """

    def ChooseLineShadingModel(self, theCustomModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theHasNodalNormals: bool) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """
        Choose Shading Model for line primitives.
        Fallbacks to UNLIT model if there are no normal attributes.
        Fallbacks to corresponding non-PBR models if PBR is unavailable.
        """

    def ChooseMarkerShadingModel(self, theCustomModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theHasNodalNormals: bool) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """Choose Shading Model for Marker primitives."""

    def ShadingModel(self) -> nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel:
        """Returns default Shading Model."""

    def SetShadingModel(self, theModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel) -> None:
        """Sets shading model."""

class OpenGl_ShadowMap(OpenGl_NamedResource):
    """This class contains shadow mapping resources."""

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Releases all OpenGL resources."""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """

    def IsValid(self) -> bool:
        """Return TRUE if defined."""

    def FrameBuffer(self) -> OpenGl_FrameBuffer:
        """Return framebuffer."""

    def Texture(self) -> OpenGl_Texture:
        """Return depth texture."""

    def LightSource(self) -> nanoocp.Graphic3d.Graphic3d_CLight:
        """Return light source casting the shadow or NULL if undefined."""

    def SetLightSource(self, theLight: nanoocp.Graphic3d.Graphic3d_CLight | None) -> None:
        """Set light source casting the shadow."""

    def Camera(self) -> nanoocp.Graphic3d.Graphic3d_Camera:
        """Return rendering camera."""

    def LightSourceMatrix(self) -> nanoocp.BVH.BVH_Mat4f:
        """Return light source mapping matrix."""

    def SetLightSourceMatrix(self, theMat: nanoocp.BVH.BVH_Mat4f) -> None:
        """Set light source mapping matrix."""

    def ShadowMapBias(self) -> float:
        """Returns shadowmap bias."""

    def SetShadowMapBias(self, theBias: float) -> None:
        """Sets shadowmap bias."""

    def UpdateCamera(self, theView: nanoocp.Graphic3d.Graphic3d_CView, theOrigin: nanoocp.gp.gp_XYZ = None) -> bool:
        """
        Compute camera.
        @param[in] theView    active view
        @param[in] theOrigin  when not-NULL - displace shadow map camera to specified Z-Layer origin
        """

class OpenGl_StencilTest(OpenGl_Element):
    def __init__(self) -> None:
        """Default constructor"""

    def Render(self, theWorkspace: OpenGl_Workspace | None) -> None:
        """Render primitives to the window"""

    def Release(self, theContext: OpenGl_Context) -> None: ...

    def SetOptions(self, theIsEnabled: bool) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class OpenGl_TextureBuffer(OpenGl_Buffer):
    """
    Texture Buffer Object.
    This is a special 1D texture that VBO-style initialized.
    The main differences from general 1D texture:
    - no interpolation between field;
    - greater sizes;
    - special sampler object in GLSL shader to access data by index.

    Notice that though TBO is inherited from VBO this is to unify design
    user shouldn't cast it to base class and all really useful methods
    are declared in this class.
    """

    def __init__(self) -> None:
        """Create uninitialized TBO."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetTarget(self) -> int:
        """Override VBO target"""

    def IsValid(self) -> bool:
        """
        Returns true if TBO is valid.
        Notice that no any real GL call is performed!
        """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Destroy object - will release GPU memory if any."""

    def Create(self, theGlCtx: OpenGl_Context | None) -> bool:
        """
        Creates VBO and Texture names (ids) if not yet generated.
        Data should be initialized by another method.
        """

    def BindTexture(self, theGlCtx: OpenGl_Context | None, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """Bind TBO to specified Texture Unit."""

    def UnbindTexture(self, theGlCtx: OpenGl_Context | None, theTextureUnit: nanoocp.Graphic3d.Graphic3d_TextureUnit) -> None:
        """Unbind TBO."""

    def TextureId(self) -> int:
        """Returns name of TBO."""

    def TextureFormat(self) -> int:
        """Returns internal texture format."""

class OpenGl_UniformBuffer(OpenGl_Buffer):
    """Uniform buffer object."""

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetTarget(self) -> int:
        """Return buffer object target (GL_UNIFORM_BUFFER)."""

    def BindBufferBase(self, theGlCtx: OpenGl_Context | None, theIndex: int) -> None:
        """
        Binds a buffer object to an indexed buffer target.
        Wrapper for glBindBufferBase().
        @param[in] theGlCtx  active OpenGL context
        @param[in] theIndex  index to bind
        """

    def BindBufferRange(self, theGlCtx: OpenGl_Context | None, theIndex: int, theOffset: int, theSize: int) -> None:
        """
        Binds a buffer object to an indexed buffer target with specified offset and size.
        Wrapper for glBindBufferRange().
        @param[in] theGlCtx   active OpenGL context
        @param[in] theIndex   index to bind (@sa GL_MAX_UNIFORM_BUFFER_BINDINGS in case of uniform
        buffer)
        @param[in] theOffset  offset within the buffer (@sa GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT in case
        of uniform buffer)
        @param[in] theSize    sub-section length starting from offset
        """

    def UnbindBufferBase(self, theGlCtx: OpenGl_Context | None, theIndex: int) -> None:
        """
        Unbinds a buffer object from an indexed buffer target.
        Wrapper for glBindBufferBase().
        @param[in] theGlCtx  active OpenGL context
        @param[in] theIndex  index to bind
        """

class OpenGl_VertexBufferCompat(OpenGl_VertexBuffer):
    """
    Compatibility layer for old OpenGL without VBO.
    Make sure to pass pointer from GetDataOffset() instead of NULL.
    Method GetDataOffset() returns pointer to real data in this class
    (while base class OpenGl_VertexBuffer always return NULL).

    Methods Bind()/Unbind() do nothing (do not affect OpenGL state)
    and ::GetTarget() is never used.
    For this reason there is no analog for OpenGl_IndexBuffer.
    Just pass GetDataOffset() to glDrawElements() directly as last argument.

    Class overrides methods init() and subData() to copy data into own memory buffer.
    Extra method initLink() might be used to pass existing buffer through handle without copying the
    data.

    Method Create() creates dummy identifier for this object which should NOT be passed to OpenGL
    functions.
    """

    def __init__(self) -> None:
        """Create uninitialized VBO."""

    def IsVirtual(self) -> bool:
        """Return TRUE."""

    def Create(self, theGlCtx: OpenGl_Context | None) -> bool:
        """
        Creates VBO name (id) if not yet generated.
        Data should be initialized by another method.
        """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Destroy object - will release memory if any."""

    def Bind(self, arg0: OpenGl_Context | None) -> None:
        """Bind this VBO."""

    def Unbind(self, arg0: OpenGl_Context | None) -> None:
        """Unbind this VBO."""

    def initLink(self, theData: nanoocp.NCollection.NCollection_Buffer | None, theComponentsNb: int, theElemsNb: int, theDataType: int) -> bool:
        """
        @name advanced methods
        Initialize buffer with existing data.
        Data will NOT be copied by this method!
        """

class OpenGl_IndexBufferCompat(OpenGl_IndexBuffer):
    """
    Compatibility layer for old OpenGL without VBO.
    Make sure to pass pointer from GetDataOffset() instead of NULL.
    Method GetDataOffset() returns pointer to real data in this class
    (while base class OpenGl_VertexBuffer always return NULL).

    Methods Bind()/Unbind() do nothing (do not affect OpenGL state)
    and ::GetTarget() is never used.
    For this reason there is no analog for OpenGl_IndexBuffer.
    Just pass GetDataOffset() to glDrawElements() directly as last argument.

    Class overrides methods init() and subData() to copy data into own memory buffer.
    Extra method initLink() might be used to pass existing buffer through handle without copying the
    data.

    Method Create() creates dummy identifier for this object which should NOT be passed to OpenGL
    functions.
    """

    def __init__(self) -> None:
        """Create uninitialized VBO."""

    def IsVirtual(self) -> bool:
        """Return TRUE."""

    def Create(self, theGlCtx: OpenGl_Context | None) -> bool:
        """
        Creates VBO name (id) if not yet generated.
        Data should be initialized by another method.
        """

    def Release(self, theGlCtx: OpenGl_Context) -> None:
        """Destroy object - will release memory if any."""

    def Bind(self, arg0: OpenGl_Context | None) -> None:
        """Bind this VBO."""

    def Unbind(self, arg0: OpenGl_Context | None) -> None:
        """Unbind this VBO."""

    def initLink(self, theData: nanoocp.NCollection.NCollection_Buffer | None, theComponentsNb: int, theElemsNb: int, theDataType: int) -> bool:
        """
        @name advanced methods
        Initialize buffer with existing data.
        Data will NOT be copied by this method!
        """

class NCollection_Vec4__bool:
    """
    Generic 4-components vector.
    To be used as RGBA color vector or XYZW 3D-point with special W-component
    for operations with projection / model view matrices.
    Use this class for 3D-points carefully because declared W-component may
    results in incorrect results if used without matrices.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theValue: bool) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theVec2: "NCollection_Vec2<bool>") -> None:
        """Constructor from 2-components vector."""

    @overload
    def __init__(self, theVec3: nanoocp.Aspect.NCollection_Vec3__bool, theW: bool = False) -> None:
        """Constructor from 3-components vector + optional 4th value."""

    @overload
    def __init__(self, theX: bool, theY: bool, theZ: bool, theW: bool) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: NCollection_Vec4__bool) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    @overload
    def SetValues(self, theX: bool, theY: bool, theZ: bool, theW: bool) -> None:
        """Assign new values to the vector."""

    @overload
    def SetValues(self, theVec3: nanoocp.Aspect.NCollection_Vec3__bool, theW: bool) -> None:
        """Assign new values as 3-component vector and a 4-th value."""

    def xy(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yx(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xz(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zx(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xw(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wx(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yz(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zy(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def yw(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wy(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def zw(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def wz(self) -> "NCollection_Vec2<bool>":
        """
        @return 2 of XYZW components in specified order as vector in GLSL-style
        """

    def xyz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xyw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yxw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xzw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def xwz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zxw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzx(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wxz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def yzw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def ywz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zyw(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def zwy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wzy(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def wyz(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """
        @return 3 of XYZW components in specified order as vector in GLSL-style
        """

    def rgb(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def rbg(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def grb(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def gbr(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def bgr(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def brg(self) -> nanoocp.Aspect.NCollection_Vec3__bool:
        """@return RGB components as vector"""

    def x(self) -> bool:
        """Alias to 1st component as X coordinate in XYZW."""

    def Setx(self, theValue: bool) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def r(self) -> bool:
        """Alias to 1st component as RED channel in RGBA."""

    def Setr(self, theValue: bool) -> None:
        """Python addition: sets the value r() returns by reference in C++."""

    def y(self) -> bool:
        """Alias to 2nd component as Y coordinate in XYZW."""

    def Sety(self, theValue: bool) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def g(self) -> bool:
        """Alias to 2nd component as GREEN channel in RGBA."""

    def Setg(self, theValue: bool) -> None:
        """Python addition: sets the value g() returns by reference in C++."""

    def z(self) -> bool:
        """Alias to 3rd component as Z coordinate in XYZW."""

    def Setz(self, theValue: bool) -> None:
        """Python addition: sets the value z() returns by reference in C++."""

    def b(self) -> bool:
        """Alias to 3rd component as BLUE channel in RGBA."""

    def Setb(self, theValue: bool) -> None:
        """Python addition: sets the value b() returns by reference in C++."""

    def w(self) -> bool:
        """Alias to 4th component as W coordinate in XYZW."""

    def Setw(self, theValue: bool) -> None:
        """Python addition: sets the value w() returns by reference in C++."""

    def a(self) -> bool:
        """Alias to 4th component as ALPHA channel in RGBA."""

    def Seta(self, theValue: bool) -> None:
        """Python addition: sets the value a() returns by reference in C++."""

    def IsEqual(self, theOther: NCollection_Vec4__bool) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: NCollection_Vec4__bool) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: NCollection_Vec4__bool) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: NCollection_Vec4__bool) -> NCollection_Vec4__bool:
        """Compute per-component summary."""

    def __neg__(self) -> NCollection_Vec4__bool:
        """Unary -."""

    def __isub__(self, theDec: NCollection_Vec4__bool) -> NCollection_Vec4__bool:
        """Compute per-component subtraction."""

    @overload
    def __imul__(self, theRight: NCollection_Vec4__bool) -> NCollection_Vec4__bool: ...

    @overload
    def __imul__(self, theFactor: bool) -> NCollection_Vec4__bool:
        """Compute per-component multiplication."""

    def Multiply(self, theFactor: bool) -> None:
        """Compute per-component multiplication."""

    @overload
    def __mul__(self, theFactor: bool) -> NCollection_Vec4__bool:
        """Compute per-component multiplication."""

    @overload
    def __mul__(self, arg: NCollection_Vec4__bool, /) -> NCollection_Vec4__bool: ...

    def Multiplied(self, theFactor: bool) -> NCollection_Vec4__bool:
        """Compute per-component multiplication."""

    def cwiseMin(self, theVec: NCollection_Vec4__bool) -> NCollection_Vec4__bool:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: NCollection_Vec4__bool) -> NCollection_Vec4__bool:
        """Compute component-wise maximum of two vectors."""

    def cwiseAbs(self) -> NCollection_Vec4__bool:
        """Compute component-wise modulus of the vector."""

    def maxComp(self) -> bool:
        """Compute maximum component of the vector."""

    def minComp(self) -> bool:
        """Compute minimum component of the vector."""

    def Dot(self, theOther: NCollection_Vec4__bool) -> bool:
        """Computes the dot product."""

    @overload
    def __itruediv__(self, theInvFactor: bool) -> NCollection_Vec4__bool:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: NCollection_Vec4__bool) -> NCollection_Vec4__bool:
        """Compute per-component division."""

    @overload
    def __truediv__(self, theInvFactor: bool) -> NCollection_Vec4__bool:
        """Compute per-component division by scale factor."""

    @overload
    def __truediv__(self, arg: NCollection_Vec4__bool, /) -> NCollection_Vec4__bool: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __add__(self, arg: NCollection_Vec4__bool, /) -> NCollection_Vec4__bool: ...

    def __sub__(self, arg: NCollection_Vec4__bool, /) -> NCollection_Vec4__bool: ...

class OpenGl_MatrixState__float:
    """Software implementation for OpenGL matrix stack."""

    @overload
    def __init__(self) -> None:
        """Constructs matrix state object."""

    @overload
    def __init__(self, theOther: OpenGl_MatrixState__float) -> None: ...

    def Push(self) -> None:
        """Pushes current matrix into stack."""

    def Pop(self) -> None:
        """Pops matrix from stack to current."""

    def Current(self) -> nanoocp.BVH.BVH_Mat4f:
        """@return current matrix."""

    def SetCurrent(self, theNewCurrent: nanoocp.BVH.BVH_Mat4f) -> None:
        """Sets given matrix as current."""

    def ChangeCurrent(self) -> nanoocp.BVH.BVH_Mat4f:
        """Change current matrix."""

    def SetIdentity(self) -> None:
        """Sets current matrix to identity."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class NCollection_Vec2__unsigned_int:
    """
    Defines the 2D-vector template.
    The main target for this class - to handle raw low-level arrays (from/to graphic driver etc.).
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor. Construct the zero vector."""

    @overload
    def __init__(self, theXY: int) -> None:
        """Initialize ALL components of vector within specified value."""

    @overload
    def __init__(self, theX: int, theY: int) -> None:
        """Per-component constructor."""

    @overload
    def __init__(self, theOther: NCollection_Vec2__unsigned_int) -> None: ...

    @staticmethod
    def Length() -> int:
        """Returns the number of components."""

    def SetValues(self, theX: int, theY: int) -> None:
        """Assign new values to the vector."""

    def xy(self) -> NCollection_Vec2__unsigned_int:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def yx(self) -> NCollection_Vec2__unsigned_int:
        """@return 2 components by their names in specified order (in GLSL-style)"""

    def x(self) -> int:
        """Alias to 1st component as X coordinate in XY."""

    def Setx(self, theValue: int) -> None:
        """Python addition: sets the value x() returns by reference in C++."""

    def y(self) -> int:
        """Alias to 2nd component as Y coordinate in XY."""

    def Sety(self, theValue: int) -> None:
        """Python addition: sets the value y() returns by reference in C++."""

    def IsEqual(self, theOther: NCollection_Vec2__unsigned_int) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __eq__(self, theOther: NCollection_Vec2__unsigned_int) -> bool:
        """
        Check this vector with another vector for equality (without tolerance!).
        """

    def __ne__(self, theOther: NCollection_Vec2__unsigned_int) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    def __iadd__(self, theAdd: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component summary."""

    def __isub__(self, theDec: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component subtraction."""

    def __neg__(self) -> NCollection_Vec2__unsigned_int:
        """Unary -."""

    @overload
    def __imul__(self, theRight: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component multiplication."""

    @overload
    def __imul__(self, theFactor: int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component multiplication by scale factor."""

    def Multiply(self, theFactor: int) -> None:
        """Compute per-component multiplication by scale factor."""

    def Multiplied(self, theFactor: int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component multiplication by scale factor."""

    def cwiseMin(self, theVec: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute component-wise minimum of two vectors."""

    def cwiseMax(self, theVec: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute component-wise maximum of two vectors."""

    def maxComp(self) -> int:
        """Compute maximum component of the vector."""

    def minComp(self) -> int:
        """Compute minimum component of the vector."""

    @overload
    def __itruediv__(self, theInvFactor: int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component division by scale factor."""

    @overload
    def __itruediv__(self, theRight: NCollection_Vec2__unsigned_int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component division."""

    @overload
    def __mul__(self, theFactor: int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component multiplication by scale factor."""

    @overload
    def __mul__(self, arg: NCollection_Vec2__unsigned_int, /) -> NCollection_Vec2__unsigned_int: ...

    @overload
    def __truediv__(self, theInvFactor: int) -> NCollection_Vec2__unsigned_int:
        """Compute per-component division by scale factor."""

    @overload
    def __truediv__(self, arg: NCollection_Vec2__unsigned_int, /) -> NCollection_Vec2__unsigned_int: ...

    def Dot(self, theOther: NCollection_Vec2__unsigned_int) -> int:
        """Computes the dot product."""

    def Modulus(self) -> int:
        """Computes the vector modulus (magnitude, length)."""

    def SquareModulus(self) -> int:
        """
        Computes the square of vector modulus (magnitude, length).
        This method may be used for performance tricks.
        """

    @staticmethod
    def DX() -> NCollection_Vec2__unsigned_int:
        """Construct DX unit vector."""

    @staticmethod
    def DY() -> NCollection_Vec2__unsigned_int:
        """Construct DY unit vector."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def __add__(self, arg: NCollection_Vec2__unsigned_int, /) -> NCollection_Vec2__unsigned_int: ...

    def __sub__(self, arg: NCollection_Vec2__unsigned_int, /) -> NCollection_Vec2__unsigned_int: ...

class BVH_Tree__float__3__BVH_QuadTree:
    """BVH tree with given arity (2 or 4)."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BVH_Tree__float__3__BVH_QuadTree) -> None: ...

class BVH_Builder__float__3(nanoocp.BVH.BVH_BuilderTransient):
    """
    Performs construction of BVH tree using bounding
    boxes (AABBs) of abstract objects.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    def Build(self, theSet: BVH_Set__float__3, theBVH: "BVH_Tree<float, 3, BVH_BinaryTree>", theBox: BVH_Box__float__3) -> None:
        """Builds BVH using specific algorithm."""

class BVH_Box__float__3:
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None:
        """Creates uninitialized bounding box."""

    @overload
    def __init__(self, thePoint: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Creates bounding box of given point."""

    @overload
    def __init__(self, theMinPoint: nanoocp.Quantity.NCollection_Vec3__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Creates bounding box from corner points."""

    @overload
    def __init__(self, theOther: BVH_Box__float__3) -> None: ...

    def Clear(self) -> None:
        """Clears bounding box."""

    def IsValid(self) -> bool:
        """Is bounding box valid?"""

    def Add(self, thePoint: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Appends new point to the bounding box."""

    def Combine(self, theBox: BVH_Box__float__3) -> None:
        """Combines bounding box with another one."""

    def CornerMin(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Returns minimum point of bounding box."""

    def CornerMax(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Returns maximum point of bounding box."""

    def Area(self) -> float:
        """
        Returns surface area of bounding box.
        If the box is degenerated into line, returns the perimeter instead.
        """

    def Size(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Returns diagonal of bounding box."""

    @overload
    def Center(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Returns center of bounding box."""

    @overload
    def Center(self, theAxis: int) -> float:
        """Returns center of bounding box along the given axis."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

    @overload
    def IsOut(self, theOther: BVH_Box__float__3) -> bool:
        """Checks if the Box is out of the other box."""

    @overload
    def IsOut(self, theMinPoint: nanoocp.Quantity.NCollection_Vec3__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Checks if the Box is out of the other box defined by two points."""

    @overload
    def IsOut(self, thePoint: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Checks if the Point is out of the box."""

    @overload
    def Contains(self, theOther: BVH_Box__float__3) -> tuple[bool, bool]:
        """Checks if the Box fully contains the other box."""

    @overload
    def Contains(self, theMinPoint: nanoocp.Quantity.NCollection_Vec3__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec3__float) -> tuple[bool, bool]:
        """Checks if the Box is fully contains the other box."""

class OpenGl_ShadowMapArray(nanoocp.Standard.Standard_Transient):
    """Array of shadow maps."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: OpenGl_ShadowMapArray) -> None: ...

    def Release(self, theCtx: OpenGl_Context) -> None:
        """Releases all OpenGL resources."""

    def IsValid(self) -> bool:
        """Return TRUE if defined."""

    def EstimatedDataSize(self) -> int:
        """
        Returns estimated GPU memory usage for holding data without considering overheads and
        allocation alignment rules.
        """
