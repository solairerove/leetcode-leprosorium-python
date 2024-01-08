from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
# n - number of all nodes
# h - height of tree
def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0

    if root.val < low:
        return range_sum_bst(self, root.right, low, high)
    elif root.val > high:
        return range_sum_bst(self, root.left, low, high)

    return root.val + range_sum_bst(self, root.left, low, high) + range_sum_bst(self, root.right, low, high)
