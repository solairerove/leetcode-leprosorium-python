from typing import List


# O(n) time || O(1) space
def length_of_lis(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)
