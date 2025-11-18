#!/usr/bin/env python3

import sys

import numpy as np


ROUNDS = 10


if __name__ == "__main__":
    birds = np.fromstring(sys.stdin.read(), dtype="int", sep="\n")

    second_round = False
    for _ in range(ROUNDS):
        if all(birds[i - 1] <= birds[i] for i in range(1, len(birds))):
            second_round = True
        for i in range(1, len(birds)):
            if not second_round and birds[i] < birds[i - 1]:
                birds[i - 1] -= 1
                birds[i] += 1
            if second_round and birds[i - 1] < birds[i]:
                birds[i] -= 1
                birds[i - 1] += 1

    ans = sum((i + 1) * count for i, count in enumerate(birds))
    print(ans)
