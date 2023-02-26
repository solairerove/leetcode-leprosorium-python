from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.sums[i + 1] = self.sums[i] + nums[i]

    # O(1) time || O(n) space
    def sum_range(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
