"""Write the ocp3xbuild patch of a ported tree: a unified diff (`a/`, `b/`, applied with `patch -p1`) of every file of
the sdist that the tree changed.

    python ocp3xbuild/tools/mkpatch.py <sdist .tar.gz> <ported tree> <output .patch>

Only files the sdist contains are compared, so build and test leftovers in the ported tree (__pycache__, exported
test files) never reach the patch; the port adds no files of its own.
"""
import difflib
import sys
import tarfile
from pathlib import Path


def main() -> None:
    tar, ported, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    chunks = []
    with tarfile.open(tar) as tf:
        for m in sorted(tf.getmembers(), key=lambda m: m.name):
            if m.isfile() is False:
                continue
            rel = m.name.split("/", 1)[1]
            old = tf.extractfile(m).read()
            new = (ported / rel).read_bytes()
            if old == new:
                continue
            d = list(difflib.unified_diff(old.decode().splitlines(keepends=True),
                                          new.decode().splitlines(keepends=True), f"a/{rel}", f"b/{rel}", n=3))
            for i, line in enumerate(d):
                if line.endswith("\n") is False:
                    d[i] = line + "\n\\ No newline at end of file\n"
            chunks.append("".join(d))
    out.write_text("".join(chunks))
    print(out.name, len(chunks), "files")


if __name__ == "__main__":
    main()
