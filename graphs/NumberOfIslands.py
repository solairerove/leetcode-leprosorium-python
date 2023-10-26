import collections
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

    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)

    return res


# O(n * m) time || O(n * m) space
def num_islands_dfs_shorter(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])

    def dfs(i, j):
        if 0 <= i < n and 0 <= j < m and grid[i][j] == "1":
            grid[i][j] = "0"
            list(map(dfs, [i - 1, i + 1, i, i], [j, j, j - 1, j + 1]))

    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                res += 1
                dfs(i, j)

    return res


# O(n * m) time || O(min(n, m)) space
def num_islands_bfs(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    res = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        dq = collections.deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dq.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                res += 1
                bfs(i, j)

    return res
