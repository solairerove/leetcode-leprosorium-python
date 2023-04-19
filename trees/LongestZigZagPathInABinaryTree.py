from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def longest_zig_zag(self, root: Optional[TreeNode]) -> int:
    self.res = 0

    def dfs(node, go_left, steps):
        if node:
            self.res = max(self.res, steps)
            if go_left:
                dfs(node.left, False, steps + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, steps + 1)

    dfs(root, False, 0)
    dfs(root, True, 0)

    return self.res
