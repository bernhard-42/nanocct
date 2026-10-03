"""Documented nanobind API only (Toolchain.md 4.3): the hand-written C++ may use nanobind's internals only where it is listed
below, with the reason. A new use fails here, and so does a removed one (shrink the list then) -- an internal can change in
any nanobind release without notice, and a list kept by hand would go stale. The generated code uses none at all."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import nanobind

ROOT = Path(__file__).parents[1]

# nanobind's backend functions, from the installed version: nb_backend_slots.h declares every one (NB_SLOT(ret, name, args));
# the nb_-prefixed names are unambiguous in code, the others (error_fetch, ...) are only reachable through NB_CALL
SLOTS = Path(nanobind.__file__).parent / "include" / "nanobind" / "nb_backend_slots.h"
BACKEND = sorted(set(re.findall(r"^\s*NB_SLOT(?:_ALIAS)?\(\s*[^,]+,\s*(nb_\w+)", SLOTS.read_text(), flags=re.M)))

# nanobind's internals as they appear in code: a backend call (NB_CALL(...), an nb_ backend function), the context and
# inlining macros, its internal headers (nb_*.h; nanobind.h, ndarray.h, stl/ are the public ones), and `nb::detail::`
# names -- except `cleanup_list`, which the documented call_policy precall signature names (api_core.rst, nb::call_policy)
INTERNAL = re.compile(r"NB_CALL\(\w+\)|NB_CTX\w*|NB_INLINE|nanobind/nb_\w+\.h|nb::detail::(?!cleanup_list\b)\w+|\b(?:"
                      + "|".join(BACKEND) + r")\b")

ALLOWED: dict[tuple[str, str], tuple[int, str]] = {
    ("src/cpp/common/nanocct_common.h", "nanobind/nb_defs.h"): (
        1, "MSVC: NB_INLINE is redefined from __forceinline to inline (math.cpp 1677 s -> 16 s, nanobind discussion 791)"),
    ("src/cpp/common/nanocct_common.h", "NB_INLINE"): (2, "the MSVC redefinition (#undef, #define)"),
    ("src/cpp/common/nanocct_casters.h", "NB_INLINE"): (1, "the OptionalCString caster's can_cast, as nanobind's own casters"),
}


def _code(text: str) -> str:
    """The text without comments and string literals (comments name nanobind's internal files, nb_type.cpp)."""
    text = re.sub(r'R"nbdoc\(.*?\)nbdoc"', '""', text, flags=re.S)
    text = re.sub(r'"(?:\\.|[^"\\\n])*"', '""', text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return re.sub(r"//[^\n]*", "", text)


def _uses(paths: list[Path]) -> Counter[tuple[str, str]]:
    found: Counter[tuple[str, str]] = Counter()
    for path in paths:
        for m in INTERNAL.finditer(_code(path.read_text(encoding="utf-8"))):
            found[(path.relative_to(ROOT).as_posix(), m.group(0))] += 1
    return found


def test_hand_written_code_uses_only_the_listed_internals():
    paths = sorted((ROOT / "src" / "cpp" / "common").glob("*.h")) + sorted((ROOT / "src" / "cpp" / "AddOns").glob("*.[ch]*"))
    assert len(paths) >= 8
    found = _uses(paths)
    assert dict(found) == {key: count for key, (count, _) in ALLOWED.items()}


def test_the_generated_code_uses_no_internals():
    paths = sorted((ROOT / "src" / "cpp").glob("TK*/*.cpp"))
    assert len(paths) > 300
    assert _uses(paths) == Counter()


def test_the_backend_list_is_read():
    assert len(BACKEND) > 20 and "nb_type_put" in BACKEND and "nb_inst_ptr" in BACKEND


def test_the_scan_sees_through_comments_but_not_code():
    """The scan itself: a use in code counts, the same words in a comment or a string do not."""
    sample = 'x = NB_CALL(nb_type_put)(a); // NB_CALL(nb_type_put) nb_type.cpp\n/* nb_inst_ptr */ s = "nb::detail::foo";\n'
    hits = [m.group(0) for m in INTERNAL.finditer(_code(sample))]
    assert hits == ["NB_CALL(nb_type_put)"]
    assert [m.group(0) for m in INTERNAL.finditer(_code("nb::detail::cleanup_list *c; nb::detail::make_caster<T> m;"))] == [
        "nb::detail::make_caster"]
