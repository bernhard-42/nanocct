"""OCCT package Message (toolkit TKernel)"""

import enum
from typing import TextIO, overload

import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Standard
import nanoocp.TColStd
import nanoocp.TCollection


class Message_Gravity(enum.IntEnum):
    """
    Defines gravity level of messages
    - Trace: low-level details on algorithm execution (usually for debug purposes)
    - Info: informative message
    - Warning: warning message
    - Alarm: non-critical error
    - Fail: fatal error
    """

    Message_Trace = 0

    Message_Info = 1

    Message_Warning = 2

    Message_Alarm = 3

    Message_Fail = 4

class Message_MetricType(enum.IntEnum):
    """Specifies kind of report information to collect"""

    Message_MetricType_None = 0

    Message_MetricType_ThreadCPUUserTime = 1

    Message_MetricType_ThreadCPUSystemTime = 2

    Message_MetricType_ProcessCPUUserTime = 3

    Message_MetricType_ProcessCPUSystemTime = 4

    Message_MetricType_WallClock = 5

    Message_MetricType_MemPrivate = 6

    Message_MetricType_MemVirtual = 7

    Message_MetricType_MemWorkingSet = 8

    Message_MetricType_MemWorkingSetPeak = 9

    Message_MetricType_MemSwapUsage = 10

    Message_MetricType_MemSwapUsagePeak = 11

    Message_MetricType_MemHeapUsage = 12

class Message_StatusType(enum.IntEnum):
    """
    Definition of types of execution status supported by
    the class Message_ExecStatus
    """

    Message_DONE = 256

    Message_WARN = 512

    Message_ALARM = 1024

    Message_FAIL = 2048

class Message_Status(enum.IntEnum):
    """
    Enumeration covering all execution statuses supported by the class
    Message_ExecStatus: 32 statuses per each of 4 types (DONE, WARN, ALARM, FAIL)
    """

    Message_None = 0

    Message_Done1 = 256

    Message_Done2 = 257

    Message_Done3 = 258

    Message_Done4 = 259

    Message_Done5 = 260

    Message_Done6 = 261

    Message_Done7 = 262

    Message_Done8 = 263

    Message_Done9 = 264

    Message_Done10 = 265

    Message_Done11 = 266

    Message_Done12 = 267

    Message_Done13 = 268

    Message_Done14 = 269

    Message_Done15 = 270

    Message_Done16 = 271

    Message_Done17 = 272

    Message_Done18 = 273

    Message_Done19 = 274

    Message_Done20 = 275

    Message_Done21 = 276

    Message_Done22 = 277

    Message_Done23 = 278

    Message_Done24 = 279

    Message_Done25 = 280

    Message_Done26 = 281

    Message_Done27 = 282

    Message_Done28 = 283

    Message_Done29 = 284

    Message_Done30 = 285

    Message_Done31 = 286

    Message_Done32 = 287

    Message_Warn1 = 512

    Message_Warn2 = 513

    Message_Warn3 = 514

    Message_Warn4 = 515

    Message_Warn5 = 516

    Message_Warn6 = 517

    Message_Warn7 = 518

    Message_Warn8 = 519

    Message_Warn9 = 520

    Message_Warn10 = 521

    Message_Warn11 = 522

    Message_Warn12 = 523

    Message_Warn13 = 524

    Message_Warn14 = 525

    Message_Warn15 = 526

    Message_Warn16 = 527

    Message_Warn17 = 528

    Message_Warn18 = 529

    Message_Warn19 = 530

    Message_Warn20 = 531

    Message_Warn21 = 532

    Message_Warn22 = 533

    Message_Warn23 = 534

    Message_Warn24 = 535

    Message_Warn25 = 536

    Message_Warn26 = 537

    Message_Warn27 = 538

    Message_Warn28 = 539

    Message_Warn29 = 540

    Message_Warn30 = 541

    Message_Warn31 = 542

    Message_Warn32 = 543

    Message_Alarm1 = 1024

    Message_Alarm2 = 1025

    Message_Alarm3 = 1026

    Message_Alarm4 = 1027

    Message_Alarm5 = 1028

    Message_Alarm6 = 1029

    Message_Alarm7 = 1030

    Message_Alarm8 = 1031

    Message_Alarm9 = 1032

    Message_Alarm10 = 1033

    Message_Alarm11 = 1034

    Message_Alarm12 = 1035

    Message_Alarm13 = 1036

    Message_Alarm14 = 1037

    Message_Alarm15 = 1038

    Message_Alarm16 = 1039

    Message_Alarm17 = 1040

    Message_Alarm18 = 1041

    Message_Alarm19 = 1042

    Message_Alarm20 = 1043

    Message_Alarm21 = 1044

    Message_Alarm22 = 1045

    Message_Alarm23 = 1046

    Message_Alarm24 = 1047

    Message_Alarm25 = 1048

    Message_Alarm26 = 1049

    Message_Alarm27 = 1050

    Message_Alarm28 = 1051

    Message_Alarm29 = 1052

    Message_Alarm30 = 1053

    Message_Alarm31 = 1054

    Message_Alarm32 = 1055

    Message_Fail1 = 2048

    Message_Fail2 = 2049

    Message_Fail3 = 2050

    Message_Fail4 = 2051

    Message_Fail5 = 2052

    Message_Fail6 = 2053

    Message_Fail7 = 2054

    Message_Fail8 = 2055

    Message_Fail9 = 2056

    Message_Fail10 = 2057

    Message_Fail11 = 2058

    Message_Fail12 = 2059

    Message_Fail13 = 2060

    Message_Fail14 = 2061

    Message_Fail15 = 2062

    Message_Fail16 = 2063

    Message_Fail17 = 2064

    Message_Fail18 = 2065

    Message_Fail19 = 2066

    Message_Fail20 = 2067

    Message_Fail21 = 2068

    Message_Fail22 = 2069

    Message_Fail23 = 2070

    Message_Fail24 = 2071

    Message_Fail25 = 2072

    Message_Fail26 = 2073

    Message_Fail27 = 2074

    Message_Fail28 = 2075

    Message_Fail29 = 2076

    Message_Fail30 = 2077

    Message_Fail31 = 2078

    Message_Fail32 = 2079

class Message_ConsoleColor(enum.IntEnum):
    """Color definition for console/terminal output (limited palette)."""

    Message_ConsoleColor_Default = 0

    Message_ConsoleColor_Black = 1

    Message_ConsoleColor_White = 2

    Message_ConsoleColor_Red = 3

    Message_ConsoleColor_Blue = 4

    Message_ConsoleColor_Green = 5

    Message_ConsoleColor_Yellow = 6

    Message_ConsoleColor_Cyan = 7

    Message_ConsoleColor_Magenta = 8

class Message_Printer(nanoocp.Standard.Standard_Transient):
    """
    Abstract interface class defining printer as output context for text messages

    The message, besides being text string, has associated gravity
    level, which can be used by printer to decide either to process a message or ignore it.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetTraceLevel(self) -> Message_Gravity:
        """
        Return trace level used for filtering messages;
        messages with lover gravity will be ignored.
        """

    def SetTraceLevel(self, theTraceLevel: Message_Gravity) -> None:
        """
        Set trace level used for filtering messages.
        By default, trace level is Message_Info, so that all messages are output
        """

    @overload
    def Send(self, theString: nanoocp.TCollection.TCollection_ExtendedString, theGravity: Message_Gravity) -> None: ...

    @overload
    def Send(self, theString: str, theGravity: Message_Gravity) -> None: ...

    @overload
    def Send(self, theString: nanoocp.TCollection.TCollection_AsciiString, theGravity: Message_Gravity) -> None:
        """
        Send a string message with specified trace level.
        The last Boolean argument is deprecated and unused.
        Default implementation redirects to send().
        """

    def SendStringStream(self, theStream: TextIO, theGravity: Message_Gravity) -> None:
        """
        Send a string message with specified trace level.
        Stream is converted to string value.
        Default implementation calls first method Send().
        """

    def SendObject(self, theObject: nanoocp.Standard.Standard_Transient, theGravity: Message_Gravity) -> None:
        """
        Send a string message with specified trace level.
        The object is converted to string in format: <object kind> : <object pointer>.
        Default implementation calls first method Send().
        """

class Message_Messenger(nanoocp.Standard.Standard_Transient):
    """
    Messenger is API class providing general-purpose interface for
    libraries that may issue text messages without knowledge
    of how these messages will be further processed.

    The messenger contains a sequence of "printers" which can be
    customized by the application, and dispatches every received
    message to all the printers.

    For convenience, a set of methods Send...() returning a string
    stream buffer is defined for use of stream-like syntax with operator <<

    Example:
    ~~~~~
    Messenger->SendFail() << " Unknown fail at line " << aLineNo << " in file " << aFile;
    ~~~~~

    The message is sent to messenger on destruction of the stream buffer,
    call to Flush(), or passing manipulator std::ends, std::endl, or std::flush.
    Empty messages are not sent except if manipulator is used.
    """

    @overload
    def __init__(self) -> None:
        """
        Empty constructor; initializes by single printer directed to std::cout.
        Note: the default messenger is not empty but directed to cout
        in order to protect against possibility to forget defining printers.
        If printing to cout is not needed, clear messenger by GetPrinters().Clear()
        """

    @overload
    def __init__(self, thePrinter: Message_Printer) -> None:
        """Create messenger with single printer"""

    @overload
    def __init__(self, theOther: Message_Messenger) -> None: ...

    class StreamBuffer:
        """
        Auxiliary class wrapping std::stringstream thus allowing constructing
        message via stream interface, and putting result into its creator
        Message_Messenger within destructor.

        It is intended to be used either as temporary object or as local
        variable, note that content will be lost if it is copied.
        """

        def __init__(self, theOther: Message_Messenger.StreamBuffer) -> None:
            """
            Formal copy constructor.

            Since buffer is intended for use as temporary object or local
            variable, copy (or move) is needed only formally to be able to
            return the new instance from relevant creation method.
            In practice it should never be called because modern compilers
            create such instances in place.
            However note that if this constructor is called, the buffer
            content (string) will not be copied (move is not supported for
            std::stringstream class on old compilers such as gcc 4.4, msvc 9).
            """

        def Flush(self, doForce: bool = False) -> None:
            """Flush collected string to messenger"""

        def Messenger(self) -> Message_Messenger:
            """Access to the messenger"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AddPrinter(self, thePrinter: Message_Printer) -> bool:
        """
        Add a printer to the messenger.
        The printer will be added only if it is not yet in the list.
        Returns True if printer has been added.
        """

    def RemovePrinter(self, thePrinter: Message_Printer) -> bool:
        """
        Removes specified printer from the messenger.
        Returns True if this printer has been found in the list
        and removed.
        """

    def RemovePrinters(self, theType: nanoocp.Standard.Standard_Type) -> int:
        """
        Removes printers of specified type (including derived classes)
        from the messenger.
        Returns number of removed printers.
        """

    def Printers(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Message.Message_Printer]:
        """Returns current sequence of printers"""

    def ChangePrinters(self) -> nanoocp.NCollection.NCollection_Sequence[nanoocp.Message.Message_Printer]:
        """
        Returns sequence of printers
        The sequence can be modified.
        """

    @overload
    def Send(self, theString: str, theGravity: Message_Gravity = Message_Gravity.Message_Warning) -> None:
        """
        Dispatch a message to all the printers in the list.
        Three versions of string representations are accepted for
        convenience, by default all are converted to ExtendedString.
        """

    @overload
    def Send(self, theStream: TextIO, theGravity: Message_Gravity = Message_Gravity.Message_Warning) -> None: ...

    @overload
    def Send(self, theString: nanoocp.TCollection.TCollection_AsciiString, theGravity: Message_Gravity = Message_Gravity.Message_Warning) -> None: ...

    @overload
    def Send(self, theString: nanoocp.TCollection.TCollection_ExtendedString, theGravity: Message_Gravity = Message_Gravity.Message_Warning) -> None: ...

    @overload
    def Send(self, theGravity: Message_Gravity) -> Message_Messenger.StreamBuffer:
        """Create string buffer for message of specified type"""

    @overload
    def Send(self, theObject: nanoocp.Standard.Standard_Transient, theGravity: Message_Gravity = Message_Gravity.Message_Warning) -> None:
        """See above"""

    @overload
    def SendFail(self) -> Message_Messenger.StreamBuffer:
        """Create string buffer for sending Fail message"""

    @overload
    def SendFail(self, theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Short-cut to Send (theMessage, Message_Fail)"""

    @overload
    def SendAlarm(self) -> Message_Messenger.StreamBuffer:
        """Create string buffer for sending Alarm message"""

    @overload
    def SendAlarm(self, theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Short-cut to Send (theMessage, Message_Alarm)"""

    @overload
    def SendWarning(self) -> Message_Messenger.StreamBuffer:
        """Create string buffer for sending Warning message"""

    @overload
    def SendWarning(self, theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Short-cut to Send (theMessage, Message_Warning)"""

    @overload
    def SendInfo(self) -> Message_Messenger.StreamBuffer:
        """Create string buffer for sending Info message"""

    @overload
    def SendInfo(self, theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Short-cut to Send (theMessage, Message_Info)"""

    @overload
    def SendTrace(self) -> Message_Messenger.StreamBuffer:
        """Create string buffer for sending Trace message"""

    @overload
    def SendTrace(self, theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Short-cut to Send (theMessage, Message_Trace)"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Message:
    """
    Defines
    - tools to work with messages
    - basic tools intended for progress indication
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Message) -> None: ...

    @staticmethod
    def DefaultMessenger() -> Message_Messenger:
        """
        Defines default messenger for OCCT applications.
        This is global static instance of the messenger.
        By default, it contains single printer directed to std::cout.
        It can be customized according to the application needs.

        The following syntax can be used to print messages:
        @code
        Message::DefaultMessenger()->Send ("My Warning", Message_Warning);
        Message::SendWarning ("My Warning"); // short-cut for Message_Warning
        Message::SendWarning() << "My Warning with " << theCounter << " arguments";
        Message::SendFail ("My Failure"); // short-cut for Message_Fail
        @endcode
        """

    @overload
    @staticmethod
    def Send(theGravity: Message_Gravity) -> Message_Messenger.StreamBuffer:
        """@name Short-cuts to DefaultMessenger"""

    @overload
    @staticmethod
    def Send(theMessage: nanoocp.TCollection.TCollection_AsciiString, theGravity: Message_Gravity) -> None: ...

    @overload
    @staticmethod
    def SendFail() -> Message_Messenger.StreamBuffer: ...

    @overload
    @staticmethod
    def SendFail(theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    @staticmethod
    def SendAlarm() -> Message_Messenger.StreamBuffer: ...

    @overload
    @staticmethod
    def SendAlarm(theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    @staticmethod
    def SendWarning() -> Message_Messenger.StreamBuffer: ...

    @overload
    @staticmethod
    def SendWarning(theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    @staticmethod
    def SendInfo() -> Message_Messenger.StreamBuffer: ...

    @overload
    @staticmethod
    def SendInfo(theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @overload
    @staticmethod
    def SendTrace() -> Message_Messenger.StreamBuffer: ...

    @overload
    @staticmethod
    def SendTrace(theMessage: nanoocp.TCollection.TCollection_AsciiString) -> None: ...

    @staticmethod
    def FillTime(Hour: int, Minute: int, Second: float) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the string filled with values of hours, minutes and seconds.
        Example:
        1. (5, 12, 26.3345) returns "05h:12m:26.33s",
        2. (0,  6, 34.496 ) returns "06m:34.50s",
        3. (0,  0,  4.5   ) returns "4.50s\"
        """

    @staticmethod
    def DefaultReport(theToCreate: bool = False) -> Message_Report:
        """
        returns the only one instance of Report
        When theToCreate is true - automatically creates message report when not exist.
        """

    @overload
    @staticmethod
    def MetricFromString(theString: str) -> Message_MetricType:
        """
        Returns the metric type from the given string identifier.
        @param theString string identifier
        @return metric type or Message_MetricType_None if string identifier is invalid
        """

    @overload
    @staticmethod
    def MetricFromString(theString: str) -> tuple[bool, Message_MetricType]:
        """
        Determines the metric from the given string identifier.
        @param theString string identifier
        @param theType detected type of metric
        @return TRUE if string identifier is known
        """

    @staticmethod
    def MetricToString(theType: Message_MetricType) -> str:
        """
        Returns the string name for a given metric type.
        @param theType metric type
        @return string identifier from the list of Message_MetricType
        """

    @staticmethod
    def ToOSDMetric(theMetric: Message_MetricType) -> tuple[bool, nanoocp.OSD.OSD_MemInfo.Counter]:
        """
        Converts message metric to OSD memory info type.
        @param[in] theMetric  message metric
        @param[out] theMemInfo  filled memory info type
        @return true if converted
        """

    @staticmethod
    def ToMessageMetric(theMemInfo: nanoocp.OSD.OSD_MemInfo.Counter) -> tuple[bool, Message_MetricType]:
        """
        Converts OSD memory info type to message metric.
        @param theMemInfo [int] memory info type
        @param[out] theMetric  filled message metric
        @return true if converted
        """

class Message_Alert(nanoocp.Standard.Standard_Transient):
    """
    Base class of the hierarchy of classes describing various situations
    occurring during execution of some algorithm or procedure.

    Alert should provide unique text identifier that can be used to distinguish
    particular type of alerts, e.g. to get text message string describing it.
    See method GetMessageKey(); by default, dynamic type name is used.

    Alert can contain some data. To avoid duplication of data, new alert
    can be merged with another one of the same type. Method SupportsMerge()
    should return true if merge is supported; method Merge() should do the
    merge if possible and return true in that case and false otherwise.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Message_Alert) -> None: ...

    def GetMessageKey(self) -> str:
        """
        Return a C string to be used as a key for generating text user
        messages describing this alert.
        The messages are generated with help of Message_Msg class, in
        Message_Report::Dump().
        Base implementation returns dynamic type name of the instance.
        """

    def SupportsMerge(self) -> bool:
        """
        Return true if this type of alert can be merged with other
        of the same type to avoid duplication.
        Basis implementation returns true.
        """

    def Merge(self, theTarget: Message_Alert) -> bool:
        """
        If possible, merge data contained in this alert to theTarget.
        @return True if merged.
        Base implementation always returns true.
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Message_AlertExtended(Message_Alert):
    """
    Inherited class of Message_Alert with some additional information.
    It has Message_Attributes to provide the alert name, and other custom information
    It has a container of composite alerts, if the alert might provide
    sub-alerts collecting.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Message_AlertExtended) -> None: ...

    @staticmethod
    def AddAlert(theReport: Message_Report, theAttribute: Message_Attribute, theGravity: Message_Gravity) -> Message_Alert:
        """
        Creates new instance of the alert and put it into report with Message_Info gravity.
        It does nothing if such kind of gravity is not active in the report
        @param theReport the message report where new alert is placed
        @param theAttribute container of additional values of the alert
        @return created alert or NULL if Message_Info is not active in report
        """

    def GetMessageKey(self) -> str:
        """
        Return a C string to be used as a key for generating text user messages describing this alert.
        The messages are generated with help of Message_Msg class, in Message_Report::Dump().
        Base implementation returns dynamic type name of the instance.
        """

    def Attribute(self) -> Message_Attribute:
        """Returns container of the alert attributes"""

    def SetAttribute(self, theAttribute: Message_Attribute) -> None:
        """
        Sets container of the alert attributes
        @param theAttributes an attribute values
        """

    def CompositeAlerts(self, theToCreate: bool = False) -> Message_CompositeAlerts:
        """
        Returns class provided hierarchy of alerts if created or create if the parameter is true
        @param theToCreate if composite alert has not been created for this alert, it should be
        created
        @return instance or NULL
        """

    def SupportsMerge(self) -> bool:
        """
        Return true if this type of alert can be merged with other
        of the same type to avoid duplication.
        Hierarchical alerts can not be merged
        Basis implementation returns true.
        """

    def Merge(self, theTarget: Message_Alert) -> bool:
        """
        If possible, merge data contained in this alert to theTarget.
        Base implementation always returns false.
        @return True if merged
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Message_ExecStatus:
    """
    Tiny class for extended handling of error / execution
    status of algorithm in universal way.

    It is in fact a set of integers represented as a collection of bit flags
    for each of four types of status; each status flag has its own symbolic
    name and can be set/tested individually.

    The flags are grouped in semantic groups:
    - No flags means nothing done
    - Done flags correspond to some operation successfully completed
    - Warning flags correspond to warning messages on some
    potentially wrong situation, not harming algorithm execution
    - Alarm flags correspond to more severe warnings about incorrect
    user data, while not breaking algorithm execution
    - Fail flags correspond to cases when algorithm failed to complete
    """

    @overload
    def __init__(self) -> None:
        """Create empty execution status"""

    @overload
    def __init__(self, theStatus: Message_Status) -> None:
        """Initialise the execution status"""

    @overload
    def __init__(self, theOther: Message_ExecStatus) -> None: ...

    class StatusRange(enum.IntEnum):
        """Definitions of range of available statuses"""

        FirstStatus = 1

        StatusesPerType = 32

        NbStatuses = 128

        LastStatus = 129

    def Set(self, theStatus: Message_Status) -> None:
        """Sets a status flag"""

    def IsSet(self, theStatus: Message_Status) -> bool:
        """Check status for being set"""

    @overload
    def Clear(self, theStatus: Message_Status) -> None:
        """Clear one status"""

    @overload
    def Clear(self) -> None:
        """Clear all statuses"""

    def IsDone(self) -> bool:
        """Check if at least one status of each type is set"""

    def IsFail(self) -> bool: ...

    def IsWarn(self) -> bool: ...

    def IsAlarm(self) -> bool: ...

    def SetAllDone(self) -> None:
        """Set all statuses of each type"""

    def SetAllWarn(self) -> None: ...

    def SetAllAlarm(self) -> None: ...

    def SetAllFail(self) -> None: ...

    def ClearAllDone(self) -> None:
        """Clear all statuses of each type"""

    def ClearAllWarn(self) -> None: ...

    def ClearAllAlarm(self) -> None: ...

    def ClearAllFail(self) -> None: ...

    def Add(self, theOther: Message_ExecStatus) -> None:
        """Add statuses to me from theOther execution status"""

    def __ior__(self, theOther: Message_ExecStatus) -> Message_ExecStatus: ...

    def And(self, theOther: Message_ExecStatus) -> None:
        """Leave only the statuses common with theOther"""

    def __iand__(self, theOther: Message_ExecStatus) -> Message_ExecStatus: ...

    @staticmethod
    def StatusIndex(theStatus: Message_Status) -> int:
        """Returns index of status in whole range [FirstStatus, LastStatus]"""

    @staticmethod
    def LocalStatusIndex(theStatus: Message_Status) -> int:
        """
        Returns index of status inside type of status (Done or Warn or, etc)
        in range [1, StatusesPerType]
        """

    @staticmethod
    def TypeOfStatus(theStatus: Message_Status) -> Message_StatusType:
        """Returns status type (DONE, WARN, ALARM, or FAIL)"""

    @staticmethod
    def StatusByIndex(theIndex: int) -> Message_Status:
        """
        Returns status with index theIndex in whole range [FirstStatus, LastStatus]
        """

class Message_Msg:
    """
    This class provides a tool for constructing the parametrized message
    basing on resources loaded by Message_MsgFile tool.

    A Message is created from a keyword: this keyword identifies the
    message in a message file that should be previously loaded by call
    to Message_MsgFile::LoadFile().

    The text of the message can contain placeholders for the parameters
    which are to be filled by the proper values when the message
    is prepared. Most of the format specifiers used in C can be used,
    for instance, %s for string, %d for integer etc. In addition,
    specifier %f is supported for double numbers (for compatibility
    with previous versions).

    User fills the parameter fields in the text of the message by
    calling corresponding methods Arg() or operators .

    The resulting message, filled with all parameters, can be obtained
    by method Get(). If some parameters were not filled, the text
    UNKNOWN is placed instead.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theMsg: Message_Msg) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, theKey: str) -> None: ...

    @overload
    def __init__(self, theKey: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """Create a message using a corresponding entry in Message_MsgFile"""

    @overload
    def Set(self, theMsg: str) -> None: ...

    @overload
    def Set(self, theMsg: nanoocp.TCollection.TCollection_ExtendedString) -> None:
        """
        Set a message body text -- can be used as alternative to
        using messages from resource file
        """

    @overload
    def Arg(self, theString: str) -> Message_Msg: ...

    @overload
    def Arg(self, theString: nanoocp.TCollection.TCollection_AsciiString) -> Message_Msg: ...

    @overload
    def Arg(self, theString: nanoocp.TCollection.TCollection_HAsciiString) -> Message_Msg: ...

    @overload
    def Arg(self, theString: nanoocp.TCollection.TCollection_ExtendedString) -> Message_Msg: ...

    @overload
    def Arg(self, theString: nanoocp.TCollection.TCollection_HExtendedString) -> Message_Msg:
        """Set a value for %..s conversion"""

    @overload
    def Arg(self, theInt: int) -> Message_Msg:
        """Set a value for %..d, %..i, %..o, %..u, %..x or %..X conversion"""

    @overload
    def Arg(self, theReal: float) -> Message_Msg:
        """Set a value for %..f, %..e, %..E, %..g or %..G conversion"""

    def Original(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """Returns the original message text"""

    def Value(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Returns current state of the message text with
        parameters to the moment
        """

    def IsEdited(self) -> bool:
        """Tells if Value differs from Original"""

    def Get(self) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Return the resulting message string with all parameters
        filled. If some parameters were not yet filled by calls
        to methods Arg (or <<), these parameters are filled by
        the word UNKNOWN
        """

class Message_Algorithm(nanoocp.Standard.Standard_Transient):
    """
    Class Message_Algorithm is intended to be the base class for
    classes implementing algorithms or any operations that need
    to provide extended information on its execution to the
    caller / user.

    It provides generic mechanism for management of the execution
    status, collection and output of messages.

    The algorithm uses methods SetStatus() to set an execution status.
    It is possible to associate a status with a number or a string
    (second argument of SetStatus() methods) to indicate precisely
    the item (object, element etc.) in the input data which caused
    the problem.

    Each execution status generated by the algorithm has associated
    text message that should be defined in the resource file loaded
    with call to Message_MsgFile::LoadFile().

    The messages corresponding to the statuses generated during the
    algorithm execution are output to Message_Messenger using
    methods SendMessages(). If status have associated numbers
    or strings, they are included in the message body in place of
    "%s" placeholder which should be present in the message text.

    The name of the message text in the resource file is constructed
    from name of the class and name of the status, separated by dot,
    for instance:

    .TObj_CheckModel.Alarm2
    Error: Some objects (%s) have references to dead object(s)

    If message for the status is not found with prefix of
    the current class type, the same message is searched for the base
    class(es) recursively.

    Message can be set explicitly for the status; in this case the
    above procedure is not used and supplied message is used as is.

    The messages are output to the messenger, stored in the field;
    though messenger can be changed, it is guaranteed to be non-null.
    By default, Message::DefaultMessenger() is used.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Message_Algorithm) -> None: ...

    @overload
    def SetStatus(self, theStat: Message_Status) -> None:
        """Sets status with no parameter"""

    @overload
    def SetStatus(self, theStat: Message_Status, theInt: int) -> None:
        """Sets status with integer parameter"""

    @overload
    def SetStatus(self, theStat: Message_Status, theStr: str, noRepetitions: bool = True) -> None:
        """
        Sets status with string parameter.
        If noRepetitions is True, the parameter will be added only
        if it has not been yet recorded for the same status flag
        """

    @overload
    def SetStatus(self, theStat: Message_Status, theStr: nanoocp.TCollection.TCollection_AsciiString, noRepetitions: bool = True) -> None: ...

    @overload
    def SetStatus(self, theStat: Message_Status, theStr: nanoocp.TCollection.TCollection_HAsciiString, noRepetitions: bool = True) -> None: ...

    @overload
    def SetStatus(self, theStat: Message_Status, theStr: nanoocp.TCollection.TCollection_ExtendedString, noRepetitions: bool = True) -> None: ...

    @overload
    def SetStatus(self, theStat: Message_Status, theStr: nanoocp.TCollection.TCollection_HExtendedString, noRepetitions: bool = True) -> None:
        """
        Sets status with string parameter
        If noRepetitions is True, the parameter will be added only
        if it has not been yet recorded for the same status flag
        """

    @overload
    def SetStatus(self, theStat: Message_Status, theMsg: Message_Msg) -> None:
        """
        Sets status with preformatted message. This message will be
        used directly to report the status; automatic generation of
        status messages will be disabled for it.
        """

    def GetStatus(self) -> Message_ExecStatus:
        """Returns copy of exec status of algorithm"""

    def ChangeStatus(self) -> Message_ExecStatus:
        """Returns exec status of algorithm"""

    def ClearStatus(self) -> None:
        """Clear exec status of algorithm"""

    def SetMessenger(self, theMsgr: Message_Messenger) -> None:
        """Sets messenger to algorithm"""

    def GetMessenger(self) -> Message_Messenger:
        """
        Returns messenger of algorithm.
        The returned handle is always non-null and can
        be used for sending messages.
        """

    def SendStatusMessages(self, theFilter: Message_ExecStatus, theTraceLevel: Message_Gravity = Message_Gravity.Message_Warning, theMaxCount: int = 20) -> None:
        """
        Print messages for all status flags that have been set during
        algorithm execution, excluding statuses that are NOT set
        in theFilter.

        The messages are taken from resource file, names being
        constructed as {dynamic class type}.{status name},
        for instance, "Message_Algorithm.Fail5".
        If message is not found in resources for this class and all
        its base types, surrogate text is printed.

        For the statuses having number or string parameters,
        theMaxCount defines maximal number of numbers or strings to be
        included in the message

        Note that this method is virtual; this allows descendant
        classes to customize message output (e.g. by adding
        messages from other sub-algorithms)
        """

    def SendMessages(self, theTraceLevel: Message_Gravity = Message_Gravity.Message_Warning, theMaxCount: int = 20) -> None:
        """
        Convenient variant of SendStatusMessages() with theFilter
        having defined all WARN, ALARM, and FAIL (but not DONE)
        status flags
        """

    @overload
    def AddStatus(self, theOther: Message_Algorithm) -> None:
        """
        Add statuses to this algorithm from other algorithm
        (including messages)
        """

    @overload
    def AddStatus(self, theStatus: Message_ExecStatus, theOther: Message_Algorithm) -> None:
        """
        Add statuses to this algorithm from other algorithm, but
        only those items are moved that correspond to statuses
        set in theStatus
        """

    def GetMessageNumbers(self, theStatus: Message_Status) -> nanoocp.TColStd.TColStd_HPackedMapOfInteger:
        """
        Return the numbers associated with the indicated status;
        Null handle if no such status or no numbers associated with it
        """

    def GetMessageStrings(self, theStatus: Message_Status) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HExtendedString]:
        """
        Return the strings associated with the indicated status;
        Null handle if no such status or no strings associated with it
        """

    @overload
    @staticmethod
    def PrepareReport(theError: nanoocp.TColStd.TColStd_HPackedMapOfInteger, theMaxCount: int) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Prepares a string containing a list of integers contained
        in theError map, but not more than theMaxCount
        """

    @overload
    @staticmethod
    def PrepareReport(theReportSeq: nanoocp.NCollection.NCollection_Sequence[nanoocp.TCollection.TCollection_HExtendedString], theMaxCount: int) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Prepares a string containing a list of names contained
        in theReportSeq sequence, but not more than theMaxCount
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Message_Attribute(nanoocp.Standard.Standard_Transient):
    """
    Additional information of extended alert attribute
    To provide other custom attribute container, it might be redefined.
    """

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Message_Attribute) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def GetMessageKey(self) -> str:
        """
        Return a C string to be used as a key for generating text user messages describing this alert.
        The messages are generated with help of Message_Msg class, in Message_Report::Dump().
        Base implementation returns dynamic type name of the instance.
        """

    def GetName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns custom name of alert if it is set
        @return alert name
        """

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets the custom name of alert
        @param theName a name for the alert
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Message_AttributeMeter(Message_Attribute):
    """
    Alert object storing alert metrics values.
    Start and stop values for each metric.
    """

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Constructor with string argument"""

    @overload
    def __init__(self, theOther: Message_AttributeMeter) -> None: ...

    @staticmethod
    def UndefinedMetricValue() -> float:
        """
        Returns default value of the metric when it is not defined
        @return undefined value
        """

    def HasMetric(self, theMetric: Message_MetricType) -> bool:
        """
        Checks whether the attribute has values for the metric
        @param[in] theMetric  metric type
        @return true if the metric values exist in the attribute
        """

    def IsMetricValid(self, theMetric: Message_MetricType) -> bool:
        """
        Returns true when both values of the metric are set.
        @param[in] theMetric  metric type
        @return true if metric values are valid
        """

    def StartValue(self, theMetric: Message_MetricType) -> float:
        """
        Returns start value for the metric
        @param[in] theMetric  metric type
        @return real value
        """

    def SetStartValue(self, theMetric: Message_MetricType, theValue: float) -> None:
        """
        Sets start values for the metric
        @param[in] theMetric  metric type
        """

    def StopValue(self, theMetric: Message_MetricType) -> float:
        """
        Returns stop value for the metric
        @param[in] theMetric  metric type
        @return real value
        """

    def SetStopValue(self, theMetric: Message_MetricType, theValue: float) -> None:
        """
        Sets stop values for the metric
        @param[in] theMetric  metric type
        """

    @staticmethod
    def StartAlert(theAlert: Message_AlertExtended) -> None:
        """
        Sets start values of default report metrics into the alert
        @param theAlert an alert
        """

    @staticmethod
    def StopAlert(theAlert: Message_AlertExtended) -> None:
        """
        Sets stop values of default report metrics into the alert
        @param theAlert an alert
        """

    @staticmethod
    def SetAlertMetrics(theAlert: Message_AlertExtended, theStartValue: bool) -> None:
        """
        Sets current values of default report metrics into the alert.
        Processed only alert with Message_AttributeMeter attribute
        @param theAlert an alert
        @param theStartValue flag, if true, the start value is collected otherwise stop
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Message_AttributeObject(Message_Attribute):
    """Alert object storing a transient object"""

    @overload
    def __init__(self, theObject: nanoocp.Standard.Standard_Transient, theName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """Constructor with string argument"""

    @overload
    def __init__(self, theOther: Message_AttributeObject) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Object(self) -> nanoocp.Standard.Standard_Transient:
        """
        Returns object
        @return the object instance
        """

    def SetObject(self, theObject: nanoocp.Standard.Standard_Transient) -> None:
        """
        Sets the object
        @param theObject an instance
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Message_AttributeStream(Message_Attribute):
    """Alert object storing stream value"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def SetStream(self, theStream: TextIO) -> None:
        """Sets stream value"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Message_CompositeAlerts(nanoocp.Standard.Standard_Transient):
    """Class providing container of alerts"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Message_CompositeAlerts) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Alerts(self, theGravity: Message_Gravity) -> nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Alert]:
        """Returns list of collected alerts with specified gravity"""

    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool:
        """
        Add alert with specified gravity. If the alert supports merge it will be merged.
        @param theGravity an alert gravity
        @param theAlert an alert to be added as a child alert
        @return true if the alert is added or merged
        """

    def RemoveAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool:
        """
        Removes alert with specified gravity.
        @param theGravity an alert gravity
        @param theAlert an alert to be removed from the children
        @return true if the alert is removed
        """

    @overload
    def HasAlert(self, theAlert: Message_Alert) -> bool:
        """
        Returns true if the alert belong the list of the child alerts.
        @param theAlert an alert to be checked as a child alert
        @return true if the alert is found in a container of children
        """

    @overload
    def HasAlert(self, theType: nanoocp.Standard.Standard_Type, theGravity: Message_Gravity) -> bool:
        """
        Returns true if specific type of alert is recorded with specified gravity
        @param theType an alert type
        @param theGravity an alert gravity
        @return true if the alert is found in a container of children
        """

    @overload
    def Clear(self) -> None:
        """Clears all collected alerts"""

    @overload
    def Clear(self, theGravity: Message_Gravity) -> None:
        """
        Clears collected alerts with specified gravity
        @param theGravity an alert gravity
        """

    @overload
    def Clear(self, theType: nanoocp.Standard.Standard_Type) -> None:
        """
        Clears collected alerts with specified type
        @param theType an alert type
        """

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

class Message_ProgressScope:
    """
    Message_ProgressScope class provides convenient way to advance progress
    indicator in context of complex program organized in hierarchical way,
    where usually it is difficult (or even not possible) to consider process
    as linear with fixed step.

    On every level (sub-operation) in hierarchy of operations
    the local instance of the Message_ProgressScope class is created.
    It takes a part of the upper-level scope (via Message_ProgressRange) and provides
    a way to consider this part as independent scale with locally defined range.

    The position on the local scale may be advanced using the method Next(),
    which allows iteration-like advancement. This method can take argument to
    advance by the specified value (with default step equal to 1).
    This method returns Message_ProgressRange object that takes responsibility
    of making the specified step, either directly at its destruction or by
    delegating this task to another sub-scope created from that range object.

    It is important that sub-scope must have life time less than
    the life time of its parent scope that provided the range.
    The usage pattern is to create scope objects as local variables in the
    functions that do the job, and pass range objects returned by Next() to
    the functions of the lower level, to allow them creating their own scopes.

    The scope has a name that can be used in visualization of the progress.
    It can be null. Note that when C string literal is used as a name, then its
    value is not copied, just pointer is stored. In other variants (char pointer
    or a string class) the string is copied, which is additional overhead.

    The same instance of the progress scope! must not be used concurrently from different threads.
    For the algorithm running its tasks in parallel threads, a common scope is
    created before the parallel execution, and the range objects produced by method
    Next() are used to initialise the data pertinent to each task.
    Then the progress is advanced within each task using its own range object.
    See example below.

    Note that while a range of the scope is specified using double
    (double) parameter, it is expected to be a positive integer value.
    If the range is not an integer, method Next() shall be called with
    explicit step argument, and the rounded value returned by method Value()
    may be not coherent with the step and range.

    A scope can be created with option "infinite". This is useful when
    the number of steps is not known by the time of the scope creation.
    In this case the progress will be advanced logarithmically, approaching
    the end of the scope at infinite number of steps. The parameter Max
    for infinite scope indicates number of steps corresponding to mid-range.

    A progress scope created with empty constructor is not connected to any
    progress indicator, and passing the range created on it to any algorithm
    allows it executing safely without actual progress indication.

    Example of preparation of progress indicator:

    @code{.cpp}
    occ::handle<Message_ProgressIndicator> aProgress = ...; // assume it can be null
    func (Message_ProgressIndicator::Start (aProgress));
    @endcode

    Example of usage in sequential process:

    @code{.cpp}
    Message_ProgressScope aWholePS(aRange, "Whole process", 100);

    // do one step taking 20%
    func1 (aWholePS.Next (20)); // func1 will take 20% of the whole scope
    if (aWholePS.UserBreak()) // exit prematurely if the user requested break
    return;

    // ... do next step taking 50%
    func2 (aWholePS.Next (50));
    if (aWholePS.UserBreak())
    return;
    @endcode

    Example of usage in nested cycle:

    @code{.cpp}
    // Outer cycle
    Message_ProgressScope anOuter (theProgress, "Outer", nbOuter);
    for (int i = 0; i < nbOuter && anOuter.More(); i++)
    {
    // Inner cycle
    Message_ProgressScope anInner (anOuter.Next(), "Inner", nbInner);
    for (int j = 0; j < nbInner && anInner.More(); j++)
    {
    // Cycle body
    func (anInner.Next());
    }
    }
    @endcode

    Example of use in function:

    @code{.cpp}
    //! Implementation of iterative algorithm showing its progress
    func (const Message_ProgressRange& theProgress)
    {
    // Create local scope covering the given progress range.
    // Set this scope to count aNbSteps steps.
    Message_ProgressScope aScope (theProgress, "", aNbSteps);
    for (int i = 0; i < aNbSteps && aScope.More(); i++)
    {
    // Optional: pass range returned by method Next() to the nested algorithm
    // to allow it to show its progress too (by creating its own scope object).
    // In any case the progress will advance to the next step by the end of the func2 call.
    func2 (aScope.Next());
    }
    }
    @endcode

    Example of usage in parallel process:

    @code{.cpp}
    struct Task
    {
    Data& Data;
    Message_ProgressRange Range;

    Task (const Data& theData, const Message_ProgressRange& theRange)
    : Data (theData), Range (theRange) {}
    };
    struct Functor
    {
    void operator() (Task& theTask) const
    {
    // Note: it is essential that this method is executed only once for the same Task object
    Message_ProgressScope aPS (theTask.Range, NULL, theTask.Data.NbItems);
    for (int i = 0; i < theTask.Data.NbSteps && aPS.More(); i++)
    {
    do_job (theTask.Data.Item[i], aPS.Next());
    }
    }
    };
    ...
    {
    std::vector<Data> aData = ...;
    std::vector<Task> aTasks;

    Message_ProgressScope aPS (aRootRange, "Data processing", aData.size());
    for (int i = 0; i < aData.size(); ++i)
    aTasks.push_back (Task (aData[i], aPS.Next()));

    OSD_Parallel::ForEach (aTasks.begin(), aTasks.end(), Functor());
    }
    @endcode

    For lightweight algorithms that do not need advancing the progress
    within individual tasks the code can be simplified to avoid inner scopes:

    @code
    struct Functor
    {
    void operator() (Task& theTask) const
    {
    if (theTask.Range.More())
    {
    do_job (theTask.Data);
    // advance the progress
    theTask.Range.Close();
    }
    }
    };
    @endcode
    """

    @overload
    def __init__(self) -> None:
        """
        @name Preparation methods
        Creates dummy scope.
        It can be safely passed to algorithms; no progress indication will be done.
        """

    @overload
    def __init__(self, theRange: Message_ProgressRange, theName: nanoocp.TCollection.TCollection_AsciiString, theMax: float, isInfinite: bool = False) -> None:
        """
        Creates a new scope taking responsibility of the part of the progress
        scale described by theRange. The new scope has own range from 0 to
        theMax, which is mapped to the given range.

        The topmost scope is created and owned by Message_ProgressIndicator
        and its pointer is contained in the Message_ProgressRange returned by the Start() method of
        progress indicator.

        @param[in][out] theRange  range to fill (will be disarmed)
        @param[in] theName        new scope name
        @param[in] theMax         number of steps in scope
        @param[in] isInfinite     infinite flag
        """

    def SetName(self, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets the name of the scope."""

    def UserBreak(self) -> bool:
        """
        @name Advance by iterations
        Returns true if ProgressIndicator signals UserBreak
        """

    def More(self) -> bool:
        """Returns false if ProgressIndicator signals UserBreak"""

    def Next(self, theStep: float = 1.0) -> Message_ProgressRange:
        """
        Advances position by specified step and returns the range
        covering this step
        """

    def Show(self) -> None:
        """
        @name Auxiliary methods to use in ProgressIndicator
        Force update of presentation of the progress indicator.
        Should not be called concurrently.
        """

    def IsActive(self) -> bool:
        """Returns true if this progress scope is attached to some indicator."""

    def Name(self) -> str:
        """
        Returns the name of the scope (may be null).
        Scopes with null name (e.g. root scope) should
        be bypassed when reporting progress to the user.
        """

    def Parent(self) -> Message_ProgressScope:
        """Returns parent scope (null for top-level scope)"""

    def MaxValue(self) -> float:
        """Returns the maximal value of progress in this scope"""

    def Value(self) -> float:
        """
        Returns the current value of progress in this scope.

        The value is computed by mapping current global progress into
        this scope range; the result is rounded up to integer.
        Note that if MaxValue() is not an integer, Value() can be
        greater than MaxValue() due to that rounding.

        This method should not be called concurrently while the progress
        is advancing, except from implementation of method Show() in
        descendant of Message_ProgressIndicator.
        """

    def IsInfinite(self) -> bool:
        """Returns the infinite flag"""

    def GetPortion(self) -> float:
        """Get the portion of the indicator covered by this scope (from 0 to 1)"""

    def Close(self) -> None:
        """
        Closes the scope and advances the progress to its end.
        Closed scope should not be used.
        """

class Message_ProgressRange:
    """
    Auxiliary class representing a part of the global progress scale allocated by
    a step of the progress scope, see Message_ProgressScope::Next().

    A range object takes responsibility of advancing the progress by the size of
    allocated step, which is then performed depending on how it is used:

    - If Message_ProgressScope object is created using this range as argument, then
    this respondibility is taken over by that scope.

    - Otherwise, a range advances progress directly upon destruction.

    A range object can be copied, the responsibility for progress advancement is
    then taken by the copy.
    The same range object may be used (either copied or used to create scope) only once.
    Any consequent attempts to use range will give no result on the progress;
    in debug mode, an assert message will be generated.

    @sa Message_ProgressScope for more details
    """

    @overload
    def __init__(self) -> None:
        """Constructor of the empty range"""

    @overload
    def __init__(self, theOther: Message_ProgressRange) -> None:
        """Copy constructor disarms the source"""

    def UserBreak(self) -> bool:
        """Returns true if ProgressIndicator signals UserBreak"""

    def More(self) -> bool:
        """Returns false if ProgressIndicator signals UserBreak"""

    def IsActive(self) -> bool:
        """Returns true if this progress range is attached to some indicator."""

    def Close(self) -> None:
        """Closes the current range and advances indicator"""

class Message_ProgressIndicator(nanoocp.Standard.Standard_Transient):
    """
    Defines abstract interface from program to the user.
    This includes progress indication and user break mechanisms.

    The progress indicator controls the progress scale with range from 0 to 1.

    Method Start() should be called once, at the top level of the call stack,
    to reset progress indicator and get access to the root range:

    @code{.cpp}
    occ::handle<Message_ProgressIndicator> aProgress = ...;
    anAlgorithm.Perform (aProgress->Start());
    @endcode

    To advance the progress indicator in the algorithm,
    use the class Message_ProgressScope that provides iterator-like
    interface for incrementing progress; see documentation of that
    class for details.
    The object of class Message_ProgressRange will automatically advance
    the indicator if it is not passed to any Message_ProgressScope.

    The progress indicator supports concurrent processing and
    can be used in multithreaded applications.

    The derived class should be created to connect this interface to
    actual implementation of progress indicator, to take care of visualization
    of the progress (e.g. show total position at the graphical bar,
    print scopes in text mode, or else), and for implementation
    of user break mechanism (if necessary).

    See details in documentation of methods Show() and UserBreak().
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Start(self) -> Message_ProgressRange:
        """
        Resets the indicator to zero, calls Reset(), and returns the range.
        This range refers to the scope that has no name and is initialized
        with max value 1 and step 1.
        Use this method to get the top level range for progress indication.
        """

    @staticmethod
    def Start_s(theProgress: Message_ProgressIndicator) -> Message_ProgressRange:
        """
        If argument is non-null handle, returns theProgress->Start().
        Otherwise, returns dummy range that can be safely used in the algorithms
        but not bound to progress indicator.
        """

    def GetPosition(self) -> float:
        """
        Returns total progress position ranged from 0 to 1.
        Should not be called concurrently while the progress is advancing,
        except from implementation of method Show().
        """

class Message_LazyProgressScope:
    """
    Progress scope with lazy updates and abort fetches.

    Although Message_ProgressIndicator implementation is encouraged to spare GUI updates,
    even optimized implementation might show a noticeable overhead on a very small update step (e.g.
    per triangle).

    The class splits initial (displayed) number of overall steps into larger chunks specified in
    constructor, so that displayed progress is updated at larger steps.
    """

    def Next(self) -> None:
        """Increment progress with 1."""

    def More(self) -> bool:
        """
        Return TRUE if progress has been aborted - return the cached state lazily updated.
        """

    def IsAborted(self) -> bool:
        """
        Return TRUE if progress has been aborted - fetches actual value from the Progress.
        """

class Message_Level:
    """
    This class is an instance of Sentry to create a level in a message report
    Constructor of the class add new (active) level in the report, destructor removes it
    While the level is active in the report, new alerts are added below the level root alert.

    The first added alert is a root alert, other are added below the root alert

    If alert has Message_AttributeMeter attribute, active metrics of the default report are stored
    in the attribute: start value of metric on adding alert, stop on adding another alert or closing
    (delete) the level in the report.

    Processing of this class is implemented in Message_Report, it is used only inside it.
    Levels using should be only through using OCCT_ADD_MESSAGE_LEVEL_SENTRY only. No other code is
    required outside.
    """

    @overload
    def __init__(self, theName: nanoocp.TCollection.TCollection_AsciiString = ...) -> None:
        """
        Constructor.
        One string key is used for all alert meters.
        The perf meter is not started automatically, it will be done in AddAlert() method
        """

    @overload
    def __init__(self, theOther: Message_Level) -> None: ...

    def RootAlert(self) -> Message_AlertExtended:
        """
        Returns root alert of the level
        @return alert instance or NULL
        """

    def SetRootAlert(self, theAlert: Message_AlertExtended, isRequiredToStart: bool) -> None:
        """
        Sets the root alert. Starts collects alert metrics if active.
        @param theAlert an alert
        """

    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool:
        """
        Adds new alert on the level. Stops the last alert metric, appends the alert and starts the
        alert metrics collecting. Sets root alert beforehand this method using, if the root is NULL,
        it does nothing.
        @param theGravity an alert gravity
        @param theAlert an alert
        @return true if alert is added
        """

class Message_MsgFile:
    """
    A tool providing facility to load definitions of message strings from
    resource file(s).

    The message file is an ASCII file which defines a set of messages.
    Each message is identified by its keyword (string).

    All lines in the file starting with the exclamation sign
    (perhaps preceding by spaces and/or tabs) are ignored as comments.

    Each line in the file starting with the dot character "."
    (perhaps preceding by spaces and/or tabs) defines the keyword.
    The keyword is a string starting from the next symbol after dot
    and ending at the symbol preceding ending newline character "\\n".

    All the lines in the file after the keyword and before next
    keyword (and which are not comments) define the message for that
    keyword. If the message consists of several lines, the message
    string will contain newline symbols "\\n" between parts (but not
    at the end).

    The experimental support of Unicode message files is provided.
    These are distinguished by two bytes FF.FE or FE.FF at the beginning.

    The loaded messages are stored in static data map; all methods of that
    class are also static.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Message_MsgFile) -> None: ...

    @staticmethod
    def Load(theDirName: str, theFileName: str) -> bool:
        """
        Load message file <theFileName> from directory <theDirName>
        or its sub-directory
        """

    @staticmethod
    def LoadFile(theFName: str) -> bool:
        """
        Load the messages from the given file, additive to any previously
        loaded messages. Messages with same keywords, if already present,
        are replaced with the new ones.
        """

    @staticmethod
    def LoadFromEnv(theEnvName: str, theFileName: str, theLangExt: str = '') -> bool:
        """
        Loads the messages from the file with name (without extension) given by environment variable.
        Extension of the file name is given separately. If its not defined, it is taken:
        - by default from environment CSF_LANGUAGE,
        - if not defined either, as "us".
        @name theEnvName  environment variable name
        @name theFileName file name without language suffix
        @name theLangExt  language file name extension
        @return TRUE on success
        """

    @staticmethod
    def LoadFromString(theContent: str, theLength: int = -1) -> bool:
        """
        Loads the messages from the given text buffer.
        @param theContent string containing the messages
        @param theLength  length of the buffer;
        when -1 specified - theContent will be considered as NULL-terminated string
        """

    @staticmethod
    def AddMsg(key: nanoocp.TCollection.TCollection_AsciiString, text: nanoocp.TCollection.TCollection_ExtendedString) -> bool:
        """
        Adds new message to the map. Parameter <key> gives
        the key of the message, <text> defines the message itself.
        If there already was defined the message identified by the
        same keyword, it is replaced with the new one.
        """

    @staticmethod
    def HasMsg(key: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns True if message with specified keyword is registered"""

    @overload
    @staticmethod
    def Msg(key: str) -> nanoocp.TCollection.TCollection_ExtendedString: ...

    @overload
    @staticmethod
    def Msg(key: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_ExtendedString:
        """
        Gives the text for the message identified by the keyword <key>.
        If there are no messages with such keyword defined, the error message is returned.
        In that case reference to static string is returned, it can be changed with next call(s) to
        Msg(). Note: The error message is constructed like 'Unknown message: <key>', and can itself be
        customized by defining message with key Message_Msg_BadKeyword.
        """

class Message_PrinterOStream(Message_Printer):
    """
    Implementation of a message printer associated with an std::ostream
    The std::ostream may be either externally defined one (e.g. std::cout),
    or file stream maintained internally (depending on constructor).
    """

    @overload
    def __init__(self, theTraceLevel: Message_Gravity = Message_Gravity.Message_Info) -> None:
        """Empty constructor, defaulting to cout"""

    @overload
    def __init__(self, theFileName: str, theDoAppend: bool, theTraceLevel: Message_Gravity = Message_Gravity.Message_Info) -> None:
        """
        Create printer for output to a specified file.
        The option theDoAppend specifies whether file should be
        appended or rewritten.
        For specific file names (cout, cerr) standard streams are used
        """

    @overload
    def __init__(self, theOther: Message_PrinterOStream) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Close(self) -> None:
        """
        Flushes the output stream and destroys it if it has been
        specified externally with option doFree (or if it is internal
        file stream)
        """

    def ToColorize(self) -> bool:
        """
        Returns TRUE if text output into console should be colorized depending on message gravity;
        TRUE by default.
        """

    def SetToColorize(self, theToColorize: bool) -> None:
        """
        Set if text output into console should be colorized depending on message gravity.
        """

class Message_PrinterSystemLog(Message_Printer):
    """
    Implementation of a message printer associated with system log.
    Implemented for the following systems:
    - Windows, through ReportEventW().
    - Android, through __android_log_write().
    - UNIX/Linux, through syslog().
    """

    @overload
    def __init__(self, theEventSourceName: nanoocp.TCollection.TCollection_AsciiString, theTraceLevel: Message_Gravity = Message_Gravity.Message_Info) -> None:
        """Main constructor."""

    @overload
    def __init__(self, theOther: Message_PrinterSystemLog) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Message_PrinterToReport(Message_Printer):
    """
    Implementation of a message printer associated with Message_Report
    Send will create a new alert of the report. If string is sent, an alert is created by Eol only.
    The alerts are sent into set report or default report of Message.
    """

    @overload
    def __init__(self) -> None:
        """Create printer for redirecting messages into report."""

    @overload
    def __init__(self, theOther: Message_PrinterToReport) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Report(self) -> Message_Report:
        """Returns the current or default report"""

    def SetReport(self, theReport: Message_Report) -> None:
        """
        Sets the printer report
        @param theReport report for messages processing, if NULL, the default report is used
        """

    def SendStringStream(self, theStream: TextIO, theGravity: Message_Gravity) -> None:
        """
        Send a string message with specified trace level.
        Stream is converted to string value.
        Default implementation calls first method Send().
        """

    def SendObject(self, theObject: nanoocp.Standard.Standard_Transient, theGravity: Message_Gravity) -> None:
        """
        Send a string message with specified trace level.
        The object is converted to string in format: <object kind> : <object pointer>.
        The parameter theToPutEol specified whether end-of-line should be added to the end of the
        message. Default implementation calls first method Send().
        """

class Message_ProgressSentry(Message_ProgressScope):
    """
    Functionality of this class (Message_ProgressSentry) has been superseded by
    Message_ProgressScope. This class is kept just to simplify transition of an old code and will be
    removed in future.
    """

    def __init__(self, theRange: Message_ProgressRange, theName: str, theMin: float, theMax: float, theStep: float, theIsInf: bool = False, theNewScopeSpan: float = 0.0) -> None:
        """
        Deprecated constructor, Message_ProgressScope should be created instead.
        """

    def Relieve(self) -> None:
        """Method Relieve() was replaced by Close() in Message_ProgressScope"""

class Message_Report(nanoocp.Standard.Standard_Transient):
    """
    Container for alert messages, sorted according to their gravity.

    For each gravity level, alerts are stored in simple list.
    If alert being added can be merged with another alert of the same
    type already in the list, it is merged and not added to the list.

    This class is intended to be used as follows:

    - In the process of execution, algorithm fills report by alert objects
    using methods AddAlert()

    - The result can be queried for presence of particular alert using
    methods HasAlert()

    - The reports produced by nested or sequentially executed algorithms
    can be collected in one using method Merge()

    - The report can be shown to the user either as plain text with method
    Dump() or in more advanced way, by iterating over lists returned by GetAlerts()

    - Report can be cleared by methods Clear() (usually after reporting)

    Message_PrinterToReport is a printer in Messenger to convert data sent to messenger into report
    """

    def __init__(self) -> None:
        """Empty constructor"""

    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> None:
        """
        Add alert with specified gravity.
        This method is thread-safe, i.e. alerts can be added from parallel threads safely.
        """

    def GetAlerts(self, theGravity: Message_Gravity) -> nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Alert]:
        """Returns list of collected alerts with specified gravity"""

    @overload
    def HasAlert(self, theType: nanoocp.Standard.Standard_Type) -> bool:
        """Returns true if specific type of alert is recorded"""

    @overload
    def HasAlert(self, theType: nanoocp.Standard.Standard_Type, theGravity: Message_Gravity) -> bool:
        """
        Returns true if specific type of alert is recorded with specified gravity
        """

    def IsActiveInMessenger(self, theMessenger: Message_Messenger = None) -> bool:
        """
        Returns true if a report printer for the current report is registered in the messenger
        @param theMessenger the messenger. If it's NULL, the default messenger is used
        """

    def ActivateInMessenger(self, toActivate: bool, theMessenger: Message_Messenger = None) -> None:
        """
        Creates an instance of Message_PrinterToReport with the current report and register it in
        messenger
        @param toActivate if true, activated else deactivated
        @param theMessenger the messenger. If it's NULL, the default messenger is used
        """

    def UpdateActiveInMessenger(self, theMessenger: Message_Messenger = None) -> None:
        """
        Updates internal flag IsActiveInMessenger.
        It becomes true if messenger contains at least one instance of Message_PrinterToReport.
        @param theMessenger the messenger. If it's NULL, the default messenger is used
        """

    def AddLevel(self, theLevel: Message_Level, theName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Add new level of alerts
        @param theLevel a level
        """

    def RemoveLevel(self, theLevel: Message_Level) -> None:
        """Remove level of alerts"""

    @overload
    def Clear(self) -> None:
        """Clears all collected alerts"""

    @overload
    def Clear(self, theGravity: Message_Gravity) -> None:
        """Clears collected alerts with specified gravity"""

    @overload
    def Clear(self, theType: nanoocp.Standard.Standard_Type) -> None:
        """Clears collected alerts with specified type"""

    def ActiveMetrics(self) -> nanoocp.NCollection.NCollection_IndexedMap[nanoocp.Message.Message_MetricType]:
        """Returns computed metrics when alerts are performed"""

    def SetActiveMetric(self, theMetricType: Message_MetricType, theActivate: bool) -> None:
        """
        Sets metrics to compute when alerts are performed
        @param theMetrics container of metrics
        """

    def ClearMetrics(self) -> None:
        """Removes all activated metrics"""

    def Limit(self) -> int:
        """
        Returns maximum number of collecting alerts. If the limit is achieved,
        first alert is removed, the new alert is added in the container.
        @return the limit value
        """

    def SetLimit(self, theLimit: int) -> None:
        """
        Sets maximum number of collecting alerts.
        @param theLimit limit value
        """

    @overload
    def Dump(self) -> object:
        """Dumps all collected alerts to stream"""

    @overload
    def Dump(self, theGravity: Message_Gravity) -> object:
        """Dumps collected alerts with specified gravity to stream"""

    @overload
    def SendMessages(self, theMessenger: Message_Messenger) -> None:
        """Sends all collected alerts to messenger."""

    @overload
    def SendMessages(self, theMessenger: Message_Messenger, theGravity: Message_Gravity) -> None:
        """
        Dumps collected alerts with specified gravity to messenger.
        Default implementation creates Message_Msg object with a message
        key returned by alert, and sends it in the messenger.
        """

    @overload
    def Merge(self, theOther: Message_Report) -> None:
        """Merges data from theOther report into this"""

    @overload
    def Merge(self, theOther: Message_Report, theGravity: Message_Gravity) -> None:
        """Merges alerts with specified gravity from theOther report into this"""

    def DumpJson(self, theDepth: int = -1) -> object:
        """Dumps the content of me into the stream"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Message
Message_ListOfAlert = nanoocp.NCollection.NCollection_List[nanoocp.Message.Message_Alert]
Message_SequenceOfPrinters = nanoocp.NCollection.NCollection_Sequence[nanoocp.Message.Message_Printer]
