from typing import List


# O(n) time || O(1) space
def sort_array_by_parity(self, nums: List[int]) -> List[int]:
    j = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums
