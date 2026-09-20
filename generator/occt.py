"""Locate OCCT modules, toolkits, packages and their headers in the source tree and install."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
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

    @property
    def include_dir(self) -> Path:
        return self.install / "include" / "opencascade"


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
    return tree
