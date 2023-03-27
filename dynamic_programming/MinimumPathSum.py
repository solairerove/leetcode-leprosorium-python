from functools import lru_cache
from typing import List


# O(n * m) time || O(n * m) space
# dp(i, j) = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
def min_path_sum_rec(self, grid: List[List[int]]) -> int:
    @lru_cache
    def dp(i, j):
        if i == len(grid) or j == len(grid[0]):
            return float('inf')

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)
