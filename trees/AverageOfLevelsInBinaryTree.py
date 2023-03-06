import collections
from typing import Optional, List

from trees.TreeNode import TreeNode


# O(n) time || O(m) space, m - max number of nodes on any level
def average_of_levels(self, root: Optional[TreeNode]) -> List[float]:
    dq = collections.deque([root])
    res = []
    while dq:
        level_len = cnt = len(dq)
        level_sum = 0
        while cnt:
            node = dq.popleft()
            level_sum += node.val

            if node.left:
                dq.append(node.left)

            if node.right:
                dq.append(node.right)

            cnt -= 1

        res.append(level_sum / level_len)

    return res
