from collections import deque
from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(max(n, log(n)) space
def min_depth_recursive(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    children = [root.left, root.right]
    if not any(children):
        return 1

    min_depth = float('inf')
    for child in children:
        if child:
            min_depth = min(min_depth_recursive(self, child), min_depth)

    return min_depth + 1


# O(n) time || O(n) space
def min_depth_dfs(self, root: Optional[TreeNode]) -> int:
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


# O(n) time || O(n) space
def min_depth_bfs(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        dq = deque([(1, root)])

    while dq:
        depth, root = dq.popleft()
        nodes = [root.left, root.right]
        if not any(nodes):
            return depth

        for node in nodes:
            if node:
                dq.append((depth + 1, node))
