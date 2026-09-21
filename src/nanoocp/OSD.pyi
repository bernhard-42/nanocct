"""OCCT package OSD (toolkit TKernel)"""

import enum
from typing import overload

import nanoocp.Quantity
import nanoocp.Standard
import nanoocp.TCollection


class OSD_SignalMode(enum.IntEnum):
    """Mode of operation for OSD::SetSignal() function"""

    OSD_SignalMode_AsIs = 0

    OSD_SignalMode_Set = 1

    OSD_SignalMode_SetUnhandled = 2

    OSD_SignalMode_Unset = 3

OSD_SignalMode_AsIs: OSD_SignalMode = OSD_SignalMode.OSD_SignalMode_AsIs

OSD_SignalMode_Set: OSD_SignalMode = OSD_SignalMode.OSD_SignalMode_Set

OSD_SignalMode_SetUnhandled: OSD_SignalMode = OSD_SignalMode.OSD_SignalMode_SetUnhandled

OSD_SignalMode_Unset: OSD_SignalMode = OSD_SignalMode.OSD_SignalMode_Unset

class OSD_SysType(enum.IntEnum):
    """
    Thisd is a set of possible system types.
    'Default' means SysType of machine operating this process.
    This can be used with the Path class.
    All UNIX-like are grouped under "UnixBSD" or "UnixSystemV".
    Such systems are Solaris, NexTOS ...
    A category of systems accept MSDOS-like path such as
    WindowsNT and OS2.
    """

    OSD_Unknown = 0

    OSD_Default = 1

    OSD_UnixBSD = 2

    OSD_UnixSystemV = 3

    OSD_VMS = 4

    OSD_OS2 = 5

    OSD_OSF = 6

    OSD_MacOs = 7

    OSD_Taligent = 8

    OSD_WindowsNT = 9

    OSD_LinuxREDHAT = 10

    OSD_Aix = 11

OSD_Unknown: OSD_SysType = OSD_SysType.OSD_Unknown

OSD_Default: OSD_SysType = OSD_SysType.OSD_Default

OSD_UnixBSD: OSD_SysType = OSD_SysType.OSD_UnixBSD

OSD_UnixSystemV: OSD_SysType = OSD_SysType.OSD_UnixSystemV

OSD_VMS: OSD_SysType = OSD_SysType.OSD_VMS

OSD_OS2: OSD_SysType = OSD_SysType.OSD_OS2

OSD_OSF: OSD_SysType = OSD_SysType.OSD_OSF

OSD_MacOs: OSD_SysType = OSD_SysType.OSD_MacOs

OSD_Taligent: OSD_SysType = OSD_SysType.OSD_Taligent

OSD_WindowsNT: OSD_SysType = OSD_SysType.OSD_WindowsNT

OSD_LinuxREDHAT: OSD_SysType = OSD_SysType.OSD_LinuxREDHAT

OSD_Aix: OSD_SysType = OSD_SysType.OSD_Aix

class OSD_WhoAmI(enum.IntEnum):
    """
    Allows great accuracy for error management.
    This is private.
    """

    OSD_WDirectory = 0

    OSD_WDirectoryIterator = 1

    OSD_WEnvironment = 2

    OSD_WFile = 3

    OSD_WFileNode = 4

    OSD_WFileIterator = 5

    OSD_WPath = 6

    OSD_WProcess = 7

    OSD_WProtection = 8

    OSD_WHost = 9

    OSD_WDisk = 10

    OSD_WChronometer = 11

    OSD_WTimer = 12

    OSD_WPackage = 13

    OSD_WEnvironmentIterator = 14

OSD_WDirectory: OSD_WhoAmI = OSD_WhoAmI.OSD_WDirectory

OSD_WDirectoryIterator: OSD_WhoAmI = OSD_WhoAmI.OSD_WDirectoryIterator

OSD_WEnvironment: OSD_WhoAmI = OSD_WhoAmI.OSD_WEnvironment

OSD_WFile: OSD_WhoAmI = OSD_WhoAmI.OSD_WFile

OSD_WFileNode: OSD_WhoAmI = OSD_WhoAmI.OSD_WFileNode

OSD_WFileIterator: OSD_WhoAmI = OSD_WhoAmI.OSD_WFileIterator

OSD_WPath: OSD_WhoAmI = OSD_WhoAmI.OSD_WPath

OSD_WProcess: OSD_WhoAmI = OSD_WhoAmI.OSD_WProcess

OSD_WProtection: OSD_WhoAmI = OSD_WhoAmI.OSD_WProtection

OSD_WHost: OSD_WhoAmI = OSD_WhoAmI.OSD_WHost

OSD_WDisk: OSD_WhoAmI = OSD_WhoAmI.OSD_WDisk

OSD_WChronometer: OSD_WhoAmI = OSD_WhoAmI.OSD_WChronometer

OSD_WTimer: OSD_WhoAmI = OSD_WhoAmI.OSD_WTimer

OSD_WPackage: OSD_WhoAmI = OSD_WhoAmI.OSD_WPackage

OSD_WEnvironmentIterator: OSD_WhoAmI = OSD_WhoAmI.OSD_WEnvironmentIterator

class OSD_FromWhere(enum.IntEnum):
    """Used by OSD_File in the method Seek."""

    OSD_FromBeginning = 0

    OSD_FromHere = 1

    OSD_FromEnd = 2

OSD_FromBeginning: OSD_FromWhere = OSD_FromWhere.OSD_FromBeginning

OSD_FromHere: OSD_FromWhere = OSD_FromWhere.OSD_FromHere

OSD_FromEnd: OSD_FromWhere = OSD_FromWhere.OSD_FromEnd

class OSD_KindFile(enum.IntEnum):
    """Specifies the type of files."""

    OSD_FILE = 0

    OSD_DIRECTORY = 1

    OSD_LINK = 2

    OSD_SOCKET = 3

    OSD_UNKNOWN = 4

OSD_FILE: OSD_KindFile = OSD_KindFile.OSD_FILE

OSD_DIRECTORY: OSD_KindFile = OSD_KindFile.OSD_DIRECTORY

OSD_LINK: OSD_KindFile = OSD_KindFile.OSD_LINK

OSD_SOCKET: OSD_KindFile = OSD_KindFile.OSD_SOCKET

OSD_UNKNOWN: OSD_KindFile = OSD_KindFile.OSD_UNKNOWN

class OSD_LockType(enum.IntEnum):
    """
    locks for files.
    NoLock is the default value when opening a file.

    ReadLock allows only one reading of the file at a time.

    WriteLock prevents others writing into a file(excepted the user
    who puts the lock)but allows everybody to read.

    ExclusiveLock prevents reading and writing except for the
    current user of the file.
    So ExclusiveLock means only one user on the file and this
    user is the one who puts the lock.
    """

    OSD_NoLock = 0

    OSD_ReadLock = 1

    OSD_WriteLock = 2

    OSD_ExclusiveLock = 3

OSD_NoLock: OSD_LockType = OSD_LockType.OSD_NoLock

OSD_ReadLock: OSD_LockType = OSD_LockType.OSD_ReadLock

OSD_WriteLock: OSD_LockType = OSD_LockType.OSD_WriteLock

OSD_ExclusiveLock: OSD_LockType = OSD_LockType.OSD_ExclusiveLock

class OSD_OpenMode(enum.IntEnum):
    """Specifies the file open mode."""

    OSD_ReadOnly = 0

    OSD_WriteOnly = 1

    OSD_ReadWrite = 2

OSD_ReadOnly: OSD_OpenMode = OSD_OpenMode.OSD_ReadOnly

OSD_WriteOnly: OSD_OpenMode = OSD_OpenMode.OSD_WriteOnly

OSD_ReadWrite: OSD_OpenMode = OSD_OpenMode.OSD_ReadWrite

class OSD_OEMType(enum.IntEnum):
    """
    This is set of possible machine types
    used in OSD_Host::MachineType
    """

    OSD_Unavailable = 0

    OSD_SUN = 1

    OSD_DEC = 2

    OSD_SGI = 3

    OSD_NEC = 4

    OSD_MAC = 5

    OSD_PC = 6

    OSD_HP = 7

    OSD_IBM = 8

    OSD_VAX = 9

    OSD_LIN = 10

    OSD_AIX = 11

OSD_Unavailable: OSD_OEMType = OSD_OEMType.OSD_Unavailable

OSD_SUN: OSD_OEMType = OSD_OEMType.OSD_SUN

OSD_DEC: OSD_OEMType = OSD_OEMType.OSD_DEC

OSD_SGI: OSD_OEMType = OSD_OEMType.OSD_SGI

OSD_NEC: OSD_OEMType = OSD_OEMType.OSD_NEC

OSD_MAC: OSD_OEMType = OSD_OEMType.OSD_MAC

OSD_PC: OSD_OEMType = OSD_OEMType.OSD_PC

OSD_HP: OSD_OEMType = OSD_OEMType.OSD_HP

OSD_IBM: OSD_OEMType = OSD_OEMType.OSD_IBM

OSD_VAX: OSD_OEMType = OSD_OEMType.OSD_VAX

OSD_LIN: OSD_OEMType = OSD_OEMType.OSD_LIN

OSD_AIX: OSD_OEMType = OSD_OEMType.OSD_AIX

class OSD_LoadMode(enum.IntEnum):
    """This enumeration is used to load shareable libraries."""

    OSD_RTLD_LAZY = 0

    OSD_RTLD_NOW = 1

OSD_RTLD_LAZY: OSD_LoadMode = OSD_LoadMode.OSD_RTLD_LAZY

OSD_RTLD_NOW: OSD_LoadMode = OSD_LoadMode.OSD_RTLD_NOW

class OSD_SingleProtection(enum.IntEnum):
    """
    Access rights for files.
    R means Read, W means Write, X means eXecute and D means Delete.
    On UNIX, the right to Delete is combined with Write access.
    So if "W"rite is not set and "D"elete is, "W"rite will be set
    and if "W" is set, "D" will be too.
    """

    OSD_None = 0

    OSD_R = 1

    OSD_W = 2

    OSD_RW = 3

    OSD_X = 4

    OSD_RX = 5

    OSD_WX = 6

    OSD_RWX = 7

    OSD_D = 8

    OSD_RD = 9

    OSD_WD = 10

    OSD_RWD = 11

    OSD_XD = 12

    OSD_RXD = 13

    OSD_WXD = 14

    OSD_RWXD = 15

OSD_None: OSD_SingleProtection = OSD_SingleProtection.OSD_None

OSD_R: OSD_SingleProtection = OSD_SingleProtection.OSD_R

OSD_W: OSD_SingleProtection = OSD_SingleProtection.OSD_W

OSD_RW: OSD_SingleProtection = OSD_SingleProtection.OSD_RW

OSD_X: OSD_SingleProtection = OSD_SingleProtection.OSD_X

OSD_RX: OSD_SingleProtection = OSD_SingleProtection.OSD_RX

OSD_WX: OSD_SingleProtection = OSD_SingleProtection.OSD_WX

OSD_RWX: OSD_SingleProtection = OSD_SingleProtection.OSD_RWX

OSD_D: OSD_SingleProtection = OSD_SingleProtection.OSD_D

OSD_RD: OSD_SingleProtection = OSD_SingleProtection.OSD_RD

OSD_WD: OSD_SingleProtection = OSD_SingleProtection.OSD_WD

OSD_RWD: OSD_SingleProtection = OSD_SingleProtection.OSD_RWD

OSD_XD: OSD_SingleProtection = OSD_SingleProtection.OSD_XD

OSD_RXD: OSD_SingleProtection = OSD_SingleProtection.OSD_RXD

OSD_WXD: OSD_SingleProtection = OSD_SingleProtection.OSD_WXD

OSD_RWXD: OSD_SingleProtection = OSD_SingleProtection.OSD_RWXD

class OSD:
    """Set of Operating System Dependent (OSD) tools."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OSD) -> None: ...

    @overload
    @staticmethod
    def SetSignal(theSignalMode: OSD_SignalMode, theFloatingSignal: bool) -> None:
        """
        Sets or removes signal and FPE (floating-point exception) handlers.
        OCCT signal handlers translate signals raised by C subsystem to C++
        exceptions inheriting Standard_Failure.

        ### Windows-specific notes

        Compiled with MS VC++ sets 3 main handlers:
        @li Signal handlers (via ::signal() functions) that translate system signals
        (SIGSEGV, SIGFPE, SIGILL) into C++ exceptions (classes inheriting
        Standard_Failure). They only be called if function ::raise() is called
        with one of supported signal type set.
        @li Exception handler OSD::WntHandler() (via ::SetUnhandledExceptionFilter())
        that will be used when user's code is compiled with /EHs option.
        @li Structured exception (SE) translator (via _set_se_translator()) that
        translates SE exceptions (aka asynchronous exceptions) into the
        C++ exceptions inheriting Standard_Failure. This translator will be
        used when user's code is compiled with /EHa option.

        This approach ensures that regardless of the option the user chooses to
        compile his code with (/EHs or /EHa), signals (or SE exceptions) will be
        translated into Open CASCADE C++ exceptions.

        MinGW should use SEH exception mode for signal handling to work.

        ### Linux-specific notes

        OSD::SetSignal() sets handlers (via ::sigaction()) for multiple signals
        (SIGFPE, SIGSEGV, etc).

        ### Common notes

        If @a theFloatingSignal is TRUE then floating point exceptions will
        generate SIGFPE in accordance with the mask
        - Windows: _EM_INVALID | _EM_DENORMAL | _EM_ZERODIVIDE | _EM_OVERFLOW,
        see _controlfp() system function.
        - Linux:   FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW,
        see feenableexcept() system function.

        If @a theFloatingSignal is FALSE then floating point calculations will gracefully
        complete regardless of occurred exceptions (e.g. division by zero).
        Otherwise the (thread-specific) FPE flags are set to raise signal if one of
        floating-point exceptions (division by zero, overflow, or invalid operation) occurs.

        The recommended approach is to call OSD::SetSignal() in the beginning of the
        execution of the program, in function main() or its equivalent.
        In multithreaded programs it is advisable to call OSD::SetSignal() or
        OSD::SetThreadLocalSignal() with the same parameters in other threads where
        OCCT is used, to ensure consistency of behavior.

        Note that in order to handle signals as C++ exceptions on Linux and under
        MinGW on Windows it is necessary to compile both OCCT and application with
        OCC_CONVERT_SIGNALS macro, and use macro OCC_CATCH_SIGNALS within each try{}
        block that has to catch this kind of exceptions.

        Refer to documentation of Standard_ErrorHandler.hxx for details.
        """

    @overload
    @staticmethod
    def SetSignal(theFloatingSignal: bool = True) -> None:
        """
        Sets signal and FPE handlers.
        Short-cut for OSD::SetSignal (OSD_SignalMode_Set, theFloatingSignal).
        """

    @staticmethod
    def SetThreadLocalSignal(theSignalMode: OSD_SignalMode, theFloatingSignal: bool) -> None:
        """
        Initializes thread-local signal handlers.
        This includes _set_se_translator() on Windows platform, and SetFloatingSignal().
        The main purpose of this method is initializing handlers for newly created threads
        without overriding global handlers (set by application or by OSD::SetSignal()).
        """

    @staticmethod
    def SetFloatingSignal(theFloatingSignal: bool) -> None:
        """
        Enables / disables generation of C signal on floating point exceptions (FPE).
        This call does NOT register a handler for signal raised in case of FPE -
        SetSignal() should be called beforehand for complete setup.
        Note that FPE setting is thread-local, new threads inherit it from parent.
        """

    @staticmethod
    def SignalMode() -> OSD_SignalMode:
        """
        Returns signal mode set by the last call to SetSignal().
        By default, returns OSD_SignalMode_AsIs.
        """

    @staticmethod
    def ToCatchFloatingSignals() -> bool:
        """
        Returns true if floating point exceptions will raise C signal
        according to current (platform-dependent) settings in this thread.
        """

    @staticmethod
    def SecSleep(theSeconds: int) -> None:
        """Commands the process to sleep for a number of seconds."""

    @staticmethod
    def MilliSecSleep(theMilliseconds: int) -> None:
        """Commands the process to sleep for a number of milliseconds"""

    @staticmethod
    def CStringToReal(aString: str) -> tuple[bool, float]:
        """
        Converts aCstring representing a real with a period as decimal point,
        no thousand separator and no grouping of digits into aReal.

        The conversion is independent from the current locale.
        """

    @staticmethod
    def ControlBreak() -> None:
        """
        since Windows NT does not support 'SIGINT' signal like UNIX,
        then this method checks whether Ctrl-Break keystroke was or
        not. If yes then raises Exception_CTRL_BREAK.
        """

    @staticmethod
    def SignalStackTraceLength() -> int:
        """
        Returns a length of stack trace to be put into exception redirected from signal;
        0 by default meaning no stack trace.
        @sa Standard_Failure::GetStackString()
        """

    @staticmethod
    def SetSignalStackTraceLength(theLength: int) -> None:
        """
        Sets a length of stack trace to be put into exception redirected from signal.
        """

class OSD_FileSystem(nanoocp.Standard.Standard_Transient):
    """
    Base interface for a file stream provider.
    It is intended to be implemented for specific file protocol.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def DefaultFileSystem() -> OSD_FileSystem:
        """
        Returns a global file system, which a selector between registered file systems
        (OSD_FileSystemSelector).
        """

    @staticmethod
    def AddDefaultProtocol(theFileSystem: OSD_FileSystem | None, theIsPreferred: bool = False) -> None:
        """
        Registers file system within the global file system selector returned by
        OSD_FileSystem::DefaultFileSystem(). Note that registering protocols is not thread-safe
        operation and expected to be done once at application startup.
        @param[in] theFileSystem  file system to register
        @param[in] theIsPreferred add to the beginning of the list when TRUE, or add to the end
        otherwise
        """

    @staticmethod
    def RemoveDefaultProtocol(theFileSystem: OSD_FileSystem | None) -> None:
        """
        Unregisters file system within the global file system selector returned by
        OSD_FileSystem::DefaultFileSystem().
        """

    def IsSupportedPath(self, theUrl: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns TRUE if URL defines a supported protocol."""

class OSD_CachedFileSystem(OSD_FileSystem):
    """
    File system keeping last stream created by linked file system
    (OSD_FileSystem::DefaultFileSystem() by default) to be reused for opening a stream with the same
    URL. Note that as file is kept in opened state, application will need destroying this object to
    ensure all files being closed. This interface could be handy in context of reading numerous
    objects pointing to the same file (at different offset). Make sure to create a dedicated
    OSD_CachedFileSystem for each working thread to avoid data races.
    """

    @overload
    def __init__(self, theLinkedFileSystem: OSD_FileSystem | None = None) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: OSD_CachedFileSystem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def LinkedFileSystem(self) -> OSD_FileSystem:
        """
        Return linked file system; initialized with OSD_FileSystem::DefaultFileSystem() by default.
        """

    def SetLinkedFileSystem(self, theLinkedFileSystem: OSD_FileSystem | None) -> None:
        """Sets linked file system."""

    def IsSupportedPath(self, theUrl: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns TRUE if URL defines a supported protocol."""

class OSD_Chronometer:
    """
    This class measures CPU time (both user and system) consumed
    by current process or thread. The chronometer can be started
    and stopped multiple times, and measures cumulative time.

    If only the thread is measured, calls to Stop() and Show()
    must occur from the same thread where Start() was called
    (unless chronometer is stopped); otherwise measurement will
    yield false values.
    """

    @overload
    def __init__(self, theThisThreadOnly: bool = False) -> None:
        """
        Initializes a stopped Chronometer.

        If ThisThreadOnly is True, measured CPU time will account
        time of the current thread only; otherwise CPU of the
        process (all threads, and completed children) is measured.
        """

    @overload
    def __init__(self, theOther: OSD_Chronometer) -> None: ...

    def IsStarted(self) -> bool:
        """Return true if timer has been started."""

    def Reset(self) -> None:
        """Stops and Reinitializes the Chronometer."""

    def Restart(self) -> None:
        """Restarts the Chronometer."""

    def Stop(self) -> None:
        """Stops the Chronometer."""

    def Start(self) -> None:
        """
        Starts (after Create or Reset) or restarts (after Stop)
        the chronometer.
        """

    @overload
    def Show(self) -> tuple[float, float]:
        """
        Returns the current CPU user and system time in variables.
        The chronometer can be running (laps Time) or stopped.
        """

    @overload
    def Show(self) -> float:
        """
        Returns the current CPU user time in a variable.
        The chronometer can be running (laps Time) or stopped.
        """

    @overload
    def Show(self) -> None:
        """
        Shows the current CPU user and system time on the
        standard output stream <cout>.
        The chronometer can be running (laps Time) or stopped.
        """

    @overload
    def Show(self) -> object:
        """
        Shows the current CPU user and system time on the output
        stream <os>.
        The chronometer can be running (laps Time) or stopped.
        """

    def UserTimeCPU(self) -> float:
        """
        Returns the current CPU user time in seconds.
        The chronometer can be running (laps Time) or stopped.
        """

    def SystemTimeCPU(self) -> float:
        """
        Returns the current CPU system time in seconds.
        The chronometer can be running (laps Time) or stopped.
        """

    def IsThisThreadOnly(self) -> bool:
        """
        Return TRUE if current thread CPU time should be measured,
        and FALSE to measure all threads CPU time; FALSE by default,
        """

    def SetThisThreadOnly(self, theIsThreadOnly: bool) -> None:
        """
        Set if current thread (TRUE) or all threads (FALSE) CPU time should be measured.
        Will raise exception if Timer is in started state.
        """

    @staticmethod
    def GetProcessCPU() -> tuple[float, float]:
        """
        Returns CPU time (user and system) consumed by the current
        process since its start, in seconds. The actual precision of
        the measurement depends on granularity provided by the system,
        and is platform-specific.
        """

    @staticmethod
    def GetThreadCPU() -> tuple[float, float]:
        """
        Returns CPU time (user and system) consumed by the current
        thread since its start. Note that this measurement is
        platform-specific, as threads are implemented and managed
        differently on different platforms and CPUs.
        """

class OSD_Path:
    @overload
    def __init__(self) -> None:
        """
        Creates a Path object initialized to an empty string.
        i.e. current directory.
        """

    @overload
    def __init__(self, aDependentName: nanoocp.TCollection.TCollection_AsciiString, aSysType: OSD_SysType = OSD_SysType.OSD_Default) -> None:
        """
        Creates a Path object initialized by dependent path.
        ex: OSD_Path me ("/usr/bin/myprog.sh",OSD_UnixBSD);

        OSD_Path me ("sys$common:[syslib]cc.exe",OSD_OSF) will
        raise a ProgramError due to invalid name for this
        type of system.
        In order to avoid a 'ProgramError' , use IsValid(...)
        to ensure you the validity of <aDependentName>.
        Raises ConstructionError when the path is either null
        or contains characters not in range of ' '...'~'.
        """

    @overload
    def __init__(self, aNode: nanoocp.TCollection.TCollection_AsciiString, aUsername: nanoocp.TCollection.TCollection_AsciiString, aPassword: nanoocp.TCollection.TCollection_AsciiString, aDisk: nanoocp.TCollection.TCollection_AsciiString, aTrek: nanoocp.TCollection.TCollection_AsciiString, aName: nanoocp.TCollection.TCollection_AsciiString, anExtension: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Initializes a system independent path.
        By default , the Path conversion will be assumed using
        currently used system.
        A special syntax is used to specify a "aTrek" in an
        independent manner :
        a "|" represents directory separator
        a "^" means directory above (father)
        examples:
        "|usr|bin" - On UNIX -> "/usr/bin"
        - On VMS  -> "[usr.bin]"
        - On MSDOS-> "\\usr\\bin"
        - On MacOs-> ": usr : bin"

        "^|rep"    - On UNIX -> "../rep"
        - On VMS  -> "[-.rep]"
        - On MSDOS -> "..\\rep"
        - On MacOS->  ":: rep"

        "subdir|" - On UNIX -> "subdir/"
        - On VMS  -> "[.subdir.]\"
        """

    @overload
    def __init__(self, theOther: OSD_Path) -> None: ...

    def Values(self, aNode: nanoocp.TCollection.TCollection_AsciiString, aUsername: nanoocp.TCollection.TCollection_AsciiString, aPassword: nanoocp.TCollection.TCollection_AsciiString, aDisk: nanoocp.TCollection.TCollection_AsciiString, aTrek: nanoocp.TCollection.TCollection_AsciiString, aName: nanoocp.TCollection.TCollection_AsciiString, anExtension: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Gets each component of a path."""

    def SetValues(self, aNode: nanoocp.TCollection.TCollection_AsciiString, aUsername: nanoocp.TCollection.TCollection_AsciiString, aPassword: nanoocp.TCollection.TCollection_AsciiString, aDisk: nanoocp.TCollection.TCollection_AsciiString, aTrek: nanoocp.TCollection.TCollection_AsciiString, aName: nanoocp.TCollection.TCollection_AsciiString, anExtension: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets each component of a path."""

    def SystemName(self, FullName: nanoocp.TCollection.TCollection_AsciiString, aType: OSD_SysType = OSD_SysType.OSD_Default) -> None:
        """
        Returns system dependent path
        <aType> is one among Unix,VMS ...
        This function is not private because you may need to
        display system dependent path on a front-end.
        It can be useful when communicating with another system.
        For instance when you want to communicate between VMS and Unix
        to transfer files, or to do a remote procedure call
        using files.
        example :
        OSD_Path myPath ("sparc4", "sga", "secret_passwd",
        "$5$dkb100","|users|examples");
        Internal ( Dependent_name );
        On UNIX  sga"secret_passwd"@sparc4:/users/examples
        On VMS   sparc4"sga secret_passwd"::$5$dkb100:[users.examples]
        Sets each component of a Path giving its system dependent name.
        """

    def ExpandedName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Returns system dependent path resolving logical symbols."""

    @staticmethod
    def IsValid(theDependentName: nanoocp.TCollection.TCollection_AsciiString, theSysType: OSD_SysType = OSD_SysType.OSD_Default) -> bool:
        """Returns TRUE if <theDependentName> is valid for this SysType."""

    def UpTrek(self) -> None:
        """
        This removes the last directory name in <aTrek>
        and returns result.
        ex:  me = "|usr|bin|todo.sh"
        me.UpTrek() gives me = "|usr|todo.sh"
        if <me> contains "|", me.UpTrek() will give again "|"
        without any error.
        """

    def DownTrek(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        This appends a directory name into the Trek.
        ex: me = "|usr|todo.sh"
        me.DownTrek("bin") gives me = "|usr|bin|todo.sh".
        """

    def TrekLength(self) -> int:
        """
        Returns number of components in Trek of <me>.
        ex: me = "|usr|sys|etc|bin"
        me.TrekLength() returns 4.
        """

    @overload
    def RemoveATrek(self, where: int) -> None:
        """
        This removes a component of Trek in <me> at position <where>.
        The first component of Trek is numbered 1.
        ex:   me = "|usr|bin|"
        me.RemoveATrek(1) gives me = "|bin|"
        To avoid a 'NumericError' because of a bad <where>, use
        TrekLength() to know number of components of Trek in <me>.
        """

    @overload
    def RemoveATrek(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        This removes <aName> from <me> in Trek.
        No error is raised if <aName> is not in <me>.
        ex:  me = "|usr|sys|etc|doc"
        me.RemoveATrek("sys") gives me = "|usr|etc|doc".
        """

    def TrekValue(self, where: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns component of Trek in <me> at position <where>.
        ex:  me = "|usr|bin|sys|"
        me.TrekValue(2) returns "bin\"
        """

    def InsertATrek(self, aName: nanoocp.TCollection.TCollection_AsciiString, where: int) -> None:
        """
        This inserts <aName> at position <where> into Trek of <me>.
        ex:  me = "|usr|etc|"
        me.InsertATrek("sys",2) gives me = "|usr|sys|etc\"
        """

    def Node(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Node of <me>."""

    def UserName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns UserName of <me>."""

    def Password(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Password of <me>."""

    def Disk(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Disk of <me>."""

    def Trek(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Trek of <me>."""

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns file name of <me>.
        If <me> hasn't been initialized, it returns an empty AsciiString.
        """

    def Extension(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns my extension name.
        This returns an empty string if path contains no file name.
        """

    def SetNode(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets Node of <me>."""

    def SetUserName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets UserName of <me>."""

    def SetPassword(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets Password of <me>."""

    def SetDisk(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets Disk of <me>."""

    def SetTrek(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets Trek of <me>."""

    def SetName(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Sets file name of <me>.
        If <me> hasn't been initialized, it returns an empty AsciiString.
        """

    def SetExtension(self, aName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Sets my extension name."""

    @staticmethod
    def RelativePath(DirPath: nanoocp.TCollection.TCollection_AsciiString, AbsFilePath: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the relative file path between the absolute directory
        path <DirPath> and the absolute file path <AbsFilePath>.
        If <DirPath> starts with "/", paths are handled as
        on Unix, if it starts with a letter followed by ":", as on
        WNT. In particular on WNT directory names are not key sensitive.
        If handling fails, an empty string is returned.
        """

    @staticmethod
    def AbsolutePath(DirPath: nanoocp.TCollection.TCollection_AsciiString, RelFilePath: nanoocp.TCollection.TCollection_AsciiString) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the absolute file path from the absolute directory path
        <DirPath> and the relative file path returned by RelativePath().
        If the RelFilePath is an absolute path, it is returned and the
        directory path is ignored.
        If handling fails, an empty string is returned.
        """

    @staticmethod
    def FolderAndFileFromPath(theFilePath: nanoocp.TCollection.TCollection_AsciiString, theFolder: nanoocp.TCollection.TCollection_AsciiString, theFileName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Split absolute filepath into folder path and file name.
        Example: IN  theFilePath ='/media/cdrom/image.jpg'
        OUT theFolder   ='/media/cdrom/'
        OUT theFileName ='image.jpg'
        @param[in] theFilePath   file path
        @param[out] theFolder    folder path (with trailing separator)
        @param[out] theFileName  file name
        """

    @staticmethod
    def FileNameAndExtension(theFilePath: nanoocp.TCollection.TCollection_AsciiString, theName: nanoocp.TCollection.TCollection_AsciiString, theExtension: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Return file extension from the name in lower case.
        Extension is expected to be within 20-symbols length, and determined as file name tail after
        last dot. Example: IN  theFilePath ='Image.sbs.JPG'
        OUT theName     ='Image.sbs'
        OUT theFileName ='jpg'
        @param[in] theFilePath    file path
        @param[out] theName       file name without extension
        @param[out] theExtension  file extension in lower case and without dot
        """

    @staticmethod
    def IsDosPath(thePath: str) -> bool:
        """
        Detect absolute DOS-path also used in Windows.
        The total path length is limited to 256 characters.
        Sample path:
        C:\\folder\\file
        @return true if DOS path syntax detected.
        """

    @staticmethod
    def IsNtExtendedPath(thePath: str) -> bool:
        """
        Detect extended-length NT path (can be only absolute).
        Approximate maximum path is 32767 characters.
        Sample path:
        \\\\?\\D:\\very long path
        File I/O functions in the Windows API convert "/" to "\\" as part of converting the name to an
        NT-style name, except when using the "\\\\?\\" prefix.
        @return true if extended-length NT path syntax detected.
        """

    @staticmethod
    def IsUncPath(thePath: str) -> bool:
        """
        UNC is a naming convention used primarily to specify and map network drives in Microsoft
        Windows. Sample path:
        \\\\server\\share\\file
        @return true if UNC path syntax detected.
        """

    @staticmethod
    def IsUncExtendedPath(thePath: str) -> bool:
        """
        Detect extended-length UNC path.
        Sample path:
        \\\\?\\UNC\\server\\share
        @return true if extended-length UNC path syntax detected.
        """

    @staticmethod
    def IsUnixPath(thePath: str) -> bool:
        """
        Detect absolute UNIX-path.
        Sample path:
        /media/cdrom/file
        @return true if UNIX path syntax detected.
        """

    @staticmethod
    def IsContentProtocolPath(thePath: str) -> bool:
        """
        Detect special URLs on Android platform.
        Sample path:
        content://filename
        @return true if content path syntax detected
        """

    @staticmethod
    def IsRemoteProtocolPath(thePath: str) -> bool:
        """
        Detect remote protocol path (http / ftp / ...).
        Actually shouldn't be remote...
        Sample path:
        http://domain/path/file
        @return true if remote protocol path syntax detected.
        """

    @staticmethod
    def IsRelativePath(thePath: str) -> bool:
        """
        Method to recognize path is absolute or not.
        Detection is based on path syntax - no any filesystem / network access performed.
        @return true if path is incomplete (relative).
        """

    @staticmethod
    def IsAbsolutePath(thePath: str) -> bool:
        """
        Method to recognize path is absolute or not.
        Detection is based on path syntax - no any filesystem / network access performed.
        @return true if path is complete (absolute)
        """

class OSD_Error:
    """Accurate management of OSD specific errors."""

    @overload
    def __init__(self) -> None:
        """
        Initializes Error to be without any Error.
        This is only used by OSD, not by programmer.
        """

    @overload
    def __init__(self, theOther: OSD_Error) -> None: ...

    def Perror(self) -> None:
        """Raises OSD_Error with accurate error message."""

    def SetValue(self, Errcode: int, From: int, Message: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Instantiates error
        This is only used by OSD methods to instantiates an error code.
        No description is done for the programmer.
        """

    def Error(self) -> int:
        """
        Returns an accurate error code.
        To test these values, you must include "OSD_ErrorList.hxx\"
        """

    def Failed(self) -> bool:
        """
        Returns TRUE if an error occurs
        This is a way to test if a system call succeeded or not.
        """

    def Reset(self) -> None:
        """
        Resets error counter to zero
        This allows the user to ignore an error (WARNING).
        """

class OSD_FileNode:
    """
    A class for 'File' and 'Directory' grouping common
    methods (file/directory manipulation tools).
    The "file oriented" name means files or directories which are
    in fact hard coded as files.
    """

    def Path(self, Name: OSD_Path) -> None:
        """Gets file name and path."""

    def SetPath(self, Name: OSD_Path) -> None:
        """
        Sets file name and path.
        If a name is not found, it raises a program error.
        """

    def Exists(self) -> bool:
        """Returns TRUE if <me> exists."""

    def Remove(self) -> None:
        """Erases the FileNode from directory"""

    def Move(self, NewPath: OSD_Path) -> None:
        """Moves <me> into another directory"""

    def Copy(self, ToPath: OSD_Path) -> None:
        """Copies <me> to another FileNode"""

    def Protection(self) -> OSD_Protection:
        """Returns access mode of <me>."""

    def SetProtection(self, Prot: OSD_Protection) -> None:
        """Changes protection of the FileNode"""

    def AccessMoment(self) -> nanoocp.Quantity.Quantity_Date:
        """
        Returns last write access.
        On UNIX, AccessMoment and CreationMoment return the
        same value.
        """

    def CreationMoment(self) -> nanoocp.Quantity.Quantity_Date:
        """
        Returns creation date.
        On UNIX, AccessMoment and CreationMoment return the
        same value.
        """

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_Directory(OSD_FileNode):
    """Management of directories (a set of directory oriented tools)"""

    @overload
    def __init__(self) -> None:
        """
        Creates Directory object.
        It is initialized to an empty name.
        """

    @overload
    def __init__(self, theName: OSD_Path) -> None:
        """Creates Directory object initialized with theName."""

    @overload
    def __init__(self, theOther: OSD_Directory) -> None: ...

    @staticmethod
    def BuildTemporary() -> OSD_Directory:
        """
        Creates a temporary Directory in current directory.
        This directory is automatically removed when object dies.
        """

    def Build(self, Protect: OSD_Protection) -> None:
        """
        Creates (physically) a directory.
        When a directory of the same name already exists, no error is
        returned, and only <Protect> is applied to the existing directory.

        If Build is used and <me> is instantiated without a name,
        OSDError is raised.
        """

class OSD_DirectoryIterator:
    """
    Manages a breadth-only search for sub-directories in the specified
    Path.
    There is no specific order of results.
    """

    @overload
    def __init__(self) -> None:
        """Instantiates Object as empty Iterator;"""

    @overload
    def __init__(self, where: OSD_Path, Mask: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Instantiates Object as Iterator.
        Wild-card "*" can be used in Mask the same way it
        is used by unix shell for file names
        """

    @overload
    def __init__(self, theOther: OSD_DirectoryIterator) -> None: ...

    def Destroy(self) -> None: ...

    def Initialize(self, where: OSD_Path, Mask: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Initializes the current File Directory"""

    def More(self) -> bool:
        """
        Returns TRUE if other items are found while
        using the 'Tree' method.
        """

    def Next(self) -> None:
        """
        Sets the iterator to the next item.
        Returns the item value corresponding to the current
        position of the iterator.
        """

    def Values(self) -> OSD_Directory:
        """Returns the next item found ."""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_Disk:
    """Disk management (a set of disk oriented tools)"""

    @overload
    def __init__(self) -> None:
        """
        Creates a disk object.
        This is used only when a class contains a Disk field.
        By default, its name is initialized to current working disk.
        """

    @overload
    def __init__(self, Name: OSD_Path) -> None:
        """
        Initializes the object Disk with the disk name
        associated to the OSD_Path.
        """

    @overload
    def __init__(self, PathName: str) -> None:
        """
        Initializes the object Disk with <PathName>.
        <PathName> specifies any file within the mounted
        file system.
        Example : OSD_Disk myDisk ("/tmp")
        Initializes a disk object with the mounted
        file associated to /tmp.
        """

    @overload
    def __init__(self, theOther: OSD_Disk) -> None: ...

    def Name(self) -> OSD_Path:
        """Returns disk name of <me>."""

    def SetName(self, Name: OSD_Path) -> None:
        """Instantiates <me> with <Name>."""

    def DiskSize(self) -> int:
        """Returns total disk capacity in 512 bytes blocks."""

    def DiskFree(self) -> int:
        """Returns free available 512 bytes blocks on disk."""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_Environment:
    """
    Management of system environment variables
    An environment variable is composed of a variable name
    and its value.

    To be portable among various systems, environment variables
    are local to a process.
    """

    @overload
    def __init__(self) -> None:
        """Creates the object Environment."""

    @overload
    def __init__(self, Name: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Creates an Environment variable initialized with value
        set to an empty AsciiString.
        """

    @overload
    def __init__(self, Name: nanoocp.TCollection.TCollection_AsciiString, Value: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Creates an Environment variable initialized with Value."""

    @overload
    def __init__(self, theOther: OSD_Environment) -> None: ...

    def SetValue(self, Value: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Changes environment variable value.
        Raises ConstructionError either if the string contains
        characters not in range of ' '...'~' or if the string
        contains the character '$' which is forbidden.
        """

    def Value(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Gets the value of an environment variable"""

    def SetName(self, name: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Changes environment variable name.
        Raises ConstructionError either if the string contains
        characters not in range of ' '...'~' or if the string
        contains the character '$' which is forbidden.
        """

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Gets the name of <me>."""

    def Build(self) -> None:
        """
        Sets the value of an environment variable
        into system (physically).
        """

    def Remove(self) -> None:
        """Removes (physically) an environment variable"""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_Exception(nanoocp.Standard.Standard_Failure):
    pass

class OSD_Exception_ACCESS_VIOLATION(OSD_Exception):
    pass

class OSD_Exception_ARRAY_BOUNDS_EXCEEDED(OSD_Exception):
    pass

class OSD_Exception_CTRL_BREAK(OSD_Exception):
    pass

class OSD_Exception_ILLEGAL_INSTRUCTION(OSD_Exception):
    pass

class OSD_Exception_IN_PAGE_ERROR(OSD_Exception):
    pass

class OSD_Exception_INT_OVERFLOW(OSD_Exception):
    pass

class OSD_Exception_INVALID_DISPOSITION(OSD_Exception):
    pass

class OSD_Exception_NONCONTINUABLE_EXCEPTION(OSD_Exception):
    pass

class OSD_Exception_PRIV_INSTRUCTION(OSD_Exception):
    pass

class OSD_Exception_STACK_OVERFLOW(OSD_Exception):
    pass

class OSD_Exception_STATUS_NO_MEMORY(OSD_Exception):
    pass

class OSD_File(OSD_FileNode):
    """
    Basic tools to manage files
    Warning: 'ProgramError' is raised when somebody wants to use the methods
    Read, Write, Seek, Close when File is not open.
    """

    @overload
    def __init__(self) -> None:
        """Creates File object."""

    @overload
    def __init__(self, Name: OSD_Path) -> None:
        """Instantiates the object file, storing its name"""

    @overload
    def __init__(self, theOther: OSD_File) -> None: ...

    def Build(self, Mode: OSD_OpenMode, Protect: OSD_Protection) -> None:
        """
        CREATES a file if it doesn't already exists or empties
        an existing file.
        After 'Build', the file is open.
        If no name was given, ProgramError is raised.
        """

    def Open(self, Mode: OSD_OpenMode, Protect: OSD_Protection) -> None:
        """
        Opens a File with specific attributes
        This works only on already existing file.
        If no name was given, ProgramError is raised.
        """

    def Append(self, Mode: OSD_OpenMode, Protect: OSD_Protection) -> None:
        """
        Appends data to an existing file.
        If file doesn't exist, creates it first.
        After 'Append', the file is open.
        If no name was given, ProgramError is raised.
        """

    def Read(self, Buffer: nanoocp.TCollection.TCollection_AsciiString, Nbyte: int) -> None:
        """
        Attempts to read Nbyte bytes from the file associated with
        the object file.
        Upon successful completion, Read returns the number of
        bytes actually read and placed in the Buffer. This number
        may be less than Nbyte if the number of bytes left in the file
        is less than Nbyte bytes. In this case only number of read
        bytes will be placed in the buffer.
        """

    @overload
    def ReadLine(self, Buffer: nanoocp.TCollection.TCollection_AsciiString, NByte: int) -> int:
        """
        Reads bytes from the data pointed to by the object file
        into the buffer <Buffer>.
        Data is read until <NByte-1> bytes have been read,
        until	a newline character is read and transferred into
        <Buffer>, or until an EOF (End-of-File) condition is
        encountered.
        Upon successful completion, Read returns the number of
        bytes actually read and placed into the Buffer <Buffer>.
        """

    @overload
    def ReadLine(self, Buffer: nanoocp.TCollection.TCollection_AsciiString, NByte: int) -> int:
        """
        Reads bytes from the data pointed to by the object file
        into the buffer <Buffer>.
        Data is read until <NByte-1> bytes have been read,
        until	a newline character is read and transferred into
        <Buffer>, or until an EOF (End-of-File) condition is
        encountered.
        Upon successful completion, Read returns the number of
        bytes actually read into <NByteRead> and placed into the
        Buffer <Buffer>.
        """

    def Write(self, theBuffer: nanoocp.TCollection.TCollection_AsciiString, theNbBytes: int) -> None:
        """Attempts to write theNbBytes bytes from the AsciiString to the file."""

    def Seek(self, Offset: int, Whence: OSD_FromWhere) -> None:
        """Sets the seek pointer associated with the open file"""

    def Close(self) -> None:
        """Closes the file (and deletes a descriptor)"""

    def IsAtEnd(self) -> bool:
        """Returns TRUE if the seek pointer is at end of file."""

    def KindOfFile(self) -> OSD_KindFile:
        """
        Returns the kind of file. A file can be a
        file, a directory or a link.
        """

    def BuildTemporary(self) -> None:
        """
        Makes a temporary File
        This temporary file is already open !
        """

    def SetLock(self, Lock: OSD_LockType) -> None:
        """Locks current file"""

    def UnLock(self) -> None:
        """Unlocks current file"""

    def GetLock(self) -> OSD_LockType:
        """Returns the current lock state"""

    def IsLocked(self) -> bool:
        """Returns TRUE if this file is locked."""

    def Size(self) -> int:
        """Returns actual number of bytes of <me>."""

    def IsOpen(self) -> bool:
        """Returns TRUE if <me> is open."""

    def IsReadable(self) -> bool:
        """
        returns TRUE if the file exists and if the user
        has the authorization to read it.
        """

    def IsWriteable(self) -> bool:
        """returns TRUE if the file can be read and overwritten."""

    def IsExecutable(self) -> bool:
        """returns TRUE if the file can be executed."""

    def ReadLastLine(self, aLine: nanoocp.TCollection.TCollection_AsciiString, aDelay: int, aNbTries: int) -> bool:
        """
        Enables to emulate unix "tail -f" command.
        If a line is available in the file <me> returns it.
        Otherwise attempts to read again aNbTries times in the file
        waiting aDelay seconds between each read.
        If meanwhile the file increases returns the next line, otherwise
        returns FALSE.
        """

    def Edit(self) -> bool:
        """find an editor on the system and edit the given file"""

    def Rewind(self) -> None:
        """Set file pointer position to the beginning of the file"""

class OSD_FileIterator:
    """
    Manages a breadth-only search for files in the specified Path.
    There is no specific order of results.
    """

    @overload
    def __init__(self) -> None:
        """Instantiates Object as empty Iterator;"""

    @overload
    def __init__(self, where: OSD_Path, Mask: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Instantiates Object as Iterator;
        Wild-card "*" can be used in Mask the same way it
        is used by unix shell for file names
        """

    @overload
    def __init__(self, theOther: OSD_FileIterator) -> None: ...

    def Destroy(self) -> None: ...

    def Initialize(self, where: OSD_Path, Mask: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Initializes the current File Iterator"""

    def More(self) -> bool:
        """
        Returns TRUE if there are other items using the 'Tree'
        method.
        """

    def Next(self) -> None:
        """
        Sets the iterator to the next item.
        Returns the item value corresponding to the current
        position of the iterator.
        """

    def Values(self) -> OSD_File:
        """Returns the next file found ."""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_FileSystemSelector(OSD_FileSystem):
    """
    File system implementation which tried to open stream using registered list of file systems.
    """

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: OSD_FileSystemSelector) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def AddProtocol(self, theFileSystem: OSD_FileSystem | None, theIsPreferred: bool = False) -> None:
        """
        Registers file system within this selector.
        @param[in] theFileSystem   file system to register
        @param[in] theIsPreferred  add to the beginning of the list when TRUE, or add to the end
        otherwise
        """

    def RemoveProtocol(self, theFileSystem: OSD_FileSystem | None) -> None:
        """Unregisters file system within this selector."""

    def IsSupportedPath(self, theUrl: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns TRUE if URL defines a supported protocol."""

class OSD_Host:
    """
    Carries information about a Host
    System version ,host name, nodename ...
    """

    @overload
    def __init__(self) -> None:
        """Initializes current host by default."""

    @overload
    def __init__(self, theOther: OSD_Host) -> None: ...

    def SystemVersion(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns system name and version"""

    def SystemId(self) -> OSD_SysType:
        """Returns the system type (UNIX System V, UNIX BSD, MS-DOS...)"""

    def HostName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns host name."""

    def AvailableMemory(self) -> int:
        """Returns available memory in Kilobytes."""

    def InternetAddress(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns Internet address of current host."""

    def MachineType(self) -> OSD_OEMType:
        """Returns type of current machine."""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_LocalFileSystem(OSD_FileSystem):
    """A file system opening local files (or files from mount systems)."""

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: OSD_LocalFileSystem) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def IsSupportedPath(self, theUrl: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Returns TRUE if URL defines a supported protocol."""

class OSD_MemInfo:
    """
    This class provide information about memory utilized by current process.
    This information includes:
    - Private Memory - synthetic value that tries to filter out the memory
    usage only by the process itself (allocated for data
    and stack), excluding dynamic libraries.
    These pages may be in RAM or in SWAP.
    - Virtual Memory - amount of reserved and committed memory in the
    user-mode portion of the virtual address space.
    Notice that this counter includes reserved memory
    (not yet in used) and shared between processes memory (libraries).
    - Working Set    - set of memory pages in the virtual address space of the process
    that are currently resident in physical memory (RAM).
    These pages are available for an application to use
    without triggering a page fault.
    - Pagefile Usage - space allocated for the pagefile, in bytes.
    Those pages may or may not be in memory (RAM)
    thus this counter couldn't be used to estimate
    how many active pages doesn't present in RAM.

    Notice that none of these counters can be used as absolute measure of
    application memory consumption!

    User should analyze all values in specific case to make correct decision
    about memory (over)usage. This is also preferred to use specialized
    tools to detect memory leaks.

    This also means that these values should not be used for intellectual
    memory management by application itself.
    """

    @overload
    def __init__(self, theImmediateUpdate: bool = True) -> None:
        """Create and initialize. By default all countes are active"""

    @overload
    def __init__(self, theOther: OSD_MemInfo) -> None: ...

    class Counter(enum.IntEnum):
        MemPrivate = 0

        MemVirtual = 1

        MemWorkingSet = 2

        MemWorkingSetPeak = 3

        MemSwapUsage = 4

        MemSwapUsagePeak = 5

        MemHeapUsage = 6

        MemCounter_NB = 7

    MemPrivate: OSD_MemInfo.Counter = Counter.MemPrivate

    MemVirtual: OSD_MemInfo.Counter = Counter.MemVirtual

    MemWorkingSet: OSD_MemInfo.Counter = Counter.MemWorkingSet

    MemWorkingSetPeak: OSD_MemInfo.Counter = Counter.MemWorkingSetPeak

    MemSwapUsage: OSD_MemInfo.Counter = Counter.MemSwapUsage

    MemSwapUsagePeak: OSD_MemInfo.Counter = Counter.MemSwapUsagePeak

    MemHeapUsage: OSD_MemInfo.Counter = Counter.MemHeapUsage

    MemCounter_NB: OSD_MemInfo.Counter = Counter.MemCounter_NB

    def IsActive(self, theCounter: OSD_MemInfo.Counter) -> bool:
        """Return true if the counter is active"""

    @overload
    def SetActive(self, theActive: bool) -> None:
        """
        Set all counters active. The information is collected for active counters.
        @param theActive state for counters
        """

    @overload
    def SetActive(self, theCounter: OSD_MemInfo.Counter, theActive: bool) -> None:
        """
        Set the counter active. The information is collected for active counters.
        @param theCounter type of counter
        @param theActive state for the counter
        """

    def Clear(self) -> None:
        """Clear counters"""

    def Update(self) -> None:
        """Update counters"""

    def ToString(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Return the string representation for all available counter."""

    def Value(self, theCounter: OSD_MemInfo.Counter) -> int:
        """
        Return value of specified counter in bytes.
        Notice that NOT all counters are available on various systems.
        size_t(-1) means invalid (unavailable) value.
        """

    def ValueMiB(self, theCounter: OSD_MemInfo.Counter) -> int:
        """
        Return value of specified counter in MiB.
        Notice that NOT all counters are available on various systems.
        size_t(-1) means invalid (unavailable) value.
        """

    def ValuePreciseMiB(self, theCounter: OSD_MemInfo.Counter) -> float:
        """
        Return floating value of specified counter in MiB.
        Notice that NOT all counters are available on various systems.
        double(-1) means invalid (unavailable) value.
        """

    @staticmethod
    def PrintInfo() -> nanoocp.TCollection.TCollection_AsciiString:
        """Return the string representation for all available counter."""

class OSD_OSDError(nanoocp.Standard.Standard_Failure):
    pass

class OSD_Thread:
    """
    A simple platform-intependent interface to execute
    and control threads.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, other: OSD_Thread) -> None:
        """Copy constructor"""

    def Assign(self, other: OSD_Thread) -> None:
        """Copy thread handle from other OSD_Thread object."""

    def SetPriority(self, thePriority: int) -> None: ...

    def Detach(self) -> None:
        """
        Detaches the execution thread from this Thread object,
        so that it cannot be waited.
        Note that mechanics of this operation is different on
        UNIX/Linux (the thread is put to detached state) and Windows
        (the handle is closed).
        However, the purpose is the same: to instruct the system to
        release all thread data upon its completion.
        """

    def Wait(self) -> bool:
        """Waits till the thread finishes execution."""

    def GetId(self) -> int:
        """
        Returns ID of the currently controlled thread ID,
        or 0 if no thread is run
        """

    @staticmethod
    def Current() -> int:
        """Auxiliary: returns ID of the current thread"""

class OSD_ThreadPool(nanoocp.Standard.Standard_Transient):
    """
    Class defining a thread pool for executing algorithms in multi-threaded mode.
    Thread pool allocates requested amount of threads and keep them alive
    (in sleep mode when unused) during thread pool lifetime.
    The same pool can be used by multiple consumers,
    including nested multi-threading algorithms and concurrent threads:
    - Thread pool can be used either by multi-threaded algorithm by creating
    OSD_ThreadPool::Launcher.
    The functor performing a job takes two parameters - Thread Index and Data Index:
    void operator(int theThreadIndex, int theDataIndex){}
    Multi-threaded algorithm may rely on Thread Index for allocating thread-local variables in
    array form, since the Thread Index is guaranteed to be within range OSD_ThreadPool::Lower()
    and OSD_ThreadPool::Upper().
    - Default thread pool (OSD_ThreadPool::DefaultPool()) can be used in general case,
    but application may prefer creating a dedicated pool for better control.
    - Default thread pool allocates the amount of threads considering concurrency
    level of the system (amount of logical processors).
    This can be overridden during OSD_ThreadPool construction or by calling OSD_ThreadPool::Init()
    (the pool should not be used!).
    - OSD_ThreadPool::Launcher reserves specific amount of threads from the pool for executing
    multi-threaded Job.
    Normally, single Launcher instance will occupy all threads available in thread pool,
    so that nested multi-threaded algorithms (within the same thread)
    and concurrent threads trying to use the same thread pool will run sequentially.
    This behavior is affected by OSD_ThreadPool::NbDefaultThreadsToLaunch() parameter
    and Launcher constructor, so that single Launcher instance will occupy not all threads
    in the pool allowing other threads to be used concurrently.
    - OSD_ThreadPool::Launcher locks thread one-by-one from thread pool in a thread-safe way.
    - Each working thread catches exceptions occurred during job execution, and Launcher will
    throw Standard_Failure in a caller thread on completed execution.
    """

    def __init__(self, theNbThreads: int = -1) -> None:
        """
        Main constructor.
        Application may consider specifying more threads than actually
        available (OSD_Parallel::NbLogicalProcessors()) and set up NbDefaultThreadsToLaunch() to a
        smaller value so that concurrent threads will be able using single Thread Pool instance more
        efficiently.
        @param theNbThreads threads number to be created by pool
        (if -1 is specified then OSD_Parallel::NbLogicalProcessors() will be used)
        """

    class Launcher:
        """
        Launcher object locking a subset of threads (or all threads)
        in a thread pool to perform parallel execution of the job.
        """

        def __init__(self, thePool: OSD_ThreadPool, theMaxThreads: int = -1) -> None:
            """
            Lock specified number of threads from the thread pool.
            If thread pool is already locked by another user,
            Launcher will lock as many threads as possible
            (if none will be locked, then single threaded execution will be done).
            @param thePool       thread pool to lock the threads
            @param theMaxThreads number of threads to lock;
            -1 specifies that default number of threads
            to be used OSD_ThreadPool::NbDefaultThreadsToLaunch()
            """

        def HasThreads(self) -> bool:
            """
            Return TRUE if at least 2 threads have been locked for parallel execution (including
            self-thread); otherwise, the functor will be executed within the caller thread.
            """

        def NbThreads(self) -> int:
            """Return amount of locked threads; >= 1."""

        def LowerThreadIndex(self) -> int:
            """Return the lower thread index."""

        def UpperThreadIndex(self) -> int:
            """
            Return the upper thread index (last index is reserved for the self-thread).
            """

        def Release(self) -> None:
            """Release threads before Launcher destruction."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def DefaultPool(theNbThreads: int = -1) -> OSD_ThreadPool:
        """
        Return (or create) a default thread pool.
        Number of threads argument will be considered only when called first time.
        """

    def HasThreads(self) -> bool:
        """
        Return TRUE if at least 2 threads are available (including self-thread).
        """

    def LowerThreadIndex(self) -> int:
        """Return the lower thread index."""

    def UpperThreadIndex(self) -> int:
        """
        Return the upper thread index (last index is reserved for self-thread).
        """

    def NbThreads(self) -> int:
        """Return the number of threads; >= 1."""

    def NbDefaultThreadsToLaunch(self) -> int:
        """
        Return maximum number of threads to be locked by a single Launcher object by default;
        the entire thread pool size is returned by default.
        """

    def SetNbDefaultThreadsToLaunch(self, theNbThreads: int) -> None:
        """
        Set maximum number of threads to be locked by a single Launcher object by default.
        Should be set BEFORE first usage.
        """

    def IsInUse(self) -> bool:
        """Checks if thread pools has active consumers."""

    def Init(self, theNbThreads: int) -> None:
        """
        Reinitialize the thread pool with a different number of threads.
        Should be called only with no active jobs, or exception Standard_ProgramError will be thrown!
        """

class OSD_Parallel:
    """
    @brief Simple tool for code parallelization.

    OSD_Parallel class provides simple interface for parallel processing of
    tasks that can be formulated in terms of "for" or "foreach" loops.

    To use this tool it is necessary to:
    - organize the data to be processed in a collection accessible by
    iteration (usually array or vector);
    - implement a functor class providing operator () accepting iterator
    (or index in array) that does the job;
    - call either For() or ForEach() providing begin and end iterators and
    a functor object.

    Iterators should satisfy requirements of STL forward iterator.
    Functor

    @code
    class Functor
    {
    public:
    void operator() ([processing instance]) const
    {
    //...
    }
    };
    @endcode

    The operator () should be implemented in a thread-safe way so that
    the same functor object can process different data items in parallel threads.

    Iteration by index (For) is expected to be more efficient than using iterators
    (ForEach).

    Implementation uses TBB if OCCT is built with support of TBB; otherwise it
    uses ad-hoc parallelization tool. In general, if TBB is available, it is
    more efficient to use it directly instead of using OSD_Parallel.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: OSD_Parallel) -> None: ...

    @staticmethod
    def ToUseOcctThreads() -> bool:
        """
        @name public methods
        Returns TRUE if OCCT threads should be used instead of auxiliary threads library;
        default value is FALSE if alternative library has been enabled while OCCT building and TRUE
        otherwise.
        """

    @staticmethod
    def SetUseOcctThreads(theToUseOcct: bool) -> None:
        """
        Sets if OCCT threads should be used instead of auxiliary threads library.
        Has no effect if OCCT has been built with no auxiliary threads library.
        """

    @staticmethod
    def NbLogicalProcessors() -> int:
        """Returns number of logical processors."""

class OSD_PerfMeter:
    """
    This class enables measuring the CPU time between two points of code execution, regardless of
    the scope of these points of code. A meter is identified by its name (string). So multiple
    objects in various places of user code may point to the same meter. The results will be printed
    on stdout upon finish of the program. For details see OSD_PerfMeter.h
    """

    @overload
    def __init__(self) -> None:
        """Constructs a void meter (to further call Init and Start)."""

    @overload
    def __init__(self, theMeterName: nanoocp.TCollection.TCollection_AsciiString, theToAutoStart: bool = True) -> None:
        """
        Constructs and starts (if autoStart is true) the named meter.
        @param theMeterName Name of the meter. If the meter with such name was already created,
        and hasn't been killed, it will be used.
        @param theToAutoStart If true, the meter will be started immediately after creation.
        Otherwise, the user should call Start() method to start the meter.
        Note that if meter already exists, theToAutoStart == true will reset it.
        """

    @overload
    def __init__(self, theOther: OSD_PerfMeter) -> None: ...

    def Init(self, theMeterName: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """
        Prepares the named meter. If the meter with such name was already created,
        it will be used. Otherwise, a new meter will be created.
        """

    def Start(self) -> None:
        """
        Starts the meter. If the meter was already started, it will be reset.
        Note that the meter with the name specified in the constructor can still be used
        in other places of the code.
        """

    def Stop(self) -> None:
        """Stops the meter."""

    def Elapsed(self) -> float:
        """Returns the elapsed time in seconds since the meter was started."""

    def Kill(self) -> None:
        """Outputs the meter data and resets it to initial state."""

    def Print(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Prints the data of this meter."""

    @staticmethod
    def PrintALL() -> nanoocp.TCollection.TCollection_AsciiString:
        """Prints the data of all meters with non-zero elapsed time."""

    @staticmethod
    def ResetALL() -> None:
        """Resets all meters."""

class OSD_Process:
    """A set of system process tools"""

    @overload
    def __init__(self) -> None:
        """Initializes the object and prepare for a possible dump"""

    @overload
    def __init__(self, theOther: OSD_Process) -> None: ...

    @staticmethod
    def ExecutablePath() -> nanoocp.TCollection.TCollection_AsciiString:
        """Return full path to the current process executable."""

    @staticmethod
    def ExecutableFolder() -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Return full path to the folder containing current process executable with trailing separator.
        """

    def TerminalType(self, Name: nanoocp.TCollection.TCollection_AsciiString) -> None:
        """Returns the terminal used (vt100, vt200 ,sun-cmd ...)"""

    def SystemDate(self) -> nanoocp.Quantity.Quantity_Date:
        """Gets system date."""

    def UserName(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the user name."""

    def IsSuperUser(self) -> bool:
        """Returns True if the process user is the super-user."""

    def ProcessId(self) -> int:
        """Returns the 'Process Id'"""

    def CurrentDirectory(self) -> OSD_Path:
        """Returns the current path where the process is."""

    def SetCurrentDirectory(self, where: OSD_Path) -> None:
        """Changes the current process directory."""

    def Failed(self) -> bool:
        """Returns TRUE if an error occurs"""

    def Reset(self) -> None:
        """Resets error counter to zero"""

    def Perror(self) -> None:
        """Raises OSD_Error"""

    def Error(self) -> int:
        """Returns error number if 'Failed' is TRUE."""

class OSD_Protection:
    """
    This class provides data to manage file protection
    Example:These rights are treated in a system dependent manner:
    On UNIX you have User,Group and Other rights
    On VMS you have Owner,Group,World and System rights
    An automatic conversion is done between OSD and UNIX/VMS.

    OSD	VMS	UNIX
    User     Owner   User
    Group    Group   Group
    World    World   Other
    System   System  (combined with Other)

    When you use System protection on UNIX you must know that
    Other rights and System rights are inclusively "ORed".
    So Other with only READ access and System with WRITE access
    will produce on UNIX Other with READ and WRITE access.

    This choice comes from the fact that ROOT can't be considered
    as member of the group nor as user. So it is considered as Other.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes global access rights as follows

        User   : Read Write
        System : Read Write
        Group  : Read
        World  : Read
        """

    @overload
    def __init__(self, System: OSD_SingleProtection, User: OSD_SingleProtection, Group: OSD_SingleProtection, World: OSD_SingleProtection) -> None:
        """Sets values of fields"""

    @overload
    def __init__(self, theOther: OSD_Protection) -> None: ...

    def Values(self) -> tuple[OSD_SingleProtection, OSD_SingleProtection, OSD_SingleProtection, OSD_SingleProtection]:
        """Retrieves values of fields"""

    def SetValues(self, System: OSD_SingleProtection, User: OSD_SingleProtection, Group: OSD_SingleProtection, World: OSD_SingleProtection) -> None:
        """Sets values of fields"""

    def SetSystem(self, priv: OSD_SingleProtection) -> None:
        """Sets protection of 'System'"""

    def SetUser(self, priv: OSD_SingleProtection) -> None:
        """Sets protection of 'User'"""

    def SetGroup(self, priv: OSD_SingleProtection) -> None:
        """Sets protection of 'Group'"""

    def SetWorld(self, priv: OSD_SingleProtection) -> None:
        """Sets protection of 'World'"""

    def System(self) -> OSD_SingleProtection:
        """Gets protection of 'System'"""

    def User(self) -> OSD_SingleProtection:
        """Gets protection of 'User'"""

    def Group(self) -> OSD_SingleProtection:
        """Gets protection of 'Group'"""

    def World(self) -> OSD_SingleProtection:
        """Gets protection of 'World'"""

    def Add(self, aRight: OSD_SingleProtection) -> OSD_SingleProtection:
        """
        Add a right to a single protection.
        ex: aProt = RWD
        me.Add(aProt,X)  -> aProt = RWXD
        """

    def Sub(self, aRight: OSD_SingleProtection) -> OSD_SingleProtection:
        """
        Subtract a right to a single protection.
        ex: aProt = RWD
        me.Sub(aProt,RW) -> aProt = D
        But me.Sub(aProt,RWX) is also valid and gives same result.
        """

class OSD_SharedLibrary:
    """
    Interface to dynamic library loader.
    Provides tools to load a shared library
    and retrieve the address of an entry point.
    """

    @overload
    def __init__(self) -> None:
        """Creates a SharedLibrary object with name NULL."""

    @overload
    def __init__(self, aFilename: str) -> None:
        """Creates a SharedLibrary object with name aFilename."""

    @overload
    def __init__(self, theOther: OSD_SharedLibrary) -> None: ...

    def SetName(self, aName: str) -> None:
        """Sets a name associated to the shared object."""

    def Name(self) -> str:
        """Returns the name associated to the shared object."""

    def DlOpen(self, Mode: OSD_LoadMode) -> bool:
        """
        The DlOpen method provides an interface to the
        dynamic library loader to allow shared libraries
        to be loaded and called at runtime. The DlOpen
        function attempts to load Filename, in the address
        space of the process, resolving symbols as appropriate.
        Any libraries that Filename depends upon are also loaded.
        If MODE is RTLD_LAZY, then the runtime loader
        does symbol resolution only as needed.
        Typically, this means that the first call to a function
        in the newly	loaded library will cause the resolution of
        the	address	of that	function to occur.
        If Mode is RTLD_NOW, then the runtime loader must do all
        symbol binding during the DlOpen call.
        The DlOpen method returns a	handle that is used by DlSym
        or DlClose.
        If there is an error, false is returned,
        true otherwise.
        If a NULL Filename is specified, DlOpen returns a handle
        for the main	executable, which allows access to dynamic
        symbols in the running program.
        """

    def DlClose(self) -> None:
        """
        Deallocates the address space for the library
        corresponding to the shared object.
        If any user function continues to call a symbol
        resolved in the address space of a library
        that has been since been deallocated by DlClose,
        the results are undefined.
        """

    def DlError(self) -> str:
        """
        The dlerror function returns a string describing
        the last error that occurred from
        a call to DlOpen, DlClose or DlSym.
        """

    def Destroy(self) -> None:
        """Frees memory allocated."""

class OSD_Signal(nanoocp.Standard.Standard_Failure):
    pass

class OSD_SIGBUS(OSD_Signal):
    pass

class OSD_SIGHUP(OSD_Signal):
    pass

class OSD_SIGILL(OSD_Signal):
    pass

class OSD_SIGINT(OSD_Signal):
    pass

class OSD_SIGKILL(OSD_Signal):
    pass

class OSD_SIGQUIT(OSD_Signal):
    pass

class OSD_SIGSEGV(OSD_Signal):
    pass

class OSD_SIGSYS(OSD_Signal):
    pass

class OSD_Timer(OSD_Chronometer):
    """
    Working on heterogeneous platforms
    we need to use the system call gettimeofday.
    This function is portable and it measures ELAPSED
    time and CPU time in seconds and microseconds.
    Example: OSD_Timer aTimer;
    aTimer.Start();   // Start the timers (t1).
    .....             // Do something.
    aTimer.Stop();    // Stop the timers (t2).
    aTimer.Show();    // Give the elapsed time between t1 and t2.
    // Give also the process CPU time between
    // t1 and t2.
    """

    @overload
    def __init__(self, theThisThreadOnly: bool = False) -> None:
        """
        Builds a Chronometer initialized and stopped.
        @param theThisThreadOnly when TRUE, measured CPU time will account time of the current thread
        only;
        otherwise CPU of the process (all threads, and completed children) is
        measured; this flag does NOT affect ElapsedTime() value, only values
        returned by OSD_Chronometer
        """

    @overload
    def __init__(self, theOther: OSD_Timer) -> None: ...

    @staticmethod
    def GetWallClockTime() -> float:
        """
        Returns current time in seconds with system-defined precision.
        The could be a system uptime or a time from some date.
        Returned value is intended for precise elapsed time measurements as a delta between
        timestamps. On Windows implemented via QueryPerformanceCounter(), on other systems via
        gettimeofday().
        """

    @overload
    def Reset(self, theTimeElapsedSec: float) -> None:
        """Stops and reinitializes the timer with specified elapsed time."""

    @overload
    def Reset(self) -> None:
        """Stops and reinitializes the timer with zero elapsed time."""

    def Restart(self) -> None:
        """Restarts the Timer."""

    @overload
    def Show(self) -> tuple[float, int, int, float]:
        """
        returns both the elapsed time(seconds,minutes,hours)
        and CPU time.
        """

    @overload
    def Show(self) -> None:
        """
        Shows both the elapsed time and CPU time on the standard output
        stream <cout>.The chronometer can be running (Lap Time) or
        stopped.
        """

    @overload
    def Show(self) -> object:
        """
        Shows both the elapsed time and CPU time on the
        output stream <OS>.
        """

    def Stop(self) -> None:
        """Stops the Timer."""

    def Start(self) -> None:
        """
        Starts (after Create or Reset) or restarts (after Stop)
        the Timer.
        """

    def ElapsedTime(self) -> float:
        """Returns elapsed time in seconds."""

def OSD_OpenFile(theName: nanoocp.TCollection.TCollection_ExtendedString, theMode: str) -> "__sFILE":
    """
    Function opens the file.
    @param theName name of file encoded in UTF-16
    @param theMode opening mode
    @return file handle of opened file
    """

def OSD_FileStatCTime(theName: str) -> int:
    """
    Function retrieves file timestamp.
    @param theName name of file encoded in UTF-8
    @return stat.st_ctime value
    """

def OSD_OpenFileDescriptor(theName: nanoocp.TCollection.TCollection_ExtendedString, theMode: int) -> int:
    """
    Open file descriptor for specified UTF-16 file path.
    @param theName name of file encoded in UTF-16
    @param theMode opening mode
    @return file descriptor on success or -1 on error
    """
