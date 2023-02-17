from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def inorder(node: TreeNode):
        if node:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

    inorder(root)

    return res
