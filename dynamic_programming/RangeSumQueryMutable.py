from typing import List


class TreeNode:
    def __init__(self, low, high):
        self.low, self.high = low, high
        self.left, self.right = None, None
        self.sum = 0


# Binary Indexed Tree
class FenwickTree:
    def __init__(self, arr):
        self.root = self.build_tree(arr, 0, len(arr) - 1)

    def build_tree(self, arr, low, high):
        if low > high:
            return None

        root = TreeNode(low, high)
        if low == high:
            root.sum = arr[low]
            return root

        mid = low + (high - low) // 2
        root.left = self.build_tree(arr, low, mid)
        root.right = self.build_tree(arr, mid + 1, high)
        root.sum = root.left.sum + root.right.sum

        return root

    def update(self, idx, val, node=None):
        if not node:
            node = self.root

        if node.low == node.high:
            node.sum = val
            return

        mid = node.low + (node.high - node.low) // 2
        if idx <= mid:
            self.update(idx, val, node.left)
        else:
            self.update(idx, val, node.right)

        node.sum = node.left.sum + node.right.sum

    def sum_range(self, low, high, node=None):
        if not node:
            node = self.root

        if node.low == low and node.high == high:
            return node.sum

        mid = node.low + (node.high - node.low) // 2
        if high <= mid:
            return self.sum_range(low, high, node.left)

        if low >= mid + 1:
            return self.sum_range(low, high, node.right)

        return self.sum_range(low, mid, node.left) + self.sum_range(mid + 1, high, node.right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = FenwickTree(nums)

    # O(log(n)) time || O(log(n)) space
    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    # O(log(n)) time || O(log(n)) space
    def sum_range(self, left: int, right: int) -> int:
        return self.tree.sum_range(left, right)
