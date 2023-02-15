from functools import lru_cache
from typing import List


# O(n * k) time || O(n * k) space
def max_profit_top_down(self, k: int, prices: List[int]) -> int:
    @lru_cache(None)
    def dp(i: int, transactions_remaining: int, holding: int):
        if transactions_remaining == 0 or i == len(prices):
            return 0

        do_nothing = dp(i + 1, transactions_remaining, holding)

        if holding:
            do_something = prices[i] + dp(i + 1, transactions_remaining - 1, 0)
        else:
            do_something = -prices[i] + dp(i + 1, transactions_remaining, 1)

        return max(do_nothing, do_something)

    return dp(0, k, 0)


# O(n * k) time || O(n * k) space
def max_profit_bottom_up(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for transactions_remaining in range(1, k + 1):
            for holding in range(2):
                do_nothing = dp[i + 1][transactions_remaining][holding]
                if holding:
                    do_something = prices[i] + dp[i + 1][transactions_remaining - 1][0]
                else:
                    do_something = -prices[i] + dp[i + 1][transactions_remaining][1]

                dp[i][transactions_remaining][holding] = max(do_nothing, do_something)

    return dp[0][k][0]
