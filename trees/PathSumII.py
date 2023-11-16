from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def path_sum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
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
