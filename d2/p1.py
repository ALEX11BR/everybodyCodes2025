#!/usr/bin/env python3

from dataclasses import dataclass
import re
from typing import Self


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
        return Num(self.x // other.x, self.y // other.y)

    def __repr__(self):
        return f"[{self.x},{self.y}]"


if __name__ == "__main__":
    inp = input()

    inp_match = re.match(r"A=\[([0-9]+),([0-9]+)\]", inp)

    a = Num(int(inp_match[1]), int(inp_match[2]))
    ans = Num(0, 0)
    for _ in range(3):
        ans *= ans
        ans /= Num(10, 10)
        ans += a
    print(ans)
