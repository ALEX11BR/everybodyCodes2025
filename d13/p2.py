#!/usr/bin/env python3

import numpy as np


ROTATE_BY = 20252025


if __name__ == "__main__":
    left_nums = np.empty(shape=0, dtype="int")
    right_nums = np.empty(shape=0, dtype="int")
    right_side = True

    while True:
        try:
            line = input()
            line_nums = np.fromstring(line, sep="-", dtype="int")

            if right_side:
                right_nums = np.append(
                    right_nums, range(line_nums[0], line_nums[1] + 1)
                )
            else:
                left_nums = np.append(
                    range(line_nums[1], line_nums[0] - 1, -1), left_nums
                )

            right_side = not right_side
        except EOFError:
            break

    ordered_nums = np.concat(
        (
            np.array((1,)),
            right_nums,
            left_nums,
        )
    )

    ans = ordered_nums[ROTATE_BY % len(ordered_nums)]
    print(ans)
