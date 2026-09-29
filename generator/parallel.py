"""The parallel side of the generator (2026-09-24): how many workers to use, and the callables they run.

`jobs_from_env` is the one place that decides the worker count, for the package pools here and for the stub
subprocesses in `stubs.py`.

Lives in its own module because macOS spawns workers rather than forking them: a spawned child re-imports the
module holding the callable, and functions defined in `generator/__main__.py` are unreachable that way
("module '__main__' has no attribute '_pool_init'").

A PackageIR is a tree of plain dataclasses, so it pickles back to the parent without the libclang cursors it was
built from -- which is what makes this possible at all.
"""
from __future__ import annotations

import os
import time
from pathlib import Path

from .occt import load_tree
from .parse import carry_state, collect_state, configure_libclang, parse_package


def default_jobs() -> int:
    """One worker per core the process may use.

    `os.process_cpu_count()` honours what the process is actually allowed (CPU affinity, a container's quota,
    taskset) and exists from Python 3.13; `os.cpu_count()` is the 3.12 fallback."""
    count = getattr(os, "process_cpu_count", os.cpu_count)()
    return count if count is not None else 1


def jobs_from_env(n_items: int) -> tuple[int, str]:
    """How many workers to run `n_items` independent units on, and a one-line explanation for the log.

    `NANOCCT_JOBS` sets it; **unset or 0 means one worker per core**, and **1 is the sequential path** -- which is
    what a byte-for-byte comparison is run against. Never more workers than items, so a one-package run does not pay
    for a pool of idle processes."""
    env = os.environ.get("NANOCCT_JOBS", "")
    requested = int(env) if env != "" else 0
    jobs = max(1, min(requested if requested > 0 else default_jobs(), max(1, n_items)))
    how = f"NANOCCT_JOBS={requested}" if requested > 0 else f"{default_jobs()} cores, NANOCCT_JOBS=1 to go sequential"
    return jobs, how


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
# `templates` has had every owner decided by the driver's assign_templates() pass. So they go into the pool
# initializer once instead of being pickled per package
# (6250 + 1125 entries, 355 jobs).
_EMIT = {}


def init_emit(src, install, known, templates, paths, toolkit_order, bases):
    global _TREE
    configure_libclang()
    _TREE = load_tree(src, install)
    from .parse import clang_args, include_prelude
    cargs = clang_args(_TREE)
    _EMIT.update(known=known, templates=templates, paths=paths, toolkit_order=toolkit_order, bases=bases,
                 toolkit_of={name: pk.toolkit for name, pk in _TREE.packages.items()},
                 prelude=lambda headers: include_prelude(headers, _TREE.include_dir, cargs))


def emit_one(job):
    """(toolkit, package, ir) -> the emitted translation unit plus what the driver has to merge."""
    from .emit import Emitter
    tk_name, pkg_name, ir = job
    em = Emitter(ir, _TREE.include_dir, _EMIT["known"], _EMIT["toolkit_of"], dict(_EMIT["templates"]),
                 _EMIT["toolkit_order"], _EMIT["paths"], prelude_check=_EMIT["prelude"], bases_of=_EMIT["bases"])
    em.preassigned = True                       # the owner of every instantiation is already recorded
    t0 = time.perf_counter()
    text = em.emit()
    return tk_name, pkg_name, text, em.report, em.includes, em.skipped, time.perf_counter() - t0
