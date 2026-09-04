# Copyright 2026 Yaroslav Mariukha
# SPDX-License-Identifier: Apache-2.0

import os
import sys
from pathlib import Path

from cocotb_tools.runner import get_runner


TEST_DIR = Path(__file__).resolve().parent
TOPLEVEL = "test_avalon_st"


def run_test():
    sim = os.getenv("SIM", "verilator")
    waves = os.getenv("WAVES", "0").lower() in {"1", "true", "yes", "on"}
    build_dir = TEST_DIR / "sim_build" / sim
    build_args = ["-Wno-fatal"] if sim == "verilator" else []

    parameters = {
        "SYMBOLS_PER_BEAT": 1,
        "BITS_PER_SYMBOL": 8
    }

    # Make test_avalon_st.py importable when this script is launched from
    # either the repository root or the test directory.
    sys.path.insert(0, str(TEST_DIR))

    runner = get_runner(sim)
    runner.build(
        sources=[TEST_DIR / "test_avalon_st.sv"],
        hdl_toplevel=TOPLEVEL,
        parameters=parameters,
        build_dir=build_dir,
        build_args=build_args,
        always=True,
        waves=waves,
    )
    runner.test(
        hdl_toplevel=TOPLEVEL,
        test_module="test_avalon_st",
        build_dir=build_dir,
        waves=waves,
    )


if __name__ == "__main__":
    run_test()
