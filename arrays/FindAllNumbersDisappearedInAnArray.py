from typing import List


# numbers are in range of [1..n]
# means we can swap element to their idx position
# then return elements with no idx

# O(n) time || O(1) space
def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
    idx = 0
    while idx < len(nums):
        pos = nums[idx] - 1
        if nums[idx] != nums[pos]:
            nums[idx], nums[pos] = nums[pos], nums[idx]
        else:
            idx += 1

    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res
