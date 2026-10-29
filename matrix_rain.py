#!/usr/bin/env python3
"""Tiny Matrix-style rain in the terminal (short demo)."""

import random
import time


CHARS = "01アイウエオカキクケコ✦★✧"


def rain(width: int = 40, height: int = 12, frames: int = 20) -> None:
    cols = [random.randint(0, height) for _ in range(width)]
    for _ in range(frames):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        for x, y in enumerate(cols):
            for trail in range(5):
                yy = y - trail
                if 0 <= yy < height:
                    grid[yy][x] = random.choice(CHARS) if trail == 0 else "·"
            cols[x] = (y + 1) % (height + 5)
        print("\033[2J\033[H", end="")
        for row in grid:
            print("".join(row))
        time.sleep(0.08)


if __name__ == "__main__":
    print("Matrix rain demo (brief)...")
    time.sleep(0.3)
    rain()
    print("\nDone.")
