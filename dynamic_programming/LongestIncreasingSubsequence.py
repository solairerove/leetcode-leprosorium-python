from bisect import bisect_left
from typing import List


# O(n^2) time || O(n) space
def length_of_lis(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)


# O(n * log(n)) time || O(n) space
def length_of_lis_bs(self, nums: List[int]) -> int:
    sub = []
    for n in nums:
        i = bisect_left(sub, n)
        if i == len(sub):
            sub.append(n)
        else:
            sub[i] = n

    return len(sub)
