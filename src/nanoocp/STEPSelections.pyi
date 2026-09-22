"""OCCT package STEPSelections (toolkit TKDESTEP)"""

from typing import overload

import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepBasic
import nanoocp.StepRepr
import nanoocp.StepSelect
import nanoocp.StepShape
import nanoocp.TCollection
import nanoocp.XSControl


class STEPSelections_AssemblyLink(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, nauo: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None, item: nanoocp.Standard.Standard_Transient | None, part: STEPSelections_AssemblyComponent | None) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_AssemblyLink) -> None: ...

    def GetNAUO(self) -> nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence: ...

    def GetItem(self) -> nanoocp.Standard.Standard_Transient: ...

    def GetComponent(self) -> STEPSelections_AssemblyComponent: ...

    def SetNAUO(self, nauo: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None) -> None: ...

    def SetItem(self, item: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetComponent(self, part: STEPSelections_AssemblyComponent | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_AssemblyComponent(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, sdr: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.STEPSelections.STEPSelections_AssemblyLink] | None) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_AssemblyComponent) -> None: ...

    def GetSDR(self) -> nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation: ...

    def GetList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.STEPSelections.STEPSelections_AssemblyLink]: ...

    def SetSDR(self, sdr: nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation | None) -> None: ...

    def SetList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.STEPSelections.STEPSelections_AssemblyLink] | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_AssemblyExplorer:
    @overload
    def __init__(self, G: nanoocp.Interface.Interface_Graph) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_AssemblyExplorer) -> None: ...

    def Init(self, G: nanoocp.Interface.Interface_Graph) -> None: ...

    def Dump(self) -> str: ...

    def FindSDRWithProduct(self, product: nanoocp.StepBasic.StepBasic_ProductDefinition | None) -> nanoocp.StepShape.StepShape_ShapeDefinitionRepresentation: ...

    def FillListWithGraph(self, cmp: STEPSelections_AssemblyComponent | None) -> None: ...

    def FindItemWithNAUO(self, nauo: nanoocp.StepRepr.StepRepr_NextAssemblyUsageOccurrence | None) -> nanoocp.Standard.Standard_Transient: ...

    def NbAssemblies(self) -> int:
        """Returns the number of root assemblies;"""

    def Root(self, rank: int = 1) -> STEPSelections_AssemblyComponent:
        """Returns root of assenbly by its rank;"""

class STEPSelections_Counter:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_Counter) -> None: ...

    def Count(self, graph: nanoocp.Interface.Interface_Graph, start: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def Clear(self) -> None: ...

    def NbInstancesOfFaces(self) -> int: ...

    def NbInstancesOfShells(self) -> int: ...

    def NbInstancesOfSolids(self) -> int: ...

    def NbInstancesOfEdges(self) -> int: ...

    def NbInstancesOfWires(self) -> int: ...

    def NbSourceFaces(self) -> int: ...

    def NbSourceShells(self) -> int: ...

    def NbSourceSolids(self) -> int: ...

    def NbSourceEdges(self) -> int: ...

    def NbSourceWires(self) -> int: ...

class STEPSelections_SelectAssembly(nanoocp.IFSelect.IFSelect_SelectExplore):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_SelectAssembly) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity, to take its faces
        Works recursively
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Assembly structures\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_SelectDerived(nanoocp.StepSelect.StepSelect_StepType):
    def __init__(self) -> None: ...

    def Matches(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None, text: nanoocp.TCollection.TCollection_AsciiString, exact: bool) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_SelectFaces(nanoocp.IFSelect.IFSelect_SelectExplore):
    """This selection returns "STEP faces\""""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_SelectFaces) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity, to take its faces
        Works recursively
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Faces\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_SelectForTransfer(nanoocp.XSControl.XSControl_SelectForTransfer):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, TR: nanoocp.XSControl.XSControl_TransferReader | None) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_SelectForTransfer) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_SelectGSCurves(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    This selection returns "curves in the geometric_set (except composite curves)\"
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_SelectGSCurves) -> None: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool: ...

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Curves\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class STEPSelections_SelectInstances(nanoocp.IFSelect.IFSelect_SelectExplore):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: STEPSelections_SelectInstances) -> None: ...

    def RootResult(self, G: nanoocp.Interface.Interface_Graph) -> nanoocp.Interface.Interface_EntityIterator: ...

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool: ...

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns a text defining the criterium : "Instances\""""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.STEPSelections
STEPSelections_HSequenceOfAssemblyLink = nanoocp.NCollection.NCollection_HSequence[nanoocp.STEPSelections.STEPSelections_AssemblyLink]
STEPSelections_SequenceOfAssemblyLink = nanoocp.NCollection.NCollection_Sequence[nanoocp.STEPSelections.STEPSelections_AssemblyLink]
