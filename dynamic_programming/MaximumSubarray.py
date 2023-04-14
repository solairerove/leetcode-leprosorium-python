from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def max_sub_array(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])

    return max(nums)


# O(n) time || O(n) space
def max_sub_array_top_down(self, nums: List[int]) -> int:
    @lru_cache(None)
    def dp(i, should_pick):
        if i >= len(nums):
            return 0 if should_pick else float('-inf')

        return max(nums[i] + dp(i + 1, True), 0 if should_pick else dp(i + 1, False))

    return dp(0, False)


# O(n) time || O(n) space
def max_sub_array_bottom_up(self, nums: List[int]) -> int:
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)
