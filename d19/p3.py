#!/usr/bin/env python3

import numpy as np


if __name__ == "__main__":
    lines = None
    while True:
        try:
            line = np.reshape(
                np.fromstring(input(), sep=",", dtype="int"), newshape=(1, -1)
            )
            if lines is None:
                lines = line
            else:
                if lines[-1, 0] == line[0, 0]:
                    continue
                lines = np.append(lines, line, axis=0)
        except EOFError:
            break

    def target_height_of(i: int) -> tuple[int, int]:
        return (lines[i, 1] + abs(lines[i, 1] % 2 - lines[i, 0] % 2), i)

    target_pos = max(range(len(lines)), key=target_height_of)
    target_height = target_height_of(target_pos)[0]
    ans = target_height + (lines[target_pos, 0] - target_height) // 2

    while target_pos + 1 < len(lines):
        new_target_pos = max(range(target_pos + 1, len(lines)), key=target_height_of)
        new_target_height = max(
            target_height_of(new_target_pos)[0],
            target_height - lines[new_target_pos, 0] + lines[target_pos, 0],
        )
        new_target_on_level = lines[target_pos, 0] + target_height - new_target_height
        ans += (lines[new_target_pos, 0] - new_target_on_level) // 2

        target_pos = new_target_pos
        target_height = new_target_height

    print(ans)
