from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(self, root: Optional[TreeNode]) -> int:
    def helper(node: TreeNode):
        if not node:
            return 0, 0

        left, right = helper(node.left), helper(node.right)
        now = node.val + left[1] + right[1]
        later = max(left) + max(right)

        return now, later

    return max(helper(root))
