from typing import List


# TODO: create topic dfs/bfs?

# O(n * m) time || O(n * m) space
def num_islands_dfs(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        else:
            return

    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)

    return res
