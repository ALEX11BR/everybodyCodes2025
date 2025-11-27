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
def compute_energy(
    plant_id: int, plants: tuple[Plant, ...], activation: tuple[bool, ...]
) -> int:
    ans = 0
    for src, thickness in plants[plant_id - 1].branches:
        if src <= -1:
            if activation[plant_id - 1]:
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
    optimal_config = None
    activations = None

    for line in sys.stdin.readlines():
        line = line.strip("\n")

        if activations is not None:
            values = np.fromstring(line, dtype="bool", sep=" ")
            activations += (tuple(values),)
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

                if line_match[1] is None:
                    if optimal_config is None:
                        optimal_config = np.zeros(plant.num - 1, dtype="bool")

                    if len(plants[source - 1].branches) == 1:
                        optimal_config[source - 1] = thickness > 0
            else:
                last_plant = plant.num
                plant = None

    optimal_energy = compute_energy(last_plant, plants, tuple(optimal_config))
    ans = sum(
        map(
            lambda e: optimal_energy - e,
            filter(
                lambda e: e > 0,
                map(
                    lambda activation: compute_energy(last_plant, plants, activation),
                    activations,
                ),
            ),
        )
    )
    print(ans)
