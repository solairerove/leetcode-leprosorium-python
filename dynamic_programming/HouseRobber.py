from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    prev_rob1 = prev_rob2 = 0
    for n in nums:
        prev_rob1, prev_rob2 = prev_rob2, max(prev_rob2, prev_rob1 + n)

    return prev_rob2


# O(n) time || O(n) space
def rob_rec(self, nums: List[int]) -> int:
    @lru_cache(None)
    def helper(ith: int) -> int:
        if ith >= len(nums):
            return 0

        return max(helper(ith + 1), helper(ith + 2) + nums[ith])

    return helper(0)
