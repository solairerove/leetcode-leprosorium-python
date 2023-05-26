from functools import lru_cache
from typing import List


# O(n^2) time || O(n^2) space
def stone_game_ii(self, piles: List[int]) -> int:
    n = len(piles)
    for i in range(n - 2, -1, -1):
        piles[i] += piles[i + 1]

    @lru_cache(None)
    def dp(i, m):
        if i + 2 * m >= n:
            return piles[i]

        return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

    return dp(0, 1)
