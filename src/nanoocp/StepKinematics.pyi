"""OCCT package StepKinematics (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.TCollection


class StepKinematics_ActuatedDirection(enum.IntEnum):
    StepKinematics_adBidirectional = 0

    StepKinematics_adPositiveOnly = 1

    StepKinematics_adNegativeOnly = 2

    StepKinematics_adNotActuated = 3

StepKinematics_adBidirectional: StepKinematics_ActuatedDirection = ...

StepKinematics_adPositiveOnly: StepKinematics_ActuatedDirection = ...

StepKinematics_adNegativeOnly: StepKinematics_ActuatedDirection = ...

StepKinematics_adNotActuated: StepKinematics_ActuatedDirection = ...

class StepKinematics_KinematicJoint(nanoocp.StepShape.StepShape_Edge):
    """Representation of STEP entity KinematicJoint"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicJoint) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicPair(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity KinematicPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theJoint: StepKinematics_KinematicJoint | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ItemDefinedTransformation(self) -> nanoocp.StepRepr.StepRepr_ItemDefinedTransformation:
        """Returns data for supertype ItemDefinedTransformation"""

    def SetItemDefinedTransformation(self, theItemDefinedTransformation: nanoocp.StepRepr.StepRepr_ItemDefinedTransformation | None) -> None:
        """Sets data for supertype ItemDefinedTransformation"""

    def Joint(self) -> StepKinematics_KinematicJoint:
        """Returns field Joint"""

    def SetJoint(self, theJoint: StepKinematics_KinematicJoint | None) -> None:
        """Sets field Joint"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ActuatedKinematicPair(StepKinematics_KinematicPair):
    """Representation of STEP entity ActuatedKinematicPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ActuatedKinematicPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, hasTX: bool, theTX: StepKinematics_ActuatedDirection, hasTY: bool, theTY: StepKinematics_ActuatedDirection, hasTZ: bool, theTZ: StepKinematics_ActuatedDirection, hasRX: bool, theRX: StepKinematics_ActuatedDirection, hasRY: bool, theRY: StepKinematics_ActuatedDirection, hasRZ: bool, theRZ: StepKinematics_ActuatedDirection) -> None:
        """Initialize all fields (own and inherited)"""

    def TX(self) -> StepKinematics_ActuatedDirection:
        """Returns field TX"""

    def SetTX(self, theTX: StepKinematics_ActuatedDirection) -> None:
        """Sets field TX"""

    def HasTX(self) -> bool:
        """Returns True if optional field TX is defined"""

    def TY(self) -> StepKinematics_ActuatedDirection:
        """Returns field TY"""

    def SetTY(self, theTY: StepKinematics_ActuatedDirection) -> None:
        """Sets field TY"""

    def HasTY(self) -> bool:
        """Returns True if optional field TY is defined"""

    def TZ(self) -> StepKinematics_ActuatedDirection:
        """Returns field TZ"""

    def SetTZ(self, theTZ: StepKinematics_ActuatedDirection) -> None:
        """Sets field TZ"""

    def HasTZ(self) -> bool:
        """Returns True if optional field TZ is defined"""

    def RX(self) -> StepKinematics_ActuatedDirection:
        """Returns field RX"""

    def SetRX(self, theRX: StepKinematics_ActuatedDirection) -> None:
        """Sets field RX"""

    def HasRX(self) -> bool:
        """Returns True if optional field RX is defined"""

    def RY(self) -> StepKinematics_ActuatedDirection:
        """Returns field RY"""

    def SetRY(self, theRY: StepKinematics_ActuatedDirection) -> None:
        """Sets field RY"""

    def HasRY(self) -> bool:
        """Returns True if optional field RY is defined"""

    def RZ(self) -> StepKinematics_ActuatedDirection:
        """Returns field RZ"""

    def SetRZ(self, theRZ: StepKinematics_ActuatedDirection) -> None:
        """Sets field RZ"""

    def HasRZ(self) -> bool:
        """Returns True if optional field RZ is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicLinkRepresentationAssociation(nanoocp.StepRepr.StepRepr_RepresentationRelationship):
    """Representation of STEP entity KinematicLinkRepresentationAssociation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicLinkRepresentationAssociation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ProductDefinitionRelationshipKinematics(nanoocp.StepRepr.StepRepr_PropertyDefinition):
    """Representation of STEP entity ProductDefinitionRelationshipKinematics"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ProductDefinitionRelationshipKinematics) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ContextDependentKinematicLinkRepresentation(nanoocp.Standard.Standard_Transient):
    """
    Representation of STEP entity ContextDependentKinematicLinkRepresentation
    """

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ContextDependentKinematicLinkRepresentation) -> None: ...

    def Init(self, theRepresentationRelation: StepKinematics_KinematicLinkRepresentationAssociation | None, theRepresentedProductRelation: StepKinematics_ProductDefinitionRelationshipKinematics | None) -> None:
        """Initialize all fields (own and inherited)"""

    def RepresentationRelation(self) -> StepKinematics_KinematicLinkRepresentationAssociation:
        """Returns field RepresentationRelation"""

    def SetRepresentationRelation(self, theRepresentationRelation: StepKinematics_KinematicLinkRepresentationAssociation | None) -> None:
        """Sets field RepresentationRelation"""

    def RepresentedProductRelation(self) -> StepKinematics_ProductDefinitionRelationshipKinematics:
        """Returns field RepresentedProductRelation"""

    def SetRepresentedProductRelation(self, theRepresentedProductRelation: StepKinematics_ProductDefinitionRelationshipKinematics | None) -> None:
        """Sets field RepresentedProductRelation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LowOrderKinematicPair(StepKinematics_KinematicPair):
    """Representation of STEP entity LowOrderKinematicPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LowOrderKinematicPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theTX: bool, theTY: bool, theTZ: bool, theRX: bool, theRY: bool, theRZ: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def TX(self) -> bool:
        """Returns field TX"""

    def SetTX(self, theTX: bool) -> None:
        """Sets field TX"""

    def TY(self) -> bool:
        """Returns field TY"""

    def SetTY(self, theTY: bool) -> None:
        """Sets field TY"""

    def TZ(self) -> bool:
        """Returns field TZ"""

    def SetTZ(self, theTZ: bool) -> None:
        """Sets field TZ"""

    def RX(self) -> bool:
        """Returns field RX"""

    def SetRX(self, theRX: bool) -> None:
        """Sets field RX"""

    def RY(self) -> bool:
        """Returns field RY"""

    def SetRY(self, theRY: bool) -> None:
        """Sets field RY"""

    def RZ(self) -> bool:
        """Returns field RZ"""

    def SetRZ(self, theRZ: bool) -> None:
        """Sets field RZ"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_CylindricalPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity CylindricalPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_CylindricalPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PairValue(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity PairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theAppliesToPair: StepKinematics_KinematicPair | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AppliesToPair(self) -> StepKinematics_KinematicPair:
        """Returns field AppliesToPair"""

    def SetAppliesToPair(self, theAppliesToPair: StepKinematics_KinematicPair | None) -> None:
        """Sets field AppliesToPair"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_CylindricalPairValue(StepKinematics_PairValue):
    """Representation of STEP entity CylindricalPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_CylindricalPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualTranslation: float, theActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualTranslation(self) -> float:
        """Returns field ActualTranslation"""

    def SetActualTranslation(self, theActualTranslation: float) -> None:
        """Sets field ActualTranslation"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_CylindricalPairWithRange(StepKinematics_CylindricalPair):
    """Representation of STEP entity CylindricalPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_CylindricalPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitActualTranslation: bool, theLowerLimitActualTranslation: float, hasUpperLimitActualTranslation: bool, theUpperLimitActualTranslation: float, hasLowerLimitActualRotation: bool, theLowerLimitActualRotation: float, hasUpperLimitActualRotation: bool, theUpperLimitActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualTranslation(self) -> float:
        """Returns field LowerLimitActualTranslation"""

    def SetLowerLimitActualTranslation(self, theLowerLimitActualTranslation: float) -> None:
        """Sets field LowerLimitActualTranslation"""

    def HasLowerLimitActualTranslation(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslation is defined"""

    def UpperLimitActualTranslation(self) -> float:
        """Returns field UpperLimitActualTranslation"""

    def SetUpperLimitActualTranslation(self, theUpperLimitActualTranslation: float) -> None:
        """Sets field UpperLimitActualTranslation"""

    def HasUpperLimitActualTranslation(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslation is defined"""

    def LowerLimitActualRotation(self) -> float:
        """Returns field LowerLimitActualRotation"""

    def SetLowerLimitActualRotation(self, theLowerLimitActualRotation: float) -> None:
        """Sets field LowerLimitActualRotation"""

    def HasLowerLimitActualRotation(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation is defined"""

    def UpperLimitActualRotation(self) -> float:
        """Returns field UpperLimitActualRotation"""

    def SetUpperLimitActualRotation(self, theUpperLimitActualRotation: float) -> None:
        """Sets field UpperLimitActualRotation"""

    def HasUpperLimitActualRotation(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_FullyConstrainedPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity FullyConstrainedPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_FullyConstrainedPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LowOrderKinematicPairWithMotionCoupling(StepKinematics_KinematicPair):
    """Representation of STEP entity LowOrderKinematicPairWithMotionCoupling"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LowOrderKinematicPairWithMotionCoupling) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_GearPair(StepKinematics_LowOrderKinematicPairWithMotionCoupling):
    """Representation of STEP entity GearPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_GearPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theRadiusFirstLink: float, theRadiusSecondLink: float, theBevel: float, theHelicalAngle: float, theGearRatio: float) -> None:
        """Initialize all fields (own and inherited)"""

    def RadiusFirstLink(self) -> float:
        """Returns field RadiusFirstLink"""

    def SetRadiusFirstLink(self, theRadiusFirstLink: float) -> None:
        """Sets field RadiusFirstLink"""

    def RadiusSecondLink(self) -> float:
        """Returns field RadiusSecondLink"""

    def SetRadiusSecondLink(self, theRadiusSecondLink: float) -> None:
        """Sets field RadiusSecondLink"""

    def Bevel(self) -> float:
        """Returns field Bevel"""

    def SetBevel(self, theBevel: float) -> None:
        """Sets field Bevel"""

    def HelicalAngle(self) -> float:
        """Returns field HelicalAngle"""

    def SetHelicalAngle(self, theHelicalAngle: float) -> None:
        """Sets field HelicalAngle"""

    def GearRatio(self) -> float:
        """Returns field GearRatio"""

    def SetGearRatio(self, theGearRatio: float) -> None:
        """Sets field GearRatio"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_GearPairValue(StepKinematics_PairValue):
    """Representation of STEP entity GearPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_GearPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualRotation1: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualRotation1(self) -> float:
        """Returns field ActualRotation1"""

    def SetActualRotation1(self, theActualRotation1: float) -> None:
        """Sets field ActualRotation1"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_GearPairWithRange(StepKinematics_GearPair):
    """Representation of STEP entity GearPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_GearPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theGearPair_RadiusFirstLink: float, theGearPair_RadiusSecondLink: float, theGearPair_Bevel: float, theGearPair_HelicalAngle: float, theGearPair_GearRatio: float, hasLowerLimitActualRotation1: bool, theLowerLimitActualRotation1: float, hasUpperLimitActualRotation1: bool, theUpperLimitActualRotation1: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualRotation1(self) -> float:
        """Returns field LowerLimitActualRotation1"""

    def SetLowerLimitActualRotation1(self, theLowerLimitActualRotation1: float) -> None:
        """Sets field LowerLimitActualRotation1"""

    def HasLowerLimitActualRotation1(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation1 is defined"""

    def UpperLimitActualRotation1(self) -> float:
        """Returns field UpperLimitActualRotation1"""

    def SetUpperLimitActualRotation1(self, theUpperLimitActualRotation1: float) -> None:
        """Sets field UpperLimitActualRotation1"""

    def HasUpperLimitActualRotation1(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation1 is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_HighOrderKinematicPair(StepKinematics_KinematicPair):
    """Representation of STEP entity HighOrderKinematicPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_HighOrderKinematicPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_UniversalPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity UniversalPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_UniversalPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasInputSkewAngle: bool, theInputSkewAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def InputSkewAngle(self) -> float:
        """Returns field InputSkewAngle"""

    def SetInputSkewAngle(self, theInputSkewAngle: float) -> None:
        """Sets field InputSkewAngle"""

    def HasInputSkewAngle(self) -> bool:
        """Returns True if optional field InputSkewAngle is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_HomokineticPair(StepKinematics_UniversalPair):
    """Representation of STEP entity HomokineticPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_HomokineticPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicLink(nanoocp.StepShape.StepShape_Vertex):
    """Representation of STEP entity KinematicLink"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicLink) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicLinkRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity KinematicLinkRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicLinkRepresentation) -> None: ...

    def Init(self, theRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theRepresentedLink: StepKinematics_KinematicLink | None) -> None:
        """Initialize all fields (own and inherited)"""

    def RepresentedLink(self) -> StepKinematics_KinematicLink:
        """Returns field RepresentedLink"""

    def SetRepresentedLink(self, theRepresentedLink: StepKinematics_KinematicLink | None) -> None:
        """Sets field RepresentedLink"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ActuatedKinPairAndOrderKinPair(StepKinematics_KinematicPair):
    """Representation of STEP entity ActuatedKinPairAndOrderKinPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ActuatedKinPairAndOrderKinPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theJoint: StepKinematics_KinematicJoint | None, theActuatedKinematicPair: StepKinematics_ActuatedKinematicPair | None, theOrderKinematicPair: StepKinematics_KinematicPair | None) -> None: ...

    def SetActuatedKinematicPair(self, aKP: StepKinematics_ActuatedKinematicPair | None) -> None: ...

    def GetActuatedKinematicPair(self) -> StepKinematics_ActuatedKinematicPair: ...

    def SetOrderKinematicPair(self, aKP: StepKinematics_KinematicPair | None) -> None: ...

    def GetOrderKinematicPair(self) -> StepKinematics_KinematicPair: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicPropertyDefinitionRepresentation(nanoocp.StepRepr.StepRepr_PropertyDefinitionRepresentation):
    """
    Representation of STEP entity KinematicPropertyDefinitionRepresentation
    """

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicPropertyDefinitionRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicPropertyMechanismRepresentation(StepKinematics_KinematicPropertyDefinitionRepresentation):
    """Representation of STEP entity KinematicPropertyMechanismRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicPropertyMechanismRepresentation) -> None: ...

    def Init(self, thePropertyDefinitionRepresentation_Definition: nanoocp.StepRepr.StepRepr_RepresentedDefinition, thePropertyDefinitionRepresentation_UsedRepresentation: nanoocp.StepRepr.StepRepr_Representation | None, theBase: StepKinematics_KinematicLinkRepresentation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Base(self) -> StepKinematics_KinematicLinkRepresentation:
        """Returns field Base"""

    def SetBase(self, theBase: StepKinematics_KinematicLinkRepresentation | None) -> None:
        """Sets field Base"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicTopologyStructure(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity KinematicTopologyStructure"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicTopologyStructure) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LinearFlexibleAndPinionPair(StepKinematics_LowOrderKinematicPairWithMotionCoupling):
    """Representation of STEP entity LinearFlexibleAndPinionPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LinearFlexibleAndPinionPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePinionRadius: float) -> None:
        """Initialize all fields (own and inherited)"""

    def PinionRadius(self) -> float:
        """Returns field PinionRadius"""

    def SetPinionRadius(self, thePinionRadius: float) -> None:
        """Sets field PinionRadius"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LinearFlexibleAndPlanarCurvePair(StepKinematics_HighOrderKinematicPair):
    """Representation of STEP entity LinearFlexibleAndPlanarCurvePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LinearFlexibleAndPlanarCurvePair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePairCurve: nanoocp.StepGeom.StepGeom_Curve | None, theOrientation: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def PairCurve(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """Returns field PairCurve"""

    def SetPairCurve(self, thePairCurve: nanoocp.StepGeom.StepGeom_Curve | None) -> None:
        """Sets field PairCurve"""

    def Orientation(self) -> bool:
        """Returns field Orientation"""

    def SetOrientation(self, theOrientation: bool) -> None:
        """Sets field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LinearFlexibleLinkRepresentation(StepKinematics_KinematicLinkRepresentation):
    """Representation of STEP entity LinearFlexibleLinkRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LinearFlexibleLinkRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LowOrderKinematicPairValue(StepKinematics_PairValue):
    """Representation of STEP entity LowOrderKinematicPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LowOrderKinematicPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualTranslationX: float, theActualTranslationY: float, theActualTranslationZ: float, theActualRotationX: float, theActualRotationY: float, theActualRotationZ: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualTranslationX(self) -> float:
        """Returns field ActualTranslationX"""

    def SetActualTranslationX(self, theActualTranslationX: float) -> None:
        """Sets field ActualTranslationX"""

    def ActualTranslationY(self) -> float:
        """Returns field ActualTranslationY"""

    def SetActualTranslationY(self, theActualTranslationY: float) -> None:
        """Sets field ActualTranslationY"""

    def ActualTranslationZ(self) -> float:
        """Returns field ActualTranslationZ"""

    def SetActualTranslationZ(self, theActualTranslationZ: float) -> None:
        """Sets field ActualTranslationZ"""

    def ActualRotationX(self) -> float:
        """Returns field ActualRotationX"""

    def SetActualRotationX(self, theActualRotationX: float) -> None:
        """Sets field ActualRotationX"""

    def ActualRotationY(self) -> float:
        """Returns field ActualRotationY"""

    def SetActualRotationY(self, theActualRotationY: float) -> None:
        """Sets field ActualRotationY"""

    def ActualRotationZ(self) -> float:
        """Returns field ActualRotationZ"""

    def SetActualRotationZ(self, theActualRotationZ: float) -> None:
        """Sets field ActualRotationZ"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_LowOrderKinematicPairWithRange(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity LowOrderKinematicPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_LowOrderKinematicPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitActualRotationX: bool, theLowerLimitActualRotationX: float, hasUpperLimitActualRotationX: bool, theUpperLimitActualRotationX: float, hasLowerLimitActualRotationY: bool, theLowerLimitActualRotationY: float, hasUpperLimitActualRotationY: bool, theUpperLimitActualRotationY: float, hasLowerLimitActualRotationZ: bool, theLowerLimitActualRotationZ: float, hasUpperLimitActualRotationZ: bool, theUpperLimitActualRotationZ: float, hasLowerLimitActualTranslationX: bool, theLowerLimitActualTranslationX: float, hasUpperLimitActualTranslationX: bool, theUpperLimitActualTranslationX: float, hasLowerLimitActualTranslationY: bool, theLowerLimitActualTranslationY: float, hasUpperLimitActualTranslationY: bool, theUpperLimitActualTranslationY: float, hasLowerLimitActualTranslationZ: bool, theLowerLimitActualTranslationZ: float, hasUpperLimitActualTranslationZ: bool, theUpperLimitActualTranslationZ: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualRotationX(self) -> float:
        """Returns field LowerLimitActualRotationX"""

    def SetLowerLimitActualRotationX(self, theLowerLimitActualRotationX: float) -> None:
        """Sets field LowerLimitActualRotationX"""

    def HasLowerLimitActualRotationX(self) -> bool:
        """Returns True if optional field LowerLimitActualRotationX is defined"""

    def UpperLimitActualRotationX(self) -> float:
        """Returns field UpperLimitActualRotationX"""

    def SetUpperLimitActualRotationX(self, theUpperLimitActualRotationX: float) -> None:
        """Sets field UpperLimitActualRotationX"""

    def HasUpperLimitActualRotationX(self) -> bool:
        """Returns True if optional field UpperLimitActualRotationX is defined"""

    def LowerLimitActualRotationY(self) -> float:
        """Returns field LowerLimitActualRotationY"""

    def SetLowerLimitActualRotationY(self, theLowerLimitActualRotationY: float) -> None:
        """Sets field LowerLimitActualRotationY"""

    def HasLowerLimitActualRotationY(self) -> bool:
        """Returns True if optional field LowerLimitActualRotationY is defined"""

    def UpperLimitActualRotationY(self) -> float:
        """Returns field UpperLimitActualRotationY"""

    def SetUpperLimitActualRotationY(self, theUpperLimitActualRotationY: float) -> None:
        """Sets field UpperLimitActualRotationY"""

    def HasUpperLimitActualRotationY(self) -> bool:
        """Returns True if optional field UpperLimitActualRotationY is defined"""

    def LowerLimitActualRotationZ(self) -> float:
        """Returns field LowerLimitActualRotationZ"""

    def SetLowerLimitActualRotationZ(self, theLowerLimitActualRotationZ: float) -> None:
        """Sets field LowerLimitActualRotationZ"""

    def HasLowerLimitActualRotationZ(self) -> bool:
        """Returns True if optional field LowerLimitActualRotationZ is defined"""

    def UpperLimitActualRotationZ(self) -> float:
        """Returns field UpperLimitActualRotationZ"""

    def SetUpperLimitActualRotationZ(self, theUpperLimitActualRotationZ: float) -> None:
        """Sets field UpperLimitActualRotationZ"""

    def HasUpperLimitActualRotationZ(self) -> bool:
        """Returns True if optional field UpperLimitActualRotationZ is defined"""

    def LowerLimitActualTranslationX(self) -> float:
        """Returns field LowerLimitActualTranslationX"""

    def SetLowerLimitActualTranslationX(self, theLowerLimitActualTranslationX: float) -> None:
        """Sets field LowerLimitActualTranslationX"""

    def HasLowerLimitActualTranslationX(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslationX is defined"""

    def UpperLimitActualTranslationX(self) -> float:
        """Returns field UpperLimitActualTranslationX"""

    def SetUpperLimitActualTranslationX(self, theUpperLimitActualTranslationX: float) -> None:
        """Sets field UpperLimitActualTranslationX"""

    def HasUpperLimitActualTranslationX(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslationX is defined"""

    def LowerLimitActualTranslationY(self) -> float:
        """Returns field LowerLimitActualTranslationY"""

    def SetLowerLimitActualTranslationY(self, theLowerLimitActualTranslationY: float) -> None:
        """Sets field LowerLimitActualTranslationY"""

    def HasLowerLimitActualTranslationY(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslationY is defined"""

    def UpperLimitActualTranslationY(self) -> float:
        """Returns field UpperLimitActualTranslationY"""

    def SetUpperLimitActualTranslationY(self, theUpperLimitActualTranslationY: float) -> None:
        """Sets field UpperLimitActualTranslationY"""

    def HasUpperLimitActualTranslationY(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslationY is defined"""

    def LowerLimitActualTranslationZ(self) -> float:
        """Returns field LowerLimitActualTranslationZ"""

    def SetLowerLimitActualTranslationZ(self, theLowerLimitActualTranslationZ: float) -> None:
        """Sets field LowerLimitActualTranslationZ"""

    def HasLowerLimitActualTranslationZ(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslationZ is defined"""

    def UpperLimitActualTranslationZ(self) -> float:
        """Returns field UpperLimitActualTranslationZ"""

    def SetUpperLimitActualTranslationZ(self, theUpperLimitActualTranslationZ: float) -> None:
        """Sets field UpperLimitActualTranslationZ"""

    def HasUpperLimitActualTranslationZ(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslationZ is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicTopologyRepresentationSelect(nanoocp.StepData.StepData_SelectType):
    """
    Representation of STEP SELECT type KinematicTopologyRepresentationSelect
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicTopologyRepresentationSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of KinematicTopologyRepresentationSelect select type
        -- 1 -> KinematicTopologyDirectedStructure
        -- 2 -> KinematicTopologyNetworkStructure
        -- 3 -> KinematicTopologyStructure
        """

    def KinematicTopologyDirectedStructure(self) -> StepKinematics_KinematicTopologyDirectedStructure:
        """
        Returns Value as KinematicTopologyDirectedStructure (or Null if another type)
        """

    def KinematicTopologyNetworkStructure(self) -> StepKinematics_KinematicTopologyNetworkStructure:
        """
        Returns Value as KinematicTopologyNetworkStructure (or Null if another type)
        """

    def KinematicTopologyStructure(self) -> StepKinematics_KinematicTopologyStructure:
        """Returns Value as KinematicTopologyStructure (or Null if another type)"""

class StepKinematics_MechanismRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity MechanismRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_MechanismRepresentation) -> None: ...

    def Init(self, theRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theRepresentedTopology: StepKinematics_KinematicTopologyRepresentationSelect) -> None:
        """Initialize all fields (own and inherited)"""

    def RepresentedTopology(self) -> StepKinematics_KinematicTopologyRepresentationSelect:
        """Returns field RepresentedTopology"""

    def SetRepresentedTopology(self, theRepresentedTopology: StepKinematics_KinematicTopologyRepresentationSelect) -> None:
        """Sets field RepresentedTopology"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_MechanismStateRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a MechanismStateRepresentation"""

    @overload
    def __init__(self, theOther: StepKinematics_MechanismStateRepresentation) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theMechanism: StepKinematics_MechanismRepresentation | None) -> None: ...

    def SetMechanism(self, theMechanism: StepKinematics_MechanismRepresentation | None) -> None: ...

    def Mechanism(self) -> StepKinematics_MechanismRepresentation: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_OrientedJoint(nanoocp.StepShape.StepShape_OrientedEdge):
    """Representation of STEP entity OrientedJoint"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_OrientedJoint) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PairRepresentationRelationship(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity PairRepresentationRelationship"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PairRepresentationRelationship) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentationRelationship_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasRepresentationRelationship_Description: bool, theRepresentationRelationship_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentationRelationship_Rep1: nanoocp.StepRepr.StepRepr_RepresentationOrRepresentationReference, theRepresentationRelationship_Rep2: nanoocp.StepRepr.StepRepr_RepresentationOrRepresentationReference, theRepresentationRelationshipWithTransformation_TransformationOperator: nanoocp.StepRepr.StepRepr_Transformation) -> None:
        """Initialize all fields (own and inherited)"""

    def RepresentationRelationshipWithTransformation(self) -> nanoocp.StepRepr.StepRepr_RepresentationRelationshipWithTransformation:
        """
        Returns data for supertype RepresentationRelationshipWithTransformation
        """

    def SetRepresentationRelationshipWithTransformation(self, theRepresentationRelationshipWithTransformation: nanoocp.StepRepr.StepRepr_RepresentationRelationshipWithTransformation | None) -> None:
        """Sets data for supertype RepresentationRelationshipWithTransformation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PlanarCurvePair(StepKinematics_HighOrderKinematicPair):
    """Representation of STEP entity PlanarCurvePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PlanarCurvePair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theCurve1: nanoocp.StepGeom.StepGeom_Curve | None, theCurve2: nanoocp.StepGeom.StepGeom_Curve | None, theOrientation: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def Curve1(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """Returns field Curve1"""

    def SetCurve1(self, theCurve1: nanoocp.StepGeom.StepGeom_Curve | None) -> None:
        """Sets field Curve1"""

    def Curve2(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """Returns field Curve2"""

    def SetCurve2(self, theCurve2: nanoocp.StepGeom.StepGeom_Curve | None) -> None:
        """Sets field Curve2"""

    def Orientation(self) -> bool:
        """Returns field Orientation"""

    def SetOrientation(self, theOrientation: bool) -> None:
        """Sets field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PlanarCurvePairRange(StepKinematics_PlanarCurvePair):
    """Representation of STEP entity PlanarCurvePairRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PlanarCurvePairRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePlanarCurvePair_Curve1: nanoocp.StepGeom.StepGeom_Curve | None, thePlanarCurvePair_Curve2: nanoocp.StepGeom.StepGeom_Curve | None, thePlanarCurvePair_Orientation: bool, theRangeOnCurve1: nanoocp.StepGeom.StepGeom_TrimmedCurve | None, theRangeOnCurve2: nanoocp.StepGeom.StepGeom_TrimmedCurve | None) -> None:
        """Initialize all fields (own and inherited)"""

    def RangeOnCurve1(self) -> nanoocp.StepGeom.StepGeom_TrimmedCurve:
        """Returns field RangeOnCurve1"""

    def SetRangeOnCurve1(self, theRangeOnCurve1: nanoocp.StepGeom.StepGeom_TrimmedCurve | None) -> None:
        """Sets field RangeOnCurve1"""

    def RangeOnCurve2(self) -> nanoocp.StepGeom.StepGeom_TrimmedCurve:
        """Returns field RangeOnCurve2"""

    def SetRangeOnCurve2(self, theRangeOnCurve2: nanoocp.StepGeom.StepGeom_TrimmedCurve | None) -> None:
        """Sets field RangeOnCurve2"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PlanarPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity PlanarPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PlanarPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PlanarPairValue(StepKinematics_PairValue):
    """Representation of STEP entity PlanarPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PlanarPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualRotation: float, theActualTranslationX: float, theActualTranslationY: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    def ActualTranslationX(self) -> float:
        """Returns field ActualTranslationX"""

    def SetActualTranslationX(self, theActualTranslationX: float) -> None:
        """Sets field ActualTranslationX"""

    def ActualTranslationY(self) -> float:
        """Returns field ActualTranslationY"""

    def SetActualTranslationY(self, theActualTranslationY: float) -> None:
        """Sets field ActualTranslationY"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PlanarPairWithRange(StepKinematics_PlanarPair):
    """Representation of STEP entity PlanarPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PlanarPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitActualRotation: bool, theLowerLimitActualRotation: float, hasUpperLimitActualRotation: bool, theUpperLimitActualRotation: float, hasLowerLimitActualTranslationX: bool, theLowerLimitActualTranslationX: float, hasUpperLimitActualTranslationX: bool, theUpperLimitActualTranslationX: float, hasLowerLimitActualTranslationY: bool, theLowerLimitActualTranslationY: float, hasUpperLimitActualTranslationY: bool, theUpperLimitActualTranslationY: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualRotation(self) -> float:
        """Returns field LowerLimitActualRotation"""

    def SetLowerLimitActualRotation(self, theLowerLimitActualRotation: float) -> None:
        """Sets field LowerLimitActualRotation"""

    def HasLowerLimitActualRotation(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation is defined"""

    def UpperLimitActualRotation(self) -> float:
        """Returns field UpperLimitActualRotation"""

    def SetUpperLimitActualRotation(self, theUpperLimitActualRotation: float) -> None:
        """Sets field UpperLimitActualRotation"""

    def HasUpperLimitActualRotation(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation is defined"""

    def LowerLimitActualTranslationX(self) -> float:
        """Returns field LowerLimitActualTranslationX"""

    def SetLowerLimitActualTranslationX(self, theLowerLimitActualTranslationX: float) -> None:
        """Sets field LowerLimitActualTranslationX"""

    def HasLowerLimitActualTranslationX(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslationX is defined"""

    def UpperLimitActualTranslationX(self) -> float:
        """Returns field UpperLimitActualTranslationX"""

    def SetUpperLimitActualTranslationX(self, theUpperLimitActualTranslationX: float) -> None:
        """Sets field UpperLimitActualTranslationX"""

    def HasUpperLimitActualTranslationX(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslationX is defined"""

    def LowerLimitActualTranslationY(self) -> float:
        """Returns field LowerLimitActualTranslationY"""

    def SetLowerLimitActualTranslationY(self, theLowerLimitActualTranslationY: float) -> None:
        """Sets field LowerLimitActualTranslationY"""

    def HasLowerLimitActualTranslationY(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslationY is defined"""

    def UpperLimitActualTranslationY(self) -> float:
        """Returns field UpperLimitActualTranslationY"""

    def SetUpperLimitActualTranslationY(self, theUpperLimitActualTranslationY: float) -> None:
        """Sets field UpperLimitActualTranslationY"""

    def HasUpperLimitActualTranslationY(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslationY is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PointOnPlanarCurvePair(StepKinematics_HighOrderKinematicPair):
    """Representation of STEP entity PointOnPlanarCurvePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnPlanarCurvePair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePairCurve: nanoocp.StepGeom.StepGeom_Curve | None, theOrientation: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def PairCurve(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """Returns field PairCurve"""

    def SetPairCurve(self, thePairCurve: nanoocp.StepGeom.StepGeom_Curve | None) -> None:
        """Sets field PairCurve"""

    def Orientation(self) -> bool:
        """Returns field Orientation"""

    def SetOrientation(self, theOrientation: bool) -> None:
        """Sets field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SpatialRotation(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SpatialRotation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SpatialRotation) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SpatialRotation select type
        -- 1 -> RotationAboutDirection
        -- 2 -> YprRotation
        """

    def RotationAboutDirection(self) -> StepKinematics_RotationAboutDirection:
        """Returns Value as RotationAboutDirection (or Null if another type)"""

    def YprRotation(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns Value as YprRotation (or Null if another type)"""

class StepKinematics_PointOnPlanarCurvePairValue(StepKinematics_PairValue):
    """Representation of STEP entity PointOnPlanarCurvePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnPlanarCurvePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnCurve: nanoocp.StepGeom.StepGeom_PointOnCurve | None, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnCurve(self) -> nanoocp.StepGeom.StepGeom_PointOnCurve:
        """Returns field ActualPointOnCurve"""

    def SetActualPointOnCurve(self, theActualPointOnCurve: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Sets field ActualPointOnCurve"""

    def InputOrientation(self) -> StepKinematics_SpatialRotation:
        """Returns field InputOrientation"""

    def SetInputOrientation(self, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Sets field InputOrientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PointOnPlanarCurvePairWithRange(StepKinematics_PointOnPlanarCurvePair):
    """Representation of STEP entity PointOnPlanarCurvePairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnPlanarCurvePairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePointOnPlanarCurvePair_PairCurve: nanoocp.StepGeom.StepGeom_Curve | None, thePointOnPlanarCurvePair_Orientation: bool, theRangeOnPairCurve: nanoocp.StepGeom.StepGeom_TrimmedCurve | None, hasLowerLimitYaw: bool, theLowerLimitYaw: float, hasUpperLimitYaw: bool, theUpperLimitYaw: float, hasLowerLimitPitch: bool, theLowerLimitPitch: float, hasUpperLimitPitch: bool, theUpperLimitPitch: float, hasLowerLimitRoll: bool, theLowerLimitRoll: float, hasUpperLimitRoll: bool, theUpperLimitRoll: float) -> None:
        """Initialize all fields (own and inherited)"""

    def RangeOnPairCurve(self) -> nanoocp.StepGeom.StepGeom_TrimmedCurve:
        """Returns field RangeOnPairCurve"""

    def SetRangeOnPairCurve(self, theRangeOnPairCurve: nanoocp.StepGeom.StepGeom_TrimmedCurve | None) -> None:
        """Sets field RangeOnPairCurve"""

    def LowerLimitYaw(self) -> float:
        """Returns field LowerLimitYaw"""

    def SetLowerLimitYaw(self, theLowerLimitYaw: float) -> None:
        """Sets field LowerLimitYaw"""

    def HasLowerLimitYaw(self) -> bool:
        """Returns True if optional field LowerLimitYaw is defined"""

    def UpperLimitYaw(self) -> float:
        """Returns field UpperLimitYaw"""

    def SetUpperLimitYaw(self, theUpperLimitYaw: float) -> None:
        """Sets field UpperLimitYaw"""

    def HasUpperLimitYaw(self) -> bool:
        """Returns True if optional field UpperLimitYaw is defined"""

    def LowerLimitPitch(self) -> float:
        """Returns field LowerLimitPitch"""

    def SetLowerLimitPitch(self, theLowerLimitPitch: float) -> None:
        """Sets field LowerLimitPitch"""

    def HasLowerLimitPitch(self) -> bool:
        """Returns True if optional field LowerLimitPitch is defined"""

    def UpperLimitPitch(self) -> float:
        """Returns field UpperLimitPitch"""

    def SetUpperLimitPitch(self, theUpperLimitPitch: float) -> None:
        """Sets field UpperLimitPitch"""

    def HasUpperLimitPitch(self) -> bool:
        """Returns True if optional field UpperLimitPitch is defined"""

    def LowerLimitRoll(self) -> float:
        """Returns field LowerLimitRoll"""

    def SetLowerLimitRoll(self, theLowerLimitRoll: float) -> None:
        """Sets field LowerLimitRoll"""

    def HasLowerLimitRoll(self) -> bool:
        """Returns True if optional field LowerLimitRoll is defined"""

    def UpperLimitRoll(self) -> float:
        """Returns field UpperLimitRoll"""

    def SetUpperLimitRoll(self, theUpperLimitRoll: float) -> None:
        """Sets field UpperLimitRoll"""

    def HasUpperLimitRoll(self) -> bool:
        """Returns True if optional field UpperLimitRoll is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PointOnSurfacePair(StepKinematics_HighOrderKinematicPair):
    """Representation of STEP entity PointOnSurfacePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnSurfacePair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePairSurface: nanoocp.StepGeom.StepGeom_Surface | None) -> None:
        """Initialize all fields (own and inherited)"""

    def PairSurface(self) -> nanoocp.StepGeom.StepGeom_Surface:
        """Returns field PairSurface"""

    def SetPairSurface(self, thePairSurface: nanoocp.StepGeom.StepGeom_Surface | None) -> None:
        """Sets field PairSurface"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PointOnSurfacePairValue(StepKinematics_PairValue):
    """Representation of STEP entity PointOnSurfacePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnSurfacePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnSurface: nanoocp.StepGeom.StepGeom_PointOnSurface | None, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnSurface(self) -> nanoocp.StepGeom.StepGeom_PointOnSurface:
        """Returns field ActualPointOnSurface"""

    def SetActualPointOnSurface(self, theActualPointOnSurface: nanoocp.StepGeom.StepGeom_PointOnSurface | None) -> None:
        """Sets field ActualPointOnSurface"""

    def InputOrientation(self) -> StepKinematics_SpatialRotation:
        """Returns field InputOrientation"""

    def SetInputOrientation(self, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Sets field InputOrientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PointOnSurfacePairWithRange(StepKinematics_PointOnSurfacePair):
    """Representation of STEP entity PointOnSurfacePairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PointOnSurfacePairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePointOnSurfacePair_PairSurface: nanoocp.StepGeom.StepGeom_Surface | None, theRangeOnPairSurface: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None, hasLowerLimitYaw: bool, theLowerLimitYaw: float, hasUpperLimitYaw: bool, theUpperLimitYaw: float, hasLowerLimitPitch: bool, theLowerLimitPitch: float, hasUpperLimitPitch: bool, theUpperLimitPitch: float, hasLowerLimitRoll: bool, theLowerLimitRoll: float, hasUpperLimitRoll: bool, theUpperLimitRoll: float) -> None:
        """Initialize all fields (own and inherited)"""

    def RangeOnPairSurface(self) -> nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface:
        """Returns field RangeOnPairSurface"""

    def SetRangeOnPairSurface(self, theRangeOnPairSurface: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None) -> None:
        """Sets field RangeOnPairSurface"""

    def LowerLimitYaw(self) -> float:
        """Returns field LowerLimitYaw"""

    def SetLowerLimitYaw(self, theLowerLimitYaw: float) -> None:
        """Sets field LowerLimitYaw"""

    def HasLowerLimitYaw(self) -> bool:
        """Returns True if optional field LowerLimitYaw is defined"""

    def UpperLimitYaw(self) -> float:
        """Returns field UpperLimitYaw"""

    def SetUpperLimitYaw(self, theUpperLimitYaw: float) -> None:
        """Sets field UpperLimitYaw"""

    def HasUpperLimitYaw(self) -> bool:
        """Returns True if optional field UpperLimitYaw is defined"""

    def LowerLimitPitch(self) -> float:
        """Returns field LowerLimitPitch"""

    def SetLowerLimitPitch(self, theLowerLimitPitch: float) -> None:
        """Sets field LowerLimitPitch"""

    def HasLowerLimitPitch(self) -> bool:
        """Returns True if optional field LowerLimitPitch is defined"""

    def UpperLimitPitch(self) -> float:
        """Returns field UpperLimitPitch"""

    def SetUpperLimitPitch(self, theUpperLimitPitch: float) -> None:
        """Sets field UpperLimitPitch"""

    def HasUpperLimitPitch(self) -> bool:
        """Returns True if optional field UpperLimitPitch is defined"""

    def LowerLimitRoll(self) -> float:
        """Returns field LowerLimitRoll"""

    def SetLowerLimitRoll(self, theLowerLimitRoll: float) -> None:
        """Sets field LowerLimitRoll"""

    def HasLowerLimitRoll(self) -> bool:
        """Returns True if optional field LowerLimitRoll is defined"""

    def UpperLimitRoll(self) -> float:
        """Returns field UpperLimitRoll"""

    def SetUpperLimitRoll(self, theUpperLimitRoll: float) -> None:
        """Sets field UpperLimitRoll"""

    def HasUpperLimitRoll(self) -> bool:
        """Returns True if optional field UpperLimitRoll is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PrismaticPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity PrismaticPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PrismaticPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PrismaticPairValue(StepKinematics_PairValue):
    """Representation of STEP entity PrismaticPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PrismaticPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualTranslation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualTranslation(self) -> float:
        """Returns field ActualTranslation"""

    def SetActualTranslation(self, theActualTranslation: float) -> None:
        """Sets field ActualTranslation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_PrismaticPairWithRange(StepKinematics_PrismaticPair):
    """Representation of STEP entity PrismaticPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_PrismaticPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitActualTranslation: bool, theLowerLimitActualTranslation: float, hasUpperLimitActualTranslation: bool, theUpperLimitActualTranslation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualTranslation(self) -> float:
        """Returns field LowerLimitActualTranslation"""

    def SetLowerLimitActualTranslation(self, theLowerLimitActualTranslation: float) -> None:
        """Sets field LowerLimitActualTranslation"""

    def HasLowerLimitActualTranslation(self) -> bool:
        """Returns True if optional field LowerLimitActualTranslation is defined"""

    def UpperLimitActualTranslation(self) -> float:
        """Returns field UpperLimitActualTranslation"""

    def SetUpperLimitActualTranslation(self, theUpperLimitActualTranslation: float) -> None:
        """Sets field UpperLimitActualTranslation"""

    def HasUpperLimitActualTranslation(self) -> bool:
        """Returns True if optional field UpperLimitActualTranslation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ProductDefinitionKinematics(nanoocp.StepRepr.StepRepr_PropertyDefinition):
    """Representation of STEP entity ProductDefinitionKinematics"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ProductDefinitionKinematics) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RackAndPinionPair(StepKinematics_LowOrderKinematicPairWithMotionCoupling):
    """Representation of STEP entity RackAndPinionPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RackAndPinionPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePinionRadius: float) -> None:
        """Initialize all fields (own and inherited)"""

    def PinionRadius(self) -> float:
        """Returns field PinionRadius"""

    def SetPinionRadius(self, thePinionRadius: float) -> None:
        """Sets field PinionRadius"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RackAndPinionPairValue(StepKinematics_PairValue):
    """Representation of STEP entity RackAndPinionPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RackAndPinionPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualDisplacement: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualDisplacement(self) -> float:
        """Returns field ActualDisplacement"""

    def SetActualDisplacement(self, theActualDisplacement: float) -> None:
        """Sets field ActualDisplacement"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RackAndPinionPairWithRange(StepKinematics_RackAndPinionPair):
    """Representation of STEP entity RackAndPinionPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RackAndPinionPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theRackAndPinionPair_PinionRadius: float, hasLowerLimitRackDisplacement: bool, theLowerLimitRackDisplacement: float, hasUpperLimitRackDisplacement: bool, theUpperLimitRackDisplacement: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitRackDisplacement(self) -> float:
        """Returns field LowerLimitRackDisplacement"""

    def SetLowerLimitRackDisplacement(self, theLowerLimitRackDisplacement: float) -> None:
        """Sets field LowerLimitRackDisplacement"""

    def HasLowerLimitRackDisplacement(self) -> bool:
        """Returns True if optional field LowerLimitRackDisplacement is defined"""

    def UpperLimitRackDisplacement(self) -> float:
        """Returns field UpperLimitRackDisplacement"""

    def SetUpperLimitRackDisplacement(self, theUpperLimitRackDisplacement: float) -> None:
        """Sets field UpperLimitRackDisplacement"""

    def HasUpperLimitRackDisplacement(self) -> bool:
        """Returns True if optional field UpperLimitRackDisplacement is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RevolutePair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity RevolutePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RevolutePair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RevolutePairValue(StepKinematics_PairValue):
    """Representation of STEP entity RevolutePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RevolutePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RevolutePairWithRange(StepKinematics_RevolutePair):
    """Representation of STEP entity RevolutePairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RevolutePairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitActualRotation: bool, theLowerLimitActualRotation: float, hasUpperLimitActualRotation: bool, theUpperLimitActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualRotation(self) -> float:
        """Returns field LowerLimitActualRotation"""

    def SetLowerLimitActualRotation(self, theLowerLimitActualRotation: float) -> None:
        """Sets field LowerLimitActualRotation"""

    def HasLowerLimitActualRotation(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation is defined"""

    def UpperLimitActualRotation(self) -> float:
        """Returns field UpperLimitActualRotation"""

    def SetUpperLimitActualRotation(self, theUpperLimitActualRotation: float) -> None:
        """Sets field UpperLimitActualRotation"""

    def HasUpperLimitActualRotation(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RigidLinkRepresentation(StepKinematics_KinematicLinkRepresentation):
    """Representation of STEP entity RigidLinkRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RigidLinkRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RigidPlacement(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type RigidPlacement"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RigidPlacement) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of RigidPlacement select type
        -- 1 -> Axis2Placement3d
        -- 2 -> SuParameters
        """

    def Axis2Placement3d(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns Value as Axis2Placement3d (or Null if another type)"""

    def SuParameters(self) -> nanoocp.StepGeom.StepGeom_SuParameters:
        """Returns Value as SuParameters (or Null if another type)"""

class StepKinematics_RollingCurvePair(StepKinematics_PlanarCurvePair):
    """Representation of STEP entity RollingCurvePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RollingCurvePair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RollingCurvePairValue(StepKinematics_PairValue):
    """Representation of STEP entity RollingCurvePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RollingCurvePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnCurve1: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnCurve1(self) -> nanoocp.StepGeom.StepGeom_PointOnCurve:
        """Returns field ActualPointOnCurve1"""

    def SetActualPointOnCurve1(self, theActualPointOnCurve1: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Sets field ActualPointOnCurve1"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SurfacePair(StepKinematics_HighOrderKinematicPair):
    """Representation of STEP entity SurfacePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SurfacePair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theSurface1: nanoocp.StepGeom.StepGeom_Surface | None, theSurface2: nanoocp.StepGeom.StepGeom_Surface | None, theOrientation: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def Surface1(self) -> nanoocp.StepGeom.StepGeom_Surface:
        """Returns field Surface1"""

    def SetSurface1(self, theSurface1: nanoocp.StepGeom.StepGeom_Surface | None) -> None:
        """Sets field Surface1"""

    def Surface2(self) -> nanoocp.StepGeom.StepGeom_Surface:
        """Returns field Surface2"""

    def SetSurface2(self, theSurface2: nanoocp.StepGeom.StepGeom_Surface | None) -> None:
        """Sets field Surface2"""

    def Orientation(self) -> bool:
        """Returns field Orientation"""

    def SetOrientation(self, theOrientation: bool) -> None:
        """Sets field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RollingSurfacePair(StepKinematics_SurfacePair):
    """Representation of STEP entity RollingSurfacePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RollingSurfacePair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RollingSurfacePairValue(StepKinematics_PairValue):
    """Representation of STEP entity RollingSurfacePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RollingSurfacePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnSurface: nanoocp.StepGeom.StepGeom_PointOnSurface | None, theActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnSurface(self) -> nanoocp.StepGeom.StepGeom_PointOnSurface:
        """Returns field ActualPointOnSurface"""

    def SetActualPointOnSurface(self, theActualPointOnSurface: nanoocp.StepGeom.StepGeom_PointOnSurface | None) -> None:
        """Sets field ActualPointOnSurface"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_RotationAboutDirection(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity RotationAboutDirection"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_RotationAboutDirection) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theDirectionOfAxis: nanoocp.StepGeom.StepGeom_Direction | None, theRotationAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def DirectionOfAxis(self) -> nanoocp.StepGeom.StepGeom_Direction:
        """Returns field DirectionOfAxis"""

    def SetDirectionOfAxis(self, theDirectionOfAxis: nanoocp.StepGeom.StepGeom_Direction | None) -> None:
        """Sets field DirectionOfAxis"""

    def RotationAngle(self) -> float:
        """Returns field RotationAngle"""

    def SetRotationAngle(self, theRotationAngle: float) -> None:
        """Sets field RotationAngle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ScrewPair(StepKinematics_LowOrderKinematicPairWithMotionCoupling):
    """Representation of STEP entity ScrewPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ScrewPair) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, thePitch: float) -> None:
        """Initialize all fields (own and inherited)"""

    def Pitch(self) -> float:
        """Returns field Pitch"""

    def SetPitch(self, thePitch: float) -> None:
        """Sets field Pitch"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ScrewPairValue(StepKinematics_PairValue):
    """Representation of STEP entity ScrewPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ScrewPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_ScrewPairWithRange(StepKinematics_ScrewPair):
    """Representation of STEP entity ScrewPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_ScrewPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theScrewPair_Pitch: float, hasLowerLimitActualRotation: bool, theLowerLimitActualRotation: float, hasUpperLimitActualRotation: bool, theUpperLimitActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitActualRotation(self) -> float:
        """Returns field LowerLimitActualRotation"""

    def SetLowerLimitActualRotation(self, theLowerLimitActualRotation: float) -> None:
        """Sets field LowerLimitActualRotation"""

    def HasLowerLimitActualRotation(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation is defined"""

    def UpperLimitActualRotation(self) -> float:
        """Returns field UpperLimitActualRotation"""

    def SetUpperLimitActualRotation(self, theUpperLimitActualRotation: float) -> None:
        """Sets field UpperLimitActualRotation"""

    def HasUpperLimitActualRotation(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SlidingCurvePair(StepKinematics_PlanarCurvePair):
    """Representation of STEP entity SlidingCurvePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SlidingCurvePair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SlidingCurvePairValue(StepKinematics_PairValue):
    """Representation of STEP entity SlidingCurvePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SlidingCurvePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnCurve1: nanoocp.StepGeom.StepGeom_PointOnCurve | None, theActualPointOnCurve2: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnCurve1(self) -> nanoocp.StepGeom.StepGeom_PointOnCurve:
        """Returns field ActualPointOnCurve1"""

    def SetActualPointOnCurve1(self, theActualPointOnCurve1: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Sets field ActualPointOnCurve1"""

    def ActualPointOnCurve2(self) -> nanoocp.StepGeom.StepGeom_PointOnCurve:
        """Returns field ActualPointOnCurve2"""

    def SetActualPointOnCurve2(self, theActualPointOnCurve2: nanoocp.StepGeom.StepGeom_PointOnCurve | None) -> None:
        """Sets field ActualPointOnCurve2"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SlidingSurfacePair(StepKinematics_SurfacePair):
    """Representation of STEP entity SlidingSurfacePair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SlidingSurfacePair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SlidingSurfacePairValue(StepKinematics_PairValue):
    """Representation of STEP entity SlidingSurfacePairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SlidingSurfacePairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPointOnSurface1: nanoocp.StepGeom.StepGeom_PointOnSurface | None, theActualPointOnSurface2: nanoocp.StepGeom.StepGeom_PointOnSurface | None, theActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPointOnSurface1(self) -> nanoocp.StepGeom.StepGeom_PointOnSurface:
        """Returns field ActualPointOnSurface1"""

    def SetActualPointOnSurface1(self, theActualPointOnSurface1: nanoocp.StepGeom.StepGeom_PointOnSurface | None) -> None:
        """Sets field ActualPointOnSurface1"""

    def ActualPointOnSurface2(self) -> nanoocp.StepGeom.StepGeom_PointOnSurface:
        """Returns field ActualPointOnSurface2"""

    def SetActualPointOnSurface2(self, theActualPointOnSurface2: nanoocp.StepGeom.StepGeom_PointOnSurface | None) -> None:
        """Sets field ActualPointOnSurface2"""

    def ActualRotation(self) -> float:
        """Returns field ActualRotation"""

    def SetActualRotation(self, theActualRotation: float) -> None:
        """Sets field ActualRotation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SphericalPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity SphericalPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SphericalPairSelect(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SphericalPairSelect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPairSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SphericalPairSelect select type
        -- 1 -> SphericalPair
        -- 2 -> SphericalPairWithPin
        """

    def SphericalPair(self) -> StepKinematics_SphericalPair:
        """Returns Value as SphericalPair (or Null if another type)"""

    def SphericalPairWithPin(self) -> StepKinematics_SphericalPairWithPin:
        """Returns Value as SphericalPairWithPin (or Null if another type)"""

class StepKinematics_SphericalPairValue(StepKinematics_PairValue):
    """Representation of STEP entity SphericalPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Initialize all fields (own and inherited)"""

    def InputOrientation(self) -> StepKinematics_SpatialRotation:
        """Returns field InputOrientation"""

    def SetInputOrientation(self, theInputOrientation: StepKinematics_SpatialRotation) -> None:
        """Sets field InputOrientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SphericalPairWithPin(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity SphericalPairWithPin"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPairWithPin) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SphericalPairWithPinAndRange(StepKinematics_SphericalPairWithPin):
    """Representation of STEP entity SphericalPairWithPinAndRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPairWithPinAndRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitYaw: bool, theLowerLimitYaw: float, hasUpperLimitYaw: bool, theUpperLimitYaw: float, hasLowerLimitRoll: bool, theLowerLimitRoll: float, hasUpperLimitRoll: bool, theUpperLimitRoll: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitYaw(self) -> float:
        """Returns field LowerLimitYaw"""

    def SetLowerLimitYaw(self, theLowerLimitYaw: float) -> None:
        """Sets field LowerLimitYaw"""

    def HasLowerLimitYaw(self) -> bool:
        """Returns True if optional field LowerLimitYaw is defined"""

    def UpperLimitYaw(self) -> float:
        """Returns field UpperLimitYaw"""

    def SetUpperLimitYaw(self, theUpperLimitYaw: float) -> None:
        """Sets field UpperLimitYaw"""

    def HasUpperLimitYaw(self) -> bool:
        """Returns True if optional field UpperLimitYaw is defined"""

    def LowerLimitRoll(self) -> float:
        """Returns field LowerLimitRoll"""

    def SetLowerLimitRoll(self, theLowerLimitRoll: float) -> None:
        """Sets field LowerLimitRoll"""

    def HasLowerLimitRoll(self) -> bool:
        """Returns True if optional field LowerLimitRoll is defined"""

    def UpperLimitRoll(self) -> float:
        """Returns field UpperLimitRoll"""

    def SetUpperLimitRoll(self, theUpperLimitRoll: float) -> None:
        """Sets field UpperLimitRoll"""

    def HasUpperLimitRoll(self) -> bool:
        """Returns True if optional field UpperLimitRoll is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SphericalPairWithRange(StepKinematics_SphericalPair):
    """Representation of STEP entity SphericalPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SphericalPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasLowerLimitYaw: bool, theLowerLimitYaw: float, hasUpperLimitYaw: bool, theUpperLimitYaw: float, hasLowerLimitPitch: bool, theLowerLimitPitch: float, hasUpperLimitPitch: bool, theUpperLimitPitch: float, hasLowerLimitRoll: bool, theLowerLimitRoll: float, hasUpperLimitRoll: bool, theUpperLimitRoll: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitYaw(self) -> float:
        """Returns field LowerLimitYaw"""

    def SetLowerLimitYaw(self, theLowerLimitYaw: float) -> None:
        """Sets field LowerLimitYaw"""

    def HasLowerLimitYaw(self) -> bool:
        """Returns True if optional field LowerLimitYaw is defined"""

    def UpperLimitYaw(self) -> float:
        """Returns field UpperLimitYaw"""

    def SetUpperLimitYaw(self, theUpperLimitYaw: float) -> None:
        """Sets field UpperLimitYaw"""

    def HasUpperLimitYaw(self) -> bool:
        """Returns True if optional field UpperLimitYaw is defined"""

    def LowerLimitPitch(self) -> float:
        """Returns field LowerLimitPitch"""

    def SetLowerLimitPitch(self, theLowerLimitPitch: float) -> None:
        """Sets field LowerLimitPitch"""

    def HasLowerLimitPitch(self) -> bool:
        """Returns True if optional field LowerLimitPitch is defined"""

    def UpperLimitPitch(self) -> float:
        """Returns field UpperLimitPitch"""

    def SetUpperLimitPitch(self, theUpperLimitPitch: float) -> None:
        """Sets field UpperLimitPitch"""

    def HasUpperLimitPitch(self) -> bool:
        """Returns True if optional field UpperLimitPitch is defined"""

    def LowerLimitRoll(self) -> float:
        """Returns field LowerLimitRoll"""

    def SetLowerLimitRoll(self, theLowerLimitRoll: float) -> None:
        """Sets field LowerLimitRoll"""

    def HasLowerLimitRoll(self) -> bool:
        """Returns True if optional field LowerLimitRoll is defined"""

    def UpperLimitRoll(self) -> float:
        """Returns field UpperLimitRoll"""

    def SetUpperLimitRoll(self, theUpperLimitRoll: float) -> None:
        """Sets field UpperLimitRoll"""

    def HasUpperLimitRoll(self) -> bool:
        """Returns True if optional field UpperLimitRoll is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_SurfacePairWithRange(StepKinematics_SurfacePair):
    """Representation of STEP entity SurfacePairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_SurfacePairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theSurfacePair_Surface1: nanoocp.StepGeom.StepGeom_Surface | None, theSurfacePair_Surface2: nanoocp.StepGeom.StepGeom_Surface | None, theSurfacePair_Orientation: bool, theRangeOnSurface1: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None, theRangeOnSurface2: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None, hasLowerLimitActualRotation: bool, theLowerLimitActualRotation: float, hasUpperLimitActualRotation: bool, theUpperLimitActualRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def RangeOnSurface1(self) -> nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface:
        """Returns field RangeOnSurface1"""

    def SetRangeOnSurface1(self, theRangeOnSurface1: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None) -> None:
        """Sets field RangeOnSurface1"""

    def RangeOnSurface2(self) -> nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface:
        """Returns field RangeOnSurface2"""

    def SetRangeOnSurface2(self, theRangeOnSurface2: nanoocp.StepGeom.StepGeom_RectangularTrimmedSurface | None) -> None:
        """Sets field RangeOnSurface2"""

    def LowerLimitActualRotation(self) -> float:
        """Returns field LowerLimitActualRotation"""

    def SetLowerLimitActualRotation(self, theLowerLimitActualRotation: float) -> None:
        """Sets field LowerLimitActualRotation"""

    def HasLowerLimitActualRotation(self) -> bool:
        """Returns True if optional field LowerLimitActualRotation is defined"""

    def UpperLimitActualRotation(self) -> float:
        """Returns field UpperLimitActualRotation"""

    def SetUpperLimitActualRotation(self, theUpperLimitActualRotation: float) -> None:
        """Sets field UpperLimitActualRotation"""

    def HasUpperLimitActualRotation(self) -> bool:
        """Returns True if optional field UpperLimitActualRotation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicTopologyDirectedStructure(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity KinematicTopologyDirectedStructure"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicTopologyDirectedStructure) -> None: ...

    def Init(self, theRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theParent: StepKinematics_KinematicTopologyStructure | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Parent(self) -> StepKinematics_KinematicTopologyStructure:
        """Returns field Parent"""

    def SetParent(self, theParent: StepKinematics_KinematicTopologyStructure | None) -> None:
        """Sets field Parent"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_KinematicTopologyNetworkStructure(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity KinematicTopologyNetworkStructure"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_KinematicTopologyNetworkStructure) -> None: ...

    def Init(self, theRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theParent: StepKinematics_KinematicTopologyStructure | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Parent(self) -> StepKinematics_KinematicTopologyStructure:
        """Returns field Parent"""

    def SetParent(self, theParent: StepKinematics_KinematicTopologyStructure | None) -> None:
        """Sets field Parent"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_UnconstrainedPair(StepKinematics_LowOrderKinematicPair):
    """Representation of STEP entity UnconstrainedPair"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_UnconstrainedPair) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_UnconstrainedPairValue(StepKinematics_PairValue):
    """Representation of STEP entity UnconstrainedPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_UnconstrainedPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theActualPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ActualPlacement(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns field ActualPlacement"""

    def SetActualPlacement(self, theActualPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Sets field ActualPlacement"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_UniversalPairValue(StepKinematics_PairValue):
    """Representation of STEP entity UniversalPairValue"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_UniversalPairValue) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, thePairValue_AppliesToPair: StepKinematics_KinematicPair | None, theFirstRotationAngle: float, theSecondRotationAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def FirstRotationAngle(self) -> float:
        """Returns field FirstRotationAngle"""

    def SetFirstRotationAngle(self, theFirstRotationAngle: float) -> None:
        """Sets field FirstRotationAngle"""

    def SecondRotationAngle(self) -> float:
        """Returns field SecondRotationAngle"""

    def SetSecondRotationAngle(self, theSecondRotationAngle: float) -> None:
        """Sets field SecondRotationAngle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepKinematics_UniversalPairWithRange(StepKinematics_UniversalPair):
    """Representation of STEP entity UniversalPairWithRange"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepKinematics_UniversalPairWithRange) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasItemDefinedTransformation_Description: bool, theItemDefinedTransformation_Description: nanoocp.TCollection.TCollection_HAsciiString | None, theItemDefinedTransformation_TransformItem1: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theItemDefinedTransformation_TransformItem2: nanoocp.StepRepr.StepRepr_RepresentationItem | None, theKinematicPair_Joint: StepKinematics_KinematicJoint | None, theLowOrderKinematicPair_TX: bool, theLowOrderKinematicPair_TY: bool, theLowOrderKinematicPair_TZ: bool, theLowOrderKinematicPair_RX: bool, theLowOrderKinematicPair_RY: bool, theLowOrderKinematicPair_RZ: bool, hasUniversalPair_InputSkewAngle: bool, theUniversalPair_InputSkewAngle: float, hasLowerLimitFirstRotation: bool, theLowerLimitFirstRotation: float, hasUpperLimitFirstRotation: bool, theUpperLimitFirstRotation: float, hasLowerLimitSecondRotation: bool, theLowerLimitSecondRotation: float, hasUpperLimitSecondRotation: bool, theUpperLimitSecondRotation: float) -> None:
        """Initialize all fields (own and inherited)"""

    def LowerLimitFirstRotation(self) -> float:
        """Returns field LowerLimitFirstRotation"""

    def SetLowerLimitFirstRotation(self, theLowerLimitFirstRotation: float) -> None:
        """Sets field LowerLimitFirstRotation"""

    def HasLowerLimitFirstRotation(self) -> bool:
        """Returns True if optional field LowerLimitFirstRotation is defined"""

    def UpperLimitFirstRotation(self) -> float:
        """Returns field UpperLimitFirstRotation"""

    def SetUpperLimitFirstRotation(self, theUpperLimitFirstRotation: float) -> None:
        """Sets field UpperLimitFirstRotation"""

    def HasUpperLimitFirstRotation(self) -> bool:
        """Returns True if optional field UpperLimitFirstRotation is defined"""

    def LowerLimitSecondRotation(self) -> float:
        """Returns field LowerLimitSecondRotation"""

    def SetLowerLimitSecondRotation(self, theLowerLimitSecondRotation: float) -> None:
        """Sets field LowerLimitSecondRotation"""

    def HasLowerLimitSecondRotation(self) -> bool:
        """Returns True if optional field LowerLimitSecondRotation is defined"""

    def UpperLimitSecondRotation(self) -> float:
        """Returns field UpperLimitSecondRotation"""

    def SetUpperLimitSecondRotation(self, theUpperLimitSecondRotation: float) -> None:
        """Sets field UpperLimitSecondRotation"""

    def HasUpperLimitSecondRotation(self) -> bool:
        """Returns True if optional field UpperLimitSecondRotation is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
