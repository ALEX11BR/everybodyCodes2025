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

    maybe_children = set(range(len(elems)))
    i = 0
    while len(maybe_children) > 1 and i < len(elems[0]):
        to_remove = set()
        for c in maybe_children:
            if elems[c][i] not in {elems[j][i] for j in range(len(elems)) if j != c}:
                to_remove.add(c)
        maybe_children -= to_remove
        i += 1

    child = maybe_children.pop()
    ans = 1
    for parent in range(len(elems)):
        if child == parent:
            continue
        local_ans = 0
        for i in range(len(elems[0])):
            local_ans += int(elems[child][i] == elems[parent][i])
        ans *= local_ans
    print(ans)
