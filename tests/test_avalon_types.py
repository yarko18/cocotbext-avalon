# Copyright 2026 Yaroslav Mariukha
# SPDX-License-Identifier: Apache-2.0

import logging

import pytest

from cocotbext.avalon import (
    AvalonFormat,
    AvalonMMBus,
    AvalonMMMasterBFM,
    AvalonSTFrame,
)


class _Signal:
    def __init__(self, width):
        self.width = width
        self.value = 0

    def __len__(self):
        return self.width


def _bus():
    return AvalonMMBus(
        address=_Signal(8),
        writedata=_Signal(32),
        write=_Signal(1),
        read=_Signal(1),
        readdata=_Signal(32),
        byteenable=_Signal(4),
        label="test_mm",
    )


def test_avalon_format_payload_width():
    assert AvalonFormat(bits_per_symbol=10, symbols_per_beat=3).payload_width == 30


def test_avalon_st_frame_copy():
    original = AvalonSTFrame([1, 2, 3], channel=4, error=0)
    assert AvalonSTFrame(original) == original


def test_master_packet_log_level_accepts_string():
    bfm = AvalonMMMasterBFM(
        _bus(),
        clock=object(),
        packet_logging=True,
        packet_log_level="debug",
    )

    assert bfm.packet_logging is True
    assert bfm.packet_log_level == logging.DEBUG


def test_master_packet_log_level_rejects_unknown_string():
    with pytest.raises(ValueError, match="Unknown log level"):
        AvalonMMMasterBFM(_bus(), clock=object(), packet_log_level="verbose")
