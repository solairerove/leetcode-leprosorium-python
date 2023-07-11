import collections
from typing import List

from trees.TreeNode import TreeNode


def distance_k(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    g = collections.defaultdict(list)
    vis, q, res = set(), collections.deque(), []
    convert_into_graph(root, None, g)

    q.append((target, 0))

    while q:
        n, d = q.popleft()
        vis.add(n)

        if d == k:
            res.append(n.val)

        for nei in g[n]:
            if nei not in vis:
                q.append((nei, d + 1))

    return res


def convert_into_graph(node, parent, g):
    if not node:
        return

    if parent:
        g[node].append(parent)

    if node.right:
        g[node].append(node.right)
        convert_into_graph(node.right, node, g)

    if node.left:
        g[node].append(node.left)
        convert_into_graph(node.left, node, g)
