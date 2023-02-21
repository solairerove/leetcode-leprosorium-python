from typing import List


# O(log(n)) time || O(1) space
def single_non_duplicate(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
