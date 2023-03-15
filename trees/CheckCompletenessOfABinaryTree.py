from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def is_complete_tree(self, root: Optional[TreeNode]) -> bool:
    def count_nodes(node):
        if not node:
            return 0

        return 1 + count_nodes(node.left) + count_nodes(node.right)

    def dfs(node, i, n):
        if not node:
            return True

        if i >= n:
            return False

        return dfs(node.left, 2 * i + 1, n) and dfs(node.right, 2 * i + 2, n)

    return dfs(root, 0, count_nodes(root))
