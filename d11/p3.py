#!/usr/bin/env python3

import sys

import numpy as np


if __name__ == "__main__":
    birds = np.fromstring(sys.stdin.read(), dtype="int", sep="\n")

    target = int(np.mean(birds))
    ans = sum(elem - target for elem in birds if elem > target)

    print(ans)
