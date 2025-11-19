#!/usr/bin/env python3

import sys

import numpy as np


ROTATE_BY = 2025


if __name__ == "__main__":
    nums = np.fromstring(sys.stdin.read(), dtype="int", sep="\n")

    ordered_nums = np.concat(
        (
            np.array((1,)),
            nums[0 : len(nums) : 2],
            nums[(len(nums) - 1 - len(nums) % 2) : 0 : -2],
        )
    )

    ans = ordered_nums[ROTATE_BY % len(ordered_nums)]
    print(ans)
