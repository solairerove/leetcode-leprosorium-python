import collections
from typing import Optional

from trees.TreeNode import TreeNode


# need to understand how to traverse trees

# O(n) time || O(n) space
def min_depth_iterative_bfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    dq = collections.deque([(root, 1)])
    while dq:
        node, level = dq.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                dq.append((node.left, level + 1))
                dq.append((node.right, level + 1))


# O(n) time || O(max(n, log(n)) space
def min_depth_recursive_dfs(self, root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0

        left, right = dfs(node.left), dfs(node.right)
        if not left:
            return right + 1
        elif not right:
            return left + 1

        return 1 + min(left, right)

    return dfs(root)
