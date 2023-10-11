import collections
from typing import Optional

from trees.TreeNode import TreeNode


# need to understand how to traverse trees

# O(n) time || O(n) space
def min_depth_iterative_bfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        dq = collections.deque([(1, root)])

    while dq:
        depth, node = dq.popleft()
        nodes = [node.left, node.right]
        if not any(nodes):
            return depth

        for node in nodes:
            if node:
                dq.append((depth + 1, node))


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


# O(n) time || O(n) space
def min_depth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        stack, min_depth = [(1, root), ], float('inf')

    while stack:
        depth, root = stack.pop()
        nodes = [root.left, root.right]
        if not any(nodes):
            min_depth = min(depth, min_depth)

        for node in nodes:
            if node:
                stack.append((depth + 1, node))

    return min_depth
