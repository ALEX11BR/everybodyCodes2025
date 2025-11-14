#!/usr/bin/env python3

import numpy as np


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

    ans = 0

    child_set = np.zeros(shape=len(elems), dtype="bool")
    for parent1 in range(len(elems) - 1):
        for parent2 in range(parent1 + 1, len(elems)):
            for child in range(len(elems)):
                if child in {parent1, parent2} or child_set[child]:
                    continue

                ok = True
                score1 = 0
                score2 = 0
                for i in range(len(elems[0])):
                    local_ok = False

                    if elems[child][i] == elems[parent1][i]:
                        score1 += 1
                        local_ok = True
                    if elems[child][i] == elems[parent2][i]:
                        score2 += 1
                        local_ok = True

                    if not local_ok:
                        ok = False
                        break

                if ok:
                    child_set[child] = True
                    child_set[parent1] = True
                    child_set[parent2] = True

                    ans += score1 * score2

    print(ans)
