"""OCCT package XCAFDimTolObjects (toolkit TKXCAF)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TDocStd
import nanoocp.TopoDS
import nanoocp.gp


class XCAFDimTolObjects_DatumTargetType(enum.IntEnum):
    """Defines types of dimension"""

    XCAFDimTolObjects_DatumTargetType_Point = 0

    XCAFDimTolObjects_DatumTargetType_Line = 1

    XCAFDimTolObjects_DatumTargetType_Rectangle = 2

    XCAFDimTolObjects_DatumTargetType_Circle = 3

    XCAFDimTolObjects_DatumTargetType_Area = 4

XCAFDimTolObjects_DatumTargetType_Point: XCAFDimTolObjects_DatumTargetType = ...

XCAFDimTolObjects_DatumTargetType_Line: XCAFDimTolObjects_DatumTargetType = ...

XCAFDimTolObjects_DatumTargetType_Rectangle: XCAFDimTolObjects_DatumTargetType = ...

XCAFDimTolObjects_DatumTargetType_Circle: XCAFDimTolObjects_DatumTargetType = ...

XCAFDimTolObjects_DatumTargetType_Area: XCAFDimTolObjects_DatumTargetType = ...

class XCAFDimTolObjects_DatumSingleModif(enum.IntEnum):
    """Defines modifirs"""

    XCAFDimTolObjects_DatumSingleModif_AnyCrossSection = 0

    XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection = 1

    XCAFDimTolObjects_DatumSingleModif_Basic = 2

    XCAFDimTolObjects_DatumSingleModif_ContactingFeature = 3

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU = 4

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV = 5

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW = 6

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX = 7

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY = 8

    XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ = 9

    XCAFDimTolObjects_DatumSingleModif_DistanceVariable = 10

    XCAFDimTolObjects_DatumSingleModif_FreeState = 11

    XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement = 12

    XCAFDimTolObjects_DatumSingleModif_Line = 13

    XCAFDimTolObjects_DatumSingleModif_MajorDiameter = 14

    XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement = 15

    XCAFDimTolObjects_DatumSingleModif_MinorDiameter = 16

    XCAFDimTolObjects_DatumSingleModif_Orientation = 17

    XCAFDimTolObjects_DatumSingleModif_PitchDiameter = 18

    XCAFDimTolObjects_DatumSingleModif_Plane = 19

    XCAFDimTolObjects_DatumSingleModif_Point = 20

    XCAFDimTolObjects_DatumSingleModif_Translation = 21

XCAFDimTolObjects_DatumSingleModif_AnyCrossSection: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Any_LongitudinalSection: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Basic: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_ContactingFeature: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintU: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintV: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintW: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintX: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintY: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DegreeOfFreedomConstraintZ: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_DistanceVariable: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_FreeState: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_LeastMaterialRequirement: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Line: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_MajorDiameter: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_MaximumMaterialRequirement: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_MinorDiameter: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Orientation: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_PitchDiameter: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Plane: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Point: XCAFDimTolObjects_DatumSingleModif = ...

XCAFDimTolObjects_DatumSingleModif_Translation: XCAFDimTolObjects_DatumSingleModif = ...

class XCAFDimTolObjects_DatumModifWithValue(enum.IntEnum):
    """Defines modifirs"""

    XCAFDimTolObjects_DatumModifWithValue_None = 0

    XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical = 1

    XCAFDimTolObjects_DatumModifWithValue_Distance = 2

    XCAFDimTolObjects_DatumModifWithValue_Projected = 3

    XCAFDimTolObjects_DatumModifWithValue_Spherical = 4

XCAFDimTolObjects_DatumModifWithValue_None: XCAFDimTolObjects_DatumModifWithValue = ...

XCAFDimTolObjects_DatumModifWithValue_CircularOrCylindrical: XCAFDimTolObjects_DatumModifWithValue = ...

XCAFDimTolObjects_DatumModifWithValue_Distance: XCAFDimTolObjects_DatumModifWithValue = ...

XCAFDimTolObjects_DatumModifWithValue_Projected: XCAFDimTolObjects_DatumModifWithValue = ...

XCAFDimTolObjects_DatumModifWithValue_Spherical: XCAFDimTolObjects_DatumModifWithValue = ...

class XCAFDimTolObjects_DimensionType(enum.IntEnum):
    """Defines types of dimension"""

    XCAFDimTolObjects_DimensionType_Location_None = 0

    XCAFDimTolObjects_DimensionType_Location_CurvedDistance = 1

    XCAFDimTolObjects_DimensionType_Location_LinearDistance = 2

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter = 3

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner = 4

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter = 5

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter = 6

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner = 7

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter = 8

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter = 9

    XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner = 10

    XCAFDimTolObjects_DimensionType_Location_Angular = 11

    XCAFDimTolObjects_DimensionType_Location_Oriented = 12

    XCAFDimTolObjects_DimensionType_Location_WithPath = 13

    XCAFDimTolObjects_DimensionType_Size_CurveLength = 14

    XCAFDimTolObjects_DimensionType_Size_Diameter = 15

    XCAFDimTolObjects_DimensionType_Size_SphericalDiameter = 16

    XCAFDimTolObjects_DimensionType_Size_Radius = 17

    XCAFDimTolObjects_DimensionType_Size_SphericalRadius = 18

    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter = 19

    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter = 20

    XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius = 21

    XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius = 22

    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter = 23

    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter = 24

    XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius = 25

    XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius = 26

    XCAFDimTolObjects_DimensionType_Size_Thickness = 27

    XCAFDimTolObjects_DimensionType_Size_Angular = 28

    XCAFDimTolObjects_DimensionType_Size_WithPath = 29

    XCAFDimTolObjects_DimensionType_CommonLabel = 30

    XCAFDimTolObjects_DimensionType_DimensionPresentation = 31

XCAFDimTolObjects_DimensionType_Location_None: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_CurvedDistance: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToOuter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromCenterToInner: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToCenter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToOuter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromOuterToInner: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToCenter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToOuter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_LinearDistance_FromInnerToInner: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_Angular: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_Oriented: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Location_WithPath: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_CurveLength: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_Diameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_SphericalDiameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_Radius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_SphericalRadius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalMinorDiameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalMajorDiameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalMinorRadius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalMajorRadius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorDiameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorDiameter: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalHighMajorRadius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_ToroidalLowMajorRadius: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_Thickness: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_Angular: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_Size_WithPath: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_CommonLabel: XCAFDimTolObjects_DimensionType = ...

XCAFDimTolObjects_DimensionType_DimensionPresentation: XCAFDimTolObjects_DimensionType = ...

class XCAFDimTolObjects_DimensionQualifier(enum.IntEnum):
    """Defines types of qualifier"""

    XCAFDimTolObjects_DimensionQualifier_None = 0

    XCAFDimTolObjects_DimensionQualifier_Min = 1

    XCAFDimTolObjects_DimensionQualifier_Max = 2

    XCAFDimTolObjects_DimensionQualifier_Avg = 3

XCAFDimTolObjects_DimensionQualifier_None: XCAFDimTolObjects_DimensionQualifier = ...

XCAFDimTolObjects_DimensionQualifier_Min: XCAFDimTolObjects_DimensionQualifier = ...

XCAFDimTolObjects_DimensionQualifier_Max: XCAFDimTolObjects_DimensionQualifier = ...

XCAFDimTolObjects_DimensionQualifier_Avg: XCAFDimTolObjects_DimensionQualifier = ...

class XCAFDimTolObjects_DimensionFormVariance(enum.IntEnum):
    """Defines value of form variance"""

    XCAFDimTolObjects_DimensionFormVariance_None = 0

    XCAFDimTolObjects_DimensionFormVariance_A = 1

    XCAFDimTolObjects_DimensionFormVariance_B = 2

    XCAFDimTolObjects_DimensionFormVariance_C = 3

    XCAFDimTolObjects_DimensionFormVariance_CD = 4

    XCAFDimTolObjects_DimensionFormVariance_D = 5

    XCAFDimTolObjects_DimensionFormVariance_E = 6

    XCAFDimTolObjects_DimensionFormVariance_EF = 7

    XCAFDimTolObjects_DimensionFormVariance_F = 8

    XCAFDimTolObjects_DimensionFormVariance_FG = 9

    XCAFDimTolObjects_DimensionFormVariance_G = 10

    XCAFDimTolObjects_DimensionFormVariance_H = 11

    XCAFDimTolObjects_DimensionFormVariance_JS = 12

    XCAFDimTolObjects_DimensionFormVariance_J = 13

    XCAFDimTolObjects_DimensionFormVariance_K = 14

    XCAFDimTolObjects_DimensionFormVariance_M = 15

    XCAFDimTolObjects_DimensionFormVariance_N = 16

    XCAFDimTolObjects_DimensionFormVariance_P = 17

    XCAFDimTolObjects_DimensionFormVariance_R = 18

    XCAFDimTolObjects_DimensionFormVariance_S = 19

    XCAFDimTolObjects_DimensionFormVariance_T = 20

    XCAFDimTolObjects_DimensionFormVariance_U = 21

    XCAFDimTolObjects_DimensionFormVariance_V = 22

    XCAFDimTolObjects_DimensionFormVariance_X = 23

    XCAFDimTolObjects_DimensionFormVariance_Y = 24

    XCAFDimTolObjects_DimensionFormVariance_Z = 25

    XCAFDimTolObjects_DimensionFormVariance_ZA = 26

    XCAFDimTolObjects_DimensionFormVariance_ZB = 27

    XCAFDimTolObjects_DimensionFormVariance_ZC = 28

XCAFDimTolObjects_DimensionFormVariance_None: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_A: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_B: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_C: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_CD: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_D: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_E: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_EF: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_F: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_FG: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_G: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_H: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_JS: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_J: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_K: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_M: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_N: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_P: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_R: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_S: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_T: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_U: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_V: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_X: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_Y: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_Z: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_ZA: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_ZB: XCAFDimTolObjects_DimensionFormVariance = ...

XCAFDimTolObjects_DimensionFormVariance_ZC: XCAFDimTolObjects_DimensionFormVariance = ...

class XCAFDimTolObjects_DimensionGrade(enum.IntEnum):
    """Defines value of grade"""

    XCAFDimTolObjects_DimensionGrade_IT01 = 0

    XCAFDimTolObjects_DimensionGrade_IT0 = 1

    XCAFDimTolObjects_DimensionGrade_IT1 = 2

    XCAFDimTolObjects_DimensionGrade_IT2 = 3

    XCAFDimTolObjects_DimensionGrade_IT3 = 4

    XCAFDimTolObjects_DimensionGrade_IT4 = 5

    XCAFDimTolObjects_DimensionGrade_IT5 = 6

    XCAFDimTolObjects_DimensionGrade_IT6 = 7

    XCAFDimTolObjects_DimensionGrade_IT7 = 8

    XCAFDimTolObjects_DimensionGrade_IT8 = 9

    XCAFDimTolObjects_DimensionGrade_IT9 = 10

    XCAFDimTolObjects_DimensionGrade_IT10 = 11

    XCAFDimTolObjects_DimensionGrade_IT11 = 12

    XCAFDimTolObjects_DimensionGrade_IT12 = 13

    XCAFDimTolObjects_DimensionGrade_IT13 = 14

    XCAFDimTolObjects_DimensionGrade_IT14 = 15

    XCAFDimTolObjects_DimensionGrade_IT15 = 16

    XCAFDimTolObjects_DimensionGrade_IT16 = 17

    XCAFDimTolObjects_DimensionGrade_IT17 = 18

    XCAFDimTolObjects_DimensionGrade_IT18 = 19

XCAFDimTolObjects_DimensionGrade_IT01: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT0: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT1: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT2: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT3: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT4: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT5: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT6: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT7: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT8: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT9: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT10: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT11: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT12: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT13: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT14: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT15: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT16: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT17: XCAFDimTolObjects_DimensionGrade = ...

XCAFDimTolObjects_DimensionGrade_IT18: XCAFDimTolObjects_DimensionGrade = ...

class XCAFDimTolObjects_DimensionModif(enum.IntEnum):
    """Defines modifirs"""

    XCAFDimTolObjects_DimensionModif_ControlledRadius = 0

    XCAFDimTolObjects_DimensionModif_Square = 1

    XCAFDimTolObjects_DimensionModif_StatisticalTolerance = 2

    XCAFDimTolObjects_DimensionModif_ContinuousFeature = 3

    XCAFDimTolObjects_DimensionModif_TwoPointSize = 4

    XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere = 5

    XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion = 6

    XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation = 7

    XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation = 8

    XCAFDimTolObjects_DimensionModif_CircumferenceDiameter = 9

    XCAFDimTolObjects_DimensionModif_AreaDiameter = 10

    XCAFDimTolObjects_DimensionModif_VolumeDiameter = 11

    XCAFDimTolObjects_DimensionModif_MaximumSize = 12

    XCAFDimTolObjects_DimensionModif_MinimumSize = 13

    XCAFDimTolObjects_DimensionModif_AverageSize = 14

    XCAFDimTolObjects_DimensionModif_MedianSize = 15

    XCAFDimTolObjects_DimensionModif_MidRangeSize = 16

    XCAFDimTolObjects_DimensionModif_RangeOfSizes = 17

    XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature = 18

    XCAFDimTolObjects_DimensionModif_AnyCrossSection = 19

    XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection = 20

    XCAFDimTolObjects_DimensionModif_CommonTolerance = 21

    XCAFDimTolObjects_DimensionModif_FreeStateCondition = 22

    XCAFDimTolObjects_DimensionModif_Between = 23

XCAFDimTolObjects_DimensionModif_ControlledRadius: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_Square: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_StatisticalTolerance: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_ContinuousFeature: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_TwoPointSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_LocalSizeDefinedBySphere: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_LeastSquaresAssociationCriterion: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MaximumInscribedAssociation: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MinimumCircumscribedAssociation: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_CircumferenceDiameter: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_AreaDiameter: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_VolumeDiameter: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MaximumSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MinimumSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_AverageSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MedianSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_MidRangeSize: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_RangeOfSizes: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_AnyRestrictedPortionOfFeature: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_AnyCrossSection: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_SpecificFixedCrossSection: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_CommonTolerance: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_FreeStateCondition: XCAFDimTolObjects_DimensionModif = ...

XCAFDimTolObjects_DimensionModif_Between: XCAFDimTolObjects_DimensionModif = ...

class XCAFDimTolObjects_AngularQualifier(enum.IntEnum):
    """Defines types of qualifier for angular dimensions"""

    XCAFDimTolObjects_AngularQualifier_None = 0

    XCAFDimTolObjects_AngularQualifier_Small = 1

    XCAFDimTolObjects_AngularQualifier_Large = 2

    XCAFDimTolObjects_AngularQualifier_Equal = 3

XCAFDimTolObjects_AngularQualifier_None: XCAFDimTolObjects_AngularQualifier = ...

XCAFDimTolObjects_AngularQualifier_Small: XCAFDimTolObjects_AngularQualifier = ...

XCAFDimTolObjects_AngularQualifier_Large: XCAFDimTolObjects_AngularQualifier = ...

XCAFDimTolObjects_AngularQualifier_Equal: XCAFDimTolObjects_AngularQualifier = ...

class XCAFDimTolObjects_GeomToleranceType(enum.IntEnum):
    """Defines types of geom tolerance"""

    XCAFDimTolObjects_GeomToleranceType_None = 0

    XCAFDimTolObjects_GeomToleranceType_Angularity = 1

    XCAFDimTolObjects_GeomToleranceType_CircularRunout = 2

    XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness = 3

    XCAFDimTolObjects_GeomToleranceType_Coaxiality = 4

    XCAFDimTolObjects_GeomToleranceType_Concentricity = 5

    XCAFDimTolObjects_GeomToleranceType_Cylindricity = 6

    XCAFDimTolObjects_GeomToleranceType_Flatness = 7

    XCAFDimTolObjects_GeomToleranceType_Parallelism = 8

    XCAFDimTolObjects_GeomToleranceType_Perpendicularity = 9

    XCAFDimTolObjects_GeomToleranceType_Position = 10

    XCAFDimTolObjects_GeomToleranceType_ProfileOfLine = 11

    XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface = 12

    XCAFDimTolObjects_GeomToleranceType_Straightness = 13

    XCAFDimTolObjects_GeomToleranceType_Symmetry = 14

    XCAFDimTolObjects_GeomToleranceType_TotalRunout = 15

XCAFDimTolObjects_GeomToleranceType_None: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Angularity: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_CircularRunout: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_CircularityOrRoundness: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Coaxiality: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Concentricity: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Cylindricity: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Flatness: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Parallelism: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Perpendicularity: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Position: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_ProfileOfLine: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_ProfileOfSurface: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Straightness: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_Symmetry: XCAFDimTolObjects_GeomToleranceType = ...

XCAFDimTolObjects_GeomToleranceType_TotalRunout: XCAFDimTolObjects_GeomToleranceType = ...

class XCAFDimTolObjects_GeomToleranceTypeValue(enum.IntEnum):
    """Defines types of value of tolerane"""

    XCAFDimTolObjects_GeomToleranceTypeValue_None = 0

    XCAFDimTolObjects_GeomToleranceTypeValue_Diameter = 1

    XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter = 2

XCAFDimTolObjects_GeomToleranceTypeValue_None: XCAFDimTolObjects_GeomToleranceTypeValue = ...

XCAFDimTolObjects_GeomToleranceTypeValue_Diameter: XCAFDimTolObjects_GeomToleranceTypeValue = ...

XCAFDimTolObjects_GeomToleranceTypeValue_SphericalDiameter: XCAFDimTolObjects_GeomToleranceTypeValue = ...

class XCAFDimTolObjects_GeomToleranceMatReqModif(enum.IntEnum):
    """Defines types of material requirement"""

    XCAFDimTolObjects_GeomToleranceMatReqModif_None = 0

    XCAFDimTolObjects_GeomToleranceMatReqModif_M = 1

    XCAFDimTolObjects_GeomToleranceMatReqModif_L = 2

XCAFDimTolObjects_GeomToleranceMatReqModif_None: XCAFDimTolObjects_GeomToleranceMatReqModif = ...

XCAFDimTolObjects_GeomToleranceMatReqModif_M: XCAFDimTolObjects_GeomToleranceMatReqModif = ...

XCAFDimTolObjects_GeomToleranceMatReqModif_L: XCAFDimTolObjects_GeomToleranceMatReqModif = ...

class XCAFDimTolObjects_GeomToleranceZoneModif(enum.IntEnum):
    """Defines types of zone"""

    XCAFDimTolObjects_GeomToleranceZoneModif_None = 0

    XCAFDimTolObjects_GeomToleranceZoneModif_Projected = 1

    XCAFDimTolObjects_GeomToleranceZoneModif_Runout = 2

    XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform = 3

XCAFDimTolObjects_GeomToleranceZoneModif_None: XCAFDimTolObjects_GeomToleranceZoneModif = ...

XCAFDimTolObjects_GeomToleranceZoneModif_Projected: XCAFDimTolObjects_GeomToleranceZoneModif = ...

XCAFDimTolObjects_GeomToleranceZoneModif_Runout: XCAFDimTolObjects_GeomToleranceZoneModif = ...

XCAFDimTolObjects_GeomToleranceZoneModif_NonUniform: XCAFDimTolObjects_GeomToleranceZoneModif = ...

class XCAFDimTolObjects_GeomToleranceModif(enum.IntEnum):
    """Defines modifirs"""

    XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section = 0

    XCAFDimTolObjects_GeomToleranceModif_Common_Zone = 1

    XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element = 2

    XCAFDimTolObjects_GeomToleranceModif_Free_State = 3

    XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement = 4

    XCAFDimTolObjects_GeomToleranceModif_Line_Element = 5

    XCAFDimTolObjects_GeomToleranceModif_Major_Diameter = 6

    XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement = 7

    XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter = 8

    XCAFDimTolObjects_GeomToleranceModif_Not_Convex = 9

    XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter = 10

    XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement = 11

    XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement = 12

    XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance = 13

    XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane = 14

    XCAFDimTolObjects_GeomToleranceModif_All_Around = 15

    XCAFDimTolObjects_GeomToleranceModif_All_Over = 16

XCAFDimTolObjects_GeomToleranceModif_Any_Cross_Section: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Common_Zone: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Each_Radial_Element: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Free_State: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Least_Material_Requirement: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Line_Element: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Major_Diameter: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Maximum_Material_Requirement: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Minor_Diameter: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Not_Convex: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Pitch_Diameter: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Reciprocity_Requirement: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Separate_Requirement: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Statistical_Tolerance: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_Tangent_Plane: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_All_Around: XCAFDimTolObjects_GeomToleranceModif = ...

XCAFDimTolObjects_GeomToleranceModif_All_Over: XCAFDimTolObjects_GeomToleranceModif = ...

class XCAFDimTolObjects_ToleranceZoneAffectedPlane(enum.IntEnum):
    """Defines types of tolerance zone affected plane"""

    XCAFDimTolObjects_ToleranceZoneAffectedPlane_None = 0

    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection = 1

    XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation = 2

XCAFDimTolObjects_ToleranceZoneAffectedPlane_None: XCAFDimTolObjects_ToleranceZoneAffectedPlane = ...

XCAFDimTolObjects_ToleranceZoneAffectedPlane_Intersection: XCAFDimTolObjects_ToleranceZoneAffectedPlane = ...

XCAFDimTolObjects_ToleranceZoneAffectedPlane_Orientation: XCAFDimTolObjects_ToleranceZoneAffectedPlane = ...

class XCAFDimTolObjects_DatumObject(nanoocp.Standard.Standard_Transient):
    """Access object to store datum"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theObj: XCAFDimTolObjects_DatumObject | None) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDimTolObjects_DatumObject) -> None: ...

    def GetSemanticName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns semantic name"""

    def SetSemanticName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets semantic name"""

    def GetName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns datum name."""

    def SetName(self, theTag: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets datum name."""

    def GetModifiers(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif]:
        """Returns a sequence of modifiers of the datum."""

    def SetModifiers(self, theModifiers: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif]) -> None:
        """Sets new sequence of datum modifiers."""

    def GetModifierWithValue(self) -> tuple[XCAFDimTolObjects_DatumModifWithValue, float]:
        """Retrieves datum modifier with value."""

    def SetModifierWithValue(self, theModifier: XCAFDimTolObjects_DatumModifWithValue, theValue: float) -> None:
        """Sets datum modifier with value."""

    def AddModifier(self, theModifier: XCAFDimTolObjects_DatumSingleModif) -> None:
        """Adds a modifier to the datum sequence of modifiers."""

    def GetDatumTarget(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns datum target shape."""

    def SetDatumTarget(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Sets datum target shape."""

    def GetPosition(self) -> int:
        """Returns datum position in the related geometric tolerance object."""

    def SetPosition(self, thePosition: int) -> None:
        """Sets datum position in the related geometric tolerance object."""

    @overload
    def IsDatumTarget(self) -> bool:
        """Returns True if the datum target is specified."""

    @overload
    def IsDatumTarget(self, theIsDT: bool) -> None:
        """Sets or drops the datum target indicator."""

    def GetDatumTargetType(self) -> XCAFDimTolObjects_DatumTargetType:
        """Returns datum target type"""

    def SetDatumTargetType(self, theType: XCAFDimTolObjects_DatumTargetType) -> None:
        """Sets datum target to point, line, rectangle, circle or area type."""

    def GetDatumTargetAxis(self) -> nanoocp.gp.gp_Ax2:
        """
        Returns datum target axis.
        The Z axis of the datum placement denotes the normal of the surface
        pointing away from the material.
        """

    def SetDatumTargetAxis(self, theAxis: nanoocp.gp.gp_Ax2) -> None:
        """Sets datum target axis."""

    def GetDatumTargetLength(self) -> float:
        """
        Returns datum target length for line and rectangle types.
        The length along the X axis of the datum placement.
        """

    def SetDatumTargetLength(self, theLength: float) -> None:
        """Sets datum target length."""

    def GetDatumTargetWidth(self) -> float:
        """
        Returns datum target width for rectangle type.
        The width along the derived Y axis, with the placement itself positioned
        at the centre of the rectangle.
        """

    def SetDatumTargetWidth(self, theWidth: float) -> None:
        """Sets datum target width."""

    def GetDatumTargetNumber(self) -> int:
        """Returns datum target number."""

    def SetDatumTargetNumber(self, theNumber: int) -> None:
        """Sets datum target number."""

    def SetPlane(self, thePlane: nanoocp.gp.gp_Ax2) -> None:
        """Sets annotation plane."""

    def GetPlane(self) -> nanoocp.gp.gp_Ax2:
        """Returns annotation plane."""

    def SetPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Sets a point on the datum target shape."""

    def GetPoint(self) -> nanoocp.gp.gp_Pnt:
        """Gets point on the datum shape."""

    def SetPointTextAttach(self, thePntText: nanoocp.gp.gp_Pnt) -> None:
        """Sets a position of the datum text."""

    def GetPointTextAttach(self) -> nanoocp.gp.gp_Pnt:
        """Gets datum text position."""

    def HasPlane(self) -> bool:
        """Returns True if the datum has annotation plane."""

    def HasPoint(self) -> bool:
        """Returns True if point on the datum target is specified."""

    def HasPointText(self) -> bool:
        """Returns True if the datum text position is specified."""

    def SetPresentation(self, thePresentation: nanoocp.TopoDS.TopoDS_Shape, thePresentationName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set graphical presentation for object."""

    def GetPresentation(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns graphical presentation of the object."""

    def GetPresentationName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns graphical presentation of the object."""

    def HasDatumTargetParams(self) -> bool:
        """
        Returns True if the datum has valid parameters for datum target (width, length, circle radius
        etc)
        """

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDimTolObjects_DimensionObject(nanoocp.Standard.Standard_Transient):
    """Access object to store dimension data"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theObj: XCAFDimTolObjects_DimensionObject | None) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDimTolObjects_DimensionObject) -> None: ...

    def GetSemanticName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns semantic name"""

    def SetSemanticName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets semantic name"""

    def SetQualifier(self, theQualifier: XCAFDimTolObjects_DimensionQualifier) -> None:
        """Sets dimension qualifier as min., max. or average."""

    def GetQualifier(self) -> XCAFDimTolObjects_DimensionQualifier:
        """Returns dimension qualifier."""

    def HasQualifier(self) -> bool:
        """Returns True if the object has dimension qualifier."""

    def SetAngularQualifier(self, theAngularQualifier: XCAFDimTolObjects_AngularQualifier) -> None:
        """Sets angular qualifier as small, large or equal."""

    def GetAngularQualifier(self) -> XCAFDimTolObjects_AngularQualifier:
        """Returns angular qualifier."""

    def HasAngularQualifier(self) -> bool:
        """Returns True if the object has angular qualifier."""

    def SetType(self, theTyupe: XCAFDimTolObjects_DimensionType) -> None:
        """Sets a specific type of dimension."""

    def GetType(self) -> XCAFDimTolObjects_DimensionType:
        """Returns dimension type."""

    def GetValue(self) -> float:
        """
        Returns the main dimension value.
        It will be the middle value in case of range dimension.
        """

    def GetValues(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns raw array of dimension values"""

    def SetValue(self, theValue: float) -> None:
        """
        Sets the main dimension value.
        Overwrites previous values.
        """

    def SetValues(self, theValue: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Replaces current raw array of dimension values with theValues array."""

    def IsDimWithRange(self) -> bool:
        """
        Returns True if the dimension is of range kind.
        Dimension is of range kind if its values array contains two elements
        defining lower and upper bounds.
        """

    def SetUpperBound(self, theUpperBound: float) -> None:
        """
        Sets the upper bound of the range dimension, otherwise
        resets it to an empty range with the specified upper bound.
        """

    def SetLowerBound(self, theLowerBound: float) -> None:
        """
        Sets the lower bound of the range dimension, otherwise
        resets it to an empty range with the specified lower bound.
        """

    def GetUpperBound(self) -> float:
        """Returns the upper bound of the range dimension, otherwise - zero."""

    def GetLowerBound(self) -> float:
        """Returns the lower bound of the range dimension, otherwise - zero."""

    def IsDimWithPlusMinusTolerance(self) -> bool:
        """
        Returns True if the dimension is of +/- tolerance kind.
        Dimension is of +/- tolerance kind if its values array contains three elements
        defining the main value and the lower/upper tolerances.
        """

    def SetUpperTolValue(self, theUperTolValue: float) -> bool:
        """
        Sets the upper value of the toleranced dimension, otherwise
        resets a simple dimension to toleranced one with the specified lower/upper tolerances.
        Returns False in case of range dimension.
        """

    def SetLowerTolValue(self, theLowerTolValue: float) -> bool:
        """
        Sets the lower value of the toleranced dimension, otherwise
        resets a simple dimension to toleranced one with the specified lower/upper tolerances.
        Returns False in case of range dimension.
        """

    def GetUpperTolValue(self) -> float:
        """Returns the lower value of the toleranced dimension, otherwise - zero."""

    def GetLowerTolValue(self) -> float:
        """Returns the upper value of the toleranced dimension, otherwise - zero."""

    def IsDimWithClassOfTolerance(self) -> bool:
        """
        Returns True if the form variance was set to not XCAFDimTolObjects_DimensionFormVariance_None
        value.
        """

    def SetClassOfTolerance(self, theHole: bool, theFormVariance: XCAFDimTolObjects_DimensionFormVariance, theGrade: XCAFDimTolObjects_DimensionGrade) -> None:
        """
        Sets tolerance class of the dimension.
        \\param theHole - True if the tolerance applies to an internal feature
        \\param theFormVariance - represents the fundamental deviation or "position letter"
        of the ISO 286 limits-and-fits tolerance classification.
        \\param theGrade - represents the quality or the accuracy grade of a tolerance.
        """

    def GetClassOfTolerance(self) -> tuple[bool, bool, XCAFDimTolObjects_DimensionFormVariance, XCAFDimTolObjects_DimensionGrade]:
        """
        Retrieves tolerance class parameters of the dimension.
        Returns True if the dimension is toleranced.
        """

    def SetNbOfDecimalPlaces(self, theL: int, theR: int) -> None:
        """
        Sets the number of places to the left and right of the decimal point respectively.
        """

    def GetNbOfDecimalPlaces(self) -> tuple[int, int]:
        """
        Returns the number of places to the left and right of the decimal point respectively.
        """

    def GetModifiers(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif]:
        """Returns a sequence of modifiers of the dimension."""

    def SetModifiers(self, theModifiers: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif]) -> None:
        """Sets new sequence of dimension modifiers."""

    def AddModifier(self, theModifier: XCAFDimTolObjects_DimensionModif) -> None:
        """Adds a modifier to the dimension sequence of modifiers."""

    def GetPath(self) -> nanoocp.TopoDS.TopoDS_Edge:
        """Returns a 'curve' along which the dimension is measured."""

    def SetPath(self, thePath: nanoocp.TopoDS.TopoDS_Edge) -> None:
        """Sets a 'curve' along which the dimension is measured."""

    def GetDirection(self, theDir: nanoocp.gp.gp_Dir) -> bool:
        """Returns the orientation of the dimension in annotation plane."""

    def SetDirection(self, theDir: nanoocp.gp.gp_Dir) -> bool:
        """Sets an orientation of the dimension in annotation plane."""

    def SetPointTextAttach(self, thePntText: nanoocp.gp.gp_Pnt) -> None:
        """Sets position of the dimension text."""

    def GetPointTextAttach(self) -> nanoocp.gp.gp_Pnt:
        """Returns position of the dimension text."""

    def HasTextPoint(self) -> bool:
        """Returns True if the position of dimension text is specified."""

    def SetPlane(self, thePlane: nanoocp.gp.gp_Ax2) -> None:
        """Sets annotation plane."""

    def GetPlane(self) -> nanoocp.gp.gp_Ax2:
        """Returns annotation plane."""

    def HasPlane(self) -> bool:
        """Returns True if the object has annotation plane."""

    def HasPoint(self) -> bool:
        """
        Returns true, if connection point exists (for dimensional_size),
        if connection point for the first shape exists (for dimensional_location).
        """

    def HasPoint2(self) -> bool: ...

    def IsPointConnection(self) -> bool:
        """
        Returns true, if the connection is a point not coordinate system (for dimensional_size),
        if connection point for the first shape exists (for dimensional_location).
        """

    def IsPointConnection2(self) -> bool: ...

    def SetPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """
        Set connection point (for dimensional_size),
        Set connection point for the first shape (for dimensional_location).
        """

    def SetPoint2(self, thePnt: nanoocp.gp.gp_Pnt) -> None: ...

    def SetConnectionAxis(self, theAxis: nanoocp.gp.gp_Ax2) -> None:
        """
        Set connection point as a coordinate system (for dimensional_size),
        Set connection point as a coordinate system for the first shape (for dimensional_location).
        """

    def SetConnectionAxis2(self, theAxis: nanoocp.gp.gp_Ax2) -> None: ...

    def GetPoint(self) -> nanoocp.gp.gp_Pnt:
        """
        Get connection point (for dimensional_size),
        Get connection point for the first shape (for dimensional_location).
        """

    def GetPoint2(self) -> nanoocp.gp.gp_Pnt: ...

    def GetConnectionAxis(self) -> nanoocp.gp.gp_Ax2:
        """
        Get connection point as a coordinate system (for dimensional_size),
        Get connection point as a coordinate system for the first shape (for dimensional_location).
        """

    def GetConnectionAxis2(self) -> nanoocp.gp.gp_Ax2: ...

    def GetConnectionName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns connection name of the object."""

    def GetConnectionName2(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns 2nd connection name of the object."""

    def SetConnectionName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets connection name of the object."""

    def SetConnectionName2(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets 2nd connection name of the object."""

    def SetPresentation(self, thePresentation: nanoocp.TopoDS.TopoDS_Shape, thePresentationName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set graphical presentation for the object."""

    def GetPresentation(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns graphical presentation of the object."""

    def GetPresentationName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns graphical presentation of the object"""

    def HasDescriptions(self) -> bool:
        """Returns true, if the object has descriptions."""

    def NbDescriptions(self) -> int:
        """Returns number of descriptions."""

    def GetDescription(self, theNumber: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns description with the given number."""

    def GetDescriptionName(self, theNumber: int) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns name of description with the given number."""

    def RemoveDescription(self, theNumber: int) -> None:
        """Remove description with the given number."""

    def AddDescription(self, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Add new description."""

    @staticmethod
    def IsDimensionalLocation(theType: XCAFDimTolObjects_DimensionType) -> bool:
        """Returns true if the dimension type is a location."""

    @staticmethod
    def IsDimensionalSize(theType: XCAFDimTolObjects_DimensionType) -> bool:
        """Returns true if the dimension type is a size."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDimTolObjects_GeomToleranceObject(nanoocp.Standard.Standard_Transient):
    """Access object to store dimension and tolerance"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theObj: XCAFDimTolObjects_GeomToleranceObject | None) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDimTolObjects_GeomToleranceObject) -> None: ...

    def GetSemanticName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns semantic name"""

    def SetSemanticName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Sets semantic name"""

    def SetType(self, theType: XCAFDimTolObjects_GeomToleranceType) -> None:
        """Sets type of the object."""

    def GetType(self) -> XCAFDimTolObjects_GeomToleranceType:
        """Returns type of the object."""

    def SetTypeOfValue(self, theTypeOfValue: XCAFDimTolObjects_GeomToleranceTypeValue) -> None:
        """Sets type of tolerance value."""

    def GetTypeOfValue(self) -> XCAFDimTolObjects_GeomToleranceTypeValue:
        """Returns type of tolerance value."""

    def SetValue(self, theValue: float) -> None:
        """Sets tolerance value."""

    def GetValue(self) -> float:
        """Returns tolerance value."""

    def SetMaterialRequirementModifier(self, theMatReqModif: XCAFDimTolObjects_GeomToleranceMatReqModif) -> None:
        """Sets material requirement of the tolerance."""

    def GetMaterialRequirementModifier(self) -> XCAFDimTolObjects_GeomToleranceMatReqModif:
        """Returns material requirement of the tolerance."""

    def SetZoneModifier(self, theZoneModif: XCAFDimTolObjects_GeomToleranceZoneModif) -> None:
        """Sets tolerance zone."""

    def GetZoneModifier(self) -> XCAFDimTolObjects_GeomToleranceZoneModif:
        """Returns tolerance zone."""

    def SetValueOfZoneModifier(self, theValue: float) -> None:
        """Sets value associated with tolerance zone."""

    def GetValueOfZoneModifier(self) -> float:
        """Returns value associated with tolerance zone."""

    def SetModifiers(self, theModifiers: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif]) -> None:
        """Sets new sequence of tolerance modifiers."""

    def AddModifier(self, theModifier: XCAFDimTolObjects_GeomToleranceModif) -> None:
        """Adds a tolerance modifier to the sequence of modifiers."""

    def GetModifiers(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif]:
        """Returns a sequence of modifiers of the tolerance."""

    def SetMaxValueModifier(self, theModifier: float) -> None:
        """Sets the maximal upper tolerance value for tolerance with modifiers."""

    def GetMaxValueModifier(self) -> float:
        """Returns the maximal upper tolerance."""

    def SetAxis(self, theAxis: nanoocp.gp.gp_Ax2) -> None: ...

    def GetAxis(self) -> nanoocp.gp.gp_Ax2: ...

    def HasAxis(self) -> bool: ...

    def SetPlane(self, thePlane: nanoocp.gp.gp_Ax2) -> None:
        """Sets annotation plane."""

    def GetPlane(self) -> nanoocp.gp.gp_Ax2:
        """Returns annotation plane."""

    def SetPoint(self, thePnt: nanoocp.gp.gp_Pnt) -> None:
        """Sets reference point."""

    def GetPoint(self) -> nanoocp.gp.gp_Pnt:
        """Returns reference point."""

    def SetPointTextAttach(self, thePntText: nanoocp.gp.gp_Pnt) -> None:
        """Sets text position."""

    def GetPointTextAttach(self) -> nanoocp.gp.gp_Pnt:
        """Returns the text position."""

    def HasPlane(self) -> bool:
        """Returns True if the object has annotation plane."""

    def HasPoint(self) -> bool:
        """Returns True if reference point is specified."""

    def HasPointText(self) -> bool:
        """Returns True if text position is specified."""

    def SetPresentation(self, thePresentation: nanoocp.TopoDS.TopoDS_Shape, thePresentationName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set graphical presentation for object."""

    def GetPresentation(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns graphical presentation of the object."""

    def GetPresentationName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns graphical presentation of the object."""

    def HasAffectedPlane(self) -> bool: ...

    def GetAffectedPlaneType(self) -> XCAFDimTolObjects_ToleranceZoneAffectedPlane: ...

    def SetAffectedPlaneType(self, theType: XCAFDimTolObjects_ToleranceZoneAffectedPlane) -> None: ...

    @overload
    def SetAffectedPlane(self, thePlane: nanoocp.gp.gp_Pln) -> None: ...

    @overload
    def SetAffectedPlane(self, thePlane: nanoocp.gp.gp_Pln, theType: XCAFDimTolObjects_ToleranceZoneAffectedPlane) -> None:
        """Sets affected plane."""

    def GetAffectedPlane(self) -> nanoocp.gp.gp_Pln:
        """Returns affected plane."""

    def DumpJson(self, theDepth: int = -1) -> str:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XCAFDimTolObjects_Tool:
    @overload
    def __init__(self, theDoc: nanoocp.TDocStd.TDocStd_Document | None) -> None: ...

    @overload
    def __init__(self, theOther: XCAFDimTolObjects_Tool) -> None: ...

    def GetDimensions(self, theDimensionObjectSequence: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject]) -> None:
        """
        Returns a sequence of Dimensions currently stored
        in the GD&T table
        """

    def GetRefDimensions(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theDimensions: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionObject]) -> bool:
        """Returns all Dimensions defined for Shape"""

    def GetGeomTolerances(self, theGeomToleranceObjectSequence: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject], theDatumObjectSequence: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject], theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject]) -> None:
        """
        Returns a sequence of Tolerances currently stored
        in the GD&T table
        """

    def GetRefGeomTolerances(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theGeomToleranceObjectSequence: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject], theDatumObjectSequence: nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject], theMap: nanoocp.NCollection.NCollection_DataMap[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceObject, nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumObject]) -> bool:
        """Returns all GeomTolerances defined for Shape"""

    def GetRefDatum(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> tuple[bool, XCAFDimTolObjects_DatumObject]:
        """Returns DatumObject defined for Shape"""

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.XCAFDimTolObjects
XCAFDimTolObjects_DatumModifiersSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DatumSingleModif]
XCAFDimTolObjects_DimensionModifiersSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_DimensionModif]
XCAFDimTolObjects_GeomToleranceModifiersSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.XCAFDimTolObjects.XCAFDimTolObjects_GeomToleranceModif]
