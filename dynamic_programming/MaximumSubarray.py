from typing import List


# O(n) time || O(n) space
def max_sub_array(self, nums: List[int]) -> int:
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)


# O(n) time || O(1) space
def max_sub_array_const(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])

    return max(nums)
