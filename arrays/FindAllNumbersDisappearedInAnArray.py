from typing import List


# O(n) time || O(1) space
def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1

    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res
