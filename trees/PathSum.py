from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def has_path_sum_recursive(self, root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    target_sum -= root.val
    if not root.left and not root.right:
        return target_sum == 0

    return has_path_sum_recursive(self, root.left, target_sum) or has_path_sum_recursive(self, root.right, target_sum)


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
