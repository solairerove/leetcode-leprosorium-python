from typing import List


# O(n * m) time || O(n * m) space
def num_enclaves(self, grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return -1

        if grid[i][j] == 0 or visit[i][j]:
            return 0

        visit[i][j] = True
        up = dfs(i - 1, j)
        right = dfs(i, j + 1)
        down = dfs(i + 1, j)
        left = dfs(i, j - 1)

        if up == -1 or right == -1 or down == -1 or left == -1:
            return -1
        else:
            return 1 + up + right + down + left

    res = 0
    visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visit[i][j]:
                island_size = dfs(i, j)
                if island_size != -1:
                    res += island_size

    return res
