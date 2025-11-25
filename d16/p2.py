#!/usr/bin/env python3

import numpy as np


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")

    periods = np.empty(shape=0, dtype="int")
    for i in range(len(nums)):
        if nums[i] > sum(1 for p in periods if (i + 1) % p == 0):
            periods = np.append(periods, i + 1)

    ans = np.prod(periods)
    print(ans)
