import collections
from typing import List


# O(n^2) time || O(n^2) space
def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
    n = len(grid)

    if grid[0][0] or grid[n - 1][n - 1]:
        return -1

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
    visit = set()
    dq = collections.deque([(0, 0, 1)])
    visit.add((0, 0))
    while dq:
        i, j, dist = dq.popleft()

        if i == n - 1 and j == n - 1:
            return dist

        for d1, d2 in dirs:
            x, y = i + d1, j + d2

            if 0 <= x < n and 0 <= y < n:
                if (x, y) not in visit and grid[x][y] == 0:
                    visit.add((x, y))
                    dq.append((x, y, dist + 1))

    return -1
