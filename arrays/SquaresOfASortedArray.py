from typing import List


# O(n) time || O(n) space
def sorted_squares(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    low, high = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[low]) < abs(nums[high]):
            sq = nums[high]
            high -= 1
        else:
            sq = nums[low]
            low += 1
        res[i] = sq * sq

    return res


# O(n * log(n)) time || O(n) space
def sorted_squares_sorting(self, nums: List[int]) -> List[int]:
    return sorted(x * x for x in nums)
