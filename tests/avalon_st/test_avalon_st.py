# Copyright 2026 Yaroslav Mariukha
# SPDX-License-Identifier: Apache-2.0

import logging
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

from cocotbext.avalon import (
    AvalonFormat,
    AvalonSTBus,
    AvalonSTFrame,
    AvalonSTSink,
    AvalonSTSource,
)

def pause_gen():
    while True:
        yield False
        yield False
        yield True
        yield True
        yield True


@cocotb.test()
async def stream_loopback_test(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    fmt = AvalonFormat(
        bits_per_symbol=8,
        symbols_per_beat=1,
        first_symbol_in_high_order_bits=False,
    )

    source = AvalonSTSource(
        AvalonSTBus.from_prefix(dut, "din"),
        fmt,
        dut.clk,
        reset=dut.reset,
        packets=True,
        idle_value=0,
    )
    sink = AvalonSTSink(
        AvalonSTBus.from_prefix(dut, "dout"),
        fmt,
        dut.clk,
        reset=dut.reset,
        packets=True,
    )
    sink.set_pause_generator(pause_gen())

    logging.getLogger(
        "cocotb.test_avalon_st.din.source"
    ).setLevel(logging.DEBUG)

    logging.getLogger(
        "cocotb.test_avalon_st.dout.sink"
    ).setLevel(logging.DEBUG)
    

    payload = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66]

    await source.send(AvalonSTFrame(data=payload))
    received = await sink.recv()

    assert received.data == payload
