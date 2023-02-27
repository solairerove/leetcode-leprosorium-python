from functools import lru_cache
from typing import List


# O(t * n) time || O(t * n) space, where t sum of nums
def find_target_sum_ways(self, nums: List[int], target: int) -> int:
    dp = {}  # (index, total) -> # of ways

    def backtracking(i, total):
        if i == len(nums):
            return 1 if total == target else 0

        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = backtracking(i + 1, total + nums[i]) + backtracking(i + 1, total - nums[i])

        return dp[(i, total)]

    return backtracking(0, 0)


# O(t * n) time || O(t * n) space, where t sum of nums
def find_target_sum_ways_top_down(self, nums: List[int], target: int) -> int:
    @lru_cache(None)
    def dp(i, total):
        if i == len(nums):
            return [0, 1][total == target]

        return dp(i + 1, total + nums[i]) + dp(i + 1, total + -nums[i])

    return dp(0, 0)
