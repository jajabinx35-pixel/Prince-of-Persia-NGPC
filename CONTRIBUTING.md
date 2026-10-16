# Contributing

Contributions are welcome to the **independently reusable NGPC profiling
utility** under `tools/ngpc_perf/`, especially additional tests, CSV import
support, and explanations of hardware-vs-emulator measurements.

For performance bugs, provide: emulator version or physical-console model,
the steps to reproduce, the baseline and candidate frame/logic-step counters,
and the exact scene tested. A short trace without ROM images is preferred.

Run tests with:

```bash
python3 -m unittest discover -s tools/ngpc_perf/tests -v
```

Please don't upload commercial game data, copyrighted sprites/music, BIOS
files, or proprietary compiler executables in issues or pull requests.
Source derived from SDLPoP is governed by its GPLv3-or-later obligations;
the scoped profiler itself is MIT-licensed.

This is a volunteer project. Review and response times vary, and a submitted
issue does not imply that the fix has been completed or independently tested.
