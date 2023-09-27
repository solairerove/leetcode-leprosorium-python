from functools import lru_cache
from typing import Optional

from trees.TreeNode import TreeNode


# O(n * log(n)) time || O(n) space
def is_balanced(self, root: Optional[TreeNode]) -> bool:
    @lru_cache(None)
    def height(node):
        if not node:
            return -1

        return 1 + max(height(node.left), height(node.right))

    @lru_cache(None)
    def balanced(node):
        if not node:
            return True

        height_of_children = abs(height(node.left) - height(node.right)) < 2
        subtrees_balanced = balanced(node.left) and balanced(node.right)

        return height_of_children and subtrees_balanced

    return balanced(root)
