from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    rob1 = rob2 = 0
    for n in nums:
        rob1, rob2 = rob2, max(n + rob1, rob2)

    return rob2


# O(n) time || O(n) space
def rob_rec(self, nums: List[int]) -> int:
    @lru_cache(None)
    def helper(ith: int) -> int:
        if ith >= len(nums):
            return 0

        return max(helper(ith + 1), helper(ith + 2) + nums[ith])

    return helper(0)
