# Points system and leaderboard rules

This port adds a score-based challenge to DOS Prince of Persia. The same scoring algorithm applies to **Normal** and **Difficult**, and to **complete** and **legitimately forfeited** attempts. The intended PERSIA online leaderboard ranks them together by score.

## How points are earned

- Complete a level to earn **time points**, calculated from the elapsed time relative to that level's target.
- Collect a **small potion**: **+50** points.
- Collect a **large potion**: **+200** points.
- Take a **sword hit**: **−25** points.
- Die: **−100** points.

**Time-scoring formula (completed level):**

```
time_points = floor(700 * target_seconds / (elapsed_seconds + target_seconds))
level_points = max(0, time_points + 50*small_potions + 200*large_potions
                      - 25*sword_hits - 100*deaths)
run_points   = min(10000, sum(level_points for completed levels))
```

Each level has a distinct target. At exactly its target time, that level earns **350 time points** before bonuses or penalties. Faster times earn more; slower times earn fewer. The final run total is capped at **10,000**. A level that was started but not completed does **not** award its level points.

### Individual level targets

| Level | Target | Level | Target |
|---:|---:|---:|---:|
| 1 | 1:30 | 8 | 3:15 |
| 2 | 2:30 | 9 | 3:45 |
| 3 | 2:45 | 10 | 3:30 |
| 4 | 3:00 | 11 | 3:15 |
| 5 | 3:30 | 12 | 3:15 |
| 6 | 2:45 | 13 | 4:45 |
| 7 | 3:30 | 14 | 2:30 |

**Example:** A completed level awards 418 time points, +200 for a large potion, −25 for a sword hit and −100 for a death, for **493 Total Level Points**. Actual time points always depend on the level target and play time. Failed-attempt potion bonuses are reset rather than credited repeatedly after death/retry.

The level-clear screen shows **Time Taken**, **Best Time**, **Run Time**, **Time Points**, **Potion Bonus**, **Sword Penalty**, **Death Penalty**, **Level Deaths**, **Total Level Points** and **Run Total**.

## Records

**Current Run** shows current eligible progress. **Best Full Run** records a completed 14-level attempt. **Best Incomplete Run** keeps the highest-scoring legitimate forfeit, separately from Best Full Run. Records include overall time, points, deaths and individual level times. Best-record page 6 provides the QR submission option.

For a **forfeited** attempt:

- Only levels already **completed** receive scored level totals.
- The current, unfinished level can contribute elapsed time and statistics, **but no level points**.
- No ending cutscene is played. The run is labelled incomplete/forfeited.
- A forfeit can be stored as **Best Incomplete Run** and can be submitted through the **same intended leaderboard** as complete runs.

## QR submissions: how they work

The game builds an on-screen QR containing the run statistics and the **`PERSIA`** game code. A phone scanner opens an address at **[ngpc-dev.com](https://www.ngpc-dev.com/)** where the player may be asked to confirm and sign in. The game itself does not connect to the internet.

- **Eligible full runs:** format 1 payload (147 QR characters).
- **Eligible forfeits:** format 2 payload (150 QR characters) containing a forfeited status and the number of levels finished.
- Both calculate and submit the **same total-points** field to **one** planned leaderboard.
- The website should independently rebuild the score from stage times, potion counts, sword hits and deaths, and reject impossible values.
- **Cheat-assisted runs are not eligible.** The cheat system prevents access to legitimate QR submission.

**Service status:** The hardware QR generator has been implemented in the project, but `PERSIA` game-code registration and server parsing for both formats require confirmation from the **ngpc-dev.com operator**. Until then, treat the online system as **pending integration**, not a guaranteed live service. Phone-scan testing on a real NGPC and server validation remain necessary.

The QR checksum detects accidental payload changes only; it is **not** cryptographic proof of honest play.
