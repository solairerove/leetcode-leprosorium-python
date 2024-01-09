from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs(node: TreeNode):
        if not node:
            return []

        if not node.left and not node.right:
            return [node.val]

        return dfs(node.left) + dfs(node.right)

    return dfs(root1) == dfs(root2)
