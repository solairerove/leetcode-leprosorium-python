from typing import List


# O(a * c) time || O(a * c) space
def change(self, amount: int, coins: List[int]) -> int:
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    for c in range(1, len(coins) + 1):
        dp[c][0] = 1
        for a in range(1, amount + 1):
            dp[c][a] = dp[c - 1][a]
            if coins[c - 1] <= a:
                dp[c][a] += dp[c][a - coins[c - 1]]

    return dp[len(coins)][amount]
