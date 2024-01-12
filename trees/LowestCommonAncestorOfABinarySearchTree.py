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


# O(h) time || O(h) space
def lowest_common_ancestor_dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return None

        if node.val < p.val and node.val < q.val:
            return dfs(node.right)

        if node.val > p.val and node.val > q.val:
            return dfs(node.left)

        return node

    return dfs(root)
