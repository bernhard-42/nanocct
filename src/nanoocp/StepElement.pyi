"""OCCT package StepElement (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.StepRepr
import nanoocp.TCollection


class StepElement_ElementOrder(enum.IntEnum):
    StepElement_Linear = 0

    StepElement_Quadratic = 1

    StepElement_Cubic = 2

StepElement_Linear: StepElement_ElementOrder = StepElement_ElementOrder.StepElement_Linear

StepElement_Quadratic: StepElement_ElementOrder = StepElement_ElementOrder.StepElement_Quadratic

StepElement_Cubic: StepElement_ElementOrder = StepElement_ElementOrder.StepElement_Cubic

class StepElement_CurveEdge(enum.IntEnum):
    StepElement_ElementEdge = 0

StepElement_ElementEdge: StepElement_CurveEdge = StepElement_CurveEdge.StepElement_ElementEdge

class StepElement_EnumeratedCurveElementFreedom(enum.IntEnum):
    StepElement_XTranslation = 0

    StepElement_YTranslation = 1

    StepElement_ZTranslation = 2

    StepElement_XRotation = 3

    StepElement_YRotation = 4

    StepElement_ZRotation = 5

    StepElement_Warp = 6

    StepElement_None = 7

StepElement_XTranslation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_YTranslation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_ZTranslation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_XRotation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_YRotation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_ZRotation: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_Warp: StepElement_EnumeratedCurveElementFreedom = ...

StepElement_None: StepElement_EnumeratedCurveElementFreedom = ...

class StepElement_EnumeratedCurveElementPurpose(enum.IntEnum):
    StepElement_Axial = 0

    StepElement_YYBending = 1

    StepElement_ZZBending = 2

    StepElement_Torsion = 3

    StepElement_XYShear = 4

    StepElement_XZShear = 5

    StepElement_Warping = 6

StepElement_Axial: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_YYBending: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_ZZBending: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_Torsion: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_XYShear: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_XZShear: StepElement_EnumeratedCurveElementPurpose = ...

StepElement_Warping: StepElement_EnumeratedCurveElementPurpose = ...

class StepElement_UnspecifiedValue(enum.IntEnum):
    StepElement_Unspecified = 0

StepElement_Unspecified: StepElement_UnspecifiedValue = ...

class StepElement_Element2dShape(enum.IntEnum):
    StepElement_Quadrilateral = 0

    StepElement_Triangle = 1

StepElement_Quadrilateral: StepElement_Element2dShape = ...

StepElement_Triangle: StepElement_Element2dShape = StepElement_Element2dShape.StepElement_Triangle

class StepElement_ElementVolume(enum.IntEnum):
    StepElement_Volume = 0

StepElement_Volume: StepElement_ElementVolume = StepElement_ElementVolume.StepElement_Volume

class StepElement_EnumeratedSurfaceElementPurpose(enum.IntEnum):
    StepElement_MembraneDirect = 0

    StepElement_MembraneShear = 1

    StepElement_BendingDirect = 2

    StepElement_BendingTorsion = 3

    StepElement_NormalToPlaneShear = 4

StepElement_MembraneDirect: StepElement_EnumeratedSurfaceElementPurpose = ...

StepElement_MembraneShear: StepElement_EnumeratedSurfaceElementPurpose = ...

StepElement_BendingDirect: StepElement_EnumeratedSurfaceElementPurpose = ...

StepElement_BendingTorsion: StepElement_EnumeratedSurfaceElementPurpose = ...

StepElement_NormalToPlaneShear: StepElement_EnumeratedSurfaceElementPurpose = ...

class StepElement_EnumeratedVolumeElementPurpose(enum.IntEnum):
    StepElement_StressDisplacement = 0

StepElement_StressDisplacement: StepElement_EnumeratedVolumeElementPurpose = ...

class StepElement_Volume3dElementShape(enum.IntEnum):
    StepElement_Hexahedron = 0

    StepElement_Wedge = 1

    StepElement_Tetrahedron = 2

    StepElement_Pyramid = 3

StepElement_Hexahedron: StepElement_Volume3dElementShape = ...

StepElement_Wedge: StepElement_Volume3dElementShape = ...

StepElement_Tetrahedron: StepElement_Volume3dElementShape = ...

StepElement_Pyramid: StepElement_Volume3dElementShape = ...

class StepElement_AnalysisItemWithinRepresentation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity AnalysisItemWithinRepresentation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_AnalysisItemWithinRepresentation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aItem: nanoocp.StepRepr.StepRepr_RepresentationItem | None, aRep: nanoocp.StepRepr.StepRepr_Representation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Item(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """Returns field Item"""

    def SetItem(self, Item: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> None:
        """Set field Item"""

    def Rep(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """Returns field Rep"""

    def SetRep(self, Rep: nanoocp.StepRepr.StepRepr_Representation | None) -> None:
        """Set field Rep"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_CurveElementPurposeMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type CurveElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementPurposeMember) -> None: ...

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

class StepElement_ElementDescriptor(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ElementDescriptor"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_ElementDescriptor) -> None: ...

    def Init(self, aTopologyOrder: StepElement_ElementOrder, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def TopologyOrder(self) -> StepElement_ElementOrder:
        """Returns field TopologyOrder"""

    def SetTopologyOrder(self, TopologyOrder: StepElement_ElementOrder) -> None:
        """Set field TopologyOrder"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_Curve3dElementDescriptor(StepElement_ElementDescriptor):
    """Representation of STEP entity Curve3dElementDescriptor"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_Curve3dElementDescriptor) -> None: ...

    def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Purpose(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]]:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]] | None) -> None:
        """Set field Purpose"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_CurveElementFreedom(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type CurveElementFreedom"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementFreedom) -> None: ...

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

    def SetEnumeratedCurveElementFreedom(self, aVal: StepElement_EnumeratedCurveElementFreedom) -> None:
        """Set Value for EnumeratedCurveElementFreedom"""

    def EnumeratedCurveElementFreedom(self) -> StepElement_EnumeratedCurveElementFreedom:
        """
        Returns Value as EnumeratedCurveElementFreedom (or Null if another type)
        """

    def SetApplicationDefinedDegreeOfFreedom(self, aVal: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set Value for ApplicationDefinedDegreeOfFreedom"""

    def ApplicationDefinedDegreeOfFreedom(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Value as ApplicationDefinedDegreeOfFreedom (or Null if another type)
        """

class StepElement_CurveElementEndReleasePacket(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementEndReleasePacket"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementEndReleasePacket) -> None: ...

    def Init(self, aReleaseFreedom: StepElement_CurveElementFreedom, aReleaseStiffness: float) -> None:
        """Initialize all fields (own and inherited)"""

    def ReleaseFreedom(self) -> StepElement_CurveElementFreedom:
        """Returns field ReleaseFreedom"""

    def SetReleaseFreedom(self, ReleaseFreedom: StepElement_CurveElementFreedom) -> None:
        """Set field ReleaseFreedom"""

    def ReleaseStiffness(self) -> float:
        """Returns field ReleaseStiffness"""

    def SetReleaseStiffness(self, ReleaseStiffness: float) -> None:
        """Set field ReleaseStiffness"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_CurveElementFreedomMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type CurveElementFreedom"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementFreedomMember) -> None: ...

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

class StepElement_CurveElementPurpose(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type CurveElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementPurpose) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of CurveElementPurpose select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member CurveElementPurposeMember
        1 -> EnumeratedCurveElementPurpose
        2 -> ApplicationDefinedElementPurpose
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type CurveElementPurposeMember"""

    def SetEnumeratedCurveElementPurpose(self, aVal: StepElement_EnumeratedCurveElementPurpose) -> None:
        """Set Value for EnumeratedCurveElementPurpose"""

    def EnumeratedCurveElementPurpose(self) -> StepElement_EnumeratedCurveElementPurpose:
        """
        Returns Value as EnumeratedCurveElementPurpose (or Null if another type)
        """

    def SetApplicationDefinedElementPurpose(self, aVal: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set Value for ApplicationDefinedElementPurpose"""

    def ApplicationDefinedElementPurpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """

class StepElement_CurveElementSectionDefinition(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CurveElementSectionDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementSectionDefinition) -> None: ...

    def Init(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aSectionAngle: float) -> None:
        """Initialize all fields (own and inherited)"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def SectionAngle(self) -> float:
        """Returns field SectionAngle"""

    def SetSectionAngle(self, SectionAngle: float) -> None:
        """Set field SectionAngle"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_MeasureOrUnspecifiedValue(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type MeasureOrUnspecifiedValue"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_MeasureOrUnspecifiedValue) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of MeasureOrUnspecifiedValue select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member MeasureOrUnspecifiedValueMember
        1 -> ContextDependentMeasure
        2 -> UnspecifiedValue
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type MeasureOrUnspecifiedValueMember"""

    def SetContextDependentMeasure(self, aVal: float) -> None:
        """Set Value for ContextDependentMeasure"""

    def ContextDependentMeasure(self) -> float:
        """Returns Value as ContextDependentMeasure (or Null if another type)"""

    def SetUnspecifiedValue(self, aVal: StepElement_UnspecifiedValue) -> None:
        """Set Value for UnspecifiedValue"""

    def UnspecifiedValue(self) -> StepElement_UnspecifiedValue:
        """Returns Value as UnspecifiedValue (or Null if another type)"""

class StepElement_CurveElementSectionDerivedDefinitions(StepElement_CurveElementSectionDefinition):
    """Representation of STEP entity CurveElementSectionDerivedDefinitions"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_CurveElementSectionDerivedDefinitions) -> None: ...

    def Init(self, aCurveElementSectionDefinition_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aCurveElementSectionDefinition_SectionAngle: float, aCrossSectionalArea: float, aShearArea: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None, aSecondMomentOfArea: nanoocp.NCollection.NCollection_HArray1[float] | None, aTorsionalConstant: float, aWarpingConstant: StepElement_MeasureOrUnspecifiedValue, aLocationOfCentroid: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None, aLocationOfShearCentre: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None, aLocationOfNonStructuralMass: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None, aNonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aPolarMoment: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Initialize all fields (own and inherited)"""

    def CrossSectionalArea(self) -> float:
        """Returns field CrossSectionalArea"""

    def SetCrossSectionalArea(self, CrossSectionalArea: float) -> None:
        """Set field CrossSectionalArea"""

    def ShearArea(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]:
        """Returns field ShearArea"""

    def SetShearArea(self, ShearArea: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None) -> None:
        """Set field ShearArea"""

    def SecondMomentOfArea(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns field SecondMomentOfArea"""

    def SetSecondMomentOfArea(self, SecondMomentOfArea: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set field SecondMomentOfArea"""

    def TorsionalConstant(self) -> float:
        """Returns field TorsionalConstant"""

    def SetTorsionalConstant(self, TorsionalConstant: float) -> None:
        """Set field TorsionalConstant"""

    def WarpingConstant(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field WarpingConstant"""

    def SetWarpingConstant(self, WarpingConstant: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field WarpingConstant"""

    def LocationOfCentroid(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]:
        """Returns field LocationOfCentroid"""

    def SetLocationOfCentroid(self, LocationOfCentroid: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None) -> None:
        """Set field LocationOfCentroid"""

    def LocationOfShearCentre(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]:
        """Returns field LocationOfShearCentre"""

    def SetLocationOfShearCentre(self, LocationOfShearCentre: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None) -> None:
        """Set field LocationOfShearCentre"""

    def LocationOfNonStructuralMass(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]:
        """Returns field LocationOfNonStructuralMass"""

    def SetLocationOfNonStructuralMass(self, LocationOfNonStructuralMass: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue] | None) -> None:
        """Set field LocationOfNonStructuralMass"""

    def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field NonStructuralMass"""

    def SetNonStructuralMass(self, NonStructuralMass: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field NonStructuralMass"""

    def PolarMoment(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field PolarMoment"""

    def SetPolarMoment(self, PolarMoment: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field PolarMoment"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_ElementAspect(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ElementAspect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_ElementAspect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ElementAspect select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member ElementAspectMember
        1 -> ElementVolume
        2 -> Volume3dFace
        3 -> Volume2dFace
        4 -> Volume3dEdge
        5 -> Volume2dEdge
        6 -> Surface3dFace
        7 -> Surface2dFace
        8 -> Surface3dEdge
        9 -> Surface2dEdge
        10 -> CurveEdge
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type ElementAspectMember"""

    def SetElementVolume(self, aVal: StepElement_ElementVolume) -> None:
        """Set Value for ElementVolume"""

    def ElementVolume(self) -> StepElement_ElementVolume:
        """Returns Value as ElementVolume (or Null if another type)"""

    def SetVolume3dFace(self, aVal: int) -> None:
        """Set Value for Volume3dFace"""

    def Volume3dFace(self) -> int:
        """Returns Value as Volume3dFace (or Null if another type)"""

    def SetVolume2dFace(self, aVal: int) -> None:
        """Set Value for Volume2dFace"""

    def Volume2dFace(self) -> int:
        """Returns Value as Volume2dFace (or Null if another type)"""

    def SetVolume3dEdge(self, aVal: int) -> None:
        """Set Value for Volume3dEdge"""

    def Volume3dEdge(self) -> int:
        """Returns Value as Volume3dEdge (or Null if another type)"""

    def SetVolume2dEdge(self, aVal: int) -> None:
        """Set Value for Volume2dEdge"""

    def Volume2dEdge(self) -> int:
        """Returns Value as Volume2dEdge (or Null if another type)"""

    def SetSurface3dFace(self, aVal: int) -> None:
        """Set Value for Surface3dFace"""

    def Surface3dFace(self) -> int:
        """Returns Value as Surface3dFace (or Null if another type)"""

    def SetSurface2dFace(self, aVal: int) -> None:
        """Set Value for Surface2dFace"""

    def Surface2dFace(self) -> int:
        """Returns Value as Surface2dFace (or Null if another type)"""

    def SetSurface3dEdge(self, aVal: int) -> None:
        """Set Value for Surface3dEdge"""

    def Surface3dEdge(self) -> int:
        """Returns Value as Surface3dEdge (or Null if another type)"""

    def SetSurface2dEdge(self, aVal: int) -> None:
        """Set Value for Surface2dEdge"""

    def Surface2dEdge(self) -> int:
        """Returns Value as Surface2dEdge (or Null if another type)"""

    def SetCurveEdge(self, aVal: StepElement_CurveEdge) -> None:
        """Set Value for CurveEdge"""

    def CurveEdge(self) -> StepElement_CurveEdge:
        """Returns Value as CurveEdge (or Null if another type)"""

class StepElement_ElementAspectMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type ElementAspect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_ElementAspectMember) -> None: ...

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

class StepElement_ElementMaterial(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ElementMaterial"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_ElementMaterial) -> None: ...

    def Init(self, aMaterialId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aProperties: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def MaterialId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field MaterialId"""

    def SetMaterialId(self, MaterialId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field MaterialId"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Properties(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation]:
        """Returns field Properties"""

    def SetProperties(self, Properties: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_MaterialPropertyRepresentation] | None) -> None:
        """Set field Properties"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_MeasureOrUnspecifiedValueMember(nanoocp.StepData.StepData_SelectNamed):
    """
    Representation of member for STEP SELECT type MeasureOrUnspecifiedValue
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_MeasureOrUnspecifiedValueMember) -> None: ...

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

class StepElement_SurfaceElementPurposeMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type SurfaceElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceElementPurposeMember) -> None: ...

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

class StepElement_Surface3dElementDescriptor(StepElement_ElementDescriptor):
    """Representation of STEP entity Surface3dElementDescriptor"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_Surface3dElementDescriptor) -> None: ...

    def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]] | None, aShape: StepElement_Element2dShape) -> None:
        """Initialize all fields (own and inherited)"""

    def Purpose(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]]:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]] | None) -> None:
        """Set field Purpose"""

    def Shape(self) -> StepElement_Element2dShape:
        """Returns field Shape"""

    def SetShape(self, Shape: StepElement_Element2dShape) -> None:
        """Set field Shape"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_SurfaceElementProperty(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceElementProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceElementProperty) -> None: ...

    def Init(self, aPropertyId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aSection: StepElement_SurfaceSectionField | None) -> None:
        """Initialize all fields (own and inherited)"""

    def PropertyId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field PropertyId"""

    def SetPropertyId(self, PropertyId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field PropertyId"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def Section(self) -> StepElement_SurfaceSectionField:
        """Returns field Section"""

    def SetSection(self, Section: StepElement_SurfaceSectionField | None) -> None:
        """Set field Section"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_SurfaceElementPurpose(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SurfaceElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceElementPurpose) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SurfaceElementPurpose select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member SurfaceElementPurposeMember
        1 -> EnumeratedSurfaceElementPurpose
        2 -> ApplicationDefinedElementPurpose
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type SurfaceElementPurposeMember"""

    def SetEnumeratedSurfaceElementPurpose(self, aVal: StepElement_EnumeratedSurfaceElementPurpose) -> None:
        """Set Value for EnumeratedSurfaceElementPurpose"""

    def EnumeratedSurfaceElementPurpose(self) -> StepElement_EnumeratedSurfaceElementPurpose:
        """
        Returns Value as EnumeratedSurfaceElementPurpose (or Null if another type)
        """

    def SetApplicationDefinedElementPurpose(self, aVal: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set Value for ApplicationDefinedElementPurpose"""

    def ApplicationDefinedElementPurpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """

class StepElement_SurfaceSection(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceSection"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceSection) -> None: ...

    def Init(self, aOffset: StepElement_MeasureOrUnspecifiedValue, aNonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aNonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Initialize all fields (own and inherited)"""

    def Offset(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field Offset"""

    def SetOffset(self, Offset: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field Offset"""

    def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field NonStructuralMass"""

    def SetNonStructuralMass(self, NonStructuralMass: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field NonStructuralMass"""

    def NonStructuralMassOffset(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field NonStructuralMassOffset"""

    def SetNonStructuralMassOffset(self, NonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field NonStructuralMassOffset"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_SurfaceSectionField(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceSectionField"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceSectionField) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_SurfaceSectionFieldConstant(StepElement_SurfaceSectionField):
    """Representation of STEP entity SurfaceSectionFieldConstant"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceSectionFieldConstant) -> None: ...

    def Init(self, aDefinition: StepElement_SurfaceSection | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Definition(self) -> StepElement_SurfaceSection:
        """Returns field Definition"""

    def SetDefinition(self, Definition: StepElement_SurfaceSection | None) -> None:
        """Set field Definition"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_SurfaceSectionFieldVarying(StepElement_SurfaceSectionField):
    """Representation of STEP entity SurfaceSectionFieldVarying"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_SurfaceSectionFieldVarying) -> None: ...

    def Init(self, aDefinitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_SurfaceSection] | None, aAdditionalNodeValues: bool) -> None:
        """Initialize all fields (own and inherited)"""

    def Definitions(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_SurfaceSection]:
        """Returns field Definitions"""

    def SetDefinitions(self, Definitions: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_SurfaceSection] | None) -> None:
        """Set field Definitions"""

    def AdditionalNodeValues(self) -> bool:
        """Returns field AdditionalNodeValues"""

    def SetAdditionalNodeValues(self, AdditionalNodeValues: bool) -> None:
        """Set field AdditionalNodeValues"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_UniformSurfaceSection(StepElement_SurfaceSection):
    """Representation of STEP entity UniformSurfaceSection"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_UniformSurfaceSection) -> None: ...

    def Init(self, aSurfaceSection_Offset: StepElement_MeasureOrUnspecifiedValue, aSurfaceSection_NonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aSurfaceSection_NonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue, aThickness: float, aBendingThickness: StepElement_MeasureOrUnspecifiedValue, aShearThickness: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Initialize all fields (own and inherited)"""

    def Thickness(self) -> float:
        """Returns field Thickness"""

    def SetThickness(self, Thickness: float) -> None:
        """Set field Thickness"""

    def BendingThickness(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field BendingThickness"""

    def SetBendingThickness(self, BendingThickness: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field BendingThickness"""

    def ShearThickness(self) -> StepElement_MeasureOrUnspecifiedValue:
        """Returns field ShearThickness"""

    def SetShearThickness(self, ShearThickness: StepElement_MeasureOrUnspecifiedValue) -> None:
        """Set field ShearThickness"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_VolumeElementPurposeMember(nanoocp.StepData.StepData_SelectNamed):
    """Representation of member for STEP SELECT type VolumeElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_VolumeElementPurposeMember) -> None: ...

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

class StepElement_Volume3dElementDescriptor(StepElement_ElementDescriptor):
    """Representation of STEP entity Volume3dElementDescriptor"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_Volume3dElementDescriptor) -> None: ...

    def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_VolumeElementPurposeMember] | None, aShape: StepElement_Volume3dElementShape) -> None:
        """Initialize all fields (own and inherited)"""

    def Purpose(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_VolumeElementPurposeMember]:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_VolumeElementPurposeMember] | None) -> None:
        """Set field Purpose"""

    def Shape(self) -> StepElement_Volume3dElementShape:
        """Returns field Shape"""

    def SetShape(self, Shape: StepElement_Volume3dElementShape) -> None:
        """Set field Shape"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepElement_VolumeElementPurpose(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type VolumeElementPurpose"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepElement_VolumeElementPurpose) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of VolumeElementPurpose select type
        return 0
        """

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a items of select member VolumeElementPurposeMember
        1 -> EnumeratedVolumeElementPurpose
        2 -> ApplicationDefinedElementPurpose
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new select member the type VolumeElementPurposeMember"""

    def SetEnumeratedVolumeElementPurpose(self, aVal: StepElement_EnumeratedVolumeElementPurpose) -> None:
        """Set Value for EnumeratedVolumeElementPurpose"""

    def EnumeratedVolumeElementPurpose(self) -> StepElement_EnumeratedVolumeElementPurpose:
        """
        Returns Value as EnumeratedVolumeElementPurpose (or Null if another type)
        """

    def SetApplicationDefinedElementPurpose(self, aVal: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set Value for ApplicationDefinedElementPurpose"""

    def ApplicationDefinedElementPurpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns Value as ApplicationDefinedElementPurpose (or Null if another type)
        """

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepElement
StepElement_Array1OfCurveElementEndReleasePacket = nanoocp.NCollection.NCollection_Array1[nanoocp.StepElement.StepElement_CurveElementEndReleasePacket]
StepElement_Array1OfCurveElementSectionDefinition = nanoocp.NCollection.NCollection_Array1[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]
StepElement_Array1OfHSequenceOfCurveElementPurposeMember = nanoocp.NCollection.NCollection_Array1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]]
StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember = nanoocp.NCollection.NCollection_Array1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]]
StepElement_Array1OfMeasureOrUnspecifiedValue = nanoocp.NCollection.NCollection_Array1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]
StepElement_Array1OfSurfaceSection = nanoocp.NCollection.NCollection_Array1[nanoocp.StepElement.StepElement_SurfaceSection]
StepElement_Array1OfVolumeElementPurposeMember = nanoocp.NCollection.NCollection_Array1[nanoocp.StepElement.StepElement_VolumeElementPurposeMember]
StepElement_HArray1OfCurveElementEndReleasePacket = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementEndReleasePacket]
StepElement_HArray1OfCurveElementSectionDefinition = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]
StepElement_HArray1OfHSequenceOfCurveElementPurposeMember = nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]]
StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember = nanoocp.NCollection.NCollection_HArray1[nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]]
StepElement_HArray1OfMeasureOrUnspecifiedValue = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_MeasureOrUnspecifiedValue]
StepElement_HArray1OfSurfaceSection = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_SurfaceSection]
StepElement_HArray1OfVolumeElementPurposeMember = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepElement.StepElement_VolumeElementPurposeMember]
StepElement_HSequenceOfCurveElementPurposeMember = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]
StepElement_HSequenceOfCurveElementSectionDefinition = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]
StepElement_HSequenceOfElementMaterial = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_ElementMaterial]
StepElement_HSequenceOfSurfaceElementPurposeMember = nanoocp.NCollection.NCollection_HSequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]
StepElement_SequenceOfCurveElementPurposeMember = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepElement.StepElement_CurveElementPurposeMember]
StepElement_SequenceOfCurveElementSectionDefinition = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepElement.StepElement_CurveElementSectionDefinition]
StepElement_SequenceOfElementMaterial = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepElement.StepElement_ElementMaterial]
StepElement_SequenceOfSurfaceElementPurposeMember = nanoocp.NCollection.NCollection_Sequence[nanoocp.StepElement.StepElement_SurfaceElementPurposeMember]
