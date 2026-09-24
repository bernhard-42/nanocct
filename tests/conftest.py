"""Shared helper for the generated-report assertions.

A toolkit's report.txt is not the same on every platform, and it cannot be: the `undefined` category comes from
R-UNDEFINED, which compares each member against the symbols the OCCT library of *this* platform actually exports.
Unix exports everything a header declares, while Windows exports only what carries Standard_EXPORT, so the same
toolkit reports e.g. 3 undefined lines on macOS and 0 on Linux (TKRWMesh), or 8 against 5 (TKOpenGl). Asserting a
total line count therefore turns every report test into a macOS test.

So the tests assert exact counts over the *portable* lines -- every category except `undefined` -- and check the
undefined ones by content instead: whatever a platform reports there must be one of the known entries.

TKOpenGl needs one more exemption, `raw-pointer` and `override`: the GL loader tables it reports are OCCT's own
per-platform entry-point lists (CGL on macOS, EGL on Linux), 768/4 against 773/2. That is the OCCT build differing,
not the generator, so those two categories are compared with a lower bound there.
"""
from pathlib import Path

CPP = Path(__file__).parents[1] / "src" / "cpp"


def report(toolkit: str) -> tuple[list[str], list[str], list[str], dict[str, int]]:
    """(all lines, portable lines, undefined lines, counts of the portable categories) for a toolkit's report.txt."""
    lines = [line for line in (CPP / toolkit / "report.txt").read_text().splitlines() if not line.startswith("#")]
    undefined = [line for line in lines if line.startswith("undefined\t")]
    portable = [line for line in lines if not line.startswith("undefined\t")]
    counts: dict[str, int] = {}
    for line in portable:
        counts[line.split("\t")[0]] = counts.get(line.split("\t")[0], 0) + 1
    return lines, portable, undefined, counts
