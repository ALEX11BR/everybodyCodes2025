#!/usr/bin/env python3

import numpy as np


WALL_LEN = 90


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")

    ans = sum(WALL_LEN // nums)
    print(ans)
