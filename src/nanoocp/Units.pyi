"""OCCT package Units (toolkit TKernel)"""

from typing import overload

import nanoocp.NCollection
import nanoocp.Standard
import nanoocp.TCollection


class Units:
    """
    This package provides all the facilities to create
    and question a dictionary of units, and also to
    manipulate measurements which are real values with
    units.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: Units) -> None: ...

    @staticmethod
    def UnitsFile(afile: str) -> None:
        """
        Defines the location of the file containing all the
        information useful in creating the dictionary of all
        the units known to the system.
        """

    @staticmethod
    def LexiconFile(afile: str) -> None:
        """
        Defines the location of the file containing the lexicon
        useful in manipulating composite units.
        """

    @staticmethod
    def DictionaryOfUnits(amode: bool = False) -> Units_UnitsDictionary:
        """
        Returns a unique instance of the dictionary of units.
        If <amode> is True, then it forces the recomputation of
        the dictionary of units.
        """

    @staticmethod
    def Quantity(aquantity: str) -> Units_Quantity:
        """Returns a unique quantity instance corresponding to <aquantity>."""

    @staticmethod
    def FirstQuantity(aunit: str) -> str:
        """Returns the first quantity string founded from the unit <aUnit>."""

    @staticmethod
    def LexiconUnits(amode: bool = True) -> Units_Lexicon:
        """
        Returns a unique instance of the Units_Lexicon.
        If <amode> is True, it forces the recomputation of
        the dictionary of units, and by consequence the
        completion of the Units_Lexicon.
        """

    @staticmethod
    def LexiconFormula() -> Units_Lexicon:
        """Return a unique instance of LexiconFormula."""

    @staticmethod
    def NullDimensions() -> Units_Dimensions:
        """Returns always the same instance of Dimensions."""

    @staticmethod
    def Convert(avalue: float, afirstunit: str, asecondunit: str) -> float:
        """Converts <avalue> expressed in <afirstunit> into the <asecondunit>."""

    @staticmethod
    def ToSI(aData: float, aUnit: str) -> float: ...

    @staticmethod
    def ToSI__Units_Dimensions(aData: float, aUnit: str) -> tuple[float, Units_Dimensions]:
        """
        ToSI__Units_Dimensions: the C++ overload ToSI(const double, const char *const, occ::handle<Units_Dimensions> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @staticmethod
    def FromSI(aData: float, aUnit: str) -> float: ...

    @staticmethod
    def FromSI__Units_Dimensions(aData: float, aUnit: str) -> tuple[float, Units_Dimensions]:
        """
        FromSI__Units_Dimensions: the C++ overload FromSI(const double, const char *const, occ::handle<Units_Dimensions> &); the suffix lists its returned out-parameters (nanoOCP R-COLLISION).
        """

    @staticmethod
    def Dimensions(aType: str) -> Units_Dimensions:
        """return the dimension associated to the Type"""

class Units_Dimensions(nanoocp.Standard.Standard_Transient):
    """
    This class includes all the methods to create and
    manipulate the dimensions of the physical
    quantities.
    """

    @overload
    def __init__(self, amass: float, alength: float, atime: float, anelectriccurrent: float, athermodynamictemperature: float, anamountofsubstance: float, aluminousintensity: float, aplaneangle: float, asolidangle: float) -> None:
        """
        Returns a Dimensions object which represents the
        dimension of a physical quantity. Each of the
        <amass>, <alength>, <atime>, <anelectriccurrent>,
        <athermodynamictemperature>, <anamountofsubstance>,
        <aluminousintensity>, <aplaneangle>, <asolidangle> are
        the powers for the 7 fundamental units of physical
        quantity and the 2 secondary fundamental units of
        physical quantity.
        """

    @overload
    def __init__(self, theOther: Units_Dimensions) -> None: ...

    def Mass(self) -> float:
        """Returns the power of mass stored in the dimensions."""

    def Length(self) -> float:
        """Returns the power of length stored in the dimensions."""

    def Time(self) -> float:
        """Returns the power of time stored in the dimensions."""

    def ElectricCurrent(self) -> float:
        """
        Returns the power of electrical intensity (current)
        stored in the dimensions.
        """

    def ThermodynamicTemperature(self) -> float:
        """
        Returns the power of temperature stored in the
        dimensions.
        """

    def AmountOfSubstance(self) -> float:
        """
        Returns the power of quantity of material (mole)
        stored in the dimensions.
        """

    def LuminousIntensity(self) -> float:
        """
        Returns the power of light intensity stored in the
        dimensions.
        """

    def PlaneAngle(self) -> float:
        """
        Returns the power of plane angle stored in the
        dimensions.
        """

    def SolidAngle(self) -> float:
        """
        Returns the power of solid angle stored in the
        dimensions.
        """

    def Quantity(self) -> str:
        """Returns the quantity string of the dimension"""

    def Multiply(self, adimensions: Units_Dimensions | None) -> Units_Dimensions:
        """
        Creates and returns a new Dimensions object which is
        the result of the multiplication of <me> and
        <adimensions>.
        """

    def Divide(self, adimensions: Units_Dimensions | None) -> Units_Dimensions:
        """
        Creates and returns a new Dimensions object which is
        the result of the division of <me> by <adimensions>.
        """

    def Power(self, anexponent: float) -> Units_Dimensions:
        """
        Creates and returns a new Dimensions object which is
        the result of the power of <me> and <anexponent>.
        """

    def IsEqual(self, adimensions: Units_Dimensions | None) -> bool:
        """
        Returns true if <me> and <adimensions> have the same
        dimensions, false otherwise.
        """

    def IsNotEqual(self, adimensions: Units_Dimensions | None) -> bool:
        """
        Returns false if <me> and <adimensions> have the same
        dimensions, true otherwise.
        """

    def Dump(self, ashift: int) -> None:
        """Useful for degugging."""

    @staticmethod
    def ALess() -> Units_Dimensions: ...

    @staticmethod
    def AMass() -> Units_Dimensions: ...

    @staticmethod
    def ALength() -> Units_Dimensions: ...

    @staticmethod
    def ATime() -> Units_Dimensions: ...

    @staticmethod
    def AElectricCurrent() -> Units_Dimensions: ...

    @staticmethod
    def AThermodynamicTemperature() -> Units_Dimensions: ...

    @staticmethod
    def AAmountOfSubstance() -> Units_Dimensions: ...

    @staticmethod
    def ALuminousIntensity() -> Units_Dimensions: ...

    @staticmethod
    def APlaneAngle() -> Units_Dimensions: ...

    @staticmethod
    def ASolidAngle() -> Units_Dimensions:
        """Returns the basic dimensions."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_Unit(nanoocp.Standard.Standard_Transient):
    """
    This class defines an elementary word contained in
    a physical quantity.
    """

    @overload
    def __init__(self, aname: str) -> None:
        """
        Creates and returns a unit. <aname> is the name of
        the unit.
        """

    @overload
    def __init__(self, aname: str, asymbol: str) -> None:
        """
        Creates and returns a unit. <aname> is the name of
        the unit, <asymbol> is the usual abbreviation of the
        unit.
        """

    @overload
    def __init__(self, aname: str, asymbol: str, avalue: float, aquantity: Units_Quantity | None) -> None:
        """
        Creates and returns a unit. <aname> is the name of
        the unit, <asymbol> is the usual abbreviation of the
        unit, and <avalue> is the value in relation to the
        International System of Units.
        """

    @overload
    def __init__(self, theOther: Units_Unit) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the unit <thename>"""

    def Symbol(self, asymbol: str) -> None:
        """Adds a new symbol <asymbol> attached to <me>."""

    @overload
    def Value(self) -> float:
        """
        Returns the value in relation with the International
        System of Units.
        """

    @overload
    def Value(self, avalue: float) -> None:
        """Sets the value <avalue> to <me>."""

    @overload
    def Quantity(self) -> Units_Quantity:
        """Returns <thequantity> contained in <me>."""

    @overload
    def Quantity(self, aquantity: Units_Quantity | None) -> None:
        """Sets the physical Quantity <aquantity> to <me>."""

    def SymbolsSequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.TCollection.TCollection_HAsciiString]:
        """Returns the sequence of symbols <thesymbolssequence>"""

    def Token(self) -> Units_Token:
        """Starting with <me>, returns a new Token object."""

    def IsEqual(self, astring: str) -> bool:
        """
        Compares all the symbols linked within <me> with the
        name of <atoken>, and returns True if there is one
        symbol equal to the name, False otherwise.
        """

    def Dump(self, ashift: int, alevel: int) -> None:
        """Useful for debugging"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_Quantity(nanoocp.Standard.Standard_Transient):
    """
    This class stores in its field all the possible
    units of all the unit systems for a given physical
    quantity. Each unit's value is expressed in the
    S.I. unit system.
    """

    @overload
    def __init__(self, aname: str, adimensions: Units_Dimensions | None, aunitssequence: nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Unit] | None) -> None:
        """
        Creates a new Quantity object with <aname> which is
        the name of the physical quantity, <adimensions> which
        is the physical dimensions, and <aunitssequence> which
        describes all the units known for this quantity.
        """

    @overload
    def __init__(self, theOther: Units_Quantity) -> None: ...

    def Name(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns in a AsciiString from TCollection the name of the quantity."""

    def Dimensions(self) -> Units_Dimensions:
        """Returns the physical dimensions of the quantity."""

    def Sequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Unit]:
        """
        Returns <theunitssequence>, which is the sequence of
        all the units stored for this physical quantity.
        """

    def IsEqual(self, astring: str) -> bool:
        """
        Returns True if the name of the Quantity <me> is equal
        to <astring>, False otherwise.
        """

    def Dump(self, ashift: int, alevel: int) -> None:
        """Useful for debugging."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_Explorer:
    """
    This class provides all the services to explore
    UnitsSystem or UnitsDictionary.
    """

    @overload
    def __init__(self) -> None:
        """Empty constructor of the class."""

    @overload
    def __init__(self, aunitssystem: Units_UnitsSystem | None) -> None:
        """
        Creates a new instance of the class, initialized with
        the UnitsSystem <aunitssystem>.
        """

    @overload
    def __init__(self, aunitsdictionary: Units_UnitsDictionary | None) -> None:
        """
        Creates a new instance of the class, initialized with
        the UnitsDictionary <aunitsdictionary>.
        """

    @overload
    def __init__(self, aunitssystem: Units_UnitsSystem | None, aquantity: str) -> None:
        """
        Creates a new instance of the class, initialized with
        the UnitsSystem <aunitssystem> and positioned at the
        quantity <aquantity>.
        """

    @overload
    def __init__(self, aunitsdictionary: Units_UnitsDictionary | None, aquantity: str) -> None:
        """
        Creates a new instance of the class, initialized with
        the UnitsDictionary <aunitsdictionary> and positioned
        at the quantity <aquantity>.
        """

    @overload
    def __init__(self, theOther: Units_Explorer) -> None: ...

    @overload
    def Init(self, aunitssystem: Units_UnitsSystem | None) -> None:
        """
        Initializes the instance of the class with the
        UnitsSystem <aunitssystem>.
        """

    @overload
    def Init(self, aunitsdictionary: Units_UnitsDictionary | None) -> None:
        """
        Initializes the instance of the class with the
        UnitsDictionary <aunitsdictionary>.
        """

    @overload
    def Init(self, aunitssystem: Units_UnitsSystem | None, aquantity: str) -> None:
        """
        Initializes the instance of the class with the
        UnitsSystem <aunitssystem> and positioned at the
        quantity <aquantity>.
        """

    @overload
    def Init(self, aunitsdictionary: Units_UnitsDictionary | None, aquantity: str) -> None:
        """
        Initializes the instance of the class with the
        UnitsDictionary <aunitsdictionary> and positioned at
        the quantity <aquantity>.
        """

    def MoreQuantity(self) -> bool:
        """
        Returns True if there is another Quantity to explore,
        False otherwise.
        """

    def NextQuantity(self) -> None:
        """Sets the next Quantity current."""

    def Quantity(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the current Quantity."""

    def MoreUnit(self) -> bool:
        """
        Returns True if there is another Unit to explore,
        False otherwise.
        """

    def NextUnit(self) -> None:
        """Sets the next Unit current."""

    def Unit(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the name of the current unit."""

    def IsActive(self) -> bool:
        """
        If the units system to explore is a user system,
        returns True if the current unit is active, False
        otherwise.

        If the units system to explore is the units
        dictionary, returns True if the current unit is the
        S.I. unit.
        """

class Units_Token(nanoocp.Standard.Standard_Transient):
    """
    This class defines an elementary word contained in
    a Sentence object.
    """

    @overload
    def __init__(self) -> None:
        """Creates and returns a empty token."""

    @overload
    def __init__(self, aword: str) -> None:
        """
        Creates and returns a token. <aword> is a string
        containing the available word.
        """

    @overload
    def __init__(self, atoken: Units_Token | None) -> None:
        """
        Creates and returns a token. <atoken> is copied in
        the returned token.
        """

    @overload
    def __init__(self, aword: str, amean: str) -> None:
        """
        Creates and returns a token. <aword> is a string
        containing the available word and <amean> gives the
        signification of the token.
        """

    @overload
    def __init__(self, aword: str, amean: str, avalue: float) -> None:
        """
        Creates and returns a token. <aword> is a string
        containing the available word, <amean> gives the
        signification of the token and <avalue> is the numeric
        value of the dimension.
        """

    @overload
    def __init__(self, aword: str, amean: str, avalue: float, adimension: Units_Dimensions | None) -> None:
        """
        Creates and returns a token. <aword> is a string
        containing the available word, <amean> gives the
        signification of the token, <avalue> is the numeric
        value of the dimension, and <adimensions> is the
        dimension of the given word <aword>.
        """

    @overload
    def __init__(self, theOther: Units_Token) -> None: ...

    def Creates(self) -> Units_Token:
        """Creates and returns a token, which is a ShiftedToken."""

    def Length(self) -> int:
        """Returns the length of the word."""

    @overload
    def Word(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns the string <theword>"""

    @overload
    def Word(self, aword: str) -> None:
        """Sets the field <theword> to <aword>."""

    @overload
    def Mean(self) -> nanoocp.TCollection.TCollection_AsciiString:
        """
        Returns the significance of the word <theword>, which
        is in the field <themean>.
        """

    @overload
    def Mean(self, amean: str) -> None:
        """Sets the field <themean> to <amean>."""

    @overload
    def Value(self) -> float:
        """Returns the value stored in the field <thevalue>."""

    @overload
    def Value(self, avalue: float) -> None:
        """Sets the field <thevalue> to <avalue>."""

    @overload
    def Dimensions(self) -> Units_Dimensions:
        """Returns the dimensions of the token <thedimensions>."""

    @overload
    def Dimensions(self, adimensions: Units_Dimensions | None) -> None:
        """Sets the field <thedimensions> to <adimensions>."""

    def Update(self, amean: str) -> None:
        """
        Updates the token <me> with the additional
        signification <amean> by concatenation of the two
        strings <themean> and <amean>. If the two
        significations are the same, an information message
        is written in the output device.
        """

    @overload
    def Add(self, aninteger: int) -> Units_Token: ...

    @overload
    def Add(self, atoken: Units_Token | None) -> Units_Token:
        """
        Returns a token which is the addition of <me> and
        another token <atoken>. The addition is possible if
        and only if the dimensions are the same.
        """

    def Subtract(self, atoken: Units_Token | None) -> Units_Token:
        """
        Returns a token which is the subtraction of <me> and
        another token <atoken>. The subtraction is possible if
        and only if the dimensions are the same.
        """

    def Multiply(self, atoken: Units_Token | None) -> Units_Token:
        """
        Returns a token which is the product of <me> and
        another token <atoken>.
        """

    def Multiplied(self, avalue: float) -> float:
        """
        This virtual method is called by the Measurement
        methods, to compute the measurement during a
        conversion.
        """

    def Divide(self, atoken: Units_Token | None) -> Units_Token:
        """
        Returns a token which is the division of <me> by another
        token <atoken>.
        """

    def Divided(self, avalue: float) -> float:
        """
        This virtual method is called by the Measurement
        methods, to compute the measurement during a
        conversion.
        """

    @overload
    def Power(self, atoken: Units_Token | None) -> Units_Token:
        """
        Returns a token which is <me> to the power of another
        token <atoken>. The computation is possible only if
        <atoken> is a dimensionless constant.
        """

    @overload
    def Power(self, anexponent: float) -> Units_Token:
        """Returns a token which is <me> to the power of <anexponent>."""

    @overload
    def IsEqual(self, astring: str) -> bool:
        """
        Returns true if the field <theword> and the string
        <astring> are the same, false otherwise.
        """

    @overload
    def IsEqual(self, atoken: Units_Token | None) -> bool:
        """
        Returns true if the field <theword> and the string
        <theword> contained in the token <atoken> are the
        same, false otherwise.
        """

    @overload
    def IsNotEqual(self, astring: str) -> bool:
        """
        Returns false if the field <theword> and the string
        <astring> are the same, true otherwise.
        """

    @overload
    def IsNotEqual(self, atoken: Units_Token | None) -> bool:
        """
        Returns false if the field <theword> and the string
        <theword> contained in the token <atoken> are the
        same, true otherwise.
        """

    def IsLessOrEqual(self, astring: str) -> bool:
        """
        Returns true if the field <theword> is strictly
        contained at the beginning of the string <astring>,
        false otherwise.
        """

    @overload
    def IsGreater(self, astring: str) -> bool: ...

    @overload
    def IsGreater(self, atoken: Units_Token | None) -> bool:
        """
        Returns false if the field <theword> is strictly
        contained at the beginning of the string <astring>,
        true otherwise.
        """

    def IsGreaterOrEqual(self, atoken: Units_Token | None) -> bool:
        """
        Returns true if the string <astring> is strictly
        contained at the beginning of the field <theword>
        false otherwise.
        """

    def Dump(self, ashift: int, alevel: int) -> None:
        """Useful for debugging"""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_Lexicon(nanoocp.Standard.Standard_Transient):
    """
    This class defines a lexicon useful to analyse and
    recognize the different key words included in a
    sentence. The lexicon is stored in a sequence of
    tokens.
    """

    @overload
    def __init__(self) -> None:
        """Creates an empty instance of Lexicon."""

    @overload
    def __init__(self, theOther: Units_Lexicon) -> None: ...

    def Creates(self) -> None:
        """
        Reads the file <afilename> to create a sequence of tokens
        stored in <thesequenceoftokens>.
        """

    def Sequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Token]:
        """Returns the first item of the sequence of tokens."""

    def AddToken(self, aword: str, amean: str, avalue: float) -> None:
        """
        Adds to the lexicon a new token with <aword>, <amean>,
        <avalue> as arguments. If there is already a token
        with the field <theword> equal to <aword>, the
        existing token is updated.
        """

    def Dump(self) -> None:
        """Useful for debugging."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_Sentence:
    """
    This class describes all the methods to create and
    compute an expression contained in a string.
    """

    @overload
    def __init__(self, alexicon: Units_Lexicon | None, astring: str) -> None:
        """
        Createsand returns a Sentence, by analyzing the
        string <astring> with the lexicon <alexicon>.
        """

    @overload
    def __init__(self, theOther: Units_Sentence) -> None: ...

    def SetConstants(self) -> None:
        """For each constant encountered, sets the value."""

    @overload
    def Sequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Token]:
        """Returns <thesequenceoftokens>."""

    @overload
    def Sequence(self, asequenceoftokens: nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Token] | None) -> None:
        """Sets the field <thesequenceoftokens> to <asequenceoftokens>."""

    def Evaluate(self) -> Units_Token:
        """
        Computes and returns in a token the result of the
        expression.
        """

    def IsDone(self) -> bool:
        """
        Return True if number of created tokens > 0
        (i.e creation of sentence is successful)
        """

    def Dump(self) -> None:
        """Useful for debugging."""

class Units_MathSentence(Units_Sentence):
    """
    This class defines all the methods to create and
    compute an algebraic formula.
    """

    @overload
    def __init__(self, astring: str) -> None:
        """
        Creates and returns a MathSentence object. The string
        <astring> describes an algebraic formula in natural
        language.
        """

    @overload
    def __init__(self, theOther: Units_MathSentence) -> None: ...

class Units_Measurement:
    """
    This class defines a measurement which is the
    association of a real value and a unit.
    """

    @overload
    def __init__(self) -> None:
        """It is the empty constructor of the class."""

    @overload
    def __init__(self, avalue: float, atoken: Units_Token | None) -> None:
        """
        Returns an instance of this class. <avalue> defines
        the measurement, and <atoken> the token which defines
        the unit used.
        """

    @overload
    def __init__(self, avalue: float, aunit: str) -> None:
        """
        Returns an instance of this class. <avalue> defines
        the measurement, and <aunit> the unit used,
        described in natural language.
        """

    @overload
    def __init__(self, theOther: Units_Measurement) -> None: ...

    def Convert(self, aunit: str) -> None:
        """
        Converts (if possible) the measurement object into
        another unit. <aunit> must have the same
        dimensionality as the unit contained in the token
        <thetoken>.
        """

    def Integer(self) -> Units_Measurement:
        """
        Returns a Measurement object with the integer value of
        the measurement contained in <me>.
        """

    def Fractional(self) -> Units_Measurement:
        """
        Returns a Measurement object with the fractional value
        of the measurement contained in <me>.
        """

    def Measurement(self) -> float:
        """Returns the value of the measurement."""

    def Token(self) -> Units_Token:
        """Returns the token contained in <me>."""

    def Add(self, ameasurement: Units_Measurement) -> Units_Measurement:
        """
        Returns (if it is possible) a measurement which is the
        addition of <me> and <ameasurement>. The chosen
        returned unit is the unit of <me>.
        """

    def __add__(self, ameasurement: Units_Measurement) -> Units_Measurement: ...

    def Subtract(self, ameasurement: Units_Measurement) -> Units_Measurement:
        """
        Returns (if it is possible) a measurement which is the
        subtraction of <me> and <ameasurement>. The chosen
        returned unit is the unit of <me>.
        """

    def __sub__(self, ameasurement: Units_Measurement) -> Units_Measurement: ...

    @overload
    def Multiply(self, ameasurement: Units_Measurement) -> Units_Measurement:
        """
        Returns a measurement which is the multiplication of
        <me> and <ameasurement>.
        """

    @overload
    def Multiply(self, avalue: float) -> Units_Measurement:
        """
        Returns a measurement which is the multiplication of
        <me> with the value <avalue>.
        """

    @overload
    def __mul__(self, ameasurement: Units_Measurement) -> Units_Measurement: ...

    @overload
    def __mul__(self, avalue: float) -> Units_Measurement: ...

    @overload
    def Divide(self, ameasurement: Units_Measurement) -> Units_Measurement:
        """
        Returns a measurement which is the division of <me> by
        <ameasurement>.
        """

    @overload
    def Divide(self, avalue: float) -> Units_Measurement:
        """
        Returns a measurement which is the division of <me> by
        the constant <avalue>.
        """

    @overload
    def __truediv__(self, ameasurement: Units_Measurement) -> Units_Measurement: ...

    @overload
    def __truediv__(self, avalue: float) -> Units_Measurement: ...

    def Power(self, anexponent: float) -> Units_Measurement:
        """
        Returns a measurement which is <me> powered
        <anexponent>.
        """

    def HasToken(self) -> bool: ...

    def Dump(self) -> None:
        """Useful for debugging."""

class Units_NoSuchType(nanoocp.Standard.Standard_NoSuchObject):
    pass

class Units_NoSuchUnit(nanoocp.Standard.Standard_NoSuchObject):
    pass

class Units_ShiftedToken(Units_Token):
    """
    The ShiftedToken class inherits from Token and
    describes tokens which have a gap in addition of
    the multiplicative factor. This kind of token
    allows the description of linear functions which
    do not pass through the origin, of the form:

    y = ax +b

    where <x> and <y> are the unknown variables, <a>
    the mutiplicative factor, and <b> the gap relative
    to the ordinate axis.

    An example is the translation between the Celsius
    and Fahrenheit degree of temperature.
    """

    @overload
    def __init__(self, aword: str, amean: str, avalue: float, amove: float, adimensions: Units_Dimensions | None) -> None:
        """
        Creates and returns a shifted token. <aword> is a
        string containing the available word, <amean> gives
        the signification of the token, <avalue> is the
        numeric value of the dimension, <amove> is the gap,
        and <adimensions> is the dimension of the given word
        <aword>.
        """

    @overload
    def __init__(self, theOther: Units_ShiftedToken) -> None: ...

    def Creates(self) -> Units_Token:
        """Creates and returns a token, which is a ShiftedToken."""

    def Move(self) -> float:
        """Returns the gap <themove>"""

    def Multiplied(self, avalue: float) -> float:
        """
        This virtual method is called by the Measurement
        methods, to compute the measurement during a
        conversion.
        """

    def Divided(self, avalue: float) -> float:
        """
        This virtual method is called by the Measurement
        methods, to compute the measurement during a
        conversion.
        """

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_ShiftedUnit(Units_Unit):
    """
    This class is useful to describe units with a
    shifted origin in relation to another unit. A well
    known example is the Celsius degrees in relation
    to Kelvin degrees. The shift of the Celsius origin
    is 273.15 Kelvin degrees.
    """

    @overload
    def __init__(self, aname: str) -> None:
        """
        Creates and returns a unit. <aname> is the name of
        the unit.
        """

    @overload
    def __init__(self, aname: str, asymbol: str) -> None:
        """
        Creates and returns a unit. <aname> is the name of
        the unit, <asymbol> is the usual abbreviation of the
        unit.
        """

    @overload
    def __init__(self, aname: str, asymbol: str, avalue: float, amove: float, aquantity: Units_Quantity | None) -> None:
        """
        Creates and returns a shifted unit. <aname> is the
        name of the unit, <asymbol> is the usual abbreviation
        of the unit, <avalue> is the value in relation to the
        International System of Units, and <amove> is the gap
        in relation to another unit.

        For example Celsius degree of temperature is an
        instance of ShiftedUnit with <avalue> equal to 1.
        and <amove> equal to 273.15.
        """

    @overload
    def __init__(self, theOther: Units_ShiftedUnit) -> None: ...

    @overload
    def Move(self, amove: float) -> None:
        """Sets the field <themove> to <amove>"""

    @overload
    def Move(self) -> float:
        """Returns the shifted value <themove>."""

    def Token(self) -> Units_Token:
        """This redefined method returns a ShiftedToken object."""

    def Dump(self, ashift: int, alevel: int) -> None: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_UnitsDictionary(nanoocp.Standard.Standard_Transient):
    """
    This class creates a dictionary of all the units
    you want to know.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty instance of UnitsDictionary."""

    @overload
    def __init__(self, theOther: Units_UnitsDictionary) -> None: ...

    def Creates(self) -> None:
        """
        Returns a UnitsDictionary object which contains the
        sequence of all the units you want to consider,
        physical quantity by physical quantity.
        """

    def Sequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Quantity]:
        """
        Returns the head of the sequence of physical
        quantities.
        """

    def ActiveUnit(self, aquantity: str) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns for <aquantity> the active unit."""

    @overload
    def Dump(self, alevel: int) -> None:
        """
        Dumps only the sequence of quantities without the
        units if <alevel> is equal to zero, and for each
        quantity all the units stored if <alevel> is equal to
        one.
        """

    @overload
    def Dump(self, adimensions: Units_Dimensions | None) -> None:
        """
        Dumps for a designated physical dimensions
        <adimensions> all the previously stored units.
        """

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_UnitSentence(Units_Sentence):
    """
    This class describes all the facilities to
    manipulate and compute units contained in a string
    expression.
    """

    @overload
    def __init__(self, astring: str) -> None:
        """
        Creates and returns a UnitSentence. The string
        <astring> describes in natural language the unit or
        the composed unit to be analysed.
        """

    @overload
    def __init__(self, astring: str, aquantitiessequence: nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Quantity] | None) -> None:
        """
        Creates and returns a UnitSentence. The string
        <astring> describes in natural language the unit to be
        analysed. The sequence of physical quantities
        <asequenceofquantities> describes the available
        dictionary of units you want to use.
        """

    @overload
    def __init__(self, theOther: Units_UnitSentence) -> None: ...

    def Analyse(self) -> None:
        """
        Analyzes the sequence of tokens created by the
        constructor to find the true significance of each
        token.
        """

    def SetUnits(self, aquantitiessequence: nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Quantity] | None) -> None:
        """
        For each token which represents a unit, finds in the
        sequence of physical quantities all the
        characteristics of the unit found.
        """

class Units_UnitsLexicon(Units_Lexicon):
    """
    This class defines a lexicon useful to analyse and
    recognize the different key words included in a
    sentence. The lexicon is stored in a sequence of
    tokens.
    """

    @overload
    def __init__(self) -> None:
        """Returns an empty instance of UnitsLexicon"""

    @overload
    def __init__(self, theOther: Units_UnitsLexicon) -> None: ...

    def Creates(self, amode: bool = True) -> None:
        """
        Reads the files <afilename1> and <afilename2> to
        create a sequence of tokens stored in
        <thesequenceoftokens>.
        """

    def Dump(self) -> None:
        """Useful for debugging."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class Units_UnitsSystem(nanoocp.Standard.Standard_Transient):
    """
    This class allows the user to define his own
    system of units.
    """

    @overload
    def __init__(self) -> None:
        """
        Returns an instance of UnitsSystem initialized to the
        S.I. units system.
        """

    @overload
    def __init__(self, aName: str, Verbose: bool = False) -> None:
        """
        Returns an instance of UnitsSystem initialized to the
        S.I. units system upgraded by the base system units description
        file.
        Attempts to find the four following files:
        $CSF_`aName`Defaults/.aName
        $CSF_`aName`SiteDefaults/.aName
        $CSF_`aName`GroupDefaults/.aName
        $CSF_`aName`UserDefaults/.aName
        See : Resource_Manager for the description of this file.
        """

    @overload
    def __init__(self, theOther: Units_UnitsSystem) -> None: ...

    def QuantitiesSequence(self) -> nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Quantity]:
        """Returns the sequence of refined quantities."""

    def ActiveUnitsSequence(self) -> nanoocp.NCollection.NCollection_HSequence[int]:
        """
        Returns a sequence of integer in correspondence with
        the sequence of quantities, which indicates, for each
        redefined quantity, the index into the sequence of
        units, of the active unit.
        """

    def Specify(self, aquantity: str, aunit: str) -> None:
        """Specifies for <aquantity> the unit <aunit> used."""

    def Remove(self, aquantity: str, aunit: str) -> None:
        """Removes for <aquantity> the unit <aunit> used."""

    def Activate(self, aquantity: str, aunit: str) -> None:
        """Specifies for <aquantity> the unit <aunit> used."""

    def Activates(self) -> None:
        """Activates the first unit of all defined system quantities"""

    def ActiveUnit(self, aquantity: str) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns for <aquantity> the active unit."""

    def ConvertValueToUserSystem(self, aquantity: str, avalue: float, aunit: str) -> float:
        """
        Converts a real value <avalue> from the unit <aunit>
        belonging to the physical dimensions <aquantity> to
        the corresponding unit of the user system.
        """

    def ConvertSIValueToUserSystem(self, aquantity: str, avalue: float) -> float:
        """
        Converts the real value <avalue> from the S.I. system
        of units to the user system of units. <aquantity> is
        the physical dimensions of the measurement.
        """

    def ConvertUserSystemValueToSI(self, aquantity: str, avalue: float) -> float:
        """
        Converts the real value <avalue> from the user system
        of units to the S.I. system of units. <aquantity> is
        the physical dimensions of the measurement.
        """

    def Dump(self) -> None: ...

    def IsEmpty(self) -> bool:
        """Returns TRUE if no units has been defined in the system."""

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

@overload
def pow(arg0: Units_Dimensions | None, arg1: float) -> Units_Dimensions: ...

@overload
def pow(arg0: Units_Token | None, arg1: Units_Token | None) -> Units_Token: ...

@overload
def pow(arg0: Units_Token | None, arg1: float) -> Units_Token: ...

# deprecated OCCT typedef names (src/Deprecated/NCollectionAliases)
import nanoocp.NCollection
import nanoocp.Units
Units_QtsSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.Units.Units_Quantity]
Units_QuantitiesSequence = nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Quantity]
Units_TksSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.Units.Units_Token]
Units_TokensSequence = nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Token]
Units_UnitsSequence = nanoocp.NCollection.NCollection_HSequence[nanoocp.Units.Units_Unit]
Units_UtsSequence = nanoocp.NCollection.NCollection_Sequence[nanoocp.Units.Units_Unit]
