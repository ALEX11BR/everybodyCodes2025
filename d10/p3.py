#!/usr/bin/env python3

from functools import cache
import sys
from typing import Generator

import numpy as np
import numpy.typing as npt


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


def parse_world(world_str: str) -> npt.NDArray[np.str_]:
    return np.array(world_str.split("\n")[:-1])


@cache
def solve(world_str: str, dragon: tuple[int, int], sheep: tuple[tuple[int, int], ...], sheep_turn: bool = True) -> int:
    if len(sheep) == 0:
        return 1

    ans = 0
    world = parse_world(world_str)

    if not sheep_turn:
        for new_dragon in l_neighbors(dragon[0], dragon[1], len(world), len(world[0])):
            new_sheep = tuple(s for s in sheep if s != new_dragon or world[s[0]][s[1]] == "#")

            ans += solve(world_str, new_dragon, new_sheep, True)
    else:
        sheep_can_move = False

        for i in range(len(sheep)):
            new_sheep_pos = (sheep[i][0] + 1, sheep[i][1])

            if dragon == new_sheep_pos and world[dragon[0]][dragon[1]] != "#":
                continue
            elif new_sheep_pos[0] == len(world):
                sheep_can_move = True
                continue

            new_sheep = sheep[:i] + (new_sheep_pos, ) + sheep[(i+1):]
            ans += solve(world_str, dragon, new_sheep, False)
            sheep_can_move = True

        if not sheep_can_move:
            ans = solve(world_str, dragon, sheep, False)

    return ans


if __name__ == "__main__":
    world_str = sys.stdin.read()
    world = parse_world(world_str)

    dragon = next((len(world) - 1, i) for i in range(len(world[0])) if world[-1][i] == "D")
    sheep = tuple((0, i) for i in range(len(world[0])) if world[0][i] == "S")

    ans = solve(world_str, dragon, sheep)
    print(ans)
