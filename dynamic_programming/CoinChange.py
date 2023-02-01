from functools import lru_cache
from typing import List


# O(c * a) time || O(a) space
def coin_change(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return [dp[amount], -1][dp[amount] == amount + 1]


# O(c * a) time || O(a) space
def coin_change_rec(self, coins: List[int], amount: int) -> int:
    @lru_cache(None)
    def dfs(a):
        if a < 0:
            return -1

        if a == 0:
            return 0

        min_cost = float(a + 1)
        for c in coins:
            res = dfs(a - c)
            if res != -1:
                min_cost = min(min_cost, res + 1)

        return [min_cost, -1][min_cost == float(a + 1)]

    return dfs(amount)
