"""Extract the OCP API the shim reproduces, from an installed cadquery-ocp(-novtk). Run it with THAT interpreter:

    <venv with the real OCP>/bin/python shim/extract_spec.py shim/
    prettier --write shim/ocp-*.json                                     (optional, for reading)

Writes ocp-<version>.json (the names each OCP module exposes) and ocp-<version>-members.json (every class member's
kind and overload signatures -- pybind11 puts one line per overload in the docstring). OCP's RTTI statics
get_type_name_s / get_type_descriptor_s are left out: the bridge adds them to every class by default.
"""
import importlib
import inspect
import json
import pkgutil
import re
import sys
from pathlib import Path

import OCP

SIG = re.compile(r"^(?:\d+\. )?(\w+)\((.*)\) -> (.+)$")
RTTI = {"get_type_name_s", "get_type_descriptor_s"}


def sigs(obj) -> list[str]:
    out = []
    for line in (getattr(obj, "__doc__", None) or "").splitlines():
        line = line.strip()
        m = SIG.match(line)
        if m is not None and m.group(2) != "*args, **kwargs":
            # pybind11 prints an object default with its address, which changes every run: keep only that a default exists
            out.append(re.sub(r" object at 0x[0-9a-f]+>", " object at 0x...>", re.sub(r"^\d+\. ", "", line)))
    return out


def main() -> None:
    out_dir = Path(sys.argv[1])
    version = OCP.__version__
    names_out: dict = {"modules": {}, "version": version}
    members_out: dict = {}
    for mod in sorted(m.name for m in pkgutil.iter_modules(OCP.__path__) if m.name != "OCP"):
        M = importlib.import_module(f"OCP.{mod}")
        names = sorted(n for n in dir(M) if not n.startswith("_"))
        names_out["modules"][mod] = {"names": names}
        for n in names:
            v = getattr(M, n)
            if not inspect.isclass(v) or hasattr(v, "__members__"):
                continue
            members = {}
            for a, av in vars(v).items():
                if a.startswith("_") or a in RTTI:
                    continue
                kind = "static" if isinstance(av, staticmethod) or a.endswith("_s") else ("property" if isinstance(av, property) else "method")
                s = sigs(getattr(v, a, None))
                if kind == "property" or len(s) > 0:
                    members[a] = {"kind": kind, "sigs": s}
            if members:
                members_out.setdefault(mod, {})[n] = members
    (out_dir / f"ocp-{version}.0.json").write_text(json.dumps(names_out, indent=2, sort_keys=True) + "\n")
    (out_dir / f"ocp-{version}.0-members.json").write_text(json.dumps(members_out, indent=2, sort_keys=True) + "\n")
    print(f"OCP {version}: {len(names_out['modules'])} modules, {sum(len(v) for v in members_out.values())} classes with members")


if __name__ == "__main__":
    main()
