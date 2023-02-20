from typing import List


# O(log(n)) time || O(1) space
def search(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            return mid

    return -1
