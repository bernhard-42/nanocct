"""OCCT package Graphic3d (toolkit TKService)"""

from collections.abc import Sequence
import enum
from typing import TextIO, overload

import nanoocp.Aspect
import nanoocp.BVH
from nanoocp.BVH import BVH_Vec2f as NCollection_Vec2__float
import nanoocp.Bnd
from nanoocp.Bnd import BVH_Box__double__3 as Graphic3d_BndBox3d
import nanoocp.Font
import nanoocp.Image
import nanoocp.Media
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Quantity
from nanoocp.Quantity import (
    NCollection_Vec3__float as NCollection_Vec3__float,
    NCollection_Vec4__float as NCollection_Vec4__float
)
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopLoc
import nanoocp.gp


class Graphic3d_AlphaMode(enum.IntEnum):
    """Defines how alpha value of base color / texture should be treated."""

    Graphic3d_AlphaMode_Opaque = 0

    Graphic3d_AlphaMode_Mask = 1

    Graphic3d_AlphaMode_Blend = 2

    Graphic3d_AlphaMode_MaskBlend = 3

    Graphic3d_AlphaMode_BlendAuto = -1

Graphic3d_AlphaMode_Opaque: Graphic3d_AlphaMode = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Opaque

Graphic3d_AlphaMode_Mask: Graphic3d_AlphaMode = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Mask

Graphic3d_AlphaMode_Blend: Graphic3d_AlphaMode = Graphic3d_AlphaMode.Graphic3d_AlphaMode_Blend

Graphic3d_AlphaMode_MaskBlend: Graphic3d_AlphaMode = Graphic3d_AlphaMode.Graphic3d_AlphaMode_MaskBlend

Graphic3d_AlphaMode_BlendAuto: Graphic3d_AlphaMode = Graphic3d_AlphaMode.Graphic3d_AlphaMode_BlendAuto

Graphic3d_ArrayFlags_None: int = 0

Graphic3d_ArrayFlags_VertexNormal: int = 1

Graphic3d_ArrayFlags_VertexColor: int = 2

Graphic3d_ArrayFlags_VertexTexel: int = 4

Graphic3d_ArrayFlags_BoundColor: int = 16

Graphic3d_ArrayFlags_AttribsMutable: int = 32

Graphic3d_ArrayFlags_AttribsDeinterleaved: int = 64

Graphic3d_ArrayFlags_IndexesMutable: int = 128

class Graphic3d_TypeOfAttribute(enum.IntEnum):
    """Type of attribute in Vertex Buffer"""

    Graphic3d_TOA_POS = 0

    Graphic3d_TOA_NORM = 1

    Graphic3d_TOA_UV = 2

    Graphic3d_TOA_COLOR = 3

    Graphic3d_TOA_CUSTOM = 4

Graphic3d_TOA_POS: Graphic3d_TypeOfAttribute = Graphic3d_TypeOfAttribute.Graphic3d_TOA_POS

Graphic3d_TOA_NORM: Graphic3d_TypeOfAttribute = Graphic3d_TypeOfAttribute.Graphic3d_TOA_NORM

Graphic3d_TOA_UV: Graphic3d_TypeOfAttribute = Graphic3d_TypeOfAttribute.Graphic3d_TOA_UV

Graphic3d_TOA_COLOR: Graphic3d_TypeOfAttribute = Graphic3d_TypeOfAttribute.Graphic3d_TOA_COLOR

Graphic3d_TOA_CUSTOM: Graphic3d_TypeOfAttribute = Graphic3d_TypeOfAttribute.Graphic3d_TOA_CUSTOM

class Graphic3d_TypeOfData(enum.IntEnum):
    """Type of the element in Vertex or Index Buffer"""

    Graphic3d_TOD_USHORT = 0

    Graphic3d_TOD_UINT = 1

    Graphic3d_TOD_VEC2 = 2

    Graphic3d_TOD_VEC3 = 3

    Graphic3d_TOD_VEC4 = 4

    Graphic3d_TOD_VEC4UB = 5

    Graphic3d_TOD_FLOAT = 6

Graphic3d_TOD_USHORT: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_USHORT

Graphic3d_TOD_UINT: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_UINT

Graphic3d_TOD_VEC2: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_VEC2

Graphic3d_TOD_VEC3: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_VEC3

Graphic3d_TOD_VEC4: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4

Graphic3d_TOD_VEC4UB: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_VEC4UB

Graphic3d_TOD_FLOAT: Graphic3d_TypeOfData = Graphic3d_TypeOfData.Graphic3d_TOD_FLOAT

class Graphic3d_TypeOfPrimitiveArray(enum.IntEnum):
    """The type of primitive array in a group in a structure."""

    Graphic3d_TOPA_UNDEFINED = 0

    Graphic3d_TOPA_POINTS = 1

    Graphic3d_TOPA_SEGMENTS = 2

    Graphic3d_TOPA_POLYLINES = 3

    Graphic3d_TOPA_TRIANGLES = 4

    Graphic3d_TOPA_TRIANGLESTRIPS = 5

    Graphic3d_TOPA_TRIANGLEFANS = 6

    Graphic3d_TOPA_LINES_ADJACENCY = 7

    Graphic3d_TOPA_LINE_STRIP_ADJACENCY = 8

    Graphic3d_TOPA_TRIANGLES_ADJACENCY = 9

    Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY = 10

    Graphic3d_TOPA_QUADRANGLES = 11

    Graphic3d_TOPA_QUADRANGLESTRIPS = 12

    Graphic3d_TOPA_POLYGONS = 13

Graphic3d_TOPA_UNDEFINED: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_POINTS: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_SEGMENTS: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_POLYLINES: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_TRIANGLES: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_TRIANGLESTRIPS: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_TRIANGLEFANS: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_LINES_ADJACENCY: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_LINE_STRIP_ADJACENCY: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_TRIANGLES_ADJACENCY: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_TRIANGLE_STRIP_ADJACENCY: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_QUADRANGLES: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_QUADRANGLESTRIPS: Graphic3d_TypeOfPrimitiveArray = ...

Graphic3d_TOPA_POLYGONS: Graphic3d_TypeOfPrimitiveArray = ...

class Graphic3d_FresnelModel(enum.IntEnum):
    """Type of the Fresnel model."""

    Graphic3d_FM_SCHLICK = 0

    Graphic3d_FM_CONSTANT = 1

    Graphic3d_FM_CONDUCTOR = 2

    Graphic3d_FM_DIELECTRIC = 3

Graphic3d_FM_SCHLICK: Graphic3d_FresnelModel = Graphic3d_FresnelModel.Graphic3d_FM_SCHLICK

Graphic3d_FM_CONSTANT: Graphic3d_FresnelModel = Graphic3d_FresnelModel.Graphic3d_FM_CONSTANT

Graphic3d_FM_CONDUCTOR: Graphic3d_FresnelModel = Graphic3d_FresnelModel.Graphic3d_FM_CONDUCTOR

Graphic3d_FM_DIELECTRIC: Graphic3d_FresnelModel = Graphic3d_FresnelModel.Graphic3d_FM_DIELECTRIC

class Graphic3d_NameOfMaterial(enum.IntEnum):
    """
    List of named materials (predefined presets).
    Each preset defines either physical (having natural color) or generic (mutable color) material
    (@sa Graphic3d_TypeOfMaterial).
    """

    Graphic3d_NameOfMaterial_Brass = 0

    Graphic3d_NameOfMaterial_Bronze = 1

    Graphic3d_NameOfMaterial_Copper = 2

    Graphic3d_NameOfMaterial_Gold = 3

    Graphic3d_NameOfMaterial_Pewter = 4

    Graphic3d_NameOfMaterial_Plastered = 5

    Graphic3d_NameOfMaterial_Plastified = 6

    Graphic3d_NameOfMaterial_Silver = 7

    Graphic3d_NameOfMaterial_Steel = 8

    Graphic3d_NameOfMaterial_Stone = 9

    Graphic3d_NameOfMaterial_ShinyPlastified = 10

    Graphic3d_NameOfMaterial_Satin = 11

    Graphic3d_NameOfMaterial_Metalized = 12

    Graphic3d_NameOfMaterial_Ionized = 13

    Graphic3d_NameOfMaterial_Chrome = 14

    Graphic3d_NameOfMaterial_Aluminum = 15

    Graphic3d_NameOfMaterial_Obsidian = 16

    Graphic3d_NameOfMaterial_Neon = 17

    Graphic3d_NameOfMaterial_Jade = 18

    Graphic3d_NameOfMaterial_Charcoal = 19

    Graphic3d_NameOfMaterial_Water = 20

    Graphic3d_NameOfMaterial_Glass = 21

    Graphic3d_NameOfMaterial_Diamond = 22

    Graphic3d_NameOfMaterial_Transparent = 23

    Graphic3d_NameOfMaterial_DEFAULT = 24

    Graphic3d_NameOfMaterial_UserDefined = 25

    Graphic3d_NOM_BRASS = 0

    Graphic3d_NOM_BRONZE = 1

    Graphic3d_NOM_COPPER = 2

    Graphic3d_NOM_GOLD = 3

    Graphic3d_NOM_PEWTER = 4

    Graphic3d_NOM_PLASTER = 5

    Graphic3d_NOM_PLASTIC = 6

    Graphic3d_NOM_SILVER = 7

    Graphic3d_NOM_STEEL = 8

    Graphic3d_NOM_STONE = 9

    Graphic3d_NOM_SHINY_PLASTIC = 10

    Graphic3d_NOM_SATIN = 11

    Graphic3d_NOM_METALIZED = 12

    Graphic3d_NOM_NEON_GNC = 13

    Graphic3d_NOM_CHROME = 14

    Graphic3d_NOM_ALUMINIUM = 15

    Graphic3d_NOM_OBSIDIAN = 16

    Graphic3d_NOM_NEON_PHC = 17

    Graphic3d_NOM_JADE = 18

    Graphic3d_NOM_CHARCOAL = 19

    Graphic3d_NOM_WATER = 20

    Graphic3d_NOM_GLASS = 21

    Graphic3d_NOM_DIAMOND = 22

    Graphic3d_NOM_TRANSPARENT = 23

    Graphic3d_NOM_DEFAULT = 24

    Graphic3d_NOM_UserDefined = 25

Graphic3d_NameOfMaterial_Brass: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Bronze: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Copper: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Gold: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Pewter: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Plastered: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Plastified: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Silver: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Steel: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Stone: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_ShinyPlastified: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Satin: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Metalized: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Ionized: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Chrome: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Aluminum: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Obsidian: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Neon: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Jade: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Charcoal: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Water: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Glass: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Diamond: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_Transparent: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_DEFAULT: Graphic3d_NameOfMaterial = ...

Graphic3d_NameOfMaterial_UserDefined: Graphic3d_NameOfMaterial = ...

Graphic3d_NOM_BRASS: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRASS

Graphic3d_NOM_BRONZE: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_BRONZE

Graphic3d_NOM_COPPER: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_COPPER

Graphic3d_NOM_GOLD: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_GOLD

Graphic3d_NOM_PEWTER: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_PEWTER

Graphic3d_NOM_PLASTER: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTER

Graphic3d_NOM_PLASTIC: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_PLASTIC

Graphic3d_NOM_SILVER: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_SILVER

Graphic3d_NOM_STEEL: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_STEEL

Graphic3d_NOM_STONE: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_STONE

Graphic3d_NOM_SHINY_PLASTIC: Graphic3d_NameOfMaterial = ...

Graphic3d_NOM_SATIN: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_SATIN

Graphic3d_NOM_METALIZED: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED

Graphic3d_NOM_NEON_GNC: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_GNC

Graphic3d_NOM_CHROME: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHROME

Graphic3d_NOM_ALUMINIUM: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_ALUMINIUM

Graphic3d_NOM_OBSIDIAN: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_OBSIDIAN

Graphic3d_NOM_NEON_PHC: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_NEON_PHC

Graphic3d_NOM_JADE: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_JADE

Graphic3d_NOM_CHARCOAL: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_CHARCOAL

Graphic3d_NOM_WATER: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_WATER

Graphic3d_NOM_GLASS: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_GLASS

Graphic3d_NOM_DIAMOND: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_DIAMOND

Graphic3d_NOM_TRANSPARENT: Graphic3d_NameOfMaterial = ...

Graphic3d_NOM_DEFAULT: Graphic3d_NameOfMaterial = Graphic3d_NameOfMaterial.Graphic3d_NOM_DEFAULT

Graphic3d_NOM_UserDefined: Graphic3d_NameOfMaterial = ...

class Graphic3d_TypeOfMaterial(enum.IntEnum):
    """Types of materials specifies if a material can change color."""

    Graphic3d_MATERIAL_ASPECT = 0

    Graphic3d_MATERIAL_PHYSIC = 1

Graphic3d_MATERIAL_ASPECT: Graphic3d_TypeOfMaterial = ...

Graphic3d_MATERIAL_PHYSIC: Graphic3d_TypeOfMaterial = ...

class Graphic3d_TypeOfReflection(enum.IntEnum):
    """Nature of the reflection of a material."""

    Graphic3d_TOR_AMBIENT = 0

    Graphic3d_TOR_DIFFUSE = 1

    Graphic3d_TOR_SPECULAR = 2

    Graphic3d_TOR_EMISSION = 3

Graphic3d_TOR_AMBIENT: Graphic3d_TypeOfReflection = Graphic3d_TypeOfReflection.Graphic3d_TOR_AMBIENT

Graphic3d_TOR_DIFFUSE: Graphic3d_TypeOfReflection = Graphic3d_TypeOfReflection.Graphic3d_TOR_DIFFUSE

Graphic3d_TOR_SPECULAR: Graphic3d_TypeOfReflection = Graphic3d_TypeOfReflection.Graphic3d_TOR_SPECULAR

Graphic3d_TOR_EMISSION: Graphic3d_TypeOfReflection = Graphic3d_TypeOfReflection.Graphic3d_TOR_EMISSION

Graphic3d_TypeOfReflection_NB: int = 4

class Graphic3d_RenderTransparentMethod(enum.IntEnum):
    """
    Enumerates transparency rendering methods supported by rasterization mode.
    """

    Graphic3d_RTM_BLEND_UNORDERED = 0

    Graphic3d_RTM_BLEND_OIT = 1

    Graphic3d_RTM_DEPTH_PEELING_OIT = 2

Graphic3d_RTM_BLEND_UNORDERED: Graphic3d_RenderTransparentMethod = ...

Graphic3d_RTM_BLEND_OIT: Graphic3d_RenderTransparentMethod = ...

Graphic3d_RTM_DEPTH_PEELING_OIT: Graphic3d_RenderTransparentMethod = ...

class Graphic3d_TypeOfShaderObject(enum.IntEnum):
    """Type of the shader object."""

    Graphic3d_TOS_VERTEX = 1

    Graphic3d_TOS_TESS_CONTROL = 2

    Graphic3d_TOS_TESS_EVALUATION = 4

    Graphic3d_TOS_GEOMETRY = 8

    Graphic3d_TOS_FRAGMENT = 16

    Graphic3d_TOS_COMPUTE = 32

Graphic3d_TOS_VERTEX: Graphic3d_TypeOfShaderObject = Graphic3d_TypeOfShaderObject.Graphic3d_TOS_VERTEX

Graphic3d_TOS_TESS_CONTROL: Graphic3d_TypeOfShaderObject = ...

Graphic3d_TOS_TESS_EVALUATION: Graphic3d_TypeOfShaderObject = ...

Graphic3d_TOS_GEOMETRY: Graphic3d_TypeOfShaderObject = ...

Graphic3d_TOS_FRAGMENT: Graphic3d_TypeOfShaderObject = ...

Graphic3d_TOS_COMPUTE: Graphic3d_TypeOfShaderObject = ...

class Graphic3d_LevelOfTextureAnisotropy(enum.IntEnum):
    """
    Level of anisotropy filter.
    Notice that actual quality depends on hardware capabilities!
    """

    Graphic3d_LOTA_OFF = 0

    Graphic3d_LOTA_FAST = 1

    Graphic3d_LOTA_MIDDLE = 2

    Graphic3d_LOTA_QUALITY = 3

Graphic3d_LOTA_OFF: Graphic3d_LevelOfTextureAnisotropy = ...

Graphic3d_LOTA_FAST: Graphic3d_LevelOfTextureAnisotropy = ...

Graphic3d_LOTA_MIDDLE: Graphic3d_LevelOfTextureAnisotropy = ...

Graphic3d_LOTA_QUALITY: Graphic3d_LevelOfTextureAnisotropy = ...

class Graphic3d_TextureUnit(enum.IntEnum):
    """Texture unit."""

    Graphic3d_TextureUnit_0 = 0

    Graphic3d_TextureUnit_1 = 1

    Graphic3d_TextureUnit_2 = 2

    Graphic3d_TextureUnit_3 = 3

    Graphic3d_TextureUnit_4 = 4

    Graphic3d_TextureUnit_5 = 5

    Graphic3d_TextureUnit_6 = 6

    Graphic3d_TextureUnit_7 = 7

    Graphic3d_TextureUnit_8 = 8

    Graphic3d_TextureUnit_9 = 9

    Graphic3d_TextureUnit_10 = 10

    Graphic3d_TextureUnit_11 = 11

    Graphic3d_TextureUnit_12 = 12

    Graphic3d_TextureUnit_13 = 13

    Graphic3d_TextureUnit_14 = 14

    Graphic3d_TextureUnit_15 = 15

    Graphic3d_TextureUnit_BaseColor = 0

    Graphic3d_TextureUnit_Emissive = 1

    Graphic3d_TextureUnit_Occlusion = 2

    Graphic3d_TextureUnit_Normal = 3

    Graphic3d_TextureUnit_MetallicRoughness = 4

    Graphic3d_TextureUnit_EnvMap = 0

    Graphic3d_TextureUnit_PointSprite = 1

    Graphic3d_TextureUnit_DepthPeelingDepth = -6

    Graphic3d_TextureUnit_DepthPeelingFrontColor = -5

    Graphic3d_TextureUnit_ShadowMap = -4

    Graphic3d_TextureUnit_PbrEnvironmentLUT = -3

    Graphic3d_TextureUnit_PbrIblDiffuseSH = -2

    Graphic3d_TextureUnit_PbrIblSpecular = -1

Graphic3d_TextureUnit_0: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_0

Graphic3d_TextureUnit_1: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_1

Graphic3d_TextureUnit_2: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_2

Graphic3d_TextureUnit_3: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_3

Graphic3d_TextureUnit_4: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_4

Graphic3d_TextureUnit_5: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_5

Graphic3d_TextureUnit_6: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_6

Graphic3d_TextureUnit_7: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_7

Graphic3d_TextureUnit_8: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_8

Graphic3d_TextureUnit_9: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_9

Graphic3d_TextureUnit_10: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_10

Graphic3d_TextureUnit_11: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_11

Graphic3d_TextureUnit_12: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_12

Graphic3d_TextureUnit_13: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_13

Graphic3d_TextureUnit_14: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_14

Graphic3d_TextureUnit_15: Graphic3d_TextureUnit = Graphic3d_TextureUnit.Graphic3d_TextureUnit_15

Graphic3d_TextureUnit_DepthPeelingDepth: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_DepthPeelingFrontColor: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_ShadowMap: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_PbrEnvironmentLUT: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_PbrIblDiffuseSH: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_PbrIblSpecular: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_BaseColor: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_Emissive: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_Occlusion: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_Normal: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_MetallicRoughness: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_EnvMap: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_PointSprite: Graphic3d_TextureUnit = ...

Graphic3d_TextureUnit_NB: int = 16

class Graphic3d_TypeOfTextureFilter(enum.IntEnum):
    """
    Type of the texture filter.
    Notice that for textures without mipmaps linear interpolation will be used instead of
    TOTF_BILINEAR and TOTF_TRILINEAR.
    """

    Graphic3d_TOTF_NEAREST = 0

    Graphic3d_TOTF_BILINEAR = 1

    Graphic3d_TOTF_TRILINEAR = 2

Graphic3d_TOTF_NEAREST: Graphic3d_TypeOfTextureFilter = ...

Graphic3d_TOTF_BILINEAR: Graphic3d_TypeOfTextureFilter = ...

Graphic3d_TOTF_TRILINEAR: Graphic3d_TypeOfTextureFilter = ...

class Graphic3d_TypeOfTextureMode(enum.IntEnum):
    """Type of the texture projection."""

    Graphic3d_TOTM_OBJECT = 0

    Graphic3d_TOTM_SPHERE = 1

    Graphic3d_TOTM_EYE = 2

    Graphic3d_TOTM_MANUAL = 3

    Graphic3d_TOTM_SPRITE = 4

Graphic3d_TOTM_OBJECT: Graphic3d_TypeOfTextureMode = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_OBJECT

Graphic3d_TOTM_SPHERE: Graphic3d_TypeOfTextureMode = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPHERE

Graphic3d_TOTM_EYE: Graphic3d_TypeOfTextureMode = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_EYE

Graphic3d_TOTM_MANUAL: Graphic3d_TypeOfTextureMode = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_MANUAL

Graphic3d_TOTM_SPRITE: Graphic3d_TypeOfTextureMode = Graphic3d_TypeOfTextureMode.Graphic3d_TOTM_SPRITE

class Graphic3d_TypeOfTexture(enum.IntEnum):
    """Type of the texture file format."""

    Graphic3d_TypeOfTexture_1D = 0

    Graphic3d_TypeOfTexture_2D = 1

    Graphic3d_TypeOfTexture_3D = 2

    Graphic3d_TypeOfTexture_CUBEMAP = 3

    Graphic3d_TOT_2D_MIPMAP = 4

    Graphic3d_TOT_1D = 0

    Graphic3d_TOT_2D = 1

    Graphic3d_TOT_CUBEMAP = 3

Graphic3d_TypeOfTexture_1D: Graphic3d_TypeOfTexture = ...

Graphic3d_TypeOfTexture_2D: Graphic3d_TypeOfTexture = ...

Graphic3d_TypeOfTexture_3D: Graphic3d_TypeOfTexture = ...

Graphic3d_TypeOfTexture_CUBEMAP: Graphic3d_TypeOfTexture = ...

Graphic3d_TOT_2D_MIPMAP: Graphic3d_TypeOfTexture = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D_MIPMAP

Graphic3d_TOT_1D: Graphic3d_TypeOfTexture = Graphic3d_TypeOfTexture.Graphic3d_TOT_1D

Graphic3d_TOT_2D: Graphic3d_TypeOfTexture = Graphic3d_TypeOfTexture.Graphic3d_TOT_2D

Graphic3d_TOT_CUBEMAP: Graphic3d_TypeOfTexture = Graphic3d_TypeOfTexture.Graphic3d_TOT_CUBEMAP

class Graphic3d_TypeOfBackfacingModel(enum.IntEnum):
    """Modes of display of back faces in the view."""

    Graphic3d_TypeOfBackfacingModel_Auto = 0

    Graphic3d_TypeOfBackfacingModel_DoubleSided = 1

    Graphic3d_TypeOfBackfacingModel_BackCulled = 2

    Graphic3d_TypeOfBackfacingModel_FrontCulled = 3

    Graphic3d_TOBM_AUTOMATIC = 0

    Graphic3d_TOBM_FORCE = 1

    Graphic3d_TOBM_DISABLE = 2

    V3d_TOBM_AUTOMATIC = 0

    V3d_TOBM_ALWAYS_DISPLAYED = 1

    V3d_TOBM_NEVER_DISPLAYED = 2

Graphic3d_TypeOfBackfacingModel_Auto: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TypeOfBackfacingModel_DoubleSided: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TypeOfBackfacingModel_BackCulled: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TypeOfBackfacingModel_FrontCulled: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TOBM_AUTOMATIC: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TOBM_FORCE: Graphic3d_TypeOfBackfacingModel = ...

Graphic3d_TOBM_DISABLE: Graphic3d_TypeOfBackfacingModel = ...

V3d_TOBM_AUTOMATIC: Graphic3d_TypeOfBackfacingModel = ...

V3d_TOBM_ALWAYS_DISPLAYED: Graphic3d_TypeOfBackfacingModel = ...

V3d_TOBM_NEVER_DISPLAYED: Graphic3d_TypeOfBackfacingModel = ...

class Graphic3d_TypeOfShadingModel(enum.IntEnum):
    """Definition of the color shading model."""

    Graphic3d_TypeOfShadingModel_DEFAULT = -1

    Graphic3d_TypeOfShadingModel_Unlit = 0

    Graphic3d_TypeOfShadingModel_PhongFacet = 1

    Graphic3d_TypeOfShadingModel_Gouraud = 2

    Graphic3d_TypeOfShadingModel_Phong = 3

    Graphic3d_TypeOfShadingModel_Pbr = 4

    Graphic3d_TypeOfShadingModel_PbrFacet = 5

    Graphic3d_TOSM_DEFAULT = -1

    Graphic3d_TOSM_UNLIT = 0

    Graphic3d_TOSM_FACET = 1

    Graphic3d_TOSM_VERTEX = 2

    Graphic3d_TOSM_FRAGMENT = 3

    Graphic3d_TOSM_PBR = 4

    Graphic3d_TOSM_PBR_FACET = 5

    Graphic3d_TOSM_NONE = 0

    V3d_COLOR = 0

    V3d_FLAT = 1

    V3d_GOURAUD = 2

    V3d_PHONG = 3

Graphic3d_TypeOfShadingModel_DEFAULT: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_Unlit: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_PhongFacet: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_Gouraud: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_Phong: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_Pbr: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TypeOfShadingModel_PbrFacet: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TOSM_DEFAULT: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TOSM_UNLIT: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_UNLIT

Graphic3d_TOSM_FACET: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_FACET

Graphic3d_TOSM_VERTEX: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TOSM_FRAGMENT: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TOSM_PBR: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_PBR

Graphic3d_TOSM_PBR_FACET: Graphic3d_TypeOfShadingModel = ...

Graphic3d_TOSM_NONE: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.Graphic3d_TOSM_NONE

V3d_COLOR: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.V3d_COLOR

V3d_FLAT: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.V3d_FLAT

V3d_GOURAUD: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.V3d_GOURAUD

V3d_PHONG: Graphic3d_TypeOfShadingModel = Graphic3d_TypeOfShadingModel.V3d_PHONG

Graphic3d_TypeOfShadingModel_NB: int = 6

class Graphic3d_BufferType(enum.IntEnum):
    """Define buffers available for dump"""

    Graphic3d_BT_RGB = 0

    Graphic3d_BT_RGBA = 1

    Graphic3d_BT_Depth = 2

    Graphic3d_BT_RGB_RayTraceHdrLeft = 3

    Graphic3d_BT_Red = 4

    Graphic3d_BT_ShadowMap = 5

Graphic3d_BT_RGB: Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_RGB

Graphic3d_BT_RGBA: Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_RGBA

Graphic3d_BT_Depth: Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_Depth

Graphic3d_BT_RGB_RayTraceHdrLeft: Graphic3d_BufferType = ...

Graphic3d_BT_Red: Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_Red

Graphic3d_BT_ShadowMap: Graphic3d_BufferType = Graphic3d_BufferType.Graphic3d_BT_ShadowMap

class Graphic3d_CappingFlags(enum.IntEnum):
    """Enumeration of capping flags."""

    Graphic3d_CappingFlags_None = 0

    Graphic3d_CappingFlags_ObjectMaterial = 1

    Graphic3d_CappingFlags_ObjectTexture = 2

    Graphic3d_CappingFlags_ObjectShader = 8

    Graphic3d_CappingFlags_ObjectAspect = 11

Graphic3d_CappingFlags_None: Graphic3d_CappingFlags = ...

Graphic3d_CappingFlags_ObjectMaterial: Graphic3d_CappingFlags = ...

Graphic3d_CappingFlags_ObjectTexture: Graphic3d_CappingFlags = ...

Graphic3d_CappingFlags_ObjectShader: Graphic3d_CappingFlags = ...

Graphic3d_CappingFlags_ObjectAspect: Graphic3d_CappingFlags = ...

class Graphic3d_TypeOfLightSource(enum.IntEnum):
    """Definition of all the type of light source."""

    Graphic3d_TypeOfLightSource_Ambient = 0

    Graphic3d_TypeOfLightSource_Directional = 1

    Graphic3d_TypeOfLightSource_Positional = 2

    Graphic3d_TypeOfLightSource_Spot = 3

    Graphic3d_TOLS_AMBIENT = 0

    Graphic3d_TOLS_DIRECTIONAL = 1

    Graphic3d_TOLS_POSITIONAL = 2

    Graphic3d_TOLS_SPOT = 3

    V3d_AMBIENT = 0

    V3d_DIRECTIONAL = 1

    V3d_POSITIONAL = 2

    V3d_SPOT = 3

Graphic3d_TypeOfLightSource_Ambient: Graphic3d_TypeOfLightSource = ...

Graphic3d_TypeOfLightSource_Directional: Graphic3d_TypeOfLightSource = ...

Graphic3d_TypeOfLightSource_Positional: Graphic3d_TypeOfLightSource = ...

Graphic3d_TypeOfLightSource_Spot: Graphic3d_TypeOfLightSource = ...

Graphic3d_TOLS_AMBIENT: Graphic3d_TypeOfLightSource = ...

Graphic3d_TOLS_DIRECTIONAL: Graphic3d_TypeOfLightSource = ...

Graphic3d_TOLS_POSITIONAL: Graphic3d_TypeOfLightSource = ...

Graphic3d_TOLS_SPOT: Graphic3d_TypeOfLightSource = Graphic3d_TypeOfLightSource.Graphic3d_TOLS_SPOT

V3d_AMBIENT: Graphic3d_TypeOfLightSource = Graphic3d_TypeOfLightSource.V3d_AMBIENT

V3d_DIRECTIONAL: Graphic3d_TypeOfLightSource = Graphic3d_TypeOfLightSource.V3d_DIRECTIONAL

V3d_POSITIONAL: Graphic3d_TypeOfLightSource = Graphic3d_TypeOfLightSource.V3d_POSITIONAL

V3d_SPOT: Graphic3d_TypeOfLightSource = Graphic3d_TypeOfLightSource.V3d_SPOT

Graphic3d_TypeOfLightSource_NB: int = 4

class Graphic3d_ClipState(enum.IntEnum):
    """Clipping state."""

    Graphic3d_ClipState_Out = 0

    Graphic3d_ClipState_In = 1

    Graphic3d_ClipState_On = 2

Graphic3d_ClipState_Out: Graphic3d_ClipState = Graphic3d_ClipState.Graphic3d_ClipState_Out

Graphic3d_ClipState_In: Graphic3d_ClipState = Graphic3d_ClipState.Graphic3d_ClipState_In

Graphic3d_ClipState_On: Graphic3d_ClipState = Graphic3d_ClipState.Graphic3d_ClipState_On

class Graphic3d_DisplayPriority(enum.IntEnum):
    """
    Structure priority - range (do not change this range!).
    Values are between 0 and 10, with 5 used by default.
    A structure of priority 10 is displayed the last and appears over the others (considering depth
    test).
    """

    Graphic3d_DisplayPriority_INVALID = -1

    Graphic3d_DisplayPriority_Bottom = 0

    Graphic3d_DisplayPriority_AlmostBottom = 1

    Graphic3d_DisplayPriority_Below2 = 2

    Graphic3d_DisplayPriority_Below1 = 3

    Graphic3d_DisplayPriority_Below = 4

    Graphic3d_DisplayPriority_Normal = 5

    Graphic3d_DisplayPriority_Above = 6

    Graphic3d_DisplayPriority_Above1 = 7

    Graphic3d_DisplayPriority_Above2 = 8

    Graphic3d_DisplayPriority_Highlight = 9

    Graphic3d_DisplayPriority_Topmost = 10

Graphic3d_DisplayPriority_INVALID: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Bottom: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_AlmostBottom: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Below2: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Below1: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Below: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Normal: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Above: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Above1: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Above2: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Highlight: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_Topmost: Graphic3d_DisplayPriority = ...

Graphic3d_DisplayPriority_NB: int = 11

Graphic3d_ZLayerId_UNKNOWN: int = -1

Graphic3d_ZLayerId_Default: int = 0

Graphic3d_ZLayerId_Top: int = -2

Graphic3d_ZLayerId_Topmost: int = -3

Graphic3d_ZLayerId_TopOSD: int = -4

Graphic3d_ZLayerId_BotOSD: int = -5

class Graphic3d_TextPath(enum.IntEnum):
    """Direction in which text is displayed."""

    Graphic3d_TP_UP = 0

    Graphic3d_TP_DOWN = 1

    Graphic3d_TP_LEFT = 2

    Graphic3d_TP_RIGHT = 3

Graphic3d_TP_UP: Graphic3d_TextPath = Graphic3d_TextPath.Graphic3d_TP_UP

Graphic3d_TP_DOWN: Graphic3d_TextPath = Graphic3d_TextPath.Graphic3d_TP_DOWN

Graphic3d_TP_LEFT: Graphic3d_TextPath = Graphic3d_TextPath.Graphic3d_TP_LEFT

Graphic3d_TP_RIGHT: Graphic3d_TextPath = Graphic3d_TextPath.Graphic3d_TP_RIGHT

class Graphic3d_HorizontalTextAlignment(enum.IntEnum):
    """
    Defines the horizontal position of the text
    relative to its anchor.
    """

    Graphic3d_HTA_LEFT = 0

    Graphic3d_HTA_CENTER = 1

    Graphic3d_HTA_RIGHT = 2

Graphic3d_HTA_LEFT: Graphic3d_HorizontalTextAlignment = ...

Graphic3d_HTA_CENTER: Graphic3d_HorizontalTextAlignment = ...

Graphic3d_HTA_RIGHT: Graphic3d_HorizontalTextAlignment = ...

class Graphic3d_VerticalTextAlignment(enum.IntEnum):
    """
    Defines the vertical position of the text
    relative to its anchor.
    """

    Graphic3d_VTA_BOTTOM = 0

    Graphic3d_VTA_CENTER = 1

    Graphic3d_VTA_TOP = 2

    Graphic3d_VTA_TOPFIRSTLINE = 3

Graphic3d_VTA_BOTTOM: Graphic3d_VerticalTextAlignment = ...

Graphic3d_VTA_CENTER: Graphic3d_VerticalTextAlignment = ...

Graphic3d_VTA_TOP: Graphic3d_VerticalTextAlignment = Graphic3d_VerticalTextAlignment.Graphic3d_VTA_TOP

Graphic3d_VTA_TOPFIRSTLINE: Graphic3d_VerticalTextAlignment = ...

class Graphic3d_TransModeFlags(enum.IntEnum):
    """
    Transform Persistence Mode defining whether to lock in object position, rotation and / or
    zooming relative to camera position.
    """

    Graphic3d_TMF_None = 0

    Graphic3d_TMF_ZoomPers = 2

    Graphic3d_TMF_RotatePers = 8

    Graphic3d_TMF_TriedronPers = 32

    Graphic3d_TMF_2d = 64

    Graphic3d_TMF_CameraPers = 128

    Graphic3d_TMF_OrthoPers = 256

    Graphic3d_TMF_AxialScalePers = 512

    Graphic3d_TMF_ZoomRotatePers = 10

    Graphic3d_TMF_AxialZoomPers = 514

Graphic3d_TMF_None: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_None

Graphic3d_TMF_ZoomPers: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_ZoomPers

Graphic3d_TMF_RotatePers: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_RotatePers

Graphic3d_TMF_TriedronPers: Graphic3d_TransModeFlags = ...

Graphic3d_TMF_2d: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_2d

Graphic3d_TMF_CameraPers: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_CameraPers

Graphic3d_TMF_OrthoPers: Graphic3d_TransModeFlags = Graphic3d_TransModeFlags.Graphic3d_TMF_OrthoPers

Graphic3d_TMF_AxialScalePers: Graphic3d_TransModeFlags = ...

Graphic3d_TMF_ZoomRotatePers: Graphic3d_TransModeFlags = ...

Graphic3d_TMF_AxialZoomPers: Graphic3d_TransModeFlags = ...

class Graphic3d_CubeMapSide(enum.IntEnum):
    """Sides of cubemap in order of OpenGL rules"""

    Graphic3d_CMS_POS_X = 0

    Graphic3d_CMS_NEG_X = 1

    Graphic3d_CMS_POS_Y = 2

    Graphic3d_CMS_NEG_Y = 3

    Graphic3d_CMS_POS_Z = 4

    Graphic3d_CMS_NEG_Z = 5

Graphic3d_CMS_POS_X: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_X

Graphic3d_CMS_NEG_X: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_X

Graphic3d_CMS_POS_Y: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Y

Graphic3d_CMS_NEG_Y: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Y

Graphic3d_CMS_POS_Z: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_POS_Z

Graphic3d_CMS_NEG_Z: Graphic3d_CubeMapSide = Graphic3d_CubeMapSide.Graphic3d_CMS_NEG_Z

class Graphic3d_DiagnosticInfo(enum.IntEnum):
    """Diagnostic info categories bit flags."""

    Graphic3d_DiagnosticInfo_Device = 1

    Graphic3d_DiagnosticInfo_FrameBuffer = 2

    Graphic3d_DiagnosticInfo_Limits = 4

    Graphic3d_DiagnosticInfo_Memory = 8

    Graphic3d_DiagnosticInfo_NativePlatform = 16

    Graphic3d_DiagnosticInfo_Extensions = 32

    Graphic3d_DiagnosticInfo_Short = 7

    Graphic3d_DiagnosticInfo_Basic = 31

    Graphic3d_DiagnosticInfo_Complete = 63

Graphic3d_DiagnosticInfo_Device: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_FrameBuffer: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Limits: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Memory: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_NativePlatform: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Extensions: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Short: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Basic: Graphic3d_DiagnosticInfo = ...

Graphic3d_DiagnosticInfo_Complete: Graphic3d_DiagnosticInfo = ...

class Graphic3d_RenderingMode(enum.IntEnum):
    """
    Describes rendering modes.
    - RM_RASTERIZATION: enables OpenGL rasterization mode;
    - RM_RAYTRACING: enables GPU ray-tracing mode.
    """

    Graphic3d_RM_RASTERIZATION = 0

    Graphic3d_RM_RAYTRACING = 1

Graphic3d_RM_RASTERIZATION: Graphic3d_RenderingMode = ...

Graphic3d_RM_RAYTRACING: Graphic3d_RenderingMode = Graphic3d_RenderingMode.Graphic3d_RM_RAYTRACING

class Graphic3d_StereoMode(enum.IntEnum):
    """This enumeration defines the list of stereoscopic output modes."""

    Graphic3d_StereoMode_QuadBuffer = 0

    Graphic3d_StereoMode_Anaglyph = 1

    Graphic3d_StereoMode_RowInterlaced = 2

    Graphic3d_StereoMode_ColumnInterlaced = 3

    Graphic3d_StereoMode_ChessBoard = 4

    Graphic3d_StereoMode_SideBySide = 5

    Graphic3d_StereoMode_OverUnder = 6

    Graphic3d_StereoMode_SoftPageFlip = 7

    Graphic3d_StereoMode_OpenVR = 8

Graphic3d_StereoMode_QuadBuffer: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_Anaglyph: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_RowInterlaced: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_ColumnInterlaced: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_ChessBoard: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_SideBySide: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_OverUnder: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_SoftPageFlip: Graphic3d_StereoMode = ...

Graphic3d_StereoMode_OpenVR: Graphic3d_StereoMode = Graphic3d_StereoMode.Graphic3d_StereoMode_OpenVR

Graphic3d_StereoMode_NB: int = 9

class Graphic3d_ToneMappingMethod(enum.IntEnum):
    """Enumerates tone mapping methods."""

    Graphic3d_ToneMappingMethod_Disabled = 0

    Graphic3d_ToneMappingMethod_Filmic = 1

Graphic3d_ToneMappingMethod_Disabled: Graphic3d_ToneMappingMethod = ...

Graphic3d_ToneMappingMethod_Filmic: Graphic3d_ToneMappingMethod = ...

class Graphic3d_TypeOfConnection(enum.IntEnum):
    """To manage the connections between the structures."""

    Graphic3d_TOC_ANCESTOR = 0

    Graphic3d_TOC_DESCENDANT = 1

Graphic3d_TOC_ANCESTOR: Graphic3d_TypeOfConnection = Graphic3d_TypeOfConnection.Graphic3d_TOC_ANCESTOR

Graphic3d_TOC_DESCENDANT: Graphic3d_TypeOfConnection = ...

class Graphic3d_TypeOfStructure(enum.IntEnum):
    """
    Structural attribute indicating if it can be displayed
    in wireframe, shadow mode, or both.
    """

    Graphic3d_TOS_WIREFRAME = 0

    Graphic3d_TOS_SHADING = 1

    Graphic3d_TOS_COMPUTED = 2

    Graphic3d_TOS_ALL = 3

Graphic3d_TOS_WIREFRAME: Graphic3d_TypeOfStructure = Graphic3d_TypeOfStructure.Graphic3d_TOS_WIREFRAME

Graphic3d_TOS_SHADING: Graphic3d_TypeOfStructure = Graphic3d_TypeOfStructure.Graphic3d_TOS_SHADING

Graphic3d_TOS_COMPUTED: Graphic3d_TypeOfStructure = Graphic3d_TypeOfStructure.Graphic3d_TOS_COMPUTED

Graphic3d_TOS_ALL: Graphic3d_TypeOfStructure = Graphic3d_TypeOfStructure.Graphic3d_TOS_ALL

class Graphic3d_NameOfTextureEnv(enum.IntEnum):
    """Types of standard textures."""

    Graphic3d_NOT_ENV_CLOUDS = 0

    Graphic3d_NOT_ENV_CV = 1

    Graphic3d_NOT_ENV_MEDIT = 2

    Graphic3d_NOT_ENV_PEARL = 3

    Graphic3d_NOT_ENV_SKY1 = 4

    Graphic3d_NOT_ENV_SKY2 = 5

    Graphic3d_NOT_ENV_LINES = 6

    Graphic3d_NOT_ENV_ROAD = 7

    Graphic3d_NOT_ENV_UNKNOWN = 8

Graphic3d_NOT_ENV_CLOUDS: Graphic3d_NameOfTextureEnv = ...

Graphic3d_NOT_ENV_CV: Graphic3d_NameOfTextureEnv = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_CV

Graphic3d_NOT_ENV_MEDIT: Graphic3d_NameOfTextureEnv = ...

Graphic3d_NOT_ENV_PEARL: Graphic3d_NameOfTextureEnv = ...

Graphic3d_NOT_ENV_SKY1: Graphic3d_NameOfTextureEnv = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY1

Graphic3d_NOT_ENV_SKY2: Graphic3d_NameOfTextureEnv = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_SKY2

Graphic3d_NOT_ENV_LINES: Graphic3d_NameOfTextureEnv = ...

Graphic3d_NOT_ENV_ROAD: Graphic3d_NameOfTextureEnv = Graphic3d_NameOfTextureEnv.Graphic3d_NOT_ENV_ROAD

Graphic3d_NOT_ENV_UNKNOWN: Graphic3d_NameOfTextureEnv = ...

class Graphic3d_TypeOfAnswer(enum.IntEnum):
    """
    The answer of the method AcceptDisplay
    AcceptDisplay means is it possible to display the
    specified structure in the specified view ?
    TOA_YES yes
    TOA_NO  no
    TOA_COMPUTE yes but we have to compute the representation
    """

    Graphic3d_TOA_YES = 0

    Graphic3d_TOA_NO = 1

    Graphic3d_TOA_COMPUTE = 2

Graphic3d_TOA_YES: Graphic3d_TypeOfAnswer = Graphic3d_TypeOfAnswer.Graphic3d_TOA_YES

Graphic3d_TOA_NO: Graphic3d_TypeOfAnswer = Graphic3d_TypeOfAnswer.Graphic3d_TOA_NO

Graphic3d_TOA_COMPUTE: Graphic3d_TypeOfAnswer = Graphic3d_TypeOfAnswer.Graphic3d_TOA_COMPUTE

class Graphic3d_TypeOfBackground(enum.IntEnum):
    """Describes type of view background."""

    Graphic3d_TOB_NONE = -1

    Graphic3d_TOB_GRADIENT = 0

    Graphic3d_TOB_TEXTURE = 1

    Graphic3d_TOB_CUBEMAP = 2

Graphic3d_TOB_NONE: Graphic3d_TypeOfBackground = Graphic3d_TypeOfBackground.Graphic3d_TOB_NONE

Graphic3d_TOB_GRADIENT: Graphic3d_TypeOfBackground = Graphic3d_TypeOfBackground.Graphic3d_TOB_GRADIENT

Graphic3d_TOB_TEXTURE: Graphic3d_TypeOfBackground = Graphic3d_TypeOfBackground.Graphic3d_TOB_TEXTURE

Graphic3d_TOB_CUBEMAP: Graphic3d_TypeOfBackground = Graphic3d_TypeOfBackground.Graphic3d_TOB_CUBEMAP

Graphic3d_TypeOfBackground_NB: int = 3

class Graphic3d_TypeOfVisualization(enum.IntEnum):
    """
    Modes of visualisation of objects in a view

    TOV_WIREFRAME   wireframe visualisation
    TOV_SHADING     shaded visualisation
    """

    Graphic3d_TOV_WIREFRAME = 0

    Graphic3d_TOV_SHADING = 1

Graphic3d_TOV_WIREFRAME: Graphic3d_TypeOfVisualization = ...

Graphic3d_TOV_SHADING: Graphic3d_TypeOfVisualization = ...

class Graphic3d_FrameStatsCounter(enum.IntEnum):
    """Stats counter."""

    Graphic3d_FrameStatsCounter_NbLayers = 0

    Graphic3d_FrameStatsCounter_NbStructs = 1

    Graphic3d_FrameStatsCounter_EstimatedBytesGeom = 2

    Graphic3d_FrameStatsCounter_EstimatedBytesFbos = 3

    Graphic3d_FrameStatsCounter_EstimatedBytesTextures = 4

    Graphic3d_FrameStatsCounter_NbLayersNotCulled = 5

    Graphic3d_FrameStatsCounter_NbStructsNotCulled = 6

    Graphic3d_FrameStatsCounter_NbGroupsNotCulled = 7

    Graphic3d_FrameStatsCounter_NbElemsNotCulled = 8

    Graphic3d_FrameStatsCounter_NbElemsFillNotCulled = 9

    Graphic3d_FrameStatsCounter_NbElemsLineNotCulled = 10

    Graphic3d_FrameStatsCounter_NbElemsPointNotCulled = 11

    Graphic3d_FrameStatsCounter_NbElemsTextNotCulled = 12

    Graphic3d_FrameStatsCounter_NbTrianglesNotCulled = 13

    Graphic3d_FrameStatsCounter_NbLinesNotCulled = 14

    Graphic3d_FrameStatsCounter_NbPointsNotCulled = 15

    Graphic3d_FrameStatsCounter_NbLayersImmediate = 16

    Graphic3d_FrameStatsCounter_NbStructsImmediate = 17

    Graphic3d_FrameStatsCounter_NbGroupsImmediate = 18

    Graphic3d_FrameStatsCounter_NbElemsImmediate = 19

    Graphic3d_FrameStatsCounter_NbElemsFillImmediate = 20

    Graphic3d_FrameStatsCounter_NbElemsLineImmediate = 21

    Graphic3d_FrameStatsCounter_NbElemsPointImmediate = 22

    Graphic3d_FrameStatsCounter_NbElemsTextImmediate = 23

    Graphic3d_FrameStatsCounter_NbTrianglesImmediate = 24

    Graphic3d_FrameStatsCounter_NbLinesImmediate = 25

    Graphic3d_FrameStatsCounter_NbPointsImmediate = 26

Graphic3d_FrameStatsCounter_NbLayers: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbStructs: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_EstimatedBytesGeom: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_EstimatedBytesFbos: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_EstimatedBytesTextures: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbLayersNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbStructsNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbGroupsNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsFillNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsLineNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsPointNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsTextNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbTrianglesNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbLinesNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbPointsNotCulled: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbLayersImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbStructsImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbGroupsImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsFillImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsLineImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsPointImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbElemsTextImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbTrianglesImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbLinesImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NbPointsImmediate: Graphic3d_FrameStatsCounter = ...

Graphic3d_FrameStatsCounter_NB: int = 27

Graphic3d_FrameStatsCounter_SCENE_LOWER: int = 0

Graphic3d_FrameStatsCounter_SCENE_UPPER: int = 4

Graphic3d_FrameStatsCounter_RENDERED_LOWER: int = 5

Graphic3d_FrameStatsCounter_RENDERED_UPPER: int = 15

Graphic3d_FrameStatsCounter_IMMEDIATE_LOWER: int = 16

Graphic3d_FrameStatsCounter_IMMEDIATE_UPPER: int = 26

class Graphic3d_FrameStatsTimer(enum.IntEnum):
    """Timers for collecting frame performance statistics."""

    Graphic3d_FrameStatsTimer_ElapsedFrame = 0

    Graphic3d_FrameStatsTimer_CpuFrame = 1

    Graphic3d_FrameStatsTimer_CpuCulling = 2

    Graphic3d_FrameStatsTimer_CpuPicking = 3

    Graphic3d_FrameStatsTimer_CpuDynamics = 4

Graphic3d_FrameStatsTimer_ElapsedFrame: Graphic3d_FrameStatsTimer = ...

Graphic3d_FrameStatsTimer_CpuFrame: Graphic3d_FrameStatsTimer = ...

Graphic3d_FrameStatsTimer_CpuCulling: Graphic3d_FrameStatsTimer = ...

Graphic3d_FrameStatsTimer_CpuPicking: Graphic3d_FrameStatsTimer = ...

Graphic3d_FrameStatsTimer_CpuDynamics: Graphic3d_FrameStatsTimer = ...

Graphic3d_FrameStatsTimer_NB: int = 5

class Graphic3d_TypeOfLimit(enum.IntEnum):
    """Type of graphic resource limit."""

    Graphic3d_TypeOfLimit_MaxNbLights = 0

    Graphic3d_TypeOfLimit_MaxNbClipPlanes = 1

    Graphic3d_TypeOfLimit_MaxNbViews = 2

    Graphic3d_TypeOfLimit_MaxTextureSize = 3

    Graphic3d_TypeOfLimit_MaxViewDumpSizeX = 4

    Graphic3d_TypeOfLimit_MaxViewDumpSizeY = 5

    Graphic3d_TypeOfLimit_MaxCombinedTextureUnits = 6

    Graphic3d_TypeOfLimit_MaxMsaa = 7

    Graphic3d_TypeOfLimit_HasPBR = 8

    Graphic3d_TypeOfLimit_HasRayTracing = 9

    Graphic3d_TypeOfLimit_HasRayTracingTextures = 10

    Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling = 11

    Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic = 12

    Graphic3d_TypeOfLimit_HasSRGB = 13

    Graphic3d_TypeOfLimit_HasBlendedOit = 14

    Graphic3d_TypeOfLimit_HasBlendedOitMsaa = 15

    Graphic3d_TypeOfLimit_HasFlatShading = 16

    Graphic3d_TypeOfLimit_HasMeshEdges = 17

    Graphic3d_TypeOfLimit_IsWorkaroundFBO = 18

    Graphic3d_TypeOfLimit_NB = 19

Graphic3d_TypeOfLimit_MaxNbLights: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxNbClipPlanes: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxNbViews: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxTextureSize: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxViewDumpSizeX: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxViewDumpSizeY: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxCombinedTextureUnits: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_MaxMsaa: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasPBR: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasRayTracing: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasRayTracingTextures: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSampling: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasRayTracingAdaptiveSamplingAtomic: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasSRGB: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasBlendedOit: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasBlendedOitMsaa: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasFlatShading: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_HasMeshEdges: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_IsWorkaroundFBO: Graphic3d_TypeOfLimit = ...

Graphic3d_TypeOfLimit_NB: Graphic3d_TypeOfLimit = Graphic3d_TypeOfLimit.Graphic3d_TypeOfLimit_NB

class Graphic3d_GroupAspect(enum.IntEnum):
    """
    Identifies primitives aspects defined per group.
    - ASPECT_LINE: aspect for line primitives;
    - ASPECT_TEXT: aspect for text primitives;
    - ASPECT_MARKER: aspect for marker primitives;
    - ASPECT_FILL_AREA: aspect for face primitives.
    """

    Graphic3d_ASPECT_LINE = 0

    Graphic3d_ASPECT_TEXT = 1

    Graphic3d_ASPECT_MARKER = 2

    Graphic3d_ASPECT_FILL_AREA = 3

Graphic3d_ASPECT_LINE: Graphic3d_GroupAspect = Graphic3d_GroupAspect.Graphic3d_ASPECT_LINE

Graphic3d_ASPECT_TEXT: Graphic3d_GroupAspect = Graphic3d_GroupAspect.Graphic3d_ASPECT_TEXT

Graphic3d_ASPECT_MARKER: Graphic3d_GroupAspect = Graphic3d_GroupAspect.Graphic3d_ASPECT_MARKER

Graphic3d_ASPECT_FILL_AREA: Graphic3d_GroupAspect = Graphic3d_GroupAspect.Graphic3d_ASPECT_FILL_AREA

class Graphic3d_NameOfTexture2D(enum.IntEnum):
    """Types of standard textures."""

    Graphic3d_NOT_2D_MATRA = 0

    Graphic3d_NOT_2D_ALIENSKIN = 1

    Graphic3d_NOT_2D_BLUE_ROCK = 2

    Graphic3d_NOT_2D_BLUEWHITE_PAPER = 3

    Graphic3d_NOT_2D_BRUSHED = 4

    Graphic3d_NOT_2D_BUBBLES = 5

    Graphic3d_NOT_2D_BUMP = 6

    Graphic3d_NOT_2D_CAST = 7

    Graphic3d_NOT_2D_CHIPBD = 8

    Graphic3d_NOT_2D_CLOUDS = 9

    Graphic3d_NOT_2D_FLESH = 10

    Graphic3d_NOT_2D_FLOOR = 11

    Graphic3d_NOT_2D_GALVNISD = 12

    Graphic3d_NOT_2D_GRASS = 13

    Graphic3d_NOT_2D_ALUMINUM = 14

    Graphic3d_NOT_2D_ROCK = 15

    Graphic3d_NOT_2D_KNURL = 16

    Graphic3d_NOT_2D_MAPLE = 17

    Graphic3d_NOT_2D_MARBLE = 18

    Graphic3d_NOT_2D_MOTTLED = 19

    Graphic3d_NOT_2D_RAIN = 20

    Graphic3d_NOT_2D_CHESS = 21

    Graphic3d_NOT_2D_UNKNOWN = 22

Graphic3d_NOT_2D_MATRA: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MATRA

Graphic3d_NOT_2D_ALIENSKIN: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_BLUE_ROCK: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_BLUEWHITE_PAPER: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_BRUSHED: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_BUBBLES: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_BUMP: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_BUMP

Graphic3d_NOT_2D_CAST: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CAST

Graphic3d_NOT_2D_CHIPBD: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHIPBD

Graphic3d_NOT_2D_CLOUDS: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CLOUDS

Graphic3d_NOT_2D_FLESH: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLESH

Graphic3d_NOT_2D_FLOOR: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_FLOOR

Graphic3d_NOT_2D_GALVNISD: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_GRASS: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_GRASS

Graphic3d_NOT_2D_ALUMINUM: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_ROCK: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_ROCK

Graphic3d_NOT_2D_KNURL: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_KNURL

Graphic3d_NOT_2D_MAPLE: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MAPLE

Graphic3d_NOT_2D_MARBLE: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_MARBLE

Graphic3d_NOT_2D_MOTTLED: Graphic3d_NameOfTexture2D = ...

Graphic3d_NOT_2D_RAIN: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_RAIN

Graphic3d_NOT_2D_CHESS: Graphic3d_NameOfTexture2D = Graphic3d_NameOfTexture2D.Graphic3d_NOT_2D_CHESS

Graphic3d_NOT_2D_UNKNOWN: Graphic3d_NameOfTexture2D = ...

class Graphic3d_NameOfTexture1D(enum.IntEnum):
    """Types of standard textures."""

    Graphic3d_NOT_1D_ELEVATION = 0

    Graphic3d_NOT_1D_UNKNOWN = 1

Graphic3d_NOT_1D_ELEVATION: Graphic3d_NameOfTexture1D = ...

Graphic3d_NOT_1D_UNKNOWN: Graphic3d_NameOfTexture1D = ...

class Graphic3d_NameOfTexturePlane(enum.IntEnum):
    """
    Type of the texture projection plane for both S and T texture coordinate.
    """

    Graphic3d_NOTP_XY = 0

    Graphic3d_NOTP_YZ = 1

    Graphic3d_NOTP_ZX = 2

    Graphic3d_NOTP_UNKNOWN = 3

Graphic3d_NOTP_XY: Graphic3d_NameOfTexturePlane = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_XY

Graphic3d_NOTP_YZ: Graphic3d_NameOfTexturePlane = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_YZ

Graphic3d_NOTP_ZX: Graphic3d_NameOfTexturePlane = Graphic3d_NameOfTexturePlane.Graphic3d_NOTP_ZX

Graphic3d_NOTP_UNKNOWN: Graphic3d_NameOfTexturePlane = ...

class Graphic3d_ShaderFlags(enum.IntEnum):
    """Standard GLSL program combination bits."""

    Graphic3d_ShaderFlags_VertColor = 1

    Graphic3d_ShaderFlags_TextureRGB = 2

    Graphic3d_ShaderFlags_TextureEnv = 4

    Graphic3d_ShaderFlags_TextureNormal = 6

    Graphic3d_ShaderFlags_PointSimple = 8

    Graphic3d_ShaderFlags_PointSprite = 16

    Graphic3d_ShaderFlags_PointSpriteA = 24

    Graphic3d_ShaderFlags_StippleLine = 32

    Graphic3d_ShaderFlags_ClipPlanes1 = 64

    Graphic3d_ShaderFlags_ClipPlanes2 = 128

    Graphic3d_ShaderFlags_ClipPlanesN = 192

    Graphic3d_ShaderFlags_ClipChains = 256

    Graphic3d_ShaderFlags_MeshEdges = 512

    Graphic3d_ShaderFlags_AlphaTest = 1024

    Graphic3d_ShaderFlags_WriteOit = 2048

    Graphic3d_ShaderFlags_OitDepthPeeling = 4096

    Graphic3d_ShaderFlags_VertColorFrontOnly = 8192

    Graphic3d_ShaderFlags_NB = 16384

    Graphic3d_ShaderFlags_IsPoint = 24

    Graphic3d_ShaderFlags_HasTextures = 6

    Graphic3d_ShaderFlags_NeedsGeomShader = 512

Graphic3d_ShaderFlags_VertColor: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_TextureRGB: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_TextureEnv: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_TextureNormal: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_PointSimple: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_PointSprite: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_PointSpriteA: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_StippleLine: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_ClipPlanes1: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_ClipPlanes2: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_ClipPlanesN: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_ClipChains: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_MeshEdges: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_AlphaTest: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_WriteOit: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_OitDepthPeeling: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_VertColorFrontOnly: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_NB: Graphic3d_ShaderFlags = Graphic3d_ShaderFlags.Graphic3d_ShaderFlags_NB

Graphic3d_ShaderFlags_IsPoint: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_HasTextures: Graphic3d_ShaderFlags = ...

Graphic3d_ShaderFlags_NeedsGeomShader: Graphic3d_ShaderFlags = ...

class Graphic3d_GlslExtension(enum.IntEnum):
    """GLSL syntax extensions."""

    Graphic3d_GlslExtension_GL_OES_standard_derivatives = 0

    Graphic3d_GlslExtension_GL_EXT_shader_texture_lod = 1

    Graphic3d_GlslExtension_GL_EXT_frag_depth = 2

    Graphic3d_GlslExtension_GL_EXT_gpu_shader4 = 3

Graphic3d_GlslExtension_GL_OES_standard_derivatives: Graphic3d_GlslExtension = ...

Graphic3d_GlslExtension_GL_EXT_shader_texture_lod: Graphic3d_GlslExtension = ...

Graphic3d_GlslExtension_GL_EXT_frag_depth: Graphic3d_GlslExtension = ...

Graphic3d_GlslExtension_GL_EXT_gpu_shader4: Graphic3d_GlslExtension = ...

Graphic3d_GlslExtension_NB: int = 4

class Graphic3d_TextureSetBits(enum.IntEnum):
    """Standard texture units combination bits."""

    Graphic3d_TextureSetBits_NONE = 0

    Graphic3d_TextureSetBits_BaseColor = 1

    Graphic3d_TextureSetBits_Emissive = 2

    Graphic3d_TextureSetBits_Occlusion = 4

    Graphic3d_TextureSetBits_Normal = 8

    Graphic3d_TextureSetBits_MetallicRoughness = 16

Graphic3d_TextureSetBits_NONE: Graphic3d_TextureSetBits = ...

Graphic3d_TextureSetBits_BaseColor: Graphic3d_TextureSetBits = ...

Graphic3d_TextureSetBits_Emissive: Graphic3d_TextureSetBits = ...

Graphic3d_TextureSetBits_Occlusion: Graphic3d_TextureSetBits = ...

Graphic3d_TextureSetBits_Normal: Graphic3d_TextureSetBits = ...

Graphic3d_TextureSetBits_MetallicRoughness: Graphic3d_TextureSetBits = ...

class Graphic3d_BufferRange:
    """Range of values defined as Start + Length pair."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theStart: int, theLength: int) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_BufferRange) -> None: ...

    def IsEmpty(self) -> bool:
        """Return TRUE if range is empty."""

    def Upper(self) -> int:
        """Return the Upper element within the range"""

    def Clear(self) -> None:
        """Clear the range."""

    def Unite(self, theRange: Graphic3d_BufferRange) -> None:
        """Add another range to this one."""

    @property
    def Start(self) -> int:
        """first element within the range"""

    @Start.setter
    def Start(self, arg: int, /) -> None: ...

    @property
    def Length(self) -> int:
        """number of elements within the range"""

    @Length.setter
    def Length(self, arg: int, /) -> None: ...

class Graphic3d_Attribute:
    """Vertex attribute definition."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_Attribute) -> None: ...

    def Stride(self) -> int: ...

    @staticmethod
    def Stride_s(theType: Graphic3d_TypeOfData) -> int:
        """@return size of attribute of specified data type"""

    @property
    def Id(self) -> Graphic3d_TypeOfAttribute:
        """
        attribute identifier in vertex shader, 0 is reserved for vertex position
        """

    @Id.setter
    def Id(self, arg: Graphic3d_TypeOfAttribute, /) -> None: ...

    @property
    def DataType(self) -> Graphic3d_TypeOfData:
        """vec2,vec3,vec4,vec4ub"""

    @DataType.setter
    def DataType(self, arg: Graphic3d_TypeOfData, /) -> None: ...

class Graphic3d_Buffer(nanoocp.NCollection.NCollection_Buffer):
    """Buffer of vertex attributes."""

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_Buffer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def DefaultAllocator() -> nanoocp.NCollection.NCollection_BaseAllocator:
        """Return default vertex data allocator."""

    def NbMaxElements(self) -> int:
        """
        Return number of initially allocated elements which can fit into this buffer,
        while NbElements can be overwritten to smaller value.
        """

    def AttributesArray(self) -> Graphic3d_Attribute:
        """@return array of attributes definitions"""

    def Attribute(self, theAttribIndex: int) -> Graphic3d_Attribute:
        """@return attribute definition"""

    def ChangeAttribute(self, theAttribIndex: int) -> Graphic3d_Attribute:
        """@return attribute definition"""

    def FindAttribute(self, theAttrib: Graphic3d_TypeOfAttribute) -> int:
        """
        Find attribute index.
        @param theAttrib attribute to find
        @return attribute index or -1 if not found
        """

    def AttributeOffset(self, theAttribIndex: int) -> int:
        """@return data offset to specified attribute"""

    def release(self) -> None:
        """Release buffer."""

    @overload
    def Init(self, theNbElems: int, theAttribs: Graphic3d_Attribute, theNbAttribs: int) -> bool: ...

    @overload
    def Init(self, theNbElems: int, theAttribs: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_Attribute]) -> bool:
        """Allocates new empty array"""

    def IsInterleaved(self) -> bool:
        """
        Flag indicating that attributes in the buffer are interleaved; TRUE by default.
        Requires sub-classing for creating a non-interleaved buffer (advanced usage).
        """

    def IsMutable(self) -> bool:
        """
        Return TRUE if data can be invalidated; FALSE by default.
        Requires sub-classing for creating a mutable buffer (advanced usage).
        """

    def InvalidatedRange(self) -> Graphic3d_BufferRange:
        """
        Return invalidated range; EMPTY by default.
        Requires sub-classing for creating a mutable buffer (advanced usage).
        """

    def Validate(self) -> None:
        """
        Reset invalidated range.
        Requires sub-classing for creating a mutable buffer (advanced usage).
        """

    def Invalidate(self) -> None:
        """Invalidate entire buffer."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def Stride(self) -> int:
        """
        the distance to the attributes of the next vertex within interleaved array
        """

    @Stride.setter
    def Stride(self, arg: int, /) -> None: ...

    @property
    def NbElements(self) -> int:
        """
        number of the elements (@sa NbMaxElements() specifying the number of initially allocated number of elements)
        """

    @NbElements.setter
    def NbElements(self, arg: int, /) -> None: ...

    @property
    def NbAttributes(self) -> int:
        """number of vertex attributes"""

    @NbAttributes.setter
    def NbAttributes(self, arg: int, /) -> None: ...

class Graphic3d_BoundBuffer(nanoocp.NCollection.NCollection_Buffer):
    """Bounds buffer."""

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_BoundBuffer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Init(self, theNbBounds: int, theHasColors: bool) -> bool:
        """Allocates new empty array"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def Colors(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """pointer to facet color values"""

    @Colors.setter
    def Colors(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def NbBounds(self) -> int:
        """number of bounds"""

    @NbBounds.setter
    def NbBounds(self, arg: int, /) -> None: ...

    @property
    def NbMaxBounds(self) -> int:
        """number of allocated bounds"""

    @NbMaxBounds.setter
    def NbMaxBounds(self, arg: int, /) -> None: ...

class Graphic3d_IndexBuffer(Graphic3d_Buffer):
    """Index buffer."""

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_IndexBuffer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def InitInt32(self, theNbElems: int) -> bool:
        """Allocates new empty index array"""

    def Index(self, theIndex: int) -> int:
        """Access index at specified position"""

    def SetIndex(self, theIndex: int, theValue: int) -> None:
        """Change index at specified position"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_ArrayOfPrimitives(nanoocp.Standard.Standard_Transient):
    """
    This class furnish services to defined and fill an array of primitives
    which can be passed directly to graphics rendering API.

    The basic interface consists of the following parts:
    1) Specifying primitive type.
    WARNING! Particular primitive types might be unsupported by specific hardware/graphics API
    (like quads and polygons).
    It is always preferred using one of basic types having maximum compatibility:
    Point, Triangle (or Triangle strip), Segment aka Lines (or Polyline aka Line Strip).
    Primitive strip types can be used to reduce memory usage as alternative to Indexed arrays.
    2) Vertex array.
    - Specifying the (maximum) number of vertexes within array.
    - Specifying the vertex attributes, complementary to mandatory vertex Position (normal,
    color, UV texture coordinates).
    - Defining vertex values by using various versions of AddVertex() or SetVertex*() methods.
    3) Index array (optional).
    - Specifying the (maximum) number of indexes (edges).
    - Defining index values by using AddEdge() method; the index value should be within number of
    defined Vertexes.

    Indexed array allows sharing vertex data across Primitives and thus reducing memory usage,
    since index size is much smaller then size of vertex with all its attributes.
    It is a preferred way for defining primitive array and main alternative to Primitive Strips
    for optimal memory usage, although it is also possible (but unusual) defining Indexed
    Primitive Strip. Note that it is NOT possible sharing Vertex Attributes partially (e.g. share
    Position, but have different Normals); in such cases Vertex should be entirely duplicated
    with all Attributes.
    4) Bounds array (optional).
    - Specifying the (maximum) number of bounds.
    - Defining bounds using AddBound() methods.

    Bounds allow splitting Primitive Array into sub-groups.
    This is useful only in two cases - for specifying per-group color and for restarting
    Primitive Strips. WARNING! Bounds within Primitive Array break rendering batches into parts
    (additional for loops),
    affecting rendering performance negatively (increasing CPU load).
    """

    def __init__(self, theOther: Graphic3d_ArrayOfPrimitives) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    @staticmethod
    def CreateArray(theType: Graphic3d_TypeOfPrimitiveArray, theMaxVertexs: int, theMaxEdges: int, theArrayFlags: int) -> Graphic3d_ArrayOfPrimitives: ...

    @overload
    @staticmethod
    def CreateArray(theType: Graphic3d_TypeOfPrimitiveArray, theMaxVertexs: int, theMaxBounds: int, theMaxEdges: int, theArrayFlags: int) -> Graphic3d_ArrayOfPrimitives:
        """Create an array of specified type."""

    def Attributes(self) -> Graphic3d_Buffer:
        """
        Returns vertex attributes buffer (colors, normals, texture coordinates).
        """

    def Type(self) -> Graphic3d_TypeOfPrimitiveArray:
        """Returns the type of this primitive"""

    def StringType(self) -> str:
        """Returns the string type of this primitive"""

    def HasVertexNormals(self) -> bool:
        """Returns TRUE when vertex normals array is defined."""

    def HasVertexColors(self) -> bool:
        """Returns TRUE when vertex colors array is defined."""

    def HasVertexTexels(self) -> bool:
        """Returns TRUE when vertex texels array is defined."""

    def VertexNumber(self) -> int:
        """Returns the number of defined vertex"""

    def VertexNumberAllocated(self) -> int:
        """Returns the number of allocated vertex"""

    def ItemNumber(self) -> int:
        """Returns the number of total items according to the array type."""

    def IsValid(self) -> bool:
        """Returns TRUE only when the contains of this array is available."""

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt) -> int: ...

    @overload
    def AddVertex(self, theVertex: nanoocp.Quantity.NCollection_Vec3__float) -> int: ...

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float) -> int:
        """
        Adds a vertice in the array.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float) -> int:
        """
        Adds a vertice in the array.
        @return the actual vertex number.
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theColor: nanoocp.Quantity.Quantity_Color) -> int: ...

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theColor32: int) -> int:
        """
        Adds a vertice and vertex color in the vertex array.
        Warning: theColor is ignored when the hasVColors constructor parameter is FALSE
        @code
        theColor32 = Alpha << 24 + Blue << 16 + Green << 8 + Red
        @endcode
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theColor: "NCollection_Vec4<unsigned char>") -> int:
        """
        Adds a vertice and vertex color in the vertex array.
        Warning: theColor is ignored when the hasVColors constructor parameter is FALSE
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theNormal: nanoocp.gp.gp_Dir) -> int:
        """
        Adds a vertice and vertex normal in the vertex array.
        Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theNX: float, theNY: float, theNZ: float) -> int: ...

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theNX: float, theNY: float, theNZ: float) -> int:
        """
        Adds a vertice and vertex normal in the vertex array.
        Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theNormal: nanoocp.gp.gp_Dir, theColor: nanoocp.Quantity.Quantity_Color) -> int:
        """
        Adds a vertice,vertex normal and color in the vertex array.
        Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE
        and      theColor  is ignored when the hasVColors  constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theNormal: nanoocp.gp.gp_Dir, theColor32: int) -> int:
        """
        Adds a vertice,vertex normal and color in the vertex array.
        Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE
        and      theColor  is ignored when the hasVColors  constructor parameter is FALSE.
        @code
        theColor32 = Alpha << 24 + Blue << 16 + Green << 8 + Red
        @endcode
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theTexel: nanoocp.gp.gp_Pnt2d) -> int:
        """
        Adds a vertice and vertex texture in the vertex array.
        theTexel is ignored when the hasVTexels constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theTX: float, theTY: float) -> int: ...

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theTX: float, theTY: float) -> int:
        """
        Adds a vertice and vertex texture coordinates in the vertex array.
        Texel is ignored when the hasVTexels constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theVertex: nanoocp.gp.gp_Pnt, theNormal: nanoocp.gp.gp_Dir, theTexel: nanoocp.gp.gp_Pnt2d) -> int:
        """
        Adds a vertice,vertex normal and texture in the vertex array.
        Warning: theNormal is ignored when the hasVNormals constructor parameter is FALSE
        and      theTexel  is ignored when the hasVTexels  constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theNX: float, theNY: float, theNZ: float, theTX: float, theTY: float) -> int:
        """
        Adds a vertice,vertex normal and texture in the vertex array.
        Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE
        and      Texel  is ignored when the hasVTexels  constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def AddVertex(self, theX: float, theY: float, theZ: float, theNX: float, theNY: float, theNZ: float, theTX: float, theTY: float) -> int:
        """
        Adds a vertice,vertex normal and texture in the vertex array.
        Warning: Normal is ignored when the hasVNormals constructor parameter is FALSE
        and  Texel  is ignored when the hasVTexels  constructor parameter is FALSE.
        @return the actual vertex number
        """

    @overload
    def SetVertice(self, theIndex: int, theVertex: nanoocp.gp.gp_Pnt) -> None:
        """
        Change the vertice of rank theIndex in the array.
        @param[in] theIndex  node index within [1, VertexNumberAllocated()] range
        @param[in] theVertex 3D coordinates
        """

    @overload
    def SetVertice(self, theIndex: int, theX: float, theY: float, theZ: float) -> None:
        """
        Change the vertice in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theX coordinate X
        @param[in] theY coordinate Y
        @param[in] theZ coordinate Z
        """

    @overload
    def SetVertexColor(self, theIndex: int, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Change the vertex color in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theColor node color
        """

    @overload
    def SetVertexColor(self, theIndex: int, theR: float, theG: float, theB: float) -> None:
        """
        Change the vertex color in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theR red   color value within [0, 1] range
        @param[in] theG green color value within [0, 1] range
        @param[in] theB blue  color value within [0, 1] range
        """

    @overload
    def SetVertexColor(self, theIndex: int, theColor: "NCollection_Vec4<unsigned char>") -> None:
        """
        Change the vertex color in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theColor node RGBA color values within [0, 255] range
        """

    @overload
    def SetVertexColor(self, theIndex: int, theColor32: int) -> None:
        """
        Change the vertex color in the array.
        @code
        theColor32 = Alpha << 24 + Blue << 16 + Green << 8 + Red
        @endcode
        @param[in] theIndex   node index within [1, VertexNumberAllocated()] range
        @param[in] theColor32 packed RGBA color values
        """

    @overload
    def SetVertexNormal(self, theIndex: int, theNormal: nanoocp.gp.gp_Dir) -> None:
        """
        Change the vertex normal in the array.
        @param[in] theIndex  node index within [1, VertexNumberAllocated()] range
        @param[in] theNormal normalized surface normal
        """

    @overload
    def SetVertexNormal(self, theIndex: int, theNX: float, theNY: float, theNZ: float) -> None:
        """
        Change the vertex normal in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theNX surface normal X component
        @param[in] theNY surface normal Y component
        @param[in] theNZ surface normal Z component
        """

    @overload
    def SetVertexTexel(self, theIndex: int, theTexel: nanoocp.gp.gp_Pnt2d) -> None:
        """
        Change the vertex texel in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theTexel node UV coordinates
        """

    @overload
    def SetVertexTexel(self, theIndex: int, theTX: float, theTY: float) -> None:
        """
        Change the vertex texel in the array.
        @param[in] theIndex node index within [1, VertexNumberAllocated()] range
        @param[in] theTX node U coordinate
        @param[in] theTY node V coordinate
        """

    def Vertice(self, theRank: int) -> nanoocp.gp.gp_Pnt:
        """
        Returns the vertice from the vertex table if defined.
        @param[in] theRank node index within [1, VertexNumber()] range
        @return node 3D coordinates
        """

    def Vertice__float__float__float(self, theRank: int) -> tuple[float, float, float]:
        """
        Vertice__float__float__float: the C++ overload Vertice(const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the vertice coordinates at rank theRank from the vertex table if defined.
        @param[in]  theRank node index within [1, VertexNumber()] range
        @param[out] theX node X coordinate value
        @param[out] theY node Y coordinate value
        @param[out] theZ node Z coordinate value
        """

    @overload
    def VertexColor(self, theRank: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns the vertex color at rank theRank from the vertex table if defined.
        @param[in] theRank node index within [1, VertexNumber()] range
        @return node color RGB value
        """

    @overload
    def VertexColor(self, theIndex: int, theColor: "NCollection_Vec4<unsigned char>") -> None:
        """
        Returns the vertex color from the vertex table if defined.
        @param[in]  theIndex node index within [1, VertexNumber()] range
        @param[out] theColor node RGBA color values within [0, 255] range
        """

    def VertexColor__float__float__float(self, theRank: int) -> tuple[float, float, float]:
        """
        VertexColor__float__float__float: the C++ overload VertexColor(const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the vertex color values from the vertex table if defined.
        @param[in]  theRank node index within [1, VertexNumber()] range
        @param[out] theR node red   color component value within [0, 1] range
        @param[out] theG node green color component value within [0, 1] range
        @param[out] theB node blue  color component value within [0, 1] range
        """

    def VertexColor__int(self, theRank: int) -> int:
        """
        VertexColor__int: the C++ overload VertexColor(const int, int &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the vertex color values from the vertex table if defined.
        @param[in]  theRank  node index within [1, VertexNumber()] range
        @param[out] theColor node RGBA color packed into 32-bit integer
        """

    def VertexNormal(self, theRank: int) -> nanoocp.gp.gp_Dir:
        """
        Returns the vertex normal from the vertex table if defined.
        @param[in] theRank node index within [1, VertexNumber()] range
        @return normalized 3D vector defining surface normal
        """

    def VertexNormal__float__float__float(self, theRank: int) -> tuple[float, float, float]:
        """
        VertexNormal__float__float__float: the C++ overload VertexNormal(const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the vertex normal coordinates at rank theRank from the vertex table if defined.
        @param[in]  theRank node index within [1, VertexNumber()] range
        @param[out] theNX   normal X coordinate
        @param[out] theNY   normal Y coordinate
        @param[out] theNZ   normal Z coordinate
        """

    def VertexTexel(self, theRank: int) -> nanoocp.gp.gp_Pnt2d:
        """
        Returns the vertex texture at rank theRank from the vertex table if defined.
        @param[in] theRank node index within [1, VertexNumber()] range
        @return UV coordinates
        """

    def VertexTexel__float__float(self, theRank: int) -> tuple[float, float]:
        """
        VertexTexel__float__float: the C++ overload VertexTexel(const int, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the vertex texture coordinates at rank theRank from the vertex table if defined.
        @param[in]  theRank node index within [1, VertexNumber()] range
        @param[out] theTX texel U coordinate value
        @param[out] theTY texel V coordinate value
        """

    def Indices(self) -> Graphic3d_IndexBuffer:
        """
        @name optional array of Indices/Edges for using shared Vertex data
        Returns optional index buffer.
        """

    def EdgeNumber(self) -> int:
        """Returns the number of defined edges"""

    def EdgeNumberAllocated(self) -> int:
        """Returns the number of allocated edges"""

    def Edge(self, theRank: int) -> int:
        """Returns the vertex index at rank theRank in the range [1,EdgeNumber()]"""

    def AddEdge(self, theVertexIndex: int) -> int:
        """
        Adds an edge in the range [1,VertexNumber()] in the array.
        @return the actual edges number
        """

    @overload
    def AddEdges(self, theVertexIndex1: int, theVertexIndex2: int) -> int:
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the
        array.
        @return the actual edges number
        """

    @overload
    def AddEdges(self, theVertexIndex1: int, theVertexIndex2: int, theVertexIndex3: int) -> int:
        """
        Convenience method, adds three vertex indices (a triangle) in the range [1,VertexNumber()] in
        the array.
        @return the actual edges number
        """

    @overload
    def AddEdges(self, theVertexIndex1: int, theVertexIndex2: int, theVertexIndex3: int, theVertexIndex4: int) -> int:
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the
        array.
        @return the actual edges number
        """

    def AddSegmentEdges(self, theVertexIndex1: int, theVertexIndex2: int) -> int:
        """
        Convenience method, adds two vertex indices (a segment) in the range [1,VertexNumber()] in the
        array of segments (Graphic3d_TOPA_SEGMENTS). Raises exception if array is not of type
        Graphic3d_TOPA_SEGMENTS.
        @return the actual edges number
        """

    @overload
    def AddTriangleEdges(self, theVertexIndex1: int, theVertexIndex2: int, theVertexIndex3: int) -> int: ...

    @overload
    def AddTriangleEdges(self, theIndexes: nanoocp.BVH.BVH_Vec3i) -> int:
        """
        Convenience method, adds three vertex indices of triangle in the range [1,VertexNumber()] in
        the array of triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        @return the actual edges number
        """

    @overload
    def AddTriangleEdges(self, theIndexes: nanoocp.BVH.BVH_Vec4i) -> int:
        """
        Convenience method, adds three vertex indices (4th component is ignored) of triangle in the
        range [1,VertexNumber()] in the array of triangles. Raises exception if array is not of type
        Graphic3d_TOPA_TRIANGLES.
        @return the actual edges number
        """

    def AddQuadEdges(self, theVertexIndex1: int, theVertexIndex2: int, theVertexIndex3: int, theVertexIndex4: int) -> int:
        """
        Convenience method, adds four vertex indices (a quad) in the range [1,VertexNumber()] in the
        array of quads. Raises exception if array is not of type Graphic3d_TOPA_QUADRANGLES.
        @return the actual edges number
        """

    @overload
    def AddQuadTriangleEdges(self, theVertexIndex1: int, theVertexIndex2: int, theVertexIndex3: int, theVertexIndex4: int) -> int: ...

    @overload
    def AddQuadTriangleEdges(self, theIndexes: nanoocp.BVH.BVH_Vec4i) -> int:
        """
        Convenience method, adds quad indices in the range [1,VertexNumber()] into array or triangles
        as two triangles. Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        @return the actual edges number
        """

    def AddTriangleStripEdges(self, theVertexLower: int, theVertexUpper: int) -> None:
        """
        Add triangle strip into indexed triangulation array.
        N-2 triangles are added from N input nodes.
        Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        @param[in] theVertexLower  index of first node defining triangle strip
        @param[in] theVertexUpper  index of last  node defining triangle strip
        """

    def AddTriangleFanEdges(self, theVertexLower: int, theVertexUpper: int, theToClose: bool) -> None:
        """
        Add triangle fan into indexed triangulation array.
        N-2 triangles are added from N input nodes (or N-1 with closed flag).
        Raises exception if array is not of type Graphic3d_TOPA_TRIANGLES.
        @param[in] theVertexLower  index of first node defining triangle fun (center)
        @param[in] theVertexUpper  index of last  node defining triangle fun
        @param[in] theToClose  close triangle fan (connect first and last points)
        """

    def AddPolylineEdges(self, theVertexLower: int, theVertexUpper: int, theToClose: bool) -> None:
        """
        Add line strip (polyline) into indexed segments array.
        N-1 segments are added from N input nodes (or N with closed flag).
        Raises exception if array is not of type Graphic3d_TOPA_SEGMENTS.
        @param[in] theVertexLower  index of first node defining line strip fun (center)
        @param[in] theVertexUpper  index of last  node defining triangle fun
        @param[in] theToClose  close triangle fan (connect first and last points)
        """

    def Bounds(self) -> Graphic3d_BoundBuffer:
        """
        @name optional array of Bounds/Subgroups within primitive array (e.g. restarting
        primitives / assigning colors)
        Returns optional bounds buffer.
        """

    def HasBoundColors(self) -> bool:
        """Returns TRUE when bound colors array is defined."""

    def BoundNumber(self) -> int:
        """Returns the number of defined bounds"""

    def BoundNumberAllocated(self) -> int:
        """Returns the number of allocated bounds"""

    def Bound(self, theRank: int) -> int:
        """Returns the edge number at rank theRank."""

    def BoundColor(self, theRank: int) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns the bound color at rank theRank from the bound table if defined.
        """

    def BoundColor__float__float__float(self, theRank: int) -> tuple[float, float, float]:
        """
        BoundColor__float__float__float: the C++ overload BoundColor(const int, double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the bound color values at rank theRank from the bound table if defined.
        """

    @overload
    def AddBound(self, theEdgeNumber: int) -> int:
        """
        Adds a bound of length theEdgeNumber in the bound array
        @return the actual bounds number
        """

    @overload
    def AddBound(self, theEdgeNumber: int, theBColor: nanoocp.Quantity.Quantity_Color) -> int:
        """
        Adds a bound of length theEdgeNumber and bound color theBColor in the bound array.
        Warning: theBColor is ignored when the hasBColors constructor parameter is FALSE
        @return the actual bounds number
        """

    @overload
    def AddBound(self, theEdgeNumber: int, theR: float, theG: float, theB: float) -> int:
        """
        Adds a bound of length theEdgeNumber and bound color coordinates in the bound array.
        Warning: <theR,theG,theB> are ignored when the hasBColors constructor parameter is FALSE
        @return the actual bounds number
        """

    @overload
    def SetBoundColor(self, theIndex: int, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetBoundColor(self, theIndex: int, theR: float, theG: float, theB: float) -> None:
        """Change the bound color of rank theIndex in the array."""

class Graphic3d_ArrayOfPoints(Graphic3d_ArrayOfPrimitives):
    """Contains points array definition."""

    @overload
    def __init__(self, theMaxVertexs: int, theHasVColors: bool = False, theHasVNormals: bool = False) -> None:
        """
        Creates an array of points (Graphic3d_TOPA_POINTS).
        The array must be filled using the AddVertex(Point) method.
        @param theMaxVertexs  maximum number of points
        @param theHasVColors  when TRUE, AddVertex(Point,Color)  should be used for specifying vertex
        color
        @param theHasVNormals when TRUE, AddVertex(Point,Normal) should be used for specifying vertex
        normal
        """

    @overload
    def __init__(self, theMaxVertexs: int, theArrayFlags: int) -> None:
        """
        Creates an array of points (Graphic3d_TOPA_POINTS).
        The array must be filled using the AddVertex(Point) method.
        @param theMaxVertexs maximum number of points
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfPoints) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfPolygons(Graphic3d_ArrayOfPrimitives):
    """
    Contains polygons array definition.
    WARNING! Polygon primitives might be unsupported by graphics library.
    Triangulation should be used instead of quads for better compatibility.
    """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxBounds: int = 0, theMaxEdges: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasBColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of polygons (Graphic3d_TOPA_POLYGONS):
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxBounds  defines the maximum allowed bound  number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxBounds: int, theMaxEdges: int, theArrayFlags: int) -> None:
        """
        Creates an array of polygons (Graphic3d_TOPA_POLYGONS), a polygon can be filled as:
        1) Creating a single polygon defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolygons (7);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        2) Creating separate polygons defined with a predefined number of bounds and the number of
        vertex per bound, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolygons (7, 2);
        myArray->AddBound (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddBound (3);
        myArray->AddVertex (x5, y5, z5);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        3) Creating a single indexed polygon defined with his vertex ans edges, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolygons (4, 0, 6);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (4);
        @endcode
        4) Creating separate polygons defined with a predefined number of bounds and the number of
        edges per bound, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolygons (6, 4, 14);
        myArray->AddBound (3);
        myArray->AddVertex (x1, y1, z1);
        myArray->AddVertex (x2, y2, z2);
        myArray->AddVertex (x3, y3, z3);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddBound (3);
        myArray->AddVertex (x4, y4, z4);
        myArray->AddVertex (x5, y5, z5);
        myArray->AddVertex (x6, y6, z6);
        myArray->AddEdge (4);
        myArray->AddEdge (5);
        myArray->AddEdge (6);
        myArray->AddBound (4);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddEdge (5);
        myArray->AddEdge (6);
        myArray->AddBound (4);
        myArray->AddEdge (1);
        myArray->AddEdge (3);
        myArray->AddEdge (5);
        myArray->AddEdge (4);
        @endcode
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxBounds  defines the maximum allowed bound  number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfPolygons) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfPolylines(Graphic3d_ArrayOfPrimitives):
    """Contains polylines array definition."""

    @overload
    def __init__(self, theMaxVertexs: int, theMaxBounds: int = 0, theMaxEdges: int = 0, theHasVColors: bool = False, theHasBColors: bool = False) -> None:
        """
        Creates an array of polylines (Graphic3d_TOPA_POLYLINES).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxBounds  defines the maximum allowed bound  number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        @param theHasVColors when TRUE AddVertex(Point,Color) or AddVertex(Point,Normal,Color) should
        be used to specify per-vertex color values
        @param theHasBColors when TRUE AddBound(number,Color) should be used to specify sub-group
        color
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxBounds: int, theMaxEdges: int, theArrayFlags: int) -> None:
        """
        Creates an array of polylines (Graphic3d_TOPA_POLYLINES), a polyline can be filled as:
        1) Creating a single polyline defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolylines (7);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        2) Creating separate polylines defined with a predefined number of bounds and the number of
        vertex per bound, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolylines (7, 2);
        myArray->AddBound (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddBound (3);
        myArray->AddVertex (x5, y5, z5);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        3) Creating a single indexed polyline defined with his vertex and edges, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolylines (4, 0, 6);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (4);
        @endcode
        4) creating separate polylines defined with a predefined number of bounds and the number of
        edges per bound, i.e:
        @code
        myArray = Graphic3d_ArrayOfPolylines (6, 4, 14);
        myArray->AddBound (3);
        myArray->AddVertex (x1, y1, z1);
        myArray->AddVertex (x2, y2, z2);
        myArray->AddVertex (x3, y3, z3);
        myArray->AddEdge (1);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddBound (3);
        myArray->AddVertex (x4, y4, z4);
        myArray->AddVertex (x5, y5, z5);
        myArray->AddVertex (x6, y6, z6);
        myArray->AddEdge (4);
        myArray->AddEdge (5);
        myArray->AddEdge (6);
        myArray->AddBound (4);
        myArray->AddEdge (2);
        myArray->AddEdge (3);
        myArray->AddEdge (5);
        myArray->AddEdge (6);
        myArray->AddBound (4);
        myArray->AddEdge (1);
        myArray->AddEdge (3);
        myArray->AddEdge (5);
        myArray->AddEdge (4);
        @endcode
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxBounds  defines the maximum allowed bound  number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfPolylines) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfQuadrangles(Graphic3d_ArrayOfPrimitives):
    """
    Contains quadrangles array definition.
    WARNING! Quadrangle primitives might be unsupported by graphics library.
    Triangulation should be used instead of quads for better compatibility.
    """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of quadrangles (Graphic3d_TOPA_QUADRANGLES).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array (for indexed
        array)
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int, theArrayFlags: int) -> None:
        """
        Creates an array of quadrangles (Graphic3d_TOPA_QUADRANGLES), a quadrangle can be filled as:
        1) Creating a set of quadrangles defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfQuadrangles (8);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x8, y8, z8);
        @endcode
        2) Creating a set of indexed quadrangles defined with his vertex ans edges, i.e:
        @code
        myArray = Graphic3d_ArrayOfQuadrangles (6, 8);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x6, y6, z6);
        myArray->AddEdges (1, 2, 3, 4);
        myArray->AddEdges (3, 4, 5, 6);
        @endcode
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array (for indexed
        array)
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfQuadrangles) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfQuadrangleStrips(Graphic3d_ArrayOfPrimitives):
    """
    Contains quadrangles strip array definition.
    WARNING! Quadrangle primitives might be unsupported by graphics library.
    Triangulation should be used instead of quads for better compatibility.
    """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxStrips: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasSColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of quadrangle strips (Graphic3d_TOPA_QUADRANGLESTRIPS).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxStrips  defines the maximum allowed strip  number in the array
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxStrips: int, theArrayFlags: int) -> None:
        """
        Creates an array of quadrangle strips (Graphic3d_TOPA_QUADRANGLESTRIPS), a polygon can be
        filled as: 1) Creating a single strip defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfQuadrangleStrips (7);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        2) Creating separate strips defined with a predefined number of strips and the number of
        vertex per strip, i.e:
        @code
        myArray = Graphic3d_ArrayOfQuadrangleStrips (8, 2);
        myArray->AddBound (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddBound (4);
        myArray->AddVertex (x5, y5, z5);
        ....
        myArray->AddVertex (x8, y8, z8);
        @endcode
        The number of quadrangle really drawn is: VertexNumber()/2 - std::min(1, BoundNumber()).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxStrips  defines the maximum allowed strip  number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfQuadrangleStrips) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfSegments(Graphic3d_ArrayOfPrimitives):
    """Contains segments array definition."""

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int = 0, theHasVColors: bool = False) -> None:
        """
        Creates an array of segments (Graphic3d_TOPA_SEGMENTS).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        @param theHasVColors when TRUE, AddVertex(Point,Color) should be used for specifying vertex
        color
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int, theArrayFlags: int) -> None:
        """
        Creates an array of segments (Graphic3d_TOPA_SEGMENTS), a segment can be filled as:
        1) Creating a set of segments defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfSegments (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        @endcode
        2) Creating a set of indexed segments defined with his vertex and edges, i.e:
        @code
        myArray = Graphic3d_ArrayOfSegments (4, 8);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddEdges (1, 2);
        myArray->AddEdges (3, 4);
        myArray->AddEdges (2, 4);
        myArray->AddEdges (1, 3);
        @endcode
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxEdges   defines the maximum allowed edge   number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfSegments) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfTriangleFans(Graphic3d_ArrayOfPrimitives):
    """Contains triangles fan array definition"""

    @overload
    def __init__(self, theMaxVertexs: int, theMaxFans: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasBColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of triangle fans (Graphic3d_TOPA_TRIANGLEFANS).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxFans    defines the maximum allowed fan    number in the array
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxFans: int, theArrayFlags: int) -> None:
        """
        Creates an array of triangle fans (Graphic3d_TOPA_TRIANGLEFANS), a polygon can be filled as:
        1) Creating a single fan defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangleFans (7);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        2) creating separate fans defined with a predefined number of fans and the number of vertex
        per fan, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangleFans (8, 2);
        myArray->AddBound (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddBound (4);
        myArray->AddVertex (x5, y5, z5);
        ....
        myArray->AddVertex (x8, y8, z8);
        @endcode
        The number of triangle really drawn is: VertexNumber() - 2 * std::min(1, BoundNumber())
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxFans    defines the maximum allowed fan    number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfTriangleFans) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfTriangles(Graphic3d_ArrayOfPrimitives):
    """Contains triangles array definition"""

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of triangles (Graphic3d_TOPA_TRIANGLES).
        @param theMaxVertexs  defines the maximum allowed vertex number in the array
        @param theMaxEdges    defines the maximum allowed edge   number in the array
        @param theHasVNormals when TRUE,  AddVertex(Point,Normal), AddVertex(Point,Normal,Color) or
        AddVertex(Point,Normal,Texel) should be used to specify vertex normal;
        vertex normals should be specified coherent to triangle orientation
        (defined by order of vertexes within triangle) for proper rendering
        @param theHasVColors  when TRUE,  AddVertex(Point,Color) or AddVertex(Point,Normal,Color)
        should be used to specify vertex color
        @param theHasVTexels  when TRUE,  AddVertex(Point,Texel) or AddVertex(Point,Normal,Texel)
        should be used to specify vertex UV coordinates
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxEdges: int, theArrayFlags: int) -> None:
        """
        Creates an array of triangles (Graphic3d_TOPA_TRIANGLES), a triangle can be filled as:
        1) Creating a set of triangles defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangles (6);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x6, y6, z6);
        @endcode
        3) Creating a set of indexed triangles defined with his vertex and edges, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangles (4, 6);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddEdges (1, 2, 3);
        myArray->AddEdges (2, 3, 4);
        @endcode
        @param theMaxVertexs  defines the maximum allowed vertex number in the array
        @param theMaxEdges    defines the maximum allowed edge   number in the array
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfTriangles) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ArrayOfTriangleStrips(Graphic3d_ArrayOfPrimitives):
    """Contains triangles strip array definition."""

    @overload
    def __init__(self, theMaxVertexs: int, theMaxStrips: int = 0, theHasVNormals: bool = False, theHasVColors: bool = False, theHasBColors: bool = False, theHasVTexels: bool = False) -> None:
        """
        Creates an array of triangle strips (Graphic3d_TOPA_TRIANGLESTRIPS).
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxStrips  defines the maximum allowed strip  number in the array;
        the number of triangle really drawn is: VertexNumber() - 2 * std::min(1,
        BoundNumber())
        @param theHasVNormals when TRUE, AddVertex(Point,Normal), AddVertex(Point,Normal,Color) or
        AddVertex(Point,Normal,Texel) should be used to specify vertex normal;
        vertex normals should be specified coherent to triangle orientation
        (defined by order of vertexes within triangle) for proper rendering
        @param theHasVColors  when TRUE, AddVertex(Point,Color) or AddVertex(Point,Normal,Color)
        should be used to specify vertex color
        @param theHasBColors  when TRUE, AddBound(number,Color) should be used to specify sub-group
        color
        @param theHasVTexels  when TRUE, AddVertex(Point,Texel) or AddVertex(Point,Normal,Texel)
        should be used to specify vertex UV coordinates
        """

    @overload
    def __init__(self, theMaxVertexs: int, theMaxStrips: int, theArrayFlags: int) -> None:
        """
        Creates an array of triangle strips (Graphic3d_TOPA_TRIANGLESTRIPS), a polygon can be filled
        as: 1) Creating a single strip defined with his vertexes, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangleStrips (7);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x7, y7, z7);
        @endcode
        2) Creating separate strips defined with a predefined number of strips and the number of
        vertex per strip, i.e:
        @code
        myArray = Graphic3d_ArrayOfTriangleStrips (8, 2);
        myArray->AddBound (4);
        myArray->AddVertex (x1, y1, z1);
        ....
        myArray->AddVertex (x4, y4, z4);
        myArray->AddBound (4);
        myArray->AddVertex (x5, y5, z5);
        ....
        myArray->AddVertex (x8, y8, z8);
        @endcode
        @param theMaxVertexs defines the maximum allowed vertex number in the array
        @param theMaxStrips  defines the maximum allowed strip  number in the array;
        the number of triangle really drawn is: VertexNumber() - 2 * std::min(1,
        BoundNumber())
        @param theArrayFlags array flags
        """

    @overload
    def __init__(self, theOther: Graphic3d_ArrayOfTriangleStrips) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_MarkerImage(nanoocp.Standard.Standard_Transient):
    """
    This class is used to store bitmaps and images for markers rendering.
    It can convert bitmap texture stored in NCollection_HArray1<uint8_t> to Image_PixMap and vice
    versa.
    """

    @overload
    def __init__(self, theImage: nanoocp.Image.Image_PixMap | None, theImageAlpha: nanoocp.Image.Image_PixMap | None = None) -> None:
        """
        Constructor from existing pixmap.
        @param[in] theImage  source image
        @param[in] theImageAlpha  colorless image
        """

    @overload
    def __init__(self, theBitMap: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None, theWidth: int, theHeight: int) -> None:
        """
        Creates marker image from array of bytes
        (method for compatibility with old markers definition).
        @param[in] theBitMap  source bitmap stored as array of bytes
        @param[in] theWidth   number of bits in a row
        @param[in] theHeight  number of bits in a column
        """

    @overload
    def __init__(self, theOther: Graphic3d_MarkerImage) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def StandardMarker(theMarkerType: nanoocp.Aspect.Aspect_TypeOfMarker, theScale: float, theColor: nanoocp.Quantity.NCollection_Vec4__float) -> Graphic3d_MarkerImage:
        """
        Returns a marker image for the marker of the specified type, scale and color.
        """

    def GetImage(self) -> nanoocp.Image.Image_PixMap:
        """
        Return marker image.
        If an instance of the class has been initialized with a bitmap, it will be converted to image.
        """

    def GetImageAlpha(self) -> nanoocp.Image.Image_PixMap:
        """
        Return image alpha as grayscale image.
        Note that if an instance of the class has been initialized with a bitmap
        or with grayscale image this method will return exactly the same image as GetImage()
        """

    def GetImageId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return an unique ID.
        This ID will be used to manage resource in graphic driver.
        """

    def GetImageAlphaId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return an unique ID.
        This ID will be used to manage resource in graphic driver.
        """

    def GetTextureSize(self) -> tuple[int, int]:
        """Return texture size"""

    def IsColoredImage(self) -> bool:
        """Return TRUE if marker image has colors (e.g. RGBA and not grayscale)."""

    def GetBitMapArray(self, theAlphaValue: float = 0.5, theIsTopDown: bool = False) -> nanoocp.NCollection.NCollection_HArray1__unsigned_char:
        """
        Return marker image as array of bytes.
        If an instance of the class has been initialized with image, it will be converted to bitmap
        based on the parameter theAlphaValue.
        @param theAlphaValue pixels in the image that have alpha value greater than
        or equal to this parameter will be stored in bitmap as "1",
        others will be stored as "0"
        @param[in] theIsTopDown  flag indicating expected rows order in returned bitmap, which is
        bottom-up by default
        """

class Graphic3d_Fresnel:
    """Describes Fresnel reflectance parameters."""

    @overload
    def __init__(self) -> None:
        """Creates uninitialized Fresnel factor."""

    @overload
    def __init__(self, theOther: Graphic3d_Fresnel) -> None: ...

    @staticmethod
    def CreateSchlick(theSpecularColor: nanoocp.Quantity.NCollection_Vec3__float) -> Graphic3d_Fresnel:
        """Creates Schlick's approximation of Fresnel factor."""

    @staticmethod
    def CreateConstant(theReflection: float) -> Graphic3d_Fresnel:
        """Creates Fresnel factor for constant reflection."""

    @staticmethod
    def CreateDielectric(theRefractionIndex: float) -> Graphic3d_Fresnel:
        """Creates Fresnel factor for physical-based dielectric model."""

    @overload
    @staticmethod
    def CreateConductor(theRefractionIndex: float, theAbsorptionIndex: float) -> Graphic3d_Fresnel:
        """Creates Fresnel factor for physical-based conductor model."""

    @overload
    @staticmethod
    def CreateConductor(theRefractionIndex: nanoocp.Quantity.NCollection_Vec3__float, theAbsorptionIndex: nanoocp.Quantity.NCollection_Vec3__float) -> Graphic3d_Fresnel:
        """
        Creates Fresnel factor for physical-based conductor model (spectral version).
        """

    def Serialize(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns serialized representation of Fresnel factor."""

    def __eq__(self, theOther: Graphic3d_Fresnel) -> bool:
        """Performs comparison of two objects describing Fresnel factor."""

    def FresnelType(self) -> Graphic3d_FresnelModel:
        """Returns type of Fresnel."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_BSDF:
    """
    Describes material's BSDF (Bidirectional Scattering Distribution Function) used
    for physically-based rendering (in path tracing engine). BSDF is represented as
    weighted mixture of basic BRDFs/BTDFs (Bidirectional Reflectance (Transmittance)
    Distribution Functions).

    NOTE: OCCT uses two-layer material model. We have base diffuse, glossy, or transmissive
    layer, covered by one glossy/specular coat. In the current model, the layers themselves
    have no thickness; they can simply reflect light or transmits it to the layer under it.
    We use actual BRDF model only for direct reflection by the coat layer. For transmission
    through this layer, we approximate it as a flat specular surface.
    """

    @overload
    def __init__(self) -> None:
        """Creates uninitialized BSDF."""

    @overload
    def __init__(self, theOther: Graphic3d_BSDF) -> None: ...

    @staticmethod
    def CreateDiffuse(theWeight: nanoocp.Quantity.NCollection_Vec3__float) -> Graphic3d_BSDF:
        """Creates BSDF describing diffuse (Lambertian) surface."""

    @staticmethod
    def CreateMetallic(theWeight: nanoocp.Quantity.NCollection_Vec3__float, theFresnel: Graphic3d_Fresnel, theRoughness: float) -> Graphic3d_BSDF:
        """Creates BSDF describing polished metallic-like surface."""

    @staticmethod
    def CreateTransparent(theWeight: nanoocp.Quantity.NCollection_Vec3__float, theAbsorptionColor: nanoocp.Quantity.NCollection_Vec3__float, theAbsorptionCoeff: float) -> Graphic3d_BSDF:
        """
        Creates BSDF describing transparent object.
        Transparent BSDF models simple transparency without
        refraction (the ray passes straight through the surface).
        """

    @staticmethod
    def CreateGlass(theWeight: nanoocp.Quantity.NCollection_Vec3__float, theAbsorptionColor: nanoocp.Quantity.NCollection_Vec3__float, theAbsorptionCoeff: float, theRefractionIndex: float) -> Graphic3d_BSDF:
        """
        Creates BSDF describing glass-like object.
        Glass-like BSDF mixes refraction and reflection effects at
        grazing angles using physically-based Fresnel dielectric model.
        """

    @staticmethod
    def CreateMetallicRoughness(thePbr: Graphic3d_PBRMaterial) -> Graphic3d_BSDF:
        """Creates BSDF from PBR metallic-roughness material."""

    def Normalize(self) -> None:
        """Normalizes BSDF components."""

    def __eq__(self, theOther: Graphic3d_BSDF) -> bool:
        """Performs comparison of two BSDFs."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def Kc(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Weight of coat specular/glossy BRDF."""

    @Kc.setter
    def Kc(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Kd(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Weight of base diffuse BRDF."""

    @Kd.setter
    def Kd(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def Ks(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Weight of base specular/glossy BRDF."""

    @Ks.setter
    def Ks(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def Kt(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Weight of base specular/glossy BTDF."""

    @Kt.setter
    def Kt(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def Le(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Radiance emitted by the surface."""

    @Le.setter
    def Le(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

    @property
    def Absorption(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Volume scattering color/density."""

    @Absorption.setter
    def Absorption(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

    @property
    def FresnelCoat(self) -> Graphic3d_Fresnel:
        """Parameters of Fresnel reflectance of coat layer."""

    @FresnelCoat.setter
    def FresnelCoat(self, arg: Graphic3d_Fresnel, /) -> None: ...

    @property
    def FresnelBase(self) -> Graphic3d_Fresnel:
        """Parameters of Fresnel reflectance of base layer."""

    @FresnelBase.setter
    def FresnelBase(self, arg: Graphic3d_Fresnel, /) -> None: ...

class Graphic3d_PBRMaterial:
    """
    Class implementing Metallic-Roughness physically based material definition
    """

    @overload
    def __init__(self) -> None:
        """
        Creates new physically based material in Metallic-Roughness system.
        'metallic' parameter is 0 by default.
        'roughness' parameter is 1 by default.
        'color' parameter is (0, 0, 0) by default.
        'alpha' parameter is 1 by default.
        'IOR' parameter is 1.5 by default.
        'emission' parameter is (0, 0, 0) by default.
        """

    @overload
    def __init__(self, theBSDF: Graphic3d_BSDF) -> None:
        """
        Creates new physically based material in Metallic-Roughness system from Graphic3d_BSDF.
        """

    @overload
    def __init__(self, theOther: Graphic3d_PBRMaterial) -> None: ...

    def Metallic(self) -> float:
        """
        Returns material's metallic coefficient in [0, 1] range.
        1 for metals and 0 for dielectrics.
        It is preferable to be exactly 0 or 1. Average values are needed for textures mixing in
        shader.
        """

    def SetMetallic(self, theMetallic: float) -> None:
        """Modifies metallic coefficient of material in [0, 1] range."""

    @staticmethod
    def Roughness_s(theNormalizedRoughness: float) -> float:
        """Maps roughness from [0, 1] to [MinRoughness, 1] for calculations."""

    def Roughness(self) -> float:
        """
        Returns real value of roughness in [MinRoughness, 1] range for calculations.
        """

    def NormalizedRoughness(self) -> float:
        """
        Returns roughness mapping parameter in [0, 1] range.
        Roughness is defined in [0, 1] for handful material settings
        and is mapped to [MinRoughness, 1] for calculations.
        """

    def SetRoughness(self, theRoughness: float) -> None:
        """Modifies roughness coefficient of material in [0, 1] range."""

    def IOR(self) -> float:
        """Returns index of refraction in [1, 3] range."""

    def SetIOR(self, theIOR: float) -> None:
        """
        Modifies index of refraction in [1, 3] range.
        In practice affects only on non-metal materials reflection possibilities.
        """

    def Color(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Returns albedo color with alpha component of material."""

    @overload
    def SetColor(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies albedo color with alpha component."""

    @overload
    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies only albedo color."""

    def Alpha(self) -> float:
        """Returns alpha component in range [0, 1]."""

    def SetAlpha(self, theAlpha: float) -> None:
        """Modifies alpha component."""

    def Emission(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """
        Returns light intensity emitted by material.
        Values are greater or equal 0.
        """

    def SetEmission(self, theEmission: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Modifies light intensity emitted by material."""

    def SetBSDF(self, theBSDF: Graphic3d_BSDF) -> None:
        """Generates material in Metallic-Roughness system from Graphic3d_BSDF."""

    def __eq__(self, theOther: Graphic3d_PBRMaterial) -> bool:
        """PBR materials comparison operator."""

    @staticmethod
    def GenerateEnvLUT(theLUT: nanoocp.Image.Image_PixMap | None, theNbIntegralSamples: int = 1024) -> None:
        """
        Generates 2D look up table of scale and bias for fresnell zero coefficient.
        It is needed for calculation reflectance part of environment lighting.
        @param[out]  theLUT table storage (must be Image_Format_RGF).
        @param[in]  theNbIntegralSamples number of importance samples in hemisphere integral
        calculation for every table item.
        """

    @staticmethod
    def RoughnessFromSpecular(theSpecular: nanoocp.Quantity.Quantity_Color, theShiness: float) -> float:
        """
        Compute material roughness from common material (specular color + shininess).
        @param[in] theSpecular  specular color
        @param[in] theShiness   normalized shininess coefficient within [0..1] range
        @return roughness within [0..1] range
        """

    @staticmethod
    def MetallicFromSpecular(theSpecular: nanoocp.Quantity.Quantity_Color) -> float:
        """
        Compute material metallicity from common material (specular color).
        @param[in] theSpecular  specular color
        @return metallicity within [0..1] range
        """

    @staticmethod
    def MinRoughness() -> float:
        """
        Roughness cannot be 0 in real calculations, so it returns minimal achievable level of
        roughness in practice
        """

    @staticmethod
    def SpecIBLMapSamplesFactor(theProbability: float, theRoughness: float) -> float:
        """
        Shows how much times less samples can be used in certain roughness value specular IBL map
        generation in compare with samples number for map with roughness of 1. Specular IBL maps with
        less roughness values have higher resolution but require less samples for the same quality of
        baking. So that reducing samples number is good strategy to improve performance of baking. The
        samples number for specular IBL map with roughness of 1 (the maximum possible samples number)
        is expected to be defined as baking parameter. Samples number for other roughness values can
        be calculated by multiplication origin samples number by this factor.
        @param theProbability value from 0 to 1 controlling strength of samples reducing.
        Bigger values result in slower reduction to provide better quality but worse performance.
        Value of 1 doesn't affect at all so that 1 will be returned (it can be used to disable
        reduction strategy).
        @param theRoughness roughness value of current generated specular IBL map (from 0 to 1).
        @return factor to calculate number of samples for current specular IBL map baking.
        Be aware! It has no obligation to return 1 in case of roughness of 1.
        Be aware! It produces poor quality with small number of origin samples. In that case it is
        recommended to be disabled.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_MaterialAspect:
    """
    This class allows the definition of the type of a surface.
    Aspect attributes of a 3d face.
    Keywords: Material, FillArea, Shininess, Ambient, Color, Diffuse,
    Specular, Transparency, Emissive, ReflectionMode,
    BackFace, FrontFace, Reflection, Absorption
    """

    @overload
    def __init__(self) -> None:
        """Creates a material from default values."""

    @overload
    def __init__(self, theName: Graphic3d_NameOfMaterial) -> None:
        """Creates a generic material."""

    @overload
    def __init__(self, theOther: Graphic3d_MaterialAspect) -> None: ...

    @staticmethod
    def NumberOfMaterials() -> int:
        """Returns the number of predefined textures."""

    @staticmethod
    def MaterialName_s(theRank: int) -> str:
        """
        Returns the name of the predefined material of specified rank within range [1,
        NumberOfMaterials()].
        """

    @staticmethod
    def MaterialType_s(theRank: int) -> Graphic3d_TypeOfMaterial:
        """
        Returns the type of the predefined material of specified rank within range [1,
        NumberOfMaterials()].
        """

    @staticmethod
    def MaterialFromName__Graphic3d_NameOfMaterial(theName: str) -> tuple[bool, Graphic3d_NameOfMaterial]:
        """
        MaterialFromName__Graphic3d_NameOfMaterial: the C++ overload MaterialFromName(const char *const, Graphic3d_NameOfMaterial &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Finds the material for specified name.
        @param[in] theName   name to find
        @param[out] theMat   found material
        @return FALSE if name was unrecognized
        """

    @staticmethod
    def MaterialFromName(theName: str) -> Graphic3d_NameOfMaterial:
        """
        Returns the material for specified name or Graphic3d_NameOfMaterial_DEFAULT if name is
        unknown.
        """

    def Name(self) -> Graphic3d_NameOfMaterial:
        """Returns the material name (within predefined enumeration)."""

    def RequestedName(self) -> Graphic3d_NameOfMaterial:
        """
        Returns the material name within predefined enumeration which has been requested (before
        modifications).
        """

    def StringName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the given name of this material. This might be:
        - given name set by method ::SetMaterialName()
        - standard name for a material within enumeration
        - "UserDefined" for non-standard material without name specified externally.
        """

    def MaterialName(self) -> str:
        """Returns the given name of this material. This might be:"""

    def SetMaterialName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        The current material become a "UserDefined" material.
        Set the name of the "UserDefined" material.
        """

    def Reset(self) -> None:
        """
        Resets the material with the original values according to
        the material name but leave the current color values untouched
        for the material of type ASPECT.
        """

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """
        Returns the diffuse color of the surface.
        WARNING! This method does NOT return color for Graphic3d_MATERIAL_ASPECT material (color is
        defined by Graphic3d_Aspects::InteriorColor()).
        """

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Modifies the ambient and diffuse color of the surface.
        WARNING! Has no effect for Graphic3d_MATERIAL_ASPECT material (color should be set to
        Graphic3d_Aspects::SetInteriorColor()).
        """

    def Transparency(self) -> float:
        """
        Returns the transparency coefficient of the surface (1.0 - Alpha); 0.0 means opaque.
        """

    def Alpha(self) -> float:
        """
        Returns the alpha coefficient of the surface (1.0 - Transparency); 1.0 means opaque.
        """

    def SetTransparency(self, theValue: float) -> None:
        """
        Modifies the transparency coefficient of the surface, where 0 is opaque and 1 is fully
        transparent. Transparency is applicable to materials that have at least one of reflection
        modes (ambient, diffuse, specular or emissive) enabled. See also SetReflectionModeOn() and
        SetReflectionModeOff() methods.

        Warning: Raises MaterialDefinitionError if given value is a negative value or greater
        than 1.0.
        """

    def SetAlpha(self, theValue: float) -> None:
        """
        Modifies the alpha coefficient of the surface, where 1.0 is opaque and 0.0 is fully
        transparent.
        """

    def AmbientColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the ambient color of the surface."""

    def SetAmbientColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the ambient color of the surface."""

    def DiffuseColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the diffuse color of the surface."""

    def SetDiffuseColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the diffuse color of the surface."""

    def SpecularColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the specular color of the surface."""

    def SetSpecularColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the specular color of the surface."""

    def EmissiveColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the emissive color of the surface."""

    def SetEmissiveColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the emissive color of the surface."""

    def Shininess(self) -> float:
        """Returns the luminosity of the surface."""

    def SetShininess(self, theValue: float) -> None:
        """
        Modifies the luminosity of the surface.
        Warning: Raises MaterialDefinitionError if given value is a negative value or greater
        than 1.0.
        """

    def IncreaseShine(self, theDelta: float) -> None:
        """
        Increases or decreases the luminosity.
        @param theDelta a signed percentage
        """

    def RefractionIndex(self) -> float:
        """Returns the refraction index of the material"""

    def SetRefractionIndex(self, theValue: float) -> None:
        """
        Modifies the refraction index of the material.
        Warning: Raises MaterialDefinitionError if given value is a lesser than 1.0.
        """

    def BSDF(self) -> Graphic3d_BSDF:
        """Returns BSDF (bidirectional scattering distribution function)."""

    def SetBSDF(self, theBSDF: Graphic3d_BSDF) -> None:
        """Modifies the BSDF (bidirectional scattering distribution function)."""

    def PBRMaterial(self) -> Graphic3d_PBRMaterial:
        """Returns physically based representation of material"""

    def SetPBRMaterial(self, thePBRMaterial: Graphic3d_PBRMaterial) -> None:
        """Modifies the physically based representation of material"""

    def ReflectionMode(self, theType: Graphic3d_TypeOfReflection) -> bool:
        """Returns TRUE if the reflection mode is active, FALSE otherwise."""

    @overload
    def MaterialType(self) -> Graphic3d_TypeOfMaterial:
        """Returns material type."""

    @overload
    def MaterialType(self, theType: Graphic3d_TypeOfMaterial) -> bool:
        """Returns TRUE if type of this material is equal to specified type."""

    def SetMaterialType(self, theType: Graphic3d_TypeOfMaterial) -> None:
        """Set material type."""

    def IsDifferent(self, theOther: Graphic3d_MaterialAspect) -> bool:
        """Returns TRUE if this material differs from specified one."""

    def __ne__(self, theOther: Graphic3d_MaterialAspect) -> bool:
        """Returns TRUE if this material differs from specified one."""

    def IsEqual(self, theOther: Graphic3d_MaterialAspect) -> bool:
        """Returns TRUE if this material is identical to specified one."""

    def __eq__(self, theOther: Graphic3d_MaterialAspect) -> bool:
        """Returns TRUE if this material is identical to specified one."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def SetReflectionModeOff(self, theType: Graphic3d_TypeOfReflection) -> None:
        """
        Deprecated in OCCT: Deprecated method, specific material component should be zerroed instead

        Deactivates the reflective properties of the surface with specified reflection type.
        """

class Graphic3d_HatchStyle(nanoocp.Standard.Standard_Transient):
    """
    A class that provides an API to use standard OCCT hatch styles
    defined in Aspect_HatchStyle enum or to create custom styles
    from a user-defined bitmap
    """

    @overload
    def __init__(self, thePattern: nanoocp.Image.Image_PixMap | None) -> None:
        """
        Creates a new custom hatch style with the given pattern and unique style id
        @warning Raises a program error if given pattern image is not a valid 32*32 bitmap
        """

    @overload
    def __init__(self, theType: nanoocp.Aspect.Aspect_HatchStyle) -> None:
        """
        Creates a new predefined hatch style with the given id in Aspect_HatchStyle enum.
        GPU memory for the pattern will not be allocated.
        """

    @overload
    def __init__(self, theOther: Graphic3d_HatchStyle) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def HatchType(self) -> int:
        """
        In case if predefined OCCT style is used, returns
        index in Aspect_HatchStyle enumeration. If the style
        is custom, returns unique index of the style
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_PolygonOffset:
    """Polygon offset parameters."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_PolygonOffset) -> None: ...

    def __eq__(self, theOther: Graphic3d_PolygonOffset) -> bool:
        """Equality comparison."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def Mode(self) -> nanoocp.Aspect.Aspect_PolygonOffsetMode: ...

    @Mode.setter
    def Mode(self, arg: nanoocp.Aspect.Aspect_PolygonOffsetMode, /) -> None: ...

    @property
    def Factor(self) -> float: ...

    @Factor.setter
    def Factor(self, arg: float, /) -> None: ...

    @property
    def Units(self) -> float: ...

    @Units.setter
    def Units(self, arg: float, /) -> None: ...

class Graphic3d_ShaderAttribute(nanoocp.Standard.Standard_Transient):
    """Describes custom vertex shader attribute."""

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString, theLocation: int) -> None:
        """Creates new attribute."""

    @overload
    def __init__(self, theOther: Graphic3d_ShaderAttribute) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns name of shader variable."""

    def Location(self) -> int:
        """Returns attribute location to be bound on GLSL program linkage stage."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ShaderObject(nanoocp.Standard.Standard_Transient):
    """This class is responsible for managing shader objects."""

    def __init__(self, theOther: Graphic3d_ShaderObject) -> None: ...

    class ShaderVariable:
        """Structure defining shader uniform or in/out variable."""

        @overload
        def __init__(self) -> None:
            """Empty constructor."""

        @overload
        def __init__(self, theVarName: nanoocp.TCollection.TCollection_AsciiString, theShaderStageBits: int) -> None:
            """Create new shader variable."""

        @overload
        def __init__(self, theOther: Graphic3d_ShaderObject.ShaderVariable) -> None: ...

        @property
        def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
            """variable name"""

        @Name.setter
        def Name(self, arg: nanoocp.TCollection.TCollection_AsciiString, /) -> None: ...

        @property
        def Stages(self) -> int:
            """active stages as Graphic3d_TypeOfShaderObject bits;"""

        @Stages.setter
        def Stages(self, arg: int, /) -> None: ...

    @staticmethod
    def CreateFromFile(theType: Graphic3d_TypeOfShaderObject, thePath: nanoocp.TCollection.TCollection_AsciiString) -> Graphic3d_ShaderObject:
        """Creates new shader object from specified file."""

    @overload
    @staticmethod
    def CreateFromSource(theType: Graphic3d_TypeOfShaderObject, theSource: nanoocp.TCollection.TCollection_AsciiString) -> Graphic3d_ShaderObject:
        """Creates new shader object from specified source."""

    @overload
    @staticmethod
    def CreateFromSource(theSource: nanoocp.TCollection.TCollection_AsciiString, theType: Graphic3d_TypeOfShaderObject, theUniforms: nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderObject.ShaderVariable], theStageInOuts: nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderObject.ShaderVariable], theInName: nanoocp.TCollection.TCollection_AsciiString = ..., theOutName: nanoocp.TCollection.TCollection_AsciiString = ..., theNbGeomInputVerts: int = 0) -> Graphic3d_ShaderObject:
        """
        This is a preprocessor for Graphic3d_ShaderObject::CreateFromSource() function.
        Creates a new shader object from specified source according to list of uniforms and in/out
        variables.
        @param theSource      shader object source code to modify
        @param theType        shader object type to create
        @param theUniforms    list of uniform variables
        @param theStageInOuts list of stage in/out variables
        @param theInName      name of input  variables block;
        can be empty for accessing each variable without block prefix
        (mandatory for stages accessing both inputs and outputs)
        @param theOutName     name of output variables block;
        can be empty for accessing each variable without block prefix
        (mandatory for stages accessing both inputs and outputs)
        @param theNbGeomInputVerts number of geometry shader input vertexes
        """

    def IsDone(self) -> bool:
        """Checks if the shader object is valid or not."""

    def Path(self) -> nanoocp.OSD.OSD_Path:
        """Returns the full path to the shader source."""

    def Source(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the source code of the shader object."""

    def Type(self) -> Graphic3d_TypeOfShaderObject:
        """Returns type of the shader object."""

    def GetId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns unique ID used to manage resource in graphic driver."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_ValueInterface:
    """Interface for generic variable value."""

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

class Graphic3d_UniformValueTypeID__int:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__int) -> None: ...

class Graphic3d_UniformValueTypeID__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__float) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec2__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec2__float) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec3__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec3__float) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec4__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec4__float) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec2__int:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec2__int) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec3__int:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec3__int) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Vec4__int:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Vec4__int) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Mat3__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Mat3__float) -> None: ...

class Graphic3d_UniformValueTypeID__NCollection_Mat4__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_UniformValueTypeID__NCollection_Mat4__float) -> None: ...

class Graphic3d_UniformInt(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: int) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformInt) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> int:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: int, /) -> None: ...

class Graphic3d_UniformVec2i(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.BVH.BVH_Vec2i) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec2i) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.BVH.BVH_Vec2i:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

class Graphic3d_UniformVec3i(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.BVH.BVH_Vec3i) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec3i) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.BVH.BVH_Vec3i:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.BVH.BVH_Vec3i, /) -> None: ...

class Graphic3d_UniformVec4i(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.BVH.BVH_Vec4i) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec4i) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.BVH.BVH_Vec4i:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.BVH.BVH_Vec4i, /) -> None: ...

class Graphic3d_UniformFloat(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: float) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformFloat) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> float:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: float, /) -> None: ...

class Graphic3d_UniformVec2(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.BVH.BVH_Vec2f) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec2) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.BVH.BVH_Vec2f:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.BVH.BVH_Vec2f, /) -> None: ...

class Graphic3d_UniformVec3(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec3) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.Quantity.NCollection_Vec3__float, /) -> None: ...

class Graphic3d_UniformVec4(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformVec4) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.Quantity.NCollection_Vec4__float, /) -> None: ...

class Graphic3d_UniformMat3(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: NCollection_Mat3__float) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformMat3) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> NCollection_Mat3__float:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: NCollection_Mat3__float, /) -> None: ...

class Graphic3d_UniformMat4(Graphic3d_ValueInterface):
    """Describes specific value of custom uniform variable."""

    @overload
    def __init__(self, theValue: nanoocp.BVH.BVH_Mat4f) -> None:
        """Creates new variable value."""

    @overload
    def __init__(self, theOther: Graphic3d_UniformMat4) -> None: ...

    def TypeID(self) -> int:
        """Returns unique identifier of value type."""

    @property
    def Value(self) -> nanoocp.BVH.BVH_Mat4f:
        """Value of custom uniform variable."""

    @Value.setter
    def Value(self, arg: nanoocp.BVH.BVH_Mat4f, /) -> None: ...

class Graphic3d_ShaderVariable(nanoocp.Standard.Standard_Transient):
    """Describes custom uniform shader variable."""

    def __init__(self, theOther: Graphic3d_ShaderVariable) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns name of shader variable."""

    def IsDone(self) -> bool:
        """Checks if the shader variable is valid or not."""

    def Value(self) -> Graphic3d_ValueInterface:
        """Returns interface of shader variable value."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_TextureParams(nanoocp.Standard.Standard_Transient):
    """This class describes texture parameters."""

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_TextureParams) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def TextureUnit(self) -> Graphic3d_TextureUnit:
        """
        Default texture unit to be used, default is Graphic3d_TextureUnit_BaseColor.
        """

    def SetTextureUnit(self, theUnit: Graphic3d_TextureUnit) -> None:
        """Setup default texture unit."""

    def IsModulate(self) -> bool:
        """
        @return TRUE if the texture is modulate.
        Default value is FALSE.
        """

    def SetModulate(self, theToModulate: bool) -> None:
        """@param theToModulate turn modulation on/off."""

    def IsRepeat(self) -> bool:
        """
        @return TRUE if the texture repeat is enabled.
        Default value is FALSE.
        """

    def SetRepeat(self, theToRepeat: bool) -> None:
        """@param theToRepeat turn texture repeat mode ON or OFF (clamping)."""

    def Filter(self) -> Graphic3d_TypeOfTextureFilter:
        """
        @return texture interpolation filter.
        Default value is Graphic3d_TOTF_NEAREST.
        """

    def SetFilter(self, theFilter: Graphic3d_TypeOfTextureFilter) -> None:
        """@param theFilter texture interpolation filter."""

    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy:
        """
        @return level of anisontropy texture filter.
        Default value is Graphic3d_LOTA_OFF.
        """

    def SetAnisoFilter(self, theLevel: Graphic3d_LevelOfTextureAnisotropy) -> None:
        """@param theLevel level of anisontropy texture filter."""

    def Rotation(self) -> float:
        """
        Return rotation angle in degrees; 0 by default.
        Complete transformation matrix: Rotation -> Translation -> Scale.
        """

    def SetRotation(self, theAngleDegrees: float) -> None:
        """@param theAngleDegrees rotation angle."""

    def Scale(self) -> nanoocp.BVH.BVH_Vec2f:
        """
        Return scale factor; (1.0; 1.0) by default, which means no scaling.
        Complete transformation matrix: Rotation -> Translation -> Scale.
        """

    def SetScale(self, theScale: nanoocp.BVH.BVH_Vec2f) -> None:
        """@param theScale scale factor."""

    def Translation(self) -> nanoocp.BVH.BVH_Vec2f:
        """
        Return translation vector; (0.0; 0.0), which means no translation.
        Complete transformation matrix: Rotation -> Translation -> Scale.
        """

    def SetTranslation(self, theVec: nanoocp.BVH.BVH_Vec2f) -> None:
        """@param theVec translation vector."""

    def GenMode(self) -> Graphic3d_TypeOfTextureMode:
        """
        @return texture coordinates generation mode.
        Default value is Graphic3d_TOTM_MANUAL.
        """

    def GenPlaneS(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """@return texture coordinates generation plane S."""

    def GenPlaneT(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """@return texture coordinates generation plane T."""

    def SetGenMode(self, theMode: Graphic3d_TypeOfTextureMode, thePlaneS: nanoocp.Quantity.NCollection_Vec4__float, thePlaneT: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Setup texture coordinates generation mode."""

    def BaseLevel(self) -> int:
        """@return base texture mipmap level; 0 by default."""

    def MaxLevel(self) -> int:
        """
        Return maximum texture mipmap array level; 1000 by default.
        Real rendering limit will take into account mipmap generation flags and presence of mipmaps in
        loaded image.
        """

    def SetLevelsRange(self, theFirstLevel: int, theSecondLevel: int = 0) -> None:
        """
        Setups texture mipmap array levels range.
        The lowest value will be the base level.
        The remaining one will be the maximum level.
        """

    def SamplerRevision(self) -> int:
        """Return modification counter of parameters related to sampler state."""

class Graphic3d_ShaderProgram(nanoocp.Standard.Standard_Transient):
    """This class is responsible for managing shader programs."""

    @overload
    def __init__(self) -> None:
        """Creates new empty program object."""

    @overload
    def __init__(self, theOther: Graphic3d_ShaderProgram) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsDone(self) -> bool:
        """Checks if the program object is valid or not."""

    def GetId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns unique ID used to manage resource in graphic driver."""

    def SetId(self, theId: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets unique ID used to manage resource in graphic driver.
        WARNING! Graphic3d_ShaderProgram constructor generates a unique id for proper resource
        management; however if application overrides it, it is responsibility of application to avoid
        name collisions.
        """

    def Header(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns GLSL header (version code and extensions)."""

    def SetHeader(self, theHeader: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Setup GLSL header containing language version code and used extensions.
        Will be prepended to the very beginning of the source code.
        Example:
        @code
        #version 300 es
        #extension GL_ARB_bindless_texture : require
        @endcode
        """

    def AppendToHeader(self, theHeaderLine: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Append line to GLSL header."""

    def NbLightsMax(self) -> int:
        """
        Return the length of array of light sources (THE_MAX_LIGHTS),
        to be used for initialization occLightSources.
        Default value is THE_MAX_LIGHTS_DEFAULT.
        """

    def SetNbLightsMax(self, theNbLights: int) -> None:
        """Specify the length of array of light sources (THE_MAX_LIGHTS)."""

    def NbShadowMaps(self) -> int:
        """
        Return the length of array of shadow maps (THE_NB_SHADOWMAPS); 0 by default.
        """

    def SetNbShadowMaps(self, theNbMaps: int) -> None:
        """Specify the length of array of shadow maps (THE_NB_SHADOWMAPS)."""

    def NbClipPlanesMax(self) -> int:
        """
        Return the length of array of clipping planes (THE_MAX_CLIP_PLANES),
        to be used for initialization occClipPlaneEquations.
        Default value is THE_MAX_CLIP_PLANES_DEFAULT.
        """

    def SetNbClipPlanesMax(self, theNbPlanes: int) -> None:
        """Specify the length of array of clipping planes (THE_MAX_CLIP_PLANES)."""

    def AttachShader(self, theShader: Graphic3d_ShaderObject | None) -> bool:
        """Attaches shader object to the program object."""

    def DetachShader(self, theShader: Graphic3d_ShaderObject | None) -> bool:
        """Detaches shader object from the program object."""

    def ShaderObjects(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderObject]:
        """Returns list of attached shader objects."""

    def Variables(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderVariable]:
        """
        The list of currently pushed but not applied custom uniform variables.
        This list is automatically cleared after applying to GLSL program.
        """

    def VertexAttributes(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderAttribute]:
        """Return the list of custom vertex attributes."""

    def SetVertexAttributes(self, theAttributes: nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_ShaderAttribute]) -> None:
        """
        Assign the list of custom vertex attributes.
        Should be done before GLSL program initialization.
        """

    def NbFragmentOutputs(self) -> int:
        """
        Returns the number (1+) of Fragment Shader outputs to be written to
        (more than 1 can be in case of multiple draw buffers); 1 by default.
        """

    def SetNbFragmentOutputs(self, theNbOutputs: int) -> None:
        """
        Sets the number of Fragment Shader outputs to be written to.
        Should be done before GLSL program initialization.
        """

    def HasAlphaTest(self) -> bool:
        """
        Return true if Fragment Shader should perform alpha test; FALSE by default.
        """

    def SetAlphaTest(self, theAlphaTest: bool) -> None:
        """
        Set if Fragment Shader should perform alpha test.
        Note that this flag is designed for usage with - custom shader program may discard fragment
        regardless this flag.
        """

    def HasDefaultSampler(self) -> bool:
        """
        Return TRUE if standard program header should define default texture sampler occSampler0; TRUE
        by default for compatibility.
        """

    def SetDefaultSampler(self, theHasDefSampler: bool) -> None:
        """
        Set if standard program header should define default texture sampler occSampler0.
        """

    def OitOutput(self) -> Graphic3d_RenderTransparentMethod:
        """
        Return if Fragment Shader color should output to OIT buffers; OFF by default.
        """

    def SetOitOutput(self, theOutput: Graphic3d_RenderTransparentMethod) -> None:
        """
        Set if Fragment Shader color should output to OIT buffers.
        Note that weighted OIT also requires at least 2 Fragment Outputs (color + coverage),
        and Depth Peeling requires at least 3 Fragment Outputs (depth + front color + back color),
        """

    def IsPBR(self) -> bool:
        """
        Return TRUE if standard program header should define functions and variables used in PBR
        pipeline. FALSE by default.
        """

    def SetPBR(self, theIsPBR: bool) -> None:
        """
        Sets whether standard program header should define functions and variables used in PBR
        pipeline.
        """

    def TextureSetBits(self) -> int:
        """
        Return texture units declared within the program, @sa Graphic3d_TextureSetBits.
        """

    def SetTextureSetBits(self, theBits: int) -> None:
        """Set texture units declared within the program."""

    def ClearVariables(self) -> None:
        """Removes all custom uniform variables from the program."""

    def PushVariableFloat(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: float) -> bool:
        """Pushes float uniform."""

    def PushVariableVec2(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.BVH.BVH_Vec2f) -> bool:
        """Pushes vec2 uniform."""

    def PushVariableVec3(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.Quantity.NCollection_Vec3__float) -> bool:
        """Pushes vec3 uniform."""

    def PushVariableVec4(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """Pushes vec4 uniform."""

    def PushVariableInt(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: int) -> bool:
        """Pushes int uniform."""

    def PushVariableVec2i(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.BVH.BVH_Vec2i) -> bool:
        """Pushes vec2i uniform."""

    def PushVariableVec3i(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.BVH.BVH_Vec3i) -> bool:
        """Pushes vec3i uniform."""

    def PushVariableVec4i(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.BVH.BVH_Vec4i) -> bool:
        """Pushes vec4i uniform."""

    def PushVariableMat3(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: NCollection_Mat3__float) -> bool:
        """Pushes mat3 uniform."""

    def PushVariableMat4(self, theName: nanoocp.TCollection.TCollection_AsciiString, theValue: nanoocp.BVH.BVH_Mat4f) -> bool:
        """Pushes mat4 uniform."""

    @staticmethod
    def ShadersFolder() -> nanoocp.TCollection.TCollection_AsciiString:
        """
        The path to GLSL programs determined from CSF_ShadersDirectory or CASROOT environment
        variables.
        @return the root folder with default GLSL programs.
        """

class Graphic3d_TextureRoot(nanoocp.Standard.Standard_Transient):
    """
    This is the texture root class enable the dialog with the GraphicDriver allows the loading of
    texture.
    """

    def __init__(self, theOther: Graphic3d_TextureRoot) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def TexturesFolder() -> nanoocp.TCollection.TCollection_AsciiString:
        """
        The path to textures determined from CSF_MDTVTexturesDirectory or CASROOT environment
        variables.
        @return the root folder with default textures.
        """

    def IsDone(self) -> bool:
        """
        Checks if a texture class is valid or not.
        @return true if the construction of the class is correct
        """

    def Path(self) -> nanoocp.OSD.OSD_Path:
        """
        Returns the full path of the defined texture.
        It could be empty path if GetImage() is overridden to load image not from file.
        """

    def Type(self) -> Graphic3d_TypeOfTexture:
        """@return the texture type."""

    def GetId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        This ID will be used to manage resource in graphic driver.

        Default implementation generates unique ID within constructor;
        inheritors may re-initialize it within their constructor,
        but should never modify it afterwards.

        Multiple Graphic3d_TextureRoot instances with same ID
        will be treated as single texture with different parameters
        to optimize memory usage though this will be more natural
        to use same instance of Graphic3d_TextureRoot when possible.

        If this ID is set to empty string by inheritor,
        then independent graphical resource will be created
        for each instance of Graphic3d_AspectFillArea3d where texture will be used.

        @return texture identifier.
        """

    def Revision(self) -> int:
        """Return image revision."""

    def UpdateRevision(self) -> None:
        """
        Update image revision.
        Can be used for signaling changes in the texture source (e.g. file update, pixmap update)
        without re-creating texture source itself (since unique id should be never modified).
        """

    def GetCompressedImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_CompressedPixMap:
        """
        This method will be called by graphic driver each time when texture resource should be
        created. It is called in front of GetImage() for uploading compressed image formats natively
        supported by GPU.
        @param[in] theSupported  the list of supported compressed texture formats;
        returning image in unsupported format will result in texture upload
        failure
        @return compressed pixmap or NULL if image is not in supported compressed format
        """

    def GetImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """
        This method will be called by graphic driver each time when texture resource should be
        created. Default constructors allow defining the texture source as path to texture image or
        directly as pixmap. If the source is defined as path, then the image will be dynamically
        loaded when this method is called (and no copy will be preserved in this class instance).
        Inheritors may dynamically generate the image.
        Notice, image data should be in Bottom-Up order (see Image_PixMap::IsTopDown())!
        @return the image for texture.
        """

    def GetParams(self) -> Graphic3d_TextureParams:
        """@return low-level texture parameters"""

    def IsColorMap(self) -> bool:
        """
        Return flag indicating color nature of values within the texture; TRUE by default.

        This flag will be used to interpret 8-bit per channel RGB(A) images as sRGB(A) textures
        with implicit linearizion of color components.
        Has no effect on images with floating point values (always considered linearized).

        When set to FALSE, such images will be interpreted as textures will be linear component
        values, which is useful for RGB(A) textures defining non-color properties (like
        Normalmap/Metalness/Roughness).
        """

    def SetColorMap(self, theIsColor: bool) -> None:
        """Set flag indicating color nature of values within the texture."""

    def HasMipmaps(self) -> bool:
        """Returns whether mipmaps should be generated or not."""

    def SetMipmapsGeneration(self, theToGenerateMipmaps: bool) -> None:
        """Sets whether to generate mipmaps or not."""

    def IsTopDown(self) -> bool:
        """Returns whether row's memory layout is top-down."""

class Graphic3d_TextureMap(Graphic3d_TextureRoot):
    """This is an abstract class for managing texture applicable on polygons."""

    def __init__(self, theOther: Graphic3d_TextureMap) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def EnableSmooth(self) -> None:
        """enable texture smoothing"""

    def IsSmoothed(self) -> bool:
        """Returns TRUE if the texture is smoothed."""

    def DisableSmooth(self) -> None:
        """disable texture smoothing"""

    def EnableModulate(self) -> None:
        """
        enable texture modulate mode.
        the image is modulate with the shading of the surface.
        """

    def DisableModulate(self) -> None:
        """
        disable texture modulate mode.
        the image is directly decal on the surface.
        """

    def IsModulate(self) -> bool:
        """Returns TRUE if the texture is modulate."""

    def EnableRepeat(self) -> None:
        """
        use this methods if you want to enable
        texture repetition on your objects.
        """

    def DisableRepeat(self) -> None:
        """
        use this methods if you want to disable
        texture repetition on your objects.
        """

    def IsRepeat(self) -> bool:
        """Returns TRUE if the texture repeat is enable."""

    def AnisoFilter(self) -> Graphic3d_LevelOfTextureAnisotropy:
        """
        @return level of anisotropy texture filter.
        Default value is Graphic3d_LOTA_OFF.
        """

    def SetAnisoFilter(self, theLevel: Graphic3d_LevelOfTextureAnisotropy) -> None:
        """@param theLevel level of anisotropy texture filter."""

class Graphic3d_TextureSet(nanoocp.Standard.Standard_Transient):
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
    def __init__(self, theTexture: Graphic3d_TextureMap | None) -> None:
        """Constructor for a single texture."""

    @overload
    def __init__(self, theOther: Graphic3d_TextureSet) -> None: ...

    class Iterator(NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap):
        """Class for iterating texture set."""

        @overload
        def __init__(self) -> None:
            """Empty constructor."""

        @overload
        def __init__(self, theSet: Graphic3d_TextureSet | None) -> None:
            """Constructor."""

        @overload
        def __init__(self, theOther: Graphic3d_TextureSet.Iterator) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsEmpty(self) -> bool:
        """Return TRUE if texture array is empty."""

    def Size(self) -> int:
        """Return number of textures."""

    def Lower(self) -> int:
        """Return the lower index in texture set."""

    def Upper(self) -> int:
        """Return the upper index in texture set."""

    def First(self) -> Graphic3d_TextureMap:
        """Return the first texture."""

    def SetFirst(self, theTexture: Graphic3d_TextureMap | None) -> None:
        """Return the first texture."""

    def Value(self, theIndex: int) -> Graphic3d_TextureMap:
        """Return the texture at specified position within [0, Size()) range."""

    def SetValue(self, theIndex: int, theTexture: Graphic3d_TextureMap | None) -> None:
        """Return the texture at specified position within [0, Size()) range."""

class NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap:
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
    def __init__(self, theOther: NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_TextureMap]) -> None: ...

    @overload
    def __init__(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_TextureMap], theOther: "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<opencascade::handle<Graphic3d_TextureMap>>, opencascade::handle<Graphic3d_TextureMap>, false>") -> None: ...

    def __iter__(self) -> NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap:
        """
        Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
        """

    def __next__(self) -> Graphic3d_TextureMap:
        """Python addition: see __iter__."""

    def Init(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_TextureMap]) -> None: ...

    def More(self) -> bool: ...

    def Initialize(self, theList: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_TextureMap]) -> None: ...

    def ValueIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<opencascade::handle<Graphic3d_TextureMap>>, opencascade::handle<Graphic3d_TextureMap>, false>": ...

    def ChangeValueIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<opencascade::handle<Graphic3d_TextureMap>>, opencascade::handle<Graphic3d_TextureMap>, false>": ...

    def EndIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<opencascade::handle<Graphic3d_TextureMap>>, opencascade::handle<Graphic3d_TextureMap>, false>": ...

    def ChangeEndIter(self) -> "NCollection_IndexedIterator<std::__1::random_access_iterator_tag, NCollection_Array1<opencascade::handle<Graphic3d_TextureMap>>, opencascade::handle<Graphic3d_TextureMap>, false>": ...

    def Next(self) -> None: ...

    def Value(self) -> Graphic3d_TextureMap: ...

    def ChangeValue(self) -> Graphic3d_TextureMap: ...

    def __eq__(self, theOther: NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap) -> bool: ...

    def __ne__(self, theOther: NCollection_Iterator__NCollection_Array1__Handle_Graphic3d_TextureMap) -> bool: ...

class Graphic3d_Aspects(nanoocp.Standard.Standard_Transient):
    """This class defines graphic attributes."""

    @overload
    def __init__(self) -> None:
        """
        Creates a context table for drawing primitives defined with the following default values:
        """

    @overload
    def __init__(self, theOther: Graphic3d_Aspects) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def InteriorStyle(self) -> nanoocp.Aspect.Aspect_InteriorStyle:
        """Return interior rendering style; Aspect_IS_SOLID by default."""

    def SetInteriorStyle(self, theStyle: nanoocp.Aspect.Aspect_InteriorStyle) -> None:
        """Modifies the interior type used for rendering"""

    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel:
        """
        Returns shading model; Graphic3d_TypeOfShadingModel_DEFAULT by default.
        Graphic3d_TOSM_DEFAULT means that Shading Model set as default for entire Viewer will be used.
        """

    def SetShadingModel(self, theShadingModel: Graphic3d_TypeOfShadingModel) -> None:
        """Sets shading model"""

    def AlphaMode(self) -> Graphic3d_AlphaMode:
        """
        Returns the way how alpha value should be treated (Graphic3d_AlphaMode_BlendAuto by default,
        for backward compatibility).
        """

    def AlphaCutoff(self) -> float:
        """
        Returns alpha cutoff threshold, for discarding fragments within Graphic3d_AlphaMode_Mask mode
        (0.5 by default). If the alpha value is greater than or equal to this value then it is
        rendered as fully opaque, otherwise, it is rendered as fully transparent.
        """

    def SetAlphaMode(self, theMode: Graphic3d_AlphaMode, theAlphaCutoff: float = 0.5) -> None:
        """Defines the way how alpha value should be treated."""

    def ColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return color"""

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Return the color."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Modifies the color."""

    def InteriorColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return interior color."""

    def InteriorColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return interior color."""

    @overload
    def SetInteriorColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetInteriorColor(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies the color of the interior of the face"""

    def BackInteriorColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return back interior color."""

    def BackInteriorColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return back interior color."""

    @overload
    def SetBackInteriorColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetBackInteriorColor(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies the color of the interior of the back face"""

    def FrontMaterial(self) -> Graphic3d_MaterialAspect:
        """Returns the surface material of external faces"""

    def ChangeFrontMaterial(self) -> Graphic3d_MaterialAspect:
        """Returns the surface material of external faces"""

    def SetFrontMaterial(self, theMaterial: Graphic3d_MaterialAspect) -> None:
        """Modifies the surface material of external faces"""

    def BackMaterial(self) -> Graphic3d_MaterialAspect:
        """Returns the surface material of internal faces"""

    def ChangeBackMaterial(self) -> Graphic3d_MaterialAspect:
        """Returns the surface material of internal faces"""

    def SetBackMaterial(self, theMaterial: Graphic3d_MaterialAspect) -> None:
        """Modifies the surface material of internal faces"""

    def FaceCulling(self) -> Graphic3d_TypeOfBackfacingModel:
        """
        Return face culling mode; Graphic3d_FaceCulling_BackClosed by default.
        A back-facing polygon is defined as a polygon whose
        vertices are in a clockwise order with respect to screen coordinates.
        """

    def SetFaceCulling(self, theCulling: Graphic3d_TypeOfBackfacingModel) -> None:
        """Set face culling mode."""

    def Distinguish(self) -> bool:
        """
        Returns true if material properties should be distinguished for back and front faces (false by
        default).
        """

    def SetDistinguish(self, toDistinguish: bool) -> None:
        """Set material distinction between front and back faces."""

    def SetDistinguishOn(self) -> None:
        """Allows material distinction between front and back faces."""

    def SetDistinguishOff(self) -> None:
        """Forbids material distinction between front and back faces."""

    def ToUseVertexColorForBackFaces(self) -> bool:
        """
        Return true if per-vertex color should be applied to back-facing fragments.
        True by default for backward compatibility.
        """

    def SetUseVertexColorForBackFaces(self, theToUse: bool) -> None:
        """
        Set whether per-vertex color should be applied to back-facing fragments.
        When disabled, back faces use back material/interior color without vertex color modulation.
        """

    def ShaderProgram(self) -> Graphic3d_ShaderProgram:
        """Return shader program."""

    def SetShaderProgram(self, theProgram: Graphic3d_ShaderProgram | None) -> None:
        """Sets up OpenGL/GLSL shader program."""

    def TextureSet(self) -> Graphic3d_TextureSet:
        """Return texture array to be mapped."""

    def SetTextureSet(self, theTextures: Graphic3d_TextureSet | None) -> None:
        """Setup texture array to be mapped."""

    def TextureMap(self) -> Graphic3d_TextureMap:
        """Return texture to be mapped."""

    def SetTextureMap(self, theTexture: Graphic3d_TextureMap | None) -> None:
        """
        Assign texture to be mapped.
        See also SetTextureMapOn() to actually activate texture mapping.
        """

    def ToMapTexture(self) -> bool:
        """Return true if texture mapping is enabled (false by default)."""

    def TextureMapState(self) -> bool:
        """Return true if texture mapping is enabled (false by default)."""

    @overload
    def SetTextureMapOn(self, theToMap: bool) -> None:
        """
        Enable or disable texture mapping (has no effect if texture is not set).
        """

    @overload
    def SetTextureMapOn(self) -> None:
        """Enable texture mapping (has no effect if texture is not set)."""

    def SetTextureMapOff(self) -> None:
        """Disable texture mapping."""

    def PolygonOffset(self) -> Graphic3d_PolygonOffset:
        """Returns current polygon offsets settings."""

    def SetPolygonOffset(self, theOffset: Graphic3d_PolygonOffset) -> None:
        """Sets polygon offsets settings."""

    def PolygonOffsets(self) -> tuple[int, float, float]:
        """Returns current polygon offsets settings."""

    def SetPolygonOffsets(self, theMode: int, theFactor: float = 1.0, theUnits: float = 0.0) -> None:
        """
        Sets up OpenGL polygon offsets mechanism.
        <aMode> parameter can contain various combinations of
        Aspect_PolygonOffsetMode enumeration elements (Aspect_POM_None means
        that polygon offsets are not changed).
        If <aMode> is different from Aspect_POM_Off and Aspect_POM_None, then <aFactor> and <aUnits>
        arguments are used by graphic renderer to calculate a depth offset value:

        offset = <aFactor> * m + <aUnits> * r, where
        m - maximum depth slope for the polygon currently being displayed,
        r - minimum window coordinates depth resolution (implementation-specific)

        Default settings for OCC 3D viewer: mode = Aspect_POM_Fill, factor = 1., units = 1.

        Negative offset values move polygons closer to the viewport,
        while positive values shift polygons away.
        Consult OpenGL reference for details (glPolygonOffset function description).
        """

    def LineType(self) -> nanoocp.Aspect.Aspect_TypeOfLine:
        """Return line type; Aspect_TOL_SOLID by default."""

    def SetLineType(self, theType: nanoocp.Aspect.Aspect_TypeOfLine) -> None:
        """Modifies the line type"""

    def LinePattern(self) -> int:
        """Return custom stipple line pattern; 0xFFFF by default."""

    def SetLinePattern(self, thePattern: int) -> None:
        """
        Modifies the stipple line pattern, and changes line type to Aspect_TOL_USERDEFINED for
        non-standard pattern.
        """

    def LineStippleFactor(self) -> int:
        """
        Return a multiplier for each bit in the line stipple pattern within [1, 256] range; 1 by
        default.
        """

    def SetLineStippleFactor(self, theFactor: int) -> None:
        """Set a multiplier for each bit in the line stipple pattern."""

    def LineWidth(self) -> float:
        """Return width for edges in pixels; 1.0 by default."""

    def SetLineWidth(self, theWidth: float) -> None:
        """
        Modifies the line thickness
        Warning: Raises Standard_OutOfRange if the width is a negative value.
        """

    @staticmethod
    def DefaultLinePatternForType(theType: nanoocp.Aspect.Aspect_TypeOfLine) -> int:
        """Return stipple line pattern for line type."""

    @staticmethod
    def DefaultLineTypeForPattern(thePattern: int) -> nanoocp.Aspect.Aspect_TypeOfLine:
        """Return line type for stipple line pattern."""

    def MarkerType(self) -> nanoocp.Aspect.Aspect_TypeOfMarker:
        """Return marker type; Aspect_TOM_POINT by default."""

    def SetMarkerType(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker) -> None:
        """Modifies the type of marker."""

    def MarkerScale(self) -> float:
        """Return marker scale factor; 1.0 by default."""

    def SetMarkerScale(self, theScale: float) -> None:
        """
        Modifies the scale factor.
        Marker type Aspect_TOM_POINT is not affected by the marker size scale factor.
        It is always the smallest displayable dot.
        Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """

    def MarkerImage(self) -> Graphic3d_MarkerImage:
        """
        Returns marker's image texture.
        Could be null handle if marker aspect has been initialized as default type of marker.
        """

    def SetMarkerImage(self, theImage: Graphic3d_MarkerImage | None) -> None:
        """Set marker's image texture."""

    def IsMarkerSprite(self) -> bool:
        """
        Returns TRUE if marker should be drawn using marker sprite (either user-provided or
        generated).
        """

    def TextFont(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns the font; NULL string by default."""

    def SetTextFont(self, theFont: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Modifies the font."""

    def TextFontAspect(self) -> nanoocp.Font.Font_FontAspect:
        """Returns text FontAspect"""

    def SetTextFontAspect(self, theFontAspect: nanoocp.Font.Font_FontAspect) -> None:
        """Turns usage of Aspect text"""

    def TextDisplayType(self) -> nanoocp.Aspect.Aspect_TypeOfDisplayText:
        """Returns display type; Aspect_TODT_NORMAL by default."""

    def SetTextDisplayType(self, theType: nanoocp.Aspect.Aspect_TypeOfDisplayText) -> None:
        """Sets display type."""

    def ColorSubTitleRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Returns text background/shadow color; equals to EdgeColor() property."""

    def ColorSubTitle(self) -> nanoocp.Quantity.Quantity_Color:
        """Return text background/shadow color; equals to EdgeColor() property."""

    @overload
    def SetColorSubTitle(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetColorSubTitle(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies text background/shadow color; equals to EdgeColor() property."""

    def IsTextZoomable(self) -> bool:
        """Returns TRUE when the Text Zoomable is on."""

    def SetTextZoomable(self, theFlag: bool) -> None:
        """Turns usage of text zoomable on/off"""

    def TextStyle(self) -> nanoocp.Aspect.Aspect_TypeOfStyleText:
        """Returns the text style; Aspect_TOST_NORMAL by default."""

    def SetTextStyle(self, theStyle: nanoocp.Aspect.Aspect_TypeOfStyleText) -> None:
        """Modifies the style of the text."""

    def TextAngle(self) -> float:
        """Returns Angle of degree"""

    def SetTextAngle(self, theAngle: float) -> None:
        """Turns usage of text rotated"""

    def ToDrawEdges(self) -> bool:
        """Returns true if mesh edges should be drawn (false by default)."""

    def SetDrawEdges(self, theToDraw: bool) -> None:
        """Set if mesh edges should be drawn or not."""

    def SetEdgeOn(self) -> None:
        """The edges of FillAreas are drawn."""

    def SetEdgeOff(self) -> None:
        """The edges of FillAreas are not drawn."""

    def EdgeColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return color of edges."""

    def EdgeColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return color of edges."""

    @overload
    def SetEdgeColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetEdgeColor(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies the color of the edge of the face"""

    def EdgeLineType(self) -> nanoocp.Aspect.Aspect_TypeOfLine:
        """Return edges line type (same as LineType())."""

    def SetEdgeLineType(self, theType: nanoocp.Aspect.Aspect_TypeOfLine) -> None:
        """Modifies the edge line type (same as SetLineType())"""

    def EdgeWidth(self) -> float:
        """Return width for edges in pixels (same as LineWidth())."""

    def SetEdgeWidth(self, theWidth: float) -> None:
        """Modifies the edge thickness (same as SetLineWidth())"""

    def ToSkipFirstEdge(self) -> bool:
        """
        Returns TRUE if drawing element edges should discard first edge in triangle; FALSE by default.
        Graphics hardware works mostly with triangles, so that wireframe presentation will draw
        triangle edges by default. This flag allows rendering wireframe presentation of quad-only
        array split into triangles. For this, quads should be split in specific order, so that the
        quad diagonal (to be NOT rendered) goes first:
        1------2
        /      /   Triangle #1: 2-0-1; Triangle #2: 0-2-3
        0------3
        """

    def SetSkipFirstEdge(self, theToSkipFirstEdge: bool) -> None:
        """
        Set skip first triangle edge flag for drawing wireframe presentation of quads array split into
        triangles.
        """

    def ToDrawSilhouette(self) -> bool:
        """
        Returns TRUE if silhouette (outline) should be drawn (with edge color and width); FALSE by
        default.
        """

    def SetDrawSilhouette(self, theToDraw: bool) -> None:
        """Enables/disables drawing silhouette (outline)."""

    def HatchStyle(self) -> Graphic3d_HatchStyle:
        """Returns the hatch type used when InteriorStyle is IS_HATCH"""

    @overload
    def SetHatchStyle(self, theStyle: Graphic3d_HatchStyle | None) -> None:
        """Modifies the hatch type used when InteriorStyle is IS_HATCH"""

    @overload
    def SetHatchStyle(self, theStyle: nanoocp.Aspect.Aspect_HatchStyle) -> None:
        """
        Modifies the hatch type used when InteriorStyle is IS_HATCH
        @warning This method always creates a new handle for a given hatch style
        """

    def IsEqual(self, theOther: Graphic3d_Aspects) -> bool:
        """Check for equality with another aspects."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def ToSuppressBackFaces(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method, FaceCulling() should be used instead
        """

    def SetSuppressBackFaces(self, theToSuppress: bool) -> None:
        """
        Deprecated in OCCT: Deprecated method, SetFaceCulling() should be used instead
        """

    def BackFace(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method, FaceCulling() should be used instead
        """

    def AllowBackFace(self) -> None:
        """
        Deprecated in OCCT: Deprecated method, SetFaceCulling() should be used instead
        """

    def SuppressBackFace(self) -> None:
        """
        Deprecated in OCCT: Deprecated method, SetFaceCulling() should be used instead
        """

class Graphic3d_AspectFillArea3d(Graphic3d_Aspects):
    """
    This class defines graphic attributes for opaque 3d primitives (polygons, triangles,
    quadrilaterals).
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a context table for fill area primitives defined with the following default values:

        InteriorStyle : Aspect_IS_EMPTY
        InteriorColor : Quantity_NOC_CYAN1
        EdgeColor     : Quantity_NOC_WHITE
        EdgeLineType  : Aspect_TOL_SOLID
        EdgeWidth     : 1.0
        FrontMaterial : NOM_BRASS
        BackMaterial  : NOM_BRASS
        HatchStyle    : Aspect_HS_SOLID

        Display of back-facing filled polygons.
        No distinction between external and internal faces of FillAreas.
        The edges are not drawn.
        Polygon offset parameters: mode = Aspect_POM_None, factor = 1., units = 0.
        """

    @overload
    def __init__(self, theInterior: nanoocp.Aspect.Aspect_InteriorStyle, theInteriorColor: nanoocp.Quantity.Quantity_Color, theEdgeColor: nanoocp.Quantity.Quantity_Color, theEdgeLineType: nanoocp.Aspect.Aspect_TypeOfLine, theEdgeWidth: float, theFrontMaterial: Graphic3d_MaterialAspect, theBackMaterial: Graphic3d_MaterialAspect) -> None:
        """
        Creates a context table for fill area primitives defined with the specified values.
        Display of back-facing filled polygons.
        No distinction between external and internal faces of FillAreas.
        The edges are not drawn.
        Polygon offset parameters: mode = Aspect_POM_None, factor = 1., units = 0.
        """

    @overload
    def __init__(self, theOther: Graphic3d_AspectFillArea3d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Edge(self) -> bool:
        """
        Deprecated in OCCT: Deprecated method, ToDrawEdges() should be used instead
        """

class Graphic3d_AspectLine3d(Graphic3d_Aspects):
    """
    Creates and updates a group of attributes for 3d line primitives.
    This group contains the color, the type of line, and its thickness.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a context table for line primitives
        defined with the following default values:

        Color = Quantity_NOC_YELLOW;
        Type  = Aspect_TOL_SOLID;
        Width = 1.0;
        """

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_TypeOfLine, theWidth: float) -> None:
        """
        Creates a context table for line primitives defined with the specified values.
        Warning: theWidth is the "line width scale factor".
        The nominal line width is 1 pixel.
        The width of the line is determined by applying the line width scale factor to this nominal
        line width. The supported line widths vary by 1-pixel units.
        """

    @overload
    def __init__(self, theOther: Graphic3d_AspectLine3d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Type(self) -> nanoocp.Aspect.Aspect_TypeOfLine:
        """Return line type."""

    def SetType(self, theType: nanoocp.Aspect.Aspect_TypeOfLine) -> None:
        """Modifies the type of line."""

    def Width(self) -> float:
        """Return line width."""

    @overload
    def SetWidth(self, theWidth: float) -> None: ...

    @overload
    def SetWidth(self, theWidth: float) -> None:
        """
        Modifies the line thickness.
        Warning: Raises Standard_OutOfRange if the width is a negative value.
        """

class Graphic3d_AspectMarker3d(Graphic3d_Aspects):
    """
    Creates and updates an attribute group for marker type primitives.
    This group contains the type of marker, its color, and its scale factor.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a context table for marker primitives
        defined with the following default values:

        Marker type : TOM_X
        Color       : YELLOW
        Scale factor: 1.0
        """

    @overload
    def __init__(self, theTextureImage: nanoocp.Image.Image_PixMap | None) -> None: ...

    @overload
    def __init__(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker, theColor: nanoocp.Quantity.Quantity_Color, theScale: float) -> None: ...

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theWidth: int, theHeight: int, theTextureBitmap: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> None:
        """
        Creates a context table for marker primitives
        defined with the specified values.
        """

    @overload
    def __init__(self, theOther: Graphic3d_AspectMarker3d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Scale(self) -> float:
        """Return scale factor."""

    @overload
    def SetScale(self, theScale: float) -> None:
        """Assign scale factor."""

    @overload
    def SetScale(self, theScale: float) -> None:
        """
        Modifies the scale factor.
        Marker type Aspect_TOM_POINT is not affected by the marker size scale factor.
        It is always the smallest displayable dot.
        Warning: Raises Standard_OutOfRange if the scale is a negative value.
        """

    def Type(self) -> nanoocp.Aspect.Aspect_TypeOfMarker:
        """Return marker type."""

    def SetType(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker) -> None:
        """Modifies the type of marker."""

    def GetTextureSize(self) -> tuple[int, int]:
        """Returns marker's texture size."""

    def GetMarkerImage(self) -> Graphic3d_MarkerImage:
        """
        Returns marker's image texture.
        Could be null handle if marker aspect has been initialized as default type of marker.
        """

    def SetBitMap(self, theWidth: int, theHeight: int, theTexture: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> None: ...

class Graphic3d_AspectText3d(Graphic3d_Aspects):
    """Creates and updates a group of attributes for text primitives."""

    @overload
    def __init__(self) -> None:
        """
        Creates a context table for text primitives defined with the following default values:
        Color            : Quantity_NOC_YELLOW
        Font             : Font_NOF_ASCII_MONO
        The style        : Aspect_TOST_NORMAL
        The display type : Aspect_TODT_NORMAL
        """

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theFont: str, theExpansionFactor: float, theSpace: float, theStyle: nanoocp.Aspect.Aspect_TypeOfStyleText = Aspect_TypeOfStyleText.Aspect_TOST_NORMAL, theDisplayType: nanoocp.Aspect.Aspect_TypeOfDisplayText = Aspect_TypeOfDisplayText.Aspect_TODT_NORMAL) -> None:
        """
        Creates a context table for text primitives defined with the specified values.
        @param[in] theColor  text color
        @param[in] theFont   font family name or alias like Font_NOF_ASCII_MONO
        @param[in] theExpansionFactor  deprecated parameter, has no effect
        @param[in] theSpace  deprecated parameter, has no effect
        @param[in] theStyle  font style
        @param[in] theDisplayType  display mode
        """

    @overload
    def __init__(self, theOther: Graphic3d_AspectText3d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Return the text color."""

    def ColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Return the text color."""

    @overload
    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    @overload
    def SetColor(self, theColor: nanoocp.Quantity.Quantity_ColorRGBA) -> None:
        """Modifies the color."""

    def Font(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return the font."""

    @overload
    def SetFont(self, theFont: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def SetFont(self, theFont: str) -> None:
        """Modifies the font."""

    def Style(self) -> nanoocp.Aspect.Aspect_TypeOfStyleText:
        """Return the text style."""

    def SetStyle(self, theStyle: nanoocp.Aspect.Aspect_TypeOfStyleText) -> None:
        """Modifies the style of the text."""

    def DisplayType(self) -> nanoocp.Aspect.Aspect_TypeOfDisplayText:
        """Return display type."""

    def SetDisplayType(self, theDisplayType: nanoocp.Aspect.Aspect_TypeOfDisplayText) -> None:
        """Define the display type of the text."""

    def GetTextZoomable(self) -> bool:
        """Returns TRUE when the Text Zoomable is on."""

    def GetTextAngle(self) -> float:
        """Returns Angle of degree"""

    def SetTextAngle(self, theAngle: float) -> None:
        """Turns usage of text rotated"""

    def GetTextFontAspect(self) -> nanoocp.Font.Font_FontAspect:
        """Returns text FontAspect"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_AttribBuffer(Graphic3d_Buffer):
    """
    Buffer of vertex attributes.
    This class is intended for advanced usage allowing invalidation of entire buffer content or its
    sub-part.
    """

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_AttribBuffer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def Init(self, theNbElems: int, theAttribs: Graphic3d_Attribute, theNbAttribs: int) -> bool: ...

    @overload
    def Init(self, theNbElems: int, theAttribs: nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_Attribute]) -> bool:
        """Allocates new empty array"""

    def IsMutable(self) -> bool:
        """Return TRUE if data can be invalidated; FALSE by default."""

    def SetMutable(self, theMutable: bool) -> None:
        """Set if data can be invalidated."""

    def IsInterleaved(self) -> bool:
        """Return TRUE for interleaved array; TRUE by default."""

    def SetInterleaved(self, theIsInterleaved: bool) -> None:
        """
        Setup interleaved/non-interleaved array.
        WARNING! Filling non-interleaved buffer should be implemented on user side
        without Graphic3d_Buffer auxiliary methods designed for interleaved data.
        """

    def InvalidatedRange(self) -> Graphic3d_BufferRange:
        """Return invalidated range."""

    def Validate(self) -> None:
        """Reset invalidated range."""

    @overload
    def Invalidate(self) -> None:
        """Invalidate the entire buffer data."""

    @overload
    def Invalidate(self, theAttributeIndex: int) -> None:
        """Invalidate the entire attribute data."""

    @overload
    def Invalidate(self, theAttributeIndex: int, theVertexLower: int, theVertexUpper: int) -> None:
        """
        Invalidate attribute data within specified sub-range (starting from 0).
        """

    @overload
    def Invalidate(self, theVertexLower: int, theVertexUpper: int) -> None:
        """
        Invalidate all attribute data within specified vertex sub-range (starting from 0).
        """

    def invalidate(self, theRange: Graphic3d_BufferRange) -> None:
        """Invalidate specified sub-range of data (as byte offsets)."""

class Graphic3d_BndBox4d:
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None:
        """Creates uninitialized bounding box."""

    @overload
    def __init__(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> None:
        """Creates bounding box of given point."""

    @overload
    def __init__(self, theMinPoint: nanoocp.BVH.BVH_Vec4d, theMaxPoint: nanoocp.BVH.BVH_Vec4d) -> None:
        """Creates bounding box from corner points."""

    @overload
    def __init__(self, theOther: Graphic3d_BndBox4d) -> None: ...

    def Clear(self) -> None:
        """Clears bounding box."""

    def IsValid(self) -> bool:
        """Is bounding box valid?"""

    def Add(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> None:
        """Appends new point to the bounding box."""

    def Combine(self, theBox: Graphic3d_BndBox4d) -> None:
        """Combines bounding box with another one."""

    def CornerMin(self) -> nanoocp.BVH.BVH_Vec4d:
        """Returns minimum point of bounding box."""

    def CornerMax(self) -> nanoocp.BVH.BVH_Vec4d:
        """Returns maximum point of bounding box."""

    def Area(self) -> float:
        """
        Returns surface area of bounding box.
        If the box is degenerated into line, returns the perimeter instead.
        """

    def Size(self) -> nanoocp.BVH.BVH_Vec4d:
        """Returns diagonal of bounding box."""

    @overload
    def Center(self) -> nanoocp.BVH.BVH_Vec4d:
        """Returns center of bounding box."""

    @overload
    def Center(self, theAxis: int) -> float:
        """Returns center of bounding box along the given axis."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

    @overload
    def IsOut(self, theOther: Graphic3d_BndBox4d) -> bool:
        """Checks if the Box is out of the other box."""

    @overload
    def IsOut(self, theMinPoint: nanoocp.BVH.BVH_Vec4d, theMaxPoint: nanoocp.BVH.BVH_Vec4d) -> bool:
        """Checks if the Box is out of the other box defined by two points."""

    @overload
    def IsOut(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> bool:
        """Checks if the Point is out of the box."""

    @overload
    def Contains(self, theOther: Graphic3d_BndBox4d) -> tuple[bool, bool]:
        """Checks if the Box fully contains the other box."""

    @overload
    def Contains(self, theMinPoint: nanoocp.BVH.BVH_Vec4d, theMaxPoint: nanoocp.BVH.BVH_Vec4d) -> tuple[bool, bool]:
        """Checks if the Box is fully contains the other box."""

class Graphic3d_BndBox4f:
    """
    Defines axis aligned bounding box (AABB) based on BVH vectors.
    \\tparam T Numeric data type
    \\tparam N Vector dimension
    """

    @overload
    def __init__(self) -> None:
        """Creates uninitialized bounding box."""

    @overload
    def __init__(self, thePoint: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Creates bounding box of given point."""

    @overload
    def __init__(self, theMinPoint: nanoocp.Quantity.NCollection_Vec4__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Creates bounding box from corner points."""

    @overload
    def __init__(self, theOther: Graphic3d_BndBox4f) -> None: ...

    def Clear(self) -> None:
        """Clears bounding box."""

    def IsValid(self) -> bool:
        """Is bounding box valid?"""

    def Add(self, thePoint: nanoocp.Quantity.NCollection_Vec4__float) -> None:
        """Appends new point to the bounding box."""

    def Combine(self, theBox: Graphic3d_BndBox4f) -> None:
        """Combines bounding box with another one."""

    def CornerMin(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns minimum point of bounding box."""

    def CornerMax(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns maximum point of bounding box."""

    def Area(self) -> float:
        """
        Returns surface area of bounding box.
        If the box is degenerated into line, returns the perimeter instead.
        """

    def Size(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns diagonal of bounding box."""

    @overload
    def Center(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Returns center of bounding box."""

    @overload
    def Center(self, theAxis: int) -> float:
        """Returns center of bounding box along the given axis."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def InitFromJson(self, theSStream: TextIO, theStreamPos: int) -> tuple[bool, int]:
        """Inits the content of me from the stream"""

    @overload
    def IsOut(self, theOther: Graphic3d_BndBox4f) -> bool:
        """Checks if the Box is out of the other box."""

    @overload
    def IsOut(self, theMinPoint: nanoocp.Quantity.NCollection_Vec4__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """Checks if the Box is out of the other box defined by two points."""

    @overload
    def IsOut(self, thePoint: nanoocp.Quantity.NCollection_Vec4__float) -> bool:
        """Checks if the Point is out of the box."""

    @overload
    def Contains(self, theOther: Graphic3d_BndBox4f) -> tuple[bool, bool]:
        """Checks if the Box fully contains the other box."""

    @overload
    def Contains(self, theMinPoint: nanoocp.Quantity.NCollection_Vec4__float, theMaxPoint: nanoocp.Quantity.NCollection_Vec4__float) -> tuple[bool, bool]:
        """Checks if the Box is fully contains the other box."""

class Graphic3d_BvhCStructureSet(nanoocp.BVH.BVH_PrimitiveSet3d):
    """Set of OpenGl_Structures for building BVH tree."""

    @overload
    def __init__(self) -> None:
        """Creates an empty primitive set for BVH clipping."""

    @overload
    def __init__(self, theOther: Graphic3d_BvhCStructureSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Size(self) -> int:
        """Returns total number of structures."""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns AABB of the structure."""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """Calculates center of the AABB along given axis."""

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps structures with the given indices."""

    def Add(self, theStruct: Graphic3d_CStructure) -> bool:
        """
        Adds structure to the set.
        @return true if structure added, otherwise returns false (structure already in the set).
        """

    def Remove(self, theStruct: Graphic3d_CStructure) -> bool:
        """
        Removes the given structure from the set.
        @return true if structure removed, otherwise returns false (structure is not in the set).
        """

    def Clear(self) -> None:
        """Cleans the whole primitive set."""

    def GetStructureById(self, theId: int) -> Graphic3d_CStructure:
        """Returns the structure corresponding to the given ID."""

    def Structures(self) -> "NCollection_IndexedMap<Graphic3d_CStructure const*, NCollection_DefaultHasher<Graphic3d_CStructure const*>>":
        """Access directly a collection of structures."""

class Graphic3d_WorldViewProjState:
    """
    Helper class for keeping reference on world-view-projection state.
    Helpful for synchronizing state of WVP dependent data structures.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theProjectionState: int, theWorldViewState: int, theCamera: nanoocp.Standard.Standard_Transient = None) -> None:
        """
        Constructor for custom projector type.
        @param[in] theProjectionState  the projection state.
        @param[in] theWorldViewState  the world view state.
        @param[in] theCamera  the pointer to the class supplying projection and
        world view matrices (camera).
        """

    @overload
    def __init__(self, theOther: Graphic3d_WorldViewProjState) -> None: ...

    def IsValid(self) -> bool:
        """
        Check state validity.
        @return true if state is set.
        """

    def Reset(self) -> None:
        """Invalidate world view projection state."""

    @overload
    def Initialize(self, theProjectionState: int, theWorldViewState: int, theCamera: nanoocp.Standard.Standard_Transient = None) -> None: ...

    @overload
    def Initialize(self, theCamera: nanoocp.Standard.Standard_Transient = None) -> None:
        """Initialize world view projection state."""

    def ProjectionState(self) -> int:
        """@return projection state counter."""

    def SetProjectionState(self, theValue: int) -> None:
        """
        Python addition: sets the value ProjectionState() returns by reference in C++.
        """

    def WorldViewState(self) -> int:
        """@return world view state counter."""

    def SetWorldViewState(self, theValue: int) -> None:
        """
        Python addition: sets the value WorldViewState() returns by reference in C++.
        """

    def IsProjectionChanged(self, theState: Graphic3d_WorldViewProjState) -> bool:
        """
        Compare projection with other state.
        @return true when the projection of the given camera state differs from this one.
        """

    def IsWorldViewChanged(self, theState: Graphic3d_WorldViewProjState) -> bool:
        """
        Compare world view transformation with other state.
        @return true when the orientation of the given camera state differs from this one.
        """

    def IsChanged(self, theState: Graphic3d_WorldViewProjState) -> bool:
        """
        Compare with other world view projection state.
        @return true when the projection of the given camera state differs from this one.
        """

    def __ne__(self, theOther: Graphic3d_WorldViewProjState) -> bool:
        """
        Compare with other world view projection state.
        @return true if the other projection state is different to this one.
        """

    def __eq__(self, theOther: Graphic3d_WorldViewProjState) -> bool:
        """
        Compare with other world view projection state.
        @return true if the other projection state is equal to this one.
        """

    def DumpJson(self, arg1: int) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_BvhCStructureSetTrsfPers(nanoocp.BVH.BVH_Set__double__3):
    """
    Set of transformation persistent OpenGl_Structure for building BVH tree.
    Provides built-in mechanism to invalidate tree when world view projection state changes.
    Due to frequent invalidation of BVH tree the choice of BVH tree builder is made
    in favor of BVH linear builder (quick rebuild).
    """

    @overload
    def __init__(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Creates an empty primitive set for BVH clipping."""

    @overload
    def __init__(self, theOther: Graphic3d_BvhCStructureSetTrsfPers) -> None: ...

    def Size(self) -> int:
        """Returns total number of structures."""

    def Box(self, theIdx: int) -> nanoocp.Bnd.BVH_Box__double__3:
        """Returns AABB of the structure."""

    def Center(self, theIdx: int, theAxis: int) -> float:
        """Calculates center of the AABB along given axis."""

    def Swap(self, theIdx1: int, theIdx2: int) -> None:
        """Swaps structures with the given indices."""

    def Add(self, theStruct: Graphic3d_CStructure) -> bool:
        """
        Adds structure to the set.
        @return true if structure added, otherwise returns false (structure already in the set).
        """

    def Remove(self, theStruct: Graphic3d_CStructure) -> bool:
        """
        Removes the given structure from the set.
        @return true if structure removed, otherwise returns false (structure is not in the set).
        """

    def Clear(self) -> None:
        """Cleans the whole primitive set."""

    def GetStructureById(self, theId: int) -> Graphic3d_CStructure:
        """Returns the structure corresponding to the given ID."""

    def Structures(self) -> "NCollection_IndexedMap<Graphic3d_CStructure const*, NCollection_DefaultHasher<Graphic3d_CStructure const*>>":
        """Access directly a collection of structures."""

    def MarkDirty(self) -> None:
        """Marks object state as outdated (needs BVH rebuilding)."""

    def BVH(self, theCamera: Graphic3d_Camera | None, theProjectionMatrix: nanoocp.BVH.BVH_Mat4d, theWorldViewMatrix: nanoocp.BVH.BVH_Mat4d, theViewportWidth: int, theViewportHeight: int, theWVPState: Graphic3d_WorldViewProjState) -> BVH_Tree__double__3__BVH_BinaryTree:
        """
        Returns BVH tree for the given world view projection (builds it if necessary).
        """

    def Builder(self) -> nanoocp.BVH.BVH_Builder3d:
        """Returns builder for bottom-level BVH."""

    def SetBuilder(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Assigns builder for bottom-level BVH."""

class Graphic3d_CameraTile:
    """Class defines the area (Tile) inside a view."""

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        Initializes the empty Tile of zero size and lower-left offset orientation.
        Such Tile is considered uninitialized (invalid).
        """

    @overload
    def __init__(self, theOther: Graphic3d_CameraTile) -> None: ...

    def IsValid(self) -> bool:
        """Return true if Tile has been defined."""

    def OffsetLowerLeft(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return offset position from lower-left corner."""

    def Cropped(self) -> Graphic3d_CameraTile:
        """Return the copy cropped by total size"""

    def __eq__(self, theOther: Graphic3d_CameraTile) -> bool:
        """Equality check."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def TotalSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """total size of the View area, in pixels"""

    @TotalSize.setter
    def TotalSize(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

    @property
    def TileSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """size of the Tile, in pixels"""

    @TileSize.setter
    def TileSize(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

    @property
    def Offset(self) -> nanoocp.BVH.BVH_Vec2i:
        """
        the lower-left corner of the Tile relative to the View area (or upper-left if IsTopDown is true), in pixels
        """

    @Offset.setter
    def Offset(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

    @property
    def IsTopDown(self) -> bool:
        """
        indicate the offset coordinate system - lower-left (default) or top-down
        """

    @IsTopDown.setter
    def IsTopDown(self, arg: bool, /) -> None: ...

class Graphic3d_Camera(nanoocp.Standard.Standard_Transient):
    """
    Camera class provides object-oriented approach to setting up projection
    and orientation properties of 3D view.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        Initializes camera with the following properties:
        Eye (0, 0, -2); Center (0, 0, 0); Up (0, 1, 0);
        Type (Orthographic); FOVy (45); Scale (1000); IsStereo(false);
        ZNear (0.001); ZFar (3000.0); Aspect(1);
        ZFocus(1.0); ZFocusType(Relative); IOD(0.05); IODType(Relative)
        """

    @overload
    def __init__(self, theOther: Graphic3d_Camera | None) -> None:
        """
        Copy constructor.
        @param[in] theOther  the camera to copy from.
        """

    @overload
    def __init__(self, theOther: Graphic3d_Camera) -> None: ...

    class Projection(enum.IntEnum):
        """
        Enumerates supported monographic projections.
        - Projection_Orthographic : orthographic projection.
        - Projection_Perspective  : perspective projection.
        - Projection_Stereo       : stereographic projection.
        - Projection_MonoLeftEye  : mono projection for stereo left eye.
        - Projection_MonoRightEye : mono projection for stereo right eye.
        """

        Projection_Orthographic = 0

        Projection_Perspective = 1

        Projection_Stereo = 2

        Projection_MonoLeftEye = 3

        Projection_MonoRightEye = 4

    Projection_Orthographic: Graphic3d_Camera.Projection = Projection.Projection_Orthographic

    Projection_Perspective: Graphic3d_Camera.Projection = Projection.Projection_Perspective

    Projection_Stereo: Graphic3d_Camera.Projection = Projection.Projection_Stereo

    Projection_MonoLeftEye: Graphic3d_Camera.Projection = Projection.Projection_MonoLeftEye

    Projection_MonoRightEye: Graphic3d_Camera.Projection = Projection.Projection_MonoRightEye

    class FocusType(enum.IntEnum):
        """
        Enumerates approaches to define stereographic focus.
        - FocusType_Absolute : focus is specified as absolute value.
        - FocusType_Relative : focus is specified relative to
        (as coefficient of) camera focal length.
        """

        FocusType_Absolute = 0

        FocusType_Relative = 1

    FocusType_Absolute: Graphic3d_Camera.FocusType = FocusType.FocusType_Absolute

    FocusType_Relative: Graphic3d_Camera.FocusType = FocusType.FocusType_Relative

    class IODType(enum.IntEnum):
        """
        Enumerates approaches to define Intraocular distance.
        - IODType_Absolute : Intraocular distance is defined as absolute value.
        - IODType_Relative : Intraocular distance is defined relative to
        (as coefficient of) camera focal length.
        """

        IODType_Absolute = 0

        IODType_Relative = 1

    IODType_Absolute: Graphic3d_Camera.IODType = IODType.IODType_Absolute

    IODType_Relative: Graphic3d_Camera.IODType = IODType.IODType_Relative

    FrustumVert_LeftBottomNear: int = 0

    FrustumVert_LeftBottomFar: int = 1

    FrustumVert_LeftTopNear: int = 2

    FrustumVert_LeftTopFar: int = 3

    FrustumVert_RightBottomNear: int = 4

    FrustumVert_RightBottomFar: int = 5

    FrustumVert_RightTopNear: int = 6

    FrustumVert_RightTopFar: int = 7

    FrustumVerticesNB: int = 8

    @staticmethod
    def Interpolate(theStart: Graphic3d_Camera | None, theEnd: Graphic3d_Camera | None, theT: float) -> Graphic3d_Camera:
        """
        Linear interpolation tool for camera orientation and position.
        This tool interpolates camera parameters scale, eye, center, rotation (up and direction
        vectors) independently.
        @sa NCollection_Lerp<occ::handle<Graphic3d_Camera>>

        Eye/Center interpolation is performed through defining an anchor point in-between Center and
        Eye. The anchor position is defined as point near to the camera point which has smaller
        translation part. The main idea is to keep the distance between Center and Eye (which will
        change if Center and Eye translation will be interpolated independently). E.g.:
        - When both Center and Eye are moved at the same vector -> both will be just translated by
        straight line;
        - When Center is not moved -> camera Eye will move around Center through arc;
        - When Eye    is not moved -> camera Center will move around Eye through arc;
        - When both Center and Eye are move by different vectors -> transformation will be something
        in between,
        and will try interpolate linearly the distance between Center and Eye.

        This transformation might be not in line with user expectations.
        In this case, application might define intermediate camera positions for interpolation or
        implement own interpolation logic.

        @param[in] theStart   initial camera position
        @param[in] theEnd     final   camera position
        @param[in] theT       step between initial and final positions within [0,1] range
        @param[out] theCamera  interpolation result
        """

    def CopyMappingData(self, theOtherCamera: Graphic3d_Camera | None) -> None:
        """Initialize mapping related parameters from other camera handle."""

    def CopyOrientationData(self, theOtherCamera: Graphic3d_Camera | None) -> None:
        """Initialize orientation related parameters from other camera handle."""

    def Copy(self, theOther: Graphic3d_Camera | None) -> None:
        """
        Copy properties of another camera.
        @param[in] theOther  the camera to copy from.
        """

    def Direction(self) -> nanoocp.gp.gp_Dir:
        """
        Get camera look direction.
        @return camera look direction.
        """

    def SetDirectionFromEye(self, theDir: nanoocp.gp.gp_Dir) -> None:
        """
        Sets camera look direction preserving the current Eye() position.
        WARNING! This method does NOT verify that the current Up() vector is orthogonal to the new
        Direction.
        @param[in] theDir  the direction.
        """

    def SetDirection(self, theDir: nanoocp.gp.gp_Dir) -> None:
        """
        Sets camera look direction and computes the new Eye position relative to current Center.
        WARNING! This method does NOT verify that the current Up() vector is orthogonal to the new
        Direction.
        @param[in] theDir  the direction.
        """

    def Up(self) -> nanoocp.gp.gp_Dir:
        """
        Get camera Up direction vector.
        @return Camera's Up direction vector.
        """

    def SetUp(self, theUp: nanoocp.gp.gp_Dir) -> None:
        """
        Sets camera Up direction vector, orthogonal to camera direction.
        WARNING! This method does NOT verify that the new Up vector is orthogonal to the current
        Direction().
        @param[in] theUp  the Up direction vector.
        @sa OrthogonalizeUp().
        """

    def OrthogonalizeUp(self) -> None:
        """Orthogonalize up direction vector."""

    def OrthogonalizedUp(self) -> nanoocp.gp.gp_Dir:
        """Return a copy of orthogonalized up direction vector."""

    def SideRight(self) -> nanoocp.gp.gp_Dir:
        """Right side direction."""

    def Eye(self) -> nanoocp.gp.gp_Pnt:
        """
        Get camera Eye position.
        @return camera eye location.
        """

    def MoveEyeTo(self, theEye: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets camera Eye position.
        Unlike SetEye(), this method only changes Eye point and preserves camera direction.
        @param[in] theEye  the location of camera's Eye.
        @sa SetEye()
        """

    def SetEyeAndCenter(self, theEye: nanoocp.gp.gp_Pnt, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets camera Eye and Center positions.
        @param[in] theEye     the location of camera's Eye
        @param[in] theCenter  the location of camera's Center
        """

    def SetEye(self, theEye: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets camera Eye position.
        WARNING! For backward compatibility reasons, this method also changes view direction,
        so that the new direction is computed from new Eye position to old Center position.
        @param[in] theEye  the location of camera's Eye.
        @sa MoveEyeTo(), SetEyeAndCenter()
        """

    def Center(self) -> nanoocp.gp.gp_Pnt:
        """
        Get Center of the camera, e.g. the point where camera looks at.
        This point is computed as Eye() translated along Direction() at Distance().
        @return the point where the camera looks at.
        """

    def SetCenter(self, theCenter: nanoocp.gp.gp_Pnt) -> None:
        """
        Sets Center of the camera, e.g. the point where camera looks at.
        This methods changes camera direction, so that the new direction is computed
        from current Eye position to specified Center position.
        @param[in] theCenter  the point where the camera looks at.
        """

    def Distance(self) -> float:
        """
        Get distance of Eye from camera Center.
        @return the distance.
        """

    def SetDistance(self, theDistance: float) -> None:
        """
        Set distance of Eye from camera Center.
        @param[in] theDistance  the distance.
        """

    def Scale(self) -> float:
        """
        Get camera scale.
        @return camera scale factor.
        """

    def SetScale(self, theScale: float) -> None:
        """
        Sets camera scale. For orthographic projection the scale factor
        corresponds to parallel scale of view mapping (i.e. size
        of viewport). For perspective camera scale is converted to
        distance. The scale specifies equal size of the view projection in
        both dimensions assuming that the aspect is 1.0. The projection height
        and width are specified with the scale and correspondingly multiplied
        by the aspect.
        @param[in] theScale  the scale factor.
        """

    def AxialScale(self) -> nanoocp.gp.gp_XYZ:
        """
        Get camera axial scale.
        @return Camera's axial scale.
        """

    def SetAxialScale(self, theAxialScale: nanoocp.gp.gp_XYZ) -> None:
        """
        Set camera axial scale.
        @param[in] theAxialScale  the axial scale vector.
        """

    def SetProjectionType(self, theProjection: Graphic3d_Camera.Projection) -> None:
        """
        Change camera projection type.
        When switching to perspective projection from orthographic one,
        the ZNear and ZFar are reset to default values (0.001, 3000.0)
        if less than 0.0.
        @param[in] theProjection the camera projection type.
        """

    def ProjectionType(self) -> Graphic3d_Camera.Projection:
        """@return camera projection type."""

    def IsOrthographic(self) -> bool:
        """
        Check that the camera projection is orthographic.
        @return boolean flag that indicates whether the camera's projection is
        orthographic or not.
        """

    def IsStereo(self) -> bool:
        """
        Check whether the camera projection is stereo.
        Please note that stereo rendering is now implemented with support of
        Quad buffering.
        @return boolean flag indicating whether the stereographic L/R projection
        is chosen.
        """

    def SetFOVy(self, theFOVy: float) -> None:
        """
        Set Field Of View (FOV) in y axis for perspective projection.
        Field of View in x axis is automatically scaled from view aspect ratio.
        @param[in] theFOVy  the FOV in degrees.
        """

    def FOVy(self) -> float:
        """
        Get Field Of View (FOV) in y axis.
        @return the FOV value in degrees.
        """

    def FOVx(self) -> float:
        """
        Get Field Of View (FOV) in x axis.
        @return the FOV value in degrees.
        """

    def FOV2d(self) -> float:
        """
        Get Field Of View (FOV) restriction for 2D on-screen elements; 180 degrees by default.
        When 2D FOV is smaller than FOVy or FOVx, 2D elements defined within offset from view corner
        will be extended to fit into specified 2D FOV.
        This can be useful to make 2D elements sharply visible, like in case of HMD normally having
        extra large FOVy.
        """

    def SetFOV2d(self, theFOV: float) -> None:
        """Set Field Of View (FOV) restriction for 2D on-screen elements."""

    def FitMinMax(self, theBox: nanoocp.Bnd.Bnd_Box, theResolution: float, theToEnlargeIfLine: bool) -> bool:
        """Adjust camera to fit in specified AABB."""

    def ZFitAll__float__float(self, theScaleFactor: float, theMinMax: nanoocp.Bnd.Bnd_Box, theGraphicBB: nanoocp.Bnd.Bnd_Box) -> tuple[bool, float, float]:
        """
        ZFitAll__float__float: the C++ overload ZFitAll(const double, const Bnd_Box &, const Bnd_Box &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Estimate Z-min and Z-max planes of projection volume to match the
        displayed objects. The methods ensures that view volume will
        be close by depth range to the displayed objects. Fitting assumes that
        for orthogonal projection the view volume contains the displayed objects
        completely. For zoomed perspective view, the view volume is adjusted such
        that it contains the objects or their parts, located in front of the camera.
        @param[in] theScaleFactor the scale factor for Z-range.
        The range between Z-min, Z-max projection volume planes
        evaluated by z fitting method will be scaled using this coefficient.
        Program error exception is thrown if negative or zero value is passed.
        @param[in] theMinMax applicative min max boundaries.
        @param[in] theGraphicBB real graphical boundaries (not accounting infinite flag).
        """

    def ZFitAll(self, theScaleFactor: float, theMinMax: nanoocp.Bnd.Bnd_Box, theGraphicBB: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Change Z-min and Z-max planes of projection volume to match the displayed objects.
        """

    def SetZRange(self, theZNear: float, theZFar: float) -> None:
        """
        Change the Near and Far Z-clipping plane positions.
        For orthographic projection, theZNear, theZFar can be negative or positive.
        For perspective projection, only positive values are allowed.
        Program error exception is raised if non-positive values are
        specified for perspective projection or theZNear >= theZFar.
        @param[in] theZNear  the distance of the plane from the Eye.
        @param[in] theZFar  the distance of the plane from the Eye.
        """

    def ZNear(self) -> float:
        """
        Get the Near Z-clipping plane position.
        @return the distance of the plane from the Eye.
        """

    def ZFar(self) -> float:
        """
        Get the Far Z-clipping plane position.
        @return the distance of the plane from the Eye.
        """

    def IsZeroToOneDepth(self) -> bool:
        """
        Return TRUE if camera should calculate projection matrix for [0, 1] depth range or for [-1, 1]
        range. FALSE by default.
        """

    def SetZeroToOneDepth(self, theIsZeroToOne: bool) -> None:
        """Set using [0, 1] depth range or [-1, 1] range."""

    def SetAspect(self, theAspect: float) -> None:
        """
        Changes width / height display ratio.
        @param[in] theAspect  the display ratio.
        """

    def Aspect(self) -> float:
        """
        Get camera display ratio.
        @return display ratio.
        """

    def SetZFocus(self, theType: Graphic3d_Camera.FocusType, theZFocus: float) -> None:
        """
        Sets stereographic focus distance.
        @param[in] theType  the focus definition type. Focus can be defined
        as absolute value or relatively to (as coefficient of) coefficient of
        camera focal length.
        @param[in] theZFocus  the focus absolute value or coefficient depending
        on the passed definition type.
        """

    def ZFocus(self) -> float:
        """
        Get stereographic focus value.
        @return absolute or relative stereographic focus value
        depending on its definition type.
        """

    def ZFocusType(self) -> Graphic3d_Camera.FocusType:
        """
        Get stereographic focus definition type.
        @return definition type used for stereographic focus.
        """

    def SetIOD(self, theType: Graphic3d_Camera.IODType, theIOD: float) -> None:
        """
        Sets Intraocular distance.
        @param[in] theType  the IOD definition type. IOD can be defined as
        absolute value or relatively to (as coefficient of) camera focal length.
        @param[in] theIOD  the Intraocular distance.
        """

    def IOD(self) -> float:
        """
        Get Intraocular distance value.
        @return absolute or relative IOD value depending on its definition type.
        """

    def GetIODType(self) -> Graphic3d_Camera.IODType:
        """
        Get Intraocular distance definition type.
        @return definition type used for Intraocular distance.
        """

    def Tile(self) -> Graphic3d_CameraTile:
        """Get current tile."""

    def SetTile(self, theTile: Graphic3d_CameraTile) -> None:
        """
        Sets the Tile defining the drawing sub-area within View.
        Note that tile defining a region outside the view boundaries is also valid - use method
        Graphic3d_CameraTile::Cropped() to assign a cropped copy.
        @param theTile tile definition
        """

    def SetIdentityOrientation(self) -> None:
        """
        Sets camera parameters to make current orientation matrix identity one.
        """

    def Transform(self, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Transform orientation components of the camera:
        Eye, Up and Center points.
        @param[in] theTrsf  the transformation to apply.
        """

    @overload
    def ViewDimensions(self) -> nanoocp.gp.gp_XYZ:
        """
        Calculate view plane size at center (target) point
        and distance between ZFar and ZNear planes.
        @return values in form of gp_Pnt (Width, Height, Depth).
        """

    @overload
    def ViewDimensions(self, theZValue: float) -> nanoocp.gp.gp_XYZ:
        """
        Calculate view plane size at center point with specified Z offset
        and distance between ZFar and ZNear planes.
        @param[in] theZValue  the distance from the eye in eye-to-center direction
        @return values in form of gp_Pnt (Width, Height, Depth).
        """

    def NDC2dOffsetX(self) -> float:
        """
        Return offset to the view corner in NDC space within dimension X for 2d on-screen elements,
        which is normally 0.5. Can be clamped when FOVx exceeds FOV2d.
        """

    def NDC2dOffsetY(self) -> float:
        """
        Return offset to the view corner in NDC space within dimension X for 2d on-screen elements,
        which is normally 0.5. Can be clamped when FOVy exceeds FOV2d.
        """

    def Frustum(self, theLeft: nanoocp.gp.gp_Pln, theRight: nanoocp.gp.gp_Pln, theBottom: nanoocp.gp.gp_Pln, theTop: nanoocp.gp.gp_Pln, theNear: nanoocp.gp.gp_Pln, theFar: nanoocp.gp.gp_Pln) -> None:
        """
        Calculate WCS frustum planes for the camera projection volume.
        Frustum is a convex volume determined by six planes directing
        inwards.
        The frustum planes are usually used as inputs for camera algorithms.
        Thus, if any changes to projection matrix calculation are necessary,
        the frustum planes calculation should be also touched.
        @param[out] theLeft  the frustum plane for left side of view.
        @param[out] theRight  the frustum plane for right side of view.
        @param[out] theBottom  the frustum plane for bottom side of view.
        @param[out] theTop  the frustum plane for top side of view.
        @param[out] theNear  the frustum plane for near side of view.
        @param[out] theFar  the frustum plane for far side of view.
        """

    def Project(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Project point from world coordinate space to
        normalized device coordinates (mapping).
        @param[in] thePnt  the 3D point in WCS.
        @return mapped point in NDC.
        """

    def UnProject(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Unproject point from normalized device coordinates
        to world coordinate space.
        @param[in] thePnt  the NDC point.
        @return 3D point in WCS.
        """

    def ConvertView2Proj(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Convert point from view coordinate space to
        projection coordinate space.
        @param[in] thePnt  the point in VCS.
        @return point in NDC.
        """

    def ConvertProj2View(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Convert point from projection coordinate space
        to view coordinate space.
        @param[in] thePnt  the point in NDC.
        @return point in VCS.
        """

    def ConvertWorld2View(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Convert point from world coordinate space to
        view coordinate space.
        @param[in] thePnt  the 3D point in WCS.
        @return point in VCS.
        """

    def ConvertView2World(self, thePnt: nanoocp.gp.gp_Pnt) -> nanoocp.gp.gp_Pnt:
        """
        Convert point from view coordinate space to
        world coordinates.
        @param[in] thePnt  the 3D point in VCS.
        @return point in WCS.
        """

    def WorldViewProjState(self) -> Graphic3d_WorldViewProjState:
        """@return projection modification state of the camera."""

    def ProjectionState(self) -> int:
        """Returns modification state of camera projection matrix"""

    def WorldViewState(self) -> int:
        """Returns modification state of camera world view transformation matrix."""

    def OrientationMatrix(self) -> nanoocp.BVH.BVH_Mat4d:
        """
        Get orientation matrix.
        @return camera orientation matrix.
        """

    def OrientationMatrixF(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        Get orientation matrix of float precision.
        @return camera orientation matrix.
        """

    def ProjectionMatrix(self) -> nanoocp.BVH.BVH_Mat4d:
        """
        Get monographic or middle point projection matrix used for monographic
        rendering and for point projection / unprojection.
        @return monographic projection matrix.
        """

    def ProjectionMatrixF(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        Get monographic or middle point projection matrix of float precision used for
        monographic rendering and for point projection / unprojection.
        @return monographic projection matrix.
        """

    def ProjectionStereoLeft(self) -> nanoocp.BVH.BVH_Mat4d:
        """
        @return stereographic matrix computed for left eye. Please note
        that this method is used for rendering for <i>Projection_Stereo</i>.
        """

    def ProjectionStereoLeftF(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        @return stereographic matrix of float precision computed for left eye.
        Please note that this method is used for rendering for <i>Projection_Stereo</i>.
        """

    def ProjectionStereoRight(self) -> nanoocp.BVH.BVH_Mat4d:
        """
        @return stereographic matrix computed for right eye. Please note
        that this method is used for rendering for <i>Projection_Stereo</i>.
        """

    def ProjectionStereoRightF(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        @return stereographic matrix of float precision computed for right eye.
        Please note that this method is used for rendering for <i>Projection_Stereo</i>.
        """

    def InvalidateProjection(self) -> None:
        """
        Invalidate state of projection matrix.
        The matrix will be updated on request.
        """

    def InvalidateOrientation(self) -> None:
        """
        Invalidate orientation matrix.
        The matrix will be updated on request.
        """

    def StereoProjection(self, theProjL: nanoocp.BVH.BVH_Mat4d, theHeadToEyeL: nanoocp.BVH.BVH_Mat4d, theProjR: nanoocp.BVH.BVH_Mat4d, theHeadToEyeR: nanoocp.BVH.BVH_Mat4d) -> None:
        """
        Get stereo projection matrices.
        @param[out] theProjL       left  eye projection matrix
        @param[out] theHeadToEyeL  left  head to eye translation matrix
        @param[out] theProjR       right eye projection matrix
        @param[out] theHeadToEyeR  right head to eye translation matrix
        """

    def StereoProjectionF(self, theProjL: nanoocp.BVH.BVH_Mat4f, theHeadToEyeL: nanoocp.BVH.BVH_Mat4f, theProjR: nanoocp.BVH.BVH_Mat4f, theHeadToEyeR: nanoocp.BVH.BVH_Mat4f) -> None:
        """
        Get stereo projection matrices.
        @param[out] theProjL       left  eye projection matrix
        @param[out] theHeadToEyeL  left  head to eye translation matrix
        @param[out] theProjR       right eye projection matrix
        @param[out] theHeadToEyeR  right head to eye translation matrix
        """

    def ResetCustomProjection(self) -> None:
        """Unset all custom frustums and projection matrices."""

    def IsCustomStereoFrustum(self) -> bool:
        """Return TRUE if custom stereo frustums are set."""

    def SetCustomStereoFrustums(self, theFrustumL: "Aspect_FrustumLRBT<double>", theFrustumR: "Aspect_FrustumLRBT<double>") -> None:
        """
        Set custom stereo frustums.
        These can be retrieved from APIs like OpenVR.
        """

    def IsCustomStereoProjection(self) -> bool:
        """Return TRUE if custom stereo projection matrices are set."""

    def SetCustomStereoProjection(self, theProjL: nanoocp.BVH.BVH_Mat4d, theHeadToEyeL: nanoocp.BVH.BVH_Mat4d, theProjR: nanoocp.BVH.BVH_Mat4d, theHeadToEyeR: nanoocp.BVH.BVH_Mat4d) -> None:
        """
        Set custom stereo projection matrices.
        @param[in] theProjL       left  eye projection matrix
        @param[in] theHeadToEyeL  left  head to eye translation matrix
        @param[in] theProjR       right eye projection matrix
        @param[in] theHeadToEyeR  right head to eye translation matrix
        """

    def IsCustomMonoProjection(self) -> bool:
        """Return TRUE if custom projection matrix is set."""

    def SetCustomMonoProjection(self, theProj: nanoocp.BVH.BVH_Mat4d) -> None:
        """Set custom projection matrix."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def FrustumPoints(self, thePoints: nanoocp.NCollection.NCollection_Array1[nanoocp.BVH.BVH_Vec3d], theModelWorld: nanoocp.BVH.BVH_Mat4d = ...) -> None:
        """
        Fill array of current view frustum corners.
        The size of this array is equal to FrustumVerticesNB.
        The order of vertices is as defined in FrustumVert_* enumeration.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_CLight(nanoocp.Standard.Standard_Transient):
    """
    Generic light source definition.
    This class defines arbitrary light source - see Graphic3d_TypeOfLightSource enumeration.
    Some parameters are applicable only to particular light type;
    calling methods unrelated to current type will throw an exception.
    """

    def __init__(self, theType: Graphic3d_TypeOfLightSource) -> None:
        """
        Empty constructor, which should be followed by light source properties configuration.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CopyFrom(self, theLight: Graphic3d_CLight | None) -> None:
        """Copy parameters from another light source excluding source type."""

    def Type(self) -> Graphic3d_TypeOfLightSource:
        """
        Returns the Type of the Light, cannot be changed after object construction.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns light source name; empty string by default."""

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets light source name."""

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns the color of the light source; WHITE by default."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Defines the color of a light source by giving the basic color."""

    def IsEnabled(self) -> bool:
        """
        Check that the light source is turned on; TRUE by default.
        This flag affects all occurrences of light sources, where it was registered and activated;
        so that it is possible defining an active light in View which is actually in disabled state.
        """

    def SetEnabled(self, theIsOn: bool) -> None:
        """
        Change enabled state of the light state.
        This call does not remove or deactivate light source in Views/Viewers;
        instead it turns it OFF so that it just have no effect.
        """

    def ToCastShadows(self) -> bool:
        """
        Return TRUE if shadow casting is enabled; FALSE by default.
        Has no effect in Ray-Tracing rendering mode.
        """

    def SetCastShadows(self, theToCast: bool) -> None:
        """Enable/disable shadow casting."""

    def IsHeadlight(self) -> bool:
        """
        Returns true if the light is a headlight; FALSE by default.
        Headlight flag means that light position/direction are defined not in a World coordinate
        system, but relative to the camera orientation.
        """

    def Headlight(self) -> bool:
        """Alias for IsHeadlight()."""

    def SetHeadlight(self, theValue: bool) -> None:
        """Setup headlight flag."""

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """Returns location of positional/spot light; (0, 0, 0) by default."""

    @overload
    def SetPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None: ...

    @overload
    def SetPosition(self, theX: float, theY: float, theZ: float) -> None:
        """Setup location of positional/spot light."""

    def Position__float__float__float(self) -> tuple[float, float, float]:
        """
        Position__float__float__float: the C++ overload Position(double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns location of positional/spot light.
        """

    def ConstAttenuation(self) -> float:
        """
        Returns constant attenuation factor of positional/spot light source; 1.0f by default.
        Distance attenuation factors of reducing positional/spot light intensity depending on the
        distance from its position:
        @code
        float anAttenuation = 1.0 / (ConstAttenuation() + LinearAttenuation() * theDistance +
        QuadraticAttenuation() * theDistance * theDistance);
        @endcode
        """

    def LinearAttenuation(self) -> float:
        """
        Returns linear attenuation factor of positional/spot light source; 0.0 by default.
        Distance attenuation factors of reducing positional/spot light intensity depending on the
        distance from its position:
        @code
        float anAttenuation = 1.0 / (ConstAttenuation() + LinearAttenuation() * theDistance +
        QuadraticAttenuation() * theDistance * theDistance);
        @endcode
        """

    def Attenuation(self) -> tuple[float, float]:
        """Returns the attenuation factors."""

    def SetAttenuation(self, theConstAttenuation: float, theLinearAttenuation: float) -> None:
        """
        Defines the coefficients of attenuation; values should be >= 0.0 and their summ should not be
        equal to 0.
        """

    def Direction(self) -> nanoocp.gp.gp_Dir:
        """Returns direction of directional/spot light."""

    @overload
    def SetDirection(self, theDir: nanoocp.gp.gp_Dir) -> None: ...

    @overload
    def SetDirection(self, theVx: float, theVy: float, theVz: float) -> None:
        """Sets direction of directional/spot light."""

    def Direction__float__float__float(self) -> tuple[float, float, float]:
        """
        Direction__float__float__float: the C++ overload Direction(double &, double &, double &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Returns the theVx, theVy, theVz direction of the light source.
        """

    def DisplayPosition(self) -> nanoocp.gp.gp_Pnt:
        """
        Returns location of positional/spot/directional light, which is the same as returned by
        Position().
        """

    def SetDisplayPosition(self, thePosition: nanoocp.gp.gp_Pnt) -> None:
        """
        Setup location of positional/spot/directional light,
        which is the same as SetPosition() but allows directional light source
        (technically having no position, but this point can be used for displaying light source
        presentation).
        """

    def Angle(self) -> float:
        """
        Returns an angle in radians of the cone created by the spot; 30 degrees by default.
        """

    def SetAngle(self, theAngle: float) -> None:
        """
        Angle in radians of the cone created by the spot, should be within range (0.0, M_PI).
        """

    def Concentration(self) -> float:
        """
        Returns intensity distribution of the spot light, within [0.0, 1.0] range; 1.0 by default.
        This coefficient should be converted into spotlight exponent within [0.0, 128.0] range:
        @code
        float aSpotExponent = Concentration() * 128.0;
        anAttenuation *= pow (aCosA, aSpotExponent);"
        @endcode
        The concentration factor determines the dispersion of the light on the surface, the default
        value (1.0) corresponds to a minimum of dispersion.
        """

    def SetConcentration(self, theConcentration: float) -> None:
        """
        Defines the coefficient of concentration; value should be within range [0.0, 1.0].
        """

    def Intensity(self) -> float:
        """Returns the intensity of light source; 1.0 by default."""

    def SetIntensity(self, theValue: float) -> None:
        """Modifies the intensity of light source, which should be > 0.0."""

    def Smoothness(self) -> float:
        """
        Returns the smoothness of light source (either smoothing angle for directional light or
        smoothing radius in case of positional light); 0.0 by default.
        """

    def SetSmoothRadius(self, theValue: float) -> None:
        """
        Modifies the smoothing radius of positional/spot light; should be >= 0.0.
        """

    def SetSmoothAngle(self, theValue: float) -> None:
        """
        Modifies the smoothing angle (in radians) of directional light source; should be within range
        [0.0, M_PI/2].
        """

    def HasRange(self) -> bool:
        """Returns TRUE if maximum distance of point light source is defined."""

    def Range(self) -> float:
        """
        Returns maximum distance on which point light source affects to objects and is considered
        during illumination calculations. 0.0 means disabling range considering at all without any
        distance limits. Has sense only for point light sources (positional and spot).
        """

    def SetRange(self, theValue: float) -> None:
        """
        Modifies maximum distance on which point light source affects to objects and is considered
        during illumination calculations. Positional and spot lights are only point light sources. 0.0
        means disabling range considering at all without any distance limits.
        """

    def GetId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return light resource identifier string"""

    def PackedParams(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """Packed light parameters."""

    def PackedColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Returns the color of the light source with dummy Alpha component, which should be ignored.
        """

    def PackedDirectionRange(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Returns direction of directional/spot light and range for positional/spot light in alpha
        channel.
        """

    def PackedDirection(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Returns direction of directional/spot light."""

    def Revision(self) -> int:
        """@return modification counter"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_ClipPlane(nanoocp.Standard.Standard_Transient):
    """
    Container for properties describing either a Clipping halfspace (single Clipping Plane),
    or a chain of Clipping Planes defining logical AND (conjunction) operation.
    The plane equation is specified in "world" coordinate system.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        Initializes clip plane container with the following properties:
        - Equation (0.0, 0.0, 1.0, 0)
        - IsOn (True),
        - IsCapping (False),
        - Material (Graphic3d_NameOfMaterial_DEFAULT),
        - Texture (NULL),
        - HatchStyle (Aspect_HS_HORIZONTAL),
        - IsHatchOn (False)
        """

    @overload
    def __init__(self, theOther: Graphic3d_ClipPlane) -> None:
        """
        Copy constructor.
        @param[in] theOther  the copied plane.
        """

    @overload
    def __init__(self, theEquation: nanoocp.BVH.BVH_Vec4d) -> None:
        """
        Construct clip plane for the passed equation.
        By default the plane is on, capping is turned off.
        @param[in] theEquation  the plane equation.
        """

    @overload
    def __init__(self, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Construct clip plane from the passed geometrical definition.
        By default the plane is on, capping is turned off.
        @param[in] thePlane  the plane.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    def SetEquation(self, thePlane: nanoocp.gp.gp_Pln) -> None:
        """
        Set plane equation by its geometrical definition.
        The equation is specified in "world" coordinate system.
        @param[in] thePlane  the plane.
        """

    @overload
    def SetEquation(self, theEquation: nanoocp.BVH.BVH_Vec4d) -> None:
        """
        Set 4-component equation vector for clipping plane.
        The equation is specified in "world" coordinate system.
        @param[in] theEquation  the XYZW (or "ABCD") equation vector.
        """

    def GetEquation(self) -> nanoocp.BVH.BVH_Vec4d:
        """
        Get 4-component equation vector for clipping plane.
        @return clipping plane equation vector.
        """

    def ReversedEquation(self) -> nanoocp.BVH.BVH_Vec4d:
        """
        Get 4-component equation vector for clipping plane.
        @return clipping plane equation vector.
        """

    def IsOn(self) -> bool:
        """
        Check that the clipping plane is turned on.
        @return boolean flag indicating whether the plane is in on or off state.
        """

    def SetOn(self, theIsOn: bool) -> None:
        """
        Change state of the clipping plane.
        @param[in] theIsOn  the flag specifying whether the graphic driver
        clipping by this plane should be turned on or off.
        """

    def SetCapping(self, theIsOn: bool) -> None:
        """
        Change state of capping surface rendering.
        @param[in] theIsOn  the flag specifying whether the graphic driver should
        perform rendering of capping surface produced by this plane. The graphic
        driver produces this surface for convex graphics by means of stencil-test
        and multi-pass rendering.
        """

    def IsCapping(self) -> bool:
        """
        Check state of capping surface rendering.
        @return true (turned on) or false depending on the state.
        """

    def ToPlane(self) -> nanoocp.gp.gp_Pln:
        """
        Get geometrical definition.
        @return geometrical definition of clipping plane
        """

    def Clone(self) -> Graphic3d_ClipPlane:
        """
        Clone plane. Virtual method to simplify copying procedure if plane
        class is redefined at application level to add specific fields to it
        e.g. id, name, etc.
        @return new instance of clipping plane with same properties and attributes.
        """

    def IsChain(self) -> bool:
        """
        Return TRUE if this item defines a conjunction (logical AND) between a set of Planes.
        Graphic3d_ClipPlane item defines either a Clipping halfspace (single Clipping Plane)
        or a Clipping volume defined by a logical AND (conjunction) operation between a set of Planes
        defined as a Chain (so that the volume cuts a space only in case if check fails for ALL Planes
        in the Chain).

        Note that Graphic3d_ClipPlane item cannot:
        - Define a Chain with logical OR (disjunction) operation;
        this should be done through Graphic3d_SequenceOfHClipPlane.
        - Define nested Chains.
        - Disable Chain items; only entire Chain can be disabled (by disabled a head of Chain).

        The head of a Chain defines all visual properties of the Chain,
        so that Graphic3d_ClipPlane of next items in a Chain merely defines only geometrical
        definition of the plane.
        """

    def ChainPreviousPlane(self) -> Graphic3d_ClipPlane:
        """
        Return the previous plane in a Chain of Planes defining logical AND operation,
        or NULL if there is no Chain or it is a first element in Chain.
        When clipping is defined by a Chain of Planes,
        it cuts a space only in case if check fails for all Planes in Chain.
        """

    def ChainNextPlane(self) -> Graphic3d_ClipPlane:
        """
        Return the next plane in a Chain of Planes defining logical AND operation,
        or NULL if there is no chain or it is a last element in chain.
        """

    def NbChainNextPlanes(self) -> int:
        """
        Return the number of chains in forward direction (including this item, so it is always >= 1).
        For a head of Chain - returns the length of entire Chain.
        """

    def SetChainNextPlane(self, thePlane: Graphic3d_ClipPlane | None) -> None:
        """
        Set the next plane in a Chain of Planes.
        This operation also updates relationship between chains (Previous/Next items),
        so that the previously set Next plane is cut off.
        """

    def CappingColor(self) -> nanoocp.Quantity.Quantity_Color:
        """Return color for rendering capping surface."""

    def SetCappingColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Set color for rendering capping surface."""

    def SetCappingMaterial(self, theMat: Graphic3d_MaterialAspect) -> None:
        """
        Set material for rendering capping surface.
        @param[in] theMat  the material.
        """

    def CappingMaterial(self) -> Graphic3d_MaterialAspect:
        """@return capping material."""

    def SetCappingTexture(self, theTexture: Graphic3d_TextureMap | None) -> None:
        """
        Set texture to be applied on capping surface.
        @param[in] theTexture  the texture.
        """

    def CappingTexture(self) -> Graphic3d_TextureMap:
        """@return capping texture map."""

    def SetCappingHatch(self, theStyle: nanoocp.Aspect.Aspect_HatchStyle) -> None:
        """
        Set hatch style (stipple) and turn hatching on.
        @param[in] theStyle  the hatch style.
        """

    def CappingHatch(self) -> nanoocp.Aspect.Aspect_HatchStyle:
        """@return hatching style."""

    def SetCappingCustomHatch(self, theStyle: Graphic3d_HatchStyle | None) -> None:
        """
        Set custom hatch style (stipple) and turn hatching on.
        @param[in] theStyle  the hatch pattern.
        """

    def CappingCustomHatch(self) -> Graphic3d_HatchStyle:
        """@return hatching style."""

    def SetCappingHatchOn(self) -> None:
        """Turn on hatching."""

    def SetCappingHatchOff(self) -> None:
        """Turn off hatching."""

    def IsHatchOn(self) -> bool:
        """@return True if hatching mask is turned on."""

    def GetId(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        This ID is used for managing associated resources in graphical driver.
        The clip plane can be assigned within a range of IO which can be
        displayed in separate OpenGl contexts. For each of the context an associated
        OpenGl resource for graphical aspects should be created and kept.
        The resources are stored in graphical driver for each of individual groups
        of shared context under the clip plane identifier.
        @return clip plane resource identifier string.
        """

    def CappingAspect(self) -> Graphic3d_AspectFillArea3d:
        """
        Return capping aspect.
        @return capping surface rendering aspect.
        """

    def SetCappingAspect(self, theAspect: Graphic3d_AspectFillArea3d | None) -> None:
        """Assign capping aspect."""

    def ToUseObjectMaterial(self) -> bool:
        """
        Flag indicating whether material for capping plane should be taken from object.
        Default value: FALSE (use dedicated capping plane material).
        """

    def SetUseObjectMaterial(self, theToUse: bool) -> None:
        """Set flag for controlling the source of capping plane material."""

    def ToUseObjectTexture(self) -> bool:
        """
        Flag indicating whether texture for capping plane should be taken from object.
        Default value: FALSE.
        """

    def SetUseObjectTexture(self, theToUse: bool) -> None:
        """Set flag for controlling the source of capping plane texture."""

    def ToUseObjectShader(self) -> bool:
        """
        Flag indicating whether shader program for capping plane should be taken from object.
        Default value: FALSE.
        """

    def SetUseObjectShader(self, theToUse: bool) -> None:
        """Set flag for controlling the source of capping plane shader program."""

    def ToUseObjectProperties(self) -> bool:
        """
        Return true if some fill area aspect properties should be taken from object.
        """

    def ProbePoint(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> Graphic3d_ClipState:
        """Check if the given point is outside / inside / on section."""

    def ProbeBox(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> Graphic3d_ClipState:
        """Check if the given bounding box is fully outside / fully inside."""

    def ProbeBoxTouch(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> bool:
        """Check if the given bounding box is In and touch the clipping planes"""

    def ProbePointHalfspace(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> Graphic3d_ClipState:
        """
        Check if the given point is outside of the half-space (e.g. should be discarded by clipping
        plane).
        """

    def ProbeBoxHalfspace(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> Graphic3d_ClipState:
        """
        Check if the given bounding box is fully outside / fully inside the half-space.
        """

    def IsPointOutHalfspace(self, thePoint: nanoocp.BVH.BVH_Vec4d) -> bool:
        """
        Check if the given point is outside of the half-space (e.g. should be discarded by clipping
        plane).
        """

    def IsBoxFullOutHalfspace(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> bool:
        """
        Check if the given bounding box is fully outside of the half-space (e.g. should be discarded
        by clipping plane).
        """

    def ProbeBoxMaxPointHalfspace(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> Graphic3d_ClipState:
        """
        Check if the given bounding box is fully outside of the half-space (e.g. should be discarded
        by clipping plane).
        """

    def IsBoxFullInHalfspace(self, theBox: nanoocp.Bnd.BVH_Box__double__3) -> bool:
        """
        Check if the given bounding box is fully inside (or touches from inside) the half-space (e.g.
        NOT discarded by clipping plane).
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def MCountEquation(self) -> int:
        """@return modification counter for equation."""

    def MCountAspect(self) -> int:
        """@return modification counter for aspect."""

class Graphic3d_PresentationAttributes(nanoocp.Standard.Standard_Transient):
    """Class defines presentation properties."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_PresentationAttributes) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Method(self) -> nanoocp.Aspect.Aspect_TypeOfHighlightMethod:
        """Returns highlight method, Aspect_TOHM_COLOR by default."""

    def SetMethod(self, theMethod: nanoocp.Aspect.Aspect_TypeOfHighlightMethod) -> None:
        """Changes highlight method to the given one."""

    def ColorRGBA(self) -> nanoocp.Quantity.Quantity_ColorRGBA:
        """Returns basic presentation color (including alpha channel)."""

    def Color(self) -> nanoocp.Quantity.Quantity_Color:
        """Returns basic presentation color, Quantity_NOC_WHITE by default."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets basic presentation color (RGB components, does not modifies transparency).
        """

    def Transparency(self) -> float:
        """
        Returns basic presentation transparency (0 - opaque, 1 - fully transparent), 0 by default
        (opaque).
        """

    def SetTransparency(self, theTranspCoef: float) -> None:
        """
        Sets basic presentation transparency (0 - opaque, 1 - fully transparent).
        """

    def ZLayer(self) -> int:
        """
        Returns presentation Zlayer, Graphic3d_ZLayerId_Default by default.
        Graphic3d_ZLayerId_UNKNOWN means undefined (a layer of main presentation to be used).
        """

    def SetZLayer(self, theLayer: int) -> None:
        """Sets presentation Zlayer."""

    def DisplayMode(self) -> int:
        """
        Returns display mode, 0 by default.
        -1 means undefined (main display mode of presentation to be used).
        """

    def SetDisplayMode(self, theMode: int) -> None:
        """Sets display mode."""

    def BasicFillAreaAspect(self) -> Graphic3d_AspectFillArea3d:
        """
        Return basic presentation fill area aspect, NULL by default.
        When set, might be used instead of Color() property.
        """

    def SetBasicFillAreaAspect(self, theAspect: Graphic3d_AspectFillArea3d | None) -> None:
        """Sets basic presentation fill area aspect."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_Flipper(nanoocp.Standard.Standard_Transient):
    """
    CPU-side analogue of OpenGl_Flipper used by the selection pipeline.
    Describes a reference coordinate system used at draw time to mirror
    group contents so that they remain upright relative to the camera.
    The same logic is used here to compute the flipping matrix applied
    to bounding boxes and sensitive frustums, so that selection matches
    the rendered geometry.
    """

    @overload
    def __init__(self, theRefPlane: nanoocp.gp.gp_Ax2) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_Flipper) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def RefPlane(self) -> nanoocp.gp.gp_Ax2:
        """Return reference plane used for flipping."""

    def SetRefPlane(self, theValue: nanoocp.gp.gp_Ax2) -> None:
        """Set reference plane used for flipping."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream."""

class Graphic3d_Vertex:
    """This class represents a graphical 3D point."""

    @overload
    def __init__(self) -> None:
        """Creates a point with 0.0, 0.0, 0.0 coordinates."""

    @overload
    def __init__(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def __init__(self, theX: float, theY: float, theZ: float) -> None:
        """Creates a point with theX, theY and theZ coordinates."""

    @overload
    def __init__(self, theOther: Graphic3d_Vertex) -> None: ...

    @overload
    def SetCoord(self, theX: float, theY: float, theZ: float) -> None: ...

    @overload
    def SetCoord(self, theX: float, theY: float, theZ: float) -> None:
        """Modifies the coordinates."""

    @overload
    def Coord(self) -> tuple[float, float, float]: ...

    @overload
    def Coord(self) -> tuple[float, float, float]:
        """Returns the coordinates."""

    def X(self) -> float:
        """Returns the X coordinates."""

    def Y(self) -> float:
        """Returns the Y coordinate."""

    def Z(self) -> float:
        """Returns the Z coordinate."""

    def Distance(self, theOther: Graphic3d_Vertex) -> float:
        """Returns the distance between two points."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def xyz(self) -> list[float]: ...

    @xyz.setter
    def xyz(self, arg: Sequence[float], /) -> None: ...

class Graphic3d_Group(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition of groups
    of primitives inside of graphic objects (presentations).
    A group contains the primitives and attributes
    for which the range is limited to this group.
    The primitives of a group can be globally suppressed.

    There are two main group usage models:

    1) Non-modifiable, or unbounded, group ('black box').
    Developers can repeat a sequence of
    SetPrimitivesAspect() with AddPrimitiveArray() methods arbitrary number of times
    to define arbitrary number of primitive "blocks" each having individual aspect values.
    Any modification of such a group is forbidden, as aspects and primitives are mixed
    in memory without any high-level logical structure, and any modification is very likely to
    result in corruption of the group internal data. It is necessary to recreate such a group as a
    whole when some attribute should be changed. (for example, in terms of AIS it is necessary to
    re-Compute() the whole presentation each time). 2) Bounded group. Developers should specify the
    necessary group aspects with help of SetGroupPrimitivesAspect() and then add primitives to the
    group. Such a group have simplified organization in memory (a single block of attributes
    followed by a block of primitives) and therefore it can be modified, if it is necessary to
    change parameters of some aspect that has already been set, using methods:
    IsGroupPrimitivesAspectSet() to detect which aspect was set for primitives;
    GroupPrimitivesAspect() to read current aspect values
    and SetGroupPrimitivesAspect() to set new values.

    Developers are strongly recommended to take all the above into account when filling
    Graphic3d_Group with aspects and primitives and choose the group usage model beforehand out of
    application needs. Note that some Graphic3d_Group class virtual methods contain only base
    implementation that is extended by the descendant class in OpenGl package.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Clear(self, theUpdateStructureMgr: bool = True) -> None:
        """
        Suppress all primitives and attributes of <me>.
        To clear group without update in Graphic3d_StructureManager
        pass false as <theUpdateStructureMgr>. This
        used on context and viewer destruction, when the pointer
        to structure manager in Graphic3d_Structure could be
        already released (pointers are used here to avoid handle
        cross-reference);
        """

    def Remove(self) -> None:
        """
        Suppress the group <me> in the structure.
        Warning: No more graphic operations in <me> after this call.
        Modifies the current modelling transform persistence (pan, zoom or rotate)
        Get the current modelling transform persistence (pan, zoom or rotate)
        """

    def Aspects(self) -> Graphic3d_Aspects:
        """Return fill area aspect."""

    def SetGroupPrimitivesAspect(self, theAspect: Graphic3d_Aspects | None) -> None:
        """Modifies the context for all the face primitives of the group."""

    def SetPrimitivesAspect(self, theAspect: Graphic3d_Aspects | None) -> None:
        """
        Modifies the current context of the group to give another aspect for all the primitives
        created after this call in the group.
        """

    def SynchronizeAspects(self) -> None:
        """Update presentation aspects after their modification."""

    def ReplaceAspects(self, theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.Graphic3d.Graphic3d_Aspects, nanoocp.Graphic3d.Graphic3d_Aspects]) -> None:
        """Replace aspects specified in the replacement map."""

    def AddText(self, theTextParams: Graphic3d_Text | None, theToEvalMinMax: bool = True) -> None:
        """Adds a text for display"""

    @overload
    def AddPrimitiveArray(self, theType: Graphic3d_TypeOfPrimitiveArray, theIndices: Graphic3d_IndexBuffer | None, theAttribs: Graphic3d_Buffer | None, theBounds: Graphic3d_BoundBuffer | None, theToEvalMinMax: bool = True) -> None: ...

    @overload
    def AddPrimitiveArray(self, thePrim: Graphic3d_ArrayOfPrimitives | None, theToEvalMinMax: bool = True) -> None:
        """Adds an array of primitives for display"""

    def SetStencilTestOptions(self, theIsEnabled: bool) -> None:
        """sets the stencil test to theIsEnabled state;"""

    def SetFlippingOptions(self, theIsEnabled: bool, theRefPlane: nanoocp.gp.gp_Ax2) -> None:
        """sets the flipping to theIsEnabled state."""

    def Flipper(self) -> Graphic3d_Flipper:
        """
        Return flipper metadata describing the runtime flip of this group, or null if not flipped.
        """

    def Transformation(self) -> nanoocp.gp.gp_Trsf:
        """Return transformation."""

    def SetTransformation(self, theTrsf: nanoocp.gp.gp_Trsf) -> None:
        """Assign transformation."""

    def TransformPersistence(self) -> Graphic3d_TransformPers:
        """Return transformation persistence."""

    def SetTransformPersistence(self, theTrsfPers: Graphic3d_TransformPers | None) -> None:
        """Set transformation persistence."""

    def IsDeleted(self) -> bool:
        """
        Returns true if the group <me> is deleted.
        <me> is deleted after the call Remove (me) or the
        associated structure is deleted.
        """

    def IsEmpty(self) -> bool:
        """Returns true if the group <me> is empty."""

    def MinMaxValues(self) -> tuple[float, float, float, float, float, float]:
        """Returns the coordinates of the boundary box of the group."""

    def SetMinMaxValues(self, theXMin: float, theYMin: float, theZMin: float, theXMax: float, theYMax: float, theZMax: float) -> None:
        """Sets the coordinates of the boundary box of the group."""

    def BoundingBox(self) -> Graphic3d_BndBox4f:
        """Returns boundary box of the group <me> without transformation applied,"""

    def ChangeBoundingBox(self) -> Graphic3d_BndBox4f:
        """
        Returns non-const boundary box of the group <me> without transformation applied,
        """

    def Structure(self) -> Graphic3d_Structure:
        """Returns the structure containing the group <me>."""

    def SetClosed(self, theIsClosed: bool) -> None:
        """
        Changes property shown that primitive arrays within this group form closed volume (do no
        contain open shells).
        """

    def IsClosed(self) -> bool:
        """
        Return true if primitive arrays within this graphic group form closed volume (do no contain
        open shells).
        """

    def Marker(self, thePoint: Graphic3d_Vertex, theToEvalMinMax: bool = True) -> None:
        """
        Deprecated in OCCT: Deprecated method Marker(), pass Graphic3d_ArrayOfPoints to AddPrimitiveArray() instead

        @name obsolete methods
        """

    @overload
    def Text(self, AText: str, APoint: Graphic3d_Vertex, AHeight: float, AAngle: float, ATp: Graphic3d_TextPath, AHta: Graphic3d_HorizontalTextAlignment, AVta: Graphic3d_VerticalTextAlignment, EvalMinMax: bool = True) -> None: ...

    @overload
    def Text(self, AText: str, APoint: Graphic3d_Vertex, AHeight: float, EvalMinMax: bool = True) -> None: ...

    @overload
    def Text(self, AText: nanoocp.TCollection.TCollection_ExtendedString, APoint: Graphic3d_Vertex, AHeight: float, AAngle: float, ATp: Graphic3d_TextPath, AHta: Graphic3d_HorizontalTextAlignment, AVta: Graphic3d_VerticalTextAlignment, EvalMinMax: bool = True) -> None:
        """
        Deprecated in OCCT: Deprecated method Text() with obsolete arguments, use AddText() instead of it

        Creates the string <AText> at position <APoint>.
        The 3D point of attachment is projected. The text is
        written in the plane of projection.
        The attributes are given with respect to the plane of
        projection.
        AHeight : Height of text.
        (Relative to the Normalized Projection
        Coordinates (NPC) Space).
        AAngle  : Orientation of the text
        (with respect to the horizontal).
        """

    @overload
    def Text(self, AText: nanoocp.TCollection.TCollection_ExtendedString, APoint: Graphic3d_Vertex, AHeight: float, EvalMinMax: bool = True) -> None:
        """
        Deprecated in OCCT: Deprecated method Text() with obsolete arguments, use AddText() instead of it

        Creates the string <AText> at position <APoint>.
        The 3D point of attachment is projected. The text is
        written in the plane of projection.
        The attributes are given with respect to the plane of
        projection.
        AHeight : Height of text.
        (Relative to the Normalized Projection
        Coordinates (NPC) Space).
        The other attributes have the following default values:
        AAngle  : PI / 2.
        ATp     : TP_RIGHT
        AHta    : HTA_LEFT
        AVta    : VTA_BOTTOM
        """

    @overload
    def Text(self, theTextUtf: str, theOrientation: nanoocp.gp.gp_Ax2, theHeight: float, theAngle: float, theTp: Graphic3d_TextPath, theHTA: Graphic3d_HorizontalTextAlignment, theVTA: Graphic3d_VerticalTextAlignment, theToEvalMinMax: bool = True, theHasOwnAnchor: bool = True) -> None: ...

    @overload
    def Text(self, theText: nanoocp.TCollection.TCollection_ExtendedString, theOrientation: nanoocp.gp.gp_Ax2, theHeight: float, theAngle: float, theTp: Graphic3d_TextPath, theHTA: Graphic3d_HorizontalTextAlignment, theVTA: Graphic3d_VerticalTextAlignment, theToEvalMinMax: bool = True, theHasOwnAnchor: bool = True) -> None:
        """
        Deprecated in OCCT: Deprecated method Text() with obsolete arguments, use AddText() instead of it

        Creates the string <theText> at orientation <theOrientation> in 3D space.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_SequenceOfHClipPlane(nanoocp.Standard.Standard_Transient):
    """
    Class defines a Clipping Volume as a logical OR (disjunction) operation between
    Graphic3d_ClipPlane in sequence. Each Graphic3d_ClipPlane represents either a single Plane
    clipping a halfspace (direction is specified by normal), or a sub-chain of planes defining a
    logical AND (conjunction) operation. Therefore, this collection allows defining a Clipping
    Volume through the limited set of Boolean operations between clipping Planes.

    The Clipping Volume can be assigned either to entire View or to a specific Object;
    in the latter case property ToOverrideGlobal() will specify if Object planes should override
    (suppress) globally defined ones or extend their definition through logical OR (disjunction)
    operation.

    Note that defining (many) planes will lead to performance degradation, and Graphics Driver may
    limit the overall number of simultaneously active clipping planes - but at least 6 planes should
    be supported on all configurations.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_SequenceOfHClipPlane) -> None: ...

    class Iterator(nanoocp.NCollection.NCollection_Sequence__Handle_Graphic3d_ClipPlane.Iterator):
        """Iterator through clipping planes."""

        @overload
        def __init__(self) -> None: ...

        @overload
        def __init__(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...

        @overload
        def __init__(self, thePlanes: Graphic3d_SequenceOfHClipPlane | None) -> None: ...

        @overload
        def __init__(self, theOther: Graphic3d_SequenceOfHClipPlane.Iterator) -> None: ...

        @overload
        def Init(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...

        @overload
        def Init(self, thePlanes: Graphic3d_SequenceOfHClipPlane | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ToOverrideGlobal(self) -> bool:
        """Return true if local properties should override global properties."""

    def SetOverrideGlobal(self, theToOverride: bool) -> None:
        """
        Setup flag defining if local properties should override global properties.
        """

    def IsEmpty(self) -> bool:
        """Return TRUE if sequence is empty."""

    def Size(self) -> int:
        """Return the number of items in sequence."""

    def Append(self, theItem: Graphic3d_ClipPlane | None) -> bool:
        """
        Append a plane.
        @return TRUE if new item has been added (FALSE if item already existed)
        """

    @overload
    def Remove(self, theItem: Graphic3d_ClipPlane | None) -> bool:
        """
        Remove a plane.
        @return TRUE if item has been found and removed
        """

    @overload
    def Remove(self, theItem: Graphic3d_SequenceOfHClipPlane.Iterator) -> None:
        """Remove a plane."""

    def Clear(self) -> None:
        """Clear the items out."""

    def First(self) -> Graphic3d_ClipPlane:
        """Return the first item in sequence."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_ViewAffinity(nanoocp.Standard.Standard_Transient):
    """Structure display state."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_ViewAffinity) -> None: ...

    def IsVisible(self, theViewId: int) -> bool:
        """Return visibility flag."""

    @overload
    def SetVisible(self, theIsVisible: bool) -> None:
        """Setup visibility flag for all views."""

    @overload
    def SetVisible(self, theViewId: int, theIsVisible: bool) -> None:
        """Setup visibility flag."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_TransformUtils_MatrixType__double:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_TransformUtils_MatrixType__double) -> None: ...

class Graphic3d_TransformUtils_MatrixType__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_TransformUtils_MatrixType__float) -> None: ...

class Graphic3d_TransformUtils_VectorType__double:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_TransformUtils_VectorType__double) -> None: ...

class Graphic3d_TransformUtils_VectorType__float:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Graphic3d_TransformUtils_VectorType__float) -> None: ...

class Graphic3d_TransformPers(nanoocp.Standard.Standard_Transient):
    """
    Transformation Persistence definition.

    Transformation Persistence defines a mutable Local Coordinate system which depends on camera
    position, so that visual appearance of the object becomes partially immutable while camera
    moves. Object visually preserves particular property such as size, placement, rotation or their
    combination.

    Graphic3d_TMF_ZoomPers, Graphic3d_TMF_RotatePers and Graphic3d_TMF_ZoomRotatePers define Local
    Coordinate system having origin in specified anchor point defined in World Coordinate system,
    while Graphic3d_TMF_TriedronPers and Graphic3d_TMF_2d define origin as 2D offset from screen
    corner in pixels.

    Graphic3d_TMF_2d, Graphic3d_TMF_TriedronPers and Graphic3d_TMF_ZoomPers defines Local Coordinate
    system where length units are pixels. Beware that Graphic3d_RenderingParams::ResolutionRatio()
    will be ignored! For other Persistence flags, normal (world) length units will apply.

    Graphic3d_TMF_AxialPers and Graphic3d_TMF_AxialZoomPers defines persistence in the axial scale,
    i.e., keeps the object visual coherence when the camera's axial scale is changed.
    Meant to be used by objects such as Manipulators and trihedrons.
    WARNING: Graphic3d_TMF_None is not permitted for defining instance of this class - NULL handle
    should be used for this purpose!
    """

    @overload
    def __init__(self, theMode: Graphic3d_TransModeFlags) -> None:
        """Set transformation persistence."""

    @overload
    def __init__(self, theMode: Graphic3d_TransModeFlags, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Set Zoom/Rotate transformation persistence with an anchor 3D point.
        Anchor point defines the origin of Local Coordinate system within World Coordinate system.
        Throws an exception if persistence mode is not Graphic3d_TMF_ZoomPers,
        Graphic3d_TMF_ZoomRotatePers or Graphic3d_TMF_RotatePers.
        """

    @overload
    def __init__(self, theMode: Graphic3d_TransModeFlags, theCorner: nanoocp.Aspect.Aspect_TypeOfTriedronPosition, theOffset: nanoocp.BVH.BVH_Vec2i = ...) -> None:
        """
        Set 2d/trihedron transformation persistence with a corner and 2D offset.
        2D offset defines the origin of Local Coordinate system as projection of 2D point on screen
        plane into World Coordinate system. Throws an exception if persistence mode is not
        Graphic3d_TMF_TriedronPers or Graphic3d_TMF_2d. The offset is a positive displacement from the
        view corner in pixels.
        """

    @overload
    def __init__(self, theOther: Graphic3d_TransformPers) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def IsZoomOrRotate_s(theMode: Graphic3d_TransModeFlags) -> bool:
        """
        Return true if specified mode is zoom/rotate transformation persistence.
        """

    @staticmethod
    def IsTrihedronOr2d_s(theMode: Graphic3d_TransModeFlags) -> bool:
        """
        Return true if specified mode is 2d/trihedron transformation persistence.
        """

    @staticmethod
    def IsOrthoPers_s(theMode: Graphic3d_TransModeFlags) -> bool:
        """
        Return true if specified mode is orthographic projection transformation persistence.
        """

    @staticmethod
    def IsAxial_s(theMode: Graphic3d_TransModeFlags) -> bool:
        """Return true if specified mode is axial transformation persistence."""

    def IsZoomOrRotate(self) -> bool:
        """
        Return true for Graphic3d_TMF_ZoomPers, Graphic3d_TMF_ZoomRotatePers or
        Graphic3d_TMF_RotatePers modes.
        """

    def IsTrihedronOr2d(self) -> bool:
        """Return true for Graphic3d_TMF_TriedronPers and Graphic3d_TMF_2d modes."""

    def IsOrthoPers(self) -> bool:
        """Return true for Graphic3d_TMF_OrthoPers mode."""

    def IsAxial(self) -> bool:
        """Return true for Graphic3d_TMF_AxialScalePers modes."""

    def Mode(self) -> Graphic3d_TransModeFlags:
        """Transformation persistence mode flags."""

    def Flags(self) -> Graphic3d_TransModeFlags:
        """Transformation persistence mode flags."""

    @overload
    def SetPersistence(self, theMode: Graphic3d_TransModeFlags, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Set Zoom/Rotate transformation persistence with an anchor 3D point.
        Throws an exception if persistence mode is not Graphic3d_TMF_ZoomPers,
        Graphic3d_TMF_ZoomRotatePers or Graphic3d_TMF_RotatePers.
        """

    @overload
    def SetPersistence(self, theMode: Graphic3d_TransModeFlags, theCorner: nanoocp.Aspect.Aspect_TypeOfTriedronPosition, theOffset: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Set 2d/trihedron transformation persistence with a corner and 2D offset.
        Throws an exception if persistence mode is not Graphic3d_TMF_TriedronPers or Graphic3d_TMF_2d.
        """

    def AnchorPoint(self) -> nanoocp.gp.gp_Pnt:
        """Return the anchor point for zoom/rotate transformation persistence."""

    def SetAnchorPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Set the anchor point for zoom/rotate transformation persistence."""

    def Corner2d(self) -> nanoocp.Aspect.Aspect_TypeOfTriedronPosition:
        """Return the corner for 2d/trihedron transformation persistence."""

    def SetCorner2d(self, thePos: nanoocp.Aspect.Aspect_TypeOfTriedronPosition) -> None:
        """Set the corner for 2d/trihedron transformation persistence."""

    def Offset2d(self) -> nanoocp.BVH.BVH_Vec2i:
        """
        Return the offset from the corner for 2d/trihedron transformation persistence.
        """

    def SetOffset2d(self, theOffset: nanoocp.BVH.BVH_Vec2i) -> None:
        """
        Set the offset from the corner for 2d/trihedron transformation persistence.
        """

    def persistentScale(self, theCamera: Graphic3d_Camera | None, theViewportWidth: int, theViewportHeight: int) -> float:
        """
        Find scale value based on the camera position and view dimensions
        @param[in] theCamera  camera definition
        @param[in] theViewportWidth  the width of viewport.
        @param[in] theViewportHeight  the height of viewport.
        """

    def persistentRotationMatrix(self, theCamera: Graphic3d_Camera | None, theViewportWidth: int, theViewportHeight: int) -> NCollection_Mat3__double:
        """
        Create orientation matrix based on camera and view dimensions.
        Default implementation locks rotation by nullifying rotation component.
        Camera and view dimensions are not used, by default.
        @param[in] theCamera  camera definition
        @param[in] theViewportWidth  the width of viewport
        @param[in] theViewportHeight  the height of viewport
        """

    def ComputeApply(self, theViewportWidth: int, theViewportHeight: int, theAnchor: nanoocp.gp.gp_Pnt = None) -> tuple[nanoocp.BVH.BVH_Mat4d, Graphic3d_Camera]:
        """
        Perform computations for applying transformation persistence on specified matrices.
        @param[in] theCamera  camera definition
        @param[in] theViewportWidth   viewport width
        @param[in] theViewportHeight  viewport height
        @param[in] theAnchor  if not NULL, overrides anchor point
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_CStructure(nanoocp.Standard.Standard_Transient):
    """Low-level graphic structure interface"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GraphicDriver(self) -> Graphic3d_GraphicDriver:
        """@return graphic driver created this structure"""

    def Groups(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_Group]:
        """@return graphic groups"""

    def Transformation(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """Return transformation."""

    def SetTransformation(self, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """Assign transformation."""

    def TransformPersistence(self) -> Graphic3d_TransformPers:
        """Return transformation persistence."""

    def SetTransformPersistence(self, theTrsfPers: Graphic3d_TransformPers | None) -> None:
        """Set transformation persistence."""

    def HasGroupTransformPersistence(self) -> bool:
        """
        Return TRUE if some groups might have transform persistence; FALSE by default.
        """

    def SetGroupTransformPersistence(self, theValue: bool) -> None:
        """Set if some groups might have transform persistence."""

    def HasGroupFlipping(self) -> bool:
        """
        Return TRUE if some groups might have flipping options; FALSE by default.
        """

    def SetGroupFlipping(self, theValue: bool) -> None:
        """Set if some groups might have flipping options."""

    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane:
        """@return associated clip planes"""

    def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane | None) -> None:
        """Pass clip planes to the associated graphic driver structure"""

    def BoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """@return bounding box of this presentation"""

    def ChangeBoundingBox(self) -> nanoocp.Bnd.BVH_Box__double__3:
        """
        @return bounding box of this presentation
        without transformation matrix applied
        """

    @overload
    def IsVisible(self) -> bool:
        """Return structure visibility flag"""

    @overload
    def IsVisible(self, theViewId: int) -> bool:
        """
        Return structure visibility considering both View Affinity and global visibility state.
        """

    def SetZLayer(self, theLayerIndex: int) -> None:
        """Set z layer ID to display the structure in specified layer"""

    def ZLayer(self) -> int:
        """Get z layer ID"""

    def HighlightStyle(self) -> Graphic3d_PresentationAttributes:
        """
        Returns valid handle to highlight style of the structure in case if
        highlight flag is set to true
        """

    def Identification(self) -> int:
        """
        Return structure id (generated by Graphic3d_GraphicDriver::NewIdentification() during
        structure construction).
        """

    def Priority(self) -> Graphic3d_DisplayPriority:
        """Return structure display priority."""

    def SetPriority(self, thePriority: Graphic3d_DisplayPriority) -> None:
        """Set structure display priority."""

    def PreviousPriority(self) -> Graphic3d_DisplayPriority:
        """Return previous structure display priority."""

    def SetPreviousPriority(self, thePriority: Graphic3d_DisplayPriority) -> None:
        """Set previous structure display priority."""

    def IsCulled(self) -> bool:
        """
        Returns FALSE if the structure hits the current view volume, otherwise returns TRUE.
        """

    def SetCulled(self, theIsCulled: bool) -> None:
        """
        Marks structure as culled/not culled - note that IsAlwaysRendered() is ignored here!
        """

    def MarkAsNotCulled(self) -> None:
        """
        Marks structure as overlapping the current view volume one.
        The method is called during traverse of BVH tree.
        """

    def BndBoxClipCheck(self) -> bool:
        """
        Returns whether check of object's bounding box clipping is enabled before drawing of object;
        TRUE by default.
        """

    def SetBndBoxClipCheck(self, theBndBoxClipCheck: bool) -> None:
        """
        Enable/disable check of object's bounding box clipping before drawing of object.
        """

    def IsAlwaysRendered(self) -> bool:
        """Checks if the structure should be included into BVH tree or not."""

    def OnVisibilityChanged(self) -> None:
        """Update structure visibility state"""

    def Clear(self) -> None:
        """Clear graphic data"""

    def Connect(self, theStructure: Graphic3d_CStructure) -> None:
        """Connect other structure to this one"""

    def Disconnect(self, theStructure: Graphic3d_CStructure) -> None:
        """Disconnect other structure to this one"""

    def GraphicHighlight(self, theStyle: Graphic3d_PresentationAttributes | None) -> None:
        """Highlights structure with the given style"""

    def GraphicUnhighlight(self) -> None:
        """
        Unhighlights the structure and invalidates pointer to structure's highlight style
        """

    def ShadowLink(self, theManager: Graphic3d_StructureManager | None) -> Graphic3d_CStructure:
        """Create shadow link to this structure"""

    def NewGroup(self, theStruct: Graphic3d_Structure | None) -> Graphic3d_Group:
        """Create new group within this structure"""

    def RemoveGroup(self, theGroup: Graphic3d_Group | None) -> None:
        """Remove group from this structure"""

    def updateLayerTransformation(self) -> None:
        """Update render transformation matrix."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def ViewAffinity(self) -> Graphic3d_ViewAffinity:
        """view affinity mask"""

    @ViewAffinity.setter
    def ViewAffinity(self, arg: Graphic3d_ViewAffinity, /) -> None: ...

    @property
    def IsInfinite(self) -> int: ...

    @IsInfinite.setter
    def IsInfinite(self, arg: int, /) -> None: ...

    @property
    def stick(self) -> int:
        """
        displaying state - should be set when structure has been added to scene graph (but can be in hidden state)
        """

    @stick.setter
    def stick(self, arg: int, /) -> None: ...

    @property
    def highlight(self) -> int: ...

    @highlight.setter
    def highlight(self, arg: int, /) -> None: ...

    @property
    def visible(self) -> int:
        """
        visibility flag - can be used to suppress structure while leaving it in the scene graph
        """

    @visible.setter
    def visible(self, arg: int, /) -> None: ...

    @property
    def HLRValidation(self) -> int: ...

    @HLRValidation.setter
    def HLRValidation(self, arg: int, /) -> None: ...

    @property
    def IsForHighlight(self) -> int: ...

    @IsForHighlight.setter
    def IsForHighlight(self, arg: int, /) -> None: ...

    @property
    def IsMutable(self) -> int: ...

    @IsMutable.setter
    def IsMutable(self, arg: int, /) -> None: ...

    @property
    def Is2dText(self) -> int: ...

    @Is2dText.setter
    def Is2dText(self, arg: int, /) -> None: ...

class Graphic3d_CubeMapOrder:
    """
    Graphic3d_CubeMapOrder maps sides of cubemap on tiles in packed cubemap image
    to support different tiles order in such images.
    Also it can be considered as permutation of numbers from 0 to 5.
    It stores permutation in one integer as convolution.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor.
        Creates empty order with zero convolution.
        """

    @overload
    def __init__(self, theOrder: Graphic3d_ValidatedCubeMapOrder) -> None:
        """Creates Graphic3d_CubeMapOrder using Graphic3d_ValidatedCubeMapOrder."""

    @overload
    def __init__(self, thePosXLocation: int, theNegXLocation: int, thePosYLocation: int, theNegYLocation: int, thePosZLocation: int, theNegZLocation: int) -> None:
        """Initializes order with values."""

    @overload
    def __init__(self, theOther: Graphic3d_CubeMapOrder) -> None: ...

    @overload
    def Set(self, theOrder: Graphic3d_CubeMapOrder) -> Graphic3d_CubeMapOrder:
        """Alias of 'operator='."""

    @overload
    def Set(self, theCubeMapSide: Graphic3d_CubeMapSide, theValue: int) -> Graphic3d_CubeMapOrder:
        """
        Sets number of tile in packed cubemap image according passed cubemap side.
        """

    def Validated(self) -> Graphic3d_ValidatedCubeMapOrder:
        """
        Checks whether order is valid and returns object containing it.
        If order is invalid then exception will be thrown.
        This method is only way to create Graphic3d_ValidatedCubeMapOrder except copy constructor.
        """

    def SetDefault(self) -> Graphic3d_CubeMapOrder:
        """Sets default order (just from 0 to 5)"""

    def Permute(self, anOrder: Graphic3d_ValidatedCubeMapOrder) -> Graphic3d_CubeMapOrder:
        """Applies another cubemap order as permutation for the current one."""

    def Permuted(self, anOrder: Graphic3d_ValidatedCubeMapOrder) -> Graphic3d_CubeMapOrder:
        """Returns permuted by other cubemap order copy of current one."""

    def Swap(self, theFirstSide: Graphic3d_CubeMapSide, theSecondSide: Graphic3d_CubeMapSide) -> Graphic3d_CubeMapOrder:
        """Swaps values of two cubemap sides."""

    def Swapped(self, theFirstSide: Graphic3d_CubeMapSide, theSecondSide: Graphic3d_CubeMapSide) -> Graphic3d_CubeMapOrder:
        """
        Returns copy of current order with swapped values of two cubemap sides.
        """

    def Get(self, theCubeMapSide: Graphic3d_CubeMapSide) -> int:
        """Returns value of passed cubemap side."""

    def __getitem__(self, theCubeMapSide: Graphic3d_CubeMapSide) -> int:
        """Alias of 'Get'."""

    def Clear(self) -> Graphic3d_CubeMapOrder:
        """Makes order empty."""

    def IsEmpty(self) -> bool:
        """Checks whether order is empty."""

    def HasRepetitions(self) -> bool:
        """Checks whether order has repetitions."""

    def HasOverflows(self) -> bool:
        """
        Checks whether attempts to assign index greater than 5 to any side happed.
        """

    def IsValid(self) -> bool:
        """
        Checks whether order is valid.
        Order is valid when it doesn't have repetitions
        and there were not attempts to assign indexes greater than 5.
        """

    @staticmethod
    def Default() -> Graphic3d_ValidatedCubeMapOrder:
        """
        Returns default order in protector container class.
        It is guaranteed to be valid.
        """

class Graphic3d_ValidatedCubeMapOrder:
    """
    Graphic3d_ValidatedCubeMapOrder contains completely valid order object.
    The only way to create this class except copy constructor is 'Validated' method of
    Graphic3d_CubeMapOrder. This class can initialize Graphic3d_CubeMapOrder. It is supposed to be
    used in case of necessity of completely valid order (in function argument as example). It helps
    to automate order's valid checks.
    """

    def __init__(self, theOther: Graphic3d_ValidatedCubeMapOrder) -> None:
        """Copy constructor."""

    @property
    def Order(self) -> Graphic3d_CubeMapOrder:
        """Completely valid order"""

class Graphic3d_CubeMap(Graphic3d_TextureMap):
    """
    Base class for cubemaps.
    It is iterator over cubemap sides.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def More(self) -> bool:
        """Returns whether the iterator has reached the end (true if it hasn't)."""

    def CurrentSide(self) -> Graphic3d_CubeMapSide:
        """Returns current cubemap side (iterator state)."""

    def Next(self) -> None:
        """
        Moves iterator to the next cubemap side.
        Uses OpenGL cubemap sides order +X -> -X -> +Y -> -Y -> +Z -> -Z.
        """

    def SetZInversion(self, theZIsInverted: bool) -> None:
        """Sets Z axis inversion (vertical flipping)."""

    def ZIsInverted(self) -> bool:
        """Returns whether Z axis is inverted."""

    def HasMipmaps(self) -> bool:
        """Returns whether mipmaps of cubemap will be generated or not."""

    def SetMipmapsGeneration(self, theToGenerateMipmaps: bool) -> None:
        """Sets whether to generate mipmaps of cubemap or not."""

    def CompressedValue(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_CompressedPixMap:
        """
        Returns current cubemap side as compressed PixMap.
        Returns null handle if current side is invalid or if image is not in supported compressed
        format.
        """

    def Value(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """
        Returns PixMap containing current side of cubemap.
        Returns null handle if current side is invalid.
        """

    def Reset(self) -> Graphic3d_CubeMap:
        """Sets iterator state to +X cubemap side."""

class Graphic3d_CubeMapPacked(Graphic3d_CubeMap):
    """Class is intended to process cubemap packed into single image plane."""

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString, theOrder: Graphic3d_ValidatedCubeMapOrder = ...) -> None:
        """
        Initialization to load cubemap from file.
        @theFileName - path to the cubemap image
        @theOrder - array containing six different indexes of cubemap sides which maps tile grid to
        cubemap sides
        """

    @overload
    def __init__(self, theImage: nanoocp.Image.Image_PixMap | None, theOrder: Graphic3d_ValidatedCubeMapOrder = ...) -> None:
        """
        Initialization to set cubemap directly by PixMap.
        @thePixMap - origin PixMap
        @theOrder - array containing six different indexes of cubemap sides which maps tile grid to
        cubemap sides
        """

    @overload
    def __init__(self, theOther: Graphic3d_CubeMapPacked) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CompressedValue(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_CompressedPixMap:
        """Returns current cubemap side as compressed PixMap."""

    def Value(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """
        Returns current cubemap side as PixMap.
        Resulting PixMap is memory wrapper over original image.
        Returns null handle if current side or whole cubemap is invalid.
        Origin image has to contain six quad tiles having one sizes without any gaps to be valid.
        """

class Graphic3d_CubeMapSeparate(Graphic3d_CubeMap):
    """Class to manage cubemap located in six different images."""

    @overload
    def __init__(self, thePaths: nanoocp.NCollection.NCollection_Array1[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Initializes cubemap to be loaded from file.
        @thePaths - array of paths to separate image files (has to have size equal 6).
        """

    @overload
    def __init__(self, theImages: nanoocp.NCollection.NCollection_Array1[nanoocp.Image.Image_PixMap]) -> None:
        """
        Initializes cubemap to be set directly from PixMaps.
        @theImages - array if PixMaps (has to have size equal 6).
        """

    @overload
    def __init__(self, theOther: Graphic3d_CubeMapSeparate) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def CompressedValue(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_CompressedPixMap:
        """Returns current cubemap side as compressed PixMap."""

    def Value(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """
        Returns current side of cubemap as PixMap.
        Returns null handle if current side or whole cubemap is invalid.
        All origin images have to have the same sizes, format and quad shapes to form valid cubemap.
        """

    def GetImage(self, arg0: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """Returns NULL."""

    def IsDone(self) -> bool:
        """
        Checks if a texture class is valid or not.
        Returns true if the construction of the class is correct.
        """

class Graphic3d_CullingTool:
    """
    Graphic3d_CullingTool class provides a possibility to store parameters of view volume,
    such as its vertices and equations, and contains methods detecting if given AABB overlaps view
    volume.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates an empty selector object with parallel projection type by default.
        """

    @overload
    def __init__(self, theOther: Graphic3d_CullingTool) -> None: ...

    class CullingContext:
        """Auxiliary structure holding non-persistent culling options."""

        @overload
        def __init__(self) -> None:
            """Empty constructor."""

        @overload
        def __init__(self, theOther: Graphic3d_CullingTool.CullingContext) -> None: ...

        @property
        def DistCull(self) -> float:
            """culling distance"""

        @DistCull.setter
        def DistCull(self, arg: float, /) -> None: ...

        @property
        def SizeCull2(self) -> float:
            """squared culling size"""

        @SizeCull2.setter
        def SizeCull2(self, arg: float, /) -> None: ...

    class Plane:
        """Auxiliary structure representing 3D plane."""

        @overload
        def __init__(self) -> None:
            """Creates default plane."""

        @overload
        def __init__(self, theOrigin: nanoocp.BVH.BVH_Vec3d, theNormal: nanoocp.BVH.BVH_Vec3d) -> None:
            """Creates plane with specific parameters."""

        @overload
        def __init__(self, theOther: Graphic3d_CullingTool.Plane) -> None: ...

        @property
        def Origin(self) -> nanoocp.BVH.BVH_Vec3d: ...

        @Origin.setter
        def Origin(self, arg: nanoocp.BVH.BVH_Vec3d, /) -> None: ...

        @property
        def Normal(self) -> nanoocp.BVH.BVH_Vec3d: ...

        @Normal.setter
        def Normal(self, arg: nanoocp.BVH.BVH_Vec3d, /) -> None: ...

    def SetViewVolume(self, theCamera: Graphic3d_Camera | None, theModelWorld: nanoocp.BVH.BVH_Mat4d = ...) -> None:
        """
        Retrieves view volume's planes equations and its vertices from projection and world-view
        matrices.
        @param[in] theCamera  camera definition
        @param[in] theModelWorld  optional object transformation for computing frustum in object local
        coordinate system
        """

    def SetViewportSize(self, theViewportWidth: int, theViewportHeight: int, theResolutionRatio: float) -> None: ...

    def SetCullingDistance(self, theCtx: Graphic3d_CullingTool.CullingContext, theDistance: float) -> None:
        """Setup distance culling."""

    def SetCullingSize(self, theCtx: Graphic3d_CullingTool.CullingContext, theSize: float) -> None:
        """Setup size culling."""

    def CacheClipPtsProjections(self) -> None:
        """
        Caches view volume's vertices projections along its normals and AABBs dimensions.
        Must be called at the beginning of each BVH tree traverse loop.
        """

    def IsCulled(self, theCtx: Graphic3d_CullingTool.CullingContext, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Checks whether given AABB should be entirely culled or not.
        @param[in] theCtx     culling properties
        @param[in] theMinPnt  maximum point of AABB
        @param[in] theMaxPnt  minimum point of AABB
        @param[out] theIsInside  flag indicating if AABB is fully inside; initial value should be set
        to TRUE
        @return TRUE if AABB is completely outside of view frustum or culled by size/distance;
        FALSE in case of partial or complete overlap (use theIsInside to distinguish)
        """

    def Camera(self) -> Graphic3d_Camera:
        """Return the camera definition."""

    def ProjectionMatrix(self) -> nanoocp.BVH.BVH_Mat4d:
        """Returns current projection matrix."""

    def WorldViewMatrix(self) -> nanoocp.BVH.BVH_Mat4d:
        """Returns current world view transformation matrix."""

    def ViewportWidth(self) -> int: ...

    def ViewportHeight(self) -> int: ...

    def WorldViewProjState(self) -> Graphic3d_WorldViewProjState:
        """
        Returns state of current world view projection transformation matrices.
        """

    def CameraEye(self) -> nanoocp.BVH.BVH_Vec3d:
        """Returns camera eye position."""

    def CameraDirection(self) -> nanoocp.BVH.BVH_Vec3d:
        """Returns camera direction."""

    def SignedPlanePointDistance(self, theNormal: nanoocp.BVH.BVH_Vec4d, thePnt: nanoocp.BVH.BVH_Vec4d) -> float:
        """
        Calculates signed distance from plane to point.
        @param[in] theNormal  the plane's normal.
        @param[in] thePnt
        """

    def IsOutFrustum(self, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Detects if AABB overlaps view volume using separating axis theorem (SAT).
        @param[in] theMinPnt    maximum point of AABB
        @param[in] theMaxPnt    minimum point of AABB
        @param[out] theIsInside  flag indicating if AABB is fully inside; initial value should be set
        to TRUE
        @return TRUE if AABB is completely outside of view frustum;
        FALSE in case of partial or complete overlap (use theIsInside to distinguish)
        @sa SelectMgr_Frustum::hasOverlap()
        """

    def IsTooDistant(self, theCtx: Graphic3d_CullingTool.CullingContext, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Returns TRUE if given AABB should be discarded by distance culling criterion.
        @param[in] theMinPnt    maximum point of AABB
        @param[in] theMaxPnt    minimum point of AABB
        @param[out] theIsInside  flag indicating if AABB is fully inside; initial value should be set
        to TRUE
        @return TRUE if AABB is completely behind culling distance;
        FALSE in case of partial or complete overlap (use theIsInside to distinguish)
        """

    def IsTooSmall(self, theCtx: Graphic3d_CullingTool.CullingContext, theMinPnt: nanoocp.BVH.BVH_Vec3d, theMaxPnt: nanoocp.BVH.BVH_Vec3d) -> bool:
        """
        Returns TRUE if given AABB should be discarded by size culling criterion.
        """

class Graphic3d_DataStructureManager(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition of a manager to
    which the graphic objects are associated.
    It allows them to be globally manipulated.
    It defines the global attributes.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_GraduatedTrihedron:
    """
    Defines the class of a graduated trihedron.
    It contains main style parameters for implementation of graduated trihedron
    @sa OpenGl_GraduatedTrihedron
    """

    @overload
    def __init__(self, theNamesFont: nanoocp.TCollection.TCollection_AsciiString = ..., theNamesStyle: nanoocp.Font.Font_FontAspect = Font_FontAspect.Font_FontAspect_Bold, theNamesSize: int = 12, theValuesFont: nanoocp.TCollection.TCollection_AsciiString = ..., theValuesStyle: nanoocp.Font.Font_FontAspect = Font_FontAspect.Font_FontAspect_Regular, theValuesSize: int = 12, theArrowsLength: float = 30.0, theGridColor: nanoocp.Quantity.Quantity_Color = ..., theToDrawGrid: bool = True, theToDrawAxes: bool = True) -> None:
        """
        Default constructor
        Constructs the default graduated trihedron with grid, X, Y, Z axes, and tickmarks
        """

    @overload
    def __init__(self, theOther: Graphic3d_GraduatedTrihedron) -> None: ...

    class AxisAspect:
        """
        Class that stores style for one graduated trihedron axis such as colors, lengths and
        customization flags. It is used in Graphic3d_GraduatedTrihedron.
        """

        @overload
        def __init__(self, theName: nanoocp.TCollection.TCollection_ExtendedString = ..., theNameColor: nanoocp.Quantity.Quantity_Color = ..., theColor: nanoocp.Quantity.Quantity_Color = ..., theValuesOffset: int = 10, theNameOffset: int = 30, theTickmarksNumber: int = 5, theTickmarksLength: int = 10, theToDrawName: bool = True, theToDrawValues: bool = True, theToDrawTickmarks: bool = True) -> None: ...

        @overload
        def __init__(self, theOther: Graphic3d_GraduatedTrihedron.AxisAspect) -> None: ...

        def SetName(self, theName: nanoocp.TCollection.TCollection_ExtendedString) -> None: ...

        def Name(self) -> nanoocp.TCollection.TCollection_ExtendedString: ...

        def ToDrawName(self) -> bool: ...

        def SetDrawName(self, theToDraw: bool) -> None: ...

        def ToDrawTickmarks(self) -> bool: ...

        def SetDrawTickmarks(self, theToDraw: bool) -> None: ...

        def ToDrawValues(self) -> bool: ...

        def SetDrawValues(self, theToDraw: bool) -> None: ...

        def NameColor(self) -> nanoocp.Quantity.Quantity_Color: ...

        def SetNameColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

        def Color(self) -> nanoocp.Quantity.Quantity_Color:
            """Color of axis and values"""

        def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
            """Sets color of axis and values"""

        def TickmarksNumber(self) -> int: ...

        def SetTickmarksNumber(self, theValue: int) -> None: ...

        def TickmarksLength(self) -> int: ...

        def SetTickmarksLength(self, theValue: int) -> None: ...

        def ValuesOffset(self) -> int: ...

        def SetValuesOffset(self, theValue: int) -> None: ...

        def NameOffset(self) -> int: ...

        def SetNameOffset(self, theValue: int) -> None: ...

    def ChangeXAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def ChangeYAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def ChangeZAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def ChangeAxisAspect(self, theIndex: int) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def XAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def YAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def ZAxisAspect(self) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def AxisAspectAt(self, theIndex: int) -> Graphic3d_GraduatedTrihedron.AxisAspect: ...

    def ArrowsLength(self) -> float: ...

    def SetArrowsLength(self, theValue: float) -> None: ...

    def GridColor(self) -> nanoocp.Quantity.Quantity_Color: ...

    def SetGridColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def ToDrawGrid(self) -> bool: ...

    def SetDrawGrid(self, theToDraw: bool) -> None: ...

    def ToDrawAxes(self) -> bool: ...

    def SetDrawAxes(self, theToDraw: bool) -> None: ...

    def NamesFont(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetNamesFont(self, theFont: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def NamesFontAspect(self) -> nanoocp.Font.Font_FontAspect: ...

    def SetNamesFontAspect(self, theAspect: nanoocp.Font.Font_FontAspect) -> None: ...

    def NamesSize(self) -> int: ...

    def SetNamesSize(self, theValue: int) -> None: ...

    def ValuesFont(self) -> nanoocp.TCollection.TCollection_AsciiString: ...

    def SetValuesFont(self, theFont: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    def ValuesFontAspect(self) -> nanoocp.Font.Font_FontAspect: ...

    def SetValuesFontAspect(self, theAspect: nanoocp.Font.Font_FontAspect) -> None: ...

    def ValuesSize(self) -> int: ...

    def SetValuesSize(self, theValue: int) -> None: ...

    def CubicAxesCallback(self, theView: Graphic3d_CView) -> bool: ...

class Graphic3d_RenderingParams:
    """Helper class to store rendering parameters."""

    @overload
    def __init__(self) -> None:
        """Creates default rendering parameters."""

    @overload
    def __init__(self, theOther: Graphic3d_RenderingParams) -> None: ...

    class Anaglyph(enum.IntEnum):
        """Anaglyph filter presets."""

        Anaglyph_RedCyan_Simple = 0

        Anaglyph_RedCyan_Optimized = 1

        Anaglyph_YellowBlue_Simple = 2

        Anaglyph_YellowBlue_Optimized = 3

        Anaglyph_GreenMagenta_Simple = 4

        Anaglyph_UserDefined = 5

    Anaglyph_RedCyan_Simple: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_RedCyan_Simple

    Anaglyph_RedCyan_Optimized: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_RedCyan_Optimized

    Anaglyph_YellowBlue_Simple: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_YellowBlue_Simple

    Anaglyph_YellowBlue_Optimized: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_YellowBlue_Optimized

    Anaglyph_GreenMagenta_Simple: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_GreenMagenta_Simple

    Anaglyph_UserDefined: Graphic3d_RenderingParams.Anaglyph = Anaglyph.Anaglyph_UserDefined

    class PerfCounters(enum.IntEnum):
        """
        Statistics display flags.
        If not specified otherwise, the counter value is computed for a single rendered frame.
        """

        PerfCounters_NONE = 0

        PerfCounters_FrameRate = 1

        PerfCounters_CPU = 2

        PerfCounters_Layers = 4

        PerfCounters_Structures = 8

        PerfCounters_Groups = 16

        PerfCounters_GroupArrays = 32

        PerfCounters_Triangles = 64

        PerfCounters_Points = 128

        PerfCounters_Lines = 256

        PerfCounters_EstimMem = 512

        PerfCounters_FrameTime = 1024

        PerfCounters_FrameTimeMax = 2048

        PerfCounters_SkipImmediate = 4096

        PerfCounters_Basic = 15

        PerfCounters_Extended = 1023

        PerfCounters_All = 4095

    PerfCounters_NONE: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_NONE

    PerfCounters_FrameRate: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_FrameRate

    PerfCounters_CPU: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_CPU

    PerfCounters_Layers: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Layers

    PerfCounters_Structures: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Structures

    PerfCounters_Groups: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Groups

    PerfCounters_GroupArrays: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_GroupArrays

    PerfCounters_Triangles: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Triangles

    PerfCounters_Points: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Points

    PerfCounters_Lines: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Lines

    PerfCounters_EstimMem: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_EstimMem

    PerfCounters_FrameTime: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_FrameTime

    PerfCounters_FrameTimeMax: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_FrameTimeMax

    PerfCounters_SkipImmediate: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_SkipImmediate

    PerfCounters_Basic: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Basic

    PerfCounters_Extended: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_Extended

    PerfCounters_All: Graphic3d_RenderingParams.PerfCounters = PerfCounters.PerfCounters_All

    class FrustumCulling(enum.IntEnum):
        """State of frustum culling optimization."""

        FrustumCulling_Off = 0

        FrustumCulling_On = 1

        FrustumCulling_NoUpdate = 2

    FrustumCulling_Off: Graphic3d_RenderingParams.FrustumCulling = FrustumCulling.FrustumCulling_Off

    FrustumCulling_On: Graphic3d_RenderingParams.FrustumCulling = FrustumCulling.FrustumCulling_On

    FrustumCulling_NoUpdate: Graphic3d_RenderingParams.FrustumCulling = FrustumCulling.FrustumCulling_NoUpdate

    def ResolutionRatio(self) -> float:
        """Returns resolution ratio."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @property
    def Method(self) -> Graphic3d_RenderingMode:
        """specifies rendering mode, Graphic3d_RM_RASTERIZATION by default"""

    @Method.setter
    def Method(self, arg: Graphic3d_RenderingMode, /) -> None: ...

    @property
    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel:
        """
        specified default shading model, Graphic3d_TypeOfShadingModel_Phong by default
        """

    @ShadingModel.setter
    def ShadingModel(self, arg: Graphic3d_TypeOfShadingModel, /) -> None: ...

    @property
    def TransparencyMethod(self) -> Graphic3d_RenderTransparentMethod:
        """specifies rendering method for transparent graphics"""

    @TransparencyMethod.setter
    def TransparencyMethod(self, arg: Graphic3d_RenderTransparentMethod, /) -> None: ...

    @property
    def Resolution(self) -> int:
        """
        Pixels density (PPI), defines scaling factor for parameters like text size
        """

    @Resolution.setter
    def Resolution(self, arg: int, /) -> None: ...

    @property
    def FontHinting(self) -> nanoocp.Font.Font_Hinting:
        """
        enables/disables text hinting within textured fonts, Font_Hinting_Off by default;
        """

    @FontHinting.setter
    def FontHinting(self, arg: nanoocp.Font.Font_Hinting, /) -> None: ...

    @property
    def LineFeather(self) -> float:
        """line feather width in pixels (> 0.0), 1.0 by default;"""

    @LineFeather.setter
    def LineFeather(self, arg: float, /) -> None: ...

    @property
    def PbrEnvPow2Size(self) -> int:
        """
        size of IBL maps side can be calculated as 2^PbrEnvPow2Size (> 0), 9 by default
        """

    @PbrEnvPow2Size.setter
    def PbrEnvPow2Size(self, arg: int, /) -> None: ...

    @property
    def PbrEnvSpecMapNbLevels(self) -> int:
        """number of levels used in specular IBL map (> 1), 6 by default"""

    @PbrEnvSpecMapNbLevels.setter
    def PbrEnvSpecMapNbLevels(self, arg: int, /) -> None: ...

    @property
    def PbrEnvBakingDiffNbSamples(self) -> int:
        """
        number of samples used in Monte-Carlo integration during diffuse IBL map's
        """

    @PbrEnvBakingDiffNbSamples.setter
    def PbrEnvBakingDiffNbSamples(self, arg: int, /) -> None: ...

    @property
    def PbrEnvBakingSpecNbSamples(self) -> int:
        """
        number of samples used in Monte-Carlo integration during specular IBL map's generation (> 0), 256 by default
        """

    @PbrEnvBakingSpecNbSamples.setter
    def PbrEnvBakingSpecNbSamples(self, arg: int, /) -> None: ...

    @property
    def PbrEnvBakingProbability(self) -> float:
        """
        controls strength of samples reducing strategy during specular IBL map's generation
        """

    @PbrEnvBakingProbability.setter
    def PbrEnvBakingProbability(self, arg: float, /) -> None: ...

    @property
    def OitDepthFactor(self) -> float:
        """
        scalar factor [0-1] controlling influence of depth of a fragment to its final coverage (Graphic3d_RTM_BLEND_OIT), 0.0 by default
        """

    @OitDepthFactor.setter
    def OitDepthFactor(self, arg: float, /) -> None: ...

    @property
    def NbOitDepthPeelingLayers(self) -> int:
        """
        number of depth peeling (Graphic3d_RTM_DEPTH_PEELING_OIT) layers, 4 by default
        """

    @NbOitDepthPeelingLayers.setter
    def NbOitDepthPeelingLayers(self, arg: int, /) -> None: ...

    @property
    def NbMsaaSamples(self) -> int:
        """
        number of MSAA samples (should be within 0..GL_MAX_SAMPLES, power-of-two number), 0 by default
        """

    @NbMsaaSamples.setter
    def NbMsaaSamples(self, arg: int, /) -> None: ...

    @property
    def RenderResolutionScale(self) -> float:
        """rendering resolution scale factor, 1 by default;"""

    @RenderResolutionScale.setter
    def RenderResolutionScale(self, arg: float, /) -> None: ...

    @property
    def ShadowMapResolution(self) -> int:
        """shadow texture map resolution, 1024 by default"""

    @ShadowMapResolution.setter
    def ShadowMapResolution(self, arg: int, /) -> None: ...

    @property
    def ShadowMapBias(self) -> float:
        """shadowmap bias, 0.005 by default;"""

    @ShadowMapBias.setter
    def ShadowMapBias(self, arg: float, /) -> None: ...

    @property
    def ToEnableDepthPrepass(self) -> bool:
        """enables/disables depth pre-pass, False by default"""

    @ToEnableDepthPrepass.setter
    def ToEnableDepthPrepass(self, arg: bool, /) -> None: ...

    @property
    def ToEnableAlphaToCoverage(self) -> bool:
        """enables/disables alpha to coverage, True by default"""

    @ToEnableAlphaToCoverage.setter
    def ToEnableAlphaToCoverage(self, arg: bool, /) -> None: ...

    @property
    def IsGlobalIlluminationEnabled(self) -> bool:
        """enables/disables global illumination effects (path tracing)"""

    @IsGlobalIlluminationEnabled.setter
    def IsGlobalIlluminationEnabled(self, arg: bool, /) -> None: ...

    @property
    def SamplesPerPixel(self) -> int:
        """number of samples per pixel (SPP)"""

    @SamplesPerPixel.setter
    def SamplesPerPixel(self, arg: int, /) -> None: ...

    @property
    def RaytracingDepth(self) -> int:
        """maximum ray-tracing depth, 3 by default"""

    @RaytracingDepth.setter
    def RaytracingDepth(self, arg: int, /) -> None: ...

    @property
    def IsShadowEnabled(self) -> bool:
        """enables/disables shadows rendering, True by default"""

    @IsShadowEnabled.setter
    def IsShadowEnabled(self, arg: bool, /) -> None: ...

    @property
    def IsReflectionEnabled(self) -> bool:
        """enables/disables specular reflections, False by default"""

    @IsReflectionEnabled.setter
    def IsReflectionEnabled(self, arg: bool, /) -> None: ...

    @property
    def IsAntialiasingEnabled(self) -> bool:
        """enables/disables adaptive anti-aliasing, False by default"""

    @IsAntialiasingEnabled.setter
    def IsAntialiasingEnabled(self, arg: bool, /) -> None: ...

    @property
    def IsTransparentShadowEnabled(self) -> bool:
        """
        enables/disables light propagation through transparent media, False by default
        """

    @IsTransparentShadowEnabled.setter
    def IsTransparentShadowEnabled(self, arg: bool, /) -> None: ...

    @property
    def UseEnvironmentMapBackground(self) -> bool:
        """enables/disables environment map background"""

    @UseEnvironmentMapBackground.setter
    def UseEnvironmentMapBackground(self, arg: bool, /) -> None: ...

    @property
    def ToIgnoreNormalMapInRayTracing(self) -> bool:
        """
        enables/disables normal map ignoring during path tracing; FALSE by default
        """

    @ToIgnoreNormalMapInRayTracing.setter
    def ToIgnoreNormalMapInRayTracing(self, arg: bool, /) -> None: ...

    @property
    def CoherentPathTracingMode(self) -> bool:
        """
        enables/disables 'coherent' tracing mode (single RNG seed within 16x16 image blocks)
        """

    @CoherentPathTracingMode.setter
    def CoherentPathTracingMode(self, arg: bool, /) -> None: ...

    @property
    def AdaptiveScreenSampling(self) -> bool:
        """
        enables/disables adaptive screen sampling mode for path tracing, FALSE by default
        """

    @AdaptiveScreenSampling.setter
    def AdaptiveScreenSampling(self, arg: bool, /) -> None: ...

    @property
    def AdaptiveScreenSamplingAtomic(self) -> bool:
        """
        enables/disables usage of atomic float operations within adaptive screen sampling, FALSE by default
        """

    @AdaptiveScreenSamplingAtomic.setter
    def AdaptiveScreenSamplingAtomic(self, arg: bool, /) -> None: ...

    @property
    def ShowSamplingTiles(self) -> bool:
        """
        enables/disables debug mode for adaptive screen sampling, FALSE by default
        """

    @ShowSamplingTiles.setter
    def ShowSamplingTiles(self, arg: bool, /) -> None: ...

    @property
    def TwoSidedBsdfModels(self) -> bool:
        """
        forces path tracing to use two-sided versions of original one-sided scattering models
        """

    @TwoSidedBsdfModels.setter
    def TwoSidedBsdfModels(self, arg: bool, /) -> None: ...

    @property
    def RadianceClampingValue(self) -> float:
        """maximum radiance value used for clamping radiance estimation."""

    @RadianceClampingValue.setter
    def RadianceClampingValue(self, arg: float, /) -> None: ...

    @property
    def RebuildRayTracingShaders(self) -> bool:
        """forces rebuilding ray tracing shaders at the next frame"""

    @RebuildRayTracingShaders.setter
    def RebuildRayTracingShaders(self, arg: bool, /) -> None: ...

    @property
    def RayTracingTileSize(self) -> int:
        """
        screen tile size, 32 by default (adaptive sampling mode of path tracing);
        """

    @RayTracingTileSize.setter
    def RayTracingTileSize(self, arg: int, /) -> None: ...

    @property
    def NbRayTracingTiles(self) -> int:
        """
        maximum number of screen tiles per frame, 256 by default (adaptive sampling mode of path tracing);
        """

    @NbRayTracingTiles.setter
    def NbRayTracingTiles(self, arg: int, /) -> None: ...

    @property
    def CameraApertureRadius(self) -> float:
        """
        aperture radius of perspective camera used for depth-of-field, 0.0 by default (no DOF) (path tracing only)
        """

    @CameraApertureRadius.setter
    def CameraApertureRadius(self, arg: float, /) -> None: ...

    @property
    def CameraFocalPlaneDist(self) -> float:
        """
        focal  distance of perspective camera used for depth-of field, 1.0 by default (path tracing only)
        """

    @CameraFocalPlaneDist.setter
    def CameraFocalPlaneDist(self, arg: float, /) -> None: ...

    @property
    def FrustumCullingState(self) -> Graphic3d_RenderingParams.FrustumCulling:
        """state of frustum culling optimization; FrustumCulling_On by default"""

    @FrustumCullingState.setter
    def FrustumCullingState(self, arg: Graphic3d_RenderingParams.FrustumCulling, /) -> None: ...

    @property
    def ToneMappingMethod(self) -> Graphic3d_ToneMappingMethod:
        """
        specifies tone mapping method for path tracing, Graphic3d_ToneMappingMethod_Disabled by default
        """

    @ToneMappingMethod.setter
    def ToneMappingMethod(self, arg: Graphic3d_ToneMappingMethod, /) -> None: ...

    @property
    def Exposure(self) -> float:
        """exposure value used for tone mapping (path tracing), 0.0 by default"""

    @Exposure.setter
    def Exposure(self, arg: float, /) -> None: ...

    @property
    def WhitePoint(self) -> float:
        """
        white point value used in filmic tone mapping (path tracing), 1.0 by default
        """

    @WhitePoint.setter
    def WhitePoint(self, arg: float, /) -> None: ...

    @property
    def StereoMode(self) -> Graphic3d_StereoMode:
        """stereoscopic output mode, Graphic3d_StereoMode_QuadBuffer by default"""

    @StereoMode.setter
    def StereoMode(self, arg: Graphic3d_StereoMode, /) -> None: ...

    @property
    def HmdFov2d(self) -> float:
        """
        sharp field of view range in degrees for displaying on-screen 2D elements, 30.0 by default;
        """

    @HmdFov2d.setter
    def HmdFov2d(self, arg: float, /) -> None: ...

    @property
    def AnaglyphFilter(self) -> Graphic3d_RenderingParams.Anaglyph:
        """filter for anaglyph output, Anaglyph_RedCyan_Optimized by default"""

    @AnaglyphFilter.setter
    def AnaglyphFilter(self, arg: Graphic3d_RenderingParams.Anaglyph, /) -> None: ...

    @property
    def AnaglyphLeft(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        left  anaglyph filter (in normalized colorspace), Color = AnaglyphRight * theColorRight + AnaglyphLeft * theColorLeft;
        """

    @AnaglyphLeft.setter
    def AnaglyphLeft(self, arg: nanoocp.BVH.BVH_Mat4f, /) -> None: ...

    @property
    def AnaglyphRight(self) -> nanoocp.BVH.BVH_Mat4f:
        """
        right anaglyph filter (in normalized colorspace), Color = AnaglyphRight * theColorRight + AnaglyphLeft * theColorLeft;
        """

    @AnaglyphRight.setter
    def AnaglyphRight(self, arg: nanoocp.BVH.BVH_Mat4f, /) -> None: ...

    @property
    def ToReverseStereo(self) -> bool:
        """flag to reverse stereo pair, FALSE by default"""

    @ToReverseStereo.setter
    def ToReverseStereo(self, arg: bool, /) -> None: ...

    @property
    def ToSmoothInterlacing(self) -> bool:
        """
        flag to smooth output on interlaced displays (improves text readability / reduces line aliasing), TRUE by default
        """

    @ToSmoothInterlacing.setter
    def ToSmoothInterlacing(self, arg: bool, /) -> None: ...

    @property
    def ToMirrorComposer(self) -> bool:
        """
        if output device is an external composer - mirror rendering results in window in addition to sending frame to composer, TRUE by default
        """

    @ToMirrorComposer.setter
    def ToMirrorComposer(self, arg: bool, /) -> None: ...

    @property
    def StatsPosition(self) -> Graphic3d_TransformPers:
        """location of stats, upper-left position by default"""

    @StatsPosition.setter
    def StatsPosition(self, arg: Graphic3d_TransformPers, /) -> None: ...

    @property
    def ChartPosition(self) -> Graphic3d_TransformPers:
        """location of stats chart, upper-right position by default"""

    @ChartPosition.setter
    def ChartPosition(self, arg: Graphic3d_TransformPers, /) -> None: ...

    @property
    def ChartSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """
        chart size in pixels, (-1, -1) by default which means that chart will occupy a portion of viewport
        """

    @ChartSize.setter
    def ChartSize(self, arg: nanoocp.BVH.BVH_Vec2i, /) -> None: ...

    @property
    def StatsTextAspect(self) -> Graphic3d_AspectText3d:
        """stats text aspect"""

    @StatsTextAspect.setter
    def StatsTextAspect(self, arg: Graphic3d_AspectText3d, /) -> None: ...

    @property
    def StatsUpdateInterval(self) -> float:
        """time interval between stats updates in seconds, 1.0 second by default;"""

    @StatsUpdateInterval.setter
    def StatsUpdateInterval(self, arg: float, /) -> None: ...

    @property
    def StatsTextHeight(self) -> int:
        """stats text size; 16 by default"""

    @StatsTextHeight.setter
    def StatsTextHeight(self, arg: int, /) -> None: ...

    @property
    def StatsNbFrames(self) -> int:
        """number of data frames to collect history; 1 by default"""

    @StatsNbFrames.setter
    def StatsNbFrames(self, arg: int, /) -> None: ...

    @property
    def StatsMaxChartTime(self) -> float:
        """
        upper time limit within frame chart in seconds; 0.1 seconds by default (100 ms or 10 FPS)
        """

    @StatsMaxChartTime.setter
    def StatsMaxChartTime(self, arg: float, /) -> None: ...

    @property
    def CollectedStats(self) -> Graphic3d_RenderingParams.PerfCounters:
        """performance counters to collect, PerfCounters_Basic by default;"""

    @CollectedStats.setter
    def CollectedStats(self, arg: Graphic3d_RenderingParams.PerfCounters, /) -> None: ...

    @property
    def ToShowStats(self) -> bool:
        """display performance statistics, FALSE by default;"""

    @ToShowStats.setter
    def ToShowStats(self, arg: bool, /) -> None: ...

class Graphic3d_Structure(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition a graphic object.
    This graphic structure can be displayed, erased, or highlighted.
    This graphic structure can be connected with another graphic structure.
    """

    @overload
    def __init__(self, theManager: Graphic3d_StructureManager | None, theLinkPrs: Graphic3d_Structure | None = None) -> None:
        """
        Creates a graphic object in the manager theManager.
        It will appear in all the views of the visualiser.
        The structure is not displayed when it is created.
        @param theManager structure manager holding this structure
        @param theLinkPrs another structure for creating a shadow (linked) structure
        """

    @overload
    def __init__(self, theOther: Graphic3d_Structure) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Clear(self, WithDestruction: bool = True) -> None:
        """
        if WithDestruction == true then
        suppress all the groups of primitives in the structure.
        and it is mandatory to create a new group in <me>.
        if WithDestruction == false then
        clears all the groups of primitives in the structure.
        and all the groups are conserved and empty.
        They will be erased at the next screen update.
        The structure itself is conserved.
        The transformation and the attributes of <me> are conserved.
        The childs of <me> are conserved.
        """

    def Display(self) -> None:
        """Displays the structure <me> in all the views of the visualiser."""

    def DisplayPriority(self) -> Graphic3d_DisplayPriority:
        """Returns the current display priority for this structure."""

    @overload
    def SetDisplayPriority(self, thePriority: Graphic3d_DisplayPriority) -> None:
        """
        Modifies the order of displaying the structure.
        Values are between 0 and 10.
        Structures are drawn according to their display priorities in ascending order.
        A structure of priority 10 is displayed the last and appears over the others.
        The default value is 5.
        Warning: If structure is displayed then the SetDisplayPriority method erases it and displays
        with the new priority. Raises Graphic3d_PriorityDefinitionError if Priority is greater than 10
        or a negative value.
        """

    @overload
    def SetDisplayPriority(self, thePriority: int) -> None:
        """
        Deprecated in OCCT: Deprecated since OCCT7.7, Graphic3d_DisplayPriority should be passed instead of integer number to SetDisplayPriority()
        """

    def ResetDisplayPriority(self) -> None:
        """
        Reset the current priority of the structure to the previous priority.
        Warning: If structure is displayed then the SetDisplayPriority() method erases it and displays
        with the previous priority.
        """

    def Erase(self) -> None:
        """Erases this structure in all the views of the visualiser."""

    def Highlight(self, theStyle: Graphic3d_PresentationAttributes | None, theToUpdateMgr: bool = True) -> None:
        """
        Highlights the structure in all the views with the given style
        @param[in] theStyle  the style (type of highlighting: box/color, color and opacity)
        @param[in] theToUpdateMgr  defines whether related computed structures will be
        highlighted via structure manager or not
        """

    @overload
    def Remove(self) -> None:
        """
        Suppress the structure <me>.
        It will be erased at the next screen update.
        Warning: No more graphic operations in <me> after this call.
        Category: Methods to modify the class definition
        """

    @overload
    def Remove(self, thePrs: Graphic3d_Structure | None) -> None:
        """Deprecated in OCCT: Deprecated alias for Disconnect()"""

    @overload
    def Remove(self, thePtr: Graphic3d_Structure, theType: Graphic3d_TypeOfConnection) -> None:
        """
        Suppress the structure in the list of descendants or in the list of ancestors.
        """

    def CalculateBoundBox(self) -> None:
        """Computes axis-aligned bounding box of a structure."""

    def SetInfiniteState(self, theToSet: bool) -> None:
        """
        Sets infinite flag.
        When TRUE, the MinMaxValues method returns:
        theXMin = theYMin = theZMin = RealFirst().
        theXMax = theYMax = theZMax = RealLast().
        By default, structure is created not infinite but empty.
        """

    def SetZLayer(self, theLayerId: int) -> None:
        """
        Set Z layer ID for the structure. The Z layer mechanism
        allows to display structures presented in higher layers in overlay
        of structures in lower layers by switching off z buffer depth
        test between layers
        """

    def GetZLayer(self) -> int:
        """
        Get Z layer ID of displayed structure.
        The method returns -1 if the structure has no ID (deleted from graphic driver).
        """

    def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane | None) -> None:
        """
        Changes a sequence of clip planes slicing the structure on rendering.
        @param[in] thePlanes  the set of clip planes.
        """

    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane:
        """
        Get clip planes slicing the structure on rendering.
        @return set of clip planes.
        """

    def SetVisible(self, AValue: bool) -> None:
        """
        Modifies the visibility indicator to true or
        false for the structure <me>.
        The default value at the definition of <me> is
        true.
        """

    def SetVisual(self, AVisual: Graphic3d_TypeOfStructure) -> None:
        """Modifies the visualisation mode for the structure <me>."""

    def SetZoomLimit(self, LimitInf: float, LimitSup: float) -> None:
        """
        Modifies the minimum and maximum zoom coefficients
        for the structure <me>.
        The default value at the definition of <me> is unlimited.
        Category: Methods to modify the class definition
        Warning: Raises StructureDefinitionError if <LimitInf> is
        greater than <LimitSup> or if <LimitInf> or
        <LimitSup> is a negative value.
        """

    def SetIsForHighlight(self, isForHighlight: bool) -> None:
        """
        Marks the structure <me> representing wired structure needed for highlight only so it won't be
        added to BVH tree.
        """

    def UnHighlight(self) -> None:
        """
        Suppresses the highlight for the structure <me>
        in all the views of the visualiser.
        """

    def Compute(self) -> None: ...

    def computeHLR(self, theProjector: Graphic3d_Camera | None) -> Graphic3d_Structure:
        """Returns the new Structure defined for the new visualization"""

    def RecomputeTransformation(self, theProjector: Graphic3d_Camera | None) -> None:
        """Calculates structure transformation for specific camera position"""

    @overload
    def ReCompute(self) -> None:
        """
        Forces a new construction of the structure <me>
        if <me> is displayed and TOS_COMPUTED.
        """

    @overload
    def ReCompute(self, aProjector: Graphic3d_DataStructureManager | None) -> None:
        """
        Forces a new construction of the structure <me>
        if <me> is displayed in <aProjetor> and TOS_COMPUTED.
        """

    def Groups(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_Group]:
        """Returns the groups sequence included in this structure."""

    def NumberOfGroups(self) -> int:
        """Returns the current number of groups in this structure."""

    def NewGroup(self) -> Graphic3d_Group:
        """Append new group to this structure."""

    def CurrentGroup(self) -> Graphic3d_Group:
        """Returns the last created group or creates new one if list is empty."""

    def HighlightStyle(self) -> Graphic3d_PresentationAttributes:
        """Returns the highlight attributes."""

    def IsDeleted(self) -> bool:
        """Returns TRUE if this structure is deleted (after Remove() call)."""

    def IsDisplayed(self) -> bool:
        """Returns the display indicator for this structure."""

    def IsEmpty(self) -> bool:
        """
        Returns true if the structure <me> is empty.
        Warning: A structure is empty if :
        it do not have group or all the groups are empties
        and it do not have descendant or all the descendants
        are empties.
        """

    def IsInfinite(self) -> bool:
        """Returns true if the structure <me> is infinite."""

    def IsHighlighted(self) -> bool:
        """Returns the highlight indicator for this structure."""

    def IsTransformed(self) -> bool:
        """Returns TRUE if the structure is transformed."""

    def IsVisible(self) -> bool:
        """Returns the visibility indicator for this structure."""

    def MinMaxValues(self, theToIgnoreInfiniteFlag: bool = False) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns the coordinates of the boundary box of the structure <me>.
        If <theToIgnoreInfiniteFlag> is TRUE, the method returns actual graphical
        boundaries of the Graphic3d_Group components. Otherwise, the
        method returns boundaries taking into account infinite state
        of the structure. This approach generally used for application
        specific fit operation (e.g. fitting the model into screen,
        not taking into account infinite helper elements).
        Warning: If the structure <me> is empty then the empty box is returned,
        If the structure <me> is infinite then the whole box is returned.
        """

    def Visual(self) -> Graphic3d_TypeOfStructure:
        """Returns the visualisation mode for the structure <me>."""

    @staticmethod
    def AcceptConnection(theStructure1: Graphic3d_Structure, theStructure2: Graphic3d_Structure, theType: Graphic3d_TypeOfConnection) -> bool:
        """
        Returns true if the connection is possible between
        <AStructure1> and <AStructure2> without a creation
        of a cycle.

        It's not possible to call the method
        AStructure1->Connect (AStructure2, TypeOfConnection)
        if
        - the set of all ancestors of <AStructure1> contains
        <AStructure1> and if the
        TypeOfConnection == TOC_DESCENDANT
        - the set of all descendants of <AStructure1> contains
        <AStructure2> and if the
        TypeOfConnection == TOC_ANCESTOR
        """

    def Ancestors(self, SG: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure]) -> None:
        """Returns the group of structures to which <me> is connected."""

    @overload
    def Connect(self, theStructure: Graphic3d_Structure, theType: Graphic3d_TypeOfConnection, theWithCheck: bool = False) -> None:
        """
        If Atype is TOC_DESCENDANT then add <AStructure>
        as a child structure of <me>.
        If Atype is TOC_ANCESTOR then add <AStructure>
        as a parent structure of <me>.
        The connection propagates Display, Highlight, Erase,
        Remove, and stacks the transformations.
        No connection if the graph of the structures
        contains a cycle and <WithCheck> is true;
        """

    @overload
    def Connect(self, thePrs: Graphic3d_Structure | None) -> None:
        """Deprecated in OCCT: Deprecated short-cut"""

    def Descendants(self, SG: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure]) -> None:
        """Returns the group of structures connected to <me>."""

    def Disconnect(self, theStructure: Graphic3d_Structure) -> None:
        """Suppress the connection between <AStructure> and <me>."""

    def DisconnectAll(self, AType: Graphic3d_TypeOfConnection) -> None:
        """
        If Atype is TOC_DESCENDANT then suppress all
        the connections with the child structures of <me>.
        If Atype is TOC_ANCESTOR then suppress all
        the connections with the parent structures of <me>.
        """

    def RemoveAll(self) -> None:
        """Deprecated in OCCT: Deprecated alias for DisconnectAll()"""

    @staticmethod
    def Network(theStructure: Graphic3d_Structure, theType: Graphic3d_TypeOfConnection, theSet: "NCollection_Map<Graphic3d_Structure*, NCollection_DefaultHasher<Graphic3d_Structure*>>") -> None:
        """
        Returns <ASet> the group of structures :
        - directly or indirectly connected to <AStructure> if the
        TypeOfConnection == TOC_DESCENDANT
        - to which <AStructure> is directly or indirectly connected
        if the TypeOfConnection == TOC_ANCESTOR
        """

    def SetHLRValidation(self, theFlag: bool) -> None: ...

    def HLRValidation(self) -> bool:
        """
        Hidden parts stored in this structure are valid if:
        1) the owner is defined.
        2) they are not invalid.
        """

    def Transformation(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """Return local transformation."""

    def SetTransformation(self, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """Modifies the current local transformation"""

    def SetTransformPersistence(self, theTrsfPers: Graphic3d_TransformPers | None) -> None:
        """Modifies the current transform persistence (pan, zoom or rotate)"""

    def TransformPersistence(self) -> Graphic3d_TransformPers:
        """@return transform persistence of the presentable object."""

    def SetMutable(self, theIsMutable: bool) -> None:
        """
        Sets if the structure location has mutable nature (content or location will be changed
        regularly).
        """

    def IsMutable(self) -> bool:
        """
        Returns true if structure has mutable nature (content or location are be changed regularly).
        Mutable structure will be managed in different way than static ones.
        """

    def ComputeVisual(self) -> Graphic3d_TypeOfStructure: ...

    def GraphicClear(self, WithDestruction: bool) -> None:
        """Clears the structure <me>."""

    def GraphicConnect(self, theDaughter: Graphic3d_Structure | None) -> None: ...

    def GraphicDisconnect(self, theDaughter: Graphic3d_Structure | None) -> None: ...

    def GraphicTransform(self, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """
        Internal method which sets new transformation without calling graphic manager callbacks.
        """

    def Identification(self) -> int:
        """Returns the identification number of this structure."""

    @staticmethod
    def PrintNetwork(AStructure: Graphic3d_Structure | None, AType: Graphic3d_TypeOfConnection) -> None:
        """
        Prints information about the network associated
        with the structure <AStructure>.
        """

    def SetComputeVisual(self, theVisual: Graphic3d_TypeOfStructure) -> None: ...

    def CStructure(self) -> Graphic3d_CStructure:
        """Returns the low-level structure"""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_TextureEnv(Graphic3d_TextureRoot):
    """This class provides environment texture."""

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates an environment texture from a file."""

    @overload
    def __init__(self, theName: Graphic3d_NameOfTextureEnv) -> None:
        """Creates an environment texture from a predefined texture name set."""

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """Creates an environment texture from the pixmap."""

    @overload
    def __init__(self, theOther: Graphic3d_TextureEnv) -> None: ...

    def Name(self) -> Graphic3d_NameOfTextureEnv:
        """
        Returns the name of the predefined textures or NOT_ENV_UNKNOWN
        when the name is given as a filename.
        """

    @staticmethod
    def NumberOfTextures() -> int:
        """Returns the number of predefined textures."""

    @staticmethod
    def TextureName(theRank: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the predefined texture of rank <aRank>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_LightSet(nanoocp.Standard.Standard_Transient):
    """Class defining the set of light sources."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_LightSet) -> None: ...

    class IterationFilter(enum.IntEnum):
        """Iteration filter flags."""

        IterationFilter_None = 0

        IterationFilter_ExcludeAmbient = 2

        IterationFilter_ExcludeDisabled = 4

        IterationFilter_ExcludeNoShadow = 8

        IterationFilter_ExcludeDisabledAndAmbient = 6

        IterationFilter_ActiveShadowCasters = 14

    IterationFilter_None: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_None

    IterationFilter_ExcludeAmbient: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_ExcludeAmbient

    IterationFilter_ExcludeDisabled: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_ExcludeDisabled

    IterationFilter_ExcludeNoShadow: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_ExcludeNoShadow

    IterationFilter_ExcludeDisabledAndAmbient: Graphic3d_LightSet.IterationFilter = ...

    IterationFilter_ActiveShadowCasters: Graphic3d_LightSet.IterationFilter = ...

    class Iterator:
        """Iterator through light sources."""

        @overload
        def __init__(self) -> None:
            """Empty constructor."""

        @overload
        def __init__(self, theSet: Graphic3d_LightSet, theFilter: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_None) -> None: ...

        @overload
        def __init__(self, theSet: Graphic3d_LightSet | None, theFilter: Graphic3d_LightSet.IterationFilter = IterationFilter.IterationFilter_None) -> None:
            """Constructor with initialization."""

        @overload
        def __init__(self, theOther: Graphic3d_LightSet.Iterator) -> None: ...

        def __iter__(self) -> Graphic3d_LightSet.Iterator:
            """
            Python addition: iterate with More()/Next(), yielding Value() (or Current()); the object is its own iterator.
            """

        def __next__(self) -> Graphic3d_CLight:
            """Python addition: see __iter__."""

        def More(self) -> bool:
            """Returns TRUE if iterator points to a valid item."""

        def Value(self) -> Graphic3d_CLight:
            """Returns current item."""

        def Next(self) -> None:
            """Moves to the next item."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Lower(self) -> int:
        """Return lower light index."""

    def Upper(self) -> int:
        """Return upper light index."""

    def IsEmpty(self) -> bool:
        """Return TRUE if lights list is empty."""

    def Extent(self) -> int:
        """Return number of light sources."""

    def Value(self, theIndex: int) -> Graphic3d_CLight:
        """
        Return the light source for specified index within range [Lower(), Upper()].
        """

    def Contains(self, theLight: Graphic3d_CLight | None) -> bool:
        """Return TRUE if light source is defined in this set."""

    def Add(self, theLight: Graphic3d_CLight | None) -> bool:
        """Append new light source."""

    def Remove(self, theLight: Graphic3d_CLight | None) -> bool:
        """Remove light source."""

    def NbLightsOfType(self, theType: Graphic3d_TypeOfLightSource) -> int:
        """Returns total amount of lights of specified type."""

    def UpdateRevision(self) -> int:
        """Update light sources revision."""

    def Revision(self) -> int:
        """
        Return light sources revision.
        @sa UpdateRevision()
        """

    def NbEnabled(self) -> int:
        """
        Returns total amount of enabled lights EXCLUDING ambient.
        @sa UpdateRevision()
        """

    def NbEnabledLightsOfType(self, theType: Graphic3d_TypeOfLightSource) -> int:
        """
        Returns total amount of enabled lights of specified type.
        @sa UpdateRevision()
        """

    def NbCastShadows(self) -> int:
        """
        Returns total amount of enabled lights castings shadows.
        @sa UpdateRevision()
        """

    def AmbientColor(self) -> nanoocp.Quantity.NCollection_Vec4__float:
        """
        Returns cumulative ambient color, which is computed as sum of all enabled ambient light
        sources. Values are NOT clamped (can be greater than 1.0f) and alpha component is fixed
        to 1.0f.
        @sa UpdateRevision()
        """

    def KeyEnabledLong(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a string defining a list of enabled light sources as concatenation of letters 'd'
        (Directional), 'p' (Point), 's' (Spot) depending on the type of light source in the list.
        Example: "dppp".
        @sa UpdateRevision()
        """

    def KeyEnabledShort(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a string defining a list of enabled light sources as concatenation of letters 'd'
        (Directional), 'p' (Point), 's' (Spot) depending on the type of light source in the list,
        specified only once. Example: "dp".
        @sa UpdateRevision()
        """

class Graphic3d_ZLayerSettings:
    """Structure defines list of ZLayer properties."""

    @overload
    def __init__(self) -> None:
        """Default settings."""

    @overload
    def __init__(self, theOther: Graphic3d_ZLayerSettings) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return user-provided name."""

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Set custom name."""

    def Lights(self) -> Graphic3d_LightSet:
        """
        Return lights list to be used for rendering presentations within this Z-Layer; NULL by
        default. NULL list (but not empty list!) means that default lights assigned to the View should
        be used instead of per-layer lights.
        """

    def SetLights(self, theLights: Graphic3d_LightSet | None) -> None:
        """Assign lights list to be used."""

    def Origin(self) -> nanoocp.gp.gp_XYZ:
        """Return the origin of all objects within the layer."""

    def OriginTransformation(self) -> nanoocp.TopLoc.TopLoc_Datum3D:
        """Return the transformation to the origin."""

    def SetOrigin(self, theOrigin: nanoocp.gp.gp_XYZ) -> None:
        """Set the origin of all objects within the layer."""

    def HasCullingDistance(self) -> bool:
        """
        Return TRUE, if culling of distant objects (distance culling) should be performed; FALSE by
        default.
        @sa CullingDistance()
        """

    def CullingDistance(self) -> float:
        """
        Return the distance to discard drawing of distant objects (distance from camera Eye point); by
        default it is Infinite (distance culling is disabled). Since camera eye definition has no
        strong meaning within orthographic projection, option is considered only within perspective
        projection. Note also that this option has effect only when frustum culling is enabled.
        """

    def SetCullingDistance(self, theDistance: float) -> None:
        """Set the distance to discard drawing objects."""

    def HasCullingSize(self) -> bool:
        """
        Return TRUE, if culling of small objects (size culling) should be performed; FALSE by default.
        @sa CullingSize()
        """

    def CullingSize(self) -> float:
        """
        Return the size to discard drawing of small objects; by default it is Infinite (size culling
        is disabled). Current implementation checks the length of projected diagonal of bounding box
        in pixels for discarding. Note that this option has effect only when frustum culling is
        enabled.
        """

    def SetCullingSize(self, theSize: float) -> None:
        """Set the distance to discard drawing objects."""

    def IsImmediate(self) -> bool:
        """
        Return true if this layer should be drawn after all normal (non-immediate) layers.
        """

    def SetImmediate(self, theValue: bool) -> None:
        """
        Set the flag indicating the immediate layer, which should be drawn after all normal
        (non-immediate) layers.
        """

    def IsRaytracable(self) -> bool:
        """
        Returns TRUE if layer should be processed by ray-tracing renderer; TRUE by default.
        Note that this flag is IGNORED for layers with IsImmediate() flag.
        """

    def SetRaytracable(self, theToRaytrace: bool) -> None:
        """Sets if layer should be processed by ray-tracing renderer."""

    def UseEnvironmentTexture(self) -> bool:
        """
        Return flag to allow/prevent environment texture mapping usage for specific layer.
        """

    def SetEnvironmentTexture(self, theValue: bool) -> None:
        """
        Set the flag to allow/prevent environment texture mapping usage for specific layer.
        """

    def ToEnableDepthTest(self) -> bool:
        """Return true if depth test should be enabled."""

    def SetEnableDepthTest(self, theValue: bool) -> None:
        """Set if depth test should be enabled."""

    def ToEnableDepthWrite(self) -> bool:
        """Return true depth values should be written during rendering."""

    def SetEnableDepthWrite(self, theValue: bool) -> None:
        """Set if depth values should be written during rendering."""

    def ToClearDepth(self) -> bool:
        """
        Return true if depth values should be cleared before drawing the layer.
        """

    def SetClearDepth(self, theValue: bool) -> None:
        """Set if depth values should be cleared before drawing the layer."""

    def ToRenderInDepthPrepass(self) -> bool:
        """
        Return TRUE if layer should be rendered within depth pre-pass; TRUE by default.
        """

    def SetRenderInDepthPrepass(self, theToRender: bool) -> None:
        """Set if layer should be rendered within depth pre-pass."""

    def PolygonOffset(self) -> Graphic3d_PolygonOffset:
        """Return glPolygonOffset() arguments."""

    def SetPolygonOffset(self, theParams: Graphic3d_PolygonOffset) -> None:
        """Setup glPolygonOffset() arguments."""

    def ChangePolygonOffset(self) -> Graphic3d_PolygonOffset:
        """Modify glPolygonOffset() arguments."""

    def SetDepthOffsetPositive(self) -> None:
        """Sets minimal possible positive depth offset."""

    def SetDepthOffsetNegative(self) -> None:
        """Sets minimal possible negative depth offset."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_CView(Graphic3d_DataStructureManager):
    """
    Base class of a graphical view that carries out rendering process for a concrete
    implementation of graphical driver. Provides virtual interfaces for redrawing its
    contents, management of displayed structures and render settings. The source code
    of the class itself implements functionality related to management of
    computed (HLR or "view-dependent") structures.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Identification(self) -> int:
        """Returns the identification number of the view."""

    def Activate(self) -> None:
        """
        Activates the view. Maps presentations defined within structure manager onto this view.
        """

    def Deactivate(self) -> None:
        """
        Deactivates the view. Unmaps presentations defined within structure manager.
        The view in deactivated state will ignore actions on structures such as Display().
        """

    def IsActive(self) -> bool:
        """Returns the activity flag of the view."""

    def Remove(self) -> None:
        """
        Erases the view and removes from graphic driver.
        No more graphic operations are allowed in this view after the call.
        """

    def IsRemoved(self) -> bool:
        """Returns true if the view was removed."""

    def Camera(self) -> Graphic3d_Camera:
        """Returns camera object of the view."""

    def SetCamera(self, theCamera: Graphic3d_Camera | None) -> None:
        """Sets camera used by the view."""

    def ToFlipOutput(self) -> bool:
        """Returns necessity to flip OY in projection matrix"""

    def SetToFlipOutput(self, arg0: bool) -> None:
        """Sets state of flip OY necessity in projection matrix"""

    def ShadingModel(self) -> Graphic3d_TypeOfShadingModel:
        """
        Returns default Shading Model of the view; Graphic3d_TypeOfShadingModel_Phong by default.
        """

    def SetShadingModel(self, theModel: Graphic3d_TypeOfShadingModel) -> None:
        """
        Sets default Shading Model of the view.
        Will throw an exception on attempt to set Graphic3d_TypeOfShadingModel_DEFAULT.
        """

    def BackfacingModel(self) -> Graphic3d_TypeOfBackfacingModel:
        """
        Return backfacing model used for the view; Graphic3d_TypeOfBackfacingModel_Auto by default,
        which means that backface culling is defined by each presentation.
        """

    def SetBackfacingModel(self, theModel: Graphic3d_TypeOfBackfacingModel) -> None:
        """Sets backfacing model for the view."""

    def VisualizationType(self) -> Graphic3d_TypeOfVisualization:
        """Returns visualization type of the view."""

    def SetVisualizationType(self, theType: Graphic3d_TypeOfVisualization) -> None:
        """Sets visualization type of the view."""

    def ZLayerTarget(self) -> int:
        """Returns ZLayerId target"""

    def SetZLayerTarget(self, theTarget: int) -> None:
        """Sets ZLayerId target."""

    def ZLayerRedrawMode(self) -> bool:
        """Returns ZLayerId redraw mode"""

    def SetZLayerRedrawMode(self, theMode: bool) -> None:
        """Sets ZLayerId redraw mode."""

    def SetComputedMode(self, theMode: bool) -> None:
        """Switches computed HLR mode in the view"""

    def ComputedMode(self) -> bool:
        """Returns the computed HLR mode state"""

    def ReCompute(self, theStructure: Graphic3d_Structure | None) -> None:
        """
        Computes the new presentation of the structure  displayed in this view with the type
        Graphic3d_TOS_COMPUTED.
        """

    def Update(self, theLayerId: int = -1) -> None:
        """Invalidates bounding box of specified ZLayerId."""

    def Compute(self) -> None:
        """
        Computes the new presentation of the structures displayed in this view with the type
        Graphic3d_TOS_COMPUTED.
        """

    def DisplayedStructures(self, theStructures: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure]) -> None:
        """Returns the set of structures displayed in this view."""

    def NumberOfDisplayedStructures(self) -> int:
        """Returns number of displayed structures in the view."""

    def IsComputed(self, theStructId: int) -> tuple[bool, Graphic3d_Structure]:
        """
        Returns true in case if the structure with the given <theStructId> is
        in list of structures to be computed and stores computed struct to <theComputedStruct>.
        """

    @overload
    def MinMaxValues(self, theToIncludeAuxiliary: bool = False) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns the bounding box of all structures displayed in the view.
        If theToIncludeAuxiliary is TRUE, then the boundary box also includes minimum and maximum
        limits of graphical elements forming parts of infinite and other auxiliary structures.
        @param theToIncludeAuxiliary consider also auxiliary presentations (with infinite flag or with
        trihedron transformation persistence)
        @return computed bounding box
        """

    @overload
    def MinMaxValues(self, theSet: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure], theToIncludeAuxiliary: bool = False) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns the coordinates of the boundary box of all structures in the set <theSet>.
        If <theToIgnoreInfiniteFlag> is TRUE, then the boundary box
        also includes minimum and maximum limits of graphical elements
        forming parts of infinite structures.
        """

    def ZFitAllBounds(self, thePrimaryBox: nanoocp.Bnd.Bnd_Box, theGraphicBox: nanoocp.Bnd.Bnd_Box) -> None:
        """Return primary and graphical bounding boxes used by camera Z fitting."""

    def StructureManager(self) -> Graphic3d_StructureManager:
        """
        Returns the structure manager handle which manage structures associated with this view.
        """

    def Redraw(self) -> None:
        """Redraw content of the view."""

    def RedrawImmediate(self) -> None:
        """Redraw immediate content of the view."""

    def Invalidate(self) -> None:
        """Invalidates content of the view but does not redraw it."""

    def IsInvalidated(self) -> bool:
        """Return true if view content cache has been invalidated."""

    def Resized(self) -> None:
        """Handle changing size of the rendering window."""

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
        """Returns the window associated to the view."""

    def IsDefined(self) -> bool:
        """Returns True if the window associated to the view is defined."""

    def BufferDump(self, theImage: nanoocp.Image.Image_PixMap, theBufferType: Graphic3d_BufferType) -> bool:
        """Dump active rendering buffer into specified memory buffer."""

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

    def InsertLayerBefore(self, theNewLayerId: int, theSettings: Graphic3d_ZLayerSettings, theLayerAfter: int) -> None:
        """
        Add a layer to the view.
        @param[in] theNewLayerId  id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings    new layer settings
        @param[in] theLayerAfter  id of layer to append new layer before
        """

    def InsertLayerAfter(self, theNewLayerId: int, theSettings: Graphic3d_ZLayerSettings, theLayerBefore: int) -> None:
        """
        Add a layer to the view.
        @param[in] theNewLayerId   id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings     new layer settings
        @param[in] theLayerBefore  id of layer to append new layer after
        """

    def ZLayerMax(self) -> int:
        """
        Returns the maximum Z layer ID.
        First layer ID is Graphic3d_ZLayerId_Default, last ID is ZLayerMax().
        """

    def Layers(self) -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_Layer]:
        """Returns the list of layers."""

    def Layer(self, theLayerId: int) -> Graphic3d_Layer:
        """Returns layer with given ID or NULL if undefined."""

    def InvalidateZLayerBoundingBox(self, theLayerId: int) -> None:
        """Returns the bounding box of all structures displayed in the Z layer."""

    def RemoveZLayer(self, theLayerId: int) -> None:
        """
        Remove Z layer from the specified view. All structures
        displayed at the moment in layer will be displayed in default layer
        ( the bottom-level z layer ). To unset layer ID from associated
        structures use method UnsetZLayer (...).
        """

    def SetZLayerSettings(self, theLayerId: int, theSettings: Graphic3d_ZLayerSettings) -> None:
        """Sets the settings for a single Z layer of specified view."""

    def ConsiderZoomPersistenceObjects(self) -> float:
        """Returns zoom-scale factor."""

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

    def CopySettings(self, theOther: Graphic3d_CView | None) -> None:
        """
        Copy visualization settings from another view.
        Method is used for cloning views in viewer when its required to create view
        with same view properties.
        """

    def RenderingParams(self) -> Graphic3d_RenderingParams:
        """Returns current rendering parameters and effect settings."""

    def ChangeRenderingParams(self) -> Graphic3d_RenderingParams:
        """Returns reference to current rendering parameters and effect settings."""

    def Background(self) -> nanoocp.Aspect.Aspect_Background:
        """Returns background  fill color."""

    def SetBackground(self, theBackground: nanoocp.Aspect.Aspect_Background) -> None:
        """Sets background fill color."""

    def GradientBackground(self) -> nanoocp.Aspect.Aspect_GradientBackground:
        """Returns gradient background fill colors."""

    def SetGradientBackground(self, theBackground: nanoocp.Aspect.Aspect_GradientBackground) -> None:
        """Sets gradient background fill colors."""

    def BackgroundImage(self) -> Graphic3d_TextureMap:
        """Returns background image texture map."""

    def BackgroundCubeMap(self) -> Graphic3d_CubeMap:
        """Returns cubemap being set last time on background."""

    def IBLCubeMap(self) -> Graphic3d_CubeMap:
        """Returns cubemap being set last time on background."""

    def SetBackgroundImage(self, theTextureMap: Graphic3d_TextureMap | None, theToUpdatePBREnv: bool = True) -> None:
        """
        Sets image texture or environment cubemap as background.
        @param[in] theTextureMap  source to set a background;
        should be either Graphic3d_Texture2D or Graphic3d_CubeMap
        @param[in] theToUpdatePBREnv  defines whether IBL maps will be generated or not
        (see GeneratePBREnvironment())
        """

    def BackgroundImageStyle(self) -> nanoocp.Aspect.Aspect_FillMethod:
        """Returns background image fill style."""

    def SetBackgroundImageStyle(self, theFillStyle: nanoocp.Aspect.Aspect_FillMethod) -> None:
        """Sets background image fill style."""

    def BackgroundType(self) -> Graphic3d_TypeOfBackground:
        """Returns background type."""

    def SetBackgroundType(self, theType: Graphic3d_TypeOfBackground) -> None:
        """Sets background type."""

    def BackgroundSkydome(self) -> nanoocp.Aspect.Aspect_SkydomeBackground:
        """Returns skydome aspect;"""

    def SetBackgroundSkydome(self, theAspect: nanoocp.Aspect.Aspect_SkydomeBackground, theToUpdatePBREnv: bool = True) -> None:
        """Sets skydome aspect"""

    def SetImageBasedLighting(self, theToEnableIBL: bool) -> None:
        """
        Enables or disables IBL (Image Based Lighting) from background cubemap.
        Has no effect if PBR is not used.
        @param[in] theToEnableIBL enable or disable IBL from background cubemap
        """

    def GridDisplay(self, theParams: nanoocp.Aspect.Aspect_GridParams, thePlane: nanoocp.gp.gp_Ax3) -> None:
        """
        Display a shader-rendered grid on the given plane.
        The default implementation is a no-op; drivers with shader support override it.
        @param[in] theParams appearance parameters
        @param[in] thePlane  grid plane in world coordinates (origin + X/Y directions)
        """

    def GridErase(self) -> None:
        """
        Erase the shader-rendered grid.
        The default implementation is a no-op; drivers with shader support override it.
        """

    @overload
    def ShaderGridEcho(self, theX: int, theY: int, thePoint: Graphic3d_Vertex) -> bool:
        """
        Return snapped point for the shader-rendered grid under the window pixel.
        The default implementation is a no-op; drivers with shader grid support override it.
        """

    @overload
    def ShaderGridEcho(self, theX: int, theY: int, thePoint: Graphic3d_Vertex, theDisplayPoint: Graphic3d_Vertex) -> bool:
        """
        Return snapped point and display point for the shader-rendered grid under the window pixel.
        The snapped point is the geometric grid point in world coordinates.
        The display point is a clip-safe proxy projected to the same window position for echo marker
        presentation; it should not be used as the geometric snap result.
        """

    def ShaderGridSnapPoint(self, thePoint: Graphic3d_Vertex, theGridPoint: Graphic3d_Vertex) -> bool:
        """
        Return snapped point for the shader-rendered grid from an arbitrary world point.
        The default implementation is a no-op; drivers with shader grid support override it.
        """

    def TextureEnv(self) -> Graphic3d_TextureEnv:
        """Returns environment texture set for the view."""

    def SetTextureEnv(self, theTextureEnv: Graphic3d_TextureEnv | None) -> None:
        """Sets environment texture for the view."""

    def Lights(self) -> Graphic3d_LightSet:
        """Returns list of lights of the view."""

    def SetLights(self, theLights: Graphic3d_LightSet | None) -> None:
        """Sets list of lights for the view."""

    def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane:
        """Returns list of clip planes set for the view."""

    def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane | None) -> None:
        """Sets list of clip planes for the view."""

    def DiagnosticInformation(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theFlags: Graphic3d_DiagnosticInfo) -> None:
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

    def UnitFactor(self) -> float:
        """
        Return unit scale factor defined as scale factor for m (meters); 1.0 by default.
        Normally, view definition is unitless, however some operations like VR input requires proper
        units mapping.
        """

    def SetUnitFactor(self, theFactor: float) -> None:
        """Set unit scale factor."""

    def XRSession(self) -> nanoocp.Aspect.Aspect_XRSession:
        """Return XR session."""

    def SetXRSession(self, theSession: nanoocp.Aspect.Aspect_XRSession | None) -> None:
        """Set XR session."""

    def IsActiveXR(self) -> bool:
        """Return TRUE if there is active XR session."""

    def InitXR(self) -> bool:
        """Initialize XR session."""

    def ReleaseXR(self) -> None:
        """Release XR session."""

    def ProcessXRInput(self) -> None:
        """Process input."""

    def SetupXRPosedCamera(self) -> None:
        """
        Compute PosedXRCamera() based on current XR head pose and make it active.
        """

    def UnsetXRPosedCamera(self) -> None:
        """
        Set current camera back to BaseXRCamera() and copy temporary modifications of PosedXRCamera().
        Calls SynchronizeXRPosedToBaseCamera() beforehand.
        """

    def PosedXRCamera(self) -> Graphic3d_Camera:
        """
        Returns transient XR camera position with tracked head orientation applied.
        """

    def SetPosedXRCamera(self, theCamera: Graphic3d_Camera | None) -> None:
        """
        Sets transient XR camera position with tracked head orientation applied.
        """

    def BaseXRCamera(self) -> Graphic3d_Camera:
        """Returns anchor camera definition (without tracked head orientation)."""

    def SetBaseXRCamera(self, theCamera: Graphic3d_Camera | None) -> None:
        """Sets anchor camera definition."""

    def PoseXRToWorld(self, thePoseXR: nanoocp.gp.gp_Trsf) -> nanoocp.gp.gp_Trsf:
        """
        Convert XR pose to world space.
        @param[in] thePoseXR  transformation defined in VR local coordinate system,
        oriented as Y-up, X-right and -Z-forward
        @return transformation defining orientation of XR pose in world space
        """

    def ViewAxisInWorld(self, thePoseXR: nanoocp.gp.gp_Trsf) -> nanoocp.gp.gp_Ax1:
        """
        Returns view direction in the world space based on XR pose.
        @param[in] thePoseXR  transformation defined in VR local coordinate system,
        oriented as Y-up, X-right and -Z-forward
        """

    def SynchronizeXRBaseToPosedCamera(self) -> None:
        """
        Recomputes PosedXRCamera() based on BaseXRCamera() and head orientation.
        """

    def SynchronizeXRPosedToBaseCamera(self) -> None:
        """
        Checks if PosedXRCamera() has been modified since SetupXRPosedCamera()
        and copies these modifications to BaseXRCamera().
        """

    def ComputeXRPosedCameraFromBase(self, theCam: Graphic3d_Camera, theXRTrsf: nanoocp.gp.gp_Trsf) -> None:
        """Compute camera position based on XR pose."""

    def ComputeXRBaseCameraFromPosed(self, theCamPosed: Graphic3d_Camera, thePoseTrsf: nanoocp.gp.gp_Trsf) -> None:
        """
        Update based camera from posed camera by applying reversed transformation.
        """

    def TurnViewXRCamera(self, theTrsfTurn: nanoocp.gp.gp_Trsf) -> None:
        """Turn XR camera direction using current (head) eye position as anchor."""

    def GetGraduatedTrihedron(self) -> Graphic3d_GraduatedTrihedron:
        """
        @name obsolete Graduated Trihedron functionality
        Returns data of a graduated trihedron
        """

    def GraduatedTrihedronDisplay(self, theTrihedronData: Graphic3d_GraduatedTrihedron) -> None:
        """Displays Graduated Trihedron."""

    def GraduatedTrihedronErase(self) -> None:
        """Erases Graduated Trihedron."""

    def GraduatedTrihedronMinMaxValues(self, theMin: nanoocp.Quantity.NCollection_Vec3__float, theMax: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Sets minimum and maximum points of scene bounding box for Graduated Trihedron stored in
        graphic view object.
        @param[in] theMin  the minimum point of scene.
        @param[in] theMax  the maximum point of scene.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    def IsSubview(self) -> bool:
        """
        @name subview properties
        Return TRUE if this is a subview of another view.
        """

    def ParentView(self) -> Graphic3d_CView:
        """Return parent View or NULL if this is not a subview."""

    def IsSubviewComposer(self) -> bool:
        """
        Return TRUE if this is view performs rendering of subviews and nothing else; FALSE by default.
        By default, view with subviews will render main scene and blit subviews on top of it.
        Rendering of main scene might become redundant in case if subviews cover entire window of
        parent view. This flag allows to disable rendering of the main scene in such scenarios without
        creation of a dedicated V3d_Viewer instance just for composing subviews.
        """

    def SetSubviewComposer(self, theIsComposer: bool) -> None:
        """
        Set if this view should perform composing of subviews and nothing else.
        """

    def Subviews(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_CView]:
        """Return subview list."""

    def AddSubview(self, theView: Graphic3d_CView | None) -> None:
        """Add subview to the list."""

    def RemoveSubview(self, theView: Graphic3d_CView) -> bool:
        """Remove subview from the list."""

    def SubviewCorner(self) -> nanoocp.Aspect.Aspect_TypeOfTriedronPosition:
        """
        Return subview position within parent view; Aspect_TOTP_LEFT_UPPER by default.
        """

    def SetSubviewCorner(self, thePos: nanoocp.Aspect.Aspect_TypeOfTriedronPosition) -> None:
        """Set subview position within parent view."""

    def SubviewTopLeft(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return subview top-left position relative to parent view in pixels."""

    def IsSubViewRelativeSize(self) -> bool:
        """
        Return TRUE if subview size is set as proportions relative to parent view.
        """

    def SubviewSize(self) -> nanoocp.BVH.BVH_Vec2d:
        """
        Return subview dimensions; (1.0, 1.0) by default.
        Values >= 2   define size in pixels;
        Values <= 1.0 define size as fraction of parent view.
        """

    def SetSubviewSize(self, theSize: nanoocp.BVH.BVH_Vec2d) -> None:
        """Set subview size relative to parent view."""

    def SubviewOffset(self) -> nanoocp.BVH.BVH_Vec2d:
        """
        Return corner offset within parent view; (0.0,0.0) by default.
        Values >= 2   define offset in pixels;
        Values <= 1.0 define offset as fraction of parent view dimensions.
        """

    def SetSubviewOffset(self, theOffset: nanoocp.BVH.BVH_Vec2d) -> None:
        """Set corner offset within parent view."""

    def SubviewMargins(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return subview margins in pixels; (0,0) by default"""

    def SetSubviewMargins(self, theMargins: nanoocp.BVH.BVH_Vec2i) -> None:
        """Set subview margins in pixels."""

    def SubviewResized(self, theWindow: nanoocp.Aspect.Aspect_NeutralWindow | None) -> None:
        """Update subview position and dimensions."""

class Graphic3d_FrameStatsData:
    """Data frame definition."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_FrameStatsData) -> None:
        """Copy constructor."""

    def FrameRate(self) -> float:
        """
        Returns FPS (frames per seconds, elapsed time).
        This number indicates an actual frame rate averaged for several frames within UpdateInterval()
        duration, basing on a real elapsed time between updates.
        """

    def FrameRateCpu(self) -> float:
        """
        Returns CPU FPS (frames per seconds, CPU time).
        This number indicates a PREDICTED frame rate,
        basing on CPU elapsed time between updates and NOT real elapsed time (which might include
        periods of CPU inactivity). Number is expected to be greater then actual frame rate returned
        by FrameRate(). Values significantly greater actual frame rate indicate that rendering is
        limited by GPU performance (CPU is stalled in-between), while values around actual frame rate
        indicate rendering being limited by CPU performance (GPU is stalled in-between).
        """

    def ImmediateFrameRate(self) -> float:
        """Returns FPS for immediate redraws."""

    def ImmediateFrameRateCpu(self) -> float:
        """Returns CPU FPS for immediate redraws."""

    def CounterValue(self, theIndex: Graphic3d_FrameStatsCounter) -> int:
        """Get counter value."""

    @overload
    def __getitem__(self, theIndex: Graphic3d_FrameStatsCounter) -> int:
        """Get counter value."""

    @overload
    def __getitem__(self, theIndex: Graphic3d_FrameStatsTimer) -> float:
        """Get timer value."""

    def TimerValue(self, theIndex: Graphic3d_FrameStatsTimer) -> float:
        """Get timer value."""

    def Reset(self) -> None:
        """Reset data."""

    def FillMax(self, theOther: Graphic3d_FrameStatsData) -> None:
        """Fill with maximum values."""

class Graphic3d_FrameStatsDataTmp(Graphic3d_FrameStatsData):
    """Temporary data frame definition."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_FrameStatsDataTmp) -> None: ...

    def FlushTimers(self, theNbFrames: int, theIsFinal: bool) -> None:
        """Compute average data considering the amount of rendered frames."""

    def Reset(self) -> None:
        """Reset data."""

    def ChangeFrameRate(self) -> float:
        """Returns FPS (frames per seconds, elapsed time)."""

    def SetFrameRate(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeFrameRate() returns by reference in C++.
        """

    def ChangeFrameRateCpu(self) -> float:
        """Returns CPU FPS (frames per seconds, CPU time)."""

    def SetFrameRateCpu(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeFrameRateCpu() returns by reference in C++.
        """

    def ChangeImmediateFrameRate(self) -> float:
        """Returns FPS for immediate redraws."""

    def SetImmediateFrameRate(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeImmediateFrameRate() returns by reference in C++.
        """

    def ChangeImmediateFrameRateCpu(self) -> float:
        """Returns CPU FPS for immediate redraws."""

    def SetImmediateFrameRateCpu(self, theValue: float) -> None:
        """
        Python addition: sets the value ChangeImmediateFrameRateCpu() returns by reference in C++.
        """

    def ChangeTimer(self, theTimer: Graphic3d_FrameStatsTimer) -> nanoocp.OSD.OSD_Timer:
        """Return a timer object for time measurements."""

    def ChangeCounterValue(self, theIndex: Graphic3d_FrameStatsCounter) -> int:
        """Get counter value."""

    def SetCounterValue(self, theIndex: Graphic3d_FrameStatsCounter, theValue: int) -> None:
        """
        Python addition: sets the value ChangeCounterValue(theIndex) returns by reference in C++.
        """

    @overload
    def __getitem__(self, theIndex: Graphic3d_FrameStatsCounter) -> int:
        """Modify counter value."""

    @overload
    def __getitem__(self, arg: Graphic3d_FrameStatsCounter, /) -> int: ...

    @overload
    def __getitem__(self, theIndex: Graphic3d_FrameStatsTimer) -> float:
        """Modify timer value."""

    @overload
    def __getitem__(self, arg: Graphic3d_FrameStatsTimer, /) -> float:
        """Python addition: alias to operator[]."""

    @overload
    def __setitem__(self, arg0: Graphic3d_FrameStatsCounter, arg1: int, /) -> None: ...

    @overload
    def __setitem__(self, arg0: Graphic3d_FrameStatsTimer, arg1: float, /) -> None:
        """
        Python addition: sets the value operator[](theIndex) returns by reference in C++.
        """

    def ChangeTimerValue(self, theIndex: Graphic3d_FrameStatsTimer) -> float:
        """Modify timer value."""

    def SetTimerValue(self, theIndex: Graphic3d_FrameStatsTimer, theValue: float) -> None:
        """
        Python addition: sets the value ChangeTimerValue(theIndex) returns by reference in C++.
        """

class Graphic3d_FrameStats(nanoocp.Standard.Standard_Transient):
    """Class storing the frame statistics."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def UpdateInterval(self) -> float:
        """
        Returns interval in seconds for updating meters across several frames; 1 second by default.
        """

    def SetUpdateInterval(self, theInterval: float) -> None:
        """Sets interval in seconds for updating values."""

    def IsLongLineFormat(self) -> bool:
        """Prefer longer lines over more greater of lines."""

    def SetLongLineFormat(self, theValue: bool) -> None:
        """Set if format should prefer longer lines over greater number of lines."""

    def FrameStart(self, theView: Graphic3d_CView | None, theIsImmediateOnly: bool) -> None:
        """Frame redraw started."""

    def FrameEnd(self, theView: Graphic3d_CView | None, theIsImmediateOnly: bool) -> None:
        """Frame redraw finished."""

    @overload
    def FormatStats(self, theFlags: Graphic3d_RenderingParams.PerfCounters) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns formatted string."""

    @overload
    def FormatStats(self, theDict: nanoocp.NCollection.NCollection_IndexedDataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString], theFlags: Graphic3d_RenderingParams.PerfCounters) -> None:
        """Fill in the dictionary with formatted statistic info."""

    def FrameDuration(self) -> float:
        """Returns duration of the last frame in seconds."""

    def FrameRate(self) -> float:
        """
        Returns FPS (frames per seconds, elapsed time).
        This number indicates an actual frame rate averaged for several frames within UpdateInterval()
        duration, basing on a real elapsed time between updates.
        """

    def FrameRateCpu(self) -> float:
        """
        Returns CPU FPS (frames per seconds, CPU time).
        This number indicates a PREDICTED frame rate,
        basing on CPU elapsed time between updates and NOT real elapsed time (which might include
        periods of CPU inactivity). Number is expected to be greater then actual frame rate returned
        by FrameRate(). Values significantly greater actual frame rate indicate that rendering is
        limited by GPU performance (CPU is stalled in-between), while values around actual frame rate
        indicate rendering being limited by CPU performance (GPU is stalled in-between).
        """

    def CounterValue(self, theCounter: Graphic3d_FrameStatsCounter) -> int:
        """
        Returns value of specified counter, cached between stats updates.
        Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """

    def TimerValue(self, theTimer: Graphic3d_FrameStatsTimer) -> float:
        """
        Returns value of specified timer for modification, should be called between ::FrameStart() and
        ::FrameEnd() calls. Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """

    def HasCulledLayers(self) -> bool:
        """Returns TRUE if some Layers have been culled."""

    def HasCulledStructs(self) -> bool:
        """Returns TRUE if some structures have been culled."""

    def LastDataFrame(self) -> Graphic3d_FrameStatsData:
        """
        Returns last data frame, cached between stats updates.
        Should NOT be called between ::FrameStart() and ::FrameEnd() calls.
        """

    def LastDataFrameIndex(self) -> int:
        """Returns last data frame index."""

    def DataFrames(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_FrameStatsData]:
        """Returns data frames."""

    def ChangeDataFrames(self) -> nanoocp.NCollection.NCollection_Array1[nanoocp.Graphic3d.Graphic3d_FrameStatsData]:
        """Returns data frames."""

    def ChangeCounter(self, theCounter: Graphic3d_FrameStatsCounter) -> int:
        """
        Returns value of specified counter for modification, should be called between ::FrameStart()
        and ::FrameEnd() calls.
        """

    def SetCounter(self, theCounter: Graphic3d_FrameStatsCounter, theValue: int) -> None:
        """
        Python addition: sets the value ChangeCounter(theCounter) returns by reference in C++.
        """

    def ChangeTimer(self, theTimer: Graphic3d_FrameStatsTimer) -> float:
        """
        Returns value of specified timer for modification, should be called between ::FrameStart() and
        ::FrameEnd() calls.
        """

    def SetTimer(self, theTimer: Graphic3d_FrameStatsTimer, theValue: float) -> None:
        """
        Python addition: sets the value ChangeTimer(theTimer) returns by reference in C++.
        """

    def ActiveDataFrame(self) -> Graphic3d_FrameStatsDataTmp:
        """
        Returns currently filling data frame for modification, should be called between ::FrameStart()
        and ::FrameEnd() calls.
        """

class Graphic3d_GraphicDriver(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition of a graphic driver
    for 3d interface (currently only OpenGl driver is used).
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def InquireLimit(self, theType: Graphic3d_TypeOfLimit) -> int:
        """Request limit of graphic resource of specific type."""

    def InquireLightLimit(self) -> int:
        """
        Request maximum number of active light sources supported by driver and hardware.
        """

    def InquirePlaneLimit(self) -> int:
        """
        Request maximum number of active clipping planes supported by driver and hardware.
        """

    def InquireViewLimit(self) -> int:
        """Request maximum number of views supported by driver."""

    def CreateStructure(self, theManager: Graphic3d_StructureManager | None) -> Graphic3d_CStructure:
        """Creates new empty graphic structure"""

    def RemoveStructure(self) -> Graphic3d_CStructure:
        """Removes structure from graphic driver and releases its resources."""

    def CreateView(self, theMgr: Graphic3d_StructureManager | None) -> Graphic3d_CView:
        """Creates new view for this graphic driver."""

    def RemoveView(self, theView: Graphic3d_CView | None) -> None:
        """Removes view from graphic driver and releases its resources."""

    def EnableVBO(self, status: bool) -> None:
        """
        enables/disables usage of OpenGL vertex buffer arrays while drawing primitive arrays
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
        """Returns information about GPU memory usage."""

    def DefaultTextHeight(self) -> float: ...

    def TextSize(self, theView: Graphic3d_CView | None, theText: str, theHeight: float) -> tuple[float, float, float]:
        """Computes text width."""

    def InsertLayerBefore(self, theNewLayerId: int, theSettings: Graphic3d_ZLayerSettings, theLayerAfter: int) -> None:
        """
        Adds a layer to all views.
        To add a structure to desired layer on display it is necessary to set the layer ID for the
        structure.
        @param[in] theNewLayerId  id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings    new layer settings
        @param[in] theLayerAfter  id of layer to append new layer before
        """

    def InsertLayerAfter(self, theNewLayerId: int, theSettings: Graphic3d_ZLayerSettings, theLayerBefore: int) -> None:
        """
        Adds a layer to all views.
        @param[in] theNewLayerId   id of new layer, should be > 0 (negative values are reserved for
        default layers).
        @param[in] theSettings     new layer settings
        @param[in] theLayerBefore  id of layer to append new layer after
        """

    def RemoveZLayer(self, theLayerId: int) -> None:
        """
        Removes Z layer. All structures displayed at the moment in layer will be displayed in
        default layer (the bottom-level z layer). By default, there are always default
        bottom-level layer that can't be removed.  The passed theLayerId should be not less than 0
        (reserved for default layers that can not be removed).
        """

    def ZLayers(self, theLayerSeq: nanoocp.NCollection.NCollection_Sequence[int]) -> None:
        """Returns list of Z layers defined for the graphical driver."""

    def SetZLayerSettings(self, theLayerId: int, theSettings: Graphic3d_ZLayerSettings) -> None:
        """Sets the settings for a single Z layer."""

    def ZLayerSettings(self, theLayerId: int) -> Graphic3d_ZLayerSettings:
        """Returns the settings of a single Z layer."""

    def ViewExists(self, theWindow: nanoocp.Aspect.Aspect_Window | None) -> tuple[bool, Graphic3d_CView]:
        """
        Returns view associated with the window if it is exists and is activated.
        Returns true if the view associated to the window exists.
        """

    def GetDisplayConnection(self) -> nanoocp.Aspect.Aspect_DisplayConnection:
        """returns Handle to display connection"""

    def NewIdentification(self) -> int:
        """Returns a new identification number for a new structure."""

    def RemoveIdentification(self, theId: int) -> None:
        """Frees the identifier of a structure."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_GraphicDriverFactory(nanoocp.Standard.Standard_Transient):
    """This class for creation of Graphic3d_GraphicDriver."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def RegisterFactory(theFactory: Graphic3d_GraphicDriverFactory | None, theIsPreferred: bool = False) -> None:
        """
        Registers factory.
        @param[in] theFactory      factory to register
        @param[in] theIsPreferred  add to the beginning of the list when TRUE, or add to the end
        otherwise
        """

    @staticmethod
    def UnregisterFactory(theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Unregisters factory."""

    @staticmethod
    def DefaultDriverFactory() -> Graphic3d_GraphicDriverFactory:
        """Return default driver factory or NULL if no one was registered."""

    @staticmethod
    def DriverFactories() -> nanoocp.NCollection.NCollection_List[nanoocp.Graphic3d.Graphic3d_GraphicDriverFactory]:
        """Return the global map of registered driver factories."""

    def CreateDriver(self, theDisp: nanoocp.Aspect.Aspect_DisplayConnection | None) -> Graphic3d_GraphicDriver:
        """Creates new empty graphic driver."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return driver factory name."""

class Graphic3d_GroupDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Graphic3d_MutableIndexBuffer(Graphic3d_IndexBuffer):
    """Mutable index buffer."""

    @overload
    def __init__(self, theAlloc: nanoocp.NCollection.NCollection_BaseAllocator | None) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Graphic3d_MutableIndexBuffer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsMutable(self) -> bool:
        """Return TRUE if data can be invalidated."""

    def InvalidatedRange(self) -> Graphic3d_BufferRange:
        """Return invalidated range."""

    def Validate(self) -> None:
        """Reset invalidated range."""

    @overload
    def Invalidate(self) -> None:
        """Invalidate the entire buffer data."""

    @overload
    def Invalidate(self, theIndexLower: int, theIndexUpper: int) -> None:
        """Invalidate the given indexes (starting from 0)"""

    def invalidate(self, theRange: Graphic3d_BufferRange) -> None:
        """Invalidate specified sub-range of data (as byte offsets)."""

class Graphic3d_MaterialDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Graphic3d_Texture2D(Graphic3d_TextureMap):
    """This abstract class for managing 2D textures"""

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Creates a texture from a file.
        MipMaps levels will be automatically generated if needed.
        """

    @overload
    def __init__(self, theNOT: Graphic3d_NameOfTexture2D) -> None:
        """
        Creates a texture from a predefined texture name set.
        MipMaps levels will be automatically generated if needed.
        """

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """
        Creates a texture from the pixmap.
        MipMaps levels will be automatically generated if needed.
        """

    @overload
    def __init__(self, theOther: Graphic3d_Texture2D) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def NumberOfTextures() -> int:
        """Returns the number of predefined textures."""

    @staticmethod
    def TextureName(theRank: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the predefined texture of rank <aRank>"""

    def Name(self) -> Graphic3d_NameOfTexture2D:
        """
        Returns the name of the predefined textures or NOT_2D_UNKNOWN
        when the name is given as a filename.
        """

    def SetImage(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """
        Assign new image to the texture.
        Note that this method does not invalidate already uploaded resources - consider calling
        ::UpdateRevision() if needed.
        """

class Graphic3d_MediaTexture(Graphic3d_Texture2D):
    """Texture adapter for Media_Frame."""

    def __init__(self, theOther: Graphic3d_MediaTexture) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """Image reader."""

    def Frame(self) -> nanoocp.Media.Media_Frame:
        """Return the frame."""

    def SetFrame(self, theFrame: nanoocp.Media.Media_Frame | None) -> None:
        """Set the frame."""

    def GenerateNewId(self) -> None:
        """Regenerate a new texture id"""

class Graphic3d_MediaTextureSet(Graphic3d_TextureSet):
    """Texture adapter for Media_Frame."""

    def __init__(self) -> None:
        """Empty constructor."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Notify(self) -> None:
        """Call callback."""

    def Input(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return input media."""

    def OpenInput(self, thePath: nanoocp.TCollection.TCollection_AsciiString, theToWait: bool) -> None:
        """
        Open specified file.
        Passing an empty path would close current input.
        """

    def PlayerContext(self) -> nanoocp.Media.Media_PlayerContext:
        """Return player context; it can be NULL until first OpenInput()."""

    def SwapFrames(self) -> bool:
        """Swap front/back frames."""

    def FrameSize(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return front frame dimensions."""

    def ShaderProgram(self) -> Graphic3d_ShaderProgram:
        """Return shader program for displaying texture set."""

    def IsPlanarYUV(self) -> bool:
        """Return TRUE if texture set defined 3 YUV planes."""

    def IsFullRangeYUV(self) -> bool:
        """Return TRUE if YUV range is full."""

    def Duration(self) -> float:
        """Return duration in seconds."""

    def Progress(self) -> float:
        """Return playback progress in seconds."""

class Graphic3d_PriorityDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Graphic3d_ShaderManager(nanoocp.Standard.Standard_Transient):
    """This class is responsible for generation of shader programs."""

    @overload
    def __init__(self, theGapi: nanoocp.Aspect.Aspect_GraphicsLibrary) -> None:
        """Creates new empty shader manager."""

    @overload
    def __init__(self, theOther: Graphic3d_ShaderManager) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsGapiGreaterEqual(self, theVerMajor: int, theVerMinor: int) -> bool:
        """
        @return true if detected GL version is greater or equal to requested one.
        """

    def GapiVersionMajor(self) -> int:
        """Return GAPI version major number."""

    def GapiVersionMinor(self) -> int:
        """Return GAPI version minor number."""

    def SetGapiVersion(self, theVerMajor: int, theVerMinor: int) -> None:
        """Return GAPI version major number."""

    def UseRedAlpha(self) -> bool:
        """
        Return TRUE if RED channel should be used instead of ALPHA for single-channel textures
        (e.g. GAPI supports only GL_RED textures and not GL_ALPHA).
        """

    def SetUseRedAlpha(self, theUseRedAlpha: bool) -> None:
        """
        Set if RED channel should be used instead of ALPHA for single-channel textures.
        """

    def HasFlatShading(self) -> bool:
        """Return flag indicating flat shading usage; TRUE by default."""

    def ToReverseDFdxSign(self) -> bool:
        """
        Return flag indicating flat shading should reverse normal flag; FALSE by default.
        """

    def SetFlatShading(self, theToUse: bool, theToReverseSign: bool) -> None:
        """Set flag indicating flat shading usage."""

    def ToEmulateDepthClamp(self) -> bool:
        """
        Return TRUE if depth clamping should be emulated by GLSL program; TRUE by default.
        """

    def SetEmulateDepthClamp(self, theToEmulate: bool) -> None:
        """Set if depth clamping should be emulated by GLSL program."""

    def HasGlslExtension(self, theExt: Graphic3d_GlslExtension) -> bool:
        """Return TRUE if specified extension is available."""

    def EnableGlslExtension(self, theExt: Graphic3d_GlslExtension, theToEnable: bool = True) -> None:
        """Set if specified extension is available or not."""

class Graphic3d_StructureDefinitionError(nanoocp.Standard.Standard_OutOfRange):
    pass

class Graphic3d_StructureManager(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition of a manager to
    which the graphic objects are associated.
    It allows them to be globally manipulated.
    It defines the global attributes.
    Keywords: Structure, Structure Manager, Update Mode,
    Destroy, Highlight, Visible
    """

    @overload
    def __init__(self, theDriver: Graphic3d_GraphicDriver | None) -> None:
        """
        Initializes the ViewManager.
        Currently creating of more than 100 viewer instances
        is not supported and leads to InitializationError and
        initialization failure.
        This limitation might be addressed in some future OCCT releases.
        Warning: Raises InitialisationError if the initialization
        of the ViewManager failed.
        """

    @overload
    def __init__(self, theOther: Graphic3d_StructureManager) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Update(self, theLayerId: int = -1) -> None:
        """Invalidates bounding box of specified ZLayerId."""

    def Remove(self) -> None:
        """Deletes and erases the 3D structure manager."""

    @overload
    def Erase(self) -> None:
        """Erases all the structures."""

    @overload
    def Erase(self, theStructure: Graphic3d_Structure | None) -> None:
        """Erases the structure."""

    def DisplayedStructures(self, SG: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure]) -> None:
        """
        Returns the set of structures displayed in
        visualiser <me>.
        """

    def HighlightedStructures(self, SG: nanoocp.NCollection.NCollection_Map[nanoocp.Graphic3d.Graphic3d_Structure]) -> None:
        """
        Returns the set of highlighted structures
        in a visualiser <me>.
        """

    @overload
    def ReCompute(self, theStructure: Graphic3d_Structure | None) -> None:
        """
        Forces a new construction of the structure.
        if <theStructure> is displayed and TOS_COMPUTED.
        """

    @overload
    def ReCompute(self, theStructure: Graphic3d_Structure | None, theProjector: Graphic3d_DataStructureManager | None) -> None:
        """
        Forces a new construction of the structure.
        if <theStructure> is displayed in <theProjector> and TOS_COMPUTED.
        """

    def Clear(self, theStructure: Graphic3d_Structure, theWithDestruction: bool) -> None:
        """Clears the structure."""

    def Connect(self, theMother: Graphic3d_Structure, theDaughter: Graphic3d_Structure) -> None:
        """Connects the structures."""

    def Disconnect(self, theMother: Graphic3d_Structure, theDaughter: Graphic3d_Structure) -> None:
        """Disconnects the structures."""

    def Display(self, theStructure: Graphic3d_Structure | None) -> None:
        """Display the structure."""

    def Highlight(self, theStructure: Graphic3d_Structure | None) -> None:
        """Highlights the structure."""

    def SetTransform(self, theStructure: Graphic3d_Structure | None, theTrsf: nanoocp.TopLoc.TopLoc_Datum3D | None) -> None:
        """Transforms the structure."""

    def ChangeDisplayPriority(self, theStructure: Graphic3d_Structure | None, theOldPriority: Graphic3d_DisplayPriority, theNewPriority: Graphic3d_DisplayPriority) -> None:
        """Changes the display priority of the structure <AStructure>."""

    def ChangeZLayer(self, theStructure: Graphic3d_Structure | None, theLayerId: int) -> None:
        """
        Change Z layer for structure. The Z layer mechanism allows to display structures in higher
        layers in overlay of structures in lower layers.
        """

    def GraphicDriver(self) -> Graphic3d_GraphicDriver:
        """Returns the graphic driver of <me>."""

    @overload
    def Identification(self, theView: Graphic3d_CView) -> int:
        """
        Attaches the view to this structure manager and sets its identification number within the
        manager.
        """

    @overload
    def Identification(self, AId: int) -> Graphic3d_Structure:
        """Returns the structure with the identification number <AId>."""

    def UnIdentification(self, theView: Graphic3d_CView) -> None:
        """
        Detach the view from this structure manager and release its identification.
        """

    def DefinedViews(self) -> "NCollection_IndexedMap<Graphic3d_CView*, NCollection_DefaultHasher<Graphic3d_CView*>>":
        """Returns the group of views defined in the structure manager."""

    def MaxNumOfViews(self) -> int:
        """
        Returns the theoretical maximum number of definable views in the manager.
        Warning: It's not possible to accept an infinite number of definable views because each
        view must have an identification and we have different managers.
        """

    @overload
    def UnHighlight(self, AStructure: Graphic3d_Structure | None) -> None:
        """Suppress the highlighting on the structure <AStructure>."""

    @overload
    def UnHighlight(self) -> None:
        """Suppresses the highlighting on all the structures in <me>."""

    @overload
    def RecomputeStructures(self) -> None:
        """
        Recomputes all structures in the manager.
        Resets Device Lost flag.
        """

    @overload
    def RecomputeStructures(self, theStructures: "NCollection_Map<Graphic3d_Structure*, NCollection_DefaultHasher<Graphic3d_Structure*>>") -> None:
        """Recomputes all structures from theStructures."""

    def RegisterObject(self, theObject: nanoocp.Standard.Standard_Transient | None, theAffinity: Graphic3d_ViewAffinity | None) -> None: ...

    def UnregisterObject(self, theObject: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def ObjectAffinity(self, theObject: nanoocp.Standard.Standard_Transient | None) -> Graphic3d_ViewAffinity: ...

    def IsDeviceLost(self) -> bool:
        """
        Returns TRUE if Device Lost flag has been set and presentation data should be reuploaded onto
        graphics driver.
        """

    def SetDeviceLost(self) -> None:
        """Sets Device Lost flag."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Graphic3d_Text(nanoocp.Standard.Standard_Transient):
    """
    This class allows the definition of a text object for display.
    The text might be defined in one of ways, using:
    - text value and position,
    - text value, orientation and the state whether the text uses position as point of attach.
    - text formatter. Formatter contains text, height and alignment parameter.

    This class also has parameters of the text height and H/V alignments.
    Custom formatting is available using Font_TextFormatter.
    """

    @overload
    def __init__(self, theHeight: float) -> None:
        """Creates default text parameters."""

    @overload
    def __init__(self, theOther: Graphic3d_Text) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Text(self) -> nanoocp.NCollection.NCollection_String:
        """Returns text value."""

    @overload
    def SetText(self, theText: nanoocp.NCollection.NCollection_String) -> None: ...

    @overload
    def SetText(self, theText: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def SetText(self, theText: str) -> None:
        """Sets text value."""

    def TextFormatter(self) -> nanoocp.Font.Font_TextFormatter:
        """
        @return text formatter; NULL by default, which means standard text formatter will be used.
        """

    def SetTextFormatter(self, theFormatter: nanoocp.Font.Font_TextFormatter | None) -> None:
        """Setup text default formatter for text within this context."""

    def Position(self) -> nanoocp.gp.gp_Pnt:
        """
        The 3D point of attachment is projected.
        If the orientation is defined, the text is written in the plane of projection.
        """

    def SetPosition(self, thePoint: nanoocp.gp.gp_Pnt) -> None:
        """Sets text point."""

    def Orientation(self) -> nanoocp.gp.gp_Ax2:
        """Returns text orientation in 3D space."""

    def HasPlane(self) -> bool:
        """Returns true if the text is filled by a point"""

    def SetOrientation(self, theOrientation: nanoocp.gp.gp_Ax2) -> None:
        """Sets text orientation in 3D space."""

    def ResetOrientation(self) -> None:
        """Reset text orientation in 3D space."""

    def HasOwnAnchorPoint(self) -> bool:
        """Returns true if the text has an anchor point"""

    def SetOwnAnchorPoint(self, theHasOwnAnchor: bool) -> None:
        """Returns true if the text has an anchor point"""

    def Height(self) -> float:
        """
        Sets height of text. (Relative to the Normalized Projection Coordinates (NPC) Space).
        """

    def SetHeight(self, theHeight: float) -> None:
        """Returns height of text"""

    def HorizontalAlignment(self) -> Graphic3d_HorizontalTextAlignment:
        """Returns horizontal alignment of text."""

    def SetHorizontalAlignment(self, theJustification: Graphic3d_HorizontalTextAlignment) -> None:
        """Sets horizontal alignment of text."""

    def VerticalAlignment(self) -> Graphic3d_VerticalTextAlignment:
        """Returns vertical alignment of text."""

    def SetVerticalAlignment(self, theJustification: Graphic3d_VerticalTextAlignment) -> None:
        """Sets vertical alignment of text."""

class Graphic3d_Texture1D(Graphic3d_TextureMap):
    """This is an abstract class for managing 1D textures."""

    def __init__(self, theOther: Graphic3d_Texture1D) -> None: ...

    def Name(self) -> Graphic3d_NameOfTexture1D:
        """
        Returns the name of the predefined textures or NOT_1D_UNKNOWN
        when the name is given as a filename.
        """

    @staticmethod
    def NumberOfTextures() -> int:
        """Returns the number of predefined textures."""

    @staticmethod
    def TextureName(aRank: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the predefined texture of rank <aRank>"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_Texture1Dmanual(Graphic3d_Texture1D):
    """
    This class provides the implementation of a manual 1D texture.
    you MUST provide texture coordinates on your facets if you want to see your texture.
    """

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates a texture from the file FileName."""

    @overload
    def __init__(self, theNOT: Graphic3d_NameOfTexture1D) -> None:
        """Create a texture from a predefined texture name set."""

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """Creates a texture from the pixmap."""

    @overload
    def __init__(self, theOther: Graphic3d_Texture1Dmanual) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_Texture1Dsegment(Graphic3d_Texture1D):
    """
    This class provides the implementation
    of a 1D texture applicable along a segment.
    You might use the SetSegment() method
    to set the way the texture is "stretched" on facets.
    """

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates a texture from a file"""

    @overload
    def __init__(self, theNOT: Graphic3d_NameOfTexture1D) -> None:
        """Creates a texture from a predefined texture name set."""

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """Creates a texture from the pixmap."""

    @overload
    def __init__(self, theOther: Graphic3d_Texture1Dsegment) -> None: ...

    def SetSegment(self, theX1: float, theY1: float, theZ1: float, theX2: float, theY2: float, theZ2: float) -> None:
        """
        Sets the texture application bounds. Defines the way
        the texture is stretched across facets.
        Default values are <0.0, 0.0, 0.0> , <0.0, 0.0, 1.0>
        """

    def Segment(self) -> tuple[float, float, float, float, float, float]:
        """Returns the values of the current segment X1, Y1, Z1 , X2, Y2, Z2."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_Texture2Dplane(Graphic3d_Texture2D):
    """
    This class allows the management of a 2D texture defined from a plane equation
    Use the SetXXX() methods for positioning the texture as you want.
    """

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates a texture from a file"""

    @overload
    def __init__(self, theNOT: Graphic3d_NameOfTexture2D) -> None:
        """Creates a texture from a predefined texture name set."""

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """Creates a texture from the pixmap."""

    @overload
    def __init__(self, theOther: Graphic3d_Texture2Dplane) -> None: ...

    def SetPlaneS(self, A: float, B: float, C: float, D: float) -> None:
        """
        Defines the texture projection plane for texture coordinate S
        default is <1.0, 0.0, 0.0, 0.0>
        """

    def SetPlaneT(self, A: float, B: float, C: float, D: float) -> None:
        """
        Defines the texture projection plane for texture coordinate T
        default is <0.0, 1.0, 0.0, 0.0>
        """

    def SetPlane(self, thePlane: Graphic3d_NameOfTexturePlane) -> None:
        """
        Defines the texture projection plane for both S and T texture coordinate
        default is NOTP_XY meaning:
        <1.0, 0.0, 0.0, 0.0> for S and
        <0.0, 1.0, 0.0, 0.0> for T
        """

    def SetScaleS(self, theVal: float) -> None:
        """
        Defines the texture scale for the S texture coordinate
        much easier than recomputing the S plane equation
        but the result is the same
        default to 1.0
        """

    def SetScaleT(self, theVal: float) -> None:
        """
        Defines the texture scale for the T texture coordinate
        much easier than recompution the T plane equation
        but the result is the same
        default to 1.0
        """

    def SetTranslateS(self, theVal: float) -> None:
        """
        Defines the texture translation for the S texture coordinate
        you can obtain the same effect by modifying the S plane
        equation but its not easier.
        default to 0.0
        """

    def SetTranslateT(self, theVal: float) -> None:
        """
        Defines the texture translation for the T texture coordinate
        you can obtain the same effect by modifying the T plane
        equation but its not easier.
        default to 0.0
        """

    def SetRotation(self, theVal: float) -> None:
        """
        Sets the rotation angle of the whole texture.
        the same result might be achieved by recomputing the
        S and T plane equation but it's not the easiest way...
        the angle is expressed in degrees
        default is 0.0
        """

    def Plane(self) -> Graphic3d_NameOfTexturePlane:
        """
        Returns the current texture plane name or NOTP_UNKNOWN
        when the plane is user defined.
        """

    def PlaneS(self) -> tuple[float, float, float, float]:
        """Returns the current texture plane S equation"""

    def PlaneT(self) -> tuple[float, float, float, float]:
        """Returns the current texture plane T equation"""

    def TranslateS(self) -> float:
        """Returns the current texture S translation value"""

    def TranslateT(self) -> float:
        """Returns the current texture T translation value"""

    def ScaleS(self) -> float:
        """Returns the current texture S scale value"""

    def ScaleT(self) -> float:
        """Returns the current texture T scale value"""

    def Rotation(self) -> float:
        """Returns the current texture rotation angle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_Texture3D(Graphic3d_TextureMap):
    """This abstract class for managing 3D textures."""

    @overload
    def __init__(self, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    def __init__(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """Creates a texture from the pixmap."""

    @overload
    def __init__(self, theFiles: nanoocp.NCollection.NCollection_Array1[nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """Creates a texture from a file."""

    @overload
    def __init__(self, theOther: Graphic3d_Texture3D) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetImage(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> None:
        """
        Assign new image to the texture.
        Note that this method does not invalidate already uploaded resources - consider calling
        ::UpdateRevision() if needed.
        """

    def GetImage(self, theSupported: nanoocp.Image.Image_SupportedFormats | None) -> nanoocp.Image.Image_PixMap:
        """Load and return image."""

class Graphic3d_TransformPersScaledAbove(Graphic3d_TransformPers):
    """
    Transformation Zoom persistence with the above boundary of scale.
    This persistence works only when the camera scale value is below the scale value of this
    persistence. Otherwise, no persistence is applied.
    """

    @overload
    def __init__(self, theScale: float, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Create a Zoom transformation persistence with an anchor 3D point and a scale value
        """

    @overload
    def __init__(self, theOther: Graphic3d_TransformPersScaledAbove) -> None: ...

    def persistentScale(self, theCamera: Graphic3d_Camera | None, theViewportWidth: int, theViewportHeight: int) -> float:
        """
        Find scale value based on the camera position and view dimensions
        If the camera scale value less than the persistence scale, zoom persistence is not applied.
        @param[in] theCamera  camera definition
        @param[in] theViewportWidth  the width of viewport.
        @param[in] theViewportHeight  the height of viewport.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Graphic3d_Layer(nanoocp.Standard.Standard_Transient):
    """Presentations list sorted within priorities."""

    @overload
    def __init__(self, theId: int, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Initializes associated priority list and layer properties"""

    @overload
    def __init__(self, theOther: Graphic3d_Layer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LayerId(self) -> int:
        """Return layer id."""

    def FrustumCullingBVHBuilder(self) -> nanoocp.BVH.BVH_Builder3d:
        """Returns BVH tree builder for frustum culling."""

    def SetFrustumCullingBVHBuilder(self, theBuilder: nanoocp.BVH.BVH_Builder3d | None) -> None:
        """Assigns BVH tree builder for frustum culling."""

    def IsImmediate(self) -> bool:
        """Return true if layer was marked with immediate flag."""

    def LayerSettings(self) -> Graphic3d_ZLayerSettings:
        """Returns settings of the layer object."""

    def SetLayerSettings(self, theSettings: Graphic3d_ZLayerSettings) -> None:
        """Sets settings of the layer object."""

    def Add(self, theStruct: Graphic3d_CStructure, thePriority: Graphic3d_DisplayPriority, isForChangePriority: bool = False) -> None: ...

    def Remove(self, theStruct: Graphic3d_CStructure, isForChangePriority: bool = False) -> tuple[bool, Graphic3d_DisplayPriority]:
        """
        Remove structure and returns its priority, if the structure is not found, method returns
        negative value
        """

    def NbStructures(self) -> int:
        """@return the number of structures"""

    def NbStructuresNotCulled(self) -> int:
        """Number of NOT culled structures in the layer."""

    def NbPriorities(self) -> int:
        """Returns the number of available priority levels"""

    def Append(self, theOther: Graphic3d_Layer) -> bool:
        """
        Append layer of acceptable type (with similar number of priorities or less).
        Returns false if the list can not be accepted.
        """

    def ArrayOfStructures(self) -> list["NCollection_IndexedMap<Graphic3d_CStructure const*, NCollection_DefaultHasher<Graphic3d_CStructure const*>>"]:
        """Returns array of structures."""

    def Structures(self, thePriority: Graphic3d_DisplayPriority) -> "NCollection_IndexedMap<Graphic3d_CStructure const*, NCollection_DefaultHasher<Graphic3d_CStructure const*>>":
        """Returns structures for specified priority."""

    def InvalidateBVHData(self) -> None:
        """
        Marks BVH tree for given priority list as dirty and
        marks primitive set for rebuild.
        """

    def InvalidateBoundingBox(self) -> None:
        """Marks cached bounding box as obsolete."""

    def BoundingBox(self, theViewId: int, theCamera: Graphic3d_Camera | None, theWindowWidth: int, theWindowHeight: int, theToIncludeAuxiliary: bool) -> nanoocp.Bnd.Bnd_Box:
        """
        Returns layer bounding box.
        @param theViewId             view index to consider View Affinity in structure
        @param theCamera             camera definition
        @param theWindowWidth        viewport width  (for applying transformation-persistence)
        @param theWindowHeight       viewport height (for applying transformation-persistence)
        @param theToIncludeAuxiliary consider also auxiliary presentations (with infinite flag or with
        trihedron transformation persistence)
        @return computed bounding box
        """

    def considerZoomPersistenceObjects(self, theViewId: int, theCamera: Graphic3d_Camera | None, theWindowWidth: int, theWindowHeight: int) -> float:
        """Returns zoom-scale factor."""

    def UpdateCulling(self, theViewId: int, theSelector: Graphic3d_CullingTool, theFrustumCullingState: Graphic3d_RenderingParams.FrustumCulling) -> None:
        """
        Update culling state - should be called before rendering.
        Traverses through BVH tree to determine which structures are in view volume.
        """

    def IsCulled(self) -> bool:
        """
        Returns TRUE if layer is empty or has been discarded entirely by culling test.
        """

    def NbOfTransformPersistenceObjects(self) -> int:
        """Returns number of transform persistence objects."""

    def CullableStructuresBVH(self) -> Graphic3d_BvhCStructureSet:
        """Returns set of Graphic3d_CStructures structures for building BVH tree."""

    def CullableTrsfPersStructuresBVH(self) -> Graphic3d_BvhCStructureSetTrsfPers:
        """
        Returns set of transform persistent Graphic3d_CStructures for building BVH tree.
        """

    def NonCullableStructures(self) -> "NCollection_IndexedMap<Graphic3d_CStructure const*, NCollection_DefaultHasher<Graphic3d_CStructure const*>>":
        """Returns indexed map of always rendered structures."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class NCollection_Mat3__float:
    """
    3x3 Matrix class.
    Warning, empty constructor returns an identity matrix.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor for identity matrix."""

    @overload
    def __init__(self, theOther: NCollection_Mat3__float) -> None: ...

    @staticmethod
    def Identity() -> NCollection_Mat3__float:
        """Return identity matrix."""

    @staticmethod
    def Zero() -> NCollection_Mat3__float:
        """Return zero matrix."""

    def GetValue(self, theRow: int, theCol: int) -> float:
        """
        Get element at the specified row and column.
        @param[in] theRow  the row.to address.
        @param[in] theCol  the column to address.
        @return the value of the addressed element.
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Access element at the specified row and column.
        @param[in] theRow  the row.to access.
        @param[in] theCol  the column to access.
        @return reference on the matrix element.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Set value for the element specified by row and columns.
        @param[in] theRow    the row to change.
        @param[in] theCol    the column to change.
        @param[in] theValue  the value to set.s
        """

    def __call__(self, theRow: int, theCol: int) -> float:
        """Return value."""

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def GetRow(self, theRow: int) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Return the row."""

    def SetRow(self, theRow: int, theVec: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Change first 3 row values by the passed vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    def GetColumn(self, theCol: int) -> nanoocp.Quantity.NCollection_Vec3__float:
        """Return the column."""

    def SetColumn(self, theCol: int, theVec: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Change first 3 column values by the passed vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    def GetDiagonal(self) -> nanoocp.Quantity.NCollection_Vec3__float:
        """
        Get vector of diagonal elements.
        @return vector of diagonal elements.
        """

    def SetDiagonal(self, theVec: nanoocp.Quantity.NCollection_Vec3__float) -> None:
        """
        Change first 3 elements of the diagonal matrix.
        @param theVec the vector of values.
        """

    def InitZero(self) -> None:
        """Initialize the zero matrix."""

    def IsZero(self) -> bool:
        """Checks the matrix for zero (without tolerance)."""

    def InitIdentity(self) -> None:
        """Initialize the identity matrix."""

    def IsIdentity(self) -> bool:
        """Checks the matrix for identity (without tolerance)."""

    def IsEqual(self, theOther: NCollection_Mat3__float) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __eq__(self, theMat: NCollection_Mat3__float) -> bool:
        """Comparison operator."""

    def __ne__(self, theOther: NCollection_Mat3__float) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    @overload
    def __mul__(self, theVec: nanoocp.Quantity.NCollection_Vec3__float) -> nanoocp.Quantity.NCollection_Vec3__float:
        """
        Multiply by the vector (M * V).
        @param[in] theVec  the vector to multiply.
        """

    @overload
    def __mul__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def __mul__(self, theFactor: float) -> NCollection_Mat3__float:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    @staticmethod
    def Multiply_s(theMatA: NCollection_Mat3__float, theMatB: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """
        Compute matrix multiplication product: A * B.
        @param[in] theMatA  the matrix "A".
        @param[in] theMatB  the matrix "B".
        """

    @overload
    def Multiply(self, theMat: NCollection_Mat3__float) -> None:
        """
        Compute matrix multiplication.
        @param[in] theMat  the matrix to multiply.
        """

    @overload
    def Multiply(self, theFactor: float) -> None:
        """
        Compute per-component multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def __imul__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """
        Multiply by the another matrix.
        @param[in] theMat  the other matrix.
        """

    @overload
    def __imul__(self, theFactor: float) -> NCollection_Mat3__float:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def Multiplied(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def Multiplied(self, theFactor: float) -> NCollection_Mat3__float:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    def Divide(self, theFactor: float) -> None:
        """
        Compute per-component division.
        @param[in] theFactor  the scale factor.
        """

    def __itruediv__(self, theScalar: float) -> NCollection_Mat3__float:
        """
        Per-component division.
        @param[in] theScalar  the scale factor.
        """

    def Divided(self, theScalar: float) -> NCollection_Mat3__float:
        """Divides all the coefficients of the matrix by scalar."""

    def __truediv__(self, theScalar: float) -> NCollection_Mat3__float:
        """Divides all the coefficients of the matrix by scalar."""

    def Add(self, theMat: NCollection_Mat3__float) -> None:
        """Per-component addition of another matrix."""

    def __iadd__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component addition of another matrix."""

    def Subtract(self, theMat: NCollection_Mat3__float) -> None:
        """Per-component subtraction of another matrix."""

    def __isub__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component subtraction of another matrix."""

    def Added(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component addition of another matrix."""

    def __add__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component addition of another matrix."""

    def Subtracted(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component subtraction of another matrix."""

    def __sub__(self, theMat: NCollection_Mat3__float) -> NCollection_Mat3__float:
        """Per-component subtraction of another matrix."""

    def Negated(self) -> NCollection_Mat3__float:
        """Returns matrix with all components negated."""

    def __neg__(self) -> NCollection_Mat3__float:
        """Returns matrix with all components negated."""

    def Transposed(self) -> NCollection_Mat3__float:
        """
        Transpose the matrix.
        @return transposed copy of the matrix.
        """

    def Transpose(self) -> None:
        """Transpose the matrix."""

    def Determinant(self) -> float:
        """Return determinant of the matrix."""

    def Adjoint(self) -> NCollection_Mat3__float:
        """Return adjoint (adjugate matrix, e.g. conjugate transpose)."""

    @overload
    def Inverted(self, theInv: NCollection_Mat3__float, theDet: float) -> bool:
        """
        Compute inverted matrix.
        @param[out] theInv the inverted matrix
        @param[out] theDet determinant of matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self, theInv: NCollection_Mat3__float) -> bool:
        """
        Compute inverted matrix.
        @param[out] theInv the inverted matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self) -> NCollection_Mat3__float:
        """Return inverted matrix."""

    def DumpJson(self, arg1: int) -> str:
        """Dumps the content of me into the stream"""

class BVH_Tree__double__3__BVH_BinaryTree:
    """BVH tree with given arity (2 or 4)."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: BVH_Tree__double__3__BVH_BinaryTree) -> None: ...

class NCollection_Mat3__double:
    """
    3x3 Matrix class.
    Warning, empty constructor returns an identity matrix.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor for identity matrix."""

    @overload
    def __init__(self, theOther: NCollection_Mat3__double) -> None: ...

    @staticmethod
    def Identity() -> NCollection_Mat3__double:
        """Return identity matrix."""

    @staticmethod
    def Zero() -> NCollection_Mat3__double:
        """Return zero matrix."""

    def GetValue(self, theRow: int, theCol: int) -> float:
        """
        Get element at the specified row and column.
        @param[in] theRow  the row.to address.
        @param[in] theCol  the column to address.
        @return the value of the addressed element.
        """

    def ChangeValue(self, theRow: int, theCol: int) -> float:
        """
        Access element at the specified row and column.
        @param[in] theRow  the row.to access.
        @param[in] theCol  the column to access.
        @return reference on the matrix element.
        """

    def SetValue(self, theRow: int, theCol: int, theValue: float) -> None:
        """
        Set value for the element specified by row and columns.
        @param[in] theRow    the row to change.
        @param[in] theCol    the column to change.
        @param[in] theValue  the value to set.s
        """

    def __call__(self, theRow: int, theCol: int) -> float:
        """Return value."""

    def __getitem__(self, arg: tuple[int, int], /) -> float:
        """Python addition: alias to operator()."""

    def __setitem__(self, arg0: tuple[int, int], arg1: float, /) -> None:
        """
        Python addition: sets the value operator()(theRow, theCol) returns by reference in C++.
        """

    def GetRow(self, theRow: int) -> nanoocp.BVH.BVH_Vec3d:
        """Return the row."""

    def SetRow(self, theRow: int, theVec: nanoocp.BVH.BVH_Vec3d) -> None:
        """
        Change first 3 row values by the passed vector.
        @param[in] theRow  the row to change.
        @param[in] theVec  the vector of values.
        """

    def GetColumn(self, theCol: int) -> nanoocp.BVH.BVH_Vec3d:
        """Return the column."""

    def SetColumn(self, theCol: int, theVec: nanoocp.BVH.BVH_Vec3d) -> None:
        """
        Change first 3 column values by the passed vector.
        @param[in] theCol  the column to change.
        @param[in] theVec  the vector of values.
        """

    def GetDiagonal(self) -> nanoocp.BVH.BVH_Vec3d:
        """
        Get vector of diagonal elements.
        @return vector of diagonal elements.
        """

    def SetDiagonal(self, theVec: nanoocp.BVH.BVH_Vec3d) -> None:
        """
        Change first 3 elements of the diagonal matrix.
        @param theVec the vector of values.
        """

    def InitZero(self) -> None:
        """Initialize the zero matrix."""

    def IsZero(self) -> bool:
        """Checks the matrix for zero (without tolerance)."""

    def InitIdentity(self) -> None:
        """Initialize the identity matrix."""

    def IsIdentity(self) -> bool:
        """Checks the matrix for identity (without tolerance)."""

    def IsEqual(self, theOther: NCollection_Mat3__double) -> bool:
        """
        Check this matrix for equality with another matrix (without tolerance!).
        """

    def __eq__(self, theMat: NCollection_Mat3__double) -> bool:
        """Comparison operator."""

    def __ne__(self, theOther: NCollection_Mat3__double) -> bool:
        """
        Check this vector with another vector for non-equality (without tolerance!).
        """

    @overload
    def __mul__(self, theVec: nanoocp.BVH.BVH_Vec3d) -> nanoocp.BVH.BVH_Vec3d:
        """
        Multiply by the vector (M * V).
        @param[in] theVec  the vector to multiply.
        """

    @overload
    def __mul__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def __mul__(self, theFactor: float) -> NCollection_Mat3__double:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    @staticmethod
    def Multiply_s(theMatA: NCollection_Mat3__double, theMatB: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """
        Compute matrix multiplication product: A * B.
        @param[in] theMatA  the matrix "A".
        @param[in] theMatB  the matrix "B".
        """

    @overload
    def Multiply(self, theMat: NCollection_Mat3__double) -> None:
        """
        Compute matrix multiplication.
        @param[in] theMat  the matrix to multiply.
        """

    @overload
    def Multiply(self, theFactor: float) -> None:
        """
        Compute per-component multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def __imul__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """
        Multiply by the another matrix.
        @param[in] theMat  the other matrix.
        """

    @overload
    def __imul__(self, theFactor: float) -> NCollection_Mat3__double:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        """

    @overload
    def Multiplied(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """
        Compute matrix multiplication product.
        @param[in] theMat  the other matrix.
        @return result of multiplication.
        """

    @overload
    def Multiplied(self, theFactor: float) -> NCollection_Mat3__double:
        """
        Compute per-element multiplication.
        @param[in] theFactor  the scale factor.
        @return the result of multiplication.
        """

    def Divide(self, theFactor: float) -> None:
        """
        Compute per-component division.
        @param[in] theFactor  the scale factor.
        """

    def __itruediv__(self, theScalar: float) -> NCollection_Mat3__double:
        """
        Per-component division.
        @param[in] theScalar  the scale factor.
        """

    def Divided(self, theScalar: float) -> NCollection_Mat3__double:
        """Divides all the coefficients of the matrix by scalar."""

    def __truediv__(self, theScalar: float) -> NCollection_Mat3__double:
        """Divides all the coefficients of the matrix by scalar."""

    def Add(self, theMat: NCollection_Mat3__double) -> None:
        """Per-component addition of another matrix."""

    def __iadd__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component addition of another matrix."""

    def Subtract(self, theMat: NCollection_Mat3__double) -> None:
        """Per-component subtraction of another matrix."""

    def __isub__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component subtraction of another matrix."""

    def Added(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component addition of another matrix."""

    def __add__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component addition of another matrix."""

    def Subtracted(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component subtraction of another matrix."""

    def __sub__(self, theMat: NCollection_Mat3__double) -> NCollection_Mat3__double:
        """Per-component subtraction of another matrix."""

    def Negated(self) -> NCollection_Mat3__double:
        """Returns matrix with all components negated."""

    def __neg__(self) -> NCollection_Mat3__double:
        """Returns matrix with all components negated."""

    def Transposed(self) -> NCollection_Mat3__double:
        """
        Transpose the matrix.
        @return transposed copy of the matrix.
        """

    def Transpose(self) -> None:
        """Transpose the matrix."""

    def Determinant(self) -> float:
        """Return determinant of the matrix."""

    def Adjoint(self) -> NCollection_Mat3__double:
        """Return adjoint (adjugate matrix, e.g. conjugate transpose)."""

    @overload
    def Inverted(self, theInv: NCollection_Mat3__double, theDet: float) -> bool:
        """
        Compute inverted matrix.
        @param[out] theInv the inverted matrix
        @param[out] theDet determinant of matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self, theInv: NCollection_Mat3__double) -> bool:
        """
        Compute inverted matrix.
        @param[out] theInv the inverted matrix
        @return true if reversion success
        """

    @overload
    def Inverted(self) -> NCollection_Mat3__double:
        """Return inverted matrix."""

    def DumpJson(self, arg1: int) -> str:
        """Dumps the content of me into the stream"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.BVH
import nanoocp.NCollection
import nanoocp.Quantity
import nanoocp.Graphic3d
Graphic3d_Mat4 = nanoocp.BVH.BVH_Mat4f
Graphic3d_Mat4d = nanoocp.BVH.BVH_Mat4d
Graphic3d_SequenceOfGroup = nanoocp.NCollection.NCollection_Sequence[nanoocp.Graphic3d.Graphic3d_Group]
Graphic3d_Vec2 = nanoocp.BVH.BVH_Vec2f
Graphic3d_Vec2d = nanoocp.BVH.BVH_Vec2d
Graphic3d_Vec2i = nanoocp.BVH.BVH_Vec2i
Graphic3d_Vec3 = nanoocp.Quantity.NCollection_Vec3__float
Graphic3d_Vec3d = nanoocp.BVH.BVH_Vec3d
Graphic3d_Vec3i = nanoocp.BVH.BVH_Vec3i
Graphic3d_Vec4 = nanoocp.Quantity.NCollection_Vec4__float
Graphic3d_Vec4d = nanoocp.BVH.BVH_Vec4d
Graphic3d_Vec4i = nanoocp.BVH.BVH_Vec4i
