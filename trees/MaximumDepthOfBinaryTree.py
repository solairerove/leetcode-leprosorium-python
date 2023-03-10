from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(log(n)) space
def max_depth_dfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        stack = [[1, root]]
        res = 0

    while stack:
        depth, node = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([depth + 1, node.left])
            stack.append([depth + 1, node.right])

    return res


# O(n) time || O(max(n, log(n))) space
def max_depth_rec(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return max(max_depth_rec(self, root.left), max_depth_rec(self, root.right)) + 1
