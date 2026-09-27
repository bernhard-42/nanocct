"""build123d's own suite through the OCP shim, against the real OCP (State.md 8.18): the standing integration test.

2 501 test IDs of real use (2026-09-26) -- the suite that found the R-RESULT crash this one had missed. Off by default:
it builds two venvs and runs build123d's suite twice (9.3 min on the M5, 2026-09-26), and it needs the wheels of
`make wheel shim` plus a build123d checkout. `make shim-parity` runs the same thing directly; this is the pytest entry.

    OCP3X_PARITY=1 python -m pytest tests/test_shim_parity.py      (BUILD123D=<checkout> to point elsewhere)
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
BUILD123D = Path(os.environ.get("BUILD123D", str(Path.home() / "Development" / "CAD" / "build123d")))


@pytest.mark.skipif(os.environ.get("OCP3X_PARITY") != "1",
                    reason="set OCP3X_PARITY=1: two venvs and two full build123d runs, ~10 min")
def test_build123d_suite_has_the_same_outcome_through_the_shim():
    r = subprocess.run([sys.executable, str(ROOT / "shim" / "parity.py"), "--build123d", str(BUILD123D),
                        "--dist", str(ROOT / "dist"), "--work", str(ROOT / "build" / "shim-parity")],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, r.stdout[-6000:] + r.stderr[-3000:]
