from typing import Optional

from trees.TreeNode import TreeNode


# O(m * n) time || O(m + n) space
def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return False
        elif is_identical(node, sub_root):
            return True

        return dfs(node.left) or dfs(node.right)

    def is_identical(node1, node2):
        if not node1 or not node2:
            return not node1 and not node2

        return (node1.val == node2.val and
                is_identical(node1.left, node2.left) and
                is_identical(node1.right, node2.right))

    return dfs(root)
