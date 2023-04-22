from functools import lru_cache
from typing import List


# O(n^2) time || O(n) space
def minimum_total(self, triangle: List[List[int]]) -> int:
    @lru_cache(None)
    def dp(i, j):
        path = triangle[i][j]
        if i < len(triangle) - 1:
            path += min(dp(i + 1, j), dp(i + 1, j + 1))

        return path

    return dp(0, 0)
