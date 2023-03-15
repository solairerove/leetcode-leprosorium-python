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
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)

    return root
