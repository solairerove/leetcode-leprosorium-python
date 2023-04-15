from typing import List


# O(k * s) time || O(n * k) space
# s - total number of all coins
def max_value_of_coins(self, piles: List[List[int]], k: int) -> int:
    n = len(piles)
    dp = [[-1] * (k + 1) for _ in range(n + 1)]

    def helper(i, coins):
        if i == 0:
            return 0

        if dp[i][coins] != -1:
            return dp[i][coins]

        curr_sum = 0
        for curr_coins in range(0, min(len(piles[i - 1]), coins) + 1):
            if curr_coins > 0:
                curr_sum += piles[i - 1][curr_coins - 1]
            dp[i][coins] = max(
                dp[i][coins],
                helper(i - 1, coins - curr_coins) + curr_sum
            )

        return dp[i][coins]

    return helper(n, k)
