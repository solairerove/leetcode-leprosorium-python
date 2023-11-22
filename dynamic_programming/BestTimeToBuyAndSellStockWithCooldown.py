from functools import lru_cache
from typing import List


# O(n) time || O(n) space
def max_profit_top_down(self, prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i, holding):
        if i >= len(prices):
            return 0

        if holding:
            res = max(prices[i] + dp(i + 2, False), dp(i + 1, True))
        else:
            res = max(-prices[i] + dp(i + 1, 1), dp(i + 1, 0))

        return res

    return dp(0, False)
