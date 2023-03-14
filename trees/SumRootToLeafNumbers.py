from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def sum_numbers(self, root: Optional[TreeNode]) -> int:
    root_to_leaf = 0
    stack = [(root, 0)]
    while stack:
        node, curr_num = stack.pop()
        if node:
            curr_num = curr_num * 10 + node.val
            if not node.left and not node.right:
                root_to_leaf += curr_num
            else:
                stack.append((node.right, curr_num))
                stack.append((node.left, curr_num))

    return root_to_leaf
