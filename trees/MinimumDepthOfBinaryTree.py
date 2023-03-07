from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space, where h can be n or lon(n)
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
