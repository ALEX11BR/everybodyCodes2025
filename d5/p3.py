#!/usr/bin/env python3

from functools import reduce
import sys

import numpy as np
import numpy.typing as npt


def find_first(arr: npt.NDArray[np.int_], target: int, lower: bool) -> int | None:
    for i in range(len(arr)):
        if (lower and target < arr[i][0]) or ((not lower) and target > arr[i][0]):
            return i
    return None


def solve_sword(spec: str) -> tuple[int, ...]:
    spec_parts = spec.split(":")
    sword = np.fromstring(spec_parts[1], sep=",", dtype="int")

    quality_score = sword[0]
    sword_level = np.array((sword[0],))
    left = np.array((sword[0], 0), ndmin=2)
    right = np.array((sword[0], 0), ndmin=2)

    for num in sword[1:]:
        num: int

        if (rm_pos := find_first(left, num, True)) is not None:
            sword_level[left[rm_pos][1]] = (
                num * (10 ** len(str(sword_level[left[rm_pos][1]])))
                + sword_level[left[rm_pos][1]]
            )
            left = np.delete(left, rm_pos, axis=0)
            continue
        if (rm_pos := find_first(right, num, False)) is not None:
            sword_level[right[rm_pos][1]] = (
                sword_level[right[rm_pos][1]] * (10 ** len(str(num))) + num
            )
            right = np.delete(right, rm_pos, axis=0)
            continue

        quality_score = quality_score * (10 ** len(str(num))) + num
        left = np.append(left, np.array((num, len(sword_level)), ndmin=2), axis=0)
        right = np.append(right, np.array((num, len(sword_level)), ndmin=2), axis=0)
        sword_level = np.append(sword_level, num)

    return (quality_score,) + tuple(sword_level) + (int(spec_parts[0]),)


if __name__ == "__main__":
    swords = sorted((solve_sword(line.strip()) for line in sys.stdin), reverse=True)

    ans = reduce(
        lambda acc, sword: acc + (1 + sword[0]) * sword[1][-1], enumerate(swords), 0
    )
    print(ans)
