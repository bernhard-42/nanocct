"""OCCT package XSControl (toolkit TKXSBase)"""

from typing import TextIO, overload

import nanoocp.DE
import nanoocp.IFSelect
import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.Transfer
import nanoocp.gp


class XSControl:
    """
    This package provides complements to IFSelect & Co for
    control of a session
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSControl) -> None: ...

    @staticmethod
    def Session(pilot: nanoocp.IFSelect.IFSelect_SessionPilot | None) -> XSControl_WorkSession:
        """
        Returns the WorkSession of a SessionPilot, but casts it as
        from XSControl : it then gives access to Control & Transfers
        """

    @staticmethod
    def Vars(pilot: nanoocp.IFSelect.IFSelect_SessionPilot | None) -> XSControl_Vars:
        """
        Returns the Vars of a SessionPilot, it is brought by Session
        it provides access to external variables
        """

class XSControl_ConnectedShapes(nanoocp.IFSelect.IFSelect_SelectExplore):
    """
    From a TopoDS_Shape, or from the entity which has produced it,
    searches for the shapes, and the entities which have produced
    them in last transfer, which are adjacent to it by VERTICES
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Selection ConnectedShapes. It remains to be set a
        TransferReader
        """

    @overload
    def __init__(self, TR: XSControl_TransferReader | None) -> None:
        """
        Creates a Selection ConnectedShapes, which will work with the
        current TransferProcess brought by the TransferReader
        """

    @overload
    def __init__(self, theOther: XSControl_ConnectedShapes) -> None: ...

    def SetReader(self, TR: XSControl_TransferReader | None) -> None:
        """
        Sets a TransferReader to sort entities : it brings the
        TransferProcess which may change, while the TransferReader does not
        """

    def Explore(self, level: int, ent: nanoocp.Standard.Standard_Transient | None, G: nanoocp.Interface.Interface_Graph, explored: nanoocp.Interface.Interface_EntityIterator) -> bool:
        """
        Explores an entity : entities from which are connected to that
        produced by this entity, including itself
        """

    def ExploreLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium.
        "Connected Entities through produced Shapes\"
        """

    @staticmethod
    def AdjacentEntities(ashape: nanoocp.TopoDS.TopoDS_Shape, TP: nanoocp.Transfer.Transfer_TransientProcess | None, type: nanoocp.TopAbs.TopAbs_ShapeEnum) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        This functions considers a shape from a transfer and performs
        the search function explained above
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_Controller(nanoocp.Standard.Standard_Transient):
    """
    This class allows a general X-STEP engine to run generic
    functions on any interface norm, in the same way. It includes
    the transfer operations. I.e. it gathers the already available
    general modules, the engine has just to know it

    The important point is that a given X-STEP Controller is
    attached to a given couple made of an Interface Norm (such as
    IGES-5.1) and an application data model (CasCade Shapes for
    instance).

    Finally, Controller can be gathered in a general dictionary then
    retrieved later by a general call (method Recorded)

    It does not manage the produced data, but the Actors make the
    link between the norm and the application
    """

    def SetNames(self, theLongName: str, theShortName: str) -> None:
        """
        Changes names
        if a name is empty, the formerly set one remains
        Remark : Does not call Record or AutoRecord
        """

    def AutoRecord(self) -> None:
        """
        Records <me> is a general dictionary under Short and Long
        Names (see method Name)
        """

    def Record(self, name: str) -> None:
        """
        Records <me> in a general dictionary under a name
        Error if <name> already used for another one
        """

    @staticmethod
    def Recorded(name: str) -> XSControl_Controller:
        """
        Returns the Controller attached to a given name
        Returns a Null Handle if <name> is unknown
        """

    def Name(self, rsc: bool = False) -> str:
        """
        Returns a name, as given when initializing :
        rsc = False (D) : True Name attached to the Norm (long name)
        rsc = True : Name of the resource set (i.e. short name)
        """

    def Protocol(self) -> nanoocp.Interface.Interface_Protocol:
        """Returns the Protocol attached to the Norm (from field)"""

    def WorkLibrary(self) -> nanoocp.IFSelect.IFSelect_WorkLibrary:
        """
        Returns the WorkLibrary attached to the Norm. Remark that it
        has to be in phase with the Protocol (read from field)
        """

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Creates a new empty Model ready to receive data of the Norm
        Used to write data from Imagine to an interface file
        """

    def ActorRead(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """
        Returns the Actor for Read attached to the pair (norm,appli)
        It can be adapted for data of the input Model, as required
        Can be read from field then adapted with Model as required
        """

    def ActorWrite(self) -> nanoocp.Transfer.Transfer_ActorOfFinderProcess:
        """
        Returns the Actor for Write attached to the pair (norm,appli)
        Read from field. Can be redefined
        """

    def SetModeWrite(self, modemin: int, modemax: int, shape: bool = True) -> None:
        """
        Sets minimum and maximum values for modetrans (write)
        Erases formerly recorded bounds and values
        Actually only for shape
        Then, for each value a little help can be attached
        """

    def SetModeWriteHelp(self, modetrans: int, help: str, shape: bool = True) -> None:
        """Attaches a short line of help to a value of modetrans (write)"""

    def ModeWriteBounds(self, shape: bool = True) -> tuple[bool, int, int]:
        """
        Returns recorded min and max values for modetrans (write)
        Actually only for shapes
        Returns True if bounds are set, False else (then, free value)
        """

    def IsModeWrite(self, modetrans: int, shape: bool = True) -> bool:
        """
        Tells if a value of <modetrans> is a good value(within bounds)
        Actually only for shapes
        """

    def ModeWriteHelp(self, modetrans: int, shape: bool = True) -> str:
        """
        Returns the help line recorded for a value of modetrans
        empty if help not defined or not within bounds or if values are free
        """

    def RecognizeWriteTransient(self, obj: nanoocp.Standard.Standard_Transient | None, modetrans: int = 0) -> bool:
        """
        Tells if <obj> (an application object) is a valid candidate
        for a transfer to a Model.
        By default, asks the ActorWrite if known (through a
        TransientMapper). Can be redefined
        """

    def TransferWriteTransient(self, obj: nanoocp.Standard.Standard_Transient | None, FP: nanoocp.Transfer.Transfer_FinderProcess | None, model: nanoocp.Interface.Interface_InterfaceModel | None, modetrans: int = 0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Takes one Transient Object and transfers it to an
        InterfaceModel (already created, e.g. by NewModel)
        (result is recorded in the model by AddWithRefs)
        FP records produced results and checks

        Default uses ActorWrite; can be redefined as necessary
        Returned value is a status, as follows :
        0  OK ,  1 No Result ,  2 Fail (e.g. exception raised)
        -1 bad conditions ,  -2 bad model or null model
        For type of object not recognized : should return 1
        """

    def RecognizeWriteShape(self, shape: nanoocp.TopoDS.TopoDS_Shape, modetrans: int = 0) -> bool:
        """
        Tells if a shape is valid for a transfer to a model
        Asks the ActorWrite (through a ShapeMapper)
        """

    def TransferWriteShape(self, shape: nanoocp.TopoDS.TopoDS_Shape, FP: nanoocp.Transfer.Transfer_FinderProcess | None, model: nanoocp.Interface.Interface_InterfaceModel | None, modetrans: int = 0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Takes one Shape and transfers it to an
        InterfaceModel (already created, e.g. by NewModel)
        Default uses ActorWrite; can be redefined as necessary
        Returned value is a status, as follows :
        Done  OK ,  Void : No Result ,  Fail : Fail (e.g. exception)
        Error : bad conditions , bad model or null model
        """

    def AddSessionItem(self, theItem: nanoocp.Standard.Standard_Transient | None, theName: str, toApply: bool = False) -> None:
        """
        Records a Session Item, to be added for customisation of the Work Session.
        It must have a specific name.
        <setapplied> is used if <item> is a GeneralModifier, to decide
        If set to true, <item> will be applied to the hook list "send".
        Else, it is not applied to any hook list.
        Remark : this method is to be called at Create time,
        the recorded items will be used by Customise
        Warning : if <name> conflicts, the last recorded item is kept
        """

    def SessionItem(self, theName: str) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an item given its name to record in a Session
        If <name> is unknown, returns a Null Handle
        """

    def Customise(self) -> XSControl_WorkSession:
        """
        Customises a WorkSession, by adding to it the recorded items (by AddSessionItem)
        """

    def AdaptorSession(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_FuncShape:
    """
    Defines additional commands for XSControl to :
    - control of initialisation (xinit, xnorm, newmodel)
    - analyse of the result of a transfer (recorded in a
    TransientProcess for Read, FinderProcess for Write) :
    statistics, various lists (roots,complete,abnormal), what
    about one specific entity, producing a model with the
    abnormal result

    This appendix of XSControl is compiled separately to distinguish
    basic features from user callable forms
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSControl_FuncShape) -> None: ...

    @staticmethod
    def Init() -> None:
        """
        Defines and loads all functions which work on shapes for XSControl (as ActFunc)
        """

    @staticmethod
    def MoreShapes(session: XSControl_WorkSession | None, name: str) -> tuple[int, nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]]:
        """
        Analyses a name as designating Shapes from a Vars or from
        XSTEP transfer (last Transfer on Reading). <name> can be :
        "*" : all the root shapes produced by last Transfer (Read)
        i.e. considers roots of the TransientProcess
        a name : a name of a variable DRAW

        Returns the count of designated Shapes. Their list is put in
        <list>. If <list> is null, it is firstly created. Then it is
        completed (Append without Clear) by the Shapes found
        Returns 0 if no Shape could be found
        """

    @staticmethod
    def FileAndVar(session: XSControl_WorkSession | None, file: str, var: str, def_: str, resfile: nanoocp.TCollection.TCollection_AsciiString, resvar: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """
        Analyses given file name and variable name, with a default
        name for variables. Returns resulting file name and variable
        name plus status "file to read"(True) or "already read"(False)
        In the latter case, empty resfile means no file available

        If <file> is null or empty or equates ".", considers Session
        and returned status is False
        Else, returns resfile = file and status is True
        If <var> is neither null nor empty, resvar = var
        Else, the root part of <resfile> is considered, if defined
        Else, <def> is taken
        """

class XSControl_Functions:
    """
    Functions from XSControl gives access to actions which can be
    commanded with the resources provided by XSControl: especially
    Controller and Transfer

    It works by adding functions by method Init
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSControl_Functions) -> None: ...

    @staticmethod
    def Init() -> None:
        """Defines and loads all functions for XSControl (as ActFunc)"""

class XSControl_Reader:
    """
    A groundwork to convert a shape to data which complies
    with a particular norm. This data can be that of a whole
    model or that of a specific list of entities in the model.
    You specify the list using a single selection or a
    combination of selections. A selection is an operator which
    computes a list of entities from a list given in input. To
    specify the input, you can use:
    - A predefined selection such as "xst-transferrable-roots"
    - A filter based on a signature.
    A signature is an operator which returns a string from an
    entity according to its type.
    For example:
    - "xst-type" (CDL)
    - "iges-level"
    - "step-type".
    A filter can be based on a signature by giving a value to
    be matched by the string returned. For example,
    "xst-type(Curve)".
    If no list is specified, the selection computes its list of
    entities from the whole model. To use this class, you have to
    initialize the transfer norm first, as shown in the example below.
    Example:
    Control_Reader reader;
    IFSelect_ReturnStatus status = reader.ReadFile (filename.);
    When using IGESControl_Reader or STEPControl_Reader - as the
    above example shows - the reader initializes the norm directly.
    Note that loading the file only stores the data. It does
    not translate this data. Shapes are accumulated by
    successive transfers. The last shape is cleared by:
    - ClearShapes which allows you to handle a new batch
    - TransferRoots which restarts the list of shapes from scratch.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a Reader from scratch (creates an empty WorkSession)
        A WorkSession or a Controller must be provided before running
        """

    @overload
    def __init__(self, norm: str) -> None:
        """
        Creates a Reader from scratch, with a norm name which
        identifies a Controller
        """

    @overload
    def __init__(self, WS: XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a Reader from an already existing Session, with a
        Controller already set
        Virtual destructor
        """

    @overload
    def __init__(self, theOther: XSControl_Reader) -> None: ...

    def SetNorm(self, norm: str) -> bool:
        """
        Sets a specific norm to <me>
        Returns True if done, False if <norm> is not available
        """

    def SetWS(self, WS: XSControl_WorkSession | None, scratch: bool = True) -> None:
        """Sets a specific session to <me>"""

    def WS(self) -> XSControl_WorkSession:
        """Returns the session used in <me>"""

    def ReadFile(self, filename: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Loads a file and returns the read status
        Zero for a Model which complies with the Controller
        """

    def ReadStream(self, theName: str, theIStream: TextIO) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Loads a file from stream and returns the read status"""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the model. It can then be consulted (header, product)"""

    @overload
    def GiveList(self, first: str = '', second: str = '') -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns a list of entities from the IGES or STEP file
        according to the following rules:
        - if first and second are empty strings, the whole file is selected.
        - if first is an entity number or label, the entity referred to is selected.
        - if first is a list of entity numbers/labels separated by commas, the entities referred to
        are selected,
        - if first is the name of a selection in the worksession and second is not defined,
        the list contains the standard output for that selection.
        - if first is the name of a selection and second is defined, the criterion defined
        by second is applied to the result of the first selection.
        A selection is an operator which computes a list of entities from a list given in
        input according to its type. If no list is specified, the selection computes its
        list of entities from the whole model.
        A selection can be:
        - A predefined selection (xst-transferrable-mode)
        - A filter based on a signature
        A Signature is an operator which returns a string from an entity according to its type. For
        example:
        - "xst-type" (CDL)
        - "iges-level"
        - "step-type".
        For example, if you wanted to select only the advanced_faces in a STEP file you
        would use the following code:
        Example
        Reader.GiveList("xst-transferrable-roots","step-type(ADVANCED_FACE)");
        Warning
        If the value given to second is incorrect, it will simply be ignored.
        """

    @overload
    def GiveList(self, first: str, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Computes a List of entities from the model as follows
        <first> being a Selection, <ent> being an entity or a list
        of entities (as a HSequenceOfTransient) :
        the standard result of this selection applied to this list
        if <first> is erroneous, a null handle is returned
        """

    def NbRootsForTransfer(self) -> int:
        """
        Determines the list of root entities which are candidate for
        a transfer to a Shape, and returns the number
        of entities in the list
        """

    def RootForTransfer(self, num: int = 1) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an IGES or STEP root
        entity for translation. The entity is identified by its
        rank in a list.
        """

    def TransferOneRoot(self, num: int = 1, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates a root identified by the rank num in the model.
        false is returned if no shape is produced.
        """

    def TransferOne(self, num: int, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates an IGES or STEP
        entity identified by the rank num in the model.
        false is returned if no shape is produced.
        """

    def TransferEntity(self, start: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Translates an IGES or STEP
        entity in the model. true is returned if a shape is
        produced; otherwise, false is returned.
        """

    def TransferList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Translates a list of entities.
        Returns the number of IGES or STEP entities that were
        successfully translated. The list can be produced with GiveList.
        Warning - This function does not clear the existing output shapes.
        """

    def TransferRoots(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Translates all translatable
        roots and returns the number of successful translations.
        Warning - This function clears existing output shapes first.
        """

    def ClearShapes(self) -> None:
        """
        Clears the list of shapes that
        may have accumulated in calls to TransferOne or TransferRoot.C
        """

    def NbShapes(self) -> int:
        """Returns the number of shapes produced by translation."""

    def Shape(self, num: int = 1) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the shape resulting
        from a translation and identified by the rank num.
        num equals 1 by default. In other words, the first shape
        resulting from the translation is returned.
        """

    def OneShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns all of the results in
        a single shape which is:
        - a null shape if there are no results,
        - a shape if there is one result,
        - a compound containing the resulting shapes if there are more than one.
        """

    def PrintCheckLoad(self, failsonly: bool, mode: nanoocp.IFSelect.IFSelect_PrintCount) -> None:
        """
        Prints the check list attached to loaded data, on the Standard
        Trace File (starts at std::cout)
        All messages or fails only, according to <failsonly>
        mode = 0 : per entity, prints messages
        mode = 1 : per message, just gives count of entities per check
        mode = 2 : also gives entity numbers
        """

    def PrintCheckLoad__str(self, failsonly: bool, mode: nanoocp.IFSelect.IFSelect_PrintCount) -> str:
        """
        PrintCheckLoad__str: the C++ overload PrintCheckLoad(Standard_OStream &, const bool, const IFSelect_PrintCount); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Prints the check list attached to loaded data.
        """

    def PrintCheckTransfer(self, failsonly: bool, mode: nanoocp.IFSelect.IFSelect_PrintCount) -> None:
        """
        Displays check results for the
        last translation of IGES or STEP entities to Open CASCADE
        entities. Only fail messages are displayed if failsonly is
        true. All messages are displayed if failsonly is
        false. mode determines the contents and the order of the
        messages according to the terms of the IFSelect_PrintCount enumeration.
        """

    def PrintCheckTransfer__str(self, failsonly: bool, mode: nanoocp.IFSelect.IFSelect_PrintCount) -> str:
        """
        PrintCheckTransfer__str: the C++ overload PrintCheckTransfer(Standard_OStream &, const bool, const IFSelect_PrintCount); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Displays check results for the last translation of IGES or STEP entities to Open CASCADE
        entities.
        """

    def PrintStatsTransfer(self, what: int, mode: int = 0) -> None:
        """
        Displays the statistics for
        the last translation. what defines the kind of
        statistics that are displayed as follows:
        - 0 gives general statistics (number of translated roots,
        number of warnings, number of fail messages),
        - 1 gives root results,
        - 2 gives statistics for all checked entities,
        - 3 gives the list of translated entities,
        - 4 gives warning and fail messages,
        - 5 gives fail messages only.
        The use of mode depends on the value of what. If what is 0,
        mode is ignored. If what is 1, 2 or 3, mode defines the following:
        - 0 lists the numbers of IGES or STEP entities in the respective model
        - 1 gives the number, identifier, type and result
        type for each IGES or STEP entity and/or its status
        (fail, warning, etc.)
        - 2 gives maximum information for each IGES or STEP entity (i.e. checks)
        - 3 gives the number of entities per type of IGES or STEP entity
        - 4 gives the number of IGES or STEP entities per result type and/or status
        - 5 gives the number of pairs (IGES or STEP or result type and status)
        - 6 gives the number of pairs (IGES or STEP or result type
        and status) AND the list of entity numbers in the IGES or STEP model.
        If what is 4 or 5, mode defines the warning and fail
        messages as follows:
        - if mode is 0 all warnings and checks per entity are returned
        - if mode is 2 the list of entities per warning is returned.
        If mode is not set, only the list of all entities per warning is given.
        """

    def PrintStatsTransfer__str(self, what: int, mode: int = 0) -> str:
        """
        PrintStatsTransfer__str: the C++ overload PrintStatsTransfer(Standard_OStream &, const int, const int); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        Displays the statistics for the last translation.
        """

    def GetStatsTransfer(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> tuple[int, int, int]:
        """Gives statistics about Transfer"""

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]) -> None:
        """
        Sets parameters for shape processing.
        @param theParameters the parameters for shape processing.
        """

    @overload
    def SetShapeFixParameters(self, theParameters: nanoocp.DE.DE_ShapeFixParameters, theAdditionalParameters: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString] = ...) -> None:
        """
        Sets parameters for shape processing.
        Parameters from @p theParameters are copied to the internal map.
        Parameters from @p theAdditionalParameters are copied to the internal map
        if they are not present in @p theParameters.
        @param theParameters the parameters for shape processing.
        @param theAdditionalParameters the additional parameters for shape processing.
        """

    def GetShapeFixParameters(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns parameters for shape processing that was set by SetParameters() method.
        @return the parameters for shape processing. Empty map if no parameters were set.
        """

    def SetShapeProcessFlags(self, theFlags: set[int]) -> None:
        """
        Sets flags defining operations to be performed on shapes.
        @param theFlags The flags defining operations to be performed on shapes.
        """

    def GetShapeProcessFlags(self) -> tuple[set[int], bool]:
        """
        Returns flags defining operations to be performed on shapes.
        @return Pair of values defining operations to be performed on shapes and a boolean value
        that indicates whether the flags were set.
        """

class XSControl_SelectForTransfer(nanoocp.IFSelect.IFSelect_SelectExtract):
    """
    This selection selects the entities which are recognised for
    transfer by an Actor for Read : current one or another one.

    An Actor is an operator which runs transfers from interface
    entities to objects for Imagine. It has a method to recognize
    the entities it can process (by default, it recognises all,
    this method can be redefined).

    A TransferReader brings an Actor, according to the currently
    selected norm and transfer conditions.

    This selection considers, either the current Actor (brought by
    the TransferReader, updated as required), or a precise one.
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a SelectForTransfer, non initialised
        it sorts nothing, unless an Actor has been defined
        """

    @overload
    def __init__(self, TR: XSControl_TransferReader | None) -> None:
        """
        Creates a SelectForTransfer, which will work with the
        currently defined Actor brought by the TransferReader
        """

    @overload
    def __init__(self, theOther: XSControl_SelectForTransfer) -> None: ...

    def SetReader(self, TR: XSControl_TransferReader | None) -> None:
        """
        Sets a TransferReader to sort entities : it brings the Actor,
        which may change, while the TransferReader does not
        """

    def SetActor(self, act: nanoocp.Transfer.Transfer_ActorOfTransientProcess | None) -> None:
        """
        Sets a precise actor to sort entities
        This definition oversedes the creation with a TransferReader
        """

    def Actor(self) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """
        Returns the Actor used as precised one.
        Returns a Null Handle for a creation from a TransferReader
        without any further setting
        """

    def Reader(self) -> XSControl_TransferReader:
        """
        Returns the Reader (if created with a Reader)
        Returns a Null Handle if not created with a Reader
        """

    def Sort(self, rank: int, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> bool:
        """
        Returns True for an Entity which is recognized by the Actor,
        either the precised one, or the one defined by TransferReader
        """

    def ExtractLabel(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns a text defining the criterium : "Recognized for Transfer [(current actor)]\"
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_SignTransferStatus(nanoocp.IFSelect.IFSelect_Signature):
    """
    This Signatures gives the Transfer Status of an entity, as
    recorded in a TransferProcess. It can be :
    - Void : not recorded, or recorded as void with no message
    (attributes are not taken into account)
    - Warning : no result, warning message(s), no fail
    - Fail : no result, fail messages (with or without warning)
    - Result.. : result, no message (neither warning nor fail)
    Result.. i.e. Result:TypeName of the result
    - Result../Warning : result, with warning but no fail
    - Result../Fail : result, with fail (.e. bad result)
    - Fail on run : no result yet recorded, no message, but
    an exception occurred while recording the result
    (this should not appear and indicates a programming error)
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a SignTransferStatus, not initialised
        it gives nothing (empty string)
        """

    @overload
    def __init__(self, TR: XSControl_TransferReader | None) -> None:
        """
        Creates a SignTransferStatus, which will work on the current
        TransientProcess brought by the TransferReader (its MapReader)
        """

    @overload
    def __init__(self, theOther: XSControl_SignTransferStatus) -> None: ...

    def SetReader(self, TR: XSControl_TransferReader | None) -> None:
        """Sets a TransferReader to work"""

    def SetMap(self, TP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None:
        """
        Sets a precise map to sign entities
        This definition oversedes the creation with a TransferReader
        """

    def Map(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """
        Returns the TransientProcess used as precised one
        Returns a Null Handle for a creation from a TransferReader
        without any further setting
        """

    def Reader(self) -> XSControl_TransferReader:
        """
        Returns the Reader (if created with a Reader)
        Returns a Null Handle if not created with a Reader
        """

    def Value(self, ent: nanoocp.Standard.Standard_Transient | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> str:
        """
        Returns the Signature for a Transient object, as its transfer
        status
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_TransferReader(nanoocp.Standard.Standard_Transient):
    """
    A TransferReader performs, manages, handles results of,
    transfers done when reading a file (i.e. from entities of an
    InterfaceModel, to objects for Imagine)

    Running is organised around basic tools : TransientProcess and
    its Actor, results are Binders and CheckIterators. It implies
    control by a Controller (which prepares the Actor as required)

    Getting results can be done directly on TransientProcess, but
    these are immediate "last produced" results. Each transfer of
    an entity gives a final result, but also possible intermediate
    data, and checks, which can be attached to sub-entities.

    Hence, final results (which intermediates and checks) are
    recorded as ResultFromModel and can be queried individually.

    Some more direct access are given for results which are
    Transient or Shapes
    """

    @overload
    def __init__(self) -> None:
        """Creates a TransferReader, empty"""

    @overload
    def __init__(self, theOther: XSControl_TransferReader) -> None: ...

    def SetController(self, theControl: XSControl_Controller | None) -> None:
        """
        Sets a Controller. It is required to generate the Actor.
        Elsewhere, the Actor must be provided directly
        """

    def SetActor(self, theActor: nanoocp.Transfer.Transfer_ActorOfTransientProcess | None) -> None:
        """
        Sets the Actor directly : this value will be used if the
        Controller is not set
        """

    def Actor(self) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """
        Returns the Actor, determined by the Controller, or if this
        one is unknown, directly set.
        Once it has been defined, it can then be edited.
        """

    def SetModel(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Sets an InterfaceModel. This causes former results, computed
        from another one, to be lost (see also Clear)
        """

    def SetGraph(self, theGraph: nanoocp.Interface.Interface_HGraph | None) -> None:
        """Sets a Graph and its InterfaceModel (calls SetModel)"""

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the currently set InterfaceModel"""

    def SetContext(self, theName: str, theCtx: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Sets a Context : according to receiving appli, to be
        interpreted by the Actor
        """

    def GetContext(self, theName: str, theType: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns the Context attached to a name, if set and if it is
        Kind of the type, else a Null Handle
        Returns True if OK, False if no Context
        """

    def Context(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]:
        """
        Returns (modifiable) the whole definition of Context
        Rather for internal use (ex.: preparing and setting in once)
        """

    def SetFileName(self, theName: str) -> None:
        """Sets a new value for (loaded) file name"""

    def FileName(self) -> str:
        """Returns actual value of file name"""

    def Clear(self, theMode: int) -> None:
        """
        Clears data, according mode :
        -1 all
        0 nothing done
        +1 final results
        +2 working data (model, context, transfer process)
        """

    def TransientProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """
        Returns the currently used TransientProcess
        It is computed from the model by TransferReadRoots, or by
        BeginTransferRead
        """

    def SetTransientProcess(self, theTP: nanoocp.Transfer.Transfer_TransientProcess | None) -> None:
        """
        Forces the TransientProcess
        Remark : it also changes the Model and the Actor, from those
        recorded in the new TransientProcess
        """

    def RecordResult(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Records a final result of transferring an entity
        This result is recorded as a ResultFromModel, taken from
        the TransientProcess
        Returns True if a result is available, False else
        """

    def IsRecorded(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if a final result is recorded for an entity
        Remark that it can bring no effective result if transfer has
        completely failed (FinalResult brings only fail messages ...)
        """

    def HasResult(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if a final result is recorded AND BRINGS AN
        EFFECTIVE RESULT (else, it brings only fail messages)
        """

    def RecordedList(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities to which a final result is
        attached (i.e. processed by RecordResult)
        """

    def Skip(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Note that an entity has been required for transfer but no
        result at all is available (typically : case not implemented)
        It is not an error, but it gives a specific status : Skipped
        Returns True if done, False if <ent> is not in starting model
        """

    def IsSkipped(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """Returns True if an entity is noted as skipped"""

    def IsMarked(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Returns True if an entity has been asked for transfert, hence
        it is marked, as : Recorded (a computation has ran, with or
        without an effective result), or Skipped (case ignored)
        """

    def FinalResult(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Transfer.Transfer_ResultFromModel:
        """Returns the final result recorded for an entity, as such"""

    def FinalEntityLabel(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns the label attached to an entity recorded for final,
        or an empty string if not recorded
        """

    def FinalEntityNumber(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Returns the number attached to the entity recorded for final,
        or zero if not recorded (looks in the ResultFromModel)
        """

    def ResultFromNumber(self, theNum: int) -> nanoocp.Transfer.Transfer_ResultFromModel:
        """
        Returns the final result recorded for a NUMBER of entity
        (internal use). Null if out of range
        """

    def TransientResult(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the resulting object as a Transient
        Null Handle if no result or result not transient
        """

    def ShapeResult(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the resulting object as a Shape
        Null Shape if no result or result not a shape
        """

    def ClearResult(self, theEnt: nanoocp.Standard.Standard_Transient | None, theMode: int) -> bool:
        """
        Clears recorded result for an entity, according mode
        <mode> = -1 : true, complete, clearing (erasing result)
        <mode> >= 0 : simple "stripping", see ResultFromModel,
        in particular, 0 for simple internal strip,
        10 for all but final result,
        11 for all : just label, status and filename are kept
        Returns True when done, False if nothing was to clear
        """

    def EntityFromResult(self, theRes: nanoocp.Standard.Standard_Transient | None, theMode: int = 0) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an entity from which a given result was produced.
        If <mode> = 0 (D), searches in last root transfers
        If <mode> = 1,     searches in last (root & sub) transfers
        If <mode> = 2,     searches in root recorded results
        If <mode> = 3,     searches in all (root & sub) recordeds
        <res> can be, either a transient object (result itself) or
        a binder. For a binder of shape, calls EntityFromShapeResult
        Returns a Null Handle if <res> not recorded
        """

    def EntityFromShapeResult(self, theRes: nanoocp.TopoDS.TopoDS_Shape, theMode: int = 0) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an entity from which a given shape result was produced
        Returns a Null Handle if <res> not recorded or not a Shape
        """

    def EntitiesFromShapeList(self, theRes: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, theMode: int = 0) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities from which some shapes were
        produced : it corresponds to a loop on EntityFromShapeResult,
        but is optimised
        """

    def CheckList(self, theEnt: nanoocp.Standard.Standard_Transient | None, theLevel: int = 0) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the CheckList resulting from transferring <ent>, i.e.
        stored in its recorded form ResultFromModel
        (empty if transfer successful or not recorded ...)

        If <ent> is the Model, returns the complete cumulated
        check-list, <level> is ignored

        If <ent> is an entity of the Model, <level> applies as follows
        <level> : -1 for <ent> only, LAST transfer (TransientProcess)
        <level> : 0  for <ent> only (D)
        1  for <ent> and its immediate subtransfers, if any
        2  for <ent> and subtransferts at all levels
        """

    def HasChecks(self, theEnt: nanoocp.Standard.Standard_Transient | None, FailsOnly: bool) -> bool:
        """
        Returns True if an entity (with a final result) has checks :
        - failsonly = False : any kind of check message
        - failsonly = True  : fails only
        Returns False if <ent> is not recorded
        """

    def CheckedList(self, theEnt: nanoocp.Standard.Standard_Transient | None, WithCheck: nanoocp.Interface.Interface_CheckStatus = Interface_CheckStatus.Interface_CheckAny, theResult: bool = True) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of starting entities to which a given check
        status is attached, IN FINAL RESULTS
        <ent> can be an entity, or the model to query all entities
        Below, "entities" are, either <ent> plus its sub-transferred,
        or all the entities of the model

        <check> = -2 , all entities whatever the check (see result)
        <check> = -1 , entities with no fail (warning allowed)
        <check> =  0 , entities with no check at all
        <check> =  1 , entities with warning but no fail
        <check> =  2 , entities with fail
        <result> : if True, only entities with an attached result
        Remark : result True and check=0 will give an empty list
        """

    def BeginTransfer(self) -> bool:
        """
        Defines a new TransferProcess for reading transfer
        Returns True if done, False if data are not properly defined
        (the Model, the Actor for Read)
        """

    def Recognize(self, theEnt: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Tells if an entity is recognized as a valid candidate for
        Transfer. Calls method Recognize from the Actor (if known)
        """

    def TransferOne(self, theEnt: nanoocp.Standard.Standard_Transient | None, theRec: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Commands the transfer on reading for an entity to data for
        Imagine, using the selected Actor for Read
        Returns count of transferred entities, ok or with fails (0/1)
        If <rec> is True (D), the result is recorded by RecordResult
        """

    def TransferList(self, theList: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, theRec: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Commands the transfer on reading for a list of entities to
        data for Imagine, using the selected Actor for Read
        Returns count of transferred entities, ok or with fails (0/1)
        If <rec> is True (D), the results are recorded by RecordResult
        """

    def TransferRoots(self, theGraph: nanoocp.Interface.Interface_Graph, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Transfers the content of the current Interface Model to
        data handled by Imagine, starting from its Roots (determined
        by the Graph <G>), using the selected Actor for Read
        Returns the count of performed root transfers (i.e. 0 if none)
        or -1 if no actor is defined
        """

    def TransferClear(self, theEnt: nanoocp.Standard.Standard_Transient | None, theLevel: int = 0) -> None:
        """
        Clears the results attached to an entity
        if <ents> equates the starting model, clears all results
        """

    def PrintStats(self, theWhat: int, theMode: int = 0) -> str:
        """
        Prints statistics on current Trace File, according <what> and
        <mode>. See PrintStatsProcess for details
        """

    def LastCheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the CheckList resulting from last TransferRead
        i.e. from TransientProcess itself, recorded from last Clear
        """

    def LastTransferList(self, theRoots: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of entities recorded as lastly transferred
        i.e. from TransientProcess itself, recorded from last Clear
        If <roots> is True , considers only roots of transfer
        If <roots> is False, considers all entities bound with result
        """

    def ShapeResultList(self, theRec: bool) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns a list of result Shapes
        If <rec> is True , sees RecordedList
        If <rec> is False, sees LastTransferList (last ROOT transfers)
        For each one, if it is a Shape, it is cumulated to the list
        If no Shape is found, returns an empty Sequence
        """

    @staticmethod
    def PrintStatsProcess(theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theWhat: int, theMode: int = 0) -> None:
        """
        This routines prints statistics about a TransientProcess
        It can be called, by a TransferReader, or isolately
        Prints are done on the default trace file
        <what> defines what kind of statistics are to be printed :
        0 : basic figures
        1 : root results
        2 : all recorded (roots, intermediate, checked entities)
        3 : abnormal records
        4 : check messages (warnings and fails)
        5 : fail messages

        <mode> is used according <what> :
        <what> = 0 : <mode> is ignored
        <what> = 1,2,3 : <mode> as follows :
        0 (D) : just lists numbers of concerned entities in the model
        1 : for each entity, gives number,label, type and result
        type and/or status (fail/warning...)
        2 : for each entity, gives maximal information (i.e. checks)
        3 : counts per type of starting entity (class type)
        4 : counts per result type and/or status
        5 : counts per couple (starting type / result type/status)
        6 : idem plus gives for each item, the list of numbers of
        entities in the starting model

        <what> = 4,5 : modes relays on an enum PrintCount :
        0 (D) : ItemsByEntity (sequential list by entity)
        1 : CountByItem
        2 : ShortByItem       (count + 5 first numbers)
        3 : ListByItem        (count + entity numbers)
        4 : EntitiesByItem    (count + entity numbers and labels)
        """

    @staticmethod
    def PrintStatsOnList(theTP: nanoocp.Transfer.Transfer_TransientProcess | None, theList: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, theWhat: int, theMode: int = 0) -> None:
        """
        Works as PrintStatsProcess, but displays data only on the
        entities which are in <list> (filter)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_TransferWriter(nanoocp.Standard.Standard_Transient):
    """
    TransferWriter gives help to control transfer to write a file
    after having converted data from Cascade/Imagine

    It works with a Controller (which itself can work with an
    Actor to Write) and a FinderProcess. It records results and
    checks
    """

    @overload
    def __init__(self) -> None:
        """
        Creates a TransferWriter, empty, ready to run
        with an empty FinderProcess (but no controller, etc)
        """

    @overload
    def __init__(self, theOther: XSControl_TransferWriter) -> None: ...

    def FinderProcess(self) -> nanoocp.Transfer.Transfer_FinderProcess:
        """Returns the FinderProcess itself"""

    def SetFinderProcess(self, theFP: nanoocp.Transfer.Transfer_FinderProcess | None) -> None:
        """Sets a new FinderProcess and forgets the former one"""

    def Controller(self) -> XSControl_Controller:
        """Returns the currently used Controller"""

    def SetController(self, theCtl: XSControl_Controller | None) -> None:
        """Sets a new Controller, also sets a new FinderProcess"""

    def Clear(self, theMode: int) -> None:
        """
        Clears recorded data according a mode
        0 clears FinderProcess (results, checks)
        -1 create a new FinderProcess
        """

    def TransferMode(self) -> int:
        """
        Returns the current Transfer Mode (an Integer)
        It will be interpreted by the Controller to run Transfers
        This call form could be later replaced by more specific ones
        (parameters suited for each norm / transfer case)
        """

    def SetTransferMode(self, theMode: int) -> None:
        """Changes the Transfer Mode"""

    def PrintStats(self, theWhat: int, theMode: int = 0) -> None:
        """
        Prints statistics on current Trace File, according what,mode
        See PrintStatsProcess for details
        """

    def RecognizeTransient(self, theObj: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Tells if a transient object (from an application) is a valid
        candidate for a transfer to a model
        Asks the Controller (RecognizeWriteTransient)
        If <obj> is a HShape, calls RecognizeShape
        """

    def TransferWriteTransient(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None, theObj: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Transfers a Transient object (from an application) to a model
        of current norm, according to the last call to SetTransferMode
        Works by calling the Controller
        Returns status : =0 if OK, >0 if error during transfer, <0 if
        transfer badly initialised
        """

    def RecognizeShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape) -> bool:
        """
        Tells if a Shape is valid for a transfer to a model
        Asks the Controller (RecognizeWriteShape)
        """

    def TransferWriteShape(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Transfers a Shape from CasCade to a model of current norm,
        according to the last call to SetTransferMode
        Works by calling the Controller
        Returns status : =0 if OK, >0 if error during transfer, <0 if
        transfer badly initialised
        """

    def CheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list of last transfer (write), i.e. the
        check-list currently recorded in the FinderProcess
        """

    def ResultCheckList(self, theModel: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list of last transfer (write), but tries
        to bind to each check, the resulting entity in the model
        instead of keeping the original Mapper, whenever known
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_Utils:
    """
    This class provides various useful utility routines, to
    facilitate handling of most common data structures :
    transients (type, type name ...),
    strings (ascii or extended, pointed or handled or ...),
    shapes (reading, writing, testing ...),
    sequences & arrays (of strings, of transients, of shapes ...),
    ...

    Also it gives some helps on some data structures from XSTEP,
    such as printing on standard trace file, recignizing most
    currently used auxiliary types (Binder,Mapper ...)
    """

    @overload
    def __init__(self) -> None:
        """
        the only use of this, is to allow a frontal to get one
        distinct "Utils" set per separate engine
        """

    @overload
    def __init__(self, theOther: XSControl_Utils) -> None: ...

    def TraceLine(self, line: str) -> None:
        """
        Just prints a line into the current Trace File. This allows to
        better characterise the various trace outputs, as desired.
        """

    def TraceLines(self, lines: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Just prints a line or a set of lines into the current Trace
        File. <lines> can be a HAscii/ExtendedString (produces a print
        without ending line) or a HSequence or HArray1 Of ..
        (one new line per item)
        """

    def IsKind(self, item: nanoocp.Standard.Standard_Transient | None, what: nanoocp.Standard.Standard_Type | None) -> bool: ...

    def TypeName(self, item: nanoocp.Standard.Standard_Transient | None, nopk: bool = False) -> str:
        """
        Returns the name of the dynamic type of an object, i.e. :
        If it is a Type, its Name
        If it is a object not a type, the Name of its DynamicType
        If it is Null, an empty string
        If <nopk> is False (D), gives complete name
        If <nopk> is True, returns class name without package
        """

    def TraValue(self, list: nanoocp.Standard.Standard_Transient | None, num: int) -> nanoocp.Standard.Standard_Transient: ...

    def NewSeqTra(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]: ...

    def AppendTra(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, traval: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def DateString(self, yy: int, mm: int, dd: int, hh: int, mn: int, ss: int) -> str: ...

    def DateValues(self, text: str) -> tuple[int, int, int, int, int, int]: ...

    @overload
    def ToCString(self, strval: nanoocp.TCollection.TCollection_HAsciiString | None) -> str: ...

    @overload
    def ToCString(self, strval: nanoocp.TCollection.TCollection_AsciiString) -> str: ...

    @overload
    def ToHString(self, strcon: str) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @overload
    def ToHString(self, strcon: str) -> nanoocp.TCollection.TCollection_HExtendedString: ...

    def ToAString(self, strcon: str) -> nanoocp.TCollection.TCollection_AsciiString: ...

    @overload
    def ToEString(self, strval: nanoocp.TCollection.TCollection_HExtendedString | None) -> str: ...

    @overload
    def ToEString(self, strval: nanoocp.TCollection.TCollection_ExtendedString) -> str: ...

    def ToXString(self, strcon: str) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    def AsciiToExtended(self, str: str) -> str: ...

    def IsAscii(self, str: str) -> bool: ...

    def ExtendedToAscii(self, str: str) -> str: ...

    def CStrValue(self, list: nanoocp.Standard.Standard_Transient | None, num: int) -> str: ...

    def EStrValue(self, list: nanoocp.Standard.Standard_Transient | None, num: int) -> str: ...

    def NewSeqCStr(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def AppendCStr(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString] | None, strval: str) -> None: ...

    def NewSeqEStr(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HExtendedString]: ...

    def AppendEStr(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HExtendedString] | None, strval: str) -> None: ...

    def CompoundFromSeq(self, seqval: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """Converts a list of Shapes to a Compound (a kind of Shape)"""

    def ShapeType(self, shape: nanoocp.TopoDS.TopoDS_Shape, compound: bool) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """
        Returns the type of a Shape : true type if <compound> is False
        If <compound> is True and <shape> is a Compound, iterates on
        its items. If all are of the same type, returns this type.
        Else, returns COMPOUND. If it is empty, returns SHAPE
        For a Null Shape, returns SHAPE
        """

    def SortedCompound(self, shape: nanoocp.TopoDS.TopoDS_Shape, type: nanoocp.TopAbs.TopAbs_ShapeEnum, explore: bool, compound: bool) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        From a Shape, builds a Compound as follows :
        explores it level by level
        If <explore> is False, only COMPOUND items. Else, all items
        Adds to the result, shapes which comply to <type>
        + if <type> is WIRE, considers free edges (and makes wires)
        + if <type> is SHELL, considers free faces (and makes shells)
        If <compound> is True, gathers items in compounds which
        correspond to starting COMPOUND,SOLID or SHELL containers, or
        items directly contained in a Compound
        """

    def ShapeValue(self, seqv: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, num: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def NewSeqShape(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def AppendShape(self, seqv: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None, shape: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    def ShapeBinder(self, shape: nanoocp.TopoDS.TopoDS_Shape, hs: bool = True) -> nanoocp.Standard.Standard_Transient:
        """
        Creates a Transient Object from a Shape : it is either a Binder
        (used by functions which require a Transient but can process
        a Shape, such as viewing functions) or a HShape (according to hs)
        Default is a HShape
        """

    def BinderShape(self, tr: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        From a Transient, returns a Shape.
        In fact, recognizes ShapeBinder ShapeMapper and HShape
        """

    def SeqLength(self, list: nanoocp.Standard.Standard_Transient | None) -> int: ...

    def SeqToArr(self, seq: nanoocp.Standard.Standard_Transient | None, first: int = 1) -> nanoocp.Standard.Standard_Transient: ...

    def ArrToSeq(self, arr: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Transient: ...

    def SeqIntValue(self, list: nanoocp.NCollection.NCollection_HSequence[int] | None, num: int) -> int: ...

class XSControl_Vars(nanoocp.Standard.Standard_Transient):
    """
    Defines a receptacle for externally defined variables, each
    one has a name

    I.E. a WorkSession for XSTEP is generally used inside a
    context, which brings variables, especially shapes and
    geometries. For instance DRAW or an application engine

    This class provides a common form for this. It also provides
    a default implementation (locally recorded variables in a
    dictionary), but which is aimed to be redefined
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSControl_Vars) -> None: ...

    def Set(self, name: str, val: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetPoint(self, name: str, val: nanoocp.gp.gp_Pnt) -> None: ...

    def SetPoint2d(self, name: str, val: nanoocp.gp.gp_Pnt2d) -> None: ...

    def SetShape(self, name: str, val: nanoocp.TopoDS.TopoDS_Shape) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_WorkSession(nanoocp.IFSelect.IFSelect_WorkSession):
    """
    This WorkSession completes the basic one, by adding :
    - use of Controller, with norm selection...
    - management of transfers (both ways) with auxiliary classes
    TransferReader and TransferWriter
    -> these transfers may work with a Context List : its items
    are given by the user, according to the transfer to be
    i.e. it is interpreted by the Actors
    Each item is accessed by a Name
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: XSControl_WorkSession) -> None: ...

    def ClearData(self, theMode: int) -> None:
        """
        In addition to basic ClearData, clears Transfer and Management
        for interactive use, for mode = 0,1,2 and over 4
        Plus : mode = 5 to clear Transfers (both ways) only
        mode = 6 to clear enforced results
        mode = 7 to clear transfers, results
        """

    def SelectNorm(self, theNormName: str) -> bool:
        """
        Selects a Norm defined by its name.
        A Norm is described and handled by a Controller
        Returns True if done, False if <normname> is unknown

        The current Profile for this Norm is taken.
        """

    def SetController(self, theCtl: XSControl_Controller | None) -> None:
        """Selects a Norm defined by its Controller itself"""

    def SelectedNorm(self, theRsc: bool = False) -> str:
        """
        Returns the name of the last Selected Norm. If none is
        defined, returns an empty string
        By default, returns the complete name of the norm
        If <rsc> is True, returns the short name used for resource
        """

    def NormAdaptor(self) -> XSControl_Controller:
        """Returns the norm controller itself"""

    def Context(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]:
        """
        Returns the current Context List, Null if not defined
        The Context is given to the TransientProcess for TransferRead
        """

    def SetAllContext(self, theContext: nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]) -> None:
        """
        Sets the current Context List, as a whole
        Sets it to the TransferReader
        """

    def ClearContext(self) -> None:
        """Clears the whole current Context (nullifies it)"""

    def PrintTransferStatus(self, theNum: int, theWri: bool) -> tuple[bool, str]:
        """
        Prints the transfer status of a transferred item, as being
        the Mapped n0 <num>, from MapWriter if <wri> is True, or
        from MapReader if <wri> is False
        Returns True when done, False else (i.e. num out of range)
        """

    def InitTransferReader(self, theMode: int) -> None:
        """
        Sets a Transfer Reader, by internal ways, according mode :
        0 recreates it clear
        1 clears it (does not recreate)
        2 aligns Roots of TransientProcess from final Results
        3 aligns final Results from Roots of TransientProcess
        4 begins a new transfer (by BeginTransfer)
        5 recreates TransferReader then begins a new transfer
        """

    def SetTransferReader(self, theTR: XSControl_TransferReader | None) -> None:
        """Sets a Transfer Reader, which manages transfers on reading"""

    def TransferReader(self) -> XSControl_TransferReader:
        """Returns the Transfer Reader, Null if not set"""

    def MapReader(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """Returns the TransientProcess(internal data for TransferReader)"""

    def SetMapReader(self, theTP: nanoocp.Transfer.Transfer_TransientProcess | None) -> bool:
        """
        Changes the Map Reader, i.e. considers that the new one
        defines the relevant read results (forgets the former ones)
        Returns True when done, False in case of bad definition, i.e.
        if Model from TP differs from that of Session
        """

    def Result(self, theEnt: nanoocp.Standard.Standard_Transient | None, theMode: int) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the result attached to a starting entity
        If <mode> = 0, returns Final Result
        If <mode> = 1, considers Last Result
        If <mode> = 2, considers Final, else if absent, Last
        returns it as Transient, if result is not transient returns
        the Binder
        <mode> = 10,11,12 idem but returns the Binder itself
        (if it is not, e.g. Shape, returns the Binder)
        <mode> = 20, returns the ResultFromModel
        """

    def TransferReadOne(self, theEnts: nanoocp.Standard.Standard_Transient | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Commands the transfer of, either one entity, or a list
        I.E. calls the TransferReader after having analysed <ents>
        It is cumulated from the last BeginTransfer
        <ents> is processed by GiveList, hence :
        - <ents> a Selection : its SelectionResult
        - <ents> a HSequenceOfTransient : this list
        - <ents> the Model : in this specific case, all the roots,
        with no cumulation of former transfers (TransferReadRoots)
        """

    def TransferReadRoots(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> int:
        """
        Commands the transfer of all the root entities of the model
        i.e. calls TransferRoot from the TransferReader with the Graph
        No cumulation with former calls to TransferReadOne
        """

    def NewModel(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        produces and returns a new Model well conditioned
        It is produced by the Norm Controller
        It can be Null (if this function is not implemented)
        """

    def TransferWriter(self) -> XSControl_TransferWriter:
        """Returns the Transfer Reader, Null if not set"""

    def SetMapWriter(self, theFP: nanoocp.Transfer.Transfer_FinderProcess | None) -> bool:
        """
        Changes the Map Reader, i.e. considers that the new one
        defines the relevant read results (forgets the former ones)
        Returns True when done, False if <FP> is Null
        """

    def TransferWriteShape(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theCompGraph: bool = True, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """
        Transfers a Shape from CasCade to a model of current norm,
        according to the last call to SetModeWriteShape
        Returns status :Done if OK, Fail if error during transfer,
        Error if transfer badly initialised
        """

    def TransferWriteCheckList(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list of last transfer (write)
        It is recorded in the FinderProcess, but it must be bound with
        resulting entities (in the resulting file model) rather than
        with original objects (in fact, their mappers)
        """

    def Vars(self) -> XSControl_Vars: ...

    def SetVars(self, theVars: XSControl_Vars | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class XSControl_Writer:
    """
    This class gives a simple way to create then write a
    Model compliant to a given norm, from a Shape
    The model can then be edited by tools by other appropriate tools
    """

    @overload
    def __init__(self) -> None:
        """Creates a Writer from scratch"""

    @overload
    def __init__(self, norm: str) -> None:
        """
        Creates a Writer from scratch, with a norm name which
        identifie a Controller
        """

    @overload
    def __init__(self, WS: XSControl_WorkSession | None, scratch: bool = True) -> None:
        """
        Creates a Writer from an already existing Session
        If <scratch> is True (D), clears already recorded data
        """

    @overload
    def __init__(self, theOther: XSControl_Writer) -> None: ...

    def SetNorm(self, norm: str) -> bool:
        """
        Sets a specific norm to <me>
        Returns True if done, False if <norm> is not available
        """

    def SetWS(self, WS: XSControl_WorkSession | None, scratch: bool = True) -> None:
        """Sets a specific session to <me>"""

    def WS(self) -> XSControl_WorkSession:
        """Returns the session used in <me>"""

    def Model(self, newone: bool = False) -> nanoocp.Interface.Interface_InterfaceModel:
        """
        Returns the produced model. Produces a new one if not yet done
        or if <newone> is True
        This method allows for instance to edit product or header
        data before writing
        """

    def TransferShape(self, sh: nanoocp.TopoDS.TopoDS_Shape, mode: int = 0, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Transfers a Shape according to the mode"""

    def WriteFile(self, filename: str) -> nanoocp.IFSelect.IFSelect_ReturnStatus:
        """Writes the produced model"""

    def PrintStatsTransfer(self, what: int, mode: int = 0) -> None:
        """Prints Statistics about Transfer"""

# C++ typedef aliases
XSControl_WorkSessionMap = nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]
