#!/usr/bin/env python3

import sys

import numpy as np
import numpy.typing as npt


ROUNDS = 1000000000
WORLD_SIZE = 34


def stringify_world(world: npt.NDArray[np.bool_]) -> str:
    return "".join(
        ("#" if world[i, j] else ".") + ("\n" if j == WORLD_SIZE - 1 else "")
        for i in range(WORLD_SIZE)
        for j in range(WORLD_SIZE)
    )


def unstringify_world(world_str: str) -> npt.NDArray[np.bool_]:
    lines = np.array(world_str.split("\n"))[:-1]
    return np.reshape(
        np.fromiter((c == "#" for line in lines for c in line), dtype="bool"),
        shape=(len(lines), -1),
    )


def assess_world(world: npt.NDArray[np.bool_], mask: npt.NDArray[np.bool_]) -> int:
    if np.all(
        mask
        == world[
            (WORLD_SIZE // 2 - mask.shape[0] // 2) : (
                WORLD_SIZE // 2 + mask.shape[0] // 2
            ),
            (WORLD_SIZE // 2 - mask.shape[1] // 2) : (
                WORLD_SIZE // 2 + mask.shape[1] // 2
            ),
        ]
    ):
        return np.count_nonzero(world)
    return 0


if __name__ == "__main__":
    world = np.zeros(shape=(WORLD_SIZE, WORLD_SIZE), dtype="bool")
    mask = unstringify_world(sys.stdin.read())

    ans = 0
    round_cache = set()
    assessed = np.empty(shape=0, dtype="int")

    for rnd in range(ROUNDS):
        world_change = np.array(world, dtype="int")
        for shift_0 in (-1, 1):
            for shift_1 in (-1, 1):
                shifted = np.roll(world, shift_0, 0)
                shifted = np.roll(shifted, shift_1, 1)

                shifted[min(shift_0, 0), :] = 0
                shifted[:, min(shift_1, 0)] = 0

                world_change += shifted

        world = ~np.array(world_change % 2, dtype="bool")
        assessed = np.insert(assessed, len(assessed), assess_world(world, mask))
        world_str = stringify_world(world)

        if world_str in round_cache:
            # Will happen at the repeat of round #1 (rnd = 0, all tiles activated)
            ans = np.sum(assessed) * (ROUNDS // rnd) + np.sum(
                assessed[: (ROUNDS % rnd)]
            )
            break
        else:
            round_cache.add(world_str)

    print(ans)
