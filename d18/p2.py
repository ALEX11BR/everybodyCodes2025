#!/usr/bin/env python3

from dataclasses import dataclass, field
from functools import cache
import re
import sys

import numpy as np


@dataclass(unsafe_hash=True)
class Plant:
    num: int
    thickness: int
    branches: tuple[tuple[int, int], ...] = field(default_factory=tuple)


@cache
def compute_energy(plant_id: int, plants: tuple[Plant, ...], activation: int) -> int:
    ans = 0
    for src, thickness in plants[plant_id - 1].branches:
        if src <= -1:
            if activation & (1 << (plant_id - 1)):
                ans += thickness
            continue

        ans += thickness * compute_energy(src, plants, activation)

    if ans < plants[plant_id - 1].thickness:
        return 0
    return ans


if __name__ == "__main__":
    plant = None
    last_plant = 0
    plants = tuple()
    core_plants = 0
    activations = None

    for line in sys.stdin.readlines():
        if activations is not None:
            values = np.fromstring(line[:-1], dtype="bool", sep=" ")
            mask = int(
                np.sum(
                    np.fromiter(map(lambda n: 1 << n, range(len(values))), dtype="int"),
                    where=values,
                )
            )
            activations += (mask,)
        elif plant is None:
            if line_match := re.match("Plant ([0-9]*) with thickness ([0-9]*)", line):
                plant = Plant(int(line_match[1]), int(line_match[2]))
                plants += (plant,)
            else:
                activations = tuple()
        else:
            if line_match := re.match(
                "- (free )?branch( to Plant )?([0-9]*)? with thickness ([-0-9]*)", line
            ):
                source = -1 if line_match[1] is not None else int(line_match[3])
                thickness = int(line_match[4])

                plant.branches += ((source, thickness),)

                if line_match[1] is not None:
                    core_plants += 1
            else:
                last_plant = plant.num
                plant = None

    ans = sum(
        compute_energy(last_plant, plants, activation) for activation in activations
    )
    print(ans)
