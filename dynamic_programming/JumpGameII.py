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
