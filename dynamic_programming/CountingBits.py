from typing import List


# O(n) time || O(1) space
def count_bits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + i % 2

    return dp[:n + 1]
