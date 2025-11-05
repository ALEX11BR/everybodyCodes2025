#!/usr/bin/env pypy3
# Note: running the solution using the regular CPython takes a while on my unoptimized solution, PyPy takes ~0,5s

from dataclasses import dataclass
import re
from typing import Self


def neg_div(a: int, b: int) -> int:
    if a > 0:
        return a // b
    return (a + b - 1) // b


@dataclass(repr=False)
class Num:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Num(self.x + other.x, self.y + other.y)

    def __mul__(self, other: Self) -> Self:
        return Num(
            self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        )

    def __truediv__(self, other: Self) -> Self:
        return Num(neg_div(self.x, other.x), neg_div(self.y, other.y))

    def __repr__(self):
        return f"[{self.x},{self.y}]"


if __name__ == "__main__":
    inp = input()

    inp_match = re.match(r"A=\[([-0-9]+),([-0-9]+)\]", inp)

    topleft = Num(int(inp_match[1]), int(inp_match[2]))
    ans = 0

    arr = [[False for _ in range(101)] for _ in range(101)]

    for x in range(topleft.x, topleft.x + 1001):
        for y in range(topleft.y, topleft.y + 1001):
            a = Num(x, y)
            det = Num(0, 0)
            good_point = True

            for k in range(100):
                det *= det
                det /= Num(100000, 100000)
                det += a

                if abs(det.x) > 1000000 or abs(det.y) > 1000000:
                    good_point = False
                    break
            if good_point:
                ans += 1
            arr[(x - topleft.x) // 10][(y - topleft.y) // 10] = good_point
    print(ans)
