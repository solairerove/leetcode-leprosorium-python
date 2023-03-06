from typing import List


# O(n * m) time || O(n * m) space
def num_islands_dfs(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                cnt += 1

    return cnt


# O(n * m) time || O(n * m) space
def num_islands_smart(self, grid: List[List[str]]) -> int:
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))

            return 1

        return 0

    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
