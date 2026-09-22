"""OCCT package StepBasic (toolkit TKDESTEP)"""

import enum
from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.StepData
import nanoocp.StepRepr
import nanoocp.TCollection


class StepBasic_AheadOrBehind(enum.IntEnum):
    StepBasic_aobAhead = 0

    StepBasic_aobExact = 1

    StepBasic_aobBehind = 2

StepBasic_aobAhead: StepBasic_AheadOrBehind = StepBasic_AheadOrBehind.StepBasic_aobAhead

StepBasic_aobExact: StepBasic_AheadOrBehind = StepBasic_AheadOrBehind.StepBasic_aobExact

StepBasic_aobBehind: StepBasic_AheadOrBehind = StepBasic_AheadOrBehind.StepBasic_aobBehind

class StepBasic_Source(enum.IntEnum):
    StepBasic_sMade = 0

    StepBasic_sBought = 1

    StepBasic_sNotKnown = 2

StepBasic_sMade: StepBasic_Source = StepBasic_Source.StepBasic_sMade

StepBasic_sBought: StepBasic_Source = StepBasic_Source.StepBasic_sBought

StepBasic_sNotKnown: StepBasic_Source = StepBasic_Source.StepBasic_sNotKnown

class StepBasic_SiPrefix(enum.IntEnum):
    StepBasic_spExa = 0

    StepBasic_spPeta = 1

    StepBasic_spTera = 2

    StepBasic_spGiga = 3

    StepBasic_spMega = 4

    StepBasic_spKilo = 5

    StepBasic_spHecto = 6

    StepBasic_spDeca = 7

    StepBasic_spDeci = 8

    StepBasic_spCenti = 9

    StepBasic_spMilli = 10

    StepBasic_spMicro = 11

    StepBasic_spNano = 12

    StepBasic_spPico = 13

    StepBasic_spFemto = 14

    StepBasic_spAtto = 15

StepBasic_spExa: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spExa

StepBasic_spPeta: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spPeta

StepBasic_spTera: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spTera

StepBasic_spGiga: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spGiga

StepBasic_spMega: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spMega

StepBasic_spKilo: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spKilo

StepBasic_spHecto: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spHecto

StepBasic_spDeca: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spDeca

StepBasic_spDeci: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spDeci

StepBasic_spCenti: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spCenti

StepBasic_spMilli: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spMilli

StepBasic_spMicro: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spMicro

StepBasic_spNano: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spNano

StepBasic_spPico: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spPico

StepBasic_spFemto: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spFemto

StepBasic_spAtto: StepBasic_SiPrefix = StepBasic_SiPrefix.StepBasic_spAtto

class StepBasic_SiUnitName(enum.IntEnum):
    StepBasic_sunMetre = 0

    StepBasic_sunGram = 1

    StepBasic_sunSecond = 2

    StepBasic_sunAmpere = 3

    StepBasic_sunKelvin = 4

    StepBasic_sunMole = 5

    StepBasic_sunCandela = 6

    StepBasic_sunRadian = 7

    StepBasic_sunSteradian = 8

    StepBasic_sunHertz = 9

    StepBasic_sunNewton = 10

    StepBasic_sunPascal = 11

    StepBasic_sunJoule = 12

    StepBasic_sunWatt = 13

    StepBasic_sunCoulomb = 14

    StepBasic_sunVolt = 15

    StepBasic_sunFarad = 16

    StepBasic_sunOhm = 17

    StepBasic_sunSiemens = 18

    StepBasic_sunWeber = 19

    StepBasic_sunTesla = 20

    StepBasic_sunHenry = 21

    StepBasic_sunDegreeCelsius = 22

    StepBasic_sunLumen = 23

    StepBasic_sunLux = 24

    StepBasic_sunBecquerel = 25

    StepBasic_sunGray = 26

    StepBasic_sunSievert = 27

StepBasic_sunMetre: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunMetre

StepBasic_sunGram: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunGram

StepBasic_sunSecond: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunSecond

StepBasic_sunAmpere: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunAmpere

StepBasic_sunKelvin: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunKelvin

StepBasic_sunMole: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunMole

StepBasic_sunCandela: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunCandela

StepBasic_sunRadian: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunRadian

StepBasic_sunSteradian: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunSteradian

StepBasic_sunHertz: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunHertz

StepBasic_sunNewton: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunNewton

StepBasic_sunPascal: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunPascal

StepBasic_sunJoule: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunJoule

StepBasic_sunWatt: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunWatt

StepBasic_sunCoulomb: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunCoulomb

StepBasic_sunVolt: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunVolt

StepBasic_sunFarad: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunFarad

StepBasic_sunOhm: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunOhm

StepBasic_sunSiemens: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunSiemens

StepBasic_sunWeber: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunWeber

StepBasic_sunTesla: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunTesla

StepBasic_sunHenry: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunHenry

StepBasic_sunDegreeCelsius: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunDegreeCelsius

StepBasic_sunLumen: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunLumen

StepBasic_sunLux: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunLux

StepBasic_sunBecquerel: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunBecquerel

StepBasic_sunGray: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunGray

StepBasic_sunSievert: StepBasic_SiUnitName = StepBasic_SiUnitName.StepBasic_sunSievert

class StepBasic_Action(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Action"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_Action) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aChosenMethod: StepBasic_ActionMethod | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def ChosenMethod(self) -> StepBasic_ActionMethod:
        """Returns field ChosenMethod"""

    def SetChosenMethod(self, ChosenMethod: StepBasic_ActionMethod | None) -> None:
        """Set field ChosenMethod"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ActionAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ActionAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ActionAssignment) -> None: ...

    def Init(self, aAssignedAction: StepBasic_Action | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedAction(self) -> StepBasic_Action:
        """Returns field AssignedAction"""

    def SetAssignedAction(self, AssignedAction: StepBasic_Action | None) -> None:
        """Set field AssignedAction"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ActionMethod(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ActionMethod"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ActionMethod) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aConsequence: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def Consequence(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Consequence"""

    def SetConsequence(self, Consequence: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Consequence"""

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Purpose"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ActionRequestAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ActionRequestAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ActionRequestAssignment) -> None: ...

    def Init(self, aAssignedActionRequest: StepBasic_VersionedActionRequest | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedActionRequest(self) -> StepBasic_VersionedActionRequest:
        """Returns field AssignedActionRequest"""

    def SetAssignedActionRequest(self, AssignedActionRequest: StepBasic_VersionedActionRequest | None) -> None:
        """Set field AssignedActionRequest"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ActionRequestSolution(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ActionRequestSolution"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ActionRequestSolution) -> None: ...

    def Init(self, aMethod: StepBasic_ActionMethod | None, aRequest: StepBasic_VersionedActionRequest | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Method(self) -> StepBasic_ActionMethod:
        """Returns field Method"""

    def SetMethod(self, Method: StepBasic_ActionMethod | None) -> None:
        """Set field Method"""

    def Request(self) -> StepBasic_VersionedActionRequest:
        """Returns field Request"""

    def SetRequest(self, Request: StepBasic_VersionedActionRequest | None) -> None:
        """Set field Request"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Address(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Address"""

    @overload
    def __init__(self, theOther: StepBasic_Address) -> None: ...

    def Init(self, hasAinternalLocation: bool, aInternalLocation: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreetNumber: bool, aStreetNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreet: bool, aStreet: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalBox: bool, aPostalBox: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtown: bool, aTown: nanoocp.TCollection.TCollection_HAsciiString | None, hasAregion: bool, aRegion: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalCode: bool, aPostalCode: nanoocp.TCollection.TCollection_HAsciiString | None, hasAcountry: bool, aCountry: nanoocp.TCollection.TCollection_HAsciiString | None, hasAfacsimileNumber: bool, aFacsimileNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelephoneNumber: bool, aTelephoneNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAelectronicMailAddress: bool, aElectronicMailAddress: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelexNumber: bool, aTelexNumber: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetInternalLocation(self, aInternalLocation: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetInternalLocation(self) -> None: ...

    def InternalLocation(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasInternalLocation(self) -> bool: ...

    def SetStreetNumber(self, aStreetNumber: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetStreetNumber(self) -> None: ...

    def StreetNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasStreetNumber(self) -> bool: ...

    def SetStreet(self, aStreet: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetStreet(self) -> None: ...

    def Street(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasStreet(self) -> bool: ...

    def SetPostalBox(self, aPostalBox: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetPostalBox(self) -> None: ...

    def PostalBox(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasPostalBox(self) -> bool: ...

    def SetTown(self, aTown: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetTown(self) -> None: ...

    def Town(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasTown(self) -> bool: ...

    def SetRegion(self, aRegion: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetRegion(self) -> None: ...

    def Region(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasRegion(self) -> bool: ...

    def SetPostalCode(self, aPostalCode: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetPostalCode(self) -> None: ...

    def PostalCode(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasPostalCode(self) -> bool: ...

    def SetCountry(self, aCountry: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetCountry(self) -> None: ...

    def Country(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasCountry(self) -> bool: ...

    def SetFacsimileNumber(self, aFacsimileNumber: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetFacsimileNumber(self) -> None: ...

    def FacsimileNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasFacsimileNumber(self) -> bool: ...

    def SetTelephoneNumber(self, aTelephoneNumber: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetTelephoneNumber(self) -> None: ...

    def TelephoneNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasTelephoneNumber(self) -> bool: ...

    def SetElectronicMailAddress(self, aElectronicMailAddress: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetElectronicMailAddress(self) -> None: ...

    def ElectronicMailAddress(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasElectronicMailAddress(self) -> bool: ...

    def SetTelexNumber(self, aTelexNumber: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetTelexNumber(self) -> None: ...

    def TelexNumber(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasTelexNumber(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApplicationContext(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApplicationContext"""

    @overload
    def __init__(self, theOther: StepBasic_ApplicationContext) -> None: ...

    def Init(self, aApplication: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetApplication(self, aApplication: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Application(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApplicationContextElement(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApplicationContextElement"""

    @overload
    def __init__(self, theOther: StepBasic_ApplicationContextElement) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFrameOfReference: StepBasic_ApplicationContext | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFrameOfReference(self, aFrameOfReference: StepBasic_ApplicationContext | None) -> None: ...

    def FrameOfReference(self) -> StepBasic_ApplicationContext: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApplicationProtocolDefinition(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApplicationProtocolDefinition"""

    @overload
    def __init__(self, theOther: StepBasic_ApplicationProtocolDefinition) -> None: ...

    def Init(self, aStatus: nanoocp.TCollection.TCollection_HAsciiString | None, aApplicationInterpretedModelSchemaName: nanoocp.TCollection.TCollection_HAsciiString | None, aApplicationProtocolYear: int, aApplication: StepBasic_ApplicationContext | None) -> None: ...

    def SetStatus(self, aStatus: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Status(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetApplicationInterpretedModelSchemaName(self, aApplicationInterpretedModelSchemaName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ApplicationInterpretedModelSchemaName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetApplicationProtocolYear(self, aApplicationProtocolYear: int) -> None: ...

    def ApplicationProtocolYear(self) -> int: ...

    def SetApplication(self, aApplication: StepBasic_ApplicationContext | None) -> None: ...

    def Application(self) -> StepBasic_ApplicationContext: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Approval(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Approval"""

    @overload
    def __init__(self, theOther: StepBasic_Approval) -> None: ...

    def Init(self, aStatus: StepBasic_ApprovalStatus | None, aLevel: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetStatus(self, aStatus: StepBasic_ApprovalStatus | None) -> None: ...

    def Status(self) -> StepBasic_ApprovalStatus: ...

    def SetLevel(self, aLevel: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Level(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApprovalAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_ApprovalAssignment) -> None: ...

    def Init(self, aAssignedApproval: StepBasic_Approval | None) -> None: ...

    def SetAssignedApproval(self, aAssignedApproval: StepBasic_Approval | None) -> None: ...

    def AssignedApproval(self) -> StepBasic_Approval: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateTimeSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a DateTimeSelect SelectType"""

    @overload
    def __init__(self, theOther: StepBasic_DateTimeSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a DateTimeSelect Kind Entity that is :
        1 -> Date
        2 -> LocalTime
        3 -> DateAndTime
        0 else
        """

    def Date(self) -> StepBasic_Date:
        """returns Value as a Date (Null if another type)"""

    def LocalTime(self) -> StepBasic_LocalTime:
        """returns Value as a LocalTime (Null if another type)"""

    def DateAndTime(self) -> StepBasic_DateAndTime:
        """returns Value as a DateAndTime (Null if another type)"""

class StepBasic_ApprovalDateTime(nanoocp.Standard.Standard_Transient):
    """Added from StepBasic Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_ApprovalDateTime) -> None: ...

    def Init(self, aDateTime: StepBasic_DateTimeSelect, aDatedApproval: StepBasic_Approval | None) -> None: ...

    def SetDateTime(self, aDateTime: StepBasic_DateTimeSelect) -> None: ...

    def DateTime(self) -> StepBasic_DateTimeSelect: ...

    def SetDatedApproval(self, aDatedApproval: StepBasic_Approval | None) -> None: ...

    def DatedApproval(self) -> StepBasic_Approval: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PersonOrganizationSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a PersonOrganizationSelect SelectType"""

    @overload
    def __init__(self, theOther: StepBasic_PersonOrganizationSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a PersonOrganizationSelect Kind Entity that is :
        1 -> Person
        2 -> Organization
        3 -> PersonAndOrganization
        0 else
        """

    def Person(self) -> StepBasic_Person:
        """returns Value as a Person (Null if another type)"""

    def Organization(self) -> StepBasic_Organization:
        """returns Value as a Organization (Null if another type)"""

    def PersonAndOrganization(self) -> StepBasic_PersonAndOrganization:
        """returns Value as a PersonAndOrganization (Null if another type)"""

class StepBasic_ApprovalPersonOrganization(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApprovalPersonOrganization"""

    @overload
    def __init__(self, theOther: StepBasic_ApprovalPersonOrganization) -> None: ...

    def Init(self, aPersonOrganization: StepBasic_PersonOrganizationSelect, aAuthorizedApproval: StepBasic_Approval | None, aRole: StepBasic_ApprovalRole | None) -> None: ...

    def SetPersonOrganization(self, aPersonOrganization: StepBasic_PersonOrganizationSelect) -> None: ...

    def PersonOrganization(self) -> StepBasic_PersonOrganizationSelect: ...

    def SetAuthorizedApproval(self, aAuthorizedApproval: StepBasic_Approval | None) -> None: ...

    def AuthorizedApproval(self) -> StepBasic_Approval: ...

    def SetRole(self, aRole: StepBasic_ApprovalRole | None) -> None: ...

    def Role(self) -> StepBasic_ApprovalRole: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApprovalRelationship(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApprovalRelationship"""

    @overload
    def __init__(self, theOther: StepBasic_ApprovalRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingApproval: StepBasic_Approval | None, aRelatedApproval: StepBasic_Approval | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetRelatingApproval(self, aRelatingApproval: StepBasic_Approval | None) -> None: ...

    def RelatingApproval(self) -> StepBasic_Approval: ...

    def SetRelatedApproval(self, aRelatedApproval: StepBasic_Approval | None) -> None: ...

    def RelatedApproval(self) -> StepBasic_Approval: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApprovalRole(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApprovalRole"""

    @overload
    def __init__(self, theOther: StepBasic_ApprovalRole) -> None: ...

    def Init(self, aRole: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetRole(self, aRole: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Role(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ApprovalStatus(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ApprovalStatus"""

    @overload
    def __init__(self, theOther: StepBasic_ApprovalStatus) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_NamedUnit(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a NamedUnit"""

    @overload
    def __init__(self, theOther: StepBasic_NamedUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None) -> None: ...

    def SetDimensions(self, aDimensions: StepBasic_DimensionalExponents | None) -> None: ...

    def Dimensions(self) -> StepBasic_DimensionalExponents: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_AreaUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_AreaUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Date(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Date"""

    @overload
    def __init__(self, theOther: StepBasic_Date) -> None: ...

    def Init(self, aYearComponent: int) -> None: ...

    def SetYearComponent(self, aYearComponent: int) -> None: ...

    def YearComponent(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_CalendarDate(StepBasic_Date):
    @overload
    def __init__(self) -> None:
        """Returns a CalendarDate"""

    @overload
    def __init__(self, theOther: StepBasic_CalendarDate) -> None: ...

    def Init(self, aYearComponent: int, aDayComponent: int, aMonthComponent: int) -> None: ...

    def SetDayComponent(self, aDayComponent: int) -> None: ...

    def DayComponent(self) -> int: ...

    def SetMonthComponent(self, aMonthComponent: int) -> None: ...

    def MonthComponent(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Certification(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Certification"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_Certification) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None, aKind: StepBasic_CertificationType | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Purpose"""

    def Kind(self) -> StepBasic_CertificationType:
        """Returns field Kind"""

    def SetKind(self, Kind: StepBasic_CertificationType | None) -> None:
        """Set field Kind"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_CertificationAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CertificationAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_CertificationAssignment) -> None: ...

    def Init(self, aAssignedCertification: StepBasic_Certification | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedCertification(self) -> StepBasic_Certification:
        """Returns field AssignedCertification"""

    def SetAssignedCertification(self, AssignedCertification: StepBasic_Certification | None) -> None:
        """Set field AssignedCertification"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_CertificationType(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CertificationType"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_CertificationType) -> None: ...

    def Init(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_CharacterizedObject(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity CharacterizedObject"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_CharacterizedObject) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Contract(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Contract"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_Contract) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None, aKind: StepBasic_ContractType | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Purpose"""

    def Kind(self) -> StepBasic_ContractType:
        """Returns field Kind"""

    def SetKind(self, Kind: StepBasic_ContractType | None) -> None:
        """Set field Kind"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ContractAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ContractAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ContractAssignment) -> None: ...

    def Init(self, aAssignedContract: StepBasic_Contract | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedContract(self) -> StepBasic_Contract:
        """Returns field AssignedContract"""

    def SetAssignedContract(self, AssignedContract: StepBasic_Contract | None) -> None:
        """Set field AssignedContract"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ContractType(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ContractType"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ContractType) -> None: ...

    def Init(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetConversionFactor(self, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def ConversionFactor(self) -> nanoocp.Standard.Standard_Transient: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndAreaUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndAreaUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndAreaUnit) -> None: ...

    def SetAreaUnit(self, anAreaUnit: StepBasic_AreaUnit | None) -> None: ...

    def AreaUnit(self) -> StepBasic_AreaUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndLengthUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndLengthUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndLengthUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetLengthUnit(self, aLengthUnit: StepBasic_LengthUnit | None) -> None: ...

    def LengthUnit(self) -> StepBasic_LengthUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndMassUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndLengthUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndMassUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetMassUnit(self, aMassUnit: StepBasic_MassUnit | None) -> None: ...

    def MassUnit(self) -> StepBasic_MassUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndPlaneAngleUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndPlaneAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndPlaneAngleUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetPlaneAngleUnit(self, aPlaneAngleUnit: StepBasic_PlaneAngleUnit | None) -> None: ...

    def PlaneAngleUnit(self) -> StepBasic_PlaneAngleUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndRatioUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndRatioUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndRatioUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetRatioUnit(self, aRatioUnit: StepBasic_RatioUnit | None) -> None: ...

    def RatioUnit(self) -> StepBasic_RatioUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndSolidAngleUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndSolidAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndSolidAngleUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetSolidAngleUnit(self, aSolidAngleUnit: StepBasic_SolidAngleUnit | None) -> None: ...

    def SolidAngleUnit(self) -> StepBasic_SolidAngleUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndTimeUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndTimeUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndTimeUnit) -> None: ...

    def Init(self, aDimensions: StepBasic_DimensionalExponents | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aConversionFactor: nanoocp.Standard.Standard_Transient | None) -> None: ...

    def SetTimeUnit(self, aTimeUnit: StepBasic_TimeUnit | None) -> None: ...

    def TimeUnit(self) -> StepBasic_TimeUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ConversionBasedUnitAndVolumeUnit(StepBasic_ConversionBasedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a ConversionBasedUnitAndVolumeUnit"""

    @overload
    def __init__(self, theOther: StepBasic_ConversionBasedUnitAndVolumeUnit) -> None: ...

    def SetVolumeUnit(self, aVolumeUnit: StepBasic_VolumeUnit | None) -> None: ...

    def VolumeUnit(self) -> StepBasic_VolumeUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_CoordinatedUniversalTimeOffset(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a CoordinatedUniversalTimeOffset"""

    @overload
    def __init__(self, theOther: StepBasic_CoordinatedUniversalTimeOffset) -> None: ...

    def Init(self, aHourOffset: int, hasAminuteOffset: bool, aMinuteOffset: int, aSense: StepBasic_AheadOrBehind) -> None: ...

    def SetHourOffset(self, aHourOffset: int) -> None: ...

    def HourOffset(self) -> int: ...

    def SetMinuteOffset(self, aMinuteOffset: int) -> None: ...

    def UnSetMinuteOffset(self) -> None: ...

    def MinuteOffset(self) -> int: ...

    def HasMinuteOffset(self) -> bool: ...

    def SetSense(self, aSense: StepBasic_AheadOrBehind) -> None: ...

    def Sense(self) -> StepBasic_AheadOrBehind: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateAndTime(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a DateAndTime"""

    @overload
    def __init__(self, theOther: StepBasic_DateAndTime) -> None: ...

    def Init(self, aDateComponent: StepBasic_Date | None, aTimeComponent: StepBasic_LocalTime | None) -> None: ...

    def SetDateComponent(self, aDateComponent: StepBasic_Date | None) -> None: ...

    def DateComponent(self) -> StepBasic_Date: ...

    def SetTimeComponent(self, aTimeComponent: StepBasic_LocalTime | None) -> None: ...

    def TimeComponent(self) -> StepBasic_LocalTime: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateAndTimeAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DateAndTimeAssignment) -> None: ...

    def Init(self, aAssignedDateAndTime: StepBasic_DateAndTime | None, aRole: StepBasic_DateTimeRole | None) -> None: ...

    def SetAssignedDateAndTime(self, aAssignedDateAndTime: StepBasic_DateAndTime | None) -> None: ...

    def AssignedDateAndTime(self) -> StepBasic_DateAndTime: ...

    def SetRole(self, aRole: StepBasic_DateTimeRole | None) -> None: ...

    def Role(self) -> StepBasic_DateTimeRole: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DateAssignment) -> None: ...

    def Init(self, aAssignedDate: StepBasic_Date | None, aRole: StepBasic_DateRole | None) -> None: ...

    def SetAssignedDate(self, aAssignedDate: StepBasic_Date | None) -> None: ...

    def AssignedDate(self) -> StepBasic_Date: ...

    def SetRole(self, aRole: StepBasic_DateRole | None) -> None: ...

    def Role(self) -> StepBasic_DateRole: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateRole(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a DateRole"""

    @overload
    def __init__(self, theOther: StepBasic_DateRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DateTimeRole(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a DateTimeRole"""

    @overload
    def __init__(self, theOther: StepBasic_DateTimeRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DerivedUnitElement(nanoocp.Standard.Standard_Transient):
    """Added from StepBasic Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DerivedUnitElement) -> None: ...

    def Init(self, aUnit: StepBasic_NamedUnit | None, aExponent: float) -> None: ...

    def SetUnit(self, aUnit: StepBasic_NamedUnit | None) -> None: ...

    def Unit(self) -> StepBasic_NamedUnit: ...

    def SetExponent(self, aExponent: float) -> None: ...

    def Exponent(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DerivedUnit(nanoocp.Standard.Standard_Transient):
    """Added from StepBasic Rev2 to Rev4"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DerivedUnit) -> None: ...

    def Init(self, elements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_DerivedUnitElement] | None) -> None: ...

    def SetElements(self, elements: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_DerivedUnitElement] | None) -> None: ...

    def Elements(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_DerivedUnitElement]: ...

    def NbElements(self) -> int: ...

    def ElementsValue(self, num: int) -> StepBasic_DerivedUnitElement: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionContext(StepBasic_ApplicationContextElement):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinitionContext"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionContext) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFrameOfReference: StepBasic_ApplicationContext | None, aLifeCycleStage: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetLifeCycleStage(self, aLifeCycleStage: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def LifeCycleStage(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DesignContext(StepBasic_ProductDefinitionContext):
    """class added to Schema AP214 around April 1996"""

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DesignContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Document(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Document"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_Document) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aKind: StepBasic_DocumentType | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def Kind(self) -> StepBasic_DocumentType:
        """Returns field Kind"""

    def SetKind(self, Kind: StepBasic_DocumentType | None) -> None:
        """Set field Kind"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DigitalDocument(StepBasic_Document):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DigitalDocument) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DimensionalExponents(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a DimensionalExponents"""

    @overload
    def __init__(self, theOther: StepBasic_DimensionalExponents) -> None: ...

    def Init(self, aLengthExponent: float, aMassExponent: float, aTimeExponent: float, aElectricCurrentExponent: float, aThermodynamicTemperatureExponent: float, aAmountOfSubstanceExponent: float, aLuminousIntensityExponent: float) -> None: ...

    def SetLengthExponent(self, aLengthExponent: float) -> None: ...

    def LengthExponent(self) -> float: ...

    def SetMassExponent(self, aMassExponent: float) -> None: ...

    def MassExponent(self) -> float: ...

    def SetTimeExponent(self, aTimeExponent: float) -> None: ...

    def TimeExponent(self) -> float: ...

    def SetElectricCurrentExponent(self, aElectricCurrentExponent: float) -> None: ...

    def ElectricCurrentExponent(self) -> float: ...

    def SetThermodynamicTemperatureExponent(self, aThermodynamicTemperatureExponent: float) -> None: ...

    def ThermodynamicTemperatureExponent(self) -> float: ...

    def SetAmountOfSubstanceExponent(self, aAmountOfSubstanceExponent: float) -> None: ...

    def AmountOfSubstanceExponent(self) -> float: ...

    def SetLuminousIntensityExponent(self, aLuminousIntensityExponent: float) -> None: ...

    def LuminousIntensityExponent(self) -> float: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentFile(StepBasic_Document):
    """Representation of STEP entity DocumentFile"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_DocumentFile) -> None: ...

    def Init(self, aDocument_Id: nanoocp.TCollection.TCollection_HAsciiString | None, aDocument_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasDocument_Description: bool, aDocument_Description: nanoocp.TCollection.TCollection_HAsciiString | None, aDocument_Kind: StepBasic_DocumentType | None, aCharacterizedObject_Name: nanoocp.TCollection.TCollection_HAsciiString | None, hasCharacterizedObject_Description: bool, aCharacterizedObject_Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def CharacterizedObject(self) -> StepBasic_CharacterizedObject:
        """Returns data for supertype CharacterizedObject"""

    def SetCharacterizedObject(self, CharacterizedObject: StepBasic_CharacterizedObject | None) -> None:
        """Set data for supertype CharacterizedObject"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductOrFormationOrDefinition(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type ProductOrFormationOrDefinition"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductOrFormationOrDefinition) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of ProductOrFormationOrDefinition select type
        1 -> Product from StepBasic
        2 -> ProductDefinitionFormation from StepBasic
        3 -> ProductDefinition from StepBasic
        0 else
        """

    def Product(self) -> StepBasic_Product:
        """Returns Value as Product (or Null if another type)"""

    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation:
        """Returns Value as ProductDefinitionFormation (or Null if another type)"""

    def ProductDefinition(self) -> StepBasic_ProductDefinition:
        """Returns Value as ProductDefinition (or Null if another type)"""

class StepBasic_DocumentProductAssociation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DocumentProductAssociation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_DocumentProductAssociation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingDocument: StepBasic_Document | None, aRelatedProduct: StepBasic_ProductOrFormationOrDefinition) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def RelatingDocument(self) -> StepBasic_Document:
        """Returns field RelatingDocument"""

    def SetRelatingDocument(self, RelatingDocument: StepBasic_Document | None) -> None:
        """Set field RelatingDocument"""

    def RelatedProduct(self) -> StepBasic_ProductOrFormationOrDefinition:
        """Returns field RelatedProduct"""

    def SetRelatedProduct(self, RelatedProduct: StepBasic_ProductOrFormationOrDefinition) -> None:
        """Set field RelatedProduct"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentProductEquivalence(StepBasic_DocumentProductAssociation):
    """Representation of STEP entity DocumentProductEquivalence"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_DocumentProductEquivalence) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentReference(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DocumentReference) -> None: ...

    def Init0(self, aAssignedDocument: StepBasic_Document | None, aSource: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def AssignedDocument(self) -> StepBasic_Document: ...

    def SetAssignedDocument(self, aAssignedDocument: StepBasic_Document | None) -> None: ...

    def Source(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetSource(self, aSource: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentRelationship(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DocumentRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelating: StepBasic_Document | None, aRelated: StepBasic_Document | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def RelatingDocument(self) -> StepBasic_Document: ...

    def SetRelatingDocument(self, aRelating: StepBasic_Document | None) -> None: ...

    def RelatedDocument(self) -> StepBasic_Document: ...

    def SetRelatedDocument(self, aRelated: StepBasic_Document | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentRepresentationType(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity DocumentRepresentationType"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_DocumentRepresentationType) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aRepresentedDocument: StepBasic_Document | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def RepresentedDocument(self) -> StepBasic_Document:
        """Returns field RepresentedDocument"""

    def SetRepresentedDocument(self, RepresentedDocument: StepBasic_Document | None) -> None:
        """Set field RepresentedDocument"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentType(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DocumentType) -> None: ...

    def Init(self, apdt: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def ProductDataType(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetProductDataType(self, apdt: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_DocumentUsageConstraint(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_DocumentUsageConstraint) -> None: ...

    def Init(self, aSource: StepBasic_Document | None, ase: nanoocp.TCollection.TCollection_HAsciiString | None, asev: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Source(self) -> StepBasic_Document: ...

    def SetSource(self, aSource: StepBasic_Document | None) -> None: ...

    def SubjectElement(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetSubjectElement(self, ase: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SubjectElementValue(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetSubjectElementValue(self, asev: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Effectivity(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_Effectivity) -> None: ...

    def Init(self, aid: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetId(self, aid: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_EffectivityAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity EffectivityAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_EffectivityAssignment) -> None: ...

    def Init(self, aAssignedEffectivity: StepBasic_Effectivity | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedEffectivity(self) -> StepBasic_Effectivity:
        """Returns field AssignedEffectivity"""

    def SetAssignedEffectivity(self, AssignedEffectivity: StepBasic_Effectivity | None) -> None:
        """Set field AssignedEffectivity"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_EulerAngles(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity EulerAngles"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_EulerAngles) -> None: ...

    def Init(self, aAngles: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Angles(self) -> nanoocp.NCollection.NCollection_HArray1[float]:
        """Returns field Angles"""

    def SetAngles(self, Angles: nanoocp.NCollection.NCollection_HArray1[float] | None) -> None:
        """Set field Angles"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_IdentificationAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity IdentificationAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_IdentificationAssignment) -> None: ...

    def Init(self, aAssignedId: nanoocp.TCollection.TCollection_HAsciiString | None, aRole: StepBasic_IdentificationRole | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field AssignedId"""

    def SetAssignedId(self, AssignedId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field AssignedId"""

    def Role(self) -> StepBasic_IdentificationRole:
        """Returns field Role"""

    def SetRole(self, Role: StepBasic_IdentificationRole | None) -> None:
        """Set field Role"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ExternalIdentificationAssignment(StepBasic_IdentificationAssignment):
    """Representation of STEP entity ExternalIdentificationAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ExternalIdentificationAssignment) -> None: ...

    def Init(self, aIdentificationAssignment_AssignedId: nanoocp.TCollection.TCollection_HAsciiString | None, aIdentificationAssignment_Role: StepBasic_IdentificationRole | None, aSource: StepBasic_ExternalSource | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Source(self) -> StepBasic_ExternalSource:
        """Returns field Source"""

    def SetSource(self, Source: StepBasic_ExternalSource | None) -> None:
        """Set field Source"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SourceItem(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type SourceItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_SourceItem) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of SourceItem select type
        1 -> HAsciiString from TCollection
        0 else
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember: ...

    def Identifier(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns Value as Identifier (or Null if another type)"""

class StepBasic_ExternallyDefinedItem(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ExternallyDefinedItem"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ExternallyDefinedItem) -> None: ...

    def Init(self, aItemId: StepBasic_SourceItem, aSource: StepBasic_ExternalSource | None) -> None:
        """Initialize all fields (own and inherited)"""

    def ItemId(self) -> StepBasic_SourceItem:
        """Returns field ItemId"""

    def SetItemId(self, ItemId: StepBasic_SourceItem) -> None:
        """Set field ItemId"""

    def Source(self) -> StepBasic_ExternalSource:
        """Returns field Source"""

    def SetSource(self, Source: StepBasic_ExternalSource | None) -> None:
        """Set field Source"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ExternalSource(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ExternalSource"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ExternalSource) -> None: ...

    def Init(self, aSourceId: StepBasic_SourceItem) -> None:
        """Initialize all fields (own and inherited)"""

    def SourceId(self) -> StepBasic_SourceItem:
        """Returns field SourceId"""

    def SetSourceId(self, SourceId: StepBasic_SourceItem) -> None:
        """Set field SourceId"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_GeneralProperty(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GeneralProperty"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_GeneralProperty) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_GeneralPropertyAssociation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GeneralPropertyAssociation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_GeneralPropertyAssociation) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aGeneralProperty: StepBasic_GeneralProperty | None, aPropertyDefinition: nanoocp.StepRepr.StepRepr_PropertyDefinition | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def GeneralProperty(self) -> StepBasic_GeneralProperty:
        """Returns field GeneralProperty"""

    def SetGeneralProperty(self, GeneralProperty: StepBasic_GeneralProperty | None) -> None:
        """Set field GeneralProperty"""

    def PropertyDefinition(self) -> nanoocp.StepRepr.StepRepr_PropertyDefinition:
        """Returns field PropertyDefinition"""

    def SetPropertyDefinition(self, PropertyDefinition: nanoocp.StepRepr.StepRepr_PropertyDefinition | None) -> None:
        """Set field PropertyDefinition"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_GeneralPropertyRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GeneralPropertyRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_GeneralPropertyRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingGeneralProperty: StepBasic_GeneralProperty | None, aRelatedGeneralProperty: StepBasic_GeneralProperty | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def RelatingGeneralProperty(self) -> StepBasic_GeneralProperty:
        """Returns field RelatingGeneralProperty"""

    def SetRelatingGeneralProperty(self, RelatingGeneralProperty: StepBasic_GeneralProperty | None) -> None:
        """Set field RelatingGeneralProperty"""

    def RelatedGeneralProperty(self) -> StepBasic_GeneralProperty:
        """Returns field RelatedGeneralProperty"""

    def SetRelatedGeneralProperty(self, RelatedGeneralProperty: StepBasic_GeneralProperty | None) -> None:
        """Set field RelatedGeneralProperty"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Group(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Group"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_Group) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_GroupAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GroupAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_GroupAssignment) -> None: ...

    def Init(self, aAssignedGroup: StepBasic_Group | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedGroup(self) -> StepBasic_Group:
        """Returns field AssignedGroup"""

    def SetAssignedGroup(self, AssignedGroup: StepBasic_Group | None) -> None:
        """Set field AssignedGroup"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_GroupRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity GroupRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_GroupRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingGroup: StepBasic_Group | None, aRelatedGroup: StepBasic_Group | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def RelatingGroup(self) -> StepBasic_Group:
        """Returns field RelatingGroup"""

    def SetRelatingGroup(self, RelatingGroup: StepBasic_Group | None) -> None:
        """Set field RelatingGroup"""

    def RelatedGroup(self) -> StepBasic_Group:
        """Returns field RelatedGroup"""

    def SetRelatedGroup(self, RelatedGroup: StepBasic_Group | None) -> None:
        """Set field RelatedGroup"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_IdentificationRole(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity IdentificationRole"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_IdentificationRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Unit(nanoocp.StepData.StepData_SelectType):
    """Implements a select type unit (NamedUnit or DerivedUnit)"""

    @overload
    def __init__(self) -> None:
        """Creates empty object"""

    @overload
    def __init__(self, theOther: StepBasic_Unit) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a type of Unit Entity
        1 -> NamedUnit
        2 -> DerivedUnit
        """

    def NamedUnit(self) -> StepBasic_NamedUnit:
        """returns Value as a NamedUnit (Null if another type)"""

    def DerivedUnit(self) -> StepBasic_DerivedUnit:
        """returns Value as a DerivedUnit (Null if another type)"""

class StepBasic_MeasureWithUnit(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a MeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_MeasureWithUnit) -> None: ...

    def Init(self, aValueComponent: StepBasic_MeasureValueMember | None, aUnitComponent: StepBasic_Unit) -> None: ...

    def SetValueComponent(self, aValueComponent: float) -> None: ...

    def ValueComponent(self) -> float: ...

    def ValueComponentMember(self) -> StepBasic_MeasureValueMember: ...

    def SetValueComponentMember(self, val: StepBasic_MeasureValueMember | None) -> None: ...

    def SetUnitComponent(self, aUnitComponent: StepBasic_Unit) -> None: ...

    def UnitComponent(self) -> StepBasic_Unit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_LengthMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a LengthMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_LengthMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_LengthUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a LengthUnit"""

    @overload
    def __init__(self, theOther: StepBasic_LengthUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_LocalTime(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a LocalTime"""

    @overload
    def __init__(self, theOther: StepBasic_LocalTime) -> None: ...

    def Init(self, aHourComponent: int, hasAminuteComponent: bool, aMinuteComponent: int, hasAsecondComponent: bool, aSecondComponent: float, aZone: StepBasic_CoordinatedUniversalTimeOffset | None) -> None: ...

    def SetHourComponent(self, aHourComponent: int) -> None: ...

    def HourComponent(self) -> int: ...

    def SetMinuteComponent(self, aMinuteComponent: int) -> None: ...

    def UnSetMinuteComponent(self) -> None: ...

    def MinuteComponent(self) -> int: ...

    def HasMinuteComponent(self) -> bool: ...

    def SetSecondComponent(self, aSecondComponent: float) -> None: ...

    def UnSetSecondComponent(self) -> None: ...

    def SecondComponent(self) -> float: ...

    def HasSecondComponent(self) -> bool: ...

    def SetZone(self, aZone: StepBasic_CoordinatedUniversalTimeOffset | None) -> None: ...

    def Zone(self) -> StepBasic_CoordinatedUniversalTimeOffset: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_MassMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a MassMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_MassMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_MassUnit(StepBasic_NamedUnit):
    """Representation of STEP entity MassUnit"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_MassUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_MeasureValueMember(nanoocp.StepData.StepData_SelectReal):
    """
    for Select MeasureValue, i.e. :
    length_measure,time_measure,plane_angle_measure,
    solid_angle_measure,ratio_measure,parameter_value,
    context_dependent_measure,positive_length_measure,
    positive_plane_angle_measure,positive_ratio_measure,
    area_measure,volume_measure, count_measure
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_MeasureValueMember) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, name: str) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductContext(StepBasic_ApplicationContextElement):
    @overload
    def __init__(self) -> None:
        """Returns a ProductContext"""

    @overload
    def __init__(self, theOther: StepBasic_ProductContext) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aFrameOfReference: StepBasic_ApplicationContext | None, aDisciplineType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetDisciplineType(self, aDisciplineType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def DisciplineType(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_MechanicalContext(StepBasic_ProductContext):
    @overload
    def __init__(self) -> None:
        """Returns a MechanicalContext"""

    @overload
    def __init__(self, theOther: StepBasic_MechanicalContext) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_NameAssignment(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity NameAssignment"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_NameAssignment) -> None: ...

    def Init(self, aAssignedName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def AssignedName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field AssignedName"""

    def SetAssignedName(self, AssignedName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field AssignedName"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ObjectRole(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ObjectRole"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ObjectRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_OrdinalDate(StepBasic_Date):
    @overload
    def __init__(self) -> None:
        """Returns a OrdinalDate"""

    @overload
    def __init__(self, theOther: StepBasic_OrdinalDate) -> None: ...

    def Init(self, aYearComponent: int, aDayComponent: int) -> None: ...

    def SetDayComponent(self, aDayComponent: int) -> None: ...

    def DayComponent(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Organization(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Organization"""

    @overload
    def __init__(self, theOther: StepBasic_Organization) -> None: ...

    def Init(self, hasAid: bool, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetId(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetId(self) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasId(self) -> bool: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_OrganizationalAddress(StepBasic_Address):
    @overload
    def __init__(self) -> None:
        """Returns a OrganizationalAddress"""

    @overload
    def __init__(self, theOther: StepBasic_OrganizationalAddress) -> None: ...

    def Init(self, hasAinternalLocation: bool, aInternalLocation: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreetNumber: bool, aStreetNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreet: bool, aStreet: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalBox: bool, aPostalBox: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtown: bool, aTown: nanoocp.TCollection.TCollection_HAsciiString | None, hasAregion: bool, aRegion: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalCode: bool, aPostalCode: nanoocp.TCollection.TCollection_HAsciiString | None, hasAcountry: bool, aCountry: nanoocp.TCollection.TCollection_HAsciiString | None, hasAfacsimileNumber: bool, aFacsimileNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelephoneNumber: bool, aTelephoneNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAelectronicMailAddress: bool, aElectronicMailAddress: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelexNumber: bool, aTelexNumber: nanoocp.TCollection.TCollection_HAsciiString | None, aOrganizations: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Organization] | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetOrganizations(self, aOrganizations: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Organization] | None) -> None: ...

    def Organizations(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Organization]: ...

    def OrganizationsValue(self, num: int) -> StepBasic_Organization: ...

    def NbOrganizations(self) -> int: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_OrganizationAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_OrganizationAssignment) -> None: ...

    def Init(self, aAssignedOrganization: StepBasic_Organization | None, aRole: StepBasic_OrganizationRole | None) -> None: ...

    def SetAssignedOrganization(self, aAssignedOrganization: StepBasic_Organization | None) -> None: ...

    def AssignedOrganization(self) -> StepBasic_Organization: ...

    def SetRole(self, aRole: StepBasic_OrganizationRole | None) -> None: ...

    def Role(self) -> StepBasic_OrganizationRole: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_OrganizationRole(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a OrganizationRole"""

    @overload
    def __init__(self, theOther: StepBasic_OrganizationRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Person(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Person"""

    @overload
    def __init__(self, theOther: StepBasic_Person) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, hasAlastName: bool, aLastName: nanoocp.TCollection.TCollection_HAsciiString | None, hasAfirstName: bool, aFirstName: nanoocp.TCollection.TCollection_HAsciiString | None, hasAmiddleNames: bool, aMiddleNames: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, hasAprefixTitles: bool, aPrefixTitles: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None, hasAsuffixTitles: bool, aSuffixTitles: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def SetId(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetLastName(self, aLastName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetLastName(self) -> None: ...

    def LastName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasLastName(self) -> bool: ...

    def SetFirstName(self, aFirstName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetFirstName(self) -> None: ...

    def FirstName(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasFirstName(self) -> bool: ...

    def SetMiddleNames(self, aMiddleNames: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def UnSetMiddleNames(self) -> None: ...

    def MiddleNames(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def HasMiddleNames(self) -> bool: ...

    def MiddleNamesValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def NbMiddleNames(self) -> int: ...

    def SetPrefixTitles(self, aPrefixTitles: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def UnSetPrefixTitles(self) -> None: ...

    def PrefixTitles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def HasPrefixTitles(self) -> bool: ...

    def PrefixTitlesValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def NbPrefixTitles(self) -> int: ...

    def SetSuffixTitles(self, aSuffixTitles: nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString] | None) -> None: ...

    def UnSetSuffixTitles(self) -> None: ...

    def SuffixTitles(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.TCollection.TCollection_HAsciiString]: ...

    def HasSuffixTitles(self) -> bool: ...

    def SuffixTitlesValue(self, num: int) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def NbSuffixTitles(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PersonalAddress(StepBasic_Address):
    @overload
    def __init__(self) -> None:
        """Returns a PersonalAddress"""

    @overload
    def __init__(self, theOther: StepBasic_PersonalAddress) -> None: ...

    def Init(self, hasAinternalLocation: bool, aInternalLocation: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreetNumber: bool, aStreetNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAstreet: bool, aStreet: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalBox: bool, aPostalBox: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtown: bool, aTown: nanoocp.TCollection.TCollection_HAsciiString | None, hasAregion: bool, aRegion: nanoocp.TCollection.TCollection_HAsciiString | None, hasApostalCode: bool, aPostalCode: nanoocp.TCollection.TCollection_HAsciiString | None, hasAcountry: bool, aCountry: nanoocp.TCollection.TCollection_HAsciiString | None, hasAfacsimileNumber: bool, aFacsimileNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelephoneNumber: bool, aTelephoneNumber: nanoocp.TCollection.TCollection_HAsciiString | None, hasAelectronicMailAddress: bool, aElectronicMailAddress: nanoocp.TCollection.TCollection_HAsciiString | None, hasAtelexNumber: bool, aTelexNumber: nanoocp.TCollection.TCollection_HAsciiString | None, aPeople: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Person] | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetPeople(self, aPeople: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Person] | None) -> None: ...

    def People(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Person]: ...

    def PeopleValue(self, num: int) -> StepBasic_Person: ...

    def NbPeople(self) -> int: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PersonAndOrganization(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PersonAndOrganization"""

    @overload
    def __init__(self, theOther: StepBasic_PersonAndOrganization) -> None: ...

    def Init(self, aThePerson: StepBasic_Person | None, aTheOrganization: StepBasic_Organization | None) -> None: ...

    def SetThePerson(self, aThePerson: StepBasic_Person | None) -> None: ...

    def ThePerson(self) -> StepBasic_Person: ...

    def SetTheOrganization(self, aTheOrganization: StepBasic_Organization | None) -> None: ...

    def TheOrganization(self) -> StepBasic_Organization: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PersonAndOrganizationAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_PersonAndOrganizationAssignment) -> None: ...

    def Init(self, aAssignedPersonAndOrganization: StepBasic_PersonAndOrganization | None, aRole: StepBasic_PersonAndOrganizationRole | None) -> None: ...

    def SetAssignedPersonAndOrganization(self, aAssignedPersonAndOrganization: StepBasic_PersonAndOrganization | None) -> None: ...

    def AssignedPersonAndOrganization(self) -> StepBasic_PersonAndOrganization: ...

    def SetRole(self, aRole: StepBasic_PersonAndOrganizationRole | None) -> None: ...

    def Role(self) -> StepBasic_PersonAndOrganizationRole: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PersonAndOrganizationRole(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a PersonAndOrganizationRole"""

    @overload
    def __init__(self, theOther: StepBasic_PersonAndOrganizationRole) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinition(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinition"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinition) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aFormation: StepBasic_ProductDefinitionFormation | None, aFrameOfReference: StepBasic_ProductDefinitionContext | None) -> None: ...

    def SetId(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFormation(self, aFormation: StepBasic_ProductDefinitionFormation | None) -> None: ...

    def Formation(self) -> StepBasic_ProductDefinitionFormation: ...

    def SetFrameOfReference(self, aFrameOfReference: StepBasic_ProductDefinitionContext | None) -> None: ...

    def FrameOfReference(self) -> StepBasic_ProductDefinitionContext: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PhysicallyModeledProductDefinition(StepBasic_ProductDefinition):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_PhysicallyModeledProductDefinition) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PlaneAngleMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a PlaneAngleMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_PlaneAngleMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_PlaneAngleUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a PlaneAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_PlaneAngleUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_Product(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a Product"""

    @overload
    def __init__(self, theOther: StepBasic_Product) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aFrameOfReference: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_ProductContext] | None) -> None: ...

    def SetId(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetFrameOfReference(self, aFrameOfReference: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_ProductContext] | None) -> None: ...

    def FrameOfReference(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_ProductContext]: ...

    def FrameOfReferenceValue(self, num: int) -> StepBasic_ProductContext: ...

    def NbFrameOfReference(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductCategory(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ProductCategory"""

    @overload
    def __init__(self, theOther: StepBasic_ProductCategory) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasAdescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def UnSetDescription(self) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def HasDescription(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductCategoryRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ProductCategoryRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductCategoryRelationship) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aCategory: StepBasic_ProductCategory | None, aSubCategory: StepBasic_ProductCategory | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def Category(self) -> StepBasic_ProductCategory:
        """Returns field Category"""

    def SetCategory(self, Category: StepBasic_ProductCategory | None) -> None:
        """Set field Category"""

    def SubCategory(self) -> StepBasic_ProductCategory:
        """Returns field SubCategory"""

    def SetSubCategory(self, SubCategory: StepBasic_ProductCategory | None) -> None:
        """Set field SubCategory"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductConceptContext(StepBasic_ApplicationContextElement):
    """Representation of STEP entity ProductConceptContext"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductConceptContext) -> None: ...

    def Init(self, aApplicationContextElement_Name: nanoocp.TCollection.TCollection_HAsciiString | None, aApplicationContextElement_FrameOfReference: StepBasic_ApplicationContext | None, aMarketSegmentType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def MarketSegmentType(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field MarketSegmentType"""

    def SetMarketSegmentType(self, MarketSegmentType: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field MarketSegmentType"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionEffectivity(StepBasic_Effectivity):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionEffectivity) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aUsage: StepBasic_ProductDefinitionRelationship | None) -> None: ...

    def Usage(self) -> StepBasic_ProductDefinitionRelationship: ...

    def SetUsage(self, aUsage: StepBasic_ProductDefinitionRelationship | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionFormation(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinitionFormation"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionFormation) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aOfProduct: StepBasic_Product | None) -> None: ...

    def SetId(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetOfProduct(self, aOfProduct: StepBasic_Product | None) -> None: ...

    def OfProduct(self) -> StepBasic_Product: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionFormationRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ProductDefinitionFormationRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionFormationRelationship) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingProductDefinitionFormation: StepBasic_ProductDefinitionFormation | None, aRelatedProductDefinitionFormation: StepBasic_ProductDefinitionFormation | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def RelatingProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation:
        """Returns field RelatingProductDefinitionFormation"""

    def SetRelatingProductDefinitionFormation(self, RelatingProductDefinitionFormation: StepBasic_ProductDefinitionFormation | None) -> None:
        """Set field RelatingProductDefinitionFormation"""

    def RelatedProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation:
        """Returns field RelatedProductDefinitionFormation"""

    def SetRelatedProductDefinitionFormation(self, RelatedProductDefinitionFormation: StepBasic_ProductDefinitionFormation | None) -> None:
        """Set field RelatedProductDefinitionFormation"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionFormationWithSpecifiedSource(StepBasic_ProductDefinitionFormation):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinitionFormationWithSpecifiedSource"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionFormationWithSpecifiedSource) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aOfProduct: StepBasic_Product | None, aMakeOrBuy: StepBasic_Source) -> None: ...

    def SetMakeOrBuy(self, aMakeOrBuy: StepBasic_Source) -> None: ...

    def MakeOrBuy(self) -> StepBasic_Source: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionOrReference(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinitionOrReference SelectType"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionOrReference) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a ProductDefinitionOrReference Kind Entity that is :
        1 -> ProductDefinition
        2 -> ProductDefinitionReference
        3 -> ProductDefinitionReferenceWithLocalPresentation
        0 else
        """

    def ProductDefinition(self) -> StepBasic_ProductDefinition:
        """returns Value as a ProductDefinition (Null if another type)"""

    def ProductDefinitionReference(self) -> StepBasic_ProductDefinitionReference:
        """returns Value as a ProductDefinitionReference (Null if another type)"""

    def ProductDefinitionReferenceWithLocalRepresentation(self) -> StepBasic_ProductDefinitionReferenceWithLocalRepresentation:
        """
        returns Value as a ProductDefinitionReferenceWithLocalRepresentation (Null if another type)
        """

class StepBasic_ProductDefinitionReference(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity Product_Definition_Reference"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionReference) -> None: ...

    @overload
    def Init(self, theSource: StepBasic_ExternalSource | None, theProductId: nanoocp.TCollection.TCollection_HAsciiString | None, theProductDefinitionFormationId: nanoocp.TCollection.TCollection_HAsciiString | None, theProductDefinitionId: nanoocp.TCollection.TCollection_HAsciiString | None, theIdOwningOrganizationName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    @overload
    def Init(self, theSource: StepBasic_ExternalSource | None, theProductId: nanoocp.TCollection.TCollection_HAsciiString | None, theProductDefinitionFormationId: nanoocp.TCollection.TCollection_HAsciiString | None, theProductDefinitionId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Source(self) -> StepBasic_ExternalSource:
        """Returns field Source"""

    def SetSource(self, theSource: StepBasic_ExternalSource | None) -> None:
        """Set field Source"""

    def ProductId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field ProductId"""

    def SetProductId(self, theProductId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field ProductId"""

    def ProductDefinitionFormationId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field ProductDefinitionFormationId"""

    def SetProductDefinitionFormationId(self, theProductDefinitionFormationId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field ProductDefinitionFormationId"""

    def ProductDefinitionId(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field ProductDefinitionId"""

    def SetProductDefinitionId(self, theProductDefinitionId: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field ProductDefinitionId"""

    def IdOwningOrganizationName(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field IdOwningOrganizationName"""

    def SetIdOwningOrganizationName(self, theIdOwningOrganizationName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field IdOwningOrganizationName"""

    def HasIdOwningOrganizationName(self) -> bool:
        """Returns true if IdOwningOrganizationName exists"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionReferenceWithLocalRepresentation(StepBasic_ProductDefinition):
    @overload
    def __init__(self) -> None:
        """Returns a ProductDefinitionReferenceWithLocalRepresentation"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionReferenceWithLocalRepresentation) -> None: ...

    def Init(self, theSource: StepBasic_ExternalSource | None, theId: nanoocp.TCollection.TCollection_HAsciiString | None, theDescription: nanoocp.TCollection.TCollection_HAsciiString | None, theFormation: StepBasic_ProductDefinitionFormation | None, theFrameOfReference: StepBasic_ProductDefinitionContext | None) -> None: ...

    def Source(self) -> StepBasic_ExternalSource:
        """Returns field Source"""

    def SetSource(self, theSource: StepBasic_ExternalSource | None) -> None:
        """Set field Source"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionRelationship(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity ProductDefinitionRelationship"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionRelationship) -> None: ...

    @overload
    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingProductDefinition: StepBasic_ProductDefinition | None, aRelatedProductDefinition: StepBasic_ProductDefinition | None) -> None: ...

    @overload
    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aRelatingProductDefinition: StepBasic_ProductDefinitionOrReference, aRelatedProductDefinition: StepBasic_ProductDefinitionOrReference) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Name"""

    def SetName(self, Name: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Name"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    def RelatingProductDefinition(self) -> StepBasic_ProductDefinition:
        """Returns field RelatingProductDefinition"""

    def RelatingProductDefinitionAP242(self) -> StepBasic_ProductDefinitionOrReference:
        """Returns field RelatingProductDefinition in AP242"""

    @overload
    def SetRelatingProductDefinition(self, RelatingProductDefinition: StepBasic_ProductDefinition | None) -> None:
        """Set field RelatingProductDefinition"""

    @overload
    def SetRelatingProductDefinition(self, RelatingProductDefinition: StepBasic_ProductDefinitionOrReference) -> None:
        """Set field RelatingProductDefinition in AP242"""

    def RelatedProductDefinition(self) -> StepBasic_ProductDefinition:
        """Returns field RelatedProductDefinition"""

    def RelatedProductDefinitionAP242(self) -> StepBasic_ProductDefinitionOrReference:
        """Returns field RelatedProductDefinition in AP242"""

    @overload
    def SetRelatedProductDefinition(self, RelatedProductDefinition: StepBasic_ProductDefinition | None) -> None:
        """Set field RelatedProductDefinition"""

    @overload
    def SetRelatedProductDefinition(self, RelatedProductDefinition: StepBasic_ProductDefinitionOrReference) -> None:
        """Set field RelatedProductDefinition in AP242"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductDefinitionWithAssociatedDocuments(StepBasic_ProductDefinition):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_ProductDefinitionWithAssociatedDocuments) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aFormation: StepBasic_ProductDefinitionFormation | None, aFrame: StepBasic_ProductDefinitionContext | None, aDocIds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Document] | None) -> None: ...

    def DocIds(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Document]: ...

    def SetDocIds(self, DocIds: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Document] | None) -> None: ...

    def NbDocIds(self) -> int: ...

    def DocIdsValue(self, num: int) -> StepBasic_Document: ...

    def SetDocIdsValue(self, num: int, adoc: StepBasic_Document | None) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductRelatedProductCategory(StepBasic_ProductCategory):
    @overload
    def __init__(self) -> None:
        """Returns a ProductRelatedProductCategory"""

    @overload
    def __init__(self, theOther: StepBasic_ProductRelatedProductCategory) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, hasAdescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None, aProducts: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Product] | None) -> None: ...

    def SetProducts(self, aProducts: nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Product] | None) -> None: ...

    def Products(self) -> nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Product]: ...

    def ProductsValue(self, num: int) -> StepBasic_Product: ...

    def NbProducts(self) -> int: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ProductType(StepBasic_ProductRelatedProductCategory):
    @overload
    def __init__(self) -> None:
        """Returns a ProductType"""

    @overload
    def __init__(self, theOther: StepBasic_ProductType) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_RatioMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a RatioMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_RatioMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_RatioUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a RatioUnit"""

    @overload
    def __init__(self, theOther: StepBasic_RatioUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_RoleSelect(nanoocp.StepData.StepData_SelectType):
    """Representation of STEP SELECT type RoleSelect"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_RoleSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a kind of RoleSelect select type
        1 -> ActionAssignment from StepBasic
        2 -> ActionRequestAssignment from StepBasic
        3 -> ApprovalAssignment from StepBasic
        4 -> ApprovalDateTime from StepBasic
        5 -> CertificationAssignment from StepBasic
        6 -> ContractAssignment from StepBasic
        7 -> DocumentReference from StepBasic
        8 -> EffectivityAssignment from StepBasic
        9 -> GroupAssignment from StepBasic
        10 -> NameAssignment from StepBasic
        11 -> SecurityClassificationAssignment from StepBasic
        0 else
        """

    def ActionAssignment(self) -> StepBasic_ActionAssignment:
        """Returns Value as ActionAssignment (or Null if another type)"""

    def ActionRequestAssignment(self) -> StepBasic_ActionRequestAssignment:
        """Returns Value as ActionRequestAssignment (or Null if another type)"""

    def ApprovalAssignment(self) -> StepBasic_ApprovalAssignment:
        """Returns Value as ApprovalAssignment (or Null if another type)"""

    def ApprovalDateTime(self) -> StepBasic_ApprovalDateTime:
        """Returns Value as ApprovalDateTime (or Null if another type)"""

    def CertificationAssignment(self) -> StepBasic_CertificationAssignment:
        """Returns Value as CertificationAssignment (or Null if another type)"""

    def ContractAssignment(self) -> StepBasic_ContractAssignment:
        """Returns Value as ContractAssignment (or Null if another type)"""

    def DocumentReference(self) -> StepBasic_DocumentReference:
        """Returns Value as DocumentReference (or Null if another type)"""

    def EffectivityAssignment(self) -> StepBasic_EffectivityAssignment:
        """Returns Value as EffectivityAssignment (or Null if another type)"""

    def GroupAssignment(self) -> StepBasic_GroupAssignment:
        """Returns Value as GroupAssignment (or Null if another type)"""

    def NameAssignment(self) -> StepBasic_NameAssignment:
        """Returns Value as NameAssignment (or Null if another type)"""

    def SecurityClassificationAssignment(self) -> StepBasic_SecurityClassificationAssignment:
        """
        Returns Value as SecurityClassificationAssignment (or Null if another type)
        """

class StepBasic_RoleAssociation(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity RoleAssociation"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_RoleAssociation) -> None: ...

    def Init(self, aRole: StepBasic_ObjectRole | None, aItemWithRole: StepBasic_RoleSelect) -> None:
        """Initialize all fields (own and inherited)"""

    def Role(self) -> StepBasic_ObjectRole:
        """Returns field Role"""

    def SetRole(self, Role: StepBasic_ObjectRole | None) -> None:
        """Set field Role"""

    def ItemWithRole(self) -> StepBasic_RoleSelect:
        """Returns field ItemWithRole"""

    def SetItemWithRole(self, ItemWithRole: StepBasic_RoleSelect) -> None:
        """Set field ItemWithRole"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SecurityClassification(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SecurityClassification"""

    @overload
    def __init__(self, theOther: StepBasic_SecurityClassification) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None, aSecurityLevel: StepBasic_SecurityClassificationLevel | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetPurpose(self, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetSecurityLevel(self, aSecurityLevel: StepBasic_SecurityClassificationLevel | None) -> None: ...

    def SecurityLevel(self) -> StepBasic_SecurityClassificationLevel: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SecurityClassificationAssignment(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_SecurityClassificationAssignment) -> None: ...

    def Init(self, aAssignedSecurityClassification: StepBasic_SecurityClassification | None) -> None: ...

    def SetAssignedSecurityClassification(self, aAssignedSecurityClassification: StepBasic_SecurityClassification | None) -> None: ...

    def AssignedSecurityClassification(self) -> StepBasic_SecurityClassification: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SecurityClassificationLevel(nanoocp.Standard.Standard_Transient):
    @overload
    def __init__(self) -> None:
        """Returns a SecurityClassificationLevel"""

    @overload
    def __init__(self, theOther: StepBasic_SecurityClassificationLevel) -> None: ...

    def Init(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetPrefix(self, aPrefix: StepBasic_SiPrefix) -> None: ...

    def UnSetPrefix(self) -> None: ...

    def Prefix(self) -> StepBasic_SiPrefix: ...

    def HasPrefix(self) -> bool: ...

    def SetName(self, aName: StepBasic_SiUnitName) -> None: ...

    def Name(self) -> StepBasic_SiUnitName: ...

    def SetDimensions(self, aDimensions: StepBasic_DimensionalExponents | None) -> None: ...

    def Dimensions(self) -> StepBasic_DimensionalExponents: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndAreaUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndAreaUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndAreaUnit) -> None: ...

    def SetAreaUnit(self, anAreaUnit: StepBasic_AreaUnit | None) -> None: ...

    def AreaUnit(self) -> StepBasic_AreaUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndLengthUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndLengthUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndLengthUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetLengthUnit(self, aLengthUnit: StepBasic_LengthUnit | None) -> None: ...

    def LengthUnit(self) -> StepBasic_LengthUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndMassUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndMassUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndMassUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetMassUnit(self, aMassUnit: StepBasic_MassUnit | None) -> None: ...

    def MassUnit(self) -> StepBasic_MassUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndPlaneAngleUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndPlaneAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndPlaneAngleUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetPlaneAngleUnit(self, aPlaneAngleUnit: StepBasic_PlaneAngleUnit | None) -> None: ...

    def PlaneAngleUnit(self) -> StepBasic_PlaneAngleUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndRatioUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndRatioUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndRatioUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetRatioUnit(self, aRatioUnit: StepBasic_RatioUnit | None) -> None: ...

    def RatioUnit(self) -> StepBasic_RatioUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndSolidAngleUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndSolidAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndSolidAngleUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetSolidAngleUnit(self, aSolidAngleUnit: StepBasic_SolidAngleUnit | None) -> None: ...

    def SolidAngleUnit(self) -> StepBasic_SolidAngleUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndThermodynamicTemperatureUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndThermodynamicTemperatureUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndThermodynamicTemperatureUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetThermodynamicTemperatureUnit(self, aThermodynamicTemperatureUnit: StepBasic_ThermodynamicTemperatureUnit | None) -> None: ...

    def ThermodynamicTemperatureUnit(self) -> StepBasic_ThermodynamicTemperatureUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndTimeUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndTimeUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndTimeUnit) -> None: ...

    def Init(self, hasAprefix: bool, aPrefix: StepBasic_SiPrefix, aName: StepBasic_SiUnitName) -> None: ...

    def SetTimeUnit(self, aTimeUnit: StepBasic_TimeUnit | None) -> None: ...

    def TimeUnit(self) -> StepBasic_TimeUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SiUnitAndVolumeUnit(StepBasic_SiUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SiUnitAndVolumeUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SiUnitAndVolumeUnit) -> None: ...

    def SetVolumeUnit(self, aVolumeUnit: StepBasic_VolumeUnit | None) -> None: ...

    def VolumeUnit(self) -> StepBasic_VolumeUnit: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SizeMember(nanoocp.StepData.StepData_SelectReal):
    """
    For immediate members of SizeSelect, i.e. :
    ParameterValue (a Real)
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_SizeMember) -> None: ...

    def HasName(self) -> bool: ...

    def Name(self) -> str: ...

    def SetName(self, name: str) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SizeSelect(nanoocp.StepData.StepData_SelectType):
    @overload
    def __init__(self) -> None:
        """Returns a SizeSelect SelectType"""

    @overload
    def __init__(self, theOther: StepBasic_SizeSelect) -> None: ...

    def CaseNum(self, ent: nanoocp.Standard.Standard_Transient | None) -> int:
        """
        Recognizes a TrimmingSelect Kind Entity that is :
        1 -> SizeMember
        0 else (i.e. Real)
        """

    def NewMember(self) -> nanoocp.StepData.StepData_SelectMember:
        """Returns a SizeMember (POSITIVE_LENGTH_MEASURE) as preferred"""

    def CaseMem(self, ent: nanoocp.StepData.StepData_SelectMember | None) -> int:
        """
        Recognizes a SelectMember as Real, named as PARAMETER_VALUE
        1 -> PositiveLengthMeasure i.e. Real
        0 else (i.e. Entity)
        """

    def SetRealValue(self, aReal: float) -> None: ...

    def RealValue(self) -> float:
        """returns Value as a Real (Null if another type)"""

class StepBasic_SolidAngleMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SolidAngleMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SolidAngleMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_SolidAngleUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a SolidAngleUnit"""

    @overload
    def __init__(self, theOther: StepBasic_SolidAngleUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_ThermodynamicTemperatureUnit(StepBasic_NamedUnit):
    """Representation of STEP entity ThermodynamicTemperatureUnit"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_ThermodynamicTemperatureUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_TimeMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a TimeMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_TimeMeasureWithUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_TimeUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None:
        """Returns a TimeUnit"""

    @overload
    def __init__(self, theOther: StepBasic_TimeUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_UncertaintyMeasureWithUnit(StepBasic_MeasureWithUnit):
    @overload
    def __init__(self) -> None:
        """Returns a UncertaintyMeasureWithUnit"""

    @overload
    def __init__(self, theOther: StepBasic_UncertaintyMeasureWithUnit) -> None: ...

    def Init(self, aValueComponent: StepBasic_MeasureValueMember | None, aUnitComponent: StepBasic_Unit, aName: nanoocp.TCollection.TCollection_HAsciiString | None, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def SetName(self, aName: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    def SetDescription(self, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None: ...

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_VersionedActionRequest(nanoocp.Standard.Standard_Transient):
    """Representation of STEP entity VersionedActionRequest"""

    @overload
    def __init__(self) -> None:
        """Empty constructor"""

    @overload
    def __init__(self, theOther: StepBasic_VersionedActionRequest) -> None: ...

    def Init(self, aId: nanoocp.TCollection.TCollection_HAsciiString | None, aVersion: nanoocp.TCollection.TCollection_HAsciiString | None, aPurpose: nanoocp.TCollection.TCollection_HAsciiString | None, hasDescription: bool, aDescription: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Initialize all fields (own and inherited)"""

    def Id(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Id"""

    def SetId(self, Id: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Id"""

    def Version(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Version"""

    def SetVersion(self, Version: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Version"""

    def Purpose(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Purpose"""

    def SetPurpose(self, Purpose: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Purpose"""

    def Description(self) -> nanoocp.TCollection.TCollection_HAsciiString:
        """Returns field Description"""

    def SetDescription(self, Description: nanoocp.TCollection.TCollection_HAsciiString | None) -> None:
        """Set field Description"""

    def HasDescription(self) -> bool:
        """Returns True if optional field Description is defined"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_VolumeUnit(StepBasic_NamedUnit):
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: StepBasic_VolumeUnit) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class StepBasic_WeekOfYearAndDayDate(StepBasic_Date):
    @overload
    def __init__(self) -> None:
        """Returns a WeekOfYearAndDayDate"""

    @overload
    def __init__(self, theOther: StepBasic_WeekOfYearAndDayDate) -> None: ...

    def Init(self, aYearComponent: int, aWeekComponent: int, hasAdayComponent: bool, aDayComponent: int) -> None: ...

    def SetWeekComponent(self, aWeekComponent: int) -> None: ...

    def WeekComponent(self) -> int: ...

    def SetDayComponent(self, aDayComponent: int) -> None: ...

    def UnSetDayComponent(self) -> None: ...

    def DayComponent(self) -> int: ...

    def HasDayComponent(self) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.StepBasic
StepBasic_Array1OfApproval = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_Approval]
StepBasic_Array1OfDerivedUnitElement = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_DerivedUnitElement]
StepBasic_Array1OfDocument = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_Document]
StepBasic_Array1OfNamedUnit = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_NamedUnit]
StepBasic_Array1OfOrganization = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_Organization]
StepBasic_Array1OfPerson = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_Person]
StepBasic_Array1OfProduct = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_Product]
StepBasic_Array1OfProductContext = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_ProductContext]
StepBasic_Array1OfUncertaintyMeasureWithUnit = nanoocp.NCollection.NCollection_Array1[nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit]
StepBasic_HArray1OfApproval = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Approval]
StepBasic_HArray1OfDerivedUnitElement = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_DerivedUnitElement]
StepBasic_HArray1OfDocument = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Document]
StepBasic_HArray1OfNamedUnit = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_NamedUnit]
StepBasic_HArray1OfOrganization = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Organization]
StepBasic_HArray1OfPerson = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Person]
StepBasic_HArray1OfProduct = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_Product]
StepBasic_HArray1OfProductContext = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_ProductContext]
StepBasic_HArray1OfUncertaintyMeasureWithUnit = nanoocp.NCollection.NCollection_HArray1[nanoocp.StepBasic.StepBasic_UncertaintyMeasureWithUnit]
