"""OCCT package Media (toolkit TKService)"""

from typing import overload

import nanoocp.BVH
import nanoocp.Image
import nanoocp.Standard
import nanoocp.TCollection


class Media_BufferPool(nanoocp.Standard.Standard_Transient):
    """AVBufferPool wrapper."""

    def __init__(self) -> None:
        """Empty constructor"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self) -> None:
        """
        Release the pool (reference-counted buffer will be released when needed).
        """

    def Init(self, theBufferSize: int) -> bool:
        """(Re-)initialize the pool."""

    def BufferSize(self) -> int:
        """Return buffer size within the pool."""

class Media_Packet(nanoocp.Standard.Standard_Transient):
    """
    AVPacket wrapper - the packet (data chunk for decoding/encoding) holder.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Media_Packet) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Unref(self) -> None:
        """av_packet_unref() wrapper."""

    def Size(self) -> int:
        """Return data size."""

    def Pts(self) -> int:
        """Return presentation timestamp (PTS)."""

    def Dts(self) -> int:
        """Return decoding timestamp (DTS)."""

    def Duration(self) -> int:
        """Return Duration."""

    def DurationSeconds(self) -> float:
        """Return Duration in seconds."""

    def SetDurationSeconds(self, theDurationSec: float) -> None:
        """Set Duration in seconds."""

    def StreamIndex(self) -> int:
        """Return stream index."""

    def IsKeyFrame(self) -> bool:
        """Return TRUE for a key frame."""

    def SetKeyFrame(self) -> None:
        """Mark as key frame."""

class Media_CodecContext(nanoocp.Standard.Standard_Transient):
    """AVCodecContext wrapper - the coder/decoder holder."""

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Media_CodecContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Close(self) -> None:
        """Close input."""

    def SizeX(self) -> int:
        """@return source frame width"""

    def SizeY(self) -> int:
        """@return source frame height"""

    def StreamIndex(self) -> int:
        """Return stream index."""

    def Flush(self) -> None:
        """avcodec_flush_buffers() wrapper."""

    def CanProcessPacket(self, thePacket: Media_Packet | None) -> bool:
        """Return true if packet belongs to this stream."""

    def SendPacket(self, thePacket: Media_Packet | None) -> bool:
        """avcodec_send_packet() wrapper."""

    def ReceiveFrame(self, theFrame: Media_Frame | None) -> bool:
        """avcodec_receive_frame() wrapper."""

class Media_FormatContext(nanoocp.Standard.Standard_Transient):
    """AVFormatContext wrapper - the media input/output stream holder."""

    @overload
    def __init__(self) -> None:
        """Constructor."""

    @overload
    def __init__(self, theOther: Media_FormatContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def FormatAVErrorDescription(theErrCodeAV: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns string description for AVError code."""

    @staticmethod
    def FormatUnitsToSeconds(theTimeUnits: int) -> float:
        """
        Convert time units into seconds for context.
        @param theTimeUnits value to convert
        @return converted time units in seconds
        """

    @staticmethod
    def SecondsToUnits(theTimeSeconds: float) -> int:
        """
        Convert seconds into time units for context.
        @param theTimeSeconds value to convert
        @return time units
        """

    @staticmethod
    def FormatTime(theSeconds: float) -> nanoocp.TCollection.TCollection_AsciiString:
        """Time formatter."""

    @staticmethod
    def FormatTimeProgress(theProgress: float, theDuration: float) -> nanoocp.TCollection.TCollection_AsciiString:
        """Time progress / duration formatter."""

    def OpenInput(self, theInput: nanoocp.TCollection.TCollection_AsciiString) -> bool:
        """Open input."""

    def Close(self) -> None:
        """Close input."""

    def NbSteams(self) -> int:
        """Return amount of streams."""

    def StreamInfo(self, theIndex: int) -> nanoocp.TCollection.TCollection_AsciiString:
        """Format stream info."""

    def PtsStartBase(self) -> float:
        """Return PTS start base in seconds."""

    def Duration(self) -> float:
        """Return duration in seconds."""

    def ReadPacket(self, thePacket: Media_Packet | None) -> bool:
        """av_read_frame() wrapper."""

    def SeekStream(self, theStreamId: int, theSeekPts: float, toSeekBack: bool) -> bool:
        """Seek stream to specified position."""

    def Seek(self, theSeekPts: float, toSeekBack: bool) -> bool:
        """Seek context to specified position."""

class Media_Frame(nanoocp.Standard.Standard_Transient):
    """AVFrame wrapper - the frame (decoded image/audio sample data) holder."""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: Media_Frame) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @staticmethod
    def FormatFFmpeg2Occt(theFormat: int) -> nanoocp.Image.Image_Format:
        """Convert pixel format from FFmpeg (AVPixelFormat) to OCCT."""

    @staticmethod
    def FormatOcct2FFmpeg(theFormat: nanoocp.Image.Image_Format) -> int:
        """
        Convert pixel format from OCCT to FFmpeg (AVPixelFormat).
        Returns -1 (AV_PIX_FMT_NONE) if undefined.
        """

    @staticmethod
    def Swap(theFrame1: Media_Frame | None, theFrame2: Media_Frame | None) -> None:
        """Swap AVFrame* within two frames."""

    def IsEmpty(self) -> bool:
        """Return true if frame does not contain any data."""

    def Unref(self) -> None:
        """av_frame_unref() wrapper."""

    def Size(self) -> nanoocp.BVH.BVH_Vec2i:
        """Return image dimensions."""

    def SizeX(self) -> int:
        """Return image width."""

    def SizeY(self) -> int:
        """Return image height."""

    def Format(self) -> int:
        """Return pixel format (AVPixelFormat)."""

    def IsFullRangeYUV(self) -> bool:
        """Return TRUE if YUV range is full."""

    def LineSize(self, thePlaneId: int) -> int:
        """@return linesize in bytes for specified data plane"""

    def BestEffortTimestamp(self) -> int:
        """
        @return frame timestamp estimated using various heuristics, in stream time base
        """

    def Pts(self) -> float:
        """Return presentation timestamp (PTS)."""

    def SetPts(self, thePts: float) -> None:
        """Set presentation timestamp (PTS)."""

    def PixelAspectRatio(self) -> float:
        """Return PAR."""

    def SetPixelAspectRatio(self, theRatio: float) -> None:
        """Set PAR."""

    def IsLocked(self) -> bool:
        """Return locked state."""

    def SetLocked(self, theToLock: bool) -> None:
        """Lock/free frame for edition."""

    def InitWrapper(self, thePixMap: nanoocp.Image.Image_PixMap | None) -> bool:
        """Wrap allocated image pixmap."""

class Media_IFrameQueue:
    """Interface defining frame queuing."""

    def LockFrame(self) -> Media_Frame:
        """
        Lock the frame, e.g. take ownership on a single (not currently displayed) frame from the queue
        to perform decoding into.
        """

    def ReleaseFrame(self, theFrame: Media_Frame | None) -> None:
        """
        Release previously locked frame, e.g. it can be displayed on the screen.
        """

class Media_Timer(nanoocp.Standard.Standard_Transient):
    """Auxiliary class defining the animation timer."""

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Media_Timer) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def ElapsedTime(self) -> float:
        """Return elapsed time in seconds."""

    def PlaybackSpeed(self) -> float:
        """Return playback speed coefficient (1.0 means normal speed)."""

    def SetPlaybackSpeed(self, theSpeed: float) -> None:
        """Setup playback speed coefficient."""

    def IsStarted(self) -> bool:
        """Return true if timer has been started."""

    def Start(self) -> None:
        """Start the timer."""

    def Pause(self) -> None:
        """Pause the timer."""

    def Stop(self) -> None:
        """Stop the timer."""

    def Seek(self, theTime: float) -> None:
        """Seek the timer to specified position."""

class Media_PlayerContext(nanoocp.Standard.Standard_Transient):
    """Player context."""

    def __init__(self, theFrameQueue: Media_IFrameQueue) -> None:
        """
        Main constructor.
        Note that Frame Queue is stored as pointer,
        and it is expected that this context is stored as a class field of Frame Queue.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    @overload
    @staticmethod
    def DumpFirstFrame(theSrcVideo: nanoocp.TCollection.TCollection_AsciiString, theMediaInfo: nanoocp.TCollection.TCollection_AsciiString) -> Media_Frame:
        """
        Dump first video frame.
        @param[in] theSrcVideo  path to the video
        @param[out] theMediaInfo  video description
        """

    @overload
    @staticmethod
    def DumpFirstFrame(theSrcVideo: nanoocp.TCollection.TCollection_AsciiString, theOutImage: nanoocp.TCollection.TCollection_AsciiString, theMediaInfo: nanoocp.TCollection.TCollection_AsciiString, theMaxSize: int = 0) -> bool:
        """
        Dump first video frame.
        @param[in] theSrcVideo  path to the video
        @param[in] theOutImage  path to make a screenshot
        @param[out] theMediaInfo  video description
        @param[in] theMaxSize  when positive - downscales image to specified size
        """

    def SetInput(self, theInputPath: nanoocp.TCollection.TCollection_AsciiString, theToWait: bool) -> None:
        """Set new input for playback."""

    def PlaybackState(self) -> tuple[bool, float, float]:
        """Return playback state."""

    def PlayPause(self) -> tuple[bool, float, float]:
        """Pause/Pause playback depending on the current state."""

    def Seek(self, thePosSec: float) -> None:
        """Seek to specified position."""

    def Pause(self) -> None:
        """Pause playback."""

    def Resume(self) -> None:
        """Resume playback."""

    def ToForceRgb(self) -> bool:
        """
        Return TRUE if queue requires RGB pixel format or can handle also YUV pixel format; TRUE by
        default.
        """

    def SetForceRgb(self, theToForce: bool) -> None:
        """
        Set if queue requires RGB pixel format or can handle also YUV pixel format.
        """

class Media_Scaler(nanoocp.Standard.Standard_Transient):
    """
    SwsContext wrapper - tool performing image scaling and pixel format conversion.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor."""

    @overload
    def __init__(self, theOther: Media_Scaler) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Release(self) -> None:
        """sws_freeContext() wrapper."""

    def Init(self, theSrcDims: nanoocp.BVH.BVH_Vec2i, theSrcFormat: int, theResDims: nanoocp.BVH.BVH_Vec2i, theResFormat: int) -> bool:
        """
        sws_getContext() wrapper - creates conversion context.
        @param theSrcDims   dimensions of input frame
        @param theSrcFormat pixel format (AVPixelFormat) of input frame
        @param theResDims   dimensions of destination frame
        @param theResFormat pixel format (AVPixelFormat) of destination frame
        """

    def Convert(self, theSrc: Media_Frame | None, theRes: Media_Frame | None) -> bool:
        """Convert one frame to another."""

    def IsValid(self) -> bool:
        """Return TRUE if context was initialized."""
