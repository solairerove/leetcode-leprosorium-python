from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p and q:
        return p.val == q.val and is_same_tree(self, p.left, q.left) and is_same_tree(self, p.right, q.right)

    return p is q
