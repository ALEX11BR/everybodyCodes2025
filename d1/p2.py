#!/usr/bin/env python3

from functools import reduce

import numpy as np


if __name__ == "__main__":
    names = np.array(input().split(","))
    input()
    ops = np.array(input().split(","))

    position = sum(
        map(lambda op: int(op[1:]) * (1 if op[0] == "R" else -1), ops), 0
    ) % len(names)

    ans = names[position]
    print(ans)
