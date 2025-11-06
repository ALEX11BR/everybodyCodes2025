#!/usr/bin/env python3

import sys

import numpy as np


if __name__ == "__main__":
    gears = np.fromstring(sys.stdin.read(), sep="\n")

    ans = int(2025 * gears[0] / gears[-1])
    print(ans)
