from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def inorder(node: TreeNode):
        if node:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

    inorder(root)

    return res


# O(n) time || O(n) space
def inorder_traversal_stack(self, root: Optional[TreeNode]) -> List[int]:
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
