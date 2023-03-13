from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def is_symmetric_rec(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    else:
        return is_mirror(self, root.left, root.right)


def is_mirror(self, left, right):
    if not left and not right:
        return True

    if not left or not right:
        return False

    if left.val == right.val:
        return is_mirror(self, left.left, right.right) and is_mirror(self, left.right, right.left)
    else:
        return False
