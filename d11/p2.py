#!/usr/bin/env python3

# Takes 2m 45s to run using CPython

import sys

import numpy as np


if __name__ == "__main__":
    birds = np.fromstring(sys.stdin.read(), dtype="int", sep="\n")

    second_round = False
    ans = 0
    while any(birds[i] != birds[i - 1] for i in range(1, len(birds))):
        ans += 1
        if all(birds[i - 1] <= birds[i] for i in range(1, len(birds))):
            second_round = True
        for i in range(1, len(birds)):
            if not second_round and birds[i] < birds[i - 1]:
                birds[i - 1] -= 1
                birds[i] += 1
            if second_round and birds[i - 1] < birds[i]:
                birds[i] -= 1
                birds[i - 1] += 1

    print(ans)
