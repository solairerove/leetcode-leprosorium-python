from typing import List


# O(n^2) time || O(n^2) space
def shortest_bridge(self, grid: List[List[int]]) -> int:
    n = len(grid)
    first_x, first_y = -1, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                first_x, first_y = i, j
                break

    def dfs(x, y):
        grid[x][y] = 2
        bfs_queue.append((x, y))
        for curr_x, curr_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= curr_x < n and 0 <= curr_y < n and grid[curr_x][curr_y] == 1:
                dfs(curr_x, curr_y)

    bfs_queue = []
    dfs(first_x, first_y)

    distance = 0
    while bfs_queue:
        new_bfs = []
        for x, y in bfs_queue:
            for curr_x, curr_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= curr_x < n and 0 <= curr_y < n:
                    if grid[curr_x][curr_y] == 1:
                        return distance
                    elif grid[curr_x][curr_y] == 0:
                        new_bfs.append((curr_x, curr_y))
                        grid[curr_x][curr_y] = -1

        bfs_queue = new_bfs
        distance += 1
