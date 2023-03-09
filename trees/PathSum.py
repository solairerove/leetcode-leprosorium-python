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
