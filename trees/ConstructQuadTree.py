from typing import List


class QuadNode:
    def __init__(self, val, is_leaf, top_left, top_right, bottom_left, bottom_right):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


# O(n * log(n)) time || O(n) space
def construct(self, grid: List[List[int]]) -> QuadNode:
    root = QuadNode(True, True, None, None, None, None)

    if len(set([item for row in grid for item in row])) == 1:
        root.val = bool(grid[0][0])

        return root

    root.is_leaf = False
    n = len(grid)

    root.top_left = construct(self, [row[:n // 2] for row in grid[:n // 2]])
    root.top_right = construct(self, [row[n // 2:] for row in grid[:n // 2]])
    root.bottom_left = construct(self, [row[:n // 2] for row in grid[n // 2:]])
    root.bottom_right = construct(self, [row[n // 2:] for row in grid[n // 2:]])

    return root
