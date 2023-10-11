from functools import lru_cache
from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n))) space
def max_depth_recursive_dfs(self, root: Optional[TreeNode]) -> int:
    @lru_cache(None)
    def dfs(node):
        if not node:
            return 0

        return 1 + max(dfs(node.left), dfs(node.right))

    return dfs(root)


# O(n) time || O(log(n)) space
def max_depth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    res, stack = 0, [[1, root]]
    while stack:
        depth, node = stack.pop()
        if node:
            stack.append([depth + 1, node.left])
            stack.append([depth + 1, node.right])
            res = max(res, depth)

    return res
