"""NCollection container templates: which hand-written binder (src/cpp/common/nanocct_ncollection.h) serves which
template, which template members it implements and which it knowingly skips (the coverage check in ncollection.py
reads both), which other instantiations it requires (HSequence<T> needs Sequence<T>), and the defaulted template
arguments that are dropped from an instantiation's key and name (Design.md 6a). Data only: no libclang here, so
parse.py and the stub generator can import it without a cycle.
"""
from __future__ import annotations

# template name -> binder function (namespace nanocct) and the members the binder implements
BINDERS: dict[str, dict] = {
    "NCollection_Array1": {
        "binder": "nanocct::bind_NCollection_Array1",
        "members": {"Init", "Size", "Length", "IsEmpty", "Lower", "Upper", "IsDeletable", "Assign", "CopyValues", "First",
                    "Last", "Value", "At", "SetValue", "UpdateLowerBound", "UpdateUpperBound", "Resize", "operator()",
                    "operator[]", "ChangeFirst", "ChangeLast", "ChangeValue", "ChangeAt"},
        # members knowingly not bound
        "skipped": {"Move", "operator=", "EmplaceValue", "begin", "cbegin", "end", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": [],
        "nargs": 1,                # template parameters without default (the ones spelled in the docs)
    },
    "NCollection_List": {
        "binder": "nanocct::bind_NCollection_List",
        "members": {"Extent", "Length", "Size", "IsEmpty", "Allocator", "Assign", "Clear", "First", "Last", "Append", "Prepend",
                    "RemoveFirst", "Remove", "InsertBefore", "InsertAfter", "Reverse", "Exchange", "Contains"},
        "skipped": {"operator=", "EmplaceAppend", "EmplacePrepend", "EmplaceBefore", "EmplaceAfter", "begin", "end", "cbegin",
                    "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "ChangeValue", "Initialize"}},
        "nested_from": {"Iterator": "NCollection_TListIterator"},
        "bases": ["NCollection_BaseList"],       # non-template bases whose public members are inherited
        "requires": [],
        "nargs": 1,
    },
    "NCollection_Sequence": {
        "binder": "nanocct::bind_NCollection_Sequence",
        "members": {"Length", "Size", "IsEmpty", "Lower", "Upper", "Allocator", "Reverse", "Exchange", "Clear", "Assign",
                    "Remove", "Append", "Prepend", "InsertBefore", "InsertAfter", "Split", "First", "ChangeFirst", "Last",
                    "ChangeLast", "Value", "operator()", "ChangeValue", "SetValue", "At", "ChangeAt"},
        "skipped": {"operator=", "delNode", "EmplaceAppend", "EmplacePrepend", "EmplaceAfter", "EmplaceBefore", "begin", "end",
                    "cbegin", "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "ChangeValue"}},
        "bases": ["NCollection_BaseSequence"],
        "requires": [],
        "nargs": 1,
    },
    "NCollection_HSequence": {
        "binder": "nanocct::bind_NCollection_HSequence",
        "members": {"Sequence", "ChangeSequence", "Append", "get_type_name", "get_type_descriptor", "DynamicType"},
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Sequence"],
        "nargs": 1,
    },
    "NCollection_Map": {
        "binder": "nanocct::bind_NCollection_Map",
        "members": {"NbBuckets", "Extent", "Length", "Size", "IsEmpty", "Allocator", "Exchange", "Assign", "ReSize", "Add", "Added",
                    "Contains", "Remove", "Clear", "IsEqual", "Union", "Unite", "HasIntersection", "Intersection", "Intersect",
                    "Subtraction", "Subtract", "Difference", "Differ"},
        "skipped": {"GetHasher", "Contained", "operator=", "Emplace", "Emplaced", "TryEmplace", "TryEmplaced", "begin", "end", "cbegin",
                    "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "Key", "Initialize", "Reset"}},
        "bases": ["NCollection_BaseMap"],
        "requires": [],
        "nargs": 2,
        "defaults": {1: "NCollection_DefaultHasher<{0}>"},      # trailing arguments equal to their default are dropped
    },
    "NCollection_DataMap": {
        "binder": "nanocct::bind_NCollection_DataMap",
        "members": {"NbBuckets", "Extent", "Length", "Size", "IsEmpty", "Allocator", "Exchange", "Assign", "ReSize", "Bind", "Bound",
                    "TryBind", "TryBound", "IsBound", "UnBind", "Seek", "Find", "operator()", "ChangeSeek", "ChangeFind", "Clear"},
        "skipped": {"GetHasher", "Contained", "Items", "operator=", "Emplace", "Emplaced", "TryEmplace", "TryEmplaced", "begin", "end",
                    "cbegin", "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "ChangeValue", "Key", "Initialize", "Reset"}},
        "bases": ["NCollection_BaseMap"],
        "requires": [],
        "nargs": 3,
        "defaults": {2: "NCollection_DefaultHasher<{0}>"},
    },
    "NCollection_IndexedMap": {
        "binder": "nanocct::bind_NCollection_IndexedMap",
        "members": {"NbBuckets", "Extent", "Length", "Size", "IsEmpty", "Allocator", "Exchange", "Assign", "ReSize", "Add", "Added",
                    "Contains", "Substitute", "Swap", "RemoveLast", "RemoveFromIndex", "RemoveKey", "FindKey", "operator()",
                    "FindIndex", "Clear"},
        "skipped": {"GetHasher", "Contained", "IndexedItems", "operator=", "Emplace", "Emplaced", "TryEmplace", "TryEmplaced", "begin",
                    "end", "cbegin", "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "Index", "IsEqual"}},
        "bases": ["NCollection_BaseMap"],
        "requires": [],
        "nargs": 2,
        "defaults": {1: "NCollection_DefaultHasher<{0}>"},
    },
    "NCollection_IndexedDataMap": {
        "binder": "nanocct::bind_NCollection_IndexedDataMap",
        "members": {"NbBuckets", "Extent", "Length", "Size", "IsEmpty", "Allocator", "Exchange", "Assign", "ReSize", "Add", "TryBound",
                    "TryBind", "Bind", "Bound", "Contains", "Substitute", "Swap", "RemoveLast", "RemoveFromIndex", "RemoveKey", "FindKey",
                    "FindFromIndex", "operator()", "ChangeFromIndex", "FindIndex", "FindFromKey", "ChangeFromKey", "Seek", "ChangeSeek",
                    "Clear"},
        "skipped": {"GetHasher", "Contained", "Items", "IndexedItems", "operator=", "Emplace", "Emplaced", "TryEmplace", "TryEmplaced",
                    "begin", "end", "cbegin", "cend", "operator new", "operator delete", "operator new[]", "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Value", "ChangeValue", "Key", "Index", "IsEqual"}},
        "bases": ["NCollection_BaseMap"],
        "requires": [],
        "nargs": 3,
        "defaults": {2: "NCollection_DefaultHasher<{0}>"},
    },
    "NCollection_Array2": {
        "binder": "nanocct::bind_NCollection_Array2",
        "members": {"BeginPosition", "LastPosition", "Size", "Length", "NbRows", "NbColumns", "RowLength", "ColLength", "LowerRow",
                    "UpperRow", "LowerCol", "UpperCol", "UpdateLowerRow", "UpdateLowerCol", "UpdateUpperRow", "UpdateUpperCol",
                    "Assign", "CopyValues", "Value", "operator()", "ChangeValue", "SetValue", "At", "ChangeAt", "Resize", "ResizeWithTrim"},
        "skipped": {"Move", "operator=", "EmplaceValue", "begin", "end", "cbegin", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array1"],    # Array2<T> derives from Array1<T>
        "nargs": 1,
    },
    "NCollection_HArray2": {
        "binder": "nanocct::bind_NCollection_HArray2",
        "members": {"Array2", "ChangeArray2", "get_type_name", "get_type_descriptor", "DynamicType"},
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array2"],
        "nargs": 1,
    },
    "NCollection_DynamicArray": {
        "binder": "nanocct::bind_NCollection_DynamicArray",
        "members": {"Size", "Length", "Lower", "Upper", "IsEmpty", "Assign", "Append", "InsertAfter", "InsertBefore", "EraseLast",
                    "Appended", "operator()", "operator[]", "Value", "First", "ChangeFirst", "Last", "ChangeLast", "ChangeValue",
                    "SetValue", "Clear", "SetIncrement"},
        "skipped": {"operator=", "EmplaceAppend", "EmplaceValue", "begin", "end", "cbegin", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": [],
        "nargs": 1,
    },
    "NCollection_LinearVector": {
        "binder": "nanocct::bind_NCollection_LinearVector",
        "members": {"Data", "HasData", "Empty", "MaxSize", "Size", "IsEmpty", "Capacity", "Reserve", "Resize", "Value", "ChangeValue",
                    "operator()", "operator[]", "First", "ChangeFirst", "Last", "ChangeLast", "Append", "Appended", "SetValue",
                    "InsertBefore", "InsertAfter", "EraseLast", "Erase", "Clear", "ToArray1"},
        "skipped": {"operator=", "EmplaceAppend", "begin", "end", "cbegin", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array1"],    # ToArray1() returns NCollection_Array1<T>
        "nargs": 1,
    },
    "NCollection_DoubleMap": {
        "binder": "nanocct::bind_NCollection_DoubleMap",
        "members": {"NbBuckets", "Extent", "Length", "Size", "IsEmpty", "Allocator", "Exchange", "Assign", "ReSize", "Bind", "TryBind",
                    "AreBound", "IsBound1", "IsBound2", "UnBind1", "UnBind2", "Find1", "Seek1", "Find2", "Seek2", "Clear"},
        "skipped": {"operator=", "TryEmplace", "begin", "end", "cbegin", "cend", "operator new", "operator delete", "operator new[]",
                    "operator delete[]"},
        "nested": {"Iterator": {"ctor", "More", "Next", "Key1", "Key2", "Value", "Initialize", "Reset"}},
        "bases": ["NCollection_BaseMap"],
        "requires": [],
        "nargs": 4,
        "defaults": {2: "NCollection_DefaultHasher<{0}>", 3: "NCollection_DefaultHasher<{1}>"},
    },
    "NCollection_Shared": {
        "binder": "nanocct::bind_NCollection_Shared",
        "members": set(),
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": [],
        "nargs": 1,                # the second parameter is an enable_if guard
        "wraps": True,             # NCollection_Shared<T> derives from T: T must be bound (class or instantiation)
    },
    "NCollection_HArray1": {
        "binder": "nanocct::bind_NCollection_HArray1",
        "members": {"Array1", "ChangeArray1", "get_type_name", "get_type_descriptor", "DynamicType"},
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array1"],    # bound first, with the same element type
        "nargs": 1,
    },
}

def instance_args(tmpl: str, canonical_args: list[str]) -> list[str]:
    """Template arguments that identify an instantiation: all non-default ones plus trailing ones that differ
    from their default (a custom hasher stays part of the key/name, the default hasher does not)."""
    info = BINDERS[tmpl]
    args = list(canonical_args[: info["nargs"]])
    defaults = info.get("defaults", {})
    while len(args) > 0 and (len(args) - 1) in defaults and args[-1] == defaults[len(args) - 1].format(*args):
        args.pop()
    return args
