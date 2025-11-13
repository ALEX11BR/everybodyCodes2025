#!/usr/bin/env python3

# Takes 42s to run using CPython

import numpy as np


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")

    lines = np.array(sorted((nums[0], nums[1])), ndmin=2, dtype="int")

    ans = 0
    for i in range(2, len(nums)):
        new_line = np.array(sorted((nums[i], nums[i - 1])), ndmin=2, dtype="int")

        for line in lines:
            if line[0] in new_line[0] or line[1] in new_line[0]:
                continue
            if (
                line[0] < new_line[0][1]
                and new_line[0][0] < line[1]
                and (line[0] < new_line[0][0]) == (line[1] < new_line[0][1])
            ):
                ans += 1

        lines = np.append(lines, new_line, axis=0)

    print(ans)
