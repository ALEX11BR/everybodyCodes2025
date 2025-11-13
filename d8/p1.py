#!/usr/bin/env python3

import numpy as np


NAILS = 32


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")

    ans = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) == (NAILS // 2):
            ans += 1
    print(ans)
