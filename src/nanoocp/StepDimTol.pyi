"""OCCT package StepDimTol (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.TCollection


class StepDimTol_AreaUnitType(enum.IntEnum):
    StepDimTol_Circular = 0

    StepDimTol_Rectangular = 1

    StepDimTol_Square = 2

StepDimTol_Circular: StepDimTol_AreaUnitType = StepDimTol_AreaUnitType.StepDimTol_Circular

StepDimTol_Rectangular: StepDimTol_AreaUnitType = StepDimTol_AreaUnitType.StepDimTol_Rectangular

StepDimTol_Square: StepDimTol_AreaUnitType = StepDimTol_AreaUnitType.StepDimTol_Square

class StepDimTol_DatumReferenceModifierType(enum.IntEnum):
    StepDimTol_CircularOrCylindrical = 0

    StepDimTol_Distance = 1

    StepDimTol_Projected = 2

    StepDimTol_Spherical = 3

StepDimTol_CircularOrCylindrical: StepDimTol_DatumReferenceModifierType = ...

StepDimTol_Distance: StepDimTol_DatumReferenceModifierType = ...

StepDimTol_Projected: StepDimTol_DatumReferenceModifierType = ...

StepDimTol_Spherical: StepDimTol_DatumReferenceModifierType = ...

class StepDimTol_SimpleDatumReferenceModifier(enum.IntEnum):
    StepDimTol_SDRMAnyCrossSection = 0

    StepDimTol_SDRMAnyLongitudinalSection = 1

    StepDimTol_SDRMBasic = 2

    StepDimTol_SDRMContactingFeature = 3

    StepDimTol_SDRMDegreeOfFreedomConstraintU = 4

    StepDimTol_SDRMDegreeOfFreedomConstraintV = 5

    StepDimTol_SDRMDegreeOfFreedomConstraintW = 6

    StepDimTol_SDRMDegreeOfFreedomConstraintX = 7

    StepDimTol_SDRMDegreeOfFreedomConstraintY = 8

    StepDimTol_SDRMDegreeOfFreedomConstraintZ = 9

    StepDimTol_SDRMDistanceVariable = 10

    StepDimTol_SDRMFreeState = 11

    StepDimTol_SDRMLeastMaterialRequirement = 12

    StepDimTol_SDRMLine = 13

    StepDimTol_SDRMMajorDiameter = 14

    StepDimTol_SDRMMaximumMaterialRequirement = 15

    StepDimTol_SDRMMinorDiameter = 16

    StepDimTol_SDRMOrientation = 17

    StepDimTol_SDRMPitchDiameter = 18

    StepDimTol_SDRMPlane = 19

    StepDimTol_SDRMPoint = 20

    StepDimTol_SDRMTranslation = 21

StepDimTol_SDRMAnyCrossSection: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMAnyLongitudinalSection: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMBasic: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMContactingFeature: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintU: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintV: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintW: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintX: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintY: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDegreeOfFreedomConstraintZ: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMDistanceVariable: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMFreeState: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMLeastMaterialRequirement: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMLine: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMMajorDiameter: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMMaximumMaterialRequirement: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMMinorDiameter: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMOrientation: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMPitchDiameter: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMPlane: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMPoint: StepDimTol_SimpleDatumReferenceModifier = ...

StepDimTol_SDRMTranslation: StepDimTol_SimpleDatumReferenceModifier = ...

class StepDimTol_GeometricToleranceModifier(enum.IntEnum):
    StepDimTol_GTMAnyCrossSection = 0

    StepDimTol_GTMCommonZone = 1

    StepDimTol_GTMEachRadialElement = 2

    StepDimTol_GTMFreeState = 3

    StepDimTol_GTMLeastMaterialRequirement = 4

    StepDimTol_GTMLineElement = 5

    StepDimTol_GTMMajorDiameter = 6

    StepDimTol_GTMMaximumMaterialRequirement = 7

    StepDimTol_GTMMinorDiameter = 8

    StepDimTol_GTMNotConvex = 9

    StepDimTol_GTMPitchDiameter = 10

    StepDimTol_GTMReciprocityRequirement = 11

    StepDimTol_GTMSeparateRequirement = 12

    StepDimTol_GTMStatisticalTolerance = 13

    StepDimTol_GTMTangentPlane = 14

StepDimTol_GTMAnyCrossSection: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMCommonZone: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMEachRadialElement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMFreeState: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMLeastMaterialRequirement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMLineElement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMMajorDiameter: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMMaximumMaterialRequirement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMMinorDiameter: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMNotConvex: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMPitchDiameter: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMReciprocityRequirement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMSeparateRequirement: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMStatisticalTolerance: StepDimTol_GeometricToleranceModifier = ...

StepDimTol_GTMTangentPlane: StepDimTol_GeometricToleranceModifier = ...

class StepDimTol_GeometricToleranceType(enum.IntEnum):
    StepDimTol_GTTAngularityTolerance = 0

    StepDimTol_GTTCircularRunoutTolerance = 1

    StepDimTol_GTTCoaxialityTolerance = 2

    StepDimTol_GTTConcentricityTolerance = 3

    StepDimTol_GTTCylindricityTolerance = 4

    StepDimTol_GTTFlatnessTolerance = 5

    StepDimTol_GTTLineProfileTolerance = 6

    StepDimTol_GTTParallelismTolerance = 7

    StepDimTol_GTTPerpendicularityTolerance = 8

    StepDimTol_GTTPositionTolerance = 9

    StepDimTol_GTTRoundnessTolerance = 10

    StepDimTol_GTTStraightnessTolerance = 11

    StepDimTol_GTTSurfaceProfileTolerance = 12

    StepDimTol_GTTSymmetryTolerance = 13

    StepDimTol_GTTTotalRunoutTolerance = 14

StepDimTol_GTTAngularityTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTCircularRunoutTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTCoaxialityTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTConcentricityTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTCylindricityTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTFlatnessTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTLineProfileTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTParallelismTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTPerpendicularityTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTPositionTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTRoundnessTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTStraightnessTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTSurfaceProfileTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTSymmetryTolerance: StepDimTol_GeometricToleranceType = ...

StepDimTol_GTTTotalRunoutTolerance: StepDimTol_GeometricToleranceType = ...

class StepDimTol_LimitCondition(enum.IntEnum):
    StepDimTol_MaximumMaterialCondition = 0

    StepDimTol_LeastMaterialCondition = 1

    StepDimTol_RegardlessOfFeatureSize = 2

StepDimTol_MaximumMaterialCondition: StepDimTol_LimitCondition = ...

StepDimTol_LeastMaterialCondition: StepDimTol_LimitCondition = ...

StepDimTol_RegardlessOfFeatureSize: StepDimTol_LimitCondition = ...

class StepDimTol_DatumReference(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DatumReference"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumReference) -> None: ...

    def Init(self, thePrecedence: int, theReferencedDatum: StepDimTol_Datum | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Precedence(self) -> int:
        """Returns field Precedence"""

    def SetPrecedence(self, thePrecedence: int) -> None:
        """Set field Precedence"""

    def ReferencedDatum(self) -> StepDimTol_Datum:
        """Returns field ReferencedDatum"""

    def SetReferencedDatum(self, theReferencedDatum: StepDimTol_Datum | None) -> None:
        """Set field ReferencedDatum"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumSystemOrReference(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DatumSystemOrReference select type"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumSystemOrReference) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DatumSystemOrReference Kind Entity that is :
        1 -> DatumSystem
        2 -> DatumReference
        0 else
        """

    def DatumSystem(self) -> StepDimTol_DatumSystem:
        """returns Value as a DatumSystem (Null if another type)"""

    def DatumReference(self) -> StepDimTol_DatumReference:
        """returns Value as a DatumReference (Null if another type)"""

class StepDimTol_GeometricToleranceTarget(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a GeometricToleranceTarget select type"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceTarget) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a GeometricToleranceTarget Kind Entity that is :
        1 -> DimensionalLocation
        2 -> DimensionalSize
        3 -> ProductDefinitionShape
        4 -> ShapeAspect
        0 else
        """

    def DimensionalLocation(self) -> nanoocp.StepShape.StepShape_DimensionalLocation:
        """returns Value as a DimensionalLocation (Null if another type)"""

    def DimensionalSize(self) -> nanoocp.StepShape.StepShape_DimensionalSize:
        """returns Value as a DimensionalSize (Null if another type)"""

    def ProductDefinitionShape(self) -> nanoocp.StepRepr.StepRepr_ProductDefinitionShape:
        """returns Value as a ProductDefinitionShape (Null if another type)"""

    def ShapeAspect(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """returns Value as a ShapeAspect (Null if another type)"""

class StepDimTol_GeometricTolerance(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GeometricTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricTolerance) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Initialize all fields (own and inherited) AP214"""

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget) -> None:
        """Initialize all fields (own and inherited) AP242"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Magnitude(self) -> nanoocp.Standard.Standard_Transient:
        """Returns field Magnitude"""

    def SetMagnitude(self, theMagnitude: nanoocp.Standard.Standard_Transient | None) -> None:
        """Set field Magnitude"""

    def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget:
        """
        Returns field TolerancedShapeAspect
        Note: in AP214(203) type of this attribute can be only StepRepr_ShapeAspect
        """

    @overload
    def SetTolerancedShapeAspect(self, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Set field TolerancedShapeAspect AP214"""

    @overload
    def SetTolerancedShapeAspect(self, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget) -> None:
        """Set field TolerancedShapeAspect AP242"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceWithDatumReference(StepDimTol_GeometricTolerance):
    """Representation of STEP entity GeometricToleranceWithDatumReference"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceWithDatumReference) -> None: ...

    @overload
    def Init(self, theGeometricTolerance_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Magnitude: nanoocp.Standard.Standard_Transient | None, theGeometricTolerance_TolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theDatumSystem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReference] | None) -> None:
        """Initialize all fields (own and inherited) AP214"""

    @overload
    def Init(self, theGeometricTolerance_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Magnitude: nanoocp.Standard.Standard_Transient | None, theGeometricTolerance_TolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theDatumSystem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumSystemOrReference] | None) -> None:
        """Initialize all fields (own and inherited) AP242"""

    def DatumSystem(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReference]:
        """Returns field DatumSystem AP214"""

    def DatumSystemAP242(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumSystemOrReference]:
        """Returns field DatumSystem AP242"""

    @overload
    def SetDatumSystem(self, theDatumSystem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReference] | None) -> None:
        """Set field DatumSystem AP214"""

    @overload
    def SetDatumSystem(self, theDatumSystem: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumSystemOrReference] | None) -> None:
        """Set field DatumSystem AP242"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_AngularityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity AngularityTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_AngularityTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_CircularRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity CircularRunoutTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_CircularRunoutTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_CoaxialityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity CoaxialityTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_CoaxialityTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_CommonDatum(nanoocp.StepRepr.StepRepr_CompositeShapeAspect):
    """Representation of STEP entity CommonDatum"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_CommonDatum) -> None: ...

    def Init(self, theShapeAspect_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_OfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theShapeAspect_ProductDefinitional: nanoocp.StepData.StepData_Logical, theDatum_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theDatum_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theDatum_OfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theDatum_ProductDefinitional: nanoocp.StepData.StepData_Logical, theDatum_Identification: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Datum(self) -> StepDimTol_Datum:
        """Returns data for supertype Datum"""

    def SetDatum(self, theDatum: StepDimTol_Datum | None) -> None:
        """Set data for supertype Datum"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ConcentricityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity ConcentricityTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ConcentricityTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_CylindricityTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity CylindricityTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_CylindricityTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_Datum(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity Datum"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_Datum) -> None: ...

    def Init(self, theShapeAspect_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_OfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theShapeAspect_ProductDefinitional: nanoocp.StepData.StepData_Logical, theIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Identification(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Identification"""

    def SetIdentification(self, theIdentification: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Identification"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumFeature(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity DatumFeature"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumFeature) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumOrCommonDatum(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DatumOrCommonDatum select type"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumOrCommonDatum) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DatumOrCommonDatum Kind Entity that is :
        1 -> Datum
        2 -> CommonDatumList
        0 else
        """

    def Datum(self) -> StepDimTol_Datum:
        """returns Value as a Datum (Null if another type)"""

    def CommonDatumList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceElement]:
        """returns Value as a CommonDatumList (Null if another type)"""

class StepDimTol_DatumReferenceModifierWithValue(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DatumReferenceModifierWithValue"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumReferenceModifierWithValue) -> None: ...

    def Init(self, theModifierType: StepDimTol_DatumReferenceModifierType, theModifierValue: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModifierType(self) -> StepDimTol_DatumReferenceModifierType:
        """Returns field ModifierType"""

    def SetModifierType(self, theModifierType: StepDimTol_DatumReferenceModifierType) -> None:
        """Set field ModifierType"""

    def ModifierValue(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field ModifierValue"""

    def SetModifierValue(self, theModifierValue: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field ModifierValue"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_SimpleDatumReferenceModifierMember(nanoocp.StepData.StepData_SelectInt):
    """
    Defines SimpleDatumReferenceModifier as unique member of DatumReferenceModifier
    Works with an EnumTool
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_SimpleDatumReferenceModifierMember) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, arg0: str) -> bool: ...

    def Kind(self) -> int: ...

    def EnumText(self) -> str: ...

    def SetEnumText(self, theValue: int, theText: str) -> None: ...

    def SetValue(self, theValue: StepDimTol_SimpleDatumReferenceModifier) -> None: ...

    def Value(self) -> StepDimTol_SimpleDatumReferenceModifier: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumReferenceModifier(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DatumReferenceModifier select type"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumReferenceModifier) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DatumReferenceModifier Kind Entity that is :
        1 -> DatumReferenceModifierWithValue
        2 -> SimpleDatumReferenceModifierMember
        0 else
        """

    def DatumReferenceModifierWithValue(self) -> StepDimTol_DatumReferenceModifierWithValue:
        """
        returns Value as a DatumReferenceModifierWithValue (Null if another type)
        """

    def SimpleDatumReferenceModifierMember(self) -> StepDimTol_SimpleDatumReferenceModifierMember:
        """
        returns Value as a SimpleDatumReferenceModifierMember (Null if another type)
        """

class StepDimTol_GeneralDatumReference(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity GeneralDatumReference"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeneralDatumReference) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theOfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theProductDefinitional: nanoocp.StepData.StepData_Logical, theBase: StepDimTol_DatumOrCommonDatum, theHasModifiers: bool, theModifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Base(self) -> StepDimTol_DatumOrCommonDatum:
        """Returns field Base"""

    def SetBase(self, theBase: StepDimTol_DatumOrCommonDatum) -> None:
        """Set field Base"""

    def HasModifiers(self) -> bool:
        """Indicates is field Modifiers exist"""

    def Modifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier]:
        """Returns field Modifiers"""

    def SetModifiers(self, theModifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier] | None) -> None:
        """Set field Modifiers"""

    def NbModifiers(self) -> int:
        """Returns number of Modifiers"""

    @overload
    def ModifiersValue(self, theNum: int) -> StepDimTol_DatumReferenceModifier:
        """Returns Modifiers with the given number"""

    @overload
    def ModifiersValue(self, theNum: int, theItem: StepDimTol_DatumReferenceModifier) -> None:
        """Sets Modifiers with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumReferenceCompartment(StepDimTol_GeneralDatumReference):
    """Representation of STEP entity DatumReferenceCompartment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumReferenceCompartment) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumReferenceElement(StepDimTol_GeneralDatumReference):
    """Representation of STEP entity DatumReferenceElement"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumReferenceElement) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumSystem(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity DatumSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumSystem) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theOfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theProductDefinitional: nanoocp.StepData.StepData_Logical, theConstituents: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceCompartment] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Constituents(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceCompartment]:
        """Returns field Constituents"""

    def SetConstituents(self, theConstituents: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceCompartment] | None) -> None:
        """Set field Constituents"""

    def NbConstituents(self) -> int:
        """Returns number of Constituents"""

    @overload
    def ConstituentsValue(self, num: int) -> StepDimTol_DatumReferenceCompartment:
        """Returns Constituents with the given number"""

    @overload
    def ConstituentsValue(self, num: int, theItem: StepDimTol_DatumReferenceCompartment | None) -> None:
        """Sets Constituents with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_DatumTarget(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity DatumTarget"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_DatumTarget) -> None: ...

    def Init(self, theShapeAspect_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeAspect_OfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theShapeAspect_ProductDefinitional: nanoocp.StepData.StepData_Logical, theTargetId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def TargetId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field TargetId"""

    def SetTargetId(self, theTargetId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field TargetId"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_FlatnessTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity FlatnessTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_FlatnessTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GeometricToleranceRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceRelationship) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theRelatingGeometricTolerance: StepDimTol_GeometricTolerance | None, theRelatedGeometricTolerance: StepDimTol_GeometricTolerance | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def RelatingGeometricTolerance(self) -> StepDimTol_GeometricTolerance:
        """Returns field RelatingGeometricTolerance"""

    def SetRelatingGeometricTolerance(self, theRelatingGeometricTolerance: StepDimTol_GeometricTolerance | None) -> None:
        """Set field RelatingGeometricTolerance"""

    def RelatedGeometricTolerance(self) -> StepDimTol_GeometricTolerance:
        """Returns field RelatedGeometricTolerance"""

    def SetRelatedGeometricTolerance(self, theRelatedGeometricTolerance: StepDimTol_GeometricTolerance | None) -> None:
        """Set field RelatedGeometricTolerance"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceWithDefinedUnit(StepDimTol_GeometricTolerance):
    """Representation of STEP entity GeometricToleranceWithDefinedUnit"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceWithDefinedUnit) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited) AP214"""

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited) AP242"""

    def UnitSize(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field UnitSize"""

    def SetUnitSize(self, theUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field UnitSize"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceWithDefinedAreaUnit(StepDimTol_GeometricToleranceWithDefinedUnit):
    """Representation of STEP entity GeometricToleranceWithDefinedAreaUnit"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceWithDefinedAreaUnit) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None, theAreaType: StepDimTol_AreaUnitType, theHasSecondUnitSize: bool, theSecondUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AreaType(self) -> StepDimTol_AreaUnitType:
        """Returns field AreaType"""

    def SetAreaType(self, theAreaType: StepDimTol_AreaUnitType) -> None:
        """Set field AreaType"""

    def SecondUnitSize(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field SecondUnitSize"""

    def SetSecondUnitSize(self, theSecondUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field SecondUnitSize"""

    def HasSecondUnitSize(self) -> bool:
        """Indicates if SecondUnitSize field exist"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceWithModifiers(StepDimTol_GeometricTolerance):
    """Representation of STEP entity GeometricToleranceWithModifiers"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceWithModifiers) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Modifiers(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier]:
        """Returns field Modifiers"""

    def SetModifiers(self, theModifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier] | None) -> None:
        """Set field Modifiers"""

    def NbModifiers(self) -> int:
        """Returns number of modifiers"""

    def ModifierValue(self, theNum: int) -> StepDimTol_GeometricToleranceModifier:
        """Returns modifier with the given number"""

    def SetModifierValue(self, theNum: int, theItem: StepDimTol_GeometricToleranceModifier) -> None:
        """Sets modifier with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeometricToleranceWithMaximumTolerance(StepDimTol_GeometricToleranceWithModifiers):
    """Representation of STEP entity GeometricToleranceWithMaximumTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_GeometricToleranceWithMaximumTolerance) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifiers: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier] | None, theUnitSize: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited)"""

    def MaximumUpperTolerance(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field MaximumUpperTolerance"""

    def SetMaximumUpperTolerance(self, theMaximumUpperTolerance: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field MaximumUpperTolerance"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthDatRef(StepDimTol_GeometricTolerance):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthDatRef) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def SetGeometricToleranceWithDatumReference(self, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None) -> None: ...

    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...

    def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod(StepDimTol_GeometricTolerance):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, aGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def SetGeometricToleranceWithDatumReference(self, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None) -> None: ...

    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...

    def SetGeometricToleranceWithModifiers(self, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None) -> None: ...

    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: ...

    def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, aGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def SetMaxTolerance(self, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None: ...

    def GetMaxTolerance(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol(StepDimTol_GeometricTolerance):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, aMGT: StepDimTol_ModifiedGeometricTolerance | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, aMGT: StepDimTol_ModifiedGeometricTolerance | None) -> None: ...

    def SetGeometricToleranceWithDatumReference(self, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None) -> None: ...

    def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...

    def SetModifiedGeometricTolerance(self, aMGT: StepDimTol_ModifiedGeometricTolerance | None) -> None: ...

    def GetModifiedGeometricTolerance(self) -> StepDimTol_ModifiedGeometricTolerance: ...

    def SetPositionTolerance(self, aPT: StepDimTol_PositionTolerance | None) -> None: ...

    def GetPositionTolerance(self) -> StepDimTol_PositionTolerance: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol(StepDimTol_GeoTolAndGeoTolWthDatRef):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theType: StepDimTol_GeometricToleranceType, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance | None) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference | None, theType: StepDimTol_GeometricToleranceType, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance | None) -> None: ...

    def SetUnequallyDisposedGeometricTolerance(self, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance | None) -> None: ...

    def GetUnequallyDisposedGeometricTolerance(self) -> StepDimTol_UnequallyDisposedGeometricTolerance: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthMod(StepDimTol_GeometricTolerance):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthMod) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def SetGeometricToleranceWithModifiers(self, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None) -> None: ...

    def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: ...

    def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_GeoTolAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthMod):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_GeoTolAndGeoTolWthMaxTol) -> None: ...

    @overload
    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    @overload
    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aMagnitude: nanoocp.Standard.Standard_Transient | None, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWM: StepDimTol_GeometricToleranceWithModifiers | None, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None, theType: StepDimTol_GeometricToleranceType) -> None: ...

    def SetMaxTolerance(self, theMaxTol: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None: ...

    def GetMaxTolerance(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_LineProfileTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity LineProfileTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_LineProfileTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ModifiedGeometricTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity ModifiedGeometricTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ModifiedGeometricTolerance) -> None: ...

    @overload
    def Init(self, theGeometricTolerance_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Magnitude: nanoocp.Standard.Standard_Transient | None, theGeometricTolerance_TolerancedShapeAspect: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theModifier: StepDimTol_LimitCondition) -> None:
        """Initialize all fields (own and inherited) AP214"""

    @overload
    def Init(self, theGeometricTolerance_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theGeometricTolerance_Magnitude: nanoocp.Standard.Standard_Transient | None, theGeometricTolerance_TolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifier: StepDimTol_LimitCondition) -> None:
        """Initialize all fields (own and inherited) AP242"""

    def Modifier(self) -> StepDimTol_LimitCondition:
        """Returns field Modifier"""

    def SetModifier(self, theModifier: StepDimTol_LimitCondition) -> None:
        """Set field Modifier"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ToleranceZoneTarget(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ToleranceZoneTarget select type"""

    @overload
    def __init__(self, theOther: StepDimTol_ToleranceZoneTarget) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ToleranceZoneTarget Kind Entity that is :
        1 -> DimensionalLocation
        2 -> DimensionalSize
        3 -> GeometricTolerance
        4 -> GeneralDatumReference
        0 else
        """

    def DimensionalLocation(self) -> nanoocp.StepShape.StepShape_DimensionalLocation:
        """returns Value as a DimensionalLocation (Null if another type)"""

    def DimensionalSize(self) -> nanoocp.StepShape.StepShape_DimensionalSize:
        """returns Value as a DimensionalSize (Null if another type)"""

    def GeometricTolerance(self) -> StepDimTol_GeometricTolerance:
        """returns Value as a GeometricTolerance (Null if another type)"""

    def GeneralDatumReference(self) -> StepDimTol_GeneralDatumReference:
        """returns Value as a GeneralDatumReference (Null if another type)"""

class StepDimTol_ToleranceZoneForm(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_ToleranceZoneForm) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Init all field own and inherited"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ToleranceZone(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity ToleranceZone"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ToleranceZone) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theOfShape: nanoocp.StepRepr.StepRepr_ProductDefinitionShape | None, theProductDefinitional: nanoocp.StepData.StepData_Logical, theDefiningTolerance: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_ToleranceZoneTarget] | None, theForm: StepDimTol_ToleranceZoneForm | None) -> None:
        """Initialize all fields (own and inherited)"""

    def DefiningTolerance(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_ToleranceZoneTarget]:
        """Returns field DefiningTolerance"""

    def SetDefiningTolerance(self, theDefiningTolerance: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_ToleranceZoneTarget] | None) -> None:
        """Set field DefiningTolerance"""

    def NbDefiningTolerances(self) -> int:
        """Returns number of Defining Tolerances"""

    def DefiningToleranceValue(self, theNum: int) -> StepDimTol_ToleranceZoneTarget:
        """Returns Defining Tolerance with the given number"""

    def SetDefiningToleranceValue(self, theNum: int, theItem: StepDimTol_ToleranceZoneTarget) -> None:
        """Sets Defining Tolerance with given number"""

    def Form(self) -> StepDimTol_ToleranceZoneForm:
        """Returns field Form"""

    def SetForm(self, theForm: StepDimTol_ToleranceZoneForm | None) -> None:
        """Set field Form"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ToleranceZoneDefinition(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ToleranceZoneDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ToleranceZoneDefinition) -> None: ...

    def Init(self, theZone: StepDimTol_ToleranceZone | None, theBoundaries: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Boundaries(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect]:
        """Returns field Boundaries"""

    def SetBoundaries(self, theBoundaries: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect] | None) -> None:
        """Set field Boundaries"""

    def NbBoundaries(self) -> int:
        """Returns number of Boundaries"""

    def BoundariesValue(self, theNum: int) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns Boundaries with the given number"""

    def SetBoundariesValue(self, theNum: int, theItem: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Sets Boundaries with given number"""

    def Zone(self) -> StepDimTol_ToleranceZone:
        """Returns field Zone"""

    def SetZone(self, theZone: StepDimTol_ToleranceZone | None) -> None:
        """Set field Zone"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_NonUniformZoneDefinition(StepDimTol_ToleranceZoneDefinition):
    """Representation of STEP entity NonUniformZoneDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_NonUniformZoneDefinition) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ParallelismTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity ParallelismTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ParallelismTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_PerpendicularityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity PerpendicularityTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_PerpendicularityTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_PlacedDatumTargetFeature(StepDimTol_DatumTarget):
    """Representation of STEP entity PlacedDatumTargetFeature"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_PlacedDatumTargetFeature) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_PositionTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity PositionTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_PositionTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ProjectedZoneDefinition(StepDimTol_ToleranceZoneDefinition):
    """Representation of STEP entity ProjectedZoneDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ProjectedZoneDefinition) -> None: ...

    def Init(self, theZone: StepDimTol_ToleranceZone | None, theBoundaries: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect] | None, theProjectionEnd: nanoocp.StepRepr.StepRepr_ShapeAspect | None, theProjectionLength: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ProjectionEnd(self) -> nanoocp.StepRepr.StepRepr_ShapeAspect:
        """Returns field ProjectionEnd"""

    def SetProjectionEnd(self, theProjectionEnd: nanoocp.StepRepr.StepRepr_ShapeAspect | None) -> None:
        """Set field ProjectionEnd"""

    def ProjectionLength(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field ProjectionLength"""

    def SetProjectionLength(self, theProjectionLength: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field ProjectionLength"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_RoundnessTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity RoundnessTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_RoundnessTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_RunoutZoneOrientation(nanoocp.Standard.Standard_Transient):
    """Added for Dimensional Tolerances"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepDimTol_RunoutZoneOrientation) -> None: ...

    def Init(self, theAngle: nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit | None) -> None:
        """Init all field own and inherited"""

    def Angle(self) -> nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit:
        """Returns field Angle"""

    def SetAngle(self, theAngle: nanoocp.StepBasic.StepBasic_PlaneAngleMeasureWithUnit | None) -> None:
        """Set field Angle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_RunoutZoneDefinition(StepDimTol_ToleranceZoneDefinition):
    """Representation of STEP entity ToleranceZoneDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_RunoutZoneDefinition) -> None: ...

    def Init(self, theZone: StepDimTol_ToleranceZone | None, theBoundaries: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_ShapeAspect] | None, theOrientation: StepDimTol_RunoutZoneOrientation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Orientation(self) -> StepDimTol_RunoutZoneOrientation:
        """Returns field Orientation"""

    def SetOrientation(self, theOrientation: StepDimTol_RunoutZoneOrientation | None) -> None:
        """Set field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_ShapeToleranceSelect(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ShapeToleranceSelect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_ShapeToleranceSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ShapeToleranceSelect select type
        1 -> GeometricTolerance from StepDimTol
        2 -> PlusMinusTolerance from StepShape
        0 else
        """

    def GeometricTolerance(self) -> StepDimTol_GeometricTolerance:
        """Returns Value as GeometricTolerance (or Null if another type)"""

    def PlusMinusTolerance(self) -> nanoocp.StepShape.StepShape_PlusMinusTolerance:
        """Returns Value as PlusMinusTolerance (or Null if another type)"""

class StepDimTol_StraightnessTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity StraightnessTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_StraightnessTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_SurfaceProfileTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity SurfaceProfileTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_SurfaceProfileTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_SymmetryTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity SymmetryTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_SymmetryTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_TotalRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference):
    """Representation of STEP entity TotalRunoutTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_TotalRunoutTolerance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepDimTol_UnequallyDisposedGeometricTolerance(StepDimTol_GeometricTolerance):
    """Representation of STEP entity UnequallyDisposedGeometricTolerance"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepDimTol_UnequallyDisposedGeometricTolerance) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theMagnitude: nanoocp.Standard.Standard_Transient | None, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theDisplacement: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Displacement(self) -> nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit:
        """Returns field Displacement"""

    def SetDisplacement(self, theDisplacement: nanoocp.StepBasic.StepBasic_LengthMeasureWithUnit | None) -> None:
        """Set field Displacement"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepDimTol
StepDimTol_Array1OfDatumReference = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_DatumReference]
StepDimTol_Array1OfDatumReferenceCompartment = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_DatumReferenceCompartment]
StepDimTol_Array1OfDatumReferenceElement = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_DatumReferenceElement]
StepDimTol_Array1OfDatumReferenceModifier = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier]
StepDimTol_Array1OfDatumSystemOrReference = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_DatumSystemOrReference]
StepDimTol_Array1OfGeometricToleranceModifier = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier]
StepDimTol_Array1OfToleranceZoneTarget = nanoocp.NCollection.NCollection_Array1[nanoocp.StepDimTol.StepDimTol_ToleranceZoneTarget]
StepDimTol_HArray1OfDatumReference = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReference]
StepDimTol_HArray1OfDatumReferenceCompartment = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceCompartment]
StepDimTol_HArray1OfDatumReferenceElement = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceElement]
StepDimTol_HArray1OfDatumReferenceModifier = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumReferenceModifier]
StepDimTol_HArray1OfDatumSystemOrReference = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_DatumSystemOrReference]
StepDimTol_HArray1OfGeometricToleranceModifier = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_GeometricToleranceModifier]
StepDimTol_HArray1OfToleranceZoneTarget = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepDimTol.StepDimTol_ToleranceZoneTarget]
