"""Compare two pytest JUnit files test by test: the parity check of a nanobuild package against the real OCP.

    python nanobuild/tools/junit_cmp.py <baseline.xml> <candidate.xml>

Prints the outcome counts of both runs and every test id whose outcome differs (`-` = missing in that run).
Run both suites serially: under pytest-xdist build123d's glTF and font tests interfere through the shared cwd.
"""
import sys
import xml.etree.ElementTree as ET
from collections import Counter

OUTCOME = {"failure": "failed", "error": "error", "skipped": "skipped"}


def outcomes(path: str) -> dict[str, str]:
    result = {}
    for tc in ET.parse(path).getroot().iter("testcase"):
        o = "passed"
        for el in tc:
            if el.tag in OUTCOME:
                o = OUTCOME[el.tag]
        result[f"{tc.get('classname')}::{tc.get('name')}"] = o
    return result


def main() -> None:
    a, b = outcomes(sys.argv[1]), outcomes(sys.argv[2])
    ids = sorted(set(a) | set(b))
    diff = [(i, a.get(i, "-"), b.get(i, "-")) for i in ids if a.get(i) != b.get(i)]
    print(f"ids {len(ids)}  baseline {dict(Counter(a.values()))}  candidate {dict(Counter(b.values()))}")
    print(f"differences {len(diff)}")
    for d in diff:
        print("  ", *d)
    sys.exit(0 if len(diff) == 0 else 1)


if __name__ == "__main__":
    main()
