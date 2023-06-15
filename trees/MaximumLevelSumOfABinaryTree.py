import collections
from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(n) space
def max_level_sum(self, root: Optional[TreeNode]) -> int:
    max_so_far, level, res = -float('inf'), 0, 0
    dq = collections.deque()
    dq.append(root)
    while dq:
        level, level_sum = level + 1, 0
        for _ in range(len(dq)):
            node = dq.popleft()
            level_sum += node.val

            if node.left:
                dq.append(node.left)

            if node.right:
                dq.append(node.right)

        if max_so_far < level_sum:
            max_so_far, res = level_sum, level

    return res
