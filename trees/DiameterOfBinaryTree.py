from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def diameter_of_binary_tree_recursive_dfs(self, root: Optional[TreeNode]) -> int:
    diameter = 0

    def longest_path(node):
        if not node:
            return 0

        nonlocal diameter
        left_path, right_path = longest_path(node.left), longest_path(node.right)
        diameter = max(diameter, left_path + right_path)

        return max(left_path, right_path) + 1

    longest_path(root)

    return diameter
