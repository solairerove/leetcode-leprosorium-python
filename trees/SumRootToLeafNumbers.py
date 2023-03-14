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


# O(n) time || O(h) space
def sum_numbers_rec(self, root: Optional[TreeNode]) -> int:
    def preorder(node, curr_num):
        nonlocal root_to_leaf
        if node:
            curr_num = curr_num * 10 + node.val

            if not (node.left or node.right):
                root_to_leaf += curr_num

            preorder(node.left, curr_num)
            preorder(node.right, curr_num)

    root_to_leaf = 0
    preorder(root, 0)

    return root_to_leaf


# O(n) time || O(1) space
def sum_numbers_morris(self, root: Optional[TreeNode]) -> int:
    root_to_leaf = curr_num = 0
    while root:
        if root.left:
            predecessor = root.left
            steps = 1
            while predecessor.right and predecessor.right is not root:
                predecessor = predecessor.right
                steps += 1

            if not predecessor.right:
                curr_num = curr_num * 10 + root.val

                predecessor.right, root = root, root.left
            else:
                if not predecessor.left:
                    root_to_leaf += curr_num

                for _ in range(steps):
                    curr_num //= 10

                predecessor.right, root = None, root.right
        else:
            curr_num = curr_num * 10 + root.val

            if not root.right:
                root_to_leaf += curr_num

            root = root.right

    return root_to_leaf
