"""NCollection container templates: which hand-written binder (src/cpp/common/nanoocp_ncollection.h)
serves which template, docstring extraction from the template headers, and a coverage check."""
from __future__ import annotations

import re
from pathlib import Path

from clang import cindex
from clang.cindex import AccessSpecifier as Access
from clang.cindex import CursorKind as K

from .parse import _canonical_args, _doc

# template name -> binder function (namespace nanoocp) and the members the binder implements
BINDERS: dict[str, dict] = {
    "NCollection_Array1": {
        "binder": "nanoocp::bind_NCollection_Array1",
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
        "binder": "nanoocp::bind_NCollection_List",
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
        "binder": "nanoocp::bind_NCollection_Sequence",
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
        "binder": "nanoocp::bind_NCollection_HSequence",
        "members": {"Sequence", "ChangeSequence", "Append", "get_type_name", "get_type_descriptor", "DynamicType"},
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Sequence"],
        "nargs": 1,
    },
    "NCollection_Map": {
        "binder": "nanoocp::bind_NCollection_Map",
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
        "binder": "nanoocp::bind_NCollection_DataMap",
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
        "binder": "nanoocp::bind_NCollection_IndexedMap",
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
        "binder": "nanoocp::bind_NCollection_IndexedDataMap",
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
        "binder": "nanoocp::bind_NCollection_Array2",
        "members": {"BeginPosition", "LastPosition", "Size", "Length", "NbRows", "NbColumns", "RowLength", "ColLength", "LowerRow",
                    "UpperRow", "LowerCol", "UpperCol", "UpdateLowerRow", "UpdateLowerCol", "UpdateUpperRow", "UpdateUpperCol",
                    "Assign", "CopyValues", "Value", "operator()", "ChangeValue", "SetValue", "At", "ChangeAt", "Resize", "ResizeWithTrim"},
        "skipped": {"Move", "operator=", "EmplaceValue", "begin", "end", "cbegin", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array1"],    # Array2<T> derives from Array1<T>
        "nargs": 1,
    },
    "NCollection_HArray2": {
        "binder": "nanoocp::bind_NCollection_HArray2",
        "members": {"Array2", "ChangeArray2", "get_type_name", "get_type_descriptor", "DynamicType"},
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": ["NCollection_Array2"],
        "nargs": 1,
    },
    "NCollection_DynamicArray": {
        "binder": "nanoocp::bind_NCollection_DynamicArray",
        "members": {"Size", "Length", "Lower", "Upper", "IsEmpty", "Assign", "Append", "InsertAfter", "InsertBefore", "EraseLast",
                    "Appended", "operator()", "operator[]", "Value", "First", "ChangeFirst", "Last", "ChangeLast", "ChangeValue",
                    "SetValue", "Clear", "SetIncrement"},
        "skipped": {"operator=", "EmplaceAppend", "EmplaceValue", "begin", "end", "cbegin", "cend", "operator new", "operator delete",
                    "operator new[]", "operator delete[]"},
        "requires": [],
        "nargs": 1,
    },
    "NCollection_DoubleMap": {
        "binder": "nanoocp::bind_NCollection_DoubleMap",
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
        "binder": "nanoocp::bind_NCollection_Shared",
        "members": set(),
        "skipped": {"operator new", "operator delete", "operator new[]", "operator delete[]"},
        "requires": [],
        "nargs": 1,                # the second parameter is an enable_if guard
        "wraps": True,             # NCollection_Shared<T> derives from T: T must be bound (class or instantiation)
    },
    "NCollection_HArray1": {
        "binder": "nanoocp::bind_NCollection_HArray1",
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


_OP_NAMES = {"operator()": "op_call", "operator[]": "op_index", "operator=": "op_assign", "operator==": "op_eq",
             "operator!=": "op_ne", "operator+=": "op_iadd", "operator new": "op_new", "operator delete": "op_delete",
             "operator new[]": "op_new_array", "operator delete[]": "op_delete_array"}


def _ident(name: str) -> str:
    return _OP_NAMES.get(name, re.sub(r"\W", "_", name))


def template_docs(include_dir: Path, args: list[str]) -> tuple[str, list[str]]:
    """Generate ncollection_docs.h (docstrings per template member, first overload wins) and return
    it together with coverage warnings (template members neither bound nor listed as skipped)."""
    warnings: list[str] = []
    out = ["// Generated by the nanoOCP generator from the NCollection template headers. Do not edit.",
           "#pragma once", "", "namespace nanoocp_doc {"]
    index = cindex.Index.create()
    for tmpl, info in BINDERS.items():
        tu = index.parse(str(include_dir / f"{tmpl}.hxx"), args=args, options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
        docs: dict[str, str] = {}
        class_doc = ""
        nested: dict[str, dict[str, str]] = {}          # nested class (Iterator) -> member docs
        for cur in tu.cursor.get_children():
            if cur.kind != K.CLASS_TEMPLATE or cur.spelling != tmpl:
                continue
            class_doc = _doc(cur)
            for ch in cur.get_children():
                if ch.access_specifier != Access.PUBLIC:
                    continue
                if ch.kind in (K.CXX_METHOD, K.CONSTRUCTOR, K.FUNCTION_TEMPLATE):
                    is_ctor = ch.kind == K.CONSTRUCTOR or ch.spelling.startswith(tmpl + "<")   # constructor templates
                    name = "ctor" if is_ctor else ch.spelling
                    d = _doc(ch)
                    if name not in docs or (docs[name] == "" and d != ""):
                        docs[name] = d
                    if not is_ctor and ch.spelling not in info["members"] and ch.spelling not in info["skipped"]:
                        warnings.append(f"{tmpl}::{ch.spelling}: public member neither bound nor listed as skipped")
                elif ch.kind in (K.CLASS_DECL, K.STRUCT_DECL) and ch.is_definition() and ch.spelling in info.get("nested", {}):
                    nd = nested.setdefault(ch.spelling, {"class_doc": _doc(ch)})
                    for m in ch.get_children():
                        if m.access_specifier == Access.PUBLIC and m.kind in (K.CXX_METHOD, K.CONSTRUCTOR):
                            nm = "ctor" if m.kind == K.CONSTRUCTOR else m.spelling
                            nd.setdefault(nm, _doc(m))
        # public members inherited from non-template base classes (NCollection_BaseList::Extent, ...)
        for base in info.get("bases", []):
            btu = index.parse(str(include_dir / f"{base}.hxx"), args=args, options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
            for cur in btu.cursor.get_children():
                if cur.kind == K.CLASS_DECL and cur.spelling == base and cur.is_definition():
                    for m in cur.get_children():
                        if m.access_specifier == Access.PUBLIC and m.kind == K.CXX_METHOD:
                            docs.setdefault(m.spelling, _doc(m))
                            if m.spelling not in info["members"] and m.spelling not in info["skipped"]:
                                warnings.append(f"{tmpl}::{m.spelling} (from {base}): public member neither bound nor listed as skipped")
        # some nested iterators are typedefs of a separate template (List::Iterator = NCollection_TListIterator)
        for nested_name, source in info.get("nested_from", {}).items():
            stu = index.parse(str(include_dir / f"{source}.hxx"), args=args, options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
            for cur in stu.cursor.get_children():
                if cur.kind == K.CLASS_TEMPLATE and cur.spelling == source:
                    nd = nested.setdefault(nested_name, {"class_doc": _doc(cur)})
                    for m in cur.get_children():
                        if m.access_specifier == Access.PUBLIC and m.kind in (K.CXX_METHOD, K.CONSTRUCTOR):
                            nd.setdefault("ctor" if m.kind == K.CONSTRUCTOR else m.spelling, _doc(m))
        for name in info["members"]:
            if name not in docs and name not in ("get_type_name", "get_type_descriptor", "DynamicType"):
                warnings.append(f"{tmpl}::{name}: bound by the binder but not found in the header")
        out.append(f"namespace {tmpl} {{")
        out.append(f'constexpr const char *class_doc = R"nbdoc({class_doc})nbdoc";')
        docs.setdefault("ctor", "")
        for name in sorted(set(docs) | info["members"]):
            out.append(f'constexpr const char *{_ident(name)} = R"nbdoc({docs.get(name, "")})nbdoc";')
        for nested_name, members in sorted(nested.items()):
            out.append(f"namespace {nested_name} {{")
            for name in sorted(set(members) | set(info["nested"][nested_name])):
                out.append(f'constexpr const char *{_ident(name)} = R"nbdoc({members.get(name, "")})nbdoc";')
            out.append(f"}} // namespace {nested_name}")
        out.append(f"}} // namespace {tmpl}")
    out += ["} // namespace nanoocp_doc", ""]
    return "\n".join(out), warnings


def deprecated_aliases(alias_dir: Path, args: list[str], templates: dict[str, dict]) -> tuple[dict[str, dict[str, tuple[str, str]]], int]:
    """OCCT 8 keeps the pre-8.0 typedef names (TColgp_Array1OfPnt = NCollection_Array1<gp_Pnt>) in
    src/Deprecated/NCollectionAliases. Returns {prefix: {alias: (home package, bound name)}} for every typedef
    whose instantiation is bound, plus the number of typedefs whose instantiation is not bound."""
    headers = sorted(h.name for h in alias_dir.glob("*.hxx"))
    umbrella = alias_dir.parent / "__nanoocp_aliases.hxx"
    text = "".join(f"#include <{h}>\n" for h in headers)
    index = cindex.Index.create()
    tu = index.parse("aliases.hxx", args=args + [f"-I{alias_dir}"], unsaved_files=[("aliases.hxx", text)],
                     options=cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
    result: dict[str, dict[str, tuple[str, str]]] = {}
    unbound = 0
    for cur in tu.cursor.get_children():
        if cur.kind not in (K.TYPEDEF_DECL, K.TYPE_ALIAS_DECL) or cur.location.file is None:
            continue
        if Path(cur.location.file.name).name not in headers:
            continue
        canon = cur.underlying_typedef_type.get_canonical()
        if canon.kind != cindex.TypeKind.RECORD or canon.get_num_template_arguments() <= 0:
            continue
        tmpl = canon.get_declaration().spelling
        if tmpl not in BINDERS:
            continue
        all_args = [_canonical_args(canon.get_template_argument_type(i)) for i in range(canon.get_num_template_arguments())]
        key = f"{tmpl}<{', '.join(instance_args(tmpl, all_args))}>"
        found = templates.get(key)
        if found is None or found.get("skipped", False):
            unbound += 1
            continue
        prefix = cur.spelling.split("_", 1)[0]
        result.setdefault(prefix, {})[cur.spelling] = (found["package"], found["name"])
    return result, unbound
