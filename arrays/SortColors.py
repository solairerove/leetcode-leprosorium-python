from typing import List


# TODO: two pointers
# O(n) time || O(1) space
def sort_colors(self, nums: List[int]) -> None:
    lt, i, gt = 0, 0, len(nums) - 1
    while i <= gt:
        if nums[i] == 0:
            nums[i], nums[lt] = nums[lt], nums[i]
            i, lt = i + 1, lt + 1
        elif nums[i] == 2:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        else:
            i += 1
