from typing import List


# O(n) time || O(1) space
def jump(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    jumps, reach, steps = 0, nums[0], nums[0]
    for i in range(1, len(nums) - 1):
        reach = max(reach, nums[i] + i)
        steps -= 1
        if steps == 0:
            jumps, steps = jumps + 1, reach - i

    return jumps + 1


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
