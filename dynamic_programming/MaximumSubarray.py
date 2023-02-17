from typing import List


# O(n) time || O(n) space
def max_sub_array(self, nums: List[int]) -> int:
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)
