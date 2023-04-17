from functools import cache
from typing import List


# O(n) time || O(n) space
def max_profit(self, prices: List[int]) -> int:
    @cache
    def dp(i, buy):
        if i >= len(prices):
            return 0

        cooldown = dp(i + 1, buy)
        return max(dp(i + 1, not buy) - prices[i], cooldown) if buy else max(dp(i + 2, not buy) + prices[i], cooldown)

    return dp(0, True)
