from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    def helper(arr: List[int]) -> int:
        rob1 = rob2 = 0
        for n in arr:
            rob1, rob2 = rob2, max(rob1 + n, rob2)

        return rob2

    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


# O(n) time || O(n) space
def rob_rec(self, nums: List[int]) -> int:
    def classic_rob_rec(arr: List[int]) -> int:
        @lru_cache(None)
        def helper(ith: int) -> int:
            if ith >= len(arr):
                return 0

            return max(helper(ith + 1), helper(ith + 2) + arr[ith])

        return helper(0)

    return max(nums[0], classic_rob_rec(nums[1:]), classic_rob_rec(nums[:-1]))
