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


class NumArrayBIT:

    def __init__(self, nums: List[int]):
        self.tree = FenwickTree(nums)

    # O(log(n)) time || O(log(n)) space
    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    # O(log(n)) time || O(log(n)) space
    def sum_range(self, left: int, right: int) -> int:
        return self.tree.sum_range(left, right)


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * 4 * self.n
        self.build_tree(0, self.n - 1, arr, 0)

    def build_tree(self, low, high, arr, idx):
        if low == high:
            self.tree[idx] = arr[low]
            return

        mid = low + (high - low) // 2
        self.build_tree(low, mid, arr, 2 * idx + 1)
        self.build_tree(mid + 1, high, arr, 2 * idx + 2)
        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]

    def sum_range(self, low, high, idx, left, right):
        if right < low or left > high:
            return 0

        if left <= low and right >= high:
            return self.tree[idx]

        mid = low + (high - low) // 2

        return self.sum_range(low, mid, 2 * idx + 1, left, right) \
            + self.sum_range(mid + 1, high, 2 * idx + 2, left, right)

    def update(self, low, high, idx, pos, val):
        if pos < low or pos > high:
            return

        if low == high:
            self.tree[idx] = val
            return

        mid = low + (high - low) // 2
        if pos <= mid:
            self.update(low, mid, 2 * idx + 1, pos, val)
        else:
            self.update(mid + 1, high, 2 * idx + 2, pos, val)

        self.tree[idx] = self.tree[2 * idx + 1] + self.tree[2 * idx + 2]


class NumArraySegmentTree:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    # O(log(n)) time || O(n) space
    def update(self, index: int, val: int) -> None:
        self.tree.update(0, self.tree.n - 1, 0, index, val)

    # O(log(n)) time || O(n) space
    def sum_range(self, left: int, right: int) -> int:
        return self.tree.sum_range(0, self.tree.n - 1, 0, left, right)
