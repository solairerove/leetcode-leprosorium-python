from typing import List


# O(n) time || O(1) space
def sorted_squares(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    pos = len(nums) - 1
    low, high = 0, len(nums) - 1
    while low <= high:
        if abs(nums[low]) > abs(nums[high]):
            res[pos] = nums[low] ** 2
            low += 1
        else:
            res[pos] = nums[high] ** 2
            high -= 1
        pos -= 1

    return res
