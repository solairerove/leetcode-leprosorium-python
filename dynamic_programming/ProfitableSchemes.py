from functools import lru_cache
from typing import List


# O(n * m * k) time || O(n * m * k) space
def profitable_schemes_top_down(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
    @lru_cache(None)
    def dp(i, p, n):
        if i == len(group):
            if p >= min_profit:
                return 1
            return 0

        pick = 0
        if n - group[i] >= 0:
            pick = dp(i + 1, min(min_profit, p + profit[i]), n - group[i])

        skip = dp(i + 1, p, n)

        return skip + pick

    return dp(0, 0, n) % (10 ** 9 + 7)
