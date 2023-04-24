from functools import lru_cache
from typing import List


# O(m * n) time || O(m * n) space
def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])

    @lru_cache(None)
    def dp(i, j):
        if i >= m or j >= n:
            return 0

        if obstacle_grid[i][j] == 1:
            return 0

        if i == m - 1 and j == n - 1:
            return 1

        return dp(i, j + 1) + dp(i + 1, j)

    return dp(0, 0)
