#!/usr/bin/env python3

import numpy as np


RADIUS = 10


if __name__ == "__main__":
    nums = None
    while True:
        try:
            line_str = input()
            if (at_column := line_str.find("@")) != -1:
                at_pos = (nums.shape[0] if nums is not None else 0, at_column)

            line = np.reshape(
                np.fromiter(
                    map(lambda x: int(x) if x != "@" else 0, line_str), dtype="int"
                ),
                shape=(1, -1),
            )

            if nums is None:
                nums = line
            else:
                nums = np.append(nums, line, axis=0)
        except EOFError:
            break

    mask = np.reshape(
        np.fromiter(
            (
                (i - at_pos[0]) ** 2 + (j - at_pos[1]) ** 2 <= RADIUS ** 2
                for i in range(nums.shape[0])
                for j in range(nums.shape[1])
            ),
            dtype="bool",
        ),
        shape=nums.shape,
    )

    ans = np.sum(nums, where=mask)
    print(ans)
