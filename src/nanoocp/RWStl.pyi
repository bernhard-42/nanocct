"""OCCT package RWStl (toolkit TKDESTL)"""

from typing import BinaryIO, TextIO, overload

import nanoocp.Message
import nanoocp.NCollection
import nanoocp.OSD
import nanoocp.Poly
import nanoocp.Standard
import nanoocp.gp


class RWStl:
    """
    This class provides methods to read and write triangulation from / to the STL files.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: RWStl) -> None: ...

    @overload
    @staticmethod
    def WriteBinary(theMesh: nanoocp.Poly.Poly_Triangulation | None, thePath: nanoocp.OSD.OSD_Path, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        Write triangulation to binary STL file.
        binary format of an STL file.
        Returns false if the cannot be opened;
        """

    @overload
    @staticmethod
    def WriteBinary(theMesh: nanoocp.Poly.Poly_Triangulation | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, bytes]:
        """Write triangulation to binary STL stream."""

    @overload
    @staticmethod
    def WriteAscii(theMesh: nanoocp.Poly.Poly_Triangulation | None, thePath: nanoocp.OSD.OSD_Path, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> bool:
        """
        write the meshing in a file following the
        Ascii format of an STL file.
        Returns false if the cannot be opened;
        """

    @overload
    @staticmethod
    def WriteAscii(theMesh: nanoocp.Poly.Poly_Triangulation | None, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> tuple[bool, str]:
        """Write triangulation to ASCII STL stream."""

    @overload
    @staticmethod
    def ReadFile(theFile: nanoocp.OSD.OSD_Path, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation: ...

    @overload
    @staticmethod
    def ReadFile(theFile: str, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read specified STL file and returns its content as triangulation.
        In case of error, returns Null handle.
        """

    @overload
    @staticmethod
    def ReadFile(theFile: str, theMergeAngle: float, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read specified STL file and returns its content as triangulation.
        @param[in] theFile file path to read
        @param[in] theMergeAngle maximum angle in radians between triangles to merge equal nodes;
        M_PI/2 means ignore angle
        @param[in] theProgress progress indicator
        @return result triangulation or NULL in case of error
        """

    @overload
    @staticmethod
    def ReadFile(theFile: str, theMergeAngle: float, theTriangList: nanoocp.NCollection.NCollection_Sequence[nanoocp.Poly.Poly_Triangulation], theProgress: nanoocp.Message.Message_ProgressRange = ...) -> None:
        """
        Read specified STL file and fills triangulation list for multi-domain case.
        @param[in] theFile file path to read
        @param[in] theMergeAngle maximum angle in radians between triangles to merge equal nodes;
        M_PI/2 means ignore angle
        @param[out] theTriangList triangulation list for multi-domain case
        @param[in] theProgress progress indicator
        """

    @staticmethod
    def ReadBinary(thePath: nanoocp.OSD.OSD_Path, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read triangulation from a binary STL file
        In case of error, returns Null handle.
        """

    @staticmethod
    def ReadAscii(thePath: nanoocp.OSD.OSD_Path, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read triangulation from an Ascii STL file
        In case of error, returns Null handle.
        """

    @staticmethod
    def ReadBinaryStream(theStream: BinaryIO, theMergeAngle: float = 1.5707963267948966, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read triangulation from binary STL stream
        In case of error, returns Null handle.
        """

    @staticmethod
    def ReadAsciiStream(theStream: TextIO, theMergeAngle: float = 1.5707963267948966, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read triangulation from ASCII STL stream
        In case of error, returns Null handle.
        """

    @staticmethod
    def ReadStream(theStream: BinaryIO, theMergeAngle: float = 1.5707963267948966, theProgress: nanoocp.Message.Message_ProgressRange = ...) -> nanoocp.Poly.Poly_Triangulation:
        """
        Read STL data from stream (auto-detects ASCII vs Binary)
        In case of error, returns Null handle.
        """

class RWStl_Reader(nanoocp.Standard.Standard_Transient):
    """
    An abstract class implementing procedure to read STL file.

    This class is not bound to particular data structure and can be used to read the file directly
    into arbitrary data model. To use it, create descendant class and implement methods addNode()
    and addTriangle().

    Call method Read() to read the file. In the process of reading, the tool will call methods
    addNode() and addTriangle() to fill the mesh data structure.

    The nodes with equal coordinates are merged automatically on the fly.
    """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

    def Read(self, theFile: str, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Reads data from STL file (either binary or Ascii).
        This function supports reading multi-domain STL files formed by concatenation
        of several "plain" files.
        The mesh nodes are not merged between domains.
        Unicode paths can be given in UTF-8 encoding.
        Format is recognized automatically by analysis of the file header.
        Returns true if success, false on error or user break.
        """

    def IsAscii(self, theStream: BinaryIO, isSeekgAvailable: bool) -> bool:
        """
        Guess whether the stream is an Ascii STL file, by analysis of the first bytes (~200).
        If the stream does not support seekg() then the parameter isSeekgAvailable should
        be passed as 'false', in this case the function attempts to put back the read symbols
        to the stream which thus must support ungetc().
        Returns true if the stream seems to contain Ascii STL.
        """

    def ReadBinary(self, theStream: BinaryIO, theProgress: nanoocp.Message.Message_ProgressRange) -> bool:
        """
        Reads STL data from binary stream.
        The stream must be opened in binary mode.
        Stops after reading the number of triangles recorded in the file header.
        Returns true if success, false on error or user break.
        """

    def AddNode(self, thePnt: nanoocp.gp.gp_XYZ) -> int:
        """
        Callback function to be implemented in descendant.
        Should create new node with specified coordinates in the target model, and return its ID as
        integer.
        """

    def AddTriangle(self, theN1: int, theN2: int, theN3: int) -> None:
        """
        Callback function to be implemented in descendant.
        Should create new triangle built on specified nodes in the target model.
        """

    def AddSolid(self) -> None:
        """
        Callback function to be implemented in descendant.
        Should create a new triangulation for a solid in multi-domain case.
        """

    def MergeAngle(self) -> float:
        """
        Return merge tolerance; M_PI/2 by default - all nodes are merged regardless angle between
        triangles.
        """

    def SetMergeAngle(self, theAngleRad: float) -> None:
        """
        Set merge angle in radians.
        Specify something like M_PI/4 (45 degrees) to avoid merge nodes between triangles at sharp
        corners.
        """

    def MergeTolerance(self) -> float:
        """
        Return linear merge tolerance; 0.0 by default (only 3D points with exactly matching
        coordinates are merged).
        """

    def SetMergeTolerance(self, theTolerance: float) -> None:
        """Set linear merge tolerance."""
