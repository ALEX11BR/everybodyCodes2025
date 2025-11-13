#!/usr/bin/env python3

# Takes 1m 29s to run using CPython

from collections import defaultdict

import numpy as np


NAILS = 256


def evaluate_pair(start1: int, end1: int, start2: int, end2: int) -> bool:
    elems2 = (start2, end2)
    if start1 in elems2 or end1 in elems2:
        return False
    if (
        start1 < end2
        and start2 < end1
        and (start1 < start2) == (end1 < end2)
    ):
        return True
    return False


if __name__ == "__main__":
    nums = np.fromstring(input(), sep=",", dtype="int")
    nums -= 1

    pair_occurrences = defaultdict(int)
    ans = 0

    for i in range(1, len(nums)):
        pair_occurrences[frozenset((int(nums[i]), int(nums[i - 1])))] += 1

    for cut_end in range(1, NAILS):
        for cut_start in range(cut_end):
            local_ans = pair_occurrences.get(frozenset((cut_start, cut_end)), 0)

            for string_ids, strings in pair_occurrences.items():
                local_ans += int(evaluate_pair(cut_start, cut_end, min(string_ids), max(string_ids))) * strings
            ans = max(ans, local_ans)

    print(ans)
