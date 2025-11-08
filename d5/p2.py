#!/usr/bin/env python3

import sys

import numpy as np
import numpy.typing as npt


def find_first(arr: npt.NDArray[np.int_], target: int, lower: bool) -> int | None:
    for i in range(len(arr)):
        if (lower and target < arr[i]) or ((not lower) and target > arr[i]):
            return i
    return None


def solve_sword(spec: str) -> int:
    sword = np.fromstring(spec.split(":")[1], sep=",", dtype="int")

    ans = sword[0]
    left = np.array((sword[0],))
    right = np.array((sword[0],))

    for num in sword[1:]:
        if (rm_pos := find_first(left, num, True)) is not None:
            left = np.delete(left, rm_pos)
            continue
        if (rm_pos := find_first(right, num, False)) is not None:
            right = np.delete(right, rm_pos)
            continue

        ans = ans * (10 ** len(str(num))) + num
        left = np.append(left, num)
        right = np.append(right, num)

    return ans


if __name__ == "__main__":
    scores = np.fromiter((solve_sword(line.strip()) for line in sys.stdin), dtype="int")

    ans = max(scores) - min(scores)
    print(ans)
