#!/usr/bin/env python3

from functools import reduce

import numpy as np


if __name__ == "__main__":
    names = np.array(input().split(","))
    input()
    ops = np.array(input().split(","))

    for op in ops:
        op_id = (int(op[1:]) * (1 if op[0] == "R" else -1)) % len(names)

        temp = names[0]
        names[0] = names[op_id]
        names[op_id] = temp

    ans = names[0]
    print(ans)
