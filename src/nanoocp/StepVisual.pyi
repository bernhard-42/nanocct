"""OCCT package StepVisual (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepData
import nanoocp.StepGeom
import nanoocp.StepRepr
import nanoocp.StepShape
import nanoocp.TCollection


class StepVisual_CentralOrParallel(enum.IntEnum):
    StepVisual_copCentral = 0

    StepVisual_copParallel = 1

StepVisual_copCentral: StepVisual_CentralOrParallel = ...

StepVisual_copParallel: StepVisual_CentralOrParallel = ...

class StepVisual_MarkerType(enum.IntEnum):
    StepVisual_mtDot = 0

    StepVisual_mtX = 1

    StepVisual_mtPlus = 2

    StepVisual_mtAsterisk = 3

    StepVisual_mtRing = 4

    StepVisual_mtSquare = 5

    StepVisual_mtTriangle = 6

StepVisual_mtDot: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtDot

StepVisual_mtX: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtX

StepVisual_mtPlus: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtPlus

StepVisual_mtAsterisk: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtAsterisk

StepVisual_mtRing: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtRing

StepVisual_mtSquare: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtSquare

StepVisual_mtTriangle: StepVisual_MarkerType = StepVisual_MarkerType.StepVisual_mtTriangle

class StepVisual_NullStyle(enum.IntEnum):
    StepVisual_Null = 0

StepVisual_Null: StepVisual_NullStyle = StepVisual_NullStyle.StepVisual_Null

class StepVisual_ShadingSurfaceMethod(enum.IntEnum):
    StepVisual_ssmConstantShading = 0

    StepVisual_ssmColourShading = 1

    StepVisual_ssmDotShading = 2

    StepVisual_ssmNormalShading = 3

StepVisual_ssmConstantShading: StepVisual_ShadingSurfaceMethod = ...

StepVisual_ssmColourShading: StepVisual_ShadingSurfaceMethod = ...

StepVisual_ssmDotShading: StepVisual_ShadingSurfaceMethod = ...

StepVisual_ssmNormalShading: StepVisual_ShadingSurfaceMethod = ...

class StepVisual_SurfaceSide(enum.IntEnum):
    StepVisual_ssNegative = 0

    StepVisual_ssPositive = 1

    StepVisual_ssBoth = 2

StepVisual_ssNegative: StepVisual_SurfaceSide = StepVisual_SurfaceSide.StepVisual_ssNegative

StepVisual_ssPositive: StepVisual_SurfaceSide = StepVisual_SurfaceSide.StepVisual_ssPositive

StepVisual_ssBoth: StepVisual_SurfaceSide = StepVisual_SurfaceSide.StepVisual_ssBoth

class StepVisual_TextPath(enum.IntEnum):
    StepVisual_tpUp = 0

    StepVisual_tpRight = 1

    StepVisual_tpDown = 2

    StepVisual_tpLeft = 3

StepVisual_tpUp: StepVisual_TextPath = StepVisual_TextPath.StepVisual_tpUp

StepVisual_tpRight: StepVisual_TextPath = StepVisual_TextPath.StepVisual_tpRight

StepVisual_tpDown: StepVisual_TextPath = StepVisual_TextPath.StepVisual_tpDown

StepVisual_tpLeft: StepVisual_TextPath = StepVisual_TextPath.StepVisual_tpLeft

class StepVisual_PresentationStyleSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationStyleSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationStyleSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a PresentationStyleSelect Kind Entity that is :
        1 -> PointStyle
        2 -> CurveStyle
        3 -> SurfaceStyleUsage
        4 -> SymbolStyle
        5 -> FillAreaStyle
        6 -> TextStyle
        7 -> NullStyle
        0 else
        """

    def PointStyle(self) -> StepVisual_PointStyle:
        """returns Value as a PointStyle (Null if another type)"""

    def CurveStyle(self) -> StepVisual_CurveStyle:
        """returns Value as a CurveStyle (Null if another type)"""

    def NullStyle(self) -> StepVisual_NullStyleMember:
        """returns Value as a NullStyleMember (Null if another type)"""

    def SurfaceStyleUsage(self) -> StepVisual_SurfaceStyleUsage:
        """returns Value as a SurfaceStyleUsage (Null if another type)"""

class StepVisual_PresentationStyleAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationStyleAssignment"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationStyleAssignment) -> None: ...

    def Init(self, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect] | None) -> None: ...

    def SetStyles(self, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect] | None) -> None: ...

    def Styles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect]: ...

    def StylesValue(self, num: int) -> StepVisual_PresentationStyleSelect: ...

    def NbStyles(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_StyledItemTarget(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a StyledItemTarget select type"""

    @overload
    def __init__(self, theOther: StepVisual_StyledItemTarget) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a StyledItemTarget Kind Entity that is :
        1 -> GeometricRepresentationItem
        2 -> MappedItem
        3 -> Representation
        4 -> TopologicalRepresentationItem
        0 else
        """

    def GeometricRepresentationItem(self) -> nanoocp.StepGeom.StepGeom_GeometricRepresentationItem:
        """returns Value as a GeometricRepresentationItem (Null if another type)"""

    def MappedItem(self) -> nanoocp.StepRepr.StepRepr_MappedItem:
        """returns Value as a MappedItem (Null if another type)"""

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def TopologicalRepresentationItem(self) -> nanoocp.StepShape.StepShape_TopologicalRepresentationItem:
        """
        returns Value as a TopologicalRepresentationItem (Null if another type)
        """

class StepVisual_StyledItem(nanoocp.StepRepr.StepRepr_RepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a StyledItem"""

    @overload
    def __init__(self, theOther: StepVisual_StyledItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None, aItem: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetStyles(self, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None) -> None: ...

    def Styles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment]: ...

    def StylesValue(self, num: int) -> StepVisual_PresentationStyleAssignment: ...

    def NbStyles(self) -> int: ...

    @overload
    def SetItem(self, aItem: nanoocp.StepRepr.StepRepr_RepresentationItem | None) -> None: ...

    @overload
    def SetItem(self, aItem: StepVisual_StyledItemTarget) -> None: ...

    def Item(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem: ...

    def ItemAP242(self) -> StepVisual_StyledItemTarget: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationOccurrence(StepVisual_StyledItem):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationCurveOccurrence(StepVisual_AnnotationOccurrence):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationCurveOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationCurveOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationCurveOccurrenceAndGeomReprItem(StepVisual_AnnotationCurveOccurrence):
    """
    Added for Dimensional Tolerances
    Complex STEP entity AnnotationCurveOccurrence & AnnotationOccurrence &
    GeometricRepresentationItem & RepresentationItem & StyledItem
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_AnnotationCurveOccurrenceAndGeomReprItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationFillArea(nanoocp.StepShape.StepShape_GeometricCurveSet):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationFillArea"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationFillArea) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationFillAreaOccurrence(StepVisual_AnnotationOccurrence):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationFillAreaOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationFillAreaOccurrence) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None, theItem: nanoocp.Standard.Standard_Transient | None, theFillStyleTarget: nanoocp.StepGeom.StepGeom_GeometricRepresentationItem | None) -> None:
        """Initialize all fields (own and inherited)"""

    def FillStyleTarget(self) -> nanoocp.StepGeom.StepGeom_GeometricRepresentationItem:
        """Returns field fill_style_target"""

    def SetFillStyleTarget(self, theTarget: nanoocp.StepGeom.StepGeom_GeometricRepresentationItem | None) -> None:
        """Set field fill_style_target"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationPlaneElement(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationPlaneElement select type"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationPlaneElement) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a IdAttributeSelect Kind Entity that is :
        1 -> DraughtingCallout
        2 -> StyledItem
        0 else
        """

    def DraughtingCallout(self) -> StepVisual_DraughtingCallout:
        """returns Value as a DraughtingCallout (Null if another type)"""

    def StyledItem(self) -> StepVisual_StyledItem:
        """returns Value as a StyledItem (Null if another type)"""

class StepVisual_AnnotationPlane(StepVisual_AnnotationOccurrence):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationPlane"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationPlane) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None, theItem: nanoocp.Standard.Standard_Transient | None, theElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_AnnotationPlaneElement] | None) -> None: ...

    def Elements(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_AnnotationPlaneElement]:
        """Returns field Elements"""

    def SetElements(self, theElements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_AnnotationPlaneElement] | None) -> None:
        """Set field Elements"""

    def NbElements(self) -> int:
        """Returns number of Elements"""

    def ElementsValue(self, theNum: int) -> StepVisual_AnnotationPlaneElement:
        """Returns Elements with the given number"""

    def SetElementsValue(self, theNum: int, theItem: StepVisual_AnnotationPlaneElement) -> None:
        """Sets Elements with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationText(nanoocp.StepRepr.StepRepr_MappedItem):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationText"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationText) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AnnotationTextOccurrence(StepVisual_AnnotationOccurrence):
    @overload
    def __init__(self) -> None:
        """Returns a AnnotationTextOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_AnnotationTextOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AreaInSet(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a AreaInSet"""

    @overload
    def __init__(self, theOther: StepVisual_AreaInSet) -> None: ...

    def Init(self, aArea: StepVisual_PresentationArea | None, aInSet: StepVisual_PresentationSet | None) -> None: ...

    def SetArea(self, aArea: StepVisual_PresentationArea | None) -> None: ...

    def Area(self) -> StepVisual_PresentationArea: ...

    def SetInSet(self, aInSet: StepVisual_PresentationSet | None) -> None: ...

    def InSet(self) -> StepVisual_PresentationSet: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_AreaOrView(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a AreaOrView SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_AreaOrView) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a AreaOrView Kind Entity that is :
        1 -> PresentationArea
        2 -> PresentationView
        0 else
        """

    def PresentationArea(self) -> StepVisual_PresentationArea:
        """returns Value as a PresentationArea (Null if another type)"""

    def PresentationView(self) -> StepVisual_PresentationView:
        """returns Value as a PresentationView (Null if another type)"""

class StepVisual_Colour(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Colour"""

    @overload
    def __init__(self, theOther: StepVisual_Colour) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_BackgroundColour(StepVisual_Colour):
    @overload
    def __init__(self) -> None:
        """Returns a BackgroundColour"""

    @overload
    def __init__(self, theOther: StepVisual_BackgroundColour) -> None: ...

    def Init(self, aPresentation: StepVisual_AreaOrView) -> None: ...

    def SetPresentation(self, aPresentation: StepVisual_AreaOrView) -> None: ...

    def Presentation(self) -> StepVisual_AreaOrView: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_BoxCharacteristicSelect:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_BoxCharacteristicSelect) -> None: ...

    def TypeOfContent(self) -> int: ...

    def SetTypeOfContent(self, aType: int) -> None: ...

    def RealValue(self) -> float: ...

    def SetRealValue(self, aValue: float) -> None: ...

class StepVisual_CameraImage(nanoocp.StepRepr.StepRepr_MappedItem):
    @overload
    def __init__(self) -> None:
        """Returns a CameraImage"""

    @overload
    def __init__(self, theOther: StepVisual_CameraImage) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraImage2dWithScale(StepVisual_CameraImage):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_CameraImage2dWithScale) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraImage3dWithScale(StepVisual_CameraImage):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_CameraImage3dWithScale) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModel(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModel"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModel) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModelD2(StepVisual_CameraModel):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModelD2"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD2) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aViewWindow: StepVisual_PlanarBox | None, aViewWindowClipping: bool) -> None: ...

    def SetViewWindow(self, aViewWindow: StepVisual_PlanarBox | None) -> None: ...

    def ViewWindow(self) -> StepVisual_PlanarBox: ...

    def SetViewWindowClipping(self, aViewWindowClipping: bool) -> None: ...

    def ViewWindowClipping(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModelD3(StepVisual_CameraModel):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModelD3"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aViewReferenceSystem: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, aPerspectiveOfVolume: StepVisual_ViewVolume | None) -> None: ...

    def SetViewReferenceSystem(self, aViewReferenceSystem: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None: ...

    def ViewReferenceSystem(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d: ...

    def SetPerspectiveOfVolume(self, aPerspectiveOfVolume: StepVisual_ViewVolume | None) -> None: ...

    def PerspectiveOfVolume(self) -> StepVisual_ViewVolume: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModelD3MultiClippingInterectionSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModelD3MultiClippingInterectionSelect select type"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3MultiClippingInterectionSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a IdAttributeSelect Kind Entity that is :
        1 -> Plane
        2 -> CameraModelD3MultiClippingUnion
        0 else
        """

    def Plane(self) -> nanoocp.StepGeom.StepGeom_Plane:
        """returns Value as a Plane (Null if another type)"""

    def CameraModelD3MultiClippingUnion(self) -> StepVisual_CameraModelD3MultiClippingUnion:
        """
        returns Value as a CameraModelD3MultiClippingUnion (Null if another type)
        """

class StepVisual_CameraModelD3MultiClipping(StepVisual_CameraModelD3):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModelD3MultiClipping"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3MultiClipping) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theViewReferenceSystem: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None, thePerspectiveOfVolume: StepVisual_ViewVolume | None, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect] | None) -> None: ...

    def SetShapeClipping(self, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect] | None) -> None: ...

    def ShapeClipping(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModelD3MultiClippingIntersection(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a StepVisual_CameraModelD3MultiClippingIntersection"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3MultiClippingIntersection) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect] | None) -> None: ...

    def SetShapeClipping(self, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect] | None) -> None: ...

    def ShapeClipping(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraModelD3MultiClippingUnionSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a CameraModelD3MultiClippingUnionSelect select type"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3MultiClippingUnionSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a IdAttributeSelect Kind Entity that is :
        1 -> Plane
        2 -> CameraModelD3MultiClippingIntersection
        0 else
        """

    def Plane(self) -> nanoocp.StepGeom.StepGeom_Plane:
        """returns Value as a Plane (Null if another type)"""

    def CameraModelD3MultiClippingIntersection(self) -> StepVisual_CameraModelD3MultiClippingIntersection:
        """
        returns Value as a CameraModelD3MultiClippingIntersection (Null if another type)
        """

class StepVisual_CameraModelD3MultiClippingUnion(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a StepVisual_CameraModelD3MultiClippingUnion"""

    @overload
    def __init__(self, theOther: StepVisual_CameraModelD3MultiClippingUnion) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingUnionSelect] | None) -> None: ...

    def SetShapeClipping(self, theShapeClipping: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingUnionSelect] | None) -> None: ...

    def ShapeClipping(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingUnionSelect]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CameraUsage(nanoocp.StepRepr.StepRepr_RepresentationMap):
    @overload
    def __init__(self) -> None:
        """Returns a CameraUsage"""

    @overload
    def __init__(self, theOther: StepVisual_CameraUsage) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_DraughtingModel(nanoocp.StepRepr.StepRepr_Representation):
    """Representation of STEP entity DraughtingModel"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingModel) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel(StepVisual_DraughtingModel):
    """
    Added for Dimensional Tolerances
    Complex STEP entity Characterized_Object & Characterized_Representation & Draughting_Model &
    Representation
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ColourSpecification(StepVisual_Colour):
    @overload
    def __init__(self) -> None:
        """Returns a ColourSpecification"""

    @overload
    def __init__(self, theOther: StepVisual_ColourSpecification) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ColourRgb(StepVisual_ColourSpecification):
    @overload
    def __init__(self) -> None:
        """Returns a ColourRgb"""

    @overload
    def __init__(self, theOther: StepVisual_ColourRgb) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aRed: float, aGreen: float, aBlue: float) -> None: ...

    def SetRed(self, aRed: float) -> None: ...

    def Red(self) -> float: ...

    def SetGreen(self, aGreen: float) -> None: ...

    def Green(self) -> float: ...

    def SetBlue(self, aBlue: float) -> None: ...

    def Blue(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TextOrCharacter(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a TextOrCharacter SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_TextOrCharacter) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a TextOrCharacter Kind Entity that is :
        1 -> AnnotationText
        2 -> CompositeText
        3 -> TextLiteral
        0 else
        """

    def AnnotationText(self) -> StepVisual_AnnotationText:
        """returns Value as a AnnotationText (Null if another type)"""

    def CompositeText(self) -> StepVisual_CompositeText:
        """returns Value as a CompositeText (Null if another type)"""

    def TextLiteral(self) -> StepVisual_TextLiteral:
        """returns Value as a TextLiteral (Null if another type)"""

class StepVisual_CompositeText(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a CompositeText"""

    @overload
    def __init__(self, theOther: StepVisual_CompositeText) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCollectedText: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TextOrCharacter] | None) -> None: ...

    def SetCollectedText(self, aCollectedText: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TextOrCharacter] | None) -> None: ...

    def CollectedText(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TextOrCharacter]: ...

    def CollectedTextValue(self, num: int) -> StepVisual_TextOrCharacter: ...

    def NbCollectedText(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CompositeTextWithExtent(StepVisual_CompositeText):
    @overload
    def __init__(self) -> None:
        """Returns a CompositeTextWithExtent"""

    @overload
    def __init__(self, theOther: StepVisual_CompositeTextWithExtent) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCollectedText: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TextOrCharacter] | None, aExtent: StepVisual_PlanarExtent | None) -> None: ...

    def SetExtent(self, aExtent: StepVisual_PlanarExtent | None) -> None: ...

    def Extent(self) -> StepVisual_PlanarExtent: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_InvisibilityContext(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a InvisibilityContext SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_InvisibilityContext) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a InvisibilityContext Kind Entity that is :
        1 -> PresentationRepresentation
        2 -> PresentationSet
        2 -> DraughtingModel
        0 else
        """

    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation:
        """returns Value as a PresentationRepresentation (Null if another type)"""

    def PresentationSet(self) -> StepVisual_PresentationSet:
        """returns Value as a PresentationSet (Null if another type)"""

    def DraughtingModel(self) -> StepVisual_DraughtingModel:
        """returns Value as a PresentationSet (Null if another type)"""

class StepVisual_InvisibleItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a InvisibleItem SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_InvisibleItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a InvisibleItem Kind Entity that is :
        1 -> StyledItem
        2 -> PresentationLayerAssignment
        3 -> PresentationRepresentation
        0 else
        """

    def StyledItem(self) -> StepVisual_StyledItem:
        """returns Value as a StyledItem (Null if another type)"""

    def PresentationLayerAssignment(self) -> StepVisual_PresentationLayerAssignment:
        """returns Value as a PresentationLayerAssignment (Null if another type)"""

    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation:
        """returns Value as a PresentationRepresentation (Null if another type)"""

class StepVisual_Invisibility(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Invisibility"""

    @overload
    def __init__(self, theOther: StepVisual_Invisibility) -> None: ...

    def Init(self, aInvisibleItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_InvisibleItem] | None) -> None: ...

    def SetInvisibleItems(self, aInvisibleItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_InvisibleItem] | None) -> None: ...

    def InvisibleItems(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_InvisibleItem]: ...

    def InvisibleItemsValue(self, num: int) -> StepVisual_InvisibleItem: ...

    def NbInvisibleItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ContextDependentInvisibility(StepVisual_Invisibility):
    @overload
    def __init__(self) -> None:
        """Returns a ContextDependentInvisibility"""

    @overload
    def __init__(self, theOther: StepVisual_ContextDependentInvisibility) -> None: ...

    def Init(self, aInvisibleItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_InvisibleItem] | None, aPresentationContext: StepVisual_InvisibilityContext) -> None: ...

    def SetPresentationContext(self, aPresentationContext: StepVisual_InvisibilityContext) -> None: ...

    def PresentationContext(self) -> StepVisual_InvisibilityContext: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_StyleContextSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a StyleContextSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_StyleContextSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a StyleContextSelect Kind Entity that is :
        1 -> Representation
        2 -> RepresentationItem
        3 -> PresentationSet
        0 else
        """

    def Representation(self) -> nanoocp.StepRepr.StepRepr_Representation:
        """returns Value as a Representation (Null if another type)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """returns Value as a RepresentationItem (Null if another type)"""

    def PresentationSet(self) -> StepVisual_PresentationSet:
        """returns Value as a PresentationSet (Null if another type)"""

class StepVisual_OverRidingStyledItem(StepVisual_StyledItem):
    @overload
    def __init__(self) -> None:
        """Returns a OverRidingStyledItem"""

    @overload
    def __init__(self, theOther: StepVisual_OverRidingStyledItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None, aItem: nanoocp.Standard.Standard_Transient | None, aOverRiddenStyle: StepVisual_StyledItem | None) -> None: ...

    def SetOverRiddenStyle(self, aOverRiddenStyle: StepVisual_StyledItem | None) -> None: ...

    def OverRiddenStyle(self) -> StepVisual_StyledItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ContextDependentOverRidingStyledItem(StepVisual_OverRidingStyledItem):
    @overload
    def __init__(self) -> None:
        """Returns a ContextDependentOverRidingStyledItem"""

    @overload
    def __init__(self, theOther: StepVisual_ContextDependentOverRidingStyledItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment] | None, aItem: nanoocp.Standard.Standard_Transient | None, aOverRiddenStyle: StepVisual_StyledItem | None, aStyleContext: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_StyleContextSelect] | None) -> None: ...

    def SetStyleContext(self, aStyleContext: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_StyleContextSelect] | None) -> None: ...

    def StyleContext(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_StyleContextSelect]: ...

    def StyleContextValue(self, num: int) -> StepVisual_StyleContextSelect: ...

    def NbStyleContext(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CurveStyleFontSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a CurveStyleFontSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_CurveStyleFontSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a CurveStyleFontSelect Kind Entity that is :
        1 -> CurveStyleFont
        2 -> PreDefinedCurveFont
        3 -> ExternallyDefinedCurveFont
        0 else
        """

    def CurveStyleFont(self) -> StepVisual_CurveStyleFont:
        """returns Value as a CurveStyleFont (Null if another type)"""

    def PreDefinedCurveFont(self) -> StepVisual_PreDefinedCurveFont:
        """returns Value as a PreDefinedCurveFont (Null if another type)"""

    def ExternallyDefinedCurveFont(self) -> StepVisual_ExternallyDefinedCurveFont:
        """returns Value as a ExternallyDefinedCurveFont (Null if another type)"""

class StepVisual_CurveStyle(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a CurveStyle"""

    @overload
    def __init__(self, theOther: StepVisual_CurveStyle) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCurveFont: StepVisual_CurveStyleFontSelect, aCurveWidth: nanoocp.StepBasic.StepBasic_SizeSelect, aCurveColour: StepVisual_Colour | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetCurveFont(self, aCurveFont: StepVisual_CurveStyleFontSelect) -> None: ...

    def CurveFont(self) -> StepVisual_CurveStyleFontSelect: ...

    def SetCurveWidth(self, aCurveWidth: nanoocp.StepBasic.StepBasic_SizeSelect) -> None: ...

    def CurveWidth(self) -> nanoocp.StepBasic.StepBasic_SizeSelect: ...

    def SetCurveColour(self, aCurveColour: StepVisual_Colour | None) -> None: ...

    def CurveColour(self) -> StepVisual_Colour: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CurveStyleFontPattern(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a CurveStyleFontPattern"""

    @overload
    def __init__(self, theOther: StepVisual_CurveStyleFontPattern) -> None: ...

    def Init(self, aVisibleSegmentLength: float, aInvisibleSegmentLength: float) -> None: ...

    def SetVisibleSegmentLength(self, aVisibleSegmentLength: float) -> None: ...

    def VisibleSegmentLength(self) -> float: ...

    def SetInvisibleSegmentLength(self, aInvisibleSegmentLength: float) -> None: ...

    def InvisibleSegmentLength(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CurveStyleFont(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a CurveStyleFont"""

    @overload
    def __init__(self, theOther: StepVisual_CurveStyleFont) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPatternList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CurveStyleFontPattern] | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPatternList(self, aPatternList: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CurveStyleFontPattern] | None) -> None: ...

    def PatternList(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CurveStyleFontPattern]: ...

    def PatternListValue(self, num: int) -> StepVisual_CurveStyleFontPattern: ...

    def NbPatternList(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_DirectionCountSelect:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_DirectionCountSelect) -> None: ...

    def SetTypeOfContent(self, aTypeOfContent: int) -> None: ...

    def TypeOfContent(self) -> int: ...

    def UDirectionCount(self) -> int: ...

    def SetUDirectionCount(self, aUDirectionCount: int) -> None: ...

    def VDirectionCount(self) -> int: ...

    def SetVDirectionCount(self, aUDirectionCount: int) -> None: ...

class StepVisual_DraughtingAnnotationOccurrence(StepVisual_AnnotationOccurrence):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingAnnotationOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingAnnotationOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_DraughtingCalloutElement(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingCalloutElement select type"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingCalloutElement) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a IdAttributeSelect Kind Entity that is :
        1 -> AnnotationCurveOccurrence
        2 -> AnnotationTextOccurrence
        3 -> TessellatedAnnotationOccurrence
        4 -> AnnotationFillAreaOccurrence
        0 else
        """

    def AnnotationCurveOccurrence(self) -> StepVisual_AnnotationCurveOccurrence:
        """returns Value as a AnnotationCurveOccurrence (Null if another type)"""

    def AnnotationTextOccurrence(self) -> StepVisual_AnnotationTextOccurrence:
        """returns Value as a AnnotationTextOccurrence"""

    def TessellatedAnnotationOccurrence(self) -> StepVisual_TessellatedAnnotationOccurrence:
        """returns Value as a TessellatedAnnotationOccurrence"""

    def AnnotationFillAreaOccurrence(self) -> StepVisual_AnnotationFillAreaOccurrence:
        """returns Value as a AnnotationFillAreaOccurrence"""

class StepVisual_DraughtingCallout(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingCallout"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingCallout) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theContents: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DraughtingCalloutElement] | None) -> None:
        """Init"""

    def Contents(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DraughtingCalloutElement]:
        """Returns field Contents"""

    def SetContents(self, theContents: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DraughtingCalloutElement] | None) -> None:
        """Set field Contents"""

    def NbContents(self) -> int:
        """Returns number of Contents"""

    def ContentsValue(self, theNum: int) -> StepVisual_DraughtingCalloutElement:
        """Returns Contents with the given number"""

    def SetContentsValue(self, theNum: int, theItem: StepVisual_DraughtingCalloutElement) -> None:
        """Sets Contents with given number"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PreDefinedColour(StepVisual_Colour):
    @overload
    def __init__(self) -> None:
        """Returns a PreDefinedColour"""

    @overload
    def __init__(self, theOther: StepVisual_PreDefinedColour) -> None: ...

    def SetPreDefinedItem(self, item: StepVisual_PreDefinedItem | None) -> None:
        """set a pre_defined_item part"""

    def GetPreDefinedItem(self) -> StepVisual_PreDefinedItem:
        """return a pre_defined_item part"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_DraughtingPreDefinedColour(StepVisual_PreDefinedColour):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingPreDefinedColour"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingPreDefinedColour) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PreDefinedItem(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PreDefinedItem"""

    @overload
    def __init__(self, theOther: StepVisual_PreDefinedItem) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PreDefinedCurveFont(StepVisual_PreDefinedItem):
    @overload
    def __init__(self) -> None:
        """Returns a PreDefinedCurveFont"""

    @overload
    def __init__(self, theOther: StepVisual_PreDefinedCurveFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_DraughtingPreDefinedCurveFont(StepVisual_PreDefinedCurveFont):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingPreDefinedCurveFont"""

    @overload
    def __init__(self, theOther: StepVisual_DraughtingPreDefinedCurveFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ExternallyDefinedCurveFont(nanoocp.StepBasic.StepBasic_ExternallyDefinedItem):
    """Representation of STEP entity ExternallyDefinedCurveFont"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_ExternallyDefinedCurveFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ExternallyDefinedTextFont(nanoocp.StepBasic.StepBasic_ExternallyDefinedItem):
    """Representation of STEP entity ExternallyDefinedTextFont"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_ExternallyDefinedTextFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_FillStyleSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a FillStyleSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_FillStyleSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a FillStyleSelect Kind Entity that is :
        1 -> FillAreaStyleColour
        2 -> ExternallyDefinedTileStyle
        3 -> FillAreaStyleTiles
        4 -> ExternallyDefinedHatchStyle
        5 -> FillAreaStyleHatching
        0 else
        """

    def FillAreaStyleColour(self) -> StepVisual_FillAreaStyleColour:
        """returns Value as a FillAreaStyleColour (Null if another type)"""

class StepVisual_FillAreaStyle(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a FillAreaStyle"""

    @overload
    def __init__(self, theOther: StepVisual_FillAreaStyle) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFillStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_FillStyleSelect] | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFillStyles(self, aFillStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_FillStyleSelect] | None) -> None: ...

    def FillStyles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_FillStyleSelect]: ...

    def FillStylesValue(self, num: int) -> StepVisual_FillStyleSelect: ...

    def NbFillStyles(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_FillAreaStyleColour(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a FillAreaStyleColour"""

    @overload
    def __init__(self, theOther: StepVisual_FillAreaStyleColour) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFillColour: StepVisual_Colour | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFillColour(self, aFillColour: StepVisual_Colour | None) -> None: ...

    def FillColour(self) -> StepVisual_Colour: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_FontSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a FontSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_FontSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a FontSelect Kind Entity that is :
        1 -> PreDefinedTextFont
        2 -> ExternallyDefinedTextFont
        0 else
        """

    def PreDefinedTextFont(self) -> StepVisual_PreDefinedTextFont:
        """returns Value as a PreDefinedTextFont (Null if another type)"""

    def ExternallyDefinedTextFont(self) -> StepVisual_ExternallyDefinedTextFont:
        """returns Value as a ExternallyDefinedTextFont (Null if another type)"""

class StepVisual_LayeredItem(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a LayeredItem SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_LayeredItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a LayeredItem Kind Entity that is :
        1 -> PresentationRepresentation
        2 -> RepresentationItem
        0 else
        """

    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation:
        """returns Value as a PresentationRepresentation (Null if another type)"""

    def RepresentationItem(self) -> nanoocp.StepRepr.StepRepr_RepresentationItem:
        """returns Value as a RepresentationItem (Null if another type)"""

class StepVisual_MarkerMember(nanoocp.StepData.StepData_SelectInt):
    """
    Defines MarkerType as unique member of MarkerSelect
    Works with an EnumTool
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_MarkerMember) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, name: str) -> bool: ...

    def EnumText(self) -> str: ...

    def SetEnumText(self, val: int, text: str) -> None: ...

    def SetValue(self, val: StepVisual_MarkerType) -> None: ...

    def Value(self) -> StepVisual_MarkerType: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_MarkerSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a MarkerSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_MarkerSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a MarkerSelect Kind Entity that is :
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a new MarkerMember"""

    def CaseMem(self, sm: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """Returns 1 for a SelectMember enum, named MARKER_TYPE"""

    def MarkerMember(self) -> StepVisual_MarkerMember:
        """Gives access to the MarkerMember in order to get/set its value"""

class StepVisual_PresentationRepresentation(nanoocp.StepRepr.StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationRepresentation"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationArea(StepVisual_PresentationRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationArea"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationArea) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_MechanicalDesignGeometricPresentationArea(StepVisual_PresentationArea):
    @overload
    def __init__(self) -> None:
        """Returns a MechanicalDesignGeometricPresentationArea"""

    @overload
    def __init__(self, theOther: StepVisual_MechanicalDesignGeometricPresentationArea) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_MechanicalDesignGeometricPresentationRepresentation(StepVisual_PresentationRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a MechanicalDesignGeometricPresentationRepresentation"""

    @overload
    def __init__(self, theOther: StepVisual_MechanicalDesignGeometricPresentationRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_NullStyleMember(nanoocp.StepData.StepData_SelectInt):
    """
    Defines NullStyle as unique member of PresentationStyleSelect
    Works with an EnumTool
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_NullStyleMember) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, arg0: str) -> bool: ...

    def Kind(self) -> int: ...

    def EnumText(self) -> str: ...

    def SetEnumText(self, theValue: int, theText: str) -> None: ...

    def SetValue(self, theValue: StepVisual_NullStyle) -> None: ...

    def Value(self) -> StepVisual_NullStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PlanarExtent(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a PlanarExtent"""

    @overload
    def __init__(self, theOther: StepVisual_PlanarExtent) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSizeInX: float, aSizeInY: float) -> None: ...

    def SetSizeInX(self, aSizeInX: float) -> None: ...

    def SizeInX(self) -> float: ...

    def SetSizeInY(self, aSizeInY: float) -> None: ...

    def SizeInY(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PlanarBox(StepVisual_PlanarExtent):
    @overload
    def __init__(self) -> None:
        """Returns a PlanarBox"""

    @overload
    def __init__(self, theOther: StepVisual_PlanarBox) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aSizeInX: float, aSizeInY: float, aPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement) -> None: ...

    def SetPlacement(self, aPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement) -> None: ...

    def Placement(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PointStyle(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PointStyle"""

    @overload
    def __init__(self, theOther: StepVisual_PointStyle) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aMarker: StepVisual_MarkerSelect, aMarkerSize: nanoocp.StepBasic.StepBasic_SizeSelect, aMarkerColour: StepVisual_Colour | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetMarker(self, aMarker: StepVisual_MarkerSelect) -> None: ...

    def Marker(self) -> StepVisual_MarkerSelect: ...

    def SetMarkerSize(self, aMarkerSize: nanoocp.StepBasic.StepBasic_SizeSelect) -> None: ...

    def MarkerSize(self) -> nanoocp.StepBasic.StepBasic_SizeSelect: ...

    def SetMarkerColour(self, aMarkerColour: StepVisual_Colour | None) -> None: ...

    def MarkerColour(self) -> StepVisual_Colour: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PreDefinedTextFont(StepVisual_PreDefinedItem):
    @overload
    def __init__(self) -> None:
        """Returns a PreDefinedTextFont"""

    @overload
    def __init__(self, theOther: StepVisual_PreDefinedTextFont) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationLayerAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationLayerAssignment"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationLayerAssignment) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aAssignedItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_LayeredItem] | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetAssignedItems(self, aAssignedItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_LayeredItem] | None) -> None: ...

    def AssignedItems(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_LayeredItem]: ...

    def AssignedItemsValue(self, num: int) -> StepVisual_LayeredItem: ...

    def NbAssignedItems(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationLayerUsage(nanoocp.Standard.Standard_Transient):
    """Added from StepVisual Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_PresentationLayerUsage) -> None: ...

    def Init(self, aAssignment: StepVisual_PresentationLayerAssignment | None, aPresentation: StepVisual_PresentationRepresentation | None) -> None: ...

    def SetAssignment(self, aAssignment: StepVisual_PresentationLayerAssignment | None) -> None: ...

    def Assignment(self) -> StepVisual_PresentationLayerAssignment: ...

    def SetPresentation(self, aPresentation: StepVisual_PresentationRepresentation | None) -> None: ...

    def Presentation(self) -> StepVisual_PresentationRepresentation: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationRepresentationSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationRepresentationSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationRepresentationSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a PresentationRepresentationSelect Kind Entity that is :
        1 -> PresentationRepresentation
        2 -> PresentationSet
        0 else
        """

    def PresentationRepresentation(self) -> StepVisual_PresentationRepresentation:
        """returns Value as a PresentationRepresentation (Null if another type)"""

    def PresentationSet(self) -> StepVisual_PresentationSet:
        """returns Value as a PresentationSet (Null if another type)"""

class StepVisual_PresentationSet(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationSet"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationSizeAssignmentSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationSizeAssignmentSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationSizeAssignmentSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a PresentationSizeAssignmentSelect Kind Entity that is :
        1 -> PresentationView
        2 -> PresentationArea
        3 -> AreaInSet
        0 else
        """

    def PresentationView(self) -> StepVisual_PresentationView:
        """returns Value as a PresentationView (Null if another type)"""

    def PresentationArea(self) -> StepVisual_PresentationArea:
        """returns Value as a PresentationArea (Null if another type)"""

    def AreaInSet(self) -> StepVisual_AreaInSet:
        """returns Value as a AreaInSet (Null if another type)"""

class StepVisual_PresentationSize(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationSize"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationSize) -> None: ...

    def Init(self, aUnit: StepVisual_PresentationSizeAssignmentSelect, aSize: StepVisual_PlanarBox | None) -> None: ...

    def SetUnit(self, aUnit: StepVisual_PresentationSizeAssignmentSelect) -> None: ...

    def Unit(self) -> StepVisual_PresentationSizeAssignmentSelect: ...

    def SetSize(self, aSize: StepVisual_PlanarBox | None) -> None: ...

    def Size(self) -> StepVisual_PlanarBox: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationStyleByContext(StepVisual_PresentationStyleAssignment):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationStyleByContext"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationStyleByContext) -> None: ...

    def Init(self, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect] | None, aStyleContext: StepVisual_StyleContextSelect) -> None: ...

    def SetStyleContext(self, aStyleContext: StepVisual_StyleContextSelect) -> None: ...

    def StyleContext(self) -> StepVisual_StyleContextSelect: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentationView(StepVisual_PresentationRepresentation):
    @overload
    def __init__(self) -> None:
        """Returns a PresentationView"""

    @overload
    def __init__(self, theOther: StepVisual_PresentationView) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentedItem(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_PresentedItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PresentedItemRepresentation(nanoocp.Standard.Standard_Transient):
    """Added from StepVisual Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepVisual_PresentedItemRepresentation) -> None: ...

    def Init(self, aPresentation: StepVisual_PresentationRepresentationSelect, aItem: StepVisual_PresentedItem | None) -> None: ...

    def SetPresentation(self, aPresentation: StepVisual_PresentationRepresentationSelect) -> None: ...

    def Presentation(self) -> StepVisual_PresentationRepresentationSelect: ...

    def SetItem(self, aItem: StepVisual_PresentedItem | None) -> None: ...

    def Item(self) -> StepVisual_PresentedItem: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_RenderingPropertiesSelect(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type RenderingPropertiesSelect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_RenderingPropertiesSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of RenderingPropertiesSelect select type
        -- 1 -> SurfaceStyleReflectanceAmbient
        -- 2 -> SurfaceStyleTransparent
        """

    def SurfaceStyleReflectanceAmbient(self) -> StepVisual_SurfaceStyleReflectanceAmbient:
        """
        Returns Value as SurfaceStyleReflectanceAmbient (or Null if another type)
        """

    def SurfaceStyleTransparent(self) -> StepVisual_SurfaceStyleTransparent:
        """Returns Value as SurfaceStyleTransparent (or Null if another type)"""

class StepVisual_TessellatedItem(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingCalloutElement select type"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedGeometricSet(StepVisual_TessellatedItem):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingCalloutElement select type"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedGeometricSet) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: "NCollection_Handle<NCollection_Array1<opencascade::handle<StepVisual_TessellatedItem>>>") -> None: ...

    def Items(self) -> "NCollection_Handle<NCollection_Array1<opencascade::handle<StepVisual_TessellatedItem>>>": ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_RepositionedTessellatedGeometricSet(StepVisual_TessellatedGeometricSet):
    """
    Representation of complex STEP entity RepositionedTessellatedGeometricSet
    """

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_RepositionedTessellatedGeometricSet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: "NCollection_Handle<NCollection_Array1<opencascade::handle<StepVisual_TessellatedItem>>>", theLocation: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Location(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns location"""

    def SetLocation(self, theLocation: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Sets location"""

class StepVisual_RepositionedTessellatedItem(StepVisual_TessellatedItem):
    """Representation of STEP entity RepositionedTessellatedItem"""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_RepositionedTessellatedItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theLocation: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Location(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement3d:
        """Returns location"""

    def SetLocation(self, theLocation: nanoocp.StepGeom.StepGeom_Axis2Placement3d | None) -> None:
        """Sets location"""

class StepVisual_SurfaceStyleElementSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleElementSelect SelectType"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleElementSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a SurfaceStyleElementSelect Kind Entity that is :
        1 -> SurfaceStyleFillArea
        2 -> SurfaceStyleBoundary
        3 -> SurfaceStyleParameterLine
        4 -> SurfaceStyleSilhouette
        5 -> SurfaceStyleSegmentationCurve
        6 -> SurfaceStyleControlGrid
        7 -> SurfaceStyleRendering
        0 else
        """

    def SurfaceStyleFillArea(self) -> StepVisual_SurfaceStyleFillArea:
        """returns Value as a SurfaceStyleFillArea (Null if another type)"""

    def SurfaceStyleBoundary(self) -> StepVisual_SurfaceStyleBoundary:
        """returns Value as a SurfaceStyleBoundary (Null if another type)"""

    def SurfaceStyleParameterLine(self) -> StepVisual_SurfaceStyleParameterLine:
        """returns Value as a SurfaceStyleParameterLine (Null if another type)"""

    def SurfaceStyleRendering(self) -> StepVisual_SurfaceStyleRendering:
        """returns Value as a SurfaceStyleRendering (Null if another type)"""

class StepVisual_SurfaceSideStyle(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceSideStyle"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceSideStyle) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_SurfaceStyleElementSelect] | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetStyles(self, aStyles: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_SurfaceStyleElementSelect] | None) -> None: ...

    def Styles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_SurfaceStyleElementSelect]: ...

    def StylesValue(self, num: int) -> StepVisual_SurfaceStyleElementSelect: ...

    def NbStyles(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleBoundary(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleBoundary"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleBoundary) -> None: ...

    def Init(self, aStyleOfBoundary: StepVisual_CurveStyle | None) -> None: ...

    def SetStyleOfBoundary(self, aStyleOfBoundary: StepVisual_CurveStyle | None) -> None: ...

    def StyleOfBoundary(self) -> StepVisual_CurveStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleControlGrid(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleControlGrid"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleControlGrid) -> None: ...

    def Init(self, aStyleOfControlGrid: StepVisual_CurveStyle | None) -> None: ...

    def SetStyleOfControlGrid(self, aStyleOfControlGrid: StepVisual_CurveStyle | None) -> None: ...

    def StyleOfControlGrid(self) -> StepVisual_CurveStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleFillArea(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleFillArea"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleFillArea) -> None: ...

    def Init(self, aFillArea: StepVisual_FillAreaStyle | None) -> None: ...

    def SetFillArea(self, aFillArea: StepVisual_FillAreaStyle | None) -> None: ...

    def FillArea(self) -> StepVisual_FillAreaStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleParameterLine(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleParameterLine"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleParameterLine) -> None: ...

    def Init(self, aStyleOfParameterLines: StepVisual_CurveStyle | None, aDirectionCounts: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DirectionCountSelect] | None) -> None: ...

    def SetStyleOfParameterLines(self, aStyleOfParameterLines: StepVisual_CurveStyle | None) -> None: ...

    def StyleOfParameterLines(self) -> StepVisual_CurveStyle: ...

    def SetDirectionCounts(self, aDirectionCounts: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DirectionCountSelect] | None) -> None: ...

    def DirectionCounts(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DirectionCountSelect]: ...

    def DirectionCountsValue(self, num: int) -> StepVisual_DirectionCountSelect: ...

    def NbDirectionCounts(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleReflectanceAmbient(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceStyleReflectanceAmbient"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleReflectanceAmbient) -> None: ...

    def Init(self, theAmbientReflectance: float) -> None:
        """Initialize all fields (own and inherited)"""

    def AmbientReflectance(self) -> float:
        """Returns field AmbientReflectance"""

    def SetAmbientReflectance(self, theAmbientReflectance: float) -> None:
        """Sets field AmbientReflectance"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleReflectanceAmbientDiffuse(StepVisual_SurfaceStyleReflectanceAmbient):
    """Representation of STEP entity SurfaceStyleReflectanceAmbientDiffuse"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleReflectanceAmbientDiffuse) -> None: ...

    def Init(self, theAmbientReflectance: float, theDiffuseReflectance: float) -> None:
        """Initialize all fields (own and inherited)"""

    def DiffuseReflectance(self) -> float:
        """Returns field DiffuseReflectance"""

    def SetDiffuseReflectance(self, theDiffuseReflectance: float) -> None:
        """Sets field DiffuseReflectance"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleReflectanceAmbientDiffuseSpecular(StepVisual_SurfaceStyleReflectanceAmbientDiffuse):
    """
    Representation of STEP entity SurfaceStyleReflectanceAmbientDiffuseSpecular
    """

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleReflectanceAmbientDiffuseSpecular) -> None: ...

    def Init(self, theAmbientReflectance: float, theDiffuseReflectance: float, theSpecularReflectance: float, theSpecularExponent: float, theSpecularColour: StepVisual_Colour | None) -> None:
        """Initialize all fields (own and inherited)"""

    def SpecularReflectance(self) -> float:
        """Returns field SpecularReflectance"""

    def SetSpecularReflectance(self, theSpecularReflectance: float) -> None:
        """Sets field SpecularReflectance"""

    def SpecularExponent(self) -> float:
        """Returns field SpecularExponent"""

    def SetSpecularExponent(self, theSpecularExponent: float) -> None:
        """Sets field SpecularExponent"""

    def SpecularColour(self) -> StepVisual_Colour:
        """Returns field SpecularColour"""

    def SetSpecularColour(self, theSpecularColour: StepVisual_Colour | None) -> None:
        """Sets field SpecularColour"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleRendering(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceStyleRendering"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleRendering) -> None: ...

    def Init(self, theRenderingMethod: StepVisual_ShadingSurfaceMethod, theSurfaceColour: StepVisual_Colour | None) -> None:
        """Initialize all fields (own and inherited)"""

    def RenderingMethod(self) -> StepVisual_ShadingSurfaceMethod:
        """Returns field RenderingMethod"""

    def SetRenderingMethod(self, theRenderingMethod: StepVisual_ShadingSurfaceMethod) -> None:
        """Sets field RenderingMethod"""

    def SurfaceColour(self) -> StepVisual_Colour:
        """Returns field SurfaceColour"""

    def SetSurfaceColour(self, theSurfaceColour: StepVisual_Colour | None) -> None:
        """Sets field SurfaceColour"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleRenderingWithProperties(StepVisual_SurfaceStyleRendering):
    """Representation of STEP entity SurfaceStyleRenderingWithProperties"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleRenderingWithProperties) -> None: ...

    def Init(self, theSurfaceStyleRendering_RenderingMethod: StepVisual_ShadingSurfaceMethod, theSurfaceStyleRendering_SurfaceColour: StepVisual_Colour | None, theProperties: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_RenderingPropertiesSelect] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Properties(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_RenderingPropertiesSelect]:
        """Returns field Properties"""

    def SetProperties(self, theProperties: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_RenderingPropertiesSelect] | None) -> None:
        """Sets field Properties"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleSegmentationCurve(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleSegmentationCurve"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleSegmentationCurve) -> None: ...

    def Init(self, aStyleOfSegmentationCurve: StepVisual_CurveStyle | None) -> None: ...

    def SetStyleOfSegmentationCurve(self, aStyleOfSegmentationCurve: StepVisual_CurveStyle | None) -> None: ...

    def StyleOfSegmentationCurve(self) -> StepVisual_CurveStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleSilhouette(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleSilhouette"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleSilhouette) -> None: ...

    def Init(self, aStyleOfSilhouette: StepVisual_CurveStyle | None) -> None: ...

    def SetStyleOfSilhouette(self, aStyleOfSilhouette: StepVisual_CurveStyle | None) -> None: ...

    def StyleOfSilhouette(self) -> StepVisual_CurveStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleTransparent(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity SurfaceStyleTransparent"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleTransparent) -> None: ...

    def Init(self, theTransparency: float) -> None:
        """Initialize all fields (own and inherited)"""

    def Transparency(self) -> float:
        """Returns field Transparency"""

    def SetTransparency(self, theTransparency: float) -> None:
        """Sets field Transparency"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_SurfaceStyleUsage(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SurfaceStyleUsage"""

    @overload
    def __init__(self, theOther: StepVisual_SurfaceStyleUsage) -> None: ...

    def Init(self, aSide: StepVisual_SurfaceSide, aStyle: StepVisual_SurfaceSideStyle | None) -> None: ...

    def SetSide(self, aSide: StepVisual_SurfaceSide) -> None: ...

    def Side(self) -> StepVisual_SurfaceSide: ...

    def SetStyle(self, aStyle: StepVisual_SurfaceSideStyle | None) -> None: ...

    def Style(self) -> StepVisual_SurfaceSideStyle: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_Template(nanoocp.StepRepr.StepRepr_Representation):
    @overload
    def __init__(self) -> None:
        """Returns a Template"""

    @overload
    def __init__(self, theOther: StepVisual_Template) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TemplateInstance(nanoocp.StepRepr.StepRepr_MappedItem):
    @overload
    def __init__(self) -> None:
        """Returns a TemplateInstance"""

    @overload
    def __init__(self, theOther: StepVisual_TemplateInstance) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TextLiteral(nanoocp.StepGeom.StepGeom_GeometricRepresentationItem):
    @overload
    def __init__(self) -> None:
        """Returns a TextLiteral"""

    @overload
    def __init__(self, theOther: StepVisual_TextLiteral) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aLiteral: nanoocp.TCollection.TCollection_HAsciiString | None, aPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement, aAlignment: nanoocp.TCollection.TCollection_HAsciiString | None, aPath: StepVisual_TextPath, aFont: StepVisual_FontSelect) -> None: ...

    def SetLiteral(self, aLiteral: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Literal(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPlacement(self, aPlacement: nanoocp.StepGeom.StepGeom_Axis2Placement) -> None: ...

    def Placement(self) -> nanoocp.StepGeom.StepGeom_Axis2Placement: ...

    def SetAlignment(self, aAlignment: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Alignment(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPath(self, aPath: StepVisual_TextPath) -> None: ...

    def Path(self) -> StepVisual_TextPath: ...

    def SetFont(self, aFont: StepVisual_FontSelect) -> None: ...

    def Font(self) -> StepVisual_FontSelect: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TextStyle(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a TextStyle"""

    @overload
    def __init__(self, theOther: StepVisual_TextStyle) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCharacterAppearance: StepVisual_TextStyleForDefinedFont | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetCharacterAppearance(self, aCharacterAppearance: StepVisual_TextStyleForDefinedFont | None) -> None: ...

    def CharacterAppearance(self) -> StepVisual_TextStyleForDefinedFont: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TextStyleForDefinedFont(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a TextStyleForDefinedFont"""

    @overload
    def __init__(self, theOther: StepVisual_TextStyleForDefinedFont) -> None: ...

    def Init(self, aTextColour: StepVisual_Colour | None) -> None: ...

    def SetTextColour(self, aTextColour: StepVisual_Colour | None) -> None: ...

    def TextColour(self) -> StepVisual_Colour: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TextStyleWithBoxCharacteristics(StepVisual_TextStyle):
    @overload
    def __init__(self) -> None:
        """Returns a TextStyleWithBoxCharacteristics"""

    @overload
    def __init__(self, theOther: StepVisual_TextStyleWithBoxCharacteristics) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aCharacterAppearance: StepVisual_TextStyleForDefinedFont | None, aCharacteristics: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_BoxCharacteristicSelect] | None) -> None: ...

    def SetCharacteristics(self, aCharacteristics: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_BoxCharacteristicSelect] | None) -> None: ...

    def Characteristics(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_BoxCharacteristicSelect]: ...

    def CharacteristicsValue(self, num: int) -> StepVisual_BoxCharacteristicSelect: ...

    def NbCharacteristics(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ViewVolume(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ViewVolume"""

    @overload
    def __init__(self, theOther: StepVisual_ViewVolume) -> None: ...

    def Init(self, aProjectionType: StepVisual_CentralOrParallel, aProjectionPoint: nanoocp.StepGeom.StepGeom_CartesianPoint | None, aViewPlaneDistance: float, aFrontPlaneDistance: float, aFrontPlaneClipping: bool, aBackPlaneDistance: float, aBackPlaneClipping: bool, aViewVolumeSidesClipping: bool, aViewWindow: StepVisual_PlanarBox | None) -> None: ...

    def SetProjectionType(self, aProjectionType: StepVisual_CentralOrParallel) -> None: ...

    def ProjectionType(self) -> StepVisual_CentralOrParallel: ...

    def SetProjectionPoint(self, aProjectionPoint: nanoocp.StepGeom.StepGeom_CartesianPoint | None) -> None: ...

    def ProjectionPoint(self) -> nanoocp.StepGeom.StepGeom_CartesianPoint: ...

    def SetViewPlaneDistance(self, aViewPlaneDistance: float) -> None: ...

    def ViewPlaneDistance(self) -> float: ...

    def SetFrontPlaneDistance(self, aFrontPlaneDistance: float) -> None: ...

    def FrontPlaneDistance(self) -> float: ...

    def SetFrontPlaneClipping(self, aFrontPlaneClipping: bool) -> None: ...

    def FrontPlaneClipping(self) -> bool: ...

    def SetBackPlaneDistance(self, aBackPlaneDistance: float) -> None: ...

    def BackPlaneDistance(self) -> float: ...

    def SetBackPlaneClipping(self, aBackPlaneClipping: bool) -> None: ...

    def BackPlaneClipping(self) -> bool: ...

    def SetViewVolumeSidesClipping(self, aViewVolumeSidesClipping: bool) -> None: ...

    def ViewVolumeSidesClipping(self) -> bool: ...

    def SetViewWindow(self, aViewWindow: StepVisual_PlanarBox | None) -> None: ...

    def ViewWindow(self) -> StepVisual_PlanarBox: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedAnnotationOccurrence(StepVisual_StyledItem):
    @overload
    def __init__(self) -> None:
        """Returns a TesselatedAnnotationOccurrence"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedAnnotationOccurrence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CoordinatesList(StepVisual_TessellatedItem):
    @overload
    def __init__(self) -> None:
        """Returns a coordinate list"""

    @overload
    def __init__(self, theOther: StepVisual_CoordinatesList) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, thePoints: nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ] | None) -> None: ...

    def Points(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.gp.gp_XYZ]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedCurveSet(StepVisual_TessellatedItem):
    @overload
    def __init__(self) -> None:
        """Returns a DraughtingCalloutElement select type"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedCurveSet) -> None: ...

    def Init(self, theName: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordList: StepVisual_CoordinatesList | None, theCurves: "NCollection_Handle<NCollection_DynamicArray<opencascade::handle<NCollection_HSequence<int>>>>") -> None: ...

    def CoordList(self) -> StepVisual_CoordinatesList: ...

    def Curves(self) -> "NCollection_Handle<NCollection_DynamicArray<opencascade::handle<NCollection_HSequence<int>>>>": ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedStructuredItem(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedStructuredItem"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedStructuredItem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_FaceOrSurface(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type FaceOrSurface"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_FaceOrSurface) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of FaceOrSurface select type
        -- 1 -> Face
        -- 2 -> Surface
        """

    def Face(self) -> nanoocp.StepShape.StepShape_Face:
        """Returns Value as Face (or Null if another type)"""

    def Surface(self) -> nanoocp.StepGeom.StepGeom_Surface:
        """Returns Value as Surface (or Null if another type)"""

class StepVisual_TessellatedFace(StepVisual_TessellatedStructuredItem):
    """Representation of STEP entity TessellatedFace"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedFace) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordinates: StepVisual_CoordinatesList | None, thePnmax: int, theNormals: nanoocp.NCollection.NCollection_HArray2[float] | None, theHasGeometricLink: bool, theGeometricLink: StepVisual_FaceOrSurface) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> StepVisual_CoordinatesList:
        """Returns field Coordinates"""

    def SetCoordinates(self, theCoordinates: StepVisual_CoordinatesList | None) -> None:
        """Sets field Coordinates"""

    def Pnmax(self) -> int:
        """Returns field Pnmax"""

    def SetPnmax(self, thePnmax: int) -> None:
        """Sets field Pnmax"""

    def Normals(self) -> nanoocp.NCollection.NCollection_HArray2[float]:
        """Returns field Normals"""

    def SetNormals(self, theNormals: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """Sets field Normals"""

    def NbNormals(self) -> int:
        """Returns number of Normals"""

    def GeometricLink(self) -> StepVisual_FaceOrSurface:
        """Returns field GeometricLink"""

    def SetGeometricLink(self, theGeometricLink: StepVisual_FaceOrSurface) -> None:
        """Sets field GeometricLink"""

    def HasGeometricLink(self) -> bool:
        """Returns True if optional field GeometricLink is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ComplexTriangulatedFace(StepVisual_TessellatedFace):
    """Representation of STEP entity ComplexTriangulatedFace"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_ComplexTriangulatedFace) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedFace_Coordinates: StepVisual_CoordinatesList | None, theTessellatedFace_Pnmax: int, theTessellatedFace_Normals: nanoocp.NCollection.NCollection_HArray2[float] | None, theHasTessellatedFace_GeometricLink: bool, theTessellatedFace_GeometricLink: StepVisual_FaceOrSurface, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None, theTriangleStrips: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None, theTriangleFans: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Pnindex(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field Pnindex"""

    def SetPnindex(self, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field Pnindex"""

    def NbPnindex(self) -> int:
        """Returns number of Pnindex"""

    def PnindexValue(self, theNum: int) -> int:
        """Returns value of Pnindex by its num"""

    def TriangleStrips(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient]:
        """Returns field TriangleStrips"""

    def SetTriangleStrips(self, theTriangleStrips: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Sets field TriangleStrips"""

    def NbTriangleStrips(self) -> int:
        """Returns number of TriangleStrips"""

    def TriangleFans(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient]:
        """Returns field TriangleFans"""

    def SetTriangleFans(self, theTriangleFans: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Sets field TriangleFans"""

    def NbTriangleFans(self) -> int:
        """Returns number of TriangleFans"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedSurfaceSet(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedSurfaceSet"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedSurfaceSet) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordinates: StepVisual_CoordinatesList | None, thePnmax: int, theNormals: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> StepVisual_CoordinatesList:
        """Returns field Coordinates"""

    def SetCoordinates(self, theCoordinates: StepVisual_CoordinatesList | None) -> None:
        """Sets field Coordinates"""

    def Pnmax(self) -> int:
        """Returns field Pnmax"""

    def SetPnmax(self, thePnmax: int) -> None:
        """Sets field Pnmax"""

    def Normals(self) -> nanoocp.NCollection.NCollection_HArray2[float]:
        """Returns field Normals"""

    def SetNormals(self, theNormals: nanoocp.NCollection.NCollection_HArray2[float] | None) -> None:
        """Sets field Normals"""

    def NbNormals(self) -> int:
        """Returns number of Normals"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_ComplexTriangulatedSurfaceSet(StepVisual_TessellatedSurfaceSet):
    """Representation of STEP entity ComplexTriangulatedSurfaceSet"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_ComplexTriangulatedSurfaceSet) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedSurfaceSet_Coordinates: StepVisual_CoordinatesList | None, theTessellatedSurfaceSet_Pnmax: int, theTessellatedSurfaceSet_Normals: nanoocp.NCollection.NCollection_HArray2[float] | None, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None, theTriangleStrips: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None, theTriangleFans: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Pnindex(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field Pnindex"""

    def SetPnindex(self, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field Pnindex"""

    def NbPnindex(self) -> int:
        """Returns number of Pnindex"""

    def PnindexValue(self, theNum: int) -> int:
        """Returns value of Pnindex by its num"""

    def TriangleStrips(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient]:
        """Returns field TriangleStrips"""

    def SetTriangleStrips(self, theTriangleStrips: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Sets field TriangleStrips"""

    def NbTriangleStrips(self) -> int:
        """Returns number of TriangleStrips"""

    def TriangleFans(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient]:
        """Returns field TriangleFans"""

    def SetTriangleFans(self, theTriangleFans: nanoocp.NCollection.NCollection_HArray1[nanoocp.Standard.Standard_Transient] | None) -> None:
        """Sets field TriangleFans"""

    def NbTriangleFans(self) -> int:
        """Returns number of TriangleFans"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_EdgeOrCurve(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type EdgeOrCurve"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_EdgeOrCurve) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of EdgeOrCurve select type
        -- 1 -> Curve
        -- 2 -> Edge
        """

    def Curve(self) -> nanoocp.StepGeom.StepGeom_Curve:
        """Returns Value as Curve (or Null if another type)"""

    def Edge(self) -> nanoocp.StepShape.StepShape_Edge:
        """Returns Value as Edge (or Null if another type)"""

class StepVisual_TessellatedEdge(StepVisual_TessellatedStructuredItem):
    """Representation of STEP entity TessellatedEdge"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedEdge) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordinates: StepVisual_CoordinatesList | None, theHasGeometricLink: bool, theGeometricLink: StepVisual_EdgeOrCurve, theLineStrip: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> StepVisual_CoordinatesList:
        """Returns field Coordinates"""

    def SetCoordinates(self, theCoordinates: StepVisual_CoordinatesList | None) -> None:
        """Sets field Coordinates"""

    def GeometricLink(self) -> StepVisual_EdgeOrCurve:
        """Returns field GeometricLink"""

    def SetGeometricLink(self, theGeometricLink: StepVisual_EdgeOrCurve) -> None:
        """Sets field GeometricLink"""

    def HasGeometricLink(self) -> bool:
        """Returns True if optional field GeometricLink is defined"""

    def LineStrip(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field LineStrip"""

    def SetLineStrip(self, theLineStrip: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field LineStrip"""

    def NbLineStrip(self) -> int:
        """Returns number of LineStrip"""

    def LineStripValue(self, theNum: int) -> int:
        """Returns value of LineStrip by its num"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CubicBezierTessellatedEdge(StepVisual_TessellatedEdge):
    """Representation of STEP entity CubicBezierTessellatedEdge"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_CubicBezierTessellatedEdge) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_CubicBezierTriangulatedFace(StepVisual_TessellatedFace):
    """Representation of STEP entity CubicBezierTriangulatedFace"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_CubicBezierTriangulatedFace) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedFace_Coordinates: StepVisual_CoordinatesList | None, theTessellatedFace_Pnmax: int, theTessellatedFace_Normals: nanoocp.NCollection.NCollection_HArray2[float] | None, theHasTessellatedFace_GeometricLink: bool, theTessellatedFace_GeometricLink: StepVisual_FaceOrSurface, theCtriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Ctriangles(self) -> nanoocp.NCollection.NCollection_HArray2[int]:
        """Returns field Ctriangles"""

    def SetCtriangles(self, theCtriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Sets field Ctriangles"""

    def NbCtriangles(self) -> int:
        """Returns number of Ctriangles"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_PathOrCompositeCurve(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type PathOrCompositeCurve"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_PathOrCompositeCurve) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of PathOrCompositeCurve select type
        -- 1 -> CompositeCurve
        -- 2 -> Path
        """

    def CompositeCurve(self) -> nanoocp.StepGeom.StepGeom_CompositeCurve:
        """Returns Value as CompositeCurve (or Null if another type)"""

    def Path(self) -> nanoocp.StepShape.StepShape_Path:
        """Returns Value as Path (or Null if another type)"""

class StepVisual_TessellatedConnectingEdge(StepVisual_TessellatedEdge):
    """Representation of STEP entity TessellatedConnectingEdge"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedConnectingEdge) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedEdge_Coordinates: StepVisual_CoordinatesList | None, theHasTessellatedEdge_GeometricLink: bool, theTessellatedEdge_GeometricLink: StepVisual_EdgeOrCurve, theTessellatedEdge_LineStrip: nanoocp.NCollection.NCollection_HArray1[int] | None, theSmooth: nanoocp.StepData.StepData_Logical, theFace1: StepVisual_TessellatedFace | None, theFace2: StepVisual_TessellatedFace | None, theLineStripFace1: nanoocp.NCollection.NCollection_HArray1[int] | None, theLineStripFace2: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Smooth(self) -> nanoocp.StepData.StepData_Logical:
        """Returns field Smooth"""

    def SetSmooth(self, theSmooth: nanoocp.StepData.StepData_Logical) -> None:
        """Sets field Smooth"""

    def Face1(self) -> StepVisual_TessellatedFace:
        """Returns field Face1"""

    def SetFace1(self, theFace1: StepVisual_TessellatedFace | None) -> None:
        """Sets field Face1"""

    def Face2(self) -> StepVisual_TessellatedFace:
        """Returns field Face2"""

    def SetFace2(self, theFace2: StepVisual_TessellatedFace | None) -> None:
        """Sets field Face2"""

    def LineStripFace1(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field LineStripFace1"""

    def SetLineStripFace1(self, theLineStripFace1: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field LineStripFace1"""

    def NbLineStripFace1(self) -> int:
        """Returns number of LineStripFace1"""

    def LineStripFace1Value(self, theNum: int) -> int:
        """Returns value of LineStripFace1 by its num"""

    def LineStripFace2(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field LineStripFace2"""

    def SetLineStripFace2(self, theLineStripFace2: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field LineStripFace2"""

    def NbLineStripFace2(self) -> int:
        """Returns number of LineStripFace2"""

    def LineStripFace2Value(self, theNum: int) -> int:
        """Returns value of LineStripFace2 by its num"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedEdgeOrVertex(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type TessellatedEdgeOrVertex"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedEdgeOrVertex) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of TessellatedEdgeOrVertex select type
        -- 1 -> TessellatedEdge
        -- 2 -> TessellatedVertex
        """

    def TessellatedEdge(self) -> StepVisual_TessellatedEdge:
        """Returns Value as TessellatedEdge (or Null if another type)"""

    def TessellatedVertex(self) -> StepVisual_TessellatedVertex:
        """Returns Value as TessellatedVertex (or Null if another type)"""

class StepVisual_TessellatedPointSet(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedPointSet"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedPointSet) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordinates: StepVisual_CoordinatesList | None, thePointList: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> StepVisual_CoordinatesList:
        """Returns field Coordinates"""

    def SetCoordinates(self, theCoordinates: StepVisual_CoordinatesList | None) -> None:
        """Sets field Coordinates"""

    def PointList(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field PointList"""

    def SetPointList(self, thePointList: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field PointList"""

    def NbPointList(self) -> int:
        """Returns number of PointList"""

    def PointListValue(self, theNum: int) -> int:
        """Returns value of PointList by its num"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedShapeRepresentation(nanoocp.StepShape.StepShape_ShapeRepresentation):
    """Representation of STEP entity TessellatedShapeRepresentation"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedShapeRepresentation) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedShapeRepresentationWithAccuracyParameters(StepVisual_TessellatedShapeRepresentation):
    """
    Representation of STEP entity TessellatedShapeRepresentationWithAccuracyParameters
    """

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedShapeRepresentationWithAccuracyParameters) -> None: ...

    def Init(self, theRepresentation_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theRepresentation_Items: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepRepr.StepRepr_RepresentationItem] | None, theRepresentation_ContextOfItems: nanoocp.StepRepr.StepRepr_RepresentationContext | None, theTessellationAccuracyParameters: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def TessellationAccuracyParameters(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns field TessellationAccuracyParameters"""

    def SetTessellationAccuracyParameters(self, theTessellationAccuracyParameters: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Sets field TessellationAccuracyParameters"""

    def NbTessellationAccuracyParameters(self) -> int:
        """Returns number of TessellationAccuracyParameters"""

    def TessellationAccuracyParametersValue(self, theNum: int) -> float:
        """Returns value of TessellationAccuracyParameters by its num"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedShell(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedShell"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedShell) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem] | None, theHasTopologicalLink: bool, theTopologicalLink: nanoocp.StepShape.StepShape_ConnectedFaceSet | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem]:
        """Returns field Items"""

    def SetItems(self, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem] | None) -> None:
        """Sets field Items"""

    def NbItems(self) -> int:
        """Returns number of Items"""

    def ItemsValue(self, theNum: int) -> StepVisual_TessellatedStructuredItem:
        """Returns value of Items by its num"""

    def TopologicalLink(self) -> nanoocp.StepShape.StepShape_ConnectedFaceSet:
        """Returns field TopologicalLink"""

    def SetTopologicalLink(self, theTopologicalLink: nanoocp.StepShape.StepShape_ConnectedFaceSet | None) -> None:
        """Sets field TopologicalLink"""

    def HasTopologicalLink(self) -> bool:
        """Returns True if optional field TopologicalLink is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedSolid(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedSolid"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedSolid) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem] | None, theHasGeometricLink: bool, theGeometricLink: nanoocp.StepShape.StepShape_ManifoldSolidBrep | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem]:
        """Returns field Items"""

    def SetItems(self, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem] | None) -> None:
        """Sets field Items"""

    def NbItems(self) -> int:
        """Returns number of Items"""

    def ItemsValue(self, theNum: int) -> StepVisual_TessellatedStructuredItem:
        """Returns value of Items by its num"""

    def GeometricLink(self) -> nanoocp.StepShape.StepShape_ManifoldSolidBrep:
        """Returns field GeometricLink"""

    def SetGeometricLink(self, theGeometricLink: nanoocp.StepShape.StepShape_ManifoldSolidBrep | None) -> None:
        """Sets field GeometricLink"""

    def HasGeometricLink(self) -> bool:
        """Returns True if optional field GeometricLink is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedVertex(StepVisual_TessellatedStructuredItem):
    """Representation of STEP entity TessellatedVertex"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedVertex) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theCoordinates: StepVisual_CoordinatesList | None, theHasTopologicalLink: bool, theTopologicalLink: nanoocp.StepShape.StepShape_VertexPoint | None, thePointIndex: int) -> None:
        """Initialize all fields (own and inherited)"""

    def Coordinates(self) -> StepVisual_CoordinatesList:
        """Returns field Coordinates"""

    def SetCoordinates(self, theCoordinates: StepVisual_CoordinatesList | None) -> None:
        """Sets field Coordinates"""

    def TopologicalLink(self) -> nanoocp.StepShape.StepShape_VertexPoint:
        """Returns field TopologicalLink"""

    def SetTopologicalLink(self, theTopologicalLink: nanoocp.StepShape.StepShape_VertexPoint | None) -> None:
        """Sets field TopologicalLink"""

    def HasTopologicalLink(self) -> bool:
        """Returns True if optional field TopologicalLink is defined"""

    def PointIndex(self) -> int:
        """Returns field PointIndex"""

    def SetPointIndex(self, thePointIndex: int) -> None:
        """Sets field PointIndex"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TessellatedWire(StepVisual_TessellatedItem):
    """Representation of STEP entity TessellatedWire"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TessellatedWire) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedEdgeOrVertex] | None, theHasGeometricModelLink: bool, theGeometricModelLink: StepVisual_PathOrCompositeCurve) -> None:
        """Initialize all fields (own and inherited)"""

    def Items(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedEdgeOrVertex]:
        """Returns field Items"""

    def SetItems(self, theItems: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedEdgeOrVertex] | None) -> None:
        """Sets field Items"""

    def NbItems(self) -> int:
        """Returns number of Items"""

    def ItemsValue(self, theNum: int) -> StepVisual_TessellatedEdgeOrVertex:
        """Returns value of Items by its num"""

    def GeometricModelLink(self) -> StepVisual_PathOrCompositeCurve:
        """Returns field GeometricModelLink"""

    def SetGeometricModelLink(self, theGeometricModelLink: StepVisual_PathOrCompositeCurve) -> None:
        """Sets field GeometricModelLink"""

    def HasGeometricModelLink(self) -> bool:
        """Returns True if optional field GeometricModelLink is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TriangulatedFace(StepVisual_TessellatedFace):
    """Representation of STEP entity TriangulatedFace"""

    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TriangulatedFace) -> None: ...

    def Init(self, theRepresentationItem_Name: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedFace_Coordinates: StepVisual_CoordinatesList | None, theTessellatedFace_Pnmax: int, theTessellatedFace_Normals: nanoocp.NCollection.NCollection_HArray2[float] | None, theHasTessellatedFace_GeometricLink: bool, theTessellatedFace_GeometricLink: StepVisual_FaceOrSurface, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None, theTriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Pnindex(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field Pnindex"""

    def SetPnindex(self, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field Pnindex"""

    def NbPnindex(self) -> int:
        """Returns number of Pnindex"""

    def PnindexValue(self, theNum: int) -> int:
        """Returns value of Pnindex by its num"""

    def Triangles(self) -> nanoocp.NCollection.NCollection_HArray2[int]:
        """Returns field Triangles"""

    def SetTriangles(self, theTriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Sets field Triangles"""

    def NbTriangles(self) -> int:
        """Returns number of Triangles"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepVisual_TriangulatedSurfaceSet(StepVisual_TessellatedSurfaceSet):
    """Representation of STEP entity TriangulatedSurfaceSet"""

    @overload
    def __init__(self) -> None:
        """default constructor"""

    @overload
    def __init__(self, theOther: StepVisual_TriangulatedSurfaceSet) -> None: ...

    def Init(self, theRepresentationItemName: nanoocp.TCollection.TCollection_HAsciiString | None, theTessellatedFaceCoordinates: StepVisual_CoordinatesList | None, theTessellatedFacePnmax: int, theTessellatedFaceNormals: nanoocp.NCollection.NCollection_HArray2[float] | None, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None, theTriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Pnindex(self) -> nanoocp.NCollection.NCollection_HArray1[int]:
        """Returns field Pnindex"""

    def SetPnindex(self, thePnindex: nanoocp.NCollection.NCollection_HArray1[int] | None) -> None:
        """Sets field Pnindex"""

    def NbPnindex(self) -> int:
        """Returns number of Pnindex"""

    def PnindexValue(self, theNum: int) -> int:
        """Returns value of Pnindex by its num"""

    def Triangles(self) -> nanoocp.NCollection.NCollection_HArray2[int]:
        """Returns field Triangles"""

    def SetTriangles(self, theTriangles: nanoocp.NCollection.NCollection_HArray2[int] | None) -> None:
        """Sets field Triangles"""

    def NbTriangles(self) -> int:
        """Returns number of Triangles"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepVisual
import nanoocp.gp
StepVisual_Array1OfAnnotationPlaneElement = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_AnnotationPlaneElement]
StepVisual_Array1OfBoxCharacteristicSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_BoxCharacteristicSelect]
StepVisual_Array1OfCameraModelD3MultiClippingInterectionSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect]
StepVisual_Array1OfCameraModelD3MultiClippingUnionSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingUnionSelect]
StepVisual_Array1OfCurveStyleFontPattern = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_CurveStyleFontPattern]
StepVisual_Array1OfDirectionCountSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_DirectionCountSelect]
StepVisual_Array1OfDraughtingCalloutElement = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_DraughtingCalloutElement]
StepVisual_Array1OfFillStyleSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_FillStyleSelect]
StepVisual_Array1OfInvisibleItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_InvisibleItem]
StepVisual_Array1OfLayeredItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_LayeredItem]
StepVisual_Array1OfPresentationStyleAssignment = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment]
StepVisual_Array1OfPresentationStyleSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect]
StepVisual_Array1OfRenderingPropertiesSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_RenderingPropertiesSelect]
StepVisual_Array1OfStyleContextSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_StyleContextSelect]
StepVisual_Array1OfSurfaceStyleElementSelect = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_SurfaceStyleElementSelect]
StepVisual_Array1OfTessellatedEdgeOrVertex = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_TessellatedEdgeOrVertex]
StepVisual_Array1OfTessellatedStructuredItem = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem]
StepVisual_Array1OfTextOrCharacter = nanoocp.NCollection.NCollection_Array1[nanoocp.StepVisual.StepVisual_TextOrCharacter]
StepVisual_HArray1OfAnnotationPlaneElement = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_AnnotationPlaneElement]
StepVisual_HArray1OfBoxCharacteristicSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_BoxCharacteristicSelect]
StepVisual_HArray1OfCameraModelD3MultiClippingInterectionSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingInterectionSelect]
StepVisual_HArray1OfCameraModelD3MultiClippingUnionSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CameraModelD3MultiClippingUnionSelect]
StepVisual_HArray1OfCurveStyleFontPattern = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_CurveStyleFontPattern]
StepVisual_HArray1OfDirectionCountSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DirectionCountSelect]
StepVisual_HArray1OfDraughtingCalloutElement = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_DraughtingCalloutElement]
StepVisual_HArray1OfFillStyleSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_FillStyleSelect]
StepVisual_HArray1OfInvisibleItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_InvisibleItem]
StepVisual_HArray1OfLayeredItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_LayeredItem]
StepVisual_HArray1OfPresentationStyleAssignment = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleAssignment]
StepVisual_HArray1OfPresentationStyleSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_PresentationStyleSelect]
StepVisual_HArray1OfRenderingPropertiesSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_RenderingPropertiesSelect]
StepVisual_HArray1OfStyleContextSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_StyleContextSelect]
StepVisual_HArray1OfSurfaceStyleElementSelect = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_SurfaceStyleElementSelect]
StepVisual_HArray1OfTessellatedEdgeOrVertex = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedEdgeOrVertex]
StepVisual_HArray1OfTessellatedStructuredItem = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TessellatedStructuredItem]
StepVisual_HArray1OfTextOrCharacter = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepVisual.StepVisual_TextOrCharacter]
