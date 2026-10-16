# NGPC real-gameplay-step profiler

A small Python 3 tool for measuring **actual gameplay updates**, rather than
mistaking display frames or animation repeats for game-logic throughput.

Designed for Neo Geo Pocket Color development using emulator traces, but the
CSV format is generic enough for any frame-driven game engine.

## Run the bundled real-data example

From the repository root:

```bash
python3 tools/ngpc_perf/analyse_steps.py \
  --baseline tools/ngpc_perf/samples/leap66_level5_steps.csv \
  --candidate tools/ngpc_perf/samples/leap67_level5_steps.csv \
  --start 5700 --end 7500
python3 -m unittest discover -s tools/ngpc_perf/tests -v
```

Expected measured results in the supplied Level 5 stress window (MAME 0.289):

| Measurement | LEAP66 | LEAP67 |
|---|---:|---:|
| Complete gameplay intervals in the 1,800-frame window | 264 | 360 |
| Longest gap (display frames) | 13 | 5 |
| Intervals above seven display frames | 81 | 0 |

These are game-logic **interval** counts, not graphics FPS, and are not
proof of identical throughput on physical hardware. This replay is a specific
stress scene, not an all-level benchmark. The original engineering report is
retained privately in the development archive.

## Input specification

A CSV file with exactly two required columns, `frame,port_steps`. There must
be one row per consecutive emulator display frame. `port_steps` increments
when actual game logic executes. Capture at least one frame before `--start`
and some frames after `--end` so the final gap is measurable.

```csv
frame,port_steps
100,200
101,200
102,201
103,201
104,202
```

`--start` is inclusive; `--end` is exclusive for the interval's starting
frame. Negative counter deltas are rejected, preventing accidental wrap or
reset from being misidentified as normal gameplay. Split or normalize traces
if your counter wraps. `--hz` defaults to 60 and is configurable.

## Origin and redistribution of the samples

The two sample files contain ONLY `(display_frame, gameplay_step_counter)`
values extracted from the owner's MAME instrumentation during the LEAP66 and
LEAP67 performance comparison. They do **not** contain ROMs, artwork,
compressed game data, emulator RAM dumps, or BIOS images.

This profiling utility and its sample data are independent of proprietary
console toolchains. The utility's code is under the MIT licence in `LICENSE`.
