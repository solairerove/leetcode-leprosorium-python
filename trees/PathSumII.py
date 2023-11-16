from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def path_sum_rec(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    if not root:
        return []

    res = []

    def dfs(node, curr_sum, curr_path):
        if not node:
            return

        curr_sum += node.val
        curr_path.append(node.val)

        if not node.left and not node.right and curr_sum == target_sum:
            res.append(list(curr_path))

        dfs(node.left, curr_sum, curr_path)
        dfs(node.right, curr_sum, curr_path)

        curr_path.pop()

    dfs(root, 0, [])

    return res


# O(n) time || O(max(n, log(n)) space
def path_sum_dfs(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    if not root:
        return []

    res = []
    stack = [(root, root.val, [root.val])]
    while stack:
        node, curr_sum, curr_path = stack.pop()

        if not node.left and not node.right and curr_sum == target_sum:
            res.append(curr_path)

        if node.left:
            stack.append((node.left, curr_sum + node.left.val, curr_path + [node.left.val]))

        if node.right:
            stack.append((node.right, curr_sum + node.right.val, curr_path + [node.right.val]))

    return res
