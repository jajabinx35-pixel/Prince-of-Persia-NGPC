# NGPC engineering: source, measurements and maintenance

## What this repository contributes

This is a noncommercial Neo Geo Pocket Color porting / performance study,
with a focus on authentic hardware constraints: scarce VRAM tile patterns,
small RAM budgets, graphics publishing, CPU-limited scenes, and distinguishing
rendered frames from actual gameplay updates.

The project has proceeded through repeated source-level changes and regression
checks. Its public, reusable contribution in this directory is the
[dependency-free gameplay-step profiler](../tools/ngpc_perf/README.md),
which demonstrates how to verify performance changes with concrete captured
counters rather than visual impressions.

## Concrete, bounded evidence

The LEAP66 and LEAP67 comparison used MAME 0.289 in an identical scripted
Level 5 stress scenario (Shadow Prince, two active chompers, and a floor
switch). A 1,800-display-frame window recorded 264 vs 360 actual gameplay
intervals, 13 vs 5 frames as the maximum interval, and 81 vs 0 intervals
above seven display frames. These results were extracted from the supplied
private LEAP67 source/evidence archive, not estimated from screenshots.

Do not generalise these results to every scene or to actual console hardware
without separate reproducible measurements. The tool's data extraction does
not include the full game or its original assets.

## Code and rights status

The complete LEAP67 development archive is **not** an appropriate public
open-source upload: it includes proprietary legacy Toshiba compiler tools,
compiled ROMs, original Prince of Persia visual and audio resources, and
large MAME traces. None of those are redistributed by this upload package.

The port's gameplay logic includes material derived from the GPLv3-or-later
[SDLPoP project](https://github.com/NagyD/SDLPoP). Source-derived work must
retain compatible GPL licensing and upstream attribution if published.
Source code licensing does not automatically grant distribution rights to
underlying game artwork, music, levels, brand, or a compiled ROM.

The code and fixture files under `tools/ngpc_perf/` are scoped under MIT as
stated in their local licence. This does not purport to relicense SDLPoP,
Prince of Persia, or the existing repository's assets or ROM release.

## Maintenance plan

- Track reproducible performance regressions with trace comparisons.
- Review bug reports for emulator version, replay description, and actual
  logic-step measurements.
- Maintain the hardware-vs-emulator verification distinction.
- Document changes, test failures, and behaviour differences transparently.
- Review future source or asset contributions for provenance before merging.

## Contribution guide

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for testing and contributions.
