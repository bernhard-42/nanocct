"""OCCT package UnitsAPI (toolkit TKernel)"""

import enum
from typing import overload

import nanoocp.Units


class UnitsAPI_SystemUnits(enum.IntEnum):
    """
    Identifies unit systems which may be defined as a
    basis system in the user's session:
    -   UnitsAPI_DEFAULT : default system (this is the SI system)
    -   UnitsAPI_SI : the SI unit system
    -   UnitsAPI_MDTV : the MDTV unit system; it
    is equivalent to the SI unit system but the
    length unit and all its derivatives use
    millimeters instead of meters.
    Use the function SetLocalSystem to set up one
    of these unit systems as working environment.
    """

    UnitsAPI_DEFAULT = 0

    UnitsAPI_SI = 1

    UnitsAPI_MDTV = 2

class UnitsAPI:
    """
    The UnitsAPI global functions are used to
    convert a value from any unit into another unit.
    Principles
    Conversion is executed among three unit systems:
    -   the SI System
    -   the user's Local System
    -   the user's Current System.
    The SI System is the standard international unit
    system. It is indicated by SI in the synopses of
    the UnitsAPI functions.
    The MDTV System corresponds to the SI
    international standard but the length unit and all
    its derivatives use millimeters instead of the meters.
    Both systems are proposed by Open CASCADE;
    the SI System is the standard option. By
    selecting one of these two systems, the user
    defines his Local System through the
    SetLocalSystem function. The Local System is
    indicated by LS in the synopses of the UnitsAPI functions.
    The user's Local System units can be modified in
    the working environment. The user defines his
    Current System by modifying its units through
    the SetCurrentUnit function. The Current
    System is indicated by Current in the synopses
    of the UnitsAPI functions.
    """

    def __init__(self) -> None: ...

    @staticmethod
    def CurrentToLS(aData: float, aQuantity: str) -> float:
        """
        Converts the current unit value to the local system units value.
        Example: CurrentToLS(1.,"LENGTH") returns 1000. if the current length unit
        is meter and LocalSystem is MDTV.
        """

    @staticmethod
    def CurrentToSI(aData: float, aQuantity: str) -> float:
        """
        Converts the current unit value to the SI system units value.
        Example: CurrentToSI(1.,"LENGTH") returns 0.001 if current length unit
        is millimeter.
        """

    @staticmethod
    def CurrentFromLS(aData: float, aQuantity: str) -> float:
        """
        Converts the local system units value to the current unit value.
        Example: CurrentFromLS(1000.,"LENGTH") returns 1. if current length unit
        is meter and LocalSystem is MDTV.
        """

    @staticmethod
    def CurrentFromSI(aData: float, aQuantity: str) -> float:
        """
        Converts the SI system units value to the current unit value.
        Example: CurrentFromSI(0.001,"LENGTH") returns 1 if current length unit
        is millimeter.
        """

    @overload
    @staticmethod
    def AnyToLS(aData: float, aUnit: str) -> float:
        """
        Converts the local unit value to the local system units value.
        Example: AnyToLS(1.,"in.") returns 25.4 if the LocalSystem is MDTV.
        """

    @overload
    @staticmethod
    def AnyToLS(aData: float, aUnit: str, aDim: nanoocp.Units.Units_Dimensions) -> float:
        """
        Converts the local unit value to the local system units value.
        and gives the associated dimension of the unit
        """

    @overload
    @staticmethod
    def AnyToSI(aData: float, aUnit: str) -> float:
        """
        Converts the local unit value to the SI system units value.
        Example: AnyToSI(1.,"in.") returns 0.0254
        """

    @overload
    @staticmethod
    def AnyToSI(aData: float, aUnit: str, aDim: nanoocp.Units.Units_Dimensions) -> float:
        """
        Converts the local unit value to the SI system units value.
        and gives the associated dimension of the unit
        """

    @staticmethod
    def AnyFromLS(aData: float, aUnit: str) -> float:
        """
        Converts the local system units value to the local unit value.
        Example: AnyFromLS(25.4,"in.") returns 1. if the LocalSystem is MDTV.
        Note: aUnit is also used to identify the type of physical quantity to convert.
        """

    @staticmethod
    def AnyFromSI(aData: float, aUnit: str) -> float:
        """
        Converts the SI system units value to the local unit value.
        Example: AnyFromSI(0.0254,"in.") returns 0.001
        Note: aUnit is also used to identify the type of physical quantity to convert.
        """

    @staticmethod
    def CurrentToAny(aData: float, aQuantity: str, aUnit: str) -> float:
        """
        Converts the aData value expressed in the
        current unit for the working environment, as
        defined for the physical quantity aQuantity by the
        last call to the SetCurrentUnit function, into the unit aUnit.
        """

    @staticmethod
    def CurrentFromAny(aData: float, aQuantity: str, aUnit: str) -> float:
        """
        Converts the aData value expressed in the unit
        aUnit, into the current unit for the working
        environment, as defined for the physical quantity
        aQuantity by the last call to the SetCurrentUnit function.
        """

    @staticmethod
    def AnyToAny(aData: float, aUnit1: str, aUnit2: str) -> float:
        """
        Converts the local unit value to another local unit value.
        Example: AnyToAny(0.0254,"in.","mm") returns 1. ;
        """

    @staticmethod
    def LSToSI(aData: float, aQuantity: str) -> float:
        """
        Converts the local system units value to the SI system unit value.
        Example: LSToSI(1.,"LENGTH") returns 0.001 if the local system
        length unit is millimeter.
        """

    @staticmethod
    def SIToLS(aData: float, aQuantity: str) -> float:
        """
        Converts the SI system unit value to the local system units value.
        Example: SIToLS(1.,"LENGTH") returns 1000. if the local system
        length unit is millimeter.
        """

    @staticmethod
    def SetLocalSystem(aSystemUnit: UnitsAPI_SystemUnits = UnitsAPI_SystemUnits.UnitsAPI_SI) -> None:
        """
        Sets the local system units.
        Example: SetLocalSystem(UnitsAPI_MDTV)
        """

    @staticmethod
    def LocalSystem() -> UnitsAPI_SystemUnits:
        """Returns the current local system units."""

    @staticmethod
    def SetCurrentUnit(aQuantity: str, aUnit: str) -> None:
        """
        Sets the current unit dimension <aUnit> to the unit quantity <aQuantity>.
        Example: SetCurrentUnit("LENGTH","mm")
        """

    @staticmethod
    def CurrentUnit(aQuantity: str) -> str:
        """
        Returns the current unit dimension <aUnit> from the unit quantity <aQuantity>.
        """

    @staticmethod
    def Save() -> None:
        """
        saves the units in the file .CurrentUnits of the directory pointed by the
        CSF_CurrentUnitsUserDefaults environment variable.
        """

    @staticmethod
    def Reload() -> None: ...

    @staticmethod
    def Dimensions(aQuantity: str) -> nanoocp.Units.Units_Dimensions:
        """return the dimension associated to the quantity"""

    @staticmethod
    def DimensionLess() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionMass() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionLength() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionTime() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionElectricCurrent() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionThermodynamicTemperature() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionAmountOfSubstance() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionLuminousIntensity() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionPlaneAngle() -> nanoocp.Units.Units_Dimensions: ...

    @staticmethod
    def DimensionSolidAngle() -> nanoocp.Units.Units_Dimensions:
        """Returns the basic dimensions."""

    @staticmethod
    def Check(aQuantity: str, aUnit: str) -> bool:
        """
        Checks the coherence between the quantity <aQuantity>
        and the unit <aUnits> in the current system and
        returns FALSE when it's WRONG.
        """
