#!/usr/bin/env python3

import sys

import numpy as np


if __name__ == "__main__":
    world = np.array(sys.stdin.readlines())

    ans = 0

    for i in range(len(world) - 1):
        for j in range(i, len(world[0]) - i - 1):
            if world[i][j] != "T":
                continue
            ans += int(world[i][j + 1] == "T") + int(
                i % 2 != j % 2 and world[i + 1][j] == "T"
            )

    print(ans)
