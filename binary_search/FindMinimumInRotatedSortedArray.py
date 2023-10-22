from typing import List


# O(log(n)) time || O(1) space
def find_min(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[high]
