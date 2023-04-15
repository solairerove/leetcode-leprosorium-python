from typing import List


# O(n) time || O(1) space
def get_max_len(self, nums: List[int]) -> int:
    n = len(nums)
    pos, neg = 0, 0

    if nums[0] > 0:
        pos = 1

    if nums[0] < 0:
        neg = 1

    res = pos
    for i in range(1, n):
        if nums[i] > 0:
            pos = 1 + pos
            neg = 1 + neg if neg > 0 else 0
        elif nums[i] < 0:
            pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
        else:
            pos, neg = 0, 0

        res = max(res, pos)

    return res
