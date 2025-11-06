#!/usr/bin/env python3

from math import ceil
import sys

import numpy as np


if __name__ == "__main__":
    gears = np.fromstring(sys.stdin.read(), sep="\n")

    ans = ceil(10000000000000 * gears[-1] / gears[0])
    print(ans)
