from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invert_tree(self, root.right), invert_tree(self, root.left)
        return root
