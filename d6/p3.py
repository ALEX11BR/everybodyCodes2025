#!/usr/bin/env python3


MAP_PERIOD = 1000
MENTOR_WINDOW = 1000


if __name__ == "__main__":
    people = input()
    ans = 0

    for i in range(MENTOR_WINDOW):
        if not people[i].isupper():
            ans += people[(-MENTOR_WINDOW + i) :].count(people[i].upper())

        if not people[-1 - i].isupper():
            ans += people[: (MENTOR_WINDOW - i)].count(people[-1 - i].upper())

    ans *= MAP_PERIOD - 1

    for i in range(len(people)):
        if people[i].isupper():
            continue
        ans += (
            people[
                max(0, i - MENTOR_WINDOW) : min(len(people), i + MENTOR_WINDOW + 1)
            ].count(people[i].upper())
            * MAP_PERIOD
        )

    print(ans)
