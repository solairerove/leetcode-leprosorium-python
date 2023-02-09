from functools import lru_cache
from typing import List


# O(n) time || O(n) space
def maximum_score(self, nums: List[int], multipliers: List[int]) -> int:
    n, m = len(nums), len(multipliers)

    @lru_cache(None)
    def dp(i: int, left: int) -> int:
        if i == m:
            return 0

        mult = multipliers[i]
        right = n - 1 - (i - left)

        return max(
            mult * nums[left] + dp(i + 1, left + 1),
            mult * nums[right] + dp(i + 1, left)
        )

    return dp(0, 0)
