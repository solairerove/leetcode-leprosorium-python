from typing import List


# TODO: two pointers
# O(n) time || O(1) space
def sort_colors(self, nums: List[int]) -> None:
    lt, i, gt = 0, 0, len(nums) - 1
    while i <= gt:
        if nums[i] == 0:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt, i = lt + 1, i + 1
        elif nums[i] == 2:
            nums[gt], nums[i] = nums[i], nums[gt]
            gt -= 1
        else:
            i += 1
