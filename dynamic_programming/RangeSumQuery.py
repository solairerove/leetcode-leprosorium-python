from typing import List


class NumArray:

    # O(n) time || O(n) space
    def __init__(self, nums: List[int]):
        self.sums = nums
        for i in range(len(nums) - 1):
            self.sums[i + 1] += self.sums[i]

    # O(1) time || O(1) space
    def sum_range(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]
