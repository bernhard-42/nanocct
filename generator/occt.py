"""Locate OCCT modules, toolkits, packages and their headers in the source tree and install."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
import platform
from pathlib import Path

MODULES = ("FoundationClasses", "ModelingData", "ModelingAlgorithms", "Visualization",
           "ApplicationFramework", "DataExchange")


@dataclass
class Package:
    name: str
    toolkit: str
    module: str
    headers: list[str] = field(default_factory=list)   # basenames, in FILES.cmake order


@dataclass
class Toolkit:
    name: str
    module: str
    packages: list[Package] = field(default_factory=list)
    depends: list[str] = field(default_factory=list)   # other toolkits (from EXTERNLIB.cmake)


@dataclass
class OcctTree:
    src: Path          # deps/occt-src
    install: Path      # deps/occt-8.0.1
    toolkits: dict[str, Toolkit] = field(default_factory=dict)
    packages: dict[str, Package] = field(default_factory=dict)
    toolkit_of_header: dict[str, str] = field(default_factory=dict)   # "TDocStd_Document.hxx" -> "TKLCAF"

    @property
    def include_dir(self) -> Path:
        """Where the install keeps the headers. OCCT's own layout differs by platform: `<install>/inc` on Windows
        (what its env.bat exports as CSF_OCCTIncludePath), `<install>/include/opencascade` elsewhere. The native
        layout is checked first, because a staged copy of another platform's headers can sit in the other location
        (it did on the Windows box, 2026-09-23) and silently parse the wrong OS's API."""
        candidates = [self.install / "inc", self.install / "include" / "opencascade"]
        if platform.system() != "Windows":
            candidates.reverse()
        for candidate in candidates:
            if candidate.is_dir():
                return candidate
        return candidates[-1]

    def link_closure(self, toolkit: str) -> set[str]:
        """The toolkit and everything it links transitively (EXTERNLIB.cmake); what the linker already sees."""
        seen: set[str] = set()
        todo = [toolkit]
        while len(todo) > 0:
            name = todo.pop()
            if name in seen:
                continue
            seen.add(name)
            tk = self.toolkits.get(name)
            if tk is not None:
                todo += tk.depends
        return seen


_SET_RE = re.compile(r"set\s*\(\s*(\w+)\s*(.*?)\)", re.S)


def _cmake_list(path: Path) -> list[str]:
    """Items of the first set(<NAME> ...) whose NAME does not end in _LOCATION (FILES.cmake has two sets)."""
    text = path.read_text()
    for m in _SET_RE.finditer(text):
        name, body = m.group(1), m.group(2)
        if name.endswith("_LOCATION"):
            continue
        items: list[str] = []
        for tok in body.split():
            if tok.startswith("#") or tok.startswith("${"):
                continue
            items.append(tok)
        return items
    return []


def load_tree(src: Path, install: Path) -> OcctTree:
    tree = OcctTree(src=src, install=install)
    for module in MODULES:
        tk_list = src / "src" / module / "TOOLKITS.cmake"
        if not tk_list.exists():
            continue
        for tk_name in _cmake_list(tk_list):
            tk_dir = src / "src" / module / tk_name
            tk = Toolkit(name=tk_name, module=module)
            pkg_file = tk_dir / "PACKAGES.cmake"
            if pkg_file.exists():
                for pkg_name in _cmake_list(pkg_file):
                    pkg_dir = tk_dir / pkg_name
                    files_cmake = pkg_dir / "FILES.cmake"
                    headers: list[str] = []
                    if files_cmake.exists():
                        headers = [f for f in _cmake_list(files_cmake) if f.endswith(".hxx")]
                    pkg = Package(name=pkg_name, toolkit=tk_name, module=module, headers=headers)
                    tk.packages.append(pkg)
                    tree.packages[pkg_name] = pkg
            ext = tk_dir / "EXTERNLIB.cmake"
            if ext.exists():
                tk.depends = [d for d in _cmake_list(ext) if d.startswith("TK") and d != tk_name]
            tree.toolkits[tk_name] = tk
    # A toolkit can *borrow* another's package: TKOpenGles compiles the same sources as TKOpenGl and lists them as
    # "../TKOpenGl/OpenGl". The headers belong to the owner, so a borrowed entry (a path, not a bare package name)
    # must not claim them -- R-LINK asked for libTKOpenGles, which a USE_GLES2=OFF build does not have (2026-09-22).
    for pkg in tree.packages.values():
        if "/" in pkg.name:
            continue
        for header in pkg.headers:
            tree.toolkit_of_header[header] = pkg.toolkit
    return tree
