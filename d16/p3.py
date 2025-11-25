#!/usr/bin/env python3

from bisect import bisect

import numpy as np


BLOCKS = 202520252025000


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")

    periods = np.empty(shape=0, dtype="int")
    for i in range(len(nums)):
        if nums[i] > sum(1 for p in periods if (i + 1) % p == 0):
            periods = np.append(periods, i + 1)

    ans = bisect(range(BLOCKS), BLOCKS, key=lambda l: np.sum(l // periods)) - 1
    print(ans)
