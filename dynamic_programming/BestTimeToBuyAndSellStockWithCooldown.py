from functools import lru_cache
from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    buy, sell, cooldown = -prices[0], 0, 0
    for price in prices[1:]:
        _buy = max(buy, cooldown - price)
        _sell = buy + price
        _cooldown = max(cooldown, sell)

        buy, sell, cooldown = _buy, _sell, _cooldown

    return max(sell, cooldown)


# O(n) time || O(n) space
def max_profit_top_down(self, prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i, holding):
        if i >= len(prices):
            return 0

        if holding:
            res = max(prices[i] + dp(i + 2, False), dp(i + 1, True))
        else:
            res = max(-prices[i] + dp(i + 1, True), dp(i + 1, False))

        return res

    return dp(0, False)
