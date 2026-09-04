<!--
Copyright 2026 Yaroslav Mariukha
SPDX-License-Identifier: Apache-2.0
-->

# cocotbext-avalon

Reusable Avalon Streaming (Avalon-ST) and Avalon Memory-Mapped (Avalon-MM)
bus functional models for cocotb.

## Install

```bash
python -m pip install cocotbext-avalon
```

For local development:

```bash
python -m pip install -e .
```

## Usage

```python
from cocotbext.avalon import (
    AvalonFormat,
    AvalonMMBus,
    AvalonMMMasterBFM,
    AvalonMMMemoryBFM,
    AvalonMMSlaveBFM,
    AvalonMMTransaction,
    AvalonSTBeat,
    AvalonSTBus,
    AvalonSTFrame,
    AvalonSTMonitor,
    AvalonSTSink,
    AvalonSTSource,
)
```

`AvalonSTSource`, `AvalonSTSink`, and `AvalonSTMonitor` support packetized and
non-packetized streams, pause generators, sideband signals, and ready modes
`ready_latency=0, ready_allowance=0` and
`ready_latency=1, ready_allowance=1`.

`AvalonMMMasterBFM`, `AvalonMMSlaveBFM`, and `AvalonMMMemoryBFM` support
register-style accesses, bursts, byte enables, wait-request backpressure,
variable-latency reads, and optional transaction recording.

HDL-backed simulator regression tests will be added after the initial package
extraction is complete.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
