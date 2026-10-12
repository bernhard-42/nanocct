"""Fail when a macOS x86_64 binary's compact unwind info cannot unwind a function with a stack probe.

A function without a frame pointer and a frame of more than 4 KB gets the frameless encoding
UNWIND_X86_64_MODE_STACK_IND in `__unwind_info`: the unwinder reads the frame size as the 32-bit immediate at a byte
offset into the function's prologue, `sub rsp, imm32` for a plain frame, `mov eax, imm32` before the
`call ___chkstk_darwin` probe of a large one. Apple's clang writes the offset of the `sub rsp` immediate for the probe
form too, one or two bytes past the real immediate; the unwinder then reads four unrelated bytes as the frame size, so a
C++ exception that unwinds through such a function crashes the process (reported: SIGBUS inside _Unwind_RaiseException
for an OCCT exception from a failing fillet, ChFi3d_FilBuilder::PerformTwoCorner). OCCT built with
-fomit-frame-pointer (BUILD_OPT_PROFILE=Production) has hundreds of them, which is why deps/build-occt-macos.sh builds
x86_64 without it; this check keeps it that way. STACK_IND is an x86_64 encoding: images of other architectures are
skipped.

Reads the Mach-O files only, executes nothing. Usage: python tools/check_compact_unwind.py <wheel | dylib | so>...
Exit code 1 when any STACK_IND entry's offset does not point at one of the two immediates.
"""
from __future__ import annotations

import struct
import sys
import zipfile
from collections.abc import Iterator
from pathlib import Path

MH_MAGIC_64 = 0xFEEDFACF
FAT_MAGIC = 0xCAFEBABE                    # big-endian on disk
CPU_TYPE_X86_64 = 0x01000007
LC_SEGMENT_64 = 0x19
MODE_MASK = 0x0F000000
MODE_STACK_IND = 0x03000000
SUB_RSP_IMM32 = b"\x48\x81\xec"           # sub rsp, imm32: the immediate follows these three bytes
MOV_EAX_IMM32 = b"\xb8"                   # mov eax, imm32: the size handed to ___chkstk_darwin ...
CALL_REL32 = b"\xe8"                      # ... by the call right after the immediate


def _slices(data: bytes) -> Iterator[bytes]:
    """The 64-bit Mach-O images in a file: itself, or each slice of a universal binary."""
    if struct.unpack_from("<I", data, 0)[0] == MH_MAGIC_64:
        yield data
    elif struct.unpack_from(">I", data, 0)[0] == FAT_MAGIC:
        for i in range(struct.unpack_from(">I", data, 4)[0]):
            offset, size = struct.unpack_from(">II", data, 8 + 20 * i + 8)
            if struct.unpack_from("<I", data, offset)[0] == MH_MAGIC_64:
                yield data[offset:offset + size]


def _layout(image: bytes) -> tuple[dict[str, tuple[int, int]], dict[str, tuple[int, int, int]]]:
    """Segments (name -> vmaddr, fileoff) and sections (name -> addr, size, fileoff) of a 64-bit image."""
    segments: dict[str, tuple[int, int]] = {}
    sections: dict[str, tuple[int, int, int]] = {}
    ncmds = struct.unpack_from("<I", image, 16)[0]
    offset = 32
    for _ in range(ncmds):
        cmd, size = struct.unpack_from("<II", image, offset)
        if cmd == LC_SEGMENT_64:
            name = image[offset + 8:offset + 24].rstrip(b"\0").decode()
            vmaddr, _vmsize, fileoff = struct.unpack_from("<QQQ", image, offset + 24)
            segments[name] = (vmaddr, fileoff)
            nsects = struct.unpack_from("<I", image, offset + 64)[0]
            for i in range(nsects):
                base = offset + 72 + 80 * i
                sect = image[base:base + 16].rstrip(b"\0").decode()
                addr, sect_size, sect_off = struct.unpack_from("<QQI", image, base + 32)
                sections[sect] = (addr, sect_size, sect_off)
        offset += size
    return segments, sections


def _entries(info: bytes) -> Iterator[tuple[int, int]]:
    """(function offset from the image base, encoding) for every function in an `__unwind_info` section."""
    _version, common_at, common_count, _pers_at, _pers_count, index_at, index_count = struct.unpack_from("<7I", info, 0)
    common = struct.unpack_from(f"<{common_count}I", info, common_at)
    for i in range(index_count - 1):                       # the last index entry is a sentinel
        first, page, _lsda = struct.unpack_from("<III", info, index_at + 12 * i)
        if page == 0:
            continue
        kind = struct.unpack_from("<I", info, page)[0]
        if kind == 2:                                      # regular page: (function offset, encoding) pairs
            _, entries_at, count = struct.unpack_from("<IHH", info, page)
            for j in range(count):
                yield struct.unpack_from("<II", info, page + entries_at + 8 * j)
        elif kind == 3:                                    # compressed page: 24-bit offset delta, 8-bit encoding index
            _, entries_at, count, encodings_at, encodings_count = struct.unpack_from("<IHHHH", info, page)
            local = struct.unpack_from(f"<{encodings_count}I", info, page + encodings_at)
            for j in range(count):
                word = struct.unpack_from("<I", info, page + entries_at + 4 * j)[0]
                k = word >> 24
                yield first + (word & 0xFFFFFF), common[k] if k < common_count else local[k - common_count]


def wrong_entries(image: bytes) -> tuple[int, int]:
    """(STACK_IND entries, those whose offset points at neither immediate) of one x86_64 image."""
    if struct.unpack_from("<I", image, 4)[0] != CPU_TYPE_X86_64:
        return 0, 0
    segments, sections = _layout(image)
    if "__unwind_info" not in sections or "__TEXT" not in segments:
        return 0, 0
    _addr, size, fileoff = sections["__unwind_info"]
    text_vmaddr, text_fileoff = segments["__TEXT"]
    total = wrong = 0
    for function, encoding in _entries(image[fileoff:fileoff + size]):
        if encoding & MODE_MASK != MODE_STACK_IND:
            continue
        total += 1
        at = function - text_vmaddr + text_fileoff + ((encoding >> 16) & 0xFF)   # where the unwinder reads the size
        # the call after the immediate tells a real mov opcode from a size whose low byte is 0xb8 (b8 b8 1d 00 00)
        probe = image[at - 1:at] == MOV_EAX_IMM32 and image[at + 4:at + 5] == CALL_REL32
        if image[at - 3:at] != SUB_RSP_IMM32 and not probe:
            wrong += 1
    return total, wrong


def _binaries(path: Path) -> Iterator[tuple[str, bytes]]:
    if path.suffix == ".whl":
        with zipfile.ZipFile(path) as wheel:
            for name in sorted(wheel.namelist()):
                if name.endswith((".dylib", ".so")):
                    yield f"{path.name}:{name}", wheel.read(name)
    else:
        yield str(path), path.read_bytes()


def main(argv: list[str]) -> int:
    if len(argv) == 0:
        sys.stderr.write(__doc__ or "")
        return 2
    total = wrong = 0
    for arg in argv:
        for name, data in _binaries(Path(arg)):
            for image in _slices(data):
                here_total, here_wrong = wrong_entries(image)
                total += here_total
                wrong += here_wrong
                if here_wrong > 0:
                    print(f"{name}: {here_wrong} of {here_total} STACK_IND entries point next to the frame size")
    print(f"check_compact_unwind: {total} STACK_IND entries, {wrong} wrong")
    return 1 if wrong > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
