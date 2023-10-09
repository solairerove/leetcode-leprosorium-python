from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def diameter_of_binary_tree_recursive_dfs(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        if not node:
            return 0

        nonlocal res
        left, right = dfs(node.left), dfs(node.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)

    return res


# O(n) time || O(max(n, log(n)) space
def diameter_of_binary_tree_dfs(self, root: Optional[TreeNode]) -> int:
    res, dic, stack = 0, {}, [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                left_path = dic.pop(node.left) if node.left else 0
                right_path = dic.pop(node.right) if node.right else 0
                res = max(res, left_path + right_path)
                dic[node] = max(left_path, right_path) + 1
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

    return res
