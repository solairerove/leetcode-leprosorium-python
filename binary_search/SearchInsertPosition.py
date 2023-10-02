from typing import List


# O(log(n)) time || O(1) space
def search_insert(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid

    return low
