import math
from functools import lru_cache
from typing import List


# O(n^2) time || O(n^2) space
def min_falling_path_sum_top_down(self, matrix: List[List[int]]) -> int:
    n = len(matrix)

    @lru_cache(None)
    def dp(i, j):
        if i == n or j == n or j < 0:
            return math.inf

        if i == n - 1:
            return matrix[i][j]

        return matrix[i][j] + min(
            dp(i + 1, j - 1),
            dp(i + 1, j),
            dp(i + 1, j + 1)
        )

    return min(dp(0, j) for j in range(n))
