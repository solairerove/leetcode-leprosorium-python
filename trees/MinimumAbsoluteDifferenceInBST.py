from typing import Optional

from trees.TreeNode import TreeNode


# O(n) time || O(h) space
def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
    stack = []

    def dfs(node):
        if node.left:
            dfs(node.left)

        stack.append(node.val)

        if node.right:
            dfs(node.right)

    dfs(root)

    return min(b - a for a, b in zip(stack, stack[1:]))


# O(n) time || O(h) space
def get_minimum_difference_rec(self, root: Optional[TreeNode]) -> int:
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []

    nums = inorder(root)

    return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))
