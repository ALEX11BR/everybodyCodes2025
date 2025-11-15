#!/usr/bin/env python3

from typing import Generator

import numpy as np
import numpy.typing as npt


MOVES = 4


def l_neighbors(
    start_line: int, start_column: int, map_lines: int, map_columns: int
) -> Generator[tuple[int, int], None, None]:
    for i in range(8):
        point = (
            start_line + (1 + i % 2) * (1 if i & 2 else -1),
            start_column + (2 - i % 2) * (1 if i & 4 else -1),
        )
        if (
            point[0] >= 0
            and point[1] >= 0
            and point[0] < map_lines
            and point[1] < map_columns
        ):
            yield point


def l_reachable(
    dragon_line: int, dragon_column: int, map_lines: int, map_columns: int
) -> npt.NDArray[np.bool_]:
    ans = np.zeros(shape=(map_lines, map_columns), dtype="bool")
    ans[dragon_line][dragon_column] = True

    last_gen = {(dragon_line, dragon_column)}
    for _ in range(MOVES):
        new_gen = set()

        for e_line, e_column in last_gen:
            new_gen.update(l_neighbors(e_line, e_column, map_lines, map_columns))

        for e_line, e_column in new_gen:
            ans[e_line][e_column] = True

        last_gen = new_gen

    return ans


if __name__ == "__main__":
    world = None
    start_line = 0
    start_column = -1
    while True:
        try:
            line = input()
            if world is None:
                world = np.array(line, ndmin=1)
            else:
                world = np.append(world, line)

            if start_column == -1:
                start_column = line.find("D")
            if start_column == -1:
                start_line += 1
        except EOFError:
            break

    reachable = l_reachable(start_line, start_column, len(world), len(world[0]))
    ans = sum(
        int(reachable[i][j] and world[i][j] == "S")
        for i in range(len(world))
        for j in range(len(world[0]))
    )

    print(ans)
