from typing import Optional

from trees.TreeNode import TreeNode


# O(h) time || O(h) space
def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return None

        if node == p or node == q:
            return node

        left, right = dfs(node.left), dfs(node.right)

        if not left:
            return right

        if not right:
            return left

        return node

    return dfs(root)
