#!/usr/bin/env python3

from functools import reduce

import numpy as np


if __name__ == "__main__":
    names = np.array(input().split(","))
    input()
    ops = np.array(input().split(","))

    position = reduce(
        lambda prev_pos, move_by: max(0, min(len(names) - 1, prev_pos + move_by)),
        map(lambda op: int(op[1:]) * (1 if op[0] == "R" else -1), ops),
        0,
    )

    ans = names[position]
    print(ans)
