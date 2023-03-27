from functools import lru_cache
from typing import List


# O(n * m) time || O(n * m) space
# dp(i, j) = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
def min_path_sum_rec(self, grid: List[List[int]]) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i == len(grid) or j == len(grid[0]):
            return float('inf')

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

    return dp(0, 0)


# O(n * m) time || O(n * m) space
def min_path_sum_bottom_up(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    dp = [[0] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j != n - 1:
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == n - 1 and i != m - 1:
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            elif i != m - 1 and j != n - 1:
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i][j] = grid[i][j]

    return dp[0][0]


# O(n * m) time || O(n) space
def min_path_sum_1d_bottom_up(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    dp = [0] * n
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j != n - 1:
                dp[j] = grid[i][j] + dp[j + 1]
            elif j == n - 1 and i != m - 1:
                dp[j] = grid[i][j] + dp[j]
            elif i != m - 1 and j != n - 1:
                dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
            else:
                dp[j] = grid[i][j]

    return dp[0]


# O(n * m) time || O(1) space
def min_path_sum_bottom_up_constant_space(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j != n - 1:
                grid[i][j] = grid[i][j] + grid[i][j + 1]
            elif j == n - 1 and i != m - 1:
                grid[i][j] = grid[i][j] + grid[i + 1][j]
            elif i != m - 1 and j != n - 1:
                grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])

    return grid[0][0]


# O(n * m) time || O(1) space
def min_path_sum_bottom_up_constant_space_readable(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]

    for j in range(1, n):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[m - 1][n - 1]
