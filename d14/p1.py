#!/usr/bin/env python3

import numpy as np


ROUNDS = 10


if __name__ == "__main__":
    world = np.empty(shape=0, dtype="bool")
    while True:
        try:
            line = input()
            line_matrix = np.fromiter((c == "#" for c in line), dtype="bool")
            world = np.append(world, line_matrix)
        except EOFError:
            break
    world = np.reshape(world, shape=(-1, len(line_matrix)))

    ans = 0
    for _ in range(ROUNDS):
        world_change = np.array(world, dtype="int")
        for shift_0 in (-1, 1):
            for shift_1 in (-1, 1):
                shifted = np.roll(world, shift_0, 0)
                shifted = np.roll(shifted, shift_1, 1)

                shifted[min(shift_0, 0), :] = 0
                shifted[:, min(shift_1, 0)] = 0

                world_change += shifted

        world = ~np.array(world_change % 2, dtype="bool")
        ans += np.count_nonzero(world)

    print(ans)
