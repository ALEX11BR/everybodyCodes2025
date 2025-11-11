#!/usr/bin/env python3

from collections import defaultdict


if __name__ == "__main__":
    people = input()

    mentors = defaultdict(int)

    ans = 0
    for el in people:
        if el.isupper():
            mentors[el.lower()] += 1
        else:
            ans += mentors[el]
    print(ans)
