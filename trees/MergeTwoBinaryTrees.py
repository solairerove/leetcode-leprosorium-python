from typing import Optional

from trees.TreeNode import TreeNode


# O(min(n, n)) time || O(min(n, m)) space
def merge_trees_rec(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2

    if not root2:
        return root1

    root1.val += root2.val
    root1.left = merge_trees_rec(self, root1.left, root2.left)
    root1.right = merge_trees_rec(self, root1.right, root2.right)

    return root1
