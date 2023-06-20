from functools import lru_cache
from typing import List


# O(m * n) time || O(m * n) space
def count_paths(self, grid: List[List[int]]) -> int:
    m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7

    @lru_cache(None)
    def dfs(i, j):
        res = 1
        for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:  # >
                res += dfs(x, y) % mod

        return res

    return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
