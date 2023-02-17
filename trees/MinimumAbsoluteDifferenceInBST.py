from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
    stack = []

    def dfs(node):
        if node.left:
            dfs(node.left)

        stack.append(node.val)

        if node.right:
            dfs(node.right)

    dfs(root)

    return min(b - a for a, b in zip(stack, stack[1:]))
