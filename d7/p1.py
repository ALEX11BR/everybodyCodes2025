#!/usr/bin/env python3

import re

import numpy as np


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

    for name in names:
        ok = True
        for i in range(len(name) - 1):
            if name[i + 1] not in char_next[name[i]]:
                ok = False
                break

        if ok:
            ans = name
            break

    print(ans)
