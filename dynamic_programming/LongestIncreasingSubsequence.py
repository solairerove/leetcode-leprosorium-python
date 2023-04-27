from bisect import bisect_left
from typing import List


# O(n^2) time || O(n) space
def length_of_lis_bottom_up(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# O(n * log(n)) time || O(n) space
def length_of_lis(self, nums: List[int]) -> int:
    sub = []
    for n in nums:
        i = bisect_left(sub, n)
        if i == len(sub):
            sub.append(n)
        else:
            sub[i] = n

    return len(sub)
