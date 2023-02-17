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


# O(n) time || O(h) space
def min_diff_in_bst_iterative(self, root: Optional[TreeNode]) -> int:
    prev, res = -float('inf'), float('inf')
    stack = [root]
    curr = root.left
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res = min(res, curr.val - prev)
        prev = curr.val
        curr = curr.right

    return res
