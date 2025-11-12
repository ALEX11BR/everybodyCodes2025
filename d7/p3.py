#!/usr/bin/env python3

import re

import numpy as np


MIN_LEN = 7
MAX_LEN = 11


if __name__ == "__main__":
    names = np.array(input().split(","))
    input()
    char_next = {}
    while True:
        try:
            char_line = input()
            parsed = re.fullmatch(r"(.) > (.*)", char_line)
            char_next[parsed[1]] = np.array(parsed[2].split(","))
        except EOFError:
            break

    possibilities = {
        c: np.array((len(cnext),), dtype="int") for c, cnext in char_next.items()
    }
    for i in range(MAX_LEN - 1):
        for c in char_next:
            possibilities[c] = np.append(
                possibilities[c],
                sum(
                    possibilities[next_c][i] if next_c in possibilities else 0
                    for next_c in char_next[c]
                ),
            )

    ans = 0
    for j in range(len(names)):
        name = names[j]
        if any(
            name != other_name and name.startswith(other_name) for other_name in names
        ):
            continue

        ok = True
        for i in range(len(name) - 1):
            if name[i + 1] not in char_next[name[i]]:
                ok = False
                break

        if ok:
            ans += sum(
                possibilities[name[-1]][i]
                for i in range(MIN_LEN - len(name) - 1, MAX_LEN - len(name))
            )

    print(ans)
