from functools import lru_cache
from typing import List


# O(k * s) time || O(n * k) space
# s - total number of all coins
def max_value_of_coins(self, piles: List[List[int]], k: int) -> int:
    @lru_cache(None)
    def dp(i, k):
        if k == 0 or i == len(piles):
            return 0

        res, curr = dp(i + 1, k), 0
        for j in range(min(len(piles[i]), k)):
            curr += piles[i][j]
            res = max(res, curr + dp(i + 1, k - j - 1))

        return res

    return dp(0, k)
