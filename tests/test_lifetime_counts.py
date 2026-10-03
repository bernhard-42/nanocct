"""A ratchet on the lifetime rules (Binding-Rules.md; the 2026-10-01 memory audit's categories as generator output): how many
bindings each rule touched, counted in the generated sources and in the generator's reports. An OCCT update, a generator
change or a new rule moves these numbers; the test then fails with the whole table, pinned and found, and the pins are
updated on purpose -- nothing appears or vanishes unseen. Python and stubs see none of it, so only this shows it.

The generated API is not the same on every platform (Cocoa only on macOS; R-UNDEFINED skips what a platform's libraries
do not export), so the pins are per platform."""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parents[1]
CPP = ROOT / "src" / "cpp"

# rule -> what its binding looks like in the generated code (one match per kept parameter, policy, class or site)
MARKERS: dict[str, str] = {
    "R-CTOR-KEEP keep_alive": r"nb::keep_alive<\d+, \d+>",                     # plain constructor keeps (and R-BYTES)
    "R-COPY keep_view_arg": r"nanocct::keep_view_arg<",                         # a constructor argument it may copy pointers out of
    "R-METHOD-KEEP slots": r"nanocct::keep_slot<",
    "R-KEPT slots on the C++ object": r"nanocct::keep_slot<[^>]*, true>",
    "R-KEPT constructor arguments": r"nanocct::keep_arg<",
    "R-KEPT constructor arguments on the C++ object": r"nanocct::keep_arg<[^>]*, true>",
    "R-KEPT classes": r"nanocct::register_kept<",
    "R-RESULT-KEEP / R-OWNER keep_view": r"nanocct::keep_view<",
    "R-RESULT reference_internal": r"rv_policy::reference_internal\b",
    "R-FIELD pointer fields": r"nanocct_def_pointer_field\(",
    "R-VIEW-GUARD wrapped calls": r"nanocct::guarded<",
    "R-VIEW-GUARD lambda checks": r"nanocct::refuse_viewed_argument\(",
    "R-VIEW-GUARD container fields": r"nanocct_def_container_field\(",
    "R-VIEW-GUARD iterator views": r"nanocct::view_of<nanocct::view_kind::iterator",
}
# the report categories of these rules: what each one could not do, and its residuals
CATEGORIES = ("copy", "kept", "lifetime", "view-guard")


# an implicit copy constructor's helper call ends in its flags: `, View>(` or, for a Kept<T> class, `, View, true, Cpp,
# nanocct_slots, N>(` (nanocct_class_helpers.h); the class name before them may hold any template arguments
COPY_TAIL = re.compile(r"^\s*nanocct_implicit_copy_ctor<.*?(?:, (true|false)(, true, (?:true|false), nanocct_slots, \d+)?)?>\(", re.M)


def counts() -> dict[str, int]:
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(CPP.glob("TK*/*.cpp")))
    out = {rule: len(re.findall(pattern, text)) for rule, pattern in MARKERS.items()}
    copies = [m.groups() for m in COPY_TAIL.finditer(text)]
    out["R-COPY implicit copies"] = len(copies)
    out["R-COPY implicit copies that keep the original"] = sum(view == "true" for view, _ in copies)
    out["R-KEPT implicit copies"] = sum(kept is not None for _, kept in copies)
    categories: Counter[str] = Counter()
    for report in sorted(CPP.glob("TK*/report.txt")):
        for line in report.read_text(encoding="utf-8").splitlines():
            if not line.startswith("#") and line != "":
                categories[line.split("\t", 1)[0]] += 1
    out.update({f"report {c}": categories[c] for c in CATEGORIES})
    return out


# measured 2026-10-02 on 8aa81b8: macOS arm64 (Xcode's libclang), Linux x86_64 and Windows (pip libclang 18 -- the two libclangs
# spell some types differently; Windows also skips what its libraries do not export)
PINNED: dict[str, dict[str, int]] = {
    "darwin": {
        "R-CTOR-KEEP keep_alive": 454,
        "R-COPY keep_view_arg": 80,
        "R-METHOD-KEEP slots": 811,
        "R-KEPT slots on the C++ object": 106,
        "R-KEPT constructor arguments": 35,
        "R-KEPT constructor arguments on the C++ object": 31,
        "R-KEPT classes": 54,
        "R-RESULT-KEEP / R-OWNER keep_view": 1094,
        "R-RESULT reference_internal": 725,
        "R-FIELD pointer fields": 28,
        "R-VIEW-GUARD wrapped calls": 1102,
        "R-VIEW-GUARD lambda checks": 106,
        "R-VIEW-GUARD container fields": 44,
        "R-VIEW-GUARD iterator views": 23,
        "R-COPY implicit copies": 4920,
        "R-COPY implicit copies that keep the original": 528,
        "R-KEPT implicit copies": 27,
        "report copy": 310,
        "report kept": 45,
        "report lifetime": 91,
        "report view-guard": 149,
    },
    "linux": {
        "R-CTOR-KEEP keep_alive": 454,
        "R-COPY keep_view_arg": 79,
        "R-METHOD-KEEP slots": 811,
        "R-KEPT slots on the C++ object": 106,
        "R-KEPT constructor arguments": 35,
        "R-KEPT constructor arguments on the C++ object": 31,
        "R-KEPT classes": 54,
        "R-RESULT-KEEP / R-OWNER keep_view": 1094,
        "R-RESULT reference_internal": 725,
        "R-FIELD pointer fields": 28,
        "R-VIEW-GUARD wrapped calls": 1102,
        "R-VIEW-GUARD lambda checks": 106,
        "R-VIEW-GUARD container fields": 44,
        "R-VIEW-GUARD iterator views": 23,
        "R-COPY implicit copies": 4920,
        "R-COPY implicit copies that keep the original": 528,
        "R-KEPT implicit copies": 27,
        "report copy": 308,
        "report kept": 45,
        "report lifetime": 91,
        "report view-guard": 149,
    },
    # Windows binds 3 more Kept<T> classes (2026-10-03, measured): WNT_Window exists only there (#if defined(_WIN32),
    # WNT_Window.hxx:22); Message_PrinterSystemLog has a Windows-only `void* myEventSource` (Message_PrinterSystemLog.hxx:43);
    # Xw_Window's Aspect_Drawable is `void*` there and `unsigned long` elsewhere (Aspect_Drawable.hxx:25-29). The layout rule
    # cannot tell what a void* holds and keeps the arguments it could point to (a title, a source name): the same API, a
    # more cautious keep. The other differences from macOS/Linux are the members R-UNDEFINED drops on Windows.
    "win32": {
        "R-CTOR-KEEP keep_alive": 448,
        "R-COPY keep_view_arg": 80,
        "R-METHOD-KEEP slots": 812,
        "R-KEPT slots on the C++ object": 109,
        "R-KEPT constructor arguments": 36,
        "R-KEPT constructor arguments on the C++ object": 32,
        "R-KEPT classes": 57,
        "R-RESULT-KEEP / R-OWNER keep_view": 1091,
        "R-RESULT reference_internal": 724,
        "R-FIELD pointer fields": 28,
        "R-VIEW-GUARD wrapped calls": 1100,
        "R-VIEW-GUARD lambda checks": 106,
        "R-VIEW-GUARD container fields": 44,
        "R-VIEW-GUARD iterator views": 23,
        "R-COPY implicit copies": 4918,
        "R-COPY implicit copies that keep the original": 528,
        "R-KEPT implicit copies": 27,
        "report copy": 315,
        "report kept": 45,
        "report lifetime": 91,
        "report view-guard": 149,
    },
}


def test_the_lifetime_rules_touch_what_they_did():
    found = counts()
    pinned = PINNED[sys.platform]
    table = "\n".join(f"  {rule:48} pinned {pinned.get(rule, '-'):>6}  found {found[rule]:>6}" for rule in found)
    assert found == pinned, f"the lifetime rules changed -- update PINNED[{sys.platform!r}] on purpose:\n{table}"


if __name__ == "__main__":                       # the numbers to pin, on the platform this runs on
    print(f'    "{sys.platform}": {{')
    for rule, n in counts().items():
        print(f'        "{rule}": {n},')
    print("    },")
