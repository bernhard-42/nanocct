"""OCCT package StepFEA (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepElement
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.TCollection


class StepFEA_CoordinateSystemType(enum.IntEnum):
    StepFEA_Cartesian = 0

    StepFEA_Cylindrical = 1

    StepFEA_Spherical = 2

StepFEA_Cartesian: StepFEA_CoordinateSystemType = StepFEA_CoordinateSystemType.StepFEA_Cartesian

StepFEA_Cylindrical: StepFEA_CoordinateSystemType = StepFEA_CoordinateSystemType.StepFEA_Cylindrical

StepFEA_Spherical: StepFEA_CoordinateSystemType = StepFEA_CoordinateSystemType.StepFEA_Spherical

class StepFEA_CurveEdge(enum.IntEnum):
    StepFEA_ElementEdge = 0

StepFEA_ElementEdge: StepFEA_CurveEdge = StepFEA_CurveEdge.StepFEA_ElementEdge

class StepFEA_EnumeratedDegreeOfFreedom(enum.IntEnum):
    StepFEA_XTranslation = 0

    StepFEA_YTranslation = 1

    StepFEA_ZTranslation = 2

    StepFEA_XRotation = 3

    StepFEA_YRotation = 4

    StepFEA_ZRotation = 5

    StepFEA_Warp = 6

StepFEA_XTranslation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_YTranslation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_ZTranslation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_XRotation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_YRotation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_ZRotation: StepFEA_EnumeratedDegreeOfFreedom = ...

StepFEA_Warp: StepFEA_EnumeratedDegreeOfFreedom = StepFEA_EnumeratedDegreeOfFreedom.StepFEA_Warp

class StepFEA_ElementVolume(enum.IntEnum):
    StepFEA_Volume = 0

StepFEA_Volume: StepFEA_ElementVolume = StepFEA_ElementVolume.StepFEA_Volume

class StepFEA_UnspecifiedValue(enum.IntEnum):
    StepFEA_Unspecified = 0

StepFEA_Unspecified: StepFEA_UnspecifiedValue = StepFEA_UnspecifiedValue.StepFEA_Unspecified

class StepFEA_FeaRepresentationItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    """Representation of STEP entity FeaRepresentationItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaRepresentationItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_AlignedCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """Representation of STEP entity AlignedCurve3dElementCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_AlignedCurve3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aCoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d:
        """Returns field CoordinateSystem"""

    def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Set field CoordinateSystem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_AlignedSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """Representation of STEP entity AlignedSurface3dElementCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_AlignedSurface3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aCoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d:
        """Returns field CoordinateSystem"""

    def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Set field CoordinateSystem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ArbitraryVolume3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """Representation of STEP entity ArbitraryVolume3dElementCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ArbitraryVolume3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aCoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d:
        """Returns field CoordinateSystem"""

    def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d | None) -> None:
        """Set field CoordinateSystem"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ConstantSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """Representation of STEP entity ConstantSurface3dElementCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ConstantSurface3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aAxis: int, aAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def Axis(self) -> int:
        """Returns field Axis"""

    def SetAxis(self, Axis: int) -> None:
        """Set field Axis"""

    def Angle(self) -> float:
        """Returns field Angle"""

    def SetAngle(self, Angle: float) -> None:
        """Set field Angle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementInterval(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementInterval"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementInterval) -> None: ...

    def Init(self, aFinishPosition: StepFEA_CurveElementLocation | None, aEuAngles: nanoocp.StepBasic.StepBasic_EulerAngles | None) -> None:
        """Initialize all fields (own and inherited)"""

    def FinishPosition(self) -> StepFEA_CurveElementLocation:
        """Returns field FinishPosition"""

    def SetFinishPosition(self, FinishPosition: StepFEA_CurveElementLocation | None) -> None:
        """Set field FinishPosition"""

    def EuAngles(self) -> nanoocp.StepBasic.StepBasic_EulerAngles:
        """Returns field EuAngles"""

    def SetEuAngles(self, EuAngles: nanoocp.StepBasic.StepBasic_EulerAngles | None) -> None:
        """Set field EuAngles"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementEndCoordinateSystem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type CurveElementEndCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementEndCoordinateSystem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of CurveElementEndCoordinateSystem select type
        1 -> FeaAxis2Placement3d from StepFEA
        2 -> AlignedCurve3dElementCoordinateSystem from StepFEA
        3 -> ParametricCurve3dElementCoordinateSystem from StepFEA
        0 else
        """

    def FeaAxis2Placement3d(self) -> StepFEA_FeaAxis2Placement3d:
        """Returns Value as FeaAxis2Placement3d (or Null if another type)"""

    def AlignedCurve3dElementCoordinateSystem(self) -> StepFEA_AlignedCurve3dElementCoordinateSystem:
        """
        Returns Value as AlignedCurve3dElementCoordinateSystem (or Null if another type)
        """

    def ParametricCurve3dElementCoordinateSystem(self) -> StepFEA_ParametricCurve3dElementCoordinateSystem:
        """
        Returns Value as ParametricCurve3dElementCoordinateSystem (or Null if another type)
        """

class StepFEA_CurveElementEndOffset(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementEndOffset"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementEndOffset) -> None: ...

    def Init(self, aCoordinateSystem: StepFEA_CurveElementEndCoordinateSystem, aOffsetVector: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem:
        """Returns field CoordinateSystem"""

    def SetCoordinateSystem(self, CoordinateSystem: StepFEA_CurveElementEndCoordinateSystem) -> None:
        """Set field CoordinateSystem"""

    def OffsetVector(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns field OffsetVector"""

    def SetOffsetVector(self, OffsetVector: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set field OffsetVector"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementEndRelease(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementEndRelease"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementEndRelease) -> None: ...

    def Init(self, aCoordinateSystem: StepFEA_CurveElementEndCoordinateSystem, aReleases: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementEndReleasePacket] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem:
        """Returns field CoordinateSystem"""

    def SetCoordinateSystem(self, CoordinateSystem: StepFEA_CurveElementEndCoordinateSystem) -> None:
        """Set field CoordinateSystem"""

    def Releases(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementEndReleasePacket]:
        """Returns field Releases"""

    def SetReleases(self, Releases: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementEndReleasePacket] | None) -> None:
        """Set field Releases"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_Curve3dElementProperty(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Curve3dElementProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_Curve3dElementProperty) -> None: ...

    def Init(self, aPropertyId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aIntervalDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementInterval] | None, aEndOffsets: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndOffset] | None, aEndReleases: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndRelease] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def PropertyId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field PropertyId"""

    def SetPropertyId(self, PropertyId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field PropertyId"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def IntervalDefinitions(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementInterval]:
        """Returns field IntervalDefinitions"""

    def SetIntervalDefinitions(self, IntervalDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementInterval] | None) -> None:
        """Set field IntervalDefinitions"""

    def EndOffsets(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndOffset]:
        """Returns field EndOffsets"""

    def SetEndOffsets(self, EndOffsets: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndOffset] | None) -> None:
        """Set field EndOffsets"""

    def EndReleases(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndRelease]:
        """Returns field EndReleases"""

    def SetEndReleases(self, EndReleases: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndRelease] | None) -> None:
        """Set field EndReleases"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity NodeRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeRepresentation) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aModelRef: StepFEA_FeaModel | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModelRef(self) -> StepFEA_FeaModel:
        """Returns field ModelRef"""

    def SetModelRef(self, ModelRef: StepFEA_FeaModel | None) -> None:
        """Set field ModelRef"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ElementRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity ElementRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ElementRepresentation) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aNodeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def NodeList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation]:
        """Returns field NodeList"""

    def SetNodeList(self, NodeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Set field NodeList"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_Curve3dElementRepresentation(StepFEA_ElementRepresentation):
    """Representation of STEP entity Curve3dElementRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_Curve3dElementRepresentation) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aElementRepresentation_NodeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None, aModelRef: StepFEA_FeaModel3d | None, aElementDescriptor: nanoocp.StepElement.StepElement_Curve3dElementDescriptor | None, aProperty: StepFEA_Curve3dElementProperty | None, aMaterial: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModelRef(self) -> StepFEA_FeaModel3d:
        """Returns field ModelRef"""

    def SetModelRef(self, ModelRef: StepFEA_FeaModel3d | None) -> None:
        """Set field ModelRef"""

    def ElementDescriptor(self) -> nanoocp.StepElement.StepElement_Curve3dElementDescriptor:
        """Returns field ElementDescriptor"""

    def SetElementDescriptor(self, ElementDescriptor: nanoocp.StepElement.StepElement_Curve3dElementDescriptor | None) -> None:
        """Set field ElementDescriptor"""

    def Property(self) -> StepFEA_Curve3dElementProperty:
        """Returns field Property"""

    def SetProperty(self, Property: StepFEA_Curve3dElementProperty | None) -> None:
        """Set field Property"""

    def Material(self) -> nanoocp.StepElement.StepElement_ElementMaterial:
        """Returns field Material"""

    def SetMaterial(self, Material: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Set field Material"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementIntervalConstant(StepFEA_CurveElementInterval):
    """Representation of STEP entity CurveElementIntervalConstant"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementIntervalConstant) -> None: ...

    def Init(self, aCurveElementInterval_FinishPosition: StepFEA_CurveElementLocation | None, aCurveElementInterval_EuAngles: nanoocp.StepBasic.StepBasic_EulerAngles | None, aSection: nanoocp.StepElement.StepElement_CurveElementSectionDefinition | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Section(self) -> nanoocp.StepElement.StepElement_CurveElementSectionDefinition:
        """Returns field Section"""

    def SetSection(self, Section: nanoocp.StepElement.StepElement_CurveElementSectionDefinition | None) -> None:
        """Set field Section"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementIntervalLinearlyVarying(StepFEA_CurveElementInterval):
    """Representation of STEP entity CurveElementIntervalLinearlyVarying"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementIntervalLinearlyVarying) -> None: ...

    def Init(self, aCurveElementInterval_FinishPosition: StepFEA_CurveElementLocation | None, aCurveElementInterval_EuAngles: nanoocp.StepBasic.StepBasic_EulerAngles | None, aSections: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementSectionDefinition] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Sections(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]:
        """Returns field Sections"""

    def SetSections(self, Sections: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementSectionDefinition] | None) -> None:
        """Set field Sections"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_CurveElementLocation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementLocation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_CurveElementLocation) -> None: ...

    def Init(self, aCoordinate: StepFEA_FeaParametricPoint | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinate(self) -> StepFEA_FeaParametricPoint:
        """Returns field Coordinate"""

    def SetCoordinate(self, Coordinate: StepFEA_FeaParametricPoint | None) -> None:
        """Set field Coordinate"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_DegreeOfFreedom(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type DegreeOfFreedom"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_DegreeOfFreedom) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of CurveElementFreedom select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member CurveElementFreedomMember
        1 -> EnumeratedCurveElementFreedom
        2 -> ApplicationDefinedDegreeOfFreedom
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type CurveElementFreedomMember"""

    def SetEnumeratedDegreeOfFreedom(self, aVal: StepFEA_EnumeratedDegreeOfFreedom) -> None:
        """Returns Value as EnumeratedDegreeOfFreedom (or Null if another type)"""

    def EnumeratedDegreeOfFreedom(self) -> StepFEA_EnumeratedDegreeOfFreedom:
        """Returns Value as EnumeratedDegreeOfFreedom (or Null if another type)"""

    def SetApplicationDefinedDegreeOfFreedom(self, aVal: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set Value for ApplicationDefinedDegreeOfFreedom"""

    def ApplicationDefinedDegreeOfFreedom(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Value as ApplicationDefinedDegreeOfFreedom (or Null if another type)
        """

class StepFEA_DegreeOfFreedomMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type CurveElementFreedom"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_DegreeOfFreedomMember) -> None: ...

    def HasName(self) -> bool:
        """Returns True if has name"""

    def Name(self) -> str:
        """Returns set name"""

    def SetName(self, name: str) -> bool:
        """Set name"""

    def Matches(self, name: str) -> bool:
        """Tells if the name of a SelectMember matches a given one;"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_DummyNode(StepFEA_NodeRepresentation):
    """Representation of STEP entity DummyNode"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_DummyNode) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ElementOrElementGroup(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ElementOrElementGroup"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ElementOrElementGroup) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ElementOrElementGroup select type
        1 -> ElementRepresentation from StepFEA
        2 -> ElementGroup from StepFEA
        0 else
        """

    def ElementRepresentation(self) -> StepFEA_ElementRepresentation:
        """Returns Value as ElementRepresentation (or Null if another type)"""

    def ElementGroup(self) -> StepFEA_ElementGroup:
        """Returns Value as ElementGroup (or Null if another type)"""

class StepFEA_ElementGeometricRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ElementGeometricRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ElementGeometricRelationship) -> None: ...

    def Init(self, aElementRef: StepFEA_ElementOrElementGroup, aItem: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None, aAspect: nanoocp.StepElement.StepElement_ElementAspect) -> None:
        """Initialize all fields (own and inherited)"""

    def ElementRef(self) -> StepFEA_ElementOrElementGroup:
        """Returns field ElementRef"""

    def SetElementRef(self, ElementRef: StepFEA_ElementOrElementGroup) -> None:
        """Set field ElementRef"""

    def Item(self) -> nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation:
        """Returns field Item"""

    def SetItem(self, Item: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None) -> None:
        """Set field Item"""

    def Aspect(self) -> nanoocp.StepElement.StepElement_ElementAspect:
        """Returns field Aspect"""

    def SetAspect(self, Aspect: nanoocp.StepElement.StepElement_ElementAspect) -> None:
        """Set field Aspect"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaGroup(nanoocp.StepBasic.StepBasic_Group):
    """Representation of STEP entity FeaGroup"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaGroup) -> None: ...

    def Init(self, aGroup_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aGroup_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aModelRef: StepFEA_FeaModel | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModelRef(self) -> StepFEA_FeaModel:
        """Returns field ModelRef"""

    def SetModelRef(self, ModelRef: StepFEA_FeaModel | None) -> None:
        """Set field ModelRef"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ElementGroup(StepFEA_FeaGroup):
    """Representation of STEP entity ElementGroup"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ElementGroup) -> None: ...

    def Init(self, aGroup_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aGroup_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaGroup_ModelRef: StepFEA_FeaModel | None, aElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_ElementRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Elements(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_ElementRepresentation]:
        """Returns field Elements"""

    def SetElements(self, Elements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_ElementRepresentation] | None) -> None:
        """Set field Elements"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaMaterialPropertyRepresentationItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    """Representation of STEP entity FeaMaterialPropertyRepresentationItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaMaterialPropertyRepresentationItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaAreaDensity(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaAreaDensity"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaAreaDensity) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstant: float) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstant(self) -> float:
        """Returns field FeaConstant"""

    def SetFeaConstant(self, FeaConstant: float) -> None:
        """Set field FeaConstant"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaAxis2Placement3d(nanoocp.StepGeom.StepGeom_Axis2Placement3d):
    """Representation of STEP entity FeaAxis2Placement3d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaAxis2Placement3d) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aPlacement_Location: nanoocp.StepGeom.StepGeom_CartesianPoint | None, hasAxis2Placement3d_Axis: bool, aAxis2Placement3d_Axis: nanoocp.StepGeom.StepGeom_Direction | None, hasAxis2Placement3d_RefDirection: bool, aAxis2Placement3d_RefDirection: nanoocp.StepGeom.StepGeom_Direction | None, aSystemType: StepFEA_CoordinateSystemType, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def SystemType(self) -> StepFEA_CoordinateSystemType:
        """Returns field SystemType"""

    def SetSystemType(self, SystemType: StepFEA_CoordinateSystemType) -> None:
        """Set field SystemType"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaCurveSectionGeometricRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity FeaCurveSectionGeometricRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaCurveSectionGeometricRelationship) -> None: ...

    def Init(self, aSectionRef: nanoocp.StepElement.StepElement_CurveElementSectionDefinition | None, aItem: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def SectionRef(self) -> nanoocp.StepElement.StepElement_CurveElementSectionDefinition:
        """Returns field SectionRef"""

    def SetSectionRef(self, SectionRef: nanoocp.StepElement.StepElement_CurveElementSectionDefinition | None) -> None:
        """Set field SectionRef"""

    def Item(self) -> nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation:
        """Returns field Item"""

    def SetItem(self, Item: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None) -> None:
        """Set field Item"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor43d(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SymmetricTensor43d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor43d) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """return 0"""

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member CurveElementFreedomMember
        1 -> AnisotropicSymmetricTensor43d
        2 -> FeaIsotropicSymmetricTensor43d
        3 -> FeaIsoOrthotropicSymmetricTensor43d
        4 -> FeaTransverseIsotropicSymmetricTensor43d
        5 -> FeaColumnNormalisedOrthotropicSymmetricTensor43d
        6 -> FeaColumnNormalisedMonoclinicSymmetricTensor43d
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember: ...

    def AnisotropicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as AnisotropicSymmetricTensor43d (or Null if another type)
        """

    def FeaIsotropicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as FeaIsotropicSymmetricTensor43d (or Null if another type)
        """

    def FeaIsoOrthotropicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as FeaIsoOrthotropicSymmetricTensor43d (or Null if another type)
        """

    def FeaTransverseIsotropicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as FeaTransverseIsotropicSymmetricTensor43d (or Null if another type)
        """

    def FeaColumnNormalisedOrthotropicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as FeaColumnNormalisedOrthotropicSymmetricTensor43d (or Null if another type)
        """

    def FeaColumnNormalisedMonoclinicSymmetricTensor43d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as FeaColumnNormalisedMonoclinicSymmetricTensor43d (or Null if another type)
        """

class StepFEA_FeaLinearElasticity(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaLinearElasticity"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaLinearElasticity) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor43d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor43d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor43d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaMassDensity(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaMassDensity"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaMassDensity) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstant: float) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstant(self) -> float:
        """Returns field FeaConstant"""

    def SetFeaConstant(self, FeaConstant: float) -> None:
        """Set field FeaConstant"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaMaterialPropertyRepresentation(nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation):
    """Representation of STEP entity FeaMaterialPropertyRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaMaterialPropertyRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaModel(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity FeaModel"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaModel) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aCreatingSoftware: nanoocp.TCollection.TCollection_HAsciiString | None, aIntendedAnalysisCode: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString] | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aAnalysisType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CreatingSoftware(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field CreatingSoftware"""

    def SetCreatingSoftware(self, CreatingSoftware: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field CreatingSoftware"""

    def IntendedAnalysisCode(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString]:
        """Returns field IntendedAnalysisCode"""

    def SetIntendedAnalysisCode(self, IntendedAnalysisCode: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_AsciiString] | None) -> None:
        """Set field IntendedAnalysisCode"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def AnalysisType(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field AnalysisType"""

    def SetAnalysisType(self, AnalysisType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field AnalysisType"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaModel3d(StepFEA_FeaModel):
    """Representation of STEP entity FeaModel3d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaModel3d) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaModelDefinition(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity FeaModelDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaModelDefinition) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor23d(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SymmetricTensor23d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor23d) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SymmetricTensor23d select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member SymmetricTensor23dMember
        1 -> IsotropicSymmetricTensor23d
        2 -> OrthotropicSymmetricTensor23d
        3 -> AnisotropicSymmetricTensor23d
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type SymmetricTensor23dMember"""

    def SetIsotropicSymmetricTensor23d(self, aVal: float) -> None:
        """Set Value for IsotropicSymmetricTensor23d"""

    def IsotropicSymmetricTensor23d(self) -> float:
        """Returns Value as IsotropicSymmetricTensor23d (or Null if another type)"""

    def SetOrthotropicSymmetricTensor23d(self, aVal: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set Value for OrthotropicSymmetricTensor23d"""

    def OrthotropicSymmetricTensor23d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as OrthotropicSymmetricTensor23d (or Null if another type)
        """

    def SetAnisotropicSymmetricTensor23d(self, aVal: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set Value for AnisotropicSymmetricTensor23d"""

    def AnisotropicSymmetricTensor23d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as AnisotropicSymmetricTensor23d (or Null if another type)
        """

class StepFEA_FeaMoistureAbsorption(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaMoistureAbsorption"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaMoistureAbsorption) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor23d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor23d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaParametricPoint(nanoocp.StepGeom.StepGeom_Point):
    """Representation of STEP entity FeaParametricPoint"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaParametricPoint) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aCoordinates: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns field Coordinates"""

    def SetCoordinates(self, Coordinates: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set field Coordinates"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaSecantCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem):
    """
    Representation of STEP entity FeaSecantCoefficientOfLinearThermalExpansion
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaSecantCoefficientOfLinearThermalExpansion) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor23d, aReferenceTemperature: float) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor23d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None:
        """Set field FeaConstants"""

    def ReferenceTemperature(self) -> float:
        """Returns field ReferenceTemperature"""

    def SetReferenceTemperature(self, ReferenceTemperature: float) -> None:
        """Set field ReferenceTemperature"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor42d(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SymmetricTensor42d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor42d) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SymmetricTensor42d select type
        1 -> HArray1OfReal from TColStd
        0 else
        """

    def AnisotropicSymmetricTensor42d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as AnisotropicSymmetricTensor42d (or Null if another type)
        """

class StepFEA_FeaShellBendingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaShellBendingStiffness"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaShellBendingStiffness) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor42d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaShellMembraneBendingCouplingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaShellMembraneBendingCouplingStiffness"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaShellMembraneBendingCouplingStiffness) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor42d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaShellMembraneStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaShellMembraneStiffness"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaShellMembraneStiffness) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor42d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor22d(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SymmetricTensor22d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor22d) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SymmetricTensor22d select type
        1 -> HArray1OfReal from TColStd
        0 else
        """

    def AnisotropicSymmetricTensor22d(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """
        Returns Value as AnisotropicSymmetricTensor22d (or Null if another type)
        """

class StepFEA_FeaShellShearStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
    """Representation of STEP entity FeaShellShearStiffness"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaShellShearStiffness) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor22d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor22d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor22d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaSurfaceSectionGeometricRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity FeaSurfaceSectionGeometricRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaSurfaceSectionGeometricRelationship) -> None: ...

    def Init(self, aSectionRef: nanoocp.StepElement.StepElement_SurfaceSection | None, aItem: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def SectionRef(self) -> nanoocp.StepElement.StepElement_SurfaceSection:
        """Returns field SectionRef"""

    def SetSectionRef(self, SectionRef: nanoocp.StepElement.StepElement_SurfaceSection | None) -> None:
        """Set field SectionRef"""

    def Item(self) -> nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation:
        """Returns field Item"""

    def SetItem(self, Item: nanoocp.StepElement.StepElement_AnalysisItemWithinRepresentation | None) -> None:
        """Set field Item"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem):
    """
    Representation of STEP entity FeaTangentialCoefficientOfLinearThermalExpansion
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaConstants: StepFEA_SymmetricTensor23d) -> None:
        """Initialize all fields (own and inherited)"""

    def FeaConstants(self) -> StepFEA_SymmetricTensor23d:
        """Returns field FeaConstants"""

    def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None:
        """Set field FeaConstants"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FreedomAndCoefficient(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity FreedomAndCoefficient"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FreedomAndCoefficient) -> None: ...

    def Init(self, aFreedom: StepFEA_DegreeOfFreedom, aA: nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue) -> None:
        """Initialize all fields (own and inherited)"""

    def Freedom(self) -> StepFEA_DegreeOfFreedom:
        """Returns field Freedom"""

    def SetFreedom(self, Freedom: StepFEA_DegreeOfFreedom) -> None:
        """Set field Freedom"""

    def A(self) -> nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue:
        """Returns field A"""

    def SetA(self, A: nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field A"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_FreedomsList(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity FreedomsList"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_FreedomsList) -> None: ...

    def Init(self, aFreedoms: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_DegreeOfFreedom] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Freedoms(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_DegreeOfFreedom]:
        """Returns field Freedoms"""

    def SetFreedoms(self, Freedoms: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_DegreeOfFreedom] | None) -> None:
        """Set field Freedoms"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_GeometricNode(StepFEA_NodeRepresentation):
    """Representation of STEP entity GeometricNode"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_GeometricNode) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_Node(StepFEA_NodeRepresentation):
    """Representation of STEP entity Node"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_Node) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeDefinition(nanoocp.StepRepr.StepRepr_ShapeAspect):
    """Representation of STEP entity NodeDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeDefinition) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeGroup(StepFEA_FeaGroup):
    """Representation of STEP entity NodeGroup"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeGroup) -> None: ...

    def Init(self, aGroup_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aGroup_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aFeaGroup_ModelRef: StepFEA_FeaModel | None, aNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Nodes(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation]:
        """Returns field Nodes"""

    def SetNodes(self, Nodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Set field Nodes"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeSet(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    """Representation of STEP entity NodeSet"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeSet) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aNodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Nodes(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation]:
        """Returns field Nodes"""

    def SetNodes(self, Nodes: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None) -> None:
        """Set field Nodes"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeWithSolutionCoordinateSystem(StepFEA_Node):
    """Representation of STEP entity NodeWithSolutionCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeWithSolutionCoordinateSystem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_NodeWithVector(StepFEA_Node):
    """Representation of STEP entity NodeWithVector"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_NodeWithVector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ParametricCurve3dElementCoordinateDirection(StepFEA_FeaRepresentationItem):
    """
    Representation of STEP entity ParametricCurve3dElementCoordinateDirection
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aOrientation: nanoocp.StepGeom.StepGeom_Direction | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Orientation(self) -> nanoocp.StepGeom.StepGeom_Direction:
        """Returns field Orientation"""

    def SetOrientation(self, Orientation: nanoocp.StepGeom.StepGeom_Direction | None) -> None:
        """Set field Orientation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ParametricCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """Representation of STEP entity ParametricCurve3dElementCoordinateSystem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ParametricCurve3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aDirection: StepFEA_ParametricCurve3dElementCoordinateDirection | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Direction(self) -> StepFEA_ParametricCurve3dElementCoordinateDirection:
        """Returns field Direction"""

    def SetDirection(self, Direction: StepFEA_ParametricCurve3dElementCoordinateDirection | None) -> None:
        """Set field Direction"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_ParametricSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
    """
    Representation of STEP entity ParametricSurface3dElementCoordinateSystem
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_ParametricSurface3dElementCoordinateSystem) -> None: ...

    def Init(self, aRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aAxis: int, aAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def Axis(self) -> int:
        """Returns field Axis"""

    def SetAxis(self, Axis: int) -> None:
        """Set field Axis"""

    def Angle(self) -> float:
        """Returns field Angle"""

    def SetAngle(self, Angle: float) -> None:
        """Set field Angle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_Surface3dElementRepresentation(StepFEA_ElementRepresentation):
    """Representation of STEP entity Surface3dElementRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_Surface3dElementRepresentation) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aElementRepresentation_NodeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None, aModelRef: StepFEA_FeaModel3d | None, aElementDescriptor: nanoocp.StepElement.StepElement_Surface3dElementDescriptor | None, aProperty: nanoocp.StepElement.StepElement_SurfaceElementProperty | None, aMaterial: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModelRef(self) -> StepFEA_FeaModel3d:
        """Returns field ModelRef"""

    def SetModelRef(self, ModelRef: StepFEA_FeaModel3d | None) -> None:
        """Set field ModelRef"""

    def ElementDescriptor(self) -> nanoocp.StepElement.StepElement_Surface3dElementDescriptor:
        """Returns field ElementDescriptor"""

    def SetElementDescriptor(self, ElementDescriptor: nanoocp.StepElement.StepElement_Surface3dElementDescriptor | None) -> None:
        """Set field ElementDescriptor"""

    def Property(self) -> nanoocp.StepElement.StepElement_SurfaceElementProperty:
        """Returns field Property"""

    def SetProperty(self, Property: nanoocp.StepElement.StepElement_SurfaceElementProperty | None) -> None:
        """Set field Property"""

    def Material(self) -> nanoocp.StepElement.StepElement_ElementMaterial:
        """Returns field Material"""

    def SetMaterial(self, Material: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Set field Material"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor23dMember(nanoocp.StepData.StepData_SelectArrReal):
    """Representation of member for STEP SELECT type SymmetricTensor23d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor23dMember) -> None: ...

    def HasName(self) -> bool:
        """Returns True if has name"""

    def Name(self) -> str:
        """Returns set name"""

    def SetName(self, name: str) -> bool:
        """Set name"""

    def Matches(self, name: str) -> bool:
        """Tells if the name of a SelectMember matches a given one;"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_SymmetricTensor43dMember(nanoocp.StepData.StepData_SelectArrReal):
    """Representation of member for STEP SELECT type SymmetricTensor43d"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_SymmetricTensor43dMember) -> None: ...

    def HasName(self) -> bool:
        """Returns True if has name"""

    def Name(self) -> str:
        """Returns set name"""

    def SetName(self, name: str) -> bool:
        """Set name"""

    def Matches(self, name: str) -> bool:
        """Tells if the name of a SelectMember matches a given one;"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepFEA_Volume3dElementRepresentation(StepFEA_ElementRepresentation):
    """Representation of STEP entity Volume3dElementRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepFEA_Volume3dElementRepresentation) -> None: ...

    def Init(self, aRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, aRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, aElementRepresentation_NodeList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation] | None, aModelRef: StepFEA_FeaModel3d | None, aElementDescriptor: nanoocp.StepElement.StepElement_Volume3dElementDescriptor | None, aMaterial: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ModelRef(self) -> StepFEA_FeaModel3d:
        """Returns field ModelRef"""

    def SetModelRef(self, ModelRef: StepFEA_FeaModel3d | None) -> None:
        """Set field ModelRef"""

    def ElementDescriptor(self) -> nanoocp.StepElement.StepElement_Volume3dElementDescriptor:
        """Returns field ElementDescriptor"""

    def SetElementDescriptor(self, ElementDescriptor: nanoocp.StepElement.StepElement_Volume3dElementDescriptor | None) -> None:
        """Set field ElementDescriptor"""

    def Material(self) -> nanoocp.StepElement.StepElement_ElementMaterial:
        """Returns field Material"""

    def SetMaterial(self, Material: nanoocp.StepElement.StepElement_ElementMaterial | None) -> None:
        """Set field Material"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepFEA
StepFEA_Array1OfCurveElementEndOffset = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_CurveElementEndOffset]
StepFEA_Array1OfCurveElementEndRelease = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_CurveElementEndRelease]
StepFEA_Array1OfCurveElementInterval = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_CurveElementInterval]
StepFEA_Array1OfDegreeOfFreedom = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_DegreeOfFreedom]
StepFEA_Array1OfElementRepresentation = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_ElementRepresentation]
StepFEA_Array1OfNodeRepresentation = nanoocp.NCollection.NCollection_Array1[nanoocp.StepFEA.StepFEA_NodeRepresentation]
StepFEA_HArray1OfCurveElementEndOffset = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndOffset]
StepFEA_HArray1OfCurveElementEndRelease = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementEndRelease]
StepFEA_HArray1OfCurveElementInterval = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_CurveElementInterval]
StepFEA_HArray1OfDegreeOfFreedom = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_DegreeOfFreedom]
StepFEA_HArray1OfElementRepresentation = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_ElementRepresentation]
StepFEA_HArray1OfNodeRepresentation = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepFEA.StepFEA_NodeRepresentation]
StepFEA_HSequenceOfElementGeometricRelationship = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementGeometricRelationship]
StepFEA_HSequenceOfElementRepresentation = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepFEA.StepFEA_ElementRepresentation]
StepFEA_SequenceOfElementGeometricRelationship = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepFEA.StepFEA_ElementGeometricRelationship]
StepFEA_SequenceOfElementRepresentation = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepFEA.StepFEA_ElementRepresentation]
