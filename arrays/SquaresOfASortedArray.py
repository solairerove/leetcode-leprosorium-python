from typing import List


# O(n) time || O(n) space
def sorted_squares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    low, high, pos = 0, n - 1, n - 1
    while low <= high:
        if abs(nums[low]) > abs(nums[high]):
            res[pos] = nums[low] * nums[low]
            low += 1
        else:
            res[pos] = nums[high] * nums[high]
            high -= 1
        pos -= 1

    return res
