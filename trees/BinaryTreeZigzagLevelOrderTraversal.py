from collections import deque
from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    res, direction = [], 1
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(level[::direction])
        direction *= -1

    return res
