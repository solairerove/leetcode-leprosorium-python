from typing import List


# O(log(n)) time || O(1) space
def search(self, nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        curr = nums[mid]
        if curr < target:
            low = mid + 1
        elif curr > target:
            high = mid - 1
        else:
            return mid

    return -1
