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


# O(n * m) time || O(m) space
def closed_island_bfs(self, grid: List[List[int]]) -> int:
    visit = set()

    def bfs(i, j):
        visit.add((i, j))
        q, res = [(i, j)], 1
        for i, j in q:
            for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    res = 0
                elif not grid[r][c] and (r, c) not in visit:
                    visit.add((r, c))
                    q.append((r, c))

        return res

    return sum(
        bfs(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if not cell and (i, j) not in visit
    )
