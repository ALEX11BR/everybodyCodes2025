#!/usr/bin/env python3

from dataclasses import dataclass, field
import re
import sys


@dataclass
class Plant:
    num: int
    thickness: int
    branches: dict[int, int] = field(default_factory=dict)


def compute_energy(plant_id: int, plants: dict[int, Plant]) -> int:
    ans = 0
    for src in plants[plant_id].branches:
        if src <= -1:
            ans += plants[plant_id].branches[src]
            continue

        ans += plants[plant_id].branches[src] * compute_energy(src, plants)

    if ans < plants[plant_id].thickness:
        return 0
    return ans


if __name__ == "__main__":
    plant = None
    plants = {}
    for line in sys.stdin.readlines():
        if plant is None:
            line_match = re.match("Plant ([0-9]*) with thickness ([0-9]*)", line)
            plant = Plant(int(line_match[1]), int(line_match[2]))
            plants[plant.num] = plant
        else:
            if line_match := re.match(
                "- (free )?branch( to Plant )?([0-9]*)? with thickness ([0-9]*)", line
            ):
                source = -1 if line_match[1] is not None else int(line_match[3])
                thickness = int(line_match[4])

                plant.branches[source] = thickness
            else:
                plant = None

    ans = compute_energy(plant.num, plants)
    print(ans)
