"""The worker side of the parallel generation (2026-09-24): whole packages parsed and emitted in separate processes.

Lives in its own module because macOS spawns workers rather than forking them: a spawned child re-imports the
module holding the callable, and functions defined in `generator/__main__.py` are unreachable that way
("module '__main__' has no attribute '_pool_init'").

A PackageIR is a tree of plain dataclasses, so it pickles back to the parent without the libclang cursors it was
built from -- which is what makes this possible at all.
"""
from __future__ import annotations

import time
from pathlib import Path

from .occt import load_tree
from .parse import carry_state, collect_state, configure_libclang, parse_package

_TREE = None


def init(src: Path, install: Path) -> None:
    global _TREE
    configure_libclang()
    _TREE = load_tree(src, install)


def parse_one(job):
    tk_name, pkg_name, known, state = job
    carry_state(state)
    pkg = next(p for p in _TREE.toolkits[tk_name].packages if p.name == pkg_name)
    t0 = time.perf_counter()
    ir = parse_package(_TREE, pkg, known_elsewhere=set(known))
    return tk_name, pkg_name, ir, time.perf_counter() - t0, collect_state()


# ---- parallel emit -------------------------------------------------------------------------------------------------
# Everything the emitter reads is complete before the first emit: `known` and `paths` are filled in the parse loop,
# `templates` has had every owner decided by the driver's assign_templates() pass, and `static_renames` is computed
# from all parsed classes. So they go into the pool initializer once instead of being pickled per package
# (6250 + 1125 entries, 355 jobs).
_EMIT = {}


def init_emit(src, install, known, templates, paths, toolkit_order, static_renames):
    global _TREE
    configure_libclang()
    _TREE = load_tree(src, install)
    from .parse import clang_args, include_prelude
    cargs = clang_args(_TREE)
    _EMIT.update(known=known, templates=templates, paths=paths, toolkit_order=toolkit_order,
                 static_renames=static_renames,
                 toolkit_of={name: pk.toolkit for name, pk in _TREE.packages.items()},
                 prelude=lambda headers: include_prelude(headers, _TREE.include_dir, cargs))


def emit_one(job):
    """(toolkit, package, ir) -> the emitted translation unit plus what the driver has to merge."""
    from .emit import Emitter
    tk_name, pkg_name, ir = job
    em = Emitter(ir, _TREE.include_dir, _EMIT["known"], _EMIT["toolkit_of"], dict(_EMIT["templates"]),
                 _EMIT["toolkit_order"], _EMIT["paths"], prelude_check=_EMIT["prelude"])
    em.static_renames = _EMIT["static_renames"]
    em.preassigned = True                       # the owner of every instantiation is already recorded
    t0 = time.perf_counter()
    text = em.emit()
    return tk_name, pkg_name, text, em.report, em.includes, em.skipped, time.perf_counter() - t0
