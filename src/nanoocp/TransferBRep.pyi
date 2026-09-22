"""OCCT package TransferBRep (toolkit TKXSBase)"""

from typing import overload

import nanoocp.Interface
import nanoocp.Message
import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TopAbs
import nanoocp.TopoDS
import nanoocp.Transfer


class TransferBRep_TransferResultInfo(nanoocp.Standard.Standard_Transient):
    """
    Data structure for storing information on transfer result.
    At the moment it dispatches information for the following types:
    - result,
    - result + warning(s),
    - result + fail(s),
    - result + warning(s) + fail(s)
    - no result,
    - no result + warning(s),
    - no result + fail(s),
    - no result + warning(s) + fail(s),
    """

    @overload
    def __init__(self) -> None:
        """Creates object with all fields nullified."""

    @overload
    def __init__(self, theOther: TransferBRep_TransferResultInfo) -> None: ...

    def Clear(self) -> None:
        """Resets all the fields."""

    def Result(self) -> int: ...

    def SetResult(self, theValue: int) -> None:
        """Python addition: sets the value Result() returns by reference in C++."""

    def ResultWarning(self) -> int: ...

    def SetResultWarning(self, theValue: int) -> None:
        """
        Python addition: sets the value ResultWarning() returns by reference in C++.
        """

    def ResultFail(self) -> int: ...

    def SetResultFail(self, theValue: int) -> None:
        """
        Python addition: sets the value ResultFail() returns by reference in C++.
        """

    def ResultWarningFail(self) -> int: ...

    def SetResultWarningFail(self, theValue: int) -> None:
        """
        Python addition: sets the value ResultWarningFail() returns by reference in C++.
        """

    def NoResult(self) -> int: ...

    def SetNoResult(self, theValue: int) -> None:
        """
        Python addition: sets the value NoResult() returns by reference in C++.
        """

    def NoResultWarning(self) -> int: ...

    def SetNoResultWarning(self, theValue: int) -> None:
        """
        Python addition: sets the value NoResultWarning() returns by reference in C++.
        """

    def NoResultFail(self) -> int: ...

    def SetNoResultFail(self, theValue: int) -> None:
        """
        Python addition: sets the value NoResultFail() returns by reference in C++.
        """

    def NoResultWarningFail(self) -> int: ...

    def SetNoResultWarningFail(self, theValue: int) -> None:
        """
        Python addition: sets the value NoResultWarningFail() returns by reference in C++.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TransferBRep:
    """
    This package gathers services to simply read files and convert
    them to Shapes from CasCade. IE. it can be used in conjunction
    with purely CasCade software
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TransferBRep) -> None: ...

    @overload
    @staticmethod
    def ShapeResult(binder: nanoocp.Transfer.Transfer_Binder | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Get the Shape recorded in a Binder
        If the Binder brings a multiple result, search for the Shape
        """

    @overload
    @staticmethod
    def ShapeResult(TP: nanoocp.Transfer.Transfer_TransientProcess | None, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Get the Shape recorded in a TransientProcess as result of the
        Transfer of an entity. I.E. in the binder bound to that Entity
        If no result or result not a single Shape, returns a Null Shape
        """

    @staticmethod
    def SetShapeResult(TP: nanoocp.Transfer.Transfer_TransientProcess | None, ent: nanoocp.Standard.Standard_Transient | None, result: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Sets a Shape as a result for a starting entity <ent>
        (reverse of ShapeResult)
        It simply creates a ShapeBinder then binds it to the entity
        """

    @overload
    @staticmethod
    def Shapes(TP: nanoocp.Transfer.Transfer_TransientProcess | None, rootsonly: bool = True) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Gets the Shapes recorded in a TransientProcess as result of a
        Transfer, considers roots only or all results according
        <rootsonly>, returns them as a HSequence
        """

    @overload
    @staticmethod
    def Shapes(TP: nanoocp.Transfer.Transfer_TransientProcess | None, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Gets the Shapes recorded in a TransientProcess as result of a
        Transfer, for a given list of starting entities, returns
        the shapes as a HSequence
        """

    @staticmethod
    def ShapeState(FP: nanoocp.Transfer.Transfer_FinderProcess | None, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.TopAbs.TopAbs_Orientation:
        """
        Returns a Status regarding a Shape in a FinderProcess
        - FORWARD means bound with SAME Orientation
        - REVERSED means bound with REVERSE Orientation
        - EXTERNAL means NOT BOUND
        - INTERNAL is not used
        """

    @staticmethod
    def ResultFromShape(FP: nanoocp.Transfer.Transfer_FinderProcess | None, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Transfer.Transfer_Binder:
        """
        Returns the result (as a Binder) attached to a given Shape
        Null if none
        """

    @staticmethod
    def TransientFromShape(FP: nanoocp.Transfer.Transfer_FinderProcess | None, shape: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the result as pure Transient attached to a Shape
        first one if multiple result
        """

    @staticmethod
    def SetTransientFromShape(FP: nanoocp.Transfer.Transfer_FinderProcess | None, shape: nanoocp.TopoDS.TopoDS_Shape, result: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Binds a Transient Result to a Shape in a FinderProcess
        (as first result if multiple : does not add it to existing one)
        """

    @staticmethod
    def ShapeMapper(FP: nanoocp.Transfer.Transfer_FinderProcess | None, shape: nanoocp.TopoDS.TopoDS_Shape) -> TransferBRep_ShapeMapper:
        """
        Returns a ShapeMapper for a given Shape (location included)
        Either <shape> is already mapped, then its Mapper is returned
        Or it is not, then a new one is created then returned, BUT
        it is not mapped here (use Bind or FindElseBind to do this)
        """

    @overload
    @staticmethod
    def TransferResultInfo(TP: nanoocp.Transfer.Transfer_TransientProcess | None, EntityTypes: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TransferBRep.TransferBRep_TransferResultInfo]:
        """
        Fills sequence of TransferResultInfo for each type of entity
        given in the EntityTypes (entity are given as objects).
        Method IsKind applied to the entities in TP is used to
        compare with entities in EntityTypes.
        TopAbs_ShapeEnum).
        """

    @overload
    @staticmethod
    def TransferResultInfo(FP: nanoocp.Transfer.Transfer_FinderProcess | None, ShapeTypes: nanoocp.NCollection.NCollection_HSequence[int] | None) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TransferBRep.TransferBRep_TransferResultInfo]:
        """
        Fills sequence of TransferResultInfo for each type of shape
        given in the ShapeTypes (which are in fact considered as
        TopAbs_ShapeEnum).
        The Finders in the FP are considered as ShapeMappers.
        """

    @staticmethod
    def PrintResultInfo(Printer: nanoocp.Message.Message_Printer | None, Header: nanoocp.Message.Message_Msg, ResultInfo: TransferBRep_TransferResultInfo | None, printEmpty: bool = True) -> None:
        """Prints the results of transfer to given priner with given header."""

    @staticmethod
    def ResultCheckList(chl: nanoocp.Interface.Interface_CheckIterator, FP: nanoocp.Transfer.Transfer_FinderProcess | None, model: nanoocp.Interface.Interface_InterfaceModel | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Takes a starting CheckIterator which brings checks bound with
        starting objects (Shapes, Transient from an Imagine appli ...)
        and converts it to a CheckIterator in which checks are bound
        with results in an InterfaceModel
        Mapping is recorded in the FinderProcess
        Starting objects for which no individual result is recorded
        remain in their state
        """

    @staticmethod
    def Checked(chl: nanoocp.Interface.Interface_CheckIterator, alsoshapes: bool = False) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """
        Returns the list of objects to which a non-empty Check is
        bound in a check-list. Objects are transients, they can then
        be either Imagine objects entities for an Interface Norm.
        <alsoshapes> commands Shapes to be returned too
        (as ShapeMapper), see also CheckedShapes
        """

    @staticmethod
    def CheckedShapes(chl: nanoocp.Interface.Interface_CheckIterator) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """
        Returns the list of shapes to which a non-empty Check is bound
        in a check-list
        """

    @staticmethod
    def CheckObject(chl: nanoocp.Interface.Interface_CheckIterator, obj: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Returns the check-list bound to a given object, generally none
        (if OK) or one check. <obj> can be, either a true Transient
        object or entity, or a ShapeMapper, in that case the Shape is
        considered
        """

class TransferBRep_BinderOfShape(nanoocp.Transfer.Transfer_Binder):
    """
    Allows direct binding between a starting Object and the Result
    of its transfer when it is Unique.
    The Result itself is defined as a formal parameter <Shape from TopoDS>
    Warning : While it is possible to instantiate BinderOfShape with any Type
    for the Result, it is not advisable to instantiate it with
    Transient Classes, because such Results are directly known and
    managed by TransferProcess & Co, through
    SimpleBinderOfTransient : this class looks like instantiation
    of BinderOfShape, but its method ResultType
    is adapted (reads DynamicType of the Result)
    """

    @overload
    def __init__(self) -> None:
        """normal standard constructor, creates an empty BinderOfShape"""

    @overload
    def __init__(self, res: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        constructor which in the same time defines the result
        Returns True if a starting object is bound with SEVERAL
        results : Here, returns always False
        But it can have next results
        """

    @overload
    def __init__(self, theOther: TransferBRep_BinderOfShape) -> None: ...

    def ResultType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type permitted for the Result, i.e. the Type
        of the Parameter Class <Shape from TopoDS> (statically defined)
        """

    def ResultTypeName(self) -> str:
        """Returns the Type Name computed for the Result (dynamic)"""

    def SetResult(self, res: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Defines the Result"""

    def Result(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the defined Result, if there is one"""

    def CResult(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns the defined Result, if there is one, and allows to
        change it (avoids Result + SetResult).
        Admits that Result can be not yet defined
        Warning : a call to CResult causes Result to be known as defined
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TransferBRep_Reader:
    """
    This class offers a simple, easy to call, way of transferring
    data from interface files to Shapes from CasCade
    It must be specialized according to each norm/protocol, by :
    - defining how to read a file (specific method with protocol)
    - definig transfer, by providing an Actor
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a non-specialised Reader. Typically, for each norm
        or protocol, is will be required to define a specific Create
        to load a file and transfer it
        """

    @overload
    def __init__(self, theOther: TransferBRep_Reader) -> None: ...

    def SetProtocol(self, protocol: nanoocp.Interface.Interface_Protocol | None) -> None:
        """Records the protocol to be used for read and transfer roots"""

    def Protocol(self) -> nanoocp.Interface.Interface_Protocol:
        """Returns the recorded Protocol"""

    def SetActor(self, actor: nanoocp.Transfer.Transfer_ActorOfTransientProcess | None) -> None:
        """Records the actor to be used for transfers"""

    def Actor(self) -> nanoocp.Transfer.Transfer_ActorOfTransientProcess:
        """Returns the recorded Actor"""

    def SetFileStatus(self, status: int) -> None:
        """
        Sets File Status to be interpreted as follows :
        = 0 OK
        < 0 file not found
        > 0 read error, no Model could be created
        """

    def FileStatus(self) -> int:
        """Returns the File Status"""

    def FileNotFound(self) -> bool:
        """Returns True if FileStatus is for FileNotFound"""

    def SyntaxError(self) -> bool:
        """
        Returns True if FileStatus is for Error during read
        (major error; for local error, see CheckModel)
        """

    def SetModel(self, model: nanoocp.Interface.Interface_InterfaceModel | None) -> None:
        """
        Specifies a Model to work on
        Also clears the result and Done status
        """

    def Model(self) -> nanoocp.Interface.Interface_InterfaceModel:
        """Returns the Model to be worked on"""

    def Clear(self) -> None:
        """clears the result and Done status. But not the Model."""

    def CheckStatusModel(self, withprint: bool) -> bool:
        """
        Checks the Model. Returns True if there is NO FAIL at all
        (regardless Warnings)
        If <withprint> is True, also sends Checks on standard output
        """

    def CheckListModel(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Checks the Model (complete : syntax + semantic) and returns
        the produced Check List
        """

    def ModeNewTransfer(self) -> bool:
        """
        Returns (by Reference, hence can be changed) the Mode for new
        Transfer : True (D) means that each new Transfer produces a
        new TransferProcess. Else keeps the original one but each
        Transfer clears its (former results are not kept)
        """

    def SetModeNewTransfer(self, theValue: bool) -> None:
        """
        Python addition: sets the value ModeNewTransfer() returns by reference in C++.
        """

    def BeginTransfer(self) -> bool:
        """
        Initializes the Reader for a Transfer (one,roots, or list)
        Also calls PrepareTransfer
        Returns True when done, False if could not be done
        """

    def EndTransfer(self) -> None:
        """Ebds a Transfer (one, roots or list) by recording its result"""

    def PrepareTransfer(self) -> None:
        """
        Prepares the Transfer. Also can act on the Actor or change the
        TransientProcess if required.
        Should not set the Actor into the TransientProcess, it is done
        by caller. The provided default does nothing.
        """

    def TransferRoots(self, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Transfers all Root Entities which are recognized as Geom-Topol
        The result will be a list of Shapes.
        This method calls user redefinable PrepareTransfer
        Remark : former result is cleared
        """

    def Transfer(self, num: int, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Transfers an Entity given its rank in the Model (Root or not)
        Returns True if it is recognized as Geom-Topol.
        (But it can have failed : see IsDone)
        """

    def TransferList(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient] | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Transfers a list of Entities (only the ones also in the Model)
        Remark : former result is cleared
        """

    def IsDone(self) -> bool:
        """Returns True if the LAST Transfer/TransferRoots was a success"""

    def NbShapes(self) -> int:
        """Returns the count of produced Shapes (roots)"""

    def Shapes(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]:
        """Returns the complete list of produced Shapes"""

    def Shape(self, num: int = 1) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns a Shape given its rank, by default the first one"""

    def ShapeResult(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a Shape produced from a given entity (if it was
        individually transferred or if an intermediate result is
        known). If no Shape is bound with <ent>, returns a Null Shape
        Warning : Runs on the last call to Transfer,TransferRoots,TransferList
        """

    def OneShape(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """
        Returns a unique Shape for the result :
        - a void Shape (type = SHAPE) if result is empty
        - a simple Shape if result has only one : returns this one
        - a Compound if result has more than one Shape
        """

    def NbTransients(self) -> int:
        """Returns the count of produced Transient Results (roots)"""

    def Transients(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Standard.Standard_Transient]:
        """Returns the complete list of produced Transient Results"""

    def Transient(self, num: int = 1) -> nanoocp.Standard.Standard_Transient:
        """
        Returns a Transient Root Result, given its rank (by default
        the first one)
        """

    def CheckStatusResult(self, withprints: bool) -> bool:
        """
        Checks the Result of last Transfer (individual or roots, no
        cumulation on several transfers). Returns True if NO fail
        occurred during Transfer (queries the TransientProcess)
        """

    def CheckListResult(self) -> nanoocp.Interface.Interface_CheckIterator:
        """
        Checks the Result of last Transfer (individual or roots, no
        cumulation on several transfers) and returns the produced list
        """

    def TransientProcess(self) -> nanoocp.Transfer.Transfer_TransientProcess:
        """
        Returns the TransientProcess. It records information about
        the very last transfer done. Null if no transfer yet done.
        Can be used for queries more accurate than the default ones.
        """

class TransferBRep_ShapeBinder(TransferBRep_BinderOfShape):
    """
    A ShapeBinder is a BinderOfShape with some additional services
    to cast the Result under various kinds of Shapes
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty ShapeBinder"""

    @overload
    def __init__(self, res: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Creates a ShapeBinder with a result"""

    @overload
    def __init__(self, theOther: TransferBRep_ShapeBinder) -> None: ...

    def ShapeType(self) -> nanoocp.TopAbs.TopAbs_ShapeEnum:
        """Returns the Type of the Shape Result (under TopAbs form)"""

    def Vertex(self) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Edge(self) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Wire(self) -> nanoocp.TopoDS.TopoDS_Wire: ...

    def Face(self) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Shell(self) -> nanoocp.TopoDS.TopoDS_Shell: ...

    def Solid(self) -> nanoocp.TopoDS.TopoDS_Solid: ...

    def CompSolid(self) -> nanoocp.TopoDS.TopoDS_CompSolid: ...

    def Compound(self) -> nanoocp.TopoDS.TopoDS_Compound: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TransferBRep_ShapeInfo:
    """
    Gives information on an object, see template DataInfo
    This class is for Shape
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TransferBRep_ShapeInfo) -> None: ...

    @staticmethod
    def Type(ent: nanoocp.TopoDS.TopoDS_Shape) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type attached to an object
        Here, TShape (Shape has no Dynamic Type)
        """

    @staticmethod
    def TypeName(ent: nanoocp.TopoDS.TopoDS_Shape) -> str:
        """
        Returns Type Name (string)
        Here, the true name of the Type of a Shape
        """

class TransferBRep_ShapeListBinder(nanoocp.Transfer.Transfer_Binder):
    """
    This binder binds several (a list of) shapes with a starting
    entity, when this entity itself corresponds to a simple list
    of shapes. Each part is not seen as a sub-result of an
    independent component, but as an item of a built-in list
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, list: nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape] | None) -> None: ...

    @overload
    def __init__(self, theOther: TransferBRep_ShapeListBinder) -> None: ...

    def IsMultiple(self) -> bool: ...

    def ResultType(self) -> nanoocp.Standard.Standard_Type: ...

    def ResultTypeName(self) -> str: ...

    def AddResult(self, res: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Adds an item to the result list"""

    def Result(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TopoDS.TopoDS_Shape]: ...

    def SetResult(self, num: int, res: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """Changes an already defined sub-result"""

    def NbShapes(self) -> int: ...

    def Shape(self, num: int) -> nanoocp.TopoDS.TopoDS_Shape: ...

    def ShapeType(self, num: int) -> nanoocp.TopAbs.TopAbs_ShapeEnum: ...

    def Vertex(self, num: int) -> nanoocp.TopoDS.TopoDS_Vertex: ...

    def Edge(self, num: int) -> nanoocp.TopoDS.TopoDS_Edge: ...

    def Wire(self, num: int) -> nanoocp.TopoDS.TopoDS_Wire: ...

    def Face(self, num: int) -> nanoocp.TopoDS.TopoDS_Face: ...

    def Shell(self, num: int) -> nanoocp.TopoDS.TopoDS_Shell: ...

    def Solid(self, num: int) -> nanoocp.TopoDS.TopoDS_Solid: ...

    def CompSolid(self, num: int) -> nanoocp.TopoDS.TopoDS_CompSolid: ...

    def Compound(self, num: int) -> nanoocp.TopoDS.TopoDS_Compound: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TransferBRep_ShapeMapper(nanoocp.Transfer.Transfer_Finder):
    @overload
    def __init__(self, akey: nanoocp.TopoDS.TopoDS_Shape) -> None:
        """
        Creates a Mapper with a Value. This Value can then not be
        changed. It is used by the Hasher to compute the HashCode,
        which will then be stored for an immediate reading.
        """

    @overload
    def __init__(self, theOther: TransferBRep_ShapeMapper) -> None: ...

    def Value(self) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns the contained value"""

    def Equates(self, other: nanoocp.Transfer.Transfer_Finder | None) -> bool:
        """
        Specific test of equality : defined as False if <other> has
        not the same true Type, else contents are compared (by
        C++ operator ==)
        """

    def ValueType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type of the Value. By default, returns the
        DynamicType of <me>, but can be redefined
        """

    def ValueTypeName(self) -> str:
        """
        Returns the name of the Type of the Value. Default is name
        of ValueType, unless it is for a non-handled object
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TransferBRep
TransferBRep_HSequenceOfTransferResultInfo = nanoocp.NCollection.NCollection_HSequence[nanoocp.TransferBRep.TransferBRep_TransferResultInfo]
TransferBRep_SequenceOfTransferResultInfo = nanoocp.NCollection.NCollection_Sequence[nanoocp.TransferBRep.TransferBRep_TransferResultInfo]
