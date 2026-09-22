"""OCCT package StlAPI (toolkit TKDESTL)"""

from typing import TextIO, overload

import nanoocp.Message
import nanoocp.TopoDS


class StlAPI:
    """Offers the API for STL data manipulation."""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StlAPI) -> None: ...

    @staticmethod
    def Write(theShape: nanoocp.TopoDS.TopoDS_Shape, theFile: str, theAsciiMode: bool = True) -> bool:
        """
        Convert and write shape to STL format.
        File is written in binary if aAsciiMode is False otherwise it is written in Ascii (by
        default).
        """

    @staticmethod
    def Read(theShape: nanoocp.TopoDS.TopoDS_Shape, aFile: str) -> bool:
        """
        Deprecated in OCCT: This method is very inefficient; see RWStl class for better alternative
        """

class StlAPI_Reader:
    """
    Reading from stereolithography format.
    Reads STL file and creates a shape composed of triangular faces, one per facet.
    IMPORTANT: This approach is very inefficient, especially for large files.
    IMPORTANT: Consider reading STL file to Poly_Triangulation object instead (see class RWStl).
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StlAPI_Reader) -> None: ...

    @overload
    def Read(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theFileName: str) -> bool:
        """
        Reads STL file to the TopoDS_Shape (each triangle is converted to the face).
        @return True if reading is successful
        """

    @overload
    def Read(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theStream: TextIO) -> bool:
        """
        Reads STL data from stream to the TopoDS_Shape (each triangle is converted to the face).
        @param theShape result shape
        @param theStream stream to read from
        @return True if reading is successful
        """

class StlAPI_Writer:
    """
    This class creates and writes
    STL files from Open CASCADE shapes. An STL file can be written to an existing STL file or to a
    new one.
    """

    @overload
    def __init__(self) -> None:
        """Creates a writer object with default parameters: ASCIIMode."""

    @overload
    def __init__(self, theOther: StlAPI_Writer) -> None: ...

    def ASCIIMode(self) -> bool:
        """
        Returns the address to the flag defining the mode for writing the file.
        This address may be used to either read or change the flag.
        If the mode returns True (default value) the generated file is an ASCII file.
        If the mode returns False, the generated file is a binary file.
        """

    def SetASCIIMode(self, theValue: bool) -> None:
        """
        Python addition: sets the value ASCIIMode() returns by reference in C++.
        """

    @overload
    def Write(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theFileName: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Converts a given shape to STL format and writes it to file with a given filename.
        \\return the error state.
        """

    @overload
    def Write(self, theShape: nanoocp.TopoDS.TopoDS_Shape, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, str]:
        """
        Converts a given shape to STL format and writes it to the specified stream.
        \\return the error state.
        """
