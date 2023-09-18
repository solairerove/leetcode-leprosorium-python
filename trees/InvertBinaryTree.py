from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invert_tree(self, root.right), invert_tree(self, root.left)
        return root


# O(n) time || O(h) space
def invert_tree_stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    stack = [root]
    while stack:
        curr = stack.pop()
        curr.left, curr.right = curr.right, curr.left

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    return root
