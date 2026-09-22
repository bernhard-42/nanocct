"""OCCT package IFGraph (toolkit TKXSBase)"""

from typing import overload

import nanoocp.Interface
import nanoocp.Standard


class IFGraph_AllConnected(nanoocp.Interface.Interface_GraphContent):
    """
    this class gives content of the CONNECTED COMPONENT(S)
    which include specific Entity(ies)
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph) -> None:
        """creates an AllConnected from a graph, empty ready to be filled"""

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        creates an AllConnected which memorizes Entities Connected to
        a given one, at any level : that is, itself, all Entities
        Shared by it and Sharing it, and so on.
        In other terms, this is the content of the CONNECTED COMPONENT
        which include a specific Entity
        """

    @overload
    def __init__(self, theOther: IFGraph_AllConnected) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        adds an entity and its Connected ones to the list (allows to
        cumulate all Entities Connected by some ones)
        Note that if "ent" is in the already computed list,, no entity
        will be added, but if "ent" is not already in the list, a new
        Connected Component will be cumulated
        """

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """does the specific evaluation (Connected entities atall levels)"""

class IFGraph_AllShared(nanoocp.Interface.Interface_GraphContent):
    """
    this class determines all Entities shared by some specific
    ones, at any level (those which will be lead in a Transfer
    for instance)
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph) -> None:
        """creates an AllShared from a graph, empty ready to be filled"""

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        creates an AllShared which memrizes Entities shared by a given
        one, at any level, including itself
        """

    @overload
    def __init__(self, theOther: IFGraph_AllShared) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        adds an entity and its shared ones to the list (allows to
        cumulate all Entities shared by some ones)
        """

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Adds Entities from an EntityIterator and all their shared
        ones at any level
        """

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """does the specific evaluation (shared entities atall levels)"""

class IFGraph_Articulations(nanoocp.Interface.Interface_GraphContent):
    """
    this class gives entities which are Articulation points
    in a whole Model or in a sub-part
    An Articulation Point divides the graph in two (or more)
    disconnected sub-graphs
    Identifying Articulation Points allows improving
    efficiency of splitting a set of Entities into sub-sets
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        creates Articulations to evaluate a Graph
        whole True : works on the whole Model
        whole False : remains empty, ready to work on a sub-part
        """

    @overload
    def __init__(self, theOther: IFGraph_Articulations) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """adds an entity and its shared ones to the list"""

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """adds a list of entities (as an iterator)"""

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """Evaluates the list of Articulation points"""

class IFGraph_Compare(nanoocp.Interface.Interface_GraphContent):
    """
    this class evaluates effect of two compared sub-parts :
    cumulation (union), common part (intersection-overlapping)
    part specific to first sub-part or to the second one
    Results are kept in a Graph, several question can be set
    Basic Iteration gives Cumulation (union)
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph) -> None:
        """creates empty Compare, ready to work"""

    @overload
    def __init__(self, theOther: IFGraph_Compare) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None, first: bool) -> None:
        """
        adds an entity and its shared ones to the list :
        first True means adds to the first sub-list, else to the 2nd
        """

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator, first: bool) -> None:
        """
        adds a list of entities (as an iterator) as such, that is,
        their shared entities are not considered (use AllShared to
        have them)
        first True means adds to the first sub-list, else to the 2nd
        """

    def Merge(self) -> None:
        """
        merges the second list into the first one, hence the second
        list is empty
        """

    def RemoveSecond(self) -> None:
        """Removes the contents of second list"""

    def KeepCommon(self) -> None:
        """
        Keeps only Common part, sets it as First list and clears
        second list
        """

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """Recomputes result of comparing to sub-parts"""

    def Common(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns entities common to the both parts"""

    def FirstOnly(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns entities which are exclusively in the first list"""

    def SecondOnly(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns entities which are exclusively in the second part"""

class IFGraph_SubPartsIterator:
    """
    defines general form for graph classes of which result is
    not a single iteration on Entities, but a nested one :
    External iteration works on sub-parts, identified by each
    class (according to its algorithm)
    Internal Iteration concerns Entities of a sub-part
    Sub-Parts are assumed to be disjoined; if they are not,
    the first one has priority

    A SubPartsIterator can work in two steps : first, load
    entities which have to be processed
    then, analyse to set those entities into sub-parts
    """

    @overload
    def __init__(self, other: IFGraph_SubPartsIterator) -> None:
        """
        Creates a SubPartIterator from another one and gets its Data
        Note that only non-empty sub-parts are taken into account
        PartNum is set to the last one
        """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        Creates with a Graph, whole or parts of it
        whole True  : works on the entire Model
        whole False : empty, ready to be filled
        SubPartIterator is set to load entities
        """

    def GetParts(self, other: IFGraph_SubPartsIterator) -> None:
        """
        Gets Parts from another SubPartsIterator (in addition to the
        ones already recorded)
        Error if both SubPartsIterators are not based on the same Model
        """

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model with which this Iterator was created"""

    def AddPart(self) -> None:
        """Adds an empty part and sets it to receive entities"""

    def NbParts(self) -> int:
        """Returns count of registered parts"""

    def PartNum(self) -> int:
        """
        Returns numero of part which currently receives entities
        (0 at load time)
        """

    def SetLoad(self) -> None:
        """
        Sets SubPartIterator to get Entities (by GetFromEntity &
        GetFromIter) into load status, to be analysed later
        """

    def SetPartNum(self, num: int) -> None:
        """
        Sets numero of receiving part to a new value
        Error if not in range (1-NbParts)
        """

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None, shared: bool) -> None:
        """
        Adds an Entity : into load status if in Load mode, to the
        current part if there is one. If shared is True, adds
        also its shared ones (shared at all levels)
        """

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        Adds a list of Entities (into Load mode or to a Part),
        given as an Iterator
        """

    def Reset(self) -> None:
        """
        Erases data (parts, entities) : "me" becomes empty and in
        load status
        """

    def Evaluate(self) -> None:
        """
        Called by Clear, this method allows evaluation just before
        iteration; its default is doing nothing, it is designed to
        be redefined
        """

    def Loaded(self) -> nanoocp.Interface.Interface_GraphContent:
        """Returns entities which where loaded (not set into a sub-part)"""

    def LoadedGraph(self) -> nanoocp.Interface.Interface_Graph:
        """Same as above, but under the form of a Graph"""

    def IsLoaded(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if an Entity is loaded (either set into a
        sub-part or not)
        """

    def IsInPart(self, ent: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if an Entity is Present in a sub-part"""

    def EntityPartNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns number of the sub-part in which an Entity has been set
        if it is not in a sub-part (or not loaded at all), Returns 0
        """

    def Start(self) -> None:
        """Sets iteration to its beginning; calls Evaluate"""

    def More(self) -> bool:
        """
        Returns True if there are more sub-parts to iterate on
        Note : an empty sub-part is not taken in account by Iteration
        """

    def Next(self) -> None:
        """
        Sets iteration to the next sub-part
        if there is not, IsSingle-Entities will raises an exception
        """

    def IsSingle(self) -> bool:
        """
        Returns True if current sub-part is single (has only one Entity)
        Error if there is no sub-part to iterate now
        """

    def FirstEntity(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the first entity of current sub-part, that is for a
        Single one, the only one it contains
        Error : same as above (end of iteration)
        """

    def Entities(self) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns current sub-part, not as a "Value", but as an Iterator
        on Entities it contains
        Error : same as above (end of iteration)
        """

class IFGraph_ConnectedComponants(IFGraph_SubPartsIterator):
    """
    determines Connected Components in a Graph.
    They define disjoined sets of Entities.
    """

    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        creates with a Graph, and will analyse :
        whole True  : all the contents of the Model
        whole False : sub-parts which will be given later
        """

    def Evaluate(self) -> None:
        """does the computation"""

class IFGraph_Cumulate(nanoocp.Interface.Interface_GraphContent):
    """
    this class evaluates effect of cumulated sub-parts :
    overlapping, forgotten entities
    Results are kept in a Graph, several question can be set
    Basic Iteration gives entities which are part of Cumulation
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph) -> None:
        """creates empty Cumulate, ready to work"""

    @overload
    def __init__(self, theOther: IFGraph_Cumulate) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """adds an entity and its shared ones to the list"""

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """
        adds a list of entities (as an iterator) as such, that is,
        without their shared entities (use AllShared to have them)
        """

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """Evaluates the result of cumulation"""

    def Overlapped(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns entities which are taken several times"""

    def Forgotten(self) -> nanoocp.Interface.Interface_EntityIterator:
        """returns entities which are not taken"""

    def PerCount(self, count: int = 1) -> nanoocp.Interface.Interface_EntityIterator:
        """
        Returns entities taken a given count of times
        (0 : same as Forgotten, 1 : same as no Overlap : default)
        """

    def NbTimes(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        returns number of times an Entity has been counted
        (0 means forgotten, more than 1 means overlap, 1 is normal)
        """

    def HighestNbTimes(self) -> int:
        """
        Returns the highest number of times recorded for every Entity
        (0 means empty, 1 means no overlap)
        """

class IFGraph_Cycles(IFGraph_SubPartsIterator):
    """determines strong components in a graph which are Cycles"""

    @overload
    def __init__(self, subparts: IFGraph_StrongComponants) -> None:
        """creates from a StrongComponants which was already computed"""

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        creates with a Graph, and will analyse :
        whole True  : all the contents of the Model
        whole False : sub-parts which will be given later
        """

    def Evaluate(self) -> None:
        """
        does the computation. Cycles are StrongComponants which are
        not Single
        """

class IFGraph_ExternalSources(nanoocp.Interface.Interface_GraphContent):
    """
    this class gives entities which are Source of entities of
    a sub-part, but are not contained by this sub-part
    """

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph) -> None:
        """creates empty ExternalSources, ready to work"""

    @overload
    def __init__(self, theOther: IFGraph_ExternalSources) -> None: ...

    def GetFromEntity(self, ent: nanoocp.Standard.Standard_Transient | None) -> None:
        """adds an entity and its shared ones to the list"""

    def GetFromIter(self, iter: nanoocp.Interface.Interface_EntityIterator) -> None:
        """adds a list of entities (as an iterator) with shared ones"""

    def ResetData(self) -> None:
        """Allows to restart on a new data set"""

    def Evaluate(self) -> None:
        """Evaluates external sources of a set of entities"""

    def IsEmpty(self) -> bool:
        """
        Returns True if no External Source are found
        It means that we have a "root" set
        (performs an Evaluation as necessary)
        """

class IFGraph_StrongComponants(IFGraph_SubPartsIterator):
    """
    determines strong components of a graph, that is
    isolated entities (single components) or loops
    """

    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        creates with a Graph, and will analyse :
        whole True  : all the contents of the Model
        whole False : sub-parts which will be given later
        """

    def Evaluate(self) -> None:
        """does the computation"""

class IFGraph_SCRoots(IFGraph_StrongComponants):
    """determines strong components in a graph which are Roots"""

    @overload
    def __init__(self, subparts: IFGraph_StrongComponants) -> None:
        """creates from a StrongComponants which was already computed"""

    @overload
    def __init__(self, agraph: nanoocp.Interface.Interface_Graph, whole: bool) -> None:
        """
        creates with a Graph, and will analyse :
        whole True  : all the contents of the Model
        whole False : sub-parts which will be given later
        """

    def Evaluate(self) -> None:
        """does the computation"""
