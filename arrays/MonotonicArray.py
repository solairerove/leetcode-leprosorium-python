from typing import List


# O(n) time | O(1) space
def is_monotonic(self, nums: List[int]) -> bool:
    is_increasing = is_decreasing = True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            is_increasing = False

        if nums[i] < nums[i + 1]:
            is_decreasing = False

    return is_increasing or is_decreasing
