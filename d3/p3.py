#!/usr/bin/env python3

from collections import defaultdict

import numpy as np


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",")
    occs = defaultdict(lambda: 0)

    for num in nums:
        occs[num] += 1

    ans = max(occs.values())
    print(ans)
