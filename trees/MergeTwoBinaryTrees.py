from typing import Optional

from trees.TreeNode import TreeNode


# O(min(n, n)) time || O(min(n, m)) space
def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1 or not root2:
        return root1 or root2

    stack = [(root1, root2)]
    while stack:
        node1, node2 = stack.pop()
        if not node2:
            continue

        node1.val += node2.val

        if not node1.left and node2.left:
            node1.left = TreeNode(0)

        if not node1.right and node2.right:
            node1.right = TreeNode(0)

        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))

    return root1


# O(min(n, n)) time || O(min(n, m)) space
def merge_trees_rec(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2

    if not root2:
        return root1

    root1.val += root2.val
    root1.left = merge_trees_rec(self, root1.left, root2.left)
    root1.right = merge_trees_rec(self, root1.right, root2.right)

    return root1
