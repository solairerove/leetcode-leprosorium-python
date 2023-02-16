from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(log(n)) space
def max_depth(self, root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res


# O(n) time || O(max(n, log(n))) space
def max_depth_rec(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return max(max_depth_rec(self, root.left), max_depth_rec(self, root.right)) + 1
