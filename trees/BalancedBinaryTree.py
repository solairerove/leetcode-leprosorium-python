from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def is_balanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0, True

        l_height, l_balanced = dfs(node.left)
        r_height, r_balanced = dfs(node.right)

        return max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <= 1

    return dfs(root)[1]
