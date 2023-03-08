import collections
from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p and q:
        return p.val == q.val and is_same_tree(self, p.left, q.left) and is_same_tree(self, p.right, q.right)

    return p is q


# O(n) time || O(h) space
def is_same_tree_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

    return True


# O(n) time || O(h) space
def is_same_tree_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    dq = collections.deque([(p, q)])
    while dq:
        node1, node2 = dq.popleft()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            dq.append((node1.left, node2.left))
            dq.append((node1.right, node2.right))

    return True
