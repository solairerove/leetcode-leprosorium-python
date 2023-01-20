from typing import List


# O(n * m) time || O(m) space, n is len(nums), s is subset_sum
def can_partition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    subset_sum = total_sum // 2

    dp = [False] * (subset_sum + 1)
    dp[0] = True
    for n in nums:
        for i in range(subset_sum, n - 1, -1):
            dp[i] = dp[i] or dp[i - n]

    return dp[subset_sum]
