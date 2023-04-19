from typing import List


# O(n) time || O(n) space
def number_of_arithmetic_slices_top_down(self, nums: List[int]) -> int:
    self.res = 0

    def dp(i):
        if i < 2:
            return 0

        ap = 0
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            ap = 1 + dp(i - 1)
            self.res += ap
        else:
            dp(i - 1)

        return ap

    dp(len(nums) - 1)

    return self.res
