from itertools import accumulate
from typing import List


# TODO: Prefix Sum
# O(n) time || O(1) space
def minimize_array_value(self, nums: List[int]) -> int:
    return max((a + i) // (i + 1) for i, a in enumerate(accumulate(nums)))


# O(n) time || O(1) space
def minimize_array_value_plain(self, nums: List[int]) -> int:
    total, res = 0, 0
    for i in range(len(nums)):
        total += nums[i]
        res = max(res, (total + i) // (i + 1))

    return res
