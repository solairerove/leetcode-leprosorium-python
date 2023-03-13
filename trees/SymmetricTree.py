from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def is_symmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    stack = [(root.left, root.right)]
    while stack:
        left, right = stack.pop()

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False

    return True


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
