"""OCCT package MoniTool (toolkit TKXSBase)"""

import enum
from typing import overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Standard
import nanoocp.TCollection
import nanoocp.TopoDS
import nanoocp.gp


class MoniTool_ValueType(enum.IntEnum):
    MoniTool_ValueMisc = 0

    MoniTool_ValueInteger = 1

    MoniTool_ValueReal = 2

    MoniTool_ValueIdent = 3

    MoniTool_ValueVoid = 4

    MoniTool_ValueText = 5

    MoniTool_ValueEnum = 6

    MoniTool_ValueLogical = 7

    MoniTool_ValueSub = 8

    MoniTool_ValueHexa = 9

    MoniTool_ValueBinary = 10

MoniTool_ValueMisc: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueMisc

MoniTool_ValueInteger: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueInteger

MoniTool_ValueReal: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueReal

MoniTool_ValueIdent: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueIdent

MoniTool_ValueVoid: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueVoid

MoniTool_ValueText: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueText

MoniTool_ValueEnum: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueEnum

MoniTool_ValueLogical: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueLogical

MoniTool_ValueSub: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueSub

MoniTool_ValueHexa: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueHexa

MoniTool_ValueBinary: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueBinary

class MoniTool_AttrList:
    """
    a AttrList allows to record a list of attributes as Transients
    which can be edited, changed ...
    Each one is identified by a name
    """

    @overload
    def __init__(self) -> None:
        """Creates an AttrList, empty"""

    @overload
    def __init__(self, other: MoniTool_AttrList) -> None:
        """
        Creates an AttrList from another one, definitions are shared
        (calls SameAttributes)
        """

    def SetAttribute(self, name: str, val: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Adds an attribute with a given name (replaces the former one
        with the same name if already exists)
        """

    def RemoveAttribute(self, name: str) -> bool:
        """
        Removes an attribute
        Returns True when done, False if this attribute did not exist
        """

    def GetAttribute(self, name: str, type: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns an attribute from its name, filtered by a type
        If no attribute has this name, or if it is not kind of this
        type, <val> is Null and returned value is False
        Else, it is True
        """

    def Attribute(self, name: str) -> nanoocp.Standard.Standard_Transient:
        """
        Returns an attribute from its name. Null Handle if not
        recorded (whatever Transient, Integer, Real ...)
        Integer is recorded as IntVal
        Real is recorded as RealVal
        Text is recorded as HAsciiString
        """

    def AttributeType(self, name: str) -> MoniTool_ValueType:
        """
        Returns the type of an attribute:
        ValueInt, ValueReal, ValueText (String), ValueIdent (any)
        or ValueVoid (not recorded)
        """

    def SetIntegerAttribute(self, name: str, val: int) -> None:
        """Adds an integer value for an attribute"""

    def GetIntegerAttribute(self, name: str) -> tuple[bool, int]:
        """
        Returns an attribute from its name, as integer
        If no attribute has this name, or not an integer,
        <val> is 0 and returned value is False
        Else, it is True
        """

    def IntegerAttribute(self, name: str) -> int:
        """Returns an integer attribute from its name. 0 if not recorded"""

    def SetRealAttribute(self, name: str, val: float) -> None:
        """Adds a real value for an attribute"""

    def GetRealAttribute(self, name: str) -> tuple[bool, float]:
        """
        Returns an attribute from its name, as real
        If no attribute has this name, or not a real
        <val> is 0.0 and returned value is False
        Else, it is True
        """

    def RealAttribute(self, name: str) -> float:
        """Returns a real attribute from its name. 0.0 if not recorded"""

    def SetStringAttribute(self, name: str, val: str) -> None:
        """Adds a String value for an attribute"""

    def StringAttribute(self, name: str) -> str:
        """Returns a String attribute from its name. "" if not recorded"""

    def AttrList(self) -> nanoocp.NCollection.NCollection_DataMap[nanoocp.TCollection.TCollection_AsciiString, nanoocp.Standard.Standard_Transient]:
        """Returns the exhaustive list of attributes"""

    def SameAttributes(self, other: MoniTool_AttrList) -> None:
        """
        Gets the list of attributes from <other>, as such, i.e.
        not copied : attributes are shared, any attribute edited,
        added, or removed in <other> is also in <me> and vice versa
        The former list of attributes of <me> is dropped
        """

    def GetAttributes(self, other: MoniTool_AttrList, fromname: str = '', copied: bool = True) -> None:
        """
        Gets the list of attributes from <other>, by copying it
        By default, considers all the attributes from <other>
        If <fromname> is given, considers only the attributes with
        name beginning by <fromname>

        For each attribute, if <copied> is True (D), its value is also
        copied if it is a basic type (Integer,Real,String), else it
        remains shared between <other> and <me>

        These new attributes are added to the existing ones in <me>,
        in case of same name, they replace the existing ones
        """

class MoniTool_CaseData(nanoocp.Standard.Standard_Transient):
    """
    This class is intended to record data attached to a case to be
    exploited.
    Cases can be :
    * internal, i.e. for immediate debug
    for instance, on an abnormal exception, fill a CaseData
    in a DB (see class DB) then look at its content by XSDRAW
    * to record abnormal situation, which cause a warning or fail
    message, for instance during a transfer
    This will allow, firstly to build a more comprehensive
    message (with associated data), secondly to help seeing
    "what happened"
    * to record data in order to fix a problem
    If a CASE is well defined and its fix is well known too,
    recording a CaseData which identifies the CASE will allow
    to furstherly call the appropriate fix routine

    A CaseData is defined by
    * an optional CASE identifier
    If it is defined, this will allow systematic exploitation
    such as calling a fix routine
    * an optional Check Status, Warning or Fail, else it is Info
    * a NAME : it just allows to identify where this CaseData was
    created (help to debug)
    * a LIST OF DATA

    Each Data has a type (integer, real etc...) and can have a name
    Hence, each data may be identified by :
    * its absolute rank (from 1 to NbData)
    * its name if it has one (exact matching)
    * else, an interpreted identifier, which gives the type and
    the rank in the type (for instance, first integer; etc)
    (See NameRank)
    """

    @overload
    def __init__(self, caseid: str = '', name: str = '') -> None:
        """
        Creates a CaseData with a CaseId and a Name
        (by default not defined)
        """

    @overload
    def __init__(self, theOther: MoniTool_CaseData) -> None: ...

    def SetCaseId(self, caseid: str) -> None:
        """Sets a CaseId"""

    def SetName(self, name: str) -> None:
        """Sets a Name"""

    def CaseId(self) -> str:
        """Returns the CaseId"""

    @overload
    def Name(self) -> str:
        """Returns the Name"""

    @overload
    def Name(self, nd: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the name of a data. If it has no name, the string is
        empty (length = 0)
        """

    def IsCheck(self) -> bool:
        """Tells if <me> is Check (Warning or Fail), else it is Info"""

    def IsWarning(self) -> bool:
        """Tells if <me> is Warning"""

    def IsFail(self) -> bool:
        """Tells if <me> is Fail"""

    def ResetCheck(self) -> None:
        """Resets Check Status, i.e. sets <me> as Info"""

    def SetWarning(self) -> None:
        """Sets <me> as Warning"""

    def SetFail(self) -> None:
        """Sets <me> as Fail"""

    def SetChange(self) -> None:
        """
        Sets the next Add... not to add but to change the data item
        designated by its name.
        If next Add... is not called with a name, SetChange is ignored
        Reset by next Add... , whatever <num> is correct or not
        """

    def SetReplace(self, num: int) -> None:
        """
        Sets the next Add... not to add but to replace the data item
        <num>, if <num> is between 1 and NbData.
        Reset by next Add... , whatever <num> is correct or not
        """

    def AddData(self, val: nanoocp.Standard.Standard_Transient | None, kind: int, name: str = '') -> None:
        """Unitary adding a data; rather internal"""

    def AddRaised(self, theException: "Standard_Failure", name: str = '') -> None:
        """Adds the currently caught exception"""

    def AddShape(self, sh: nanoocp.TopoDS.TopoDS_Shape, name: str = '') -> None:
        """Adds a Shape (recorded as a HShape)"""

    def AddXYZ(self, aXYZ: nanoocp.gp.gp_XYZ, name: str = '') -> None:
        """Adds a XYZ"""

    def AddXY(self, aXY: nanoocp.gp.gp_XY, name: str = '') -> None:
        """Adds a XY"""

    def AddReal(self, val: float, name: str = '') -> None:
        """Adds a Real"""

    def AddReals(self, v1: float, v2: float, name: str = '') -> None:
        """Adds two reals (for instance, two parameters)"""

    def AddCPU(self, lastCPU: float, curCPU: float = 0.0, name: str = '') -> None:
        """
        Adds the CPU time between lastCPU and now
        if <curCPU> is given, the CPU amount is curCPU-lastCPU
        else it is currently measured CPU - lastCPU
        lastCPU has been read by call to GetCPU
        See GetCPU to get amount, and LargeCPU to test large amount
        """

    def GetCPU(self) -> float:
        """
        Returns the current amount of CPU
        This allows to laterly test and record CPU amount
        Its value has to be given to LargeCPU and AddCPU
        """

    def LargeCPU(self, maxCPU: float, lastCPU: float, curCPU: float = 0.0) -> bool:
        """
        Tells if a CPU time amount is large
        <maxCPU>  gives the amount over which an amount is large
        <lastCPU> gives the start CPU amount
        if <curCPU> is given, the tested CPU amount is curCPU-lastCPU
        else it is currently measured CPU - lastCPU
        """

    def AddGeom(self, geom: nanoocp.Standard.Standard_Transient | None, name: str = '') -> None:
        """Adds a Geometric as a Transient (Curve, Surface ...)"""

    def AddEntity(self, ent: nanoocp.Standard.Standard_Transient | None, name: str = '') -> None:
        """
        Adds a Transient, as an Entity from an InterfaceModel for
        instance : it will then be printed with the help of a DBPE
        """

    def AddText(self, text: str, name: str = '') -> None:
        """Adds a Text (as HAsciiString)"""

    def AddInteger(self, val: int, name: str = '') -> None:
        """Adds an Integer"""

    def AddAny(self, val: nanoocp.Standard.Standard_Transient | None, name: str = '') -> None:
        """Adds a Transient, with no more meaning"""

    def RemoveData(self, num: int) -> None:
        """Removes a Data from its rank. Does nothing if out of range"""

    def NbData(self) -> int:
        """Returns the count of data recorded to a set"""

    def Data(self, nd: int) -> nanoocp.Standard.Standard_Transient:
        """Returns a data item (n0 <nd> in the set <num>)"""

    def GetData(self, nd: int, type: nanoocp.Standard.Standard_Type | None) -> tuple[bool, nanoocp.Standard.Standard_Transient]:
        """
        Returns a data item, under control of a Type
        If the data item is kind of this type, it is returned in <val>
        and the returned value is True
        Else, <val> is unchanged and the returned value is False
        """

    def Kind(self, nd: int) -> int:
        """
        Returns the kind of a data :
        KIND TYPE      MEANING
        0  ANY       any (not one of the following)
        1  EX        raised exception
        2  EN        entity
        3  G         geom
        4  SH        shape
        5  XYZ       XYZ
        6  XY or UV  XY
        7  RR        2 reals
        8  R         1 real
        9  CPU       CPU (1 real)
        10 T         text
        11 I         integer

        For NameNum, these codes for TYPE must be given exact
        i.e. SH for a Shape, not S nor SHAPE nor SOLID etc
        """

    def NameNum(self, name: str) -> int:
        """
        Returns the first suitable data rank for a given name
        Exact matching (exact case, no completion) is required
        Firstly checks the recorded names
        If not found, considers the name as follows :
        Name = "TYPE" : search for the first item with this TYPE
        Name = "TYPE:nn" : search for the nn.th item with this TYPE
        See allowed values in method Kind
        """

    def Shape(self, nd: int) -> nanoocp.TopoDS.TopoDS_Shape:
        """Returns a data as a shape, Null if not a shape"""

    def XYZ(self, nd: int, val: nanoocp.gp.gp_XYZ) -> bool:
        """
        Returns a data as a XYZ (i.e. Geom_CartesianPoint)
        Returns False if not the good type
        """

    def XY(self, nd: int, val: nanoocp.gp.gp_XY) -> bool:
        """
        Returns a data as a XY (i.e. Geom2d_CartesianPoint)
        Returns False if not the good type
        """

    def Reals(self, nd: int) -> tuple[bool, float, float]:
        """Returns a couple of reals (stored in Geom2d_CartesianPoint)"""

    def Real(self, nd: int) -> tuple[bool, float]:
        """
        Returns a real or CPU amount (stored in Geom2d_CartesianPoint)
        (allows an Integer converted to a Real)
        """

    def Integer(self, nd: int) -> tuple[bool, int]:
        """Returns an Integer"""

    def Msg(self) -> nanoocp.Message.Message_Msg:
        """
        Returns a Msg from a CaseData : it is build from DefMsg, which
        gives the message code plus the designation of items of the
        CaseData to be added to the Msg
        Empty if no message attached

        Remains to be implemented
        """

    @staticmethod
    def SetDefWarning(acode: str) -> None:
        """Sets a Code to give a Warning"""

    @staticmethod
    def SetDefFail(acode: str) -> None:
        """Sets a Code to give a Fail"""

    @staticmethod
    def DefCheck(acode: str) -> int:
        """
        Returns Check Status for a Code : 0 non/info (default),
        1 warning, 2 fail

        Remark : DefCheck is used to set the check status of a
        CaseData when it is attached to a case code, it can be changed
        later (by SetFail, SetWarning, ResetCheck)
        """

    @staticmethod
    def SetDefMsg(casecode: str, mesdef: str) -> None:
        """
        Attaches a message definition to a case code
        This definition includes the message code plus designation of
        items of the CaseData to be added to the message (this part
        not yet implemented)
        """

    @staticmethod
    def DefMsg(casecode: str) -> str:
        """
        Returns the message definition for a case code
        Empty if no message attached
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_DataInfo:
    """
    Gives information on an object
    Used as template to instantiate Elem, etc
    This class is for Transient
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MoniTool_DataInfo) -> None: ...

    @staticmethod
    def Type(ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.Standard.Standard_Type:
        """
        Returns the Type attached to an object
        Here, the Dynamic Type of a Transient. Null Type if unknown
        """

    @staticmethod
    def TypeName(ent: nanoocp.Standard.Standard_Transient | None) -> str:
        """
        Returns Type Name (string)
        Allows to name type of non-handled objects
        """

class MoniTool_Element(nanoocp.Standard.Standard_Transient):
    """
    a Element allows to map any kind of object as a Key for a Map.
    This works by defining, for a Hash Code, that of the real Key,
    not of the Element which acts only as an intermediate.
    When a Map asks for the HashCode of a Element, this one returns
    the code it has determined at creation time
    """

    def GetHashCode(self) -> int:
        """
        Returns the HashCode which has been stored by SetHashCode
        (remark that HashCode could be deferred then be defined by
        sub-classes, the result is the same)
        """

    def Equates(self, other: MoniTool_Element | None) -> bool:
        """
        Specific testof equality : to be defined by each sub-class,
        must be False if Elements have not the same true Type, else
        their contents must be compared
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

    def ListAttr(self) -> MoniTool_AttrList:
        """Returns (readonly) the Attribute List"""

    def ChangeAttr(self) -> MoniTool_AttrList:
        """Returns (modifiable) the Attribute List"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_IntVal(nanoocp.Standard.Standard_Transient):
    """An Integer through a Handle (i.e. managed as TShared)"""

    @overload
    def __init__(self, val: int = 0) -> None: ...

    @overload
    def __init__(self, theOther: MoniTool_IntVal) -> None: ...

    def Value(self) -> int: ...

    def CValue(self) -> int: ...

    def SetCValue(self, theValue: int) -> None:
        """Python addition: sets the value CValue() returns by reference in C++."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_RealVal(nanoocp.Standard.Standard_Transient):
    """A Real through a Handle (i.e. managed as TShared)"""

    @overload
    def __init__(self, val: float = 0.0) -> None: ...

    @overload
    def __init__(self, theOther: MoniTool_RealVal) -> None: ...

    def Value(self) -> float: ...

    def CValue(self) -> float: ...

    def SetCValue(self, theValue: float) -> None:
        """Python addition: sets the value CValue() returns by reference in C++."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_SignText(nanoocp.Standard.Standard_Transient):
    """
    Provides the basic service to get a text which identifies
    an object in a context
    It can be used for other classes (general signatures ...)
    It can also be used to build a message in which an object
    is to be identified
    """

    def Name(self) -> str:
        """
        Returns an identification of the Signature (a word), given at
        initialization time
        """

    def TextAlone(self, ent: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gives a text as a signature for a transient object alone, i.e.
        without defined context.
        By default, calls Text with undefined context (Null Handle) and
        if empty, then returns DynamicType
        """

    def Text(self, ent: nanoocp.Standard.Standard_Transient | None, context: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Gives a text as a signature for a transient object in a context
        If the context is senseless, it can be given as Null Handle
        empty result if nothing to give (at least the DynamicType could
        be sent ?)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_SignShape(MoniTool_SignText):
    """
    Signs HShape according to its real content (type of Shape)
    Context is not used
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: MoniTool_SignShape) -> None: ...

    def Name(self) -> str:
        """Returns "SHAPE\""""

    def Text(self, ent: nanoocp.Standard.Standard_Transient | None, context: nanoocp.Standard.Standard_Transient | None) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns for a HShape, the string of its ShapeEnum
        The Model is absolutely useless (may be null)
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_Stat:
    """
    This class manages Statistics to be queried asynchronously.

    It is organized as a stack of counters, identified by their
    levels, from one to ... . Each one has a total account of
    items to be counted, a count of already passed items, plus a
    count of "current items". The counters of higher level play on
    these current items.
    For instance, if a counter has been opened for 100 items, 40
    already passed, 20 current, its own percent is 40, but there
    is the contribution of higher level counters, rated for 20 %
    of this counter.

    Hence, a counter is opened, items are added. Also items can be
    add for sub-counter (of higher level), they will be added
    definitively when the sub-counter will be closed. When the
    count has ended, this counter is closed, the counter of
    lower level cumulates it and goes on. As follows :

    Way of use :
    Open(nbitems);
    Add(..)  :  direct adding
    Add(..)
    AddSub (nsub)  :  for sub-counter
    Open (nbsubs)  :  nbsubs for this sub-counter
    Add (..)
    Close        : the sub-counter
    AddEnd()
    etc...
    Close          : the starting counter

    This means that a counter can be opened in a Stat, regardless
    to the already opened ones :: this will be cumulated

    A Current Stat is available, but it is possible to have others
    """

    @overload
    def __init__(self, title: str = '') -> None:
        """
        Creates a Stat form. At start, one default phase is defined,
        with one default step. Then, it suffises to start with a
        count of items (and cycles if several) then record items,
        to have a queryable report.
        """

    @overload
    def __init__(self, other: MoniTool_Stat) -> None:
        """used when starting"""

    @staticmethod
    def Current() -> MoniTool_Stat: ...

    def Open(self, nb: int = 100) -> int:
        """Opens a new counter with a starting count of items"""

    def OpenMore(self, id: int, nb: int) -> None:
        """Adds more items to be counted by Add... on current level"""

    def Add(self, nb: int = 1) -> None:
        """Directly adds items"""

    def AddSub(self, nb: int = 1) -> None:
        """
        Declares a count of items to be added later. If a sub-counter
        is opened, its percentage multiplies this sub-count to compute
        the percent of current level
        """

    def AddEnd(self) -> None:
        """Ends the AddSub and cumulates the sub-count to current level"""

    def Close(self, id: int) -> None: ...

    def Level(self) -> int: ...

    def Percent(self, fromlev: int = 0) -> float: ...

class MoniTool_Timer(nanoocp.Standard.Standard_Transient):
    """
    Provides convenient service on global timers
    accessed by string name, mostly aimed for debugging purposes

    As an instance, envelopes the OSD_Timer to have it as Handle

    As a tool, supports static dictionary of timers
    and provides static methods to easily access them
    """

    @overload
    def __init__(self) -> None:
        """Create timer in empty state"""

    @overload
    def __init__(self, theOther: MoniTool_Timer) -> None: ...

    def Timer(self) -> nanoocp.OSD.OSD_Timer:
        """Return reference to embedded OSD_Timer"""

    def Start(self) -> None: ...

    def Stop(self) -> None: ...

    def Reset(self) -> None:
        """
        Start, Stop and reset the timer
        In addition to doing that to embedded OSD_Timer,
        manage also counter of hits
        """

    def Count(self) -> int:
        """Return value of hits counter (count of Start/Stop pairs)"""

    def IsRunning(self) -> int:
        """Returns value of nesting counter"""

    def CPU(self) -> float:
        """Return value of CPU time minus accumulated amendment"""

    def Amend(self) -> float:
        """Return value of accumulated amendment on CPU time"""

    def Dump(self) -> str:
        """Dumps current state of a timer shortly (one-line output)"""

    @staticmethod
    def Timer_s(name: str) -> MoniTool_Timer:
        """
        Returns a timer from a dictionary by its name
        If timer not existed, creates a new one
        """

    @staticmethod
    def Start_s(name: str) -> None: ...

    @staticmethod
    def Stop_s(name: str) -> None:
        """
        Inline methods to conveniently start/stop timer by name
        Shortcut to Timer(name)->Start/Stop()
        """

    @staticmethod
    def Dictionary() -> "NCollection_DataMap<char const*, opencascade::handle<MoniTool_Timer>, Standard_CStringHasher>":
        """Returns map of timers"""

    @staticmethod
    def ClearTimers() -> None:
        """Clears map of timers"""

    @staticmethod
    def DumpTimers() -> str:
        """Dumps contents of the whole dictionary"""

    @staticmethod
    def ComputeAmendments() -> None:
        """
        Computes and remembers amendments for times to
        access, start, and stop of timer, and estimates
        second-order error measured by 10 nested timers
        """

    @staticmethod
    def GetAmendments() -> tuple[float, float, float, float]:
        """The computed amendmens are returned (for information only)"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class MoniTool_TimerSentry:
    """
    A tool to facilitate using MoniTool_Timer functionality
    by automatically ensuring consistency of start/stop actions

    When instance of TimerSentry is created, a timer
    with corresponding name is started
    When instance is deleted, timer stops
    """

    @overload
    def __init__(self, cname: str) -> None: ...

    @overload
    def __init__(self, timer: MoniTool_Timer | None) -> None:
        """Constructor creates an instance and runs the corresponding timer"""

    @overload
    def __init__(self, theOther: MoniTool_TimerSentry) -> None: ...

    def Timer(self) -> MoniTool_Timer: ...

    def Stop(self) -> None:
        """Manually stops the timer"""

class MoniTool_TransientElem(MoniTool_Element):
    """
    an TransientElem defines an Element for a specific input class
    its definition includes the value of the Key to be mapped,
    and the HashCoder associated to the class of the Key

    Transient from Standard defines the class to be keyed
    MapTransientHasher from TColStd is the associated Hasher
    DataInfo from MoniTool is an additional class which helps to provide
    information on the value (template : see DataInfo)
    """

    @overload
    def __init__(self, akey: nanoocp.Standard.Standard_Transient | None) -> None:
        """
        Creates a TransientElem with a Value. This Value can then not be
        changed. It is used by the Hasher to compute the HashCode,
        which will then be stored for an immediate reading.
        """

    @overload
    def __init__(self, theOther: MoniTool_TransientElem) -> None: ...

    def Value(self) -> nanoocp.Standard.Standard_Transient:
        """Returns the contained value"""

    def Equates(self, other: MoniTool_Element | None) -> bool:
        """
        Specific testof equality : defined as False if <other> has
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

class MoniTool_TypedValue(nanoocp.Standard.Standard_Transient):
    """
    This class allows to dynamically manage .. typed values, i.e.
    values which have an alphanumeric expression, but with
    controls. Such as "must be an Integer" or "Enumerative Text"
    etc

    Hence, a TypedValue brings a specification (type + constraints
    if any) and a value. Its basic form is a string, it can be
    specified as integer or real or enumerative string, then
    queried as such.
    Its string content, which is a occ::handle<HAsciiString> can be
    shared by other data structures, hence gives a direct on line
    access to its value.
    """

    @overload
    def __init__(self, name: str, type: MoniTool_ValueType = MoniTool_ValueType.MoniTool_ValueText, init: str = '') -> None:
        """
        Creates a TypedValue, with a name

        type gives the type of the parameter, default is free text
        Also available : Integer, Real, Enum, Entity (i.e. Object)
        More precise specifications, titles, can be given to the
        TypedValue once created

        init gives an initial value. If it is not given, the
        TypedValue begins as "not set", its value is empty
        """

    @overload
    def __init__(self, other: MoniTool_TypedValue | None) -> None:
        """Creates a TypedValue from another one, by duplication"""

    @overload
    def __init__(self, theOther: MoniTool_TypedValue) -> None: ...

    def Name(self) -> str:
        """Returns the name"""

    def ValueType(self) -> MoniTool_ValueType:
        """Returns the type of the value"""

    def Definition(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the Definition
        By priority, the enforced one, else an automatic one, computed
        from the specification
        """

    def SetDefinition(self, deftext: str) -> None:
        """Enforces a Definition"""

    def Print(self) -> str:
        """Prints definition, specification, and actual status and value"""

    def PrintValue(self) -> str:
        """Prints only the Value"""

    def AddDef(self, initext: str) -> bool:
        """
        Completes the definition of a TypedValue by command <initext>,
        once created with its type
        Returns True if done, False if could not be interpreted
        <initext> may be :
        imin ival : minimum value for an integer
        imax ival : maximum value for an integer
        rmin rval : minimum value for a real
        rmax rval : maximum value for a real
        unit name : name of unit
        ematch i  : enum from integer value i, match required
        enum   i  : enum from integer value i, match not required
        eval text : add an enumerative value (increments max by 1)
        eval ??   : add a non-authorised enum value (to be skipped)
        tmax   l  : maximum length for a text
        """

    def SetLabel(self, label: str) -> None:
        """Sets a label, which can then be displayed"""

    def Label(self) -> str:
        """Returns the label, if set; else returns an empty string"""

    def SetMaxLength(self, max: int) -> None:
        """Sets a maximum length for a text (active only for a free text)"""

    def MaxLength(self) -> int:
        """Returns the maximum length, 0 if not set"""

    def SetIntegerLimit(self, max: bool, val: int) -> None:
        """
        Sets an Integer limit (included) to <val>, the upper limit
        if <max> is True, the lower limit if <max> is False
        """

    def IntegerLimit(self, max: bool) -> tuple[bool, int]:
        """
        Gives an Integer Limit (upper if <max> True, lower if <max>
        False). Returns True if this limit is defined, False else
        (in that case, gives the natural limit for Integer)
        """

    def SetRealLimit(self, max: bool, val: float) -> None:
        """
        Sets a Real limit (included) to <val>, the upper limit
        if <max> is True, the lower limit if <max> is False
        """

    def RealLimit(self, max: bool) -> tuple[bool, float]:
        """
        Gives an Real Limit (upper if <max> True, lower if <max>
        False). Returns True if this limit is defined, False else
        (in that case, gives the natural limit for Real)
        """

    def SetUnitDef(self, def_: str) -> None:
        """
        Sets (Clears if <def> empty) a unit definition, as an equation
        of dimensions. TypedValue just records this definition, does
        not exploit it, to be done as required by user applications
        """

    def UnitDef(self) -> str:
        """Returns the recorded unit definition, empty if not set"""

    def StartEnum(self, start: int = 0, match: bool = True) -> None:
        """
        For an enumeration, precises the starting value (default 0)
        and the match condition : if True (D), the string value must
        match the definition, else it may take another value : in that
        case, the Integer Value will be Start - 1.
        (empty value remains allowed)
        """

    def AddEnum(self, v1: str = '', v2: str = '', v3: str = '', v4: str = '', v5: str = '', v6: str = '', v7: str = '', v8: str = '', v9: str = '', v10: str = '') -> None:
        """Adds enumerative definitions. For more than 10, several calls"""

    def AddEnumValue(self, val: str, num: int) -> None:
        """
        Adds an enumeration definition, by its string and numeric
        values. If it is the first setting for this value, it is
        recorded as main value. Else, it is recognized as alternate
        string for this numeric value
        """

    def EnumDef(self) -> tuple[bool, int, int, bool]:
        """
        Gives the Enum definitions : start value, end value, match
        status. Returns True for an Enum, False else.
        """

    def EnumVal(self, num: int) -> str:
        """
        Returns the value of an enumerative definition, from its rank
        Empty string if out of range or not an Enum
        """

    def EnumCase(self, val: str) -> int:
        """
        Returns the case number which corresponds to a string value
        Works with main and additional values
        Returns (StartEnum - 1) if not OK, -1 if not an Enum
        """

    def SetObjectType(self, typ: nanoocp.Standard.Standard_Type | None) -> None:
        """
        Sets type of which an Object TypedValue must be kind of
        Error for a TypedValue not an Object (Entity)
        """

    def ObjectType(self) -> nanoocp.Standard.Standard_Type:
        """
        Returns the type of which an Object TypedValue must be kind of
        Default is Standard_Transient
        Null for a TypedValue not an Object
        """

    def HasInterpret(self) -> bool:
        """Tells if a TypedValue has an Interpret"""

    def SatisfiesName(self) -> str:
        """Returns name of specific satisfy, empty string if none"""

    def IsSetValue(self) -> bool:
        """Returns True if the value is set (not empty/not null object)"""

    def CStringValue(self) -> str:
        """Returns the value, as a cstring. Empty if not set."""

    def HStringValue(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Returns the value, as a Handle (can then be shared)
        Null if not defined
        """

    def Interpret(self, hval: nanoocp.TCollection.TCollection_HAsciiString | None, native: bool) -> nanoocp.TCollection.TCollection_HAsciiString:
        """
        Interprets a value.
        <native> True  : returns a native value
        <native> False : returns a coded  value
        If the Interpret function is set, calls it
        Else, for an Enum, Native returns the Text, Coded returns
        the number
        STANDARD RETURNS : = hval means no specific interpretation
        Null means senseless
        Can also be redefined
        """

    def Satisfies(self, hval: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Returns True if a value statifies the specification
        (remark : does not apply to Entity : see ObjectType, for this
        type, the string is just a comment)
        """

    def ClearValue(self) -> None:
        """Clears the recorded Value : it is now unset"""

    def SetCStringValue(self, val: str) -> bool:
        """
        Changes the value. The new one must satisfy the specification
        Returns False (and did not set) if the new value
        does not satisfy the specification
        Can be redefined to be managed (in a subclass)
        """

    def SetHStringValue(self, hval: nanoocp.TCollection.TCollection_HAsciiString | None) -> bool:
        """
        Forces a new Handle for the Value
        It can be empty, else (if Type is not free Text), it must
        satisfy the specification.
        Not only the value is changed, but also the way it is shared
        Remark : for Type=Object, this value is not controlled, it can
        be set as a comment
        Returns False (and did not set) if the new value
        does not satisfy the specification
        Can be redefined to be managed (in a subclass)
        """

    def IntegerValue(self) -> int:
        """
        Returns the value as integer, i.e. :
        For type = Integer, the integer itself; 0 if not set
        For type = Enum, the designated rank (see Enum definition)
        StartEnum - 1 if not set or not in the definition
        Else, returns 0
        """

    def SetIntegerValue(self, ival: int) -> bool:
        """Changes the value as an integer, only for Integer or Enum"""

    def RealValue(self) -> float:
        """
        Returns the value as real, for a Real type TypedValue
        Else, returns 0.
        """

    def SetRealValue(self, rval: float) -> bool:
        """Changes the value as a real, only for Real"""

    def ObjectValue(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns the value as Transient Object, only for Object/Entity
        Remark that the "HString value" is IGNORED here
        Null if not set; remains to be casted
        """

    def GetObjectValue(self) -> nanoocp.Standard.Standard_Transient:
        """
        Same as ObjectValue, but avoids DownCast : the receiving
        variable is directly loaded. It is assumed that it complies
        with the definition of ObjectType ! Otherwise, big trouble
        """

    def SetObjectValue(self, obj: nanoocp.Standard.Standard_Transient | None) -> bool:
        """
        Changes the value as Transient Object, only for Object/Entity
        Returns False if DynamicType does not satisfy ObjectType
        Can be redefined to be managed (in a subclass)
        """

    def ObjectTypeName(self) -> str:
        """
        Returns the type name of the ObjectValue, or an empty string
        if not set
        """

    @staticmethod
    def AddLib(tv: MoniTool_TypedValue | None, def_: str = '') -> bool:
        """
        Adds a TypedValue in the library.
        It is recorded then will be accessed by its Name
        Its Definition may be imposed, else it is computed as usual
        By default it will be accessed by its Definition (string)
        Returns True if done, False if tv is Null or brings no
        Definition or <def> not defined

        If a TypedValue was already recorded under this name, it is
        replaced
        """

    @staticmethod
    def Lib(def_: str) -> MoniTool_TypedValue:
        """
        Returns the TypedValue bound with a given Name
        Null Handle if none recorded
        Warning: it is the original, not duplicated
        """

    @staticmethod
    def FromLib(def_: str) -> MoniTool_TypedValue:
        """
        Returns a COPY of the TypedValue bound with a given Name
        Null Handle if none recorded
        """

    @staticmethod
    def LibList() -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_AsciiString]:
        """
        Returns the list of names of items of the Library of Types
        Library of TypedValue as Valued Parameters, accessed by
        parameter name for use by management of Static Parameters
        """

    @staticmethod
    def StaticValue(name: str) -> MoniTool_TypedValue:
        """Returns a static value from its name, null if unknown"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.TopTools
MoniTool_DataMapOfShapeTransient = nanoocp.NCollection.NCollection_DataMap[nanoocp.TopoDS.TopoDS_Shape, nanoocp.Standard.Standard_Transient, nanoocp.TopTools.TopTools_ShapeMapHasher]
