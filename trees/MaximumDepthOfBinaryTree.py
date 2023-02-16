from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n))) space
def max_depth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return max(max_depth(self, root.left), max_depth(self, root.right)) + 1
