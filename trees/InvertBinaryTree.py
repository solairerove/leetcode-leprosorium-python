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
        return root

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return root
