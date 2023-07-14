from typing import List


# O(n) time || O(n) space
def longest_subsequence(self, arr: List[int], difference: int) -> int:
    dp = {}
    for num in arr:
        dp[num] = dp.get(num - difference, 0) + 1

    return max(dp.values())
