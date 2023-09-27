from typing import Optional

from trees.TreeNode import TreeNode


# O(h) time || O(h) space
def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root:
        return None

    if root == p or root == q:
        return root

    left, right = lowest_common_ancestor(self, root.left, p, q), lowest_common_ancestor(self, root.right, p, q)

    if not left:
        return right

    if not right:
        return left

    return root
