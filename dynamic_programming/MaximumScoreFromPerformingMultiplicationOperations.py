from functools import lru_cache
from typing import List


# O(m^2) time || O(m^2) space
def maximum_score_top_down(self, nums: List[int], multipliers: List[int]) -> int:
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


# O(m^2) time || O(m^2) space
def maximum_score_bottom_up(self, nums: List[int], multipliers: List[int]) -> int:
    n, m = len(nums), len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for left in range(i, -1, -1):
            mult = multipliers[i]
            right = n - 1 - (i - left)
            dp[i][left] = max(
                mult * nums[left] + dp[i + 1][left + 1],
                mult * nums[right] + dp[i + 1][left]
            )

    return dp[0][0]
