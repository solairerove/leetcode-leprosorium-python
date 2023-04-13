from typing import List


# O(n) time || O(1) space
def jump(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    res, curr_end, curr_far = 0, 0, 0
    for i in range(len(nums) - 1):
        curr_far = max(curr_far, i + nums[i])
        if i == curr_end:
            res, curr_end = res + 1, curr_far

    return res


# O(n) time || O(n) space
def jump_bottom_up(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    dp = [0] * len(nums)
    j = 0
    for i in range(1, len(nums)):
        while j + nums[j] < i:
            j += 1
        dp[i] = dp[j] + 1

    return dp[-1]
