"""OCCT package Prs3d (toolkit TKV3d)"""

import enum
from typing import overload

import nanoocp.Aspect
import nanoocp.BVH
import nanoocp.Bnd
import nanoocp.GeomAbs
import nanoocp.Graphic3d
import nanoocp.NCollection
import nanoocp.Poly
import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.gp


class Prs3d_VertexDrawMode(enum.IntEnum):
    """
    Describes supported modes of visualization of the shape's vertices:
    VDM_Isolated  - only isolated vertices (not belonging to a face) are displayed.
    VDM_All       - all vertices of the shape are displayed.
    VDM_Inherited - the global settings are inherited and applied to the shape's presentation.
    """

    Prs3d_VDM_Isolated = 0

    Prs3d_VDM_All = 1

    Prs3d_VDM_Inherited = 2

Prs3d_VDM_Isolated: Prs3d_VertexDrawMode = Prs3d_VertexDrawMode.Prs3d_VDM_Isolated

Prs3d_VDM_All: Prs3d_VertexDrawMode = Prs3d_VertexDrawMode.Prs3d_VDM_All

Prs3d_VDM_Inherited: Prs3d_VertexDrawMode = Prs3d_VertexDrawMode.Prs3d_VDM_Inherited

class Prs3d_TypeOfHLR(enum.IntEnum):
    """
    Declares types of hidden line removal algorithm.
    TOH_Algo enables using of exact HLR algorithm.
    TOH_PolyAlgo enables using of polygonal HLR algorithm.
    TOH_NotSet is used by Prs3d_Drawer class, it means that the drawer should return the global
    value. For more details see Prs3d_Drawer class, AIS_Shape::Compute() method and HLRAlgo package
    from TKHLR toolkit.
    """

    Prs3d_TOH_NotSet = 0

    Prs3d_TOH_PolyAlgo = 1

    Prs3d_TOH_Algo = 2

Prs3d_TOH_NotSet: Prs3d_TypeOfHLR = Prs3d_TypeOfHLR.Prs3d_TOH_NotSet

Prs3d_TOH_PolyAlgo: Prs3d_TypeOfHLR = Prs3d_TypeOfHLR.Prs3d_TOH_PolyAlgo

Prs3d_TOH_Algo: Prs3d_TypeOfHLR = Prs3d_TypeOfHLR.Prs3d_TOH_Algo

class Prs3d_DatumAttribute(enum.IntEnum):
    """Enumeration defining a datum attribute, see Prs3d_Datum."""

    Prs3d_DatumAttribute_XAxisLength = 0

    Prs3d_DatumAttribute_YAxisLength = 1

    Prs3d_DatumAttribute_ZAxisLength = 2

    Prs3d_DatumAttribute_ShadingTubeRadiusPercent = 3

    Prs3d_DatumAttribute_ShadingConeRadiusPercent = 4

    Prs3d_DatumAttribute_ShadingConeLengthPercent = 5

    Prs3d_DatumAttribute_ShadingOriginRadiusPercent = 6

    Prs3d_DatumAttribute_ShadingNumberOfFacettes = 7

    Prs3d_DA_XAxisLength = 0

    Prs3d_DA_YAxisLength = 1

    Prs3d_DA_ZAxisLength = 2

    Prs3d_DP_ShadingTubeRadiusPercent = 3

    Prs3d_DP_ShadingConeRadiusPercent = 4

    Prs3d_DP_ShadingConeLengthPercent = 5

    Prs3d_DP_ShadingOriginRadiusPercent = 6

    Prs3d_DP_ShadingNumberOfFacettes = 7

Prs3d_DatumAttribute_XAxisLength: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_YAxisLength: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ZAxisLength: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ShadingTubeRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ShadingConeRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ShadingConeLengthPercent: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ShadingOriginRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_ShadingNumberOfFacettes: Prs3d_DatumAttribute = ...

Prs3d_DA_XAxisLength: Prs3d_DatumAttribute = Prs3d_DatumAttribute.Prs3d_DA_XAxisLength

Prs3d_DA_YAxisLength: Prs3d_DatumAttribute = Prs3d_DatumAttribute.Prs3d_DA_YAxisLength

Prs3d_DA_ZAxisLength: Prs3d_DatumAttribute = Prs3d_DatumAttribute.Prs3d_DA_ZAxisLength

Prs3d_DP_ShadingTubeRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DP_ShadingConeRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DP_ShadingConeLengthPercent: Prs3d_DatumAttribute = ...

Prs3d_DP_ShadingOriginRadiusPercent: Prs3d_DatumAttribute = ...

Prs3d_DP_ShadingNumberOfFacettes: Prs3d_DatumAttribute = ...

Prs3d_DatumAttribute_NB: int = 8

class Prs3d_DatumAxes(enum.IntEnum):
    """Enumeration defining axes used in datum aspect, see Prs3d_Datum."""

    Prs3d_DatumAxes_XAxis = 1

    Prs3d_DatumAxes_YAxis = 2

    Prs3d_DatumAxes_ZAxis = 4

    Prs3d_DatumAxes_XYAxes = 3

    Prs3d_DatumAxes_YZAxes = 6

    Prs3d_DatumAxes_XZAxes = 5

    Prs3d_DatumAxes_XYZAxes = 7

    Prs3d_DA_XAxis = 1

    Prs3d_DA_YAxis = 2

    Prs3d_DA_ZAxis = 4

    Prs3d_DA_XYAxis = 3

    Prs3d_DA_YZAxis = 6

    Prs3d_DA_XZAxis = 5

    Prs3d_DA_XYZAxis = 7

Prs3d_DatumAxes_XAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_XAxis

Prs3d_DatumAxes_YAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_YAxis

Prs3d_DatumAxes_ZAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_ZAxis

Prs3d_DatumAxes_XYAxes: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_XYAxes

Prs3d_DatumAxes_YZAxes: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_YZAxes

Prs3d_DatumAxes_XZAxes: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_XZAxes

Prs3d_DatumAxes_XYZAxes: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DatumAxes_XYZAxes

Prs3d_DA_XAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_XAxis

Prs3d_DA_YAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_YAxis

Prs3d_DA_ZAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_ZAxis

Prs3d_DA_XYAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_XYAxis

Prs3d_DA_YZAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_YZAxis

Prs3d_DA_XZAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_XZAxis

Prs3d_DA_XYZAxis: Prs3d_DatumAxes = Prs3d_DatumAxes.Prs3d_DA_XYZAxis

class Prs3d_DatumParts(enum.IntEnum):
    """Enumeration defining a part of datum aspect, see Prs3d_Datum."""

    Prs3d_DatumParts_Origin = 0

    Prs3d_DatumParts_XAxis = 1

    Prs3d_DatumParts_YAxis = 2

    Prs3d_DatumParts_ZAxis = 3

    Prs3d_DatumParts_XArrow = 4

    Prs3d_DatumParts_YArrow = 5

    Prs3d_DatumParts_ZArrow = 6

    Prs3d_DatumParts_XOYAxis = 7

    Prs3d_DatumParts_YOZAxis = 8

    Prs3d_DatumParts_XOZAxis = 9

    Prs3d_DatumParts_None = 10

    Prs3d_DP_Origin = 0

    Prs3d_DP_XAxis = 1

    Prs3d_DP_YAxis = 2

    Prs3d_DP_ZAxis = 3

    Prs3d_DP_XArrow = 4

    Prs3d_DP_YArrow = 5

    Prs3d_DP_ZArrow = 6

    Prs3d_DP_XOYAxis = 7

    Prs3d_DP_YOZAxis = 8

    Prs3d_DP_XOZAxis = 9

    Prs3d_DP_None = 10

Prs3d_DatumParts_Origin: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_Origin

Prs3d_DatumParts_XAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_XAxis

Prs3d_DatumParts_YAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_YAxis

Prs3d_DatumParts_ZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_ZAxis

Prs3d_DatumParts_XArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_XArrow

Prs3d_DatumParts_YArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_YArrow

Prs3d_DatumParts_ZArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_ZArrow

Prs3d_DatumParts_XOYAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_XOYAxis

Prs3d_DatumParts_YOZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_YOZAxis

Prs3d_DatumParts_XOZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_XOZAxis

Prs3d_DatumParts_None: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DatumParts_None

Prs3d_DP_Origin: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_Origin

Prs3d_DP_XAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_XAxis

Prs3d_DP_YAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_YAxis

Prs3d_DP_ZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_ZAxis

Prs3d_DP_XArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_XArrow

Prs3d_DP_YArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_YArrow

Prs3d_DP_ZArrow: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_ZArrow

Prs3d_DP_XOYAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_XOYAxis

Prs3d_DP_YOZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_YOZAxis

Prs3d_DP_XOZAxis: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_XOZAxis

Prs3d_DP_None: Prs3d_DatumParts = Prs3d_DatumParts.Prs3d_DP_None

Prs3d_DatumParts_NB: int = 11

class Prs3d_DatumMode(enum.IntEnum):
    """
    Enumeration defining a mode of datum graphic presentation, see Prs3d_Datum.
    """

    Prs3d_DM_WireFrame = 0

    Prs3d_DM_Shaded = 1

Prs3d_DM_WireFrame: Prs3d_DatumMode = Prs3d_DatumMode.Prs3d_DM_WireFrame

Prs3d_DM_Shaded: Prs3d_DatumMode = Prs3d_DatumMode.Prs3d_DM_Shaded

class Prs3d_DimensionArrowOrientation(enum.IntEnum):
    """
    Specifies dimension arrow location and orientation.
    DAO_Internal - arrows "inside", pointing outwards.
    DAO_External - arrows "outside", pointing inwards.
    DAO_Fit      - arrows oriented inside if value label with arrowtips fit the dimension line,
    otherwise - externally
    """

    Prs3d_DAO_Internal = 0

    Prs3d_DAO_External = 1

    Prs3d_DAO_Fit = 2

Prs3d_DAO_Internal: Prs3d_DimensionArrowOrientation = ...

Prs3d_DAO_External: Prs3d_DimensionArrowOrientation = ...

Prs3d_DAO_Fit: Prs3d_DimensionArrowOrientation = Prs3d_DimensionArrowOrientation.Prs3d_DAO_Fit

class Prs3d_DimensionTextHorizontalPosition(enum.IntEnum):
    """
    Specifies options for positioning dimension value label in horizontal direction.
    DTHP_Left   - value label located at left side on dimension extension.
    DTHP_Right  - value label located at right side on dimension extension.
    DTHP_Center - value label located at center of dimension line.
    DTHP_Fit    - value label located automatically at left side if does not fits
    the dimension space, otherwise the value label is placed at center.
    """

    Prs3d_DTHP_Left = 0

    Prs3d_DTHP_Right = 1

    Prs3d_DTHP_Center = 2

    Prs3d_DTHP_Fit = 3

Prs3d_DTHP_Left: Prs3d_DimensionTextHorizontalPosition = ...

Prs3d_DTHP_Right: Prs3d_DimensionTextHorizontalPosition = ...

Prs3d_DTHP_Center: Prs3d_DimensionTextHorizontalPosition = ...

Prs3d_DTHP_Fit: Prs3d_DimensionTextHorizontalPosition = ...

class Prs3d_DimensionTextVerticalPosition(enum.IntEnum):
    """
    Specifies options for positioning dimension value label in vertical direction
    with respect to dimension (extension) line.
    DTVP_Above - text label is located above the dimension or extension line.
    DTVP_Below - text label is located below the dimension or extension line.
    DTVP_Center - the text label middle-point is in line with dimension or extension line.
    """

    Prs3d_DTVP_Above = 0

    Prs3d_DTVP_Below = 1

    Prs3d_DTVP_Center = 2

Prs3d_DTVP_Above: Prs3d_DimensionTextVerticalPosition = ...

Prs3d_DTVP_Below: Prs3d_DimensionTextVerticalPosition = ...

Prs3d_DTVP_Center: Prs3d_DimensionTextVerticalPosition = ...

class Prs3d_TypeOfHighlight(enum.IntEnum):
    """Type of highlighting to apply specific style."""

    Prs3d_TypeOfHighlight_None = 0

    Prs3d_TypeOfHighlight_Selected = 1

    Prs3d_TypeOfHighlight_Dynamic = 2

    Prs3d_TypeOfHighlight_LocalSelected = 3

    Prs3d_TypeOfHighlight_LocalDynamic = 4

    Prs3d_TypeOfHighlight_SubIntensity = 5

    Prs3d_TypeOfHighlight_NB = 6

Prs3d_TypeOfHighlight_None: Prs3d_TypeOfHighlight = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_None

Prs3d_TypeOfHighlight_Selected: Prs3d_TypeOfHighlight = ...

Prs3d_TypeOfHighlight_Dynamic: Prs3d_TypeOfHighlight = ...

Prs3d_TypeOfHighlight_LocalSelected: Prs3d_TypeOfHighlight = ...

Prs3d_TypeOfHighlight_LocalDynamic: Prs3d_TypeOfHighlight = ...

Prs3d_TypeOfHighlight_SubIntensity: Prs3d_TypeOfHighlight = ...

Prs3d_TypeOfHighlight_NB: Prs3d_TypeOfHighlight = Prs3d_TypeOfHighlight.Prs3d_TypeOfHighlight_NB

class Prs3d_TypeOfLinePicking(enum.IntEnum):
    Prs3d_TOLP_Point = 0

    Prs3d_TOLP_Segment = 1

Prs3d_TOLP_Point: Prs3d_TypeOfLinePicking = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Point

Prs3d_TOLP_Segment: Prs3d_TypeOfLinePicking = Prs3d_TypeOfLinePicking.Prs3d_TOLP_Segment

class Prs3d_DimensionUnits:
    """
    This class provides units for two dimension groups:
    - lengths (length, radius, diameter)
    - angles
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor. Sets meters as default length units
        and radians as default angle units.
        """

    @overload
    def __init__(self, theUnits: Prs3d_DimensionUnits) -> None: ...

    def SetAngleUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets angle units"""

    def GetAngleUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return angle units"""

    def SetLengthUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets length units"""

    def GetLengthUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """@return length units"""

class Prs3d_Drawer(nanoocp.Graphic3d.Graphic3d_PresentationAttributes):
    """
    A graphic attribute manager which governs how
    objects such as color, width, line thickness and deflection are displayed.
    A drawer includes an instance of the Aspect classes with particular default values.
    """

    @overload
    def __init__(self) -> None:
        """Default constructor."""

    @overload
    def __init__(self, theOther: Prs3d_Drawer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetupOwnDefaults(self) -> None:
        """Setup all own aspects with default values."""

    def SetTypeOfDeflection(self, theTypeOfDeflection: nanoocp.Aspect.Aspect_TypeOfDeflection) -> None:
        """
        Sets the type of chordal deflection.
        This indicates whether the deflection value is absolute or relative to the size of the object.
        """

    def TypeOfDeflection(self) -> nanoocp.Aspect.Aspect_TypeOfDeflection:
        """
        Returns the type of chordal deflection.
        This indicates whether the deflection value is absolute or relative to the size of the object.
        """

    def HasOwnTypeOfDeflection(self) -> bool:
        """Returns true if the drawer has a type of deflection setting active."""

    def UnsetOwnTypeOfDeflection(self) -> None:
        """
        Resets HasOwnTypeOfDeflection() flag, e.g. undoes SetTypeOfDeflection().
        """

    def SetMaximalChordialDeviation(self, theChordialDeviation: float) -> None:
        """
        Defines the maximal chordial deviation when drawing any curve.
        Even if the type of deviation is set to TOD_Relative, this value is used by:
        Prs3d_DeflectionCurve
        Prs3d_WFDeflectionSurface
        Prs3d_WFDeflectionRestrictedFace
        """

    def MaximalChordialDeviation(self) -> float:
        """
        Returns the maximal chordal deviation. The default value is 0.0001.
        Drawings of curves or patches are made with respect to an absolute maximal chordal deviation.
        """

    def HasOwnMaximalChordialDeviation(self) -> bool:
        """
        Returns true if the drawer has a maximal chordial deviation setting active.
        """

    def UnsetOwnMaximalChordialDeviation(self) -> None:
        """
        Resets HasOwnMaximalChordialDeviation() flag, e.g. undoes SetMaximalChordialDeviation().
        """

    def SetTypeOfHLR(self, theTypeOfHLR: Prs3d_TypeOfHLR) -> None:
        """Sets the type of HLR algorithm used by drawer's interactive objects"""

    def TypeOfHLR(self) -> Prs3d_TypeOfHLR:
        """Returns the type of HLR algorithm currently in use."""

    def HasOwnTypeOfHLR(self) -> bool:
        """Returns true if the type of HLR is not equal to Prs3d_TOH_NotSet."""

    def SetMaximalParameterValue(self, theValue: float) -> None:
        """
        Defines the maximum value allowed for the first and last
        parameters of an infinite curve.
        """

    def MaximalParameterValue(self) -> float:
        """
        Sets the maximum value allowed for the first and last parameters of an infinite curve.
        By default, this value is 500000.
        """

    def HasOwnMaximalParameterValue(self) -> bool:
        """
        Returns true if the drawer has a maximum value allowed for the first and last
        parameters of an infinite curve setting active.
        """

    def UnsetOwnMaximalParameterValue(self) -> None:
        """
        Resets HasOwnMaximalParameterValue() flag, e.g. undoes SetMaximalParameterValue().
        """

    def SetIsoOnPlane(self, theIsEnabled: bool) -> None:
        """
        Sets IsoOnPlane on or off by setting the parameter theIsEnabled to true or false.
        """

    def IsoOnPlane(self) -> bool:
        """Returns True if the drawing of isos on planes is enabled."""

    def HasOwnIsoOnPlane(self) -> bool:
        """Returns true if the drawer has IsoOnPlane setting active."""

    def UnsetOwnIsoOnPlane(self) -> None:
        """Resets HasOwnIsoOnPlane() flag, e.g. undoes SetIsoOnPlane()."""

    def IsoOnTriangulation(self) -> bool:
        """Returns True if the drawing of isos on triangulation is enabled."""

    def HasOwnIsoOnTriangulation(self) -> bool:
        """Returns true if the drawer has IsoOnTriangulation setting active."""

    def UnsetOwnIsoOnTriangulation(self) -> None:
        """
        Resets HasOwnIsoOnTriangulation() flag, e.g. undoes SetIsoOnTriangulation().
        """

    def SetIsoOnTriangulation(self, theToEnable: bool) -> None:
        """
        Enables or disables isolines on triangulation by setting the parameter theIsEnabled to true or
        false.
        """

    def SetDiscretisation(self, theValue: int) -> None:
        """Sets the discretisation parameter theValue."""

    def Discretisation(self) -> int:
        """Returns the discretisation setting."""

    def HasOwnDiscretisation(self) -> bool:
        """Returns true if the drawer has discretisation setting active."""

    def UnsetOwnDiscretisation(self) -> None:
        """Resets HasOwnDiscretisation() flag, e.g. undoes SetDiscretisation()."""

    @overload
    def SetDeviationCoefficient(self, theCoefficient: float) -> None:
        """
        Sets the deviation coefficient theCoefficient.
        Also sets the hasOwnDeviationCoefficient flag to true and
        myPreviousDeviationCoefficient
        """

    @overload
    def SetDeviationCoefficient(self) -> None:
        """
        Resets HasOwnDeviationCoefficient() flag, e.g. undoes previous SetDeviationCoefficient().
        """

    def DeviationCoefficient(self) -> float:
        """
        Returns the deviation coefficient.
        Drawings of curves or patches are made with respect
        to a maximal chordal deviation. A Deviation coefficient
        is used in the shading display mode. The shape is
        seen decomposed into triangles. These are used to
        calculate reflection of light from the surface of the
        object. The triangles are formed from chords of the
        curves in the shape. The deviation coefficient gives
        the highest value of the angle with which a chord can
        deviate from a tangent to a curve. If this limit is
        reached, a new triangle is begun.
        This deviation is absolute and is set through the
        method: SetMaximalChordialDeviation. The default value is 0.001.
        In drawing shapes, however, you are allowed to ask
        for a relative deviation. This deviation will be:
        SizeOfObject * DeviationCoefficient.
        """

    def HasOwnDeviationCoefficient(self) -> bool:
        """
        Returns true if there is a local setting for deviation
        coefficient in this framework for a specific interactive object.
        """

    def PreviousDeviationCoefficient(self) -> float:
        """
        Saves the previous value used for the chordal
        deviation coefficient.
        """

    def UpdatePreviousDeviationCoefficient(self) -> None:
        """
        Updates the previous value used for the chordal deviation coefficient to the current state.
        """

    @overload
    def SetDeviationAngle(self, theAngle: float) -> None:
        """
        Sets the deviation angle theAngle.
        Also sets the hasOwnDeviationAngle flag to true, and myPreviousDeviationAngle.
        """

    @overload
    def SetDeviationAngle(self) -> None:
        """
        Resets HasOwnDeviationAngle() flag, e.g. undoes previous SetDeviationAngle().
        """

    def DeviationAngle(self) -> float:
        """
        Returns the value for deviation angle in radians, 20 * M_PI / 180 by default.
        """

    def HasOwnDeviationAngle(self) -> bool:
        """
        Returns true if there is a local setting for deviation
        angle in this framework for a specific interactive object.
        """

    def PreviousDeviationAngle(self) -> float:
        """Returns the previous deviation angle"""

    def UpdatePreviousDeviationAngle(self) -> None:
        """Updates the previous deviation angle to the current value"""

    def SetAutoTriangulation(self, theIsEnabled: bool) -> None:
        """
        Sets IsAutoTriangulated on or off by setting the parameter theIsEnabled to true or false.
        If this flag is True automatic re-triangulation with deflection-check logic will be applied.
        Else this feature will be disable and triangulation is expected to be computed by application
        itself and no shading presentation at all if unavailable.
        """

    def IsAutoTriangulation(self) -> bool:
        """Returns True if automatic triangulation is enabled."""

    def HasOwnIsAutoTriangulation(self) -> bool:
        """Returns true if the drawer has IsoOnPlane setting active."""

    def UnsetOwnIsAutoTriangulation(self) -> None:
        """
        Resets HasOwnIsAutoTriangulation() flag, e.g. undoes SetAutoTriangulation().
        """

    def UIsoAspect(self) -> Prs3d_IsoAspect:
        """
        Defines own attributes for drawing an U isoparametric curve of a face,
        settings from linked Drawer or NULL if neither was set.

        These attributes are used by the following algorithms:
        Prs3d_WFDeflectionSurface
        Prs3d_WFDeflectionRestrictedFace
        """

    def SetUIsoAspect(self, theAspect: Prs3d_IsoAspect | None) -> None: ...

    def HasOwnUIsoAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        UIso aspect that overrides the one in the link.
        """

    def VIsoAspect(self) -> Prs3d_IsoAspect:
        """
        Defines own attributes for drawing an V isoparametric curve of a face,
        settings from linked Drawer or NULL if neither was set.

        These attributes are used by the following algorithms:
        Prs3d_WFDeflectionSurface
        Prs3d_WFDeflectionRestrictedFace
        """

    def SetVIsoAspect(self, theAspect: Prs3d_IsoAspect | None) -> None:
        """Sets the appearance of V isoparameters - theAspect."""

    def HasOwnVIsoAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        VIso aspect that overrides the one in the link.
        """

    def WireAspect(self) -> Prs3d_LineAspect:
        """
        Returns own wire aspect settings, settings from linked Drawer or NULL if neither was set.
        These attributes are used by the algorithm Prs3d_WFShape.
        """

    def SetWireAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """Sets the parameter theAspect for display of wires."""

    def HasOwnWireAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        wire aspect that overrides the one in the link.
        """

    def SetWireDraw(self, theIsEnabled: bool) -> None:
        """
        Sets WireDraw on or off by setting the parameter theIsEnabled to true or false.
        """

    def WireDraw(self) -> bool:
        """Returns True if the drawing of the wire is enabled."""

    def HasOwnWireDraw(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw wires" flag that overrides the one in the link.
        """

    def UnsetOwnWireDraw(self) -> None:
        """Resets HasOwnWireDraw() flag, e.g. undoes SetWireDraw()."""

    def PointAspect(self) -> Prs3d_PointAspect:
        """
        Returns own point aspect setting, settings from linked Drawer or NULL if neither was set.
        These attributes are used by the algorithms Prs3d_Point.
        """

    def SetPointAspect(self, theAspect: Prs3d_PointAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of points"""

    def HasOwnPointAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        point aspect that overrides the one in the link.
        """

    def SetupOwnPointAspect(self, theDefaults: Prs3d_Drawer | None = None) -> bool:
        """
        Sets own point aspect, which is a yellow Aspect_TOM_PLUS marker by default.
        Returns FALSE if the drawer already has its own attribute for point aspect.
        """

    def LineAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for line aspects, settings from linked Drawer or NULL if neither was set.
        These attributes are used by the following algorithms:
        Prs3d_Curve
        Prs3d_Line
        Prs3d_HLRShape
        """

    def SetLineAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of lines."""

    def HasOwnLineAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        line aspect that overrides the one in the link.
        """

    def SetOwnLineAspects(self, theDefaults: Prs3d_Drawer | None = None) -> bool:
        """
        Sets own line aspects, which are
        single U and single V gray75 solid isolines (::UIsoAspect(), ::VIsoAspect()),
        red wire (::WireAspect()), yellow line (::LineAspect()),
        yellow seen line (::SeenLineAspect()), dashed yellow hidden line (::HiddenLineAspect()),
        green free boundary (::FreeBoundaryAspect()), yellow unfree boundary
        (::UnFreeBoundaryAspect()). Returns FALSE if own line aspect are already set.
        """

    def SetOwnDatumAspects(self, theDefaults: Prs3d_Drawer | None = None) -> bool:
        """
        Sets own line aspects for datums.
        Returns FALSE if own line for datums are already set.
        """

    def TextAspect(self) -> Prs3d_TextAspect:
        """
        Returns own settings for text aspect, settings from linked Drawer or NULL if neither was set.
        """

    def SetTextAspect(self, theAspect: Prs3d_TextAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of text."""

    def HasOwnTextAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        text aspect that overrides the one in the link.
        """

    def ShadingAspect(self) -> Prs3d_ShadingAspect:
        """
        Returns own settings for shading aspects, settings from linked Drawer or NULL if neither was
        set.
        """

    def SetShadingAspect(self, theAspect: Prs3d_ShadingAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of shading."""

    def HasOwnShadingAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        shading aspect that overrides the one in the link.
        """

    def SetupOwnShadingAspect(self, theDefaults: Prs3d_Drawer | None = None) -> bool:
        """
        Sets own shading aspect, which is Graphic3d_NameOfMaterial_Brass material by default.
        Returns FALSE if the drawer already has its own attribute for shading aspect.
        """

    def SeenLineAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for seen line aspects, settings of linked Drawer or NULL if neither was
        set.
        """

    def SetSeenLineAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets the parameter theAspect for the display of seen lines in hidden line removal mode.
        """

    def HasOwnSeenLineAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        seen line aspect that overrides the one in the link.
        """

    def PlaneAspect(self) -> Prs3d_PlaneAspect:
        """
        Returns own settings for the appearance of planes, settings from linked Drawer or NULL if
        neither was set.
        """

    def SetPlaneAspect(self, theAspect: Prs3d_PlaneAspect | None) -> None:
        """Sets the parameter theAspect for the display of planes."""

    def HasOwnPlaneAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        plane aspect that overrides the one in the link.
        """

    def ArrowAspect(self) -> Prs3d_ArrowAspect:
        """
        Returns own attributes for display of arrows, settings from linked Drawer or NULL if neither
        was set.
        """

    def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of arrows."""

    def HasOwnArrowAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        arrow aspect that overrides the one in the link.
        """

    def SetLineArrowDraw(self, theIsEnabled: bool) -> None:
        """
        Enables the drawing of an arrow at the end of each line.
        By default the arrows are not drawn.
        """

    def LineArrowDraw(self) -> bool:
        """
        Returns True if drawing an arrow at the end of each edge is enabled
        and False otherwise (the default).
        """

    def HasOwnLineArrowDraw(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw arrow" flag that overrides the one in the link.
        """

    def UnsetOwnLineArrowDraw(self) -> None:
        """Reset HasOwnLineArrowDraw() flag, e.g. undoes SetLineArrowDraw()."""

    def HiddenLineAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for hidden line aspects, settings from linked Drawer or NULL if neither
        was set.
        """

    def SetHiddenLineAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets the parameter theAspect for the display of hidden lines in hidden line removal mode.
        """

    def HasOwnHiddenLineAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        hidden lines aspect that overrides the one in the link.
        """

    def DrawHiddenLine(self) -> bool:
        """
        Returns true if the hidden lines are to be drawn.
        By default the hidden lines are not drawn.
        """

    def EnableDrawHiddenLine(self) -> None:
        """Enables the DrawHiddenLine function."""

    def DisableDrawHiddenLine(self) -> None:
        """Disables the DrawHiddenLine function."""

    def HasOwnDrawHiddenLine(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw hidden lines" flag that overrides the one in the link.
        """

    def UnsetOwnDrawHiddenLine(self) -> None:
        """
        Resets HasOwnDrawHiddenLine() flag, e.g. unsets
        EnableDrawHiddenLine()/DisableDrawHiddenLine().
        """

    def VectorAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for the appearance of vectors, settings from linked Drawer or NULL if
        neither was set.
        """

    def SetVectorAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """Sets the modality theAspect for the display of vectors."""

    def HasOwnVectorAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        vector aspect that overrides the one in the link.
        """

    def SetVertexDrawMode(self, theMode: Prs3d_VertexDrawMode) -> None:
        """
        Sets the mode of visualization of vertices of a TopoDS_Shape instance.
        By default, only stand-alone vertices (not belonging topologically to an edge) are drawn,
        that corresponds to Prs3d_VDM_Standalone mode.
        Switching to Prs3d_VDM_Standalone mode makes all shape's vertices visible.
        To inherit this parameter from the global drawer instance ("the link") when it is present,
        Prs3d_VDM_Inherited value should be used.
        """

    def VertexDrawMode(self) -> Prs3d_VertexDrawMode:
        """
        Returns the current mode of visualization of vertices of a TopoDS_Shape instance.
        """

    def HasOwnVertexDrawMode(self) -> bool:
        """
        Returns true if the vertex draw mode is not equal to <b>Prs3d_VDM_Inherited</b>.
        This means that individual vertex draw mode value (i.e. not inherited from the global
        drawer) is used for a specific interactive object.
        """

    def DatumAspect(self) -> Prs3d_DatumAspect:
        """
        Returns own settings for the appearance of datums, settings from linked Drawer or NULL if
        neither was set.
        """

    def SetDatumAspect(self, theAspect: Prs3d_DatumAspect | None) -> None:
        """Sets the modality theAspect for the display of datums."""

    def HasOwnDatumAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        datum aspect that overrides the one in the link.
        """

    def SectionAspect(self) -> Prs3d_LineAspect:
        """
        Returns own LineAspect for section wire, settings from linked Drawer or NULL if neither was
        set. These attributes are used by the algorithm Prs3d_WFShape.
        """

    def SetSectionAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """Sets the parameter theAspect for display attributes of sections."""

    def HasOwnSectionAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        section aspect that overrides the one in the link.
        """

    def SetFreeBoundaryAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets the parameter theAspect for the display of free boundaries.
        The method sets aspect owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def FreeBoundaryAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for presentation of free boundaries, settings from linked Drawer or NULL
        if neither was set. In other words, this settings affect boundaries which are not shared.
        These attributes are used by the algorithm Prs3d_WFShape
        """

    def HasOwnFreeBoundaryAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        free boundaries aspect that overrides the one in the link.
        """

    def SetFreeBoundaryDraw(self, theIsEnabled: bool) -> None:
        """
        Enables or disables drawing of free boundaries for shading presentations.
        The method sets drawing flag owned by the drawer that will be used during
        visualization instead of the one set in link.
        theIsEnabled is a boolean flag indicating whether the free boundaries should be
        drawn or not.
        """

    def FreeBoundaryDraw(self) -> bool:
        """
        Returns True if the drawing of the free boundaries is enabled
        True is the default setting.
        """

    def HasOwnFreeBoundaryDraw(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw free boundaries" flag that overrides the one in the link.
        """

    def UnsetOwnFreeBoundaryDraw(self) -> None:
        """
        Resets HasOwnFreeBoundaryDraw() flag, e.g. undoes SetFreeBoundaryDraw().
        """

    def SetUnFreeBoundaryAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets the parameter theAspect for the display of shared boundaries.
        The method sets aspect owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def UnFreeBoundaryAspect(self) -> Prs3d_LineAspect:
        """
        Returns own settings for shared boundary line aspects, settings from linked Drawer or NULL if
        neither was set. These attributes are used by the algorithm Prs3d_WFShape
        """

    def HasOwnUnFreeBoundaryAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        unfree boundaries aspect that overrides the one in the link.
        """

    def SetUnFreeBoundaryDraw(self, theIsEnabled: bool) -> None:
        """
        Enables or disables drawing of shared boundaries for shading presentations.
        The method sets drawing flag owned by the drawer that will be used during
        visualization instead of the one set in link.
        theIsEnabled is a boolean flag indicating whether the shared boundaries should be drawn or
        not.
        """

    def UnFreeBoundaryDraw(self) -> bool:
        """
        Returns True if the drawing of the shared boundaries is enabled.
        True is the default setting.
        """

    def HasOwnUnFreeBoundaryDraw(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw shared boundaries" flag that overrides the one in the link.
        """

    def UnsetOwnUnFreeBoundaryDraw(self) -> None:
        """
        Resets HasOwnUnFreeBoundaryDraw() flag, e.g. undoes SetUnFreeBoundaryDraw().
        """

    def SetFaceBoundaryAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets line aspect for face boundaries.
        The method sets line aspect owned by the drawer that will be used during
        visualization instead of the one set in link.
        theAspect is the line aspect that determines the look of the face boundaries.
        """

    def FaceBoundaryAspect(self) -> Prs3d_LineAspect:
        """
        Returns own line aspect of face boundaries, settings from linked Drawer or NULL if neither was
        set.
        """

    def HasOwnFaceBoundaryAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        face boundaries aspect that overrides the one in the link.
        """

    def SetupOwnFaceBoundaryAspect(self, theDefaults: Prs3d_Drawer | None = None) -> bool:
        """
        Sets own face boundary aspect, which is a black solid line by default.
        Returns FALSE if the drawer already has its own attribute for face boundary aspect.
        """

    def SetFaceBoundaryDraw(self, theIsEnabled: bool) -> None:
        """
        Enables or disables face boundary drawing for shading presentations.
        The method sets drawing flag owned by the drawer that will be used during
        visualization instead of the one set in link.
        theIsEnabled is a boolean flag indicating whether the face boundaries should be drawn or not.
        """

    def FaceBoundaryDraw(self) -> bool:
        """Checks whether the face boundary drawing is enabled or not."""

    def HasOwnFaceBoundaryDraw(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        "draw face boundaries" flag that overrides the one in the link.
        """

    def UnsetOwnFaceBoundaryDraw(self) -> None:
        """
        Resets HasOwnFaceBoundaryDraw() flag, e.g. undoes SetFaceBoundaryDraw().
        """

    def HasOwnFaceBoundaryUpperContinuity(self) -> bool:
        """
        Returns true if the drawer has its own attribute for face boundaries upper edge continuity
        class that overrides the one in the link.
        """

    def FaceBoundaryUpperContinuity(self) -> nanoocp.GeomAbs.GeomAbs_Shape:
        """Get the most edge continuity class; GeomAbs_CN by default (all edges)."""

    def SetFaceBoundaryUpperContinuity(self, theMostAllowedEdgeClass: nanoocp.GeomAbs.GeomAbs_Shape) -> None:
        """Set the most edge continuity class for face boundaries."""

    def UnsetFaceBoundaryUpperContinuity(self) -> None:
        """Unset the most edge continuity class for face boundaries."""

    def DimensionAspect(self) -> Prs3d_DimensionAspect:
        """
        Returns own settings for the appearance of dimensions, settings from linked Drawer or NULL if
        neither was set.
        """

    def SetDimensionAspect(self, theAspect: Prs3d_DimensionAspect | None) -> None:
        """
        Sets the settings for the appearance of dimensions.
        The method sets aspect owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def HasOwnDimensionAspect(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        the appearance of dimensions that overrides the one in the link.
        """

    def SetDimLengthModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets dimension length model units for computing of dimension presentation.
        The method sets value owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def SetDimAngleModelUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets dimension angle model units for computing of dimension presentation.
        The method sets value owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def DimLengthModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns length model units for the dimension presentation."""

    def DimAngleModelUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns angle model units for the dimension presentation."""

    def HasOwnDimLengthModelUnits(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        dimension length model units that overrides the one in the link.
        """

    def UnsetOwnDimLengthModelUnits(self) -> None:
        """
        Resets HasOwnDimLengthModelUnits() flag, e.g. undoes SetDimLengthModelUnits().
        """

    def HasOwnDimAngleModelUnits(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        dimension angle model units that overrides the one in the link.
        """

    def UnsetOwnDimAngleModelUnits(self) -> None:
        """
        Resets HasOwnDimAngleModelUnits() flag, e.g. undoes SetDimAngleModelUnits().
        """

    def SetDimLengthDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets length units in which value for dimension presentation is displayed.
        The method sets value owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def SetDimAngleDisplayUnits(self, theUnits: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets angle units in which value for dimension presentation is displayed.
        The method sets value owned by the drawer that will be used during
        visualization instead of the one set in link.
        """

    def DimLengthDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns length units in which dimension presentation is displayed."""

    def DimAngleDisplayUnits(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns angle units in which dimension presentation is displayed."""

    def HasOwnDimLengthDisplayUnits(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        length units in which dimension presentation is displayed
        that overrides the one in the link.
        """

    def UnsetOwnDimLengthDisplayUnits(self) -> None:
        """
        Resets HasOwnDimLengthModelUnits() flag, e.g. undoes SetDimLengthDisplayUnits().
        """

    def HasOwnDimAngleDisplayUnits(self) -> bool:
        """
        Returns true if the drawer has its own attribute for
        angle units in which dimension presentation is displayed
        that overrides the one in the link.
        """

    def UnsetOwnDimAngleDisplayUnits(self) -> None:
        """
        Resets HasOwnDimAngleDisplayUnits() flag, e.g. undoes SetDimLengthDisplayUnits().
        """

    @overload
    def Link(self) -> Prs3d_Drawer:
        """Returns the drawer to which the current object references."""

    @overload
    def Link(self, theDrawer: Prs3d_Drawer | None) -> None:
        """Sets theDrawer as a link to which the current object references."""

    def HasLink(self) -> bool:
        """Returns true if the current object has a link on the other drawer."""

    def SetLink(self, theDrawer: Prs3d_Drawer | None) -> None:
        """Sets theDrawer as a link to which the current object references."""

    def ClearLocalAttributes(self) -> None:
        """Removes local attributes."""

    def SetShaderProgram(self, theProgram: nanoocp.Graphic3d.Graphic3d_ShaderProgram | None, theAspect: nanoocp.Graphic3d.Graphic3d_GroupAspect, theToOverrideDefaults: bool = False) -> bool:
        """
        Assign shader program for specified type of primitives.
        @param theProgram new program to set (might be NULL)
        @param theAspect  the type of primitives
        @param theToOverrideDefaults if true then non-overridden attributes using defaults will be
        allocated and copied from the Link;
        otherwise, only already customized attributes will be changed
        @return TRUE if presentation should be recomputed after creating aspects not previously
        customized (if theToOverrideDefaults is also TRUE)
        """

    def SetShadingModel(self, theModel: nanoocp.Graphic3d.Graphic3d_TypeOfShadingModel, theToOverrideDefaults: bool = False) -> bool:
        """Sets Shading Model type for the shading aspect."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @overload
    def SetHLRAngle(self, theAngle: float) -> None:
        """
        Deprecated in OCCT: SetDeviationAngle() should be used instead

        @name deprecated methods
        """

    @overload
    def SetHLRAngle(self) -> None:
        """Deprecated in OCCT: SetDeviationAngle() should be used instead"""

    def HLRAngle(self) -> float:
        """Deprecated in OCCT: DeviationAngle() should be used instead"""

    def HasOwnHLRDeviationAngle(self) -> bool:
        """Deprecated in OCCT: HasOwnDeviationAngle() should be used instead"""

    def PreviousHLRDeviationAngle(self) -> float:
        """Deprecated in OCCT: PreviousDeviationAngle() should be used instead"""

class Prs3d:
    """
    The Prs3d package provides the following services
    -   a presentation object (the context for all
    modifications to the display, its presentation will be
    displayed in every view of an active viewer)
    -   an attribute manager governing how objects such
    as color, width, and type of line are displayed;
    these are generic objects, whereas those in
    StdPrs are specific geometries and topologies.
    -   generic algorithms providing default settings for
    objects such as points, curves, surfaces and shapes
    -   a root object which provides the abstract
    framework for the DsgPrs definitions at work in
    display of dimensions, relations and trihedra.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d) -> None: ...

    @staticmethod
    def MatchSegment(X: float, Y: float, Z: float, aDistance: float, p1: nanoocp.gp.gp_Pnt, p2: nanoocp.gp.gp_Pnt) -> tuple[bool, float]:
        """
        draws an arrow at a given location, with respect
        to a given direction.
        """

    @overload
    @staticmethod
    def GetDeflection(theBndMin: nanoocp.BVH.BVH_Vec3d, theBndMax: nanoocp.BVH.BVH_Vec3d, theDeviationCoefficient: float) -> float:
        """
        Computes the absolute deflection value based on relative deflection
        Prs3d_Drawer::DeviationCoefficient().
        @param[in] theBndMin  bounding box min corner
        @param[in] theBndMax  bounding box max corner
        @param[in] theDeviationCoefficient  relative deflection coefficient from
        Prs3d_Drawer::DeviationCoefficient()
        @return absolute deflection coefficient based on bounding box dimensions
        """

    @overload
    @staticmethod
    def GetDeflection(theBndBox: nanoocp.Bnd.Bnd_Box, theDeviationCoefficient: float, theMaximalChordialDeviation: float) -> float:
        """
        Computes the absolute deflection value based on relative deflection
        Prs3d_Drawer::DeviationCoefficient().
        @param[in] theBndBox  bounding box
        @param[in] theDeviationCoefficient  relative deflection coefficient from
        Prs3d_Drawer::DeviationCoefficient()
        @param[in] theMaximalChordialDeviation  absolute deflection coefficient from
        Prs3d_Drawer::MaximalChordialDeviation()
        @return absolute deflection coefficient based on bounding box dimensions or
        theMaximalChordialDeviation if bounding box is Void or Infinite
        """

    @staticmethod
    def PrimitivesFromPolylines(thePoints: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> nanoocp.Graphic3d.Graphic3d_ArrayOfPrimitives:
        """
        Assembles array of primitives for sequence of polylines.
        @param[in] thePoints  the polylines sequence
        @return array of primitives
        """

    @staticmethod
    def AddPrimitivesGroup(thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None, theAspect: Prs3d_LineAspect | None, thePolylines: nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]) -> None:
        """
        Add primitives into new group in presentation and clear the list of polylines.
        """

    @staticmethod
    def AddFreeEdges(theSegments: nanoocp.NCollection.NCollection_Sequence[nanoocp.gp.gp_Pnt], thePolyTri: nanoocp.Poly.Poly_Triangulation | None, theLocation: nanoocp.gp.gp_Trsf) -> None:
        """
        Add triangulation free edges into sequence of line segments.
        @param[out] theSegments  sequence of line segments to fill
        @param[in] thePolyTri    triangulation to process
        @param[in] theLocation   transformation to apply
        """

class Prs3d_Arrow:
    """
    Provides class methods to draw an arrow at a given location, along a given direction and using a
    given angle.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d_Arrow) -> None: ...

    @staticmethod
    def DrawShaded(theAxis: nanoocp.gp.gp_Ax1, theTubeRadius: float, theAxisLength: float, theConeRadius: float, theConeLength: float, theNbFacettes: int) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Defines the representation of the arrow as shaded triangulation.
        @param theAxis       axis definition (arrow origin and direction)
        @param theTubeRadius tube (cylinder) radius
        @param theAxisLength overall arrow length (cylinder + cone)
        @param theConeRadius cone radius (arrow tip)
        @param theConeLength cone length (arrow tip)
        @param theNbFacettes tessellation quality for each part
        """

    @staticmethod
    def DrawSegments(theLocation: nanoocp.gp.gp_Pnt, theDir: nanoocp.gp.gp_Dir, theAngle: float, theLength: float, theNbSegments: int) -> nanoocp.Graphic3d.Graphic3d_ArrayOfSegments:
        """
        Defines the representation of the arrow as a container of segments.
        @param theLocation   location of the arrow tip
        @param theDir        direction of the arrow
        @param theAngle      angle of opening of the arrow head
        @param theLength     length of the arrow (from the tip)
        @param theNbSegments count of points on polyline where location is connected
        """

    @staticmethod
    def Draw(theGroup: nanoocp.Graphic3d.Graphic3d_Group | None, theLocation: nanoocp.gp.gp_Pnt, theDirection: nanoocp.gp.gp_Dir, theAngle: float, theLength: float) -> None:
        """
        Defines the representation of the arrow.
        Note that this method does NOT assign any presentation aspects to the primitives group!
        @param theGroup     presentation group to add primitives
        @param theLocation  location of the arrow tip
        @param theDirection direction of the arrow
        @param theAngle     angle of opening of the arrow head
        @param theLength    length of the arrow (from the tip)
        """

class Prs3d_BasicAspect(nanoocp.Standard.Standard_Transient):
    """
    All basic Prs3d_xxxAspect must inherits from this class
    The aspect classes qualifies how to represent a given kind of object.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_ArrowAspect(Prs3d_BasicAspect):
    """
    A framework for displaying arrows in representations of dimensions and relations.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty framework for displaying arrows
        in representations of lengths. The lengths displayed
        are either on their own or in chamfers, fillets,
        diameters and radii.
        """

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectLine3d | None) -> None: ...

    @overload
    def __init__(self, anAngle: float, aLength: float) -> None:
        """
        Constructs a framework to display an arrow with a
        shaft of the length aLength and having a head with
        sides at the angle anAngle from each other.
        """

    @overload
    def __init__(self, theOther: Prs3d_ArrowAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetAngle(self, anAngle: float) -> None:
        """defines the angle of the arrows."""

    def Angle(self) -> float:
        """returns the current value of the angle used when drawing an arrow."""

    def SetLength(self, theLength: float) -> None:
        """Defines the length of the arrows."""

    def Length(self) -> float:
        """Returns the current value of the length used when drawing an arrow."""

    def SetZoomable(self, theIsZoomable: bool) -> None:
        """Turns usage of arrow zoomable on/off"""

    def IsZoomable(self) -> bool:
        """Returns TRUE when the Arrow Zoomable is on; TRUE by default."""

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None: ...

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_AspectLine3d: ...

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectLine3d | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_Root:
    """
    A root class for the standard presentation algorithms of the StdPrs package.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d_Root) -> None: ...

    @staticmethod
    def CurrentGroup(thePrs3d: nanoocp.Graphic3d.Graphic3d_Structure | None) -> nanoocp.Graphic3d.Graphic3d_Group:
        """
        Deprecated in OCCT: This method is deprecated - Prs3d_Presentation::CurrentGroup() should be called instead
        """

    @staticmethod
    def NewGroup(thePrs3d: nanoocp.Graphic3d.Graphic3d_Structure | None) -> nanoocp.Graphic3d.Graphic3d_Group:
        """
        Deprecated in OCCT: This method is deprecated - Prs3d_Presentation::NewGroup() should be called instead
        """

class Prs3d_BndBox(Prs3d_Root):
    """Tool for computing bounding box presentation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d_BndBox) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theBndBox: nanoocp.Bnd.Bnd_Box, theDrawer: Prs3d_Drawer | None) -> None: ...

    @overload
    @staticmethod
    def Add(thePresentation: nanoocp.Graphic3d.Graphic3d_Structure | None, theBndBox: nanoocp.Bnd.Bnd_OBB, theDrawer: Prs3d_Drawer | None) -> None:
        """
        Computes presentation of a bounding box.
        @param[in] thePresentation  the presentation.
        @param[in] theBndBox  the bounding box.
        @param[in] theDrawer  the drawer.
        """

    @overload
    @staticmethod
    def FillSegments(theBox: nanoocp.Bnd.Bnd_OBB) -> nanoocp.Graphic3d.Graphic3d_ArrayOfSegments: ...

    @overload
    @staticmethod
    def FillSegments(theBox: nanoocp.Bnd.Bnd_Box) -> nanoocp.Graphic3d.Graphic3d_ArrayOfSegments:
        """
        Create primitive array with line segments for displaying a box.
        @param[in] theBox  the box to add
        """

    @overload
    @staticmethod
    def FillSegments(theSegments: nanoocp.Graphic3d.Graphic3d_ArrayOfSegments | None, theBox: nanoocp.Bnd.Bnd_OBB) -> None: ...

    @overload
    @staticmethod
    def FillSegments(theSegments: nanoocp.Graphic3d.Graphic3d_ArrayOfSegments | None, theBox: nanoocp.Bnd.Bnd_Box) -> None:
        """
        Create primitive array with line segments for displaying a box.
        @param[in][out] theSegments   primitive array to be filled;
        should be at least 8 nodes and 24 edges in size
        @param[in] theBox  the box to add
        """

    @staticmethod
    def fillSegments(theSegments: nanoocp.Graphic3d.Graphic3d_ArrayOfSegments | None, theBox: nanoocp.gp.gp_Pnt) -> None:
        """
        Create primitive array with line segments for displaying a box.
        @param[in][out] theSegments   primitive array to be filled;
        should be at least 8 nodes and 24 edges in size
        @param[in] theBox  the box to add
        """

class Prs3d_LineAspect(Prs3d_BasicAspect):
    """
    A framework for defining how a line will be displayed
    in a presentation. Aspects of line display include
    width, color and type of line.
    The definition set by this class is then passed to the
    attribute manager Prs3d_Drawer.
    Any object which requires a value for line aspect as
    an argument may then be given the attribute manager
    as a substitute argument in the form of a field such as myDrawer for example.
    """

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectLine3d | None) -> None: ...

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_TypeOfLine, theWidth: float) -> None:
        """
        Constructs a framework for line aspect defined by
        -   the color aColor
        -   the type of line aType and
        -   the line thickness aWidth.
        Type of line refers to whether the line is solid or dotted, for example.
        """

    @overload
    def __init__(self, theOther: Prs3d_LineAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets the line color defined at the time of construction.
        Default value: Quantity_NOC_YELLOW
        """

    def SetTypeOfLine(self, theType: nanoocp.Aspect.Aspect_TypeOfLine) -> None:
        """
        Sets the type of line defined at the time of construction.
        This could, for example, be solid, dotted or made up of dashes.
        Default value: Aspect_TOL_SOLID
        """

    def SetWidth(self, theWidth: float) -> None:
        """
        Sets the line width defined at the time of construction.
        Default value: 1.
        """

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_AspectLine3d:
        """
        Returns the line aspect. This is defined as the set of
        color, type and thickness attributes.
        """

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectLine3d | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_PointAspect(Prs3d_BasicAspect):
    """
    This class defines attributes for the points
    The points are drawn using markers, whose size does not depend on
    the zoom value of the views.
    """

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectMarker3d | None) -> None: ...

    @overload
    def __init__(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker, theColor: nanoocp.Quantity.Quantity_Color, theScale: float) -> None: ...

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theWidth: int, theHeight: int, theTexture: nanoocp.NCollection.NCollection_HArray1__unsigned_char | None) -> None:
        """Defines the user defined marker point."""

    @overload
    def __init__(self, theOther: Prs3d_PointAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        defines the color to be used when drawing a point.
        Default value: Quantity_NOC_YELLOW
        """

    def SetTypeOfMarker(self, theType: nanoocp.Aspect.Aspect_TypeOfMarker) -> None:
        """
        defines the type of representation to be used when drawing a point.
        Default value: Aspect_TOM_PLUS
        """

    def SetScale(self, theScale: float) -> None:
        """
        defines the size of the marker used when drawing a point.
        Default value: 1.
        """

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_AspectMarker3d: ...

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectMarker3d | None) -> None: ...

    def GetTextureSize(self) -> tuple[int, int]:
        """Returns marker's texture size."""

    def GetTexture(self) -> nanoocp.Graphic3d.Graphic3d_MarkerImage:
        """Returns marker's texture."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_ShadingAspect(Prs3d_BasicAspect):
    """
    A framework to define the display of shading.
    The attributes which make up this definition include:
    -   fill aspect
    -   color, and
    -   material
    """

    @overload
    def __init__(self) -> None:
        """Constructs an empty framework to display shading."""

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectFillArea3d | None) -> None:
        """Constructor with initialization."""

    @overload
    def __init__(self, theOther: Prs3d_ShadingAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColor(self, aColor: nanoocp.Quantity.Quantity_Color, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None:
        """Change the polygons interior color and material ambient color."""

    def SetMaterial(self, aMaterial: nanoocp.Graphic3d.Graphic3d_MaterialAspect, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None:
        """Change the polygons material aspect."""

    def SetTransparency(self, aValue: float, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_BOTH_SIDE) -> None:
        """
        Change the polygons transparency value.
        Warning : aValue must be in the range 0,1. 0 is the default (NO transparent)
        """

    def Color(self, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> nanoocp.Quantity.Quantity_Color:
        """Returns the polygons color."""

    def Material(self, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> nanoocp.Graphic3d.Graphic3d_MaterialAspect:
        """Returns the polygons material aspect."""

    def Transparency(self, aModel: nanoocp.Aspect.Aspect_TypeOfFacingModel = Aspect_TypeOfFacingModel.Aspect_TOFM_FRONT_SIDE) -> float:
        """Returns the polygons transparency value."""

    def ToUseVertexColorForBackFaces(self) -> bool:
        """
        Return true if per-vertex color should be applied to back-facing fragments.
        """

    def SetUseVertexColorForBackFaces(self, theToUse: bool) -> None:
        """
        Set whether per-vertex color should be applied to back-facing fragments.
        """

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_AspectFillArea3d:
        """Returns the polygons aspect properties."""

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectFillArea3d | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_TextAspect(Prs3d_BasicAspect):
    """Defines the attributes when displaying a text."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty framework for defining display attributes of text."""

    @overload
    def __init__(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectText3d | None) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d_TextAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """Sets the color of the type used in text display."""

    def SetFont(self, theFont: str) -> None:
        """Sets the font used in text display."""

    def SetHeight(self, theHeight: float) -> None:
        """Sets the height of the text."""

    def SetAngle(self, theAngle: float) -> None:
        """Sets the angle"""

    def Height(self) -> float:
        """Returns the height of the text box."""

    def Angle(self) -> float:
        """Returns the angle"""

    def SetHorizontalJustification(self, theJustification: nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment) -> None:
        """Sets horizontal alignment of text."""

    def SetVerticalJustification(self, theJustification: nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment) -> None:
        """Sets the vertical alignment of text."""

    def SetOrientation(self, theOrientation: nanoocp.Graphic3d.Graphic3d_TextPath) -> None:
        """Sets the orientation of text."""

    def HorizontalJustification(self) -> nanoocp.Graphic3d.Graphic3d_HorizontalTextAlignment:
        """
        Returns the horizontal alignment of the text.
        The range of values includes:
        -   left
        -   center
        -   right, and
        -   normal (justified).
        """

    def VerticalJustification(self) -> nanoocp.Graphic3d.Graphic3d_VerticalTextAlignment:
        """
        Returns the vertical alignment of the text.
        The range of values includes:
        -   normal
        -   top
        -   cap
        -   half
        -   base
        -   bottom
        """

    def Orientation(self) -> nanoocp.Graphic3d.Graphic3d_TextPath:
        """
        Returns the orientation of the text.
        Text can be displayed in the following directions:
        -   up
        -   down
        -   left, or
        -   right
        """

    def Aspect(self) -> nanoocp.Graphic3d.Graphic3d_AspectText3d:
        """
        Returns the purely textual attributes used in the display of text.
        These include:
        -   color
        -   font
        -   height/width ratio, that is, the expansion factor, and
        -   space between characters.
        """

    def SetAspect(self, theAspect: nanoocp.Graphic3d.Graphic3d_AspectText3d | None) -> None: ...

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_DatumAspect(Prs3d_BasicAspect):
    """A framework to define the display of datums."""

    @overload
    def __init__(self) -> None:
        """An empty constructor."""

    @overload
    def __init__(self, theOther: Prs3d_DatumAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LineAspect(self, thePart: Prs3d_DatumParts) -> Prs3d_LineAspect:
        """Returns line aspect for specified part."""

    def ShadingAspect(self, thePart: Prs3d_DatumParts) -> Prs3d_ShadingAspect:
        """Returns shading aspect for specified part."""

    @overload
    def TextAspect(self, thePart: Prs3d_DatumParts) -> Prs3d_TextAspect:
        """
        Returns the text attributes for rendering label of specified part
        (Prs3d_DatumParts_XAxis/Prs3d_DatumParts_YAxis/Prs3d_DatumParts_ZAxis).
        """

    @overload
    def TextAspect(self) -> Prs3d_TextAspect:
        """
        Deprecated in OCCT: This method is deprecated - TextAspect() with axis parameter should be called instead

        Returns the text attributes for rendering labels.
        """

    def SetTextAspect(self, theTextAspect: Prs3d_TextAspect | None) -> None:
        """Sets text attributes for rendering labels."""

    def PointAspect(self) -> Prs3d_PointAspect:
        """Returns the point aspect of origin wireframe presentation"""

    def SetPointAspect(self, theAspect: Prs3d_PointAspect | None) -> None:
        """Returns the point aspect of origin wireframe presentation"""

    def ArrowAspect(self) -> Prs3d_ArrowAspect:
        """Returns the arrow aspect of presentation."""

    def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect | None) -> None:
        """Sets the arrow aspect of presentation"""

    def DrawDatumPart(self, thePart: Prs3d_DatumParts) -> bool:
        """Returns true if the given part is used in axes of aspect"""

    def SetDrawDatumAxes(self, theType: Prs3d_DatumAxes) -> None:
        """Sets the axes used in the datum aspect"""

    def DatumAxes(self) -> Prs3d_DatumAxes:
        """Returns axes used in the datum aspect"""

    def Attribute(self, theType: Prs3d_DatumAttribute) -> float:
        """Returns the attribute of the datum type"""

    def SetAttribute(self, theType: Prs3d_DatumAttribute, theValue: float) -> None:
        """Sets the attribute of the datum type"""

    def AxisLength(self, thePart: Prs3d_DatumParts) -> float:
        """Returns the length of the displayed first axis."""

    def SetAxisLength(self, theL1: float, theL2: float, theL3: float) -> None:
        """Sets the lengths of the three axes."""

    def ToDrawLabels(self) -> bool:
        """@return true if axes labels are drawn; TRUE by default."""

    def SetDrawLabels(self, theToDraw: bool) -> None:
        """Sets option to draw or not to draw text labels for axes"""

    def SetToDrawLabels(self, theToDraw: bool) -> None: ...

    def ToDrawArrows(self) -> bool:
        """@return true if axes arrows are drawn; TRUE by default."""

    def SetDrawArrows(self, theToDraw: bool) -> None:
        """Sets option to draw or not arrows for axes"""

    def CopyAspectsFrom(self, theOther: Prs3d_DatumAspect | None) -> None:
        """Performs deep copy of attributes from another aspect instance."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def ArrowPartForAxis(thePart: Prs3d_DatumParts) -> Prs3d_DatumParts:
        """Returns type of arrow for a type of axis"""

class Prs3d_DimensionAspect(Prs3d_BasicAspect):
    """defines the attributes when drawing a Length Presentation."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty framework to define the display of dimensions."""

    @overload
    def __init__(self, theOther: Prs3d_DimensionAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LineAspect(self) -> Prs3d_LineAspect:
        """
        Returns the settings for the display of lines used in presentation of dimensions.
        """

    def SetLineAspect(self, theAspect: Prs3d_LineAspect | None) -> None:
        """
        Sets the display attributes of lines used in presentation of dimensions.
        """

    def TextAspect(self) -> Prs3d_TextAspect:
        """
        Returns the settings for the display of text used in presentation of dimensions.
        """

    def SetTextAspect(self, theAspect: Prs3d_TextAspect | None) -> None:
        """
        Sets the display attributes of text used in presentation of dimensions.
        """

    def IsText3d(self) -> bool:
        """Check if text for dimension label is 3d."""

    def MakeText3d(self, isText3d: bool) -> None:
        """Sets type of text."""

    def IsTextShaded(self) -> bool:
        """Check if 3d text for dimension label is shaded."""

    def MakeTextShaded(self, theIsTextShaded: bool) -> None:
        """Turns on/off text shading for 3d text."""

    def IsArrows3d(self) -> bool:
        """Gets type of arrows."""

    def MakeArrows3d(self, theIsArrows3d: bool) -> None:
        """Sets type of arrows."""

    def IsUnitsDisplayed(self) -> bool:
        """Shows if Units are to be displayed along with dimension value."""

    def MakeUnitsDisplayed(self, theIsDisplayed: bool) -> None:
        """
        Specifies whether the units string should be displayed
        along with value label or not.
        """

    def SetArrowOrientation(self, theArrowOrient: Prs3d_DimensionArrowOrientation) -> None:
        """
        Sets orientation of arrows (external or internal).
        By default orientation is chosen automatically according to situation and text label size.
        """

    def ArrowOrientation(self) -> Prs3d_DimensionArrowOrientation:
        """Gets orientation of arrows (external or internal)."""

    def SetTextVerticalPosition(self, thePosition: Prs3d_DimensionTextVerticalPosition) -> None:
        """Sets vertical text alignment for text label."""

    def TextVerticalPosition(self) -> Prs3d_DimensionTextVerticalPosition:
        """Gets vertical text alignment for text label."""

    def SetTextHorizontalPosition(self, thePosition: Prs3d_DimensionTextHorizontalPosition) -> None:
        """Sets horizontal text alignment for text label."""

    def TextHorizontalPosition(self) -> Prs3d_DimensionTextHorizontalPosition:
        """Gets horizontal text alignment for text label."""

    def ArrowAspect(self) -> Prs3d_ArrowAspect:
        """Returns the settings for displaying arrows."""

    def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect | None) -> None:
        """
        Sets the display attributes of arrows used in presentation of dimensions.
        """

    def SetCommonColor(self, theColor: nanoocp.Quantity.Quantity_Color) -> None:
        """
        Sets the same color for all parts of dimension: lines, arrows and text.
        """

    def SetExtensionSize(self, theSize: float) -> None:
        """Sets extension size."""

    def ExtensionSize(self) -> float:
        """Returns extension size."""

    def SetArrowTailSize(self, theSize: float) -> None:
        """Set size for arrow tail (extension without text)."""

    def ArrowTailSize(self) -> float:
        """Returns arrow tail size."""

    def SetValueStringFormat(self, theFormat: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets "Sprintf"-syntax format for formatting dimension value labels."""

    def ValueStringFormat(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns format."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_InvalidAngle(nanoocp.Standard.Standard_RangeError):
    pass

class Prs3d_IsoAspect(Prs3d_LineAspect):
    """
    A framework to define the display attributes of isoparameters.
    This framework can be used to modify the default
    setting for isoparameters in Prs3d_Drawer.
    """

    @overload
    def __init__(self, theColor: nanoocp.Quantity.Quantity_Color, theType: nanoocp.Aspect.Aspect_TypeOfLine, theWidth: float, theNumber: int) -> None:
        """
        Constructs a framework to define display attributes of isoparameters.
        These include:
        -   the color attribute aColor
        -   the type of line aType
        -   the width value aWidth
        -   aNumber, the number of isoparameters to be displayed.
        """

    @overload
    def __init__(self, theOther: Prs3d_IsoAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetNumber(self, theNumber: int) -> None:
        """
        defines the number of U or V isoparametric curves
        to be drawn for a single face.
        Default value: 10
        """

    def Number(self) -> int:
        """
        returns the number of U or V isoparametric curves drawn for a single face.
        """

class Prs3d_PlaneAspect(Prs3d_BasicAspect):
    """A framework to define the display of planes."""

    @overload
    def __init__(self) -> None:
        """Constructs an empty framework for the display of planes."""

    @overload
    def __init__(self, theOther: Prs3d_PlaneAspect) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def EdgesAspect(self) -> Prs3d_LineAspect:
        """
        Returns the attributes of displayed edges involved in the presentation of planes.
        """

    def IsoAspect(self) -> Prs3d_LineAspect:
        """
        Returns the attributes of displayed isoparameters involved in the presentation of planes.
        """

    def ArrowAspect(self) -> Prs3d_LineAspect:
        """Returns the settings for displaying an arrow."""

    def SetArrowsLength(self, theLength: float) -> None: ...

    def ArrowsLength(self) -> float:
        """Returns the length of the arrow shaft used in the display of arrows."""

    def SetArrowsSize(self, theSize: float) -> None:
        """Sets the angle of the arrowhead used in the display of planes."""

    def ArrowsSize(self) -> float:
        """Returns the size of arrows used in the display of planes."""

    def SetArrowsAngle(self, theAngle: float) -> None:
        """
        Sets the angle of the arrowhead used in the display
        of arrows involved in the presentation of planes.
        """

    def ArrowsAngle(self) -> float:
        """
        Returns the angle of the arrowhead used in the
        display of arrows involved in the presentation of planes.
        """

    def SetDisplayCenterArrow(self, theToDraw: bool) -> None:
        """Sets the display attributes defined in DisplayCenterArrow to active."""

    def DisplayCenterArrow(self) -> bool:
        """Returns true if the display of center arrows is allowed."""

    def SetDisplayEdgesArrows(self, theToDraw: bool) -> None:
        """Sets the display attributes defined in DisplayEdgesArrows to active."""

    def DisplayEdgesArrows(self) -> bool:
        """Returns true if the display of edge arrows is allowed."""

    def SetDisplayEdges(self, theToDraw: bool) -> None: ...

    def DisplayEdges(self) -> bool: ...

    def SetDisplayIso(self, theToDraw: bool) -> None:
        """Sets the display attributes defined in DisplayIso to active."""

    def DisplayIso(self) -> bool:
        """Returns true if the display of isoparameters is allowed."""

    def SetPlaneLength(self, theLX: float, theLY: float) -> None: ...

    def PlaneXLength(self) -> float:
        """Returns the length of the x axis used in the display of planes."""

    def PlaneYLength(self) -> float:
        """Returns the length of the y axis used in the display of planes."""

    def SetIsoDistance(self, theL: float) -> None:
        """
        Sets the distance L between isoparameters used in the display of planes.
        """

    def IsoDistance(self) -> float:
        """
        Returns the distance between isoparameters used in the display of planes.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_PresentationShadow(nanoocp.Graphic3d.Graphic3d_Structure):
    """
    Defines a "shadow" of existing presentation object with custom aspects.
    """

    @overload
    def __init__(self, theViewer: nanoocp.Graphic3d.Graphic3d_StructureManager | None, thePrs: nanoocp.Graphic3d.Graphic3d_Structure | None) -> None:
        """Constructs a shadow of existing presentation object."""

    @overload
    def __init__(self, theOther: Prs3d_PresentationShadow) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ParentId(self) -> int:
        """Returns the id of the parent presentation"""

    def ParentAffinity(self) -> nanoocp.Graphic3d.Graphic3d_ViewAffinity:
        """Returns view affinity of the parent presentation"""

    def CalculateBoundBox(self) -> None:
        """
        Do nothing - axis-aligned bounding box should be initialized from parent structure.
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

class Prs3d_Text:
    """A framework to define the display of texts."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Prs3d_Text) -> None: ...

    @overload
    @staticmethod
    def Draw(theGroup: nanoocp.Graphic3d.Graphic3d_Group | None, theAspect: Prs3d_TextAspect | None, theText: nanoocp.TCollection.TCollection_ExtendedString, theAttachmentPoint: nanoocp.gp.gp_Pnt) -> nanoocp.Graphic3d.Graphic3d_Text:
        """
        Defines the display of the text.
        @param theGroup  group to add primitives
        @param theAspect presentation attributes
        @param theText   text to draw
        @param theAttachmentPoint attachment point
        @return text to draw
        """

    @overload
    @staticmethod
    def Draw(theGroup: nanoocp.Graphic3d.Graphic3d_Group | None, theAspect: Prs3d_TextAspect | None, theText: nanoocp.TCollection.TCollection_ExtendedString, theOrientation: nanoocp.gp.gp_Ax2, theHasOwnAnchor: bool = True) -> nanoocp.Graphic3d.Graphic3d_Text:
        """
        Draws the text label.
        @param theGroup       group to add primitives
        @param theAspect      presentation attributes
        @param theText        text to draw
        @param theOrientation location and orientation specified in the model 3D space
        @param theHasOwnAnchor
        @return text to draw
        """

class Prs3d_ToolQuadric:
    """Base class to build 3D surfaces presentation of quadric surfaces."""

    @staticmethod
    def TrianglesNb_s(theSlicesNb: int, theStacksNb: int) -> int:
        """Return number of triangles for presentation with the given params."""

    @staticmethod
    def VerticesNb_s(theSlicesNb: int, theStacksNb: int, theIsIndexed: bool = True) -> int:
        """Return number of vertices for presentation with the given params."""

    def CreateTriangulation(self, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface presentation.
        @param[in] theTrsf  optional transformation to apply
        @return generated triangulation
        """

    def CreatePolyTriangulation(self, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Poly.Poly_Triangulation:
        """
        Generate primitives for 3D quadric surface presentation.
        @param[in] theTrsf  optional transformation to apply
        @return generated triangulation
        """

    def FillArray__Graphic3d_ArrayOfTriangles(self, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        FillArray__Graphic3d_ArrayOfTriangles: the C++ overload FillArray(occ::handle<Graphic3d_ArrayOfTriangles> &, const gp_Trsf &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Generate primitives for 3D quadric surface and fill the given array.
        @param[in][out] theArray  the array of vertices;
        when NULL, function will create an indexed array;
        when not NULL, triangles will be appended to the end of array
        (will raise an exception if reserved array size is not large enough)
        @param[in] theTrsf  optional transformation to apply
        """

    def TrianglesNb(self) -> int:
        """Return number of triangles in generated presentation."""

    def VerticesNb(self, theIsIndexed: bool = True) -> int:
        """Return number of vertices in generated presentation."""

    def FillArray__Graphic3d_ArrayOfTriangles__Poly_Triangulation(self, theTrsf: nanoocp.gp.gp_Trsf) -> tuple[nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles, nanoocp.Poly.Poly_Triangulation]:
        """
        FillArray__Graphic3d_ArrayOfTriangles__Poly_Triangulation: the C++ overload FillArray(occ::handle<Graphic3d_ArrayOfTriangles> &, occ::handle<Poly_Triangulation> &, const gp_Trsf &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Deprecated in OCCT: Deprecated method, CreateTriangulation() and CreatePolyTriangulation() should be used instead

        Generate primitives for 3D quadric surface presentation.
        @param[out] theArray  generated array of triangles
        @param[out] theTriangulation  generated triangulation
        @param[in] theTrsf  optional transformation to apply
        """

class Prs3d_ToolDisk(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for disk surface.
    """

    @overload
    def __init__(self, theInnerRadius: float, theOuterRadius: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a disk.
        @param[in] theInnerRadius  inner disk radius
        @param[in] theOuterRadius  outer disk radius
        @param[in] theNbSlices     number of slices within U parameter
        @param[in] theNbStacks     number of stacks within V parameter
        """

    @overload
    def __init__(self, theOther: Prs3d_ToolDisk) -> None: ...

    @staticmethod
    def Create(theInnerRadius: float, theOuterRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface.
        @param[in] theInnerRadius  inner disc radius
        @param[in] theOuterRadius  outer disc radius
        @param[in] theNbSlices     number of slices within U parameter
        @param[in] theNbStacks     number of stacks within V parameter
        @param[in] theTrsf         optional transformation to apply
        @return generated triangulation
        """

    def SetAngleRange(self, theStartAngle: float, theEndAngle: float) -> None:
        """
        Set angle range in radians [0, 2*PI] by default.
        @param[in] theStartAngle  Start angle in counter clockwise order
        @param[in] theEndAngle    End   angle in counter clockwise order
        """

class Prs3d_ToolCylinder(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for cylindrical surface.
    """

    @overload
    def __init__(self, theBottomRad: float, theTopRad: float, theHeight: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a cylinder.
        @param[in] theBottomRad  cylinder bottom radius
        @param[in] theTopRad     cylinder top radius
        @param[in] theHeight     cylinder height
        @param[in] theNbSlices   number of slices within U parameter
        @param[in] theNbStacks   number of stacks within V parameter
        """

    @overload
    def __init__(self, theOther: Prs3d_ToolCylinder) -> None: ...

    @staticmethod
    def Create(theBottomRad: float, theTopRad: float, theHeight: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface and return a filled array.
        @param[in] theBottomRad  cylinder bottom radius
        @param[in] theTopRad     cylinder top radius
        @param[in] theHeight     cylinder height
        @param[in] theNbSlices   number of slices within U parameter
        @param[in] theNbStacks   number of stacks within V parameter
        @param[in] theTrsf       optional transformation to apply
        @return generated triangulation
        """

class Prs3d_ToolSector(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for disk surface.
    """

    @overload
    def __init__(self, theRadius: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a sector (quadrant).
        @param[in] theRadius    sector radius
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theOther: Prs3d_ToolSector) -> None: ...

    @staticmethod
    def Create(theRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface.
        @param[in] theRadius    sector radius
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

class Prs3d_ToolSphere(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for spherical surface.
    """

    @overload
    def __init__(self, theRadius: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a sphere.
        @param[in] theRadius    sphere radius
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theOther: Prs3d_ToolSphere) -> None: ...

    @staticmethod
    def Create(theRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface.
        @param[in] theRadius    sphere radius
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

class Prs3d_ToolTorus(Prs3d_ToolQuadric):
    """
    Standard presentation algorithm that outputs graphical primitives for torus surface.
    """

    @overload
    def __init__(self, theMajorRad: float, theMinorRad: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a complete torus.
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theMajorRad: float, theMinorRad: float, theAngle: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a torus pipe segment.
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle     angle to create a torus pipe segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theMajorRad: float, theMinorRad: float, theAngle1: float, theAngle2: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a torus ring segment.
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle1    first  angle to create a torus ring segment
        @param[in] theAngle2    second angle to create a torus ring segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theMajorRad: float, theMinorRad: float, theAngle1: float, theAngle2: float, theAngle: float, theNbSlices: int, theNbStacks: int) -> None:
        """
        Initializes the algorithm creating a torus ring segment.
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle1    first  angle to create a torus ring segment
        @param[in] theAngle2    second angle to create a torus ring segment
        @param[in] theAngle     angle to create a torus pipe segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        """

    @overload
    def __init__(self, theOther: Prs3d_ToolTorus) -> None: ...

    @overload
    @staticmethod
    def Create(theMajorRad: float, theMinorRad: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface (complete torus).
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

    @overload
    @staticmethod
    def Create(theMajorRad: float, theMinorRad: float, theAngle: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface (torus segment).
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle     angle to create a torus pipe segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

    @overload
    @staticmethod
    def Create(theMajorRad: float, theMinorRad: float, theAngle1: float, theAngle2: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface (torus ring segment).
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle1    first  angle to create a torus ring segment
        @param[in] theAngle2    second angle to create a torus ring segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

    @overload
    @staticmethod
    def Create(theMajorRad: float, theMinorRad: float, theAngle1: float, theAngle2: float, theAngle: float, theNbSlices: int, theNbStacks: int, theTrsf: nanoocp.gp.gp_Trsf) -> nanoocp.Graphic3d.Graphic3d_ArrayOfTriangles:
        """
        Generate primitives for 3D quadric surface (segment of the torus ring segment).
        @param[in] theMajorRad  distance from the center of the pipe to the center of the torus
        @param[in] theMinorRad  radius of the pipe
        @param[in] theAngle1    first  angle to create a torus ring segment
        @param[in] theAngle2    second angle to create a torus ring segment
        @param[in] theAngle     angle to create a torus pipe segment
        @param[in] theNbSlices  number of slices within U parameter
        @param[in] theNbStacks  number of stacks within V parameter
        @param[in] theTrsf      optional transformation to apply
        @return generated triangulation
        """

# C++ typedef aliases
Prs3d_Presentation = nanoocp.Graphic3d.Graphic3d_Structure

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
Prs3d_NListOfSequenceOfPnt = nanoocp.NCollection.NCollection_List[nanoocp.NCollection.NCollection_HSequence[nanoocp.gp.gp_Pnt]]
