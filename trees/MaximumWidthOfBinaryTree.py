import collections
from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(w) space, w - biggest number of nodes
def width_of_binary_tree_bfs(self, root: Optional[TreeNode]) -> int:
    prev_level, prev_num, max_width = 1, 1, 0
    dq = collections.deque([(prev_level, prev_num, root)])
    while dq:
        num, level, node = dq.popleft()
        if level > prev_level:
            prev_level, prev_num = level, num

        max_width = max(max_width, num - prev_num + 1)

        if node.left:
            dq.append((num * 2, level + 1, node.left))

        if node.right:
            dq.append((num * 2 + 1, level + 1, node.right))

    return max_width
