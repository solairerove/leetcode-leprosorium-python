from typing import Optional

from trees.TreeNode import TreeNode


# O(n * log(n)) time || O(n) space
def is_balanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node) -> (bool, int):
        if not node:
            return True, -1

        left_balanced, l_height = dfs(node.left)
        if not left_balanced:
            return False, 0

        right_balanced, r_height = dfs(node.right)
        if not right_balanced:
            return False, 0

        return (abs(l_height - r_height) < 2), 1 + max(l_height, r_height)

    return dfs(root)[0]
