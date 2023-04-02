from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def can_jump_greedy(self, nums: List[int]) -> bool:
    high = 0
    for i, n in enumerate(nums):
        if i > high:
            return False
        high = max(high, i + n)

    return True


# O(n) time || O(n) space TLE
def can_jump_top_down(self, nums: List[int]) -> bool:
    n = len(nums)

    @lru_cache(n)
    def dp(i):
        if i == n - 1:
            return True

        if nums[i] == 0:
            return False

        for j in range(i + 1, min(i + nums[i], n - 1) + 1):
            if dp(j):
                return True

        return False

    return dp(0)
