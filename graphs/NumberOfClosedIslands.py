from typing import List


# O(n * m) time || O(n * m) space
def closed_island_dfs(self, grid: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if grid[i][j]:
            return 1

        grid[i][j] = 2

        return dfs(i, j + 1) * dfs(i, j - 1) * dfs(i + 1, j) * dfs(i - 1, j)

    return sum(dfs(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if not cell)
