from typing import List


# O(n) time || O(1) space
def coin_change(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
