#!/usr/bin/env python3

# Takes 1m 5s to run using CPython

from collections import deque
import sys
from typing import Generator

import numpy as np
import numpy.typing as npt


def neighbors(
    point: tuple[int, int], world_size: tuple[int, int]
) -> Generator[tuple[int, int], None, None]:
    for i in range(4):
        candidate = (
            point[0] + (0 if i & 2 else (-1) ** (i & 1)),
            point[1] + ((-1) ** (1 - (i & 1)) if i & 2 else 0),
        )
        if (
            candidate[0] >= 0
            and candidate[1] >= 0
            and candidate[0] < world_size[0]
            and candidate[1] < world_size[1]
        ):
            yield candidate


def evaluate_point(
    point: tuple[int, int], visited: npt.NDArray[np.bool_]
) -> tuple[int, npt.NDArray[np.bool_]]:
    visited = np.copy(visited)
    q = deque()
    q.append(point)
    ans = 0

    while q:
        elem = q.popleft()
        if visited[elem]:
            continue

        visited[elem] = True
        ans += 1
        for neigh in neighbors(elem, barrels.shape):
            if barrels[neigh] <= barrels[elem]:
                q.append(neigh)

    return ans, visited


if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    barrels = np.array(tuple(int(c) for l in input_lines for c in l[:-1]), dtype="int")
    barrels = np.reshape(barrels, shape=(len(input_lines), -1))
    visited = np.zeros_like(barrels, dtype="bool")

    ans = 0
    for _ in range(3):
        best_ans = 0
        for i in range(barrels.shape[0]):
            for j in range(barrels.shape[1]):
                if visited[i, j]:
                    continue

                local_ans, local_visited = evaluate_point((i, j), visited)

                if local_ans > best_ans:
                    best_ans = local_ans
                    best_visited = local_visited

        ans += best_ans
        visited = best_visited

    print(ans)
