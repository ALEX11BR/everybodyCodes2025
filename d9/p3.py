#!/usr/bin/env python3

# Takes 2m 33s to run using CPython

from collections import defaultdict

import numpy as np


class DisjointSet:
    def __init__(self, elem_count: int):
        self.parents = np.array(range(elem_count), dtype="int")

    def find(self, elem_id: int) -> int:
        while self.parents[elem_id] != elem_id:
            elem_id, self.parents[elem_id] = (
                self.parents[elem_id],
                self.parents[self.parents[elem_id]],
            )
        return int(elem_id)

    def union(self, id1: int, id2: int):
        set1 = self.find(id1)
        set2 = self.find(id2)

        self.parents[set2] = set1


if __name__ == "__main__":
    elems = None
    while True:
        try:
            elem = input().split(":")[1]
            if elems is None:
                elems = np.array(elem, ndmin=1)
            else:
                elems = np.append(elems, elem)
        except EOFError:
            break

    families = DisjointSet(len(elems))

    for child in range(len(elems)):
        child_done = False

        for parent1 in range(len(elems) - 1):
            if parent1 == child:
                continue

            for parent2 in range(parent1 + 1, len(elems)):
                if parent2 == child:
                    continue

                ok = True
                for i in range(len(elems[0])):
                    local_ok = False

                    if elems[child][i] == elems[parent1][i]:
                        local_ok = True
                    if elems[child][i] == elems[parent2][i]:
                        local_ok = True

                    if not local_ok:
                        ok = False
                        break

                if ok:
                    families.union(child, parent1)
                    families.union(child, parent2)
                    child_done = True
                    break

            if child_done:
                break

    family_sizes = defaultdict(lambda: np.array((0, 0)))
    for i in range(len(elems)):
        dinasty = families.find(i)
        family_sizes[dinasty][0] += 1
        family_sizes[dinasty][1] += i + 1

    ans = int(max(family_sizes.values(), key=lambda f: f[0])[1])
    print(ans)
