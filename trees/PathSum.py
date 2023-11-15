from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def has_path_sum_rec(self, root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    def dfs(node, curr_sum):
        if not node:
            return False

        curr_sum += node.val

        if not node.left and not node.right:
            return curr_sum == target_sum

        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)


# O(n) time || O(max(n, log(n)) space
def has_path_sum_dfs(self, root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    stack = [(root, target_sum - root.val)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True

        if node.right:
            stack.append((node.right, curr_sum - node.right.val))

        if node.left:
            stack.append((node.left, curr_sum - node.left.val))

    return False
