"""OCCT package WNT (toolkit TKService)"""

import enum

import nanoocp.BVH
import nanoocp.Standard


class WNT_OrientationType(enum.IntEnum):
    """Portrait/landscape orientation."""

    WNT_OT_PORTRAIT = 0

    WNT_OT_LANDSCAPE = 1

WNT_OT_PORTRAIT: WNT_OrientationType = WNT_OrientationType.WNT_OT_PORTRAIT

WNT_OT_LANDSCAPE: WNT_OrientationType = WNT_OrientationType.WNT_OT_LANDSCAPE

class WNT_ClassDefinitionError(nanoocp.Standard.Standard_ConstructionError):
    pass

class WNT_HIDSpaceMouse:
    """
    Wrapper over Space Mouse data chunk within WM_INPUT event (known also as Raw Input in WinAPI).
    This class predefines specific list of supported devices, which does not depend on 3rdparty
    library provided by mouse vendor. Supported input chunks:
    - Rotation (3 directions);
    - Translation (3 directions);
    - Pressed buttons.

    To use the class, register Raw Input device:
    @code
    occ::handle<WNT_Window> theWindow;
    RAWINPUTDEVICE aRawInDevList[1];
    RAWINPUTDEVICE& aRawSpace = aRawInDevList[0];
    aRawSpace.usUsagePage = HID_USAGE_PAGE_GENERIC;
    aRawSpace.usUsage     = HID_USAGE_GENERIC_MULTI_AXIS_CONTROLLER;
    aRawSpace.dwFlags     = 0; // RIDEV_DEVNOTIFY
    aRawSpace.hwndTarget  = (HWND )theWindow->NativeHandle();
    if (!::RegisterRawInputDevices (aRawInDevList, 1, sizeof(aRawInDevList[0]))) { Error; }
    @endcode

    Then handle WM_INPUT events within window message loop.
    @code
    AIS_ViewController theViewCtrl;
    case WM_INPUT:
    {
    UINT aSize = 0;
    ::GetRawInputData ((HRAWINPUT )theLParam, RID_INPUT, NULL, &aSize, sizeof(RAWINPUTHEADER));
    NCollection_LocalArray<BYTE> aRawData (aSize); // receive Raw Input for any device and
    process known devices if (aSize == 0 || ::GetRawInputData ((HRAWINPUT )theLParam, RID_INPUT,
    aRawData, &aSize, sizeof(RAWINPUTHEADER)) != aSize)
    {
    break;
    }
    const RAWINPUT* aRawInput = (RAWINPUT* )(BYTE* )aRawData;
    if (aRawInput->header.dwType != RIM_TYPEHID)
    {
    break;
    }

    RID_DEVICE_INFO aDevInfo; aDevInfo.cbSize = sizeof(RID_DEVICE_INFO);
    UINT aDevInfoSize = sizeof(RID_DEVICE_INFO);
    if (::GetRawInputDeviceInfoW (aRawInput->header.hDevice, RIDI_DEVICEINFO, &aDevInfo,
    &aDevInfoSize) != sizeof(RID_DEVICE_INFO)
    || (aDevInfo.hid.dwVendorId != WNT_HIDSpaceMouse::VENDOR_ID_LOGITECH
    && aDevInfo.hid.dwVendorId != WNT_HIDSpaceMouse::VENDOR_ID_3DCONNEXION))
    {
    break;
    }

    Aspect_VKeySet& aKeys = theViewCtrl.ChangeKeys();
    const double aTimeStamp = theViewCtrl.EventTime();
    WNT_HIDSpaceMouse aSpaceData (aDevInfo.hid.dwProductId, aRawInput->data.hid.bRawData,
    aRawInput->data.hid.dwSizeHid); if (aSpaceData.IsTranslation())
    {
    // process translation input
    bool isIdle = true, isQuadric = true;
    const NCollection_Vec3<double> aTrans = aSpaceData.Translation (isIdle, isQuadric);
    aKeys.KeyFromAxis (Aspect_VKey_NavSlideLeft, Aspect_VKey_NavSlideRight, aTimeStamp,
    aTrans.x()); aKeys.KeyFromAxis (Aspect_VKey_NavForward,   Aspect_VKey_NavBackward,
    aTimeStamp, aTrans.y()); aKeys.KeyFromAxis (Aspect_VKey_NavSlideUp,
    Aspect_VKey_NavSlideDown,  aTimeStamp, aTrans.z());
    }
    if (aSpaceData.IsRotation()) {} // process rotation input
    if (aSpaceData.IsKeyState()) {} // process keys input
    break;
    }
    @endcode
    """

    def __init__(self, theOther: WNT_HIDSpaceMouse) -> None: ...

    VENDOR_ID_LOGITECH: int = 1133

    VENDOR_ID_3DCONNEXION: int = 9583

    @staticmethod
    def IsKnownProduct(theProductId: int) -> bool:
        """Return if product id is known by this class."""

    def RawValueRange(self) -> int:
        """Return the raw value range."""

    def SetRawValueRange(self, theRange: int) -> None:
        """Set the raw value range."""

    def IsTranslation(self) -> bool:
        """Return TRUE if data chunk defines new translation values."""

    def Translation(self, theIsQuadric: bool) -> tuple[nanoocp.BVH.BVH_Vec3d, bool]:
        """
        Return new translation values.
        @param[out] theIsIdle  flag indicating idle state (no translation)
        @param[in] theIsQuadric  flag to apply non-linear scale factor
        @return vector of 3 elements defining translation values within [-1..1] range, 0 meaning idle,
        .x defining left/right slide, .y defining forward/backward and .z defining up/down
        slide.
        """

    def IsRotation(self) -> bool:
        """Return TRUE if data chunk defines new rotation values."""

    def Rotation(self, theIsQuadric: bool) -> tuple[nanoocp.BVH.BVH_Vec3d, bool]:
        """
        Return new rotation values.
        @param[out] theIsIdle  flag indicating idle state (no rotation)
        @param[in] theIsQuadric  flag to apply non-linear scale factor
        @return vector of 3 elements defining rotation values within [-1..1] range, 0 meaning idle,
        .x defining tilt, .y defining roll and .z defining spin.
        """

    def IsKeyState(self) -> bool:
        """Return TRUE for key state data chunk."""

    def KeyState(self) -> int:
        """Return new keystate."""

    def HidToSpaceKey(self, theKeyBit: int) -> int:
        """Convert key state bit into virtual key."""
