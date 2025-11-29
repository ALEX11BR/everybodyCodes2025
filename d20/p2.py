#!/usr/bin/env python3

import sys

import numpy as np


if __name__ == "__main__":
    world = np.array(sys.stdin.readlines())
    start = next(
        (i, j)
        for i in range(len(world))
        for j in range(len(world[0]))
        if world[i][j] == "S"
    )
    end = next(
        (i, j)
        for i in range(len(world))
        for j in range(len(world[0]))
        if world[i][j] == "E"
    )

    q = ((start, 0),)
    visited = set()

    while len(q) > 0:
        point, dist = q[0]
        q = q[1:]

        if point in visited:
            continue
        if point == end:
            ans = dist
            break

        visited.add(point)

        if point[1] > 0 and world[point[0]][point[1] - 1] in "TE":
            q += (((point[0], point[1] - 1), dist + 1),)
        if world[point[0]][point[1] + 1] in "TE":
            q += (((point[0], point[1] + 1), dist + 1),)
        if (
            point[0] > 0
            and point[0] % 2 == point[1] % 2
            and world[point[0] - 1][point[1]] in "TE"
        ):
            q += (((point[0] - 1, point[1]), dist + 1),)
        if (
            point[0] + 1 < len(world)
            and point[0] % 2 != point[1] % 2
            and world[point[0] + 1][point[1]] in "TE"
        ):
            q += (((point[0] + 1, point[1]), dist + 1),)

    print(ans)
