#!/usr/bin/env python3

import numpy as np


if __name__ == "__main__":
    start_gear = None
    end_gear = None
    speed = 1

    while True:
        try:
            line = input()

            if start_gear is None:
                start_gear = int(line)
                continue

            if "|" in line:
                nums = np.fromstring(line, sep="|")
                speed *= nums[1] / nums[0]
            else:
                end_gear = int(line)

        except EOFError:
            break

    ans = int(100 * speed * start_gear / end_gear)
    print(ans)
