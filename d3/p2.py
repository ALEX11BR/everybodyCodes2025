#!/usr/bin/env python3


if __name__ == "__main__":
    nums = set(int(el) for el in input().split(","))

    ans = sum(sorted(nums)[:20])
    print(ans)
