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
    start: tuple[int, int],
    world: set[tuple[int, int]],
    discrete_points_0: npt.NDArray[np.int_],
    discrete_points_1: npt.NDArray[np.int_],
) -> Generator[tuple[int, int], None, None]:
    for i in range(4):
        point = (
            start[0] + (i & 1) * (1 if i & 2 else -1),
            start[1] + (1 - (i & 1)) * (1 if i & 2 else -1),
        )
        if (
            point[0] > 0
            and point[1] > 0
            and point[0] < len(discrete_points_0)
            and point[1] < len(discrete_points_1)
            and (discrete_points_0[point[0]], discrete_points_1[point[1]]) not in world
        ):
            yield point


def bfs(
    world: set[tuple[int, int]],
    dest: tuple[int, int],
    discrete_points_0: npt.NDArray[np.int_],
    discrete_points_1: npt.NDArray[np.int_],
) -> int:
    world.discard(dest)

    dists = {}

    start = (
        np.searchsorted(discrete_points_0, 0),
        np.searchsorted(discrete_points_1, 0),
    )
    the_dest = (
        np.searchsorted(discrete_points_0, dest[0]),
        np.searchsorted(discrete_points_1, dest[1]),
    )

    q = np.array(start + (0,), dtype="int,int,int", ndmin=1)
    while len(q) > 0:
        elem = tuple(int(el) for el in q[0])
        q = np.delete(q, 0)

        if elem[:2] in dists:
            continue
        if elem[:2] == the_dest:
            return elem[2]

        dists[elem[:2]] = elem[2]
        q = np.append(
            q,
            np.fromiter(
                (
                    neigh
                    + (
                        elem[2]
                        + abs(discrete_points_0[elem[0]] - discrete_points_0[neigh[0]])
                        + abs(discrete_points_1[elem[1]] - discrete_points_1[neigh[1]]),
                    )
                    for neigh in neighbors(
                        elem[:2], world, discrete_points_0, discrete_points_1
                    )
                ),
                dtype="int,int,int",
            ),
        )

    return -1


if __name__ == "__main__":
    tunels = np.array(input().split(","))
    world = set()

    direction = np.array((-1, 0))
    point = np.array((0, 0))
    set_0 = {-1, 0, 1}
    set_1 = {-1, 0, 1}

    for tunel in tunels:
        direction = update_direction(direction, tunel[0])

        for _ in range(int(tunel[1:])):
            point += direction
            world.add(tuple(int(el) for el in point))

        set_0.update(point[0] + x for x in range(-1, 2))
        set_1.update(point[1] + x for x in range(-1, 2))

    discrete_points_0 = np.sort(np.fromiter(set_0, dtype="int"))
    discrete_points_1 = np.sort(np.fromiter(set_1, dtype="int"))

    ans = bfs(
        world, tuple(int(el) for el in point), discrete_points_0, discrete_points_1
    )
    print(ans)
