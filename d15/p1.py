#!/usr/bin/env python3

from typing import Generator

import numpy as np
import numpy.typing as npt


def update_direction(
    direction: npt.NDArray[np.int_], move_dir: str
) -> npt.NDArray[np.int_]:
    new_delta = (-1) ** int((direction[0] == 0) ^ (move_dir == "R"))
    return np.array((direction[1] * new_delta, direction[0] * new_delta))


def neighbors(
    start: tuple[int, int], world: set[tuple[int, int]]
) -> Generator[tuple[int, int], None, None]:
    for i in range(4):
        point = (
            start[0] + (i & 1) * (1 if i & 2 else -1),
            start[1] + (1 - (i & 1)) * (1 if i & 2 else -1),
        )
        if point not in world:
            yield point


def bfs(world: set[tuple[int, int]], dest: tuple[int, int]) -> int:
    world.discard(dest)

    dists = {}

    q = np.array((0, 0, 0), dtype="int,int,int", ndmin=1)
    while len(q) > 0:
        elem = tuple(int(el) for el in q[0])
        q = np.delete(q, 0)

        if elem[:2] in dists:
            continue
        if elem[:2] == dest:
            return elem[2]

        dists[elem[:2]] = elem[2]
        q = np.append(
            q,
            np.fromiter(
                (neighbor + (elem[2] + 1,) for neighbor in neighbors(elem[:2], world)),
                dtype="int,int,int",
            ),
        )

    return -1


if __name__ == "__main__":
    tunels = np.array(input().split(","))
    world = set()

    direction = np.array((-1, 0))
    point = np.array((0, 0))

    for tunel in tunels:
        direction = update_direction(direction, tunel[0])
        for _ in range(int(tunel[1:])):
            point += direction
            world.add(tuple(int(el) for el in point))

    ans = bfs(world, tuple(int(el) for el in point))
    print(ans)
