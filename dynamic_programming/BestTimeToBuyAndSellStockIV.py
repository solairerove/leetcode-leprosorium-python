from functools import lru_cache
from typing import List


# O(n) time || O(n) space
def max_profit(self, k: int, prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i: int, transactions_remaining: int, holding: int):
        if transactions_remaining == 0 or i == len(prices):
            return 0

        do_nothing = dp(i + 1, transactions_remaining, holding)
        do_something = 0

        if holding:
            do_something = prices[i] + dp(i + 1, transactions_remaining - 1, 0)
        else:
            do_something = -prices[i] + dp(i + 1, transactions_remaining, 1)

        return max(do_nothing, do_something)

    return dp(0, k, 0)
