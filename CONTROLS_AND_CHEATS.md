# Controls, menus, saves and cheats

These notes describe the controls implemented in the reviewed NGPC port source associated with the selected v1.0.0 ROM. Please test them on your own cartridge/emulator before publishing a final release.

## Basic play

| Input | Result |
|---|---|
| Left / Right | Move Prince left or right |
| Up | Vertical jump |
| A | Jump forward; combine with directional running for a long jump |
| Hold B | Walk cautiously / grip or grab a ledge |
| Down + B | Cautious crouched interaction / item pick-up |
| Sword drawn: A | Attack |
| Sword drawn: B **or** Up | Parry |
| Option | Pause |

### Title screen

| Input | Result |
|---|---|
| A | New game (confirm replacement if a save exists) |
| Tap B and release | Switch Normal / Difficult |
| Option | Continue existing save, if present |
| B + Up | Records |
| B + Down | Controls page |
| B + Left | Confirm reset of **all** save data and records |

- **Normal:** Three starting health hearts, normal retry behaviour.
- **Difficult:** Two starting health hearts; three total attempts (initial + two retries).
- The normal campaign has a one-hour countdown until the final stage, as in the DOS game adaptation.

### Pause screen

| Input | Result |
|---|---|
| Option | Resume game |
| A | Restart current level |
| Brief B tap | Save and return to title |
| B + Up | View records, when eligible |
| B + Down | Open **FORFEIT THIS RUN?** confirmation |

To **forfeit**, confirm with A. To cancel, use B or Option. Forfeiting skips the usual ending and offers statistics and QR submission for an eligible run. Only fully finished levels earn level-completion points. It will be saved as Best Incomplete Run if the score beats the previous incomplete record. A previously completed Best Full Run remains separate and is not overwritten.

### Records

- Left / Right: change pages.
- Up / Down: cycle between available **Current Run**, **Best Full Run** and **Best Incomplete Run** records.
- B or Option: return to previous menu.
- On page 6 of **Best Full Run** or **Best Incomplete Run**, press A to enter leaderboard submission (if eligible).

### Online QR entry

- Up / Down: change current initial A–Z.
- Left / Right: move between the three initials.
- Option: generate the QR code.
- B: return/back.
- On the displayed QR, B or Option returns to the initials screen.
- Scan with a phone to visit **ngpc-dev.com**. A scannable QR is not proof that the website is already configured to accept the result.

## Hidden practice cheat

**Spoiler:** From the title screen, rotate the D-pad clockwise through all eight directional positions **10 full rotations**. After it unlocks, you can select any **level 1–14** with Left / Right and increase or decrease **health hearts up to 10** with Up / Down (not below the difficulty minimum).

The cheat is intended for practice, demonstrations and testing. **It deliberately disables eligibility for legitimate high-score recording and QR leaderboard submissions.** Reaching the ending using level select does not bypass this restriction. The reset-data menu clears the cheat but also **permanently wipes saves and records**.

## Important distinctions

- **Health hearts** are how many hits Prince can sustain.
- **Difficult-mode attempts** are the separate fixed retry limit; changing hearts does not change this limit.
- **Forfeit** is a legitimate ending to an eligible run, not a cheat.
- **A score on screen** is not proof of submission to an online leaderboard. Website support must be enabled separately.
