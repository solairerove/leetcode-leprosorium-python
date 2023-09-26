from typing import Optional

from trees.TreeNode import TreeNode


# O(h) time || O(1) space
def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    mn, mx = min(p.val, q.val), max(p.val, q.val)
    while root:
        if root.val > mx:
            root = root.left
        elif root.val < mn:
            root = root.right
        else:
            return root

    return None
