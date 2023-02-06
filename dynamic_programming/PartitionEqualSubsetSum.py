from functools import lru_cache
from typing import List, Tuple


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


# O(n * m) time || O(n * m) space, n is len(nums), s is subset_sum
def can_partition_rec(self, nums: List[int]) -> bool:
    @lru_cache(None)
    def dfs(arr: Tuple[int], n: int, subset_sum: int) -> bool:
        if subset_sum == 0:
            return True

        if n == 0 or subset_sum < 0:
            return False

        return (
                dfs(arr, n - 1, subset_sum - nums[n - 1])
                or
                dfs(arr, n - 1, subset_sum)
        )

    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    return dfs(tuple(nums), len(nums) - 1, total_sum // 2)
