from typing import List


# O(n) time || O(1) space
def wiggle_max_length(self, nums: List[int]) -> int:
    length = 1
    increasing = None
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] and increasing is not True:
            length, increasing = length + 1, True

        if nums[i] < nums[i - 1] and increasing is not False:
            length, increasing = length + 1, False

    return length
