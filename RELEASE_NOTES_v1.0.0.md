# Prince of Persia NGPC — v1.0.0

**Status: v1.0.0 ROM prepared — online leaderboard activation pending.**

The original DOS *Prince of Persia* has been adapted to the **Neo Geo Pocket Color**, with all **14 levels** and a new scoring challenge. The port is **heavily AI-assisted** and the result of a long cycle of debugging, performance optimisation and testing on real hardware.

### Features

- Original-style Prince of Persia gameplay, sword combat, traps, storyline and ending.
- Normal and Difficult modes, with optional hidden level select / heart settings for practice.
- Save/continue and in-game statistics.
- New scoring system: time-based level points; **+50** small potion, **+200** large potion, **−25** sword hit, **−100** death.
- Best Full Run and Best Incomplete Run records.
- Pause-menu forfeit to end a legitimate run without the story ending.
- On-device QR generation for an intended **single PERSIA online leaderboard** supporting both complete and forfeited runs (**subject to website support**).
- **Cheat-assisted results cannot be submitted to the leaderboard.**

### Performance expectations

The game has been played through on **real NGPC hardware** and is in a playable state after significant optimisation. **Brief stutters can remain** during demanding scenes with multiple hazards or overlapping scenery. Video captured in **emulation** may look noticeably smoother and should not be mistaken for a physical-console performance guarantee.

### Controls / cheat / QR help

See [README.md](README.md), [CONTROLS_AND_CHEATS.md](CONTROLS_AND_CHEATS.md), and [SCORING_AND_LEADERBOARDS.md](SCORING_AND_LEADERBOARDS.md).

### Credits

Original *Prince of Persia* — **Jordan Mechner**. DOS reverse-engineering contributors and **SDLPoP** by **Dávid Nagy**: https://github.com/NagyD/SDLPoP. The points/QR work was motivated by **https://www.ngpc-dev.com/**. See [CREDITS_AND_RIGHTS.md](CREDITS_AND_RIGHTS.md).

### Intended ROM

`Prince_of_Persia-NGPC-v1.0.0.ngc` — **2,097,152 bytes (2 MiB)**. Its SHA-256 is recorded in [ROM_CHECKSUM_SHA256.txt](ROM_CHECKSUM_SHA256.txt).

The ROM is included in the prepared release package under `GitHub_Release_ROM/` for attachment to GitHub Releases. No game source or Toshiba build tools are provided. **Important:** distributing a ROM containing GPL-derived code without the corresponding source may fail to satisfy GPL licence conditions, and original-game assets may require separate permission. See [CREDITS_AND_RIGHTS.md](CREDITS_AND_RIGHTS.md).
