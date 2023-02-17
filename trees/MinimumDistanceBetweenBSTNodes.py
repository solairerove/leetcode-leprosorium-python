from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def min_diff_in_bst(self, root: Optional[TreeNode]) -> int:
    def inorder(node, pre, res):
        if not node:
            return

        inorder(node.left, pre, res)
        pre[0], res[0] = node.val, min(res[0], node.val - pre[0])
        inorder(node.right, pre, res)

    prev, result = [-float('inf')], [float('inf')]
    inorder(root, prev, result)

    return int(result[0])
