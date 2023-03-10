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


# O(n) time || O(max(n, log(n)) space
def diameter_of_binary_tree_dfs(self, root: Optional[TreeNode]) -> int:
    res, dic, stack = 0, {}, [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                left_path = 0 if node.left is None else dic.pop(node.left)
                right_path = 0 if node.right is None else dic.pop(node.right)
                res = max(res, left_path + right_path)
                dic[node] = max(left_path, right_path) + 1
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

    return res
