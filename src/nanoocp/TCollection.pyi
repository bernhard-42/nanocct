"""OCCT package TCollection (toolkit TKernel)"""

from typing import TextIO, overload

import nanoocp.Message
import nanoocp.Standard


class TCollection:
    """
    The package <TCollection> provides the services for the
    transient basic data structures.
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, theOther: TCollection) -> None: ...

    @staticmethod
    def NextPrimeForMap(I: int) -> int:
        """
        Returns a prime number greater than <I> suitable
        to dimension a Map. When <I> becomes great there
        is a limit on the result (today the limit is
        around 1 000 000). This is not a limit of the number
        of items but a limit in the number of buckets. i.e.
        there will be more collisions in the map.
        """

class TCollection_AsciiString:
    """
    Class defines a variable-length sequence of 8-bit characters.
    Despite class name (kept for historical reasons), it is intended to store UTF-8 string, not just
    ASCII characters. However, multi-byte nature of UTF-8 is not considered by the following
    methods:
    - Method ::Length() return the number of bytes, not the number of Unicode symbols.
    - Methods taking/returning symbol index work with 8-bit code units, not true Unicode symbols,
    including ::Remove(), ::SetValue(), ::Value(), ::Search(), ::Trunc() and others.
    If application needs to process multi-byte Unicode symbols explicitly,
    NCollection_UtfIterator<char> class can be used for iterating through Unicode string (UTF-32
    code unit will be returned for each position).

    Class provides editing operations with built-in memory management to make AsciiString objects
    easier to use than ordinary character arrays. AsciiString objects follow value semantics; in
    other words, they are the actual strings, not handles to strings, and are copied through
    assignment. You may use HAsciiString objects to get handles to strings.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a AsciiString to an empty AsciiString."""

    @overload
    def __init__(self, theStringView: str) -> None:
        """
        Initializes a AsciiString with a string_view.
        @param[in] theStringView the string view to initialize from
        """

    @overload
    def __init__(self, theMessage: str) -> None:
        """
        Initializes a AsciiString with a CString (null-terminated).
        @param[in] theMessage the C string to initialize from
        """

    @overload
    def __init__(self, theChar: str) -> None:
        """
        Initializes a AsciiString with a single character.
        @param[in] theChar the character to initialize from
        """

    @overload
    def __init__(self, theValue: int) -> None:
        """
        Initializes an AsciiString with an integer value
        @param[in] theValue the integer value to convert to string
        """

    @overload
    def __init__(self, theValue: float) -> None:
        """
        Initializes an AsciiString with a real value
        @param[in] theValue the real value to convert to string
        """

    @overload
    def __init__(self, theString: TCollection_AsciiString) -> None:
        """
        Initializes a AsciiString with another AsciiString.
        @param[in] theString the string to copy from
        """

    @overload
    def __init__(self, theExtendedString: TCollection_ExtendedString, theReplaceNonAscii: str = '\x00') -> None:
        """
        Creation by converting an extended string to an ascii string.
        If replaceNonAscii is non-null character, it will be used
        in place of any non-ascii character found in the source string.
        Otherwise, creates UTF-8 unicode string.
        @param[in] theExtendedString the extended string to convert
        @param[in] theReplaceNonAscii replacement character for non-ASCII characters
        """

    @overload
    def __init__(self, theMessage: str, theLength: int) -> None:
        """
        Initializes a AsciiString with a CString and explicit length.
        @param[in] theMessage the C string to initialize from
        @param[in] theLength the length of the string
        """

    @overload
    def __init__(self, theLength: int, theFiller: str) -> None:
        """
        Initializes an AsciiString with specified length space allocated
        and filled with filler character. This is useful for buffers.
        @param[in] theLength the length to allocate
        @param[in] theFiller the character to fill with
        """

    @overload
    def __init__(self, theString: TCollection_AsciiString, theChar: str) -> None:
        """
        Initializes a AsciiString with copy of another AsciiString
        concatenated with the message character.
        @param[in] theString the string to copy
        @param[in] theChar the character to append
        """

    @overload
    def __init__(self, theString: TCollection_AsciiString, theMessage: str) -> None:
        """
        Initializes a AsciiString with copy of another AsciiString
        concatenated with the message string.
        @param[in] theString the string to copy
        @param[in] theMessage the C string to append
        """

    @overload
    def __init__(self, theString: TCollection_AsciiString, theOtherString: TCollection_AsciiString) -> None:
        """
        Initializes a AsciiString with copy of another AsciiString
        concatenated with the message string.
        @param[in] theString the string to copy
        @param[in] theOtherString the string to append
        """

    @overload
    def AssignCat(self, theOther: str) -> None:
        """
        Appends other character to this string. This is an unary operator.
        @param[in] theOther the character to append
        """

    @overload
    def AssignCat(self, theOther: int) -> None:
        """
        Appends other integer to this string. This is an unary operator.
        @param[in] theOther the integer to append
        """

    @overload
    def AssignCat(self, theOther: float) -> None:
        """
        Appends other real number to this string. This is an unary operator.
        @param[in] theOther the real number to append
        """

    @overload
    def AssignCat(self, theOther: TCollection_ExtendedString, theReplaceNonAscii: str = '\x00') -> None:
        """
        Appends an extended string to this ASCII string.
        If theReplaceNonAscii is non-null character, it will be used
        in place of any non-ASCII character found in the source string.
        Otherwise, appends UTF-8 representation of the source string.
        @param[in] theOther the extended string to append
        @param[in] theReplaceNonAscii replacement character for non-ASCII characters
        """

    @overload
    def AssignCat(self, theString: str, theLength: int) -> None:
        """
        Core implementation: Appends string (pointer and length) to this ASCII string.
        This is the primary implementation that all other AssignCat overloads redirect to.
        @param[in] theString pointer to the string to append
        @param[in] theLength length of the string to append
        """

    @overload
    def AssignCat(self, theOther: TCollection_AsciiString) -> None:
        """
        Appends other string to this string. This is an unary operator.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello");
        TCollection_AsciiString anotherString(" World");
        aString += anotherString;
        // Result: aString == "Hello World"
        ```
        @param[in] theOther the string to append
        """

    @overload
    def AssignCat(self, theCString: str) -> None:
        """
        Appends C string to this ASCII string.
        @param[in] theCString the C string to append
        """

    @overload
    def AssignCat(self, theStringView: str) -> None:
        """
        Appends string view to this ASCII string. This is an unary operator.
        @param[in] theStringView the string view to append
        """

    @overload
    def __iadd__(self, theOther: str) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theOther: int) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theOther: float) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theOther: TCollection_ExtendedString) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theOther: TCollection_AsciiString) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theCString: str) -> TCollection_AsciiString: ...

    @overload
    def __iadd__(self, theStringView: str) -> TCollection_AsciiString: ...

    def Capitalize(self) -> None:
        """
        Converts the first character into its corresponding
        upper-case character and the other characters into lowercase

        Example:
        ```cpp
        TCollection_AsciiString aString("hellO ");
        aString.Capitalize();
        // Result: aString == "Hello "
        ```
        """

    @overload
    def Cat(self, theString: str, theLength: int) -> TCollection_AsciiString:
        """
        Core implementation: Appends string (pointer and length) to this ASCII string and returns
        a new string. This is the primary implementation that all other Cat overloads redirect to.
        @param[in] theString pointer to the string to append
        @param[in] theLength length of the string to append
        @return new string with the string appended
        """

    @overload
    def Cat(self, theOther: str) -> TCollection_AsciiString:
        """
        Appends other character to this string.

        Example:
        ```cpp
        TCollection_AsciiString aString("I say ");
        TCollection_AsciiString aResult = aString + '!';
        // Result: aResult == "I say !"

        // To catenate more, you must put a String before.
        // "Hello " + "Dolly" // THIS IS NOT ALLOWED
        // This rule is applicable to AssignCat (operator +=) too.
        ```
        @param[in] theOther the character to append
        @return new string with character appended
        """

    @overload
    def Cat(self, theOther: int) -> TCollection_AsciiString:
        """
        Appends other integer to this string.

        Example:
        ```cpp
        TCollection_AsciiString aString("I say ");
        TCollection_AsciiString aResult = aString + 15;
        // Result: aResult == "I say 15"
        ```
        @param[in] theOther the integer to append
        @return new string with integer appended
        """

    @overload
    def Cat(self, theOther: float) -> TCollection_AsciiString:
        """
        Appends other real number to this string.

        Example:
        ```cpp
        TCollection_AsciiString aString("I say ");
        TCollection_AsciiString aResult = aString + 15.15;
        // Result: aResult == "I say 15.15"
        ```
        @param[in] theOther the real number to append
        @return new string with real number appended
        """

    @overload
    def Cat(self, theOther: TCollection_ExtendedString, theReplaceNonAscii: str = '\x00') -> TCollection_AsciiString:
        """
        Appends extended string to this string.
        If theReplaceNonAscii is non-null character, it will be used
        in place of any non-ASCII character found in the source string.
        Otherwise, concatenates UTF-8 representation of the source string.
        @param[in] theOther the extended string to append
        @param[in] theReplaceNonAscii replacement character for non-ASCII characters
        @return new string with extended string appended
        """

    @overload
    def Cat(self, theOther: TCollection_AsciiString) -> TCollection_AsciiString:
        """
        Appends other string to this string.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello");
        TCollection_AsciiString anotherString(" World");
        TCollection_AsciiString aResult = aString + anotherString;
        // Result: aResult == "Hello World"
        ```
        @param[in] theOther the string to append
        @return new string with other string appended
        """

    @overload
    def Cat(self, theCString: str) -> TCollection_AsciiString:
        """
        Appends C string to this ASCII string.
        @param[in] theCString the C string to append
        @return new string with C string appended
        """

    @overload
    def Cat(self, theStringView: str) -> TCollection_AsciiString:
        """
        Appends string view to this ASCII string.
        @param[in] theStringView the string view to append
        @return new string with string view appended
        """

    @overload
    def __add__(self, theOther: str) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theOther: int) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theOther: float) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theOther: TCollection_ExtendedString) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theOther: TCollection_AsciiString) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theCString: str) -> TCollection_AsciiString: ...

    @overload
    def __add__(self, theStringView: str) -> TCollection_AsciiString: ...

    def Center(self, theWidth: int, theFiller: str) -> None:
        """
        Modifies this ASCII string so that its length
        becomes equal to Width and the new characters
        are equal to Filler. New characters are added
        both at the beginning and at the end of this string.
        If Width is less than the length of this ASCII string, nothing happens.

        Example:
        ```cpp
        TCollection_AsciiString anAlphabet("abcdef");
        anAlphabet.Center(9, ' ');
        // Result: anAlphabet == " abcdef "
        ```
        @param[in] theWidth the desired width
        @param[in] theFiller the character to fill with
        """

    def ChangeAll(self, theChar: str, theNewChar: str, theCaseSensitive: bool = True) -> None:
        """
        Substitutes all the characters equal to aChar by NewChar
        in this AsciiString.
        The substitution can be case sensitive.
        If you don't use default case sensitive, no matter whether aChar
        is uppercase or not.

        Example:
        ```cpp
        TCollection_AsciiString aString("Histake");
        aString.ChangeAll('H', 'M', true);
        // Result: aString == "Mistake"
        ```
        @param[in] theChar the character to replace
        @param[in] theNewChar the replacement character
        @param[in] theCaseSensitive flag indicating case sensitivity
        """

    def Clear(self) -> None:
        """
        Removes all characters contained in this string.
        This produces an empty AsciiString.
        """

    @overload
    def Copy(self, theString: str, theLength: int) -> None:
        """
        Core implementation: Copy string (pointer and length) to this ASCII string.
        This is the primary implementation that all other Copy overloads redirect to.
        Used as operator =
        @param[in] theString pointer to the string to copy from
        @param[in] theLength length of the string to copy
        """

    @overload
    def Copy(self, theCString: str) -> None:
        """
        Copy C string to this ASCII string.
        Used as operator =
        @param[in] theCString the C string to copy from
        """

    @overload
    def Copy(self, theStringView: str) -> None:
        """
        Copy string view to this ASCII string.
        Used as operator =
        @param[in] theStringView the string view to copy from
        """

    @overload
    def Copy(self, theFromWhere: TCollection_AsciiString) -> None:
        """
        Copy fromwhere to this string.
        Used as operator =

        Example:
        ```cpp
        TCollection_AsciiString aString;
        TCollection_AsciiString anotherString("Hello World");
        aString = anotherString;  // operator=
        // Result: aString == "Hello World"
        ```
        """

    def Swap(self, theOther: TCollection_AsciiString) -> None:
        """
        Exchange the data of two strings (without reallocating memory).
        @param[in,out] theOther the string to exchange data with
        """

    @overload
    def FirstLocationInSet(self, theSet: str, theSetLength: int, theFromIndex: int, theToIndex: int) -> int:
        """
        Core implementation: Returns the index of the first character of this string that is
        present in the given character set (pointer and length).
        The search begins at index FromIndex and ends at index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.
        @param[in] theSet pointer to the set of characters to search for
        @param[in] theSetLength length of the set
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character found in set, or 0 if not found
        """

    @overload
    def FirstLocationInSet(self, theSet: TCollection_AsciiString, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string that is
        present in Set.
        The search begins to the index FromIndex and ends to the
        the index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.

        Example:
        ```cpp
        TCollection_AsciiString aString("aabAcAa");
        TCollection_AsciiString aSet("Aa");
        int anIndex = aString.FirstLocationInSet(aSet, 1, 7);
        // Result: anIndex == 1
        ```
        @param[in] theSet the set of characters to search for
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character found in set, or 0 if not found
        """

    @overload
    def FirstLocationInSet(self, theSet: str, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string that is present in string_view.
        @param[in] theSet the string view of characters to search for
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character found in set, or 0 if not found
        """

    @overload
    def FirstLocationNotInSet(self, theSet: str, theSetLength: int, theFromIndex: int, theToIndex: int) -> int:
        """
        Core implementation: Returns the index of the first character of this string
        that is not present in the given character set (pointer and length).
        The search begins at index FromIndex and ends at index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.
        @param[in] theSet pointer to the set of characters to check against
        @param[in] theSetLength length of the set
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character not in set, or 0 if not found
        """

    @overload
    def FirstLocationNotInSet(self, theSet: TCollection_AsciiString, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string
        that is not present in the set Set.
        The search begins to the index FromIndex and ends to the
        the index ToIndex in this string.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.

        Example:
        ```cpp
        TCollection_AsciiString aString("aabAcAa");
        TCollection_AsciiString aSet("Aa");
        int anIndex = aString.FirstLocationNotInSet(aSet, 1, 7);
        // Result: anIndex == 3
        ```
        @param[in] theSet the set of characters to check against
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character not in set, or 0 if not found
        """

    @overload
    def FirstLocationNotInSet(self, theSet: str, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string that is not present in string_view.
        @param[in] theSet the string view of characters to check against
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first character not in set, or 0 if not found
        """

    @overload
    def Insert(self, theWhere: int, theWhat: str) -> None:
        """
        Inserts a Character at position where.

        Example:
        ```cpp
        TCollection_AsciiString aString("hy not ?");
        aString.Insert(1, 'W');
        // Result: aString == "Why not ?"

        TCollection_AsciiString bString("Wh");
        bString.Insert(3, 'y');
        // Result: bString == "Why"
        ```
        @param[in] theWhere the position to insert at
        @param[in] theWhat the character to insert
        """

    @overload
    def Insert(self, theWhere: int, theString: str, theLength: int) -> None:
        """
        Core implementation: Inserts a string (pointer and length) at position theWhere.
        This is the primary implementation that all other Insert overloads redirect to.
        @param[in] theWhere position to insert at
        @param[in] theString pointer to the string to insert
        @param[in] theLength length of the string to insert
        """

    @overload
    def Insert(self, theWhere: int, theWhat: TCollection_AsciiString) -> None:
        """
        Inserts a AsciiString at position where.
        @param[in] theWhere the position to insert at
        @param[in] theWhat the ASCII string to insert
        """

    @overload
    def Insert(self, theWhere: int, theCString: str) -> None:
        """
        Inserts a C string at position theWhere.
        @param[in] theWhere position to insert at
        @param[in] theCString the C string to insert
        """

    @overload
    def Insert(self, theWhere: int, theStringView: str) -> None:
        """
        Inserts a string_view at position theWhere.
        @param[in] theWhere position to insert at
        @param[in] theStringView the string view to insert
        """

    @overload
    def InsertAfter(self, theIndex: int, theString: str, theLength: int) -> None:
        """
        Core implementation: Inserts string (pointer and length) after a specific index in this
        string. This is the primary implementation that all other InsertAfter overloads redirect to.
        Raises an exception if index is out of bounds (less than 0 or greater than the length).
        @param[in] theIndex the index to insert after
        @param[in] theString pointer to the string to insert
        @param[in] theLength length of the string to insert
        """

    @overload
    def InsertAfter(self, theIndex: int, theOther: TCollection_AsciiString) -> None:
        """
        Inserts an ASCII string after a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert after
        @param[in] theOther the string to insert
        """

    @overload
    def InsertAfter(self, theIndex: int, theCString: str) -> None:
        """
        Inserts a C string after a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert after
        @param[in] theCString the C string to insert
        """

    @overload
    def InsertAfter(self, theIndex: int, theStringView: str) -> None:
        """
        Inserts a string_view after a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert after
        @param[in] theStringView the string view to insert
        """

    @overload
    def InsertBefore(self, theIndex: int, theString: str, theLength: int) -> None:
        """
        Core implementation: Inserts string (pointer and length) before a specific index in this
        string. This is the primary implementation that all other InsertBefore overloads redirect to.
        Raises an exception if index is out of bounds (less than 1 or greater than the length).
        @param[in] theIndex the index to insert before
        @param[in] theString pointer to the string to insert
        @param[in] theLength length of the string to insert
        """

    @overload
    def InsertBefore(self, theIndex: int, theOther: TCollection_AsciiString) -> None:
        """
        Inserts an ASCII string before a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert before
        @param[in] theOther the string to insert
        """

    @overload
    def InsertBefore(self, theIndex: int, theCString: str) -> None:
        """
        Inserts a C string before a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert before
        @param[in] theCString the C string to insert
        """

    @overload
    def InsertBefore(self, theIndex: int, theStringView: str) -> None:
        """
        Inserts a string_view before a specific index in this string.
        Raises an exception if index is out of bounds.
        @param[in] theIndex the index to insert before
        @param[in] theStringView the string view to insert
        """

    def IsEmpty(self) -> bool:
        """Returns True if this string contains zero character."""

    @overload
    def IsEqual(self, theOther: TCollection_AsciiString) -> bool:
        """
        Returns true if the characters in this ASCII string
        are identical to the characters in ASCII string other.
        Note that this method is an alias of operator ==.
        @param[in] theOther the ASCII string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def IsEqual(self, theString: str, theLength: int) -> bool:
        """
        Core implementation: Returns true if the characters in this ASCII string
        are identical to the string (pointer and length).
        This is the primary implementation that string_view and CString overloads redirect to.
        @param[in] theString pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def IsEqual(self, theCString: str) -> bool:
        """
        Returns true if the characters in this ASCII string are identical to the C string.
        @param[in] theCString the C string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def IsEqual(self, theStringView: str) -> bool:
        """
        Returns true if the characters in this ASCII string
        are identical to the characters in string_view.
        @param[in] theStringView the string view to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def __eq__(self, theOther: TCollection_AsciiString) -> bool: ...

    @overload
    def __eq__(self, theCString: str) -> bool: ...

    @overload
    def __eq__(self, theStringView: str) -> bool: ...

    @overload
    def IsDifferent(self, theOther: TCollection_AsciiString) -> bool:
        """
        Returns true if there are differences between the
        characters in this ASCII string and ASCII string other.
        Note that this method is an alias of operator !=
        @param[in] theOther the ASCII string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def IsDifferent(self, theString: str, theLength: int) -> bool:
        """
        Core implementation: Returns true if there are differences between this ASCII string
        and the string (pointer and length).
        This is the primary implementation that string_view and CString overloads redirect to.
        @param[in] theString pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def IsDifferent(self, theCString: str) -> bool:
        """
        Returns true if there are differences between this ASCII string and C string.
        @param[in] theCString the C string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def IsDifferent(self, theStringView: str) -> bool:
        """
        Returns true if there are differences between the
        characters in this ASCII string and string_view.
        @param[in] theStringView the string view to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def __ne__(self, theOther: TCollection_AsciiString) -> bool: ...

    @overload
    def __ne__(self, theCString: str) -> bool: ...

    @overload
    def __ne__(self, theStringView: str) -> bool: ...

    @overload
    def IsLess(self, theString: str, theLength: int) -> bool:
        """
        Core implementation: Returns TRUE if this string is lexicographically less than
        the string (pointer and length).
        This is the primary implementation that all other IsLess overloads redirect to.
        @param[in] theString pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if this string is lexicographically less than the given string
        """

    @overload
    def IsLess(self, theOther: TCollection_AsciiString) -> bool:
        """
        Returns TRUE if this string is 'ASCII' less than other.
        @param[in] theOther the ASCII string to compare with
        @return true if this string is lexicographically less than other
        """

    @overload
    def IsLess(self, theCString: str) -> bool:
        """
        Returns TRUE if this string is lexicographically less than C string.
        @param[in] theCString the C string to compare with
        @return true if this string is lexicographically less than C string
        """

    @overload
    def IsLess(self, theStringView: str) -> bool:
        """
        Returns TRUE if this ASCII string is lexicographically less than theStringView.
        @param[in] theStringView the string view to compare with
        @return true if this string is lexicographically less than theStringView
        """

    @overload
    def __lt__(self, theOther: TCollection_AsciiString) -> bool: ...

    @overload
    def __lt__(self, theCString: str) -> bool: ...

    @overload
    def __lt__(self, theStringView: str) -> bool: ...

    @overload
    def IsGreater(self, theString: str, theLength: int) -> bool:
        """
        Core implementation: Returns TRUE if this string is lexicographically greater than
        the string (pointer and length).
        This is the primary implementation that all other IsGreater overloads redirect to.
        @param[in] theString pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if this string is lexicographically greater than the given string
        """

    @overload
    def IsGreater(self, theOther: TCollection_AsciiString) -> bool:
        """
        Returns TRUE if this string is 'ASCII' greater than other.
        @param[in] theOther the ASCII string to compare with
        @return true if this string is lexicographically greater than other
        """

    @overload
    def IsGreater(self, theCString: str) -> bool:
        """
        Returns TRUE if this string is lexicographically greater than C string.
        @param[in] theCString the C string to compare with
        @return true if this string is lexicographically greater than C string
        """

    @overload
    def IsGreater(self, theStringView: str) -> bool:
        """
        Returns TRUE if this ASCII string is lexicographically greater than theStringView.
        @param[in] theStringView the string view to compare with
        @return true if this string is lexicographically greater than theStringView
        """

    @overload
    def __gt__(self, theOther: TCollection_AsciiString) -> bool: ...

    @overload
    def __gt__(self, theCString: str) -> bool: ...

    @overload
    def __gt__(self, theStringView: str) -> bool: ...

    @overload
    def StartsWith(self, theStartString: str, theStartLength: int) -> bool:
        """
        Core implementation: Determines whether the beginning of this string instance matches
        the specified string (pointer and length).
        @param[in] theStartString pointer to the string to check for at the beginning
        @param[in] theStartLength length of the string to check for
        @return true if this string starts with theStartString
        """

    @overload
    def StartsWith(self, theStartString: TCollection_AsciiString) -> bool:
        """
        Determines whether the beginning of this string instance matches the specified string.
        @param[in] theStartString the string to check for at the beginning
        @return true if this string starts with theStartString
        """

    @overload
    def StartsWith(self, theCString: str) -> bool:
        """
        Determines whether the beginning of this string matches the specified C string.
        @param[in] theCString the C string to check for at the beginning
        @return true if this string starts with theCString
        """

    @overload
    def StartsWith(self, theStartString: str) -> bool:
        """
        Determines whether the beginning of this string instance matches the specified string_view.
        @param[in] theStartString the string view to check for at the beginning
        @return true if this string starts with theStartString
        """

    @overload
    def EndsWith(self, theEndString: str, theEndLength: int) -> bool:
        """
        Core implementation: Determines whether the end of this string instance matches
        the specified string (pointer and length).
        @param[in] theEndString pointer to the string to check for at the end
        @param[in] theEndLength length of the string to check for
        @return true if this string ends with theEndString
        """

    @overload
    def EndsWith(self, theEndString: TCollection_AsciiString) -> bool:
        """
        Determines whether the end of this string instance matches the specified string.
        @param[in] theEndString the string to check for at the end
        @return true if this string ends with theEndString
        """

    @overload
    def EndsWith(self, theEndString: str) -> bool:
        """
        Determines whether the end of this string instance matches the specified string_view.
        @param[in] theEndString the string view to check for at the end
        @return true if this string ends with theEndString
        """

    def IntegerValue(self) -> int:
        """
        Converts a AsciiString containing a numeric expression to an Integer.

        Example:
        ```cpp
        TCollection_AsciiString aString("215");
        int anInt = aString.IntegerValue();
        // Result: anInt == 215
        ```
        @return the integer value of the string
        """

    def IsIntegerValue(self) -> bool:
        """
        Returns True if the AsciiString contains an integer value.
        Note: an integer value is considered to be a real value as well.
        @return true if string represents an integer value
        """

    def IsRealValue(self, theToCheckFull: bool = False) -> bool:
        """
        Returns True if the AsciiString starts with some characters that can be interpreted as integer
        or real value.
        @param[in] theToCheckFull  when TRUE, checks if entire string defines a real value;
        otherwise checks if string starts with a real value
        Note: an integer value is considered to be a real value as well.
        @return true if string represents a real value
        """

    def IsAscii(self) -> bool:
        """
        Returns True if the AsciiString contains only ASCII characters
        between ' ' and '~'.
        This means no control character and no extended ASCII code.
        @return true if string contains only ASCII characters
        """

    def LeftAdjust(self) -> None:
        """Removes all space characters in the beginning of the string."""

    def LeftJustify(self, theWidth: int, theFiller: str) -> None:
        """
        left justify
        Length becomes equal to Width and the new characters are
        equal to Filler.
        If Width < Length nothing happens.
        Raises an exception if Width is less than zero.

        Example:
        ```cpp
        TCollection_AsciiString aString("abcdef");
        aString.LeftJustify(9, ' ');
        // Result: aString == "abcdef   "
        ```
        @param[in] theWidth the desired width
        @param[in] theFiller the character to fill with
        """

    def Length(self) -> int:
        """
        Returns number of characters in this string.
        This is the same functionality as 'strlen' in C.

        Example:
        ```cpp
        TCollection_AsciiString anAlphabet("abcdef");
        int aLength = anAlphabet.Length();
        // Result: aLength == 6
        ```
        -   1 is the position of the first character in this string.
        -   The length of this string gives the position of its last character.
        -   Positions less than or equal to zero, or
        greater than the length of this string are
        invalid in functions which identify a character
        of this string by its position.
        @return the number of characters in the string
        """

    @overload
    def Location(self, theOther: TCollection_AsciiString, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns an index in this string of the first occurrence
        of the string S in this string from the starting index
        FromIndex to the ending index ToIndex
        returns zero if failure
        Raises an exception if FromIndex or ToIndex is out of range.

        Example:
        ```cpp
        TCollection_AsciiString aString("aabAaAa");
        TCollection_AsciiString aSearchString("Aa");
        int anIndex = aString.Location(aSearchString, 1, 7);
        // Result: anIndex == 4
        ```
        @param[in] theOther the string to search for
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of first occurrence, or 0 if not found
        """

    @overload
    def Location(self, theN: int, theC: str, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the nth occurrence of the character C
        in this string from the starting index FromIndex to the
        ending index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.

        Example:
        ```cpp
        TCollection_AsciiString aString("aabAa");
        int anIndex = aString.Location(3, 'a', 1, 5);
        // Result: anIndex == 5
        ```
        @param[in] theN the occurrence number to find
        @param[in] theC the character to search for
        @param[in] theFromIndex the starting index for search
        @param[in] theToIndex the ending index for search
        @return the index of the nth occurrence, or 0 if not found
        """

    def LowerCase(self) -> None:
        """
        Converts this string to its lower-case equivalent.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello Dolly");
        aString.UpperCase();
        // Result: aString == "HELLO DOLLY"
        aString.LowerCase();
        // Result: aString == "hello dolly"
        ```
        """

    def Prepend(self, theOther: TCollection_AsciiString) -> None:
        """
        Inserts the string other at the beginning of this ASCII string.

        Example:
        ```cpp
        TCollection_AsciiString anAlphabet("cde");
        TCollection_AsciiString aBegin("ab");
        anAlphabet.Prepend(aBegin);
        // Result: anAlphabet == "abcde"
        ```
        @param[in] theOther the string to prepend
        """

    def Print(self) -> object:
        """
        Displays this string on a stream.
        @param[in] theStream the output stream
        """

    def Read(self, theStream: TextIO) -> None:
        """
        Read this string from a stream.
        @param[in] theStream the input stream
        """

    def RealValue(self) -> float:
        """
        Converts an AsciiString containing a numeric expression to a Real.

        Example:
        ```cpp
        TCollection_AsciiString aString1("215");
        double aReal1 = aString1.RealValue();
        // Result: aReal1 == 215.0

        TCollection_AsciiString aString2("3.14159267");
        double aReal2 = aString2.RealValue();
        // Result: aReal2 == 3.14159267
        ```
        @return the real value of the string
        """

    @overload
    def RemoveAll(self, theC: str, theCaseSensitive: bool) -> None:
        """
        Remove all the occurrences of the character C in the string.

        Example:
        ```cpp
        TCollection_AsciiString aString("HellLLo");
        aString.RemoveAll('L', true);
        // Result: aString == "Hello"
        ```
        @param[in] theC the character to remove
        @param[in] theCaseSensitive flag indicating case sensitivity
        """

    @overload
    def RemoveAll(self, theWhat: str) -> None:
        """
        Removes every what characters from this string.
        @param[in] theWhat the character to remove
        """

    def Remove(self, theWhere: int, theHowMany: int = 1) -> None:
        """
        Erases ahowmany characters from position where,
        where included.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello");
        aString.Remove(2, 2); // erases 2 characters from position 2
        // Result: aString == "Hlo"
        ```
        @param[in] theWhere the position to start erasing from
        @param[in] theHowMany the number of characters to erase
        """

    def RightAdjust(self) -> None:
        """Removes all space characters at the end of the string."""

    def RightJustify(self, theWidth: int, theFiller: str) -> None:
        """
        Right justify.
        Length becomes equal to Width and the new characters are
        equal to Filler.
        if Width < Length nothing happens.
        Raises an exception if Width is less than zero.

        Example:
        ```cpp
        TCollection_AsciiString aString("abcdef");
        aString.RightJustify(9, ' ');
        // Result: aString == "   abcdef"
        ```
        @param[in] theWidth the desired width
        @param[in] theFiller the character to fill with
        """

    @overload
    def Search(self, theWhat: str, theWhatLength: int) -> int:
        """
        Core implementation: Searches a string (pointer and length) in this string from the beginning
        and returns position of first item matching.
        It returns -1 if not found.
        @param[in] theWhat pointer to the string to search for
        @param[in] theWhatLength length of the string to search for
        @return the position of first match, or -1 if not found
        """

    @overload
    def Search(self, theWhat: TCollection_AsciiString) -> int:
        """
        Searches an AsciiString in this string from the beginning
        and returns position of first item what matching.
        It returns -1 if not found.
        @param[in] theWhat the ASCII string to search for
        @return the position of first match, or -1 if not found
        """

    @overload
    def Search(self, theCString: str) -> int:
        """
        Searches a C string in this string from the beginning.
        @param[in] theCString the C string to search for
        @return the position of first match, or -1 if not found
        """

    @overload
    def Search(self, theWhat: str) -> int:
        """
        Searches a string_view in this string from the beginning
        and returns position of first item matching.
        It returns -1 if not found.
        @param[in] theWhat the string view to search for
        @return the position of first match, or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: str, theWhatLength: int) -> int:
        """
        Core implementation: Searches a string (pointer and length) in this string from the end
        and returns position of first item matching.
        It returns -1 if not found.
        @param[in] theWhat pointer to the string to search for
        @param[in] theWhatLength length of the string to search for
        @return the position of first match from end, or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: TCollection_AsciiString) -> int:
        """
        Searches a AsciiString in another AsciiString from the end
        and returns position of first item what matching.
        It returns -1 if not found.
        @param[in] theWhat the ASCII string to search for
        @return the position of first match from end, or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theCString: str) -> int:
        """
        Searches a C string in this string from the end.
        @param[in] theCString the C string to search for
        @return the position of first match from end, or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: str) -> int:
        """
        Searches a string_view in this string from the end
        and returns position of first item matching.
        It returns -1 if not found.
        @param[in] theWhat the string view to search for
        @return the position of first match from end, or -1 if not found
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: str) -> None:
        """
        Replaces one character in the AsciiString at position where.
        If where is less than zero or greater than the length of this string
        an exception is raised.

        Example:
        ```cpp
        TCollection_AsciiString aString("Garbake");
        aString.SetValue(6, 'g');
        // Result: aString == "Garbage"
        ```
        @param[in] theWhere the position to replace at
        @param[in] theWhat the character to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theString: str, theLength: int) -> None:
        """
        Core implementation: Replaces a part of this string with a string (pointer and length).
        This is the primary implementation that all other SetValue string overloads redirect to.
        @param[in] theWhere position to start replacement
        @param[in] theString pointer to the string to replace with
        @param[in] theLength length of the string to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: TCollection_AsciiString) -> None:
        """
        Replaces a part of this string by another AsciiString.
        @param[in] theWhere the position to start replacement
        @param[in] theWhat the ASCII string to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theCString: str) -> None:
        """
        Replaces a part of this ASCII string with a C string.
        @param[in] theWhere position to start replacement
        @param[in] theCString the C string to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theStringView: str) -> None:
        """
        Replaces a part of this ASCII string with a string_view.
        @param[in] theWhere position to start replacement
        @param[in] theStringView the string view to replace with
        """

    def Split(self, theWhere: int) -> TCollection_AsciiString:
        """
        Splits a AsciiString into two sub-strings.

        Example:
        ```cpp
        TCollection_AsciiString aString("abcdefg");
        TCollection_AsciiString aSecondPart = aString.Split(3);
        // Result: aString == "abc" and aSecondPart == "defg"
        ```
        @param[in] theWhere the position to split at
        @return the second part of the split string
        """

    def SubString(self, theFromIndex: int, theToIndex: int) -> TCollection_AsciiString:
        """
        Creation of a sub-string of this string.
        The sub-string starts to the index Fromindex and ends
        to the index ToIndex.
        Raises an exception if ToIndex or FromIndex is out of bounds

        Example:
        ```cpp
        TCollection_AsciiString aString("abcdefg");
        TCollection_AsciiString aSubString = aString.SubString(3, 6);
        // Result: aSubString == "cdef"
        ```
        @param[in] theFromIndex the starting index
        @param[in] theToIndex the ending index
        @return the substring from FromIndex to ToIndex
        """

    def ToCString(self) -> str:
        """
        Returns pointer to AsciiString (char *).
        This is useful for some casual manipulations.
        Warning: Because this "char *" is 'const', you can't modify its contents.
        @return the C string representation
        """

    def Token(self, theSeparators: str = ' \t', theWhichOne: int = 1) -> TCollection_AsciiString:
        """
        Extracts whichone token from this string.
        By default, the separators is set to space and tabulation.
        By default, the token extracted is the first one (whichone = 1).
        separators contains all separators you need.
        If no token indexed by whichone is found, it returns empty AsciiString.

        Example:
        ```cpp
        TCollection_AsciiString aString("This is a     message");
        TCollection_AsciiString aToken1 = aString.Token();
        // Result: aToken1 == "This"

        TCollection_AsciiString aToken2 = aString.Token(" ", 4);
        // Result: aToken2 == "message"

        TCollection_AsciiString aToken3 = aString.Token(" ", 2);
        // Result: aToken3 == "is"

        TCollection_AsciiString aToken4 = aString.Token(" ", 9);
        // Result: aToken4 == ""

        TCollection_AsciiString bString("1234; test:message   , value");
        TCollection_AsciiString bToken1 = bString.Token("; :,", 4);
        // Result: bToken1 == "value"

        TCollection_AsciiString bToken2 = bString.Token("; :,", 2);
        // Result: bToken2 == "test"
        ```
        @param[in] theSeparators the separator characters
        @param[in] theWhichOne the token number to extract
        """

    def Trunc(self, theHowMany: int) -> None:
        """
        Truncates this string to ahowmany characters.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello Dolly");
        aString.Trunc(3);
        // Result: aString == "Hel"
        ```
        @param[in] theHowMany the number of characters to keep
        """

    def UpperCase(self) -> None:
        """Converts this string to its upper-case equivalent."""

    def UsefullLength(self) -> int:
        """
        Length of the string ignoring all spaces (' ') and the
        control character at the end.
        @return the useful length of the string
        """

    def Value(self, theWhere: int) -> str:
        """
        Returns character at position where in this string.
        If where is less than zero or greater than the length of this string,
        an exception is raised.

        Example:
        ```cpp
        TCollection_AsciiString aString("Hello");
        char aChar = aString.Value(2);
        // Result: aChar == 'e'
        ```
        @param[in] theWhere the position to get character from
        @return the character at the specified position
        """

    def HashCode(self) -> int:
        """
        Computes a hash code for the given ASCII string
        Returns the same integer value as the hash function for TCollection_ExtendedString
        @return a computed hash code
        """

    @staticmethod
    def EmptyString() -> TCollection_AsciiString:
        """
        Returns a const reference to a single shared empty string instance.
        This method provides access to a static empty string to avoid creating temporary empty
        strings. Use this method instead of constructing empty strings when you need a const
        reference.

        Example:
        ```cpp
        const TCollection_AsciiString& anEmptyStr = TCollection_AsciiString::EmptyString();
        // Use anEmptyStr instead of TCollection_AsciiString()
        ```
        @return const reference to static empty string
        """

    @overload
    @staticmethod
    def IsEqual_s(string1: TCollection_AsciiString, string2: TCollection_AsciiString) -> bool:
        """
        Returns True when the two strings are the same.
        (Just for HashCode for AsciiString)
        @param[in] string1 first string to compare
        @param[in] string2 second string to compare
        @return true if strings are equal
        """

    @overload
    @staticmethod
    def IsEqual_s(theString1: TCollection_AsciiString, theStringView: str) -> bool:
        """
        Returns True when the ASCII string and string_view are the same.
        (Just for HashCode for AsciiString)
        @param[in] theString1 first string to compare
        @param[in] theStringView second string view to compare
        @return true if strings are equal
        """

    @overload
    @staticmethod
    def IsEqual_s(theStringView: str, theString2: TCollection_AsciiString) -> bool:
        """
        Returns True when the string_view and ASCII string are the same.
        (Just for HashCode for AsciiString)
        @param[in] theStringView first string view to compare
        @param[in] theString2 second string to compare
        @return true if strings are equal
        """

    @overload
    @staticmethod
    def IsSameString(theString1: str, theLength1: int, theString2: str, theLength2: int, theIsCaseSensitive: bool) -> bool:
        """
        Core implementation: Returns True if the two strings (pointer and length) contain same
        characters. This is the primary implementation that all other IsSameString overloads redirect
        to.
        @param[in] theString1 pointer to first string to compare
        @param[in] theLength1 length of first string
        @param[in] theString2 pointer to second string to compare
        @param[in] theLength2 length of second string
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theString1: TCollection_AsciiString, theString2: TCollection_AsciiString, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the strings contain same characters.
        @param[in] theString1 first string to compare
        @param[in] theString2 second string to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theString1: TCollection_AsciiString, theCString: str, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the string and C string contain same characters.
        @param[in] theString1 first string to compare
        @param[in] theCString second C string to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theCString: str, theString2: TCollection_AsciiString, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the C string and string contain same characters.
        @param[in] theCString first C string to compare
        @param[in] theString2 second string to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theString1: TCollection_AsciiString, theStringView: str, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the string and string_view contain same characters.
        @param[in] theString1 first string to compare
        @param[in] theStringView second string view to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theStringView: str, theString2: TCollection_AsciiString, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the string_view and string contain same characters.
        @param[in] theStringView first string view to compare
        @param[in] theString2 second string to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theCString1: str, theCString2: str, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the two C strings contain same characters.
        @param[in] theCString1 first C string to compare
        @param[in] theCString2 second C string to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

    @overload
    @staticmethod
    def IsSameString(theStringView1: str, theStringView2: str, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the two string_views contain same characters.
        @param[in] theStringView1 first string view to compare
        @param[in] theStringView2 second string view to compare
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @return true if strings contain same characters
        """

class TCollection_ExtendedString:
    """
    A variable-length sequence of "extended" (UNICODE) characters (16-bit character type).
    It provides editing operations with built-in memory management
    to make ExtendedString objects easier to use than ordinary extended character arrays.
    ExtendedString objects follow "value semantics", that is, they are the actual strings,
    not handles to strings, and are copied through assignment.
    You may use HExtendedString objects to get handles to strings.

    Beware that class can transparently store UTF-16 string with surrogate pairs
    (Unicode symbol represented by two 16-bit code units).
    However, surrogate pairs are not considered by the following methods:
    - Method ::Length() return the number of 16-bit code units, not the number of Unicode symbols.
    - Methods taking/returning symbol index work with 16-bit code units, not true Unicode symbols,
    including ::Remove(), ::SetValue(), ::Value(), ::Search(), ::Trunc() and others.
    If application needs to process surrogate pairs, NCollection_UtfIterator<char16_t> class can be
    used for iterating through Unicode string (UTF-32 code unit will be returned for each position).
    """

    @overload
    def __init__(self) -> None:
        """Initializes an ExtendedString to an empty ExtendedString."""

    @overload
    def __init__(self, theString: str, theIsMultiByte: bool = False) -> None:
        """
        Creation by converting a CString to an extended string.
        If theIsMultiByte is true then the string is treated as having UTF-8 coding.
        If it is not a UTF-8 then theIsMultiByte is ignored and each character is
        copied to ExtCharacter.
        @param[in] theString the C string to convert
        @param[in] theIsMultiByte flag indicating UTF-8 coding
        """

    @overload
    def __init__(self, theString: str) -> None:
        """
        Creation by converting an ExtString (char16_t*) to an extended string.
        @param[in] theString the char16_t string to copy
        """

    @overload
    def __init__(self, theChar: str) -> None:
        """
        Initializes an ExtendedString with a single ASCII character.
        @param[in] theChar the ASCII character to initialize from
        """

    @overload
    def __init__(self, theChar: str) -> None:
        """
        Initializes an ExtendedString with a single extended character.
        @param[in] theChar the extended character to initialize from
        """

    @overload
    def __init__(self, theValue: int) -> None:
        """
        Initializes an ExtendedString with an integer value.
        @param[in] theValue the integer value to convert to string
        """

    @overload
    def __init__(self, theValue: float) -> None:
        """
        Initializes an ExtendedString with a real value.
        @param[in] theValue the real value to convert to string
        """

    @overload
    def __init__(self, theString: TCollection_ExtendedString) -> None:
        """
        Initializes an ExtendedString with another ExtendedString.
        @param[in] theString the string to copy from
        """

    @overload
    def __init__(self, theString: TCollection_AsciiString, theIsMultiByte: bool = True) -> None:
        """
        Creation by converting an AsciiString to an extended string.
        The string is treated as having UTF-8 coding.
        If it is not a UTF-8 or multi byte then each character is copied to ExtCharacter.
        @param[in] theString the ASCII string to convert
        @param[in] theIsMultiByte flag indicating UTF-8 coding
        """

    @overload
    def __init__(self, theLength: int, theFiller: str) -> None:
        """
        Initializes an ExtendedString with specified length space allocated
        and filled with filler character. This is useful for buffers.
        @param[in] theLength the length to allocate
        @param[in] theFiller the character to fill with
        """

    @overload
    def __init__(self, theString: str, theLength: int) -> None:
        """
        Initializes an ExtendedString with a char16_t string and explicit length.
        @param[in] theString the char16_t string to initialize from
        @param[in] theLength the length of the string
        """

    @overload
    def __init__(self, theFrom: nanoocp.Message.Message_Msg) -> None: ...

    @overload
    def AssignCat(self, theOther: TCollection_ExtendedString) -> None:
        """
        Appends the other extended string to this extended string.
        Note that this method is an alias of operator +=.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Hello");
        TCollection_ExtendedString anotherString(u" World");
        aString += anotherString;
        // Result: aString == u"Hello World"
        ```
        @param[in] theOther the string to append
        """

    @overload
    def AssignCat(self, theOther: int) -> None:
        """
        Appends the integer value to this extended string.
        @param[in] theOther the integer to append
        """

    @overload
    def AssignCat(self, theChar: str) -> None:
        """
        Appends the ASCII character to this extended string.
        @param[in] theChar the character to append
        """

    @overload
    def AssignCat(self, theOther: float) -> None:
        """
        Appends the real value to this extended string.
        @param[in] theOther the real value to append
        """

    @overload
    def AssignCat(self, theChar: str) -> None:
        """
        Appends the utf16 char to this extended string.
        @param[in] theChar the character to append
        """

    @overload
    def AssignCat(self, theString: str, theLength: int) -> None:
        """
        Core implementation: Appends char16_t string (pointer and length) to this extended string.
        This is the primary implementation that all other AssignCat overloads redirect to.
        @param[in] theString pointer to the string to append
        @param[in] theLength length of the string to append
        """

    @overload
    def AssignCat(self, theString: str) -> None:
        """
        Appends the char16_t string to this extended string.
        @param[in] theString the string to append
        """

    @overload
    def __iadd__(self, theOther: TCollection_ExtendedString) -> TCollection_ExtendedString: ...

    @overload
    def __iadd__(self, theOther: int) -> TCollection_ExtendedString: ...

    @overload
    def __iadd__(self, theChar: str) -> TCollection_ExtendedString: ...

    @overload
    def __iadd__(self, theOther: float) -> TCollection_ExtendedString: ...

    @overload
    def __iadd__(self, theString: str) -> TCollection_ExtendedString:
        """
        Appends the char16_t string to this extended string (alias of AssignCat()).
        """

    @overload
    def Cat(self, theOther: str, theLength: int) -> TCollection_ExtendedString:
        """
        Core implementation: Concatenates char16_t string (pointer and length)
        and returns a new string.
        @param[in] theOther pointer to the string to append
        @param[in] theLength length of the string to append
        @return new string with theOther appended
        """

    @overload
    def Cat(self, theOther: str) -> TCollection_ExtendedString:
        """
        Concatenates char16_t string and returns a new string.
        @param[in] theOther the null-terminated string to append
        @return new string with theOther appended
        """

    @overload
    def Cat(self, theOther: int) -> TCollection_ExtendedString:
        """
        Appends the integer value to this string and returns a new string.
        @param[in] theOther the integer to append
        @return new string with integer appended
        """

    @overload
    def Cat(self, theOther: float) -> TCollection_ExtendedString:
        """
        Appends the real value to this string and returns a new string.
        @param[in] theOther the real value to append
        @return new string with real value appended
        """

    @overload
    def Cat(self, theChar: str) -> TCollection_ExtendedString:
        """
        Appends a single ASCII character to this string and returns a new string.
        @param[in] theChar the ASCII character to append
        """

    @overload
    def Cat(self, theChar: str) -> TCollection_ExtendedString:
        """
        Appends a single extended (char16_t) character to this string and returns a new string.
        @param[in] theChar the extended character to append
        """

    @overload
    def Cat(self, theOther: TCollection_ExtendedString) -> TCollection_ExtendedString:
        """
        Appends the other extended string to this string and returns a new string.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Hello");
        TCollection_ExtendedString anotherString(u" World");
        TCollection_ExtendedString aResult = aString + anotherString;
        // Result: aResult == u"Hello World"
        ```
        @param[in] theOther the string to append
        @return new string with theOther appended
        """

    @overload
    def __add__(self, theOther: str) -> TCollection_ExtendedString: ...

    @overload
    def __add__(self, theOther: int) -> TCollection_ExtendedString: ...

    @overload
    def __add__(self, theOther: float) -> TCollection_ExtendedString: ...

    @overload
    def __add__(self, theChar: str) -> TCollection_ExtendedString: ...

    @overload
    def __add__(self, theChar: str) -> TCollection_ExtendedString: ...

    @overload
    def __add__(self, theOther: TCollection_ExtendedString) -> TCollection_ExtendedString: ...

    def ChangeAll(self, theChar: str, theNewChar: str) -> None:
        """
        Substitutes all the characters equal to theChar by theNewChar
        in this ExtendedString.
        The substitution can be case sensitive.
        If you don't use default case sensitive, no matter whether theChar is uppercase or not.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Histake");
        aString.ChangeAll(u'H', u'M');
        // Result: aString == u"Mistake"
        ```
        @param[in] theChar the character to replace
        @param[in] theNewChar the replacement character
        """

    def Clear(self) -> None:
        """
        Removes all characters contained in this string.
        This produces an empty ExtendedString.
        """

    @overload
    def Copy(self, theString: str, theLength: int) -> None:
        """
        Core implementation: Copy from a char16_t pointer with explicit length.
        @param[in] theString pointer to the string to copy
        @param[in] theLength length of the string to copy
        """

    @overload
    def Copy(self, theString: str) -> None:
        """
        Copy from a char16_t pointer.
        @param[in] theString the null-terminated string to copy
        """

    @overload
    def Copy(self, theFromWhere: TCollection_ExtendedString) -> None:
        """
        Copy theFromWhere to this string.
        Used as operator =

        Example:
        ```cpp
        TCollection_ExtendedString aString;
        TCollection_ExtendedString anotherString(u"Hello World");
        aString = anotherString;  // operator=
        // Result: aString == u"Hello World"
        ```
        @param[in] theFromWhere the string to copy from
        """

    def Swap(self, theOther: TCollection_ExtendedString) -> None:
        """
        Exchange the data of two strings (without reallocating memory).
        @param[in,out] theOther the string to exchange data with
        """

    @overload
    def Insert(self, theWhere: int, theWhat: str) -> None:
        """
        Insert a Character at position theWhere.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"hy not ?");
        aString.Insert(1, u'W');
        // Result: aString == u"Why not ?"
        ```
        @param[in] theWhere the position to insert at (1-based)
        @param[in] theWhat the character to insert
        """

    @overload
    def Insert(self, theWhere: int, theWhat: str, theLength: int) -> None:
        """
        Core implementation: Insert a char16_t string (pointer and length) at position theWhere.
        @param[in] theWhere the position to insert at (1-based)
        @param[in] theWhat pointer to the string to insert
        @param[in] theLength length of the string to insert
        """

    @overload
    def Insert(self, theWhere: int, theWhat: str) -> None:
        """
        Insert a char16_t string at position theWhere.
        @param[in] theWhere the position to insert at (1-based)
        @param[in] theWhat the null-terminated string to insert
        """

    @overload
    def Insert(self, theWhere: int, theWhat: TCollection_ExtendedString) -> None:
        """
        Insert an ExtendedString at position theWhere.
        @param[in] theWhere the position to insert at (1-based)
        @param[in] theWhat the string to insert
        """

    def IsEmpty(self) -> bool:
        """Returns True if this string contains no characters."""

    @overload
    def IsEqual(self, theOther: str, theLength: int) -> bool:
        """
        Core implementation: Returns true if this string equals theOther (pointer and length).
        @param[in] theOther pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def IsEqual(self, theOther: str) -> bool:
        """
        Returns true if this string equals theOther null-terminated string.
        Note that this method is an alias of operator ==.
        @param[in] theOther the char16_t string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def IsEqual(self, theOther: TCollection_ExtendedString) -> bool:
        """
        Returns true if the characters in this extended
        string are identical to the characters in theOther extended string.
        Note that this method is an alias of operator ==.
        @param[in] theOther the extended string to compare with
        @return true if strings are equal, false otherwise
        """

    @overload
    def __eq__(self, theOther: str) -> bool: ...

    @overload
    def __eq__(self, theOther: TCollection_ExtendedString) -> bool: ...

    @overload
    def IsDifferent(self, theOther: str, theLength: int) -> bool:
        """
        Core implementation: Returns true if this string differs from theOther (pointer and length).
        @param[in] theOther pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def IsDifferent(self, theOther: str) -> bool:
        """
        Returns true if this string differs from theOther null-terminated string.
        Note that this method is an alias of operator !=.
        @param[in] theOther the char16_t string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def IsDifferent(self, theOther: TCollection_ExtendedString) -> bool:
        """
        Returns true if there are differences between the
        characters in this extended string and theOther extended string.
        Note that this method is an alias of operator !=.
        @param[in] theOther the extended string to compare with
        @return true if strings are different, false otherwise
        """

    @overload
    def __ne__(self, theOther: str) -> bool: ...

    @overload
    def __ne__(self, theOther: TCollection_ExtendedString) -> bool: ...

    @overload
    def IsLess(self, theOther: str, theLength: int) -> bool:
        """
        Core implementation: Returns TRUE if this string is lexicographically less than theOther.
        @param[in] theOther pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if this string is less than theOther
        """

    @overload
    def IsLess(self, theOther: str) -> bool:
        """
        Returns TRUE if this string is lexicographically less than theOther.
        @param[in] theOther the char16_t string to compare with
        @return true if this string is less than theOther
        """

    @overload
    def IsLess(self, theOther: TCollection_ExtendedString) -> bool:
        """
        Returns TRUE if this string is lexicographically less than theOther.
        @param[in] theOther the extended string to compare with
        @return true if this string is less than theOther
        """

    @overload
    def __lt__(self, theOther: str) -> bool: ...

    @overload
    def __lt__(self, theOther: TCollection_ExtendedString) -> bool: ...

    @overload
    def IsGreater(self, theOther: str, theLength: int) -> bool:
        """
        Core implementation: Returns TRUE if this string is lexicographically greater than theOther.
        @param[in] theOther pointer to the string to compare with
        @param[in] theLength length of the string to compare with
        @return true if this string is greater than theOther
        """

    @overload
    def IsGreater(self, theOther: str) -> bool:
        """
        Returns TRUE if this string is lexicographically greater than theOther.
        @param[in] theOther the char16_t string to compare with
        @return true if this string is greater than theOther
        """

    @overload
    def IsGreater(self, theOther: TCollection_ExtendedString) -> bool:
        """
        Returns TRUE if this string is lexicographically greater than theOther.
        @param[in] theOther the extended string to compare with
        @return true if this string is greater than theOther
        """

    @overload
    def __gt__(self, theOther: str) -> bool: ...

    @overload
    def __gt__(self, theOther: TCollection_ExtendedString) -> bool: ...

    @overload
    def StartsWith(self, theStartString: str, theLength: int) -> bool:
        """
        Core implementation: Determines whether this string starts with theStartString.
        @param[in] theStartString pointer to the string to check for
        @param[in] theLength length of the string to check for
        @return true if this string starts with theStartString
        """

    @overload
    def StartsWith(self, theStartString: str) -> bool:
        """
        Determines whether this string starts with theStartString.
        @param[in] theStartString the null-terminated string to check for
        @return true if this string starts with theStartString
        """

    @overload
    def StartsWith(self, theStartString: TCollection_ExtendedString) -> bool:
        """
        Determines whether the beginning of this string instance matches the specified string.
        @param[in] theStartString the string to check for at the beginning
        @return true if this string starts with theStartString
        """

    @overload
    def EndsWith(self, theEndString: str, theLength: int) -> bool:
        """
        Core implementation: Determines whether this string ends with theEndString.
        @param[in] theEndString pointer to the string to check for
        @param[in] theLength length of the string to check for
        @return true if this string ends with theEndString
        """

    @overload
    def EndsWith(self, theEndString: str) -> bool:
        """
        Determines whether this string ends with theEndString.
        @param[in] theEndString the null-terminated string to check for
        @return true if this string ends with theEndString
        """

    @overload
    def EndsWith(self, theEndString: TCollection_ExtendedString) -> bool:
        """
        Determines whether the end of this string instance matches the specified string.
        @param[in] theEndString the string to check for at the end
        @return true if this string ends with theEndString
        """

    def IsAscii(self) -> bool:
        """
        Returns True if the ExtendedString contains only "Ascii Range" characters.
        @return true if string contains only ASCII characters
        """

    def Length(self) -> int:
        """
        Returns the number of 16-bit code units
        (might be greater than number of Unicode symbols if string contains surrogate pairs).
        @return the number of 16-bit code units
        """

    def Print(self) -> object:
        """
        Displays this string on a stream.
        @param[in] theStream the output stream
        """

    def RemoveAll(self, theWhat: str) -> None:
        """
        Removes every theWhat characters from this string.
        @param[in] theWhat the character to remove
        """

    def Remove(self, theWhere: int, theHowMany: int = 1) -> None:
        """
        Erases theHowMany characters from position theWhere, theWhere included.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Hello");
        aString.Remove(2, 2); // erases 2 characters from position 2
        // Result: aString == u"Hlo"
        ```
        @param[in] theWhere the position to start erasing from (1-based)
        @param[in] theHowMany the number of characters to erase
        """

    @overload
    def Search(self, theWhat: str, theLength: int) -> int:
        """
        Core implementation: Searches for theWhat (pointer and length) from the beginning.
        @param[in] theWhat pointer to the string to search for
        @param[in] theLength length of the string to search for
        @return the position of first match (1-based), or -1 if not found
        """

    @overload
    def Search(self, theWhat: str) -> int:
        """
        Searches for theWhat null-terminated string from the beginning.
        @param[in] theWhat the null-terminated string to search for
        @return the position of first match (1-based), or -1 if not found
        """

    @overload
    def Search(self, theWhat: TCollection_ExtendedString) -> int:
        """
        Searches an ExtendedString in this string from the beginning
        and returns position of first item theWhat matching.
        It returns -1 if not found.
        @param[in] theWhat the string to search for
        @return the position of first match (1-based), or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: str, theLength: int) -> int:
        """
        Core implementation: Searches for theWhat (pointer and length) from the end.
        @param[in] theWhat pointer to the string to search for
        @param[in] theLength length of the string to search for
        @return the position of first match from end (1-based), or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: str) -> int:
        """
        Searches for theWhat null-terminated string from the end.
        @param[in] theWhat the null-terminated string to search for
        @return the position of first match from end (1-based), or -1 if not found
        """

    @overload
    def SearchFromEnd(self, theWhat: TCollection_ExtendedString) -> int:
        """
        Searches an ExtendedString in this string from the end
        and returns position of first item theWhat matching.
        It returns -1 if not found.
        @param[in] theWhat the string to search for
        @return the position of first match from end (1-based), or -1 if not found
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: str) -> None:
        """
        Replaces one character in the ExtendedString at position theWhere.
        If theWhere is less than zero or greater than the length of this string
        an exception is raised.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Garbake");
        aString.SetValue(6, u'g');
        // Result: aString == u"Garbage"
        ```
        @param[in] theWhere the position to replace at (1-based)
        @param[in] theWhat the character to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: str, theLength: int) -> None:
        """
        Core implementation: Replaces a part of this string by char16_t string (pointer and length).
        @param[in] theWhere the position to start replacement (1-based)
        @param[in] theWhat pointer to the string to replace with
        @param[in] theLength length of the string to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: str) -> None:
        """
        Replaces a part of this string by a null-terminated char16_t string.
        @param[in] theWhere the position to start replacement (1-based)
        @param[in] theWhat the null-terminated string to replace with
        """

    @overload
    def SetValue(self, theWhere: int, theWhat: TCollection_ExtendedString) -> None:
        """
        Replaces a part of this string by another ExtendedString.
        @param[in] theWhere the position to start replacement (1-based)
        @param[in] theWhat the string to replace with
        """

    def SubString(self, theFromIndex: int, theToIndex: int) -> TCollection_ExtendedString:
        """
        Copies characters from this string starting from index theFromIndex
        to the index theToIndex (inclusive).
        Raises an exception if theToIndex or theFromIndex is out of bounds.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"abcdefg");
        TCollection_ExtendedString aSubString = aString.SubString(3, 6);
        // Result: aSubString == u"cdef"
        ```
        @param[in] theFromIndex the starting index (1-based)
        @param[in] theToIndex the ending index (1-based, inclusive)
        @return the substring from theFromIndex to theToIndex
        """

    def Split(self, theWhere: int) -> TCollection_ExtendedString:
        """
        Splits this extended string into two sub-strings at position theWhere.
        -   The second sub-string (from position theWhere + 1 of this string to the end) is
        returned in a new extended string.
        -   This extended string is modified: its last characters are removed, it becomes equal to
        the first sub-string (from the first character to position theWhere).

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"abcdefg");
        TCollection_ExtendedString aSecondPart = aString.Split(3);
        // Result: aString == u"abc" and aSecondPart == u"defg"
        ```
        @param[in] theWhere the position to split at (0-based)
        @return the second part of the split string
        """

    def Token(self, theSeparators: str, theWhichOne: int = 1) -> TCollection_ExtendedString:
        """
        Extracts theWhichOne token from this string.
        By default, the theSeparators is set to space and tabulation.
        By default, the token extracted is the first one (theWhichOne = 1).
        theSeparators contains all separators you need.
        If no token indexed by theWhichOne is found, it returns an empty ExtendedString.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"This is a     message");
        TCollection_ExtendedString aToken1 = aString.Token();
        // Result: aToken1 == u"This"

        TCollection_ExtendedString aToken2 = aString.Token(u" ", 4);
        // Result: aToken2 == u"message"

        TCollection_ExtendedString aToken3 = aString.Token(u" ", 2);
        // Result: aToken3 == u"is"

        TCollection_ExtendedString aToken4 = aString.Token(u" ", 9);
        // Result: aToken4 == u""

        TCollection_ExtendedString bString(u"1234; test:message   , value");
        TCollection_ExtendedString bToken1 = bString.Token(u"; :,", 4);
        // Result: bToken1 == u"value"
        ```
        @param[in] theSeparators the separator characters
        @param[in] theWhichOne the token number to extract (1-based)
        @return the extracted token
        """

    def ToExtString(self) -> str:
        """
        Returns pointer to ExtString (char16_t*).
        @return the char16_t string representation
        """

    def Trunc(self, theHowMany: int) -> None:
        """
        Truncates this string to theHowMany characters.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Hello Dolly");
        aString.Trunc(3);
        // Result: aString == u"Hel"
        ```
        @param[in] theHowMany the number of characters to keep
        """

    def Value(self, theWhere: int) -> str:
        """
        Returns character at position theWhere in this string.
        If theWhere is less than zero or greater than the length of
        this string, an exception is raised.

        Example:
        ```cpp
        TCollection_ExtendedString aString(u"Hello");
        char16_t aChar = aString.Value(2);
        // Result: aChar == u'e'
        ```
        @param[in] theWhere the position to get character from (1-based)
        @return the character at the specified position
        """

    def HashCode(self) -> int:
        """
        Returns a hashed value for the extended string.
        Note: if string is ASCII, the computed value is the same as the value computed with the
        HashCode function on a TCollection_AsciiString string composed with equivalent ASCII
        characters.
        @return a computed hash code
        """

    @staticmethod
    def EmptyString() -> TCollection_ExtendedString:
        """
        Returns a const reference to a single shared empty string instance.
        This method provides access to a static empty string to avoid creating temporary empty
        strings. Use this method instead of constructing empty strings when you need a const
        reference.

        Example:
        ```cpp
        const TCollection_ExtendedString& anEmptyStr = TCollection_ExtendedString::EmptyString();
        // Use anEmptyStr instead of TCollection_ExtendedString()
        ```
        @return const reference to static empty string
        """

    @staticmethod
    def IsEqual_s(theString1: TCollection_ExtendedString, theString2: TCollection_ExtendedString) -> bool:
        """
        Returns true if the characters in this extended
        string are identical to the characters in the other extended string.
        Note that this method is an alias of operator ==.
        @param[in] theString1 first string to compare
        @param[in] theString2 second string to compare
        @return true if strings are equal
        """

    def LengthOfCString(self) -> int:
        """
        Returns expected CString length in UTF8 coding (like strlen, without null terminator).
        It can be used for memory calculation before converting to CString containing symbols in UTF8
        coding. For external allocation, use: char* buf = new char[str.LengthOfCString() + 1];
        @return expected UTF-8 string length
        """

    def LeftAdjust(self) -> None:
        """Removes all space characters in the beginning of the string."""

    def RightAdjust(self) -> None:
        """Removes all space characters at the end of the string."""

    def LeftJustify(self, theWidth: int, theFiller: str) -> None:
        """
        Left justify.
        Length becomes equal to theWidth and the new characters are
        equal to theFiller.
        If theWidth < Length nothing happens.
        @param[in] theWidth the desired width of the string
        @param[in] theFiller the character to fill with
        """

    def RightJustify(self, theWidth: int, theFiller: str) -> None:
        """
        Right justify.
        Length becomes equal to theWidth and the new characters are
        equal to theFiller.
        If theWidth < Length nothing happens.
        @param[in] theWidth the desired width of the string
        @param[in] theFiller the character to fill with
        """

    def Center(self, theWidth: int, theFiller: str) -> None:
        """
        Modifies this string so that its length becomes equal to theWidth
        and the new characters are equal to theFiller.
        New characters are added both at the beginning and at the end of this string.
        If theWidth is less than the length of this string, nothing happens.
        @param[in] theWidth the desired width of the string
        @param[in] theFiller the character to fill with
        """

    def Capitalize(self) -> None:
        """
        Converts the first character into its corresponding
        upper-case character and the other characters into lowercase.
        @note Only ASCII characters (a-z, A-Z) are affected by case conversion.
        """

    @overload
    def Prepend(self, theOther: str, theLength: int) -> None:
        """
        Core implementation: Inserts char16_t string (pointer and length) at the beginning.
        @param[in] theOther pointer to the string to prepend
        @param[in] theLength length of the string to prepend
        """

    @overload
    def Prepend(self, theOther: str) -> None:
        """
        Inserts a null-terminated char16_t string at the beginning.
        @param[in] theOther the null-terminated string to prepend
        """

    @overload
    def Prepend(self, theOther: TCollection_ExtendedString) -> None:
        """
        Inserts the other extended string at the beginning of this string.
        @param[in] theOther the string to prepend
        """

    def FirstLocationInSet(self, theSet: TCollection_ExtendedString, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string that is
        present in theSet.
        The search begins at index theFromIndex and ends at index theToIndex.
        Returns zero if failure.
        @param[in] theSet the set of characters to search for
        @param[in] theFromIndex the starting index for search (1-based)
        @param[in] theToIndex the ending index for search (1-based)
        @return the index of first character found in set, or 0 if not found
        """

    def FirstLocationNotInSet(self, theSet: TCollection_ExtendedString, theFromIndex: int, theToIndex: int) -> int:
        """
        Returns the index of the first character of this string that is
        NOT present in theSet.
        The search begins at index theFromIndex and ends at index theToIndex.
        Returns zero if failure.
        @param[in] theSet the set of characters to check against
        @param[in] theFromIndex the starting index for search (1-based)
        @param[in] theToIndex the ending index for search (1-based)
        @return the index of first character not in set, or 0 if not found
        """

    def IntegerValue(self) -> int:
        """
        Converts this extended string containing a numeric expression to an Integer.
        @return the integer value
        """

    def IsIntegerValue(self) -> bool:
        """
        Returns True if this extended string contains an integer value.
        @return true if string represents an integer value
        """

    def RealValue(self) -> float:
        """
        Converts this extended string containing a numeric expression to a Real.
        @return the real value
        """

    def IsRealValue(self, theToCheckFull: bool = False) -> bool:
        """
        Returns True if this extended string starts with characters that can be
        interpreted as a real value.
        @param[in] theToCheckFull when TRUE, checks if entire string defines a real value;
        otherwise checks if string starts with a real value
        @return true if string represents a real value
        """

    def IsSameString(self, theOther: TCollection_ExtendedString, theIsCaseSensitive: bool) -> bool:
        """
        Returns True if the strings contain same characters.
        @param[in] theOther the string to compare with
        @param[in] theIsCaseSensitive flag indicating case sensitivity
        @note When case-insensitive, only ASCII characters (a-z, A-Z) are affected.
        @return true if strings contain same characters
        """

    def __hash__(self) -> int: ...

class TCollection_HAsciiString(nanoocp.Standard.Standard_Transient):
    """
    A variable-length sequence of ASCII characters
    (normal 8-bit character type). It provides editing
    operations with built-in memory management to
    make HAsciiString objects easier to use than ordinary character arrays.
    HAsciiString objects are handles to strings.
    -   HAsciiString strings may be shared by several objects.
    -   You may use an AsciiString object to get the actual string.
    Note: HAsciiString objects use an AsciiString string as a field.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a HAsciiString to an empty AsciiString."""

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a HAsciiString with a CString."""

    @overload
    def __init__(self, aChar: str) -> None:
        """Initializes a HAsciiString with a single character."""

    @overload
    def __init__(self, value: int) -> None:
        """Initializes a HAsciiString with an integer value"""

    @overload
    def __init__(self, value: float) -> None:
        """Initializes a HAsciiString with a real value"""

    @overload
    def __init__(self, aString: TCollection_AsciiString) -> None:
        """Initializes a HAsciiString with a AsciiString."""

    @overload
    def __init__(self, aString: TCollection_HAsciiString) -> None:
        """Initializes a HAsciiString with a HAsciiString."""

    @overload
    def __init__(self, length: int, filler: str) -> None:
        """
        Initializes a HAsciiString with <length> space allocated.
        and filled with <filler>.This is useful for buffers.
        """

    @overload
    def __init__(self, aString: TCollection_HExtendedString, replaceNonAscii: str) -> None:
        """
        Initializes a HAsciiString with a HExtendedString.
        If replaceNonAscii is non-null character, it will be used
        in place of any non-ascii character found in the source string.
        Otherwise, creates UTF-8 unicode string.
        """

    @overload
    def __init__(self, theOther: TCollection_HAsciiString) -> None: ...

    @overload
    def AssignCat(self, other: str) -> None:
        """Appends <other> to me."""

    @overload
    def AssignCat(self, other: TCollection_HAsciiString) -> None:
        """
        Appends <other> to me.
        Example: aString = aString + anotherString
        """

    def Capitalize(self) -> None:
        """
        Converts the first character into its corresponding
        upper-case character and the other characters into lowercase.
        Example:
        before
        me = "hellO "
        after
        me = "Hello \"
        """

    @overload
    def Cat(self, other: str) -> TCollection_HAsciiString:
        """
        Creates a new string by concatenation of this
        ASCII string and the other ASCII string.
        Example:
        aString = aString + anotherString
        aString = aString + "Dummy"
        aString contains "I say "
        aString = aString + "Hello " + "Dolly"
        gives "I say Hello Dolly"
        Warning: To catenate more than one CString, you must put a String before.
        So the following example is WRONG !
        aString = "Hello " + "Dolly"  THIS IS NOT ALLOWED
        This rule is applicable to AssignCat (operator +=) too.
        """

    @overload
    def Cat(self, other: TCollection_HAsciiString) -> TCollection_HAsciiString:
        """
        Creates a new string by concatenation of this
        ASCII string and the other ASCII string.
        Example: aString = aString + anotherString
        """

    def Center(self, Width: int, Filler: str) -> None:
        """
        Modifies this ASCII string so that its length
        becomes equal to Width and the new characters
        are equal to Filler. New characters are added
        both at the beginning and at the end of this string.
        If Width is less than the length of this ASCII string, nothing happens.
        Example
        occ::handle<TCollection_HAsciiString>
        myAlphabet
        = new
        TCollection_HAsciiString
        ("abcdef");
        myAlphabet->Center(9,' ');
        assert ( !strcmp(
        myAlphabet->ToCString(),
        " abcdef ") );
        """

    def ChangeAll(self, aChar: str, NewChar: str, CaseSensitive: bool = True) -> None:
        """
        Replaces all characters equal to aChar by
        NewChar in this ASCII string. The substitution is
        case sensitive if CaseSensitive is true (default value).
        If you do not use the default case sensitive
        option, it does not matter whether aChar is upper-case or not.
        Example
        occ::handle<TCollection_HAsciiString>
        myMistake = new
        TCollection_HAsciiString
        ("Hather");
        myMistake->ChangeAll('H','F');
        assert ( !strcmp(
        myMistake->ToCString(),
        "Father") );
        """

    def Clear(self) -> None:
        """
        Removes all characters contained in <me>.
        This produces an empty HAsciiString.
        """

    def FirstLocationInSet(self, Set: TCollection_HAsciiString, FromIndex: int, ToIndex: int) -> int:
        """
        Returns the index of the first character of <me> that is
        present in <Set>.
        The search begins to the index FromIndex and ends to the
        the index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range
        Example:
        before
        me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7
        after
        me = "aabAcAa"
        returns
        1
        """

    def FirstLocationNotInSet(self, Set: TCollection_HAsciiString, FromIndex: int, ToIndex: int) -> int:
        """
        Returns the index of the first character of <me>
        that is not present in the set <Set>.
        The search begins to the index FromIndex and ends to the
        the index ToIndex in <me>.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range.
        Example:
        before
        me = "aabAcAa", S = "Aa", FromIndex = 1, Toindex = 7
        after
        me = "aabAcAa"
        returns
        3
        """

    @overload
    def Insert(self, where: int, what: str) -> None:
        """
        Insert a Character at position <where>.
        Example:
        aString contains "hy not ?"
        aString.Insert(1,'W'); gives "Why not ?"
        aString contains "Wh"
        aString.Insert(3,'y'); gives "Why"
        aString contains "Way"
        aString.Insert(2,'h'); gives "Why\"
        """

    @overload
    def Insert(self, where: int, what: str) -> None: ...

    @overload
    def Insert(self, where: int, what: TCollection_HAsciiString) -> None:
        """Insert a HAsciiString at position <where>."""

    def InsertAfter(self, Index: int, other: TCollection_HAsciiString) -> None:
        """
        Inserts the other ASCII string a after a specific index in the string <me>
        Example:
        before
        me = "cde" , Index = 0 , other = "ab"
        after
        me = "abcde" , other = "ab\"
        """

    def InsertBefore(self, Index: int, other: TCollection_HAsciiString) -> None:
        """
        Inserts the other ASCII string a before a specific index in the string <me>
        Raises an exception if Index is out of bounds
        Example:
        before
        me = "cde" , Index = 1 , other = "ab"
        after
        me = "abcde" , other = "ab\"
        """

    def IsEmpty(self) -> bool:
        """Returns True if the string <me> contains zero character"""

    def IsLess(self, other: TCollection_HAsciiString) -> bool:
        """Returns TRUE if <me> is 'ASCII' less than <other>."""

    def IsGreater(self, other: TCollection_HAsciiString) -> bool:
        """Returns TRUE if <me> is 'ASCII' greater than <other>."""

    def IntegerValue(self) -> int:
        """
        Converts a HAsciiString containing a numeric expression to
        an Integer.
        Example: "215" returns 215.
        """

    def IsIntegerValue(self) -> bool:
        """Returns True if the string contains an integer value."""

    def IsRealValue(self) -> bool:
        """Returns True if the string contains a real value."""

    def IsAscii(self) -> bool:
        """
        Returns True if the string contains only ASCII characters
        between ' ' and '~'.
        This means no control character and no extended ASCII code.
        """

    def IsDifferent(self, S: TCollection_HAsciiString) -> bool:
        """
        Returns True if the string S not contains same characters than
        the string <me>.
        """

    @overload
    def IsSameString(self, S: TCollection_HAsciiString) -> bool: ...

    @overload
    def IsSameString(self, S: TCollection_HAsciiString, CaseSensitive: bool) -> bool:
        """
        Returns True if the string S contains same characters than the
        string <me>.
        """

    def LeftAdjust(self) -> None:
        """Removes all space characters in the beginning of the string"""

    def LeftJustify(self, Width: int, Filler: str) -> None:
        """
        Left justify.
        Length becomes equal to Width and the new characters are
        equal to Filler
        if Width < Length nothing happens
        Raises an exception if Width is less than zero
        Example:
        before
        me = "abcdef" , Width = 9 , Filler = ' '
        after
        me = "abcdef   \"
        """

    def Length(self) -> int:
        """
        Returns number of characters in <me>.
        This is the same functionality as 'strlen' in C.
        """

    @overload
    def Location(self, other: TCollection_HAsciiString, FromIndex: int, ToIndex: int) -> int:
        """
        returns an index in the string <me> of the first occurrence
        of the string S in the string <me> from the starting index
        FromIndex to the ending index ToIndex
        returns zero if failure
        Raises an exception if FromIndex or ToIndex is out of range.
        Example:
        before
        me = "aabAaAa", S = "Aa", FromIndex = 1, ToIndex = 7
        after
        me = "aabAaAa"
        returns
        4
        """

    @overload
    def Location(self, N: int, C: str, FromIndex: int, ToIndex: int) -> int:
        """
        Returns the index of the nth occurrence of the character C
        in the string <me> from the starting index FromIndex to the
        ending index ToIndex.
        Returns zero if failure.
        Raises an exception if FromIndex or ToIndex is out of range
        Example:
        before
        me = "aabAa", N = 3, C = 'a', FromIndex = 1, ToIndex = 5
        after
        me = "aabAa"
        returns 5
        """

    def LowerCase(self) -> None:
        """Converts <me> to its lower-case equivalent."""

    def Prepend(self, other: TCollection_HAsciiString) -> None:
        """
        Inserts the other string at the beginning of the string <me>
        Example:
        before
        me = "cde" , S = "ab"
        after
        me = "abcde" , S = "ab\"
        """

    def Print(self) -> object:
        """Prints this string on the stream <astream>."""

    def RealValue(self) -> float:
        """
        Converts a string containing a numeric expression to a Real.
        Example:
        "215" returns 215.0.
        "3.14159267" returns 3.14159267.
        """

    @overload
    def RemoveAll(self, C: str, CaseSensitive: bool) -> None:
        """
        Remove all the occurrences of the character C in the string
        Example:
        before
        me = "HellLLo", C = 'L' , CaseSensitive = True
        after
        me = "Hello\"
        """

    @overload
    def RemoveAll(self, what: str) -> None:
        """Removes every <what> characters from <me>"""

    def Remove(self, where: int, ahowmany: int = 1) -> None:
        """
        Erases <ahowmany> characters from position <where>,
        <where> included.
        Example:
        aString contains "Hello"
        aString.Erase(2,2) erases 2 characters from position 1
        This gives "Hlo".
        """

    def RightAdjust(self) -> None:
        """Removes all space characters at the end of the string."""

    def RightJustify(self, Width: int, Filler: str) -> None:
        """
        Right justify.
        Length becomes equal to Width and the new characters are
        equal to Filler
        if Width < Length nothing happens
        Raises an exception if Width is less than zero
        Example:
        before
        me = "abcdef" , Width = 9 , Filler = ' '
        after
        me = "   abcdef\"
        """

    @overload
    def Search(self, what: str) -> int:
        """
        Searches a CString in <me> from the beginning
        and returns position of first item <what> matching.
        It returns -1 if not found.
        Example:
        aString contains "Sample single test"
        aString.Search("le") returns 5
        """

    @overload
    def Search(self, what: TCollection_HAsciiString) -> int:
        """
        Searches a String in <me> from the beginning
        and returns position of first item <what> matching.
        it returns -1 if not found.
        """

    @overload
    def SearchFromEnd(self, what: str) -> int:
        """
        Searches a CString in a String from the end
        and returns position of first item <what> matching.
        It returns -1 if not found.
        Example:
        aString contains "Sample single test"
        aString.SearchFromEnd("le") returns 12
        """

    @overload
    def SearchFromEnd(self, what: TCollection_HAsciiString) -> int:
        """
        Searches a HAsciiString in another HAsciiString from the end
        and returns position of first item <what> matching.
        It returns -1 if not found.
        """

    @overload
    def SetValue(self, where: int, what: str) -> None:
        """
        Replaces one character in the string at position <where>.
        If <where> is less than zero or greater than the length of <me>
        an exception is raised.
        Example:
        aString contains "Garbake"
        astring.Replace(6,'g')  gives <me> = "Garbage\"
        """

    @overload
    def SetValue(self, where: int, what: str) -> None:
        """
        Replaces a part of <me> in the string at position <where>.
        If <where> is less than zero or greater than the length of <me>
        an exception is raised.
        Example:
        aString contains "Garbake"
        astring.Replace(6,'g')  gives <me> = "Garbage\"
        """

    @overload
    def SetValue(self, where: int, what: TCollection_HAsciiString) -> None:
        """Replaces a part of <me> by another string."""

    def Split(self, where: int) -> TCollection_HAsciiString:
        """
        Splits a HAsciiString into two sub-strings.
        Example:
        aString contains "abcdefg"
        aString.Split(3) gives <me> = "abc" and returns "defg\"
        """

    def SubString(self, FromIndex: int, ToIndex: int) -> TCollection_HAsciiString:
        """
        Creation of a sub-string of the string <me>.
        The sub-string starts to the index Fromindex and ends
        to the index ToIndex.
        Raises an exception if ToIndex or FromIndex is out of
        bounds
        Example:
        before
        me = "abcdefg", ToIndex=3, FromIndex=6
        after
        me = "abcdefg"
        returns
        "cdef\"
        """

    def ToCString(self) -> str:
        """
        Returns pointer to string (char *)
        This is useful for some casual manipulations
        Because this "char *" is 'const', you can't modify its contents.
        """

    def Token(self, separators: str = ' \t', whichone: int = 1) -> TCollection_HAsciiString:
        """
        Extracts <whichone> token from <me>.
        By default, the <separators> is set to space and tabulation.
        By default, the token extracted is the first one (whichone = 1).
        <separators> contains all separators you need.
        If no token indexed by <whichone> is found, it returns an empty String.
        Example:
        aString contains "This is a     message"
        aString.Token()  returns "This"
        aString.Token(" ",4) returns "message"
        aString.Token(" ",2) returns "is"
        aString.Token(" ",9) returns ""
        Other separators than space character and tabulation are allowed
        aString contains "1234; test:message   , value"
        aString.Token("; :,",4) returns "value"
        aString.Token("; :,",2) returns "test\"
        """

    def Trunc(self, ahowmany: int) -> None:
        """
        Truncates <me> to <ahowmany> characters.
        Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel\"
        """

    def UpperCase(self) -> None:
        """Converts <me> to its upper-case equivalent."""

    def UsefullLength(self) -> int:
        """
        Length of the string ignoring all spaces (' ') and the
        control character at the end.
        """

    def Value(self, where: int) -> str:
        """
        Returns character at position <where> in <me>.
        If <where> is less than zero or greater than the length of
        <me>, an exception is raised.
        Example:
        aString contains "Hello"
        aString.Value(2) returns 'e'
        """

    def String(self) -> TCollection_AsciiString:
        """Returns the field myString."""

    def IsSameState(self, other: TCollection_HAsciiString) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...

class TCollection_HExtendedString(nanoocp.Standard.Standard_Transient):
    """
    A variable-length sequence of "extended"
    (UNICODE) characters (16-bit character
    type). It provides editing operations with
    built-in memory management to make
    ExtendedString objects easier to use than
    ordinary extended character arrays.
    HExtendedString objects are handles to strings.
    - HExtendedString strings may be shared by several objects.
    - You may use an ExtendedString object to get the actual string.
    Note: HExtendedString objects use an
    ExtendedString string as a field.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a HExtendedString to an empty ExtendedString."""

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a HExtendedString with a CString."""

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a HExtendedString with an ExtString."""

    @overload
    def __init__(self, aChar: str) -> None:
        """Initializes a HExtendedString with a single character."""

    @overload
    def __init__(self, aString: TCollection_ExtendedString) -> None:
        """Initializes a HExtendedString with a ExtendedString."""

    @overload
    def __init__(self, aString: TCollection_HAsciiString) -> None:
        """Initializes a HExtendedString with an HAsciiString."""

    @overload
    def __init__(self, aString: TCollection_HExtendedString) -> None:
        """Initializes a HExtendedString with a HExtendedString."""

    @overload
    def __init__(self, length: int, filler: str) -> None:
        """
        Initializes a HExtendedString with <length> space allocated.
        and filled with <filler>. This is useful for buffers.
        """

    @overload
    def __init__(self, theOther: TCollection_HExtendedString) -> None: ...

    def AssignCat(self, other: TCollection_HExtendedString) -> None:
        """Appends <other> to me."""

    def Cat(self, other: TCollection_HExtendedString) -> TCollection_HExtendedString:
        """Returns a string appending <other> to me."""

    def ChangeAll(self, aChar: str, NewChar: str) -> None:
        """
        Substitutes all the characters equal to aChar by NewChar
        in the string <me>.
        """

    def Clear(self) -> None:
        """
        Removes all characters contained in <me>.
        This produces an empty ExtendedString.
        """

    def IsEmpty(self) -> bool:
        """Returns True if the string <me> contains zero character"""

    @overload
    def Insert(self, where: int, what: str) -> None:
        """
        Insert a ExtCharacter at position <where>.
        Example:
        aString contains "hy not ?"
        aString.Insert(1,'W'); gives "Why not ?"
        aString contains "Wh"
        aString.Insert(3,'y'); gives "Why"
        aString contains "Way"
        aString.Insert(2,'h'); gives "Why\"
        """

    @overload
    def Insert(self, where: int, what: TCollection_HExtendedString) -> None:
        """Insert a HExtendedString at position <where>."""

    def IsLess(self, other: TCollection_HExtendedString) -> bool:
        """Returns TRUE if <me> is less than <other>."""

    def IsGreater(self, other: TCollection_HExtendedString) -> bool:
        """Returns TRUE if <me> is greater than <other>."""

    def IsAscii(self) -> bool:
        """Returns True if the string contains only "Ascii Range" characters"""

    def Length(self) -> int:
        """
        Returns number of characters in <me>.
        This is the same functionality as 'strlen' in C.
        """

    def Remove(self, where: int, ahowmany: int = 1) -> None:
        """
        Erases <ahowmany> characters from position <where>,
        <where> included.
        Example:
        aString contains "Hello"
        aString.Erase(2,2) erases 2 characters from position 1
        This gives "Hlo".
        """

    def RemoveAll(self, what: str) -> None:
        """Removes every <what> characters from <me>."""

    @overload
    def SetValue(self, where: int, what: str) -> None:
        """
        Replaces one character in the string at position <where>.
        If <where> is less than zero or greater than the length of <me>
        an exception is raised.
        Example:
        aString contains "Garbake"
        astring.Replace(6,'g') gives <me> = "Garbage\"
        """

    @overload
    def SetValue(self, where: int, what: TCollection_HExtendedString) -> None:
        """Replaces a part of <me> by another string."""

    def Split(self, where: int) -> TCollection_HExtendedString:
        """
        Splits a ExtendedString into two sub-strings.
        Example:
        aString contains "abcdefg"
        aString.Split(3) gives <me> = "abc" and returns "defg\"
        """

    def Search(self, what: TCollection_HExtendedString) -> int:
        """
        Searches a String in <me> from the beginning
        and returns position of first item <what> matching.
        It returns -1 if not found.
        """

    def SearchFromEnd(self, what: TCollection_HExtendedString) -> int:
        """
        Searches a ExtendedString in another ExtendedString from the end
        and returns position of first item <what> matching.
        It returns -1 if not found.
        """

    def ToExtString(self) -> str:
        """Returns pointer to ExtString"""

    def Token(self, separators: str, whichone: int = 1) -> TCollection_HExtendedString:
        """
        Extracts <whichone> token from <me>.
        By default, the <separators> is set to space and tabulation.
        By default, the token extracted is the first one (whichone = 1).
        <separators> contains all separators you need.
        If no token indexed by <whichone> is found, it returns an empty String.
        Example:
        aString contains "This is a     message"
        aString.Token()  returns "This"
        aString.Token(" ",4) returns "message"
        aString.Token(" ",2) returns "is"
        aString.Token(" ",9) returns ""
        Other separators than space character and tabulation are allowed
        aString contains "1234; test:message   , value"
        aString.Token("; :,",4) returns "value"
        aString.Token("; :,",2) returns "test\"
        """

    def Trunc(self, ahowmany: int) -> None:
        """
        Truncates <me> to <ahowmany> characters.
        Example: me = "Hello Dolly" -> Trunc(3) -> me = "Hel\"
        """

    def Value(self, where: int) -> str:
        """
        Returns ExtCharacter at position <where> in <me>.
        If <where> is less than zero or greater than the length of
        <me>, an exception is raised.
        Example:
        aString contains "Hello"
        aString.Value(2) returns 'e'
        """

    def String(self) -> TCollection_ExtendedString:
        """Returns the field myString"""

    def Print(self) -> object:
        """Displays <me>."""

    def IsSameState(self, other: TCollection_HExtendedString) -> bool: ...

    @staticmethod
    def get_type_name() -> str: ...

    @staticmethod
    def get_type_descriptor() -> nanoocp.Standard.Standard_Type: ...

    def DynamicType(self) -> nanoocp.Standard.Standard_Type: ...
