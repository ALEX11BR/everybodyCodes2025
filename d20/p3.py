#!/usr/bin/env python3

import sys
from typing import Generator

import numpy as np


def rotate_point_trigo(point: tuple[int, int], world_len: int) -> tuple[int, int]:
    diag_diff = 2 * point[0] + (point[0] + point[1]) % 2
    diag_sum = world_len - abs(point[1] - point[0])

    return (abs(diag_sum - diag_diff) // 2, (diag_sum + diag_diff) // 2)


def triangle_neighbors(
    point: tuple[int, int], columns_count: int
) -> Generator[tuple[int, int], None, None]:
    yield point
    if point[1] > point[0]:
        yield (point[0], point[1] - 1)
    if point[1] + 1 < columns_count - point[0]:
        yield (point[0], point[1] + 1)
    if point[0] > 0 and point[0] % 2 == point[1] % 2:
        yield (point[0] - 1, point[1])
    if (
        point[0] + 1 <= point[1]
        and point[0] + 1 <= columns_count - point[1] - 1
        and point[0] % 2 != point[1] % 2
    ):
        yield (point[0] + 1, point[1])


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

        if point in visited or world[point[0]][point[1]] not in "TES":
            continue
        if point == end:
            ans = dist
            break

        visited.add(point)

        for neighbor in map(
            lambda p: rotate_point_trigo(p, len(world[0]) - 2),
            triangle_neighbors(point, len(world[0]) - 1),
        ):
            q += ((neighbor, dist + 1),)

    print(ans)
