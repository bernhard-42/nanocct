"""OCCT package UnitsMethods (toolkit TKernel)"""

import enum
from typing import overload


class UnitsMethods_LengthUnit(enum.IntEnum):
    """The Enumeration describes possible values for length units"""

    UnitsMethods_LengthUnit_Undefined = 0

    UnitsMethods_LengthUnit_Inch = 1

    UnitsMethods_LengthUnit_Millimeter = 2

    UnitsMethods_LengthUnit_Foot = 4

    UnitsMethods_LengthUnit_Mile = 5

    UnitsMethods_LengthUnit_Meter = 6

    UnitsMethods_LengthUnit_Kilometer = 7

    UnitsMethods_LengthUnit_Mil = 8

    UnitsMethods_LengthUnit_Micron = 9

    UnitsMethods_LengthUnit_Centimeter = 10

    UnitsMethods_LengthUnit_Microinch = 11

class UnitsMethods:
    """Class for using global units variables"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: UnitsMethods) -> None: ...

    @staticmethod
    def GetLengthFactorValue(theUnit: int) -> float:
        """
        Returns value of unit encoded by parameter theUnit
        (integer value denoting unit, as described in IGES
        standard) in millimeters by default
        """

    @staticmethod
    def GetCasCadeLengthUnit(theBaseUnit: UnitsMethods_LengthUnit = ...) -> float:
        """
        Returns value of current internal unit for CASCADE
        in millemeters by default
        """

    @overload
    @staticmethod
    def SetCasCadeLengthUnit(theUnitValue: float, theBaseUnit: UnitsMethods_LengthUnit = ...) -> None:
        """Sets value of current internal unit for CASCADE"""

    @overload
    @staticmethod
    def SetCasCadeLengthUnit(theUnit: int) -> None:
        """
        Sets value of current internal unit for CASCADE
        by parameter theUnit (integer value denoting unit,
        as described in IGES standard)
        """

    @staticmethod
    def GetLengthUnitScale(theFromUnit: UnitsMethods_LengthUnit, theToUnit: UnitsMethods_LengthUnit) -> float:
        """
        Returns the scale factor for switch from first given unit to second given unit
        """

    @staticmethod
    def GetLengthUnitByFactorValue(theFactorValue: float, theBaseUnit: UnitsMethods_LengthUnit = ...) -> UnitsMethods_LengthUnit:
        """Returns the enumeration corresponding to the given scale factor"""

    @overload
    @staticmethod
    def DumpLengthUnit(theScaleFactor: float, theBaseUnit: UnitsMethods_LengthUnit = ...) -> str:
        """Returns string name for the given scale factor"""

    @overload
    @staticmethod
    def DumpLengthUnit(theUnit: UnitsMethods_LengthUnit) -> str:
        """Returns string for the given value of LengthUnit"""

    @staticmethod
    def LengthUnitFromString(theStr: str, theCaseSensitive: bool) -> UnitsMethods_LengthUnit:
        """Make conversion of given string to value of LengthUnit"""
