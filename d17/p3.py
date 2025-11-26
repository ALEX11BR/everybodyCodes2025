#!/usr/bin/env python3

# Takes 16s to run using CPython

from dataclasses import dataclass, field
from typing import Generator

import numpy as np
import numpy.typing as npt


CIRCLE_TIME = 30


@dataclass
class MyHeap:
    """
    My personal challenge is not to construct Python lists
    So, instead of using heapq, I reimplemented it
    """

    value: tuple[int, tuple[int, int], bool] | None
    left: MyHeap | None = field(default=None)
    right: MyHeap | None = field(default=None)
    left_h: int = field(default=0)
    right_h: int = field(default=0)

    def push(self, elem: tuple[int, tuple[int, int], bool]):
        if self.value is None or elem < self.value:
            old_value = self.value
            self.value = elem
            if old_value is not None:
                self.push(old_value)
            return

        if self.left_h < self.right_h:
            self.left_h += 1
            if self.left is None:
                self.left = MyHeap(elem)
            else:
                self.left.push(elem)
        else:
            self.right_h += 1
            if self.right is None:
                self.right = MyHeap(elem)
            else:
                self.right.push(elem)

    def pop(self) -> tuple[int, tuple[int, int], bool]:
        ans = self.value

        if self.left is not None and (
            self.right is None or self.left.value < self.right.value
        ):
            self.left_h -= 1
            self.value = self.left.pop()
            if self.left.value is None:
                self.left = None
        elif self.right is not None:
            self.right_h -= 1
            self.value = self.right.pop()
            if self.right.value is None:
                self.right = None
        else:
            self.value = None

        return ans


def neighbors(
    start_line: int,
    start_column: int,
    mask: npt.NDArray[np.bool_],
    at_point: tuple[int, int],
) -> Generator[tuple[int, int], None, None]:
    for i in range(4):
        point = (
            start_line + (i % 2) * (1 if i & 2 else -1),
            start_column + (1 - i % 2) * (1 if i & 2 else -1),
        )
        if (
            point[0] >= 0
            and point[1] >= 0
            and point[0] < mask.shape[0]
            and point[1] < mask.shape[1]
            and not mask[point]
            and (
                start_line != at_point[0]
                or start_column > at_point[1]
                or point[0] > start_line
            )
        ):
            yield point


def dijkstra(
    start: tuple[int, int],
    end: int,
    nums: npt.NDArray[np.int_],
    mask: npt.NDArray[np.bool_],
    at_pos: tuple[int, int],
) -> int:
    dists = set()
    q = MyHeap((0, start, False))

    while q.value is not None:
        dist, node, quarter = q.pop()
        if (node, quarter) in dists:
            continue

        dists.add((node, quarter))

        if node == start and quarter:
            return dist
        if dist > end:
            return dist

        for neighbor in neighbors(node[0], node[1], mask, at_pos):
            neigh_dist = int(dist + nums[neighbor])
            q.push(
                (
                    neigh_dist,
                    neighbor,
                    quarter or (node[0] == at_pos[0] and node[1] < at_pos[1]),
                )
            )


if __name__ == "__main__":
    nums = None
    while True:
        try:
            line_str = input()
            if (at_column := line_str.find("@")) != -1:
                at_pos = (nums.shape[0] if nums is not None else 0, at_column)
            if (s_column := line_str.find("S")) != -1:
                s_pos = (nums.shape[0] if nums is not None else 0, s_column)

            line = np.reshape(
                np.fromiter(
                    map(lambda x: int(x) if x not in "S@" else 0, line_str), dtype="int"
                ),
                shape=(1, -1),
            )

            if nums is None:
                nums = line
            else:
                nums = np.append(nums, line, axis=0)
        except EOFError:
            break

    for r in range(
        1,
        min(
            at_pos[0],
            at_pos[1],
            nums.shape[0] - at_pos[0] - 1,
            nums.shape[1] - at_pos[1] - 1,
        )
        + 1,
    ):
        mask = np.reshape(
            np.fromiter(
                (
                    (i - at_pos[0]) ** 2 + (j - at_pos[1]) ** 2
                    in range((r - 1) ** 2 + 1, r**2 + 1)
                    for i in range(nums.shape[0])
                    for j in range(nums.shape[1])
                ),
                dtype="bool",
            ),
            shape=nums.shape,
        )

        time_to_finish = dijkstra(s_pos, CIRCLE_TIME * (r + 1), nums, mask, at_pos)
        if time_to_finish < CIRCLE_TIME * (r + 1):
            ans = time_to_finish * r
            break

    print(ans)
