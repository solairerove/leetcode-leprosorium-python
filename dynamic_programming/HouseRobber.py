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
