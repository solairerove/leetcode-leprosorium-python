from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    prev = curr = 0
    for n in nums:
        prev, curr = curr, max(curr, prev + n)

    return curr


# O(n) time || O(n) space
def rob_top_down(self, nums: List[int]) -> int:
    @lru_cache(None)
    def dp(i: int) -> int:
        if i == 0:
            return nums[0]

        if i == 1:
            return max(nums[0], nums[1])

        return max(dp(i - 1), dp(i - 2) + nums[i])

    return dp(len(nums) - 1)


# O(n) time || O(n) space
def rob_bottom_up(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]
